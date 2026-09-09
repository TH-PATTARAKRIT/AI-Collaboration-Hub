# SA_AR_04 — BOSS DECISION FAMILY PACK

## CP-SA-AR-40 — BOSS DECISION FAMILIES READY

**24 decisions · 8 families · 8 questions.** Each card carries the eighteen elements master prompt §5
requires, opens with a plain-business statement of what is actually being chosen, and ends with wording
Boss can use verbatim.

---

## 1. THE EIGHT QUESTIONS, IN BUSINESS LANGUAGE

| Family | In one plain sentence | Members | Gates Pre-Test **entry**? |
|---|---|---:|---|
| **`F1`** | When does a sale become a cost in the books, and what does a return give back? | 2 | No |
| **`F2`** | When a control trips and nobody configured a preference, do we stop the user or let them through? | 3 | No |
| **`F3`** | When goods ship supplier→customer and never touch our warehouse, does stock accounting happen at all? | 2 | No |
| **`F4`** | Does our one approved data contract cover every module boundary or just one — and can a shortage ever be cleared by buying? | 2 | **Yes** — `XMC-D-02` |
| **`F5`** | Restate two overhead blockers that can't be answered as written, and set four overhead policies | 6 | No |
| **`F6`** | May one company inside a tenant ever see another's data? | 4 | **Yes** — `MTI-D-04` |
| **`F7`** | Is a storage location something we grant permission on, and what closes two open lists? | 4 | **Yes** — `RC-D-01` |
| **`F8`** | Is "we can't yet prove we won't double-post" a blocker, or a build task? | 1 | No — sets Pre-Test **exit** |
| | **Total** | **24** | 3 of 8 carry an entry-gating member |

**Ruling `F2` and `F6` alone closes 7 of the 24** — `F2`'s three and `F6`'s four, enumerated.

> **`AR-C-01` — an identifier census of this pack returns 23, not 24.** The **over-receipt tolerance
> default** in `F2` is a named decision with **no identifier**; the other 23 all carry one. Any reader
> counting by identifier will get 23 and conclude something is missing. **Nothing is missing — the unit
> is the decision, and one decision has never been given an id.** Stated here because this is the same
> unit-versus-identifier confusion that produced `AR-F-01` one family away.

**`F5` = 6, not 8.** The parent pack's summary counted `F5` by identifier and its own card by decision.
`POH-D-06` is one governance act with two subjects, and "veto limb 2" is a design gap (`POH-G-03`), not
a Boss decision. Derivation at `SA_AR_01` §3.

---

## 2. DECISION CARDS

---

### `F1` — COGS RECOGNITION AND REVERSAL BASIS

**In business terms.** A customer buys something. Somewhere between the goods leaving the warehouse and
the invoice being issued, the cost of those goods must become an expense. Boss is choosing **which of
those two moments is the one**. Separately, when the customer returns the item, Boss is choosing whether
we put back **what it originally cost us** or **what it costs today**.

