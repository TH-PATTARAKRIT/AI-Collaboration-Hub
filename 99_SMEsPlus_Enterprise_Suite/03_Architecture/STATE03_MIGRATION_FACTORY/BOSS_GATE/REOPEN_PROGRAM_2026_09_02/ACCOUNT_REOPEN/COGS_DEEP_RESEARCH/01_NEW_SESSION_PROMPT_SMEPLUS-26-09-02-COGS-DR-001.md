# [SMEPLUS-26-09-02-COGS-DR-001]
# COGS + Inventory Valuation Deep Research — Menu-by-Menu / Periodic vs Perpetual / Product Category + Product Accounting / L9999.9999

## SINGLE END-TO-END NEW SESSION PROMPT

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Domain: `ACCOUNTING CORE / COGS / COSTING / INVENTORY VALUATION / ACCOUNTING × INVENTORY INTERFACE`  
Jira: `ERPPLUS-142`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Target Executor: `Claude Sonnet 5 Max`  
Execution Mode: `READ ONLY / DEEP RESEARCH / MENU-BY-MENU / FIELD-BY-FIELD / EVIDENCE-FIRST / CLEAN-ROOM / NO-DESIGN-FREEZE / L9999.9999`  
Boss: `Sole Final Approver`

Pre-Prompt Challenge Commit: `4f8b7d0be000046b1ea62624e5397baea0603125`

Boss-approved Joint controls already in force:
- 22-Scenario Accounting × Inventory Cross-Proof baseline: `296b495144bad0ce20b796ca6ac487dd1604cc40`
- Inventory → Accounting Minimum Handoff Data Contract: `d9e845ede58d5a34c9ab1117482e8883d36e1314`

---

## 1. BOSS DIRECTIVE / WHY THIS SESSION EXISTS

Do **not** proceed to final Accounting × Inventory interface closure until COGS has been deeply understood first.

Inventory Final Solution v1.0 already contains `Inventory Valuation` and emits stock/cost/valuation facts, but the Accounting side must first establish verified understanding of:

- `COGS / Cost of Goods Sold`;
- `Inventory Asset / Inventory Valuation`;
- `Costing Policy`;
- `Periodic vs Perpetual accounting`;
- `Product Category accounting configuration`;
- `Product -> Accounting tab -> Income / Expense behavior`;
- recognition timing;
- return/reversal treatment;
- close/cut-off;
- landed cost / late cost;
- manufacturing cost flow;
- reconciliation between Stock Truth and Financial Truth.

This is a prerequisite research session.

Target condition:

`MATERIAL COGS / COSTING / INVENTORY-VALUATION UNKNOWN EXHAUSTION — READY FOR COGS FINAL SOLUTION CANDIDATE`

Do not manufacture certainty. A controlled `HOLD / EVIDENCE REQUIRED` is preferable to a guessed answer.

---

## 2. ABSOLUTE DOMAIN BOUNDARY

`Inventory Core = Stock Truth Owner.`  
`Accounting Core = Financial Truth Owner.`

Inventory may determine and preserve physical quantity, movement, cost-layer and valuation facts according to an approved policy.
Accounting owns financial recognition, account classification, journal truth, COGS presentation, period close and financial-statement effects.

Research must prove the boundary; do not assume the final implementation.

Candidate relationship to challenge:

`Inventory Cost/Valuation Fact -> Accounting Recognition Rule -> Inventory Asset / COGS / Other Approved Financial Classification`

Not every reduction in Inventory Value is COGS.
Scrap, loss, write-down, adjustment, production consumption, inter-company movement, corrections and other events must be separately proven.

---

## 3. CLEAN-ROOM / REFERENCE-SYSTEM BOUNDARY

The OpenSource reference ERP is a **learning / benchmark source only**.

Allowed in Layer-2 controlled evidence:
- exact observed menu paths;
- exact observed field labels;
- UI behavior;
- documentation behavior;
- configuration defaults/visibility conditions;
- source-code inspection only when necessary to prove behavior;
- version-delta observations.

