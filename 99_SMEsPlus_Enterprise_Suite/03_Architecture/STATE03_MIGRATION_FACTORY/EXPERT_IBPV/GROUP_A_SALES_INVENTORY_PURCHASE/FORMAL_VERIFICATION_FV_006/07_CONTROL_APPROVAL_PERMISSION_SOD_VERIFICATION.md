> GROUP A — Sales + Inventory + Purchase Integrated Backbone | EXPERT IBPV — Formal Independent Verification
> Session: SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006 | Phase 6 — Approval / Permission / SoD Verification (Deliverable 07)
> Independent verification only. No redesign. No business-policy selection. No inference of missing legacy workflow.

# 07 — CONTROL, APPROVAL, PERMISSION & SEPARATION-OF-DUTIES (SoD) VERIFICATION

## 00 — Scope and Method

This deliverable independently verifies TEAM B's approval/control/SoD design — `APR-001` (Amount-Threshold
Approval), `APR-002` (Sequential Level-Based Approval), and `APR-003` (Sales Confirmation Gate) — against the
Boss-approved evidence baseline. It does not redesign, repair, or replace any TEAM B artifact. Findings use only
the charter vocabulary: `VERIFIED`, `VERIFIED WITH CONDITIONS`, `GAP FOUND`, `CONFLICT FOUND`, `EVIDENCE MISSING`,
`REWORK REQUIRED`, `NOT READY FOR DEVELOPMENT`, `READY FOR BOSS DECISION`.

**Artifacts reviewed:**

- TEAM B primary: `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md` (§00–§06)
- TEAM B: `17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md` (§03, §04)
- TEAM B: `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md` (§05)
- TEAM A: `16_FIT_GAP_CANDIDATE_PACK.md` (§03, §04)
- TEAM A: `13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md` (§01 item 10, §02 item 5)
- Boss Evidence Gate: `GROUP_A_BOSS_EVIDENCE_GATE_APPROVAL_2026-08-31.md` (§4 item 1)
- Readiness record: `00_PRE_PROMPT_READINESS_SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006.md` (§3.3, §9.2)

**Scope limitation, stated explicitly rather than silently assumed:** TEAM B's `13_...md` cites
`04_SALES_CANONICAL_DESIGN.md`, `07_PURCHASE_CANONICAL_DESIGN.md`, and `09_CANONICAL_BUSINESS_EVENT_CATALOG.md` as
supporting cross-references (Approved Evidence Input / Event Impact fields). Those three files were not included in
the source set made available for this verification pass. Where a finding below depends on information that might
be resolved in one of those files, this is stated as a review-scope limitation, not asserted as a confirmed defect
in the TEAM B package as a whole. SHA-256 manifest reproduction and full-package completeness are handled in a
separate deliverable (Phase 1) and are not re-performed here.

## 01 — Verification Matrix

| Control | Creator ≠ Approver / No Self-Approval Enforced | Rejection / Resubmission / Cancel Interaction Defined | Company/Branch Scoping Defined | Auditable (Who/What/When) |
|---|---|---|---|---|
| APR-001 (Amount-Threshold) | PARTIAL — role-gate evidenced; identity-based self-approval exclusion not stated (Finding FV006-SOD-001) | GAP — unauthorized-attempt messaging defined; authorized-approver reject/resubmit path not defined (Finding FV006-SOD-002) | VERIFIED — §02 "company-scoped, currency-converted per company" | GAP — no explicit approver-identity/timestamp statement in this artifact (Finding FV006-SOD-003) |
| APR-002 (Sequential Level-Based) | VERIFIED (data-shape only) — §05 explicit distinguishability requirement, enforcement algorithm correctly left open | PARTIAL — rejection + mandatory reason defined; resubmission-vs-restart explicitly `HOLD` (correctly carried forward) | VERIFIED — §03 "resolve within the acting company/branch scope" | VERIFIED (shape only) — §03 "approve/reject event with timestamp" and rejection reason |
| APR-003 (Sales Confirmation Gate) | N/A — policy gate, not a person-approval workflow | PARTIAL — refusal-with-reason defined; no explicit audit-log statement for blocked attempts (Finding FV006-SOD-008) | VERIFIED — §04 "Policy is company-configurable" | GAP — no explicit statement that policy-block events are logged with actor/timestamp (Finding FV006-SOD-008) |

## 02 — APR-001 (Amount-Threshold Approval) — Detailed Verification

