# SMEsPlus ENTERPRISE SUITE
## GMVQ — G03 MASTER_DATA / partnership Module MVQ Bank

**Document ID:** GMVQ-G03-PARTNERSHIP-MVQ48-V1.00
**Group:** G03 MASTER_DATA
**Module Metadata:** `partnership`
**Wave:** W1
**Author Cell:** TEAM 16 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN / REVISED R3
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific MVQ set for `partnership` under Group G03 MASTER_DATA, targeting
the reach areas named in GROUP_BRIEF_G03_MASTER_DATA.md: a grade that drives pricing or discount and what
happens to open documents when it changes mid-flight; lapse and renewal boundaries and back-dated renewal;
whether entitlement is evaluated at document date or at posting date; downgrade after benefits were already
consumed; per-company membership of one partner; and auditability of a grade change with a financial
consequence.

The question text is source-neutral: it does not name any vendor, product, table, field, method, XML ID
or API shape, and does not name the module itself outside the MODULE field.

## Control

- Every question carries a falsifiable DISCONFIRMING_OBSERVATION that is a failure state, not a restatement.
- No padding: 48 questions exist because they test 48 distinct material hypotheses.
- Questions are not evidence. A later ANSWERED state requires an actual artifact or evidence reference.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Clean Room: authored from generic ERP domain knowledge only; no reference or vendor source tree opened.

## G03-PARTNERSHIP-Q001

```yaml
QID: G03-PARTNERSHIP-Q001
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A change to a partner's programme grade takes effect according to a defined, observable point in
  time (for example, immediately, or from the next document), and that point is consistent every time
  the grade changes.
WHY_IT_MATTERS: >
  An inconsistent or undefined effective point makes pricing and entitlement impossible to reproduce
  or explain.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical grade changes take effect at different points relative to when they were
  saved, with no explicit rule accounting for the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change a partner's grade twice under equivalent conditions and compare exactly when each change
  becomes effective for pricing purposes.
```

## G03-PARTNERSHIP-Q002

```yaml
QID: G03-PARTNERSHIP-Q002
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a partner simultaneously qualifies for more than one grade under the configured rules, there is
  a defined precedence (for example, highest benefit) rather than an arbitrary or order-dependent
  outcome.
WHY_IT_MATTERS: >
  An undefined precedence means the same partner could end up with different effective benefits
  depending on unrelated factors like processing order.
DISCONFIRMING_OBSERVATION: >
  A partner qualifying for two grades at once ends up with different effective benefits on different
  occasions with no configured precedence rule explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Construct or find a partner who satisfies the criteria for two grades at once and determine which
  benefits actually apply, then repeat to check consistency.
```

## G03-PARTNERSHIP-Q003

```yaml
QID: G03-PARTNERSHIP-Q003
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A membership that has lapsed or expired is distinguishable, in the record, from a partner who was
  never enrolled in the programme at all.
WHY_IT_MATTERS: >
  Treating "never enrolled" and "used to be enrolled" as the same state discards history that matters
  for both service and audit.
DISCONFIRMING_OBSERVATION: >
  A partner whose membership lapsed presents identically, in every visible respect, to a partner who
  was never a member.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Let a membership lapse, then compare that partner's record state to a partner who has never been
  enrolled.
```

## G03-PARTNERSHIP-Q004

```yaml
QID: G03-PARTNERSHIP-Q004
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A document already open for entry, but not yet finalized, reflects a grade change made to the
  partner while that document is still open, according to a defined rule, rather than an
  unpredictable mix of old and new terms.
WHY_IT_MATTERS: >
  If it is unclear which behavior applies, the price the customer sees can silently diverge from the
  price they end up being charged.
DISCONFIRMING_OBSERVATION: >
  A document open before a grade change and finalized after it applies pricing inconsistent with any
  stated rule for which grade should govern a document that spans the change.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Begin entering a document for a partner, change that partner's grade before finalizing, then
  finalize and inspect which grade's terms were applied.
```

## G03-PARTNERSHIP-Q005

