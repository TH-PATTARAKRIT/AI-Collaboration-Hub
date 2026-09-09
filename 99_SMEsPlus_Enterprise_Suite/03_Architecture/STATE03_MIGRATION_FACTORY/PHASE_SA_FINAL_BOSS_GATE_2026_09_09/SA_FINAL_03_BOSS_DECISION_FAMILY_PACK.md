# SA_FINAL_03 — BOSS DECISION FAMILY PACK

## CP-SA-FG-30 — DECISION FAMILIES CONSOLIDATED

Session: `[SMEPLUS-26-09-09-PHASE-SA-FINAL-BOSS-GATE-001]`
Branch: `architecture/phase-sa-final-boss-gate-readiness-2026-09-09-001`
Boss: **SOLE FINAL APPROVER**

---

## 1. Consolidation rule and result

**Combine** where **one Boss ruling on a principle settles every affected scenario**. **Do not combine**
issues that merely share a domain. Each family below states the single question Boss is answering; the
member decisions are the places that answer lands.

| Family | Members | Gates Pre-Test **entry**? |
|---|---:|---|
| **`F1` COGS recognition and reversal basis** | 2 | No — blocks expected *values* on 8 scenarios |
| **`F2` Commercial control-default policy** | 3 | No — both branches are testable |
| **`F3` Dropship valuation and cost landing** | 2 | No |
| **`F4` Cross-module contract scope and supply binding** | 2 | **`XMC-D-02` yes** — it sets how many boundaries Pre-Test must cover |
| **`F5` Manufacturing overhead governance** | 9 | No |
| **`F6` Cross-company visibility and commercial scope** | 4 | **`MTI-D-04` yes** — it supplies or withdraws the isolation suite's exception test data |
| **`F7` Authorization axis and configurable-record scope** | 4 | **`RC-D-01` yes** — it fixes the axis set the negative-access suite enumerates |
| **`F8` Idempotency severity** | 1 | No — but it sets Pre-Test **exit** criteria |
| **Total** | **27** | 3 of 8 families carry an entry-gating member |

**27 decisions from 33 candidates, presented as 8 questions.** CORR5 presented 15 rows; a reader had to
reconstruct that `XD1-P1`, `TV6-BOSS-01` and the tolerance default are **one principle asked three
times**, which is `F2`.

---

## 2. Decision cards

Each card carries the sixteen elements master prompt §4 requires.

---

### `F1` — COGS RECOGNITION AND REVERSAL BASIS

