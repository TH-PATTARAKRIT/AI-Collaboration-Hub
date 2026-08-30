# EXPERT IBPV — Independent Business Process & Design Verification

Status: ACTIVE GOVERNANCE UNIT
Effective Date: 2026-08-30
Reporting Line: Direct to Boss only
Authority Source: `00_Project_Governance/DECISIONS/BOSS_DECISION_EXPERT_IBPV_APPOINTMENT_2026-08-30.md`
Charter: `00_Project_Governance/EXPERT_IBPV_CHARTER.md`

## Position in Migration Factory

```text
Team A — Source Extraction / Observation / Evidence
→ Evidence Gate
→ Team B — Independent SMEsPlus Canonical Design
→ EXPERT IBPV — Independent Process & Design Verification
→ Pre-Development Design Gate
→ Boss Decision
→ Team C — Migration Adapter / Engineering / Development
→ Team D — Independent Clean-room / QA / Compliance Audit
```

## Mandatory Rule

No controlled domain may proceed from Team B to Team C Development without EXPERT IBPV verification and subsequent Boss decision, unless Boss issues an explicit written exception.

## IBPV Domain Work Package Pattern

For each domain, create a controlled folder such as:

```text
EXPERT_IBPV/
└── DOMAIN_xx_<DOMAIN_NAME>/
    ├── 00_INPUT_EVIDENCE_REGISTER.md
    ├── 01_E2E_PROCESS_VERIFICATION.md
    ├── 02_CROSS_DOMAIN_FLOW_VERIFICATION.md
    ├── 03_STATE_EVENT_VERIFICATION.md
    ├── 04_DATA_FLOW_OWNERSHIP_VERIFICATION.md
    ├── 05_CONTROL_APPROVAL_SOD_VERIFICATION.md
    ├── 06_EXCEPTION_RECOVERY_VERIFICATION.md
    ├── 07_ACCOUNTING_COMPLIANCE_IMPACT.md
    ├── 08_INTEGRATION_FLOW_VERIFICATION.md
    ├── 09_REQUIREMENT_DESIGN_TRACEABILITY.md
    ├── 10_DESIGN_CONFLICT_REGISTER.md
    ├── 11_OPEN_GAP_UNKNOWN_REGISTER.md
    └── 12_IBPV_INDEPENDENT_VERIFICATION_REPORT.md
```

## Independence Boundary

EXPERT IBPV does not design in place of Team B, does not write Production Code, does not merge/release/deploy and does not self-approve.

Its findings are reported directly to Boss. PMO may preserve and track evidence but may not alter the IBPV verdict.

**No Evidence = No Progress**

**Never Skip Gate**

**Boss = Sole Final Approver**
