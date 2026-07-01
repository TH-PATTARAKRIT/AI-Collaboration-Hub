# iTEST02 Data Governance Controls

**Generated date:** 2026-07-02

## Control Objective

Protect production-like ERP data during analysis, restore, migration design, and AI-assisted documentation.

## Sensitive Data Classes

| Class | Examples | Minimum control |
|---|---|---|
| PII contact | name, email, phone, address | Mask or tokenize |
| HR employee | employee, contract, payroll fields | Restrict and mask |
| Financial | bank, account, payment, tax fields | Restrict, mask, reconcile |
| Authentication | token, key, secret, password, session | Purge or rotate |
| Communication | mail, message, body, description | Mask or exclude |
| AI and knowledge | embeddings, chatbot, document content | Review before reuse |

## Clean-Room Rules

1. Use only schema-level exports for general design work.
2. Do not share row-level data until masking is complete.
3. Do not paste sensitive extracts into AI tools.
4. Treat all tokens, keys, and sessions as compromised if restored outside production.
5. Use role-based access for the restore environment.
6. Capture evidence for every transition from HOLD to PASS.

## Masking Priority

| Priority | Data | Action |
|---|---|---|
| P0 | passwords, tokens, API keys, sessions | purge or rotate |
| P1 | employee, payroll, bank, tax identifiers | mask before sharing |
| P2 | customer and vendor contact details | mask or tokenize |
| P3 | messages, descriptions, attachments | sample, redact, or exclude |
| P4 | product and configuration metadata | usually safe after review |

## Recommended Repository Handling

Store only metadata reports and diagrams in GitHub unless the repository is private and access-controlled. Never commit the raw `.dump` file or unmasked row-level exports.
