# 14 — Transfer / Receipt / Delivery Handoff Map

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-05 OUTPUT — TRANSACTION FLOW AND HANDOFF REFERENCE — NOT APPROVED DESIGN`
Clean-room boundary: flows are written as Thai business documents and handoffs. Benchmark movement semantics are cited from reopen deliverables `05_IBPV` and `06_IDTM` at business level only.

Menu covered: MENU-OP-03 Transfers (umbrella for receipts, deliveries, internal transfers, returns).

---

## 1. Why "Transfers" Must Be Split for Thai Users

The benchmark groups every stock document under one "Transfers" concept differentiated by operation type. Thai warehouse staff think in three documents (รับเข้า / จ่ายออก / โอนย้าย) plus returns. This map treats them as four flows sharing one movement fact model.

---

## 2. Receipt — รับสินค้าเข้า

```text
PO confirmed (Purchase) ──▶ Receipt document created (planned qty, expected date, vendor)          [Purchase -> Inventory handoff: demand fact]
   ──▶ Goods arrive: warehouse checks vendor delivery note / tax invoice against PO
   ──▶ Enter received qty per line; assign lots/serials/expiry; choose destination (putaway)
   ──▶ Partial? create backorder for remaining or close short (policy)
   ──▶ Over-receipt? tolerance policy (benchmark: no ceiling)  [GAP-MD-06]
   ──▶ Validate: movement vendor -> stock (or -> receiving area in 2/3-step)                       [stock truth: on-hand ↑]
   ──▶ Emit receipt valuation fact (qty, cost basis reference, date)                                [Inventory -> Accounting handoff]
   ──▶ Purchase sees received qty (bill matching is Purchase/Accounting)                           [Inventory -> Purchase handoff]
```

| Aspect | Content |
|---|---|
| Input | PO lines (or manual receipt without PO — policy), vendor delivery note, physical goods. |
| Output | Validated receipt, lot records, on-hand increase, receipt valuation fact, backorder if partial. |
| Exceptions | Partial; over-receipt; wrong product; damaged at dock (return to vendor or hold); no PO; late vendor bill changing cost after period close (`FIN-DELTA-04`, Joint Session). |
| Controls | Receiver ≠ PO approver; qty vs PO check; lot mandatory when tracked; period guard on validation date. |
| Accounting impact | Receipt value = qty × cost basis (PO price or later bill, policy) — Accounting decides posting (perpetual vs periodic); `ACCOUNTING_INTERFACE_REQUIREMENT`. |
| Thai reading | ใบรับสินค้า อ้างอิงใบสั่งซื้อ และใบส่งของ/ใบกำกับภาษีของผู้ขาย. |

---

## 3. Delivery — จ่ายสินค้าออก / ส่งสินค้า

```text
SO confirmed (Sales) ──▶ Delivery document created (planned qty, customer, address)                [Sales -> Inventory handoff: demand fact]
   ──▶ Reservation per policy (at confirm / at scheduled date / manual)                             [available ↓, on-hand unchanged]
   ──▶ Pick (and pack, ship in 2/3-step); assign lots by FIFO/FEFO; print ใบส่งของ
   ──▶ Partial? backorder or close short (policy); customer notified (Sales)
   ──▶ Validate: movement stock -> customer                                                        [stock truth: on-hand ↓, reservation consumed]
   ──▶ Emit issue/COGS valuation fact (qty, cost per policy, date)                                 [Inventory -> Accounting handoff]
   ──▶ Sales sees delivered qty (invoicing is Sales/Accounting; recognition timing is a design decision, `FIN-DELTA-03`)
```

| Aspect | Content |
|---|---|
| Input | SO lines (or manual delivery), reservation policy, lot strategy. |
| Output | Validated delivery, on-hand decrease, lot history, COGS fact, backorder if partial. |
| Exceptions | Insufficient stock (wait / partial / substitute); over-delivery (no ceiling in benchmark); cancellation after reservation (release) or after done (impossible — use return); address/branch data for delivery (`GRPA-M19` unknown). |
| Controls | Picker ≠ approver of SO; lot recorded; delivery note numbering; period guard. |
| Accounting impact | COGS at delivery vs at invoice must be an explicit SMEsPlus policy (benchmark label and trigger disagree — reopen `08_FINANCIAL` `FIN-DELTA-03`). |
| Thai reading | ใบจ่ายสินค้า / ใบส่งของ อ้างอิงใบสั่งขาย; ใบกำกับภาษีเป็นเรื่องของฝ่ายขาย/บัญชี. |

---

## 4. Internal Transfer — โอนย้ายภายใน

```text
Request (manual, putaway, replenishment between warehouses, QC release) ──▶ Transfer document
   ──▶ Reserve at source; move; validate                                                             [on-hand per location changes; company total unchanged]
   ──▶ Inter-warehouse: source WH จ่ายออกไป "ระหว่างขนส่ง" -> destination WH รับเข้าจาก "ระหว่างขนส่ง"  [transit balance visible]
   ──▶ No accounting handoff within one company (valuation unchanged); cross-company transfer = sale/purchase pair (Joint Session, never traced — GAP-MD-20)
