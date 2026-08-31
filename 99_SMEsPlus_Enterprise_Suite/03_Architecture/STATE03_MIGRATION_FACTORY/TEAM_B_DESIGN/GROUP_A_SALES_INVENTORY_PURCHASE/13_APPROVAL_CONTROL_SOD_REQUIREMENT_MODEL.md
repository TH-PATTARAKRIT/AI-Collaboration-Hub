> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 8 — Approval / Control / SoD Design

# 13 — APPROVAL, CONTROL AND SoD REQUIREMENT MODEL

## 00 — Mandatory Approval Unknown Control (Governing Prompt §11) — Compliance Statement

Evidence confirms three modules (`sale_order_level_approve`, `purchase_request_level_approve_po`,
`purchase_request_level_approve`) exist, are installed, and show real historical usage — but their exact Python
source is absent from every location the research effort had access to, including the Independent Evidence
Review's own independent confirmation. Per governing prompt §11 and Boss Gate §4.1, TEAM B does **not** infer
exact internal workflow from field names or row values. The following remain unverified and are not designed here:
exact approval-button behavior; exact Level 1 → Level 2 transition; exact reject transition; exact permission
model; exact SoD behavior; exact trigger for the undocumented intermediate state observed in live data; exact
cancel/reset interaction with an in-progress approval.

Every design decision below that touches this area is explicitly marked `HOLD / EVIDENCE REQUIRED FOR THIS
DECISION POINT` where it depends on the unverified internal logic, while the surrounding, evidence-supportable
target business requirement is still stated.

## 01 — Two Genuinely Distinct Approval Mechanisms — Not to Be Merged

Restated from [07](07_PURCHASE_CANONICAL_DESIGN.md) §03 as the governing principle for this file: **Amount-
Threshold Approval** and **Sequential Level-Based Approval** are two different control concepts that happen to
coexist on the same commitment types in evidence. A target design must implement them as two separate,
independently-configurable Approval Control mechanisms, never as one merged concept.

## 02 — Amount-Threshold Approval (Fully Evidenced, `ADAPT`)

