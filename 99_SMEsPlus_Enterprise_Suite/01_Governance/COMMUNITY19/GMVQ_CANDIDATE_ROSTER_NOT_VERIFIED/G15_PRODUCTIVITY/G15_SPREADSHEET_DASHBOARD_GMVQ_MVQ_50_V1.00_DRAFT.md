# SMEsPlus ENTERPRISE SUITE
## GMVQ — G15 PRODUCTIVITY / spreadsheet_dashboard Module MVQ Bank

**Document ID:** GMVQ-G15-SPREADSHEET_DASHBOARD-MVQ50-V1.00
**Group:** G15 PRODUCTIVITY (Wave W4)
**Module Metadata:** `spreadsheet_dashboard`
**Wave:** W4
**Author Cell:** P15-1 (GMVQ Question Factory — Production Cell P15-1)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for the base dashboard-of-dashboards capability —
the foundation module that every domain-specific dashboard bridge in this group builds on. Per the
Group Brief, this bank carries the deepest treatment of dashboard-general behaviour: refresh
cadence and staleness disclosure, permission scope independent of underlying source data, drill-down
scoping, snapshot immutability, aggregation integrity under failure, sharing and distribution
boundaries, and the tenant/company boundary. Domain-specific seam questions (dashboard-plus-account,
dashboard-plus-sale, and so on) belong to their own bridge banks, not here.

Question text is source-neutral. It does not name the module, any vendor or product, or any
technical identifier. Generic terms such as "tile", "source range" and "aggregation" are used
throughout in place of implementation-specific naming.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 50 questions exist because each tests a distinct material hypothesis, spread across
  business capability, business rule, state transition, configuration dependency, role and
  permission, exception path, cancellation, reversal, negative case, cross-module dependency,
  optional behaviour, auditability, tenant/company boundary, concurrency and ordering, and runtime
  reachability.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G15-SPREADSHEET_DASHBOARD-Q001

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q001
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A tile's aggregation recalculates according to its own configured refresh mode, and does not
  silently continue showing a value from before a source change past its own disclosed refresh
  cadence.
WHY_IT_MATTERS: >
  A tile that quietly stops refreshing on schedule presents outdated figures as though they were
  current.
DISCONFIRMING_OBSERVATION: >
  A tile configured for real-time refresh does not update after its underlying source data changes,
  with no indication that the refresh failed.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure a real-time tile, change its underlying source data, and observe whether and when it
  updates.
```

## G15-SPREADSHEET_DASHBOARD-Q002

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q002
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A dashboard's own sharing scope is independent of its underlying source data's sharing scope, and
  cannot be used to grant a viewer visibility into source data broader than their own direct
  permission on that data.
WHY_IT_MATTERS: >
  A dashboard that bypasses source-level permission through its own separate sharing model is a
  general-purpose data leak across every domain it aggregates.
DISCONFIRMING_OBSERVATION: >
  Sharing a dashboard grants a recipient visibility into underlying source data they could not open
  directly.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Share a dashboard with a user who lacks direct access to its underlying source data, and check
  what that user can see.
```

## G15-SPREADSHEET_DASHBOARD-Q003

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q003
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Drilling down from an aggregated tile into its underlying rows applies the same row-level
  permission the viewer would face accessing that data directly, not a wider view exposed only
  through the dashboard path.
WHY_IT_MATTERS: >
  A drill-down that ignores row-level permission turns an aggregated summary into a full-detail leak
  for anyone who can drill in.
DISCONFIRMING_OBSERVATION: >
  Drill-down from a dashboard tile surfaces rows the viewer could not see through direct access to
  the source.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Restrict a viewer's row-level access on the source data, then have that viewer drill down from an
  aggregated tile.
```

## G15-SPREADSHEET_DASHBOARD-Q004

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q004
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Two viewers of the same shared dashboard, with no personal filter applied, see identical figures
  for the same tile at the same moment.
WHY_IT_MATTERS: >
  A shared dashboard that disagrees between equally-permissioned viewers cannot serve as a common
  reference point for decisions.
DISCONFIRMING_OBSERVATION: >
  Two viewers with the same access and no applied filters see different numbers on the same shared
  dashboard tile at the same time.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Open the same dashboard as two equally-permissioned users at the same time and compare a tile's
  figure.
```

