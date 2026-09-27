# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_margin Module Adversarial MVQ Bank

**Document ID:** GMVQ-G08-SALE_MARGIN-MVQ48-V1.00  
**Group:** G08 SALES  
**Module Metadata:** `sale_margin`  
**Wave:** W2  
**Author Cell:** P-S3 (GMVQ Question Factory — Wave W2 Production)  
**Review Cell:** PENDING  
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN  
**actual_mvq_count:** 48  
**Standard bank reference:** 55 (shared, not reproduced here)  
**Research depth:** 55 + 48 = 103  
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded  

## Purpose

This bank authors the module-specific MVQ set for `sale_margin` — the margin figure computed on a
commercial order line where the cost is a standing attribute of the item, known before the sale and
available for display at quotation time, before any commitment exists. Per the GMVQ Bridge Module
Rule and the Five-Margin Problem in the G08 Group Brief, this bank is built around the specific
timing, revisability and authority of a PRE-KNOWN cost: what the quotation-stage figure is built
from, what happens when that standing cost moves before confirmation, which cost governs when an
item carries several, how a manual override interacts with the figure, what happens to the figure
across replacement, non-confirmation, aggregation and export. This bank deliberately does not
re-author the general cost-basis, recompute-versus-restate, or reconciliation questions already
covered for derived margin figures elsewhere in the programme; it targets only the ground specific
to a cost that is knowable before the sale is ever made.

The question text is source-neutral and does not expose vendor model names, field names, methods,
schema, XML IDs, API shapes, or implementation algorithms. `MODULE: sale_margin` appears only in
the structured metadata field, never inside question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that states a concrete failure state.
- No padding: 48 questions exist because they test 48 distinct material hypotheses.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `module + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
- Authored under the GMVQ Bridge Module Rule V1.00 Five-Margin Problem: this bank's ground is the
  standing, pre-sale cost only; siblings own the delivery-valuation, production-outcome, third-
  party-invoice and recorded-labour cost grounds.

## G08-SALE_MARGIN-Q001

```yaml
QID: G08-SALE_MARGIN-Q001
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A margin figure shown to a salesperson at quotation time, before the order exists as a commercial
  commitment, must be clearly attributable to the standing cost active at that moment.
WHY_IT_MATTERS: >
  A figure the salesperson relies on to negotiate must reflect a real, current cost, not a value
  whose origin in time cannot be established.
DISCONFIRMING_OBSERVATION: >
  Two quotations created at the same moment for the same item show different margin figures with no
  way to establish which standing cost each one actually used.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create two quotations for the same item at the same time and compare the margin shown on each.
```

## G08-SALE_MARGIN-Q002

```yaml
QID: G08-SALE_MARGIN-Q002
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the standing cost of an item changes between the moment a quotation line is created and the
  moment the order is confirmed, the confirmed order's margin figure follows a defined, disclosed
  rule for which of the two cost values it uses.
WHY_IT_MATTERS: >
  An undefined rule lets the same negotiation produce different profitability outcomes depending on
  the accident of timing, with no way to explain the difference afterward.
DISCONFIRMING_OBSERVATION: >
  The confirmed order's margin figure uses neither the cost that stood at quotation creation nor the
  cost that stood at confirmation, or the figure changes between two confirmations of otherwise
  identical quotations without a documented reason.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a quotation, change the item's standing cost, then confirm the quotation, and compare the
  order's margin to both the pre-change and post-change cost.
```

## G08-SALE_MARGIN-Q003

```yaml
QID: G08-SALE_MARGIN-Q003
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Revising an unrelated line on an open quotation does not cause an untouched line's margin to
  re-snapshot against a standing cost that has since changed.
WHY_IT_MATTERS: >
  A figure that moves without its own line being touched is unpredictable and erodes trust in every
  other figure on the same document.
DISCONFIRMING_OBSERVATION: >
  Editing quantity or price on one line changes the displayed margin of a different, untouched line
  on the same quotation after the untouched line's item cost has changed.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a two-line quotation, change one item's standing cost, edit only the other line, and check
  whether the first line's margin moved.
```

## G08-SALE_MARGIN-Q004

```yaml
QID: G08-SALE_MARGIN-Q004
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Once an order is confirmed, its margin figure remains frozen at its confirmation-time value when
  the item's standing cost changes afterward, unless an explicit recomputation is invoked.
WHY_IT_MATTERS: >
  A confirmed commercial commitment whose reported profitability silently moves after the fact
  misstates the outcome of a deal that has already been agreed.
