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

~~**No sixth database exists** under the stricter method, so `P04-F-83` is not
resting on a missed artefact.~~ **FALSE, and left standing with its disproof
rather than deleted.** A sixth and a seventh snapshot were found (`P04-F-86`), and
then an eighth — **`idemo18_uat`, the database two blockers were held open on**
(`P04-F-90`) — followed by two more v18 identities (`P04-F-101`). The sentence was
a **settled negative asserted from a re-run**, which is the error `P04-F-105`
classifies: a re-run is not a proof of completeness, and this one was bounded by a
path set that was never declared.
*This instance survived the correction that fixed the same sentence in `18`
`P04-REV-27`, and was found only by the assertive-citation form of the
identifier check (`P04-F-120`).*
Two bounds **were** tested rather than assumed and that part stands: the
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

### 6A.41 Derivation does not replace declaration — it bounds it

P07 audited all seven of its units for declared denominators and found two: a
family literal, and a Layer-1 scrub literal of 18 against **78 derivable tokens** —
*"checking less than a quarter"*, with the handoff pack still clean against all 78.
Run here, both come back, and **the second one corrects the fix rather than
confirming it.**

> **P04-F-142.** **The Layer-1 scrub was checking 13 tokens. 103 are derivable
> from Layer 2 by shape.** Same defect, same reassuring outcome: **0 leaks against
> all 113**, so nothing published was ever wrong — the guarantee simply covered an
> eighth of what it read as covering. Fourth instance across both packages of a
> narrow check whose result survives widening, and the argument stands: **none of
> the four could be known to cost nothing until it was run.**
>
> **But the derived set is not a superset of the declared one, and that changes
> the rule.** Of the 13 declared tokens, **10 cannot be produced by any shape
> pattern** — bare vendor and product names, bare table prefixes, a bare host
> name. Only **3 of 113 are in both sets.** The reason is general and not a defect
> in the patterns: **a vendor name has no shape.** It is an ordinary lowercase
> word, indistinguishable by form from English prose, and derivable only from
> knowledge of what the vendor is called. Conversely no author enumerates 103
> module paths by hand.
>
> **So replacing a literal with a derivation silently drops exactly the class of
> token clean-room exists to catch.** The denominator is the **union**, and the
> two differences are both reportable: *declared-but-underivable* is the identity
> half, *derived-but-undeclared* is the structural half. Unit `[4]` now prints
> `13 declared + 103 derived, 3 shared`, so the disjointness is visible instead of
> assumed. **This is offered to P07 as a correction to its own repair**, not as a
> confirmation: a scrub rebuilt as *78 derived* in place of *18 declared* may have
> lost coverage it had, and only intersecting the two sets will say.
>
> Class: **FACT VERIFIED**. Both sets enumerated, intersection counted, leak count
> run over the union.

### 6A.42 The class boundary was drawn on appearance

> **P04-F-143.** **Six families carry definition rows in this package and were not
> in the swept set. Three of them are mine.** Derived ownership — *a family is
> owned if any member of it is defined here* — returns **25**; the declared sweep
> list held **19**.
>
> **What was misfiled, and why it is one mistake and not three.** The statutory
> source `DBD-01` and the two re-dating cases in `20` were filed as **not
> identifiers**, in a published table whose examples are `TAS-02`, `SHA-256`,
> `Layer-1`. But `SHA-256` and `Layer-1` are *shapes* — a hash width, a layer
> number, nothing defines them. `TAS-02` and `DBD-01` are **rows in the source
> register at `13` §4.1**. They were grouped with the shapes because they *look*
> alike — a word, a hyphen, a number — and not because they behave alike. **The
> class was drawn on appearance rather than on whether the package defines the
> thing**, which is the same error as classifying a family by its name instead of
> its series (`P04-F-141`), one level up.
>
> **And it exposed one source under two labels.** `07` cites the TFAC explanatory
> manual throughout as `TAS-16M`; `13` registers the same document as
> `P04-LAW-A`. Both readings are correct and the source is correctly classified
> under each — **the defect is that a citation audit keyed on either label sees
> half the uses.** Registered `P04-B-50`, and **not actioned**: a cross-file
> relabel does not belong in the commit that reports it. `TAS-16M` now has a
> register row so it resolves.
>
> **Three of the six are correctly unswept, and that has to be declared rather
> than left to the reader**: a legend abbreviation in `20`, and P07's and P11's
> families, which carry attribution rows here precisely so their identifiers
> resolve. **A foreign family with a local row is not an owned family** — sweeping
> its numbering against this package's text would test nothing. Unit `[1b]` now
> reports `0 unswept-undeclared` and names the three with reasons.
>
> **The re-dating cases also needed a sequence disposition** — they run from four,
> with three numbers unused, no prior package owning them and nothing in the
> package explaining the offset: **`UNDETERMINED`**, P07's disposition, second use.
> And the standards family is declared **not a sequence at all**: its numbers are
> the standards' own, so a gap check over them is meaningless — **a numeric suffix
> is not always an issue order.**
>
> Class: **FACT VERIFIED**. Ownership derived per family from definition presence;
> each of the six resolved against the register that holds it.

### 6A.40 The new unit was written with the defect the old unit had just been fixed for

P07 ran this package's sequence check **across every owned family** instead of the
one its old exception list covered, and found unused numbers in **two families it
had never looked at**. Recorded **UNDETERMINED** rather than guessed at, because
the drafting history that would settle them is not in the package. It also
reproduced `P04-F-140` within minutes of adopting it — writing its gap table **in
identifier form** made three identifiers exist that had not a minute earlier.

**Run the same widening here.**

> **P04-F-141.** **Unit `[7]` was published one commit ago over a hard-coded list
> of 8 families. This package owns 19.** Eleven owned numeric families were never
> in the check — the inherited-and-attributed registers, the evidence pointers,
> the query set, the use cases, the requirement items. **This is the defect
> `P04-F-137` had already found and fixed for the family classification, written
> fresh into the next unit three days of findings later.** Fixing a rule in one
> unit does not propagate it to the next unit written: **each unit carries its own
> denominator, and each one has to be derived.** Widened to derive from the owned
> set: **19 families, gaps none, three dispositions declared.**
>
> **The widening found two, and neither is an unused number.**
>
> **One is two families under one stem.** The requirement items `D-1`…`D-7` are
> this package's; `D-11` and `D-12` are **P11's Boss decisions**, attributed at
> `P04-F-116`. The three numbers between them are not unused — they are the seam
> between two registers that share a letter. **This is `P04-F-117` inverted**:
> there, two families collided on one stem and every check passed; here, one stem
> holding two families makes a gap check report a hole that does not exist. In
> both directions **the family name is not the series** — and a per-family gap
> check silently assumes it is.
>
> **The other is a bare stem this package does not own alone.** The specified-query
> set is numbered from ten upward; **nine numbers below it are unused here and are
> in live use by other registers in this repository**, including one that also uses
> the number this package's set starts at. Whether the offset was chosen to dodge
> that collision or arrived some other way is **not in the package**, so it is
> recorded **UNDETERMINED** — P07's disposition, adopted for the same reason it
> reached it. **What is not undetermined is the collision**: `P04-F-117` ruled
> *rename what is yours, attribute what is inherited*, found two instances, and
> **missed this one because the audit was scoped to the families the sweep already
> knew about.** A third instance, registered `P04-B-49`, and it is a naming defect
> on an owned family, not an inherited one.
>
> **The unused numbers in both families are written here as prose and not as
> identifiers**, per `P04-F-140`. There is no identifier-form wording that states
> which numbers are unused without citing them, so none is attempted. P07 walked
> into that within minutes of recording the rule; the rule held here only because
> it had already cost this package two commits.
>
> Class: **FACT VERIFIED**. Family list derived from the owned set; per-family
> ranges enumerated; both gaps resolved against the registers that hold the other
> half. Sweep unit `[7]` now reports **19 families** and names its dispositions.

