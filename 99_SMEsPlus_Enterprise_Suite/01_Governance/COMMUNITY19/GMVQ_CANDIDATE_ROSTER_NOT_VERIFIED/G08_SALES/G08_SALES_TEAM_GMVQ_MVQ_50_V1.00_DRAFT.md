# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sales_team Module Adversarial MVQ Bank

**Document ID:** GMVQ-G08-SALES_TEAM-MVQ50-V1.00
**Group:** G08 SALES
**Module Metadata:** `sales_team`
**Wave:** W2
**Author Cell:** P-S1 (GMVQ Question Factory — Production Team P-S1)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50

## Purpose

`sales_team` is the second BASE module of G08. Where `sale` treats the commercial transaction, this bank treats the organisational dimension: who owns an order, who may see it, and how organisational structure interacts with target and pipeline reporting over time. Ground covered: an order's team versus its individually assigned owner when the two disagree; an individual moved between teams while orders are open, and what happens to history and to accrued targets; a team archived with open orders still attached; targets and quota measured against an explicit date basis (order, delivery, or invoice) and restated when an order is cancelled; visibility rules governing one team seeing another's pipeline or margins; a manager's access versus an ordinary member's; bulk reassignment and its audit trail; a team spanning more than one company; an order with no team attribution at all; commission or credit attribution when two individuals touch one order; and the team dimension inside a report that a later reassignment would otherwise silently rewrite. Per the Bridge Module Rule, this bank does not restate `sale`'s transactional invariants (Q048 explicitly tests that organisational attribution cannot alter commercial content) -- it treats ownership, visibility and organisational reporting only.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 50 questions exist because they test 50 distinct material hypotheses, spread across business capability, business rule, state transition, configuration dependency, role/permission, exception path, reversal, negative case, auditability, tenant/company boundary, concurrency and ordering, and configuration reachability.
- Particular depth is placed on team/owner disagreement and reassignment history (Q001-Q006), on visibility and permission boundaries distinct from ordinary order access (Q012-Q015, Q032, Q040-Q041), and on target restatement and reporting integrity across a reassignment (Q010-Q011, Q024-Q025, Q034-Q036).
- `LAYER: BASE` marks a foundation/configuration question (team/owner data-model independence, membership versus target configuration, multi-company scope, visibility-permission structure, manager-role assignment); `LAYER: PROCESS` marks a transactional/lifecycle question, since this module carries both layers.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.


## G08-SALES_TEAM-Q001

```yaml
QID: G08-SALES_TEAM-Q001
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Every order carries a team attribution and an individually assigned owner as two independently stored values, so the two can legitimately disagree rather than one being derived from the other at read time.
WHY_IT_MATTERS: >
  If the individual owner were merely derived from the team, there would be no way to represent the ordinary case of one person on a team handling a specific account while the record still rolls up to their team.
DISCONFIRMING_OBSERVATION: >
  An order's individually assigned owner cannot be set to anyone outside its recorded team, showing the owner is derived from the team rather than stored independently.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to assign an order's individual owner to someone who is not a member of that order's recorded team.
```

## G08-SALES_TEAM-Q002

```yaml
QID: G08-SALES_TEAM-Q002
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When an order's team and its individually assigned owner disagree (the owner does not belong to the recorded team), the order still resolves to a single determining owner for target and pipeline purposes rather than being counted twice or not at all.
WHY_IT_MATTERS: >
  An order counted twice would inflate combined figures, while one counted nowhere would understate them; either failure makes every aggregate number built on top of it unreliable.
DISCONFIRMING_OBSERVATION: >
  An order whose owner does not belong to its recorded team is counted in both the owner's and the team's separate target figures, or in neither.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create an order whose individually assigned owner does not belong to the order's recorded team, and check how it is counted in each figure.
```

## G08-SALES_TEAM-Q003

```yaml
QID: G08-SALES_TEAM-Q003
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Changing an order's team after confirmation does not silently change which individual is recorded as its owner.
WHY_IT_MATTERS: >
  If a team change silently reassigned the owner too, no one could change organisational attribution without also, unintentionally, changing who is personally responsible for the account.
DISCONFIRMING_OBSERVATION: >
  Changing a confirmed order's recorded team also changes its individually assigned owner with no separate action taken on the owner field.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order, note its individual owner, change only the order's team, and check whether the owner field changed as a side effect.
```

## G08-SALES_TEAM-Q004

