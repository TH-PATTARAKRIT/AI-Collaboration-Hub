#!/bin/bash
# P10-ENUM-02 : TIME-BASED RECOGNITION MECHANISM POPULATION
# POPULATION : every code path in the declared reference root that creates or schedules
#              an accounting entry whose DATE is derived from a period/schedule rather
#              than from a business document date
# PATTERN    : five independent selecting expressions, each declared with its own
#              false-negative mode (see P10_SCHEDULE_ENGINE_SEMANTIC_RESEARCH.md S.3)
# UNIT       : one module directory
# PATH SET   : addons/ and addons_archive/ of the declared reference root
set -u
R="/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo"
P=("$R/addons" "$R/addons_archive")
mod() { sed -E 's#.*/(addons_archive|addons)/([^/]+)/.*#\1/\2#' | sort -u; }
echo "== E1 deferral field carriers (deferred_start_date) =="
grep -rl "deferred_start_date" "${P[@]}" 2>/dev/null | grep -v "/i18n/" | mod
echo "== E2 accrual wizard model (account.accrued.orders.wizard) =="
grep -rl "account\.accrued\.orders\.wizard\|AccruedExpenseRevenue" "${P[@]}" 2>/dev/null | grep -v "/i18n/" | mod
echo "== E3 asset depreciation board (account.asset / depreciation_move_ids) =="
grep -rl "depreciation_move_ids" "${P[@]}" 2>/dev/null | grep -v "/i18n/" | mod
echo "== E4 recurring auto-post entries (_copy_recurring_entries / auto_post_origin_id) =="
grep -rl "_copy_recurring_entries\|auto_post_origin_id" "${P[@]}" 2>/dev/null | grep -v "/i18n/" | mod
echo "== E5 any other schedule-dated entry generator (spread/amortis/amortiz/rateable) =="
grep -rlE "amortis|amortiz|rateable|revenue_recognition" "${P[@]}" 2>/dev/null | grep -v "/i18n/" | mod