## G15-SPREADSHEET_DASHBOARD-Q005

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q005
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A personal filter one viewer applies to a shared dashboard affects only that viewer's own view, not
  the state seen by other concurrent viewers of the same dashboard.
WHY_IT_MATTERS: >
  A personal filter that leaks into the shared state would make it unsafe for anyone to explore a
  shared dashboard without disrupting everyone else's view.
DISCONFIRMING_OBSERVATION: >
  One viewer's personal filter changes what another concurrent viewer sees on the same dashboard.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  Apply a personal filter as one viewer while a second viewer is concurrently viewing, and compare
  what each sees.
```

## G15-SPREADSHEET_DASHBOARD-Q006

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q006
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A tile that fails to compute, for example because its source is unreachable, displays an explicit
  error or unavailable state rather than a blank or zero value indistinguishable from a legitimate
  result.
WHY_IT_MATTERS: >
  A failed tile that looks like a genuine zero can be read as good news when it is actually a broken
  computation.
DISCONFIRMING_OBSERVATION: >
  A tile that failed to retrieve its source data displays a value indistinguishable from a genuine
  zero or empty result.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Make a tile's source temporarily unreachable and inspect what the tile displays.
```

## G15-SPREADSHEET_DASHBOARD-Q007

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q007
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Duplicating a dashboard copies its tile configuration, defining what and how to aggregate, but does
  not carry over the source dashboard's already-computed cached figures as though they were fresh
  results for the new copy.
WHY_IT_MATTERS: >
  A duplicate that inherits stale computed figures can be mistaken for a dashboard that has already
  run its own aggregation.
DISCONFIRMING_OBSERVATION: >
  A newly duplicated dashboard shows the original's previously computed values before it has run its
  own aggregation.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Duplicate a dashboard immediately and inspect what the copy shows before any refresh cycle
  completes.
```

## G15-SPREADSHEET_DASHBOARD-Q008

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q008
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A dashboard explicitly saved as a fixed point-in-time snapshot remains unchanged by later updates
  to its underlying source data, distinct from a live dashboard.
WHY_IT_MATTERS: >
  A snapshot that silently drifts defeats the entire purpose of freezing a dashboard for a formal
  reporting record.
DISCONFIRMING_OBSERVATION: >
  A dashboard explicitly marked as a frozen snapshot changes its displayed figures after the
  underlying source data is later updated.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Save a dashboard as a fixed snapshot, then change its underlying source data and re-open the
  snapshot.
```

## G15-SPREADSHEET_DASHBOARD-Q009

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q009
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A tile's last-refreshed indicator reflects the actual time its underlying data was last read, not
  the time the page happened to render.
WHY_IT_MATTERS: >
  An indicator that just reflects page-load time gives a false sense of freshness on every visit.
DISCONFIRMING_OBSERVATION: >
  The displayed refresh time changes on every page load regardless of whether the tile's data was
  actually re-read.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Load the same dashboard page twice in quick succession with no underlying data change, and compare
  the displayed refresh time.
```

## G15-SPREADSHEET_DASHBOARD-Q010

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q010
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Removing a viewer's access to a dashboard leaves no previously generated export, embed, or link for
  that dashboard still serving them live updating figures.
WHY_IT_MATTERS: >
  A live link that survives revocation is an invisible, unrevoked access path for someone whose
  access was supposed to be removed.
DISCONFIRMING_OBSERVATION: >
  A viewer whose dashboard access was revoked can still retrieve current figures through a previously
  obtained export or embed link.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Obtain an export or embed link as a viewer, revoke that viewer's dashboard access, and retest the
  link.
```

## G15-SPREADSHEET_DASHBOARD-Q011

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q011
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard combining tiles from more than one underlying source, presented as comparable, computes
  them on a common key or period rather than silently juxtaposing figures on inconsistent bases.
