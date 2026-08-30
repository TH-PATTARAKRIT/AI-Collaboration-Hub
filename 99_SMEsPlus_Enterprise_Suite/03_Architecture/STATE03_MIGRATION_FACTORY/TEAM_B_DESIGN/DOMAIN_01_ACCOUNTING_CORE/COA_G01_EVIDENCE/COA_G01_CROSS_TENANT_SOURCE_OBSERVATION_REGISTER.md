# COA-G01 — Cross-Tenant Source Observation Register

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Investigate and register source evidence/gaps for SI-08 (No cross-tenant COA access) | Claude (session SMEPLUS-26-08-30-COA-G01R-001) | GitHub `SMEsPlus` branch; local `ACCOUNT` folder | 2026-08-30 22:27 +0700 | ChatGPT Independent Review (pending); Boss (pending) | HOLD / EVIDENCE REQUIRED (no source-side finding to reconcile; target control unexecuted) | Directly feeds COA-G07 (Multi-company & Dimension Proof), which owns hard-failure testing of cross-tenant access |

## Source-side observation

The reference source (Odoo Community/Enterprise `account` module and `l10n_th`) is **single-tenant, on-premise software** with no multi-tenant data model at all — there is no "other tenant's data" for it to leak, because it has no tenant concept. Consequently:

- **No documented cross-tenant vulnerability, coupling, or leakage was found in the source material reviewed** (the 19-type core enum, the 144-row `l10n_th` template, the 389-row Odoo18 workbook). This is expected, not a clean bill of health on multi-tenancy — the source was simply never multi-tenant, so it was never exposed to this risk class.
- Local finding S5 (Tenant → Company → Tax Branch) is the closest available source-adjacent finding, but it addresses the *organizational modeling* question (how many levels a tenant's own hierarchy needs), not cross-tenant isolation between different tenants.

**Conclusion: SI-08 is correctly classified at COA-G01 as a forward-looking design control with no applicable source-side finding to report, positive or negative.** It should not be marked PASS as if a source-side test were performed — none exists to perform, since the source has no multi-tenant surface.

## Target-side status

| Item | Status | Evidence |
|---|---|---|
| SI-08 defined as a mandatory cross-gate invariant: "No cross-tenant COA access" | BOSS RULING | `AL_COA_CLOSURE_EVIDENCE_INDEX.md`; Jira comment `10901` |
| SI-08 treated as a hard failure at COA-G07 | BOSS RULING | `AO_BOSS_CROSS_GATE_SAAS_INVARIANTS_RULING.md` §5, COA-G07: "Cross-tenant access is a hard failure." |
| `ARC-0003` (Multi-Tenant/Company/Branch Data Isolation Matrix) required-content checklist, including "Cross-tenant risk" and "Required isolation rule" | REQUIRED-CONTENT CHECKLIST ONLY — not answered | Local `07 SAAS ARCHITECH/SMEsPlus SaaS Architecture Review.pdf` |
| Any actual runtime/database isolation test | NOT PERFORMED | No code, schema, or provisioning exists yet (Development Authorization = NOT GRANTED) |

## COA-G01-scope conclusion

- SI-08 evidence status for **COA-G01 purposes** (classification only): **PASS / VERIFIED** — correctly classified as "not applicable to observe at the source layer; mandatory at the target layer; not yet executed."
- SI-08 evidence status for **execution/production purposes** (COA-G07 scope): **HOLD / EVIDENCE REQUIRED** — no isolation test has been run because no implementation exists. This register does not claim otherwise, and does not attempt to simulate or infer a test result.
