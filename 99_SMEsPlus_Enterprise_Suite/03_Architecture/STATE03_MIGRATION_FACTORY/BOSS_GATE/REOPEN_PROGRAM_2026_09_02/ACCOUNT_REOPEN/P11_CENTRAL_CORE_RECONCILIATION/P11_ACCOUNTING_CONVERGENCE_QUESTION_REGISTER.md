# P11 — ACCOUNTING CONVERGENCE QUESTION REGISTER (`CQ-P11-01` … `15`)

`[SMEPLUS-26-09-06-…-CORR2-PHASES-001]` · `CP-P11C2-07` · **PHASE S — DOMAIN PURITY FIRST** · AI EOS **NOT ACTIVE**

> Every item is a **CANDIDATE** until Phase B / Phase C / Boss Pre-Design Gate.
> Every peer fact is **received and attributed**, never restated as P11's own.
> **P11 opened no peer lifecycle, module internal, or model internal in CORR2.**

---

## `CQ-P11-01` — Peer accounting input population

**Population:** the **12** P11-addressed artefacts in `P11_CORR2_PEER_CLAIM_SNAPSHOT.md` §3, at the ten
frozen SHAs. **13 are new since CORR1, from 7 peers.**

| Producer | Artefact @ SHA | Material accounting input | Class |
|---|---|---|---|
| `P01` | `P01_TO_P11_HANDOFF.md` @ `b820b29` | `S16-B-05`; GRNI **13,666 posted items / −฿7,048,692.08**; correction is **immutable reversal, 5,115 pairs, 0 unresolvable**; **no lock date on 3 surfaces / 169,143 entries**; AP **97.89 %** reconciled | `CANDIDATE INPUT` |
| `P01` | `P01_P11_S18_DIRECT_VERIFICATION_SUPPLEMENT.md` | **Five P11-carried findings are ONE setting with five consequences** | `CANDIDATE INPUT` |
| `P01` | `P01_P11_EVIDENCE_VERSION_DEPLOYMENT_SUPPLEMENT.md` | `ERR-P01-23`, `ERR-P01-41` — two of P01's own negatives withdrawn | `CONTRADICTED — CORRECTED` |
| `P03` | `P03_TO_P11_HANDOFF.md` @ `bc767a8` | conversion cost **zero in 4 databases**; **30 corrupt valuation records, −48.7 %**; routes 3 decisions | `CANDIDATE INPUT` |
| `P03` | `73_P03_P11_RUNTIME_INVERSION_SUPPLEMENT.md` | *"the two things conversion cost needs have never existed together in any examined deployment"* | `CANDIDATE INPUT` |
| `P04` | `P04_TO_P11_HANDOFF.md` @ `65b8841` | 6 Boss decisions; asset engine **cannot post off-balance**; `P04-B-51` | `BOSS DECISION REQUIRED` |
| `P05` | `65_P05_P11_EVIDENCE_BASE_AND_LIVE_RISK_SUPPLEMENT.md` @ `205e0ac` | evidence base **excluded the target platform**; `RE-20`; petty cash **634 of 993** | `CANDIDATE INPUT` |
| `P06` | `70_P06_P11_SUPPLEMENTAL_CRITICAL_RISK_HANDOFF.md` @ `249b7c2` | `om_data_remove` **installed**, no server-side authorisation, **`REACHABLE — DEPLOYMENT VERIFIED`** | `CANDIDATE INPUT` |
| `P08` | `58_P08_P11_RECONCILIATION_BOUNDARY_HANDOFF.md` @ `194efcb` | what the ledger **can and cannot** supply — 5 supplied, **8 not supplied** | `CANDIDATE INPUT` |
| `P09` | `D25_P09_CHALLENGE_CORRECTION.md` @ `5441f8d` | depreciation nets ~0 per cost centre; **margin overstated**; gross **43×** the net | `CANDIDATE INPUT` |
| `P10` | `P10_TO_P11_HANDOFF.md` @ `1fea562` | three coupled Boss decisions; kernel candidate; population bounded to 4 of ≥10 | `CANDIDATE INPUT` |
| `P10` | `41_P10_P11_DECISION_INTEGRITY_CORRECTION.md` | `T0-13` over-adoption withdrawn; **`OPT-A` restored; option set is six** | `CONTRADICTED — CORRECTED` |

