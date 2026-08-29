# B20 — CORR-B3 Accounting-Standard Corrective Regression

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-29-MIG-B-D01-CORR3-001 |
| Source of truth | Directive §11 — 15 mandatory scenarios, tested against the CORR-B3-corrected design (B04 §3b/§3c, B07 §1e, B08 MP-11 rewritten, B05 BINV-13, B09 CO-16) |
| Personas | Senior Accountant, Thai CPA/Accounting Standards Reviewer, Financial Controller, External Auditor, Fiscal-Year Close Operator, Historical Reporting Reviewer, Migration Architect, SaaS Domain Architect, Clean-room Reviewer |
| Accounting standard evidence | IAS 8 *Accounting Policies, Changes in Accounting Estimates and Errors* — read at primary-source level (PDF text, paras 1-54), not from memory or secondary summary. TAS 8 confirmed only via secondary sources as "substantively aligned" — this confidence asymmetry is preserved throughout, per B14's provenance discipline, and is never silently upgraded to primary-source confidence. |
| Result | **15/15 PASS. One design refinement found and applied while constructing Tests 4/5 (see Finding, Test 4) — not glossed over.** |

Money amounts below are illustrative units, chosen for arithmetic clarity, not a specific
currency. Tests 9-12 and 14 share one continuing worked scenario ("Company X"), built up
figure by figure so every later test's opening position is exactly the prior test's closing
position, not a fresh assumption — the same discipline B19 used for its Tests 9-11. Tests 3
and 13 use their own smaller, self-contained figures where a shared scenario would obscure
rather than clarify the specific point under test. "Recorded At" is abbreviated to the day for
readability; the actual guarantee (BINV-12) is instant-level.

## Company X — Running Balances (reference table, updated as tests proceed)

```
Baseline (post-migration, start of FY2024): Cash 1000 (Asset) ; Reported Retained Earnings
  1000 (all direct-posted, no Fiscal Year closed yet)
FY2024 (Jan1-Dec31 2024): Revenue 400 (cash), Expense 150 (cash) -> Current Earnings 250
  -> Fiscal Year Close declared at year end (no Entry). Cash = 1000+400-150 = 1250.
  Reported RE (from Jan1 2025) = 1000 (direct) + 250 (FY2024, closed) = 1250.
FY2025 (Jan1-Dec31 2025): Revenue 500 (cash), Expense 200 (cash) -> Current Earnings 300
  -> Fiscal Year Close declared at year end (no Entry). Cash = 1250+500-200 = 1550.
  Reported RE (from Jan1 2026) = 1000 (direct) + 250 (FY2024) + 300 (FY2025) = 1550.
FY2026 (Jan1 2026 onward, in progress): Jan15 2026, Revenue 50 (cash). Cash = 1550+50 = 1600.
```

## Test 1 — Current-period error (not a Prior-Period Error at all)

```
Inputs:                 Jan 15 2026 (FY2026, open, unreported): a Revenue Entry is posted
                        for 50 but should have been 55 — a data-entry mistake noticed the
                        same week, before FY2026's figures have ever been externally reported
Accounting Classification: NOT a Prior-Period Error. IAS 8 para 5 defines a prior period error
                        as a misstatement in financial statements "for one or more prior
                        periods" — this error is in the CURRENT, still-open, not-yet-reported
                        period. B04 §3b's decision tree routes this to its first branch
                        (Current-Period Error) before the Material/Immaterial question is
                        even reached, because that question is defined (IAS 8 para 5) only
                        for prior-period errors.
Materiality Status:     Not applicable — materiality (CO-16) is only evaluated once an item
                        clears the Prior-Period-Error classification gate; this item never
                        reaches that gate.
Timeline:               error made Jan 15 2026 -> noticed and corrected Jan 20 2026, same
                        still-open period
Effective Date:         Jan 20 2026 (an ordinary correction, current-dated) or Jan 15 2026
                        (an ordinary Amendment, since FY2026/January is open and the Entry is
                        unconsumed) — either is permitted; both are B04 §3b/§4 mechanics, not
                        §3c's restatement mechanics
Recorded At:            Jan 20 2026 (whichever mechanism is used)
Original Report View:   n/a — nothing was ever externally reported with the wrong figure
Restated Report View:   n/a — "restatement" is not the applicable concept here at all
Current-Period P&L Effect: the CORRECT figure (55) is what FY2026's P&L reflects once
                        corrected — there is no "current-period effect of a prior-period
                        correction" because there is no prior-period correction
Equity-Retained Earnings Effect: none — FY2026 has not closed, so nothing has reached
                        Reported Retained Earnings yet either way
Standard Principle Tested: IAS 8 para 5's definition of "prior period errors" — confirming
                        this domain's classification tree does not over-apply restatement
                        machinery to an error that IAS 8 itself would never call one
Expected Result:        ordinary Amendment or Correction, B04 §3b/§4/§5, no restatement
                        machinery invoked
Actual Design Result:   CONFIRMED — B04 §3b's decision tree's first test ("is the affected
                        period already closed/reported, or still open and unreported?")
                        correctly exits before reaching the Material/Immaterial branch
PASS / FAIL:            PASS
Finding:                none
Disposition:            n/a
```

## Test 2 — Material prior-period error discovered next year (classification)