```

Controls: transfer cannot leave stock stranded in transit beyond N days without alert; destination confirmation is a separate step for inter-warehouse; lots preserved.

---

## 5. Returns — รับคืน / ส่งคืน

| Flow | Trigger | Movement | Valuation | Notes |
|---|---|---|---|---|
| Customer return | Sales credit / RMA | customer → stock (or → QC / → damaged hold) | Return valuation: cost basis is `C-03` `CONFLICTING` (original cost vs recomputed) — Joint Session | Inspect before restock; may end in scrap |
| Vendor return | Rejection / claim | stock → vendor | Reverse receipt valuation | Links to vendor credit note (Accounting) |

Benchmark: one generic return flow reverses any transfer; no damaged-goods hold state (`U-02`).

---

## 6. Partial, Backorder, Cancellation — the exception grammar

| Exception | Candidate rule | Evidence status |
|---|---|---|
| Partial receipt/delivery | User chooses: สร้างใบค้าง (backorder) or ปิดยอด (no backorder); Sales/Purchase informed | Benchmark has three non-unified partial representations across Sales/Purchase/MFG (reopen `02` item 15) — SMEsPlus must define one |
| Backorder chain | Backorder references original; both reference the source order line | Benchmark closed |
| Cancel before done | Releases reservation; cascades from SO/PO cancellation | Sales side traced; Purchase side symmetry `C-01` conflicting |
| Cancel after done | Not allowed; use return | Append-only confirmed |
| Over-fulfilment | Tolerance % per operation type; above tolerance requires approval | No ceiling in benchmark — `GAP-MD-06` |
| Backdating | Validation date must be within open period; exception audited | `G-2`/`G-3`; Joint Session |

---

## 7. Handoff Summary (this menu)

| Direction | Fact handed | Owner of the fact | Receiver's use |
|---|---|---|---|
| Purchase → Inventory | PO line demand (product, qty, expected date, vendor, price reference) | Purchase | Create receipt |
| Inventory → Purchase | Received qty/date per PO line | Inventory | 3-way match, bill control |
| Sales → Inventory | SO line demand (product, qty, date, customer, address) | Sales | Create delivery, reserve |
| Inventory → Sales | Delivered qty/date/lot per SO line | Inventory | Invoice trigger, customer info |
| Inventory → Accounting | Receipt valuation fact; issue/COGS fact; return facts; transfer none | Inventory emits; Accounting owns posting | GL posting per policy |
| MFG → Inventory / Inventory → MFG | Component consumption demand; finished goods receipt | MFG / Inventory | MO progress; WIP valuation (`FIN-DELTA-01`) |
| Inventory → Management reporting | Late deliveries, backorders, receipt lead time | Inventory | Warehouse analysis |

---

## 8. Mandatory Process Questions (umbrella)

| # | Answer |
|---|---|
| 1 Business problem | Record every physical movement of goods once, correctly, with its source document. |
| 2 Users | คลัง, หัวหน้าคลัง, จัดซื้อ (view), ฝ่ายขาย (view), บัญชี (valuation facts). |
| 3 Starting event | PO/SO confirmation; manual request; replenishment; return. |
| 4 Master data first | Products, UoM, warehouses/locations, operation types, partners (Sales/Purchase). |
| 5 Manual vs automated | Automated: document creation from orders, reservation, lot proposal, backorder creation; Manual: physical confirmation, lot entry, exception decisions. |
| 6 Quantity state change | Planned → reserved → done; on-hand per location; transit balances. |
| 7 Valuation handoff | Receipt, issue, return facts; internal none. |
| 8 Approval / SoD | Order approver ≠ validator; period guard; large exceptions escalated. |
| 9 What goes wrong | Duplicate validation on retry (idempotency `C-02`); wrong lot; partial not backordered; over-receipt unnoticed; validated in wrong period; stranded transit. |
| 10 Migration data | Open documents (planned qty) regenerated from orders; done movements as history; transit balances at cutover. |
| 11 Thai name | รับสินค้าเข้า / จ่ายสินค้าออก / โอนย้ายภายใน / รับคืน-ส่งคืน. |
| 12 Must not copy | Benchmark document/state model, benchmark document-type vocabulary, return wizard shape. |

---

## 9. Gaps Carried

| Gap ID | Item | Owner | Gate impact |
|---|---|---|---|
| GAP-MD-06 | Over-receipt / over-delivery tolerance policy | Track 03 / S1 | Team B precondition |
| GAP-MD-07 | Unified partial/backorder/return Thai user flow; damaged-goods hold | Track 03, 02 / S1 | Team B precondition |
| GAP-MD-20 | Cross-company transfer workflow | Track 05 / Joint Session | Blocks multi-company design |
| C-01 | Purchase-side cancellation cascade | Track 01 / Team A | Bounded verification |
| C-03 | Return cost basis | Track 01 / Boss | Bounded verification |
| FIN-DELTA-03 | COGS timing (delivery vs invoice) explicit decision | Track 06 / Joint Session | Blocks Joint Backbone publication |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
