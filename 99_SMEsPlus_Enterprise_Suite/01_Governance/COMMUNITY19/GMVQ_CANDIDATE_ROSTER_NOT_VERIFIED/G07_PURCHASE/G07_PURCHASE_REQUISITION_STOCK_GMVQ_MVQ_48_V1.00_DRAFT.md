# SMEsPlus ENTERPRISE SUITE
## GMVQ — G07 PURCHASE / purchase_requisition_stock Module Adversarial MVQ Bank

**Document ID:** GMVQ-G07-PURCHASE_REQUISITION_STOCK-MVQ48-V1.00
**Group:** G07 PURCHASE
**Module Metadata:** `purchase_requisition_stock`
**Wave:** W2
**Author Cell:** P18 (GMVQ Question Factory — Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `purchase_requisition_stock` — a BRIDGE per
GMVQ_BRIDGE_MODULE_RULE_V1.00, seam: an internal purchase requisition raised from an AUTOMATIC
STOCK RULE. The requisition's own invariants (selection, award mechanics, agreement validity and
exhaustion, approval authority over the award in general) belong to the `purchase_requisition`
family base and are deliberately NOT re-asked here. This bank asks only what happens at the seam
where nobody decided — a rule did — and the conditions that justified it may no longer hold: the
rule's trigger condition resolving before the tender closes; the same shortage triggering a second
requisition while the first is open; stock arriving from another source in the meantime; the
rule's own parameters changing after the requisition was raised; a quantity rounded up by the rule
and the excess nobody owns; the resulting movement and its destination; a rule firing across
warehouses or companies; who reviews an automatically raised requisition before money commits, and
whether it can reach commitment with no human at all; suppression of duplicate automatic
requisitions; and traceability from the eventual receipt back to the rule that caused it. Every
question was tested against the bridge rule: if it would read equally well with no automatic rule
in the picture — i.e. for an ordinary, manually raised requisition — it was cut.

The question text is source-neutral and does not expose vendor model names, field names, methods,
schema, XML IDs, API shapes, or implementation algorithms. `MODULE: purchase_requisition_stock`
appears only in the structured metadata field, never inside question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that states a concrete failure state.
- No padding: 48 questions exist because they test 48 distinct material hypotheses at the seam.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `module + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
- BRIDGE MODULE per GMVQ_BRIDGE_MODULE_RULE_V1.00: every question fails only at the seam between an
  automatic stock rule and the requisition it raises. None restates a `purchase_requisition` award,
  selection, or agreement-validity invariant that holds with no automatic rule present, and none is
  a pure stock-replenishment invariant restated with this module's name attached.
- Cross-check performed against the sibling `purchase_requisition_sale` bank authored in the same
  batch: no `DISCONFIRMING_OBSERVATION` in either bank describes the same event as one in the
  other — the two origins (customer commitment vs. automatic stock rule) do not overlap in ground.
- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' <G07 siblings>/*.md | sort`
  was run against the existing `purchase` (base) and `purchase_edi_ubl_bis3` banks before authoring.
  No overlap found; those banks cover order/receipt/bill tolerance, currency, approval thresholds,
  duplicate detection, and vendor lifecycle — none of it origin-of-demand ground.

## G07-PURCHASE_REQUISITION_STOCK-Q001

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q001
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the stock condition that triggered an automatic requisition, such as the shortage it was
  raised to cover, no longer holds by the time the tender closes, that change is surfaced before
  award rather than the requisition proceeding to award as if the original trigger were still
  valid.
WHY_IT_MATTERS: >
  Awarding against a shortage that has already resolved itself commits money and stock space to
  nothing the business still needs.
DISCONFIRMING_OBSERVATION: >
  The stock position that triggered the automatic requisition has already recovered by the time of
  award, and the requisition proceeds to award the full original quantity with no flag.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Let an automatic requisition's triggering shortage resolve itself, through another movement or
  correction, before its tender closes, then continue the requisition to award.
```

## G07-PURCHASE_REQUISITION_STOCK-Q002

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q002
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The same underlying shortage does not generate a second automatic requisition while an earlier
  one raised for it is still open, unless a deliberate reason for a second one is recorded.
WHY_IT_MATTERS: >
  Two open requisitions for the same shortage risk double-ordering the same stock with nobody
  realizing both are live.
DISCONFIRMING_OBSERVATION: >
  A second automatic requisition is raised for a shortage that already has an open, unresolved
  requisition covering it, with no recorded reason distinguishing the two.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Leave an automatically raised requisition open and let the same shortage condition persist or
  recur, then check whether a second requisition is raised.
```