**FV006-SOD-001 — Business problem framed as "self-approval prevention" but the specified mechanism is role-based, not identity-based**

- Verification Area: Approval Control — SoD sufficiency
- TEAM B Artifact(s): `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md` §02 (Business Problem/Need; TEAM B Independent Decision)
- Approved Evidence/Baseline: TEAM A `13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md` §01 item 10 — "a non-manager cannot self-approve above the configured amount" (Purchase PO-06/08, ORM method guard, test-confirmed)
- Finding Status: `GAP FOUND`
- Severity: Major
- Why it matters: §02's stated Business Problem/Need is "Prevent self-approval of a supply commitment above a value threshold without oversight." The mechanism actually specified — "a configurable threshold amount ... and an approval-authority role; a commitment above threshold and without an authorized actor transitions to Pending Approval" — and the cited evidence itself ("a non-manager cannot self-approve") are both **role-based** gates (does the acting user hold the authority role?), not **identity-based** self-approval prevention (is the acting approver the same person who created/requested the commitment?). As written, a role-holder (e.g., a manager) who personally created the above-threshold commitment is not stated to be excluded from also approving it. This is a real gap between the stated business intent and the specified/evidenced control, not a hypothetical edge case — it is exactly the self-approval scenario the requirement claims to prevent.
- Cross-domain impact: None beyond Purchase; this is a Purchase-owned control per §02.
- Gate impact: Does not block the overall Purchase design, but the amount-threshold control cannot be certified as satisfying its own stated purpose ("prevent self-approval") until this is resolved.
- Required owner: TEAM B (clarify/state the identity-based rule explicitly, without inventing unverified legacy internals) and/or Boss/business (decide whether role-based gating alone is the accepted control strength, or whether identity exclusion of the creator is also required — a control-risk-appetite decision, not an evidence question).
- Blocking Development: No, for the threshold/state-machine shape itself. Yes, for certifying the control as meeting its stated "prevent self-approval" purpose.
- Boss decision required: Yes — this is a control-strength policy choice (role-based sufficiency vs. mandatory creator exclusion), not resolvable from evidence alone.

**FV006-SOD-002 — Rejection / resubmission path for an authorized approver is undefined**

- Verification Area: Approval Control — exception handling
- TEAM B Artifact(s): `13_...md` §02 (Exception/Correction Impact row)
- Approved Evidence/Baseline: TEAM A `16_FIT_GAP_CANDIDATE_PACK.md` §01 item 2 (amount-threshold gate observation); no evidence cited on a reject action within this control
- Finding Status: `GAP FOUND`
- Severity: Moderate
- Why it matters: §02 defines behavior only for an *unauthorized* approval attempt (must surface an explicit rejection message instead of a silent no-op). It does not define what happens when an *authorized* approver reviews a Pending Approval commitment and declines it: is there a reject action, a reason requirement, and does the document return to Draft, remain Pending, or require cancellation and re-creation? Compare `APR-002` §03, which explicitly makes rejection "a first-class event with a mandatory reason" — APR-001 has no equivalent statement.
- Cross-domain impact: None identified beyond Purchase.
- Gate impact: A material control-behavior gap for a real, evidenced financial gate (Purchase order value threshold).
- Required owner: TEAM B — add an explicit statement of the authorized-approver reject/resubmit/cancel interaction (or an explicit, correctly-labeled `HOLD` if this genuinely cannot be resolved from evidence).
- Blocking Development: Yes, for implementation of the approver-decision path specifically; no, for the threshold/Pending-Approval state introduction itself.
- Boss decision required: No, unless TEAM B/evidence cannot resolve it, in which case it becomes the same class of decision as the APR-002 resubmission Unknown.

**FV006-SOD-003 — Auditability not explicitly stated for APR-001 within the reviewed artifact**

- Verification Area: Approval Control — auditability
- TEAM B Artifact(s): `13_...md` §02 (Event Impact row: "Supply Commitment Confirmed (may branch); Supply Commitment Approved")
- Approved Evidence/Baseline: N/A — documentation-completeness observation, not an evidence conflict
- Finding Status: `GAP FOUND` (scope-limited — see §00 above)
- Severity: Minor
- Why it matters: APR-002 explicitly states its approval event carries "a timestamp" and "a rejection reason." APR-001's row lists only event names ("Supply Commitment Approved") without an explicit statement that approver identity and timestamp are captured. This may already be resolved in `09_CANONICAL_BUSINESS_EVENT_CATALOG.md`, which was not part of this review's source set — this finding records an unconfirmed point, not a proven absence.
- Cross-domain impact: None.
- Gate impact: Low on its own; relevant only in combination with FV006-SOD-001 (a role-based, non-identity-checked approval is harder to govern after the fact if the approval event itself does not clearly record who approved and when).
- Required owner: TEAM B / cross-reference confirmation against file 09.
- Blocking Development: No.
- Boss decision required: No.

