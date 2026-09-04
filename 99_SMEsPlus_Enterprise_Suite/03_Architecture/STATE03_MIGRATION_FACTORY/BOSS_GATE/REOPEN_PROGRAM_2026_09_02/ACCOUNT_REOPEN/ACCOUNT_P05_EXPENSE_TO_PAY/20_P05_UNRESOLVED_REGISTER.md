# 20 — P05 UNRESOLVED REGISTER

`LAYER 2 — AUDIT QUARANTINE`
Per `EC-03`, every material unknown carries a final disposition from the permitted set:
`CLOSED` · `NON-GATING` · `ROUTED TO LATER WAVE/STATE` · `OUT OF SCOPE WITH EVIDENCE` ·
`BOSS DECISION REQUIRED`. **No unclassified `GATING UNKNOWN` may remain when advancing.**
A later-wave route may not be used to hide a blocker belonging to the current scope.

## 1. Register

| ID | Unknown | Why it matters | Disposition | Gating? |
|---|---|---|---|---|
| `U-01` | **Which modules are actually installed in the deployed system.** Three copies of the custom addon set exist at differing version strings; this session read one. | Every custom-module finding — petty cash, advance, WHT — is conditional on installation. Conversely, `E1-02` (sample) and `E1-03` (payroll double payment) are conditional on optional core modules. | `BOSS DECISION REQUIRED` — supply the deployed module list, or authorise a runtime enumeration | **YES** |
| `U-02` | **No runtime or database evidence exists for P05.** Every behavioural claim is derived from source reading. | `EC-02` convergence cannot be demonstrated on source alone for the claims marked `SUPPORTED INTERPRETATION`. | `BOSS DECISION REQUIRED` — authorise a P05 runtime trace equivalent to the Asset-domain dump | **YES** |
| `U-03` | **Exact `payment_state` and residual outcome of a bill force-cancelled by a raw `state` write, and of a cross-currency clearing reconciliation.** Expert 3 declined to assert it, classing it **D — UNKNOWN**, rather than infer it. | Determines the true blast radius of `TZ-08` and `TZ-07`. | `ROUTED` — requires runtime (`U-02`) | **YES**, for `TZ-07`/`TZ-08` closure only |
| `U-04` | ~~`account_disallowed_expenses` mechanism and its linkage to `hr_expense`.~~ | — | **CLOSED** by AAS-03 Expert 4: report-only, no GL write path (class **A**), no connection to `hr_expense` (class **A**). See `07 §6`. The *derived* requirement — whether a Thai add-back obligation needs more than a report — is `HOLD / EVIDENCE REQUIRED` and rolls into `U-09`. | NO |
| `U-05` | **`sale_expense` re-invoicing chain not traced.** Class **C — NOT YET SEARCHED** for its accounting effect; Expert 1 did report two defects in it incidentally (`E1-15`). | Re-invoiced expense crosses into P02. | `ROUTED TO LATER WAVE/STATE` — P02 boundary | NO |
| `U-06` | **`multi_level_approval` linkage.** The module exists in the custom set but no dependency links it to `hr.expense` or `advance.expense.request`. | If approval chains are expected, the reference supplies none for P05. | `NON-GATING` for the source finding; `BOSS DECISION REQUIRED` for the SMEsPlus requirement | NO |
| `U-07` | **`hr_expense_extract`, `hr_expense_predict_product`, `documents_hr_expense` install status.** | `E1-02` (`TZ-10`) is conditional on the first. | subsumed by `U-01` | via `U-01` |
| `U-08` | **Scope determinations `SO-01`..`SO-04`** (`22 §4`). | Four architecture decisions depend on them. | `HOLD — SCOPE EVIDENCE REQUIRED`, per `CORR1 §8`; unaffected work continued | `SO-01`, `SO-03` YES |
| `U-09` | **Thai statutory basis** for WHT rates, forms, certificate content and the deductibility rules behind `EC-04`. | Statutory assertions require an authoritative source; none is in this session's evidence set. | `HOLD / EVIDENCE REQUIRED` — routed to the Accounting-Tax track | YES, for `07`'s statutory claims only |
| `U-10` | **Whether `is_editable`-gated view attributes have any model-level equivalent anywhere outside the six modules Expert 1 searched.** Class **B** beyond that boundary. | Determines whether `TZ-03` is a design choice or an omission. | `ROUTED` — one further enumeration pass | NO |
| `U-11` | **`addons_archive` (959 modules) was not searched** by Expert 1 for compensating guards. Every one of that expert's negative claims is therefore class **C** as a statement about the whole installation. | Bounds the confidence of eight negative claims. | `ROUTED TO LATER WAVE` — with the boundary declared, per `DR-NC` rules | NO |

## 2. Gating Summary

| Gating unknown | Blocks |
|---|---|
| `U-01` | `EC-01`, `EC-03` |
| `U-02` | `EC-02`, and closure of `U-03` |
| `U-03` | `EC-04` closure of `TZ-07`, `TZ-08` |
| `U-08` (`SO-01`, `SO-03`) | `EC-03` |
| `U-09` | `EC-03` for `07`'s statutory rows only |

**Five gating unknowns remain.** Per `EC-03` none of them is routed to a later wave in order to hide
it: each is stated with the specific evidence that would close it, and each belongs to the current
scope. This is the primary reason the terminal state of this session is a HOLD (`19 §9`).
