# 15 — Pre-Development Gate Recommendation to Boss

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006-D15`
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone
Execution Function: EXPERT IBPV — Independent Business Process & Design Verification Team
Session: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006`
Decision Authority: Boss — Sole Final Approver
Recommending Body: EXPERT IBPV (verification only — this is not a self-approval and not a Team C authorization)

## 1. Recommendation

**`FORMAL IBPV COMPLETE — REWORK REQUIRED / NOT READY FOR DEVELOPMENT`**

TEAM B's GROUP A design is independently assessed as substantially complete and well-evidenced. It is not, however, clear to begin unrestricted Team C development today, because five distinct items independently trigger the charter's Pre-Development Blocking Rule (`EXPERT_IBPV_CHARTER.md` §9). Each is narrow and nameable — none requires TEAM B to restart or broadly redesign GROUP A. Full detail and evidence citations for every item below are in Deliverable 14 (§3) and the individual verification files it references.

This is a recommendation, not a decision. EXPERT IBPV cannot authorize Team C, waive a gap, or approve this design finally — only Boss can.

## 2. What May Proceed Now, Without Further Boss Action

The following is independently verified and, in this team's assessment, may proceed to Team C planning/development immediately once Boss accepts this report:

- End-to-end order-to-cash, procure-to-pay, and inventory-movement process design (Deliverable 02 — 5/7 findings `VERIFIED` outright).
- Domain boundaries, shared-master model, Legal Company/Branch/Warehouse layering (Deliverable 03, Deliverable 11 `FV006-SAAS-002`).
- The approval control's vendor-neutral **data shape** (levels, approver assignment, approve/reject event as data, rejection-reason field) — independent of its still-unresolved internal enforcement logic (Deliverable 07).
- The over-fulfillment and Sales-Confirmation-Gate **mechanisms** (configurable policy switches) — independent of their still-open default values (Deliverable 08, Deliverable 13 §D.0).
- The Thailand/user-reality register as an evidence-tier-disciplined tracking document (Deliverable 11, `FV006-TH-001`–`004`, all `VERIFIED`).
- The financial/accounting **handoff interface itself** (what crosses the boundary, when, with what reference) (Deliverable 09, `FV006-ACC-001` `VERIFIED`).

## 3. Items Requiring a Boss Decision

These are not defects TEAM B can fix by itself — each is a business-policy or baseline-ratification choice that only Boss can make. IBPV states the options; it does not choose among them.

| # | Item | Options | IBPV's view on urgency |
|---|---|---|---|
| 1 | **Tenant / SaaS boundary structural design** (D14 §3.2) | (a) Ratify TEAM B's Tenant structure (file 14) as the new approved SaaS baseline; or (b) direct TEAM B to justify/rework it against an explicit baseline before it is treated as settled. | Before the Tenant-layer boundary model is built by Team C. Everything beneath it (Legal Company/Branch/Warehouse) is independently evidenced and unaffected either way. |
| 2 | **Sales-side cancellation gate symmetry** (D14 §3.3) | (a) Require a Sales-side cancellation gate symmetric to Purchase's (block on locked/posted invoice); or (b) accept the asymmetry as a deliberate, disclosed business-risk trade-off. Either is legitimate — what is not legitimate is treating it as already decided by the reasoning TEAM B offered, which this session found does not hold up against the evidence it cites. | Before the Sales-side cancellation-gate design is finalized. Requires input from whoever owns the Accounting Core / AR-AP domain, since the underlying fact in question (posted vendor bill vs. posted customer invoice) is outside GROUP A's authority to resolve alone. |
| 3 | **Approval internal-logic evidence gap** (D14 §3.1 — pre-existing, carried forward from the Boss Evidence Gate, not new) | (a) Commission source acquisition / reverse-engineering / interview effort for the three named legacy approval modules; or (b) explicitly accept the vendor-neutral shape as the final target design and formally close the legacy-fidelity question without further acquisition. | Before the level-to-level approval **gating logic** (not the shape) is implemented. |
| 4 | **Three deferred policy defaults** — canonical Invoiced Quantity definition, Over-Fulfillment/Over-Billing default, Sales Confirmation Gate default (D13 §D.0, all independently judged **safe to defer**) | Set each default value (or explicitly rule "no default"). | Not before Development starts broadly. Recommended before the specific computation/flow each feeds is considered feature-complete (see D13 for per-item timing detail — the Sales Confirmation Gate default carries the shortest fuse of the three, given its proximity to credit-risk and overselling control). |

## 4. Items Requiring TEAM B Rework (Documentation/Design Clarification, Not a Business-Policy Choice)

These are independently verified as genuine gaps in TEAM B's own design package. None requires new evidence or a Boss policy call — they are for TEAM B to close directly.

1. **Denied-approval wind-down path** (D14 §3.4, Critical) — no state transition or event exists for what happens when a Supply Commitment approval is denied. Newly found by this session; not previously flagged by TEAM B.
2. **Retry/idempotency contract for Confirm/Movement Execution** (D14 §3.5, Critical) — undefined whether a duplicate submission safely no-ops or double-creates effects. Newly found by this session.
3. **Downstream-failure compensation for hard cross-domain handoffs** (D14 §3.5, Major) — no compensation/timeout/reconciliation defined for when a receiving domain's write fails after the initiating domain has committed. Newly found by this session.
4. **"Sequential" approval wording internal inconsistency** (D14 §3.1, Major) — the artifact's own wording could be misread as confirming enforced sequential gating in the same section that correctly marks that logic HOLD.
5. **Self-approval mechanism gap** (D14 §3.1, Major) — the stated "prevent self-approval" purpose is broader than the actual role-based mechanism.
6. **Event transport-semantics gap** (D14 §3.6, Major, systemic) — no event in the catalog states sync/async, ordering, or delivery-guarantee semantics; underlies two race-condition findings.
7. **Lot/serial and package fact ownership** (D14 §3.7, Major) — first-class facts with no stated owner, changing event, or lifecycle-end.
8. **Shared-master archival rule** (D14 §3.7, Major) — no general rule against hard-deleting a Shared Master fact once referenced by history.

## 5. Governance Confirmations

- Repository, branches, and all four cited frozen commits (canonical baseline, TEAM B design, TEAM A evidence, independent evidence review) were independently verified to exist and resolve correctly (Deliverable 01 §2).
- TEAM B's 21-file manifest was independently re-hashed: **PASS** (Deliverable 01 §4, Deliverable 12 §1).
- No TEAM B or TEAM A artifact was edited by this session (Deliverable 01 §3, confirmed again at time of writing via `git status`).
- No vendor source, ORM structure, or quarantined material was used as input (Deliverable 01 §3).
- This report used only the charter's allowed status vocabulary throughout (Deliverable 14 §5).
- No true stop condition (per the governing prompt §17) was encountered during this session.

## 6. What This Recommendation Is Not

- It is **not** `TEAM C AUTHORIZED`.
- It is **not** `BOSS APPROVED` or `FINAL APPROVED` for TEAM B's design.
- It does **not** waive any gap — every held item above remains on HOLD until Boss rules on it or its named owner closes it.
- It does **not** merge, release, or deploy anything. This session's only repository actions are: creating the fifteen files in `EXPERT_IBPV/GROUP_A_SALES_INVENTORY_PURCHASE/FORMAL_VERIFICATION_FV_006/` (plus the SHA-256 manifest at Deliverable 16), committing them, and pushing the dedicated branch `ibpv/group-a-sip-formal-verification-006`.

`Independent experts verify the design; only Boss decides whether the lifecycle may advance.`