| Element | |
|---|---|
| **Family ID** | `F1` |
| **Atomic decisions** | `JT-04` recognition timing · `JT-05` return cost basis — **2** |
| **Business problem** | Under `BD-ACC-03A`'s `Perpetual`, which event recognises cost of sales — the physical movement or the customer invoice? And does a return reverse at original or current cost? |
| **Modules affected** | Inventory · Accounting · Sales |
| **Current evidence** | The reference estate implements **two mutually exclusive rules by generation** — delivery-triggered pre-19, invoice-triggered 19.0+ — corroborated across ≥7 research files; the current generation's own label reads *"Perpetual (at invoicing)"* (`C2-F-03`, `FACT VERIFIED`). `XMC-C-B2` publishes cost-of-sales recognition at invoice *posted*. **The corpus contains both readings and no SMEsPlus determination** |
| **Prior Boss rulings that constrain** | `BD-ACC-01` event identity, retry, reversal, Tenant+Company scope · `BD-ACC-03A` `Periodic\|Perpetual` at Product Category · `BD-ACC-03B` `Standard\|Average\|FIFO` at Product Category · `BD-ACC-02` company-scoped tax. **The values and their owner are ruled; the event and the reversal basis are not** |
| **Options** | `JT-04`: (a) movement-triggered · (b) invoice-triggered · (c) posting-event-triggered · (d) configuration-dependent hybrid · (e) cut-off/reconciliation-based. `JT-05`: original cost · current cost |
| **Consequence of each** | (a) cost and stock move together, invoice-period matching can break · (b) matches revenue exactly, leaves goods gone and cost unrecognised in between · (c) ties cost to the posting act, inheriting `C-02`'s identity gap · (d) two behaviours to test and explain · (e) defers to a reconciliation that must then always run. `JT-05` original: needs per-unit cost lineage retained; current: manufactures a margin no sale earned |
| **SMEs Core recommendation** | `JT-04` → **(a)**, under `ND-10`: *Perpetual* = recognition at the physical movement, *Periodic* = at period close, **with both definitions restated wherever the terms appear**, because the same two words denote two different points across two generations of one reference product. `JT-05` → **original cost**: `XMC-C-A8` binds the reversal to the original event's identity, so the original amount is always recoverable |
| **Dissent / adversarial view** | `ND-10` is a **SMEs Core position, not Boss-approved**. CORR5's first freeze adopted it *as if* `BD-ACC-03A` had ruled it (`C10-A1`); **two independent challengers falsified that** and the adjudication was withdrawn. **Boss should weigh that the executing party's instinct was to decide this one** |
| **Effect on Inventory** | When the valuation fact is emitted; whether per-unit original-cost lineage becomes a data-model requirement |
| **Effect on Accounting** | The recognition role inside the immutable event identity basis (`XMC-C-A3` part 5) and the posting trigger |
| **Effect on Manufacturing / Purchase / Sales** | **Sales**: the sale document's role changes from cost trigger to cost witness or back. Manufacturing and Purchase unaffected |
| **SaaS / Tenant / Company** | None — identity is Tenant+Company bounded under every option |
| **Audit / Control** | `RC-03` reconciliation posture follows: *at the closing boundary* under `Periodic`, *continuous* under `Perpetual`. The audit contract carries both dates regardless (`AUD-C-B4`) |
| **Pre-Test consequence** | Test cases writable now; **expected accounting values cannot be set** for 10 affected rows. Deferring past Functional Design forces costing rework, because the recognition role sits inside the immutable identity basis |
| **Prerequisite inputs, and who owns them** | `SME-Q-03` invoice/delivery sequencing — **Business SME** · `TH-NEW-01` does TAS 2 constrain the trigger — **Thai Accounting-Tax track** · `TH-NEW-02` costing consistency on returns — same · `CGS-U20`/`U31` bounded re-fetch — **Docs/Research**. **Boss may rule now or commission these four first; they are not Boss's to perform** |
| **Affected scenarios** | 22-scenario rows 1–6, 16, 17 (`JT-04`), 8, 9 (`JT-05`); `SA15` `E2E-01`, `-03`, `-11`, `-12`, `-13` |
| **Affected vetoes** | `AAS-V-03` COGS-gap condition · `MTI-46` value half |
| **Evidence pointers** | `08_JT04_TARGETED_RESOLUTION.md` §5 · `09_JT05_TARGETED_RESOLUTION.md` §5 · `11_COGS_RECOGNITION_OPTIONS_ANALYSIS` · `SA_CORR2_02` `C2-F-03` · `SA_CORR2_12` (`ND-10`) · `XMC-C-A3`, `-A8`, `-B2` |
| **Recommended Boss wording** | *"`F1` = `JT-04` movement-triggered under the `ND-10` definitions, both definitions to be restated wherever the terms appear; `JT-05` original cost."* — or *"`F1` = HOLD pending `SME-Q-03` and `TH-NEW-01`."* |

---

### `F2` — COMMERCIAL CONTROL-DEFAULT POLICY

**In business terms.** Three different controls can trip: cancelling a sale that is already invoiced,
confirming an order that pushes a customer past their credit limit, receiving more goods than were
ordered. In each case the tenant has configured nothing. Boss is choosing **what SMEsPlus does by
default** — stop the user, let them through with a permanent recorded exception, or let them through
silently. **This is one risk-appetite question, and answering it once answers all three.**

| Element | |
|---|---|
| **Family ID** | `F2` |
| **Atomic decisions** | `XD1-P1` sell-side cancellation gate · `TV6-BOSS-01` credit exposure at commitment confirmation · over-receipt tolerance default — **3** |
| **Business problem** | When a commercial control fires and no preference is configured, does SMEsPlus default to `block`, `warn-and-allow` into a recorded owed-condition, or `allow-silently`? |
| **Modules affected** | Sales · Purchase · Inventory · Accounting (cancellation reaches revenue) |
| **Current evidence** | `XD1-P1`: trigger, data contract, durability substrate, failure behaviour, audit requirements and Tenant/Company scoping **all determined** (`SA_CORR3_01` §§5–12); exactly two alternatives survive proof. `TV6-BOSS-01`: `APR-003`'s explicitly deferred item, **open since the Group A round and re-reported "undefined" three times**. Tolerance: **no source supplies a default** — `SA_CORR2_05` returns `0` for "tolerance" and "over-receipt" |
| **Prior Boss rulings that constrain** | **None rules a default.** `ND-03` (an automatic cross-module document may not enter a module beneath its control floor) and `XMC-C-D3` bind the *floor*, not the default |
| **Options** | `block` · `warn-and-allow` with a non-dismissible recorded condition · `allow-silently` |
| **Consequence of each** | **`block`**: friction lands on the user at the moment of the act; nothing corrupt enters the ledger. **`warn-and-allow`**: work continues, and every allowed breach must emit a recorded owed-condition or the control degrades to a silent no-op, which `EP-P` forbids. **`allow-silently`**: no control at all; an over-receipt corrupts stock truth before anything sees it |
| **SMEs Core recommendation** | **`block` on all three, ruled once as a principle.** Sell-side exposure is larger and carries a statutory element the buy-side gate never protected. **Where a tenant needs looser behaviour it configures it — the question is only the default** |
| **Dissent / adversarial view** | CORR3 recorded that Boss *"may wish to rule once on the principle"* and **deliberately kept the items separate** so as not to conflate separately-evidenced elections. **This pack combines them and says so, so Boss can still split the ruling** |
| **Effect on Inventory** | Over-receipt: refused, or recorded as an evented exception with a reason class |
| **Effect on Accounting** | Cancellation gate: which invoice state blocks a sell-side cancellation, hence when revenue and receivable may be undone |
| **Effect on Manufacturing / Purchase / Sales** | **Purchase**: the receiving clerk's experience at over-delivery. **Sales**: whether an invoiced order can still be cancelled, and whether an over-limit order can be confirmed |
| **SaaS / Tenant / Company** | The default is **platform-owned**; the override is **company-scoped** configuration (`CF-I-07`) |
| **Audit / Control** | Under `warn-and-allow`, the recorded owed-condition is the audit artefact and must be non-dismissible |
| **Pre-Test consequence** | **No entry gate** — both branches are testable; the suite writes the branch Boss rules. Deferred, Pre-Test cannot state an expected result for the unconfigured case, **which is the commonest case in a new tenant** |
| **Affected scenarios** | 22-scenario rows 5, 10; `SA15` `E2E-01` |
| **Affected vetoes** | None |
| **Evidence pointers** | `SA_CORR3_00_DECISION_RECLASSIFICATION.md` §5.1 · `SA_CORR3_01` §§5–12 · `APR-003` · `SA_CORR2_05` · `CF-I-07` · `ND-03`, `XMC-C-D3`, `EP-P` |
| **Recommended Boss wording** | *"`F2` = `block` as the platform default for all three controls; tenants may configure looser behaviour per company."* — or *"`F2` = `block` for `XD1-P1` and the over-receipt tolerance; `TV6-BOSS-01` = `warn-and-allow` with a recorded owed-condition."* |

