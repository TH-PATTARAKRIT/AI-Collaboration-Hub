# SMEsPlus ENTERPRISE SUITE
## GMVQ — G15 PRODUCTIVITY / spreadsheet_dashboard_account Module MVQ Bank

**Document ID:** GMVQ-G15-SPREADSHEET_DASHBOARD_ACCOUNT-MVQ48-V1.00
**Group:** G15 PRODUCTIVITY (Wave W4)
**Module Metadata:** `spreadsheet_dashboard_account`
**Wave:** W4
**Author Cell:** P15-1 (GMVQ Question Factory — Production Cell P15-1)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for the two-way bridge between the base dashboard
capability and accounting data. Per the Bridge Module Rule, every question here fails the "would this
still make sense with the capability removed" test in the affirmative direction: each one is a seam
question that only exists because a live reporting layer is drawing on accounting data, not a
restatement of either the base dashboard bank's own general behaviour or of the accounting group's own
questions. The material ground is staleness disclosure, draft-versus-posted inclusion, cached-versus-
live authority, aggregation permission leakage that lets a viewer infer a restricted transaction,
multi-currency and multi-period reconciliation on the reporting layer, and reversal/lifecycle mismatch
between a snapshot and the ledger it summarized.

Sibling bridge banks in this group (`spreadsheet_dashboard_hr_expense`, `spreadsheet_dashboard_sale`,
`spreadsheet_dashboard_stock_account`, and others) were checked against this bank's ground at
authoring time per the Bridge Module Rule's pre-authoring step; none existed yet in this batch, so no
cross-bank duplication was found to remove. A later cell adding a sibling bank must run the same check
against this bank's HYPOTHESIS lines before authoring.

Question text is source-neutral. It does not name the module, any vendor or product, or any technical
identifier.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because each tests a distinct seam-only hypothesis, spread across
  ordering, partiality, ownership, timing, reversal, quantity/money, lifecycle mismatch, error
  asymmetry, and authority as defined by the Bridge Module Rule.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q001

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q001
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard tile aggregating a financial figure distinguishes posted transactions from
  not-yet-posted draft ones, rather than silently combining both into a single total.
WHY_IT_MATTERS: >
  A total that quietly includes still-changeable draft entries misrepresents a financial position as
  more final than it actually is.
DISCONFIRMING_OBSERVATION: >
  Discarding a draft entry before it is posted still changes a dashboard total that had already
  included it, with no distinction ever shown between posted and draft contributions.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Create a draft accounting entry, note the dashboard total, then discard the draft without posting
  and compare.
LAYER: PROCESS
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q002

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q002
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an accounting entry is reversed after a dashboard snapshot has already been generated or
  distributed, reopening that snapshot discloses that its figure predates the reversal, rather than
  silently presenting the pre-reversal figure as current.
WHY_IT_MATTERS: >
  A distributed report that silently becomes wrong after a reversal can drive a decision on a figure
  everyone believes is still accurate.
DISCONFIRMING_OBSERVATION: >
  Opening a previously distributed dashboard snapshot after a reversal shows the old total with no
  indication it may be outdated relative to the ledger.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Distribute a dashboard snapshot including a figure, reverse the underlying entry, then reopen the
  snapshot.
LAYER: PROCESS
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q003

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q003
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a dashboard's cached aggregated balance and the ledger's live balance for the same account
  diverge due to refresh timing, the dashboard discloses which figure is authoritative rather than
  presenting both silently as equally current.
WHY_IT_MATTERS: >
  Two figures presented as equally valid but actually disagreeing leaves the viewer no way to know
  which one to trust.
DISCONFIRMING_OBSERVATION: >
  The dashboard and a live ledger view show different totals for the same account at the same moment
  with neither labeled as the cached or lagging one.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Post an entry, then immediately compare the dashboard's cached figure to the ledger's live figure
  for the same account before the next refresh.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q004

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q004
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard tile aggregating accounting data discloses its refresh cadence, whether scheduled batch
  or on-demand, so a batch-refreshed figure is not presented indistinguishably from a real-time one.
