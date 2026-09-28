# 01 — Source Code Research

Purpose: controlled forensic learning of source artifacts without transferring proprietary implementation into SMEsPlus design.

## Required Research Coverage

- Module identity and business capability
- Dependencies and cross-module coupling
- Models / entities and important fields
- Stored, non-stored, computed, related, and generated behavior
- Major business methods and validation points
- Lifecycle and state transitions
- Security and access behavior
- Accounting, inventory, manufacturing, tax, and integration impact
- Scheduled/background behavior
- Sequence and document-numbering behavior
- Reports, exceptions, and edge cases

## Research Method

1. Establish artifact identity, version, path, hash, and classification.
2. Apply source-class policy before source-body access.
3. Capture observation at behavioral and semantic level.
4. Separate business rule from framework mechanism.
5. Record evidence location, reviewer, confidence, and gate impact.
6. Transfer only independently expressible domain facts into business-semantic research.

## Prohibited Outputs

- Copied or translated source code
- Odoo ORM mappings used as target architecture
- Direct reuse of class, method, field, module, or workflow-engine structures
- Proprietary algorithms reproduced in target design

All detailed observations must be registered in `99_EVIDENCE_REGISTER/CODE_DEEP_RESEARCH_REGISTER.csv`.
