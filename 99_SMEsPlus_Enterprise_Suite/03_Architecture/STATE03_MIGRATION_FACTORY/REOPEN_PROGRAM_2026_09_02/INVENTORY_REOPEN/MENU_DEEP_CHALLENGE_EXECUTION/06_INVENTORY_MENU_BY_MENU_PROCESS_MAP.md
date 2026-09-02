# 06 — Inventory Menu-by-Menu Process Map

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub` | Canonical Branch: `SMEsPlus` | Execution Branch: `audit/inventory-menu-deep-challenge-2026-09-02-001`
Status: `CP-03..CP-06 OUTPUT — MENU-BY-MENU PROCESS REFERENCE — CANDIDATE ONLY, NOT FINAL SOLUTION`
Clean-room boundary: every block follows `Benchmark Menu -> Business Meaning -> Thai User Language -> SMEsPlus Candidate Process -> Evidence / Gap / Gate Impact`. Benchmark facts are cited from Layer 1 reopen deliverables (`170af9ea`) and CORR-007B clean-room summaries (`9996072a`). No source code, model, field, file path, or vendor architecture is described. Thai names are candidates only.

Each menu answers: **Purpose / Input / Process / Output / Accounting-Control Impact**, then the twelve mandatory process questions (Q1 business problem; Q2 Thai users; Q3 starting event; Q4 master data first; Q5 manual vs automated; Q6 quantity state change; Q7 valuation/accounting handoff; Q8 approval/audit/SoD; Q9 what goes wrong; Q10 migration data; Q11 Thai name; Q12 must not copy). Detailed flows live in maps 08–16; this file is the single per-menu index.

---

## A. OPERATIONS

### MENU-OP-01 Replenishment — เติมสินค้า / แผนเติมสินค้า  (`CONDITIONAL`; detail: map 12)

| Purpose | Decide what to order/make/transfer before stock runs out, from rules rather than memory. |
|---|---|
| Input | Reorder rules (min/max/route), forecast (on hand + confirmed in − confirmed out), manual additions. |
| Process | Scheduler computes shortfalls → proposals listed → purchasing reviews, edits, confirms → PO / MO / transfer created in the owning domain. |
| Output | Proposal list; source documents (PO, MO, transfer); explanation per proposal. |
| Accounting / Control impact | None until receipt. Control: proposal confirm is not PO approval; automatic drafts logged. |

| Q | Answer |
|---|---|
| Q1 | Stock-outs and over-stock. |
| Q2 | จัดซื้อ, เจ้าของ, หัวหน้าคลัง, วางแผนผลิต. |
| Q3 | Scheduled run; SO confirmation; manual check. |
| Q4 | Products, warehouses, route templates, reorder rules, vendors. |
| Q5 | Auto: forecast, proposal. Manual: review, confirm. |
| Q6 | None; planned incoming created on document confirm. |
| Q7 | None. |
| Q8 | Confirm role; auto-draft cannot self-approve; run log. |
| Q9 | Duplicate proposals after retry (`C-02`); forecast ignoring unconfirmed demand; wrong UoM in min/max. |
| Q10 | Rules as policy; proposals regenerated, not migrated. |
| Q11 | เติมสินค้า / แผนเติมสินค้า. |
| Q12 | Scheduler/procurement architecture; rule object model. |
| Evidence / Gap / Gate | Dispatch mechanism proven (reopen `02` item 24); user process never studied — `GAP-MD-01`; idempotency `C-02` (Boss). Gate: Team B precondition. |

### MENU-OP-02 Inventory Adjustments — ปรับปรุงยอดสต็อก  (`MANDATORY`; detail: map 13)

| Purpose | Make system quantity equal physical quantity with an approved reason. |
|---|---|
| Input | Count sheet results or direct correction request; reason code; evidence; approval. |
| Process | Plan count → freeze policy → count → compare → recount → approve → apply as movement (adjustment ↔ stock) → register. |
| Output | Corrected on-hand; adjustment register; valuation delta fact. |
| Accounting / Control impact | Delta × cost → inventory gain/loss (Accounting posts). Controls: reason, SoD, threshold, period guard, immutability. |

| Q | Answer |
|---|---|
| Q1 | Book vs physical mismatch. |
| Q2 | คลัง, หัวหน้าคลัง, บัญชี, ผู้สอบบัญชี. |
| Q3 | Count schedule; discrepancy; year-end; migration opening balance. |
| Q4 | Products, locations, lots, reason codes, approvers. |
| Q5 | Manual: count, reason, approve. Auto: diff, thresholds, movement. |
| Q6 | On-hand ± delta; reservations affected. |
| Q7 | Gain/loss fact; period guard. |
| Q8 | Counter ≠ approver; witnessed year-end; escalate by value. |
| Q9 | Counting during receiving; stale count applied; backdating; hiding theft; opening balance without source (`G-5`). |
| Q10 | Adjustment history with reasons; certified cutover balance. |
| Q11 | ปรับปรุงยอดสต็อก (นับสต็อก sub-flow). |
| Q12 | Soft-only conflict default; global bypass toggle; conflict wizard flow. |
| Evidence / Gap / Gate | `N-A7-01` source behaviour proven, policy open; `G-2`/`G-3` Joint; Thai count practice unvalidated — `GAP-MD-02`, `GAP-MD-03`. Gate: Team B precondition; `G-2`/`G-3` block Joint Backbone. |

### MENU-OP-03 Transfers — รับสินค้าเข้า / จ่ายสินค้าออก / โอนย้ายภายใน  (`MANDATORY`; detail: maps 11, 14)

| Purpose | Record every physical movement once against its source document. |
|---|---|
| Input | PO/SO/MO lines, manual requests, returns; physical goods; lots. |
| Process | Document created from order → reserve → pick/receive → partial/backorder decisions → validate → facts emitted. |
| Output | Validated receipt/delivery/transfer; on-hand per location; valuation facts; backorders. |
| Accounting / Control impact | Receipt and delivery cross company boundary → valuation facts; internal none. Controls: SoD per operation type, period guard, tolerance. |

| Q | Answer |
|---|---|
| Q1 | One truthful movement record per physical event. |
| Q2 | คลัง, หัวหน้าคลัง; จัดซื้อ/ขาย view; บัญชี facts. |
| Q3 | Order confirmation; replenishment; return; manual. |
| Q4 | Products, UoM, locations, operation types, partners. |
| Q5 | Auto: document creation, reservation, lot proposal, backorder. Manual: confirm quantities, lots, exceptions. |
| Q6 | planned → reserved → done; on-hand per location. |
| Q7 | Receipt value, COGS, return facts. |
| Q8 | Validator ≠ order approver; period guard; over-tolerance approval. |
| Q9 | Duplicate validation; wrong lot; partial not backordered; over-receipt; stranded transit; COGS timing mismatch (`FIN-DELTA-03`). |
| Q10 | Done movements as history; open documents regenerated; transit balances. |
| Q11 | Split labels as above; umbrella รายการเคลื่อนย้ายสินค้า. |
| Q12 | Document/state model; benchmark document-type vocabulary; return wizard. |
| Evidence / Gap / Gate | Movement semantics `CARRY_FORWARD_WITH_EVIDENCE`; `C-01` cancellation conflict; `GAP-MD-06`, `GAP-MD-07`, `GAP-MD-20`. Gate: Team B precondition. |

### MENU-OP-04 Scrap — ตัดสินค้าชำรุด/สูญเสีย  (`MANDATORY`; detail: map 13)

| Purpose | Remove unusable stock with approval, reason, and a loss fact. |
|---|---|
| Input | Scrap request (product, lot, qty, location, reason, evidence). |
| Process | Identify → request → approve (threshold, statutory witness where required) → move to loss location → dispose → register. |
| Output | On-hand reduced; scrap register; loss fact. |
| Accounting / Control impact | Qty × cost → loss (Accounting posts); Thai deductibility evidence (`HOLD`). |

| Q | Answer |
|---|---|
| Q1 | Unusable stock inflating books. |
| Q2 | คลัง, หัวหน้าคลัง, QA, บัญชี, ภาษี. |
| Q3 | Damage/expiry/loss found; QC reject; return inspection. |
| Q4 | Loss location, reason codes, roles, lot tracking. |
| Q5 | Manual: request, evidence, approve. Auto: movement, fact, expiry candidates. |
| Q6 | On-hand ↓; lot ↓. |
| Q7 | Loss fact; statutory evidence pack. |
| Q8 | Requester ≠ approver; witness for destruction. |
| Q9 | Hiding theft; scrapping sellable goods; missing destruction evidence; closed-period date. |
| Q10 | Scrap history with reasons; loss location zero at cutover. |
| Q11 | ตัดสินค้าชำรุด/สูญเสีย. |
| Q12 | Scrap document shape; no damaged-goods state as default. |
| Evidence / Gap / Gate | Scrap model exists (reopen `02` item 18); `U-02` damaged-goods unknown; `GAP-MD-04` statutory `HOLD`. Gate: Team B precondition; statutory item to Accounting-Tax. |

### MENU-OP-05 Landed Costs — ต้นทุนสินค้าเพิ่มเติม  (`CONDITIONAL`; detail: map 15)

| Purpose | Add freight/duty/insurance to received goods' value. |
|---|---|
| Input | Extra-cost bills, target receipts, allocation method, cost-type account mapping (Accounting). |
| Process | Select receipts → cost lines → allocate → review → validate → cost basis updated. |
| Output | Allocation statement; adjusted cost basis; accounting facts. |
| Accounting / Control impact | Value-only change; method eligibility and posting are Joint; import VAT/duty treatment statutory `HOLD`. |

| Q | Answer |
|---|---|
| Q1 | True landed cost for margins and stock value. |
| Q2 | นำเข้า/จัดซื้อ, บัญชี. |
| Q3 | Freight/duty/broker bill. |
| Q4 | Cost types with accounts; validated receipts; costing method. |
| Q5 | Manual: select, method, review. Auto: allocation, facts. |
| Q6 | None. |
| Q7 | Value change per receipt line. |
| Q8 | Accounting approval; period guard. |
| Q9 | Allocating to sold goods; VAT included; double allocation; standard-cost products. |
| Q10 | Cost history only (Accounting). |
| Q11 | ต้นทุนสินค้าเพิ่มเติม / ต้นทุนนำเข้า. |
| Q12 | Benchmark eligibility restriction as rule; account vocabulary. |
| Evidence / Gap / Gate | Reopen `08` `FIN-DELTA-02`; never fully read — `GAP-MD-05`; `GAP-MD-24` statutory. Gate: Team B precondition (conditional). |

### MENU-OP-06 Run Scheduler — ประมวลผลแผนสต็อก  (`NOT APPLICABLE` as user menu; detail: map 12)

| Purpose | Run background planning now: forecasts, proposals, reservations, route chains. |
|---|---|
| Input | All rules and pending demands. |
| Process | Deterministic batch per company/warehouse/rule; log. |
| Output | Proposals/drafts; reservations; run log. |
| Accounting / Control impact | None. Control: idempotent, explainable, auditable; AI may flag anomalies only. |

| Q | Answer |
|---|---|
| Q1 | Planning must happen without a person remembering to run it. |
| Q2 | ผู้ดูแลระบบ (log); no end-user menu. |
| Q3 | Timer; manual "run now". |
| Q4 | Rules, routes, products. |
| Q5 | Fully automated; manual trigger only. |
| Q6 | Reservation state changes; no on-hand change. |
| Q7 | None. |
| Q8 | Run log with counts/errors; cannot create done movements. |
| Q9 | Double-run duplicates; silent failure; stale run. |
| Q10 | None. |
| Q11 | ประมวลผลแผนสต็อก (admin status only). |
| Q12 | Job/cron architecture. |
| Evidence / Gap / Gate | Reopen `11` deterministic controls; `GAP-MD-21`. Gate: Boss decision `C-02`. |

## B. PRODUCTS

### MENU-PR-01 Products — สินค้า  (`MANDATORY`; detail: map 09)

| Purpose | One identity per item traded. |
|---|---|
| Input | Names, code, barcode, kind (stockable / consumable / service), category, UoM, tracking, expiry, reorder, tax defaults. |
| Process | Create → variants → policies → activate; controlled changes; archive. |
| Output | Product master used everywhere. |
| Accounting / Control impact | Kind decides stock truth; category decides valuation policy; tax defaults Accounting-owned. |

| Q | Answer |
|---|---|
| Q1 | Consistent identity across departments. |
| Q2 | เจ้าของ, จัดซื้อ, ขาย, คลัง, บัญชี. |
| Q3 | New item; supplier catalogue; migration. |
| Q4 | UoM, categories, attributes, tax codes. |
| Q5 | Manual create; auto codes/variants/barcode check. |
| Q6 | None directly. |
| Q7 | Category inheritance; cost visibility. |
| Q8 | Type/cost changes logged; type change after stock approved. |
| Q9 | Duplicates; wrong UoM/type; migrated rows violating the type invariant (989 of 83,753 in studied data). |
| Q10 | Code, names, barcode, both type axes, UoM, category, tracking, external IDs. |
| Q11 | สินค้า / ข้อมูลสินค้า. |
| Q12 | Two-axis gate as literal schema; transliterated type labels. |
| Evidence / Gap / Gate | Reopen `12` (`INV-FP-13` CARRY_FORWARD); `GAP-MD-10` tie-break; Thai real-user validation absent. Gate: Team B precondition. |

### MENU-PR-02 Product Variants — สินค้าย่อย  (`CONDITIONAL`; detail: map 09)

| Purpose | Count stock per colour/size while managing one model. |
|---|---|
| Input | Template + attributes/values; generation mode. |
| Process | Combination → variant (SKU); own barcode/code. |
| Output | Variant grid; stock per variant. |
| Accounting / Control impact | Stock and valuation per variant; identity by attribute-value codes. |

| Q | Answer |
|---|---|
| Q1 | Retail assortments. |
| Q2 | ขาย, คลัง, จัดซื้อ. |
| Q3 | New model with options. |
| Q4 | Attributes and values. |
| Q5 | Auto generation; manual pruning. |
| Q6 | Per variant. |
| Q7 | Per variant. |
| Q8 | Cannot delete stocked variant. |
| Q9 | Renamed values breaking identity; explosion of unused variants. |
| Q10 | Attribute-value codes; variant ↔ legacy SKU map. |
| Q11 | สินค้าย่อย / ตัวเลือกสินค้า. |
| Q12 | Benchmark variant model. |
| Evidence / Gap / Gate | No prior evidence (reopen `02` item 2) — `GAP-MD-08`. Gate: Team B precondition (conditional). |

### MENU-PR-03 Lots/Serial Numbers — เลขล็อต / เลขซีเรียล  (`CONDITIONAL` menu, `MANDATORY` capability; detail: map 09)

| Purpose | Trace batch/unit for recall, expiry, warranty. |
|---|---|
| Input | Tracking mode; lot/serial values; expiry dates. |
| Process | Assign on receipt → propose by FIFO/FEFO on issue → history per lot. |
| Output | Lot master; movement history; expiry list; recall query. |
| Accounting / Control impact | No valuation effect; uniqueness must be DB-enforced in target. |

| Q | Answer |
|---|---|
| Q1 | Recall, expiry, warranty obligations. |
| Q2 | คลัง, QA, ขาย (warranty), ลูกค้าสัมพันธ์. |
| Q3 | Receipt of tracked product. |
| Q4 | Product tracking mode; expiry policy. |
| Q5 | Manual/scan entry; auto proposal and expiry alerts. |
| Q6 | Per lot balance. |
| Q7 | None. |
| Q8 | Lot immutable after first move; serial unique. |
| Q9 | Duplicate serials (benchmark detects reactively); expired lots shipped; missing expiry on receipt. |
| Q10 | Lot values, expiry, per-lot balances, history. |
| Q11 | เลขล็อต / เลขซีเรียล. |
| Q12 | App-layer-only uniqueness; benchmark lot model. |
| Evidence / Gap / Gate | Identity facts carried (`02` items 20–21); expiry workflow unread — `GAP-MD-09`; `GAP-MD-11`. Gate: Team B precondition for tracked industries. |

## C. REPORTING (detail: map 16)

### MENU-RP-01 Stock — ยอดสินค้าคงเหลือ  (`MANDATORY`)
Purpose: what we have / promised / sellable. Input: on-hand, reservations, planned. Process: aggregate done movements; subtract reservations. Output: คงเหลือจริง / จองแล้ว / พร้อมใช้ / คาดการณ์. Control: conservation check; negatives displayed. Q1 daily availability; Q2 คลัง ขาย จัดซื้อ; Q3 any time; Q4 products/locations; Q5 auto; Q6 none; Q7 none; Q8 access by warehouse; Q9 hidden negatives, planned shown as stock; Q10 none (derived); Q11 ยอดสินค้าคงเหลือ; Q12 benchmark quantity model. Evidence: `02` items 9–10; Gate: none (design requirement).

### MENU-RP-02 Locations — สินค้าคงเหลือตามตำแหน่งจัดเก็บ  (`CONDITIONAL`)
Purpose: where it is. Input: on-hand per location/lot/package. Process: location-first and product-first views. Output: bin contents, empty bins, capacity. Control: warehouse-level authorization (`U-01`). Q1 find and count; Q2 คลัง ผู้ตรวจนับ; Q3 multi-location on; Q4 location tree; Q5 auto; Q6–Q7 none; Q8 `U-01`; Q9 wrong bin data; Q10 location paths; Q11 as above; Q12 benchmark location model. Evidence: `02` item 5; Gate: `U-01` Team B precondition.

### MENU-RP-03 Moves History — ประวัติการเคลื่อนไหวสินค้า / สต็อกการ์ด  (`MANDATORY`)
Purpose: per-product running ledger for audit. Input: done lines, opening balance. Process: chronological running balance; as-of-date. Output: stock card. Control: append-only; reproducible; export tested. Q1 prove balances; Q2 บัญชี ผู้สอบบัญชี สรรพากร คลัง; Q3 audit/period end; Q4 movements; Q5 auto; Q6–Q7 none; Q8 immutability; Q9 non-reproducible as-of, export failure (`G-7` lesson); Q10 full history or certified opening + history from cutover; Q11 สต็อกการ์ด; Q12 benchmark report layout. Evidence: `02` item 38; statutory format `GAP-MD-12` `HOLD`. Gate: statutory to Accounting-Tax.

### MENU-RP-04 Stock Moves — รายการเคลื่อนไหวสินค้า  (`MANDATORY` ledger / `CONDITIONAL` menu)
Purpose: fact-level list. Input: all movement lines. Process: filter. Output: facts with state/document/qty/dates/user. Control: planned vs done distinct; migration replay base. Q1 investigation/reconciliation; Q2 บัญชี ผู้ตรวจสอบ IT; Q3 investigation; Q4 none; Q5 auto; Q6–Q7 none; Q8 immutability; Q9 planned mistaken for done; Q10 replay identities (`C-02`); Q11 รายการเคลื่อนไหวสินค้า; Q12 benchmark move model. Evidence: `05_IBPV`, `06_IDTM`. Gate: `C-02` Boss decision.

### MENU-RP-05 Valuation — มูลค่าสินค้าคงเหลือ  (`MANDATORY`; detail: map 15)
Purpose: stock value as of date under policy; reconcile to GL. Input: qty, cost per method, policy version, GL balance. Process: compute; period movement of value; reconcile. Output: valuation and reconciliation. Control: policy printed; reproducible; export. Q1 books and audit; Q2 บัญชี เจ้าของ ผู้สอบบัญชี; Q3 period end / any date; Q4 costing policy per category; Q5 auto compute, manual reconcile; Q6 none; Q7 core interface; Q8 Accounting closes; Q9 method not stated, export fails, late bills change closed period; Q10 opening value certified (`G-5`); Q11 มูลค่าสินค้าคงเหลือ ณ วันที่; Q12 benchmark report/valuation model, account vocabulary. Evidence: `N-A12-01` REOPENED; `C-03`; `G-7`; `C-05` control. Gate: **blocks Joint Backbone publication**.

### MENU-RP-06 Warehouse Analysis — วิเคราะห์คลังสินค้า  (`CONDITIONAL`)
Purpose: performance and cash tied in stock. Input: planned vs done dates, volumes, ages, values. Process: KPIs. Output: on-time %, backorders, ageing, turnover, dead stock, adjustment/scrap trend. Control: management only. Q1 decisions on space/cash/service; Q2 เจ้าของ ผู้จัดการ; Q3 weekly/monthly; Q4 documents; Q5 auto; Q6–Q7 none; Q8 not audit figures; Q9 KPI misread as accounting; Q10 none; Q11 วิเคราะห์คลังสินค้า; Q12 benchmark dashboard. Evidence: none — `GAP-MD-25`. Gate: non-blocking.

## D. CONFIGURATION (detail: maps 08, 10)

### MENU-CF-01 Settings — ตั้งค่าระบบคลังสินค้า  (`MANDATORY`)
Purpose: switch capabilities on/off per company. Input: admin choices (lots, expiry, multi-location, packages, variants, landed cost, barcode, multi-step routes, reservation policy). Process: switch reveals menus/fields; some generate records. Output: effective feature set. Control: switch-off guards; audit log; no silent regeneration (`SAAS-04`). Q1 SMEs see only what they use; Q2 ผู้ดูแลระบบ เจ้าของ; Q3 onboarding, growth; Q4 company; Q5 manual switches, auto defaults; Q6 none; Q7 valuation switches are Accounting-interface; Q8 audit every change; Q9 turning off with dependent data, regenerating flows silently; Q10 switch set as tenant policy; Q11 as above; Q12 benchmark settings structure. Evidence: `07_IESA` `SAAS-04` — `GAP-MD-14`. Gate: Team B precondition.

### MENU-CF-02 Warehouses — คลังสินค้า  (`MANDATORY`)
Purpose: physical site. Input: name, code, address, company, step policy. Process: creates locations, operation types, routes. Output: warehouse tree. Control: code is migration key; not tax branch (`GRPA-H8/H3`). Q1 where operations run; Q2 ผู้ดูแลระบบ หัวหน้าคลัง; Q3 new site; Q4 company; Q5 manual create, auto defaults; Q6 none; Q7 valuation usually company-wide (interface question); Q8 setup role; Q9 warehouse ≡ branch confusion; step change regenerating flows; Q10 code, name, locations; Q11 คลังสินค้า; Q12 benchmark regeneration behaviour. Evidence: `02` item 4 — `GAP-MD-15`. Gate: Team B precondition.

### MENU-CF-03 Locations — ตำแหน่งจัดเก็บ  (`MANDATORY` defaults / `CONDITIONAL` bins)
Purpose: where stock sits. Input: name, parent, type, warehouse, storage category. Process: tree; every move from→to. Output: location tree; on-hand per location. Control: types closed enumeration; system locations undeletable; `U-01`. Q1 physical/logical place; Q2 หัวหน้าคลัง; Q3 layout change; Q4 warehouse; Q5 manual; Q6 none; Q7 boundary crossing triggers valuation; Q8 archive only when empty; Q9 stock in view locations, wrong type; Q10 full path, type, archive state; Q11 ตำแหน่งจัดเก็บ; Q12 benchmark location model. Evidence: `02` item 5 CLOSED; `U-01`. Gate: `U-01` Team B precondition.

### MENU-CF-04 Routes — เส้นทางการไหลของสินค้า  (`CONDITIONAL`)
Purpose: how demand becomes movements. Input: template choice per warehouse/category/product. Process: resolve template → movement chain. Output: chains, purchase/MO requests. Control: deterministic, explainable, versioned. Q1 multi-step flows, MTO, resupply, dropship; Q2 ผู้ดูแลระบบ; Q3 setup; Q4 warehouses, locations, operation types; Q5 manual template pick, auto resolution; Q6 none; Q7 none; Q8 advanced audited edit; Q9 duplicate chains on retry; opaque resolution; Q10 policy statement only; Q11 as above (templates); Q12 route/rule object model. Evidence: `02` items 24–25 — `REWRITE_AS_CLEAN_ROOM_LEARNING`. Gate: Team B precondition.

### MENU-CF-05 Rules — กฎการไหลของสินค้า  (`CONDITIONAL`, hidden)
Purpose: one step of a route. Input: action (pull/push/buy/manufacture), from/to, operation type, supply method, lead time. Process: chained by resolution. Output: planned movements. Control: hidden behind templates; audited. Q1–Q12 as MENU-CF-04; Q11 กฎการไหลของสินค้า; Q12 rule engine architecture. Evidence: same. Gate: same.

### MENU-CF-06 Operations Types — ประเภทรายการคลัง  (`MANDATORY`; detail: map 11)
Purpose: document kinds with numbering, defaults, roles. Input: name, warehouse, direction, sequence, default locations, return type, reservation policy. Process: auto-created per warehouse; extras added. Output: series; dashboards. Control: SoD unit; direction decides valuation. Q1 distinct documents Thai staff recognise; Q2 ผู้ดูแลระบบ หัวหน้าคลัง; Q3 warehouse creation; Q4 warehouse, locations; Q5 auto defaults, manual extras; Q6 none; Q7 inbound/outbound → valuation; Q8 SoD per type (`GAP-MD-22`); Q9 wrong default locations, shared sequences; Q10 series and prefixes; Q11 ประเภทรายการคลัง; Q12 benchmark document-type vocabulary, string-literal kind coupling. Evidence: `02` item 14; `02` item 38. Gate: Team B precondition.

### MENU-CF-07 Storage Categories — ประเภทพื้นที่จัดเก็บ  (`CONDITIONAL`)
Purpose: capacity/condition constraints of places. Input: limits, allowed content, mixing rules. Process: putaway consults capacity. Output: capacity-aware destination. Control: advisory by default. Q1 cold/hazard/weight limits; Q2 หัวหน้าคลัง; Q3 bin management; Q4 locations; Q5 manual setup, auto check; Q6–Q7 none; Q8 none; Q9 blocking receipts when full; Q10 none; Q11 as above; Q12 benchmark model. Evidence: none — `GAP-MD-16`. Gate: non-blocking.

### MENU-CF-08 Putaway Rules — กฎจัดเก็บสินค้าเข้าที่  (`CONDITIONAL`)
Purpose: where to store on arrival. Input: product/category/package → destination/storage category; priority. Process: most specific rule wins; capacity filter. Output: suggested bin. Control: explainable; never overrides explicit choice; category dual ownership. Q1 consistent storage; Q2 คลัง; Q3 receipt; Q4 locations, categories; Q5 auto suggestion, manual override; Q6 none (location assignment); Q7 none; Q8 none; Q9 conflicting rules; Q10 rules as policy; Q11 as above; Q12 benchmark rule model, category coupling. Evidence: none — `GAP-MD-17`; `14` §2. Gate: Team B precondition (category design joint).

### MENU-CF-09 Product Categories — หมวดหมู่สินค้า  (`MANDATORY`; detail: maps 08, 15)
Purpose: grouping + valuation policy owner candidate. Input: tree, removal strategy, valuation timing, costing method, accounts (Accounting). Process: inheritance; controlled policy change. Output: effective policy per product. Control: highest accounting impact; `C-05` control. Q1 report grouping and consistent costing; Q2 บัญชี เจ้าของ; Q3 setup; Q4 company, accounts; Q5 manual; Q6 none; Q7 core policy owner (Joint); Q8 policy change approval with effective date; Q9 category move changing valuation silently; Q10 tree + policy history; Q11 หมวดหมู่สินค้าและนโยบายต้นทุน; Q12 category model, account fields, dual ownership. Evidence: CORR-007B `09` Layer 1; `N-A12-01` REOPENED — `GAP-MD-13`. Gate: **blocks Joint Backbone publication**.

### MENU-CF-10 Attributes — คุณลักษณะสินค้า  (`CONDITIONAL`)
Purpose: variant axes. Input: attribute, values, mode. Process: template assignment → variants. Output: grid. Control: stable value codes. Q1 assortments; Q2 ขาย จัดซื้อ; Q3 new model; Q4 none; Q5 manual; Q6–Q8 none; Q9 renaming values; Q10 value codes; Q11 คุณลักษณะสินค้า; Q12 benchmark attribute model. Evidence: none — `GAP-MD-08`. Gate: conditional.

### MENU-CF-11 Product Packagings — หน่วยบรรจุ  (`CONDITIONAL`)
Purpose: pack sizes for entry/barcode. Input: product, name, qty in base, barcode. Process: conversion to base on documents. Output: base-unit stock. Control: not UoM. Q1 buy by carton, count by piece; Q2 คลัง ขาย จัดซื้อ; Q3 supplier packs; Q4 UoM; Q5 manual; Q6 none; Q7 none; Q8 none; Q9 double conversion; Q10 pack definitions; Q11 หน่วยบรรจุ; Q12 benchmark packaging-via-unit representation. Evidence: DR-002 note — `GAP-MD-18`. Gate: non-blocking.

### MENU-CF-12 Reordering Rules — จุดสั่งซื้อ  (`CONDITIONAL`; detail: map 12)
Purpose: min/max policy per product/location. Input: min, max, route, horizon, trigger mode. Process: forecast vs min → proposal. Output: proposals. Control: opt-in automation, explanation. Q1 automatic reorder points; Q2 จัดซื้อ; Q3 setup; Q4 products, routes; Q5 manual rules, auto evaluation; Q6 none; Q7 none; Q8 confirm role; Q9 wrong UoM, archived products; Q10 rules as policy; Q11 จุดสั่งซื้อ; Q12 benchmark reorder-rule model. Evidence: `02` item 24 — `GAP-MD-23`. Gate: Team B precondition (conditional).

### MENU-CF-13 Barcode Nomenclatures — รูปแบบบาร์โค้ด  (`CONDITIONAL`)
Purpose: parse scans. Input: rules (pattern, type). Process: first match parses product/lot/qty. Output: parsed scan. Control: mis-parse = wrong movement. Q1 scanning accuracy; Q2 ผู้ดูแลระบบ; Q3 barcode ops; Q4 products with barcodes; Q5 manual rules, auto parse; Q6 none; Q7 none; Q8 none; Q9 overlapping patterns; Q10 barcode values; Q11 รูปแบบบาร์โค้ด; Q12 benchmark nomenclature model. Evidence: none — `GAP-MD-19`. Gate: non-blocking.

### MENU-CF-14 UoM Categories — กลุ่มหน่วยนับ  (`MANDATORY`; detail: map 09)
Purpose: convertible unit groups. Input: group, units, factors, rounding. Process: convert to base. Output: base-unit stock. Control: versioned factors; rounding explicit. Q1 buy/count/sell in different units; Q2 ผู้ดูแลระบบ จัดซื้อ; Q3 setup; Q4 none; Q5 manual; Q6 none; Q7 conversion affects valuation; Q8 base unit immutable; Q9 retroactive factor edits (benchmark non-retroactive, rounding up default); Q10 units, factors, versions; Q11 กลุ่มหน่วยนับ; Q12 benchmark unit tree model. Evidence: `02` item 3. Gate: design requirement.

---

## E. Cross-Menu Summary

| Question | Answer across menus |
|---|---|
| Which menus carry stock truth? | OP-02, OP-03, OP-04 (movements); PR-01/PR-03 (identity); CF-02/CF-03 (where). Reports read it; configuration shapes it. |
| Which menus emit accounting facts? | OP-03 (receipt/delivery/return), OP-02, OP-04, OP-05; RP-05 presents; CF-09 owns policy candidate. |
| Which menus are pure Inventory-owned? | Replenishment proposals, transfers internal, locations, routes, operation types, storage/putaway, packagings, barcode, UoM, stock/location/history/moves reports. |
| Which are Joint? | Valuation, Product Categories policy, landed cost eligibility/posting, period close, cutover opening balance. |
| Which need Thai real-user validation before design? | All (structural TBRAC gap); most acutely OP-02, OP-03 split, OP-04 reasons, CF-02 branch labelling, RP-03 statutory format. |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
