# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_expense Module Bridge MVQ Bank

**Document ID:** GMVQ-G08-SALE_EXPENSE-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_expense`
**Wave:** W2
**Author Cell:** P-S4 (GMVQ Question Factory — Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `sale_expense` — a BRIDGE per
GMVQ_BRIDGE_MODULE_RULE_V1.00, seam: a cost incurred by staff becoming a line the customer is
charged for. The underlying expense record's own lifecycle (submission, approval workflow
mechanics, reimbursement to the employee in general) belongs to the expense-tracking base family
and is deliberately NOT re-asked here; likewise the base `sale` order's own pricing, quotation and
confirmation invariants are not restated. This bank asks only what happens at the seam where an
internal cost and a customer-facing commercial document meet: whether an expense's approval state
gates its appearance on that document; who sets the re-invoicing basis (cost, markup, fixed) and
how a later policy change interacts with what was already invoiced; the exchange rate applied when
the expense's currency differs from the customer's; reclassification of billable status before and
after invoicing; prevention of the same cost being re-invoiced twice; an expense reaching an order
that is already closed or invoiced; the tax treatment on the re-invoiced line as distinct from tax
the business itself reclaimed on the original cost; what employee-identifying detail the customer
is and is not shown; and the reconciling action required when an expense is rejected after the
customer has already paid. Every question was tested against the bridge rule: if it would read
equally well with no customer-facing document in the picture at all, it was cut. Margin arithmetic
on the re-invoiced cost is deliberately excluded from this bank — that is the separate
`sale_expense_margin` bank's subject (the Five-Margin Problem, per GROUP_BRIEF_G08_SALES.md).

The question text is source-neutral and does not expose vendor or product names, field names,
methods, schema, XML IDs, API shapes, or implementation algorithms. `MODULE: sale_expense` appears
only in the structured metadata field, never inside question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` stating a concrete failure state,
  never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses at the seam
  between an incurred cost and a customer-facing charge; none was trimmed or stretched to hit count.
- Question text is source-neutral: no vendor or product name, no technical identifier (field,
  model, method, XML ID, API path); `sale_expense` appears only in the `MODULE:` field.
- BRIDGE MODULE per GMVQ_BRIDGE_MODULE_RULE_V1.00: every question fails only at the seam. None
  restates an expense-submission or approval-workflow invariant that holds with no customer-facing
  document present, and none restates a `sale` order invariant (pricing, quotation, confirmation)
  with this module's name attached.
- Margin arithmetic on the re-invoiced cost is out of scope for this bank by design — see the
  sibling `sale_expense_margin` bank.
- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G08_SALES/*.md
  2>/dev/null | sort` was run before authoring. No sibling bank existed on disk in G08_SALES at
  authoring time. Overlap against this same cell's `sale_expense_margin`, `sale_timesheet` and
  `sale_timesheet_margin` drafts was checked directly against their HYPOTHESIS text at authoring time.
- Questions are not evidence. A later ANSWERED state requires an actual artifact/evidence.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## G08-SALE_EXPENSE-Q001

```yaml
QID: G08-SALE_EXPENSE-Q001
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  An expense that has not yet been approved cannot appear as a line on a customer-facing
  commercial document, regardless of how far along that document otherwise is.
WHY_IT_MATTERS: >
  Billing a customer for a cost nobody has yet certified as legitimate removes the approval
  control's entire purpose and can commit the business to a charge it later has to unwind.
DISCONFIRMING_OBSERVATION: >
  An expense still awaiting approval is found as a line, or a line derived from it, on a
  customer-facing document at all.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Submit an expense intended for re-invoicing and attempt to draft or send a customer document
  referencing it before its approval is granted.
```

## G08-SALE_EXPENSE-Q002

```yaml
QID: G08-SALE_EXPENSE-Q002
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  If an expense's approval is reversed or rejected after it was drafted onto a customer document
  but before that document is sent, the line is removed or blocked, not left standing as if still
  approved.
WHY_IT_MATTERS: >
  A withdrawn approval that silently survives on a pending customer document charges for a cost
  the business has already decided not to stand behind.
DISCONFIRMING_OBSERVATION: >
  A rejected-after-the-fact expense's line remains present and sendable on the still-unsent
  customer document with no change and no warning.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Draft an expense line onto an unsent customer document, then reject the expense's approval, and
  inspect the draft document.
```

## G08-SALE_EXPENSE-Q003

```yaml
QID: G08-SALE_EXPENSE-Q003
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Where an expense requires more than one approval step, a partial approval does not make the
  expense eligible for re-invoicing; eligibility requires the full approval chain to complete.
WHY_IT_MATTERS: >
  Treating a partially-approved cost as billable defeats a multi-step approval control designed
  precisely for costs above a single approver's authority.
DISCONFIRMING_OBSERVATION: >
  An expense with one of two required approvals recorded is accepted as a candidate for
  re-invoicing onto a customer document.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure a two-step approval requirement, obtain only the first approval, and attempt to select
  the expense for re-invoicing.
```

## G08-SALE_EXPENSE-Q004

```yaml
QID: G08-SALE_EXPENSE-Q004
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The re-invoicing basis (at cost, at a markup, or at a fixed price) is a resolved, deliberate
  value on the specific expense line before the customer-facing amount is fixed, not silently
  defaulted to raw cost regardless of what policy is actually configured.
WHY_IT_MATTERS: >
  A silent default that ignores configured pricing policy either overcharges or undercharges the
  customer without anyone having decided that outcome.
DISCONFIRMING_OBSERVATION: >
  A markup or fixed-price policy is configured for the relevant customer or contract, yet the
  re-invoiced line is priced at raw cost with no record of the configured policy being applied.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a non-cost re-invoicing basis for a customer or contract, then re-invoice a qualifying
  expense and inspect the resulting line's amount and basis.
```

## G08-SALE_EXPENSE-Q005

```yaml
QID: G08-SALE_EXPENSE-Q005
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  The role permitted to set or override the re-invoicing basis on a specific expense line is
  distinct from the role of the employee who submitted that same expense.
WHY_IT_MATTERS: >
  Letting the person who incurred a cost also set the price the customer pays for it removes the
  segregation of duties the pricing decision depends on.
DISCONFIRMING_OBSERVATION: >
  The expense's own submitter is able to set or change the re-invoicing basis on their own
  submitted expense with no separate approval or role check.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  As the submitter of an expense, attempt to set or change its re-invoicing basis directly.
```

## G08-SALE_EXPENSE-Q006

```yaml
QID: G08-SALE_EXPENSE-Q006
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Changing the configured re-invoicing basis (for example from cost to markup) after an expense has
  already been re-invoiced does not retroactively alter the amount already committed to that
  earlier customer line.
WHY_IT_MATTERS: >
  Retroactively repricing an already-issued customer line misstates a document the customer has
  already seen or been charged against.
DISCONFIRMING_OBSERVATION: >
  Changing the configured basis after the fact changes the amount recorded on an expense line that
  was already re-invoiced under the earlier basis.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Re-invoice an expense under one configured basis, change the configuration, and inspect whether
  the earlier line's recorded amount changed.
```

## G08-SALE_EXPENSE-Q007

```yaml
QID: G08-SALE_EXPENSE-Q007
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A markup rate set specifically for a customer or contract is honored on an expense re-invoiced
  under that customer or contract even where it differs from the business's general default markup.
WHY_IT_MATTERS: >
  A specific negotiated rate silently overridden by a general default breaks a commercial
  commitment made to that customer.
DISCONFIRMING_OBSERVATION: >
  A customer-specific markup rate is configured, yet an expense re-invoiced to that customer is
  priced using the general default rate instead.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a customer-specific markup that differs from the general default, then re-invoice a
  qualifying expense to that customer and inspect which rate was actually applied.
```

## G08-SALE_EXPENSE-Q008

```yaml
QID: G08-SALE_EXPENSE-Q008
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The exchange rate applied to a re-invoiced line, when the expense's original currency differs
  from the customer's invoicing currency, follows a single defined rate policy (for example the
  expense date or the invoice date), not whichever rate happens to be current at the moment the
  line is drafted.
WHY_IT_MATTERS: >
  An undefined, moment-of-drafting rate makes the same underlying cost produce a different customer
  charge depending purely on when someone happened to click a button.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical foreign-currency expenses re-invoiced on different days, with no stated
  rate policy tying the rate to a fixed reference date, are converted at two different rates with
  no record of which policy governed either.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Record a foreign-currency expense, re-invoice it on two separate occasions under otherwise
  identical conditions, and compare the rate actually used against any stated rate policy.
```

## G08-SALE_EXPENSE-Q009

```yaml
QID: G08-SALE_EXPENSE-Q009
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When an expense's currency differs from both the employee's home currency and the customer's
  invoicing currency, the conversion path used to reach the customer line is a single defined path,
  not an undocumented double conversion whose rounding could materially change the result.
WHY_IT_MATTERS: >
  An undocumented double conversion can compound rounding into a customer charge that no one
  configured or intended.
DISCONFIRMING_OBSERVATION: >
  A three-currency case produces a customer-line amount that cannot be reproduced from any single,
  stated conversion path, and no record shows which path was actually used.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record and re-invoice an expense where the expense currency, the employee's home currency, and
  the customer's invoicing currency are all different, and attempt to reproduce the resulting
  amount from a stated conversion path.
```

## G08-SALE_EXPENSE-Q010

```yaml
QID: G08-SALE_EXPENSE-Q010
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A currency rate correction recorded after the expense was captured, but before it is re-invoiced,
  is either picked up or deliberately frozen according to a stated policy, consistently across
  expenses, not resolved ad hoc case by case.
WHY_IT_MATTERS: >
  An ad hoc answer to a rate correction means two otherwise identical expenses can be billed at two
  different amounts for no reason a reviewer can point to.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical expenses, each affected by a rate correction before re-invoicing, are
  handled differently from each other with no stated policy explaining why.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Trigger a currency rate correction between expense capture and re-invoicing for two comparable
  expenses and compare how each was actually handled.
```

## G08-SALE_EXPENSE-Q011

```yaml
QID: G08-SALE_EXPENSE-Q011
MODULE: sale_expense
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  An expense's reimbursement status to the person who incurred it and its billing status toward a
  customer are tracked independently, so changing one does not silently force a change in the
  other.
WHY_IT_MATTERS: >
  If the two statuses were coupled, an employee could be blocked from reimbursement pending a
  customer billing decision, or a business could reimburse a cost while believing it was still
  awaiting a billing decision, with neither outcome visibly decided by anyone.
DISCONFIRMING_OBSERVATION: >
  Changing an expense's billing status toward a customer changes its reimbursement status to the
  submitting employee, or changing its reimbursement status changes its billing status, when
  neither change was directly requested.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Submit an expense, then independently change its billing status and its reimbursement status in
  either order, and check whether changing one causes an unrequested change in the other.
```

## G08-SALE_EXPENSE-Q012

```yaml
QID: G08-SALE_EXPENSE-Q012
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Reclassifying an expense's billable status before it has been re-invoiced changes only its
  eligibility for future re-invoicing, without needing any correcting record, since nothing has
  been charged to a customer yet.
WHY_IT_MATTERS: >
  Generating an unnecessary correcting record for a change that has no customer-facing consequence
  yet would clutter the audit trail with noise that obscures the corrections that do matter.
DISCONFIRMING_OBSERVATION: >
  Reclassifying a not-yet-invoiced expense's billable status is blocked, or generates a
  customer-facing correcting document where none was ever issued.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reclassify an expense's billable status before it has ever been re-invoiced to any customer.
```

## G08-SALE_EXPENSE-Q013

```yaml
QID: G08-SALE_EXPENSE-Q013
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  An expense that has already been attached to one customer-facing line cannot be selected again
  to produce a second, independent customer-facing line for the same cost.
WHY_IT_MATTERS: >
  Charging a customer twice for the same underlying cost is an overcharge that damages trust and
  may have to be refunded once discovered.
DISCONFIRMING_OBSERVATION: >
  The same expense is selected and successfully re-invoiced a second time, producing two
  independent customer-facing lines for the same underlying cost.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Re-invoice an expense once, then attempt to select the same expense for re-invoicing again on
  the same or a different order.
```

## G08-SALE_EXPENSE-Q014

```yaml
QID: G08-SALE_EXPENSE-Q014
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If the expense report containing an already re-invoiced expense is reset, cancelled, or
  recreated, the underlying cost still cannot be re-invoiced a second time.
WHY_IT_MATTERS: >
  A reset that clears the "already billed" marker without clearing the customer line already
  issued reopens the same double-charge risk through an indirect path.
DISCONFIRMING_OBSERVATION: >
  Resetting or recreating the expense report makes the same underlying cost selectable for
  re-invoicing again despite a customer line already existing for it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Re-invoice an expense, then reset or recreate the expense report it belongs to, and attempt to
  re-invoice the same cost again.
```

## G08-SALE_EXPENSE-Q015

```yaml
QID: G08-SALE_EXPENSE-Q015
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where an expense can be split for billing across more than one customer or order, the sum billed
  across all the splits never exceeds the original expense's full amount.
WHY_IT_MATTERS: >
  A splitting mechanism that does not track the remaining unbilled balance can double-count part
  of a cost across two customers.
DISCONFIRMING_OBSERVATION: >
  Splitting one expense across two customer lines results in the two lines together exceeding the
  original expense's total amount.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split a single expense's amount across two separate customer-facing lines and sum the two
  resulting amounts against the original.
```

## G08-SALE_EXPENSE-Q016

```yaml
QID: G08-SALE_EXPENSE-Q016
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Attaching a new expense to an order that is already fully invoiced or locked is either blocked
  outright or routed through an explicit supplementary path, never silently absorbed as if the
  order were still open.
WHY_IT_MATTERS: >
  Silently reopening a closed commercial document to add a charge bypasses whatever control closed
  it in the first place and can misstate a period already reported as final.
DISCONFIRMING_OBSERVATION: >
  A new expense is attached and billed against an order already marked fully invoiced or locked
  with no distinguishable supplementary document and no blocking step.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Fully invoice and lock an order, then attempt to attach and re-invoice a new expense against it.
```

## G08-SALE_EXPENSE-Q017

```yaml
QID: G08-SALE_EXPENSE-Q017
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An order that has been invoiced but is not yet closed still permits an additional expense to be
  appended only through a defined, auditable path (for example a supplementary invoice), not by
  editing the amount already invoiced.
WHY_IT_MATTERS: >
  Editing an amount already sent to a customer rather than issuing a supplementary line makes the
  original invoice document an unreliable record of what was actually communicated.
DISCONFIRMING_OBSERVATION: >
  Appending an expense to an invoiced-but-open order changes the amount on the already-issued
  invoice document rather than producing a separate, additional line or document.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Invoice an order without closing it, then append a new re-invoiceable expense and inspect
  whether the original invoice document itself changed.
```

## G08-SALE_EXPENSE-Q018

```yaml
QID: G08-SALE_EXPENSE-Q018
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  The tax applied to a re-invoiced cost line follows the tax rules governing the sale to the
  customer, not the tax treatment that was used when the business itself recorded or reclaimed tax
  on the original expense.
WHY_IT_MATTERS: >
  Carrying the wrong tax treatment onto the customer line either under- or over-charges tax the
  business is legally required to account for correctly.
DISCONFIRMING_OBSERVATION: >
  A re-invoiced line's tax is found to be a direct copy of the original expense's own recorded tax
  treatment rather than the tax determined by the sale itself.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Record an expense with one tax treatment, re-invoice it to a customer whose sale carries a
  different tax rule, and inspect which tax treatment the customer line actually received.
```

## G08-SALE_EXPENSE-Q019

```yaml
QID: G08-SALE_EXPENSE-Q019
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Where the business reclaimed input tax on the original expense, that reclaim is tracked
  independently of whatever output tax is charged to the customer on the re-invoiced line — the two
  are not conflated into a single figure.
WHY_IT_MATTERS: >
  Conflating input tax reclaimed by the business with output tax charged to the customer can
  understate or duplicate a tax liability the business owes to the authorities.
DISCONFIRMING_OBSERVATION: >
  The output tax recorded on the re-invoiced customer line is found to net against, or otherwise
  merge with, the input tax the business separately reclaimed on the original expense.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Record an expense on which input tax is reclaimed, re-invoice it with output tax charged to the
  customer, and inspect whether the two tax records remain independently traceable.
```

## G08-SALE_EXPENSE-Q020

```yaml
QID: G08-SALE_EXPENSE-Q020
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Where the jurisdiction of the original expense and the jurisdiction of the customer being billed
  differ, the tax applied to the re-invoiced line is a deliberate resolution of that difference, not
  a default carried over from whichever tax code the expense happened to be recorded under.
WHY_IT_MATTERS: >
  An undeliberate default across a jurisdiction boundary can apply a tax treatment neither
  jurisdiction's rules actually call for.
DISCONFIRMING_OBSERVATION: >
  A cross-jurisdiction re-invoice carries the expense's original jurisdiction tax code with no
  record of a deliberate resolution for the customer's own jurisdiction.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record an expense in one tax jurisdiction and re-invoice it to a customer in a different
  jurisdiction, then inspect how the resulting tax treatment was determined.
```

## G08-SALE_EXPENSE-Q021

```yaml
QID: G08-SALE_EXPENSE-Q021
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  The customer-facing document exposes only the commercially relevant description and amount for a
  re-invoiced cost, never employee-identifying detail such as the submitter's name, personal
  payment instrument, or merchant-level receipt detail, by default.
WHY_IT_MATTERS: >
  Exposing an employee's personal spending detail to a customer is a privacy exposure the employee
  never consented to and the business did not intend.
DISCONFIRMING_OBSERVATION: >
  A customer-facing document generated by default shows the submitting employee's name, personal
  payment detail, or merchant-level receipt detail alongside the re-invoiced line.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Re-invoice an expense to a customer using default settings and inspect exactly what detail
  appears on the resulting customer-facing document.
```

## G08-SALE_EXPENSE-Q022

```yaml
QID: G08-SALE_EXPENSE-Q022
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Attaching the original receipt or proof-of-spend to a customer-facing communication is a
  distinct, explicit action taken by a person, not an automatic side effect of the re-invoicing
  action itself.
WHY_IT_MATTERS: >
  An automatic attachment removes the one checkpoint where a person could catch and stop
  sensitive receipt detail from reaching a customer.
DISCONFIRMING_OBSERVATION: >
  Re-invoicing an expense automatically attaches its original receipt image or file to the
  customer-facing communication with no separate action or confirmation.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Re-invoice an expense that has an attached receipt and observe whether the receipt is
  automatically included in what reaches the customer.
```

## G08-SALE_EXPENSE-Q023

```yaml
QID: G08-SALE_EXPENSE-Q023
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Where several employees' expenses are consolidated onto one customer-facing line, that line does
  not individually identify which employee incurred which portion of the total.
WHY_IT_MATTERS: >
  A consolidated line that still exposes per-employee detail defeats the purpose of consolidating
  and leaks the same personal detail Q021 requires be withheld.
DISCONFIRMING_OBSERVATION: >
  A consolidated customer line, or its supporting detail reachable by the customer, breaks the
  total down by which specific employee incurred which amount.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Consolidate expenses from two different employees onto a single customer-facing line and inspect
  whether the customer can see the per-employee breakdown.
```

## G08-SALE_EXPENSE-Q024

```yaml
QID: G08-SALE_EXPENSE-Q024
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  An expense rejected (for example as fraudulent or policy-violating) after the customer has
  already paid the re-invoiced amount produces an explicit reconciling action — credit, write-off,
  or flag — rather than leaving the paid line standing with no link to the rejection.
WHY_IT_MATTERS: >
  A paid line left standing after its underlying cost is invalidated means the business either
  keeps money it has no legitimate basis for or never notices the discrepancy at all.
DISCONFIRMING_OBSERVATION: >
  An expense is rejected after its re-invoiced line was already paid by the customer, and no
  credit, write-off, or flag is generated linking the two.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Have a customer pay a re-invoiced line in full, then reject the underlying expense, and inspect
  what reconciling record, if any, is produced.
```

## G08-SALE_EXPENSE-Q025

```yaml
QID: G08-SALE_EXPENSE-Q025
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Rejecting the underlying expense after its line has already been invoiced to the customer does
  not retroactively alter the already-issued invoice document itself.
WHY_IT_MATTERS: >
  A document already issued to a customer must remain a stable record of what was actually
  communicated, even when the cost behind one of its lines is later invalidated.
DISCONFIRMING_OBSERVATION: >
  Rejecting an expense after its line was already invoiced changes the content of the
  already-issued invoice document rather than producing a separate correcting record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Invoice a re-invoiced expense line to a customer, then reject the underlying expense, and inspect
  the already-issued invoice for any change.
```

## G08-SALE_EXPENSE-Q026

```yaml
QID: G08-SALE_EXPENSE-Q026
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a customer order after an expense has been re-invoiced onto it, but before the order
  is fully closed, produces an explicit, visible reversal of the link between the expense and the
  now-cancelled line, rather than leaving it dangling.
WHY_IT_MATTERS: >
  A dangling link leaves an expense marked as billed against a commercial document that no longer
  exists, making the cost's true billing status unrecoverable without manual investigation.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order with a re-invoiced expense on it leaves that expense marked as billed with no
  visible indication that the order it was billed against was cancelled.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Re-invoice an expense onto an order, cancel the order before it closes, and inspect the
  expense's recorded billing status.
```

## G08-SALE_EXPENSE-Q027

```yaml
QID: G08-SALE_EXPENSE-Q027
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Crediting a re-invoiced expense line through a credit note returns the underlying expense to a
  billable-again state through one controlled, singular transition, not left permanently "used up"
  nor made freely re-billable with no record of the credit.
WHY_IT_MATTERS: >
  Permanently locking a credited cost out of re-billing loses a legitimate charge; leaving it
  freely re-billable with no memory of the credit risks the double-billing Q013 prohibits.
DISCONFIRMING_OBSERVATION: >
  After a credit note reverses a re-invoiced expense line, the expense is either permanently
  unable to be re-invoiced, or becomes billable again with no trace of the prior credit.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Re-invoice an expense, issue a credit note against that line, and attempt to re-invoice the same
  expense again while inspecting its recorded history.
```

## G08-SALE_EXPENSE-Q028

```yaml
QID: G08-SALE_EXPENSE-Q028
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  An expense marked explicitly as non-billable at submission time never appears as a candidate for
  re-invoicing under any configuration.
WHY_IT_MATTERS: >
  A non-billable marking that can be bypassed by any configuration path removes the one signal an
  employee has to keep a personal or ineligible cost off a customer's bill.
DISCONFIRMING_OBSERVATION: >
  An expense submitted and marked non-billable appears as a selectable candidate for re-invoicing
  under some configuration or workflow path.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Submit an expense explicitly marked non-billable and attempt, under every re-invoicing entry
  point available, to select it for billing.
```

## G08-SALE_EXPENSE-Q029

```yaml
QID: G08-SALE_EXPENSE-Q029
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  An expense's cost-center or department scoping does not, by itself, determine which customer
  order it can be re-invoiced to — the target customer or order is a separate, deliberate selection.
WHY_IT_MATTERS: >
  Inferring a billing target from organisational scoping alone could route a cost to a customer
  order with no genuine relationship to that cost.
DISCONFIRMING_OBSERVATION: >
  An expense is re-invoiced to a customer order automatically selected on the basis of matching
  cost-center or department, with no separate deliberate selection step.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit an expense scoped to a given cost-center that also has an unrelated customer order sharing
  the same scoping, and inspect how (or whether) a billing target is selected.
```

## G08-SALE_EXPENSE-Q030

```yaml
QID: G08-SALE_EXPENSE-Q030
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where re-invoicing can happen automatically rather than through manual selection, an
  automatically re-invoiced expense is still subject to the same approval-before-appearance gate
  described in Q001 — automation is not an exemption from that gate.
WHY_IT_MATTERS: >
  An automated path that skips the approval gate would let an unapproved cost reach a customer
  faster and with less oversight than the manual path ever could.
DISCONFIRMING_OBSERVATION: >
  An automatic re-invoicing process bills an expense to a customer that has not completed its
  required approval.
EXPECTED_SURFACE: S1,S4,S8
PRECONDITIONS: >
  Configure automatic re-invoicing, submit an expense that has not been approved, and observe
  whether the automated process bills it regardless.
```

## G08-SALE_EXPENSE-Q031

```yaml
QID: G08-SALE_EXPENSE-Q031
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A re-invoiced expense line retains a durable, queryable link back to its originating expense
  record even after the order and invoice it appears on are fully processed and archived.
WHY_IT_MATTERS: >
  Losing that link once documents are archived makes it impossible to later audit what an
  archived customer charge was actually for.
DISCONFIRMING_OBSERVATION: >
  Once the order and invoice are archived, the re-invoiced line's link back to its originating
  expense record can no longer be resolved.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Re-invoice an expense to completion, archive the resulting order and invoice, and attempt to
  trace the line back to its originating expense.
```

## G08-SALE_EXPENSE-Q032

```yaml
QID: G08-SALE_EXPENSE-Q032
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  In a multi-company setup, an expense recorded under one company cannot be re-invoiced onto a
  customer order belonging to a different company without going through an explicit intercompany
  mechanism.
WHY_IT_MATTERS: >
  Crossing a company boundary without an explicit mechanism corrupts each company's own financial
  records and defeats the separation the multi-company structure exists to guarantee.
DISCONFIRMING_OBSERVATION: >
  An expense recorded under one company is successfully re-invoiced directly onto another
  company's customer order with no intercompany record created.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  In a multi-company configuration, attempt to re-invoice an expense recorded under one company
  onto a customer order belonging to a different company.
```

## G08-SALE_EXPENSE-Q033

```yaml
QID: G08-SALE_EXPENSE-Q033
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two people re-invoicing overlapping sets of expenses onto the same order at close to the same
  time cannot both succeed in attaching the same expense line to that order.
WHY_IT_MATTERS: >
  A race condition here reproduces the same double-billing failure as Q013 through concurrency
  rather than through a workflow gap.
DISCONFIRMING_OBSERVATION: >
  Two concurrent re-invoicing actions on overlapping expense sets both succeed in attaching the
  same underlying expense to the order.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Have two people simultaneously attempt to re-invoice an overlapping set of expenses, including at
  least one shared expense, onto the same order.
```

## G08-SALE_EXPENSE-Q034

```yaml
QID: G08-SALE_EXPENSE-Q034
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  The path from an approved, billable expense to an actual invoiced customer line is reachable
  under normal configuration without requiring a manual workaround such as a hand-entered
  accounting adjustment.
WHY_IT_MATTERS: >
  A capability that only works through a manual workaround is not a reliable seam; it means the
  intended path is broken or was never actually completed.
DISCONFIRMING_OBSERVATION: >
  Under default, unmodified configuration, an approved billable expense cannot be turned into an
  invoiced customer line without a manual accounting workaround outside the normal re-invoicing
  action.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Under default configuration, approve a billable expense and attempt to reach an invoiced customer
  line for it using only the normal re-invoicing action.
```

## G08-SALE_EXPENSE-Q035

```yaml
QID: G08-SALE_EXPENSE-Q035
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A business that has never configured a markup or fixed-price policy still re-invoices at a
  defined, documented default (for example cost) rather than reaching an undefined or blocking
  state.
WHY_IT_MATTERS: >
  An undefined state on first use, with no configuration ever touched, would make the seam
  unusable out of the box for the majority of businesses that never customize pricing policy.
DISCONFIRMING_OBSERVATION: >
  With no re-invoicing basis ever configured, attempting to re-invoice a qualifying expense either
  fails outright or produces an amount that cannot be traced to any documented default.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  With no re-invoicing basis configuration ever touched, re-invoice a qualifying expense and
  inspect the resulting amount and basis.
```

## G08-SALE_EXPENSE-Q036

```yaml
QID: G08-SALE_EXPENSE-Q036
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The currency conversion recorded against a re-invoiced line matches the conversion the resulting
  accounting or tax record shows for that same line — the two do not independently compute or
  display different converted values for the same event.
WHY_IT_MATTERS: >
  Two different converted values for what is supposed to be one event makes it impossible to know
  which figure is actually correct, and undermines both the commercial and the accounting record.
DISCONFIRMING_OBSERVATION: >
  The converted amount shown on the customer-facing line and the converted amount shown on its
  corresponding accounting or tax record disagree for the same underlying expense.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Re-invoice a foreign-currency expense and compare the converted amount on the customer line
  against the converted amount on its accounting or tax record.
```

## G08-SALE_EXPENSE-Q037

```yaml
QID: G08-SALE_EXPENSE-Q037
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Attempting to re-invoice an expense whose original currency has no defined conversion path to the
  customer's invoicing currency produces an explicit blocking exception, not a fallback to an
  arbitrary or last-known rate.
WHY_IT_MATTERS: >
  A silent arbitrary fallback can produce a customer charge based on a rate nobody chose or can
  reproduce later.
DISCONFIRMING_OBSERVATION: >
  An expense in a currency with no defined conversion path to the customer's currency is
  re-invoiced anyway, using a rate that cannot be traced to any configured source.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record an expense in a currency for which no conversion path to the customer's invoicing
  currency is configured, and attempt to re-invoice it.
```

## G08-SALE_EXPENSE-Q038

```yaml
QID: G08-SALE_EXPENSE-Q038
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  An expense fully reimbursed to the employee as a purely internal, non-billable cost is thereby
  removed from the pool of candidates for re-invoicing — billing and pure reimbursement are
  mutually exclusive outcomes for the same expense.
WHY_IT_MATTERS: >
  Allowing both outcomes for the same expense risks either double-recovering the cost (from the
  customer and by treating it as unreimbursed internally) or losing track of which treatment
  actually applies.
DISCONFIRMING_OBSERVATION: >
  An expense already processed as a purely internal reimbursement is still selectable as a
  candidate for re-invoicing to a customer.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Process an expense as a purely internal, non-billable reimbursement, then attempt to select it
  for customer re-invoicing.
```

## G08-SALE_EXPENSE-Q039

```yaml
QID: G08-SALE_EXPENSE-Q039
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Editing an expense's amount after it has already been re-invoiced, where the underlying expense
  record itself remains editable, does not silently change the amount already committed to the
  customer-facing line.
WHY_IT_MATTERS: >
  A customer line that changes underneath an already-issued or already-viewed document without any
  visible action misstates what was actually communicated to the customer.
DISCONFIRMING_OBSERVATION: >
  Editing an already re-invoiced expense's amount changes the amount on the customer-facing line it
  was already used to produce, with no separate correcting action.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Re-invoice an expense, then edit that same expense's recorded amount, and inspect whether the
  already-produced customer line changed.
```

## G08-SALE_EXPENSE-Q040

```yaml
QID: G08-SALE_EXPENSE-Q040
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  When an expense's approval is granted by a delegate acting for an absent approver, the approval
  record behind the resulting re-invoiceable expense preserves the delegate's own identity,
  distinct from the approver whose authority was delegated.
WHY_IT_MATTERS: >
  Attributing a delegate's approval to the absent approver corrupts the accountability trail
  behind a customer-facing charge and makes review of who actually approved it unreliable.
DISCONFIRMING_OBSERVATION: >
  An expense approved by a delegate is recorded, on the resulting re-invoiceable expense, as
  approved by the absent approver rather than by the delegate who actually acted.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Configure an approval delegation, have the delegate approve an expense intended for
  re-invoicing, and inspect who the approval record actually shows.
```

## G08-SALE_EXPENSE-Q041

```yaml
QID: G08-SALE_EXPENSE-Q041
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where a customer-specific markup rate is itself changed after being applied to an already
  re-invoiced expense line but the change is intended only going forward, the earlier line's
  already-fixed amount is unaffected by the new rate.
WHY_IT_MATTERS: >
  This is the customer-negotiated-rate counterpart to Q006's general policy-change protection; a
  rate renegotiation must not quietly reprice a charge the customer already saw.
DISCONFIRMING_OBSERVATION: >
  Changing a customer's markup rate going forward alters the amount already recorded on an
  expense line re-invoiced under the prior rate.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Re-invoice an expense under one customer-specific markup rate, change that customer's rate, and
  inspect whether the earlier line's amount changed.
```

## G08-SALE_EXPENSE-Q042

```yaml
QID: G08-SALE_EXPENSE-Q042
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a special re-invoicing basis override is applied to a specific expense instead of the
  configured default, the record of that override persists as a value alongside the line, not lost
  once the resulting invoice posts.
WHY_IT_MATTERS: >
  Losing the override's record once posted makes it impossible to later explain why one customer's
  charge deviated from the standard policy.
DISCONFIRMING_OBSERVATION: >
  An overridden re-invoicing basis applied to a specific expense cannot be distinguished, once the
  invoice has posted, from an expense billed under the ordinary default policy.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply an override to a specific expense's re-invoicing basis, post the resulting invoice, and
  attempt to find a record that the override was applied.
```

## G08-SALE_EXPENSE-Q043

```yaml
QID: G08-SALE_EXPENSE-Q043
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A customer with portal or API access to their own invoices cannot enumerate or view re-invoiced
  expense detail belonging to a different customer's order through that same access.
WHY_IT_MATTERS: >
  Cross-customer visibility into another customer's re-invoiced cost detail is a direct data
  isolation failure with both privacy and competitive-exposure consequences.
DISCONFIRMING_OBSERVATION: >
  A customer's own portal or API access is used to retrieve re-invoiced expense detail belonging to
  an order that is not theirs.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a customer with portal or API access to their own invoices, attempt to retrieve re-invoiced
  expense detail for an order belonging to a different customer.
```

## G08-SALE_EXPENSE-Q044

```yaml
QID: G08-SALE_EXPENSE-Q044
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If an expense is approved for billing at the same moment its target order is independently
  closed or fully invoiced by someone else, one of the two operations is rejected or reconciled,
  not both silently succeeding and leaving the expense stranded as billable against a document that
  no longer accepts new lines.
WHY_IT_MATTERS: >
  A stranded, "billable" expense with nowhere left to be billed is a cost that silently falls out
  of both the customer-billing and the internal-reimbursement path.
DISCONFIRMING_OBSERVATION: >
  An expense approval and an independent order closure, occurring at close to the same time, both
  succeed, leaving the expense marked billable against an order that can no longer accept it.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Approve an expense for billing to a specific order at close to the same time that order is
  independently closed or fully invoiced by someone else, and inspect the expense's resulting state.
```

## G08-SALE_EXPENSE-Q045

```yaml
QID: G08-SALE_EXPENSE-Q045
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Whether a re-invoiced line's tax is computed from the sale's own tax rules or carried over from
  the expense's originally recorded tax is a deliberate, configured choice, not incidentally
  determined by which field happens to already be populated when the line is created.
WHY_IT_MATTERS: >
  An incidental rather than deliberate answer means the correct tax treatment (per Q018) can hold
  or fail to hold unpredictably depending on data-entry order rather than policy.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical re-invoiced expenses, differing only in which of their tax-relevant
  fields happened to be populated first, end up with different tax treatments and no configuration
  explains the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Produce two comparable re-invoiced expenses that differ only in data-entry order for
  tax-relevant fields and compare the resulting tax treatment on each.
```

## G08-SALE_EXPENSE-Q046

```yaml
QID: G08-SALE_EXPENSE-Q046
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  An expense recorded by a contractor or other external submitter with limited system access
  passes through the exact same approval-before-billing gate described in Q001 as an employee's
  expense — the gate is not bypassed for a different class of submitter.
WHY_IT_MATTERS: >
  A weaker gate for external submitters would make the control's overall strength only as good as
  its least-checked entry point.
DISCONFIRMING_OBSERVATION: >
  An expense submitted by an external, limited-access submitter reaches a customer-facing line
  without going through the same approval requirement an employee's equivalent expense would.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a contractor or other externally-scoped submitter, submit an expense intended for
  re-invoicing and compare the approval path it takes against an employee's equivalent expense.
```

## G08-SALE_EXPENSE-Q047

```yaml
QID: G08-SALE_EXPENSE-Q047
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Fully cancelling and voiding a customer order that had re-invoiced expenses on it returns those
  expenses to a billable-again state through an explicit, visible transition, not leaving them
  silently orphaned as permanently "already billed" with no order left to point to.
WHY_IT_MATTERS: >
  A cost permanently locked out of being billed elsewhere, because a now-void order still claims
  it, is a legitimate charge the business can never recover.
DISCONFIRMING_OBSERVATION: >
  After a customer order carrying re-invoiced expenses is fully voided, those expenses remain
  marked as billed with no visible path back to a billable state.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Re-invoice expenses onto an order, fully void that order, and inspect the resulting state of the
  expenses that were on it.
```

## G08-SALE_EXPENSE-Q048

```yaml
QID: G08-SALE_EXPENSE-Q048
MODULE: sale_expense
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A fixed re-invoicing price configured for a contract does not change even when the underlying
  expense's actual amount later turns out to differ, and any tracked difference is visible as a
  distinct value rather than blended invisibly into the fixed customer price.
WHY_IT_MATTERS: >
  A fixed price that silently absorbs an actual-cost difference removes the commercial certainty a
  fixed-price arrangement is supposed to provide to both sides.
DISCONFIRMING_OBSERVATION: >
  A fixed-price re-invoiced line's amount changes when the underlying expense's actual amount is
  later corrected, or the difference between the two is nowhere recorded.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure a fixed re-invoicing price for a contract, re-invoice an expense under it, then correct
  the underlying expense's actual amount, and inspect the fixed line and any difference record.
```

