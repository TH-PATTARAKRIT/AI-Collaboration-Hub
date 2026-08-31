# DOMAIN_01 Thailand COA Closure — Evidence Index

Date: 2026-08-31 (Round 2 correction)
Jira: ERPPLUS-132
Boss Authorization Commit: `e8cc4d942d7f5c611ca3add0266c39196515b636`
Boss SaaS Architecture Amendment Commit: `c084a741b22e3352992fbeb0c212cbd1463efb92`
Boss Cross-Gate SaaS Invariants Ruling: `e16b29f35d8011723a6e2593994bc226870d9fd7`
COA-G01 Round 1 Evidence Package Commit: `00daa7d74478e59e9516593811b9e8fb5344bd2b`
Commit `c530138fd33b5651d56e3542be6d35f8d3d72111`: preserved, but reclassified — see below.
COA-G01 Round 2 Remediation: see `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_G01_EVIDENCE/COA_G01_CURRENT_STATE_ADDENDUM_R2.md`

## Round 2 correction notice (2026-08-31)

Commit `c530138` and the immediately following index update (superseded by this correction) declared `ChatGPT Independent Evidence Review = PASS` and `COA-G01 blocking evidence gaps = 0`. A full provenance investigation (Round 2 session `SMEPLUS-26-08-30-COA-G01R2-001`) found **no separate independent review artifact, no PMO artifact, and no Jira record** supporting that declaration — the PASS text was written inline, in the same commit, by the same unsigned author, 20 seconds after the evidence it purports to review. This is classified `CONFLICTING EVIDENCE / UNVERIFIED SELF-DECLARED RESULT` and is **not** used as Gate closure evidence. Full rationale: `COA_G01_CURRENT_STATE_ADDENDUM_R2.md`; conflict record: `COA_G01_SOURCE_CONFLICT_REGISTER.md` C-07. Commit `c530138` itself is preserved unmodified — only this index's characterization of it is corrected.

## Current Gate

`COA CLOSURE WORKSTREAM = OPEN / AUTHORIZED BY BOSS`

Current execution Gate:

`COA-G01 — Source Baseline Reconciliation`

Round 2 remediation package is complete for independent review. This index does **not** declare that independent review has occurred.

`ChatGPT Independent Evidence Review = NOT YET PERFORMED (the c530138/8fceca0 self-declaration is not accepted as this review — see correction notice above)`

`COA-G01 Gate Status = HOLD / CORRECTION REQUIRED + EVIDENCE REQUIRED` (per Boss directive `COA-G01R2-CORR1` and `COA_G01_GATE_REPORT.md` §16 — genuine open items unchanged: C-01, C-02, C-06, Class E/F, SI-10, N-01; CORR1 correction cycle applied and closed, see `COA_G01_CORR1_POST_PUBLICATION_CLOSURE.md`)

`Boss Final COA-G01 Gate Decision = PENDING`

`COA-G02 = NOT STARTED / BLOCKED PENDING BOSS AUTHORIZATION`

No later Gate receives execution credit from this G01 review.

## Cross-Gate SaaS Invariant Control

**SI-01 through SI-10 apply to every COA Closure Gate: G01, G02, G03, G04, G04S, G05, G06, G07 and G08.**

1. `SI-01 Tenant context is mandatory.`
2. `SI-02 Company context is mandatory where company-scoped.`
3. `SI-03 Standard Template is not tenant-owned mutable data.`
4. `SI-04 Tenant customization cannot modify the published Standard Template.`
5. `SI-05 Account Code / Name is not canonical identity.`
6. `SI-06 Published Template Version is immutable.`
7. `SI-07 Upgrade is explicit, previewable and auditable.`
8. `SI-08 No cross-tenant COA access.`
9. `SI-09 Company customization must preserve canonical reporting semantics.`
10. `SI-10 SaaS Core must not hard-code Thailand-specific source architecture.`

Every Gate Report must include a `SAAS INVARIANT COMPLIANCE` matrix covering SI-01..SI-10 with evidence, owner, reviewer, status and Gate impact.

Enforcement:

- applicable SI violation -> `FAIL / FROZEN`;
- applicable SI evidence missing -> `HOLD`;
- `N/A` requires explicit justification;
- no Gate may be declared PASS/FROZEN/READY FOR HANDOFF/COMPLETE while an applicable SI is unresolved.

## Revised Gate Register

