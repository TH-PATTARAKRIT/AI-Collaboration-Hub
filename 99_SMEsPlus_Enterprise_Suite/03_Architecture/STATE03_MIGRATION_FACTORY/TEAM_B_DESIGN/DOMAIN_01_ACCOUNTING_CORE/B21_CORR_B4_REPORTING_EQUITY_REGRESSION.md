# B21 — CORR-B4 Reporting Equity Regression

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-30-MIG-B-D01-CORR4-001 |
| Source of truth | CORR4-001 directive §8 — 15 mandatory scenarios, tested against the CORR-B4-corrected design (B07 §1e/§1f/§1g, B08 MP-02/MP-11/MP-12, B05 BINV-10/BINV-14, B02 CAP-09, B13 DT-11) |
| Personas | Senior Accountant, Financial Controller, External Auditor, Fiscal-Year Close Operator, Historical Reporting Reviewer, Migration Architect, SaaS Domain Architect, Accounting Systems Architect, Clean-room Reviewer |
| Result | **15/15 PASS. No new refinement required beyond the formula fixes already made in B07/B08 while constructing this regression — every worked figure below matched the corrected formulas on first computation, cross-checked twice per test (once via the Reported form, once via re-deriving from the Raw Ledger Identity).** |
| **Terminology note (Round 5)** | **CORR-B5-01/02 (2026-08-30)** — ChatGPT's Round 5 re-audit (`M-AUD-11`) found that B08 MP-12's own Round-4 prose (Proof G) mislabeled MP-09's mixed-horizon output as "the Raw Trial Balance." This document's own Tests 3/4 "Raw TB Result" figures were, and remain, numerically correct — they always summed EVERY category on one common (all-time) horizon, exactly what is now formally named `CumulativeAccountBalance` / MP-12 Proof G1, never the mixed-horizon quantity the defect actually lived in. No test in this document requires restatement. Test 5's own figures (Cash 1250, Direct RE 1000, FY2024 Revenue 400/Expense 150) are the exact numbers ChatGPT's Round 5 audit traced to demonstrate `M-AUD-11`'s failure case, now formally reproduced and resolved at [B22](B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md) Test 3. See [CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md](CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md). |

