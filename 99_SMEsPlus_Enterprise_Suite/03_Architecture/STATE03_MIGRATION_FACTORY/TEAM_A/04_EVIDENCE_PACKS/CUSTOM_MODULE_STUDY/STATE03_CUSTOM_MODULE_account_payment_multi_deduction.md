> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE — account_payment_multi_deduction

Module: account_payment_multi_deduction
License (confirmed in manifest): AGPL-3 (account_payment_multi_deduction/__manifest__.py:8)
Author (manifest): Ecosoft, Odoo Community Association (OCA) (manifest:7)
Version (manifest): 19.0.1.0.2 (manifest:6); development_status "Alpha" (manifest:17)
Path: addons_Extramodule/addons/account_payment_multi_deduction
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- In the "Register Payment" dialog, when the paid amount differs from the invoice amount, adds a third handling choice "Mark invoice as fully paid (multi deduct)" so the difference can be split over several deduction lines, each with its own account, label, amount and analytic split. (account_payment_multi_deduction/wizard/account_payment_register.py:13-28; wizard/account_payment_deduction.py:22-29; wizard/account_payment_register_views.xml:29-60)
- A deduction line can instead be marked "keep open" (left unpaid, no accounting line created). (account_payment_deduction.py:27, account_payment_register.py:106)
- Total of deductions must equal the payment difference or the wizard raises an error. (account_payment_register.py:65-80)
- Also adds an analytic distribution to the standard single "post difference" write-off. (account_payment_register.py:92-98; views xml:7-20)

## 2. Attachment to CORE
- Depends on core `account` (manifest:11). Also uses the `analytic.mixin` abstract model (core:analytic/models/analytic_mixin.py:13) via inheritance (payment_deduction.py:9, payment_register.py:11) although `analytic` is not in the manifest depends (core account manifest lists analytic: core:account/__manifest__.py:17).
- `account.payment.register` (core:account/wizard/account_payment_register.py): adds selection value to `payment_difference_handling` (core:...:136), one-to-many deduction lines, a remaining-amount computed field, and an analytic JSON field (account_payment_multi_deduction/wizard/account_payment_register.py:13-29).
- Override `_create_payment_vals_from_wizard` (payment_register.py:89; core:account/wizard/account_payment_register.py:993): ADDS behavior after core. For the multi-deduct choice it REPLACES the core-built list of write-off lines with one line per non-open deduction, and flags the payment as multi-deduction (payment_register.py:100-108).
- Onchange `_onchange_default_deduction` (payment_register.py:51-63): new method; clears deduction lines whenever difference or handling changes.
- `account.payment` (core:account/models/account_payment.py): adds boolean `is_multi_deduction` (account_payment_multi_deduction/models/account_payment.py:10).
- Override `_prepare_move_line_default_vals` (models/account_payment.py:30; core:account/models/account_payment.py:394): ADDS behavior after core — for ordinary payments with a write-off it copies analytic distribution onto the matching write-off line.
- Override `write` (models/account_payment.py:60; core:account/models/account_payment.py:951): ALTERS CORE CONTROL (payment-to-journal-entry synchronisation): for payments flagged multi-deduction it sets the context switch that tells the core to skip payment/move synchronisation (`skip_account_move_synchronization`, used in core:account/models/account_move.py:3066). It still calls core, which itself still runs `_synchronize_to_moves` for non-posted moves (core:account/models/account_payment.py:999-1011). Effect on draft multi-deduction entries: UNKNOWN.
- Override `_synchronize_from_moves` on account.payment (models/account_payment.py:55): core 19 no longer defines this method on account.payment (it exists only on the bank statement line: core:account/models/account_bank_statement_line.py:712). See section 4.
- Posting, lock dates, valuation, approvals and numbering are not touched directly; deduction lines post as ordinary write-off journal items to user-chosen accounts. Segregation is limited only by the account domain (section 4).

## 3. New objects, security, automation
- New transient model `account.payment.deduction` (payment_deduction.py:8-10). ACL: only group `account.group_account_invoice` has full rights (security/ir.model.access.csv:2). No record rules (transient; no company scoping seen).
- No crons, server actions or external calls.
- Currency conversion of each deduction uses the company currency and payment date via core rate helper (payment_register.py:111-132; core:base/models/res_currency.py:273).

## 4. Odoo 19 compatibility
- MISMATCH: deduction account domain filters on field `wt_account` of `account.account` (account_payment_multi_deduction/wizard/account_payment_deduction.py:24); no such field found in the Community tree (grep of core:addons returned nothing). It probably needs a withholding-tax field from a different module; whether one is installed: UNKNOWN. Without it, opening the deduction list is expected to fail at domain evaluation; not run.
- MISMATCH: `_synchronize_from_moves` override on account.payment (models/account_payment.py:55-58) calls a super method that does not exist on account.payment in core 19 (only on statement line, core:account/models/account_bank_statement_line.py:712). Would fail only if invoked; no core caller on payment found.
- Matches: `_seek_for_lines` (core:account/models/account_payment.py:215), `_prepare_move_line_default_vals` signature with force_balance (core:...:394), `writeoff_account_id` view field and `group1`/`group2` groups (core:account/wizard/account_payment_register_views.xml:58,106). The path `/form/group/group[@name='group1']/div/div` used in the view inheritance (views xml:22) was not fully verified against core structure.
- Uses `_(...)` import style and `self.env.user.company_id` (payment_register.py:67), not checked against v19 deprecations.

## 5. Custom-to-custom dependencies
- Implicit: needs an `account.account` boolean `wt_account` (likely from a withholding-tax/localisation custom module) — not declared in manifest depends.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: which module supplies `wt_account` in this deployment.
- UNKNOWN — EVIDENCE INSUFFICIENT: reconciliation and tax behaviour for "keep open" lines and how partial-payment state is derived (runtime not observed).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of draft multi-deduction payments when edited (sync suppression vs core sync).
- UNKNOWN — EVIDENCE INSUFFICIENT: on-disk copy vs upstream OCA release (module marked Alpha).
