# 68 — P05 CLOSURE QUESTION REGISTER V3

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05C-04`, `CP-P05C-05`
Terminal dispositions per prompt §17. **No vague OPEN/TBD.**

## 1. Material Deltas Declared and Executed in This Continuation

Only two additional evidence actions were taken. Both were declared before execution, both were
bounded to a named surface, both had a stop condition, and both stopped.

| MD | Affected CQ | Boundary | Why existing evidence insufficient | Result | Stopped? |
|---|---|---|---|---|---|
| **`MD-01`** | `CQ-P05-03`, `CQ-P05-09` | The single directory `scgl_signature_hr_expense` within the three **already-declared** source roots. No wider search. | The module is **installed on the v18 target** and extends the expense surface; it appears in no prior P05 analysis (`U-15`). | **NOT PRESENT in any of the three declared source roots.** Deployed at `18.0.1.0.0`; source unavailable within the declared path set. Class **B**. | **YES** — no wider search performed |
| **`MD-02`** | `CQ-P05-13` | `__manifest__.py` version key of six P05 modules vs `latest_version` in the registry already extracted. No new extraction. | `U-16` held that the analysed source might not be the deployed code; the version-basis hypothesis was untested. | **Five of five installed P05 modules match exactly.** One source copy (`scgl_purchase_advance_payment`) carries a **non-series version**. | **YES** |

**No whole-estate sweep, whole-volume search, CloudStorage sweep, backup enumeration or adjacent-Pxx
research was performed.** The prior round's exhaustive-search method is **not** repeated here; it is
explicitly forbidden by this prompt and the prohibition was honoured.

## 2. `MD-02` Result — version basis

| Module | Source manifest | Deployed (`idemo18_uat` v18) | Basis |
|---|---|---|---|
| `hr_expense` (core, ENT18) | `'2.0'` → `18.0.2.0` | `18.0.2.0` | **MATCH** |
| `hr_expense_petty_cash` | `18.0.1.2` | `18.0.1.2` | **MATCH** |
| `l10n_th_withholding_tax` | `18.0.1.4` | `18.0.1.4` | **MATCH** |
| `l10n_th_withholding_tax_cert` | `18.0.1.3` | `18.0.1.3` | **MATCH** |
| `account_payment_multi_deduction` | `18.0.1.0.2` | `18.0.1.0.2` | **MATCH** |
| `scgl_signature_hr_expense` | **absent from all three roots** | `18.0.1.0.0` installed | **NO SOURCE** |
| `scgl_purchase_advance_payment` | **`1.0.0`** — not an 18-series string | uninstalled on v18; `16.0.1.0.0` / `19.0.1.0.0` elsewhere | **NO GENERATION MATCH** |

> **`U-16` NARROWS but does not close.** The version-mismatch hypothesis is **refuted** for the five
> modules P05's own findings rest on. Per the standing project rule, **a matching manifest version
> string is not proof of identical code** — code identity remains class **D**. What is now established
> is that the **version basis is correct**, which is the precondition for reading that source at all.
>
> **New finding `VB-01`:** the `scgl_purchase_advance_payment` source read by P05 carries version
> `1.0.0`, matching **none** of the three deployed generations. The P01-routed findings therefore rest
> on a source copy of **unestablished generation**. This materially qualifies the P01 handoff and is
> recorded in `74`.

## 3. Closure Question Dispositions

| CQ | Question | Disposition | Basis |
|---|---|---|---|
| `CQ-P05-01` | What enters P05? | **FACT VERIFIED — CLOSED FOR CURRENT P05 EVIDENCE** | 7 candidate inputs, `69 §A`. Each has producer class, meaning, amount/currency, counterparty, date, scope, validation. Producer internals **not** researched. |
| `CQ-P05-02` | Expense classification boundary | **FACT VERIFIED — CLOSED**, with one class routed out | Three P05-decidable classes (immediate operating, employee claim, vendor payable) + advance cases. **Prepaid/period-spanning is NOT P05-decidable** → `EXTERNAL DOMAIN BOUNDARY` `CH-09`. |
| `CQ-P05-03` | P05 recognition and liability point | **FACT VERIFIED — CLOSED** | Recognition is triggered by the **approval transition**, elevated, before posting; document state is *derived from* the entries. Operational approval ≠ accounting recognition ≠ settlement readiness — three distinct states, evidenced. `70`. |
| `CQ-P05-04` | Employee vs vendor payable semantics | **FACT VERIFIED — CLOSED** | Both resolve to the **same** payable account; the distinction is carried **only by counterparty identity**. Advance cases evidenced. `69 §B`, `71`. |
| `CQ-P05-05` | Analytic attribution at the P05 boundary | **FACT VERIFIED — CLOSED** | P05 can carry attribution on the **expense debit line only**; not on tax or payable lines; absent from the advance/float chain. P05 stops at publishing it. `CH-02`. |
| `CQ-P05-06` | Tax/WHT interface boundary | **FACT VERIFIED — CLOSED for the P05 side** | P05 carries WHT attributes and emits a withheld amount at settlement. **Statutory ownership is P07's**; nine questions routed, zero assertions. `CH-04`. |
| `CQ-P05-07` | Settlement-ready payable output | **FACT VERIFIED — CLOSED** | Seven-element output contract candidate, `72`. |
| `CQ-P05-08` | Accounting event output boundary | **FACT VERIFIED — CLOSED** | P05 produces an accounting-relevant event; ledger integrity and period architecture are P08's. `73`. |
| `CQ-P05-09` | Correction / reversal / cancellation | **FACT VERIFIED — CLOSED, with a named defect** | Three distinct cancel semantics; reversal severs the claim↔entry link; **no correction event is published**. `74`. |
| `CQ-P05-10` | Scope / company / SaaS boundary | **FACT VERIFIED — CLOSED** | Per-object scope derived, not blanket-enforced. `75`. |
| `CQ-P05-11` | Evidence blockers and obtainable closure | **AUTHORIZATION REQUIRED — EXACT EVIDENCE ACTION NAMED** | `76`. Three authorization items, each with an exact action and owner. |
| `CQ-P05-12` | Candidate I/P/O/Handoff model | **FACT VERIFIED — CLOSED** | `69` — 7 inputs, 6 outputs, 9 handoffs, 4 orphans. |
| `CQ-P05-13` | Evidence integrity / terminality | **FACT VERIFIED — CLOSED**, with `U-16` narrowed | This file §1–§2; `77`. |

**11 of 13 closed on current evidence. 1 authorization-required. 1 closed-with-narrowing.**

## 4. Items Re-Labelled `EXTERNAL DOMAIN BOUNDARY` (`DPC-01`)

These were carried inside P05's own registers by earlier rounds. They remain in the lineage as
evidence; they are **no longer counted as P05-owned closure items**.

| Item | Was | Now | Owner |
|---|---|---|---|
| `TZ-08` hashed entry force-cancellable | P05 tolerance-zero | **EXTERNAL DOMAIN BOUNDARY** — core ledger integrity | **P08** |
| `TZ-11b` payroll double-payment path | P05 tolerance-zero | **EXTERNAL DOMAIN BOUNDARY** | HR/Payroll + P08 |
| `E1-15` `sale_expense` reinvoicing domain | P05 finding | **EXTERNAL DOMAIN BOUNDARY** | **P02** |
| `TX-24` disallowed-expense mechanics | P05 finding | **EXTERNAL DOMAIN BOUNDARY**; only "no GL write path" retained | **P07** |
| `TZ-11a`, `TZ-12` vendor down payment / `sudo()` billing | P05 tolerance-zero | **EXTERNAL DOMAIN BOUNDARY** — evidence retained, routed | **P01** |

> **Consequence for the tolerance-zero population:** of the 13 items in `58`, **five are not P05's to
> close**. P05's own tolerance-zero population is **8**. This is a *narrowing by domain purity*, not a
> closure — none of the five is resolved, and each remains open with its owner named. Recorded so that
> P05's register stops implying it can close another process's boundary.

## 5. What This Continuation Did NOT Do

No reset · no restart at L1 · no whole-estate or whole-volume search · no CloudStorage sweep · no
backup enumeration · no adjacent-Pxx research · no P04/P10 dependency · no PHASE B · no AI EOS · no
SMEsPlus function design · no mutation of any source, database, module or container · no merge.
