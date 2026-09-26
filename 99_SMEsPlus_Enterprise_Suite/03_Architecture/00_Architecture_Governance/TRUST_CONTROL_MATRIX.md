# Mandatory Trust Control Matrix

Session: [SMEPLUS-26-07-10-001]
Version: 2.0-draft
Status: CONTROLLED DRAFT
Gate Status: HOLD

| Control ID | Control | Primary Domain | Mandatory Reviewer | Required Evidence | Gate Coverage | Waiver Rule |
|---|---|---|---|---|---|---|
| TC-01 | Tenant Isolation | Tenant Architecture | Tenant Isolation Specialist + Human Security Reviewer | Isolation model, enforcement points, test plan and test result | B-D | NON-WAIVABLE while critical finding open |
| TC-02 | Identity and Privileged Access | IAM Architecture | IAM Specialist + Human Security Reviewer | RBAC/ABAC model, privileged access, SoD and access review evidence | B-D | NON-WAIVABLE while critical finding open |
| TC-03 | Data Ownership and Classification | Data and Privacy | Data Governance Specialist + Human Data Reviewer | System-of-record matrix, classification, retention and lineage | B-D | NON-WAIVABLE while critical finding open |
| TC-04 | Security Threat Model | Security Architecture | Security Specialist + Human Security Reviewer | Threat model, mitigations and residual-risk decision | B-D | NON-WAIVABLE while critical finding open |
| TC-05 | Privacy and Regulatory Compliance | Privacy and Compliance | Privacy/Compliance Specialist + Human Compliance Reviewer | Processing purpose, data subject handling, retention and control mapping | B-D | NON-WAIVABLE while critical finding open |
| TC-06 | Secrets and Key Management | Security/Infrastructure | Security and DevSecOps Specialists | Key lifecycle, secret storage, rotation and access evidence | B-D | NON-WAIVABLE while critical finding open |
| TC-07 | Accounting and Thai Tax Integrity | Module/Data Architecture | Accounting/Thai Tax Specialist + Human Accounting Reviewer | Posting integrity, tax rules, audit trail and reconciliation evidence | B-D | NON-WAIVABLE while critical finding open |
| TC-08 | Backup, Restore and Recovery Integrity | Resilience Architecture | Backup/DR Specialist + Human Infrastructure Reviewer | RTO/RPO, backup evidence, restore test and DR exercise | B-D | NON-WAIVABLE while critical finding open |

## Veto Rule

An open CRITICAL finding in any Trust Control causes automatic HOLD or FAIL for the affected gate.

No specialist review = No gate pass.
No required evidence = No gate pass.
Expired evidence = Gate returns to HOLD.

## Review Result Values

- PASS
- HOLD
- FAIL
- NOT REVIEWED

Conditional Pass is not permitted for an open critical Trust Control finding.
