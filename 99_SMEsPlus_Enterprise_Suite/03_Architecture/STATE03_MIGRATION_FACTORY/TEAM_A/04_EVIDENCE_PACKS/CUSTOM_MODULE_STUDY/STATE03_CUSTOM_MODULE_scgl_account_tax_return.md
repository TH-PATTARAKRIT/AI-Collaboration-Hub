> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_account_tax_return

Module: scgl_account_tax_return
License (confirmed in manifest): LGPL-3 (scgl_account_tax_return/__manifest__.py:9)
Author (manifest): SCG Legacy (Thailand) Co., Ltd. (__manifest__.py:10)
Version (manifest): 19.0.1.0.1 (__manifest__.py:7)
Path: Extra_Module_scgl/scgl_account_tax_return
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Monthly Thai VAT return period (form "PP.30") with a status flow To Do -> Closed -> Filed (models/tax_return.py:28; PROVENANCE.txt:2-3).
- For each period it sums output tax and input tax from posted tax lines and shows net tax payable or refundable (models/tax_return.py:36-39, 98-108).
- "Close Period" creates a draft closing journal entry that clears each VAT account balance of the period into a VAT-payable or VAT-refundable account (models/tax_return.py:113-157).
- Then the user posts the closing entry, marks the return as filed, or resets it (models/tax_return.py:159-184; views/tax_return_views.xml:29-38).
- Per-company settings: closing journal, VAT payable account, VAT refundable account (models/res_company.py:9-19; views/res_config_settings_views.xml:10-28).
- Provenance note states clean-room rewrite without reading OEEL-1 code (PROVENANCE.txt:4). Self-declared, not verified.

## 2. Attachment to CORE
- core:account, account.move: one added link field to the tax return (models/account_move.py:9). No method override on account.move. Overrides of core methods by name: none.
- core:account, res.company / res.config.settings: added fields only (models/res_company.py:9-19, models/res_config_settings.py:9-11).
- core:account, account.move.line: read-only use. Tax lines = posted lines with a tax_line_id, sale/purchase tax type, non-negative rate, inside the period dates, not on a tax-return closing entry; cash-basis transition lines are excluded until paid (models/tax_return.py:85-96). Group taxes excluded by the domain helper (line 83) but that helper is not used by the line search (see section 6).
- Posting side effect: `action_close` creates an account.move of type entry dated the period end (models/tax_return.py:149-153), one line per VAT account with non-zero balance plus one balancing line (lines 113-141). `action_post_entry` posts it through core action_post (lines 159-163; core action_post hard-posts, core:account/models/account_move.py:6198).
- Reversal on reset: a posted closing entry is reversed with cancel=True using the original date; a draft one is deleted (lines 174-184). Uses core `_reverse_moves` (core:account/models/account_move.py:5495).
- Lock-date and tax-closing interaction (facts only):
  - The module does not read, set or move tax_lock_date, fiscalyear_lock_date, sale/purchase lock or hard lock date (no reference in module files). "Closed" and "Filed" are module-local statuses and do not lock the period.
  - After Close, additional VAT lines posted later inside the same period are not part of the existing closing entry; the return figures recompute from live data (models/tax_return.py:98-108), so figures can drift from the posted closing entry. Nothing in the module blocks or warns.
  - The closing entry's lines carry no tax or tax tags, so core does not treat it as tax-report-affecting and the tax lock date does not apply to it (core:account/models/account_move_line.py:1522-1524; core:account/models/account_move.py:5315-5316). Fiscal-year and hard lock dates do apply (core:account/models/company.py:723-737).
  - If the period end falls on or before a fiscal/hard lock date, core hard-post re-dates the entry to the day after the lock rather than refusing (core:account/models/account_move.py:5702-5706). The reversal path is also shifted by core copy logic (core:account/models/account_move.py:3813-3829). Resulting entry date may differ from the return period.
  - Verdict on core controls: adds a new period-closing step next to core; does not replace, block or bypass any core lock. Not `ALTERS CORE CONTROL`, except that the created closing entry moves balances between tax accounts outside core's own tax reporting.
- Delete guard: a return not in To Do cannot be deleted (models/tax_return.py:195-198).
- Menu: under core Closing menu (views/menus.xml:5; core:account/views/account_menuitem.xml:29).

## 3. New objects, security, automation, external calls
- New model scgl.tax.return with mail thread and activities, company default, overlap constraint per company, period-end CHECK (models/tax_return.py:16-75).
- ACL: account.group_account_user full CRUD, account.group_account_readonly read-only (security/ir.model.access.csv:2-3). No ir.rule file; company scoping relies on the company field, `_check_company_auto` and the company-aware many2one fields (models/tax_return.py:21,24). No record rule found. Company defaults to the active company (line 24).
- Crons / server actions / external calls: none found. Companion viewer module may show a "Returns" button when this model exists (PROVENANCE.txt:5); not studied here.

## 4. Odoo 19 compatibility (checked against Community 19 tree)
- Exist in core 19: tax_line_id (core:account/models/account_move_line.py:212), parent_state (:69), account.tax cash_basis_transition_account_id (core:account/models/account_tax.py:170), type_tax_use (:81), amount_type (:84), menu account.account_closing_menu (core:account/views/account_menuitem.xml:29), settings anchor for app "account" (core:account/views/res_config_settings_views.xml:23).
- Uses the `models.Constraint` declaration (models/tax_return.py:44), which core 19 also uses (core:account/models/account_journal.py:36). The `self.env._` translation helper is `not checked` beyond core's own use of it in account_move.py.
- No mismatch found in the account fields/methods listed.

## 5. Custom-to-custom dependencies
- Manifest: none beyond account (__manifest__.py:12). Optional coupling from a viewer module by model-presence check (PROVENANCE.txt:5).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: `_vat_taxes_domain` (models/tax_return.py:82-83) is defined but the tax-line search (lines 89-94) does not use it; whether group taxes' child lines are filtered correctly is not shown by the code.
- UNKNOWN - EVIDENCE INSUFFICIENT: multi-company isolation (no record rule).
- UNKNOWN - EVIDENCE INSUFFICIENT: legal correctness of the Thai VAT figures; tests cover a sale/purchase 7% scenario only (tests/test_tax_return.py:61-104).
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior when the closing journal or accounts are changed after a return is closed.
