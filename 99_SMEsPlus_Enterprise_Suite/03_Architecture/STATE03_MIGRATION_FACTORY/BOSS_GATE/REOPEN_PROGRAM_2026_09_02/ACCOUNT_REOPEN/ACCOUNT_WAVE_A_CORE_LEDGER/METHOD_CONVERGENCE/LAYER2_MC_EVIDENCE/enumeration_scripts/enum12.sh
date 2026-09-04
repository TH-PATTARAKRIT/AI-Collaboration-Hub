#!/bin/bash
AD="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons"
echo "### BOUNDED ENUMERATION: every write path to res.currency.rate across all 797 addons"
echo "-- create/write on res.currency.rate --"
grep -rn "env\['res.currency.rate'\]" "$AD" --include="*.py" 2>/dev/null | grep -vE "/tests?/" | sed "s|$AD/||"
echo
echo "-- rate_ids write (one2many create) --"
grep -rn "rate_ids" "$AD" --include="*.py" 2>/dev/null | grep -vE "/tests?/|\.po:" | grep -E "create|write|\[\(0" | sed "s|$AD/||" | head -20