## G07-PURCHASE_REQUISITION_STOCK-Q003

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q003
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whatever mechanism prevents a duplicate automatic requisition for the same shortage does not
  also suppress a new requisition when the shortage has genuinely grown larger than what the open
  requisition already covers.
WHY_IT_MATTERS: >
  Overly broad duplicate suppression would silently under-cover a shortage that has gotten worse
  since the first requisition was raised.
DISCONFIRMING_OBSERVATION: >
  The shortage grows larger than the quantity already covered by an open automatic requisition,
  and no further requisition or adjustment is raised for the additional amount.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Increase the shortage beyond what an already-open automatic requisition covers, then check
  whether the additional amount is picked up.
```

## G07-PURCHASE_REQUISITION_STOCK-Q004

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q004
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If stock that resolves the shortage arrives from a source other than the requisition raised to
  cover it, for example a transfer or a return, the open automatic requisition is reduced or
  flagged rather than continuing toward award for stock that has effectively already arrived.
WHY_IT_MATTERS: >
  Awarding a requisition for stock that has already arrived by another route creates avoidable
  excess inventory.
DISCONFIRMING_OBSERVATION: >
  Stock resolving the shortage arrives through an unrelated movement, and the open automatic
  requisition proceeds to award without adjustment or flag.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Resolve the triggering shortage through a movement unrelated to the open requisition, then
  observe whether the requisition adjusts.
```

## G07-PURCHASE_REQUISITION_STOCK-Q005

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q005
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing the replenishment rule's parameters after a requisition has already been raised from it
  does not silently alter the quantity or terms of that already-raised requisition to match the
  new parameters.
WHY_IT_MATTERS: >
  A requisition whose quantity silently shifts after being raised no longer reflects the decision,
  or the shortage, that actually caused it.
DISCONFIRMING_OBSERVATION: >
  Changing the rule's parameters after a requisition has already been raised causes that existing
  requisition's quantity or terms to change without any explicit action on the requisition itself.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Raise an automatic requisition, then change the underlying rule's parameters, and check the
  already-raised requisition for unexplained changes.
```

## G07-PURCHASE_REQUISITION_STOCK-Q006

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q006
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A change to the replenishment rule's parameters is reflected in the next requisition the rule
  raises, rather than the rule continuing to fire using values cached from before the change.
WHY_IT_MATTERS: >
  A rule that ignores its own updated parameters defeats the purpose of adjusting it and can go
  unnoticed for a long time.
DISCONFIRMING_OBSERVATION: >
  After changing the rule's parameters, the next automatically raised requisition still reflects
  the old parameters rather than the new ones.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Change the rule's parameters, then trigger a new firing of the rule and inspect the resulting
  requisition.
```

## G07-PURCHASE_REQUISITION_STOCK-Q007

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q007
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a rule rounds the raised quantity up, for example to a pack or batch size, past what the
  shortage strictly requires, the resulting excess is attributable to a recorded rounding rule
  rather than appearing as an unexplained extra quantity nobody accounts for.
WHY_IT_MATTERS: >
  An unexplained excess quantity looks like an error to anyone reviewing the requisition later and
  invites unnecessary investigation, or worse, goes uninvestigated when it should not.
DISCONFIRMING_OBSERVATION: >
  The requisitioned quantity exceeds the shortage that triggered it, and nothing on the requisition
  indicates that the excess is a deliberate rounding rather than a mistake.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Trigger a rule that rounds the requisitioned quantity up beyond the exact shortage, then inspect
  the requisition for an explanation of the difference.
```

## G07-PURCHASE_REQUISITION_STOCK-Q008

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q008
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The portion of a received quantity that exceeds the original shortage, due to rounding, remains
  identifiable as excess after receipt, rather than blending invisibly into general stock with no
  record of why more arrived than was short.
WHY_IT_MATTERS: >
  An untracked excess distorts future shortage calculations if the rule does not know that surplus
  already exists.
DISCONFIRMING_OBSERVATION: >
  After receipt of a rounded-up quantity, there is no way to identify how much of the received
  stock was the original shortage versus the rounding excess.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Receive a full rounded-up quantity from an automatic requisition and attempt to distinguish the
  excess portion in the resulting stock record.
```

## G07-PURCHASE_REQUISITION_STOCK-Q009

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q009
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The stock movement resulting from an automatically raised requisition delivers to the specific
  location whose shortage triggered the rule, not to a default or generic location that may not be
  the one actually short.
WHY_IT_MATTERS: >
  Replenishment landing anywhere other than the shortage location fails to solve the problem the
  rule exists to solve.
