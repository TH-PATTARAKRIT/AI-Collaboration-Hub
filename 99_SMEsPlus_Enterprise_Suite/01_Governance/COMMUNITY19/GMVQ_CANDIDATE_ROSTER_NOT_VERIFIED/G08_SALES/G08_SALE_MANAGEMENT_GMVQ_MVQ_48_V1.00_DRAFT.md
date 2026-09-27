# SALE_MANAGEMENT QUESTION BANK — G08 SALES
Document ID: GMVQ-QB-G08-SALE_MANAGEMENT-V1.00
Group: G08 SALES
Module Metadata: sale_management
Wave: W2
Author Cell: P-S8
Review Cell: PENDING
Status: DRAFT / AUTHORING COMPLETE / NOT FROZEN
actual_mvq_count: 48
Purpose: Seam-only questions for the managed order lifecycle layer that sits above day-to-day
order entry — supervisory overrides, bulk administrative actions, templates and recurring
generation, and aggregate reporting. Passes the bridge test: remove either the base order concept
or the administrative/supervisory layer over it, and these questions stop making sense; they live
only where an administrator or a bulk/automated process acts on order data that an individual
salesperson would otherwise enter and manage one record at a time.
Control: Produced under GMVQ_AUTHORING_STANDARD_V1.00 and GMVQ_BRIDGE_MODULE_RULE_V1.00. Clean
Room — no vendor or reference source tree was opened for this bank; questions are authored from
generic ERP domain knowledge only. Mandatory pre-authoring sibling check performed per Bridge
Rule §5: `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G08_SALES/*.md` was run and the HYPOTHESIS lines
of the closest adjacent sibling on disk at authoring time (sales_team: the organisational
attribution, target, quota and team-visibility seam) were read in full before authoring, to keep
this bank's ground — administrative/supervisory control over an order's own lifecycle state and
content — distinct from that bank's ground, which is who an order is organisationally attributed
to. No question in this bank concerns team membership, quota, commission split, or cross-team
visibility; those are sales_team's ground, not this bank's. Not approved. Not frozen. Not
verified. Not MASTER-ready.

