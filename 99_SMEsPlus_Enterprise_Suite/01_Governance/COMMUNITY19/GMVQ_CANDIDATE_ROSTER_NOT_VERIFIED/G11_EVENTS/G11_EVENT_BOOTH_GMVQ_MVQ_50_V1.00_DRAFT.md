# SMEsPlus ENTERPRISE SUITE
## GMVQ — G11 EVENTS / event_booth Module Adversarial MVQ Bank

**Document ID:** GMVQ-G11-EVENT_BOOTH-MVQ50-V1.00
**Group:** G11 EVENTS
**Module Metadata:** `event_booth`
**Wave:** W2
**Author Cell:** P-E3 (GMVQ Question Factory — Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 50 = 105
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded
**Date authored:** 2026-09-27

## Purpose

This bank authors the module-specific MVQ set for `event_booth` — exhibition space as a
separately allocated, finite, individually identified resource at an event, distinct from the
base `event` module's general attendee capacity (a booth is a specific thing, not an
interchangeable slot). Per the G11 group brief, this module's questions fail only at the seam
between the base event's own lifecycle (its date, its venue, its cancellation, its per-company
scope) and the booth-allocation domain layered on top of it: a booth withdrawn because the venue
changed, an allocation surviving or not surviving an event date move, booths cascading or failing
to cascade when the parent event is cancelled, and per-company visibility extended down to
individual booths. It also covers the booth-allocation domain's own structural and lifecycle
invariants that do not depend on any commercial transaction: named-booth identity versus category
counts, the allocation/release/withdrawal/transfer lifecycle, concurrency on the last available
booth, exhibitor staff distinct from attendee registration, and the no-exhibitor-identified
placeholder state. Nothing here concerns price, order, invoice, payment, or revenue timing — that
seam belongs entirely to the sibling bank `event_booth_sale`, deliberately not duplicated here.

The question text is source-neutral and does not expose vendor names, model names, field names,
methods, schema, XML IDs, API shapes, or implementation algorithms. `MODULE: event_booth` appears
only in the structured metadata field, never inside question text.

`LAYER: BASE` marks a structural/identity-model question (what a booth is, how it is categorized,
configured and scoped). `LAYER: PROCESS` marks a lifecycle/transition question (allocate, release,
withdraw, transfer, and the booth's interaction with the base event's own lifecycle events).

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that states a concrete failure state.
- No padding: 50 questions exist because they test 50 distinct material hypotheses; none restates
  another question's disconfirming event with a noun swapped.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `module + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
- CLEAN ROOM: authored from generic business/behavioural knowledge of exhibition-space allocation.
  No vendor or reference source tree was opened to produce this bank.
- Mandatory pre-authoring sibling check performed per GMVQ_BRIDGE_MODULE_RULE_V1.00 §5:
  `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G11_EVENTS/*.md | sort` was run before authoring.
  DISCLOSURE: at authoring time, `01_QUESTION_BANKS/G11_EVENTS/` did not yet exist on disk — this
  cell's two banks (`event_booth`, `event_booth_sale`) are the first committed to that path. No
  sibling bank content (including any `event_sale` bank) was available to check against. The
  differentiation from `event_sale` (fungible, interchangeable seats versus this module's
  individually identified, non-fungible booths) was therefore ensured by construction against the
  routing brief's stated distinction, not by a completed sibling-overlap check, and should be
  re-verified against `event_sale` once that bank is committed to this path. Recorded as a
  DEVIATION for RED TEAM / Reconciler attention, per §7 of the deviation register discipline.
- POST-AUTHORING SUPPLEMENTARY CHECK: other cells committed the remaining G11_EVENTS banks (including `event_sale` and the base `event` bank) to disk during this same session. `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G11_EVENTS/*.md` and a targeted scan for `booth`/`exhibitor`/`exhibition` leakage into sibling banks were re-run after they landed: no sibling bank uses booth/exhibitor language, and `event_sale`'s ground (seat/registration quantity, attendee naming, capacity consumption timing) does not overlap this bank's specific-named-booth ground. The DEVIATION above is superseded by this supplementary check for the siblings that exist as of this authoring session; it still applies to any G11_EVENTS bank committed after this one.

## G11-EVENT_BOOTH-Q001

```yaml
QID: G11-EVENT_BOOTH-Q001
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A booth is modeled as a specific, individually identified physical space, and its
  allocation is never satisfied by treating it as one interchangeable unit out of an
  undifferentiated pool the way general attendee capacity is.
WHY_IT_MATTERS: >
  Collapsing an identified space into a fungible count would make it impossible to say
  which physical location an exhibitor actually holds, defeating the purpose of allocating
  space rather than a headcount.
DISCONFIRMING_OBSERVATION: >
  An exhibitor's confirmed allocation record shows only a category and a quantity, with no
  way to determine which specific named booth they occupy.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Allocate a booth to an exhibitor and inspect the resulting allocation record for a
  reference to a specific, individually identified booth rather than a category tally.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q002

```yaml
QID: G11-EVENT_BOOTH-Q002
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A booth category's declared count and the number of individually named booth records
  that actually exist under that category are kept in agreement, not tracked as two
  independent numbers that can silently diverge.