WHY_IT_MATTERS: >
  A viewer who assumes a batch figure is live may act on it without accounting for the lag.
DISCONFIRMING_OBSERVATION: >
  A dashboard tile aggregating accounting data gives no indication of when its underlying data was
  last refreshed.
EXPECTED_SURFACE: S7,S5
PRECONDITIONS: >
  Inspect a dashboard tile aggregating accounting figures for any refresh-time disclosure.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q005

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q005
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A viewer permitted to see an aggregated financial total, but not permitted to view individual
  accounting entries, cannot narrow the dashboard's own filters to a small enough window to infer the
  value of a single underlying transaction.
WHY_IT_MATTERS: >
  An aggregation that can be narrowed down to one transaction converts a summary-level permission into
  full entry-level exposure through a side channel.
DISCONFIRMING_OBSERVATION: >
  Some combination of available dashboard filters lets a restricted viewer isolate the precise
  contribution of an account or entry they are not permitted to view directly.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a viewer with aggregate-only access, attempt to narrow the dashboard's date or account filters
  until only one underlying transaction remains represented.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q006

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q006
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a dashboard aggregation spans an accounting period that has since closed and one that remains
  open, the dashboard attributes which portion of its total comes from the still-open, still-changeable
  period.
WHY_IT_MATTERS: >
  A merged total gives no way to know how much of a reported figure could still change before the
  open period closes.
DISCONFIRMING_OBSERVATION: >
  A dashboard total spanning a closed and an open period gives no way to tell how much derives from
  the still-open portion.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Build a dashboard total spanning a closed period and a currently open one, and inspect whether the
  open-period contribution is distinguishable.
LAYER: PROCESS
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q007

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q007
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard aggregation combining amounts recorded in more than one currency applies a single,
  disclosed exchange-rate basis, such as a stated rate date, rather than silently mixing rates from
  different dates without disclosure.
WHY_IT_MATTERS: >
  A multi-currency total that mixes undisclosed rate dates can move materially with no underlying
  transaction ever changing, misleading anyone tracking it.
DISCONFIRMING_OBSERVATION: >
  The same multi-currency dashboard total changes materially between two viewings with no
  configuration change and no disclosed reason tied to a rate date.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  View a multi-currency dashboard total on two occasions with no underlying transaction change and
  compare, checking for any disclosed rate basis.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q008

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q008
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a dashboard's aggregation query over accounting data fails partway through, for example on
  timeout against a large account set, it reports the failure rather than displaying a partial sum as
  though it were the complete total.
WHY_IT_MATTERS: >
  A partial sum presented as complete is a plausible-looking but materially wrong financial figure
  with no reason for anyone to question it.
DISCONFIRMING_OBSERVATION: >
  A dashboard tile shows a plausible-looking total when in fact only some of the underlying accounts
  were successfully included.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Force a partial failure in a large accounting aggregation query and inspect what the tile displays.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q009

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q009
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Archiving or closing an account referenced by an existing dashboard tile places that tile in an
  explicit error or notice state rather than silently dropping the account's contribution from the
  total with no indication.
WHY_IT_MATTERS: >
  A silently shrunken total after an account archival looks like a real decline rather than a
  reporting artifact.
DISCONFIRMING_OBSERVATION: >
  After an underlying account is archived, its dashboard tile's total silently drops without any flag
  that a component became unavailable.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Archive an account referenced by a dashboard tile and inspect the tile's resulting total and any
  flag.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q010

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q010
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A viewer's access to a dashboard's aggregated account total is revoked promptly when their access to
  the underlying accounting data is revoked, rather than the dashboard continuing to serve a cached
  view of data they can no longer see directly.
WHY_IT_MATTERS: >
  A dashboard that outlives the underlying access revocation is an unrevoked, invisible access path
  to financial data.