## 03 — APR-002 (Sequential Level-Based Approval) — Detailed Verification

This is the priority review item identified by both TEAM B itself (`20_...md` §05 item 1: "the single highest-priority review item") and the Formal IBPV Pre-Prompt Readiness Record (`00_...md` §3.3 item 1, §9.2). The central question specified for this verification: does the "sequential level-based" shape stand on its own as a justified target business requirement using only evidence that does not require knowing the missing legacy modules' internals, or does it secretly depend on that missing internal logic?

**Finding: the answer is mixed, and TEAM B's own artifact draws the line correctly in one place (§00) but states the shape imprecisely in another place (§03/§06), creating an internal wording inconsistency that must be resolved.**

### 03.1 — What is legitimately evidence-supported independent of the missing legacy internals — classification (a)

- The *existence* of the three modules, their installation, and real historical usage is evidenced independent of source code: TEAM A `16_FIT_GAP_CANDIDATE_PACK.md` §03 item 13 cites row-level counts (1,945 approved / 96 rejected of 2,199 records on Purchase Request) and schema field evidence (`level1_approved_by` populated on 0 of 27,874 Purchase Order rows). These are dump/data-forensics facts, not inferences from Python source.
- The *generic business need* — "multi-person, sequential, auditable sign-off with a recorded reason on rejection" (`13_...md` §03, Business Problem/Need) — is therefore justifiable from usage-volume evidence and schema field naming (multiple `levelN_approved_by`-style fields imply an enumerated set of approval slots) without needing the modules' internal trigger/transition code.
- **Classification: (a) — justified as a target business requirement using evidence that does not require the missing legacy internals.** Finding Status: `VERIFIED` for this narrow claim (multi-level, auditable, reason-on-reject control exists as a real requirement).

### 03.2 — What is correctly held open, not invented — classification matching the carry-forward control

- `13_...md` §00 explicitly lists as unverified and NOT designed: "exact Level 1 → Level 2 transition; exact reject transition; exact permission model; exact SoD behavior; ... exact cancel/reset interaction with an in-progress approval." §03 repeats this: "Internal trigger conditions, exact level-to-level transition rules, and exact permission checks are not designed — `HOLD / EVIDENCE REQUIRED FOR THIS DECISION POINT`." This matches the Boss Evidence Gate carry-forward control (`GROUP_A_BOSS_EVIDENCE_GATE_APPROVAL_2026-08-31.md` §4 item 1) precisely, and correctly.
- Whether a rejected document can be resubmitted through the same levels or must restart is also explicitly `HOLD` (§03, Exception/Correction Impact row).
- **Finding Status for this portion: `EVIDENCE MISSING` — correctly classified by TEAM B, not silently invented, and appropriately carried forward.** This is not a new finding against TEAM B; it is IBPV's independent confirmation that the HOLD was applied honestly rather than glossed over.

**FV006-SOD-004 — "Sequential" / "ordered" framing in §03 and §06 is not rigorously scoped to exclude the transition-gating behavior that §00 explicitly holds open**