WHY_IT_MATTERS: >
  A category count that disagrees with the real named booths under it misleads anyone
  planning the floor or selling space against it.
DISCONFIRMING_OBSERVATION: >
  A category reports a count of available spaces that does not match the number of named
  booth records that exist under it, with nothing in the system flagging the mismatch.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a booth category with a declared count, then add or remove named booth records
  under it and compare the category's reported count to the actual records.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q003

```yaml
QID: G11-EVENT_BOOTH-Q003
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Reducing a category's declared count below the number of named booths already allocated
  under it is either rejected or produces an explicit, visible conflict, not a silently
  accepted contradiction.
WHY_IT_MATTERS: >
  An unresolved contradiction between a configured limit and already-committed allocations
  leaves nobody accountable for which allocations are actually valid.
DISCONFIRMING_OBSERVATION: >
  A category's declared count is lowered below its number of currently allocated booths
  and the configuration change is accepted with no warning, flag, or blocked allocations
  identified.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Allocate several booths under a category, then reduce that category's declared count
  below the number already allocated.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q004

```yaml
QID: G11-EVENT_BOOTH-Q004
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A named booth may override attributes it inherits from its category (size, position,
  attachable services), and that override is a deliberate per-booth setting rather than an
  accidental side effect of editing the category.
WHY_IT_MATTERS: >
  If a category edit can silently overwrite a booth-specific override, floor-plan and
  service data that took real effort to set up disappears without warning.
DISCONFIRMING_OBSERVATION: >
  Changing a category-level attribute after a booth has its own override for that
  attribute causes the booth's override to be silently replaced by the category's new
  value.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set a booth-level override that differs from its category's value, then change the
  category's value and inspect the booth's own attribute.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q005

```yaml
QID: G11-EVENT_BOOTH-Q005
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a booth's attributes are changed after it has already been allocated to an
  exhibitor, the exhibitor's existing allocation record reflects what was true at
  allocation time on any commercially or logistically material point, rather than silently
  tracking the live, possibly different, current attribute.
WHY_IT_MATTERS: >
  An exhibitor who agreed to a certain size, position or service set should not discover a
  materially different booth at the event because a later configuration edit was applied
  retroactively.
DISCONFIRMING_OBSERVATION: >
  A booth's size, position, or included services are changed after allocation and the
  exhibitor's own allocation record or confirmation shows the new values with no record of
  what was originally agreed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Allocate a booth to an exhibitor, then change one of the booth's attributes, and compare
  the exhibitor's allocation record to the booth's current live attributes.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q006

```yaml
QID: G11-EVENT_BOOTH-Q006
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Two named booths under the same event cannot be assigned the same physical position or
  location identifier at the same time.
WHY_IT_MATTERS: >
  Two booths claiming the same physical spot makes the floor plan unusable and guarantees
  an on-site conflict between exhibitors.
DISCONFIRMING_OBSERVATION: >
  Two distinct named booth records under the same event are saved carrying the identical
  position or location identifier with no rejection or warning.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create two named booths under the same event and attempt to assign both the same
  position or location value.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q007

```yaml
QID: G11-EVENT_BOOTH-Q007
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A named booth's status (available, allocated, withdrawn, and any other state the design
  defines) is an explicit, finite value that can be read directly, not a condition that
  has to be inferred by checking whether other records happen to reference it.
WHY_IT_MATTERS: >
  A status that only exists as an inference is fragile, since anything that changes the
  referencing data can silently change the booth's apparent status without an explicit
  transition ever happening.
DISCONFIRMING_OBSERVATION: >
  A booth's current status cannot be determined except by separately checking for the
  presence or absence of related records, with no single explicit status value to read.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Inspect a booth record across its available, allocated and withdrawn states and
  determine whether an explicit status field or only inferred state is present.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q008

```yaml
QID: G11-EVENT_BOOTH-Q008
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A booth allocated on behalf of an event with no exhibitor yet identified, a placeholder
  or provisional hold, is represented as its own distinct, recognizable state, not folded
  into either the plain available state or a normal completed allocation.
WHY_IT_MATTERS: >
  If a placeholder hold looks identical to either a free booth or a fully allocated one,
  staff cannot tell a genuinely open space from one already spoken for informally.
DISCONFIRMING_OBSERVATION: >
  A booth held with no exhibitor identified appears indistinguishable from either a fully
  available booth or a booth allocated to a named exhibitor when viewed through the normal
  record.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a booth allocation with no exhibitor identified and compare its recorded state to
  an ordinary available booth and to a normally allocated one.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q009