DISCONFIRMING_OBSERVATION: >
  A user whose accounting access was revoked can still view a previously loaded dashboard tile's
  up-to-date total.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Revoke a user's underlying accounting access while they have a dashboard tile open, and check
  whether it keeps updating for them.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q011

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q011
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Drilling down from an aggregated dashboard figure into the underlying accounting transactions
  applies the same company and branch scoping the viewer would face accessing the accounting system
  directly.
WHY_IT_MATTERS: >
  A drill-down that ignores company or branch scoping turns a dashboard into a bypass around the
  accounting system's own tenant boundary.
DISCONFIRMING_OBSERVATION: >
  Drill-down from the dashboard surfaces individual entries the viewer could not open directly in the
  accounting module.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Restrict a viewer's branch scope in accounting, then have that viewer drill down from a
  company-wide dashboard total.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q012

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q012
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A scheduled dashboard refresh drawing on accounting data that fails to complete is surfaced to the
  dashboard owner as a failure, rather than silently leaving the last successful figure displayed
  with no distinction from a fresh one.
WHY_IT_MATTERS: >
  A silent refresh failure over financial data leaves the owner relying on a figure that may already
  be materially outdated.
DISCONFIRMING_OBSERVATION: >
  A failed scheduled refresh leaves the dashboard showing an old accounting total with no different
  presentation from a successfully refreshed one.
EXPECTED_SURFACE: S8,S7
PRECONDITIONS: >
  Force a scheduled refresh of an accounting tile to fail and check for any owner-facing notice.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q013

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q013
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A dashboard KPI derived from accounting data agrees with the equivalent figure produced directly by
  the accounting reporting system for the same period and as-of point, within any disclosed rounding
  tolerance.
WHY_IT_MATTERS: >
  A dashboard figure that disagrees with the accounting system's own report for the identical period
  undermines confidence in every figure the dashboard presents.
DISCONFIRMING_OBSERVATION: >
  The dashboard figure and the accounting system's own report for the identical period disagree
  beyond any stated rounding tolerance, with no explanation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Produce the equivalent report directly from accounting for the same period and compare it to the
  dashboard's KPI.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q014

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q014
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Sharing a dashboard outside the boundary of the company that owns the underlying accounting data
  does not carry live aggregated financial figures to a recipient with no accounting access in that
  company.
WHY_IT_MATTERS: >
  Live financial figures reaching a recipient outside the owning company is a direct cross-tenant
  financial data leak.
DISCONFIRMING_OBSERVATION: >
  A dashboard shared to an external or cross-tenant recipient still renders live totals sourced from
  accounting data in a company that recipient has no access to.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Share an accounting-derived dashboard with a recipient outside the owning company and check for
  live updating figures.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q015

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q015
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard tile's as-of timestamp reflects the actual point at which the underlying accounting
  data was read, not the time the dashboard page happened to render.
WHY_IT_MATTERS: >
  An as-of time tied only to page load gives a false sense of freshness for a figure that may not
  actually have been re-read.
DISCONFIRMING_OBSERVATION: >
  The displayed as-of time changes on every page load even when the underlying accounting data has
  not actually been re-read.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Reload the same accounting-derived dashboard page twice with no underlying data change and compare
  the displayed as-of time.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q016

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q016
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Duplicating a dashboard that includes accounting-derived tiles copies the tile configuration but
  does not carry over the source dashboard's already-computed figures as though they were fresh for
  the new copy.
WHY_IT_MATTERS: >
  A duplicate that inherits stale accounting figures can be mistaken for a dashboard that already ran
  its own aggregation against current data.
DISCONFIRMING_OBSERVATION: >
  A newly duplicated dashboard displays the source dashboard's old computed totals before ever
  running its own aggregation.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Duplicate a dashboard with accounting tiles and check what the copy shows before any refresh cycle
  completes.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q017

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q017
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The dashboard interface cannot be used as a path to modify the underlying accounting records it
  aggregates; no interaction with a displayed figure writes back to the ledger.
