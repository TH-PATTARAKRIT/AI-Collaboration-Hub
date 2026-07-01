# iTEST02 Prompt Pack Index

**Package:** iTEST02 Governance Prompt Pack  
**Date:** 2026-07-02  
**Repository area:** `99_SMEsPlus_Enterprise_Suite/05_Prompts`  
**Rule:** No raw row data, credentials, tokens, private employee data, bank details, or customer PII may be pasted into AI prompts.

## Purpose

This folder provides reusable prompts for continuing analysis of the iTEST02 PostgreSQL/Odoo-style dump without exposing sensitive data. Prompts are designed for schema-only review, evidence-based delivery, migration readiness checks, and owner signoff preparation.

## Prompt Files

| File | Purpose |
|---|---|
| `PROMPT_schema_only_analysis.md` | Analyze schema metadata only |
| `PROMPT_sensitive_data_classification.md` | Classify sensitive columns and define controls |
| `PROMPT_erd_by_module_generation.md` | Generate module ERD notes |
| `PROMPT_evidence_gate_review.md` | Review evidence gate status |
| `PROMPT_migration_readiness_assessment.md` | Assess migration readiness |
