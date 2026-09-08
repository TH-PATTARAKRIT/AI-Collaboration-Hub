# SMEPLUS CLEAN-ROOM NATURE DNA CONSTITUTION

Status: BOSS APPROVED  
Authority: Boss — Sole Final Approver

## 1. Source-learning boundary

Reference systems, including v18, v19, SAP, Salesforce and other ERP systems, may be used for:

- learning;
- experimentation;
- benchmark;
- source/code/database study;
- business-semantic discovery;
- control/risk discovery;
- edge-case discovery;
- UX familiarity and comparison.

They are NOT, by default:

- SMEsPlus Design Authority;
- SMEsPlus Schema Authority;
- SMEsPlus ORM Authority;
- SMEsPlus Workflow Authority;
- SMEsPlus State Model Authority;
- SMEsPlus UI Authority;
- SMEsPlus Ownership Boundary Authority.

Common ERP/business terminology may be reused where semantically correct. Similarity is allowed; dependency is not.

## 2. Clean-room synthesis rule

Every Phase SA functional design must pass this sequence:

SOURCE EVIDENCE -> BUSINESS FACT -> BUSINESS SEMANTIC -> CONTROL/RISK -> ALTERNATIVE MODELS -> SMEPLUS PRINCIPLE -> CLEAN-ROOM DESIGN -> CHALLENGE

The design team must not jump directly from source structure to SMEsPlus structure.

## 3. Minimum Phase SA rationale

For every material functional area, Phase SA must answer:

1. What did we learn?
2. What did we deliberately NOT inherit?
3. What is SMEsPlus doing better or differently?
4. What is the independent SMEsPlus rationale for the selected model?

If the answer to #3 or #4 is absent for a material design, the design is NOT READY for Boss approval.

This does not require artificial novelty. A conventional pattern may be selected when independently justified. The reason must never be merely 'the reference system does it this way.'

## 4. SMEsPlus Nature DNA

Every canonical SMEsPlus design must establish its own:

- identity;
- ownership;
- lifecycle;
- event semantics;
- control model;
- audit lineage;
- Tenant boundary;
- Company boundary;
- integration contract;
- data-retention/correction semantics.

## 5. Database namespace constitution

All SMEsPlus-owned persistent business tables MUST use the `smeplus_*` namespace.

Examples include:

- `smeplus_company`
- `smeplus_product`
- `smeplus_product_category`
- `smeplus_account`
- `smeplus_accounting_event`
- `smeplus_journal_entry`
- `smeplus_journal_item`
- `smeplus_payment`
- `smeplus_reconciliation`
- `smeplus_inventory_valuation`
- `smeplus_cost_layer`
- `smeplus_audit_event`

Naming alone is not proof of clean-room design. The underlying object model and behavior must also satisfy the independent-rationale rule.

## 6. Permanent principles

**SOURCE IS EVIDENCE, NOT DESIGN.**  
**LEARN BEHAVIOR, NOT STRUCTURE.**  
**TRANSFER BUSINESS MEANING, NOT APPLICATION ARCHITECTURE.**  
**EVERY SMEPLUS DESIGN MUST HAVE AN INDEPENDENT CLEAN-ROOM RATIONALE.**  
**THE TARGET IS NOT PARITY WITH THE REFERENCE SYSTEM; THE TARGET IS A BETTER SMEPLUS SYSTEM.**
