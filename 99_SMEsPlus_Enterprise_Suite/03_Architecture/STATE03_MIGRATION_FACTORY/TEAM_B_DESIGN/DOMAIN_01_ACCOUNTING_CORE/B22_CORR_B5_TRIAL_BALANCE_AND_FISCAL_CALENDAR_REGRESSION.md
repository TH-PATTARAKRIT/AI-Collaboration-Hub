# B22 — CORR-B5 Trial Balance & Fiscal Calendar Regression

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-30-MIG-B-D01-CORR5-001 |
| Source of truth | CORR5-001 directive §8 — 15 mandatory scenarios, tested against the CORR-B5-corrected design (B08 MP-09 renamed/split, MP-12 Proof G rebuilt G1-G4; B07 §1h new; B05 BINV-15/16 new; B13 DT-12 new) |
| Personas | Senior Accountant, Financial Controller, External Auditor, Historical Reporting Reviewer, Fiscal Calendar Administrator, Migration Architect, SaaS Domain Architect, Accounting Systems Architect, Clean-room Reviewer |
| Result | **15/15 PASS. No in-round refinement required — every worked figure matched the corrected B07/B08 formulas on first computation, cross-checked against both the running companies' own prior-round figures (B20/B21) and independent re-derivation from the Raw Ledger Identity.** |

Money amounts below are illustrative units. Four companies are used: **Company X** (continues
from B20/B21 — single Equity account), **Company W** (continues from B21 Test 2 — multiple
Equity accounts), **Company Y** (continues from B20/B21 — migration example), and Company X
again for the Fiscal Calendar tests (Tests 12-15), since it already has genuine, multi-year
reliance built up across every prior round's testing — exactly the precondition Tests 12-13
need. Per the directive's required schema, every test below records: Inputs / Timeline / Query
Date D / Knowledge Cutoff T (if applicable) / Fiscal-Year Definition / Fiscal-Year Definition
Status/Version / Raw Cumulative Ledger Components / Raw Cumulative TB Result / Current-FY
Activity Components / Derived Presentation Components / Reported Equity Components / Reporting
Viewpoint / Expected Equation / Actual Design Equation / Expected Result / Actual Result /
PASS-FAIL / Finding / Disposition.

## Company X — Running Balances (continued from B20/B21; FY2024 boundary version history added this document)

```
(from B20/B21) Baseline start FY2024 (Jan1 2024): Cash 1000, Direct RE 1000 (only account)
(from B20/B21) FY2024: Revenue 400, Expense 150 -> CE 250. Elapsed Dec31/2024. Cash = 1250.
(from B20/B21) FY2025: Revenue 500, Expense 200 -> CE 300. Elapsed Dec31/2025. Cash = 1550.
(from B20/B21) FY2026 Jan15: Revenue 50 (cash). Cash = 1600.
(from B20/B21) FY2025 Restatement, March 1 2026: Expense +40 (Payable), Effective Dec 15
  2025, MATERIAL.
(NEW, this document) FY2024's boundary: Version 1 = Jan1-Dec31 2024, set at Company X's
  original setup (2023-12-01), never changed until Test 12.
(NEW, this document) Jan10 2025: an additional FY2025 Revenue 30 (cash), for Test 7 only —
  Cash reaches 1280 at that specific point in the timeline before continuing to the March
  2026 Restatement above.
```

## Test 1 — Mid first Fiscal Year cumulative Raw TB

```
Inputs:                  Company X, FY2024 (its first-ever Fiscal Year) half-elapsed: as of
                         June 30 2024, Revenue 200 and Expense 75 posted so far (half of
                         FY2024's eventual full-year 400/150)
Timeline:                Jan1 2024 setup -> partial FY2024 activity -> query June 30 2024
Query Date D:            June 30 2024
Knowledge Cutoff T:      n/a (Current viewpoint)
Fiscal-Year Definition:  FY2024 = Jan1-Dec31 2024
Fiscal-Year Definition Status/Version: Version 1 (original, set 2023-12-01, unchanged)
Raw Cumulative Ledger Components: Cash 1125 (dr, =1000+200-75); Direct RE 1000 (cr);
                         Revenue 200 (cr, cumulative — ledger inception through D, no
                         Fiscal-Year bound); Expense 75 (dr, cumulative)
Raw Cumulative TB Result: dr 1125+75=1200; cr 1000+200=1200. BALANCED — MP-09
                         `CumulativeAccountBalance_Current`, every category on one horizon
                         (MP-12 Proof G1)
Current-FY Activity Components: Revenue(FY2024)=200; Expense(FY2024)=75 (MP-09
                         `FiscalYearActivity_Current`)
Derived Presentation Components: n/a for this test (see Test 2)
Reported Equity Components: Other Ledger Equity = 0; Reported Retained Earnings = 1000
                         (direct) + 0 (no Fiscal Year has elapsed yet) = 1000
Reporting Viewpoint:     Current
Expected Equation:       Raw Cumulative TB balances directly (Proof G1)
Actual Design Equation:  1200 = 1200
Expected Result:         balanced, unconditionally
Actual Result:           CONFIRMED
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 2 — Mid first Fiscal Year current-FY reporting activity

```
Inputs:                  identical facts to Test 1 (Company X, June 30 2024)
Timeline:                same as Test 1
Query Date D:            June 30 2024
Knowledge Cutoff T:      n/a
Fiscal-Year Definition:  FY2024 = Jan1-Dec31 2024 (Version 1)
Fiscal-Year Definition Status/Version: Version 1, unchanged
Raw Cumulative Ledger Components: identical to Test 1
Raw Cumulative TB Result: 1200 = 1200 (identical to Test 1 — same underlying ledger)
Current-FY Activity Components: Revenue(FY2024)=200; Expense(FY2024)=75 — NUMERICALLY
                         IDENTICAL to the cumulative figures in Test 1
