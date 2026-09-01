# [SMEPLUS-26-09-02-INV-REOPEN-001]
# Inventory Core Full Reopen — 9 Veto Council + 9 Special Team Deep Revalidation / L999.999

## SINGLE END-TO-END NEW SESSION PROMPT

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Jira: `ERPPLUS-139`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Boss: `Sole Final Approver`  
Mode: `READ ONLY / EVIDENCE-FIRST / DELTA-FIRST / CLEAN-ROOM / MATERIAL-UNKNOWN-EXHAUSTION`  
Control Level: `/L999.999`

Mandatory governance inputs:

- Full Reopen Program: `42e04e639f2c83aeef6d7c313152a55170a4c6ef`
- Inventory 9-Veto Challenge / Readiness: `3cfb26faf04dddda6aea5f59e201ee1f008b94dd`
- NEW PROMPT Governance v2.0: `03b4244b2101e8c0a89d36255cc654fc2537c748`
- 9 Veto / 9 Special Team Charter: `5d81d628b9b159f89a93da7ab920c42ef8f09555`
- Global Challenge Ledger: `f8d940900896a5a11e7232bac0e829fc5a60e908`

This Prompt reopens the complete Inventory knowledge/evidence chain for revalidation while preserving all historical work.

`FULL REOPEN != RESET TO ZERO.`

`No repeated question without a material delta.`

---

## 1. Mission

Determine whether SMEsPlus Inventory / Stock Truth has been learned deeply enough that no hidden material doubt remains about the stock domain, its exceptions, its SaaS/migration controls, and its interface to Accounting.

The work must answer:

1. What prior Inventory findings are still valid and should be carried forward?
2. Which findings require revalidation because of the new backbone/governance/joint-session deltas?
3. Which conclusions must be reopened because of contradictory evidence?
4. What material Unknowns remain in Stock Truth?
5. Are stockable / consumable / service routing assumptions evidence-supported and correctly bounded?
6. Are Inventory quantities, movements, reservations, traceability and exceptions semantically complete?
7. Does Inventory emit sufficient facts for Accounting without owning Accounting truth?
8. Is Inventory evidence strong enough for future migration and deterministic reconciliation?
9. What does each of the 9 Veto mandates require before Inventory may be treated as materially understood?

Target condition:

`MATERIAL UNKNOWN EXHAUSTION FOR INVENTORY KNOWLEDGE — NOT ARTIFICIAL CERTAINTY.`

---

## 2. Mandatory Prior Evidence Load

Before asking new questions, enumerate and inspect at minimum:

- historical `GROUP_A_SALES_INVENTORY_PURCHASE` Inventory evidence;
- DR-002 Account-grade Inventory Deep Research;
- DR-002 execution artifacts;
- all corrective/supersession records through CORR-005;
- independent-review lineage;
- IDR-007 readiness `54025627d63eb4055ff89f602454d9122876dfb2`;
- IDR-007 prompt `d5261b7a61cc317bccbaaf466c26417da6ba3486`;
- any IDR-007 result that may exist after the pre-reopen baseline — if found, preserve and reconcile it;
- Boss `bh_* / bhpro_*` Inventory source-scope exclusions and other source-control rulings;
- Accounting / Inventory backbone roadmap and current Account state;
- New Prompt Governance v2.0 and challenge ledgers;
- Migration Factory controls and Thailand Business Reality controls.

Do not assume the latest status from memory. Reconstruct the current Inventory evidence chain from immutable commits and canonical artifacts.

---

## 3. Historical Question Control

Build an Inventory Question Fingerprint Index before asking questions.

Classify each prior question:

- `CLOSED_WITH_EVIDENCE — DO NOT REASK`
- `CARRY_FORWARD — NO MATERIAL DELTA`
- `REOPEN_ELIGIBLE — DELTA TRIGGER EXISTS`
- `CONFLICTING — REOPEN REQUIRED`
- `UNKNOWN — STILL MATERIAL`
- `SUPERSEDED — HISTORICAL ONLY`

For every reopened question record the exact Delta Trigger.

---

## 4. 9 Veto Council — Mandatory Deep Challenge Tracks

Execute all nine mandate tracks separately before convergence.

### Track 01 — Audit VETO / Evidence & Governance

Deeply verify:

- DR-002 -> corrective -> independent-review -> current-state chain;
- superseded/unexecuted Prompt handling;
- branch/commit/evidence preservation;
- exact current status of IDR-007 or successors;
- stale closure claims;
- owner/timestamp/verifier/evidence completeness;
- whether Material Unknown Exhaustion was ever actually proven.

### Track 02 — TBRAC / Thailand Business Reality & User Fitness

Deeply test Inventory against real Thai operating practice where evidenced/applicable:

- warehouse/storekeeper roles;
- purchasing/receiving/sales delivery interactions;
- stock count / cycle count / adjustment;
- returns, damaged goods, scrap, shortages, overages;
- lot/serial/expiry where relevant;
- branch/warehouse operational differences;
- documents and approval reality;
- SME simplicity vs enterprise control;
- real-user validation gaps;
- industry-dependent requirements.

Do not generalize from one source implementation.

### Track 03 — IBPV / Business Process & Design Integrity

Deeply test end-to-end physical-stock semantics:

- demand/planned quantity;
- reservation/allocation;
- receipt;
- delivery;
- internal transfer;
- partial receipt/delivery;
- backorder;
- cancellation before/after execution;
- returns/reversal;
- scrap;
- physical count/adjustment;
- replenishment;
- MTO/MTS/route behavior where evidenced;
- manufacturing consumption/WIP/finished-goods handoff;
- Sales/Purchase/MFG ownership boundaries;
- no duplicate ownership of stock truth.

### Track 04 — IDTM / Data, Identity, Reconciliation & Integrity

Deeply test:

- on-hand, reserved, available/free and moved quantities;
- UOM conversions and rounding;
- lot/serial/package traceability identities;
- duplicate/retry/idempotency;
- negative-stock or exceptional states where evidenced;
- source-to-canonical inventory provenance;
- historical opening/closing stock continuity;
- inventory quantity/value reconciliation requirements;
- orphan and migration-invalid states;
- replayability of migration/import.

### Track 05 — IESA / ERP & SaaS System Integrity

Deeply test:

- warehouse/location hierarchy;
- company/tenant ownership;
- multi-warehouse / multi-company flows;
- cross-company transfers if applicable;
- route/replenishment architecture semantics;
- performance/resilience implications at SaaS scale;
- stock-event and integration boundaries;
- Inventory independence from source ERP architecture;
- interaction with Accounting, Sales, Purchase and Manufacturing.

### Track 06 — Financial / Accounting / Tax / Statutory VETO

Deeply test the Inventory-to-Accounting boundary without taking Accounting ownership:

- receipt valuation handoff;
- delivery/COGS handoff;
- return/reversal handoff;
- adjustment financial handoff;
- manufacturing valuation handoff;
- landed/additional cost concepts where evidenced;
- cost timing / cut-off;
- stockable vs consumable vs service financial-routing effect;
- what Inventory must know/emit vs what Accounting must decide;
- unresolved COA/valuation dependencies.

Every Accounting-dependent conclusion must be classified `STABLE / PROVISIONAL / HOLD` with evidence.

### Track 07 — Security / Privacy / Resilience VETO

Deeply test:

- permission to receive/deliver/transfer/adjust/scrap/count;
- destructive or fraud-prone stock actions;
- tenant/company/warehouse isolation;
- privileged override;
- audit trail;
- concurrent actions and recovery;
- backup/recovery implications for stock truth;
- interface authentication/authorization where architecture evidence exists.

### Track 08 — Clean-Room / IP / Provenance VETO

Deeply test:

- source stock models/routes/workflows mistakenly becoming target architecture;
- source field/model identities leaking into canonical semantics;
- vendor-specific features treated as universal business truth;
- licensed/quarantined source handling;
- raw source/customer data preservation rules;
- neutralization of evidence before downstream target design.

### Track 09 — AI Control / Automation / Human Oversight VETO

Deeply test AI use for:

- source Inventory classification;
- product type mapping;
- warehouse/location mapping;
- lot/serial traceability mapping;
- exception classification;
- duplicate/anomaly detection;
- migration transformation;
- reconciliation explanation.

Define which controls must remain deterministic:

- quantity conservation where applicable;
- source/target record counts;
- referential integrity;
- tenant/company isolation;
- UOM conversions according to controlled rules;
- idempotency/replay protection;
- source/target checksums;
- reconciliation identities.

Mandatory:

`AI must not fabricate stock movements, quantities, valuation facts or historical events to make migration/reconciliation pass.`

---

## 5. Product / Service Routing Deep Proof

Treat the Boss routing model as a target hypothesis to be validated, not a source fact:

- `Stockable / Inventory-managed -> Inventory Stock Truth applies`.
- `Consumable -> no stock ledger by default; Accounting effect may apply`.
- `Service -> no stock ledger; Accounting effect may apply`.

Research:

- source evidence;
- Thai real-business evidence;
- edge cases;
- whether target terminology needs precision;
- whether any company/industry requires additional classification;
- migration consequences;
- Accounting handoff consequences.

Do not silently force a source system's product-type taxonomy onto SMEsPlus.

---

## 6. Mandatory Inventory Coverage Register

Cover at minimum:

1. Product/inventory-management classification.
2. Product variants if relevant.
3. UOM and conversion.
4. Warehouse.
5. Location.
6. Company/tenant ownership.
7. Demand/planned quantity.
8. Reservation/allocation.
9. On-hand.
10. Available/free.
11. Executed movement.
12. Receipt.
13. Delivery.
14. Internal transfer.
15. Partial/backorder.
16. Return/reversal.
17. Cancellation.
18. Scrap/damage.
19. Physical count/adjustment.
20. Lot.
21. Serial.
22. Package/handling unit.
23. Expiry where evidenced.
24. Routes/replenishment.
25. MTO/MTS where evidenced.
26. Procurement handoff.
27. Sales handoff.
28. Purchase handoff.
29. Manufacturing handoff.
30. Accounting valuation interface.
31. Period/cut-off.
32. Multi-warehouse.
33. Multi-company.
34. SaaS/tenant isolation.
35. Migration/provenance.
36. Historical stock continuity.
37. Idempotency/retry/concurrency.
38. Security/SoD/audit trail.
39. Thailand user/business reality.
40. AI control boundary.

For each: `Prior Status / Prior Evidence / Delta / Current Evidence / Unknown / Special Team / Accounting Dependency / Gate Impact`.

---

## 7. Accounting Dependency Discipline

Inventory may deeply research financial interface evidence, but must not invent final Accounting rules.

Use classifications:

- `INVENTORY-OWNED STOCK FACT`
- `ACCOUNTING INTERFACE FACT`
- `ACCOUNTING CONTRACT STABLE`
- `ACCOUNTING CONTRACT PROVISIONAL`
- `ACCOUNTING CONTRACT HOLD`
- `OUT OF INVENTORY AUTHORITY`

This keeps Inventory moving without contaminating Accounting.

---

## 8. Mandatory Deliverables

Publish under a dedicated controlled reopen execution path:

1. `01_INVENTORY_PRIOR_EVIDENCE_AND_QUESTION_FINGERPRINT_INDEX.md`
2. `02_INVENTORY_FULL_COVERAGE_STATUS_REGISTER.md`
3. `03_AUDIT_VETO_DEEP_FINDINGS.md`
4. `04_TBRAC_DEEP_FINDINGS.md`
5. `05_IBPV_DEEP_FINDINGS.md`
6. `06_IDTM_DEEP_FINDINGS.md`
7. `07_IESA_DEEP_FINDINGS.md`
8. `08_FINANCIAL_ACCOUNTING_INTERFACE_VETO_FINDINGS.md`
9. `09_SECURITY_PRIVACY_RESILIENCE_VETO_FINDINGS.md`
10. `10_CLEANROOM_IP_PROVENANCE_VETO_FINDINGS.md`
11. `11_AI_CONTROL_AUTOMATION_VETO_FINDINGS.md`
12. `12_STOCKABLE_CONSUMABLE_SERVICE_DEEP_PROOF.md`
13. `13_INVENTORY_MATERIAL_UNKNOWN_CONFLICT_REGISTER.md`
14. `14_INVENTORY_ACCOUNTING_DEPENDENCY_REGISTER.md`
15. `15_INVENTORY_GATE_REOPEN_OR_CARRY_FORWARD_REGISTER.md`
16. `16_INVENTORY_NEXT_CONTROLLED_ACTION_AND_OWNER_MATRIX.md`
17. `17_INVENTORY_REOPEN_DEEP_REVALIDATION_REPORT.md`
18. `18_INVENTORY_REOPEN_SHA256_MANIFEST.txt`
19. `19_SESSION_CLOSURE_SMEPLUS-26-09-02-INV-REOPEN-001.md`
20. `20_INVENTORY_PENDING_JOINT_SESSION_3_INTERFACE_REGISTER.md`

If evidence is missing, create the deliverable with `HOLD / EVIDENCE REQUIRED`. Do not fabricate closure.

---

## 9. Terminal Status

Use only:

- `INVENTORY FULL REOPEN DEEP REVALIDATION COMPLETE — READY FOR INDEPENDENT REOPEN AUDIT`
- `HOLD / EVIDENCE REQUIRED`
- `FAIL / FROZEN — MATERIAL EVIDENCE / GOVERNANCE / CLEAN-ROOM FAILURE`

Do NOT self-declare Inventory Boss Gate PASS, Team B authorization, Team C authorization or Development readiness.

---

## 10. Hard Rules

`No Evidence = No Progress.`  
`No Material Unknown Exhaustion = No Inventory Evidence Gate PASS.`  
`No reset-to-zero challenge.`  
`No repeated question without a material delta.`  
`No Answer Key Before Research.`  
`No Cross-Team Execution.`  
`No Evidence Preservation = No Lifecycle Promotion.`  
`Never Skip Gate.`  
`Boss = Sole Final Approver.`

