# SMEsPlus ENTERPRISE SUITE
## GMVQ — G15 PRODUCTIVITY / spreadsheet_dashboard_event_sale Module Bridge MVQ Bank

**Document ID:** GMVQ-G15-SPREADSHEET_DASHBOARD_EVENT_SALE-MVQ40-V1.00
**Group:** G15 PRODUCTIVITY
**Module Metadata:** `spreadsheet_dashboard_event_sale`
**Wave:** W4 (GMVQ 25-Team Acceleration, 2026-09-27)
**Author Cell:** P15-3 (GMVQ Question Factory — Production Cell P15-3)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 40
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 40 = 95
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `spreadsheet_dashboard_event_sale`, a three-participant seam (live dashboard reporting layer + event attendance/capacity data + sale revenue data). Per GROUP_BRIEF_G15_PRODUCTIVITY.md this module carries HIGH ARITY-EXHAUSTION RISK: every question below was authored and re-audited against the strict removal test — if the question would still make sense with the dashboard layer removed (a pure event+sale operational question), or with either the event or the sale side removed (a pure single-domain dashboard question already owned by a narrower sibling bank), it does not belong here and was cut. Every surviving question requires all three participants: a live or scheduled reporting rollup, event-side state (attendance, capacity, registration, session), and sale-side state (payment, refund, currency, pricing) interacting at the point where reporting is layered on top of the combined data. The material ground worked is staleness between the two source domains' refresh cycles, permission leakage through aggregation and drill-through, real-time-versus-batch mismatch, and cross-record rollup exposure — the four failure classes named in the Group Brief — plus reversal, cancellation, multi-currency, multi-company and cross-tenant handling of the combined reporting layer specifically.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure state, never a restatement of its own hypothesis.
- Arity control: every question requires the dashboard/reporting layer AND event-side state AND sale-side state simultaneously; a question answerable by any two of the three alone was rewritten to add the missing dependency or cut.
- No padding: authoring was stopped at 40 distinct material seam hypotheses rather than stretched to reach 48; see the Arity Exhaustion Statement below.
- Question text is source-neutral: no vendor or product name, no technical identifier, and the module's own metadata name never appears outside the `MODULE:` field.
- Checked against the Bridge Module Rule's seam dimensions (ordering, partiality, ownership, timing, reversal, quantity and money, lifecycle mismatch, error asymmetry, authority) before being kept.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## ARITY EXHAUSTION STATEMENT

This bank reaches 40 material questions, short of the 48-question floor set by GMVQ_AUTHORING_STANDARD_V1.00 §2. This shortfall is reported honestly rather than closed with manufactured questions, consistent with the module's flagged HIGH ARITY-EXHAUSTION RISK status and GMVQ_BRIDGE_MODULE_RULE_V1.00 §7 ("a short honest bank is worth more than a padded one").

Reasoning: the 40 questions above already work every seam dimension in GMVQ_BRIDGE_MODULE_RULE_V1.00 §3 for this specific three-way combination — ORDERING and TIMING (registration transfer, ticket-type upgrade, backdated correction attribution, refresh-cycle age mismatch), PARTIALITY (split payments, concurrent walk-in processing, waitlist conversion after sold-out), OWNERSHIP (which figure is authoritative when event and sale disagree on headcount versus payment), REVERSAL (cancellation, refund, void, full-event cancellation with all sales refunded), QUANTITY AND MONEY (multi-currency conversion consistency, multi-attendee sale splitting, tier misattribution), LIFECYCLE MISMATCH (cached rollup after event cancellation, deleted event history, archived event post-refund), and — specific to a reporting bridge rather than a ledger bridge — a dense cluster of AGGREGATION/PERMISSION-LEAKAGE questions (narrow-segment inference, small-N average disclosure, drill-through bypass, cross-event and cross-branch summary bleed, external share scope, ranking-based inference) that the Group Brief identifies as this group's own distinguishing failure class.

Candidate ground considered and REJECTED as belonging to a narrower sibling bank, not this three-way bridge (fails the removal test — would still make sense with one of the three participants removed):
- "Does the combined widget correctly total sale revenue for an event" with no reporting-layer failure mode attached — this is a `spreadsheet_dashboard_sale` or a pure `event_sale` question, not a seam question about what breaks specifically when reporting is layered on the combination.
- "Does event capacity update correctly when a registration is cancelled" with no sale or revenue dimension at all — this is an event-module question with no funding sale in the picture.
- "Does a sales dashboard correctly filter by date range" — a dashboard-only configuration question with no event participant, already the domain of the base `spreadsheet_dashboard` bank.