**Disposition: `FACT VERIFIED — CLOSED FOR CURRENT P11 EVIDENCE`** for the population;
**`POST-SNAPSHOT MATERIAL DELTA CANDIDATE`** is the only route to widen it.

---

## `CQ-P11-02` — Accounting event identity

`P08` `58_`, current and **narrowed from the statement P11 wrongly quoted in CORR1**:

> A durable event identity **exists on one inbound channel, on a nullable column, and is unpopulated on
> all 13,814 rows.** *Absent as a **platform property**; not absent as a fact.*

Compounding, all received: **41.89 %** of items cannot name their entry; **17.00 %** carry no origin
mark; **96.1 %** of posted entries carry at least one origin pointer (`P08`). **No as-of
reconstruction** of any balance exists — `amount_residual` is current state only.

> **`CANDIDATE ACCOUNTING TRUTH`:** the identity object required for accounting reconciliation is
> **not present as a platform property in any generation examined by any peer**. Evidence class **`C`**
> — the CORR1 upgrade to `A` is **withdrawn and stays withdrawn** (`P11-E-31`).

**Dependent processes: eight** — `P02`, `P05` (`HE-09`), `P06`, `P07`, `P08`, `P09`, `P10`, `P11`.
**Disposition: `BOSS DECISION REQUIRED — DECISION PACKAGE READY` (`D-5`).**
**P11 designs no event schema.**

---

## `CQ-P11-03` — Business owner vs accounting owner

| Case | Business owner | Accounting owner | Basis |
|---|---|---|---|
| Valuation cost explosion | **`P01`** | P11 reconciles consequence only | **`P01` withdrew its routing to `P03`; `P03` independently reached the same attribution from its own data.** Two processes, opposite directions, one answer |
| `om_data_remove` module | **`P06`** | **P11** owns *reliance* on the zeros it can produce | `P01` `S16-B-05` states the split exactly |
| Depreciation attribution | **`P04`/`P09`** | P11 reconciles the boundary | `P09` `D25` |
| Petty-cash dominance | **`P05`** | P11 reconciles the obligation balance | `P05` `65_` |

> **`P11-G-06`:** a GL consequence does **not** transfer business-process ownership to P11. P11 takes
> **reliance**, never **lifecycle**. This rule was applied to reject four candidate paths (see
> `P11_DOMAIN_PURITY_AND_CROSS_PROCESS_BOUNDARY_REGISTER.md`).

**Disposition: `FACT VERIFIED — CLOSED FOR CURRENT P11 EVIDENCE`.**

---

## `CQ-P11-04` — Recognition and posting timing

Received facts: settlement chronology is **not trustworthy** — **46.4 %** of settlements recorded
*after* their as-of date, **44.3 % before**, maximum **594 days** late (`P08`). Recognition collapsed
into the posting act is `P10`'s root cause. There is **no accounting-period object** (`P08`).

> **`CANDIDATE ACCOUNTING TRUTH`:** occurrence, recognition, posting and settlement are **four
> distinct times**, and the estate reliably carries **one** of them. A reconciliation that
> assumes any two coincide is unsupported.

**Disposition: `UNRESOLVED — SPECIFIC P11 EVIDENCE UNAVAILABLE`**, gated on `D-5` and `P10-D-02`.

---

## `CQ-P11-05` — Debit/credit and account-role truth

> ### The **30 producer debit/credit cells remain WITHHELD.** Fifth challenge survived.

