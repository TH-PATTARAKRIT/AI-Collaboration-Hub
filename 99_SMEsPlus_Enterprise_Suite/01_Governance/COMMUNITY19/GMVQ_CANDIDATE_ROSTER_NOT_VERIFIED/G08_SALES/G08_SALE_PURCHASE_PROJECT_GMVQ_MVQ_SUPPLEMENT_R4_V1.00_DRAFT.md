# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_purchase_project Module Bridge MVQ Bank — SUPPLEMENT R4

**Document ID:** GMVQ-G08-SALE_PURCHASE_PROJECT-MVQ-SUPPLEMENT-R4-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_purchase_project`
**Wave:** W2 (GMVQ 25-Team Acceleration, 2026-09-27)
**Parent Bank:** G08_SALE_PURCHASE_PROJECT_GMVQ_MVQ_20_V1.00_DRAFT.md
**Parent count:** 20 (Q001–Q020)
**Questions added:** 5 (Q021–Q025)
**actual_mvq_count (resulting):** 25
**Author Cell:** P-S11 (GMVQ Production Team, GMVQ 25-Team Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**CHANGE_REASON:** Parent bank was authored to 20 material questions and honestly stopped well
below the 48-question floor set by GMVQ_AUTHORING_STANDARD_V1.00 §2 rather than padded. This
supplement was commissioned to establish, honestly, whether further genuine three-participant seam
ground exists (customer order + project task + vendor commitment) per GMVQ_BRIDGE_MODULE_RULE_V1.00.

## ARITY EXHAUSTION STATEMENT — the 48 floor is NOT met by this supplement

Five additional questions were found and are authored below. The resulting actual count is 25, 23
short of the 48 floor. This is the module the Control Desk explicitly expects to land short (per the
governing directive), and this result confirms that expectation with real numbers rather than
assuming it. The shortfall is reported honestly rather than closed with manufactured questions, per
GMVQ_BRIDGE_MODULE_RULE_V1.00 §7.

Reasoning: `sale_purchase_project` is a three-participant bridge (order, project task, vendor
commitment) with a narrower genuine seam than a two-participant bridge, because most of the
candidate ground that touches only two of the three participants correctly belongs to a sibling bank
and is excluded by the bridge test in GMVQ_BRIDGE_MODULE_RULE_V1.00 §2 ("if this capability were
removed and A and B were used entirely apart, would the question still make sense?"). The parent
bank's 20 questions already cover: ORDERING (task removal after commitment, order amendment after
commitment, order-scope mismatch surfacing), OWNERSHIP (traceability surviving re-numbering,
reassignment leaving a visible trail, which authority governs a spend decision), TIMING (invoiced
reality updating tracked spend, expected receipt date following order changes), PARTIALITY (partial
receipt allocation across two order-funded tasks, one commitment serving order and non-order
purchases), REVERSAL/LIFECYCLE MISMATCH (cancellation flagging the commitment, task merge updating
the reference, project hold's treatment of a placed commitment, duplicated task not inheriting a
live reference), AUTHORITY (separate approval chains for project spend vs. purchasing approval), and
ERROR ASYMMETRY (substitute-item and late-delivery reconciliation against the order's current
state). This is close to the full set of dimensions in GMVQ_BRIDGE_MODULE_RULE_V1.00 §3 already
represented at least once, which is the expected shape for a genuinely narrow three-participant
bridge rather than a sign that authoring stopped early.

Candidate ground supplied in the routing brief for this run and REJECTED on the bridge test, because
it survives with one of the three participants removed and therefore belongs to a sibling bank, not
here (checked per §5 against the full `grep -h 'HYPOTHESIS'` listing before authoring):
- "a vendor commitment raised against a project budget the customer order later reduces" — this is
  already covered verbatim in substance by the parent bank's existing question on amending the
  customer order's scope after a vendor commitment was placed for the original scope.
- "the vendor delivering to the project site against an order line billed to a different address" —
  removing the project, this is still a meaningful question about a vendor delivery address versus
  an order's billing address; it belongs to `sale_purchase`, not to this bridge, and duplicates
  ground the parent bank already covers from the project-site-versus-general-warehouse angle.
- "committed-versus-actual spend visible on the project while the customer sees only the order
  value" — partially valid; the surviving, non-duplicate half of this ground is authored below as
  Q022, scoped specifically to what the CUSTOMER can see, which the parent bank did not yet ask.

## Questions

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q021
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A subcontracted deliverable that a project marks as accepted, but that the customer subsequently
  disputes or rejects on the funding order, results in a documented reopening of the vendor
  commitment's acceptance status rather than the vendor commitment remaining closed as accepted.
WHY_IT_MATTERS: >
  A vendor commitment left closed as accepted while the customer disputes the very deliverable it
  paid for would leave no path back to the vendor for correction or recovery.
DISCONFIRMING_OBSERVATION: >
  A project's subcontracted deliverable is marked accepted, the customer disputes it on the funding
  order, and the vendor commitment's own acceptance status stays closed with no documented
  reopening.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Mark a subcontracted deliverable as accepted at the project, have the customer dispute it on the
  funding order, and check whether the vendor commitment's acceptance status is reopened.
```

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q022
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A customer viewing their own order through a self-service channel sees only the order's own price,
  not the internal vendor commitment amount raised to source the project task fulfilling that order.