| Field | Content |
|---|---|
| Decision ID | APR-001 |
| Business Problem / Need | Require oversight of a supply commitment above a value threshold: (a) a role-based authority gate — an actor without the approval-authority role cannot approve it — **and** (b) an identity-based exclusion — the commitment's own creator/requester may not approve it, regardless of role. **CORR-008 correction (`FV006-SOD-001`):** the prior wording of this row asserted "prevent self-approval" as the business need while specifying only the role-based mechanism below, which does not by itself exclude a role-holding creator from approving their own commitment. TEAM B corrects the wording to state both requirements explicitly, and adds (b) as an explicit new requirement — see the added row "Identity-Based Self-Approval Exclusion" below. |
| Approved Evidence Input | `04` §02 PO-06/07/08, test-confirmed (role-based gate only — see Unknown/Assumption row for what (b) is and is not evidenced by) |
| Evidence Status | VERIFIED FACT (role-based gate); (b) is a TEAM B target-design addition, not evidenced — see Unknown/Assumption row |
| Team A Candidate | ADAPT (Fit-Gap #2) |
| TEAM B Independent Decision | `ADAPT` unmodified as a Purchase-side Approval Control: a configurable threshold amount (currency-converted where the commitment's currency differs from the threshold's reference currency) and an approval-authority role; a commitment above threshold and without an authorized actor transitions to Pending Approval instead of erroring. **CORR-008 addition:** independently of the role check, the acting approver's identity must be evaluated against the commitment's own creator/requester identity at the moment of approval; if they match, the approval attempt is refused with an explicit reason (reusing the same explicit-rejection UX pattern already required below for an unauthorized-role attempt), regardless of whether the matching actor also holds the approval-authority role. |
| Identity-Based Self-Approval Exclusion (CORR-008 addition, `FV006-SOD-001`) | A commitment's creator/requester identity and its approver identity, for any given approval action, must be independently evaluable and must not be equal. This composes with, and extends, the general SoD data-shape requirement in §05 below (which requires requester/approver identities to be *distinguishable* in the data model) by additionally requiring that distinguishability be *enforced* — not merely representable — at the amount-threshold control specifically. TEAM B does not claim this was how any legacy module's internal logic behaved (that internal logic remains outside evidence, per §00); this is a target business-control requirement stated independently of the unverified legacy internals, closing the gap between APR-001's stated purpose and its previously role-only mechanism. Whether role-based gating alone would have been an acceptable control strength, versus mandatory creator exclusion being required, was Formal IBPV's identified open policy question (`FV006-SOD-001`); TEAM B resolves it here by requiring the stronger (identity-exclusion) control, consistent with the stated business need this control has always claimed to serve. |
| Rationale | Clean, simple, working control with no ambiguity in evidence for the role-based half; the identity-based half is added because the control's own stated purpose ("prevent self-approval") otherwise remains unmet by its specified mechanism, which is a gap Formal IBPV independently identified as certifiable-blocking for this control's stated purpose specifically |
| Business Fact(s) | Supply Commitment approval state |
| Owner | Purchase |
| Lifecycle/State Impact | Introduces the `Pending Approval` phase in [07](07_PURCHASE_CANONICAL_DESIGN.md) §01 |
| Event Impact | Supply Commitment Confirmed (may branch); Supply Commitment Approved; Supply Commitment Rejected (**CORR-010 cross-reference**, `FV006-STE-004`/`FV006-EVT-003` — this control's denial path is fully designed in [07](07_PURCHASE_CANONICAL_DESIGN.md) §01 and [09](09_CANONICAL_BUSINESS_EVENT_CATALOG.md) §02; this row only records that APR-001, not APR-002 below, is the control that raises it — Formal IBPV RV-009 found no cross-reference existed here despite one being claimed) |
| Quantity/Value Impact | None directly; gates on commitment total value |
| Cross-Domain Dependency | None beyond Purchase itself |
| Thailand/User Reality Status | N/A |
| SaaS/Multi-Company Impact | Threshold and authority role are company-scoped, currency-converted per company |
| Accounting Interface Impact | None |
| Exception/Correction Impact | An unauthorized approval attempt is a silent no-op in evidence — TEAM B requires the target design to surface an explicit, informative rejection instead (a deliberate UX strengthening; see [12_PERSONA...]-equivalent friction note carried into §16) |
| Future Testability/Observable Outcome | Given: commitment total > threshold, actor lacks authority-role → When: confirm action taken → Then: state = Pending Approval, no error raised, an explicit "awaiting approval" signal is observable |
| Unknown/Assumption | None material |
| Carry-Forward | None |
| Formal IBPV Review Need | Standard |

Sales-side equivalent: evidence shows only an advisory, non-blocking credit-exposure warning, never a hard gate
(test-confirmed). See §04 below for TEAM B's independent decision on whether Sales needs an equivalent hard
control.

## 03 — Sequential Level-Based Approval (`EXTEND`, Internal Logic `HOLD`)

> **CORR-008 reading note (`FV006-SOD-004`):** "Sequential" in this section's title, and "sequential" in the
> Business Problem/Need row below, name the *numbering/labeling* convention (Level 1, Level 2, ... — a data
> shape) and the general multi-person sign-off *need*. Neither asserts that level-to-level **gating** is enforced
> in strict order. Whether gating is actually enforced in sequence remains `HOLD / EVIDENCE REQUIRED FOR THIS
> DECISION POINT`, stated explicitly in the "TEAM B Independent Decision" row below and consistent with §00's
> disclaimer. Read the title and this row's "sequential" as a name, not a settled enforcement claim.

| Field | Content |
|---|---|
| Decision ID | APR-002 |
| Business Problem / Need | Multi-person, sequential, auditable sign-off with a recorded reason on rejection |
| Approved Evidence Input | `04` §03 (full cross-model investigation), `07` §04 (approval fact table), Boss Gate §4.1 |
| Evidence Status | RESOLVED — ACTIVE HISTORICAL CONTROL WITH OWNERSHIP EVIDENCE (existence, installation, and real usage); internal workflow logic EVIDENCE_MISSING |
| Team A Candidate | UPDATED to EXTEND (Fit-Gap #13), with an explicit UNKNOWN remainder on the Purchase-commitment-level half |
| TEAM B Independent Decision | `EXTEND` — design a vendor-neutral **Approval Control** concept: N approval levels, each carrying an assigned approver, an approve/reject event with timestamp, and a rejection reason; attachable to any commitment-type document (Commercial Commitment, Supply Commitment, Internal Demand Request) that a business configures to require it. **CORR-008 wording correction (`FV006-SOD-004`):** the levels are numbered/labeled (Level 1, Level 2, ...) for audit and display purposes only — this numbering is a data-shape/labeling convention, not an assertion that levels are enforced in strict sequential gating order. Whether Level 2 may act before Level 1 completes (i.e., whether gating is actually enforced in sequence) is part of the internal trigger/transition logic below and remains **not** designed — `HOLD / EVIDENCE REQUIRED FOR THIS DECISION POINT`. Internal trigger conditions, the exact level-to-level transition/gating rule, and exact permission checks are **not** designed. |
| Rationale | The DATA proves the feature is real and was used (heaviest, clearly-completed usage on the Internal Demand Request concept: large share approved/rejected in evidence); it does not prove every internal workflow rule. Designing the generic shape without the internal logic keeps this design evidence-honest while still giving Formal IBPV something concrete to review |
| Business Fact(s) | Approval level assignment, approval/rejection event, rejection reason |
| Owner | The owning commitment/request document (Sales, Purchase, or Internal Demand Request) |
| Lifecycle/State Impact | Gates progression from Draft/Pending toward Committed/Approved on whichever document type has it configured |
| Event Impact | New events: Approval Level Assigned, Approval Level Approved, Approval Level Rejected — added to [09](09_CANONICAL_BUSINESS_EVENT_CATALOG.md) as document-type-conditional, not universal |
| Quantity/Value Impact | None directly |
| Cross-Domain Dependency | Shared Approval Control concept usable by Sales, Purchase, and Internal Demand Request without being owned by any single one of them — a Shared Master-adjacent control capability |
| Thailand/User Reality Status | N/A — no Thailand-specific evidence found for this control |
| SaaS/Multi-Company Impact | Approver assignment must resolve within the acting company/branch scope |
| Accounting Interface Impact | None |
| Exception/Correction Impact | Rejection is a first-class event with a mandatory reason; whether a rejected document can be resubmitted through the same levels or must restart is `HOLD` |
| Future Testability/Observable Outcome | Given: a document type configured to require N approval levels → When: submitted → Then: an approval-pending signal is observable per level, in order; exact button/permission behavior is explicitly NOT specified pending source |
| Unknown/Assumption | Internal workflow logic (button triggers, exact transitions, SoD enforcement) — `HOLD`, per Boss Gate §4.1 |
| Carry-Forward | Yes — source-code acquisition for the three named modules remains the action item that would resolve this HOLD |
| Formal IBPV Review Need | High — this decision point should be a priority review item precisely because of the internal-logic HOLD |

## 04 — Sales-Side Confirmation Gate — An Open Business-Policy Decision

| Field | Content |
|---|---|
| Decision ID | APR-003 |
| Business Problem / Need | Should a commercial commitment be blocked by credit exposure or inventory availability at confirmation? |
| Approved Evidence Input | `03` §02 SO-32/33/36 (advisory-only, test-confirmed non-blocking); `02` (advisory-only availability, no blocking gate found) |
| Evidence Status | VERIFIED FACT (for the reference system's own behavior) |
| Team A Candidate | UNKNOWN (Fit-Gap #14) |
| TEAM B Independent Decision | Neither `ADAPT` (advisory-only) nor invent a hard gate by default — require an **explicit, configurable Confirmation Gate Policy** per gate type (credit exposure, inventory availability), each independently settable to block / warn-and-allow / allow-silently. TEAM B does not fix a default. |
| Rationale | The reference system's choice is one legitimate configuration, not necessarily SMEsPlus's correct default — this must be a deliberate business decision, not an inherited default, per governing prompt §13.1 |
| Business Fact(s) | Commercial Commitment confirmation eligibility |
| Owner | Sales |
| Lifecycle/State Impact | May prevent Draft/Sent → Committed transition if configured to block |
| Event Impact | Commercial Commitment Confirmed may now fail with an explicit reason, where configured |
| Quantity/Value Impact | None directly |
| Cross-Domain Dependency | Inventory (Available/Forecasted read), Shared Master (Party credit exposure read) |
| Thailand/User Reality Status | N/A |
| SaaS/Multi-Company Impact | Policy is company-configurable |
| Accounting Interface Impact | None |
| Exception/Correction Impact | N/A |
| Future Testability/Observable Outcome | Given: policy=block, condition breached → When: confirm attempted → Then: confirmation refused with an explicit, named reason (not a silent no-op) |
| Unknown/Assumption | Which default (if any) SMEsPlus should ship with — explicitly left to Boss/business |
| Carry-Forward | Yes — recorded in [17](17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md) as requiring Boss/business input before finalization |
| Formal IBPV Review Need | Medium |

## 05 — Separation of Duties (SoD) — Business-Semantic Requirement, Not Implementation

TEAM B's canonical requirement, independent of the internal-logic Unknown in §03: **the actor who creates or
requests a commitment/request must be distinguishable, in the data model, from the actor(s) who approve it at
each level**, so that a future SoD control (self-approval prevention) can be enforced without a schema change.
This is a minimal, evidence-supportable requirement (both real mechanisms in evidence separate requester/approver
roles) — TEAM B does not specify the enforcement algorithm itself, only that the data shape must support it.

**CORR-008 cross-reference (`FV006-SOD-001`)**: §02 above now *enforces* this distinguishability specifically for
APR-001 (identity-based self-approval exclusion), not merely represents it. This section's requirement remains
the general, document-type-agnostic data-shape baseline every Approval Control instance (APR-001 and APR-002
alike) must satisfy; §02's addition is the first place that baseline is turned into an enforced control rather
than left as a representable-but-unenforced data shape.

## 06 — Summary Table

| Control | Status | TEAM B Disposition | HOLD? |
|---|---|---|---|
| Purchase amount-threshold approval — role-based gate | Real, working | `ADAPT` | No |
| Purchase amount-threshold approval — identity-based self-approval exclusion | New TEAM B requirement (CORR-008, `FV006-SOD-001`) | `EXTEND` | No |
| Sequential level-based approval (generic shape; "sequential" = numbering/labeling only, per CORR-008 note in §03) | Real, historically used | `EXTEND` | No (shape only) |
| Sequential level-based approval (internal workflow / level-to-level gating logic) | Real but source-unavailable | Not designed | **Yes** |
| Sales confirmation hard-gate (credit/availability) | Not present in reference (advisory-only) | New configurable policy, no default fixed | No (policy shape), Yes (default value, deferred to Boss) |
| SoD data-shape requirement (general baseline) | Inferred from both real mechanisms | `EXTEND` (minimal) | No |
