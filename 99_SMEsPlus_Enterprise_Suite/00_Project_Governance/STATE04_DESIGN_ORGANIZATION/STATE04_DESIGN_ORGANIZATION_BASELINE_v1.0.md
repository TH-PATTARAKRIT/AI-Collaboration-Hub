# STATE04 DESIGN ORGANIZATION BASELINE

Version: v1.0  
Status: Approved  
Owner: Executive Secretary / SMEsPlus PMO (stewardship / coordination only)  
Approved By: Boss  
Effective Date: 2026-08-30  
Scope: STATE04 — Functional & Solution Design  
Related Decision: `SMEPLUS-BDR-STATE04-DESIGN-ORG-2026-08-30-001`  
Jira Epic: `ERPPLUS-103`

## 1. Purpose

Define the complete STATE04 design organization required to convert approved architecture, research evidence, business requirements and controlled Team-B outputs into official SMEsPlus design baselines before STATE05 / STATE06.

STATE04 uses ten permanent design responsibilities. These responsibilities are always defined even when staffing is elastic.

Principle:

`10 Permanent Design Responsibilities != 10 Large Permanent Staff Groups`

A role may support more than one design team when competent and capacity permits, but a person / AI / role may not independently audit its own deliverable.

## 2. Upstream / Downstream Boundary

```text
Team A1 / A2 — Deep Research & Evidence
        ↓
Team B — Analysis / Transformation / Candidate Design Input
        ↓
Controlled Handoff
        ↓
STATE04 — Ten Official Design Teams
        ↓
Team11 Continuous Independent Audit Veto
        ↓
Boss Gate
        ↓
Approved SMEsPlus Design Baseline
        ↓
STATE05 UX/UI + STATE06 Development
```

Team-B output is candidate design input, not an approved STATE04 design baseline.

## 3. STATE04 Team Matrix

| Team | Design Responsibility | Primary Accountable Board | Core Roles | Independent Challenger | Jira |
|---|---|---|---|---|---|
| 01 | Functional & Domain Design | Board04 — Business Modules | Functional Architect; Domain SME; Business Process Analyst; FDS/Requirement Analyst; Acceptance-Criteria Designer; Evidence Coordinator | Team11.1 | ERPPLUS-104 |
| 02 | SaaS & Platform Solution Design | Board03 — Platform Foundation | SaaS Solution Architect; Multi-Tenant Architect; Tenant Lifecycle Designer; Entitlement/Subscription Designer; Platform Services Designer; Config/Extensibility Designer; Evidence Coordinator | Team11.2 | ERPPLUS-105 |
| 03 | Data & Database Design | Board06 — Data & Canonical Model | Data Architect; Domain Data Modeler; Logical DB Designer; Master/Reference Data Designer; Data Lifecycle Designer; Tenant Data Boundary Designer; Data Quality/Lineage Analyst | Team11.3 | ERPPLUS-106 |
| 04 | Integration / API / Event Design | Board03 — Platform Foundation | Integration Architect; API Contract Designer; Event/Message Designer; Idempotency/Retry Designer; External Interface Analyst; Error Contract Designer | Team11.4 | ERPPLUS-107 |
| 05 | Security / IAM / Approval / Audit Design | Board05 — Approval & Control | Security & Control Architect; IAM/RBAC/ABAC Designer; SoD Analyst; Approval Policy Designer; Audit-Trail Designer; Sensitive-Action Control Designer | Team11.5 | ERPPLUS-108 |
| 06 | Reporting & Analytics Design | Board04 + Board06 | Reporting Architect; Financial Reporting SME; Operational Reporting SME; KPI/Metric Designer; Drill-down/Traceability Designer; Reconciliation Designer; Analytics Data Modeler | Team11.6 | ERPPLUS-109 |
| 07 | Localization & Compliance Design | Board04 + Board05 | Localization Architect; Thai Accounting SME; VAT/e-Tax SME; WHT SME; Statutory Document Analyst; Regulatory Evidence Analyst | Team11.7 | ERPPLUS-110 |
| 08 | Migration & Canonical Mapping Design | Board06 — Data & Canonical Model | Migration Architect; Mapping Analyst; Transformation Rule Designer; Reconciliation Designer; Cutover Analyst; Exception/Hold Designer; Lineage Coordinator | Team11.8 | ERPPLUS-111 |
| 09 | NFR / Reliability / Operability Design | Board02 + Board03; Board08 Consulted | NFR Architect; Performance/Scalability Designer; Reliability/Availability Designer; Resilience/Recovery Designer; Observability Designer; Backup/DR Analyst; Operability Designer | Team11.9 | ERPPLUS-112 |
| 10 | AI Capability & Automation Design | Board01 + Board03; AI Governance Control | AI Solution Architect; AI Use-Case Designer; Human-Control Designer; Model I/O Contract Designer; Safety/Fallback Designer; AI Auditability Designer; Automation Workflow Designer | Team11.10 | ERPPLUS-113 |
| 11 | Independent Design Assurance & Audit Veto Office | Direct to Boss / independent | Audit Veto Lead; 10 Domain Audit Experts; Evidence Challenge Coordinator; Cross-Domain Assurance | N/A — independent unit | ERPPLUS-114 |