WHY_IT_MATTERS: >
  Exposing the internal procurement cost to the customer would reveal the company's own margin and
  sourcing terms that were never meant for external visibility.
DISCONFIRMING_OBSERVATION: >
  A customer viewing their own order through a self-service channel can see the internal vendor
  commitment amount raised to source the project task behind that order.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Raise a vendor commitment to source a project task funding a customer's order, and check what the
  customer can see about that commitment through their own self-service view of the order.
```

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q023
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a project task after its vendor commitment has already passed the point of being
  cancellable results in a documented disposition of that now-orphaned commitment, rather than the
  cancelled task simply losing any reference to an obligation that still stands.
WHY_IT_MATTERS: >
  An irrevocable vendor obligation with no task left to consume it would leave a standing cost with
  nobody accountable for deciding what to do with it.
DISCONFIRMING_OBSERVATION: >
  A project task is cancelled while its vendor commitment can no longer be cancelled, and no
  documented record shows what happens to that now-orphaned, still-standing commitment.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a project task after its vendor commitment has passed the point where it can still be
  cancelled, and check whether a documented disposition of the commitment is recorded.
```

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q024
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Rejecting and returning vendor-delivered material to the vendor after the project task it was
  meant to fulfil has already reported that material as consumed against the customer order results
  in a documented reconciliation of the resulting shortfall.
WHY_IT_MATTERS: >
  An unreconciled shortfall between material reported consumed and material actually returned to the
  vendor would leave the customer order's fulfilment record referencing material that is no longer
  there.
DISCONFIRMING_OBSERVATION: >
  Vendor-delivered material already reported consumed by a project task is returned to the vendor
  with no documented reconciliation of the resulting shortfall against the customer order it was
  fulfilling.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Report vendor-delivered material as consumed by a project task fulfilling a customer order line,
  then reject and return that material to the vendor, and check whether the shortfall is reconciled.
```

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q025
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A vendor commitment priced in a different currency than its funding customer order is converted
  using one documented rate when compared against the project's own tracked spend, rather than the
  two being compared at face value in two different currencies.
WHY_IT_MATTERS: >
  Comparing unconverted figures in two currencies could make a commitment look within budget or over
  budget purely as an artefact of which currency happened to be larger in number, not real cost.
DISCONFIRMING_OBSERVATION: >
  A vendor commitment priced in a different currency than its funding customer order is compared
  against the project's tracked spend at face value, with no documented conversion rate applied.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Raise a vendor commitment in a currency different from its funding customer order's own currency,
  and check how that commitment is compared against the project's own tracked spend.
```
