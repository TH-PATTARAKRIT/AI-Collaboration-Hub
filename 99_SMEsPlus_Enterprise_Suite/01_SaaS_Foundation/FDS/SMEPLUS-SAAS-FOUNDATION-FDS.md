# SMEsPlus SaaS Foundation
# Functional Design Specification — Master Index

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-001
Version: 2.0.0 (restructured to domain-based layout)
Status: Draft — Evidence-Pending
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## Governance Note
This package restructures the earlier 31-section FDS into per-domain files under `Domains/`, one
file per Foundation entity, using `FDS_TEMPLATE.md` as the common authoring template. This keeps
each domain independently reviewable and evidence-matchable, and lets downstream AI roles
(Database Design AI, Figma UX UI AI, Claude Code AI, QA UAT AI) consume one domain at a time.

Target path `99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS` remains **unregistered** in
`FOLDER_REGISTRY.yaml` / `DOCUMENT_REGISTRY.yaml`. Registration + PMO/Boss sign-off is still
pending (see prior package's Appendix C). Functional Design (State 04) remains HOLD at
project-status level. This package is a Draft prepared ahead of gate release, per ADR-0002
"No Evidence = No Progress" — no domain file below should be treated as Reviewed/Approved until
matched against `SMEPLUS-FUNCTIONAL-DESIGN-MATCHING-MATRIX.md`.

## Structure

```
FDS/
├── SMEPLUS-SAAS-FOUNDATION-FDS.md   (this file)
├── FDS_TEMPLATE.md                   (authoring template — copy for new domains)
└── Domains/
    ├── FDS_TENANT.md
    ├── FDS_COMPANY.md
    ├── FDS_BRANCH.md
    ├── FDS_DIVISION.md
    ├── FDS_IAM.md
    ├── FDS_ROLE.md
    ├── FDS_PERMISSION.md
    ├── FDS_SUBSCRIPTION.md
    ├── FDS_MODULE.md
    ├── FDS_APPROVAL.md
    ├── FDS_NOTIFICATION.md
    ├── FDS_AUDIT.md
    ├── FDS_INTEGRATION.md
    ├── FDS_REPORTING.md
    └── FDS_CONFIGURATION.md
```

## Domain Index

| Domain File | Purpose | Depends On |
|---|---|---|
| FDS_TENANT.md | Tenant lifecycle and isolation | — (root entity) |
| FDS_COMPANY.md | Legal entity under a tenant | Tenant |
| FDS_BRANCH.md | Operational location under a company | Company |
| FDS_DIVISION.md | Department/unit under a branch | Branch |
| FDS_IAM.md | Identity, authentication, user lifecycle | Tenant |
| FDS_ROLE.md | Role definition and assignment | IAM |
| FDS_PERMISSION.md | Fine-grained access rights | Role |
| FDS_SUBSCRIPTION.md | Plan, billing gate, feature flags | Tenant |
| FDS_MODULE.md | Module registry / marketplace enablement | Subscription |
| FDS_APPROVAL.md | Generic multi-level approval engine | IAM, Role |
| FDS_NOTIFICATION.md | In-app/email notification delivery | IAM, Approval |
| FDS_AUDIT.md | Audit trail / change log | IAM |
| FDS_INTEGRATION.md | API contract surface for modules/external systems | Module |
| FDS_REPORTING.md | Cross-domain reporting requirements | Audit, Approval |
| FDS_CONFIGURATION.md | Tenant/company-level configuration values | Tenant, Company |

## Evidence Status Reference
See `SMEPLUS-FUNCTIONAL-DESIGN-MATCHING-MATRIX.md` for authoritative MATCHED/PARTIAL/GAP status
per requirement (FD-001–FD-030). Each domain file below references the relevant FD-IDs but does
not restate their evidence status — the Matrix remains single source of truth.