---

### `F3` — DROPSHIP VALUATION AND COST LANDING

**In business terms.** A customer orders, and the supplier ships straight to them. The goods never
reach our warehouse. Boss is choosing whether SMEsPlus **pretends the goods arrived and left** so that
the sale carries a cost, or **records nothing in stock** and states explicitly that no stock cost
arises, binding the cost to the sale another way.

| Element | |
|---|---|
| **Family ID** | `F3` |
| **Atomic decisions** | `XMC-D-01` · `C2-D-02` — **2** |
| **Business problem** | When goods move supplier→customer with no internal end, does SMEsPlus emit two valuation facts or none — and where does the cost land, bound to the sale by what identity? |
| **Modules affected** | Inventory · Accounting · Purchase · Sales |
| **Current evidence** | The reference records a dropship movement then **excludes it from valuation on three independent paths**; revenue, receivable and tax are recognised with **no cost**, and the cost lands on the vendor bill at the bill's date, **unlinked to the sale** (`C2-F-02`). `H-02` grades movement→valuation `SEMANTICALLY INCOMPATIBLE — MEASURED`; `H-03` grades cost→revenue `NO IDENTITY`. **The routing itself is determined** — `XMC-F-03` names *"direct shipment from supplier to customer"* as a template |
| **Prior Boss rulings that constrain** | `XMC-C-C6` — *every revenue recognition produces either a cost recognition bound to the same identity or an explicit recorded determination that none arises; **silence is not a permitted answer***. **It forces the question to be answered; it does not answer it** |
| **Options** | (a) **two valuation facts** — a notional receipt and issue, giving a bound cost · (b) **none**, with an explicit recorded determination under `XMC-C-C6`, cost bound by the accounting event identity instead |
| **Consequence of each** | (a) stock records movements for goods never held; inventory quantity truth is unaffected but movement history gains synthetic entries. (b) stock stays literal; the recorded determination becomes an audit artefact that must be evented, and the cost-to-revenue link depends entirely on the accounting event identity — **which is `F8`'s subject** |
| **SMEs Core recommendation** | **None offered, deliberately.** CORR3 carried this **with a standing dissent**: *"a second executor's buy-side evidence suggests the answer may be available without a decision."* **This round did not resolve the dissent** — doing so needs the buy-side package re-read, outside a delta-first round's scope — and presents it unresolved, as CORR3 required |
| **Dissent / adversarial view** | **Live and unresolved. Boss should see it before deciding: if the dissent is right, this is a determination and leaves the Boss list entirely** |
| **Effect on Inventory** | Whether a dropship line creates movement facts at all |
| **Effect on Accounting** | Whether `XMC-C-C6`'s symmetry is met by a bound cost or by a recorded determination |
| **Effect on Manufacturing / Purchase / Sales** | **Purchase**: whether the vendor bill is the cost's only anchor. **Sales**: whether a dropship line's margin is computable at the line. Manufacturing unaffected |
| **SaaS / Tenant / Company** | None |
| **Audit / Control** | Under (b) the recorded determination is the audit artefact and must be evented |
| **Pre-Test consequence** | No entry gate. Deferred, `E2E-05` keeps two named breaks and the dropship cost-to-revenue link stays untestable |
| **Affected scenarios** | `SA15` `E2E-05`; 22-scenario row 18 via `XMC-C-D6`'s carve-out |
| **Affected vetoes** | None |
| **Evidence pointers** | `SA_CORR3_12` `B-4` · `SA_CORR2_02` §6 · `C2-F-02` · `H-02`, `H-03` · `XMC-F-03` · `XMC-C-C6`, `XMC-C-D6` |
| **Recommended Boss wording** | *"`F3` = resolve the standing dissent first: commission the buy-side re-read, then return `F3` if a decision is still required."* — or *"`F3` = (b) no valuation facts; record an explicit determination under `XMC-C-C6` and bind cost by the accounting event identity."* |

