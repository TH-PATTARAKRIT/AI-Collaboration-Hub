# GMVQ MODULE-SPECIFIC QUESTION BANK

**Document ID:** G09-CRM_LIVECHAT-GMVQ-MVQ-050-V1.00-DRAFT
**Group:** G09 CRM
**Module Metadata:** crm_livechat
**Wave:** W2
**Author Cell:** P-C3
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Purpose:** Module-specific research questions (MVQ) for the blind two-lane Clean Room study of the
module whose seam is a live conversation becoming an opportunity, wherever that conversation happens
(not limited to the public website — see the sibling bank for that narrower seam). Lane A answers these
against reference source; Lane B answers the same QIDs against runtime observation only. Neither lane
sees the other's answers or working notes. The standard bank (55 questions, shared across all G09
modules) is authored and frozen separately and is not reproduced in this file.
**Control:** Governed by `GMVQ_AUTHORING_STANDARD_V1.00.md` and `GMVQ_BRIDGE_MODULE_RULE_V1.00.md`.
This module is named `crm_livechat` (an `A_B` bridge per the Bridge Module Rule): every question below
passes the seam test — if the live-conversation capability were removed and the base pipeline used with
no conversational channel at all, the question would no longer make sense. Clean Room: no vendor name,
product name, table/field/method name, or other technical identifier appears in any HYPOTHESIS,
WHY_IT_MATTERS, DISCONFIRMING_OBSERVATION, or PRECONDITIONS field below. DRAFT ONLY — not approved,
not frozen, not verified, not MASTER-ready.

**Pre-authoring sibling check (Bridge Module Rule §5):** `grep -h 'HYPOTHESIS: >' -A1` was run against
every file then present in `01_QUESTION_BANKS/G09_CRM/` (base `crm` bank, `crm_iap_enrich`,
`website_crm_partner_assign`) before authoring. No overlap found: those banks cover forecast/stage
mechanics, paid-enrichment provenance, and partner routing respectively, none of which touch the
conversation-to-opportunity seam this bank studies. This bank's own cross-check against its sibling
`website_crm_livechat` is recorded in that sibling's header.

## Seam ground index
1. Q001-Q005 — the moment an opportunity exists, and who decides
2. Q006-Q010 — transfer between operators mid-conversation, and resulting ownership
3. Q011-Q015 — several conversations with one person over time, and whether they merge or split
4. Q016-Q020 — the transcript as attached evidence, and its editability afterward
5. Q021-Q025 — a conversation abandoned mid-way, and whether a partial opportunity remains
6. Q026-Q030 — operator availability, and conversations that receive no operator at all
7. Q031-Q035 — expected value set from a conversation with no commercial content
8. Q036-Q040 — an opportunity created from what was actually a support complaint
9. Q041-Q045 — retention of transcripts containing personal detail
10. Q046-Q050 — concurrency when two operators act on one conversation

---

```yaml
QID: G09-CRM_LIVECHAT-Q001
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A live conversation converts to an opportunity at one identifiable point in the exchange, not across
  an ambiguous window that could be read differently by different observers.
WHY_IT_MATTERS: >
  If the creation point is fuzzy, two people reviewing the same conversation could disagree about
  whether, or when, a sales opportunity actually began, undermining every downstream figure that
  depends on that moment (assignment, forecast timing, response-time metrics).
DISCONFIRMING_OBSERVATION: >
  Two independent reviews of the same conversation transcript identify different turns as the moment an
  opportunity exists, or the system itself cannot report a single turn or action that triggered creation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Have one complete conversation transcript that resulted in an opportunity, and the ability to inspect
  the record's creation timestamp/trigger alongside the transcript's turn-by-turn timestamps.
```

```yaml
QID: G09-CRM_LIVECHAT-Q002
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether an opportunity is created automatically from a conversation, or only after a deliberate
  operator action, is a configurable choice rather than a fixed, unchangeable behaviour.
WHY_IT_MATTERS: >
  A business that wants every serious inquiry captured needs automatic creation; a business worried
  about noise needs operator judgment in the loop. If this is not configurable, one class of business
  is permanently mismatched.
DISCONFIRMING_OBSERVATION: >
  The creation trigger behaves identically regardless of any setting changed, or no such setting is
  exposed anywhere reachable by an administrator.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Access to the channel's administrative configuration area and the ability to run the same
  conversation script under two different settings.
```

