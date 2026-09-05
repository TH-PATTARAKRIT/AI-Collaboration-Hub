# 01 — P04 UPSTREAM CAPITALIZATION TRACE

Session: `SMEPLUS-26-09-04-ACC-P04-A2R-REV2-001`
Layer: **2 — audit quarantine**
Status: research evidence. No implementation. No merge.

This file answers one question the three prior Asset packages did not ask:
**by what mechanism does a fixed asset come into existence, and which business
document is the source of truth for the capitalization decision?**

The governing prompt required that no single mechanism be assumed. Seven
candidates were named and each was tested independently.

---

## 1. Declared enumeration

Per the denominator rule, the four elements are declared before any count.

| Element | Declaration |
|---------|-------------|
| **POPULATION** | Every installable module in the reference-ERP v18 Enterprise build `20250608` addons root — **790**, being the directories that carry a module manifest — plus the project custom addon set, v18 line — **65 directories**. Total **855**. See §1.2 for how these figures were obtained and what they correct. |
| **PATTERN** | (a) `grep -rn --include='*.py' "account\.asset"` excluding `/i18n/`; (b) `grep -rn --include='*.xml' 'model="account\.asset'`; (c) `grep -rn --include='*.py' "_inherit *= *['\"]account\.asset"`; (d) `grep -rn --include='*.py' -E "asset_model_ids\|create_asset"`; (e) `grep -rn --include='*.js' "account\.asset"`; (f) per-module case-insensitive `asset` probe over the procurement, receipt and expense modules; (g) `grep -rn "ir.cron"` over the asset module. |
| **PATH SET** | `<EV-CODE>/addons/` and `<EV-CUST>/addons/`, both to full depth. |
| **UNIT** | One module that references the asset model; and separately, one code location that instantiates an asset record. |

**Verification that the root is complete:** a search for further addons roots
inside the build returned a single hit, i.e. community and enterprise modules are
merged into one tree. The enumeration is therefore a population, not a sample.

### 1.1 Correction to the denominator, executed

Prior packages and this session's own first draft quoted **797** as a module
population. Executed directly:

| Measure | Count |
|---------|-------|
| Entries a directory listing reports in the reference addons root | 797 (it hides one dotfile; 798 entries exist) |
| Of which are **directories** | **791** |
| Of which carry a module manifest — the **installable-module population** | **790** |
| Entries in the custom addons root | 68 |
| Of which are **directories** | **65** |

The one directory of the 791 that carries **no** manifest is a web-integration
module reduced to an empty translation folder — a module stripped to nothing.
The 790 figure excludes it, and that exclusion is stated rather than silent.
No negative finding in this package changes: the searches covered the whole tree
either way. See `05` §2.1 and `18` `P04-REV-01`.

### 1.2 Result of the enumeration

Of the 855 modules, **five** reference the asset model at all:

| Module | Layer | Relationship to the asset record | Creates an asset? |
|--------|-------|----------------------------------|-------------------|
| the asset module | `EV-CODE` | Owner of the model | **Yes** |
| the loans module | `EV-CODE` | Links assets to a loan through an asset-group dimension; adds two related fields and a smart button | No |
| the project–asset bridge | `EV-CODE` | Counts and filters existing assets by analytic distribution | No |
| the custom equipment-sequence module | `EV-CUST` | Adds an equipment reference field; overrides confirm to stamp an equipment status | No |
| the custom advance-expense-request module | `EV-CUST` | **Manifest dependency only.** Its sole asset reference is a demo record setting the automation flag to "no" | No |

**FACT VERIFIED.** Exactly one module in the estate instantiates an asset record.

### 1.3 The custom advance-expense module — corrected after independent challenge

The earlier statement that this module is a *"manifest dependency only"* whose
sole asset reference is a *"demo record"* was **wrong in both particulars**.

| Claim | Corrected |
|-------|-----------|
| It is a demo record | The file lives in a `demo/` folder, but it is listed under the manifest's **`data`** key. The manifest's **`demo` key is commented out**. **It therefore loads on every install, not only in demo mode.** |
| It contributes no behaviour | It **creates a general-ledger account** — a hard-coded code `555555`, "Employee Advance Expense", expense type, reconcilable — and a service product whose expense account points at it. The record is marked no-update, so it persists |
| Its asset reference is incidental | The account record **explicitly sets the capitalization automation flag** to "no" |

> **P04-F-10 (restated).** Installing this custom module does not merely activate
> the asset engine through a manifest dependency. It **injects a fixed
> general-ledger account into the chart of accounts of every company that
> installs it**, and it **sets that account's capitalization flag from a data
> file**.
> Class: **FACT VERIFIED.** Severity **High** for multi-company deployment.
> Registered `P04-B-41`.

Two consequences for P04:

1. **It is direct evidence for `UC-02` / `UC-04` in §3.1.** The capitalization
   designation is being written by a **data file**, not by an accountant in the
   interface. This package argued that every non-interface write path bypasses
   the interface-only controls; here is one, shipped, in the project's own
   custom estate, writing that exact field.
2. A chart of accounts is **company legal-accounting truth** (`20` §2.1). A
   module that writes into it on install is making a company-scoped accounting
   decision from platform-scoped packaging.

---

## 2. The seven candidate mechanisms, tested

| # | Candidate | Verdict | Basis |
|---|-----------|---------|-------|
| 1 | **Purchase item / purchase order line** | **ABSENT** | No asset reference of any kind found in the procurement modules under the declared path set and pattern. No field, no hook, no instantiation. |
| 2 | **Goods receipt / stock move** | **ABSENT — doubly blocked** | (a) no asset reference found in the inventory or inventory-valuation modules; (b) even if a valuation entry reached the creation hook, it is rejected twice: the hook processes only invoice-type documents, and valuation/interim accounts are of a current-asset type that the eligibility computation deliberately excludes. |
| 3 | **Vendor bill / supplier invoice line** | **PRESENT — the only automatic path** | The creation hook is invoked from the **posting** transition of the accounting document. |
| 4 | **Expense** | **PRESENT, but only as a re-entry into #3, and only for the employee-paid mode** | The employee-paid path builds a vendor-bill-type document, which then flows through #3. The company-paid path builds a document with no invoice type, which the hook filters out. **Company-paid expenses can never auto-capitalize.** |
| 5 | **Manual capitalization** | **PRESENT — three distinct sub-paths** | (a) direct creation from the asset menu; (b) "turn selected journal items into an asset" from posted journal items; (c) "save as model", which creates a second record in model state. |
| 6 | **Construction / WIP accumulation then capitalization** | **ABSENT** | No construction-in-progress or work-in-progress asset model exists under the declared path set. The project–asset bridge only counts assets; it creates none. |
| 7 | **Import / migration** | **PRESENT** | The model is a plain persisted model with no import restriction. A purpose-built migration field for previously-recognised depreciation exists. XML data load is also a live creation path. |
| 8a | **Revaluation creates a child asset** | **PRESENT — a second genuine instantiation point** | The modify wizard, on a net value increase, posts a journal entry and then creates a **child asset whose source document is that system-generated entry**. |
| 8b | Asset split | **ABSENT as an event** | The nearest capability splits **at creation time** — one bill line into N assets — driven by an account-level flag. There is no post-creation split. |
| 8c | Subscription / contract | **ABSENT** | A name match on `subscription` over the reference addons root returns **13** directories (12 excluding a test module); **none** appears in the asset-reference result set. |
| 8d | Lease / IFRS 16 right-of-use | **ABSENT** | No module matching a lease or IFRS-16 naming exists in the population. The loans module, the nearest neighbour, links to assets but creates none. |
| 8e | Copy / duplicate | **PRESENT** | Standard record duplication. The link to the source bill lines is **not copied**, so a duplicate is detached from its origin. |
| 8f | Scheduled / cron creation | **ABSENT** | No scheduled action exists in the asset module. |

All ABSENT verdicts above are to be read as
*"not found under the declared path set using the declared pattern"*.

### 2.1 The headline answer

> **The capitalization source of truth is the posted vendor bill (or a manually
> selected posted journal item). It is never the purchase order, never the goods
> receipt, and never the product.**
> Classification: **FACT VERIFIED.**

---

## 3. Where the capitalization decision actually lives

The designation "this is a capitalizable account" lives **exclusively on the
chart of accounts**. It does not live on the product, the product category, the
journal, the purchase document, or the asset model.

```
account type ∈ {fixed asset, non-current asset}
        │  (eligibility computation)
        ▼
"can create asset"  — COMPUTED, NOT STORED
        │  gates visibility of the whole automation section
        ▼
"create asset"  ∈ { no | create in draft | create and validate }
        │  required, defaults to "no", change-tracked
        ▼
"asset models"  — many-to-many to asset records in model state
        │  change-tracked; MAY BE EMPTY
        ├── "multiple assets per line" — boolean, defaults false
        ▼
asset.model  → asset.fixed-asset-account
```

### 3.1 Six control observations on that chain

| ID | Observation | Class |
|----|-------------|-------|
| **UC-01** | The eligibility flag is **computed and not stored**. It therefore cannot be searched, used in a record rule, or used in a server-side domain without recomputation. Any control that tries to report "which accounts are capitalization-enabled" cannot filter on it directly. | FACT VERIFIED |
| **UC-02** | The requirement that an asset model be attached when the mode is "create and validate" is a **view-level attribute only**. There is no model-level constraint. An ORM write or a data import can therefore set "create and validate" with **no** asset model attached. | FACT VERIFIED |
| **UC-03** | With no asset model attached, the creation loop still runs **once with no model**, producing an asset with **no method, no duration and no depreciation or expense account inherited**. With N models attached, **N assets are created per qualifying line**. | FACT VERIFIED |
| **UC-04** | The depreciation and expense accounts are `required` **in the view only**. The field definitions carry no requirement and there is no model-level constraint. An imported or ORM-created asset can carry blanks; the failure surfaces late, as a database check violation caught and re-raised at confirm time. | FACT VERIFIED |
| **UC-05** | The "multiple assets per line" flag is cleared **only by an on-change** when automation is switched off. An ORM write can leave it set while automation is off. Dormant, but it becomes live the moment automation is re-enabled. | FACT VERIFIED |
| **UC-06** | The model's own configuration is applied **after** insertion, not during it. Where the mode is "create and validate", confirmation runs immediately afterwards and posts the whole depreciation schedule. A misconfigured account therefore produces a fully posted schedule before any human sees the record. | FACT VERIFIED |

**UC-02 + UC-03 + UC-04 together** are the material upstream control finding of
this session: three of the four values that determine every future depreciation
entry are enforced only by the user interface. Every non-interface write
path — import, migration, integration, scripted correction — bypasses all three.
This is directly load-bearing for the migration population described in §6.

---

## 4. The automatic path in detail

**Trigger:** the **posting** state transition of an accounting document — not the
confirmation of any upstream operational document. The hook runs with elevated
privilege.

**Per-line eligibility.** All of the following must hold:

1. the document is of an invoice type;
2. the line's account is of a fixed-asset or non-current-asset type;
3. the account's automation mode is not "no";
4. the line total is non-zero **and positive**;
5. the line has no asset yet and is not a tax line;
6. **not** (the document is a sale-type document **and** the account's internal
   group is the asset group).

### 4.1 A structural consequence of conditions 2 and 6

The internal group is derived from the first token of the account type. Both
eligible account types therefore always yield the asset group. Condition 6
consequently cancels **every** sale-type document that passed condition 2.

> **In this build the automatic path is reachable only from purchase-type
> documents.** The revenue-recognition half of the engine's own description has
> **no live automatic entry point**.
> Classification: **FACT VERIFIED** (from the code path); the *intent* behind the
> exclusion is **UNRESOLVED**.

This matters for P10 — Time-Based Recognition. Any SMEsPlus design that expects
to drive deferred **revenue** through this engine automatically is designing
against a path that does not execute.

### 4.2 What happens to the source journal item

**Nothing.** It is not reversed, not re-classified, not re-posted. It is only
**joined** to the asset through a many-to-many relation table. The source
document is stamped with an "asset move type" of purchase, and a note is written
to the asset's message log.

This is a clean design in one respect — the original accounting is preserved —
and a control gap in another: **the asset sub-ledger and the general ledger are
joined by a relation table, not by a balancing entry.** Nothing in the creation
path proves that the sum of asset cost equals the balance of the fixed-asset
account. See `04_P04_ASSET_TO_GL_MATRIX.md` §5.

### 4.3 Surviving link fields, source document → asset

| Direction | Link | Nature |
|-----------|------|--------|
| journal item → assets | many-to-many, relation table, **not copied on duplicate** | the only durable upstream link |
| asset → journal items | many-to-many, inverse side, **not copied on duplicate** | the only durable upstream link |
| document → assets | **computed, not stored** | not searchable |
| depreciation entry → asset | many-to-one, cascade delete, not copied | this is the **downstream** link, not the source-document link |

