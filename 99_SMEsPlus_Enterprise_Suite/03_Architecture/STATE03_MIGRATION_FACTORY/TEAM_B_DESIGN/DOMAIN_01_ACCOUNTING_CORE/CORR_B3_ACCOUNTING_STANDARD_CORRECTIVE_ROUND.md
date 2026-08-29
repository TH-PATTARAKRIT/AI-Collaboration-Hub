# CORR-B3 — Targeted Corrective Round 3: Prior-Period Error Compliance + Fiscal Close Resolution

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-29-MIG-B-D01-CORR3-001 |
| Domain | DOMAIN_01 — Accounting Core |
| Source of truth | ChatGPT Independent Team B Design Re-Audit Round 3, commit `f6fb633fd141f45caf047bc94d75f84420e1cc6d`, verified against the live repository before any correction was made |
| Accounting standard evidence | IAS 8 *Accounting Policies, Changes in Accounting Estimates and Errors* — read at primary-source level (fetched PDF, paragraphs 1-54 extracted and read directly via primary text, not from memory or a secondary summary, per explicit directive instruction). TAS 8 (the Thai equivalent standard) is confirmed only via secondary sources as "substantively aligned with IAS 8" — this is a genuinely lower confidence tier than the IAS 8 primary-source read, and is never silently upgraded or blended with it anywhere in this correction, consistent with [B14](B14_CLEAN_ROOM_PROVENANCE_MATRIX.md)'s provenance-confidence discipline. |
| Scope | Targeted correction of exactly two material findings (`M-AUD-06`, `M-AUD-07`). B0–B19 not restarted. No code. No DOMAIN_02. No PMO. No self-approval. No Boss assumption resolution. |

## 0. CORR-B3 Change Log (required schema)

