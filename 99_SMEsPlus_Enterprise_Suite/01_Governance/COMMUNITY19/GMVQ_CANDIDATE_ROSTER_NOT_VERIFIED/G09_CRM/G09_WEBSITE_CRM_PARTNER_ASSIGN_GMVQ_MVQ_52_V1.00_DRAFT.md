# SMEsPlus ENTERPRISE SUITE
## GMVQ — G09 CRM / website_crm_partner_assign Module Adversarial MVQ Bank

**Document ID:** GMVQ-G09-WEBSITE_CRM_PARTNER_ASSIGN-MVQ52-V1.00
**Group:** G09 CRM
**Module Metadata:** `website_crm_partner_assign`
**Wave:** W2
**Author Cell:** P-C6 (GMVQ Question Factory — Wave W2 Acceleration, 25-Team Programme)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 52
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 52 = 107
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `website_crm_partner_assign` — the seam where a
web-sourced opportunity is routed OUT of the business to an external partner company: a distinct
legal entity that is not an employee, not a tenant user, and carries its own commercial interests.
Everything the base opportunity record already owns — pipeline stage, expected value, activities,
merge and duplicate handling, the lead-to-opportunity boundary — belongs to the `crm` base bank and
is deliberately not re-asked here. This bank asks only what happens at the handoff itself: what the
partner can see and whether it is exactly what the handoff intended; what happens when a partner
declines, ignores, or never answers, and how long the business waits before it can act; a lead
reclaimed after the partner has already made contact; the same lead visible to, or reachable by,
more than one partner; grade, territory, and specialism driving routing, and what a change to that
routing rule does to leads already assigned under the old one; a partner whose agreement has lapsed
still receiving leads; routing decided from a submitter-supplied location or language that may be
wrong; a partner's self-reported outcome that the business cannot itself verify, and what turns on
that claim; the submitter's personal data crossing into another legal entity — the recorded basis
for that, whether the submitter was told, and what an erasure request does once the data has already
moved; the partner's own staff accessing the record and what happens to that access when someone
leaves; the audit trail of who assigned a lead, when, and under which rule version; a partner record
itself being archived or merged while leads are open with it; and a business running several
companies, each with its own separate partner network. Every question was tested against the bridge
rule: if it would read equally well with no external partner in the picture at all, it was cut.

The question text is source-neutral and does not expose vendor model names, field names, methods,
schema, XML IDs, API shapes, or implementation algorithms. `MODULE: website_crm_partner_assign`
appears only in the structured metadata field, never inside question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that states a concrete failure state.
- No padding: 52 questions exist because they test 52 distinct material hypotheses at the seam.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `module + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
- BRIDGE MODULE per GMVQ_BRIDGE_MODULE_RULE_V1.00: every question fails only at the seam between a
  web-sourced opportunity and the external partner it is routed to. None restates a `crm` base
  invariant (stage, value, activity, merge, duplicate handling) that holds with no external partner
  present, and none is a generic third-party-data-sharing question that would apply regardless of
  this specific handoff.
- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' G09_CRM/*.md | sort` was
  run against `01_QUESTION_BANKS/G09_CRM/` before authoring. No sibling bank exists yet in that
  directory — this is the first bank issued for G09 — so no overlap check against existing G09
  content was possible; that is recorded here as a fact, not concealed. The `crm` base module's own
  ground (pipeline, assignment/reassignment, won/lost, duplicates, activities) is treated as
  reserved to the base bank and avoided on that basis alone.
- Privacy is treated as first-class per GROUP_BRIEF_G09_CRM.md: consent, retention, disclosure to a
  third party, and subject access are covered directly in this bank (Q040–Q045) rather than deferred
  to a separate privacy module.

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q001

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q001
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The information made visible to an external partner about a routed lead is limited to what the
  handoff requires — the submitter's own contact and enquiry details — and excludes anything not
  necessary to act on that specific lead.
WHY_IT_MATTERS: >
  An external partner is a separate commercial entity; excess exposure hands a third party more of
  the business's data than the handoff justifies, without anyone having chosen that.
DISCONFIRMING_OBSERVATION: >
  A partner viewing one assigned lead can also see information about the submitter, the business,
  or other records that was never part of what was routed to them.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Route a single lead to a partner and, acting as that partner, inspect everything the record view
  exposes beyond the specific enquiry fields.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q002

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q002
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A partner's view of a routed lead does not extend to other enquiries, opportunities, or pipeline
  records the same submitter has with the business that were not routed to that partner.
