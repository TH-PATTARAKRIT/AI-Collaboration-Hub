# GMVQ MODULE-SPECIFIC QUESTION BANK

Document ID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-GMVQ-MVQ-V1.00-DRAFT
Group: G06 MANUFACTURING
Module Metadata: mrp_subcontracting_landed_costs
Wave: W2
Author Cell: P13
Review Cell: PENDING
Status: DRAFT / AUTHORING COMPLETE / NOT FROZEN
actual_mvq_count: 48
Purpose: Module-specific research questions (MVQ) for the blind two-lane ROOM A study of
  mrp_subcontracting_landed_costs. Answered independently by Lane A (source reading) and Lane B
  (runtime observation only) and compared cell-to-cell by the Reconciler under MODULE + QID.
Control: Authored under GMVQ_AUTHORING_STANDARD_V1.00.md and GMVQ_BRIDGE_MODULE_RULE_V1.00.md.
  Clean Room absolute - generic ERP business/behavioural concepts only, no vendor names and no
  technical identifiers. This bank governs seam behaviour only: a cost that arrives after output
  the operator never physically held has already been consumed, sold, or shipped onward.
  Subcontracting's own invariants belong to mrp_subcontracting (cell P11); the ledger seam and the
  commercial-document seam belong to mrp_subcontracting_account / mrp_subcontracting_purchase
  (cell P12) and are out of scope here.

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
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q001
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A later-arriving cost can be allocated across output units even when those units cannot
  be physically inspected or counted at the time the cost arrives.
WHY_IT_MATTERS: >
  If allocation requires a physical count that is no longer possible, subcontracted output
  would be permanently excluded from later cost capture.
DISCONFIRMING_OBSERVATION: >
  Applying a later-arriving cost to already-dispersed subcontracted output fails or is
  blocked specifically because the units can no longer be physically counted.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A subcontracted production order fully received and its output already moved out of the
  receiving location, a later cost document introduced for it.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q002
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A later cost applied to subcontracted output that has already been consumed as a
  component in a further production order is reflected, in some form, in that further
  order's own cost.
WHY_IT_MATTERS: >
  If the cost stops at the first order, the true cost of the second order's output is
  permanently understated.
DISCONFIRMING_OBSERVATION: >
  The later cost is fully absorbed at the first production order with no mechanism to
  carry any portion of it into the second order that already consumed the output.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Subcontracted output received, consumed as a component in a second production order,
  then a later cost arrives for the original subcontracted order.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q003
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A later-arriving cost and a variance already recognized at the original receipt are kept
  as separate, individually identifiable entries rather than merging into one figure that
  could hide double counting.
WHY_IT_MATTERS: >
  If the two blend into one number, no one can verify afterward that the same amount was
  not counted twice.
DISCONFIRMING_OBSERVATION: >
  After the later cost is applied, the original variance entry and the new cost entry can
  no longer be distinguished or individually reconciled.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  A subcontracted order with a variance recognized at original receipt, followed by a
  later cost document for the same output.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q004
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A later cost applied to subcontracted output already sold to a customer is traceable
  back to the specific sale it affects.
WHY_IT_MATTERS: >
  Without that link, a margin correction happens with no visibility into which sale's
  profitability actually changed.
DISCONFIRMING_OBSERVATION: >
  The later cost is applied and posted with no traceable link back to the specific
  customer sale the affected output was part of.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Subcontracted output received, sold to a customer, then a later cost document arrives
  for that output.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q005
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A later cost arriving after the accounting period of the original receipt has closed is
  handled through a defined reopening or current-period mechanism, not silently dropped or
  silently posted against the closed period without any control.
WHY_IT_MATTERS: >
  An uncontrolled posting into a closed period undermines the integrity of financial
  statements already issued for that period.
DISCONFIRMING_OBSERVATION: >
  The later cost posts directly into the already-closed period with no reopening step,
  override record, or any distinguishing control.
EXPECTED_SURFACE: S2,S7
PRECONDITIONS: >
  A subcontracted order received and its accounting period closed, then a later cost
  document arrives referencing that order.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q006
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A later cost document that has already been distributed across several output units can
  be reversed in a way that unwinds the allocation from each affected unit individually.
WHY_IT_MATTERS: >
  An all-or-nothing reversal that cannot reach individual units would leave partial,
  unexplained cost residue behind.
