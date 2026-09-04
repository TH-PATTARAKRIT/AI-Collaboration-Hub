# 12 — P03 CROSS-PROCESS OWNERSHIP REGISTER

**LAYER 2 — AUDIT QUARANTINE.**

Parallel peers `P01 — Procure-to-Pay` (`origin/research/…p01-procure-to-pay-2026-09-04-001`)
and `P02 — Order-to-Cash` (`origin/research/…p02-order-to-cash-2026-09-04-001`) were
running when this session executed. **No peer output was read and none is duplicated.**
Boundaries are asserted from the P03 side only; each is recorded as requiring peer
confirmation.

---

## 1. Ownership register

| ID | Boundary object | P03 position | Owner | Confirmation |
|---|---|---|---|---|
| `OWN-01` | Raw material **purchase** cost | Enters P03 already valued, as a valuation layer | **P01** | Peer confirmation required |
| `OWN-02` | Inbound freight / landed cost on materials | Applied to receipts, before P03 | **P01** | Peer confirmation required |
| `OWN-03` | **Subcontract vendor bill** | P03 consumes the *receipt price* via `extra_cost`; the bill and any price difference are P2P events | **P01**, with a P03 read | **Contested — §2** |
| `OWN-04` | Raw material **consumption** valuation | The layer value is Inventory's; P03 only sums it | **Inventory track** | Settled by the Inventory R4 / MTI lineage |
| `OWN-05` | **Finished goods unit cost** | **P03 owns it, exclusively** | **P03** | Asserted |
| `OWN-06` | Finished goods **inventory valuation** thereafter | Inventory's, once P03 has written the unit cost | **Inventory track** | Settled |
| `OWN-07` | **Joint / co-product cost allocation** | **Unowned — §3** | **None today** | Boss routing required |
| `OWN-08` | Delivery and **COGS recognition** | P03 hands a value, not an entry | **P02 / COGS track** | COGS track is at terminal HOLD |
| `OWN-09` | **Asset depreciation** of production equipment | P03 needs it; P03 must not compute it | **Asset track** | `BLK-07` open |
| `OWN-10` | **Maintenance** cost, planned and unplanned | Asset/maintenance domain | **Asset track** | `BLK-08` open |
| `OWN-11` | **Payroll** cost of production employees | P03 consumes an hourly rate; it does not own payroll | **HR / Payroll** | **Unbridged — §4** |
| `OWN-12` | Energy and utilities | No P03 path exists | **Unowned** | Boss routing required |
| `OWN-13` | Period **close** of the production account | P03 produces residues it cannot clear | **Core Accounting** | **This session's handoff** |

## 2. `OWN-03` — a contested boundary, stated so P01 can settle it

`mrp_subcontracting_account/models/mrp_production.py:10-16` sets the MO's `extra_cost` from
`last_done_receipt._get_price_unit()` — **the receipt's price, not the vendor bill's.**

Therefore, if the bill differs from the receipt price:
- for a **standard-costed** product, the difference is routed to the price-difference
  account (`…/stock_move.py:24-29`) — a P1/P3 shared path that works;
- for a **FIFO or average-costed** product, `extra_cost` was already capitalised at the
  receipt price, and the branch at `:30-32` derives the component cost by subtraction.
  **What happens to a later bill difference is a P2P question and is not visible from the
  P03 side.**

**P03 asserts nothing about it and asks P01 to state the answer.** Recorded as `DEP-06`.
This is exactly the situation the Constitution's independent-team boundary contemplates:
P03 must not supply P01 with an answer key.

## 3. `OWN-07` — genuinely unowned

The co-product / joint-product cost model is:
- **not** in P03 — the reference product expresses co-products only as by-products with
  cost shares (`11` §5), and P03 found no joint-cost object;
- **not** in the COGS track — `smeplus-cogs-targeted-resolution-status` records the Joint
  Closure branch as **content-empty**;
- **not** in Inventory — the MTI rulings govern tenancy and valuation, not joint costing.

**Three tracks, none owning it.** Recorded as `P03-GAP-02`. Routing is a Boss decision, and
P03 does not assign it, because assigning it would create exactly the kind of unilateral
cross-track adjudication that `smeplus-session-execution-pattern` forbids.

## 4. `OWN-11` — the payroll bridge does not exist in the cost direction

P03 consumes `hourly_cost` from the employee record
(`hr_hourly_cost/models/hr_employee.py:9`), or a work-centre default when no employee is
named (`mrp_workorder/models/mrp_workcenter.py:66-68`).

**Enumeration.** POPULATION: the module set in `02` §3 plus `hr_payroll_account`.
PATTERN: any reference reconciling absorbed labour to posted payroll expense.
UNIT: one function.
**Result: NO EVIDENCE FOUND — PATTERN NOT MECHANICAL.**

AAS-03 `C-06` records that this PATTERN is stated as a concept rather than as a
reproducible search string, so this negative claim is **weaker than the others in this
package** and must not be relied on to the same degree. It is carried as `DEP-07` for that
reason.

The absorbed labour credit therefore lands on whatever account `DC-07` selects, and
**nothing reconciles it to the payroll expense actually posted.** The rate is a standing
parameter; the payroll is an actual. Their difference is a labour rate variance that,
per `10` §2, the system does not recognise.

`FACT VERIFIED`, scope declared. Recorded as `DEP-07`.

## 5. What P03 hands to whom

| To | What | File |
|---|---|---|
| **Core Accounting Reconciliation** | The residues, the account-family split, the period-date defect, and the five reconciliation queries | `20` |
| **Asset track** | Independent confirmation of `CTR-C-06`; evidence for `UNR-C-03`; the observation supporting `BLK-07` | `04` §3, `10` §5, `04` §6 |
| **COGS track** | The exact FG unit-cost formula and its exclusion list | `03` §5 |
| **Inventory / MTI** | `DC-11` and the WIP wizard's company handling, for conformance | `05` §4, `06` §5 |
| **P01** | The `OWN-03` question | §2 |
| **Boss** | `BD-P03-01`, `BD-P03-02`, `P03-GAP-01`, `P03-GAP-02` | `14`, `16` |