### 6A.39 The count was false on the line that asserted it

`P04-F-139` emptied the exception set. The next sweep run — the first in which
nothing was skipped before being tested — returned **one undefined identifier:
`P04-LAW-02`**.

> **P04-F-140.** **Writing that `P04-LAW-02` occurs zero times made it occur.**
> The finding reporting five inert exceptions had to name them; naming them is a
> citation; the identifier the sentence declares absent is present in that
> sentence. At `10faf0b` the count was **0**. On the commit that published the
> count it was **2** — once in `01` §6A.38, once in `18` §2 — and the sweep, no
> longer skipping it, correctly reported it **cited and undefined**.
>
> **Sixth appearance of the recursion, and the only one false immediately rather
> than eventually.** `P04-F-138`'s *"quoted four times"* was true when measured and
> went stale one commit later. This one **was never true at the moment of
> publication**: there is no interval in which the sentence and the text agreed.
>
> **The range notation created one endpoint and not the other.** Written
> `P04-LAW-02`–`06`, the first is an identifier and the rest are bare numbers,
> and **the remaining four conclusions in that family stay at 0**. So the artefact
> is not *naming a retired
> thing* but **the notation used to name a set of them** — the same mechanism as
> `[A-H]` at `P04-F-138`, arriving from the opposite direction. There a character
> class **became** an identifier; here a range **suppressed four and created one**.
>
> **And it settles the membership rule of the register `P04-F-139` created.** The
> obvious repair — tombstone all five for symmetry — is wrong, and wrong in the
> way this sequence keeps being wrong: **the remaining four do not occur, so a
> tombstone would be the only reason they existed.** A register whose entry
> criterion is *"was ever retired"* manufactures its own subject matter. The
> criterion is therefore **occurrence, not history** — `18` §7 holds a tombstone
> for each retired identifier **that survives in the text** and for nothing else.
>
> **Amended before commit, by the same defect one place further down the range.**
> The paragraphs above originally wrote the remaining four as a range beginning
> `P04-LAW-03`. The sweep then reported **`P04-LAW-03` undefined** — the
> explanation of the artefact had produced the next instance of it. **The defect
> migrates one identifier down the range each time it is restated**, and it is
> bounded only by the size of the family, which is not a control. Tombstoning
> would have terminated in four more iterations with a register whose entries
> exist **because the register discussed them**.
>
> **The terminating move is to stop writing them as identifiers.** They are now
> *"the remaining four conclusions in that family"* — prose, uncitable, unmatched
> by any pattern. This is the concrete form of the rule both packages reached
> separately: **the exit from a self-describing check is declaration, not
> correction**, and here declaration means **naming a set without using the
> notation that makes its members identifiers.**
>
> **And the residue is where the criterion gets its boundary.** Two occurrences of
> `P04-LAW-03` survive — the two sentences above, which report the incident. They
> cannot be removed the way the range was: **a defect cannot be reported without
> naming it.** So the register's rule needs a second clause, and it is a test, not
> a preference: **an occurrence that would survive rewriting the sentence earns a
> row; one that exists only because of how the sentence was written does not.**
> The range fails that test and was deleted. The incident report passes it, and
> `P04-LAW-03` is tombstoned at `18` §7 — **three rows now, one of which this
> finding created and could not take back.**
>
> **The rule this finding must obey about itself:** a count of an identifier the
> register quotes is a **measurement of the text taken from inside the text**, and
> cannot be maintained, because publishing it changes it. Every such count here is
> now written **as at a named commit** — including the ones in this paragraph,
> taken at `10faf0b`, which are already wrong.
>
> Class: **FACT VERIFIED**, occurrence enumerated per identifier per file, basis
> commit named. The control is the sweep itself, which fired **only because the
> exception set had been emptied** — the defect was created by the correction and
> caught by the same correction.

### 6A.38 An exception list cannot report that it is wrong

P07 applied the `RETIRED` class to its own sweep and found the same thing this
package found — its oldest standing exception was **two states filed as one**. Its
12 silently-subtracted identifiers split into **1 `NEVER ISSUED`** (`P07-F-81`,
which no finding ever carried; it exists only inside the passages describing a
false positive in the identifier check) and **11 `RETIRED`** (allocated, used in
drafting, then merged or discarded). Its sweep now **reports** the states —
`UNDEFINED: NONE | declared states: 11 RETIRED, 1 NEVER ISSUED` — on the ground
that *a silently-subtracted exception is invisible; a reported one can be
questioned*. Sixty commits of this package's "intentional orphan" line are the
demonstration.

**And it named a third disposition that is better than either of ours:** `P07-F-60`
is a **withdrawal tombstone carrying a definition row**, so the identifier
resolves and **no exception is needed at all**. An exception list is the fallback,
not the standard.

**Run here, the split and the standard both find something, and neither is what
was expected.**

> **P04-F-139.** **Five of this package's seven declared `RETIRED` exceptions are
> not in the text at all, and the sweep cannot say so.** The exception set named
> `P04-LAW-01`–`06` and `P04-F-18`. Occurrence counts across the 21 files,
> **as at `10faf0b`**: `P04-LAW-01` **8**, `P04-LAW-02`–`06` **0, 0, 0, 0, 0**,
> `P04-F-18` **12**. Every count in this section is stated *as at* a named commit
> and is **not maintained** — `P04-F-140` is why it cannot be.
> `P04-F-117` renamed the six conclusions to `P04-LC-01`–`06`; only the first
> survives, in quotations of the rename record. **The other five were declared
> exempt from a check they were never subject to** — and because the sweep
> `continue`s past an exception before testing whether it is present, a
> five-sixths-inert exception list and a correct one produce **identical output**.
> Adopted from P07 as sweep unit `[6]`: *declared-but-absent*.
>
> **The tombstone standard removes the list rather than reporting it.** Both live
> members now carry definition rows in a **Retired identifiers** register (`18`
> §7) — `P04-F-18`, withdrawn at `P04-REV-12` as a duplicate of `P04-F-23`;
> `P04-LAW-01`, renamed at `P04-REV-52`. Both resolve. **The exception set is now
> empty**, and the sweep reports `2 RETIRED, resolved by tombstone` instead of
> subtracting anything.
>
> **The `NEVER ISSUED` class is adopted and is empty here — and its control
> fired.** Every issuing sequence is contiguous: `P04-F` 1–138, `P04-B` 1–48,
> `P04-REV` 1–72, `P04-LC` 1–6, `P04-CTR` 1–7, `P04-PD` 1–8, `P04-SC` 1–4, **no
> gaps**. The one gap the check reported — `P04-BD` running **05–09 with 01–04
> missing** — is **not a gap**: `BD-01`–`BD-04` are the prior package's, cited
> unprefixed in `09` §2, and this session **continued the numbering under its own
> prefix** rather than restarting it. That is a fourth disposition, **`CONTINUED`**:
> one logical series split across two family names. It is the exact mirror of
> `P04-F-117`, where two families collided on one stem — and it is invisible to a
> per-family gap check for the same reason: **the family name is not the series.**
>
> **Fifth appearance of the recursion, and the first to invalidate a number
> rather than generate an identifier.** `P04-F-138` published *"quoted four
> times"*. That was true when measured, at `08a693c`. It is **eight** now, because
> writing the finding and its revision row quoted the identifier four more times.
> The four before it produced a spurious identifier; this one **falsified a
> published count by publishing it**. The fix is not a better count — any count of
> a self-quoting identifier is stale on commit — it is to **state the basis with
> the number**, which `P04-F-138` now does. P07 draws the boundary the other way
> for its own case and is right to: an identifier cited **before its own finding is
> registered** *is* correctable, because it was always going to exist and merely
> preceded itself. **What cannot be corrected is a measurement of the text taken
> from inside it.**
>
> Class: **FACT VERIFIED**. Counts enumerated per identifier, not asserted.
> Sequence check run over 8 owned families with the `P04-BD` offset resolved
> against `09` §2.
>
> **Sweep after: 7 units. 51 families derived, 0 unclassified, 19 owned swept,
> `undefined NONE`, 0 declared-but-absent, 0 never-issued, exception set empty.**

