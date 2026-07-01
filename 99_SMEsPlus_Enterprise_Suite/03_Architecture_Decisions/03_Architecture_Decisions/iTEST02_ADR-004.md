# ADR-004: Governance for Vector and AI-Related Database Capabilities

**Status:** PROPOSED  
**Date:** 2026-07-02  
**Context:** iTEST02 PostgreSQL dump analysis  
**Owner:** TBD  
**Related folder:** `03_Architecture_Decisions`

## Context

The dump includes the `vector` extension and AI/knowledge-related tables. This indicates possible semantic search, chatbot, knowledge base, or AI workflow usage.

## Decision

AI-related tables and vectorized content must be treated as a distinct governance domain with separate review for data provenance, personal data leakage, and model context sharing.

## Consequences

### Positive

Supports future AI features while keeping knowledge data and embeddings under governance.

### Negative / Risk

May require specialized review because vector content can indirectly encode sensitive source data.

## Evidence Required

- List of AI and knowledge tables
- Extension compatibility evidence
- Data source register
- AI usage and sharing policy

## Gate Mapping

| Gate | Result | Reason |
|---|---|---|
| Functional design evidence | PASS | Based on extracted schema metadata |
| Technical validation | CONDITIONAL | Requires restore or owner review |
| Security / privacy | HOLD | Sensitive columns are present |
| Production readiness | HOLD | Not approved until validation completes |

## Next Action

Create AI data provenance register before using restored content for AI workflows.
