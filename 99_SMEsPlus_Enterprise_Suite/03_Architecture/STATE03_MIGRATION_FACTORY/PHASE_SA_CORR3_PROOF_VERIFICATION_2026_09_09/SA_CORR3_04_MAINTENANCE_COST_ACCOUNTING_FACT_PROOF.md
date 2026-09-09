# `SA_CORR3_04` — MAINTENANCE COST TO ACCOUNTING FACT — PROOF

**Phase SA CORR3 · BLK-07 targeted very deep study, master prompt §7 · SMEs Core**
**Finding prefix `MNT-` · Frame: `CORR3-FRAME` (cited, not re-declared)**
**Design content is `DESIGN CANDIDATE`. Nothing here is approved, frozen, or authorised for development.**

> **Orchestrator intake note.** This artifact was produced by a same-model executor and is labelled
> `INTERNAL ADVERSARIAL SELF-CHALLENGE`. It was **not adopted on the executor's word**. Two
> load-bearing claims were re-verified against primary text before acceptance: `MNT-F-12` (the
> `SA_CORR2_05` tally contradiction — confirmed: line 69 reads `14 + 3 + 1 = 18`, line 232 reads
> `13 of 18 reconciled, 4 …`) and `MNT-F-10` (`BLK-08` exists, is maintenance-specific, and carries
> the recommendation `Split` — confirmed at `09_P04_BOSS_DECISION_REGISTER.md` line 23). The
> executor's own residual-uncertainty section is preserved unedited.

---

## 1. Scope, instrument, and controls

### 1.1 What this artifact owns and what it does not

Master prompt §7 commissions the study of **maintenance cost becoming an accounting fact**. Master
prompt §6 separately commissions the **production overhead absorption chain** in `SA_CORR3_03`.

The boundary held here: this artifact determines **which maintenance cost enters the §6 chain, on
what criterion, carrying what dimensions, owned by whom**. It does **not** redesign the absorption
arithmetic, the normal-capacity denominator, or the under/over-absorption remainder — those are
§6's. Where a route hands over, the handover is named.

### 1.2 The route list is a floor, not a denominator

Master prompt §7 reads *"Study and prove applicable routes **such as**"* followed by twelve items.
**"Such as" makes the list illustrative.** The twelve are therefore treated as a **mandated floor**,
and are used as unit `U-R` with population 12 because they are **given by the prompt, not chosen by
this author**. Routes added from evidence are reported **separately and never mixed into the
twelve** (§7.4).

### 1.3 Instrument and controls, executed

| Control | Expected | Executed result |
|---|---|---|
| Positive — `BD-ACC-01` | 55 | **55** |
| Positive — `clean.room` (`-i`) | 1,266 | **1,266** |
| Negative — `qxvz7481_no_such_token` | 0 | **0** |
| Injection — probe written, queried, removed, re-queried | 0 → 1 → 0 | **0 → 1 → 0**, blob count restored to 3,900 |
| Positive on a *second* command shape — `component depreciation` | non-zero | **17 files** |

Every count below was validated with a **second command of a different shape**. Where the two
shapes disagreed, the disagreement is published, not reconciled silently (`MNT-F-16`).

---

## 2. What CORR2 asserted, and what CORR2's own primary sources say

This section reads the **registers and their status fields**, not the headline tables.

### 2.1 The four assertions carried into Boss Decision 4

`SA_CORR2_13` §16 Decision 4:

> *"maintenance cost never becomes an accounting fact at all — `FACT VERIFIED`, denominator
> declared, `0 of 4` deployments"*, joined to **`BLK-07` normal capacity**.

Four separable assertions: **(i)** the universal negative; **(ii)** the declared denominator;
**(iii)** the `0 of 4` figure; **(iv)** the join to `BLK-07`. Each was tested independently.

### 2.2 `MNT-F-01` — the universal negative is over-wide relative to its own declared denominator

The primary source declares its denominator precisely and correctly:

> **Denominator for the negative:** every source file in the maintenance module's model directory.
> Zero references to the journal-entry model; zero to the analytic model.

That denominator supports exactly one claim: **the maintenance module's own objects do not post.**
It does **not** support *"maintenance cost never becomes an accounting fact at all"*, because
maintenance cost is overwhelmingly incurred **outside** that module — as a purchased service, as an
issued spare part, as internal labour.

**The same document says so, three paragraphs later:**

> *"A repair booked as a vendor bill is an ordinary expense with no equipment dimension; the
> equipment's cost float is not connected to it."*

A vendor bill **is** an accounting fact. So the primary source simultaneously affirms an accounting
route and is quoted for the proposition that none exists.

`SA_CORR2_06` `AR-29` then states the destination as settled:

> *"period expense, through the vendor bill, owned by Expense-to-Pay. Not production cost. Not asset
> carrying amount."*

**`MNT-F-01`.** `SA_CORR2_06` `AR-29` and `SA_CORR2_13` §16 Decision 4 assert contradictory
propositions about the same subject in the same package: that maintenance cost **reaches** the
ledger through a named route, and that it **never becomes an accounting fact at all**. The narrow
form is true and evidenced; the wide form is false and is the form escalated to Boss. **Class: scope
stated as a description rather than declared as a set.** Severity **HIGH** — it is the premise of a
Boss decision request.

### 2.3 `MNT-F-02` — the `0 of 4` figure is transplanted from a different claim about a different subject

`0 of 4` originates in a P03 register whose gate row reads:

> *"Deployments where any **machine cost** reached **finished goods**: 0 of 4."*

Its subject is **machine cost reaching finished goods** — a usage/depreciation absorption question,
measured against the work-centre rate vehicle (*"enabled on 1 of 60 work centres"*). Its subject is
**not** maintenance cost, and its predicate is **not** "becomes an accounting fact".

**`MNT-F-02`.** A denominator measured for *machine cost into finished goods* is attached,
unmodified, to a claim about *maintenance cost becoming an accounting fact*. **Neither cited primary
source measured the transplanted claim.** The `0 of 4` neither supports nor refutes the proposition
it is quoted for. Severity **HIGH**.

### 2.4 `MNT-F-03` — the eligibility of the four is not established, and is contradicted on the record