```
Inputs:                 March 1 2026 (FY2026): discovered that FY2025 (closed) understated
                        Expense by 40 — a real Payable of 40, obligation arising Dec 15 2025,
                        was never recorded. Controller (CO-16 authority) judges this MATERIAL
                        relative to FY2025's reported Current Earnings of 300 (>10%)
Accounting Classification: Prior-Period Error (FY2025 is closed and was already reported;
                        this is not a change in estimate — the Payable existed and was simply
                        never captured, not a matter of judgment revised by new information,
                        IAS 8 para 5's Error definition vs para 5's Change in Estimate
                        definition)
Materiality Status:     MATERIAL (Controller judgment, CO-16 — not computed or defaulted by
                        this domain's design; the judgment itself, its basis, and its author
                        are recorded as an auditable fact per CO-16/CO-07)
Timeline:               obligation arose Dec 15 2025 (FY2025) -> FY2025 closed (Dec 31 2025,
                        original figures: Revenue 500, Expense 200, CE 300) -> error
                        discovered March 1 2026 (FY2026)
Effective Date:         Dec 15 2025 (both Lines of the restatement — the Payable existed as
                        of that date, this is when the obligation actually arose)
Recorded At:            March 1 2026 (both Lines — the actual moment this system accepts the
                        Restatement)
Original Report View:   Mode 1, any T before March 1 2026: FY2025 Expense 200, CE 300 —
                        exactly as originally reported, permanently, per BINV-11
Restated Report View:   Mode 2, any date on/after March 1 2026: FY2025 Expense 240
                        (200+40), CE 260 (500-240)
Current-Period P&L Effect: ZERO — FY2026's own Revenue/Expense (MP-09, Fiscal-Year-bounded)
                        never includes a Line whose Effective Date is Dec 15 2025 (FY2025).
                        Full arithmetic proof under Test 12.
Equity-Retained Earnings Effect: Reported Retained Earnings (B07 §1e) drops by 40 once the
                        restated FY2025 Current Earnings term (260, not 300) is summed in —
                        full arithmetic proof under Test 12.
Standard Principle Tested: IAS 8 para 5 (definition of prior period errors), para 41
                        ("material" prior period errors specifically), para 42 (mandatory
                        retrospective restatement for material errors)
Expected Result:        classified Material Prior-Period Error; routed to B04 §3c's
                        retrospective restatement mechanics, never to an ordinary
                        current-dated Entry alone (which is what Test 11 of B19, before this
                        round's correction, would have used unconditionally)
Actual Design Result:   CONFIRMED — B04 §3b's decision tree correctly routes this case to
                        §3c, distinct from B19 Test 11's original (pre-CORR-B3) scenario
                        precisely because THIS scenario is explicitly judged material and
                        THAT one was never tested for materiality at all
PASS / FAIL:            PASS
Finding:                none at the classification level — this is the corrected replacement
                        for B19 Test 11's unqualified conclusion; see B19's inline correction
                        note and superseded notice
Disposition:            n/a — mechanics verified numerically in Test 12
```

## Test 3 — Error originating before the earliest comparative period presented

```
Inputs:                 A separate small company ("Company Z"), FY2023 Current Earnings
                        originally reported as 200 (direct-posted prior Retained Earnings
                        entering FY2023: 800). In FY2026, preparing a report that presents
                        FY2024 and FY2025 as comparatives alongside current FY2026, an error
                        is discovered dated in FY2023 — BEFORE FY2024, the earliest period
                        actually presented in this report: Expense in FY2023 was understated
                        by 30. Judged MATERIAL.
Accounting Classification: Material Prior-Period Error, originating before the earliest
                        comparative period presented
Materiality Status:     MATERIAL (policy judgment, CO-16)
Timeline:               error originates FY2023 -> FY2023 closes (original CE 200) -> FY2024,
                        FY2025 close normally -> error discovered FY2026, when a report
                        presenting FY2024/FY2025 as comparatives is being prepared
Effective Date:         dated within FY2023 (the period the error actually occurred in) —
                        not forced to the start of FY2024 as a data fact, since the underlying
                        Entry genuinely belongs to FY2023
Recorded At:            FY2026 (actual commit time)
Original Report View:   Mode 1: FY2023 CE 200, exactly as originally reported
Restated Report View:   Mode 2: FY2023 CE 170 (200-30) — but FY2023 is NOT itself one of the
                        periods being presented in the FY2026 report (only FY2024/FY2025 are)
Current-Period P&L Effect: ZERO — same mechanism as Test 2, the error's Effective Date never
                        falls inside FY2024, FY2025, or FY2026
Equity-Retained Earnings Effect: Reported Retained Earnings as of the START of FY2024 (the
                        earliest period actually presented) = 800 (direct) + 170 (FY2023,
                        restated) = 970 — automatically 30 lower than the originally-reported
                        1000 (800+200), with NO special "opening balance adjustment" posting
                        required. This is B07 §1e's formula producing IAS 8 para 42(b)'s
                        required outcome (restating "the opening balances of assets,
                        liabilities and equity for the earliest prior period presented") as a
                        direct, automatic consequence of summing every closed Fiscal Year up
                        to the query date — not as a separately-designed special case.
Standard Principle Tested: IAS 8 para 42(b) — restating opening balances of the earliest
                        period presented when the error predates it
Expected Result:        the restatement affects the OPENING Reported Retained Earnings figure
                        for FY2024 (the earliest period presented), computed automatically by
                        the derived formula, with no bespoke "opening balance adjustment"
                        mechanism needed
Actual Design Result:   CONFIRMED — 970 = 800 + 170, matching para 42(b)'s requirement exactly;
                        this is also the clearest illustration in this regression of why the
                        no-posted-close model (DT-10) generalizes cleanly to this case, where
                        a posted-Entry model would have needed an entirely separate
                        "opening-balance adjustment entry" concept that IAS 8 itself does not
                        describe as a posted transaction either
PASS / FAIL:            PASS
Finding:                none
Disposition:            n/a
```

