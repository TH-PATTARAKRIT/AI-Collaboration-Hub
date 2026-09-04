#!/bin/bash
B="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account"
BASE="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/base"
# Wave A primary source files
FILES="models/account_account.py models/account_account_tag.py models/account_root.py models/account_code_mapping.py models/account_journal.py models/account_move.py models/account_move_line.py models/account_full_reconcile.py models/account_partial_reconcile.py models/account_lock_exception.py models/sequence_mixin.py wizard/setup_wizards.py wizard/account_move_reversal.py wizard/account_resequence.py wizard/account_automatic_entry_wizard.py wizard/account_secure_entries_wizard.py wizard/account_merge_wizard.py wizard/account_validate_account_move.py"
echo "### P-14 Wave A source files and LOC"
tot=0
for f in $FILES; do n=$(wc -l < "$B/$f" | tr -d ' '); tot=$((tot+n)); printf "%-46s %6s\n" "$f" "$n"; done
echo "TOTAL FILES: $(echo $FILES | wc -w | tr -d ' ')   TOTAL LOC: $tot"

echo
echo "### P-11 Field declarations per Wave A file (fields.X = )"
ftot=0
for f in $FILES; do n=$(grep -cE "^[[:space:]]+[a-z_0-9]+ = fields\." "$B/$f"); ftot=$((ftot+n)); printf "%-46s %6s\n" "$f" "$n"; done
echo "TOTAL FIELD DECLARATIONS: $ftot"

echo
echo "### P-14b def statements per Wave A file"
mtot=0
for f in $FILES; do n=$(grep -cE "^[[:space:]]+def [a-zA-Z_]" "$B/$f"); mtot=$((mtot+n)); printf "%-46s %6s\n" "$f" "$n"; done
echo "TOTAL DEF: $mtot"
