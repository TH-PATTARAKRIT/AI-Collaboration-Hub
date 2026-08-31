# 14 — EXPERT IBPV Independent Verification Report

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006-D14`
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone
Execution Function: EXPERT IBPV — Independent Business Process & Design Verification Team
Session: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006`
Control Level: `/L999.999`
Boss: Sole Final Approver
Charter: `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/EXPERT_IBPV_CHARTER.md`

This report consolidates Deliverables 01–13 of this session. It does not restate their detail; it cross-references every material finding across all twelve verification files (a step none of the individual verification files could perform on its own, since each was produced by an independent reviewer scoped to a subset of TEAM B's package) and states this team's overall independent conclusion. **This report is a verification conclusion, not a Boss decision and not a Team C authorization.**

## 1. What Was Verified and How

- TEAM B's frozen design package (21 files, commit `b98a3b9f...`) was independently re-hashed against its own manifest: **PASS**, 21/21 files present, all 20 hashes match (Deliverable 01 §4, Deliverable 12 §1 — re-performed twice independently, same result both times).
- Every one of the charter's twelve core verification responsibilities (Charter §5) was independently assigned to a dedicated deliverable: business process (D02), cross-domain flow (D03), state transitions (D04), event flow (D05), data/fact ownership and handoff (D06), approval/permission/SoD (D07), exception/partial/cancel/return/correction/recovery (D08), accounting/compliance interface (D09), integration failure/retry/recovery (D10), SaaS/multi-company/Thailand reality (D11), and requirement-to-evidence traceability with conflict/gap consolidation (D12–D13).
- No TEAM B or TEAM A artifact was edited. No design was authored or repaired by IBPV in place of TEAM B (verified: `git status` shows only new files under `FORMAL_VERIFICATION_FV_006/`).
- TEAM B's own self-assessment (file `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md`) was treated as a claim to test, not as evidence — every deliverable that touched a claim from that file independently re-derived its own conclusion from the underlying design and evidence artifacts.

## 2. Domain-Wide Picture

The large majority of TEAM B's design was **independently verified** as complete, evidence-traceable, and internally coherent:

- End-to-end order-to-cash, procure-to-pay, and inventory-movement processes are complete and traceable to TEAM A's evidence (D02 — 5 of 7 findings `VERIFIED` outright, the remaining 2 `VERIFIED WITH CONDITIONS` on disclosed policy items).
- Domain boundaries, the shared-master model, and Legal Company/Branch/Warehouse layering are evidence-cited and internally consistent (D03, D11 `FV006-SAAS-002`).
- The core state and event models are largely sound and traceable to TEAM A's E2E lifecycle map, with specific, named exceptions detailed in §3 below (D04, D05).
- Fact ownership is mostly clear, with named gaps for two specific fact types and one missing archival rule, none independently blocking (D06).
- The Thailand/user-reality evidence-tier discipline (Observed Practice vs. Company Variation vs. Thailand Reality vs. Target Requirement) is faithfully preserved with no detected silent generalization (D11 `FV006-TH-001` through `004`, all `VERIFIED`).
- The three business-policy items TEAM B explicitly deferred to Boss (canonical Invoiced Quantity definition, Over-Fulfillment/Over-Billing default, Sales Confirmation Gate default) were each independently re-judged safe to leave open at this Pre-Development Gate — none is itself a control-integrity or evidentiary gap (D13 §D.0, D08 `FV006-EXC-004`).

This is not a marginal design. It is independently assessed as substantially complete and well-evidenced. The findings in §3 are real, but they are concentrated, nameable, and — with one exception discussed in §4 — scoped to specific control points rather than to the design as a whole.

## 3. Consolidated Material Findings (Cross-Referenced Across All Deliverables)

Findings below are grouped by theme because several were independently rediscovered from different angles by different reviewers who could not see each other's work — that convergence is itself evidence the finding is real, not an artifact of one reviewer's framing.

### 3.1 Approval / Permission / SoD Internal Logic — Critical, pre-existing carry-forward

- **Status:** `EVIDENCE MISSING`. **Severity:** Critical. **Source:** D07 (`FV006-SOD` series), D13 `FV006-GAP-001`.
- The internal enforcement/permission logic of the three legacy approval modules (`sale_order_level_approve`, `purchase_request_level_approve_po`, `purchase_request_level_approve`) has never been located in any source extraction, by TEAM A, the independent evidence review, or this session. This was already recorded as a controlled carry-forward at the Boss Evidence Gate (`GROUP_A_BOSS_EVIDENCE_GATE_APPROVAL_2026-08-31.md` §4 item 1) — it is not new. TEAM B correctly designed only the vendor-neutral shape and marked the internal logic HOLD; this session independently confirms that HOLD was applied honestly.
- **Blocks:** only the internal enforcement/gating logic of the Sequential Level-Based Approval control (APR-002). The surrounding data shape (levels, approver assignment, approve/reject event, rejection reason) is independently verified and may proceed.
- **New in this session (not pre-existing):** two additional, TEAM-B-fixable defects layered on top of the pre-existing HOLD:
  - `FV006-SOD-004` (D07, Major, `CONFLICT FOUND`) — the design artifact names the control "**Sequential**" and describes "**ordered**" levels in the same section that separately marks the transition logic `HOLD`, without ever stating that "ordered" means numbering/labeling only. A reader could mistake this for the sequencing behavior being settled. Wording clarification only — not a redesign.
  - `FV006-SOD-001` (D07, Major, `GAP FOUND`) — the control's stated purpose ("prevent self-approval") is broader than its actual mechanism (a role check, not an identity check); nothing currently excludes a role-holding creator from approving their own commitment.
- **Required owner:** Boss/PMO for the pre-existing evidence gap (source acquisition or equivalent); TEAM B for the two wording/mechanism defects.

### 3.2 SaaS Tenant Boundary — Untraceable Structural Design

- **Status:** `GAP FOUND` (D11 `FV006-SAAS-001`, D13 `FV006-GAP-007`) independently corroborated as `EVIDENCE MISSING` / Critical by a second, differently-scoped reviewer (D03 `FV006-XDF-006`). **Severity: Major to Critical (reviewers disagree on label; both classify it as blocking).**
- Independently confirmed by direct grep of `00_Project_Governance/` (D11): the project's approved baselines (`STATE01_PROJECT_CHARTER_v1.0.md`, `STATE01_SCOPE_PRINCIPLES_RACI_v1.0.md`, `ARCHITECTURE_GOVERNANCE_STANDARD.md`) do mandate that SMEsPlus be multi-tenant SaaS — the *need* for a Tenant concept is traceable. But no governance document defines what a Tenant *is* structurally, its relation to Legal Company, or its isolation mechanics. TEAM B's file 14 is the first artifact in the whole corpus to define that structure, and says so itself.
- A related internal-consistency issue rides on the same finding: file 14's absolute "no fact crosses Tenants" rule is not re-asserted per-row in its own shared-master sharing table (`FV006-SAAS-003`, Moderate).
- **Blocks:** the Tenant-layer boundary model specifically — not the Legal Company/Branch/Warehouse layers beneath it, which are independently evidence-cited (`FV006-SAAS-002`, `VERIFIED WITH CONDITIONS`).
- **Required owner:** Boss (this is fundamentally a baseline-ratification decision: either Boss ratifies TEAM B's Tenant structure as the new approved SaaS baseline, or directs TEAM B to justify it further before it is treated as settled).

### 3.3 Asymmetric Cancellation Gate (Fit-Gap #12) — the most independently corroborated finding in this session

- **Status:** `CONFLICT FOUND`. **Severity: Major** (one reviewer independently scored the same underlying dependency `Critical` from the accounting-interface angle — see below). **Independently found, from four different angles, by four different reviewers who could not see each other's work:**
  - D03 `FV006-XDF-003` (cross-domain flow angle: Sales/Purchase gates read Accounting-owned facts never modeled in the interface files)
  - D08 `FV006-EXC-005` (exception-catalog angle: the comparison TEAM B used to justify the asymmetry isn't the comparison that actually tests it)
  - D09 `FV006-ACC-003` (accounting-boundary angle, scored **Critical**: the "non-cancel/non-draft vendor bill" fact the justification depends on is an AR/AP internal document-lifecycle state that File 15 itself places outside Group A's authority)
  - D12 `FV006-FG-012` (evidence-traceability angle: TEAM B closed an item TEAM A explicitly found "not resolvable from source alone," using a rationale that, on independent re-reading, mischaracterizes the evidence it cites)
- Consolidated in D13 `FV006-GAP-015`.
- **Why this matters more than a typical Moderate design nuance:** TEAM B's own accounting-interface model (D09's primary source, file 15) explicitly states that AR/AP internal posting logic is Accounting Core's domain, "not designed, redesigned, or second-guessed here." Fit-Gap #12's justification for Purchase's stricter gate does exactly that — it reaches into an AR/AP-internal fact to justify a GROUP A control decision, inconsistently with the boundary GROUP A itself declared everywhere else in the same design package.
- **Blocks:** the Sales-side cancellation-gate design specifically (does not block Purchase's own gate, which is evidenced independently of this justification, nor the rest of GROUP A).
- **Required owner:** Boss (business-policy decision: does SMEsPlus want a Sales-side cancellation gate symmetric to Purchase's, or is the asymmetry a deliberately accepted risk trade-off?) — this decision needs input from whoever independently owns the Accounting Core domain's AR/AP posting-state model, since the underlying fact in question is outside GROUP A's authority to define unilaterally.

### 3.4 Denied-Approval Wind-Down Path — new Critical finding, not previously flagged by TEAM B

- **Status:** `GAP FOUND`. **Severity: Critical.** **Source:** D04 `FV006-STE-004`, D05 `FV006-EVT-003` (same underlying gap, found independently from the state-model and event-catalog angles respectively).
- The Supply Commitment (Purchase Order) can enter a `Pending Approval` state, but **no state transition and no catalogued event exists anywhere in the design for what happens if that approval is denied.** Unlike the three items TEAM B explicitly flagged as open Boss/business policy questions, TEAM B did not self-flag this — it is a genuine process-completeness gap this session found independently. The concrete risk named by both reviewers: a denied approval could leave an already-triggered Inventory fulfillment request with no instruction to stand down — an audit/financial-integrity risk, not merely a UX gap.
- **This finding does not appear in Deliverable 13's consolidated gap register**, because Deliverable 13 was built from TEAM B's own carry-forward register (file 18) plus this session's traceability audit (D12) — neither of which covers state/event-model completeness. It is recorded here for the first time as a cross-deliverable synthesis finding and must be added to any downstream tracking of this Gate's open items.
- **Blocks:** the denied-approval path for the Sequential Level-Based Approval control specifically; does not block the approved-path flow.
- **Required owner:** TEAM B (add the missing state transition and event; coordinate with the Approval/SoD design in §3.1).

### 3.5 Retry / Idempotency and Downstream-Failure Compensation — new findings, not previously flagged by TEAM B

- **`FV006-INT-001`** (D10). **Status:** `GAP FOUND`. **Severity: Critical.** TEAM B defines idempotency for exactly one narrow case (Stock Position bin concurrency). There is no stated contract for what happens if a Confirm action or a Movement Execution trigger is invoked twice (double-click, network retry, message redelivery) — whether it safely no-ops or silently double-creates instructions, reservations, or billing writes is unstated.
- **`FV006-INT-002`** (D10). **Status:** `GAP FOUND`. **Severity: Major.** The "hard" cross-domain handoffs (Sales↔Inventory, Inventory↔Purchase) are documented only for their success path; no compensation, timeout, or reconciliation mechanism is defined for when the receiving side's write fails after the initiating side has already committed.
- **Like §3.4, neither finding appears in Deliverable 13's register**, for the same structural reason (D13 was not built from D10's source material). Recorded here for the first time as a cross-deliverable synthesis finding.
- **Blocks:** the retry/idempotency contract for Confirm/Movement Execution actions specifically, and the compensation mechanism for hard cross-domain handoffs specifically. Does not block the rest of GROUP A's design.
- **Required owner:** TEAM B.

### 3.6 Event Transport Semantics — systemic, contributing cause of two race-condition findings

- **`FV006-EVT-002`** (D05). **Status:** `GAP FOUND`. **Severity: Major** (systemic — affects every row of the canonical event catalog). No event in TEAM B's catalog states whether it is synchronous or asynchronous, its delivery-ordering guarantee, or its consumer-failure behavior. This underlies two concrete, separately-scored race-condition findings in the same deliverable (a Sales-side race tied to §3.4's denied-approval gap, and a lower-risk Purchase-side race since Purchase's receipt-demand path is stated as direct/synchronous).
- **Blocks:** does not independently block beyond what §3.4 already blocks; recorded because it is the systemic cause and should be closed once, not per-event.
- **Required owner:** TEAM B.

### 3.7 Data Ownership — Major, non-blocking, but should close before Gate sign-off

- **`FV006-DFO-001`** (D06, Major, `GAP FOUND`): Traceability Unit (lot/serial) and Handling Unit (package) facts — which the design itself calls first-class — have no stated owner, changing event, or lifecycle-end.
- **`FV006-DFO-005`** (D06, Major, `GAP FOUND`): no general rule requires Shared Master facts to be archived rather than hard-deleted once referenced by a historical transaction, despite TEAM A's evidence showing this protection already exists for several individual concepts in the reference system.
- Neither reviewer scored these as independently blocking Development, but both flagged them as items that should be closed before this Gate is considered fully discharged, since Development would otherwise have to guess at the answer.
- **Required owner:** TEAM B.

## 4. What This Means, Read Together

No single finding in this report, taken alone, would justify calling the whole GROUP A design not ready. What changes that assessment is reading all twelve deliverables together, which none of the individual reviewers could do: **the charter's Pre-Development Blocking Rule (§9) is written as an "any of the following" test, and this session independently confirms at least five distinct, unresolved items each independently matching a different one of its blocking categories** — not one item interpreted five ways, five separate items:

1. Unresolved security/permission/SoD design issue → §3.1 (approval internal logic + internal wording conflict)
2. Untraceable Team B design decision → §3.2 (Tenant structural design)
3. Unresolved accounting/compliance impact → §3.3 (cancellation-gate dependency on AR/AP-internal fact)
4. Unverified state/event transition affecting financial/control integrity → §3.4 (denied-approval wind-down) and §3.5 (retry/idempotency for Confirm/Movement Execution)
5. (Contributing) missing evidence for a material business rule → the pre-existing approval-logic evidence gap within §3.1

Per the charter, each of these independently keeps its own specific control point on HOLD unless Boss explicitly rules otherwise for that item — the charter does not require the whole design to be defect-free, but it does require each blocking category to be actually resolved or explicitly overridden, one item at a time, not waived in bulk because most of the design is sound.

## 5. Status Vocabulary Compliance

Every deliverable in this session (01–13) used only the charter's allowed status vocabulary. No deliverable used `FINAL APPROVED`, `PRODUCTION READY`, `RELEASE APPROVED`, or claimed `BOSS APPROVED` for its own conclusion (the phrase appears only where deliverables correctly cite the *pre-existing*, already-approved Evidence Gate and Charter status — verified by direct search, Deliverable-file-level, before this report was written).

## 6. Terminal Classification

**`FORMAL IBPV COMPLETE — REWORK REQUIRED / NOT READY FOR DEVELOPMENT`**

This classification is scoped, not blanket — see Deliverable 15 for the precise, itemized breakdown of what may proceed immediately, what requires TEAM B rework, what requires Boss policy decision, and what requires input from outside GROUP A's authority. It does not authorize Team C. It does not constitute Boss approval. It is this team's independent verification conclusion for Boss to act on.