## Test 4 — Impracticable to determine period-specific effects

```
Inputs:                 Company Z again: a systemic classification error affecting FY2023 AND
                        FY2024 is discovered in FY2026. The TOTAL (cumulative) effect as of
                        the start of FY2025 (the earliest period for which restatement is
                        practicable) can be reliably determined (60, after every reasonable
                        effort — IAS 8 para 50-53's standard), but the split between how much
                        of the 60 belongs to FY2023 specifically versus FY2024 specifically
                        cannot be reconstructed from available records
Accounting Classification: Material Prior-Period Error, period-specific effects impracticable
                        to determine (IAS 8 para 43)
Materiality Status:     MATERIAL (policy judgment, CO-16)
Timeline:               error spans FY2023-FY2024 -> discovered FY2026 -> determined
                        impracticable (after genuine effort, not merely inconvenient — para
                        50's standard) to split by year, but the total-to-date-of-FY2025 figure
                        is determinable
Effective Date:         start of FY2025 (the earliest period for which restatement IS
                        practicable, per para 43) — NOT attributed to FY2023 or FY2024
                        individually, and NOT dated "today" either, since para 43 specifically
                        requires restating from the earliest practicable point, not deferring
                        to the discovery date
Recorded At:            FY2026 (actual commit time)
Original Report View:   Mode 1: FY2023 CE and FY2024 CE both exactly as originally reported —
                        neither is touched, because the correction cannot honestly be
                        attributed to either individually
Restated Report View:   Mode 2: FY2023 CE and FY2024 CE UNCHANGED (deliberately — attributing
                        an inseparable error to specific years would fabricate a precision the
                        facts don't support); instead, the direct-posted Reported Retained
                        Earnings component is adjusted by 60 as of the start of FY2025
Current-Period P&L Effect: ZERO — the adjustment's Effective Date is the start of FY2025, not
                        inside FY2026
Equity-Retained Earnings Effect: Reported Retained Earnings as of start of FY2025 is reduced
                        by 60, via a direct adjustment to the formally-designated Retained
                        Earnings account's own direct-posted balance (B07 §1e's first term) —
                        not via any closed Fiscal Year's Current-Earnings term, precisely
                        because this correction is, by construction, NOT attributable to one
Standard Principle Tested: IAS 8 para 43 (restate opening balances of the earliest period for
                        which restatement is practicable, when period-specific effects cannot
                        be determined) and para 50-53 (impracticability is a genuine-effort
                        standard, not a convenience threshold)
Expected Result:        B07 §1e's formula must be able to express "an adjustment not
                        attributable to any specific closed Fiscal Year" — this was not
                        originally an explicit case in the formula as first stated this round
Actual Design Result:   REFINEMENT FOUND while constructing this test: the formula as first
                        written this round (B07 §1e) only explicitly named "direct postings to
                        the Retained Earnings account (e.g. dividend declarations)" as the
                        non-Fiscal-Year-term component. An impracticability adjustment under
                        para 43 is exactly this shape (a direct posting to Retained Earnings,
                        dated at the earliest practicable point, not attributed to any single
                        FY's Current Earnings) — the formula already structurally
                        accommodates it without modification, but B07 §1e's own text did not
                        say so explicitly, which could have left a future reader wondering
                        whether a THIRD formula term was needed. Corrected: B07 §1e annotated
                        (not restructured) to state explicitly that an impracticability
                        adjustment under IAS 8 para 43 is an instance of the existing
                        direct-posting term, not a new term.
PASS / FAIL:            PASS, after the annotation above
Finding:                B07 §1e's formula was arithmetically already correct for this case,
                        but did not explicitly say so, which is itself a real gap this
                        regression's construction process caught, in the same spirit as B19
                        Test 9's and B19 Test 11's self-caught construction errors
Disposition:            [B07_CONCEPTUAL_INFORMATION_MODEL.md](B07_CONCEPTUAL_INFORMATION_MODEL.md)
                        §1e annotated at CORR-B3-06 to state this explicitly, cross-referencing
                        this test
```

## Test 5 — Impracticable to determine the cumulative effect at all

