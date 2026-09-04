#!/bin/bash
BASE="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/base"
A="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account"
AD="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons"
echo "### A-01: _check_company_id on res.currency.rate"
sed -n '455,465p' "$BASE/models/res_currency.py"
echo
echo "### A-02: cron root-only filter"
grep -n "parent_id.*False\|_parse_.*data\|search(\[" "$AD/currency_rate_live/models/res_config_settings.py" | sed -n '1,12p'
sed -n '1324,1334p' "$AD/currency_rate_live/models/res_config_settings.py"
echo
echo "### A-03: sibling resolvers :395 and :401-403"
sed -n '392,406p' "$BASE/models/res_currency.py"
echo
echo "### A-04: 6th config parameter"
sed -n '154,162p' "$A/models/sequence_mixin.py"
echo
echo "### addon dir count"
find "$AD" -maxdepth 1 -mindepth 1 -type d | wc -l
echo "### account_move_line sql_constraints tuples"
sed -n '429,450p' "$A/models/account_move_line.py"