DISCONFIRMING_OBSERVATION: >
  Reversing the later cost document leaves some previously allocated units with cost
  residue that cannot be traced or cleared.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A later cost document already applied across multiple subcontracted output units, then
  reversed or corrected.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q007
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The system can show, after the fact, exactly which output units absorbed a share of a
  given later cost, even though those units were never on the operator's own premises to
  be counted.
WHY_IT_MATTERS: >
  Without this, no one can answer a basic audit question about where a specific cost
  adjustment actually landed.
DISCONFIRMING_OBSERVATION: >
  The later cost document shows only a total amount applied with no breakdown reaching the
  individual units or lots it was spread across.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A later cost document applied across subcontracted output, reviewed for unit-level
  traceability.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q008
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the affected output quantity is split across multiple destinations (in stock,
  consumed, shipped to customer) at the time the later cost arrives, one consistent
  allocation basis is applied across all of them.
WHY_IT_MATTERS: >
  An inconsistent basis by destination would make the per-unit cost meaningless for
  comparison or reconciliation.
DISCONFIRMING_OBSERVATION: >
  The allocation basis used differs depending on which destination a portion of the output
  has reached, with no configuration explaining the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Subcontracted output split across in-stock, consumed, and shipped destinations, a later
  cost document applied across the whole quantity.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q009
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A later cost can be attributed to a specific production order and event, not only to a
  batch or period in aggregate, when the source document identifies one.
WHY_IT_MATTERS: >
  Aggregated-only attribution would prevent any investigation from isolating which
  specific production run actually incurred the extra cost.
DISCONFIRMING_OBSERVATION: >
  A later cost document that clearly references one specific production order can only be
  applied at an aggregate batch or period level, losing that specific link.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A later cost document referencing one identifiable subcontracted production order.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q010
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A later cost cannot be applied to a subcontracted receipt that has not yet been
  finalized, preventing the two from racing into an inconsistent combined state.
WHY_IT_MATTERS: >
  Allowing a cost to attach ahead of a finalized receipt risks the cost applying to a
  quantity or valuation that is still subject to change.
DISCONFIRMING_OBSERVATION: >
  A later cost document is successfully applied to a subcontracted receipt that is still
  in an unfinalized, editable state, and the receipt is subsequently changed without
  adjusting the cost.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  A subcontracted receipt left in an unfinalized state, a later cost document introduced
  against it before finalization.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q011
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the components actually sent to the external party differed from the original plan
  (a substitution), a later cost applied afterward follows the actual components used, not
  the originally planned ones.
WHY_IT_MATTERS: >
  Allocating the cost against the wrong component set would misstate the true cost of what
  was actually produced.
DISCONFIRMING_OBSERVATION: >
  The later cost calculation or allocation still references the originally planned
  components rather than the ones actually substituted and consumed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A subcontracted order where a component substitution occurred, followed by a later cost
  document.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q012
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A later cost document referencing a production event that has since been fully reversed
  is flagged as unresolved rather than silently applied or silently dropped.
WHY_IT_MATTERS: >
  A silently dropped cost is a real charge going unrecorded; a silently applied one
  attaches money to an event that officially no longer exists.
DISCONFIRMING_OBSERVATION: >
  The later cost document is applied or discarded with no flag, exception, or record
  indicating that its referenced production event no longer exists.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A subcontracted production order fully reversed or cancelled, then a later cost document
  arrives referencing it.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q013
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a later cost may be applied to subcontracted output that has already left the
  operator's control is governed by an explicit, visible setting rather than being an
  unconditional, undocumented capability.
WHY_IT_MATTERS: >
  An undocumented unconditional capability means no one deliberately decided this
  behavior should be allowed.
DISCONFIRMING_OBSERVATION: >
  No setting or configuration governing this capability can be found; the behavior simply
  occurs whenever attempted with no controlling option anywhere.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Subcontracted output already dispersed beyond operator control, a later cost document
  introduced, configuration reviewed.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q014
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Applying a later cost to output already sold triggers a visible re-evaluation of that
  sale's recorded margin, rather than the margin figure remaining frozen at its original,
  now-outdated value.
WHY_IT_MATTERS: >
  A frozen, outdated margin figure would misrepresent the actual profitability of a
  completed sale to anyone relying on it.
DISCONFIRMING_OBSERVATION: >
  The originally recorded margin on the affected sale remains unchanged and unflagged
  after the later cost is applied.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Subcontracted output sold to a customer with a recorded margin, then a later cost
  applied to that output.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q015
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the external party's engagement spans more than one of the operator's own company
  records, the later cost is attributed to a specific, determinable entity rather than
  left ambiguous.
