# B18 — CORR-B Focused Red-Team Regression

| Field | Value |
|---|---|
| **Coherence-annotated (Round 7)** | **CORR-B7-03 (2026-08-30)** — this document had never been touched since Round 1, and Test 5's scenario text still described the pre-CORR-B2-03/04/CORR-B3-05 posted-Entry carry-forward mechanism as if current. Annotated below, not rewritten — Test 5's own numeric conclusion was never wrong. See [CORR_B7_ACTIVE_SEMANTIC_CONSOLIDATION_ROUND.md](CORR_B7_ACTIVE_SEMANTIC_CONSOLIDATION_ROUND.md). |
| Session | SMEPLUS-26-08-29-MIG-B-D01-CORR-001 |
| Source of truth | `DOMAIN_01_ACCOUNTING_CORE_K_CORR_B_EXECUTOR_PROMPT.md` (commit `f363ee127b17d0d2743c4c2fde402bd39eabc633`) §CORR-B05 — ten scenarios, tested against the corrected design (CORR-B01/B02/B03) |
| Personas | Senior Accountant, External Auditor, CFO, Migration Architect, Period-Close Operator, Historical Reporting Reviewer, Clean-room Reviewer |
| Result | **10/10 PASS. One genuine precision gap was found while constructing test 10 and fixed before this document was finalized (BINV-11/MP-09 scope — Amendment distinguished from Correction/Void).** |

## Test Log

### Test 1 — Close → reopen → correct, no independent permanent consumption

```
scenario:            Period P closes; Entry E in P, never independently consumed; authorized
                      reopen (CO-08) fires
preconditions:        E is COMMITTED, unconsumed, dated within P
expected_invariant:   Amendment on E becomes available again after reopen (BINV-02 restored;
                       BINV-06/07 never engaged, nothing to violate)
design_path_examined: B04 §4 gate rule — (a) consumed=false, (b) period=open, both required
result:               PASS
finding:              none
disposition:          n/a
residual_risk:        none
```

### Test 2 — Close → permanent downstream consumption → attempted reopen/correction

```
scenario:             Period P closes; before reopen, E is filed (Consumption trigger 1,
                      permanent Consumption Record); authorized reopen fires
preconditions:        E is COMMITTED and has a Consumption Record
expected_invariant:   Amendment on E remains refused after reopen; only a linked Correction
                       is available, permanently (BINV-06/07)
design_path_examined: B04 §4 gate rule — condition (a) consumed=false is FALSE and stays
                       false regardless of Period status; BR-07
result:               PASS — this is the specific case the pre-correction design got wrong
finding:              confirms CORR-B01's fix
disposition:          n/a
residual_risk:        none
```

### Test 3 — Multiple close/reopen cycles

```
scenario:             Period P: close, reopen, close, reopen (N=2 cycles); one entry E1
                      consumed during cycle 1, one entry E2 never consumed
preconditions:        E1 has a Consumption Record from cycle 1; E2 does not
expected_invariant:   Each close/reopen is independently logged (PeriodClosed/PeriodReopened,
                      B04 §3); E1 stays permanently non-amendable through every cycle; E2
                      becomes amendable again on every reopen, refused on every close
design_path_examined: B04 §4 — Period Lock (BINV-02) and Consumption (BINV-06/07) are
                      orthogonal; toggling Period status any number of times cannot create,
                      remove, or affect a Consumption Record, which is written once and
                      permanent (BINV-07)
result:               PASS
finding:              none — no cycle-count limit or special case exists or is needed, by
                      construction
disposition:          n/a
residual_risk:        none
```

### Test 4 — Open-period Revenue/Expense/Current Earnings equation

```
scenario:             Company C: Assets 1,000 / Liabilities 200 / Equity 800 at period start;
                      mid-period sale (dr Cash 300 / cr Revenue 300) and expense payment
                      (dr Expense 100 / cr Cash 100)
preconditions:        both Entries individually satisfy MP-01
expected_invariant:   MP-02's expanded equation holds: Assets + Expenses = Liabilities +
                      Equity + Revenue
design_path_examined: B08 MP-02 (corrected)
result:               PASS, verified numerically: Assets=1,200, Expenses=100 → 1,300;
                      Liabilities=200, Equity=800, Revenue=300 → 1,300. Match. Simple equation
                      checked and confirmed NOT holding mid-period (1,200 ≠ 1,000) by exactly
                      Current Earnings (200) — confirms the corrected proof's central claim
                      with real numbers, not only algebra.
finding:              none
disposition:          n/a
residual_risk:        none
```

