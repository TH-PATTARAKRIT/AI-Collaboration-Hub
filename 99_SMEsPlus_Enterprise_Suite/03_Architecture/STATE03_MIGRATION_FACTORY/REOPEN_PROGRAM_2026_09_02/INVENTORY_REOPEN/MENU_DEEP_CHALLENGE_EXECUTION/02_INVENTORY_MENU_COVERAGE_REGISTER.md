# 02 — Inventory Menu Coverage Register

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub` | Canonical Branch: `SMEsPlus` | Execution Branch: `audit/inventory-menu-deep-challenge-2026-09-02-001`
Status: `CP-02 OUTPUT — MENU COVERAGE REGISTER — NOT A GATE DECISION`
Clean-room boundary: benchmark labels are coverage-checklist evidence only. Thai names are candidates only. Nothing here approves a SMEsPlus UI label, schema, or workflow.

---

## 1. Classification Rules Used

| Classification | Meaning for Thai SMEsPlus |
|---|---|
| `MANDATORY` | Every Thai SME tenant that manages stock needs this capability from day one, even if the UI hides advanced options. |
| `CONDITIONAL` | Needed only by some industries or operating models (import, food/pharma, retail with variants, multi-site). Platform capability should exist; tenant visibility should be switchable. |
| `NOT APPLICABLE` | Benchmark-specific or not a Thai SME user concern; may exist as a background system function but not as a user menu. |
| `UNKNOWN` | Evidence insufficient to classify. |

Prior-study status uses the prompt §3 taxonomy: `CARRY_FORWARD_WITH_EVIDENCE` / `REOPEN_FOR_MENU_PROCESS_DEPTH` / `REWRITE_AS_CLEAN_ROOM_LEARNING` / `CONFLICTING - REOPEN REQUIRED` / `HOLD / EVIDENCE REQUIRED`.

Prior evidence anchor for every row: Inventory Reopen package commit `170af9ea7a5afd127abcaae0ffb40aaa1fa25d4d` (deliverables `01`–`20`), CORR-007B remediation commit `9996072aa3a353dca99de4b22e8611171e24baf4`, and the lineage register `01_PRIOR_EVIDENCE_AND_CLEAN_ROOM_LINEAGE_REGISTER.md` in this package.

---

## 2. Coverage Register (29 menus)

| Menu ID | Group | Benchmark menu | Thai candidate name (see 17) | Thai SMEsPlus classification | Industry condition | Prior-study status (this session's classification) | Prior evidence pointer | Menu-level evidence status now | Owner | Verifier |
|---|---|---|---|---|---|---|---|---|---|---|
| MENU-OP-01 | Operations | Replenishment | เติมสินค้า / แผนเติมสินค้า | `CONDITIONAL` (recommended core for trading & manufacturing; hidden for micro-retail) | Any SME with reorder planning; mandatory when MFG or multi-warehouse | `REOPEN_FOR_MENU_PROCESS_DEPTH` — route dispatch mechanism studied (`02` item 24), replenishment as a user process never studied | Reopen `02` items 24–25; `07_IESA`; `11_AI_CONTROL` | `COVERED` in 06/12 as candidate process; concurrency/idempotency residual carried | Track 05 / S5 | UNVERIFIED |
| MENU-OP-02 | Operations | Inventory Adjustments | ปรับปรุงยอดสต็อก (รวม นับสต็อก) | `MANDATORY` | All | `REOPEN_FOR_MENU_PROCESS_DEPTH` — count-freeze source behavior proven (`N-A7-01`), approval/reason/Thai count-sheet flow never mapped | CORR-007B `N-A7-01`; Reopen `02` item 19; `09_SECURITY` G-2/G-3 | `COVERED` in 06/13; approval policy remains Team B decision (`GAP-MD-02`) | Track 03 / S1 | UNVERIFIED |
| MENU-OP-03 | Operations | Transfers | รับสินค้าเข้า / จ่ายสินค้าออก / โอนย้ายภายใน (umbrella: รายการเคลื่อนย้ายสินค้า) | `MANDATORY` | All | `CARRY_FORWARD_WITH_EVIDENCE` for movement semantics (`02` items 12–17); `REOPEN_FOR_MENU_PROCESS_DEPTH` for document/user flow, partial, backorder, return, cancellation paths | Reopen `05_IBPV`, `06_IDTM`; `13` C-01 (cancellation conflict) | `COVERED` in 06/11/14; C-01 remains `CONFLICTING` | Track 03 / S1, S3 | UNVERIFIED |
| MENU-OP-04 | Operations | Scrap | ตัดสินค้าชำรุด/สูญเสีย | `MANDATORY` | All (Thai tax-deductible destruction requires evidence — statutory claim `HOLD`) | `REOPEN_FOR_MENU_PROCESS_DEPTH` — scrap model existence proven; damaged-goods category is `U-02` unknown; Thai destruction-witness control never studied | Reopen `02` item 18; `13` U-02; `04_TBRAC` | `PARTIAL` — process mapped; Thai statutory destruction evidence `HOLD / EVIDENCE REQUIRED` (`GAP-MD-04`) | Track 02, 06 / S1 | UNVERIFIED |
| MENU-OP-05 | Operations | Landed Costs | ต้นทุนสินค้าเพิ่มเติม (ต้นทุนนำเข้า) | `CONDITIONAL` (mandatory for importers; hidden for domestic-only SMEs) | Import / freight-heavy trading | `HOLD / EVIDENCE REQUIRED` — reopen `15` §D: "code present, commented out, never read"; `08_FINANCIAL` names it a blind spot | Reopen `15` §D; `08_FINANCIAL`; `16` Tier 3 | `PARTIAL` — business process mapped from benchmark documentation knowledge; source-behaviour verification not performed (`GAP-MD-05`) | Track 06 / S6 | UNVERIFIED |
| MENU-OP-06 | Operations | Run Scheduler | ประมวลผลแผนสต็อก | `NOT APPLICABLE` as a Thai user menu; `MANDATORY` as a background system function with an admin-visible run log | All (system) | `REOPEN_FOR_MENU_PROCESS_DEPTH` — scheduler as automation boundary named by Track 09; never explained as a business trigger | Reopen `11_AI_CONTROL`; `02` item 24 | `COVERED` in 12; deterministic-control requirement carried | Track 09 / S5 | UNVERIFIED |
| MENU-PR-01 | Products | Products | สินค้า / ข้อมูลสินค้า | `MANDATORY` | All | `CARRY_FORWARD_WITH_EVIDENCE` for product type routing (`12` deep-proof); `REOPEN_FOR_MENU_PROCESS_DEPTH` for master-data process, mandatory fields, Thai product naming, migration keys | Reopen `12`; `02` item 1 | `COVERED` in 09; tie-break rule for type vs storable flag still `UNKNOWN` | Track 04 / S2 | UNVERIFIED |
| MENU-PR-02 | Products | Product Variants | สินค้าย่อย / ตัวเลือกสินค้า | `CONDITIONAL` (retail apparel, footwear, cosmetics, spare parts) | Variant-driven industries | `HOLD / EVIDENCE REQUIRED` — reopen `02` item 2: "No track produced dedicated variant evidence" | Reopen `02` item 2 | `PARTIAL` — business process mapped; identity/migration evidence `HOLD` (`GAP-MD-08`) | Track 04 / S2 | UNVERIFIED |
| MENU-PR-03 | Products | Lots/Serial Numbers | เลขล็อต / เลขซีเรียล | `CONDITIONAL` as a user menu; platform capability `MANDATORY` (food, pharma, cosmetics, electronics, warranty goods) | Traceability / expiry / warranty industries | `CARRY_FORWARD_WITH_EVIDENCE` for identity constraint facts (`02` items 20–21); `REOPEN_FOR_MENU_PROCESS_DEPTH` for recall/expiry/warranty user process; expiry workflow still unread (`02` item 23) | Reopen `06_IDTM`; `02` items 20–23 | `PARTIAL` — process mapped; expiry workflow depth `HOLD` (`GAP-MD-09`) | Track 04 / S4 | UNVERIFIED |
| MENU-RP-01 | Reporting | Stock | ยอดสินค้าคงเหลือ | `MANDATORY` | All | `REOPEN_FOR_MENU_PROCESS_DEPTH` — on-hand/reserved/available semantics proven; report never studied as a user artifact | Reopen `02` items 9–10; `06_IDTM` | `COVERED` in 16 | Track 03 / S7 | UNVERIFIED |
| MENU-RP-02 | Reporting | Locations | สินค้าคงเหลือตามตำแหน่งจัดเก็บ | `CONDITIONAL` (multi-location / multi-warehouse) | Multi-site or bin-managed warehouses | `REOPEN_FOR_MENU_PROCESS_DEPTH` | Reopen `02` item 5 | `COVERED` in 16 | Track 05 / S7 | UNVERIFIED |
| MENU-RP-03 | Reporting | Moves History | ประวัติการเคลื่อนไหวสินค้า (สต็อกการ์ด) | `MANDATORY` (Thai VAT stock report / stock card need — statutory claim `HOLD` pending authoritative evidence) | All | `REOPEN_FOR_MENU_PROCESS_DEPTH` — append-only done-move history proven (`02` item 38); Thai stock-card report never studied | Reopen `09_SECURITY`; `04_TBRAC` | `PARTIAL` — process mapped; statutory report format `HOLD / EVIDENCE REQUIRED` (`GAP-MD-12`) | Track 06, 02 / S7, S8 | UNVERIFIED |
| MENU-RP-04 | Reporting | Stock Moves | รายการเคลื่อนไหวสินค้า | `MANDATORY` as audit fact ledger; `CONDITIONAL` as end-user menu (advanced) | All (audit) | `CARRY_FORWARD_WITH_EVIDENCE` for movement fact semantics; `REOPEN_FOR_MENU_PROCESS_DEPTH` for fact-vs-summary distinction | Reopen `05_IBPV`, `06_IDTM` | `COVERED` in 16 | Track 04 / S3 | UNVERIFIED |
| MENU-RP-05 | Reporting | Valuation | มูลค่าสินค้าคงเหลือ | `MANDATORY` (accounting interface) | All with stock accounting | `CONFLICTING - REOPEN REQUIRED` at boundary level: `N-A12-01` = HIGH FUNCTIONAL DESIGN GAP — REOPENED; return-valuation cost basis `C-03` conflicting; export defect `G-7` | CORR-007B; Reopen `08_FINANCIAL`, `13` C-03/C-05, `14`, `20` | `PARTIAL` — report purpose mapped; ownership routed to Joint Session (`GAP-MD-13`) | Track 06 / S6 | UNVERIFIED |
| MENU-RP-06 | Reporting | Warehouse Analysis | วิเคราะห์คลังสินค้า | `CONDITIONAL` (management dashboard) | SMEs with management reporting need | `HOLD / EVIDENCE REQUIRED` — never studied in any prior round | none | `PARTIAL` — business questions defined in 16; benchmark content unverified | Track 03 / S7 | UNVERIFIED |
| MENU-CF-01 | Configuration | Settings | ตั้งค่าระบบคลังสินค้า | `MANDATORY` | All | `REOPEN_FOR_MENU_PROCESS_DEPTH` — feature switches never mapped to SMEsPlus tenant-provisioning | Reopen `07_IESA` SAAS-04 | `COVERED` in 08 | Track 05 / S5 | UNVERIFIED |
| MENU-CF-02 | Configuration | Warehouses | คลังสินค้า | `MANDATORY` | All | `CARRY_FORWARD_WITH_EVIDENCE` (`02` item 4, `SAAS-04` regeneration risk) | Reopen `07_IESA` | `COVERED` in 10 | Track 05 / S5 | UNVERIFIED |
| MENU-CF-03 | Configuration | Locations | ตำแหน่งจัดเก็บ | `MANDATORY` (system-default locations); `CONDITIONAL` (user-managed bins) | All / bin-managed | `CARRY_FORWARD_WITH_EVIDENCE` (`02` item 5 CLOSED_WITH_EVIDENCE) | Reopen `07_IESA` | `COVERED` in 10; warehouse-level authorization `U-01` unknown carried | Track 05, 07 / S1 | UNVERIFIED |
| MENU-CF-04 | Configuration | Routes | เส้นทางการไหลของสินค้า | `CONDITIONAL` (multi-step receipt/delivery, MTO, dropship) | Manufacturing, distribution | `REOPEN_FOR_MENU_PROCESS_DEPTH` — dispatch mechanism proven; business meaning for Thai users never written | Reopen `02` items 24–25; `07_IESA` | `COVERED` in 10 as business logic; `REWRITE_AS_CLEAN_ROOM_LEARNING` note applied | Track 05, 08 / S5 | UNVERIFIED |
| MENU-CF-05 | Configuration | Rules | กฎการไหลของสินค้า | `CONDITIONAL` (advanced; should be hidden behind route templates for Thai SMEs) | Advanced | same as MENU-CF-04 | same | `COVERED` in 10 | Track 05, 08 / S5 | UNVERIFIED |
| MENU-CF-06 | Configuration | Operations Types | ประเภทรายการคลัง (รับเข้า / จ่ายออก / โอนภายใน) | `MANDATORY` (system-defaulted per warehouse) | All | `REOPEN_FOR_MENU_PROCESS_DEPTH` — operation-kind string-literal coupling noted (`02` item 14); document numbering, Thai document names, SoD per type never mapped | Reopen `05_IBPV` | `COVERED` in 11 | Track 03 / S1 | UNVERIFIED |
| MENU-CF-07 | Configuration | Storage Categories | ประเภทพื้นที่จัดเก็บ | `CONDITIONAL` (WMS-grade warehouses; capacity control) | Larger warehouses, cold-chain | `HOLD / EVIDENCE REQUIRED` — never studied | none | `PARTIAL` — business meaning mapped; no source verification (`GAP-MD-16`) | Track 05 / S4 | UNVERIFIED |
| MENU-CF-08 | Configuration | Putaway Rules | กฎจัดเก็บสินค้าเข้าที่ | `CONDITIONAL` (bin-managed warehouses) | Multi-bin warehouses | `HOLD / EVIDENCE REQUIRED` — Product Category dual ownership (valuation + putaway) noted in `14`; rules themselves never studied | Reopen `14` §2; `20` §3 | `PARTIAL` (`GAP-MD-17`) | Track 05 / S4 | UNVERIFIED |
| MENU-CF-09 | Configuration | Product Categories | หมวดหมู่สินค้า | `MANDATORY` (valuation-policy owner candidate) | All | `REWRITE_AS_CLEAN_ROOM_LEARNING` — CORR-007B file 09 rewritten as clean-room summary (`9996072a`); `C-05` remains Boss-visible pending independent re-audit | CORR-007B `09`, `17`; Reopen `13` C-05 | `COVERED` in 08/15 from Layer 1 summary only; `C-05` control preserved | Track 06, 08 / S6 | UNVERIFIED |
| MENU-CF-10 | Configuration | Attributes | คุณลักษณะสินค้า | `CONDITIONAL` (with variants) | Variant-driven industries | `HOLD / EVIDENCE REQUIRED` (paired with MENU-PR-02) | Reopen `02` item 2 | `PARTIAL` (`GAP-MD-08`) | Track 04 / S2 | UNVERIFIED |
| MENU-CF-11 | Configuration | Product Packagings | หน่วยบรรจุ / แพ็กสินค้า | `CONDITIONAL` (case/carton selling, distribution) | Wholesale, FMCG | `HOLD / EVIDENCE REQUIRED` — DR-002 noted no packaging model in the studied source; packaging as a business capability never studied | Reopen `01` Part B (DR-002 summary) | `PARTIAL` (`GAP-MD-18`) | Track 04 / S2 | UNVERIFIED |
| MENU-CF-12 | Configuration | Reordering Rules | จุดสั่งซื้อ / กฎสั่งเติมสินค้า | `CONDITIONAL` (pairs with MENU-OP-01) | As MENU-OP-01 | `REOPEN_FOR_MENU_PROCESS_DEPTH` | Reopen `02` item 24 | `COVERED` in 12 | Track 05 / S5 | UNVERIFIED |
| MENU-CF-13 | Configuration | Barcode Nomenclatures | รูปแบบบาร์โค้ด | `CONDITIONAL` (barcode-enabled operations; Thai GS1 EAN-13 common) | Retail, distribution | `HOLD / EVIDENCE REQUIRED` — never studied | none | `PARTIAL` (`GAP-MD-19`) | Track 04 / S2 | UNVERIFIED |
| MENU-CF-14 | Configuration | UoM Categories | กลุ่มหน่วยนับ | `MANDATORY` (Thai units: ชิ้น กล่อง โหล ลัง กิโลกรัม) | All | `CARRY_FORWARD_WITH_EVIDENCE` for conversion facts (`02` item 3: rounding default, non-retroactive factor edits); `REOPEN_FOR_MENU_PROCESS_DEPTH` for Thai unit setup process | Reopen `06_IDTM`; `02` item 3 | `COVERED` in 09 | Track 04 / S2 | UNVERIFIED |

---

## 3. Roll-Up

| Classification | Count | Menu IDs |
|---|---:|---|
| `MANDATORY` | 13 | OP-02, OP-03, OP-04, PR-01, RP-01, RP-03, RP-04, RP-05, CF-01, CF-02, CF-03, CF-06, CF-09, CF-14 (CF-03 mandatory for system defaults) |
| `CONDITIONAL` | 15 | OP-01, OP-05, PR-02, PR-03, RP-02, RP-06, CF-04, CF-05, CF-07, CF-08, CF-10, CF-11, CF-12, CF-13 (+ RP-04 as end-user menu) |
| `NOT APPLICABLE` (as a user menu) | 1 | OP-06 (system function, admin log only) |
| `UNKNOWN` | 0 | — |

| Prior-study status | Count | Menu IDs |
|---|---:|---|
| `CARRY_FORWARD_WITH_EVIDENCE` (fully or partly) | 8 | OP-03, PR-01, PR-03, RP-04, CF-02, CF-03, CF-14 (+ CF-09 via rewritten Layer 1) |
| `REOPEN_FOR_MENU_PROCESS_DEPTH` | 13 | OP-01, OP-02, OP-03, OP-04, OP-06, PR-01, PR-03, RP-01, RP-02, RP-03, RP-04, CF-01, CF-04, CF-05, CF-06, CF-12, CF-14 (overlaps counted once per primary status) |
| `REWRITE_AS_CLEAN_ROOM_LEARNING` | 1 | CF-09 (plus route/rule wording notes on CF-04/CF-05) |
| `CONFLICTING - REOPEN REQUIRED` | 1 | RP-05 (boundary-level: `N-A12-01`, `C-03`) |
| `HOLD / EVIDENCE REQUIRED` | 9 | OP-05, PR-02, RP-06, CF-07, CF-08, CF-10, CF-11, CF-13 (+ OP-04 statutory sub-item, RP-03 statutory sub-item) |

| Menu-level evidence status now | Count |
|---|---:|
| `COVERED` (candidate process fully mapped, residual gaps named) | 17 |
| `PARTIAL` (process mapped; evidence hold on a material sub-item) | 12 |
| `GAP` / `HOLD` / `NOT APPLICABLE` at row level | 0 / 0 / 0 (holds are recorded at sub-item level in 24) |

No menu was left unmapped. Every `HOLD` sub-item is carried to `24_UNKNOWN_CONFLICT_GAP_OWNER_GATE_IMPACT_REGISTER.md` with an owner.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