WHY_IT_MATTERS: >
  Ambiguous entity attribution would misstate the accounts of whichever entity should
  have, or should not have, borne the cost.
DISCONFIRMING_OBSERVATION: >
  The later cost document offers no way to determine or select which company entity's
  books it should post against when more than one is involved.
EXPECTED_SURFACE: S2,S4
PRECONDITIONS: >
  A subcontracting relationship spanning two of the operator's own company records, a
  later cost document introduced.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q016
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two later-cost documents arriving for overlapping output quantities at nearly the same
  time are applied in a way that prevents the same unit from absorbing both in full,
  unless that is the deliberate intent.
WHY_IT_MATTERS: >
  Two uncoordinated full applications to the same units would silently double the cost
  burden on them.
DISCONFIRMING_OBSERVATION: >
  Both later-cost documents apply their full amount to the same overlapping units with no
  reconciliation or warning of the overlap.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Two later-cost documents introduced in close succession, both targeting an overlapping
  quantity of the same subcontracted output.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q017
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a later cost is split across output that no longer forms an intact physical
  grouping, any rounding remainder is assigned through a defined, consistent rule rather
  than left unassigned or assigned arbitrarily.
WHY_IT_MATTERS: >
  An unassigned remainder is money that disappears from the books; an arbitrary assignment
  is unauditable.
DISCONFIRMING_OBSERVATION: >
  A rounding remainder from the allocation cannot be located anywhere in the resulting
  entries, or its assignment cannot be explained by any stated rule.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A later cost document whose amount does not divide evenly across the affected output
  quantity.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q018
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Applying a cost adjustment to output that has already left the operator's control
  entirely requires a role beyond ordinary data entry access.
WHY_IT_MATTERS: >
  Unrestricted authority to adjust cost on goods no one can verify anymore creates a
  control gap for manipulation or error.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary data-entry access, and no cost or accounting authorization
  role, can successfully apply the later cost.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  A later cost document ready to apply to already-departed subcontracted output, attempted
  by users with different role assignments.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q019
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A durable, queryable link is recorded between the later cost document and each
  individual output unit it affected, not only a one-line summary total.
WHY_IT_MATTERS: >
  Without a durable link, the connection between a cost and what it actually touched is
  lost as soon as the summary view is closed.
DISCONFIRMING_OBSERVATION: >
  No query or report can reconstruct, from the later cost document alone, the individual
  units it was allocated across.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A later cost document already applied across multiple subcontracted output units.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q020
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a later cost document's stated quantity exceeds what was actually produced or
  received in the original event, the system flags the mismatch rather than applying the
  excess silently.
WHY_IT_MATTERS: >
  Silently applying an overstated quantity spreads cost across units that were never
  actually part of the transaction.
DISCONFIRMING_OBSERVATION: >
  A later cost document quantity larger than the original receipt is accepted and applied
  without any mismatch warning.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A later cost document whose stated quantity exceeds the original subcontracted receipt
  quantity.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q021
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a later cost document covers fewer units than the full original output, the system
  requires an explicit choice of which units receive it rather than applying a default
  that isn't visible to the person posting it.
WHY_IT_MATTERS: >
  An invisible default choice means no one can verify or challenge which specific units
  were selected to absorb the cost.
DISCONFIRMING_OBSERVATION: >
  The later cost is applied to a subset of units by a default rule that is never shown or
  made available for the posting person to see or override.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A later cost document covering fewer units than the full original subcontracted output
  quantity.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q022
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The system uses a single, clearly defined date among the cost's invoice date, entry
  date, and the original production date to determine which accounting period the later
  cost lands in.
WHY_IT_MATTERS: >
  An unclear or inconsistent choice of governing date could place the same kind of cost
  into different periods depending on how it happens to be entered.
DISCONFIRMING_OBSERVATION: >
  Two later-cost documents with identical invoice and production dates but entered on
  different days land in different accounting periods.
EXPECTED_SURFACE: S2
PRECONDITIONS: >
  Two comparable later-cost documents differing only in system entry date, period
  placement compared.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q023
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A correction to an undercosted component and a new service charge from the external
  party are both handled through the same later-cost mechanism, or the difference between
  the two paths is explicit and documented.
WHY_IT_MATTERS: >
  Two silently different mechanisms for what looks like the same kind of adjustment invite
  inconsistent handling depending on which path someone happens to use.