DISCONFIRMING_OBSERVATION: >
  The receipt resulting from an automatic requisition is recorded at a location other than the one
  whose shortage triggered the rule, with the original shortage location still short.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a rule tied to a specific shortage location, complete the resulting requisition through
  to receipt, and check the destination location recorded.
```

## G07-PURCHASE_REQUISITION_STOCK-Q010

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q010
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a single rule construct can fire across more than one warehouse, a shortage in one
  warehouse and a separate shortage in another are not combined into a single requisition that
  then delivers the combined quantity to only one of them.
WHY_IT_MATTERS: >
  Combining two warehouses' shortages into one delivery leaves one warehouse still short while the
  other holds stock it did not need as urgently.
DISCONFIRMING_OBSERVATION: >
  Shortages in two different warehouses covered by the same rule produce a single requisition
  whose resulting receipt goes entirely to one warehouse, leaving the other's shortage unresolved.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger the same rule construct from shortages in two different warehouses and inspect how many
  requisitions result and where the stock lands.
```

## G07-PURCHASE_REQUISITION_STOCK-Q011

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q011
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  If a replenishment rule can fire in a way that spans more than one company, the requisition it
  raises, and the money it commits, is attributed to the company whose stock was actually short,
  not to a different company by default.
WHY_IT_MATTERS: >
  Attributing procurement spend to the wrong company misstates that company's books and can commit
  money without the right company's authorization.
DISCONFIRMING_OBSERVATION: >
  A rule spanning companies raises a requisition attributed to a company other than the one whose
  location actually recorded the shortage.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Set up a rule construct spanning two companies, trigger a shortage in one, and check which
  company the resulting requisition is raised under.
```

## G07-PURCHASE_REQUISITION_STOCK-Q012

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q012
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An automatically raised requisition passes through a point where a person can review it before
  any money is actually committed to a vendor, unless the organization has explicitly configured
  full automation for that rule.
WHY_IT_MATTERS: >
  A rule that can commit spend with no review point by default removes human judgment from a
  decision an organization may not have intended to fully automate.
DISCONFIRMING_OBSERVATION: >
  An automatically raised requisition proceeds all the way to a committed vendor order with no
  review step available and no configuration setting was made to enable full automation.
EXPECTED_SURFACE: S3,S4,S7
PRECONDITIONS: >
  Let a rule raise a requisition under default configuration and trace whether a review step
  exists before commitment.
```

## G07-PURCHASE_REQUISITION_STOCK-Q013

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q013
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where an automatically raised requisition is allowed to proceed to award and commitment with no
  human step at all, that behavior is the result of an explicit, recorded configuration choice,
  not an incidental default nobody chose.
WHY_IT_MATTERS: >
  An organization should be able to show, on review, that fully unattended spend commitment was a
  deliberate decision and by whom.
DISCONFIRMING_OBSERVATION: >
  A requisition proceeds to a fully committed vendor order with no human step, and no configuration
  record shows anyone deliberately enabled that behavior.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Find an automatically raised requisition that reached commitment with no human step and check
  for a configuration record authorizing that path.
```

## G07-PURCHASE_REQUISITION_STOCK-Q014

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q014
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A person reviewing an automatically raised requisition before commitment can see what shortage
  and which rule triggered it, not only the resulting requisition lines with no context for why
  they exist.
WHY_IT_MATTERS: >
  A reviewer who cannot see the triggering condition cannot meaningfully judge whether the
  requisition is still justified.
DISCONFIRMING_OBSERVATION: >
  The review step for an automatically raised requisition shows only the requisition lines, with
  no way to see the shortage or rule that caused it to be raised.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Reach the review step for an automatically raised requisition and check whether the triggering
  shortage and rule are visible from there.
```

## G07-PURCHASE_REQUISITION_STOCK-Q015

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q015
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a duplicate automatic requisition is suppressed in favor of an already-open one, the
  surviving requisition still goes through whatever review step it would otherwise require, rather
  than the suppression event itself being treated as equivalent to review.
WHY_IT_MATTERS: >
  Duplicate suppression is a stock-level decision and should not double as an approval decision it
  was never designed to be.
DISCONFIRMING_OBSERVATION: >
  A duplicate requisition is suppressed, and the surviving requisition is found to have skipped its
  normal review step as a result of the suppression event.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Trigger a duplicate suppression scenario and check whether the surviving requisition's review
  step still occurs normally.
