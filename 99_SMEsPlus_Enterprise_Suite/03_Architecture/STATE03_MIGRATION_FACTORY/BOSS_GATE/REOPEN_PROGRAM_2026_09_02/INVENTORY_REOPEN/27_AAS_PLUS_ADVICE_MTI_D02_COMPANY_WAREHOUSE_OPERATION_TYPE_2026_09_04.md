# AAS+ Advice — MTI-D-02 Company + Warehouse + Operation-Type

## 1. Advice Identity

Project: SMEsPlus ENTERPRISE SUITE
Workstream: Inventory Deep Research R4 / Multi-Tenant Invariant Set
Related Boss Ruling: MTI-D-02
Advice Body: AAS+ — AI Audit SMEsPlus
Date: 2026-09-04
Status: RECORDED AFTER BOSS APPROVAL

## 2. AAS+ Recommendation Confirmed

AAS+ recommends and Boss approves:

`Company + Warehouse + Operation-Type`

This is the correct Inventory authorization granularity for SaaS tenant separation and internal operational control.

## 3. Why This Is Required

Company-only authorization is too broad for Inventory because Inventory actions are not only accounting ownership events. They are also physical and operational events.

Warehouse-only authorization is incomplete because warehouse records must still be tenant/company-bound.

Operation-Type-only authorization is incomplete because operation types must operate inside a tenant/company and warehouse context.

Therefore, the minimum enforceable context for controlled Inventory action is:

`tenant/company + warehouse + operation type`

## 4. Control Implications

AAS+ advises that downstream design must prove the following:

1. Every Inventory action resolves tenant/company context before execution.
2. Every warehouse-sensitive action resolves warehouse context before execution.
3. Every operation-sensitive action resolves operation-type context before execution.
4. Permission checks must run before search, selection, confirmation, posting handoff, report generation, export, import, scheduler execution, and API execution.
5. No user interface, API, background job, report, or reconciliation view may expose another tenant/company's Inventory data.
6. Same-company access must still be restricted by warehouse and operation type where the role requires it.

## 5. Proof Requirements

Downstream proof must include at least:

- Positive access proof for an allowed company/warehouse/operation-type combination
- Negative access proof for another company
- Negative access proof for another warehouse in the same company
- Negative access proof for another operation type in the same warehouse
- Report/export isolation proof
- Scheduler/background job context proof
- API/import context proof
- Audit trail proof showing who performed what action under which tenant/company/warehouse/operation type

## 6. HOLD Condition

If a downstream package cannot produce proof for this control, AAS+ must keep the relevant item in HOLD.

This ruling specifies the required control model; it does not verify that the model has been built.

## 7. Gate Boundary

This file is not a Development Final Gate, not a build authorization, and not a production release authorization.

It is a Boss-approved control ruling and AAS+ advisory record for Inventory v2.0 preparation.