```yaml
QID: G08-SALES_TEAM-Q004
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Moving an individual from one team to another leaves that individual's historical orders attributed to the team recorded on each order at the time it was created or confirmed, not retroactively reattributed to the new team.
WHY_IT_MATTERS: >
  Retroactively reattributing history would rewrite what team actually handled a past transaction, corrupting any historical reporting built on that record.
DISCONFIRMING_OBSERVATION: >
  Moving an individual to a new team changes the team recorded on that individual's already-existing, previously confirmed orders.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Move an individual with existing confirmed orders to a different team and check whether the team recorded on those existing orders changed.
```

## G08-SALES_TEAM-Q005

```yaml
QID: G08-SALES_TEAM-Q005
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A target or quota figure already accrued under a prior team assignment is not silently transferred to or merged with the new team's target after a reassignment.
WHY_IT_MATTERS: >
  Silently merging accrued figures across teams would let one team's performance history inflate or dilute a different team's target with no visible explanation.
DISCONFIRMING_OBSERVATION: >
  Reassigning an individual to a new team causes that individual's previously accrued target contribution to appear inside the new team's target figure.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reassign an individual with an already-accrued target contribution to a new team and check whether that prior contribution appears in the new team's figures.
```

## G08-SALES_TEAM-Q006

```yaml
QID: G08-SALES_TEAM-Q006
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An individual moved between teams mid-period has their contribution attributed by an explicit rule (split by date, wholly to the old team, or wholly to the new team), not by an unspecified default.
WHY_IT_MATTERS: >
  Without an explicit rule, the same reassignment could produce a different reported figure depending purely on how the underlying system happens to process it, with no one able to say which figure is correct.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical mid-period reassignments produce different attributions of the individual's contribution with no identifiable rule explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Reassign an individual mid-period between teams and check which explicit rule, if any, governs how their contribution up to that point is attributed.
```

## G08-SALES_TEAM-Q007

```yaml
QID: G08-SALES_TEAM-Q007
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Archiving a team that still has open (unconfirmed or unfulfilled) orders does not silently detach those orders from their team attribution.
WHY_IT_MATTERS: >
  An order stripped of its team attribution on archival would become unowned at the organisational level even while commercially still active, with no one accountable for progressing it.
DISCONFIRMING_OBSERVATION: >
  Archiving a team with open orders removes or blanks the team attribution recorded on those still-open orders.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Archive a team that has at least one open order and check whether that order's team attribution is preserved.
```

## G08-SALES_TEAM-Q008

```yaml
QID: G08-SALES_TEAM-Q008
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Orders still open against an archived team can either still be progressed through confirmation, delivery and invoicing, or are explicitly blocked from progressing, as a defined rule rather than an accidental side effect of the archival action.
WHY_IT_MATTERS: >
  An accidental side effect, rather than a deliberate rule, means the outcome for in-flight work could differ unpredictably from one archival to the next with no one having actually decided it should.
DISCONFIRMING_OBSERVATION: >
  Archiving a team causes its open orders to become unable to progress, or to progress without restriction, with no identifiable rule governing which outcome applies.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Archive a team with an open order and attempt to progress that order through its next lifecycle step, checking whether the outcome matches a defined rule.
```

## G08-SALES_TEAM-Q009

```yaml
QID: G08-SALES_TEAM-Q009
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A target or quota is defined against an explicit measurement-date basis (order date, delivery date, or invoice date), and this basis is a stored, inspectable configuration rather than an assumption applied inconsistently across reports.
WHY_IT_MATTERS: >
  An inconsistent, assumed basis would let two reports drawing on the same underlying orders attribute the same figure to two different periods with no way to reconcile them.
DISCONFIRMING_OBSERVATION: >
  Two reports on the same target, both claiming to use the same measurement basis, attribute the same order to different periods.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Inspect the stored measurement-date basis for a configured target and generate two reports spanning a period boundary to check whether both attribute a boundary-crossing order consistently.
```

## G08-SALES_TEAM-Q010

```yaml
QID: G08-SALES_TEAM-Q010
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When an order counted toward a target is later cancelled, the target figure is restated to remove that order's contribution rather than permanently retaining credit for a commitment that no longer exists.
WHY_IT_MATTERS: >
  Retaining credit for a cancelled commitment would let a target figure overstate genuine performance indefinitely, with no mechanism ever correcting it.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order that had already counted toward a target leaves that target's reported figure unchanged.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an order that counts toward a target, note the target figure, cancel the order, and check whether the target figure is restated.
```

## G08-SALES_TEAM-Q011

