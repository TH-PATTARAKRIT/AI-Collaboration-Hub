> GROUP A — Sales + Inventory + Purchase Integrated Backbone | EXPERT IBPV — Formal Re-Verification RV-009
> Session: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009` | Phase 5 lens — Approval / Permission / SoD Re-Verification (Deliverable 05)
> Independent re-verification only. TEAM B's own closure register is treated as a claim to test, not as evidence.

# 05 — APPROVAL, PERMISSION & SoD RE-VERIFICATION (RV9-04, RV9-05, and the SoD-angle of RV9-01)

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009-D05`
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone
Execution Function: EXPERT IBPV — Independent Business Process & Design Verification Team
Session: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009`
Re-Verification Target: TEAM B CORR-008 corrective package — `CORR8-04`, `CORR8-05`, and the Approval-Control-coordination sub-claim of `CORR8-01`
Baseline-correction commit: `e7eeba86d2693c5e15234d73f6722a9745038853`
Closure-package commit: `359f96c0cfee2f74955fe7e8f1d0110ec21a0a45`
Control Level: `/L999.999`
Boss: Sole Final Approver
Charter: `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/EXPERT_IBPV_CHARTER.md`
Status vocabulary used below: `VERIFIED`, `VERIFIED WITH CONDITIONS`, `GAP FOUND`, `CONFLICT FOUND`, `EVIDENCE MISSING`, `REWORK REQUIRED`, `NOT READY FOR DEVELOPMENT`, `READY FOR BOSS DECISION` — no other term is used.

## 00 — Scope, Independence Statement, and Method

This deliverable independently re-verifies:

- **RV9-04 / CORR8-04** — the "Sequential"/"ordered" wording correction (`FV006-SOD-004`, originally `CONFLICT FOUND`, Major).
- **RV9-05 / CORR8-05** — the identity-based self-approval exclusion addition (`FV006-SOD-001`, originally `GAP FOUND`, Major).
- The Approval-Control-coordination sub-claim of **RV9-01 / CORR8-01** — whether `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md` actually and coherently references the new `Rejected` state CORR8-01 introduced elsewhere. (The state/event/E2E mechanics of RV9-01 itself are re-verified in Deliverable 04; this section covers only the Approval-Control coordination angle, which belongs on the SoD side of the file split.)

`22_TEAM_B_CORR008_FINDING_CLOSURE_REGISTER.md`'s own conclusions ("`CLOSED BY TEAM B CORRECTION`") are treated throughout as claims to test, not as evidence. Every verdict below is derived from independently reading the corrected artifacts themselves: `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md` (full), `07_PURCHASE_CANONICAL_DESIGN.md` §01/§03, `06_SALES_CANONICAL_DESIGN.md` §07, `09_CANONICAL_BUSINESS_EVENT_CATALOG.md` §02, `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md` §01, `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §14, `16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md` §03, `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md`, `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md` §05, `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` §06, and TEAM B's own evidence artifacts `22`, `24`, `26` (read as claims, then checked against the artifacts they cite). A repository-wide `grep -rniH` sweep for `"sequential"` and `"ordered"` was run independently across every `.md` file under `GROUP_A_SALES_INVENTORY_PURCHASE/`, not limited to the two artifacts TEAM B names as corrected — see §01.3 below for why this matters.

## 01 — RV9-04 — Sequential-Approval Wording (`CORR8-04` / `FV006-SOD-004`)

### 01.1 Original finding reproduced

`FV006-SOD-004` (`FV_006/07_CONTROL_APPROVAL_PERMISSION_SOD_VERIFICATION.md` §03, `CONFLICT FOUND`, Major): the pre-correction artifact named the control "Sequential Level-Based Approval" and stated "N **ordered** approval levels" in the same document whose §00 explicitly held the exact level-to-level transition/gating rule as unverified (`HOLD`). The finding's required-owner guidance was explicit: "state explicitly, **at the point** the label and 'ordered' phrase are used, that 'ordered' denotes level numbering/labeling for audit purposes and does NOT assert enforced sequential gating." The finding's own re-verification question (repeated verbatim in `22` CORR8-04) asks whether **every** instance of "sequential"/"ordered" in the corrected package now carries that qualifier, with **no remaining unqualified instance** that could mislead a reader.

### 01.2 Corrected artifacts independently inspected — the two TEAM B names

