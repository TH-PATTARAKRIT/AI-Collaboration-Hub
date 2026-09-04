#!/bin/bash
A="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account"
B="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/base"
echo "### A-07: declared _sql_constraints unique_name vs real DDL index"
sed -n '710,740p' "$A/models/account_move.py"
echo
echo "### A-05: merge wizard company union + FK retarget"
sed -n '141,145p' "$A/wizard/account_merge_wizard.py"; echo "   ..."; sed -n '160,166p' "$A/wizard/account_merge_wizard.py"; echo "   ..."; sed -n '208,213p' "$A/wizard/account_merge_wizard.py"
echo
echo "### A-06: silent DELETE fallback"
sed -n '148,162p' "$B/wizard/base_partner_merge.py"
echo
echo "### A-08: res.company lock dates"
grep -n "lock_date\|fiscalyear_last" "$A/models/company.py" | head -14
echo "company.py LOC: $(wc -l < "$A/models/company.py")"