```yaml
QID: G08-SALES_TEAM-Q011
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A partial cancellation (some lines cancelled, others retained) restates the target contribution proportionally rather than removing or retaining the order's entire original contribution.
WHY_IT_MATTERS: >
  Treating a partial cancellation as though it were total, in either direction, would either overstate performance on what was actually cancelled or understate it on what was genuinely retained.
DISCONFIRMING_OBSERVATION: >
  Partially cancelling some lines of an order that counts toward a target either leaves the full original contribution unchanged or removes the entire contribution rather than adjusting it proportionally.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Partially cancel some but not all lines of a target-counting order and check whether the target restatement is proportional to what was actually cancelled.
```

## G08-SALES_TEAM-Q012

```yaml
QID: G08-SALES_TEAM-Q012
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Visibility of one team's pipeline (open, unconfirmed orders) to members of a different team is governed by an explicit configuration, not granted by default to every authenticated user.
WHY_IT_MATTERS: >
  Default visibility across every team's pipeline would remove any meaningful boundary between teams, regardless of whether cross-team visibility was ever intended.
DISCONFIRMING_OBSERVATION: >
  A member of one team can see another team's open pipeline with no cross-team visibility grant having been explicitly configured.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  As a member of one team with no explicit cross-team grant, attempt to view another team's open pipeline.
```

## G08-SALES_TEAM-Q013

```yaml
QID: G08-SALES_TEAM-Q013
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Visibility of margin or cost figures on another team's orders is governed by a permission distinct from visibility of that order's existence and its committed price and quantity.
WHY_IT_MATTERS: >
  Bundling margin visibility with ordinary order visibility would expose sensitive cost data to anyone merely allowed to see that an order exists at all.
DISCONFIRMING_OBSERVATION: >
  A user granted visibility into another team's order records, but not separately granted margin visibility, can nonetheless see that order's cost or margin figures.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user with cross-team order visibility but no separate margin-visibility grant, attempt to view another team's order margin figures.
```

## G08-SALES_TEAM-Q014

```yaml
QID: G08-SALES_TEAM-Q014
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A team manager's access to the records of every member of their own team is broader than an individual member's access to peers' records within the same team, as an explicit role distinction rather than an incidental effect of shared team membership.
WHY_IT_MATTERS: >
  Without an explicit distinction, either every ordinary member would see everything a manager sees, or a manager would see no more than an ordinary peer, neither of which reflects a real management role.
DISCONFIRMING_OBSERVATION: >
  An ordinary team member has access to every peer's individual records identical to what the team's manager has access to.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Compare an ordinary team member's access to peers' individual order records against the team manager's access to the same records.
```

## G08-SALES_TEAM-Q015

```yaml
QID: G08-SALES_TEAM-Q015
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A team manager's elevated access does not extend to another team's records unless an explicit cross-team or organisation-wide role is separately granted.
WHY_IT_MATTERS: >
  Elevated access bleeding across teams by default would make the manager role a de facto organisation-wide role for everyone who holds it, whether or not that was ever intended.
DISCONFIRMING_OBSERVATION: >
  A manager of one team, with no cross-team or organisation-wide role granted, is nonetheless able to access another team's records at the same elevated level.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  As a manager of one team with no cross-team role, attempt to access another team's records at the same level available on your own team.
```

## G08-SALES_TEAM-Q016

```yaml
QID: G08-SALES_TEAM-Q016
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reassigning many orders from one individual or team to another in a single bulk action leaves an auditable record of the prior attribution for each affected order, not only the new value.
WHY_IT_MATTERS: >
  Without the prior value retained, a bulk change could not be reviewed or reversed, since there would be no way to know what any individual order's attribution had actually been beforehand.
DISCONFIRMING_OBSERVATION: >
  A bulk reassignment overwrites each affected order's attribution with no retrievable record of what it was immediately before the bulk action.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform a bulk reassignment across several orders and attempt to retrieve, for one affected order, the attribution it carried immediately before the bulk action.
```

## G08-SALES_TEAM-Q017

```yaml
QID: G08-SALES_TEAM-Q017
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A bulk reassignment applied while some of the affected orders are locked or already fully invoiced either skips those orders with a recorded exception, or handles them under an explicit rule, rather than silently reassigning historical attribution on closed records.
WHY_IT_MATTERS: >
  Silently rewriting attribution on a closed, fully settled record would alter the historical account of who actually handled a transaction that has already run its course.
DISCONFIRMING_OBSERVATION: >
  A bulk reassignment changes the recorded attribution on an already-locked or fully-invoiced order with no exception raised and no rule identifiable for why it was included.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Include an already-locked or fully-invoiced order in a bulk reassignment batch and check whether it is skipped, exception-flagged, or silently reassigned.
```

## G08-SALES_TEAM-Q018

