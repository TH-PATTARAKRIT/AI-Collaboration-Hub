#!/bin/bash
# P10-ENUM-01 : PATH SET PROOF
# POPULATION : every directory on this volume that can contain reference-ERP addon code
# PATTERN    : directories directly containing at least one __manifest__.py
# UNIT       : one addon directory (one module)
# PATH SET   : declared below, enumerated - NOT habit-derived
set -u
ROOTS=(
"/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608"
"/Volumes/iMacSys/CLAUDE AI/MIGRATION/ODOO18/odoo-18.0+e.20250608"
"/Volumes/iMacSys/CLAUDE AI/MIGRATION/ODOO18/odoo-18.0.post20260605"
"/Volumes/iMacSys/ODOO/SOURCE CODE/ODOO 18/odoo-18.0.post20260605"
"/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18"
"/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo14"
)
for r in "${ROOTS[@]}"; do
  if [ -d "$r" ]; then
    n=$(find "$r" -name "__manifest__.py" 2>/dev/null | wc -l | tr -d ' ')
    echo "MODULES=$n  ROOT=$r"
  else
    echo "MODULES=ABSENT  ROOT=$r"
  fi
done