WHY_IT_MATTERS: >
  Two figures presented side by side as comparable but computed on different bases can lead to a
  materially wrong conclusion.
DISCONFIRMING_OBSERVATION: >
  Two tiles presented on the same dashboard as comparable turn out to be computed over different,
  undisclosed periods or scopes.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Place two tiles side by side intended as comparable and check whether their computation basis
  actually matches.
```

## G15-SPREADSHEET_DASHBOARD-Q012

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q012
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A scheduled dashboard refresh that fails is surfaced as a failure to the dashboard owner rather
  than silently leaving a stale figure displayed indistinguishably from a successfully refreshed
  one.
WHY_IT_MATTERS: >
  A silent refresh failure leaves the owner with no reason to suspect the figures being relied on are
  actually stale.
DISCONFIRMING_OBSERVATION: >
  A failed scheduled refresh produces no notice, and the stale figure is presented identically to a
  successfully refreshed one.
EXPECTED_SURFACE: S8,S7
PRECONDITIONS: >
  Force a scheduled refresh to fail and check for any notice to the dashboard owner.
```

## G15-SPREADSHEET_DASHBOARD-Q013

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q013
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A tile referencing a source range that has since been deleted is placed in an explicit broken or
  error state rather than being silently omitted or crashing the whole dashboard view.
WHY_IT_MATTERS: >
  An unhandled failure on one tile that takes down the entire dashboard denies access to every other
  tile that was otherwise fine.
DISCONFIRMING_OBSERVATION: >
  Opening a dashboard containing a tile whose source range was deleted produces an unhandled error,
  or silently drops the tile with no trace.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Delete a source range referenced by a dashboard tile, then reopen the dashboard.
```

## G15-SPREADSHEET_DASHBOARD-Q014

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q014
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Switching the active company context fully re-scopes a dashboard's tiles, so no tile continues to
  display figures computed under a previously active company.
WHY_IT_MATTERS: >
  A tile that keeps showing another company's figures after a company switch is a direct cross-tenant
  data leak.
DISCONFIRMING_OBSERVATION: >
  After switching the active company, a dashboard tile still shows a figure computed under the
  previous company's data.
EXPECTED_SURFACE: S4,S1
PRECONDITIONS: >
  As a user with access to two companies, view a dashboard under one company, then switch the active
  company and re-check the tile.
```

## G15-SPREADSHEET_DASHBOARD-Q015

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q015
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A dashboard's layout or configuration change made by one editor is visible identically to every
  other collaborator with access, not as a private personalization masquerading as a shared change.
WHY_IT_MATTERS: >
  A layout that silently diverges between collaborators breaks the shared reference the dashboard is
  meant to provide.
DISCONFIRMING_OBSERVATION: >
  One editor's layout change to a shared dashboard is not reflected when another collaborator with
  edit access opens it.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Change a shared dashboard's layout as one editor, then open it as a different collaborator with
  edit access.
```

## G15-SPREADSHEET_DASHBOARD-Q016

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q016
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A guest or external viewer granted access to a dashboard sees only the tiles explicitly shared with
  them, not the full set of tiles available to internal viewers by default.
WHY_IT_MATTERS: >
  A guest with default internal-level visibility can see far more of a dashboard's data than was
  intended when they were invited.
DISCONFIRMING_OBSERVATION: >
  A guest granted limited dashboard access can view additional tiles beyond what was explicitly
  shared.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Grant a guest access scoped to specific tiles and check whether other tiles are also reachable.
```

## G15-SPREADSHEET_DASHBOARD-Q017

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q017
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A tile's threshold or alert rule evaluates against its current, refreshed figure rather than a
  cached value already superseded by newer source data.
WHY_IT_MATTERS: >
  An alert evaluated against a stale figure can fail to fire, or fire incorrectly, exactly when it
  matters most.
DISCONFIRMING_OBSERVATION: >
  An alert fails to fire, or fires late, because it evaluated against a stale cached figure a
  subsequent data change had already superseded.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure a threshold alert, change the underlying data to cross the threshold, and observe the
  alert's timing relative to the change.
