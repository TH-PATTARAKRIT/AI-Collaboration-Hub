# 13 — Design Conflict / Open Gap / Evidence-Missing Register

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006-D13`
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone
Execution Function: EXPERT IBPV — Independent Business Process & Design Verification Team
Session: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006`
Control Level: `/L999.999`
Boss: Sole Final Approver
Role reminder: IBPV classifies and judges deferability. It does not choose the business policy itself in any of the items below — where a default value or business rule is genuinely Boss's/business's call, this register says so explicitly and stops there.

Sources consolidated: `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` (TEAM B's own carry-forward register), `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md` §05 (TEAM B's own red-flag list), `TEAM_A/14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md` (baseline), and `12_REQUIREMENT_EVIDENCE_TO_DESIGN_TRACEABILITY_AUDIT.md` (this session's own new findings, Deliverable 12). `11_SAAS_MULTI_COMPANY_THAILAND_REALITY_VERIFICATION.md` is cross-referenced, not duplicated, for the Tenant-layer item this session's Deliverable 11 already fully adjudicated.

Classification vocabulary used below is the charter's allowed vocabulary only (`EXPERT_IBPV_CHARTER.md` §8): `VERIFIED`, `VERIFIED WITH CONDITIONS`, `GAP FOUND`, `CONFLICT FOUND`, `EVIDENCE MISSING`, `REWORK REQUIRED`, `NOT READY FOR DEVELOPMENT`, `READY FOR BOSS DECISION`. The Pre-Development Blocking Rule applied throughout is the charter's own (`EXPERT_IBPV_CHARTER.md` §9): Development stays on HOLD, absent explicit Boss override, where there is an unresolved Critical business-flow gap, an unresolved Critical cross-domain conflict, missing evidence for a material business rule, an unverified state/event transition affecting financial/control integrity, an unresolved accounting/compliance impact, an unresolved security/permission/SoD design issue, or an untraceable Team B design decision.

---

## Section A — The Six Mandatory Carry-Forwards (Governing Prompt §16 / File 18 §01)

### FV006-GAP-001 — Internal Workflow/Permission Logic of the Sequential Approval Modules

- **Verification Area:** Approval, permission and SoD flow (Charter §5.5)
- **TEAM B Artifact(s):** `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md` §00, §03 (APR-002); `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` §01 item 1
- **Approved Evidence/Baseline reference:** `TEAM_A/04_PURCHASE_CAPABILITY_MODEL.md` §03 (three real, installed, historically-used modules — `sale_order_level_approve`, `purchase_request_level_approve_po`, `purchase_request_level_approve` — with Python source confirmed absent everywhere searched, independently re-confirmed by `AUDIT_REVIEW/07...` §04 item 3)
- **Finding Status:** `EVIDENCE MISSING`
- **Severity:** Critical
- **Why it matters:** The exact approve/reject button behavior, level-to-level transition rules, permission model, and Separation-of-Duties enforcement for a real, historically-used, multi-level approval control are unknown because the source code has never been located, machine-wide, by either TEAM A or the Independent Evidence Review. TEAM B correctly designed only the vendor-neutral shape (N ordered levels, an approve/reject event, a rejection reason) and explicitly marked the internal logic `HOLD`. TEAM B's own readiness report (file 20 §05 item 1) flags this as "the single highest-priority review item." This independent review concurs and elevates it formally.
- **Cross-domain impact:** Affects Sales, Purchase, and the Internal Demand Request document types — any of the three may be configured to require this control. A missing or wrong permission/SoD model here is a live risk to segregation-of-duties integrity across the whole GROUP A backbone.
- **Gate impact:** This is the one item in this entire register that most directly and literally matches the charter's blocking language: "unresolved security/permission/SoD design issue." It should remain the headline blocking item of this Pre-Development Gate.
- **Required owner:** Boss/PMO (action item: acquire the three modules' source code, or commission an equivalent reverse-engineering/interview effort) — not resolvable by TEAM B or IBPV from documentation alone.
- **Blocking Development:** **Yes**, specifically for the internal enforcement/permission logic of the Sequential Level-Based Approval Control. Development of the surrounding vendor-neutral shape (levels, approver assignment, rejection event/reason as data) may proceed, since that shape is evidence-supported and independent of the unresolved internal logic.
- **Boss decision required:** Yes — both to authorize the source-acquisition action item and to decide whether Development may proceed on the surrounding shape while this HOLD remains open.

### FV006-GAP-002 — `account.fiscal.position` Base Logic (Accounting Core Interface)

- **Verification Area:** Accounting, tax, and compliance interface boundary (Charter §5.6)
- **TEAM B Artifact(s):** `15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md` §06; `18_...` §01 item 2
- **Approved Evidence/Baseline reference:** `TEAM_A/14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md` §02 High #4 — referenced constantly by Sale/Purchase tax computation but never located in source; "not addressed by CORR-003 — remains open"
- **Finding Status:** `EVIDENCE MISSING`
- **Severity:** Moderate (for GROUP A); this is a genuine dependency for Accounting Core's own domain, not a GROUP A defect
- **Why it matters:** GROUP A correctly treats tax-substitution logic as an interface-only handoff point, not something in its own design scope. The fact-of-substitution is designed; the algorithm is not, and cannot be, from GROUP A evidence.
- **Cross-domain impact:** Accounting Core domain must resolve this before Financial Handoff / tax-computation correctness can be fully verified end-to-end.
- **Gate impact:** Does not block GROUP A's own Pre-Development Gate — it is correctly scoped out. Should be tracked as an open dependency for whichever gate covers Accounting Core.
- **Required owner:** Accounting Core domain's own Team A/Team B/IBPV chain.
- **Blocking Development:** No, for GROUP A. Possibly yes for Accounting Core's own tax-computation build — outside this register's authority to determine.
- **Boss decision required:** No, for GROUP A specifically.

### FV006-GAP-003 — Orphaned `res.partner` Multi-Brand/Multi-HQ Columns

- **Verification Area:** Data flow, ownership, and traceability (Charter §5.4/§5.10)
- **TEAM B Artifact(s):** `04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md` §01; `18_...` §01 item 3
- **Approved Evidence/Baseline reference:** `TEAM_A/01_SHARED_MASTER_DEPENDENCY_MAP.md` PTY-21/CO-24 (real DB columns, zero source anywhere) — independently re-confirmed present and un-sourced during this session's own spot-check (Deliverable 12, `FV006-TRC-004`)
- **Finding Status:** `EVIDENCE MISSING` (origin/purpose of the columns), correctly **not** converted into a design gap by invention
- **Severity:** Minor
- **Why it matters:** TEAM B correctly declined to design a multi-brand/HQ capability the evidence cannot support, rather than guessing at a schema shape from unexplained columns. This is disciplined, not deficient, behavior.
- **Cross-domain impact:** None at present — no capability was built on top of the unexplained columns.
- **Gate impact:** None. If a real multi-brand/HQ requirement is later confirmed by business evidence, it is new scope for a future design session, not a defect in this one.
- **Required owner:** Future session, if and when a real business need is confirmed.
- **Blocking Development:** No.
- **Boss decision required:** No.

### FV006-GAP-004 — Two Uncoordinated Thai Branch Implementations

- **Verification Area:** Multi-company/Thailand business-reality boundary (Charter §5.8)
- **TEAM B Artifact(s):** `16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md` §01 item 1; `04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md` §01; `18_...` §01 item 4
- **Approved Evidence/Baseline reference:** `TEAM_A/01_SHARED_MASTER_DEPENDENCY_MAP.md` CO-15..24 (independently re-confirmed, Deliverable 12 `FV006-TRC-004`)
- **Finding Status:** `VERIFIED WITH CONDITIONS` — the structural duplication is correctly resolved (one Tax-Branch attribute, not two competing sources of truth); the underlying "does this correctly represent real Thai SME tax-branch structure" question is correctly preserved as `Unknown / Requires Real-User Validation` rather than answered
- **Severity:** Moderate
- **Why it matters:** Already independently examined in full in this session's own `11_SAAS_MULTI_COMPANY_THAILAND_REALITY_VERIFICATION.md` (`FV006-TH-001`, TBRAC evidence-tier preservation confirmed VERIFIED). Not re-litigated in full here; cross-referenced for completeness of this register.
- **Cross-domain impact:** Party/tax-registration modeling across all three GROUP A domains.
- **Gate impact:** Structural decision is sound for Pre-Development purposes; the real-user validation should happen before General Availability in Thailand, not necessarily before Development starts.
- **Required owner:** Business/real-user validation owner (Thailand market fit), per `16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md`.
- **Blocking Development:** No.
- **Boss decision required:** No additional decision beyond what `FV006-TH-001` already recorded.

### FV006-GAP-005 — Remaining Medium/Low Items from Team A's Register

See **Section C** below for the full item-by-item table (14 items, none elevated on independent review).

### FV006-GAP-006 — Real-User Validation Items from TBRAC Evidence

- **Verification Area:** Thailand/user-reality validation status
- **TEAM B Artifact(s):** `16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md` (full); `18_...` §01 item 6
- **Approved Evidence/Baseline reference:** `TEAM_A/11_THAILAND_BUSINESS_REALITY_AND_VARIATION_REGISTER.md`
- **Finding Status:** `VERIFIED` — already independently confirmed line-by-line in this session's `11_SAAS_MULTI_COMPANY_THAILAND_REALITY_VERIFICATION.md` (`FV006-TH-001` through `FV006-TH-003`); not re-performed here.
- **Severity:** N/A (positive confirmation, cross-referenced)
- **Why it matters / Cross-domain impact / Gate impact:** See `FV006-TH-001`–`003`.
- **Required owner:** N/A.
- **Blocking Development:** No.
- **Boss decision required:** No.

---

## Section B — The Tenant Concept (Cross-Referenced, Not Duplicated)

### FV006-GAP-007 — SaaS Tenant Boundary Has No Evidence Basis

- **Verification Area:** SaaS/multi-tenancy boundary (Charter §5.8)
- **TEAM B Artifact(s):** `14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md` §00, §02; flagged by TEAM B itself in `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md` §05 item 3 and in `18_...` §04
- **Approved Evidence/Baseline reference:** None in the GROUP A evidence package (TEAM B's own honest disclosure); approved-governance-mandate traceability (but not structural-definition traceability) independently confirmed in `11_SAAS_MULTI_COMPANY_THAILAND_REALITY_VERIFICATION.md` (`FV006-SAAS-001`)
- **Finding Status:** `GAP FOUND` (full detail and rationale in `FV006-SAAS-001` — not repeated here)
- **Severity:** Major
- **Why it matters / Cross-domain impact / Gate impact:** See `FV006-SAAS-001` in full.
- **Required owner:** Boss (baseline ratification decision), per `FV006-SAAS-001`.
- **Blocking Development:** Yes, for the Tenant-layer boundary model specifically (per `FV006-SAAS-001`).
- **Boss decision required:** Yes (per `FV006-SAAS-001`).

---

## Section C — Team A's Remaining Medium/Low Items (Consolidated)

Independently spot-checked against `TEAM_A/14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md` §03/§04 and TEAM B's disposition in `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` §02. None of the 14 items below was found, on independent review, to warrant elevation beyond TEAM B's own classification — each is either a genuine implementation-level compute detail already covered by an independently-designed business fact, or genuinely out of GROUP A's scope (Manufacturing/Repair/Accounting-presentation domains). Full narrative Finding-Model treatment is not repeated per item below (all 14 share the same "no elevation, not blocking" disposition); this table itself constitutes the required register entry for each so that none is silently dropped.

| Team A # | Item | TEAM B disposition | IBPV independent concurrence | Blocking |
|---|---|---|---|---|
| Medium #10 | `stock_move.is_in`/`is_out` column semantics | NOT MATERIAL TO CURRENT DESIGN | Concur — Movement Instruction source/destination model already covers the business fact | No |
| Medium #11 | `returned_move_ids` field definition | NOT MATERIAL TO CURRENT DESIGN | Concur — Reversal traceability independently elevated as a first-class requirement regardless of the field's exact definition | No |
| Medium #12 | `produce_line_ids` (likely MRP) | OUT-OF-SCOPE — REGISTER ONLY | Concur — Manufacturing domain, outside GROUP A | No |
| Medium #13 | Owning module for `sale_order_line.is_service` | NOT MATERIAL TO CURRENT DESIGN | Concur — Stock-vs-service determination independently derived from Product type attribute | No |
| Medium #14 | `product.type` literal `'product'` alongside `'consu'` | NOT MATERIAL TO CURRENT DESIGN | Concur | No |
| Medium #15 | Owning module for remaining `purchase_order_line` columns | NOT MATERIAL TO CURRENT DESIGN | Concur — material columns (`sale_line_id`, `purchase_request_id`) already resolved and designed elsewhere | No |
| Medium #16 | Full contents of `stock_dropshipping/models/stock.py` | NOT MATERIAL TO CURRENT DESIGN | Concur — dropship already designed at business-semantic level | No |
| Medium #17 | `stock.rule.Procurement` field typing | RESOLVED BY APPROVED EVIDENCE | Concur — already closed in evidence before TEAM B began | No |
| Medium #18 | WHT PND form-code correctness | OUT-OF-SCOPE — REGISTER ONLY | Concur — Accounting Core's own domain | No |
| Medium #19 | Thai district/sub-district address reach into delivery workflow | CONTROLLED CARRY-FORWARD | Concur — consolidated in Thailand register, already covered by `FV006-TH` series | No |
| Low #20 | MRP/Repair/Purchase-Requisition extension columns | OUT-OF-SCOPE — REGISTER ONLY | Concur | No |
| Low #21 | `stock_warehouse` MRP/repair/subcontracting columns | OUT-OF-SCOPE — REGISTER ONLY | Concur | No |
| Low #22 | `product_template` manufacturing/cold-chain columns | OUT-OF-SCOPE — REGISTER ONLY | Concur — likely an unrelated vertical | No |
| Low #23 | `num2words` Thai-locale linguistic/legal correctness | OUT-OF-SCOPE — REGISTER ONLY | Concur — Accounting Core presentation layer | No |

**Finding Status for this section as a whole:** `VERIFIED` (TEAM B's dispositions independently concurred with). **Severity:** N/A. **Blocking Development:** No. **Boss decision required:** No.

---

## Section D — New Open Items TEAM B Introduced During Design (File 18 §03, N1–N7)

### D.0 — The Three Deferred Policy Defaults (Explicit, Per Instruction)

These three are called out explicitly because they are the items TEAM B itself flags (file 20 §05 item 2) as requiring Boss/business confirmation before implementation-level design proceeds, and because the task of this register is to independently judge — not decide — whether each is safe to leave open at this Pre-Development Gate.

### FV006-GAP-008 (N1) — Canonical "Invoiced Quantity" Definition (Any-Non-Cancelled vs. Posted-Only)

- **Verification Area:** Data flow / financial-handoff quantity semantics (Charter §5.4)
- **TEAM B Artifact(s):** `11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md` §04; `18_...` §03 item N1
- **Approved Evidence/Baseline reference:** No TEAM A evidence establishes one canonical answer — this is a genuine business-policy choice, not an evidentiary gap. TEAM B records a reasoned, explicitly non-binding recommendation (posted-only) "for Boss review."
- **Finding Status:** `READY FOR BOSS DECISION`
- **Severity:** Moderate
- **Why it matters:** "Invoiced quantity" feeds the Billable-Now computation on both Sales and Purchase. If Sales and Purchase (or different Team C engineers) each pick a different definition without a single ratified answer, the two sides of the same commercial relationship could report inconsistent billing-eligibility figures — a real, if narrow, financial-reporting-consistency risk.
- **Cross-domain impact:** Accounting (billing/AR/AP figures), any future reporting layer that reads "Invoiced" quantity.
- **Gate impact / IBPV independent judgment on deferability:** **Safe to defer to Boss/business, with a scope condition.** This is a definitional/business-policy choice, not missing evidence for an existing rule and not a control-integrity gap — TEAM B has already designed the surrounding mechanism (the Billable-Now three-layer model) so that either answer plugs in without a structural redesign. It does **not** need to be resolved before Development starts broadly on GROUP A. It **does** need to be resolved before the specific Invoiced-quantity/Billable-Now computation logic is finalized for either Sales or Purchase — Team C should not build that specific computation against an assumed default. Recommend: Development may proceed on all other GROUP A work in parallel; this specific computation module should carry an explicit "policy pending" flag until Boss decides.
- **Required owner:** Boss (policy decision on TEAM B's recommendation).
- **Blocking Development:** No, for GROUP A generally. Yes, narrowly, for the Invoiced-quantity/Billable-Now computation module specifically.
- **Boss decision required:** Yes.

### FV006-GAP-009 (N2) — Default Value for the Over-Fulfillment/Over-Billing Policy

- **Verification Area:** Exception/correction control (Charter §5.7)
- **TEAM B Artifact(s):** `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §02/§03; `18_...` §03 item N2
- **Approved Evidence/Baseline reference:** No baseline default exists — the reference system is unguarded on both sides (`TEAM_A/16_FIT_GAP_CANDIDATE_PACK.md` item 10); this is a pure forward-looking business-policy choice. See also `FV006-FG-010` (Deliverable 12) for independent confirmation that the policy *mechanism* itself (as opposed to its default) was soundly and honestly designed.
- **Finding Status:** `READY FOR BOSS DECISION`
- **Severity:** Minor
- **Why it matters:** Because the mechanism is explicitly designed to be a per-business, per-direction configurable setting (block / warn-and-allow / allow-silently), the specific shipped default carries materially lower risk than a hardcoded, undocumented behavior would — a business can change it. The main risk is only during any interim period before a business first configures it.
- **Cross-domain impact:** Minor — a permissive default could allow silent over-delivery/over-receipt to persist until a business notices and configures the policy; a strict default could block legitimate edge cases (e.g., a small over-pack) until adjusted.
- **Gate impact / IBPV independent judgment on deferability:** **Safe to defer.** This is squarely a business/operational configuration choice with a designed mechanism already in place; it carries none of the charter's blocking characteristics (not a control-integrity issue, not an accounting-compliance issue, not a SoD issue, not untraceable). Recommend a conservative interim default (e.g., warn-and-allow) be used during Development/QA so the feature is testable, with Boss ratifying the shipped default before Production release — not before Pre-Development Gate.
- **Required owner:** Boss/business (final default value); TEAM B/Team C (interim QA default, non-binding).
- **Blocking Development:** No.
- **Boss decision required:** Yes, but only before Production release, not before Development starts.

### FV006-GAP-010 (N3) — Default Value for the Sales Confirmation Gate Policy

- **Verification Area:** Approval/control gate (Charter §5.5); also touches financial-control integrity via credit-exposure gating
- **TEAM B Artifact(s):** `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md` §04 (APR-003); `18_...` §03 item N3
- **Approved Evidence/Baseline reference:** `TEAM_A/03_SALES_CAPABILITY_MODEL.md` SO-32/33/36 (advisory-only, test-confirmed non-blocking in the reference system) — a real baseline behavior exists, but TEAM A explicitly frames adopting it by default as an inherited-default risk, not a validated correct choice (`TEAM_A/16_...` item 14)
- **Finding Status:** `READY FOR BOSS DECISION`
- **Severity:** Moderate
- **Why it matters:** Unlike N2 (a quantity-mismatch policy), this default touches whether a sales commitment can be confirmed while over a customer's credit exposure or without inventory availability — both are closer to financial-control and overselling risk than N2's data-quality concern. TEAM B correctly did not adopt the reference system's advisory-only behavior as a silent default, and correctly designed the policy as configurable per gate type (credit exposure, inventory availability) rather than a single switch.
- **Cross-domain impact:** Party credit-exposure data (Shared Master), Inventory Available/Forecasted quantities — both are read at confirmation time regardless of which default ships.
- **Gate impact / IBPV independent judgment on deferability:** **Safe to defer, but with a shorter fuse than N1/N2.** The mechanism (configurable, per-gate-type policy) is sound and does not itself need a chosen default to be built. Because this default sits closer to credit-risk and overselling control than the other two, this review recommends Boss ratify it earlier in the Development timeline than N1/N2 (e.g., before the Sales confirmation flow is functionally complete, not merely before Production release) — but building the surrounding Commercial Commitment confirmation flow, and the policy switch itself, does not need to wait on it.
- **Required owner:** Boss/business.
- **Blocking Development:** No, for starting Development of the confirmation-flow mechanism. Recommend it be resolved before that flow is considered feature-complete.
- **Boss decision required:** Yes.

### FV006-GAP-011 (N4) — Sales-Initiated RMA Affordance

- **Verification Area:** Exception/correction — commercial-side Return UX
- **TEAM B Artifact(s):** `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §05; `16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md` §04; `18_...` §03 item N4
- **Approved Evidence/Baseline reference:** TEAM A Fit-Gap #15's underlying rationale ("many SME businesses expect a salesperson-initiated RMA") is explicitly unsourced generalization, correctly not treated as evidence by TEAM B (Boss Gate §4.3) — already independently examined in `FV006-TH-002` (Deliverable 11), status `VERIFIED WITH CONDITIONS`
- **Finding Status:** `VERIFIED` — correctly left open as a real-user-validation item, not invented in either direction
- **Severity:** Minor
- **Why it matters:** The Inventory-owned Reversal mechanism is fully designed and functions regardless of how this is resolved; this is a UX/affordance question layered on top of a working mechanism, not a structural gap.
- **Cross-domain impact:** None current.
- **Gate impact:** None.
- **Required owner:** Real-user validation owner.
- **Blocking Development:** No.
- **Boss decision required:** No, unless/until real-user validation surfaces a confirmed need.

### FV006-GAP-012 (N5) — Cross-Company Handoff Mechanism (Single Transaction Spanning Multiple Legal Companies)

- **Verification Area:** Multi-company/SaaS boundary
- **TEAM B Artifact(s):** `14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md` §06; `18_...` §03 item N5
- **Approved Evidence/Baseline reference:** Thin, DB-level-only evidence (`TEAM_A/08_SOURCE_DATABASE_SEMANTIC_TRACEABILITY_MATRIX.md` §02), never functionally traced — already independently examined in `FV006-SAAS-004` (Deliverable 11), status `VERIFIED` (correct scope discipline)
- **Finding Status:** `VERIFIED` (scope discipline — correctly registered as not-designed rather than guessed at)
- **Severity:** Minor
- **Why it matters:** See `FV006-SAAS-004` for full detail.
- **Cross-domain impact:** Inter-company supply-chain scenarios within one Tenant remain undesigned; low current impact given how thin the evidence is.
- **Gate impact:** None at this time.
- **Required owner:** Future session, if a real inter-company transaction requirement is confirmed.
- **Blocking Development:** No.
- **Boss decision required:** No.

### FV006-GAP-013 (N6) — Late Supply / SLA Breach / Missing-Document Exception Handling

- **Verification Area:** Exception and recovery paths (Charter §5.7)
- **TEAM B Artifact(s):** `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §13; `18_...` §03 item N6
- **Approved Evidence/Baseline reference:** `NOT OBSERVED` anywhere in the TEAM A evidence package — no detection or grace-period handling was found in the reference system, and no independent business need was identified by TEAM B.
- **Finding Status:** `EVIDENCE MISSING` — correctly registered rather than invented
- **Severity:** Minor
- **Why it matters:** Inventing an SLA/lateness mechanism without any evidenced business need would violate the no-invented-certainty discipline this whole design package otherwise follows correctly. Registering it as an open item, rather than silently omitting it or inventing a mechanism, is the correct behavior.
- **Cross-domain impact:** None currently designed.
- **Gate impact:** None — no business flow currently depends on this being resolved.
- **Required owner:** Business, if a real SLA/lateness requirement is later identified.
- **Blocking Development:** No.
- **Boss decision required:** No, unless a business need is later confirmed.

### FV006-GAP-014 (N7) — Wrong-Item/Wrong-Quantity as a Distinct Exception Mechanism

- **Verification Area:** Exception and recovery paths
- **TEAM B Artifact(s):** `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §16; `18_...` §03 item N7
- **Approved Evidence/Baseline reference:** `NOT OBSERVED` as a distinct workflow in TEAM A evidence — handled, if at all, via existing edit-in-place/Reversal mechanisms already designed.
- **Finding Status:** `VERIFIED` (NOT MATERIAL TO CURRENT DESIGN — independently concurred; existing mechanisms are sufficient and no gap in coverage was found)
- **Severity:** Minor
- **Why it matters:** No additional capability is needed; the existing floor-guard and Reversal mechanisms already cover the practical cases.
- **Cross-domain impact:** None.
- **Gate impact:** None.
- **Required owner:** N/A.
- **Blocking Development:** No.
- **Boss decision required:** No.

---

## Section E — New Items This IBPV Session Independently Found (Not in TEAM B's Own Register)

These two items were not flagged by TEAM B as open; they are this review's own independent findings, developed in full in Deliverable 12 and consolidated here per this register's mandate to include everything found, not only what TEAM B itself flagged.

### FV006-GAP-015 — Asymmetric Cancellation Gate Closure Is an Unsupported Assumption (= `FV006-FG-012`)

- **Verification Area:** Exception/cancellation control, cross-domain into Accounting Core Financial Handoff
- **TEAM B Artifact(s):** `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §07 (gate asymmetry disposition); `17_...FIT_GAP_REGISTER.md` item 12
- **Approved Evidence/Baseline reference:** `TEAM_A/16_FIT_GAP_CANDIDATE_PACK.md` item 12 ("not resolvable from source alone"); `TEAM_A/04_PURCHASE_CAPABILITY_MODEL.md` PO-35; `TEAM_A/03_SALES_CAPABILITY_MODEL.md` CANC-04/05. Full analysis in `12_REQUIREMENT_EVIDENCE_TO_DESIGN_TRACEABILITY_AUDIT.md`, `FV006-FG-012`.
- **Finding Status:** `CONFLICT FOUND`
- **Severity:** Major
- **Why it matters:** TEAM B closed an item TEAM A explicitly found unresolvable from evidence, using a business-semantic rationale that mischaracterizes the actual evidenced asymmetry (see `FV006-FG-012` for the full textual comparison). This is the most severe item in this register that TEAM B itself did not flag as open.
- **Cross-domain impact:** Sales↔Accounting Core Financial Handoff boundary — an outstanding posted customer invoice against a cancelled sales order has no defined treatment anywhere in this design package.
- **Gate impact:** Recommend re-classifying Fit-Gap item 12 from closed (`ADAPT`) to `EVIDENCE MISSING` / `CONTROLLED CARRY-FORWARD`, pending an explicit Boss/business decision on whether Sales needs a cancellation gate symmetric to Purchase's.
- **Required owner:** Boss (business-policy decision), TEAM B (design custodian once directed).
- **Blocking Development:** **Yes**, for the Sales-side cancellation-gate design specifically. Does not block the rest of GROUP A.
- **Boss decision required:** Yes.

### FV006-GAP-016 — Physical-Count-vs-On-Hand Schema Separation Remains Functionally Open (= `FV006-FG-007`)

- **Verification Area:** Inventory physical-fact modeling
- **TEAM B Artifact(s):** `03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md` §00; `17_...FIT_GAP_REGISTER.md` item 7
- **Approved Evidence/Baseline reference:** `TEAM_A/16_FIT_GAP_CANDIDATE_PACK.md` item 7. Full analysis in `12_REQUIREMENT_EVIDENCE_TO_DESIGN_TRACEABILITY_AUDIT.md`, `FV006-FG-007`.
- **Finding Status:** `VERIFIED WITH CONDITIONS`
- **Severity:** Moderate
- **Why it matters:** TEAM B's fact-type classification is sound, but the practical schema question TEAM A actually raised (should count-in-progress and settled on-hand be structurally separate) is not decided by it, despite being labeled "resolved."
- **Cross-domain impact:** None beyond Inventory.
- **Gate impact:** Recommend re-labeling as `CONTROLLED CARRY-FORWARD`, scoped to the schema-separation question only.
- **Required owner:** TEAM B (documentation correction); Team C (implementation-time schema decision).
- **Blocking Development:** No.
- **Boss decision required:** No.

---

## Section F — Summary

### F.1 — Counts by Status

| Status | Count | Items |
|---|---|---|
| VERIFIED | 6 | GAP-004(partial)\*, GAP-006, Section C (14 items, 1 row), GAP-011, GAP-012, GAP-014 |
| VERIFIED WITH CONDITIONS | 2 | GAP-004, GAP-016 |
| GAP FOUND | 1 | GAP-007 (Tenant, cross-referenced) |
| EVIDENCE MISSING | 3 | GAP-001, GAP-002, GAP-013 |
| CONFLICT FOUND | 1 | GAP-015 |
| READY FOR BOSS DECISION | 3 | GAP-008 (N1), GAP-009 (N2), GAP-010 (N3) |

\*GAP-004 is counted once, carrying a mixed VERIFIED/VERIFIED WITH CONDITIONS disposition as described in its own entry.

### F.2 — Counts by Severity

| Severity | Count |
|---|---|
| Critical | 1 (GAP-001 — approval internal-logic evidence gap) |
| Major | 2 (GAP-007 — Tenant boundary; GAP-015 — cancellation-gate closure) |
| Moderate | 4 (GAP-004, GAP-008, GAP-010, GAP-016) |
| Minor | 9 (GAP-002, GAP-003, Section C's 14-item consolidated block, GAP-009, GAP-011, GAP-012, GAP-013, GAP-014, GAP-006) |

### F.3 — Blocking Development (per Charter §9)

Only two items in this entire register independently meet the charter's Pre-Development Blocking Rule at Critical/Major severity with a direct textual match to a blocking category:

1. **`FV006-GAP-001`** (internal approval workflow/permission/SoD logic) — blocks the internal-logic portion of the Sequential Level-Based Approval Control specifically. Matches: "unresolved security/permission/SoD design issue."
2. **`FV006-GAP-015`** (asymmetric cancellation gate closure) — blocks the Sales-side cancellation-gate design specifically. Matches: "unverified state/event transition that affects financial/control integrity," with a likely "unresolved accounting/compliance impact" pending Accounting Core confirmation.

One additional item carries a Major severity and a Boss-decision requirement without itself meeting the blocking bar in the same direct way, already fully adjudicated in Deliverable 11:

3. **`FV006-GAP-007`** (Tenant boundary, cross-referenced to `FV006-SAAS-001`) — blocks the Tenant-layer boundary model specifically.

No other item in this register is found, on independent review, to justify a project-wide `NOT READY FOR DEVELOPMENT` status. The three deferred policy defaults (N1/N2/N3) are each independently judged **safe to defer** to Boss/business policy decision at this Pre-Development Gate, with scoped conditions on *when* (not *whether*) each must be finalized relative to the specific computation/flow it feeds — none of the three rises to the charter's blocking bar on its own, because in each case the surrounding mechanism is soundly designed and only a configurable value, not a missing control or an evidentiary gap, remains open.