Derived Presentation Components: none needed — Test 1's Raw Cumulative TB already balances,
                         so no bridge line is required at this point in Company X's history
Reported Equity Components: same as Test 1 — Other Ledger Equity 0, Reported RE 1000
Reporting Viewpoint:     Current
Expected Equation:       Current-Fiscal-Year Activity is expected to coincide EXACTLY with
                         Cumulative Balance for Revenue/Expense during a company's first-ever
                         Fiscal Year — not because the two formulas are the same formula, but
                         because nothing precedes FY2024 in this ledger for Fiscal-Year-bounding
                         to exclude. This is the honest, correctly-reasoned boundary case, not
                         a forced or artificial "distinct" result.
Actual Design Equation:  CumulativeAccountBalance_Current(Revenue,C,D) = 200 =
                         FiscalYearActivity_Current(Revenue,C,D); likewise Expense: 75 = 75
Expected Result:         the two formulas' outputs coincide during FY2024 specifically, and
                         are expected to diverge starting only from FY2025 onward (Test 3)
Actual Result:           CONFIRMED — coincidence during FY2024, by construction, not by
                         coincidence of arithmetic; the divergence is demonstrated directly
                         in Test 3 below, once a second Fiscal Year exists to be excluded from
PASS / FAIL:             PASS
Finding:                 none — this test's role is to show the formulas behave correctly
                         (coincide) exactly when the math says they must, avoiding a false
                         impression that "distinct" was achieved by construction rather than
                         genuinely earned
Disposition:             n/a
```

## Test 3 — First day of second Fiscal Year (the audit's own exact numbers)

```
Inputs:                  Company X, FY2024 complete (Revenue 400, Expense 150, CE 250,
                         Cash 1250) — the exact figures ChatGPT's Round 5 audit itself cited
Timeline:                FY2024 elapses Dec31/2024 -> query Jan5/2025 (FY2025 in progress,
                         no activity yet)
Query Date D:            Jan 5 2025
Knowledge Cutoff T:      n/a (Current)
Fiscal-Year Definition:  FY2024 = Jan1-Dec31 2024 (Version 1); FY2025 = Jan1-Dec31 2025
                         (Version 1)
Fiscal-Year Definition Status/Version: both Version 1, unchanged
Raw Cumulative Ledger Components: Cash 1250 (dr); Direct RE 1000 (cr); Revenue 400 (cr,
                         cumulative, NOT Fiscal-Year-bounded); Expense 150 (dr, cumulative)
Raw Cumulative TB Result: dr 1250+150=1400; cr 1000+400=1400. BALANCED (MP-12 Proof G1) —
                         this is the true Raw Cumulative Trial Balance
Current-FY Activity Components: Revenue(FY2025)=0; Expense(FY2025)=0 (nothing dated into
                         FY2025 yet) — mixed with the cumulative Balance Sheet figures (Cash
                         1250, Direct RE 1000), this gives the Current-Fiscal-Year Reporting
                         Balance (MP-12 Proof G2): dr 1250+0=1250; cr 1000+0=1000 — **OFF BY
                         EXACTLY 250, NOT BALANCED** — this is the audit's own traced failure
                         case, now correctly labeled as a non-balanced reporting view rather
                         than mislabeled "the Raw Trial Balance"
Derived Presentation Components: "Accumulated Elapsed-Fiscal-Year Earnings" = 250 (FY2024's
                         Current Earnings, MP-12 Proof G3) — DERIVED PRESENTATION COMPONENT,
                         NOT A POSTED FINANCIAL FACT
Reported Equity Components: Other Ledger Equity = 0; Reported Retained Earnings = 1000
                         (direct) + 250 (FY2024, Elapsed) = 1250; Reported Equity = 1250
Reporting Viewpoint:     Current
Expected Equation:       G1 balances (1400=1400); G2 does NOT balance on its own (1250 vs
                         1000, explicitly not claimed to); G2 + the 250 bridge line balances
                         (Proof G3); the simple reporting form Assets = Liabilities + Reported
                         Equity holds using Reported Equity specifically (Proof C)