A P03 ownership matrix records, for the planned-maintenance element: *"installed in **2 of 4** DBs"*.

The maintenance-integration capability was therefore **absent from half the population** for reasons
unrelated to the design question. Two of the four are **ineligible by construction** for any claim
about the integration's behaviour: the mechanism could not exist there. Per the standing lesson that
**the four denominator clauses all assume the set is eligible**, this is an exclusion error that is
invisible inside the count.

Countervailing: `SA_CORR2_06` `AR-29` and `SA_CORR2_03` §3.4 both say the result was verified *"with
the maintenance-integration capability installed"* — which is P03 §1's statement about **its own**
verification run, not a statement that all four deployments carried it. Reading the register rather
than the summary, the two statements are compatible and the eligible denominator is **2, not 4**,
for any integration-dependent claim.

**`MNT-F-03`.** The `0 of 4` denominator is not shown eligible, and the record shows at least half
of it is not. Severity **MEDIUM-HIGH**.

### 2.5 `MNT-F-04` — what `CORR3-FRAME` can and cannot say about the four

Declared negative, with tool, pattern, path set and authority:

- **Tool**: per-blob header inspection and line-class counting, both executed.
- **Pattern, shape 1**: first line containing a column-inventory header signature.
  **Shape 2**: blobs with >200 lines matching a `name,type` column-census signature.
- **Path set**: `CORR3-FRAME` in full.
- **Result, both shapes**: **exactly one** deployed-schema column inventory and **exactly one**
  foreign-key inventory.
- **Authority for what was not searched**: `CORR3-FRAME`'s declared complement — non-head-history
  blobs, and all non-`.md`/`.txt`/`.csv` files. Runtime database artefacts on the execution host are
  **outside this frame** and are **not asserted absent**.

**`MNT-F-04`.** Within `CORR3-FRAME` the eligible deployed-schema population for a schema-level
maintenance claim is **n = 1**. This study therefore **neither reproduces nor refutes** the
`0 of 4`; it establishes that the claim the figure was attached to is a different claim
(`MNT-F-02`), which is dispositive independently of the count.

---

## 3. The evidence base for this study, declared as a claim

Per the standing rule that **the evidence base is itself a claim**:

| Source | What it is | Denominators |
|---|---|---|
| Deployed column inventory | Table/column/type census of one deployed estate | **1,396 tables · 13,941 columns** |
| Deployed foreign-key inventory | Referential census of the same estate | **5,142 foreign-key rows** |
| Standards register | TAS 2 ¶12–13 carried as translated standard text; TAS 16 gazette **unretrieved** | — |
| Allocation-cause model | The productive/non-productive cause model, `DESIGN CANDIDATE` | 8 causes |
| Allocation-driver matrix | The fixed/variable two-driver departure | 4 candidates |
| Asset↔equipment trace | Primary trace of the custom link | — |
| Boss decision — Equipment vs Fixed Asset boundary | **STANDS** | — |
| Boss decision — Work Order / Maintenance Order naming | **STANDS** | — |
| Standards audit map | `SA11-F-01`. **Both blob versions read; identical on maintenance content** | — |

**Provenance caveat on the standard text.** TAS 2 ¶12–13 is available to this study **only as text
carried inside the corpus**, classified there as `ACCOUNTING STANDARD REQUIREMENT`. This study did
**not** independently retrieve the gazetted publication. TAS 16 is worse: the same register records
the gazetted text as **located but unretrieved**, and classifies every TAS 16 conclusion as
`ACCOUNTING STANDARD INTERPRETATION`, **never statutory**. §6 states, route by route, whether an
architectural conclusion depends on this. **Thai statutory claims remain `HOLD / EVIDENCE REQUIRED`
and Thai naming remains candidate / UNVALIDATED.**

---

## 4. Business Nature decomposition of maintenance expenditure

Master prompt §7 requires classification **by Business Nature and accounting substance**, and warns
against assuming all maintenance enters manufacturing cost. The classes below are **derived
structurally from the deployed estate**, not asserted.

**Declared pattern**, executed on both artefacts: tables whose name matches
`(maintenance|repair|service|fleet|productivity)`, case-insensitive.
**Result, both shapes: 36 tables.** Of those, the columns carrying money or a ledger reference:

| Object class | Money column | Ledger reference |
|---|---|---|
| Equipment-maintenance objects (7 tables, 136 columns) | **1** — a cost attribute on the equipment master | **0** |
| Maintenance-request object (41 columns) | **0** | **0** |
| Vehicle-service-log object | **1** — an amount | **1** — a direct reference to a ledger line |
| Vehicle-contract object | **1** — an amount | 0 |
| Work-centre time-loss object | **1** — a labour cost | **1** — a direct reference to a ledger line |

**6 money-or-ledger columns across 4 tables, of 36 tables in the pattern. Both shapes agree
(grep: 6; awk: 6).**

### The five cost-origin classes (unit `U-C`, population 5)

| # | Business Nature | Where the cost arises | Reaches the ledger today? |
|---|---|---|---|
| **C1** | Maintenance **procured externally** | Vendor invoice | **YES** — as an ordinary expense, **with no maintenance, equipment, or cause dimension** |
| **C2** | **Spare parts issued from own stock** | Goods movement | **The movement posts; the maintenance identity does not exist** — `MNT-F-08` |
| **C3** | **Own labour** on a maintenance job | Duration captured on the maintenance event | **NO** — no rate, no amount, no ledger reference |
| **C4** | **Vehicle / fleet servicing** | Service-log event | **YES — completely.** Event date, service type, vendor, usage meter, amount, **and a direct ledger-line reference** |
| **C5** | Equipment **master cost attribute** | A single value on the equipment master | **NO** — it has no event grain at all |

**`MNT-F-06`.** **2 of 5 maintenance cost-origin classes reach the ledger today**, one of them
(`C4`) **complete with its own cause dimension, object identity, and usage meter**. This is a direct
structural counter-example to *"maintenance cost never becomes an accounting fact at all"*, obtained
from a **different evidence shape** (deployed schema) than the claim's source (module source tree),
on a surface the claim's declared denominator **excluded by construction**. Severity **HIGH**.
**Class: declared set vs deployed set.**