Forbidden for SMEsPlus target design:
- copied source code;
- copied ORM/schema;
- copied technical implementation architecture;
- copied method/field identifiers as canonical SMEsPlus design;
- assuming reference behavior is correct for Thailand;
- assuming reference behavior is the required SMEsPlus solution.

Required transformation:

`Observed Reference Behavior -> Neutral Business Meaning -> Accounting Principle / Control Question -> Thai Evidence Check -> SMEsPlus Candidate / HOLD`

Maintain three separate evidence layers:

1. `Layer A — OpenSource Reference ERP Observed Behavior`
2. `Layer B — Thai Accounting / Tax / Statutory / Audit Evidence`
3. `Layer C — SMEsPlus Clean-Room Candidate Semantics`

Never merge the three layers into one unsupported conclusion.

---

## 4. MANDATORY PRIOR EVIDENCE LOAD

Before new conclusions, reconstruct and read the latest controlled evidence at minimum:

### 4.1 Accounting / Governance
- Account Full Reopen Prompt and latest Account evidence.
- COA-G01 / G02 / G03 and later COA evidence available at execution time.
- `PROJECT_CONSTITUTION.md` and current governance addenda.
- 9 Veto / 9 Special Team Charter.
- Challenge Continuity Ledger.
- `Understand deeply -> Transfer accurately -> Preserve verifiably` lifecycle standard.

### 4.2 Inventory Final Solution v1.0
From branch `design/inventory-final-solution-v1-2026-09-02-001`, read at minimum:
- `07_INVENTORY_ACCOUNTING_CONTROL_IMPACT_V1.md`
- `08_INVENTORY_VALUATION_LANDED_ANALYTIC_COST_V1.md`
- `10_INVENTORY_CROSS_MODULE_HANDOFF_V1.md`
- `12_INVENTORY_RISK_GAP_DECISION_REGISTER_V1.md`
- `13_AI_AUDIT_SMEPLUS_FINAL_SOLUTION_CHALLENGE_V1.md`
- `14_BOSS_FINAL_GATE_PACKAGE.md`
- `17_SESSION_CLOSURE_SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V1-001.md`

Explicitly reconcile open Joint decisions including `JT-01 / JT-02 / JT-03 / JT-04 / JT-05 / JT-06 / JT-08 / JT-09`.

### 4.3 Joint Controls
Read:
- Boss-approved 22-Scenario Accounting × Inventory Cross-Proof baseline.
- Boss-approved 16-field Inventory → Accounting Minimum Handoff Data Contract.

Do not execute the final Joint Cross-Proof in this session. Prepare verified COGS inputs for it.

---

## 5. MANDATORY EXTERNAL RESEARCH BASELINE

Independently verify current and relevant historical OpenSource reference ERP documentation/source behavior. Do not rely only on this Prompt.

Research must include version-aware evidence for:

- Inventory Valuation configuration;
- Periodic valuation / stock closing;
- Perpetual valuation / recognition timing;
- Product Category accounting configuration;
- Product-level accounting overrides;
- Costing Method;
- Inventory / Stock / Valuation Account;
- Variation / Stock Variation Account;
- Income Account;
- Expense / COGS / Cost-of-Revenue Account behavior;
- Price Difference behavior where applicable;
- Inventory Loss / Production cost controls where applicable;
- Inventory valuation reporting;
- Balance Sheet and Profit & Loss effects.

### Version-delta rule

Reference behavior has materially changed across versions.
Therefore create an explicit:

`REFERENCE_VERSION_BEHAVIOR_DELTA_REGISTER`

At minimum compare the relevant current reference version with the immediately prior architecture used by historical SMEsPlus learning.
Do not silently carry an old Automatic/Manual valuation interpretation into a newer Periodic/Perpetual model, or vice versa.

---