WHY_IT_MATTERS: >
  Leaking the submitter's wider relationship with the business to one partner exposes competitive or
  commercial information the submitter never consented to share with that party.
DISCONFIRMING_OBSERVATION: >
  Viewing one assigned lead's record surfaces or links to another opportunity or enquiry from the
  same submitter that was not assigned to that partner.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create two separate enquiries from the same submitter, route only one to a partner, and check
  whether the partner's view of the routed one reaches the other.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q003

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q003
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Internal annotations, qualification notes, or scoring recorded by the business's own staff before
  or after the handoff are not shown to the external partner.
WHY_IT_MATTERS: >
  Internal assessments, such as how promising or low-value the business privately judged the lead,
  are commercially sensitive and were never meant for a third party's eyes.
DISCONFIRMING_OBSERVATION: >
  A note, tag, or score entered by internal staff for internal use appears in the record view
  available to the assigned partner.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Add an internal-only note or score to a lead before routing it to a partner, then inspect the
  partner-facing view for the same record.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q004

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q004
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A partner user can see only the leads assigned to their own partner company, never leads assigned
  to a different partner.
WHY_IT_MATTERS: >
  Cross-partner visibility hands one commercial competitor visibility into another's active leads.
DISCONFIRMING_OBSERVATION: >
  A user acting for one partner can retrieve, list, or navigate to a lead currently assigned to a
  different partner.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  Assign two leads to two different partners and, acting as one partner's user, attempt to reach the
  other partner's lead by direct access or by listing.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q005

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q005
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Once a lead is reclaimed away from a partner, that partner's ability to view or act on the record
  ends at the point of reclaim, not some indeterminate time later.
WHY_IT_MATTERS: >
  Continued access after reclaim is an unauthorized retention of an external party's visibility into
  data that is no longer theirs to act on.
DISCONFIRMING_OBSERVATION: >
  A partner whose assignment was reclaimed can still open, edit, or export the lead's record after
  the reclaim is recorded.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Reclaim a lead from a partner and, acting as that partner, attempt to open the same record
  immediately afterward.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q006

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q006
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A partner is never shown which other partner company was previously, or is concurrently,
  considered or assigned for the same lead.
WHY_IT_MATTERS: >
  Revealing a competitor's involvement to another partner damages both the submitter's and the other
  partner's commercial position.
DISCONFIRMING_OBSERVATION: >
  A partner's record view or history for a lead names or otherwise identifies a different partner
  company that held or was considered for the same assignment.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Move a lead from one partner to another and, acting as the second partner, inspect the record's
  history for any trace of the first.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q007

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q007
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The submitter's message and communication history shared with a partner is limited to what
  pertains to the specific lead routed, not the submitter's full communication history with the
  business.
WHY_IT_MATTERS: >
  Sharing an entire relationship history for the sake of routing one enquiry is a disproportionate
  transfer of personal data.
DISCONFIRMING_OBSERVATION: >
  A partner viewing one routed lead can see messages, calls, or interactions unrelated to that
  specific enquiry.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Build a submitter's history from more than one unrelated interaction, route only one lead to a
  partner, and inspect what communication history is visible on that routed record.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q008

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q008
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Fields on the submitter's record that are unrelated to acting on the routed lead are not surfaced
  in the partner-facing view.
WHY_IT_MATTERS: >
  Exposing more personal data than the handoff needs increases the business's data-protection
  exposure without a compensating business reason.
DISCONFIRMING_OBSERVATION: >
  A partner-facing view of a routed lead includes a personal-data field that has no bearing on
  contacting or servicing that lead.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Populate the submitter's broader record with data unrelated to the enquiry, route the lead, and
  check the partner-facing view for that unrelated data.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q009

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q009
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An unanswered or declined lead becomes eligible for reclaim and rerouting after a defined, bounded
  waiting period, not only at someone's discretion with no time bound.
WHY_IT_MATTERS: >
  An unbounded wait leaves a live commercial enquiry stalled indefinitely with no one accountable for
  moving it forward.
DISCONFIRMING_OBSERVATION: >
  A lead with no partner response sits assigned with no available action to reclaim it and no
  elapsed-time trigger ever fires.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Route a lead to a partner, let it go unanswered, and observe whether any bounded period exists
  after which reclaim becomes possible or automatic.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q010

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q010
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A partner that neither accepts, declines, nor contacts the submitter does not retain the
  assignment indefinitely as though nothing were wrong.