WHY_IT_MATTERS: >
  A reporting surface able to silently alter the ledger it summarizes would corrupt the distinction
  between reporting and financial transaction control.
DISCONFIRMING_OBSERVATION: >
  Changing a displayed dashboard figure directly alters the underlying accounting entries.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Attempt every available interaction on an accounting-derived dashboard figure and check the
  underlying ledger for any change.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q018

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q018
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When two accounting entries affecting the same dashboard aggregation post concurrently, the
  dashboard's eventual total reflects both rather than only whichever posted last silently
  overwriting the other's contribution.
WHY_IT_MATTERS: >
  A dropped concurrent posting produces a total that is missing real financial activity with no sign
  anything was lost.
DISCONFIRMING_OBSERVATION: >
  Two concurrent postings that should both count toward the same total result in a dashboard figure
  reflecting only one of them.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Post two entries affecting the same aggregation at nearly the same time and check whether the
  dashboard total reflects both.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q019

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q019
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard's period-over-period comparison of accounting figures applies the same closing and
  cutoff boundary logic the accounting system itself uses for period boundaries.
WHY_IT_MATTERS: >
  A dashboard using its own independent cutoff can split the same transaction into a different period
  than the accounting close did, producing a comparison that does not match the books.
DISCONFIRMING_OBSERVATION: >
  The dashboard's period-over-period figures split transactions into different periods than the
  accounting system's own period closing does for the same dates.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Post a transaction near a period boundary and compare which period it falls into on the dashboard
  versus in the accounting system's own closing.
LAYER: PROCESS
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q020

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q020
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A dashboard tile combining figures from more than one accounting company reconciles them on a
  common company or branch key rather than silently summing figures that belong to different legal
  or reporting boundaries.
WHY_IT_MATTERS: >
  A silently merged multi-company total makes it impossible to attribute financial results back to
  the correct legal entity.
DISCONFIRMING_OBSERVATION: >
  A consolidated dashboard total mixes figures from separate companies without any way to attribute
  how much came from each.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Build a tile combining figures from two companies and check whether their individual contributions
  can be attributed.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q021

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q021
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A viewer whose role grants access only to their own branch's accounting data sees dashboard
  aggregations scoped to that branch, not a company-wide total silently including other branches'
  figures.
WHY_IT_MATTERS: >
  A branch-scoped viewer seeing a company-wide total leaks the existence and scale of other branches'
  financial activity they have no permission to see.
DISCONFIRMING_OBSERVATION: >
  A branch-scoped user's dashboard total is larger than what their own branch's accounting data could
  account for.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Scope a viewer to a single branch and compare their dashboard total to what that branch alone could
  produce.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q022

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q022
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard export or scheduled email of an accounting-derived figure carries the same as-of or
  staleness disclosure as the live dashboard view, rather than a bare number stripped of that context.
WHY_IT_MATTERS: >
  A distributed report missing staleness context can be relied on with no way for the reader to judge
  how current the financial figure actually is.
DISCONFIRMING_OBSERVATION: >
  An exported or emailed dashboard report presents an accounting total with no indication of when it
  was computed relative to the ledger.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Compare the live dashboard's as-of disclosure to the same figure's exported or emailed version.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q023

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q023
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A cached accounting aggregation is invalidated and recomputed after a correcting or adjusting entry
  is posted, rather than continuing to serve a stale cached value indefinitely until an unrelated
  scheduled cycle.
WHY_IT_MATTERS: >
  A correction that never surfaces on the dashboard leaves a known-wrong figure displayed as though
  it were still accurate.
DISCONFIRMING_OBSERVATION: >
  Posting a correcting entry produces no eventual change in a dashboard figure that should include
  it, even after a reasonable wait.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Post a correcting entry affecting a cached dashboard figure and wait a reasonable interval to check
  for an update.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q024

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q024
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard tile referencing an account that has since been merged or renumbered continues to
  resolve to the correct underlying data rather than silently reporting on a stale or orphaned
  reference.