```yaml
QID: G09-CRM_LIVECHAT-Q003
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A conversation that never receives any operator response does not, by itself, generate an opportunity
  attributed to a person who took no part in it.
WHY_IT_MATTERS: >
  An unattended queue silently producing owned opportunities would assign accountability to staff for
  work they never did, and would corrupt performance and forecast figures built on ownership.
DISCONFIRMING_OBSERVATION: >
  An opportunity appears with a named human owner after a conversation in which that person sent no
  message and took no recorded action.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  A conversation that reaches the channel with no operator ever joining or replying, observed through
  to its natural close.
```

```yaml
QID: G09-CRM_LIVECHAT-Q004
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Converting a conversation into an opportunity requires a role with authority over the pipeline, not
  merely the ability to participate in the conversation.
WHY_IT_MATTERS: >
  If any conversation participant can write into the pipeline, the boundary between a support/service
  function and the sales pipeline collapses, and unqualified records enter forecast data.
DISCONFIRMING_OBSERVATION: >
  A participant holding no pipeline-related role is able to trigger opportunity creation from a
  conversation they are in.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Two operator accounts, one with pipeline permissions and one without, each handling a comparable
  conversation.
```

```yaml
QID: G09-CRM_LIVECHAT-Q005
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A conversation that closes with an explicit outcome of no interest does not go on to produce an
  opportunity record.
WHY_IT_MATTERS: >
  Counting explicit declines as open pipeline inflates the forecast with prospects who have already
  said no, misleading anyone who reads the pipeline as a measure of real, live interest.
DISCONFIRMING_OBSERVATION: >
  An opportunity record exists and remains open for a conversation whose recorded outcome was an
  explicit statement of no interest.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A conversation carried through to an explicit "not interested" outcome recorded by the operator or
  the visitor.
```

```yaml
QID: G09-CRM_LIVECHAT-Q006
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a conversation is transferred between operators before an opportunity is created, the resulting
  opportunity's ownership follows a defined rule rather than whichever operator happened to save last.
WHY_IT_MATTERS: >
  Without a defined rule, ownership becomes an accident of timing, and two operators who both worked
  the same conversation have no way to know, or dispute, who is credited with it.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical transfer scenarios, differing only in the order actions were saved, produce
  different final owners with no stated rule explaining the difference.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A conversation handled first by one operator and then handed to a second before conversion, with the
  ability to vary which operator performs the final action.
```

```yaml
QID: G09-CRM_LIVECHAT-Q007
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A conversation cannot be simultaneously transferred to, and acted on by, two operators in a way that
  produces two separate opportunities from the one conversation.
WHY_IT_MATTERS: >
  Two opportunities from a single conversation double-counts the same prospect in the pipeline and
  creates two competing owners for what is, to the customer, one interaction.
DISCONFIRMING_OBSERVATION: >
  One conversation transcript is found attached as evidence to more than one opportunity record.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Two operator sessions able to act on the same conversation at effectively the same time.
```

```yaml
QID: G09-CRM_LIVECHAT-Q008
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A transfer between operators is recorded in a way that distinguishes who actually spoke with the
  visitor at each point from who ends up owning the resulting opportunity.
WHY_IT_MATTERS: >
  Without that distinction, later review of a disputed or escalated case cannot tell who actually made
  which commitment to the customer.
DISCONFIRMING_OBSERVATION: >
  The record shows only a final owner, with no trace of the earlier operator(s) who were part of the
  same conversation before the transfer.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  A conversation with at least one transfer, followed by conversion to an opportunity.
```

```yaml
QID: G09-CRM_LIVECHAT-Q009
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An operator going offline mid-transfer leaves the conversation in a recognizable, recoverable state
  rather than a silent dead end that never surfaces to anyone.
WHY_IT_MATTERS: >
  A conversation stuck in limbo because the receiving operator disappeared mid-handoff can lose a live
  prospect with nobody aware it happened.
DISCONFIRMING_OBSERVATION: >
  A conversation whose receiving operator went offline during transfer remains unassigned and unlisted
  in any queue or alert visible to another operator or supervisor.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  A transfer initiated to an operator account that is then made unavailable before accepting it.
```

```yaml
QID: G09-CRM_LIVECHAT-Q010
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Transfers across different teams or departments are governed by an explicit assignment rule rather
  than being permitted, or blocked, as an incidental side effect of unrelated settings.
WHY_IT_MATTERS: >
  Cross-team handoffs need a deliberate rule, or unqualified conversations end up owned by teams with
  no mandate to work them.
DISCONFIRMING_OBSERVATION: >
  A conversation transferred to an operator in an entirely unrelated team is accepted and converted with
  no rule, warning, or record of the cross-team nature of that move.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Operator accounts belonging to two clearly distinct teams, with a transfer attempted between them.
```

