# A1 — SOURCE LANDSCAPE

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-28-MIG-A-EXPERT-DR-001 |
| Date | 2026-08-28 |
| Phase | A1 — Full Source Forensic Inventory (L0–L1 depth achieved; L2 seeded) |
| Method | Read-only scan (AST manifest parse, 93,859 files walked) + 13-agent parallel forensic analysis + prior-baseline reconciliation |
| Status | EVIDENCE PACK PREPARED — inventory closed at metadata level |

## 1. What the Source System IS (one paragraph, evidence-backed)

The source is a **customer deployment of Odoo 19.0 Enterprise** (official `odoo/enterprise`
addons tree — 744 OEEL-1 + 706 LGPL-3 modules — split by the customer into an accounting
partition `01 ACCOUNT` (62 modules) and the remainder `02 OTHER` (1,371)), extended by
**69 customer/third-party modules** (`addons_extra`: SMEsPlus-authored customs, Thai
localization stack, OCA modules — some locally forked — and purchased proprietary modules) plus
**2 purchased Ksolves dashboard modules**, with one **PostgreSQL 18.4 custom-format database
dump** of database `iTEST02` (snapshot 2026-06-14). Deep Thai capability (WHT certificates,
PND reports, PromptPay, RD VAT lookup, Thai cheque/voucher printing) is implemented in the
customer layer, not the vendor layer (vendor ships only `l10n_th` + `l10n_th_reports`).

## 2. Source Landscape (L0)

| # | Source | Type | Scale | Register |
|---|---|---|---:|---|
| S-01 | `SOURCE CODE/01 ACCOUNT` | Odoo 19 Enterprise accounting partition | 62 modules / 5,553 files | MODULE_MASTER_REGISTER.md §3 |
| S-02 | `SOURCE CODE/02 OTHER` | Odoo 19 Enterprise remainder (community+enterprise) | 1,371 modules / 85,444 files | MODULE_MASTER_REGISTER.md §4 |
| S-03 | `SOURCE CODE/addons_extra` | Customer customization layer | 69 modules / 2,393 files | MODULE_MASTER_REGISTER.md §5 |
| S-04 | `SOURCE CODE/ks_dashboard_ninja` + `ks_dn_advance` | Purchased dashboard suite (Ksolves, OPL-1) | 2 modules / 469 files | MODULE_MASTER_REGISTER.md §5 |
| S-05 | `iTEST02_2026-06-14_14-41-19.dump` | PostgreSQL 18.4 custom dump | 65.4 MB; 13,942 known column rows (prior register) | DATABASE_DUMP_REGISTER.md |
| S-06 | 6 zip archives + Working Pack zip | Chain-of-custody archives (all with extracted counterparts verified via `unzip -l`) | 804 MB umbrella + 5 area zips | SOURCE_MANIFEST.md |
| S-07 | `ACCOUNT/03 DATABASE` V1.1–V2.0 | Mapping/documentation pack versions (NOT dumps) | 162+ files incl. Dump_Table_Inventory.csv, Source_to_Dump_Mapping_Validation.csv | DATABASE_DUMP_REGISTER.md §3 |
| S-08 | `ACCOUNT/04 FLOWCHART_BPMN` | BPMN Evidence Controlled Diagram Pack v2.2 | 62 items | supporting evidence (P5) |
| S-09 | Project documents (Constitution v1.0, Accounting Module Overview, Technical Review, Working Pack Report, SaaS Architecture Review, AI Collab Framework v2.3, UX Blueprint v2.4) | Customer/project documents | 10+ docs | supporting evidence (P5) |
| S-10 | STEP03xx/STEP04xx evidence packs + `06 MIGRATION FACTORY` prior Team A workspace | Approved prior evidence chain | ~186k files (incl. STEP040301 source snapshot 157,849 files) | SOURCE_BASELINE_RECONCILIATION.md |

## 3. Key Verified Facts

1. **1,504 modules** total; zero manifest parse errors; zero cross-area duplicate names;
   count reconciled to every prior baseline (see SOURCE_BASELINE_RECONCILIATION.md §1).
2. `01 ACCOUNT` ∪ `02 OTHER` = one Odoo 19.0 Enterprise addons tree (disjoint partition, proven
   by name-set and dependency evidence).
3. Dump created by **pg_dump 18.4 / PostgreSQL 18.4**; both file copies byte-identical
   (SHA-256 verified); Odoo accounting schema + Thai WHT customization tables visible in
   read-only header probe.
4. Licensing: 744 OEEL-1 (proprietary enterprise) + 17 OPL-1 + 2 other proprietary + 12
   UNDECLARED → **large proprietary surface; clean-room quarantine control remains critical**.
