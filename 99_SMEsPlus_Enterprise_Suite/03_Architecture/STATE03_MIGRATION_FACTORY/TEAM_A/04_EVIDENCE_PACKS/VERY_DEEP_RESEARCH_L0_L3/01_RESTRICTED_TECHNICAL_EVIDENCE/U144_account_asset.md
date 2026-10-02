# U144 — account_asset: Fixed Asset Depreciation (Community Presence Check)

**Unit:** U144  
**Group:** G01  
**Priority:** P1  
**Research date:** 2026-10-02  
**Researcher:** DeepSeek STATE03 VDR Worker  
**Verdict:** ABSENT — module not present in Odoo Community 19  

---

## Presence Check Result

```
ls "/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/account_asset"
# => No such file or directory
```

Confirmed: `account_asset` does **not** exist under `/odoo/addons/` in the Community 19.0.post20260921 source tree. The only asset-adjacent module found is `test_assetsbundle`, which is a JavaScript bundling test module, not a fixed-asset accounting module.

All account-related modules present in Community:
- `account`, `account_payment`, `account_debit_note`, `account_check_printing`,
  `account_edi`, `account_edi_ubl_cii`, `account_edi_proxy_client`,
  `account_fleet`, `account_payment_interco`, `account_peppol`,
  `account_peppol_advanced_fields`, `account_peppol_response`,
  `account_qr_code_emv`, `account_qr_code_sepa`, `account_tax_python`,
  `account_test`, `account_update_tax_tags`, `account_add_gln`

None of these provide fixed asset depreciation functionality.

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|----------|-------------|---------|--------|-------|-----------|-------|---------------------|-------------|
| U144-C001 | MODULE_PRESENCE | addons/account_asset — directory | n/a | ABSENT | Community 19.0.post20260921 | GAP | The account_asset module directory does not exist in the Odoo 19 Community source tree under odoo/addons. | Fixed asset depreciation is not shipped as part of the standard community accounting suite |
| U144-C002 | ASSET_MODEL | addons/account_asset/models/account_asset.py | n/a | ABSENT | Community 19.0.post20260921 | GAP | No account.asset ORM model exists in Community; the asset record, depreciation method fields, and state machine are absent. | The data model for tracking individual depreciable assets does not exist in the community edition |
| U144-C003 | DEPRECIATION_BOARD | addons/account_asset/models/account_asset.py — board computation method | n/a | ABSENT | Community 19.0.post20260921 | GAP | No depreciation board computation function (linear or degressive monthly/annual schedule) exists in Community source. | Automated generation of depreciation schedule entries over an asset's useful life is not available in the community build |
| U144-C004 | JOURNAL_ENTRY_GEN | addons/account_asset/models/account_move.py | n/a | ABSENT | Community 19.0.post20260921 | GAP | No account_asset extension of account.move exists; the debit Depreciation Expense / credit Accumulated Depreciation journal entry creation logic is absent. | The mechanism that posts periodic depreciation charges as double-entry journal lines does not exist in community |
| U144-C005 | ASSET_DISPOSAL | addons/account_asset/models/account_asset.py — disposal method | n/a | ABSENT | Community 19.0.post20260921 | GAP | No asset disposal/write-off method exists in Community; final disposal entry computation, gain/loss on disposal, and asset closure workflow are absent. | The workflow and accounting entries for removing a fully or partially depreciated asset from the balance sheet are not present in community |

---

## Migration Risk Assessment

**C1 Risk confirmed.** Fixed asset accounting (depreciation schedules, accumulated depreciation tracking, asset disposal) is an **Enterprise-only** feature in Odoo 19 Community. Any SMEsPlus migration targeting Community must either:

1. Accept the absence of this capability (manual depreciation via standard journal entries only), or
2. License Odoo Enterprise for `account_asset`, or
3. Implement a third-party Community module providing equivalent functionality.

This gap affects balance sheet completeness (Property, Plant & Equipment schedule), period-close accuracy, and compliance with fixed-asset disclosure requirements.