```yaml
QID: G09-CRM_LIVECHAT-Q011
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Repeat conversations from a person already known to the business are matched to that existing contact
  rather than each spawning a new, separate contact identity.
WHY_IT_MATTERS: >
  Fragmenting one real person into several contact records scatters their history, defeats
  deduplication, and misrepresents how many distinct prospects the business actually has.
DISCONFIRMING_OBSERVATION: >
  A second conversation from a person who already has an existing contact record produces a brand-new,
  separate contact rather than linking to the existing one, with no matching attempted.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An existing contact record with identifying detail, and a second conversation from that same person
  using consistent identifying detail.
```

```yaml
QID: G09-CRM_LIVECHAT-Q012
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Whether a second conversation on the same subject extends an already-open opportunity or always
  creates a new one is a defined, stated rule rather than accidental behaviour.
WHY_IT_MATTERS: >
  Without a stated rule, the pipeline could show either an artificially split history or an artificially
  merged one, and nobody could say which was intended.
DISCONFIRMING_OBSERVATION: >
  Two otherwise-identical repeat-conversation scenarios (same contact, same subject, same time gap) are
  found to behave differently with no configuration difference to explain it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  An open opportunity from a first conversation, and a second conversation from the same contact on a
  closely related subject shortly afterward.
```

```yaml
QID: G09-CRM_LIVECHAT-Q013
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Any time-window or subject-matching setting that governs merging versus splitting of repeat
  conversations is exposed as an explicit, inspectable configuration.
WHY_IT_MATTERS: >
  A hidden, hard-coded window that a business cannot see or adjust prevents them from tuning the
  behaviour to their own sales cycle.
DISCONFIRMING_OBSERVATION: >
  The merge/split behaviour changes at some time boundary that cannot be located in any configuration
  screen or documentation reachable by an administrator.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Repeat conversations spaced at varying intervals from the same contact.
```

```yaml
QID: G09-CRM_LIVECHAT-Q014
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Conversations from the same person about clearly unrelated subjects are not silently folded into a
  single opportunity's history.
WHY_IT_MATTERS: >
  Merging unrelated conversations into one opportunity muddies the record a salesperson relies on and
  can misattribute one subject's outcome to an unrelated one.
DISCONFIRMING_OBSERVATION: >
  A conversation about a subject unrelated to an already-open opportunity is appended to that
  opportunity's history rather than treated as a separate matter.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An open opportunity on one subject and a new conversation from the same contact on a clearly
  different subject.
```

```yaml
QID: G09-CRM_LIVECHAT-Q015
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an opportunity is already open for a contact, a new conversation from that same contact is
  attached to the existing opportunity rather than creating a second, competing one on the same matter.
WHY_IT_MATTERS: >
  Two competing opportunities for the same live deal split the forecast value and can cause two
  salespeople to independently pursue, and possibly offer conflicting terms to, the same prospect.
DISCONFIRMING_OBSERVATION: >
  A second, separate opportunity is created for the same contact and same subject while the first is
  still open, with no link or reference between the two.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An already-open opportunity for a contact, and a new conversation from that same contact continuing
  the same subject.
```

```yaml
QID: G09-CRM_LIVECHAT-Q016
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Once a transcript is attached to an opportunity as evidence, the operator who produced it cannot
  subsequently edit its content in place.
WHY_IT_MATTERS: >
  An editable evidentiary record defeats its own purpose — it can no longer be relied on to show what
  was actually said if the party who said it can silently change it afterward.
DISCONFIRMING_OBSERVATION: >
  The operator who took part in the conversation is able to alter the wording of their own
  already-attached transcript with no trace that a change occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A closed conversation with its transcript attached to an opportunity, and the same operator's account
  used to attempt a change to that transcript.
```

```yaml
QID: G09-CRM_LIVECHAT-Q017
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Only a role distinct from the original participants may redact or amend transcript content after the
  fact, and that action is itself distinguishable from the original record.
WHY_IT_MATTERS: >
  Legitimate redaction (for example, removing personal data on request) must remain possible without
  granting free editing rights that could be used to alter what was actually said.
DISCONFIRMING_OBSERVATION: >
  A redaction performed by an authorised role leaves the transcript indistinguishable from an unaltered
  one, with no marker that a redaction took place.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A transcript attached to an opportunity, and an account holding a redaction-capable role distinct
  from the conversation's participants.
```

