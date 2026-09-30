> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_account_coa

Module: scgl_account_coa
License (confirmed in manifest): LGPL-3 (scgl_account_coa/__manifest__.py:7)
Author (manifest): SCG Legacy (Thailand) Co., Ltd. (__manifest__.py:8)
Version (manifest): 19.0.1.0.0 (__manifest__.py:5)
Path: Extra_Module_scgl/scgl_account_coa
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Presentation-only change to the Chart of Accounts list: relabels and un-hides columns so the list resembles a hosted-Odoo layout (summary at __manifest__.py:3-4; views/account_account_views.xml:3-7).
- Adds one read-only display field "Current Rate" showing the account currency's current rate (models/account_account.py:9).

## 2. Attachment to CORE
- core:account, object account.account.
  - Added field: `currency_rate`, related to the account currency's rate, read-only, six decimals (models/account_account.py:9). Core currency rate is a computed field (core:base/models/res_currency.py:31).
  - No core method overridden. Overrides by name: none.
- core:account, view account.view_account_list (core:account/views/account_account_views.xml:95-113). This module inherits it (views/account_account_views.xml:11) and:
  - Renames "group" column to "Parent Account" and shows it by default (lines 13-16).
  - Renames "reconcile" column to "Payment Reconciliation" (lines 17-19).
  - Turns on default display for active, non-trade, default taxes, tags (lines 20-31).
  - Removes the multi-currency group restriction on the account currency column and shows it always (lines 32-35), and adds the rate column after it (lines 36-38).
- No control is blocked or altered (no posting, lock date, valuation, approval, security or numbering change). Not `ALTERS CORE CONTROL`. Note: removing the multi-currency group on a column only affects UI visibility, not data access.

## 3. New objects, security, automation, external calls
- New models: none. New security files: none (no ACL, no groups, no rules). Company scoping: inherited from core account.account.
- Crons / server actions / external calls: none found.

## 4. Odoo 19 compatibility (checked against Community 19 tree)
- Fields referenced in the list view all exist in core 19: group_id (core:account/models/account_account.py:113), reconcile (:89), active (:42), non_trade (:123), tax_ids (:92), tag_ids (:104), currency_id (:35).
- The inherited list view id exists (core:account/views/account_account_views.xml:95). All positions target fields present in that view (core lines 103-115).
- Test asserts `company_ids` on account.account (tests/test_coa.py:21), which exists (core:account/models/account_account.py:97).
- No mismatches found.

## 5. Custom-to-custom dependencies
- None (depends only on account, __manifest__.py:10).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior of the rate column when the account currency has no rate row for the current company (the test expects 0.0 only for accounts without a currency, tests/test_coa.py:23-24).
- UNKNOWN - EVIDENCE INSUFFICIENT: interaction with other modules that also modify the same list view (no evidence in this module folder).
- Comment at views/account_account_views.xml:5-6 says a later version will switch to a parent link; no such code exists here.
