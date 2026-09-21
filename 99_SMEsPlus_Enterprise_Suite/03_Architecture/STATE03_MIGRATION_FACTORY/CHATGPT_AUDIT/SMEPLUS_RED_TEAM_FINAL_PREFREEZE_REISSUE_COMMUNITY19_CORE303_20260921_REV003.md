# SMEsPlus ENTERPRISE SUITE
## RED TEAM Final Pre-Freeze Re-Issue — Odoo 19 Community Core Corpus

**Session:** `SMEPLUS-26-09-21-008-REDTEAM-COMMUNITY19-CORE303-FINAL`  
**Date:** 2026-09-21  
**Mode:** Independent Data-Level Reconciliation / Final Pre-Freeze Review  
**Boss Decision:** `PENDING` for corpus freeze  
**Current Gate:** `GLOBAL HOLD — PRE-FREEZE / NO FORMAL COVERAGE`

---

## 1. Objective

RED TEAM shall perform the final independent data-level review of the current SMEsPlus Odoo 19 Community research corpus before any Boss Freeze, Function-ID denominator construction, Formal Coverage calculation, or resumption of the automatic `A1 -> A2 -> A3 -> MASTER` execution chain.

This review MUST use the dedicated Odoo Community 19 source distribution as population authority and MUST NOT use any earlier `857`, `722`, `690`, `418`, `398`, `342`, `316`, `309`, or other historical working number as the current population without reconciling it to the source described below.

---

## 2. Authoritative Source Population

Primary learning population:

`Odoo Community 19.0.post20260921`

Authoritative source root:

`02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE /Odoo Community/odoo-19.0.post20260921`

Direct manifest scan result:

- Odoo 19 Community addon manifests: **692**
- Parsed manifest failures: **0**
- Licence: **LGPL-3 for all 692**

The previous `690` population is superseded because it was generated from an older/mixed source inventory. A direct comparison found a **44-row membership delta** between the old 690 and the authoritative 692 source population:

- 23 current Community modules were absent from the old 690 register.
- 21 rows from the old 690 register are absent from the dedicated current Community distribution.

Therefore:

> `690 / 316` MUST NOT be frozen and MUST NOT be used for current Formal Coverage.

---

## 3. Current Recomputed Scope Equation

```text
Authoritative Odoo 19 Community                    692
- Controlled source-scope exclusions              299
------------------------------------------------------
Pre-product-scope candidates                      393

Boss product-scope deferrals affecting 393:
- POS family dependency closure                    38
- eCommerce family                                 19
- Lunch                                             1
- Data Recycle                                      1
- IoT Base                                          1
- Marketing family dependency closure              24
- Payment-provider review rows moved to Next Phase  5
- payment_demo moved to non-core / Next Phase       1
------------------------------------------------------
Current Working Core                              303
```

**Important:** `303` is a **Working Core Candidate count only**. It is **PRE-FREEZE / NOT FORMAL DENOMINATOR**.

### 3.1 Controlled source-scope exclusions = 299

- `EXCLUDE_NON_TH`: **256**
- `EXCLUDE_NONFUNCTIONAL`: **43**
- Total: **299**

Test/QA rows are not research subjects, but they MUST remain available as evidence sources:

`NOT A RESEARCH SUBJECT / RETAINED AS EVIDENCE SOURCE`

Installation status MUST NOT override research scope.

---

## 4. Boss Product-Scope Decisions — Canonical Current State

### 4.1 POS / Restaurant
`DEFERRED-NEXT-PHASE — POS / RETAIL / RESTAURANT`
Current Odoo 19 Community dependency closure: **38 modules**.
Includes `point_of_sale`, `pos_restaurant`, and POS-specific overlays/dependants.

### 4.2 eCommerce
`DEFERRED-NEXT-PHASE — ECOMMERCE`
Current closure: **19 modules**.
Website / Portal foundation may remain only when independently required by Core SaaS.

### 4.3 Lunch
`lunch` -> `DEFERRED-NEXT-PHASE — NON-CORE HR/EMPLOYEE SERVICE`.
Count effect: **1**.

### 4.4 Data Recycle
`data_recycle` -> `DEFERRED-NEXT-PHASE — PRODUCTIVITY / OPTIONAL CAPABILITY`.
Count effect: **1**.
Reverse transitive dependency check into current Core previously returned no retained Core hit.