DISCONFIRMING_OBSERVATION: >
  The two cases produce materially different outcomes (different traceability, different
  period handling, different allocation) with no documented reason for the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  One later-cost case originating from a component cost correction and one from a new
  external service charge, outcomes compared.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q024
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a single later-cost document covers a mixed population of still-on-hand and
  already-departed output, the on-hand portion's valuation is updated distinctly and
  visibly from the departed portion's treatment.
WHY_IT_MATTERS: >
  If the two are blended without distinction, the operator cannot verify that on-hand
  inventory value was actually corrected.
DISCONFIRMING_OBSERVATION: >
  After applying the later cost, the on-hand portion's valuation shows no traceable
  adjustment distinguishable from what happened to the departed portion.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A later cost document covering output that is partly on hand and partly already
  departed, applied and reviewed.
```
```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q025
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A later cost document referencing a subcontracted production order that never fully
  completed is held or flagged rather than applied silently to whatever partial state
  exists.
WHY_IT_MATTERS: >
  Silent application to an incomplete order risks attaching a cost to output that may
  still change or never materialize.
DISCONFIRMING_OBSERVATION: >
  The later cost document applies without any hold, flag, or warning against a production
  order that never reached completion.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A subcontracted production order left incomplete, a later cost document introduced
  referencing it.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q026
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If both the original receipt and its later cost need to be reversed, the system either
  enforces a required order between the two reversals or produces a correct result
  regardless of the order chosen.
WHY_IT_MATTERS: >
  An order-dependent result that isn't enforced could leave inconsistent figures behind
  depending on which the user reverses first.
DISCONFIRMING_OBSERVATION: >
  Reversing the later cost before the original receipt produces a different, unreconciled
  final state than reversing them in the opposite order.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Both an original subcontracted receipt and its later cost document reversed, in each of
  the two possible orders, for comparison.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q027
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A later cost that corrects an estimate already embedded in the original valuation is
  recorded distinctly from a later cost that is a genuinely new, previously unestimated
  charge.
WHY_IT_MATTERS: >
  Treating a correction and a brand-new charge identically obscures whether the original
  estimate process is working or not.
DISCONFIRMING_OBSERVATION: >
  Both cases post through the identical entry type and label, with nothing distinguishing
  a correction from a genuinely new charge.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  One later cost representing a correction to an original estimate, and one representing a
  genuinely new charge, entries compared.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q028
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A later cost cannot be silently applied to a subcontracted production order that has
  been closed and locked for its period without an explicit unlock or override step.
WHY_IT_MATTERS: >
  Allowing silent changes to locked, closed records defeats the purpose of period locking
  as a financial control.
DISCONFIRMING_OBSERVATION: >
  The later cost applies successfully to a closed and locked production order with no
  unlock, override, or exception record of any kind.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  A subcontracted production order closed and locked for its period, a later cost document
  introduced against it.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q029
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If output that already absorbed a later cost is subsequently returned to the external
  party as defective, the cost's disposition (retained, reversed, or reallocated) is an
  explicit, visible outcome rather than left unaddressed.
WHY_IT_MATTERS: >
  Leaving the cost's fate unaddressed on a returned defective unit either overstates its
  value or silently loses the cost record.
DISCONFIRMING_OBSERVATION: >
  The output is returned as defective and its later-cost allocation remains exactly as it
  was, with no visible decision or record about what happens to it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Subcontracted output that already absorbed a later cost, then returned to the external
  party as defective.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q030
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The later-cost allocation mechanism treats a batch with partial ship-through (some units
  gone to a customer, some still on hand) as distinguishable groups rather than one
  undifferentiated pool.
WHY_IT_MATTERS: >
  Treating them as one pool loses the distinction the operator needs between cost sitting
  in inventory and cost that has already flowed through to a sale.
DISCONFIRMING_OBSERVATION: >
  The allocation result gives no way to separate how much of the later cost landed on the
  still-on-hand portion versus the already-shipped portion.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A subcontracted output batch with partial ship-through, a later cost document applied
  across the whole batch.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q031
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A later cost can still be applied, in some traceable form, even when no unit of the
  original output remains identifiable because it was fully consumed into a further
  assembly.
WHY_IT_MATTERS: >
  If the cost simply cannot be applied in this case, it either gets lost entirely or forced
  into an unrelated, arbitrary posting.
DISCONFIRMING_OBSERVATION: >
  The later cost cannot be applied at all once the output is fully consumed into a further
  assembly, and no alternative traceable posting path exists either.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Subcontracted output fully consumed as a component into a further assembly, a later cost
  document introduced afterward.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q032
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A later cost applied to output already consumed as a component in a second production
  order flows into that second order's recorded cost, rather than stopping at the first
  order's records only.
