# CORR-B6 — Targeted Corrective Round 6: Fiscal Calendar Viewpoint, Membership Coherence & Retroactive-Change Semantics

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-30-MIG-B-D01-CORR6-001 |
| Domain | DOMAIN_01 — Accounting Core |
| Source of truth | ChatGPT Independent Team B Design Re-Audit Round 6, commit `b0ce666dad72909411a49690d0f642313d94dd13`, verified against the live repository before any correction was made |
| Scope | Targeted correction of exactly two findings (`M-AUD-13`, `M-AUD-14`). B0–B22 not restarted. No code. No DOMAIN_02. No PMO. No self-approval. Jira assignee/due date preserved as governance red flags, not invented. |

## 0. CORR-B6 Change Log (required schema)

| finding_id | old_statement_or_rule | corrected_statement_or_rule | affected_artifacts | reason | verification_status |
|---|---|---|---|---|---|
| M-AUD-13 | B07 §1g (Round 4): "The Elapsed test itself (§1e) never takes a viewpoint parameter... Fiscal Year boundaries are not themselves posted facts subject to Recorded-At framing, so there is nothing for a Mode-1/Mode-2 split to apply to at that step." B07 §1h (Round 5, written the very next round): defines a Versioned Fiscal Calendar model WITH explicit Known/Current views for the boundary itself — directly contradicting §1g, never revised to match. | §1g corrected in place (struck through, not deleted). New §1i formalizes `FiscalYearDefinition_Known(C,Y,T)`/`FiscalYearDefinition_Current(C,Y)` and `Elapsed_Known(Y,D,T)`/`Elapsed_Current(Y,D)`, proven a fixed point once T has passed via the same Recorded-At argument BINV-11/12 already establish for Entries — the calendar boundary DOES take a viewpoint parameter, exactly since §1h's Round-5 correction. | B07 §1g (corrected)/§1i (new), B08 MP-09 (`FiscalYearStart_Known/Current`)/MP-12 (Proofs D, G4, corrected), B09 CO-14 (extended), B15 §3f | §1g's claim was true when written — at Round 4, a Fiscal Year boundary genuinely was a bare, unversioned fact. §1h made the boundary itself a versioned fact one round later, but nothing revised §1g's now-false claim, leaving a literal implementer with no instruction to use the boundary's Known view inside a `_Known(...,T)` formula — exactly the forbidden "historical facts @ T + current calendar @ now" hybrid | VERIFIED — B23 Tests 1, 6, 7 (Known-view fixed-point re-verified after a later calendar change; Elapsed_Known vs. Elapsed_Current shown to genuinely diverge for the same D) |
| M-AUD-14 | B07 §1h (Round 5): "Changing a boundary does not, by itself, retroactively move any existing COMMITTED Entry's Fiscal-Year membership... unless a separate, explicit reclassification action is taken" — that action left undefined, ungated as atomic, and untimed relative to the boundary change itself. B22 Test 12 exercised exactly this gap: "FY2024 Version 2 ... created ... existing COMMITTED Entries ... do NOT move" — a hybrid state with no defined Current-viewpoint reporting behavior. | `FiscalYearBoundaryChanged` (B04) is now constitutionally scoped to never reach backward over reliance — its Version Effective Date must fall no earlier than the point reliance began. New `FiscalYearMembershipRestated` event (B04, B07 §1j) atomically changes the Current-viewpoint boundary AND reclassifies every affected Entry's Current-viewpoint membership in one indivisible action. `Membership_Known(E,T)`/`Membership_Current(E)` formalized, with the proven invariant `Membership_Current(E) = Membership_Known(E,RecordedAt(E))` absent an explicit Restatement. B07's Fiscal Year identity statement corrected to be viewpoint/version-safe, with no-overlap/no-coverage-gap/transition-preservation/future-validation invariants stated explicitly (CORR-B6-05). | B02 CAP-09 (extended), B04 (`FiscalYearBoundaryChanged` scope-corrected, `FiscalYearMembershipRestated` new), B05 BINV-17 (new), B07 §1h (corrected)/§1j (new), B09 CO-15 (extended), B11 scenario 21 (corrected)/22 (new), B13 DT-13 (new), B15 §3f/§6 | Leaving the reclassification action undefined and independently-timed let a new boundary version and stale Entry membership coexist indefinitely, with no rule for what Current-viewpoint `FiscalYearActivity`, Elapsed earnings, Reported Retained Earnings, or comparative reporting should do in the meantime — a genuine internal incoherence, not a labeling nuance | VERIFIED — B23 Tests 2-5, 8-15 (rejection of the ordinary mechanism reaching into reliance; the exact Round-5 Test-12 scenario re-worked with concrete numbers; membership before/after; Current-viewpoint reporting after the atomic reclassification; no-overlap/no-gap rejection; multi-company isolation) |