## 6. MENU-BY-MENU / FIELD-BY-FIELD STUDY

Study the following reference UI surfaces one by one. If a menu/field is absent in a version, record `NOT PRESENT IN THIS VERSION` with evidence.

### MENU A — Accounting -> Configuration -> Settings -> Inventory Valuation

For every visible/conditional field record:
- purpose;
- values/options;
- default;
- visibility condition;
- company scope;
- relationship to Periodic/Perpetual;
- relationship to costing method;
- stock/valuation/variation account behavior;
- journal/closing behavior;
- transaction triggers;
- financial statement impact;
- version delta;
- evidence source.

Prove the observed meaning of:
- Inventory Valuation method;
- Periodic Valuation / closing cadence;
- Inventory Cost Method;
- Valuation/Stock Account;
- Variation Account;
- valuation journal;
- other inventory loss / production accounts where supported.

### MENU B — Inventory -> Configuration -> Product Categories

Study the full category form, especially Accounting / Inventory Valuation sections.

Mandatory field research:
- Costing Method;
- Inventory Valuation;
- Income Account;
- Expense Account;
- Stock / Valuation Account;
- Variation / interim accounts where observed;
- Price Difference Account where observed;
- category/company ownership;
- inheritance to product;
- effect of changing category or policy;
- historical effect / effective dating;
- impact on existing stock;
- behavior by Periodic vs Perpetual.

Do not stop at field definitions. Prove when each field is actually consumed by a business transaction.

### MENU C — Product -> Products -> Product -> Accounting Tab

Study exact observed fields and behavior, especially:
- Income Account;
- Expense Account;
- Sales Taxes;
- Purchase Taxes;
- Cost / Standard Cost where relevant;
- Invoicing Policy or other accounting-impacting product settings where present;
- company context;
- product-category inheritance;
- product override;
- blank/default behavior;
- precedence when product and category differ;
- effect on historical vs future transactions.

Mandatory question:

`When does the Product-level Income/Expense account override the Product Category default, and which business event uses the resolved account under Periodic and under Perpetual accounting?`

### MENU D — Accounting -> Configuration -> Chart of Accounts

Study account types used in the COGS / inventory lifecycle:
- Current Asset / Inventory Asset;
- Expense;
- Cost of Revenue / Cost of Goods Sold;
- Other Expense / Loss where applicable;
- WIP / Production asset or expense concepts where applicable;
- variation/interim concepts observed in the reference.

Do not infer Thai COA classification from the reference. Map observed behavior separately from Thai authoritative requirements.

### MENU E — Inventory -> Reporting -> Inventory Valuation

Prove:
- quantity/value relationship;
- cost method effect;
- opening / inbound / outbound / adjustment / landed / manufacturing / closing values;
- as-of-date behavior;
- drill-down/provenance;
- reconciliation to Accounting;
- difference reporting;
- negative/zero-cost exceptions;
- version delta.

### MENU F — Accounting -> Inventory Valuation / Stock Closing / Closing Entry Flow

Where present, study:
- close initiation;
- closing date;
- entry generation;
- periodic cadence;
- valuation vs variation treatment;
- prior-period handling;
- late cost handling;
- reversal/reopening behavior;
- audit trail;
- permissions/approval;
- effect on Balance Sheet / P&L.

### MENU G — Vendor Bill / Customer Invoice Accounting Behavior

Trace how Product Category/Product accounting resolution is consumed when:
- Vendor Bill is posted;
- Customer Invoice is posted;
- bill/invoice exists before or after receipt/delivery;
- partial quantities exist;
- returns occur;
- price differs from cost;
- period is closed.

### MENU H — Inventory Loss / Production / Location Accounting Controls

Where supported by the reference version, study:
- inventory loss/shrinkage account;
- production/WIP cost account;
- location-specific accounting controls;
- distinction between COGS and non-COGS inventory reductions.

Every Menu A-H must produce a Menu Evidence Sheet.