## 4. Mandatory Cross-Team Review Rule

A feature is owned by one Primary Design Team but every materially affected design team must participate before D3.

Example — Customer Invoice:

- Primary: Team01 Functional & Domain.
- Mandatory as applicable: Team03 Data/DB; Team05 Security/Approval; Team06 Reporting; Team07 Localization; Team08 Migration.
- Conditional: Team04 Integration; Team09 NFR; Team10 AI.

`NOT APPLICABLE` is a review disposition and must include reviewer, reason and evidence. Silence or omission is not N/A.

## 5. Design Team Exit Criteria

A design package may enter Team11 D3 only when it contains, as applicable:

- approved input references;
- business / domain objectives;
- explicit assumptions and unknowns;
- design decisions and alternatives;
- state / event / lifecycle rules;
- data and ownership impacts;
- security / control impacts;
- localization / compliance impacts;
- reporting / reconciliation impacts;
- integration impacts;
- NFR / operability impacts;
- migration impacts;
- AI impacts where applicable;
- acceptance criteria;
- evidence traceability;
- cross-team dispositions.

## 6. Authority Model

Design Team: authors and defends its design.  
Team11: independently challenges, verifies and may block.  
PMO: tracks evidence, owners, due dates and gate state; cannot alter Audit Veto verdict.  
Boards: provide domain accountability and constraints.  
Boss: sole Final Approver.

Audit Veto PASS does not equal Boss approval. Audit Veto VETO blocks normal progression unless Boss records an explicit exception / risk acceptance.

## 7. Staffing Status

Role baseline: APPROVED.  
Named Team Leads: UNASSIGNED.  
Named Team Members: TBD.  
Named Team11 Cross-Domain Audit Lead: UNASSIGNED.  
Named Audit Experts 11.2–11.10: UNASSIGNED.  
Existing Boss-approved EXPERT IBPV capability: AVAILABLE FOR CONTROLLED MAPPING TO 11.1 / cross-domain business-process verification.

No schedule-progress percentage is claimed until named assignments and due dates are evidenced.

## 8. Existing Independent Expert Interfaces

- `EXPERT_IBPV_CHARTER.md` — existing Boss-approved pre-development independent process/design verification capability; organizationally mapped into Team11 control model without reducing charter independence.
- `EXPERT_IESA_CHARTER.md` — downstream ERP/SaaS system assurance; remains separate.
- `EXPERT_IDTM_CHARTER.md` — downstream deep test matrix/system verification; remains separate.
- Team D — post-implementation QA / clean-room / compliance audit; remains separate.

## 9. Prohibited Shortcuts

- No Design Team self-review.
- No Team-B output directly becomes a STATE04 approved design.
- No missing specialist review may be treated as implicit N/A.
- No unresolved Critical/High Audit Veto finding may be hidden or reclassified without evidence.
- No physical target DB schema freeze merely because logical design exists.
- No coding / merge / release / deploy / production authority is created by this baseline.

No Evidence = No Progress.  
Never Skip Gate.  
Boss = Sole Final Approver.