```

## G15-SPREADSHEET_DASHBOARD-Q018

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q018
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Deleting a dashboard has no effect on the underlying source data it aggregated.
WHY_IT_MATTERS: >
  A reporting layer that can destroy the data it merely summarizes would be an unacceptable and
  unexpected coupling.
DISCONFIRMING_OBSERVATION: >
  Removing a dashboard produces any observable change to the underlying source ranges or records.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Note the state of a dashboard's underlying source data, delete the dashboard, and re-check the
  source.
```

## G15-SPREADSHEET_DASHBOARD-Q019

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q019
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard's printed or exported version preserves the same as-of or refresh disclosure as its
  live view, rather than presenting a bare figure stripped of that context only in the export path.
WHY_IT_MATTERS: >
  A printed report missing staleness context can be circulated and relied on with no way for the
  reader to judge how current it actually is.
DISCONFIRMING_OBSERVATION: >
  An exported or printed dashboard drops the refresh-time disclosure the live view shows.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Compare the live dashboard's refresh disclosure to the same dashboard's exported or printed
  version.
```

## G15-SPREADSHEET_DASHBOARD-Q020

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q020
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A dashboard cannot itself be used as a write path back into its underlying source data; no
  interaction with a tile alters the source range or record it aggregates.
WHY_IT_MATTERS: >
  A reporting surface that can silently write back to its own source data blurs the line between
  reporting and operational editing, with unpredictable consequences.
DISCONFIRMING_OBSERVATION: >
  Any interaction with a dashboard tile changes the underlying source data it was built from.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Interact with a dashboard tile in every available way and check the underlying source data for any
  change.
```

## G15-SPREADSHEET_DASHBOARD-Q021

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q021
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard built from a template does not retain a live link to the original template's own data,
  only its structural definition.
WHY_IT_MATTERS: >
  A template that stays live-linked after being used turns a reusable structure into an unintended
  data-sharing channel.
DISCONFIRMING_OBSERVATION: >
  Editing the source template dashboard's data after a new dashboard was created from it also changes
  the new dashboard's figures.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a dashboard from a template, then edit the template's own data and check the new dashboard.
```

## G15-SPREADSHEET_DASHBOARD-Q022

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q022
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A company-wide dashboard search or directory listing only surfaces dashboards the searching user
  has permission to open.
WHY_IT_MATTERS: >
  A search that ignores dashboard-level permission is a systemic bypass of every dashboard's access
  controls at once.
DISCONFIRMING_OBSERVATION: >
  A company-wide dashboard search reveals the name or content of a dashboard the searching user
  cannot open.
EXPECTED_SURFACE: S4,S3
PRECONDITIONS: >
  Create a dashboard the test user cannot access, then search for it as that user.
```

## G15-SPREADSHEET_DASHBOARD-Q023

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q023
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A real-time tile and a batch-refreshed tile placed on the same dashboard are each visually labeled
  with their own refresh mode, so a viewer cannot mistake a batch figure for a real-time one.
WHY_IT_MATTERS: >
  Mixing refresh modes with no visual distinction lets a viewer treat a stale batch figure as if it
  were live.
DISCONFIRMING_OBSERVATION: >
  A dashboard mixes real-time and batch tiles with no visual distinction identifying which is which.
EXPECTED_SURFACE: S5,S7
PRECONDITIONS: >
  Place a real-time and a batch-refreshed tile on the same dashboard and inspect their visual
  labeling.
```

## G15-SPREADSHEET_DASHBOARD-Q024

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q024
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A tile's underlying aggregation does not silently sample or truncate a large source data set
  without disclosing that the figure is based on partial data.
WHY_IT_MATTERS: >
  An undisclosed partial computation on a large data set produces a total that looks complete but is
  materially wrong.
DISCONFIRMING_OBSERVATION: >
  A tile's total for a large data set differs from a full direct computation over the same data, with
  no disclosure that only part of it was read.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Build a tile aggregating a very large source range and compare its total to a full direct
  computation over the same data.
```