```

## G07-PURCHASE_REQUISITION_STOCK-Q016

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q016
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A receipt resulting from an automatically raised requisition can be traced back to the specific
  rule and the shortage condition that caused the requisition to be raised in the first place.
WHY_IT_MATTERS: >
  Without that trace, nobody reviewing incoming stock later can tell whether it arrived because of
  a genuine need or a misconfigured rule.
DISCONFIRMING_OBSERVATION: >
  A receipt exists that resulted from an automatically raised requisition, but no trace from the
  receipt leads back to the rule or the shortage that caused it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete an automatically raised requisition through to receipt, then attempt to trace back from
  the receipt to the originating rule.
```

## G07-PURCHASE_REQUISITION_STOCK-Q017

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q017
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  If the replenishment rule that caused a requisition is later deactivated or removed, the trace
  from an already-completed receipt back to that rule's identity still resolves, rather than
  pointing to nothing once the rule no longer exists.
WHY_IT_MATTERS: >
  Rules get tuned and retired over time, and losing the historical trace when that happens erases
  the reason for past procurement.
DISCONFIRMING_OBSERVATION: >
  After the triggering rule is deactivated or deleted, the trace from a previously completed
  receipt back to it no longer resolves to anything.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Complete a requisition-to-receipt cycle from a rule, then deactivate or remove that rule, and
  attempt to trace back from the receipt.
```

## G07-PURCHASE_REQUISITION_STOCK-Q018

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q018
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A requisition raised automatically by a stock rule carries a recorded, observable fact
  distinguishing it from a manually raised requisition, not something inferable only by noticing
  nobody manually created it.
WHY_IT_MATTERS: >
  Without a recorded origin, no report or control that treats automatic and manual demand
  differently can be built reliably.
DISCONFIRMING_OBSERVATION: >
  There is no field, tag, or record identifying a requisition as automatically raised, and the only
  way to tell is the absence of any sign that a person created it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Raise a requisition automatically through the rule and look for a direct, recorded indicator of
  that origin on the requisition.
```

## G07-PURCHASE_REQUISITION_STOCK-Q019

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q019
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether the shortage resolves itself before the rule's own evaluation runs, versus resolving just
  after a requisition has already been raised, produces genuinely different, and correctly
  different, outcomes rather than the same requisition existing regardless of when the resolution
  happened.
WHY_IT_MATTERS: >
  If the timing of resolution relative to rule evaluation makes no difference, the rule is not
  actually checking current stock at the moment it decides to act.
DISCONFIRMING_OBSERVATION: >
  A requisition is raised even when the shortage had already resolved before the rule's own
  evaluation ran, exactly as if the resolution had happened afterward instead.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Resolve the shortage just before the rule's scheduled evaluation in one run, and just after in
  another, and compare the outcomes.
```

## G07-PURCHASE_REQUISITION_STOCK-Q020

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q020
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the rule's evaluation runs twice in close succession, whether through overlapping scheduled
  passes or a manual trigger alongside a scheduled one, the two runs do not each independently
  raise a requisition for the same still-open shortage.
WHY_IT_MATTERS: >
  A race between two evaluations of the same rule is exactly the condition duplicate suppression is
  meant to prevent, and it is most likely to fail under real concurrency rather than a single clean
  run.
DISCONFIRMING_OBSERVATION: >
  Two overlapping evaluations of the same rule for the same shortage each raise their own
  requisition, resulting in two open requisitions for one shortage.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Force two evaluations of the same rule to run close together against the same unresolved
  shortage.
```

## G07-PURCHASE_REQUISITION_STOCK-Q021

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q021
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If a person is in the middle of manually creating a requisition for a shortage at the same
  moment the automatic rule also fires for it, the two do not both end up as separate open
  requisitions with nothing linking or reconciling them.
WHY_IT_MATTERS: >
  Two independently created requisitions for the same real shortage, one manual and one automatic,
  is the same double-cover risk as two automatic ones, just harder to anticipate.
DISCONFIRMING_OBSERVATION: >
  A manually created requisition and an automatically raised one both exist for the same shortage
  at the same time, with neither one aware of the other.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Begin manually creating a requisition for a shortage while the automatic rule is also due to fire
  for the same condition, and observe the result.
```

## G07-PURCHASE_REQUISITION_STOCK-Q022

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q022
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the quantity on an automatically raised requisition is edited by hand after creation, the
  rule's own record of what it believes it has already covered is updated to match, rather than
  the rule continuing to track its original, now-incorrect value.
WHY_IT_MATTERS: >
  If the rule keeps tracking a stale value after a manual edit, it may under- or over-trigger the
  next time it evaluates the same shortage.
DISCONFIRMING_OBSERVATION: >
  The requisition quantity is manually changed after automatic creation, and a later rule
  evaluation behaves as though the original, unedited quantity is still what was requisitioned.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Manually edit the quantity on an automatically raised, still-open requisition, then trigger
  another evaluation of the same rule.
```

