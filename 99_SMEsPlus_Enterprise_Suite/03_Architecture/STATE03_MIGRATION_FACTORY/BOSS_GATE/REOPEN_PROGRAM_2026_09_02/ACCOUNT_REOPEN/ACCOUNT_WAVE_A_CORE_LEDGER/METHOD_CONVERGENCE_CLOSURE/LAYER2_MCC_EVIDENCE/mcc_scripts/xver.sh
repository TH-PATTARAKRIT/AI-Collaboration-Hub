#!/bin/bash
# Cross-version matrix for res.currency.rate company scoping
for T in \
 "/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/addons/base/models/res_currency.py:v16" \
 "/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/base/models/res_currency.py:v18-e-20250608(SRC-A)" \
 "/Volumes/iMacSys/ODOO/SOURCE CODE/ODOO 18/odoo-18.0.post20260605/odoo/addons/base/models/res_currency.py:v18-post20260605" \
 "/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/ODOO19/addons/base/models/res_currency.py:v19-community" \
 "/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/SMEsPlus19/odoo-19.0+e.20260312/odoo/addons/base/models/res_currency.py:v19-e-20260312" \
 "/Volumes/iMacSys/CLAUDE AI/SMEsPlus/SMEsPlus19/SMEsPlus/odoo-19.0+e.20260417/odoo/addons/base/models/res_currency.py:v19-e-20260417" \
 ; do
  F="${T%:*}"; L="${T##*:}"
  if [ ! -f "$F" ]; then echo "$L | FILE MISSING"; continue; fi
  CHK=$(grep -c "_check_company_id" "$F")
  GR=$(grep -n "company_id', 'in', (False" "$F" | wc -l | tr -d ' ')
  LR=$(grep -c "_get_latest_rate" "$F")
  LRC=$(grep -c "_get_last_rates_for_companies" "$F")
  DEF=$(grep -n "default=lambda self: self.env.company" "$F" | head -1 | cut -d: -f1)
  UNQ=$(grep -c "unique_name_per_day\|unique (name,currency_id,company_id)" "$F")
  echo "$L | LOC=$(wc -l < "$F") | _check_company_id=$CHK | _get_rates(False,root)=$GR | default_root_line=$DEF | uniq_constraint=$UNQ"
done