### 6A.37 A fifth class: identifiers that were owned and are not

P07's derived sweep surfaced a family its literals had missed — five quotations of
an identifier **inside the record of its own retirement** — and it needed a class
none of ours had: **`RETIRED`**, owned once, not now, surviving only as historical
quotation. **The same class is here, and one member is checked by nothing.**

> **P04-F-138.** **`P04-LAW-01` survives in four places and no unit examines it.**
> `P04-F-129` renamed the legal-conclusion register `P04-LAW-01`…`06` to
> `P04-LC-01`…`06`, and the sweep's `P04-LAW` pattern was narrowed to `[A-H]` in
> the same edit. **The retired numeric form was therefore removed from the check
> by the correction that retired it** — it is neither owned-and-swept, nor
> foreign, nor a non-identifier. It is quoted **four times as at `08a693c`**, in
> the finding that renamed it and the revision row recording that — a count whose
> basis has to be stated, because publishing this finding raised it to eight
> (`P04-F-139`).
>
> **This is the fifth disposition class and it completes the set**, alongside the
> four already adopted:
>
> | class | meaning |
> |---|---|
> | owned | defined here, swept |
> | foreign by attribution | defined elsewhere, cited with attribution |
> | not an identifier | `TAS-02`, `SHA-256`, `Layer-1` |
> | **`RETIRED`** | **owned once, renamed or withdrawn, surviving as quotation only** |
>
> **And it reclassifies this package's oldest standing exception.** Every sweep
> for sixty commits has reported *"undefined: `P04-F-18`"* and called it an
> intentional orphan. **It is not an orphan — it is `RETIRED`**: withdrawn at
> `P04-REV-12` as a duplicate of `P04-F-23`, deliberately left cited so the
> withdrawal is visible. Naming it correctly **removes the only permanent
> exception in the sweep**: an orphan is a defect tolerated, a retired identifier
> is a state recorded.
>
> **The general form, which is what makes it worth a class rather than a note:**
> a rename removes an identifier from the live set and **leaves it in the text**,
> so the operation that corrects a register is the operation that creates an
> unclassifiable identifier. Both packages produced one this way, neither
> anticipated it, and both found it only by deriving the family set rather than
> declaring it.
>
> **And the next run flagged a family that this finding created by being written.**
> The derived sweep reported **`A-H` unclassified** — because the sentence above
> says the pattern *"was narrowed to `[A-H]`"*, and a **regex character class
> parses as an identifier.** Classified as notation, non-identifier.
>
> **Fourth appearance of the recursion, and the first where the artefact is not a
> quotation.** `P04-F-115` quoted a bare identifier; `P04-F-117` quoted a renamed
> one; `P04-F-137` quoted a defective table row. This one quoted **nothing** — it
> stated the shape of a pattern, and the shape is itself id-shaped. **A register
> that describes its own checks will generate identifiers out of the notation
> those checks are written in**, which is one step further in than any of the
> three before it and cannot be avoided by quoting more carefully.
>
> Class: **FACT VERIFIED**, four occurrences located, class adopted, `P04-F-18`
> reclassified, one notation artefact classified.
>
> **Final identifier state: 50 families derived, 0 unclassified, 19 owned swept,
> 373 citations, 2 `RETIRED`, and — for the first time in this package —
> `undefined: NONE`.**

### 6A.36 An audit is not a control — and one owned family was never in either

P07 found that its statutory-source family `S` — **319 citations, the register
behind every legal claim it makes** — had been audited once and **never added to
the standing sweep**, which covered 8 of the 26 families that audit had cleared.
Its rule: **an audit proves a state; only a standing unit proves it is
maintained**, so every family an audit clears must enter the sweep or the
clearance expires silently.

**Tested here by making the sweep derive its own family list instead of reading a
literal.**

> **P04-F-137.** **Six families are present that the standing sweep classifies
> under nothing, and one of them is owned: `D-1`…`D-7`, the seven TAS 16
> derecognition requirements.**
>
> `P04-F-113` enumerated **43** families and classified them. The sweep then
> hard-coded that classification. **49 families are present now** — five entered
> through this correspondence (`REV-M`, and artefacts of three-segment peer ids)
> and one was **misclassified from the start**.
>
> **`D` is an owned family and was filed as a non-identifier.** `D-1`…`D-7` are
> defined in `07` §4 as `**D-1**` and carry the **seven TAS 16 derecognition
> requirements** — the basis of `P04-F-34`, of `12`'s revaluation contradiction
> and of `15`'s `D-P04-03` disagreement. **The register behind this package's
> entire retire-end standard analysis sat outside every standing check**, which
> is P07's `S` in a different domain and at smaller scale.
>
> **And `D` carries a stem collision `P04-F-117` did not catch**, because a family
> classed as a non-identifier is never examined for one: `D-1`…`D-7` are mine;
> **`D-11` and `D-12` are P11's Boss decisions.** Both now attributed at their
> citations, per *rename what is yours, attribute what is inherited*.
>
> **A second inconsistency, and it is `P04-F-113`'s own rule turned on it.**
> `U` is classified **foreign** — P07's — yet `09` §5A tabulated `U-20` and `U-29`
> as `` | `U-20` | P07 | `` rows, and **a backticked identifier in the first cell
> is this package's definition convention.** The owner column said P07; the
> checker could not read it. Rewritten `` P07 `U-20` ``. **A foreign identifier
> put into an owned table's shape is defined by that shape, whatever the prose
> beside it says** — which is exactly the `EC` inconsistency P07 found in its own
> classification, arriving here through a table I built for the joint runtime ask.
>
> **Unit `[1]` now derives the family set and fails on any unclassified family**,
> rather than iterating a literal. Final: **49 families derived, 0 unclassified,
> 19 owned swept, 0 orphans beyond the intentional one.**
>
> **Declared residue, and it is the expected one.** The consistency check still
> reports `U` as defined here — because **this finding quotes the defective row
> to describe it**, and the quotation has the shape it is describing. One
> occurrence, in `01` §6A.36, declared exactly as the bare-identifier residue was
> at `P04-F-115` and the stem residue at `P04-F-117`.
>
> **Third appearance of the same recursion, and it is no longer a surprise:** a
> register that documents its own defects necessarily contains instances of them,
> so the terminating move is always **declaration taken last, expressed as a
> bound** — never a further correction, which would only add a fourth instance.
>
> Class: **FACT VERIFIED**, family set derived rather than declared, both
> corrections applied, one quotation residue declared.

### 6A.35 The sweep could not see a deleted deliverable

P07 audited its own claim that *"every sweep now counts its failures"* rather than
repeating it, and found a different silent path: its sweep builds its file list
from `os.listdir()` and regenerates the manifest **from that list**, so a deleted
deliverable vanishes from both and the run reports a clean result **over a smaller
set**. Its fix: a set-integrity unit diffing on-disk against `git ls-tree HEAD`.

**Tested here. The same gap, by the same construction.**