- Verification Area: Approval Control — internal consistency of the requirement statement
- TEAM B Artifact(s): `13_...md` §00 ("exact Level 1 → Level 2 transition" listed as not designed) vs. §03 (Decision ID `APR-002` titled "Sequential Level-Based Approval"; TEAM B Independent Decision states "N **ordered** approval levels") vs. §06 (summary table row "Sequential level-based approval (generic shape) ... HOLD? No (shape only)")
- Approved Evidence/Baseline: Boss Evidence Gate carry-forward control item 1 (internal workflow/transition/permission logic of the three modules is explicitly not to be invented)
- Finding Status: `CONFLICT FOUND`
- Severity: Major
- Why it matters: The word "Sequential" in the Decision's own name, and the phrase "N ordered approval levels" in its description, assert an ordering property for the approval-levels concept. §00 and §03's own `HOLD` clause state that the *exact Level 1 → Level 2 transition* — i.e., whether the levels are enforced in strict gated order (Level 2 cannot act before Level 1 completes) — is explicitly not designed and evidence-missing. If "ordered" in §03/§06 is read as asserting that levels are traversed in enforced sequence, it directly contradicts the artifact's own §00 disclaimer. If "ordered" is intended only as a numbering/labeling convention (Level 1, Level 2, ... for audit/display, with no claim about enforcement order), then it does not conflict with §00 — but the artifact does not state this distinction anywhere. As written, a reader relying on §06's "HOLD? No (shape only)" row — without also reading §00's fine print — could reasonably conclude the sequencing/gating behavior is a settled requirement, when TEAM B's own artifact says the opposite. This is precisely the risk the Formal IBPV Pre-Prompt Readiness Record (`00_...md` §9.2) was raised to catch: "If a material target rule cannot be justified without the missing legacy workflow, classify that point `EVIDENCE MISSING`."
- Cross-domain impact: The shared Approval Control concept is designed for reuse across Sales, Purchase, and Internal Demand Request (`13_...md` §03, Cross-Domain Dependency row) — an unresolved "sequential" ambiguity here would propagate identically into all three document types.
- Gate impact: Blocks unambiguous sign-off of APR-002's "shape" claim as fully separated from the unverified legacy workflow; the shape and the transition-gating question must be visibly distinguished, not merely implied by a HOLD buried in §00.
- Required owner: TEAM B — a wording clarification only (state explicitly, at the point the label and "ordered" phrase are used, that "ordered" denotes level numbering/labeling for audit purposes and does NOT assert enforced sequential gating, which remains a separate, still-open `HOLD` item). This is a precision correction to the existing document, not a redesign of the control.
- Blocking Development: Yes, specifically for any implementation of level-to-level gating logic — Team C must not infer or default to strict sequential enforcement from this artifact as currently worded. Not blocking for the data-shape elements (level records, approver assignment, approve/reject event, reason field).
- Boss decision required: Yes — ultimately either (i) legacy source is acquired and the actual transition rule is confirmed, or (ii) Boss/business makes a fresh policy decision on whether SMEsPlus's target system should enforce strict level-to-level gating, independent of legacy behavior. IBPV does not choose between these paths.

**FV006-SOD-005 — Cross-document generalization (one shared Approval Control for Sales, Purchase, and Internal Demand Request) is a correctly-labeled new TEAM B decision, but rests on asymmetric evidence strength across the three document types**

- Verification Area: Approval Control — scope generalization
- TEAM B Artifact(s): `13_...md` §03 (Cross-Domain Dependency: "usable by Sales, Purchase, and Internal Demand Request without being owned by any single one of them"); `17_...md` §03 item 13 ("TEAM B agrees with the mixed classification but designs one shared, vendor-neutral Approval Control concept usable by all three document types ... a generalization Team A's evidence-only mandate did not attempt")
- Approved Evidence/Baseline: TEAM A `16_FIT_GAP_CANDIDATE_PACK.md` §03 item 13 — usage is heaviest and clearly completed on Purchase Request (1,945/96/2,199); "partial usage (approver-assignment only)" on Purchase Order (`level1_approved_by` populated on 0 of 27,874 rows — the approval-recording half appears never to have been completed in practice); Sale Order has only 2 historical records ("sample too small to classify with confidence")
- Finding Status: `VERIFIED WITH CONDITIONS`
- Severity: Moderate
- Why it matters: `17_...md` §00 and §03 are explicit that this is TEAM B's own reasoned extension, not an inherited Team A answer — this satisfies classification **(c): an explicit new TEAM B design decision, correctly labeled as such**, which is acceptable practice per the governing prompt. However, `13_...md` does not carry forward, at the point the shared concept is defined, the specific evidence-strength imbalance already documented by Team A: strong/complete evidence (Purchase Request), assignment-only/possibly-never-completed evidence (Purchase Order), and statistically insignificant evidence (Sale Order). Presenting the three as one uniform concept without restating this imbalance risks a future reader treating Sale Order's or Purchase Order's fit with the shared concept as equally well-evidenced as Purchase Request's.
- Cross-domain impact: Directly affects Sales, Purchase, and any future Internal Demand Request implementation equally, since all three would inherit the same generic shape regardless of how differently each was actually evidenced.
- Gate impact: Does not block the shape's Development readiness, but the condition below should be satisfied before this decision is treated as equally strong across all three document types.
- Required owner: TEAM B — add an explicit note, where the shared concept is defined, restating the asymmetric evidence strength across the three document types (a citation-level clarification, not a scope change).
- Blocking Development: No.
- Boss decision required: No, unless the evidence-strength imbalance is judged material enough to warrant a differentiated rollout (e.g., enabling the control by default for Purchase Request but not for Sale Order) — that judgment belongs to Boss/business, not to TEAM B or IBPV.