### `MNT-F-05` — the causal skeleton is complete; the monetary spine is absent

The maintenance-request object carries, in **41 columns**: the maintained object; a
**preventive/corrective type**; a duration; a scheduled window; a close date; the work centre; the
production work order; the manufacturing order; the assigned person; a work-centre-blocking flag;
recurrence; and a link to **calendar capacity removal**.

It carries **zero** monetary columns and **zero** ledger references.

**`MNT-F-05`.** The estate's maintenance defect is **not** the causal mechanism — which is richer
than either P03 or P04 recorded — but the **money**. *Cause is fully modelled and entirely
uncosted.* This **inverts** the premise of CORR2 Decision 4, which presents maintenance as *"a second
absent mechanism"* alongside fixed overhead. The absent thing is a **monetary spine on an existing
causal object**, not an absent causality. Severity **HIGH**, and it materially reduces the design
distance to closure.

### `MNT-F-07` — the asset ↔ operational-object relation exists; the register CORR2 imported says it does not

`SA_CORR2_03` §3.4 imports P03's formulation: *"Equipment → Asset: **NO** — no reference in either
direction."*

Executed against the deployed foreign-key inventory, **two shapes**:

- a direct reference from the **accounting asset object to the maintenance-equipment object**;
- a direct reference from the **accounting asset object to the vehicle object**;
- a **many-to-many relation between the accounting asset object and the equipment *category*** — a
  third relation named by neither P03 nor P04.

**Shape disagreement, published (`MNT-F-16`):** a table-prefix grep returned **4**; a target-table
filter returned **3**. Both are correct **for different units** — 3 *relations*, expressed as 4
*foreign-key rows* (the many-to-many contributes two rows). **The unit, not the population, was the
discrepancy.** Reported rather than silently reconciled.

P04 had **already narrowed** P03's claim on primary evidence: *"Custom estate: one live
one-directional many-to-one"*, with the reference product itself having none. **CORR2 imported P03's
wide version and not P04's narrowed one.** Verified, not adopted, from P04's own trace: the link is
**custom-only**, **one-way** (asset → object, no reverse), **many-to-one and unconstrained**,
**editable in every state including after full depreciation**, and drives an **irreversible** status
transition — *"4 occurrences, all one direction, 0 writes"* of the reverse — with **no company
domain**, where the comparable field has one.

**`MNT-F-07`.** The asset relationship route is **not absent**; it is **present and defective**, in
three named ways, at equipment grain. This is a materially different design position from absence.
Severity **HIGH**.

### `MNT-F-08` — the maintenance part issue cannot be identified as a maintenance part issue

`IR-18` (`SA_CORR2_05` §6) states: *"a maintenance part issue is a stock movement whose cost has no
destination."*

Executed on the foreign-key inventory, **two shapes**: the **only** reference of any kind between the
stock domain and the maintenance domain is a **location reference on the equipment master** — *where
the equipment physically sits*. There is **no reference from any goods movement to any maintenance
object**, and **none in the reverse direction**.

**`MNT-F-08`.** `IR-18` is correct that the cost has no destination, and it stops one level too
late. **The movement cannot be identified as maintenance consumption at all**, so the question of its
destination cannot even be posed at the movement grain. The gap is **upstream** of the cost
destination: it is an **identification** gap, and it is cheaper to close (a reference) than a
valuation gap would be. Severity **HIGH**, and it **narrows and re-prices** `IR-18` rather than
contradicting it.

### `MNT-F-09` — the ownership answer CORR2 reports as verified was declined by both parties

The P04→P05 handoff asks P05 verbatim: *"When a repair is paid as a vendor bill, does anything
connect that expense back to the equipment it repaired? **P04 asserts only that the asset/maintenance
side has no link**"* — materiality **High**, and *"P04 asks nothing to be decided."*

P05's own boundary register answers: *"P05 has **not** determined whether any expense should be
capitalised… P05 did **not** wait for P04 and did **not** consume P04 output"*, and *"P05 classifies
the obligation, not the machine."*

**`MNT-F-09`.** `SA_CORR2_06` `AR-29` records the destination as `FACT VERIFIED` — *"owned by
Expense-to-Pay"* — for a question the sending party explicitly left open and the receiving party
explicitly declined. **No party verified it.** **Class: peer status-field rule.** Severity **HIGH**:
an unowned route is being reported as an owned one, and ownership is exactly what §7 asks this study
to establish.

### `MNT-F-12` — `SA_CORR2_05` contradicts its own corrected tally

Line 69: *"14 + 3 + 1 = 18"*, with an explicit correction note recording that the table *"first
published 13 / 4 / 1"* and was wrong. Line 232, the closing checkpoint of the **same file**:
*"**13 of 18 reconciled, 4 partial, 1 not reconciled**"*.

**`MNT-F-12`.** The correction was applied to the table and **not** to the checkpoint line that
reports it — on the very register that carries `IR-18`. **Class: a revision log is not a correction;
audit the text by identifier, not the disposition column.** Severity **MEDIUM**. This artifact's own
closing checkpoint (§13) is checked against its own tables for the same defect.

---

## 5. The accounting-substance fork, and the single criterion it turns on

### 5.1 The three destinations, and what decides between them

| Destination | Criterion | Standard basis in corpus | Class |
|---|---|---|---|
| **Period expense** | The expenditure neither (i) converts materials into finished goods nor (ii) meets asset-recognition criteria | Default; also TAS 2 ¶13 for the unabsorbed remainder | Requires no standard to reach — it is the residual |
| **Conversion cost, absorbed into inventory** | The expenditure is an **indirect cost of production** on an asset **used in the production process** | TAS 2 ¶12, which **names maintenance of factory buildings and factory equipment by example** | `ACCOUNTING STANDARD REQUIREMENT` — carried text, not independently retrieved |
| **Capitalised to the asset** | The expenditure meets asset-recognition criteria — subsequent expenditure, component replacement, major overhaul | TAS 16 | `ACCOUNTING STANDARD INTERPRETATION` — **gazette unretrieved** → **HOLD on the criterion threshold** |

### 5.2 `MNT-F-17` — the whole fork turns on one classification that exists nowhere

Every branch above is selected by one predicate: **is the maintained object used in the production
process?**