## G15-SPREADSHEET_DASHBOARD-Q025

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q025
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Undoing a layout or configuration change to a dashboard restores the exact prior tile arrangement
  and settings, not merely a similar-looking default state.
WHY_IT_MATTERS: >
  An undo that produces a plausible but different layout can leave the dashboard visibly wrong with
  nobody realizing the undo was incomplete.
DISCONFIRMING_OBSERVATION: >
  Undoing a dashboard layout change results in a different arrangement than what existed immediately
  before the change.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Note a dashboard's exact layout, change it, then undo and compare to the original.
```

## G15-SPREADSHEET_DASHBOARD-Q026

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q026
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard's own activity or change log records who altered a tile's configuration and when,
  distinct from any log of the underlying source data's own changes.
WHY_IT_MATTERS: >
  Without a distinguishable configuration history, nobody can determine whether a wrong figure
  resulted from a data change or a tile misconfiguration.
DISCONFIRMING_OBSERVATION: >
  The dashboard's own change history cannot be distinguished from changes made to its underlying
  source data.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Change a tile's configuration and separately change its underlying source data, then compare their
  traces in the log.
```

## G15-SPREADSHEET_DASHBOARD-Q027

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q027
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Removing a source data range referenced by more than one dashboard produces the same defined
  outcome, such as an equivalent error state, for every dashboard referencing it, rather than
  inconsistent behaviour between them.
WHY_IT_MATTERS: >
  Inconsistent handling of the same underlying failure across dashboards makes the platform's
  behaviour unpredictable and harder to diagnose.
DISCONFIRMING_OBSERVATION: >
  Two different dashboards referencing the same now-deleted source range display inconsistent
  outcomes for the equivalent tile.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Reference the same source range from two separate dashboards, delete the range, and compare both
  dashboards' outcomes.
```

## G15-SPREADSHEET_DASHBOARD-Q028

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q028
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A tile configured to aggregate over a rolling period, such as a trailing window of days,
  recalculates its window as time passes without requiring the tile to be manually reconfigured.
WHY_IT_MATTERS: >
  A rolling window that fails to advance silently turns a "recent activity" figure into a stale,
  fixed snapshot.
DISCONFIRMING_OBSERVATION: >
  A rolling-period tile continues to reflect the same fixed date range well past when the rolling
  window should have advanced.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure a rolling-period tile, let time pass well beyond the window length, and check whether the
  window advanced.
```

## G15-SPREADSHEET_DASHBOARD-Q029

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q029
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A dashboard embedded in an external page cannot be viewed by someone who could not open the
  dashboard directly due to lacking permission.
WHY_IT_MATTERS: >
  An embed that bypasses the dashboard's own authorization is a separate, unguarded access path to
  the same data.
DISCONFIRMING_OBSERVATION: >
  An embedded version of a dashboard is viewable by someone who could not open the dashboard directly.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Embed a dashboard in an external page and attempt to view it as a user with no direct dashboard
  permission.
```

## G15-SPREADSHEET_DASHBOARD-Q030

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q030
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a dashboard performs a currency or unit conversion, it uses a single disclosed basis
  consistently across every tile on the same dashboard, rather than silently mixing bases between
  tiles.
WHY_IT_MATTERS: >
  Two tiles meant to be compared but converted on different, undisclosed bases can lead to a
  materially wrong conclusion.
DISCONFIRMING_OBSERVATION: >
  Two tiles on the same dashboard apply different, undisclosed conversion bases to figures that
  should be comparable.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Build two comparable tiles requiring conversion on the same dashboard and check whether their
  conversion basis actually matches.
```

## G15-SPREADSHEET_DASHBOARD-Q031

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q031
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard's rendering does not silently degrade into showing partial tiles as though complete
  under heavy concurrent viewer load.
WHY_IT_MATTERS: >
  A partial render presented as complete under load misleads viewers exactly when many people are
  relying on the dashboard at once.
