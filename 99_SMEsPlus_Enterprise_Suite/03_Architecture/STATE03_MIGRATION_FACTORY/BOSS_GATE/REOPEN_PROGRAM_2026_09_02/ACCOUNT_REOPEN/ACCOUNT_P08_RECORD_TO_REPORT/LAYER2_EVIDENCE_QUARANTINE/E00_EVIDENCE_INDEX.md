
## CLOSURE DELTA — module identifiers used in Layer 1 file 49

| Layer-1 id | Technical name | Tree | State in DB-SM |
|---|---|---|---|
| `CM-16` | `scgl_account_sequence` | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/addons` | installed |
| `CM-17` | `scgl_tax_period_date` | same | installed |

Unsearched-tree path, 16.0 line: `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/addons` — 58 module manifests, covering 45 of the 190 modules installed in `DB-SM`.
Numbering derivation, `CM-16` `models/account_move.py:11`: `starting_sequence = "%s%d%02d0000" % (self.journal_id.code, self.date.year, self.date.month)`; custom `_sequence_monthly_regex` at `models/sequence_mixin.py:7`.
Tax-period carrier, `CM-17` `models/tax_period.py:24` `tax_period` on `account.move`; `:43` `tax_period_date` on `account.move.line`.

## CLOSURE DELTA — module identifiers used in Layer 1 file 42

| Layer-1 id | Technical name |
|---|---|
| `CM-01` | `scgl_purchase_advance_payment` |
| `CM-02` | `dev_print_cheque` |
| `CM-03` | `account_discount_catalog` |
| `CM-04` | `invoice_promptpay` |
| `CM-05` | `scgl_account_reports` |
| `CM-06` | `print_voucher_request` |
| `CM-07` | `equipment_sequence` |
| `CM-08` | `bi_print_journal_entries` |
| `CM-09` | `full_summarize_bills` |

Tax-group name storage literals, `DB-SM`: VAT group `{"en_US": "VAT 7%"}`; adjacent group `{"en_US": "Taxes", "th_TH": "\u0e20\u0e32\u0e29\u0e35"}`.