```yaml
QID: G03-PARTNERSHIP-Q005
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A grade change made after a document has been finalized, but before it is posted, does not
  retroactively alter the pricing already recorded on that document.
WHY_IT_MATTERS: >
  Retroactively repricing a document the customer has already agreed to undermines the finality of
  finalization.
DISCONFIRMING_OBSERVATION: >
  A finalized-but-unposted document's pricing changes as a side effect of a grade change made after it
  was finalized.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Finalize a document under one grade, change the partner's grade before posting, and inspect the
  document's recorded pricing.
```

## G03-PARTNERSHIP-Q006

```yaml
QID: G03-PARTNERSHIP-Q006
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A membership activation period can be recorded with no end date at all (an open-ended
  enrolment), and the record continues to show no end date rather than the system silently
  imposing one of its own.
WHY_IT_MATTERS: >
  An invisible implicit expiry attached to what was configured as an indefinite membership
  would lapse a partner's entitlement without any change ever having been recorded against
  that membership.
DISCONFIRMING_OBSERVATION: >
  A membership is created with its end date left blank, and at some later point the partner
  is found lapsed, or the record now shows a computed end date, with no renewal, edit, or
  other explicit action recorded in between.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a membership activation period leaving the end date empty, let time pass with no
  further action taken, and inspect whether the record and the partner's entitlement still
  reflect an open-ended period.
```

## G03-PARTNERSHIP-Q007

```yaml
QID: G03-PARTNERSHIP-Q007
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A document can be traced back to the grade that was actually in effect when it was created, even
  after the partner's grade has since changed one or more times.
WHY_IT_MATTERS: >
  Without this, a later billing dispute cannot be resolved by reference to what was actually true at
  the time.
DISCONFIRMING_OBSERVATION: >
  There is no way, after a partner's grade has changed since a document was created, to determine what
  grade applied to that document at creation time.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a document under one grade, change the partner's grade at least once afterward, and attempt
  to determine the grade that applied to the original document.
```

## G03-PARTNERSHIP-Q008

```yaml
QID: G03-PARTNERSHIP-Q008
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Between a membership's stated expiry and it actually lapsing, any grace period is a configured,
  visible value rather than an undocumented default.
WHY_IT_MATTERS: >
  An invisible grace period makes it impossible for anyone to correctly predict when entitlement
  actually ends.
DISCONFIRMING_OBSERVATION: >
  A membership continues granting benefits for a period after its stated expiry with no configuration
  surface showing that a grace period exists or its length.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Let a membership reach its stated expiry date and observe whether and for how long benefits
  continue, then check whether that duration is visible in configuration.
```

## G03-PARTNERSHIP-Q009

```yaml
QID: G03-PARTNERSHIP-Q009
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  At the precise moment a membership's activation period ends, entitlement evaluated at exactly that
  boundary is treated consistently as either still active or already lapsed, not ambiguously as both
  depending on which part of the system checks it.
WHY_IT_MATTERS: >
  Ambiguity exactly at the boundary is where billing disputes and inconsistent behavior concentrate.
DISCONFIRMING_OBSERVATION: >
  One part of the system treats a membership as active at its exact expiry moment while another part
  simultaneously treats it as lapsed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Construct a case at the exact boundary of an activation period's end and check entitlement from more
  than one path that consults it.
```

## G03-PARTNERSHIP-Q010

```yaml
QID: G03-PARTNERSHIP-Q010
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Renewing a membership before it expires extends the activation period from its current expiry date,
  not from the date the renewal itself was recorded, unless a different rule is explicitly configured.
WHY_IT_MATTERS: >
  Extending from the renewal date instead of the expiry date silently shortens or lengthens what the
  customer is actually entitled to.
DISCONFIRMING_OBSERVATION: >
  An early renewal produces an effective new expiry date measured from the renewal date rather than
  the prior expiry date, with no configuration indicating that is intended.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Renew a membership well before its expiry and compare the resulting new expiry date against both
  possible reference points.
```

## G03-PARTNERSHIP-Q011

```yaml
QID: G03-PARTNERSHIP-Q011
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A renewal can be recorded with an effective date earlier than the date it was actually entered, and
  doing so is a deliberate, identifiable action rather than something that happens by default.
WHY_IT_MATTERS: >
  Back-dating capability is legitimate for correcting real-world timing but must be visible, not
  incidental.
DISCONFIRMING_OBSERVATION: >
  A renewal's effective date can be set in the past with no distinct indication, anywhere, that the
  renewal was back-dated relative to when it was recorded.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a renewal with an effective date earlier than today and inspect whether that fact is
  identifiable afterward.
```