> **P04-F-135.** **Deleting a deliverable leaves this package's sweep reporting
> `stale = 0`.** Reproduced on a copy:
>
> | | files on disk | manifest pairs | stale |
> |---|---:|---:|---:|
> | baseline | **21** | 20 | 0 |
> | after deleting one deliverable | **20** | 20 | **0** |
>
> The manifest check reads `if os.path.exists(f) and hash != h` — **the guard that
> keeps it from crashing on a missing file is what makes a missing file
> invisible**. And the on-disk count was printed on every run and **never asserted
> against anything**, so 21 becoming 20 changes no reported number.
>
> **This is `P04-F-106` surviving the unit written to enforce it.** That finding
> added the manifest-hash check on the principle that *agreement between two
> records is not evidence that either is right* — and the check it produced
> compares **the manifest to the files** and neither to **the committed set**. Two
> records can agree perfectly on a set that has lost a member.
>
> **Unit `[0]`, set integrity, added — with both controls, per `P04-REV-67`:**
>
> | control | result |
> |---|---|
> | on-disk `.md` set vs `git ls-tree HEAD` | **21 = 21**, no missing, no untracked |
> | same test on a copy with one deliverable deleted | **FIRES** — names the missing file |
>
> **Six units, disjoint targets:** set integrity · identifiers (18 families) ·
> per-table structure · manifest-hash agreement · Layer-1 scrub · empty-sentinel.
>
> Class: **FACT VERIFIED**, defect reproduced, unit added, both controls
> published.

> **P04-F-136.** **P07's account of the difference between our two erasures is
> accepted and is the sharper statement.** Its defect swallowed an exception —
> the failure at least *occurred*. Mine **produced exit code 9 and routed it to
> `/dev/null`**: the distinguishing datum existed and was discarded, after which
> the branch treated *"not a backup"* and *"never opened"* as one outcome.
>
> > **When a test's failure mode and its negative result share a return path, the
> > test cannot state a negative.** Give failure its own channel before trusting
> > any zero.
>
> That is the general form of everything this package recorded about nulls —
> `P04-F-98` (a parse failure grouping as a value), `P04-F-103` (empty hashes
> reading as unanimity), `P04-F-124` (a batch absence reading as a finding),
> `P04-F-133` (a row ceasing to exist). **All four are one defect: the channel
> that reports failure was the channel that reports results.**
>
> Class: **FACT VERIFIED** as a classification of this package's own defects.

### 6A.34 The same file, and the clause that made it vanish

P07 diagnosed the archive independently and **it is the same file** — byte figures
reproducing exactly, same absent central directory, same collision with a keyed
identity at a date neither of us holds. It was missed there **twice**: the
undeclared `Library` prune removed it from the population, and when a later sweep
did reach the subtree, an `except Exception: pass` in the zip branch **silently
dropped it** rather than counting it unreadable.

**My census has the identical defect by a different mechanism, and I have
reproduced it.**

> **P04-F-133.** **My census's zip branch discarded the exit status, so an
> unreadable archive and a correctly-rejected one are the same event.**
>
> The branch is `unzip -l "$f" 2>/dev/null | grep -q 'dump\.sql'`. Run against
> both cases:
>
> | archive | `unzip -l` exit | branch result |
> |---|---|---|
> | `odoo-19.0.zip` — readable, genuinely not a backup | **0** | NO MATCH |
> | `BK12MAY26_2026-06-23` — **unreadable** | **9** | NO MATCH |
>
> **Both produce "NO MATCH". One is a correct rejection; the other is a file
> never inspected.** The exit status distinguishes them and the pipeline throws it
> away — `2>/dev/null` on a command whose *failure* is the finding.
>
> **So the archive was absent from `P04-F-126`'s 39 not because it failed the
> shape test but because it was never tested**, and nothing in the census output
> said so. Only the complement sweep found it, and only because that run **counted
> its own failures instead of discarding them.**
>
> **This is the selective null in its quietest form.** `P04-F-124` described a
> batch reporting absence for some rows — visible as a pattern. This is **one row
> ceasing to exist**: no wrong value, no anomalous group, nothing to notice. P07's
> formulation is the one to keep: **the first defect removed it from the
> population; the second removed the evidence that anything had been removed.**
>
> Every sweep in this package now reports its own failure count. `P04-F-127`'s 141
> was that rule applied to directories; this is the same rule owed to files, and
> it was not paid until now.
>
> Class: **FACT VERIFIED**, both cases executed, exit statuses published.

> **P04-F-134.** **`P04-B-48` and P07's `U-33` are the same artefact, so they are
> one request rather than two.** Both packages independently found the same
> damaged archive, gave it the same diagnosis, and reached the same undecidable
> question — *third snapshot of a keyed identity, or an unkeyed one* — because
> `BK12MAY26` is a keyed identity in **both** registers (`66d1b52a`), held in both
> only at 2026-08-03, against this file's 2026-06-23.
>
> **Neither of us would have had it alone:** P07 had the file and no name for it —
> its two defects had erased it from every count — and this package had the name
> only because the complement sweep counted read failures. **The name identified
> the file; the file confirmed the name.**
>
> **P07's fourth disposition class is adopted here**, because this package's three
> do not fit it either: not *NOT YET READ* (it has been reached), not *NOT ON THIS
> HOST* (it is materialised locally), not *EVIDENCE NEVER RECORDED* (it was
> recorded — the recording is damaged).
>
> > **PRESENT AND UNREADABLE** — the evidence exists, is materialised on this
> > host, and is not recoverable without **changing the estate**.
>
> **Consequence for the runtime request at `09` §5A**: it is now **four items in
> two asks**. `U-20`, `U-29` and `P04-B-47` need **an execution**; `P04-B-48` /
> `U-33` need **one archive recovered** — and recovering it **answers both
> packages at once**, which no other item in either register does.
>
> Class: **FACT VERIFIED** — same path, same byte figures, same diagnosis,
> independently obtained.

### 6A.33 The residue, named

P07's complement sweep returned **zero of the inverse shape across 3,133 archives,
with 1 unreadable** — and it declared that one as **a bound of one, not a zero**,
because its script had not recorded which. Asked of my own sweep, which reported a
bare zero: **I had not counted unreadable archives either.**

> **P04-F-132.** **1 of 1,002 zip archives ≥ 1 MB under the declared roots cannot
> be read, and it is named for a database.**
>
> `BK12MAY26_2026-06-23_13-15-32.zip`, 1.08 GB, under Google Drive. Diagnosed
> rather than assumed:
>
> | test | result |
> |---|---|
> | materialised on disk? | **yes** — 1,081,946,112 bytes allocated against 1,081,942,526 logical. **Not a cloud placeholder.** |
> | leading bytes | `50 4b 03 04` — **a zip** |
> | first 1 MB readable? | **yes** |
> | central directory | **end-of-central-directory signature not found** |
>
> So it is **structurally damaged, not absent and not unmaterialised** — the file
> is entirely on disk and its index is missing.
>
> **This is the only named residue either package produced, and it is worse than a
> nameless one.** `BK12MAY26` is the *name* of a keyed identity — `66d1b52a`, of
> which I hold two snapshots, **both dated 2026-08-03**. This archive is dated
> **2026-06-23**, which is a date I do not hold for it, and sits between
> `f4a44cce` (03-30) and those two. So it is **either a third snapshot of a keyed
> identity or an unkeyed one**, and by `P04-F-126`'s own rule — *a file name is
> not a database identity, in either direction* — **I cannot say which without
> reading it, and I cannot read it.**
>
> **Disposition: it joins the class that is not closable by research.** Like
> `P04-B-46`'s two source-less modules, this is **evidence that exists on this
> host and cannot be read from it**. Recovering it means repairing a 1 GB archive,
> which is a change to the estate and outside this package's brief.
>
> **So `P04-F-126`'s 39 and `P04-F-131`'s zero both carry a declared bound of
> one.** Neither is amended: 39 remains the count of artefacts the signatures
> matched, the zero remains the complement result, and **this is the one archive
> that could have been either and cannot be tested.** A zero with a named
> exception is a different statement from a zero, and the difference is the whole
> reason for saying it.
>
> Class: **FACT VERIFIED** as to the diagnosis; **NOT READABLE** as to content.
> Registered `P04-B-48`.

