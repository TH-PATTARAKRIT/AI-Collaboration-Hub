# COA-G01 — Template Version / Upgrade Source Register

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Investigate and register source evidence/gaps for SI-06 (Template Version immutable) and SI-07 (Upgrade explicit/previewable/auditable) | Claude (session SMEPLUS-26-08-30-COA-G01R-001) | GitHub `SMEsPlus` branch; local `ACCOUNT/07 SAAS ARCHITECH/` | 2026-08-30 22:27 +0700 | ChatGPT Independent Review (pending); Boss (pending) | HOLD / EVIDENCE REQUIRED (source has no versioning concept to observe; target principle is Boss-approved but unexecuted) | Directly feeds COA-G04S, which owns execution of SI-06/SI-07 |

## Source-side observation (what the reference/source systems actually do)

The Odoo/`l10n_th`/Odoo18-workbook source material is **single-tenant, on-premise software with one live, directly-editable Chart of Accounts** — it has no template/instance separation and no version-lineage concept for a chart of accounts. This is an expected and unremarkable source characteristic, not a defect: single-tenant on-prem software has no structural need for template versioning.

- Evidence: the 389-row Odoo18 workbook tab and the 144-row `l10n_th` CSV are each a single flat data extraction, not a versioned series (`DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md`, `DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`).
- Conclusion for COA-G01: SI-06 and SI-07 are **target-architecture invariants with no source analogue to reconcile against** — COA-G01's job is limited to noting this absence, per the Gate-appropriate evidence boundary (G01 must not be required to produce production tenancy/versioning proof).

## Target-side status (what has already been Boss-ruled, and what remains unexecuted)

| Item | Status | Evidence |
|---|---|---|
| Standard COA Template vs Company COA Instance separation (conceptual) | BOSS APPROVED (direction only) | `BOSS_GATE/..._AG_BOSS_COA_LOCAL_TH_RULING.md` §4 |
| `COA-G04S` created as the mandatory Gate to execute template/tenancy/versioning/upgrade architecture | BOSS AUTHORIZED / NOT EXECUTED | `BOSS_GATE/..._AM_BOSS_COA_SAAS_ARCHITECTURE_AMENDMENT.md` |
| Upgrade principle: `Template Version Change -> Compatibility Assessment -> Tenant Delta Analysis -> Upgrade Preview -> Controlled Apply -> Audit Evidence` | BOSS RULING (principle only, not implemented) | `AM`, `AN` |
| "No automatic destructive overwrite of Tenant/Company customizations is authorized" | BOSS RULING (constraint on future design) | `AM` |
| 13-item COA-G04S exit-criteria checklist (tenant isolation VERIFIED, template versioning VERIFIED, etc.) | ALL UNMET | `AL_COA_CLOSURE_EVIDENCE_INDEX.md` Governance Red Flags: "COA-G04S execution evidence = NOT YET AVAILABLE" |
| SaaS Architecture Review PDF, `ARC-0003` (Multi-Tenant/Company/Branch Data Isolation Matrix), `ARC-0008` (includes "Version control" as a required heading) | REQUIRED-CONTENT CHECKLIST ONLY — no answers produced | Local `07 SAAS ARCHITECH/SMEsPlus SaaS Architecture Review.pdf`; folder contains only this one PDF, no `ARC-0001`–`ARC-0010` deliverables exist |

## COA-G01-scope conclusion

- SI-06 / SI-07 evidence status for **COA-G01 purposes** (classification only): **PASS / VERIFIED** — the absence of a source-side versioning concept has been correctly classified, and the target principle is already Boss-ruled and referenced.
- SI-06 / SI-07 evidence status for **execution/production purposes** (COA-G04S scope): **HOLD / EVIDENCE REQUIRED** — remains entirely unexecuted. This register does not claim otherwise.
