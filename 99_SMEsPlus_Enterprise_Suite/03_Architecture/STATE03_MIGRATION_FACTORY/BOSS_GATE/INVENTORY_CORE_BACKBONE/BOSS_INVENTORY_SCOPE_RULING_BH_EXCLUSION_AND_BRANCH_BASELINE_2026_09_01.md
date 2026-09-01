# Boss Inventory Scope Ruling — bh/bhpro Exclusion and Approved Branch Baseline

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Effective date: `2026-09-01`  
Authority: `Boss — Sole Final Approver`

## 1. Binding Scope Rulings

### 1.1 `bh_*` / `bhpro_*` source-learning exclusion

All source modules, packages, folders, namespaces, models, or implementation artifacts whose identifying module/package prefix begins with:

- `bh_*`
- `bhpro_*`

are **EXCLUDED / OUT-OF-SCOPE FOR SMEsPlus SOURCE LEARNING**.

Reason supplied by Boss: these modules are considered incomplete / analytically unreliable and must not be used as a learning or architecture reference.

Permitted handling is limited to legacy-data provenance where necessary to avoid data loss during migration. The project may record that a legacy table/field/module exists, but must not derive target business logic, workflow, schema design, architecture, validation behavior, or canonical semantics from excluded source.

Therefore Inventory finding `H2 / GRPA-H5 — Partner Brand/HQ / bh_parent_company` is reclassified for Inventory purposes as:

`CLOSED BY BOSS SCOPE EXCLUSION / LEGACY MIGRATION DATA CARRY-FORWARD ONLY`

No further source acquisition or source study of `bh_parent_company`, `bh_brand`, `bh_store_type`, or other `bh_*` / `bhpro_*` modules is authorized for Inventory research.

### 1.2 Approved SaaS Multi-Company / Multi-Branch baseline must not be reopened

SMEsPlus already operates under an approved SaaS architecture baseline with Tenant, Company and Branch context. Downstream module research must verify its contract with that baseline; it must not re-research or redefine the Tenant / Company / Branch architecture unless new material evidence demonstrates a direct contradiction, compliance defect, or unresolvable business-reality conflict.

Binding control rule:

`Approved Platform Architecture must not be re-researched by downstream module teams unless new material evidence demonstrates a direct contradiction, compliance defect, or unresolvable business-reality conflict.`

For Inventory, this means Warehouse / Location / Stock Truth must preserve the approved Tenant / Company / Branch context, but Inventory research does not own the definition of the platform Branch model.

Therefore Inventory finding `H3 / GRPA-H8 — Thai Branch representation conflict` is reclassified as:

`CLOSED AS AN INVENTORY ARCHITECTURE QUESTION`

The remaining legacy `branch` versus `company_registry` question is a controlled Migration / TBRAC mapping carry-forward only. Customer real-user validation may still be required to determine which legacy field was operationally trusted for migration. Tax-document branch semantics remain an Accounting / Tax interface concern. None of these reopens the approved SMEsPlus Branch architecture and none is an Inventory Stock Truth blocker.

## 2. Mandatory Downstream Handling

1. H2 must not trigger any further `bh_*` / `bhpro_*` source research.
2. H3 must not trigger any further Branch architecture research in Inventory.
3. DR-002 registers must be reconciled so these two items are no longer represented as open Inventory research blockers.
4. Valid migration, TBRAC, Accounting/Tax, or real-user-validation carry-forwards must remain explicitly recorded rather than silently deleted.
5. Existing Independent Review evidence remains part of the audit trail; it is not rewritten retroactively.
6. Team B Inventory Design is not authorized by this ruling alone.
7. Inventory Evidence Gate remains a Boss decision after Team A register reconciliation and Independent Delta Re-Review.

## 3. Governance Invariants

- `No Evidence = No Progress.`
- `Never Skip Gate.`
- `Boss = Sole Final Approver.`
- `Unknown is not Fact.`
- `Scope exclusion is not implementation proof.`
- `Approved architecture is verified downstream; it is not repeatedly redesigned downstream.`