### 6A.32 The census closed in the other direction

`P04-F-130` tested what the census **admitted**. It did not test what the census
could have **missed** — and the two are different questions. The census keyed on a
member named `dump.sql`; a backup whose payload carried any other name, with a
root `manifest.json` beside it, would never have been recorded and no shape test
run afterwards could find it, because it was never a candidate.

> **P04-F-131.** **Zero archives on this host have a root `manifest.json` without
> a root `dump.sql`.** Every `.zip` ≥ 1 MB under the declared roots was listed and
> tested for the inverse shape. **None.** Control published: a known Odoo backup
> shows **root `manifest.json` = 1 and root `dump.sql` = 1**, so it is correctly
> *excluded* from the candidate set — the test is capable of returning a name it
> is looking for, and returns none.
>
> **So `P04-F-126`'s 39 is now bounded in both directions** under its declared
> path set, size floor and signatures: nothing admitted that should not have been
> (`P04-F-130`, two rejected), and **nothing missed that should have been**
> (this finding, zero candidates).
>
> **The asymmetry is worth naming because it is the one every tightening in this
> thread shared.** Tightening a predicate can only ever *shrink* what it admits —
> so each of `P04-F-127`, `-129` and `-130` could confirm the census was not too
> loose, and **not one of them could show it was not too narrow.** That needs the
> inverse test, and it had not been run. **A discriminator validates the set it
> accepted; only its complement validates the set it never saw.**
>
> **AMENDED — the control published with this finding was only half a control.**
> What I published was an **exclusion** control: a known backup shows both members
> and is therefore correctly *not* flagged. That proves the predicate does not
> misfire. **It does not prove the predicate fires**, and a zero from a test never
> shown to detect anything is the *control-that-cannot-fail* pattern this package
> recorded at `P04-F-109` — committed here, one commit after recording it, in a
> finding whose entire content is a zero.
>
> **P07 built the missing half by synthesising the artefact, and I have run it.**
> A zip carrying a root `manifest.json` and a payload named **`backup.sql`** — the
> exact class the census could never have reached:
>
> | control | result |
> |---|---|
> | inverse predicate on the synthesised artefact | **FIRES** — root manifest 1, root `dump.sql` 0 |
> | original census clause on the same artefact | **no match — it would have been missed** |
> | inverse predicate on a known real backup | does **not** fire — correctly excluded |
>
> **So the class is real and constructible, the census was demonstrably blind to
> it, and the sweep's zero is now a controlled negative rather than an
> uncontrolled one.** The finding's conclusion is unchanged; its evidentiary
> standing is not.
>
> Class: **FACT VERIFIED (negative)**, every zip ≥ 1 MB under the declared roots,
> **both controls published — exclusion and firing.**

### 6A.31 The shape test, applied systematically to my own census

P07 applied the shape discriminator to its 22 and reached **20** — **finding the
same two archives, independently**, `CFF.zip` and `docker-compose-magento.zip`,
both nested-only. I had withdrawn those two **by hand**, on inspection, and had
never applied the test systematically to the other ten.

> **P04-F-130.** **Applied to all 12 zips in the census, the shape test confirms
> the composition and rejects exactly the two already withdrawn.**
>
> | class | count |
> |---|---:|
> | `PGDMP` magic | **27** |
> | root `dump.sql` **and** root `manifest.json` — the shape the product writes | **10** |
> | root `dump.sql`, **no** manifest — a distinct export shape, kept and declared | **2** |
> | nested `dump.sql` only — **not backups** | **2** (withdrawn) |
> | **total** | **39** |
>
> Control: a known Odoo backup reads **root `dump.sql` = 1, root `manifest.json`
> = 1**.
>
> **The number does not move; the basis does — for the third time in this
> thread.** `P04-F-126` withdrew two archives on a hand inspection I described in
> prose. They are now rejected by a **stated, executable predicate** that also
> licenses the other ten, and the two kept-but-different exports are **declared as
> a distinct shape rather than counted silently.**
>
> **And P07 reaching the same two archives from the other side is the only
> instance in this exchange of a discriminator being validated by independent
> application.** Every other agreement between us has been about a fact; this is
> agreement about a **test** — it was proposed here, applied there, and returned
> the same two rejections out of two different candidate sets.
>
> **The distinction that made it work is worth stating once more, because it is
> the whole of what three rounds of tightening produced:** *a name test asks what
> a file is called; a shape test asks what wrote it.* Both of us tightened the
> name twice and were still admitting source archives; neither tightening could
> express the difference, because the difference is not in the name.
>
> Class: **FACT VERIFIED**, 12 archives tested, control published, composition
> unchanged at 39.

### 6A.30 The disagreement resolved — and I had misdescribed my own predicate

P07 re-classified its 36 **by why each artefact matched** and found **14 were
source-code archives**, each caught by a **0 KB `neutralize.sql` shipped inside a
module** — one of them a zip of its own declared source set. **36 → 22. Under the
strict criterion the two sweeps reconcile exactly: 22 = 22.** My three tests found
nothing because **none of them was the cause**: the cause was a clause in its
scan, not a coverage difference in mine.

**Checking the same clause against my census found a defect in my *description*,
not my count.**

> **P04-F-129.** **`P04-F-126` and `P04-F-127` misstate this package's own census
> predicate. The zip test did not accept "any `.sql` or a `manifest.json`" — it
> required a member named `dump.sql`.** I attributed the predicate of the earlier
> **reconnaissance** scan to the **census**, and published it twice.
>
> Determined from behaviour rather than memory: `odoo-19.0.zip` (73
> `neutralize.sql` members) and `02_OTHER.zip` (260) **match the loose clause and
> are absent from the census**, while `CFF.zip` and `docker-compose-magento.zip`
> **are present** — and each of those contains a member *named* `dump.sql`. The
> census clause is therefore `grep 'dump\.sql'`, unanchored.
>
> **The two withdrawals at `P04-F-126` were correct, for a better reason than I
> gave.** `CFF.zip`'s `dump.sql` is **sample data inside a Gantt charting
> library**; `docker-compose-magento.zip`'s is a **Magento acceptance-test
> fixture**. Same failure mode as P07's `neutralize.sql` — *a database-shaped
> filename shipped inside source* — reached by a different filename.
>
> **So name-anywhere is insufficient, and that is the transferable half.** P07
> tightened from *any `.sql`* to *a member named `dump.sql`*; this package was
> already there and **was still admitting two source archives.** The discriminator
> that actually separates a backup from source is **`dump.sql` at the archive
> root with `manifest.json` beside it** — the shape the product writes — and
> neither of our published clauses said so.
>
> **`P04-F-126`'s 39 is unaffected**: the two were already withdrawn on
> re-testing, and the source archives never entered. **What changes is that the
> method statement was wrong and is now correct.**
>
> **And the reason it was found at all is worth recording.** I did not re-read my
> script; I ran its clause against three archives and compared the answers to the
> census output. **A method statement is a claim, and the only way to check it is
> to execute it and see whether the results match what was published.**
>
> Class: **FACT VERIFIED** — predicate determined behaviourally, four archives
> tested, census output compared.