```yaml
QID: G11-EVENT_BOOTH-Q009
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The services a booth can carry, such as power, furniture, or signage, exist as
  configuration attached to the booth or its category independently of whether that booth
  is currently allocated to anyone.
WHY_IT_MATTERS: >
  Service configuration tied to occupancy rather than to the space itself would force
  every service definition to be redone each time a booth changes hands.
DISCONFIRMING_OBSERVATION: >
  A booth's configured services disappear or become unavailable to configure while the
  booth is in the available, unallocated, state.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure services on a booth or its category while unallocated, then allocate and
  release it, checking whether the service configuration persisted throughout.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q010

```yaml
QID: G11-EVENT_BOOTH-Q010
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A booth that is already allocated to one exhibitor cannot be allocated to a second
  exhibitor for the same event without first releasing or withdrawing the first
  allocation.
WHY_IT_MATTERS: >
  Two exhibitors holding the same physical space produces an unresolvable on-site conflict
  that cannot be fixed once the event has started.
DISCONFIRMING_OBSERVATION: >
  A second allocation of an already-allocated booth to a different exhibitor is accepted
  while the first exhibitor's allocation remains active and unreleased.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Allocate a booth to one exhibitor, then attempt to allocate the same booth to a second
  exhibitor without releasing the first.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q011

```yaml
QID: G11-EVENT_BOOTH-Q011
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the last remaining available named booth in a category is requested by two
  concurrent allocation attempts, exactly one succeeds and the other receives a definite
  rejection, rather than both appearing to succeed or the outcome depending on unrelated
  timing elsewhere in the system.
WHY_IT_MATTERS: >
  An indeterminate or double-successful outcome under concurrency produces exactly the
  double-booked booth this whole capability exists to prevent.
DISCONFIRMING_OBSERVATION: >
  Two concurrent allocation attempts against the same last-available named booth both
  report success, or the booth ends up referenced by two active allocations.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Reduce a category to a single remaining available named booth and submit two allocation
  attempts against it at effectively the same time.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q012

```yaml
QID: G11-EVENT_BOOTH-Q012
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Releasing an allocated booth returns it to the available pool through a deterministic,
  immediate effect of the release action itself, not through a separate manual
  republishing or recount step that could be skipped.
WHY_IT_MATTERS: >
  A release that does not deterministically restore availability creates phantom scarcity:
  a booth nobody holds but that nobody can book either.
DISCONFIRMING_OBSERVATION: >
  A booth is released from its allocation but does not appear as available for a new
  allocation without some additional, separate action being taken first.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Allocate then release a booth, and immediately attempt to allocate it again with no
  intervening administrative step.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q013

```yaml
QID: G11-EVENT_BOOTH-Q013
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Releasing a booth that already has services attached and marked as delivered or consumed
  produces a defined outcome for those service records, rather than leaving them attached
  to a now-unallocated booth with no owner.
WHY_IT_MATTERS: >
  An orphaned, already-delivered service with no attributable owner is a cost with no one
  left to bill or account for.
DISCONFIRMING_OBSERVATION: >
  A booth with services already marked delivered is released and those service records
  remain attached to the booth with no exhibitor reference and no defined handling.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attach and mark a service as delivered on an allocated booth, then release that booth's
  allocation and inspect the service record.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q014

```yaml
QID: G11-EVENT_BOOTH-Q014
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Moving an allocation directly from one exhibitor to another is either explicitly
  supported as a single transfer action, or is explicitly disallowed and requires release
  followed by a new allocation, but the platform does not leave it ambiguous which of the
  two applies.
WHY_IT_MATTERS: >
  An ambiguous in-between, where a transfer sometimes behaves like one step and sometimes
  silently requires two, is exactly the kind of inconsistent behaviour a floor manager
  cannot rely on.
DISCONFIRMING_OBSERVATION: >
  Attempting to change the exhibitor on an existing allocation produces different
  outcomes, direct change versus rejection requiring release, depending on unrelated
  circumstances, with no documented rule governing which occurs.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to change the exhibitor referenced by an existing active allocation directly,
  without an explicit release step.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q015

```yaml
QID: G11-EVENT_BOOTH-Q015
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an already-allocated booth is withdrawn because the venue changed, the exhibitor's
  allocation is put into an explicit, visible state that reflects the loss of their space,
  rather than being left to point at a booth record that has simply vanished from the
  available floor plan.
WHY_IT_MATTERS: >
  An exhibitor whose space disappears without an explicit signal has no way to know they
  need to be reaccommodated until they discover it on-site.
DISCONFIRMING_OBSERVATION: >
  A booth withdrawn while allocated leaves the exhibitor's allocation record showing no
  change, with nothing distinguishing it from a normal active allocation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Allocate a booth to an exhibitor, then withdraw that same booth, and inspect the
  exhibitor's allocation record afterward.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q016

```yaml
QID: G11-EVENT_BOOTH-Q016
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A withdrawn booth's prior allocation history remains available afterward for review,
  rather than being cleared or made unreachable at the same time the booth is withdrawn.
