# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_project_stock_account Module Bridge MVQ Bank — SUPPLEMENT R4

**Document ID:** GMVQ-G08-SALE_PROJECT_STOCK_ACCOUNT-MVQ-SUPPLEMENT-R4-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_project_stock_account`
**Wave:** W2 (GMVQ 25-Team Acceleration, 2026-09-27)
**Parent Bank:** G08_SALE_PROJECT_STOCK_ACCOUNT_GMVQ_MVQ_28_V1.00_DRAFT.md
**Parent count:** 28 (Q001–Q028)
**Questions added:** 10 (Q029–Q038)
**actual_mvq_count (resulting):** 38
**Author Cell:** P-S11 (GMVQ Production Team, GMVQ 25-Team Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**CHANGE_REASON:** Parent bank was authored to 28 material questions and honestly stopped below the
48-question floor set by GMVQ_AUTHORING_STANDARD_V1.00 §2 rather than padded. This supplement was
commissioned to establish, honestly, whether further genuine four-participant seam ground exists
(order + project + physical goods movement + ledger posting) per GMVQ_BRIDGE_MODULE_RULE_V1.00.

## ARITY EXHAUSTION STATEMENT — the 48 floor is NOT met by this supplement

Ten additional questions were found and are authored below. The resulting actual count is 38, still
10 short of the 48 floor. This shortfall is reported honestly rather than closed with manufactured
questions, per GMVQ_BRIDGE_MODULE_RULE_V1.00 §7 and GMVQ_AUTHORING_STANDARD_V1.00 §2.

Reasoning: the parent bank's 28 questions already exhaustively work the seam dimensions listed in
GMVQ_BRIDGE_MODULE_RULE_V1.00 §3 for this specific four-way combination — ORDERING and TIMING
(recognition at issue vs. invoice, fiscal-year-boundary mismatch, mid-period returns, billing ahead
of delivery), PARTIALITY (two tasks/two projects sharing one delivery or one order), OWNERSHIP
(which register is authoritative at closure, which entity's ledger receives a three-company posting),
QUANTITY AND MONEY (three-currency reconciliation, variance beyond priced assumption, two valuation
methods under one order), REVERSAL (cancellation with WIP, standard-cost change, write-off, deletion
of a project with a posted entry), and LIFECYCLE MISMATCH (fully invoiced order with a stranded WIP
balance, a return after the order's accounting period is closed). Each of these dimensions is already
represented, several of them more than once from a different triggering event, which is the correct
and expected density for a ledger-facing bridge — this is a case the Bridge Module Rule itself
anticipates in §7: "a short honest bank is worth more than a padded one."

Candidate ground that was considered and REJECTED because it duplicates a HYPOTHESIS already on disk
in the parent bank (checked per §5 against the full `grep -h 'HYPOTHESIS'` listing before authoring):
- "material cost capitalised to a project and the project later re-billed at a different value" —
  already covered by the parent's questions on the order's invoiced price against recognized cost,
  and on a project's completion being revised downward after both sides were already recognized.
- "the ledger attribution when project, order and warehouse sit in different companies" — already
  covered verbatim in substance by the parent's three-company posting and inter-company-ordering
  questions.
- "material returned after the project's revenue was recognized" — already covered by the parent's
  mid-period-return and closed-period-return questions; the ten new questions below deliberately do
  not add a third variant of the same reversal event.

Candidate ground REJECTED as belonging to a different module or a different arity, not this bridge:
- work-in-progress carrying both project labour and project material, settling in different periods —
  this pulls in recorded labour time, which is a `sale_timesheet` concern; applying the bridge test
  (would the question still make sense with labour removed?) answers NO for the labour half and YES
  for the material half, so it does not belong to this three-capability bank as a fourth participant.

## Questions

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q029
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Someone who can view a project's recognized cost or margin figure but has no permission to view
  the underlying order's own financial figures cannot see order-derived price or invoiced-revenue
  information through the project's cost view.
WHY_IT_MATTERS: >
  A cost or margin view that leaks order-level financial detail to someone without permission on the
  order itself would bypass the order's own access controls entirely.
DISCONFIRMING_OBSERVATION: >
  A person permitted to see a project's recognized cost or margin figure, but not permitted to see
  the funding order's own financial figures, can nonetheless see order-derived price or revenue
  detail through the project's cost view.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Grant a user permission to view a project's cost or margin figure without permission to view the
  funding order's own financial figures, and check what order-derived detail is visible through the
  project.
```

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q030
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A manual adjustment made directly to a project's recognized material cost figure is distinguishable
  in the record from a cost figure produced by the automated recognition process.
WHY_IT_MATTERS: >
  An adjustment indistinguishable from an automated figure would make it impossible to tell later
  whether a recognized cost reflects the system's own rule or a person's override of it.
DISCONFIRMING_OBSERVATION: >
  A manually entered adjustment to a project's recognized material cost figure appears identical in
  the record to a figure the automated recognition process produced, with no way to tell them apart
  afterward.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Let the automated process recognize a project's material cost, then manually adjust that figure,
  and check whether the adjustment is distinguishable from the automated figure in the record.
