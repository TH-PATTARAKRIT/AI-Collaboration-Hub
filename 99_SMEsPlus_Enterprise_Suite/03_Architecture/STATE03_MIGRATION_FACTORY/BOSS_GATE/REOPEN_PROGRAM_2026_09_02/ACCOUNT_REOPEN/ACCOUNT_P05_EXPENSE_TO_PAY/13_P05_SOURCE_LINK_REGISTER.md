# 13 — P05 SOURCE LINK REGISTER

`LAYER 2 — AUDIT QUARANTINE`
**Clean-room notice:** every citation below is a reference-ERP path. Under Clean Room Learning
Directive v2.0 Policy A these citations **must not** be transcribed into any Layer 1 reference package
or any Team B deliverable. Layer 1 output is confined to `17 §6` and `19 §1–§6`.

## 1. Repository / Branch / Commit Lineage

| Item | Value |
|---|---|
| Repository | `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub.git` |
| Canonical branch | `SMEsPlus` |
| Working branch | `research/account-p05-expense-to-pay-2026-09-04-001` |
| Branch point | `88f52cd7ba6dc40b8951c4bfc4e0016af7cbb7ad` — *governance: approve canonical evidence acquisition flow* |
| Merge policy | **Never merged.** Boss decides. |
| Peer sessions at same base | `research/account-p01-procure-to-pay-2026-09-04-001`, `...p02-order-to-cash...`, `...p03-manufacture-to-cost...` — all at `88f52cd`, no committed output at the time of writing |

## 2. Governance Documents Consulted

| Document | Path on `SMEsPlus` @ `88f52cd` |
|---|---|
| 8-Criteria Universal Exit Constitution `SMEPLUS-DR-EXIT-8C-001` | `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/SMEPLUS_VERY_DEEP_RESEARCH_8_CRITERIA_UNIVERSAL_EXIT_CONSTITUTION.md` |
| Negative Claim Standard | `99_SMEsPlus_Enterprise_Suite/00_PROJECT_STANDARD/SMEPLUS_DEEP_RESEARCH_NEGATIVE_CLAIM_STANDARD.md` |
| Method Convergence Standard | `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/SMEPLUS_DEEP_RESEARCH_METHOD_CONVERGENCE_STANDARD.md` |
| Canonical Evidence Acquisition Flow | `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/SMEPLUS_CANONICAL_EVIDENCE_ACQUISITION_FLOW_STANDARD.md` |
| AI Bootstrap Package | `bootstrap/AI_BOOTSTRAP_PACKAGE.md` |
| Repository contract + 3 registries | `repository-contract/` |
| `GB-08` Boss ruling — FX ownership & missing-rate policy | `.../ACCOUNT_REOPEN/ACCOUNT_FULL_DEEP_RESEARCH/GB08_BOSS_RULING_FX_RATE_OWNERSHIP_AND_MISSING_RATE_POLICY_2026_09_04.md` |
| Scope-Aware Constitution Correction | `SMEPLUS-26-09-04-ACC-REV2-CORR1` (session-borne; applied in `22`) |

## 3. Reference-ERP Source Roots (Layer 2 — audit quarantine)

