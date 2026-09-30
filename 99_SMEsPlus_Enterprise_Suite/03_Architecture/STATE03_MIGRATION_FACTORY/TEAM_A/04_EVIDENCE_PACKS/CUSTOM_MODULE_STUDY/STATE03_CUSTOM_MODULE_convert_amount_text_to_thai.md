> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: convert_amount_text_to_thai

## 0. Header
- Module: convert_amount_text_to_thai
- License (confirmed in manifest): AGPL-3 (convert_amount_text_to_thai/__manifest__.py:9)
- Author (manifest): Ecosoft, Odoo Community Association (OCA) (convert_amount_text_to_thai/__manifest__.py:7)
- Version (manifest): 19.0.1.0.0 (convert_amount_text_to_thai/__manifest__.py:6)
- Path: addons_Extramodule/addons_extra/convert_amount_text_to_thai
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Makes the "amount in words" output (used on printed documents such as invoices/receipts that call the currency amount-to-text helper) render in Thai when the user or document language is Thai (th_TH): convert_amount_text_to_thai/models/res_currency.py:19-23.
- For Thai baht (currency code THB) the words come from the third-party number-to-words library's currency mode (convert_amount_text_to_thai/models/res_currency.py:41-45).
- For other currencies the number is spelled in Thai and the unit labels are looked up in a fixed three-entry translation table (Dollars, Euros, Cents) (convert_amount_text_to_thai/models/res_currency.py:8,46-59). Any other currency unit label is not in the table (see section 6).
- Manifest declares Alpha development status (convert_amount_text_to_thai/__manifest__.py:16).

## 2. Attachment to CORE
- Depends on base (convert_amount_text_to_thai/__manifest__.py:12) and on the external Python library num2words (convert_amount_text_to_thai/__manifest__.py:13).
- Extends core res.currency (convert_amount_text_to_thai/models/res_currency.py:12).
- Override of core method amount_to_text: REPLACES core only when the context language equals th_TH; otherwise it delegates to core unchanged (convert_amount_text_to_thai/models/res_currency.py:19-23). Core method at core:base/models/res_currency.py:175. So: ADDS a Thai branch in front of core; core behaviour is preserved for all other languages. ALTERS CORE CONTROL: no (formatting only).
- New hook method _convert_currency_name_hook on res.currency, returning the Thai label from the fixed table (convert_amount_text_to_thai/models/res_currency.py:14-17).
- Reads core fields currency_unit_label / currency_subunit_label (core:base/models/res_currency.py:45-46), decimal_places (core:base/models/res_currency.py:39), core method is_zero (core:base/models/res_currency.py:248), and res.lang iso_code (core:base/models/res_lang.py:74).

## 3. New objects, security, automation, external calls
- No new models, fields, ACLs, groups, record rules, cron or views (manifest data empty: convert_amount_text_to_thai/__manifest__.py:14).
- No network calls; the only external element is the num2words library (local Python package).

## 4. Odoo 19 compatibility
- Referenced core items exist in Community 19: res.currency.amount_to_text, currency_unit_label, currency_subunit_label, is_zero, res.lang.iso_code (pointers above). tools.ustr is still exported by core 19 tools (core:tools/misc.py:44,109) - the code uses it at convert_amount_text_to_thai/models/res_currency.py:48,56.
- The test file imports SavepointCase from odoo.tests.common (convert_amount_text_to_thai/tests/test_amount_to_text.py:7); no SavepointCase was found in core:tests/*.py (grep), so the shipped test would probably fail to import under 19. Tests are not part of runtime.
- The core method in 19 also handles a missing num2words with a warning; this override imports num2words at module import (convert_amount_text_to_thai/models/res_currency.py:4) so the module would fail to load if the library is absent.

## 5. Custom-to-custom dependencies
- None declared. NOTE: this module is byte-identical in Python and manifest content to its sibling (l10n_th_amount_to_text) - both extend res.currency.amount_to_text identically; installing both is redundant and the inheritance chain would run the same override twice. The static description page differs only.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: behaviour for non-THB currencies other than USD/EUR (lookup table has only three labels; a missing key path is not guarded in convert_amount_text_to_thai/models/res_currency.py:17).
- UNKNOWN - EVIDENCE INSUFFICIENT: which printed reports in the suite call amount_to_text and whether their language context is set to th_TH.
- UNKNOWN - EVIDENCE INSUFFICIENT: which version of num2words is installed in the target environment.
