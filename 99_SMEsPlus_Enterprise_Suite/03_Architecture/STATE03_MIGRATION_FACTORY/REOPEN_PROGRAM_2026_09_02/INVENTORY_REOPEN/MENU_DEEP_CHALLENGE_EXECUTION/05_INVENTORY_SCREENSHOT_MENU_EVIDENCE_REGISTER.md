# 05 — Inventory Screenshot Menu Evidence Register

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub` | Canonical Branch: `SMEsPlus` | Execution Branch: `audit/inventory-menu-deep-challenge-2026-09-02-001`
Status: `CP-02 OUTPUT — SCREENSHOT MENU EVIDENCE REGISTER — NOT A GATE DECISION`
Clean-room boundary: benchmark menu labels are recorded here as `MENU COVERAGE CHECKLIST` evidence only. No label below is an approved SMEsPlus name.

---

## 1. Evidence Source Statement

| Item | Finding |
|---|---|
| Boss screenshot image files | **Not present** in the repository (`git ls-tree origin/SMEsPlus` returns no inventory-menu image), not present in the session working area, not present in `~/Downloads` or `~/Desktop` for 2026-09-01/02. |
| Evidence of record used by this session | The menu enumeration transcribed by Boss/PMO into §4 of `04_NEW_SESSION_PROMPT_SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001.md` (29 menu items in 4 groups). This session treats that transcription as the screenshot evidence of record. |
| Evidence status | `TRANSCRIBED — IMAGE ARCHIVE HOLD / EVIDENCE REQUIRED`. The transcription is sufficient for menu coverage; the image files should still be archived under the BOSS_GATE folder so the evidence chain does not depend on a chat attachment. |
| Independent cross-check performed | Layer 2 quarantine source (module/view inventory export `Evidence_CSV/XML_View_Action_Menu_Inventory.csv`, canonical V2.0 handoff package) was opened only to confirm that the inventory module family exists in the reference evidence set. No menu XML, view, or action content was read into any Layer 1 deliverable. |
| Benchmark version caveat | The screenshot menu tree is consistent with a current-generation Odoo-style Inventory application. Exact version is `UNKNOWN / EVIDENCE REQUIRED`; version differences affect sub-menu placement (for example Replenishment and Run Scheduler visibility depends on settings), not business meaning. |

---

## 2. Screenshot Menu Enumeration (evidence of record)

| Menu ID | Group | Benchmark label (as transcribed) | Screenshot order | Visible by default in benchmark? | Evidence status |
|---|---|---|---|---|---|
| MENU-OP-01 | Operations | Replenishment | 4.1.1 | Conditional (appears when replenishment planning is enabled) | TRANSCRIBED |
| MENU-OP-02 | Operations | Inventory Adjustments | 4.1.2 | Yes | TRANSCRIBED |
| MENU-OP-03 | Operations | Transfers | 4.1.3 | Yes (receipts / deliveries / internal grouped) | TRANSCRIBED |
| MENU-OP-04 | Operations | Scrap | 4.1.4 | Yes | TRANSCRIBED |
| MENU-OP-05 | Operations | Landed Costs | 4.1.5 | Conditional (feature switch) | TRANSCRIBED |
| MENU-OP-06 | Operations | Run Scheduler | 4.1.6 | Conditional (developer/advanced mode) | TRANSCRIBED |
| MENU-PR-01 | Products | Products | 4.2.1 | Yes | TRANSCRIBED |
| MENU-PR-02 | Products | Product Variants | 4.2.2 | Conditional (variants switch) | TRANSCRIBED |
| MENU-PR-03 | Products | Lots/Serial Numbers | 4.2.3 | Conditional (tracking switch) | TRANSCRIBED |
| MENU-RP-01 | Reporting | Stock | 4.3.1 | Yes | TRANSCRIBED |
| MENU-RP-02 | Reporting | Locations | 4.3.2 | Conditional (multi-location switch) | TRANSCRIBED |
| MENU-RP-03 | Reporting | Moves History | 4.3.3 | Yes | TRANSCRIBED |
| MENU-RP-04 | Reporting | Stock Moves | 4.3.4 | Conditional (advanced mode) | TRANSCRIBED |
| MENU-RP-05 | Reporting | Valuation | 4.3.5 | Conditional (stock accounting bridge installed) | TRANSCRIBED |
| MENU-RP-06 | Reporting | Warehouse Analysis | 4.3.6 | Conditional (advanced/enterprise reporting) | TRANSCRIBED |
| MENU-CF-01 | Configuration | Settings | 4.4.1 | Yes | TRANSCRIBED |
| MENU-CF-02 | Configuration | Warehouses | 4.4.2 | Yes | TRANSCRIBED |
| MENU-CF-03 | Configuration | Locations | 4.4.3 | Conditional (multi-location switch) | TRANSCRIBED |
| MENU-CF-04 | Configuration | Routes | 4.4.4 | Conditional (multi-step routes switch) | TRANSCRIBED |
| MENU-CF-05 | Configuration | Rules | 4.4.5 | Conditional (advanced mode) | TRANSCRIBED |
| MENU-CF-06 | Configuration | Operations Types | 4.4.6 | Yes | TRANSCRIBED |
| MENU-CF-07 | Configuration | Storage Categories | 4.4.7 | Conditional (storage category switch) | TRANSCRIBED |
| MENU-CF-08 | Configuration | Putaway Rules | 4.4.8 | Conditional (multi-location switch) | TRANSCRIBED |
| MENU-CF-09 | Configuration | Product Categories | 4.4.9 | Yes | TRANSCRIBED |
| MENU-CF-10 | Configuration | Attributes | 4.4.10 | Conditional (variants switch) | TRANSCRIBED |
| MENU-CF-11 | Configuration | Product Packagings | 4.4.11 | Conditional (packaging switch) | TRANSCRIBED |
| MENU-CF-12 | Configuration | Reordering Rules | 4.4.12 | Yes (under Operations or Configuration by version) | TRANSCRIBED |
| MENU-CF-13 | Configuration | Barcode Nomenclatures | 4.4.13 | Conditional (barcode switch) | TRANSCRIBED |
| MENU-CF-14 | Configuration | UoM Categories | 4.4.14 | Conditional (UoM switch) | TRANSCRIBED |

Total: **29 menu items** (6 Operations + 3 Products + 6 Reporting + 14 Configuration).

---

## 3. Menus Present in Benchmark Practice but Absent from the Screenshot Transcription

Recorded so the coverage register is not silently narrower than the benchmark. None of these is added to SMEsPlus scope by this session (Charter §9: challenge cannot silently add scope).

| Candidate | Why it matters for Thai SMEsPlus | Disposition |
|---|---|---|
| Receipts / Deliveries / Internal as separate operation entries | Thai warehouse staff think in รับเข้า / จ่ายออก / โอนภายใน, not in one generic "Transfers" list | Covered inside MENU-OP-03 process map (06) as sub-flows; naming register (17) proposes split labels |
| Physical Inventory / Count sheets | Thai year-end stock count (ตรวจนับสินค้าประจำปี) with auditor witness | Covered inside MENU-OP-02 as count sub-flow |
| Returns (customer / vendor) | Common Thai SME exception; benchmark handles via reverse transfer | Covered inside MENU-OP-03 exception path; carried as `GAP-MD-07` |
| Packages / Package types | Only when package tracking enabled | Noted in 09 (packaging) as conditional; not a screenshot menu |
| Quality / Dropship / Batch picking | Optional benchmark add-ons | `NOT APPLICABLE` to this study; noted for completeness only |
| Batch/wave transfers | Enterprise-grade picking | `NOT APPLICABLE` to this study |

---

## 4. Evidence Register per Menu Group

| Group | Prior study depth (reopen package `170af9ea`) | Menu-level depth available before this session | Delta this session |
|---|---|---|---|
| Operations | Deep on movement semantics, adjustment/count freeze (`N-A7-01`), scrap model, returns wizard; landed cost named "never read" (deliverable `15` §D) | Semantics yes; menu purpose/input/output/Thai user flow **no** | Menu-level process reconstruction (06), impact matrix (07), Thai names (17) |
| Products | Product type routing deep-proof (`12`); variants "not separately researched" (`02` item 2); lots/serial constraint facts | Variants gap explicit | Menu-level product/variant/lot maps (09) |
| Reporting | Valuation report export defect (`G-7`); no dedicated reporting study | Reporting **never studied menu-by-menu** | Reporting map (16) with operational / management / audit / accounting-support split |
| Configuration | Warehouse regeneration risk (`SAAS-04`), location usage enumeration, route dispatch, category dual ownership; storage categories, putaway, packaging, barcode nomenclature, UoM categories **never studied** | Partial | Configuration foundation map (08), warehouse/route/rule map (10) |

---

## 5. Register Statement

All 29 screenshot menus are carried into `02_INVENTORY_MENU_COVERAGE_REGISTER.md`, `06_INVENTORY_MENU_BY_MENU_PROCESS_MAP.md`, `07_INVENTORY_MENU_IMPACT_MATRIX.md` and `17_THAI_MENU_AND_REPORT_NAMING_REGISTER.md` with the Menu IDs above. Image archive remains `HOLD / EVIDENCE REQUIRED` until Boss or PMO commits the screenshot files to the BOSS_GATE evidence folder.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
