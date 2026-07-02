# DOCUMENT_MAP.md

Version: v1.1
Status: Approved Baseline
Owner: SMEsPlus Product & Architecture Team
Scope: `01_SaaS_Foundation`

## Purpose

เอกสารนี้ใช้เป็นแผนที่นำทางเอกสารทั้งหมดของ `01_SaaS_Foundation` เพื่อให้ทีมงานเข้าใจว่าแต่ละไฟล์มีหน้าที่อะไร ควรอ่านลำดับใด และเกี่ยวข้องกับเอกสารอื่นอย่างไร

## Document Groups

### 1. Foundation Governance

| Document                       | Purpose                                 |
| ------------------------------- | ---------------------------------------- |
| `README.md`                    | จุดเริ่มต้นของเอกสารทั้งหมด             |
| `DOCUMENT_MAP.md`              | แผนที่เอกสารและลำดับการอ่าน             |
| `GLOSSARY.md`                  | นิยามคำศัพท์กลาง                        |
| `ARCHITECTURE_PRINCIPLES.md`   | หลักการออกแบบระบบ                       |
| `ARCHITECTURE_GOVERNANCE.md`   | กระบวนการควบคุมและอนุมัติ architecture  |
| `ARCHITECTURE_DECISION_LOG.md` | รายการ decision สำคัญ                   |
| `TRACEABILITY_MATRIX.md`       | ตารางเชื่อมโยง requirement ถึง test/UAT |
| `VERSION_HISTORY.md`           | ประวัติ version ของเอกสาร               |
| `CHANGELOG.md`                 | บันทึกการเปลี่ยนแปลง                    |

### 2. Architecture Decision Records

| Folder | Purpose                                             |
| ------ | ---------------------------------------------------- |
| `ADR/` | เก็บเหตุผลและผลกระทบของการตัดสินใจเชิง architecture |

Required files:

* `ADR_TEMPLATE.md`
* `ADR-0001-SaaS-First.md`
* `ADR-0002-Multi-Tenant.md`
* `ADR-0003-API-First.md`
* `ADR-0004-Modular-Monolith.md`
* `ADR-0005-PostgreSQL.md`
* `ADR-0006-RBAC-ABAC-RLS.md`
* `ADR-0007-Audit-By-Design.md`
* `ADR-0008-Kubernetes-Deployment.md`

### 3. Functional Design Specification

| Folder | Purpose                                              |
| ------ | ---------------------------------------------------- |
| `FDS/` | ระบุ requirement เชิง functional ของ SaaS Foundation |

Main documents (updated v1.1 — 11-file structure, supersedes the original 2-file plan):

* `SMEPLUS-SAAS-FOUNDATION-FDS.md` — Master Index
* `01_DOCUMENT_CONTROL.md` — version, ownership, approval, change history
* `02_BUSINESS_CONTEXT.md` — business background, scope, stakeholders
* `03_FUNCTIONAL_REQUIREMENTS.md` — FR-FD-001 to FR-FD-004 with evidence status
* `04_NON_FUNCTIONAL_REQUIREMENTS.md` — performance, scalability, availability, security NFRs
* `05_DOMAIN_MODEL.md` — core entities and relationships
* `06_USER_STORIES.md` — user stories per persona
* `07_USE_CASES.md` — detailed use case flows
* `08_SECURITY_REQUIREMENTS.md` — tenant isolation, RBAC/ABAC, RLS requirements
* `09_INTEGRATION_REQUIREMENTS.md` — internal/external integration points
* `10_ACCEPTANCE_CRITERIA.md` — Given/When/Then acceptance criteria per FR

> Status of all 11 files above: Draft — In Review, pending Boss approval to Approved Baseline. `FDS_TEMPLATE.md` from the original plan was not carried forward; the numbered 01–10 structure now serves as the standing FDS template for future modules unless superseded.

### 4. Software Design Specification

| Folder | Purpose                                                 |
| ------ | -------------------------------------------------------- |
| `SDS/` | อธิบาย service, domain model, flow และ component design |

Main documents:

* `SDS_FOUNDATION.md`
* `DOMAIN_MODEL.md`
* `SERVICE_CATALOG.md`

### 5. API

| Folder | Purpose                                                   |
| ------ | ----------------------------------------------------------- |
| `API/` | ระบุ API contract, standard, error, pagination และ events |

Main documents:

* `OPENAPI_FOUNDATION.yaml`
* `API_GUIDELINE.md`
* `ERROR_CODE_STANDARD.md`
* `PAGINATION_STANDARD.md`
* `EVENT_CATALOG.md`

### 6. Database

| Folder      | Purpose                                                            |
| ----------- | -------------------------------------------------------------------- |
| `DATABASE/` | ระบุ ERD, data dictionary, database standard และ migration scripts |

Main documents:

* `ERD_FOUNDATION.md`
* `DATA_DICTIONARY.md`
* `DATABASE_STANDARDS.md`
* `MIGRATION/001_initial_schema.sql`
* `MIGRATION/002_rls_policy.sql`
* `MIGRATION/003_seed_data.sql`

### 7. Security

| Folder      | Purpose                                                                |
| ----------- | -------------------------------------------------------------------------- |
| `SECURITY/` | ระบุ security architecture, permission, tenant isolation และ checklist |