## 1. CORR-B6-01 — Make Fiscal-Year Definition / Elapsed Selection Viewpoint-Aware

### The problem, precisely

`M-AUD-13` found a direct textual contradiction this domain's own process had not caught: B07
§1g (Round 4) states the Elapsed test "never takes a viewpoint parameter," reasoning that a
calendar boundary is a bare, timeless fact. B07 §1h (Round 5) then defines exactly a Known/
Current split FOR that boundary — directly contradicting §1g, which was never revised. Read
literally, an implementation following §1g's prose would use today's calendar for the boundary
lookup even inside a `_Known(...,T)` historical reconstruction, while correctly restricting Line
content to Recorded At <= T — exactly the forbidden hybrid this round's own directive names
verbatim: "historical financial facts @ T + current calendar version @ now."

### The fix

§1g corrected in place — the false claim struck through, not deleted, with a correction
explaining exactly when and why it became false. New §1i defines
`FiscalYearDefinition_Known(C,Y,T)` / `FiscalYearDefinition_Current(C,Y)` and
`Elapsed_Known(Y,D,T)` / `Elapsed_Current(Y,D)`, built on the SAME Recorded-At-filtering
mechanism BINV-11/12 already prove unconditional for Entries — not a new guarantee, the existing
one applied one level up. Every place this design references "which Fiscal Years have elapsed"
or "the Fiscal Year containing D" inside a `_Known(...,T)` formula now explicitly routes through
the matching viewpoint.

### Mandatory proof (worked numerically, per directive)

[B23](B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md) Test 1 re-runs a
Known-viewpoint report after a later calendar change and confirms byte-for-byte identical
membership/Elapsed/Reported RE/Reported Equity; Test 6 exhibits a query date (Dec 15, 2024)
where `Elapsed_Known` and `Elapsed_Current` genuinely diverge (FALSE vs. TRUE), proving the
parameter is real, not vacuous; Test 7 re-confirms the fixed-point guarantee survives both a
later ordinary Restatement and a later calendar reclassification.

### What changed

`B07` §1g (corrected)/§1i (new) · `B08` MP-09 (`FiscalYearStart_Known/Current`)/MP-12 (Proofs D,
G4, corrected) · `B09` CO-14 (extended) · `B15` §3f.

## 2. CORR-B6-02 — Choose and Prove One Coherent Post-Reliance Calendar-Change Model

### The problem, precisely

`M-AUD-14` found B07 §1h's Round-5 model under-specified for Current-viewpoint reporting: it
permits a post-reliance boundary version to exist while affected Entries' membership stays
frozen under the old version, "unless a separate, explicit reclassification action is taken" —
an action left completely undefined, un-gated as atomic, and untimed relative to the boundary
change. B22 Test 12 exercised exactly this gap without resolving it. In substance, Round 5's own
design was already an incompletely-specified Option B (Retroactive Change with Atomic
Restatement) — "atomic" in name only, since nothing enforced the two actions (boundary change,
reclassification) happening together.