---

## 7. MANDATORY FIELD EVIDENCE SHEET FORMAT

For each material field create a row with:

| Field | Requirement |
|---|---|
| Menu Path | Exact observed path/version |
| Field Label | Exact UI label in Layer A evidence |
| Purpose | Observed business purpose |
| Values / Options | Exact observed values where available |
| Default | Observed default / UNKNOWN |
| Visibility | Always / conditional + condition |
| Scope | Company / category / product / location / global |
| Inherits From | Source of default |
| Override Precedence | Which value wins and when |
| Transaction Consumer | Receipt / bill / delivery / invoice / close / adjustment / etc. |
| Periodic Behavior | Evidence-backed behavior |
| Perpetual Behavior | Evidence-backed behavior |
| Account Type Impact | Asset / COGS / expense / variation / etc. |
| Financial Statement Impact | BS / P&L / both / none |
| Change Impact | Existing stock/history/future only |
| Version Delta | What changed across reference versions |
| Evidence | URL / screenshot / source line / commit |
| Fact Status | VERIFIED / PROVISIONAL / HOLD / CONFLICTING |

No blank material cells. Use `UNKNOWN / HOLD` where evidence is missing.

---

## 8. PERIODIC VS PERPETUAL — DEEP ACCOUNTING RESEARCH

Build two full accounting lifecycles separately before comparison.

### 8.1 PERIODIC

Prove the observed lifecycle for:

`Opening Inventory -> Purchases / Vendor Bills -> Physical Receipts -> Sales -> Deliveries -> Customer Invoices -> Physical Closing Stock -> Stock Closing Entry -> COGS / Stock Variation -> Financial Statements`

Research questions:
- When is purchase cost first expensed or capitalized?
- Is Inventory Asset updated transaction-by-transaction or at close?
- How is closing inventory value determined?
- How is stock variation calculated?
- How is COGS derived/presented?
- What happens if a receipt exists with no bill?
- What happens if a bill exists with no receipt?
- How are returns handled before/after closing?
- How are write-down, loss, scrap and adjustment distinguished?
- How does the close reconcile physical Stock Truth to Financial Truth?

### 8.2 PERPETUAL

Prove the observed lifecycle for:

`Opening Inventory -> Purchase / Receipt / Vendor Bill -> Inventory Asset -> Sale / Delivery / Customer Invoice -> COGS Recognition -> Returns/Reversals -> Period Close/Reconciliation`

Research questions:
- Which event updates Inventory Asset?
- Which event recognizes COGS?
- Is COGS triggered by delivery, invoice, or another event in each reference version/accounting standard mode?
- What interim/variation control exists when physical and financial timing differ?
- What happens to partial receipt/delivery?
- What happens when the vendor bill price differs from valuation cost?
- What happens when landed cost arrives after some stock has been sold?
- How are returns reversed to the original cost basis?
- What does period close still do under Perpetual?

### 8.3 Mandatory Comparison Matrix

Compare at minimum:
- accounting event trigger;
- Inventory Asset timing;
- COGS timing;
- purchase expense timing;
- stock variation;
- close workload;
- reconciliation burden;
- late cost;
- returns;
- negative stock;
- audit traceability;
- migration complexity;
- Thai SME operational fit;
- SaaS/multi-company control.

No recommendation until evidence layers are complete.

---

## 9. COSTING METHOD DEEP RESEARCH

Research each cost method separately where supported/evidenced:

- Standard Cost;
- Average / Weighted Average;
- FIFO;
- Specific Identification as an accounting/business requirement where authoritative evidence makes it relevant, even if the reference UI does not implement it as a selectable method.

For each method prove:
- receipt cost formation;
- issue cost release;
- cost layer or average identity;
- price difference;
- negative stock effect;
- return cost basis;
- landed cost effect;
- late supplier bill effect;
- cost method change;
- existing-stock conversion;
- close/reconciliation;
- migration/opening balance requirements;
- COGS consequence under Periodic and Perpetual.