```yaml
QID: G08-SALES_TEAM-Q018
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A team that spans more than one company has its cross-company scope explicitly configured, rather than a team created under one company silently gaining visibility into another company's orders.
WHY_IT_MATTERS: >
  Silent cross-company visibility would defeat the separation each company's own records are meant to have, purely as a side effect of how a team happened to be set up.
DISCONFIRMING_OBSERVATION: >
  A team created under a single company can see orders belonging to a different company with no explicit multi-company scope having been configured for it.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Create a team scoped to a single company and check whether it can see orders belonging to a different company with no additional configuration applied.
```

## G08-SALES_TEAM-Q019

```yaml
QID: G08-SALES_TEAM-Q019
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  An order created under a team that spans multiple companies is still attributed to a single determining company for accounting and numbering purposes, not left ambiguous between the companies the team spans.
WHY_IT_MATTERS: >
  An order with no single determining company would be unable to receive a coherent number or be posted to a coherent set of books, since both depend on knowing exactly which company the transaction belongs to.
DISCONFIRMING_OBSERVATION: >
  An order raised under a multi-company team cannot be resolved to a single determining company for numbering or posting purposes.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Raise an order under a team spanning two companies and check whether the order resolves to one specific company for numbering and posting.
```

## G08-SALES_TEAM-Q020

```yaml
QID: G08-SALES_TEAM-Q020
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An order created with no team attribution at all is still valid and processable, and is identifiable afterward as unattributed rather than being silently defaulted to an arbitrary team with no record that a default was applied.
WHY_IT_MATTERS: >
  A silent, unrecorded default would make an order look deliberately assigned to a team that, in fact, no one ever chose, misrepresenting who actually owns it.
DISCONFIRMING_OBSERVATION: >
  An order created with no team attribution is later found to carry a specific team's attribution with no record of a default rule having been applied.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create an order with no team attribution and later inspect its record for a team value and for any trace of how that value arose.
```

## G08-SALES_TEAM-Q021

```yaml
QID: G08-SALES_TEAM-Q021
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where a default team is configured for orders left unattributed, that default is an explicit, inspectable configuration value rather than an implicit fallback with no record of which rule produced it.
WHY_IT_MATTERS: >
  An implicit, unrecorded fallback could not be reviewed, changed deliberately, or even confirmed to be operating as intended, since there would be nothing to point to as the source of the behaviour.
DISCONFIRMING_OBSERVATION: >
  Unattributed orders are consistently assigned to the same team with no configuration value anywhere identifiable as the source of that default.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Locate the configuration governing the default team for unattributed orders and confirm it is an inspectable, explicit value rather than inferred behaviour.
```

## G08-SALES_TEAM-Q022

```yaml
QID: G08-SALES_TEAM-Q022
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When two individuals have both contributed to a single order (for example, one attributed as opener and another as closer), the order's commission or credit is split according to an explicit rule rather than both being credited the full value or only one being credited with no trace of the other's involvement.
WHY_IT_MATTERS: >
  Crediting both in full would overstate combined performance, crediting only one erases a real contributor's involvement entirely, and either failure makes commission and recognition figures untrustworthy.
DISCONFIRMING_OBSERVATION: >
  An order with two contributing individuals shows the full value credited to both, or credited to only one with no record that a second individual was involved at all.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record two individuals as contributors to a single order and check how the order's value is split, or not split, between them.
```

## G08-SALES_TEAM-Q023

```yaml
QID: G08-SALES_TEAM-Q023
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A change to which individual is credited for an order after it has already contributed to a settled commission or target period leaves that prior period's figures unchanged, affecting attribution only going forward, unless an explicit retroactive correction is separately invoked.
WHY_IT_MATTERS: >
  Automatically rewriting an already-settled period would make a settled figure meaningless, since it could still change later purely because of an unrelated administrative correction made afterward.
DISCONFIRMING_OBSERVATION: >
  Changing an order's credited individual after its contributing period has already settled alters that already-settled period's reported figure with no explicit retroactive correction having been invoked.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change the credited individual on an order after its contribution has already settled into a closed period, and check whether that closed period's figure changes.
```

## G08-SALES_TEAM-Q024

```yaml
QID: G08-SALES_TEAM-Q024
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A report that aggregates figures by team reflects the team attribution recorded on each order at the time the report is generated; when a later reassignment changes an order's team, a previously generated and distributed report is not silently altered to match, and the resulting discrepancy is identifiable.
WHY_IT_MATTERS: >
  If a distributed report silently changed after the fact, no one who had already acted on it could trust that the figures they saw were the figures that actually existed at that time.
DISCONFIRMING_OBSERVATION: >
  A report already generated and distributed changes its own recorded figures after a later reassignment, with no way to identify that a discrepancy now exists between the two.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate and retain a team-aggregated report, reassign an order included in it to a different team, and check whether the retained report's figures change or a discrepancy becomes identifiable.
```

