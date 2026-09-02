# 10 — Inventory Cross-Module Handoff v1.0

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V1-001` | Jira: `ERPPLUS-139`
Status: `SMEsPlus-OWNED HANDOFF DESIGN — BUSINESS FACTS ONLY — CLOSES NO JOINT OR ACCOUNTING DECISION`
Clean-room: Layer 1. Handoffs are described as **business facts exchanged between domains**. No integration architecture, interface technology, event model or reference-ERP module boundary is described or proposed.

---

## 1. Ownership Principle

> **Inventory owns Stock Truth.** Sales, Purchase and Manufacturing own commercial or production intent and receive movement facts. Accounting owns Financial Truth and receives valuation facts. Migration owns provenance and replay. Management reporting reads everything and owns nothing.

No domain shares ownership of stock truth with Inventory. Where two domains appear to need the same fact, one of them owns it and the other receives it.

---

## 2. Handoff Register

Classification: `INV-OWNED` = Inventory owns the fact and the design is settled on the Inventory side; `ACCT-IF` = an accounting-interface requirement Inventory must satisfy; `JOINT` = an unresolved Accounting ↔ Inventory decision; `TAX-HOLD` = routed to the Accounting-Tax track with `HOLD / EVIDENCE REQUIRED`.

| ID | From → To | Fact handed over | Trigger | Receiver's obligation | Menus | Class |
|---|---|---|---|---|---|---|
| `HX-01` | Sales → Inventory | Demand: product, quantity, requested date, customer, destination, priority | Sales order confirmed | Create the delivery, reserve per policy | OP-03 | `INV-OWNED` |
| `HX-02` | Inventory → Sales | Delivered quantity, date, lot or serial, backorder status | Delivery validated | Trigger invoicing, inform the customer | OP-03, RP-04 | `INV-OWNED` |
| `HX-03` | Sales → Inventory | Cancellation or quantity change before dispatch | Sales order changed | Release the reservation, cancel the chain | OP-03 | `INV-OWNED` — symmetry with the purchase side is a carried conflict (`C-01`) |
| `HX-04` | Purchase → Inventory | Expected receipt: product, quantity, expected date, supplier, price reference | Purchase order confirmed | Create the receipt | OP-03 | `INV-OWNED` |
| `HX-05` | Inventory → Purchase | Received quantity, date, lot, over- or under-receipt | Receipt validated | Three-way match, backorder decision | OP-03 | `INV-OWNED` — over-receipt tolerance policy still open |
| `HX-06` | Inventory → Purchase | Replenishment proposal with quantity, date and suggested supplier | Reorder rule shortfall | Convert to a purchase order, or reject with a reason | OP-01 | `INV-OWNED` |
| `HX-07` | Inventory → Accounting | Receipt valuation fact | Receipt validated | Post per the timing policy | OP-03, RP-05 | `ACCT-IF` |
| `HX-08` | Accounting → Inventory | Supplier bill price against the receipt cost basis; late bill after close | Bill posted | Price variance handling; late-bill rule | RP-05 | `JOINT` (`JT-06`) |
| `HX-09` | Inventory → Accounting | Issue / cost-of-goods-sold fact | Delivery validated | Recognition timing decision | OP-03, RP-05 | `JOINT` (`JT-04`) |
| `HX-10` | Inventory → Accounting | Return facts, inbound and outbound, with cost basis | Return validated | Reversing posting | OP-03 | `JOINT` (`JT-05`, `C-03`) |
| `HX-11` | Inventory → Accounting | Adjustment fact: quantity delta, cost, reason, approver | Adjustment applied | Gain or loss posting; period handling | OP-02 | `ACCT-IF` |
| `HX-12` | Inventory → Accounting / Tax | Scrap fact plus the destruction evidence pack | Scrap validated | Loss posting; deductibility assessment | OP-04 | `ACCT-IF` + `TAX-HOLD` (`TH-HOLD-02`) |
| `HX-13` | Accounting → Inventory | Landed-cost bills and their cost types | Cost bill posted | Allocate to receipts | OP-05 | `ACCT-IF` |
| `HX-14` | Inventory → Accounting | Landed-cost allocation per receipt line | Allocation validated | Post the value change | OP-05 | `ACCT-IF` + `JOINT` on eligibility (`JT-08`) |
| `HX-15` | Accounting → Inventory | Valuation policy: timing, method, and the version in force | Policy set or changed | Apply it in valuation | CF-09, RP-05 | `JOINT` (`JT-01`, `JT-02`, `JT-03`) |
| `HX-16` | Accounting → Inventory | Period lock date; backdating exception grants with grantor, reason and expiry | Period close | Enforce the guard natively | OP-02, OP-03, OP-04 | `JOINT` (`JT-12`) |
| `HX-17` | Inventory → Accounting | Period close valuation summary and reconciliation | Close run | Closing entry | RP-05 | `JOINT` (`JT-07`) |
| `HX-18` | Manufacturing → Inventory | Component demand; expected finished-goods output | Manufacturing order confirmed | Reserve and issue components; receive output | OP-03 | `INV-OWNED` |
| `HX-19` | Inventory → Manufacturing | Consumed quantity and lot; produced quantity and lot | Consumption or output validated | Order progress; cost roll-up | OP-03 | `INV-OWNED` |
| `HX-20` | Inventory → Accounting | Manufacturing consumption and output valuation; work-in-progress timing | Consumption or output validated | Work-in-progress and finished-goods posting | RP-05 | `ACCT-IF` + `JOINT` (`JT-09`) |
| `HX-21` | Inventory ↔ Inventory (other warehouse) | Transfer out and transfer in via transit | Resupply | Confirm receipt at the destination; age open transit | OP-03 | `INV-OWNED` — cross-company path never traced (`GAP-FS-07`) |
| `HX-22` | Inventory ↔ another company | An inter-company transfer is a sale and a purchase, not one transfer | Inter-company resupply | Inter-company invoicing in both companies | OP-03 | `JOINT` (`JT-10`) |
| `HX-23` | Migration → Inventory | Master data with a provenance reference | Cutover | Validate, load, reconcile counts | PR-*, CF-* | `INV-OWNED` — provenance does not exist yet (`GAP-FS-08`) |
| `HX-24` | Migration → Inventory / Accounting | Certified opening balances, quantity and value | Cutover | Human certification; cross-proof against the opening trial balance | OP-02, RP-05 | `JOINT` (`JT-11`, `G-5`) |
| `HX-25` | Migration → Inventory | Movement history, or opening plus history from the cutover date | Cutover | Replay with a stable identity; reconcile | RP-03, RP-04 | `INV-OWNED` — depends on `C-02` |
| `HX-26` | Inventory → Management reporting | Operational indicators | Periodic | Present as management information, never as accounting figures | RP-06 | `INV-OWNED` |
| `HX-27` | Inventory → Audit / Tax | Stock card; adjustment and scrap registers; valuation as of date | On request or at period end | Statutory formats | RP-03, RP-05, R-07, R-08 | `TAX-HOLD` (`TH-HOLD-01`, `TH-HOLD-02`) |
| `HX-28` | Inventory → Accounting / Tax | Product kind as a business fact (goods against service) | Product created or kind changed | Withholding-tax applicability design | PR-01 | `TAX-HOLD` (`TH-HOLD-04`) |
| `HX-29` | Point of sale / barcode → Inventory | Scanned identification resolving to product, variant, pack or batch; and, where a point-of-sale channel exists, the sale event | Scan; sale | Resolve the scan; record the issue movement | CF-13, OP-03 | `INV-OWNED` — **candidate, `UNVALIDATED - THAI USER REVIEW REQUIRED`**; whether SMEsPlus v1.0 includes a point-of-sale channel at all is a scope question for Boss (`GAP-FS-15`) |
| `HX-30` | Inventory → Sales | Availability: on-hand, reserved, available, and the earliest promise date | Continuous | Quote and promise honestly | RP-01 | `INV-OWNED` |
| `HX-31` | Accounting → Inventory | Tax defaults carried on the product master | Product created | Carry, never interpret | PR-01 | `ACCT-IF` |

---

## 3. Handoff Roll-Up

| Class | Count | IDs |
|---|---:|---|
| `INV-OWNED` | 14 | HX-01, 02, 03, 04, 05, 06, 18, 19, 21, 23, 25, 26, 29, 30 |
| `ACCT-IF` | 7 | HX-07, 11, 12 (part), 13, 14 (part), 20 (part), 31 |
| `JOINT` (unresolved Accounting ↔ Inventory) | 9 | HX-08, 09, 10, 15, 16, 17, 22, 24, and the eligibility parts of 14 and 20 |
| `TAX-HOLD` | 4 | HX-12 (statutory part), 27, 28, and the destruction-evidence part of 12 |

**Inventory closes none of the `JOINT` or `TAX-HOLD` rows in this session.**

---

## 4. Domain-by-Domain Summary

### 4.1 Sales
Sales sends demand and cancellations; Inventory returns delivered quantities, lots, backorder status and live availability. The one design tension is *promising*: Sales wants to promise from forecast, Inventory will only guarantee from available. The design resolves it by handing Sales both numbers, clearly distinguished, and letting Sales own the promise.

### 4.2 Purchase
Purchase sends expected receipts; Inventory returns received quantities with over- and under-receipt detail, and sends replenishment proposals. Open: the over-receipt tolerance policy, and the asymmetry between sales-side and purchase-side cancellation (`C-01`).

### 4.3 Accounting
The largest and least settled interface. Inventory emits facts; Accounting owns policy, posting, the lock date and the close. Twelve Joint decisions (file 07 §7) remain open, and the valuation report cannot be finalised without the first of them.

### 4.4 Manufacturing
Applicable where the tenant manufactures. Manufacturing sends component demand and expected output; Inventory issues components, receives output, and returns consumed and produced quantities with lots. Work-in-progress recognition timing is Joint. Whether Manufacturing is in the SMEsPlus v1.0 scope at all is a programme-level question outside this file.

### 4.5 Point of sale and barcode
Barcode format definition and scan resolution are Inventory-owned. Whether a point-of-sale channel exists in v1.0, and if so whether it issues stock in real time or in end-of-day batches, is an open scope question for Boss (`GAP-FS-15`). The design requirement either way is that a sale is an ordinary issue movement with its own document type, not a special case that bypasses stock truth.

### 4.6 Migration
Migration supplies master data, opening balances and history, each with a provenance reference — which does not exist today and must be built. Opening balances require human certification against the accountant's opening trial balance.

### 4.7 Thai tax and localisation
Every statutory item is routed to the Accounting-Tax track with `HOLD / EVIDENCE REQUIRED`. Inventory supplies facts and artefacts; it asserts no Thai statutory requirement and claims no statutory report title.

---

## 5. Handoff Design Rules

| # | Rule |
|---|---|
| `HR-01` | A fact is handed over once, from its owner, with a stable identity — never re-derived independently by the receiver. |
| `HR-02` | A retried handover must be recognisable as the same fact, not treated as a second one (`C-02`). |
| `HR-03` | A receiver may reject a fact, but may not silently alter it. |
| `HR-04` | Every fact carries the reference that lets the receiver trace it back to the physical event. |
| `HR-05` | A handoff whose receiving owner is not confirmed is an open item, not a completed design — several rows above are in exactly that state. |
| `HR-06` | No handoff row in this file grants any authorization to any team. |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