### 4.4 The two-hop problem (P01 boundary)

The purchase order and the goods receipt each leave a reference **on the journal
item**, not on the asset. Reaching a purchase order from an asset therefore
requires the two-hop traversal

```
asset → source journal items → purchase order line → purchase order
```

and **that traversal is nowhere materialized on the asset record**.

Consequences, all **FACT VERIFIED**:

- There is no stored field by which "which purchase order produced this asset"
  can be reported, searched, grouped, or made the subject of a record rule.
- If the join to the source journal item is lost — by duplication (§2, 8e), by
  a correction that unlinks lines, or by a migration that creates the asset
  without lines — the upstream trace is **irrecoverable from the asset record**.
- The prompt's mandatory chain *"always trace financial fact to initiating
  business event"* is therefore **not satisfiable by stored data** for assets in
  this build. It is satisfiable only by a live two-hop join, and only while the
  join survives.

This is registered as blocker **P04-B-01**.

---

## 5. The second instantiation point: revaluation creates a child asset

On a net value increase, the modify wizard **first posts a journal entry**, and
**then** creates a child asset whose source journal items are the debit line of
that very entry.

> The child asset's "source document" is a **system-generated journal entry with
> no external business document behind it at all.**
> Classification: **FACT VERIFIED.**

Attributes of the child:

- it carries **no asset model** — method, period and accounts are copied field by
  field from the parent;
- its life is clipped to the parent's remaining life;
- its depreciation start is the wizard date plus one day;
- **it carries no analytic distribution, and neither does the entry that created
  it** — see `06_P04_DEPRECIATION_COST_HANDOFF.md`, finding **P04-F-53**. This is the
  point at which the Boss's 100 % attribution requirement is broken by the
  reference behaviour.

A downward revaluation creates **only** a journal entry and no asset.

---

## 6. Runtime evidence, and what it does and does not establish

Source: `EV-RT`, an ORM read-out captured 2026-08-26 against the UAT database.

### 6.1 What is established

| Statement | Basis | Class |
|-----------|-------|-------|
| The population of asset records in states other than "model", across companies 1 and 2, is **280**, all in company 1. | Unbounded query (`limit 10000`) over the stated domain; returned 280 rows. | **FACT VERIFIED** |
| **All 280** carry **no asset model**. | Same query, grouped. | **FACT VERIFIED** |
| The state distribution is draft 35, running 217, on-hold 1, closed 27. | Per-state counts. | **FACT VERIFIED** |
| **35** of the 280 carry a completely empty account triple. | Same query, grouped by triple. | **FACT VERIFIED** |
| At least **10** asset records carry migration external identifiers under a migration module namespace. | Bounded query — see §6.2. | **FACT VERIFIED, but not a population statement** |

### 6.2 What is NOT established — a declared bound

The external-identifier query in that capture was **restricted to a hand-picked
list of 26 candidate identifiers**. It returned 10 of them. Therefore:

> **The proportion of the 280 assets that originate from migration rather than
> from any other mechanism is NOT established by `EV-RT`.**
> The query's own domain was name-bounded; promoting its result to a population
> statement would be exactly the denominator defect this programme has already
> recorded once.

Classified **UNRESOLVED**. Registered as blocker **P04-B-02**. The closing
evidence is a single unbounded count of asset records grouped by presence and
namespace of an external identifier — a query that takes one execution.

### 6.3 What the capture could not answer at all

The capture's field list contains **12 fields** and does **not** include the
link to source journal items. Therefore:

> Whether any of the 280 assets carries a link to a source vendor bill is
> **not observable** from `EV-RT`. "No upstream link observed" would be a false
> negative produced by the capture's own field selection, not a finding.

Classified **UNRESOLVED** *for `EV-RT`* — and **SUPERSEDED for a different
population**: §6A.3 answers it against database `iSMEs`, where **647 of 669
non-template assets (96.7 %) carry no source-document link at all**. What remains
unresolved is `idemo18_uat` specifically. Registered as blocker **P04-B-03**,
which now carries both states.

*This paragraph said only "UNRESOLVED" for one commit after §6A was written. A
reader arriving here would have read a superseded boundary — the same defect P07
found in its own package on the same day, and the reason the rule is* **a
revision log is not a correction; the edit is** *(`18` `P04-REV-25`).*

### 6.4 The one inference that is safe, and why it is only an inference

The controlled model list in `EV-HND` shows 16 asset models already normalised
in the target, while `EV-RT` shows **all 280 live assets carrying none of them**.
A population created by the automatic vendor-bill path with a configured account
would carry the account's attached model. A population created by import would
not.

> **SUPPORTED INTERPRETATION:** the live asset population was created by a path
> that does not attach an asset model — import/migration and/or manual creation —
> rather than by the automatic vendor-bill path.
> This is **not** FACT VERIFIED: manual creation without a model, and automatic
> creation from an account with no model attached (§UC-03), produce the same
> observable. Three mechanisms remain consistent with the evidence.

---

## 6A. DATABASE EVIDENCE — obtained after this package declared it unavailable

This section exists because a peer process proposed a clause — *a statement that
something is unavailable to this session is a capability claim, and a capability
claim is evidence: test it before relying on it* — and applying it to this
package's own declared deviation found the deviation false. See `18`
`P04-REV-21`. The evidence below was one directory listing away for the whole
session.

### 6A.1 What was found

**Ten archive files on the host — seven distinct snapshots of five distinct
databases — and every one carries fixed-asset table data.**

**Corrected three times, each time after a peer's warning — `18` `P04-REV-23`,
`P04-REV-24`, `P04-REV-35`.** The first version of this table reported **four**
dumps, one of them with *"no asset table data"* — a **false negative from the
tool** — and the search that found the four was **bounded to one directory**.
The second reported **five**, from a scan by magic bytes. The third, executed on
two archive signatures and keyed on `database.uuid`, reports **seven snapshots /
five identities**. *Each correction was found by a peer, none by this package.*

| Database | Dated | Archive | Reads under host default client (16.15)? | Generation signature | Asset rows | Of which **real** |
|----------|-------|---------|------------------------------------------|----------------------|------------|-------------------|
| `iSMEs` `45a8e08e` | 2026-07-11 | v1.14 | **yes** | **v16** — carries an `asset_type` column the v18 source tree does not define | **685** | **669** |
| `iEVING` `1f6338ae` | 2026-07-23 | v1.14 | **yes** | **v19** — no `asset_type` | 36 | **0** |
| `iEVING` `f4a44cce` | 2026-03-30 | **zip** (`dump.sql` + `manifest.json`) | **yes**, no client needed | **v19** — `manifest.json` states `version_info [19,0,0,'final',0,'e']`, 179 modules | 12 | **0** |
| `BK12MAY26` `66d1b52a` | 2026-08-03 05:48 | v1.14 | **yes** | **v19** | 36 | **0** |
| `BK12MAY26` `66d1b52a` | 2026-08-03 11:28 | **zip** | **yes**, no client needed | **v19** — manifest, 251 modules | 36 | **0** |
| `iTEST02` `a1430edc` | 2026-07-14 | **v1.16** | **NO** — needs `postgresql@18` | **v19** | 12 | **0** |
| `iTEST02` `a1430edc` | 2026-06-14 | **v1.16** | **NO** — needs `postgresql@18` | **v19** | 12 | **0** |

**Rows are keyed on `database.uuid`, read from `ir_config_parameter` in each
archive — not on the file name.** The two artefacts named `iEVING` are **two
different databases**; the two named `BK12MAY26` are **one**. Reported by P07 and
re-derived here from the archives before adoption.

**The enumeration behind this table was re-run by a stricter method, after P07
reported the same bound in its own** (`18` `P04-REV-27`). The first search matched
on **file extension** at **bounded depth**; the re-run matched on the archive's
**magic bytes**, any extension, any depth, over both trees.

| Measure | Count | Unit |
|---------|-------|------|
| Files | **10** | one file on disk; `iTEST02` @ 2026-06-14 exists in **four** copies across trees |
| **Snapshots** | **7** | one database captured at one moment |
| **Database identities** | **5** | `45a8e08e` (v16), `1f6338ae`, `f4a44cce`, `66d1b52a`, `a1430edc` — the unit every independence claim below uses |

**This census was wrong twice, and the correction came from P07 both times.**

- **Format.** The re-run described below matched *"the archive's magic bytes"* —
  but it matched **one signature**, `PGDMP`. Two of the seven snapshots are
  **`.zip` containers holding `dump.sql` + `manifest.json`**, and a zip does not
  begin `PGDMP`. So the fix for an extension-bounded search was itself
  **pattern-bounded**, and excluded two databases. *An enumeration by magic bytes
  is only as complete as the set of signatures it enumerates.*
- **Identity.** The identity unit was the **file name**. Keyed on
  `database.uuid`, the name is wrong **in both directions at once** — it splits
  one database into two and merges two into one.

**Exclusion errors are invisible by construction.** An over-inclusive count
leaves the wrong row on the page to be checked; an under-inclusive one leaves
nothing at all. No control in this package looks for members that are absent —
neither the orphan check, nor the structural check, nor the independent review.
What found it was a peer publishing a table with a name in it that this package
had never opened.

> **P04-F-86.** **This package's database evidence base was under-enumerated
> twice, and both failures were in controls it had already adopted as remedies.**
> Published census: *8 files · 5 snapshots · 4 database identities*. Executed
> census: **10 · 7 · 5**.
> - **Format.** The remedy for an extension-bounded search (`18` `P04-REV-27`)
>   was a scan *"by magic bytes, any extension, any depth"* — matching **one
>   signature**, `PGDMP`. Two snapshots are `.zip` containers holding `dump.sql`
>   + `manifest.json`. **An enumeration by magic bytes is only as complete as the
>   set of signatures it enumerates.**
> - **Identity.** The identity unit was the **file name**. Keyed on
>   `database.uuid` (read from `ir_config_parameter` in each archive) the name is
>   wrong **in both directions at once**: two artefacts named `iEVING` are **two
>   databases** (`f4a44cce`, `1f6338ae`); two named `BK12MAY26` are **one**
>   (`66d1b52a`).
>
> **The headline total was right by arithmetic accident.** `96` was published as
> `36+36+12+12` over *"three identities"*; the true composition is `36+12+36+12`
> over **four** — a **double-count of `a1430edc`** and an **omission of
> `f4a44cce`**, **12 each, in opposite directions**. *A total that survives a
> correction to its own unit has not been confirmed by surviving; it has only
> failed to move.*
>
> **Exclusion errors are invisible by construction**, which is the transferable
> part: an over-inclusive count leaves the wrong row on the page to be checked;
> an under-inclusive one leaves nothing. No control in this package looks for
> **absent members** — not the orphan check, not the structural check, not the
> independent adversarial review, all of which passed over this. What found it
> was **P07 publishing a table naming a database this package had never opened.**
>
> Class: **FACT VERIFIED**. Reported by P07; **re-derived here before adoption** —
> uuid extracted from all seven snapshots, asset counts re-run on all seven.
> Effect on conclusions: **`P04-F-83` and `P04-F-84` both strengthen**; no
> finding is withdrawn.

