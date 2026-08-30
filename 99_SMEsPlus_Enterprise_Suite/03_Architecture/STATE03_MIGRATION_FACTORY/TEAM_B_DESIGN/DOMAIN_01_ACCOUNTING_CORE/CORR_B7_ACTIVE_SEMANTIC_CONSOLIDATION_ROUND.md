# CORR-B7 — Targeted Corrective Round 7: Active Semantic Consolidation & Dependency Hygiene

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-30-MIG-B-D01-CORR7-001 |
| Domain | DOMAIN_01 — Accounting Core |
| Source of truth | ChatGPT Independent Team B Design Re-Audit Round 7, commit `c22f236d0bf8b550636fc665a04c46281ca3d017`, verified against the live repository before any correction was made |
| Scope | Targeted correction of exactly two findings (`M-AUD-15`, `M-AUD-16`) plus one controlled active-semantic consistency sweep across the authoritative design pack, per explicit directive instruction to also fix any other artifact actually found stale. B0–B24 not restarted. No code. No DOMAIN_02. No PMO. No self-approval. Jira assignee/due date preserved as governance red flags, not invented. |

## 0. CORR-B7 Change Log (required schema)

| finding_id | old_statement_or_rule | corrected_statement_or_rule | affected_artifacts | reason | verification_status |
|---|---|---|---|---|---|
| M-AUD-15 | B02 CAP-04: "Outputs: ...a closed-period record that CAP-06 relies on for carry-forward. Downstream dependents: CAP-02..., CAP-06 (defines when carry-forward is triggered)..." | CAP-04's Outputs/Downstream-dependents corrected to name only CAP-02, CAP-08, and external reporting; explicit statement that ordinary carry-forward is implicit (B07 §1d) and is never output or triggered by this or any capability; explicit statement that CAP-06 has never actually been a downstream dependent of CAP-04. | B02 CAP-04, B15 §3g/§8a | CAP-06 is Currency Recognition & Remeasurement — it has never had any role in carry-forward. Ordinary carry-forward became implicit at CORR-B2-03/04; CAP-04's own text was never revisited when that redesign happened, and has carried this stale claim, unedited, since the original B02 pass — through all six prior corrective rounds | VERIFIED — B24 Tests 1, 14 |
| M-AUD-16 | B07 §1 entity table, Consumption Record row: "...downstream reference — including CAP-09's own carry-forward, which references the prior period's closing Entries — is observed within this domain" | The stale example replaced with a currently-valid one: a Correction/Reversal Entry (B04 §6), which genuinely is "computed from or references" the Entry it targets. Explicit statement added that no Period/Fiscal-Year lock or boundary event (`PeriodClosed`/`FiscalYearClosed`/`FiscalYearBoundaryChanged`/`FiscalYearMembershipRestated`) is an automatic Consumption trigger. | B07 §1 (Consumption Record row), B15 §3g/§8a | `CarriedForward` was removed as an event at CORR-B2-03/04; CAP-09/Fiscal Year Close has posted no financial Entry, and referenced no prior Entry, since CORR-B3-05 — there is no CAP-09 carry-forward left to be this trigger's example. This row was itself edited at CORR-B01 (trigger count corrected from four to three) without the same edit re-examining its own illustrative example, which was already, in that same round, describing a mechanism CORR-B01 was narrowing | VERIFIED — B24 Tests 2, 12 |