DISCONFIRMING_OBSERVATION: >
  Under concurrent viewer load, some tiles render incomplete figures with no indication that the
  render was incomplete.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Generate heavy concurrent viewer load on a dashboard and inspect whether any tile renders
  incompletely without a warning.
```

## G15-SPREADSHEET_DASHBOARD-Q032

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q032
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A tile referencing a source range within an archived or read-only workbook either continues to
  display accurate figures or explicitly flags that its source is now archived, rather than silently
  going stale with no notice.
WHY_IT_MATTERS: >
  A tile that silently freezes without any flag can be mistaken for a live figure long after its
  source stopped updating.
DISCONFIRMING_OBSERVATION: >
  A tile referencing an archived source workbook shows outdated figures with no indication the source
  is no longer active.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Archive a workbook referenced by a dashboard tile, then re-check the tile's display and any
  associated flag.
```

## G15-SPREADSHEET_DASHBOARD-Q033

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q033
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A viewer's own session-level personalization, such as a collapsed section, does not get persisted
  as a shared change visible to other viewers.
WHY_IT_MATTERS: >
  A personalization that leaks to other viewers would mean nobody could safely adjust their own view
  without disturbing everyone else's.
DISCONFIRMING_OBSERVATION: >
  One viewer's session-only display personalization becomes visible to other viewers of the same
  shared dashboard.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  Collapse a section as one viewer and check whether it appears collapsed for a different concurrent
  viewer.
```

## G15-SPREADSHEET_DASHBOARD-Q034

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q034
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A dashboard's scheduled export or email distribution list is restricted to recipients the owner
  explicitly configured, and does not silently include additional recipients through an inherited or
  default list.
WHY_IT_MATTERS: >
  A distribution reaching unintended recipients can leak aggregated figures well beyond who the owner
  meant to see them.
DISCONFIRMING_OBSERVATION: >
  A scheduled dashboard distribution reaches a recipient the owner never explicitly added to that
  distribution.
EXPECTED_SURFACE: S4,S8
PRECONDITIONS: >
  Configure a scheduled distribution to a specific list and verify the actual recipients of a
  delivered run.
```

## G15-SPREADSHEET_DASHBOARD-Q035

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q035
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A dashboard tile that links through to navigate to an underlying record respects that record's own
  access control at the destination, even if the tile itself was reachable.
WHY_IT_MATTERS: >
  A click-through that ignores the destination's own access control lets a dashboard become an
  unintended bypass into records a viewer should not open.
DISCONFIRMING_OBSERVATION: >
  Clicking through a dashboard tile opens an underlying record the viewer could not otherwise open
  directly.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Configure a tile linking to a specific record, restrict a viewer's direct access to that record, and
  have them click through.
```

## G15-SPREADSHEET_DASHBOARD-Q036

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q036
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A tile's calculation definition, what is aggregated and how, is inspectable by an authorized editor
  rather than being an opaque figure with no way to verify what it represents.
WHY_IT_MATTERS: >
  An opaque tile cannot be trusted or corrected because nobody authorized to maintain it can verify
  what it is actually computing.
DISCONFIRMING_OBSERVATION: >
  An authorized dashboard editor has no way to inspect what a tile's figure actually represents or how
  it was computed.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  As an authorized editor, attempt to inspect a tile's underlying aggregation definition.
```

## G15-SPREADSHEET_DASHBOARD-Q037

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q037
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A tile's period-over-period comparison, such as this period versus last, uses a consistent,
  disclosed period-boundary definition rather than one that silently shifts depending on when the
  dashboard happens to be viewed.
WHY_IT_MATTERS: >
  A shifting boundary can make the same comparison figure mean something different depending on the
  day it is viewed, with no way to tell.
DISCONFIRMING_OBSERVATION: >
  Viewing the same comparison tile on different days within the same period produces
  boundary-inconsistent results not explainable by new data alone.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  View the same period comparison tile on different days within the same period and compare results.