WHY_IT_MATTERS: >
  Losing the record of who held a space right before it was withdrawn removes the one
  piece of evidence needed to reaccommodate that exhibitor or explain the withdrawal.
DISCONFIRMING_OBSERVATION: >
  After a booth is withdrawn, no record of its most recent allocation, who held it and
  since when, can be retrieved through any normal means.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Allocate then withdraw a booth, and attempt to retrieve the record of who held it
  immediately before withdrawal.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q017

```yaml
QID: G11-EVENT_BOOTH-Q017
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the event's date is moved after a booth was already allocated to an exhibitor, that
  allocation's continuation, required reconfirmation, or invalidation is a defined,
  consistent outcome, not something left to whichever record happens to update first.
WHY_IT_MATTERS: >
  An exhibitor could show up prepared for the original date, or be silently dropped from a
  rescheduled one, if the effect of a date change on existing allocations is undefined.
DISCONFIRMING_OBSERVATION: >
  The event's date is changed and existing booth allocations show no defined response:
  some appear untouched, others disappear, with no documented rule explaining the
  difference.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Allocate a booth to an exhibitor, then change the parent event's date, and inspect the
  state of that allocation afterward.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q018

```yaml
QID: G11-EVENT_BOOTH-Q018
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the event's venue or location changes after booths have position or floor-plan
  attributes tied to the previous venue, those position attributes are flagged for review
  rather than silently carried forward as if still accurate.
WHY_IT_MATTERS: >
  A floor position that made sense at the old venue can be meaningless or physically
  impossible at the new one, and nobody notices the invalid reference until they arrive.
DISCONFIRMING_OBSERVATION: >
  The event's venue is changed and existing booths' position attributes remain unchanged
  and unflagged, with nothing indicating they may no longer be valid.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Set position attributes on booths under an event, then change the event's venue and
  check whether the position attributes are flagged.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q019

```yaml
QID: G11-EVENT_BOOTH-Q019
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When an event is cancelled while it still has active booth allocations, each of those
  allocations is moved into an explicit terminal state that reflects the cancellation,
  rather than being left exactly as it was under an event that no longer runs.
WHY_IT_MATTERS: >
  An allocation that still reads as active under a cancelled event misleads anyone later
  checking whether a space commitment still stands.
DISCONFIRMING_OBSERVATION: >
  An event is cancelled and its previously active booth allocations still show as active
  with no indication tying their state to the event's cancellation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Allocate booths under an event, cancel the event, and inspect the resulting state of
  each allocation.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q020

```yaml
QID: G11-EVENT_BOOTH-Q020
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling an event automatically propagates to release every one of its booth
  allocations rather than requiring each allocation to be released one at a time by hand
  afterward as a separate, easy-to-forget step.
WHY_IT_MATTERS: >
  A manual, easy-to-skip cleanup step after a cancellation is exactly the kind of step
  that gets missed under pressure, leaving stale allocations behind.
DISCONFIRMING_OBSERVATION: >
  An event is cancelled and its booths remain in an allocated state, with release
  requiring a separate manual action per booth rather than following automatically from
  the cancellation.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Allocate several booths under an event, cancel the event, and check whether the booths
  are released without further manual action.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q021

```yaml
QID: G11-EVENT_BOOTH-Q021
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A booth belonging to one company's event cannot be viewed, allocated, or otherwise acted
  on by a user whose access is scoped to a different company.
WHY_IT_MATTERS: >
  Leaking one company's floor plan, exhibitor list, or space availability to another
  company using the same platform breaks the tenant boundary the whole multi-company
  design depends on.
DISCONFIRMING_OBSERVATION: >
  A user scoped to one company can view or act on a booth belonging to an event owned by a
  different company.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create booths under an event owned by one company, then attempt to view or allocate them
  as a user scoped to a different company.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q022

```yaml
QID: G11-EVENT_BOOTH-Q022
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The list of booths shown as available to a prospective exhibitor respects the event's
  own visibility or publication state, and does not surface booths belonging to an event
  that has not yet been published or is otherwise hidden.
WHY_IT_MATTERS: >
  Exposing space availability for an unpublished event undermines whatever reason the
  event was kept unpublished in the first place, whether commercial timing or incomplete
  setup.
DISCONFIRMING_OBSERVATION: >
  Booths belonging to an unpublished or hidden event are visible in the general
  availability listing shown to prospective exhibitors.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create booths under an event kept in an unpublished state and check whether they appear
  in the availability listing shown externally.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q023

