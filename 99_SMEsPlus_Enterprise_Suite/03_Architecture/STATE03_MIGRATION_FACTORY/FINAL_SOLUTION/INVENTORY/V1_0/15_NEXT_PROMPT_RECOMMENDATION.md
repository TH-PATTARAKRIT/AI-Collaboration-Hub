# 15 — Next Prompt Recommendation

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V1-001` | Jira: `ERPPLUS-139`
Status: `RECOMMENDATION ONLY — BOSS CHOOSES THE NEXT SESSION`

---

## 1. Candidate Next Sessions

| # | Candidate | What it would do | Prerequisite | Value |
|---|---|---|---|---|
| A | **Joint Accounting ↔ Inventory session** | Close the twelve `JT-*` decisions, starting with valuation-policy ownership and the period-close design. | Boss convenes it; the Accounting track must supply a counterpart. | **Highest.** Unblocks valuation, close, landed cost, return cost basis and work-in-progress in one pass. |
| B | **Thai user validation session** | Walk a small panel of real Thai SME users through file 11's labels and file 05's sixteen scenarios; produce a per-label and per-flow acceptance record. | Boss commissions; needs real users, not a proxy. | **High.** It is the only precondition shared by every user-facing part of the design, and it is comparatively cheap. |
| C | **Independent re-audit of this package** | A separate session verifies this package's clean-room compliance, evidence traceability and internal consistency. | Boss decides re-audit is needed rather than reading it directly. | Medium. Addresses tension `T-5`. |
| D | **Migration provenance design session** | Design the provenance reference as a first-class Migration Factory component. | None — it can start now. | High and independent. Expert lane E-2 calls its absence the largest silent risk. |
| E | **Inventory resilience and exception design session** | Close `GAP-FS-23` — interrupted counts, connectivity loss mid-scan, interrupted planning runs. | None. | Medium. A gap this session created and should not leave open indefinitely. |
| F | **Boss history-containment ruling** | Not an AI session at all — a Boss decision on the `C-05` options. | Boss only. | Blocking for the evidence chain, and nothing else can substitute for it. |

---

## 2. Recommendation

**Run B and D in parallel, and put A on Boss's own calendar.**

Reasoning: A is the highest-value session but needs a counterpart Boss must convene, so it cannot be started unilaterally. B and D are both fully unblocked, are independent of each other and of A, and each removes a precondition that otherwise sits underneath everything. C should wait until Boss decides whether he prefers to read this package himself. E is real but smaller and can follow. F is not a session — it is a decision only Boss can make, and it should be made regardless of which session runs next.

---

## 3. Recommended Prompt for the Next Session (Option B — Thai user validation)

> **Session:** `SMEPLUS-26-09-XX-INV-THAI-USER-VALIDATION-001`
> **Jira:** `ERPPLUS-139` · **STATE03 — Architecture** · Control Level `/L999.999`
>
> **Authoritative source:** `design/inventory-final-solution-v1-2026-09-02-001`, folder
> `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/FINAL_SOLUTION/INVENTORY/V1_0/`
>
> **Purpose.** Produce a Thai user validation instrument and, once real user sessions have been run, a per-label and per-flow acceptance record that converts the `UNVALIDATED - THAI USER REVIEW REQUIRED` rows in file 11 into evidenced decisions.
>
> **Mandatory reading:** files 03, 04, 05, 11 and 12 of the package above.
>
> **Scope.**
> 1. Build a validation instrument covering all 29 menu names, the report, document and reason-code names, and the sixteen UAT scenarios — phrased for a Thai storekeeper, a warehouse supervisor, a purchaser, an owner and an external accountant.
> 2. For each item, capture accept / reject / replace, plus the user's own words for the concept.
> 3. Specifically test the five open Thai-practice questions: the three-document split of transfers; the count freeze policy; the adjustment and scrap reason lists; the warehouse-against-branch distinction; and which internal location roles Thai warehouses actually use.
> 4. Produce an acceptance record per label and per flow, so that "validated" is evidenced rather than asserted.
>
> **Boundaries.** No screen design. No code. No schema. Clean-room Layer 1 output only — no reference-ERP name, code, model, field, method, schema or markup. No Thai statutory claim: every statutory question stays `HOLD / EVIDENCE REQUIRED` and routed to the Accounting-Tax track. Do not close any item in file 12 that a user session did not actually answer. Do not declare `PASS` and do not authorize any team, merge or release.
>
> **Terminal status:** one of `READY FOR BOSS FINAL GATE REVIEW - THAI USER VALIDATION INSTRUMENT ONLY`, `HOLD - MATERIAL GAP / BOSS DECISION REQUIRED`, or `FAIL / FROZEN - EVIDENCE OR CLEAN-ROOM RISK`.
>
> `No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.`

---

## 4. Recommended Prompt for the Parallel Session (Option D — Migration provenance)

> **Session:** `SMEPLUS-26-09-XX-MIGRATION-PROVENANCE-DESIGN-001`
> **Jira:** `ERPPLUS-139` · **STATE03 — Architecture**
>
> **Purpose.** Design the provenance reference — the mapping from every legacy source record to its SMEsPlus record — as a first-class Migration Factory component, because it does not exist and nothing about cutover can be reconciled or safely replayed without it.
>
> **Mandatory reading:** files 05 (`FL-13`), 06 (`CN-36`, `IV-09`), 10 (`HX-23`…`HX-25`) and 12 (`GAP-FS-08`, `GAP-FS-09`, `RISK-C02`) of the Inventory Final Solution v1.0 package.
>
> **Scope.** What a provenance reference must carry; how it survives merges, splits and renames in the legacy data; how replay idempotency is built on it; how reconciliation before and after cutover uses it; and how opening-balance certification (`G-5`) depends on it.
>
> **Boundaries.** Conceptual design only — no schema, no code, no vendor content. Do not resolve `C-02`; state what provenance requires of whatever ruling Boss makes.
>
> **Terminal status:** one of the three permitted statuses.
>
> `No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.`

---

## 5. What Should Not Be the Next Session

| Not this | Why |
|---|---|
| A schema or data-model session | Blocked by `C-02`, `U-03` and the absent provenance layer; and it would be design work no one has authorized. |
| A screen or user-interface design session | Blocked by the total absence of Thai user validation. |
| Any build, migration or release session | Not authorized by any ruling in this programme. |
| Another Inventory-only functional pass | Diminishing returns — what remains open is Joint, Boss-only, or needs real users, none of which another Inventory-only AI session can supply. |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