## G03-PARTNERSHIP-Q012

```yaml
QID: G03-PARTNERSHIP-Q012
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A back-dated renewal that closes a gap between an old expiry and a new activation retroactively
  re-evaluates entitlement for any documents dated within that now-covered gap.
WHY_IT_MATTERS: >
  If it does not, a customer's back-dated renewal fails to actually restore the entitlement the
  back-dating was meant to grant for events in that window.
DISCONFIRMING_OBSERVATION: >
  Documents dated within the gap a back-dated renewal was meant to cover are not re-evaluated and
  remain priced or treated as if the gap still existed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Let a membership lapse, create a document dated within the lapse window, then record a back-dated
  renewal covering that window and check whether the document is re-evaluated.
```

## G03-PARTNERSHIP-Q013

```yaml
QID: G03-PARTNERSHIP-Q013
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a document's entry date and its posting date fall on either side of a membership boundary
  (activation, lapse, or renewal), there is a defined rule for which date governs entitlement, and it
  is applied consistently.
WHY_IT_MATTERS: >
  Without a defined and consistent rule, otherwise identical documents can receive different treatment
  purely due to processing delay.
DISCONFIRMING_OBSERVATION: >
  Two documents with the same entry date but different posting dates relative to a membership boundary
  receive different entitlement treatment with no rule explaining why, or the same document's
  entitlement outcome changes between entry and posting with no rule cited.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a document dated within an active period but post it after the membership would have lapsed,
  and determine which date the entitlement decision actually used.
```

## G03-PARTNERSHIP-Q014

```yaml
QID: G03-PARTNERSHIP-Q014
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A document dated inside an active membership period but posted after that membership has since
  lapsed is not treated identically to a document that was both dated and posted after the lapse.
WHY_IT_MATTERS: >
  Conflating the two erases a distinction the timing rule is supposed to preserve.
DISCONFIRMING_OBSERVATION: >
  The document dated within the active period but posted after lapse receives exactly the same
  treatment as one dated and posted entirely after the lapse.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Compare the treatment of a document dated-within/posted-after case against a document that is both
  dated and posted after lapse.
```

## G03-PARTNERSHIP-Q015

```yaml
QID: G03-PARTNERSHIP-Q015
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A partner can be downgraded even after they have already consumed a benefit that required the higher
  grade, and the system does not block the downgrade solely because of that prior consumption.
WHY_IT_MATTERS: >
  Blocking a legitimate downgrade because of unrelated historical consumption would make grade
  management unworkable, but the interaction must at least be a deliberate, known behavior.
DISCONFIRMING_OBSERVATION: >
  Attempting a downgrade fails or is silently blocked specifically because a higher-grade benefit was
  previously consumed, with no explanation surfaced.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have a partner consume a grade-gated benefit, then attempt to downgrade that partner and observe the
  outcome.
```

## G03-PARTNERSHIP-Q016

```yaml
QID: G03-PARTNERSHIP-Q016
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Whether a previously consumed higher-grade benefit is clawed back after a downgrade, or left
  standing, is an explicit, documented decision rather than an incidental side effect of how the
  downgrade happens to be implemented.
WHY_IT_MATTERS: >
  Silence on this point leaves a real financial question (does the customer keep what they already
  got) answered by accident rather than by policy.
DISCONFIRMING_OBSERVATION: >
  Downgrading a partner produces a claw-back or non-claw-back outcome for already-consumed benefits
  with no corresponding configuration or documented rule governing that outcome.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Downgrade a partner after they have consumed a higher-grade benefit and check whether the outcome
  traces to any explicit rule.
```

## G03-PARTNERSHIP-Q017

```yaml
QID: G03-PARTNERSHIP-Q017
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A single partner can hold an independent grade and membership status per company, when the partner
  is shared across more than one company.
WHY_IT_MATTERS: >
  Programme membership is commonly a company-specific commercial relationship, not an inherent trait
  of the partner as a legal entity.
DISCONFIRMING_OBSERVATION: >
  A partner shared across companies is forced into one single grade or membership status visible
  identically from every company.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Share a single partner record across two companies, assign different grades under each, and check
  whether both are honored independently.
```

## G03-PARTNERSHIP-Q018

