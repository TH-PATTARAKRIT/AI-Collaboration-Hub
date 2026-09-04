#!/bin/bash
AD="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons"
echo "### CROSS-MODULE: addons declaring a dependency on the accounting addon"
c=0
for d in "$AD"/*/; do
  m="$d__manifest__.py"
  [ -f "$m" ] && grep -q "'account'" "$m" && c=$((c+1))
done
echo "addons depending on 'account': $c  (of $(ls -d "$AD"/*/ | wc -l | tr -d ' ') addons)"
echo
echo "### CROSS-MODULE PRODUCERS: addons outside 'account' that create account.move"
grep -rl "env\['account.move'\]" "$AD" --include="*.py" 2>/dev/null | grep -v "/account/" | grep -vE "/tests?/" | sed "s|$AD/||;s|/.*||" | sort -u | tee /tmp/producers.txt | wc -l
echo "-- list --"; cat /tmp/producers.txt | head -40
echo
echo "### SCHEDULED JOBS (ir.cron) in account addon"
grep -rh "model=\"ir.cron\"" "$AD/account/data/"*.xml 2>/dev/null | wc -l
grep -rloE "ir_cron" "$AD/account/data/"*.xml 2>/dev/null
echo
echo "### automated/base_automation on Wave A models across tree"
grep -rl "base_automation" "$AD/account/" 2>/dev/null | head -3
