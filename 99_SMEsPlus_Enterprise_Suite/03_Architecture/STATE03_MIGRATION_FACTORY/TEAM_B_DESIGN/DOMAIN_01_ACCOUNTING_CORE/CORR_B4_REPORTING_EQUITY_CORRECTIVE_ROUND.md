# CORR-B4 — Targeted Corrective Round 4: Reported Equity Mathematics, Fiscal-Boundary Continuity & Viewpoint-Safe Retained Earnings

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-30-MIG-B-D01-CORR4-001 |
| Domain | DOMAIN_01 — Accounting Core |
| Source of truth | ChatGPT Independent Team B Design Re-Audit Round 4, commit `9c0a3f2d179994a20f01db16d5713989a78c0b2a`, verified against the live repository before any correction was made |
| Scope | Targeted correction of exactly three findings (`M-AUD-08`, `M-AUD-09`, `M-AUD-10`). B0–B20 not restarted. No code. No DOMAIN_02. No PMO. No self-approval. Jira owner/due date preserved as governance red flags, not invented. |

## 0. CORR-B4 Change Log (required schema)

| finding_id | old_statement_or_rule | corrected_statement_or_rule | affected_artifacts | reason | verification_status |
|---|---|---|---|---|---|
| M-AUD-08 | B07 §1e (Round 3): Reported Retained Earnings = designated RE account's direct-posted balance + Σ closed-FY Current Earnings. B08 MP-02 (Round 3, informal): "Reported Equity = Equity(ledger, all-time) + Reported Retained Earnings." | B07 §1f (new): Reported Equity = Other Ledger Equity (every Equity account EXCEPT the designated RE account) + Reported Retained Earnings — a non-overlapping partition of the Equity category, so the designated RE account contributes exactly once. B08 MP-02/MP-12 corrected to use this decomposition explicitly. | B02 CAP-09, B05 BINV-10/BINV-14 (new), B07 §1f (new), B08 MP-02/MP-12 (new), B10 MG-C15 (new), B15 §3d | The designated Retained Earnings account is itself inside the Equity Account Category (B07 §1a/CAP-01) — summing it once directly and once inside Reported Retained Earnings double-counts it, overstating Reported Equity by that account's own balance on every report | VERIFIED — B21 Tests 1, 2, 12, 13 (including the first genuine multi-Equity-account Company this design pack has constructed) |
| M-AUD-09 | B07 §1e (Round 3): sums "every Fiscal Year that CLOSED before D" — closed meaning the `FiscalYearClosed` Audit Event had been declared. | B07 §1e (corrected): sums "every Fiscal Year that has ELAPSED as of D" — a pure calendar fact (End Date <= D), independent of whether `FiscalYearClosed` has been declared. `FiscalYearClosed` now governs posting-lock scope only (B02 CAP-09, B04 event table). | B02 CAP-09, B04 (event table + closing summary), B05 BINV-10/BINV-14, B07 §1e (corrected), B08 MP-02/MP-11/MP-12, B11 scenario 20 (new), B13 DT-11 (new), B15 §3d | A real, expected gap between a Fiscal Year's calendar end and its operational close declaration (reconciliation, review — commonly days to weeks) would, under the declaration-gated formula, silently omit that year's earnings from Reported Retained Earnings for the entire gap — a genuine, standing reporting hole, not an edge case | VERIFIED — B21 Tests 5-7 (the audit's own delayed-close scenario, worked with real numbers, including the direct contrast against what the superseded formula would have wrongly computed) |
| M-AUD-10 | B07 §1e (Round 3) defined Reported Retained Earnings using MP-09 Mode 2 only; B20 Test 8 relied on an undefined Mode-1 ("as originally known") version without the authoritative formula ever specifying one. | B07 §1g (new): Reported Retained Earnings and Reported Equity are parameterized by reporting viewpoint — `_Known(C,D,T)` (Mode 1, built directly on MP-09's existing Recorded-At filtering) and `_Current(C,D)` (Mode 2) — built on the same mechanism MP-09 already uses, not a new one. CO-14's mode-labeling requirement extended to cover these outputs explicitly. | B07 §1g (new), B08 MP-12 (Proofs D/E), B09 CO-14 (extended) | Without a defined Known-viewpoint formula, a literal implementation following B07 §1e would let a later Restatement silently alter an already-issued historical Balance Sheet, violating BINV-11's reproducibility guarantee one level up from where BINV-11 itself is proven | VERIFIED — B21 Tests 8-10 (reconstructing an originally-issued figure after a later Restatement, and confirming the boundary-driven Elapsed test removes a second viewpoint question the superseded model would have needed) |

## 1. CORR-B4-01 / CORR-B4-02 — Raw vs. Reported Identity and Elimination of Direct RE Double-Counting

### The problem, precisely

`M-AUD-08` found that Round 3's B07 §1e, combined with B08 MP-02's informal companion
paragraph, double-counted the designated Retained Earnings account: that account sits inside
the Equity Account Category, so `Equity(ledger, all-time)` already contains its balance —
adding the full Reported Retained Earnings figure on top (which independently repeats that same
balance as its own first term) counts it twice. The audit additionally found that Round 3 never
formally re-derived the reporting equation from MP-02's original, single-horizon proof after
introducing mixed horizons (Balance Sheet categories all-time, Income Statement categories
Fiscal-Year-bounded, Reported Retained Earnings folding in prior years) — it asserted the
transformation rather than proving it.

### The fix

**Non-overlapping decomposition adopted** (B07 §1f, new): Equity is partitioned into **Other
Ledger Equity** (every Equity-category account EXCEPT the one designated Retained Earnings
account) and **Reported Retained Earnings** (which alone covers the designated account, plus
elapsed-Fiscal-Year earnings). Reported Equity is their sum. Because the designated account is
excluded from Other Ledger Equity by definition, and is the only account inside Reported
Retained Earnings's direct-posting term, no account is ever counted twice.

**Full re-derivation performed** (B08 MP-12, new): Proof A restates MP-02's original expanded
equation as the Raw Ledger Identity (every category on one all-time horizon, including
Revenue/Expense — this is what Round 3 never explicitly separated out). Proof B partitions
Revenue/Expense by Fiscal Year, splits the sum into elapsed years plus the year in progress,
decomposes RawEquity per B07 §1f, and substitutes to derive the Reported Financial-Statement
Identity by algebra alone — introducing no new assumption beyond Proof A and the two B07
definitions. Proof C states the resulting target form cleanly.

### Alternatives compared (per directive, not accepting the audit's suggested direction blindly)

The directive's suggested relationship (`Other Ledger Equity = Raw Ledger Equity excluding the
designated RE component; Reported Equity = Other Ledger Equity + Reported Retained Earnings`)
was independently re-derived from first principles (B08 MP-12 Proof B), not merely copied —
the derivation confirms it is not just *a* non-double-counting model but the *unique* one
consistent with MP-02's already-proven Raw Ledger Identity, since any other partition of the
Equity category would either omit an account from both terms (undercounting) or include an
account in both (the original defect). No alternative decomposition was found that avoids one
of these two failure modes while still producing Round 3's required properties (no double
counting from postings; Restatements flow through automatically).

### Mandatory proof (worked numbers, per directive)

The audit's own cited example (direct RE 1000, FY2024 CE 250, correct total 1250, not 2250) is
reproduced and confirmed at [B21](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md) Test 1. A genuine
multi-Equity-account Company — which no prior round's regression happened to construct, which
is exactly why the double-count never surfaced numerically before — is built and verified at
B21 Test 2.

### What changed

`B02` CAP-09 · `B05` BINV-10 (rewritten again), BINV-14 (new) · `B07` §1f (new) · `B08` MP-02
(post-boundary paragraph corrected again), MP-11 (cross-reference corrected), MP-12 (new) ·
`B10` MG-C15 (new) · `B15` §3d (new).

## 2. CORR-B4-03 — Fiscal-Boundary Continuity Independent of Operational Close Timing

### The problem, precisely

`M-AUD-09` found that Round 3's B07 §1e gated a Fiscal Year's inclusion in Reported Retained
Earnings on the `FiscalYearClosed` *declaration* — an authorized, operator-triggered action
with no requirement that it happen instantaneously at the Fiscal Year's own calendar boundary.
Worked failure scenario (the audit's own): direct RE 1000, FY2024 CE 250, Cash at Dec 31 2024 =
1250; if the declaration is delayed to Jan 15 2025, a report on Jan 5 2025 would show Reported
Equity = 1000 against Assets of 1250 — a reporting failure of exactly 250, solely because an
operator had not yet acted.

### The fix

**Boundary-driven ("Elapsed") inclusion adopted.** B07 §1e now sums every Fiscal Year whose own
End Date has passed as of the query date — a pure calendar fact, never gated on
`FiscalYearClosed`. `FiscalYearClosed` (B02 CAP-09, B04) is re-scoped to govern posting-lock
scope only, exactly like `PeriodClosed` but wider — the same "orthogonal gates" pattern this
domain has used since CORR-B01 (Period Lock vs. Consumption) and CORR-B2-03/04 (Period Lock vs.
Fiscal-Year Lock).

### Alternatives compared (per directive, not accepting the suggested direction blindly)

Three models compared at [B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-11, per the
directive's explicit requirement: **Option A (adopted)** — boundary-driven, as above. **Option
B (rejected)** — an explicit "Completed-but-Unclosed Earnings" reported-equity component,
reclassified into Retained Earnings at declaration time with zero change to the total; rejected
as unnecessary complexity, since the provisional/final distinction it would buy is already
available more simply via CAP-04's existing Period-Lock-extended-to-Fiscal-Year status, without
needing a second dollar-value component. **Option C (rejected)** — mandatory atomic close
before the next Fiscal Year may open; rejected on independent operational grounds (real close
processes take genuine calendar time; blocking new-year activity for the duration is not a
requirement any of this domain's evidence has ever authorized), not merely because the directive
cautioned against selecting it reflexively — it was evaluated and found to fail even without
that caution.

### Mandatory proof (worked numbers, per directive)

[B21](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md) Tests 5-7 trace the audit's own scenario
exactly: Test 5 shows the corrected formula produces the right figure at the undeclared 5-day
mark (with the superseded formula's wrong figure computed alongside, for direct contrast); Test
6 proves Reported Equity is referentially identical immediately before and after the eventual
declaration, with no new financial fact; Test 7 confirms a new-Fiscal-Year posting is safely
permitted while the prior year remains undeclared.

### What changed

`B02` CAP-09 (posted-declaration scope corrected) · `B04` event table (`FiscalYearClosed` row
and explanatory paragraph corrected again) · `B05` BINV-10 (rewritten again), BINV-14 (new) ·
`B07` §1e (Elapsed redefinition) · `B08` MP-02/MP-11/MP-12 (Proof F) · `B11` scenario 20 (new) ·
`B13` DT-11 (new) · `B15` §3d.

## 3. CORR-B4-04 — Viewpoint-Aware Reported Retained Earnings / Reported Equity

### The problem, precisely

`M-AUD-10` found B07 §1e defined Reported Retained Earnings using MP-09 Mode 2 only, while
[B20](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md) Test 8 already relied on a Mode-1 ("as
originally known") version to prove a later Restatement cannot silently alter an already-issued
historical report. The regression's behavior was correct; the formula it was nominally testing
never actually specified that behavior — a real risk if a future implementation followed B07
§1e literally rather than B20's test intent.

### The fix

B07 §1g parameterizes Reported Retained Earnings and Reported Equity by reporting viewpoint —
`ReportedRetainedEarnings_Known(C,D,T)` / `_Current(C,D)`, and the same split applied to
Reported Equity — built directly on MP-09's already-proven Mode 1/Mode 2 mechanism (no new
temporal machinery invented). The Elapsed test itself (B07 §1e) takes no viewpoint parameter,
since it is a pure calendar fact — a direct, structural benefit of CORR-B4-03's boundary-driven
redefinition: a second, independent viewpoint question ("was the declaration itself known as of
T?") that would have existed under the superseded declaration-driven model is removed entirely,
not merely deferred. CO-14 (B09) extended to explicitly require mode-labeling for these outputs.

### Mandatory proof (worked numbers, per directive)

[B21](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md) Tests 8-9 reconstruct an originally-issued
figure after a later Restatement and confirm the Known view stays fixed while the Current view
reflects the Restatement; Test 10 confirms the boundary-driven redefinition's specific benefit
(no need to reason about the declaration's own Recorded-At timing at all).

### What changed

`B07` §1g (new) · `B08` MP-12 (Proofs D/E) · `B09` CO-14 (scope extended).

## 4. CORR-B4-05 — Mathematical Re-Proof

Full re-derivation performed at [B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md) MP-12
(new), covering every proof the directive required: **Proof A** (Raw Ledger Identity, citing
MP-02's already-proven expanded equation). **Proof B** (Reporting Transformation — Revenue/
Expense partitioned by Fiscal Year, elapsed-vs-current split, Equity decomposed per B07 §1f,
substitution derives the reported form). **Proof C** (the target Current-Fiscal-Year reporting
form). **Proof D** (Historical Mode 1 — the same algebra, viewpoint-restricted, since MP-01's
grand-total identity holds for any consistent Entry subset). **Proof E** (Restated Mode 2 — a
Restatement is itself an ordinary balanced Entry, so Proof A-C's derivation is agnostic to
whether it exists). **Proof F** (the Fiscal Close Declaration Invariant — `FiscalYearClosed`
appears in none of the formula's terms, so Reported Equity is referentially, not merely
provably, identical before and after it, absent new financial facts). **Proof G** (Trial
Balance vs. Financial Statements — both presentations tie to the identical underlying ledger,
differing only in how the Equity category is grouped).

## 5. CORR-B4-06 — Targeted Regression

See [B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md) —
15/15 scenarios pass. Unlike Rounds 1-3, this regression's own construction did not surface a
further defect requiring correction — recorded honestly as what actually happened, not
polished into a false claim of higher process-confidence than earned (per
[G §4d](DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md)).

## 6. CORR-B4-07 — Propagation Check

Every artifact in the directive's "at minimum inspect/update" list was inspected: B02, B04,
B05, B07, B08, B09, B10, B11, B13, B15, B20, F, G, H, TEAM_B_STATUS.md. Two pre-existing gaps
unrelated to this round's specific findings were noticed and fixed while propagating (not
Round-4 findings themselves, disclosed as such where fixed): B02 §5's capability-list summary
still named "Period-End Carry-Forward" (Round 1's pre-rename name); B04's header table was
missing a Round-3 summary row even though Round-3 body edits were made; B04's "what constitutes
a new accounting fact" table row still listed a Fiscal-Year-Close Entry after Round 3 removed
it. All three are corrected, visibly, in this round's file changes.

## 7. CORR-B4-08 — Evidence / Push Verification

See [DOMAIN_01_ACCOUNTING_CORE_T_CORR_B4_CLOSURE_EVIDENCE.md](DOMAIN_01_ACCOUNTING_CORE_T_CORR_B4_CLOSURE_EVIDENCE.md)
and [SESSION_ARCHIVE/SESSION_SMEPLUS-26-08-30-MIG-B-D01-CORR4-001_CLOSURE.md](SESSION_ARCHIVE/SESSION_SMEPLUS-26-08-30-MIG-B-D01-CORR4-001_CLOSURE.md).

## 8. Six Assumptions — Status After This Round

```
1. Rounding method .................................. OPEN, unchanged
2. Period close / Consumption ....................... OPEN, unchanged this round (see B15 §6
                                                        Round 4 note — this round's subject
                                                        matter, reporting-equity mathematics,
                                                        does not bear on reopen/consumption
                                                        timing at all)
3. COA template/instance ............................. OPEN, unchanged
4. Broad audit tamper-evidence scope .................. OPEN, unchanged
5. Correction shape flexibility ....................... OPEN, unchanged
6. CO-02/CO-06 coupling ............................... OPEN, unchanged
```

**No assumption was resolved by Team B fiat, and none was narrowed this round** — Round 4's
findings (Reported Equity double-counting, Fiscal-boundary continuity, viewpoint
parameterization) are pure reporting-formula mathematics with no bearing on any of the six
assumptions' subject matter. The designated Retained Earnings account (B07 §1f, B10 MG-C15) is
a required, unambiguous migration-configuration fact — exactly one correct answer per Company —
not a seventh open judgment call in the sense the six standing assumptions are.

## 9. Jira Governance Facts — Preserved, Not Invented

Per explicit instruction, `ERPPLUS-100`'s Assignee (`UNASSIGNED`) and Due Date (`TBD`/empty)
are preserved exactly as found — flagged as PMO/governance red flags in the evidence comment,
never filled in by this executor. This is a PMO/Boss-level control decision, outside this
executor's authority to resolve, exactly as the six design assumptions are outside this
executor's authority to resolve.
