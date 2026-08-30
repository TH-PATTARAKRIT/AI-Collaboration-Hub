# DOMAIN_01 ACCOUNTING CORE — TEAM B DESIGN EVIDENCE PACK

| Field | Value |
|---|---|
| Project | SMEsPlus ENTERPRISE SUITE |
| STATE | STATE03 — Architecture |
| Workstream | SMEsPlus Migration Factory |
| Board | Board06 — Data & Canonical Model |
| Domain | DOMAIN_01 — Accounting Core |
| Team | Team B — Independent Clean-Room Design |
| Directive | SMEPLUS-26-08-29-MIG-B-D01-E2E-001, corrective rounds SMEPLUS-26-08-29-MIG-B-D01-CORR-001, SMEPLUS-26-08-29-MIG-B-D01-CORR2-001, SMEPLUS-26-08-29-MIG-B-D01-CORR3-001, and SMEPLUS-26-08-30-MIG-B-D01-CORR4-001 |
| Date | 2026-08-30 |
| Executor | Claude Sonnet 5 |
| **Corrective round 1 applied** | **CORR-B01/B02/B03 (2026-08-29)** — ChatGPT Independent Design Audit (`aa60c2d0497cefe804d37953bbfaa597c3476d79`) found three BLOCKING defects, all corrected: a Consumption/Period-reopen contradiction, an incomplete accounting-equation proof, and time-inconsistent historical as-of balances after VOID. Full record: [CORR_B01_B02_B03_CORRECTIVE_ROUND.md](CORR_B01_B02_B03_CORRECTIVE_ROUND.md) and [B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md](B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md). |
| **Corrective round 2 applied** | **CORR-B2-01..05 (2026-08-29)** — ChatGPT's Round 2 re-audit (`04e44b06489d8bea6c8d39410050d68cf08bce21`) found two further BLOCKING defects: a backdated Correction could still rewrite relied-upon history (`M-AUD-04`), and CAP-09 overgeneralized Team A's year-end-specific carry-forward rule to every ordinary Period close, risking double-counted balances (`M-AUD-05`). Fixed with a two-temporal-axis model (Effective Date / Recorded At) and a Continuous Ledger with Fiscal Year Close as a distinct event from ordinary Period Lock. Full record: [CORR_B2_CORRECTIVE_ROUND.md](CORR_B2_CORRECTIVE_ROUND.md) and [B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md](B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md) (which itself found and corrected one over-engineered requirement in its own first draft). |
| **Corrective round 3 applied** | **CORR-B3-01..08 (2026-08-29)** — ChatGPT's Round 3 re-audit (`f6fb633fd141f45caf047bc94d75f84420e1cc6d`) found two further findings: Round 2's own Fiscal Year Close fix (MP-11) directly contradicted this design's "Revenue/Expense never reset by a posted action" claim and was a genuine arithmetic bug (`M-AUD-07`), and the Round-2 regression's own conclusion about prior-period corrections was never tested against materiality, contrary to IAS 8's mandatory retrospective-restatement requirement for material errors (`M-AUD-06`). Fixed with a full IAS 8-grounded Error/Estimate/Materiality classification ([B04](B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md) §3b/§3c) and a no-posted-close model where Fiscal Year Close is purely declarative and Reported Retained Earnings is a derived reporting formula ([B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1e). Full record: [CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md](CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md) and [B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md) (which itself found and fixed one formula-documentation gap in its own first draft). |
| **Corrective round 4 applied** | **CORR-B4-01..08 (2026-08-30)** — ChatGPT's Round 4 re-audit (`9c0a3f2d179994a20f01db16d5713989a78c0b2a`) found three further findings, two of which (`M-AUD-08`, `M-AUD-09`) were introduced by Round 3's own fix rather than pre-existing: Reported Equity double-counted the designated Retained Earnings account (`M-AUD-08`); Reported Retained Earnings depended on `FiscalYearClosed` declaration timing rather than the Fiscal Year's own calendar boundary (`M-AUD-09`); Reported Retained Earnings had no defined Mode-1 ("as originally known") viewpoint despite the Round-3 regression relying on one (`M-AUD-10`). Fixed with a non-overlapping Reported Equity decomposition ([B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1f), boundary-driven ("Elapsed") Fiscal-Year reporting inclusion (§1e, corrected), viewpoint-parameterized Known/Current formulas (§1g), and a full algebraic re-derivation from the Raw Ledger Identity ([B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md) MP-12, Proofs A-G). Full record: [CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md](CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md) and [B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md) (the first regression round whose own construction did not surface a further gap). This is the corrected state of the design — every pre-correction state is preserved, visibly, inside each affected B0x file, not deleted. |

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
Correction & Reversal, Period Control, Company/Entity Boundary Enforcement, Currency
Recognition & Remeasurement, Regulated Document Integrity, Audit Trail & Evidence Provision,
Fiscal Year Close & Earnings Transfer *(renamed from "Period-End Carry-Forward" at
CORR-B2-03/04; corrected again at CORR-B3-05 — this section's name for it was left stale
through Round 2 and is fixed here — posts no financial Entry; "Earnings Transfer" now names a
reporting-time derivation, [B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1e, not a posted
action)*. Full definitions, ownership, and dependency graph:
[B02](B02_ACCOUNTING_CORE_CAPABILITY_MODEL.md).

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

Fourteen invariants (BINV-01..14, the last three added at CORR-B2-01/02, CORR-B3-04, and
CORR-B4-01/02/03 respectively): six independently re-evaluated from Team A's INV-01..06, eight
newly added (Consumption Record Permanence, Audit Evidence Independence, Account Category
Immutability, Carry-Forward Correctness, Historical As-of Reproducibility, Recorded-At
Immutability, Material Prior-Period Error P&L Exclusion, and now Reported Equity Non-Duplication
and Declaration-Independence). All six mandated coverage areas confirmed. **Corrected at
CORR-B01:** BINV-06's trigger list fixed to match B04. **Rewritten at CORR-B02, again at
CORR-B3-05, and again at CORR-B4-01/02/03:** BINV-10 no longer requires a posted Current-
Earnings transfer at close — Fiscal Year Close posts no Entry; Current Earnings becomes part of
Reported Retained Earnings via a derived, non-overlapping, boundary-driven formula instead
([B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1e/§1f). [B05](B05_ACCOUNTING_INVARIANT_BASELINE.md).

## 9. Business Rule Baseline

Fifteen rules (BR-01..15): thirteen restated from Team A's GR-01..13 in this domain's own
vocabulary — three explicitly strengthened past the reference system's observed weaknesses
(BR-05 no bypass, BR-07 no mutation of consumed facts, BR-13 full deprecation guard) — plus
two new rules (BR-14 Amendment, BR-15 Consumption recording):
[B06](B06_BUSINESS_RULE_BASELINE.md).

## 10. Conceptual Information Model

Eleven conceptual entities, cardinality rules tied to specific invariants, three identity
principles (no source-ID reuse; identity independent of display numbers; Audit Events
identified by append-only sequence alone), amended during red-team review to add Normal
Balance Side and tenant/company-scoped Audit Event identity:
[B07](B07_CONCEPTUAL_INFORMATION_MODEL.md).

## 11. Accounting & Mathematical Design Principles

Twelve principles (MP-01..12: MP-11 added at CORR-B2-03/04, rewritten at CORR-B3-05, cross-
reference-corrected at CORR-B4-01/02/03; MP-12 new at CORR-B4-01/02/03/05) covering all eleven
mandated areas, including a full proof of the expanded accounting equation (`Assets + Expenses
= Liabilities + Equity + Revenue`, holding unconditionally, with the simple equation as the
closed-period special case — **corrected at CORR-B02** after the original proof was found
incomplete for open periods, and verified numerically against a worked example in
[CORR-B05](B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md)), a proof that a constructed reversal is
automatically balanced, a time-consistent, two-mode aggregation formula (**corrected at
CORR-B03, then rebuilt at CORR-B2-01/02** — no longer filters by an Entry's current status, and
now distinguishes "as originally known" from "current/restated" via the Effective Date/
Recorded At split, closing a historical-rewrite defect), a Fiscal Year Close principle
(**rewritten at CORR-B3-05, cross-reference-corrected at CORR-B4-01/02/03** — no longer a
posted closing Entry, now a derived, non-overlapping, boundary-driven Reported-Retained-
Earnings reporting formula), a new Reported Equity Reconciliation principle (**MP-12, added at
CORR-B4-01/02/03/05** — a full seven-proof re-derivation of the Reported Financial-Statement
Identity from the Raw Ledger Identity, closing a gap where Round 3 had asserted the
transformation rather than proving it), and a proposed rounding policy where Team A's evidence
left the question open (flagged for gate confirmation):
[B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md).

## 12. Control / Audit Design Objectives

Sixteen objectives (CO-01..16: CO-13 added during red-team review; CO-14/CO-15 added at
CORR-B2-01/02 for temporal-mode labeling and Restatement authorization; CO-16 added at
CORR-B3-04, requiring that materiality remain a policy/judgment input this domain's design
never computes or invents; CO-14's scope extended at CORR-B4-04 to explicitly cover Reported
Retained Earnings/Equity outputs) covering all twelve mandated areas plus an explicit residual
scope boundary (infrastructure-level bypass is outside this domain's control-design reach):
[B09](B09_CONTROL_AUDIT_DESIGN_OBJECTIVES.md).

## 13. Migration Requirements

Fifteen canonical, source-neutral requirements (MG-C01..15: MG-C13 added during red-team
review to cover source-side unposted activity at cutover; MG-C14 added at CORR-B2-03/04 for
migrated-Entry Recorded At; MG-C15 added at CORR-B4-07, requiring an explicit, unambiguous
designated-Retained-Earnings-account configuration per Company, required by B07 §1f's
`M-AUD-08` fix): [B10](B10_CANONICAL_MIGRATION_REQUIREMENTS.md).

## 14. Exception Model

Twenty scenarios (the 19th, prior-period-error materiality misclassification, added at
CORR-B3-01/02; the 20th, delayed Fiscal Year Close declaration — resolved by design, not a
genuine failure mode — added at CORR-B4-03), six of the original eighteen requiring genuinely
new design (wrong tenant, duplicate detection, future posting, missing reference, concurrency,
partial failure) because Team A's evidence either declined to analyze them or found the
reference system's own answer unproven: [B11](B11_EXCEPTION_FAILURE_MODEL.md).

## 15. Advancement Design

Nine advancement items (AD-01..09, the last identified independently by Team B, not present
in Team A's ADV-01..08), each with a chosen design mechanism and a measurement criterion:
[B12](B12_REFERENCE_TO_ADVANCEMENT_DESIGN.md).

## 16. Design Options / Trade-offs

Eleven significant decisions (DT-07 added at CORR-B03; DT-08/DT-09 added at CORR-B2-01..04;
DT-10 added at CORR-B3-05; DT-11 added at CORR-B4-03) formally compared across eight dimensions
each, with Team-B-only recommendations explicitly marked not-yet-approved. **Revised at
CORR-B01:** DT-02's original recommendation was withdrawn as internally contradictory (not
merely reconsidered) and replaced with a coherent option, kept visible alongside the
withdrawal. **Added at CORR-B3-05:** DT-10 compares the Round-2 posted-Fiscal-Year-Close-Entry
model against a no-posted-close derived-formula model, finding the former structurally
defective (no dating choice avoids either corrupting the closing year's own history or
re-violating the never-reset claim) rather than merely less preferred. **Added at CORR-B4-03:**
DT-11 compares three models for Fiscal-Year reporting-inclusion timing (boundary-driven,
adopted; an explicit unclosed-earnings component, rejected as unnecessary complexity; mandatory
atomic close, rejected on independent operational grounds): [B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md).

## 17. Clean-Room Provenance

Every material decision mapped to Accounting Standard / Regulatory Requirement / Industry
Principle / Cross-ERP Pattern / Team A Fact / Migration Requirement / Independent Reasoning.
Three vendor-adjacent terms individually reviewed and confirmed traceability-only.
**Critical Vendor-Derived Design Risk = 0**, re-confirmed unaffected by the CORR-B01/B02/B03
corrections, again by CORR-B2-01..05, again by CORR-B3-01..08, and again by CORR-B4-01..08
(reporting-equity mathematics is accounting/algebraic reasoning, not vendor structure — the
same evidentiary category as PR-01/PR-02, not a new category requiring re-review of B14
itself): [B14](B14_CLEAN_ROOM_PROVENANCE_MATRIX.md).

## 18. Traceability

Full chains traced end-to-end for three exemplar threads; one ID-space collision and one
rule-interaction gap found internally and resolved explicitly (not silently). **Three further,
more severe (BLOCKING) defects were subsequently found by ChatGPT's independent audit — not
by this domain's own traceability pass — and are recorded with equal transparency, including
the honest note that this domain's own review missed them (§3a); two more were found by
ChatGPT's Round 2 re-audit (§3b); two more were found by ChatGPT's Round 3 re-audit (§3c);
three more were found by ChatGPT's Round 4 re-audit (§3d), two of which were introduced by
Round 3's own fix — the pattern named at §3a is recorded as having recurred a fourth time, not
minimized:** [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §3a/§3b/§3c/§3d. Zero orphan critical
decisions, zero circular definitions, zero regulatory overreach, before and after all four
correction rounds: [B15](B15_DESIGN_TRACEABILITY_MATRIX.md).

## 19. Residual Unknowns

Team A's full 20-item residual register carries forward unchanged, incorporated by reference
([B01](B01_AUTHORIZED_INPUT_REGISTER.md) §11). This domain's design does not depend on any of
them resolving in a particular direction (see [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6 for
the two items — OQ-01, OQ-02 — explicitly checked against this design's dependencies).

## 20. Assumptions

Six Team B design assumptions requiring gate confirmation, consolidated in
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
**Round 4 likewise narrowed or resolved none of the six** — its findings are pure
reporting-equity mathematics (double-counting, boundary timing, viewpoint parameterization),
with no bearing on any of the six assumptions' subject matter (see
[CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md](CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md)
§8 and [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6's Round 4 note). The designated Retained
Earnings account (B07 §1f, B10 MG-C15) is likewise not a seventh assumption — it is a required,
unambiguous migration-configuration fact with exactly one correct answer per Company, not an
open judgment call.

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
