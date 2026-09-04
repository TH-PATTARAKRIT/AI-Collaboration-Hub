# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 03 — L2 UI / Field / Configuration Forensic

Level: `L2 — UI / Field / Configuration Forensic`
Scope: `29 of 29 Inventory menus`
Control Level: `/L9999.9999`
Status: `L2 COMPLETE FOR 29/29 MENUS — 6 MENUS PARTIAL WITH NAMED CAUSE — DEEP RESEARCH ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. Method And Evidence Basis

For each menu this register records the seven L2 dimensions required by the standard: required fields, optional fields, configuration drivers, status/state fields, visibility rules, user-facing labels with Thai naming candidates, and configuration risk.

Three evidence strengths are used and are marked on every material statement:

| Tag | Meaning |
|---|---|
| `L2-OBS` | Observed directly in the OpenSource reference ERP's own implementation during this session's Layer 2 forensic inspection on 2026-09-04. Strongest available evidence short of a live instance test. |
| `L1-CF` | Carried forward from an earlier SMEsPlus round (Menu Deep Challenge, Reopen, v1.0 Final Solution) and re-read this session. |
| `L0-INF` | Inferred from business necessity, not from source or from prior evidence. Weakest. Explicitly flagged so it is never mistaken for a fact. |

The Menu Deep Challenge round recorded eight menus as resting on no prior evidence at all (`GAP-FS-20`): landed cost, variants, warehouse analysis, storage categories, put-away rules, attributes, packagings, barcode formats. **R4 materially reduces that gap.** Layer 2 inspection this session produced first-hand field and behaviour evidence for six of those eight. The two that remain evidence-thin are recorded in Section 6.

Thai labels below are quoted from `17_THAI_MENU_AND_REPORT_NAMING_REGISTER.md` and remain `CANDIDATE / UNVALIDATED — THAI USER REVIEW REQUIRED` (`GAP-FS-11`). R4 does not validate any of them.

---

## 2. Group A — Operations

### `INV-M01` Replenishment — `TH-01` เติมสินค้า / แผนเติมสินค้า

| L2 Dimension | Finding |
|---|---|
| Required fields | Product; location or warehouse context; proposed quantity; supply route. |
| Optional fields | Preferred supplier; requested date; manual override quantity; note. |
| Configuration drivers | Reordering rule parameters (`INV-M27`); route availability (`INV-M19`); supplier lead time; forecast horizon setting. |
| Status / state fields | Proposal state, and — separately — a *manual* proposed quantity distinct from the *computed* proposed quantity. `L2-OBS`: the reference system holds the computed and the manually-entered order quantity as two separate values, with the effective quantity derived from both. This is a genuinely important design point: an operator override must not be silently erased by the next automatic recomputation. |
| Visibility rules | The whole menu is meaningful only when reordering rules or forecast data exist. Rows are suppressed while a rule is in a snoozed / suspended period (`L2-OBS`). |
| Labels + Thai candidates | Primary `เติมสินค้า / แผนเติมสินค้า`; alternates `รายการที่ต้องสั่งเติม`, `สินค้าใกล้หมด`. Naming must distinguish the human act from the system proposal (`P3`). |
| Configuration risk | **HIGH.** `L2-OBS`: the shortfall computation uses the *greater* of the configured minimum and maximum, so a rule entered with minimum above maximum does not error — it silently orders to the minimum. A Thai SME entering the two fields the wrong way round would get quietly wrong ordering with no warning. R4 raises this as a new finding: `R4-F-01`. |

### `INV-M02` Inventory Adjustments — `TH-02` ปรับปรุงยอดสต็อก

| L2 Dimension | Finding |
|---|---|
| Required fields | Product; location; counted quantity; count date; company. |
| Optional fields | Lot/serial (required where the product is tracked); package; owner; reason; note; counter identity. |
| Configuration drivers | Multi-location setting; traceability setting; package setting; counting cycle configured on the location (`L2-OBS` — locations carry a cyclic counting frequency and a last-counted date, and the company carries an annual count month and day); period lock supplied by Accounting. |
| Status / state fields | Counted quantity, difference, and applied state. `L2-OBS`: the reference model keeps the counted quantity and the resulting difference as separate values on the on-hand record itself rather than as an independent count document — meaning the count is an attribute of the balance, not a document with its own lifecycle. **This is a control weakness SMEsPlus must not inherit.** `CN-27` (count session) already anticipates the correction; R4 confirms the reference pattern is the weaker one. Finding `R4-F-02`. |
| Visibility rules | Lot/serial and package columns appear only when those capabilities are enabled. |
| Labels + Thai candidates | `ปรับปรุงยอดสต็อก`, with the count sub-flow entered as `นับสต็อก / ตรวจนับสินค้า`; reason label `เหตุผลการปรับ`. |
| Configuration risk | **HIGH.** No approval state exists in the reference pattern (`L2-OBS`), so the reason code and approver identity are the only control, and neither is mandatory there. Carried as `GAP-MD-02` (approval policy unselected). |

### `INV-M03` Transfers — `TH-03` รับเข้า / จ่ายออก / โอนย้ายภายใน

| L2 Dimension | Finding |
|---|---|
| Required fields | Operation type; source location; destination location; product; demanded quantity; company. |
| Optional fields | Done quantity before validation; lot/serial; package; owner; scheduled date; effective date; source document; carrier and tracking; note. |
| Configuration drivers | Operation type defaults (`INV-M21`); route and rule configuration (`INV-M19`, `INV-M20`); multi-step settings; traceability; packages; backorder policy on the operation type. |
| Status / state fields | Draft, waiting, ready, done, cancelled — plus a separate reserved quantity that is not itself a state. `L2-OBS`: reservation is held as a quantity on the balance record, not as a first-class reservation document, which is why a reservation can be silently reduced by an adjustment. |
| Visibility rules | Multi-step intermediate steps appear only where the route defines them; lot/serial capture appears only for tracked products. |
| Labels + Thai candidates | Umbrella `รายการเคลื่อนย้ายสินค้า`; three first-level entries `รับสินค้าเข้า`, `จ่ายสินค้าออก / ส่งสินค้า`, `โอนย้ายภายใน`; returns `รับคืน / ส่งคืน`. Naming conflict `N-1` carried. |
| Configuration risk | **HIGH.** The operation type's default source and destination silently determine whether an operation has a financial consequence. A misconfigured default is invisible to the operator and produces a valuation effect nobody intended. |

### `INV-M04` Scrap — `TH-04` ตัดสินค้าชำรุด/สูญเสีย

| L2 Dimension | Finding |
|---|---|
| Required fields | Product; quantity; unit of measure; source location; scrap destination location; company. |
| Optional fields | Lot/serial; package; owner; source document; linked transfer; reason tag; replenish-after-scrap flag. |
| Configuration drivers | Locations flagged as scrap destinations; traceability; packages; the reason tag list. |
| Status / state fields | `L2-OBS`: **two states only — draft and done. There is no approval state, no rejection path, and no reviewer field.** |
| Visibility rules | Lot/serial visible only for tracked products; the linked-transfer field appears only when scrapping from an operation. |
| Labels + Thai candidates | `ตัดสินค้าชำรุด/สูญเสีย`; alternates `ตัดสินค้าเสีย`, `ทำลายสินค้า` for witnessed destruction; reason axis `ชำรุด / หมดอายุ / สูญหาย / ทำลายตามระเบียบภาษี`. |
| Configuration risk | **HIGH — and R4 raises a new material finding here.** `L2-OBS`: the reference scrap object has **no salvage-value field and no salvage-recovery concept of any kind**. The Boss-mandated L6 edge case "scrap with salvage value" therefore has no reference pattern to learn from at all — it is original design work for SMEsPlus, not a transfer. Recorded as `R4-F-03` and escalated to `L13`. A second, independent finding: because scrap has only draft and done states, the Boss-required scrap approval control (L7 item 4) also has no reference pattern — `R4-F-04`. |

### `INV-M05` Landed Costs — `TH-05` ต้นทุนสินค้าเพิ่มเติม

| L2 Dimension | Finding |
|---|---|
| Required fields | Cost description; cost amount; allocation basis; target document set; posting journal; company; date. |
| Optional fields | Vendor bill reference; cost account; per-line weight and volume; note. |
| Configuration drivers | Landed cost capability switch; costing method of the affected products; account determination; the target-document kind. `L2-OBS`: the reference system allows landed cost to target **either received goods or production orders**, which widens the concept beyond import cost. |
| Status / state fields | Draft, done, cancelled; plus computed adjustment lines each carrying former cost, additional cost, and final cost as three separate values (`L2-OBS`). |
| Visibility rules | Only visible when the capability is enabled and only applicable to products under a real-time-valued costing category. |
| Labels + Thai candidates | `ต้นทุนสินค้าเพิ่มเติม`; alternates `ต้นทุนนำเข้า`, `ค่าใช้จ่ายรวมเข้าต้นทุนสินค้า`. The label must signal that stock value changes. |
| Configuration risk | **HIGH.** Five allocation bases are available (`L2-OBS`: equal, by quantity, by current cost value, by weight, by volume). Weight- and volume-based allocation silently produce a zero or distorted allocation when the products carry no weight or volume — a very likely state in a Thai SME product master. Recorded as `R4-F-05`. `GAP-MD-05` and `GAP-MD-24` remain open; posting structure is `DEPENDENCY: ACCOUNTING COGS GAP` (`JT-08`). |

### `INV-M06` Run Scheduler — `TH-06` ประมวลผลแผนสต็อก

| L2 Dimension | Finding |
|---|---|
| Required fields | None from the user — it is an action, not a form. |
| Optional fields | Company scope; product or warehouse scope where offered. |
| Configuration drivers | Which rules are set to automatic; the scheduled run frequency; the planning horizon. |
| Status / state fields | Run identity, start time, completion time, outcome. `CN-35` requires a run log; `L2-OBS` confirms the reference system's own scheduled-run record is a general-purpose scheduling record, not a stock-planning-specific audit log with a business-readable outcome. SMEsPlus needs the latter. |
| Visibility rules | Should be an administrative surface, not an everyday menu — carried from `MENU-OP-06` classification `NOT APPLICABLE as user menu`. |
| Labels + Thai candidates | `ประมวลผลแผนสต็อก`; in admin `สถานะการประมวลผลอัตโนมัติ`. |
| Configuration risk | **HIGH.** Nothing in the reference pattern prevents a manual run overlapping a scheduled run, or a user pressing it repeatedly. `GAP-MD-21` (scheduler idempotency under concurrent retry) is confirmed by R4 as a real exposure, not a theoretical one — see `07` `L6-10` and the `L15` escalation. |

---

## 3. Group B — Products

### `INV-M07` Products — `TH-07` สินค้า

| L2 Dimension | Finding |
|---|---|
| Required fields | Name; product kind; default unit of measure; company or company-shared scope. |
| Optional fields | Internal code; Thai and English descriptions; purchase unit; barcode; product category; traceability policy; weight; volume; supplier list; images. |
| Configuration drivers | Traceability capability; multi-unit capability; variant capability; costing category assignment; packaging capability. |
| Status / state fields | Active/archived; can-be-sold and can-be-purchased flags; traceability selection (none / by lot / by unique serial). |
| Visibility rules | Purchase unit visible only with multi-unit enabled; traceability visible only with traceability enabled; variant tab only with variants enabled. |
| Labels + Thai candidates | `สินค้า` / `ข้อมูลสินค้า`; kinds `สินค้าคงคลัง` (stock-controlled), `วัสดุสิ้นเปลือง` (consumable), `บริการ` (service). Naming conflict `N-4` carried: consumable must be `วัสดุสิ้นเปลือง`. |
| Configuration risk | **HIGH.** `L2-OBS` confirms the reference generation expresses stock-control classification across **two interacting attributes rather than one**, which is precisely the two-axis structure the Reopen round recorded and `GAP-FS-04` / `GAP-MD-10` flagged as needing an explicit tie-break rule. R4 confirms the two-axis structure still exists in the target generation. The tie-break rule remains undefined — carried, not closed. |

### `INV-M08` Product Variants — `TH-08` สินค้าย่อย

| L2 Dimension | Finding |
|---|---|
| Required fields | Parent product; the attribute-value combination. |
| Optional fields | Variant code; variant barcode; variant-specific cost; variant image. |
| Configuration drivers | Variant capability switch; attribute definitions (`INV-M25`); whether an attribute actually creates variants or is only informational. |
| Status / state fields | Active/archived. |
| Visibility rules | Entirely hidden when variants are disabled. |
| Labels + Thai candidates | `สินค้าย่อย`; alternates `ตัวเลือกสินค้า`, `รุ่นย่อย (สี/ไซซ์)`. Stock is counted per variant, not per parent. |
| Configuration risk | **HIGH.** `GAP-FS-03` — variant identity when the attribute set changes after variants already hold stock — is unresolved and R4 does not resolve it. `IV-14` (attribute value codes immutable once used) is the candidate invariant that would contain it. R4 upgrades this menu from `HOLD / EVIDENCE REQUIRED` (`GAP-MD-08`) to **PARTIAL WITH FIRST-HAND FIELD EVIDENCE**: the field and configuration structure is now observed, but the destructive-change semantics remain unproven without a live instance test. |

### `INV-M09` Lots/Serial Numbers — `TH-09` เลขล็อต / เลขซีเรียล

| L2 Dimension | Finding |
|---|---|
| Required fields | Identifier value; product; company context. |
| Optional fields | Expiry date; best-before date; removal date; alert date; supplier batch reference; note. |
| Configuration drivers | Traceability policy on the product; expiry capability; whether valuation is tracked per batch (`L2-OBS`: the reference generation carries a per-product switch making value itself batch-level, which is a materially stronger coupling between traceability and valuation than earlier SMEsPlus rounds recorded). |
| Status / state fields | Active/archived; expiry-derived states. |
| Visibility rules | Expiry fields visible only with the expiry capability; batch-level cost visible only when batch valuation is on. |
| Labels + Thai candidates | `เลขล็อต / เลขซีเรียล`; show `วันหมดอายุ` and `สถานะประกัน` as columns. |
| Configuration risk | **HIGH — R4 raises a new finding.** `L2-OBS`: identifier uniqueness in the reference pattern is scoped to **(identifier, product, company)**, and records may exist with *no company*, which forces a cross-company duplicate check as a special case. A company-less batch identity is therefore visible and collidable across companies. This is a direct multi-company exposure and is recorded as `R4-F-06`, feeding `10_L9_SAAS_MULTI_TENANT_MULTI_COMPANY_REGISTER.md`. It also confirms `INV-04` / `IV-04` (serial uniqueness must be enforced below the application layer) as necessary rather than merely desirable. |

---

## 4. Group C — Reporting

### `INV-M10` Stock — `TH-10` ยอดสินค้าคงเหลือ

| L2 Dimension | Finding |
|---|---|
| Required fields (as displayed measures) | Product; on-hand quantity; reserved quantity; available quantity. |
| Optional fields | Incoming; outgoing; forecast; location; lot/serial; package; owner; unit of measure. |
| Configuration drivers | Multi-location; traceability; packages; consignment/ownership capability. |
| Status / state fields | None — it is derived. `CN-26` / `P-03`: on-hand is derived and never directly edited. |
| Visibility rules | Location, lot, package and owner columns each appear only with their capability enabled. |
| Labels + Thai candidates | `ยอดสินค้าคงเหลือ`; the three quantities must be labelled `คงเหลือจริง` (on hand), `จองแล้ว` (reserved), `พร้อมใช้` (available). |
| Configuration risk | **MEDIUM-HIGH.** `L2-OBS`: available quantity is clamped so it does not display below zero, while the true on-hand value can genuinely be negative. A user therefore cannot tell a real negative position from a zero position on this screen. This confirms `INV-02` / `IV-02` (negative on-hand must be displayed and flagged, not hidden) as a required divergence from the reference pattern. Recorded as `R4-F-07`. |

### `INV-M11` Locations (Reporting) — `TH-11` สินค้าคงเหลือตามตำแหน่งจัดเก็บ

| L2 Dimension | Finding |
|---|---|
| Required fields | Location; product; quantity. |
| Optional fields | Lot/serial; package; owner; value. |
| Configuration drivers | Multi-location capability; location hierarchy depth. |
| Status / state fields | None — derived. |
| Visibility rules | Hidden entirely when multi-location is off. |
| Labels + Thai candidates | `สินค้าคงเหลือตามตำแหน่งจัดเก็บ`; short `คงเหลือตามที่เก็บ`. |
| Configuration risk | **MEDIUM.** Non-physical locations (supplier, customer, loss, production counterpart, transit) will appear in a naive location report and confuse users into thinking the business holds stock it does not. The report must distinguish physical from counterpart locations by default. `L1-CF` from the v1.0 non-physical counterpart place list. |

### `INV-M12` Moves History — `TH-12` ประวัติการเคลื่อนไหวสินค้า / สต็อกการ์ด

| L2 Dimension | Finding |
|---|---|
| Required fields | Date; product; quantity; source; destination; document reference. |
| Optional fields | Lot/serial; package; owner; unit of measure; running balance; value. |
| Configuration drivers | Traceability; packages; multi-location. |
| Status / state fields | Completed movements only. Immutability is the defining property (`P-02`, `IV-05`). |
| Visibility rules | Running balance is meaningful only per product and per location context. |
| Labels + Thai candidates | `ประวัติการเคลื่อนไหวสินค้า`; Thai accountants call this `สต็อกการ์ด`. The statutory-style name `รายงานสินค้าและวัตถุดิบ` is `HOLD / EVIDENCE REQUIRED` (`TH-HOLD-01`, `GAP-MD-12`, naming conflict `N-5`) and must not be used as a label until the Accounting-Tax track confirms it. |
| Configuration risk | **MEDIUM.** The running-balance column is the field an auditor actually wants and it is derived, so its correctness depends entirely on the ordering rule used. Ordering by record-creation sequence and ordering by effective date give different running balances whenever anything is backdated — which in a Thai SME is routine. This is a real reporting-integrity requirement, recorded as `R4-F-08`. |

### `INV-M13` Stock Moves — `TH-13` รายการเคลื่อนไหวสินค้า

| L2 Dimension | Finding |
|---|---|
| Required fields | Product; demanded quantity; source; destination; state. |
| Optional fields | Done quantity; reserved quantity; scheduled date; priority; source document; lot/serial. |
| Configuration drivers | Same as `INV-M03`. |
| Status / state fields | The full lifecycle including not-yet-done states — this is what separates it from `INV-M12`. |
| Visibility rules | Should be an advanced or audit surface (`MENU-RP-04` classification). |
| Labels + Thai candidates | `รายการเคลื่อนไหวสินค้า`. |
| Configuration risk | **MEDIUM.** Two adjacent menus (`INV-M12`, `INV-M13`) whose difference is a state filter is a comprehension risk in Thai and is recorded for Thai user validation. |

### `INV-M14` Valuation — `TH-14` มูลค่าสินค้าคงเหลือ

| L2 Dimension | Finding |
|---|---|
| Required fields | Product; quantity; unit cost; total value; valuation date; company. |
| Optional fields | Location; lot/serial; costing method; remaining quantity and remaining value per cost layer; linked document; linked accounting entry. |
| Configuration drivers | Costing method and valuation mode, both carried on the product category as company-scoped properties (`L2-OBS`); account determination; landed cost capability; batch-level valuation switch. |
| Status / state fields | `L2-OBS`: each value event carries a **remaining quantity** and **remaining value** which are consumed over time. A negative remaining quantity is the marker of value released against stock that had not yet been received — the mechanism behind the retroactive cost correction described in `19_L13_PLUS_ESCALATION_REGISTER.md`. |
| Visibility rules | Only meaningful for products in a real-time-valued category. |
| Labels + Thai candidates | `มูลค่าสินค้าคงเหลือ`; must show `ณ วันที่`; naming conflict `N-3` — the header must state the policy (`ตามนโยบายต้นทุน: มาตรฐาน / ถัวเฉลี่ย / FIFO`). |
| Configuration risk | **HIGHEST IN THE MODULE. `DEPENDENCY: ACCOUNTING COGS GAP` — all conclusions locked.** `L2-OBS` establishes one fact that R4 can state without trespassing on the Accounting decision: the costing method is a property of the **product category**, scoped per company, not of the product. Changing one category value therefore re-points the costing of every product in it at once. That is a configuration-blast-radius fact, and it is exactly what makes `JT-01` (valuation policy owner) load-bearing. R4 supplies the fact; the decision stays with the Joint track. |

### `INV-M15` Warehouse Analysis — `TH-15` วิเคราะห์คลังสินค้า

| L2 Dimension | Finding |
|---|---|
| Required fields | The measure set, the period, and the grouping dimension. |
| Optional fields | Warehouse; product category; comparison period. |
| Configuration drivers | Which measures are enabled; whether value-based measures are permitted (gated by the COGS dependency). |
| Status / state fields | None — analytical. |
| Visibility rules | Should be management-facing and clearly separated from audit reports (`TH-15` note). |
| Labels + Thai candidates | `วิเคราะห์คลังสินค้า`; alternates `ภาพรวมคลังสินค้า`, `แดชบอร์ดคลังสินค้า`. Must not be confusable with audit reports. |
| Configuration risk | **MEDIUM.** `GAP-MD-25` — the measure set itself has never been evidenced or validated against what a Thai SME owner wants. R4 does not close it; it remains one of the two genuinely evidence-thin menus (Section 6). |

---

## 5. Group D — Configuration

### `INV-M16` Settings — `TH-16` ตั้งค่าระบบคลังสินค้า

| L2 Dimension | Finding |
|---|---|
| Required fields | None; it is a switch panel. |
| Optional fields | Every capability switch. |
| Configuration drivers | Company scope; licence/edition; interdependencies between switches. |
| Status / state fields | On/off per capability, per company. `CN-34` requires this set to be versioned with effective dates (`IV-15`). |
| Visibility rules | Switches reveal dependent switches; some cannot be turned off once data exists. |
| Labels + Thai candidates | `ตั้งค่าระบบคลังสินค้า`; switches worded as business options — `เปิดใช้ล็อต/ซีเรียล`, `เปิดใช้หลายตำแหน่งจัดเก็บ`. |
| Configuration risk | **HIGH.** `GAP-MD-14` (switch-off guards, versioning versus regeneration, `SAAS-04`) is unresolved. The damaging case R4 highlights is enabling traceability on a product that already holds untracked stock: the existing balance has no batch identity and the system must decide what that balance now means. No safe default is evidenced. |

### `INV-M17` Warehouses — `TH-17` คลังสินค้า

| L2 Dimension | Finding |
|---|---|
| Required fields | Name; short code; company. |
| Optional fields | Address; incoming and outgoing step configuration; resupply relationships; buy/manufacture-to-order options. |
| Configuration drivers | Multi-warehouse capability; multi-step capability; route generation. |
| Status / state fields | Active/archived. |
| Visibility rules | Step configuration visible only with multi-step enabled. |
| Labels + Thai candidates | `คลังสินค้า`. Naming conflict `N-2` is a hard rule: a warehouse must **never** be default-labelled `สาขา` (Thai tax branch). Carried as `GAP-MD-15` and `TH-HOLD-06`. |
| Configuration risk | **HIGH.** `L2-OBS`: changing a warehouse's step configuration causes its operation types, locations and routes to be re-derived. Structural re-derivation on an existing warehouse with live stock is the `SAAS-04` regeneration risk, and R4 confirms the re-derivation behaviour exists in the target generation. `CN-05` / `IV-15` (version configuration, never regenerate in place) is the required SMEsPlus divergence. |

### `INV-M18` Locations (Configuration) — `TH-18` ตำแหน่งจัดเก็บ

| L2 Dimension | Finding |
|---|---|
| Required fields | Name; parent location; location kind. |
| Optional fields | Company; barcode; storage category; cyclic counting frequency; last counted date; next expected count date; replenish-location flag; scrap-destination flag; returns-destination flag. |
| Configuration drivers | Multi-location capability; storage category capability; counting configuration. |
| Status / state fields | Active/archived. |
| Visibility rules | Kind-dependent fields appear conditionally. |
| Labels + Thai candidates | `ตำแหน่งจัดเก็บ`; system locations such as `สินค้าระหว่างรับ` need plain-Thai explanations. Five internal role names remain benchmark-derived and unvalidated (`GAP-FS-21`). |
| Configuration risk | **HIGHEST STRUCTURAL RISK, and R4 raises a new multi-company finding.** `L2-OBS`: a location's company is **optional**. A location with no company is not scoped to any single company, which is the structural mechanism by which cross-company stock visibility can occur. Recorded as `R4-F-09` and carried into the L9 register. Separately, the location *kind* is what makes an internal transfer financially neutral (`P-04`); changing a kind retrospectively re-interprets history and must be an approved, versioned change. |

### `INV-M19` Routes — `TH-19` เส้นทางการไหลของสินค้า

| L2 Dimension | Finding |
|---|---|
| Required fields | Route name; applicability scope; ordered rule set. |
| Optional fields | Company; warehouse restriction; product or category restriction; sequence. |
| Configuration drivers | Multi-step capability; warehouse step configuration; which applicability levels are enabled. |
| Status / state fields | Active/archived. |
| Visibility rules | Advanced surface; should be presented to SME users as named templates (`RT-*`), not as raw routes. |
| Labels + Thai candidates | `เส้นทางการไหลของสินค้า`; presented as `รับสินค้า 1 ขั้นตอน`, `รับแล้วตรวจคุณภาพก่อนเก็บ`. |
| Configuration risk | **HIGH.** `L2-OBS`: a company-scoped route and a rule belonging to a different company is explicitly rejected — so the company constraint here is real and enforced. That is a genuine strength worth transferring. The residual risk is comprehension, not isolation. |

### `INV-M20` Rules — `TH-20` กฎการไหลของสินค้า

| L2 Dimension | Finding |
|---|---|
| Required fields | Action; source location; destination location; operation type; company. |
| Optional fields | Supply method; delay in days; propagation behaviour; partner address; sequence/priority. |
| Configuration drivers | Route membership; warehouse configuration; operation types. |
| Status / state fields | Active/archived. |
| Visibility rules | Advanced only. |
| Labels + Thai candidates | `กฎการไหลของสินค้า`; short `กฎสินค้า`. |
| Configuration risk | **HIGH.** This is the most common origin of unexplained system behaviour and there is no user-facing explanation surface. R4 records an explainability requirement: every generated operation must name the rule that produced it (`P-06`). Without it, a Thai SME cannot self-diagnose and the module becomes support-dependent. |

### `INV-M21` Operation Types — `TH-21` ประเภทรายการคลัง

| L2 Dimension | Finding |
|---|---|
| Required fields | Name; operation class; warehouse; numbering sequence; company. |
| Optional fields | Default source and destination location; backorder policy; traceability capture options; package options; print options; reservation policy. |
| Configuration drivers | Warehouse configuration; capability switches; route generation. |
| Status / state fields | Active/archived. |
| Visibility rules | Class-dependent options. |
| Labels + Thai candidates | `ประเภทรายการคลัง`; numbering prefixes `ใบรับสินค้า RC-`, `ใบจ่ายสินค้า DO-`, `ใบโอน TR-`. |
| Configuration risk | **HIGH.** Two distinct risks. First, `L1-CF` from the Reopen round: operation classification was found to be coupled to string literals, which makes classification fragile. Second, numbering: Thai accountants and auditors expect continuity and non-reuse of document numbers, and a numbering-sequence change is a controlled change. `GAP-MD-22` (SoD matrix and Thai document numbering standards) remains open; `TH-HOLD-09` covers the delivery-document-to-tax-invoice linkage and is `HOLD / EVIDENCE REQUIRED`. |

### `INV-M22` Storage Categories — `TH-22` ประเภทพื้นที่จัดเก็บ

| L2 Dimension | Finding |
|---|---|
| Required fields | Name; company. |
| Optional fields | Maximum weight; capacity by product; capacity by package; allow-mixed-products flag. |
| Configuration drivers | Storage category capability; put-away rules that consume it. |
| Status / state fields | Active/archived. |
| Visibility rules | Hidden unless the capability is enabled. |
| Labels + Thai candidates | `ประเภทพื้นที่จัดเก็บ`; alternates `ประเภทที่เก็บ (เย็น/แห้ง/อันตราย)`, `ความจุพื้นที่`. |
| Configuration risk | **MEDIUM.** R4 upgrades this menu from `HOLD / EVIDENCE REQUIRED` (`GAP-MD-16`) to **PARTIAL WITH FIRST-HAND FIELD EVIDENCE** — the capacity and mixing-constraint structure is now observed. What remains unevidenced is whether Thai regulated-storage requirements (cold chain, chemical) map onto this structure; that stays `HOLD / EVIDENCE REQUIRED` and belongs to the Accounting-Tax and legal routing track. |

### `INV-M23` Putaway Rules — `TH-23` กฎจัดเก็บสินค้าเข้าที่

| L2 Dimension | Finding |
|---|---|
| Required fields | Applicability key (product or product category); source/when-received location; destination location; company. |
| Optional fields | Package type; storage category; sequence/priority. |
| Configuration drivers | Storage categories; location hierarchy; package capability. |
| Status / state fields | Active/archived. |
| Visibility rules | Hidden unless the capability is enabled. |
| Labels + Thai candidates | `กฎจัดเก็บสินค้าเข้าที่`; must read as `สินค้านี้รับเข้าแล้วให้ไปเก็บที่ไหน`. |
| Configuration risk | **MEDIUM-HIGH.** R4 upgrades this from `HOLD / EVIDENCE REQUIRED` (`GAP-MD-17`) to **PARTIAL WITH FIRST-HAND FIELD EVIDENCE**. The dual-ownership concern is confirmed: product category drives both put-away applicability and costing policy, which is exactly `GAP-FS-02` (is it acceptable for product category to own both, or must they be separated). R4 confirms the coupling is real in the reference pattern. The decision remains `DEPENDENCY: ACCOUNTING COGS GAP` because `JT-01` is its precondition. |

### `INV-M24` Product Categories — `TH-24` หมวดหมู่สินค้า

| L2 Dimension | Finding |
|---|---|
| Required fields | Name; parent category. |
| Optional fields | Costing method; valuation mode; account determination set; put-away applicability; removal strategy. |
| Configuration drivers | Whether valuation is real-time or manual; company scope of the costing properties. |
| Status / state fields | None beyond structure. |
| Visibility rules | Accounting fields visible only to users with accounting rights. |
| Labels + Thai candidates | `หมวดหมู่สินค้า`; if it owns valuation policy, `หมวดหมู่สินค้าและนโยบายต้นทุน`. |
| Configuration risk | **HIGHEST CONFIGURATION RISK IN THE MODULE.** `L2-OBS` establishes three facts. (1) Costing method and valuation mode are company-scoped properties of the category, so the same category can cost differently in different companies. (2) The reference system contains explicit handling for a product moving between categories with different costing methods — meaning the migration-between-methods case is real and non-trivial. (3) Category therefore simultaneously owns a *reporting* concern, an *operational* put-away concern, and a *financial* costing concern. R4's finding `R4-F-10`: this triple ownership is the structural root of `GAP-FS-02`, `JT-01` and `GAP-MD-13` alike. **R4 does not choose the owner — `DEPENDENCY: ACCOUNTING COGS GAP`, `JT-01` NOT DECIDABLE.** |

### `INV-M25` Attributes — `TH-25` คุณลักษณะสินค้า

| L2 Dimension | Finding |
|---|---|
| Required fields | Attribute name; value list. |
| Optional fields | Display type; variant-creation mode; sequence; per-value extra price. |
| Configuration drivers | Variant capability. |
| Status / state fields | Active/archived. |
| Visibility rules | Hidden unless variants enabled. |
| Labels + Thai candidates | `คุณลักษณะสินค้า`; alternates `ตัวเลือก (สี, ขนาด)`, `คุณสมบัติสินค้า`. |
| Configuration risk | **HIGH.** `L2-OBS` confirms the variant-creation mode is itself configurable — an attribute can generate variants immediately, on demand, or not at all. Changing that mode after stock exists changes what the variant set means. `IV-14` (attribute value codes immutable once used) is the containing invariant. R4 upgrades from `HOLD / EVIDENCE REQUIRED` (`GAP-MD-08`) to **PARTIAL WITH FIRST-HAND FIELD EVIDENCE**. |

### `INV-M26` Product Packagings — `TH-26` หน่วยบรรจุ

| L2 Dimension | Finding |
|---|---|
| Required fields | Packaging name; product; contained quantity in the product's base unit. |
| Optional fields | Barcode; company; whether it applies to sales, to purchases, or to both. |
| Configuration drivers | Packaging capability. |
| Status / state fields | Active/archived. |
| Visibility rules | Hidden unless the capability is enabled. |
| Labels + Thai candidates | `หน่วยบรรจุ / แพ็กสินค้า`; the distinction must be explicit — `หน่วยบรรจุ` is how goods are packed, `หน่วยนับ` is how they are counted. |
| Configuration risk | **MEDIUM-HIGH.** R4 upgrades this from `HOLD / EVIDENCE REQUIRED` (`GAP-MD-18`) to **PARTIAL WITH FIRST-HAND FIELD EVIDENCE** — a packaging structure with a contained base quantity does exist in the target generation, which corrects the earlier round's finding that no packaging model was present in the source examined then. This is a genuine R1-R3 correction and is recorded in `20_RISK_GAP_DECISION_REGISTER.md` as `R4-D-02`. The residual risk is that changing the contained quantity retrospectively re-interprets every historical document that used it. |

### `INV-M27` Reordering Rules — `TH-27` จุดสั่งซื้อ

| L2 Dimension | Finding |
|---|---|
| Required fields | Product; location; minimum quantity; maximum quantity; company. |
| Optional fields | Order multiple; preferred route; trigger mode (automatic or manual); suspension-until date; lead time; a manually-entered order quantity. |
| Configuration drivers | Multi-location; route availability; scheduler configuration. |
| Status / state fields | Trigger mode and suspension state. |
| Visibility rules | Location visible only with multi-location; route only with multi-route. |
| Labels + Thai candidates | `จุดสั่งซื้อ / กฎสั่งเติมสินค้า`; alternates `ยอดต่ำสุด-สูงสุด (min-max)`. |
| Configuration risk | **HIGH — and R4 raises the most concrete new finding in this register.** `L2-OBS`: uniqueness is enforced on the combination **(product, location, company)** only. Two rules for the same product at a *parent* location and a *child* location are therefore both permitted and both active, and the shortfall computation walks the location hierarchy. **Two overlapping rules on nested locations can each raise supply for the same shortfall.** This makes the Boss-mandated L6 edge case "reordering rule conflict" a demonstrated structural exposure rather than a hypothesis. Recorded as `R4-F-11`, carried into `07` as `L6-11`, and combined with `R4-F-01` (silent min/max inversion) this menu is the single highest-value configuration-control target in the module. |

### `INV-M28` Barcode Nomenclatures — `TH-28` รูปแบบบาร์โค้ด

| L2 Dimension | Finding |
|---|---|
| Required fields | Nomenclature name; rule set. |
| Optional fields | Per-rule pattern, encoding, type, and interpretation; whether the nomenclature follows a structured international standard. |
| Configuration drivers | Barcode capability; which nomenclature is assigned to the company. |
| Status / state fields | Active/archived; rule sequence. |
| Visibility rules | Administrative surface. |
| Labels + Thai candidates | `รูปแบบบาร์โค้ด`; alternates `มาตรฐานบาร์โค้ด (EAN-13 / GS1 / ภายใน)`. "Nomenclature" has no Thai SME equivalent — `รูปแบบ` must be used. |
| Configuration risk | **HIGH.** `L2-OBS` confirms the target generation supports both a plain and a structured-standard nomenclature, and that structured patterns can encode quantity, weight, batch and expiry. R4 upgrades this from `HOLD / EVIDENCE REQUIRED` (`GAP-MD-19`) to **PARTIAL WITH FIRST-HAND FIELD EVIDENCE**. The material risk is that a misinterpreted structured barcode produces a *plausible but wrong quantity* silently — a worse failure than a rejected scan. A scan-interpretation confirmation step is a design requirement, recorded as `R4-F-12`. |

### `INV-M29` UoM Categories — `TH-29` กลุ่มหน่วยนับ

| L2 Dimension | Finding |
|---|---|
| Required fields | Category name; member units; each unit's relation to the reference unit; rounding precision. |
| Optional fields | Unit type (reference, bigger, smaller); active flag. |
| Configuration drivers | Multi-unit capability. |
| Status / state fields | Active/archived. |
| Visibility rules | Hidden unless multi-unit is enabled. |
| Labels + Thai candidates | `กลุ่มหน่วยนับ`; must show conversion plainly — `1 โหล = 12 ชิ้น`. Thai units in scope: `ชิ้น กล่อง โหล ลัง กิโลกรัม`. |
| Configuration risk | **HIGH.** `L2-OBS` confirms two things the earlier rounds recorded as `INV-11` / `IV-11`. First, conversion across categories is refused outright, which is correct and worth transferring. Second, **the default rounding direction on conversion is upward**. Systematic upward rounding means repeated conversion can only inflate quantity, never deflate it, and the inflation is silent. For a Thai SME buying in `ลัง` and selling in `ชิ้น` this accumulates. R4 records `R4-F-13`: SMEsPlus must make the rounding direction an explicit, per-category, versioned decision rather than inheriting an implicit default. |

---

## 6. L2 Coverage Result

| Status | Count | Menus |
|---|---:|---|
| L2 COMPLETE with first-hand or carried evidence | 23 | All except those listed below |
| L2 PARTIAL — evidence-thin, named cause | 6 | `INV-M08`, `INV-M15`, `INV-M22`, `INV-M23`, `INV-M26`, `INV-M28` |
| L2 not attempted | 0 | — |

Of the six PARTIAL menus, five are PARTIAL only because their *destructive-change* or *validation* semantics cannot be proven without a live reference-instance test or Thai user input — their field and configuration structure is now first-hand evidence. Only `INV-M15` (Warehouse Analysis) remains genuinely evidence-thin at the level of what it should contain at all.

**Net movement versus the Menu Deep Challenge round:** that round recorded nine menus at `HOLD / EVIDENCE REQUIRED` for want of any evidence. R4 supplies first-hand field and configuration evidence for six of them (`INV-M08`, `INV-M22`, `INV-M23`, `INV-M25`, `INV-M26`, `INV-M28`). This is the principal gap-fill achievement of R4 at L2. It does not close `GAP-FS-20`, `GAP-MD-08`, `GAP-MD-16`, `GAP-MD-17`, `GAP-MD-18` or `GAP-MD-19` — closure requires validation, not only evidence — but it materially changes their evidence basis, and each is annotated accordingly in `20_RISK_GAP_DECISION_REGISTER.md`.

---

## 7. New L2 Findings Raised By R4

| ID | Menu | Finding | Severity |
|---|---|---|---|
| `R4-F-01` | `INV-M27` | Shortfall computation uses the greater of minimum and maximum, so an inverted min/max entry silently orders to the minimum with no error | MATERIAL |
| `R4-F-02` | `INV-M02` | Reference pattern treats the count as an attribute of the balance rather than as a document with its own lifecycle and approval state | MATERIAL |
| `R4-F-03` | `INV-M04` | Scrap carries no salvage-value concept at all in the reference pattern — salvage is original design work | MATERIAL |
| `R4-F-04` | `INV-M04` | Scrap has two states only, with no approval or rejection path — the mandated scrap approval control has no reference pattern | MATERIAL |
| `R4-F-05` | `INV-M05` | Weight- and volume-based landed cost allocation silently distorts when product weight/volume is unmaintained | MATERIAL |
| `R4-F-06` | `INV-M09` | Batch/serial identity is scoped to (identifier, product, company) and company-less identities are possible, creating a cross-company collision surface | BLOCKING for multi-company |
| `R4-F-07` | `INV-M10` | Available quantity is display-clamped at zero while true on-hand can be negative — a real negative position is indistinguishable from zero on screen | MATERIAL |
| `R4-F-08` | `INV-M12` | Running balance differs depending on whether history is ordered by entry sequence or by effective date; backdating is routine in Thai SMEs | MATERIAL |
| `R4-F-09` | `INV-M18` | A location's company assignment is optional; a company-less location is the structural mechanism for cross-company stock visibility | BLOCKING for multi-company |
| `R4-F-10` | `INV-M24` | Product category simultaneously owns reporting, put-away and costing concerns — the structural root of `GAP-FS-02` / `JT-01` | MATERIAL — `DEPENDENCY: ACCOUNTING COGS GAP` |
| `R4-F-11` | `INV-M27` | Rule uniqueness is per (product, location, company) only, so overlapping rules on nested locations can each raise supply for the same shortfall | MATERIAL |
| `R4-F-12` | `INV-M28` | A misinterpreted structured barcode yields a plausible but wrong quantity silently | MATERIAL |
| `R4-F-13` | `INV-M29` | Default conversion rounding is upward, so repeated conversion inflates quantity silently and monotonically | MATERIAL |

All thirteen are **new in R4** and none is closed by this session.

---

## 8. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