- If **no** → period expense. Nothing else needs deciding, and **normal capacity is irrelevant**.
- If **yes** → conversion cost, and the absorption arithmetic engages.
- Independently, if the expenditure meets recognition criteria → capitalise, whether or not the
  object is productive.

The allocation-cause model already records this: *"only the depreciation of assets used in the
production process enters this model… The reference product has no such classification — the asset
grouping object carries no behaviour — so SMEsPlus must add one."*

**`MNT-F-17`.** The **production / non-production classification of the maintained object** is the
single criterion the entire maintenance fork depends on, it does **not** exist in the estate, and it
is **not gated by any Boss decision** — it is a classification of accounting substance. It is the
**highest-leverage single design act** in this study: it alone splits maintenance into the branch
that needs `BLK-07` and the branch that never touches it. Severity **HIGH**. Owner: **SMEs Core**.

### 5.3 Fixed versus variable — where `BLK-07` does and does not reach

`BLK-07` is, on the record: *"the allocation denominator — normal capacity or actual hours"* for
**fixed** production overhead.

The corpus already establishes that **the two classes take different bases**:

| Cost class | Required basis | Gated by `BLK-07`? |
|---|---|---|
| **Fixed** production overhead | **Normal capacity** | **YES** |
| **Variable** production overhead | **Actual use** of the production facilities | **NO — a different basis entirely** |

TAS 2 ¶12 names maintenance in the **fixed** class by example, and states the classifying criterion
in the same sentence: *indirect costs of production that remain relatively constant regardless of
production volume.* Maintenance expenditure that **varies directly with volume** —
consumption-driven part replacement, usage-metered servicing — is **variable production overhead by
the stated criterion** and is allocated on actual use. It **never reaches the `BLK-07` question**.

### 5.4 Downtime is a denominator input, not a cost route — and the hook already exists

The corpus establishes, from ¶13's own definition of normal capacity, that **planned maintenance is
subtracted from the denominator when normal capacity is set**, and therefore **must not also
generate a charge** — *"Expensing it as well would charge it twice."* Unplanned maintenance does the
reverse.

**`MNT-F-14`.** Two structural facts close this route further than any register records:

1. The maintenance-request object carries a **preventive/corrective type** — the split data
   **already exists**, confirmed independently here at deployed-schema level; the corpus states
   *"No new capture is required."*
2. The maintenance-request object carries a **direct relation to calendar capacity removal**, and a
   **work-centre-blocking flag**. **The mechanism by which planned maintenance removes capacity from
   the denominator is structurally present in the deployed estate.**

So the downtime route's *treatment* is determined by the standard, its *data* exists, and its
*capacity mechanism* exists. What remains is confirmation of the split — which is **`BLK-08`**, not
`BLK-07`.

### 5.5 `MNT-F-10` — CORR2's Decision 4 names the wrong blocker for the part it does gate

`BLK-08` exists in the corpus, is already open, is already Boss-owned, and reads verbatim:

> *"Does maintenance split into planned (absorbed) and unplanned (period expense)?"* —
> recommendation **Split**; *"The non-productive model cannot be finalised"* without it.

There is also a standing ownership row: *"`OWN-10` — **Maintenance** cost, planned and unplanned —
Asset/maintenance domain — Asset track — `BLK-08` open."*

**`MNT-F-10`.** The corpus contains a **maintenance-specific Boss blocker**, already raised, already
carrying a recommendation, with an ownership row naming maintenance cost by name.
**`SA_CORR2_13` §16 Decision 4 does not name it**, and instead joins maintenance to `BLK-07`, whose
subject is a denominator. **The join is attached to the wrong blocker even for the portion that is
genuinely Boss-gated.** Severity **HIGH**.

### 5.6 `MNT-F-11` — the capitalization fork has zero coverage anywhere in the corpus

Declared negative, fully specified:

- **Tool**: `q.sh` (`grep -rlE -i`), then a second shape, `find … -print0 | xargs -0 grep -il`.
- **Patterns**: `subsequent expenditure`; `component replacement`; `major inspection`.
- **Path set**: `CORR3-FRAME` in full, `U1` = 3,900 blobs.
- **Result**: **0 blobs on all three patterns, on both shapes.**
- **Positive control on the same shape**: `component depreciation` → **17 blobs**.
- **Injection control**: 0 → 1 → 0, verified, blob set restored to 3,900.
- **Authority for what was not searched**: `CORR3-FRAME`'s declared complement. Not asserted absent
  there.

**`MNT-F-11`.** The **capitalization branch of maintenance — subsequent expenditure, component
replacement, major overhaul — has never been addressed anywhere in this corpus.** This is not a
defect in an existing answer; it is a route with no coverage at all. It is a **SMEs Core design
act**, not a Boss decision, because the criterion is accounting substance — with the criterion
**threshold** on HOLD pending TAS 16 primary text. Severity **HIGH**.

### 5.7 `MNT-F-15` — event ownership, posting ownership, reversal and audit trail are already decided

`BD-ACC-01` **stands** and reads: Accounting Core owns the canonical immutable Accounting Event
Identity, distinct from source-document number, journal number and reconciliation matching number;
**Source Module owns the Business Fact; Posting Engine owns Ledger Posting**; retry is idempotent;
**reversal is a new event referencing the original**; event identity is Tenant + Company bounded.

Applied to maintenance, with **no new decision required**: the **maintenance domain owns the
maintenance business fact**; **Accounting Core owns the posting and the event identity**; **a
maintenance correction is a new event referencing the original**, never an edit.

The Boss decision on the *Equipment vs Fixed Asset boundary* supplies the object ownership the ruling
presupposes: **Equipment is the operational object; Fixed Asset is the accounting classification;
not every Equipment is a Fixed Asset; an Equipment may optionally link to a Fixed Asset**, and
*"Operational lifecycle and accounting lifecycle remain separate responsibilities while preserving
traceability."*

The Boss decision on *Work Order / Maintenance Order naming* supplies the event vocabulary and the
cross-domain chain, and already separates **Preventive** from **Corrective** and names **Downtime**
as a first-class item.

