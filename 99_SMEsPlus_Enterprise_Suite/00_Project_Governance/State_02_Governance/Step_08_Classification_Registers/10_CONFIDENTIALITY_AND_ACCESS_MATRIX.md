# 10_CONFIDENTIALITY_AND_ACCESS_MATRIX.md

Order: /L99.99 — State 02, Step 08 — Classification Registers
Work Package: WP-08-10 — Confidentiality and Access Matrix
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Working Branch: claude/state-02-classification-registers-7qwwcy
Prepared By: Claude Code (Preparer / Executor — Responsible role only)
Prepared At: 2026-07-14 (UTC)
Document Status: PREPARED FOR INDEPENDENT REVIEW
Gate Status: HOLD

## 1. Confidentiality Levels

```text
PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED
SECRET / CREDENTIAL — REFERENCE ONLY
```

## 2. Secret-Handling Rule (absolute)

Never copy credentials, passwords, tokens, private keys, or secrets into any register,
report, matrix, or evidence file. Record only a controlled reference to the secret-storage
location (e.g., "stored in the project secret manager; access via secret owner"). No secret
value appears anywhere in this Step 08 package.

## 3. Confidentiality × Access Matrix

| Level | Who may View | Who may Edit | Who may Approve | Storage | Export | Evidence Handling | Retention | Redaction |
|---|---|---|---|---|---|---|---|---|
| PUBLIC | All roles + external | DC | Boss | Repository (public) | Allowed | Normal | Per registry | None |
| INTERNAL | All project roles | DC, Owner | Boss | Repository (internal) | Internal only | Normal | Per registry | None |
| CONFIDENTIAL | Boss, ES, named Owner, L99, EV | Owner (controlled) | Boss | Repository (controlled) | Prohibited without Boss | Access logged | Retain; no delete | Redact on external share |
| RESTRICTED | Boss, ES, named Owner only | Owner (Boss-authorized) | Boss | Controlled store | Prohibited | Access logged + reviewed | Retain; no delete | Redact all identifiers on share |
| SECRET / CREDENTIAL — REFERENCE ONLY | Secret owner + Boss | Secret owner only | Boss | Dedicated secret manager (NOT the repo) | Prohibited | Reference-only; never inline | Per security policy | Full — value never written |

## 4. State 02 / Step 08 Classification Assignments

| Item / Class | Confidentiality | Access | Rationale |
|---|---|---|---|
| Step 08 registers (docs 00–17) | INTERNAL | View: all project roles; Edit: DC/Owner; Approve: Boss | Governance documentation, no secrets |
| Document Classification Register (doc 03) | INTERNAL | as above | Repository paths only |
| Evidence Register (doc 05) | INTERNAL | as above | Paths, SHAs; no secrets |
| RACI / Authority docs | INTERNAL | as above | Role model; no secrets |
| SHA-256 manifest | INTERNAL | View all; Edit DC | Integrity hashes only |
| Validation script | INTERNAL | View all; Edit Owner | Read-only tool; no secrets |
| Any credential/token | SECRET — REFERENCE ONLY | Secret owner + Boss | None present in this package |

## 5. Confidentiality Validation

The validation script scans register files for common secret patterns (e.g., `password=`,
`token`, `BEGIN PRIVATE KEY`, `AKIA...`, high-entropy assignments) and flags any match as an
invalid confidentiality classification (a secret must never appear inline). Result for this
package: no inline secret detected (see STEP08_VALIDATION_REPORT.md).

## 6. Control Statement

No secret value is stored in this package. All Step 08 governance content is INTERNAL. Boss
is the sole approver for any confidentiality reclassification with authority or export impact.