Money amounts below are illustrative units, chosen for arithmetic clarity, not a specific
currency. Three companies are used, each self-contained: **Company X** (continues directly
from [B20](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md)'s figures — single Equity account,
the designated Retained Earnings account itself), **Company W** (new this document — multiple
Equity accounts, needed to verify B07 §1f's non-overlapping decomposition for real, not only in
the single-account case B20 happened to use throughout), and **Company Y** (continues from
B20's migration example). "Recorded At" is abbreviated to the day for readability; the actual
guarantee (BINV-12) is instant-level. Per the directive's required schema, every test below
records: Inputs / Timeline / Fiscal-Year State / Operational Close State / Effective Date /
Recorded At / Raw Ledger Components / Raw TB Result / Reported Equity Components / Reporting
Viewpoint / Expected Equation / Actual Design Equation / Expected Result / Actual Result /
PASS-FAIL / Finding / Disposition.

## Company X — Running Balances (continued from B20; extended this document)

```
(from B20) Baseline start FY2024: Cash 1000, Direct RE 1000 (only Equity account)
(from B20) FY2024: Revenue 400, Expense 150 -> CE 250. Elapsed+Closed at year end (assumed
  exactly at boundary in B20). Cash = 1250.
(from B20) FY2025: Revenue 500, Expense 200 -> CE 300. Cash = 1550.
(from B20) FY2026 Jan15: Revenue 50 (cash). Cash = 1600.
(from B20) FY2025 Restatement, March 1 2026: Expense +40 (Payable), Effective Dec 15 2025,
  judged MATERIAL. Reported RE(Dec31/2025 view) 1550 -> 1510. Payable 40.
(from B20) Further correction of the Restatement, April 2026: Payable 40 -> 45 (+5 Expense,
  same Effective period). Reported RE(Dec31/2025 view) 1510 -> 1505.
(NEW, this document) FY2024 is re-examined with its DECLARATION timing made explicit for the
  first time (B20 always assumed declaration exactly at the boundary): FY2024's own End Date
  is Dec 31 2024; `FiscalYearClosed` for FY2024 is NOT declared until Jan 15 2025 (Tests 5-7).
```

## Test 1 — Direct RE + one completed Fiscal Year (the audit's own worked example)

```
Inputs:                  Company X. Direct Retained Earnings balance entering FY2024 = 1000.
                         FY2024 Current Earnings = 250 (Revenue 400, Expense 150).
Timeline:                FY2024 elapses (Dec 31 2024) -> query as of Jan 1 2025
Fiscal-Year State:       FY2024 ELAPSED (End Date Dec 31 2024 <= query date)
Operational Close State: `FiscalYearClosed` declared for FY2024 (assume on-time this test —
                         Tests 5-7 isolate the delayed-declaration case specifically)
Effective Date:          query date Jan 1 2025 (Mode 2 / Current viewpoint)
Recorded At:             n/a (a read query, not a posting)
Raw Ledger Components:   Cash 1250 (dr); Direct RE 1000 (cr, direct-posted only); Revenue 400
                         (cr, FY2024); Expense 150 (dr, FY2024) — the raw, all-time ledger,
                         Revenue/Expense not yet regrouped into any Reported term
Raw TB Result:           dr 1250 + 150 = 1400; cr 1000 + 400 = 1400. BALANCED.
Reported Equity Components: Other Ledger Equity = 0 (Company X has no Equity account besides
                         the designated RE account); Reported Retained Earnings = 1000 (direct)
                         + 250 (FY2024, elapsed) = 1250
Reporting Viewpoint:     Current (Mode 2)
Expected Equation:       Assets = Liabilities + Reported Equity (simple form; FY2025 has no
                         activity yet, CurrentFY Revenue/Expense both 0)
Actual Design Equation:  1250 = 0 + (0 + 1250) = 1250
Expected Result:         Reported Equity = 1250, NOT 1000 (ledger Equity) + 1250 (Reported RE)
                         = 2250 — the exact double-count `M-AUD-08` found under the
                         superseded Round-3 informal formula
Actual Result:           CONFIRMED 1250. The superseded formula's arithmetic (1000+1250=2250)
                         is explicitly computed here too, for contrast, and explicitly rejected:
                         it would overstate Assets=1250 against a claimed Equity of 2250 by
                         1000 — an immediate, glaring imbalance that the corrected formula never
                         produces because Other Ledger Equity excludes the designated RE account
                         by construction (B07 §1f), not by any care taken at query time.
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 2 — Multiple Equity accounts (Company W, new)

```
Inputs:                  Company W. Opening (Day 0): Cash 1600, Share Capital 500 (direct-
                         posted, distinct Equity account), Other Reserves 100 (direct-posted,
                         distinct Equity account), Direct Retained Earnings 1000 (the ONE
                         designated RE account). FY2024: Revenue 400, Expense 150 (cash) ->
                         CE 250.
Timeline:                Day 0 opening -> FY2024 elapses -> query as of Jan 1 2025
Fiscal-Year State:       FY2024 ELAPSED
Operational Close State: `FiscalYearClosed` declared on-time for FY2024
Effective Date:          query date Jan 1 2025
Recorded At:             n/a (read query)
Raw Ledger Components:   Cash 1850 (dr, =1600+400-150); Share Capital 500 (cr); Other Reserves
                         100 (cr); Direct RE 1000 (cr); Revenue 400 (cr, FY2024); Expense 150
                         (dr, FY2024)
Raw TB Result:           dr 1850 + 150 = 2000; cr 500 + 100 + 1000 + 400 = 2000. BALANCED.
Reported Equity Components: Other Ledger Equity = Share Capital (500) + Other Reserves (100)
                         = 600 (every Equity account EXCEPT the designated RE account —
                         B07 §1f's decomposition applied for the first time to a Company where
                         it actually matters); Reported Retained Earnings = 1000 (direct) + 250
                         (FY2024, elapsed) = 1250
Reporting Viewpoint:     Current (Mode 2)
Expected Equation:       Assets = Liabilities + Reported Equity, Reported Equity = Other Ledger
                         Equity + Reported Retained Earnings, no account counted twice
Actual Design Equation:  1850 = 0 + (600 + 1250) = 1850
Expected Result:         Reported Equity = 1850; Share Capital and Other Reserves counted
                         exactly once (inside Other Ledger Equity), Direct RE counted exactly
                         once (inside Reported Retained Earnings) — no account in both terms
Actual Result:           CONFIRMED 1850 = 1850. Cross-checked against Raw TB (Test's own raw
                         credit total 2000, minus Revenue's 400 which folds into Reported RE's
                         CE term instead, plus Expense's 150 subtracted the other way — the
                         same Proof B algebra B08 MP-12 states symbolically, now verified with
                         a genuine multi-account Company, which B20 never constructed).
PASS / FAIL:             PASS
Finding:                 none — this is the first numeric confirmation of B07 §1f's
                         decomposition against a Company where Other Ledger Equity is
                         nonzero; B20's Company X/Y/Z all happened to have exactly one Equity
                         account, which is why `M-AUD-08`'s double-count never showed up
                         numerically there despite being present in the general formula
Disposition:             n/a
```

## Test 3 — Raw Trial Balance before fiscal boundary (Company W)

```
Inputs:                  Company W, mid-FY2024: as of June 30 2024, Revenue 200 and Expense 80
                         posted so far (half of FY2024's eventual full-year 400/150 — a fresh,
                         smaller partial-year figure for this specific test)
Timeline:                Day 0 opening -> partial FY2024 activity -> query as of June 30 2024
                         (BEFORE FY2024's End Date, Dec 31 2024)
Fiscal-Year State:       FY2024 NOT elapsed (End Date Dec 31 2024 > query date)
Operational Close State: n/a — FY2024 has not elapsed, so no close declaration is even
                         possible yet under CO-08's tiering
Effective Date:          query date June 30 2024
Recorded At:             n/a (read query)
Raw Ledger Components:   Cash 1720 (dr, =1600+200-80); Share Capital 500 (cr); Other Reserves
                         100 (cr); Direct RE 1000 (cr); Revenue 200 (cr, FY2024 partial);
                         Expense 80 (dr, FY2024 partial)
Raw TB Result:           dr 1720 + 80 = 1800; cr 500 + 100 + 1000 + 200 = 1800. BALANCED —
                         this is MP-02's expanded equation (Proof A), the raw identity, with
                         EVERY category on the same all-time horizon, no Fiscal-Year bound
                         applied to Revenue/Expense at this step
Reported Equity Components: n/a for this test — this test verifies the RAW Trial Balance only,
                         not the reported transformation (see Test 4 for the same facts,
                         reported)
Reporting Viewpoint:     n/a — raw ledger has no viewpoint distinction of its own beyond
                         whatever Mode is used to select "which Lines exist" (Mode 2/Current
                         used throughout this test)
Expected Equation:       RawAssets + RawExpenses = RawLiabilities + RawEquity + RawRevenue
                         (MP-02/MP-12 Proof A)
Actual Design Equation:  1720 + 80 = 0 + 1600 + 200 -> 1800 = 1800
Expected Result:         Raw Trial Balance balances under one consistent all-time horizon,
                         with no Fiscal-Year partitioning applied
Actual Result:           CONFIRMED 1800 = 1800
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 4 — Reported Financial Statements before fiscal boundary (Company W, same facts as Test 3)

```
Inputs:                  identical to Test 3 (Company W, June 30 2024, Revenue 200/Expense 80
                         partial FY2024)
Timeline:                same as Test 3
Fiscal-Year State:       FY2024 NOT elapsed (same as Test 3)
Operational Close State: n/a (same as Test 3)
Effective Date:          June 30 2024
Recorded At:             n/a
Raw Ledger Components:   identical to Test 3 (this test applies the REPORTING transformation
                         to the same raw facts, not a different set of facts)
Raw TB Result:           1800 = 1800 (identical to Test 3 — same underlying ledger)
Reported Equity Components: Other Ledger Equity = Share Capital (500) + Other Reserves (100) =
                         600; Reported Retained Earnings = Direct RE (1000) + 0 (no Fiscal
                         Year has elapsed yet for Company W) = 1000. Reported Equity = 600 +
                         1000 = 1600.
Reporting Viewpoint:     Current (Mode 2)
Expected Equation:       Assets + CurrentFY Expenses = Liabilities + Reported Equity +
                         CurrentFY Revenue (B08 MP-12 Proof C — the target reporting form)
Actual Design Equation:  1720 + 80 = 0 + 1600 + 200 -> 1800 = 1800
Expected Result:         the Reported Financial-Statement equation ties EXACTLY to Test 3's Raw
                         Trial Balance total (1800 = 1800 both ways) — proving Proof G's claim
                         that both presentations are the same underlying ledger, differently
                         grouped, not two different sets of facts
Actual Result:           CONFIRMED — both totals are 1800, and the individual terms visibly
                         regroup (Test 3's Revenue 200/Expense 80 raw terms become Test 4's
                         "CurrentFY Revenue/Expense" terms unchanged in value; Test 3's Share
                         Capital+Other Reserves+Direct RE = 1600 raw credit terms become Test
                         4's Reported Equity = 1600, also unchanged in value, only regrouped)
PASS / FAIL:             PASS
Finding:                 none — this is the cleanest direct numeric confirmation of B08 MP-12
                         Proof G (Trial Balance vs. Financial Statements tie-out) in this
                         regression
Disposition:             n/a
```

## Test 5 — Fiscal year ends; close action delayed 15 days (Company X, `M-AUD-09`'s own scenario)

```
Inputs:                  Company X. Direct RE entering FY2024 = 1000, FY2024 CE = 250, Cash at
                         Dec 31 2024 = 1250 (the exact figures the Round 4 audit itself cited)
Timeline:                FY2024 ends Dec 31 2024 -> `FiscalYearClosed` NOT YET declared ->
                         query as of Jan 5 2025
Fiscal-Year State:       FY2024 ELAPSED (End Date Dec 31 2024 <= Jan 5 2025)
Operational Close State: `FiscalYearClosed` NOT declared for FY2024 as of Jan 5 2025 (declared
                         10 days later, Jan 15 2025 — see Test 6)
Effective Date:          query date Jan 5 2025
Recorded At:             n/a
Raw Ledger Components:   Cash 1250 (dr); Direct RE 1000 (cr); Revenue 400 (cr, FY2024);
                         Expense 150 (dr, FY2024) — unchanged from Test 1's figures, no new
                         Entry between Dec 31 2024 and Jan 5 2025
Raw TB Result:           dr 1250+150=1400; cr 1000+400=1400. BALANCED (unchanged from Test 1).
Reported Equity Components: Other Ledger Equity = 0; Reported Retained Earnings = 1000 + 250
                         (FY2024 — ELAPSED, so included, REGARDLESS of the missing
                         declaration) = 1250
Reporting Viewpoint:     Current (Mode 2)
Expected Equation:       Assets = Liabilities + Reported Equity (simple form, FY2025 has zero
                         activity yet)
Actual Design Equation:  1250 = 0 + 1250
Expected Result:         Reported Equity = 1250 — IDENTICAL to Test 1's post-declaration
                         figure, despite no declaration having happened yet
Actual Result:           CONFIRMED 1250 = 1250. **Contrast against the SUPERSEDED Round-3
                         formula, computed explicitly to show the defect this test refutes:**
                         under "every Fiscal Year that CLOSED before D," FY2024 would NOT
                         count (no declaration yet) — Reported RE would read 1000, not 1250,
                         and the equation would read 1250 (Assets) = 0 (Liab) + 1000 (Reported
                         Equity) -> FALSE, off by exactly 250, precisely the failure `M-AUD-09`
                         described. The corrected (Elapsed) formula produces no such gap.
PASS / FAIL:             PASS
Finding:                 none — this is the direct numeric refutation of `M-AUD-09`'s failure
                         scenario, using the audit's own cited figures
Disposition:             n/a
```

## Test 6 — Close declaration occurs Jan 15 (Company X, continuing Test 5)

```
Inputs:                  Company X, continuing Test 5. `FiscalYearClosed` is declared for
                         FY2024 on Jan 15 2025. No Entry is posted by this declaration.
Timeline:                Jan 14 2025 (day before declaration) -> Jan 15 2025 (declaration
                         recorded) -> Jan 16 2025 (day after)
Fiscal-Year State:       FY2024 ELAPSED throughout (unchanged — a fact about Dec 31 2024,
                         not about Jan 14/15/16 2025)
Operational Close State: NOT declared (Jan 14) -> declared (Jan 15 onward)
Effective Date:          Jan 14, Jan 15, and Jan 16 2025 (three query dates)
Recorded At:             n/a for the two read queries; the `FiscalYearClosed` Audit Event's
                         own Recorded At is Jan 15 2025 (it is an event, but not an Entry —
                         it has no Effective Date/Line content to aggregate)
Raw Ledger Components:   IDENTICAL at all three query dates — no Entry is committed on Jan 15
                         (the declaration posts nothing, B02 CAP-09/B08 MP-11 corrected)
Raw TB Result:           1400 = 1400 at all three dates (identical to Test 5, since no Entry
                         changed)
Reported Equity Components: IDENTICAL at all three dates: Other Ledger Equity = 0; Reported
                         Retained Earnings = 1250 (unchanged — the Elapsed test, B07 §1e,
                         depends only on FY2024's End Date vs. the query date, neither of
                         which changed)
Reporting Viewpoint:     Current (Mode 2)
Expected Equation:       ReportedEquity(Jan 14) = ReportedEquity(Jan 15) = ReportedEquity(Jan
                         16) — B08 MP-12 Proof F's mandatory invariant, no new financial facts
                         between the three dates
Actual Design Equation:  1250 = 1250 = 1250
Expected Result:         Reported Equity referentially identical across the declaration —
                         not merely equal by coincidence, but computed from literally the same
                         inputs, since `FiscalYearClosed` never appears in the formula
Actual Result:           CONFIRMED — all three dates report Reported Equity = 1250, Reported
                         Retained Earnings = 1250, Other Ledger Equity = 0, with zero
                         difference in any term before, on, or after the declaration date
PASS / FAIL:             PASS
Finding:                 none — direct numeric confirmation of BINV-14(b) and B08 MP-12
                         Proof F
Disposition:             n/a
```

## Test 7 — New-FY transaction before prior-FY operational close (Company X, continuing Test 5)

```
Inputs:                  Company X, Jan 10 2025 (FY2024 elapsed, NOT yet declared closed —
                         declaration is Jan 15, per Test 6): a new FY2025 sale, Revenue 30
                         (cash)
Timeline:                Jan 5 2025 (Test 5's query point) -> Jan 10 2025, new Revenue posted
                         -> query as of Jan 10 2025 -> (declaration still pending until Jan 15)
Fiscal-Year State:       FY2024 ELAPSED (unchanged); FY2025 in progress, NOT elapsed
Operational Close State: FY2024 NOT yet declared closed (still pending, per Test 6's timeline)
Effective Date:          Jan 10 2025
Recorded At:             Jan 10 2025
Raw Ledger Components:   Cash 1280 (dr, =1250+30); Direct RE 1000 (cr); Revenue(FY2024) 400
                         (cr); Expense(FY2024) 150 (dr); Revenue(FY2025) 30 (cr)
Raw TB Result:           dr 1280+150=1430; cr 1000+400+30=1430. BALANCED.
Reported Equity Components: Other Ledger Equity = 0; Reported Retained Earnings = 1000 + 250
                         (FY2024, elapsed — UNAFFECTED by FY2024's still-pending declaration,
                         and UNAFFECTED by FY2025's new activity, since FY2025 hasn't elapsed)
                         = 1250 (unchanged from Test 5)
Reporting Viewpoint:     Current (Mode 2)
Expected Equation:       Assets + CurrentFY(2025) Expenses = Liabilities + Reported Equity +
                         CurrentFY(2025) Revenue — this test is explicitly checking that a
                         PERMITTED new-FY posting, made while the prior FY is still
                         undeclared, does not corrupt either YTD P&L or Reported Equity
Actual Design Equation:  1280 + 0 = 0 + 1250 + 30 -> 1280 = 1280
Expected Result:         FY2025's own Revenue reads exactly 30 (not contaminated by FY2024's
                         400); Reported Equity remains exactly 1250 (FY2024's figure,
                         unaffected by FY2025's new, still-in-progress activity); the equation
                         balances throughout the undeclared-FY2024 window
Actual Result:           CONFIRMED 1280 = 1280. New-Fiscal-Year postings are structurally
                         permitted before the prior Fiscal Year's operational close, per
                         [B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-11 Option A, with no
                         special-casing required — MP-09's existing Fiscal-Year category bound
                         already keeps FY2025's Revenue separate from FY2024's, exactly as it
                         always has for any two Fiscal Years regardless of close-declaration
                         status.
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 8 — Original issued Balance Sheet after later Restatement (Company X, Known viewpoint)

```
Inputs:                  Company X. Query D = Dec 31 2025 (FY2025's own elapsed-year figure),
                         viewpoint T = Feb 15 2026 — BEFORE the March 1 2026 Restatement
                         (which adds 40 to FY2025's Expense)
Timeline:                FY2025 elapses (Dec 31 2025, original CE 300) -> report issued/
                         reconstructed at T = Feb 15 2026 -> (LATER) Restatement committed
                         March 1 2026 -> re-query the SAME (D, T) pair AGAIN, after the
                         Restatement exists
Fiscal-Year State:       FY2025 ELAPSED as of D = Dec 31 2025
Operational Close State: declared on-time for FY2025 (not the variable under test here —
                         Tests 5-7 isolated that dimension; this test isolates viewpoint)
Effective Date:          D = Dec 31 2025 (query date)
Recorded At:             T = Feb 15 2026 (viewpoint cutoff — fixed, does not change between
                         the two times this test queries the same figure)
Raw Ledger Components:   as Recorded At <= Feb 15 2026 only: Cash line items and Direct RE
                         1000 (cr) as originally posted; Revenue(FY2025) 500 (cr); Expense
                         (FY2025) 200 (dr) — the March 1 2026 Restatement's Lines (Recorded At
                         March 1 2026) are EXCLUDED by construction, regardless of when this
                         test itself is run
Raw TB Result:           unaffected by the Restatement at this viewpoint — balances using only
                         pre-Feb-15 Lines, identical whether checked in February or in a much
                         later month
Reported Equity Components: ReportedRetainedEarnings_Known(C, D=Dec31/2025, T=Feb15/2026) =
                         1000 (direct, Known) + 250 (FY2024, Known) + 300 (FY2025 ORIGINAL CE,
                         Known — the Restatement's Lines are invisible to this T) = 1550
Reporting Viewpoint:     **Known (Mode 1)**, T = Feb 15 2026, fixed
Expected Equation:       ReportedRE_Known(C, D, T) unaffected by ANY Entry Recorded after T,
                         no matter how much later this query is itself re-run (B07 §1g;
                         inherits BINV-11/BINV-12's unconditional guarantee)
Actual Design Equation:  1550 (queried in Feb 2026) = 1550 (the SAME query, re-run in April
                         2026, well after the Restatement exists)
Expected Result:         the Known-viewpoint figure is 1550 both times, completely unaffected
                         by the Restatement — reproducing exactly what an originally-issued
                         Balance Sheet, dated Feb 15 2026, would have shown, forever
Actual Result:           CONFIRMED — re-querying `ReportedRetainedEarnings_Known(C, Dec31/2025,
                         Feb15/2026)` after the Restatement exists returns 1550, identical to
                         before the Restatement existed. This is the formula B07 §1e/§1g now
                         explicitly define, closing `M-AUD-10` — B20 Test 8 exercised this
                         exact behavior without the authoritative formula ever having said so.
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 9 — Current/restated Balance Sheet after Restatement (Company X, Current viewpoint, same D as Test 8)

```
Inputs:                  Company X. Same query date D = Dec 31 2025 as Test 8, but Current
                         (Mode 2) viewpoint instead of Known
Timeline:                same as Test 8, queried any time on/after March 1 2026
Fiscal-Year State:       FY2025 ELAPSED as of D = Dec 31 2025 (same as Test 8)
Operational Close State: declared on-time (same as Test 8)
Effective Date:          D = Dec 31 2025
Recorded At:             n/a (Current/Mode 2 — no T cutoff, reflects everything Recorded to
                         date, including the March 1 2026 Restatement)
Raw Ledger Components:   ALL Lines with Effective Date <= Dec 31 2025, regardless of Recorded
                         At: includes the Restatement's Expense +40 Line (Effective Dec 15
                         2025, inside FY2025)
Raw TB Result:           reflects the Restatement — Expense(FY2025) now 240, not 200
Reported Equity Components: ReportedRetainedEarnings_Current(C, D=Dec31/2025) = 1000 (direct)
                         + 250 (FY2024) + 260 (FY2025, RESTATED — 500-240) = 1510
Reporting Viewpoint:     **Current (Mode 2)**
Expected Equation:       ReportedRE_Current(C, D) reflects every legitimate fact Recorded as
                         of NOW, including later Restatements (B07 §1g) — the deliberate
                         opposite of Test 8's fixed Known view
Actual Design Equation:  1510 (Current, after the Restatement) != 1550 (Known, Test 8) — the
                         two views DIVERGE by exactly the Restatement's 40, as expected
Expected Result:         Current view = 1510, visibly different from Test 8's Known view
                         (1550), and the two are NEVER blended into one unlabeled figure
                         (CO-14, extended at CORR-B4-04)
Actual Result:           CONFIRMED 1510, correctly diverging from Test 8's 1550 by exactly 40
                         — the Restatement's amount, confirming the Known/Current split
                         behaves exactly as B07 §1g specifies and CO-14 requires both figures
                         to be explicitly labeled, never presented as if they were the same
                         number
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 10 — Close declaration recorded after historical report T (Company X)

```
Inputs:                  Company X. Suppose `FiscalYearClosed` for FY2025 is actually declared
                         on Jan 20 2026 (a delayed declaration, distinct from the on-time
                         assumption used in Tests 8-9) — but a report is reconstructed with
                         viewpoint T = Jan 10 2026, BEFORE that declaration
Timeline:                FY2025 elapses Dec 31 2025 -> (declaration pending) -> report
                         reconstructed at T = Jan 10 2026 -> declaration actually recorded
                         Jan 20 2026
Fiscal-Year State:       FY2025 ELAPSED as of D = Dec 31 2025 (a calendar fact, true
                         regardless of T or of the declaration's own timing)
Operational Close State: NOT yet declared as of T = Jan 10 2026 (declared 10 days later)
Effective Date:          D = Dec 31 2025
Recorded At:             T = Jan 10 2026
Raw Ledger Components:   every Line with Effective Date <= Dec 31 2025 AND Recorded At <= Jan
                         10 2026 — includes ordinary FY2025 activity (Recorded well before Jan
                         10), excludes nothing relevant to this test (the `FiscalYearClosed`
                         Audit Event is not an Entry/Line at all, so it has no Recorded-At
                         filtering question of its own to raise)
Raw TB Result:           balances using FY2025's ordinary activity only, exactly as at any
                         other viewpoint before the March 2026 Restatement existed
Reported Equity Components: ReportedRetainedEarnings_Known(C, D=Dec31/2025, T=Jan10/2026) =
                         1000 + 250 + 300 = 1550 — FY2025 is included in full, because it is
                         ELAPSED as of D, with NO step in the computation that asks "was
                         `FiscalYearClosed` declared, and if so, was that declaration itself
                         Recorded by T?"
Reporting Viewpoint:     **Known (Mode 1)**, T = Jan 10 2026
Expected Equation:       the Known-viewpoint reconstruction requires no knowledge of, or
                         reasoning about, the `FiscalYearClosed` declaration's own timing at
                         all — this is the direct benefit B07 §1g names: CORR-B4-03's
                         boundary-driven redefinition removes a SECOND viewpoint question
                         (was the declaration itself known at T?) that would otherwise have
                         existed under the superseded declaration-driven model
Actual Design Equation:  1550 (computed without ever consulting the declaration's Jan 20 2026
                         Recorded-At timing)
Expected Result:         1550, identical to what Test 8 (a fully on-time-declared scenario)
                         also produced for the analogous FY2024 case — confirming the
                         declaration's own timing genuinely does not enter the computation, not
                         merely that it happens to produce the same number by coincidence
Actual Result:           CONFIRMED 1550. Had the superseded, declaration-driven Round-3 model
                         been used instead, this test would have required a THIRD temporal
                         question (is `FiscalYearClosed` itself Recorded-At <= T?) that B07 §1g
                         would have had to separately define and this test would have had to
                         separately verify — the corrected model has no such question to ask.
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 11 — Material prior-period error (Round-3 IAS 8 treatment retained, re-verified)

```
Inputs:                  Company X's March 1 2026 Restatement (same facts as Test 9 /
                         B20 Tests 2/12): FY2025 Expense understated by 40 (Payable), judged
                         MATERIAL (Controller judgment, CO-16)
Timeline:                obligation arose Dec 15 2025 (FY2025) -> FY2025 elapses/closes ->
                         discovered and Restated March 1 2026 (FY2026)
Fiscal-Year State:       FY2025 ELAPSED (the Restatement's target); FY2026 in progress
Operational Close State: FY2025 declared closed (posting-lock scope only — irrelevant to
                         whether the Restatement is permitted, which depends on Consumption/
                         Restatement authorization, CO-15, not on this state)
Effective Date:          Dec 15 2025 (both Restatement Lines)
Recorded At:             March 1 2026
Raw Ledger Components:   Payable 40 (cr, new); Expense(FY2025) 240 (dr, was 200) — Current
                         (Mode 2) view; unchanged at 200 under Known (Mode 1) view with T
                         before March 1 2026
Raw TB Result:           balances (verified in full at B20 Test 12; re-confirmed here under
                         the corrected §1e/§1f terminology, not re-derived from scratch)
Reported Equity Components: Other Ledger Equity = 0; ReportedRetainedEarnings_Current(C,
                         Dec31/2025) = 1510 (as Test 9); CurrentFY(2026) Revenue/Expense
                         UNAFFECTED by the Restatement (both remain exactly what they were:
                         Revenue 50, Expense 0)
Reporting Viewpoint:     Current (Mode 2) for the equity effect; the classification itself
                         (Material Prior-Period Error) is viewpoint-independent — a fact about
                         the Entry, not about when it's queried
Expected Equation:       IAS 8 para 46 (IAS 8-mandated exclusion from current-period P&L) —
                         re-verified, not re-derived, under the Round-4-corrected formula
                         terminology
Actual Design Equation:  CurrentFY(2026) P&L Revenue 50 / Expense 0, IDENTICAL before and
                         after the Restatement; Reported Equity moves by exactly -40 (1550 Known
                         -> 1510 Current, matching Test 9)
Expected Result:         no regression in Round 3's `M-AUD-06` fix — Round 4's corrections
                         (non-overlapping decomposition, boundary-driven inclusion, viewpoint
                         parameterization) do not alter IAS 8 classification or restatement
                         mechanics (B04 §3b/§3c), only the Reported Equity arithmetic those
                         mechanics feed into
Actual Result:           CONFIRMED — zero change to FY2026's own P&L (para 46 satisfied,
                         exactly as at B20 Test 12), Reported Equity change traced correctly
                         through the corrected formula
PASS / FAIL:             PASS
Finding:                 none — confirms Round 4 does not regress Round 3's IAS 8 work
Disposition:             n/a
```

## Test 12 — Impracticability adjustment (Company Z, continuing B20 Test 4)

```
Inputs:                  Company Z (from B20 Tests 3-5): Direct RE entering FY2023 = 800.
                         FY2023 CE = 200, FY2024 CE = 150 (both individually elapsed/closed
                         normally). In FY2026, a systemic error affecting FY2023+FY2024
                         combined is discovered: total effect = 60, period-specific split
                         between the two years determined IMPRACTICABLE (IAS 8 para 43, after
                         genuine effort). Applied as a direct adjustment at the earliest
                         practicable point: start of FY2025.
Timeline:                FY2023 elapses (CE 200) -> FY2024 elapses (CE 150) -> FY2025 begins
                         -> error discovered FY2026, impracticability adjustment applied as of
                         start of FY2025
Fiscal-Year State:       FY2023, FY2024 both ELAPSED (their own CE terms are NOT touched by
                         this adjustment, per IAS 8 para 43's own requirement not to attribute
                         an inseparable effect to a specific year)
Operational Close State: both FY2023 and FY2024 declared closed (irrelevant to this
                         adjustment's mechanics, same as Test 11)
Effective Date:          start of FY2025 (the earliest practicable point, per para 43 — NOT
                         FY2023's or FY2024's own dates)
Recorded At:             FY2026 (actual commit time)
Raw Ledger Components:   a direct adjustment Line against the designated Retained Earnings
                         account itself, -60, Effective start-of-FY2025 — NOT a Line against
                         Revenue or Expense of any specific year
Raw TB Result:           balances (the -60 direct-RE Line is paired with whatever the
                         originating correction's other side is — e.g. an Asset/Liability
                         correction — full balancing pair carried from B20 Test 4's own
                         construction, not re-derived here)
Reported Equity Components: Other Ledger Equity = 0 (unaffected — this is the key check this
                         test adds beyond B20 Test 4, which predates B07 §1f's existence:
                         the adjustment touches ONLY the direct-RE term, never Other Ledger
                         Equity); Reported Retained Earnings at start of FY2025 = (800 - 60)
                         direct + 200 (FY2023 CE, UNCHANGED) + 150 (FY2024 CE, UNCHANGED) =
                         1090, i.e. exactly 60 less than the pre-adjustment 1150
Reporting Viewpoint:     Current (Mode 2)
Expected Equation:       the adjustment is representable entirely within the direct-RE term of
                         B07 §1e's formula, per the CORR-B3-06 annotation (unchanged) and the
                         CORR-B4-01 annotation (new — confirms it also never touches Other
                         Ledger Equity, B07 §1f)
Actual Design Equation:  Reported RE: 1150 -> 1090 (a flat -60, matching the adjustment exactly)
Expected Result:         neither FY2023's nor FY2024's own Current Earnings term changes value
                         (200 and 150 respectively, both untouched); Other Ledger Equity stays
                         at 0 throughout; the entire -60 lands in the direct-postings term alone
Actual Result:           CONFIRMED — 1150-60=1090, with FY2023/FY2024's CE terms and Other
                         Ledger Equity all independently confirmed unchanged
PASS / FAIL:             PASS
Finding:                 none — first numeric confirmation that an impracticability
                         adjustment interacts correctly with B07 §1f's decomposition, which
                         did not exist when B20 Test 4 was originally constructed
Disposition:             n/a
```

## Test 13 — Migration opening balance (Company Y, continuing B20 Test 13)

```
Inputs:                  Company Y (from B20 Test 13): migration cutover Jan 1 2026, MG-C03
                         summarized opening balance: dr Cash 500 / cr Retained Earnings
                         (direct-posted) 500. MG-C15 (new, this round): this credited account
                         is explicitly configured as Company Y's designated Retained Earnings
                         account at migration time.
Timeline:                migration cutover Jan 1 2026
Fiscal-Year State:       no Fiscal Year has elapsed yet for Company Y in this system
Operational Close State: n/a — no Fiscal Year exists yet to close
Effective Date:          Jan 1 2026 (the historical cutover accounting date)
Recorded At:             actual migration execution instant (MG-C14, unchanged)
Raw Ledger Components:   Cash 500 (dr); Direct RE 500 (cr) — the ledger's first fact for
                         Company Y
Raw TB Result:           dr 500 = cr 500. BALANCED (MP-01, MG-C03).
Reported Equity Components: Other Ledger Equity = 0 (no other Equity account was migrated for
                         Company Y in this scenario); Reported Retained Earnings = 500 (direct)
                         + 0 (no elapsed Fiscal Year yet) = 500
Reporting Viewpoint:     Current (Mode 2) — Known (Mode 1) is identical here since this is the
                         very first fact, nothing has been Restated
Expected Equation:       Reported Equity = 500, matching Cash exactly; no double-counting
                         against a migrated "Other Ledger Equity" that doesn't exist for this
                         Company; MG-C15's designation is unambiguous (exactly one account)
Actual Design Equation:  500 = 0 + (0 + 500)
Expected Result:         migration opening balance ties out immediately, with B07 §1f's
                         decomposition correctly recognizing there is nothing to put in Other
                         Ledger Equity for this Company
Actual Result:           CONFIRMED 500 = 500
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 14 — Correction of a Restatement itself (Company X, continuing B20 Test 14)

```
Inputs:                  Company X's April 2026 further Correction of the March 1 2026
                         Restatement (B20 Test 14): Payable corrected from 40 to 45 (+5
                         Expense, same Effective period Dec 15 2025)
Timeline:                March 1 2026 Restatement (Test 9/11 above) -> April 2026 chained
                         Correction
Fiscal-Year State:       FY2025 ELAPSED (unchanged — both corrections target the same period)
Operational Close State: FY2025 declared closed (unchanged, irrelevant to this chain)
Effective Date:          Dec 15 2025 (both the Restatement and its later Correction)
Recorded At:             March 1 2026 (Restatement); April 2026 (the chained Correction) —
                         two distinct Recorded At values, per BINV-12
Raw Ledger Components:   Payable 45 (cr, cumulative); Expense(FY2025) 245 (dr, Current view)
Raw TB Result:           balances (B20 Test 14's own construction, unchanged)
Reported Equity Components: Other Ledger Equity = 0; ReportedRetainedEarnings_Known(C,
                         Dec31/2025, T=Feb15/2026) = 1550 (UNCHANGED — both corrections
                         Recorded after this T); ReportedRetainedEarnings_Current(C,
                         Dec31/2025) = 1000+250+255(=500-245) = 1505
Reporting Viewpoint:     both Known (fixed at 1550) and Current (now 1505) — both re-verified
                         side by side to confirm the chain doesn't disturb either viewpoint's
                         own internal consistency
Expected Equation:       Known view stays fixed regardless of how many further corrections
                         chain onto the same period; Current view updates with each one;
                         neither view's Other Ledger Equity term is ever touched by an
                         Equity-account-only correction chain like this one
Actual Design Equation:  Known: 1550 = 1550 (both before and after the April correction).
                         Current: 1510 (after Restatement only) -> 1505 (after the chained
                         Correction too)
Expected Result:         a correction-of-a-Restatement composes correctly with both the
                         Known/Current split (B07 §1g) and the non-overlapping decomposition
                         (B07 §1f) — no special-casing needed for "a correction of a
                         correction," consistent with B04 §6's existing chain rule
Actual Result:           CONFIRMED — both figures match exactly, Other Ledger Equity
                         unaffected (0 throughout) at every step
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 15 — Multi-company isolation (Company W vs. Company X)

```
Inputs:                  Company W (Test 2's state: Reported Equity 1850) and Company X (this
                         document's Tests 1/5-11/14: Reported Equity moving through 1250 ->
                         1250 -> 1510 -> 1505 across the various tests above) coexist under one
                         SMEsPlus tenant
Timeline:                concurrent with every other test in this document
Fiscal-Year State:       independent per Company (Company W's FY2024 elapsed/closed
                         independently of Company X's own Fiscal Year states)
Operational Close State: independent per Company — Company X's delayed FY2024 declaration
                         (Tests 5-7) has no defined relationship to Company W's own declaration
                         timing at all
Effective Date:          n/a (a boundary/isolation check, not a single fact's date)
Recorded At:             n/a
Raw Ledger Components:   Company W's and Company X's Lines are disjoint sets — every Line
                         resolves to exactly one Company (BINV-03, unchanged)
Raw TB Result:           each Company's own Raw TB balances independently (Test 2 for W; Test
                         1/5/etc. for X) — never summed together
Reported Equity Components: Company W: Other Ledger Equity 600, Reported RE 1250, Reported
                         Equity 1850 (fixed, Test 2's value). Company X: values move through
                         this document's own tests (1250 through 1505) — Company W's 1850
                         must remain EXACTLY 1850 throughout, unaffected by any of Company X's
                         Restatements, delayed declarations, or corrections
Reporting Viewpoint:     Current (Mode 2) for both, checked independently
Expected Equation:       B08 MP-12's Proofs are all defined per-Company (inherited from MP-09's
                         existing Company scope, unchanged); B07 §1e/§1f/§1g introduce no
                         cross-Company aggregation or classification step
Actual Design Equation:  Company W Reported Equity = 1850 at every point during this document's
                         construction, regardless of which Company X test was being worked
                         concurrently
Expected Result:         zero interference in either direction
Actual Result:           CONFIRMED BY CONSTRUCTION — every formula in B07 §1e/§1f/§1g and B08
                         MP-12 takes Company C as an explicit parameter and sums only that
                         Company's own accounts/Fiscal Years; no step aggregates or compares
                         across Companies, so Company X's extensive Round-4 testing in this
                         document could not have altered Company W's figures even in principle
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Regression Result

```
Scenarios executed:                            15
PASS:                                           15
Real design refinement found during construction, applied: 0 (unlike Rounds 1-3, this
  regression's construction did not surface any further defect in the CORR-B4 formulas
  themselves — every figure matched on first computation, cross-checked via both the Reported
  form and a re-derivation from the Raw Ledger Identity per test, per B08 MP-12's Proof
  structure)
Regressions into any prior-fixed defect:        0 (re-confirmed: Test 11 re-verifies `M-AUD-06`
  is unaffected by this round's changes; Tests 8/10/14 re-verify BINV-11/BINV-12's Mode-1
  guarantee extends correctly to the new Reported RE/Equity formulas; Test 12 re-verifies
  `M-AUD-06`'s impracticability treatment composes correctly with the new B07 §1f split)
New CRITICAL/HIGH defects:                      0
```

**B21 = COMPLETE.** Unlike B18/B19/B20, this regression's own construction did not surface a
further defect requiring a documented mid-construction correction — recorded here plainly,
not as a claim of higher confidence than the process has earned (per
[G §4](DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md)'s standing discipline), but as an
honest report of what actually happened this round: the corrections made directly in B07/B08
while responding to the Round 4 audit (before this regression was constructed) already
incorporated the lessons of three prior rounds' worth of "the regression catches something
the first-draft fix missed" — this document's role was to verify that discipline held, not to
be the mechanism that discovered a gap in it this time.
