# CORR-007B — Clean-room Compliance Review

Project: SMEsPlus ENTERPRISE SUITE  
Branch: `audit/inventory-core-corr007b-3high-closure-010`  
Context: Boss-approved dual mandate: 9 Veto Challenge Council + 9 Special Team Challenge  
Status: Clean-room governance review only; not Gate PASS; not Team B/C authorization

## 1. Clean-room Principles

Boss reaffirmed that SMEsPlus must remain 100% Clean-room.

The mandatory principles are:

1. **Reference Only**  
   Odoo / SAP / Salesforce / Legacy / Dump are for learning, benchmarking, and business-semantic proof only.

2. **No Copy / No Clone / No Reuse**  
   No source code, XML, QWeb, ORM, schema, workflow, naming pattern, or application architecture may be copied, cloned, or reused as SMEsPlus target implementation.

3. **Migrate Business Facts + Business Semantics Only**  
   SMEsPlus may migrate facts and meanings, not legacy application architecture.

4. **SMEsPlus Target Design Must Be Original**  
   SMEsPlus target design must be a new clean-room Node.js SaaS ERP design supported by evidence and Boss approval.

## 2. Compliance Boundary for Source/Dump Learning

Allowed use of Odoo and dump evidence:

- identify business concepts;
- identify process variants;
- identify accounting/stock semantics;
- identify configuration ownership, such as Product Category-level valuation policy;
- identify reference source mechanism;
- identify migration facts;
- define SMEsPlus business rules independently.

Disallowed use:

- copying Odoo Python/XML/QWeb code;
- copying ORM models;
- cloning schema;
- cloning workflows;
- copying UI/report layout into target product;
- using Odoo naming as canonical identity without independent SMEsPlus definition;
- using reference architecture as target architecture.

## 3. N-A12-01 Clean-room Risk

N-A12-01 is high-risk for clean-room drift because the issue involves Odoo Product Category valuation policy, stock_account source behavior, periodic/perpetual valuation, and accounting close workflow.

The correct clean-room handling is:

1. use Odoo Product Category settings as reference evidence only;
2. extract business semantics:
   - valuation policy belongs to category/grouping;
   - products inherit policy from grouping;
   - manual vs automated valuation changes accounting timing;
   - costing method changes valuation computation;
   - monthly close requires stock/accounting cut-off;
   - year-end close transfers profit/loss to retained earnings;
3. design SMEsPlus independently:
   - clean-room domain model;
   - clean-room event model;
   - clean-room close contract;
   - clean-room posting contract;
   - clean-room UAT scenarios;
4. avoid copying Odoo schema, ORM, QWeb, source implementation, or UI layout.

## 4. Clean-room Challenge Questions

The 9 Veto Challenge Council and 9 Special Team Challenge must ask:

1. Are we using Odoo only as reference?
2. Are we copying code, XML, QWeb, schema, workflow, or architecture?
3. Are we extracting business semantics only?
4. Is the SMEsPlus target rule original?
5. Can every target rule be explained without depending on Odoo internals?
6. Is any field or module name being treated as canonical identity without independent SMEsPlus definition?
7. Are source/dump facts separated from recommendations?
8. Are carry-forward items controlled with owner, target gate, and evidence requirement?
9. Does the recommendation overstate evidence?

## 5. Immediate Clean-room Finding

The current N-A12-01 source-mechanism proof is acceptable as reference evidence, but not sufficient as clean-room functional design.

A clean-room SMEsPlus design still requires original definition of:

- Product Group / Category valuation policy;
- valuation method configuration hierarchy;
- periodic/perpetual posting behavior;
- monthly close command and lock flow;
- stock movement cut-off rule;
- inventory valuation-to-GL reconciliation;
- retained earnings transfer at year-end;
- opening balance carry-forward;
- audit trail and approval workflow.

## 6. Compliance Disposition

`N-A12-01 = NOT CLEAN-ROOM FUNCTIONAL DESIGN CLOSED`

Reason:

Reference source mechanisms have been read, but SMEsPlus original functional design has not yet been proven, challenged, and accepted through the dual challenge model.

This review does not declare Gate PASS and does not authorize Team B or Team C.
