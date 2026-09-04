#!/bin/bash
B="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account"
cd "$B"
echo "### Which Wave A models have a company record rule? (bounded scope = account/security/*.xml)"
for m in account.account account.journal account.journal.group account.move account.move.line account.full.reconcile account.partial.reconcile account.lock_exception account.group account.root account.code.mapping account.account.tag; do
  n=$(grep -A6 "model=\"ir.rule\"" security/*.xml | grep -c "model_$(echo $m | tr '.' '_')\"")
  printf "%-30s ir.rule refs = %s\n" "$m" "$n"
done
echo
echo "### ALL ir.rule model refs in account/security (bounded enumeration)"
grep -oE "ref=\"model_[a-z_0-9]+\"" security/*.xml | sed 's/.*ref="//;s/"//' | sort | uniq -c | sort -rn
echo
echo "### access rows for reconcile / lock_exception models across WHOLE addon dir"
tail -n +2 security/ir.model.access.csv | grep -E "reconcile|lock_exception" 