---

## 11. Boss Addendum — Inventory Reopen Parallel Safety and Boundary Strengthening

This Inventory Reopen session must incorporate the Boss-approved parallel execution control, Dual Challenge Mandate, and the latest Account / Inventory boundary rules.

### 11.1 Dual Challenge Mandate

1. `9 Veto Challenge Council` is the primary mandatory Gate challenge body.
2. `9 Special Team Challenge` is the supplementary deep-dive mechanism for Boss-identified risks.
3. Both report directly to Boss only.
4. Neither may declare Gate PASS, authorize Team B, authorize Team C, authorize development, merge, release, or production.
5. Boss remains the sole Final Approver.

### 11.2 Clean-room Principles

All Inventory evidence, findings, and recommendations must enforce these four principles:

1. `Reference Only` — Odoo / SAP / Salesforce / Legacy / Dump are for learning and business-semantic proof only.
2. `No Copy / No Clone / No Reuse` — no source code, XML, QWeb, ORM, schema, workflow, naming pattern, or application architecture reuse.
3. `Migrate Business Facts + Business Semantics Only` — not legacy application architecture.
4. `SMEsPlus Target Design Must Be Original` — clean-room Node.js SaaS target design with Boss approval.

Every deliverable must explicitly state its Clean-room impact or Clean-room boundary.

### 11.3 Inventory-specific Mandatory Deep Challenges

This Inventory Reopen must deeply test and publish evidence for:

1. Product Category / Product Group valuation-policy ownership and boundary.
2. Manual vs Automated inventory valuation as source behavior and target hypothesis.
3. Periodic vs Perpetual stock/accounting behavior as an interface issue, not an Inventory-only closure.
4. Standard / FIFO / AVCO or other costing behavior only where source/dump evidence supports it.
5. `stock.move`, `stock.quant`, `stock.picking`, valuation layer and physical movement semantics.
6. Physical count / cycle count / adjustment / freeze / conflict / backdate behavior.
7. Stock cut-off as of period close date.
8. Opening and closing stock quantity continuity.
9. Stock valuation handoff requirements to Accounting.
10. Stockable / Consumable / Service routing and edge cases.
11. Product Category-level financial-account configuration as evidence only, not target design cloning.
12. Inventory-owned facts required for later Account x Inventory Joint Session.

### 11.4 Parallel-session Safety

This Inventory session is expected to run in parallel with Account Reopen.

Before execution, the executor must:

1. create an isolated Inventory worktree;
2. create/use a dedicated Inventory execution branch;
3. verify the current branch before every commit;
4. never reuse the Account session worktree or branch;
5. never reuse the Joint session worktree or branch;
6. never commit Inventory evidence to an Account or Joint branch;
7. never commit Account or Joint evidence to the Inventory branch;
8. not push until final branch verification is complete;
9. include a branch/worktree verification note in the session closure.

Required branch:

`audit/inventory-reopen-2026-09-02-inv-reopen-001`

Required execution folder:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/EXECUTION/`

### 11.5 Cross-domain Boundary

Inventory may define Stock Truth and Inventory-owned facts.

Inventory must not close Account-owned findings.

Accounting-dependent items must be routed to one of these statuses:

- `INVENTORY_OWNED_STOCK_FACT`
- `ACCOUNTING_INTERFACE_REQUIREMENT`
- `PENDING_ACCOUNT_SESSION`
- `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION`
- `OUT_OF_INVENTORY_SCOPE`

Inventory must not independently close:

- COA / Account Type / Account Group conclusions;
- final journal entry design;
- VAT / WHT / CIT statutory conclusions;
- retained earnings / current-year earnings logic;
- Account lock-date policy as Accounting truth;
- Inventory valuation to GL reconciliation as final Accounting closure;
- Account x Inventory Backbone baseline.

These must be carried to Account Reopen or the later Account x Inventory Joint Reopen.

### 11.6 Mandatory Session 3 Interface Register

The additional deliverable `20_INVENTORY_PENDING_JOINT_SESSION_3_INTERFACE_REGISTER.md` must list:

1. Inventory-owned conclusions ready for later joint use.
2. Accounting-dependent open questions.
3. Joint Account x Inventory questions.
4. Required evidence for Session 3.
5. Blocked baseline assumptions.
6. Owner and target gate for each pending interface.
7. Whether the item blocks Inventory-only understanding, Account-only understanding, or Joint Backbone publication.

### 11.7 Final Reinforced Stop Condition

This Inventory Reopen may end only at evidence publication and recommendation.

It must not declare:

- Inventory final closure;
- Account closure;
- Account x Inventory Backbone baseline;
- Gate PASS;
- Team B authorization;
- Team C authorization;
- Development authorization.