Do not treat warehouse removal strategy as accounting cost method without evidence.

---

## 10. MINIMUM COGS CONTROLLED SCENARIOS

Execute research/evidence mapping for at least these 32 scenarios:

1. Opening inventory with known quantity/value.
2. Purchase receipt before vendor bill.
3. Vendor bill before receipt.
4. Receipt and bill same period.
5. Receipt in period N, bill in N+1.
6. Vendor bill price differs from receipt/valuation basis.
7. Purchase return before bill.
8. Purchase return after bill.
9. Landed cost before any sale.
10. Landed cost after partial sale.
11. Landed cost after full sale.
12. Customer delivery before invoice.
13. Customer invoice before delivery.
14. Delivery and invoice same period.
15. Partial delivery.
16. Backorder.
17. Customer return in same period.
18. Customer return in later period.
19. Cancellation before physical movement.
20. Correction/reversal after physical movement.
21. Inventory adjustment gain.
22. Inventory adjustment loss.
23. Scrap / damage / shrinkage.
24. NRV/write-down or impairment treatment where authoritative evidence applies.
25. Internal warehouse transfer same company.
26. Inter-company inventory transfer.
27. Manufacturing raw-material consumption.
28. Manufacturing WIP -> finished goods.
29. Manufacturing finished goods -> COGS.
30. Period-end closing / cut-off with unbilled receipts and uninvoiced deliveries.
31. Migration/opening inventory replay.
32. Retry/idempotency/replay with no duplicated COGS or Inventory Value.

Add scenarios if a material Delta Trigger emerges.

For every scenario run **both Periodic and Perpetual** where logically applicable.

---

## 11. PRODUCT CATEGORY vs PRODUCT OVERRIDE PROOF

This is a mandatory deep-dive, not a sub-note.

Build a precedence matrix for at least:

1. Category has Income Account; Product blank.
2. Category has Expense Account; Product blank.
3. Category and Product have same Income Account.
4. Category and Product have different Income Accounts.
5. Category and Product have same Expense Account.
6. Category and Product have different Expense Accounts.
7. Product changes category before any transaction.
8. Product changes category with existing stock.
9. Product accounting override changes mid-period.
10. Company A and Company B use different policies/accounts.
11. Category valuation method differs from company default where reference version permits override.
12. Category costing method differs from company default where reference version permits override.

For each case prove:
- resolved configuration;
- transaction(s) affected;
- Periodic outcome;
- Perpetual outcome;
- historical effect;
- future effect;
- required approval/audit trail;
- migration implication.

---

## 12. COGS RECOGNITION / ACCOUNT FLOW PROOF

Do not produce a single static journal-entry example and stop.

Derive evidence-backed accounting flow archetypes for:
- purchase cost acquisition;
- inventory capitalization;
- sale / COGS recognition;
- purchase return;
- sales return;
- price difference;
- stock variation;
- adjustment gain/loss;
- scrap/loss;
- landed cost;
- manufacturing consumption/WIP/output;
- closing entry;
- migration opening.

Every archetype must label:
- `REFERENCE OBSERVATION`;
- `ACCOUNTING MEANING`;
- `THAI RULE STATUS`;
- `SMEPLUS CANDIDATE / HOLD`.

Do not prescribe final SMEsPlus account codes or journal structure in this research session.

---

## 13. THAI ACCOUNTING / TAX / AUDIT TRACK

Use authoritative Thai evidence only for Thai requirements.

At minimum investigate:
- inventory cost composition;
- acceptable cost-flow assumptions/methods;
- lower-of-cost/NRV or applicable inventory measurement requirements;
- recognition of carrying amount as expense/COGS when related revenue is recognized;
- inventory write-down and reversal;
- abnormal loss / scrap / destroyed inventory treatment;
- landed cost / duty / recoverable VAT distinction;
- period cut-off and physical stock evidence;
- tax inventory valuation requirements;
- consistency/change of costing method;
- financial-statement presentation of Inventory / COGS / gross profit.