---

### `F4` — CROSS-MODULE CONTRACT SCOPE AND SUPPLY BINDING

**In business terms.** Two things. First: SMEsPlus has one Boss-approved list of sixteen data elements
that must travel between modules, and it currently applies to **one** boundary out of twelve. Boss is
choosing whether it applies to all of them. Second: when manufacturing runs short of a raw material and
a purchase is raised, Boss is choosing whether that purchase can ever **clear** the shortage — today
the shortage only clears when stock is reserved, so **a shortage can be entered and never left by
buying**.

| Element | |
|---|---|
| **Family ID** | `F4` |
| **Atomic decisions** | `XMC-D-02` contract scope · `C2-D-01` supply binding — **2** |
| **Business problem** | Does the 16-element handoff contract govern every cross-module boundary or only Inventory → Accounting — and when a manufacturing shortage raises supply, is the fulfiller hard-bound or soft-bound? |
| **Modules affected** | **All** — that is what `XMC-D-02` is about. Directly: Inventory, Accounting, Manufacturing, Purchase |
| **Current evidence** | `XMC-D-02`: the contract's scope is *"unambiguous at primary text — one boundary, one direction"*, so widening it **amends a Boss-approved control** — *"Nothing to research; something to decide"*. **Eleven of twelve mandated handoffs have no element contract.** `C2-D-01`: **narrowed but not resolved** — `BN-04` re-graded `PARTIAL`, ownership `FACT VERIFIED`, the *"make-or-buy on demand"* template exists, and the fact-ownership matrix already binds the fulfiller **softly**. **The same sentence continues:** *"the target manufacturing state machine's shortage state exits **only on reservation completing, never on procurement being raised.** A shortage can therefore be entered and never left by supply"* |
| **Prior Boss rulings that constrain** | `03_BOSS_APPROVAL_…MINIMUM_HANDOFF_DATA_CONTRACT` §3 (the 16 elements) and §4 (the `PASS / VERIFIED` gate) |
| **Options** | `XMC-D-02`: extend to all boundaries · give each boundary its own contract · leave it at one and accept eleven uncontracted handoffs. `C2-D-01`: confirm **soft binding and add an explicit procurement exit** to the shortage state · require **hard binding** to a named fulfiller · confirm soft binding **and accept** that a shortage exits only on reservation |
| **Consequence of each** | Extending multiplies element carriage and attestation obligations across eleven boundaries and **re-scopes the Pre-Test Matrix before it is written**. Leaving it at one boundary means `XMC-C-D2` applies — *a rule addressed to a receiver with no element capable of satisfying it is not a rule* — to eleven handoffs. On `C2-D-01`, accepting the current exit rule **leaves `E2E-04` permanently untraversable**; adding a procurement exit closes it |
| **SMEs Core recommendation** | `XMC-D-02` → **extend**. `C2-D-01` → **confirm soft binding *and* add the procurement exit**, because confirming the stated position alone does not close the flow |
| **Dissent / adversarial view** | None outstanding. **A caution instead:** a first draft of the parent round re-graded `E2E-04` traversable by quoting the first half of the sentence above and suppressing the second. **The re-grade was withdrawn. `E2E-04` is untraversable until `C2-D-01` is ruled** |
| **Effect on Inventory** | `C2-D-01` sets whether a shortage creates an obligation on a named party |
| **Effect on Accounting** | `XMC-D-02` sets how many boundaries must carry elements 1–16 |
| **Effect on Manufacturing / Purchase / Sales** | **Manufacturing**: whether a shortage state has a supply-side exit at all. **Purchase**: whether a raised order is bound to the shortage that caused it. **Sales**: the downstream promise date depends on both |
| **SaaS / Tenant / Company** | Extending extends `HF-CTX-01`/`-02` mandatory carriage to eleven more boundaries |
| **Audit / Control** | Extending multiplies attestation obligations (`HF-CTX-06`, `-11`) accordingly |
| **Pre-Test consequence** | **`XMC-D-02` gates Pre-Test entry** — it determines the Matrix's own scope. Deferred, Pre-Test builds over one boundary and discovers eleven later, which is a re-scope, not an increment |
| **Affected scenarios** | 22-scenario row 18; `SA15` **`E2E-04` — the one scenario that remains `NOT TRAVERSABLE`** — and `E2E-06` |
| **Affected vetoes** | None directly |
| **Evidence pointers** | `SA_CORR3_08_CROSS_MODULE_CONTRACT_PROOF.md` · `SA_CORR2_02` §3.1 and §6 · `03_BOSS_APPROVAL_…HANDOFF_DATA_CONTRACT` §3, §4 · `XMC-C-D2` · `HF-CTX-01`, `-02`, `-06`, `-11` |
| **Recommended Boss wording** | *"`F4` = extend the 16-element contract to all twelve boundaries; confirm soft binding and direct that the manufacturing shortage state gain an explicit procurement exit."* |

---

### `F5` — MANUFACTURING OVERHEAD GOVERNANCE