They are not derivable from convention, and CORR2 supplies the sharpest proof yet that deriving them
would have been wrong — `P01` `ERR-P01-49`:

> P01's own earlier wording *"capitalised into inventory / no P&L variance"* was **FALSE IN BOTH
> HALVES**. Measured: **1,175 of 1,267** price-difference layers **never reach the GL**; the **92**
> that do net **−฿7,267,712.95 against Raw material — a reduction, not an addition** — and put
> **−฿2,563.84 on a P&L account**; **1,082 of the 1,175 sit on a bill line posted to P&L**.

> **The convention said "capitalised". The measurement said the opposite, on both halves, in the
> producer's own package.** Any P11 cell filled from convention would have been filled wrong.

**Disposition: `UNRESOLVED — SPECIFIC P11 EVIDENCE UNAVAILABLE`.** Cells stay withheld.

---

## `CQ-P11-06` — Subledger → GL boundary

**`P08` `58_` answers this, and the answer changes the question:**

> *"For the party dimension there is **no independent record to reconcile the ledger against** — the
> subledger **is** the ledger filtered by account, so agreement is **true by construction and
> unverifiable**."*
>
> *"The asset register and the inventory valuation record **are** separate stores; **the kernel imposes
> no tie-out, no periodic proof and no exception**."* — `P08-RQ-KRN-01`

Independently, P11's own re-run reaches **0 subledgers of record, unqualified** out of seven
(`P11_B17_SCOPE_REPAIR_CORR2.md`). **Two routes, one conclusion.**

> ### `P11-C-12` — a genuine convergence, and the most consequential in the package
> **AR/AP "reconciliation" against the GL is not a control.** It compares a set of rows with itself.
> The two places where genuinely separate records exist — **asset register** and **inventory
> valuation** — are exactly the two the kernel **never requires to be tied out**.
>
> **`CANDIDATE ACCOUNTING TRUTH`:** the estate has reconciliation **where it is vacuous** and
> **no reconciliation where it would be meaningful.**

**Disposition: `FACT VERIFIED — CLOSED FOR CURRENT P11 EVIDENCE`**, with the five questions `P08`
routes to P11 carried into `CQ-P11-15` as candidate outputs, **unanswered**.

---

## `CQ-P11-07` — Cost / inventory / COGS accounting consequence

| Received fact | Owner |
|---|---|
| **Five P11-carried findings are ONE setting with five consequences** — `property_valuation = manual_periodic`, global, unoverridden, **126 of 126 categories, all 4 companies**. Gate closed at the valuation-accounting entry point; GRNI bridge, price-difference replay, derived-item deletion and anglo-saxon eligibility **all unreachable in that deployment** | `P01` |
| Conversion cost is **zero in every examined deployment**; **no fixed-overhead cost exercised anywhere** | `P03` |
| **30 valuation records up to ±1.5 × 10²¹, distorting inventory valuation by −48.7 %**; 25 diverge from the ledger | `P03` |
| **49 completed production receipts carry no valuation record**; 280 valued zero; 1,386 component consumptions unvalued | `P03` |
| *"The two things conversion cost needs — resources carrying a rate, and automated valuation — have **never existed together** in any examined deployment"* | `P03` |
| Receipt → valuation → GL **executes** in series 16 — **57,863 of 74,982 layers** | `P01` — *the programme's only positive control for this mechanism* |

> **`P11-C-13` — CORRECTED BEFORE PUBLICATION (`P11-E-37`).**
> `P01` writes: *"Five P11 findings that P11 has been carrying as separate items are not five items…
> P11 should carry this as one decision, not five blockers."* **P11 executed the check against its own
> registers instead of accepting it: P11 does NOT carry five items on this.** The blocker register
> carries **none** of the five; the event-to-GL matrix carries **one** related row (`UAE-12`, an
> unresolved contradiction on price-difference account scope); *"derived journal item"* returns **0**
> occurrences package-wide.
>
> **What is true:** the producer's instruction is **accepted for carriage going forward** — this is
> **one** accounting decision with five consequences, and P11 will carry it as one. **What is not
> true:** that P11 was carrying five and has collapsed them. **The collapse is `0 → 1`, not `5 → 1`,
> and CORR2 does not shrink the package.**
>
> **`P01`'s statement about P11's register is not accurate, and is routed back** — the same class as
> `P10` `G02-R-15`, where a peer described P11's objects without resolving them to register rows.