```yaml
QID: G11-EVENT_BOOTH-Q023
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The permission needed to withdraw or reconfigure an already-allocated booth is distinct
  from, and not automatically granted by, the permission needed to perform the initial
  allocation.
WHY_IT_MATTERS: >
  If allocating a booth implicitly grants the power to withdraw or reconfigure one already
  in use, a role meant only to assign space can inadvertently disrupt exhibitors already
  committed.
DISCONFIRMING_OBSERVATION: >
  A user role able to allocate booths can also withdraw or reconfigure an already-
  allocated booth with no separate permission check.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Compare the permission required to allocate a booth against the permission required to
  withdraw or reconfigure one that is already allocated.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q024

```yaml
QID: G11-EVENT_BOOTH-Q024
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An exhibitor's on-site staff members tied to a booth allocation are modeled and counted
  separately from the general attendee registrations of the event, with their own limit
  governed by the booth allocation rather than by the event's overall attendee capacity.
WHY_IT_MATTERS: >
  Conflating exhibitor staff with general attendees would let a large exhibiting company
  crowd out ordinary attendee capacity, or be wrongly capped by a limit meant for a
  different population.
DISCONFIRMING_OBSERVATION: >
  An exhibitor's staff member registered against their booth allocation counts against, or
  is limited by, the event's general attendee capacity rather than a limit tied to the
  booth.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Register staff against a booth allocation and check what capacity or limit their
  registration is counted against.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q025

```yaml
QID: G11-EVENT_BOOTH-Q025
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Attempting to register more staff against a booth allocation than the limit tied to that
  booth allows is rejected, not silently accepted past the configured limit.
WHY_IT_MATTERS: >
  An unenforced staff limit defeats whatever capacity or badge-printing plan the limit was
  meant to protect.
DISCONFIRMING_OBSERVATION: >
  Staff registrations against a single booth allocation exceed the limit configured for
  that booth with no rejection or warning.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Register staff against a booth allocation up to and then beyond its configured staff
  limit.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q026

```yaml
QID: G11-EVENT_BOOTH-Q026
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling one of an exhibitor's staff registrations against a booth deterministically
  frees a staff slot on that booth for a replacement, rather than leaving the slot count
  uncertain until some other action recalculates it.
WHY_IT_MATTERS: >
  An exhibitor needing to swap staff close to the event should be able to rely on an
  immediately correct available-slot count, not one that lags behind their own
  cancellation.
DISCONFIRMING_OBSERVATION: >
  Cancelling a staff registration against a booth does not immediately free a slot for a
  new staff registration against the same booth.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Fill a booth's staff limit, cancel one staff registration, and immediately attempt to
  register a replacement.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q027

```yaml
QID: G11-EVENT_BOOTH-Q027
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a booth category has zero remaining available named booths, the system reports that
  correctly and does not allow an allocation to be recorded against a booth instance that
  does not actually exist or is not actually free.
WHY_IT_MATTERS: >
  An allocation permitted against a phantom or already-committed instance defeats the
  entire purpose of tracking booths as finite, identified resources.
DISCONFIRMING_OBSERVATION: >
  An allocation is successfully recorded under a category reporting zero remaining
  available named booths, without referencing any actual free booth record.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Exhaust all named booths under a category and attempt a further allocation under that
  same category.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q028

```yaml
QID: G11-EVENT_BOOTH-Q028
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A booth category can be configured with a declared count greater than zero even though
  no named booth records have actually been created under it, and this gap between
  declared and actual is surfaced rather than silently trusted.
WHY_IT_MATTERS: >
  A declared count that nobody has to back with real records can quietly promise floor
  space that does not exist.
DISCONFIRMING_OBSERVATION: >
  A category shows a nonzero declared count with zero actual named booth records under it,
  and nothing in the system flags that gap.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a booth category with a declared count and create no named booth records under
  it, then inspect how the category's availability is reported.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q029

```yaml
QID: G11-EVENT_BOOTH-Q029
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A named booth with no category assigned is still correctly counted and reachable through
  general event-level booth reporting, rather than being silently excluded because it does
  not belong to any category grouping.
WHY_IT_MATTERS: >
  A booth invisible to reporting because it lacks a category is space nobody can plan
  around or sell, without anyone knowing it is missing.
DISCONFIRMING_OBSERVATION: >
  A named booth with no assigned category does not appear in the event's overall booth
  count or availability reporting.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a named booth under an event without assigning it to any category, then check
  whether it appears in event-level booth totals.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q030

```yaml
QID: G11-EVENT_BOOTH-Q030
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a released booth is reallocated to a new exhibitor, the record of the prior
  exhibitor's allocation is retained for later review rather than being overwritten so
  that only the newest allocation is ever visible.
WHY_IT_MATTERS: >
  Losing the history of who previously held a booth removes the ability to investigate
  disputes, no-shows, or billing questions raised after the fact.