```yaml
QID: G09-CRM_LIVECHAT-Q018
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Any correction made to a transcript after attachment leaves a visible trace of what changed and who
  made the change.
WHY_IT_MATTERS: >
  Without a trace, a dispute about what was actually promised to a customer cannot be resolved, and an
  improper alteration cannot be detected after the fact.
DISCONFIRMING_OBSERVATION: >
  A transcript is found to differ from an earlier saved or exported copy with no accompanying log entry
  describing the change.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  A transcript attached to an opportunity, an exported or otherwise independently saved copy of it, and
  a subsequent authorised correction to the live copy.
```

```yaml
QID: G09-CRM_LIVECHAT-Q019
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Content inserted into the conversation by an automated aid (for example, a suggested reply or an
  automatic translation) is distinguishable in the record from what the human operator or visitor
  actually typed themselves.
WHY_IT_MATTERS: >
  Treating machine-inserted content as if a person said it verbatim misrepresents the actual human
  exchange when the transcript is later relied on as evidence.
DISCONFIRMING_OBSERVATION: >
  A message inserted by an automated aid appears in the transcript with no marker distinguishing it
  from a message the operator or visitor typed themselves.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A conversation in which at least one automated aid contributed content, carried through to an
  attached transcript.
```

```yaml
QID: G09-CRM_LIVECHAT-Q020
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether the transcript is attached to the opportunity automatically upon creation, or requires a
  manual action, is a defined behaviour, and if the manual step is skipped, the opportunity is not
  silently left without any evidentiary record.
WHY_IT_MATTERS: >
  An opportunity with no attached evidence cannot later be defended, audited, or reviewed against what
  was actually said, and a silent skip would go unnoticed until it mattered.
DISCONFIRMING_OBSERVATION: >
  An opportunity created from a conversation exists with no transcript attached, and nothing in the
  record flags that the attachment step did not happen.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  A conversion path in which the transcript-attachment step can be deliberately skipped or interrupted.
```

```yaml
QID: G09-CRM_LIVECHAT-Q021
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A conversation the visitor abandons before any commercial content is exchanged does not, on that
  basis alone, produce an opportunity.
WHY_IT_MATTERS: >
  Counting bare abandonments as pipeline manufactures phantom prospects with no real interest behind
  them, inflating counts that management reads as a measure of demand.
DISCONFIRMING_OBSERVATION: >
  An opportunity exists for a conversation whose entire content, before abandonment, contained no
  expression of interest, request, or commercial content of any kind.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A conversation opened and abandoned by the visitor with only greeting-level or no content exchanged.
```

```yaml
QID: G09-CRM_LIVECHAT-Q022
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An opportunity created from a conversation that is later abandoned mid-way is left in an identifiable
  stalled or incomplete state, rather than silently disappearing or silently advancing as if it had
  concluded normally.
WHY_IT_MATTERS: >
  A salesperson working a pipeline needs to see which opportunities stalled versus which genuinely
  progressed; an indistinguishable record hides real risk in the forecast.
DISCONFIRMING_OBSERVATION: >
  An opportunity from an abandoned conversation carries the same status as one from a conversation that
  reached a normal, complete close.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An opportunity already created from a conversation that is then abandoned by the visitor before
  reaching any conclusion.
```

```yaml
QID: G09-CRM_LIVECHAT-Q023
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The length of inactivity after which a conversation is treated as abandoned is a defined, and
  ideally configurable, threshold rather than an arbitrary or undocumented cutoff.
WHY_IT_MATTERS: >
  Too short a threshold wrongly abandons live conversations; too long a threshold leaves operators and
  visitors in limbo. A business needs to be able to see and tune this.
DISCONFIRMING_OBSERVATION: >
  The point at which an inactive conversation is treated as abandoned cannot be found in any
  configuration or documentation, and differs between otherwise identical test cases.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Two otherwise identical conversations left inactive for different lengths of time.
```

```yaml
QID: G09-CRM_LIVECHAT-Q024
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A premature opportunity created from a conversation that turned out to be abandoned can be reversed,
  merged, or withdrawn without leaving a misleading "lost" record if the same visitor later returns and
  genuinely engages.
WHY_IT_MATTERS: >
  A false lost record on a prospect who actually came back and converted misrepresents both that
  salesperson's performance and the true win rate for the pipeline.
DISCONFIRMING_OBSERVATION: >
  A visitor who abandoned once, generating a premature opportunity, then returns and completes a
  genuine engagement, but the system leaves the original abandonment permanently recorded as a lost
  outcome alongside the new one with no link or correction path.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A first abandoned conversation that created an opportunity, followed by a later, genuine return
  conversation from the same visitor.
```