```yaml
QID: G03-PARTNERSHIP-Q018
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A membership status or grade recorded for a partner under one company does not surface as that
  partner's status when viewed or transacted under an unrelated company.
WHY_IT_MATTERS: >
  Leaking a company-specific commercial status across company boundaries misrepresents the
  relationship in the other company.
DISCONFIRMING_OBSERVATION: >
  A grade or status assigned under one company is visible or applied to the same partner's
  transactions under a different, unrelated company.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Set a distinctive grade for a partner under one company, then inspect and transact with that same
  partner under a different company.
```

## G03-PARTNERSHIP-Q019

```yaml
QID: G03-PARTNERSHIP-Q019
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Every change to a partner's grade records who made the change, when, and (directly or indirectly)
  why.
WHY_IT_MATTERS: >
  A grade change has a direct financial consequence and needs the same accountability as any other
  financially consequential action.
DISCONFIRMING_OBSERVATION: >
  A grade change on a partner's record leaves no trace of who performed it or when.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Change a partner's grade and inspect the record's available history or audit surface for that
  change.
```

## G03-PARTNERSHIP-Q020

```yaml
QID: G03-PARTNERSHIP-Q020
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A reviewer can determine, for any past date, which grade was in effect for a given partner on that
  date, not just the current grade.
WHY_IT_MATTERS: >
  Investigating a past pricing dispute requires knowing the state of the world at that time, not the
  state today.
DISCONFIRMING_OBSERVATION: >
  There is no way to reconstruct which grade was in effect for a partner on a specified past date once
  the grade has since changed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change a partner's grade at least twice over time, then attempt to determine which grade was in
  effect on a date between those changes.
```

## G03-PARTNERSHIP-Q021

```yaml
QID: G03-PARTNERSHIP-Q021
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Changing the definition of what a grade entitles a partner to (its configured benefits) does not
  retroactively alter the entitlement already recorded for historical documents created under the old
  definition.
WHY_IT_MATTERS: >
  Redefining a grade's benefits going forward is normal maintenance; silently rewriting history is
  not.
DISCONFIRMING_OBSERVATION: >
  A historical document's recorded entitlement or pricing changes after the grade's benefit definition
  is edited, with no explicit re-application requested.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Record a document under a grade's current benefit definition, then change that definition, and check
  whether the historical document's recorded terms changed.
```

## G03-PARTNERSHIP-Q022

```yaml
QID: G03-PARTNERSHIP-Q022
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Changing a partner's grade, which in turn affects pricing, requires the same authorization a direct
  pricing or discount change would require; it is not reachable by a user who lacks that authority
  through an unrelated screen.
WHY_IT_MATTERS: >
  A grade field is effectively a pricing control and should not be governable by someone without
  pricing authority just because it lives on a different form.
DISCONFIRMING_OBSERVATION: >
  A user without any pricing or discount authority can change a partner's grade and thereby alter
  pricing outcomes.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Restrict a user's pricing/discount authority, then have that user attempt to change a partner's
  grade and observe whether it succeeds and what it affects.
```

## G03-PARTNERSHIP-Q023

```yaml
QID: G03-PARTNERSHIP-Q023
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A grade change either requires an approval step before taking effect, or is explicitly configured to
  take effect immediately on save; the behavior is a deliberate choice, not incidental.
WHY_IT_MATTERS: >
  Whether a financially consequential change needs a second set of eyes should be a governed decision,
  not a default nobody chose.
DISCONFIRMING_OBSERVATION: >
  A grade change takes effect immediately with no approval step, and no configuration exists to
  indicate this was a deliberate choice versus an oversight.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change a partner's grade and determine whether an approval step exists, then check whether its
  presence or absence is a configurable, documented setting.
```

## G03-PARTNERSHIP-Q024

```yaml
QID: G03-PARTNERSHIP-Q024
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A membership record left with no explicit grade assigned defaults to a defined, no-benefit baseline
  rather than an undefined or inconsistent state.
WHY_IT_MATTERS: >
  An undefined default can silently grant or deny benefits depending on unrelated implementation
  detail.
DISCONFIRMING_OBSERVATION: >
  A membership record with no grade explicitly set behaves inconsistently across different parts of
  the system (granting benefits in one place, none in another).
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a membership record without setting an explicit grade and check its treatment across more
  than one path that would consult it.
```