WHY_IT_MATTERS: >
  Silent non-response is functionally identical to losing the lead, and treating it as still handled
  hides an unserved customer from the business.
DISCONFIRMING_OBSERVATION: >
  A lead assigned to an unresponsive partner shows no distinguishable at-risk or overdue status weeks
  after assignment, and nothing about its state differs from a lead that was actively worked.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Assign a lead to a partner, take no action as that partner for an extended period, and compare its
  visible state to a lead that received prompt contact.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q011

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q011
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An explicit decline by a partner is recorded as a distinct event from a reclaim triggered purely
  by the elapse of time with no response.
WHY_IT_MATTERS: >
  Conflating an active refusal with mere inaction destroys the ability to later tell whether a
  partner is unreliable or was simply never reached.
DISCONFIRMING_OBSERVATION: >
  The record left behind by an explicit decline is indistinguishable from the record left behind by
  a timeout-triggered reclaim.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce one lead declined outright and one lead reclaimed only after the wait period elapses, then
  compare the two resulting records.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q012

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q012
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reclaiming an unanswered lead from a partner does not erase the fact that it was originally
  assigned to that partner and for how long.
WHY_IT_MATTERS: >
  Losing that history removes the only evidence by which a partner's responsiveness could ever be
  evaluated.
DISCONFIRMING_OBSERVATION: >
  After a reclaim, no trace remains in the record of which partner previously held the lead or for
  how long.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reclaim a lead from an unresponsive partner and inspect the record afterward for evidence of the
  original assignment.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q013

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q013
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When a reclaimed lead is rerouted, it goes back through the same routing logic as a fresh lead
  unless a person deliberately overrides that, and the override is recorded as such.
WHY_IT_MATTERS: >
  An ungoverned manual reroute after reclaim quietly bypasses whatever grading, territory, or
  fairness rule the business relies on for routing.
DISCONFIRMING_OBSERVATION: >
  A reclaimed lead is reassigned to a specific partner with no record of either the routing rule
  having chosen that partner or a recorded manual override.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Reclaim a lead and observe how the next assignment is produced and what, if anything, records how
  that outcome was reached.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q014

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q014
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A lead is not reclaimed and handed to a new owner without the new owner being told that the
  previous partner already made contact with the submitter.
WHY_IT_MATTERS: >
  A customer contacted twice, independently, by two different owners of the same enquiry
  experiences the business as disorganized and can receive contradictory information.
DISCONFIRMING_OBSERVATION: >
  A reclaimed lead is reassigned and the new owner's record shows no indication that the prior
  partner had already reached out to the submitter.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Have a partner record contact with the submitter, then reclaim and reassign the lead to a new
  owner and inspect what the new owner is shown.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q015

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q015
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a lead already contacted by a partner is reclaimed, the record of that contact having
  occurred is retained, not discarded along with the assignment.
WHY_IT_MATTERS: >
  Discarding that evidence removes the only way to later establish whether the submitter was already
  approached before a dispute or duplicate outreach arises.
DISCONFIRMING_OBSERVATION: >
  After reclaim, no record remains showing that the previous partner had contacted the submitter,
  even though it happened.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a partner's contact with the submitter, reclaim the lead, and check whether that contact
  event is still visible afterward.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q016

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q016
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reassigning an already-contacted lead does not, by itself, trigger the new owner to repeat an
  initial outreach step that the submitter has already been through.
WHY_IT_MATTERS: >
  A submitter receiving the same introductory contact twice, from two different parties acting for
  the same business, reads as a lack of coordination that damages trust.
DISCONFIRMING_OBSERVATION: >
  Reassignment automatically triggers a fresh initial-contact action toward the submitter with no
  check for contact that already occurred.
EXPECTED_SURFACE: S1,S5,S8
PRECONDITIONS: >
  Reassign an already-contacted lead to a new owner and observe whether any automatic first-contact
  step fires regardless of the prior contact.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q017

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q017
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A new owner taking over a reclaimed, already-contacted lead can see the history of what was
  already communicated, rather than starting with no context.
WHY_IT_MATTERS: >
  Without that continuity the new owner cannot avoid contradicting or repeating what the submitter
  was already told.
