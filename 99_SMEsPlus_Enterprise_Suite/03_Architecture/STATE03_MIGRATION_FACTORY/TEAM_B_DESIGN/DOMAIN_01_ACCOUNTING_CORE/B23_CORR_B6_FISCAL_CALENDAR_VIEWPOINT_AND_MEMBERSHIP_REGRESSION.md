# B23 — CORR-B6 Fiscal Calendar Viewpoint & Membership Regression

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-30-MIG-B-D01-CORR6-001 |
| Source of truth | CORR6-001 directive §CORR-B6-06 — 15 mandatory scenarios, tested against the CORR-B6-corrected design (B07 §1g corrected, §1i/§1j new; B08 MP-09/MP-12 Proofs D/G4 corrected; B04 `FiscalYearBoundaryChanged` scope corrected, `FiscalYearMembershipRestated` new; B05 BINV-17 new; B13 DT-13 new) |
| Personas | Senior Accountant, Financial Controller, External Auditor, Historical Reporting Reviewer, Fiscal Calendar Administrator, Migration Architect, SaaS Domain Architect, Accounting Systems Architect, Clean-room Reviewer |
| Result | **15/15 PASS. No in-round refinement required — every worked figure matched the corrected B07/B08 formulas on first computation, cross-checked against the running Company X figures established at B20/B21/B22.** |

Money amounts below are illustrative units, continuing exactly the Company X scenario carried
from B20/B21/B22 — not restarted. Per the directive's required schema, every test below
records: Inputs / Timeline / Query Date D / Knowledge Cutoff T / Calendar Version(s) / Version
Effective Date / Version Recorded At / Entry Effective Date / Entry Recorded At /
Membership_Known / Membership_Current / Elapsed_Known / Elapsed_Current / Raw Cumulative TB /
Fiscal-Year Activity / Reported RE / Reported Equity / Expected Result / Actual Result /
PASS-FAIL / Finding / Disposition.

## Company X — Running Balances (continued from B20/B21/B22; the Dec15/2024 Entry, already
## included in every prior round's FY2024 Revenue 400 total, is individually named for the
## first time this round; the April 2026 reclassification is a new, illustrative event)

```
(from B20/B21/B22) Baseline start FY2024 (Jan1 2024): Cash 1000, Direct RE 1000 (only account)
(from B20/B21/B22) FY2024: Revenue 400, Expense 150 -> CE 250. Elapsed Dec31/2024. Cash = 1250.
  Of FY2024's 400 Revenue, 60 is a single Entry dated Dec 15 2024 (Cash 60 / Revenue 60,
  Recorded Dec 15 2024) — always part of the 400 total every prior round used; named
  individually for the first time this round, as the specific illustrative Entry Tests 4-6, 9
  use.
(from B20/B21/B22) FY2025: Revenue 500, Expense 200 -> CE 300. Elapsed Dec31/2025. Cash = 1550.
(from B20/B21/B22) FY2026 Jan15: Revenue 50 (cash). Cash = 1600.
(from B20/B21/B22) FY2025 Restatement, March 1 2026: Expense +40 (Payable), Effective Dec 15
  2025, MATERIAL. FY2025 Current CE becomes 500 - 240 = 260 from March 2026 forward.
(from B22) FY2024's boundary: Version 1 = Jan1-Dec31 2024, Effective/Recorded 2023-12-01,
  relied upon by every prior round's testing.
(from B22) FY2025's boundary: Version 1 = Jan1-Dec31 2025, Effective/Recorded 2023-12-01.
(NEW, this document) April 2026: an authorized `FiscalYearMembershipRestated` action is
  exercised (Tests 3-9, 11 below) — FY2024 Version 2: End Date Nov30/2024 (was Dec31/2024);
  FY2025 Version 2: Start Date Dec1/2024 (was Jan1/2025) — a PAIRED change, both Fiscal Years'
  boundaries moved atomically in one action, per BINV-17/DT-13's no-gap requirement. Both
  versions Effective April 2026 forward for Current-viewpoint purposes; Recorded April 2026.
  The Dec15/2024 Entry's Current-viewpoint membership reclassifies from FY2024 to FY2025 in the
  SAME atomic action. FY2024 Current CE becomes (400-60)-150 = 190; FY2025 Current CE becomes
  (500+60)-(200+40) = 320. Total unchanged: 190+320 = 510 = 250+260.
(NEW, this document) FY2027: Version 1 = Jan1-Dec31 2027, Effective/Recorded 2023-12-01,
  zero reliance as of 2026 (Tests 2, 12 below).
```

## Test 1 — Known report before later calendar change: general principle (membership, Elapsed, P&L, Reported RE, Reported Equity all identical)

