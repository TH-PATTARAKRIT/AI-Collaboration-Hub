#!/bin/bash
A="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account"
B="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/base"
ORIG=()
for f in account_account account_account_tag account_root account_code_mapping account_journal account_move account_move_line account_full_reconcile account_partial_reconcile account_lock_exception sequence_mixin; do ORIG+=("$A/models/$f.py"); done
for f in setup_wizards account_move_reversal account_resequence account_automatic_entry_wizard account_secure_entries_wizard account_merge_wizard account_validate_account_move; do ORIG+=("$A/wizard/$f.py"); done
ADD=("$A/models/company.py" "$A/models/partner.py" "$A/models/res_currency.py" "$A/models/account_journal_dashboard.py" "$A/models/account_move_line_tax_details.py" "$B/models/res_currency.py" "$B/models/res_company.py" "$B/wizard/base_partner_merge.py")
echo "### ADDED BOUNDARY-CARRIER FILES"
for f in "${ADD[@]}"; do printf "  + %-52s LOC %6s  sudo %3s  sql %3s\n" "$(echo "$f" | sed 's|.*/addons/||')" "$(wc -l < "$f"|tr -d ' ')" "$(grep -c '\.sudo()' "$f")" "$(grep -c 'cr\.execute' "$f")"; done
echo
echo "ORIGINAL  files=${#ORIG[@]}  LOC=$(cat "${ORIG[@]}" | wc -l | tr -d ' ')  defs=$(grep -hE '^[[:space:]]+def ' "${ORIG[@]}" | wc -l | tr -d ' ')  fields=$(grep -hE '^[[:space:]]+[A-Za-z_0-9]+ = fields\.' "${ORIG[@]}" | wc -l | tr -d ' ')  raises=$(grep -hE 'raise (UserError|ValidationError|RedirectWarning|AccessError)' "${ORIG[@]}" | wc -l | tr -d ' ')"
echo "CORRECTED files=$(( ${#ORIG[@]} + ${#ADD[@]} ))  LOC=$(cat "${ORIG[@]}" "${ADD[@]}" | wc -l | tr -d ' ')  defs=$(grep -hE '^[[:space:]]+def ' "${ORIG[@]}" "${ADD[@]}" | wc -l | tr -d ' ')  fields=$(grep -hE '^[[:space:]]+[A-Za-z_0-9]+ = fields\.' "${ORIG[@]}" "${ADD[@]}" | wc -l | tr -d ' ')  raises=$(grep -hE 'raise (UserError|ValidationError|RedirectWarning|AccessError)' "${ORIG[@]}" "${ADD[@]}" | wc -l | tr -d ' ')"
echo
echo "### NEW POPULATIONS from reviewer A (Wave A original 18 files)"
echo "api.depends      : $(grep -hE '@api\.depends' "${ORIG[@]}" | wc -l | tr -d ' ')"
echo "compute=         : $(grep -ho 'compute=' "${ORIG[@]}" | wc -l | tr -d ' ')"
echo "store=True       : $(grep -ho 'store=True' "${ORIG[@]}" | wc -l | tr -d ' ')"
echo "ondelete=        : $(grep -ho "ondelete=" "${ORIG[@]}" | wc -l | tr -d ' ')"
echo "ondelete cascade : $(grep -ho "ondelete='cascade'" "${ORIG[@]}" | wc -l | tr -d ' ')"
echo "api.onchange     : $(grep -hE '@api\.onchange' "${ORIG[@]}" | wc -l | tr -d ' ')"
echo "tracking=        : $(grep -ho 'tracking=' "${ORIG[@]}" | wc -l | tr -d ' ')"
echo "def init/_auto_init: $(grep -hE '^[[:space:]]+def (init|_auto_init)\(' "${ORIG[@]}" | wc -l | tr -d ' ')"
echo "ir.actions.server: $(grep -h 'model="ir.actions.server"' "$A"/data/*.xml "$A"/views/*.xml 2>/dev/null | wc -l | tr -d ' ')"
