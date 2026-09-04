#!/bin/bash
B="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account"
FILES=$(cd "$B" && echo models/account_account.py models/account_account_tag.py models/account_root.py models/account_code_mapping.py models/account_journal.py models/account_move.py models/account_move_line.py models/account_full_reconcile.py models/account_partial_reconcile.py models/account_lock_exception.py models/sequence_mixin.py wizard/setup_wizards.py wizard/account_move_reversal.py wizard/account_resequence.py wizard/account_automatic_entry_wizard.py wizard/account_secure_entries_wizard.py wizard/account_merge_wizard.py wizard/account_validate_account_move.py)
cd "$B"
echo "### P-15 SQL constraints in Wave A files"
grep -n "_sql_constraints" $FILES
echo "-- constraint tuples --"
for f in $FILES; do awk '/_sql_constraints/,/\]/' "$f" | grep -cE "^\s*\(" | xargs -I{} echo "$f {}"; done | grep -v " 0$"
echo
echo "### P-15b @api.constrains decorators (application-level)"
grep -c "@api.constrains" $FILES | grep -v ":0$"
echo "TOTAL: $(grep -h "@api.constrains" $FILES | wc -l | tr -d ' ')"
echo
echo "### P-12 state selection fields in Wave A files"
grep -nE "^[[:space:]]+(state|status|payment_state|parent_state|move_type|reconciled)[a-z_]* = fields\.Selection" $FILES
echo
echo "### P-23 failure paths: raise UserError / ValidationError / RedirectWarning"
for f in $FILES; do n=$(grep -cE "raise (UserError|ValidationError|RedirectWarning|AccessError)" "$f"); printf "%-46s %4s\n" "$f" "$n"; done
echo "TOTAL RAISES: $(grep -hEc "raise (UserError|ValidationError|RedirectWarning|AccessError)" $FILES | paste -sd+ | bc)"
