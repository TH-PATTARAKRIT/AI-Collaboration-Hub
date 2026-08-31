> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B Corrective Rework (CORR-008)

# 23 — TEAM B CORR-008 SAAS/TENANT BASELINE RECONCILIATION

Session: `SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-008`
Scope: CORR8-09 only (`FV006-SAAS-001`, `FV006-SAAS-003`, `FV006-XDF-006`, `FV006-GAP-007`)

This is the mandatory dedicated SaaS/Tenant evidence artifact required by CORR-008 §8. It does **not** claim
runtime Tenant isolation is implemented or proven — this is canonical design/traceability work only, consistent
with the evidence-boundary discipline already established for the analogous Domain-01 Accounting Core work cited
below (classification-scope vs. execution-scope are two different questions; this artifact answers only the
former for GROUP A).

## 1 — Exact Formal IBPV Finding Reproduction

### `FV006-SAAS-001` (D11, Major, `GAP FOUND`)
Independently confirmed by direct grep of `00_Project_Governance/`: the approved baselines
(`STATE01_PROJECT_CHARTER_v1.0.md`, `STATE01_SCOPE_PRINCIPLES_RACI_v1.0.md`, `ARCHITECTURE_GOVERNANCE_STANDARD.md`)
mandate that SMEsPlus be multi-tenant SaaS — the *need* for a Tenant concept is traceable. No governance document
defines what a Tenant *is* structurally, its relation to Legal Company, or its isolation mechanics. TEAM B's file
14 is the first artifact in the corpus to attempt that structural definition, and discloses this itself.
**Blocks**: the Tenant-layer boundary model specifically. **Required owner**: Boss (baseline-ratification
decision).

### `FV006-SAAS-003` (D11, Moderate, `GAP FOUND`)
File 14 §02's absolute "no fact crosses Tenants" rule was not re-asserted per-row in its own shared-master
sharing table (§05), risking a reader who consults §05 in isolation missing the Tenant-scoping boundary at the
exact point an implementer is most likely to be reading.

### `FV006-XDF-006` (D03, Critical, `EVIDENCE MISSING`)
A second, differently-scoped reviewer independently corroborated the same underlying gap from the cross-domain
angle: the Tenant boundary layer sits above Company/Branch, which every Sales and Purchase line's access-scoping
rule is defined relative to, with no approved baseline on either side of the new layer. Named the single most
consequential open item that review identified.

### `FV006-GAP-007` (D13, Major, consolidated reference)
Consolidates `FV006-SAAS-001` into the Design Conflict/Open Gap Register; full detail and rationale carried by
reference to `FV006-SAAS-001`, not repeated.

## 2 — Current Boss Directive (CORR-008 Reframing)

Per the CORR-008 corrective prompt §2.4 and §4 (CORR8-09): **the project does not need a new decision on whether
SMEsPlus should be Multi-Tenant. Tenant context is a mandatory cross-module SaaS invariant; company-scoped
operations require Tenant + Company context.** The defect is therefore reframed as a baseline-traceability and
structural-classification defect, not a request to re-approve Multi-Tenant SaaS. This directive is consistent
with, and generalizes, the Boss-approved SaaS Context Clarification already recorded for Domain 01 (Accounting
Core) — see §3 below — extended here to GROUP A as an existing cross-module control, not a new per-module
approval request.

## 3 — Existing Controlled SaaS/Tenant Sources and Their Scope

