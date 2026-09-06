# P11 — CANDIDATE ACCOUNTING INPUT → PROCESS → OUTPUT → HANDOFF PACK

`[SMEPLUS-26-09-06-…-CORR2-PHASES-001]` · `CP-P11C2-09` · **PHASE S — DOMAIN PURITY FIRST** · AI EOS **NOT ACTIVE**

> ## Everything in this pack is a **CANDIDATE**.
> Not a contract. Not an architecture. Not a design. Not frozen. **Phase B has not started, Phase C has
> not started, Functional Design is not authorised, and no Producer/Consumer contract is established.**

---

# A. CANDIDATE INPUTS — `12`

Published accounting-facing facts from `P01`–`P10`, at the frozen SHAs in
`P11_CORR2_PEER_CLAIM_SNAPSHOT.md`. Each is **received and attributed**; none is re-derived by P11.

| # | Candidate input | Producer @ SHA |
|---|---|---|
| `CI-01` | Posted monetary fact at item granularity — **0 unbalanced / 169,143**, reporting currency only | `P08` @ `194efcb` |
| `CI-02` | Settlement graph — **63,773 records / 100,580 lines**, residual drift **0** | `P08` |
| `CI-03` | Company + journal attribution — **447,384 of 447,384** | `P08` |
| `CI-04` | Posting state and date on every entry; origin pointer on **96.1 %** | `P08` |
| `CI-05` | GRNI position — **13,666 posted items / −฿7,048,692.08**, `reconcile='f'` | `P01` @ `b820b29` |
| `CI-06` | Correction as **immutable reversal** — 5,115 pairs, 0 unresolvable | `P01` |
| `CI-07` | Price-difference disposition — **1,175 of 1,267 never reach the GL** | `P01` |
| `CI-08` | Valuation gate — one setting, **126 of 126 categories**, five consequences | `P01` |
| `CI-09` | Manufacturing cost position — conversion cost **0**; **30 records ±1.5 × 10²¹**, **−48.7 %** | `P03` @ `bc767a8` |
| `CI-10` | Expense position — petty cash **634 of 993**; WHT **332 certificates**, 40 codes | `P05` @ `205e0ac` |
| `CI-11` | Analytic position — **12 of 23** centres net exactly 0.00; gross **43×** net | `P09` @ `5441f8d` |
| `CI-12` | Destructive-path position — `om_data_remove` **installed**, unauthorised, reachable; FK **`ON DELETE SET NULL`** | `P06` @ `249b7c2` · `P01` |

---

# B. P11 PROCESS SEMANTIC CORE — candidate

| Element | Candidate position | Status |
|---|---|---|
| **Accounting Event Identity** | Required; **absent as a platform property**; exists on one channel, nullable, **unpopulated on 13,814 of 13,814**. **Eight** processes depend on it | `BOSS DECISION REQUIRED — D-5`. Evidence class **`C`** |
| **Accounting Owner** | Distinct from business-process owner. A GL consequence **does not** transfer lifecycle ownership to P11 (`P11-G-06`) | `SUPPORTED INTERPRETATION — P11` |
| **Financial Meaning** | Established per row in `P11_ACCOUNTING_TRUTH_CONVERGENCE_MATRIX.md` §2 | `FACT VERIFIED` where marked |
| **Accounting Timing** | **Four distinct times** — occurrence, recognition, posting, settlement. The estate reliably carries **one** | `UNRESOLVED` — gated on `D-5`, `P10-D-02` |
| **Subledger → GL** | For the party dimension, agreement is **true by construction and unverifiable**. Where separate stores exist, **no kernel tie-out** | `FACT VERIFIED` (`P11-C-12`) |
| **Debit/Credit + Account Role** | **30 producer cells WITHHELD.** Convention demonstrated wrong in both halves | `UNRESOLVED — SPECIFIC P11 EVIDENCE UNAVAILABLE` |
| **Scope** | `PLATFORM` / `TENANT` / `COMPANY` per row. `MISSING REQUIRED SCOPE = DENY`; `OWNERSHIP ≠ AVAILABILITY` | `SUPPORTED INTERPRETATION — P11` |
| **Correction / Reversal** | Immutable reversal is measured clean; **the deletion path bypasses it and leaves no trace by design** | `FACT VERIFIED` + `UNRESOLVED` |
| **Period / Cut-off** | **No accounting-period object.** 0 of 6 companies close; no lock date on 3 surfaces / 169,143 entries | `FACT VERIFIED` |
| **Currency / Amount** | Balance assertion is **reporting-currency only**; two rounding currencies observed | `FACT VERIFIED` |
| **Analytic / Tax / Settlement boundary** | Analytic: reconcile on **gross per centre**, never a net. Tax: two WHT subsystems co-installed. Settlement: chronology untrustworthy | `EXTERNAL DOMAIN BOUNDARY` |