**Disposition: `FACT VERIFIED — CLOSED FOR CURRENT P11 EVIDENCE`** for the accounting consequence;
`OUT OF P11 SCOPE — DOMAIN PURITY PRESERVED` for every mechanism internal.

---

## `CQ-P11-08` — AR / AP / settlement / reconciliation

Received: settlement graph **63,773 records / 100,580 lines / residual drift 0** at tolerance ≥ 1e-6;
company and journal attribution **447,384 of 447,384**; **0 unbalanced posted entries** in the
reporting currency across **169,143** (`P08`). AP **97.89 %** reconciled, positive control **0 of
52,996** reconciled items carry a residual (`P01`).

**Against that arithmetic soundness stands `CQ-P11-06`:** the agreement is **structural**, not
evidential. **Both are true.** The ledger is internally sound and externally unverified.

**Disposition: `FACT VERIFIED — CLOSED FOR CURRENT P11 EVIDENCE`.**

---

## `CQ-P11-09` — Asset / time-based recognition / tax / analytic boundaries

| Boundary | Received fact | Owner |
|---|---|---|
| Asset | the reference asset engine **cannot post off-balance**, constraining a Boss-approved policy input; asset↔equipment cardinality **unconstrained** | `P04` |
| Time-based | recognition event collapsed into the posting act; **`OPT-A` restored**, option set **six**; `AASP-VETO-01` r3 lifts only on `D-5` **and** `P10-D-02` | `P10` |
| Tax | both WHT subsystems installed together; a rate record **named `WHT3%` valued `0`** with **2,038 payments / ฿21,556,228.06** posted after zeroing, amounts **hand-entered** | `P07`, `P01`, `P05` |
| Analytic | depreciation nets ≈ 0 per cost centre; **margin overstated by the amount erased**; **gross 43× the net**; cross-centre displacement **2,019,008.49 each way** inside entries counted as zero | `P09` |

**Disposition: `EXTERNAL DOMAIN BOUNDARY — CANDIDATE HANDOFF RECORDED`** for all four.

---

## `CQ-P11-10` — Correction / reversal / cancellation

**Healthiest profile measured in the estate** (`P01`): correction is **immutable reversal — 5,115
pairs, 0 unresolvable originals**. Against it: `P10`'s correction algebra gives **three outcomes,
domain-selected**, and *"the operations are not shared"*; `P05` carries a correction/reversal boundary
at v3; `P07` a correction/reversal lineage matrix.

> **`P11-C-14`:** correction is the **one** accounting behaviour where a producer has demonstrated a
> clean, complete, measured mechanism. **It is also the behaviour `om_data_remove` bypasses entirely**
> — deletion is not reversal, leaves no pair, and by design leaves no trace.

**Disposition: `UNRESOLVED — SPECIFIC P11 EVIDENCE UNAVAILABLE`** for the cross-process algebra.

---

## `CQ-P11-11` — Duplicate / replay / double counting

> ### The CORR2 headline, and it is a **reliance** finding, not a new defect
>
> `P01` `S16-B-05`, schema-verified with controls:
> **`stock_valuation_layer_account_move_id_fkey … ON DELETE SET NULL`.** Deleting journal entries
> **silently NULLs `account_move_id` on every valuation layer that referenced them** — *"reproducing
> exactly the '0 of N valuation layers linked' signature P01 published for the series-18 OCC deployment
> (**0 of 47,801**) and the series-19 estate (**0 of 14,441**)"*.
>
> **Neither finding is overturned.** *"What is new is that a competing explanation exists and was never
> excluded — the programme has read those zeros as 'never posted' when 'posted and later deleted' is
> **observationally identical**."*

