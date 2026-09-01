# CORR-007B — 9 Veto Challenge Council Report

Project: SMEsPlus ENTERPRISE SUITE  
Branch: `audit/inventory-core-corr007b-3high-closure-010`  
Context: Boss-approved governance addendum for CORR-007B / N-A12-01  
Status: Governance ruling publication only; not Gate PASS; not Team B/C authorization

## 1. Boss Approval

Boss approved the dual challenge model and directed execution.

The main duty of the added challenge capacity is to operate as the **9 Veto Challenge Council**.

The supplementary duty is to operate as the **9 Special Team Challenge** when Boss raises a specific concern requiring deeper domain proof.

Both report directly to Boss only.

## 2. Authority Boundary

The 9 Veto Challenge Council:

- reports directly to Boss only;
- is independent from PMO, Team A, Team B, Team C, Team D, Developer, and execution ownership;
- may challenge any evidence, source/dump interpretation, functional design, database design, integration/localization, code/UI proof, clean-room claim, carry-forward logic, or Boss decision recommendation;
- cannot declare Gate PASS;
- cannot authorize Team B;
- cannot authorize Team C;
- cannot authorize development, merge, release, or production;
- cannot override Boss.

Boss remains the sole Final Approver.

## 3. 9 Veto Challenge Council Composition

The council is formed by the existing 5 Special Team challenge capacity plus 4 Boss-appointed AI expert roles.

| # | Capacity | Veto / Challenge Focus |
|---:|---|---|
| 1 | Team A — Source Extraction & Observation | Source/dump evidence, source-to-fact extraction, evidence traceability |
| 2 | Team B — SMEsPlus Canonical Domain Design | Canonical domain, clean-room semantic model, target domain consistency |
| 3 | Figma / UX Team | Screen flow, operational usability, user-proofed workflow, UAT handoff |
| 4 | Team C — Engineering / Migration Adapter / Implementation | Engineering feasibility, implementation boundary, migration adapter proof |
| 5 | Team D — Independent QA / Compliance / Regression | Regression, compliance, reproducibility, gate-readiness verification |
| 6 | Leader Functional Design | Business flow, Odoo module mapping, functional logic, FSD, workflow matrix, UAT test plan |
| 7 | Leadership Database Design | Table structure, relations, PostgreSQL schema, master data, migration map, performance risk |
| 8 | Lead Integration & Localization | API, webhook, Thai tax/accounting localization, WHT/VAT/PND, integration settings |
| 9 | Lead Code & UI Architect | Python/XML/QWeb source learning, UI/report behavior, code quality, module boundary |

## 4. Mandatory Veto Duties

Before any closure recommendation, the council must challenge:

1. evidence sufficiency;
2. source/dump interpretation;
3. business-semantic extraction;
4. functional design completeness;
5. database/data migration impact;
6. integration/localization completeness;
7. code/UI/report evidence;
8. clean-room compliance;
9. carry-forward owner, target gate, evidence requirement, and stop condition;
10. whether the Boss decision recommendation is overstated.

## 5. Own-Domain Deep Challenge Rule

If an issue belongs to one capacity's own domain, that capacity must not merely ask questions.

It must:

- test directly where possible;
- re-read source/dump evidence;
- identify missing proof;
- separate fact, inference, and recommendation;
- publish a domain-specific challenge note;
- refuse closure when evidence is insufficient.

## 6. Immediate Application to N-A12-01

N-A12-01 is reopened for functional-design challenge because the prior CORR-007B proof reached source-mechanism level, but did not complete the functional design proof required by Boss.

The council must challenge at minimum:

1. Product Category-level valuation policy;
2. Manual vs Automated inventory valuation;
3. Periodic vs Perpetual accounting behavior;
4. monthly close;
5. Month 12 year-end close;
6. retained earnings under Equity / Account Category 3;
7. stock.move cut-off / backdate control;
8. inventory valuation to GL reconciliation;
9. opening balance carry-forward;
10. source + dumpfile business semantics;
11. clean-room SMEsPlus target design boundary.

## 7. Council Finding

The previous statement `Pure Inventory High blockers = 0` must not be used as functional-design closure for N-A12-01.

Corrected governance status:

`N-A12-01 = REOPENED HIGH FUNCTIONAL DESIGN GAP UNTIL 9 VETO CHALLENGE COUNCIL REVIEW IS COMPLETE`

This report does not declare Gate PASS and does not authorize Team B or Team C.