## G08-SALES_TEAM-Q025

```yaml
QID: G08-SALES_TEAM-Q025
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Re-running the same team-aggregated report after a reassignment produces a different figure for the affected teams than the original report did, and the difference is attributable specifically to the reassignment rather than to any other change.
WHY_IT_MATTERS: >
  If the difference could not be attributed to the specific reassignment, no one reconciling two versions of the same report could explain why the numbers moved.
DISCONFIRMING_OBSERVATION: >
  Re-running the same team-aggregated report after a reassignment produces an identical figure to the original, or a different figure with no way to attribute the change to the reassignment specifically.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate a team-aggregated report, reassign one contributing order, re-run the same report, and check whether the resulting difference is attributable to that specific reassignment.
```

## G08-SALES_TEAM-Q026

```yaml
QID: G08-SALES_TEAM-Q026
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Team membership (who belongs to a team) is a distinct configuration from team-level target or quota configuration, so that adding or removing a member does not itself alter an already-set team target.
WHY_IT_MATTERS: >
  If membership and target configuration were entangled, a routine staffing change could silently move a target figure that management believed had been deliberately and separately set.
DISCONFIRMING_OBSERVATION: >
  Adding or removing a member from a team changes that team's already-configured target figure with no separate action taken on the target itself.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Set a team's target, then add or remove a member from that team, and check whether the target figure changed as a side effect.
```

## G08-SALES_TEAM-Q027

```yaml
QID: G08-SALES_TEAM-Q027
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  An individual who is a member of more than one team at the same time has each of their orders attributed to a single determining team per order, rather than that order counting toward every team the individual belongs to.
WHY_IT_MATTERS: >
  An order counting toward multiple teams at once would inflate every team's combined figure by the same underlying transaction, overstating total performance across the organisation.
DISCONFIRMING_OBSERVATION: >
  An order raised by an individual belonging to two teams simultaneously is counted toward both teams' aggregate figures.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have an individual who belongs to two teams raise a single order and check whether it is counted toward one team's aggregate figure or both.
```

## G08-SALES_TEAM-Q028

```yaml
QID: G08-SALES_TEAM-Q028
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Removing an individual from a team does not retroactively remove that individual's attribution from orders already recorded under that team while they were a member.
WHY_IT_MATTERS: >
  Retroactively stripping attribution would erase the historical record of who actually handled a transaction, purely because of a later, unrelated staffing change.
DISCONFIRMING_OBSERVATION: >
  Removing an individual from a team changes the recorded attribution on that individual's orders that were created while they were still a member.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Remove an individual from a team after they have already created orders as a member, and check whether those existing orders' attribution changes.
```

## G08-SALES_TEAM-Q029

```yaml
QID: G08-SALES_TEAM-Q029
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An individual's account deactivated or removed from the system entirely leaves their historical order attribution intact and identifiable, rather than the orders becoming attributed to no one or reassigned automatically with no record.
WHY_IT_MATTERS: >
  Losing historical attribution when an account is deactivated would make it impossible, afterward, to know who actually handled a set of past transactions.
DISCONFIRMING_OBSERVATION: >
  Deactivating or removing an individual's account clears or automatically reassigns the attribution on their historical orders with no retrievable trace of the original attribution.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deactivate or remove an individual's account who has historical orders, and check whether those orders retain an identifiable, original attribution.
```

## G08-SALES_TEAM-Q030

```yaml
QID: G08-SALES_TEAM-Q030
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A team's designated leader or manager role is a distinct, explicit assignment rather than being inferred from seniority, join date, or any other implicit signal.
WHY_IT_MATTERS: >
  An inferred manager role could change unpredictably as membership changes, handing elevated access to whoever happens to satisfy the inferred signal rather than to someone deliberately appointed.
DISCONFIRMING_OBSERVATION: >
  A team's manager-level access is held by whichever member currently has the longest tenure or earliest join date, rather than by an explicitly designated individual.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Change a team's membership order or tenure without making any explicit manager assignment, and check whether manager-level access shifts to a different member as a result.
```

## G08-SALES_TEAM-Q031

