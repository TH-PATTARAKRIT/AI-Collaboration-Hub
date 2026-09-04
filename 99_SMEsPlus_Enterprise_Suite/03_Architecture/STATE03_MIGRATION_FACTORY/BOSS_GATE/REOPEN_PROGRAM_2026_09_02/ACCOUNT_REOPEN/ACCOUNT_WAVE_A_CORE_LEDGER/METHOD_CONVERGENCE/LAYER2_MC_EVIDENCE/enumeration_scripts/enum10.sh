#!/bin/bash
BASE="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/base"
F="$BASE/models/res_currency.py"
echo "### ALL rate-resolution sites in res_currency.py"
grep -n "def _get_rates\|def _select_companies_rates\|def _get_conversion_rate\|cr.execute\|_cr.execute\|def _convert\|def _compute_current_rate" "$F"
echo
echo "### _get_rates body"
sed -n "$(grep -n 'def _get_rates' "$F" | head -1 | cut -d: -f1),+40p" "$F"