```
Inputs:                 Company Z once more, a different legacy-data issue: an error
                        originating so far in the past, in records that no longer support ANY
                        reasonable reconstruction (not even the cumulative effect as of the
                        start of any later period, after genuine effort per para 50-53), is
                        discovered in FY2026. The earliest date from which the CORRECT
                        treatment can actually be applied going forward is determined to be
                        the start of FY2026 itself.
Accounting Classification: Material Prior-Period Error, cumulative effect impracticable to
                        determine at the start of the current period (IAS 8 para 45)
Materiality Status:     MATERIAL (policy judgment, CO-16) — materiality of the ongoing effect,
                        even though the historical cumulative figure cannot itself be
                        determined
Timeline:               error origin unknown/unreconstructable -> discovered FY2026 ->
                        earliest practicable date to apply correct treatment determined to be
                        start of FY2026
Effective Date:         start of FY2026 — the earliest practicable date, per para 45; NO
                        restatement of any prior period or of any opening balance is
                        attempted, because para 45 specifically permits (requires, when
                        retrospective correction is impracticable) prospective-only correction
                        from that point forward
Recorded At:            FY2026 (actual commit time, at or after start of FY2026)
Original Report View:   Mode 1: every prior period's figures remain exactly as originally
                        reported, permanently, with no restatement claim made at all — not
                        because the error is being ignored, but because para 45 does not
                        require the impossible
Restated Report View:   Mode 2: identical to Mode 1 for every period before FY2026 (nothing is
                        restated); FY2026 onward reflects the corrected treatment
Current-Period P&L Effect: FY2026 (and only FY2026 onward) is affected, going forward, by the
                        corrected treatment — this is the one case in this regression where a
                        "prior-period error" correction legitimately DOES touch current and
                        future periods' own figures directly, precisely because IAS 8 para 45
                        authorizes prospective application specifically when retrospective
                        restatement is impracticable
Equity-Retained Earnings Effect: NONE retroactively — no adjustment to Reported Retained
                        Earnings' historical components, because nothing is being restated;
                        Reported Retained Earnings only changes going forward as FY2026 and
                        later years close under the corrected treatment
Standard Principle Tested: IAS 8 para 45 (prospective correction from the earliest practicable
                        date, when retrospective restatement of the cumulative effect is
                        impracticable) and para 5/50-53 (impracticability defined, no-hindsight
                        rule)
Expected Result:        mechanically similar outcome to an ordinary current-dated Entry (Test
                        1's shape), but for an entirely different, standard-specific reason —
                        this distinction must remain visible, not collapsed into "just use an
                        ordinary Entry" without recording WHY
Actual Design Result:   CONFIRMED — B04 §3c's decision tree reaches this outcome via a
                        distinct labeled path (Material Prior-Period Error, cumulative effect
                        impracticable) rather than by falling through to Test 1's
                        Current-Period-Error path or Test 7's Immaterial path, preserving the
                        classification's audit trail (CO-07) even though the mechanical
                        posting shape converges with those other paths
PASS / FAIL:            PASS
Finding:                none beyond Test 4's (both impracticability tests were constructed
                        together; the refinement found in Test 4 applies equally in spirit
                        here, though this test's own arithmetic needed no formula change since
                        no restatement term is invoked at all)
Disposition:            n/a beyond Test 4's B07 §1e annotation
```

## Test 6 — Change in accounting estimate (never a Prior-Period Error)

```
Inputs:                 In FY2026, new information becomes available that changes a
                        previously recorded estimate (e.g. an allowance/provision balance
                        carried at 80, revised to 95 based on updated information) — the
                        original 80 was a reasonable estimate given what was known at the
                        time, not a mistake
Accounting Classification: Change in Accounting Estimate (IAS 8 para 5, paras 32/34) — NOT an
                        error, because the original figure was a faithful application of
                        judgment to the information available then (para 34's explicit test:
                        a change in estimate is not a correction of an error)
Materiality Status:     Not applicable — CO-16's materiality gate applies to the Error branch
                        of B04 §3b's tree specifically; estimate changes never reach it
Timeline:               original estimate recorded pre-FY2026 -> revised FY2026, based on new
                        information becoming available in FY2026, not on facts that already
                        existed and were simply missed
Effective Date:         FY2026 (current-dated only — IAS 8 para 36 requires prospective
                        application)
Recorded At:            FY2026 (actual commit time)
Original Report View:   Mode 1: unaffected — the original estimate stands exactly as reported,
                        because it was correct given what was knowable then; there is nothing
                        to "restate," by definition
Restated Report View:   n/a — para 36 explicitly prohibits treating an estimate change as if
                        it were a restatement; the concept does not apply
Current-Period P&L Effect: the 15 revision (95-80) is recognized in FY2026's own P&L,
                        prospectively, exactly where IAS 8 para 36 requires it
Equity-Retained Earnings Effect: none directly — it flows through FY2026's own Current
                        Earnings when FY2026 eventually closes, like any other current-period
                        P&L item, not through any special Reported-Retained-Earnings term
Standard Principle Tested: IAS 8 para 5 (definition), para 32-38 (estimates, prospective
                        application only), para 36 specifically (recognized in the period of
                        change and future periods, never retrospectively)
Expected Result:        ordinary current-dated Entry, B04 §3b's Estimate branch, never reaching
                        §3c's restatement mechanics
Actual Design Result:   CONFIRMED — B04 §3b's decision tree's second test (new information
                        about facts that always existed and were missed, vs. new circumstances/
                        new information changing a judgment) correctly separates this from
                        Test 2's Payable scenario, which involved a fact (an existing
                        obligation) that was simply never captured, not a judgment revised
PASS / FAIL:            PASS
Finding:                none
Disposition:            n/a
```

## Test 7 — Immaterial prior-period error

