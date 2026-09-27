# GMVQ MODULE-SPECIFIC QUESTION BANK

Document ID: G06-MRP_SUBCONTRACTING_REPAIR-GMVQ-MVQ-V1.00-DRAFT
Group: G06 MANUFACTURING
Module Metadata: mrp_subcontracting_repair
Wave: W2
Author Cell: P13
Review Cell: PENDING
Status: DRAFT / AUTHORING COMPLETE / NOT FROZEN
actual_mvq_count: 48
Purpose: Module-specific research questions (MVQ) for the blind two-lane ROOM A study of
  mrp_subcontracting_repair. Answered independently by Lane A (source reading) and Lane B
  (runtime observation only) and compared cell-to-cell by the Reconciler under MODULE + QID.
Control: Authored under GMVQ_AUTHORING_STANDARD_V1.00.md and GMVQ_BRIDGE_MODULE_RULE_V1.00.md.
  Clean Room absolute - generic ERP business/behavioural concepts only, no vendor names and no
  technical identifiers. This bank governs seam behaviour only: an item's identity and history
  crossing an external repair loop and coming back. Subcontracting's own invariants belong to
  mrp_subcontracting (cell P11); the ledger seam and the commercial-document seam belong to
  mrp_subcontracting_account / mrp_subcontracting_purchase (cell P12) and are out of scope here.

Note on cross-check: at authoring time no sibling bank existed on disk under
01_QUESTION_BANKS/G06_MANUFACTURING/ for mrp_subcontracting, mrp_subcontracting_account, or
mrp_subcontracting_purchase. The mandatory grep required by GMVQ_BRIDGE_MODULE_RULE_V1.00.md
Section 5 was run and returned no results because no sibling file exists yet, not because the
check was skipped. Overlap against those three siblings could not be verified against actual
authored text and should be re-checked once they exist on disk.

This bank produces DRAFT question content only. Not approved, not frozen, not verified. No merge,
release, STATE closure or gate approval is authorized by this document.

---

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q001
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An item returning from external repair bearing a different identifier than it left with
  triggers a required reconciliation step rather than being silently accepted as the same
  item.
WHY_IT_MATTERS: >
  Silently accepting a changed identifier would break the item's traceable history without
  anyone noticing.
DISCONFIRMING_OBSERVATION: >
  An item returned with a different identifier than recorded at outbound is received into
  the system with no reconciliation step, warning, or record of the discrepancy.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A serialized item sent to an external party for repair, returned bearing a different
  identifier than it left with.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q002
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The warranty coverage clock's behavior while an item is at an external repairer
  (continuing, pausing, or resetting) is an explicit, consistent rule rather than an
  incidental side effect of how the repair record happens to be structured.
WHY_IT_MATTERS: >
  An unintended side effect here could silently extend or shorten a customer's actual
  warranty entitlement.
DISCONFIRMING_OBSERVATION: >
  The warranty coverage end date changes as a result of the repair loop with no rule or
  setting anywhere that explains why or by how much.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  An item under warranty sent for external repair, warranty coverage dates compared before
  and after.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q003
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An item that the external party scraps instead of repairing produces a record of that
  loss, distinct from and comparable to an in-house scrap record.
WHY_IT_MATTERS: >
  Without a record, an asset or customer item permanently disappears from the books with
  no trace of what happened to it.
DISCONFIRMING_OBSERVATION: >
  An item scrapped by the external party leaves no scrap or loss record at all, differing
  from how an in-house scrap event is normally recorded.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  An item sent for external repair that the external party reports as scrapped rather than
  returned.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q004
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An item's accumulated history (prior operations, prior components) remains one
  continuous, queryable record across the external repair loop rather than splitting into
  two disconnected records.
WHY_IT_MATTERS: >
  A broken history record would make it impossible to see an item's full lifecycle in one
  place, undermining later investigation.
DISCONFIRMING_OBSERVATION: >
  Querying the item's history after it returns from external repair shows only the
  post-return portion, with the pre-repair history unreachable from the same record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  An item with recorded history sent for external repair and returned, history queried
  afterward.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q005
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a customer-owned item is sent to a third party for repair, the system records who
  is accountable for it while it is away, distinct from ordinary operator-owned equipment.
WHY_IT_MATTERS: >
  Without a recorded liability holder, a lost or damaged customer item creates a dispute
  with no documented basis for resolving it.
