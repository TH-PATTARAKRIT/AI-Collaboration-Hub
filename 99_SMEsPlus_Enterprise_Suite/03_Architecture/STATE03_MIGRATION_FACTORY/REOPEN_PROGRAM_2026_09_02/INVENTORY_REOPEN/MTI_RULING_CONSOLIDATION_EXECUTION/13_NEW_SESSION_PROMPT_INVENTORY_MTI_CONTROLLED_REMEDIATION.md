# [SMEPLUS-26-09-05-INV-MTI-CONTROLLED-REMEDIATION-001]
# New Session Prompt — Inventory MTI Controlled Remediation / Ruling-Conformance Re-Specification
# Full Depth L1-L12 + L13+ / L99999.99999

> **Status of this file:** prepared by `SMEPLUS-26-09-04-INV-MTI-RULING-CONSOLIDATION-001` as its required work product. **It is not authorized until Boss commissions it.** Do not execute on the strength of this file alone.

---

## 1. Project Identity

Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Jira: ERPPLUS-139
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Executor: Claude Opus 5 High / Extra
Mode: AAS+ / PMO Governance Execution
Lane: **R1 — Ruling-Conformance Re-Specification (Lane A)**
Status Target: READY FOR BOSS REVIEW — NOT DEVELOPMENT FINAL GATE

Boss is the sole Final Approver.
No Evidence = No Progress.
Never Skip Gate.

---

## 2. Clean-Room Boundary

SMEsPlus is a new clean-room Node.js SaaS ERP.

Reference systems are learning and benchmark inputs only.

Do not copy source code, schema, ORM, workflow implementation, naming dependency, or vendor-specific architecture.

Use OpenSource reference ERP / reference ERP / benchmark ERP wording where reference context is necessary.

---

## 3. Full Depth Standard

Use `SMEsPlus All Module Deep Research Standard — Full Depth L1-L12 / L13+ as required / L99999.99999`.

L1 Domain Understanding · L2 UI/Field/Configuration Forensic · L3 Function Forensic · L4 Cross-Module Dependency · L5 Whole-System Semantic · L6 Contradiction/Failure/Edge Case · L7 Control/Internal Control · L8 Data/Identity/Immutability · L9 SaaS/Multi-Tenant/Multi-Company · L10 Migration/Historical Continuity · L11 Reconciliation/End-to-End Proof · L12 Adversarial Challenge/Audit Veto.

Open `L13+` with reason, evidence, checkpoint lineage, risk or blocker ID, and downstream impact. Do not ask Boss to approve each `L13+` expansion during execution.

---

## 4. Mandatory Evidence Sources

Fetch and read every source below before producing any conclusion. **If any source cannot be fetched and read, stop and publish `HOLD — MANDATORY EVIDENCE SOURCE MISSING`. Do not continue by assumption.**

### 4.1 MTI Ruling Consolidation — the immediate predecessor

Branch: `governance/inventory-mti-ruling-consolidation-2026-09-04-001`
Folder: `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/MTI_RULING_CONSOLIDATION_EXECUTION/`

Mandatory files — **all of them**:
`02_MTI_D01_D02_D03_RULING_CONSOLIDATION.md` · `03_R4_FINDING_TO_RULING_IMPACT_MATRIX.md` · `04_INVENTORY_MTI_CONTROL_MODEL.md` · `05_SAAS_POOL_VS_PRIVATE_COMPANY_BOUNDARY.md` · `06_PRODUCT_IDENTITY_AND_DUPLICATION_POLICY.md` · `07_AUTHORIZATION_CONTEXT_PROOF_REQUIREMENTS.md` · `08_TENANT_CONFIG_OVERLAY_PROOF_REQUIREMENTS.md` · `09_REMAINING_BLOCKER_REGISTER_AFTER_RULINGS.md` · `10_NEXT_CONTROLLED_REMEDIATION_LANE_SPLIT.md` · `11_AAS_PLUS_VERDICT.md` · `12_PMO_RECOMMENDATION.md` · `14_BOSS_DECISION_PACKAGE.md`

### 4.2 Inventory Multi-Tenant Invariant Set — the artifact being re-specified

Branch: `design/inventory-multitenant-invariant-set-2026-09-04-001`
Tip: `dcb92278769d6a8239a5183ec4890e230a7caf68`
Folder: `…/INVENTORY_REOPEN/MULTI_TENANT_INVARIANT_SET_EXECUTION/`