DISCONFIRMING_OBSERVATION: >
  A confirmed order's displayed margin changes after the standing cost of its item changes, with no
  recomputation action performed or logged.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order, then change the item's standing cost, then reopen the confirmed order and
  compare its margin to the value recorded at confirmation.
```

## G08-SALE_MARGIN-Q005

```yaml
QID: G08-SALE_MARGIN-Q005
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Merely reopening a quotation for viewing, without saving any change, does not itself alter a
  previously computed margin figure even when the standing cost has moved since it was last saved.
WHY_IT_MATTERS: >
  A figure that changes on a read-only open destroys the ability to compare what was actually shown
  to the customer against what is displayed today.
DISCONFIRMING_OBSERVATION: >
  Opening a quotation without editing or saving anything produces a different margin figure than
  the one last saved for that document.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Save a quotation, change the item's standing cost, then reopen the quotation without editing or
  saving, and compare the figure shown to the one previously saved.
```

## G08-SALE_MARGIN-Q006

```yaml
QID: G08-SALE_MARGIN-Q006
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When a standing cost change is scheduled for a future effective date, a quotation's margin figure
  uses the cost that is actually in effect at the moment the figure is computed or the order is
  confirmed, not a cost that has not yet taken effect.
WHY_IT_MATTERS: >
  Using a not-yet-effective cost overstates or understates real profitability for a deal actually
  transacted under the current cost regime.
DISCONFIRMING_OBSERVATION: >
  A quotation confirmed before a scheduled cost change's effective date shows a margin computed
  against the future cost value rather than the cost standing at confirmation.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Schedule a future-dated cost change on an item, create and confirm a quotation before that date,
  and compare the order's margin to the cost that was actually in effect at confirmation.
```

## G08-SALE_MARGIN-Q007

```yaml
QID: G08-SALE_MARGIN-Q007
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the same standing-cost change is applied while several open quotations reference the same
  item, each quotation's margin figure updates independently and each converges to a value
  consistent with the same new cost, rather than some converging and others not.
WHY_IT_MATTERS: >
  Inconsistent convergence across open documents for the identical item means the same negotiation
  input produces different profitability answers depending on which document happens to be open.
DISCONFIRMING_OBSERVATION: >
  After one standing-cost change, two open quotations for the same item display margin figures
  computed against two different cost values with no pending edit to explain the difference.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Open two quotations referencing the same item, change the item's standing cost, and compare the
  margin figure each quotation displays afterward.
```

## G08-SALE_MARGIN-Q008

```yaml
QID: G08-SALE_MARGIN-Q008
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When an item carries more than one standing cost recorded for different scopes with no
  transaction yet specifying which applies, the quotation-stage margin figure discloses, or makes
  discoverable, which cost scope it actually used.
WHY_IT_MATTERS: >
  A silently chosen cost scope can materially misstate margin on items sourced through more than one
  route, with no way for the reviewer to know which route was assumed.
DISCONFIRMING_OBSERVATION: >
  A quotation's margin figure cannot be traced to a specific cost scope when the item has more than
  one standing cost recorded, and no scope is indicated anywhere on the document.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Set up an item with two standing costs under different scopes, quote it with neither scope forced
  by the transaction, and check whether the scope used is discoverable.
```

## G08-SALE_MARGIN-Q009

```yaml
QID: G08-SALE_MARGIN-Q009
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  On a multi-company sale, the margin figure uses the standing cost recorded at the company actually
  issuing the quotation, not a default or originating company's cost.
WHY_IT_MATTERS: >
  Using the wrong company's cost misstates the profitability of the entity that actually bears the
  cost and books the sale.
DISCONFIRMING_OBSERVATION: >
  A quotation issued by one company shows a margin computed against a standing cost recorded for a
  different company.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure an item with different standing costs at two companies, quote it from the company that
  is not the item's default, and check which cost the margin used.
```

## G08-SALE_MARGIN-Q010

```yaml
QID: G08-SALE_MARGIN-Q010
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a sales line's unit of measure differs from the unit the standing cost is recorded in, the
  margin figure converts consistently between the two rather than mixing quantities expressed in
  different units.
WHY_IT_MATTERS: >
  A unit mismatch silently understates or overstates margin by whatever factor separates the two
  units, without any visible error.
DISCONFIRMING_OBSERVATION: >
  A margin figure on a line sold in one unit of measure is inconsistent with the standing cost when
  both are converted to a common unit by hand.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Quote an item in a unit of measure different from the one its standing cost is recorded in, and
  independently recompute the margin in a common unit to compare.
