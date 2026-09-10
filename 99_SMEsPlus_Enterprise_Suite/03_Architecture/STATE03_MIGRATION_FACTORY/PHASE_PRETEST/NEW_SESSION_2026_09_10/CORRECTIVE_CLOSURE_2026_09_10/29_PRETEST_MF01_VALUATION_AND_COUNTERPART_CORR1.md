# 29 — `MF-01` VALUATION AND COUNTERPART · `MF-03` RE-CLASSIFICATION — `CORR1`

## `CHECKPOINT C (part 3) + E (part 1) — CC-F-11 NARROWED · CORE-06 SPECIFIED · MF-03 RE-DERIVED`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7-RETURN-CORR1-001]` · Boss: **SOLE FINAL APPROVER**

> **Prompt §6 and §7 are both `T7`. They are answered in one file so the `MF-01`/`MF-03` interaction is
> visible; `MF-03` is §8, under its own heading, and is derived without reference to any `PTX` control.**

---

## 1. The claim being retired

**`CC-F-11`, as published at `17_` §2.1 and `22_` §7.1:**

> *"**`MF-01` creates value with no purchase and no movement.** **Every** valuation rule in the corpus
> binds value to a **movement** (`JT-04` = recognition at the physical movement). Opening balance has no
> movement, **so no existing rule reaches it**, and its counterpart account is undetermined."*

**The clause *"no existing rule reaches it"* is WITHDRAWN.** It is a universal negative that was never
measured against the ruled costing methods. `B7-F-09` falsified it on the `Standard` branch;
§2 falsifies it on `Average` as well, and finds the **narrower gap that is actually there**.

**The clause *"its counterpart account is undetermined"* SURVIVES** and is closed at §6.

### 1.1 The conflation that produced the error

| Two different things `CC-F-11` treated as one | |
|---|---|
| **Cost-of-sales RECOGNITION** | movement-bound — `JT-04`, `SC-BD-05`, ruled |
| **Initial CARRYING VALUE** | **not movement-bound under any ruled method.** `BD-ACC-03B` sets it from a **Product-Category policy**, not from a movement's carried cost |

**`MF-01` establishes a carrying value. It recognises no cost of sales. `JT-04` never reached it, and
never needed to.**

---

## 2. `MF-01` under each ruled valuation mode — tested separately

**Governing authority at primary text:**
`BD-ACC-03A` — Inventory Valuation Recognition = `Periodic | Perpetual`; **policy authority Product
Category only**. `BD-ACC-03B` — Costing Method = `Standard | Average | FIFO`; **policy authority Product
Category only**. Product > Accounting permits **only** `Income Account`, `Expense Account`,
`Price Difference Account`; blank inherits Product Category.
`HX-24` — *"certified opening balances, **quantity and value**"*; the only **dual-target** handoff.

| Mode | Does a rule reach `MF-01`? | Mechanism | Residual |
|---|---|---|---|
| **`Standard`** | **YES** | Carrying value = **standard cost × quantity**, set by Product Category policy independent of any movement. `SA_CORR3_03`: *"under standard costing, work-centre cost **never enters finished-goods value**"* — value is a policy attribute, confirming the mechanism from the other side | The certified extract's value will differ from `standard × qty`. **The difference is a variance with an existing destination — the `Price Difference Account`**, which is one of the three permitted Product-Accounting overrides. **A rule reaches both the value and the difference** |
| **`Average`** | **YES** | The certified extract supplies quantity **and** value; their quotient **is** the opening moving average. No further rule is required — the flow originates the average rather than adjusting one | **None at origination.** (The `Average` residual that gates rows 8/9 arises on **reversal**, not on opening — a different event) |
| **`FIFO`** | **NO — and this is the real gap** | `FIFO` is **layer-ordered**: value is carried as an ordered set of `(quantity, unit cost, acquisition sequence)` layers, and every subsequent issue consumes the oldest layer. **`HX-24` carries `quantity` and `value` as an AGGREGATE.** An aggregate cannot reconstruct layers: infinitely many layer sets share one total | **`CORR1-F-02`** — see §3 |
| `Periodic` vs `Perpetual` (`BD-ACC-03A`) | **Not determinative for `MF-01`** | Recognition **timing**, not carrying-value **derivation**. Opening balance is dated at cutover under both | — |