Mandatory files — **all sixteen**, `00` through `15`. This is the package being brought into conformance; a partial read is not sufficient.

### 4.3 Boss Rulings And AAS+ Advice — authoritative

Read all six. **The three AAS+ advice records are mandatory, not optional.**

| File | Branch | Commit |
|---|---|---|
| `24_BOSS_RULING_…MTI-D01-PRODUCT-MASTER-SCOPE-001.md` | `ruling/inventory-mti-d01-product-master-scope-2026-09-04-001` | `d84fe4965850784876acc3420c727494e38c2804` |
| `25_AAS_PLUS_ADVICE_CORRECTION_MTI_D01_OPTION_B_2026_09_04.md` | same | same |
| `26_BOSS_RULING_…MTI-D02-AUTHORIZATION-GRANULARITY-001.md` | `ruling/inventory-mti-d02-authorization-granularity-2026-09-04-001` | `13b3e63f9170f650481cd4caedc237bb4ba54f3a` |
| `27_AAS_PLUS_ADVICE_MTI_D02_COMPANY_WAREHOUSE_OPERATION_TYPE_2026_09_04.md` | same | same |
| `28_BOSS_RULING_…MTI-D03-TENANT-CHANGEABLE-BOUNDARY-001.md` | `ruling/inventory-mti-d03-tenant-changeable-boundary-2026-09-04-001` | `6897cc9e81057d36baccc747a0be4f6363e0cd67` |
| `29_AAS_PLUS_ADVICE_MTI_D03_PLATFORM_CORE_TENANT_OVERLAY_2026_09_04.md` | same | same |

All six exist in the tree at `6897cc9`, which is a descendant of every other evidence commit named in this prompt.

### 4.4 Supporting Evidence

| Package | Branch | Tip | Files |
|---|---|---|---|
| Inventory R4 Deep Research | `audit/inventory-deep-research-r4-l12-2026-09-04-001` | `fc0b16888ddaea1648abea4ee7d78fe3132861d4` | `16_PROCESS_HANDOFF_MAP.md`, `17_ACCOUNTING_COGS_VALUATION_DEPENDENCY_REGISTER.md`, `20_RISK_GAP_DECISION_REGISTER.md` |
| Inventory R4 AAS+ / PMO Review | `review/inventory-r4-aas-pmo-review-2026-09-04-001` | `e218e5b550a2a8f839f295876f0a3ff1ce3e69d4` | `04_R4_F16_STRUCTURAL_BLOCKER_REVIEW.md`, `06_ACCOUNTING_COGS_DEPENDENCY_REVIEW.md`, `10`, `11`, `12` |

---

## 5. Binding Decisions To Carry Forward

Carry this block verbatim into every output file's header context or cite the three ruling files directly.

```
MTI-D-01 = OPTION B — Company-owned Product Master / tenant-company scoped
           product identity. Similar products across tenants/companies are
           separate business objects unless an explicit Boss-authorized
           mapping layer links them for reporting or migration purposes.
           Duplication is NOT a defect.

MTI-D-02 = Company + Warehouse + Operation-Type. Inventory action context
           must carry tenant/company, warehouse and operation type wherever
           applicable, across UI, API, import, export, scheduler, report,
           audit trail and cross-module handoff.

MTI-D-03 = Platform-owned Core + Tenant Config Overlay. Shared SaaS pool
           keeps platform core centrally owned; tenants configure approved
           Inventory master/config records only. Private Company may be
           opened for high-specificity customers through Gate and Boss
           Ruling, and is never automatically approved.
```

---

## 6. Session Purpose

Bring the Inventory multi-tenant design into **conformance** with the three Boss rulings, and specify the proof obligations that follow. This session must answer:

1. What exactly changes in the invariant set to conform to `MTI-D-01`, and what follows from each change?
2. What is the relationship between `CTX` and `AUTH`, and where does the operation-type axis attach?
3. What proof is required for each of the thirteen mandated themes, and which are definable today?
4. Which proof requirements remain **not definable**, and precisely what blocks each?
5. What must Boss rule before the remaining lanes can execute?
6. What exact New Prompt should Claude execute next?

**This is a re-specification and proof-definition session. It is not an implementation, and it is not a new deep research round.**

