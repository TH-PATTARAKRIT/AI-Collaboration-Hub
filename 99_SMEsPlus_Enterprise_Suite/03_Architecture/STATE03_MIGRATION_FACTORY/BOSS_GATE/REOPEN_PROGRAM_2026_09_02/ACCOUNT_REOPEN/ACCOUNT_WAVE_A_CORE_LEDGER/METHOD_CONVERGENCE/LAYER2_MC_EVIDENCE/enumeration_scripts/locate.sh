#!/bin/bash
B="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account"
BASE="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/base"
MODELS="account.account account.account.tag account.group account.root account.code.mapping account.journal account.journal.group account.move account.move.line account.full.reconcile account.partial.reconcile account.lock_exception account.financial.year.op sequence.mixin account.move.reversal account.resequence.wizard account.automatic.entry.wizard account.secure.entries.wizard account.merge.wizard account.merge.wizard.line validate.account.move"
for m in $MODELS; do
  hit=$(grep -rn "_name = '$m'" "$B" 2>/dev/null | head -1)
  if [ -z "$hit" ]; then hit=$(grep -rn "_name = \"$m\"" "$B" 2>/dev/null | head -1); fi
  f=$(echo "$hit" | cut -d: -f1)
  loc=""
  if [ -n "$f" ]; then loc=$(wc -l < "$f" | tr -d ' '); fi
  printf "%-34s %s  [LOC %s]\n" "$m" "$(echo "$hit" | sed "s|$B/||" | cut -d: -f1,2)" "$loc"
done
echo "--- base currency models ---"
grep -rn "_name = 'res.currency" "$BASE/models/res_currency.py" 2>/dev/null