DISCONFIRMING_OBSERVATION: >
  A new owner of a reclaimed lead has no access to the record of the prior partner's contact with
  the submitter.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Reassign an already-contacted lead to a new owner and check what prior-contact history that new
  owner can see.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q018

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q018
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  At any one moment, a given lead has at most one partner holding an active assignment on it, never
  two simultaneously.
WHY_IT_MATTERS: >
  Two partners simultaneously believing they own the same enquiry leads to duplicate, uncoordinated,
  and possibly contradictory outreach to the same submitter.
DISCONFIRMING_OBSERVATION: >
  A lead's record shows two different partner companies both holding a current, active assignment to
  it at the same time.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attempt to trigger a second assignment on a lead that already holds an active assignment and
  observe whether the first is ever displaced or whether both persist.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q019

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q019
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When more than one partner could equally match a lead's territory or specialism, a defined rule
  decides the single result, rather than the outcome depending on unrecorded chance.
WHY_IT_MATTERS: >
  An undefined tie-break makes routing outcomes unrepeatable and unexplainable to a partner who asks
  why they did not get a lead they otherwise qualify for.
DISCONFIRMING_OBSERVATION: >
  Two equally-qualifying partners exist for a lead and the assignment outcome cannot be explained by
  any recorded rule or precedence.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure two partners with identical qualifying territory or specialism for one lead and submit
  it, then ask for the rule that decided the outcome.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q020

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q020
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Whether the routing logic checks for, and avoids, sending a submitter's enquiry to a partner known
  to compete directly with the submitter is a deliberate, documented answer, not an unconsidered gap.
WHY_IT_MATTERS: >
  Routing a prospect's enquiry to their own competitor, even unintentionally, is a reputational and
  trust failure the moment it is discovered.
DISCONFIRMING_OBSERVATION: >
  No configuration, rule, or documented design choice exists one way or the other for whether
  competitor relationships are considered, and the question cannot be answered by anyone responsible
  for the routing.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Ask whoever owns the routing configuration whether, and how, a submitter's known competitors are
  ever excluded from receiving that submitter's own lead.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q021

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q021
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a submitter has indicated they do not want to be referred to a particular partner or class
  of partner, the routing outcome respects that exclusion.
WHY_IT_MATTERS: >
  Routing against an explicit expressed preference turns a lead-generation feature into something
  the submitter did not agree to.
DISCONFIRMING_OBSERVATION: >
  A submitter's recorded exclusion of a partner does not prevent that same partner from being
  assigned the submitter's lead.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record a submitter's exclusion of a specific partner, then submit a lead that would otherwise
  route to that partner.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q022

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q022
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A partner's grade or tier is applied consistently as one factor in routing, such that two
  otherwise-identical leads are not routed differently because of unrelated factors overriding it
  with no record.
WHY_IT_MATTERS: >
  An inconsistent application of grade undermines whatever commercial arrangement grade was meant to
  enforce, such as priority access for higher-tier partners.
DISCONFIRMING_OBSERVATION: >
  Two leads matching the same criteria are routed to partners of different grade with no recorded
  reason for the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Submit two leads matching identical routing criteria and compare the grade of the partner each is
  routed to.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q023

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q023
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Every territory a lead can originate from maps to exactly one routing outcome — a specific
  partner, or a defined fallback — never to no outcome at all.
WHY_IT_MATTERS: >
  A lead from an uncovered territory that simply has nowhere to go is a lost commercial opportunity
  that nobody is even alerted to.
DISCONFIRMING_OBSERVATION: >
  A lead originates from a territory with no partner coverage and no fallback fires; the lead is
  left with no assignment and no alert.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Submit a lead from a territory deliberately left without a covering partner and observe what
  happens to it.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q024

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q024
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where two partners' territories overlap for a given lead, a defined precedence decides the outcome
  rather than both being silently assigned or the result being arbitrary.
WHY_IT_MATTERS: >
  An arbitrary or dual outcome in overlapping territory recreates the same duplicate-ownership
  problem territory routing exists to prevent.
DISCONFIRMING_OBSERVATION: >
  A lead falling in an overlapping territory is assigned to both partners, or the choice between them
  cannot be traced to any rule.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure two partners with overlapping territory coverage, submit a lead into the overlap, and
  trace how the outcome was decided.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q025

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q025
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Changing the routing rules going forward does not itself alter leads that were already assigned
  under the previous rule set.
