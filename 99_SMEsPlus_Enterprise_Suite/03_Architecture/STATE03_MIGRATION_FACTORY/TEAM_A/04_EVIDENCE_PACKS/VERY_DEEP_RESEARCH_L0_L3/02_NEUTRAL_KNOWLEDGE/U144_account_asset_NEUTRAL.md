# U144 — account_asset Neutral Knowledge (Community Presence Check)

**Unit:** U144 | **Date:** 2026-10-02 | **Verdict:** ABSENT

---

## VDR Claims Table — Neutral Column

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|----------|-------------|---------|--------|-------|-----------|-------|---------------------|-------------|
| U144-C001 | MODULE_PRESENCE | addons/account_asset — directory | n/a | ABSENT | Community 19.0.post20260921 | GAP | The account_asset module directory does not exist in the Odoo 19 Community source tree under odoo/addons. | Fixed asset depreciation is not shipped as part of the standard community accounting suite |
| U144-C002 | ASSET_MODEL | addons/account_asset/models/account_asset.py | n/a | ABSENT | Community 19.0.post20260921 | GAP | No account.asset ORM model exists in Community; the asset record, depreciation method fields, and state machine are absent. | The data model for tracking individual depreciable assets does not exist in the community edition |
| U144-C003 | DEPRECIATION_BOARD | addons/account_asset/models/account_asset.py — board computation method | n/a | ABSENT | Community 19.0.post20260921 | GAP | No depreciation board computation function (linear or degressive monthly/annual schedule) exists in Community source. | Automated generation of depreciation schedule entries over an asset lifespan is not available in the community build |
| U144-C004 | JOURNAL_ENTRY_GEN | addons/account_asset/models/account_move.py | n/a | ABSENT | Community 19.0.post20260921 | GAP | No account_asset extension of account.move exists; the debit Depreciation Expense / credit Accumulated Depreciation journal entry creation logic is absent. | The mechanism that posts periodic depreciation charges as double-entry journal lines does not exist in community |
| U144-C005 | ASSET_DISPOSAL | addons/account_asset/models/account_asset.py — disposal method | n/a | ABSENT | Community 19.0.post20260921 | GAP | No asset disposal/write-off method exists in Community; final disposal entry computation, gain/loss on disposal, and asset closure workflow are absent. | The workflow and accounting entries for removing a depreciated asset from the balance sheet are not present in community |

---

## Summary

The fixed asset depreciation module is absent from Odoo 19 Community. This is a known architectural boundary: Odoo reserves the full fixed asset lifecycle management capability for the Enterprise edition. Community users must rely on manual journal entries or third-party modules to record depreciation, manage asset registers, and account for disposals.
