# 10 — Warehouse / Location / Route / Rule Map

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-03 OUTPUT — WAREHOUSE STRUCTURE AND FLOW-POLICY REFERENCE — NOT APPROVED DESIGN`
Clean-room boundary: business-structure learning only. No vendor model, field, rule-engine architecture, or naming is proposed for reuse. Route/rule content is expressed as Thai business templates, which is the required transformation (`Benchmark Menu -> Business Meaning -> Thai User Language -> SMEsPlus Candidate Process`).

---

## 1. The Three Questions This Map Answers

1. **Where** can stock be? (warehouse and location structure)
2. **How** does a demand become a chain of movements? (routes as business templates)
3. **Who** is allowed to do what, where? (authorization dimension — largely unknown, carried)

---

## 2. Warehouse and Location Structure (candidate reference)

> **Structural notation and node-count caveat:** the role list and grouping below are described in prose, not as a vendor-style parent-code/child-name path (e.g. no `WH/Stock`-style notation). The five internal-location roles listed (main stock, input, quality, output, packing) are **benchmark-derived and unvalidated** — they mirror the default location set a well-known reference ERP uses to model 1-/2-/3-step receipt and delivery, carried forward for structural learning only. Which of these roles Thai SME warehouses actually use, and under what names, is `UNKNOWN / EVIDENCE REQUIRED` pending TBRAC field input, not a business requirement established by this document.

Each company scopes one or more warehouses (here, a single warehouse example, Thai name "คลังหลัก", referenced elsewhere as `MENU-CF-02`). Under a warehouse, one grouping node holds no stock of its own and exists only to organize the roles beneath it. Within that grouping, business practice (candidate, unvalidated) suggests up to five internal-stock roles, used depending on how many steps a company's receipt and delivery process has:

| Location role (candidate) | Thai label (candidate) | Business meaning | When used |
|---|---|---|---|
| Main stock | "คลังสินค้า" | On-hand stock lives here; may be further divided into optional zones/shelves or a "ห้องเย็น" (cold-storage) area if the warehouse tracks bin-level detail | Always |
| Receiving holding area | "รับเข้า (รอตรวจ/รอเก็บ)" | Goods sit here after arrival, before quality check or put-away | Only in a 2- or 3-step receipt process |
| Quality-check area | "ตรวจคุณภาพ" | Goods sit here awaiting inspection | Only in a 3-step receipt process |
| Shipping staging area | "รอจัดส่ง" | Goods sit here awaiting dispatch | Only in a 2- or 3-step delivery process |
| Packing area | "แพ็กสินค้า" | Goods are packed here before staging/dispatch | Only in a 3-step delivery process |

Alongside the warehouse's internal locations, the structure also implies several non-physical ("virtual") counterpart locations that never hold real stock but serve as the other end of a movement: a vendor location (source of receipts, Thai "ผู้ขาย"), a customer location (destination of deliveries, "ลูกค้า"), a loss/scrap location ("สินค้าเสีย/สูญหาย"), an inventory-adjustment counterpart ("ปรับปรุงยอด"), a production counterpart if manufacturing applies ("การผลิต"), and an in-transit location for movements between warehouses or companies ("ระหว่างขนส่ง").

Business rules that the structure implies (candidate, not benchmark copy):

| Rule | Meaning | Control impact |
|---|---|---|
| Stock truth = internal locations only | Only quantities in internal locations are "company stock" | Valuation counts internal locations; virtual locations are counterparts |
| Every movement has one source and one destination | Movement fact is always (from, to) | Enables conservation check: Σ in − Σ out = on-hand |
| Virtual locations are exception/boundary sinks | vendor/customer = boundary; loss/adjustment = exception | Accounting handoff is triggered by crossing internal ↔ non-internal boundary |
| View locations hold nothing | Grouping only | Reporting roll-up |
| A location belongs to exactly one warehouse and one company | Tenant isolation | Cross-company movement passes through transit (workflow never traced end-to-end — Reopen `02` item 33) |

Evidence: Reopen `02` item 5 (location type enumeration CLOSED_WITH_EVIDENCE), item 4 (warehouse regeneration behaviour `SAAS-04`), item 33 (cross-company transit not traced).

---

## 3. Routes as Thai Business Templates

Benchmark meaning (process level): a route is a named flow policy; a rule is one step in that policy ("pull from A to B via operation type T", "push from A to B", "buy", "manufacture"). Rules chain backwards from the demand location until a boundary (vendor, production) is reached.

SMEsPlus candidate: **expose templates, hide rules.**

| Template ID | Thai template name | Business meaning | Locations touched | Operation types generated | Typical Thai SME |
|---|---|---|---|---|---|
| RT-R1 | รับสินค้า 1 ขั้นตอน | Goods go straight from vendor to stock | vendor → Stock | รับเข้า | Most SMEs |
| RT-R2 | รับแล้วเก็บเข้าที่ (2 ขั้นตอน) | Receive at dock, then put away | vendor → Input → Stock | รับเข้า, จัดเก็บ | Distribution with bins |
| RT-R3 | รับ-ตรวจ-เก็บ (3 ขั้นตอน) | Receive, QC, put away | vendor → Input → Quality → Stock | รับเข้า, ตรวจคุณภาพ, จัดเก็บ | Food, pharma, cosmetics |
| RT-D1 | จ่ายสินค้า 1 ขั้นตอน | Pick and ship in one document | Stock → customer | จ่ายออก | Most SMEs |
| RT-D2 | หยิบแล้วส่ง (2 ขั้นตอน) | Pick to output area, then ship | Stock → Output → customer | หยิบสินค้า, จ่ายออก | Distribution |
| RT-D3 | หยิบ-แพ็ก-ส่ง (3 ขั้นตอน) | Pick, pack, ship | Stock → Packing → Output → customer | หยิบ, แพ็ก, จ่ายออก | E-commerce fulfilment |
| RT-MTO | สั่งซื้อ/ผลิตเมื่อมีออเดอร์ | Demand triggers a purchase or manufacturing request instead of stock reservation | demand location ← buy/manufacture | (purchase / MO) | Made-to-order, project trading |
| RT-BUY | ซื้อเมื่อสินค้าต่ำกว่าจุดสั่งซื้อ | Reorder rule triggers purchase proposal | vendor → Stock | รับเข้า | All with reorder planning |
| RT-RESUPPLY | เติมจากคลังอื่น | Branch warehouse resupplied from main warehouse | WH-A Stock → transit → WH-B Stock | จ่ายออก (A), รับเข้า (B) | Multi-site SMEs |
| RT-DROP | ส่งตรงจากผู้ขายถึงลูกค้า | Vendor ships directly; stock never enters the warehouse | vendor → customer | (dropship) | Marketplace / social-commerce resellers (`GRPA-M16`) |
| RT-MFG | ผลิต (เบิกวัตถุดิบ → รับสินค้าสำเร็จรูป) | Consume raw material, produce finished goods | Stock → production → Stock | เบิกผลิต, รับผลิต | Manufacturing (conditional) |

Rules for templates (candidate):

1. A template is applied per warehouse, and may be overridden per product category or product (for example "สินค้าแช่เย็นใช้ RT-R3 เสมอ").
2. Changing a warehouse template does not alter movements already planned; it applies to new demand only (explicit effective date). Benchmark behaviour regenerates rule graphs on write (`SAAS-04`); SMEsPlus should version instead.
3. Route resolution must be deterministic and produce an explanation record ("ออเดอร์ SO-123 ใช้เส้นทาง RT-D2 เพราะคลัง WH ตั้งค่า 2 ขั้นตอน").
4. Duplicate demand must not create duplicate movement chains (idempotency): a demand identity (source document line + route + attempt) must be unique. Benchmark evidence: only quantity-remaining merges, `PARTIALLY SUPPORTED, not proven` (Reopen `02` item 24, `C-02`).
5. Raw rule editing is an advanced, audited administrator action; Thai SME users never see "rules".

---

## 4. Rules — What a Thai Administrator Needs to Know (only if advanced mode)

| Rule element | Business meaning | Thai explanation candidate |
|---|---|---|
| Action: pull | "When something is needed at B, take it from A" | ดึงจาก A ไป B เมื่อมีความต้องการ |
| Action: push | "When something arrives at A, move it on to B" | เมื่อของถึง A ให้ส่งต่อไป B |
| Action: buy | "When needed and none available, create purchase request" | สั่งซื้อเมื่อไม่พอ |
| Action: manufacture | "When needed, create manufacturing order" | สั่งผลิตเมื่อไม่พอ |
| Operation type | Which document the step creates | สร้างเอกสารประเภทใด |
| Supply method: take from stock / trigger another rule / mixed | Whether to reserve existing stock first | ใช้ของในคลังก่อนหรือไม่ |
| Lead time | Days added to planning date | ระยะเวลานำ (วัน) |

None of this is a design instruction; it is the vocabulary the process needs.

---

## 5. Authorization Dimension (carried unknown)

| Question | Status | Evidence |
|---|---|---|
| Can a user be limited to one warehouse inside a company? | `UNKNOWN / EVIDENCE REQUIRED` — no evidence either way in nine rounds | Reopen `13` U-01 |
| Can a user be limited by operation type (receive but not adjust)? | Operation-level role segregation "genuinely unitemized" | Reopen `02` item 38 |
| Is company (tenant) isolation enforced below the application layer? | ORM-layer only; DB backstop absent (`SAAS-03`); privileged bypass audit never performed | Reopen `02` item 6, `09_SECURITY` |

SMEsPlus candidate: permissions modelled on three axes (company, warehouse, operation type) plus action rights (create / confirm / adjust / scrap / count / unlock backdate). Decision belongs to Track 07 and Boss (Reopen `16` Tier 3).

---

## 6. Migration Implications

| Data | Must be preserved | Why |
|---|---|---|
| Warehouse code and name | Yes | Document numbers embed it; historical documents reference it |
| Location full path and type | Yes | Every historical movement is (from, to); quantities are per location |
| Location archive state | Yes | Empty archived bins may still appear in history |
| Route/rule configuration | **No** as configuration; **Yes** as business policy statement ("warehouse used 2-step receipt from 2024-01") | Clean-room: migrate business facts, not application architecture |
| Transit balances at cutover | Yes | In-transit stock is company stock not yet in an internal location |

---

## 7. Gaps and Gate Impact

| Gap ID | Item | Owner | Gate impact |
|---|---|---|---|
| GAP-MD-14 | Warehouse step-policy change behaviour (regeneration vs versioning) for SaaS provisioning | Track 05 / S5 | Team B precondition |
| GAP-MD-20 | Cross-warehouse / cross-company resupply through transit never traced end-to-end | Track 05 / S5; Joint Session | Blocks multi-company design, not single-company understanding |
| GAP-MD-21 | Route resolution idempotency / concurrent-retry safety | Track 04, 09 / S3, S5 | Boss decision `C-02` |
| U-01 | Warehouse-level authorization | Track 07 | Team B precondition |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