5. Customer layer contains **11 external integrations** (2C2P, Monday.com, JasperReports,
   Redis sessions, Thai RD VAT service, GeoNames, PromptPay QR, OpenRouter/DeepSeek LLM,
   multi-cloud DB backup, plus file-based Excel/AXIS import bridge).
6. Source copies came from a **running deployment** (compiled `.pyc` files present in customer
   layers) — configuration/data behavior in the dump is therefore expected to reflect real usage.
7. Prior approved research scope = **134 modules** (THAILAND_CORE / BOSS_EXTRA /
   CORE_DEPENDENCY) with 31 metadata-only and 19 permanently-black-box constraints; 591 distinct
   models already extracted under that scope (STEP040304R4, Boss-approved).

## 4. Working Domain Index (research index only — NOT product scope)

Evidence-derived candidate research domains, seeded from the 134-module scope grouping, the
62-module accounting clusters, the 69-module customer layer, and the dump schema families:

| # | Working domain | Primary evidence anchors |
|---|---|---|
| D-01 | Accounting core (GL/journal/posting) | `account`, `account_accountant`, dump `account_*` tables |
| D-02 | AR / AP / Payments | payments cluster (11 modules), `account_payment*`, 2C2P, PromptPay |
| D-03 | Tax & Thai statutory (VAT / WHT / PND) | 21 Thai-relevant customer modules, `l10n_th*`, WHT cert tables in dump |
| D-04 | Bank & statement reconciliation | bank import cluster (6), online sync |
| D-05 | Assets & loans | `account_asset`, `account_loans`, `smesplus_advance_expense_request` |
| D-06 | Reporting & statutory reports | `account_reports`, `smesplus_account_reports`, `l10n_th_reports*`, Jasper/XLSX report stack |
| D-07 | Sales | `sale*` (58), customer sale customs (6) |
| D-08 | Purchase & procurement approval | `purchase*` (12), `purchase_request`, multi_level_approval suite |
| D-09 | Inventory / Warehouse | `stock*` (22), customer inventory customs |
| D-10 | MRP / Manufacturing | `mrp*` (24) |
| D-11 | Product & UoM | `product*`, `smesplus_uom_ext`, product customs (5) |
| D-12 | Partner / Contact | `partner*` customs, `l10n_th_partner`, RD VAT lookup |
| D-13 | Approval workflow (cross-cutting) | multi_level_approval family |
| D-14 | Dashboards & BI | ks_dashboard_ninja suite |
| D-15 | Security / Access | `smesplus_special_access_rights`, vendor security model |
| D-16 | Integration & system infra | Monday.com connector, Redis session, backup, import bridges |
| D-17 | HR-Expense bridge | `hr_expense`, accountant_hr_expense, advance expense request |

## 5. Recommended Research Order (proposal — Boss decides)

Ranking criteria per directive §83: dependency centrality · accounting criticality · migration
criticality · data dependency · evidence availability.

1. **D-01 Accounting core** — maximal dependency centrality (every financial domain posts into
   it; dump evidence richest here; prior 591-model extraction covers it).
2. **D-03 Tax & Thai statutory** — highest regulatory risk; almost entirely customer-layer code
   (= the least documented, most migration-critical layer); S1 Thai statutory report dependency
   already flagged open at STATE03 level.
3. **D-02 AR/AP/Payments** — direct money movement, 2C2P/PromptPay integrations, feeds D-01.
4. **D-06 Reporting & statutory reports** — consumes D-01/D-03; Jasper/XLSX custom stack.
5. **D-07/D-08/D-09 transactional domains** (Sales → Purchase/Approval → Inventory) — they
   generate the accounting facts; approval workflow is deeply customized.
6. Remaining domains (D-04, D-05, D-10…D-17) ordered by evidence availability thereafter.

Rationale for Accounting-first: consistent with prior evidence (STEP040302 Thailand filter kept
accounting at core; Board06 mandate is Data & Canonical Model; dump is accounting-dominant).

## 6. Coverage Metrics (denominators measured this session)

| Metric | Value |
|---|---|
| Source files inventoried / discovered | 93,859 / 93,859 (extracted areas; archives registered by listing) |
| Modules inventoried / discovered | 1,504 / 1,504 (metadata level) |
| Modules deep-researched (row-level forensic) / total | 133 (69 + 62 + 2) / 1,504 — vendor-standard remainder governed by 134-module approved scope |
| DB objects inventoried / discovered | 0 fresh this session (file-level only); prior register: 13,942 column rows carried forward |
| Domains identified / deep-researched | 17 / 0 (A4 not yet begun) |
| Critical findings registered | see registers; unknowns: 9 (UNKNOWN register) |
| Quarantine items | 12 CLASS-D carry-forward + Class E/F controls active |

No "COMPLETE" claim is made for research; **inventory closure at metadata level only**.