```yaml
QID: G08-SALES_TEAM-Q031
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Changing a team's manager does not alter the historical record of who approved or was attributed on orders already handled under the prior manager.
WHY_IT_MATTERS: >
  Rewriting historical approval attribution to match a newly appointed manager would misrepresent who actually made past decisions on the team's behalf.
DISCONFIRMING_OBSERVATION: >
  Replacing a team's manager changes the recorded approver or attribution on orders that were already handled under the prior manager.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Handle and record approval on an order under one team manager, replace that manager, and check whether the prior order's recorded approver changes.
```

## G08-SALES_TEAM-Q032

```yaml
QID: G08-SALES_TEAM-Q032
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A user without membership in a given team, and without an explicit cross-team role, cannot confirm or edit an order attributed to that team through the ordinary order-management path.
WHY_IT_MATTERS: >
  Without this boundary, team attribution would carry no actual access consequence, and any authenticated user could act on any team's commitments regardless of their own assignment.
DISCONFIRMING_OBSERVATION: >
  A user with no membership or cross-team role for a given team is nonetheless able to confirm or edit an order attributed to that team.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user with no membership or cross-team role for a specific team, attempt to confirm or edit an order attributed to that team.
```

## G08-SALES_TEAM-Q033

```yaml
QID: G08-SALES_TEAM-Q033
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An order's team attribution can be changed after confirmation only through an explicit action distinct from ordinary field editing, and that action leaves an auditable trace.
WHY_IT_MATTERS: >
  If team reattribution were indistinguishable from any other field edit, a change to who organisationally owns a confirmed commitment could pass unnoticed among routine edits.
DISCONFIRMING_OBSERVATION: >
  Changing a confirmed order's team attribution through the ordinary editing path leaves no trace distinguishable from any other routine field edit.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change a confirmed order's team attribution and check whether the resulting audit trail distinguishes it from an ordinary field edit.
```

## G08-SALES_TEAM-Q034

```yaml
QID: G08-SALES_TEAM-Q034
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Target measurement configured on invoice date rather than order date produces a materially different in-period figure for an order confirmed in one period but invoiced in a later one, and this basis is applied consistently across every report drawing on the same target.
WHY_IT_MATTERS: >
  Inconsistent application of the measurement basis across reports would let the same underlying target be represented by two different figures depending purely on which report happened to be consulted.
DISCONFIRMING_OBSERVATION: >
  Two different reports drawing on the same invoice-date-based target attribute the same period-crossing order to two different periods.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Confirm an order in one period, invoice it in a later period, and compare how two separate reports drawing on the same target attribute that order's period.
```

## G08-SALES_TEAM-Q035

```yaml
QID: G08-SALES_TEAM-Q035
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An order confirmed near a period boundary and invoiced just after it is attributed to the period matching its configured measurement basis, not to whichever period the report happens to be run closest to.
WHY_IT_MATTERS: >
  If the run date of the report, rather than the configured basis, determined the period, the same order could shift between periods purely because of when someone chose to look at it.
DISCONFIRMING_OBSERVATION: >
  Running the same period report on different dates changes which period a fixed, boundary-crossing order is attributed to.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an order near a period boundary, invoice it just after, and run the relevant period report on two different dates to check whether the order's attributed period changes.
```

## G08-SALES_TEAM-Q036

```yaml
QID: G08-SALES_TEAM-Q036
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A quota or target figure exposed to an individual or team reflects only orders that individual or team is actually authorized to see, and does not leak the existence or value of another team's contributing orders through an aggregate total.
WHY_IT_MATTERS: >
  An aggregate that leaks another team's underlying figures would defeat the entire purpose of restricting visibility at the individual-order level, since the same information would still be recoverable through the total.
DISCONFIRMING_OBSERVATION: >
  An individual with no visibility into another team's orders can nonetheless infer that team's contributing value from an aggregate target figure exposed to them.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user with no cross-team visibility, examine an aggregate target figure that includes another team's contribution and check whether that team's value can be inferred from it.
```

## G08-SALES_TEAM-Q037

```yaml
QID: G08-SALES_TEAM-Q037
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A newly created team starts with no historical orders attributed to it, and any pre-existing orders become attributed to it only through an explicit reassignment, never through an automatic backfill tied merely to matching criteria.
WHY_IT_MATTERS: >
  An automatic backfill would let a brand-new team suddenly inherit historical performance it had no actual role in producing, misrepresenting its own track record from the moment it exists.
DISCONFIRMING_OBSERVATION: >
  A newly created team shows pre-existing historical orders attributed to it with no explicit reassignment action having been taken.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a new team and check whether any pre-existing order becomes attributed to it without an explicit reassignment action.
```

## G08-SALES_TEAM-Q038

