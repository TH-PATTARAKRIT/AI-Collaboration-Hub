
## CLOSURE DELTA — module identifiers used in Layer 1 file 49

| Layer-1 id | Technical name | Tree | State in DB-SM |
|---|---|---|---|
| `CM-16` | `scgl_account_sequence` | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/addons` | installed |
| `CM-17` | `scgl_tax_period_date` | same | installed |

Unsearched-tree path, 16.0 line: `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/addons` — 58 module manifests, covering 45 of the 190 modules installed in `DB-SM`.
Numbering derivation, `CM-16` `models/account_move.py:11`: `starting_sequence = "%s%d%02d0000" % (self.journal_id.code, self.date.year, self.date.month)`; custom `_sequence_monthly_regex` at `models/sequence_mixin.py:7`.
Tax-period carrier, `CM-17` `models/tax_period.py:24` `tax_period` on `account.move`; `:43` `tax_period_date` on `account.move.line`.
