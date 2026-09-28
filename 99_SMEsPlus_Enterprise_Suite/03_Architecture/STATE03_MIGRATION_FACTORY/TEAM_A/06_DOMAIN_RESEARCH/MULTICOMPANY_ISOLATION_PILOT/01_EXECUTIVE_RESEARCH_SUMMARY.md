> Domain: MULTICOMPANY_ISOLATION_PILOT (Gx9) | Documentation-Tier

# 01 — EXECUTIVE RESEARCH SUMMARY (Gx9)

## Scope

Five functions: warehouse-company binding, inter-company transaction automation, shared/per-company Chart of Accounts, consolidation reporting, and warehouse-level user access control.

## Material finding 1 — company boundary is structural; warehouse-level user restriction is not

A warehouse's Company field is required and singular — a warehouse belongs to exactly one company, and users are linked to companies, which is a hard structural boundary. But documentation and multiple community threads confirm that restricting a specific user (already in the right company) to one specific warehouse **requires manually built record rules and per-warehouse security groups** — it is not a native, single-field "assign user to warehouse" configuration. Third-party apps exist specifically to fill this gap, corroborating that it isn't natively simple.

## Material finding 2 — inter-company automation is opt-in and configurable per-flow

"Inter-Company Transactions" is a per-company-pair toggle with four independently selectable behaviors: auto-create vendor bill from a confirmed sales invoice, auto-create sales order from a confirmed PO, auto-create PO from a confirmed SO, and synchronize stock moves. None of these are bundled as a single all-or-nothing switch.

## Material finding 3 — accounting can be shared or separate across companies

Each company can have its own Chart of Accounts, but accounts can also be shared across companies specifically to support consolidation reporting — this is a design choice, not a fixed architecture.

## Not established

Exact record-rule mechanics for warehouse restriction (not detailed in official documentation, only implied by forum questions and third-party apps). Full runtime confirmation, as always.
