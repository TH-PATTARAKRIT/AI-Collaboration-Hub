# iTEST02 Architecture Decisions Index

**Repository path:** `99_SMEsPlus_Enterprise_Suite/03_Architecture_Decisions`  
**Source:** PostgreSQL custom dump `iTEST02_2026-06-14_14-41-19.dump`  
**Generated:** 2026-07-02  
**Status:** Draft for review

## Purpose

This package converts the functional design findings from `02_Functional_Design` into architecture decision records for the next governance stage. The dump shows a large Odoo-style ERP database with 1,395 tables, 5,141 foreign keys, and sensitive data categories across accounting, HR, CRM, website, documents, and AI/knowledge modules.

## Architecture Decision Records

| ADR | Title | Decision | Gate Status |
|---|---|---|---|
| ADR-001 | Restore in isolated environment | Required | HOLD until restore evidence exists |
| ADR-002 | Domain-based ERD and migration slicing | Required | PASS for documentation |
| ADR-003 | Sensitive data masking before sharing | Required | HOLD until masking evidence exists |
| ADR-004 | Vector and AI extension governance | Required | CONDITIONAL PASS |
| ADR-005 | Evidence-first repository promotion | Required | PASS for docs, HOLD for production |
| ADR-006 | Module owner signoff model | Required | HOLD until owners assigned |

## Decision Summary

The next architecture step is not to migrate immediately. The correct next step is to validate the dump in an isolated PostgreSQL restore environment, classify sensitive columns, confirm module ownership, and only then promote detailed migration actions. This follows the project control principle: **No Evidence = No Progress**.