---

## 7. Mandatory Proof Themes

The session must produce a proof requirement for each theme below, and must state for each whether it is `DEFINABLE`, `DEFINABLE — CONDITIONAL`, `NOT DEFINABLE`, or `HELD` under the Accounting COGS Gap — with the blocker named in every case that is not `DEFINABLE`.

| # | Theme | Predecessor Baseline |
|---:|---|---|
| 1 | Tenant/company product isolation | `RC-P-01` .. `RC-P-04` |
| 2 | Duplicate product names/codes/barcodes across companies without identity collision | `RC-P-05` .. `RC-P-08` |
| 3 | Warehouse-specific authorization | `RC-P-09` .. `RC-P-12` |
| 4 | Operation-Type-specific authorization | `RC-P-13` .. `RC-P-16` |
| 5 | Cross-company report prevention by default | `RC-P-17` .. `RC-P-19` |
| 6 | Controlled mapping/provenance for group-level reporting | `RC-P-20` .. `RC-P-22` — **two are `NOT DEFINABLE`; say so or close them** |
| 7 | SaaS pool configuration boundary | `RC-P-35` .. `RC-P-44` |
| 8 | Private Company escalation criteria | `RC-P-45` .. `RC-P-48` — **three are `NOT DEFINABLE`** |
| 9 | Scheduler/background job context carriage | `RC-P-23` .. `RC-P-25` |
| 10 | API/import/export context carriage | `RC-P-26` .. `RC-P-28` |
| 11 | Immutable audit trail context | `RC-P-29` .. `RC-P-31` |
| 12 | Negative access tests | Structural — every criterion is a **rejection that must occur** |
| 13 | Cross-module handoff context to Sale, Purchase, Manufacturing, Accounting, Approval, Payment, Document and Reporting | `RC-P-32` .. `RC-P-34`, plus **Payment**, which has no published obligation — `RC-F-09` |

**A proof requirement is a proposition plus an acceptance criterion. It is not a proof. No implementation exists, so no theme may be recorded as proven, verified or satisfied.**

---

## 8. Required Work Products

1. `00_EXECUTION_README.md`
2. `01_EVIDENCE_INTAKE_AND_SOURCE_VERIFICATION.md`
3. `02_RULING_CONFORMANCE_DELTA_REGISTER.md` — every change required by the rulings, with its consequence
4. `03_MTI_INVARIANT_SET_R2_CONFORMED.md` — the invariant set re-specified under all three rulings
5. `04_CTX_AUTH_RELATIONSHIP_AND_AXIS_MODEL.md` — `RC-F-05`; where operation type attaches, and to deferred execution
6. `05_CROSS_CONTEXT_REGISTER_R2.md` — the register after `XCR-03`'s elimination
7. `06_PRODUCT_IDENTITY_CONFORMANCE_SPECIFICATION.md` — `MTI-11` and dependents under Option B
8. `07_CONSUMING_MODULE_OBLIGATION_MATRIX_R2.md` — eight modules **including Payment**
9. `08_PROOF_REQUIREMENT_REGISTER_13_THEMES.md` — all thirteen themes, with definability state and blocker
10. `09_NEGATIVE_ACCESS_TEST_SPECIFICATION.md` — theme 12 as a structural specification
11. `10_NOT_DEFINABLE_REGISTER_AND_ROOT_CAUSE.md` — every requirement that cannot be stated, and why
12. `11_OPEN_ITEMS_AND_DEPENDENCY_REGISTER.md`
13. `12_AAS_PLUS_CHALLENGE_VERDICT.md`
14. `13_PMO_NEXT_GATE_RECOMMENDATION.md`
15. `14_BOSS_DECISION_PACKAGE.md`
16. `15_SESSION_CLOSURE.md`
17. `16_SHA256_MANIFEST.md`

---

## 9. Output Branch And Folder

Fresh isolated branch:

`design/inventory-mti-ruling-conformance-2026-09-05-001`