| Source | Status | What it controls | Scope applicable to GROUP A |
|---|---|---|---|
| `State_01_Project_Identity/STATE01_PROJECT_CHARTER_v1.0.md` §5 | Approved Baseline, Boss-approved 2026-07-13 | "SaaS Foundation and tenant control" is in scope | Mandate only — establishes *that* a Tenant concept must exist |
| `State_01_Project_Identity/STATE01_SCOPE_PRINCIPLES_RACI_v1.0.md` (Product Boundary) | Approved Baseline, Boss-approved 2026-07-13 | "tenant/company/user control" is in scope | Mandate only |
| `ARCHITECTURE_GOVERNANCE_STANDARD.md` (Architecture Principles) | Approved | "Multi-Tenant by Design" is a named architecture principle | Mandate only |
| `BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AQ_BOSS_SAAS_CONTEXT_CLARIFICATION_AND_G01_REMEDIATION_AUTHORIZATION.md` §3 | Recorded controlled ruling (2026-08-30), classification/definition boundary only, not execution proof | States the operational context rule: (1) Platform Template administration = Platform Context; (2) tenant-owned or tenant-access operation = Tenant Context mandatory; (3) company-scoped operation = Tenant Context + Company Context mandatory; (4) a Platform operation must not impersonate a Tenant operation; (5) a Tenant/Company operation must not access or mutate Platform-owned data | **Items (2) and (3) only** are the cross-module SaaS/context invariant applicable to GROUP A (mandatory Tenant context for tenant-facing operations; mandatory Tenant+Company context for company-scoped operations). Items (1), (4), (5) concern the Platform-Context / Published-Standard-Template axis, which is COA-G01-specific (Domain 01 Accounting Core's Chart-of-Accounts template administration) and has **no GROUP A counterpart** — Sales/Inventory/Purchase has no equivalent "Platform Template" concept. **Not imported into GROUP A.** |
| `COA_G01_SAAS_INVARIANT_COMPLIANCE.md` (Domain 01, SI-01..SI-10 matrix) | PASS/VERIFIED at classification scope for SI-01 (Tenant context mandatory) and SI-02 (Company context mandatory where company-scoped); HOLD at execution scope for both (COA-G04S) | Demonstrates the same cross-module invariant (SI-01/SI-02) already passed classification-scope review for a different domain | Confirms the invariant is a project-wide, cross-module control already established outside GROUP A — GROUP A applies the same invariant, it does not newly invent it. **SI-03 through SI-10 (Template, versioning, Tax-Branch-adjacent items) are Domain-01-specific and are explicitly not imported.** |
| `COA_G01_SAAS_CONTEXT_BOUNDARY_REGISTER.md` | Classification complete at G01 scope | Applies the AQ ruling to specific Domain-01 concepts (COA Template publishing, provisioning, upgrade) | Domain-01-specific worked examples; not directly applicable to GROUP A facts, but the underlying two-item rule (Tenant mandatory; Tenant+Company mandatory for company-scoped ops) is the same rule GROUP A applies |

**Evidence-boundary rule applied throughout this artifact** (per CORR-008 §2.4): only the cross-module
Tenant/Company context rule (AQ §3 items 2–3, and SI-01/SI-02) is treated as applicable authority for GROUP A.
Platform Context, Standard Template administration, Template versioning (SI-03/SI-04/SI-06/SI-07), and any
Thai-Tax-Branch-adjacent finding (the local "Finding S5," `SI-10`) are Domain-01/Accounting-specific and are
**not** imported into this reconciliation — GROUP A has no analogous concept for any of them, and no separate
evidence makes them applicable here.

## 4 — Statement-by-Statement Reconciliation of TEAM B File 14

Every material Tenant/Company-scope rule in `14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md`, classified per the
five-category scheme (CORR-008 §4, item 3):

| # | Statement | File 14 location | Classification | Basis |
|---|---|---|---|---|
| 1 | A Tenant concept must exist as the top-level SaaS isolation boundary above Legal Company | §01, §02 | `EXISTING BOSS-CONTROLLED SAAS INVARIANT` | STATE01 Project Charter §5; STATE01 Scope Principles RACI; Architecture Governance Standard "Multi-Tenant by Design"; independently re-confirmed by Formal IBPV D11 §A.0 direct grep |
| 2 | Tenant is a *hard* layer (no fact of any kind crosses it under any configuration) — the specific isolation-strength choice | §02 | `TEAM B CANONICAL DESIGN CHOICE WITH EXPLICIT RATIONALE` | Not separately evidenced as a structural definition; TEAM B's own reasoned elaboration of item 1's mandate, self-disclosed as such in the pre-correction file 14 §00/§02 ("independently reasoned," "new capability requirement, not inferred from evidence") |
| 3 | Accessible-branch resolution must be Tenant-scoped first, Company-hierarchy-scoped second | §03 | `TEAM B CANONICAL DESIGN CHOICE WITH EXPLICIT RATIONALE` | The concrete enforcement mechanism implementing item 1's mandate at the one place Sales/Purchase touch Company/Branch scope; not itself evidenced, but the necessary consequence of the mandate combined with the project's zero-tolerance tenant-leakage defect policy (`PROJECT_CONSTITUTION.md` line 171; `POLICIES/TEST_CASE_TOLERANCE_AND_ZERO_DEFECT_POLICY.md` line 49, both independently confirmed by Formal IBPV D11 §A.0) |
| 4 | Legal Company/Branch hierarchy (Branch = child Company record; currency matches across hierarchy; hierarchy position immutable) | §03 | `EVIDENCE-SUPPORTED GROUP A DESIGN ELABORATION` | Cited to `01` §12, `04` §02 — Formal IBPV `FV006-SAAS-002` found this citation-complete (VERIFIED WITH CONDITIONS, condition being independent re-opening of files 01/04, unchanged by CORR-008) |
| 5 | Warehouse/Location layer (company-owned, immutable after creation; Location optionally shared) | §04 | `EVIDENCE-SUPPORTED GROUP A DESIGN ELABORATION` | Adopted unmodified from `04` §05, itself evidence-cited |
| 6 | Per-concept sharing defaults (11 Shared Master concepts) | §05 | `EVIDENCE-SUPPORTED GROUP A DESIGN ELABORATION` (each row cites its own evidence item) | TEAM A source evidence per concept, as originally cited in file 14 §05 |
| 6a | "Always within-Tenant" qualifier applied to every row of the §05 table (CORR-008 addition, closes `FV006-SAAS-003`) | §05 | `TEAM B CANONICAL DESIGN CHOICE` | Direct restatement, at point of use, of item 2's already-classified rule — not new evidence, a consistency correction |
| 7 | Cross-Company handoff mechanism (single transaction spanning >1 Company within a Tenant) | §06 | `CONTROLLED ASSUMPTION / REQUIRES FUTURE VERIFICATION` | Evidence thin (only DB-level inter-company columns, `08` §02, never functionally traced); Formal IBPV `FV006-SAAS-004` independently confirmed this scope discipline as correct, not a defect |
| 8 | Whether the Company/Branch hierarchy maps onto real Thai SME legal/operating structures | §07 (cross-ref `16` item 9) | `CONTROLLED ASSUMPTION / REQUIRES FUTURE VERIFICATION` | TEAM A evidence classifies this `Unknown / Requires Real-User Validation`; carried forward unresolved, unchanged by CORR-008 |

**No statement above is classified `DESIGN DECISION BLOCKED AT THIS POINT`.** No new, material, necessary-for-
correctness structural rule was found that cannot currently be derived from an approved control or safely held as
a controlled assumption — the CORR-008 §4 item 8 escalation path is therefore not triggered.

## 5 — Cross-File Tenant/Company Scope Sweep

Every GROUP A TEAM B file (01–21) was searched for Tenant/Company/Branch/Warehouse scope statements. Results:

| File | Tenant/Company mentions found | Consistency result |
|---|---|---|
| `01_TEAM_B_SCOPE_BASELINE_AND_INPUT_REGISTER.md` | One index reference ("Multi-company/tenant/branch/warehouse boundary semantics" listed as an in-scope deliverable area) | Consistent — an index entry, not a structural claim |
| `02_CANONICAL_CAPABILITY_AND_DOMAIN_BOUNDARY_MODEL.md` | One capability-catalog row (C12, "Company/Branch Structure... What legal/tenant boundary does this transaction belong to?") | Consistent — uses "tenant boundary" loosely as a synonym for the legal-entity boundary being catalogued, not a competing structural claim; no correction needed |
| `04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md` §06 | Company/Branch defined as "a legal-entity/tenant hierarchy," cross-references file 14 for SaaS/Tenant detail | Consistent — explicitly defers structural detail to file 14 rather than asserting its own competing definition |
| `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` §07 | References file 14 for Company/Branch scoping in the multi-warehouse/company scenario | Consistent — pure cross-reference |
| `09_CANONICAL_BUSINESS_EVENT_CATALOG.md` §05 | "Company/Branch accessible-scope" read by Sales/Purchase, governed by file 14 | Consistent — pure cross-reference |
| `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §12 | Cross-warehouse/cross-company case handling deferred to file 14 | Consistent — pure cross-reference |
| `16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md` item 9 | The Company/Branch-to-Thai-SME-structure mapping question, `Unknown / Requires Real-User Validation` | Consistent — this is reconciliation item 8 above; unchanged, correctly still open |
| `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` §04 | The Tenant-concept note, now corrected by CORR-008 (see §6 below) | Corrected — see §6 |
| `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md` | Deliverable-index row for file 14, citing `01` §12 and `05` Scenario 11 as its evidence sources | Consistent — unchanged, still accurate as an index entry |
| `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md` §05 item 3 | Original self-flag that the Tenant concept has no evidence basis | Superseded by this reconciliation — see the supersession notice added to file 20 in this corrective session; the original disclosure is retained, not deleted |

**No file was found asserting a structural claim about Tenant/Company scope that contradicts file 14's
corrected classification.** Every other file either defers to file 14 or uses "tenant"/"company" in a way
consistent with the reconciliation above. No cross-file contradiction required correction beyond file 14 itself
and the two register updates (18, 20) already made.

## 6 — Correction to `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` §04

The pre-correction note stated only that the Tenant concept "is not an Unknown or a carry-forward — it is a new
capability requirement." This was accurate but incomplete: it did not distinguish the mandate (traceable) from
the structural shape (not independently verified against a baseline). CORR-008 corrects the note in place
(retaining the original text, appending the correction) rather than deleting it, per the discipline of correcting
wording/classification instead of asking Boss to re-approve the existence of Tenant (CORR-008 §4 item 7).

## 7 — Cross-Tenant Isolation Invariant (Canonical Design Level Only)

Restated once, for clarity, as the design-level (not runtime-proof) statement this reconciliation confirms is
consistently represented across GROUP A:

> **No GROUP A canonical design rule — in file 14 or any other file in this folder — permits a Commercial
> Commitment, Supply Commitment, Movement Instruction/Execution, Stock Position, Reservation, Reversal,
> Traceability Unit, Handling Unit, Financial Handoff record, or any Shared Master fact to be visible or
> referenceable across two different Tenants, under any configuration.** Tenant context is mandatory for every
> tenant-facing operation; Tenant + Company context is mandatory for every company-scoped operation
> (`14` §01–§03). This is a canonical design invariant, not a claim that any runtime system currently enforces
> it — enforcement proof is out of scope for this design tier, exactly as the analogous Domain-01 SI-01/SI-02
> classification-scope-vs-execution-scope distinction (§3 above) already establishes as the correct evidence
> boundary for this kind of claim.

## 8 — Residual Structural Unknowns

None new. The two pre-existing `CONTROLLED ASSUMPTION / REQUIRES FUTURE VERIFICATION` items (reconciliation
items 7 and 8, §4 above) remain open, unchanged by CORR-008 — they were correctly registered before this
correction and are reclassified here using CORR-008's five-category scheme for consistency, not newly
discovered.

## 9 — Conclusion: Is the IBPV Traceability Defect Closed?

**Yes, for the traceability/classification question the finding actually raises.** `FV006-SAAS-001`,
`FV006-SAAS-003`, `FV006-XDF-006`, and `FV006-GAP-007` all identify the same underlying defect from different
angles: TEAM B's file 14 presented a self-disclosed new structural design choice without distinguishing it,
in wording and classification, from the separately traceable mandate that a Tenant concept must exist. That
defect is closed by:

1. §00/§02/§03/§05/§08 of the corrected file 14, which now classify every material statement per the five-category
   scheme rather than leaving the mandate and the elaboration undifferentiated;
2. §05's per-row restatement of the Tenant-scoping boundary, closing `FV006-SAAS-003` specifically;
3. this artifact's statement-by-statement reconciliation and cross-file sweep, finding no remaining
   unclassified or contradictory statement.

**What remains explicitly NOT claimed, consistent with CORR-008's authorization boundary**: this closure does not
constitute Boss re-approval of Multi-Tenant SaaS (never re-opened), does not constitute a Formal IBPV PASS (Formal
IBPV re-verification remains mandatory and independent), and does not constitute proof that Tenant isolation is
implemented or enforced in any running system (no such system exists at this design tier).