WHY_IT_MATTERS: >
  A tile silently pointing at the wrong account after a renumbering can misreport financial figures
  indefinitely with no visible error.
DISCONFIRMING_OBSERVATION: >
  After an account renumbering, the dashboard tile's total no longer matches what the renumbered
  account actually contains, without any error shown.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Renumber an account referenced by a dashboard tile and compare the tile's total to the account's
  actual current contents.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q025

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q025
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A filter one viewer applies to an accounting-derived dashboard does not alter the figures another
  concurrent viewer of the same shared dashboard sees.
WHY_IT_MATTERS: >
  A filter that leaks into shared state would mean two viewers relying on the same financial dashboard
  could unknowingly be looking at different scopes.
DISCONFIRMING_OBSERVATION: >
  One viewer narrowing a dashboard's account filter changes the total another concurrent viewer sees
  on the same shared dashboard.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  Apply an account filter as one viewer while a second viewer concurrently views the same shared
  dashboard, and compare what each sees.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q026

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q026
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard aggregating tax-inclusive or tax-exclusive accounting figures discloses which basis it
  is using, so a viewer comparing it to a source report cannot mistake one basis for the other.
WHY_IT_MATTERS: >
  An undisclosed tax basis mismatch can make a dashboard figure and a source report disagree by an
  amount someone might mistake for an error elsewhere.
DISCONFIRMING_OBSERVATION: >
  A dashboard figure and the equivalent accounting report disagree by an amount consistent with a tax
  basis mismatch, with no disclosure of which basis the dashboard used.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare a dashboard's tax-sensitive total to the equivalent accounting report and check for a
  disclosed basis.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q027

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q027
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When an account is reclassified into a different category, a dashboard tile previously configured
  against the old category is flagged for review rather than silently continuing to aggregate under a
  category definition that no longer matches.
WHY_IT_MATTERS: >
  A tile silently misaligned with a reclassified structure can keep reporting under a label that no
  longer reflects how the data is actually organized.
DISCONFIRMING_OBSERVATION: >
  A dashboard tile keeps producing figures under an account-category label that no longer matches how
  the underlying accounting data is actually classified, with no notice.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Reclassify an account referenced by a dashboard tile's category filter and check for any flag on
  the tile.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q028

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q028
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A dashboard explicitly saved as a fixed point-in-time snapshot for closing reporting purposes
  remains immutable to later ledger changes, so it does not silently update after distribution.
WHY_IT_MATTERS: >
  A closing snapshot that silently changes after distribution defeats the purpose of freezing a
  formal reporting record for that period.
DISCONFIRMING_OBSERVATION: >
  A dashboard explicitly saved as a fixed point-in-time snapshot changes its figures after later
  postings to the ledger.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Save an accounting-derived dashboard as a fixed snapshot, post further ledger entries, then reopen
  the snapshot.
LAYER: PROCESS
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q029

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q029
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A dashboard's scheduled distribution of an accounting-derived report is scoped to recipients who
  hold the same accounting access the figures would require to view directly, rather than reaching a
  broader list irrespective of underlying access.
WHY_IT_MATTERS: >
  A scheduled distribution reaching someone without underlying accounting access is a bypass of the
  accounting system's own permission model.
DISCONFIRMING_OBSERVATION: >
  A scheduled dashboard distribution reaches a recipient who has no direct permission to view the
  underlying accounting data being summarized.
EXPECTED_SURFACE: S4,S8
PRECONDITIONS: >
  Configure a scheduled distribution of an accounting-derived dashboard and check the actual
  recipients' underlying accounting access.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q030

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q030
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard threshold or alert rule tied to an accounting figure evaluates against the current
  authoritative ledger value rather than a cached value already superseded by a subsequent posting.
WHY_IT_MATTERS: >
  An alert evaluated against a stale cached figure can fail to fire, or fire incorrectly, exactly when
  a real financial threshold is crossed.