**Population ranked before selection — checked retrospectively, and the result is
luck rather than method.** P07 found it had built an entire runtime section on the
**smallest** database available (23 accounting lines against another's 447,384)
because that one sat inside its declared path set and so was opened first — and
named the corrective as *rank the population before choosing*, not *open more*.
Tested here:

| Snapshot | Asset rows | Real (non-template) |
|----------|-----------:|--------------------:|
| **`iSMEs`** `45a8e08e` | **685** | **669** |
| `1f6338ae` | 36 | 0 |
| `f4a44cce` | 12 | 0 |
| `66d1b52a` ×2 | 36 each | 0 |
| `a1430edc` ×2 | 12 each | 0 |

**And "rank the population" needs its own declared unit.** P07 ranked with P11
and the order **inverted**: one database is largest by bytes and rows, the other
has **more than twice the populated tables** — one is the **broadest module
install**, the other the **deepest data set**. So the rule invented to fix an
undeclared unit silently requires one. **Rank by the unit the claim needs:
population claims want depth, configuration claims want breadth.**

`P04-F-82` is a **population** claim and rests on `iSMEs` — the **largest**
population and **the only one containing real assets at all**. So the selection was **forced by the data**, not
chosen for convenience. **Recorded as luck, not method:** this session did not
rank before reading; it read the largest file first and the ranking only exists
because it was executed afterwards, at a peer's prompting. The rule is adopted
prospectively.

**No sixth database exists** under the stricter method, so `P04-F-83` is not
resting on a missed artefact. Two bounds were tested rather than assumed: the
extension filter **did** cost coverage in principle and **not** in fact, and a
minimum-size filter cost nothing — **no archive on either tree is under 1 MB**.

**Readability is per artefact, not uniform** — adopted from P11, which found the
same split from the other side. *"Database evidence is available"* and *"no
database access"* are **both wrong**; the true statement is per file.

**And the caveat must say what a reader would wrongly conclude, not merely what
they would miss.** Sharpened by P07, whose own case inverts: **both** databases
in which its headline defect fires are the two a default client **cannot** open,
so a reader reproducing it with stock tooling opens only the deployments where
the defect is **absent** and would reasonably conclude P07 is **wrong**. A
coverage footnote would not have warned them.

Tested here, finding by finding:

| Finding | Rests on | Stock-tooling reader sees | Conclusion |
|---------|----------|---------------------------|------------|
| `P04-F-81` convention split | 5 readable + 2 needing `postgresql@18` | 108 of 144 template rows, all `constant_periods`; 683/685 real assets on daily | **holds** |
| `P04-F-82` source-link 96.7 % | **one readable archive only** | everything | **fully reproducible** |
| `P04-F-83` zero real assets | 4 readable + 2 needing `postgresql@18` | 4 of 6 v19 snapshots, 3 of 4 v19 identities, **zero real assets in every one** | **holds — and on more evidence than when written** |

*Counts in this table were restated at `18` `P04-REV-35`: they were written
against five snapshots and are now against seven. The **two `.zip` archives need
no PostgreSQL client at all**, so the correction moves the stock-tooling reader's
coverage from 3 of 5 snapshots to **5 of 7** — the caveat weakens in the reader's
favour, which is the direction a coverage caveat is least likely to be re-checked
in.*

> **No finding in this package depends on an artefact a default client cannot
> open.** A reader with stock tooling reaches **the same conclusion on all
> three**, from less evidence. That is the opposite of P07's position and is
> stated because the caveat is only useful if it is specific about which way it
> cuts.

**Scope, stated before any finding — and CORRECTED, because the generation labels
were wrong.** None of these is `idemo18_uat`, the database the runtime capture in
§6 came from, so nothing here closes a blocker that names it.

**The generations were declared from a single structural signal** — the presence
of a column the v18 source tree does not define — and **never checked against the
installed-module version record.** Executed against `ir_module_module`:

| Identity | Installed modules | Generation |
|----------|------------------:|------------|
| `iSMEs` | 189 | **v16** |
| `iEVING` | 232 | **v19** |
| `BK12MAY26` | 251 | **v19** |
| `iTEST02` | 461 | **v19** |

> **P04-F-85.** **No database on this host is the same generation as the source
> tree these behavioural findings rest on.** The source is **v18**; the databases
> are **v16** (one identity, the only one holding real assets) and **v19** (three
> identities, templates only). The package previously labelled the v19 databases
> *"v18-line"* and `iSMEs` *"an older generation"* — the first is **wrong**, the
> second understates a **two-generation** gap.
> Class: **FACT VERIFIED** from the module version records.

**What this changes and what it does not.** Every *count* below stands — the
records were read correctly. What was wrong is the **generation each population
belongs to**, and therefore **which source-code findings it can be set against**:

- Statements about **v19 deployments** (templates, absence of real assets) are
  statements about the **deployment target**, and remain directly relevant.
- Statements drawn from **v18 source** cannot be corroborated by any database
  here, because **no v18 database exists on this host**. The Runtime → Database
  leg of the semantic trace is therefore **weaker than this package previously
  declared** — see `17` deviation 1.

Every statement below is bounded to the identity **and generation** named in it.

*An earlier version of this paragraph read "two of the three are a different
product generation". It was **wrong when written** — one of the three then read
was the older generation, not two — and **stale thereafter**, once seven snapshots
had been read. Both errors sat in the scoping paragraph that governs the whole
section. Corrected under `18` `P04-REV-31`.*

### 6A.2 The day convention, across generations

| Database | Generation | `constant_periods` | `daily_computation` |
|----------|-----------|-------------------|---------------------|
| `45a8e08e` `iSMEs` — 669 real + 16 templates | **v16** | **2** | **683** |
| — *of which its 16 **templates*** | v16 | **1** | **15** |
| `1f6338ae` `iEVING` @ 2026-07-23 — 36, all templates | **v19** | **36** | 0 |
| `f4a44cce` `iEVING` @ 2026-03-30 — 12, all templates | **v19** | **12** | 0 |
| `66d1b52a` `BK12MAY26` @ 2026-08-03 05:48 — 36, all templates | **v19** | **36** | 0 |
| `66d1b52a` `BK12MAY26` @ 2026-08-03 11:28 — 36, all templates | **v19** | **36** | 0 |
| `a1430edc` `iTEST02` @ 2026-07-14 — 12, all templates | **v19** | **12** | 0 |
| `a1430edc` `iTEST02` @ 2026-06-14 — 12, all templates | **v19** | **12** | 0 |
| **v19 total, per snapshot** | | **144 — 100 %** | **0** |
| **v19 total, per identity** (one snapshot each) | | **96 — 100 %** | **0** |

*The row labels in this table read `v18` until this revision — a survivor of the
generation correction (`18` `P04-REV-33`) sitting in a table whose own total row
already said `v19`. Sixth survivor of that correction; found by re-deriving the
table rather than by re-reading it.*

> **P04-F-81.** The operational population runs on **daily computation** (683 of
> 685 in the only database holding real assets), while **every asset template in
> the v19 line — 144 of 144 across six snapshots, 96 of 96 across all four v19
> database identities — is on `constant_periods`** — the
> product default, and the convention the operational population does **not** use.
> Templates govern the configuration of assets created from them. So the
> databases that would seed new assets are seeded with the **opposite**
> convention to the one in production use.
> **This is a compound claim and its two halves rest on different kinds of
> database.** Adopted from P07, which found it had used a *configuration* database
> for *population* claims and had never distinguished the two kinds in one file:
>
> | Half | Kind of claim | Evidence required | Source used |
> |------|---------------|-------------------|-------------|
> | 683 of 685 real assets on daily | **population** | the **deepest data set** | `iSMEs` — the only snapshot with real assets |
> | 96 of 96 templates on `constant_periods` | **configuration** | the **broadest install**, i.e. every snapshot carrying templates | all **six** v19 snapshots, **four** identities |
>
> Each half rests on the right kind, **by construction rather than by design** —
> the population half had only one candidate and the configuration half was
> enumerated exhaustively. The split is stated because the finding did not
> previously say which evidence supported which half, and a reader could not have
> told.
>
> Class: **FACT VERIFIED**. Population half bounded to `iSMEs`; configuration half
> bounded to the **six v19 snapshots across four identities**. Enumeration
> of candidates at §6A.1.

> **P04-F-84.** **A stronger statement the split makes available, and which the
> single sentence concealed.** The configuration half is not *"the templates are
> on the product default"*. It is **96 of 96 templates on the product default
> across four independent database identities, captured by different operators
> between 2026-03-30 and 2026-08-03** — and **not one** carries the convention the
> operational system actually runs on.
>
> **The total 96 was right by arithmetic accident, and the correction proves it.**
> The published figure was `36 + 36 + 12 + 12` over what it called *"three
> identities"*. Keyed on `database.uuid` the composition is **`36 + 12 + 36 + 12`
> over four** — the old sum **double-counted `a1430edc`** (the same database
> captured twice) and **omitted `f4a44cce`** entirely, and the two errors are
> **12 each, in opposite directions**. Same total, wrong denominator, wrong
> membership. *A total that survives a correction to its own unit has not been
> confirmed by surviving; it has only failed to move.* Registered as `P04-F-86`.
>
> So this is not an oversight in one deployment. **No v19 deployment
> examined has ever changed the day convention from the shipped default, at any
> point across roughly seven weeks, by any operator** — while the only population
> of real assets in existence runs on the other convention. Combined with
> `P04-F-83` (the v19 line has never had an asset created in it) the migration
> exposure is stated at full strength: **the first asset ever created in the
> target generation will inherit the wrong convention, and nothing in any
> deployment's history suggests anyone would notice** — the two conventions agree
> annually to within 0.05 %.
>
> **And the contrast is not v19-versus-nothing — it is a live counter-example.**
> The one identity that has real assets, `45a8e08e`, **also carries templates —
> 16 of them — and 15 are on `daily_computation`.** So the install that went on to
> transact **did** move its templates off the shipped default; the four that never
> transacted never did. The claim is therefore not *"nobody changes this
> setting"* but the sharper **"every install that used assets changed it, and no
> install in the target generation has"** — which is what makes the first asset
> created in the target generation the exposure.
>
> > **P04-F-87.** **The one database that has real assets also moved its
> > templates off the shipped default; not one database in the target generation
> > has.** `45a8e08e` holds **16 templates, 15 of them `daily_computation`** —
> > alongside 683 of 685 real assets on the same convention. The four v19
> > identities hold **96 templates, 96 on `constant_periods`**, zero real assets.
> > So the day-convention exposure is not *"a setting nobody changes"*: it is a
> > setting **every install that actually used assets did change**, and that **no
> > install in the generation this project is migrating to has ever reached** —
> > because none has ever created an asset (`P04-F-83`). The counter-example is
> > what gives the claim its force, and it was **not visible until the census was
> > re-derived per identity**.
> >
> > Class: **FACT VERIFIED**, bounded to the five identities enumerated at §6A.1.

> **P04-F-88.** **The exclusion of `idemo18_uat` from the evidence base was
> asserted from *file names* and never verified — and it is true.** `BLK-01` and
> `P04-B-03` both stay open on the stated ground that the database the runtime
> capture names *"was not among the accessible dumps"*. That was read off the
> filenames. Tested properly — `pg_restore -l` header `dbname:` for the five
> `PGDMP` archives, `manifest.json` → `db_name` for the two zips — the internal
> names are `iSMEs`, `iEVING` ×2, `BK12MAY26` ×2, `iTEST02` ×2. **None is
> `idemo18_uat`**, and no artefact under either tree carries `demo` or `uat` in a
> database-archive name. The exclusion **holds**, and both blockers stay open for
> the reason given.
>
> **Recorded although it survived**, on P07's rule (`REV-E-44`): a *negative
> about the evidence base* needs the **same authority** as a negative about the
> subject. P07 found the same class in its own population and its exclusion was
> **false** — a database excluded as *"different product line"* that was the
> declared generation all along. The dangerous property is shared regardless of
> outcome: **an exclusion furnished with a stated reason stops the audit that
> would have checked it.** Mine was right by luck of the naming convention, not
> by verification, and a reader could not have told the difference.
>
> Class: **WITHDRAWN — the claim it supported is false.** See `P04-F-90`.
>
> **The negative as literally worded survives and is worthless.** *"No archive
> under `~/Downloads` or the SMEsPlus tree has internal database name
> `idemo18_uat`"* is still true. **`idemo18_uat` is on this host** — at
> `~/OCC_BACKUP/`, one directory away from a path set **I chose and never
> declared**. The exclusion that kept two blockers open was therefore **false in
> use** while **true as written**, which is the worst combination available: a
> reader auditing it would have confirmed it.
>
> This finding was registered **as an application of P07's exclusion-authority
> rule**, and it verified the wrong thing. I checked the *authority* of the
> exclusion — internal `dbname` rather than filename — and never checked its
> **path set**. *Raising the authority of a statement about a population does
> nothing for a population that was drawn wrongly.* And the rule that governs
> this exact defect is one this package has stated eleven times: **POPULATION +
> PATTERN + PATH SET + UNIT, none author-chosen.** The path set was author-chosen
> and undeclared, in a finding written to demonstrate rigour about exclusions.

### 6A.4 The database the blockers name — found, read, and it is v18

> **P04-F-90.** **`idemo18_uat` is on this host, it is a v18 deployment, and it
> holds 388 real assets.** Archive
> `~/OCC_BACKUP/idemo18_uat_pre_scgl_occ_website_20260830_085432.dump`,
> `PGDMP`, 45.6 MB, dated **2026-08-30** — later than every archive previously
> enumerated. Internal `dbname: idemo18_uat`; `database.uuid`
> `551ab874-9acb-11f1-b150-6ec7a480be3d`; **`base` `18.0.1.3`**, `account`
> `18.0.1.3`, **`account_asset` `18.0.1.0` installed**, 361 installed modules.
> Requires `postgresql@18`; the host default client cannot open it.
>
> **This falsifies the headline of `P04-F-85`.** That finding said *"no database
> on this host is the same generation as the source tree at all"* and, on it,
> `17` §5 deviation 1 declared the **Runtime → Database leg weaker than
> previously stated**. There **is** a v18 database on this host, it is the one
> the runtime capture names, and it carries a **real, transacted asset
> population**. The leg is **materially stronger**, not weaker — and the
> behavioural findings in this package now have a same-generation deployment to
> be set against. `P04-F-85`'s **method** point stands unchanged: the generation
> labels were declared from one structural signal and were wrong. Its **scope**
> claim is withdrawn.
>
> Class: **FACT VERIFIED.** Found by running the census with a **declared** path
> set after P07 reported an eleventh artefact outside mine — see `P04-F-88`,
> withdrawn, and `18` `P04-REV-37`.

> **P04-F-91.** **`BLK-01` is answered in the database it names, and the answer
> is the mismatch this package predicted.** Of **388 real assets** in
> `idemo18_uat`: **375 on `daily_computation`, 13 on `constant_periods`**
> (96.6 % daily). Of its **16 templates: 16 on `constant_periods`, none on
> daily.**
>
> So the template-versus-population split of `P04-F-81` is no longer an inference
> across generations — it is **measured inside a single v18 database**, the one
> the blocker names: **every asset it actually runs is on one convention and
> every template it would create the next asset from is on the other.** Third
> population measured, third time the same shape: `iSMEs` v16 683/685 daily,
> `idemo18_uat` v18 375/388 daily, and every template set in every database on
> `constant_periods` except v16's.
>
> **Discrepancy recorded, not smoothed:** `BLK-01`'s close condition names *"the
> 280 records"*. This archive holds **404** asset rows (388 real + 16 templates).
> The runtime capture's figure and the archive's do not agree, and this package
> cannot say which moment either describes. The count is published against the
> archive, dated, and the blocker is **ANSWERED — NOT CLOSED** for that reason.
>
> Class: **FACT VERIFIED**, bounded to `551ab874` @ 2026-08-30.

> **P04-F-92.** **`P04-B-03` answered for the v18 database, and the answer is
> total.** `asset_move_line_rel` **exists in the archive and holds no rows** — so
> **0 of 388 real assets in `idemo18_uat` carry a link to the journal item that
> created them.** Positive control run in the same command: `account_asset`
> extracts **404** rows from the same archive by the same method, so the empty
> result is **absence of data, not a failed extraction** (the defect recorded at
> `18` `P04-REV-23`).
>
> Against `iSMEs` (v16): **22 of 669 linked, 647 unlinked (96.7 %)**. In the v18
> deployment the figure is **0 of 388 — 100 %**. `P04-B-01` moves from a design
> gap, to a measured gap, to a gap **measured at totality in the target
> generation**.
>
> Class: **FACT VERIFIED**, bounded to `551ab874` @ 2026-08-30. **Narrowed at `P04-F-104`**: the link mechanism works — **6 of 7** real assets are linked in a second v18 identity — so this zero is a property of *this* deployment, not of the design.

### 6A.20 A correction that reached two files and not the other five

P07 asked *why* one identifier carried definition-shaped rows in five files, and
the question — not the check — found **fifteen stale restatements**: before/after
tables whose *"after"* column had itself been superseded, in a package whose
phrase-greps had passed, **because each row states the same figure in different
words**. Run here as an identifier-level check over every finding this package has
narrowed.

> **P04-F-119.** **`P04-F-100` narrowed `P04-F-99` in two files and left it
> standing in five.** When a second v18 identity was found with **9 analytic
> accounts**, where the netting fires **14 of 14**, the latency claim was
> corrected in `19` — the Layer-1 pack, twice — and in `10`. It was **not**
> corrected in `06` (twice), `09`, `11`, `16` or `20`, each of which still read
> that the dimension is empty *"in the only v18 deployment"*.
>
> By then there were **three** v18 identities and the phrase *"the only v18
> deployment"* had been false for six commits.
>
> **Five corrections applied**, and the replacement is stronger than a date fix:
> `BD-02` is now stated as **breached in both deployments by two different
> mechanisms** — *absence* where the dimension is empty, *cancellation* where it
> is populated — with the consequence that **a design that fixes one does not fix
> the other**. That distinction was implicit in `P04-F-100` and stated nowhere a
> reader of `09` would find it.
>
> **Why every earlier sweep missed it.** This package has run phrase-greps for
> propagation four times (`18` `P04-REV-29`/`-31`), and they search **wordings**.
> These five rows say *"the only v18 deployment"*, *"in the only same-generation
> deployment"*, *"one plan, zero accounts"* and *"latent"* — **four wordings of
> one superseded figure.** The identifier-level check finds them because it asks
> *which citations of `P04-F-99` lack the qualifier `P04-F-100` added*, and that
> question is indifferent to phrasing.
>
> **Fifth occurrence of the propagation class here, and the first found by
> identifier rather than by phrase.** The rule this replaces the phrase-grep with:
> **when a finding is narrowed, enumerate its citations by identifier and require
> the qualifier on each — never grep for the old wording, because the wording is
> what varies.**
>
> Class: **FACT VERIFIED**, 25 citations of 8 narrowed findings audited, 5
> genuinely stale, corrected; the remainder are defining blocks stating a claim
> before their own qualification, or revision-log rows recording history.

### 6A.19 Which findings carry the exposure

`P04-F-116` partitioned the **models**. P07 went one step further and partitioned
its **findings**, which is what a reader actually needs — and reported the first
finding it holds sitting on **opposite sides** of the copy-identity and
stack-completeness questions. Done here for all 116.

> **P04-F-118.** **Six substantive findings carry the unreadable-stack exposure;
> the asset core does not.**
>
> | standing | findings | basis |
> |---|---:|---|
> | **Complete declared stack** | **27** | `account.asset` — no installed module outside the declared scope (`P04-F-116`) |
> | Partly exposed — `account.move`/`.line` | 25 | 3 and 2 undeclared modules declare there |
> | Partly exposed — `account.account` | 2 | `scgl_account_coa_control`, readable but unread |
> | **Exposed — unreadable member** | **6** | `maintenance.equipment` carries `equipment_fleet`, **no source on this host** |
> | Not model-bound | 56 | method, census and governance findings |
>
> The six exposed: **`P04-F-35`, `-37`, `-38`, `-39`, `-40`** — the
> asset-to-equipment relationship findings in `05` — and **`P04-F-108`**, the
> on-change forcing. **These are the findings a reader should treat as resting on
> an incompletely readable stack, and they are the only ones.**
>
> **The classifier over-reported and was corrected before publication.** Its first
> run returned **12**, because it assigns by the model vocabulary a finding's text
> uses — and six of the twelve (`P04-F-94`, `-97`, `-102`, `-107`, `-114`, `-116`)
> are **method** findings that merely *name* equipment while describing a census
> or a check. **That is precisely the name-driven assignment this package
> criticised at `P04-F-114`**, committed in the instrument built to apply
> `P04-F-116`, and caught only by reading the six defining blocks.
>
> **Declared bound:** the partition is assigned from each finding's **defining
> block**, by business-language vocabulary, with the twelve equipment hits read
> individually. It is a **reader's guide, not a proof** — a finding classified
> *complete* rests on `account.asset` having no undeclared module **declaring** on
> it, which `P04-F-116` already states is a floor rather than a ceiling.
>
> Class: **FACT VERIFIED** as to the partition, **bounded** as stated. No
> finding's content changes; what changes is that a reader can now tell **which
> six** to discount and which twenty-seven not to.

### 6A.18 Two registers under one family name

P07 ran *count the forms, not the identifiers* over its own families and found
that two of its three dual-form entries **were not two forms of one family — they
were two different families colliding on one stem**, one meaning a module
dependency and the other the tax invoice. Every check it owns reported both
clean, because both had definition rows: **the collision is semantic, not
structural.** Run here, the same view finds two, and one is three-way.

> **P04-F-117.** **`P04-LAW` was two registers under one name, and a third
> register collided with it numerically.**
>
> | identifier | file | what it is |
> |---|---|---|
> | `P04-LAW-A`…`H` | `13` | **statutory sources** — the manual, ป.79/2541, ป.84/2542, the ruling, the VAT announcement |
> | `P04-LAW-01`…`06` | `07` | **legal conclusions** — *"a VAT-registered person selling a fixed asset is making a sale of goods"* |
> | `LAW-01`, `LAW-02` | `13` | **P3's inherited sources** — ม.65 ทวิ(2), พ.ร.ฎ. 145 |
>
> So one family name carried **a source register and a conclusions register**,
> distinguished only by whether the suffix was a letter or a digit, and the
> digits then collided with an inherited family holding sources again. **A reader
> meeting `P04-LAW-01` had no way to know it was a conclusion rather than a
> source, and `LAW-01` beside it is a source.** Every identifier resolved; two
> resolved to different *kinds* of thing under one stem.
>
> **The conclusions are renamed `P04-LC-01`…`06`** — 9 occurrences, one file —
> **with the source family counted before and after as the control: 22 and 22.**
> Renaming was correct here because both families are this package's own.
>
> **`CTR` is the second, and it is fixed the other way.** P3's `CTR-01`…`06` and
> this session's `P04-CTR-01`…`07` **occupy the same numbers with entirely
> different content** — P3's `CTR-01` is the unimplemented depreciation method,
> this session's is three enumerations of one population disagreeing. Here a
> rename would **break lineage to P3**, so the inherited identifiers are left
> untouched and **attributed instead**: written `P3 CTR-nn` outside their
> register, with a note on the register section itself. Same for `LAW-01/02`.
>
> **Rename what is yours; attribute what is inherited.** The choice is not
> stylistic — renaming an inherited identifier destroys the only link back to the
> package that raised it.
>
> **And this is invisible to every check in the sweep, by construction.** The
> identifier check, the structural check, the manifest check, the scrub and the
> sentinel are all satisfied: both families are defined, every citation resolves.
> **Counting forms per family is the only view in which a stem collision appears
> at all**, and no amount of re-reading substitutes for it — the credit is P07's.
>
> **Sweep unit `1c` added — stems carrying two families with overlapping numbers
> — and its first run reports five, all declared:**
>
> | stem | families | disposition |
> |---|---|---|
> | `LAW` | `P04-LAW`, `LAW` | **renamed** (`P04-LC`) + inherited **attributed**; the residual digits under `P04-LAW` are this finding **quoting the old identifiers** |
> | `CTR` | `P04-CTR`, `CTR` | inherited **attributed** `P3 CTR-nn`; rename refused to preserve lineage |
> | `B` | `P04-B`, `B` | declared quotations at §6A.13 / §6A.16 |
> | `REV` | `P04-REV`, `REV` | `REV-03` attributed to **P2** |
> | `E` | `P11-E`, `E` | attributed elisions of **P11's** identifiers |
>
> **The check flags any sixth.** And the fifth row is the recursion again — this
> finding cannot say *"`P04-LAW-01`…`06` were legal conclusions"* without writing
> those identifiers, which re-creates the overlap it documents. Declared as a
> bound, per §6A.16, rather than chased to zero.
>
> Class: **FACT VERIFIED**, two collisions, one renamed with a control, one
> attributed; **no finding's content changes** — what changes is that two
> registers no longer share a name.

### 6A.17 Copy-identity is not stack-completeness

P07 found its own closure narrower than the use its citations were being put to:
a module **outside its declared path set** overrides the very method one of its
findings turns on, calling `super()` first and post-processing the result. Its
rule — **a claim discharged against the right module is not discharged against
the deployed stack.** `P04-F-102` closed the *copy-identity* question for
`equipment_sequence`. It never asked what else is installed on the same models.

> **P04-F-116.** **The model this entire package turns on has a complete declared
> stack; the model beside it does not.** Every installed module declaring fields
> or views on each model, checked against both declared roots:
>
> | model | modules declaring | outside both declared roots |
> |---|---:|---|
> | **`account.asset`** | 6 | **none** |
> | `maintenance.equipment` | 6 | **`equipment_fleet`** |
> | `account.account` | 10 | `scgl_account_coa_control`, `accessories` |
> | `account.move` | 28 | `account_invoice_fixed_discount`, `sale_fixed_discount`, `scgl_signature` |
> | `account.move.line` | 13 | `accessories`, `account_invoice_fixed_discount` |
>
> **The positive result first, because it is the one that matters most and this
> package has not been able to say anything like it before.** On **`account.asset`
> itself — the model every capitalization, depreciation, revaluation and
> derecognition finding here turns on — no installed module lies outside the
> declared source scope.** The six are the reference asset module, its fleet
> bridge, the loans module, two framework mixins, and this package's own
> `equipment_sequence`. Whatever `P04-F-93` established about the *estate's* 27
> undeclared modules, **none of them declares on the asset model.**
>
> **`P04-F-102` is qualified, not withdrawn.** It closed *which copy of
> `equipment_sequence` is deployed*. It did not close *what else acts on
> `maintenance.equipment`* — and **`equipment_fleet` does, from outside both
> declared roots, with no source anywhere under `/Volumes` or `$HOME`**
> (`P04-F-94`). So the asset–equipment findings in `05` rest on a stack with one
> unreadable member, while the pure asset findings do not. **That distinction did
> not exist in this package until the question was asked in P07's form.**
>
> **The one-directional limit still binds and is the reason this closes nothing.**
> `ir_model_data` sees declarations carrying an XML id. A module can override
> `create`, `write` or `_post` on `account.asset` with no field and no view and
> appear nowhere in the table above. **"None outside the declared roots" is a
> floor on the declared stack, not proof of a complete one** — and the sharpest
> statement available is: *no undeclared module is shown to act on
> `account.asset`, and none is shown not to.*
>
> Class: **FACT VERIFIED** as to the declarations, **bounded** as stated.
> `P04-B-46` unchanged and still UNRESOLVED.

### 6A.16 The prefix rule created the defect it was written to prevent

> **P04-F-115.** **Requiring the package prefix converted a false positive into a
> silent omission, and the one instance is inside the paragraph that introduced
> the rule.** P07 reported it first, in its own package: its `REV-E-64` fix —
> require `P07-` so a peer's ids are not read as its own — made **eleven bare
> citations of its own findings invisible to its own checker**, while a reader
> mid-exchange could read them as this package's.
>
> Swept here across every family that exists in both bare and prefixed form. Of
> **79** bare citations:
>
> | | |
> |---|---:|
> | families with **no prefixed form** — `BD`, `CTR`, `LAW`, audited under their bare names | 75 |
> | deliberate quotations of the defective form, inside the findings describing it | 3 |
> | **genuine silent omissions** | **1** |
>
> The one is `` `F-81` `` at `01` §6A.13 — **this package's own finding**, written
> bare in the sentence explaining that P07's checker had reported `P07-F-81`
> when the match was a citation of *this package's* `F-81`. **The rule and its
> violation are in the same sentence.** Written out.
>
> **The two defects have one root and each fix creates the other:**
>
> > **An identifier without its package prefix is ambiguous, and requiring the
> > prefix converts a false positive into a silent omission. Neither is safe;
> > only writing identifiers out in full is.**
>
> P07's formulation, adopted verbatim. **The operative rule for this package is
> narrower and worth stating separately**: a family is safe when it has **exactly
> one canonical form** and the check audits that form. `BD`, `CTR` and `LAW` have
> no prefixed form and are audited bare — correctly. The failure mode is a family
> existing in **two** forms, which was true only of `P04-F`/`F`, `P04-B`/`B` and
> `P04-REV`/`REV`. **Count the forms, not the identifiers.**
>
> **The regress is real and this is where it stops.** A **dual-form check** was
> added as sweep unit `1b` — bare citations of any family that also exists in
> prefixed form, minus those carrying attribution. Its first run reported **4**,
> and **all four are quotations of the defective form inside the findings
> describing it** — including one this very finding introduced by quoting `F-81`
> a second time. *Writing about bare identifiers creates bare identifiers.*
>
> The terminating move is **declaration, not further correction** — and it took
> two attempts, both defeated by the act of writing them:
>
> 1. Keyed on **line numbers**: invalidated immediately, because adding the
>    paragraph shifted every line below it. *An allowlist keyed on position is
>    invalidated by the edit that creates it.*
> 2. Re-keyed on **file and count**: also wrong on its first run, because
>    **writing the counts down added one more occurrence of each identifier being
>    counted.**
>
> The declaration is therefore taken **after** the describing text is final, and
> the three quoted identifiers in this file stand at **4, 2 and 2** occurrences.
> The check flags any **increase** on those, or any occurrence in another file.
> This paragraph is written to add none.
>
> **That is the whole shape of the regress in three lines**, and it is not a
> curiosity: a self-describing register changes what it describes, so the only
> stable declaration is one taken last and expressed as a bound rather than a
> list. **A residue that is enumerated is
> not the same defect as a residue that is unknown** — and chasing it to zero
> would require the finding to stop describing what it found.
>
> Class: **FACT VERIFIED**, 79 bare citations classified, 1 corrected, 4 retained
> as declared quotations at `01` §6A.13 and §6A.16, keyed on count rather than
> line number.

### 6A.15 "27 modules wide" was the size of the gap, not the size of the exposure

P07 closed its widest open item by applying two filters in order — **generation
first, then the specific claim** — and turned a 20-tree exposure into 2 candidate
bodies per cited file, all four claims discharged. Its generalisation: **the size
of a diff is not the size of the exposure.** `P04-B-46` was published as *"27
modules wide"*, which is the same kind of number.

> **P04-F-114.** **Of the 27 deployed-but-undeclared modules, 9 declare anything
> on a model this package's findings turn on — and two of the five this package
> named by name declare nothing at all.**
>
> Measured from the deployment rather than from module names: `ir_model_data`
> rows for each module, resolved through `ir_model_fields.model` and
> `ir_ui_view.model` into the **business** models each module actually declares
> fields or views on.
>
> **The first instrument was wrong and a control caught it.** Reading
> `ir_model_data.model` directly gives the model of the *referenced record* —
> `ir.ui.view`, `ir.model.fields` — not the business model, and it reported that
> **one** module in the whole database touches `account.move`. After resolution:
> **28**, and `account_asset` resolves to exactly `account.asset`,
> `account.asset.group`, `account.account`, `account.move`, `account.move.line`.
> Both controls are published because the first number was plausible and wrong.
>
> | | |
> |---|---:|
> | modules deployed and in neither declared root | **27** |
> | of those, declaring on a model this package's findings turn on | **9** |
>
> The nine: `accessories` and `account_invoice_fixed_discount`
> (`account.move`/`account.move.line`), `sale_fixed_discount` and `scgl_signature`
> (`account.move`), **`scgl_account_coa_control` (`account.account`)**,
> `equipment_fleet` (`maintenance.equipment`), `scgl_delivery_cost` and
> `scgl_stock_fleet` (`stock.picking`), `scgl_product_category_company`
> (`product.template`/`product.product`).
>
> **`scgl_account_coa_control` is the one that matters** and it survives the
> narrowing: the capitalization designation lives on the **chart-of-accounts
> account** (`01` §3), and this module declares on `account.account`.
>
> **Two of the five modules this package named by name declare nothing on any
> business model**: `scgl_date_range_auto_period`, which was flagged against the
> silent re-dating finding, and `journal_entries_report`. **Those flags were
> name-driven speculation.** They were published as *pointers, not an
> assessment* — which was the right label — but two of five being wrong is the
> measure of what a name is worth, and it is now measured rather than hedged.
>
> **The bound is one-directional and that must not be lost.** `ir_model_data`
> covers records carrying an XML id. A module can override a method — `write`,
> `create`, `_post` — in Python with **no new field and no view**, and declare
> nothing. So **9 is a floor on what demonstrably touches these models, not a
> ceiling on what could affect them**; the other 18 are *undemonstrated*, not
> cleared. `P04-B-46` stays **UNRESOLVED** and its two source-less modules stay
> **NOT ON THIS HOST**.
>
> Class: **FACT VERIFIED** as to the nine, **bounded** as stated. What changes is
> that the blocker now names **which** modules and **why**, instead of a count.

### 6A.14 The family list was itself an author-chosen population

> **P04-F-113.** **The 14 families audited at `P04-F-111` were hand-picked from a
> list filtered at a frequency floor this package never declared. Enumerated
> without a floor there are 43.** P07 audited **46** and found **26 owned**
> against its own 8 — so its coverage gap was larger than this package's, and
> neither of us found ours without the other stating a number.
>
> The defect is the one this package records more than any other, arriving in the
> **audit of the check itself**: `P04-F-111` declared *"14 owned families"* as
> though the denominator were given. It was **selected** — families appearing
> twice or more, chosen by eye.
>
> Full enumeration, no floor, every identifier-shaped token:
>
> | class | families | note |
> |---|---:|---|
> | **owned — audited** | **17** | 309 citations |
> | **foreign by attribution** | 14 | `P11-*`, `SCP`, `U`, `REV-E`, `P07-F`, `P2 REV`, `HOLD` (prior package), and bare `F` where it means P07's |
> | **not identifiers** | 12 | `TAS-02`, `IFRS-16`, `SHA-256`, `Layer-1`, `Tier-1`, `ERPPLUS-17`, `DBD-01` … |
>
> **Four families had never been checked at all**, the largest being the **event
> register `EV-01`…`EV-24`** — the spine of `03` — together with the use-case set
> `UC-01`…`UC-06`, the specified-query set `Q-10`…`Q-14`, and `HOLD-nn`.
>
> **Result: 309 citations across 17 owned families, one undefined** — the
> intentional withdrawal notice `P04-F-18`. Control: a deliberately absent
> identifier is reported.
>
> **One reclassification.** `HOLD-02`, `HOLD-03` and `HOLD-05` are **prior-package
> identifiers**. `07` attributed one of them (*"from the prior package"*) and `06`
> attributed none, so two citations were indistinguishable from unresolved local
> ids. Attribution added — the same rule already applied to `P2 REV-03` and
> `P07's F-65`. **A foreign identifier without its attribution is an orphan to
> every reader and every checker.**
>
> **And reclassifying `HOLD` moved it out of the audited set**, which is the
> point: a family's class is a **judgement**, and the check must be re-run after
> the judgement changes. The first run of this sweep still listed `HOLD` as owned
> and reported its three ids as orphans **after** the finding above had
> reclassified them — the register and the checker disagreed for one run.
>
> Class: **FACT VERIFIED**, coverage stated: 43 families enumerated, 17 audited,
> 26 classified out with reasons.

### 6A.13 The identifier check covered 2 of 14 families

P07 extended its orphan check beyond the one family it was written for and found
**12 orphans out of 27 cited in the family that carries its HOLD**. Run here.

> **P04-F-111.** **This package's identifier check covered 2 of its 14 owned
> identifier families. Extended to all 14, the genuine orphan count is zero — and
> the extension surfaced three defects in the *check*, not the package.**
>
> Families in use: `P04-F`, `P04-B`, `P04-REV`, `P04-CTR`, `P04-BD`, `P04-PD`,
> `P04-LAW`, `P04-SC`, `BLK`, `D-P04`, `BD`, `CTR`, `CTR-C`, `LAW`. Only the
> first and third were ever checked. **`P04-B` carries this package's HOLD**, and
> it had never been enumerated against its citations.
>
> The first extended run reported **19 apparent orphans. None was genuine:**
>
> | apparent orphans | what they actually were |
> |---|---|
> | `P04-LAW-A`…`H` (8) | defined as **backticked table rows**, not bold |
> | `D-P04-01`…`04` (4) | defined as **`**Disagreement recorded — `D-P04-01`.**`** |
> | `BLK-03`…`06` (4) | defined in **prose**, in the closed-for-lineage section |
> | `SCP-08`, `SCP-09` (2) | **P11's identifiers**, correctly cited and not ours to define |
> | `CTR-C` (1) | a **regex artefact** — family `CTR` matching `CTR-C-01` |
>
> **The package uses at least four definition conventions and the check knew
> one.** That is worse than a check that finds nothing: 19 false positives train a
> reader to dismiss the output, so a genuine orphan appearing later would be lost
> in noise the check itself manufactured.
>
> **Three fixes, each from a defect this exchange produced:**
> - **Peer families are excluded by name.** P07 found its extended check reporting
>   `P07-F-81` as an orphan when the match was a citation of *this package's*
>   `P04-F-81`. **In a two-package exchange, identifier collision is the normal case,
>   not an edge case**, so the prefix is required and peer families are declared.
> - **Own identifiers are no longer elided.** Lists such as *"`P04-B-16`, `B-18`,
>   `B-19`, `B-28`"* were readable and unmatchable; nine such elisions across five
>   files are now written in full. Bare forms that remain are **foreign by
>   attribution** — `P2 REV-03`, `P2 CTR-05`, `P07's F-65` — and are correct.
> - **`BLK-03`…`06` are emboldened**, so a reader and a checker find them by the
>   same route.
>
> And the self-referential trap P07 hit arrived here too: **writing this finding
> cited `P04-F-111` before it was defined**, and the check reported it until this
> paragraph existed.
>
> Class: **FACT VERIFIED**. Final state: **2 undefined across 14 families** — the
> intentional withdrawal notice `P04-F-18`, and this finding's own identifier
> until now. Control: a deliberately absent id is reported.

> **P04-F-112.** **Three items across two packages are one ask, and separately
> each reads as a small residue.** `P04-B-47` — were the missing asset entries
> never created, or created and removed — and P07's `U-20` and `U-29`, both of
> which reduce to **template/module load order**, are the only items in either
> package that **no reading, no wider census and no better query can close**
> (`P04-F-105`).
>
> What they need is identical in kind: **a controlled installation executed twice,
> in opposite orders, with the sequence recorded.** For `P04-B-47` the equivalent
> is a second capture of one identity at a different point in time, or the
> deployment's own audit trail.
>
> **Stated because the shape is invisible from inside either package.** P07's two
> sit in a tax register and this package's in an asset register; each looks like a
> minor unresolved item next to dozens of others. Together they are **the only
> category of evidence neither session can manufacture**, and they are the entire
> content of what a runtime request would be for.
>
> Class: **CROSS-PACKAGE DECISION ITEM**, routed to `09` §5. Not a research
> finding and not closable by research.

### 6A.12 The second module: axis open, exposure characterised

> **P04-F-107.** **For `product_stock_equipment` the code-identity axis is NOT
> closed — and characterising the divergence discharges the claim anyway.**
> Eleven copies enumerated over the declared path set; whole-tree hash,
> CR-normalised, bytecode excluded, **empty-sentinel control printed and not
> matched** (19 real files behind every hash):
>
> | tree | copies | where |
> |---|---:|---|
> | `3befb71c` | **7** | includes the **declared** root |
> | `658b5625` | **2** | both under `MIGRATION/ODOO18/` (18.0.4, 18.0.5) |
> | `effc9e3d` | 2 | both **v16** paths — different generation |
>
> **Two distinct v18-line trees**, and every copy declares `'1.0'`, so **version
> cannot discriminate them.** Unlike `equipment_sequence` (`P04-F-102`) the axis
> stays open.
>
> **Divergence, measured rather than assumed** — 7 of 7 python files AST-parsed,
> 0 failures:
>
> | | |
> |---|---|
> | class-level field differences | **0** |
> | XML files differing | **1 of 5** — 4 lines |
> | python changed lines | **3**, all in `models/product_template.py` |
>
> The XML difference is **presentational only** — an inline-block `span` wrapper
> against a `div`; no field, attribute, domain or readonly/required changes. The
> python difference is a **multi-record safety** one: the declared copy iterates
> its recordset before writing a descriptive note onto equipment matched by
> **name**, the other addresses the recordset as a singleton. So a bulk write
> raises in one copy and not the other.
>
> **The claim this package draws from the module is unaffected, and that is
> checked rather than asserted.** `05` §3 cites the module for creating an
> equipment record on stock validation and for **forcing any equipment-flagged
> product to non-storable with serial tracking**. That forcing lives in
> `onchange_equipment`, which is **byte-identical in both trees** and is not in
> the diff. The diverging function writes a **note** — descriptive text — and
> touches no accounting value.
>
> Class: **FACT VERIFIED**. Axis **OPEN** for the module, **exposure characterised
> and the cited claim discharged**. This is P07's split applied to a case where
> views *do* differ: the rule is not *"views identical ⇒ structural claims safe"*
> but **compare the difference against the specific claim** — a presentational
> wrapper cannot carry a structural claim, and a note write cannot carry an
> accounting one.

> **P04-F-108.** **The forcing is an `@api.onchange`, so it binds only in the
> form.** `onchange_equipment` sets a product to non-storable with serial
> tracking **when a user ticks the box in the UI**. An import, a script or any
> programmatic `create`/`write` sets `equipment_ok` without it firing, so a
> product can be flagged as equipment while remaining storable and untracked.
>
> This is **independent corroboration of this package's central pattern from a
> different module**: three of the four values driving every depreciation entry
> are UI-enforced only (`01` §3), and here the equipment/stock designation is too.
> Found while comparing copies for a different purpose, and it holds whichever
> copy is deployed.
>
> Class: **FACT VERIFIED**, both trees.

> **P04-F-109.** **All five sweep units are now demonstrated capable of reporting
> a defect — by injection, not by having fired accidentally.** P02 found its
> clean-room scrubber had only ever returned zero and had never been shown able
> to return one. This package's units *had* fired, but by accident rather than by
> design, which is not a control.
>
> A copy of the package was taken and one defect injected per unit: a citation of
> an undefined finding id, an extra table cell, an edit invalidating a published
> hash, four vendor tokens appended to the Layer-1 pack, and an empty deliverable.
>
> | unit | baseline | injected |
> |---|---:|---:|
> | identifiers | 0 | **1** |
> | per-table structure | 0 | **1** |
> | manifest-hash agreement | 0 | **4** |
> | Layer-1 scrub | 0 | **4** |
> | empty-sentinel | 0 | **1** |
>
> **All five fire.** Class: **FACT VERIFIED**, reproduced in the session
> scratchpad against a copy, never against the package itself.

> **P04-F-110.** **This package's evidence commands are shell-dependent, and the
> dependence is one-directional.** Every evidence root here contains spaces.
> Tested on this host: **`zsh` does not word-split an unquoted expansion** — one
> argument, and quoted and unquoted searches return identical results — while
> **`bash` splits it into two**, and an unquoted `grep -rl` over a spaced path
> returns **0 matches on a file that exists**.
>
> All evidence in this package was executed in **`zsh`**, so **the negatives
> stand as executed**. But a reader re-deriving any of them **under `bash`
> without quoting would get zeros indistinguishable from true absence** — the
> `P04-F-103` shape, in a reader's hands rather than the author's.
>
> Recorded as a **re-derivation warning, not a defect**: anyone re-running a
> declared negative from `13` must quote every path or state the shell. Reported
> by P02, verified here rather than adopted.
>
> Class: **FACT VERIFIED**, executed in both shells on this host.

### 6A.11 A fifth axis: facts that were never recorded

The four scope axes — signature set, path set, source scope, code identity — are
all about **where the author looked**, and every one is closable by looking
better. P07 identified a fifth that is not.

> **P04-F-105.** **Some open items are open because the evidence was never
> recorded by anyone, including the deployments themselves.** P07 traced both of
> its headline findings to **template/module load order** — whether the chart
> loaded before or after a language was activated. A database records the
> **result** of that order and never the order, so no archive, no wider census
> and no better query can settle it; only a controlled install executed twice, in
> opposite orders, can.
>
> **This package has one item of the same class and had already registered it
> without naming the class.** `P04-B-47` asks whether the missing asset journal
> entries were **never created** or **created and then removed** — the question
> `P04-B-40` turns on, since that is the routine whose draft branch has no date
> test. A single snapshot cannot distinguish them, and neither can more
> snapshots of *other* identities: what would settle it is the **sequence of
> writes to one identity**, which is not in the archive.
>
> **The distinction changes what a HOLD means**, and it is worth stating in the
> Boss pack: every other open item in `10` is open because something has **not
> yet been read**. `P04-B-47` — and `P04-B-46`'s two modules whose source exists
> nowhere on this host — are open because the evidence **does not exist to be
> read**. The first kind is closed by more work; the second only by **executing
> something and recording it**.
>
> Class: **FACT VERIFIED** as a classification of this package's own register.
> `P04-B-47` is re-tagged **EVIDENCE NEVER RECORDED**, and the remedy is a
> runtime request, not research.

> **P04-F-106.** **A control, once added, is never removed — and this session has
> the proof rather than the argument.** `P04-F-103` (42 hashes of empty input
> reading as *"42 identical copies"*) was caught **only** because the file count
> printed alongside each hash had been added after `P04-F-98`, a different defect
> in a different test. **The control for defect *n−1* caught defect *n*.**
>
> Adopted, and the pre-commit sweep gains a **fifth unit**: no published hash may
> equal the **empty-input SHA-256** `e3b0c442…`, and no deliverable may be empty.
> This closes a real gap — check 3 compares the manifest's hashes against the
> files, so a file that became **empty** would be re-hashed on regeneration, the
> manifest would agree with it, and the check would report **0 stale** while the
> deliverable was gone. **Agreement between two records is not evidence that
> either is right.**
>
> Class: **FACT VERIFIED** — the gap was reproduced against the sweep before the
> unit was added.

### 6A.10 The zeros, made falsifiable

P02 laid its zero-COGS result against four deployments spanning every
discriminating configuration — never transacted, gate on with valuation off, gate
off with valuation on — and could then say the zero is *a property of the
mechanism, not of data volume*. **This package's zeros had never been laid out
that way, and doing it narrows one of them.**

| identity | gen | real assets | **source-linked** | analytic accounts | distributed asset moves | day convention |
|---|---|---:|---:|---:|---|---|
| `96548e18` | v18 | **no asset table** — module not installed | — | 0 | — | — |
| `551ab874` | v18 | 388 | **0** | **0** | none possible | 375/388 **daily** |
| `4b766580` | v18 | 7 | **6** | **9** | **14 of 14 net to zero** | 7/7 **constant** |
| `45a8e08e` | v16 | 669 | 22 | 0 | none possible | 683/685 **daily** |

> **P04-F-104.** **The source-link mechanism demonstrably works, so `P04-F-92`'s
> zero is a property of that deployment and not of the design.** In `4b766580`,
> `asset_move_line_rel` holds **6 rows covering 6 of its 7 real assets — 86 %**.
> In `551ab874` the same table exists and holds **0 rows against 388 real
> assets**. In `45a8e08e` (v16), **22 of 669 — 3.3 %**.
>
> **What this withdraws:** any reading of `P04-F-92` as *"the link is not
> implemented"* or *"the subledger cannot reach its source"*. It can, and in one
> deployment it does for almost every asset.
>
> **What this strengthens, and it is the more useful half:** the contrast is now
> a **measured spread of 0 %, 3.3 % and 86 % across three deployments of the same
> product**, which is a far sharper statement of `P04-B-01` than a single zero
> was. The three-values-of-four driving every depreciation entry are
> **UI-enforced only**, so any import or script bypasses them — and a population
> created by import would carry **no** source line while one created from posted
> vendor bills would carry one. The observed spread is **consistent with that**
> and with nothing else this package has found.
>
> Class: **FACT VERIFIED** as to the three coverage figures. The creation-path
> explanation is **SUPPORTED INTERPRETATION** — a single snapshot cannot show how
> a record was created, and this package will not infer it from a correlation.
> `P04-B-03` stays answered per identity, **not** generalised.
>
> **And the same table makes the other zeros falsifiable.** The netting mechanism
> fires **14 of 14** where analytic accounts exist, so `P04-F-99`'s zero is
> configuration, not absence of capability; `96548e18` — a v18 install where the
> asset module is not installed at all — is the negative control that shows what
> a genuinely empty estate looks like, and it looks nothing like `551ab874`.
> **A deployment with 388 assets, no source links and no analytic accounts is not
> an empty system; it is a populated one with two mechanisms switched off.**
>
> *The set was not assembled by design.* Two of the three v18 identities came
> from P02 correcting this package's population, after this package had corrected
> P02's. Neither of us chose the discriminating set; it is the residue of two
> reciprocal corrections.

### 6A.9 Closing the code-identity axis, one module at a time

P07 could not close the fourth axis for its modules and found something better:
its two copies differ **only in Python method bodies** — identical field sets,
identical views — so *nothing that differs is persisted*, and the axis threatens
**behavioural** claims only. Structural claims are discharged. Run here against
the two custom modules `EV-CUST` names and that are actually installed
(`P04-F-97`).

> **P04-F-102.** **For `equipment_sequence` the code-identity axis is CLOSED, not
> narrowed.** The deployed version in `551ab874` is **`18.0.1.6`**. Enumerated
> over the declared path set `/Volumes/iMacSys` + `$HOME`, **exactly two copies
> on this host carry that version** — the declared root and one other. Compared:
>
> | Test | Result |
> |---|---|
> | Common files | **42**, none present in one copy and absent from the other except compiled bytecode |
> | Python files parsed (AST, **class bodies only**) | **13 of 13**, 0 parse failures |
> | **Class-level field differences** | **0** |
> | View/XML files differing | **0 of 10** |
> | Python changed lines, CR-normalised | **0** |
> | Whole-tree source hash (bytecode excluded) | **identical — 1 distinct tree from 2 copies** |
>
> The copies are **byte-identical in source**. So which one is deployed cannot
> change any finding drawn from that module — **structural or behavioural**. This
> is stronger than P07's result, where method bodies diverged by 17–179 lines and
> only the structural half could be discharged.
>
> **P07's split is adopted as the general rule** and is the more useful outcome:
> where copies agree on fields and views but differ in method bodies, **findings
> citing models, fields or views are discharged and findings citing logic stay
> exposed** — because what differs is not persisted. The axis only ever threatens
> behavioural claims.
>
> **Qualified at `P04-F-116`**: this closes *which copy of this module is
> deployed*, **not** what else is installed on the model it operates on —
> `equipment_fleet` declares on `maintenance.equipment` from outside both declared
> roots and cannot be read from this host. Copy-identity and stack-completeness
> are two questions, and closing the first reads like closing the second.
>
> Class: **FACT VERIFIED**, bounded to the declared path set, with the version
> filter stated: only copies carrying the **deployed** version are candidates.
> `product_stock_equipment` is **NOT YET REPORTED** — 11 eligible copies were
> enumerated and the comparison is still executing; a partial answer is not
> published here.

> **P04-F-103.** **The first run of the test above returned 44 copies in 3 groups
> and was meaningless.** Forty-two of the 44 hashed to
> `e3b0c44298fc…` — the SHA-256 of **empty input** — because paths containing
> spaces were **word-split by the shell**, so the walk visited directories that
> do not exist and hashed nothing. The output was confident, reproducible, and
> would have read as *"42 identical copies"*.
>
> **This is the defect P07 reported one message earlier**, arriving here inside
> the test written to apply P07's lesson. It is also the **null-that-behaves-like-
> a-value** pattern from `P04-F-98`: 42 empty walks did not spread out as noise,
> they **collapsed into a single group** and looked like the strongest possible
> agreement.
>
> Caught by a control that was in the output only because the previous defect had
> taught it: the group carried a **file count of 0**. Every subsequent run prints
> the empty-input hash explicitly and flags any group equal to it.
>
> Class: **FACT VERIFIED** — recorded as a method defect of this package, not a
> finding about the estate.

### 6A.8 The analytic consequence clause, measured

P07 withdrew the second clause of its strongest finding after measuring it for
the first time: the *"resolves into a withholding group"* half was measured
everywhere, the *"and therefore settles against the withholding control
accounts"* half **nowhere**. It is latent — a zero-amount tax generates no tax
line, so the misassigned group has no vehicle to post through. This package has a
finding of the same shape.

> **P04-F-99.** **The analytic consequence clause is latent in the only v18
> deployment, and the reason is more basic than the finding.** This package
> publishes that **depreciation's analytic route nets to zero** — both entry
> lines carry the distribution, there is no account-type filter, and the signed
> amounts cancel, so *attribution exists at line level and the balance is zero*.
> The first half is source-derived and unchanged. **The second half has never
> been measured. Measured now, it cannot fire.**
>
> | | `551ab874` |
> |---|---:|
> | `analytic` module | **installed**, `18.0.1.1` |
> | `account_analytic_plan` rows | **1** |
> | **`account_analytic_account` rows** | **0** |
> | `account_analytic_line` rows | **0** |
> | move lines carrying `analytic_distribution` | **0 of 40,353** |
> | — of which asset-move lines | 0 of 4,236 (3,440 depreciation) |
>
> **Positive controls on the same extraction, same table, same method:** `name`
> non-null on **38,228** lines, `account_id` on **40,282**, `balance` on
> **40,353**. The column is index 32 of 64 and its only observed value is `\N`.
> So the zero is **absence of data, not a failed read** — the defect recorded at
> `18` `P04-REV-23` and the standard P07 applied to its own controls.
>
> **What changes is the finding's live form.** *"Attribution exists at line level
> but the balance is zero"* describes code that has never run here. There are
> **no analytic accounts at all**, so no distribution is ever set, so **there is
> no attribution at line level either.** The netting defect is real in source and
> sits **downstream of a more basic absence**: the analytic dimension is
> installed, has a plan, and has never been populated.
>
> The same reasoning withdraws the liveness of the companion claim that
> **mandatory analytic plans never fire on programmatic posts** — with one plan
> and zero accounts, nothing can be mandatory over an empty set.
>
> **This corroborates P09 directly** — that session's headline is that the
> analytic dimension is *schema, not data*, one root cause behind eleven defects.
> It was reasoning from source; this is the measurement, in a v18 deployment with
> 40,353 posted lines.
>
> Class: **FACT VERIFIED** as to the counts, **bounded to `551ab874` and
> narrowed one commit later** — see `P04-F-100`. **The latency is a property of
> that identity, not of the generation**: a second v18 identity has analytic
> accounts, and there the mechanism fires.

> **P04-F-100.** **The analytic cancellation is CONFIRMED — measured, in a
> deployment where it can fire, without exception.** P02 reported further
> databases outside every census either of us had run. One is **`4b766580`
> (`pankhamhom`), `base 18.0.1.3`, 478 installed modules, 20 assets (13
> templates, 7 real), 956 move lines** — and unlike `551ab874` it has **9
> analytic accounts**.
>
> | | `4b766580` |
> |---|---:|
> | move lines carrying a distribution — **whole database** | **30 of 956** |
> | of those, belonging to an **asset** move | **30 of 30** |
> | distinct asset moves carrying distributed lines | **14** |
> | of those, signed debit − credit sums to **zero** | **14** |
> | non-zero | **0** |
>
> Thirteen of the fourteen carry **two** distributed lines and one carries four.
> **Every one nets to exactly 0.00.** This is `P04-F-49` observed rather than
> derived: both lines of the entry carry the asset's distribution and the signed
> amounts cancel, so the cost centre receives the charge and loses it in the same
> entry. **14 of 14, no exceptions**, and every distributed line in the entire
> database belongs to an asset move.
>
> **So `P04-F-49` is upgraded from source-derived to measured, and `P04-F-99` is
> narrowed to the identity it was measured in.** The correction published one
> commit earlier — that the cancellation *"has never carried a value"* — was true
> of `551ab874` and **false as a general statement**, including in the Layer-1
> pack, where it has now been corrected a second time. *A latency finding is a
> claim about a population, and mine had a population of one.*
>
> Also present in `4b766580` and absent from `551ab874`: **`asset_move_line_rel`
> holds 6 rows** (source links exist here), and moves of type **`disposal`** and
> **`sale`** exist — the disposal one in state `cancel`. And its **7 real assets
> are all on `constant_periods`**, a **third** day-convention pattern against
> `iSMEs` 683/685 daily and `551ab874` 375/388 daily.
>
> Class: **FACT VERIFIED**, bounded to `4b766580` @ 2026-01-21.

> **P04-F-101.** **Three v18 identities are now known, not one.** `551ab874`
> (361 modules, 388 real assets), `4b766580` (478 modules, 7 real assets), and
> **`96548e18` (`T805efaplus`, `base 18.0.1.3`, 123 modules) which has no
> `account_asset` table at all** — the asset module is not installed and it has
> **0 move lines**: a never-transacted v18 install, the v18 counterpart of the
> fresh-install control P07 used.
>
> `96548e18` was reachable by **neither** of this package's sweeps: it is a
> **`.zip`**, so the `PGDMP` signature scan missed it, and it is dated
> **2025**-12-27, so the reconciliation sweep's `*_2026-*` name pattern missed it
> too. **A second, independent bound in the very sweep that was written to
> reconcile the first.**
>
> Class: **FACT VERIFIED**. Every single-identity bound in §6A is hereby a
> **floor**, and the census remains OPEN.

### 6A.7 Are the custom modules this package read the ones that run?

P07 found it had analysed a module installed in **0 of 4** identities, while a
**different technical name** carrying the **same display name and version** held
the **same code** and *was* installed. Run here against `551ab874`.

> **P04-F-97.** **One of the three custom modules this package's evidence
> register names is not installed in either v18 deployment that holds assets —
> and in the one where it exists, it is explicitly uninstalled.**
> *(Restated at `P04-F-119`: written when only one v18 identity was known, and
> re-measured against the second. The finding **strengthens**.)* `13` §1 `EV-CUST` names three: the equipment-sequence module, the
> equipment-product-stock module, and the advance-expense-request module.
>
> | Declared module | In `551ab874` | Deployed version |
> |---|---|---|
> | `equipment_sequence` | **installed** | `18.0.1.6` — matches the declared copy's manifest |
> | `product_stock_equipment` | **installed** | `18.0.1.0` — the declared copy's `'1.0'`, series-normalised |
> | `scgl_advance_expense_request` | **NOT INSTALLED** in `551ab874`; **present but `uninstalled`** in `4b766580` | — |

> Re-measured across both v18 identities holding assets: `equipment_sequence`
> is `18.0.1.6` and `product_stock_equipment` `18.0.1.0` **in both**, identical
> versions; `scgl_advance_expense_request` runs in **neither**. In `551ab874` it
> is absent from the module table entirely; in `4b766580` it is **present in the
> addons path and never installed** — which is the stronger form, because it
> distinguishes *not deployed* from *not available*.
>
> More broadly, **37 of the 65 declared custom directories are not installed
> there** (`P04-F-93`); this names the one that a finding rests on.
>
> **And a matching version proves nothing.** P07 established that two code bodies
> can share one version string (17–179 changed lines across seven files) and that
> a display name and version can span two technical identities. **Neither name,
> nor version, nor display name identifies deployed code — only the installed
> module list does, and it identifies only the *name*.** The deployment's own
> addons directory is not on this host, so **agreement of code cannot be checked
> at all**; "installed, same version" is the strongest statement available and it
> is weaker than it reads.
>
> Class: **FACT VERIFIED** as to installation state; the code-identity question
> is **NOT DECIDABLE** from this host. Folded into `P04-B-46`.

> **P04-F-98.** **P07's twin defect does not reproduce here — a negative,
> published as one.** Comparing display names across the 361 installed modules
> and all **65** declared custom modules: **zero display names are shared by two
> different technical module names where either is a declared custom module.**
> The only shared display names in the estate are the reference product's own
> community/enterprise pairs (`account`/`account_accountant` both "Invoicing",
> and eight similar), which are expected and are not the defect.
>
> **The first run of this test reported 11 twins and was wrong.** Ten of them
> were a single bogus group produced by the test's own manifest parser failing on
> 10 of the 65 manifests and recording them all as name `?`, which then collided
> with each other. Re-run with a parser that reads **65 of 65**, the answer is
> **0**. *A test with an unreported parse hole does not return a weaker result —
> it returns a confident wrong one*, and the failures grouped themselves into
> exactly the shape the test was looking for.
>
> Class: **FACT VERIFIED (negative)**, bounded to `551ab874` and the 65 declared
> custom modules, parser coverage **65/65 declared** stated because the previous
> run's coverage was 55/65 and unstated.

### 6A.6 The behavioural findings, tested against a same-generation deployment

Every behavioural finding in this package was derived from v18 **source** and,
until `P04-F-90`, had **no v18 deployment** to be set against. Two are now
measured. **One does not manifest, and the other cannot be separated from a
larger effect** — both results are published because a test run only when it
confirms is not a test.

> **P04-F-95.** **The unposted-entry concern does NOT manifest for scheduled
> depreciation in the one deployment where it can be tested.** `idemo18_uat`
> holds **1,720 depreciation entries in `draft`** — and **every one is dated in
> the future**: 2026-08-31 to 2038-11-30, against a snapshot taken 2026-08-30.
> **Zero past-dated drafts.** The **398** asset-linked entries whose dates have
> already fallen due — 2026-01-31 to 2026-07-31 — are all **`posted`**.
>
> So draft-and-future is the *designed* state of a depreciation board, and the
> posting machinery in this deployment **demonstrably posts**. Had this package
> reported *"1,720 depreciation entries sitting unposted"* it would have been a
> serious false positive, and the shape of it — a large number, in the expected
> direction, from a query that never asked the discriminating question — is the
> shape of most of the defects recorded in `18`.
>
> **This is also the positive control the derecognition test needs**: posting is
> not globally broken here, so an absence elsewhere cannot be explained by it.
>
> Class: **FACT VERIFIED (negative)**, bounded to `551ab874` @ 2026-08-30.

> **P04-F-96.** **In this deployment 323 of 388 real assets carry no journal
> entry of any kind — and that is why the disposal-specific claim cannot be
> confirmed here.**
>
> | Asset group | Assets | With ≥1 journal entry |
> |---|---:|---:|
> | `open` | 303 | **65** |
> | `paused` | 17 | **0** |
> | **disposed** (`disposal_date` set, all `close`) | **30** | **0** |
> | `draft` (not validated — none expected) | 38 | 0 |
> | templates | 16 | 0 |
> | **Real assets total** | **388** | **65** |
>
> **All 30 disposed assets have no derecognition entry — and no entry at all, in
> any state.** Taken alone that reads as confirmation of this package's headline
> TAS 16 finding. **It is not, and the control is what shows it:** **238 of 303
> `open` assets** and **17 of 17 `paused`** also have none. The absence is
> **general, not disposal-specific**, so this deployment **cannot separate**
> *"no disposal path posts the derecognition entry"* from *"the asset subledger
> largely never reached the ledger at all"*.
>
> **The source finding is unchanged and remains source-derived.** What is
> withdrawn is the temptation to cite this database as its confirmation.
>
> **What the measurement does establish**, and it is larger than the finding it
> failed to confirm: of the **350** assets in states that should have generated
> entries (`open`, `paused`, disposed), **285 have none**. With `P04-F-92`
> (**0 of 388** carry a source-line link), the asset subledger in the one v18
> deployment available is **almost entirely disconnected from the general ledger
> in both directions** — nothing points back to the document that created the
> asset, and 83 % of assets have produced no accounting effect.
>
> A single snapshot **cannot distinguish** entries never created from entries
> created and removed. That distinction is exactly what `P04-B-40` (the draft
> branch with no date test) turns on, and it is **not decidable from this
> evidence**. Recorded as such rather than resolved.
>
> Class: **FACT VERIFIED** as to the counts; **NOT DECIDABLE** as to cause.
> Bounded to `551ab874` @ 2026-08-30. Blocker `P04-B-47`.

### 6A.5 Is the source this package read the source that is deployed?

Untestable until `P04-F-90` produced a same-generation deployment. Now testable,
and run on P07's finding that its own excluded source root **was** the deployed
code.

> **P04-F-93.** **The declared source scope is not the deployed source scope, in
> both directions.** Against `idemo18_uat` (`551ab874`, v18, 361 installed
> modules):
>
> | Measure | Count |
> |---|---:|
> | Installed modules in the deployment | **361** |
> | Present in the declared reference tree | 306 |
> | Present in the declared custom set (65 dirs) | 28 |
> | **Installed and in NEITHER declared root** | **27** |
> | **Declared-custom modules NOT installed here** | **37 of 65** |
>
> So **27 modules are running in the v18 deployment that this package's declared
> source scope never contained**, and **37 of the 65 custom directories it did
> read are not installed in this deployment at all.** The declared set overlaps
> the deployed set by 28 modules out of 65 declared and 55 deployed-custom.
>
> **`13` §1 declares the source scope by *description* — *"Reference ERP v18
> Enterprise source tree, build `20250608`"* and *"Project custom addon set, v18
> line"* — and names no path.** That is the same defect as the undeclared archive
> path set (`P04-F-88`, withdrawn), one level up: **a source scope stated as a
> description cannot be audited, and cannot be shown to be the deployed one.**
>
> **And the build string does not identify the tree.** Two directories on this
> host carry build `20250608` and hold **793** and **1753** manifests
> respectively. Whichever this package read, *naming the build did not name the
> code* — P07 reached the same conclusion from the other side, where two copies
> of a module carried one version string and differed by 279 changed lines in a
> single file.
>
> Class: **FACT VERIFIED.** Counts executed against `ir_module_module` in the
> archive and against manifest enumeration in both trees.

> **P04-F-94.** **Part of the deployed behaviour cannot be read from this host at
> all.** Of the 27 modules deployed and outside both declared roots, source is
> present for some — `scgl_account_coa_control` (three copies),
> `scgl_multi_approve_core` (three), and `scgl_date_range_auto_period`, which
> sits **one directory above the declared custom root**, the same shape as the
> archive that sat one directory outside the declared path set. For others
> **no directory of that name exists anywhere under `/Volumes` or `$HOME`** —
> including **`equipment_fleet`** and **`journal_entries_report`**.
>
> **Stated as exposure, not as an assessment — this package has not read any of
> them.** What can be said is which load-bearing findings sit in the path of an
> unread deployed module *by name*:
>
> | Unread deployed module | Findings it could touch | Source on host? |
> |---|---|---|
> | `scgl_account_coa_control` | capitalization designation lives **on the chart-of-accounts account** — the source-of-truth finding | yes |
> | `scgl_date_range_auto_period` | period assignment — the **silent re-dating** finding and `P04-B-31` | yes |
> | `equipment_fleet` | the Operation–Equipment gap, machine identity, `BD-03` | **no** |
> | `scgl_multi_approve_core` / `_purchase_request` | the upstream purchase path into capitalization | yes |
> | `journal_entries_report` | reporting over the entries the reconciliation reads | **no** |
>
> **No finding is withdrawn and none is confirmed by this.** The honest statement
> is that every source-derived finding in this package is bounded to a source
> scope that is **now known not to be the deployed one**, and that the gap is
> **27 modules wide**, at least two of which cannot be closed from this host.
>
> Class: **FACT VERIFIED** as to the enumeration; **UNRESOLVED** as to effect.
> Registered as blocker `P04-B-46`.

> **P04-F-89.** **This package published two integrity records and let them
> disagree.** `SHA256SUMS.txt` and the manifest's own per-file hash table were in
> agreement at `abf265c`, `b27040e` and `c57d846`, and **disagreed on 6 of 20
> files at `985840e`** — the commit whose message reports three checks run and
> clean. The sums file was regenerated; the manifest table was not.
>
> The three checks that ran were **identifiers, table structure and Layer-1
> scrub**. None of them has the unit *"the integrity record agrees with the
> files it describes"*, so all three passed. **The document asserting that the
> package is intact was the document that was wrong**, and it was wrong for
> exactly one commit — long enough to publish.
>
> Consequence adopted: the pre-commit sweep is **four checks with disjoint
> units** — identifiers, per-table structure, **manifest-hash agreement**, and
> the Layer-1 scrub — plus register counts executed rather than typed. Adopted
> in the same form from P07, which reached four checks from the other direction.
>
> Class: **FACT VERIFIED**, reproduced against git history at four commits.
>
> Class: **FACT VERIFIED**, bounded to the four v19 identities named.
> **Available only once the halves were separated**: while they shared a
> sentence, the configuration half read as a property of the templates rather
> than as a **consistent non-action across independent operators**, and the
> population half was doing no work for it. The shape is adopted from P07, which
> found the same concealment in its own compound finding.

> **P04-F-83.** **No v19 database on this host contains a single real asset
> record.** **Unit declared:** **six** v19 snapshots across **four database
> identities** (`1f6338ae`, `f4a44cce`, `66d1b52a` and `a1430edc`, the last two
> captured twice each), spanning **2026-03-30 to 2026-08-03**, holding **96
> templates per identity and zero real assets** between them.
> The only population of real assets available anywhere is on the **older
> generation**.
>
> *An earlier wording said "four v19 databases", conflating snapshots with
> identities — the same unit defect this package records nine times over.*
> Class: **FACT VERIFIED**, bounded to the **six v19 snapshots across four
> identities** named at §6A.1, within an enumeration of all **seven** snapshots.
> **Strengthened, not weakened, by the census correction**: the newly-found
> identity `f4a44cce` is a fifth database and a fourth v19 one, and it too holds
> **zero real assets** — the claim now spans four months rather than seven weeks.
> **Reproduction caveat, with the unit declared.** The two unreadable v1.16
> archives are **both snapshots of one identity** (`iTEST02`, a month apart). So
> a reader on the host's default client sees **3 of 4 v19 identities** and **4 of
> 6 v19 snapshots** — and, critically, **zero real assets in every identity
> they can open.** The conclusion survives; only the sample shrinks. See the
> finding-by-finding table at §6A.1 for why this caveat cuts the opposite way to
> a peer's on the same evidence class.
>
> Consequence for migration readiness: the target generation has **never had an
> asset created in it** in any environment captured here. Every behavioural
> finding in this package about v18 asset behaviour is therefore a statement
> about **code that has not yet been exercised on this project's data**, and the
> template configuration that would govern the first asset created is on the
> **wrong convention** (`P04-F-81`).

This is the concrete form of a risk two prior packages stated in the abstract:
the two conventions **agree annually within 0.05 %**, so an annual reconciliation
**cannot detect** a wrong setting. Here is a population of templates carrying the
setting that prior work identified as the wrong one for this business, in
databases nobody had opened. It does **not** close inherited blocker `BLK-01`,
which names `idemo18_uat`; it gives that blocker a second population and makes
its consequence concrete rather than theoretical.

### 6A.3 The source-document link — `P04-B-03` answered for one database

`P04-B-03` recorded that whether any live asset carries a link to a source vendor
bill was **not observable**, because the runtime capture's 12-field list omitted
the relation. In `iSMEs` it is directly observable.

| Measure | Count |
|---------|-------|
| Asset records, excluding templates | **669** |
| Rows in the asset-to-journal-item relation | 33 |
| **Distinct assets carrying any source-line link** | **22** |
| **Assets with no link to any source document** | **647 — 96.7 %** |

> **P04-F-82.** **`n = 1` — this is a single-database finding and is stated as
> one.** Unlike `P04-F-81` and `P04-F-83`, which were enumerated across **all**
> snapshots before publication, this rests on the **one** database holding real
> assets, so no claim about generality is available. A peer withdrew the
> universality of its own headline on exactly this test — 2 of 4, not "the
> shipped state" — while keeping its severity, on the reasoning that *a defect
> firing in half of deployments and silent in the other half cannot be found by
> testing a system that works.* The same caution applies here in the other
> direction: **the proportion below may be characteristic of this database
> alone.**
>
> In this database, **fewer than 4 % of asset records carry any
> link to a source journal item.** The upstream trace described at §4.4 is not
> merely *unstored* — for the overwhelming majority of this population **the
> first hop does not exist**, so no traversal can reach a purchase order however
> it is written.
> Class: **FACT VERIFIED**, bounded to `iSMEs` at 2026-07-11.

This converts `P04-B-01` from a design observation into a measured one: the
mandatory rule *always trace a financial fact to its initiating business event*
is not merely unsatisfiable from stored asset data by construction — in the one
asset population this session could measure, **it is unsatisfiable in fact for
96.7 % of records**.

`P04-B-03` is **answered for `iSMEs` and remains open for `idemo18_uat`**.

### 6A.4 What this does and does not do to the blocker set

| Blocker | Effect |
|---------|--------|
| `P04-B-03` | **Answered for one database**, open for the one it names |
| `P04-B-01` | **Strengthened from design gap to measured gap** (`P04-F-82`) |
| `BLK-01` (inherited) | **Materially advanced, not closed** — a second population, and the template-versus-population split made concrete (`P04-F-81`) |
| `P04-B-02` (origin mechanism) | Not answered — requires the external-identifier table, not extracted this session |
| `P04-B-16`, `P04-B-18`, `P04-B-19`, `P04-B-28` | Unchanged. They concern v18 behaviour; the only database with real assets is an older generation |

**The honest summary: one blocker answered for one population, one strengthened,
one advanced, four unchanged — and the reason four are unchanged is a real
generation mismatch, not an absence of evidence.** That is a different sentence
from *"no database access was attempted"*, which is what this package published.

## 7. Thai acquisition forms the estate does not model

Two acquisition forms that are ordinary in Thailand have **no host** in this
build. Both are recorded here because they are upstream of capitalization and
therefore in P04 scope.

| Form | Status in the estate | Statutory note | Class |
|------|---------------------|----------------|-------|
| **Hire purchase / instalment sale** (เช่าซื้อ / ซื้อขายผ่อนชำระ) — the ordinary way machinery and vehicles are acquired by Thai SMEs | No acquisition mechanism found under the declared path set; the loans module links to assets but capitalizes nothing | Revenue Department instruction **ป.36/2536** (15 Nov 2536) prescribes the VAT treatment: the lessor issues a tax invoice **on each instalment due date**, and VAT is computed per instalment, not on the whole contract at inception | Estate finding **FACT VERIFIED**; statutory citation **FACT VERIFIED**; the SMEsPlus treatment is a **DESIGN CANDIDATE** and is **HOLD / EVIDENCE REQUIRED** pending the Accounting-Tax track |
| **Borrowing-cost capitalization** (TAS 23) — interest capitalized into a qualifying asset's cost | Tested directly: under pattern `original_value\|capitaliz` across the loans module, **no write of loan interest into asset cost was found**. Loan interest is directed to an expense account | Not researched in this session | Estate finding **FACT VERIFIED** (scoped); statutory position **UNRESOLVED** |

Registered as blocker **P04-B-04** (hire purchase) and **P04-B-05**
(borrowing cost).

---

## 8. Summary of upstream findings

| ID | Finding | Class |
|----|---------|-------|
| **P04-F-01** | The capitalization source of truth is the **posted vendor bill or a manually selected posted journal item** — never the purchase order, never the goods receipt, never the product. | FACT VERIFIED |
| **P04-F-02** | The capitalization designation lives **only on the chart of accounts**. There is no product-level or category-level fixed-asset designation anywhere in the population. | FACT VERIFIED |
| **P04-F-03** | Three of the four values that determine every future depreciation entry — automation mode with no model, and both depreciation accounts — are enforced **by the user interface only**. Every non-interface write path bypasses them. | FACT VERIFIED |
| **P04-F-04** | The automatic path is reachable **only from purchase-type documents**; the sale-side exclusion cancels every sale document that would otherwise qualify. | FACT VERIFIED |
| **P04-F-05** | The source journal item is **never reversed or re-classified**; asset and ledger are joined by a **relation table, not a balancing entry**. | FACT VERIFIED |
| **P04-F-06** | The upstream link to the purchase order exists **only on the journal item**, requiring a two-hop join that is nowhere stored on the asset. The mandatory "trace to initiating business event" is **not satisfiable from stored asset data**. | FACT VERIFIED |
| **P04-F-07** | A second instantiation point exists: revaluation creates a **child asset sourced from a system-generated journal entry**, with no external business document and **no analytic distribution**. | FACT VERIFIED |
| **P04-F-08** | **Company-paid employee expenses can never auto-capitalize**; only the employee-paid mode re-enters the vendor-bill path. | FACT VERIFIED |
| **P04-F-09** | No construction-in-progress / WIP capitalization mechanism was found under the declared path set. | FACT VERIFIED (scoped negative) |
| **P04-F-10** | A custom module declares a dependency on the asset engine while contributing no asset behaviour, so installing it silently activates the engine. | FACT VERIFIED |
| **P04-F-11** | The live asset population (280) carries **no asset model at all**, and 35 carry an empty account triple. | FACT VERIFIED |
| **P04-F-12** | The **origin mechanism** of the live population is **not established**; the runtime capture that appeared to show migration origin was identifier-bounded. | UNRESOLVED |