**Two further items found and corrected during this round's own CORR-B7-03/04 sweep, beyond
the two audit-named findings** (disclosed per this domain's standing transparency discipline):

| item | old_statement_or_rule | corrected_statement_or_rule | affected_artifacts | reason | verification_status |
|---|---|---|---|---|---|
| Self-found (a) | B02 CAP-01: "Downstream dependents: CAP-02..., CAP-06 (statement placement), all reporting/consolidation..." | The CAP-06 claim removed; downstream dependents corrected to CAP-02 and external reporting/consolidation only. | B02 CAP-01, B15 §3g/§8a | The same shape of defect as `M-AUD-15` — CAP-06 (Currency Recognition & Remeasurement) has never consumed statement placement, which is a reporting-layer concern already covered by the adjacent clause | VERIFIED — B24 Test 14 |
| Self-found (b) | B02 CAP-08: "Inputs: every state-changing action from CAP-02, CAP-03, CAP-04." | Corrected to also list CAP-07 and CAP-09, both of which separately state, in their own sections, that they feed CAP-08 directly. | B02 CAP-08, B15 §3g/§8a | An internal inconsistency (not a claim about a removed mechanism) found by the same systematic cross-check: CAP-07 and CAP-09 each already claimed CAP-08 as a downstream dependent, but CAP-08's own Inputs field never reciprocated | VERIFIED — B24 Test 14 |
| Self-found (c) | F §10: "Eleven conceptual entities" | Corrected to "Twelve" | F §10 | A milder class of staleness than (a)/(b) — not a claim about a removed mechanism, but an unmaintained summary count: F's own §10 was never updated after the Fiscal Year entity was added to B07 at Round 2, and has undercounted by one ever since | VERIFIED — direct count against B07 §1's current entity table |

## 1. CORR-B7-01 — Fix CAP-04 Active Dependency / Carry-Forward Stale Semantics

### The problem, precisely

`M-AUD-15` found CAP-04's own active Outputs/Downstream-dependents text still claimed a
closed-period record is something "CAP-06 relies on for carry-forward," and named CAP-06 as
the capability that "defines when carry-forward is triggered." This is doubly wrong: CAP-06 is
Currency Recognition & Remeasurement, with no carry-forward role at any point in this design's
history, and "carry-forward" itself has been implicit (no triggered event at all) since
CORR-B2-03/04. This text predates every corrective round — CAP-04 has never once appeared in
any prior round's own "Corrected" header row, even though the concept it references was
completely redesigned twice (CORR-B2-03/04, CORR-B3-05).

### The fix

CAP-04's Outputs corrected to: an open/closed determination and an authorized reopen action,
consultable by CAP-02, with an explicit statement that this determination is never itself a
carry-forward fact and triggers no carry-forward mechanism. Downstream dependents corrected to
CAP-02 (gates commitment/amendment), CAP-08 (every close/reopen is itself audit-evidenced —
new this round), and external financial reporting (a legitimate consumer of "what is frozen,"
never a claim about carry-forward). The stale CAP-06 claim is struck through, not deleted, with
an explicit correction note.

### Mandatory check (re-check every capability edge, per directive)

Performed as [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §8a's Dependency Sanity Matrix — every
CAP-01..09 Inputs/Outputs/Downstream-dependents field re-read against the actual current
definition of every capability it names. Found two further stale/incomplete edges beyond
`M-AUD-15` itself (self-found (a)/(b), above), both corrected in the same pass.

### What changed

`B02` CAP-01 (self-found (a)), CAP-04 (`M-AUD-15`), CAP-08 (self-found (b)) · `B15` §3g (new),
§8a (new).

## 2. CORR-B7-02 — Fix B07 Consumption Record Stale CAP-09 Carry-Forward Example

### The problem, precisely

`M-AUD-16` found the §1 entity table's Consumption Record row still named, as its active
illustration of downstream-reference Consumption, "CAP-09's own carry-forward, which references
the prior period's closing Entries." `CarriedForward` was removed as an event at CORR-B2-03/04;
CAP-09/Fiscal Year Close has posted no financial Entry, and referenced no prior Entry, since
CORR-B3-05. This row was edited once before, at CORR-B01, but that edit corrected only the
trigger count (four to three) — it never re-examined the row's own illustrative example, which
was, in that same round, already describing a mechanism CORR-B01 was in the process of
narrowing.

### The fix

The stale example replaced with a currently-valid one: a Correction or Reversal Entry (B04
§6), which genuinely is "computed from or references" the Entry it targets — squarely within
trigger (3)'s own definition, and unaffected by any of the six prior corrective rounds. An
explicit statement added, per the directive's own instruction, that none of `PeriodClosed`,
`FiscalYearClosed`, `FiscalYearBoundaryChanged`, or `FiscalYearMembershipRestated` is an
automatic Consumption trigger merely because the event exists.

### Mandatory reconciliation (per directive)

Reconciled directly against: B04 §4's three trigger kinds (the replacement example is trigger
(3), correctly instantiated); B05 BINV-06/07 (Consumption permanence, unaffected — a Correction/
Reversal triggering Consumption on its TARGET Entry is fully consistent with BINV-06's existing
scope); CAP-09's current no-posted-close semantics (confirmed there is genuinely nothing left
for the old example to point at); the current Fiscal Calendar versioning/restatement model (B07
§1h/§1j, confirmed none of its four events touches Consumption at all).

### What changed

`B07` §1 (Consumption Record row) · `B15` §3g (new), §8a (new).

## 3. CORR-B7-03 — Active-Semantic Consistency Sweep

### Method