| Gate | Owner Role | Evidence | Reviewer | Status | Gate Impact |
|---|---|---|---|---|---|
| COA-G01 Source Baseline Reconciliation | Team A Evidence + controlled reconciliation (Round 1 + Round 2) | `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_G01_EVIDENCE/` (21 files: 15 Round 1 + 6 Round 2) + SI-01..SI-10 matrix | ChatGPT (pending — not yet performed) | **HOLD / EVIDENCE REQUIRED** (see `COA_G01_GATE_REPORT.md` §15.3) | **Blocks G02 until Boss decision** |
| COA-G02 Base COA Kernel Discovery | Team B Design after G01 approval | TBD + SI-01..SI-10 compliance evidence required | ChatGPT | NOT STARTED | Blocks G03/G04 |
| COA-G03 AI Semantic Consolidation | Team B Design | TBD + SI-01..SI-10 compliance evidence required | ChatGPT | NOT STARTED | Blocks canonical freeze |
| COA-G04 Account Type & Account Group Architecture | Team B Design | Existing 19-type Boss ruling + new artifact TBD + SI compliance | ChatGPT | PARTIAL BASELINE / OPEN | Blocks G04S |
| **COA-G04S SaaS COA Tenancy, Provisioning, Versioning & Upgrade Architecture** | Team B SaaS/Accounting Architecture | Boss amendment `c084a741...` + execution artifact TBD + SI compliance | ChatGPT | **BOSS AUTHORIZED / NOT EXECUTED** | **Blocks G05 and later freeze** |
| COA-G05 Financial Statement Taxonomy | Team B Design | External statement evidence + mapping TBD + SI compliance | ChatGPT | OPEN / NOT EXECUTED | Blocks COA freeze |
| COA-G06 Thailand Tax Accounting Controls | Team A evidence + Team B design | TBD + SI compliance | ChatGPT | OPEN / NOT EXECUTED | Blocks COA freeze |
| COA-G07 Multi-company & Dimension Proof | Team B Design / Verification | TBD + SI compliance | ChatGPT | NOT STARTED | Blocks PMO |
| COA-G08 Independent Audit + PMO + Boss Freeze | ChatGPT -> PMO -> Boss | Full SI-01..SI-10 final compliance matrix required | Boss final | NOT OPEN | Final handoff gate |

## COA-G01 Evidence Summary

Reconciled source layers:

- Team A Accounting Core deep research and direct source anchors.
- Authorized Accounting Core source semantics.
- Thailand localization source: 144 rows / 15 instantiated Account Types.
- Boss-approved Odoo18 workbook: 389 rows / 14 observed Account Type labels; directly re-verified in connected Drive during G01 execution.
- Boss Thai COA business requirements.
- Thai financial-statement presentation principles and official Thai reporting anchors at G01 classification level.
- Existing Boss / PMO / ChatGPT audit evidence.
- Primary Thai regulatory sources at concept level for VAT/WHT/CIT/reporting claims.

Reconciled target rule:

- Core source universe = 19 Account Types.
- `l10n_th` observation = 15 Account Types.
- Odoo18 workbook observation = 14 labels.
- SMEsPlus Local Thailand target = 19 ACTIVE Account Types by Boss ruling.

Source conflicts are preserved and routed, not silently corrected. Key examples include inconsistent accumulated-depreciation source classifications and source tax accounts under generic Account Types.

`COA-G01 open conflicts = 7 (C-01..C-07, see COA_G01_SOURCE_CONFLICT_REGISTER.md); open unknowns = 5 (N-01..N-05); SI-10 = HOLD at classification scope; Class E/F = EVIDENCE_MISSING.`

`COA-G01 SI-01..SI-09 = PASS at G01 classification scope; SI-10 = HOLD even at classification scope — COA-G01 is therefore not reportable as PASS per the Audit Veto rule below.`

This does not claim G04S/G07 runtime or architecture proof is complete.

## COA-G04S Mandatory Evidence Scope

Before G05 can be opened for closure credit, G04S must evidence:

- Tenant isolation
- Company isolation
- Standard Thai COA Template vs Company COA Instance separation
- Tenant/Company provisioning
- Template versioning
- Tenant customization boundary
- Controlled upgrade / delta handling
- Backward compatibility
- Canonical identity independent from Account Code
- Company-maintainable Account Group behaviour
- Multi-company sharing/separation rules
- Role/permission boundary
- Audit/change history
- Migration mapping compatibility
- Canonical reporting continuity after customization/upgrade

## Audit Veto Control

The Cross-Gate ruling is a mandatory audit control, not a recommendation.

Any applicable SI violation or unresolved evidence gap prevents the affected Gate from receiving closure credit and prevents final COA handoff unless Boss separately issues a controlled exception ruling.

## Governance Red Flags / Carry-Forward

- Jira Assignee = UNASSIGNED.
- Due Date = TBD.
- Exact Base Kernel count = TBD / EVIDENCE REQUIRED; `~32` remains a working expectation only.
- Exact final canonical COA count = TBD / EVIDENCE REQUIRED.
- Account-by-account semantic consolidation = NOT STARTED.
- Exact Financial Statement taxonomy = NOT EXECUTED.
- Exact VAT/WHT/CIT mapping = NOT EXECUTED.
- COA-G04S execution evidence = NOT YET AVAILABLE.
- Multi-company / cross-tenant proof = NOT EXECUTED.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