### The fix

**Option A (Prospective-Only Change After Reliance), refined, adopted.** `FiscalYearBoundaryChanged`
is scoped to never reach backward over reliance, full stop — no exceptions, no "authorized"
carve-out. A new, dedicated, atomic mechanism — `FiscalYearMembershipRestated` (B04, new) —
handles the genuinely rare case of correcting an already-relied-upon Fiscal Year's own effective
boundary: it changes the Current-viewpoint boundary AND reclassifies every affected Entry's
Current-viewpoint membership in the SAME action, indivisibly. This is not a third, invented
model — it is the completion of Option A's own referenced-but-unspecified "separate formal
reclassification path," given full mechanics for the first time.

### Alternatives compared (per directive, not accepting the suggested direction blindly)

Compared at [B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-13 (new). **Option A — Prospective-
Only Change After Reliance (adopted, refined):** correct by construction — no reachable hybrid
state, since the lightweight mechanism is constitutionally barred from reliance and the
heavyweight mechanism is atomic by definition; mirrors this design's existing Correction-vs-
Restatement separation for Entries (CO-06/CO-15), applied one level up. **Option B — Retroactive
Change with Atomic Restatement/Reclassification, read strictly (rejected as the general
mechanism):** correct only if the atomicity requirement is followed without exception — which is
exactly what Round 5's own incomplete specification failed to enforce, producing `M-AUD-14` in
the first place; overloads one mechanism with two conceptually distinct purposes (lightweight
forward-looking policy vs. heavyweight historical correction). **Option C — a different model
(rejected):** no alternative was found that resolves the coherence requirement with less
machinery than a refined Option A already reuses from this design's own established patterns.

**The seventh Team B assumption (authorization tier) is unchanged, not resolved, by this
selection** — this round decides WHICH mechanism applies WHEN (a design decision this domain
makes and justifies, DT-13), not WHAT authorization tier governs either mechanism (still a
genuine open Boss-level policy question, [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6).

### Mandatory proof (worked numerically, per directive)

[B23](B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md) Test 3 proves the
mechanism-level split (an attempt via the ordinary mechanism is refused; the same reclassification
via the new atomic mechanism succeeds, fully evidenced); Tests 4-5 re-work the exact Round-5
Test-12 scenario with the Dec 15, 2024 illustrative Entry, showing its membership and the
resulting Reported RE/Equity figures under both Known (1250, 1190 unaffected) and Current (1190,
after reclassification) viewpoints, with no hybrid ambiguity at any point.

### What changed

`B02` CAP-09 (extended) · `B04` `FiscalYearBoundaryChanged` (scope corrected)/`FiscalYearMembershipRestated`
(new) · `B07` §1h (corrected)/§1j (new) · `B09` CO-15 (extended) · `B11` scenario 21
(corrected)/22 (new) · `B13` DT-13 (new) · `B15` §3f/§6.

## 3. CORR-B6-03 — Reconcile Entry Fiscal-Year Membership with Calendar Versions

### The problem, precisely

Round 5's design left four statements unreconciled: "exactly one Fiscal Year contains any date";
"boundary versions can change"; "an Entry's membership is fixed by the boundary version
authoritative when Recorded"; "Current view uses the latest authoritative version." Together
these permit a state where an Entry's own membership answer depends on which of these four
statements a reader applies, with no single formal definition tying them together.

### The fix

New B07 §1j formalizes `Membership_Known(E,T)` (the Fiscal Year containing E's Effective Date
under `FiscalYearDefinition_Known(C,Y,T)`) and `Membership_Current(E)` (the same, under
`FiscalYearDefinition_Current(C,Y)`, unless explicitly reclassified by a
`FiscalYearMembershipRestated` event). **Proved, not merely asserted:** absent such an event,
`Membership_Current(E) = Membership_Known(E, RecordedAt(E))`, permanently — a direct consequence
of Option A's constraint that `FiscalYearBoundaryChanged` can never move a boundary backward
over a date that already has reliance. An Entry's membership therefore never silently drifts: it
is either exactly what it was at Record-time, or it was explicitly, atomically, auditably
reclassified. There is no third state.

### Mandatory proof (worked numerically, per directive)

[B23](B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md) Test 5 shows the Dec
15, 2024 Entry's authoritative membership before (FY2024, Known) and after (FY2025, Current)
the reclassification, both independently reconstructable and labeled; Test 9 confirms Revenue/
Expense membership resolves to exactly one Fiscal Year's activity, never zero, never two.

### What changed

`B05` BINV-17 (new) · `B07` §1j (new) · `B15` §3f.

## 4. CORR-B6-04 — Propagate Coherent Viewpoint Semantics Through Every Reporting Formula

### The problem, precisely

Formalizing the boundary's own viewpoint (CORR-B6-01) is only useful if every downstream formula
that consults a Fiscal-Year boundary is corrected to route through it. Left unpropagated, MP-09's
`FiscalYearActivity` and MP-12's Proofs D/G4 would continue silently consulting today's calendar
inside a Known-viewpoint computation, reproducing `M-AUD-13`'s exact defect one layer down.

### The fix

MP-09's `FiscalYearActivity_Known/Current` corrected to use `FiscalYearStart_Known(C,D,T)` /
`FiscalYearStart_Current(C,D)` (B07 §1i) in place of the prior bare, unparameterized
`FiscalYearStart(C,D)`. MP-12 Proof D corrected to state explicitly that "elapsed"/"FY_now" in
its Known-viewpoint form use `Elapsed_Known`/`FiscalYearDefinition_Known`, never
`Elapsed_Current`/`FiscalYearDefinition_Current`, even though the rest of the proof is "evaluated
at a fixed recording-time cutoff." Proof G4 corrected identically for G2/G3's own elapsed/FY_now
split. `ReportedRetainedEarnings_Known/Current` and `ReportedEquity_Known/Current` (B07 §1g)
inherit the fix transitively, since they are built directly on `FiscalYearActivity`/the Elapsed
test. No hybrid ("historical facts @ T + current calendar @ now") formula remains anywhere in
this design pack.

### Mandatory proof (worked numerically, per directive)

[B23](B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md) Tests 8, 10, 11
verify Reported RE/Equity, the Raw Cumulative Trial Balance (unaffected, ledger-fact-driven
only), and the Balanced Presentation Trial Balance's derived bridge line all cohere under one
single Current viewpoint after a legitimate reclassification, with the bridge line matching
Reported RE's own elapsed-CE term exactly.

### What changed

`B08` MP-09 (`FiscalYearActivity_Known/Current` corrected)/MP-12 (Proofs D, G4, corrected).

## 5. CORR-B6-05 — Correct the Fiscal-Year Cardinality/Identity Statement

### The problem, precisely

B07 §1's Fiscal Year identity principle read "exactly one Fiscal Year contains any given date
for a Company" — true when a Fiscal Year's boundary was a bare, unversioned fact, incomplete
once versions and viewpoints exist, since a date could, in principle, appear to fall under two
different Fiscal Years depending on which calendar version a reader silently assumes.

### The fix

Replaced with: "For one Company and one authoritative calendar viewpoint/version (a fixed Known
cutoff T, or the Current viewpoint), exactly one Fiscal Year governs any eligible date" (B07
§1j). Supporting invariants stated explicitly and enforced by validation-before-activation: no
overlap within one viewpoint's version-set; no coverage gap (derived from MP-09's own need for
every Line to resolve to exactly one Fiscal Year's activity, not an invented regulatory
mandate); transition preservation (checked against the FULL resulting boundary set, not the one
version in isolation); future-dated validation (a not-yet-relied-upon change is checked before
acceptance too, never exempted). No implementation storage invented — the statement covers only
the conceptual entities and the validation they must pass, per B07 §2's standing exclusion.