DISCONFIRMING_OBSERVATION: >
  An alert fails to fire, or fires incorrectly, because it evaluated against a cached figure that a
  recent posting had already superseded.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure an accounting threshold alert, post an entry that crosses it, and observe the alert's
  timing relative to the posting.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q031

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q031
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A dashboard aggregation of accounting figures rounds consistently with the accounting system's own
  rounding rule for that currency, rather than applying an independent rounding approach.
WHY_IT_MATTERS: >
  A rounding mismatch between the dashboard and the accounting system can make a manual reconciliation
  of the two figures never quite tie out, with no real discrepancy behind it.
DISCONFIRMING_OBSERVATION: >
  Summing the dashboard's displayed line-level figures by hand does not match its own displayed total,
  by more than the accounting system's own rounding rule would allow.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Sum a dashboard's displayed line-level accounting figures by hand and compare to the tile's own
  displayed total.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q032

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q032
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard tile built on accounting data does not continue rendering figures once the underlying
  data source connection or account access has been withdrawn, without any indication that the
  figures shown are no longer live.
WHY_IT_MATTERS: >
  A tile that keeps looking live after its source connection is gone can be relied on for a decision
  well after it stopped reflecting reality.
DISCONFIRMING_OBSERVATION: >
  A dashboard keeps rendering what looks like current figures after the accounting data source behind
  it has been disconnected or revoked.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Disconnect the accounting data source behind a dashboard tile and check what the tile continues to
  display.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q033

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q033
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A dashboard's calculation of an accounting ratio, such as a margin, uses figures drawn from the same
  as-of point for both numerator and denominator, rather than combining a real-time figure with a
  stale cached one.
WHY_IT_MATTERS: >
  A ratio combining figures from two different moments can move for reasons that have nothing to do
  with the actual underlying business relationship it is meant to represent.
DISCONFIRMING_OBSERVATION: >
  A dashboard ratio changes in a way explainable only by its two component figures being read at
  different, undisclosed points in time.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Inspect a dashboard ratio tile's two component figures for whether they share the same as-of point.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q034

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q034
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Restoring a dashboard from a backup or prior version does not silently reconnect it to whatever
  accounting structure currently exists under the same identifiers if that structure was redefined
  since the dashboard's original save point, without flagging the mismatch.
WHY_IT_MATTERS: >
  A restored dashboard silently pointing at a redefined accounting structure can report figures under
  a stale assumption about what that structure means.
DISCONFIRMING_OBSERVATION: >
  A restored older dashboard configuration silently reports figures against accounting structures
  that were redefined after the dashboard's original save point, with no warning.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Save a dashboard version, redefine the referenced accounting structure, then restore the earlier
  dashboard version.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q035

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q035
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a dashboard mixes a real-time tile and a batch-refreshed tile that both source accounting
  data on the same page, each is labeled with its own refresh mode so a viewer does not mistake the
  batch figure for real-time.
WHY_IT_MATTERS: >
  Mixing refresh modes on financial tiles with no visual distinction lets a viewer treat a stale batch
  figure as current.
DISCONFIRMING_OBSERVATION: >
  A dashboard mixes real-time and batch-refreshed accounting tiles on one page with no visual
  distinction between them.
EXPECTED_SURFACE: S5,S7
PRECONDITIONS: >
  Place a real-time and a batch-refreshed accounting tile on the same dashboard and inspect their
  visual labeling.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q036

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q036
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An accounting entry in a currency requiring a same-day exchange rate that is not yet available is
  either excluded from the dashboard total until a rate is set, or flagged, rather than silently
  treated as a zero or placeholder rate that distorts the total.
WHY_IT_MATTERS: >
  A missing-rate entry silently treated as zero can materially understate a multi-currency total with
  no visible cause.
