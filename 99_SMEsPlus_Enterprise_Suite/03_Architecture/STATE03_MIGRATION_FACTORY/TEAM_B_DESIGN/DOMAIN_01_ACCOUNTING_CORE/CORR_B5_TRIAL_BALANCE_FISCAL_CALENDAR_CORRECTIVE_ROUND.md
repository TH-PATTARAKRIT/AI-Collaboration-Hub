# CORR-B5 — Targeted Corrective Round 5: Trial Balance Horizon Integrity & Fiscal Calendar Historical Safety

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-30-MIG-B-D01-CORR5-001 |
| Domain | DOMAIN_01 — Accounting Core |
| Source of truth | ChatGPT Independent Team B Design Re-Audit Round 5, commit `de7492afd0af0f58185f3f36940a77f2389aa8b8`, verified against the live repository before any correction was made |
| Scope | Targeted correction of exactly two findings (`M-AUD-11`, `M-AUD-12`). B0–B21 not restarted. No code. No DOMAIN_02. No PMO. No self-approval. Jira assignee/due date preserved as governance red flags, not invented. |

## 0. CORR-B5 Change Log (required schema)

| finding_id | old_statement_or_rule | corrected_statement_or_rule | affected_artifacts | reason | verification_status |
|---|---|---|---|---|---|
| M-AUD-11 | B08 MP-09 (Round 2-4): defines category-bounded account balances (Asset/Liability/Equity all-time, Revenue/Expense Fiscal-Year-bounded) as its single output. B08 MP-12 Proof G (Round 4): "The Raw Trial Balance is MP-09's direct output for every account... It balances via Proof A + MP-09's existing category-bounded aggregation." | MP-09 renamed and split into `CumulativeAccountBalance_Current/Known` (one common horizon, every category, the true raw formula) and `FiscalYearActivity_Current/Known` (Revenue/Expense only, Fiscal-Year-bounded, never itself a Trial Balance). MP-12 Proof G rebuilt into G1 (Raw Cumulative Trial Balance — genuinely balanced), G2 (Current-Fiscal-Year Reporting Balance — explicitly NOT balanced once any Fiscal Year has elapsed), G3 (Balanced Presentation Trial Balance — G2 plus one explicit, permanently-not-postable derived bridge line), G4 (Known vs. Current, applied to G1-G3). | B02 CAP-09 (light touch), B05 BINV-15 (new), B08 MP-09 (renamed/split)/MP-12 (Proof G rebuilt), B09 CO-14 (extended), B10 MG-C11 (corrected), B15 §3e, B20/B21 (terminology annotations, no rewrite) | MP-12 Proof G reused Proof A's name and conclusion for a mixed-horizon quantity without re-checking whether Proof A's precondition (one common horizon) still held for it — it did not, once any Fiscal Year had elapsed. Verified against Team B's own B21 Test 5 numbers: mixed-horizon debit 1250 vs. credit 1000, off by exactly 250 (the prior elapsed Fiscal Year's Current Earnings) | VERIFIED — B22 Tests 1-4 (including the exact failure case, now correctly labeled and resolved) |
| M-AUD-12 | B07 §1e (Round 4): the Elapsed test compares a query date against a Fiscal Year's Start/End boundary, deliberately taking no viewpoint parameter, treating the boundary as a timeless fact. No invariant protected that boundary from retroactive editing. | B07 §1h (new): a Versioned Fiscal Calendar model — pre-reliance boundary corrections remain free and ungated; post-reliance changes require a new, CO-15-tier-or-stricter `FiscalYearBoundaryChanged` Audit Event (B04, new), never a silent overwrite, with the old boundary version permanently queryable for Known-viewpoint reconstruction, and no automatic reclassification of existing COMMITTED Entries' Fiscal-Year membership. | B02 CAP-09 (light touch), B04 (new event), B05 BINV-16 (new), B07 §1h (new), B09 CO-15 (extended), B10 MG-C16 (new), B11 scenario 21 (new), B13 DT-12 (new), B15 §3e/§6 (new seventh assumption) | Nothing protected a Fiscal Year's calendar configuration from silent retroactive editing — `Recorded At` (BINV-12) protects Entry-level backdating, but the boundary those Entries are measured against had no equivalent protection, risking a silent defeat of BINV-11's reproducibility guarantee from a direction never previously covered | VERIFIED — B22 Tests 12-15 (an attempted silent edit routed through controlled semantics, a post-consumption report remaining reproducible, an authorized future-dated change, and multi-company isolation) |

## 1. CORR-B5-01 / CORR-B5-02 — Separate Raw Cumulative Balance from Category-Bounded Reporting Balance; Repair MP-09 Semantics

### The problem, precisely