---

# C. CANDIDATE OUTPUTS

## C.1 Reconciled accounting truth candidates — `6` converged, `17` single-owner
See `P11_ACCOUNTING_TRUTH_CONVERGENCE_MATRIX.md`.

## C.2 Contradictions — `3` live
`OC-06` series-16 source · `OC-07` decision-id namespace *(corrected)* · `P11-C-11` T0-13 over-adoption *(corrected at both ends)*.

## C.3 Unresolved evidence items — `4`
`CQ-04` timing · `CQ-05` debit/credit cells · `CQ-10` correction algebra · `CQ-11` deletion exclusion.

## C.4 Boss decisions — `18`, a declared **floor**, `0` decided by P11
See `P11_BOSS_DECISION_MATRIX_CORR2.md`.

## C.5 Orphan / collision / double-count candidates — `10`
See `P11_ACCOUNTING_ORPHAN_COLLISION_DOUBLE_COUNT_REGISTER.md`.

## C.6 Candidate accounting controls — for **later** Phase-B/Design review only

| # | Candidate control | Motivating evidence |
|---|---|---|
| `CC-01` | A periodic tie-out obligation between each genuinely separate store and the ledger, with a **named exception outcome** | `P08-RQ-KRN-01`; `OC-01`/`OC-02` |
| `CC-02` | A settlement event carrying **identity + date + reversal link** as one requirement | `P11-C-09` |
| `CC-03` | Management attribution reconciled on **gross movement per cost centre**, never a scalar net | `OC-08` |
| `CC-04` | Deletion of posted financial history distinguished from correction, and **server-side authorised** | `CI-12`; `T0-14` |
| `CC-05` | An accounting-period object distinct from a date range on a company | `CQ-12` |

> **These are candidates for review, not requirements, not designs, and not adopted.** P11 selects no
> mechanism, technology, schema or API for any of them.

---

# D. CANDIDATE HANDOFFS — minimal interface facts only

| To | Item | Exact ask |
|---|---|---|
| **`P01` / `P03` / `P04`** | `OC-06` | Settle whether a series-16 source tree exists on this host. **Two published statements are mutually exclusive; a hold carried by two processes may already be discharged.** P11 opens no tree |
| **`P06`** | `OC-10` | Execute the orphan-signature query `P06` itself specified, to convert *"installed"* into *"fired, and here is the damage"* |
| **`P05`** | `RE-20` | Confirm which prior P05 negatives post-date `41`, so P11 can restore them from class B |
| **`P08`** | `CQ-06` | The five questions `P08` routes to P11 are **carried unanswered**; P11 confirms receipt and asserts no preferred option |
| **`P10`** | `P11-C-11` | Correction acknowledged at both ends; `T0-13` remains `HOLD — BOSS DECISION REQUIRED` and **is not adopted** |
| **`P09`** | `OC-08` | P11 adopts the gross-not-net rule and applies it to its own registers |
| **Phase B** | `CQ-11` | Duplicate/replay/idempotency requirements — **routed, not designed** |
| **Phase B** | `P08` q5 | *How two Pxx truth sets are compared at all* — `EXTERNAL DOMAIN BOUNDARY` |
| **Phase C** | — | Nothing. Phase C follows Phase B and is not addressed |
| **Boss** | 18 decisions | `P11_BOSS_DECISION_MATRIX_CORR2.md` |

---

# E. Attestation

