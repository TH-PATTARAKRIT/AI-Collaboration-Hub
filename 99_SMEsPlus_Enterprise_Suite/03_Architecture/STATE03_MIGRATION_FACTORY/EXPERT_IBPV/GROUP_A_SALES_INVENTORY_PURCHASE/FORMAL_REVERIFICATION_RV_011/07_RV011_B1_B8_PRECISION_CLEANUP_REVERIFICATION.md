> GROUP A — Sales + Inventory + Purchase Integrated Backbone | EXPERT IBPV — Formal Re-Verification RV-011

# 07 — RV-009 B1–B8 PRECISION CLEANUP RE-VERIFICATION (RV11-04)

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-011-D07`

Method: each row's RV-009-identified residual defect was reproduced from RV-009 Deliverable 11 §B (and, for B1,
Deliverables 04/05), then the current, corrected primary-source text was read directly and checked against the
specific defect — not against CORR-010's own file 32 claim of closure.

## B1 — Denied-Approval Wind-Down

**RV-009 residual**: `07`§01's canonical-state summary line omitted `Rejected`; `13` never cross-referenced
`Rejected` despite a coordination claim, and the claim named the wrong control (§03 instead of §02).

**Independent re-check**: `07_PURCHASE_CANONICAL_DESIGN.md` §01, read directly — the summary line now reads
"Canonical states: `Draft` → (`Sent`...) → [`Pending Approval`, conditional] → `Committed` → `Cancelled`;
`Pending Approval` may also resolve to `Rejected` instead of `Committed`..." — **`Rejected` is now present in the
enumeration.** The same section's coordination text now names "the Approval Control concept (`13`§02, APR-001 —
the Amount-Threshold Approval control that actually produces the `Pending Approval`/`Rejected` transition; **not**
§03's Sequential Level-Based Approval" — the citation is corrected to the control that actually gates the
transition. `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md` §02's Event Impact row, read directly, now lists
"Supply Commitment Rejected (**CORR-010 cross-reference**...)" — the missing cross-reference is present.

**Verdict: `VERIFIED` — CLOSED.**

## B2 — Retry/Idempotency Trigger Wording

**RV-009 residual**: `12`§11's idempotency invariant enumerated covered triggering actions more narrowly than its
own protected-effects list — a redelivered `Commercial Fulfillment Requested` event was not literally named.

**Independent re-check**: `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §11, read directly — the
operative invariant text now explicitly names, as trigger (b), "creates or reconciles a fulfillment/receipt
instruction in response to `Commercial Fulfillment Requested`, `Commercial Line Quantity Changed`, or `Supply
Commitment Line Quantity Changed` (named explicitly here — **CORR-010 precision fix**...)."

**Verdict: `VERIFIED` — CLOSED.**

## B3 — Downstream-Failure Compensation Citations and Non-Disappearance Guarantee

**RV-009 residual**: `08`§12 cited `[09]`§07 (nonexistent) and `[12]`§13 (wrong section) instead of `§00A`/`§13A`;
no explicit "cannot silently disappear" guarantee stated for `Handoff Unresolved`.

**Independent re-check**: `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` §12, read directly — now cites
`12`§13A explicitly ("**CORR-010 citation correction** — previously misread as plain §13...") and correctly
states the transport-semantics window is in `09`§00A ("**CORR-010 citation correction** — file `09` has no
§07"). `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §13A, read directly, now contains an explicit
"Non-disappearance guarantee (CORR-010 addition): a `Handoff Unresolved` status, once set, can be cleared only by
the convergence criterion above — no manual dismissal, auto-expiry, or archival/cleanup process may clear or hide
it."

**Verdict: `VERIFIED` — CLOSED.**

## B4 — Unqualified "Sequential"/"Ordered" Residue

**RV-009 residual**: `06`§07 and `19`'s APR-002 worked example retained unqualified "sequential" language, missed
because TEAM B's own CORR-008 keyword sweep never searched for "sequential."

**Independent re-check**: `06_SALES_CANONICAL_DESIGN.md` §07, read directly — now states "**CORR-010 wording
correction (`FV006-SOD-004`)**: 'sequential' here names the levels' numbering/labeling convention only... not an
assertion that level-to-level gating is enforced in strict order — the same qualifier already applied at every
other point of use in `13`§03/§06 and `07`§03. Formal IBPV RV-009 independently found this sentence was missed by
TEAM B's own CORR-008 keyword sweep." `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md`, read directly — the APR-002
worked example now reads "levels numbered/labeled for audit purposes only — not an enforced-sequence claim, per
the CORR-008/CORR-010 wording correction in `13`§03," with an explicit correction note appended.

Independently re-checked the three instances RV-009 D05 judged **not** requiring correction (`10`§01, `16`§03,
`20`§05 — co-located with an explicit `HOLD` cross-reference): `10`§01 still reads "Approval state (sequential
level-based)... (internal trigger logic `HOLD` — see `13`)" — unchanged, correctly left alone, consistent with
RV-009's own bar. CORR-010's file 32 additionally claims `12`§14 was checked and left unchanged under the same
bar; independently spot-checked and consistent with the pattern (not itself a point of contention, as RV-009 D05
never flagged `12`§14).