```

## G08-SALE_MARGIN-Q011

```yaml
QID: G08-SALE_MARGIN-Q011
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When an item has both a general standing cost and a customer-specific or contract-specific cost
  that actually governs procurement for that customer, the quotation margin for that customer uses
  the cost that actually governs, not the general default.
WHY_IT_MATTERS: >
  Defaulting to a general cost the business does not actually pay for that customer misstates the
  real profitability of that specific relationship.
DISCONFIRMING_OBSERVATION: >
  A quotation to a customer with a contract-specific cost shows a margin computed against the
  general standing cost instead.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set a contract-specific cost for one customer that differs from the item's general standing cost,
  quote that customer, and compare the margin's implied cost to the contract cost.
```

## G08-SALE_MARGIN-Q012

```yaml
QID: G08-SALE_MARGIN-Q012
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a standing cost is defined at both a specific variant level and a shared template level and
  the two disagree, every sales line referencing that variant uses the variant-level figure
  consistently.
WHY_IT_MATTERS: >
  Inconsistent selection between variant and template cost across lines produces margin figures for
  the identical sold item that disagree with each other for no business reason.
DISCONFIRMING_OBSERVATION: >
  Two lines selling the identical variant on the same or different documents show margins implying
  two different cost values, one matching the variant-level cost and one matching the template-level
  cost.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Set a variant-level cost that disagrees with its template-level cost, sell the variant on two
  separate lines, and compare the implied cost behind each line's margin.
```

## G08-SALE_MARGIN-Q013

```yaml
QID: G08-SALE_MARGIN-Q013
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an item has no standing cost recorded at all, the quotation-stage margin figure is explicit
  about the missing cost rather than silently computing a number against an assumed value.
WHY_IT_MATTERS: >
  A number that looks like a real margin but rests on an assumed zero or default cost can lead a
  salesperson to underprice a deal without ever knowing the figure was meaningless.
DISCONFIRMING_OBSERVATION: >
  A quotation line for an item with no recorded standing cost displays a specific numeric margin
  figure with no indication that the underlying cost was missing.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Quote an item that has never had a standing cost recorded and inspect whether the margin field
  indicates a missing cost or shows a computed number.
```

## G08-SALE_MARGIN-Q014

```yaml
QID: G08-SALE_MARGIN-Q014
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a salesperson manually overrides the unit price on a line, the margin figure recomputes
  against the overridden price rather than continuing to reflect the price the override replaced.
WHY_IT_MATTERS: >
  A margin figure that ignores an active override shows the salesperson a profitability picture that
  does not correspond to what the customer will actually be charged.
DISCONFIRMING_OBSERVATION: >
  After a manual price override is applied to a line, the displayed margin still corresponds to the
  price that existed before the override.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Apply a manual price override to a quotation line and compare the resulting margin to what the
  original, pre-override price would have produced.
```

## G08-SALE_MARGIN-Q015

```yaml
QID: G08-SALE_MARGIN-Q015
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a manual override drops a line's margin below a configured minimum, the figure itself still
  displays the true computed value rather than the enforcement mechanism altering or suppressing the
  number instead of gating the action that produced it.
WHY_IT_MATTERS: >
  A gate that hides the number rather than blocking the action leaves the salesperson unable to see
  the very figure the policy exists to protect.
DISCONFIRMING_OBSERVATION: >
  A line priced below the configured margin floor displays a margin figure that does not match an
  independent computation from the actual override price and standing cost.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Override a price to fall below the configured margin floor and compare the displayed figure to an
  independently computed value from the same inputs.
```

## G08-SALE_MARGIN-Q016

```yaml
QID: G08-SALE_MARGIN-Q016
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a manual override is entered as a percentage discount rather than a fixed price, the order in
  which the discount and currency rounding are applied is defined and produces the same margin
  figure every time for the same inputs.
WHY_IT_MATTERS: >
  An undefined order of operations between discounting and rounding produces small, unexplained
  discrepancies that compound across many lines and periods.
DISCONFIRMING_OBSERVATION: >
  Applying the identical percentage discount to the identical line on two separate occasions
  produces two different margin figures.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Apply the same percentage discount to the same line twice, independently, and compare the two
  resulting margin figures.
```

## G08-SALE_MARGIN-Q017

```yaml
QID: G08-SALE_MARGIN-Q017
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a manual price override is removed and the line reverts to its list-derived price, the margin
  figure for that line reverts fully to the value it would have shown had the override never been
  applied.