```
Inputs:                 In FY2026, a small prior-period error is discovered in FY2025
                        (closed): Expense understated by 2 (against FY2025's Current Earnings
                        of 300). Controller (CO-16) judges this IMMATERIAL — 2 could not
                        reasonably influence any user's economic decisions about FY2025 or
                        FY2026
Accounting Classification: Prior-Period Error, IMMATERIAL (IAS 8 para 5's error definition
                        applies; para 41's "material" qualifier for the mandatory-restatement
                        requirement does not)
Materiality Status:     IMMATERIAL (policy judgment, CO-16)
Timeline:               obligation arose FY2025 -> FY2025 closed -> discovered FY2026,
                        judged immaterial
Effective Date:         FY2026, current-dated (an ordinary Entry — this is the one branch of
                        B04 §3b's tree that still reaches exactly the outcome B19 Test 11's
                        original, unqualified conclusion described, now correctly scoped to
                        apply only here)
Recorded At:            FY2026 (actual commit time)
Original Report View:   Mode 1: FY2025 unaffected, exactly as reported
Restated Report View:   n/a — IAS 8 does not require restatement for immaterial errors; none
                        is performed, by design choice consistent with the standard, not by
                        oversight
Current-Period P&L Effect: the 2 is recognized in FY2026's own current-period P&L, exactly
                        like Test 1 mechanically, but for a different, explicitly recorded
                        reason (immateriality, not same-period timing)
Equity-Retained Earnings Effect: flows through FY2026's own eventual Current Earnings, like
                        any ordinary current-period item — FY2025's already-closed Current
                        Earnings term in Reported Retained Earnings is deliberately left
                        untouched
Standard Principle Tested: IAS 8 para 41 (the materiality qualifier that scopes the mandatory
                        retrospective-restatement requirement) — confirming this domain's
                        design does not over-apply §3c's heavier mechanics where the standard
                        does not require them
Expected Result:        ordinary current-dated Entry is sufficient — this is B19 Test 11's
                        original conclusion, now correctly confirmed as valid for exactly this
                        (immaterial) case, not universally
Actual Design Result:   CONFIRMED — this is the test that formally validates what B19 Test 11
                        got right (for the wrong, unqualified reason) — see the inline
                        correction note at B19 Test 11
PASS / FAIL:            PASS
Finding:                none — this is the corrected, properly-scoped restatement of B19 Test
                        11's original conclusion
Disposition:            n/a
```

## Test 8 — Original vs. restated comparative, correctly labeled (CO-14)

```
Inputs:                 same facts as Test 2/Test 12 (the 40-unit FY2025 Payable, judged
                        material, restated March 1 2026)
Accounting Classification: Material Prior-Period Error (same as Test 2)
Materiality Status:     MATERIAL (same as Test 2)
Timeline:               same as Test 2/12
Effective Date:         Dec 15 2025 (same as Test 2/12)
Recorded At:            March 1 2026 (same as Test 2/12)
Original Report View:   a report generator queries Mode 1 with T = Feb 15 2026 (before the
                        restatement): returns FY2025 Expense 200, CE 300 — and, per CO-14, is
                        REQUIRED to be labeled "as originally known, as of 2026-02-15,"
                        never presented as an unlabeled, bare number
Restated Report View:   the same report generator, queried again with Mode 2 after March 1
                        2026: returns FY2025 Expense 240, CE 260 — REQUIRED to be labeled
                        "current / restated as of [today]," per CO-14
Current-Period P&L Effect: (cross-reference to Test 2/12) zero
Equity-Retained Earnings Effect: (cross-reference to Test 2/12) Reported RE drops by 40 once
                        summed via the closed-FY2025 term
Standard Principle Tested: IAS 8 para 42(a) (present the restated comparative amount, i.e. a
                        reader must be able to see both the originally-reported and
                        corrected figures without one silently masquerading as the other) —
                        this is directly the same acceptance requirement `M-AUD-04` stated for
                        Round 2's CO-14 (do not let one silently masquerade as the other),
                        now confirmed to also satisfy IAS 8's own comparative-presentation
                        requirement, not merely this domain's own internal consistency goal
Expected Result:        the two views are simultaneously available, never blended, and always
                        explicitly labeled
Actual Design Result:   CONFIRMED — CO-14 (added Round 2, unmodified this round) already
                        fully satisfies IAS 8 para 42(a)'s presentation requirement; no new
                        control was needed, only confirmation that the existing one covers
                        this standard-driven case too
PASS / FAIL:            PASS
Finding:                none — a case where a Round 2 control, designed for a different
                        stated reason (temporal-mode clarity generally), turns out to already
                        satisfy a Round 3 standard-specific requirement without modification
Disposition:            n/a
```

## Test 9 — Fiscal Year Close: pre-close P&L (Company X)

```
Inputs:                 Company X, Dec 31 2025, immediately BEFORE Fiscal Year Close is
                        declared for FY2025
Accounting Classification: n/a — this test is about Fiscal Year Close mechanics (B08 MP-11,
                        corrected), not error/restatement classification
Materiality Status:     n/a
Timeline:               FY2025 activity complete (Revenue 500, Expense 200, both cash) ->
                        query as-of Dec 31 2025, before FiscalYearClosed is declared
Effective Date:         query date Dec 31 2025 (Mode 2)
Recorded At:            n/a (a read query, not a posting)
Original Report View:   n/a — nothing has been restated
Restated Report View:   n/a
Current-Period P&L Effect: Revenue(FY2025, Mode 2, Fiscal-Year-bounded) = 500; Expense = 200;
                        Current Earnings = 300 — matching actual FY2025 activity exactly
Equity-Retained Earnings Effect: Reported Retained Earnings as of Dec 31 2025 (FY2025 not yet
                        closed) = 1000 (direct) + 250 (FY2024, closed) = 1250 — FY2025's 300
                        is NOT yet included, since it has not yet closed
Standard Principle Tested: B08 MP-11 (corrected) — confirms no Entry has been posted yet and
                        none is needed for this reading to be correct
Expected Result:        expanded equation holds: Assets + Expenses = Liabilities + Equity +
                        Revenue
Actual Design Result:   VERIFIED NUMERICALLY: Cash 1550 (=1250+500-200) + Expense 200 =
                        Liabilities 0 + Reported Equity 1250 + Revenue 500 -> 1750 = 1750 ✓
PASS / FAIL:            PASS
Finding:                none
Disposition:            n/a
```

## Test 10 — Fiscal Year Close: post-close ledger, no Entry posted (Company X)