DISCONFIRMING_OBSERVATION: >
  A customer-owned item sent for external repair is recorded identically to
  operator-owned equipment, with no distinguishing liability or ownership marker.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  A customer-owned item sent to an external party for repair.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q006
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An item that never returns from external repair and is never declared scrapped either
  moves into a distinguishable overdue or exception state rather than remaining
  indistinguishable from an item still legitimately in transit.
WHY_IT_MATTERS: >
  An indistinguishable state means a genuinely lost item can sit unnoticed indefinitely,
  mistaken for a normal delay.
DISCONFIRMING_OBSERVATION: >
  An item well past any expected repair turnaround shows the identical state and
  appearance as one sent out yesterday, with nothing to flag the overdue condition.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  An item sent for external repair with no return or scrap declaration recorded well
  beyond the expected turnaround.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q007
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The system can capture what was actually done by the external party as reported, and
  compare it against what was originally specified, even though it cannot independently
  verify the physical work.
WHY_IT_MATTERS: >
  Without a captured record of the discrepancy, the operator has no way to know or
  evidence that the external party deviated from instructions.
DISCONFIRMING_OBSERVATION: >
  There is no field, note, or record anywhere capable of showing that the work actually
  performed differed from what was originally specified.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  An item sent for external repair with a specific scope of work, and the actual work
  reported back differs from that scope.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q008
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The system provides a way to record whether the returned item is the same physical unit
  repaired or a different unit substituted as a replacement, even when only the external
  party actually knows which occurred.
WHY_IT_MATTERS: >
  Treating a replacement as a repair (or vice versa) misrepresents the item's true
  identity and accumulated history going forward.
DISCONFIRMING_OBSERVATION: >
  No field or record exists anywhere to distinguish a genuine repair-and-return from a
  replacement issued under the same identity.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  An item returned from external repair, reviewed for whether repaired-versus-replaced can
  be recorded at all.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q009
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Components consumed by the external party during the repair are recorded on the
  operator's own records at the level of detail available, not only inferred from the
  final invoice total.
WHY_IT_MATTERS: >
  Relying only on an invoice total gives no visibility into what was actually replaced or
  used on the item.
DISCONFIRMING_OBSERVATION: >
  The only information available about components used in the repair is a single lump
  total on the external invoice, with no itemized record captured anywhere.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An external repair invoice itemizing components used, reviewed against what the system
  records for that repair.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q010
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The accounting treatment of a repair's cost differs, in a defined way, depending on
  whether the repaired item is customer-owned or the operator's own asset.
WHY_IT_MATTERS: >
  Applying operator-asset cost treatment to a customer-owned item's repair would misstate
  the operator's own asset costs with an amount that isn't really theirs to capitalize or
  expense.
DISCONFIRMING_OBSERVATION: >
  A customer-owned item's repair cost is recorded through the identical accounting
  treatment as a repair on the operator's own asset, with no distinguishing rule.
EXPECTED_SURFACE: S2
PRECONDITIONS: >
  One repair on a customer-owned item and one on an operator-owned item, cost treatment
  compared.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q011
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the customer recalls their item while it is still at the external party mid-repair,
  the system supports recording that recall as a distinct state rather than forcing the
  record through a normal repair-complete path.
WHY_IT_MATTERS: >
  Forcing an interrupted repair through a completion path would misrepresent an unfinished
  job as a finished one.
DISCONFIRMING_OBSERVATION: >
  Recording a customer recall mid-repair is only possible by marking the repair falsely
  complete, with no distinct interrupted or recalled state available.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An item at an external party mid-repair, the customer requests its return before work is
  finished.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q012
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An item returned from an external party whose identity cannot be matched to any outbound
  repair record is held in a distinct exception state on receipt rather than accepted into
  normal stock.
WHY_IT_MATTERS: >
  Accepting an unmatched item into normal stock could introduce an item of unknown origin,
  history, or ownership into circulation.
DISCONFIRMING_OBSERVATION: >
  An item with no matching outbound repair record is received into ordinary stock with no
  exception, hold, or flag raised.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An item returned from an external party with no identifiable matching outbound repair
  record.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q013
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The item's serial or lot history shows the external repair window as an explicit gap in
  direct observation, rather than fabricating a continuous, fully-observed narrative where
  none was verified.
WHY_IT_MATTERS: >
  A fabricated continuous history overstates the operator's actual knowledge of what
  happened to the item while it was away.
DISCONFIRMING_OBSERVATION: >
  The item's history presents the external repair period as fully observed and verified,
  identical in presentation to periods genuinely under the operator's own observation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  An item returned from external repair, its history record reviewed for how the external
  period is presented.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q014
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Authorizing a customer-owned item to be sent to a third party requires a role distinct
  from, or at least equally controlled as, the role needed to send the operator's own item
  externally.
