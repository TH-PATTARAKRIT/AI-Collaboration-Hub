# SMEsPlus ENTERPRISE SUITE
## GMVQ — G09 CRM / crm Module Adversarial MVQ Bank

**Document ID:** GMVQ-G09-CRM-MVQ66-V1.00
**Group:** G09 CRM
**Module Metadata:** `crm`
**Wave:** W2
**Author Cell:** P-C1 (GMVQ Question Factory — Production Team P-C1, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 66

## Purpose

`crm` is the BASE module of G09 (11 modules, none previously had a bank). It owns the group's core
invariants — the boundary between an unqualified inbound interest and a qualified opportunity and what must
survive that crossing; pipeline stage and the probability attached to it driving a forecast that management
reads as fact; the integrity of expected-value and close-date edits and who is accountable for them;
assignment and reassignment while activities remain open, including automatic-assignment fallback and
fairness; won and lost as mutually exclusive, reversible-with-a-trace states; duplicate detection and merge
without losing history or double-counting forecast value; the survival of an opportunity's link and access
when its linked customer record is archived, merged or deleted; the currency of activities and next steps
across stage changes and closure; pipeline-stage configuration change while opportunities sit in scope;
forecast movement caused by a rule change rather than an event; cross-company and cross-team visibility; and
the audit trail of who changed a value and when, with the prior value preserved — so that the ten bridge
banks in this group (`crm_iap_enrich`, `crm_iap_mine`, `crm_livechat`, `crm_mail_plugin`, `crm_sms`,
`website_crm`, `website_crm_iap_reveal`, `website_crm_livechat`, `website_crm_partner_assign`,
`website_crm_sms`) do not need to restate these invariants and can instead ask what happens to them at their
own seam — a paid-lookup credit boundary, an inbound channel becoming a pipeline entry, or a routing decision
to an external partner.

Because this module holds personal data about people who have never transacted with the business — an
inbound interest that never converts, an anonymous visitor later identified through a paid service, a
contact captured through a public channel — privacy is treated here as a first-class dimension carrying the
same weight as the pipeline invariants, not as an afterthought left to a separate privacy-focused module.

Question text is source-neutral: no vendor or product name, no technical identifier (model, table, field,
method, XML ID, API path), and no reference to how any specific implementation is built. Language is generic
sales/relationship-management business behaviour throughout — "opportunity", "interest", "stage", "owner",
"activity" and "contact" are used as plain business terms, never as technical identifiers.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 66 questions exist because they test 66 distinct material hypotheses, spread across business
  capability, business rule, state transition, configuration dependency, role/permission, exception path,
  reversal, negative case, cross-module dependency, optional behaviour, auditability, tenant/company
  boundary, and concurrency/ordering.
- Particular depth is placed on forecast rollup correctness and forecast movement from a rule change rather
  than an event (Q009–Q011, Q050–Q052), on won/lost as mutually exclusive and auditably reversible states
  (Q025–Q030), on duplicate detection and merge without history loss or forecast double-counting
  (Q031–Q036), and on privacy — consent basis, retention, third-party disclosure, subject access, erasure
  conflict, and consent-withdrawal scope (Q061–Q066).
- `LAYER: BASE` marks a foundation/configuration question (stage and probability configuration,
  automatic-assignment rule configuration, multi-company/team scoping); `LAYER: PROCESS` marks a
  transactional/lifecycle question, since this module carries both layers.
- Per the Bridge Module Rule (§6), `crm` is a base module, not a bridge: it owns real behaviour and gets the
  deep treatment here so the ten bridge banks in this group can ask what happens to these invariants at
  their own seam instead of restating them.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `MODULE + QID` is a
  Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G09-CRM-Q001

```yaml
QID: G09-CRM-Q001
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A record converted from an initial inbound interest into a qualified opportunity is represented as a single
  continuous record, or an explicitly linked pair, so that the interest's original source, contact details,
  and first-contact timestamp survive the conversion.
WHY_IT_MATTERS: >
  If conversion silently creates a new record disconnected from the original interest, source attribution,
  response-time reporting, and the audit trail of how the relationship began are lost.
DISCONFIRMING_OBSERVATION: >
  Converting an inbound interest into an opportunity produces a record whose original source, first-contact
  timestamp, or submitted contact details cannot be traced back to the originating interest.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Capture an inbound interest with a recorded source and timestamp, convert it into an opportunity, and
  inspect whether the resulting record still exposes that source and timestamp.
```

## G09-CRM-Q002

```yaml
QID: G09-CRM-Q002
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Converting an inbound interest whose contact details match an already-existing customer contact links the
  resulting opportunity to that existing contact rather than creating a second, disconnected contact record.
WHY_IT_MATTERS: >
  A duplicate contact record fragments relationship history and can cause two salespeople to independently
  and unknowingly pursue the same account.
DISCONFIRMING_OBSERVATION: >
  Converting an interest whose contact details match an existing customer contact creates an entirely new,
  unlinked contact record instead of associating the opportunity with the existing one.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a customer contact, then capture and convert an inbound interest carrying matching contact details,
  and check whether the opportunity is linked to the existing contact or a new one.
```

## G09-CRM-Q003

```yaml
QID: G09-CRM-Q003
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An inbound interest can be disqualified and closed without ever being converted, and this outcome is
  distinguishable in later reporting from an opportunity that was actively pursued and then lost.
WHY_IT_MATTERS: >
  Conflating "never qualified" with "pursued and lost" misrepresents the sales team's actual win rate and the
  real size of the addressable pipeline.
DISCONFIRMING_OBSERVATION: >
  A disqualified, never-converted interest appears in the same lost-opportunity count or lost-value total as
  opportunities that were actively pursued through the pipeline.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Disqualify one interest before conversion and separately lose one converted opportunity, then compare how
  each is counted in pipeline and loss reporting.
```

## G09-CRM-Q004

```yaml
QID: G09-CRM-Q004
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Conversion of an interest into an opportunity is a one-way, auditable transition; there is no path that
  silently reverts a fully working opportunity back to a state indistinguishable from a never-qualified
  interest while discarding the stage and activity history already recorded against it.
WHY_IT_MATTERS: >
  A silent reversal would erase the record of work already done and could be used to make an unfavourable
  pipeline entry disappear from reporting.
DISCONFIRMING_OBSERVATION: >
  An opportunity that has already progressed through one or more pipeline stages can be returned to
  unqualified-interest status and its prior stage and activity history is no longer visible anywhere.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Progress an opportunity through at least one stage change and one recorded activity, then attempt to revert
  it to an unqualified interest state and check whether the prior history remains visible.
```

## G09-CRM-Q005

```yaml
QID: G09-CRM-Q005
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two independently submitted inbound interests that both identify the same underlying prospect are surfaced
  to the person qualifying them as a potential duplicate before both are separately converted into two
  competing opportunities.
WHY_IT_MATTERS: >
  Two live opportunities for the same prospect, worked by two different salespeople, causes conflicting
  outreach, double-counted forecast value, and an inconsistent story presented to the customer.
DISCONFIRMING_OBSERVATION: >
  Two interests carrying the same contact identity are both converted into separate opportunities with no
  indication anywhere in the qualification flow that a potential duplicate existed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit two inbound interests with matching contact identity through the same or different channels and
  observe whether either qualification step flags the overlap before conversion.
```

## G09-CRM-Q006

```yaml
QID: G09-CRM-Q006
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Each pipeline stage carries a default win-probability value applied when an opportunity enters that stage,
  and this default can be distinguished from a probability a person has manually overridden on an individual
  opportunity.
WHY_IT_MATTERS: >
  If a manual override cannot be told apart from the stage default, a manager reviewing forecast confidence
  cannot tell whether a number reflects the standard model or one person's private optimism.
DISCONFIRMING_OBSERVATION: >
  After a person manually changes the probability on an individual opportunity, there is no way to determine
  afterward whether the value shown is the stage default or a manual override.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Move an opportunity into a stage with a configured default probability, note the value, manually change it,
  then inspect whether the override is distinguishable from the default.
```

## G09-CRM-Q007

```yaml
QID: G09-CRM-Q007
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Moving an opportunity backward to an earlier pipeline stage updates its probability to reflect that earlier
  stage rather than retaining the higher probability associated with the stage it is leaving.
WHY_IT_MATTERS: >
  A stale, too-high probability surviving a backward stage move would overstate the forecast for a deal that
  has actually regressed.
DISCONFIRMING_OBSERVATION: >
  An opportunity moved backward to an earlier stage keeps the probability value associated with the more
  advanced stage it just left.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Advance an opportunity to a later stage, note its probability, move it back to an earlier stage, and
  compare the probability before and after.
```

## G09-CRM-Q008

```yaml
QID: G09-CRM-Q008
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A forecast confidence grouping used in management reporting (for example, "committed" versus "pipeline")
  can be set or read independently of the raw stage-derived probability, so the two can legitimately disagree
  on the same opportunity.
WHY_IT_MATTERS: >
  If the forecast category is only ever a mechanical restatement of the probability number, the model cannot
  express a salesperson's qualitative judgment that a numerically likely deal is not actually committed, or
  the reverse.
DISCONFIRMING_OBSERVATION: >
  The forecast category always matches a fixed mechanical mapping from the current probability with no way
  for a person to set it independently, or no such distinct category exists at all.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set an opportunity's probability to a mid-range value and attempt to independently set its forecast
  category to a value that would not follow from a pure mechanical mapping, then check whether it is
  retained.
```

## G09-CRM-Q009

```yaml
QID: G09-CRM-Q009
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A rollup forecast figure shown to management (for example, total expected value across a team's open
  pipeline) is computed from the current state of each opportunity at the moment the figure is generated, not
  from a value cached at an earlier point that could have gone stale.
WHY_IT_MATTERS: >
  A cached, stale rollup would let management make decisions on numbers that no longer reflect changes
  salespeople have already made to their opportunities.
DISCONFIRMING_OBSERVATION: >
  Changing the stage, probability, or expected value on an open opportunity does not change a subsequently
  generated rollup forecast figure that includes it.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Generate a rollup forecast figure, change the stage or expected value of one open opportunity included in
  it, regenerate the figure, and compare the two results.
```

## G09-CRM-Q010

```yaml
QID: G09-CRM-Q010
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An opportunity's contribution to the forecast is computed from its currently recorded probability at the
  time the forecast is generated, and it is possible to reconstruct what probability was in effect for that
  opportunity at any past date a forecast was actually run.
WHY_IT_MATTERS: >
  Without a reconstructable history of past probability values, a discrepancy between what was reported to
  management last month and what the pipeline shows today can never be explained or trusted.
DISCONFIRMING_OBSERVATION: >
  There is no way to determine what probability value an opportunity carried at a specific past date, so a
  prior forecast figure cannot be reproduced or explained after the fact.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record an opportunity's probability on a given date, change it later, and attempt to determine what value
  was in effect on the earlier date using only records available in the system.
```

## G09-CRM-Q011

```yaml
QID: G09-CRM-Q011
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An opportunity manually excluded from the forecast rollup (marked as not to be counted, distinct from being
  closed) is visibly flagged as excluded rather than simply vanishing from pipeline views with no indication
  that anything was suppressed.
WHY_IT_MATTERS: >
  A silently vanishing opportunity could be used, deliberately or accidentally, to understate risk in a
  pipeline review without anyone noticing a number was left out.
DISCONFIRMING_OBSERVATION: >
  An opportunity excluded from the forecast rollup no longer appears in any pipeline listing at all, with no
  flag or indication distinguishing "excluded from forecast" from "does not exist."
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Mark an open opportunity as excluded from forecast rollup and compare its visibility in a general pipeline
  listing before and after.
```

## G09-CRM-Q012

```yaml
QID: G09-CRM-Q012
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Editing the expected value of an open opportunity records who made the change and when, distinguishable
  from the opportunity's creation event.
WHY_IT_MATTERS: >
  Without this, a large late change to a forecasted amount cannot be attributed to anyone, which is exactly
  the situation a forecast-integrity review needs to be able to answer.
DISCONFIRMING_OBSERVATION: >
  The expected value on an opportunity is changed after creation and no record exists anywhere of who made
  that change or when, separate from the original creation record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create an opportunity, later edit its expected value, and search for any trace of the change separate from
  the creation timestamp.
```

## G09-CRM-Q013

```yaml
QID: G09-CRM-Q013
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Editing the expected value or close date of an opportunity does not require the person making the change to
  record a reason, and this absence of a mandatory justification is a real, exploitable gap rather than
  something enforced elsewhere.
WHY_IT_MATTERS: >
  If a material forecast number can be moved with no required justification, a pattern of quarter-end value
  inflation would leave no trace of intent even where the value change itself is logged.
DISCONFIRMING_OBSERVATION: >
  The system in fact requires and enforces a reason to be recorded on every expected-value or close-date
  edit, or blocks the edit entirely without one; that outcome disproves the hypothesis and should be reported
  as such.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attempt to change the expected value and separately the close date on an open opportunity while providing
  no explanatory text, and observe whether the edit is accepted, and if accepted, whether any reason field
  was actually required.
```

## G09-CRM-Q014

```yaml
QID: G09-CRM-Q014
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Repeatedly pushing an opportunity's close date forward without ever changing its stage is not treated any
  differently by the forecast than an opportunity whose close date has never moved, so that repeated slippage
  is invisible unless someone deliberately looks at the change history.
WHY_IT_MATTERS: >
  A deal repeatedly rescheduled but never actually lost inflates the near-term forecast indefinitely while
  looking identical, at a glance, to a healthy on-track deal.
DISCONFIRMING_OBSERVATION: >
  The system in fact surfaces or flags a pattern of repeated close-date slippage distinct from a stable close
  date, which would disprove the hypothesis and should be reported.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Push the same opportunity's close date forward several times across separate edits without changing its
  stage, and check whether any view or report distinguishes it from an opportunity whose close date has not
  moved.
```

## G09-CRM-Q015

```yaml
QID: G09-CRM-Q015
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A bulk edit that changes the expected value or close date across many opportunities at once (for example,
  through an import or a mass-update action) is recorded with the same per-record traceability as a single
  manual edit, not as one anonymous batch event that obscures which records changed and by how much.
WHY_IT_MATTERS: >
  A bulk update is exactly the kind of action that could be used to move many forecast numbers at once; if it
  is logged at batch granularity only, no one can later tell which individual opportunities were actually
  touched or what their prior values were.
DISCONFIRMING_OBSERVATION: >
  After a bulk update changes the expected value on multiple opportunities, the per-opportunity prior value
  and change attribution cannot be individually recovered, only that a batch operation occurred.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Perform a bulk update changing the expected value on several opportunities at once, then attempt to recover
  the prior value and change attribution for one individual record from that batch.
```

## G09-CRM-Q016

```yaml
QID: G09-CRM-Q016
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reassigning an opportunity to a different owner while it has open, unfinished next-step activities either
  transfers those activities to the new owner or leaves them clearly visible as still owned by the previous
  person, but does not silently strand them with no owner at all.
WHY_IT_MATTERS: >
  A stranded activity with no effective owner is a commitment to a customer that nobody is now responsible
  for keeping.
DISCONFIRMING_OBSERVATION: >
  After reassigning an opportunity with open activities to a new owner, at least one activity ends up with no
  owner able to see or act on it as their own responsibility.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create an opportunity with an open, unfinished activity, reassign the opportunity to a different owner, and
  check who the activity is now assigned to.
```

## G09-CRM-Q017

```yaml
QID: G09-CRM-Q017
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The history of a reassigned opportunity retains the identity of its previous owner and the date of the
  reassignment, rather than overwriting the record so that only the current owner is ever visible.
WHY_IT_MATTERS: >
  Losing the prior-owner history makes it impossible to evaluate individual salesperson performance on deals
  they worked before being reassigned, or to investigate a customer complaint about an earlier point of
  contact.
DISCONFIRMING_OBSERVATION: >
  After an opportunity is reassigned, there is no record anywhere of who owned it before the change or when
  the change happened.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reassign an opportunity from one owner to another and search the record for any trace of the previous owner
  and the reassignment date.
```

## G09-CRM-Q018

```yaml
QID: G09-CRM-Q018
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Reassigning an opportunity does not itself change its pipeline stage, probability, or expected value;
  ownership and pipeline position are independent facts about the record.
WHY_IT_MATTERS: >
  If reassignment silently resets or alters the deal's pipeline position, a routine ownership handover would
  corrupt the forecast for reasons that have nothing to do with the deal itself.
DISCONFIRMING_OBSERVATION: >
  Reassigning an opportunity to a new owner, with nothing else changed, results in a different stage,
  probability, or expected value than it had immediately before.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Record an opportunity's stage, probability, and expected value, reassign it to a different owner, and
  compare those three values immediately before and after.
```

## G09-CRM-Q019

```yaml
QID: G09-CRM-Q019
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A person who no longer has an active account cannot be selected as the new owner in a manual reassignment,
  and an opportunity currently owned by such a person is identifiable so it can be redistributed rather than
  sitting invisibly under a dead account.
WHY_IT_MATTERS: >
  A pipeline of live deals silently attached to someone who can no longer act on them is effectively unworked
  and undiscoverable pipeline risk.
DISCONFIRMING_OBSERVATION: >
  An opportunity remains assigned to a deactivated or removed person with nothing in any standard pipeline
  view distinguishing it from one owned by an active salesperson.
EXPECTED_SURFACE: S1,S4,S5
PRECONDITIONS: >
  Deactivate the account of a person who owns one or more open opportunities and check whether those
  opportunities are flagged, filtered, or otherwise made discoverable as needing reassignment.
```

## G09-CRM-Q020

```yaml
QID: G09-CRM-Q020
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A person can only reassign an opportunity to themselves or to another owner if their role or scope permits
  acting on that opportunity in the first place; reassignment is not a way to bypass the same permission
  boundary that governs viewing or editing it.
WHY_IT_MATTERS: >
  If reassignment ignores ownership and scope permissions, anyone could redirect pipeline they have no
  legitimate business relationship to, undermining territory and team boundaries entirely.
DISCONFIRMING_OBSERVATION: >
  A person with no view or edit access to an opportunity is nonetheless able to reassign it to themselves or
  to a third party.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a person with no assigned access to a particular opportunity, attempt to reassign it and observe whether
  the action is blocked.
```

## G09-CRM-Q021

```yaml
QID: G09-CRM-Q021
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When an automatic assignment rule finds no eligible owner matching its criteria at the moment a new
  opportunity arrives, the opportunity is placed somewhere explicitly visible as unassigned rather than being
  silently dropped or left invisible to everyone.
WHY_IT_MATTERS: >
  An opportunity that arrives and is neither assigned nor visibly flagged as unassigned is functionally lost
  before anyone even knows it exists.
DISCONFIRMING_OBSERVATION: >
  An opportunity created under conditions where no eligible automatic-assignment owner exists ends up with no
  owner and does not appear in any unassigned or exception queue.
EXPECTED_SURFACE: S1,S5,S8
PRECONDITIONS: >
  Configure or arrange an automatic assignment rule with no currently eligible owner, create a new
  opportunity that should be routed by that rule, and check where the opportunity ends up.
```

## G09-CRM-Q022

```yaml
QID: G09-CRM-Q022
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Automatic assignment does not route new opportunities to a person whose account is deactivated, even if
  that person still matches the rule's other eligibility criteria.
WHY_IT_MATTERS: >
  Routing live pipeline to someone who has left silently creates the same unworked-deal risk as a manual
  assignment to a departed employee, but happens continuously and without anyone deciding it.
DISCONFIRMING_OBSERVATION: >
  A new opportunity is automatically assigned to a person whose account has been deactivated.
EXPECTED_SURFACE: S1,S4,S8
PRECONDITIONS: >
  Deactivate the account of a person who would otherwise match an automatic assignment rule's criteria,
  trigger a new opportunity that the rule would route, and observe the resulting owner.
```

## G09-CRM-Q023

```yaml
QID: G09-CRM-Q023
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Changing the configuration of an automatic assignment rule (for example, its eligible owners or its
  distribution logic) affects only opportunities assigned after the change, and does not retroactively
  reassign opportunities already routed under the previous configuration.
WHY_IT_MATTERS: >
  Retroactive reassignment triggered by a configuration change would move live pipeline between people with
  no one having taken that specific action, breaking accountability for who is actually working each deal.
DISCONFIRMING_OBSERVATION: >
  Changing the automatic assignment rule's configuration causes one or more already-assigned opportunities to
  change owner with no separate reassignment action taken.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Let an automatic assignment rule assign several opportunities, then change the rule's configuration, and
  check whether the ownership of the already-assigned opportunities changes as a result.
```

## G09-CRM-Q024

```yaml
QID: G09-CRM-Q024
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where automatic assignment is meant to distribute new opportunities evenly or by a stated rotation among
  eligible owners, a person who receives a manually assigned opportunity outside that rotation is not skipped
  in, or otherwise able to unfairly benefit from, the next automatic distribution.
WHY_IT_MATTERS: >
  If manual assignment interacts unpredictably with the fairness logic, the distribution rule effectively
  cannot be trusted to have distributed pipeline as evenly as it was configured to.
DISCONFIRMING_OBSERVATION: >
  Manually assigning an opportunity to a specific person measurably skips that person's position in, or
  otherwise distorts, the next automatic rotation-based assignment.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Manually assign an opportunity to a person who is also part of an automatic rotation pool, then trigger the
  next automatic assignment and compare the resulting distribution to what the stated rotation would produce.
```

## G09-CRM-Q025

```yaml
QID: G09-CRM-Q025
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Marking an opportunity as won requires, or automatically records, a close date, so that a won opportunity
  is never left with an undefined or clearly incorrect close date.
WHY_IT_MATTERS: >
  A won deal with no meaningful close date corrupts any reporting that groups revenue by the period it was
  actually closed in.
DISCONFIRMING_OBSERVATION: >
  An opportunity can be marked won while its close date is left blank or is a date that clearly predates the
  actual point at which it was won.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Mark an opportunity as won without separately setting a close date and check what close date, if any, the
  record ends up with.
```

## G09-CRM-Q026

```yaml
QID: G09-CRM-Q026
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Marking an opportunity as lost requires a lost reason to be recorded before the status change is accepted,
  rather than the reason being an optional field a person can skip.
WHY_IT_MATTERS: >
  If a lost reason is optional, loss-analysis reporting becomes unreliable exactly where it matters most:
  understanding why the business is not winning deals.
DISCONFIRMING_OBSERVATION: >
  An opportunity can be marked lost and saved with no lost reason recorded at all.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to mark an opportunity lost while leaving the lost-reason field empty and observe whether the
  change is accepted.
```

## G09-CRM-Q027

```yaml
QID: G09-CRM-Q027
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Reopening an opportunity previously marked lost returns it to an active pipeline state distinguishable from
  a brand-new opportunity, retaining its prior stage history, activities, and the record that it was once
  marked lost and why.
WHY_IT_MATTERS: >
  Losing the prior loss context on reopening would mean the same objection or reason that killed the deal
  once could recur completely unnoticed the second time around.
DISCONFIRMING_OBSERVATION: >
  Reopening a previously lost opportunity clears its prior stage history, its recorded activities, or the
  fact and reason that it was once lost.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Mark an opportunity lost with a reason and some prior activity history, reopen it, and inspect whether the
  history and the loss record are still present.
```

## G09-CRM-Q028

```yaml
QID: G09-CRM-Q028
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reopening an opportunity previously marked won removes or clearly flags any revenue it had contributed to a
  completed forecast period, rather than leaving that period's historical won total permanently overstated
  with no trace of the reversal.
WHY_IT_MATTERS: >
  A won deal later reopened (for example, because the deal actually fell through after being recorded won)
  but whose reversal never reaches historical reporting leaves a permanently wrong number in every past
  report that included it.
DISCONFIRMING_OBSERVATION: >
  Reopening a previously won opportunity leaves the historical won-revenue total for the period in which it
  was originally won completely unchanged, with no flag anywhere that a reversal occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Mark an opportunity won within a reporting period, record the period's won total, reopen the opportunity,
  and check whether the historical total or any accompanying record reflects the reversal.
```

## G09-CRM-Q029

```yaml
QID: G09-CRM-Q029
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An opportunity cannot be simultaneously in both a won state and a lost state at the same time; the two are
  mutually exclusive statuses enforced by the system, not merely a convention a person is expected to follow.
WHY_IT_MATTERS: >
  A record that is somehow both won and lost at once would make every revenue and loss report that includes
  it internally contradictory.
DISCONFIRMING_OBSERVATION: >
  An opportunity is found, through direct action or through a sequence of actions, to carry both a won status
  and a lost status at the same time.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Attempt to mark an already-lost opportunity as won without first reopening it, and the reverse, and observe
  whether the system enforces mutual exclusivity or allows a contradictory state.
```

## G09-CRM-Q030

```yaml
QID: G09-CRM-Q030
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The count and value of "won this period" reported for a team is derived from opportunities actually marked
  won within that period, not inflated by an opportunity that was marked won, reopened, and marked won again
  being counted more than once for the same underlying deal.
WHY_IT_MATTERS: >
  Double-counting a single deal's revenue across a won/reopen/won cycle would overstate actual sales
  performance without any deliberate manipulation being required.
DISCONFIRMING_OBSERVATION: >
  An opportunity that is marked won, reopened, and marked won again appears twice in a won-revenue total for
  the same or overlapping reporting period.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Mark an opportunity won, reopen it, mark it won again, and check whether a won-revenue report counts its
  value once or twice.
```

## G09-CRM-Q031

```yaml
QID: G09-CRM-Q031
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The system offers some mechanism, automatic or assisted, to surface likely duplicate opportunities to a
  person before they are worked as two separate deals, rather than relying entirely on a person noticing the
  overlap unaided.
WHY_IT_MATTERS: >
  With no detection mechanism at all, duplicate opportunities for the same prospect accumulate silently, and
  everything downstream that depends on catching this early — forecast double-counting, conflicting
  outreach — becomes unavoidable rather than merely possible.
DISCONFIRMING_OBSERVATION: >
  Two opportunities that share the same underlying contact and clearly overlapping subject matter are never
  surfaced to any user as potential duplicates under any workflow the system provides.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Create two opportunities sharing the same contact and closely overlapping details, and check whether any
  available view, list, or workflow ever surfaces the overlap to a user.
```

## G09-CRM-Q032

```yaml
QID: G09-CRM-Q032
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Merging two opportunities preserves the activity history of both records under the surviving record, rather
  than discarding the activities that belonged to whichever record did not survive the merge.
WHY_IT_MATTERS: >
  Discarding one side's activity history on merge erases legitimate work already done and any commitments
  already made to the customer under that record.
DISCONFIRMING_OBSERVATION: >
  After merging two opportunities, one side's previously recorded activities are no longer present anywhere
  against the surviving record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create two opportunities, record distinct activities against each, merge them, and check whether the
  surviving record shows the activities from both.
```

## G09-CRM-Q033

```yaml
QID: G09-CRM-Q033
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Merging two opportunities that each carried their own expected value and forecast contribution results in
  the surviving record's forecast contribution reflecting a single deliberate resolution, not simply both
  values continuing to exist and being separately counted in the pipeline forecast.
WHY_IT_MATTERS: >
  If the non-surviving record's forecast contribution is not properly retired, a merge intended to clean up a
  duplicate would instead leave the forecast double-counting the same underlying deal.
DISCONFIRMING_OBSERVATION: >
  After merging two opportunities, the total forecast contribution attributable to the merged deal is higher
  than could be justified by treating it as a single opportunity, indicating the discarded record's value is
  still being counted somewhere.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create two opportunities each with its own expected value, include both in a forecast total, merge them,
  and compare the forecast total before and after the merge.
```

## G09-CRM-Q034

```yaml
QID: G09-CRM-Q034
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The record of who changed what and when for both opportunities involved in a merge remains available after
  the merge, even for the record that did not survive, rather than being deleted along with the non-surviving
  record.
WHY_IT_MATTERS: >
  If the discarded record's change history disappears entirely, any question about what happened to that side
  of the story before the merge becomes permanently unanswerable.
DISCONFIRMING_OBSERVATION: >
  After a merge, no trace of the non-surviving opportunity's own change history can be found anywhere in the
  system.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Make several traceable changes to each of two opportunities before merging them, then attempt to locate the
  change history belonging to the non-surviving record after the merge.
```

## G09-CRM-Q035

```yaml
QID: G09-CRM-Q035
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Two opportunities in different pipeline stages, or owned by different people, can still be merged, and the
  merge forces an explicit resolution of which stage and which owner the surviving record takes, rather than
  the merge being silently blocked or producing an ambiguous combined state.
WHY_IT_MATTERS: >
  If a merge across different stages or owners is either blocked outright or resolved inconsistently, the
  very duplicates that are hardest to catch early, because they diverged the most, become the ones that can
  never be cleaned up.
DISCONFIRMING_OBSERVATION: >
  Attempting to merge two opportunities in different stages or with different owners either fails with no
  path to resolution, or succeeds while leaving the surviving record's stage or owner ambiguous or
  contradictory.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create two opportunities in different pipeline stages with different owners, attempt to merge them, and
  check whether the merge completes and what stage and owner the result carries.
```

## G09-CRM-Q036

```yaml
QID: G09-CRM-Q036
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Merging two opportunities that belong to different companies or business units in a multi-company setup is
  either blocked, or requires explicit confirmation that crosses the company boundary deliberately, rather
  than happening silently as a side effect of an otherwise ordinary duplicate cleanup.
WHY_IT_MATTERS: >
  A silent cross-company merge could move a deal's value, history, and customer relationship across a
  boundary that the organization's structure and reporting depend on staying intact.
DISCONFIRMING_OBSERVATION: >
  Two opportunities belonging to different companies are merged with no distinct warning, confirmation, or
  block related to the cross-company nature of the action.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create two opportunities under two different companies in a multi-company configuration, attempt to merge
  them, and observe whether the cross-company nature of the merge is specifically addressed.
```

## G09-CRM-Q037

```yaml
QID: G09-CRM-Q037
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When the customer contact linked to an open opportunity is archived rather than deleted, the opportunity
  remains fully visible and workable, still correctly showing the archived contact's identity, rather than
  the link silently breaking or the opportunity disappearing from view.
WHY_IT_MATTERS: >
  Archiving a contact for unrelated reasons, such as a company reorganization, should not have the side
  effect of hiding or breaking active sales pipeline tied to that contact.
DISCONFIRMING_OBSERVATION: >
  Archiving the customer contact linked to an open opportunity causes the opportunity to disappear from
  standard pipeline views, or the link to the contact's identity to break or display as blank.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Link an open opportunity to a customer contact, archive that contact, and check whether the opportunity
  remains visible and correctly linked.
```

## G09-CRM-Q038

```yaml
QID: G09-CRM-Q038
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When two customer contact records are merged into one, a separate cleanup action from opportunity merging,
  every opportunity previously linked to either contact ends up linked to the single surviving contact,
  rather than some opportunities losing their contact link.
WHY_IT_MATTERS: >
  Losing the contact link on a subset of opportunities after a contact merge breaks the connection between a
  live deal and the customer it is actually with.
DISCONFIRMING_OBSERVATION: >
  After merging two customer contact records, at least one opportunity that was linked to either original
  contact no longer shows a link to the surviving merged contact.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Link separate opportunities to two different customer contacts, merge the two contacts, and check whether
  both opportunities now correctly link to the single surviving contact.
```

## G09-CRM-Q039

```yaml
QID: G09-CRM-Q039
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A person's access to view or act on an opportunity is not silently revoked purely because the customer
  contact record it is linked to is archived; access continues to follow the opportunity's own ownership and
  sharing rules.
WHY_IT_MATTERS: >
  If archiving a contact record has the unrelated side effect of locking out the salesperson working the
  deal, an administrative cleanup action ends up blocking legitimate sales activity.
DISCONFIRMING_OBSERVATION: >
  A salesperson who previously had access to an opportunity loses that access after the linked customer
  contact is archived, with no separate access change made to the opportunity itself.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Confirm a salesperson's access to an opportunity, archive the linked customer contact, and re-check the
  salesperson's access to the opportunity.
```

## G09-CRM-Q040

```yaml
QID: G09-CRM-Q040
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Deleting, not merely archiving, a customer contact linked to one or more opportunities is either blocked
  while the link exists, or the deletion explicitly and visibly resolves what happens to those opportunities,
  rather than leaving them pointing at a contact that no longer exists.
WHY_IT_MATTERS: >
  An opportunity referencing a customer contact that no longer exists at all is a broken record that can
  silently corrupt any reporting or reassignment logic that assumes the link is valid.
DISCONFIRMING_OBSERVATION: >
  A customer contact linked to one or more open opportunities can be deleted outright, and the opportunities
  are left referencing a contact that no longer exists with no warning or resolution.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Link an opportunity to a customer contact, attempt to delete that contact outright, and observe whether the
  deletion is blocked or how the opportunity's link is resolved.
```

## G09-CRM-Q041

```yaml
QID: G09-CRM-Q041
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An activity or next step whose due date has passed without being completed is distinguishable in the
  relevant views, for example marked overdue, from one that is still upcoming, rather than the two looking
  identical until someone checks the date manually.
WHY_IT_MATTERS: >
  Without a visible overdue distinction, a salesperson's or manager's view of what actually needs attention
  today silently degrades as missed commitments blend in with future ones.
DISCONFIRMING_OBSERVATION: >
  An activity whose due date has clearly passed without completion appears identically to an upcoming
  activity in every standard list or view, with nothing indicating it is overdue.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create an activity with a due date in the past that has not been marked complete, and check whether
  standard activity views distinguish it from an upcoming one.
```

## G09-CRM-Q042

```yaml
QID: G09-CRM-Q042
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An activity cannot exist with no owner at all; it is always assigned either to a specific person or, at
  minimum, inherits the responsible person from the opportunity it belongs to.
WHY_IT_MATTERS: >
  A next step assigned to nobody is a commitment that, by construction, nobody is being reminded to keep.
DISCONFIRMING_OBSERVATION: >
  An activity is found in a state where it has no individual owner and does not inherit responsibility from
  its parent opportunity's owner either.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create an activity under an opportunity without explicitly assigning it to a person, and check who, if
  anyone, is recorded as responsible for it.
```

## G09-CRM-Q043

```yaml
QID: G09-CRM-Q043
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An activity remains attached to its opportunity and retrievable in its history when the opportunity's
  pipeline stage changes, rather than being dropped or hidden as a side effect of a stage transition.
WHY_IT_MATTERS: >
  Losing activity records on a routine stage move would destroy the working history of a deal every time it
  progresses, which is the opposite of what an activity log is for.
DISCONFIRMING_OBSERVATION: >
  An opportunity's recorded activities are no longer visible or retrievable after its pipeline stage is
  changed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Record an activity against an opportunity, change the opportunity's pipeline stage, and check whether the
  activity is still visible in its history.
```

## G09-CRM-Q044

```yaml
QID: G09-CRM-Q044
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Marking an opportunity won or lost does not automatically and silently delete its still-open, uncompleted
  activities; they either remain visible as historical record or are explicitly closed out in a way
  distinguishable from having been completed by someone.
WHY_IT_MATTERS: >
  Silently deleting open activities on closure would erase evidence of what was still pending when the deal
  closed, useful for both process improvement and dispute resolution.
DISCONFIRMING_OBSERVATION: >
  Marking an opportunity won or lost causes its open, uncompleted activities to disappear entirely, or to
  display as completed by a person when no one actually completed them.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Leave an open, uncompleted activity on an opportunity, mark that opportunity won or lost, and check the
  activity's state afterward.
```

## G09-CRM-Q045

```yaml
QID: G09-CRM-Q045
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Deactivating the account of a person who owns open activities does not delete those activities; they remain
  visible and are identifiable as needing redistribution to an active owner.
WHY_IT_MATTERS: >
  Activities silently deleted along with a departing employee's account represent lost customer commitments
  with no chance for anyone to pick them back up.
DISCONFIRMING_OBSERVATION: >
  Deactivating a person's account causes their still-open activities to be deleted, or to become invisible to
  anyone else, rather than remaining discoverable for reassignment.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create open activities owned by a specific person, deactivate that person's account, and check whether the
  activities still exist and are discoverable.
```

## G09-CRM-Q046

```yaml
QID: G09-CRM-Q046
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Removing a pipeline stage from the configured stage set while one or more opportunities currently sit in
  that stage either blocks the removal or forces an explicit resolution, such as reassigning those
  opportunities to another stage, rather than leaving them silently pointing at a stage that no longer exists
  in the configuration.
WHY_IT_MATTERS: >
  Opportunities stranded in a stage that has been deleted from the configuration could vanish from
  stage-based views entirely, effectively hiding live pipeline.
DISCONFIRMING_OBSERVATION: >
  A pipeline stage holding open opportunities is removed from configuration, and those opportunities are left
  referencing a stage that no longer exists with no resolution offered.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Place an opportunity in a specific pipeline stage, attempt to remove that stage from the configured stage
  set, and observe what happens to the opportunity and whether the removal is blocked or resolved.
```

## G09-CRM-Q047

```yaml
QID: G09-CRM-Q047
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Reordering the sequence of pipeline stages in configuration, without deleting any stage, does not by itself
  silently change the probability value already recorded on opportunities currently sitting in those stages.
WHY_IT_MATTERS: >
  A configuration action as routine as reordering stages for display purposes should not have the side effect
  of quietly rewriting every open deal's forecast probability.
DISCONFIRMING_OBSERVATION: >
  Reordering the configured sequence of pipeline stages changes the recorded probability on opportunities
  already sitting in an unmodified stage.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Note the probability of an opportunity in a given stage, reorder the stage sequence in configuration without
  changing that stage's own settings, and compare the opportunity's probability before and after.
```

## G09-CRM-Q048

```yaml
QID: G09-CRM-Q048
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Renaming a pipeline stage, changing only its label, is distinguishable, in any historical reporting that
  groups past opportunities by the stage they were in, from having deleted the old stage and created an
  unrelated new one with a similar name.
WHY_IT_MATTERS: >
  If a rename is indistinguishable from a delete-and-recreate, historical stage-based reporting would show a
  discontinuity for no real operational reason, or worse, silently merge two genuinely different stages that
  happened to share a similar label.
DISCONFIRMING_OBSERVATION: >
  Renaming a pipeline stage causes historical reports that group past opportunities by stage to either lose
  track of opportunities previously associated with that stage, or to be unable to distinguish the renamed
  stage from an unrelated new one.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Record which stage several closed opportunities were in historically, rename that stage's label, and check
  whether historical reporting still correctly attributes those opportunities to it.
```

## G09-CRM-Q049

```yaml
QID: G09-CRM-Q049
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A change to the pipeline stage configuration, adding, removing, or reordering stages, made for one team or
  company scope does not by itself alter the stage configuration or the opportunities of a different team or
  company sharing the same environment.
WHY_IT_MATTERS: >
  If stage configuration is not properly scoped, one team's process change could silently disrupt an entirely
  unrelated team's pipeline structure.
DISCONFIRMING_OBSERVATION: >
  Changing the pipeline stage configuration for one team or company also changes the available stages or the
  stage assignments of opportunities belonging to a different team or company.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure distinct pipeline stage sets for two different teams or companies, change one team's stage
  configuration, and check whether the other team's configuration or opportunities are affected.
```

## G09-CRM-Q050

```yaml
QID: G09-CRM-Q050
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Changing the default probability value configured for a pipeline stage updates the forecast contribution
  only of opportunities whose probability was still following that stage default, and does not silently
  override a probability a person had already manually set on an individual opportunity.
WHY_IT_MATTERS: >
  If a configuration change overrides individually recorded judgment, a salesperson's deliberate assessment
  of a specific deal is erased by an administrative action they may not even know happened.
DISCONFIRMING_OBSERVATION: >
  Changing a stage's default probability configuration also changes the probability of an opportunity in that
  stage whose probability had been manually set to a different value.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Manually set a specific probability on an opportunity that differs from its stage's default, then change
  the stage's default probability configuration, and check whether the individually set value changes.
```

## G09-CRM-Q051

```yaml
QID: G09-CRM-Q051
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A change to the currency exchange rate used for reporting does not retroactively change the expected value
  recorded against an opportunity in its original currency at the time it was set; only the converted
  reporting figure moves, not the underlying recorded value.
WHY_IT_MATTERS: >
  If the exchange-rate change corrupts the originally recorded value itself rather than just a converted view
  of it, the deal's actual recorded commitment becomes a moving target with no real event behind the change.
DISCONFIRMING_OBSERVATION: >
  A change to the currency exchange rate used for reporting alters the expected value stored against an
  opportunity in its own original currency.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record an opportunity's expected value in a currency different from the reporting currency, change the
  exchange rate configuration, and compare the opportunity's own recorded value in its original currency
  before and after.
```

## G09-CRM-Q052

```yaml
QID: G09-CRM-Q052
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A rollup forecast figure for a past, already-closed reporting period is stable and does not change value
  later purely because current pipeline configuration, such as the stage set, default probabilities, or
  currency rates, was subsequently altered.
WHY_IT_MATTERS: >
  A closed period's reported forecast outcome moving retroactively, with no new event in that period, would
  make historical performance reporting untrustworthy as a record of what was actually reported and decided
  on at the time.
DISCONFIRMING_OBSERVATION: >
  A forecast figure previously generated and recorded for an already-closed reporting period produces a
  different value when regenerated later, purely as a result of an unrelated configuration change made
  afterward.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Generate and record a forecast figure for a closed reporting period, change pipeline stage or currency
  configuration afterward, regenerate the same historical figure, and compare the two.
```

## G09-CRM-Q053

```yaml
QID: G09-CRM-Q053
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A salesperson's default view of the pipeline shows only opportunities within their own team or company
  scope, and seeing pipeline belonging to another team or company requires an explicit broader permission
  rather than being the default.
WHY_IT_MATTERS: >
  If cross-team or cross-company visibility is the default, salespeople and managers can see, and potentially
  act on, pipeline belonging to an entirely different part of the organization, undermining territory and
  confidentiality boundaries.
DISCONFIRMING_OBSERVATION: >
  A salesperson with no cross-team or cross-company permission granted can see opportunities belonging to a
  different team or company in their standard pipeline view.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  As a salesperson scoped to one team or company with no additional visibility granted, check whether
  opportunities belonging to a different team or company appear in the standard pipeline view.
```

## G09-CRM-Q054

```yaml
QID: G09-CRM-Q054
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A manager's rollup view across multiple teams or companies they are responsible for aggregates pipeline
  data correctly without allowing them to directly edit records outside their own direct scope, keeping
  visibility and edit rights as separate permissions.
WHY_IT_MATTERS: >
  Conflating "can see the rollup number" with "can act on the underlying record" would let a rollup-level
  manager make unauthorized changes to pipeline they were only meant to monitor, not manage directly.
DISCONFIRMING_OBSERVATION: >
  A manager with rollup visibility across multiple teams is able to directly edit an opportunity belonging to
  a team outside their own direct management scope.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Grant a manager rollup visibility across teams they do not directly manage, and attempt to edit an
  opportunity belonging to one of those other teams.
```

## G09-CRM-Q055

```yaml
QID: G09-CRM-Q055
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  When the same customer contact has separate, legitimate business relationships recorded under two different
  companies in a multi-company setup, an opportunity opened under one company does not become visible by
  default to salespeople who only have access to the other company.
WHY_IT_MATTERS: >
  A shared customer across company boundaries should not automatically dissolve the intended separation
  between the two companies' pipelines, which may serve entirely different business lines or reporting
  entities.
DISCONFIRMING_OBSERVATION: >
  An opportunity created under one company for a shared customer contact is visible by default to a
  salesperson scoped only to a different company.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Create opportunities for the same customer contact under two different companies, and check whether a
  salesperson scoped to only one company can see the opportunity recorded under the other.
```

## G09-CRM-Q056

```yaml
QID: G09-CRM-Q056
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Reassigning an opportunity across a company or team boundary, from an owner in one scope to an owner in
  another, is either blocked or requires an explicit action that visibly crosses that boundary, rather than
  being possible through the same routine reassignment step used within a single team.
WHY_IT_MATTERS: >
  If a cross-boundary reassignment is indistinguishable from an ordinary one, pipeline and its associated
  customer relationship could move across an organizational boundary without anyone deliberately deciding
  that should happen.
DISCONFIRMING_OBSERVATION: >
  An opportunity is reassigned from an owner in one company or team to an owner in a different one using the
  same unmarked action as a routine within-team reassignment, with no distinct indication that a boundary was
  crossed.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Reassign an opportunity from an owner in one team or company to an owner in a different one, and observe
  whether the action is distinguished in any way from an ordinary same-scope reassignment.
```

## G09-CRM-Q057

```yaml
QID: G09-CRM-Q057
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Every change to an opportunity's stage, probability, expected value, close date, or owner is recorded with
  who made the change and when, forming a trail that can be reviewed independently of the current state of
  the record.
WHY_IT_MATTERS: >
  Without this, no governance review of pipeline integrity can ever establish what actually happened to a
  deal over time, only what it looks like right now.
DISCONFIRMING_OBSERVATION: >
  At least one of these fields, stage, probability, expected value, close date, or owner, can be changed with
  no resulting entry anywhere describing who changed it or when.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change each of the listed fields on an opportunity in turn and check, for each, whether a corresponding
  change record exists showing who and when.
```

## G09-CRM-Q058

```yaml
QID: G09-CRM-Q058
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a change to a field is logged, the log entry preserves the prior value, not merely the fact that a
  change occurred, so the actual before-and-after can be reconstructed.
WHY_IT_MATTERS: >
  A log that records only that a change occurred, with no prior value, is not useful evidence; it cannot
  answer the single most important question a review would ask, which is what the number used to be.
DISCONFIRMING_OBSERVATION: >
  A change log entry for a field change records that a change occurred but does not preserve what the value
  was immediately before the change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change a tracked field on an opportunity and inspect the resulting log entry for whether the prior value is
  present, not only the fact of a change.
```

## G09-CRM-Q059

```yaml
QID: G09-CRM-Q059
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A record created or modified through a bulk import process carries the same change-attribution and history
  as a record created or modified through the normal interface, rather than the import process bypassing the
  audit trail entirely.
WHY_IT_MATTERS: >
  If bulk import is a way to change or create records with no audit trail, it becomes the obvious route for
  making an untraceable change to the pipeline at scale.
DISCONFIRMING_OBSERVATION: >
  An opportunity value changed through a bulk import process shows no change-attribution record, while the
  same change made through the normal interface would have produced one.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Change the same field on two comparable opportunities, one through a bulk import process and one through
  the normal interface, and compare whether both produce an equivalent audit record.
```

## G09-CRM-Q060

```yaml
QID: G09-CRM-Q060
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A change made through an automated background process, for example a scheduled rule or an automatic
  assignment, is attributed in the audit trail as having been made by that automated process, distinguishable
  from a change made directly by a person.
WHY_IT_MATTERS: >
  If automated changes are recorded as if a specific person made them, or with no distinguishable actor at
  all, a review cannot tell the difference between a person's deliberate action and a system rule firing,
  which is exactly the distinction needed to explain an unexpected change.
DISCONFIRMING_OBSERVATION: >
  A change made by an automated background process appears in the audit trail attributed to a specific person
  who did not make it, or with no way to tell it apart from a manual change.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Trigger a change through an automated background process and a comparable manual change by a person, and
  compare how each is attributed in the audit trail.
```

## G09-CRM-Q061

```yaml
QID: G09-CRM-Q061
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Personal contact information captured about a person through an inbound interest, someone who has not yet
  and may never become a paying customer, records the basis on which that information is being held,
  distinguishable from information about someone who is already an established customer.
WHY_IT_MATTERS: >
  A person who merely expressed interest has a different, and generally weaker, relationship basis for the
  business holding their personal data than an existing customer does, and the two must not be treated
  identically for governance purposes.
DISCONFIRMING_OBSERVATION: >
  There is no way to distinguish, for a given personal contact record, whether it was captured from a mere
  inbound interest or from an existing customer relationship, and no separate basis is recorded for holding
  the interest-only contact's information.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Capture personal contact information from an inbound interest that has no other relationship with the
  business, and check whether any basis for holding that information is recorded and distinguishable from an
  established customer's record.
```

## G09-CRM-Q062

```yaml
QID: G09-CRM-Q062
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An opportunity, and the personal data of the individual it concerns, that has been marked lost and inactive
  for an extended period is subject to some identifiable retention expectation, whether a defined period, a
  review flag, or an explicit indefinite-hold decision, rather than persisting by default with no owner ever
  having decided how long it should be kept.
WHY_IT_MATTERS: >
  Personal data about a person who never became a customer, kept indefinitely by default with no one having
  actually decided to keep it, is exactly the exposure a retention policy exists to prevent.
DISCONFIRMING_OBSERVATION: >
  A lost, long-inactive opportunity holding personal data about a non-customer shows no retention period,
  review flag, or any other indication that its continued retention was ever a deliberate decision.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Locate or create a lost opportunity with personal contact data that has been inactive for a long period, and
  check whether any retention period, review flag, or deliberate retention decision is recorded against it.
```

## G09-CRM-Q063

```yaml
QID: G09-CRM-Q063
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When an opportunity, along with the personal data it carries, is routed or made visible to a party outside
  the immediate organization, such as a partner or an external service the record is shared with, that
  disclosure is recorded, identifying what was shared, to whom, and when.
WHY_IT_MATTERS: >
  An unrecorded disclosure of personal data to an outside party leaves the business unable to answer the most
  basic accountability question a data-protection review or an affected individual could ask: who else has
  seen this information.
DISCONFIRMING_OBSERVATION: >
  An opportunity's personal data is shared with or made visible to an external party with no record anywhere
  of what was disclosed, to whom, or when.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Arrange for an opportunity's personal data to be shared with or made visible to a party outside the
  immediate organization, and check whether a record of that disclosure exists afterward.
```

## G09-CRM-Q064

```yaml
QID: G09-CRM-Q064
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a person exercises a right to know what personal data is held about them, the response can be
  assembled to include not just their basic contact record but the personal-data-bearing content recorded in
  activities, notes, and history attached to any opportunity concerning them, not just the top-level contact
  fields.
WHY_IT_MATTERS: >
  A subject access response limited to top-level contact fields while omitting personal details embedded in
  activity notes or history would be materially incomplete, understating what the business actually holds
  about the person.
DISCONFIRMING_OBSERVATION: >
  Attempting to assemble everything held about a specific individual surfaces only their top-level contact
  fields and misses personal-data-bearing content recorded in activities, notes, or history tied to
  opportunities about them.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Record personal details about an individual both in their top-level contact fields and within the free-text
  notes or activities of an opportunity concerning them, then attempt to assemble everything held about that
  individual and check what is actually surfaced.
```

## G09-CRM-Q065

```yaml
QID: G09-CRM-Q065
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A request to erase a specific individual's personal data is resolved differently depending on whether that
  data sits on a still-open, actively pursued opportunity versus one that is closed and historical, with the
  conflict between erasure and any legitimate ongoing business need made explicit rather than the request
  being either silently ignored or blindly executed regardless of context.
WHY_IT_MATTERS: >
  Blind execution could delete personal data still needed for a live, legitimate business relationship, while
  silent refusal defeats the erasure request entirely; neither failure mode is acceptable, and the difference
  has to be visible to whoever is handling the request.
DISCONFIRMING_OBSERVATION: >
  An erasure request against personal data on an open, actively pursued opportunity is either executed with no
  acknowledgment of the conflict with the ongoing relationship, or is silently dropped with no outcome
  recorded at all.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit an erasure request for the personal data of an individual who has an open, actively pursued
  opportunity, and observe how the request is handled and recorded.
```

## G09-CRM-Q066

```yaml
QID: G09-CRM-Q066
MODULE: crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Withdrawal of marketing consent by an individual, for example opting out of promotional contact, is recorded
  as distinct from, and does not automatically remove or block, an active salesperson's ability to continue
  direct, individual outreach on an open opportunity that the individual is themselves a party to.
WHY_IT_MATTERS: >
  Conflating a marketing opt-out with a block on all direct communication could break an active sales
  conversation the individual actually wants to continue, while failing to distinguish them in the other
  direction could mean a marketing opt-out is ignored entirely because it was recorded as if it were the same
  thing as an active-deal communication preference.
DISCONFIRMING_OBSERVATION: >
  Withdrawing marketing consent either has no recorded effect distinguishable from having no consent
  preference at all, or it also blocks or removes the salesperson's ability to directly communicate about
  their own open, active opportunity with that same individual.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record a marketing consent withdrawal for an individual who is also the subject of an open, actively worked
  opportunity, and check both whether the withdrawal is distinctly recorded and whether it affects the
  salesperson's ability to continue direct outreach on that opportunity.
```