| ID | Absolute path | Population | Denominator command |
|---|---|---|---|
| `ENT18` | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons` | 790 modules | `find <parent> -name '__manifest__.py' \| sed 's\|/[^/]*/__manifest__.py$\|\|' \| sort \| uniq -c` |
| `ARC18` | `.../odoo/addons_archive` | 959 modules | same command, same run |
| `CUSTOM` | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/smeplus-custom/addons` | 68 entries | `ls \| wc -l` |
| `LEGACY14` | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo14/addons` | 127 entries | `ls \| wc -l` |

Total `__manifest__.py` under the `ENT18` parent: **1753**.

> **Path-set caveat, recorded per the denominator rule.** Two further near-identical copies of the
> custom addon set are known to exist (`Odoo18/t8master/custom/addons`,
> `CLAUDE AI/MIGRATION/ODOO18/18.0.4_smeplus_v2/addons`) at differing version strings. This session
> read **only** the `smeplus-custom` copy. Findings about custom modules are therefore bounded to that
> copy and are **not** claims about the deployed system. See `20 U-01` (gating).

## 4. File-Level Citation Index

### 4.1 `ENT18/hr_expense`

| File | Lines cited | Findings |
|---|---|---|
| `models/hr_expense.py` | 17, 170-199, 180-188, 250-281, 467-514, 516-527, 539-541, 613-643, 676-682, 715-724, 881-968, 970-1002, 1004-1019 | `EC-02`, `DUP-01/02`, `AN-01..06`, `RI-04`, `EF-01/02/06`, `GL-01/02/03`, `P05-F-19/23/24/25` |
| `models/hr_expense_sheet.py` | 29-49, 59-65, 145-158, 183-188, 196-200, 209-237, 239-262, 264-309, 322-334, 342-368, 380-384, 386-420, 422-444, 491-509, 511-515, 570-614, 664-705, 707-744, 746-796, 798-822, 824-861, 863-865, 876-900 | `EX-02/03/06/07`, `AE-01..04`, `RI-01/02/03`, `SR-01/02/03`, `EC-01/10/11/12`, `EF-03/04/05` |
| `models/account_move.py` | 12, 15-25, 38-45, 47-49, 56-76, 85-90, 92-95, 97-103 | `EX-07`, `SR-07`, `P05-F-20/27`, `03 §3.3` |
| `models/account_move_line.py` | 12, 14-16, 24-27, 29-30 | `GL-02`, `EC-05`, `P05-F-21` |
| `models/account_payment.py` | 11-18, 20-28, 49-52 | `C-01`, `EF-16`, `TZ-04` |
| `wizard/account_payment_register.py` | 13-22, 24-31, 33-41 | `SR-05`, `EF-17`, `P05-F-new-02` |
| `security/` | assigned to Expert 1 | `16 §4` |

### 4.2 `ENT18/account`

| File | Lines cited | Findings |
|---|---|---|
| `models/account_move.py` | 3202-3281 (`write`), 5153-5161 (`action_register_payment`) | `EC-13`, `P05-F-29` (disproof) |
| `models/account_move_line.py` | 91 (`move_type`), 1112-1124 (`action_register_payment`) | `P05-F-29` (disproof) |

### 4.3 `CUSTOM/hr_expense_petty_cash`

| File | Lines cited | Findings |
|---|---|---|
| `models/petty_cash.py` | 7-49, 12-33, 34-36, 38-49 | `TZ-02`, `22 §3 R-02`, `EF-07` |
| `models/hr_expense.py` | 11-14, 32-52, 64-70, 72-79 | `TZ-01`, `EX-04`, `EF-12` |
| `models/hr_expense_sheet.py` | 13-33, 35-52, 55-83, 86-122, 125-131, 134-158 | `EF-07`, `EF-08`, `EF-13`, `P05-F-05` |
| `models/account_move.py` | 12-16, 18-20, 22-88, 90-111, 113-151 | `AE-08`, `05 §5` |
| `models/account_invoice.py` | whole file | `P05-F-04` — not imported by `models/__init__.py` |
| `models/__init__.py` | whole file (4 imports) | `P05-F-04` |
| `security/ir.model.access.csv` | 2 | `TZ-02` |

### 4.4 `CUSTOM/scgl_advance_expense_request`

| File | Lines cited | Findings |
|---|---|---|
| `models/advance_expense_request.py` | 16-33, 41-64, 88-120, 122-149, 151-176, 183-199, 201-216, 218-237, 239-289, 291-302, 311-337, 358-369 | `EX-01`, `AE-05`, `GL-04`, `RI-05/06/07`, `EF-09/10/18`, `P05-F-07/10/11/12/13` |
| `models/advance_expense_request_line.py` | 14-16, 100-104, 109-134 | `02 §3`, `P05-F-new` |
| `models/account_move.py` | 10-12, 14-32, 45-56, 58-114, 118-122 | `GL-05`, `EF-11`, `AE-06` |
| `models/hr_employee.py` | 4-7 | `EF-18` |
| `models/product_template.py` | 7-12 | `02 §3` |
| `wizard/advance_request_reconcile.py` | 6-49, 52-92 | `AE-06/07`, `GL-05/06/07`, `SR-04`, `EF-09/11` |
| `wizard/advance_request_rejected.py` | 5-16 | `EX-08`, `EC-11` |
| `security/ir.model.access.csv`, `security/advance_request_security.xml` | whole files | `22 §2`, `16 §4` |

### 4.5 `CUSTOM/l10n_th_withholding_tax` (+ satellites)

| File | Lines cited | Findings |
|---|---|---|
| `models/account.py` | 8-15, 18-36, 38-64, 66-72 | `07` |
| `models/account_move.py` | 6-22, 23-42, 45-58 | `P05-F-14/15/16/17`, `EF-14` |
| `models/account_withholding_tax.py` | 7-32, 26 | `SC-01`, `22 §3 R-03` |
| `models/account_payment.py`, `models/product.py` | whole files | `07` |
| `wizard/account_payment_register.py` | 10-26, 28-72, 74-93 | `AE-09`, `EF-15`, `P05-F-18` |
| `security/ir.model.access.csv:2`, `security/security.xml:2-4` | as cited | `P05-F-30` (disproof) |

## 5. Runtime / Database Evidence

| Item | Status |
|---|---|
| Live database access this session | **NONE.** No connection was attempted or available. |
| Runtime ORM dumps | Known to exist for the **Asset** domain (`~/Downloads/occ_asset_trace_output.txt` and siblings, captured 2026-08-26 against `idemo18_uat`). **No P05-equivalent dump exists.** |
| Consequence | Every behavioural claim in this package is derived from **source reading**, not from observed runtime. Claims marked `SUPPORTED INTERPRETATION` are exactly those that a runtime trace would settle. Recorded as `20 U-02` (gating for `EC-02` convergence). |

## 6. Reproducibility

All enumeration commands used in this package are stated inline with their **path set and pattern**,
per the denominator rule. The AST evaluation behind `C-01` is reproduced verbatim in `14 §3` so a
reader can re-run it without re-deriving it.
