# [SMEPLUS-26-09-02-GRPA-INV-PARALLEL-001]
# STATE03 — Boss Directive: Active GROUP A Sales + Purchase, Inventory Backbone Parallel Closure, Account-First Cross-Proof Hold / L999.999

Date: 2026-09-02
Project: SMEsPlus ENTERPRISE SUITE
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Canonical Branch: `SMEsPlus`
STATE: STATE03 — Architecture
Boss: Sole Final Approver

## 1. Boss Decision

Boss approves the following controlled operating structure and continuation sequence:

1. Preserve all historical `GROUP_A_SALES_INVENTORY_PURCHASE` evidence exactly as audit lineage. Do not rewrite or delete historical Group A evidence merely because the active operating structure changes.
2. From this ruling forward, the **active GROUP A operating scope** for remaining non-backbone design closure is:

   `GROUP A = Sales + Purchase`

3. Inventory remains an independent Stock Truth domain but is governed operationally inside the dual-backbone program:

   `BACKBONE = Accounting Core / COA + Inventory / Stock Truth`

4. Sales + Purchase and Inventory may continue their own outstanding controlled closure work in parallel.
5. **Do not execute Accounting x Inventory Cross-Proof, Sales/Purchase final dependent reconciliation, downstream design freeze, Team C handoff, or Development readiness until Accounting Core / COA is fully closed through the controlled final COA Gate.**
6. For this directive, `Account complete` means:

   `COA-G08 Independent Audit + PMO + Boss Final COA Freeze = APPROVED / CLOSED`

7. After Account completion, perform:

   `Accounting x Inventory Cross-Proof -> Sales/Purchase dependent reconciliation -> controlled final design-freeze eligibility`

No Evidence = No Progress.
Never Skip Gate.
No Evidence Preservation = No Lifecycle Promotion.
No Backbone Reconciliation = No Dependent Design Freeze.
No Evidence Chain Seal = No Team C.
Boss is the sole Final Approver.

## 2. Current Verified Inputs

### 2.1 Accounting Core / COA

Current latest G03 Team B publication:

`82b5569af8601a47c0c395dbc3f28bbd26d43eb3`

Current status:

`COA-G01 = CLOSED`

`COA-G02 = CLOSED`

`COA-G03 = TEAM B COMPLETE / READY FOR FRESH INDEPENDENT AUDIT`

`COA-G04..G08 = NOT CLOSED`

Therefore:

`ACCOUNT / COA AS A WHOLE = NOT COMPLETE`

### 2.2 Historical GROUP A — Sales + Inventory + Purchase

Historical evidence lineage remains authoritative for prior lifecycle events under:

`GROUP_A_SALES_INVENTORY_PURCHASE`

Key CORR-010 Team B executor commit:

`e44186448eaae38926a78447639d6fa693cc1a6f`

Terminal Team B state from CORR-010:

`TEAM B NON-ACCOUNTING CORRECTIVE CLOSURE COMPLETE`

`READY FOR FORMAL IBPV RE-VERIFICATION`

`PRE-DEVELOPMENT GATE STILL HOLD FOR ACCOUNTING / CONTROLLED DEPENDENCIES`

Fresh Formal IBPV RV-011 governance/readiness and prompt:

- Five-Unit readiness: `b95f6ce7391a1ee6215df205f9b0baed58e93636`
- RV-011 execution prompt: `168cffee532d268b255e94e1928b22cd11bbd61e`

As of this ruling, no RV-011 execution-result commit has been verified on canonical `SMEsPlus`.

### 2.3 Inventory Backbone

Inventory remains the Stock Truth backbone and is no longer treated as an active GROUP A ownership domain for new lifecycle control.

Current controlled sequence has progressed to fresh independent delta re-review readiness:

- CORR-005 Five-Unit delta re-review readiness lineage exists.
- Fresh IDR-007 Five-Unit readiness: `54025627d63eb4055ff89f602454d9122876dfb2`
- Fresh IDR-007 execution prompt: `d5261b7a61cc317bccbaaf466c26417da6ba3486`

As of this ruling, no IDR-007 execution-result commit has been verified on canonical `SMEsPlus`.

## 3. Active Operating Model

Historical evidence taxonomy:

`Historical GROUP A = Sales + Inventory + Purchase — PRESERVED`

Active operating taxonomy from this ruling:

`Active GROUP A = Sales + Purchase`

`Inventory = Stock Truth Backbone`

`Accounting Core / COA = Financial Truth Backbone`