```

## G15-SPREADSHEET_DASHBOARD-Q038

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q038
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A dashboard shared outside the company or tenant boundary that owns its underlying data does not
  carry live updating figures to a recipient who has no access within that tenant.
WHY_IT_MATTERS: >
  Live figures reaching a recipient outside the owning tenant is a direct cross-tenant data
  exfiltration path.
DISCONFIRMING_OBSERVATION: >
  A dashboard shared externally continues to serve live, updating figures sourced from data in a
  tenant the recipient has no access to.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Share a dashboard with a user outside its owning tenant and check whether they receive live
  updates.
```

## G15-SPREADSHEET_DASHBOARD-Q039

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q039
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A tile explicitly restricted to a smaller group within an otherwise shared dashboard is enforced
  even for viewers who otherwise have general dashboard access.
WHY_IT_MATTERS: >
  Tile-level confidentiality that a general dashboard permission overrides is not an effective
  control.
DISCONFIRMING_OBSERVATION: >
  A viewer with general dashboard access can see a tile explicitly restricted to a smaller group.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Restrict a specific tile to a subset of dashboard viewers, then check visibility as a viewer
  outside that subset.
```

## G15-SPREADSHEET_DASHBOARD-Q040

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q040
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A single tile's data-source failure does not prevent the entire dashboard from rendering; unaffected
  tiles continue to display while the affected one shows its own error state.
WHY_IT_MATTERS: >
  One broken tile taking down the whole dashboard denies access to every other unrelated figure that
  was otherwise fine.
DISCONFIRMING_OBSERVATION: >
  A single tile's source failure prevents the entire dashboard page from rendering any tile at all.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Break one tile's source on a multi-tile dashboard and observe whether the rest of the dashboard
  still renders.
```

## G15-SPREADSHEET_DASHBOARD-Q041

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q041
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reverting a dashboard to a previous saved configuration restores the tile definitions as they were
  at that version, not a mix of the old layout with currently configured tile logic.
WHY_IT_MATTERS: >
  A restore that mixes historical layout with current logic misrepresents what that earlier version
  actually computed.
DISCONFIRMING_OBSERVATION: >
  Restoring an earlier dashboard version applies current tile logic rather than the logic in force at
  that historical version.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Save a dashboard version, change a tile's logic, then restore the earlier version and check which
  logic applies.
```

## G15-SPREADSHEET_DASHBOARD-Q042

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q042
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A dashboard KPI, when independently verified against a direct computation over the same underlying
  source data and period, agrees with that computation within any disclosed rounding tolerance.
WHY_IT_MATTERS: >
  A KPI that disagrees with its own source data undermines confidence in every figure the dashboard
  presents.
DISCONFIRMING_OBSERVATION: >
  A dashboard figure disagrees with a direct computation over the same underlying source data and
  period, beyond any stated rounding tolerance.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Independently compute the same figure directly from the source data and compare it to the
  dashboard's displayed KPI.
```

## G15-SPREADSHEET_DASHBOARD-Q043

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q043
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where the underlying source enforces record ownership or scoping, a tile's aggregation respects that
  scoping so a scoped viewer's total does not silently include records outside their own scope.
WHY_IT_MATTERS: >
  An aggregation that ignores source-level scoping leaks the existence and magnitude of records a
  viewer should not be able to see even indirectly.
DISCONFIRMING_OBSERVATION: >
  A scoped viewer's dashboard total is larger than what records within their own scope could account
  for.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Scope a viewer to a subset of source records, then compare their dashboard total to what that
  subset alone could produce.
```

## G15-SPREADSHEET_DASHBOARD-Q044

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q044
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard's configuration can be exported and re-imported into a different environment without
  silently resolving its tiles against unintended source data in the new environment.
WHY_IT_MATTERS: >
  A silent mis-resolution across environments can produce a dashboard that looks correctly configured
  but reports on entirely wrong data.
DISCONFIRMING_OBSERVATION: >
  A dashboard configuration imported into a different environment silently resolves its tiles against
  unintended data with no validation or error.
EXPECTED_SURFACE: S7,S3
PRECONDITIONS: >
  Export a dashboard's configuration, import it into a different environment, and check what source
  data its tiles resolve to.
```