```yaml
QID: G09-CRM_LIVECHAT-Q025
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A conversation the visitor has left, but which the operator has not yet closed, is treated differently
  from one the operator has actively closed, rather than both being folded into the same ended state
  with no distinction.
WHY_IT_MATTERS: >
  An operator working from a queue needs to know whether a conversation ended because the customer left
  or because it was deliberately concluded; conflating the two hides genuinely still-open work.
DISCONFIRMING_OBSERVATION: >
  A conversation left open on the operator's side after the visitor disconnects is reported in exactly
  the same state and appears in exactly the same lists as one the operator explicitly closed.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  One conversation ended by visitor disconnect with the operator side left open, and one conversation
  explicitly closed by the operator, compared side by side.
```

```yaml
QID: G09-CRM_LIVECHAT-Q026
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A conversation begun when no operator is available is captured with a status that distinguishes it
  from a conversation an operator actually attended.
WHY_IT_MATTERS: >
  Treating an unattended conversation identically to an attended one hides a real service gap and can
  misattribute credit or blame for outcomes nobody actually influenced.
DISCONFIRMING_OBSERVATION: >
  A conversation started with zero operators available carries the same status markers as one where an
  operator was present and responded.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  The channel configured or scheduled so that no operator is available, and a visitor conversation
  started during that window.
```

```yaml
QID: G09-CRM_LIVECHAT-Q027
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An availability or staffing schedule can be configured for the channel, and that schedule has an
  actual, observable effect on whether an opportunity can be created outside those hours.
WHY_IT_MATTERS: >
  A business that only staffs certain hours needs the system's behaviour to reflect that; if the
  schedule has no real effect, it is decoration rather than a control.
DISCONFIRMING_OBSERVATION: >
  Changing the configured availability schedule produces no observable difference in whether or how
  opportunities are created outside the scheduled hours.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Ability to change the channel's staffing schedule and run comparable conversations inside and outside
  the configured hours.
```

```yaml
QID: G09-CRM_LIVECHAT-Q028
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An automated responder handling a conversation with no human operator involved does not, on its own,
  produce an opportunity attributed to a specific human operator.
WHY_IT_MATTERS: >
  Attributing automated interactions to a named person falsifies that person's activity record and can
  trigger performance credit, notifications, or accountability for work they did not do.
DISCONFIRMING_OBSERVATION: >
  An opportunity created from a conversation handled entirely by an automated responder is recorded
  with a specific human operator as its acting participant.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A conversation handled end-to-end by an automated responder with no human operator ever joining,
  resulting in an opportunity.
```

```yaml
QID: G09-CRM_LIVECHAT-Q029
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An opportunity created from an unattended conversation has a defined ownership assignment (a queue, a
  team, or an explicit unassigned state), rather than defaulting unpredictably to whichever operator is
  nearest in an unrelated setting.
WHY_IT_MATTERS: >
  Unclear ownership for unattended-conversation opportunities means nobody is accountable for following
  up, and the prospect can be silently lost.
DISCONFIRMING_OBSERVATION: >
  An opportunity from an unattended conversation is found assigned to a specific individual with no
  rule or record explaining why that person was chosen.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  An opportunity resulting from a conversation with no operator participation, and visibility into how
  its owner field was populated.
```

```yaml
QID: G09-CRM_LIVECHAT-Q030
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The fact that no operator ever engaged with a conversation remains visible on the resulting
  opportunity rather than being lost once the record is created.
WHY_IT_MATTERS: >
  A salesperson picking up the opportunity later needs to know whether they are the first human to ever
  engage, which changes how they should open the follow-up.
DISCONFIRMING_OBSERVATION: >
  An opportunity from a wholly unattended conversation is indistinguishable, once viewed later, from
  one where an operator was actively engaged throughout.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  An opportunity created from an unattended conversation, reviewed at a later point after creation.
```

```yaml
QID: G09-CRM_LIVECHAT-Q031
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The expected value recorded on an opportunity requires some originating commercial basis from the
  conversation, rather than being populated with a nonzero figure when no commercial content was ever
  discussed.
WHY_IT_MATTERS: >
  An expected value with no basis behind it is a fabricated number that still feeds directly into the
  forecast total management relies on for planning.
DISCONFIRMING_OBSERVATION: >
  An opportunity created from a conversation containing no pricing, quantity, or product discussion
  nonetheless carries a nonzero expected value.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A conversation with no commercial content of any kind, carried through to opportunity creation.
```