The use of the term `Backbone` does not merge Accounting and Inventory into one business domain. It creates one coordinated control program with two distinct authorities:

- Accounting owns Financial Truth / canonical accounting contract.
- Inventory owns Stock Truth / stock movement and inventory-managed-item control.
- Their interaction must be proven later through the dedicated Accounting x Inventory Cross-Proof.

## 4. Authorized Parallel Work — BEFORE Account Completion

### Track A — Sales + Purchase

Authorized next action:

`Formal IBPV RV-011 independent re-verification`

Use controlling prompt commit:

`168cffee532d268b255e94e1928b22cd11bbd61e`

Execution shall independently verify CORR-010 and may close authorized non-Accounting findings only.

It shall not:

- declare Pre-Development PASS solely because non-Accounting items pass;
- resolve Accounting-owned dependencies by assumption;
- authorize Team C;
- authorize Development;
- redefine Inventory ownership;
- perform Accounting x Inventory Cross-Proof.

If RV-011 passes non-Accounting scope, route to the next controlled PMO/Gate reconciliation while retaining Account-dependent holds.

### Track B — Inventory

Authorized next action:

`Fresh Independent Delta Re-Review IDR-007`

Use controlling prompt commit:

`d5261b7a61cc317bccbaaf466c26417da6ba3486`

Execution shall independently re-review the controlled CORR-005 delta and publish the exact PASS / HOLD / FAIL disposition allowed by its prompt.

It shall not:

- consume unfinished Account/COA design as final truth;
- freeze valuation/posting interfaces that depend on unfinished COA Gates;
- perform Accounting x Inventory Cross-Proof;
- authorize Team C or Development.

If IDR-007 passes, continue Inventory PMO/Gate reconciliation and Boss Inventory Evidence Gate only within its own controlled evidence scope.

## 5. Mandatory Account-First Integration Hold

The following activities are explicitly **HOLD** until Account / COA is complete through G08:

- Accounting x Inventory Cross-Proof;
- final Inventory valuation/posting contract freeze against COA;
- Sales final financial-impact reconciliation against Account + Inventory backbones;
- Purchase final AP/tax/stock-impact reconciliation against Account + Inventory backbones;
- final GROUP A canonical design freeze;
- Pre-Development Gate PASS where Account/Inventory backbone evidence is a prerequisite;
- Team C controlled handoff;
- Development / Release / Deployment / Production authorization.

Mandatory trigger to release this hold:

`COA-G08 = APPROVED / PASS / CLOSED BY BOSS`

No earlier G03/G04/G05/G06/G07 partial result may be treated as equivalent to Account completion unless Boss issues a separate explicit exception ruling.

## 6. Post-Account Completion Sequence

After `COA-G08 = APPROVED / PASS / CLOSED`, execute in this order:

1. Verify latest Inventory Evidence Gate state and close any still-open Inventory-specific findings.
2. Execute `Accounting x Inventory Cross-Proof` using the frozen Account contract and controlled Inventory contract.
3. Reconcile active `Sales + Purchase` dependent design against both backbones.
4. Re-run applicable independent verification / PMO Gate checks for any dependent design materially affected by the backbone reconciliation.
5. Route final design-freeze / Pre-Development decision to Boss.
6. Team C remains unauthorized until the evidence chain is sealed and Boss explicitly authorizes Development.

## 7. Evidence Preservation Rule

Do not rename, delete or rewrite historical paths merely to make old artifacts match the new active grouping.

Historical path examples such as:

`GROUP_A_SALES_INVENTORY_PURCHASE`

remain valid audit evidence of the lifecycle state at the time they were produced.

New governance / next-stage artifacts should distinguish clearly between:

- historical Group A lineage;
- active Sales + Purchase scope;
- Inventory Backbone scope;
- Account / COA Backbone scope;
- later Cross-Proof scope.

## 8. Progress Reporting

`% Board = TBD / NO APPROVED BASELINE`

`% STATE = TBD / NO APPROVED BASELINE`

`% STEP = TBD / NO APPROVED BASELINE`

No guessed percentages.

## 9. Authority Boundary

This ruling authorizes controlled evidence/review/Gate work for the two parallel tracks only.

`ACCOUNT x INVENTORY CROSS-PROOF = HOLD UNTIL COA-G08 CLOSED`

`TEAM C = NOT AUTHORIZED`

`DEVELOPMENT = NOT AUTHORIZED`

`RELEASE / DEPLOYMENT / PRODUCTION = NOT AUTHORIZED`

Boss is the sole Final Approver.
