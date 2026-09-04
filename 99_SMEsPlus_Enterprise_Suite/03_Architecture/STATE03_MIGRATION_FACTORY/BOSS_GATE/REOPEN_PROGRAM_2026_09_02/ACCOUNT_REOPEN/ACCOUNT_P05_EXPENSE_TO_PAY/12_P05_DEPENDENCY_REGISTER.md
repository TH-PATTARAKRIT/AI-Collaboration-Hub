# 12 — P05 DEPENDENCY REGISTER

`LAYER 2 — AUDIT QUARANTINE`

## 1. Inbound Dependencies — P05 cannot be settled without these

| ID | Dependency | Owner | Status | Blocks |
|---|---|---|---|---|
| `D-01` | **Installed module set of the deployed system.** Three near-identical copies of the custom addon set exist at differing version strings; which is deployed is not determinable from any source tree. | Boss / Infrastructure | **OPEN — GATING** | Every claim about the *as-operated* system. Claims about the *as-written* source are unaffected. |
| `D-02` | **`GB-08` Boss ruling — FX rate ownership and missing-rate policy** (`ACCOUNT_REOPEN/ACCOUNT_FULL_DEEP_RESEARCH/GB08_BOSS_RULING_FX_RATE_OWNERSHIP_AND_MISSING_RATE_POLICY_2026_09_04.md`). | Boss — **already ruled** | **BINDING ON P05** | `EC-02` (multi-currency), `GL-06` (clearing lines carry no currency), and the user-implied rate at `hr_expense.py:270`. P05 must conform, not re-decide. |
| `D-03` | **Account Wave A event-identity conclusion.** P05's `SR-07` independently reaches the same conclusion for the expense surface. | Core Ledger track | **CONVERGENT — OPEN** | `SR-07`; any claim/entry reconciliation key |
| `D-04` | **Boss decision on clock-derived accounting dates** (`BD-03`). Wave A raised it for the core ledger; P05 finds three further instances (`03 §3.1`, `RI-06`, `E1-13`). | Boss | **OPEN** | `AE-01`, `AE-05`, `EC-12` |
| `D-05` | **Thai statutory basis for WHT rates, forms and certificate content.** No authoritative source is in this session's evidence set. | Accounting-Tax track | **HOLD / EVIDENCE REQUIRED** | Every statutory assertion in `07`; `SC-01`'s statutory half |
| `D-06` | **Scope determination `SO-01`** — is `hr.employee` tenant-scoped with company-specific contracts, or one record per company? | P11 / Architecture | **HOLD — SCOPE EVIDENCE REQUIRED** | `22 §3 R-04`; `E1-08` company scoping of employee lookup |
| `D-07` | **Scope determination `SO-03`** — do unrelated independent companies in the deployment share a tenant? Per `CORR1`, unrelated independent companies are separate tenants by default. | P11 / Architecture | **HOLD — SCOPE EVIDENCE REQUIRED** | `TZ-02` blast radius |
| `D-08` | **Runtime / database evidence for P05.** None exists; an Asset-domain dump exists but has no P05 equivalent. | Evidence acquisition | **OPEN — GATING for `EC-02`** | Every `SUPPORTED INTERPRETATION` in this package |

## 2. Outbound Dependencies — what P05 owes other processes

| ID | Consumer | What P05 supplies | Status |
|---|---|---|---|
| `D-09` | **P11 — cross-process scope reconciliation** | Four scope contributions: `R-01` (reference scope ≠ financial scope, so tenant-scoped partner references must not be company-constrained), `R-02` (an object whose balance is a company's GL position is company-scoped by derivation), `R-03` (`SC-01` — statutory tax reference must be platform-scoped, not duplicated per company), `R-04` (an operation must determine its executing scope *before* resolving its authoriser) | **DELIVERED** in `22` |
| `D-10` | **P01 — Procure-to-Pay** | Ownership boundary: P01 must state whether it owns vendor advances (`scgl_purchase_advance_payment`), and whether an expense line naming a `vendor_id` may reach vendor-facing accounts without a purchase document. Two high-severity defects in that module are reported here because they were found in P05's trace (`E3-12`, `E3-13`). | **PEER DEPENDENCY OPEN** |
| `D-11` | **P08/P09 — cash & treasury** | Petty cash float ownership; `TZ-01`, `TZ-02`, `E3-05` | **PEER DEPENDENCY OPEN** |
| `D-12` | **P10 — controlling** | Analytic handoff contract and its three gaps (`06 §4`) | **DELIVERED, CONDITIONAL** |
| `D-13` | **Core Accounting Reconciliation** | `19_P05_CORE_RECON_HANDOFF_PACK.md` | See `19` |

## 3. Peer Session Status

Per `CORR1 §7`, P05 does **not** stop for peers.

| Peer | Branch | State at time of writing |
|---|---|---|
| P01 Procure-to-Pay | `research/account-p01-procure-to-pay-2026-09-04-001` | at base `88f52cd`, no committed output |
| P02 Order-to-Cash | `research/account-p02-order-to-cash-2026-09-04-001` | at base `88f52cd`, no committed output |
| P03 Manufacture-to-Cost | `research/account-p03-manufacture-to-cost-2026-09-04-001` | at base `88f52cd`, no committed output |
| P04, P06–P11 | not found among remote branches | not started, or not yet pushed |

`PEER DEPENDENCY OPEN` recorded for `D-10`, `D-11`. All unaffected P05 work has continued.

## 4. Dependency Impact on the Exit Criteria

| Criterion | Blocked by |
|---|---|
| `EC-01` Scope Bounded | `D-01` — the module population of the *deployed* system is `UNBOUNDED / NOT YET ENUMERABLE` |
| `EC-02` Enumeration Converged | `D-08` — no runtime evidence; and `EC-07` has not been attempted |
| `EC-03` Unknown Exhausted | `D-01`, `D-05`, `D-06`, `D-07` |
| `EC-04` Tolerance-Zero Closed | thirteen boundaries open (`10 §3`) |
| `EC-05` Contradiction Resolution | see `11` |
| `EC-06` Negative Claim Controlled | see `21` |
| `EC-07` Two Consecutive Clean Passes | **not started** — this is the first pass, and it produced new material findings from every reviewer that has reported |
| `EC-08` Final Knowledge Package | this package, incomplete while the above stand |
