# DOMAIN_01 Thailand COA Closure — Evidence Index

Date: 2026-08-31 (CORR4 correction)
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

Round 2 remediation package, CORR1 and CORR2 have been independently re-audited by ChatGPT (commit `8f5fa522a3f1a3553584eb5d5063238eec6a88a2`, `CHATGPT_AUDIT/DOMAIN_01_ACCOUNTING_CORE_AE_COA_G01_CORR2_INDEPENDENT_REAUDIT.md`). This index does **not** declare that this review resulted in PASS — its disposition was `CORR2 TARGETED CORRECTIONS = PARTIALLY ACCEPTED`, `HOLD / CORRECTION REQUIRED`, driving the authorized CORR3 pass below.

`ChatGPT Independent Evidence Review = PERFORMED for CORR2 (commit 8f5fa52, result: HOLD / CORRECTION REQUIRED — 3 findings AUD2-01..03) and CORR3 (commit f37a3076..., result: PASS / VERIFIED for CORR3 targeted remediation, AUD2-01..03 all CLOSED); CORR4 itself is pending its own independent re-audit as of this commit (the c530138/8fceca0 self-declaration remains rejected — see correction notice above, not accepted as any part of this review chain)`

`COA-G01 Gate Status = HOLD / EVIDENCE REQUIRED` (per Boss directive `COA-G01R2-CORR4` and `COA_G01_GATE_REPORT.md` §19 — the CORR1-3 correction cycles are closed and independently verified PASS; CORR4 recovered the workbook (N-01 RESOLVED), ported all local STATE03/T1-T9/STEP0303R2-R5 evidence (C-01/N-02 RESOLVED), resolved SI-10 to PASS at classification scope, and partially resolved Class E — genuine open items now: N-04/Class F (`ACCESS_DENIED`), N-05 (`STEP0303R2` cause `UNKNOWN`), C-02 cause, C-03 substantive status; see `COA_G01_CORR4_POST_PUBLICATION_CLOSURE.md`)

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
| COA-G01 Source Baseline Reconciliation | Team A Evidence + controlled reconciliation (Round 1 + Round 2 + CORR1-4) | `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_G01_EVIDENCE/` — **96 files physically present** (32 top-level Markdown + 63 ported `COA_G01_SOURCE_PORT/STATE03_LOCAL/` files + 1 checksum file); **99 total operational SHA-256 entries** (95 local + `AQ` + 3 `COA_STANDARD` documents), recomputed CORR4, 2026-08-31 + SI-01..SI-10 matrix (10/10 PASS at classification scope) | ChatGPT (CORR2 audit: HOLD/CORRECTION REQUIRED; CORR3 audit: PASS/VERIFIED, AUD2-01..03 CLOSED; CORR4 pending its own re-audit) | **HOLD / EVIDENCE REQUIRED** (see `COA_G01_GATE_REPORT.md` §19) | **Blocks G02 until Boss decision** |
| COA-G02 Base COA Kernel Discovery | Team B Design after G01 approval | TBD + SI-01..SI-10 compliance evidence required | ChatGPT | NOT STARTED | Blocks G03/G04 |
| COA-G03 AI Semantic Consolidation | Team B Design | TBD + SI-01..SI-10 compliance evidence required | ChatGPT | NOT STARTED | Blocks canonical freeze |
| COA-G04 Account Type & Account Group Architecture | Team B Design | Existing 19-type Boss ruling + new artifact TBD + SI compliance | ChatGPT | PARTIAL BASELINE / OPEN | Blocks G04S |
| **COA-G04S SaaS COA Tenancy, Provisioning, Versioning & Upgrade Architecture** | Team B SaaS/Accounting Architecture | Boss amendment `c084a741...` + execution artifact TBD + SI compliance | ChatGPT | **BOSS AUTHORIZED / NOT EXECUTED** | **Blocks G05 and later freeze** |
| COA-G05 Financial Statement Taxonomy | Team B Design | External statement evidence + mapping TBD + SI compliance | ChatGPT | OPEN / NOT EXECUTED | Blocks COA freeze |
| COA-G06 Thailand Tax Accounting Controls | Team A evidence + Team B design | TBD + SI compliance | ChatGPT | OPEN / NOT EXECUTED | Blocks COA freeze |
| COA-G07 Multi-company & Dimension Proof | Team B Design / Verification | TBD + SI compliance | ChatGPT | NOT STARTED | Blocks PMO |
| COA-G08 Independent Audit + PMO + Boss Freeze | ChatGPT -> PMO -> Boss | Full SI-01..SI-10 final compliance matrix required | Boss final | NOT OPEN | Final handoff gate |

## COA-G01 Evidence Summary