WHY_IT_MATTERS: >
  Retroactively moving already-assigned leads because a rule changed strips partners of leads they
  were legitimately given and disrupts work already under way.
DISCONFIRMING_OBSERVATION: >
  Updating the routing configuration causes a previously assigned, still-open lead to change
  ownership with no separate action having caused that.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Assign a lead under one routing configuration, change the configuration, and check whether the
  existing assignment moves on its own.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q026

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q026
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A lead's assignment record can be explained against the specific version of the routing rules that
  was in force at the moment it was assigned.
WHY_IT_MATTERS: >
  Without that link, a challenged assignment from months ago can never be defended or audited against
  the rule that actually produced it.
DISCONFIRMING_OBSERVATION: >
  The routing rules have since changed and the historical assignment record does not indicate,
  directly or indirectly, which rule version produced it.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Assign a lead, change the routing configuration afterward, and attempt to determine which
  configuration governed the earlier assignment.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q027

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q027
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A lead requiring a specialism no available partner currently offers is placed into a defined
  fallback — an internal queue, a default partner, or an escalation — rather than being left with no
  owner.
WHY_IT_MATTERS: >
  An enquiry that simply falls through because no partner happens to match is a lost opportunity
  indistinguishable, from the business's side, from one that never arrived.
DISCONFIRMING_OBSERVATION: >
  A lead requiring an unmatched specialism has no assignment and triggers no escalation, queue
  placement, or alert of any kind.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Submit a lead requiring a specialism no configured partner currently covers and observe what
  happens to it.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q028

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q028
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Lowering a partner's grade after a lead is already assigned to them does not, by itself, move or
  flag that already-open lead unless someone deliberately acts on it.
WHY_IT_MATTERS: >
  An automatic silent reshuffle of live commercial work triggered by an unrelated administrative
  change would surprise both the partner and whoever is managing the relationship.
DISCONFIRMING_OBSERVATION: >
  A partner's grade is lowered and a lead already assigned to them changes status or owner with no
  separate, recorded action having caused it.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Assign a lead to a partner, lower that partner's grade, and observe whether the existing
  assignment changes on its own.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q029

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q029
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Once a partner's commercial agreement has lapsed, no further new lead is routed to them from the
  moment the lapse takes effect.
WHY_IT_MATTERS: >
  Continuing to hand a live commercial relationship's leads to a partner with no current agreement
  exposes the business with no contract underpinning the handoff.
DISCONFIRMING_OBSERVATION: >
  A new lead is routed to a partner after the recorded effective date of that partner's agreement
  lapsing.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Let a partner's agreement lapse and submit a new lead that would otherwise route to them.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q030

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q030
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Leads already open with a partner at the moment its agreement lapses have a defined disposition —
  continue to completion, reclaim, or hold — rather than being left in an unaddressed state.
WHY_IT_MATTERS: >
  An undefined state leaves open commercial enquiries with an entity the business no longer has a
  current agreement to route to.
DISCONFIRMING_OBSERVATION: >
  A partner's agreement lapses while leads remain open with them, and nothing in the system flags,
  holds, or otherwise addresses those open leads differently from before the lapse.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Let a partner's agreement lapse while it still holds open leads and observe what, if anything,
  happens to those leads.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q031

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q031
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The business can, on demand, produce the list of leads currently open with any partner whose
  agreement is not currently active.
WHY_IT_MATTERS: >
  Without that visibility, a lapsed agreement's operational fallout — open leads nobody is tracking —
  can go unnoticed indefinitely.
DISCONFIRMING_OBSERVATION: >
  No available view or query can identify which currently-open leads belong to a partner whose
  agreement is not active.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  With at least one partner whose agreement is not active and still holding open leads, attempt to
  produce a list of exactly those leads.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q032

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q032
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where the submitter's self-entered location or language conflicts with other available evidence, a
  defined rule decides which one governs routing, rather than the first value entered being trusted
  permanently regardless of later contradiction.
WHY_IT_MATTERS: >
  Routing on a self-reported value the submitter got wrong, with no way to reconsider it, sends the
  enquiry to the wrong partner with no correction path.