## G03-PARTNERSHIP-Q025

```yaml
QID: G03-PARTNERSHIP-Q025
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A partner cannot end up with two simultaneously active membership activation periods that overlap;
  the configuration or the system prevents or flags this rather than allowing an ambiguous
  double-active state.
WHY_IT_MATTERS: >
  Two overlapping active periods make "what is this partner actually entitled to right now" an
  unanswerable question.
DISCONFIRMING_OBSERVATION: >
  A partner is left with two overlapping active activation periods with no prevention, warning, or
  defined precedence between them.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to create a second activation period for a partner that overlaps an already-active one and
  observe the result.
```

## G03-PARTNERSHIP-Q026

```yaml
QID: G03-PARTNERSHIP-Q026
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Cancelling a membership mid-period has an explicit, defined effect on documents already created
  using that membership's grade; those documents are not silently altered by the cancellation.
WHY_IT_MATTERS: >
  Cancellation is a partner-level action; retroactively touching already-created documents needs to be
  a stated behavior, not a side effect.
DISCONFIRMING_OBSERVATION: >
  Cancelling a membership mid-period changes or invalidates the pricing on documents already created
  under that membership, with no rule describing that this should happen.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create documents under an active membership, cancel that membership mid-period, and inspect whether
  the existing documents changed.
```

## G03-PARTNERSHIP-Q027

```yaml
QID: G03-PARTNERSHIP-Q027
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reversing or undoing a grade change restores not only the prior grade value but also the prior
  effective and activation dates that were in place before the change.
WHY_IT_MATTERS: >
  A partial reversal that restores the grade but not its timing leaves the record in a state that
  never actually existed.
DISCONFIRMING_OBSERVATION: >
  Undoing a grade change restores the previous grade but leaves activation or effective dates at
  values that do not match any state the record was actually in before.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change a partner's grade, note the full prior state, reverse the change, and compare the restored
  state to the original in full.
```

## G03-PARTNERSHIP-Q028

```yaml
QID: G03-PARTNERSHIP-Q028
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An activation period with an end date earlier than its start date is rejected at entry rather than
  silently accepted.
WHY_IT_MATTERS: >
  Accepting an impossible period silently produces undefined downstream entitlement behavior with no
  clear cause.
DISCONFIRMING_OBSERVATION: >
  A membership activation period with an end date before its start date is saved without any
  validation error.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to save an activation period whose end date precedes its start date and observe whether it
  is accepted.
```

## G03-PARTNERSHIP-Q029

```yaml
QID: G03-PARTNERSHIP-Q029
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A membership change does not automatically create or alter an unrelated pricing or discount
  assignment elsewhere on the partner without an explicit, separately visible configuration linking
  the two.
WHY_IT_MATTERS: >
  Hidden automatic propagation between the membership feature and pricing configuration makes it
  impossible to reason about either one in isolation.
DISCONFIRMING_OBSERVATION: >
  Changing a partner's membership grade silently creates or changes a pricing or discount assignment
  that is not itself described as driven by that grade.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change a partner's grade and inspect any pricing or discount assignments on that partner for changes
  not explicitly tied to the grade.
```

## G03-PARTNERSHIP-Q030

```yaml
QID: G03-PARTNERSHIP-Q030
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Grade-driven pricing can be selectively excluded for specific document types where it should not
  apply, through configuration, rather than applying uniformly to every kind of document with no way
  to exempt one.
WHY_IT_MATTERS: >
  Not every document type a partner touches is necessarily meant to receive programme pricing, and an
  all-or-nothing rule removes legitimate control.
DISCONFIRMING_OBSERVATION: >
  There is no configuration path to exclude grade-driven pricing for a specific document type; it is
  all-or-nothing across every document type a partner can appear on.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Look for a configuration option to exclude grade-driven pricing on a specific document type and test
  whether it is honored.
```

## G03-PARTNERSHIP-Q031