WHY_IT_MATTERS: >
  A figure that retains drift from a removed override misrepresents a line that the salesperson
  believes has been restored to standard terms.
DISCONFIRMING_OBSERVATION: >
  After removing a manual override, the line's margin differs from the margin the same line shows
  when it has never had an override applied at all.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Apply and then remove a manual override on a line, and compare its margin to an equivalent line
  that never had an override.
```

## G08-SALE_MARGIN-Q018

```yaml
QID: G08-SALE_MARGIN-Q018
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a below-floor override requires an approval workflow, the margin figure used to trigger and
  display that workflow reflects the same standing cost that will actually appear on the confirmed
  order, not a value captured at an earlier or later moment.
WHY_IT_MATTERS: >
  An approval granted against one cost value while a different cost ends up on the confirmed order
  means the approval decision was made on a figure that was never real.
DISCONFIRMING_OBSERVATION: >
  The margin figure shown to the approver differs from the margin figure that appears on the order
  once it is actually confirmed, with the standing cost unchanged in between.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Trigger a below-floor approval workflow, record the margin shown to the approver, then confirm the
  order and compare it to the figure now shown on the confirmed order.
```

## G08-SALE_MARGIN-Q019

```yaml
QID: G08-SALE_MARGIN-Q019
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a manual override is applied to a bundled or grouped set of lines rather than to one line,
  the resulting margin change is attributed to the specific lines the override actually affected,
  not spread evenly across every line in the group regardless of what the override touched.
WHY_IT_MATTERS: >
  Even attribution across a group hides which specific items actually absorbed the discount, making
  per-item profitability unreadable.
DISCONFIRMING_OBSERVATION: >
  A group override that was applied to one line within a group changes the displayed margin of a
  different, untouched line in the same group.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Apply an override intended for one line within a grouped set of lines and check whether other
  lines in the group show a changed margin.
```

## G08-SALE_MARGIN-Q020

```yaml
QID: G08-SALE_MARGIN-Q020
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A quotation that is never confirmed, is left to lapse, or is explicitly declined does not continue
  to appear in a margin report as if it represented committed or realized business.
WHY_IT_MATTERS: >
  Business that was never won inflating a margin total misleads whoever relies on that total to make
  a resourcing or forecasting decision.
DISCONFIRMING_OBSERVATION: >
  A margin report that is supposed to reflect committed business includes the figure from a
  quotation that was never confirmed, with nothing distinguishing it from confirmed business.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a quotation, leave it unconfirmed, and check whether a margin report meant to reflect
  committed business includes its figure.
```

## G08-SALE_MARGIN-Q021

```yaml
QID: G08-SALE_MARGIN-Q021
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a quotation's validity period lapses without confirmation, its margin figure is automatically
  excluded from forward-looking margin reporting rather than persisting indefinitely as an open
  figure.
WHY_IT_MATTERS: >
  A pipeline of expired quotations that never ages out overstates the margin actually available to
  be won.
DISCONFIRMING_OBSERVATION: >
  A quotation whose validity period has visibly lapsed still contributes to a forward-looking margin
  or pipeline total with no indication of its expired status.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Let a quotation's validity period lapse without confirming it, then check a forward-looking margin
  report for its continued presence.
```

## G08-SALE_MARGIN-Q022

```yaml
QID: G08-SALE_MARGIN-Q022
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a quotation is duplicated into a second quotation and only one of the two is ever confirmed,
  an aggregate margin report does not count both as independent, uncorrelated contributions to the
  same underlying opportunity.
WHY_IT_MATTERS: >
  Counting a duplicated quotation twice inflates pipeline or forecast margin for business that only
  exists once.
DISCONFIRMING_OBSERVATION: >
  A margin or pipeline total counts the margin of a duplicated quotation and its original as two
  separate opportunities after only one of them is confirmed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Duplicate a quotation, confirm only one copy, and check whether an aggregate report counts the
  unconfirmed duplicate as separate open business.
```

## G08-SALE_MARGIN-Q023

```yaml
QID: G08-SALE_MARGIN-Q023
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a quotation is revised into a new version, the superseded version's margin figure stops being
  presented as a separate, still-open item once the revision exists.
WHY_IT_MATTERS: >
  A superseded quotation left open in reporting inflates the count and value of live opportunities
  beyond what the salesperson is actually pursuing.