### Mandatory proof (worked numerically, per directive)

[B23](B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md) Test 13 (overlapping
proposed versions, rejected pre-activation), Test 14 (an uncovered gap, rejected pre-activation),
Test 12 (a clean, validated future-Fiscal-Year transition with zero reliance).

### What changed

`B07` §1 (Fiscal Year row, corrected)/§1j (new, the invariant's home) · `B05` BINV-17 (new,
covers the coherence half of this requirement) · `B11` scenario 22 (new).

## 6. CORR-B6-06 — Targeted Regression

See [B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md](B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md) —
15/15 mandatory scenarios pass, using the same nine personas as Round 5 and continuing (not
restarting) Company X's running numeric scenario from B20/B21/B22, with the Dec 15, 2024
illustrative Entry named individually for the first time this round and a new, atomic
`FiscalYearMembershipRestated` worked example. This round's own regression construction did not
surface a further defect beyond the two the audit itself named — recorded honestly, per
[G §4f](DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md), as a fact about this round's process,
not a claim that the underlying difficulty in this domain's Fiscal-Calendar/reporting core has
fully resolved, especially given this is now the fourth consecutive self-inflicted-finding round.

## 7. CORR-B6-07 — Propagation Check

Every artifact in the directive's "at minimum inspect/update" list was inspected: B02, B04, B05,
B07, B08, B09, B10, B11, B13, B15, B22 (existing, annotated not rewritten), B23 (new), F, G, H,
TEAM_B_STATUS.md. B10's MG-C16 (migration-time calendar setup is always pre-reliance) was
checked for CORR-B6-01/02/03 dependencies and confirmed unaffected — pre-reliance setup remains
outside both `FiscalYearBoundaryChanged`'s and `FiscalYearMembershipRestated`'s scope either way.
B01, B03, B06, B12, B14, B16, B18, B19, B20, B21 were checked and confirmed either unaffected or
already addressed in a prior round's annotation.