DISCONFIRMING_OBSERVATION: >
  A dashboard total silently changes by an amount consistent with a missing exchange rate having been
  treated as zero or a placeholder value.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post a foreign-currency entry before its same-day rate is available and observe the dashboard
  total's behaviour.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q037

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q037
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Deleting a dashboard has no effect on the underlying accounting entries or accounts it aggregated.
WHY_IT_MATTERS: >
  A reporting layer able to alter the ledger it merely summarizes when removed would be an
  unacceptable coupling between reporting and financial records.
DISCONFIRMING_OBSERVATION: >
  Removing a dashboard has any observable effect on the underlying accounting records themselves.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Note the state of the underlying accounting data, delete the dashboard, and re-check the accounting
  data.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q038

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q038
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard's printed or exported version of an accounting figure preserves the same as-of date and
  currency-basis disclosures as the live on-screen view, rather than dropping that context only in
  the export path.
WHY_IT_MATTERS: >
  A printed financial report missing the same context as the live view can be circulated and relied
  on with no way to judge its currency or timing basis.
DISCONFIRMING_OBSERVATION: >
  Printing or exporting a dashboard drops the as-of or basis disclosure that the live view shows.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Compare a live accounting dashboard's disclosures to its printed or exported version.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q039

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q039
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard tile aggregating figures across multiple accounting periods correctly excludes a period
  from being treated as final once that period is reopened for adjustment, or flags the reopening.
WHY_IT_MATTERS: >
  A total that keeps treating a reopened period as closed hides the fact that part of the figure is
  still subject to change.
DISCONFIRMING_OBSERVATION: >
  Reopening a previously closed accounting period for correction produces no observable change or
  flag in a dashboard total that previously treated that period as final.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Reopen a previously closed accounting period referenced by a dashboard total and check for any
  change or flag.
LAYER: PROCESS
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q040

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q040
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Viewing a sensitive aggregated accounting figure through the dashboard leaves the same kind of
  access trace that direct access to the underlying accounting data would produce, rather than being
  effectively invisible to whatever audit trail governs direct account access.
WHY_IT_MATTERS: >
  A reporting path around the accounting system's own audit trail would let sensitive financial data
  be viewed with no record that it happened.
DISCONFIRMING_OBSERVATION: >
  Viewing a sensitive aggregated accounting figure through the dashboard leaves no trace in any access
  or audit log that direct access to the same data would have produced.
EXPECTED_SURFACE: S6,S4
PRECONDITIONS: >
  View a sensitive aggregated accounting figure through the dashboard and check whether any access
  log recorded it.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q041

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q041
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard combining an accounting figure with data from a different business domain reconciles
  the two on a shared transaction date or period rather than silently aligning them on whichever date
  each source happens to record independently.
WHY_IT_MATTERS: >
  A date-basis mismatch between combined domains can attribute an accounting figure to the wrong
  period relative to the other domain's data, producing a misleading combined view.
DISCONFIRMING_OBSERVATION: >
  A combined dashboard total misattributes an accounting figure to the wrong period relative to the
  other domain's data due to a date-basis mismatch.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Combine an accounting figure with data from a different domain near a period boundary and check
  which period each is attributed to.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q042

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q042
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard's aggregation of a high-volume accounting transaction set does not silently truncate or
  sample the underlying data without disclosing that the total is based on a partial read.
WHY_IT_MATTERS: >
  An undisclosed partial read of a large transaction volume produces a financial total that looks
  complete but is materially wrong.
DISCONFIRMING_OBSERVATION: >
  A dashboard total for a high-volume account set differs from a full direct query of the same
  accounting data, with no disclosure that only part of the data was read.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Build a dashboard total over a very large accounting transaction set and compare it to a full direct
  query over the same data.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q043

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q043
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A personal filter one viewer applies to an accounting dashboard tile does not persist into what is
  delivered to other recipients of a shared or scheduled distribution of the same dashboard.
WHY_IT_MATTERS: >
  A personal filter leaking into a scheduled distribution would silently change what other recipients
  receive without anyone configuring that change for them.
