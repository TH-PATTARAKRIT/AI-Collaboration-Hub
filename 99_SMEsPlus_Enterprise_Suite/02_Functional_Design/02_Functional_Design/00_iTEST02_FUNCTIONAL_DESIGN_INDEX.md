# iTEST02 Functional Design Analysis Index

**Generated date:** 2026-07-02  
**Source dump:** `iTEST02_2026-06-14_14-41-19.dump`  
**Target repository path:** `99_SMEsPlus_Enterprise_Suite/02_Functional_Design/`

## Purpose

This package converts the PostgreSQL custom dump review into functional design evidence for the SMEsPlus Enterprise Suite repository. It is intended to support ERP discovery, migration planning, data privacy review, and module-level design discussions.

## Included Evidence

| File | Purpose |
|---|---|
| `README_iTEST02_analysis.md` | Short overview of the database analysis package |
| `iTEST02_module_inventory.csv` | Module grouping, table counts, and relationship counts |
| `iTEST02_foreign_keys.csv` | Extracted foreign key relationship inventory |
| `iTEST02_sensitive_columns_inventory.csv` | Sensitive column inventory by category |
| `iTEST02_sensitive_data_summary_by_category.csv` | Aggregated sensitive data counts |
| `iTEST02_sensitive_data_risk_report.md` | Risk analysis and mitigation recommendations |
| `iTEST02_ERD_Accounting_Finance.md` | Functional ERD notes for accounting and finance |
| `iTEST02_ERD_Sales_CRM.md` | Functional ERD notes for sales and CRM |
| `iTEST02_ERD_Inventory_Purchase.md` | Functional ERD notes for inventory and purchasing |
| `iTEST02_ERD_HR_Payroll.md` | Functional ERD notes for HR and payroll |
| `iTEST02_functional_design_assumptions.md` | Assumptions, scope, and limitations |
| `iTEST02_evidence_gate_report.md` | Evidence gate status using No Evidence equals No Progress |
| `iTEST02_migration_readiness_checklist.md` | Migration readiness checklist |
| `iTEST02_restore_validation_plan.md` | Restore and validation plan |
| `iTEST02_data_governance_controls.md` | Data privacy and clean-room handling controls |
| `iTEST02_repository_commit_plan.md` | Suggested Git commit and pull request plan |
| `iTEST02_functional_design_governance_flow_diagram.md` | Online governance flow diagram links |

## Current Assessment

The dump represents a broad ERP implementation with accounting, CRM, stock, purchase, HR, payroll, manufacturing, website, documents, and AI-related capabilities. The schema is large enough that module-level documentation is safer than a single global ERD. Sensitive data handling should be treated as mandatory before any restore, AI analysis, vendor sharing, or non-production reuse.