`M-AUD-11` found that MP-09's category-bounded aggregation (Balance Sheet all-time, Income
Statement Fiscal-Year-bounded) was silently treated, by MP-12 Proof G, as if it were the same
population MP-12 Proof A proved balances — but Proof A's identity holds only when every
category shares one common horizon. Truncating Revenue/Expense to the current Fiscal Year
while leaving Equity all-time (uncorrected for prior elapsed years' earnings) produces a set of
numbers that does not sum to Proof A's identity once any Fiscal Year has elapsed. This is not a
labeling nuance; it is a genuine arithmetic contradiction, confirmed by tracing Team B's own
prior-round numbers (Company X, Jan 5 2025: 1250 debit vs. 1000 credit, off by exactly 250).

### The fix

MP-09 is renamed from "Aggregation (Account Balance / Trial Balance)" to "Cumulative Account
Balance & Fiscal-Year Activity" — removing "Trial Balance" from its own name — and split into
two formula families: `CumulativeAccountBalance_Current/Known` (the pure, single-horizon raw
formula, defined identically for every Account Category, inheriting the Mode 1/Mode 2 viewpoint
mechanism unchanged) and `FiscalYearActivity_Current/Known` (a new, narrower pair, meaningful
for Revenue/Expense specifically, Fiscal-Year-bounded, never itself claimed to be a Trial
Balance). B07 §1b's Current Earnings and §1e's Reported Retained Earnings formula are both
corrected to cite `FiscalYearActivity` explicitly rather than bare "Mode 2."

## 2. CORR-B5-03 / CORR-B5-04 — Balanced Reporting/Presentation TB; Re-Prove MP-12 Proof G

### The fix

MP-12 Proof G is rebuilt into four sub-proofs, exactly as required: **G1 — Raw Cumulative
Trial Balance** (every category, `CumulativeAccountBalance_Current`, balances directly and
unconditionally — this is the only object entitled to be called a "Trial Balance" without
further qualification). **G2 — Current-Fiscal-Year Reporting Transformation** (the mixed-horizon
per-account set MP-09 previously conflated with a Trial Balance — a genuine, useful reporting
view, explicitly and permanently never labeled "balanced"). **G3 — Balanced Presentation Trial
Balance** (G2 plus exactly one further line — "Accumulated Elapsed-Fiscal-Year Earnings,"
labeled `DERIVED PRESENTATION COMPONENT — NOT A POSTED FINANCIAL FACT` — restoring balance
exactly; this bridge line is identical to Reported Retained Earnings' own second summand, B07
§1e, reused rather than duplicated). **G4 — Known vs. Current, applied to G1-G3** (every
quantity in G1/G2/G3 has a Known-viewpoint counterpart, built the same way every other
Known-viewpoint quantity in this design is built).

CO-14 (B09) is extended to require every presentation to explicitly label which of G1/G2/G3 it
is showing — the same "do not let one silently masquerade as the other" principle CO-14 has
enforced since Round 2, now covering a case this domain's own Round-4 design had itself
violated. New BINV-15 (B05) formalizes the non-confusion requirement as an invariant.

### Mandatory proof (worked numerically, per directive)

[B22](B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md) Tests 1-4 prove all three
outputs across the required checkpoints (mid-first-Fiscal-Year, first-day-of-second-Fiscal-Year
— the audit's own exact numbers — and the explicit bridge tie-out), and Tests 5-9 extend the
proof through a delayed operational close window and a later Restatement, exactly as required.

### What changed

`B02` CAP-09 (light touch) · `B05` BINV-15 (new) · `B08` MP-09 (renamed/split), MP-12 (Proof G
rebuilt, Principle statement corrected) · `B09` CO-14 (extended) · `B10` MG-C11 (corrected) ·
`B15` §3e · `B20`/`B21` (terminology annotations, no rewrite — both documents' own arithmetic
was already correct; only B08's prose had conflated the concepts).

## 3. CORR-B5-05 — Protect Fiscal-Year Boundaries from Silent Historical Reclassification

### The problem, precisely

`M-AUD-12` found that B07 §1e's Elapsed test (Round 4) deliberately takes no viewpoint
parameter, reasoning that a calendar boundary is a pure, timeless fact — correct as far as it
went, but nothing in the Round-4 design actually protected that boundary from being
retroactively edited after Entries, Elapsed determinations, or issued reports had already
relied on it. A silent change could alter which Fiscal Years are Elapsed at any date, which
Lines belong to which Fiscal Year's Current Earnings, and what any Known-viewpoint
reconstruction produces — with no Entry, Correction, Restatement, or (before this correction)
even an Audit Event marking the change.

### The fix

**Versioned Fiscal Calendar model adopted** (B07 §1h, new): a Fiscal Year's boundary is itself
a versioned, effective-dated fact, mirroring the Effective-Date/Recorded-At split (§1c) and the
Known/Current split (§1g) this design already uses elsewhere. Pre-reliance corrections update
the one current version harmlessly. Post-reliance changes require a new `FiscalYearBoundaryChanged`
Audit Event (B04, new) at an authorization tier at least as strict as Restatement (CO-15,
reused). The old version remains permanently queryable for Known-viewpoint reconstruction; a
boundary change alone never moves an existing COMMITTED Entry's Fiscal-Year membership without
a further, separately-gated reclassification action.

### Alternatives compared (per directive, not accepting the suggested direction blindly)

Three models compared at [B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-12. **Option A —
boundary immutability after first authoritative use (rejected):** simplest in the abstract, but
forces an awkward "abandon and recreate" workaround even for a harmless, immediately-caught
configuration mistake, since it does not distinguish pre- from post-reliance changes. **Option B
— Versioned Fiscal Calendar (adopted):** strictly generalizes Option A's protection everywhere
it actually matters (post-reliance behavior is functionally Option A's rule) while adding a
narrow, harmless escape hatch for the pre-reliance case, reusing this design's own established
vocabulary rather than inventing a parallel "frozen bit" concept. **Option C — a different
model (rejected):** no alternative was found that preserves historical reproducibility as
strongly as Option B while being simpler; a bespoke third mechanism would only duplicate
versioning + authorization-tiering machinery this design already has.

**A genuinely new, seventh Team B assumption is flagged** (not hidden inside B07 §1h's prose,
per explicit directive instruction): the exact authorization tier for a post-reliance boundary
change is a real open policy question this domain's own evidence does not settle — CO-15's
tier is stated as this domain's working default, not asserted as the evidence-derived answer
materiality (CO-16) or the designated Retained Earnings account (MG-C15) were.

### Mandatory proof (worked numerically, per directive)

[B22](B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md) Tests 12-15 trace an
attempted silent edit (refused, routed through controlled semantics), a post-consumption
report's continued reproducibility, an authorized future-dated calendar change (touching no
historical Entry's membership), and multi-company calendar isolation.

### What changed

`B02` CAP-09 (Fiscal Year boundary governance, light extension) · `B04` new
`FiscalYearBoundaryChanged` event · `B05` BINV-16 (new) · `B07` §1h (new) · `B09` CO-15
(extended) · `B10` MG-C16 (new — migration-time calendar setup is always pre-reliance) · `B11`
scenario 21 (new) · `B13` DT-12 (new) · `B15` §3e/§6 (new seventh assumption).

## 4. CORR-B5-06 — Targeted Regression

See [B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md](B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md) —
15/15 scenarios pass. This is the second consecutive round (after B21) whose own regression
construction did not surface a further defect requiring correction — recorded honestly, per
[G §4e](DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md), as a fact about this round's
process, not a claim that the underlying difficulty in this domain's reporting-mathematics
core has fully resolved.

## 5. CORR-B5-07 — Propagation Check

Every artifact in the directive's "at minimum inspect/update" list was inspected: B02, B04,
B05, B07, B08, B09, B10, B11, B13, B15, B21, F, G, H, TEAM_B_STATUS.md. B20 was additionally
touched (a terminology annotation, no rewrite — its own Round-3 arithmetic was never wrong).
B12, B14, B16, B18, B19 were checked for CORR-B5-01/02/05 dependencies and confirmed
unaffected.

## 6. CORR-B5-08 — Evidence / Push Verification

See [DOMAIN_01_ACCOUNTING_CORE_W_CORR_B5_CLOSURE_EVIDENCE.md](DOMAIN_01_ACCOUNTING_CORE_W_CORR_B5_CLOSURE_EVIDENCE.md)
and [SESSION_ARCHIVE/SESSION_SMEPLUS-26-08-30-MIG-B-D01-CORR5-001_CLOSURE.md](SESSION_ARCHIVE/SESSION_SMEPLUS-26-08-30-MIG-B-D01-CORR5-001_CLOSURE.md).

## 7. Six (Now Seven) Assumptions — Status After This Round

```
1. Rounding method .................................. OPEN, unchanged
2. Period close / Consumption ....................... OPEN, unchanged this round
3. COA template/instance ............................. OPEN, unchanged
4. Broad audit tamper-evidence scope .................. OPEN, unchanged
5. Correction shape flexibility ....................... OPEN, unchanged
6. CO-02/CO-06 coupling ............................... OPEN, unchanged
7. Fiscal Year boundary change authorization tier ..... NEW this round — OPEN
```

**Assumptions #1-6 were not resolved by Team B fiat, and none was narrowed this round** —
Round 5's findings (Trial Balance output labeling, Fiscal Calendar historical safety) are pure
internal-consistency/mathematics corrections with no bearing on their subject matter. **A
genuine seventh assumption was added, per explicit directive instruction to flag it rather than
hide it inside prose** — the exact authorization tier for a post-reliance Fiscal Year boundary
change is a real open policy question this domain's own evidence does not settle; CO-15's tier
is stated as a working default, not the evidence-derived answer.

## 8. Jira Governance Facts — Preserved, Not Invented

Per explicit instruction, `ERPPLUS-100`'s Assignee (`UNASSIGNED`) and Due Date (`TBD`/empty)
are preserved exactly as found — flagged as PMO/governance red flags in the evidence comment,
never filled in by this executor.