Candidate ground considered and REJECTED as duplicating the sibling `spreadsheet_dashboard_sale_timesheet` bank's material (per the Group Brief's duplicate-risk note, both are dashboard+sale 3-way bridges and share a sale-side vocabulary):
- Generic "aggregate rollup with too few underlying rows discloses an individual figure" was kept in both banks only because it recurs against a genuinely different second domain (event attendee count vs. employee headcount) each time, not as a restated pair — each instance names the domain-specific consequence (an attendee's payment vs. an employee's hourly cost) rather than a generic restatement.

## Questions

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q001

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q001
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combined revenue-per-attendee widget recomputes correctly when a registration is cancelled and its linked sale is refunded, rather than continuing to count the cancelled attendee in the headcount or the refunded amount in the revenue figure.
WHY_IT_MATTERS: >
  Continuing to count a reversed registration and its refunded payment would present attendance and revenue as though a cancelled transaction had never been reversed.
DISCONFIRMING_OBSERVATION: >
  After a registration is cancelled and its sale fully refunded, the combined widget still counts the attendee in headcount or still counts the refunded amount in revenue.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Register and pay for an event, cancel the registration and refund the sale, then check whether the combined widget's headcount and revenue figures still reflect the reversed transaction.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q002

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q002
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A viewer permitted to see an event's attendance figures but not a customer's payment amounts cannot use a narrow segment filter on the combined widget (down to a single attendee) to infer that attendee's individual payment.
WHY_IT_MATTERS: >
  A rollup that can be narrowed to one row defeats the purpose of aggregate-only permission and exposes an individual's payment to someone never granted that access.
DISCONFIRMING_OBSERVATION: >
  Filtering the combined widget down to a single attendee reveals that attendee's individual payment amount to a viewer who lacks permission to see payment detail.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Grant a user permission to view event attendance but not sale amounts, narrow the combined widget's filter to a single attendee, and check whether a payment figure becomes visible.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q003

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q003
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A combined widget's attendee headcount and its sale-derived revenue figure, when drawn from refresh cycles of different ages, are not presented to the viewer as though both were captured at the same moment.
WHY_IT_MATTERS: >
  Presenting two figures of different ages as a single coherent snapshot would mislead a viewer about how current the combined picture actually is.
DISCONFIRMING_OBSERVATION: >
  The widget shows a headcount and a revenue figure of visibly different refresh ages with no indication that the two halves are not contemporaneous.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a refresh of only the event-side or only the sale-side data feeding a combined widget, then check whether the displayed figure indicates the resulting age mismatch.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q004

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q004
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an event registration is transferred from one attendee to another after its sale has already occurred, the combined widget's per-attendee revenue attribution reflects the current occupant of the seat, not the original registrant, unless a documented rule states otherwise.
WHY_IT_MATTERS: >
  Attributing revenue to whoever originally purchased a now-transferred seat would misstate which attendee the combined figure actually describes.
DISCONFIRMING_OBSERVATION: >
  After a registration transfer, the combined widget's per-attendee revenue figure still names the original registrant rather than the current attendee.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Transfer a paid registration from one attendee to another, then check which attendee the combined widget's revenue figure is attributed to.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q005

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q005
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A widget grouping revenue by event session does not count a single sale that funds attendance at two sessions of the same event twice, once under each session's total.
WHY_IT_MATTERS: >
  Double counting one payment across two session totals would overstate the event's true combined revenue.
DISCONFIRMING_OBSERVATION: >
  A sale funding attendance at two sessions appears in full under both sessions' revenue totals in the combined widget.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Purchase one sale that grants attendance at two sessions of one event, and check whether the combined per-session revenue widget counts that sale once or twice.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q006

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q006
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an event offers multiple pricing tiers, a combined widget blending session attendance counts with total sale revenue does not attribute a higher-tier attendee's payment to a lower-tier bucket.
WHY_IT_MATTERS: >
  Misattributing a payment to the wrong tier bucket would misstate each tier's actual revenue performance.