WHY_IT_MATTERS: >
  Weaker control over sending customer property to a third party creates disproportionate
  risk relative to sending the operator's own equipment.
DISCONFIRMING_OBSERVATION: >
  Any user able to send the operator's own item externally can send a customer-owned item
  externally with no additional check or distinction.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Attempts to send both a customer-owned item and an operator-owned item to an external
  party, by users with different role assignments.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q015
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Any service or warranty commitment already promised to the end customer remains visible
  and trackable while their item is held by an external repairer the customer cannot see
  into directly.
WHY_IT_MATTERS: >
  A commitment that becomes invisible during the external hold could be missed or breached
  with no one aware it is at risk.
DISCONFIRMING_OBSERVATION: >
  The commitment's due date or status becomes unavailable or unclear to the operator for
  the duration the item sits with the external repairer.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  A customer item under an active service commitment, sent to an external repairer.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q016
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An item's recorded ownership and company scope remain unchanged throughout the external
  repair loop unless an explicit transaction changes them.
WHY_IT_MATTERS: >
  An unexplained scope change during a repair loop could misattribute the item to the
  wrong entity's books or responsibility.
DISCONFIRMING_OBSERVATION: >
  The item's recorded ownership or company scope differs after the external loop with no
  explicit transaction accounting for the change.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  An item's ownership and company scope recorded before being sent for external repair,
  compared after its return.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q017
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling a repair engagement after the item has already been shipped to the external
  party produces a defined recall or return request path rather than leaving the item's
  status unresolved.
WHY_IT_MATTERS: >
  An unresolved status after cancellation leaves an item physically at a third party with
  no active instruction guiding its return.
DISCONFIRMING_OBSERVATION: >
  Cancelling the repair after shipment leaves the item's record showing no recall action,
  reminder, or instruction of any kind.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A repair engagement cancelled after the item has already been shipped to the external
  party.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q018
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The system's basis for treating a returned item as the same physical item is more than a
  label or identifier claim asserted at receipt with nothing to independently support it.
WHY_IT_MATTERS: >
  Relying purely on an asserted claim means a mismatched or substituted item could pass
  through completely unnoticed.
DISCONFIRMING_OBSERVATION: >
  The only basis available anywhere for confirming the returned item's identity is the
  identifier claimed at the point of receipt itself, with no independent supporting
  evidence ever required or recorded.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  An item received back from external repair, reviewed for what evidence supports its
  claimed identity.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q019
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A repair outcome where some reported defects were fixed and others were not can be
  recorded as such, rather than the system only supporting a binary repaired-or-not
  outcome.
WHY_IT_MATTERS: >
  A forced binary outcome would misrepresent a partially successful repair as either a
  full success or a full failure.
DISCONFIRMING_OBSERVATION: >
  Attempting to record a partial repair outcome forces a choice between only fully
  repaired or fully unrepaired, with no way to capture the partial result.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An external repair where some but not all reported defects were resolved.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q020
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An item genuinely away at an external repairer with unknown real-time location is
  prevented, or at least flagged, from being used in another transaction that assumes it
  is available.
WHY_IT_MATTERS: >
  Allowing a transaction against an item that is physically elsewhere could commit
  something to a customer or process that cannot actually be fulfilled.
DISCONFIRMING_OBSERVATION: >
  A transaction proceeds against the item as if it were available and on hand while it
  remains recorded as away at an external repairer.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An item recorded as sent for external repair, an unrelated transaction attempted against
  the same item.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q021
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the external party reports the repair complete, the system's state reflects that
  this is a reported claim, not a verified fact of physical receipt.
WHY_IT_MATTERS: >
  Treating a reported claim as verified fact could lead the operator to promise the item to
  the customer before it has actually arrived.
DISCONFIRMING_OBSERVATION: >
  The system's state after a reported completion is presented identically to the state
  after the item is actually physically received back.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An external party reports a repair complete, the item's system state reviewed before
  physical return is confirmed.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q022
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The full chain of custody for an item across the external repair loop can be
  reconstructed from the operator's own system records alone, without needing to rely on
  the external party's own paperwork.
WHY_IT_MATTERS: >
  A chain of custody that depends on the external party's own paperwork is not something
  the operator actually controls or can independently produce for audit.
