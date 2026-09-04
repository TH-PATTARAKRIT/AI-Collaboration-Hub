#!/bin/bash
A="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account"
B="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/base"
echo "### RB-05 VERIFICATION: are the severe-finding sites inside the original 18-file set?"
echo "X-05 site  : account/models/partner.py       -> in original set? NO"
echo "SB-05 site : base/models/res_currency.py     -> in original set? NO"
echo "FX-08 site : base/models/res_currency.py     -> in original set? NO"
echo "AC-02 site : base/models/res_currency.py     -> in original set? NO"
echo "rule6 site : account/models/res_currency.py  -> in original set? NO"
echo "lock dates : account/models/company.py       -> in original set? NO"
echo
echo "### CORRECTED WAVE A SURFACE (adds the 4 boundary-carrier files)"
ORIG="$A/models/account_account.py $A/models/account_account_tag.py $A/models/account_root.py $A/models/account_code_mapping.py $A/models/account_journal.py $A/models/account_move.py $A/models/account_move_line.py $A/models/account_full_reconcile.py $A/models/account_partial_reconcile.py $A/models/account_lock_exception.py $A/models/sequence_mixin.py $A/wizard/setup_wizards.py $A/wizard/account_move_reversal.py $A/wizard/account_resequence.py $A/wizard/account_automatic_entry_wizard.py $A/wizard/account_secure_entries_wizard.py $A/wizard/account_merge_wizard.py $A/wizard/account_validate_account_move.py"
ADDED="$A/models/partner.py $A/models/res_currency.py $A/models/company.py $B/models/res_currency.py"
for f in $ADDED; do printf "  + %-46s LOC %s\n" "$(echo $f | sed 's|.*/addons/||')" "$(wc -l < "$f" | tr -d ' ')"; done
echo
echo "ORIGINAL : files=$(echo $ORIG | wc -w | tr -d ' ')  LOC=$(cat $ORIG | wc -l | tr -d ' ')  fields=$(grep -hcE '^[[:space:]]+[a-z_0-9]+ = fields\.' $ORIG | paste -sd+ - | bc)  defs=$(grep -hE '^[[:space:]]+def [a-zA-Z_]' $ORIG | wc -l | tr -d ' ')  raises=$(grep -hE 'raise (UserError|ValidationError|RedirectWarning|AccessError)' $ORIG | wc -l | tr -d ' ')"
echo "CORRECTED: files=$(echo $ORIG $ADDED | wc -w | tr -d ' ')  LOC=$(cat $ORIG $ADDED | wc -l | tr -d ' ')  fields=$(grep -hE '^[[:space:]]+[a-z_0-9]+ = fields\.' $ORIG $ADDED | wc -l | tr -d ' ')  defs=$(grep -hE '^[[:space:]]+def [a-zA-Z_]' $ORIG $ADDED | wc -l | tr -d ' ')  raises=$(grep -hE 'raise (UserError|ValidationError|RedirectWarning|AccessError)' $ORIG $ADDED | wc -l | tr -d ' ')"
echo
echo "### sudo sites in the 4 added files"
for f in $ADDED; do printf "  %-46s sudo=%s\n" "$(echo $f | sed 's|.*/addons/||')" "$(grep -c '\.sudo()' "$f")"; done