DISCONFIRMING_OBSERVATION: >
  A submission carries a self-reported location that conflicts with other captured evidence, and the
  routing outcome cannot be explained by any rule for resolving the conflict.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Submit a lead whose self-entered location conflicts with other available evidence about the same
  submitter and trace how the routing decision was reached.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q033

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q033
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A lead misrouted because of an incorrect self-reported location or language can be manually
  corrected and rerouted, and the original submission details remain intact through that correction.
WHY_IT_MATTERS: >
  Losing the original submission when correcting a routing mistake destroys the evidence of what
  actually happened and why the correction was needed.
DISCONFIRMING_OBSERVATION: >
  Correcting a misrouted lead's destination requires re-entering or overwriting the original
  submission data, or the original values are no longer retrievable afterward.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit a lead with an incorrect location, correct the routing manually, and check whether the
  original submission is still intact and retrievable.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q034

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q034
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When a lead is routed to a default or catch-all partner because no specific geographic or language
  match was found, that fact is recorded, not indistinguishable from a genuine match.
WHY_IT_MATTERS: >
  Without that distinction, nobody can later tell how often the routing is actually working versus
  quietly falling back to a default.
DISCONFIRMING_OBSERVATION: >
  A lead assigned via a default or catch-all path is recorded identically to one that matched a
  specific criterion, with no way to tell them apart afterward.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Submit a lead with no matching geographic or language criterion so it falls to any default routing
  path, then inspect its record for a marker of that fact.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q035

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q035
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An outcome that a partner self-reports about a lead — won, lost, never contacted — is recorded in
  a way that shows it as the partner's own assertion, distinct from anything the business
  independently verified.
WHY_IT_MATTERS: >
  Treating an unverified third-party claim as an established fact removes the business's ability to
  ever question or audit it later.
DISCONFIRMING_OBSERVATION: >
  A partner-reported outcome is stored identically to, and indistinguishable from, an outcome the
  business itself confirmed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Have a partner report an outcome for a lead with no independent verification by the business, then
  inspect how that outcome is recorded.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q036

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q036
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a partner's self-reported outcome affects commission, credit, or performance standing, some
  means exists for the business to corroborate or challenge that claim, or the absence of any such
  means is at least an observable, documented fact.
WHY_IT_MATTERS: >
  Commission paid purely on an unverifiable claim, with no way to ever challenge it, is an
  open-ended financial exposure.
DISCONFIRMING_OBSERVATION: >
  A partner's self-reported outcome directly determines a commission or credit result and no
  corroboration, evidence attachment, or challenge path exists anywhere in the process, nor is that
  gap documented as a known and accepted position.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Trace a case where a partner's self-reported outcome determines a commission or credit result and
  look for any corroboration or challenge step in that path.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q037

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q037
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A partner reporting a lead as lost or closed does not remove the business's ability to see the
  reasoning or evidence behind that outcome.
WHY_IT_MATTERS: >
  A closure the business cannot inspect prevents it from ever learning whether leads are being
  under-served or written off too readily.
DISCONFIRMING_OBSERVATION: >
  A lead marked lost or closed by a partner shows no reason, note, or evidence field visible to the
  business explaining the outcome.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Have a partner mark an assigned lead lost or closed and check what reasoning or evidence is
  visible to the business afterward.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q038

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q038
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the business's own evidence about a lead's outcome conflicts with what the partner reported,
  that conflict is flagged rather than one value silently replacing the other.
WHY_IT_MATTERS: >
  Silent overwriting of a contradiction destroys the fact that a discrepancy ever existed, which is
  exactly the situation most worth investigating.
DISCONFIRMING_OBSERVATION: >
  A partner's reported outcome and the business's own contradicting record about the same lead
  coexist with no flag, and the later-saved value simply overwrites the earlier one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record the business's own evidence about a lead's outcome, then have the partner report a
  conflicting outcome for the same lead and observe what happens to the two values.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q039

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q039
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A pattern of one partner repeatedly self-reporting never contacted or lost for leads is at least
  visible in aggregate to the business, rather than each instance being recorded as an isolated,
  unremarkable event.
WHY_IT_MATTERS: >
  An unreliable partner's pattern of poor outcomes is only actionable if the business can actually
  see the pattern, not just each individual case.
DISCONFIRMING_OBSERVATION: >
  No aggregate or historical view exists that would let the business notice a partner's repeated
  pattern of self-reported non-contact or loss across their assigned leads.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Accumulate several leads from one partner self-reported as never contacted or lost, then look for
  any view that surfaces that pattern in aggregate.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q040

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q040
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The moment a submitter's personal data is made available to an external partner company is
  captured as its own recorded event — who, when, to which partner, and what data — rather than
  being indistinguishable from an ordinary internal reassignment.