DISCONFIRMING_OBSERVATION: >
  Both the original and the revised version of the same quotation appear as separate open items in
  a pipeline margin report after the revision has been made.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Revise a quotation into a new version and check whether the superseded version still appears
  separately in a pipeline report.
```

## G08-SALE_MARGIN-Q024

```yaml
QID: G08-SALE_MARGIN-Q024
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where an unconfirmed quotation's margin is treated differently from a confirmed order's margin in
  any average, forecast, or blended calculation, that distinction is disclosed to the reader of the
  resulting figure.
WHY_IT_MATTERS: >
  An undisclosed blend of provisional and committed margin produces a figure that looks like one
  thing and means another.
DISCONFIRMING_OBSERVATION: >
  A blended margin figure combines confirmed and unconfirmed quotations with no indication that the
  mix includes anything other than confirmed business.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Produce a blended or averaged margin figure spanning confirmed and unconfirmed documents and check
  whether the mix is disclosed.
```

## G08-SALE_MARGIN-Q025

```yaml
QID: G08-SALE_MARGIN-Q025
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A salesperson who is not entitled to view an item's standing cost cannot derive that cost from a
  margin figure and a price that are both visible to them on the same quotation.
WHY_IT_MATTERS: >
  A permission model that blocks cost directly but leaves margin and price both visible achieves
  nothing, since the blocked value is trivially recoverable by subtraction.
DISCONFIRMING_OBSERVATION: >
  A user without cost-viewing entitlement can see both a margin figure and the price on the same
  line, from which the cost can be directly computed.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user without cost-viewing entitlement, open a quotation and check whether both price and
  margin are visible together.
```

## G08-SALE_MARGIN-Q026

```yaml
QID: G08-SALE_MARGIN-Q026
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When margin visibility is granted for quotation purposes but cost visibility is not, a quotation
  confirmation step or a customer-facing document generated from it does not surface the underlying
  cost figure at any point.
WHY_IT_MATTERS: >
  A cost figure leaking into a downstream document defeats the purpose of restricting it at the
  point where it was supposedly controlled.
DISCONFIRMING_OBSERVATION: >
  The underlying cost value appears, visibly or in the underlying data, in a document generated from
  a quotation confirmation for a user who was never granted cost visibility.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  As a user with margin but not cost visibility, confirm a quotation and inspect the generated
  document and its underlying data for the cost value.
```

## G08-SALE_MARGIN-Q027

```yaml
QID: G08-SALE_MARGIN-Q027
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Granting a subordinate temporary permission to override price on one quotation does not
  incidentally expose the standing cost value needed to evaluate that override beyond what the
  subordinate's role otherwise allows.
WHY_IT_MATTERS: >
  A narrow, task-specific grant that quietly widens into a permanent cost-visibility grant
  undermines the whole point of scoping the permission to one task.
DISCONFIRMING_OBSERVATION: >
  After a temporary price-override grant expires or is revoked, the subordinate retains the ability
  to view the standing cost they were exposed to while the grant was active.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Grant a subordinate a temporary price-override permission, let it expire or revoke it, and check
  whether cost visibility persists.
```

## G08-SALE_MARGIN-Q028

```yaml
QID: G08-SALE_MARGIN-Q028
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When margin appears as a column in a sales-team pipeline list rather than a single quotation's
  detail view, the same cost-visibility restriction is enforced there as in the detail view, with no
  hover, tooltip, or computed value leaking the underlying cost.
WHY_IT_MATTERS: >
  A restriction that holds in one view and not another is not a restriction; it is a gap the user
  will eventually find.
DISCONFIRMING_OBSERVATION: >
  A user without cost-viewing entitlement can reveal the underlying cost through a hover, tooltip,
  or export action available from a pipeline list view that shows margin as a column.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user without cost-viewing entitlement, open a pipeline list showing margin as a column and
  probe for any interaction that surfaces the underlying cost.
```

## G08-SALE_MARGIN-Q029

```yaml
QID: G08-SALE_MARGIN-Q029
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a quotation is shared with a second salesperson as a co-owner or delegate, that person's
  cost-visibility entitlement is evaluated independently of the original owner's, rather than
  inherited alongside margin visibility.
WHY_IT_MATTERS: >
  Inheriting cost exposure through a sharing action rather than through an explicit grant lets
  entitlement spread in a way no administrator decided.
DISCONFIRMING_OBSERVATION: >
  A delegate added to a quotation gains the ability to see the underlying cost despite having no
  independent cost-viewing entitlement of their own.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Share a quotation with a delegate who lacks cost-viewing entitlement and check whether they can
  see the underlying cost through the shared document.