DISCONFIRMING_OBSERVATION: >
  After a booth is released and reallocated, no record of the prior exhibitor's allocation
  can be retrieved through any normal means.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Allocate a booth to one exhibitor, release it, allocate it to a second exhibitor, and
  attempt to retrieve the first exhibitor's allocation record.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q031

```yaml
QID: G11-EVENT_BOOTH-Q031
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where the same physical booth is reused across separate editions of a recurring event,
  each edition's allocation history is scoped to that edition and does not bleed into or
  get confused with another edition's history for the same physical booth.
WHY_IT_MATTERS: >
  An allocation history that mixes editions could show a past exhibitor as still holding
  space in an edition they never registered for.
DISCONFIRMING_OBSERVATION: >
  A booth's allocation history from one event edition appears attributed to, or mixed
  with, a different edition of the same recurring event for the same physical booth.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Allocate a physical booth across two separate editions of a recurring event to different
  exhibitors and inspect each edition's allocation history independently.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q032

```yaml
QID: G11-EVENT_BOOTH-Q032
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An allocation request naming a booth identifier that does not exist under the specified
  event is explicitly rejected, rather than creating a malformed allocation record with a
  dangling reference.
WHY_IT_MATTERS: >
  A silently accepted allocation against a nonexistent booth produces a record that can
  never be resolved to any real physical space.
DISCONFIRMING_OBSERVATION: >
  An allocation request referencing a booth identifier not present under the specified
  event is accepted and creates a record rather than being rejected outright.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit an allocation request referencing a booth identifier that does not exist under
  the target event.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q033

```yaml
QID: G11-EVENT_BOOTH-Q033
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a category-level attribute that materially affects value, such as an included
  service tier, changes after some of that category's booths are already allocated, those
  already-allocated booths keep the value that was true at the time of allocation rather
  than retroactively inheriting the new category value.
WHY_IT_MATTERS: >
  Retroactively changing what an already-allocated exhibitor is entitled to, without their
  agreement, creates a mismatch between what was promised and what the live configuration
  now says.
DISCONFIRMING_OBSERVATION: >
  A category-level attribute affecting value is changed and an already-allocated booth
  under that category reflects the new value rather than what applied when it was
  allocated.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Allocate a booth under a category, change a material category-level attribute, and
  compare the allocated booth's effective value to what applied at allocation time.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q034

```yaml
QID: G11-EVENT_BOOTH-Q034
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Every allocation, release, transfer, and withdrawal action on a booth is attributable to
  a specific identified actor and a specific timestamp, not something that can only be
  guessed at from the record's current values.
WHY_IT_MATTERS: >
  Without an attributable trail, a disputed double-allocation or an unexplained withdrawal
  can never be resolved to who did what and when.
DISCONFIRMING_OBSERVATION: >
  A booth's allocation, release, transfer, or withdrawal action exists with no
  identifiable actor or timestamp recorded against it.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Perform an allocation, a release, and a withdrawal on a booth, then attempt to retrieve
  the actor and timestamp for each action.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q035

```yaml
QID: G11-EVENT_BOOTH-Q035
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a category mandates a fixed minimum set of services that cannot be removed at
  the individual booth level, versus leaving every service fully optional per booth, is a
  deliberate configuration choice that is consistently enforced, not a distinction that
  exists in name only.
WHY_IT_MATTERS: >
  A minimum service set that can quietly be stripped away at the booth level defeats
  whatever standard the category was meant to guarantee to every booth in it.
DISCONFIRMING_OBSERVATION: >
  A category configured with a mandatory minimum service set allows an individual booth
  under it to have that mandatory service removed.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a category with a mandatory minimum service, then attempt to remove that
  service from an individual booth under it.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q036

```yaml
QID: G11-EVENT_BOOTH-Q036
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Withdrawing a booth that currently has no exhibitor allocated behaves the same, at the
  data-model level, as withdrawing one that is currently allocated, aside from there being
  no exhibitor to notify, and it does not require first forcing the booth through an
  allocation step it never needed.
WHY_IT_MATTERS: >
  A withdrawal path that only works cleanly on already-allocated booths would make
  removing genuinely free space needlessly awkward.
DISCONFIRMING_OBSERVATION: >
  Withdrawing a currently unallocated booth is blocked, or requires it to first be put
  into an allocated state, before the withdrawal can be recorded.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to withdraw a booth that currently has no exhibitor allocated.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q037

```yaml
QID: G11-EVENT_BOOTH-Q037
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an exhibitor withdraws entirely from the event, ending their participation rather
  than merely releasing one booth deliberately, every booth allocated to that exhibitor is
  released as a consequence, rather than being left allocated to an exhibitor no longer
  participating.
WHY_IT_MATTERS: >
  A booth left allocated to an exhibitor who has withdrawn blocks space that could go to
  someone who still wants it, while showing no one is actually coming.
DISCONFIRMING_OBSERVATION: >
  An exhibitor's participation in the event is ended and a booth previously allocated to
  them still shows as allocated to that exhibitor.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Allocate one or more booths to an exhibitor, then end that exhibitor's participation in
  the event, and check the state of their booths afterward.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q038

```yaml
QID: G11-EVENT_BOOTH-Q038
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Through the normal supported workflow, a booth cannot end up marked as allocated while
  its exhibitor reference is broken or missing, and if a no-exhibitor-identified
  placeholder is a deliberately supported state, it remains clearly distinguishable from
  that broken-reference case.