DISCONFIRMING_OBSERVATION: >
  A personal filter one viewer applied to an accounting dashboard tile appears in a scheduled
  distribution sent to other recipients who did not set that filter.
EXPECTED_SURFACE: S4,S8
PRECONDITIONS: >
  Apply a personal filter to an accounting tile as one viewer, then inspect a scheduled distribution
  sent to other recipients.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q044

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q044
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an account's display name, used purely for labeling on the dashboard, is renamed, a previously
  frozen point-in-time dashboard snapshot retains the label as it was at the time of that snapshot
  rather than being silently relabeled after the fact.
WHY_IT_MATTERS: >
  A frozen snapshot that silently adopts a later renamed label misrepresents what the report actually
  looked like at the time it was produced.
DISCONFIRMING_OBSERVATION: >
  A previously frozen point-in-time dashboard snapshot displays an account's current name rather than
  the name it had when the snapshot was taken.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Take a frozen dashboard snapshot referencing an account, rename that account, then reopen the
  snapshot.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q045

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q045
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard tile that fails to resolve an accounting figure, for example due to a permission or
  connectivity issue at render time, displays an explicit error state distinguishable from a
  legitimate zero balance.
WHY_IT_MATTERS: >
  A failed lookup indistinguishable from a real zero can be read as good financial news when it is
  actually a broken computation.
DISCONFIRMING_OBSERVATION: >
  A dashboard tile displays a zero for an accounting figure it actually failed to retrieve,
  indistinguishable from a real zero balance.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Force a resolution failure on an accounting tile at render time and inspect what value it displays.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q046

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q046
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Switching the active company within the dashboard interface fully re-scopes any cached accounting
  aggregation, so a tile does not momentarily or persistently show figures computed under the
  previously active company.
WHY_IT_MATTERS: >
  A tile that briefly or persistently shows another company's cached financial figures after a company
  switch is a cross-tenant leak of accounting data.
DISCONFIRMING_OBSERVATION: >
  After switching the active company, a dashboard tile still displays a total that was computed under
  the previous company's accounting data.
EXPECTED_SURFACE: S4,S1
PRECONDITIONS: >
  View an accounting tile under one company, switch the active company, and immediately re-check the
  tile.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q047

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q047
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A shared dashboard link or embed referencing a specific accounting-derived tile does not silently
  escalate the recipient's effective access if the tile's own definition is later broadened to
  include more sensitive figures, beyond what that recipient's own permissions would otherwise allow.
WHY_IT_MATTERS: >
  A link that automatically inherits an expanded tile definition can grant a recipient visibility into
  more sensitive financial detail than was ever explicitly approved for them.
DISCONFIRMING_OBSERVATION: >
  A shared dashboard link continues to display expanded accounting detail to a recipient after the
  tile's definition is broadened, even though that recipient's own permissions were never elevated.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Share a dashboard link with a recipient, later broaden the referenced tile's definition to include
  more sensitive detail, and re-check what that recipient's link now shows.
```

## G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q048

```yaml
QID: G15-SPREADSHEET_DASHBOARD_ACCOUNT-Q048
MODULE: spreadsheet_dashboard_account
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an accounting period closes while a dashboard's scheduled refresh cycle for that period is
  still pending, the next completed refresh reflects the closed period's final figures rather than a
  refresh that was already in flight silently using pre-close data.
WHY_IT_MATTERS: >
  A refresh caught mid-flight at the moment of closing could publish a dashboard figure that never
  matches either the pre-close or the post-close state of the books.
DISCONFIRMING_OBSERVATION: >
  A dashboard refresh that was already running when a period closed completes and publishes a figure
  that matches neither the pre-close nor the post-close ledger state, with no flag that the refresh
  straddled the closing event.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a period close while a scheduled dashboard refresh for that period is already in progress,
  and inspect the resulting published figure against both the pre-close and post-close ledger.
LAYER: PROCESS
```