For each Thai point classify:
- `AUTHORITATIVE / VERIFIED`;
- `INTERPRETATION — REVIEW REQUIRED`;
- `NOT FOUND / HOLD`.

Do not treat blog/accounting-firm commentary as statutory authority unless clearly labeled secondary evidence.

---

## 14. RECONCILIATION IDENTITIES TO CHALLENGE

Derive and test; do not blindly assume:

### Physical Stock
`Opening Qty + Valid Inflows - Valid Outflows +/- Controlled Adjustments = Closing Qty`

### Inventory Value
`Opening Inventory Value + Capitalizable Cost Added - Cost Released +/- Approved Valuation Adjustments = Closing Inventory Value`

### Cost Release
`Inventory Cost Released -> COGS OR another explicitly approved financial classification`

### Periodic COGS Candidate
Investigate whether and under what evidence:
`Opening Inventory + Net Purchases / Capitalizable Costs - Closing Inventory = COGS`, adjusted for the actual applicable accounting model.

### Cross-System Reconciliation
`Inventory valuation as-of-date <-> Accounting inventory balance + fully explained reconciling items`

Every identity must be classified `VERIFIED / CANDIDATE / HOLD` with evidence and scope conditions.

---

## 15. 9 VETO COUNCIL — MANDATORY EXECUTION

Run all nine independently before convergence:

1. Audit VETO — evidence chain, no skipped Gate, version traceability.
2. TBRAC — Thai SME usability and real closing/accountant workflow.
3. IBPV — end-to-end cost/COGS process integrity.
4. IDTM — identity, cost layer, original/reversal, reconciliation and migration integrity.
5. IESA — SaaS, company/tenant, policy inheritance and interface integrity.
6. Financial/Accounting/Tax VETO — primary authority for COGS, valuation, close and financial statement risk.
7. Security/Privacy/Resilience VETO — configuration authority, period lock, override, audit trail, recovery.
8. Clean-Room/IP/Provenance VETO — source quarantine and neutral business semantics.
9. AI Control/Human Oversight VETO — no invented entries/costs; deterministic proof.

Each returns:
- `CONTINUE_WITH_NOTES`
- `HOLD`
- `FAIL / FROZEN`

Most conservative unresolved material verdict controls.

---

## 16. 9 SPECIAL TEAM DEEP INVESTIGATION — ALL ACTIVATED

Produce separate outputs for:

- S1 COGS / Financial Accounting
- S2 Inventory Costing
- S3 Product Category & Product Accounting Configuration
- S4 Periodic Accounting
- S5 Perpetual Accounting
- S6 Returns / Adjustment / Scrap / Landed Cost
- S7 Manufacturing Cost
- S8 Thai Accounting / Tax / Audit Reality
- S9 Migration / Replay / AI Control

Each Special Team must report:
- current understanding;
- evidence;
- hypothesis;
- unknowns;
- contradictions;
- what was tried;
- findings;
- what Owning Team must absorb;
- reusable reasoning pattern;
- future trigger to detect the same problem.

Special Team does not become the owner of Accounting knowledge.

---

## 17. UNDERSTAND -> TRANSFER -> PRESERVE GATE

Before session closure, Accounting Owning Team must pass Teach-Back.

Required Teach-Back questions:

1. Explain Periodic accounting from purchase through closing and COGS.
2. Explain Perpetual accounting from purchase through COGS and closing reconciliation.
3. Explain Product Category vs Product Income/Expense inheritance and overrides.
4. Explain why Inventory Value decrease is not always COGS.
5. Explain COGS recognition timing and timing differences with physical stock.
6. Explain returns and original cost linkage.
7. Explain late supplier bill / landed cost after stock sale.
8. Explain Standard / Average / FIFO differences and migration implications.
9. Explain Balance Sheet Inventory vs P&L COGS reconciliation.
10. State exactly what remains UNKNOWN / HOLD and what the Joint Team must not assume.

