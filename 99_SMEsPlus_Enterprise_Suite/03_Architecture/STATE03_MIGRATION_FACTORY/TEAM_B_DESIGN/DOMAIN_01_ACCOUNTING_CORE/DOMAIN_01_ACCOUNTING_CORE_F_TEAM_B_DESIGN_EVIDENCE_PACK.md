# DOMAIN_01 ACCOUNTING CORE — TEAM B DESIGN EVIDENCE PACK

| Field | Value |
|---|---|
| Project | SMEsPlus ENTERPRISE SUITE |
| STATE | STATE03 — Architecture |
| Workstream | SMEsPlus Migration Factory |
| Board | Board06 — Data & Canonical Model |
| Domain | DOMAIN_01 — Accounting Core |
| Team | Team B — Independent Clean-Room Design |
| Directive | SMEPLUS-26-08-29-MIG-B-D01-E2E-001, corrective rounds SMEPLUS-26-08-29-MIG-B-D01-CORR-001, SMEPLUS-26-08-29-MIG-B-D01-CORR2-001, SMEPLUS-26-08-29-MIG-B-D01-CORR3-001, SMEPLUS-26-08-30-MIG-B-D01-CORR4-001, SMEPLUS-26-08-30-MIG-B-D01-CORR5-001, SMEPLUS-26-08-30-MIG-B-D01-CORR6-001, and SMEPLUS-26-08-30-MIG-B-D01-CORR7-001 |
| Date | 2026-08-30 |
| Executor | Claude Sonnet 5 |
| **Corrective round 1 applied** | **CORR-B01/B02/B03 (2026-08-29)** — ChatGPT Independent Design Audit (`aa60c2d0497cefe804d37953bbfaa597c3476d79`) found three BLOCKING defects, all corrected: a Consumption/Period-reopen contradiction, an incomplete accounting-equation proof, and time-inconsistent historical as-of balances after VOID. Full record: [CORR_B01_B02_B03_CORRECTIVE_ROUND.md](CORR_B01_B02_B03_CORRECTIVE_ROUND.md) and [B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md](B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md). |
| **Corrective round 2 applied** | **CORR-B2-01..05 (2026-08-29)** — ChatGPT's Round 2 re-audit (`04e44b06489d8bea6c8d39410050d68cf08bce21`) found two further BLOCKING defects: a backdated Correction could still rewrite relied-upon history (`M-AUD-04`), and CAP-09 overgeneralized Team A's year-end-specific carry-forward rule to every ordinary Period close, risking double-counted balances (`M-AUD-05`). Fixed with a two-temporal-axis model (Effective Date / Recorded At) and a Continuous Ledger with Fiscal Year Close as a distinct event from ordinary Period Lock. Full record: [CORR_B2_CORRECTIVE_ROUND.md](CORR_B2_CORRECTIVE_ROUND.md) and [B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md](B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md) (which itself found and corrected one over-engineered requirement in its own first draft). |
| **Corrective round 3 applied** | **CORR-B3-01..08 (2026-08-29)** — ChatGPT's Round 3 re-audit (`f6fb633fd141f45caf047bc94d75f84420e1cc6d`) found two further findings: Round 2's own Fiscal Year Close fix (MP-11) directly contradicted this design's "Revenue/Expense never reset by a posted action" claim and was a genuine arithmetic bug (`M-AUD-07`), and the Round-2 regression's own conclusion about prior-period corrections was never tested against materiality, contrary to IAS 8's mandatory retrospective-restatement requirement for material errors (`M-AUD-06`). Fixed with a full IAS 8-grounded Error/Estimate/Materiality classification ([B04](B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md) §3b/§3c) and a no-posted-close model where Fiscal Year Close is purely declarative and Reported Retained Earnings is a derived reporting formula ([B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1e). Full record: [CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md](CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md) and [B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md) (which itself found and fixed one formula-documentation gap in its own first draft). |
| **Corrective round 4 applied** | **CORR-B4-01..08 (2026-08-30)** — ChatGPT's Round 4 re-audit (`9c0a3f2d179994a20f01db16d5713989a78c0b2a`) found three further findings, two of which (`M-AUD-08`, `M-AUD-09`) were introduced by Round 3's own fix rather than pre-existing: Reported Equity double-counted the designated Retained Earnings account (`M-AUD-08`); Reported Retained Earnings depended on `FiscalYearClosed` declaration timing rather than the Fiscal Year's own calendar boundary (`M-AUD-09`); Reported Retained Earnings had no defined Mode-1 ("as originally known") viewpoint despite the Round-3 regression relying on one (`M-AUD-10`). Fixed with a non-overlapping Reported Equity decomposition ([B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1f), boundary-driven ("Elapsed") Fiscal-Year reporting inclusion (§1e, corrected), viewpoint-parameterized Known/Current formulas (§1g), and a full algebraic re-derivation from the Raw Ledger Identity ([B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md) MP-12, Proofs A-G). Full record: [CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md](CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md) and [B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md) (the first regression round whose own construction did not surface a further gap). |
| **Corrective round 5 applied** | **CORR-B5-01..08 (2026-08-30)** — ChatGPT's Round 5 re-audit (`de7492afd0af0f58185f3f36940a77f2389aa8b8`) found two further findings, one of which (`M-AUD-11`) was introduced by Round 4's own fix: MP-12's own Proof G (Round 4) mislabeled MP-09's mixed-horizon output as a balanced Raw Trial Balance, when it is not once any Fiscal Year has elapsed (`M-AUD-11`, CRITICAL); and Fiscal Year boundaries, relied upon by Round 4's new Elapsed test, had no protection against silent retroactive editing (`M-AUD-12`, HIGH). Fixed with MP-09 renamed and split into `CumulativeAccountBalance`/`FiscalYearActivity` ([B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md)), MP-12 Proof G rebuilt into G1 (Raw Cumulative Trial Balance)/G2 (Current-FY Reporting Balance, not balanced)/G3 (Balanced Presentation TB, with an explicit never-posted derived bridge)/G4 (Known vs. Current), and a Versioned Fiscal Calendar model ([B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1h). Full record: [CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md](CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md) and [B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md](B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md) (the second consecutive regression round whose own construction did not surface a further gap). |
| **Corrective round 6 applied** | **CORR-B6-01..08 (2026-08-30)** — ChatGPT's Round 6 re-audit (`b0ce666dad72909411a49690d0f642313d94dd13`) found two further findings, BOTH introduced by Round 5's own fix: B07 §1g's Round-4 claim that the Elapsed test "never takes a viewpoint parameter" directly contradicted §1h's own Round-5 Known/Current calendar model, never revised to match (`M-AUD-13`, CRITICAL); and §1h's own post-reliance change model permitted a new boundary version to coexist indefinitely with stale Entry membership, with no defined Current-viewpoint reporting behavior (`M-AUD-14`, CRITICAL). Fixed with §1g corrected in place, new §1i formalizing `FiscalYearDefinition_Known/Current` and `Elapsed_Known/Current` ([B07](B07_CONCEPTUAL_INFORMATION_MODEL.md)), and new §1j adopting Option A (Prospective-Only Change After Reliance), refined with a new, atomic `FiscalYearMembershipRestated` mechanism ([B04](B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md)). Full record: [CORR_B6_FISCAL_CALENDAR_VIEWPOINT_MEMBERSHIP_CORRECTIVE_ROUND.md](CORR_B6_FISCAL_CALENDAR_VIEWPOINT_MEMBERSHIP_CORRECTIVE_ROUND.md) and [B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md](B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md) (the third consecutive regression round whose own construction did not surface a further gap beyond the audit's own findings). |
| **Corrective round 7 applied** | **CORR-B7-01..08 (2026-08-30)** — ChatGPT's Round 7 re-audit (`c22f236d0bf8b550636fc665a04c46281ca3d017`) found two further findings, NEITHER introduced by a recent round — both predate Round 1 entirely: B02 CAP-04's active text still named CAP-06 as the consumer of a "closed-period record... for carry-forward" (`M-AUD-15`, HIGH — carry-forward became implicit at CORR-B2-03/04; CAP-06 never had any role in it); B07's Consumption Record row still named "CAP-09's own carry-forward, which references the prior period's closing Entries" as an active example (`M-AUD-16`, HIGH — that mechanism was removed at CORR-B2-03/04/CORR-B3-05). Fixed by correcting both cross-references to name current, accurate content, plus two further self-found items (CAP-01's own stale CAP-06 claim; CAP-08's incomplete Inputs list) via a full [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §8a Dependency Sanity Matrix sweep. CAP-09 retitled to drop the ambiguous word "Transfer." Full record: [CORR_B7_ACTIVE_SEMANTIC_CONSOLIDATION_ROUND.md](CORR_B7_ACTIVE_SEMANTIC_CONSOLIDATION_ROUND.md) and [B24_CORR_B7_ACTIVE_SEMANTIC_AND_DEPENDENCY_REGRESSION.md](B24_CORR_B7_ACTIVE_SEMANTIC_AND_DEPENDENCY_REGRESSION.md) (a new reading-comprehension regression method; no further contradiction found beyond the four items disclosed). This is the corrected state of the design — every pre-correction state is preserved, visibly, inside each affected B0x file, not deleted. |

