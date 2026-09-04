#!/bin/bash
B="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account"
cd "$B"
echo "### RAW SQL execution sites in account/models (record-rule bypass surface)"
echo "TOTAL cr.execute: $(grep -rh "cr.execute\|_cr.execute" models/ | wc -l | tr -d ' ')"
grep -rc "cr.execute" models/ 2>/dev/null | grep -v ":0$" | sort -t: -k2 -rn | head -20
echo
echo "### EXPLICIT BYPASS TOKENS (named bypass mechanisms)"
for t in bypass_lock_check BYPASS_LOCK_CHECK defer_account_code_checks check_move_validity skip_ tracking_disable install_mode; do
  n=$(grep -rh "$t" models/ wizard/ 2>/dev/null | wc -l | tr -d ' ')
  printf "%-30s sites=%s\n" "$t" "$n"
done
echo
echo "### ir.config_parameter keys read/written in account addon (database-wide, no company dimension)"
grep -rhoE "get_param\(['\"][a-zA-Z_0-9.]+['\"]|set_param\(['\"][a-zA-Z_0-9.]+['\"]" models/ wizard/ 2>/dev/null | sed -E "s/.*\(['\"]//" | sort -u
echo "COUNT: $(grep -rhoE "get_param\(['\"][a-zA-Z_0-9.]+['\"]|set_param\(['\"][a-zA-Z_0-9.]+['\"]" models/ wizard/ 2>/dev/null | sed -E "s/.*\(['\"]//" | sort -u | wc -l | tr -d ' ')"