**In business terms.** Two old blockers about factory overhead **cannot be answered as they are
written** — one of them offers a choice between two options, and its own register already rejected one
of them. Boss is being asked to **restate them into the question that is actually live**, and then to
settle **five** policy points underneath: whether machine depreciation follows time or output, whether the
departure from a standing ruling is confirmed, whether setup time counts as productive, whether idle
and no-demand are one cause or two, and who owns the capacity figure.

| Element | |
|---|---|
| **Family ID** | `F5` |
| **Atomic decisions** | `POH-D-06` **restate `BLK-07` and `BLK-08`** (one governance act, two subjects) · `POH-D-01` · `POH-D-02` · `POH-D-03` · `POH-D-04` · `POH-D-05` — **6** |
| **Business problem** | Restate or confirm `BLK-07` and `BLK-08` in the form the evidence supports, and rule the five policy elections underneath them |
| **Modules affected** | Manufacturing · Inventory (WIP value) · Accounting (variance posting) |
| **Current evidence** | **`BLK-07` as worded is unanswerable**: its §3 states a binary — *normal capacity or actual hours* — and **its own §6 already rejected the second branch by name** (*"`REJECTED — INVALID ASSUMPTION`… breaches TAS 2 ¶13, undefined at zero output, capitalises idleness into inventory"*). *"A Boss asked to decide 'normal capacity or actual hours' is being asked to choose between an option and an option his own registers rejected, while the choice that is actually live is not on the paper"* (`POH-F-12`). **The live choice is `POH-D-02`, a depreciation-method election.** The three design gaps beneath the blocker (`POH-G-01` pool/denominator/capture, `POH-G-02` receiver, `POH-G-04` variance) were **closed at specification by CORR5** (`SA_CORR5_10A`) |
| **Prior Boss rulings that constrain** | **`BD-02`** — the destination of unabsorbed overhead is **already closed by Boss**. **`BD-04`** — one allocation driver per configuration context, which `POH-D-01` proposes to depart from per cost class |
| **Options** | `POH-D-06`: **restate** `BLK-07` as the `POH-D-02` election and confirm normal capacity as the denominator · re-affirm the original binary · retire `BLK-07` and carry only `POH-D-02`. `POH-D-01`: confirm the `BD-04` departure per cost class, or refuse it. `POH-D-02`: straight-line, or units-of-production, both absorbed at normal capacity. `POH-D-03`: setup productive, or not. `POH-D-04`: `IDLE` and `NO_DEMAND` one cause, or two. `POH-D-05`: who owns the normal-capacity figure and the review cadence |
| **Consequence of each** | Re-affirming the original binary asks Boss to pick an option his own register rejected on statutory grounds. Restating puts the live depreciation-method election in front of Boss **with its tax consequences unresearched and stated as unresearched**. `POH-D-04` is **pure management reporting — the two causes are accounted identically**, so the cost is only in reporting granularity |
| **SMEs Core recommendation** | **Restate.** Confirm **normal capacity** as the absorption denominator (it *"comes from statute, not from analysis preference"*), confirm the `BD-04` departure per cost class, and put straight-line vs units-of-production before Boss as `POH-D-02`. Candidates on the rest: setup **productive**; keep `IDLE` and `NO_DEMAND` **both**; a **dated, attributed** capacity record reviewed annually alongside useful life |
| **Dissent / adversarial view** | `SA_CORR3_03` §13.3 **names its own headline as the first thing a challenger should attack**; the challenge ran and the headline held. **The over-absorption cap's *strength* remains a declared statutory dependency (`HOLD`)** — the recommendation does not close it |
| **Effect on Inventory** | WIP value composition gains the absorbed-overhead component (`SA_CORR5_10A` §3) |
| **Effect on Accounting** | The variance event's owner, mechanism and destination (`BD-02` for under-absorption); `POH-D-02` has **unresearched tax consequences** |
| **Effect on Manufacturing / Purchase / Sales** | **Manufacturing** is the whole subject: which machine hours absorb cost, and whether setup and idle time are charged to jobs |
| **SaaS / Tenant / Company** | The capacity register is **company-scoped**; the operation classes are **platform-owned** |
| **Audit / Control** | The per-pool closure identity is the publication gate; a non-zero residual raises and never re-absorbs |
| **Pre-Test consequence** | No entry gate. Deferred, two scenarios keep an expected-value gap and the absorption suite cannot state a numeric expectation |
| **Affected scenarios** | 22-scenario rows 16, 17; `SA15` `E2E-03`, `E2E-13`, `E2E-17` |
| **Affected vetoes** | **Veto limb 2** — undischarged and, as written, undischargeable. **It is `POH-G-03`, a design gap, not a decision**; the mutual-exclusion mechanism it would test is specified at `SA_CORR5_10A` §4 |
| **Evidence pointers** | `SA_CORR3_03_PRODUCTION_OVERHEAD_PROOF.md` §7.2, §13.3, `POH-F-12`, `POH-G-01`…`-04`, `POH-D-01`…`-06` · `SA_CORR5_10A` §3, §4 · `BD-02`, `BD-04` · TAS 2 ¶13 |
| **Recommended Boss wording** | *"`F5` = restate `BLK-07` as the `POH-D-02` depreciation-method election with normal capacity confirmed as the denominator; `BLK-08` confirmed; `POH-D-01` departure approved per cost class; `POH-D-02` = straight-line; `POH-D-03` = setup productive; `POH-D-04` = keep both causes; `POH-D-05` = Finance owns the figure, reviewed annually. Tax consequences of `POH-D-02` to be researched before build."* |