```yaml
QID: G09-CRM_LIVECHAT-Q032
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Any default expected-value setting applied to automatically created opportunities is visible and
  adjustable by an administrator, rather than a hidden constant.
WHY_IT_MATTERS: >
  An invisible default distorts every forecast built from this channel and cannot be corrected by the
  business if nobody can find or change it.
DISCONFIRMING_OBSERVATION: >
  Newly created opportunities from this channel carry a consistent nonzero default value that does not
  appear in, and cannot be changed from, any configuration screen.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Several opportunities created from conversations with no explicit value discussed, compared for a
  consistent default figure.
```

```yaml
QID: G09-CRM_LIVECHAT-Q033
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An expected value set from a conversation with no real commercial substance persists unchanged into
  management-facing forecast reporting unless a person deliberately intervenes to correct it.
WHY_IT_MATTERS: >
  A forecast quietly padded with baseless figures misleads planning decisions until someone happens to
  notice and fix each one individually.
DISCONFIRMING_OBSERVATION: >
  A forecast report totals in a baseless default value from an unreviewed opportunity exactly as if it
  were a substantiated figure, with no flag distinguishing it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  An unreviewed opportunity carrying a default expected value, included in a standard forecast report.
```

```yaml
QID: G09-CRM_LIVECHAT-Q034
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A currency or amount field can only be attached to an opportunity from this channel in a way that is
  meaningful, not fabricated from a channel that never captured any monetary figure at all.
WHY_IT_MATTERS: >
  If the channel structurally cannot know an amount, the field should reflect that absence rather than
  presenting a number that looks as reliable as one entered from an actual quote.
DISCONFIRMING_OBSERVATION: >
  An opportunity from this channel shows a specific currency amount with no traceable source for that
  figure anywhere in the conversation or configuration.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  An opportunity created from a conversation where no monetary figure was ever mentioned by either
  party.
```

```yaml
QID: G09-CRM_LIVECHAT-Q035
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A conversation entirely about a support question, with no mention of a new purchase, does not produce
  an opportunity carrying a nonzero expected value.
WHY_IT_MATTERS: >
  Valuing a support interaction as if it were a sales prospect misrepresents both the pipeline and the
  actual purpose of the customer's contact.
DISCONFIRMING_OBSERVATION: >
  A conversation whose entire content is a question about an existing product or service produces an
  opportunity with a nonzero expected value attached.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A conversation limited entirely to a support-type question, with no new-purchase content, carried
  through to any resulting record.
```

```yaml
QID: G09-CRM_LIVECHAT-Q036
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A conversation whose content is a complaint about an existing product or service is, at least in
  principle, distinguishable from one expressing new purchase intent before an opportunity is created
  from it.
WHY_IT_MATTERS: >
  Treating every conversation as equally likely to be a sales lead, with no distinction for complaint
  content, guarantees that dissatisfied customers get miscast as prospects.
DISCONFIRMING_OBSERVATION: >
  A conversation containing a clear complaint about an existing product or service, with no expression
  of new purchase intent, results in a sales opportunity indistinguishable from a genuine lead.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A conversation whose content is unambiguously a complaint, with no new-purchase language, carried
  through the same conversion path as any other conversation.
```

```yaml
QID: G09-CRM_LIVECHAT-Q037
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An opportunity mistakenly created from what was actually a complaint can be reclassified or withdrawn
  through a recorded action, rather than only being removable by deleting the record and losing the
  trail entirely.
WHY_IT_MATTERS: >
  Deleting a misclassified record destroys the evidence that the mistake happened at all, preventing
  the business from learning why it occurred or how often.
DISCONFIRMING_OBSERVATION: >
  The only way to remove a misclassified opportunity from the pipeline is deletion, with no
  reclassification action that preserves a record of the original conversation and the correction made.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  An opportunity created in error from a complaint-only conversation, and an attempt to correct its
  classification.
```

```yaml
QID: G09-CRM_LIVECHAT-Q038
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A complaint miscast as a sales opportunity affects the sales forecast total, and there is no automatic
  mechanism that excludes it before a person notices and corrects it.
WHY_IT_MATTERS: >
  An uncorrected miscast complaint sits in the forecast total for as long as it takes someone to spot
  it, silently overstating pipeline value in the meantime.
DISCONFIRMING_OBSERVATION: >
  A miscast complaint-opportunity is included in a forecast total identically to a genuine opportunity,
  with no distinguishing flag raised anywhere before manual review.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A miscast complaint-based opportunity left unreviewed, included in a standard forecast total.
```