### 2.1 The eight questions §6 requires, answered

| # | Question | Answer |
|---:|---|---|
| **1** | Can a certified opening balance create stock value without purchase? | **YES.** `HX-24` carries *"quantity and value"* by design; the value originates from a **certified legacy extract**, not a purchase. This is not a defect — it is what a cutover is |
| **2** | Is movement mandatory? | **NO for carrying value** (§1.1). **YES for cost-of-sales recognition** (`JT-04`). The two were conflated |
| **3** | Can a valuation layer/event originate from migration? | **Under `Standard` and `Average`, no layer is needed. Under `FIFO` it MUST, and `HX-24` cannot supply it** — §3 |
| **4** | Required counterpart account | **SPECIFIED at §6** — a Migration Opening Balance Control Account that must net to zero at cutover certification |
| **5** | Reconciliation behaviour | certified extract ↔ opening position, **plus** the control account's zero-net test — §6.2 |
| **6** | Historical cut-off semantics | the **cutover date**, never the system date; the period object is `XMC-C-A15`; a pre-cutover-dated correction is `XMC-C-A16` (candidate rule, statutory `S`) |
| **7** | COGS consequence | the opening basis **is** the basis for the first post-cutover `JT-04` recognition. **Under `FIFO` the §3 gap propagates directly into COGS**, because the first issue consumes a layer that was never established |
| **8** | Tenant / Company ownership | **per-Company**, certified per Company (`L10-07`); element `10` carries tenant/company context; `BD-ACC-02` keeps statutory posting company-scoped |

---

## 3. `CORR1-F-02` — the `FIFO` layer gap

> **`MF-01` as specified cannot establish a `FIFO` opening position, and no register records this.**

| | |
|---|---|
| **The defect** | `HX-24` specifies *"quantity and value"*. `FIFO` requires **ordered layers**. An aggregate total is not reducible to layers |
| **Why it was invisible** | `CC-F-11`'s universal *"no rule reaches `MF-01`"* was **true-sounding and wrong**, and it **covered this**. A universal negative that is false in two of three branches conceals the branch where it is true |
| **Scope** | any Product Category whose `BD-ACC-03B` method is `FIFO`. `BD-ACC-03B` is Product-Category-scoped, so **`FIFO` categories can coexist with `Standard` and `Average` categories in one Company** |
| **Consequence if unaddressed** | either the migration silently collapses `FIFO` to a single synthetic layer at average cost — **changing the valuation method by the act of migrating** — or the first post-cutover issue consumes a layer that does not exist |
| **Owner** | **SMEs Core / Architecture — a specification act, not a Boss election.** The requirement follows from `BD-ACC-03B` as already ruled; nothing new is being elected |
| **Required correction** | **`HX-24`'s payload must carry layer granularity for `FIFO` categories**: `(quantity, unit cost, acquisition sequence or date)` per layer, with an explicit `N/A + reason` for `Standard` and `Average` categories where the aggregate is sufficient. **Recorded as new obligation `CORE-07`** |
| **Boss item?** | **NO.** §15 minimization: the evidence resolves it |

---

## 4. `CC-F-11` restated — the surviving claim

> ### `CC-F-11` (CORR1)
>
> **`MF-01` creates carrying value without a purchase and without a movement, and that is correct by
> design.** Under **`Standard`** the Product-Category standard cost reaches it and the difference lands
> in the `Price Difference Account`; under **`Average`** the certified value *is* the opening average.
> **Under `FIFO` no rule reaches it, because `HX-24` supplies an aggregate where `FIFO` requires ordered
> layers (`CORR1-F-02`).** **What remains undetermined across all three modes is the counterpart account**,
> closed at §6.

**`0` findings deleted. `17_` §2.1 and `22_` §7.1 remain Audit Lineage and are not edited; this section
supersedes their universal clause.**

---

## 5. `IR` / `AR` convergence — effect of this file