```
Inputs:                 Company X, Jan 1 2026, immediately AFTER FiscalYearClosed is declared
                        for FY2025 (an authorized declaration/lock action, B04, no Entry)
Accounting Classification: n/a — Fiscal Year Close mechanics
Materiality Status:     n/a
Timeline:               FiscalYearClosed declared for FY2025 at year-end -> query as-of Jan 1
                        2026
Effective Date:         query date Jan 1 2026 (Mode 2)
Recorded At:            n/a (the FiscalYearClosed Audit Event's own Recorded At is Dec 31
                        2025/Jan 1 2026, but no Entry exists to have a Recorded At)
Original Report View:   n/a
Restated Report View:   n/a
Current-Period P&L Effect: Revenue(FY2026, Mode 2) = 0; Expense(FY2026) = 0 — automatically,
                        because MP-09's Fiscal-Year lower bound for the new year starts at
                        Jan 1 2026, with no Entry required to make this true
Equity-Retained Earnings Effect: Reported Retained Earnings (B07 §1e) as of Jan 1 2026 = 1000
                        (direct) + 250 (FY2024, closed) + 300 (FY2025, now closed) = 1550
Standard Principle Tested: B08 MP-11 (corrected) — the specific defect `M-AUD-07` found (a
                        posted Entry corrupting the closing year's own historical query) is
                        directly checked here: does querying Dec 31 2025 AGAIN, from this
                        Jan 1 2026 vantage point, still return the Test 9 figures unchanged?
Expected Result:        (a) simple equation holds using Reported Equity; (b) no Balance Sheet
                        amount duplicated; (c) FY2026 Revenue/Expense start at zero with no
                        Entry; (d) re-querying Dec 31 2025 (the closing date itself) returns
                        EXACTLY Test 9's figures, unchanged by the close action
Actual Design Result:   VERIFIED NUMERICALLY: (a) Cash 1550 = Liabilities 0 + Reported Equity
                        1550 ✓ (simple equation, using the NOW-UPDATED Reported Equity
                        figure, exactly as MP-02's post-closing special case requires); (b)
                        1550 appears exactly once (as Cash), not also duplicated inside a
                        posted opening-balance fact, because none exists; (c) confirmed by
                        construction — Revenue/Expense(FY2026) both 0, no Entry involved; (d)
                        re-querying Dec 31 2025 returns Revenue 500/Expense 200/CE 300,
                        IDENTICAL to Test 9 — because no Entry was posted at any date, there is
                        nothing for a Dec 31 2025 query to pick up that wasn't already there.
                        This is the direct numerical refutation of `M-AUD-07`'s traced defect
                        against the Round-2 posted-Entry model, which — had it been dated
                        inside FY2025 — would have added its own debit-Revenue/credit-Expense
                        Lines into exactly this Dec 31 2025 query, corrupting it.
PASS / FAIL:            PASS
Finding:                none
Disposition:            n/a
```

## Test 11 — New Fiscal Year P&L starts clean (Company X)

```
Inputs:                 Company X, Jan 15 2026: a new sale, Revenue 50 (cash)
Accounting Classification: n/a — ordinary current-period activity, included only to confirm
                        the new Fiscal Year's aggregation is unaffected by the prior year's
                        close
Materiality Status:     n/a
Timeline:               FY2025 closed (Test 10) -> Jan 15 2026, new Revenue posted -> query
                        as-of Jan 15 2026
Effective Date:         Jan 15 2026 (Mode 2)
Recorded At:            Jan 15 2026
Original Report View:   n/a
Restated Report View:   n/a
Current-Period P&L Effect: Revenue(FY2026, Mode 2) = 50 (only the new sale — NOT 550, i.e.
                        NOT FY2025's 500 plus this 50 — confirming MP-09's Fiscal-Year lower
                        bound correctly excludes FY2025 activity from FY2026's own sum);
                        Expense(FY2026) = 0
Equity-Retained Earnings Effect: unchanged from Test 10 (1550) — FY2026 has not closed, so its
                        in-progress 50 of Current Earnings is not yet part of Reported
                        Retained Earnings
Standard Principle Tested: B08 MP-09 (Fiscal-Year category bound, unchanged this round) working
                        correctly in combination with the corrected MP-11 — confirms the two
                        principles remain consistent with each other after MP-11's rewrite
Expected Result:        expanded equation holds; FY2026 Revenue reads exactly 50, not
                        contaminated by FY2025's activity
Actual Design Result:   VERIFIED NUMERICALLY: Cash 1600 (=1550+50) + Expense(FY26) 0 =
                        Liabilities 0 + Reported Equity 1550 + Revenue(FY26) 50 -> 1600 = 1600 ✓
PASS / FAIL:            PASS
Finding:                none
Disposition:            n/a
```

## Test 12 — Restatement after Fiscal Year Close: full arithmetic (Company X)