Actual Design Equation:  G1: 1400=1400. G2 alone: 1250 != 1000 (confirmed imbalance, exactly
                         250, exactly as traced). G3 (G2 + bridge): 1250 = 1000+250 = 1250.
                         Reporting form: 1250 = 0 + 1250.
Expected Result:         three distinct, correctly-labeled outputs, none confused with another
Actual Result:           CONFIRMED — this is the direct numeric reproduction and resolution of
                         `M-AUD-11`'s exact failure case
PASS / FAIL:             PASS
Finding:                 none — this is the corrected replacement for B21 Test 5's own figures,
                         which were numerically identical but never previously labeled this
                         precisely
Disposition:             n/a
```

## Test 4 — Balanced presentation TB bridge (same D, explicit tie-out)

```
Inputs:                  identical facts to Test 3
Timeline:                same as Test 3
Query Date D:            Jan 5 2025
Knowledge Cutoff T:      n/a
Fiscal-Year Definition:  same as Test 3
Fiscal-Year Definition Status/Version: both Version 1
Raw Cumulative Ledger Components: same as Test 3 (1400=1400)
Raw Cumulative TB Result: 1400 = 1400 (cross-reference to Test 3, not re-derived)
Current-FY Activity Components: same as Test 3 (Assets 1250 dr, Direct RE 1000 cr,
                         Revenue/Expense(FY2025) both 0) — G2, still not balanced alone
Derived Presentation Components: "Accumulated Elapsed-Fiscal-Year Earnings" = 250, added to
                         G2's credit side, labeled DERIVED PRESENTATION COMPONENT — NOT A
                         POSTED FINANCIAL FACT
Reported Equity Components: same as Test 3 (Reported Equity = 1250)
Reporting Viewpoint:     Current
Expected Equation:       G2 + exactly one bridge line = balanced (MP-12 Proof G3); the bridge
                         value equals Reported Retained Earnings' own second summand exactly
                         once, never duplicated
Actual Design Equation:  dr 1250 (Assets) + 0 (FY2025 Expense) = 1250
                         cr 1000 (Direct RE) + 0 (FY2025 Revenue) + 250 (bridge) = 1250
Expected Result:         balanced, with the bridge appearing exactly once and carrying its
                         required label
Actual Result:           CONFIRMED 1250 = 1250. The bridge (250) is verified identical to
                         Reported Retained Earnings' elapsed-Fiscal-Year summand (Test 3) —
                         the same quantity, reused, not a fourth number to keep synchronized
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 5 — Delayed FiscalYearClosed declaration: all three outputs remain coherent

```
Inputs:                  Company X, same as Test 3, but with `FiscalYearClosed` for FY2024
                         explicitly NOT YET declared as of the query date (declared 10 days
                         later, Jan15/2025 — see Test 6)
Timeline:                FY2024 elapses Dec31/2024 -> `FiscalYearClosed` NOT declared ->
                         query Jan5/2025
Query Date D:            Jan 5 2025
Knowledge Cutoff T:      n/a
Fiscal-Year Definition:  same as Test 3
Fiscal-Year Definition Status/Version: both Version 1
Raw Cumulative Ledger Components: identical to Test 3 — UNAFFECTED by the missing declaration
Raw Cumulative TB Result: 1400 = 1400 (G1, unaffected by declaration status)
Current-FY Activity Components: identical to Test 3 (G2, still off by 250 — the SAME gap,
                         still correctly never called "balanced")
Derived Presentation Components: identical to Test 3 (bridge = 250, G3 balances)
Reported Equity Components: identical to Test 3 (Reported Equity = 1250) — **FY2024 IS
                         included, because it is ELAPSED, regardless of the missing
                         declaration** (B07 §1e)
Reporting Viewpoint:     Current
Expected Equation:       all of G1/G2(labeled correctly)/G3/Reported-Equity are IDENTICAL to
                         Test 3's declared-on-time figures — the declaration was never an
                         input to any of them
Actual Design Equation:  G1: 1400=1400; G2: 1250 vs 1000 (same gap); G3: 1250=1250; Reported
                         Equity: 1250, matching Test 3 exactly
Expected Result:         no output depends on whether `FiscalYearClosed` has been declared
Actual Result:           CONFIRMED — every figure in this test is identical to Test 3's,
                         confirming mathematical coherence throughout the undeclared window
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 6 — Declaration occurs with no financial facts: no value changes

```
Inputs:                  Company X, continuing Test 5. `FiscalYearClosed` for FY2024 is
                         declared Jan15/2025. No Entry is posted by this declaration.
Timeline:                Jan14/2025 (undeclared) -> Jan15/2025 (declared) -> Jan16/2025
Query Date D:            Jan 14, Jan 15, and Jan 16 2025 (three query points)
Knowledge Cutoff T:      n/a
Fiscal-Year Definition:  same as Test 3
Fiscal-Year Definition Status/Version: both Version 1, unchanged across all three dates
Raw Cumulative Ledger Components: IDENTICAL at all three dates — no Entry committed on
                         Jan15 (the declaration posts nothing)
