# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_project_stock Module Bridge MVQ Bank — SUPPLEMENT R4

**Document ID:** GMVQ-G08-SALE_PROJECT_STOCK-MVQ-SUPPLEMENT-R4-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_project_stock`
**Wave:** W2 (GMVQ 25-Team Acceleration, 2026-09-27)
**Parent Bank:** G08_SALE_PROJECT_STOCK_GMVQ_MVQ_36_V1.00_DRAFT.md
**Parent count:** 36 (Q001–Q036)
**Questions added:** 12 (Q037–Q048)
**actual_mvq_count (resulting):** 48
**Author Cell:** P-S11 (GMVQ Production Team, GMVQ 25-Team Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**CHANGE_REASON:** Parent bank was authored to 36 material questions and honestly stopped below the
48-question floor set by GMVQ_AUTHORING_STANDARD_V1.00 §2 rather than padded. This supplement was
commissioned to establish, honestly, whether further genuine three-participant (order + project +
physical goods movement) seam ground exists per GMVQ_BRIDGE_MODULE_RULE_V1.00. Twelve additional
seam questions were found that survive the bridge test (§2: the question fails only when order,
project and stock movement are all three present) and do not duplicate any HYPOTHESIS already on
disk in this parent bank or in any sibling G08_SALES bank, per the pre-authoring check in
GMVQ_BRIDGE_MODULE_RULE_V1.00 §5.

## Pre-authoring check performed

`grep -h 'HYPOTHESIS' G08_SALES/*.md` was read in full (1502 matching lines across the group) before
authoring, together with the full text of the parent bank and its neighbours `sale_project`,
`sale_stock`, `sale_purchase`, `sale_purchase_stock` and the base `sale` bank. The twelve questions
below were checked individually against that list and against each other for the forbidden shapes in
GMVQ_BRIDGE_MODULE_RULE_V1.00 §4 (nouns-swapped restatement, base-module restatement with the
bridge's name attached, a question any sibling bank already asks). Ground that was considered and
REJECTED as already covered or as not surviving the bridge test:
- "a project spanning two warehouses" — already covered by the parent bank's existing question on a
  project spanning multiple physical locations feeding one order's delivery (Q012-equivalent ground).
- "material issued to a project site then returned to a different warehouse" as a bare return — the
  parent bank already covers an undifferentiated return; only the different-location variant below
  is new, because it changes which stock record must be reconciled.

## Questions

```yaml
QID: G08-SALE_PROJECT_STOCK-Q037
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Material issued to a project site from one stock location and later returned to a different stock
  location updates the order's own delivered-quantity record through the same documented path as a
  return to the original location.
WHY_IT_MATTERS: >
  If a return to a different location is not recognized the same way, the order's delivered figure
  and the company's stock records would silently disagree about where the returned quantity actually
  sits.
DISCONFIRMING_OBSERVATION: >
  A return of previously delivered project material to a different stock location than the one it was
  issued from either fails to reduce the order's delivered-quantity record or is not reflected in the
  receiving location's own stock figures.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Issue material to a project site from one stock location, return the unused portion to a different
  stock location, and check whether the order's delivered figure and both locations' stock figures
  agree.
```

```yaml
QID: G08-SALE_PROJECT_STOCK-Q038
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Closing a project while material already shipped toward it has not yet been recorded as received
  results in a documented treatment of that in-transit quantity, rather than the project simply
  losing any record that it is still owed.
WHY_IT_MATTERS: >
  In-transit material with no owner once its destination project is closed could be lost from both
  the order's and the project's own tracking with no one accountable for it.
DISCONFIRMING_OBSERVATION: >
  Closing a project with material already shipped but not yet received leaves that in-transit
  quantity with no visible record in either the order's or any successor record's tracking.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Ship material toward a project site, close the project before that shipment is recorded as
  received, and check what happens to the in-transit quantity's record.
```

```yaml
QID: G08-SALE_PROJECT_STOCK-Q039
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Rescheduling a project task to a date after the order's already-committed delivery date does not
  silently leave material already reserved to that task counted as still promised against the
  order's original committed date.
WHY_IT_MATTERS: >
  A stale reservation tied to a date that has already passed could make the order appear ready to
  deliver when the actual work reserving that material has moved out.
DISCONFIRMING_OBSERVATION: >
  A task rescheduled past the order's committed delivery date keeps its material reservation showing
  against the original committed date with no update or flag reflecting the new schedule.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Reserve material to a project task, reschedule that task to a date after the order's own
  committed delivery date, and check whether the reservation record reflects the change.
```

```yaml
QID: G08-SALE_PROJECT_STOCK-Q040
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Material consumption logged against a project whose funding line still sits on an unconfirmed
  quotation is not counted by the order's own delivered or fulfilled status calculations until that
  quotation is actually confirmed.
WHY_IT_MATTERS: >
  Treating consumption against a not-yet-committed quotation as fulfilling a real order would let
  stock move out and a project draw material for work the customer has not yet actually agreed to
  pay for.
DISCONFIRMING_OBSERVATION: >
  Material consumption logged against a project tied to an unconfirmed quotation is reflected in
  that quotation's own delivered or fulfilled figures before the quotation is confirmed as an order.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attach a project to a quotation before it is confirmed, log material consumption against the
  project, and check whether the quotation's own status reflects that consumption before
  confirmation.
```

```yaml
QID: G08-SALE_PROJECT_STOCK-Q041
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Deleting a project task that already has material reserved to it releases that reservation back to
  the order's own available pool through a documented action, rather than leaving it reserved
  against a task that no longer exists.
WHY_IT_MATTERS: >
  A reservation left attached to a deleted task would make that material appear unavailable to the
  order indefinitely with no task left to ever consume it.
DISCONFIRMING_OBSERVATION: >
  Deleting a project task that has material reserved to it leaves that material still shown as
  reserved with no task left to reference and no documented release back to the order.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Reserve material to a project task, delete that task, and check whether the reservation is
  released back to the order's own available pool.
```

```yaml
QID: G08-SALE_PROJECT_STOCK-Q042
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project's forecast future material requirement, entered before any material is actually issued,
  that already exceeds what the order's line has remaining to deliver is flagged at the point it is
  entered rather than only once the excess is actually issued.
WHY_IT_MATTERS: >
  Catching an over-commitment only after the material physically moves is more disruptive and harder
  to correct than catching it while it is still a plan.
DISCONFIRMING_OBSERVATION: >
  A forecast project material requirement already exceeding the order line's remaining deliverable
  quantity produces no flag until the excess material is actually issued.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Enter a forecast material requirement for a project task that exceeds the funding order line's
  remaining undelivered quantity, before issuing any material, and check whether it is flagged at
  entry.
```

```yaml
QID: G08-SALE_PROJECT_STOCK-Q043
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Where one order line's delivery to a single project site is split across more than one separate
  shipment, the order's delivered-quantity figure correctly reflects the sum of all of those
  shipments rather than only the first one received.
WHY_IT_MATTERS: >
  An order appearing complete after only a partial shipment would let invoicing or reporting treat a
  still-open commitment as satisfied.
DISCONFIRMING_OBSERVATION: >
  An order line delivered to one project site across more than one shipment shows as fully
  delivered, or stops updating, before every shipment toward it has actually arrived.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Deliver one order line's quantity to a single project site across more than one separate shipment,
  and check whether the order's delivered figure reflects the running total correctly.
```

```yaml
QID: G08-SALE_PROJECT_STOCK-Q044
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where the order line prices a quantity in one unit of measure and the project's own material
  requirement is tracked in a different unit of measure for the same item, the reconciliation
  between what the order shows delivered and what the project shows consumed converts consistently
  between the two.
WHY_IT_MATTERS: >
  An unconverted or inconsistently converted unit of measure would make the order's delivered figure
  and the project's consumption figure permanently disagree without either being wrong on its own
  terms.
DISCONFIRMING_OBSERVATION: >
  The order's delivered quantity and the project's consumption quantity for the same underlying
  material disagree once expressed in a common unit of measure, with no conversion reconciling
  them.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure an order line and its funding project's material requirement for the same item in two
  different units of measure, deliver and consume material, and check whether the two figures
  reconcile in a common unit.
```

```yaml
QID: G08-SALE_PROJECT_STOCK-Q045
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Stock present at a project site but not owned by the company, held there temporarily rather than
  issued against the order, is excluded from what the order's own delivered-quantity figure counts
  as fulfilled.
WHY_IT_MATTERS: >
  Counting material the company does not yet own or has not yet issued as delivered against the
  order would overstate fulfilment before any real transfer of ownership occurred.
DISCONFIRMING_OBSERVATION: >
  Stock present at a project site under a non-owned or not-yet-issued status is counted in the
  order's own delivered-quantity figure as though it had been issued against the order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place stock the company does not yet own at a project site alongside stock actually issued against
  the order, and check whether the order's delivered figure distinguishes the two.
```

```yaml
QID: G08-SALE_PROJECT_STOCK-Q046
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where a project's material request must be approved by one person before a different person
  actually issues the stock, the record of the approval and the record of the eventual issue are
  both retained and remain linked, even when the two happen at very different times.
WHY_IT_MATTERS: >
  Losing the link between who approved a project's material request and who actually issued it would
  break the ability to reconstruct accountability for a movement well after the fact.
DISCONFIRMING_OBSERVATION: >
  A project material issue that required a separate approval step shows the actual issue event with
  no retained, linked record of who approved the request that authorized it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Approve a project material request through one user action, have the actual stock issue performed
  later by a different user, and check whether the two events remain linked in the record.
```

```yaml
QID: G08-SALE_PROJECT_STOCK-Q047
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where two separate project tasks each independently reserve material against the same order line,
  the combined reservation is checked against that line's own remaining quantity, rather than each
  task's reservation being validated on its own as if the other did not exist.
WHY_IT_MATTERS: >
  Validating each task's reservation in isolation could let the combined total silently exceed what
  the order line was ever able to deliver, discovered only once actual issue is attempted.
DISCONFIRMING_OBSERVATION: >
  Two project tasks each reserve material against the same order line, and the combined reserved
  quantity exceeds the line's own remaining deliverable quantity with no flag raised at the time the
  second reservation was made.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Reserve material to one project task against an order line, then reserve additional material to a
  second task against the same line such that the combined total exceeds the line's remaining
  quantity, and check whether this is flagged.
```

```yaml
QID: G08-SALE_PROJECT_STOCK-Q048
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A credit note issued against an order line after its material has already been delivered to and
  consumed by the project does not, by itself, reverse the project's own record of that material as
  consumed.
WHY_IT_MATTERS: >
  If a credit note silently reversed already-consumed project material, the project's consumption
  record would no longer reflect what actually physically happened on site.
DISCONFIRMING_OBSERVATION: >
  Issuing a credit note against an order line whose material was already delivered to and consumed
  by the project changes the project's own consumption record for that material with no separate,
  visible action having done so.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Deliver and consume project material against an order line, issue a credit note against that line,
  and check whether the project's own consumption record for that material changes.
```