WHY_IT_MATTERS: >
  An allocated booth with a broken exhibitor reference looks, on the surface, exactly like
  a valid placeholder hold, hiding a data problem behind what looks like ordinary business
  behaviour.
DISCONFIRMING_OBSERVATION: >
  A booth shows as allocated but its exhibitor reference cannot be resolved to any actual
  exhibitor record, and this state is not distinguishable from a deliberate no-exhibitor-
  identified placeholder.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt, through the normal supported workflow, to reach a state where an allocated
  booth's exhibitor reference cannot be resolved, and compare it against a deliberate
  placeholder allocation.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q039

```yaml
QID: G11-EVENT_BOOTH-Q039
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deactivating or removing the underlying exhibitor contact record that holds active booth
  allocations triggers a defined handling path, rather than leaving those allocations
  pointing at a party that no longer exists in the system.
WHY_IT_MATTERS: >
  An allocation orphaned by a deactivated exhibitor record can neither be honoured,
  transferred, nor cleanly cancelled without someone first noticing it.
DISCONFIRMING_OBSERVATION: >
  The underlying exhibitor record behind an active booth allocation is deactivated or
  removed, and the allocation remains unchanged with no flag or triggered handling.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Deactivate or remove the exhibitor record referenced by an active booth allocation and
  inspect the allocation's resulting state.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q040

```yaml
QID: G11-EVENT_BOOTH-Q040
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A summary count of booths available at an event correctly excludes withdrawn booths from
  both the count of available spaces and the total number of spaces the event is
  considered to have, not just from the available count alone.
WHY_IT_MATTERS: >
  Counting a withdrawn booth in the total while excluding it from availability makes the
  event look larger than the space it can actually offer.
DISCONFIRMING_OBSERVATION: >
  A withdrawn booth is excluded from the available count shown for an event but still
  counted in the event's total booth count.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Withdraw a booth under an event and compare the event's reported available count and
  total count before and after.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q041

```yaml
QID: G11-EVENT_BOOTH-Q041
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A booth category cannot be deleted outright while named booth records still reference
  it; it can only be withdrawn or deprecated in a way that preserves the reference those
  booths depend on.
WHY_IT_MATTERS: >
  Deleting a category still in use would leave its named booths referencing something that
  no longer exists, corrupting whatever reporting or pricing depends on that category.
DISCONFIRMING_OBSERVATION: >
  A booth category with active named booth records still referencing it is deleted
  outright, and those booth records are left with an unresolved category reference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to delete a booth category while named booth records still reference it.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q042

```yaml
QID: G11-EVENT_BOOTH-Q042
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a release of a booth and a new allocation request for that same booth arrive in
  close succession, the outcome follows a defined ordering rule rather than depending on
  unspecified timing that could go either way.
WHY_IT_MATTERS: >
  An outcome that depends on unspecified timing means the same sequence of actions can
  produce different, unrepeatable results, making the system impossible to reason about
  under load.
DISCONFIRMING_OBSERVATION: >
  A release and a competing allocation request for the same booth, submitted in close
  succession, produce different outcomes across repeated trials with no documented rule
  explaining which should win.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Submit a release and a competing allocation request for the same booth in close
  succession, repeated across multiple trials.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q043

```yaml
QID: G11-EVENT_BOOTH-Q043
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Changing the exhibitor referenced by an allocation that currently sits on a withdrawn
  booth is rejected, rather than silently succeeding and producing a record of an
  exhibitor holding a booth that no longer exists on the floor.
WHY_IT_MATTERS: >
  Allowing an exhibitor change on a withdrawn booth's allocation manufactures a new,
  equally invalid claim on space that has already been removed.
DISCONFIRMING_OBSERVATION: >
  The exhibitor referenced by an allocation on a withdrawn booth is successfully changed
  to a different exhibitor.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Withdraw a booth that carries an active allocation, then attempt to change the exhibitor
  referenced by that allocation.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q044

```yaml
QID: G11-EVENT_BOOTH-Q044
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a booth withdrawal is reversed and the booth reinstated, it returns to the
  available pool for a fresh allocation decision rather than automatically restoring the
  exhibitor who held it before the withdrawal.
WHY_IT_MATTERS: >
  Automatically restoring a prior exhibitor without a deliberate decision could reassign
  space that has, in the interim, already been promised or reallocated to someone else.