## G07-PURCHASE_REQUISITION_STOCK-Q023

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q023
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Cancelling an automatically raised requisition, for whatever reason, leaves the underlying
  shortage visible to the rule again so that it can be picked up on a future evaluation, rather
  than the cancellation being treated as if the shortage had been resolved.
WHY_IT_MATTERS: >
  A cancelled requisition that quietly closes out the shortage as though covered leaves a real gap
  in stock the rule will never revisit.
DISCONFIRMING_OBSERVATION: >
  After an automatically raised requisition is cancelled, a subsequent rule evaluation does not
  raise a new requisition for the same still-unresolved shortage.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Cancel an automatically raised, still-unresolved requisition, then trigger another evaluation of
  the same rule.
```

## G07-PURCHASE_REQUISITION_STOCK-Q024

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q024
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the vendor fails to fulfil an automatically raised requisition, the underlying shortage is not
  marked as resolved on the strength of the requisition having existed, and remains something the
  rule, or a person, can still act on.
WHY_IT_MATTERS: >
  A shortage that is considered handled just because a requisition was once raised for it,
  regardless of whether anything actually arrived, is a silent stockout waiting to happen.
DISCONFIRMING_OBSERVATION: >
  A vendor fails to deliver against an automatically raised requisition, and the shortage it was
  meant to cover shows as resolved or is never picked up again by the rule.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Fail vendor fulfillment against an automatically raised requisition and observe whether the
  shortage is later re-evaluated.
```

## G07-PURCHASE_REQUISITION_STOCK-Q025

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q025
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Money committed through an automatically raised requisition counts against the same spend
  visibility and controls, such as budget or approval-limit tracking, as money committed through a
  manually raised one.
WHY_IT_MATTERS: >
  If automatic spend is invisible to the same controls, actual commitments can exceed what anyone
  reviewing spend against budget believes has been committed.
DISCONFIRMING_OBSERVATION: >
  Spend committed through automatically raised requisitions does not appear in the same spend
  tracking or approval-limit calculations that manually raised requisitions are subject to.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Commit spend through an automatically raised requisition and check whether it appears in the
  same spend controls as manual requisitions.
```

## G07-PURCHASE_REQUISITION_STOCK-Q026

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q026
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Deactivating a replenishment rule does not affect a requisition it already raised that is still
  open — that requisition continues through its own lifecycle independent of whether the rule that
  created it still exists.
WHY_IT_MATTERS: >
  An open requisition abandoned or stuck because its parent rule was turned off would silently
  orphan a commitment already made.
DISCONFIRMING_OBSERVATION: >
  Deactivating the rule causes an already-open requisition it raised to become stuck, blocked, or
  unable to progress through its normal lifecycle.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Deactivate a rule while a requisition it raised is still open, then attempt to progress that
  requisition normally.
```

## G07-PURCHASE_REQUISITION_STOCK-Q027

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q027
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The person who configured or owns the replenishment rule is not, by default, automatically also
  the approver of the requisitions it raises, unless assigned that role deliberately.
WHY_IT_MATTERS: >
  Collapsing rule ownership and requisition approval into the same person removes the independent
  check the review step is meant to provide.
DISCONFIRMING_OBSERVATION: >
  The requisition approval step for an automatically raised requisition is assigned, without any
  explicit configuration, to the same person who set up the triggering rule.
EXPECTED_SURFACE: S3,S4,S7
PRECONDITIONS: >
  Trace who is assigned to approve requisitions raised by a given rule and compare that against who
  configured the rule.
```

## G07-PURCHASE_REQUISITION_STOCK-Q028

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q028
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A configured replenishment rule can be observed actually firing and raising a requisition when
  its condition is met, not merely existing as a configuration record with no confirmable runtime
  effect.
WHY_IT_MATTERS: >
  A rule that looks correctly configured but never actually fires gives false confidence that
  replenishment is being handled.
DISCONFIRMING_OBSERVATION: >
  A rule's condition is met in the running system, and no requisition is raised, with no error or
  log explaining why.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Bring stock to the exact condition the rule is configured to react to and observe whether a
  requisition is actually raised.
```

## G07-PURCHASE_REQUISITION_STOCK-Q029

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q029
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The setting controlling whether an automatically raised requisition requires human review before
  commitment is something an administrator can actually find and change, not a behavior fixed in
  the rule's logic with no corresponding control surfaced anywhere.