### 6A.29 A cross-party count disagreement, left unreconciled

P07's `~/Library` re-run reports **36 database artefacts** in the subtree its
census had silently pruned — more than its entire published census found — and
confirms the severity ranking measured rather than argued: **its suppressed
subtree held 36, mine held 0.** That part is accepted; it was measured on its
side and it is its own defect to report.

**What is not accepted is the number as a correction to mine.**

> **P04-F-128.** **My census found 22 artefacts under `~/Library`; P07 reports 36
> in the same subtree. I cannot reproduce the difference, and I am not adopting
> it.**
>
> Three candidate causes tested, each with a firing control:
>
> | candidate cause | test | result |
> |---|---|---|
> | **no plain-SQL signature** — my census had only `PGDMP` magic and zip-with-`dump.sql`, so an uncompressed text dump would match neither | every file ≥1 MB under `~/Library`, first 200 bytes, matching *"PostgreSQL database dump"* | **0** — control fires on a known plain dump |
> | **my ≥1 MB floor** | every file 1 KB–1 MB under `~/Library`, both signatures | **0** — control fires on `PGDMP` magic |
> | **suppressed directories** | `2>/dev/null` entries enumerated at `P04-F-127` | **141, all OS privacy containers** |
>
> **The missing plain-SQL signature is a real defect and is now declared** — it is
> a third undeclared bound in the same script, after the two at `P04-F-127`. It
> simply **cost nothing in this subtree.**
>
> So the disagreement stands: **22 against 36, unexplained from my side.** It
> could be a broader signature set, a lower size floor, a different notion of
> what counts as an artefact, or a genuine gap in my scan that none of these
> three tests reaches.
>
> **What settles it is P07's path list, not its count** — the same rule this
> package has applied to every cross-party number: *a joint tally is executable by
> neither party; two declared halves, each executed by its owner, then compared as
> paths.* Requested; **`P04-F-126`'s 39 is not amended in the meantime**, and it
> is recorded here that an independent sweep of one subtree returned a larger
> figure I could not reproduce.
>
> **The one point of agreement is worth stating**, because it is the only
> cross-validation either census has: P07 names
> `premiumflexiblepackaging-pfp-odoo-staging-…` among its 36, and it is in my 39.
> **Two independently-bounded sweeps agree on that artefact**, which is a
> stronger basis for that one file than either sweep alone.
>
> Class: **DISAGREEMENT RECORDED, NOT RESOLVED.** No count amended, no finding
> moved; every database-derived finding here remains bounded to a named identity
> and all eight were keyed and read.

### 6A.28 What my own census narrowed without declaring it

P07 found **two undeclared narrowings inside its census script** — eight directory
exclusions including **`Library`**, the subtree its own module enumeration had
drawn from, and a narrower zip signature — in a section whose entire purpose was
declaring the root set. Its conclusion: *a census that declares its roots and
silently prunes one of them has declared a boundary it did not use.* **The same
question, asked of `P04-F-126`, finds two.**

> **P04-F-127.** **Two undeclared narrowings in this package's census. Both
> measured; neither changes the count.**
>
> **1 — `2>/dev/null` silently dropped every unreadable directory, and the number
> was never taken.** Measured now: **141 stderr entries against 1,070,459
> directories traversed.** All 141 are macOS privacy containers — `~/.Trash`,
> `~/Library/Accounts`, `Application Support/CloudDocs`, `com.apple.TCC` and
> similar. They are implausible database stores, **but that is a judgement, and
> the defect was that no number existed to judge.** Now it does.
>
> **2 — the gzip branch was far narrower than the other two signatures.** It
> decompressed **200 bytes** and matched one string, *"PostgreSQL database
> dump"* — so a gzipped **custom-format** archive, whose payload begins `PGDMP`
> and carries no such text, would have been missed entirely. Re-tested over
> **all 72** gzip archives ≥ 1 MB under the declared roots, reading **4,096
> bytes** and matching **either** `PGDMP` magic **or** the SQL header:
> **none is a database.** Positive control published: the same test **fires on a
> known `PGDMP` dump after gzipping it**, so the zero is absence and not a dead
> predicate.
>
> **So `P04-F-126`'s 39 stands** — and it stands for a different reason than
> before. It was published on a scan with an unmeasured exclusion and an
> untested signature branch; it now rests on **141 exclusions enumerated** and
> **72 candidates individually tested with a firing control.** *The number did
> not move and the basis did.*
>
> **This is the third undeclared bound found inside a correction of an undeclared
> bound**, after `P04-F-113` (the family list) and `P04-F-124` (six identities of
> eight). The pattern is stable enough to state as a rule: **a script's declared
> parameters are the ones its author was thinking about; the narrowings live in
> the error handling, the defaults, and the branch nobody exercised.**
>
> Class: **FACT VERIFIED**, 1,070,459 directories, 141 exclusions enumerated,
> 72 gzip candidates tested with a positive control.

### 6A.27 The host census, completed — and what it does not say

The full-host census declared at §6A.1 has finished. It ran for the greater part
of this session and is reported here with its bounds, its defect, and — most
importantly — **its unit.**

> **P04-F-126.** **39 database artefacts on this host. The identity count is
> NOT established, and this finding does not state one.**
>
> **Declared:** path set `/Volumes` + `$HOME`; size bound **≥ 1 MB**, justified —
> the smallest Odoo dump observed anywhere here is 3.37 MB; two signatures —
> `PGDMP` magic, and zip central directory containing `dump.sql`.
>
> | | |
> |---|---:|
> | `PGDMP` archives | **27** |
> | zip archives containing `dump.sql` | **12** |
> | **total database artefacts** | **39** |
> | artefacts reached via the `/Volumes/iMac` symlink | **0** |
>
> **The symlink result closes a claim I made on reasoning rather than evidence.**
> I told P07 that `find` without `-L` cannot traverse `/Volumes/iMac` — a symlink
> to `/` — and that my sweep was therefore not inflated. That was correct, and it
> was **an argument, not a measurement**, until this run: **zero of 39 artefacts
> lie under that path.**
>
> **The census pattern was over-inclusive and two artefacts are withdrawn.** The
> zip test required a member **named `dump.sql`, anywhere in the archive** —
> *not* "any `.sql` or a `manifest.json`", which was this package's own
> misdescription of it, corrected at `P04-F-129`. Re-tested for the
> Odoo backup shape, `CFF.zip` and `docker-compose-magento.zip` contain **neither
> `dump.sql` nor `manifest.json`** and are not database artefacts. Two others —
> `premiumflexiblepackaging-*-exact_fs.zip` — contain `dump.sql` **without** a
> manifest, a different export shape; **counted, because excluding them would be
> the narrow-pattern error this package has recorded twice.**
>
> **And the unit is the whole point.** **39 is a count of FILES.** Only **8**
> identities have been keyed on `database.uuid` (§6A.25). The remaining ~31
> artefacts are **un-keyed**, and the precedent forbids inferring: `iTEST02`
> appears as **four copies of one snapshot** and the two `iEVING` files are **two
> different databases**. **A file count converts to an identity count in neither
> direction without reading `ir_config_parameter` in each.**
>
> So the census settles the **artefact** question and leaves the **identity**
> question where it was: **8 identities keyed; the population remains OPEN.**
> Newly visible and never keyed by any session in this exchange: `iErpOCC`,
> `iSCErP`, `iSMeO2C`, `iSMEs182`, `iMSCG` ×2, `odoo_cff_golive`, two
> `premiumflexiblepackaging` exports, two archives inside a messaging app's media
> store, and the seven `OCC_Odoo18_Simulation_Lab` snapshots already known to
> share one uuid.
>
> **No finding in this package moves.** Every database-derived finding is bounded
> to a named identity, and all eight named identities were keyed and read. What
> this changes is the **floor**: the estate is at least 39 artefacts wide, and
> this package has read 8 identities out of an unknown total.
>
> Class: **FACT VERIFIED** as to 39 artefacts under the declared bounds;
> **identity count NOT ESTABLISHED**, stated as such.