Raw Cumulative TB Result: 1400 = 1400 at all three dates
Current-FY Activity Components: IDENTICAL at all three dates
Derived Presentation Components: bridge = 250 at all three dates, unchanged
Reported Equity Components: Reported Equity = 1250 at all three dates, unchanged
Reporting Viewpoint:     Current
Expected Equation:       ReportedEquity(Jan14) = ReportedEquity(Jan15) = ReportedEquity(Jan16)
                         — MP-12 Proof F's mandatory invariant, re-verified here alongside the
                         G1/G2/G3 outputs specifically
Actual Design Equation:  1250 = 1250 = 1250 (and G1/G2/G3 likewise unchanged across all three)
Expected Result:         referentially identical, not merely coincidentally equal
Actual Result:           CONFIRMED
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 7 — Current-FY transaction after boundary: all outputs reconcile

```
Inputs:                  Company X, Jan10/2025 (FY2024 elapsed, still undeclared per Test
                         5/6's timeline): a new FY2025 sale, Revenue 30 (cash)
Timeline:                Jan5/2025 (Test 5) -> Jan10/2025, new Revenue posted -> query
                         Jan10/2025 (declaration still pending until Jan15, Test 6)
Query Date D:            Jan 10 2025
Knowledge Cutoff T:      n/a
Fiscal-Year Definition:  same as Test 3
Fiscal-Year Definition Status/Version: both Version 1
Raw Cumulative Ledger Components: Cash 1280 (dr, =1250+30); Direct RE 1000 (cr); Revenue
                         430 (cr, cumulative — FY2024's 400 + FY2025's 30 so far); Expense
                         150 (dr, cumulative, unchanged)
Raw Cumulative TB Result: dr 1280+150=1430; cr 1000+430=1430. BALANCED (G1)
Current-FY Activity Components: Revenue(FY2025)=30 (only the new sale — NOT 430); Expense
                         (FY2025)=0. Mixed with Cash 1280/Direct RE 1000: G2 = dr 1280+0=1280;
                         cr 1000+30=1030 — off by 250, the SAME gap as Test 3/5, UNAFFECTED
                         by the new FY2025 activity (confirming the gap is entirely
                         attributable to FY2024's stranded earnings, not to anything about
                         FY2025 itself)
Derived Presentation Components: bridge = 250 still (FY2024's Current Earnings, unchanged by
                         FY2025's new activity)
Reported Equity Components: Other Ledger Equity 0; Reported Retained Earnings = 1000+250=1250
                         (unchanged — FY2025 hasn't elapsed, so its in-progress 30 isn't
                         folded in yet); Reported Equity = 1250
Reporting Viewpoint:     Current
Expected Equation:       Assets + CurrentFY Expenses = Liabilities + Reported Equity +
                         CurrentFY Revenue (Proof C) — confirming a permitted new-FY posting,
                         made while the prior FY remains undeclared, does not corrupt any
                         output
Actual Design Equation:  1280 + 0 = 0 + 1250 + 30 -> 1280 = 1280
Expected Result:         G1 balances (1430=1430); G2's gap is unchanged at 250 (not worsened,
                         not fixed, by the unrelated FY2025 activity); G3 balances (1280 =
                         1030+250); the reporting form balances (1280=1280)
Actual Result:           CONFIRMED — all four checks hold
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 8 — Later material Restatement of prior FY: Current Raw TB and Reported Equity change consistently

```
Inputs:                  Company X's March1/2026 Restatement (continuing from B20/B21): FY2025
                         Expense understated by 40 (Payable), Effective Dec15/2025, judged
                         MATERIAL (CO-16)
Timeline:                obligation arose Dec15/2025 (FY2025) -> FY2025 elapses -> Restated
                         March1/2026 (FY2026)