---

### `F6` — CROSS-COMPANY VISIBILITY AND COMMERCIAL SCOPE

**In business terms.** A Thai SME group runs several companies inside one tenant and wants to see them
together. The isolation boundary says they cannot. Boss is choosing whether **a sanctioned door exists
at all** — and if it does, who owns the mapping, what escalates a tenant to the Private Company model,
and whether a product's base sell price is one number for the group or one per company.

| Element | |
|---|---|
| **Family ID** | `F6` |
| **Atomic decisions** | `MTI-D-04` cross-company grant · `RC-D-03` escalation to Private Company · `RC-D-04` mapping-layer ownership · `TV6-BOSS-02` price scope — **4** |
| **Business problem** | Does a sanctioned cross-company read exist inside a tenant at all — and if so, who owns the mapping layer, what escalates a tenant to Private Company, and is base sell price a tenant fact or a company fact? |
| **Modules affected** | **Platform / SaaS Foundation** primarily · Inventory · Accounting · Sales (price) |
| **Current evidence** | `XCR-02` (the cross-context report grant) is `SPECIFIED — CONDITIONAL (MTI-D-04)`; **`CF-XCR-GAP-01` is deliberately un-numbered** because giving it an entry would place an unspecified object in a register **whose completeness is the isolation claim**. `AAS-V-03` forbids any such grant carrying valuation content while the COGS gap stands. **CORR5 traced the one cross-company path that exists at data level**: 1,201 completed legs into a company-less transit place paired with 1,201 out — the `XCR-01` shape, **never one movement spanning two companies** |
| **Prior Boss rulings that constrain** | **`BD-ACC-02`** — no cross-company statutory posting, offsetting, settlement or filing; **management views permitted**. `MTI-D-01`/`-02`/`-03` ruled. `MTI-22` is the only permitted cross-company means, register complete with three entries |
| **Options** | `MTI-D-04`: **no grant in v1** · a read-only enumerated grant · a broader grant. `TV6-BOSS-02`: tenant-scoped price · company-scoped price. `RC-D-03`, `RC-D-04`: as their registers state |
| **Consequence of each** | **No grant**: the group need is met by per-company export, which becomes the designed answer rather than the informal one; `XCR-02`, `CF-XCR-GAP-01`, `AAS-V-03`'s subject and `CF-I-03`'s exception test data all settle in one ruling; widening later unbuilds nothing. **A grant**: requires grant identity, granting authority, scope, expiry and a per-use log, and `MTA-11` records that **every grant mechanism degrades toward permanence** with no review cadence designed anywhere |
| **SMEs Core recommendation** | `MTI-D-04` → **no cross-company grant in v1**. `TV6-BOSS-02` → **company-scoped**, because a price that cannot differ by company while everything consuming it can will produce cross-company margin figures no one can defend |
| **Dissent / adversarial view** | Recorded counter-argument: *"**Not deciding is not neutral** — the need gets met by export, which is the worst outcome"* (R1 `11`). Under the recommendation, export becomes the designed route rather than the informal one — **but Boss should note the counter-argument is about the cost of a `HOLD`, not about the merits of the grant** |
| **Effect on Inventory** | Whether the mapping/provenance object is commissioned at all (`RC-D-04`) |
| **Effect on Accounting** | Cross-company management views; `BD-ACC-02`'s statutory boundary is unaffected either way |
| **Effect on Manufacturing / Purchase / Sales** | **Sales**: `TV6-BOSS-02` decides whether one company can price differently from another |
| **SaaS / Tenant / Company** | **This family *is* the company boundary.** A grant is the only sanctioned crossing |
| **Audit / Control** | `XCR-02` needs grant identity, authority, scope, expiry and a log entry per use |
| **Pre-Test consequence** | **`MTI-D-04` gates Pre-Test entry**: `CF3-P-04`, the cross-company exception path, either has test data or is struck, and the isolation suite cannot be scoped without knowing which |
| **Affected scenarios** | 22-scenario row 15; `MTI-22`, `MTI-44`, `CF-I-03` `P5` |
| **Affected vetoes** | **`AAS-V-03` and `CF-V-02` — both held open by this family** |
| **Evidence pointers** | `11_OPEN_ITEMS_AND_DEPENDENCY_REGISTER.md` · `XCR-01`, `XCR-02`, `CF-XCR-GAP-01` · `MTA-11` · `MTI-22`, `MTI-44` · `CF-I-03` `P5` · `BD-ACC-02` · `SA_CORR5_09` |
| **Recommended Boss wording** | *"`F6` = no cross-company grant in v1; the group-view need is met by per-company export as the designed route. `TV6-BOSS-02` = company-scoped price. `RC-D-03`/`RC-D-04` as recommended in their registers."* |

---

### `F7` — AUTHORIZATION AXIS AND CONFIGURABLE-RECORD SCOPE