### 4.5 IoT
`iot` is Enterprise and outside the Community denominator.
`iot_base` -> `DEFERRED-NEXT-PHASE / COMM-G10 only if a generic technical capability is later proven necessary`.
Count effect: **1**.
Its Community reverse dependency closure was POS-family only and already deferred.

### 4.6 Marketing
Boss directive: retain `survey` in current study and move the Marketing business suite to Next Phase.
Direct Community seeds deferred: `mass_mailing`, `marketing_card`, `website_event`, `mass_mailing_sms`.
Dependency closure: **24 modules**.
Enterprise `social` and `marketing_automation` are Next Phase and do not affect Community count.

### 4.7 Payment Gateway / Provider-specific Payment Integration
**ALL provider-specific Payment Gateway / Payment Provider connectors -> NEXT PHASE — PAYMENT GATEWAY INTEGRATION**.

Dedicated Community source contains **21 external provider connectors** in the normalized Next-Phase family.

Count treatment:
- 16 were already outside Core due source-scope rules.
- 5 review rows inside the then-current Core were explicitly deferred by Boss.
- `payment_demo` is removed from Core as demo/non-production capability.

Core boundary:
- `payment` -> **KEEP CORE** as Generic Payment Engine.
- `payment_custom` -> **KEEP CORE** as Generic/Offline Custom Payment Mode and dependency of `delivery`.
- Provider-specific gateway integrations -> **NEXT PHASE**.
- `payment_demo` -> **NON-CORE / DEFER**.

### 4.8 Marketplace Connectors
`DEFERRED-NEXT-PHASE — MARKETPLACE INTEGRATION`
Includes `sale_lazada`, `sale_amazon`, `sale_shopee`.
These are Enterprise and do not change Community Core count.
Generic API/webhook/idempotency/retry/queue/reconciliation/event mechanisms may be evaluated under `COMM-G10` only if independently required by Core.

### 4.9 Other Enterprise / Optional capabilities already deferred
Social Marketing, Marketing Automation, ESG, AI application layer, Meeting Rooms, VoIP, provider-specific marketplace apps, and other Enterprise-only specialized capabilities selected by Boss remain visible in the audit trail but outside Community Core.

---

## 5. Mandatory G10 Rule

Deferred business apps/providers/channels remain Next Phase.

Only a reusable source-neutral technical mechanism proven necessary for Core may be evaluated separately under `COMM-G10`.

Examples: API contract, webhook/event intake, idempotency, retry/queue, reconciliation framework, scheduler, generic notification, external connector abstraction, secure integration boundary.

RED TEAM MUST prevent `COMM-G10` from becoming a backdoor that re-admits deferred business workflows.

---

## 6. Remaining Scope Items Requiring Explicit Attention

Two non-payment Community rows remain unresolved in the current working set:

- `snailmail`
- `snailmail_account`

RED TEAM shall verify their dependency role, determine whether they are required Core dependencies or optional IAP postal/document-delivery capabilities, issue an evidence-based recommendation, and NOT silently remove or retain them.

Final scope disposition remains a Boss decision.

---

## 7. Taxonomy / Ownership Rules for the 303 Working Corpus

Use `COMM-G01..G10`.

Each retained module/function must have:
- Exactly **1 Primary Owner**
- `0..N Secondary Domains`
- `0..N Mandatory Co-Reviewers`

Mandatory co-review is required where applicable for Accounting effect, Inventory valuation effect, Tax effect, or Tenant/company isolation effect.

`COMM-G01` = shared platform/business foundation.
`COMM-G10` = administration/integration/cross-cutting technical mechanisms.
`Secondary=all` is invalid.
Thai statutory requirements remain clean-origin requirements.

---

## 8. Existing Research Already Executed — Do Not Restart Blindly

Executed early Foundation modules:
- `base`
- `uom`
- `base_sparse_field`

All three exist in the authoritative Odoo 19 Community distribution and remain in current Working Core.

Do not discard or restart this evidence solely because the corpus changed.

Current carry-forward state:
`VALID EVIDENCE CANDIDATE / NOT TERMINAL / NOT COVERAGE-ELIGIBLE`

Carry-forward requires source re-anchor, preservation of all open CRQs/findings, material-delta validation, and no automatic conversion into Research-Complete or Formal Coverage.

---

## 9. Auto Pipeline Containment

Historical controller profile was bound to the older 857-corpus route.