```

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q031
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A single material issue event that triggers both the automated cost-recognition process and a
  manual cost entry made for the same event at nearly the same time results in exactly one recognized
  cost entry for that event, not two.
WHY_IT_MATTERS: >
  Two recognized entries for one physical event would overstate the project's true cost and corrupt
  the margin figure computed against the order's revenue.
DISCONFIRMING_OBSERVATION: >
  A single material issue event produces two separate recognized cost entries, one automated and one
  manual, both counted toward the project's total cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Trigger the automated cost-recognition process for a material issue and, at nearly the same time,
  manually enter a cost record for that same issue, and check how many recognized entries result.
```

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q032
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Material cost recognized against a project whose funding line still sits on an unconfirmed
  quotation is not included in any report of cost matched against recognized revenue until that
  quotation is confirmed as an order.
WHY_IT_MATTERS: >
  Counting cost against revenue that does not yet exist because the customer has not committed would
  misstate margin for work that may never actually be sold.
DISCONFIRMING_OBSERVATION: >
  Material cost recognized against a project tied to an unconfirmed quotation appears in a report
  matching cost against recognized revenue before the quotation is confirmed as an order.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Attach a project to a quotation before confirmation, recognize material cost against it, and check
  whether that cost appears in any cost-versus-revenue report before the quotation is confirmed.
```

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q033
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Material cost already capitalized as a project's work-in-progress is excluded from the company's
  own on-hand stock valuation figure, so the same value is never counted in both the inventory asset
  figure and the project's asset figure at the same time.
WHY_IT_MATTERS: >
  Counting the same material value in both figures at once would overstate the company's total
  assets without either figure being individually wrong.
DISCONFIRMING_OBSERVATION: >
  Material cost capitalized as a project's work-in-progress still appears in the company's own
  on-hand stock valuation figure at the same time as it appears in the project's own asset figure.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Capitalize material cost as a project's work-in-progress, and check whether that same value still
  appears in the company's regular on-hand stock valuation report.
```

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q034
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A project explicitly configured to not track its own cost accounting still allows its funding
  order's own margin figure to compute correctly, without the missing project-level figure causing
  an error or an inflated margin from an assumed zero cost.
WHY_IT_MATTERS: >
  An order's margin silently inflating because a linked project opted out of cost tracking would
  misstate profitability with no visible cause.
DISCONFIRMING_OBSERVATION: >
  An order funding a project configured without cost accounting shows a margin figure that is either
  an error or one inflated by treating the missing project-level cost as zero.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure a project to not track its own cost accounting, fund it from an order, and check how the
  order's own margin figure computes.
```

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q035
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where an order line's remaining undelivered quantity is split off into a new order, material cost
  already recognized against the original order's project for the portion already delivered stays
  attributed to the original order, and cost for the portion still to be delivered is attributed to
  whichever order actually retains that scope.
WHY_IT_MATTERS: >
  Cost attribution left pointing at an order that no longer holds the remaining scope would misstate
  both the original and the new order's own margin figures.
DISCONFIRMING_OBSERVATION: >
  After an order line's remaining quantity is split into a new order, material cost recognized for
  that remaining quantity stays attributed to the original order, or the already-delivered portion's
  cost moves to the new order.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split an order line's remaining undelivered quantity into a new order after some cost was already
  recognized against the original order's project, and check which order each portion of cost stays
  attributed to.
```

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q036
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A recognized material cost entry referencing a project task that is later merged into a different
  task has its reference updated to the surviving task, rather than being left pointing at a task
  that no longer exists.
WHY_IT_MATTERS: >
  A cost entry pointing at a task that no longer exists would become untraceable back to the work
  and the order it was actually meant to represent.
DISCONFIRMING_OBSERVATION: >
  A recognized material cost entry still references a project task after that task has been merged
  into a different task, with no update to the surviving task's reference.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Recognize material cost against a project task, merge that task into a different task, and check
  whether the cost entry's reference is updated.
```

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q037
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where material is transferred between two stock locations of the same company that use different
  valuation methods before being consumed by a project, the cost recognized against the funding
  order uses one documented, consistently applied rule for which location's method governs.
WHY_IT_MATTERS: >
  Two locations disagreeing silently on which valuation method governs would let the same physical
  transfer produce a different recognized cost depending on which record is consulted.
DISCONFIRMING_OBSERVATION: >
  Material transferred between two stock locations using different valuation methods before project
  consumption has its recognized cost computed differently depending on which location's record is
  consulted, with no documented rule for which governs.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Transfer material between two stock locations of the same company that use different valuation
  methods, then have a project consume it, and check which location's valuation method the
  recognized cost uses.
```

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q038
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A credit note issued to the customer for fully delivered and consumed project material does not,
  by itself, automatically reverse the already-recognized material cost side of that transaction,
  leaving revenue and cost visibly reconciled rather than one adjusted without the other.
WHY_IT_MATTERS: >
  A one-sided reversal would leave the order's revenue and cost figures permanently disagreeing
  about the same physical event with no visible trace of why.
DISCONFIRMING_OBSERVATION: >
  A credit note issued for already-delivered and consumed project material either silently reverses
  the recognized material cost with no separate action, or leaves the revenue side adjusted with no
  documented treatment of the now-mismatched cost side.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Recognize revenue and material cost for delivered and consumed project material, issue a credit
  note to the customer for it, and check whether the cost side is reconciled against the
  revenue-side adjustment through a documented rule.
```
