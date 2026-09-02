# 04 — Inventory Process Handoff Map

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-07 OUTPUT — CROSS-DOMAIN HANDOFF MATRIX — NOT APPROVED DESIGN`
Clean-room boundary: handoffs are described as business facts exchanged between domains. No integration architecture, API, event model, or vendor module boundary is described or proposed (the posting-architecture fork is explicitly left to the Joint Session).

---

## 1. Ownership Principle (carry-forward)

`Inventory owns Stock Truth. Sales, Purchase and Manufacturing own commercial or production intent and receive movement facts. Accounting owns Financial Truth and receives valuation facts. Migration owns provenance and replay. Management Reporting reads all and owns nothing.`

Evidence: reopen `05_IBPV` (no duplicate ownership of stock truth in the reference pattern; untestable against a SMEsPlus schema until one exists), `14`, `20`.

---

## 2. Handoff Matrix

| HO ID | From → To | Fact handed | Trigger | Owner of fact | Receiver obligation | Menu(s) | Classification | Evidence / status |
|---|---|---|---|---|---|---|---|---|
| HO-01 | Sales → Inventory | Demand: product, qty, date, customer, address, route hint, priority | SO confirmed | Sales | Create delivery, reserve per policy | OP-03 | `INVENTORY_OWNED_STOCK_FACT` (receipt of demand) | R:02 item 27 — reference pattern only |
| HO-02 | Inventory → Sales | Delivered qty, date, lot/serial, backorder status | Delivery validated / backorder created | Inventory | Invoice trigger, customer communication | OP-03, RP-04 | `INVENTORY_OWNED_STOCK_FACT` | R:02 item 13 |
| HO-03 | Sales → Inventory | Cancellation / quantity change before delivery | SO change | Sales | Release reservation, cancel chain | OP-03 | `INVENTORY_OWNED_STOCK_FACT` | Sale side traced; Purchase symmetry `C-01` |
| HO-04 | Purchase → Inventory | Expected receipt: product, qty, date, vendor, price reference | PO confirmed | Purchase | Create receipt | OP-03 | `INVENTORY_OWNED_STOCK_FACT` | R:02 item 12 |
| HO-05 | Inventory → Purchase | Received qty, date, lot, over/under receipt | Receipt validated | Inventory | 3-way match, backorder decision | OP-03 | `INVENTORY_OWNED_STOCK_FACT` | R:02 item 28 (over-receipt gap `GAP-MD-06`) |
| HO-06 | Inventory → Purchase | Replenishment proposal (product, qty, date, vendor suggestion) | Rule shortfall | Inventory | Convert to PO or reject | OP-01 | `INVENTORY_OWNED_STOCK_FACT` | `GAP-MD-01` |
| HO-07 | Inventory → Accounting | Receipt valuation fact (qty, cost basis ref, date, category) | Receipt validated | Inventory emits | Post per timing policy | OP-03, RP-05 | `ACCOUNTING_INTERFACE_REQUIREMENT` | R:08 |
| HO-08 | Accounting → Inventory | Vendor bill price vs receipt cost basis; late bill after close | Bill posted | Accounting | Price variance; late-bill rule | RP-05 | `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` | R:08 FIN-DELTA-04 |
| HO-09 | Inventory → Accounting | Issue / COGS fact (qty, cost per method, date) | Delivery validated | Inventory emits | COGS timing decision (delivery vs invoice) | OP-03, RP-05 | `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` | R:08 FIN-DELTA-03 |
| HO-10 | Inventory → Accounting | Return facts (customer / vendor) with cost basis | Return validated | Inventory emits | Reverse posting | OP-03 | `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` (`C-03`) | R:13 C-03 |
| HO-11 | Inventory → Accounting | Adjustment fact (delta qty, cost, reason, approver) | Adjustment applied | Inventory emits | Gain/loss posting; period | OP-02 | `ACCOUNTING_INTERFACE_REQUIREMENT` | R:02 item 19 |
| HO-12 | Inventory → Accounting / Tax | Scrap fact + destruction evidence pack | Scrap validated | Inventory emits | Loss posting; deductibility | OP-04 | `ACCOUNTING_INTERFACE_REQUIREMENT` + `PENDING_ACCOUNT_SESSION` | `GAP-MD-04` |
| HO-13 | Accounting → Inventory | Landed-cost bills and cost-type account mapping | Cost bill posted | Accounting | Allocate to receipts | OP-05 | `ACCOUNTING_INTERFACE_REQUIREMENT` | R:08 FIN-DELTA-02 |
| HO-14 | Inventory → Accounting | Landed-cost allocation per receipt line | Allocation validated | Inventory emits | Post value change | OP-05 | `ACCOUNTING_INTERFACE_REQUIREMENT` + Joint (eligibility) | `GAP-MD-05` |
| HO-15 | Accounting → Inventory | Valuation policy (timing, method) per category; account mapping | Policy set | **Accounting / Joint** | Apply in valuation engine | CF-09, RP-05 | `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` | CR:09; `N-A12-01` |
| HO-16 | Accounting → Inventory | Period lock date; exception grants (user, reason, expiry) | Period close | Accounting | Block/allow backdated movements | OP-02, OP-03, OP-04 | `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` (`G-1`, `G-2`, `G-3`) | R:09; CR |
| HO-17 | Inventory → Accounting | Period close valuation summary and reconciliation | Close run | Inventory emits | Closing entry; retained earnings (`G-6`) | RP-05 | `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` | CR; R:20 |
| HO-18 | MFG → Inventory | Component demand; finished goods expected | MO confirmed | MFG | Reserve/issue components; receive FG | OP-03 | `INVENTORY_OWNED_STOCK_FACT` | R:02 item 29 |
| HO-19 | Inventory → MFG | Consumed qty/lot; produced qty/lot | Consumption / production validated | Inventory | MO progress; cost roll-up | OP-03 | `INVENTORY_OWNED_STOCK_FACT` | R:02 item 29 |
| HO-20 | Inventory → Accounting | Manufacturing consumption/output valuation; WIP timing | Consumption / production validated | Inventory emits | WIP and FG posting; close automation | RP-05 | `ACCOUNTING_INTERFACE_REQUIREMENT` + Joint | R:08 FIN-DELTA-01 |
| HO-21 | Inventory ↔ Inventory (other warehouse) | Transfer out / in via transit | Resupply | Inventory | Confirm receipt at destination | OP-03 | `INVENTORY_OWNED_STOCK_FACT` | `GAP-MD-20` (cross-company untraced) |
| HO-22 | Inventory ↔ other company | Inter-company transfer = sale + purchase pair | Inter-company resupply | Both companies | Inter-company invoicing | OP-03 | `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` | R:02 item 33 |
| HO-23 | Migration → Inventory | Master data (products, UoM, categories, locations, lots) with provenance | Cutover | Migration | Validate, load, reconcile counts | PR-*, CF-* | `INVENTORY_OWNED_STOCK_FACT` (design) | R:11; `GAP-MD-27` |
| HO-24 | Migration → Inventory / Accounting | Certified opening balances (qty and value) | Cutover | **Joint** | Human certification; cross-proof with opening TB | OP-02, RP-05 | `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` (`G-5`) | R:13 U-04 |
| HO-25 | Migration → Inventory | Movement history (or opening + history from cutover) | Cutover | Migration | Replay with idempotency; reconcile | RP-03, RP-04 | `INVENTORY_OWNED_STOCK_FACT` | `C-02` |
| HO-26 | Inventory → Management Reporting | KPIs: on-time %, backorders, ageing, turnover, adjustment/scrap trend | Periodic | Inventory | Present; never as accounting figures | RP-06 | `INVENTORY_OWNED_STOCK_FACT` | `GAP-MD-25` |
| HO-27 | Inventory → Audit / Tax | Stock card per product; adjustment and scrap registers; valuation as of date | On request / period | Inventory | Statutory report formats | RP-03, RP-05, TH-R07/08 | `PENDING_ACCOUNT_SESSION` (formats) | `GAP-MD-12` |
| HO-28 | Product kind → Accounting / Tax | Goods vs service nature (WHT correlation) | Product creation | Inventory (fact) | WHT applicability design | PR-01 | `PENDING_ACCOUNT_SESSION` | R:12 §8 |

---

## 3. Handoff Sequence Diagrams (business level)

### 3.1 Purchase-to-stock
```text
Purchase: PO confirmed ──HO-04──▶ Inventory: receipt planned ──goods arrive──▶ receipt validated
   ──HO-05──▶ Purchase: received qty (3-way match)
   ──HO-07──▶ Accounting: receipt valuation fact