## 8. CORR-B6-08 — Evidence / Push Verification

See [DOMAIN_01_ACCOUNTING_CORE_Z_CORR_B6_CLOSURE_EVIDENCE.md](DOMAIN_01_ACCOUNTING_CORE_Z_CORR_B6_CLOSURE_EVIDENCE.md)
and [SESSION_ARCHIVE/SESSION_SMEPLUS-26-08-30-MIG-B-D01-CORR6-001_CLOSURE.md](SESSION_ARCHIVE/SESSION_SMEPLUS-26-08-30-MIG-B-D01-CORR6-001_CLOSURE.md).

## 9. Seven Assumptions — Status After This Round

```
1. Rounding method .................................. OPEN, unchanged
2. Period close / Consumption ....................... OPEN, unchanged this round
3. COA template/instance ............................. OPEN, unchanged
4. Broad audit tamper-evidence scope .................. OPEN, unchanged
5. Correction shape flexibility ....................... OPEN, unchanged
6. CO-02/CO-06 coupling ............................... OPEN, unchanged
7. Fiscal Year boundary change authorization tier ..... OPEN, unchanged in wording — this round
   selects WHICH mechanism (FiscalYearBoundaryChanged vs. FiscalYearMembershipRestated) applies
   WHEN, not WHAT tier governs either one
```

**No eighth assumption is added.** Choosing Option A (refined) over Option B for the change
model (DT-13) is a design decision this domain makes and justifies — the same category as DT-08
through DT-12's own resolutions — not an open policy question deferred to Boss.

## 10. Jira Governance Facts — Preserved, Not Invented

Per explicit instruction, `ERPPLUS-100`'s Assignee (`UNASSIGNED`) and Due Date (`TBD`/empty) are
preserved exactly as found — flagged as PMO/governance red flags in the evidence comment, never
filled in by this executor.
