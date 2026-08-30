# DOMAIN_01 Accounting Core — Boss Final Gate Ruling

Date: 2026-08-30

## Authority

Boss = Sole Final Approver.

## Final Gate Decision

**APPROVE WITH CONTROL — DOMAIN_01 ACCOUNTING CORE TEAM B INDEPENDENT CLEAN-ROOM BLUEPRINT.**

This decision is based on:

- Team B Round-7 controlled design evidence and closure;
- ChatGPT Independent Re-Audit Round 8 — REVIEW PASS;
- PMO Design Verification — PASS / forward to Boss Final Gate;
- Boss ruling for Thailand COA standardization;
- controlled extraction evidence for the `Odoo18` tab prerequisite.

This approval is for the DOMAIN_01 conceptual/domain blueprint only. It does not by itself authorize Development or Production.

## A1–A7 Boss Rulings

| ID | Decision Topic | PMO Recommendation | Boss Ruling | Evidence / Condition | Final Status |
|---|---|---|---|---|---|
| A1 | Rounding Policy | Option B — configurable rounding policy | **APPROVED — OPTION B** | Preserve exact-decimal core; explicit policy/profile controls | BOSS APPROVED |
| A2 | Ordinary Period Reopen | Option A — no universal hard-coded time window | **APPROVED — OPTION A** | Period Lock and Consumption remain separate; Restatement protects relied-upon history | BOSS APPROVED |
| A3 | COA Template / Instance | Option A WITH CARRY-FORWARD | **APPROVED — OPTION A WITH CONTROL** | Boss required controlled item 1 first. Item 1 is now evidenced by COA source inventory commit `ae2b0719081ef9497f08e3b3e1ea8329d053cf83`; Thailand/Odoo18 COA direction is recorded at `27dd58f42bb63e6f2ed7f3389813490356e16ccc` | BOSS APPROVED — PRECONDITION SATISFIED |
| A4 | Audit Tamper-Evidence Scope | Option A — broader internal-control objective, not legal overclaim | **APPROVED — OPTION A** | Stronger tamper evidence may be designed as SMEsPlus internal control/advancement; must not be represented as statutory obligation without evidence | BOSS APPROVED |
| A5 | Correction Shape Flexibility | Option A — allow controlled reversal-repost and delta | **APPROVED — OPTION A** | Additive history, linkage, balance, audit and Restatement controls remain mandatory | BOSS APPROVED |
| A6 | CO-02 / CO-06 Coupling | Option A — approve coupling | **APPROVED — OPTION A** | Amendment path must not bypass stronger correction control/SoD configuration | BOSS APPROVED |
| A7 | Fiscal-Year Membership Restatement Authorization Tier | Option A — CO-15 Restatement-level-or-stricter | **APPROVED — OPTION A** | Post-reliance Fiscal-Year calendar/membership correction must never be authorized below Restatement control level | BOSS APPROVED |

## A3 — COA Prerequisite Closure

Boss required that controlled COA extraction item 1 be completed before A3 became effective.

### Item 1

> Extract and inventory the actual `Odoo18` tab rows/columns from the Boss-provided workbook.

Evidence:

- Workbook: `Account_Odoo18_19 sent 270369.xlsx`
- Boss-designated tab: `Odoo18`
- Source Drive ID: `1KoprCep3eeYy49OcV0TTFQOlc1zq9m2f`
- Evidence artifact: `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_STANDARD/DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md`
- Evidence commit: `ae2b0719081ef9497f08e3b3e1ea8329d053cf83`
- Verified inventory: 389 data rows, row indices `0–388`, five business columns: `id`, `name`, `reconcile`, `code`, `account_type`.

Therefore:

**A3 prerequisite item 1 = SATISFIED.**

**D01-GATE-A3 = BOSS APPROVED WITH CONTROL.**

The exact row-by-row SMEsPlus canonical mapping remains a downstream controlled work item before exact COA Blueprint Freeze.

## Thailand COA Baseline

Approved direction remains:

1. SMEsPlus Accounting COA standardization targets Thailand localization.
2. Non-Thai localization COA learning is excluded from this COA workstream unless Boss reopens scope.
3. `Odoo18` tab is the primary business-facing seed/reference for the SMEsPlus Standard Thai COA Candidate.
4. Account Type UX/classification should remain Odoo-like/familiar at the business-facing layer.
5. Canonical Account Type IDs, rules, data model and identity remain SMEsPlus-owned.
6. Architecture: `Standard Thai COA Template → Company/Tenant COA Instance → Source Mapping Layer`.
7. Account Code is not canonical identity.
8. Source mapping remains `Source Account → Business Meaning → SMEsPlus Canonical Classification → SMEsPlus Company Account`.
9. Express remains usability/reference benchmark only.
10. Odoo ORM/schema/source-code/technical-ID/module architecture cloning remains prohibited.

## Residual Unknown Control

Team A residual unknowns remain carry-forward and must not be converted into facts without evidence.

Governance note: the residual register currently contains a declared summary total that requires reconciliation against the individually enumerated open/partially-open IDs. Until reconciled, PMO must report the count as:

`RESIDUAL UNKNOWN COUNT = RECONCILIATION REQUIRED`

This count discrepancy does not reopen the approved Team B design findings, but it must be corrected before administrative closure of the DOMAIN_01 evidence package.

## Gate Effect

```text
DOMAIN_01 TEAM B BLUEPRINT = BOSS APPROVED WITH CONTROL
A1 = APPROVED
A2 = APPROVED
A3 = APPROVED — ITEM-1 PRECONDITION SATISFIED
A4 = APPROVED
A5 = APPROVED
A6 = APPROVED
A7 = APPROVED

Development Authorization = NOT GRANTED BY THIS RULING
Production Authorization = NOT GRANTED
DOMAIN_02 Authorization = NOT GRANTED BY IMPLICATION
```

## Next Controlled Work

1. Continue COA standardization from the verified `Odoo18` source inventory.
2. Build the row-level `Reference → Business Meaning → Canonical Classification → SMEsPlus Standard Thai COA Candidate` mapping.
3. Build Odoo-like Account Type labels with SMEsPlus-owned canonical IDs/rules.
4. Detect duplicates, classification anomalies and Thai-specific VAT/WHT/accounting dependencies.
5. Reconcile the Team A residual-unknown count.
6. Update PMO active decision register to show Boss-approved evidence status rather than recommendation-only status.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