Accounting: vendor bill posted ──HO-08──▶ Inventory/Joint: price variance, late-bill rule
Accounting: freight/duty bills ──HO-13──▶ Inventory: landed cost allocation ──HO-14──▶ Accounting
```

### 3.2 Stock-to-customer
```text
Sales: SO confirmed ──HO-01──▶ Inventory: delivery planned, reserved ──pick/ship──▶ delivery validated
   ──HO-02──▶ Sales: delivered qty/lot (invoice trigger)
   ──HO-09──▶ Accounting: COGS fact (timing policy Joint)
Customer return ──▶ Inventory: return validated ──HO-10──▶ Accounting (cost basis C-03)
```

### 3.3 Exceptions
```text
Count/adjust ──HO-11──▶ Accounting gain/loss;  Scrap ──HO-12──▶ Accounting loss + Tax evidence
Period close: Accounting lock ──HO-16──▶ Inventory guard;  Inventory close summary ──HO-17──▶ Accounting closing entry
```

### 3.4 Migration
```text
Legacy ──HO-23──▶ master data with provenance ──HO-25──▶ history replay (idempotent) ──HO-24──▶ certified opening balance ⇄ Accounting opening TB (G-5 cross-proof)
```

---

## 4. Handoff Classification Roll-Up

| Classification | Count | HO IDs |
|---|---:|---|
| `INVENTORY_OWNED_STOCK_FACT` | 12 | 01, 02, 03, 04, 05, 06, 18, 19, 21, 23, 25, 26 |
| `ACCOUNTING_INTERFACE_REQUIREMENT` | 6 | 07, 11, 12 (part), 13, 14 (part), 20 (part) |
| `PENDING_ACCOUNT_SESSION` | 4 | 12 (statutory), 27, 28, (04 destruction evidence via 12) |
| `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` | 9 | 08, 09, 10, 15, 16, 17, 22, 24, (14/20 eligibility parts) |
| `OUT_OF_INVENTORY_SCOPE` | 0 | — (legal sign-off `GRPA-M18-E` not a handoff row) |

Inventory closes none of the Joint or Account rows in this session.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