Query Date D:            Dec 31 2025 (FY2025's own elapsed point)
Knowledge Cutoff T:      n/a (Current — evaluated any time on/after March1/2026)
Fiscal-Year Definition:  FY2025 = Jan1-Dec31 2025 (Version 1); FY2026 = Jan1-Dec31 2026
                         (Version 1)
Fiscal-Year Definition Status/Version: both Version 1, unchanged
Raw Cumulative Ledger Components: Cash 1550 (dr, unaffected — accrual, no cash movement);
                         Payable 40 (cr, new); Direct RE 1000 (cr); Revenue 900 (cr,
                         cumulative, 400+500); Expense 390 (dr, cumulative, 150+200+40 restated)
Raw Cumulative TB Result: dr 1550+390=1940; cr 1000+40+900=1940. BALANCED (G1, Current view,
                         reflecting the Restatement)
Current-FY Activity Components: Revenue(FY2026)=0; Expense(FY2026)=0 — UNAFFECTED by the
                         Restatement, whose Effective Date (Dec15/2025) falls in FY2025, not
                         FY2026 — the direct numeric confirmation IAS 8 para 46's exclusion
                         from current-period P&L, re-verified under the corrected G1/G2
                         terminology
Derived Presentation Components: bridge (as of Dec31/2025) = 250(FY2024) + 260(FY2025
                         restated, 500-240) = 510
Reported Equity Components: Other Ledger Equity 0; Reported Retained Earnings = 1000+250+260
                         =1510; Reported Equity = 1510 — matches B21 Test 9's figure exactly,
                         re-derived here under the corrected G1/G2/G3 framework
Reporting Viewpoint:     Current
Expected Equation:       Raw Cumulative TB (Current) reflects the Restatement and balances;
                         current-period (FY2026) P&L is untouched; Reported Equity moves by
                         exactly -40 from its pre-Restatement value (1550 Known, Test 9 below)
Actual Design Equation:  G1: 1940=1940. FY2026 P&L: 0/0, unchanged. Reported Equity: 1510 (was
                         1550 Known/pre-Restatement) — a movement of exactly 40
Expected Result:         all three outputs reflect the Restatement consistently and correctly
Actual Result:           CONFIRMED
PASS / FAIL:             PASS
Finding:                 none — no regression in `M-AUD-06`'s IAS 8 treatment
Disposition:             n/a
```

## Test 9 — Known view before Restatement: original cumulative TB / Reported Equity exactly reproducible

```
Inputs:                  same underlying facts as Test 8, viewpoint T = Feb15/2026 — BEFORE
                         the March1/2026 Restatement
Timeline:                FY2025 elapses (original CE 300) -> report issued/reconstructed at
                         T=Feb15/2026 -> (LATER) Restatement committed March1/2026 -> re-query
                         the SAME (D,T) pair again, after the Restatement exists
Query Date D:            Dec 31 2025
Knowledge Cutoff T:      Feb 15 2026 (fixed)
Fiscal-Year Definition:  same as Test 8
Fiscal-Year Definition Status/Version: both Version 1
Raw Cumulative Ledger Components: as Recorded At <= Feb15/2026 only: Cash 1550, Direct RE
                         1000, Revenue 900 (cumulative), Expense 350 (cumulative — the
                         March1/2026 Restatement's Lines, Recorded March1, are EXCLUDED by
                         construction regardless of when this test itself is re-run)
Raw Cumulative TB Result: dr 1550+350=1900; cr 1000+900=1900. BALANCED (G1, Known view,
                         T=Feb15/2026) — IDENTICAL whether queried in February or, as
                         explicitly re-checked here, in a much later month after the
                         Restatement exists
Current-FY Activity Components: n/a for this test's focus (G1/Reported Equity are the
                         relevant checks)
Derived Presentation Components: bridge (Known, T=Feb15/2026) = 250(FY2024)+300(FY2025
                         original CE)=550
Reported Equity Components: ReportedRetainedEarnings_Known(C,Dec31/2025,Feb15/2026) =
                         1000+250+300=1550; ReportedEquity_Known = 1550
