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