**Verdict: `VERIFIED` — CLOSED**, and — independently — the correction is scoped precisely to the two instances
RV-009 actually flagged, with no over-correction of the instances RV-009 explicitly judged acceptable.

## B5 — Self-Approval Mechanism

**RV-009 verdict**: `VERIFIED`, no residual defect; re-verification only, no change expected.

**Independent re-check**: `13`§02's Identity-Based Self-Approval Exclusion row, read directly, is unchanged in
substance from the CORR-008 text RV-009 D05 already verified (§02.3–02.4 of that deliverable). None of CORR-010's
B1/B2/B3/B4/B6/B7/B8/CORR10-01/CORR10-02 edits touches `13`§02.

**Verdict: `VERIFIED` — no change required, correctly unchanged.**

## B6 — Event Transport Semantics

**RV-009 residual**: `09`§00A's ordering clause self-contradicted for same-line/different-event-type pairs (the
exact `FV006-EVT-004` scenario); the same section falsely claimed `FV006-EVT-004`/`005` were "tracked in file
18."

**Independent re-check**: closed together with CORR10-01 — see Deliverable 04 (ordering-clause counterexample
trace) and Deliverable 06 §04 (false-claim correction), both independently re-performed above. The systemic
sync/async classification and consumer-failure rule (`09`§00A's other two dimensions), which RV-009 D06 already
found precise and testable, are independently confirmed unchanged by this correction.

**Verdict: `VERIFIED` — CLOSED** (cross-referenced to Deliverables 04, 06).

## B7 — Lot/Serial and Package Ownership Citation

**RV-009 residual**: `10`§01's Handling-Unit-historical-snapshot row cited `[04]`§09 instead of `[04]`§08 for a
"never deleted" claim.

**Independent re-check**: `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md` §01, read directly — the Handling
Unit historical-snapshot row now cites "`04`§08 — **CORR-010 citation correction**: previously misread as §09,
the plain Written-by/Read-by Summary Boundary Table, which contains no permanence statement; the correct target
is §08's General Archival/Non-Deletion Rule." Independently cross-checked against `04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md`
§08 and §09 directly: §08 is indeed the General Archival/Non-Deletion Rule (the correct target, containing the
"must never be hard-deleted" language), and §09 is indeed the plain Summary Boundary Table (no permanence
statement) — the correction targets the right section.

**Verdict: `VERIFIED` — CLOSED.**

## B8 — Shared-Master Archival Rule Labeling

**RV-009 residual**: `04`§08's archival-rule generalization extends to 10 of 13 Shared Master concepts without
per-item evidenced-vs-design-choice labeling; TEAM B's own CORR-008 re-verification question undercounted the
unevidenced set (named 5, actual 10).

**Independent re-check**: `04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md` §08, read directly — a new
"Evidenced-vs-extended labeling" paragraph independently confirmed to state the count exactly as claimed: **3**
directly-evidenced concepts (UOM, Payment Term, Currency, citing `UOM-06`/`PAY-07`/`CUR-08`), **2** differently-
evidenced concepts (Warehouse/Location, Company/Branch — immutability protection, not deletion protection, citing
`01_SHARED_MASTER_DEPENDENCY_MAP.md` §11/§12), and **8** unevidenced-extension concepts (Party, Product/Service,
Product Classification, Sales Price Rule, Vendor Price Reference, Tax Rule, Document Sequence, Cost Dimension) —
**3 + 2 + 8 = 13**, matching the file's own full concept list in §09's Summary Boundary Table, independently
counted and confirmed to total 13 rows. The paragraph explicitly states the corrected count (10 unevidenced-or-
differently-evidenced) against TEAM B's own prior undercount (5).

**Verdict: `VERIFIED` — CLOSED**, with the count independently re-derived and matching, not merely taken on the
corrected text's own word.

## Summary

| Item | Independent verdict |
|---|---|
| B1 | VERIFIED — CLOSED |
| B2 | VERIFIED — CLOSED |
| B3 | VERIFIED — CLOSED |
| B4 | VERIFIED — CLOSED, scoped correctly |
| B5 | VERIFIED — no change required, correctly unchanged |
| B6 | VERIFIED — CLOSED (cross-ref D04, D06) |
| B7 | VERIFIED — CLOSED |
| B8 | VERIFIED — CLOSED, count independently re-derived |

**8/8 independently confirmed correctly dispositioned.** Every closure was checked against the actual current
primary-source text, not against CORR-010's own closure register. No B-item edit was found to alter a
substantive design decision beyond what RV-009 itself required — consistent with RV-009 D11's own characterization
of these as "a light-touch documentation pass, not a design rework cycle."