```
Inputs:                  Company X, D = Dec31/2024, T1 = Jan5/2025 (an ordinary report,
                         issued shortly after FY2024's own end, well before any Round-6
                         calendar change)
Timeline:                FY2024 Version 1 set 2023-12-01 -> FY2024 elapses Dec31/2024 ->
                         report issued/computed Jan5/2025 (T1) -> ... -> April 2026,
                         FiscalYearMembershipRestated creates FY2024/FY2025 Version 2 (Tests
                         3-9) -> Known(D,T1) re-run after all of that
Query Date D:            Dec 31 2024
Knowledge Cutoff T:      Jan 5 2025 (T1, fixed)
Calendar Version(s):     FY2024 Version 1 (only version Recorded by T1)
Version Effective Date:  2023-12-01 (Version 1's own)
Version Recorded At:     2023-12-01 (Version 1's own) — Version 2 (Recorded April 2026) is
                         excluded from this Known query by construction, since April 2026 > T1
Entry Effective Date:    every FY2024 Line's own Effective Date, unaffected by anything after T1
Entry Recorded At:       every FY2024 Line's own Recorded At, all <= T1 by construction (the
                         year had already elapsed and been queried by T1)
Membership_Known:        every FY2024 Entry (including the Dec15/2024 Entry) -> FY2024, under
                         FiscalYearDefinition_Known(X,FY2024,T1) = Version 1
Membership_Current:      n/a for this test (Known-only)
Elapsed_Known:           Elapsed_Known(FY2024, Dec31/2024, Jan5/2025) = TRUE (Version 1 End
                         Dec31/2024 <= Dec31/2024)
Elapsed_Current:         n/a for this test
Raw Cumulative TB:       1250 (Cash) = 1000 (Direct RE) + 250 (cumulative Revenue-Expense,
                         Proof G1) — unaffected by anything Fiscal-Year-related, per BINV-15
Fiscal-Year Activity:    FY2024 CE_Known(T1) = 400 - 150 = 250 (the Dec15/2024 Entry's 60 is
                         part of this 400, under Version 1, exactly as always)
Reported RE:             ReportedRetainedEarnings_Known(X, Dec31/2024, Jan5/2025) = 1000 + 250
                         = 1250
Reported Equity:         ReportedEquity_Known(X, Dec31/2024, Jan5/2025) = 0 (Other Ledger
                         Equity) + 1250 = 1250
Expected Result:         re-running this exact Known(D=Dec31/2024, T=Jan5/2025) query at ANY
                         later point — including after April 2026's FiscalYearMembershipRestated
                         — returns byte-for-byte identical membership, Elapsed, Fiscal-Year
                         Activity, Reported RE, and Reported Equity
Actual Result:           CONFIRMED — re-computed after April 2026's reclassification: Membership_Known
                         still FY2024 for the Dec15/2024 Entry, Elapsed_Known still TRUE under
                         Version 1, Reported RE_Known/Reported Equity_Known still exactly 1250,
                         all unchanged, per B07 §1i's Recorded-At-filtered fixed-point guarantee
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 2 — Current report after prospective-only future calendar change

```
Inputs:                  Company X, 2026: FY2027 (Jan1-Dec31 2027, Version 1, zero reliance)
                         is authorized to change to a different basis before it begins —
                         reusing the ordinary, lightweight `FiscalYearBoundaryChanged`
                         mechanism, since no reliance exists yet
Timeline:                FY2027 Version 1 set 2023-12-01 -> 2026, authorized
                         `FiscalYearBoundaryChanged` action changes FY2027 to Version 2
                         (Apr1/2027-Mar31/2028) -> Current report queried for dates spanning
                         FY2024-2027
Query Date D:            various — Dec31/2024 (FY2024, elapsed), Dec31/2025 (FY2025,
                         elapsed), and a date within FY2027 under either version
Knowledge Cutoff T:      n/a (Current)
Calendar Version(s):     FY2024 Version 2 (post-April-2026 reclassification, Tests 3-9);
                         FY2025 Version 2 (paired); FY2027 Version 2 (Apr-Mar basis)
Version Effective Date:  FY2027 Version 2: some 2026 date, before FY2027's own Jan1/2027 start
                         under either version
Version Recorded At:     2026 (before FY2027 begins under either version)
Entry Effective Date:    n/a directly (no new Entry introduced by this test)
Entry Recorded At:       n/a
Membership_Known:        n/a for this test (Current-only)
Membership_Current:      unaffected for FY2024/FY2025 Entries by the FY2027 change (disjoint
                         Fiscal Years, disjoint validation scope)
Elapsed_Known:           n/a
Elapsed_Current:         Elapsed_Current(FY2024, Dec31/2024) = TRUE (per Test 4/5's own
                         reclassified Version 2), completely independent of the FY2027 change
Raw Cumulative TB:       unaffected — the FY2027 change touches no COMMITTED Line's Effective
                         Date or membership
Fiscal-Year Activity:    FY2024/FY2025's own Current-viewpoint activity (190/320, per the
                         April-2026 reclassification) is byte-for-byte unaffected by the
                         FY2027 change; FY2027's own activity, once it begins, is bounded by
                         the NEW Apr-Mar basis
Reported RE:             ReportedRetainedEarnings_Current(X, Dec31/2025) = 1000 + 190 + 320 =
                         1510, identical before and after the FY2027 change
Reported Equity:         ReportedEquity_Current(X, Dec31/2025) = 1510, identical before and
                         after the FY2027 change
Expected Result:         only FY2027-onward is affected; every earlier Fiscal Year's Current-
                         viewpoint figures are completely undisturbed
Actual Result:           CONFIRMED — no change detected in any FY2024/FY2025 figure after the
                         FY2027 change is applied
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 3 — Current report after retroactive boundary change: mechanism-level (rejection via the ordinary mechanism; success only via the atomic mechanism)