DISCONFIRMING_OBSERVATION: >
  Reconstructing the full chain of custody requires referring to the external party's own
  documents because the operator's own records leave gaps.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A completed external repair loop, chain of custody reconstructed using only the
  operator's own system records.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q023
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the external repair introduces components whose origin cannot be established, the
  item's accumulated history reflects that uncertainty rather than presenting the new
  components as having a known, verified origin.
WHY_IT_MATTERS: >
  Presenting unknown-origin parts as verified would give a false sense of assurance about
  what the item is actually made of now.
DISCONFIRMING_OBSERVATION: >
  Components of unknown origin introduced during the external repair appear in the item's
  record identically to components with a fully known and verified origin.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  An external repair that introduces components whose origin the operator cannot
  establish.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q024
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A control exists, or the absence of one is explicit, to catch an item being returned to
  a party other than its original owner or customer.
WHY_IT_MATTERS: >
  An item misdirected to the wrong party with no catching control is a real loss and
  liability exposure the operator should at least know it does not guard against.
DISCONFIRMING_OBSERVATION: >
  An item returned to a party other than its original owner passes through the process
  with no available control point that could have caught it, and this is not documented as
  a known limitation.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An item's return process reviewed for whether any check ties the returning destination
  back to the original owner or customer.
```
```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q025
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The system has a defined way to represent an item being forwarded from one external
  repairer to a second one while still out, or an explicit statement that this scenario is
  out of scope.
WHY_IT_MATTERS: >
  A silently unsupported nested loop means the operator's records would show the item at
  the first party while it is really somewhere else entirely.
DISCONFIRMING_OBSERVATION: >
  There is no way to represent a nested forwarding to a second external party, and nothing
  indicates this is a known, accepted limitation.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An item at an external repairer that is, in the real scenario being modeled, forwarded
  onward to a second external party.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q026
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the customer who owns an item transfers ownership of it while it is away being
  externally repaired, the repair record reflects the new owner rather than continuing to
  reference the original one silently.
WHY_IT_MATTERS: >
  Continuing to reference the original owner after a transfer could return the item, or
  its liability, to the wrong party.
DISCONFIRMING_OBSERVATION: >
  The repair record continues to show the original owner as the responsible party after an
  ownership transfer has been recorded elsewhere in the system.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A customer-owned item away at external repair, ownership of the item transferred to
  another customer during that time.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q027
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An item is considered out of service for scheduling or availability purposes for the
  entire actual duration of the external loop, not only for a system-estimated portion of
  it.
WHY_IT_MATTERS: >
  Treating the item as available again before it actually returns could lead to committing
  it to another use it cannot fulfill.
DISCONFIRMING_OBSERVATION: >
  The item is shown as available again based on an estimated return date that has passed,
  even though it has not actually been received back.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  An item away at external repair past its estimated return date but not yet physically
  received.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q028
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The cost of a failed repair attempt (returned unrepaired) is captured and
  distinguishable from the cost of a successful repair.
WHY_IT_MATTERS: >
  Blending failed and successful repair costs together hides how much is being spent on
  repairs that don't actually work.
DISCONFIRMING_OBSERVATION: >
  A failed repair attempt's cost is recorded identically to a successful repair's cost,
  with no way to distinguish the two afterward.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  An external repair attempt that the external party reports as unsuccessful, cost record
  reviewed.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q029
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The defined states between sent-for-external-repair and returned are each recorded in
  order, without the record skipping a state or moving backward without an explicit
  reason.
WHY_IT_MATTERS: >
  A skipped or reversed state without explanation hides whether an expected checkpoint in
  the repair process actually happened.
DISCONFIRMING_OBSERVATION: >
  The item's repair record moves from an early state directly to fully returned, with an
  intermediate state never recorded, or moves backward with no explanation logged.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An item's repair record tracked through each state change from being sent to being
  returned.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q030
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The system relies on a unique identifier, not merely a description or item type, to
  confirm which specific item has returned from external repair.
WHY_IT_MATTERS: >
  Relying on description alone risks two visually or functionally similar items being
  swapped without detection.
DISCONFIRMING_OBSERVATION: >
  An item can be received back and closed out against a repair record using only a
  matching description or type, with no unique identifier check performed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Two items of the same description and type, one sent for external repair, receipt
  process reviewed for identity verification.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q031
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An external repair invoice referencing an item the operator has no record of sending is
  surfaced as a discrepancy rather than paid or filed without question.
WHY_IT_MATTERS: >
  Paying an invoice with no matching record risks paying for a repair that never should
  have occurred on the operator's account.
