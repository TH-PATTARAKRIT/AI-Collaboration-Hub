# SMEsPlus ENTERPRISE SUITE
## GMVQ — G15 PRODUCTIVITY / spreadsheet_dashboard_im_livechat Module Bridge MVQ Bank

**Document ID:** GMVQ-G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-MVQ50-V1.00
**Group:** G15 PRODUCTIVITY (Wave W4)
**Module Metadata:** `spreadsheet_dashboard_im_livechat`
**Wave:** W4
**Author Cell:** P15-2 (GMVQ Question Factory — Wave W4 Acceleration, Cell P15-2)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 50 = 105
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `spreadsheet_dashboard_im_livechat` — a 2-way
BRIDGE per GMVQ_BRIDGE_MODULE_RULE_V1.00 and GROUP_BRIEF_G15_PRODUCTIVITY.md, seam: a live
collaborative dashboard drawing volume, performance, and satisfaction rollups from real-time
conversation data it does not itself own. The underlying conversation's own routing, transfer, and
closure mechanics belong to the live-conversation base family and are deliberately NOT re-asked
here. This bank asks only what becomes true or uncertain **because a dashboard layer sits on top
of** that data: whether an aggregate or ranking indirectly discloses transcript content, an
operator's or visitor's identity, to a viewer scoped only to non-attributed figures; real-time
versus batch-refresh mismatch for a channel that is inherently live; small-sample rollups that
functionally identify one conversation or one operator; and cross-channel or cross-tenant
summation that should not have happened at the reporting layer. Every question was tested against
the bridge rule: if it would read equally well with no dashboard in the picture at all — i.e. it is
really a question about how a conversation itself is routed, rated, or closed — it was cut.