```

## G08-SALE_MARGIN-Q030

```yaml
QID: G08-SALE_MARGIN-Q030
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A currency or unit conversion figure displayed alongside margin at quotation time does not, by
  the arithmetic it exposes, allow a user entitled to see only price and margin to back into the
  underlying standing cost.
WHY_IT_MATTERS: >
  An incidental conversion display can reopen a channel that the direct cost field was deliberately
  closed to that user.
DISCONFIRMING_OBSERVATION: >
  A user without cost-viewing entitlement can compute the underlying cost using only the price,
  margin, and a conversion figure all visible to them on the same quotation.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user without cost-viewing entitlement, inspect a quotation with a currency or unit conversion
  shown alongside margin and attempt to derive the cost.
```

## G08-SALE_MARGIN-Q031

```yaml
QID: G08-SALE_MARGIN-Q031
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the item on a sales line is replaced with a different item, the line's margin figure updates
  to reflect the replacement item's standing cost rather than retaining the original item's figure.
WHY_IT_MATTERS: >
  A margin figure left over from a replaced item misstates the profitability of what the customer
  will actually receive.
DISCONFIRMING_OBSERVATION: >
  After replacing the item on a line, the displayed margin still corresponds to the original item's
  cost rather than the replacement's.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Replace the item on a quotation line with a different item and compare the resulting margin to
  what the replacement item's own standing cost would produce.
```

## G08-SALE_MARGIN-Q032

```yaml
QID: G08-SALE_MARGIN-Q032
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When an item on a line that already passed a margin-based approval is replaced, the replacement
  triggers a fresh evaluation of that approval against the new item's cost rather than carrying the
  original approval forward unchanged.
WHY_IT_MATTERS: >
  An approval that silently survives an item swap can authorize a deal at a margin nobody actually
  approved.
DISCONFIRMING_OBSERVATION: >
  A line whose item is replaced after a margin-based approval keeps its approved status even though
  the replacement item's margin would not itself have cleared the same approval threshold.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Obtain a margin-based approval on a line, replace its item with one whose margin would fail the
  same threshold, and check whether the approval still stands.
```

## G08-SALE_MARGIN-Q033

```yaml
QID: G08-SALE_MARGIN-Q033
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a replacement item shares the same customer-facing price as the original but carries a
  different standing cost, the resulting margin change is visible to the person who made the
  replacement.
WHY_IT_MATTERS: >
  A profitability change invisible at the moment it happens defeats the purpose of showing margin to
  the person making the substitution.
DISCONFIRMING_OBSERVATION: >
  Replacing an item with one of identical price but different cost produces no visible change to the
  line's displayed margin at the moment of replacement.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Replace an item with one of identical price and different standing cost, and check whether the
  margin change is visible immediately at the point of replacement.
```

## G08-SALE_MARGIN-Q034

```yaml
QID: G08-SALE_MARGIN-Q034
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When an item is replaced on a confirmed order that already has partial delivery or partial
  invoicing recorded against the original item, the order-level aggregate margin correctly reflects
  the replacement without double-counting or dropping the portion already fulfilled under the
  original item.
WHY_IT_MATTERS: >
  A replacement that does not reconcile against what was already fulfilled produces an aggregate
  figure that belongs to no real sequence of events.
DISCONFIRMING_OBSERVATION: >
  The order-level margin after an item replacement on a partially fulfilled line does not account
  correctly for the cost already incurred under the original item before replacement.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Partially deliver or invoice a line, replace its item, and check whether the order-level margin
  correctly separates the pre-replacement and post-replacement portions.
```

## G08-SALE_MARGIN-Q035

```yaml
QID: G08-SALE_MARGIN-Q035
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Replacing a line's item and then replacing it back to the original item returns the margin figure
  to its original value without retaining drift introduced by the round trip.
WHY_IT_MATTERS: >
  A figure that drifts after a round trip that should be a no-op signals a computation that is not
  actually idempotent, which undermines confidence in every other transition.
DISCONFIRMING_OBSERVATION: >
  After replacing an item and then replacing it back to the original, the line's margin differs from
  its value before either replacement occurred.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Replace a line's item, then replace it back to the original item, and compare the final margin to
  the value recorded before either change.
```

## G08-SALE_MARGIN-Q036

```yaml
QID: G08-SALE_MARGIN-Q036
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an item replacement is applied across many open quotations at once through a bulk operation,
  each affected line's margin change is individually traceable to that specific bulk operation.