**CORR3 correction notice (2026-08-31, finding `AUD2-02`):** the "Reconciled source layers" list immediately below previously stated the workbook was *"directly re-verified in connected Drive during G01 execution"* and listed Thai COA business requirements / financial-statement presentation as if reconciled. Both statements originated from the rejected `c530138`/`8fceca0` self-declared package (see correction notice above and `COA_G01_SOURCE_CONFLICT_REGISTER.md` C-07) and were never independently verified. They are corrected below to evidence-supported wording. This is not treated as a new conflict requiring a new register entry — it is the same C-07 provenance issue, previously corrected everywhere *except* this specific bullet list, which the CORR2 independent re-audit caught.

Reconciled source layers (corrected CORR3; further corrected CORR4, 2026-08-31):

- Team A Accounting Core deep research and direct source anchors — `VERIFIED FACT`.
- Authorized Accounting Core source semantics — `VERIFIED FACT`.
- Thailand localization source: 144 rows / 15 instantiated Account Types — `VERIFIED FACT` (source observation only, not a target-count ruling — see the CORR3 supersession notice in `COA_STANDARD/DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`).
- Boss-approved Odoo18 workbook: 389 rows / 14 observed Account Type labels — `VERIFIED FACT`, **now including the primary workbook file itself (CORR4)**: recovered by direct Drive ID, independently SHA-256 hashed (exact match), content independently parsed and cross-checked with zero discrepancies against the existing extraction. See `COA_G01_PRIMARY_SOURCE_RECOVERY_REGISTER_R4.md`. The `c530138` "directly re-verified" claim remains **unverified and is still not used as Gate evidence** — this CORR4 recovery is independent of and does not corroborate that earlier claim.
- Boss Thai COA business requirements (**Source Class E**) — `PARTIALLY RESOLVED` (CORR4). Nearly every G01-relevant requirement is now traced to an exact Boss-authored GitHub ruling/section — see `COA_G01_BOSS_THAI_COA_REQUIREMENTS_REGISTER_R4.md`. No single consolidated "requirements document" beyond this register exists or is claimed.
- Thai financial-statement presentation principles / official Thai reporting anchors (**Source Class F**) — `EVIDENCE_MISSING`, **CORR4 recovery attempted and blocked**: Boss provided a specific Drive file ID; both metadata and content lookups returned "not found" (`ACCESS_DENIED`, not classified as nonexistent). See `COA_G01_THAI_FINANCIAL_STATEMENT_PRESENTATION_SOURCE_R4.md`. No substitute evidence fabricated.
- Existing Boss / PMO / ChatGPT audit evidence — `VERIFIED FACT`, **excluding** the rejected `c530138`/`8fceca0` self-declaration (C-07).
- Primary Thai regulatory sources at concept level for VAT/WHT/CIT/reporting claims — `VERIFIED FACT` at concept-citation level only; not a statutory-verification claim (deferred to COA-G06).
- Local `STATE03` (S1–S11), Thai toolchain (T1–T9), and `STEP0303R2`–`R5` findings — `VERIFIED FACT`, **now ported to GitHub (CORR4)**: 63 files, security-scanned clean, hashed, independently verified byte-identical. See `COA_G01_LOCAL_STATE03_SOURCE_PORT_MANIFEST_R4.md`.

Reconciled target rule:

- Core source universe = 19 Account Types.
- `l10n_th` observation = 15 Account Types.
- Odoo18 workbook observation = 14 labels.
- SMEsPlus Local Thailand target = 19 ACTIVE Account Types by Boss ruling (not 15 — see the CORR3 supersession notice in `COA_STANDARD/DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`, finding `AUD2-01`).

Source conflicts are preserved and routed, not silently corrected. Key examples include inconsistent accumulated-depreciation source classifications and source tax accounts under generic Account Types.

**CORR4 update (2026-08-31):** `COA-G01 open conflicts = C-02 (cause only, existence RESOLVED), C-03 (substantive status), C-05 (carried forward, not re-adjudicated) — C-01, C-04, C-06, C-07 all RESOLVED/CLOSED; open unknowns = 2 (N-04 Class F ACCESS_DENIED, N-05 STEP0303R2 cause UNKNOWN) — N-01, N-02, N-03 all RESOLVED; SI-10 = PASS at classification scope (corrected from HOLD); Class E = PARTIALLY RESOLVED; Class F = EVIDENCE_MISSING (ACCESS_DENIED on this attempt).`

`COA-G01 SI-01..SI-10 = PASS at G01 classification scope (10/10, corrected CORR4).` COA-G01 is still not reportable as PASS — not because of an unresolved applicable SI, but because N-04/Class F and N-05 remain genuine, unresolved evidence gaps per the Audit Veto rule below.

*(Historical, superseded: "open unknowns = 4... SI-10 = HOLD even at classification scope — COA-G01 is therefore not reportable as PASS per the Audit Veto rule below." Accurate through CORR3, corrected above by CORR4.)*

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