### Test 5 — Close/carry-forward equation transition

**Coherence note (Round 7, CORR-B7-03):** this test's own numeric conclusion (the simple
equation holds post-close, using the updated Equity figure) has never been wrong and is
re-verified independently, under the current design, at
[B20](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md) Tests 9-11 and
[B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md) MP-12 Proof F. The scenario text below
predates CORR-B2-03/04 and CORR-B3-05 and describes the mechanism this design used at Round 1
only — "CAP-09 transfers Current Earnings... resets Revenue/Expense to zero" — which was
removed as internally contradictory and arithmetically unsound (`M-AUD-07`) two rounds later.
ChatGPT's Round 7 audit (`M-AUD-15`/`M-AUD-16`, and this domain's own CORR-B7-03 sweep) found
this scenario text was never annotated when the mechanism it describes was superseded, unlike
[B20](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md)/[B21](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md)/[B22](B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md)'s
own later terminology annotations for comparable gaps. **Kept visible below as the historical
record it is, not deleted — but it is no longer current design authority for HOW the equation
transition happens, only for the fact THAT it holds numerically.** Under the current design, no
Entry is posted at Fiscal Year Close and Revenue/Expense are never reset by any posted action —
the same post-close position is reached instead through B07 §1e's derived Reported Retained
Earnings formula, applied once the relevant Fiscal Year has Elapsed (never through a "period
closes... resets" mechanism as this test's scenario line describes).

```
scenario:             Continuing Test 4: period closes; CAP-09 transfers Current Earnings
                      (200) into formal Equity, resets Revenue/Expense to zero
preconditions:        Test 4's ending position
expected_invariant:   Simple equation (Assets = Liabilities + Equity) holds on the new
                      period's opening position, using the updated Equity figure
design_path_examined: B05 BINV-10 (strengthened), B08 MP-02 (corrected, post-closing
                      special case)
result:               PASS, verified numerically: new Equity = 800+200 = 1,000; Assets 1,200
                      = Liabilities 200 + Equity 1,000. Match.
finding:              none
disposition:          n/a
residual_risk:        none
```

### Test 6 — E valid D1, void D2, as-of D1/D2

```
scenario:             E1 dated D1, committed, included in a report issued as of D1; voided at
                      D2 > D1 via linked Correction E2 (zero-net reversal, dated D2)
preconditions:        E1 COMMITTED at D1; E2 links to E1, dated D2
expected_invariant:   "balance as of D1" queried at any later time reproduces exactly what
                      was true at D1; "balance as of D2 or later" reflects the void
design_path_examined: B08 MP-09 (corrected — pure date filter, no status filter)
result:               PASS: as-of-D1 query sums only E1 (D1<=D1); E2 excluded (D2>D1) —
                      identical to the original D1 report. As-of-D2 query sums E1+E2, net
                      zero.
finding:              none — this is the specific case CORR-B03 fixed
disposition:          n/a
residual_risk:        none
```

### Test 7 — Correction-of-correction

```
scenario:             E2 (a void of E1) is later found itself mistaken; corrected by E3
                      (chain: E1 -> E2 -> E3)
preconditions:        E2 is SUPERSEDED by E3's link; E3's Lines restate E1's original effect
expected_invariant:   Balance as of D1 (E1's date) unaffected by the E2/E3 chain; balance as
                      of E3's date or later nets back to E1's original effect; no ambiguity
                      in the chain (GAP-D01-23 stays resolved)
design_path_examined: B04 §6 (chain design, unaffected by CORR-B01/02/03), B07 §3 cardinality
                      rule (at most one direct target link per Entry — chains, not trees)
result:               PASS
finding:              none — confirms chaining and historical stability compose correctly,
                      no special case needed where they interact
disposition:          n/a
residual_risk:        none
```

### Test 8 — Multi-company isolation

```
scenario:             Company C1 has Entry E1; Company C2 is independently operating; check
                      whether any of the three corrections introduce a cross-company leak
preconditions:        none — this is a structural review, not a single transaction trace
expected_invariant:   BINV-03 (company boundary) holds exactly as before; no Consumption
                      trigger, Period Lock, or Void mechanism can reference or affect another
                      company's data
design_path_examined: B04 §4 (Consumption triggers, Period Lock — both already company-scoped
                      per BINV-02/CAP-05, unmodified by this round); B08 MP-02/MP-09 (both
                      explicitly "for one Company", unmodified in this respect); B03 §3
                      (downstream-reference trigger scoped to named domain seams, never to
                      another company's books)
result:               PASS
finding:              none — none of the three corrections touched CAP-05/BINV-03, and each
                      was independently re-checked against it rather than assumed unaffected
disposition:          n/a
residual_risk:        none
```

### Test 9 — Audit/event permanence

```
scenario:             Check whether CORR-B01/B02/B03 weakened CAP-08/BINV-07/BINV-08 (forced,
                      append-only, independently-reconstructable audit trail)
preconditions:        none — structural review
expected_invariant:   Every state change still produces exactly one forced event; Consumption
                      Records remain permanent; Audit Evidence remains independent of Entry
                      content
design_path_examined: B04 §3 (event table — gained one new forced event, PeriodReopened,
                      lost none); B05 BINV-07/BINV-08 (both textually unchanged by this round
                      except BINV-06's trigger-list correction, which does not touch
                      permanence itself)
result:               PASS — if anything, strengthened: the pre-correction contradiction
                      (BINV-07 "never retracted" vs. B04's reopen claim) was itself a latent
                      threat to confidence in audit permanence, now removed
finding:              none
disposition:          n/a
residual_risk:        none
```

### Test 10 — Duplicate/idempotent event handling at conceptual level

```
scenario:             An Entry E1 (with origin reference R) is voided (E2, linked); does R
                      become available for reuse, or does resubmitting R still get refused as
                      a duplicate (B11 scenario 9)?
preconditions:        E1 COMMITTED with origin reference R; E1 later voided by E2
expected_invariant:   R must remain permanently associated with its original submission —
                      voiding the FINANCIAL EFFECT must not silently free up the idempotency
                      key, or a resubmitted duplicate of the same origination event could
                      double-process
design_path_examined: B11 scenario 9 (duplicate detection design) cross-checked against B04
                      §5 (void, corrected). B11's design never described idempotency keys as
                      freed by voiding — this was implicitly correct, but had not been
                      explicitly cross-checked against the corrected Void mechanism until now
result:               PASS, on inspection — no defect found, but the cross-check itself was
                      new (not performed during the original B11 design or the original B16
                      red-team)
finding:              A genuine precision gap was found while performing THIS cross-check,
                      but in BINV-11's wording, not in the duplicate-detection design itself
                      — see disposition
disposition:          **Found and fixed:** constructing this test required reasoning
                      precisely about what "as of D1" should mean when D1 predates an
                      Amendment (not just a Void), which surfaced that BINV-11's original
                      wording did not explicitly distinguish Amendment from Correction/Void.
                      Fixed in B05 (BINV-11) and B08 (MP-09 proof requirement): the historical
                      reproducibility guarantee is unconditional for consumed facts and
                      intentionally does not extend to an unconsumed fact's pre-consumption
                      Amendments, because "unconsumed" means nothing has relied on the value
                      yet. This is not a defect in the duplicate-detection design (which
                      remains correct as originally specified) — it is a scope-precision fix
                      to a different invariant, surfaced by this test's adjacent reasoning.
residual_risk:        None remaining — fix applied and verified against the same worked
                      reasoning that found it.
```

## Regression Result

```
Scenarios executed:                          10
PASS on first construction:                  9
Found real gap during construction, fixed:   1 (Test 10 — BINV-11/MP-09 scope precision)
Regressions into any of B16's six original fixes: 0
Regressions into CORR-B01/02/03 themselves:  0
New CRITICAL/BLOCKING defects:                0
Open CRITICAL findings:                       0
Open HIGH findings:                           0
```

**B18 = COMPLETE.** Supersedes the earlier, narrower eight-scenario regression drafted before
the more detailed CORR-B executor specification (K) was found on the repository — that
earlier draft's eight scenarios are all subsumed by Tests 1–2 and 4–7 above; Tests 3, 8, 9,
10 are the four scenarios K specifies that the earlier draft had not yet covered.
