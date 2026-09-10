# Research Gap and Risk Register

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Status: `FINAL GATE INPUT / OPEN CONTROLS`  
Final Approver: Boss

## 1. Executive Position

The historical Phase B evidence package is accessible and useful for controlled learning. The current Session baseline cannot be fully certified because current source/dump identity, lineage, and row-level mapping evidence remain incomplete.

## 2. Open Gaps

| Gap ID | Gap | Severity | Evidence Position | Owner | Required Resolution | Status | Gate Impact |
|---|---|---|---|---|---|---|---|
| DR-GAP-001 | Current source archives lack independently verified SHA-256 and file inventory | Critical | Current uploads received; archive bodies not independently evidenced | Source Evidence Owner | Produce SHA-256, archive member manifest, size, timestamp, source version | HOLD | Blocks current source certification |
| DR-GAP-002 | 1,436 historical modules to 1,502 current records delta is not reconciled | Critical | Historical `Module_Inventory.csv` verifies 1,436; current 1,502 is a working claim | Source Research Lead | Row-level delta register for 66 records | HOLD | Blocks all-module coverage claim |
| DR-GAP-003 | CLASS-A/B/C/D register is not inspectable | Critical | Counts provided in Session; module-level list unavailable | Governance / License Reviewer | Provide classified manifest with evidence and reviewer | HOLD | CLASS-C/D treatment cannot be independently verified |
| DR-GAP-004 | CLASS-D 12 modules lack explicit names and Boss ruling | Critical | Quarantine count only | Boss / Governance | Keep quarantined or approve specific research items | HOLD | Blocks CLASS-D research |
| DR-GAP-005 | Current dump identity and SHA-256 are not bound to research outputs | Critical | Historical dump evidence exists; current version not proved | Database Evidence Owner | Dump hash, version, extraction timestamp, restore/schema evidence | HOLD | Blocks current DB certification |
| DR-GAP-006 | 13,940 historical to 13,942 current column delta is unresolved | High | Two-column delta is a working claim | Database Research Lead | Current column inventory and delta explanation | HOLD | Blocks current schema reconciliation |
| DR-GAP-007 | Constraint/FK/index evidence used dump-string fallback | High | Historical gate explicitly records limitation | Database Research Lead | `pg_restore`/schema.sql or restored metadata validation | HOLD | Limits schema-level assurance |
| DR-GAP-008 | Current 27,682 mapping distribution lacks inspectable register SHA and lineage | Critical | Total is historical; current status distribution provided as working baseline | Mapping Lead | Current mapping file, SHA-256, timestamps, row-level lineage | HOLD | Blocks DR4 certification |
| DR-GAP-009 | 18,979 unmatched/not-found records are not semantically classified | Critical | Current working distribution includes table/column not found | Mapping + Business Owners | Rule-based and sampled classification into normalized statuses | HOLD | Blocks migration design |
| DR-GAP-010 | No reverse DB-only inventory | High | Mapping starts from source expectations | Database/Mapping Lead | Identify tables/columns/business facts without source-field counterpart | HOLD | DB-only facts may be omitted |
| DR-GAP-011 | Orphan, duplicate, cross-company, quantity/value, and unbalanced-ledger checks not evidenced | Critical | Structural inventories only | Data Quality Lead | Executable validation queries and evidence pack | HOLD | Blocks migration readiness |
| DR-GAP-012 | End-to-end business behavior is not proven for every domain | Critical | Method/UI inventories are discovery evidence, not executed proof | Functional Owners / QA | Behavioral scenarios, sample transactions, logs/screenshots | HOLD | Blocks all-module semantic certification |
| DR-GAP-013 | Current authoritative Board/STATE/STEP binding is unresolved | High | Session binding not tied to authoritative registry | PMO | Bind Session to approved STEP and denominator | HOLD | Board/STATE/STEP percentages remain TBD |
| DR-GAP-014 | Independent legal/license review is not recorded | Critical | Mixed LGPL-3/OEEL-1 and third-party source observed | Legal / License Reviewer | Module-level treatment ruling and clean-room protocol sign-off | HOLD | Blocks unrestricted source treatment |
| DR-GAP-015 | Independent domain-owner review is incomplete | High | Blueprint prepared by AI analyst | Accounting, Inventory, MRP Owners | Rule-by-rule review and exception log | HOLD | Blueprint remains review baseline |

## 3. Risk Register

| Risk ID | Risk | Severity | Trigger | Mitigation | Residual Position |
|---|---|---|---|---|---|
| DR-RISK-001 | Accidental architectural cloning | Critical | Source class/table/module names appear in target design | Enforce semantic abstraction and independent naming/design review | Controlled but requires independent review |
| DR-RISK-002 | Proprietary algorithm leakage | Critical | Method-level implementation is translated into target service | CLASS-C black-box treatment; CLASS-D quarantine; no code copying | HOLD until license review |
| DR-RISK-003 | False completeness claim | Critical | 1,502/all-module research reported without current evidence | No Evidence = No Progress; Final Gate recommendation HOLD | Controlled |
| DR-RISK-004 | Migration fact loss | Critical | DB-only facts or unmatched source fields ignored | Reverse DB-only inventory and business-owner classification | Open |
| DR-RISK-005 | Accounting imbalance | Critical | Posting design lacks strict debit/credit, period, currency controls | Immutable posting engine, balance invariant, closed-period rejection | Design control defined; not tested |
| DR-RISK-006 | Inventory quantity/value divergence | Critical | quantity events and valuation events are not atomically linked | Separate immutable ledgers with correlation and reconciliation | Design control defined; not tested |
| DR-RISK-007 | Negative stock valuation distortion | High | outbound event precedes receipt/cost evidence | Explicit negative-stock policy and later cost-adjustment event | Open policy decision |
| DR-RISK-008 | MRP WIP/cost leakage | Critical | partial production or scrap not closed correctly | WIP subledger, material/output correlation, close validation | Design control defined; not tested |
| DR-RISK-009 | Cross-tenant data leakage | Critical | tenant identifier accepted from untrusted payload or missing filter | Trusted auth context, tenant-scoped repositories, authorization tests | Design control defined; not tested |
| DR-RISK-010 | Duplicate financial/stock effects | Critical | retries repeat posting/completion | Idempotency key + aggregate version + event uniqueness | Design control defined; not tested |
| DR-RISK-011 | Statutory localization error | Critical | VAT/WHT/tax invoice rules inferred without legal review | Thai tax owner and legal review; effective-dated rules | Open |
| DR-RISK-012 | Historical closure inherited as current PASS | High | v1.5 closure used without current lineage | Revalidate accessibility, version, timestamp, scope, consistency | Controlled by current HOLD |

## 4. Required Next Evidence Pack

A controlled continuation requires:

1. Current three-archive SHA-256 manifest and member inventory.
2. Current 1,502-row source manifest with classification and license evidence.
3. Explicit 66-row historical/current delta report.
4. Current dump identity, hash, schema extraction evidence, and 13,942-column register.
5. Current 27,682 mapping register with normalized statuses and row lineage.
6. DB-only fact inventory and anomaly/orphan validation pack.
7. Per-domain behavioral evidence for Finance, Sales, Procurement, Inventory, Manufacturing, Tax, Treasury, Assets, Approval, and shared platform domains.
8. Independent clean-room/license review and domain-owner review.

## 5. Gate Position

`OPEN GAPS = 15`  
`CRITICAL = 10`  
`HIGH = 5`  
`FINAL GATE IMPACT = HOLD`