Main documents:

* `SECURITY_ARCHITECTURE.md`
* `PERMISSION_MATRIX.md`
* `TENANT_ISOLATION.md`
* `SECURITY_CHECKLIST.md`

### 8. UI

| Folder | Purpose                                                              |
| ------ | ---------------------------------------------------------------------- |
| `UI/`  | ระบุ screen specification, UI guideline, Figma mapping และ user flow |

Main documents:

* `SCREEN_SPEC_FOUNDATION.md`
* `UI_GUIDELINE.md`
* `FIGMA_MAPPING.md`
* `USER_FLOW.md`

### 9. QA

| Folder | Purpose                                                     |
| ------ | ------------------------------------------------------------- |
| `QA/`  | ระบุ test strategy, UAT scenarios, test data และ test cases |

Main documents:

* `TEST_STRATEGY.md`
* `UAT_SCENARIOS.md`
* `TEST_DATA.md`
* `TEST_CASES.md`

### 10. DevOps

| Folder    | Purpose                                                   |
| --------- | ------------------------------------------------------------ |
| `DEVOPS/` | ระบุ CI/CD, Docker, Kubernetes และ environment management |

Main documents:

* `CI_CD.md`
* `DOCKER.md`
* `KUBERNETES.md`
* `ENVIRONMENT.md`

### 11. Deployment

| Folder        | Purpose                                                         |
| -------------- | ------------------------------------------------------------------ |
| `DEPLOYMENT/` | ระบุ migration plan, deployment readiness และ go-live checklist |

Main documents:

* `MIGRATION_PLAN.md`
* `DEPLOYMENT_READINESS_CHECKLIST.md`
* `GO_LIVE_CHECKLIST.md`

## Recommended Reading Order

### For Executives / PM

1. `README.md`
2. `DOCUMENT_MAP.md`
3. `FDS/SMEPLUS-SAAS-FOUNDATION-FDS.md`
4. `TRACEABILITY_MATRIX.md`
5. `DEPLOYMENT/GO_LIVE_CHECKLIST.md`

### For Architects

1. `README.md`
2. `ARCHITECTURE_PRINCIPLES.md`
3. `ARCHITECTURE_GOVERNANCE.md`
4. `ARCHITECTURE_DECISION_LOG.md`
5. `ADR/*`
6. `SDS/SDS_FOUNDATION.md`
7. `SECURITY/SECURITY_ARCHITECTURE.md`
8. `DATABASE/ERD_FOUNDATION.md`

### For Backend Developers

1. `SDS/SDS_FOUNDATION.md`
2. `SDS/SERVICE_CATALOG.md`
3. `API/API_GUIDELINE.md`
4. `API/OPENAPI_FOUNDATION.yaml`
5. `DATABASE/DATABASE_STANDARDS.md`
6. `SECURITY/PERMISSION_MATRIX.md`

### For Frontend Developers

1. `UI/SCREEN_SPEC_FOUNDATION.md`
2. `UI/UI_GUIDELINE.md`
3. `UI/USER_FLOW.md`
4. `API/OPENAPI_FOUNDATION.yaml`
5. `SECURITY/PERMISSION_MATRIX.md`

### For QA

1. `FDS/SMEPLUS-SAAS-FOUNDATION-FDS.md`
2. `TRACEABILITY_MATRIX.md`
3. `QA/TEST_STRATEGY.md`
4. `QA/TEST_CASES.md`
5. `QA/UAT_SCENARIOS.md`

### For DevOps

1. `DEVOPS/CI_CD.md`
2. `DEVOPS/DOCKER.md`
3. `DEVOPS/KUBERNETES.md`
4. `DEVOPS/ENVIRONMENT.md`
5. `DEPLOYMENT/DEPLOYMENT_READINESS_CHECKLIST.md`

## Dependency Rule

เอกสาร downstream ต้องไม่ขัดแย้งกับเอกสาร upstream

```text
README
→ Principles / Governance / ADR
→ FDS
→ SDS
→ API / Database / UI / Security
→ QA
→ DevOps / Deployment
```

## Maintenance Rule

เมื่อมีการเปลี่ยนแปลง requirement หรือ architecture ต้องอัปเดตเอกสารที่เกี่ยวข้องอย่างน้อย:

* `CHANGELOG.md`
* `VERSION_HISTORY.md`
* `TRACEABILITY_MATRIX.md`
* เอกสารต้นทางที่เปลี่ยน
* เอกสาร downstream ที่ได้รับผลกระทบ

## Approval Rule

เอกสารนี้ต้องได้รับการอัปเดตทุกครั้งที่มีการเพิ่ม ลบ หรือย้ายไฟล์ใน `01_SaaS_Foundation`

## Change History

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-07-02 | v1.0 | Approved baseline (original) | SMEsPlus Product & Architecture Team |
| 2026-07-02 | v1.1 | Updated Section 3 (Functional Design Specification) to reflect actual 11-file FDS structure created under `FDS/`, replacing the original 2-file plan. Change directed by Boss. `CHANGELOG.md`, `VERSION_HISTORY.md`, and `TRACEABILITY_MATRIX.md` still need corresponding updates (see Maintenance Rule). | Functional Specification AI (Claude), per Boss instruction |