```yaml
QID: G09-CRM_LIVECHAT-Q039
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The same conversation transcript can be linked to a complaint-handling record and to a sales
  opportunity only where both are genuinely warranted, not exclusively to one or automatically to both
  by default.
WHY_IT_MATTERS: >
  A conversation can legitimately contain both a resolved complaint and a genuine new interest; forcing
  an either/or link, or an automatic both, misrepresents cases that do not fit that assumption.
DISCONFIRMING_OBSERVATION: >
  A single conversation transcript is found structurally unable to be linked to both a
  complaint-handling record and a sales opportunity even where the content genuinely supports both.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A conversation containing both a resolved complaint element and a genuine new-purchase element.
```

```yaml
QID: G09-CRM_LIVECHAT-Q040
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  No rule, keyword check, or manual-flag mechanism exists that helps separate a complaint conversation
  from a genuine sales conversation before conversion — the hypothesis names this absence and asks
  whether it is in fact absent.
WHY_IT_MATTERS: >
  If no such mechanism exists at all, the complaint/opportunity confusion in this cluster has no
  safeguard anywhere in the channel, which is itself a material finding about the design.
DISCONFIRMING_OBSERVATION: >
  A configuration, keyword rule, or manual flag is found that does distinguish complaint-type
  conversations from sales-type conversations before conversion.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Full visibility into the channel's administrative configuration and conversion-triggering logic as
  exposed to an administrator.
```

```yaml
QID: G09-CRM_LIVECHAT-Q041
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A retention period or policy governs how long stored conversation transcripts are kept, and it is
  enforced rather than defaulting to indefinite storage with no policy applied.
WHY_IT_MATTERS: >
  Indefinite retention of conversations that may contain personal detail extends the business's
  exposure and obligations for as long as the data exists, with no natural end.
DISCONFIRMING_OBSERVATION: >
  Transcripts older than any stated or configured retention period remain fully present and unchanged,
  with no enforcement action ever taken against them.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Visibility into retention configuration (if any) and a transcript old enough to have exceeded a
  stated or plausible retention window.
```

```yaml
QID: G09-CRM_LIVECHAT-Q042
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Personal detail volunteered mid-conversation, typed into the chat itself, is retained as an
  undifferentiated part of the permanent evidence record, with no separate handling from the rest of
  the conversation.
WHY_IT_MATTERS: >
  Personal detail buried inside free-text evidence is much harder to find, redact, or respond to under
  a data-subject request than detail held in a structured, purpose-built field.
DISCONFIRMING_OBSERVATION: >
  A transcript containing an address or phone number typed mid-conversation shows no distinguishable
  handling, flag, or extraction compared to a transcript with no personal detail at all.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A conversation in which the visitor volunteers a piece of personal detail directly in the chat text,
  carried through to a stored transcript.
```

```yaml
QID: G09-CRM_LIVECHAT-Q043
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting or anonymizing a conversation transcript on request does not silently break, orphan, or
  falsify the opportunity record for which it was originally evidence.
WHY_IT_MATTERS: >
  A legitimate deletion request should not have the side effect of leaving a business record that looks
  complete but has quietly lost the evidence it was built on.
DISCONFIRMING_OBSERVATION: >
  Removing a transcript on request leaves the associated opportunity showing as if it always had no
  evidence attached, or breaks in a way that is only discovered later.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  An opportunity with an attached transcript, and a deletion or anonymization request carried out
  against that transcript.
```

```yaml
QID: G09-CRM_LIVECHAT-Q044
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Access to stored transcripts is itself limited and logged by role, rather than open to anyone who can
  see the opportunity the transcript is attached to.
WHY_IT_MATTERS: >
  An opportunity's ownership and visibility rules were not designed with personal-data transcripts in
  mind; without a separate access check, anyone with pipeline visibility gains transcript access too.
DISCONFIRMING_OBSERVATION: >
  A role with visibility into the opportunity, but with no stated need to view personal conversation
  content, can open and read the full transcript with no separate permission check or log entry.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Two accounts with different roles, both able to view a given opportunity, tested for transcript
  access specifically.
```