| | |
|---|---|
| **Decision IDs** | `JT-04` (recognition timing) · `JT-05` (return cost basis) |
| **The question, one sentence** | **Under `BD-ACC-03A`'s `Perpetual`, which event recognises cost of sales — the physical movement or the customer invoice — and under `JT-05`, does a return reverse at the original cost or the current cost?** |
| **Why Boss authority** | `08_JT04` §5: *"Final event selection → **Boss**, informed by the above but not derivable from them alone."* `11_COGS_RECOGNITION_OPTIONS_ANALYSIS`: all five candidate models require a Business/Boss decision. `09_JT05` §5: *"Final return-cost-basis rule → **Boss**"* |
| **Existing ruling context** | `BD-ACC-01` (event identity ownership, retry, reversal, Tenant+Company scope) · `BD-ACC-03A` `Periodic \| Perpetual` at Product Category · `BD-ACC-03B` `Standard \| Average \| FIFO` at Product Category · `BD-ACC-02` company-scoped tax. **The values and their owner are ruled; the event and the reversal basis are not** |
| **Evidence** | The reference estate implements **two mutually exclusive rules by generation** — delivery-triggered pre-19, invoice-triggered 19.0+ — corroborated across ≥7 research files; the current generation's own label reads *"Perpetual (at invoicing)"* (`C2-F-03`, `FACT VERIFIED`). `XMC-C-B2` publishes cost-of-sales recognition at invoice *posted*. **The corpus therefore contains both readings and no SMEsPlus determination** |
| **Alternatives** | `JT-04`: (a) delivery/movement-triggered · (b) invoice-triggered · (c) posting-event-triggered · (d) configuration-dependent hybrid · (e) cut-off/reconciliation-based. `JT-05`: original cost · current cost |
| **SMEs Core recommendation** | `JT-04` → **(a) `ND-10`**: *Perpetual* = recognition at the physical movement, *Periodic* = at period close, **with both definitions stated wherever the terms appear** — because the same two words denote two different points across two generations of one reference product, and a term whose meaning moved once will move again. `JT-05` → **original cost**: `XMC-C-A8` binds the reversal's basis to the original event's identity, so the original amount is always recoverable; current-cost reversal manufactures a margin no sale earned |
| **Dissent / challenge result** | `ND-10` is a **SMEs Core position, not Boss-approved** (`SA_CORR2_12`). CORR5's first freeze adopted it *as if* `BD-ACC-03A` had ruled it (`C10-A1`) and **two independent challengers falsified that**; the adjudication was withdrawn and the item returned here. **That reversal is the single most consequential correction in the CORR5 chain and Boss should weigh it: the executing party's instinct was to decide this** |
| **Effect on Inventory** | Determines when the valuation fact is emitted and, for `JT-05`, whether per-unit original-cost lineage is a data-model requirement |
| **Effect on Accounting** | Determines the recognition role in the event identity basis (`XMC-C-A3` part 5) and the posting trigger |
| **Effect on Tenant/Company** | None — identity is Tenant+Company bounded under either answer |
| **Effect on Audit/Control** | `RC-03` reconciliation posture follows: *at the closing boundary* under `Periodic`, *continuous* under `Perpetual`. The audit contract carries both dates regardless (`AUD-C-B4`) |
| **Affected E2E / cross-proof scenarios** | 22-scenario rows **1, 2, 3, 4, 5, 6, 16, 17** (`JT-04`) and **8, 9** (`JT-05`); `SA15` `E2E-01`, `-03`, `-11`, `-12` |
| **Affected vetoes** | `AAS-V-03` (its COGS-gap condition), `MTI-46` value half |
| **Required before Pre-Test starts?** | **No.** Test cases are writable now; **expected accounting values cannot be set** for the ten affected rows until ruled |
| **Consequence of deferment** | Pre-Test proceeds on structure and context for all 22; ten rows carry `expected value pending`. **Deferring past Functional Design would force a costing rework, because the recognition role sits inside the immutable identity basis** |
| **Prerequisite inputs, and who owns them** | `SME-Q-03` SMEsPlus's actual invoice/delivery sequencing — **Business SME** · `TH-NEW-01` does TAS 2 constrain the trigger — **Thai Accounting-Tax track** · `TH-NEW-02` costing consistency on returns — same · `CGS-U20`/`U31` bounded re-fetch — **Docs/Research**. **Boss may rule on the recommendation now, or commission these four first; they are not Boss's to perform** |

---

### `F2` — COMMERCIAL CONTROL-DEFAULT POLICY

