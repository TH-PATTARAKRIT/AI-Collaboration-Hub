# DOMAIN_01 ACCOUNTING CORE — TEAM B CONTROLLED HANDOFF AUTHORIZATION

## Handoff identity

| Field | Value |
|---|---|
| Project | SMEsPlus ENTERPRISE SUITE |
| State | STATE03 — Architecture |
| Workstream | SMEsPlus Migration Factory |
| Board | Board06 — Data & Canonical Model |
| Domain | DOMAIN_01 — Accounting Core |
| Source team | Team A — Fable Part 1 + Sonnet Part 2 |
| Independent audit | ChatGPT Final Team-A Audit |
| PMO verification | VERIFIED WITH CARRY-FORWARD |
| Boss decision | APPROVED WITH CONTROL |
| Boss decision commit | `512da309b0bbe597a1343ce386302d8f870d1fcf` |
| STEP | TBD / BASELINE LINKAGE REQUIRED |
| Handoff status | AUTHORIZED — SANITIZED INPUT ONLY |

## 1. Authorization

Boss has authorized DOMAIN_01 Accounting Core to move from Team A into the controlled Team B independent clean-room design process.

This authorization is limited to sanitized, neutralized, evidence-backed input.

It is NOT authorization for coding, development, migration execution, deployment, release, production, or reuse of vendor implementation.

## 2. Authorized Team B input

Team B may consume:

- sanitized business facts;
- accounting principles;
- generic business rules;
- business invariants;
- neutral business events and lifecycle findings;
- migration requirements;
- audit/control requirements;
- scoped regulatory requirements;
- cross-ERP common patterns;
- advancement objectives;
- open business questions explicitly marked as unresolved.

Primary sanitized input artifact:

`TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/SONNET_DEEP_SYNTHESIS/13_TEAM_B_CANDIDATE_INPUT.md`

Supporting reviewed artifacts may be used only for traceability and context under the clean-room controls below.

## 3. Prohibited Team B input as design authority

Team B must NOT use the following as target-design authority:

- raw vendor source code;
- vendor ORM/model/table/field/method structures;
- vendor class hierarchy;
- vendor internal hooks/triggers;
- proprietary algorithms;
- Class E/F implementation details;
- quarantine artifacts;
- Class G unknowns represented as facts;
- unqualified regulatory claims beyond evidenced scope.

## 4. Clean-room design objective

Team B must independently answer:

- What should the SMEsPlus Accounting Core business model be?
- What invariants must be guaranteed independently of the reference system?
- What neutral lifecycle/events are appropriate?
- What domain boundaries and responsibilities are appropriate?
- What improvement objectives should be designed into SMEsPlus?
- How will the proposed design demonstrate measurable advancement over the reference capability?

Team B must not translate or port vendor implementation into a target design.

## 5. Advancement requirement

Boss-approved design principle:

`Understand the reference deeply. Rebuild independently. Improve measurably.`

Every major Team B design decision should identify:

1. Independent business requirement/principle.
2. Evidence source or approved Team A finding.
3. Reference limitation or risk, if relevant.
4. Independent design objective.
5. Measurable improvement criterion.
6. Residual assumption or unknown.

Advancement objectives are not pre-approved implementations. Team B must independently evaluate them.

## 6. Mandatory carry-forward controls

1. Class E/F remains restricted and cannot become target architecture by inheritance.
2. Class G remains open and receives zero progress credit.
3. Data-level balance validity of the source snapshot remains unproven.
4. Thai e-Tax integrity official evidence is accepted only for the evidenced e-Tax document scope.
5. Thai Revenue Department serial-number evidence is accepted only for the evidenced tax-invoice scope.
6. General-ledger-wide tamper-evidence and universal gapless journal-numbering requirements remain OPEN unless independently proven.
7. Development/coding remains prohibited until the later design/development Gates are approved.
8. STEP/STATE/Project official percentages remain TBD where the approved baseline/weight is absent.

## 7. Team B expected outputs

Team B should prepare, at minimum:

- independent Accounting Core domain/capability model;
- neutral business lifecycle/event model;
- invariant and business-rule baseline;
- independent conceptual information model;
- accounting/mathematical design principles;
- control/audit design objectives;
- migration-facing canonical requirements;
- advancement design-option register;
- measurable improvement criteria;
- open-question / assumption register;
- clean-room provenance matrix;
- Team B design evidence pack for independent review.

Target implementation artifacts such as code, physical database schema, API implementation, DTO/class/service code, or production configuration remain outside this authorization.

## 8. Next Gate

Team B design outputs must stop at the Team B evidence/design pack and proceed through the next controlled review Gate before any development authorization.

Expected flow:

`Team B Independent Design → Independent Review / PMO Verification → Boss Gate → Development authorization decision`

## 9. Status

```text
TEAM A DOMAIN_01: PASS — BOSS APPROVED WITH CONTROL
TEAM B DOMAIN_01: AUTHORIZED TO START INDEPENDENT CLEAN-ROOM DESIGN
AUTHORIZED INPUT: SANITIZED TEAM A EVIDENCE ONLY
DEVELOPMENT: NOT AUTHORIZED
PRODUCTION: NOT AUTHORIZED
```

**No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.**