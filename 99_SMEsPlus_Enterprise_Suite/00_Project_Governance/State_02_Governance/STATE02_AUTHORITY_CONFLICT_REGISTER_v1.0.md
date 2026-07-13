# STATE02_AUTHORITY_CONFLICT_REGISTER_v1.0.md

Session: SMEPLUS-26-07-13-002
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Branch: SMEsPlus
Commit Reference: bedb70555e0a16551f379f4db7e59d0bd0fb0dba
Prepared By: Claude AI (Specialist AI — draft/evidence preparation only)
Register Status: HOLD — PENDING INDEPENDENT REVIEW AND VERIFICATION

All records begin at HOLD. Claude AI is not the Evidence Verifier and does not self-verify.

| Conflict ID | Document / Path | Version / Commit | Line / Section | Existing Text / Current Authority | Type | Severity | Required Authority | Reviewer | Verifier | Verification | Gate Impact | Corrective Action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACF-001 | `00_Project_Governance/AI_ROLE_AND_RESPONSIBILITY.md` | v1.0 / `bedb705...` | Line 160, Gate Control | Build Gate owner = `PMO + Boss` | AC-02 | P0 | Boss approval authority; AI PMO Support Only | NOT ASSIGNED | NOT ASSIGNED | HOLD | Build Gate HOLD | STEP 03 correction proposal; reconcile with Approval Matrix line 25 |
| ACF-002 | `00_Project_Governance/AI_ROLE_AND_RESPONSIBILITY.md` | v1.0 / `bedb705...` | Line 159, Gate Control | QA/UAT Gate owner = `QA AI + PMO` | AC-02 | P0 | Accountable Owner/Boss structure; AI PMO Support Only | NOT ASSIGNED | NOT ASSIGNED | HOLD | QA/UAT Gate HOLD | STEP 03 correction proposal |
| ACF-003 | `00_Project_Governance/AI_ROLE_AND_RESPONSIBILITY.md` | v1.0 / `bedb705...` | Line 95, Rule 9 | Production approved by `Boss and PMO Gate` | AC-07; AC-03 candidate | P1 | Boss-only explicit Production approval | NOT ASSIGNED | NOT ASSIGNED | HOLD | Production authority ambiguity | STEP 03 wording clarification |
| ACF-004 | `00_Project_Governance/ARCHITECTURE_GOVERNANCE_STANDARD.md` | v1.0 / `bedb705...` | Line 31, Authority | `Boss / PMO authority` required for gate movement | AC-02 / AC-03 | P0 | Boss Sole Final Approver; AI PMO Support Only | NOT ASSIGNED | NOT ASSIGNED | HOLD | Architecture Gate HOLD | STEP 03 correction proposal |
| ACF-005 | `00_Project_Governance/APPROVAL_AUTHORITY_MATRIX.md` | v1.0 / `bedb705...` | Line 23 | FDS Final Approver = `Boss / PMO` | AC-03 | P0 | Boss | NOT ASSIGNED | NOT ASSIGNED | HOLD | FDS Gate HOLD | STEP 03 replacement row |
| ACF-006 | `00_Project_Governance/APPROVAL_AUTHORITY_MATRIX.md` | v1.0 / `bedb705...` | Line 24 | SDS/API/DB/UX Final Approver = `Boss / PMO` | AC-03 | P0 | Boss | NOT ASSIGNED | NOT ASSIGNED | HOLD | Technical artifact approval conflict | STEP 03 replacement row |
| ACF-007 | `00_Project_Governance/APPROVAL_AUTHORITY_MATRIX.md` | v1.0 / `bedb705...` | Line 18 | Project Constitution Draft Owner = `Liza / PMO AI` | AC-07 | P1 | Clarify AI drafting scope under Support Only | NOT ASSIGNED | NOT ASSIGNED | HOLD | Governance Gate ambiguity | Resolve canonical role definition first |
| ACF-008 | `DOCUMENT_REGISTRY.yaml` vs. three 2026-07-05 standards | v1.1 / `bedb705...` | Registry lines 9–12 | Registry says AI PMO Support Only / Boss final authority; older standards still conflict | AC-08 | P0 | Latest Boss-approved baseline applied consistently | NOT ASSIGNED | NOT ASSIGNED | HOLD | Governance source-of-truth conflict | Synchronized re-issue/version correction in STEP 03 |
| ACF-009 | `00_Project_Governance/FOLDER_REGISTRY.yaml` | v1.0 / `bedb705...` | Lines 26,31,36,41,61 | Bare or joint `PMO` used as folder owner | AC-01 candidate / AC-07 | P1 | Distinguish human PMO from AI PMO; AI PMO not Accountable Owner | NOT ASSIGNED | NOT ASSIGNED | HOLD / NOT VERIFIED ENTITY | Repository Gate ambiguity | Resolve PMO definition then correct ownership labels |
| ACF-010 | Cross-document governance set | mixed / `bedb705...` | Multiple | `PMO` has at least three apparent meanings | AC-07 | P1 | Canonical unambiguous PMO role definitions | NOT ASSIGNED | NOT ASSIGNED | HOLD | Root cause across Governance Gate | Add canonical Role Definitions / glossary in STEP 03 |

Evidence Timestamp for all findings: 2026-07-13.

## Documents Scanned With No Conflict Found

PROJECT_CONSTITUTION.md; AI_COLLABORATION_STANDARD.md; FUNCTIONAL_SPECIFICATION_STANDARD.md; DOCUMENT_STANDARD.md; TRACEABILITY_STANDARD.md; QUALITY_GATE_STANDARD.md; MASTER_EXECUTION_ROADMAP.md; STATE01_SOURCE_OF_TRUTH_POLICY_v1.0.md; REPOSITORY_REGISTRY.yaml; root README.md.

## Not Available For Scan

Governance-related GitHub Issue descriptions and templates: NOT AVAILABLE FOR SCAN. No confirmed STEP 01 issue references were available and the broad query was rate-limited. Absence must not be treated as No Conflict.

## Control Statement

```text
Boss = Sole Final Approver
AI PMO = Support Only
Source documents were not modified
STEP 02 remains HOLD pending Reviewer and Verifier action
```