WHY_IT_MATTERS: >
  A control that exists only in documentation and not in the actual configuration surface cannot be
  relied on by the organization that needs it.
DISCONFIRMING_OBSERVATION: >
  No configuration option can be found anywhere that controls whether an automatically raised
  requisition requires human review before commitment.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Search the available configuration for a setting controlling human review before commitment on
  automatically raised requisitions.
```

## G07-PURCHASE_REQUISITION_STOCK-Q030

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q030
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the documented design states that an automatically raised requisition always requires human
  review before commitment, the running system does not actually allow that requisition to reach
  commitment without it.
WHY_IT_MATTERS: >
  A gap between what is documented as a control and what the running system actually enforces is
  exactly the kind of contradiction the study is meant to surface.
DISCONFIRMING_OBSERVATION: >
  The running system commits an automatically raised requisition with no human review having
  occurred, despite review being described as mandatory.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Attempt to push an automatically raised requisition to commitment without performing any review
  step, in a configuration where review is documented as mandatory.
```

## G07-PURCHASE_REQUISITION_STOCK-Q031

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q031
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A stock shortage that falls outside what any configured rule is set to watch does not itself
  cause a requisition to be raised as though a rule had fired for it.
WHY_IT_MATTERS: >
  A requisition appearing with no rule actually responsible for it would be unexplainable and would
  undermine trust in the traceability the rule mechanism is meant to provide.
DISCONFIRMING_OBSERVATION: >
  A requisition is automatically raised for a shortage that no configured rule was set to watch,
  with no rule identifiable as its cause.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Create a shortage condition deliberately outside the scope of any configured rule and observe
  whether a requisition is nonetheless raised.
```

## G07-PURCHASE_REQUISITION_STOCK-Q032

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q032
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the quantity considered available for a location is manually adjusted, such as a correction or
  an override outside ordinary movements, the rule's shortage calculation reflects that adjustment
  rather than continuing to calculate from a value the adjustment was meant to correct.
WHY_IT_MATTERS: >
  A rule that ignores manual corrections to the numbers it depends on can keep re-raising
  requisitions for a shortage that has already been corrected.
DISCONFIRMING_OBSERVATION: >
  After a manual adjustment corrects the available quantity, the rule's next evaluation still
  raises a requisition based on the pre-correction quantity.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Manually adjust the quantity underlying a rule's shortage calculation, then trigger another
  evaluation.
```

## G07-PURCHASE_REQUISITION_STOCK-Q033

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q033
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The stock movement that results from receiving against an automatically raised requisition
  carries some recorded indication that it originated from an automatic rule, not only the
  requisition it came from carrying that fact with the movement itself silent on it.
WHY_IT_MATTERS: >
  Someone auditing movements directly, without first finding the requisition, needs the movement
  itself to be traceable to its automatic origin.
DISCONFIRMING_OBSERVATION: >
  The stock movement resulting from an automatic requisition's receipt carries no indication,
  direct or by reference, that it originated from a rule rather than a manual requisition.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete an automatic requisition through to receipt and inspect the resulting movement record
  directly for any indication of its origin.
```

## G07-PURCHASE_REQUISITION_STOCK-Q034

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q034
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The rounding excess portion of a received quantity is delivered to the same destination as the
  portion that covers the actual shortage, not split to a different location without a stated
  reason.
WHY_IT_MATTERS: >
  An unexplained split destination for the excess portion would be an easy way for stock to end up
  somewhere nobody is tracking it.
DISCONFIRMING_OBSERVATION: >
  The rounding excess from a received quantity is recorded at a different destination location
  than the portion covering the original shortage, with no stated reason.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Receive a rounded-up quantity from an automatic requisition and compare the destination of the
  excess portion against the shortage-covering portion.
```

## G07-PURCHASE_REQUISITION_STOCK-Q035

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q035
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing the rule's parameters after a requisition it raised has already been awarded does not
  alter the terms already committed to a vendor on that award.
WHY_IT_MATTERS: >
  Retroactively altering an already-committed award based on a later configuration change would
  create a mismatch between what was agreed and what the system now records.
DISCONFIRMING_OBSERVATION: >
  Changing the rule's parameters after award causes the already-awarded requisition's committed
  quantity or terms to change without a new, explicit action.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Award a requisition raised by a rule, then change the rule's parameters, and check the awarded
  requisition's terms for any unexplained change.