DISCONFIRMING_OBSERVATION: >
  A higher-tier attendee's payment appears under a lower pricing tier's revenue bucket in the combined widget.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Register attendees under two different pricing tiers for one event, and check whether the combined widget attributes each payment to the correct tier.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q007

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q007
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A viewer who can see an aggregate revenue-per-event widget but has no permission to view individual customer records cannot use a drill-through or click-through on a rollup cell to reach the underlying sale record.
WHY_IT_MATTERS: >
  A drill-through that bypasses the aggregate-only permission would let an unauthorized viewer reach individual sale detail through the back door of the dashboard.
DISCONFIRMING_OBSERVATION: >
  Clicking through an aggregate rollup cell exposes an underlying individual sale record to a viewer who is not permitted to view customer sale records.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Grant a user permission to view only the aggregate combined widget, attempt to drill through a rollup cell, and check whether the underlying sale record becomes visible.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q008

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q008
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling an event after its combined revenue/attendance widget has already been rendered and cached does not leave that cached rollup permanently presented as current with no indication that the underlying event no longer exists.
WHY_IT_MATTERS: >
  A stale cached figure presented as current for a cancelled event would mislead anyone relying on the dashboard about the event's actual status.
DISCONFIRMING_OBSERVATION: >
  After the event is cancelled, the previously cached combined widget continues to display as though the event were still live, with no indication of its cancelled status.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Cache a combined widget for a live event, cancel the event, and check whether the cached widget indicates that the underlying event is no longer active.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q009

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q009
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A sale linked to an event registration that is later voided for a payment failure is removed from the combined dashboard's revenue figure within the same refresh cycle in which the sale is voided, not carried forward as still-valid revenue.
WHY_IT_MATTERS: >
  Carrying a voided payment forward as valid revenue would overstate the event's actual collected income.
DISCONFIRMING_OBSERVATION: >
  After a linked sale is voided for payment failure, the combined widget's revenue figure still includes that sale's amount past the refresh cycle in which it was voided.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Void a sale linked to an event registration due to a payment failure, then check whether the next combined widget refresh removes that sale's amount from revenue.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q010

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q010
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a linked sale's currency differs from the event's default reporting currency, the combined revenue-per-attendee figure uses one documented, consistently applied conversion moment across every attendee shown in the same widget.
WHY_IT_MATTERS: >
  Mixing conversion moments within one rollup would make the combined revenue-per-attendee figure numerically incoherent even though every individual amount is correct.
DISCONFIRMING_OBSERVATION: >
  Two attendees shown in the same combined widget have their foreign-currency payments converted using different exchange-rate moments.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Register attendees whose sales are recorded in a currency different from the event's reporting currency, and compare the conversion basis used across attendees in the same widget.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q011

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q011
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined dashboard split by company or branch for a multi-branch event does not blend attendees registered under one branch with sale revenue actually recognized under a different branch.
WHY_IT_MATTERS: >
  Blending figures across branches would misstate each branch's true attendance-to-revenue relationship and could leak one branch's data into another's view.
DISCONFIRMING_OBSERVATION: >
  The combined widget for one branch shows revenue that was actually recognized under a different branch's books mixed into its own total.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Set up a multi-branch event where attendees register under different branches, and check whether each branch's combined widget shows only its own branch's revenue.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q012

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q012
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Exporting a combined event-sale rollup to a shared file applies the same permission-based filtering that the live widget applies, rather than exposing full unfiltered underlying detail to whoever receives the file.
WHY_IT_MATTERS: >
  An export that bypasses live-view filtering would hand a recipient more detail than the dashboard itself ever showed them.
DISCONFIRMING_OBSERVATION: >
  An exported copy of the combined widget contains itemized attendee-to-sale detail that the same viewer's live widget never displayed.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Export a combined widget to a file as a user with aggregate-only permission, and compare the exported content against what the live widget shows that same user.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q013

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q013
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A widget showing average spend per attendee for an event with very few paying attendees does not, at that granularity, allow a viewer to infer a single attendee's individual payment amount.
WHY_IT_MATTERS: >
  An average computed over too small a group functions as an individual disclosure even though it is presented as an aggregate.