**`MNT-F-15`.** Four of the twelve mandated routes — **accounting event ownership, posting
ownership, reversal/correction, and the object-ownership half of asset relationship** — are
**already settled by standing Boss rulings**. What is missing is the **`XD-06` contract**, which
`SA_CORR2_06` §6 itself assigns to **SMEs Core** with *"No Boss decision required — the ruling
exists."*

---

## 6. Route-by-route register (unit `U-R`, population 12, given by master prompt §7)

Statuses use two independent axes, never conflated: **SEMANTIC** (is the accounting answer
determined?) and **MECHANISM** (does a route exist to deliver it?).

| # | Route | Business Nature | Accounting substance | Cost destination | Accounting event owner | Posting owner | Status (semantic / mechanism) |
|---|---|---|---|---|---|---|---|
| **R1** | Maintenance expense directly to period cost | Upkeep of a **non-production** object | Period cost; residual branch, **reachable under any framework** | **Period expense, classified by cause** | Maintenance domain | Accounting Core | **DETERMINED** / **PARTIAL** — exists for `C1`, `C4`; absent for `C3`; unidentifiable for `C2` |
| **R2** | Maintenance related to production equipment | Upkeep of an object **used in production** | **Conversion cost** — TAS 2 ¶12 names it by example | **Inventory value**, via §6's chain | Maintenance domain | Accounting Core | **DETERMINED** / **ABSENT** — the production classification does not exist |
| **R3** | Capitalization where appropriate | **Subsequent expenditure, component replacement, major overhaul** | Increases carrying amount; replaced component **derecognised** | **Asset carrying amount** | Maintenance raises; Asset recognises | Accounting Core | **HOLD — criterion threshold** / **ABSENT — zero corpus coverage** |
| **R4** | Production cost allocation | Production-object maintenance, **fixed vs variable** | Fixed → normal capacity. **Variable → actual use** | Inventory value | Maintenance domain | Accounting Core | **SPLIT**: variable **DETERMINED**; fixed **GATED — `BLK-07`** / **ABSENT** |
| **R5** | Asset relationship | Equipment ↔ Fixed Asset traceability | Optional link; **not every operational object is a Fixed Asset** | n/a — a dimension | — | — | **DETERMINED** by standing ruling / **PARTIAL — DEFECTIVE**: 3 relations, one-way, unconstrained, irreversible, no company domain |
| **R6** | Work Center relationship | Maintenance against equipment serving a work centre | Locates cost object and capacity effect | n/a — a dimension | Maintenance domain | — | **DETERMINED** by standing ruling / **PRESENT** |
| **R7** | Downtime effects | **Planned** vs **unplanned** capacity loss | **Planned reduces the denominator**; **unplanned is period expense**. Charging planned twice is the error the standard prevents | Planned → absorbed; unplanned → period expense | Maintenance domain | Accounting Core | **DETERMINED BY STANDARD; CONFIRMATION GATED — `BLK-08`** / **PARTIAL** |
| **R8** | Monthly close | Period-end disposition of the unabsorbed remainder | **Unallocated production overhead is expensed in the period incurred**; remainder decomposed by cause, reconciling to zero | Period expense, **reported by cause** | Accounting Core | Accounting Core | **DETERMINED** / **ABSENT** — no reconciliation exists to run |
| **R9** | Accounting event ownership | All classes | **Source Module owns the Business Fact** | n/a | **Maintenance domain** | Accounting Core | **DETERMINED — `BD-ACC-01`** / **ABSENT — contract unpublished (`XD-06`)** |
| **R10** | Posting ownership | All classes | **Accounting Core owns Ledger Posting and event identity**; retry idempotent | n/a | Maintenance domain | **Accounting Core** | **DETERMINED — `BD-ACC-01`** / **ABSENT — `XD-06`** |
| **R11** | Reversal / correction | All classes | **A reversal is a new event referencing the original**; never an edit | Reverses to origin | Maintenance domain | Accounting Core | **DETERMINED — `BD-ACC-01`** / **PARTIAL** — carried defect: entries can be silently re-dated past a period lock |
| **R12** | Audit trail | All classes | Cause, object, meter, amount and event identity persist on the posted fact | n/a | Maintenance domain | Accounting Core | **DETERMINED** / **PARTIAL** — inherits the same lock defect; **not maintenance-specific** |

### 6.1 Tally, executed by reading the status column above rather than asserted

**Semantic**: `DETERMINED` **10** (R1, R2, R5, R6, R7, R8, R9, R10, R11, R12) · `SPLIT` **1** (R4) ·
`HOLD` **1** (R3). **10 + 1 + 1 = 12.** ✓
**Mechanism**: `PRESENT` **1** (R6) · `PARTIAL` **5** (R1, R5, R7, R11, R12) · `ABSENT` **6**
(R2, R3, R4, R8, R9, R10). **1 + 5 + 6 = 12.** ✓
Every identifier `R1`…`R12` appears **exactly once**.

**Does the architectural conclusion depend on the Thai statutory material?**

- **R1, R5, R6, R9, R10, R11, R12 — NO.** They rest on Boss rulings that stand, on the deployed
  structure, and on the residual nature of period cost. They hold under any recognition framework.
- **R2, R4, R7, R8 — YES**, on TAS 2 ¶12–13 as carried in the corpus. If that text were withdrawn,
  the *requirement* to absorb and the *denominator* constraint would both lapse.
- **R3 — the requirement that a capitalization route exist does NOT depend on it**; the **criterion
  threshold** does, and TAS 16 is on **HOLD / EVIDENCE REQUIRED**.

---

## 7. The (a) / (b) / (c) decomposition, with sizes

### 7.1 Primary-blocker partition of `U-R` (population 12, mutually exclusive, exhaustive)

| Bucket | Routes | **Size** |
|---|---|---|
| **(a) Decidable on accounting substance alone → closes at SMEs Core, no Boss decision** | R1, R2, R5, R6, R8, R9, R10, R11, R12 | **9 of 12 — 75%** |
| **(b) Genuinely gated behind the `BLK-07` normal-capacity decision** | **R4, and only its fixed-class absorption arithmetic** | **1 of 12 — 8%** |
| **Gated behind a *different* Boss item (`BLK-08`)** | R7 | **1 of 12 — 8%** |
| **Blocked by an evidence gap, not a decision (TAS 16 unretrieved)** | R3 | **1 of 12 — 8%** |