```yaml
QID: G03-PARTNERSHIP-Q031
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a manual grade change and an automatic renewal-driven grade evaluation happen for the same
  partner at nearly the same time, the final grade recorded reflects a deterministic, explainable
  resolution rather than an unpredictable race outcome.
WHY_IT_MATTERS: >
  An unpredictable outcome between two legitimate triggers makes the resulting grade unexplainable
  after the fact.
DISCONFIRMING_OBSERVATION: >
  Repeating the same near-simultaneous manual change and automatic evaluation produces different final
  grades on different occasions with no explanation.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Arrange a manual grade change to occur at nearly the same time as a scheduled renewal evaluation for
  the same partner and observe the final state, repeating to check consistency.
```

## G03-PARTNERSHIP-Q032

```yaml
QID: G03-PARTNERSHIP-Q032
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a scheduled renewal and a same-day manual downgrade both apply to one partner, the order in
  which they were actually processed is determinable, and the final state matches that order rather
  than being ambiguous.
WHY_IT_MATTERS: >
  Without a determinable order, a customer complaint about their grade cannot be resolved by
  reconstructing what actually happened.
DISCONFIRMING_OBSERVATION: >
  The final grade after both events cannot be explained by any determinable processing order, or two
  attempts to reconstruct the sequence from available records disagree.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Cause a scheduled renewal and a manual downgrade to occur on the same day for one partner, then
  attempt to reconstruct the order and confirm it matches the final state.
```

## G03-PARTNERSHIP-Q033

```yaml
QID: G03-PARTNERSHIP-Q033
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A partner's grade and activation dates can only be changed through the same controlled path as a
  renewal or programme action, not by directly editing the underlying dates as if they were arbitrary
  fields.
WHY_IT_MATTERS: >
  A back-door edit path bypasses whatever rules, approvals, or history-recording the proper renewal
  workflow enforces.
DISCONFIRMING_OBSERVATION: >
  A user can change a partner's effective grade or activation dates through a generic edit path that
  bypasses the renewal/lapse workflow and its associated recording.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to change a partner's grade or activation dates through a direct field edit rather than the
  dedicated renewal or programme action, and observe whether it succeeds and whether it is recorded
  the same way.
```

## G03-PARTNERSHIP-Q034

```yaml
QID: G03-PARTNERSHIP-Q034
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The check that lapses an expired membership or activates a scheduled one runs on a scheduled
  background pass, and a delayed or skipped pass produces a visible, detectable backlog rather than a
  silent, permanent miss.
WHY_IT_MATTERS: >
  If a missed scheduled pass has no visible trace, expired memberships can keep granting benefits
  indefinitely with nobody aware.
DISCONFIRMING_OBSERVATION: >
  A delayed or skipped scheduled pass results in an expired membership continuing to grant benefits
  with no way to detect that the check was ever missed.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Identify or simulate a delay in the scheduled lapse/renewal check and observe whether the resulting
  backlog or miss is detectable afterward.
```

## G03-PARTNERSHIP-Q035

```yaml
QID: G03-PARTNERSHIP-Q035
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Any documented or configured grace period or cutover rule for lapse and renewal matches what is
  actually observed to happen at the cutover moment.
WHY_IT_MATTERS: >
  A mismatch between the stated rule and actual behavior means whoever relies on the stated rule is
  planning around a fiction.
DISCONFIRMING_OBSERVATION: >
  A membership's actual behavior at its lapse or renewal boundary differs from what its own configured
  grace-period or cutover setting states.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Note the configured grace-period or cutover rule for a membership, then observe the actual behavior
  at that boundary and compare.
```

## G03-PARTNERSHIP-Q036

```yaml
QID: G03-PARTNERSHIP-Q036
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A partner-programme grade or membership benefit configured for one tenant is never visible or
  applicable to a partner record under a different, unrelated tenant.
WHY_IT_MATTERS: >
  Programme membership is a commercial arrangement scoped to one business; leaking it across tenants
  misattributes a benefit that was never extended.
DISCONFIRMING_OBSERVATION: >
  A grade or membership benefit set up under one tenant is observed to apply to, or be visible for, a
  partner under a different tenant.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Set a distinctive grade for a partner under one tenant, then check whether that grade or its
  benefits are visible under a separate, unrelated tenant.
```

## G03-PARTNERSHIP-Q037

