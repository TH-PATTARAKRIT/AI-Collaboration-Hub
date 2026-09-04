#!/bin/bash
O="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo"
echo "### framework check_company_domain definitions"
grep -n -A6 "^def check_company_domain_parent_of\|^def check_companies_domain_parent_of\|^def check_company_domain_exact" "$O/models.py" 2>/dev/null | head -30
echo
echo "### currency_rate_live actual create call"
grep -n -A12 "CurrencyRate.create\|rate_ids\|company_id.*company.id" "$O/addons/currency_rate_live/models/res_config_settings.py" | sed -n '1,40p'
