# 16 — Reporting: Stock / Location / Move / Valuation / Analysis Map

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-06 OUTPUT — REPORTING REFERENCE BY AUDIENCE — NOT APPROVED DESIGN`
Clean-room boundary: reports are defined by the business question they answer and the audience that asks it. No benchmark report layout, query, or model is described or proposed.

Menus covered: MENU-RP-01 Stock, MENU-RP-02 Locations, MENU-RP-03 Moves History, MENU-RP-04 Stock Moves, MENU-RP-05 Valuation, MENU-RP-06 Warehouse Analysis.

---

## 1. Four Report Classes (the required separation)

| Class | Question type | Audience | Must be |
|---|---|---|---|
| Operational | "What do we have / what must we do today?" | Warehouse, sales, purchasing | Live, fast, per location |
| Management | "How well is the warehouse performing / where is cash tied up?" | Owner, managers | Periodic, comparative |
| Audit | "Prove every quantity from movements" | Internal audit, external auditor, Revenue Department | Immutable, reproducible as of date |
| Accounting support | "What value goes into the books and does it reconcile?" | Accountant | Policy-aware, period-based, reconcilable to GL |

Prior evidence: no round studied Inventory reporting as a user artifact; the only reporting fact is the reconciliation report export defect (`G-7`). All rows below are therefore new menu-level reference, `PROCESS BENCHMARK` knowledge plus Thai practice, unless cited.

---

## 2. Report Map

### 2.1 Stock — ยอดสินค้าคงเหลือ (MENU-RP-01) — Operational

| Aspect | Content |
|---|---|
| Question | How much of each product do we have, how much is promised, how much can I sell? |
| Input | Current quantities per product (× location, lot, package); reservations; incoming/outgoing planned. |
| Process | Aggregate done movements to on-hand; subtract reservations for available; add planned for forecast. |
| Output | Per product: คงเหลือจริง / จองแล้ว / พร้อมใช้ / กำลังเข้า / กำลังออก / คาดการณ์; filters by warehouse, category, lot, expiry. |
| Control | Must equal Σ movements (conservation) — any drift is an integrity alarm. Benchmark: available is clamped to zero while a true negative can persist underneath (reopen `02` item 10) — SMEsPlus should surface negatives, not hide them. |
| Thai reading | Three-column reading is the key UX: "มี 100 จองแล้ว 30 ขายได้อีก 70". |

### 2.2 Locations — สินค้าคงเหลือตามตำแหน่งจัดเก็บ (MENU-RP-02) — Operational

| Aspect | Content |
|---|---|
| Question | Where exactly is it (which warehouse / zone / bin), and what is in this bin? |
| Input | On-hand per location × product × lot × package. |
| Output | Location-first view and product-first view; empty-bin list; capacity usage where storage categories exist. |
| Control | Warehouse-level authorization (`U-01`) decides who may see which warehouse. |
| Condition | Only meaningful with multi-location enabled. |

### 2.3 Moves History — ประวัติการเคลื่อนไหวสินค้า / สต็อกการ์ด (MENU-RP-03) — Audit

| Aspect | Content |
|---|---|
| Question | For this product (and lot), show every in and out with running balance from opening to date. |
| Input | Done movement lines with from/to, qty, date, document, user; opening balance for the period. |
| Process | Chronological running balance per product (× location / lot); as-of-date reproducibility. |
| Output | Stock card: วันที่ / เอกสาร / รับ / จ่าย / คงเหลือ / ต้นทุน (optional) / ผู้ทำรายการ. |
| Control | Append-only movement history (reopen `02` item 38); as-of-date must reproduce identically later; export to PDF/XLSX for auditors (benchmark valuation report export is defective — `G-7` — SMEsPlus must test exports). |
| Thai statutory note | Thai VAT registrants are commonly required to keep a goods and raw materials report (รายงานสินค้าและวัตถุดิบ) — **statutory claim held**: `HOLD / EVIDENCE REQUIRED` (`GAP-MD-12`), owner Accounting-Tax track. Inventory must be able to produce a per-product in/out/balance ledger by date regardless. |

### 2.4 Stock Moves — รายการเคลื่อนไหวสินค้า (MENU-RP-04) — Audit (technical)

| Aspect | Content |
|---|---|
| Question | List every movement fact (not summarized) with all attributes, for reconciliation and investigation. |
| Input | All movement lines, any state. |
| Output | Filterable fact list: state, document, operation type, product, lot, from, to, planned qty, done qty, dates, user, source order. |
| Control | Distinguish planned vs done clearly; done facts immutable; this list is the reconciliation base for migration replay (`C-02`). |
| Condition | Advanced/audit visibility; not a first-level Thai SME menu. |

### 2.5 Valuation — มูลค่าสินค้าคงเหลือ (MENU-RP-05) — Accounting support

| Aspect | Content |
|---|---|
| Question | What is stock worth as of date, by product/category/location, under which policy, and does it reconcile to GL? |
| Input | Quantities as of date; cost per method; policy version; GL inventory balance (Accounting). |
| Output | Valuation as of date; period movement of value (opening, receipts, issues, adjustments, scrap, landed cost, closing); reconciliation to GL with differences explained. |
| Control | Method and policy printed on the report; as-of-date reproducibility; export mandatory (benchmark defect `G-7`). Ownership: facts Inventory; reconciliation closure Accounting (`PENDING_ACCOUNT_INVENTORY_JOINT_SESSION`). |
| Thai reading | มูลค่าสินค้าคงเหลือ ณ วันที่ … ตามวิธี … ; กระทบยอดกับบัญชี. |

### 2.6 Warehouse Analysis — วิเคราะห์คลังสินค้า (MENU-RP-06) — Management

| Aspect | Content |
|---|---|
| Question | Are we receiving and shipping on time? What is late? Where is stock ageing? What is turning? |
| Input | Documents with planned vs done dates; movement volumes; stock ages; values. |
| Output | Candidate KPIs: on-time receipt %, on-time delivery %, backorder count/age, stock age buckets (0-30/31-90/91-180/180+ วัน), turnover per category, dead stock list, adjustment and scrap value trend, count accuracy %. |
| Control | Management only; must not be mistaken for audit or accounting figures. |
| Evidence status | `HOLD / EVIDENCE REQUIRED` — benchmark content unverified; KPI set is a candidate (`GAP-MD-25`). |

---

## 3. Audience × Report Matrix

| Report | Warehouse | Sales/Purchase | Owner/Mgmt | Accountant | Auditor / Tax |
|---|---|---|---|---|---|
| Stock (2.1) | ✔ primary | ✔ | ✔ | – | – |
| Locations (2.2) | ✔ primary | – | – | – | ✔ (count) |
| Moves History (2.3) | ✔ | – | – | ✔ | ✔ primary |
| Stock Moves (2.4) | – | – | – | ✔ | ✔ |
| Valuation (2.5) | – | – | ✔ | ✔ primary | ✔ |
| Warehouse Analysis (2.6) | ✔ | ✔ | ✔ primary | – | – |
| Adjustment register (TH-R07) | ✔ | – | ✔ | ✔ | ✔ |
| Scrap register (TH-R08) | ✔ | – | ✔ | ✔ | ✔ |
| Traceability / recall (TH-R09) | ✔ | ✔ | – | – | ✔ (recall) |
| Expiry watch (TH-R10) | ✔ | ✔ | – | – | – |

---

## 4. Report Integrity Rules (candidate)

1. Every summary report must be reproducible from the movement fact ledger as of any date.
2. Reports state the policy and version they used (valuation method, UoM rounding).
3. Exports (PDF/XLSX) are tested as part of acceptance — the benchmark shipped a silent export failure.
4. Audit reports never show planned quantities as stock.
5. Negative on-hand is displayed, flagged, and explained, never clamped.
6. Report access follows the same company / warehouse / role axes as transactions.

---

## 5. Gaps Carried

| Gap ID | Item | Owner | Gate impact |
|---|---|---|---|
| GAP-MD-12 | Thai statutory stock report format (รายงานสินค้าและวัตถุดิบ) | Accounting-Tax track | `HOLD / EVIDENCE REQUIRED` |
| GAP-MD-25 | Warehouse analysis KPI set and benchmark content | Track 03 / S7 | Non-blocking |
| GAP-MD-13 | Valuation-to-GL reconciliation ownership and export | Joint Session | Blocks Joint Backbone publication |
| G-7 | Reconciliation report export defect (reference fact; SMEsPlus acceptance rule) | Track 04, 05 | Non-blocking (design requirement) |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
