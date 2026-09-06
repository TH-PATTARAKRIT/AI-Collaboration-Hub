# P04 — MAINTENANCE / REPAIR / IDLE / NON-PRODUCTIVE CAUSE ATTRIBUTION

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P04-08`. Source basis series 18.

---

## 1. Source events that exist

| Event | Model | Carries cost? | Reaches the ledger? |
|---|---|---|---|
| Maintenance request | `maintenance.request` | — | **no** |
| Equipment maintenance record | `maintenance.equipment` | `cost = fields.Float('Cost')`, **one field** | **no** |
| Maintenance team / stage / schedule | `maintenance.*` | — | **no** |
| Work-centre productivity / downtime | `mrp.workcenter.productivity` (P03-owned) | loss reason, not money | **no** |

**Denominator for the negative:** every `.py` in `addons/maintenance/models/`. **Zero**
references to `account.move`; **zero** to `account.analytic`.

> **`P04-F-152`** (also carried in `CQ-P04-04`). **Maintenance cost is a statistical float.**
> There is no journal entry, no analytic item, no cost object and therefore **no accounting
> attribution of a non-productive cause anywhere in the reference product.**

## 2. Downtime linkage

Work-centre productivity records a **loss reason** and belongs to the work centre, not the
machine — P03's finding, accepted. Since equipment→work-centre exists but
operation→equipment does not, a downtime record **cannot be resolved to the equipment that
was down**, and therefore cannot be resolved to an asset.

> **The non-productive cause taxonomy the Boss policy requires has no anchor in the estate:
> the cause is recorded against a work centre, the depreciation is recorded against an asset,
> and there is no join between them.**

## 3. Separation of depreciation attribution from repair expense

The Boss policy requires these be distinct. In the estate they are **already distinct, but for
the wrong reason** — not because the design separates them, but because **repair expense never
becomes an accounting fact at all**. A repair booked as a vendor bill is an ordinary expense
with no equipment dimension; the equipment's `cost` float is not connected to it.

> **This is a separation by absence, not by control.** Recorded explicitly so that it is not
> read as the policy already being satisfied.

## 4. Double-count controls

| Control the policy needs | Present? |
|---|---|
| Depreciation attributed once and only once across productive + non-productive | **absent** — no allocation mechanism exists to control |
| Repair expense not also absorbed as machine cost | **absent**, and unnecessary today because neither reaches a cost object |
| Expensed equipment not also capitalised | **absent** — `P04-F-151` |

## 5. Disposition

> **`CQ-P04-08` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** as a **negative with a
> declared denominator**: the source events exist, they carry no accounting effect, and no
> cause-to-asset join exists.
> **Every non-productive attribution mechanism is therefore a `DESIGN CANDIDATE`**, carried to
> the Design Input Pack. **Routed to P05** for the repair/vendor-expense half, which is
> Expense-to-Pay's to own.
