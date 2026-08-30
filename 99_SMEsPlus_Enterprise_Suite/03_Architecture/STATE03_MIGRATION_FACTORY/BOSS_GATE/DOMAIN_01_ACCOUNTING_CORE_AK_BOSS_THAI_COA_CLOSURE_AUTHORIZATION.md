# DOMAIN_01 Accounting Core — Boss Authorization: Thailand COA Architecture Closure & Boss Freeze

Date: 2026-08-30
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain: DOMAIN_01 — Accounting Core
Control Level: /L99.99
Final Approval Authority: Boss
Jira: ERPPLUS-132

## 1. Boss Decision

**APPROVED — OPEN `[STATE03][DOMAIN_01] SMEsPlus Thailand COA Architecture Closure & Boss Freeze / L99.99`.**

Boss approved the proposed dedicated COA closure work item and the controlled closure sequence before handoff to downstream teams.

This authorization is separate from ERPPLUS-100 so that completed DOMAIN_01 targeted-design revision evidence is not mixed with the remaining COA architecture closure work.

## 2. Objective

Close the remaining SMEsPlus Local Thailand COA architecture into a stable, evidence-backed architecture contract before downstream functional, data, migration, UX, engineering or other teams consume the COA baseline.

## 3. Authorized Closure Gates

### COA-G01 — Source Baseline Reconciliation
Reconcile authorized Accounting Core source, `l10n_th`, Boss-approved `Odoo18` workbook tab, Team A Deep Research, and Boss-provided Thai COA business requirements.

### COA-G02 — Base COA Kernel Discovery
Identify the smallest defensible Thailand baseline account set. The working expectation of approximately 32 baseline accounts is not a target mandate. Exact count remains `TBD / EVIDENCE REQUIRED` until proven.

### COA-G03 — AI Semantic Consolidation
Classify source accounts by business meaning and accounting treatment. Consolidate N source rows to one canonical account only where accounting treatment is materially equivalent. Preserve source provenance.

### COA-G04 — Account Type & Account Group Architecture
Use the Boss-approved 19 active Account Types. Account Group shall be maintainable per company while canonical accounting meaning and Account Type remain controlled.

### COA-G05 — Financial Statement Taxonomy
Map canonical accounts to standard financial-statement lines independently from company-specific Account Groups. Off-Balance Sheet shall be excluded from ordinary Balance Sheet / P&L totals by default and reportable separately under controlled rules.

### COA-G06 — Thailand Tax Accounting Controls
Evidence and map VAT, Undue VAT, WHT, CIT, non-deductible expense and other Thailand-specific controls. Statutory claims require authoritative evidence.

### COA-G07 — Multi-company & Dimension Proof
Prove that company-specific Account Groups do not break canonical reporting or consolidation. Prefer dimensions over GL-account proliferation where accounting treatment does not differ.

### COA-G08 — Independent Audit + PMO + Boss Freeze
ChatGPT Independent Audit -> PMO Verification -> Boss Final COA Freeze Gate.

## 4. Approved Existing Baseline

The closure work shall inherit these already-approved controls:

- DOMAIN_01 Accounting Core Team B Blueprint = Boss APPROVED WITH CONTROL.
- A1-A7 = Boss Approved / Evidence Recorded.
- COA Template / Instance direction = Boss Approved with prerequisite satisfied.
- SMEsPlus Local Thailand Account Type baseline = 19 ACTIVE types.
- `389 source rows != 389 target accounts`.
- `~32 Base Kernel` = working expectation only, not a frozen count.
- Account Code is not canonical identity.
- Account Group may be company-maintainable but shall not silently redefine canonical Account Type or financial-statement meaning.
- Clean-room boundary remains absolute: no source-code, ORM, schema, technical ID or vendor architecture cloning.

## 5. Mandatory Handoff Gate

No downstream team may treat the Thailand COA as a frozen architecture baseline until all of the following are evidenced:

- Thailand COA Source Baseline = VERIFIED
- Base COA Kernel = VERIFIED
- Canonical COA = FROZEN
- Account Group Rules = VERIFIED
- Financial Statement Mapping = VERIFIED
- Off-Balance Rules = VERIFIED
- Thailand VAT/WHT/CIT Controls = VERIFIED
- Multi-company / Dimension Proof = PASS
- Blocking COA Unknowns = 0
- ChatGPT Independent Review = PASS
- PMO Verification = PASS
- Boss COA Freeze Gate = APPROVED

## 6. Owner and Evidence Chain

Authorized execution chain:

`Team A Evidence -> Team B Independent Clean-Room Design -> ChatGPT Independent Audit -> PMO Verification -> Boss Final Freeze`

Jira Assignee: `UNASSIGNED` until governance assigns a named account.
Due Date: `TBD` until governance approves a date.

Every Gate must record:

- task / item
- owner or owner role
- evidence location
- timestamp
- reviewer / verifier
- verification status
- gate impact

## 7. Jira Traceability

Dedicated work item:

`ERPPLUS-132 — [STATE03][DOMAIN_01] SMEsPlus Thailand COA Architecture Closure & Boss Freeze / L99.99`

ERPPLUS-132 is linked to ERPPLUS-100 as `Relates`, but remains a separate work item to prevent scope/evidence mixing.

## 8. Authority Boundaries

This Boss authorization opens COA architecture closure work only.

Development Authorization = **NOT GRANTED**.
Production Authorization = **NOT GRANTED**.
Downstream implementation from an unfrozen COA = **NOT AUTHORIZED**.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
