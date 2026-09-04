#!/bin/bash
A="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account"
cd "$A" || exit 1
F18="models/account_account.py models/account_account_tag.py models/account_root.py models/account_code_mapping.py models/account_journal.py models/account_move.py models/account_move_line.py models/account_full_reconcile.py models/account_partial_reconcile.py models/account_lock_exception.py models/sequence_mixin.py wizard/setup_wizards.py wizard/account_move_reversal.py wizard/account_resequence.py wizard/account_automatic_entry_wizard.py wizard/account_secure_entries_wizard.py wizard/account_merge_wizard.py wizard/account_validate_account_move.py"
echo "=== _name declarations over the 18 files ==="
grep -hoE "^[[:space:]]+_name = ['\"][^'\"]+" $F18 | sed -E "s/.*['\"]//" | sort -u
echo "COUNT: $(grep -hoE "^[[:space:]]+_name = ['\"][^'\"]+" $F18 | sed -E "s/.*['\"]//" | sort -u | wc -l | tr -d ' ')"
echo
echo "=== _check_company_auto over 18 files ==="
grep -n "_check_company_auto" $F18
echo "COUNT True: $(grep -h "_check_company_auto[[:space:]]*=[[:space:]]*True" $F18 | wc -l | tr -d ' ')"
echo
echo "=== check_company=True over 18 files: $(grep -h "check_company=True" $F18 | wc -l | tr -d ' ')"
echo "=== relational field decls over 18 files: $(grep -hE "^[[:space:]]+[A-Za-z_][A-Za-z0-9_]* = fields\.(Many2one|Many2many|One2many)" $F18 | wc -l | tr -d ' ')"
echo
echo "=== company.py: check_company=True on res.company + _check_company_auto ==="
grep -c "check_company=True" models/company.py
grep -n "_check_company_auto" models/company.py "$A/../base/models/res_company.py" 2>/dev/null
echo "_check_company() call sites in addons/account: $(grep -rn "_check_company()" --include='*.py' . | wc -l | tr -d ' ')"
