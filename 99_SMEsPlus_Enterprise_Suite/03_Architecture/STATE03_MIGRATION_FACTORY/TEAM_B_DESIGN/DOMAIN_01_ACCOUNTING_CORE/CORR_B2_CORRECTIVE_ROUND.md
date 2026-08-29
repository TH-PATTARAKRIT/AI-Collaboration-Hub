# CORR-B2 — Targeted Corrective Round 2: Temporal Truth + Fiscal Close

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-29-MIG-B-D01-CORR2-001 |
| Domain | DOMAIN_01 — Accounting Core |
| Source of truth | ChatGPT Independent Team B Design Re-Audit Round 2, commit `04e44b06489d8bea6c8d39410050d68cf08bce21`, verified against the live repository before any correction was made |
| Scope | Targeted correction of exactly two material findings (`M-AUD-04`, `M-AUD-05`). B0–B18 not restarted. No code. No DOMAIN_02. No PMO. No self-approval. |

## 0. CORR-B2 Change Log (required schema)

| finding_id | old_statement_or_rule | corrected_statement_or_rule | affected_artifacts | reason | verification_status |
|---|---|---|---|---|---|
| M-AUD-04 | B08 MP-09 (Round 1): historical reproducibility held "provided no Correction/Void dated <= D is committed since" — a proviso, not a structural guarantee; B11 Scenario 10: backdating has "no special rule," including for corrections | Entry split into Effective Date (business date) and Recorded At (system-generated, immutable, B07 §1c/BINV-12); MP-09 rebuilt as two modes — Mode 1 ("as originally known," filtered by Effective Date AND Recorded At) is a provable fixed point once its recording-time parameter has passed; Mode 2 ("current/restated") reflects later corrections by design. A Correction/Void backdated into an already-consumed period is classified a Restatement (B04 §3a), with its own authorization tier (CO-15) | B07 §1c, B08 MP-09, B05 BINV-11/12, B04 §3a/§4, B09 CO-14/15, B11 scenario 10, B13 DT-09, B15 §3b | Round 1's proviso was insufficient: a backdated Correction always satisfies "date <= D," so the proviso could always be violated — the guarantee needed to depend on something that CANNOT be backdated (Recorded At), not on a rule someone must follow (no backdating) | VERIFIED — B19 Tests 4-7 |
| M-AUD-05 | B02 CAP-09 (Round 1): "Period-End Carry-Forward" — posts an opening-balance fact at every ordinary Period close, transferring Current Earnings and resetting Revenue/Expense; B05 BINV-10: "opening balance of period N+1 equals closing balance of period N ... computed by CAP-09" | Continuous Ledger adopted (B07 §1d): Asset/Liability/Equity accumulate all-time, nothing is posted at ordinary Period close, so nothing can double-count. CAP-09 renamed/rescoped to Fiscal Year Close only, posting exactly one Current-Earnings-transfer Entry (MP-11). Revenue/Expense are Fiscal-Year-bounded by the aggregation formula itself (B08 MP-09), never reset by a posted action | B02 CAP-09, B07 §1b/§1d (Fiscal Year entity, Current Earnings re-bounded), B05 BINV-10, B08 MP-02/MP-09/MP-11, B10 MG-C03/C07/C14, B13 DT-08, B15 §3b | B01 BF-09 (authorized evidence) is explicitly year-end; generalizing it to every ordinary Period close, combined with all-time summation, produces exactly the double-count `M-AUD-05` identified — confirmed it would have produced Feb Cash = 200, not 100, in B19 Test 1's scenario | VERIFIED — B19 Tests 1, 8, 9, 10 |
| (regression finding, not an audit ID) | B04 §3a (as first drafted this round): a Restatement crossing a closed Fiscal Year boundary requires a mandatory backdated "Prior Period Adjustment" line against Retained Earnings | Corrected: the simpler, standard treatment (ordinary current-dated recognition of a prior-period error) is sufficient for current Balance Sheet correctness; the mandatory backdated adjustment line is not required and was over-engineered | B04 §3a | Found while working B19 Test 11 with real numbers — the first-draft requirement needed a clearing mechanism this domain never designed and does not actually need | VERIFIED — B19 Test 11 |

## 1. CORR-B2-01 / CORR-B2-02 — Temporal Truth Model and Backdated-Correction Control

### The problem, precisely

Round 1 fixed VOID's current-status filtering (`D01-B-AUD-03`) but left a single-date Entry
model in place. `M-AUD-04` found this insufficient: nothing prevented a Correction, committed
today, from claiming an Effective Date inside an already-consumed, reopened historical
period — and Round 1's BINV-11 proviso ("provided no Correction/Void dated <= D...") could
always be violated by exactly this maneuver, since a backdated Correction trivially satisfies
"dated <= D."

### The fix

Entry now carries two independent temporal properties (B07 §1c): **Effective Date**
(business-meaningful, determines Period/Fiscal-Year membership) and **Recorded At**
(system-generated at the instant of commitment, immutable, BINV-12 — new). MP-09 (B08) is
rebuilt around two aggregation modes:

- **Mode 1 — "as originally known"**: filtered by Effective Date <= D AND Recorded At <= T.
  Provably a fixed point once T has passed, unconditionally — no Entry committed after T can
  ever satisfy "Recorded At <= T," regardless of what Effective Date it claims.
- **Mode 2 — "current/restated"**: filtered by Effective Date <= D only. Intentionally
  reflects later, legitimate corrections.

A Correction/Void whose target has independent Consumption AND whose Effective Date falls
within the period that Consumption covers is classified a **Restatement** (B04 §3a) — a
distinguished correction purpose, producing its own `Restated` event and requiring CO-15's
stricter authorization tier. This satisfies `M-AUD-04`'s explicit requirement that a
restatement never be "silently indistinguishable" from an ordinary correction.

