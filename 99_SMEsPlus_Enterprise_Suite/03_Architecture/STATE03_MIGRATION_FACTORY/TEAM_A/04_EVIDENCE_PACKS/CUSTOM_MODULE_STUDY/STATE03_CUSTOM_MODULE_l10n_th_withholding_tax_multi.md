> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: l10n_th_withholding_tax_multi

## 0. Header
- Module: l10n_th_withholding_tax_multi
- License (confirmed in manifest): AGPL-3 (l10n_th_withholding_tax_multi/__manifest__.py:8)
- Author (manifest): Ecosoft, Odoo Community Association (OCA) (l10n_th_withholding_tax_multi/__manifest__.py:7)
- Version (manifest): 19.0.1.0.2 (l10n_th_withholding_tax_multi/__manifest__.py:6)
- Path: addons_Extramodule/addons_extra/l10n_th_withholding_tax_multi
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Lets a vendor payment (Register Payment wizard) withhold tax for several bill lines that carry different withholding tax codes in one payment, by pre-filling one "deduction" line per bill line with a withholding tax (l10n_th_withholding_tax_multi/models/account_payment.py:37-82).
- Computation of the withheld amount per bill line: tax rate x line subtotal, reduced by withholding already taken on earlier payments against the same bill line and tax code (partial-payment handling) (account_payment.py:42-69). Each deduction line records the tax, its account, the base amount, the withheld amount and the currency (account_payment.py:72-80).
- Deduction lines are turned into journal items on the payment that carry the withholding tax code, its tax tags and a link to the original bill line (account_payment.py:85-92; account.move.line.wt_move_line, account_payment.py:122-125). These items are what the certificate module reads (see l10n_th_withholding_tax_cert file).
- When selected lines carry more than one withholding tax code and there is a payment difference, the wizard automatically switches to a "multiple deduction" handling mode (account_payment.py:23-25). Users cannot add withholding lines manually; the form raises an error for that (account_payment.py:106-113).
- The wizard deduction list gets extra columns WT and base amount (views/account_payment_view.xml:11-20).

## 2. Attachment to CORE
- Depends on l10n_th_withholding_tax and account_payment_multi_deduction (manifest:11); neither is a core Community module (see section 5).
- Extends core transient model account.payment.register (models/account_payment.py:8-9), core account.move.line (account_payment.py:122-125), and the OCA transient model account.payment.deduction (account_payment.py:95-96).
- Override of _compute_payment_difference_handling on the register wizard (core:account/wizard/account_payment_register.py:862-867): calls the core compute, then recomputes the same value again with the same rule and finally may set a third mode 'reconcile_multi_deduct' (account_payment.py:11-25). Effect: ADDS after core; the custom mode is not in the core selection (core:account/wizard/account_payment_register.py:136-142, only 'open' and 'reconcile'), so the option must come from account_payment_multi_deduction. ALTERS CORE CONTROL: yes, a payment-difference control - when the condition holds the difference is routed to multi deduction handling instead of core's "keep open / mark as paid" choice.
- Override of _update_vals_multi_deduction and _prepare_deduct_move_line: both belong to account_payment_multi_deduction, not core; they ADD to that parent's behaviour (account_payment.py:37-38,85-86).
- Reads core payment fields: early_payment_discount_mode, can_edit_wizard, payment_difference (core:account/wizard/account_payment_register.py:28,109,134) and account.move.matched_payment_ids (core:account/models/account_move.py:214).

## 3. New objects, security, automation, external calls
- No new persistent models. New transient-model fields (wt_tax_id, wt_move_line, base_amount) on account.payment.deduction and a new field wt_move_line on account.move.line (persistent, self-reference).
- No ACLs, groups, rules, cron, external calls added. Company scoping: none added; relies on core wizard/payment behaviour.
- Financial effect: the withheld amounts reduce the cash paid and are posted as separate journal items on the WT accounts through the deduction mechanism of the parent module (posting logic is in the parent, not here).

## 4. Odoo 19 compatibility
- Models/fields not in the Community 19 tree (grep of core): account.payment.deduction / deduction_ids / reconcile_multi_deduct (account_payment.py:25,38,82,96), account.withholding.tax (account_payment.py:100), wt_tax_id, payment.move_line_ids / wt_move_line (account_payment.py:45,47,88-91). They depend on other add-ons (l10n_th_withholding_tax, account_payment_multi_deduction).
- In _compute_payment_difference_handling the variable "lines" is only assigned when the context model is account.move or account.move.line (account_payment.py:14-17); with another context (e.g. no active model) the later use at line 23 would fail (code path reading, not executed).
- payment.move_line_ids used at account_payment.py:45 is declared by l10n_th_withholding_tax_cert (l10n_th_withholding_tax_cert/models/account_payment.py:23), which is NOT a declared dependency here; l10n_th_withholding_tax (declared, not read) may also provide it - UNKNOWN.
- The dependency account_payment_multi_deduction exists only in addons_Extramodule/addons (directory listing), not in addons_extra.
- Test file with 269 lines present (tests/test_withholding_tax_multi.py); not checked.

## 5. Custom-to-custom dependencies
- Declared: l10n_th_withholding_tax, account_payment_multi_deduction (manifest:11). Implicit: l10n_th_withholding_tax_cert (payment.move_line_ids at account_payment.py:45).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: the parent modules' selection values and posting logic for 'reconcile_multi_deduct' (not read).
- UNKNOWN - EVIDENCE INSUFFICIENT: rounding/currency conversion of withheld amounts for foreign currency bills (line currency copied, no conversion visible in this file).
- UNKNOWN - EVIDENCE INSUFFICIENT: behaviour when a bill line is partially paid across several payments in different states (only cancelled/rejected excluded, account_payment.py:44).