## G15-SPREADSHEET_DASHBOARD-Q045

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q045
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard's caching layer, if present, invalidates and recomputes an affected tile promptly after
  a relevant source data change rather than serving a stale figure indefinitely until an unrelated
  scheduled cycle.
WHY_IT_MATTERS: >
  A cache that only clears on an unrelated schedule can leave an obviously outdated figure displayed
  long after it should have changed.
DISCONFIRMING_OBSERVATION: >
  A source data change produces no eventual update to a dependent tile even after a reasonable wait
  beyond any disclosed refresh interval.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Change source data behind a cached tile and wait beyond the disclosed refresh interval to check for
  an update.
```

## G15-SPREADSHEET_DASHBOARD-Q046

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q046
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Two dashboards owned by different users but referencing the same underlying source range compute
  independently and do not leak one owner's tile configuration or filter settings to the other.
WHY_IT_MATTERS: >
  Configuration leaking between independently owned dashboards would expose one user's private
  analysis choices to another.
DISCONFIRMING_OBSERVATION: >
  One user's dashboard tile configuration or filter becomes visible or applied on a different user's
  separately owned dashboard referencing the same source.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Have two users independently build dashboards referencing the same source range with different
  configurations, and check for any cross-leakage.
```

## G15-SPREADSHEET_DASHBOARD-Q047

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q047
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A tile configured to aggregate only the records a viewer is permitted to see recalculates that
  scope as the viewer's own permissions change over time, not against a permission snapshot taken
  when the tile was first configured.
WHY_IT_MATTERS: >
  A stale permission snapshot can let a viewer keep seeing an aggregation reflecting access they no
  longer actually have.
DISCONFIRMING_OBSERVATION: >
  A viewer whose permissions were reduced still sees a dashboard total reflecting their earlier,
  broader scope.
EXPECTED_SURFACE: S4,S1
PRECONDITIONS: >
  Reduce a viewer's permission scope after a tile was already configured for them, then re-check
  their dashboard total.
```

## G15-SPREADSHEET_DASHBOARD-Q048

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q048
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A tile does not fall back to a cached figure from a different, unrelated data context when its
  intended source is temporarily unavailable, without disclosing that the figure shown is not from
  the intended source.
WHY_IT_MATTERS: >
  A silent fallback to unrelated data during an outage can present a plausible but entirely wrong
  figure with no disclosure.
DISCONFIRMING_OBSERVATION: >
  A tile shows a plausible figure during a source outage that turns out to be unrelated placeholder or
  cached data from a different context, with no disclosure.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Make a tile's intended source temporarily unavailable and inspect what figure, if any, it displays
  and whether it is disclosed as not from the intended source.
```

## G15-SPREADSHEET_DASHBOARD-Q049

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q049
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A tile's drill-down breadcrumb accurately reflects the actual aggregation path taken, including
  which filters were applied, so a viewer reviewing the drill-down is not misled about what scope
  produced the figures shown.
WHY_IT_MATTERS: >
  A breadcrumb that misstates the actual filter scope can lead a viewer to draw a conclusion about the
  wrong subset of data.
DISCONFIRMING_OBSERVATION: >
  A drill-down view's stated filter or scope does not match the actual data being displayed.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Drill down through a tile with a specific filter applied and verify the breadcrumb against the
  actual data shown.
```

## G15-SPREADSHEET_DASHBOARD-Q050

```yaml
QID: G15-SPREADSHEET_DASHBOARD-Q050
MODULE: spreadsheet_dashboard
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Archiving a dashboard, as distinct from deleting it, preserves its configuration and history in a
  retrievable form rather than being functionally indistinguishable from deletion.
WHY_IT_MATTERS: >
  If archiving behaves like deletion, users lose a safe, reversible way to retire a dashboard without
  destroying its record.
DISCONFIRMING_OBSERVATION: >
  An archived dashboard's configuration or history cannot actually be retrieved or restored, making
  archiving equivalent to deletion.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Archive a dashboard, then attempt to retrieve or restore its configuration and history.
```