```

## G07-PURCHASE_REQUISITION_STOCK-Q036

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q036
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Suppression logic meant to prevent duplicate requisitions for the same shortage does not also
  suppress a second requisition when the second shortage, though triggered by the same rule
  construct, is actually a separate shortage at a different location.
WHY_IT_MATTERS: >
  Over-broad suppression by rule identity alone, rather than by the specific shortage, would leave
  a genuinely separate location's need unmet.
DISCONFIRMING_OBSERVATION: >
  A shortage at a second location is not covered by any requisition because an existing requisition
  from the same rule, covering a different location's shortage, is treated as already covering it.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger the same rule construct for two genuinely separate location shortages close together and
  check whether both are covered.
```

## G07-PURCHASE_REQUISITION_STOCK-Q037

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q037
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A role that holds ordinary requisition approval permission cannot use that permission alone to
  bypass a mandated review step specifically required for automatically raised requisitions, unless
  separately granted that ability.
WHY_IT_MATTERS: >
  If ordinary approval permission is enough to bypass the automatic-requisition review step, the
  extra control the review step was meant to add does not actually exist.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary requisition approval permission is able to bypass the review step
  specifically required for automatically raised requisitions.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Attempt to bypass the automatic-requisition review step using an account with only ordinary
  requisition approval permission.
```

## G07-PURCHASE_REQUISITION_STOCK-Q038

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q038
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a rule is configured to fully automate a requisition through to commitment with no human
  step, the record shows who made that configuration choice and when, not just that the setting is
  currently on.
WHY_IT_MATTERS: >
  A full-automation setting with no record of who enabled it cannot be reviewed or held accountable
  later if it produces an unwanted commitment.
DISCONFIRMING_OBSERVATION: >
  A rule is configured for full automation with no human step, and there is no record of who set
  that configuration or when.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Find a rule configured for full automation and check for a record of who enabled that
  configuration.
```

## G07-PURCHASE_REQUISITION_STOCK-Q039

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q039
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user configuring a replenishment rule cannot set it to fire for a location or company outside
  their own permission scope, committing spend somewhere they would not otherwise be authorized to
  act.
WHY_IT_MATTERS: >
  A rule is a standing, unattended instruction, so a scope gap in who can point it where is more
  dangerous than an equivalent gap in a one-time manual action.
DISCONFIRMING_OBSERVATION: >
  A user configures a rule to fire for a location or company outside their own permission scope,
  and the configuration is accepted with no restriction.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Attempt to configure a rule to fire for a location or company the configuring user's own
  permissions do not otherwise cover.
```

## G07-PURCHASE_REQUISITION_STOCK-Q040

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q040
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When the rule's evaluation runs, and how often, is recorded and can be checked after the fact,
  rather than being an assumed cadence that can only be inferred from when requisitions happen to
  appear.
WHY_IT_MATTERS: >
  Diagnosing why a shortage went unaddressed for too long requires knowing whether the rule ran on
  schedule or not at all.
DISCONFIRMING_OBSERVATION: >
  There is no record of when the rule's evaluation actually ran, and the only way to guess its
  cadence is to infer it from the timestamps of resulting requisitions.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Look for a record of the rule's own evaluation runs, independent of the requisitions those runs
  may or may not have produced.
```

## G07-PURCHASE_REQUISITION_STOCK-Q041

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q041
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a rule spanning companies raises a requisition attributed to one company, only an approver
  with authority in that specific company can approve it, not an approver whose authority comes
  from the other company involved in the rule's configuration.
WHY_IT_MATTERS: >
  Cross-company rule configurations are exactly the kind of setup where an approval boundary is
  most likely to be accidentally widened.
DISCONFIRMING_OBSERVATION: >
  A requisition attributed to one company is approved by a user whose approval authority is granted
  only in the other company involved in the rule's cross-company configuration.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Set up a cross-company rule configuration and attempt to approve the resulting requisition using
  an account authorized in only the other company.
```

## G07-PURCHASE_REQUISITION_STOCK-Q042

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q042
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a duplicate automatic requisition is suppressed in favor of an existing open one, the fact
  that a duplicate was attempted and suppressed is recorded somewhere, rather than the second
  attempt simply vanishing with no trace it ever happened.
WHY_IT_MATTERS: >
  An unrecorded suppression makes it impossible to later confirm the duplicate-prevention mechanism
  is actually working rather than the second shortage having simply never triggered at all.
DISCONFIRMING_OBSERVATION: >
  A duplicate requisition attempt is suppressed and no record exists anywhere that a suppression
  event occurred.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Trigger a duplicate suppression scenario and search for any record that the suppression happened.
```