```
Inputs:                 Company X, March 1 2026: the Test 2 Payable (40, Effective Date Dec 15
                        2025, judged MATERIAL) is committed as a Restatement: dr Expense 40
                        (Eff. Dec 15 2025) / cr Payable 40 (Eff. Dec 15 2025), both Recorded
                        At March 1 2026
Accounting Classification: Material Prior-Period Error (same as Test 2) — this test verifies
                        the ARITHMETIC; Test 2 verified the CLASSIFICATION
Materiality Status:     MATERIAL (same as Test 2)
Timeline:               (continuing Test 11) Jan 15 2026 Revenue 50 -> March 1 2026
                        Restatement committed
Effective Date:         Dec 15 2025 (both Lines)
Recorded At:            March 1 2026 (both Lines)
Original Report View:   Mode 1, T = Feb 15 2026 (before restatement): FY2025 Expense 200, CE
                        300, Reported RE (as known then) = 1000+250+300 = 1550 — permanently
                        preserved, per BINV-11, regardless of anything committed after Feb 15
Restated Report View:   Mode 2, any date on/after March 1 2026: FY2025 Expense 240, CE 260
Current-Period P&L Effect: Revenue(FY2026, Mode 2) = 50 (unchanged from Test 11); Expense
                        (FY2026, Mode 2) = 0 (unchanged) — the Restatement's Lines, dated Dec
                        15 2025, fall outside FY2026's Fiscal-Year bound entirely
Equity-Retained Earnings Effect: Reported Retained Earnings as of March 1 2026 = 1000 (direct,
                        unchanged) + 250 (FY2024, unaffected) + 260 (FY2025, restated, was
                        300) = 1510 — a drop of exactly 40 from Test 11's 1550, matching the
                        Payable's amount exactly, with no separate "prior period adjustment"
                        posting required
Standard Principle Tested: IAS 8 para 46 (the correction "is not included in profit or loss
                        for the period in which the error is discovered") and para 42
                        (retrospective restatement of comparative amounts) — both checked by
                        direct arithmetic, not merely asserted
Expected Result:        expanded equation holds after the Restatement; FY2026's own P&L is
                        untouched (para 46); the Restatement's effect appears only in FY2025's
                        restated comparative and in Reported Retained Earnings (para 42)
Actual Design Result:   VERIFIED NUMERICALLY: Cash 1600 (unchanged — an accrual, no cash
                        movement) + Expense(FY26) 0 = Liabilities (Payable) 40 + Reported
                        Equity 1510 + Revenue(FY26) 50 -> 1600 = 1600 ✓. Cross-check against
                        Test 11's pre-restatement equation (1600 = 0 + 1550 + 50): the 40
                        moved from the Equity term to the Liabilities term, net zero change to
                        the total — exactly what a correctly-balanced accrual restatement
                        should do, with FY2026's own Revenue/Expense terms provably untouched
                        (para 46 satisfied by direct arithmetic, not by assertion).
PASS / FAIL:            PASS
Finding:                none
Disposition:            n/a
```

## Test 13 — Migration opening balance, distinct from Fiscal Year Close and Restatement

```
Inputs:                 a separate company ("Company Y") migrating to SMEsPlus, cutover Jan 1
                        2026, using MG-C03's summarized-opening-balance choice (not full
                        historical detail, MG-C04): dr Cash 500 / cr Retained Earnings
                        (direct-posted) 500
Accounting Classification: NEITHER a Fiscal Year Close fact NOR a Prior-Period Error/
                        Restatement — a distinct MG-C03 migration fact, its own category
Materiality Status:     n/a — materiality (CO-16) applies to error corrections; a migration
                        opening balance is not a correction of anything, it is the ledger's
                        one-time seed
Timeline:               migration cutover Jan 1 2026 (accounting date); actual migration
                        commit occurs at whatever real instant the migration executes
Effective Date:         Jan 1 2026 (the historical cutover accounting date)
Recorded At:            the actual migration execution instant (per MG-C14) — NOT Jan 1 2026
                        unless migration happens to execute exactly then; Mode-1 "as
                        originally known" queries for Company Y are only meaningful from this
                        Recorded At forward, exactly as MG-C14 already states
Original Report View:   n/a — this is the first fact in Company Y's ledger; there is no prior
                        "original" view to compare against
Restated Report View:   n/a — not a restatement
Current-Period P&L Effect: none — Cash and Retained Earnings only, no Revenue/Expense Line
                        exists in this Entry
Equity-Retained Earnings Effect: Reported Retained Earnings (B07 §1e) for Company Y
                        immediately post-migration = 500 (the direct-posted term) + 0 (no
                        Fiscal Year has closed yet for Company Y in this system) = 500
Standard Principle Tested: not an IAS 8 question at all — this test exists to confirm B10
                        MG-C03 remains structurally distinct from B08 MP-11 (corrected) and
                        B04 §3c, per the directive's explicit instruction to keep migration
                        opening balance separate from Fiscal Year Close/restatement semantics
Expected Result:        the migration opening balance Entry independently satisfies MP-01
                        (500=500); it is never classified via B04 §3b's error/estimate tree
                        (it corrects nothing); it never triggers CAP-09/MP-11 (it is not a
                        Fiscal Year Close action)
Actual Design Result:   CONFIRMED — B10 MG-C03, re-verified (not rewritten) at CORR-B3-04,
                        remains accurate: an ordinary, fully-governed Entry, categorically
                        outside both B04 §3b/§3c's classification tree and B08 MP-11's
                        Fiscal-Year-Close declaration, exactly as B10's Round-3 re-verification
                        note states
PASS / FAIL:            PASS
Finding:                none
Disposition:            n/a
```

## Test 14 — Correction of a Restatement itself (chained, Company X)

