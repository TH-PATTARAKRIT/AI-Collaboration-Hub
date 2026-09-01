# Five-Unit Pre-Prompt Challenge — Inventory H2/H3 Targeted Closure CORR-004

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Target: `Inventory Core DR-002 H2/H3 targeted evidence reconciliation`  
Risk Class: `HIGH`  
Boss: `Sole Final Approver`

## 1. Audit VETO — Evidence / Governance Challenge

Questions challenged:

- Does H2 require unavailable `bh_parent_company` Python source before Inventory can move?
- Does H3 require continued source reading even after current Odoo/OCA source and Revenue Department evidence are available?
- Would declaring H2/H3 fully "resolved" silently erase still-valid migration/user-validation unknowns?

Result:

`NO VETO — PROCEED WITH GATE-LEVEL CLOSURE, NOT UNIVERSAL CLOSURE.`

Mandatory controls:

1. H2 may close only as an Inventory research/gate blocker. Vendor internal workflow/validation remains UNKNOWN until source is obtained.
2. H3 may close only as an Inventory research/gate blocker. Customer-specific actual field usage remains `REQUIRES REAL USER VALIDATION` for migration.
3. Do not convert the BHPRO model or either Odoo branch representation into SMEsPlus target architecture.
4. TEAM A must update its own evidence registers; the Independent Reviewer must re-check the delta before Boss Gate decision.

## 2. TBRAC — Thailand Reality Challenge

Evidence now available:

- Revenue Department VAT Notification No. 39 establishes Head Office/Branch identification requirements on tax invoices, including `00000` for Head Office and registered branch identity for branches.
- Odoo 18 and OCA 18 source converge on `company_registry` for branch-code representation, while OCA 16 used a separate `branch` field.

TBRAC finding:

- Regulatory branch identity is now materially clearer.
- Source representation is implementation-specific and must not be treated as Thailand-wide architecture.
- Customer operational usage still requires real-user validation if needed for migration.

Result:

`PROCEED — STATUTORY FACT MAY BE FROZEN; CUSTOMER USAGE REMAINS CONTROLLED CARRY-FORWARD.`

## 3. EXPERT IBPV — Business Process / Design Challenge

Advisory questions:

- Does H2 affect Inventory business state, quantity, reservation, warehouse, or valuation? Evidence says no direct Stock Truth dependency.
- Does H3 affect Stock Truth directly? Evidence says no; it is a future organizational/tax-scoping concern.
- Can either finding dictate canonical target design? No.

Result:

`PROCEED — CLOSE INVENTORY RESEARCH GAPS; PRESERVE CROSS-DOMAIN INTERFACE NOTES.`

## 4. EXPERT IDTM — Future Deep Test Challenge

Advisory carry-forward:

- Future migration tests should verify legacy Partner/Brand/HQ mapping if H2 data is migrated.
- Future Thai branch tests should verify Head Office/Branch identity, document output, and company/tenant isolation against the final canonical design.
- No formal IDTM execution is authorized now.

Result:

`ADVISORY ONLY — NO BLOCKER TO TARGETED EVIDENCE RECONCILIATION.`

## 5. EXPERT IESA — Enterprise / SaaS Assurance Challenge

Advisory carry-forward:

- H2 is a customer-specific extension and therefore a migration/provenance risk, not a reusable enterprise invariant.
- H3 is a tax/business-identity fact that must remain separate from legal-company and tenant identity unless later canonical design explicitly relates them.
- Do not treat child-company hierarchy as a Thai statutory branch requirement.

Result:

`ADVISORY ONLY — NO SYSTEM-LEVEL VETO.`

## 6. Joint Prompt Readiness

`Risk = HIGH`  
`Audit VETO = NO VETO`  
`TBRAC = PROCEED WITH CONTROLLED CARRY-FORWARD`  
`IBPV = PROCEED`  
`IDTM = ADVISORY ONLY`  
`IESA = ADVISORY ONLY`  
`Critical Blocking Unknown Before Start = NONE`

### Prompt Readiness

`READY — TEAM A H2/H3 TARGETED CORRECTIVE RECONCILIATION MAY START`

The authorized Team must discover/reconcile the evidence. Independent experts challenge the questions; they do not provide an answer key or self-approve the result.

`Ask until materially clear — not until everyone agrees.`