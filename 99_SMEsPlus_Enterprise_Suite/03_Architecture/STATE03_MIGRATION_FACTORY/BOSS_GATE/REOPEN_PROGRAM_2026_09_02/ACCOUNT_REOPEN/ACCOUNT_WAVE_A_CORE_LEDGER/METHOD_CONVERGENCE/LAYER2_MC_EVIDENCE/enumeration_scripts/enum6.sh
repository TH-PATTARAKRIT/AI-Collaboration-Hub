#!/bin/bash
B="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account"
cd "$B"
echo "### P-09 MENUS (ir.ui.menu) in account addon"
grep -rhoE "<menuitem[^>]*id=\"[a-z_0-9]+\"" views/*.xml | wc -l
echo "-- menuitem total incl multiline --"
grep -rh "<menuitem" views/*.xml | wc -l
echo
echo "### P-09b VIEWS (ir.ui.view records)"
grep -rh "model=\"ir.ui.view\"" views/*.xml | wc -l
echo "-- views naming Wave A models --"
for m in account.account account.journal account.move account.move.line account.full.reconcile account.partial.reconcile account.lock_exception account.group; do
  n=$(grep -rh -A4 "model=\"ir.ui.view\"" views/*.xml | grep -c "\"model\">$m<")
  printf "%-28s views=%s\n" "$m" "$n"
done
echo
echo "### P-10/P-11 WINDOW ACTIONS (ir.actions.act_window)"
grep -rh "model=\"ir.actions.act_window\"" views/*.xml wizard/*.xml 2>/dev/null | wc -l
echo
echo "### P-12 SERVER ACTIONS / buttons: type=\"object\" in Wave A views"
grep -rhoE "type=\"object\" name=\"[a-z_0-9]+\"|name=\"[a-z_0-9]+\" type=\"object\"" views/*.xml | wc -l
