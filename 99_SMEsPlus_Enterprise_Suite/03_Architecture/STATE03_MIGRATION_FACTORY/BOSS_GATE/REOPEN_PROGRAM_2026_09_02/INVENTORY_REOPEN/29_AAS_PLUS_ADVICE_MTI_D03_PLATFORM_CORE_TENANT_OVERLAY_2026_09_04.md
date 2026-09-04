# AAS+ Advice — MTI-D-03 Platform-owned Core + Tenant Config Overlay

## 1. Advice Identity

Project: SMEsPlus ENTERPRISE SUITE
Workstream: Inventory Deep Research R4 / Multi-Tenant Invariant Set
Related Boss Ruling: MTI-D-03
Advice Body: AAS+ — AI Audit SMEsPlus
Date: 2026-09-04
Status: RECORDED AFTER BOSS APPROVAL

## 2. AAS+ Recommendation Confirmed

AAS+ recommends and Boss approves:

`Platform-owned Core + Tenant Config Overlay`

This is the correct boundary for shared SaaS pool Inventory design.

## 3. Interpretation

The shared SaaS pool should keep common platform logic centrally governed while allowing each tenant/company to configure its own operational master data.

Examples include Warehouse, Location, Route, Rule, Operation Type, Putaway Rule, Reordering Rule, Storage Category, Product Category, Unit of Measure Category, and Barcode Nomenclature.

The design should not assume that duplicated configuration across companies is a defect. Different companies may use similar labels with different business meaning, tax treatment, operational practice, approval control, or reporting consequence.

## 4. Two-Lane Operating Model

AAS+ advises downstream design to separate the model into two lanes:

| Lane | Purpose | Boundary |
|---|---|---|
| SaaS Pool | Standard shared SaaS operation | Platform core + tenant/company configuration overlay |
| Private Company | High-specificity customer operation | Explicitly opened by governance when shared SaaS pool is not enough |

Private Company may be available as a future operating option, but it must not be treated as automatically approved for every customer-specific requirement.

## 5. Proof Requirements

Downstream proof must show:

1. Which Inventory records are platform-owned.
2. Which Inventory records are tenant/company-configurable.
3. Which configuration changes are allowed in the shared SaaS pool.
4. Which changes require Private Company escalation.
5. How MTI-D-01 product isolation remains intact.
6. How MTI-D-02 Company + Warehouse + Operation-Type authorization remains intact.
7. How cross-tenant leakage is prevented in UI, API, report, scheduler, import, export, and audit trail.
8. How configuration changes are versioned, auditable, and reversible where applicable.

## 6. AAS+ Caution

The phrase Tenant Config Overlay must not be interpreted as allowing uncontrolled customer customization.

It means controlled configuration within a platform-owned boundary.

If a customer requirement needs source-level behavior, schema-level divergence, posting behavior divergence, or isolation-rule divergence, AAS+ recommends moving it to Private Company evaluation rather than modifying the shared SaaS pool.

## 7. HOLD Condition

If downstream design cannot classify a requirement as SaaS Pool-safe or Private Company-required, the item must remain HOLD until classification evidence exists.

## 8. Gate Boundary

This file is not a Development Final Gate, not a build authorization, and not a production release authorization.

It is a Boss-approved control ruling and AAS+ advisory record for Inventory v2.0 preparation.