Containment executed:
- Local Auto Controller stopped.
- MASTER FND-002 REV009 worker stopped before a REV009 MASTER output package was created.
- No new `A1 / A2 / A3 / MASTER` worker may be dispatched under the old profile.

Current state:
`GLOBAL-HOLD-COMMUNITY19-CORE303-PREFREEZE`

Engine design `A1 -> A2 -> A3 -> MASTER` is retained but requires a new Community19 execution profile after corpus verification and Boss Freeze.

---

## 10. RED TEAM Mandatory Data-Level Tests

1. Population test — reproduce exactly 692 Community manifests.
2. Licence test — verify Community classification and contamination.
3. Membership-delta test — reproduce 44-row old690/current692 delta.
4. Exclusion test — reproduce 299 exclusions and predicates.
5. Test/QA test — 43 excluded from research denominator but retained as evidence sources.
6. Boss-deferral test — verify count effects and prevent double counting.
7. POS closure test — reproduce 38.
8. eCommerce closure test — reproduce 19.
9. Marketing closure test — reproduce 24 while keeping `survey`.
10. Payment test — provider gateways Next Phase; `payment` and `payment_custom` Core; `payment_demo` not Core.
11. Marketplace test — Enterprise marketplace apps do not contaminate Community Core.
12. Dependency/orphan test — every retained 303 row justified.
13. Edition contamination test — no Enterprise, Custom/Third-party, or Odoo18-only row inside 303.
14. Deferred backdoor test — no G01-G10 lane re-admits a deferred business app.
15. Ownership test — one Primary Owner plus mandatory co-reviewers.
16. Remaining-review test — recommend disposition for `snailmail`, `snailmail_account`.
17. Carry-forward test — determine which existing A1/A2 evidence can be re-anchored.
18. CRQ visibility test — no open Critical/High/UNASSIGNED control disappears.
19. Hash/inventory test — immutable file inventory and SHA-256.
20. No Formal Coverage test — no Formal Coverage before Boss freezes Function-ID denominator.

---

## 11. Required RED TEAM Deliverables

1. `00_RED_TEAM_FINAL_REISSUE_REPORT.md`
2. `01_POPULATION_REPRODUCTION.tsv`
3. `02_SOURCE_MEMBERSHIP_DELTA.tsv`
4. `03_EXCLUSION_REPRODUCTION.tsv`
5. `04_BOSS_SCOPE_RECONCILIATION.tsv`
6. `05_DEPENDENCY_AND_ORPHAN_ANALYSIS.tsv`
7. `06_CORE303_CANDIDATE_REGISTER.tsv`
8. `07_TAXONOMY_OWNERSHIP_REVIEW.tsv`
9. `08_REMAINING_REVIEW_DISPOSITION.tsv`
10. `09_CARRY_FORWARD_EVIDENCE_REVIEW.tsv`
11. `10_FINDING_REGISTER.tsv`
12. `11_EXACT_NEXT_ROUTE.md`
13. `MANIFEST_SHA256.txt`

---

## 12. RED TEAM Allowed Disposition

Use only:
- `PASS RECOMMENDATION`
- `CONDITIONAL PASS RECOMMENDATION`
- `HOLD RECOMMENDATION`
- `FAIL RECOMMENDATION`

Do not write `FINAL APPROVED`.
`BOSS DECISION = PENDING` until Boss explicitly freezes the Canonical Community Module Corpus.

---

## 13. Exact Decision Question for RED TEAM

> **Is the current Odoo 19 Community Core working corpus, currently 303 candidates before resolution of the two explicit non-payment review rows, reproducible from the authoritative 19.0.post20260921 source, free from edition/scope contamination, dependency-safe, intentionally bounded by Boss product-scope decisions, and suitable to be presented to Boss as the Canonical Community Module Corpus Freeze Candidate?**

If conditional, identify exact remaining conditions and rows affected. Do not change the denominator merely to obtain a higher coverage result.

---

## 14. Stop Conditions

Issue `HOLD RECOMMENDATION` for any material source population mismatch, unexplained membership delta, invalid exclusion predicate, orphan retained module, dependency break caused by deferral, Enterprise/Custom/Odoo18 contamination, hidden re-admission of deferred functions, unresolved scope contradiction, untracked Critical/High control, invalid carry-forward, or premature denominator freeze.

No Evidence = No Progress. Never Skip Gate.