**In business terms.** Boss already ruled that permissions are granted on Company, Warehouse and
Operation Type. **Storage location was not in that list**, and five design rows are stuck because it is
unclear whether it should have been. Two other open lists — which record types a tenant may configure,
and which operation classes the platform owns — cannot be closed by evidence, only by declaration. And
one row needs Boss to say whether two differently-named objects in two rulings are the same thing.

| Element | |
|---|---|
| **Family ID** | `F7` |
| **Atomic decisions** | `RC-D-01` location as an authorization axis · `RC-D-02` configurable-record enumeration · `CF-D-01` `MTI-D-03` scope · `CF-D-02` operation-class enumeration — **4** |
| **Business problem** | Is `location` an authorization axis; what closes the configurable-record enumeration; is `MTI-D-03`'s *"Unit of Measure Category"* the same object as the context matrix's *"Unit group and unit"*; and what closes the platform-owned operation-class enumeration? |
| **Modules affected** | Platform / SaaS Foundation · Inventory · indirectly Accounting through control binding |
| **Current evidence** | `CF-I-01` fixes the four-axis tuple; **`location` anchors records (`CTX`) and is not ruled an authorization axis** — five matrix rows are unsettled on it. `CF-I-05` is `SPECIFIED — CONDITIONAL (CF-D-02)` and **`CF-D-02` option (c) would withdraw it entirely**. `CF-I-07` is `SPECIFIED — CONDITIONAL (RC-D-02)` because the class list is open-ended. **`CF-D-01` leaves anchor row 17 with two possible answers** — the single residual on `MTI-05` after CORR5's adjudication |
| **Prior Boss rulings that constrain** | **`MTI-D-02`** ruled `AUTH` = Company + Warehouse + Operation-Type, and **location is not among them**. **`MTI-D-03`** names the tenant-changeable boundary |
| **Options** | As each register states. `CF-D-02` in particular: close at the eight illustrated classes with an addition process · derive from the `INV-F-*` function set · rule that no platform class exists and **withdraw `CF-I-05`** |
| **Consequence of each** | Adding `location` to `AUTH` widens the negative-access suite's denominator and narrows `CF-I-03` `D5`'s domain; refusing it settles five matrix rows the other way. Withdrawing `CF-I-05` removes a specified invariant rather than completing it |
| **SMEs Core recommendation** | **As the registers state; no new position is originated here.** `CF-D-01`'s ground is decisive and general: ***"only Boss may state what a Boss ruling covers"*** |
| **Dissent / adversarial view** | None outstanding |
| **Effect on Inventory** | `RC-D-02` and `CF-D-01` fix the anchor of two configurable record classes |
| **Effect on Accounting** | Indirect, through the operation-class binding of controls |
| **Effect on Manufacturing / Purchase / Sales** | Operation-type authorization reaches receiving, issuing and production operations alike |
| **SaaS / Tenant / Company** | `RC-D-01` decides whether a warehouse-scoped actor can be further confined by location |
| **Audit / Control** | **`AUD-C-A5`** (the situational location axis) and the negative-access substitution tests `S-01`…`S-08` enumerate exactly the ruled axes |
| **Pre-Test consequence** | **`RC-D-01` gates Pre-Test entry**, because the axis set is the negative-access suite's own denominator. Deferred, the suite is written over an axis set that may change — **the wrong-denominator class this programme has recorded repeatedly** |
| **Affected scenarios** | Row 15 and every row's authorization dimension; `MTI-05` row 17 |
| **Affected vetoes** | `RC-V-01`'s under-inclusive condition touches the same rows |
| **Evidence pointers** | `02_RULING_CONFORMANCE_DELTA_REGISTER.md` · `CF-I-01`, `-03`, `-05`, `-07` · `MTI-D-02`, `MTI-D-03` · `AUD-C-A5` · `S-01`…`S-08` · `MTI-05` row 17 |
| **Recommended Boss wording** | *"`F7` = `RC-D-01` location is **not** an authorization axis; `CF-D-01` `MTI-D-03`'s Unit of Measure Category **is** the same object as the matrix's Unit group and unit; `RC-D-02` and `CF-D-02` close at the enumerated classes with a named addition process."* |

---

### `F8` — IDEMPOTENCY SEVERITY

**In business terms.** If the same event is processed twice, SMEsPlus has no deterministic way to
recognise it as the same event and refuse the duplicate. The **design** for that identity now exists;
the **build and proof** do not. Boss is choosing whether that gap **stops Phase SA from closing**, or
whether it is a build task Phase SA may pass with.