| Register | Denominator | Reconciled before | **After** |
|---|---:|---:|---|
| `IR` | `20` | `14` | **`14`** — `MF-01` remains `NOT RECONCILED` while `CORR1-F-02` and `CORE-06` are open |
| `AR` | `30` | `15` | **`15`** — as above |

**A narrowed finding is not a reconciled flow. `MF-01` moves from *"no rule reaches it"* to *"two of three
modes reach it, one does not, and the counterpart is now specified"* — which is a better description of
the same open item, not a closure.** `0` reconciled counts rise.

---

## 6. `CORE-06` — counterpart-account architecture, SPECIFIED

**§15 requires Architecture to attempt this before Boss. It is resolvable, and is resolved here.**

### 6.1 The determination

> **The counterpart of a certified opening balance is a `MIGRATION OPENING BALANCE CONTROL ACCOUNT` —
> a Company-scoped control account that MUST net to zero at cutover certification. It is NOT a direct
> posting to equity.**

**Reason, stated so it can be attacked:** a direct-to-equity credit is unreconcilable. It leaves no
artefact against which the certified extract can be proved, and no state in which the migration is
*"complete"* as distinct from *"partially posted"*. A control account makes the cutover **falsifiable**:
its balance is the exact measure of what has been asserted and not yet certified, and its required end
state is a single testable number.

### 6.2 Specification

| Element | Determination |
|---|---|
| **Account class** | control / suspense, **Company-scoped** (`BD-ACC-02` keeps statutory posting company-scoped) |
| **Posting** | `Dr Inventory` (per the §2 mode) · `Cr Migration Opening Balance Control` |
| **Required end state** | **balance = `0`** at cutover certification, per Company |
| **Non-zero balance means** | the certified extract and the loaded position disagree. **A non-zero balance is a FAILED cutover, not a rounding item, and must block certification** |
| **Reconciliation control** | certified extract total ↔ loaded opening position ↔ control-account movement — a three-way tie-out, per Company, per costing mode |
| **Clearing** | on certification, to the Company's opening-equity account. **Which equity account is a chart-of-accounts configuration, not an architecture decision** |
| **Provenance** | every posting carries `XMC-C-A17` (batch identity · source system · source record · mapping rule identity **and version** · load-act attempt identity · evidence reference) |
| **Audit** | the certification act is evented and approved; the control account is **not** manually adjustable |

### 6.3 What is NOT closed by this specification

| Residual | Owner |
|---|---|
| The **equity account identity** into which the control account clears | **Company chart-of-accounts configuration** — a deployment act, not a design act |
| Whether Thai statutory rules constrain the **presentation** of a migrated opening equity | **Thai statutory** — added to `36_` as a new external item |
| `CORR1-F-02` — `FIFO` layer granularity | **`CORE-07`**, SMEs Core |

| | |
|---|---|
| **`CORE-06` status** | **DISCHARGED at architecture level.** The mechanism, its control, its failure semantics and its provenance are specified |
| **Boss item?** | **NO.** The two residuals are a configuration act and a statutory question, neither of which a Boss ruling can supply |

---

## 7. `MF-03` — re-classification without any `PTX` control

**`B7-F-10` is upheld against the reasoning:** `17_` §2 excluded `MF-03` because it *"adds ZERO
quantity"* and *"adds ZERO value"*, cited to **`RT-E15-05`** — a control at **`0 of 11` satisfied**, over
an element (`15`) that is **unbuilt**. **A property guaranteed by an unbuilt control is an intention, not
a fact.** That reasoning is **WITHDRAWN**.

### 8. `MF-03` derived from business semantics alone

