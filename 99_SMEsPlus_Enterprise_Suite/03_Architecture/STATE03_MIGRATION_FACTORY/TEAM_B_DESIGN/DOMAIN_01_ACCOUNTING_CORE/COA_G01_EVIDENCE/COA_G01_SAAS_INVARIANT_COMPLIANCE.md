# COA-G01 — Cross-Gate SaaS Invariant (SI-01..SI-10) Compliance Matrix

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Produce the first SI-01..SI-10 compliance matrix for COA-G01, as mandated by Jira comment `10901` / commit `e16b29f3` | Claude (session SMEPLUS-26-08-30-COA-G01R-001) | This artifact; supporting registers in this folder | 2026-08-30 22:27 +0700 | ChatGPT Independent Review (pending); PMO (pending); Boss (pending) | See per-SI status below; overall = HOLD / EVIDENCE REQUIRED | Per governance: "No Gate may be reported PASS/FROZEN/COMPLETE/READY FOR HANDOFF while an applicable SI remains unresolved" — this Gate is not reported PASS |

## Scope interpretation (must be read before the table below)

Per the session's Gate-appropriate evidence boundary: *"COA-G01 is a Source Baseline Gate, not the G04S deep-design Gate... Do not require G01 to produce production tenancy architecture, physical schema, API, provisioning engine or runtime isolation test proof... G01 must explicitly classify the source assumptions and retain every missing item as UNKNOWN or EVIDENCE_MISSING."*

Accordingly, each SI below is scored at **two levels**:
- **G01 classification scope** — has the invariant been correctly classified against source-baseline evidence, with no unknown silently resolved?
- **Execution scope** — has the invariant actually been implemented/proven (this is generally COA-G04S/G06/G07 work, not COA-G01)?

A PASS at G01-classification-scope is **not** a claim that the invariant is enforced in any running system.

## Matrix

| SI | Statement | G01 classification-scope status | Execution-scope status | Evidence |
|---|---|---|---|---|
| SI-01 | Tenant context is mandatory | PASS / VERIFIED | HOLD / EVIDENCE REQUIRED (COA-G04S) | AQ ruling §3; `COA_G01_SAAS_CONTEXT_BOUNDARY_REGISTER.md` |
| SI-02 | Company context is mandatory where company-scoped | PASS / VERIFIED | HOLD / EVIDENCE REQUIRED (COA-G04S) | AQ ruling §3; local finding S5 (Tenant→Company→Tax Branch) |
| SI-03 | Standard Template is not tenant-owned mutable data | PASS / VERIFIED | HOLD / EVIDENCE REQUIRED (COA-G04S) | AQ ruling §3.1/§3.5; `AG_BOSS_COA_LOCAL_TH_RULING.md` §4 |
| SI-04 | Tenant customization cannot modify the Published Standard Template | PASS / VERIFIED | HOLD / EVIDENCE REQUIRED (COA-G04S) | AQ ruling §3.5; `AM_BOSS_COA_SAAS_ARCHITECTURE_AMENDMENT.md` |
| SI-05 | Account Code / Name is not canonical identity | PASS / VERIFIED | N/A — this is a modeling rule verifiable at design time, not a runtime proof; already consistently applied across every COA-G01 artifact in this remediation | Repeated Boss ruling across `AG`, `AJ`, `AL`, `AO`, `AP`; applied throughout this session's artifacts |
| SI-06 | Published Template Version is immutable | PASS / VERIFIED (classification: source has no versioning concept to reconcile; target principle Boss-ruled) | HOLD / EVIDENCE REQUIRED (COA-G04S) | `COA_G01_TEMPLATE_VERSION_UPGRADE_SOURCE_REGISTER.md` |
| SI-07 | Upgrade is explicit, previewable and auditable | PASS / VERIFIED (classification only) | HOLD / EVIDENCE REQUIRED (COA-G04S) | `COA_G01_TEMPLATE_VERSION_UPGRADE_SOURCE_REGISTER.md` |
| SI-08 | No cross-tenant COA access | PASS / VERIFIED (classification: source has no multi-tenant surface to test; correctly flagged as inapplicable at source layer) | HOLD / EVIDENCE REQUIRED (COA-G07) | `COA_G01_CROSS_TENANT_SOURCE_OBSERVATION_REGISTER.md` |
| SI-09 | Company customization must preserve canonical reporting semantics | PASS / VERIFIED (classification: rule stated and applied consistently — Account Group may not redefine Account Type or Financial Statement Mapping) | HOLD / EVIDENCE REQUIRED (COA-G05/G07) | Session prompt §7; `COA_G01_ACCOUNT_CONCEPT_UNIVERSE.md` |
| SI-10 | SaaS Core must not hard-code Thailand-specific source architecture | **HOLD / EVIDENCE REQUIRED even at classification scope** | HOLD / EVIDENCE REQUIRED (COA-G06) | `COA_G01_THAI_RELEVANCE_REGISTER.md` — supporting findings (S1, S4) exist only locally, not yet on GitHub, and no formal SI-10 compliance analysis of the `l10n_th` structures has been produced anywhere yet (see `COA_G01_SOURCE_CONFLICT_REGISTER.md` C-01) |

## Overall Gate-level SI status

**9 of 10 invariants (SI-01–SI-09) PASS at G01 classification scope. SI-10 is HOLD even at classification scope**, because its supporting evidence (local findings S1/S4, and the `l10n_th` 144-row/15-type structural breakdown) has not yet been reconciled into the GitHub Source of Record, and no dedicated SI-10 compliance analysis document exists yet anywhere in the evidence base.

Per the Audit Veto rule ("no Gate may be reported PASS... while an applicable SI remains unresolved"): **COA-G01 cannot be reported PASS while SI-10 remains HOLD at classification scope.** This is the primary technical driver of the overall Gate recommendation in `COA_G01_GATE_REPORT.md`.

All nine execution-scope columns marked HOLD are expected and do not block COA-G01 (they are explicitly out of G01's Gate-appropriate scope) — they are recorded here so COA-G04S/G05/G06/G07 inherit an accurate starting checklist rather than re-deriving it.
