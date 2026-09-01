# Inventory Full Reopen — Accounting Dependency Register

Session: `SMEPLUS-26-09-02-INV-REOPEN-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-07 OUTPUT — ACCOUNTING BOUNDARY DISCIPLINE — NOT A GATE DECISION`

Per the execution prompt §7, every Accounting-dependent item is classified using exactly one of: `INVENTORY_OWNED_STOCK_FACT` / `ACCOUNTING_INTERFACE_REQUIREMENT` / `PENDING_ACCOUNT_SESSION` / `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` / `OUT_OF_INVENTORY_SCOPE`. This register exists to keep Inventory moving without contaminating Accounting — no item below is closed by Inventory acting alone where it touches Accounting's own authority.

---

## 1. Confirmation: Inventory Did Not Close Any Boundary Item

Per the execution prompt's explicit list of what Inventory must not independently close, this reopen's own output was checked against each:

| Boundary Item | Did any of the 20 deliverables close this? | Evidence |
|---|---|---|
| COA / Account Type / Account Group conclusions | **No.** Current Account state (COA-G01/G02 CLOSED, COA-G03 published-not-audited, G04–G08 NOT CLOSED) is cited as context only throughout. | `01` Part E; `07`, `08`, `09` all cite COA gate status without ruling on it |
| Final journal entry design | **No.** The Inventory→Accounting posting-architecture fork (direct `account.move` write vs. neutral valuation-event emission) is repeatedly named as open, never resolved. | `07_IESA` §5.9, §6.6 |
| VAT/WHT/CIT statutory conclusions | **No.** `GRPA-M18-D` (Thai WHT/PND monthly filing) is explicitly carried to Accounting/Tax ownership, not closed here; the ROUTING deep-proof states WHT-linkage-to-classification is "an Accounting/Tax design decision this research does not make." | `08_FINANCIAL` §8.2; `12_STOCKABLE...` §8, §10.4 |
| Retained earnings / current-year-earnings logic | **No.** `G-6` (no year-end retained-earnings entry found anywhere in the reference system) is named as a new design decision needed, not designed here. | `08_FINANCIAL`, `06_IDTM` §3.7 |
| Account lock-date policy as Accounting truth | **No.** `G-2`/`G-3` describe Inventory's *own* backdate-bypass mechanism as a fact, contrasted with Accounting's `account.lock_exception` as a fact — neither is prescribed as the answer for SMEsPlus. | `09_SECURITY` §3.3; `04_TBRAC` §5.4 |
| Inventory valuation-to-GL reconciliation as final Accounting closure | **No.** `G-7` (empty PDF/XLSX export stubs on the one reconciliation report) is reported as a bounded code defect, not a reconciliation ruling. | `06_IDTM` §3.7; `07_IESA` §5.10, §6.9 |
| Account × Inventory Backbone baseline | **No.** Every track that touches `N-A12-01` explicitly states `Account + Inventory Backbone Reference Baseline = HOLD` is reconfirmed, not lifted or newly declared. | `08_FINANCIAL` §1, §10; `13` |

No deliverable in this reopen crosses any of these seven lines.

---

## 2. Classification Register

### `INVENTORY_OWNED_STOCK_FACT` — Inventory decides these alone

- On-hand, reserved, available/free quantity mechanics (items 7–11, 19 of `02`)
- Warehouse/location structure and route dispatch mechanism (items 4–5, 24–26)
- Lot/serial/package traceability identity (items 20–22)
- Reservation/allocation, receipt, delivery, internal transfer, backorder mechanics (items 8, 12–15)
- Stockable/Consumable/Service routing target design itself (once Team B is authorized) — the *business fact* of what routes where is Inventory's; the *WHT correlation* is not (see below)
- Migration idempotency-key design for stock records (item 37) — the mechanism is Inventory/Migration's to design; whether it is Gate-blocking is Boss's call (`C-02`)

### `ACCOUNTING_INTERFACE_REQUIREMENT` — Inventory must emit/expose these facts; Accounting decides what to do with them

- Receipt valuation handoff, delivery/COGS handoff (items 12–13)
- Manufacturing valuation handoff / WIP close automation (item 29) — new blind spot this round
- UOM conversion facts feeding valuation calculations (item 3)
- Over-fulfillment/over-receipt facts (item 28) — Inventory exposes the gap; whether it needs a financial control is Accounting-adjacent
- Migration/provenance facts needed for reconciliation (item 35)

### `PENDING_ACCOUNT_SESSION` — genuinely Accounting's to resolve, Inventory has no further evidence to contribute

- `GRPA-M18-D` — Thai WHT/PND3/PND53 monthly statutory filing (CORR-007A hand-off; receipt by the Account Reopen track not yet confirmed — see `13` row `INV-FP-06`)
- `TH-INV-03` — Thai costing-method/valuation-norm requirement, explicitly deferred by DR-002's own A11 register to `COA-G06`, which remains not closed
- WHT-applicability-vs-routing-classification linkage (ROUTING deep-proof §10.4)

### `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` — neither domain can close alone

- **`N-A12-01` in full** — Account-led monthly/year-end close, stock cut-off, product category valuation policy, periodic/perpetual posting, carry-forward balance, GL reconciliation, retained earnings. Standing `HIGH FUNCTIONAL DESIGN GAP — REOPENED`. (item 30)
- `G-1` — lock-date/closing-sequencing, unproven
- `G-2` — asymmetric post-close correction governance (Inventory's unaudited global toggle vs. Accounting's governed exception model)
- `G-5` — migration-cutover opening-balance cross-proof (the highest AI-fabrication-risk item in the whole reopen, per Track 09)
- `G-6` — no year-end retained-earnings entry design exists
- Inventory→Accounting posting-architecture fork (direct journal write vs. neutral event emission) — `IESA §5.9`
- Return-valuation cost basis — `CONFLICTING`, item `C-03` in deliverable `13`
- Company/tenant `ir.rule` cross-domain consistency — Accounting's own side of the shared enforcement pattern (A16 scenario 9) is explicitly flagged "still pending" in its own source text, while Inventory's side is evidenced-ready
- Multi-company / cross-company transfer workflow (item 33) — touches both domains' ownership models
- Product Category's dual ownership (valuation-policy owner *and* routing/putaway-policy owner) — both Track 05 and Track 09 independently recommend Category redesign be run as one joint Accounting+Inventory design pass

### `OUT_OF_INVENTORY_SCOPE` — not Inventory's concern at all

- Legal sign-off (`GRPA-M18-E`) — Legal-owned, not Accounting or Inventory
- GROUP_A Sales+Purchase's own remaining open items (`A1`/`A2` from the RV-011 lineage) — active GROUP_A scope no longer includes Inventory as of the 2026-09-02 restructuring ruling

---

## 3. Net Position

The reopen identifies **one live pure-Inventory High item** (`N-A12-01`'s Inventory-owned facets, already evidenced) sitting inside a **joint Account×Inventory decision space** for its closure. Every other Accounting-touching item in this register is either a clean fact-handoff (`ACCOUNTING_INTERFACE_REQUIREMENT`), a confirmed non-Inventory item (`PENDING_ACCOUNT_SESSION`/`OUT_OF_INVENTORY_SCOPE`), or explicitly named for the forthcoming Account × Inventory Joint Reopen (`PENDING_ACCOUNT_INVENTORY_JOINT_SESSION`, carried forward in full to deliverable `20`).

This register does not authorize the Joint Reopen to begin on any specific finding here — that authorization is the Joint Reopen's own session prompt's to grant, per the parallel-session boundary rules in this execution prompt §4/§11.5.