WHY_IT_MATTERS: >
  If the cascade stops short, the second order's cost figure never reflects a real cost
  that belongs to it.
DISCONFIRMING_OBSERVATION: >
  The second production order's recorded cost is unchanged after the later cost is applied
  to the first order's already-consumed output.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Subcontracted output consumed into a second production order, a later cost then applied
  to the first order's output.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q033
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the later cost is denominated in a different currency than the original receipt,
  the exchange rate used for allocation is explicit and recorded, not implicitly assumed.
WHY_IT_MATTERS: >
  An unrecorded implicit rate makes the allocated amount unverifiable and unreproducible
  later.
DISCONFIRMING_OBSERVATION: >
  The exchange rate actually used to convert and allocate the later cost cannot be found
  anywhere in the resulting records.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A later cost document denominated in a currency different from the original
  subcontracted receipt.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q034
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Applying a later cost to output already fully consumed, sold, or shipped is reachable
  through the standard document flow, not only through a manual journal workaround outside
  the mechanism's own logic.
WHY_IT_MATTERS: >
  A manual-only path means the scenario's actual behavior may differ from whatever the
  intended mechanism is meant to produce.
DISCONFIRMING_OBSERVATION: >
  Applying the later cost to already-disposed output can only be achieved through a manual
  journal entry outside the later-cost mechanism itself.
EXPECTED_SURFACE: S2,S7
PRECONDITIONS: >
  Subcontracted output already fully disposed of (consumed, sold, or shipped), a later
  cost applied using only the standard mechanism.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q035
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If guidance describes the later cost as needing to be applied before the receipt is
  closed, the runtime either enforces that requirement or the guidance is corrected to
  match what is actually allowed.
WHY_IT_MATTERS: >
  A live contradiction between stated requirement and actual permissiveness means neither
  can be relied on with confidence.
DISCONFIRMING_OBSERVATION: >
  The later cost is successfully applied well after the receipt is closed, contradicting a
  stated requirement that it happen before closure, with the contradiction unacknowledged
  anywhere.
EXPECTED_SURFACE: S2,S7
PRECONDITIONS: >
  A subcontracted receipt closed, a later cost applied afterward, checked against any
  stated requirement about timing.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q036
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two later costs from two different sources, both targeting the same output batch, are
  combined in a way that keeps each one's contribution separately identifiable in the
  final valuation.
WHY_IT_MATTERS: >
  Merging them into one indistinguishable adjustment prevents anyone from later isolating
  which source contributed what.
DISCONFIRMING_OBSERVATION: >
  After both later costs are applied, their individual contributions to the batch's
  valuation can no longer be separated or identified.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Two later-cost documents from different sources, both applied in sequence to the same
  subcontracted output batch.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q037
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The later cost record retains a link back to the external party's original commercial
  document it was billed on, not only to the internal production record.
WHY_IT_MATTERS: >
  Without that link, verifying a later cost against what the external party actually
  billed requires a separate manual cross-reference.
DISCONFIRMING_OBSERVATION: >
  The later cost record shows no reference at all to the external commercial document it
  originated from.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A later cost document originating from an external party's commercial document, reviewed
  for traceable linkage.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q038
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A later cost document voided before it is ever applied leaves no provisional allocation
  behind that would need separate cleanup.
WHY_IT_MATTERS: >
  A stray provisional allocation from a voided document could be mistaken for a real,
  applied cost if not cleanly removed.
DISCONFIRMING_OBSERVATION: >
  Voiding the later cost document before application leaves a provisional allocation entry
  still visible against the affected output.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A later cost document created but voided before ever being applied to output.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q039
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a planned component cost correction and a later external cost both affect the same
  production order at the same time, the system applies both without one silently
  overwriting or absorbing the other.
WHY_IT_MATTERS: >
  One correction silently overwriting the other would leave the final cost figure
  reflecting only one of two real adjustments.
DISCONFIRMING_OBSERVATION: >
  Applying both corrections in close succession results in only one of the two being
  reflected in the final cost figure.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A subcontracted production order with both a component cost correction and a later
  external cost introduced at nearly the same time.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q040
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The basis used to allocate a later cost (quantity, value, weight, or another driver) has
  a defined default when left unset, rather than failing or behaving unpredictably.
WHY_IT_MATTERS: >
  Unpredictable behavior when the basis is unset would make the allocation outcome depend
  on an accident of configuration rather than a deliberate choice.
