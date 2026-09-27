# SMEsPlus ENTERPRISE SUITE
## GMVQ — G05 INVENTORY / stock_fleet Module MVQ Bank

**Document ID:** GMVQ-G05-STOCK_FLEET-MVQ48-V1.00
**Group:** G05 INVENTORY
**Module Metadata:** `stock_fleet`
**Wave:** W2
**Author Cell:** P07 (GMVQ Question Factory — Bridge Module Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose
This bank supplies the module-specific research questions for `stock_fleet` — the seam between
vehicles as the physical means of a stock movement and the movement itself. It is written for a
blind two-lane study: Lane A reads reference source, Lane B observes a running system, and
neither sees the other's answers. Question text is source-neutral throughout and never names
the module.

## Control
- `stock_fleet` is a BRIDGE module (GMVQ_BRIDGE_MODULE_RULE_V1.00). Every question below passes
  the seam test: if the vehicle/fleet capability were removed and stock movements ran without it,
  the question would no longer make sense.
- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` distinct from every other
  question's; no two questions share a disconfirming event.
- No padding: 48 questions test 48 distinct hypotheses spread across weight/volume capacity versus
  assigned quantity, overlapping vehicle bookings, ownership and valuation of goods in transit, a
  vehicle failing after loading, driver as a constraint distinct from the vehicle, trip cost
  attribution back to goods, a movement completed with no vehicle where one was required, archived
  vehicle records that historical movements still reference, and cross-company vehicle use.
- This bank is DRAFT authoring output only. Not approved, not frozen, not verified.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived here.

---

## G05-STOCK_FLEET-Q001

```yaml
QID: G05-STOCK_FLEET-Q001
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A movement is not allowed to be assigned to a vehicle whose declared weight or volume capacity
  the assigned quantity already exceeds at the moment of assignment.
WHY_IT_MATTERS: >
  Assigning a load a vehicle cannot actually carry is discovered, at best, when the vehicle fails
  to move it and, at worst, once it is already in transit.
DISCONFIRMING_OBSERVATION: >
  A quantity exceeding the vehicle's declared capacity is assigned with no block or warning.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to assign a quantity that exceeds a vehicle's declared weight or volume capacity to that
  vehicle, and observe whether the assignment is blocked or flagged.
```

## G05-STOCK_FLEET-Q002

```yaml
QID: G05-STOCK_FLEET-Q002
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Vehicle capacity is checked on weight and volume independently, rather than one dimension
  standing in for both, since a load can fail one dimension while satisfying the other.
WHY_IT_MATTERS: >
  A single combined check can pass a load that is actually too bulky but not too heavy, or too
  heavy but not too bulky, missing the failure entirely.
DISCONFIRMING_OBSERVATION: >
  A load that exceeds only the volume limit while remaining under the weight limit, or the
  reverse, is not flagged because only one of the two dimensions is actually evaluated.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Assign a load that exceeds the vehicle's volume limit while staying under its weight limit, and
  a second load with the reverse profile, and observe whether either is flagged.
```

## G05-STOCK_FLEET-Q003

```yaml
QID: G05-STOCK_FLEET-Q003
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the goods on an already-assigned movement change after vehicle assignment, the capacity
  check runs again against the new totals rather than the original assignment standing unexamined.
WHY_IT_MATTERS: >
  A capacity check that only ever runs once, at assignment time, misses every overload created by
  a later change to the goods.
DISCONFIRMING_OBSERVATION: >
  Increasing the assigned quantity after a vehicle is already attached produces no re-check
  against that vehicle's capacity.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Assign a movement to a vehicle within capacity, then increase the assigned quantity beyond that
  vehicle's capacity, and observe whether a re-check occurs.
```

## G05-STOCK_FLEET-Q004

```yaml
QID: G05-STOCK_FLEET-Q004
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A vehicle with no declared capacity figures is treated as unknown or blocking for a capacity
  check, not as though it always has sufficient capacity.
WHY_IT_MATTERS: >
  Silently treating an unspecified capacity as unlimited removes the very safeguard the capacity
  check exists to provide.
DISCONFIRMING_OBSERVATION: >
  A vehicle with no recorded capacity accepts an assignment of any size with no distinction from a
  vehicle known to have ample capacity.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Assign a large quantity to a vehicle with no declared capacity figures, and compare the result
  against assigning the same quantity to a vehicle with a known, ample capacity.
```

## G05-STOCK_FLEET-Q005

```yaml
QID: G05-STOCK_FLEET-Q005
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When one movement is split across more than one vehicle because no single vehicle can carry the
  full quantity, each vehicle's share is checked with reference to what the other vehicles already
  carry of that same movement, not in isolation.
WHY_IT_MATTERS: >
  Checking each partial assignment in isolation can let the same over-limit condition recur on
  every vehicle in the split without ever being caught.
DISCONFIRMING_OBSERVATION: >
  Splitting one movement across several vehicles allows each vehicle individually to be
  over-assigned because the check does not consider the other vehicles' shares of the same
  movement.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Split a single movement whose total exceeds any one vehicle's capacity across two vehicles, and
  check whether each vehicle's own capacity is still individually respected.
```

## G05-STOCK_FLEET-Q006

```yaml
QID: G05-STOCK_FLEET-Q006
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where a vehicle's capacity figure can be overridden for a specific assignment, that override is
  distinguishable in the record from the vehicle's standing declared capacity.
WHY_IT_MATTERS: >
  An invisible override makes an assignment that only cleared because of a one-off exception look
  identical to one that cleared against the vehicle's normal, standing capacity.
DISCONFIRMING_OBSERVATION: >
  An assignment that only clears capacity because of a per-assignment override shows identically
  to one that cleared against the vehicle's standing capacity, with the override itself invisible.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Override a vehicle's capacity figure for one specific assignment, and compare the resulting
  record against an assignment that cleared against the vehicle's unmodified standing capacity.
```

## G05-STOCK_FLEET-Q007

```yaml
QID: G05-STOCK_FLEET-Q007
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the goods' weight or volume is recorded in a different unit of measure than the vehicle's
  declared capacity, a conversion is applied before the two are compared, rather than the mismatch
  letting an actually over-capacity load appear to pass.
WHY_IT_MATTERS: >
  A capacity check that compares numbers in different units without converting them is comparing
  numbers that have no real relationship to each other.
DISCONFIRMING_OBSERVATION: >
  Goods recorded in one unit are compared directly against a vehicle capacity declared in a
  different unit with no conversion, letting an actually-over-capacity load pass the check.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record a load's weight or volume in a unit different from the vehicle's declared capacity unit,
  in a case that is genuinely over capacity once converted, and observe the check's result.
```

## G05-STOCK_FLEET-Q008

```yaml
QID: G05-STOCK_FLEET-Q008
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reducing the quantity assigned to a vehicle after assignment frees up the corresponding capacity
  for another assignment, rather than leaving the vehicle marked as though it still carries the
  original, larger amount.
WHY_IT_MATTERS: >
  Capacity that is not actually released after a reduction blocks other assignments the vehicle
  could genuinely still accommodate.
DISCONFIRMING_OBSERVATION: >
  Reducing the assigned quantity leaves the vehicle's committed capacity unchanged, blocking
  assignments that the actual remaining capacity would allow.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Assign a vehicle to near its full capacity, reduce the assigned quantity, and attempt a new
  assignment that should now fit within the freed-up capacity.
```

## G05-STOCK_FLEET-Q009

```yaml
QID: G05-STOCK_FLEET-Q009
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A vehicle cannot be confirmed against a second movement whose time window overlaps a first
  movement it is already confirmed against without at least a surfaced conflict.
WHY_IT_MATTERS: >
  A vehicle cannot physically be in two places doing two movements at once; an undetected double
  booking is discovered only when one of the two movements cannot actually happen.
DISCONFIRMING_OBSERVATION: >
  Two movements with overlapping time windows are both confirmed against the same vehicle with no
  conflict surfaced to whoever made the second assignment.
EXPECTED_SURFACE: S1,S5,S8
PRECONDITIONS: >
  Confirm a vehicle against one movement, then attempt to confirm the same vehicle against a
  second movement whose time window overlaps the first.
```

## G05-STOCK_FLEET-Q010

```yaml
QID: G05-STOCK_FLEET-Q010
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where an overlap produces only a warning rather than a hard block, the person confirming the
  second assignment is shown which specific other movement it conflicts with, not a generic notice
  with nothing to act on.
WHY_IT_MATTERS: >
  A warning that does not say what it conflicts with gives the person confirming it nothing to
  investigate or resolve.
DISCONFIRMING_OBSERVATION: >
  The conflict warning gives no way to identify which other movement is causing it.
EXPECTED_SURFACE: S5
PRECONDITIONS: >
  Trigger an overlap warning by assigning a vehicle to a second, overlapping movement, and inspect
  whether the warning identifies the specific conflicting movement.
```

## G05-STOCK_FLEET-Q011

```yaml
QID: G05-STOCK_FLEET-Q011
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a first movement's time window shifts after a second, non-overlapping assignment was
  already confirmed, the second assignment is re-checked against the new window rather than the
  now-real overlap going undetected.
WHY_IT_MATTERS: >
  A schedule shift that creates a new overlap is just as real a double-booking as one that existed
  from the start, whether or not the check happens to run again.
DISCONFIRMING_OBSERVATION: >
  A schedule change that creates a new overlap between two already-confirmed assignments produces
  no re-evaluation or notice.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Confirm two non-overlapping assignments to the same vehicle, then shift the first movement's
  time window so it now overlaps the second, and observe whether anything re-checks the pair.
```

## G05-STOCK_FLEET-Q012

```yaml
QID: G05-STOCK_FLEET-Q012
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Two movements assigned to the same vehicle with genuinely non-overlapping, sequential time
  windows are not blocked or flagged as though they conflicted.
WHY_IT_MATTERS: >
  A check that treats any second assignment to a busy vehicle as a conflict, whether or not the
  times actually overlap, blocks entirely legitimate sequential use of the same vehicle.
DISCONFIRMING_OBSERVATION: >
  A vehicle already assigned to one movement cannot be assigned to a second, clearly non-
  overlapping movement without triggering the same conflict handling as a genuine overlap.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Assign a vehicle to one movement, then assign it to a second movement whose time window follows
  the first with no overlap, and observe whether any conflict is raised.
```

## G05-STOCK_FLEET-Q013

```yaml
QID: G05-STOCK_FLEET-Q013
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  For a vehicle shared across more than one company, an overlap check for one company's movement
  also considers commitments already confirmed by the other company sharing the same vehicle.
WHY_IT_MATTERS: >
  A vehicle shared across companies can be double-booked in a way neither company's own records
  alone would ever reveal, if each company only checks against itself.
DISCONFIRMING_OBSERVATION: >
  A vehicle shared across companies can be double-booked because the overlap check for one
  company's movement never considers the other company's already-confirmed assignment to the same
  vehicle.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Share a vehicle across two companies, confirm an assignment from one company, and attempt an
  overlapping assignment to the same vehicle from the other company.
```

## G05-STOCK_FLEET-Q014

```yaml
QID: G05-STOCK_FLEET-Q014
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Force-confirming a movement against a vehicle despite a detected overlap is recorded distinctly
  from a confirmation made with no conflict present.
WHY_IT_MATTERS: >
  An unrecorded override of a detected double-booking removes the ability to know later that the
  conflict was knowingly accepted rather than missed.
DISCONFIRMING_OBSERVATION: >
  A forced confirmation over a detected overlap is stored identically to an ordinary conflict-free
  confirmation, with the override itself untraceable.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Force-confirm a movement against a vehicle despite a detected overlap, and compare the resulting
  record against an ordinary confirmation with no conflict.
```

## G05-STOCK_FLEET-Q015

```yaml
QID: G05-STOCK_FLEET-Q015
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  While goods are recorded as in transit on a vehicle, the record gives a single, consistent
  answer for which location or party currently holds them, rather than allowing two different
  parts of the record to disagree.
WHY_IT_MATTERS: >
  A record that cannot say where goods actually are during transit cannot be relied on for
  ownership, valuation, or responsibility questions raised during that window.
DISCONFIRMING_OBSERVATION: >
  During transit, one part of the record shows the goods as still at the origin while another
  shows them already at the destination, with no single answer resolvable.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Put goods into a recorded in-transit state on a vehicle, and query which location or party the
  record treats as currently holding them from more than one angle.
```

## G05-STOCK_FLEET-Q016

```yaml
QID: G05-STOCK_FLEET-Q016
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The valuation applied to goods while in transit is fixed at the moment they were loaded, rather
  than silently changing if the underlying valuation basis moves while the goods are still on the
  vehicle and not yet received anywhere.
WHY_IT_MATTERS: >
  Goods in transit are, for accounting purposes, frozen in a specific state; a value that drifts
  while nothing observable has happened to the goods misstates what actually occurred.
DISCONFIRMING_OBSERVATION: >
  The recorded value of in-transit goods changes between loading and receipt with no event to
  explain why, purely because of a background revaluation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Load goods onto a vehicle, trigger a change to the underlying valuation basis while they remain
  in transit, and compare the goods' recorded value before and after.
```

## G05-STOCK_FLEET-Q017

```yaml
QID: G05-STOCK_FLEET-Q017
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Goods in transit across a company or warehouse boundary have a defined point at which ownership
  or value transfers, rather than leaving a gap where the goods are, in effect, unowned by either
  side.
WHY_IT_MATTERS: >
  An undefined ownership gap during transit means neither side's books, nor a court asked to
  settle a loss, has a clear answer for who was responsible at the moment something went wrong.
DISCONFIRMING_OBSERVATION: >
  Querying the goods' owning company while the vehicle is between origin and destination returns
  neither the origin nor the destination company, or returns both simultaneously.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Load goods for a movement that crosses a company or warehouse boundary, and query the owning
  party while the vehicle is between the two.
```

## G05-STOCK_FLEET-Q018

```yaml
QID: G05-STOCK_FLEET-Q018
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the vehicle carrying in-transit goods is swapped for a different vehicle mid-trip, the
  in-transit record follows the goods to the new vehicle rather than remaining attached to the
  original, now-uninvolved vehicle.
WHY_IT_MATTERS: >
  A record that still shows goods on a vehicle no longer carrying them makes any question about
  where the goods actually are, or who is responsible for them, unanswerable from the system.
DISCONFIRMING_OBSERVATION: >
  After a mid-trip vehicle swap, the record still shows the goods as being carried by the original,
  now-uninvolved vehicle.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Load goods onto a vehicle, swap them to a different vehicle mid-trip, and inspect which vehicle
  the in-transit record shows afterward.
```

## G05-STOCK_FLEET-Q019

```yaml
QID: G05-STOCK_FLEET-Q019
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Simply assigning a vehicle to a movement, with no actual loading event recorded, does not by
  itself produce an in-transit state for the goods.
WHY_IT_MATTERS: >
  Goods that are shown as in transit before they have actually left anywhere misrepresent both
  their physical location and their accounting state.
DISCONFIRMING_OBSERVATION: >
  Simply assigning a vehicle to a movement, with no loading event recorded, is enough to show the
  goods as in transit.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Assign a vehicle to a movement without recording an actual loading event, and check whether the
  goods show as in transit.
```

## G05-STOCK_FLEET-Q020

```yaml
QID: G05-STOCK_FLEET-Q020
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When only part of a movement's quantity has actually been loaded onto the vehicle, the in-transit
  and valuation state reflects only what was actually loaded, not the movement's full quantity.
WHY_IT_MATTERS: >
  Treating unloaded goods as already in transit overstates what is actually moving and misstates
  where the remaining quantity really is.
DISCONFIRMING_OBSERVATION: >
  A movement with only part of its quantity actually loaded onto the vehicle shows the full
  quantity as in transit.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Load only part of a movement's total quantity onto a vehicle, and inspect what quantity the
  in-transit and valuation state reflects.
```

## G05-STOCK_FLEET-Q021

```yaml
QID: G05-STOCK_FLEET-Q021
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling a trip after loading but before delivery returns the goods and their value cleanly to
  the origin, rather than leaving a portion stranded in an in-transit state with no vehicle or
  location claiming it.
WHY_IT_MATTERS: >
  Goods left recorded as in transit with nothing actually carrying them are effectively lost from
  the record even though they physically still exist somewhere.
DISCONFIRMING_OBSERVATION: >
  Cancelling a trip after loading leaves the goods recorded as in transit with no further movement
  returning them to a real location.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Load goods onto a vehicle, cancel the trip before delivery, and inspect whether the goods and
  their value are returned to a real location.
```

## G05-STOCK_FLEET-Q022

```yaml
QID: G05-STOCK_FLEET-Q022
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a vehicle becomes unavailable after goods have already been loaded onto it, there is a
  defined path for those goods distinct from ordinary movement cancellation, rather than leaving
  them with no vehicle and no defined next state.
WHY_IT_MATTERS: >
  Already-loaded goods with a failed vehicle are a live operational problem; treating the case as
  an ordinary cancellation, or defining no path at all, leaves real goods with nowhere to go in the
  record.
DISCONFIRMING_OBSERVATION: >
  A vehicle marked unavailable after loading leaves the already-loaded goods with no defined status
  and no prescribed next action.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Load goods onto a vehicle, mark that vehicle unavailable, and observe what defined status or
  action applies to the already-loaded goods.
```

## G05-STOCK_FLEET-Q023

```yaml
QID: G05-STOCK_FLEET-Q023
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Transferring an already-loaded quantity from a now-unavailable vehicle to a replacement vehicle
  is itself a recorded event, rather than the replacement vehicle simply appearing as the carrier
  with no trace of the substitution.
WHY_IT_MATTERS: >
  An untraceable substitution removes the ability to later explain why the record shows a
  different vehicle than the one originally loaded.
DISCONFIRMING_OBSERVATION: >
  Swapping the carrying vehicle after loading leaves no record that a substitution occurred, only
  the end state.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Substitute the carrying vehicle for an already-loaded quantity, and inspect the record for
  evidence that a substitution, rather than an original assignment, took place.
```

## G05-STOCK_FLEET-Q024

```yaml
QID: G05-STOCK_FLEET-Q024
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a load is transferred to a replacement vehicle after the original became unavailable, the
  capacity check runs again against the replacement vehicle's own limits.
WHY_IT_MATTERS: >
  A substitution that bypasses the capacity check can carry over a load the replacement vehicle
  cannot actually handle.
DISCONFIRMING_OBSERVATION: >
  A load moved onto a replacement vehicle is not re-checked against that vehicle's own capacity
  limits.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Substitute a vehicle carrying a load that would exceed the replacement vehicle's own declared
  capacity, and observe whether the check is re-run.
```

## G05-STOCK_FLEET-Q025

```yaml
QID: G05-STOCK_FLEET-Q025
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A vehicle becoming unavailable before anything was loaded onto it is resolved as a simple
  reassignment, without invoking whatever heavier recovery handling exists for a post-loading
  failure.
WHY_IT_MATTERS: >
  Applying heavy in-transit-recovery handling to a case where nothing was ever loaded adds
  unnecessary friction to what should be a routine reassignment.
DISCONFIRMING_OBSERVATION: >
  An unavailability that occurs before any loading forces the same recovery handling as a
  post-loading failure, with no distinction made.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Mark a vehicle unavailable before any goods have been loaded onto it, and compare the resulting
  handling against a vehicle that becomes unavailable after loading.
```

## G05-STOCK_FLEET-Q026

```yaml
QID: G05-STOCK_FLEET-Q026
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Driver eligibility is checked as a constraint independent of vehicle capacity, so an assignment
  with a suitable vehicle but no qualified driver is blocked just as an assignment with a qualified
  driver but an unsuitable vehicle would be.
WHY_IT_MATTERS: >
  A vehicle capable of carrying the load is not enough on its own; treating driver and vehicle as
  one combined check can let an unstaffed movement proceed.
DISCONFIRMING_OBSERVATION: >
  An assignment with a suitable vehicle but no qualified driver recorded is allowed to proceed as
  if the driver constraint did not exist.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Assign a suitable vehicle to a movement with no qualified driver recorded, and observe whether
  the assignment is blocked or flagged.
```

## G05-STOCK_FLEET-Q027

```yaml
QID: G05-STOCK_FLEET-Q027
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A driver assigned to two movements with overlapping time windows is detected as its own
  conflict, independent of which vehicles are involved in either movement.
WHY_IT_MATTERS: >
  A driver, like a vehicle, cannot be in two places at once; checking only vehicle overlap misses a
  double-booked driver on two different vehicles.
DISCONFIRMING_OBSERVATION: >
  A driver double-booked across two overlapping movements on two different vehicles produces no
  conflict, because only vehicle overlap is checked.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Assign the same driver to two different vehicles for movements with overlapping time windows,
  and observe whether a conflict is detected.
```

## G05-STOCK_FLEET-Q028

```yaml
QID: G05-STOCK_FLEET-Q028
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a driver becomes unavailable after assignment while the vehicle they were assigned to remains
  available, the movement's readiness state reflects the missing driver rather than appearing
  fully staffed because only the vehicle side is checked.
WHY_IT_MATTERS: >
  A movement that looks fully staffed while it actually has no driver will be discovered unstaffed
  only when it is time to depart.
DISCONFIRMING_OBSERVATION: >
  A movement with an available vehicle but a now-unavailable driver shows no different readiness
  state than one with both available.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Assign a vehicle and driver to a movement, make the driver unavailable while the vehicle remains
  available, and observe the movement's readiness state.
```

## G05-STOCK_FLEET-Q029

```yaml
QID: G05-STOCK_FLEET-Q029
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a movement type is explicitly configured as not requiring a driver, it is not blocked or
  flagged for lacking one.
WHY_IT_MATTERS: >
  A universal driver requirement that ignores movement types genuinely configured not to need one
  blocks legitimate work for no reason.
DISCONFIRMING_OBSERVATION: >
  A movement type explicitly configured as not requiring a driver is still blocked or flagged for
  missing one.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Configure a movement type as not requiring a driver, create a movement of that type with no
  driver recorded, and observe whether it is blocked or flagged.
```

## G05-STOCK_FLEET-Q030

```yaml
QID: G05-STOCK_FLEET-Q030
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The driver on a movement can be reassigned without touching the vehicle assignment, as a
  distinct, permitted action.
WHY_IT_MATTERS: >
  Forcing a vehicle re-assignment just to change the driver adds friction and risk to what should
  be an isolated, low-impact change.
DISCONFIRMING_OBSERVATION: >
  There is no way to change only the driver on an assignment without also re-touching the vehicle
  assignment.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Attempt to change only the driver on an existing vehicle-and-driver assignment, leaving the
  vehicle assignment untouched.
```

## G05-STOCK_FLEET-Q031

```yaml
QID: G05-STOCK_FLEET-Q031
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A cost recorded against a trip has a defined mechanism, even if optional, by which it can be
  attributed back to the goods that trip carried.
WHY_IT_MATTERS: >
  A trip cost with no path to the goods it served cannot be reflected in what those goods actually
  cost the business to deliver.
DISCONFIRMING_OBSERVATION: >
  A trip cost is recorded with no mechanism, even optional, by which it could be attributed to the
  goods it carried.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a cost against a completed trip, and check whether any mechanism exists to attribute that
  cost to the goods the trip carried.
```

## G05-STOCK_FLEET-Q032

```yaml
QID: G05-STOCK_FLEET-Q032
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a single trip carries goods for more than one company, the trip's cost is split across them
  by a defined basis, rather than landing wholesale on whichever movement happened to be recorded
  first.
WHY_IT_MATTERS: >
  Charging the full cost of a shared trip to only one company misstates that company's cost and
  gives the others a free ride at its expense.
DISCONFIRMING_OBSERVATION: >
  A shared trip's cost is charged in full to one company or movement with no allocation to the
  others whose goods were also carried.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Carry goods for two different companies on a single trip with a recorded cost, and inspect how
  that cost is allocated between them.
```

## G05-STOCK_FLEET-Q033

```yaml
QID: G05-STOCK_FLEET-Q033
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a trip's actual cost is known only after the goods it carried have already been received
  and valued, that later cost has a defined path to adjust the goods' valuation.
WHY_IT_MATTERS: >
  A trip cost that never reaches the goods it was meant to be part of leaves the goods permanently
  undervalued by that amount.
DISCONFIRMING_OBSERVATION: >
  A trip cost recorded after the goods are already received and valued produces no adjustment path
  back to that valuation, even where the business would expect one.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Receive and value goods before the trip's actual cost is known, then record that cost, and check
  whether it adjusts the goods' existing valuation.
```

## G05-STOCK_FLEET-Q034

```yaml
QID: G05-STOCK_FLEET-Q034
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A trip cost recorded for a purely internal, no-charge relocation is distinguishable from one
  intended to be attributed to goods valuation, rather than the two being conflated into the same
  figure.
WHY_IT_MATTERS: >
  Conflating internal, non-attributable costs with valuation-relevant ones either inflates goods
  cost with movements that should not count, or hides costs that should.
DISCONFIRMING_OBSERVATION: >
  There is no way to record or view a trip cost as internal or non-attributable, distinct from one
  intended to reach the goods' valuation.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record a trip cost for a purely internal relocation, and check whether it can be distinguished
  from a trip cost intended to affect goods valuation.
```

## G05-STOCK_FLEET-Q035

```yaml
QID: G05-STOCK_FLEET-Q035
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the movement a trip cost was attributed to is later cancelled or reversed, that cost reverses
  or is reattributed along with it, rather than standing against a movement that no longer exists
  in the same form.
WHY_IT_MATTERS: >
  A cost left standing against a movement that was undone overstates the true cost of whatever
  actually happened.
DISCONFIRMING_OBSERVATION: >
  Cancelling the movement leaves its attributed trip cost recorded with no adjustment or
  reattribution.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Attribute a trip cost to a movement, cancel that movement, and inspect whether the trip cost is
  adjusted or reattributed.
```

## G05-STOCK_FLEET-Q036

```yaml
QID: G05-STOCK_FLEET-Q036
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A movement type configured as requiring a vehicle cannot be marked complete with no vehicle ever
  recorded against it, without that gap being surfaced.
WHY_IT_MATTERS: >
  A completed movement with no vehicle, despite one being required, is a compliance gap that
  should be visible rather than silently accepted.
DISCONFIRMING_OBSERVATION: >
  A movement configured to require a vehicle reaches completion with no vehicle recorded and no
  flag distinguishing it from a properly staffed one.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a movement type as requiring a vehicle, complete a movement of that type with no
  vehicle recorded, and observe whether the gap is flagged.
```

## G05-STOCK_FLEET-Q037

```yaml
QID: G05-STOCK_FLEET-Q037
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A configured vehicle requirement is actually evaluated at some defined point in the movement's
  lifecycle, rather than existing only as a configured expectation with nothing that checks it.
WHY_IT_MATTERS: >
  A requirement that is declared but never checked provides no real assurance, only the appearance
  of one.
DISCONFIRMING_OBSERVATION: >
  The configured vehicle requirement has no point in the movement's lifecycle at which it is
  actually evaluated.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Configure a vehicle requirement for a movement type, then trace the movement's lifecycle to find
  the point, if any, at which the requirement is checked.
```

## G05-STOCK_FLEET-Q038

```yaml
QID: G05-STOCK_FLEET-Q038
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A vehicle attached retroactively to close a compliance gap on an already-completed movement is
  distinguishable in the record from a vehicle recorded at the proper time.
WHY_IT_MATTERS: >
  A retroactive fix that looks identical to a properly timed record hides the fact that the
  requirement was not actually met when the movement happened.
DISCONFIRMING_OBSERVATION: >
  A vehicle attached after the fact to close a compliance gap is indistinguishable from one
  recorded during the actual movement.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a movement with a missing required vehicle, later attach a vehicle retroactively, and
  compare the resulting record against one recorded at the proper time.
```

## G05-STOCK_FLEET-Q039

```yaml
QID: G05-STOCK_FLEET-Q039
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Completing a movement with no vehicle where one is required has a visible effect on downstream
  figures that assume a vehicle was involved, rather than those figures silently treating the gap
  as a zero-cost, zero-impact event.
WHY_IT_MATTERS: >
  Downstream cost and utilisation figures that quietly absorb a missing-vehicle gap as if nothing
  happened understate the real state of operations.
DISCONFIRMING_OBSERVATION: >
  Downstream cost or utilisation figures show no distinguishable effect, not even an absence
  marker, from a required vehicle never having been recorded.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete a movement with no vehicle recorded where one is required, and inspect downstream cost
  or utilisation figures for any resulting effect or absence marker.
```

## G05-STOCK_FLEET-Q040

```yaml
QID: G05-STOCK_FLEET-Q040
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Archiving a vehicle record does not remove or hide the historical movements that reference it, so
  past trips remain traceable to the vehicle that actually carried them.
WHY_IT_MATTERS: >
  Losing traceability to an archived vehicle breaks the historical record for every past movement
  it was ever involved in.
DISCONFIRMING_OBSERVATION: >
  Archiving a vehicle makes historical movements that reference it unreadable, blank, or unable to
  resolve which vehicle was involved.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Archive a vehicle with historical movements referencing it, and inspect those movements
  afterward.
```

## G05-STOCK_FLEET-Q041

```yaml
QID: G05-STOCK_FLEET-Q041
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An archived vehicle is actually blocked from being selected for a new assignment, rather than
  remaining selectable exactly as if it were still active.
WHY_IT_MATTERS: >
  An archived vehicle that can still be assigned defeats the purpose of archiving it and can put
  goods on a vehicle no longer meant to be in service.
DISCONFIRMING_OBSERVATION: >
  An archived vehicle can be assigned to a brand-new movement exactly as if it were still active.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Archive a vehicle, and attempt to assign it to a brand-new movement.
```

## G05-STOCK_FLEET-Q042

```yaml
QID: G05-STOCK_FLEET-Q042
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: R5-remediation
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Archiving a vehicle that was never used produces no reference to movements or trips that do not
  actually exist.
WHY_IT_MATTERS: >
  A phantom reference on an otherwise unused vehicle record would mislead anyone reviewing its
  history into thinking it was used when it never was.
DISCONFIRMING_OBSERVATION: >
  Inspecting the archived, never-used vehicle's history reveals a populated trip count, a
  last-movement date, or a listed movement or trip reference, and that entry cannot be traced to
  any actual movement record held anywhere else in the system.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Archive a vehicle record that has never been used on any movement, and inspect it for any
  reference to a movement or trip.
```

## G05-STOCK_FLEET-Q043

```yaml
QID: G05-STOCK_FLEET-Q043
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reinstating an archived vehicle leaves its historical movements and any cost attribution tied to
  it exactly as they were, rather than altering or duplicating the historical record.
WHY_IT_MATTERS: >
  A reinstatement that alters or duplicates history corrupts records of movements that already
  happened and were already correctly recorded.
DISCONFIRMING_OBSERVATION: >
  Reinstating an archived vehicle changes or duplicates the historical movement records that
  referenced it while archived.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Archive a vehicle with historical movements, reinstate it, and compare those historical movement
  records before archiving and after reinstatement.
```

## G05-STOCK_FLEET-Q044

```yaml
QID: G05-STOCK_FLEET-Q044
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When one company sharing a vehicle archives it, the other company sharing the same vehicle sees
  a consistent active or archived state, rather than the two companies' views disagreeing.
WHY_IT_MATTERS: >
  Disagreement between sharing companies about whether a vehicle is even still in service can lead
  one to assign a vehicle the other has already retired.
DISCONFIRMING_OBSERVATION: >
  One company sees the shared vehicle as archived while another company sharing it can still
  actively assign it, with no reconciliation between the two views.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Share a vehicle across two companies, archive it from one company's context, and check whether
  the other company's context reflects the same state.
```

## G05-STOCK_FLEET-Q045

```yaml
QID: G05-STOCK_FLEET-Q045
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  For a vehicle owned by one company but used to carry goods for another, the record can represent
  an owning company distinct from the company whose goods are being carried on a given trip.
WHY_IT_MATTERS: >
  A record that collapses ownership and use into a single company field cannot represent the very
  cross-company arrangement it is meant to support.
DISCONFIRMING_OBSERVATION: >
  The record has no way to represent an owning company different from the company whose goods are
  being carried on a given trip.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record a trip where the carrying vehicle's owning company differs from the company whose goods
  are carried, and check whether both facts can be represented.
```

## G05-STOCK_FLEET-Q046

```yaml
QID: G05-STOCK_FLEET-Q046
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A company using a vehicle it does not own needs a distinct, recognised permission to assign it,
  rather than any company with visibility of the vehicle record being able to assign it freely.
WHY_IT_MATTERS: >
  Free assignment of another company's vehicle with no permission check removes any real control
  the owner has over how its own asset is used.
DISCONFIRMING_OBSERVATION: >
  A company with no ownership stake in a vehicle can assign it to its own movements with no
  distinct permission check from assigning a vehicle it owns outright.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Attempt to assign a vehicle to a movement from a company that has no ownership stake in that
  vehicle, and observe whether a distinct permission check applies.
```

## G05-STOCK_FLEET-Q047

```yaml
QID: G05-STOCK_FLEET-Q047
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the owning company records a shared vehicle as unavailable or out of service, that state
  propagates to block assignment attempts by the using company, rather than the using company being
  able to continue assigning it.
WHY_IT_MATTERS: >
  A using company that can still book a vehicle the owner has already pulled from service can
  commit goods to a vehicle that will not actually be able to carry them.
DISCONFIRMING_OBSERVATION: >
  The using company can still assign a vehicle to a movement after the owning company has recorded
  it as unavailable or out of service.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Mark a shared vehicle unavailable from the owning company's context, and attempt to assign it to
  a movement from the using company's context.
```

## G05-STOCK_FLEET-Q048

```yaml
QID: G05-STOCK_FLEET-Q048
MODULE: stock_fleet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A vehicle used exclusively within its owning company, never shared, carries none of the
  cross-company reconciliation overhead that sharing introduces.
WHY_IT_MATTERS: >
  Forcing every vehicle through cross-company checks and fields, whether or not it is ever shared,
  adds friction to ordinary single-company use for no benefit.
DISCONFIRMING_OBSERVATION: >
  Assigning a vehicle that has never been shared and belongs to a single company requires resolving
  cross-company fields or checks that have no bearing on it.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Assign a vehicle that has never been shared and belongs to a single company to a movement, and
  observe whether any cross-company fields or checks are required.
```