The question text is source-neutral and does not expose vendor or product names, field names,
methods, schema, XML IDs, API shapes, or implementation algorithms. `MODULE:
spreadsheet_dashboard_im_livechat` appears only in the structured metadata field, never inside
question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` stating a concrete failure state,
  never a restatement of its own hypothesis.
- No padding: 50 questions exist because they test 50 distinct material hypotheses at the seam
  between a reporting/dashboard layer and live-conversation data; none was trimmed or stretched to
  hit count.
- BRIDGE MODULE per GMVQ_BRIDGE_MODULE_RULE_V1.00: every question fails only at the seam. None
  restates a conversation routing, transfer, or closure invariant that holds with no dashboard layer
  present.
- Mandatory pre-authoring sibling check performed: `01_QUESTION_BANKS/G15_PRODUCTIVITY/` held this
  cell's own `spreadsheet_dashboard_hr_expense` and `spreadsheet_dashboard_hr_timesheet` banks on
  disk at authoring time (checked directly); their HYPOTHESIS text was reviewed and no overlap
  found. Overlap against this cell's own `spreadsheet_dashboard_sale` draft was checked directly at
  authoring time; no overlap found.
- Questions are not evidence. A later ANSWERED state requires an actual artifact/evidence.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q001

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q001
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard showing conversation volume does not require drill-down access to expose the
  transcript content of any individual conversation to a viewer who lacks operator or channel-level
  access.
WHY_IT_MATTERS: >
  A volume-only view is supposed to protect conversation content; any path from it to raw transcript
  text defeats that scoping.
DISCONFIRMING_OBSERVATION: >
  A viewer scoped to volume-only visibility can reach transcript text for an individual conversation
  through any control the dashboard offers.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a viewer scoped to aggregate volume only, attempt to reach transcript-level content through any
  interactive element of the dashboard.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q002

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q002
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A "currently active conversations" counter reflects live session state, not a cached count from
  the last scheduled refresh, when the dashboard is presented as real-time.
WHY_IT_MATTERS: >
  A stale active-count on a widget presented as live misleads a supervisor about current queue
  pressure and staffing need.
DISCONFIRMING_OBSERVATION: >
  A counter presented as real-time does not change when conversations start or end, only updating on
  its underlying scheduled refresh.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Start and end conversations while watching a counter presented as real-time and check whether it
  updates immediately or only on a scheduled refresh.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q003

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q003
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An aggregate response-time metric computed over a very small number of conversations (such as one
  operator in one hour) does not effectively identify which specific conversation drove the figure
  to a viewer who should only see aggregate performance.
WHY_IT_MATTERS: >
  A small-sample aggregate is functionally an individual-level disclosure; presenting it as if it
  were a safe rollup defeats the aggregate-only restriction.
DISCONFIRMING_OBSERVATION: >
  A response-time aggregate computed over a single conversation or a single operator-hour is shown to
  a viewer scoped to aggregate-only visibility with no suppression or minimum-sample rule applied.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Isolate a time window and operator combination with only one conversation and check whether an
  aggregate-only-scoped viewer's widget still renders a figure for it.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q004

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q004
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A conversation transferred between operators or channels is attributed to exactly one operator or
  channel in a volume rollup, not double-counted across both.
WHY_IT_MATTERS: >
  Double counting a single conversation inflates volume and per-operator load figures beyond what
  actually occurred.
DISCONFIRMING_OBSERVATION: >
  A single transferred conversation contributes to the volume count of both the originating and
  receiving operator or channel.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Transfer a conversation between two operators or channels and inspect both parties' volume
  aggregates for double counting.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q005

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q005
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A rating or satisfaction aggregate excludes conversations abandoned before a rating was actually
  given, rather than treating an absent rating as a neutral or zero score.
WHY_IT_MATTERS: >
  Silently scoring an unrated, abandoned conversation distorts a satisfaction metric in a direction
  the customer never actually expressed.
DISCONFIRMING_OBSERVATION: >
  A satisfaction average changes when an unrated, abandoned conversation is included, as though it
  contributed a real score.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have a conversation end without a rating being given and check whether it affects a satisfaction
  aggregate.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q006

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q006
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Drilling from a volume or performance tile into the underlying conversation list enforces the same
  channel or operator visibility restriction as the source conversation list, not a broader default
  scope introduced by the reporting layer.
WHY_IT_MATTERS: >
  A reporting layer more permissive than the record it summarizes turns an aggregate tile into a
  backdoor around the source module's own access control.
DISCONFIRMING_OBSERVATION: >
  A viewer restricted to one channel reaches, via drill-down, conversations belonging to a different
  channel they could not open directly.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a viewer scoped to one channel, drill down from an aggregate tile and inspect the full set of
  conversations the resulting list contains.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q007

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q007
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A dashboard combining data from multiple channels belonging to different scopes (such as different
  brands or departments) does not silently merge them into one total unless the viewer holds
  explicit cross-channel visibility.
WHY_IT_MATTERS: >
  Merging across channel boundaries without authorization exposes one brand's or department's
  conversation pattern to viewers of another.
DISCONFIRMING_OBSERVATION: >
  A viewer scoped to a single channel is shown, or a total silently includes, conversations belonging
  to a different channel they hold no cross-channel right to see.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  In a multi-channel configuration, view a volume dashboard as a single-channel-scoped user and
  check whether any total includes another channel's figures.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q008

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q008
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An operator removed or deactivated after handling conversations remains attributable in historical
  performance aggregates that already included their work, rather than that history disappearing.
WHY_IT_MATTERS: >
  A historical performance total should not shrink retroactively just because the operator who
  handled the work has since left.
DISCONFIRMING_OBSERVATION: >
  A closed-period performance aggregate drops after the contributing operator's account is
  deactivated, with no change to the underlying conversations.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Deactivate an operator whose handled conversations are already reflected in a closed-period
  aggregate and re-render that aggregate.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q009

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q009
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A scheduled or batch-refreshed livechat dashboard visibly indicates its "as of" time so a viewer
  does not mistake it for a live, second-by-second figure.
WHY_IT_MATTERS: >
  A viewer who believes a stale figure is live may misjudge current queue pressure or staffing need.
DISCONFIRMING_OBSERVATION: >
  A batch-refreshed livechat widget presents its figures with no visible timestamp or staleness
  indicator.
EXPECTED_SURFACE: S5,S8
PRECONDITIONS: >
  Identify a widget known to refresh on a schedule and inspect whether it discloses its effective
  timestamp.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q010

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q010
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A message or transcript redacted or deleted after the fact is not still counted toward a
  message-volume aggregate in a way that contradicts its removal from the visible transcript.
WHY_IT_MATTERS: >
  A volume figure that outlives a redaction contradicts the redaction's purpose and can itself hint
  at removed content's existence.
DISCONFIRMING_OBSERVATION: >
  A message-volume aggregate for a conversation does not decrease after a message within it is
  redacted or deleted.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Redact or delete a message from a conversation already reflected in a message-volume aggregate and
  re-render that aggregate.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q011

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q011
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An anonymous visitor and a later-identified version of the same visitor (such as after they log in
  mid-conversation) are not double-counted as two separate visitors in a unique-visitor aggregate.
WHY_IT_MATTERS: >
  Double counting the same person as two visitors inflates reach and engagement figures beyond
  actual unique traffic.
DISCONFIRMING_OBSERVATION: >
  A unique-visitor count increases by two, rather than one, when an anonymous visitor identifies
  themselves partway through a single conversation.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Start a conversation anonymously, identify the visitor partway through, and inspect a
  unique-visitor aggregate spanning the conversation.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q012

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q012
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A queue-length or wait-time metric only counts conversations genuinely waiting for an operator, not
  conversations already assigned but not yet actively responded to.
WHY_IT_MATTERS: >
  Conflating "waiting for assignment" with "assigned but not yet answered" misrepresents true queue
  pressure and can mask an operator who is not responding promptly.
DISCONFIRMING_OBSERVATION: >
  A queue-length figure includes a conversation already assigned to an operator, alongside genuinely
  unassigned ones, with no distinction between the two states.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Assign a conversation to an operator without an immediate response and check whether it still
  counts in the queue-length aggregate.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q013

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q013
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A business-hours-based service-level aggregate uses the business-hours configuration in effect for
  the relevant channel, not a default or differing definition introduced by the reporting layer.
WHY_IT_MATTERS: >
  A service-level figure built on the wrong business-hours definition silently misreports performance
  against the actual configured expectation.
DISCONFIRMING_OBSERVATION: >
  A service-level metric's business-hours boundary does not match the channel's actual configured
  business hours.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure distinct business hours for a channel and compare the service-level widget's actual
  boundary behaviour against that configuration.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q014

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q014
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two dashboard widgets built from the same conversation data but refreshed at different times can
  disagree, and each is distinguishable by its own refresh timestamp rather than implying equal
  currency.
WHY_IT_MATTERS: >
  Two disagreeing widgets with no way to know which is more current leave a viewer unable to decide
  which figure to trust.
DISCONFIRMING_OBSERVATION: >
  Two widgets covering the same underlying conversations show different totals with no per-widget
  indication of their own refresh time.
EXPECTED_SURFACE: S5,S8
PRECONDITIONS: >
  Place two overlapping-data widgets on refresh schedules that will drift apart and compare their
  values and any per-widget timestamps.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q015

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q015
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A conversation still open, not yet closed, is either excluded from a "resolved" aggregate or
  clearly marked in-progress, not blended indistinguishably into a completed-conversations figure.
WHY_IT_MATTERS: >
  Counting an open conversation as resolved overstates how much work has actually been completed.
DISCONFIRMING_OBSERVATION: >
  A "resolved" total includes a conversation that is still open and ongoing.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Leave a conversation open and check whether a "resolved" aggregate counts it.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q016

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q016
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard grouped by operator does not expose an operator's individual identity to a viewer
  whose permission is limited to aggregate, non-attributed performance figures.
WHY_IT_MATTERS: >
  An operator-grouped view is individual-level by construction; giving it to a viewer without
  individual-level rights defeats the point of scoping them to aggregates.
DISCONFIRMING_OBSERVATION: >
  A viewer restricted to aggregate-only visibility can see a named operator attached to a performance
  figure.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As an aggregate-only-scoped viewer, inspect an operator-grouped performance widget for named
  attribution.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q017

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q017
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Access to the livechat performance dashboard does not itself grant the ability to join, read, or
  respond to a live conversation from within the dashboard.
WHY_IT_MATTERS: >
  A reporting surface that also exposes a live conversation control bypasses the separation between
  viewing performance and actually engaging with customers that the source module's permission
  model is built on.
DISCONFIRMING_OBSERVATION: >
  A viewer with dashboard access but no conversation-handling authority can join or respond to a live
  conversation from within the dashboard interface.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a viewer with dashboard access but no conversation-handling authority, attempt to join or
  respond to a live conversation from within the dashboard.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q018

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q018
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A drill-down link on an aggregate figure that no longer resolves to any conversation record,
  because it was deleted or purged, fails visibly rather than silently substituting a default value
  or a zero.
WHY_IT_MATTERS: >
  A silent substitution disguises a broken reference as legitimate data, hiding a data-integrity
  problem from anyone relying on the drill-down.
DISCONFIRMING_OBSERVATION: >
  Following a drill-down link to a deleted or purged conversation produces a blank or zeroed page
  instead of a visible error or not-found state.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Delete or purge a conversation already referenced by a dashboard drill-down link and follow that
  link.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q019

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q019
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A dashboard reporting average handling time does not misrepresent a distribution skewed by one
  unusually long conversation as if it were typical, and the underlying detail remains reachable to
  a viewer entitled to see it.
WHY_IT_MATTERS: >
  A single outlier can move an average enough to mislead about "typical" handling time unless the
  dashboard surfaces the skew or lets an entitled viewer inspect it.
DISCONFIRMING_OBSERVATION: >
  An average-handling-time figure moves sharply due to one outlier conversation with no way for an
  entitled viewer to discover or drill into that outlier from the average widget.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Introduce one unusually long conversation into a group shown as an average and check whether the
  outlier is discoverable from the average widget.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q020

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q020
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A conversation reassigned from one operator's queue to another after it was already reflected in
  the first operator's aggregate is removed from that operator's figure, not left counted for both.
WHY_IT_MATTERS: >
  Leaving a reassigned conversation counted for the original operator overstates their workload after
  they no longer own it.
DISCONFIRMING_OBSERVATION: >
  After a reassignment, both the original and the new operator show the same conversation in their
  respective aggregates.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Reassign a conversation between operators and compare their respective aggregates before and after.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q021

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q021
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Exporting the dashboard's underlying conversation-level data to a shareable file does not bypass
  the same visibility restriction that applies when viewing the same conversations within the
  dashboard interface.
WHY_IT_MATTERS: >
  An export path that ignores the on-screen restriction turns a properly scoped view into an
  unrestricted file the moment it is downloaded.
DISCONFIRMING_OBSERVATION: >
  A viewer exports conversation-level data and the exported file contains conversations the same
  viewer could not see on screen.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a scoped viewer, export the underlying conversation-level data and compare its contents to what
  is visible on screen.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q022

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q022
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A dashboard combining current-period and prior-period conversation totals for comparison correctly
  isolates each period even where a single conversation spans the boundary between the two.
WHY_IT_MATTERS: >
  A comparison that double counts or drops a boundary-spanning conversation misstates the
  period-over-period trend it exists to show.
DISCONFIRMING_OBSERVATION: >
  A conversation spanning a period boundary is counted in both periods' totals, or in neither.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Have a conversation span a period boundary and inspect a period-comparison widget for double
  counting or omission.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q023

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q023
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard auto-refreshing at a fixed interval marks itself visibly stale rather than silently
  continuing to display data past a failed refresh attempt.
WHY_IT_MATTERS: >
  Silent staleness after a failed refresh is indistinguishable from a genuinely current figure,
  removing the viewer's ability to know they should not trust it.
DISCONFIRMING_OBSERVATION: >
  A dashboard whose scheduled refresh fails continues to present its last-good figures with no
  visible staleness indicator.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Cause or simulate a refresh failure on an auto-refreshing widget and inspect the presentation
  afterward.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q024

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q024
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rollup exposed at an organization-wide level does not carry channel-level detail fine enough to
  reconstruct near-individual conversation content when a channel's volume is very small.
WHY_IT_MATTERS: >
  Fine-grained detail at the organization level defeats the purpose of aggregating if it still lets a
  viewer reconstruct one conversation's content.
DISCONFIRMING_OBSERVATION: >
  An organization-wide rollup's channel-level breakdown, combined with known small channel volume,
  allows recovery of an individual conversation's detail.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Inspect an organization-wide rollup's channel-level granularity where at least one channel has
  very low volume.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q025

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q025
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A viewer's ability to filter a livechat dashboard by visitor does not become a way to enumerate
  identifiable visitor information beyond what that viewer would otherwise be authorized to browse.
WHY_IT_MATTERS: >
  A filter control with an unrestricted autocomplete or picklist can leak customer identity data to a
  viewer with no browsing right to that directory.
DISCONFIRMING_OBSERVATION: >
  A viewer with no visitor-directory browsing right can enumerate identifiable visitor information
  through the dashboard's visitor filter control.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a viewer without directory-browsing rights, use the dashboard's visitor filter and check what it
  allows them to enumerate.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q026

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q026
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A cached dashboard aggregate is invalidated and recomputed when a viewer's channel access is
  reduced, rather than continuing to serve a total computed under their former, broader scope.
WHY_IT_MATTERS: >
  A cache that outlives a permission reduction hands a now-restricted viewer data their narrower
  scope should no longer include.
DISCONFIRMING_OBSERVATION: >
  A viewer whose channel access has just been reduced still receives a cached aggregate reflecting
  their former, broader scope.
EXPECTED_SURFACE: S4,S8
PRECONDITIONS: >
  Reduce a viewer's channel access after a cached aggregate has been computed for them, then reload
  the dashboard before any unrelated cache expiry.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q027

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q027
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A concurrent update by two operators on the same conversation (such as a transfer occurring at the
  same moment as a closure) does not produce an aggregate reflecting neither operator's final state.
WHY_IT_MATTERS: >
  A lost-update outcome under concurrency can leave a conversation's status inconsistent with what
  either operator actually did.
DISCONFIRMING_OBSERVATION: >
  After a near-simultaneous transfer and closure on the same conversation, the resulting aggregate
  state matches neither operator's individually intended outcome.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a transfer and a closure on the same conversation at nearly the same time and inspect the
  resulting aggregate state.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q028

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q028
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A sentiment or rating aggregate spanning multiple languages does not silently treat untranslated or
  unrecognized text as a neutral score without flagging it as unclassified.
WHY_IT_MATTERS: >
  Silently scoring unclassifiable text as neutral distorts the aggregate by data that was never
  actually assessed.
DISCONFIRMING_OBSERVATION: >
  A sentiment aggregate includes a value for a conversation whose text was never actually classified,
  with no unclassified flag anywhere.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Introduce a conversation in an unsupported or unrecognized language and check whether it is scored
  neutrally or flagged unclassified in a sentiment aggregate.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q029

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q029
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A dashboard combining conversation volume across multiple companies or tenants does not silently
  sum figures that should remain tenant-scoped unless the viewer holds explicit cross-tenant
  visibility.
WHY_IT_MATTERS: >
  Summing across tenant boundaries without authorization exposes one tenant's conversation pattern to
  users of another, which in a multi-tenant SaaS platform is a severe isolation failure.
DISCONFIRMING_OBSERVATION: >
  A viewer scoped to a single tenant is shown, or a total silently includes, conversation data
  belonging to a different tenant they hold no cross-tenant right to see.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  In a multi-tenant configuration, view a livechat dashboard as a single-tenant-scoped user and check
  whether any total includes another tenant's figures.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q030

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q030
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A conversation started outside configured business hours is attributed to the correct reporting
  period or day consistently between the source record and the aggregate, not shifted by a differing
  period definition introduced by the reporting layer.
WHY_IT_MATTERS: >
  A period mismatch silently shifts conversations between periods that never actually moved in the
  underlying records, breaking reconciliation.
DISCONFIRMING_OBSERVATION: >
  A conversation started just outside business hours is attributed to a different reporting day or
  period in the dashboard than in the source record.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Start a conversation just outside configured business hours and compare its period attribution
  between the source record and the dashboard.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q031

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q031
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A "first response time" metric only measures time to a genuine operator reply, not time to an
  automated or canned acknowledgment that a viewer might mistake for a human response.
WHY_IT_MATTERS: >
  Counting an automated acknowledgment as the first response overstates actual operator
  responsiveness.
DISCONFIRMING_OBSERVATION: >
  A first-response-time figure is driven down by an automated acknowledgment sent before any genuine
  operator reply.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Trigger an automated acknowledgment ahead of any human reply and inspect the resulting
  first-response-time figure.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q032

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q032
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard's operator-performance ranking does not surface an operator's identity to a viewer
  whose role is limited to team-level, non-attributed reporting.
WHY_IT_MATTERS: >
  A ranking is individual-level disclosure by definition; presenting it to a viewer who should only
  see team-level aggregates defeats the access model at the reporting layer.
DISCONFIRMING_OBSERVATION: >
  A viewer restricted to team-level visibility can see a named operator attached to a ranked
  performance figure.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a team-level-scoped viewer, open any operator-ranking widget and check for named attribution.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q033

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q033
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Deleting or archiving a channel after conversations occurred on it does not remove those
  conversations from historical aggregates that already included them, though it may affect where a
  new drill-down points.
WHY_IT_MATTERS: >
  A historical total should not shrink just because its referenced channel was later removed.
DISCONFIRMING_OBSERVATION: >
  A historical aggregate's total drops after the channel it was logged against is deleted or
  archived.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Delete or archive a channel already reflected in a historical conversation aggregate and re-render
  that aggregate.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q034

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q034
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A real-time "operators currently online" indicator only reflects sessions still genuinely active,
  not sessions that ended abnormally without a proper sign-off event.
WHY_IT_MATTERS: >
  A stuck "online" status for a session that actually ended misrepresents current staffing available
  to handle incoming conversations.
DISCONFIRMING_OBSERVATION: >
  An operator whose session ended abnormally continues to be shown as online indefinitely.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  End an operator's session abnormally (without a proper sign-off) and observe how long the online
  indicator persists.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q035

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q035
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard widget configured against a filter referencing a specific operator or channel does not
  continue silently returning stale results after that operator or channel is deactivated.
WHY_IT_MATTERS: >
  A filter silently keeping stale references produces results the configuration owner no longer
  intends and cannot explain by inspecting the current, active configuration.
DISCONFIRMING_OBSERVATION: >
  A widget filtered to a since-deactivated operator or channel still returns data as though the
  reference were active, with no warning that it is stale.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Build a widget filtered to a specific operator or channel, deactivate that reference, and re-render
  the widget.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q036

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q036
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An aggregate figure computed before a bulk correction (such as a batch reclassification of
  conversation category) is reconciled to reflect the correction, with the fact that a correction
  occurred left visible rather than the number simply drifting with no explanation.
WHY_IT_MATTERS: >
  An unexplained change to a previously reported figure undermines trust in every other number the
  dashboard has ever shown.
DISCONFIRMING_OBSERVATION: >
  A previously reported aggregate changes value after a bulk correction with no visible indication
  that a correction occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger or identify a bulk correction to previously aggregated conversation data and check for a
  visible change-disclosure alongside the updated figure.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q037

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q037
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A dashboard grouped by conversation topic or category reflects a category correction made after
  the fact, rather than continuing to use the category assigned at conversation start indefinitely.
WHY_IT_MATTERS: >
  A category rollup that never absorbs a correction silently misattributes volume to the wrong topic
  indefinitely.
DISCONFIRMING_OBSERVATION: >
  A conversation recategorized after the fact continues to appear under its old category in a
  category rollup rendered after the correction.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Recategorize an already-counted conversation and re-render the category rollup.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q038

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q038
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A merged pair of duplicate conversation records is represented once, not twice, in any aggregate
  that would otherwise double count them.
WHY_IT_MATTERS: >
  A duplicate left counted twice after resolution silently overstates volume by exactly the
  duplicated conversation.
DISCONFIRMING_OBSERVATION: >
  An aggregate still reflects both records of a duplicate pair after they have been merged.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a duplicate pair already reflected separately in an aggregate, merge them, and re-render the
  aggregate.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q039

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q039
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A manager who loses oversight of a team of operators mid-period sees that team's conversations drop
  out of "my team" aggregates for the appropriate portion of the period, not remain permanently
  attributed to them.
WHY_IT_MATTERS: >
  Permanently attributing a former team's conversations to a manager who no longer oversees them
  misrepresents both the manager's actual scope and the team's actual reporting line during the
  period.
DISCONFIRMING_OBSERVATION: >
  A "my team" aggregate for a manager continues to include a former team's conversations for periods
  after the oversight change, with no split at the change point.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Change a team's reporting manager mid-period and inspect both managers' "my team" aggregates
  spanning the change.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q040

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q040
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A dashboard widget cached from before a bulk import of historical conversation data does not
  silently omit the imported records from subsequent totals indefinitely.
WHY_IT_MATTERS: >
  A cache that never absorbs a bulk import produces totals that permanently understate history by
  exactly the imported amount.
DISCONFIRMING_OBSERVATION: >
  A widget's historical total remains unchanged after a bulk import of historical conversations that
  should have altered it, even well after any stated refresh window.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Perform a bulk import of historical conversation data and check a previously cached historical
  aggregate after the stated refresh window.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q041

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q041
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A viewer granted only a read-only, aggregate-level role cannot use dashboard interactions, such as
  a group-by or filter control, to reconstruct individual conversation content the direct
  conversation list would otherwise hide from them.
WHY_IT_MATTERS: >
  An interactive reporting control that can be narrowed down to a single row is functionally
  equivalent to direct record access, defeating the aggregate-only restriction.
DISCONFIRMING_OBSERVATION: >
  A read-only, aggregate-scoped viewer can narrow a group-by or filter control until it isolates a
  single conversation's content.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As an aggregate-only-scoped viewer, attempt to use group-by or filter controls to isolate a single
  conversation.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q042

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q042
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An abandonment-rate metric only counts conversations that a visitor genuinely left without
  resolution, not conversations that were properly closed after resolution.
WHY_IT_MATTERS: >
  Miscounting a properly closed conversation as abandoned overstates a negative customer-experience
  metric that did not actually occur.
DISCONFIRMING_OBSERVATION: >
  An abandonment-rate figure includes a conversation that was properly closed after being resolved.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Properly close a resolved conversation and check whether it is counted in an abandonment-rate
  aggregate.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q043

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q043
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Sharing a dashboard snapshot outside the organization does not carry forward drill-down access to
  the underlying, access-restricted conversation transcripts even though the aggregate figures are
  shared.
WHY_IT_MATTERS: >
  External sharing is the highest-consequence disclosure boundary; a snapshot meant to share summary
  figures should not also hand out transcript access to parties with no organizational relationship.
DISCONFIRMING_OBSERVATION: >
  A recipient of an externally shared dashboard snapshot can drill down into individual conversation
  transcripts not covered by the sharing configuration.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Share a dashboard snapshot externally at aggregate granularity and attempt to drill down into
  transcript-level data from the shared view.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q044

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q044
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard combining conversation counts with a customer's identity across multiple channels does
  not silently merge that customer's activity from a channel the viewer is not authorized to see
  into the detail behind a visible total.
WHY_IT_MATTERS: >
  Merging cross-channel customer activity behind a single visible figure defeats channel-level
  authorization even when the top-line number looks properly scoped.
DISCONFIRMING_OBSERVATION: >
  A viewer authorized for only one channel can, through a customer-level total or drill-down, see
  evidence of that same customer's activity on a channel they are not authorized to see.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Have the same identified customer interact across two channels with different viewer
  authorizations and inspect a customer-level aggregate for cross-channel leakage.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q045

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q045
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A conversation still queued and never picked up by any operator is represented in an "unresolved"
  bucket distinct from one that was picked up and later abandoned.
WHY_IT_MATTERS: >
  Blending "never picked up" with "picked up then abandoned" hides which of two very different
  service failures actually occurred.
DISCONFIRMING_OBSERVATION: >
  A never-picked-up conversation and a picked-up-then-abandoned conversation land in the same
  unresolved bucket with no distinction between them.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Produce one conversation that is never picked up and one that is picked up then abandoned, and
  compare their representation in an unresolved-conversations aggregate.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q046

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q046
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard reporting response-time targets against actual performance reflects a change to the
  target configuration made after some conversations were already measured, without silently
  re-baselining already-elapsed periods.
WHY_IT_MATTERS: >
  Re-baselining an already-elapsed period against a target that did not exist at the time
  misrepresents how performance actually tracked against the target during that period.
DISCONFIRMING_OBSERVATION: >
  A historical period's target-versus-actual comparison changes after the target configuration is
  updated, for a period that had already elapsed under the old target.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change a response-time target configuration after a period has elapsed and re-render that period's
  target-versus-actual comparison.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q047

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q047
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A canned or templated response used in a conversation is not counted as a distinct "resolution" in
  an aggregate unless the conversation was actually closed as resolved.
WHY_IT_MATTERS: >
  Counting the use of a template as if it were a resolution overstates how many issues were actually
  closed out.
DISCONFIRMING_OBSERVATION: >
  A "resolutions" aggregate increases when a canned response is sent, even though the conversation
  remains open and unresolved.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Send a canned response in an otherwise still-open conversation and check whether a resolutions
  aggregate reflects it.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q048

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q048
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A channel-comparison view attributes a conversation to the channel the visitor actually initiated
  contact through, not the channel an operator later moved the conversation into for internal
  routing purposes.
WHY_IT_MATTERS: >
  Attributing volume to an internal routing destination rather than the visitor's actual entry point
  misrepresents which channel customers are genuinely using to reach the business.
DISCONFIRMING_OBSERVATION: >
  A conversation moved internally to a different channel for routing is attributed to the new channel
  rather than the visitor's originating channel in a channel-comparison widget.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Move a conversation to a different channel for internal routing after it started and check its
  channel attribution in a channel-comparison widget.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q049

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q049
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An operator working across more than one channel at once has their contribution reflected in each
  channel's own aggregate proportionally to the conversations actually handled there, not duplicated
  in full in both.
WHY_IT_MATTERS: >
  Duplicating an operator's full contribution into every channel they touch overstates staffing
  capacity attributed to each individual channel.
DISCONFIRMING_OBSERVATION: >
  An operator's full conversation count is duplicated identically into two different channels' own
  aggregates rather than being split between them.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have one operator handle conversations across two channels and inspect each channel's own
  aggregate for that operator's contribution.
```

## G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q050

```yaml
QID: G15-SPREADSHEET_DASHBOARD_IM_LIVECHAT-Q050
MODULE: spreadsheet_dashboard_im_livechat
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A unique-visitor count over a period does not inflate when the same visitor returns for a
  follow-up conversation, unless the dashboard is explicitly measuring conversation count rather
  than visitor count.
WHY_IT_MATTERS: >
  Conflating repeat-visitor conversations with new unique visitors overstates actual reach and
  misrepresents how much of the volume is repeat contact.
DISCONFIRMING_OBSERVATION: >
  A unique-visitor count increases when a previously counted visitor starts a follow-up conversation
  in the same period, on a widget explicitly labeled as counting unique visitors.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have the same visitor start two separate conversations within the same period and inspect a
  unique-visitor aggregate for that period.
```