**9 + 1 + 1 + 1 = 12.** ✓

### 7.2 (c) — design gaps, reported as a **separate, cross-cutting count**

**(c) is not a member of the §7.1 partition and is not added to it.** A route can be semantically
closed and mechanically empty; that is the normal case here. Stated explicitly, because the failure
mode that produced `MNT-F-12` is exactly a cross-unit tally added as though it were one unit.

| (c) sub-class | Routes | Size |
|---|---|---|
| **No cost destination** | R2, R4 | 2 |
| **No accounting event** | R3, R8 | 2 |
| **No posting owner *contract*** (owner ruled, contract unpublished — `XD-06`) | R9, R10 | 2 |
| **Mechanism present but defective** | R1, R5, R7, R11, R12 | 5 |
| **Mechanism sound** | R6 | 1 |

**Mechanism `ABSENT` on 6 of 12 (50%); `PARTIAL` on 5 of 12 (42%); `PRESENT` on 1 of 12 (8%).**
These are **SMEs Core design acts**, every one.

### 7.3 Second unit `U-C` — cost-origin classes (population 5)

| | Size |
|---|---|
| Classes that reach the ledger today | **2 of 5** (`C1`, `C4`) |
| Classes reaching the ledger **with a cause dimension** | **1 of 5** (`C4` only) |
| Classes with **no monetary representation at all** | **2 of 5** (`C3`, `C5`) |
| Classes where the **maintenance identity itself is absent** | **1 of 5** (`C2`) |

**The universal negative fails on 2 of 5 classes. The useful narrow claim — *no maintenance cost
reaches the ledger carrying a maintenance cause dimension* — fails on 1 of 5** and is therefore
**also not universal**, though it is very nearly so.

### 7.4 Routes added by evidence — reported separately, never merged into the twelve

| ID | Route the twelve do not name | Why it is separate | Owner |
|---|---|---|---|
| **A1** | **Identification** of a goods movement as maintenance consumption | Logically upstream of "cost destination"; `MNT-F-08` | SMEs Core |
| **A2** | **Derecognition of a replaced component** on capitalization | Counterpart of R3; omitting it double-counts the asset | SMEs Core, threshold on HOLD with R3 |
| **A3** | **Production / non-production classification of the maintained object** | The single criterion the whole fork turns on; `MNT-F-17` | SMEs Core |

**3 added routes. `U-R` remains 12.** All three fall in **(a) semantically** and **(c) mechanically**.

---

## 8. Verdict on CORR2's join of maintenance to normal capacity

> ## `MNT-V-01` — **THE JOIN IS OVER-WIDE, AND IT IS ALSO MIS-ADDRESSED.**

**Over-wide**, on size: **11 of 12 mandated routes do not require the normal-capacity decision.**
`BLK-07` decides a **denominator**. A denominator cannot be applied to a cost that has no accounting
existence, no cause dimension and no cost object — so every question about **capture,
identification, classification, posting, ownership, reversal, audit trail, period expense, and
capitalization** sits **upstream** of `BLK-07` and is untouched by whichever way it is decided.
**`BLK-07` reaches exactly one route (R4), and within it, only the absorption arithmetic of the fixed
class — not the classification that decides membership of that class.**

**Mis-addressed**, on identity: the portion of maintenance that *is* Boss-gated is gated by
**`BLK-08`** — a blocker that **already exists, is already open, already carries the recommendation
`Split`, and has an ownership row naming maintenance cost by name** (`MNT-F-10`).

**Founded on a premise that does not hold**: Decision 4's stated ground is that *"maintenance cost
never becomes an accounting fact at all"*. That proposition is **over-wide relative to its own
declared denominator** (`MNT-F-01`), **contradicted by the register's own §3 and by `AR-29` in the
same package**, **carries a denominator transplanted from a different claim about a different
subject** (`MNT-F-02`) **whose eligibility is contradicted on the record** (`MNT-F-03`), and is
**structurally falsified on 2 of 5 cost-origin classes** (`MNT-F-06`).

**And the direction of the gap is inverted**: CORR2 presents maintenance as *"a second absent
mechanism"*. The mechanism that is absent is **not causality — which is complete and richer than the
registers record — but money** (`MNT-F-05`).

### `MNT-F-13` — the residue, sized

| | Before this study | After |
|---|---|---|
| Routes escalated to Boss under `BLK-07` | **12 of 12** (the whole subject, by the join) | **1 of 12**, and only its arithmetic |
| Routes closing at SMEs Core on accounting substance | 0 stated | **9 of 12** |
| Routes gated by a **different, already-open** Boss item (`BLK-08`) | 0 stated | **1 of 12** |
| Routes blocked by an **evidence gap**, not a decision | 0 stated | **1 of 12** |

**`MNT-F-13`. The Boss residue for maintenance is approximately one-twelfth of the size the join
implies, and the single largest gated item is not the one named.** Severity **HIGH**.