WHY_IT_MATTERS: >
  Without that distinct record, the business cannot ever demonstrate to the submitter, a regulator,
  or itself when and to whom their data left the business.
DISCONFIRMING_OBSERVATION: >
  No record exists that separately identifies the moment personal data crossed from the business to
  the external partner, distinct from the general assignment history.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Route a lead to an external partner and search for a record that specifically identifies that
  moment as a transfer of personal data outside the business, not merely a reassignment.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q041

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q041
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Whatever basis the business relies on for sharing a submitter's data with an external partner is
  recorded or configurable somewhere in the setup, rather than being an unrecorded assumption.
WHY_IT_MATTERS: >
  A transfer of personal data to a separate legal entity with no recorded basis for it is a
  compliance gap the business cannot even see it has.
DISCONFIRMING_OBSERVATION: >
  Nobody responsible for the configuration can point to where the basis for the partner data-sharing
  is recorded, and no such record exists to find.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Ask whoever owns the partner-routing configuration to produce the recorded basis for sharing
  submitter data with partners, and see what, if anything, is produced.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q042

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q042
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a submitter has indicated at the point of submission that they do not want their details
  shared with a third party, that preference prevents the partner handoff from happening for their
  lead, or a defined alternative path exists for handling it.
WHY_IT_MATTERS: >
  Routing an enquiry to an external company against the submitter's stated wish makes the sharing
  itself unauthorized as far as the submitter is concerned.
DISCONFIRMING_OBSERVATION: >
  A submitter records a preference against third-party sharing and their lead is routed to an
  external partner regardless, with no different handling.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Submit a lead carrying a recorded preference against third-party sharing and observe whether the
  partner-routing step still occurs.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q043

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q043
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A request to erase a submitter's data received after it has already been shared with a partner
  results in a defined, recorded action — at minimum, that the request was logged and that the fact
  of the prior transfer is not concealed — rather than the erasure only ever touching the business's
  own copy with no acknowledgement that a copy exists elsewhere.
WHY_IT_MATTERS: >
  An erasure that only ever addresses the sending side gives the submitter, and the business itself,
  a false sense that their data has actually been removed.
DISCONFIRMING_OBSERVATION: >
  An erasure request is processed with no record of it, and nothing about the process acknowledges
  that the same data was previously made available to an external partner.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Route a lead to a partner, then submit an erasure request for the submitter's data and observe what
  the process does and records.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q044

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q044
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Personal data already shared with a partner for one lead is not automatically carried into a
  later, separate lead from the same submitter without that later sharing being its own recorded
  event.
WHY_IT_MATTERS: >
  Treating an earlier disclosure as blanket permission for every future one expands the original
  transfer well beyond what it was ever recorded to cover.
DISCONFIRMING_OBSERVATION: >
  A submitter's second, unrelated lead is routed to a partner with no new transfer record, relying
  instead on data sharing that only the first lead's record ever documented.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Route one lead from a submitter to a partner, then submit a second, unrelated lead from the same
  submitter and check whether a fresh transfer event is recorded for it.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q045

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q045
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  If the business has a retention expectation for how long shared data should remain relevant, a
  lead still open with a partner well past that point is at least identifiable, rather than ageing
  indefinitely with no visibility.
WHY_IT_MATTERS: >
  Without visibility into ageing open leads, data keeps circulating at a partner long after the
  business's own retention expectations would have called it into question.
DISCONFIRMING_OBSERVATION: >
  No view or report can identify leads that have remained open with a partner well beyond any
  retention expectation the business holds, because nothing tracks the elapsed time against it.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Leave a lead open with a partner well past any retention expectation the business holds and look
  for a view that would surface it as such.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q046

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q046
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where more than one person at the partner company can access an assigned lead, which individual
  accessed or acted on it is distinguishable in the record, not merged into a single undifferentiated
  attribution to the partner as a whole.
WHY_IT_MATTERS: >
  Without individual attribution, the business cannot ever answer a question about who at the partner
  actually saw or acted on a specific submitter's data.