Output folder:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/MTI_RULING_CONFORMANCE_EXECUTION/`

Write nothing outside this folder. **Do not merge to `SMEsPlus`. Do not modify the invariant-set branch — the re-specification is a new document in a new folder, never an edit to published evidence.**

---

## 10. Required Analysis Rules

1. Boss rulings are authoritative. Do not re-litigate `MTI-D-01`, `MTI-D-02` or `MTI-D-03`.
2. Where the published invariant set contradicts a ruling, **the design changes and the ruling stands**.
3. Do not mark any blocker closed because a ruling exists, or because a specification exists.
4. Classify every item as one of: `DECIDED BY BOSS` · `SPECIFIED BUT NOT PROVED` · `PROOF REQUIRED` · `BLOCKED BY ACCOUNTING COGS GAP` · `BLOCKED BY CLEAN-ROOM RELIANCE` · `BLOCKED BY PRIVATE COMPANY CLASSIFICATION` · `HOLD`.
5. Keep SaaS pool controls separate from Private Company escalation controls throughout.
6. Preserve `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` on every valuation, COGS, landed-cost posting, period-close, return-cost-basis and cross-company valuation item.
7. Carry every existing identifier unchanged. Do not renumber, retire or merge `R4-F-*`, `MTI-*`, `REV-F-*`, `RC-*`, `JT-*`, `GAP-*`, `RISK-*` or `TH-HOLD-*`.
8. State counts as counts. `0 of 8`, `0 of 22`, `0 of 10`, `0 of 12`, `0 of 78` must appear unsoftened wherever they are relevant.
9. **Assert no open-item roll-up total.** `REV-F-04` records the 92 figure as not reconstructable and no crosswalk exists. Enumerate new items exactly instead.
10. Where a negative claim is made, state the search **population, pattern, path set and unit**. `NO EVIDENCE FOUND` is not `DOES NOT EXIST`.

---

## 11. Vetoes In Force At The Start Of This Session

| ID | Veto | Effect On This Session |
|---|---|---|
| `AAS-V-01` | Element 10 may not be recorded as supplied, satisfied or suppliable. Its status is `specified, not built, not verified` | **No substitute wording anywhere in the output** |
| `AAS-V-02` | Implementation start vetoed before the three shape decisions are ruled. **Condition satisfied; veto not discharged** | This session may not treat it as lifted; discharge is an AAS+ / Boss act |
| `AAS-V-03` | No cross-company grant may carry valuation content while the COGS Gap stands | Binding on themes 5, 6 and 13 |
| `RC-V-01` | No implementation start against `03_INVENTORY_MULTI_TENANT_INVARIANT_SET.md` as published, until `MTI-11`, `XCR-03`, `04` §4.1 and matrix rows 5-7 are re-specified to a company anchor | **This session's output is the remedy. It does not discharge the veto — an independent check does** |

---

## 12. Hard Prohibitions

Do not:

- Start development, write application code, define a schema, or freeze one
- Modify the canonical branch, or any prior evidence branch
- Merge branches
- Claim Final Gate `PASS`, `APPROVED`, `CLOSED`, or Final Solution accepted
- Mark specification as proof, or definability as verification
- Record element 10 as supplied
- Close a COGS-dependent item without Accounting COGS evidence
- Answer `SME-Q-02`, `SME-Q-03`, `MTI-D-06`, or any Thai statutory question — **no AI may answer these**
- Make any Thai statutory claim
- Classify the severity of `C-02`
- Rule on `MTI-D-04`, `MTI-D-05`, `RC-D-01`, `RC-D-02`, `RC-D-03` or `RC-D-04` — **state options, never choose**
- Use vendor-specific source, schema, workflow or ORM as design authority
- Collapse tenant/company identity to reduce duplicate records
- Describe cross-company product duplication as a defect, anomaly or cleanup candidate
- Treat Private Company as approved, available, or automatically applicable
- Discharge any veto

---

## 13. Publication Requirements

1. Commit all output files.
2. Push the branch to GitHub.
3. Verify the remote branch tip.
4. Recompute the SHA-256 manifest and confirm every digest matches.
5. Publish Direct GitHub Links for: branch · final commit · output folder · Boss Decision Package · any New Session Prompt created · Session Closure.
6. Stop.

---

## 14. Required Final Status

`READY FOR BOSS REVIEW — INVENTORY MTI RULING-CONFORMANCE RE-SPECIFICATION ONLY — NOT DEVELOPMENT FINAL GATE`

Applying additionally to every valuation-related section:

`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`

If evidence is missing:

`HOLD — MANDATORY EVIDENCE SOURCE MISSING`

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
