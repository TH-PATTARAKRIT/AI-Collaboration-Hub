# A3 — DOMAIN PRIORITIZATION

**This is research sequencing, NOT final product scope.** No product scope is declared here.

## Why DOMAIN_01 Accounting Core is researched first — evidence-based

| Criterion | Evidence | Assessment |
|---|---|---|
| **Dependency centrality** | `account_move` is extended **10×** and `account_move_line` **8×** by the customer layer — the most-extended models in the entire customisation set (STEP040304R4 model inventory). 511 of 1,504 modules are accounting-named or accounting-category. | HIGHEST |
| **Migration criticality** | Every downstream domain (AR/AP, Payments, Tax/WHT, Assets, Inventory Valuation, Reporting) posts into or reads from `account_move`/`account_move_line`. Nothing else can be migrated correctly before the journal model is understood. | HIGHEST |
| **Financial correctness** | The debit=credit invariant has **zero database enforcement** (0 CHECK constraints across `account_move` + `account_move_line`; only 1 PK + 36 FK and 1 PK + 30 FK). Correctness rests entirely on application code that is explicitly bypassable. | CRITICAL RISK |
| **Downstream impact** | 5,141 FK edges exist in the dump; `account_move_line` carries 30 of the FK constraints in the core pair and 27 indexes — it is the hub object. | HIGHEST |
| **Evidence availability** | `account` is **LGPL-3 and fully readable**; its 40 model files are in the readable partition. Schema evidence exists for all core tables. This domain has the best evidence-to-risk ratio available. | STRONG |
| **Risk level** | Lock-date behaviour spans **six** distinct company-level controls incl. an irreversible `hard_lock_date`; hash-chain immutability is **opt-in per journal**. Misunderstanding any of these produces silently wrong financials. | HIGH |

## Deferred, captured as dependencies only
AR/AP · Payments · Tax/VAT/WHT · Assets · Inventory Valuation · Reporting.
Each is registered in `14_INTEGRATION_REGISTER.md` as a coupling point with no research performed.

## Not declared here
Product scope · target design · migration order commitment · module inclusion list.