| | |
|---|---|
| **Decision IDs** | `XD1-P1` (sell-side cancellation gate) · `TV6-BOSS-01` (credit exposure at commitment confirmation) · over-receipt tolerance default |
| **The question, one sentence** | **When a commercial control fires and the business has not configured a preference, does SMEsPlus default to `block`, to `warn-and-allow` into a recorded owed-condition, or to `allow-silently`?** |
| **Why Boss authority** | A **risk-appetite election**. `SA_CORR3_00` §5.1: *"both surviving options are architecturally sound and equally auditable"* — they differ only in whose work the friction lands on. For `XD1-P1`, Group A's owning session **reserved the election to Boss in writing** and the reservation is undischarged; SMEs Core may not discharge a reservation it does not hold |
| **Existing ruling context** | None rules a default. `ND-03` (an automatic cross-module document may not enter a module beneath its control floor) and `XMC-C-D3` bind the *floor*, not the default |
| **Evidence** | `XD1-P1`: trigger, data contract, durability substrate, failure behaviour, audit requirements and Tenant/Company scoping **all determined** (`SA_CORR3_01` §§5–12); exactly two alternatives survive proof. `TV6-BOSS-01`: `APR-003`'s explicitly deferred item, **open since the Group A round and re-reported "undefined" three times**. Tolerance: no source in the corpus supplies a default (`SA_CORR2_05` returns **0** for "tolerance"/"over-receipt") |
| **Alternatives** | `block` · `warn-and-allow` with a non-dismissible recorded condition · `allow-silently` |
| **SMEs Core recommendation** | **`block` on all three, ruled once as a principle.** Sell-side exposure is the larger and carries a statutory element the buy-side gate never protected; an over-receipt accepted silently corrupts stock truth before any control sees it. **Where a tenant needs looser behaviour it configures it — the question is only the default** |
| **Dissent / challenge result** | CORR3 recorded that Boss *"may wish to rule once on the principle"* and deliberately kept the two items separate so as not to conflate separately-evidenced elections. **This pack combines them because a single principle answers all three, and states the separation so Boss can still split the ruling** |
| **Effect on Inventory** | Over-receipt: whether a receipt above the ordered quantity is refused or recorded as an evented exception with a reason class |
| **Effect on Accounting** | Cancellation gate: which invoice state blocks a sell-side cancellation, hence when revenue/receivable may be undone |
| **Effect on Tenant/Company** | The default is platform-owned; the override is company-scoped configuration (`CF-I-07`) |
| **Effect on Audit/Control** | Under `warn-and-allow`, every allowed breach must emit a recorded owed-condition — otherwise the control degrades to a silent no-op, which `EP-P` forbids |
| **Affected scenarios** | 22-scenario rows **5** and **10**; `SA15` `E2E-01` |
| **Affected vetoes** | None |
| **Required before Pre-Test starts?** | **No** — both branches are testable; the suite writes the branch Boss rules |
| **Consequence of deferment** | Three controls stay unspecified at their default; Pre-Test cannot state an expected result for the unconfigured case, which is the commonest case in a new tenant |

---

### `F3` — DROPSHIP VALUATION AND COST LANDING

