# SMEsPlus Reopen Session Package — Account, Inventory, and Account x Inventory

Project: SMEsPlus ENTERPRISE SUITE  
Date: 2026-09-02  
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub  
Branch: SMEsPlus  
Authority: Boss direction  
Status: New Session Prompt Package; not execution result; not Gate PASS

## 1. Boss Direction

Boss directs creation of three new sessions:

1. Reopen all Account work under the updated governance standard.
2. Reopen all Inventory work under the updated governance standard.
3. Create a new joint Account x Inventory session under the updated governance standard.

All three sessions may use prior evidence and old documents as inputs, but old documents are not final authority by themselves. Every material conclusion must be re-proven with evidence.

## 2. Mandatory Governance Standard

All sessions must apply:

- No Evidence = No Progress.
- Never Skip Gate.
- Boss is the sole Final Approver.
- Clean Room First.
- No Gate PASS self-declaration.
- No Team B authorization.
- No Team C authorization.
- No development, merge, release, or production authorization.

## 3. Clean-room Principles

1. Reference Only: Odoo / SAP / Salesforce / legacy systems / dump files are learning and business-semantic references only.
2. No Copy / No Clone / No Reuse: no source code, XML, QWeb, ORM, schema, workflow, naming pattern, or application architecture may be copied into SMEsPlus.
3. Migrate Business Facts + Business Semantics Only: migrate meaning and business facts, not legacy application architecture.
4. SMEsPlus Target Design Must Be Original: design must be original Clean-room Node.js SaaS ERP design with evidence and Boss approval.

## 4. Dual Challenge Mandate

Main duty: 9 Veto Challenge Council.
- Mandatory gate-control challenge body.
- Challenges evidence, source/dump interpretation, functional design, database design, integration/localization, code/UI proof, clean-room compliance, carry-forward logic, and Boss decision recommendation.

Supplementary duty: 9 Special Team Challenge.
- Deep-dive mechanism when Boss raises a specific concern.
- Used to eliminate risk in domain-specific gaps.

Both report directly to Boss only.

## 5. Prompt Files

1. `01_ACCOUNT_FULL_REOPEN_DEEP_RESEARCH_PROMPT.md`
   - Reopen Account work from source/dump/evidence.
   - Includes COA, AR, AP, GL, VAT, WHT, PND, period/month close, year-end close, retained earnings, Thai localization, accounting controls.

2. `02_INVENTORY_FULL_REOPEN_DEEP_RESEARCH_PROMPT.md`
   - Reopen Inventory work from source/dump/evidence.
   - Includes product category valuation policy, stock.move, stock.quant, stock.picking, stock valuation, manual/automated, periodic/perpetual, count/freeze, stock cut-off.

3. `03_ACCOUNT_INVENTORY_JOINT_REOPEN_DEEP_RESEARCH_PROMPT.md`
   - Reopen the joint Account x Inventory interface.
   - Includes monthly close, year-end close, stock valuation to GL reconciliation, opening carry-forward, product category valuation contract, stock movement cut-off, cross-domain event matrix.

## 6. Baseline Hold

Account + Inventory Backbone Reference Baseline remains HOLD until the three new sessions produce evidence and Boss accepts the result.

This package only creates New Session prompts. It does not close any finding.