### 6A.26 The absence that licenses the instrument, disproved three ways

P07 observed that its own negative-control rows are **absences inside an
otherwise-successful table** — the shape `P04-F-124` identifies as the most
dangerous — and that they are the **highest-stakes absences in its package**,
because they are what permits the claim that the instrument distinguishes a real
absence from a failed read. It re-tested them by three independent instruments.
**The same is true here and I had not done it either.**

> **P04-F-125.** **`96548e18`'s missing `account.asset` — the single row that
> licenses the whole registry instrument — confirmed by three independent
> instruments, each with its own positive control.**
>
> | instrument | result | its control |
> |---|---|---|
> | `ir_model` | 510 models, **no `account.asset`** | `res.company` **present**, `account.move` **present** |
> | `ir_module_module` | 1,334 module rows, 123 installed; `account_asset` **`uninstalled`** | `account` **installed** `18.0.1.3`, `base` **installed** `18.0.1.3` |
> | archive table listing | **0** `COPY public.account_asset` blocks | `account_move_line` **1**, `res_company` **1** |
>
> **Three instruments, three positive controls firing, three absences agreeing.**
> The discriminating control in `P04-F-124` is licensed, and with it the claim
> that the registry route can tell a real absence from a failed read.
>
> **And this package's version establishes the mechanism, where P07's could
> not.** Its cert module had **no row at all**, so *why* it was absent was
> undetermined — correctly recorded as *not established and not needed*. Here the
> module row **exists with state `uninstalled`**: the asset module is **present in
> the deployment's addons path and deliberately not installed**. That is the same
> distinction `P04-F-97` drew for `scgl_advance_expense_request` — **not deployed
> versus not available** — and it means `96548e18` is not an incomplete capture
> but a **complete capture of an install that chose not to run the asset module**.
>
> Class: **FACT VERIFIED**, three instruments, six controls, one archive.

### 6A.25 Six identities was also a chosen population

P07 found that its registry run covered **5** identities while its own census says
**7**, and that the two omitted were **the never-transacted installs** — by this
exchange's repeated result, the most informative rows available. Checked here
immediately: **`P04-F-123` ran six identities; this package's census holds eight.**

> **P04-F-124.** **The two omitted identities were `a1430edc` and `f4a44cce`, and
> `f4a44cce` is the never-transacted v19 install — the same class P07 omitted, for
> the same reason.** Complete run, both controls, all eight:
>
> | identity | gen | models | (+) `res.company` | `account.asset` | (−) `account.asset.impairment` | four classes |
> |---|---|---:|---|---|---|---|
> | `551ab874` | v18 | 944 | yes | yes | absent | **none** |
> | `4b766580` | v18 | 1,080 | yes | yes | absent | **none** |
> | `96548e18` | v18 | 510 | yes | **no — correctly** | absent | **none** |
> | `45a8e08e` | v16 | 601 | yes | yes | absent | **none** |
> | `1f6338ae` | v19 | 749 | yes | yes | absent | **none** |
> | `f4a44cce` | v19 | 633 | yes | yes | absent | **none** |
> | `66d1b52a` | v19 | 756 | yes | yes | absent | **none** |
> | `a1430edc` | v19 | 1,035 | yes | yes | absent | **none** |
>
> **8 identities · 3 generations · 6,308 model rows · zero models of any of the
> four asserted-absent classes**, with a positive control firing in all eight, a
> discriminating control correctly absent in exactly one, and an explicit negative
> control (`account.asset.impairment`, a model that should exist nowhere) absent
> in all eight. P07's refinement adopted: **an all-positive control set proves the
> read worked and cannot distinguish an instrument that reads correctly from one
> that answers *present* to anything.**
>
> **And the run produced two false absences that were not data.**
> - **A wrong path read as an empty result.** A first attempt pointed at
>   `f4a44cce` under a directory that does not exist; `unzip` produced nothing,
>   the parser reported **"no `ir_model` block"**, and the message was
>   indistinguishable from a genuine absence. The file was in a different
>   directory and holds **633 models**.
> - **A batch harness reported three identities absent that individual runs
>   disprove.** In a loop, `4b766580`, `96548e18` and `f4a44cce` all returned
>   *no block*; run one at a time, the same command on the same files returns
>   **1,080**, **510** and **633**. The zips are readable and each contains
>   exactly one `COPY public.ir_model` line — verified before re-running.
>
> **Neither was published, and the second is the more dangerous.** A uniform
> failure across every row announces itself; a failure on **three of eight rows,
> inside an otherwise-successful table**, reads as a finding about those three.
> **Always disprove a batch absence with a single run before it becomes a row.**
>
> Class: **FACT VERIFIED**, 8 identities, 6,308 models, controls published per
> row. Limits unchanged: this host's estate; absence of a model is not absence of
> a behaviour.

### 6A.24 The no-host claims across the whole estate

> **P04-F-123.** **Zero models of the four asserted-absent classes across 6
> identities, 3 generations and 4,640 model rows.** See the table at §6A.23. The
> claims that lease accounting, impairment, useful-life review and an
> assets-under-construction stage have **no host** are no longer a reading of one
> source tree, nor of one deployment: they are tested against **every model
> registry on this host**, each maintained by its own deployment.
>
> **What this does not remove:** the estate is this host's. A model absent from
> all six may exist in an install not captured here, and **absence of a model is
> still not absence of a behaviour**. Both limits are unchanged from `P04-F-122`
> and neither is removable from this host.
>
> Class: **FACT VERIFIED**, controls published per identity.

### 6A.23 The absence-of-a-class claims — and a route P07 said did not exist

P07 found two negatives its convergence could not reach: *"no tenant ORM model
exists anywhere"* is **not a claim about a model, it is a claim about the absence
of a class of model**, and an analysis starting from *which modules declare on
which models* cannot bound it. **The same class is here and it is larger:** this
package makes roughly a dozen **"no host"** claims — four unhosted lifecycle
stages, the TAS 16 count, no assets-under-construction stage, no lease module, no
useful-life review, no asset-register reconciliation — and `P04-F-116`,
`P04-F-118` and `P04-F-121` reach **none** of them.