DISCONFIRMING_OBSERVATION: >
  An 'average spend per attendee' figure for an event with only one or two paying attendees reveals, in practice, an individual attendee's exact payment.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  View the combined average-spend widget for an event with only one or two paying attendees, and check whether the resulting figure discloses an individual payment amount.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q014

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q014
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an event's capacity is reduced after tickets are already sold and the sale side still shows those transactions as completed, the combined dashboard reconciles the two figures rather than silently displaying an attendee count exceeding the stated capacity with no flag.
WHY_IT_MATTERS: >
  An unflagged overcapacity figure would hide a real operational problem from whoever relies on the dashboard to manage the event.
DISCONFIRMING_OBSERVATION: >
  The combined widget shows an attendee count exceeding the event's stated capacity with no flag or note explaining the discrepancy.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Reduce an event's stated capacity after tickets were already sold beyond the new limit, and check whether the combined widget flags the resulting overcapacity.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q015

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q015
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A recurring background refresh of the combined widget picks up a correction to a sale's linked event reference made after an earlier refresh already ran, rather than perpetually attributing that sale to the originally recorded event.
WHY_IT_MATTERS: >
  A correction that never propagates would leave the dashboard permanently misattributing a sale to the wrong event.
DISCONFIRMING_OBSERVATION: >
  After a sale's linked event reference is corrected, a subsequent scheduled refresh of the combined widget still attributes that sale to the original, incorrect event.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Correct a sale's linked event reference after an earlier scheduled refresh has already run, wait for the next scheduled refresh, and check which event the sale is attributed to.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q016

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q016
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where one sale funds registrations for multiple attendees at the same event, the combined per-attendee revenue rollup splits that sale's amount across attendees using one documented rule rather than assigning the full sale amount to each attendee shown.
WHY_IT_MATTERS: >
  Assigning the full amount to every attendee funded by one shared sale would overstate the event's total revenue by a multiple of the actual payment.
DISCONFIRMING_OBSERVATION: >
  A single sale funding several attendees at one event shows its full amount repeated against each of those attendees in the combined per-attendee rollup.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Purchase one sale that registers multiple attendees for one event, and check how the combined widget splits that sale's amount across the attendees.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q017

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q017
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A viewer with permission scoped to one event cannot see another event's combined revenue or attendance figures bleed into a cross-event summary rollup that sums a wider grouping, without at least the same aggregate-only breakdown they are already authorized to see.
WHY_IT_MATTERS: >
  A wider summary that leaks a specific unauthorized event's figures would defeat the event-level permission scoping entirely.
DISCONFIRMING_OBSERVATION: >
  A cross-event summary rollup available to a viewer scoped to one event reveals another event's specific combined figures beyond what that viewer is authorized to see.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Grant a user permission scoped to one event only, view a cross-event summary rollup that includes other events, and check whether another event's specific figures are visible.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q018

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q018
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Refreshing the combined widget concurrently with a sale being processed for a walk-in attendee does not produce a rollup where the attendee is counted in headcount but the paid amount is not yet reflected, or the reverse, without the widget indicating that reconciliation is pending.
WHY_IT_MATTERS: >
  An unlabeled partial state during concurrent processing would present an inconsistent, momentarily wrong figure as though it were settled.
DISCONFIRMING_OBSERVATION: >
  During concurrent processing of a walk-in sale, the combined widget shows the attendee counted in headcount without the corresponding payment reflected, or the payment reflected without the headcount, and gives no indication that reconciliation is pending.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Process a walk-in attendee's sale at the same moment the combined widget refreshes, and check whether the resulting figure shows a partial, unlabeled mismatch between headcount and revenue.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q019

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q019
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A combined widget built at event setup time is updated when the event's linked sale product or price changes, rather than continuing to compute revenue using the original linkage with no record of when the configuration changed.
WHY_IT_MATTERS: >
  A silently frozen configuration would let the dashboard drift away from the event's actual current pricing without anyone knowing when or why.
DISCONFIRMING_OBSERVATION: >
  After the event's linked sale product or price is changed, the combined widget's computed revenue still reflects the original configuration with no record that a change occurred.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change an event's linked sale product or price after the combined widget was first configured, and check whether the widget reflects the change and records when it took effect.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q020

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q020
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Deleting an event that already has combined dashboard history referencing it leaves that historical rollup intact and clearly marked as referring to a removed event, rather than the widget erroring or silently reporting zero.
WHY_IT_MATTERS: >
  Losing historical figures on deletion would destroy a legitimate record of past performance for no operational reason.
