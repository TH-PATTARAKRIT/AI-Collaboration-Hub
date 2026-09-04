#!/bin/bash
B="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account"
cd "$B"
echo "### P-16 SECURITY — ir.model.access.csv rows total"
tail -n +2 security/ir.model.access.csv | grep -c . 
echo "-- Wave A model access rows --"
tail -n +2 security/ir.model.access.csv | grep -E "model_account_(account|journal|move|move_line|full_reconcile|partial_reconcile|lock_exception|group|root|code_mapping|account_tag)($|,)" | wc -l
echo
echo "### P-16b RECORD RULES (ir.rule) in security/*.xml"
grep -h "model=\"ir.rule\"" security/*.xml | wc -l
echo "-- record rules referencing Wave A models --"
grep -oE "<record id=\"[a-z_0-9]+\" model=\"ir.rule\">" security/*.xml | wc -l
echo "-- rule ids --"
grep -oE "record id=\"[a-z_0-9]+\" model=\"ir.rule\"" security/*.xml | sed 's/record id="//;s/" model="ir.rule"//' 