WHY_IT_MATTERS: >
  An untraceable bulk change to profitability figures across many open deals leaves no way to audit
  or reverse the operation later.
DISCONFIRMING_OBSERVATION: >
  A line's margin changed following a bulk item-replacement operation, but no record ties that
  specific change to the operation that caused it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Run a bulk item-replacement operation across several open quotations and check whether each
  resulting margin change is traceable to that operation.
```

## G08-SALE_MARGIN-Q037

```yaml
QID: G08-SALE_MARGIN-Q037
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order-level margin figure that is positive overall does not obscure the existence of one or
  more individual lines sold at a loss; a reviewer looking only at the order-level figure has some
  way to discover a negative line exists.
WHY_IT_MATTERS: >
  A healthy-looking total that hides a loss-making line prevents the exact review the figure is
  supposed to enable.
DISCONFIRMING_OBSERVATION: >
  An order with a negative-margin line shows a positive order-level margin with no indication
  anywhere on the order-level view that a negative line exists.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Build an order containing one loss-making line among otherwise profitable lines and inspect
  whether the order-level view indicates the loss anywhere.
```

## G08-SALE_MARGIN-Q038

```yaml
QID: G08-SALE_MARGIN-Q038
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A loss-making line deliberately included to help win a larger deal can be distinguished, in some
  available report, from a loss-making line that resulted from an error.
WHY_IT_MATTERS: >
  Without any way to separate deliberate loss-leaders from mistakes, every loss line looks the same
  and none can be reviewed appropriately.
DISCONFIRMING_OBSERVATION: >
  No available report or field distinguishes a deliberately loss-led line from an accidental
  negative-margin line.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a deliberately loss-led line and check whether any available field or report distinguishes
  it from an ordinary negative-margin line.
```

## G08-SALE_MARGIN-Q039

```yaml
QID: G08-SALE_MARGIN-Q039
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When lines are grouped or subtotaled within an order, a negative-margin line's loss remains
  identifiable within its subtotal rather than being absorbed into a subtotal that reads as
  uniformly healthy.
WHY_IT_MATTERS: >
  A subtotal that hides the composition of its own lines misleads a reviewer working at the subtotal
  level, who has no reason to drill further.
DISCONFIRMING_OBSERVATION: >
  A subtotal containing a negative-margin line displays as healthy with nothing in the subtotal
  presentation indicating an underlying loss.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Group a negative-margin line into a subtotal alongside profitable lines and inspect whether the
  subtotal presentation indicates the loss.
```

## G08-SALE_MARGIN-Q040

```yaml
QID: G08-SALE_MARGIN-Q040
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order-level margin percentage computed as a weighted average across lines is presented in a way
  that does not let a small high-margin line and a large negative-margin line combine into an
  overall percentage read as acceptable while the underlying imbalance goes unseen.
WHY_IT_MATTERS: >
  A weighted average is mathematically correct and can still be practically misleading if nothing
  next to it signals the spread it is hiding.
DISCONFIRMING_OBSERVATION: >
  An order with one severely negative-margin line and one small high-margin line shows an
  acceptable weighted-average percentage with nothing indicating the underlying spread.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Construct an order with one large negative-margin line and one small high-margin line and inspect
  whether the order-level percentage indicates the underlying spread.
```

## G08-SALE_MARGIN-Q041

```yaml
QID: G08-SALE_MARGIN-Q041
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An approval workflow gated on order-level margin also catches an order containing a severely
  negative individual line even when the order's aggregate margin still clears the configured floor.
WHY_IT_MATTERS: >
  A gate that only reads the aggregate lets an approver sign off on an order the gate was built to
  catch, simply because other lines masked it.
DISCONFIRMING_OBSERVATION: >
  An order containing a severely negative-margin line passes the margin-floor approval gate without
  any flag, because the aggregate margin alone cleared the floor.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Build an order whose aggregate margin clears the approval floor but which contains one severely
  negative line, and check whether the approval gate flags it.
```

## G08-SALE_MARGIN-Q042

```yaml
QID: G08-SALE_MARGIN-Q042
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When orders are aggregated at the customer or salesperson level, a drill-down path from that
  aggregate to the specific offending line or order is actually reachable, rather than the aggregate
  being a dead end.
WHY_IT_MATTERS: >
  An aggregate with no path back to its components cannot be investigated even by someone who
  suspects something is wrong with it.