DISCONFIRMING_OBSERVATION: >
  After the event is deleted, the combined widget's historical rollup for that event either errors or reports zero instead of preserving the original figures with a removed-event notation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Delete an event that has existing combined dashboard history, and check whether that history remains visible and correctly labeled.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q021

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q021
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combined dashboard's no-show metric, derived by comparing sale-confirmed registrations against event check-in records, does not misclassify a valid late check-in as a no-show due to a refresh timing gap between the two source records.
WHY_IT_MATTERS: >
  A false no-show classification caused only by refresh timing would misrepresent actual attendance for reporting or follow-up purposes.
DISCONFIRMING_OBSERVATION: >
  A late but valid check-in is shown as a no-show in the combined widget solely because the check-in record refreshed after the no-show calculation already ran.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Have an attendee check in late relative to the combined widget's refresh cycle, and check whether the no-show metric misclassifies them before the next refresh.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q022

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q022
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a sale for an event registration is split across two partial payments, the combined revenue rollup does not count the attendee as fully paid before the second installment has actually been recorded on the sale side.
WHY_IT_MATTERS: >
  Showing an attendee as fully paid ahead of the actual second payment would overstate collected revenue and could mask a payment default risk.
DISCONFIRMING_OBSERVATION: >
  The combined widget marks an attendee as fully paid while the second installment of their split payment has not yet been recorded on the sale.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Register an attendee under a two-installment payment plan, record only the first installment, and check whether the combined widget already shows the attendee as fully paid.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q023

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q023
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined widget shared externally via a public or semi-public link exposes only the same aggregate figures a permitted internal viewer would see, and not the underlying itemized attendee-to-sale mapping.
WHY_IT_MATTERS: >
  An external share that exposes more than an internal aggregate view would leak individual customer data beyond the organization's own access controls.
DISCONFIRMING_OBSERVATION: >
  A publicly or externally shared version of the combined widget reveals itemized attendee-to-sale detail that an equivalent internal aggregate-only viewer never sees.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Share a combined widget via an external link, and compare its content against the same widget as viewed internally by a user with aggregate-only permission.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q024

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q024
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an attendee cancels but the seat is not resold, the combined dashboard's revenue-per-seat figure reflects the reduced actual headcount rather than continuing to divide revenue by the original registered count.
WHY_IT_MATTERS: >
  Dividing by an outdated headcount would understate the true revenue-per-seat for the attendees who actually remain.
DISCONFIRMING_OBSERVATION: >
  After a cancellation with no resale, the combined widget's revenue-per-seat figure still divides by the original registered headcount rather than the reduced actual count.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Cancel an attendee's registration without reselling the seat, and check whether the combined widget's revenue-per-seat calculation updates its denominator.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q025

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q025
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rollup showing revenue trend over time for an event series attributes a late-arriving, backdated sale correction to the period in which the correction was actually applied, not to the originally intended transaction period.
WHY_IT_MATTERS: >
  Misattributing a backdated correction to the wrong period would distort the trend line for a period that never actually saw that change.
DISCONFIRMING_OBSERVATION: >
  A backdated correction to a sale appears in the combined trend widget under the period the sale originally occurred in, rather than the period the correction was actually applied.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a backdated correction to a sale within an event series' history, and check which period the combined trend widget attributes the correction to.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q026

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q026
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Combined widget row-level access for a co-organizer scoped to only their assigned sessions of a multi-session event does not surface revenue figures for sessions outside their scope through a shared summary total.
WHY_IT_MATTERS: >
  A shared summary that leaks out-of-scope session revenue would defeat the row-level scoping given to a co-organizer.
DISCONFIRMING_OBSERVATION: >
  A co-organizer scoped to specific sessions can see, through a shared summary total, revenue figures for sessions they were not assigned.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Scope a co-organizer's access to specific sessions of a multi-session event, and check whether a shared summary total exposes other sessions' revenue.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q027

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q027
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A combined dashboard's real-time indicator, where present, accurately reflects which half of the combined figure (event side or sale side) is actually live versus last-batch, rather than presenting a single unqualified live label when only one side refreshes in real time.
WHY_IT_MATTERS: >
  An unqualified live label covering a partially batched figure would overstate how current the displayed information actually is.