**Labels used:** `FACT VERIFIED — P11 ACCOUNTING BOUNDARY` · `SUPPORTED INTERPRETATION — P11` ·
`CANDIDATE INPUT` · `CANDIDATE ACCOUNTING TRUTH` · `CANDIDATE OUTPUT` · `CANDIDATE HANDOFF` ·
`CONTRADICTED — CORRECTED` · `UNRESOLVED — SPECIFIC EVIDENCE REQUIRED` · `AUTHORIZATION REQUIRED` ·
`BOSS DECISION REQUIRED` · `EXTERNAL DOMAIN BOUNDARY — DO NOT RESEARCH HERE` ·
`POST-SNAPSHOT MATERIAL DELTA CANDIDATE`.

**Forbidden labels used: `0`.** No `FINAL CONTRACT`, `FINAL ERP TRUTH`, `FINAL ARCHITECTURE`,
`DESIGN FROZEN`.

**`CP-P11C2-09` — COMPLETE — EVIDENCE VERIFIED.**

---

# CORR3 RE-DERIVATION — `2026-09-06` · `CP-P11C3-08`

> Re-derived **after** validated intake and falsification. **Statuses remain `CANDIDATE`.**
> **No Phase-B Producer↔Consumer contract validation is performed.**

## F.1 Candidate inputs — corrected

| # | Change |
|---|---|
| `CI-01` | *"complete and arithmetically sound"* → **arithmetically sound at tolerance ≥ 0.005; at 1e-7 the count is 3.** *"Complete"* **withdrawn by the owner** |
| `CI-02` | settlement graph → **no longer offered as reconcilable.** `HO-13`: deletable outside the object layer |
| `CI-03` | 447,384 → **all-states population; the posted population is 417,700** |
| `CI-04` | origin pointers **96.1 % → 78.03 %** structured |
| `CI-12` | deletion path → **installed in all three deployed databases**, two generations |
| **`CI-13`** *(new)* | **`HO-13`** — the raw-SQL deletion order and the **entry-number sequence reset to 1** |
| **`CI-14`** *(new)* | **`HO-14`** — the statutory register family selects on **two different period bases**, so **5,228** entries can appear in one register and not the other |
| **`CI-15`** *(new)* | **`P02` `43_` §5** — three scope holds, six design candidates, and the invariant failing **at correction/reversal** |

## F.2 Process semantic core — corrected

| Element | Change |
|---|---|
| **Accounting timing** | **weakened** — the settlement-chronology finding is **withdrawn as containing no defect**. What survives: recognition collapsed into posting, and `฿29.0m` received with no recognition |
| **Subledger → GL** | **downgraded** to `SUPPORTED INTERPRETATION — 18.0 SOURCE LINE`, under `AAS+-VETO-01` |
| **Period / cut-off** | **re-scoped to the 18.0 root set.** A dated recurring return object exists on the 19.0 line |
| **Correction / reversal** | **the invariant's named failure point** (`P11-C-15`), and `HO-13` bypasses correction entirely |
| **Duplicate risk** | **new** — a sequence reset permits re-issue of previously-issued entry numbers |

## F.3 Candidate handoffs — with delivery status, which is the point

| To | Item | Exact ask | **Written** | **Delivered/received** |
|---|---|---|---|---|
| `P08` | `IC-01` `฿29,029,467.66` | judge the completeness question at a reporting date; `P01` routes it to you | ✔ | **unevidenced** |
| `P06` + `P08` | `HO-13` | whether the deletion path has **executed** on any deployment — the `exercised` rung | ✔ | **unevidenced** |
| `P07` | `HO-14` | the two period bases and the 5,228 divergent entries | ✔ (by `P08`) | **unevidenced** |
| `P01`/`P03`/`P04` | `OC-06` | closed by `P02` `C-86`; confirm discharge | ✔ | **unevidenced** |
| `P09` | `OC-08` | gross-not-net adopted by P11 | ✔ | **unevidenced** |
| Boss | 19 decisions, `D-1` first | packaged, not written | ✔ | n/a |
| Phase B | idempotency; `P08` q5 | routed, not designed | ✔ | n/a |

> **Every row's delivery status is `unevidenced`. That is `P11-B-31`, and it is the honest state of the
> programme's handoff layer — not a P11 omission and not any single peer's.**