```yaml
QID: G03-PARTNERSHIP-Q037
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A partner can freely move down in grade over time; no hidden floor silently preserves the highest
  grade they have ever reached once they no longer qualify for it.
WHY_IT_MATTERS: >
  An undocumented "highest ever" floor would grant a benefit the current rules no longer justify, with
  nobody having decided that.
DISCONFIRMING_OBSERVATION: >
  A partner who no longer meets the criteria for a previously held higher grade continues to receive
  that higher grade's benefits with no configured floor rule explaining it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Move a partner from a higher grade to conditions that no longer qualify for it and check whether the
  higher grade's benefits persist.
```

## G03-PARTNERSHIP-Q038

```yaml
QID: G03-PARTNERSHIP-Q038
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the partner record that a membership belongs to is archived or deactivated, the membership
  itself transitions to a defined state (for example, suspended or ended) rather than remaining
  silently active in the background.
WHY_IT_MATTERS: >
  An active membership sitting behind a deactivated partner is a state nobody would have intentionally
  chosen.
DISCONFIRMING_OBSERVATION: >
  A membership remains in an active, benefit-granting state after its parent partner record has been
  archived or deactivated.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Archive or deactivate a partner who holds an active membership and inspect the membership's
  resulting state.
```

## G03-PARTNERSHIP-Q039

```yaml
QID: G03-PARTNERSHIP-Q039
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When archiving a partner ends their membership, the resulting end is recorded distinctly from an
  ordinary lapse due to expiry, so the two causes remain distinguishable later.
WHY_IT_MATTERS: >
  "Ended because archived" and "ended because time ran out" are different facts that matter for later
  review.
DISCONFIRMING_OBSERVATION: >
  A membership ended by its partner being archived is indistinguishable, in the record, from one that
  lapsed on its own schedule.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Archive a partner with an active membership, then compare the resulting membership record against
  one that lapsed naturally.
```

## G03-PARTNERSHIP-Q040

```yaml
QID: G03-PARTNERSHIP-Q040
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A grade change does not automatically re-price an open, unposted invoice that was created under the
  previous grade; re-pricing such a document requires an explicit action.
WHY_IT_MATTERS: >
  Automatically rewriting an already-issued invoice's pricing behind the scenes can silently change
  what the customer was told they owe.
DISCONFIRMING_OBSERVATION: >
  An open invoice created under a partner's previous grade shows different pricing after that
  partner's grade changes, with no explicit re-pricing action taken.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create an open invoice under a partner's current grade, change the grade, and inspect the invoice's
  pricing afterward.
```

## G03-PARTNERSHIP-Q041

```yaml
QID: G03-PARTNERSHIP-Q041
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  There is a control point, before a grade change is saved, that surfaces its pricing consequence so a
  change is not applied blind to its financial effect.
WHY_IT_MATTERS: >
  Without any surfaced consequence, a grade change that quietly reduces a customer's discount can be
  made without anyone realizing what it does.
DISCONFIRMING_OBSERVATION: >
  A grade change that measurably reduces a partner's effective discount can be saved with no
  indication anywhere of the pricing consequence.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Change a partner's grade to one with a materially lower discount and check whether any consequence
  is surfaced before or at the point of saving.
```

## G03-PARTNERSHIP-Q042

```yaml
QID: G03-PARTNERSHIP-Q042
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An activation period set entirely in the future does not make the partner currently entitled;
  entitlement only begins once the period's start date is actually reached.
WHY_IT_MATTERS: >
  Treating a future-dated period as already active would grant benefits before the business
  relationship it represents has actually begun.
DISCONFIRMING_OBSERVATION: >
  A partner with an activation period that starts in the future is already receiving that period's
  benefits before the start date arrives.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set an activation period with a future start date for a partner and check current entitlement before
  that date arrives.
```

## G03-PARTNERSHIP-Q043

```yaml
QID: G03-PARTNERSHIP-Q043
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When two partner records, each with its own membership history, are merged into one, the resulting
  record's membership history reflects a defined, explainable resolution rather than an arbitrary pick
  or a silent loss of one side's history.
WHY_IT_MATTERS: >
  Losing or arbitrarily discarding one side's membership history in a merge destroys the audit trail
  behind a financially consequential status.
DISCONFIRMING_OBSERVATION: >
  After merging two partner records that each held distinct membership histories, one side's history
  is gone with no trace and no stated rule for why that side was dropped.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Merge two partner records that each carry an independent membership history and inspect what the
  resulting record's history contains.
```

## G03-PARTNERSHIP-Q044

