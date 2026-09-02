# 07 — Inventory Menu Impact Matrix

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-07 OUTPUT — MANDATORY MENU IMPACT MATRIX — NO BLANK CELLS — NOT A GATE DECISION`
Clean-room boundary: matrix cells describe business impact only. The "Clean-room transformation note" column records how each benchmark menu was transformed into a SMEsPlus candidate and what must not be copied.

Legend: `Y` = yes, `N` = no, `C` = conditional. Evidence pointers: `R:` = Inventory Reopen package commit `170af9ea` (deliverable number / item), `CR:` = CORR-007B clean-room commit `9996072a`, `M:` = this package's map number. Status vocabulary: `COVERED / PARTIAL / GAP / HOLD / NOT APPLICABLE`. Owner = challenge track / special team assigned in this session (not an execution team). Verifier = `UNVERIFIED` for all rows: no independent verification of this package has occurred.

The 27 required fields are split into three tables per menu group to keep the matrix readable; every menu appears in all three tables with the same ID.

---

## A. Descriptive Fields

| ID | Menu group | Benchmark menu/function | Thai candidate name | Business purpose | Input | Process | Output | Handoff to next process |
|---|---|---|---|---|---|---|---|---|
| MENU-OP-01 | Operations | Replenishment | เติมสินค้า / แผนเติมสินค้า | Prevent stock-out / over-stock | Reorder rules, forecast | Compute shortfall → propose → confirm | Proposals; PO/MO/transfer | Purchase (PO), MFG (MO), Inventory (transfer) |
| MENU-OP-02 | Operations | Inventory Adjustments | ปรับปรุงยอดสต็อก | Align book to physical | Count results / correction request, reason | Count → compare → approve → apply | Corrected on-hand, register | Accounting (gain/loss fact) |
| MENU-OP-03 | Operations | Transfers | รับเข้า / จ่ายออก / โอนย้ายภายใน | Record physical movements | Orders, goods, lots | Create → reserve → confirm → validate | Done movements, backorders | Purchase, Sales, Accounting, MFG |
| MENU-OP-04 | Operations | Scrap | ตัดสินค้าชำรุด/สูญเสีย | Remove unusable stock | Scrap request, reason, evidence | Request → approve → move to loss → register | Reduced on-hand, loss fact | Accounting, Tax (destruction evidence) |
| MENU-OP-05 | Operations | Landed Costs | ต้นทุนสินค้าเพิ่มเติม | True acquisition cost | Cost bills, receipts, method | Allocate → validate | Adjusted cost basis | Accounting |
| MENU-OP-06 | Operations | Run Scheduler | ประมวลผลแผนสต็อก | Background planning on demand | Rules, demands | Deterministic batch | Proposals, reservations, log | Replenishment, Transfers |
| MENU-PR-01 | Products | Products | สินค้า | Single item identity | Master attributes | Create → policies → activate | Product master | All domains |
| MENU-PR-02 | Products | Product Variants | สินค้าย่อย | Stock per option | Template + attributes | Generate variants | SKU grid | Sales, Inventory |
| MENU-PR-03 | Products | Lots/Serial Numbers | เลขล็อต / เลขซีเรียล | Traceability | Tracking mode, values, expiry | Assign → propose → history | Lot history, expiry list | QA, Sales (warranty), Recall |
| MENU-RP-01 | Reporting | Stock | ยอดสินค้าคงเหลือ | Availability | On-hand, reservations | Aggregate | Qty columns | Sales, Purchasing |
| MENU-RP-02 | Reporting | Locations | สินค้าคงเหลือตามตำแหน่งจัดเก็บ | Where stock is | Per-location balances | Views | Bin contents | Warehouse, Count |
| MENU-RP-03 | Reporting | Moves History | ประวัติการเคลื่อนไหวสินค้า (สต็อกการ์ด) | Audit ledger per product | Done lines | Running balance | Stock card | Audit, Tax, Accounting |
| MENU-RP-04 | Reporting | Stock Moves | รายการเคลื่อนไหวสินค้า | Fact list | All lines | Filter | Fact list | Audit, Migration |
| MENU-RP-05 | Reporting | Valuation | มูลค่าสินค้าคงเหลือ | Stock value & GL reconciliation | Qty, cost, policy, GL | Compute, reconcile | Valuation, reconciliation | Accounting |
| MENU-RP-06 | Reporting | Warehouse Analysis | วิเคราะห์คลังสินค้า | Performance KPIs | Dates, volumes, ages | KPI calc | Dashboard | Management |
| MENU-CF-01 | Configuration | Settings | ตั้งค่าระบบคลังสินค้า | Feature switches | Admin choices | Enable/generate | Feature set | All Inventory menus |
| MENU-CF-02 | Configuration | Warehouses | คลังสินค้า | Physical site | Site data, step policy | Create defaults | Warehouse tree | Locations, Operation types, Routes |
| MENU-CF-03 | Configuration | Locations | ตำแหน่งจัดเก็บ | Stock places | Tree, types | Maintain tree | Location tree | Movements, Reports |
| MENU-CF-04 | Configuration | Routes | เส้นทางการไหลของสินค้า | Flow templates | Template choice | Resolve | Movement chains | Transfers, Purchase, MFG |
| MENU-CF-05 | Configuration | Rules | กฎการไหลของสินค้า | Route steps | Rule params | Chain | Planned moves | Routes |
| MENU-CF-06 | Configuration | Operations Types | ประเภทรายการคลัง | Document kinds | Name, direction, sequence | Create per warehouse | Series, dashboards | Transfers |
| MENU-CF-07 | Configuration | Storage Categories | ประเภทพื้นที่จัดเก็บ | Place constraints | Limits, rules | Assign to locations | Capacity control | Putaway |
| MENU-CF-08 | Configuration | Putaway Rules | กฎจัดเก็บสินค้าเข้าที่ | Auto destination | Product/category → place | Match rule | Suggested bin | Receipts, Internal |
| MENU-CF-09 | Configuration | Product Categories | หมวดหมู่สินค้า | Grouping + valuation policy | Tree, policy, accounts | Inherit | Effective policy | Products, Valuation, Accounting |
| MENU-CF-10 | Configuration | Attributes | คุณลักษณะสินค้า | Variant axes | Attributes, values | Assign | Variant grid | Variants |
| MENU-CF-11 | Configuration | Product Packagings | หน่วยบรรจุ | Pack sizes | Product, qty, barcode | Convert | Base-unit qty | Transfers, Barcode |
| MENU-CF-12 | Configuration | Reordering Rules | จุดสั่งซื้อ | Min/max policy | Min, max, route | Evaluate | Proposals | Replenishment |
| MENU-CF-13 | Configuration | Barcode Nomenclatures | รูปแบบบาร์โค้ด | Scan parsing | Patterns | Parse | Parsed scan | Transfers, Count |
| MENU-CF-14 | Configuration | UoM Categories | กลุ่มหน่วยนับ | Unit conversion | Units, factors | Convert | Base-unit stock | Products, Transfers, Valuation |

---

## B. Impact Flags (Y / N / C)

| ID | Stock truth | Quantity | Reservation | Lot/serial | Warehouse/location | Valuation | Accounting handoff | Tax/statutory | Management report | Audit/control | Migration | SaaS/multi-company |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MENU-OP-01 | N | N | C (auto reservation after run) | N | Y | N | N | N | Y | C | C (rules as policy) | Y |
| MENU-OP-02 | Y | Y | C | Y | Y | Y | Y | C (year-end count witness) | Y | Y | Y (opening balance `G-5`) | Y |
| MENU-OP-03 | Y | Y | Y | Y | Y | Y (receipt/delivery/return) | Y | C (delivery note, tax invoice link) | Y | Y | Y | Y |
| MENU-OP-04 | Y | Y | C | Y | Y | Y | Y | Y (destruction evidence — `HOLD`) | Y | Y | C | Y |
| MENU-OP-05 | N | N | N | N | N | Y | Y | C (import duty/VAT — `HOLD`) | C | Y | C (cost history) | Y |
| MENU-OP-06 | N | N | Y | N | Y | N | N | N | N | Y (run log) | N | Y |
| MENU-PR-01 | Y (identity) | N | N | C | N | Y (policy inheritance) | C | C (WHT by kind) | Y | Y | Y | Y |
| MENU-PR-02 | Y (identity) | N | N | N | N | Y | N | N | Y | C | Y | Y |
| MENU-PR-03 | Y | C (per lot) | C | Y | Y | N | N | C (recall, pharma/food regs — `HOLD`) | Y | Y | Y | Y |
| MENU-RP-01 | N (reads) | N | N | C | Y | N | N | N | Y | C | N | Y |
| MENU-RP-02 | N (reads) | N | N | C | Y | N | N | N | Y | C | N | Y |
| MENU-RP-03 | N (reads) | N | N | Y | Y | C | C | Y (stock report — `HOLD`) | C | Y | Y | Y |
| MENU-RP-04 | N (reads) | N | Y (shows) | Y | Y | N | N | N | N | Y | Y | Y |
| MENU-RP-05 | N (reads) | N | N | N | C | Y | Y | Y (statutory valuation — `HOLD`) | Y | Y | Y | Y |
| MENU-RP-06 | N (reads) | N | N | N | Y | C | N | N | Y | N | N | Y |
| MENU-CF-01 | C (structural) | N | C (policy) | C | Y | C | C | N | N | Y | Y | Y |
| MENU-CF-02 | Y (where) | N | N | N | Y | C | N | C (branch ≠ warehouse) | Y | Y | Y | Y |
| MENU-CF-03 | Y (where) | N | N | N | Y | C (boundary crossing) | C | N | Y | Y | Y | Y |
| MENU-CF-04 | N | N | C | N | Y | N | N | N | N | Y | C (policy) | Y |
| MENU-CF-05 | N | N | C | N | Y | N | N | N | N | Y | C (policy) | Y |
| MENU-CF-06 | C (direction) | N | C (policy) | C | Y | C | C | C (document names/numbering) | Y | Y | Y (series) | Y |
| MENU-CF-07 | N | N | N | N | Y | N | N | N | N | N | N | Y |
| MENU-CF-08 | N | N | N | C | Y | N | N | N | N | C | N | Y |
| MENU-CF-09 | N | N | N | N | N | Y | Y | Y (costing norm `TH-INV-03`) | Y | Y | Y | Y |
| MENU-CF-10 | Y (identity) | N | N | N | N | N | N | N | C | C | Y | Y |
| MENU-CF-11 | N | C (conversion) | N | N | N | N | N | N | N | C | C | Y |
| MENU-CF-12 | N | N | N | N | Y | N | N | N | Y | C | C (policy) | Y |
| MENU-CF-13 | N | C (parse errors) | N | C | C | N | N | N | N | C | C | Y |
| MENU-CF-14 | Y (base unit) | Y (conversion) | N | N | N | Y (rounding) | C | N | N | Y | Y | Y |

SaaS/multi-company is `Y` for every row because every configuration and transaction is tenant- and company-scoped and no Inventory-side SaaS invariant set exists yet (`U-03`, reopen `02` item 34).

---

## C. Transformation, Evidence, Ownership, Gate

| ID | Clean-room transformation note | Evidence location | Owner | Verifier | Gate impact | Status |
|---|---|---|---|---|---|---|
| MENU-OP-01 | Benchmark planning feature → "what to order now" business process with explainable proposals; no scheduler/procurement architecture | R:02 item 24, R:07, R:11; M:12 | Track 05 / S5 | UNVERIFIED | Team B precondition; `C-02` Boss | COVERED |
| MENU-OP-02 | Benchmark soft-conflict count → Thai count + approval + reason + period guard process; four freeze options left open | CR: `N-A7-01`; R:05, R:09, R:02 items 19, 31; M:13 | Track 03, 07 / S1 | UNVERIFIED | Team B precondition; `G-2`/`G-3` Joint | COVERED |
| MENU-OP-03 | Single "Transfers" concept → three Thai documents + returns sharing one movement fact model; no state machine or benchmark document-type vocabulary | R:05, R:06, R:13 C-01; M:11, M:14 | Track 03 / S1, S3 | UNVERIFIED | Team B precondition; `C-01` bounded | COVERED |
| MENU-OP-04 | Benchmark scrap document → reason-driven exception with approval and Thai destruction evidence pack | R:02 item 18, R:13 U-02, R:04; M:13 | Track 02, 06 / S1 | UNVERIFIED | Team B precondition; statutory `HOLD` | PARTIAL |
| MENU-OP-05 | Benchmark landed cost → allocation business process; eligibility/posting left to Joint | R:08 FIN-DELTA-02, R:15 §D; M:15 | Track 06 / S6 | UNVERIFIED | Team B precondition (conditional) | PARTIAL |
| MENU-OP-06 | Benchmark manual scheduler trigger → admin-visible deterministic background planning with run log; no job architecture | R:11, R:02 item 24; M:12 | Track 09 / S5 | UNVERIFIED | `C-02` Boss | COVERED (as system function) |
| MENU-PR-01 | Two-axis benchmark type gate → three Thai business labels over a documented derivation; tie-break open | R:12, R:02 item 1; M:09 | Track 04 / S2 | UNVERIFIED | Team B precondition | COVERED |
| MENU-PR-02 | Benchmark variants → stable attribute-value identity SKUs | R:02 item 2 (no evidence); M:09 | Track 04 / S2 | UNVERIFIED | Team B precondition (conditional) | PARTIAL |
| MENU-PR-03 | Benchmark lot/serial → recall/expiry/warranty process with DB-enforced uniqueness requirement | R:06, R:02 items 20–23; M:09 | Track 04 / S4 | UNVERIFIED | Team B precondition for tracked industries | PARTIAL |
| MENU-RP-01 | Benchmark quantity report → three-column Thai availability view; negatives displayed | R:02 items 9–10; M:16 | Track 03 / S7 | UNVERIFIED | Design requirement | COVERED |
| MENU-RP-02 | Benchmark location report → bin view with warehouse authorization | R:02 item 5, R:13 U-01; M:16 | Track 05 / S7 | UNVERIFIED | `U-01` Team B precondition | COVERED |
| MENU-RP-03 | Benchmark move history → Thai stock card with as-of reproducibility; statutory format held | R:02 item 38, R:04; M:16 | Track 06, 02 / S7, S8 | UNVERIFIED | Statutory `HOLD` (Accounting-Tax) | PARTIAL |
| MENU-RP-04 | Benchmark move list → audit fact ledger and replay base | R:05, R:06; M:16 | Track 04 / S3 | UNVERIFIED | `C-02` Boss | COVERED |
| MENU-RP-05 | Benchmark valuation report → policy-aware valuation + GL reconciliation; ownership Joint; `C-05` control | CR:09, CR:17; R:08, R:13 C-03/C-05, R:14, R:20; M:15 | Track 06 / S6 | UNVERIFIED | **Blocks Joint Backbone publication** | PARTIAL |
| MENU-RP-06 | Benchmark analysis → candidate KPI set for Thai owners | none; M:16 | Track 03 / S7 | UNVERIFIED | Non-blocking | PARTIAL |
| MENU-CF-01 | Benchmark settings → Thai business-question switches with guards and audit; no silent regeneration | R:07 SAAS-04, R:09 G-2; M:08 | Track 05 / S5 | UNVERIFIED | Team B precondition | COVERED |
| MENU-CF-02 | Benchmark warehouse → physical site with explicit branch attribute; versioned step policy | R:02 item 4, R:15 §B GRPA-H8; M:08, M:10 | Track 05, 02 / S5 | UNVERIFIED | Team B precondition | COVERED |
| MENU-CF-03 | Benchmark location tree → Thai-labelled controlled types; authorization axis open | R:02 item 5, R:13 U-01; M:08, M:10 | Track 05, 07 / S1 | UNVERIFIED | `U-01` Team B precondition | COVERED |
| MENU-CF-04 | Benchmark routes → Thai flow templates (RT-*) hiding rules; deterministic explainable resolution | R:02 items 24–25, R:07, R:05 §7; M:10 | Track 05, 08 / S5 | UNVERIFIED | Team B precondition | COVERED |
| MENU-CF-05 | Benchmark rules → hidden template internals; advanced audited edit only | same as CF-04; M:10 | Track 05, 08 / S5 | UNVERIFIED | Team B precondition | COVERED |
| MENU-CF-06 | Benchmark document types → Thai document types with numbering and SoD | R:02 items 14, 38; M:11 | Track 03, 07 / S1 | UNVERIFIED | Team B precondition | COVERED |
| MENU-CF-07 | Benchmark storage category → capacity/condition class, advisory by default | none; M:08 | Track 05 / S4 | UNVERIFIED | Non-blocking | PARTIAL |
| MENU-CF-08 | Benchmark putaway → explainable storage rule; category dual ownership to Joint | R:14 §2, R:20 §3; M:08 | Track 05 / S4; Joint | UNVERIFIED | Team B precondition | PARTIAL |
| MENU-CF-09 | Benchmark category-as-policy-owner → four candidate owners; SMEsPlus must choose (Layer 1 only) | CR:09, CR:17; R:08, R:12, R:14; M:08, M:15 | Track 06, 08 / S6; Joint | UNVERIFIED | **Blocks Joint Backbone publication** | COVERED (Layer 1) |
| MENU-CF-10 | Benchmark attributes → stable value codes | R:02 item 2; M:08, M:09 | Track 04 / S2 | UNVERIFIED | Conditional | PARTIAL |
| MENU-CF-11 | Benchmark packaging (represented via units) → explicit pack definitions over base UoM | R:01 Part B, R:05 §3; M:08, M:09 | Track 04 / S2 | UNVERIFIED | Non-blocking | PARTIAL |
| MENU-CF-12 | Benchmark reorder rule → จุดสั่งซื้อ min/max policy with explanation | R:02 item 24; M:12 | Track 05 / S5 | UNVERIFIED | Team B precondition (conditional) | COVERED |
| MENU-CF-13 | Benchmark nomenclature → Thai default barcode formats (EAN-13, GS1, internal) | none; M:08 | Track 04 / S2 | UNVERIFIED | Non-blocking | PARTIAL |
| MENU-CF-14 | Benchmark unit tree → Thai unit groups with versioned factors and explicit rounding | R:02 item 3, R:06; M:08, M:09 | Track 04 / S2 | UNVERIFIED | Design requirement | COVERED |

---

## D. Roll-Up

| Status | Count | IDs |
|---|---:|---|
| COVERED | 17 | OP-01, OP-02, OP-03, OP-06, PR-01, RP-01, RP-02, RP-04, CF-01, CF-02, CF-03, CF-04, CF-05, CF-06, CF-09, CF-12, CF-14 |
| PARTIAL | 12 | OP-04, OP-05, PR-02, PR-03, RP-03, RP-05, RP-06, CF-07, CF-08, CF-10, CF-11, CF-13 |
| GAP / HOLD / NOT APPLICABLE (row level) | 0 | Holds are recorded per sub-item in register 24 |

| Gate impact class | IDs |
|---|---|
| Blocks Joint Backbone publication | RP-05, CF-09 (+ OP-02 via `G-2`/`G-3`, OP-05 via posting design) |
| Boss decision required | OP-01, OP-06, RP-04 (`C-02`) |
| Statutory `HOLD` to Accounting-Tax | OP-04, OP-05, RP-03, RP-05, CF-09 (`TH-INV-03`) |
| Team B precondition (non-blocking for this study) | remaining rows |

No cell in this matrix is blank. Verifier is `UNVERIFIED` for every row because no independent audit of this package has occurred; that audit is the next controlled action (see 26).

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
