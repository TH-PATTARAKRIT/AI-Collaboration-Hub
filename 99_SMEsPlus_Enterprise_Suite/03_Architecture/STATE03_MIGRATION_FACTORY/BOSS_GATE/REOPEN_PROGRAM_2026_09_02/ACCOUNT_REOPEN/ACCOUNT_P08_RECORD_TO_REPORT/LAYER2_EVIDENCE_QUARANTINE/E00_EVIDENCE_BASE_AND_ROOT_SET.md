# E00 — EVIDENCE BASE AND ROOT SET (LAYER 2 — AUDIT QUARANTINE)

**Distribution: Boss / PMO / AI-Audit only.** This file carries reference-source paths, symbols and line citations. It must not be transcribed into any downstream reference or design package. Layer 1 files cite `EV-*` identifiers, never these locations.

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`

## 1. Root set — the declared 22

PATTERN: `find /Volumes/iMacSys -type f -path "*/addons/base/models/res_currency.py"` → strip `/addons/base/models/res_currency.py` → `sort`
UNIT: one core root · DENOMINATOR: **22**

```
CLAUDE AI/MIGRATION/ODOO18/18.0.1/odoo                                  804 mod  v18
CLAUDE AI/MIGRATION/ODOO18/18.0.2_community_enterprise/odoo             802 mod  v18
CLAUDE AI/MIGRATION/ODOO18/18.0.3_smeplus/odoo                          498 mod  v18
CLAUDE AI/MIGRATION/ODOO18/enterprise                                  1420 mod  v18
CLAUDE AI/MIGRATION/ODOO18/odoo-18.0+e.20250608/odoo                    792 mod  v18
CLAUDE AI/MIGRATION/ODOO18/odoo-18.0.post20260605/odoo                  456 mod  v18
CLAUDE AI/MIGRATION/ODOO18/odoo-18_community                            447 mod  v18
CLAUDE AI/MIGRATION/SMEsPlus19/02_enterprise                            804 mod  v19
CLAUDE AI/SMEsPlus/SMEsPlus18/01_base_community                         454 mod  v18
CLAUDE AI/SMEsPlus/SMEsPlus19/SMEsPlus/odoo-19.0+e.20260417/odoo        1433 mod  v19
CLAUDE AI/SMEsPlus/SMEsPlus_19.0.20260418/.../odoo-19.0+e.20260417/odoo 1433 mod  v19
CLAUDE AI/SMEsPlus/SMEsPlus_19.0.20260418/.../Odoo19 community to SMEsPlus 474 mod v19
CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo            [TARGET ROOT]  790 mod  v18
ODOO/ODOO-COMMUNITY/ODOO19                                             1399 mod  v19
ODOO/ODOO-COMMUNITY/Odoo18/t8master                                    1273 mod  v18
ODOO/ODOO-COMMUNITY/Odoo18/t8master/smeplus-server                      638 mod  v18
ODOO/ODOO-COMMUNITY/Odoo18/t8master/smeplus-server/odoo                 636 mod  v18
ODOO/ODOO-COMMUNITY/Odoo18/t8master/smeplus-server/odoo_old              28 mod  v18
ODOO/ODOO-COMMUNITY/SMEsPlus19/SOURCE CODE                             1421 mod  v19
ODOO/ODOO-COMMUNITY/SMEsPlus19/enterprise                              1420 mod  v19
ODOO/ODOO-COMMUNITY/SMEsPlus19/odoo-19.0+e.20260312/odoo                1421 mod  v19
ODOO/SOURCE CODE/ODOO 18/odoo-18.0.post20260605/odoo                    682 mod  v18
```
All paths relative to `/Volumes/iMacSys`. Rows 16–18 are nested inside row 15/16. Version split 13 v18 / 9 v19.

## 2. Target root population

REF18 = `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons`
CORE  = `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo`
CUST18 = `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/smeplus-custom/addons`

| Population | Pattern | Count |
|---|---|---|
| modules with a manifest | `find REF18 -maxdepth 2 -name __manifest__.py` | 790 |
| manifests parsed by `ast.literal_eval` without error | script | 790 / 790 |
| direct dependents of `account` | parsed `depends` | 37 |
| transitive dependents of `account` | reverse closure | 334 |
| localization modules | `find REF18 -maxdepth 1 -type d -name 'l10n_*'` | 2 (`l10n_th`, `l10n_th_reports`) |
| distinct model names declared | `grep -rEh "^\s*_name = ['\"]"` → unique | 1533 |
| models named `account.*` | same, filtered | 131 |
| custom modules with a manifest | `find CUST18 -maxdepth 2 -name __manifest__.py` | 65 |
| custom modules referencing the ledger entry model | `grep -rl "account\.move" --include=*.py CUST18` | 21 |

## 3. Root-set-wide scans

| ID | Pattern | Result |
|---|---|---|
| `RS-A-01` | `grep -rEho "_name = ['\"][a-z_.]*event[a-z_.]*['\"]" --include=*.py <root>` per root, dedup, framework/marketing namespaces excluded | 0 accounting-event models in 22/22; residual in 9 roots is `report.event_iot.event_registration_badge_printer_report` |
| `RS-A-02` | `grep -rEho "_name = ['\"]account\.period['\"]\|_name = ['\"][a-z_.]*accounting.period[a-z_.]*['\"]" --include=*.py <root>` | 0 in 22/22 |
| `RS-A-03` | `grep -rEl "CHECK ?\(.*(sum\|SUM).*(debit\|credit\|balance)" --include=*.py <root>` | 0 files in 22/22 |
| `RS-B-01` | `grep -rEli "year.end closing (entry\|move)\|closing_move\|result_appropriation\|carry.?forward.*earning" --include=*.py <root>` | 0 in 7 roots, 3 in 1, 8–9 in 5, 19 in 1, 24 in 8 — **not promoted**, vocabulary pattern |
| `RS-P-01` | `grep -rn "COALESCE((%s), (%s), 1.0)" --include=res_currency.py <root>` | present in 21/22; absent only in the 28-module partial tree |

Script retained at `/tmp/rootscan.sh` for the session; reproduced from the pattern text above.

## 4. Literal patterns behind the Layer 1 identifiers

| Ref | Literal pattern |
|---|---|
| `EV-P-01` | `find <root>/addons -maxdepth 2 -name "__manifest__.py"` |
| `EV-P-02` | `ast.literal_eval` over each `__manifest__.py` |
| `EV-P-03` | `find <REF18> -maxdepth 1 -type d -name 'l10n_*'` |
| `EV-P-04` | `grep -rEh "^\s*_name = ['\"]account\." --include="*.py" <REF18>` → extract → `sort -u` |
| `EV-P-05` | `grep -rEho "_name = ['\"][a-z_.]*event[a-z_.]*['\"]" --include="*.py" <root>` per root → dedup → exclude `event.*`, `website.event*`. Residual non-marketing matches across the set: `calendar.event`, `calendar.event.type`, `barcodes.barcode_events_mixin`, and in 9 roots a `report.event_iot.*` print model. None accounting. |
| `EV-P-06` | `grep -rEho "_name = ['\"]account\.period['\"]\|_name = ['\"][a-z_.]*accounting.period[a-z_.]*['\"]" --include="*.py" <root>` |
| `EV-P-07` | (i) `grep -rEl "CHECK ?\(.*(sum\|SUM).*(debit\|credit\|balance)" --include="*.py" <root>` ; (ii) `grep -rEl "CREATE (OR REPLACE )?TRIGGER" --include="*.py" --include="*.sql" <root>` ; (iii) `grep -rEl "DEFERRABLE\|EXCLUDE USING" --include="*.py" --include="*.sql" <root>` restricted to accounting tables. Exclusion-constraint capability demonstrated elsewhere in the framework at `hr_work_entry/models/hr_work_entry.py:58` (`EXCLUDE USING GIST`). |
| `EV-P-08` | Partner-merge raw-SQL path: `base/wizard/base_partner_merge.py` `_merge` → `_update_foreign_keys` → `_update_foreign_keys_generic('res.partner', …)`, raw `UPDATE "<table>" SET "<column>"`, skipping only tables named `base_partner_merge_*`. `account_move_line.partner_id` is a stored `Many2one` with `ondelete='restrict'` and is repointed. Refusal set in `_merge`: >3 contacts, parent/child relation, >1 linked user, differing e-mail (**auto-disabled for an administrator caller**). Five wizard definitions in the target root: `base`, `mail`, `website`, `loyalty`, `account`. |
| `EV-P-09` | Retention cannot be disabled once entries exist: `account/models/company.py:317-322 _check_audit_trail_records` raises when `check_account_audit_trail` is false and any move exists for the company. |
| `EV-P-10` | Deletion log gated on the flag: `account/models/account_move.py:3304-3312 _get_unlink_logger_message` filters `m.posted_before and m.company_id.check_account_audit_trail`; the `if not self._context.get('force_delete'): pass` at `:3307-3308` is dead code. |
| `EV-P-11` | Settlement item references: `account/models/account_partial_reconcile.py:14-19` — `debit_move_id` / `credit_move_id`, `required=True`, no explicit `ondelete` → framework default for required = `RESTRICT` (`odoo/fields.py:3189-3197`). |
| `EV-P-12` | Warehouse-manager grant on the settlement record: `sale_stock/security/ir.model.access.csv:14` — `1,1,1,1` on `account.partial.reconcile` to `stock.group_stock_manager`. |
| `EV-P-13` | Unconditional item-deletion audit record: `account/models/account_move_line.py:1709-1721` — `move._message_log("Journal Item %s deleted", tracking_value_ids=…)` for any move with `posted_before`, independent of the retention flag. |

## 5. Corrections to §1 and §3 after independent review

| Item | Correction |
|---|---|
| Version split | **14 on the 18 line, 8 on the 19 line** (draft said 13/9). Product line is readable from a version file in **14 of 22** roots; the other 8 — `R-04`, `R-07`, `R-08`, `R-09`, `R-12`, `R-14`, `R-19`, `R-20` — are **INFERRED from directory naming** and are marked so. |
| `RS-A-01` residual | Non-marketing matches across the set are `calendar.event`, `calendar.event.type`, `barcodes.barcode_events_mixin`, plus a print-report model in 9 roots. None accounting. |
| `RS-P-01` | **Inverted in the draft.** `R-18` (`ODOO/ODOO-COMMUNITY/Odoo18/t8master/smeplus-server/odoo_old`) — file **present and complete** (22 847 bytes, dated 2024-10-04), holding an **older two-tier resolver**: `COALESCE((SELECT r.rate … WHERE r.currency_id = c.id AND r.name <= %s AND (r.company_id IS NULL OR r.company_id = %s) ORDER BY r.company_id, r.name DESC LIMIT 1), 1.0)` at `addons/base/models/res_currency.py:121-135`. Therefore: **parity present 22/22**; **earliest-rate-ever tier present 21/22, absent in `R-18`**. |
| `RS-A-03` | A reviewer widened the pattern to **all file types**, not only program files, across all 22 roots: still **0**. The `.sql` / trigger / migration-script surface remains `C NOT YET SEARCHED` — candidate files exist in 7 roots and were not opened. |