| Element | |
|---|---|
| **Family ID** | `F8` |
| **Atomic decision** | `C-02` — **1** |
| **Business problem** | Is the absence of a deterministic idempotency identity gate-blocking, or a design input a phase may pass with? |
| **Modules affected** | Accounting (owner of the identity) · Inventory · **every module that emits an event** |
| **Current evidence** | Element 15 is **specified** by CORR5 (`E15-A1`, `XMC-C-A14`) and **not built**. The estate's only carrier is table-global and **populated on 0 of 13,814 rows**, so a uniqueness test over it **passes on every row** — a control that cannot detect its own failure. The Boss-approved handoff contract §4 already forbids `PASS / VERIFIED` where duplicate effects cannot be prevented *"when idempotency is required"* |
| **Prior Boss rulings that constrain** | **`BD-ACC-01` ruled the *object***: same-event retry must not create duplicate accounting events, and the Accounting Core owns the identity. **`UAE-29`, the Account programme's root blocker, is thereby ruled. `C-02` asks only about *severity*** |
| **Options** | (a) **gate-blocking** — no phase may close while element 15 is unproven · (b) **design input** — the specification suffices for Phase SA; the proof is a Pre-Test/build obligation |
| **Consequence of each** | (a) holds Phase SA and every later phase until `RT-E15-01`…`-09` execute, which requires a build that does not exist. (b) lets Phase SA close on specification, **relying on contract §4 to stop a `PASS` one level down** — the protection Boss would buy with (a) already exists there |
| **SMEs Core recommendation** | **(b) design input, not phase-holding** |
| **Dissent / adversarial view** | **CORR5's first freeze declared this "dissolved by standing rulings" and two challengers independently reversed it** — a commissioning prompt is not a ruling, and four registers name Boss as owner. **It is presented as open precisely because the executing party twice tried to close it** |
| **Effect on Inventory** | None to the specification; `MTI-31` and `XMC-C-A14` stand either way |
| **Effect on Accounting** | None to the specification; everything to when the proof is owed |
| **Effect on Manufacturing / Purchase / Sales** | None to the specification |
| **SaaS / Tenant / Company** | None |
| **Audit / Control** | Under (a), no gate may close until `RT-E15-01`…`-09` execute |
| **Pre-Test consequence** | **No entry gate — but it sets Pre-Test *exit* criteria**, and should be ruled before exit criteria are agreed. Deferred, Pre-Test may reach the end of its matrix without an agreed rule on whether an unproven element 15 blocks closure — **the argument arriving at the worst moment** |
| **Affected scenarios** | Row 22 — and, under (a), **every** row, since element 15 is the join key |
| **Affected vetoes** | None directly; interacts with `AAS-V-01`/`CF-V-01`'s runtime scope |
| **Evidence pointers** | `03_INVENTORY_FUNCTIONAL_DESIGN_V1.md` (*"whether this is gate-blocking is Boss's decision"*) · `SA_CORR5_01_ELEMENT15_IDEMPOTENCY_ADJUDICATION.md` · `E15-A1`, `XMC-C-A14` · `BD-ACC-01` · handoff contract §4 · `GAP-FS-06` |
| **Recommended Boss wording** | *"`F8` = design input, not gate-blocking; element 15 proof is a Pre-Test exit criterion, not a Phase SA entry condition."* |

---

## 3. THE FIVE BOSS ACTS — NOT DECISIONS

These have **one correct form and no alternatives**, so Boss is not asked to *decide* what he is being
asked to *do*. **Sequenced**, because one of them unblocks the others.

| # | Act | What is being asked | Why an act, not a decision |
|---:|---|---|---|
| **1** | **`B-7`** | Appoint a `Q-BOSS-02`-eligible structurally independent challenger for the Phase SA package | `Q-BOSS-02` control 2 **forbids a session selecting its own challenger**. **Do this first** — under `FG-F-06` Reading A it is gate-blocking, and the handoff package at `SA_AR_06` is ready |
| **2** | **`C4-D-01`** | Commission the Boss-mandated `ACCOUNTING_INVENTORY_INTERFACE_CONTRACT_AND_CROSS_PROOF`, and direct the merge-or-archive disposition of the 20 stranded architecture deliverables | The artefact is **mandated by a standing Boss approval** and exists in `0` of the corpus's paths |
| **3** | **`C4-D-02`** | Appoint the independent review that decides the platform-actor model (**R1** separate identity domain vs **R2** scoped role) | CORR4 re-scoped it from a design act to *"a governance act plus an independent review"* |
| **4** | **`AAS-V-02` discharge** | Ratify AAS+'s discharge of a veto whose stated condition — `MTI-D-01`, `-D-02`, `-D-03` ruled — **is satisfied** | R2: *"CONDITION SATISFIED — NOT DISCHARGED … never reported as lifted."* Discharge is the issuer's act, ratified by Boss |
| **5** | **Thai user panel** | Commission the Thai user validation panel | `18_THAI_USER_VALIDATION_CHECKLIST` line 11: **"Boss to commission."** Unblocks `R4-Q-01`, `GAP-FS-11` and every Thai label, all `candidate / UNVALIDATED` |

---

## 4. WHAT BOSS CAN CLOSE WITH THE FEWEST RULINGS

| Ruling | Closes |
|---|---|
| `F2` | 3 decisions |
| `F6` | 4 decisions, **and renders `AAS-V-03` vacuous and `CF-V-02` limb 1 closed** on the recommended branch |
| `F4` | 2 decisions **and unblocks Pre-Test scope**, and closes the one untraversable scenario |
| `F7` `RC-D-01` alone | unblocks the negative-access suite's denominator |
| **Act 1 (`B-7`)** | the only path to `EC-07`, if `FG-F-06` is Reading A |

## 5. Checkpoint

> ## `CP-SA-AR-40 — BOSS DECISION FAMILIES READY`
> **8 families · 24 decisions · 18 required elements on every card · plain-business framing on every
> card · recommended Boss wording on every card · 5 acts sequenced · 1 family (`F3`) carries an
> unresolved dissent and deliberately offers no recommendation.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