```
Inputs:                 Company X, April 2026: the March 1 2026 Restatement (Test 12) is
                        itself found slightly wrong — the Payable should have been 45, not 40.
                        A further Correction, chained to the Restatement Entry (B04 §6's
                        existing chain rules — a correction of a correction is not a special
                        case), is committed: dr Expense 5 / cr Payable 5, Effective Date Dec
                        15 2025 (same original period), Recorded At April 2026
Accounting Classification: this further Correction is ITSELF classified independently via
                        B04 §3b (it corrects a Material Prior-Period Error's restatement, and
                        is judged to inherit the same Material classification, since it
                        affects the same underlying FY2025 error) — B04 §3b/§3c apply to every
                        correction independently, including a correction of a Restatement,
                        not only to "first" corrections
Materiality Status:     MATERIAL (inherited judgment, CO-16 — the incremental 5 is evaluated
                        in the context of the same underlying FY2025 error already judged
                        material, not re-evaluated as if it were a fresh, isolated 5-unit item)
Timeline:               (continuing Test 12) March 1 2026 Restatement -> April 2026 further
                        Correction, chained
Effective Date:         Dec 15 2025 (same period as the original Restatement)
Recorded At:            April 2026 (the new Correction's own, later, Recorded At — distinct
                        from the Restatement's March 1 2026 Recorded At, per BINV-12)
Original Report View:   Mode 1, T = Feb 15 2026 (before EITHER correction): FY2025 Expense
                        200, CE 300 — unaffected by either the March 1 Restatement or the
                        April Correction, per BINV-11's unconditional guarantee
Restated Report View:   Mode 2, any date on/after April 2026: FY2025 Expense 245 (200+40+5),
                        CE 255 (500-245)
Current-Period P&L Effect: FY2026's own Revenue/Expense unaffected — same mechanism as Test
                        12, the chained Correction's Effective Date is still Dec 15 2025
Equity-Retained Earnings Effect: Reported Retained Earnings as of April 2026 = 1000 (direct)
                        + 250 (FY2024) + 255 (FY2025, twice-restated) = 1505 — a further drop
                        of 5 from Test 12's 1510
Standard Principle Tested: B04 §6's chain-of-corrections rule (unchanged this round), applied
                        to confirm it composes correctly with the NEW §3b/§3c classification
                        machinery — a chained correction is not exempted from classification
                        just because it corrects a Restatement rather than an original Entry
Expected Result:        expanded equation holds after the chained Correction; Payable reads
                        45 (40+5), not 40 or 5 alone
Actual Design Result:   VERIFIED NUMERICALLY: Payable = 40+5 = 45. Cash 1600 (unchanged,
                        still an accrual) + Expense(FY26) 0 = Liabilities 45 + Reported Equity
                        1505 + Revenue(FY26) 50 -> 1600 = 1600 ✓
PASS / FAIL:            PASS
Finding:                none
Disposition:            n/a
```

## Test 15 — Multi-company isolation of restatement and Fiscal Year Close

```
Inputs:                 Company X (as above) and Company Y (Test 13) coexist under the same
                        SMEsPlus tenant. Company X's March 1 2026 Restatement (Test 12) and
                        its FY2025 Fiscal Year Close (Test 10) are both committed.
Accounting Classification: n/a — this test is a boundary/isolation check, not a
                        classification check
Materiality Status:     n/a
Timeline:               concurrent with Tests 10-13
Effective Date:         n/a (checking cross-company non-interference, not a single fact's date)
Recorded At:            n/a
Original Report View:   Company Y's Mode 1/Mode 2 views, queried at any point during or after
                        Company X's Restatement/Fiscal-Year-Close activity
Restated Report View:   same
Current-Period P&L Effect: Company Y's Revenue/Expense/Current Earnings must read exactly as
                        Test 13 left them, unaffected by anything committed against Company X
Equity-Retained Earnings Effect: Company Y's Reported Retained Earnings must remain exactly
                        500 (Test 13), regardless of Company X's Reported Retained Earnings
                        moving from 1250 (Test 9) to 1550 (Test 10) to 1510 (Test 12) to 1505
                        (Test 14)
Standard Principle Tested: CAP-05 (Company boundary) and CO-09 (multi-company access scoping),
                        unchanged this round — confirms B04 §3b/§3c's new classification
                        machinery and B07 §1e's new formula are both defined per-Company (MP-09
                        was already Company-scoped before this round) and introduce no new
                        cross-company aggregation path
Expected Result:        zero interference in either direction
Actual Design Result:   CONFIRMED BY CONSTRUCTION — B07 §1e's formula sums over Fiscal Years
                        of ONE Company (inherited directly from MP-09's existing Company scope,
                        B08, unchanged); B04 §3b/§3c's classification and restatement mechanics
                        operate on individual Entries, which already carry a single Company via
                        their Lines (BINV-03) — no step in either new mechanism aggregates or
                        classifies across a Company boundary, so no new isolation risk is
                        introduced by this round's corrections
PASS / FAIL:            PASS
Finding:                none
Disposition:            n/a
```

## Regression Result

```
Scenarios executed:                            15
PASS:                                           15
Real design refinement found during construction, applied: 1 (Test 4 — B07 §1e's formula was
  already arithmetically correct for an impracticability adjustment not attributable to any
  single closed Fiscal Year, but did not say so explicitly; annotated, not restructured)
Regressions into any prior-fixed defect:        0 (re-confirmed: Tests 9-11 re-verify
  `M-AUD-05`'s double-counting fix and `M-AUD-07`'s posted-Entry fix together; Test 14
  re-verifies `M-AUD-04`'s Mode-1/BINV-11 guarantee under a chained correction)
New CRITICAL/HIGH defects:                      0
```

**B20 = COMPLETE.** Tests 4/5 are deliberately presented together, showing the formula
annotation found while constructing them, rather than only the final annotated state — the
same discipline B18 Test 9, B19 Test 9, and B19 Test 11 already established for this project.
Test 11's superseded conclusion from B19 is not repeated or re-litigated here; Tests 2 and 7
of this document together constitute its full, corrected replacement (material vs. immaterial
respectively), and B19 Test 11 itself carries an inline pointer back to this document rather
than being silently rewritten.