- `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md` §03 — the reading-note blockquote ("Read the title and this row's 'sequential' as a name, not a settled enforcement claim") and the "TEAM B Independent Decision" row, which states plainly: "the levels are numbered/labeled ... for audit and display purposes only — this numbering is a data-shape/labeling convention, not an assertion that levels are enforced in strict sequential gating order."
- `13` §06 — the Summary Table row is split into two rows: "generic shape... 'sequential' = numbering/labeling only" (`HOLD? No`) vs. "internal workflow / level-to-level gating logic" (`HOLD? Yes`).
- `07_PURCHASE_CANONICAL_DESIGN.md` §03 — "N numbered levels — 'numbered' for audit/display purposes only, not an enforced-sequence claim, per the CORR-008 wording clarification in `13` §03."

**Result on these two artifacts: `VERIFIED`.** The wording is precise, is stated at the point of first use (not buried), matches the finding's own required-owner guidance exactly, and does not merge the two genuinely distinct claims (numbering vs. enforcement). `13` §00 and §03's `Evidence Status` field ("internal workflow logic `EVIDENCE_MISSING`") is unchanged and still correctly holds the enforcement question open — the corrected wording does not silently resolve it.

### 01.3 Independent package-wide sweep — beyond the two named artifacts

The re-verification question explicitly asks about "every instance ... across the corrected GROUP A package," not just the two artifacts TEAM B edited. An independent `grep -rniH "sequential"` and `grep -rniH "\bordered\b\|\bordering\b"` across all `.md` files in `GROUP_A_SALES_INVENTORY_PURCHASE/` (outside `CORRECTIVE_CORR_008/`, which is evidence commentary, not primary design) surfaced two additional live instances that were **not** touched by CORR-008 and do **not** carry the explicit numbering-only qualifier:

- `06_SALES_CANONICAL_DESIGN.md` §07: *"A real, historically-used, sequential per-level approval control exists on Sales commitments in the evidence (confirmed installed and used, though internal workflow logic is a Controlled Carry-Forward Unknown)."*
- `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md` (APR-002 worked example): *"a real, historically-used, sequential multi-level approval control exists on at least one document type, with unverifiable internal logic."*

Neither sentence states that "sequential" denotes numbering/labeling only — both simply juxtapose "sequential" with a general "internal logic is unverified" caveat, which is structurally the **same pattern** the original `FV006-SOD-004` finding held insufficient when it appeared in pre-correction `13` (juxtaposition without an explicit disclaimer was exactly what the finding objected to). The risk of a reader being misled is lower here than in the pre-correction `13` (both sentences do flag the internal logic as unverified in the same breath), but it is not zero, and it is not the fix TEAM B's own closure claims to have applied "at every point of use" (`22` CORR8-04 corrective-reasoning paragraph).

Two further instances were checked and judged **not** to require correction, because each already co-locates the term with an explicit `HOLD` cross-reference in the same clause:
- `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md` §01: "Approval state (sequential level-based) ... (internal trigger logic `HOLD` — see `13`)."
- `16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md` §03: "Whether staff experience/expect the sequential level-based approval workflow as a two-person, sequential process — directly relevant to `13` APR-002's `HOLD`."
- `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md` §05 item 1: "the sequential level-based Approval Control's internal workflow logic is designed only at the vendor-neutral shape level; its exact trigger/transition rules remain `HOLD`/`EVIDENCE REQUIRED`."

**Why the two flagged instances were missed**: TEAM B's own cross-file consistency sweep (`24_TEAM_B_CORR008_CROSS_FILE_CONSISTENCY_REPORT.md` §1, pass 2) states its keyword list explicitly: `"ordered"`, `"Pending Approval"`, `"Tenant"`, `"self-approval"`, `"idempoten"`, `"Traceability Unit"`/`"lot/serial"`/`"Handling Unit"`. **`"sequential"` is not in that list**, despite being the word in the finding's own title and in the control's own name ("Sequential Level-Based Approval"). `24` §4 separately lists `06_SALES_CANONICAL_DESIGN.md` as "intentionally unchanged," but the stated reason ("No CORR8 finding touches Sales-specific design; CORR8-01's denial path is Supply-Commitment-only") addresses CORR8-01, not CORR8-04's wording concern — file 06's own "sequential" sentence at §07 was never evaluated against CORR8-04's standard at all.

### 01.4 EVIDENCE MISSING framing check

Independently confirmed: `13` §00 and §03 both continue to state the internal level-to-level enforcement logic as `EVIDENCE_MISSING` / `HOLD / EVIDENCE REQUIRED FOR THIS DECISION POINT`, consistently, with no corrected artifact anywhere claiming this is settled. The corrected package does not silently upgrade the enforcement question's status. **Verified.**

### 01.5 Verdict — RV9-04