**P11's own exposure, stated plainly:** P11's registers rest on zeros of exactly this shape —
`0 of 13,814` identity rows, `0 of 109` sealed journals, `0 of 89` companies with a period lock,
`P02`'s **zero COGS lines across 447,384**, and P11's own **0 subledgers of record**.
**`P11-B-26`: every P11 zero-shaped negative is downgraded pending exclusion of the deletion
explanation.** Not withdrawn — **downgraded**, because no evidence says the module fired.

Also received: cross-cost-centre displacement of **2,019,008.49 in each direction** inside entries that
net exactly zero — **double movement invisible to every aggregate**.

**Disposition: `UNRESOLVED — SPECIFIC P11 EVIDENCE UNAVAILABLE`.** Exclusion requires the query `P06`
named (`account_full_reconcile` rows with zero surviving parts) and is **`AUTHORIZATION REQUIRED`**
under `D-3b` v5. **P11 designs no idempotency mechanism** — routed to Phase B.

---

## `CQ-P11-12` — Period / cut-off / currency

**No accounting-period object exists** — a period is a date range on a company record (`P08`,
`A VERIFIED ABSENCE`, 7-observation limit). **0 of 6 transacting companies set a close.** **No lock
date on any of three locking surfaces** over **169,143 posted entries** (`P01`, enumerated *after*
challenge — the earlier phrasing had been tested against **one** surface). Balance assertions are
**reporting-currency only**.

**Disposition: `FACT VERIFIED — CLOSED FOR CURRENT P11 EVIDENCE`.** Consequence for `D-5`/`P10-D-02`
carried, not decided.

---

## `CQ-P11-13` — SaaS accounting scope

`PLATFORM` / `TENANT` / `COMPANY` applied per candidate truth in
`P11_ACCOUNTING_TRUTH_CONVERGENCE_MATRIX.md`. Live scope items: `P03` `SCOPE-02` — a company-scoped
financial effect on a record permitted to have **no company**, closing evidence returning **0 of 60** in
a fourth database; `P09` — cross-company mirroring keeps company-less shared axis values, so two
companies' records **partly cancel on one tenant-level object**.

**`MISSING REQUIRED SCOPE = DENY` holds. `OWNERSHIP ≠ AVAILABILITY` holds.**
**Disposition: `BOSS DECISION REQUIRED`** (`D-13`, `D-16`) · **P11 designs no isolation mechanism.**

---

## `CQ-P11-14` — Orphan / collision / unowned accounting truth

Full register: `P11_ACCOUNTING_ORPHAN_COLLISION_DOUBLE_COUNT_REGISTER.md`. **9 items.**

---

## `CQ-P11-15` — Candidate Input → Process → Output → Handoff

Full pack: `P11_CANDIDATE_ACCOUNTING_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md`.

---

## Disposition summary

| Disposition | CQs |
|---|---|
| `FACT VERIFIED — CLOSED FOR CURRENT P11 EVIDENCE` | `01`, `03`, `06`, `07`, `08`, `12` — **6** |
| `UNRESOLVED — SPECIFIC P11 EVIDENCE UNAVAILABLE` | `04`, `05`, `10`, `11` — **4** |
| `BOSS DECISION REQUIRED` | `02`, `13` — **2** |
| `EXTERNAL DOMAIN BOUNDARY — CANDIDATE HANDOFF RECORDED` | `09` — **1** |
| Carried to their own registers | `14`, `15` — **2** |

**`CP-P11C2-07` — COMPLETE — EVIDENCE VERIFIED. 15 of 15 dispositioned. 0 ambiguous.**