DISCONFIRMING_OBSERVATION: >
  An invoice referencing an unrecorded outbound item proceeds through processing with no
  discrepancy flag raised anywhere.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  An external repair invoice received referencing an item with no matching outbound repair
  record.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q032
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Terminating the repair engagement with an external party while items are still recorded
  as out with them produces a visible list or flag of those outstanding items rather than
  silently closing the relationship.
WHY_IT_MATTERS: >
  A silent closure could leave items stranded at a party the operator has just ended its
  relationship with, unnoticed.
DISCONFIRMING_OBSERVATION: >
  Terminating the engagement with the external party produces no list, flag, or reminder of
  items still recorded as out with them.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An external party relationship with items currently recorded as out for repair, the
  relationship then terminated.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q033
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The system distinguishes a repair-and-return of the operator's own equipment from a
  repair-and-return of a customer's item at the point of creating the repair record, not
  only inferred later from context.
WHY_IT_MATTERS: >
  Without an explicit distinction at creation, the different ownership and liability
  implications could be handled inconsistently or missed.
DISCONFIRMING_OBSERVATION: >
  Creating a repair record provides no explicit way to indicate whether the item is the
  operator's own or a customer's, leaving it to be inferred later if at all.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A repair record created for an item, reviewed for whether ownership type is captured at
  creation.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q034
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A prior open work order or maintenance schedule tied to an item is placed into a defined
  hold or exception state while that item is externally out of reach for repair.
WHY_IT_MATTERS: >
  An open schedule item that assumes the equipment is available would generate false
  expectations or missed maintenance windows.
DISCONFIRMING_OBSERVATION: >
  A prior open work order or maintenance schedule for the item remains active and due as
  normal while the item is externally out of reach.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  An item with an open work order or maintenance schedule, then sent for external repair.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q035
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Closing the repair record requires an operator-side inspection step, not only the
  external party's own confirmation that the work is done.
WHY_IT_MATTERS: >
  Relying solely on the external party's own say-so to close the record removes any
  independent check on the quality of what was returned.
DISCONFIRMING_OBSERVATION: >
  The repair record can be closed based solely on the external party's confirmation, with
  no operator-side inspection step available or required.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  A repair record ready for closure, reviewed for what is required to close it.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q036
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If the item's serial changed during the external loop, the system's history links the
  pre-loop and post-loop identifiers as one continuous identity rather than treating the
  pre-loop history as orphaned.
WHY_IT_MATTERS: >
  An orphaned pre-loop history would make the item appear to have no history at all from
  the moment it returns, losing everything before the change.
DISCONFIRMING_OBSERVATION: >
  After a serial change during the loop, the pre-loop history becomes unreachable from the
  item's current identifier, with no link connecting the two.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  An item whose identifier changed during external repair, history reviewed for
  continuity across the change.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q037
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Additional parts or accessories returned along with the repaired item, but not
  originally sent, are captured in the receiving record rather than passing through
  unrecorded.
WHY_IT_MATTERS: >
  Unrecorded additional items could be lost track of, or their unexplained origin could
  raise questions no one can answer later.
DISCONFIRMING_OBSERVATION: >
  Additional parts included with the returned item beyond what was originally sent are
  received with no record capturing their addition.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An item returned from external repair along with additional parts not part of the
  original outbound shipment.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q038
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The external repairer is not given visibility into which end customer a repaired item
  belongs to beyond what is operationally necessary for the repair itself.
WHY_IT_MATTERS: >
  Unnecessary exposure of the end-customer association to a third party is a disclosure
  the operator did not need to make.
DISCONFIRMING_OBSERVATION: >
  Documentation or interfaces given to the external party include the end customer's
  identity or details with no operational need for the repair itself.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  A customer-owned item sent for external repair, documents and interfaces exposed to the
  external party reviewed.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q039
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A repair record marked complete and closed, later found to have never actually occurred
  (the item was never sent), can still be corrected rather than the closure blocking any
  further change.
WHY_IT_MATTERS: >
  A closure that blocks correction would leave a known-false record standing permanently
  in the system.
DISCONFIRMING_OBSERVATION: >
  The closed repair record cannot be corrected or reopened even after it is established
  that the underlying event never occurred.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  A repair record marked complete and closed, later discovered to be based on an event
  that never actually happened.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q040
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A warranty claim raised by the end customer for the same defect the external repair
  addressed maintains a visible link back to that original repair record.