If the Owning Team cannot teach these back from evidence:

`TRANSFER NOT COMPLETE — GATE HOLD`

---

## 18. MANDATORY DELIVERABLES

Publish under a dedicated controlled execution path. Minimum deliverables:

1. `00_EXECUTION_CHECKPOINT_LOG.md`
2. `01_PRIOR_EVIDENCE_AND_QUESTION_FINGERPRINT_INDEX.md`
3. `02_REFERENCE_VERSION_BEHAVIOR_DELTA_REGISTER.md`
4. `03_MENU_A_ACCOUNTING_SETTINGS_INVENTORY_VALUATION_EVIDENCE.md`
5. `04_MENU_B_PRODUCT_CATEGORY_ACCOUNTING_FIELD_REGISTER.md`
6. `05_MENU_C_PRODUCT_ACCOUNTING_INCOME_EXPENSE_FIELD_REGISTER.md`
7. `06_MENU_D_COA_COGS_INVENTORY_ACCOUNT_TYPE_REGISTER.md`
8. `07_MENU_E_INVENTORY_VALUATION_REPORT_DEEP_RESEARCH.md`
9. `08_MENU_F_STOCK_CLOSING_PERIOD_CLOSE_DEEP_RESEARCH.md`
10. `09_MENU_G_VENDOR_BILL_CUSTOMER_INVOICE_COST_FLOW.md`
11. `10_MENU_H_INVENTORY_LOSS_PRODUCTION_ACCOUNT_CONTROLS.md`
12. `11_PRODUCT_CATEGORY_PRODUCT_INHERITANCE_OVERRIDE_PRECEDENCE_MATRIX.md`
13. `12_PERIODIC_ACCOUNTING_END_TO_END_MODEL.md`
14. `13_PERPETUAL_ACCOUNTING_END_TO_END_MODEL.md`
15. `14_PERIODIC_VS_PERPETUAL_COMPARISON_MATRIX.md`
16. `15_COSTING_METHOD_DEEP_RESEARCH_MATRIX.md`
17. `16_COGS_32_SCENARIO_EVIDENCE_REGISTER.md`
18. `17_PURCHASE_RECEIPT_VENDOR_BILL_COST_FLOW.md`
19. `18_SALES_DELIVERY_INVOICE_COGS_RECOGNITION_FLOW.md`
20. `19_RETURN_REVERSAL_ORIGINAL_COST_LINKAGE.md`
21. `20_ADJUSTMENT_SCRAP_LOSS_WRITEDOWN_CLASSIFICATION.md`
22. `21_LANDED_COST_LATE_COST_PRICE_DIFFERENCE_RESEARCH.md`
23. `22_MANUFACTURING_RM_WIP_FG_COGS_RESEARCH.md`
24. `23_PERIOD_CLOSE_CUTOFF_RECONCILIATION_MODEL.md`
25. `24_THAI_ACCOUNTING_TAX_STATUTORY_EVIDENCE_REGISTER.md`
26. `25_MULTI_COMPANY_TENANT_POLICY_ISOLATION_REGISTER.md`
27. `26_MIGRATION_OPENING_COST_REPLAY_IDEMPOTENCY_REGISTER.md`
28. `27_COGS_INVENTORY_RECONCILIATION_IDENTITY_REGISTER.md`
29. `28_9_VETO_COUNCIL_FINDINGS.md`
30. `29_9_SPECIAL_TEAM_FINDINGS_AND_LEARNING_ABSORPTION.md`
31. `30_COGS_MATERIAL_UNKNOWN_CONFLICT_REGISTER.md`
32. `31_COGS_TO_INVENTORY_HANDOFF_CONTRACT_CANDIDATE.md`
33. `32_ACCOUNTING_OWNER_TEACH_BACK_AND_UNDERSTANDING_GATE.md`
34. `33_COGS_DEEP_RESEARCH_FINAL_REPORT.md`
35. `34_NEXT_CONTROLLED_ACTION_AND_OWNER_MATRIX.md`
36. `35_SHA256_MANIFEST.txt`
37. `36_SESSION_CLOSURE_SMEPLUS-26-09-02-COGS-DR-001.md`