| | |
|---|---|
| **Decision IDs** | `XMC-D-01` · `C2-D-02` |
| **The question, one sentence** | **When goods move supplier→customer with no internal end, does SMEsPlus emit two valuation facts, or none — and where does the cost land, bound to the sale by what identity?** |
| **Why Boss authority** | `SA_CORR3_12` `B-4`: *"Both readings are consistent with every fact in the corpus"*, and the boundary rule that decides four other Inventory rows **has no case for a movement with no internal end**. `SA_CORR2_02` §6: *"Both reference generations are `FACT VERIFIED` and they disagree. Choosing between them is a determination"* |
| **Existing ruling context** | `XMC-C-C6` — *every revenue recognition produces either a cost recognition bound to the same identity or an explicit recorded determination that none arises; **silence is not a permitted answer***. **That clause forces the question to be answered; it does not answer it** |
| **Evidence** | The reference records a dropship movement and then **excludes it from valuation on three independent paths**; revenue, receivable and tax are recognised with **no cost**, and the cost lands on the vendor bill at the bill's date, **unlinked to the sale** (`C2-F-02`). `H-02` grades the movement→valuation hop `SEMANTICALLY INCOMPATIBLE — MEASURED`; `H-03` grades the cost→revenue link `NO IDENTITY`. **The routing itself is determined** in the SMEsPlus-owned design (`XMC-F-03`: *"direct shipment from supplier to customer"* is a named template) |
| **Alternatives** | (a) two valuation facts — a notional receipt and issue, giving a bound cost · (b) none, with an explicit recorded determination under `XMC-C-C6` and the cost bound by the accounting event identity instead |
| **SMEs Core recommendation** | **None offered — and that is deliberate.** CORR3 carried this **with a standing dissent**: *"a second executor's buy-side evidence suggests the answer may be available without a decision"*. **This session did not resolve the dissent** (doing so would need the buy-side package re-read, which is outside a final-gate round's delta-first scope) and presents it unresolved, as CORR3 required |
| **Dissent / challenge result** | **Live and unresolved — Boss should see it before deciding.** If the dissent is right, this becomes a determination and leaves the Boss list |
| **Effect on Inventory** | Whether a dropship line creates movement facts at all |
| **Effect on Accounting** | Whether `XMC-C-C6`'s symmetry is met by a bound cost or by a recorded determination |
| **Effect on Tenant/Company** | None |
| **Effect on Audit/Control** | Under (b), the recorded determination becomes the audit artefact and must be evented |
| **Affected scenarios** | `SA15` `E2E-05`; 22-scenario row **18** via `XMC-C-D6`'s carve-out |
| **Affected vetoes** | None |
| **Required before Pre-Test starts?** | **No** |
| **Consequence of deferment** | `E2E-05` keeps two named breaks; the dropship cost-to-revenue link stays untestable |

---

### `F4` — CROSS-MODULE CONTRACT SCOPE AND SUPPLY BINDING

| | |
|---|---|
| **Decision IDs** | `XMC-D-02` · `C2-D-01` |
| **The question, one sentence** | **Does the Boss-approved 16-element handoff contract govern every cross-module boundary or only Inventory → Accounting — and when a manufacturing shortage raises supply, is the fulfiller hard-bound or soft-bound?** |
| **Why Boss authority** | `XMC-D-02`: the contract's scope is *"unambiguous at primary text — one boundary, one direction"*, so widening it **amends a Boss-approved control** — *"Nothing to research; something to decide"*. `C2-D-01`: `SA_CORR2_02` §6 assigns it *"SMEs Core design position → **Boss confirm**"* |
| **Existing ruling context** | `03_BOSS_APPROVAL_…MINIMUM_HANDOFF_DATA_CONTRACT` §3 (the 16 elements) and §4 (the `PASS / VERIFIED` gate). **Eleven of twelve mandated handoffs currently have no element contract** |
| **Evidence** | `C2-D-01` is **narrowed by existing evidence** (`SA_FINAL_02` #10): `BN-04` is re-graded **`PARTIAL`**, ownership is `FACT VERIFIED`, the routing template *"make-or-buy on demand"* exists in the SMEsPlus-owned design, and the target fact-ownership matrix already binds the fulfiller **softly** — *"Hard trigger, soft binding (Inventory does not know who will respond)"*. **Boss is confirming a stated position, not choosing in a vacuum** |
| **Alternatives** | `XMC-D-02`: extend the one contract to all boundaries · give each boundary its own contract · leave it at one boundary and accept eleven uncontracted handoffs. `C2-D-01`: confirm **soft binding** · require **hard binding** to a named fulfiller |
| **SMEs Core recommendation** | `XMC-D-02` → **extend**, because `XMC-C-D2` makes a rule addressed to a receiver with no element capable of satisfying it *not a rule*. `C2-D-01` → **confirm soft binding**, as the target design already states |
| **Dissent / challenge result** | None outstanding |
| **Effect on Inventory** | `C2-D-01` sets whether a shortage creates an obligation on a named party |
| **Effect on Accounting** | `XMC-D-02` sets how many boundaries must carry elements 1–16 |
| **Effect on Tenant/Company** | Extending the contract extends `HF-CTX-01`/`-02` mandatory carriage to eleven more boundaries |
| **Effect on Audit/Control** | Extending multiplies the attestation obligations (`HF-CTX-06`, `-11`) accordingly |
| **Affected scenarios** | 22-scenario row **18**; `SA15` `E2E-04`, `E2E-06` |
| **Affected vetoes** | None directly |
| **Required before Pre-Test starts?** | **`XMC-D-02` — YES.** It determines the Pre-Test Matrix's own scope: how many boundaries have an element contract to test against. `C2-D-01` — no |
| **Consequence of deferment** | Pre-Test builds a matrix over one boundary and discovers eleven more later, which is a re-scope rather than an increment |

---

### `F5` — MANUFACTURING OVERHEAD GOVERNANCE

| | |
|---|---|
| **Decision IDs** | `BLK-07` restatement · `BLK-08` restatement · veto-limb-2 restatement (together `POH-D-06`/`B-6`) · `POH-D-01` · `POH-D-02` · `POH-D-03` · `POH-D-04` · `POH-D-05` · *(the three restatements are one act with three subjects)* |
| **The question, one sentence** | **Restate or confirm `BLK-07`, `BLK-08` and veto limb 2 in the form the evidence now supports, and rule the four policy elections underneath them.** |
| **Why Boss authority** | *"**Governance act.** A Boss-owned blocker can only be retired, restated or confirmed by Boss."* `POH-D-01` *modifies a standing Boss decision* (`BD-04`). `POH-D-02` *changes the charge itself* and has *unresearched tax consequences* |
| **Existing ruling context** | `BD-02` — **the destination of unabsorbed overhead is already CLOSED by Boss**. `BD-04` — one allocation driver per configuration context, which `POH-D-01` proposes to depart from per cost class |
| **Evidence** | **`BLK-07` as currently worded is unanswerable**: its §3 states a binary — *normal capacity or actual hours* — and **its own §6 already rejected the second branch by name** (*"`REJECTED — INVALID ASSUMPTION`… breaches TAS 2 ¶13, undefined at zero output, capitalises idleness into inventory"*). *"A Boss asked to decide 'normal capacity or actual hours' is being asked to choose between an option and an option his own registers rejected, while the choice that is actually live is not on the paper"* (`POH-F-12`). **The live choice is `POH-D-02`, a depreciation-method election, carried under a different identifier.** The three SMEs Core design gaps beneath the blocker (`POH-G-01` pool + denominator + capture, `POH-G-02` receiver, `POH-G-04` variance) were **closed at specification level by CORR5** (`SA_CORR5_10A`) |
| **Alternatives** | Restate `BLK-07` as the `POH-D-02` election and confirm normal capacity as the absorption denominator · re-affirm the original binary · retire `BLK-07` and carry only `POH-D-02` |
| **SMEs Core recommendation** | **Restate.** Confirm **normal capacity** as the absorption denominator (it *"comes from statute, not from analysis preference"*), confirm the `BD-04` departure per cost class, and put the live choice — straight-line vs units-of-production absorbed at normal capacity — before Boss as `POH-D-02` with its tax consequences unresearched and stated |
| **Dissent / challenge result** | `SA_CORR3_03` §13.3 names its own headline as the first thing a challenger should attack; the challenge was run and the headline held. **The over-absorption cap's *strength* remains a declared statutory dependency (`HOLD`)** |
| **Effect on Inventory** | WIP value composition gains the absorbed-overhead component (`SA_CORR5_10A` §3) |
| **Effect on Accounting** | The variance event's owner, mechanism and destination (`BD-02` for under-absorption) |
| **Effect on Tenant/Company** | The capacity register is company-scoped; the operation classes are platform-owned |
| **Effect on Audit/Control** | The per-pool closure identity is the publication gate; a non-zero residual raises and never re-absorbs |
| **Affected scenarios** | 22-scenario rows **16**, **17**; `SA15` `E2E-03`, `E2E-13`, `E2E-17` |
| **Affected vetoes** | **Veto limb 2** — undischarged and, as written, undischargeable; the mutual-exclusion mechanism it would test is specified at `SA_CORR5_10A` §4 |
| **Required before Pre-Test starts?** | **No** |
| **Consequence of deferment** | Two scenarios keep an expected-value gap; the absorption suite cannot state a numeric expectation |

---

### `F6` — CROSS-COMPANY VISIBILITY AND COMMERCIAL SCOPE

| | |
|---|---|
| **Decision IDs** | `MTI-D-04` · `RC-D-03` · `RC-D-04` · `TV6-BOSS-02` |
| **The question, one sentence** | **Does a sanctioned cross-company read exist inside a tenant at all — and if so who owns the mapping layer, what escalates a tenant to the Private Company model, and is a product's base sell price a tenant fact or a company fact?** |
| **Why Boss authority** | R1 `11`: *"A real Thai SME group need, and a deliberate hole in an isolation boundary. **Only Boss may authorise a door.**"* The other three are the doors' consequences and one commercial scope election |
| **Existing ruling context** | `BD-ACC-02` — no cross-company statutory posting, offsetting, settlement or filing; management views permitted. `MTI-D-01`/`-02`/`-03` ruled. `MTI-22` is the only permitted cross-company means and its register is **complete at register level** with three entries |
| **Evidence** | `XCR-02` (the cross-context report grant) is `SPECIFIED — CONDITIONAL (MTI-D-04)`; `CF-XCR-GAP-01` — a required mapping/provenance relationship class — **is deliberately un-numbered because giving it an entry would place an unspecified object in a register whose completeness is the isolation claim**. `AAS-V-03` forbids any such grant carrying valuation content while the COGS gap stands. **And CORR5 traced the one cross-company path that does exist at data level**: 1,201 completed legs into a company-less transit place paired with 1,201 out of it — the `XCR-01` shape, never one movement spanning two companies |
| **Alternatives** | `MTI-D-04`: **no grant in v1** · a read-only enumerated grant · a broader grant. `TV6-BOSS-02`: tenant-scoped price · company-scoped price |
| **SMEs Core recommendation** | `MTI-D-04` → **"no cross-company grant in v1; the group-view need is met by per-company export."** It settles `XCR-02`, `CF-XCR-GAP-01`, `AAS-V-03`'s subject and `CF-I-03`'s exception-path test data **in one ruling**, and can be widened later without unbuilding anything. `TV6-BOSS-02` → **company-scoped**, because a price that cannot differ by company while everything consuming it can will produce cross-company margin figures no one can defend |
| **Dissent / challenge result** | Recorded counter-argument: *"Not deciding is not neutral — the need gets met by export, which is the worst outcome"* (R1 `11`). Under the recommendation the export route becomes the **designed** answer rather than the informal one |
| **Effect on Inventory** | Whether the mapping/provenance object is commissioned at all (`RC-D-04`) |
| **Effect on Accounting** | Cross-company management views; `BD-ACC-02`'s boundary is unaffected either way |
| **Effect on Tenant/Company** | **This family is the company boundary.** A grant is the only sanctioned crossing |
| **Effect on Audit/Control** | `XCR-02` needs grant identity, granting authority, scope, expiry and a log entry per use; `MTA-11` records that **every grant mechanism degrades toward permanence** and no review cadence is designed anywhere |
| **Affected scenarios** | 22-scenario row **15**; `MTI-22`, `MTI-44`, `CF-I-03` `P5` |
| **Affected vetoes** | **`AAS-V-03`** and **`CF-V-02`** — both are held open by this family |
| **Required before Pre-Test starts?** | **`MTI-D-04` — YES.** `CF3-P-04` (the cross-company exception path) either has test data or is struck; the isolation suite cannot be scoped without knowing which |
| **Consequence of deferment** | Two vetoes stay active on a ground no further specification can move, and the isolation suite is built against an unknown exception set |

---

### `F7` — AUTHORIZATION AXIS AND CONFIGURABLE-RECORD SCOPE

| | |
|---|---|
| **Decision IDs** | `RC-D-01` · `RC-D-02` · `CF-D-01` · `CF-D-02` |
| **The question, one sentence** | **Is `location` an authorization axis; what closes the configurable-record enumeration; is `MTI-D-03`'s "Unit of Measure Category" the same object as the context matrix's "Unit group and unit"; and what closes the platform-owned operation-class enumeration?** |
| **Why Boss authority** | `CF-D-01`'s ground is decisive and general: ***"only Boss may state what a Boss ruling covers."*** The other three close enumerations that Boss rulings opened |
| **Existing ruling context** | `MTI-D-02` ruled `AUTH` = **Company + Warehouse + Operation-Type** and location is **not** among them; `MTI-D-03` names the tenant-changeable boundary |
| **Evidence** | `CF-I-01` fixes the four-axis tuple; **`location` anchors records (`CTX`) and is not ruled an authorization axis** — five matrix rows are unsettled on it. `CF-I-05` is `SPECIFIED — CONDITIONAL (CF-D-02)`; **`CF-D-02` option (c) would withdraw `CF-I-05` entirely**. `CF-I-07` is `SPECIFIED — CONDITIONAL (RC-D-02)` because the class list is open-ended. **`CF-D-01` currently leaves one anchor row (`17`) with two possible answers** — the single residual on `MTI-05` after CORR5's adjudication |
| **Alternatives** | As each register states; `CF-D-02` in particular: close at the eight illustrated classes with an addition process · derive from the `INV-F-*` function set · rule that no platform class exists and withdraw `CF-I-05` |
| **SMEs Core recommendation** | As the registers state; **no new position is originated here** |
| **Dissent / challenge result** | None outstanding |
| **Effect on Inventory** | `RC-D-02`/`CF-D-01` fix the anchor of two configurable record classes |
| **Effect on Accounting** | Indirect — through the operation-class binding of controls |
| **Effect on Tenant/Company** | `RC-D-01` decides whether a warehouse-scoped actor can be further confined by location |
| **Effect on Audit/Control** | **`AUD-C-A5`** (the situational location axis) and the negative-access substitution tests `S-01`…`S-08` enumerate exactly the ruled axes; `CF-I-03` `D5`'s domain narrows or widens with `RC-D-01` |
| **Affected scenarios** | Row **15** and every row's authorization dimension; `MTI-05` row 17 |
| **Affected vetoes** | `RC-V-01`'s under-inclusive condition touches the same rows |
| **Required before Pre-Test starts?** | **`RC-D-01` — YES**, because the axis set is the negative-access suite's own denominator. The other three — no |
| **Consequence of deferment** | The negative-access suite is written over an axis set that may change, which is the *wrong-denominator* class the programme has recorded repeatedly |

---

### `F8` — IDEMPOTENCY SEVERITY

| | |
|---|---|
| **Decision ID** | `C-02` |
| **The question, one sentence** | **Is the absence of a deterministic idempotency identity gate-blocking, or a design input that a phase may pass with?** |
| **Why Boss authority** | Owner *"Boss directly"* on **five independent instruments**: R4 `07_L6` line 210 and line 222 (*"an unresolved Boss decision across multiple rounds… R4 does not decide it"*), R1 `03` §7.2, R2 `04` §7.2, `GAP-FS-06`, and the SMEsPlus-owned functional design itself — *"Carried finding `C-02`: whether this is gate-blocking is Boss's decision"* |
| **Existing ruling context** | `BD-ACC-01` ruled the *object*: same-event retry must not create duplicate accounting events, and the Accounting Core owns the identity. **`UAE-29`, the Account programme's "no accounting-event identity" root blocker, is thereby ruled.** `C-02` asks only about **severity** |
| **Evidence** | Element 15 is **specified** by CORR5 (`E15-A1`, `XMC-C-A14`) and **not built**. The estate's only carrier is table-global and **populated on 0 of 13,814 rows**, so a uniqueness test over it passes on every row. The Boss-approved handoff contract §4 already forbids `PASS / VERIFIED` where duplicate effects cannot be prevented *"when idempotency is required"* |
| **Alternatives** | (a) gate-blocking — no phase may close while element 15 is unproven · (b) design input — the specification suffices for Phase SA and the proof is a Pre-Test/build obligation |
| **SMEs Core recommendation** | **(b) design input, not phase-holding** — at scenario level the contract §4 already makes duplicate prevention a `PASS / VERIFIED` precondition, so the protection Boss would be buying with (a) already exists one level down |
| **Dissent / challenge result** | **CORR5's first freeze declared this "dissolved by standing rulings" and two challengers independently reversed it** — a commissioning prompt is not a ruling, and four registers say the owner is Boss. **Presented here as open precisely because the executing party twice tried to close it** |
| **Effect on Inventory** | None to the specification; `MTI-31` and `XMC-C-A14` stand either way |
| **Effect on Accounting** | None to the specification |
| **Effect on Tenant/Company** | None |
| **Effect on Audit/Control** | Under (a), no gate may close until `RT-E15-01`…`-09` execute |
| **Affected scenarios** | Row **22** — and, under (a), **every** row, since element 15 is the join key |
| **Affected vetoes** | None directly; interacts with `AAS-V-01`/`CF-V-01`'s runtime scope |
| **Required before Pre-Test starts?** | **No — but it sets Pre-Test *exit* criteria** and should be ruled before exit criteria are agreed |
| **Consequence of deferment** | Pre-Test may reach the end of its matrix without an agreed rule on whether an unproven element 15 blocks closure — which is the argument arriving at the worst moment |

---

## 3. Cross-family note Boss may act on once

**`F2` is one principle asked three times. `F6` and `F7` are the Inventory programme's own open
registers, already before Boss in that programme's decision package** — Phase SA inherits them and
does **not** re-ask them as new; they appear here so that the Phase SA consequence of each is visible
in one place. **Ruling `F2` and `F6` alone closes 5 of the 27 decisions and unblocks two vetoes.**

## 4. Boss ACTS requested — not decisions (`SA_FINAL_02` §4.2)

| Act | What is being asked | Why it is an act |
|---|---|---|
| **`B-7`** | Appoint a `Q-BOSS-02`-eligible structurally independent challenger for the Phase SA package | `Q-BOSS-02` control 2 **forbids a session selecting its own challenger**. One correct form; no alternatives |
| **`C4-D-01`** | Commission the Boss-mandated `ACCOUNTING_INVENTORY_INTERFACE_CONTRACT_AND_CROSS_PROOF`, and direct the merge-or-archive disposition of the 20 stranded architecture deliverables | The artefact is **mandated by a standing Boss approval** and exists in `0` of the corpus's paths; the disposition is PMO's once directed |
| **`C4-D-02`** | Appoint the independent review that decides the platform-actor model (**R1** separate identity domain vs **R2** scoped role) | CORR4 re-scoped it from a design act to *"a governance act plus an independent review"*; CORR5 left both models standing with a recommendation for R1 |
| **`AAS-V-02` discharge** | Ratify AAS+'s discharge of a veto whose stated condition — `MTI-D-01`, `-D-02`, `-D-03` ruled — **is satisfied** | R2: *"CONDITION SATISFIED — NOT DISCHARGED … never reported as lifted"*. Discharge is the issuer's act, ratified by Boss |
| **Thai user panel** | Commission the Thai user validation panel | `18_THAI_USER_VALIDATION_CHECKLIST` line 11: **"Boss to commission"**. It unblocks `R4-Q-01` (reason-code labels), `GAP-FS-11` and every Thai label in the corpus, all of which are `candidate / UNVALIDATED` |

## 5. Checkpoint

> ## `CP-SA-FG-30 — DECISION FAMILIES CONSOLIDATED`
> **27 decisions in 8 families · 5 acts separated · 3 families carry a Pre-Test-entry-gating member
> (`XMC-D-02`, `MTI-D-04`, `RC-D-01`) · 1 family (`F3`) carries a live unresolved dissent · 0 new
> decisions originated.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