## 1. Executive Summary

Team B independently designed the Accounting Core domain for SMEsPlus across eighteen
mandatory phases (B0–B17), starting only from Team A's audited, sanitized candidate input —
never from vendor source. The design's central thread addresses the single weakness Team A's
independent research identified as most severe: the reference system permits a committed,
even externally-reported, financial fact to be silently returned to an editable state and
altered, with no forced trace. This design closes that gap structurally (a Consumption Gate,
[B04](B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md) §4) rather than procedurally, and applies the
same discipline — measured advancement, not imitation — across nine further capability areas
([B12](B12_REFERENCE_TO_ADVANCEMENT_DESIGN.md)). An internal red-team pass
([B16](B16_TEAM_B_INTERNAL_RED_TEAM_REVIEW.md)) found and fixed six real design gaps before
this pack was first assembled. A subsequent **independent** ChatGPT audit found three further,
more severe (BLOCKING) defects the internal review had missed entirely — all three corrected
in a targeted round, with a focused regression against real numeric examples (not just
algebraic assertions) finding and fixing one additional precision gap
([CORR_B05](B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md)). Clean-room provenance was independently
verified twice before the corrective round ([B14](B14_CLEAN_ROOM_PROVENANCE_MATRIX.md),
[B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §8) and re-confirmed unaffected by it (B15 §3a):
zero critical vendor-derived design risk, throughout.

**Round 2:** a second independent re-audit found the Round-1 fix for historical
reproducibility still incomplete (a backdated Correction could rewrite relied-upon history)
and found that the carry-forward model had silently generalized Team A's year-end-specific
evidence to every ordinary Period close, risking double-counted balances. Both are corrected:
Entry now carries two distinct temporal properties (Effective Date, business-meaningful;
Recorded At, system-generated and immutable — [B07](B07_CONCEPTUAL_INFORMATION_MODEL.md)
§1c), and the domain adopts a Continuous Ledger where ordinary Period close is a lock only
and Fiscal Year Close is a distinct, separately-authorized event that posts exactly one
Current-Earnings-transfer Entry ([B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1d,
[B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md) MP-11). The focused Round 2
regression ([B19](B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md)) verified every mathematical
claim with real worked numbers — including a case where the regression's own first-draft
requirement (a mandatory "Prior Period Adjustment" line) turned out to be over-engineered and
was simplified, visibly, rather than left standing uncorrected. Clean-room provenance
re-confirmed unaffected a second time ([B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §3b): zero
critical vendor-derived design risk, still.

**Round 3:** a third independent re-audit found that Round 2's own B19 Test 11 conclusion
("an ordinary current-dated Entry is always sufficient" for a Restatement crossing a closed
Fiscal Year) was silently generalized without ever testing materiality — IAS 8 (read at
primary-source level, paras 5/41/42/46) requires mandatory retrospective restatement,
excluded from current-period profit or loss, specifically for *material* prior-period errors —
and found that MP-11 (introduced by Round 2's own fix) directly contradicted this design's
repeated "Revenue/Expense never reset by a posted action" claim while also being a genuine
arithmetic bug (a posted closing Entry, however dated, would corrupt either the closing year's
own historical query or the new year's own Revenue/Expense). Both are corrected: a full
Error/Estimate/Materiality classification decision tree grounded directly in IAS 8's own
paragraph text ([B04](B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md) §3b/§3c, with materiality itself
supplied only as an external policy judgment, never computed or invented by this design —
[B09](B09_CONTROL_AUDIT_DESIGN_OBJECTIVES.md) CO-16, new), and a no-posted-close model where
Fiscal Year Close is a purely declarative event and the closing year's Current Earnings
becomes part of Reported Retained Earnings through a derived reporting formula, never a posted
transfer ([B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1e, new). The focused Round 3 regression
([B20](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md)) verified all fifteen mandated scenarios
with real worked numbers, including a continuing worked example carried through Fiscal Year
Close, a Restatement after close, and a correction of that Restatement — and, again, the
regression's own construction found and fixed one further gap (a formula-documentation
omission in B07 §1e, annotated during Tests 4/5). Clean-room provenance re-confirmed unaffected
a third time ([B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §3c): zero critical vendor-derived
design risk, still — IAS 8/TAS 8 are accounting-standard evidence, not vendor structure.

**Round 4:** a fourth independent re-audit found three further findings, two of which were
introduced by Round 3's own fix rather than pre-existing — the second consecutive round with a
self-inflicted finding, stated plainly in
[G §4d](DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md), not smoothed over. Reported Equity
(Round 3's informal `Equity(ledger, all-time) + Reported Retained Earnings`) double-counted the
designated Retained Earnings account, since that account sits inside both terms (`M-AUD-08`).
Reported Retained Earnings gated a Fiscal Year's inclusion on the `FiscalYearClosed`
*declaration* rather than the year's own calendar boundary, meaning a routine, expected delay
in the operational close process would silently omit real earnings from every report for the
duration of the gap (`M-AUD-09`). And Reported Retained Earnings had no formally defined
Mode-1 ("as originally known") viewpoint despite the Round-3 regression already relying on one
(`M-AUD-10`). All three are corrected: [B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1f (new)
partitions Equity into "Other Ledger Equity" and "Reported Retained Earnings," non-overlapping
by construction; §1e (corrected) redefines Fiscal-Year inclusion as boundary-driven ("Elapsed")
rather than declaration-driven — the same orthogonal-gates pattern this domain has used since
CORR-B01; §1g (new) parameterizes both figures by reporting viewpoint, built directly on MP-09's
existing Mode 1/Mode 2 mechanism. [B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md) MP-12
(new) formally re-derives the Reported Financial-Statement Identity from the Raw Ledger
Identity — seven lettered proofs (A-G) — closing the gap Round 3 left by asserting the
transformation rather than proving it. Three fiscal-boundary models were compared
([B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-11), with the boundary-driven model adopted
and a mandatory-atomic-close alternative independently rejected on operational grounds, not
merely because the audit cautioned against it. The focused Round 4 regression
([B21](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md)) verified all fifteen mandated scenarios with
real worked numbers, including the audit's own delayed-close failure scenario (now passing) and
the first genuine multi-Equity-account Company this design pack has constructed — and, for the
first time across four rounds, the regression's own construction did not surface a further gap,
recorded honestly as a fact about this round's process, not a claim of newly-earned confidence
in the design overall (G §4d). Clean-room provenance re-confirmed unaffected a fourth time
([B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §3d): zero critical vendor-derived design risk, still.

**Round 5:** a fifth independent re-audit found two further findings, one of which
(`M-AUD-11`) was introduced by Round 4's own new mathematical machinery — the third instance of
this specific sub-pattern (following `M-AUD-07` from Round 2's MP-11 and `M-AUD-08`/`M-AUD-09`
from Round 3's B07 §1e), stated plainly in [G §4e](DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md).
B08 MP-12's own Round-4 Proof G silently claimed MP-09's mixed-horizon output was a balanced
Raw Trial Balance — traced against Team B's own prior-round numbers (Company X, Jan 5 2025: a
mixed-horizon debit of 1250 against a credit of 1000, off by exactly 250, the prior elapsed
Fiscal Year's Current Earnings) and found false (`M-AUD-11`, CRITICAL). Separately, B07 §1e's
Elapsed test (Round 4) relied on a Fiscal Year's calendar boundary as a timeless fact, with
nothing protecting that boundary from silent retroactive editing after real accounting facts
had already depended on it (`M-AUD-12`, HIGH) — a different shape of finding from every prior
round's: not a wrong formula, but a missing protection for an input a correctly-reasoned new
mechanism had begun relying on. Both are corrected:
[B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md) MP-09 is renamed (removing "Trial
Balance" from its own name) and split into `CumulativeAccountBalance` (the true single-horizon
raw formula) and `FiscalYearActivity` (Revenue/Expense only, Fiscal-Year-bounded, never itself
a Trial Balance); MP-12 Proof G is rebuilt into G1 (Raw Cumulative Trial Balance, genuinely
balanced), G2 (Current-Fiscal-Year Reporting Balance, explicitly not balanced), G3 (Balanced
Presentation Trial Balance, with one explicit, permanently-not-postable derived bridge line),
and G4 (Known vs. Current, applied to G1-G3). [B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1h
(new) adopts a Versioned Fiscal Calendar model — pre-reliance corrections remain free, while
post-reliance changes require a new, CO-15-tier-or-stricter `FiscalYearBoundaryChanged` Audit
Event, never a silent overwrite — compared against boundary-immutability-after-use at
[B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-12. This round adds a genuine seventh Team B
assumption (the exact authorization tier for a boundary change,
[B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6) rather than resolving it unilaterally — the first
new assumption since the original six. The focused Round 5 regression
([B22](B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md)) verified all fifteen
mandated scenarios with real worked numbers, including the audit's own exact traced failure
case (now resolved) and an attempted silent calendar edit (correctly refused/routed) — the
second consecutive round whose own regression construction did not surface a further gap,
recorded honestly, not as newly-earned confidence, per
[G §4e](DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md). Clean-room provenance re-confirmed
unaffected a fifth time ([B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §3e): zero critical
vendor-derived design risk, still.

**Round 6:** a sixth independent re-audit found two further findings, BOTH introduced by Round
5's own new design surface — the fourth instance of the self-inflicted-finding sub-pattern, and
the first where both of one round's findings trace to the same single prior-round section, per
[G §4f](DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md). B07 §1g's Round-4 claim that "the
Elapsed test never takes a viewpoint parameter" directly contradicted §1h's own Round-5 Known/
Current calendar model — written the very next round, never revised to match §1g (`M-AUD-13`,
CRITICAL). Separately, §1h's own post-reliance change model permitted a new boundary version to
coexist indefinitely with stale, un-reclassified Entry membership, with no defined Current-
viewpoint reporting behavior for that state — the exact gap [B22](B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md)
Test 12 exercised without resolving (`M-AUD-14`, CRITICAL). Both are corrected: B07 §1g is
corrected in place, and new §1i formalizes `FiscalYearDefinition_Known(C,Y,T)`/`_Current(C,Y)`
and `Elapsed_Known(Y,D,T)`/`_Current(Y,D)`, proven a fixed point once T has passed by the same
Recorded-At argument BINV-11/12 already establish for Entries — not a new guarantee, the
existing one applied one level up. New §1j selects and fully specifies a post-reliance change
model — **Option A (Prospective-Only Change After Reliance), refined** — under which the
ordinary `FiscalYearBoundaryChanged` mechanism can never reach backward over reliance at all,
and a new, dedicated, atomic `FiscalYearMembershipRestated` mechanism ([B04](B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md))
handles genuine post-reliance correction, moving the Current-viewpoint boundary AND
reclassifying every affected Entry's membership in one indivisible action. `Membership_Known(E,T)`/
`Membership_Current(E)` are formalized, with the proven invariant that the two coincide unless
an explicit reclassification occurred. B07's Fiscal Year identity statement is corrected to be
viewpoint/version-safe, with no-overlap/no-coverage-gap/transition-preservation invariants
stated explicitly, compared against a strict reading of Option B at
[B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-13 (new). The focused Round 6 regression
([B23](B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md)) verified all fifteen
mandated scenarios with real worked numbers, continuing (not restarting) Company X's running
scenario and re-examining the exact Round-5 Test-12 scenario with a concrete, individually-named
Entry (Dec 15, 2024) — the third consecutive round whose own regression construction did not
surface a further gap beyond the audit's own two named findings, recorded honestly, not as
newly-earned confidence, per [G §4f](DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md).
Clean-room provenance re-confirmed unaffected a sixth time
([B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §3f): zero critical vendor-derived design risk, still.

**Round 7:** a seventh independent re-audit found two further findings, NEITHER introduced by
a recent round's own text — the first round whose findings break the self-inflicted-finding
pattern rather than extend it. B02 CAP-04's active Outputs/Downstream-dependents text still
named CAP-06 as the consumer of a "closed-period record... for carry-forward" (`M-AUD-15`,
HIGH) — stale since ordinary carry-forward became implicit at CORR-B2-03/04; CAP-04 itself had
never once appeared in any prior round's own "Corrected" header row. B07's Consumption Record
entity row still named, as an active example, "CAP-09's own carry-forward, which references the
prior period's closing Entries" (`M-AUD-16`, HIGH) — a mechanism removed at CORR-B2-03/04 and
CORR-B3-05, never swept up when this same row was edited at CORR-B01 for an unrelated reason
(trigger count). Both corrected: CAP-04's dependency list now names only current, accurate
consumers ([B02](B02_ACCOUNTING_CORE_CAPABILITY_MODEL.md)); the Consumption Record row's stale
example replaced with a currently-valid one (a Correction/Reversal Entry,
[B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1). Per the directive's own instruction to also fix
any other artifact found stale, a full Dependency Sanity Matrix
([B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §8a) was built by re-reading every capability's own
stated dependencies against its targets' actual current definitions — finding two further items
beyond the two the audit named: CAP-01's own stale CAP-06 claim ("statement placement"), and
CAP-08's incomplete Inputs list (missing CAP-07/CAP-09, both of which separately claim to feed
it). [B18](B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md) Test 5 (Round 1's own regression, never
touched since) was found still describing the pre-Round-2 posted-Entry carry-forward mechanism
and was annotated, not rewritten — its own numeric conclusion was never wrong. CAP-09 was
retitled from "Fiscal Year Close & Earnings Transfer" to "Fiscal Year Close & Boundary
Governance," per the directive's explicit instruction to remove an ambiguous word rather than
merely footnote around it. The focused Round 7 regression
([B24](B24_CORR_B7_ACTIVE_SEMANTIC_AND_DEPENDENCY_REGRESSION.md)) is the first to use a
reading-comprehension method rather than numeric/temporal verification — 9 personas, 15
mandatory scenarios, 15/15 pass, no further contradiction found beyond the four items already
disclosed. Clean-room provenance re-confirmed unaffected a seventh time
([B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §3g): zero critical vendor-derived design risk,
still — this round introduced no new design content at all, only removed stale cross-references
to an already-removed mechanism.

## 2. Authorized Input

`TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/SONNET_DEEP_SYNTHESIS/13_TEAM_B_CANDIDATE_INPUT.md`,
authorized by `TEAM_B_HANDOFF/DOMAIN_01_ACCOUNTING_CORE_E_TEAM_B_HANDOFF_AUTHORIZATION.md`
(commit `2314a786d9a1918f4cf4de3da7c2f8b85d3c98fe`), itself gated by
`BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_D_BOSS_GATE_DECISION_PACK.md` (commit
`512da309b0bbe597a1343ce386302d8f870d1fcf`). Full verification chain, including the
governance discrepancy this session found and resolved against the live authoritative
repository, is recorded in
[B00](B00_GOVERNANCE_AND_HANDOFF_VERIFICATION.md).

## 3. Scope

DOMAIN_01 Accounting Core only. Conceptual/domain design. No code, no physical schema, no
ORM, no migration implementation, no API. See
[B03](B03_DOMAIN_BOUNDARY_MODEL.md) §4/§4a for the explicit out-of-scope boundary and the
inter-company-transaction clarification added during red-team review.

## 4. Independent Design Principles

`Understand the reference deeply. Rebuild independently. Improve measurably.` Applied
concretely: every capability (§6) was defined from business responsibility first, checked
against — and in three documented respects diverges from — the reference system's actual
module shape ([B02](B02_ACCOUNTING_CORE_CAPABILITY_MODEL.md) §3).

## 5. Capability Model

Nine capabilities: Chart of Accounts Governance, Financial Fact Capture & Commitment,
Correction & Reversal, Period Control *(Outputs/Downstream-dependents corrected at CORR-B7-01
— a stale claim that CAP-06 relies on this capability for carry-forward, predating every
corrective round, `M-AUD-15`)*, Company/Entity Boundary Enforcement, Currency Recognition &
Remeasurement, Regulated Document Integrity, Audit Trail & Evidence Provision *(Inputs
corrected at CORR-B7-04 to reciprocate CAP-07/CAP-09's own already-stated dependency on it)*,
Fiscal Year Close & Boundary Governance *(renamed from "Period-End Carry-Forward" at
CORR-B2-03/04; "Earnings Transfer" corrected at CORR-B3-05 — this section's name for it was
left stale through Round 2 and is fixed here — posts no financial Entry; retitled again at
CORR-B7-05, dropping "Earnings Transfer" entirely — the word alone risked being misread as a
posted transfer despite the re-scoping footnote, and the capability's own scope has since grown
to include Fiscal Year boundary/membership governance, which the old title never named)*. Chart
of Accounts Governance's own downstream-dependents list also corrected at CORR-B7-04 (a stale
"CAP-06, statement placement" claim, self-found, same category as `M-AUD-15`). Full definitions,
ownership, and dependency graph: [B02](B02_ACCOUNTING_CORE_CAPABILITY_MODEL.md).

## 6. Domain Boundaries

Boundary statement, nine conceptual objects (Financial Fact, Entry, Line, Posting, Ledger,
Period, Currency Context, Correction/Reversal, Audit Evidence), eleven neighbor seams, and
explicit out-of-scope list: [B03](B03_DOMAIN_BOUNDARY_MODEL.md).

## 7. Lifecycle / Event Model

Four states (DRAFT, COMMITTED, VOIDED, SUPERSEDED — the last a Team B addition), ten forced
event types (including `PeriodReopened`, added at CORR-B01), and the Consumption Gate — the
domain's central original design contribution, extending Team A's neutral observation into an
actual enforced mechanism. **Corrected at CORR-B01/B03:** Period Lock and Consumption are now
two independent, orthogonal gates on Amendment (period close is no longer a Consumption
trigger — three triggers, not four); Void is now always a dated, linked Correction Entry,
never a status flip. [B04](B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md).

## 8. Invariant Baseline

Seventeen invariants (BINV-01..17, the last six added at CORR-B2-01/02, CORR-B3-04,
CORR-B4-01/02/03, CORR-B5-01/02/05, and CORR-B6-01/02/03 respectively): six independently
re-evaluated from Team A's INV-01..06, eleven newly added (Consumption Record Permanence, Audit
Evidence Independence, Account Category Immutability, Carry-Forward Correctness, Historical
As-of Reproducibility, Recorded-At Immutability, Material Prior-Period Error P&L Exclusion,
Reported Equity Non-Duplication and Declaration-Independence, Trial Balance Output
Non-Confusion, Fiscal Year Boundary Historical Safety, and now Fiscal-Year Membership Viewpoint
Coherence). All six mandated coverage areas confirmed. **Corrected at CORR-B01:** BINV-06's
trigger list fixed to match B04. **Rewritten at CORR-B02, again at CORR-B3-05, and again at
CORR-B4-01/02/03:** BINV-10 no longer requires a posted Current-Earnings transfer at close —
Fiscal Year Close posts no Entry; Current Earnings becomes part of Reported Retained Earnings
via a derived, non-overlapping, boundary-driven formula instead
([B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1e/§1f). **Added at CORR-B5-01/02/05:** BINV-15
requires the Raw Cumulative Trial Balance, Current-Fiscal-Year Reporting Balance, and Balanced
Presentation Trial Balance never be confused with one another (`M-AUD-11`); BINV-16 requires a
Fiscal Year boundary that has governed real facts never be silently edited in place (`M-AUD-12`,
§1h). **Added at CORR-B6-01/02/03:** BINV-17 requires every Fiscal-Year boundary/Elapsed lookup
to be viewpoint-consistent, every Entry to have exactly one authoritative membership per
viewpoint, and no reachable hybrid state between a post-reliance boundary change and Entry
membership (`M-AUD-13`/`M-AUD-14`, §1i/§1j). [B05](B05_ACCOUNTING_INVARIANT_BASELINE.md).

## 9. Business Rule Baseline

Fifteen rules (BR-01..15): thirteen restated from Team A's GR-01..13 in this domain's own
vocabulary — three explicitly strengthened past the reference system's observed weaknesses
(BR-05 no bypass, BR-07 no mutation of consumed facts, BR-13 full deprecation guard) — plus
two new rules (BR-14 Amendment, BR-15 Consumption recording):
[B06](B06_BUSINESS_RULE_BASELINE.md).

## 10. Conceptual Information Model

**Twelve** conceptual entities *(corrected at CORR-B7-03 — this section had never been updated
to reflect the Fiscal Year entity added at Round 2, and still said "Eleven"; found during this
round's active-semantic sweep)*, cardinality rules tied to specific invariants, three identity
principles (no source-ID reuse; identity independent of display numbers; Audit Events
identified by append-only sequence alone), amended during red-team review to add Normal Balance
Side and tenant/company-scoped Audit Event identity, and at Round 6/7 to add viewpoint-aware
Fiscal Year definition/membership (§1i/§1j) and to correct the Consumption Record entity's own
stale downstream-reference example (`M-AUD-16`): [B07](B07_CONCEPTUAL_INFORMATION_MODEL.md).

## 11. Accounting & Mathematical Design Principles

Twelve principles (MP-01..12: MP-09 **renamed at CORR-B5-02** from "Aggregation (Account
Balance / Trial Balance)" to "Cumulative Account Balance & Fiscal-Year Activity," split into
two formula families; MP-11 added at CORR-B2-03/04, rewritten at CORR-B3-05, cross-reference-
corrected at CORR-B4-01/02/03; MP-12 new at CORR-B4-01/02/03/05, Proof G **rebuilt at
CORR-B5-03/04**) covering all eleven mandated areas, including a full proof of the expanded
accounting equation (`Assets + Expenses = Liabilities + Equity + Revenue`, holding
unconditionally, with the simple equation as the closed-period special case — **corrected at
CORR-B02** after the original proof was found incomplete for open periods, and verified
numerically against a worked example in [CORR-B05](B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md)),
a proof that a constructed reversal is automatically balanced, a time-consistent, two-mode
aggregation formula (**corrected at CORR-B03, rebuilt at CORR-B2-01/02, renamed/split at
CORR-B5-02** — no longer filters by an Entry's current status, distinguishes "as originally
known" from "current/restated," and now separates the true single-horizon Cumulative Balance
formula from the narrower, Fiscal-Year-bounded Activity formula MP-09 previously conflated
under one name — `M-AUD-11`), a Fiscal Year Close principle (**rewritten at CORR-B3-05,
cross-reference-corrected at CORR-B4-01/02/03** — no longer a posted closing Entry, now a
derived, non-overlapping, boundary-driven Reported-Retained-Earnings reporting formula), a
Reported Equity Reconciliation principle (**MP-12, added at CORR-B4-01/02/03/05, Proof G
rebuilt at CORR-B5-03/04, Proofs D/G4 corrected for viewpoint consistency at CORR-B6-04** — a
full re-derivation of the Reported Financial-Statement Identity from the Raw Ledger Identity,
now correctly distinguishing the Raw Cumulative Trial Balance from the Current-Fiscal-Year
Reporting Balance from the Balanced Presentation Trial Balance, G1-G4, with every Fiscal-Year
boundary lookup routed through the matching Known/Current viewpoint), and a proposed rounding
policy where Team A's evidence left the question open (flagged for gate confirmation).
**MP-09's `FiscalYearActivity` corrected at CORR-B6-01** to use a viewpoint-parameterized
`FiscalYearStart_Known/Current` boundary lookup (B07 §1i) in place of a bare, unparameterized
one — closing `M-AUD-13`: [B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md).

## 12. Control / Audit Design Objectives

Sixteen objectives (CO-01..16: CO-13 added during red-team review; CO-14/CO-15 added at
CORR-B2-01/02 for temporal-mode labeling and Restatement authorization; CO-16 added at
CORR-B3-04, requiring that materiality remain a policy/judgment input this domain's design
never computes or invents; CO-14's scope extended at CORR-B4-04 to explicitly cover Reported
Retained Earnings/Equity outputs, again at CORR-B5-02 to cover the three Trial Balance outputs
(G1/G2/G3), and again at CORR-B6-01/02 to cover which Fiscal-Year-boundary viewpoint and which
membership a presentation is using; CO-15's authorization tier reused, not reinvented, at
CORR-B5-05 for post-reliance Fiscal Year boundary changes, and again at CORR-B6-02 for the new
`FiscalYearMembershipRestated` event) covering all twelve mandated areas plus an explicit
residual scope boundary (infrastructure-level bypass is outside this domain's control-design
reach): [B09](B09_CONTROL_AUDIT_DESIGN_OBJECTIVES.md).

## 13. Migration Requirements

Sixteen canonical, source-neutral requirements (MG-C01..16: MG-C13 added during red-team
review to cover source-side unposted activity at cutover; MG-C14 added at CORR-B2-03/04 for
migrated-Entry Recorded At; MG-C15 added at CORR-B4-07, requiring an explicit, unambiguous
designated-Retained-Earnings-account configuration per Company, required by B07 §1f's
`M-AUD-08` fix; MG-C11 precision-corrected and MG-C16 added at CORR-B5-07, confirming Fiscal
Year calendar setup at migration is always pre-reliance, `M-AUD-12`):
[B10](B10_CANONICAL_MIGRATION_REQUIREMENTS.md).

## 14. Exception Model

Twenty-two scenarios (the 19th, prior-period-error materiality misclassification, added at
CORR-B3-01/02; the 20th, delayed Fiscal Year Close declaration — resolved by design, not a
genuine failure mode — added at CORR-B4-03; the 21st, attempted post-reliance Fiscal Year
boundary edit, added at CORR-B5-05, corrected at CORR-B6-02 — the "authorized path" is now a
distinct, atomic action, never `FiscalYearBoundaryChanged` itself; the 22nd, genuine
post-reliance membership reclassification and rejected overlapping/gapped calendar versions,
added at CORR-B6-02/05), six of the original eighteen requiring genuinely new design (wrong
tenant, duplicate detection, future posting, missing reference, concurrency, partial failure)
because Team A's evidence either declined to analyze them or found the reference system's own
answer unproven: [B11](B11_EXCEPTION_FAILURE_MODEL.md).

## 15. Advancement Design

Nine advancement items (AD-01..09, the last identified independently by Team B, not present
in Team A's ADV-01..08), each with a chosen design mechanism and a measurement criterion:
[B12](B12_REFERENCE_TO_ADVANCEMENT_DESIGN.md).

## 16. Design Options / Trade-offs

Thirteen significant decisions (DT-07 added at CORR-B03; DT-08/DT-09 added at CORR-B2-01..04;
DT-10 added at CORR-B3-05; DT-11 added at CORR-B4-03; DT-12 added at CORR-B5-05; DT-13 added at
CORR-B6-02) formally compared across eight dimensions each, with Team-B-only recommendations
explicitly marked not-yet-approved. **Revised at CORR-B01:** DT-02's original recommendation
was withdrawn as internally contradictory (not merely reconsidered) and replaced with a
coherent option, kept visible alongside the withdrawal. **Added at CORR-B3-05:** DT-10 compares
the Round-2 posted-Fiscal-Year-Close-Entry model against a no-posted-close derived-formula
model, finding the former structurally defective rather than merely less preferred. **Added at
CORR-B4-03:** DT-11 compares three models for Fiscal-Year reporting-inclusion timing. **Added
at CORR-B5-05:** DT-12 compares boundary-immutability-after-use against a Versioned Fiscal
Calendar model (adopted — strictly generalizes the former's protection while adding a harmless
pre-reliance escape hatch) for Fiscal Year boundary historical safety. **Added at CORR-B6-02:**
DT-13 compares Prospective-Only Change After Reliance (adopted, refined) against a strict
reading of Retroactive Change with Atomic Restatement for post-reliance Fiscal-Year-membership
change — the former keeps the existing `FiscalYearBoundaryChanged` mechanism lightweight and
introduces one new, dedicated, atomic mechanism for the rare reliance-reaching case, rather than
overloading one mechanism with two purposes: [B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md).

## 17. Clean-Room Provenance

Every material decision mapped to Accounting Standard / Regulatory Requirement / Industry
Principle / Cross-ERP Pattern / Team A Fact / Migration Requirement / Independent Reasoning.
Three vendor-adjacent terms individually reviewed and confirmed traceability-only.
**Critical Vendor-Derived Design Risk = 0**, re-confirmed unaffected by the CORR-B01/B02/B03
corrections, again by CORR-B2-01..05, again by CORR-B3-01..08, again by CORR-B4-01..08, again
by CORR-B5-01..08, again by CORR-B6-01..08, and again by CORR-B7-01..08 (Round 7's corrections
are pure active-semantic/dependency hygiene, removing stale cross-references to an
already-removed mechanism — no new design content, nothing to newly vet against vendor
structure): [B14](B14_CLEAN_ROOM_PROVENANCE_MATRIX.md).

## 18. Traceability

Full chains traced end-to-end for three exemplar threads; one ID-space collision and one
rule-interaction gap found internally and resolved explicitly (not silently). **Three further,
more severe (BLOCKING) defects were subsequently found by ChatGPT's independent audit — not
by this domain's own traceability pass — and are recorded with equal transparency, including
the honest note that this domain's own review missed them (§3a); two more were found by
ChatGPT's Round 2 re-audit (§3b); two more were found by ChatGPT's Round 3 re-audit (§3c);
three more were found by ChatGPT's Round 4 re-audit (§3d), two of which were introduced by
Round 3's own fix; two more were found by ChatGPT's Round 5 re-audit (§3e), one of which was
introduced by Round 4's own fix; two more were found by ChatGPT's Round 6 re-audit (§3f), BOTH
of which were introduced by Round 5's own fix; two more were found by ChatGPT's Round 7
re-audit (§3g), NEITHER introduced by a recent round — both predate Round 1 entirely — plus two
further stale/incomplete dependency edges (and one stale summary count in this document's own
§10) found by this domain's own §8a dependency sanity sweep — the pattern named at §3a is
recorded as having recurred a seventh time, with Round 7 breaking rather than extending the
self-inflicted-finding sub-pattern §3d-§3f established:**
[B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §3a/§3b/§3c/§3d/§3e/§3f/§3g. Zero orphan critical
decisions, zero circular definitions, zero regulatory overreach, before and after all seven
correction rounds: [B15](B15_DESIGN_TRACEABILITY_MATRIX.md).

## 19. Residual Unknowns

Team A's full 20-item residual register carries forward unchanged, incorporated by reference
([B01](B01_AUTHORIZED_INPUT_REGISTER.md) §11). This domain's design does not depend on any of
them resolving in a particular direction (see [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6 for
the two items — OQ-01, OQ-02 — explicitly checked against this design's dependencies).

## 20. Assumptions

**Seven** Team B design assumptions requiring gate confirmation, consolidated in
[B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6: rounding method (round-half-up); period-close
vs. consumption (**revised at CORR-B01** — the internal contradiction is fixed, a narrower
residual question about reopen time-limits remains open); chart-of-accounts template/instance
structure; audit-trail tamper-evidence scope beyond evidenced legal requirement; flexible
correction shape (Void, B13 DT-07, is now understood as an instance of this same flexibility);
and the CO-02/CO-06 configuration-coupling rule found during traceability review. **No
assumption was resolved by Team B itself during any corrective round** — assumption #2's
Round 1 and Round 2 revisions were required fixes to an incoherent design, distinguished
explicitly from the other five genuine open choices (see
[CORR_B01_B02_B03_CORRECTIVE_ROUND.md](CORR_B01_B02_B03_CORRECTIVE_ROUND.md) §6). **Round 3
narrowed or resolved none of the six** — its findings (error/estimate/materiality
classification, Fiscal Year Close posting semantics) do not bear on any of the six assumptions'
subject matter, stated explicitly rather than left for a reader to infer (see
[CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md](CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md)
§7 and [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6's Round 3 note). Materiality itself, the one
new judgment-input concept Round 3 introduces, is not a seventh assumption — CO-16 closes it as
a settled design decision (externally supplied, never computed here), not an open question.
**Round 4 likewise narrowed or resolved none of the original six** — its findings are pure
reporting-equity mathematics (double-counting, boundary timing, viewpoint parameterization),
with no bearing on any of the six assumptions' subject matter (see
[CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md](CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md)
§8 and [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6's Round 4 note). The designated Retained
Earnings account (B07 §1f, B10 MG-C15) is likewise not a seventh assumption — it is a required,
unambiguous migration-configuration fact with exactly one correct answer per Company, not an
open judgment call. **Round 5 narrowed or resolved none of the original six either, but adds a
genuine seventh** — the exact authorization tier for a post-reliance Fiscal Year boundary
change (B07 §1h, BINV-16) is a real open policy question this domain's own evidence does not
settle, unlike materiality or the designated RE account, both of which are closed design
decisions rather than open ones. This domain's working default (reuse CO-15's Restatement
tier) is stated as a default, not asserted as the settled answer (see
[CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md](CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md)
§7 and [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6's Round 5 note). **Round 6 narrowed or
resolved none of the seven, and adds no eighth** — its findings (Fiscal Calendar viewpoint
coherence, post-reliance membership semantics) are pure internal-consistency corrections with
no bearing on any of the seven assumptions' subject matter; the seventh assumption's own tier
question is unchanged in wording, since Round 6 selects WHICH mechanism applies WHEN
(DT-13), not WHAT tier governs either mechanism — a design decision this domain makes and
justifies, not an open policy question (see
[CORR_B6_FISCAL_CALENDAR_VIEWPOINT_MEMBERSHIP_CORRECTIVE_ROUND.md](CORR_B6_FISCAL_CALENDAR_VIEWPOINT_MEMBERSHIP_CORRECTIVE_ROUND.md)
§9 and [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6's Round 6 note). **Round 7 likewise narrowed
or resolved none of the seven, and adds no eighth** — its findings and self-found corrections
are pure active-semantic/dependency hygiene (stale cross-references to an already-removed
mechanism, an ambiguous title, an unmaintained count), with zero bearing on rounding method,
period-close/consumption timing, chart-of-accounts structure, tamper-evidence scope,
correction-shape flexibility, the CO-02/CO-06 coupling, or the Fiscal Year boundary
authorization tier (see
[CORR_B7_ACTIVE_SEMANTIC_CONSOLIDATION_ROUND.md](CORR_B7_ACTIVE_SEMANTIC_CONSOLIDATION_ROUND.md)
§9 and [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6's Round 7 note).

## 21. Red-Team Findings

Ten personas engaged in the original pass; six real, substantive gaps found and fixed (not
merely noted); two areas checked and confirmed already-adequate without padding; two areas
confirmed correctly out of this phase's scope. **Honest addendum added at CORR-B01/B02/B03**
([B16](B16_TEAM_B_INTERNAL_RED_TEAM_REVIEW.md) §13): none of the ten personas caught any of
the three defects the subsequent independent audit found. A further, focused seven-persona
regression against the corrected design ([CORR-B05](B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md))
tested eight adversarial scenarios, including two verified with real worked numbers (not just
algebra), and found one additional precision gap — fixed before this pack was updated. Full
record, including every fix's exact text: [B16](B16_TEAM_B_INTERNAL_RED_TEAM_REVIEW.md).

## 22. Acceptance Criteria

```
B0–B16 evidence artifacts completed          : YES (17 of 17 prior phases)
Authorized Input fully registered            : YES (B01)
Critical invariants traceable                : YES (B05, B15)
Critical rules traceable                     : YES (B06, B15)
Conceptual design complete                   : YES (B07)
Math/accounting principles defined           : YES (B08)
Lifecycle/events coherent                    : YES (B04)
Control objectives defined                   : YES (B09)
Migration requirements defined               : YES (B10)
Critical exceptions analyzed                 : YES (B11)
Advancement criteria measurable              : YES (B12)
Design options documented                    : YES (B13)
Critical Vendor-Derived Design Risk = 0      : YES (B14)
Critical orphan design decisions = 0         : YES (B15)
Class G items still visible                  : YES (B01 §11, B15 §6, this section §19)
Regulatory scope not overstated              : YES (B09 CO-07/CO-11, B15 §7)
Internal Red-Team completed                  : YES (B16)
Independent audit findings corrected (Round 1) : YES — all 3 BLOCKING findings from
                                                `aa60c2d0497cefe804d37953bbfaa597c3476d79`
                                                resolved (CORR_B01_B02_B03_CORRECTIVE_ROUND.md)
Focused regression completed (Round 1)       : YES (B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md)
Independent audit findings corrected (Round 2) : YES — both BLOCKING findings from
                                                `04e44b06489d8bea6c8d39410050d68cf08bce21`
                                                resolved (CORR_B2_CORRECTIVE_ROUND.md)
Focused regression completed (Round 2)       : YES (B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md)
Independent audit findings corrected (Round 3) : YES — both findings from
                                                `f6fb633fd141f45caf047bc94d75f84420e1cc6d`
                                                resolved (CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md)
Accounting-standard regression completed (Round 3) : YES (B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md)
Primary-source accounting-standard evidence used (Round 3) : YES — IAS 8 read directly from
                                                fetched PDF text, paras 1-54; TAS 8 confidence
                                                explicitly held at secondary-source tier only
Independent audit findings corrected (Round 4) : YES — all 3 findings from
                                                `9c0a3f2d179994a20f01db16d5713989a78c0b2a`
                                                resolved (CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md),
                                                including 2 introduced by Round 3's own fix
Reporting-equity regression completed (Round 4) : YES (B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md)
  — the first regression round whose own construction found no further gap
Full algebraic re-derivation, Raw Ledger Identity to Reported Financial-Statement Identity
  (Round 4)                                    : YES — B08 MP-12, Proofs A-G
Jira governance red flags (owner/due date) preserved, not invented (Round 4) : YES —
                                                `ERPPLUS-100` remains UNASSIGNED / TBD
Independent audit findings corrected (Round 5) : YES — both findings from
                                                `de7492afd0af0f58185f3f36940a77f2389aa8b8`
                                                resolved (CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md),
                                                including 1 introduced by Round 4's own fix
Trial Balance / Fiscal Calendar regression completed (Round 5) : YES
  (B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md) — the second consecutive
  regression round whose own construction found no further gap
MP-09 renamed, split into Cumulative Balance / Fiscal-Year Activity; MP-12 Proof G rebuilt
  into G1-G4 (Round 5)                          : YES — B08 MP-09/MP-12
Versioned Fiscal Calendar model adopted, compared against boundary-immutability (Round 5) :
                                                YES — B07 §1h, B13 DT-12
Jira governance red flags (owner/due date) preserved, not invented (Round 5) : YES —
                                                `ERPPLUS-100` remains UNASSIGNED / TBD
  (independently re-verified via direct Jira lookup, not assumed carried-forward)
Independent audit findings corrected (Round 6) : YES — both findings from
                                                `b0ce666dad72909411a49690d0f642313d94dd13`
                                                resolved (CORR_B6_FISCAL_CALENDAR_VIEWPOINT_MEMBERSHIP_CORRECTIVE_ROUND.md),
                                                BOTH introduced by Round 5's own fix
Fiscal Calendar Viewpoint & Membership regression completed (Round 6) : YES
  (B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md) — the third
  consecutive regression round whose own construction found no further gap beyond the
  audit's own two named findings
Elapsed test and Fiscal-Year boundary lookup made viewpoint-aware end-to-end; no
  `_Known(...,T)` formula anywhere in this design silently consults today's calendar
  (Round 6)                                     : YES — B07 §1i, B08 MP-09/MP-12 Proofs D/G4
Post-reliance change model selected (Option A, refined) and fully specified, including a
  new atomic `FiscalYearMembershipRestated` mechanism; no reachable hybrid boundary-
  version/Entry-membership state (Round 6)      : YES — B07 §1j, B04, B13 DT-13
Fiscal Year cardinality/identity restated as viewpoint/version-safe; no-overlap/no-coverage-
  gap/transition-preservation/future-validation invariants stated, no storage invented
  (Round 6)                                     : YES — B07 §1/§1j
Jira governance red flags (owner/due date) preserved, not invented (Round 6) : YES —
                                                `ERPPLUS-100` remains UNASSIGNED / TBD
  (independently re-verified via direct Jira lookup, not assumed carried-forward)
Independent audit findings corrected (Round 7) : YES — both findings from
                                                `c22f236d0bf8b550636fc665a04c46281ca3d017`
                                                resolved (CORR_B7_ACTIVE_SEMANTIC_CONSOLIDATION_ROUND.md),
                                                NEITHER introduced by a recent round — both
                                                predate Round 1 entirely
Active-Semantic & Dependency regression completed (Round 7) : YES
  (B24_CORR_B7_ACTIVE_SEMANTIC_AND_DEPENDENCY_REGRESSION.md) — first reading-comprehension-
  method regression; no further contradiction found beyond the four items disclosed
CAP-04/CAP-01 stale CAP-06 cross-references removed; CAP-08 Inputs completed; Consumption
  Record's stale CAP-09 carry-forward example replaced with a currently-valid one (Round 7) :
                                                YES — B02 CAP-01/04/08, B07 §1, B15 §8a
Dependency Sanity Matrix built, all four required acceptance criteria confirmed (Round 7) :
                                                YES — B15 §8a
CAP-09 retitled to remove an ambiguous word, per explicit directive instruction (Round 7) :
                                                YES — B02 CAP-09
Jira governance red flags (owner/due date) preserved, not invented (Round 7) : YES —
                                                `ERPPLUS-100` remains UNASSIGNED / TBD
  (independently re-verified via direct Jira lookup, not assumed carried-forward)
```

## 23. Measured Advancement Criteria (summary — full detail in B12)

| Item | Reference-system status | This design's target |
|---|---|---|
| AD-01 Balance guarantee | Suppressible, app-only, 0 DB triggers | Structurally non-optional |
| AD-03 Period control mechanisms | 8+ independent, disagreeing controls | 1 authoritative answer + 1 logged override path |
| AD-04 Consumed-fact correction | Both sound and unsound paths coexist, unforced | 100% additive for consumed facts, structurally enforced |
| AD-06 Monetary representation | 3 independently-writable columns, structurally-possible disagreement | 2 authoritative values, derived views only |
| AD-09 Multi-tenant safety | Not evaluated (single-deployment reference) | 0 capabilities requiring cross-tenant shared state |

**Evidence Pack complete. Proceeding to self-review (G) and Final Gate Candidate (H).**
