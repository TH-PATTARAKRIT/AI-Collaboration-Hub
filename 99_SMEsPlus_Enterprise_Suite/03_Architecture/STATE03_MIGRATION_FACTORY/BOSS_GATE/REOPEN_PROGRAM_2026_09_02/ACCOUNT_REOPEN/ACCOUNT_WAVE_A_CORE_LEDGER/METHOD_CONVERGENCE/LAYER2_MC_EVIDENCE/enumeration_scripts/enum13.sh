#!/bin/bash
AD="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons"
echo "### RULE 5 candidate: account/models/res_currency.py:220-240"
sed -n '218,240p' "$AD/account/models/res_currency.py"
echo
echo "### default check_company_domain (framework) definition"
grep -rn "def check_company_domain_exact\|def check_company_domain_parent_of\|def check_companies_domain_parent_of" "$AD/../odoo/models.py" "$AD/base/models/"*.py 2>/dev/null | head
find "$AD/.." -maxdepth 2 -name "models.py" -path "*odoo*" 2>/dev/null | head -3
echo
echo "### RULE 6 candidate: currency_rate_live writer"
sed -n '258,285p' "$AD/currency_rate_live/models/res_config_settings.py"
