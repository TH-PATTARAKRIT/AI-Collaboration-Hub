# B15 — Design Traceability & Consistency Verification

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B15 — Traceability & Consistency Verification |
| Method | Genuine audit — findings below are real, not a rubber stamp. Two consistency issues were found internally and are resolved explicitly, not silently; three further, more severe defects were subsequently found by ChatGPT's independent audit (Round 1) and recorded in §3a; two more were found by ChatGPT's Round 2 re-audit and recorded in §3b; two more were found by ChatGPT's Round 3 re-audit and recorded in §3c; three more were found by ChatGPT's Round 4 re-audit and recorded in §3d; two more were found by ChatGPT's Round 5 re-audit and recorded in §3e; two more were found by ChatGPT's Round 6 re-audit and recorded in §3f — all with equal transparency. |
| **Corrected (Round 4)** | **CORR-B4-01..08 (2026-08-30)** — new §3d added for `M-AUD-08`/`M-AUD-09`/`M-AUD-10`. See [CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md](CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md). |
| **Corrected (Round 5)** | **CORR-B5-01..08 (2026-08-30)** — new §3e added for `M-AUD-11`/`M-AUD-12`; §6 gains a genuine seventh Team B assumption (Fiscal Year boundary change authorization tier). See [CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md](CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md). |
| **Corrected (Round 6)** | **CORR-B6-01..08 (2026-08-30)** — new §3f added for `M-AUD-13`/`M-AUD-14`; §6's seventh assumption confirmed unchanged, not narrowed or widened. See [CORR_B6_FISCAL_CALENDAR_VIEWPOINT_MEMBERSHIP_CORRECTIVE_ROUND.md](CORR_B6_FISCAL_CALENDAR_VIEWPOINT_MEMBERSHIP_CORRECTIVE_ROUND.md). |

## 1. Full Chain Traces (Exemplars)

**Chain A — the domain's central design thread:**

```
BF-04 (B01 Authorized Input: "correction should be additive, never destructive")
  → MG-01/AU-01 (B01 Requirement)
  → BINV-06 + BR-07 (B05/B06 Rule/Invariant)
  → B04 §4 Consumption Gate (Lifecycle/Event design)
  → Correction Link entity, "at most one direct target link" cardinality (B07 Conceptual Model)
  → CO-04 + CO-06 (B09 Control)
  → MG-C04/MG-C05 (B10 Migration Requirement)
  → AD-04 (B12 Advancement Objective — highest priority)
  → B04 §4 mechanism + BR-06/BR-07 (Design Decision)
  → B14 vendor-risk=NONE, B16 red-team review (Acceptance Criterion)
```

**Chain B — an assumption-flagged thread, traced to show the chain still works when the
answer is "not yet decided":**

```
OQ-03 (B01 Open Question: rounding policy unresolved)
  → MP-04 (B08 Mathematical Design Principle — Team B proposes round-half-up)
  → BR-01/BR-08 dependency (B06, balance checks operate on rounded values)
  → DT-01 (B13 Design Option — explicitly marked "not approved")
  → carried to B17 residual assumptions, not silently resolved
```

**Chain C — a regulatory-grounded thread:**

```
RG-04 (B01, Revenue Department of Thailand, official source)
  → BR-12/CAP-07 (B06/B02)
  → BINV-09 is NOT implicated (category vs. document-numbering are distinct — correctly
    not cross-wired)
  → CO-12 (B09 Control — individually traceable citation requirement)
  → B13 DT-06 (per-company sequence scope)
  → B14 provenance = RG, vendor risk = NONE
```

## 2. Orphan Check

Every B01 input item (BF-xx, PR-xx, IV-xx, LC-xx, RG-xx, MG-xx, AU-xx, AO-xx, OQ-xx) was
checked against B02–B14 for at least one downstream use. **Result: no orphans.** The one
input item with the thinnest downstream development is AO-05 (document typing / ADV-05),
consistent with it also being Team A's thinnest-evidenced advancement candidate
(single-source, Part 1 only, not independently re-evidenced by Sonnet) — carried at the same
weight, not silently dropped, not artificially inflated either (B12 AD-05 explicitly says so).

## 3. Consistency Issues Found and Resolved

**Issue 1 — ID space collision: `BR-xx` used in two places.**
B01 §4 ("Business Rules") assigned IDs `BR-01`..`BR-13` as a preliminary classification of
Team A's GR-01..13. B06 ("Business Rule Baseline") independently assigned the *same* ID space
`BR-01`..`BR-15` to its own, fully operationalized rule register. The underlying rules
correspond 1:1 for items 1–13 (same rule, increasing refinement), so there is no *content*
contradiction, but the shared numbering is a real risk for a reader (or auditor) encountering
both documents. **Resolution:** B06 is designated the canonical `BR-xx` register for this
domain going forward; B01 §4 is retroactively understood as a preliminary classification pass
that B06 supersedes in detail, not a competing definition. Recorded here rather than silently
edited into B01, per this project's own "visible corrections, not silent edits" principle
(already demonstrated in [B00](B00_GOVERNANCE_AND_HANDOFF_VERIFICATION.md)).