Reporting Viewpoint:     Known (Mode 1), T = Feb 15 2026, fixed
Expected Equation:       G1/Known and Reported Equity/Known are unaffected by ANY Entry
                         Recorded after T, no matter how much later this query is re-run
                         (B07 §1g; inherits BINV-11/12's unconditional guarantee)
Actual Design Equation:  1900=1900 (queried in Feb 2026) = 1900=1900 (the SAME query, re-run
                         in April 2026, well after the Restatement exists). Reported Equity:
                         1550 both times.
Expected Result:         permanently reproducible, diverging from Test 8's Current-view
                         figures (1940/1510) by exactly the Restatement's effect
Actual Result:           CONFIRMED — 1900/1550 (Known) vs. 1940/1510 (Current, Test 8),
                         diverging by exactly 40, as expected
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 10 — Multiple Equity accounts: no double count across Other Ledger Equity, Direct RE, and accumulated elapsed-FY earnings

```
Inputs:                  Company W (continuing B21 Test 2): Share Capital 500, Other Reserves
                         100, Direct RE 1000, FY2024 Revenue 400/Expense 150 -> CE 250
Timeline:                Day0 opening -> FY2024 elapses -> query Jan1/2025
Query Date D:            Jan 1 2025
Knowledge Cutoff T:      n/a
Fiscal-Year Definition:  FY2024 = Jan1-Dec31 2024 (Version 1)
Fiscal-Year Definition Status/Version: Version 1
Raw Cumulative Ledger Components: Cash 1850 (dr); Share Capital 500 (cr); Other Reserves 100
                         (cr); Direct RE 1000 (cr); Revenue 400 (cr, cumulative); Expense 150
                         (dr, cumulative)
Raw Cumulative TB Result: dr 1850+150=2000; cr 500+100+1000+400=2000. BALANCED (G1)
Current-FY Activity Components: Revenue(FY2025)=0; Expense(FY2025)=0 — G2: dr 1850+0=1850;
                         cr 500+100+1000+0=1600 — off by exactly 250 (the same pattern,
                         confirmed to generalize beyond the single-Equity-account case)
Derived Presentation Components: bridge = 250, added to G2: cr 1600+250=1850=dr1850. Every
                         account (Share Capital, Other Reserves, Direct RE) appears exactly
                         once across {Other Ledger Equity, Reported Retained Earnings}; the
                         bridge is a THIRD, separate, never-posted quantity, not a duplicate
                         of any of the three accounts
Reported Equity Components: Other Ledger Equity = Share Capital(500)+Other Reserves(100)=600;
                         Reported Retained Earnings = 1000+250=1250; Reported Equity =
                         600+1250=1850
Reporting Viewpoint:     Current
Expected Equation:       Assets = Liabilities + Reported Equity, with Share Capital and Other
                         Reserves counted exactly once (inside Other Ledger Equity), Direct RE
                         counted exactly once (inside Reported Retained Earnings)
Actual Design Equation:  1850 = 0 + (600+1250) = 1850
Expected Result:         no account double-counted, matching B21 Test 2's figure exactly,
                         now additionally verified against G1/G2/G3's precise terminology
Actual Result:           CONFIRMED 1850 = 1850
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 11 — Migration opening balance: no double count with derived prior-FY accumulated earnings

```
Inputs:                  Company Y (continuing B20/B21 Test 13): migration cutover Jan1/2026,
                         MG-C03 summarized opening balance: dr Cash 500 / cr Retained Earnings
                         (direct-posted, MG-C15-designated) 500
Timeline:                migration cutover Jan1/2026
Query Date D:            Jan 1 2026
Knowledge Cutoff T:      n/a
Fiscal-Year Definition:  FY2026 = Jan1-Dec31 2026 (Version 1, established at migration setup
                         — see MG-C16, always pre-reliance at the moment of setup)
Fiscal-Year Definition Status/Version: Version 1, newly established, pre-reliance at this
                         exact moment
Raw Cumulative Ledger Components: Cash 500 (dr); Direct RE 500 (cr) — the ledger's first fact
Raw Cumulative TB Result: dr 500 = cr 500. BALANCED (G1)
Current-FY Activity Components: Revenue(FY2026)=0; Expense(FY2026)=0 (nothing posted yet
                         beyond the opening balance, which is not a Revenue/Expense fact) —
                         G2 = dr 500+0=500; cr 500+0=500 — BALANCED already, because no
                         Fiscal Year has elapsed yet for Company Y (no gap exists to bridge)
Derived Presentation Components: bridge = 0 (no elapsed Fiscal Year) — confirming the bridge
                         is never a "phantom" quantity conjured from nothing; it is exactly 0
                         when nothing has accumulated to bridge
Reported Equity Components: Other Ledger Equity = 0; Reported Retained Earnings = 500
                         (direct) + 0 (no elapsed FY) = 500; Reported Equity = 500
Reporting Viewpoint:     Current
Expected Equation:       migration opening balance ties out immediately, with no double-count
                         against a derived accumulated-earnings bridge that doesn't yet exist
Actual Design Equation:  500 = 0 + (0+500)
Expected Result:         G1, G2, and Reported Equity are all IDENTICAL (500) at this specific,
                         pre-elapse moment — a distinct, also-honest coincidence from Test 2's,
                         this time because the bridge term is genuinely zero, not because
                         cumulative and FY-bounded formulas coincide
Actual Result:           CONFIRMED 500 = 500 = 500
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 12 — Attempt to edit elapsed Fiscal-Year End Date (post-reliance, via COMMITTED Entries)

```
Inputs:                  Company X, April/2026: an attempt is made to change FY2024's End
                         Date from Dec31/2024 to Nov30/2024 — FY2024 has extensive reliance
                         by this point (COMMITTED Entries throughout, elapsed since Dec2024,
                         referenced in every prior round's reports)
Timeline:                FY2024 Version 1 set 2023-12-01 -> extensive reliance accumulates
                         (Rounds 3-5's entire worked history) -> April/2026, boundary-edit
                         attempted
Query Date D:            n/a (this test evaluates the edit ATTEMPT itself, not a balance query)
Knowledge Cutoff T:      n/a
Fiscal-Year Definition:  FY2024, currently Version 1 (Jan1-Dec31 2024)
Fiscal-Year Definition Status/Version: Version 1 at attempt time; the test evaluates whether
                         a Version 2 may be created and how
Raw Cumulative Ledger Components: n/a (no financial fact is at issue in this test)
Raw Cumulative TB Result: n/a
Current-FY Activity Components: n/a
Derived Presentation Components: n/a
Reported Equity Components: n/a directly, though the CONSEQUENCE of the attempted change (if
                         it succeeded silently) would corrupt every Reported Equity figure in
                         Tests 3-9 above, which is exactly the risk BINV-16 exists to close
Reporting Viewpoint:     n/a
Expected Equation:       per BINV-16/B07 §1h: a silent, in-place edit is REFUSED; the change
                         must instead be routed through an authorized, CO-15-tier
                         `FiscalYearBoundaryChanged` action, creating Version 2 as a new,
                         separately-dated fact — never overwriting Version 1
Actual Design Equation:  (a) silent-edit path: REFUSED, logged as a refused attempt with actor
                         and timestamp (same pattern as any other refused unauthorized action,
                         CO-01). (b) authorized path: FY2024 Version 2 (End Date Nov30/2024)
                         created, Effective [administrator-chosen date], Recorded April/2026;
                         Version 1 remains permanently stored, never deleted. (c) existing
                         COMMITTED Entries dated within Dec2024 (under Version 1's boundary)
                         do NOT move to a different Fiscal Year automatically — their
                         membership was fixed by Version 1, the boundary authoritative when
                         they were Recorded
Expected Result:         no silent historical rewrite either way
Actual Result:           CONFIRMED — both the refusal (if attempted silently) and the
                         controlled path (if properly authorized) behave exactly as BINV-16
                         requires; Tests 3-9's figures, computed under Version 1, remain
                         exactly as computed, since they are Known-viewpoint-reproducible
                         regardless of what Version 2 or later attempts
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 13 — Attempt to edit boundary after a report was consumed (the "issued/consumed report" trigger, distinct from Test 12's "COMMITTED Entry" trigger)

```
Inputs:                  Company Y, immediately after migration cutover (Jan1/2026): a report
                         is generated and issued to stakeholders showing FY2026's structure
                         (End Date Dec31/2026) — even though FY2026 has almost no activity yet
                         beyond the MG-C03 opening balance (Test 11)
Timeline:                Jan1/2026 cutover -> report issued/consumed same day, referencing
                         FY2026's boundary -> a later attempt (say, June/2026) to silently
                         change FY2026's End Date
Query Date D:            n/a (evaluating the edit attempt and the report's continued
                         reproducibility)
Knowledge Cutoff T:      Jan 1 2026 (the issued report's own viewpoint)
Fiscal-Year Definition:  FY2026, Version 1 (Jan1-Dec31 2026), set at migration (Test 11/MG-C16)
Fiscal-Year Definition Status/Version: Version 1 at issuance; a June/2026 attempt would need
                         to create Version 2, per the SAME rule as Test 12 — the "issued/
                         consumed report" trigger alone is sufficient to require it, even
                         though FY2026 has (as of the report's own date) almost no COMMITTED
                         Entries yet
Raw Cumulative Ledger Components: n/a directly (the issued report's own figures are Test 11's:
                         G1 = 500=500)
Raw Cumulative TB Result: n/a beyond Test 11's cross-reference
Current-FY Activity Components: n/a
Derived Presentation Components: n/a
Reported Equity Components: the issued report's own figure, ReportedEquity_Known(Company Y,
                         Jan1/2026, T=Jan1/2026) = 500 (Test 11) — this is the figure that
                         must remain reproducible
Reporting Viewpoint:     Known, T = Jan 1 2026 (fixed, the report's own issuance moment)
Expected Equation:       even though FY2026 had almost no COMMITTED-Entry reliance as of
                         Jan1/2026, the mere fact that a report was issued/consumed referencing
                         its boundary is, by itself, a sufficient trigger for post-reliance
                         protection (B07 §1h's third listed trigger, independent of the first)
Actual Design Equation:  a June/2026 attempt to silently change FY2026's boundary is refused
                         on the same basis as Test 12; an authorized change creates Version 2;
                         re-querying `ReportedEquity_Known(Company Y, Jan1/2026, T=Jan1/2026)`
                         after ANY such change still returns exactly 500, unchanged
Expected Result:         the originally-issued report's own figure survives any later boundary
                         change, authorized or attempted
Actual Result:           CONFIRMED — 500, unchanged, confirming the "issued/consumed report"
                         trigger operates independently of the "COMMITTED Entry" trigger
                         Test 12 exercised
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 14 — Authorized future Fiscal-Year calendar change: future dates change as intended without reclassifying historical Entries

```
Inputs:                  Company X, in 2026: an authorized, CO-15-tier action changes FY2027's
                         calendar (currently configured Jan1-Dec31 2027, Version 1, NOT yet
                         begun, zero reliance) to April1/2027-March31/2028 — a genuine
                         forward-looking fiscal-year-basis change, decided before FY2027 begins
Timeline:                FY2027 Version 1 set at original Company X setup (2023-12-01,
                         alongside FY2024-2026) -> 2026, authorized change to FY2027's basis,
                         before FY2027 has begun
Query Date D:            various — checked against FY2024 (elapsed), FY2025 (elapsed), FY2026
                         (in progress), and FY2027 (future, changed)
Knowledge Cutoff T:      n/a (Current)
Fiscal-Year Definition:  FY2024/2025/2026 unaffected, still Version 1 each; FY2027 changed
                         from Version 1 (Jan1-Dec31 2027) to Version 2 (Apr1/2027-Mar31/2028)
Fiscal-Year Definition Status/Version: FY2027 Version 2, Effective/Recorded in 2026, before
                         FY2027's own start under either version
Raw Cumulative Ledger Components: unaffected for FY2024-2026's own historical activity
                         (Tests 3/7/8's figures unchanged)
Raw Cumulative TB Result: unaffected — the change touches only FY2027's future boundary
                         definition, not any COMMITTED Entry's own Effective Date or Fiscal
                         Year membership for FY2024-2026
Current-FY Activity Components: n/a for the historical years (unchanged); FY2027's own
                         activity, once it begins, will be bounded by the NEW Apr-Mar basis
Derived Presentation Components: n/a
Reported Equity Components: Reported Retained Earnings figures computed for any D within
                         FY2024-2026 are completely unaffected by the FY2027 change (Tests
                         3/7/8's 1250/1280-equation/1510 figures all hold exactly as before)
Reporting Viewpoint:     Current
Expected Equation:       a future, not-yet-relied-upon Fiscal Year's boundary may be changed
                         (even via the full authorized/audited path, chosen here out of policy
                         even though a lighter pre-reliance update would also have been valid,
                         per B07 §1h) without touching any earlier Fiscal Year's own definition
                         or any existing Entry's membership
Actual Design Equation:  FY2024/2025/2026's own Reported Equity figures (1250 at Test 3's D,
                         etc.) are byte-for-byte identical before and after the FY2027 change
Expected Result:         only FY2027-onward is affected, exactly as intended
Actual Result:           CONFIRMED — no change detected in any FY2024-2026 figure
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Test 15 — Multi-company calendar isolation

```
Inputs:                  Company X (Tests 12/14's calendar changes) and Company W (Test 10's
                         Reported Equity of 1850) coexist under one SMEsPlus tenant
Timeline:                concurrent with Tests 12-14
Query Date D:            Jan 1 2025 (Company W's Test 10 query point)
Knowledge Cutoff T:      n/a
Fiscal-Year Definition:  Company X's FY2024 (Version 2 attempt, Test 12) and FY2027 (Version 2,
                         Test 14) are entirely Company X's own facts; Company W's FY2024
                         remains its own, separate, Version-1, untouched definition
Fiscal-Year Definition Status/Version: Company W's FY2024: Version 1, unaffected by anything
                         done to Company X's calendar in Tests 12-14
Raw Cumulative Ledger Components: Company W's own (Test 10: 2000=2000), unaffected
Raw Cumulative TB Result: Company W's own, unaffected: 2000 = 2000
Current-FY Activity Components: Company W's own, unaffected
Derived Presentation Components: Company W's own bridge (250), unaffected
Reported Equity Components: Company W's Reported Equity = 1850, checked again after Company
                         X's Test 12/14 calendar changes — MUST remain exactly 1850
Reporting Viewpoint:     Current
Expected Equation:       B07 §1h's versioning model is defined per-Company (Fiscal Year is
                         already identified by "its Company and the span it covers," B07 §1);
                         no step in the boundary-change mechanism aggregates or compares across
                         Companies
Actual Design Equation:  Company W Reported Equity = 1850, identical to Test 10's figure,
                         checked after Company X's Test 12 (FY2024 boundary edit attempt) and
                         Test 14 (FY2027 authorized change) both completed
Expected Result:         zero interference in either direction
Actual Result:           CONFIRMED BY CONSTRUCTION — every Fiscal Year definition, and every
                         `FiscalYearBoundaryChanged` event, carries an explicit Company
                         reference (mirroring BINV-03's existing Company-boundary discipline);
                         no cross-Company aggregation or classification step exists anywhere
                         in B07 §1h's model for Company X's changes to reach through
PASS / FAIL:             PASS
Finding:                 none
Disposition:             n/a
```

## Regression Result

```
Scenarios executed:                            15
PASS:                                           15
Real design refinement found during construction, applied: 0 (matching B21 — the second
  consecutive round whose regression construction did not surface a further defect; the
  corrections made directly in B07/B08 while responding to the Round 5 audit, before this
  regression was constructed, already incorporated the relevant lessons)
Regressions into any prior-fixed defect:        0 (re-confirmed: Test 8 re-verifies `M-AUD-06`
  is unaffected; Tests 9/13 re-verify BINV-11/12's Known-viewpoint guarantee extends correctly
  to both G1-G3 and to Fiscal Year boundary versions; Tests 5-7 re-verify `M-AUD-09`'s
  delayed-close invariant under the corrected G1/G2/G3 terminology)
New CRITICAL/HIGH defects:                      0
```

**B22 = COMPLETE.** Test 2 and Test 11 are deliberately presented as showing genuine
coincidences (Cumulative = Current-FY Activity during a first Fiscal Year; a zero-valued
bridge before any Fiscal Year has elapsed) rather than forcing artificially "distinct" numbers
— consistent with this project's standing discipline of showing what the math actually says,
not what would look most different. Tests 3-4 are the direct, exact reproduction of ChatGPT's
Round 5 audit's own traced failure case, now resolved and correctly labeled.