**`VERIFIED WITH CONDITIONS`.**

- The two artifacts TEAM B specifically corrected (`13` §03/§06, `07` §03) are precisely and correctly fixed, exactly per the finding's own required-owner guidance.
- Condition: TEAM B's closure claim of package-wide completeness is not fully accurate — `06_SALES_CANONICAL_DESIGN.md` §07 and `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md` retain unqualified "sequential" language that TEAM B's own keyword sweep (`24` §1) could not have caught, because "sequential" was never in its search list. Practical mislead-risk at these two spots is low (both sit next to language flagging the internal logic as unverified) but is not the explicit numbering-only disclaimer the finding required "at the point" of use.
- Gate impact: does **not** reopen a Critical/blocking gap — the enforcement-logic `HOLD` is correctly preserved everywhere. This is a non-blocking documentation-completeness condition: add the same reading-note treatment to `06` §07 and `19`'s APR-002 entry before this finding is certified fully, package-wide closed.
- Residual unknown: none new. The underlying level-to-level gating logic remains the pre-existing, correctly-labeled `HOLD` from Boss Gate §4.1.

## 02 — RV9-05 — Self-Approval Prevention (`CORR8-05` / `FV006-SOD-001`)

### 02.1 Original finding reproduced

`FV006-SOD-001` (`FV_006/07` §02, `GAP FOUND`, Major): `13`'s pre-correction Business Problem/Need for APR-001 stated "prevent self-approval," but the specified mechanism and its cited evidence (`04` §02 PO-06/07/08) were both **role-based** (does the actor hold the authority role?), not **identity-based** (is the approver the same person as the creator?). A role-holding creator was not excluded from approving their own commitment — a real gap between stated purpose and actual mechanism, not a hypothetical.

### 02.2 Corrected artifact independently inspected

`13` §02 (APR-001) — read in full: the Business Problem/Need row (now stating both (a) role-based and (b) identity-based requirements explicitly), the TEAM B Independent Decision row (adds the concrete enforcement: "if they match, the approval attempt is refused with an explicit reason ... regardless of whether the matching actor also holds the approval-authority role"), the new "Identity-Based Self-Approval Exclusion" row, the Approved Evidence Input / Evidence Status rows, and §05 (cross-reference) and §06 (Summary Table row).

### 02.3 Independent verification method and result