### Alternatives compared (per directive, not accepting the suggested direction blindly)

Query-layer safety (Mode 1's structural guarantee) alone would close the *data-correctness*
half of the finding but leave a human/process-error gap (nothing at the write layer flags a
backdated correction as different from a routine one). Write-layer distinction
(Restatement/CO-15) alone would close the process-visibility half but not the underlying
mathematical guarantee. **Both were adopted together** ([B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md)
DT-09) — neither is sufficient alone, and the combination directly answers both clauses of
`M-AUD-04`'s acceptance requirement ("must never silently change" + "if a formal restatement
... must remain independently reconstructable").

### What changed

`B04` §2/§3/§3a (new)/§4/§9 · `B05` BINV-11 (rewritten), BINV-12 (new) · `B07` §1c (new) ·
`B08` MP-09 (rebuilt) · `B09` CO-14/CO-15 (new) · `B11` scenario 10 (rewritten) ·
`B13` DT-09 (new) · `B15` §3b (new).

## 2. CORR-B2-03 / CORR-B2-04 / CORR-B2-05 — Fiscal Year Close and Carry-Forward

### The problem, precisely

`M-AUD-05` found B01's authorized evidence (BF-09) is explicitly year-end, but B02's CAP-09
generalized it to *every* ordinary Period close — and, combined with MP-09's all-time
summation, this created a real double-counting risk: a posted "opening balance" Entry at
every month/quarter boundary, on top of historical activity MP-09 already counted.

### The fix

**Continuous Ledger model adopted** (B07 §1d, compared against a Segmented-Period
alternative in [B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-08): Asset/Liability/Equity
accumulate all-time with no periodic re-assertion — carry-forward across an ordinary Period
boundary is *implicit*, a consequence of the aggregation formula, not a posted fact. Nothing
is posted at ordinary Period close, so nothing can double-count. **CAP-09 renamed and
rescoped** to Fiscal Year Close only (B02), posting exactly one Entry (MP-11, new) that
transfers Current Earnings into formal Equity. Revenue/Expense accounts are bounded by the
current Fiscal Year in MP-09's aggregation itself (B08) — their zero-point for a new Fiscal
Year is automatic, not a reset anyone performs.

MP-02's reconciliation (CORR-B2-05): the expanded equation
(`Assets + Expenses = Liabilities + Equity + Revenue`) is unaffected — Current Earnings is
now explicitly Fiscal-Year-bounded rather than "since the last close," and the post-closing
special case is now correctly tied to Fiscal Year Close specifically, not ordinary Period
close. Verified to hold before, during, immediately after, and following Fiscal Year Close,
with real worked numbers ([B19](B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md) Tests 8-10).

### Mandatory proof (worked numbers, per directive)

All four required tests (A: month boundary, B: YTD P&L, C: fiscal-year close, D: migration
opening balance) were performed with real figures — see
[B19](B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md) Tests 1, 8, 9/10, 12 respectively. Test 9
is deliberately left showing a first, internally-inconsistent attempt at illustrative figures
before the corrected, self-consistent trial balance — shown, not polished away.

### What changed

`B02` CAP-09 (renamed/rescoped) · `B04` §3/§9 (event table) · `B05` BINV-10 (rewritten) ·
`B07` §1 (Fiscal Year entity, new), §1b (Current Earnings re-bounded), §1d (new) · `B08` MP-02
(reconciled), MP-09 (category-bounded), MP-10 (clarified), MP-11 (new) · `B10` MG-C03/C07/C14 ·
`B13` DT-08 (new) · `B15` §3b.

## 3. CORR-B2-06 — Terminology Precision

`M-AUD-05`'s §5 non-blocking note (the ambiguity of "every COMMITTED Entry" once VOIDED/
SUPERSEDED exist as labels) is resolved by construction, not by inventing a new term: since
Round 2's MP-09 never filters by status at all (only by the two temporal axes), there is no
remaining ambiguity for a new term to disambiguate — "every COMMITTED Entry" in this domain's
current design already means, precisely, every Entry whose Lines are eligible by date,
regardless of any label later attached to it.

## 4. CORR-B2-07 — Propagation Check

Every artifact in the directive's "at minimum inspect/update" list was inspected: B02, B04,
B05, B07, B08, B10, B11, B13, B15, B18 (superseded by B19 for Round 2 scenarios, not
deleted), F, G, H, TEAM_B_STATUS.md. Additional propagation found necessary beyond the
minimum list: B09 (CO-14/CO-15, required by B04/B08's own new cross-references) and B12
(light-touch note — Round 2 did not require any change to AD-01..09's objectives or
measurement criteria, confirmed by inspection, not assumed).

## 5. CORR-B2-08 — Focused Red-Team Regression

See [B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md](B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md) —
15/15 scenarios pass; one over-engineered requirement in this round's own first draft was
found and corrected during construction (Test 11).

## 6. Six Assumptions — Status After This Round

```
1. Rounding method .................................. OPEN, unchanged
2. Period close / Consumption ....................... REVISED AGAIN (narrower than after
                                                        Round 1 — see B15 §6)
3. COA template/instance ............................. OPEN, unchanged
4. Broad audit tamper-evidence scope .................. OPEN, unchanged
5. Correction shape flexibility ....................... OPEN, unchanged (Restatement is a
                                                        new named instance, not a new
                                                        question)
6. CO-02/CO-06 coupling ............................... OPEN, unchanged
```

**No assumption was resolved by Team B fiat.** Assumption #2's further narrowing is a
consequence of closing a real internal-consistency gap (`M-AUD-04`), exactly as its Round 1
narrowing was — not a judgment call made on Boss's behalf.