DISCONFIRMING_OBSERVATION: >
  A customer- or salesperson-level margin aggregate that includes a negative-margin order provides
  no reachable path to identify which order or line is responsible.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Include a negative-margin order within a customer- or salesperson-level aggregate and attempt to
  drill down from the aggregate to the offending order.
```

## G08-SALE_MARGIN-Q043

```yaml
QID: G08-SALE_MARGIN-Q043
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a quotation or order is exported to an external document, spreadsheet, or integration
  channel, the export excludes margin and cost figures for a recipient process or user with no
  entitlement to either.
WHY_IT_MATTERS: >
  An export is a supported path exactly like the screen the permission was designed for, and a gap
  there defeats the restriction entirely.
DISCONFIRMING_OBSERVATION: >
  An export produced for a recipient without margin or cost entitlement contains the margin or cost
  figure.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  As or for a user without margin or cost entitlement, produce an export of a quotation or order and
  inspect it for the presence of either figure.
```

## G08-SALE_MARGIN-Q044

```yaml
QID: G08-SALE_MARGIN-Q044
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A customer-facing quotation document contains no internal margin or cost figure anywhere in its
  underlying data, including a hidden field, cell, or metadata layer not rendered on the visible
  page.
WHY_IT_MATTERS: >
  A figure hidden from view but present in the file can be recovered by the recipient simply by
  inspecting the document's underlying data.
DISCONFIRMING_OBSERVATION: >
  A customer-facing quotation document's underlying data contains an internal margin or cost value
  that is not rendered on the visible page.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Generate a customer-facing quotation document and inspect its underlying data, not just its
  rendered view, for internal margin or cost values.
```

## G08-SALE_MARGIN-Q045

```yaml
QID: G08-SALE_MARGIN-Q045
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An outbound integration that exists purely for fulfillment purposes, such as a channel connector,
  does not carry margin or cost figures in its data feed despite having no legitimate need for
  either.
WHY_IT_MATTERS: >
  A fulfillment-only channel carrying profitability data multiplies the exposure of a sensitive
  figure to a party that never needed it for its stated purpose.
DISCONFIRMING_OBSERVATION: >
  A fulfillment-purpose integration's outbound data feed includes the margin or cost figure for an
  order.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Inspect the outbound data feed of a fulfillment-only integration for the presence of margin or
  cost figures.
```

## G08-SALE_MARGIN-Q046

```yaml
QID: G08-SALE_MARGIN-Q046
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A report containing margin that is scheduled for automatic distribution honors the entitlement of
  the actual recipient of that distribution, not the entitlement of the person who configured the
  schedule.
WHY_IT_MATTERS: >
  A schedule that runs under the configurer's entitlement rather than the recipient's silently
  broadcasts a restricted figure to whoever is on the distribution list.
DISCONFIRMING_OBSERVATION: >
  A recipient without margin entitlement receives a scheduled distribution containing the margin
  figure, configured by a user who does have that entitlement.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure a scheduled distribution of a margin report as an entitled user, naming a recipient who
  lacks that entitlement, and check what the recipient receives.
```

## G08-SALE_MARGIN-Q047

```yaml
QID: G08-SALE_MARGIN-Q047
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Margin data copied through a generic data-export or API mechanism not specifically designed for
  margin reporting is still subject to the same access control as the purpose-built margin report.
WHY_IT_MATTERS: >
  A generic export path is an easy, overlooked back door around a restriction that was only ever
  enforced on the purpose-built report.
DISCONFIRMING_OBSERVATION: >
  A user without margin entitlement retrieves the margin figure through a generic export or API
  mechanism that is not the purpose-built margin report.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  As a user without margin entitlement, attempt to retrieve margin data through a generic export or
  API path rather than the purpose-built report.
```

## G08-SALE_MARGIN-Q048

```yaml
QID: G08-SALE_MARGIN-Q048
MODULE: sale_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Exporting a quotation's underlying data for a purpose unrelated to margin, such as a shipping
  label or a customer acknowledgment, is logged as an event of lower sensitivity than an export that
  explicitly includes the margin or cost figure.
WHY_IT_MATTERS: >
  Treating every export as equally sensitive, or equally insensitive, in the audit trail makes it
  impossible to later tell which exports actually carried the figure that matters.
DISCONFIRMING_OBSERVATION: >
  An export that includes the margin or cost figure is logged identically, with no greater
  sensitivity marking, to an export of unrelated data such as a shipping label.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform an export that includes margin or cost and a separate export that does not, and compare
  how each is logged.
```