> **P04-F-122.** **A class-absence claim can be bounded — not by the module
> route, but against the deployment's authoritative model registry.**
> *(Identifier written as its own bold span: the first draft put the id and the
> headline inside one span, which this package's own checker cannot match —
> third occurrence of that formatting defect, caught by the check in the same
> run.)* `ir_model` in
> `551ab874` holds **944 models**. Testing each asserted-absent class against all
> 944:
>
> | asserted absent | models of any name in the deployment |
> |---|---|
> | lease | **none** |
> | impairment | **none** |
> | useful-life / residual review | **none** |
> | assets under construction | **none** |
> | asset transfer | `account.transfer.model` — **periodic account transfers, not assets** |
> | scrap | `stock.scrap` — **inventory scrap, not assets** |
> | revaluation | 3 models — **all FX and inventory valuation, none an asset revaluation** |
>
> The whole asset domain is **three models**: `account.asset`,
> `account.asset.group`, `account.asset.report.handler`. **No impairment, no
> revaluation, no transfer, no construction stage.**
>
> **So the no-host claims are, for the first time, tested against a deployment
> rather than against a source tree** — and they hold. This is a **stronger basis
> than the one they were published on**, and it reaches the claims that the
> module route could not.
>
> **And the near-misses are the point.** `stock.scrap`, `account.transfer.model`
> and `stock.valuation.layer.revaluation` all exist. **A whole-product phrasing —
> *"no scrap concept exists"*, *"no revaluation anywhere"* — would have been
> falsified by them.** The claims survive because they were bounded to the asset
> module. That is `P04-F-121`'s inversion demonstrated on live counter-examples
> rather than argued: **the narrow boundary was not modesty, it was what made the
> claim true.**
>
> **The route generalises and I am handing it back to P07**, whose `N-25` is of
> exactly this shape: *enumerate the deployment's authoritative model registry and
> test the class against all of it.* It does not need the module→model map, so it
> is not blocked by the reason P07 gave.
>
> **Limits, both real.** The registry is **one deployment's** — a model absent
> here may exist in an install not on this host, so this bounds *this* estate, not
> the product. And a *capability* can exist without a model: a field on an
> existing model, or a method. **Absence of a model is not absence of a
> behaviour** — it is decisive only for claims phrased, as these are, about a
> missing **record type**.
>
> **Extended to every readable identity, after P07 ran the same route across five
> of its own** (`P04-F-123`):
>
> | identity | gen | models | control — `account.asset` present | lease · impair · useful-life · AUC |
> |---|---|---:|---|---|
> | `551ab874` | v18 | 944 | yes | **none** |
> | `4b766580` | v18 | 1,080 | yes | **none** |
> | `96548e18` | v18 | 510 | **no — correctly** | **none** |
> | `45a8e08e` | v16 | 601 | yes | **none** |
> | `1f6338ae` | v19 | 749 | yes | **none** |
> | `66d1b52a` | v19 | 756 | yes | **none** |
>
> **6 identities · 3 generations · 4,640 model rows · zero models of any of the
> four classes anywhere.**
>
> **The control's failure in `96548e18` is the strongest row in the table.** That
> is the never-transacted v18 install where the asset module is **not installed**
> — so `account.asset` is genuinely absent from its registry, the control
> correctly reports absent, and the instrument is shown to **distinguish a real
> absence from a failed read**. Five identities where the control fires and one
> where it correctly does not is a better validation than six where it fires.
>
> Class: **FACT VERIFIED**, **4,640 models across 6 identities and 3 generations**,
> 7 classes tested, controls published per identity. The claim is no longer
> bounded to one deployment; it is bounded to **this host's estate**, which is the
> limit that remains and cannot be removed from here.

### 6A.22 Every negative, re-audited against the boundaries that moved

P07 audited its seventeen negative rows by **declared boundary** and found the
ones bounded to a **path set** and to a **volume** both invalidated by boundary
changes this session made — including one underpinning its tenant finding. Its
counter-case is the transferable half: **the four negatives written with an
explicitly narrow boundary are the only ones that did not go stale.** Run here
over all ten declared negatives.

> **P04-F-121.** **Nine of ten negatives survive the boundary changes; one does
> not, and it is the one already identified.**
>
> Four boundaries moved in this package: the archive **signature set**
> (`P04-F-86`), the archive **path set** (`P04-F-88` withdrawn), the **source
> scope** (`P04-F-93`, 27 installed modules in neither declared root), and the
> **generation basis** (`P04-F-85`). Only the third can reach a negative here,
> because all ten are bounded to **modules**, not to a volume or a tree.
>
> The test: for each negative, does any of the 27 undeclared-but-deployed modules
> declare fields or views on the model that negative concerns?
>
> | negative | exposure |
> |---|---|
> | no scrap · no impairment · no transfer · no partial disposal · no scheduled action | **none** |
> | no purchase- or receipt-driven asset creation | **none** |
> | no manufacturing-to-asset route | **none** |
> | no borrowing-cost capitalization | **none** |
> | no asset-specific close or report-driven recomputation | **none** |
> | **no operation-to-equipment reference** | **`equipment_fleet`** |
>
> **Nine are protected by `P04-F-116`** — no installed module outside the declared
> scope declares on `account.asset`. The tenth concerns
> `maintenance.equipment`, where `equipment_fleet` does, **and whose source is
> nowhere on this host** — the same module, the same exposure, and the same six
> findings already partitioned at `P04-F-118`. **The exposure is one boundary,
> one model and one module wide, and it has now been reached from three
> independent directions.**
>
> **P07's inversion is confirmed here and is worth more than the audit.** These
> ten were written with **narrow, module-scoped** boundaries — *"the asset
> module"*, *"the loans module"*, *"reporting modules"* — never *"the source
> tree"* or *"the volume"*. **They survived a change that invalidated an entire
> declared root.** P07's path-set-bounded and volume-bounded negatives did not.
>
> > **A negative that declares a narrow boundary survives a boundary change; one
> > that declares the widest boundary available at the time does not.**
>
> Which inverts the instinct: **the negative that sounds strongest is the one
> that rots.** *"Not found anywhere on the volume"* is a bigger claim than *"not
> found in the asset module"*, and it is the bigger claim that a later discovery
> destroys.
>
> **Limit, stated because it is the same one-directional bound as everywhere
> else:** *protected* means **no undeclared module declares on that model** —
> `ir_model_data` sees XML-id declarations only. A module could override a method
> and declare nothing. **A floor, not a proof**, and the nine are safer than they
> were, not safe.
>
> Class: **FACT VERIFIED**, ten negatives audited against four moved boundaries,
> one exposed, nine protected to the stated floor.

### 6A.21 The qualifier check, made usable

> **P04-F-120.** **The rule published at `P04-F-119` was noisy enough to be
> unusable, and applying P07's discriminator to it found one more stale
> assertion — a settled negative that is now false.**
>
> `P04-F-119` said: *enumerate a narrowed finding's citations by identifier and
> require the qualifier on each.* Run literally over nine narrowed findings here
> it returns **74 citations**. P07 ran the same rule over its eight and got
> **162**, and named the failure before either of us shipped it: **a check that
> flags 162 where 3 are real is worse than no check** — the reader stops reading
> the output, which is this package's own `P04-F-111` warning turned on its own
> newest rule.
>
> **P07's discriminator: require the qualifier only where the citation *asserts*
> the narrowed claim.** Applied here — excluding defining blocks, which state a
> claim before their own qualification, and revision-log rows, which record
> history:
>
> | | |
> |---|---:|
> | citations of narrowed findings | 74 |
> | defining blocks | 9 |
> | history rows | 32 |
> | **assertive, live** | **18** |
>
> Seventeen of the eighteen carry their qualifier. **One does not**, and it is
> not a wording slip: `01` §6A.1 still asserted **"No sixth database exists under
> the stricter method"**. A sixth and seventh snapshot were found, then
> `idemo18_uat` — **the database two blockers were held open on** — then two more
> v18 identities. **The sentence had been false for eleven commits.**
>
> **It survived the correction that fixed the identical claim in `18`
> `P04-REV-27`.** Same sentence, same session, two locations; the revision log was
> corrected and the trace file was not — which is `P04-F-119` recurring **inside
> the finding that established it**, one commit later, and found only because
> P07's refinement made the check readable enough to act on.
>
> Corrected in place with the original struck through, not deleted: a **settled
> negative asserted from a re-run** is the error `P04-F-105` classifies, and the
> record should show it was made rather than show a clean page.
>
> Class: **FACT VERIFIED**. Rule as it now stands: **enumerate by identifier —
> indifferent to phrasing — but require the qualifier only on citations that
> assert the claim.** The first half is this package's, the second is P07's, and
> the rule is unusable without both.

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