## G07-PURCHASE_REQUISITION_STOCK-Q043

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q043
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  If the rule that raised a requisition is later renamed, replaced, or reconfigured under the same
  identity, an already-raised requisition's traceable link continues to point to the rule
  configuration as it existed at the time it actually fired, not to whatever the rule has since
  become.
WHY_IT_MATTERS: >
  A trace that silently follows the rule's current state rather than its state at firing time
  misrepresents why a past requisition was actually raised.
DISCONFIRMING_OBSERVATION: >
  After the rule's configuration is changed, tracing back from an already-raised requisition shows
  the rule's current parameters rather than the parameters in effect when the requisition was
  actually raised.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Raise a requisition from a rule, then change the rule's configuration, and trace back from the
  requisition to see which version of the rule's parameters is shown.
```

## G07-PURCHASE_REQUISITION_STOCK-Q044

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q044
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whatever threshold, if any, exempts a low-value automatically raised requisition from human
  review does not also exempt a high-value one raised by the same rule, unless a separate, explicit
  setting says so.
WHY_IT_MATTERS: >
  A single blanket exemption that does not distinguish value would let a rule commit a large amount
  of unattended spend under a control meant only for routine, low-value replenishment.
DISCONFIRMING_OBSERVATION: >
  A high-value automatically raised requisition skips human review under the same exemption
  configured for routine low-value ones, with no separate value-based setting distinguishing the
  two.
EXPECTED_SURFACE: S3,S4,S7
PRECONDITIONS: >
  Configure a review exemption intended for routine low-value automatic requisitions, then trigger
  a high-value one from the same rule and see whether it also skips review.
```

## G07-PURCHASE_REQUISITION_STOCK-Q045

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q045
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If a person edits an automatically raised requisition, for instance adjusting the quantity,
  before approving it, the requisition's record of having originated from the rule is preserved
  rather than the human edit making it indistinguishable from one raised manually from the start.
WHY_IT_MATTERS: >
  Losing the automatic-origin fact after the first human touch would make it impossible to know how
  much of what looks like manual procurement actually started as a rule-driven suggestion.
DISCONFIRMING_OBSERVATION: >
  After a person edits an automatically raised requisition before approval, the record no longer
  shows that it originated from the rule.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Edit an automatically raised requisition's quantity before approving it, then check whether its
  rule origin is still recorded.
```

## G07-PURCHASE_REQUISITION_STOCK-Q046

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q046
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rounding excess received against one shortage becomes ordinary, visible stock on hand at its
  destination once received, available to the same shortage calculations as any other stock, rather
  than being kept invisibly separate from what the rule sees.
WHY_IT_MATTERS: >
  If the excess is invisible to the rule's own stock calculation, the rule may re-trigger for a
  shortage the excess had already covered.
DISCONFIRMING_OBSERVATION: >
  The rounding excess is received and recorded, but the rule's next evaluation still treats the
  location as short by an amount that ignores the excess already sitting there.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Receive a rounded-up quantity leaving an excess at the destination, then trigger another
  evaluation of the same rule and check whether the excess is counted.
```

## G07-PURCHASE_REQUISITION_STOCK-Q047

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q047
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  If an unrelated configuration change, such as archiving a location or a routing setting, has the
  side effect of stopping a replenishment rule from ever firing again, the rule's own status
  reflects that it is no longer effectively active, rather than still appearing enabled while never
  actually firing.
WHY_IT_MATTERS: >
  A rule that looks active in its own configuration but has been silently neutralized by something
  else gives false confidence that a location is being watched.
DISCONFIRMING_OBSERVATION: >
  A rule continues to display as enabled after an unrelated configuration change has made it
  impossible for the rule to ever fire again.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Make an unrelated configuration change that prevents a rule from ever firing, then check whether
  the rule's own displayed status reflects that.
```

## G07-PURCHASE_REQUISITION_STOCK-Q048

```yaml
QID: G07-PURCHASE_REQUISITION_STOCK-Q048
MODULE: purchase_requisition_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When two separately configured rules both cover conditions that the same shortage at the same
  location satisfies, only one requisition results, not one from each rule acting independently of
  the other's existence.
WHY_IT_MATTERS: >
  Two independently configured rules that both act on the same real-world shortage, without any
  awareness of each other, is a duplicate-ordering risk the single-rule duplicate check would not
  catch.
DISCONFIRMING_OBSERVATION: >
  A single shortage that satisfies the conditions of two separately configured rules results in two
  separate requisitions, one from each rule, existing at the same time.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure two separate rules whose conditions both cover the same location and shortage type,
  then trigger the shared condition and observe how many requisitions result.
```