**Stated against my own bias, because this conclusion is convenient.** This study narrows a Boss
escalation, which is the direction an executor is biased toward. Tested against the opposite
reading: *is any route in (a) actually gated by normal capacity and hidden there?* The test is
whether the route's **answer changes** depending on which denominator Boss picks. For R1, R5, R6,
R9, R10, R11, R12 it demonstrably does not. For R2 and R8 it does not either: R2's classification is
a property of the maintained object, and R8's remainder-to-period-expense rule holds under both
denominators (only the remainder's *size* changes). **If Boss judges that no maintenance design work
may begin while any absorption input is undecided, holding the whole subject is a coherent position
and this artifact supports it without amendment** — but it should then be recorded as a **sequencing
choice**, not as the evidenced scope of `BLK-07`.

---

## 9. Accounting semantics determined by this study (SMEs Core, `DESIGN CANDIDATE`)

Semantics only. **No functional design, no data-model design, no interface design, no application
code.** Justified independently of any vendor product (§10).

| ID | Determination | Ground |
|---|---|---|
| **`MNT-D-01`** | **The maintained object carries a production / non-production classification, and it is an accounting property, not an operational one.** Nothing else in the fork can be decided before it | `MNT-F-17` |
| **`MNT-D-02`** | **A maintenance completion is an accounting event.** It carries, at minimum: the **cause** (preventive/corrective), the **maintained object**, the **period**, the **amount**, the **usage meter reading where one exists**, and the **canonical event identity**. Business fact owned by the maintenance domain; posting by Accounting Core | `BD-ACC-01`; `MNT-F-05` |
| **`MNT-D-03`** | **A maintenance expenditure is classified before it is posted, never after.** Order: recognition criteria → capitalise; else production object → conversion cost; else → period expense. **An unclassified maintenance cost is a control failure, not a residual bucket** | §5.1 |
| **`MNT-D-04`** | **Planned maintenance reduces normal capacity and generates no separate charge; unplanned maintenance does not reduce the denominator and does generate one.** Charging planned maintenance twice is the specific error this prevents | §5.4; **subject to `BLK-08`** |
| **`MNT-D-05`** | **A goods movement consumed by maintenance carries the maintenance event identity.** Without it the movement is indistinguishable from any other issue and no destination can be selected. This closes `IR-18` at its actual grain | `MNT-F-08` |
| **`MNT-D-06`** | **Capitalised subsequent expenditure derecognises what it replaces**, in the same accounting event. **Threshold on HOLD** pending TAS 16 primary text; the **requirement is not** | `MNT-F-11`; `A2` |
| **`MNT-D-07`** | **A maintenance correction is a new event referencing the original.** Direct application of a standing ruling; **no new decision** | `BD-ACC-01` |
| **`MNT-D-08`** | **The equipment master cost attribute is not an accounting figure and must not be represented as one.** No event grain, no period, no counterpart | `MNT-F-05` |

---

## 10. What was declined, and what was not copied

- **Declined: copying a vendor maintenance module.** No object model, field set, state machine,
  module structure, naming, or navigation from any examined product is proposed for adoption. The
  examined estate is used **only as evidence of what does and does not happen**, never as a design.
- **Declined: adopting the one complete chain found.** The vehicle-servicing surface (`C4`) is the
  only maintenance cost reaching the ledger with its own cause dimension. It is cited as a
  **falsifier of a universal negative** and **explicitly not** proposed as a pattern to replicate.
- **Declined: adopting the master-data cost attribute** as any part of a costing route (`MNT-D-08`).
- **Declined: inheriting a peer's reading.** P03's *"no reference in either direction"* was **not**
  adopted; it was re-executed and narrowed (`MNT-F-07`). `SA_CORR2_06`'s `AR-29` ownership statement
  was **not** adopted; both registers were read and both decline it (`MNT-F-09`).
- **Independently justified**: every determination in §9 is grounded in a standing Boss ruling, the
  accounting substance of the transaction, or the standards text carried in the corpus — **never**
  in "the reference product does it this way".

---

## 11. Findings register

| ID | Finding | Severity |
|---|---|---|
| `MNT-F-01` | *"Maintenance cost never becomes an accounting fact at all"* is over-wide relative to its own declared denominator, and is contradicted by its own source §3 and by `AR-29` in the same package | **HIGH** |
| `MNT-F-02` | The `0 of 4` denominator is transplanted from *machine cost into finished goods*; neither source measured the transplanted claim | **HIGH** |
| `MNT-F-03` | The four are not shown eligible; the record says the integration was installed in **2 of 4** | **MED-HIGH** |
| `MNT-F-04` | Within `CORR3-FRAME`, deployed-schema population is **n = 1**; the `0 of 4` is out-of-frame and is neither reproduced nor refuted here | **MEDIUM** |
| `MNT-F-05` | **The causal skeleton is complete and the monetary spine is absent** — 41 columns of cause, 0 of money. Inverts the "second absent mechanism" premise | **HIGH** |
| `MNT-F-06` | **2 of 5 cost-origin classes reach the ledger; 1 with a full cause dimension.** Universal negative falsified on a surface its denominator excluded | **HIGH** |
| `MNT-F-07` | Asset ↔ operational-object relation **exists** — 3 relations / 4 FK rows — one-way, unconstrained, irreversible, no company domain. CORR2 imported P03's wide version, not P04's narrowed one | **HIGH** |
| `MNT-F-08` | **No reference in either direction between the stock and maintenance domains.** `IR-18`'s gap is an *identification* gap upstream of the cost destination | **HIGH** |
| `MNT-F-09` | The P04→P05 handoff question was **declined by both parties**; `AR-29` reports its answer as `FACT VERIFIED` | **HIGH** |
| `MNT-F-10` | **`BLK-08` is the maintenance-specific blocker and Decision 4 does not name it** | **HIGH** |
| `MNT-F-11` | **Zero corpus coverage** of subsequent expenditure / component replacement / major inspection — 3 patterns, 2 shapes, positive and injection controls | **HIGH** |
| `MNT-F-12` | `SA_CORR2_05` line 232 contradicts its own corrected table at line 69 (`13/4/1` vs `14/3/1`) | **MEDIUM** |
| `MNT-F-13` | **The Boss residue is ~1/12 of the size the join implies, and the largest gated item is not the one named** | **HIGH** |
| `MNT-F-14` | **Downtime is a denominator input, not a cost route** — preventive/corrective type *and* capacity-removal relation both structurally present | **MED-HIGH** |
| `MNT-F-15` | Event ownership, posting ownership, reversal and object ownership are **already decided**; only the `XD-06` contract is missing, and it is already SMEs Core-owned | **MED-HIGH** |
| `MNT-F-16` | Two shapes returned **4** and **3** for the asset↔object relation count. **The unit differed, not the population.** Published, not silently reconciled | **LOW** |
| `MNT-F-17` | **The production / non-production classification of the maintained object is the single criterion the whole fork turns on, exists nowhere, and is gated by no Boss decision** | **HIGH** |

**17 findings. Every identifier `MNT-F-01`…`MNT-F-17` appears exactly once.** ✓

---

## 12. Exact Boss decisions that survive the qualification test

Two survive; **all other maintenance content is SMEs Core work.**

**`MNT-B-01` — `BLK-08`, restated with its evidence complete.**
Does maintenance split into **planned** (absorbed through the normal-capacity rate) and **unplanned**
(period expense)? The standards text carried in the corpus requires the split; the split data already
exists in the estate; the capacity-removal mechanism already exists. **This is the blocker that
actually gates maintenance, and Decision 4 does not name it.** A recommendation already stands on the
record: **Split**.

**`MNT-B-02` — `BLK-07`, correctly scoped.**
The normal-capacity denominator, gating **one route (R4), in its fixed-class absorption arithmetic
only** — **not** the classification that decides membership of that class, and **not** the eleven
other routes.

**Explicitly NOT requested:**
- Any decision on period expense, capitalization, event ownership, posting ownership, reversal,
  audit trail, work-centre relationship, or object classification — **decidable on accounting
  substance, closing at SMEs Core**.
- Re-decision of the Equipment / Fixed Asset boundary or the Maintenance Order vocabulary — **both
  already ruled and both stand**.
- Authorisation of research into maintenance routing — **`TVDR-05` is re-owned, and this artifact
  discharges the re-owned question**.

---

## 13. Residual uncertainty, proof gaps, and what a challenger should attack first

### (a) Residual uncertainty

1. **The standards text is carried, not retrieved.** TAS 2 ¶12–13 reaches this study only through a
   corpus blob. Per the standing secondary-source rule, **a summary may locate a source but never be
   the evidence.** **R2, R4, R7 and R8 depend on it; R1, R5, R6, R9–R12 do not.**
2. **TAS 16 is a declared evidence gap.** The capitalization **criterion threshold** is on
   **HOLD — EVIDENCE REQUIRED**. The **requirement** that R3 and `A2` exist does not depend on it.
3. **`LATENT vs LIVE` is unresolved for the defects in `R5` and `R11`.** Both are established
   **structurally**; this study did **not** measure whether either has fired. Source structure cannot
   establish reachability; severity ranking of those two is **provisional**.
4. **`C3` (own labour) rests on an absence of columns.** A labour rate could be supplied by
   configuration outside the schema. The claim is *"no monetary representation on the maintenance
   event"*, which the schema does establish; it is **not** a claim that no organisation costs
   maintenance labour by other means.
5. **The category-grain asset↔equipment-category relation is reported as existing, not as
   understood.** Its behaviour was not traced. Neither prior register named it.
6. **Thai localization terms** in the Boss naming decision are referenced, not validated, and remain
   **candidate / UNVALIDATED**.

### (b) What could not be proved, and the exact proof gap

| # | Not proved | Exact gap |
|---|---|---|
| 1 | That `0 of 4` is or is not correct | Requires the four runtime artefacts. **Zero are in `CORR3-FRAME`** — n = 1, two shapes. A **path-set gap**, closable only by naming and reading the four deployments' artefacts on the execution host. *(Standing lesson: never declare a database absent from a frame not drawn to include it.)* |
| 2 | That any maintenance cost **has** or **has not** reached inventory value in any deployment | Requires posted-row evidence with a state basis (posted / draft / cancelled). **No such extraction is in-frame.** Every claim here is **schema-structural**: structure proves possibility, not occurrence |
| 3 | That the vehicle-servicing ledger reference is **populated**, not merely present | A column that exists may be null on every row. `MNT-F-06`'s falsification is **structural** — it proves the estate provides a route, **not** that the route carried traffic. **The wide claim it falsifies does not require occurrence to fall** |
| 4 | That the twelve routes are exhaustive | §7 says *"such as"*. **The population is a floor.** Three routes were added; more may exist. Every size in §7 is a **ratio over a declared floor**, not over a proven universe |
| 5 | That `BLK-08`'s recommendation is safe to adopt | Its ground is the standards text of residual uncertainty #1 |
| 6 | Whether the four routes settled by `BD-ACC-01` are settled **for maintenance specifically** | The ruling is general and its **contract (`XD-06`) is unpublished**. **`MNT-F-15` claims the decision exists, not that the interface does** |

### (c) The claims a challenger should attack first, in order

1. **`MNT-V-01` and its sizing (`MNT-F-13`).** This is the disposition, it narrows a Boss escalation,
   and it is the convenient conclusion. **Attack the primary-blocker assignment directly**: for each
   of the nine routes in (a), ask whether its *answer* — not its *magnitude* — changes with the
   denominator. If any one does, (a) drops to 8 and (b) rises to 2.
2. **`MNT-F-06`, the falsification of the universal negative.** It rests on **one** deployed-schema
   artefact and on **structure, not occurrence**. **Attack the class boundary of `U-C`**: five classes
   were derived from a declared pattern; a different defensible pattern could yield a different
   denominator, and every ratio in §7.3 moves with it.
3. **`MNT-F-02`, the denominator transplant.** Load-bearing, and rests on reading two source
   documents' *subjects* as different. A challenger who shows P03's *"machine cost"* was intended to
   include maintenance cost would restore the `0 of 4` — though `MNT-F-01` and `MNT-F-06` still stand
   independently.
4. **`MNT-F-17` and `MNT-D-01`.** **Attack by finding a route in §6 decidable without the
   classification.** If one exists, the design ordering in §9 is wrong even if every finding is right.
5. **The §6.1 and §7.1 tallies.** `MNT-F-12` records a peer publishing a corrected table and an
   uncorrected checkpoint in the same file. **Re-execute both tallies by reading the status columns**,
   and verify that §7.2's (c) count was **not** added into §7.1's partition.

---

`CP-SA-C3-10 (maintenance limb) — MAINTENANCE COST TO ACCOUNTING FACT (execution status).`
**Routes mandated 12 · semantic `DETERMINED` 10, `SPLIT` 1, `HOLD` 1 · mechanism `PRESENT` 1,
`PARTIAL` 5, `ABSENT` 6 · primary-blocker partition (a) 9 / (b) 1 / `BLK-08` 1 / evidence gap 1 ·
3 routes added separately · 17 findings · 8 determinations · 2 Boss decisions survive.**

*Checked against §6.1 and §7.1 by re-reading their status columns. The (c) count of 6 is the
mechanism-`ABSENT` count and is deliberately **not** summed into the primary-blocker partition.*

Checkpoint completion is **not** Boss approval.

**Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.**
