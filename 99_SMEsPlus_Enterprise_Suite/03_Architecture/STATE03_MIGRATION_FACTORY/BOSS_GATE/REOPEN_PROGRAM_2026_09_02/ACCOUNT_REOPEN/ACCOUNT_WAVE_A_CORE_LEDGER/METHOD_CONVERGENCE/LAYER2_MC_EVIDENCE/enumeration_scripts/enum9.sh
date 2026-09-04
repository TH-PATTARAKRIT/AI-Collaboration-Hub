#!/bin/bash
A="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account"
BASE="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/base"
echo "### account.move state selection values"
sed -n '144,157p' "$A/models/account_move.py"
echo
echo "### account.lock_exception state"
sed -n '20,26p' "$A/models/account_lock_exception.py"
echo
echo "### res.currency.rate company_id declaration (SB-05 core)"
grep -rn "company_id" "$BASE/models/res_currency.py" | head -12
echo
echo "### res.currency.rate record rule in base?"
grep -rn "res_currency_rate\|currency_rate" "$BASE/security/"*.xml 2>/dev/null | head -10
echo "--- base ir.rule count ---"
grep -h "model=\"ir.rule\"" "$BASE/security/"*.xml 2>/dev/null | wc -l
