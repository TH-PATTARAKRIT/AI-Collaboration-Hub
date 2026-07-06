# Module Tiering Strategy

Owner: Enterprise Architect AI
Reviewers: PMO AI, Functional Specification AI
Status: Draft

## Tiers
- Tier 1 — Core / Thai Localized / High-Risk Modules: full FDS required
  (Accounting, Inventory, Purchase, Sales, Manufacturing/MRP, Product/Master Data,
  Thai Localization/Tax).
- Tier 1.5 — Mixed-Risk / Escalation Modules: Expenses, HR/Payroll-related.
- Tier 2 — Standard / Low-Risk Modules: Lite FDS acceptable
  (CRM unless connected to quotation/sales flow, Leave, Recruitment).

## Tier Assignment Rules
- A module is Tier 1 if it touches statutory/Thai tax compliance, core financial
  ledgers, or cross-module inventory/valuation logic.
- A module is Tier 1.5 if it has partial statutory exposure or feeds payroll/HR
  compliance without being the core accounting engine.
- A module defaults to Tier 2 unless it has a direct, documented dependency into a
  Tier 1 module's data or approval flow (e.g. CRM feeding Sales quotation).

## Metadata Requirements
Every module FDS must declare: tier, owner AI role, reviewer roles, ADR reference
(if applicable), evidence status, and gate state.

## Forbidden Behavior
- No module may be silently reclassified from Tier 1 to Tier 2 without an ADR.
- No Tier 2 Lite FDS may substitute for a Tier 1 Full FDS.

## Gate Impact
Tier 1 modules require Functional Design gate PASS before Build Ready is considered.
Tier 2 modules may proceed on Lite FDS with PMO sign-off.