DISCONFIRMING_OBSERVATION: >
  The record of activity on an assigned lead identifies only the partner company as a whole, with no
  way to tell which individual person performed a given action.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Have two different individuals at the same partner company act on the same assigned lead and
  inspect whether the record distinguishes between them.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q047

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q047
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An individual's ability to access leads assigned to a partner is tied to their current affiliation
  with that partner, such that the business has some means to have that access ended when told the
  person has left, rather than access being permanent once granted.
WHY_IT_MATTERS: >
  Access surviving someone's departure from the partner company leaves the submitter's data reachable
  by a person no longer accountable to anyone in the relationship.
DISCONFIRMING_OBSERVATION: >
  The business is told a specific person has left the partner company and has no means, directly or
  by request to the partner, to cause that person's access to end.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Be told that a named individual at a partner company has left, and attempt to have that person's
  access to assigned leads ended.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q048

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q048
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: R5-remediation
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When an anonymous website visitor's identity later resolves to an existing contact record (for
  example, once they identify themselves through a form submission or a login), the visitor's
  prior activity converges onto that existing record and whichever assignment currently owns it,
  rather than staying attached to a separate anonymous identity or spawning a second, disconnected
  record for the same person.
WHY_IT_MATTERS: >
  If prior activity does not follow the visitor once they are recognized, whoever is following up
  loses the browsing and engagement history that led to the identification, and the business is
  left with two disconnected records for one real person instead of one complete picture.
DISCONFIRMING_OBSERVATION: >
  After an anonymous visitor's identity resolves to an existing contact record, the visitor's
  earlier activity is found still attached to a separate anonymous identity, has been dropped
  entirely, or a second contact record has been created alongside the existing one rather than the
  two being reconciled into one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate activity from an anonymous website visitor, then have that visitor identify themselves in
  a way that matches an existing contact record, and inspect whether the prior activity and the
  existing record's current assignment converge onto a single record.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q049

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q049
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A person manually choosing a lead's partner is distinguishable in the record from the routing rule
  having chosen it automatically.
WHY_IT_MATTERS: >
  Without that distinction, a pattern of manual overrides that quietly bypasses the routing rules
  would be invisible to anyone reviewing outcomes.
DISCONFIRMING_OBSERVATION: >
  The assignment record for a lead does not indicate, and cannot be used to determine, whether the
  outcome came from the routing rule or from a person overriding it.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Produce one assignment from the routing rule and one from a manual override, then compare what each
  leaves behind in the record.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q050

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q050
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Archiving or merging an external partner's own record while leads are still open with it produces
  a defined effect on those open leads — reassignment, a hold, or an explicit flag — rather than
  leaving them pointing at a record no longer functioning as an active partner.
WHY_IT_MATTERS: >
  An open commercial lead silently left attached to a partner record that no longer behaves as active
  effectively strands it with nobody responsible.
DISCONFIRMING_OBSERVATION: >
  A partner record is archived or merged while leads remain open with it, and those leads show no
  change in status, flag, or ownership as a result.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Archive or merge a partner record that still holds open leads and observe what happens to those
  leads.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q051

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q051
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Merging two partner records preserves the assignment history that existed under each of the
  original records, rather than collapsing it into a single trail that can no longer show which
  original record a past assignment belonged to.
WHY_IT_MATTERS: >
  Losing that distinction after a merge removes the ability to reconstruct which of two formerly
  separate partner relationships a historical lead actually went through.
DISCONFIRMING_OBSERVATION: >
  After merging two partner records, a lead's assignment history no longer indicates which of the two
  original partner records it was actually assigned under.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Assign leads under two separate partner records, merge those records, and check whether each
  lead's history still shows its original partner record.
```

## G09-WEBSITE_CRM_PARTNER_ASSIGN-Q052

```yaml
QID: G09-WEBSITE_CRM_PARTNER_ASSIGN-Q052
MODULE: website_crm_partner_assign
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where the business operates more than one company, each with its own partner network, a lead
  originating under one company is only ever routed to a partner authorized for that specific
  company, never to a partner that belongs only to a different company's network.
WHY_IT_MATTERS: >
  Crossing a lead from one company's customer base into another company's partner network exposes it
  to a third party with no relationship to the company that actually generated the lead.
DISCONFIRMING_OBSERVATION: >
  A lead originating under one company is assigned to a partner that is authorized only for a
  different company in the same installation.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Operate two companies each with its own partner network, submit a lead under one company, and check
  whether it can be routed to a partner authorized only for the other.
```