DISCONFIRMING_OBSERVATION: >
  The widget's live indicator applies to the whole combined figure even though only the event side or only the sale side actually refreshes in real time.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure one side of a combined widget's data source to refresh in real time and the other on a batch schedule, and check what the widget's live indicator actually communicates.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q028

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q028
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Refunding a sale for an attendee after the event has already concluded and been archived posts a correction that the combined historical dashboard for that concluded event reflects, rather than the archived rollup remaining fixed at its pre-refund figures with no update path.
WHY_IT_MATTERS: >
  An archived figure that can never be corrected would leave a known, real refund permanently unreflected in the historical record.
DISCONFIRMING_OBSERVATION: >
  After a post-event refund, the archived combined dashboard for that concluded event continues to show the pre-refund figures with no way for the correction to reach it.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Refund a sale for an attendee of an already-concluded, archived event, and check whether the archived combined widget's historical figures update to reflect the refund.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q029

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q029
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A combined widget grouping revenue by ticket type shows a mid-registration ticket-type upgrade as a documented transition rather than retroactively attributing the original tier's sale record to the new tier.
WHY_IT_MATTERS: >
  Silently reattributing the original-tier record would erase the actual transition history between the two tiers.
DISCONFIRMING_OBSERVATION: >
  After a ticket-type upgrade, the combined widget shows the attendee's original purchase as though it always belonged to the new tier, with no record of the transition.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Upgrade an attendee's ticket type mid-registration, and check whether the combined widget shows the transition or silently reattributes the original sale to the new tier.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q030

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q030
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where two attendees swap registrations peer-to-peer with no new sale created, the combined dashboard's per-attendee revenue attribution follows the attendee actually occupying the seat rather than the original purchaser, unless a documented rule states otherwise.
WHY_IT_MATTERS: >
  Attributing revenue to whoever no longer holds the seat would misstate which attendee the combined figure actually describes.
DISCONFIRMING_OBSERVATION: >
  After a peer-to-peer registration swap with no new sale, the combined widget still attributes the original purchaser's payment to that same original purchaser rather than the current occupant.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have two attendees swap registrations directly with no new sale recorded, and check which attendee the combined widget's revenue figure is attributed to afterward.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q031

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q031
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A combined widget's cache invalidation triggered by a sale-side change, such as a refund, also invalidates the event-side headcount portion of the same cached rollup, rather than updating only the revenue half.
WHY_IT_MATTERS: >
  Updating only one half of a cached combined figure would leave headcount and revenue permanently out of step after any sale-side change.
DISCONFIRMING_OBSERVATION: >
  After a refund triggers cache invalidation, the combined widget's revenue figure updates but its headcount figure continues to reflect the stale cached value.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a refund that invalidates a combined widget's cache, and check whether both the revenue and headcount portions of the rollup are refreshed.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q032

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q032
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where a corporate account purchases block registrations for an event on one consolidated sale, the combined per-attendee dashboard does not require exposing the corporate account's overall order value to someone permitted to see only individual attendee-level rollups.
WHY_IT_MATTERS: >
  Exposing the consolidated order value through an individual-level view would leak commercial information beyond what that viewer's permission was meant to allow.
DISCONFIRMING_OBSERVATION: >
  A viewer permitted to see only individual attendee-level figures can nonetheless see the corporate account's overall consolidated order value through the combined widget.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Have a corporate account purchase block registrations on one consolidated sale, and check whether a viewer scoped to individual attendee-level rollups can see the consolidated order value.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q033

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q033
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combined dashboard configured to auto-refresh on a schedule shorter than the underlying sale ledger's own posting cadence does not present a revenue figure as final when it has not actually cleared the posting process yet.
WHY_IT_MATTERS: >
  Presenting an unposted figure as final would mislead a viewer into treating provisional revenue as confirmed.
DISCONFIRMING_OBSERVATION: >
  The combined widget presents a revenue figure with no provisional label even though the underlying sale has not yet cleared the ledger's posting process.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure the combined widget's refresh interval shorter than the sale ledger's posting cadence, and check whether an unposted revenue figure is presented as final.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q034

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q034
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined widget definition cloned from one tenant's event-sale setup into another tenant does not retain any live reference back to the source tenant's actual event or sale records.
WHY_IT_MATTERS: >
  A live cross-tenant reference would leak one customer's actual data into a different customer's dashboard.