| finding_id | old_statement_or_rule | corrected_statement_or_rule | affected_artifacts | reason | verification_status |
|---|---|---|---|---|---|
| M-AUD-06 | B19 Test 11 (Round 2): "recognizing the correction as an ordinary current-dated fact is always sufficient" — a Restatement crossing a closed Fiscal Year boundary never requires anything beyond an ordinary current-dated Entry. B04 §3a (Round 2) contained no Error/Estimate/Materiality classification step at all. | B04 §3b adds a full classification decision tree (Current-Period Error / Prior-Period Error / Change in Accounting Estimate / Material vs. Immaterial Prior-Period Error), grounded directly in IAS 8 paras 5/34/36-38/41/46. §3c adds retrospective restatement mechanics for the Material branch specifically (comparative restatement; opening-balance restatement for the earliest period presented, or the earliest practicable period under impracticability, IAS 8 paras 42/43/45/50-53). B19 Test 11's original conclusion is retained as correct for the Immaterial branch only (confirmed at [B20](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md) Test 7) and superseded for the Material branch (confirmed at B20 Tests 2-5, 9-12). No numeric materiality threshold is invented anywhere in this correction (B09 CO-16, new). | B04 §3b/§3c (new), B05 BINV-13 (new), B09 CO-16 (new), B11 scenario 19 (new), B15 §3c, B19 Test 11 (annotated, not rewritten) | IAS 8 para 42 requires mandatory retrospective restatement for material prior-period errors, and para 46 requires the correction be excluded from current-period profit or loss — B19 Test 11 never tested materiality at all, so its universal conclusion silently assumed every case was immaterial, which is exactly the shape of error a single-executor regression pass cannot reliably catch on its own (B15 §3c pattern note) | VERIFIED — B20 Tests 1-3, 6-8 (classification), Tests 2, 9-12 (material-branch mechanics with real numbers), Test 7 (immaterial-branch confirmation) |
| M-AUD-07 | B08 MP-11 (Round 2, `new, added at CORR-B2-03/04`): "Fiscal Year Close commits exactly one new Entry per Company: Lines that debit Revenue accounts ... and credit Expense accounts, with the net difference (Current Earnings) posted to a designated formal Equity account." B02 CAP-09 and B05 BINV-10 described the same posted-Entry model. | No-posted-close model adopted (compared against the superseded posted-Entry model, [B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-10). Fiscal Year Close is now a purely declarative Audit Event (`FiscalYearClosed`, B04, corrected) — it posts no Entry. B07 §1e (new) defines Reported Retained Earnings as a derived reporting formula: the formally-designated Retained Earnings account's own direct-posted balance, plus the sum, over every closed Fiscal Year, of that year's Current Earnings computed via MP-09 Mode 2. B08 MP-11 rewritten to match (Round-2 text kept fully visible above the correction); B02 CAP-09, B05 BINV-10, B04's event table all propagated. | B02 CAP-09, B04 (event table + §3b/§3c cross-references), B05 BINV-10, B07 §1b/§1d/§1e, B08 MP-02/MP-11, B13 DT-10 (new), B15 §3c | The Round-2 MP-11 text directly contradicted this same design's own repeated claim that "Revenue/Expense are never reset by a posted action" (B07 §1d, MP-02's own post-closing paragraph) — a real internal contradiction, not a wording nuance — and, traced through MP-09's Effective-Date-bounded aggregation, would corrupt the closing Fiscal Year's own historical query if the closing Entry were dated inside that year (and would violate the never-reset claim again if dated in the new year instead) — a genuine arithmetic bug with no dating choice that avoids it | VERIFIED — B20 Tests 9-11 (pre-close, post-close, new-FY-clean, all with real numbers) directly refute the traced defect by re-querying the closing date itself after the close and confirming it is unchanged |

## 1. CORR-B3-01 / CORR-B3-02 — Error vs. Estimate Classification and IAS 8 Prior-Period Error Treatment

### The problem, precisely

`M-AUD-06` found that Round 2's B04 §3a and its own regression (B19 Test 11) never asked
whether a prior-period correction was **material**. IAS 8 draws several distinctions this
domain's design had not yet made explicit: a **Current-Period Error** (an error in the same,
still-open, not-yet-reported period — not even within IAS 8's definition of a "prior period
error," para 5) is not the same as a **Prior-Period Error** (para 5: a misstatement in
financial statements for one or more prior periods); a Prior-Period Error is not the same as a
**Change in Accounting Estimate** (para 5, paras 32-38: a revision based on new information
about circumstances, not a correction of a past mistake, applied prospectively only, para 36);
and within Prior-Period Errors, **Material** errors (para 41) are treated differently from
**Immaterial** ones (para 41's qualifier scopes the mandatory-restatement requirement, para 42,
to material errors specifically — IAS 8 never requires restating an immaterial one).

### The fix

B04 §3b adds the full decision tree, in order: (1) is the affected period still open and
unreported — if so, Current-Period Error, ordinary correction, stop; (2) is this a revision of
a past mistake, or a revision of judgment based on new information about circumstances — if the
latter, Change in Accounting Estimate, prospective only (IAS 8 para 36), stop; (3) is the
resulting Prior-Period Error Material or Immaterial — a **policy/judgment input this domain
never computes** (CO-16, B09, new), never a numeric threshold this design invents; (4)
Immaterial — ordinary current-dated Entry is sufficient (B19 Test 11's original conclusion,
now correctly scoped, confirmed at B20 Test 7); Material — routed to §3c's retrospective
restatement mechanics.

§3c implements the Material branch precisely: comparative amounts for the specific prior
period(s) affected are restated (IAS 8 para 42(a)); if the error predates the earliest
comparative period presented, the opening balances of assets/liabilities/equity for that
earliest period are restated instead (para 42(b)) — and, per B07 §1e's formula, this happens
**automatically**, with no bespoke "opening balance adjustment" mechanism, because Reported
Retained Earnings already sums every closed Fiscal Year up to the query date (verified at
[B20](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md) Test 3); the correction is never included
in the period-of-discovery's own profit or loss (para 46, verified numerically at B20 Test 12).
Two impracticability sub-cases (para 43: period-specific effects impracticable to determine —
restate from the earliest practicable period instead, verified at B20 Test 4, with a formula
annotation added to B07 §1e as a direct result of constructing that test; para 45: even the
cumulative effect impracticable to determine — correct prospectively from the earliest
practicable date instead, verified at B20 Test 5) are both explicitly modeled, following IAS 8
paras 50-53's genuine-effort standard for what "impracticable" means (not mere inconvenience).

### Alternatives compared (per directive, not accepting the audit's suggested direction blindly)

Two candidate shapes for the classification step were considered. **Option A (adopted):** a
single ordered decision tree (current-period → estimate → material/immaterial), evaluated once
per correction, with materiality supplied externally (CO-16). **Option B (rejected):** treat
materiality as itself computable from a stated default threshold (e.g. a fixed percentage of
Revenue or Current Earnings), to make the classification fully mechanical. Option B was
rejected because IAS 8 itself defines materiality only qualitatively (para 5's cross-reference
to whether an item "could reasonably be expected to influence" a user's economic decisions) and
states no numeric bright line anywhere in the paragraphs read — inventing one would not be a
reasonable design simplification, it would be asserting a professional judgment this domain has
no authority to assert, directly the failure mode CO-16 exists to block. This is a required
fix, not a discretionary choice between two equally defensible options, the same category as
DT-02's Round-1 resolution.

### What changed

`B04` §3b (new)/§3c (new)/event table (FiscalYearClosed row, propagated from §2) · `B05`
BINV-13 (new) · `B07` §1e (new formula, annotated once more at CORR-B3-06 per B20 Test 4) ·
`B09` CO-16 (new) · `B11` scenario 19 (new) · `B15` §3c (new) · `B19` Test 11 (annotated, kept
visible, not rewritten) · `B20` (new, all 15 tests).

## 2. CORR-B3-05 — Fiscal Close / MP-11 Semantics Resolution

### The problem, precisely

`M-AUD-07` found MP-11 (B08, added at CORR-B2-03/04) internally contradictory: it defined
Fiscal Year Close as posting a single Entry that debits every Revenue account and credits every
Expense account — but this domain's own B07 §1d and MP-02's post-closing paragraph both
independently claimed "Revenue/Expense accounts are never reset by any posted action." The
audit did not stop at naming the contradiction; tracing the literal wording further showed it
was a genuine arithmetic bug: such an Entry, dated anywhere within the Fiscal Year it closes,
would be included in that same year's own MP-09 aggregation for any as-of date within it,
corrupting the historical figure the Entry was trying to record — and dating it in the new
Fiscal Year instead simply moves the same contradiction one day forward (it would then reset
the NEW year's Revenue/Expense instead). The audit's explicit instruction was to resolve this
by choosing **exactly one** coherent model, not retaining both.

### The fix

**No-posted-close model adopted.** Fiscal Year Close (CAP-09, B02, corrected) performs exactly
one action: an authorized declaration (`FiscalYearClosed`, B04, corrected) that locks the
Fiscal Year and marks its Current Earnings as closed. It posts no Entry. B07 §1e (new) defines
**Reported Retained Earnings** as a derived reporting formula — the formally-designated
Retained Earnings account's own direct-posted balance (real direct postings only, e.g. dividend
declarations) plus the sum, over every closed Fiscal Year, of that year's Current Earnings
computed via MP-09 Mode 2. B08 MP-11 is rewritten to describe this formula instead of a posted
Entry, with the superseded Round-2 text kept fully visible above the correction (not deleted).

### Alternatives compared (per directive, not accepting the audit's suggested direction blindly)

Full comparison recorded at [B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-10 (new). In
summary: **Option A — retain a posted Fiscal-Year-Close Entry** (the Round-2 model) was found
to have no dating choice that avoids both defects simultaneously — this is not a tradeoff
between two workable options, it is a structural defect in Option A itself, confirmed by
tracing the arithmetic rather than merely accepting the audit's characterization. **Option B —
no posted Entry, derived formula (adopted)** is structurally immune to both defects (there is
no Entry to mis-date), and, as a direct consequence, automatically gives a later Restatement of
a closed Fiscal Year (§3c) a "flows through with no separate posting" property that Option A
could never have provided without yet another bespoke mechanism — retroactively validating (for
a corrected reason) what B19 Test 11 originally concluded about Prior Period Adjustment lines
being unnecessary.

### Mandatory proof (worked numerically, per directive)

[B20](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md) Tests 9-11 trace one continuing worked
example (Company X) through pre-close P&L, the close itself (no Entry), and the new Fiscal
Year's clean start — and, critically, **re-query the closing date itself from after the close**
to directly refute `M-AUD-07`'s traced corruption concern by showing the figure is unchanged
(Test 10). Test 12 extends the same example through a full Restatement after Fiscal Year Close,
confirming both the no-double-counting property and IAS 8 para 46's current-period-P&L
exclusion by direct arithmetic, not assertion. Test 14 further confirms a chained correction of
that Restatement composes correctly with BINV-11's Mode-1 guarantee (Round 2, unmodified).

### What changed

`B02` CAP-09 (posted-Entry language removed; "Earnings Transfer" in its name clarified as a
logical/reporting transfer, not a posted one) · `B04` event table (`FiscalYearClosed` row and
its explanatory paragraph corrected) · `B05` BINV-10 (rewritten a third time, Round-2 text kept
visible) · `B07` §1b/§1d (corrected)/§1e (new) · `B08` MP-02 (post-closing special case
corrected)/MP-11 (rewritten, Round-2 text kept visible) · `B13` DT-10 (new; DT-08's Option A
description annotated) · `B15` §3c.

## 3. CORR-B3-03 / CORR-B3-04 — Original vs. Restated History, and Retained Earnings / Opening Comparative Treatment

Both requirements are satisfied by the combination of CORR-B3-01/02's classification-and-
mechanics fix and CORR-B3-05's formula fix, not by a separate third mechanism:

- **Original vs. Restated History:** already-existing Round-2 machinery (Effective Date vs.
  Recorded At, B07 §1c; Mode 1 "as originally known" vs. Mode 2 "current/restated," B08 MP-09;
  CO-14's mandatory mode-labeling) is confirmed, not modified, to already satisfy IAS 8 para
  42(a)'s comparative-presentation requirement — verified explicitly at
  [B20](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md) Test 8. No new control was needed; this
  is recorded as a genuine cross-check finding (a Round-2 control designed for one stated
  reason turning out to satisfy a Round-3 standard-specific requirement), not assumed without
  verification.
- **Retained Earnings / Opening Comparative Treatment:** B07 §1e's formula, by construction,
  restates the opening Reported Retained Earnings figure for the earliest period presented
  whenever a closed Fiscal Year before that period is restated (IAS 8 para 42(b)) — verified
  numerically at B20 Test 3 — and accommodates both impracticability sub-cases (para 43/45)
  without requiring a structurally different formula, only the explicit annotation added this
  round (B07 §1e, per B20 Test 4's finding).

## 4. CORR-B3-06 — Accounting-Standard Regression

See [B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md) —
15/15 scenarios pass; one genuine formula-documentation gap in this round's own first-draft
B07 §1e was found and fixed during construction (Tests 4/5), in the same spirit as B18 Test 9,
B19 Test 9, and B19 Test 11 before it. Nine personas, exact 16-field schema per the directive.
Real worked numbers used throughout Tests 2-5, 9-12, and 14, built as one continuing scenario
(Company X) so each test's opening position is the prior test's verified closing position, not
a fresh, unverified assumption.

## 5. CORR-B3-07 — Propagation Check

Every artifact in the directive's "at minimum inspect/update" list was inspected: B02, B04,
B05, B07, B08, B09, B10, B11, B13, B15, B19, F, G, H, TEAM_B_STATUS.md. B10 was re-verified and
confirmed accurate without requiring a rewrite (MG-C03's opening balance remains structurally
distinct from both the corrected Fiscal Year Close and the new restatement mechanics — verified
at B20 Test 13). B12 was inspected and confirmed genuinely unaffected (AD-01..09 concern the
Consumption Gate, tamper-evidence, period control, currency, and multi-tenancy — none touch
Fiscal Year Close Entry semantics or error classification) — light-touch, no file edit, per the
same pattern Round 2 used for B12. B06, B01, B03, B14, B16, B18 were checked for
CORR-B3-01/02/05 dependencies and confirmed either unaffected or already addressed elsewhere.

## 6. CORR-B3-08 — Evidence / Push Verification

See [DOMAIN_01_ACCOUNTING_CORE_Q_CORR_B3_CLOSURE_EVIDENCE.md](DOMAIN_01_ACCOUNTING_CORE_Q_CORR_B3_CLOSURE_EVIDENCE.md)
and [SESSION_ARCHIVE/SESSION_SMEPLUS-26-08-29-MIG-B-D01-CORR3-001_CLOSURE.md](SESSION_ARCHIVE/SESSION_SMEPLUS-26-08-29-MIG-B-D01-CORR3-001_CLOSURE.md).

## 7. Six Assumptions — Status After This Round

```
1. Rounding method .................................. OPEN, unchanged
2. Period close / Consumption ....................... OPEN, unchanged this round (see B15 §6
                                                        Round 3 note — this round's subject
                                                        matter does not bear on reopen/
                                                        consumption timing at all)
3. COA template/instance ............................. OPEN, unchanged
4. Broad audit tamper-evidence scope .................. OPEN, unchanged
5. Correction shape flexibility ....................... OPEN, unchanged
6. CO-02/CO-06 coupling ............................... OPEN, unchanged
```

**No assumption was resolved by Team B fiat, and none was narrowed this round either** —
unlike Round 1 and Round 2, where the specific findings under correction directly bore on
assumption #2's subject matter, Round 3's findings (error/estimate/materiality classification,
Fiscal Year Close posting semantics) do not touch any of the six assumptions' subject matter.
Materiality itself — the one genuinely new judgment-input concept this round introduces — is
explicitly NOT added as a seventh assumption, because CO-16 (B09, new) already closes it as a
settled design decision (materiality is permanently out of this domain's computation scope,
supplied externally), not an open question deferred to Boss. This distinction — a new concept
that is fully resolved by design vs. a genuinely open question awaiting Boss judgment — is
itself recorded explicitly so the six-assumption count is never inflated or deflated without
a stated reason.
