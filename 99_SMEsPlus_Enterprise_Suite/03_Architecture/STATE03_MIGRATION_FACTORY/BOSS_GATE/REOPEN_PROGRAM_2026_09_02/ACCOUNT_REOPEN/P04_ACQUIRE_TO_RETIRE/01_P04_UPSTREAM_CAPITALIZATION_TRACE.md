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

Four PostgreSQL custom-format dumps on the host, all readable with standard
tooling. Three carry fixed-asset table data.

**Corrected twice after a peer's warning — see `18` `P04-REV-23` and `P04-REV-24`.**
The first version of this table reported four dumps, one of them with *"no asset
table data"*. That was a **false negative from the tool**, and the search that
found the four was **bounded to one directory**. Executed properly there are
**five**, and all five carry asset data.

| Database | Dated | Archive | Reads under host default client (16.15)? | Generation signature | Asset rows | Of which **real** |
|----------|-------|---------|------------------------------------------|----------------------|------------|-------------------|
| `iSMEs` | 2026-07-11 | v1.14 | **yes** | **older line** — carries an `asset_type` column the v18 source tree does not define | **685** | **669** |
| `iEVING` | 2026-07-23 | v1.14 | **yes** | **v18 line** — no `asset_type` | 36 | **0** |
| `BK12MAY26` | 2026-08-03 | v1.14 | **yes** | **v18 line** | 36 | **0** |
| `iTEST02` | 2026-07-14 | **v1.16** | **NO** — needs `postgresql@18` | **v18 line** | 12 | **0** |
| `iTEST02` | 2026-06-14 | **v1.16** | **NO** — needs `postgresql@18` | **v18 line** | 12 | **0** |

**The enumeration behind this table was re-run by a stricter method, after P07
reported the same bound in its own** (`18` `P04-REV-27`). The first search matched
on **file extension** at **bounded depth**; the re-run matched on the archive's
**magic bytes**, any extension, any depth, over both trees.

| Measure | Count | Unit |
|---------|-------|------|
| Files | **8** | one file on disk; `iTEST02` @ 2026-06-14 exists in **four** copies across trees |
| **Snapshots** | **5** | one database captured at one moment — the unit every finding below uses |
| **Database identities** | **4** | `iSMEs`, `iEVING`, `BK12MAY26`, `iTEST02` — the last captured twice |

**No sixth database exists** under the stricter method, so `P04-F-83` is not
resting on a missed artefact. Two bounds were tested rather than assumed: the
extension filter **did** cost coverage in principle and **not** in fact, and a
minimum-size filter cost nothing — **no archive on either tree is under 1 MB**.

**Readability is per artefact, not uniform** — adopted from P11, which found the
same split from the other side. *"Database evidence is available"* and *"no
database access"* are **both wrong**; the true statement is per file. A reader
with only the host's default client reproduces **three of five**, and would see
two v18-line databases rather than four.

**Scope, stated before any finding.** None of these is `idemo18_uat`, the database
the runtime capture in §6 came from. Nothing here closes a blocker that names that
database. Two of the three are a **different product generation** from the v18
source tree this package's behavioural findings rest on. Every statement below is
bounded to the database named in it.

### 6A.2 The day convention, across generations

| Database | Generation | `constant_periods` | `daily_computation` |
|----------|-----------|-------------------|---------------------|
| `iSMEs` — 669 real assets + 16 templates | older | **2** | **683** |
| `iEVING` — 36 rows, all templates | v18 | **36** | 0 |
| `BK12MAY26` — 36 rows, all templates | v18 | **36** | 0 |
| `iTEST02` @ 2026-07-14 — 12 rows, all templates | v18 | **12** | 0 |
| `iTEST02` @ 2026-06-14 — 12 rows, all templates | v18 | **12** | 0 |
| **v18 line, total** | | **96 — 100 %** | **0** |

> **P04-F-81.** The operational population runs on **daily computation** (683 of
> 685 in the only database holding real assets), while **every one of the 96 asset
> templates across all four v18-line databases is on `constant_periods`** — the
> product default, and the convention the operational population does **not** use.
> Templates govern the configuration of assets created from them. So the
> databases that would seed new assets are seeded with the **opposite**
> convention to the one in production use.
> Class: **FACT VERIFIED**, bounded to the three databases named.

> **P04-F-83.** **No v18-line database on this host contains a single real asset
> record.** **Unit declared:** four v18-line **snapshots** across **three database
> identities** (`iEVING`, `BK12MAY26`, and `iTEST02` captured twice), spanning
> 2026-06-14 to 2026-08-03, holding **96 templates and zero assets** between them.
> An earlier wording said *"four v18-line databases"*, which conflates snapshots
> with identities — the same unit defect this package records nine times over. The only population of real
> assets available anywhere is on the **older generation**.
> Class: **FACT VERIFIED**, bounded to the five databases named.
> **Reproduction caveat:** two of the four v18-line databases are v1.16 archives
> and are **unreadable by the host's default client**. A reader reproducing this
> with `pg_restore` 16.15 will see two v18-line databases, not four, and should
> not read the smaller number as a contradiction.
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
| `P04-B-16`, `B-18`, `B-19`, `B-28` | Unchanged. They concern v18 behaviour; the only database with real assets is an older generation |

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