**Issue 2 — Interaction between CO-02 (segregation of duties) and CO-06 (safe-path-not-harder).**
CO-02 lists "corrections to consumed facts" as a candidate for optional maker-checker
separation. CO-06 requires that the correction path never carry a *higher* authorization tier
than whatever unconsumed Amendment (BR-14) requires. Read independently, a tenant could
configure CO-02's optional SoD for corrections without raising Amendment's bar to match,
which would silently violate CO-06's objective — exactly the kind of gap this domain's whole
design exists to close, so it cannot be left implicit. **Resolution (new, stated here for the
first time):** CO-02's optional SoD configuration for "corrections to consumed facts," if
enabled, must apply an equal-or-stricter authorization tier to unconsumed Amendment (BR-14)
at the same time — CO-06 constrains how CO-02 may be configured, not merely a static
comparison of two independently-set values. This resolution is itself now part of this
domain's control design and should be carried into B17's evidence pack as a stated
cross-reference, not left as an implicit reader inference.

## 3a. Corrective Round — Issues Found by Independent Audit and Resolved *(added at CORR-B01/B02/B03)*

Three further defects, all more severe than the two in §3 (all three were BLOCKING, per
ChatGPT's audit severity ratings), were found not by this domain's own traceability pass or
red-team review, but by the subsequent ChatGPT Independent Design Audit
(`aa60c2d0497cefe804d37953bbfaa597c3476d79`). Recorded here with the same discipline as §3,
because a traceability document that only shows the issues it caught itself would
misrepresent how this design actually reached its current state.

**Issue 3 (`D01-B-AUD-01`) — Consumption permanence contradicted period-reopen semantics.**
B04 treated period close as a permanent Consumption trigger while also describing reopen as
restoring correctability — impossible to reconcile against BINV-07's "never retracted"
guarantee. **Resolution:** Period Lock (CAP-04/BINV-02) and Consumption (BINV-06/07)
separated into two independent, orthogonal gates on Amendment; period close removed as a
Consumption trigger (three remain, not four). Full comparison of alternatives:
[CORR_B01_B02_B03_CORRECTIVE_ROUND.md](CORR_B01_B02_B03_CORRECTIVE_ROUND.md) §1; applied to
B04 §2/§4/§5, B05 BINV-06, B08 MP-10, B13 DT-02.

**Issue 4 (`D01-B-AUD-02`) — MP-02's accounting-equation proof was mathematically incomplete.**
Per-entry balance plus correct normal-balance-side does not, by itself, imply the *simple*
equation `Assets = Liabilities + Equity` during an open period — it implies the *expanded*
equation `Assets + Expenses = Liabilities + Equity + Revenue`, with the simple form as a
special case once Revenue and Expenses are both zero (post-closing). **Resolution:** MP-02
rebuilt with a full proof of the expanded equation, Current Earnings defined (B07 §1b), and
BINV-10 strengthened to require the closing transfer that makes the simple equation hold
again after close. Full proof: [B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md) MP-02.

**Issue 5 (`D01-B-AUD-03`) — Historical as-of balances were not time-consistent across a later VOID.**
MP-09 filtered aggregation by an Entry's *current* VOIDED status, so a later void could
silently change what an earlier "balance as of D1" query reported. **Resolution:** voiding
redefined as always a dated, linked Correction Entry (a zero-net reversal, B04 §5), and
MP-09's status-based exclusion removed entirely — a void's own (later-dated) Lines now
naturally affect only aggregations dated on or after the void itself, via the same date
filter every other Entry already uses. New invariant BINV-11 states this property directly.
Comparison of alternatives: [B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-07.

**Pattern note:** all three issues share a common shape — this domain's own first design pass
introduced exactly the kind of conflation (two distinct questions collapsed into one
mechanism; a proof that quietly assumed its own conclusion; a status check standing in for a
date check) that Team A's research identified as the reference system's central weakness
(CF-06, `06_STATE_EVENT_LOGIC_ANALYSIS.md`'s "two genuinely different business questions...
conflated into one field"). None were caught by this domain's own ten-persona internal
red-team pass ([B16](B16_TEAM_B_INTERNAL_RED_TEAM_REVIEW.md)) despite that pass genuinely
finding and fixing six other real gaps — recorded honestly as a limitation of single-executor
review, not smoothed over. This is precisely why directive §0 requires an independent audit
before PMO/Boss Gate, not a second round of the same reviewer's own red-team.

## 3b. Corrective Round 2 — Issues Found by ChatGPT Re-Audit and Resolved *(added at CORR-B2-01..04)*

Two further defects, found by ChatGPT's Round 2 re-audit (`04e44b06489d8bea6c8d39410050d68cf08bce21`)
— **after** this domain's own §3a corrective round, meaning the pattern in §3a's closing
note repeated: neither was caught by [B18](B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md)'s
10-scenario regression, despite that regression genuinely finding and fixing one precision
gap of its own.

**Issue 6 (`M-AUD-04`) — Backdated corrections could still rewrite relied-upon history.**
Round 1's BINV-11 fix filtered by Effective Date alone; a Correction committed after the fact
could still claim an Effective Date inside an already-relied-upon, reopened period. Team A's
own B11 Scenario 10 ("no special rule" for backdating) was never revisited for corrections
specifically when it was written, and the Round-1 corrective round did not revisit it either.
**Resolution:** Entry split into Effective Date and Recorded At (B07 §1c); MP-09 rebuilt with
two aggregation modes, the "as originally known" mode filtered by the immutable Recorded At
(BINV-12, new); a distinguished Restatement correction-purpose (B04 §3a) for backdated
corrections into consumed periods, with its own authorization tier (CO-15). Full comparison:
[B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-09.

**Issue 7 (`M-AUD-05`) — CAP-09 overgeneralized Team A's year-end-specific carry-forward rule.**
B01 BF-09 (authorized input) explicitly says year-end; B02's original CAP-09 applied the same
rule to every ordinary Period close, and — combined with MP-09's all-time summation — created
a genuine double-counting risk (verified: the Round-1 design, if taken literally, would have
produced Feb Cash = 200 instead of 100 in [B19](B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md)
Test 1's scenario). **Resolution:** Continuous Ledger model adopted (B07 §1d) — ordinary
carry-forward is implicit (no posted fact, nothing to double-count); CAP-09 renamed and
rescoped to Fiscal Year Close only, posting exactly one Current-Earnings-transfer Entry
(MP-11). Full comparison: [B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-08.

**Pattern note, continued from §3a:** both issues are, again, instances of the same root
category Team A identified in the reference system (CF-06's field-conflation pattern) —
Issue 6 conflated "when this happened" with "when this could be known"; Issue 7 conflated
"an ordinary posting lock" with "a fiscal year's economic closing event." That this pattern
recurred even after §3a's corrective round explicitly named it is recorded honestly, not
minimized: single-executor design and single-executor regression testing have a structural
blind spot for exactly this category of error, which is the whole reason independent
re-audit — not a third round of this domain's own review — is what actually catches it.

## 3c. Corrective Round 3 — Issues Found by ChatGPT Re-Audit and Resolved *(added at CORR-B3-01..08)*

Two further defects, found by ChatGPT's Round 3 re-audit (`f6fb633fd141f45caf047bc94d75f84420e1cc6d`)
— **after** this domain's own §3a and §3b corrective rounds, meaning the pattern named at the
end of §3b's own entry repeated a third time: neither was caught by
[B19](B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md)'s 15-scenario Round-2 regression, despite
that regression genuinely finding and fixing one design over-reach of its own (its Test 11).

**Issue 8 (`M-AUD-06`) — B19 Test 11's "ordinary current-dated Entry is sufficient" conclusion
was universalized without a materiality branch.** Round 2's own regression, working through a
prior-year restatement scenario, concluded a simple current-dated recognition was always
sufficient — correctly identifying that its own *first* draft (a mandatory backdated Prior
Period Adjustment line) was over-engineered, but incorrectly generalizing the simplified
conclusion to every case, rather than only the immaterial case. IAS 8 (verified from
primary-source PDF text, paras 41/42/46) requires mandatory retrospective restatement,
specifically excluded from current-period profit or loss, for prior-period errors that are
**material** — a distinction B19 Test 11 never drew. **Resolution:** B04 §3b adds a full
Error/Estimate/Materiality classification decision tree (citing IAS 8 paras 5/34/36-38/41/46
directly); §3c adds the retrospective restatement mechanics for the material branch
specifically; B05 adds BINV-13 (material prior-period error P&L exclusion, new); B09 adds
CO-16 (materiality is a policy input, never computed, new); B19 Test 11 itself is annotated
with a visible correction note (not rewritten) pointing to
[B20](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md)'s corrected treatment.

**Issue 9 (`M-AUD-07`) — MP-11 (Round 2) directly contradicted this domain's own
"Revenue/Expense never reset by a posted action" claim, and was a genuine arithmetic bug.**
MP-11, as added at CORR-B2-03/04, defined Fiscal Year Close as posting one Entry debiting
Revenue and crediting Expense — literally a posted reset of exactly the accounts B07 §1d and
MP-02's own post-closing paragraph claimed were never reset by a posted action. Tracing the
wording further (not merely noting the contradiction) showed it was worse than inconsistent:
combined with MP-09's Effective-Date-bounded aggregation, such an Entry — dated anywhere
within the Fiscal Year it closes — would corrupt that year's own historical query. **Resolution:**
no-posted-close model adopted (compared against the superseded posted-Entry model,
[B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-10) — Fiscal Year Close becomes a purely
declarative Audit Event; B07 §1e defines Reported Retained Earnings as a derived reporting
formula, never a posted balance; B08 MP-11 rewritten to match, with the Round-2 text kept
fully visible above the correction; B02 CAP-09, B05 BINV-10 propagated to match.

**Pattern note, continued from §3a and §3b:** both issues are, again, instances of the same
root category named twice already — Issue 8 is a scope-generalization error (a conclusion
correct for one case silently applied to all cases, the same shape as Issue 7's
`M-AUD-05` scope error); Issue 9 is a direct internal contradiction between two claims this
domain's own design made about the same subject (the same shape as Issue 6's temporal
contradiction). That this pattern recurred a third time, even after being explicitly named
twice, is recorded honestly, not minimized, for the same reason given in §3b: independent
re-audit — not a fourth round of this domain's own self-review — is structurally what catches
this category of error, and the self-review document (G, §4c) records this pattern explicitly
rather than treating each round's fix as evidence the underlying blind spot has closed.

## 3d. Corrective Round 4 — Issues Found by ChatGPT Re-Audit and Resolved *(added at CORR-B4-01..08)*

Three further defects, found by ChatGPT's Round 4 re-audit (`9c0a3f2d179994a20f01db16d5713989a78c0b2a`)
— **after** this domain's own §3a, §3b, and §3c corrective rounds. Two of the three
(`M-AUD-08`, `M-AUD-09`) were defects **introduced by Round 3's own corrective fix** for
`M-AUD-07` — the no-posted-close model itself, not a pre-existing gap Round 3 merely failed to
notice.

**Issue 10 (`M-AUD-08`) — Reported Equity double-counted the designated Retained Earnings
account.** B07 §1e (Round 3) defined Reported Retained Earnings as the designated RE account's
direct balance plus accumulated closed-Fiscal-Year earnings; B08 MP-02's companion paragraph
separately described "Reported Equity" as `Equity(ledger, all-time) + Reported Retained
Earnings` — but the designated RE account is itself inside `Equity(ledger, all-time)`, so its
balance was summed twice. **Resolution:** B07 §1f (new) partitions Equity into two disjoint
sets — Other Ledger Equity (every Equity account EXCEPT the designated RE account) and
Reported Retained Earnings (which alone covers that account) — so Reported Equity's two terms
never overlap. B08 MP-02/MP-12 corrected to match; full comparison and worked multi-account
proof: [B21](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md) Test 2.

**Issue 11 (`M-AUD-09`) — Reported Retained Earnings depended on operational close timing, not
the Fiscal Year's own calendar boundary.** B07 §1e (Round 3) summed "every Fiscal Year that
closed before D" — closed meaning `FiscalYearClosed` had been declared. A real, expected delay
between a Fiscal Year's actual end and its formal close declaration (reconciliation, review)
would silently omit that year's earnings from every report for the duration of the gap.
**Resolution:** Fiscal-Year inclusion redefined as boundary-driven ("Elapsed" — End Date <=
query date, a pure calendar fact, B07 §1e) rather than declaration-driven; `FiscalYearClosed`
now governs posting-lock scope only. Three models compared (boundary-driven; an explicit
"unclosed earnings" component; mandatory atomic close), with the third rejected on independent
operational grounds, not merely because the audit cautioned against it:
[B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-11. Worked delayed-close proof:
[B21](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md) Tests 5-7.

**Issue 12 (`M-AUD-10`) — Reported Retained Earnings/Equity had no defined Mode-1 ("as
originally known") version, despite the Round-3 regression (B20 Test 8) already relying on
one.** The regression's *behavior* was correct; the *formula* it was supposedly testing never
actually defined that behavior, meaning a literal implementation of B07 §1e would let a later
Restatement silently alter an already-issued historical report — violating BINV-11's
reproducibility guarantee one level up from where BINV-11 itself is proven. **Resolution:**
B07 §1g (new) parameterizes Reported Retained Earnings and Reported Equity by reporting
viewpoint (`_Known(C,D,T)` / `_Current(C,D)`), built directly on MP-09's existing Mode 1/Mode 2
split rather than inventing new machinery; CO-14's mode-labeling requirement extended to cover
these outputs explicitly (B09). Worked reconstruction proof:
[B21](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md) Tests 8-9.

**Pattern note, continued from §3a/§3b/§3c:** this is the fourth consecutive corrective round
in which independent re-audit found what this domain's own process — including its own
regression testing — did not. Two new observations belong here, beyond simply reaffirming the
pattern named three times already. **First**, `M-AUD-08` and `M-AUD-09` were not latent defects
Round 3 merely failed to notice in pre-existing design — they were defects Round 3's OWN fix
for `M-AUD-07` introduced. A corrective round's output is new design surface with the same
defect potential as any other design surface, and this is now direct, repeated evidence of that
(the same observation G §4c makes, from the self-review angle, about this specific instance).
**Second**, `M-AUD-10` illustrates a distinct failure shape from the first three rounds' worth
of findings: not a wrong formula and not a wrong scope, but a formula whose *regression test*
(B20 Test 8) exercised a behavior the *formula itself* never actually specified. Real, worked
numeric regression testing is this project's core verification discipline — but Issue 12 shows
it is not sufficient on its own if the authoritative specification the regression is supposedly
validating was left silently under-defined; the regression can look green while the design
document it is meant to hold accountable simply never made the claim being tested. Both
observations are recorded plainly, in the same spirit as every prior round's pattern note, and
are reflected in [G §4d](DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md).

## 3e. Corrective Round 5 — Issues Found by ChatGPT Re-Audit and Resolved *(added at CORR-B5-01..08)*

Two further defects, found by ChatGPT's Round 5 re-audit (`de7492afd0af0f58185f3f36940a77f2389aa8b8`)
— **after** this domain's own §3a-§3d corrective rounds. Both are, in different ways, direct
descendants of Round 4's own corrective work: `M-AUD-11` is a defect Round 4's OWN fix (MP-12)
introduced; `M-AUD-12` is a gap Round 4's OWN new concept (the Elapsed test, B07 §1e) exposed
by relying on a fact (the Fiscal Year boundary) this design had never previously needed to
protect.

**Issue 13 (`M-AUD-11`, CRITICAL) — MP-12 Proof G claimed MP-09's mixed-horizon output was a
balanced Raw Trial Balance; it is not, once a Fiscal Year has elapsed.** Proof A/B (Round 4)
were careful to use one common horizon throughout their own derivation; Proof G then silently
reused Proof A's name and conclusion for a DIFFERENT, mixed-horizon quantity, without
re-checking whether Proof A's precondition (one common horizon) still held for it. It did not
— verified against Team B's own B21 Test 5 numbers (Company X, Jan 5 2025: mixed-horizon debit
1250 vs. credit 1000, off by exactly 250). **Resolution:** MP-09 renamed and split into
`CumulativeAccountBalance` (the true single-horizon formula) and `FiscalYearActivity`
(Revenue/Expense only, Fiscal-Year-bounded, never itself called a Trial Balance); MP-12 Proof G
rebuilt into G1 (Raw Cumulative Trial Balance, genuinely balanced)/G2 (Current-Fiscal-Year
Reporting Balance, explicitly NOT balanced)/G3 (Balanced Presentation Trial Balance, with an
explicit, permanently-not-postable derived bridge line)/G4 (Known vs. Current, applied to
G1-G3); new BINV-15 (B05) makes the non-confusion requirement an explicit invariant; CO-14
(B09) extended to require G1/G2/G3 labeling. Full comparison and worked re-verification:
[B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md) MP-12,
[B22](B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md) Tests 1-4.

**Issue 14 (`M-AUD-12`, HIGH) — Fiscal Year boundaries were used as timeless facts with no
protection against silent retroactive editing.** B07 §1e's Elapsed test (Round 4) deliberately
takes no viewpoint parameter, reasoning that a calendar boundary is a pure fact independent of
when it's queried — correct as far as it went, but Round 4 never asked whether that boundary
could itself be silently changed after Entries, Elapsed determinations, or issued reports had
already relied on it. **Resolution:** B07 §1h (new) adopts a Versioned Fiscal Calendar model
(compared against boundary-immutability-after-use and a rejected open "Option C" at
[B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-12) — pre-reliance corrections remain free and
ungated; post-reliance changes require a new, CO-15-tier-or-stricter `FiscalYearBoundaryChanged`
Audit Event (B04, new), never a silent overwrite, with the old boundary version permanently
queryable for Known-viewpoint reconstruction. New BINV-16 (B05) formalizes the invariant. The
exact authorization tier is flagged as a new, seventh Team B assumption (§6, below), not
resolved by this domain's own evidence the way CO-16's materiality decision was.

**Pattern note, continued from §3a-§3d:** this is the fifth consecutive corrective round in
which independent re-audit found what this domain's own process did not — and, notably, BOTH
of this round's findings trace directly to Round 4's own new design surface (MP-12's proof
structure; the Elapsed test's implicit calendar-timelessness assumption), continuing the
"a corrective round's own fix is new attack surface" observation §3d first made explicit for
`M-AUD-08`/`M-AUD-09`. Reflected in
[G §4e](DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md).

## 3f. Corrective Round 6 — Issues Found by ChatGPT Re-Audit and Resolved *(added at CORR-B6-01..08)*

Two further defects, found by ChatGPT's Round 6 re-audit (`b0ce666dad72909411a49690d0f642313d94dd13`)
— **both tracing directly to Round 5's own new §1h text**, making this the fourth instance of
the self-inflicted-finding sub-pattern (§3d/§3e first named it) and the first where BOTH of one
round's findings originate in the SAME single prior-round section.

**Issue 15 (`M-AUD-13`, CRITICAL) — B07 §1g's Round-4 claim that "the Elapsed test never takes a
viewpoint parameter" directly contradicted §1h's own Round-5 Known/Current calendar model,
which was never revised to match.** §1g was correct when written; §1h's Round-5 addition made it
false, and nothing in Round 5's own corrective work went back to reconcile the two. **Resolution:**
§1g corrected in place (struck through, not deleted); new §1i formalizes
`FiscalYearDefinition_Known(C,Y,T)`/`_Current(C,Y)` and `Elapsed_Known(Y,D,T)`/`_Current(Y,D)`,
proven a fixed point once T has passed by the same Recorded-At argument BINV-11/12 already
establish for Entries. Propagated into B08 MP-09 (`FiscalYearStart_Known/Current`) and MP-12
(Proofs D/G4, corrected to route every boundary lookup through the matching viewpoint). Full
record: [B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1i,
[B23](B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md) Tests 1, 6, 7.

**Issue 16 (`M-AUD-14`, CRITICAL) — §1h's Round-5 model left Current-viewpoint reporting
under-specified once a post-reliance boundary version and old Entry membership can coexist.**
§1h permitted a new boundary version to exist "unless a separate, explicit reclassification
action is taken" — leaving that action undefined and un-gated as atomic, so a new version and
stale Entry membership could coexist indefinitely with no defined Current-viewpoint reporting
behavior. **Resolution:** new B07 §1j selects and fully specifies a change model — Option A
(Prospective-Only Change After Reliance), refined with a new, dedicated, atomic
`FiscalYearMembershipRestated` mechanism (B04) that moves the boundary AND reclassifies affected
Entries' Current-viewpoint membership in one indivisible action, never two independently-timed
ones. `Membership_Known(E,T)`/`Membership_Current(E)` formalized; the proven invariant
`Membership_Current(E) = Membership_Known(E,RecordedAt(E))` (absent an explicit Restatement)
closes the "which membership is authoritative" question directly. B07's Fiscal Year identity
statement corrected to be viewpoint/version-safe (CORR-B6-05), with no-overlap/no-coverage-gap/
transition-preservation/future-validation invariants stated explicitly. Compared against a
strict, unrefined reading of Option B (Retroactive Change with Atomic Restatement applied to the
EXISTING `FiscalYearBoundaryChanged` mechanism itself) at
[B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-13 (new) — rejected because it would overload
one mechanism with two conceptually distinct purposes rather than cleanly separating them, as
this design already does for Entries (Correction vs. Restatement). New BINV-17 (B05) formalizes
the coherence requirement. Full record: [B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1j,
[B23](B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md) Tests 2-5, 8-15.

**Pattern note, continued from §3a-§3e:** this is the SIXTH consecutive corrective round in
which independent re-audit found what this domain's own process did not, and the fourth
consecutive instance of the self-inflicted-finding sub-pattern (Round 3 introduced `M-AUD-07`'s
predecessor gap; Round 4's own MP-12 introduced `M-AUD-11`; Round 5's own new §1h introduced
BOTH of this round's findings at once). Unlike §3d/§3e's cases, where a round's fix introduced a
single new formula-level defect, this round's findings are the first to arise from an outright
textual CONTRADICTION between two sections of this domain's own design (§1g vs. §1h) rather than
a defect internal to one formula — a qualitatively different failure mode this domain's own
process had not previously exhibited. Reflected in
[G §4f](DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md).

## 4. Contradictory Rules Check

Beyond Issue 2 (resolved above), no other rule pair was found to assert incompatible
requirements. BR-07 (consumed: no mutation) and BR-14 (unconsumed: mutation permitted, logged)
are complementary partitions of the same state space (consumed vs. not), not a contradiction.

## 5. Circular Definition Check

Traced (re-verified Round 2, this statement corrected — the original B15 pass predated
CORR-B01 and described a dependency that no longer exists): Consumption (B04 §4) and Period
Lock (CAP-04) are, since CORR-B01, explicitly independent — neither depends on the other,
which is the whole point of separating them. Restatement (B04 §3a, new Round 2) depends on
BOTH (it is defined by a Consumption Record existing AND an Effective Date falling in the
period it covers), but neither Consumption nor Period Lock depends on Restatement — no cycle.
SUPERSEDED status depends on an incoming Correction Link, which can only attach to an
already-COMMITTED target at link-creation time — links only ever point from newer to older
(by Recorded At, now that the two temporal axes are distinct, B07 §1c), so no cycle is
reachable through chaining (B04 §6, B07 §3). **No circular definitions found.**

## 6. Unresolved Critical Assumptions Register (consolidated)

**Round 3 note (CORR-B3-07):** none of the six Team B design assumptions below is narrowed,
widened, or resolved by this round's corrections. Round 3's subject matter (IAS 8 error/
estimate/materiality classification, retrospective restatement mechanics, and the Fiscal
Year Close posted-Entry-vs-derived-formula resolution) does not bear on rounding method,
period-close/reopen/consumption timing, chart-of-accounts structure, tamper-evidence scope,
correction-shape flexibility, or the CO-02/CO-06 coupling — the six rows are reproduced below
unchanged, per this directive's explicit instruction not to resolve an assumption merely to
make the pack look more complete. Materiality itself (the one new judgment-input concept this
round introduces) is **not** added as a seventh assumption, because it is not an open design
question this domain defers to Boss — CO-16 (B09, new) already closes it as a settled design
decision: materiality is explicitly and permanently out of this domain's computation scope,
supplied externally, which is a resolved design choice, not an unresolved one.

**Round 4 note (CORR-B4-07):** likewise, none of the six assumptions is narrowed, widened, or
resolved by this round's corrections. Round 4's subject matter (Reported Equity's non-
overlapping decomposition, Fiscal-Year-boundary-driven reporting inclusion, and Mode-1/Mode-2
viewpoint parameterization) is pure reporting-formula mathematics — it does not touch rounding
method, period-close/reopen/consumption timing, chart-of-accounts structure, tamper-evidence
scope, correction-shape flexibility, or the CO-02/CO-06 coupling either. The designated
Retained Earnings account (B07 §1f, B10 MG-C15) is a required migration-configuration fact,
not an open judgment call in the sense the six assumptions are — it has exactly one correct
answer per Company (which account the source system actually used), not a range of
defensible choices awaiting Boss's preference.

**Round 5 note (CORR-B5-07):** assumptions #1-6 are unchanged, for the same reason as Round 3
and Round 4 — this round's findings (Trial Balance output labeling, Fiscal Calendar historical
safety) are pure internal-consistency/mathematics corrections with no bearing on their subject
matter. **Unlike Round 3 and Round 4, this round adds a genuine seventh assumption** (below) —
the exact authorization tier for a post-reliance Fiscal Year boundary change (B07 §1h, BINV-16)
is a real open policy question this domain's own evidence does not settle, unlike materiality
(CO-16, closed by IAS 8's own refusal to state a threshold) or the designated Retained Earnings
account (MG-C15, closed because it has exactly one factually correct answer per Company). This
domain's working default (reuse CO-15's existing Restatement tier) is stated as a default, not
asserted as the settled answer — flagged explicitly, per the directive's instruction, rather
than hidden inside B07 §1h's prose.

**Round 6 note (CORR-B6-07):** assumptions #1-6 are unchanged, for the same reason as every
prior round — this round's findings (Fiscal Calendar viewpoint coherence and post-reliance
membership semantics) are pure internal-consistency corrections with no bearing on their subject
matter. **The seventh assumption (authorization tier) is likewise unchanged in wording** — this
round selects WHICH mechanism (`FiscalYearBoundaryChanged` vs. the new
`FiscalYearMembershipRestated`) applies WHEN, and both continue to reuse CO-15's tier as a
working default; it does not narrow, widen, or settle WHAT that tier should be. No eighth
assumption is added: choosing Option A over Option B for the change model (DT-13) is a design
decision this domain makes and justifies, the same category as DT-08 through DT-12's own
resolutions, not an open policy question deferred to Boss.

| Assumption | First flagged | Disposition (per B01 §7 categories) |
|---|---|---|
| Rounding method = round-half-up | B08 MP-04, B13 DT-01 | **TEAM B DESIGN ASSUMPTION — REQUIRES GATE** |
| **REVISED at CORR-B01, FURTHER NARROWED at CORR-B2-01/02 (was: "period close as automatic, blanket consumption trigger" — that framing is withdrawn, not carried forward, per ChatGPT audit `D01-B-AUD-01`).** Now: Period Lock and Consumption are two independent, orthogonal gates on Amendment (three consumption triggers: filed, reconciled, referenced — period close is not one). Round 2 added the Restatement mechanism (B04 §3a, CO-15) specifically for backdated corrections into consumed periods, which — combined with MP-09 Mode 1's structural safety (BINV-11/12) — makes the residual open question from Round 1 (should reopen carry a time-window restriction?) lower-stakes than it was, though still genuinely undesigned: even without a time limit on ordinary reopen, a Restatement into a truly consumed period now requires CO-15's stricter tier and cannot corrupt Mode-1 history regardless of timing. | B04 §3a/§4 (corrected), B08 MP-09 (corrected), B09 CO-15, B13 DT-02/DT-09 | **TEAM B DESIGN ASSUMPTION — REQUIRES GATE**, narrowed in scope twice now |
| Chart of accounts template/instance structure (Option B) | B07 §2, B13 DT-03 | **TEAM B DESIGN ASSUMPTION — REQUIRES GATE** (also **CARRIED FORWARD** from Team A's GAP-D01-05, itself still open) |
| Audit trail tamper-evidence extended beyond evidenced legal scope | B09 CO-07, B13 DT-04 | **TEAM B DESIGN ASSUMPTION — REQUIRES GATE** |
| Correction shape left flexible (both reversal-repost and delta permitted); Void (B04 §5, corrected) is now understood as the zero-net instance of this same flexibility, not a separate question | B08 MP-08, B13 DT-05, B13 DT-07 (new) | **TEAM B DESIGN ASSUMPTION — REQUIRES GATE** |
| CO-02/CO-06 configuration coupling (Issue 2 above) | B15 §3 (new) | **TEAM B DESIGN ASSUMPTION — REQUIRES GATE** |
| **NEW at CORR-B5-05.** Fiscal Year boundary change authorization tier: a post-reliance change to a Fiscal Year's Start/End boundary (B07 §1h) requires an authorized `FiscalYearBoundaryChanged` action — this domain's working default reuses Restatement's tier (CO-15), on the reasoning that re-partitioning which Fiscal Year a transaction belongs to carries comparable blast radius to restating a period's current view, but no independent evidence (Team A or accounting-standard) settles whether that specific tier is correct, too strict, or too lax for this specific action. | B07 §1h (new), B05 BINV-16 (new), B09 CO-15 (extended), B13 DT-12 (new) | **TEAM B DESIGN ASSUMPTION — REQUIRES GATE**, new this round |
| Whether Thai law extends tamper-evidence/gapless-numbering beyond e-Tax/tax-invoice scope | B01 §11 OQ-01 | **CARRIED FORWARD** (unchanged from Team A — this domain's design does not depend on the answer either way, per CO-07's explicit separation) |
| IAS 21 remeasurement — whether reference system does this at all | B01 §11 OQ-02 | **OUT OF DOMAIN for this question specifically** — this domain designs CAP-06 to satisfy the standard regardless of the answer (AD-08), so the carried-forward unknown does not block design, only migration-time comparison |
| Full 20-item Team A residual unknown register | `11_RESIDUAL_UNKNOWN_REGISTER.md` | **CARRIED FORWARD**, incorporated by reference (B01 §11) |

## 7. Regulatory Overreach Check

Every regulatory citation in this design (RG-01..05, cited throughout B02–B13) was checked
against its B01 scope statement. No design document was found asserting general-ledger-wide
tamper evidence or universal gapless numbering as a *legal* requirement — where broader
coverage is designed (CO-07), it is consistently and explicitly labeled as Team B's own
initiative, not a regulatory claim. **No overreach found.**

## 8. Vendor Leakage Cross-Check

Full vendor-derivation review was performed in [B14](B14_CLEAN_ROOM_PROVENANCE_MATRIX.md).
Cross-checked again here from the traceability angle (does any design decision's *chain*
bottom out in a vendor artifact rather than an AS/RG/IP/XP/TF/MR/IR category): **no**, every
chain traced in §1 and spot-checked across B02–B13 bottoms out in one of the seven approved
categories.

## 9. Acceptance Check

```
No orphan critical design decision       : CONFIRMED (§2)
Contradictory rules                       : 1 found internally (Issue 2), RESOLVED explicitly
                                             (§3); 3 defects found by Round-1 independent audit,
                                             RESOLVED (§3a); 2 more found by Round-2 re-audit,
                                             RESOLVED (§3b); 2 more found by Round-3 re-audit,
                                             RESOLVED (§3c); 3 more found by Round-4 re-audit,
                                             RESOLVED (§3d, two of which were introduced by
                                             Round 3's own fix); 2 more found by Round-5
                                             re-audit, RESOLVED (§3e, both of which trace
                                             directly to Round 4's own new design surface —
                                             see §3e pattern note); 2 more found by Round-6
                                             re-audit, RESOLVED (§3f, both tracing directly to
                                             Round 5's own new §1h text — the fourth consecutive
                                             self-inflicted-finding instance, and the first
                                             arising from a textual contradiction rather than a
                                             single formula's own defect); 1 stale statement
                                             found during Round-2 re-verification and corrected
                                             (§5)
Circular definitions                      : NONE, re-verified Round 2 (§5); re-checked Round 3,
                                             Round 4, Round 5, and Round 6 — the new B07
                                             §1f/§1g/§1h/§1i/§1j decompositions and B08
                                             MP-09/MP-12 (corrected) introduce no new dependency
                                             that could cycle back on Consumption, Period Lock,
                                             Restatement, or the Elapsed test —
                                             `FiscalYearMembershipRestated` depends on
                                             `FiscalYearBoundaryChanged` having NOT applied (its
                                             scope is mutually exclusive, not layered), so no
                                             cycle is introduced between the two new-this-round
                                             mechanisms either
Unresolved critical assumptions           : 7 Team B assumptions (#2 revised/narrowed twice,
                                             Round 1 and Round 2, not withdrawn; #1, #3-6
                                             unchanged by Round 3, Round 4, and Round 6; #7 NEW
                                             at Round 5, Fiscal Year boundary change
                                             authorization tier, confirmed unchanged at Round 6
                                             — see §6 notes) + 3 carried-forward Team A items,
                                             ALL VISIBLE (§6), none hidden
Regulatory overreach                      : NONE (§7)
Vendor leakage                             : NONE (§8, cross-checked against B14; re-confirmed
                                             unaffected by Round 2's temporal/fiscal model, by
                                             Round 3's IAS 8 classification and no-posted-close
                                             model, by Round 4's reporting-equity mathematics,
                                             by Round 5's Trial Balance/Fiscal Calendar
                                             corrections, and by Round 6's viewpoint/membership
                                             corrections — all six are grounded in accounting
                                             standards/mathematics and this domain's own prior
                                             vocabulary (Known/Current, Effective/Recorded,
                                             CO-15's tier), not vendor structure)
```

**B15 = COMPLETE.** *(Corrected at CORR-B01/B02/B03/CORR-B2-01..04/CORR-B3-01..08/CORR-B4-01..08/
CORR-B5-01..08/CORR-B6-01..08 — §3a, §3b, §3c, §3d, §3e, and §3f added, §5 corrected (a stale
pre-Round-1 statement found during Round 2 re-verification), §6 assumption #2 revised in place
twice (Round 1, Round 2) and explicitly confirmed unchanged at Round 3, Round 4, and Round 6,
with every prior wording kept visible, not deleted, per instruction. §6 gains a genuine seventh
assumption at Round 5 — the first round to add one since the original six were established —
confirmed unchanged in wording and scope-of-question at Round 6. §1, §2, §4, §7, §8 re-verified
as still accurate after Round 6's corrections: no new orphans, no new overreach, no new vendor
leakage, no new circularity.)*