- **Attribution check** (the task's specific concern — is this falsely attributed to legacy behavior?): §02's new row states in full: *"TEAM B does not claim this was how any legacy module's internal logic behaved (that internal logic remains outside evidence, per §00); this is a target business-control requirement stated independently of the unverified legacy internals."* This is checked directly against `13` §00's evidence-boundary statement ("exact permission model; exact SoD behavior ... remain unverified and are not designed here") — the two are consistent; no attribution violation found. `22`'s CORR8-05 "Governing evidence/baseline" line matches this framing exactly: *"the identity-based half is not evidenced and is a new TEAM B target requirement, labeled as such."* No over-claim found in either artifact.
- **Evidentiary honesty**: the Approved Evidence Input row is explicit that only the role-based half is evidenced ("`04` §02 PO-06/07/08, test-confirmed") and flags the identity-based half separately ("(b) is a TEAM B target-design addition, not evidenced"). This is the correct evidentiary posture — stronger than merely not being wrong, it affirmatively separates the two evidence tiers in the same row a careless reader might otherwise conflate.
- **Mechanism completeness**: unlike a bare policy statement, the Decision row specifies an actual enforcement behavior (refusal with explicit reason, evaluated independently of role) — this closes the finding's own "gap between stated purpose and actual mechanism" concretely, not just rhetorically.
- **Composition with §05**: §05's general SoD data-shape requirement (creator/approver must be *distinguishable*) is not duplicated or contradicted by §02's new requirement (creator/approver must be *unequal*, enforced) — the cross-reference in §05 explicitly names this as composition ("extends... by additionally requiring that distinguishability be *enforced*"). No double-counting or conflation found.
- **State/event impact check**: `22` claims "none" — no new state or event. Independently confirmed against `09_CANONICAL_BUSINESS_EVENT_CATALOG.md` §02: the `Supply Commitment Approved` row is unchanged and does not need to be, since the identity check gates the approval *action* before any event fires; a matched-identity attempt produces a refusal, not a state transition. This is architecturally consistent with how the pre-existing role-based refusal is already handled (a "silent no-op... surface an explicit, informative rejection instead," `13` §02 Exception/Correction Impact row, unchanged and correctly reused for the new case per the Decision row's own text).

### 02.4 Verdict — RV9-05

**`VERIFIED`.** The addition fully and honestly resolves `FV006-SOD-001`: APR-001's stated purpose ("prevent self-approval") is now backed by two independently-evaluable, jointly-necessary mechanisms (role check and identity check), the identity check is correctly and consistently labeled everywhere it appears as a TEAM B target-design decision rather than a claim about unverified legacy behavior, and no state/event catalog change was needed or silently omitted.

- Residual unknown: none material to this finding's own scope.
- Gate impact: none — a control-strength addition that closes a Major gap without depending on the still-open `13` §03 internal-logic `HOLD`.

## 03 — RV9-01 Intersection Check: Does `13` Coherently Reference the New `Rejected` State?

### 03.1 Claim being tested

`22`'s CORR8-01 entry states the new `Rejected` state's owner is "Purchase (the Supply Commitment document type), **coordinated with the Approval Control concept (`13` §03)** that raises the rejection."

### 03.2 Independent verification method

Full read of `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md` (already performed for §01–§02 above), plus a targeted `grep -n "Reject"` against the file.

### 03.3 Result

The grep returns exactly two matches, both inside `13` §03 (APR-002, Sequential Level-Based Approval — a different control from the one that actually produces `Pending Approval`/`Rejected` on a Supply Commitment): "Approval Level Rejected" (a new *per-level* rejection event name, for the multi-level control) and "a rejected document" (the resubmission-restart `HOLD`). **Neither match, and no other text anywhere in `13`, refers to the Supply Commitment's own `Rejected` state or to the `Supply Commitment Rejected` event CORR8-01 introduced.** In particular, `13` §02 (APR-001, Amount-Threshold Approval — the control that actually gates `Pending Approval` and is therefore the actual origin of CORR8-01's denial path) lists its Event Impact as only *"Supply Commitment Confirmed (may branch); Supply Commitment Approved"* — unchanged, with no `Supply Commitment Rejected` addition.

This is independently corroborated by `24_TEAM_B_CORR008_CROSS_FILE_CONSISTENCY_REPORT.md` §3's own "Files Changed" table: row 9 lists `13`'s CORR-008 changes as "CORR8-04 (primary), CORR8-05 (primary)" only — **CORR8-01 is not listed as touching file 13 at all**, confirming independently (from TEAM B's own accounting, not just the absence of the word) that `13` was never edited as part of CORR8-01's correction.

### 03.4 Verdict — RV9-01 SoD-angle intersection

**`GAP FOUND`** (documentation-coherence, Minor-to-Moderate — not a control-integrity gap). `22`'s "coordinated with the Approval Control concept (`13` §03)" phrasing describes a coordination that does not exist in the artifact it names. The substantive fix (state, event, cascade, audit trail — see Deliverable 04) is independently sound on its own terms and does not structurally depend on `13` referencing it, so this does **not** reopen the original Critical `FV006-STE-004`/`FV006-EVT-003` gap. It should nonetheless be corrected: a one-line cross-reference added to `13` §02's Event Impact row (mirroring the pattern already used for the CORR8-05 cross-reference at `13` §05) would make the artifact match the closure register's own description of it.

- Gate impact: non-blocking. A documentation-completeness correction, not a rework trigger.

## 04 — Consolidated Verdict Table

| Finding | Verdict | Residual / Condition | Gate Impact |
|---|---|---|---|
| RV9-04 (`CORR8-04`) | `VERIFIED WITH CONDITIONS` | `06` §07 and `19` retain unqualified "sequential" wording; TEAM B's own keyword sweep (`24` §1) omitted "sequential" | Non-blocking |
| RV9-05 (`CORR8-05`) | `VERIFIED` | None material | None |
| RV9-01 SoD-angle (Approval-Control coordination) | `GAP FOUND` | `13` never references the new `Rejected` state anywhere, contrary to `22`'s "coordinated with `13` §03" claim | Non-blocking |

## 05 — Overall Gate Impact for This Deliverable

None of the three items re-verified here reopens a Critical or blocking gap from Formal IBPV FV-006. Two non-blocking documentation-completeness conditions are identified and should be satisfied before CORR8-01 and CORR8-04 are certified as fully, package-wide closed: (1) extend the CORR8-04 reading-note wording to `06` §07 and `19`'s APR-002 worked example; (2) add the missing cross-reference from `13` §02 to the new `Supply Commitment Rejected` event. Neither condition changes this deliverable's status from `READY FOR BOSS DECISION` on the substance of RV9-04/RV9-05/RV9-01's SoD angle — see the consolidated RV-009 report for the package-wide recommendation.