WHY_IT_MATTERS: >
  Without the link, no one can tell whether a new claim is a genuine repeat failure of the
  same repair or an unrelated issue.
DISCONFIRMING_OBSERVATION: >
  A warranty claim for the same defect shows no link back to the original external repair
  record addressing it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  An item externally repaired for a specific defect, later the subject of a new warranty
  claim for the same defect.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q041
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The full external repair loop, from sending the item out to receiving it back and
  closing the record, is reachable end-to-end through the standard documented transactions
  without a manual workaround.
WHY_IT_MATTERS: >
  A manual-only path for part of the loop means its actual behavior in practice may not
  match what any specification describes.
DISCONFIRMING_OBSERVATION: >
  Completing part of the external repair loop requires a manual step or workaround outside
  the standard documented flow.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  An item processed through the full external repair loop using only the standard
  documented flow.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q042
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The system requires or at least strongly supports capturing an originating fault or
  reason when an item is sent for external repair, rather than allowing the record to
  exist with no reason at all.
WHY_IT_MATTERS: >
  Missing fault reasons across repair records would prevent any later root-cause or
  failure-pattern analysis.
DISCONFIRMING_OBSERVATION: >
  A repair record can be created and carried through to completion with no fault or reason
  ever captured at any point.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  A new external repair record created without entering any fault or reason.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q043
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the same item goes through the external repair loop more than once over its
  lifetime, each loop is captured as a distinct, separately traceable event rather than
  merging into one combined record.
WHY_IT_MATTERS: >
  Merged records would make it impossible to tell how many times an item has actually
  failed and been repaired.
DISCONFIRMING_OBSERVATION: >
  A second external repair loop for the same item overwrites or merges with the first,
  leaving no way to see them as two separate events.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  An item that has gone through the external repair loop more than once over its recorded
  lifetime.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q044
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether an operator-side inspection is required on return from external repair can be
  configured per item type or per external party, rather than being a single fixed rule
  for every case.
WHY_IT_MATTERS: >
  A single fixed rule that cannot flex by risk level either over-inspects low-risk items or
  under-inspects high-risk ones.
DISCONFIRMING_OBSERVATION: >
  No configuration exists to vary the inspection requirement by item type or external
  party; it is fixed identically for every case.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  The inspection-on-return requirement reviewed for configurability across different item
  types and external parties.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q045
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An item recorded as out for external repair is excluded from an expected-on-hand
  physical inventory count, or clearly explained as a known variance, rather than
  appearing as an unexplained discrepancy.
WHY_IT_MATTERS: >
  An unexplained discrepancy during a physical count wastes investigation effort chasing
  something the system already knows about.
DISCONFIRMING_OBSERVATION: >
  A physical inventory count flags the item as an unexplained discrepancy with no
  indication anywhere that it is currently out for external repair.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An item recorded as out for external repair at the time a physical inventory count is
  performed on its expected location.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q046
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the external repair's cost is given only as a lump sum with no component breakdown,
  that limitation is visible on the item's accumulated cost history rather than being
  presented as if it were itemized detail.
WHY_IT_MATTERS: >
  Presenting a lump sum as if it were itemized detail overstates the granularity of
  information actually available.
DISCONFIRMING_OBSERVATION: >
  A lump-sum external repair cost appears in the item's cost history displayed in the same
  itemized format used for genuinely itemized costs.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  An external repair invoiced as a single lump sum, cost history reviewed for how it is
  presented.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q047
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The operator can require photographic or documentary evidence of the item's condition
  before and after external repair as a system-enforced gate, even as an optional
  configuration.
WHY_IT_MATTERS: >
  Without this option, there is no system-level way to reduce disputes about the item's
  condition change during the external loop.
DISCONFIRMING_OBSERVATION: >
  No configuration anywhere can require documentary evidence of condition before or after
  the repair, even as an optional setting.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  An external repair record type reviewed for available configuration options around
  condition evidence.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_REPAIR-Q048
MODULE: mrp_subcontracting_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An item destroyed or lost in transit to or from the external party is recorded distinctly
  from an item scrapped at the external party's own site, given the different liability
  implications.
WHY_IT_MATTERS: >
  Transit loss and on-site scrap can carry different liability and insurance consequences,
  and blending them together would obscure which applies.
DISCONFIRMING_OBSERVATION: >
  An item lost in transit and an item scrapped at the external party's site are recorded
  through the identical event type, with nothing distinguishing the two situations.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  One case of an item lost in transit to or from the external party, and one case of an
  item scrapped at the party's own site, records compared.
```