DISCONFIRMING_OBSERVATION: >
  Reversing a booth's withdrawal automatically restores the previous exhibitor's
  allocation with no fresh allocation decision taken.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Allocate a booth, withdraw it, then reverse the withdrawal, and check whether the prior
  exhibitor's allocation is automatically restored.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q045

```yaml
QID: G11-EVENT_BOOTH-Q045
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Whether an exhibitor-side user can release their own booth allocation without organizer
  involvement is a defined permission choice, and when self-service release is allowed, it
  is logged with the same actor-and-timestamp rigor as an organizer-initiated release.
WHY_IT_MATTERS: >
  A self-service release logged less rigorously than a staff-initiated one creates a gap
  in the audit trail exactly where disputes over who released a booth, and when, are most
  likely to arise.
DISCONFIRMING_OBSERVATION: >
  An exhibitor-side user releases their own booth allocation and the resulting log entry
  lacks the actor or timestamp detail that an organizer-initiated release would carry.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Have an exhibitor-side user release their own booth allocation, if permitted, and
  compare the resulting log entry to one produced by an organizer-initiated release.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q046

```yaml
QID: G11-EVENT_BOOTH-Q046
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A booth's visibility respects not only the company that owns its event but any branch-
  level scoping that company applies to its own events, rather than treating company-level
  scoping as the only boundary that matters.
WHY_IT_MATTERS: >
  A company operating multiple branches may need one branch's events kept from another's
  users even within the same company, and ignoring that finer boundary leaks space and
  exhibitor data across branches.
DISCONFIRMING_OBSERVATION: >
  A user scoped to one branch of a company can view or act on booths belonging to an event
  the company has scoped to a different branch.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create an event scoped to one branch of a company and attempt to view or act on its
  booths as a user scoped to a different branch of the same company.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q047

```yaml
QID: G11-EVENT_BOOTH-Q047
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Between a booth's plain available state and a completed allocated state, there is either
  an explicit, named transitional hold state the design defines and exposes, or the
  transition is genuinely atomic with nothing in between, but the platform does not
  present an undocumented in-between state that behaves inconsistently depending on where
  it is viewed from.
WHY_IT_MATTERS: >
  An undocumented, inconsistent in-between state means two different views of the same
  booth can disagree about whether it is actually free.
DISCONFIRMING_OBSERVATION: >
  A booth is observed in a state that is neither the defined available state nor the
  defined allocated state, and that in-between condition is not a documented, named state
  of its own.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Observe a booth's state at each step of an allocation action to determine whether an
  explicit intermediate state exists or the transition is atomic.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q048

```yaml
QID: G11-EVENT_BOOTH-Q048
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A booth category's declared count and a live count of the named booth records that
  actually exist under it are checked against each other, and any disagreement between the
  two is flagged rather than the declared figure being trusted at face value everywhere it
  is used.
WHY_IT_MATTERS: >
  Trusting a declared figure that can silently disagree with reality means every
  downstream use of that count, sales, reporting, floor planning, inherits an error nobody
  chose to accept.
DISCONFIRMING_OBSERVATION: >
  A category's declared count disagrees with a live count of its actual named booth
  records, and the declared figure is used elsewhere in the system with no flag raised.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Deliberately create a disagreement between a category's declared count and its actual
  named booth records, then check whether that disagreement is surfaced anywhere the count
  is used.
LAYER: BASE
```

## G11-EVENT_BOOTH-Q049

```yaml
QID: G11-EVENT_BOOTH-Q049
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When an exhibitor's on-site staff have already been checked in and a booth is later
  withdrawn mid-event, their check-in access is handled by a defined rule, revoked,
  retained, or flagged for review, rather than continuing or vanishing purely as an
  accidental side effect of the booth's own state change.
WHY_IT_MATTERS: >
  Leaving on-site access as an unintended side effect of a booth's withdrawal means nobody
  actually decided whether those staff should still be on the premises.
DISCONFIRMING_OBSERVATION: >
  A booth is withdrawn mid-event while its exhibitor's staff are already checked in, and
  their check-in access changes or persists with no traceable rule governing which
  happened.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Check in an exhibitor's staff against a booth, withdraw that booth mid-event, and
  inspect what happens to the staff's check-in access.
LAYER: PROCESS
```

## G11-EVENT_BOOTH-Q050

```yaml
QID: G11-EVENT_BOOTH-Q050
MODULE: event_booth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A booth is associated with exactly one category at a time for the purpose of category-
  level counting, and if the design allows a booth to carry more than one category-like
  designation, it is not counted toward more than one category's availability total
  simultaneously.
WHY_IT_MATTERS: >
  A booth counted in more than one category's total overstates the real available space in
  every category it is double-counted under.
DISCONFIRMING_OBSERVATION: >
  A single named booth is counted toward the available or total figure of more than one
  category at the same time.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to associate a single named booth with more than one category designation and
  check whether it is counted under each.
LAYER: BASE
```
