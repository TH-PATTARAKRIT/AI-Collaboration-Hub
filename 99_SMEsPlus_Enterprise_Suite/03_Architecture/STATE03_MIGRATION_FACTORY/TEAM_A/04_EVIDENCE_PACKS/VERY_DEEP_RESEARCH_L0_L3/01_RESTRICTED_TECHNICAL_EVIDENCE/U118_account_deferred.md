# U118 — account: Deferred Revenue/Expense (account_deferred)
## Status: GATE-PENDING
## DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
## Date: 2026-10-02
## Modules: account (Community — no standalone account_deferred module)
## Function IDs: ACR-F01, ACR-F02
## Finding: ABSENT — no deferred revenue/expense management in Odoo 19 Community

### Absence Summary
The `account_deferred` module does not exist as a standalone module in Odoo 19 Community.
No `account.deferred` model class exists anywhere in the Community source tree.
No amortization schedule logic, no automated periodic journal entry generation, and no
deferral management workflow are present in Community. The only deferred-related references
are test helper utilities that use generic balance-sheet account types as placeholder accounts
for payment configuration purposes. Full deferred revenue/expense management is an Odoo
Enterprise-only feature.

### Source Evidence
- Checked: `account_deferred` directory — NOT FOUND
- Checked: `account/models/` — no deferred model file present
- Checked: `account/models/account_move.py` — no deferred fields
- Checked: `account/models/account_account.py` lines 44–70 — account_type selection has no dedicated deferred types
- Checked: `account/data/` — no deferred data or cron files
- Checked: `account/views/` — no deferred view files
- Reference (test placeholder only): `account/tests/common.py` lines 365–372 — uses `asset_current` for deferred expense account and `liability_current` for deferred revenue account in payment configuration test setup only

### Claim Table
| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|----------|-------------|---------|--------|-------|-----------|-------|---------------------|-------------|
| C001 | ACR-F01 | account/models/ | directory listing | C1 | No account_deferred module or model file present in Community source | ABSENT | No standalone deferred revenue or expense module exists in Odoo 19 Community | Deferred revenue module absent from Community |
| C002 | ACR-F01 | account/models/account_account.py:44-70 | account_type selection field definition | C1 | account_type selection has no dedicated deferred revenue or deferred expense entries | ABSENT | Account type enumeration covers asset, liability, equity, income and expense categories but contains no dedicated deferred revenue or deferred expense account types | Account classification has no dedicated deferred category |
| C003 | ACR-F01 | account/models/account_move.py | file content | C1 | No deferred fields or deferred schedule logic present in journal entry model | ABSENT | The journal entry model carries no fields for deferred revenue or deferred expense scheduling and no amortization calculation logic | Journal entry model has no deferred schedule fields |
| C004 | ACR-F01 | account/data/ | directory listing | C1 | No deferred cron actions or automated entry triggers present in account data directory | ABSENT | No scheduled action data records for deferred revenue or expense automation exist in Community | No automated deferred entry scheduling exists in Community |
| C005 | ACR-F02 | account/tests/common.py:365-372 | test helper setup block | C1 | Test setup assigns asset_current account type as deferred expense placeholder and liability_current as deferred revenue placeholder for payment configuration only | PRESENT-PARTIAL | Community test helpers reference deferred expense and deferred revenue account slots using generic balance sheet account types as placeholders for payment method configuration tests only — no functional deferred management logic is involved | Test helpers use generic balance sheet accounts as deferred placeholders |
| C006 | ACR-F01 | account/ | full module scan | C1 | No account.deferred model class definition exists anywhere in Community account module source | ABSENT | The account.deferred ORM model does not exist in Community — no amortization schedule storage, no period definition, no deferred entry state machine | Deferred schedule model absent from Community |
| C007 | ACR-F02 | account/models/account_account.py:44-70 | account_type field selection | C1 | Community account type list includes asset_prepayments type which can serve as a manual proxy for deferred recording but provides no automation or schedule | PRESENT-PARTIAL | Community provides a prepayment account type that practitioners may manually assign to represent deferred costs but there is no automated amortisation schedule linked to it | Prepayment account type available but no automated schedule |