DISCONFIRMING_OBSERVATION: >
  A cloned combined widget in a new tenant displays live data originating from the source tenant's actual event or sale records.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Clone a combined event-sale widget definition from one tenant into another, and check whether the cloned widget resolves to the source tenant's live data.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q035

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q035
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where an event is cancelled entirely after ticket sales occurred and all sales are refunded, the combined dashboard for that event shows the fully reversed state consistently on both the attendance and revenue axes, not one axis reversed while the other still shows original figures.
WHY_IT_MATTERS: >
  A partially reversed dashboard would misrepresent a fully cancelled event as still having had real attendance or real revenue.
DISCONFIRMING_OBSERVATION: >
  After a full event cancellation with all sales refunded, the combined widget shows the revenue axis reversed to zero while the attendance axis still shows the original headcount, or the reverse.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Cancel an event entirely and refund all its sales, then check whether the combined widget's attendance and revenue figures both reflect the full reversal.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q036

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q036
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combined widget that lets a viewer filter attendees by paid versus pending sale status does not include an attendee whose sale is still pending in a confirmed-paid-attendance total shown elsewhere in the same dashboard.
WHY_IT_MATTERS: >
  Counting a pending sale as confirmed elsewhere in the same dashboard would present two inconsistent pictures of the same underlying fact.
DISCONFIRMING_OBSERVATION: >
  An attendee whose sale status is still pending appears in a confirmed-paid-attendance total shown elsewhere in the same combined dashboard.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Register an attendee whose sale remains in pending status, and check whether a confirmed-paid-attendance total elsewhere in the dashboard includes them.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q037

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q037
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an event's sale-linked waiting list converts a waitlisted person to a full sale after the event's capacity widget already showed the event as sold out, the combined dashboard reconciles the resulting capacity figure rather than displaying an attendee count above the previously shown sold-out capacity with no note.
WHY_IT_MATTERS: >
  An unreconciled overcapacity figure following a waitlist conversion would look like an unexplained data error rather than a real, tracked event.
DISCONFIRMING_OBSERVATION: >
  After a waitlist conversion following a sold-out state, the combined widget shows an attendee count above the event's stated capacity with no note explaining the conversion.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Convert a waitlisted person to a full paid registration after the combined widget already shows the event as sold out, and check whether the resulting capacity figure is reconciled or flagged.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q038

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q038
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined revenue-by-event ranking widget used to compare events does not let a viewer infer, from a visible rank change alone, the exact revenue figure of an event they are not permitted to view in detail.
WHY_IT_MATTERS: >
  A rank change alone can leak enough information to reconstruct a restricted figure, defeating the purpose of hiding that event's detail.
DISCONFIRMING_OBSERVATION: >
  A viewer without permission to see a specific event's revenue in detail can determine that event's exact figure from a visible change in its ranking position.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Restrict detailed revenue visibility for one event while it appears in a ranking widget, and check whether a rank change alone reveals its exact figure to an unauthorized viewer.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q039

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q039
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a sale for event attendance is later reclassified to a different, unrelated product category, the combined dashboard drops that reclassified sale from the event's revenue rollup within the same refresh in which it was reclassified.
WHY_IT_MATTERS: >
  Continuing to count a reclassified sale would attribute revenue to an event for a transaction that no longer represents that event's attendance.
DISCONFIRMING_OBSERVATION: >
  After a sale is reclassified away from an event's product category, the combined widget's revenue rollup for that event still includes the reclassified sale past the refresh in which it changed.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Reclassify a sale originally linked to event attendance into an unrelated product category, then check whether the next combined widget refresh removes it from the event's revenue.
```

## G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q040

```yaml
QID: G15-SPREADSHEET_DASHBOARD_EVENT_SALE-Q040
MODULE: spreadsheet_dashboard_event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined dashboard aggregating multiple events' attendee-revenue data into one company-wide summary does not let a viewer permitted to see only the summary total infer an individual event's exact figure when the summary happens to include just one event for a given period.
WHY_IT_MATTERS: >
  A summary that degenerates to a single event's figure in a sparse period functions as a direct disclosure despite being presented as an aggregate.
DISCONFIRMING_OBSERVATION: >
  A company-wide summary total, in a period containing only one event, reveals that event's exact figure to a viewer who is not permitted to see individual event detail.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  View the company-wide combined summary for a period containing only one active event, and check whether the summary total discloses that event's exact individual figure.
```