```yaml
QID: G08-SALE_MANAGEMENT-Q001
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A supervisory override of a confirmed order's price requires a distinct, elevated permission
  from ordinary order editing, and is recorded in the order's history as an override rather than
  an indistinguishable ordinary edit.
WHY_IT_MATTERS: >
  If a price override on a confirmed commitment requires no more than everyday edit access, the
  control meant to gate exceptional pricing decisions does not actually exist.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary order-edit permission successfully changes a confirmed order's price,
  and the resulting record shows an ordinary edit with no indication an override occurred.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  As a user with ordinary, non-elevated order-edit permission, attempt to change the price on an
  already-confirmed order and inspect what permission is required and how the change is recorded.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q002
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A supervisory override of a confirmed order's committed delivery or commitment date is
  distinguished in the order's history from an ordinary date change made before any commitment to
  the customer existed.
WHY_IT_MATTERS: >
  A committed date is a promise already made; changing it after the fact is a different kind of
  event than setting it the first time, and the record should say so.
DISCONFIRMING_OBSERVATION: >
  Changing a confirmed order's committed date produces the same history entry, with no
  distinguishing marker, as setting the date on a draft order for the first time.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order with a committed date, then change that date, and compare the resulting
  history entry to the entry created when the date was first set on the draft order.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q003
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A supervisory block placed on an order to prevent further processing is visible to the ordinary
  user who owns that order, not a silent restriction they discover only when an ordinary action
  unexpectedly fails.
WHY_IT_MATTERS: >
  An invisible block wastes the order owner's time chasing a failure with no visible cause, and
  looks to them like a system defect rather than a deliberate administrative decision.
DISCONFIRMING_OBSERVATION: >
  An order's owner attempts an ordinary action on a blocked order, the action fails, and nothing
  in the order's own view indicates that a block exists or why.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Place a supervisory block on an order, then, as that order's ordinary owner, view the order and
  attempt a normal action against it.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q004
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Removing a supervisory block from an order requires the same or higher authority as the role
  that was able to place it, rather than any ordinary user being able to clear a restriction they
  could never have imposed themselves.
WHY_IT_MATTERS: >
  A block that any ordinary user can clear is not actually a control; it only ever delays the
  outcome the block was meant to prevent.
DISCONFIRMING_OBSERVATION: >
  An ordinary user with no authority to place a supervisory block is nonetheless able to remove
  one that a supervisor placed.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As an ordinary user with no block-placing authority, attempt to remove a supervisory block that
  was placed on an order by a higher-authority role.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q005
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Bulk-locking many confirmed orders in a single administrative action records, for each
  individual order, that it was locked as part of that batch, rather than producing only a
  single batch-level log entry with no per-order trace.
WHY_IT_MATTERS: >
  Without a per-order trace, nobody can later answer "was this specific order locked, by whom,
  and as part of what action" without trusting an unverifiable batch summary.
DISCONFIRMING_OBSERVATION: >
  After a bulk-lock action affecting many orders, an individual order's own history shows no
  entry for having been locked, even though it is now locked.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Select many confirmed orders and lock them in a single bulk action, then inspect one individual
  order's own history for a record of that lock.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q006
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A bulk-lock action applied to a set of orders that includes some not yet in a lockable state
  (for example, still draft) either skips those orders with a recorded exception, or applies a
  documented rule for handling them, rather than silently forcing every selected order into a
  locked state regardless of its own readiness.
WHY_IT_MATTERS: >
  Silently locking a draft order that was never ready to be locked can freeze work still in
  progress with no warning to whoever was editing it.
DISCONFIRMING_OBSERVATION: >
  A bulk-lock action selecting both confirmed and draft orders locks the draft orders too, with
  no exception recorded and no distinguishing outcome from the confirmed ones.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Select a mixed batch of confirmed and draft orders and run a bulk-lock action, then inspect the
  resulting state of the draft orders specifically.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q007
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Bulk-unlocking a set of previously locked orders does not silently bypass whatever business
  rule required them to be locked in the first place; the rule is either re-validated on unlock
  or the bypass is explicitly and visibly recorded.
WHY_IT_MATTERS: >
  A lock exists to enforce some condition (closed period, completed invoicing); an unlock that
  quietly ignores that condition reopens exactly the risk the lock was created to prevent.
DISCONFIRMING_OBSERVATION: >
  Bulk-unlocking orders that were locked for a specific enforced reason succeeds with no
  re-validation of that reason and no visible record that the original condition was bypassed.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Lock a set of orders for a specific enforced reason, then bulk-unlock them and inspect whether
  the original condition is re-checked or the bypass is recorded.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q008
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A reporting view built for supervisors to review outstanding orders does not silently exclude
  orders that fail to meet an assumed default filter, without disclosing that an exclusion is in
  effect.
WHY_IT_MATTERS: >
  A supervisor reviewing "all outstanding orders" who is actually seeing a filtered subset, with
  no indication of the filter, can make decisions believing they have full visibility when they
  do not.
DISCONFIRMING_OBSERVATION: >
  An order that any reasonable definition of "outstanding" would include is missing from the
  supervisory report, with no visible filter or note explaining its absence.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create an order that qualifies as outstanding under an edge-case condition (e.g. an unusual
  status combination) and check whether it appears in the standard supervisory report.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q009
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two supervisors running the same "all outstanding orders" report at effectively the same time
  see the same population of orders, rather than each seeing a subtly different set with no
  indication of why they differ.
WHY_IT_MATTERS: >
  Two supervisors making decisions from what should be the same data, but silently seeing
  different populations, can reach contradictory conclusions with neither aware of the
  discrepancy.
DISCONFIRMING_OBSERVATION: >
  Two supervisors, with identical permissions, running the identical report within moments of
  each other, see different sets of orders with no data change and no explanation.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Have two supervisor accounts with identical permissions run the same outstanding-orders report
  at nearly the same time and compare the resulting order lists.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q010
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An order template used to generate new orders on a recurring schedule can itself be edited, and
  doing so is a distinct, separately recorded action from editing one specific order instance
  that template already produced.
WHY_IT_MATTERS: >
  Conflating a template edit with an instance edit risks either silently rewriting past, already-
  confirmed orders, or silently failing to apply an intended change to future ones.
DISCONFIRMING_OBSERVATION: >
  Editing the recurring template changes the content of an order it already generated and
  confirmed in the past, with no separate action having touched that specific order.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Generate an order from a recurring template, confirm it, then edit the template and check
  whether the already-confirmed order's content changed.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q011
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Orders generated automatically from a recurring template are identifiable as machine-generated,
  distinguishable from an order a person manually reviewed and confirmed.
WHY_IT_MATTERS: >
  A batch of orders nobody individually reviewed carries a different risk profile than
  individually confirmed ones; if they cannot be told apart, that risk is invisible to whoever
  later audits confirmed orders for quality.
DISCONFIRMING_OBSERVATION: >
  An automatically generated and confirmed order is indistinguishable, in every available view,
  from one a person manually reviewed and confirmed themselves.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate and auto-confirm an order from a recurring template, then compare its record to a
  manually confirmed order for any distinguishing indicator.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q012
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A recurring template with an error in its own configuration (an invalid product, a stale price)
  either fails visibly when it next generates an order, or the resulting order is clearly flagged
  as carrying that defect forward, rather than the bad configuration silently propagating into a
  seemingly normal, unflagged order.
WHY_IT_MATTERS: >
  A silently propagated configuration defect can repeat across every future cycle of the
  template, multiplying an error nobody has any reason to go looking for.
DISCONFIRMING_OBSERVATION: >
  A recurring template with a known configuration defect generates a new order carrying that
  defect with no failure, warning, or flag anywhere on the resulting order.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Introduce a known defect into a recurring template's configuration, let it generate its next
  order, and inspect the result for any failure or flag.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q013
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an administrator takes an action on an order on behalf of a salesperson (approving,
  confirming, or editing it), the record distinguishes the administrator as the actual actor
  rather than attributing the action to the salesperson as though they had performed it
  themselves.
WHY_IT_MATTERS: >
  Misattributing an administrative action to the nominal order owner erases accountability for
  who actually made the decision, and can make a salesperson answerable for a choice they never
  made.
DISCONFIRMING_OBSERVATION: >
  An action taken by an administrator "on behalf of" a salesperson is logged as having been
  performed by the salesperson, with no trace of the administrator's actual involvement.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  As an administrator, perform an action on an order on behalf of its assigned salesperson, and
  inspect the resulting audit entry for who is recorded as the actor.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q014
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A supervisory action taken on behalf of a salesperson does not, by itself, silently change who
  is recorded as the order's own owner or salesperson of record.
WHY_IT_MATTERS: >
  An administrative fill-in action is not a reassignment; if it silently rewrites ownership, a
  purely operational convenience quietly alters who is credited with and accountable for the
  order.
DISCONFIRMING_OBSERVATION: >
  An administrator performing a single action on behalf of a salesperson causes the order's own
  recorded owner or salesperson field to change to the administrator.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  As an administrator, perform a single action on an order on behalf of its salesperson and check
  whether the order's own owner field changed as a result.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q015
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A global configuration change made while orders are still open in the pipeline (a new default
  term, a changed rounding rule) is applied according to one documented rule for whether it
  affects already-open orders or only newly created ones, applied consistently rather than
  differently across the orders caught mid-flight.
WHY_IT_MATTERS: >
  Inconsistent application of a global change across orders open at the moment of the change
  produces orders that should be identical but are not, for a reason nobody configured on
  purpose.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical orders, both open at the moment a global configuration changes, end up
  with different resulting values with no documented rule explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create two similar open orders, change a global configuration value, and compare how each
  order is affected.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q016
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An order already confirmed before a global configuration change retains the configuration
  values that were in effect at the time it was confirmed, rather than being silently
  recalculated against the new configuration the next time it is viewed.
WHY_IT_MATTERS: >
  A confirmed order recalculating itself against a later configuration change silently rewrites
  a commercial commitment that was already made under different terms.
DISCONFIRMING_OBSERVATION: >
  Reopening a confirmed order after a global configuration change shows figures that have shifted
  to match the new configuration rather than the one in effect at confirmation.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Confirm an order under one global configuration, change that configuration, and reopen the
  confirmed order to check whether its figures shifted.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q017
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Permission to view every order in the system is a distinct, separately grantable permission from
  permission to act on (edit, confirm, cancel) any order, so a user can be given broad visibility
  without also being given broad editing authority.
WHY_IT_MATTERS: >
  Conflating view-all with act-on-all forces a choice between withholding oversight visibility
  and granting far more editing power than an oversight role actually needs.
DISCONFIRMING_OBSERVATION: >
  Granting a user permission to view every order in the system also grants them the ability to
  edit or confirm any of those orders, with no separate permission required.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Grant a user only the permission to view all orders, withhold any act-on-order permission
  beyond their own scope, and attempt to edit an order outside that scope.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q018
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user granted broad view permission but not broad act permission cannot reach the ability to
  modify an order outside their ordinary scope through any indirect path, such as a bulk action
  or a report-embedded control.
WHY_IT_MATTERS: >
  A permission boundary that holds on the ordinary edit screen but not on a bulk-action or
  report-embedded control is not a real boundary; it is a boundary with a known side door.
DISCONFIRMING_OBSERVATION: >
  A user without act-on-order permission beyond their own scope is able to modify an
  out-of-scope order through a bulk action or a control embedded in a view-all report.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user with view-all but not act-on-all permission, attempt to use a bulk action or a
  report-embedded control to modify an order outside your ordinary scope.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q019
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order state reachable only through an administrative override path (bypassing a normal
  check such as a credit limit or an availability check) is visibly marked as having been reached
  that way, rather than looking identical to an order that satisfied the check through the
  ordinary path.
WHY_IT_MATTERS: >
  An unmarked bypass makes it impossible to later distinguish an order that genuinely passed a
  control from one that was pushed through despite failing it, undermining the value of the
  control entirely.
DISCONFIRMING_OBSERVATION: >
  An order confirmed by bypassing a normally required check through an administrative override
  looks, in every subsequent view, identical to an order that passed that check normally.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Use an administrative override to confirm an order that fails a normally required check, then
  compare its record to an order that passed the same check normally.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q020
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The administrative override path that bypasses a normal confirmation check requires a distinct,
  elevated permission from the ordinary confirmation action, rather than being available to the
  same set of users who can confirm an order normally.
WHY_IT_MATTERS: >
  If the same users can both hit the normal check and bypass it, the check functions only as a
  suggestion, not a control, since anyone who would fail it can simply choose the other path.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary order-confirmation permission is able to invoke the override path
  that bypasses a normally required check.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user with ordinary confirmation permission only, attempt to invoke the administrative
  override path that bypasses a normally required check.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q021
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A bulk cancellation applied across many orders correctly identifies and either skips or
  distinctly flags orders that have already been partially invoiced, rather than cancelling
  already-billed lines the same way as entirely untouched ones.
WHY_IT_MATTERS: >
  Cancelling a partially invoiced order the same way as an untouched one either leaves a
  dangling, uncancelled invoice behind or silently voids billed revenue with no distinct handling.
DISCONFIRMING_OBSERVATION: >
  A bulk cancellation affecting a mix of untouched and partially invoiced orders treats both
  identically, with no distinct outcome or flag for the partially invoiced ones.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Select a batch containing both untouched and partially invoiced orders and run a bulk
  cancellation, then compare the outcomes for each category.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q022
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A bulk discount or price-list override applied across many still-open orders at once produces
  an individually auditable change per order, with the prior value recoverable for any specific
  order, rather than a single collapsed log entry giving no way to see what any one order's price
  was before the bulk change.
WHY_IT_MATTERS: >
  Without a recoverable prior value per order, a bulk pricing mistake cannot be selectively
  corrected; the only options become accepting the error or reversing the entire batch blindly.
DISCONFIRMING_OBSERVATION: >
  After a bulk price override across many orders, no individual order's history shows what its
  price was immediately before the bulk change.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Run a bulk price override across several open orders and check whether each order's own history
  retains its pre-override price.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q023
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an administrative dashboard aggregates order counts or values across the whole business,
  an order missing a required field expected by that dashboard appears in an explicit
  "unassigned" or "exception" bucket, rather than silently vanishing from every total the
  dashboard reports.
WHY_IT_MATTERS: >
  A dashboard total that silently drops incomplete records understates the true business figure
  without any indication that anything was excluded.
DISCONFIRMING_OBSERVATION: >
  An order missing a field the dashboard expects is absent from every total shown, with no
  exception bucket or count of excluded records anywhere on the dashboard.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create an order deliberately missing a field the administrative dashboard depends on and check
  whether it is reflected anywhere in the dashboard's totals.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q024
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A supervisory override that sets an order's price below a configured minimum threshold requires
  a recorded justification, distinct from an ordinary price edit that stays within normal bounds.
WHY_IT_MATTERS: >
  A below-floor price with no required justification removes the one check meant to catch
  underpricing before it becomes a pattern that erodes margin unnoticed.
DISCONFIRMING_OBSERVATION: >
  A price set below the configured minimum threshold is accepted with no prompt, requirement, or
  record of justification, identical to an ordinary in-bounds price edit.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Attempt to set an order's price below its configured minimum threshold and observe whether any
  justification is required or recorded.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q025
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reversing a supervisory override (returning an order to its pre-override value) leaves both the
  original override and its reversal visible in the order's history, rather than the reversal
  erasing the record that an override ever occurred.
WHY_IT_MATTERS: >
  Erasing the trace of an override once it is reversed removes the very evidence an auditor would
  need to see how often overrides happen and whether they are later walked back.
DISCONFIRMING_OBSERVATION: >
  Reversing a previously applied override removes the original override entry from the order's
  history rather than adding a new entry alongside it.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Apply a supervisory override to an order, then reverse it, and inspect the order's history for
  both the original override and its reversal.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q026
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Deactivating a recurring order template does not retroactively alter or cancel the orders it
  had already generated and confirmed before deactivation.
WHY_IT_MATTERS: >
  Deactivation should stop future generation, not reach backward and disturb commitments already
  made to customers under that template.
DISCONFIRMING_OBSERVATION: >
  Deactivating a recurring template changes the state or content of an order it had already
  generated and confirmed prior to the deactivation.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Confirm an order generated from a recurring template, then deactivate the template and inspect
  the already-confirmed order for any change.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q027
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A bulk edit of payment terms across many orders at once does not silently apply the new terms
  to orders that are already locked or fully invoiced under their original terms.
WHY_IT_MATTERS: >
  Silently changing payment terms on a closed, invoiced order contradicts the terms the customer
  was already billed under, creating a mismatch between the invoice and the order it came from.
DISCONFIRMING_OBSERVATION: >
  A bulk payment-terms edit changes the terms recorded on an order that is already locked or
  fully invoiced, with no exception applied to it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Include a locked, fully invoiced order in a bulk payment-terms edit and check whether its terms
  changed.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q028
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An administrative "hold" placed on an order to prevent shipment or invoicing is a state distinct
  from an ordinary cancellation; releasing the hold restores the order to its prior processable
  state rather than requiring the order to be recreated from scratch.
WHY_IT_MATTERS: >
  Conflating a temporary hold with a cancellation either destroys work that only needed a pause,
  or gives a hold the same finality as a cancellation when that was never the intent.
DISCONFIRMING_OBSERVATION: >
  Releasing a hold placed on an order does not restore it to a processable state; the order must
  instead be recreated to continue.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place a hold on an order mid-process, then release the hold and check whether the order
  resumes processing or must be recreated.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q029
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two different bulk administrative actions run concurrently over overlapping sets of orders (for
  example, one bulk-locking and another bulk-cancelling) do not leave any of the overlapping
  orders in an inconsistent combined state with no record of which action actually took effect.
WHY_IT_MATTERS: >
  A race between two administrative bulk actions is exactly the kind of failure that only appears
  under real operational load, and an inconsistent, unrecorded outcome is very hard to diagnose
  after the fact.
DISCONFIRMING_OBSERVATION: >
  Running two overlapping bulk actions at nearly the same time leaves some orders in a state that
  does not match either action's intended outcome, with no record of which action prevailed.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Run two different bulk administrative actions over an overlapping set of orders at nearly the
  same time and inspect the resulting state and history of the overlapping orders.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q030
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A supervisor's override of the exchange rate applied to an order is recorded as a deliberate
  override, distinct from and clearly marked against the rate that would otherwise have applied
  automatically.
WHY_IT_MATTERS: >
  An unmarked manual rate looks like the system's own calculation, hiding a deliberate financial
  decision inside what appears to be routine, automatic behaviour.
DISCONFIRMING_OBSERVATION: >
  An order with a manually overridden exchange rate displays and logs identically to one using
  the automatically determined rate, with no distinguishing marker.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Manually override the exchange rate on an order and compare its record to an otherwise
  identical order using the automatically determined rate.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q031
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order confirmed by bypassing a normally required check through an administrative "force
  confirm" path is flagged in a way that later reporting can specifically identify which
  confirmations bypassed which checks.
WHY_IT_MATTERS: >
  Without that identification, a pattern of repeated bypasses of the same check (a sign of a
  process problem or misuse) is invisible to anyone reviewing confirmed orders after the fact.
DISCONFIRMING_OBSERVATION: >
  There is no available report or query that can identify, after the fact, which confirmed orders
  bypassed a required check through the force-confirm path, or which check each one bypassed.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Force-confirm several orders bypassing different checks, then search for a report or query
  capable of identifying each bypass and which check it bypassed.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q032
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A permission that allows editing an order's commercial figures (price, discount) does not
  implicitly also grant permission to change the order's customer or company assignment; these
  are separately governed actions.
WHY_IT_MATTERS: >
  Reassigning an order's customer or company is a different, and often more consequential, kind
  of change than adjusting its price; bundling the two under one permission grants more authority
  than intended.
DISCONFIRMING_OBSERVATION: >
  A user granted only commercial-figure edit permission is nonetheless able to change the order's
  customer or company assignment.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Grant a user permission to edit only an order's commercial figures and attempt, as that user,
  to change the order's customer or company assignment.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q033
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where multiple administrators each individually have authority to override the same order, the
  record shows exactly which specific administrator performed a given override, rather than only
  showing that "an administrator" acted with no way to tell which one.
WHY_IT_MATTERS: >
  Shared authority without individual attribution makes it impossible to hold any one person
  accountable for a specific decision, even though several people could have made it.
DISCONFIRMING_OBSERVATION: >
  An override performed by one of several equally authorised administrators is logged only as
  "administrator," with no way to determine which specific person performed it.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  As one of several administrators with equal override authority on an order, perform an
  override and inspect whether the log identifies you specifically.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q034
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An override made to a specific order generated from a template (its price or terms) does not
  propagate back and silently alter the template's own default values for future orders.
WHY_IT_MATTERS: >
  A one-off exception silently becoming the new template default would apply an exception
  intended for a single case to every future order generated from that template.
DISCONFIRMING_OBSERVATION: >
  Overriding a value on one order generated from a template changes the value the template itself
  uses for the next order it generates.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Override a value on one order generated from a recurring template, then check whether the
  template's own default for future orders changed as a result.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q035
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A scheduled process that regenerates recurring orders on a fixed cadence records a visible
  outcome for every cycle, including a failure, rather than silently skipping a cycle with no
  record when something prevents generation.
WHY_IT_MATTERS: >
  A silently skipped generation cycle can mean a customer expecting a recurring order was never
  billed, with nothing in the record to explain why until they ask.
DISCONFIRMING_OBSERVATION: >
  A cycle in which the scheduled recurring-order generation fails to run produces no record
  anywhere indicating that the expected cycle did not occur.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Cause the scheduled recurring-generation process to fail for one cycle and check whether any
  record reflects that the cycle was skipped.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q036
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Bulk administrative actions of different kinds (lock, cancel, reassign, override) are all
  funnelled through the same auditable action-logging mechanism, rather than some kinds of bulk
  action being logged in detail while others leave no comparable trace.
WHY_IT_MATTERS: >
  Uneven logging across bulk-action types means an audit can reliably reconstruct some
  administrative history and not other parts, with no way to know in advance which is which.
DISCONFIRMING_OBSERVATION: >
  One kind of bulk administrative action produces a detailed, per-order audit trail while another
  kind of bulk action, run the same way, produces little or no comparable trace.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Run at least two different kinds of bulk administrative action over similar order sets and
  compare the resulting audit trails for completeness.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q037
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A "view all orders" report used for supervisory oversight does not itself expose editable
  controls that would let a viewer act on an order beyond what their own individual act-on
  permission would otherwise allow.
WHY_IT_MATTERS: >
  An oversight report is meant to inform, not to quietly extend editing authority; if it does,
  the view/act permission separation is defeated through the reporting surface itself.
DISCONFIRMING_OBSERVATION: >
  A user with view-all but limited act-on permission can edit an out-of-scope order directly
  through a control embedded in the view-all report.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user with broad view permission but limited act-on permission, open the view-all report
  and attempt to edit an out-of-scope order through any control it offers.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q038
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order generated from a template with a materially incomplete configuration (a missing
  required field) either fails to generate with a visible error, or generates in a clearly
  flagged incomplete state, rather than silently generating as if it were fully valid.
WHY_IT_MATTERS: >
  A silently generated, incomplete order can proceed through confirmation and invoicing carrying
  a defect nobody had any reason to look for, since nothing marked it as incomplete.
DISCONFIRMING_OBSERVATION: >
  A template missing a value it requires still generates a new order with no failure, warning, or
  flag indicating the missing configuration.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Configure a recurring template with a required field left unset and let it attempt to generate
  its next order, then inspect the result.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q039
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Locking an order to prevent ordinary edits does not also prevent an administrator holding an
  explicit override permission from making a deliberate, distinctly recorded exception when
  genuinely required.
WHY_IT_MATTERS: >
  An absolute lock with no override path at all forces a full unlock (and its own risks) for even
  a minor, legitimate correction, when a narrower, recorded exception would serve better.
DISCONFIRMING_OBSERVATION: >
  An administrator with explicit override permission has no available path to make even a single,
  recorded exception on a locked order without a full unlock.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Lock an order, then, as an administrator with override permission, attempt a single, narrow
  correction without performing a full unlock.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q040
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A supervisory block placed on a customer rather than a specific order applies to that
  customer's existing open orders according to one documented, consistent rule, rather than only
  affecting new orders going forward while existing open ones are left untouched with no notice.
WHY_IT_MATTERS: >
  A customer-level block meant to stop further exposure that silently exempts every order already
  open defeats the purpose of blocking at the customer level in the first place.
DISCONFIRMING_OBSERVATION: >
  Placing a block on a customer has no effect at all on that customer's existing open orders, with
  no documentation stating that this is the intended, deliberate behaviour.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Place a customer-level block on a customer who has existing open orders and inspect what
  happens to those orders as a result.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q041
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Removing a customer-level block does not silently and automatically release an order-level block
  that had been separately and deliberately placed on one of that customer's orders for a
  different reason.
WHY_IT_MATTERS: >
  Two blocks placed for two different reasons should be released independently; automatically
  clearing one because the other was lifted can reopen an order for a reason nobody intended to
  resolve yet.
DISCONFIRMING_OBSERVATION: >
  Removing a customer-level block also clears a separately placed, still-valid order-level block
  on one of that customer's orders.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Place both a customer-level block and a separate, distinctly reasoned order-level block on one
  of that customer's orders, then remove only the customer-level block and inspect the order.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q042
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An administrative bulk re-pricing action applied across many orders respects an order that was
  deliberately priced outside the standard list as a negotiated exception, rather than uniformly
  overwriting that negotiated price along with every standard-priced order in the same batch.
WHY_IT_MATTERS: >
  Silently overwriting a negotiated exception during routine bulk re-pricing breaks a specific
  commitment made to a specific customer, for a reason that has nothing to do with that customer.
DISCONFIRMING_OBSERVATION: >
  A bulk re-pricing action changes the price on an order that was deliberately negotiated outside
  the standard list, with no distinction from how it treats standard-priced orders.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Include an order with a deliberately negotiated, non-standard price in a batch subject to bulk
  re-pricing and inspect whether its price changed.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q043
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A supervisor's ability to reopen a fully closed, invoiced order for correction is a distinct,
  elevated action from ordinary editing, and requires a recorded reason rather than behaving like
  an unremarkable edit to any other field.
WHY_IT_MATTERS: >
  Reopening a closed financial record is a materially different event than editing an open one;
  treating it the same erases the signal that a closed record was disturbed and why.
DISCONFIRMING_OBSERVATION: >
  A fully closed, invoiced order is reopened for correction using the same action, with the same
  lack of required justification, as editing an ordinary open order.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Attempt to reopen a fully closed, invoiced order for correction and observe what permission and
  justification, if any, are required.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q044
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where the administrative layer allows merging two separate orders into one, the resulting
  merged order retains a traceable link back to both original orders, rather than one original's
  identity being silently absorbed and lost in the merge.
WHY_IT_MATTERS: >
  Losing one original order's identity in a merge breaks any later attempt to trace history,
  disputes, or commitments back to the order the customer actually placed.
DISCONFIRMING_OBSERVATION: >
  After merging two orders, the resulting order cannot be traced back to one of the two originals
  by any available means.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Merge two separate orders into one using the administrative merge action, then attempt to trace
  the result back to both original orders.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q045
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Splitting one order into several via an administrative action retains a traceable link from
  each resulting order back to the original, rather than the resulting orders appearing as if
  they had always been independent, unrelated records.
WHY_IT_MATTERS: >
  Losing the link back to the original order after a split makes it impossible to later explain
  why a customer has several smaller orders instead of the one they originally placed.
DISCONFIRMING_OBSERVATION: >
  After splitting one order into several, none of the resulting orders can be traced back to the
  original order by any available means.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Split one order into several using the administrative split action, then attempt to trace each
  resulting order back to the original.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q046
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A global default configuration value (such as a default payment term) that an administrator
  changes is timestamped or versioned, so an order confirmed under the prior default can still be
  explained by which value was actually in effect when it was confirmed.
WHY_IT_MATTERS: >
  Without a versioned history of default values, an old order's now-unexplained terms cannot be
  reconstructed once the configuration has since moved on.
DISCONFIRMING_OBSERVATION: >
  After a global default configuration value changes, there is no way to determine what the
  default value actually was at the time an older order was confirmed.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Confirm an order under one global default, change the default afterward, and attempt to
  determine what the default was at the time of the original confirmation.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q047
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An administrative report that ranks or lists orders by an aggregate figure (such as largest
  outstanding balance) recalculates from current data each time it is run, rather than silently
  displaying a stale, cached total that no longer matches the orders it claims to summarise.
WHY_IT_MATTERS: >
  A stale cached total presented as current can drive a collections or oversight decision based on
  numbers that no longer reflect what has actually happened since the cache was built.
DISCONFIRMING_OBSERVATION: >
  Re-running the aggregate report immediately after a change to an underlying order shows a total
  that does not reflect that change.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Change a value on an order feeding into an aggregate administrative report, then immediately
  re-run the report and check whether the change is reflected.
```

```yaml
QID: G08-SALE_MANAGEMENT-Q048
MODULE: sale_management
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A user granted a temporary, time-limited elevated permission (for example, an administrator
  covering for someone on leave) has actions taken during that window recorded distinctly, so a
  later audit can identify which actions were taken under the temporary grant rather than under a
  permanent role.
WHY_IT_MATTERS: >
  Without that distinction, a temporary grant's use cannot be reviewed or bounded after the fact,
  and there is no way to confirm the elevated access was not used beyond its intended, limited
  purpose.
DISCONFIRMING_OBSERVATION: >
  An action taken under a temporary, time-limited elevated permission is logged identically to one
  taken under a permanent role, with no way to identify it as having occurred under the temporary
  grant.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Grant a user a temporary, time-limited elevated permission, have them perform an action under
  it, and inspect whether the log distinguishes that action from one taken under a permanent role.
```
