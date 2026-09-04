#!/bin/bash
AD="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons"
echo "### Bounding the negative claim: any ir.rule for reconcile models ANYWHERE in the addons tree?"
echo "-- addons dir count --"; ls "$AD" | wc -l
echo "-- grep for model_account_partial_reconcile / full_reconcile in any ir.rule context --"
grep -rl "model_account_partial_reconcile" "$AD" 2>/dev/null | head -20
echo "--- full ---"
grep -rl "model_account_full_reconcile" "$AD" 2>/dev/null | head -20
echo
echo "### Files that mention them at all (bounded scope = whole addons tree)"
grep -rn "model_account_partial_reconcile" "$AD" 2>/dev/null | head -10
