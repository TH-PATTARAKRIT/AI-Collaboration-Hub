# 42 — P05 MULTI-DATABASE POPULATION PROOF

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E02` — **PARTIAL — RESUMABLE**

## 1. Population

Nine distinct database identities (`41 §3`). Seven readable in substance; two are zero-byte cloud
placeholders (`UNREADABLE — CLOUD PLACEHOLDER`, class **D**, not treated as absence).

| Database | Version | Companies | `hr_expense` | `hr_expense_sheet` | `petty_cash` | `advance_expense_request` | `purchase_advance_payment_bill` | `account_withholding_tax` | `withholding_tax_cert` | `account_move` | `account_move_line` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **`idemo18_uat`** | **18.0** | **4** | **993** | **979** | **8** | table absent | table absent | **40** | **332** | **15,522** | **40,353** |
| `iSMEs` | 16.0 | 1 | 2 | 0 | table absent | table absent | **21** | 7 | **5,201** | 183,590 | 447,384 |
| `iEVING` | 19.0 | — | 0 | 0 | absent | absent | 0 | 4 | 0 | — | — |
| `BK12MAY26` | 19.0 | — | 0 | 0 | absent | absent | 0 | 4 | 1 | — | — |
| `iTEST02` | 19.0 | — | — | — | absent | absent | 0 | — | 0 | — | — |
| `occ_sim` | 18.0 | — | n/a (`hr_expense` uninstalled) | — | absent | absent | absent | absent | absent | — | — |
| `pankhamhom` | **NOT READ** | — | — | — | — | — | — | — | — | — | — |

## 2. Where the P05 Evidence Actually Is

Two databases carry the whole evidential weight, and they carry **different halves**:

| | `idemo18_uat` v18 | `iSMEs` v16 |
|---|---|---|
| Expense/petty-cash operational evidence | **993 expenses, 979 sheets, 8 holders, 4 companies** | 2 expenses, 0 sheets |
| WHT certificate operational evidence | 332 certificates | **5,201 certificates, 6,159 lines** |
| Vendor advance usage | module uninstalled | **21 wizard rows** |
| Journal population | 15,522 / 40,353 | 183,590 / 447,384 |

> **This is why the population matters.** Round 2 measured the certificate findings on `iSMEs` and had
> **no expense data at all** (2 rows, 0 sheets). It then reclassified the petty-cash and advance
> findings on a population that contained no petty cash and no expense claims. `idemo18_uat` is where
> the expense evidence lives, and it was not in that population.

## 3. Evidence Boundary

| Statement | Class |
|---|---|
| These row counts for the six read databases | **A** — extracted, counted, reproducible |
| `pankhamhom` contains no P05 evidence | **C — NOT YET SEARCHED.** Explicitly not claimed. |
| The two zero-byte archives contain no P05 evidence | **D — UNKNOWN** |
| No further database exists outside the two declared roots | **B** |

## 4. Resume Point

`CP-P05E02` remains **PARTIAL — RESUMABLE**: read `pankhamhom`'s `ir_module_module` and P05 table
counts, then re-run `43 §2` and `44` for any change. Recorded as `U-18`.