```yaml
QID: G08-SALES_TEAM-Q038
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Deleting a team (as opposed to archiving it) that still has historical orders attributed to it is either blocked while those historical references exist, or the historical orders retain an identifiable attribution after deletion rather than losing their team reference entirely.
WHY_IT_MATTERS: >
  Losing the team reference entirely would strip historical orders of organisational context with no way to recover who, at the team level, had actually handled them.
DISCONFIRMING_OBSERVATION: >
  Deleting a team with historical orders attached succeeds and leaves those historical orders with no identifiable team reference at all.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Attempt to delete a team that has historical orders attributed to it and check whether the deletion is blocked or those orders retain an identifiable reference.
```

## G08-SALES_TEAM-Q039

```yaml
QID: G08-SALES_TEAM-Q039
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A commission or credit split configured between two individuals on an order is captured at a specific point (order confirmation) and does not silently recompute if the underlying split-rule configuration changes afterward.
WHY_IT_MATTERS: >
  A silently recomputing split would change how a specific, already-confirmed order's credit is divided purely because of an unrelated configuration change made later, with neither individual having agreed to the new split.
DISCONFIRMING_OBSERVATION: >
  Changing the general commission-split rule configuration after an order is confirmed changes the credit split already captured for that specific, already-confirmed order.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Confirm an order with a captured commission split between two individuals, change the general split-rule configuration, and check whether the already-confirmed order's split changes.
```

## G08-SALES_TEAM-Q040

```yaml
QID: G08-SALES_TEAM-Q040
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Visibility scope (which orders a user can see) and target/quota scope (which orders count toward a user's own number) are governed by two distinct configurations, so a user can see an order without it counting toward their target, or the reverse.
WHY_IT_MATTERS: >
  Entangling the two would force every visibility grant to also be a performance-crediting decision, or every crediting decision to also expose full order visibility, when the two are legitimately separate business needs.
DISCONFIRMING_OBSERVATION: >
  A user granted visibility into an order for reference purposes only has that order counted toward their personal target with no separate crediting decision made.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Grant a user visibility into an order that is not meant to count toward their own target, and check whether it nonetheless appears in their target figure.
```

## G08-SALES_TEAM-Q041

```yaml
QID: G08-SALES_TEAM-Q041
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A user with visibility into another team's pipeline through an explicit cross-team grant does not thereby gain the ability to edit or confirm orders belonging to that other team.
WHY_IT_MATTERS: >
  Visibility and edit rights are different kinds of access, and collapsing them would mean every cross-team reporting or oversight grant also silently hands out unintended control over another team's live commitments.
DISCONFIRMING_OBSERVATION: >
  A user granted cross-team visibility, with no separate edit or confirm right, is nonetheless able to edit or confirm an order belonging to the visible team.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user with a cross-team visibility grant only, attempt to edit or confirm an order belonging to the team you can see but not manage.
```

## G08-SALES_TEAM-Q042

```yaml
QID: G08-SALES_TEAM-Q042
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Two teams within the same company, each with their own configured target, do not have their targets or pipeline figures silently combined into a single company-wide number in a way that makes team-level performance unrecoverable.
WHY_IT_MATTERS: >
  If the two teams' figures could not be recovered separately once combined, no one could evaluate either team's actual performance independently, defeating the purpose of tracking targets at the team level at all.
DISCONFIRMING_OBSERVATION: >
  A company-wide target figure combining two teams cannot be broken back down into each team's separate contribution.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate a company-wide aggregate figure spanning two teams with separately configured targets and attempt to recover each team's individual contribution from it.
```

## G08-SALES_TEAM-Q043

```yaml
QID: G08-SALES_TEAM-Q043
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A team's default currency or company scope, where configured, governs newly created orders raised under that team without altering the currency or company already recorded on the team's pre-existing orders.
WHY_IT_MATTERS: >
  Retroactively altering pre-existing orders' currency or company would rewrite the terms of transactions that had already been agreed under different conditions.
DISCONFIRMING_OBSERVATION: >
  Changing a team's default currency or company scope alters the currency or company already recorded on that team's pre-existing orders.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change a team's default currency or company-scope configuration and check whether the team's pre-existing orders' recorded currency or company changed.
```

## G08-SALES_TEAM-Q044

```yaml
QID: G08-SALES_TEAM-Q044
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Bulk-reassigning orders across a currency or company boundary between two teams triggers an explicit exception or conversion rule rather than silently changing the order's recorded currency or company to match the new team.
WHY_IT_MATTERS: >
  Silently changing a financial attribute like currency or company as a side effect of an organisational reassignment would alter the transaction's actual financial terms without anyone deliberately deciding to.
DISCONFIRMING_OBSERVATION: >
  Bulk-reassigning an order to a team scoped to a different currency or company silently changes the order's own recorded currency or company with no exception raised.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Bulk-reassign an order to a team scoped to a different currency or company and check whether the order's own currency or company field changes silently or an exception is raised.
```