```yaml
QID: G03-PARTNERSHIP-Q044
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A renewal submitted exactly on the membership's expiry date is treated consistently as either before
  or after lapse, according to a defined rule, not inconsistently depending on which path processes
  it.
WHY_IT_MATTERS: >
  The exact boundary is precisely where "just in time" and "just too late" renewals collide, and
  inconsistency there directly costs or credits a customer.
DISCONFIRMING_OBSERVATION: >
  A renewal submitted on the exact expiry date is treated as timely by one part of the system and as
  late by another, with no rule reconciling the two.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Submit a renewal precisely on a membership's expiry date and check its treatment from more than one
  path that would evaluate it.
```

## G03-PARTNERSHIP-Q045

```yaml
QID: G03-PARTNERSHIP-Q045
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Changing what a grade's benefit definition consists of applies going forward to partners already
  enrolled at that grade, according to a stated rule, rather than an unstated mix of some partners
  keeping the old definition and others getting the new one.
WHY_IT_MATTERS: >
  An unstated mixed outcome means two partners at the same nominal grade could silently have different
  actual entitlements.
DISCONFIRMING_OBSERVATION: >
  After a grade's benefit definition changes, partners already enrolled at that grade end up with
  inconsistent entitlements from each other, with no rule accounting for the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change a grade's benefit definition while multiple partners are already enrolled at it, and compare
  their resulting entitlements against each other.
```

## G03-PARTNERSHIP-Q046

```yaml
QID: G03-PARTNERSHIP-Q046
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Attempting to renew a membership that was never activated in the first place is handled as a
  distinct, sensible case (for example, requiring activation first) rather than silently creating an
  ambiguous or backdated activation as a side effect of the renewal action.
WHY_IT_MATTERS: >
  Renewal and initial activation are different business events and conflating them obscures when a
  membership actually began.
DISCONFIRMING_OBSERVATION: >
  Renewing a never-activated membership silently activates it with a starting point that does not
  correspond to any explicit activation decision.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Attempt to renew a membership for a partner whose membership was never activated and observe the
  resulting state.
```

## G03-PARTNERSHIP-Q047

```yaml
QID: G03-PARTNERSHIP-Q047
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a grade change happens as a side effect of an automatic process (such as a renewal evaluation),
  the record retains what specifically triggered that change, not only the fact that the grade is now
  different.
WHY_IT_MATTERS: >
  Knowing only the end state, without the triggering event, makes it impossible to distinguish an
  automatic outcome from a manual override later.
DISCONFIRMING_OBSERVATION: >
  An automatically triggered grade change leaves only the new grade value in the record, with nothing
  indicating which event or process caused the change.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Let an automatic process (such as a scheduled renewal evaluation) change a partner's grade, then
  inspect what the record shows about the cause.
```

## G03-PARTNERSHIP-Q048

```yaml
QID: G03-PARTNERSHIP-Q048
MODULE: partnership
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a grade change generates any outward notification or follow-up task is a configurable
  behavior per tenant, not a fixed behavior that every tenant is forced to either have or lack.
WHY_IT_MATTERS: >
  Different businesses want different communication behavior around a commercial status change, and a
  fixed behavior denies that choice.
DISCONFIRMING_OBSERVATION: >
  A grade change always generates the same notification/task outcome (always one, or never one) with
  no tenant-level configuration able to change that.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Look for a tenant-level configuration governing notifications or tasks generated by a grade change,
  and test whether toggling it changes the observed behavior.
```

## CHANGE_REASON (R3)

- **QID revised:** G03-PARTNERSHIP-Q006
- **Returned by:** M3 (GMVQ Master Audit Team), DUPLICATE_OVERLAP finding against G03-PARTNERSHIP-Q040
- **Directive:** SMEPLUS-GMVQ-20P-5AUDIT-20260927-004
- **Old event tested:** a grade change silently repricing a batch of open, unposted documents
  created under the partner's prior grade (batch granularity of the same event Q040 tests at
  single-document granularity).
- **New event tested:** an open-ended (no end date) membership activation period silently
  acquiring an implicit expiry the system imposes on its own, with no explicit action recorded.
- **Disposition:** QID preserved, question rewritten in place per authoring standard section 7.
  No silent correction — recorded here per governance requirement.