A systematic grep-and-inspect sweep across the full authoritative design pack for every
high-risk term the directive named (`carry-forward`, `CarriedForward`, `earnings transfer`,
`opening balance`, `reset`, `CAP-06`, `CAP-09`, `PeriodClosed`, `FiscalYearClosed`, `Consumed`,
`freeze`, `Trial Balance`, `Mode 1/Mode 2`, `FiscalYearStart`, `Elapsed`,
`FiscalYearBoundaryChanged`, `FiscalYearMembershipRestated`), classifying every hit as
Active-Valid, Active-Stale, or Historical-OK.

### Stale-semantics register (complete)

| Candidate | File/Location | Classification | Disposition |
|---|---|---|---|
| "CAP-06 relies on for carry-forward" / "CAP-06 (defines when carry-forward is triggered)" | B02 CAP-04 Outputs/Downstream-dependents | Active-Stale (`M-AUD-15`) | **CORRECTED** |
| "CAP-06 (statement placement)" | B02 CAP-01 Downstream-dependents | Active-Stale (self-found) | **CORRECTED** |
| "every state-changing action from CAP-02, CAP-03, CAP-04" (incomplete) | B02 CAP-08 Inputs | Active-Incomplete (self-found) | **CORRECTED** |
| "CAP-09's own carry-forward, which references the prior period's closing Entries" | B07 §1 Consumption Record row | Active-Stale (`M-AUD-16`) | **CORRECTED** |
| "period closes; CAP-09 transfers Current Earnings... resets Revenue/Expense to zero" | B18 Test 5 scenario text | Historical-but-never-labeled (self-found) | **ANNOTATED** (numeric conclusion unaffected, never wrong) |
| CAP-09 title "& Earnings Transfer" | B02 CAP-09 heading | Active-Ambiguous (audit's explicit CORR-B7-05 concern) | **RENAMED** to "& Boundary Governance" |
| "Eleven conceptual entities" | F §10 | Active-Stale-Count (self-found — a milder class, an unmaintained summary count, not a claim about a removed mechanism) | **CORRECTED** to "Twelve" |
| BINV-10 "Carry-Forward Correctness," all occurrences | B05 | Active-Valid | none — describes the CURRENT implicit mechanism accurately |
| B07 §1d "Carry-Forward Is Implicit," all occurrences | B07 | Active-Valid | none — the current, correct model explanation |
| B04 `CarriedForward removed` note | B04 §3 | Historical, correctly labeled | none — already framed as "Round 1 listed this..." |
| All remaining "carry-forward"/"opening balance"/"CAP-06"/"Trial Balance"/"Mode 1/Mode 2"/"reset" hits (44 additional locations checked) | B01, B05, B07, B08, B09, B10, B12, B13, B14, B15, B16, B19-B23, F, G, H, TEAM_B_STATUS, CORR_Bx docs | Active-Valid or Historical-OK (already struck through / narrative past tense / Team A's own input evidence / unrelated governance-sense "carry-forward") | none — no correction needed |

**44 additional locations were individually inspected and found clean** — the full grep output
(counts and file/line locations) was reviewed line-by-line before this register was finalized;
none required correction beyond the six items listed above.

### What changed

`B02` (CAP-01, CAP-04, CAP-08, CAP-09 title), `B07` (Consumption Record row), `B18` (Test 5,
annotated), `B15` (§3g, §8a, both new).

## 4. CORR-B7-04 — Capability / Event / Invariant Dependency Sanity

Full matrix: [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §8a — covers CAP-01..09, the four
Fiscal-Calendar events, Consumption's three trigger kinds, Period/Fiscal-Year controls, and the
Known/Current viewpoint mechanism, with the required 7-column schema (Source/Target/Why/
Current-Responsibility/Evidence/Status/Disposition). All four required acceptance criteria
confirmed directly in that section:

```
zero active dependency edges to a responsibility the target no longer owns    : CONFIRMED
zero active references to removed `CarriedForward` behavior                   : CONFIRMED
zero active implication that CAP-06 owns carry-forward                        : CONFIRMED
zero active implication that FiscalYearClose posts an earnings-transfer Entry : CONFIRMED
zero active implication that ordinary Period close automatically causes Consumption : CONFIRMED
```

## 5. CORR-B7-05 — Terminology Consolidation

Current authoritative terms (Raw Cumulative Trial Balance / Current-Fiscal-Year Reporting
Balance / Balanced Presentation Trial Balance / `CumulativeAccountBalance` /
`FiscalYearActivity` / Reported Retained Earnings / Reported Equity / Period Close / Fiscal Year
Close / `FiscalYearBoundaryChanged` / `FiscalYearMembershipRestated` / Consumption /
Restatement / Migration Opening Balance) were each individually checked, per [B15](B15_DESIGN_TRACEABILITY_MATRIX.md)
§8a, against every place they are used, and found distinctly and consistently defined — no
removed term is reused as shorthand anywhere in the active pack.

**CAP-09's title, specifically addressed per the directive's explicit instruction:** the audit
required either proving "Transfer" in "Fiscal Year Close & Earnings Transfer" cannot be misread
as a posted transfer, or renaming. Proving a word can never be misread is a weaker guarantee
than removing the word — and the capability's own scope has grown, at CORR-B5-05/CORR-B6-02, to
include Fiscal Year boundary and membership governance, which "Earnings Transfer" never named
at all even under its own footnoted re-scoping. **Renamed to "CAP-09 — Fiscal Year Close &
Boundary Governance."** The old title (and its own prior name, "Period-End Carry-Forward") is
preserved in the section's own history parenthetical, not deleted.

### What changed

`B02` CAP-09 heading and Capability Dependency Summary diagram label.

## 6. CORR-B7-06 — Focused Regression / Semantic Implementer Test

See [B24_CORR_B7_ACTIVE_SEMANTIC_AND_DEPENDENCY_REGRESSION.md](B24_CORR_B7_ACTIVE_SEMANTIC_AND_DEPENDENCY_REGRESSION.md) —
9 personas, all 15 directive-specified scenarios, exact required schema. 15/15 PASS. This is
the first regression round whose method is reading-comprehension verification (does the active
text communicate the current model to an implementer reading it cold) rather than numeric/
temporal verification — every prior round's own numeric conclusions (B18-B23) are re-confirmed
unaffected by this round's pure terminology/dependency corrections.

## 7. CORR-B7-07 — Propagation

Every artifact in the directive's "at minimum expected" list was updated: B02, B07, B15, F, G,
H, TEAM_B_STATUS. Additionally updated, found stale during CORR-B7-03: B18 (Test 5 annotation).
B03, B04, B05, B06, B08, B09, B10, B11, B12, B13, B14, B16, B19-B23 were inspected (per the
directive's own "at minimum inspect" list, extended to every remaining Bxx file for
completeness) and confirmed to contain no active-stale semantics requiring correction.

**All seven Boss-level assumptions preserved unchanged** — this round's corrections are pure
active-semantic/dependency hygiene, with no bearing on rounding method, period-close/
consumption timing, chart-of-accounts structure, tamper-evidence scope, correction-shape
flexibility, the CO-02/CO-06 coupling, or the Fiscal Year boundary authorization tier. None
resolved by Team B. Team A's 20 residual unknowns remain visible, unconverted into requirements.

## 8. CORR-B7-08 — Evidence / Push Verification

See [DOMAIN_01_ACCOUNTING_CORE_AC_CORR_B7_CLOSURE_EVIDENCE.md](DOMAIN_01_ACCOUNTING_CORE_AC_CORR_B7_CLOSURE_EVIDENCE.md)
and [SESSION_ARCHIVE/SESSION_SMEPLUS-26-08-30-MIG-B-D01-CORR7-001_CLOSURE.md](SESSION_ARCHIVE/SESSION_SMEPLUS-26-08-30-MIG-B-D01-CORR7-001_CLOSURE.md).

## 9. Seven Assumptions — Status After This Round

```
1. Rounding method .................................. OPEN, unchanged
2. Period close / Consumption ....................... OPEN, unchanged this round
3. COA template/instance ............................. OPEN, unchanged
4. Broad audit tamper-evidence scope .................. OPEN, unchanged
5. Correction shape flexibility ....................... OPEN, unchanged
6. CO-02/CO-06 coupling ............................... OPEN, unchanged
7. Fiscal Year boundary change authorization tier ..... OPEN, unchanged — this round did not
   touch the change-model or its authorization tier at all, only active-text hygiene
```

**No eighth assumption is added.** This round resolved zero design questions — it corrected
stale cross-references and renamed one ambiguous title, all of which have exactly one correct
current answer traceable to already-settled prior-round decisions, not new open policy
questions.

## 10. Jira Governance Facts — Preserved, Not Invented

Per explicit instruction, `ERPPLUS-100`'s Assignee (`UNASSIGNED`) and Due Date (`TBD`/empty)
are preserved exactly as found — flagged as PMO/governance red flags in the evidence comment,
never filled in by this executor.
