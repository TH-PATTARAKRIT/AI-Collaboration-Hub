#!/usr/bin/env bash
set -euo pipefail

# SMEsPlus Architecture Office Setup Script
# Document ID: SMEPLUS-ARCH-OFFICE-SETUP-SH-v0.1
# Purpose: Create Architecture Office folders and baseline Markdown files.
# Usage: Run from repository root on branch SMEsPlus.

BASE_DIR="99_SMEsPlus_Enterprise_Suite/00_Architecture_Office"

mkdir -p "$BASE_DIR/ADR"
mkdir -p "$BASE_DIR/Enterprise_Standards"
mkdir -p "$BASE_DIR/Review_Checklists"
mkdir -p "$BASE_DIR/Governance"
mkdir -p "$BASE_DIR/Decision_Log"
mkdir -p "$BASE_DIR/Reference_Architecture"
mkdir -p "$BASE_DIR/Design_Patterns"

cat > "$BASE_DIR/ADR/README.md" <<'EOF'
# ADR

Purpose: Architecture Decision Records for SMEsPlus Enterprise Suite.

Rule: Every major architecture decision must have an ADR reference before implementation.

Minimum fields:

- ADR ID
- Decision title
- Status
- Context
- Decision
- Consequences
- Owner
- Review date
- Jira reference
- Evidence reference
EOF

cat > "$BASE_DIR/Enterprise_Standards/README.md" <<'EOF'
# Enterprise Standards

Purpose: Store enterprise-wide standards for architecture, functional design, data, security, integration, and quality.

Standards must be used before creating Jira execution work.

Core rule:

No standard alignment = ARG-HOLD.
EOF

cat > "$BASE_DIR/Review_Checklists/ARG_CHECKLIST.md" <<'EOF'
# Architecture Review Gate Checklist

Document ID: SMEPLUS-ARG-CHECKLIST-v0.1
Status: Approved for Execution
Owner: Architecture Office (ChatGPT)
Consumer: PMO Office (Jira), Engineering Office (Claude)

## Mandatory Rule

No ARG Pass = No Claude Development.

## Business Gate

- [ ] Requirement ID exists
- [ ] Business objective is clear
- [ ] Business value is stated
- [ ] Owner is identified
- [ ] Priority is defined
- [ ] Scope is clear

Result: PASS / HOLD / FAIL / ACCEPTED WITH CONTROL

## Functional Gate

- [ ] FDS section exists
- [ ] Functional Requirements exist
- [ ] Business Rules exist
- [ ] Workflow or process is clear
- [ ] Screen requirement exists where applicable
- [ ] Exception path exists where applicable

Result: PASS / HOLD / FAIL / ACCEPTED WITH CONTROL

## Data Gate

- [ ] Data model or entity list exists
- [ ] Master data impact is identified
- [ ] Tenant / company / branch scope is clear
- [ ] Traceability mapping exists
- [ ] Audit requirement is defined
- [ ] Data owner is identified where applicable

Result: PASS / HOLD / FAIL / ACCEPTED WITH CONTROL

## Integration Gate

- [ ] API requirement exists where applicable
- [ ] Event or webhook requirement exists where applicable
- [ ] External dependency is identified
- [ ] Internal dependency is identified
- [ ] Error and retry rule exists where applicable
- [ ] Security and permission impact is identified

Result: PASS / HOLD / FAIL / ACCEPTED WITH CONTROL

## Quality Gate

- [ ] UAT case exists
- [ ] Acceptance Criteria exists
- [ ] Test data need is identified
- [ ] Evidence requirement is identified
- [ ] Review owner is identified
- [ ] Done criteria is clear

Result: PASS / HOLD / FAIL / ACCEPTED WITH CONTROL

## Final ARG Result

ARG Result:
Business Gate:
Functional Gate:
Data Gate:
Integration Gate:
Quality Gate:
Final Architecture Decision:
Evidence Reference:
Reviewer:
Review Date:
Claude Execution Permission: YES / NO / CONTROLLED
EOF

cat > "$BASE_DIR/Governance/README.md" <<'EOF'
# Governance

Purpose: Store Architecture Office governance rules and gate policies.

Primary document:

- ARCHITECTURE_REVIEW_GATE.md

Mandatory rule:

No ARG Pass = No Claude Development.
EOF

cat > "$BASE_DIR/Decision_Log/README.md" <<'EOF'
# Decision Log

Purpose: Track approved decisions by CEO / Product Owner and Architecture Office.

Minimum fields:

- Decision ID
- Date
- Decision summary
- Approved by
- Impacted scope
- Jira reference
- GitHub reference
- Evidence reference
EOF

cat > "$BASE_DIR/Reference_Architecture/README.md" <<'EOF'
# Reference Architecture

Purpose: Store approved reference architecture for SMEsPlus Enterprise Suite.

Scope:

- SaaS architecture
- Multi-tenant architecture
- Identity and access architecture
- Integration architecture
- Data architecture
- AI execution architecture
EOF

cat > "$BASE_DIR/Design_Patterns/README.md" <<'EOF'
# Design Patterns

Purpose: Store approved design patterns for SMEsPlus Enterprise Suite.

Examples:

- Tenant-aware module pattern
- Approval foundation pattern
- Audit trail pattern
- Notification pattern
- AI task traceability pattern
- Jira mapping pattern
EOF

cat > "$BASE_DIR/README.md" <<'EOF'
# 00 Architecture Office

Document ID: SMEPLUS-ARCH-OFFICE-README-v0.1
Project: SMEsPlus Enterprise Suite
Status: Approved for Execution
Owner: Architecture Office (ChatGPT)
Approved by: CEO / Product Owner

## Purpose

This folder is the official Architecture Office control area for SMEsPlus Enterprise Suite.

## Structure

```text
00_Architecture_Office/
├── ADR/
├── Enterprise_Standards/
├── Review_Checklists/
├── Governance/
├── Decision_Log/
├── Reference_Architecture/
└── Design_Patterns/
```

## Mandatory Rule

No ARG Pass = No Claude Development.

## Control Flow

CEO / Product Owner -> Architecture Office (ChatGPT) -> PMO Office (Jira) -> Engineering Office (Claude) -> GitHub Repository
EOF

echo "Architecture Office structure created under: $BASE_DIR"
echo "Next step: git add $BASE_DIR && git commit -m 'Create Architecture Office baseline structure' && git push origin SMEsPlus"