| Criterion | `MF-01` | `MF-02` | **`MF-03` Replay / re-run** |
|---|---|---|---|
| **Trigger** | cutover | cutover | **a prior migration batch is executed again** |
| **State transition — target** | none → stock and value at cutover | none → history | **intended IDENTICAL before and after** |
| **State transition — own** | the opening position | the history set | **a new load-act ATTEMPT identity beside an UNCHANGED occurrence identity** (`XMC-C-A17`, `A14`) |
| **Quantity change** | creates quantity | none (historical) | **originates none of its own** — any quantity it moves is `MF-01`'s or `MF-02`'s |
| **Value change** | creates value | none | **originates none of its own** |
| **Ownership** | Migration → Inventory + Accounting | Migration → Inventory | Migration |
| **Accounting consequence** | opening posting (§6) | none | **none of its own** |
| **Inventory consequence** | opening position | none | **none of its own** |
| **Historical identity** | cutover date | original dates | **original identities preserved; a new attempt identity added** |
| **Consumer** | Inventory + Accounting | Inventory | both — **but only via `MF-01`/`MF-02`** |
| **Reversal** | undetermined (element 13) | undetermined | **replay is not a reversal** |

### 8.1 The determination, and why it is a `B` and not a `C`

> ## `MF-03` = **`B` — EXECUTION MODE**

**`MF-03` originates no business fact that `MF-01` or `MF-02` does not originate.** Every quantity and
every value it can put into Inventory or Accounting is, by construction, a quantity or value **of one of
those two flows being run again**. Its only distinct state transition is on the **load-act attempt
object** — a new attempt identity beside an unchanged occurrence identity — which is **provenance
metadata about an execution**, not a movement of stock or value.

**A register of material flows counts state transitions of stock and value. `MF-03` contributes none of
its own. It is a mode in which `MF-01` and `MF-02` are executed.**

**Note the distinction from `C` (migration dimension):** a *dimension* would be an attribute that varies
across the flows (as a costing mode does). Replay is not an attribute of a flow; it is **an act performed
upon one**. `B` is the exact class.

### 8.2 Where B-7's real objection goes — it is not discarded

**B-7 exposed a genuine risk and mis-located it.** The risk is not *"`MF-03` might be a flow"*; it is:

> **`MF-03`'s zero-effect is UNPROVEN, so `MF-01` and `MF-02` can double-post on re-run.**

**That is a defect of `MF-01`/`MF-02` execution, not a member of the flow denominator.** It is re-routed:

| Destination | Why |
|---|---|
| **`X-22`** (retry / idempotency / replay) | the scenario whose entire subject this is; `WRITABLE`, `0 of 22` verified |
| **element `15`** / `MTI-50` | the mechanism that must exist for the property to hold |
| **`RT-E15-05`** within `PTX` | the control that tests it — **`0 of 11`, unchanged, and NOT cited as proof of anything here** |
| **`CORR1-F-03`** | **NEW FINDING:** *"`MF-01` and `MF-02` are admitted to `IR`/`AR` while the idempotency of their execution is unbuilt and untested. A re-run before element `15` exists can duplicate an opening balance, and nothing in the flow registers records that exposure."* Owner: SMEs Core → Functional Design |

**Result: `MF-03`'s exclusion from `IR`/`AR` is CONFIRMED on an evidence-independent basis, the defective
reasoning is withdrawn, and the risk B-7 found is preserved where it can be tested.**

---

## 9. Checkpoint

> ## `CHECKPOINT C (part 3) + E (part 1)`
>
> **`CC-F-11`'s universal clause WITHDRAWN and restated: `Standard` and `Average` both reach `MF-01`;
> **`FIFO` does not, and that is `CORR1-F-02` — a gap the false universal was concealing** ·
> the conflation named: **cost-of-sales recognition is movement-bound, initial carrying value is not** ·
> **`CORE-06` DISCHARGED at architecture level** — Migration Opening Balance Control Account, net-zero at
> certification, non-zero = failed cutover; `2` residuals routed to configuration and statutory, **`0` to Boss** ·
> **`MF-03` = `B` EXECUTION MODE**, derived with `0` reference to any `PTX` control; exclusion confirmed,
> reasoning replaced · **B-7's underlying risk preserved as `CORR1-F-03`** ·
> `IR 14/20` and `AR 15/30` — **`0` reconciled counts rise** · `2` new obligations (`CORE-07`, `CORR1-F-03`), `0` new Boss items.**

No Evidence = No Progress. A narrowed finding is not a closed one. Boss is the sole Final Approver.