DISCONFIRMING_OBSERVATION: >
  Leaving the allocation basis unset produces an error, an unexplained default, or an
  inconsistent result across otherwise identical cases.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  A later cost document introduced with the allocation basis setting deliberately left
  unset.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q041
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The sum of all individual unit-level allocations from a later cost document always
  reconciles exactly to that document's stated total.
WHY_IT_MATTERS: >
  A drifting sum would mean money is being created or lost purely through the mechanics of
  the allocation process.
DISCONFIRMING_OBSERVATION: >
  Summing the individual unit-level allocations produces a total that differs from the
  later cost document's stated amount.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A later cost document applied across a quantity of subcontracted output that does not
  divide evenly.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q042
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A later cost applied against output that was itself scrapped after receipt but before
  the cost arrived is reflected as a loss or write-off rather than sitting as if the output
  were still a normal asset.
WHY_IT_MATTERS: >
  Treating cost on scrapped output as if it still had ordinary value would overstate the
  value of stock that no longer exists.
DISCONFIRMING_OBSERVATION: >
  The later cost posts against the scrapped output with no distinction from how it would
  post against normal, undamaged output.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Subcontracted output received and then scrapped, a later cost document arriving
  afterward for that output.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q043
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The role that approves the later cost is checked against, and can be distinguished from,
  the role that approved the original production receipt, at least in the audit record.
WHY_IT_MATTERS: >
  With no distinction recorded, a segregation-of-duties review cannot verify whether the
  same person controlled both ends of the transaction.
DISCONFIRMING_OBSERVATION: >
  The audit record for the later cost gives no way to determine whether its approver is
  the same person who approved the original receipt.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  A later cost document approved by a specific role, original receipt approval role
  reviewed for comparison.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q044
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A single later-cost document covering output produced across more than one production
  order in the same period can represent the split across those orders individually.
WHY_IT_MATTERS: >
  Without the split, the cost cannot be attributed correctly to the specific orders whose
  output actually incurred it.
DISCONFIRMING_OBSERVATION: >
  A later cost document covering multiple production orders can only be applied to one of
  them, forcing the others to be handled through a separate, disconnected entry.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A later cost document whose stated scope spans output from more than one subcontracted
  production order in the same period.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q045
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the later cost is denominated in a different unit of measure than the output was
  received in, the system performs and records an explicit conversion rather than applying
  the cost without regard to the mismatch.
WHY_IT_MATTERS: >
  Applying a cost across mismatched units without conversion would misallocate the cost
  per actual unit of output.
DISCONFIRMING_OBSERVATION: >
  The later cost is applied without any visible conversion step despite being denominated
  in a different unit of measure than the received output.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A later cost document denominated in a different unit of measure than the original
  subcontracted receipt.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q046
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If applying a later cost requires reopening an already-closed accounting period, that
  reopening is logged as its own distinct auditable event, separate from the cost
  application itself.
WHY_IT_MATTERS: >
  Without a distinct log of the reopening, a reviewer cannot tell how often, or by whom,
  closed periods are being reopened at all.
DISCONFIRMING_OBSERVATION: >
  The period reopening required to apply the later cost leaves no separate audit trace
  distinguishable from the cost application entry itself.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  A later cost document requiring an already-closed accounting period to be reopened
  before it can be applied.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q047
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The system's record linking a later cost to a specific unit relies on an identifier
  established at the original receipt, not on an assumption made only at the time the cost
  is applied.
WHY_IT_MATTERS: >
  Without that anchor, there's no basis for claiming the unit charged is the same physical
  unit the original receipt actually recorded.
DISCONFIRMING_OBSERVATION: >
  The unit-level link used when applying the later cost is newly assigned at application
  time rather than tracing back to an identifier recorded at the original receipt.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A later cost document applied at the unit level to subcontracted output, identifier
  lineage reviewed.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_LANDED_COSTS-Q048
MODULE: mrp_subcontracting_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the system reuses the same later-cost mechanism for subcontracted output as for an
  ordinarily purchased good, that reuse does not silently ignore the fact that
  subcontracted output was never in the operator's own custody at receipt.
WHY_IT_MATTERS: >
  A mechanism built for goods the operator directly received and inspected may carry
  assumptions that do not hold for subcontracted output, if applied unmodified.
DISCONFIRMING_OBSERVATION: >
  The later-cost mechanism treats subcontracted output identically to an ordinarily
  purchased good in every respect, including aspects that assume direct physical receipt
  occurred.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  One later-cost case applied to subcontracted output and one applied to an ordinarily
  purchased good, mechanisms compared.
```
