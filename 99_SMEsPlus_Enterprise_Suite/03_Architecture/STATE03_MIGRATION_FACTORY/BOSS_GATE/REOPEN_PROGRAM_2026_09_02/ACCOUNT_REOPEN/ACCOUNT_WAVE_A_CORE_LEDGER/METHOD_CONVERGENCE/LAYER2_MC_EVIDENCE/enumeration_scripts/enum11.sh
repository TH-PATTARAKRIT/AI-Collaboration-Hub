#!/bin/bash
AD="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons"
echo "### Who calls _select_companies_rates ?"
grep -rn "_select_companies_rates" "$AD" 2>/dev/null | grep -v "\.po:" | head
echo
echo "### rate company_id in base views (AC-01 editability)"
grep -n "company_id" "$AD/base/views/res_currency_views.xml" | head -12
echo
echo "### ir.model.access rows for res.currency.rate"
grep -h "model_res_currency_rate" "$AD/base/security/ir.model.access.csv" 2>/dev/null
grep -rh "model_res_currency_rate," "$AD/account/security/ir.model.access.csv" 2>/dev/null
