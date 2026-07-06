# FDS Factory Pipeline

Document ID: SMEPLUS-FDSFAC-PIPELINE-001
Owner: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss
Status: Draft — pending Boss/PMO review
Location note: consolidated into existing canonical folder `17_Functional_Specification_Factory/`
per `SMEPLUS_REGISTRY.yaml` (no new `FDS_Factory/` top-level folder created).

## Purpose
Defines the draft-only, evidence-first pipeline used to generate Functional Design
Specification (FDS) drafts for SMEsPlus modules. Output from this pipeline is never
self-approved; every stage output is a draft pending human/AI-role review per the
AI Project Constitution.

## Pipeline Stages
1. Repository / Knowledge Source
2. Repository Checker — confirms folder/file mapping exists before any generation
3. Factory Job Scheduler — reads `factory_jobs/` queue
4. Clean-Room Knowledge Loader — loads only Concept Match sources (ADR-0006)
5. Knowledge Normalization
6. Requirement Extractor
7. Business Rule Generator
8. Workflow / Process Draft Generator
9. Data Mapping Draft Generator
10. API Contract Draft Generator
11. UI Requirement Draft Generator
12. Acceptance Criteria Generator
13. Gap Generator
14. Evidence Mapper (MATCHED / PARTIAL / GAP / NEW / RETIRE)
15. Traceability Generator — writes to `12_Traceability/`
16. QA / Gate Validator
17. Human Review Package Builder
18. Git Branch / Pull Request (requires confirmed write credentials)

## Control Rules
- Draft-only. No stage output counts as approved project knowledge until reviewed.
- Clean Room 100%: no direct Odoo/OCA runtime code reuse — Concept Match only.
- Evidence-first: every generated artifact must carry owner, source, timestamp,
  status (MATCHED/PARTIAL/GAP/NEW/RETIRE).
- No Build / No Production output from this pipeline.
- Human review required before any output is merged into `02_Functional_Design/`.