## G08-SALES_TEAM-Q045

```yaml
QID: G08-SALES_TEAM-Q045
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An order manually reassigned away from the team that a rule-based (automatic) assignment would otherwise have selected does not silently revert to the rule-based team on a later, unrelated edit to that order.
WHY_IT_MATTERS: >
  A silent reversion would undo a deliberate manual correction purely as a side effect of an unrelated edit, with no one having decided to reverse the original reassignment.
DISCONFIRMING_OBSERVATION: >
  Making an unrelated edit to a manually reassigned order causes its team attribution to revert to the automatic, rule-based team.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Manually reassign an order away from its automatic rule-based team, make an unrelated edit to the order, and check whether the team attribution reverts.
```

## G08-SALES_TEAM-Q046

```yaml
QID: G08-SALES_TEAM-Q046
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Automatic team-assignment rules (where configured, for example by territory or product) are inspectable as explicit configuration, and a specific order's assignment can be traced to the rule that produced it or to a manual override that superseded it.
WHY_IT_MATTERS: >
  Without traceability, no one could distinguish an order that landed on a team purely by an automatic rule from one that was deliberately placed there by a manual decision.
DISCONFIRMING_OBSERVATION: >
  An order's team assignment cannot be traced to either the specific automatic rule that produced it or a manual override that superseded it.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Trigger an automatic team-assignment rule on one order and a manual override on another, then attempt to trace each order's assignment back to its cause.
```

## G08-SALES_TEAM-Q047

```yaml
QID: G08-SALES_TEAM-Q047
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  An individual who leaves the organisation but whose historical orders remain has those orders still counted correctly in closed, historical target and period reports, distinguishing an individual who is no longer active from one who never existed in the record at all.
WHY_IT_MATTERS: >
  Treating a departed individual's historical contribution as though it never existed would understate the actual performance recorded during the period they were genuinely active.
DISCONFIRMING_OBSERVATION: >
  Removing an individual from the organisation causes their previously counted contribution to disappear from an already-closed historical period report.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Close a period report that includes a since-departed individual's contribution, remove that individual from the organisation, and re-check whether the closed report's figure changed.
```

## G08-SALES_TEAM-Q048

```yaml
QID: G08-SALES_TEAM-Q048
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The organisational team or owner attribution recorded on an order is independent of, and does not alter, the commercial content of the order itself (its lines, prices, and quantities).
WHY_IT_MATTERS: >
  If organisational attribution could alter commercial content, a purely administrative reassignment could unintentionally change what was actually promised to the customer.
DISCONFIRMING_OBSERVATION: >
  Reassigning an order's team or owner changes one of its lines, prices, or quantities as a side effect.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reassign an order's team or owner and compare its lines, prices, and quantities before and after to check for any unintended change.
```

## G08-SALES_TEAM-Q049

```yaml
QID: G08-SALES_TEAM-Q049
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Concurrent bulk-reassignment actions run by two different managers over overlapping sets of orders do not leave some orders with an inconsistent or partially applied attribution with no record of which action actually took effect.
WHY_IT_MATTERS: >
  An unrecorded, inconsistent outcome would leave overlapping orders in an unpredictable state that neither manager could explain or correct, since neither could tell which of the two actions had actually applied.
DISCONFIRMING_OBSERVATION: >
  Two overlapping bulk-reassignment actions run at the same time leave some orders with an attribution that matches neither action cleanly, with no record of which action took effect.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Run two overlapping bulk-reassignment actions targeting some of the same orders at the same time and check the resulting attribution and audit trail on the overlapping orders.
```

## G08-SALES_TEAM-Q050

```yaml
QID: G08-SALES_TEAM-Q050
MODULE: sales_team
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A team scoped to one company cannot be selected as the team on an order being raised under a different company without an explicit cross-company grant, mirroring the same boundary enforced on price lists and orders themselves.
WHY_IT_MATTERS: >
  Without this boundary, an order could be organisationally attributed to a team that has no legitimate standing in the company under which the order is actually being raised.
DISCONFIRMING_OBSERVATION: >
  An order raised under one company can select a team scoped to a different company with no cross-company grant configured for that team.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to select a team scoped to a different company on an order being raised under a company for which that team has no explicit cross-company grant.
```