**FV006-SOD-006 — APR-002 SoD data-shape requirement correctly scoped as data-shape-only**

- Verification Area: Separation of Duties
- TEAM B Artifact(s): `13_...md` §05 ("the actor who creates or requests a commitment/request must be distinguishable, in the data model, from the actor(s) who approve it at each level ... TEAM B does not specify the enforcement algorithm itself, only that the data shape must support it")
- Approved Evidence/Baseline: TEAM A `13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md` (both real approval mechanisms in evidence separate requester/approver roles, per §05's own rationale)
- Finding Status: `VERIFIED`
- Severity: N/A (positive finding)
- Why it matters: This is the correct way to state a minimal, evidence-supportable SoD requirement without overreaching into an enforcement algorithm that is not evidenced. It is honestly scoped, unlike APR-001's Business Problem/Need statement (FV006-SOD-001), which asserts a stronger outcome ("prevent self-approval") than its own mechanism guarantees. IBPV recommends TEAM B apply §05's more careful framing pattern to APR-001's Business Problem/Need statement as well (a wording-consistency observation, not a new requirement).
- Cross-domain impact: Applies uniformly to whichever document type configures Approval Control.
- Gate impact: None — this requirement is Development-ready as a schema-level obligation (record a distinct approver identity per level, distinct from the requester identity).
- Required owner: N/A.
- Blocking Development: No.
- Boss decision required: No.

## 04 — APR-003 (Sales Confirmation Gate) — Detailed Verification

**FV006-SOD-007 — Default Sales Confirmation Gate policy correctly left open as a Boss/business decision, not silently defaulted**

- Verification Area: Confirmation Gate Policy — business-policy deferral
- TEAM B Artifact(s): `13_...md` §04 ("TEAM B does not fix a default"; Unknown/Assumption: "Which default (if any) SMEsPlus should ship with — explicitly left to Boss/business"; Carry-Forward: "Yes — recorded in [17] as requiring Boss/business input before finalization")
- Approved Evidence/Baseline: TEAM A `16_FIT_GAP_CANDIDATE_PACK.md` §04 item 14 (UNKNOWN); TEAM A `13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md` §02 item 5 (confirmed absence of a hard stock/credit gate in the reference system — advisory-only, test-confirmed)
- Cross-check: `17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md` §04 item 14 ("TEAM B resolves the shape of the decision (must be configurable) but explicitly defers the default value to Boss/business — a partial resolution, not a full one") and `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md` §05 item 2 (lists the Sales Confirmation Gate Policy default among three business-policy decisions TEAM B explicitly did not default, and recommends Formal IBPV confirm these are surfaced to Boss)
- Finding Status: `VERIFIED WITH CONDITIONS`
- Severity: Moderate
- Why it matters: This is the correct disposition. TEAM B did not silently inherit the reference system's advisory-only behavior as SMEsPlus's default, and it did not invent a hard-gate default on its own initiative either — both would have violated governing-prompt §13.1 as TEAM B itself notes. It instead designed the *shape* (an independently-configurable policy per gate type — credit exposure, inventory availability — each settable to block / warn-and-allow / allow-silently) and explicitly deferred the *default value* to Boss/business, consistently across three independent artifacts (`13` §04, `17` §04 item 14, `20` §05 item 2). No silent default was found anywhere in the reviewed set. IBPV does not select the default value itself, consistent with scope.
- Cross-domain impact: Depends on Inventory (Available/Forecasted read) and Shared Master (Party credit exposure read), per `13_...md` §04 Cross-Domain Dependency row — both are read-only dependencies at the semantic level, not a redesign of those domains.
- Gate impact: The configurable-policy *mechanism* is Development-ready. The control cannot be considered functionally complete, tested, or deployed until Boss/business selects a default (or explicitly rules that no system-wide default will be set and each company/branch must configure it before go-live).
- Required owner: Boss/business (policy default selection) — not TEAM B, not IBPV.
- Blocking Development: No, for building the configurable-policy mechanism itself. Yes, for final acceptance/UAT/production configuration of this specific control until a default (or an explicit "no default" ruling) is set.
- Boss decision required: Yes — already correctly flagged by TEAM B for exactly this purpose.

**FV006-SOD-008 — Audit trail for policy-blocked confirmation attempts not explicitly stated**

- Verification Area: Confirmation Gate Policy — auditability
- TEAM B Artifact(s): `13_...md` §04 (Future Testability/Observable Outcome: "confirmation refused with an explicit, named reason (not a silent no-op)")
- Approved Evidence/Baseline: N/A — documentation-completeness observation
- Finding Status: `GAP FOUND` (scope-limited — see §00 above)
- Severity: Minor
- Why it matters: The artifact specifies that a blocked confirmation attempt must surface an explicit, named reason to the user, but does not state whether the attempt (actor, timestamp, gate type, reason) is itself recorded as an auditable event. This may be covered in `09_CANONICAL_BUSINESS_EVENT_CATALOG.md`, not in this review's source set.
- Cross-domain impact: None identified.
- Gate impact: Low.
- Required owner: TEAM B / cross-reference confirmation against file 09.
- Blocking Development: No.
- Boss decision required: No.

## 05 — Summary of Findings

| ID | Area | Status | Severity | Blocking Development | Boss Decision Required |
|---|---|---|---|---|---|
| FV006-SOD-001 | APR-001 self-approval framing vs. role-based mechanism | GAP FOUND | Major | Yes (for "prevents self-approval" certification only) | Yes |
| FV006-SOD-002 | APR-001 approver reject/resubmit path undefined | GAP FOUND | Moderate | Yes (for approver-decision path) | No (unless unresolvable from evidence) |
| FV006-SOD-003 | APR-001 auditability not explicit in reviewed artifact | GAP FOUND (scope-limited) | Minor | No | No |
| FV006-SOD-004 | APR-002 "sequential/ordered" wording vs. §00 transition HOLD | CONFLICT FOUND | Major | Yes (for level-to-level gating logic only) | Yes |
| FV006-SOD-005 | APR-002 shared cross-document concept vs. asymmetric evidence | VERIFIED WITH CONDITIONS | Moderate | No | No (unless differentiated rollout desired) |
| FV006-SOD-006 | APR-002 SoD data-shape requirement | VERIFIED | N/A | No | No |
| FV006-SOD-007 | APR-003 confirmation gate default deferred, not defaulted | VERIFIED WITH CONDITIONS | Moderate | No (mechanism); Yes (final acceptance) | Yes (already flagged by TEAM B) |
| FV006-SOD-008 | APR-003 blocked-attempt audit trail not explicit | GAP FOUND (scope-limited) | Minor | No | No |

## 06 — Section-Level Verification Outcome

Within the scope of Approval / Permission / SoD verification only (this deliverable feeds the consolidated
Deliverable 14/15 recommendation; it is not itself the Formal IBPV terminal recommendation):

- APR-001 (Amount-Threshold Approval): `VERIFIED WITH CONDITIONS`. The threshold mechanism, company/branch
  scoping, and Pending-Approval state are sound and evidence-traced. The stated self-approval-prevention purpose
  is broader than the specified role-based mechanism guarantees (FV006-SOD-001), and the approver reject/resubmit
  path is undefined (FV006-SOD-002).
- APR-002 (Sequential Level-Based Approval): `VERIFIED WITH CONDITIONS`, with one `CONFLICT FOUND` requiring
  resolution before the "sequential" shape can be considered unambiguously separated from the unverified legacy
  workflow (FV006-SOD-004). TEAM B correctly did **not** invent the missing internal transition/permission logic —
  that remains properly classified `EVIDENCE MISSING` and carried forward, consistent with the Boss Evidence Gate
  control. The finding here is one of imprecise labeling risk, not of hidden fabrication.
- APR-003 (Sales Confirmation Gate): `VERIFIED WITH CONDITIONS`. TEAM B correctly left the default policy value as
  an open Boss/business decision rather than quietly adopting the reference system's advisory-only behavior or
  inventing a hard-gate default. This is the cleanest of the three controls in this review.
- SoD data-shape requirement (§05): `VERIFIED` as a correctly-scoped, evidence-supportable, enforcement-agnostic
  requirement.

No finding in this deliverable independently warrants an overall `NOT READY FOR DEVELOPMENT` verdict for GROUP A;
that determination is reserved for the consolidated Deliverable 14/15 review, which must weigh this section's
findings alongside all other verification areas.
