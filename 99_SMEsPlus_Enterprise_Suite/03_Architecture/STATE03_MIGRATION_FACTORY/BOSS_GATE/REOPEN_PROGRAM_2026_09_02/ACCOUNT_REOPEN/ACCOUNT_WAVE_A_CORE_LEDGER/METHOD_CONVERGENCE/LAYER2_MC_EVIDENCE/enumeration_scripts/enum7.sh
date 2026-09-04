#!/bin/bash
B="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account"
BASE="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/base"
cd "$B"
echo "### COMPANY-SCOPING MECHANISM ENUMERATION (Wave A + framework)"
echo "-- distinct check_company_domain functions defined in base/models/models.py --"
grep -n "def check_company_domain" "$BASE/models/models.py"
echo
echo "-- _check_company_domain assignments across account addon --"
grep -rn "_check_company_domain = " models/ wizard/ | sed 's|^|  |'
echo
echo "### sudo() call sites in Wave A files (privilege elevation = scoping bypass surface)"
for f in models/account_account.py models/account_journal.py models/account_move.py models/account_move_line.py models/account_partial_reconcile.py models/account_full_reconcile.py models/account_lock_exception.py models/sequence_mixin.py models/partner.py; do
  n=$(grep -c "\.sudo()" "$f" 2>/dev/null); printf "%-42s sudo sites=%s\n" "$f" "${n:-NA}"
done
echo "TOTAL sudo in account/models: $(grep -rh '\.sudo()' models/ | wc -l | tr -d ' ')"
echo
echo "### root_id usage (root-vs-company scoping divergence)"
grep -rn "root_id" models/ | wc -l
grep -rln "root_id" models/
