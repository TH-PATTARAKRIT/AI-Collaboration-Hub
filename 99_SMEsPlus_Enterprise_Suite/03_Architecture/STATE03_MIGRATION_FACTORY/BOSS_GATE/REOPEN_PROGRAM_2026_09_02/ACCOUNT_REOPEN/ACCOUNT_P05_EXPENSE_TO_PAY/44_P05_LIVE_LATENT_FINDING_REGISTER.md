# 44 — P05 LIVE / LATENT FINDING REGISTER

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E04`
Every material finding classified on the five-axis test the directive requires.
**Reference platform for "deployed" = `idemo18_uat` (Odoo 18.0), the target version.**

Exposure classes: `LIVE — OBSERVED` · `LIVE — CONFIGURED/REACHABLE` · `LATENT — SOURCE ONLY` ·
`LATENT — MODULE NOT INSTALLED` · `LATENT — REQUIRED DATA ABSENT` · `UNREACHABLE IN VERIFIED
DEPLOYMENT` · `VERSION-DEPENDENT` · `CONTRADICTED` · `UNKNOWN`.

| ID | Finding | Source defect | Module installed (v18)? | Reachable? | Data observed? | Effect observed? | **Exposure class** |
|---|---|---|---|---|---|---|---|
| `TX-01` | Two WHT subsystems; custom line has no `tax_line_id`, CSV inner-joins on it | verified | **yes** | yes | **358 lines** | **100.00% divergence** | **LIVE — OBSERVED** |
| `PC-01` | **238 of 625 petty-cash sheets have no linked entry; 206 are `done`** | — | **yes** | yes | **yes** | **yes** | **LIVE — OBSERVED** |
| `TZ-01` | *"Petty cash never credits the petty cash account"* | source-copy verified | **yes** | yes | **386/387 credits DO land on the petty cash account** | **contrary** | **CONTRADICTED** |
| `TZ-02` | `petty.cash` has no company scoping | verified | yes | yes | 4 companies present | **no cross-company posting observed** | **LATENT — REQUIRED DATA ABSENT** |
| `TZ-03` | Expense amount/currency/date writable after posting | verified | yes | yes | 993 expenses | not tested | **LIVE — CONFIGURED/REACHABLE** |
| `TZ-04` | Payment immutability guard omits `journal_id`/`ref` | verified (AST) | yes | yes | — | not tested | **LIVE — CONFIGURED/REACHABLE** |
| `TZ-09` | Approval enforced in action, not on field | verified | yes | yes | 979 sheets | not tested | **LIVE — CONFIGURED/REACHABLE** |
| `TZ-10` | Sheet reaches `done`/"Paid" with no entry (`sample`) | verified | **`hr_expense_extract` INSTALLED on v18** | yes | not isolated | — | **LIVE — CONFIGURED/REACHABLE** |
| `TZ-11a` | Vendor down payment never deducted | verified | **no on v18**; yes in 4 registries | yes there | 21 wizard rows (`iSMEs`) | **not observed** | **LIVE — CONFIGURED/REACHABLE** (not on target) |
| `TZ-11b` | Payroll double-payment path | verified | `hr_payroll_expense` **uninstalled** on v18 | no | — | — | **LATENT — MODULE NOT INSTALLED** |
| `TZ-12` | `sudo()` vendor-bill creation | verified | **no on v18**; yes in 4 | partial | — | — | **LIVE — CONFIGURED/REACHABLE**, `PARTIAL AUTHORIZATION` |
| `TZ-05`,`TZ-07`,`TZ-13` | Advance state-write, clearing collapse, fabricated bank receipt | verified | **no** — installed nowhere | no | table absent | — | **LATENT — MODULE NOT INSTALLED** |
| `TZ-08` | Hashed entry force-cancellable | verified (core) | core, always present | yes via other paths | not tested | — | **LIVE — CONFIGURED/REACHABLE** (P08 owns) |
| `TZ-06` / `DUP-03`,`DUP-05` | Cross-document duplicates involving advance/petty | verified | advance: no | no | — | — | **LATENT** |
| `DUP-04` | Claim vs vendor bill duplicate undetected | verified | yes | yes | not tested | — | **LIVE — CONFIGURED/REACHABLE** |
| `DUP-09` | Duplicate WHT certificate | verified + **1 instance in 5,201** | yes | yes | **yes (v16)** | **1 exact duplicate** | **LIVE — OBSERVED** (v16) |
| `TX-03`,`TX-04` | WHT latch drops/misposts withholding | verified | yes | yes | not isolated | — | **LIVE — CONFIGURED/REACHABLE** |
| `TX-05` | `_multi` breaks single-WHT | verified | `_multi` **uninstalled everywhere** | no | — | — | **LATENT — MODULE NOT INSTALLED** |
| `TX-06` | Multi-deduction UI-only | verified | **`account_payment_multi_deduction` INSTALLED on v18** | yes | **0 deduction rows** | — | **LATENT — REQUIRED DATA ABSENT** |
| `TX-10` | Receipt move types inverted | verified | yes | yes | **0 receipt moves** | — | **LATENT — REQUIRED DATA ABSENT** |
| `TX-13` | Certificate duplication control absent | verified (`DB-01`) | yes | yes | **332 certs (v18), 5,201 (v16)** | **1 duplicate** | **LIVE — OBSERVED** |
| `TX-20` | `payment_date` is a create-time artefact | verified | yes | yes | **100% of 5,201 (v16)** | yes | **LIVE — OBSERVED** (v16) |
| `TX-24` | No non-deductible treatment | verified | **`account_disallowed_expenses` INSTALLED on v18** | report-only | not extracted | — | **VERSION/CONFIG-DEPENDENT — re-open, class `C`** |
| `SR-07` | Claim↔entry link severable | verified | yes | yes | **`PC-01` measures it** | **yes** | **LIVE — OBSERVED** |
| `R-01'` | Late `check_company` on `vendor_id` | verified | yes | yes | not tested | — | **LIVE — CONFIGURED/REACHABLE** |

## 2. Summary

| Class | Count |
|---|---|
| **LIVE — OBSERVED** | **5** (`TX-01`, `PC-01`, `DUP-09`, `TX-13`, `TX-20`, `SR-07` — `TX-13`/`DUP-09` are one instance) |
| **LIVE — CONFIGURED/REACHABLE** | 9 |
| **LATENT — MODULE NOT INSTALLED** | 5 |
| **LATENT — REQUIRED DATA ABSENT** | 3 |
| **CONTRADICTED** | **1 — `TZ-01`** |
| Re-opened as version/config-dependent | 1 — `TX-24` |

## 3. What Changed Against Round 2

Round 2's reach classification rested on a population that **excluded the target platform**. With
`idemo18_uat` included:

- `TZ-01` moves from `LATENT` to **`CONTRADICTED`** — the opposite of both prior positions.
- `PC-01` is **new** and is the strongest petty-cash finding yet.
- `TZ-10`, `TX-06`, `TX-24` move from `LATENT` toward **live or re-opened**, because
  `hr_expense_extract`, `account_payment_multi_deduction` and `account_disallowed_expenses` are all
  **installed on v18** and Round 2 had them as uninstalled or absent.
- `TZ-11a`/`TZ-12` move from *"live in all four"* to **live in four registries but not the target**.
- The employee-advance cluster is **confirmed** latent — strengthened, not weakened.