Missing evidence = HOLD, not synthesis.

---

## 19. COGS -> INVENTORY JOINT HANDOFF PREPARATION

The research must end with an Accounting-side candidate contract sufficient for later Joint Cross-Proof, including at minimum:

### Contract A — INVENTORY COST CONTRACT
What costs may enter Inventory Value, when, under which policy/version, and with which evidence.

### Contract B — COGS RECOGNITION CONTRACT
When/how Inventory Value is released into COGS or another approved classification, including revenue/physical/invoice timing differences.

### Contract C — COST REVERSAL / ADJUSTMENT CONTRACT
How returns, cancellations, correction, late cost, landed cost, write-down, scrap, manufacturing variance and period-close adjustments preserve original-event linkage and avoid duplicate financial effects.

These are candidate contracts only until independently reviewed and reconciled with Inventory.

---

## 20. CHECKPOINT CONTROL

Minimum checkpoints:

- `CP-00` Branch/worktree isolation and evidence-source access.
- `CP-01` Prior evidence reconstruction complete.
- `CP-02` Reference version delta established.
- `CP-03` Menu A-H coverage complete.
- `CP-04` Product Category/Product inheritance proof complete.
- `CP-05` Periodic model complete.
- `CP-06` Perpetual model complete.
- `CP-07` Costing method model complete.
- `CP-08` 32-scenario evidence register complete.
- `CP-09` Thai evidence track complete or explicitly HOLD.
- `CP-10` 9 Veto + 9 Special Team challenge complete.
- `CP-11` Teach-Back / Owner Understanding Gate complete.
- `CP-12` COGS-to-Inventory candidate contracts complete.
- `CP-13` Evidence manifest verified.
- `CP-14` Session closure published.

If a checkpoint hits a material contradiction that invalidates downstream conclusions, stop and classify HOLD/FAIL appropriately.

---

## 21. TERMINAL STATUS

Use only one:

- `COGS DEEP RESEARCH COMPLETE — READY FOR INDEPENDENT COGS RESEARCH AUDIT AND COGS FINAL SOLUTION CANDIDATE`
- `HOLD / EVIDENCE REQUIRED — COGS MATERIAL UNKNOWN NOT EXHAUSTED`
- `FAIL / FROZEN — MATERIAL ACCOUNTING / GOVERNANCE / CLEAN-ROOM FAILURE`

This session must NOT self-declare:
- COGS Final Solution PASS;
- Account Final Solution PASS;
- Inventory Final Solution PASS;
- Accounting × Inventory Cross-Proof PASS;
- Final Freeze;
- Team C / Team D authorization;
- Development / Release / Production readiness.

---

## 22. HARD RULES

`COGS Deep Research precedes Accounting × Inventory Final Cross-Proof.`  
`Inventory owns Stock Truth. Accounting owns Financial Truth.`  
`Inventory emits evidence-backed valuation facts; Accounting owns financial recognition.`  
`Not every inventory-value decrease is COGS.`  
`Reference behavior is evidence, not target architecture.`  
`Version drift must be proven, not assumed away.`  
`No hidden account inheritance or override.`  
`No hidden timing assumption.`  
`No fabricated journal entry.`  
`No fabricated cost.`  
`No Evidence = No Progress.`  
`No Evidence Preservation = No Lifecycle Promotion.`  
`Understand deeply -> Transfer accurately -> Preserve verifiably.`  
`Do not hand off documents. Hand off verified understanding.`  
`Never Skip Gate.`  
`Boss = Sole Final Approver.`