```
Inputs:                  Company X, April 2026: two DIFFERENT attempts to change FY2024's End
                         Date from Dec31/2024 to Nov30/2024 are made — (a) via the ordinary
                         `FiscalYearBoundaryChanged` mechanism, (b) via the new, dedicated
                         `FiscalYearMembershipRestated` mechanism
Timeline:                FY2024 Version 1 relied upon since 2024 -> April 2026, both attempts
                         made
Query Date D:            n/a (evaluating the attempts themselves)
Knowledge Cutoff T:      n/a
Calendar Version(s):     FY2024 Version 1 at attempt time
Version Effective Date:  n/a for the refused attempt (a); April 2026 (Current-viewpoint) for
                         the accepted attempt (b)
Version Recorded At:     n/a for (a); April 2026 for (b)
Entry Effective Date:    n/a
Entry Recorded At:       n/a
Membership_Known:        n/a
Membership_Current:      unaffected by (a) (refused, no effect); reclassified per (b) — see
                         Tests 4/5 for the worked Entry-level detail
Elapsed_Known:           n/a
Elapsed_Current:         n/a directly to this mechanism-level test
Raw Cumulative TB:       n/a
Fiscal-Year Activity:    n/a
Reported RE:             n/a directly; the CONSEQUENCE of (a) succeeding silently would corrupt
                         every figure in Tests 1, 7-8, exactly the risk BINV-17 exists to close
Reported Equity:         n/a directly, same consequence-risk as above
Expected Equation:       per BINV-17/B07 §1j: (a) is REFUSED outright — `FiscalYearBoundaryChanged`
                         is constitutionally barred from reaching backward over reliance, full
                         stop, no "created but Entries frozen" middle state. (b) SUCCEEDS, but
                         only as one atomic action that ALSO reclassifies every affected Entry's
                         Current-viewpoint membership in the same step — never as two
                         independently-timed actions
Actual Result:           CONFIRMED — (a) refused, logged with actor/timestamp/the specific rule
                         that blocked it (B11 scenario 21, corrected); (b) accepted, logged as
                         one `FiscalYearMembershipRestated` event with scope (FY2024+FY2025 paired),
                         old/new boundary versions, reason, actor, Recorded At, Effective Date,
                         and every affected reporting period (B11 scenario 22) — at no point does
                         a new boundary version exist for FY2024 while the Dec15/2024 Entry's
                         Current-viewpoint membership still reads FY2024
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 4 — The exact Round-5 Test-12 scenario re-examined: December Entries under Known AND Current views, no hybrid ambiguity

```
Inputs:                  Company X, the exact B22 Test 12 scenario: FY2024 Version 1 =
                         Jan1-Dec31/2024; an attempt is made to change to Version 2 =
                         Jan1-Nov30/2024, AFTER heavy reliance (COMMITTED Entries throughout,
                         elapsed since Dec2024, referenced in every prior round's reports).
                         Re-examined here per the directive's explicit instruction, using the
                         Dec15/2024 Revenue-60 Entry as the concrete illustrative case
Timeline:                FY2024 Version 1 relied upon 2024-2026 -> April 2026, authorized
                         `FiscalYearMembershipRestated` action (Test 3(b)) -> queries both
                         before (T-fixed, Known) and after (Current) the action
Query Date D:            Dec31/2024 (FY2024's own original End Date)
Knowledge Cutoff T:      Jan1/2026 (Known, before the April-2026 action) — Current queries use
                         no T (evaluated after April 2026)
Calendar Version(s):     FY2024 Version 1 (Known, T=Jan1/2026) / FY2024 Version 2 + FY2025
                         Version 2, paired (Current, post-April-2026)
Version Effective Date:  Version 2: April 2026 (Current-viewpoint forward only)
Version Recorded At:     Version 2: April 2026
Entry Effective Date:    Dec 15 2024 (the illustrative Entry)
Entry Recorded At:       Dec 15 2024 (same-day, ordinary Entry — well before April 2026)
Membership_Known:        Membership_Known(Dec15/2024 Entry, T=Jan1/2026) = FY2024, under
                         Version 1
Membership_Current:      Membership_Current(Dec15/2024 Entry), post-April-2026 =
                         FY2025 — explicitly reclassified by the `FiscalYearMembershipRestated`
                         event, atomically with the boundary change itself
Elapsed_Known:           Elapsed_Known(FY2024, Dec31/2024, Jan1/2026) = TRUE (Version 1 End
                         Dec31/2024 <= Dec31/2024)
Elapsed_Current:         Elapsed_Current(FY2024, Dec31/2024), post-April-2026 = TRUE (Version 2
                         End Nov30/2024 <= Dec31/2024) — both TRUE at this specific D, but via
                         DIFFERENT boundary versions (see Test 6 for a D where they diverge)
Raw Cumulative TB:       1250 = 1250 (Proof G1), IDENTICAL before and after — no COMMITTED
                         Line's existence, amount, or Effective Date changed; only the Dec15/2024
                         Entry's Fiscal-Year MEMBERSHIP (a reporting-time classification, not a
                         ledger fact) changed under Current viewpoint
Fiscal-Year Activity:    Known(T=Jan1/2026): FY2024 CE = 400-150 = 250 (Dec15 Entry counted in
                         FY2024). Current (post-April-2026): FY2024 CE = (400-60)-150 = 190,
                         FY2025 CE = (500+60)-(200+40) = 320 (Dec15 Entry counted in FY2025,
                         exactly once, never in both)
Reported RE:             Known(T=Jan1/2026, D=Dec31/2024) = 1000+250 = 1250, UNCHANGED by the
                         later action. Current (post-April-2026, D=Dec31/2024) = 1000+190 =
                         1190 — Elapsed_Current(FY2025,Dec31/2024)=FALSE (FY2025's End Dec31/2025
                         > Dec31/2024), so FY2025's 320 is not yet included at this query date
Reported Equity:         Known = 1250 (unchanged); Current (D=Dec31/2024) = 1190
Expected Result:         no hybrid ambiguity allowed — Known and Current each produce ONE
                         internally coherent figure, each drawn from a single, consistent
                         viewpoint throughout (never "historical facts @ T + current calendar @
                         now"); the two figures (1250 vs. 1190) are legitimately different
                         BECAUSE they are different viewpoints, not because either mixes facts
                         and calendars inconsistently
Actual Result:           CONFIRMED — 1250 (Known, permanently reproducible) and 1190 (Current,
                         post-reclassification), each internally consistent, each independently
                         reconstructable and labeled (CO-14, extended)
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 5 — December 15/2024 Entry: authoritative Fiscal-Year membership before and after the calendar-change process

```
Inputs:                  Company X, the Dec15/2024 Revenue-60 Entry, exactly at the affected
                         boundary (between the old Dec31 End and the new Nov30 End)
Timeline:                Entry Recorded/Effective Dec15/2024 -> April 2026,
                         FiscalYearMembershipRestated action
Query Date D:            n/a (querying membership, not a balance)
Knowledge Cutoff T:      Jan1/2026 (Known) / n/a (Current, post-April-2026)
Calendar Version(s):     FY2024 Version 1 (Known) / FY2024+FY2025 Version 2, paired (Current)
Version Effective Date:  Version 2: April 2026
Version Recorded At:     Version 2: April 2026
Entry Effective Date:    Dec 15 2024
Entry Recorded At:       Dec 15 2024
Membership_Known:        FY2024 (T=Jan1/2026, under Version 1 — Dec15/2024 falls within
                         Jan1-Dec31/2024)
Membership_Current:      FY2025 (post-April-2026, under Version 2 — Dec15/2024 falls within
                         FY2025's new Dec1/2024-Dec31/2025 span, since FY2024's own span
                         shrank to Jan1-Nov30/2024)
Elapsed_Known:           n/a directly (membership test)
Elapsed_Current:         n/a directly (membership test)
Raw Cumulative TB:       n/a
Fiscal-Year Activity:    n/a directly (see Test 4 for the resulting activity figures)
Reported RE:             n/a directly (see Test 4)
Reported Equity:         n/a directly (see Test 4)
Expected Result:         exactly one authoritative membership per viewpoint — never both FY2024
                         and FY2025 simultaneously interpretable as this Entry's home under one
                         viewpoint
Actual Result:           CONFIRMED — FY2024 under Known(T=Jan1/2026), FY2025 under Current
                         (post-April-2026), each a single, unambiguous answer; both remain
                         independently reconstructable and explicitly labeled, satisfying
                         CORR-B6-03's acceptance criterion directly
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 6 — Elapsed_Known vs. Elapsed_Current for the same historical D/T after later boundary versioning

```
Inputs:                  Company X, D = Dec15/2024 (deliberately chosen inside the gap between
                         the old Dec31 End and the new Nov30 End)
Timeline:                FY2024 Version 1 relied upon -> April 2026, FiscalYearMembershipRestated
                         action (FY2024 End -> Nov30/2024)
Query Date D:            Dec 15 2024
Knowledge Cutoff T:      Jan 1 2026 (Known)
Calendar Version(s):     FY2024 Version 1 (Known, T=Jan1/2026) / FY2024 Version 2 (Current,
                         post-April-2026)
Version Effective Date:  Version 2: April 2026
Version Recorded At:     Version 2: April 2026
Entry Effective Date:    n/a (boundary test, not an Entry test)
Entry Recorded At:       n/a
Membership_Known:        n/a directly (Elapsed test)
Membership_Current:      n/a directly (Elapsed test)
Elapsed_Known:           Elapsed_Known(FY2024, Dec15/2024, Jan1/2026) = FALSE — Version 1's own
                         End Date (Dec31/2024) is NOT <= Dec15/2024
Elapsed_Current:         Elapsed_Current(FY2024, Dec15/2024), post-April-2026 = TRUE — Version
                         2's own End Date (Nov30/2024) IS <= Dec15/2024
Raw Cumulative TB:       n/a
Fiscal-Year Activity:    n/a directly (see Test 4)
Reported RE:             n/a directly (see Test 4)
Reported Equity:         n/a directly (see Test 4)
Expected Result:         Known uses the historical calendar version authoritative at T (Version
                         1); Current uses the authorized current semantics (Version 2) — the two
                         are legitimately, provably different for this specific D, demonstrating
                         `Elapsed_*` is genuinely viewpoint-parameterized, closing `M-AUD-13`
                         directly rather than by assertion
Actual Result:           CONFIRMED — FALSE (Known) vs. TRUE (Current), exactly as B07 §1i
                         predicts; re-verified that Elapsed_Known(FY2024,Dec15/2024,Jan1/2026)
                         remains FALSE even when re-queried after April 2026 (T is fixed, the
                         later version is Recorded after T and is therefore excluded — the
                         fixed-point guarantee holds)
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 7 — Reported RE Known after later calendar change must remain identical to the originally-issued result

```
Inputs:                  Company X, D = Dec31/2025, T = Jan1/2026 (a report computed just
                         before the March-2026 ordinary Restatement AND well before the
                         April-2026 FiscalYearMembershipRestated action)
Timeline:                FY2024/FY2025 Version 1 relied upon -> report computed Jan1/2026 (T)
                         -> March 2026, ordinary Restatement (+40 Expense, ineligible for this
                         T since Recorded after it) -> April 2026, FiscalYearMembershipRestated
                         -> Known(D,T) re-run after both later events
Query Date D:            Dec 31 2025
Knowledge Cutoff T:      Jan 1 2026
Calendar Version(s):     FY2024/FY2025 Version 1 (only versions Recorded by T)
Version Effective Date:  2023-12-01 (both, their own)
Version Recorded At:     2023-12-01 (both, their own)
Entry Effective Date:    every FY2024/FY2025 Line's own, as Recorded by Jan1/2026
Entry Recorded At:       all <= Jan1/2026 by construction
Membership_Known:        FY2024's Entries (incl. Dec15/2024) -> FY2024; FY2025's Entries ->
                         FY2025, both under Version 1
Membership_Current:      n/a for this test (Known-only)
Elapsed_Known:           Elapsed_Known(FY2024,Dec31/2025,Jan1/2026)=TRUE;
                         Elapsed_Known(FY2025,Dec31/2025,Jan1/2026)=TRUE (Version 1 End
                         Dec31/2025 <= Dec31/2025)
Elapsed_Current:         n/a for this test
Raw Cumulative TB:       1550 = 1550 (Proof G1, cumulative through Dec31/2025, pre-March-2026
                         Restatement)
Fiscal-Year Activity:    FY2024 CE_Known(T) = 250; FY2025 CE_Known(T) = 500-200 = 300 (the
                         +40 Restatement is not yet Recorded as of T)
Reported RE:             ReportedRetainedEarnings_Known(X,Dec31/2025,Jan1/2026) = 1000+250+300
                         = 1550
Reported Equity:         ReportedEquity_Known(X,Dec31/2025,Jan1/2026) = 1550
Expected Result:         re-running this exact Known(D=Dec31/2025,T=Jan1/2026) query after BOTH
                         the March-2026 Restatement AND the April-2026 FiscalYearMembershipRestated
                         returns byte-for-byte 1550, unchanged by either later event
Actual Result:           CONFIRMED — 1550, unchanged, re-computed after both later events;
                         neither a later ordinary Restatement nor a later Fiscal-Year membership
                         reclassification can alter an already-fixed Known-viewpoint result,
                         per B07 §1i/§1j's structural (Recorded-At-filtered) guarantee
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 8 — Reported RE Current after a legitimate historical calendar Restatement reflects the approved reclassification consistently

```
Inputs:                  Company X, D = Dec31/2024, evaluated Current-viewpoint AFTER the
                         April-2026 FiscalYearMembershipRestated action
Timeline:                (as Test 4) -> April 2026, action applied -> Current query, any time
                         after April 2026
Query Date D:            Dec 31 2024
Knowledge Cutoff T:      n/a (Current)
Calendar Version(s):     FY2024 Version 2 (End Nov30/2024), FY2025 Version 2 (Start Dec1/2024)
Version Effective Date:  April 2026 (both)
Version Recorded At:     April 2026 (both)
Entry Effective Date:    n/a directly (see Test 5 for the Dec15/2024 Entry specifically)
Entry Recorded At:       n/a directly
Membership_Known:        n/a for this test (Current-only)
Membership_Current:      the Dec15/2024 Entry -> FY2025 (Test 5)
Elapsed_Known:           n/a
Elapsed_Current:         Elapsed_Current(FY2024,Dec31/2024)=TRUE (Nov30<=Dec31);
                         Elapsed_Current(FY2025,Dec31/2024)=FALSE (Dec31/2025 End > Dec31/2024)
Raw Cumulative TB:       1250 = 1250 (Proof G1, unaffected — same ledger facts, same amounts)
Fiscal-Year Activity:    FY2024 Current CE = 190 (elapsed, included); FY2025 Current CE = 320
                         (not yet elapsed as of this D, excluded)
Reported RE:             ReportedRetainedEarnings_Current(X,Dec31/2024) = 1000+190 = 1190
Reported Equity:         ReportedEquity_Current(X,Dec31/2024) = 1190
Expected Result:         the approved reclassification is reflected consistently — every
                         constituent term (membership, Elapsed, Fiscal-Year Activity) uses the
                         SAME Current viewpoint throughout, re-derivable from Proof B/C's general
                         derivation applied under the reclassified boundary, not an ad hoc figure
Actual Result:           CONFIRMED — 1190, consistent with Test 4's own derivation and with
                         Test 11's G3 bridge cross-check (below)
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 9 — Current-FY P&L after a calendar version transition: Revenue/Expense membership has one authoritative answer

```
Inputs:                  Company X, the Dec15/2024 Revenue-60 Entry, queried via
                         FiscalYearActivity_Current for BOTH FY2024 and FY2025 after the
                         April-2026 reclassification
Timeline:                (as Test 4) -> April 2026, action applied
Query Date D:            Dec 31 2024 (for FY2024's own activity) and Dec 31 2025 (for FY2025's)
Knowledge Cutoff T:      n/a (Current)
Calendar Version(s):     FY2024 Version 2 (End Nov30/2024), FY2025 Version 2 (Start Dec1/2024)
Version Effective Date:  April 2026 (both)
Version Recorded At:     April 2026 (both)
Entry Effective Date:    Dec 15 2024
Entry Recorded At:       Dec 15 2024
Membership_Known:        n/a for this test (Current-only)
Membership_Current:      FY2025 (single, unambiguous — Test 5)
Elapsed_Known:           n/a
Elapsed_Current:         Elapsed_Current(FY2024,Dec31/2024)=TRUE; Elapsed_Current(FY2025,Dec31/2025)=TRUE
Raw Cumulative TB:       n/a directly (see Test 3/4)
Fiscal-Year Activity:    FiscalYearActivity_Current(Revenue,X,FY2024-bounded) = 340 (400-60,
                         the Dec15 Entry EXCLUDED); FiscalYearActivity_Current(Revenue,X,
                         FY2025-bounded) = 560 (500+60, the Dec15 Entry INCLUDED) — the 60
                         appears in exactly ONE of the two computations, never both, never
                         neither
Reported RE:             n/a directly (see Test 4/8 for the resulting Reported RE)
Reported Equity:         n/a directly (see Test 4/8)
Expected Result:         Revenue/Expense membership has one authoritative answer — no
                         computation path in this design attributes the Dec15/2024 Entry's
                         Revenue to both Fiscal Years, or to neither, under Current viewpoint
Actual Result:           CONFIRMED BY CONSTRUCTION — `FiscalYearActivity_Current` sums Lines
                         with Effective Date within `[FiscalYearStart_Current(C,D), D]` for the
                         Fiscal Year containing D; since FY2024 and FY2025's Current-viewpoint
                         spans are non-overlapping and gap-free by construction (BINV-17's
                         no-overlap/no-gap check, validated before the reclassification was
                         accepted), the Dec15/2024 Entry resolves to exactly one bucket for any
                         D queried
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 10 — Raw cumulative TB remains ledger-fact-driven and balanced, independent of Fiscal-Year version changes

```
Inputs:                  Company X, D = Dec31/2024, Raw Cumulative Trial Balance (Proof G1),
                         compared before and after the April-2026 FiscalYearMembershipRestated
                         action
Timeline:                (as Test 4) -> April 2026, action applied
Query Date D:            Dec 31 2024
Knowledge Cutoff T:      n/a (Current, both before and after)
Calendar Version(s):     FY2024 Version 1 (before) / Version 2 (after) — Raw Cumulative TB does
                         not consult Fiscal Year boundaries at all (MP-09, `CumulativeAccountBalance`)
Version Effective Date:  n/a to this computation
Version Recorded At:     n/a to this computation
Entry Effective Date:    n/a directly (all Lines' own, unaffected)
Entry Recorded At:       n/a directly (all Lines' own, unaffected)
Membership_Known:        n/a to this computation
Membership_Current:      n/a to this computation — `CumulativeAccountBalance` is category-wide,
                         all-time, with no Fiscal-Year partitioning at all (CORR-B5-02)
Elapsed_Known:           n/a
Elapsed_Current:         n/a
Raw Cumulative TB:       1250 (Cash, debit) = 1000 (Direct RE) + 250 (cumulative net
                         Revenue-Expense) — IDENTICAL before and after the reclassification
Fiscal-Year Activity:    n/a to this test (see Test 9 for the FY-partitioned figures, which DO
                         change)
Reported RE:             n/a directly
Reported Equity:         n/a directly
Expected Result:         the Raw Cumulative Trial Balance (G1) is ledger-fact-driven only — it
                         must remain byte-for-byte balanced and unchanged by any Fiscal-Year
                         version change, since no COMMITTED Line's existence, amount, Account, or
                         Effective Date was touched by the reclassification (only a reporting-time
                         classification changed)
Actual Result:           CONFIRMED — 1250 = 1250, identical before and after, exactly as BINV-15
                         requires; only Proof G2's mixed reporting view and Proof G3's derived
                         bridge (Test 11) reflect the reclassification, never G1 itself
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 11 — Balanced Presentation TB after a calendar Restatement: derived bridge and Reported Equity use the same Current viewpoint and balance

```
Inputs:                  Company X, D = Dec31/2024, Balanced Presentation Trial Balance (Proof
                         G3), evaluated Current-viewpoint after the April-2026 reclassification
Timeline:                (as Test 4/8) -> April 2026, action applied
Query Date D:            Dec 31 2024
Knowledge Cutoff T:      n/a (Current)
Calendar Version(s):     FY2024 Version 2 (End Nov30/2024), FY2025 Version 2 (Start Dec1/2024)
Version Effective Date:  April 2026
Version Recorded At:     April 2026
Entry Effective Date:    n/a directly (aggregate test)
Entry Recorded At:       n/a directly
Membership_Known:        n/a for this test (Current-only)
Membership_Current:      as Test 9 — Dec15/2024 Entry -> FY2025
Elapsed_Known:           n/a
Elapsed_Current:         Elapsed_Current(FY2024,Dec31/2024)=TRUE (only FY2024 has elapsed by
                         this D, under the reclassified boundary — Dec31/2024 itself is now
                         inside FY2025's own in-progress span, since FY2025 Current Start is
                         Dec1/2024)
Raw Cumulative TB:       1250 = 1250 (Proof G1, Test 10, unaffected)
Fiscal-Year Activity:    G2's mixed reporting-balance set at D=Dec31/2024 (Current,
                         post-reclassification): Cash cumulative 1250; FY2025 (the Fiscal Year
                         "in progress" at this D, under the new boundary) in-progress Revenue =
                         60 (only the Dec15/2024 Entry has occurred within FY2025's new span so
                         far), Expense = 0
Reported RE:             1190 (Test 8, cross-referenced, not re-derived)
Reported Equity:         1190 (Test 8, cross-referenced, not re-derived)
Expected Equation:       G2's mixed-horizon set: debit 1250(Assets)+0(FY2025 Expense-in-progress)
                         = 1250; credit 1000(direct RE)+60(FY2025 Revenue-in-progress) = 1060 —
                         imbalance of exactly 190, FY2024's OWN elapsed CE under the reclassified
                         boundary. G3's derived bridge = "Accumulated Elapsed-FY earnings" = 190
                         (only FY2024 has elapsed by this D). G3 balanced: 1250 = 1060+190 = 1250
Actual Design Equation:  1250 = 1250, confirmed; the bridge line (190) is IDENTICAL to Test 8's
                         Reported RE second summand (the FY2024 elapsed-CE term), reused not
                         duplicated, exactly as MP-12 Proof G3 requires
Expected Result:         the derived bridge and the separately-computed Reported Equity figure
                         both draw from the SAME Current-viewpoint boundary/membership — G3
                         balances, and its bridge figure matches Reported RE's own elapsed-CE
                         term exactly, confirming no divergence between the two computations
Actual Result:           CONFIRMED — G3 balances at 1250=1250; bridge (190) matches Test 8's
                         Reported RE elapsed-CE component exactly
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 12 — Future version with zero reliance: change next Fiscal Year before any Entry/report relies on it; verify clean transition

```
Inputs:                  Company X, 2026: FY2027 (Jan1-Dec31 2027, Version 1) has zero
                         reliance — no COMMITTED Entry, not yet elapsed, no issued/consumed
                         report references it — changed to Version 2 (Apr1/2027-Mar31/2028)
Timeline:                FY2027 Version 1 set 2023-12-01, alongside FY2024-2026 -> 2026,
                         `FiscalYearBoundaryChanged` action (ordinary, lightweight — zero
                         reliance) changes FY2027 to Version 2, before FY2027 begins under
                         either version
Query Date D:            n/a (evaluating the transition itself)
Knowledge Cutoff T:      n/a
Calendar Version(s):     FY2027 Version 1 -> Version 2
Version Effective Date:  a 2026 date, before Jan1/2027 (either version's own start)
Version Recorded At:     2026
Entry Effective Date:    n/a — no Entry exists in FY2027 at change time
Entry Recorded At:       n/a
Membership_Known:        n/a
Membership_Current:      n/a — no Entry to reclassify (zero reliance means nothing to move)
Elapsed_Known:           n/a
Elapsed_Current:         Elapsed_Current(FY2027, D) for any D before either version's own End
                         Date = FALSE, under either version — the change does not affect
                         Elapsed determination for prior Fiscal Years at all
Raw Cumulative TB:       unaffected — no COMMITTED Line exists in the affected span
Fiscal-Year Activity:    n/a — no activity exists yet to be bounded either way
Reported RE:             unaffected for any D within FY2024-2026 (Tests 1-11's figures hold
                         exactly)
Reported Equity:         unaffected for any D within FY2024-2026
Expected Result:         a genuinely future, not-yet-relied-upon Fiscal Year's boundary may be
                         changed freely (using either the lightweight pre-reliance path or, as
                         chosen here, the full `FiscalYearBoundaryChanged` authorized/audited
                         path even though a lighter update would also have been valid) without
                         requiring `FiscalYearMembershipRestated` at all — there is nothing to
                         reclassify
Actual Result:           CONFIRMED — clean transition, validated for no-overlap/no-gap against
                         FY2026's own End Date (Dec31/2026) before acceptance (BINV-17), no
                         Entry-membership question arises since none exists yet
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 13 — Overlapping proposed versions: rejected before activation

```
Inputs:                  Company X, an attempt to set FY2027's boundary to
                         Oct1/2027-Sep30/2028 while FY2026 remains Jan1-Dec31/2026 — creating
                         an overlap (Oct1/2027-Dec31/2027 would be claimed by neither
                         exclusively, and Jan1/2028-Sep30/2028 would double-claim against a
                         hypothetical FY2028) — more directly: an attempt to set FY2027 to
                         Nov1/2026-Oct31/2027, which overlaps FY2026's own Nov-Dec/2026 span
Timeline:                FY2026 Version 1 (Jan1-Dec31/2026) already governs 2026's activity ->
                         2026, a proposed FY2027 Version (Nov1/2026-Oct31/2027) is submitted
Query Date D:            n/a (validation-before-activation test)
Knowledge Cutoff T:      n/a
Calendar Version(s):     FY2026 Version 1 (existing); proposed FY2027 Version (rejected, never
                         becomes a version at all)
Version Effective Date:  the proposal's own claimed Nov1/2026 (never accepted)
Version Recorded At:     n/a — rejected before being Recorded as an authoritative version
Entry Effective Date:    n/a
Entry Recorded At:       n/a
Membership_Known:        n/a
Membership_Current:      n/a — nothing changes, since the proposal never activates
Elapsed_Known:           n/a
Elapsed_Current:         n/a
Raw Cumulative TB:       unaffected — no version is ever accepted
Fiscal-Year Activity:    unaffected
Reported RE:             unaffected
Reported Equity:         unaffected
Expected Result:         per BINV-17's no-overlap requirement, the proposal is validated against
                         the FULL resulting set of Company X's Current-viewpoint Fiscal Year
                         boundaries (including FY2026's existing Nov1-Dec31/2026 span) BEFORE
                         acceptance — the overlap is detected and the proposal is rejected,
                         never accepted and reconciled after the fact
Actual Result:           CONFIRMED — rejected pre-activation, with the specific overlapping date
                         range identified in the refusal (B11 scenario 22(b))
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 14 — Gap between Fiscal Years: rejected before activation

```
Inputs:                  Company X, an attempt to set FY2027's boundary to Feb1/2027-Dec31/2027
                         while FY2026 remains Jan1-Dec31/2026 — creating an uncovered gap,
                         Jan1/2027-Jan31/2027, that would belong to no Fiscal Year at all
Timeline:                FY2026 Version 1 in force -> 2026, the proposed FY2027 Version
                         (Feb1/2027-Dec31/2027) is submitted
Query Date D:            n/a (validation-before-activation test)
Knowledge Cutoff T:      n/a
Calendar Version(s):     FY2026 Version 1 (existing); proposed FY2027 Version (rejected)
Version Effective Date:  the proposal's own claimed Feb1/2027 (never accepted)
Version Recorded At:     n/a — rejected before being Recorded
Entry Effective Date:    n/a
Entry Recorded At:       n/a
Membership_Known:        n/a
Membership_Current:      n/a
Elapsed_Known:           n/a
Elapsed_Current:         n/a
Raw Cumulative TB:       unaffected
Fiscal-Year Activity:    unaffected — but if accepted, any Line dated Jan1-Jan31/2027 would
                         have no `FiscalYearActivity` home at all, an undefined state MP-09
                         itself cannot resolve
Reported RE:             unaffected
Reported Equity:         unaffected
Expected Result:         per BINV-17's no-coverage-gap requirement (derived directly from MP-09's
                         own need for every Revenue/Expense Line to resolve to exactly one Fiscal
                         Year's activity, not an invented regulatory mandate), the proposal is
                         rejected before activation — this domain's own business does require
                         continuous coverage, since MP-09 has no defined behavior for a Line
                         dated into an uncovered gap
Actual Result:           CONFIRMED — rejected pre-activation, with the specific uncovered date
                         range identified in the refusal (B11 scenario 22(b))
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 15 — Multi-company calendar isolation

```
Inputs:                  Company X (Tests 3-14's reclassifications and rejected proposals) and
                         Company W (B22 Test 10's Reported Equity of 1850) coexist under one
                         SMEsPlus tenant
Timeline:                concurrent with Tests 3-14
Query Date D:            Jan 1 2025 (Company W's own B22 Test 10 query point)
Knowledge Cutoff T:      n/a
Calendar Version(s):     Company X's FY2024/FY2025 Version 2 (Tests 4-11) and FY2027's Version
                         2 (Test 12) are entirely Company X's own facts; Company W's FY2024
                         remains its own, separate, Version 1, entirely untouched
Version Effective Date:  Company W's FY2024 Version 1: unchanged since original setup
Version Recorded At:     Company W's FY2024 Version 1: unchanged since original setup
Entry Effective Date:    Company W's own Entries, unaffected
Entry Recorded At:       Company W's own Entries, unaffected
Membership_Known:        Company W's own Entries' membership, unaffected by anything done to
                         Company X's calendar
Membership_Current:      Company W's own Entries' membership, unaffected
Elapsed_Known:           n/a directly (see Reported Equity below)
Elapsed_Current:         n/a directly
Raw Cumulative TB:       Company W's own (B22 Test 10: 2000=2000), unaffected
Fiscal-Year Activity:    Company W's own, unaffected
Reported RE:             Company W's own, unaffected
Reported Equity:         Company W's Reported Equity = 1850, re-checked after Company X's Tests
                         3-14 (both the successful FiscalYearMembershipRestated action and the
                         two rejected overlap/gap proposals) — MUST remain exactly 1850
Expected Result:         B07 §1i/§1j's viewpoint/membership model is defined per-Company (Fiscal
                         Year is already identified by "its Company and the span it covers," B07
                         §1); no step in `FiscalYearMembershipRestated`, `Membership_Known/Current`,
                         or the no-overlap/no-gap validation aggregates or compares across
                         Companies
Actual Result:           CONFIRMED BY CONSTRUCTION — Company W Reported Equity = 1850, identical
                         to B22 Test 10's own figure, checked after every one of Company X's
                         Round-6 calendar operations; every Fiscal Year definition, Version, and
                         `FiscalYearMembershipRestated`/`FiscalYearBoundaryChanged` event carries
                         an explicit Company reference (mirroring BINV-03), and the no-overlap/
                         no-gap validation is itself scoped per-Company — Company W's own
                         boundary set is never consulted when validating a Company X proposal,
                         or vice versa
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Regression Result

```
CONFIRMED PASS — 15/15 scenarios, no in-round refinement required
No regression into any of the twelve defects the five prior audits already found and fixed
No regression into any of the six defects B16's original red-team found and fixed
No new CRITICAL/HIGH defect
`M-AUD-13` closed: Elapsed/FiscalYearDefinition are genuinely viewpoint-parameterized (Tests 1,
  6, 7) — a Known-viewpoint report is provably unaffected by any later calendar change, of
  either kind (`FiscalYearBoundaryChanged` or `FiscalYearMembershipRestated`)
`M-AUD-14` closed: no hybrid boundary-version/Entry-membership state is ever reachable (Test 3);
  a genuine post-reliance reclassification is atomic (Tests 4, 5, 8, 9, 11); the cardinality/
  identity invariant holds per-viewpoint, with no-overlap and no-coverage-gap enforced before
  activation (Tests 13, 14); multi-company isolation holds throughout (Test 15)
```