```yaml
QID: G09-CRM_LIVECHAT-Q045
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The retention configuration for stored transcripts is set per company or tenant, rather than a single
  global setting applied identically to every business sharing the same platform.
WHY_IT_MATTERS: >
  Different businesses on a shared platform may operate under different retention obligations; a single
  shared setting forces every tenant into the same policy regardless of their own requirements.
DISCONFIRMING_OBSERVATION: >
  Changing the retention setting for one company/tenant is found to also change the effective retention
  behaviour for a different, unrelated company/tenant on the same platform.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Two distinct company/tenant configurations on the same platform instance, with retention changed on
  one and observed on the other.
```

```yaml
QID: G09-CRM_LIVECHAT-Q046
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Two operators replying to the same open conversation at effectively the same time do not each
  independently trigger the creation of a separate opportunity from it.
WHY_IT_MATTERS: >
  Two opportunities from one live conversation double the apparent pipeline for a single real prospect
  and force an arbitrary later decision about which one to keep.
DISCONFIRMING_OBSERVATION: >
  A single conversation, acted on near-simultaneously by two operators, results in two distinct
  opportunity records rather than one.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Two operator sessions both able to act on the same open conversation at effectively the same moment.
```

```yaml
QID: G09-CRM_LIVECHAT-Q047
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When two operators act on one conversation in close succession, the action recorded second does not
  silently overwrite an assignment or commitment the first operator's action had already committed.
WHY_IT_MATTERS: >
  Silent overwrites mean the first operator's genuine work can vanish without either operator being
  told it happened.
DISCONFIRMING_OBSERVATION: >
  An assignment or field value set by the first operator's action is found replaced by the second
  operator's action with no conflict notice to either operator.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Two operator sessions performing conflicting actions on the same conversation in quick succession.
```

```yaml
QID: G09-CRM_LIVECHAT-Q048
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Whether a claim or lock exists to stop a second operator acting on a conversation the first has
  already claimed is a deliberate, statable design choice, not an unexamined gap.
WHY_IT_MATTERS: >
  Whichever way this is designed has consequences for accountability; not knowing which way it actually
  behaves means the business cannot rely on either assumption.
DISCONFIRMING_OBSERVATION: >
  A second operator is able to act on a conversation the first operator has already explicitly claimed,
  with no lock, warning, or record of the conflict, and no design statement exists explaining that this
  is intended.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  One operator explicitly claiming a conversation, followed by a second operator attempting to act on
  it.
```

```yaml
QID: G09-CRM_LIVECHAT-Q049
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: BASE
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When two operators did both act on one conversation, the record preserves who did what distinctly,
  rather than merging their actions into one anonymous history attributed to a single owner.
WHY_IT_MATTERS: >
  A later review or dispute about what was said or promised needs to know which of the two operators is
  responsible for which part of the exchange.
DISCONFIRMING_OBSERVATION: >
  A conversation worked by two distinct operators shows a single, undifferentiated history with no way
  to tell which operator contributed which message or action.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  A conversation genuinely worked by two different operators at different points, reviewed afterward.
```

```yaml
QID: G09-CRM_LIVECHAT-Q050
MODULE: crm_livechat
TYPE: MODULE
AUTHOR: GMVQ
LAYER: PROCESS
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  One of two concurrently active operators losing connection mid-action does not indefinitely block the
  other operator's subsequent, legitimate action on the same conversation.
WHY_IT_MATTERS: >
  A dropped session that leaves a permanent lock or inconsistent state can strand a live conversation
  with no way for a still-present operator to continue serving the visitor.
DISCONFIRMING_OBSERVATION: >
  A conversation becomes permanently unresponsive to a still-connected operator's actions after the
  other, concurrently active operator's session drops mid-action.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Two operators concurrently active on one conversation, with one operator's session forcibly
  disconnected mid-action.
```

---

**Verification note (self-check by author cell, not an independent review):** 50 fenced yaml blocks
above, QIDs G09-CRM_LIVECHAT-Q001 through Q050 contiguous with no gaps or repeats, matching the count in
the filename and in `actual_mvq_count`. RISK_TIER values used: CRITICAL, HIGH, MEDIUM only.
OUTPUT_CLASS values used: BUSINESS INVARIANT, RISK, BEHAVIOUR, CONFIGURATION, BOUNDARY only. Every
question carries a DISCONFIRMING_OBSERVATION stating a concrete failure state, not a restatement of its
HYPOTHESIS. Coverage spans business capability, business rule, state transition, configuration
dependency, role/permission, exception path, reversal, negative case, auditability, tenant boundary,
and concurrency/ordering, per the authoring standard's required dimension spread.
