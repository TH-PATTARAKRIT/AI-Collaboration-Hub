# QUESTION BANK — STANDARD 35
## ROOM A · applies to EVERY module, without exception

**Version:** V1.00 DRAFT
**Date:** 2026-09-22 · Asia/Bangkok
**Drafted by:** RED TEAM (internal audit)
**Status:** `PREPARED ONLY / READY FOR INDEPENDENT REVIEW` — not agreed, not frozen
**Authority for the rules below:** Boss decisions V1, V2, V3, V5, V7 (2026-09-22)

---

## 1. The rules these 30 questions operate under

| Rule | Value |
|---|---|
| Standard questions | **35 — every module answers all 35. No tiering, no exceptions.** |
| Module-specific questions | ≥ 30 authored by Tester + Odoo Functional, frozen before either lane starts |
| Combined answered floor | **≥ 75 per module** |
| Arithmetic consequence | standard 35 + module-specific **≥ 40** = 75 |
| Padding | **Forbidden.** Every question must be able to be proven wrong. |
| Cannot reach 40 module-specific with real hypotheses | **Raise a Blocker for Boss decision. Do not pad.** |

### Every question must be "touched". Three answers are valid:

| Answer | Meaning | Required with it |
|---|---|---|
| `ANSWERED` | Observed / established, with proof | evidence artifact + hash |
| `NOT_APPLICABLE` | This capability does not exist in this module | **reason, in business language** |
| `NOT_OBSERVED` | Should exist but could not be found | exactly what was tried, and on which surface |

**A blank is not an answer.** CI rejects a module record with any of the 35 unfilled.

---

## 2. Why these 35 and not others

Every question below is traceable to the Project Constitution. None was invented by RED TEAM.

| Source | Questions |
|---|---|
| §3.2 Approval / Execution / Posting separation | Q11 – Q14 |
| §12 ERP and Accounting Control | Q15 – Q26 |
| §3.3 Multi-Tenant and Security | Q27 – Q30 |
| §12 goods movement and inventory valuation (Boss correction, 2026-09-22) | Q31 – Q35 |
| §11 AI Coding Rules — "must not guess" list | Q01 – Q10 |

This matters: a question set invented by an AI can be argued with. A question set derived from the
governance document the team already signed cannot.

---

## 3. Answer record schema

```yaml
MODULE:        <technical name>       # traceability only, stripped at the ROOM B gate
QID:           STD-Q07
LANE:          A | B
STATUS:        ANSWERED | NOT_APPLICABLE | NOT_OBSERVED
BUSINESS_ANSWER: >
  What the system does, in business language.
  No model names, no field names, no module names. This is what the Reconciler compares.
OBSERVED_DETAIL: >
  Raw detail. Technical identifiers allowed here. Stops at the ROOM B gate.
SURFACE:       S1 | S2 | S3 | S4 | S5 | S6      # Lane B only
EVIDENCE:      [path]                            # mandatory when STATUS = ANSWERED
EVIDENCE_SHA256: [hash]
REASON:        >                                 # mandatory when NOT_APPLICABLE / NOT_OBSERVED
CONFIDENCE:    CONF-1 | CONF-2
```

Because both lanes answer the **same QID**, the Reconciler compares cell to cell.
No semantic matching. No interpretation. A script does it.

---

## 4. THE STANDARD 35

Each question carries a `DISCONFIRMING_OBSERVATION` — what result would prove the expectation
wrong. This is the mechanical test for Rule ๔: a question that cannot be proven wrong is padding,
and CI rejects it.

---

### A. Behaviour and lifecycle — Q01–Q10
*Constitution §11: the list of things an agent must never guess.*

**STD-Q01 — Business purpose**
What business outcome does this capability exist to produce, stated without naming the system?
`DISCONFIRM:` the capability produces no outcome a business user would ask for.

**STD-Q02 — Who may use it**
Which roles can reach this capability, and which are blocked?
`DISCONFIRM:` a role with no business reason can reach it.

**STD-Q03 — Entry points**
By what routes can this be started — screen, scheduled job, automation, external call?
`DISCONFIRM:` a route exists that no one documented, e.g. it can be triggered without a user.

**STD-Q04 — Records created or changed**
What business records come into existence or change as a result?
`DISCONFIRM:` a record changes that the user was never told about.

**STD-Q05 — Mandatory data**
What must be supplied before the system will let the work proceed?
`DISCONFIRM:` the work proceeds with a mandatory value missing.

**STD-Q06 — States**
What states can the business document occupy, from creation to final?
`DISCONFIRM:` a state exists that is reachable but not listed.

**STD-Q07 — Transition triggers**
What causes each state change — a person, a rule, a schedule, another document?
`DISCONFIRM:` a state changes with no identifiable trigger.

**STD-Q08 — Blocking validations**
Which rules stop the work, and what does the user see when they do?
`DISCONFIRM:` a rule that should block, warns only, and the work completes.

**STD-Q09 — Negative path**
What happens when the work fails midway — is it fully undone, or partly applied?
`DISCONFIRM:` a failure leaves the records in a half-changed state.

**STD-Q10 — Repetition and duplication**
What happens if the same action is performed twice, or by two people at once?
`DISCONFIRM:` duplicate business documents are created with no warning.

---

### B. Approval, execution and posting separation — Q11–Q14
*Constitution §3.2. This separation is mandatory for SMEsPlus, so every module is tested for it.*

**STD-Q11 — Approval requirement**
Does anything here require approval before it may proceed, and who approves?
`DISCONFIRM:` something with financial effect proceeds with no approval at all.

**STD-Q12 — Approval does not execute**
When approval is given, does the business transaction execute immediately as part of that act?
`DISCONFIRM:` approving also executes the transaction in the same step.
*This is the single most important structural question in the set.*

**STD-Q13 — Who executes**
What actually performs the business transaction, and is it separable from the approval?
`DISCONFIRM:` execution cannot be separated from approval.

**STD-Q14 — Posting trigger**
What exact event causes accounting posting — approval, confirmation, delivery, payment, a date?
`DISCONFIRM:` posting happens inside the approval step, or at a point nobody can name.

---

### C. Accounting — Q15–Q22
*Constitution §12.*

**STD-Q15 — Journal entries produced**
What accounting entries result, and when?
`DISCONFIRM:` an entry appears that the business event does not justify.

**STD-Q16 — Debit and credit logic**
Which side moves, against what, and on what basis is the account chosen?
`DISCONFIRM:` the account chosen changes with no rule the business can state.

**STD-Q17 — Posting date versus document date**
Which date drives the accounting, and can they differ?
`DISCONFIRM:` posting lands in a period the user did not intend and was not warned about.

**STD-Q18 — Accounting period control**
Can a back-dated entry land in a closed period, and who may override?
`DISCONFIRM:` a closed period accepts a new entry.
*Statutory exposure — a filed financial statement changing after filing.*

**STD-Q19 — Reversal**
How is a posted entry reversed, and what does the reversal look like in the ledger?
`DISCONFIRM:` a posted entry can be deleted rather than reversed.

**STD-Q20 — Cancellation and correction**
Can a confirmed business document be cancelled or corrected, and what happens to what it produced?
`DISCONFIRM:` cancellation leaves the accounting effect in place.

**STD-Q21 — Reconciliation impact**
What does this leave open to be matched later, and how is the match recorded?
`DISCONFIRM:` an item is marked matched without a counterpart.

**STD-Q22 — Financial report impact**
Which financial reports change as a result, and by how much?
`DISCONFIRM:` a report changes in a way the underlying entries do not explain.

---

### D. Tax, money and numbering — Q23–Q26
*Constitution §12. Thai statutory relevance.*

**STD-Q23 — Tax basis and VAT**
On what amount is tax computed, and what determines the rate?
`DISCONFIRM:` the base or rate changes with no rule an accountant can state.
`LEGAL_TAX_REVIEW_REQUIRED` if Thai treatment cannot be established from evidence.

**STD-Q24 — Withholding tax**
Is withholding applied, at what point in the flow, on what base, and what document is produced?
`DISCONFIRM:` withholding is computed on a base that differs from the payment it accompanies.
`LEGAL_TAX_REVIEW_REQUIRED` if the Thai rule cannot be established from evidence.

**STD-Q25 — Currency, exchange and rounding**
How are foreign amounts converted, at what rate and date, and where does rounding land?
`DISCONFIRM:` a rounding difference disappears instead of being posted somewhere.

**STD-Q26 — Document numbering**
How is the document number produced, is it gapless, and can it be reused or altered?
`DISCONFIRM:` a number can be changed after posting, or reused.

---

### E. Multi-tenant, security and audit — Q27–Q30
*Constitution §3.3. Every uncertainty here is a Blocker by constitutional rule, not a note.*

**STD-Q27 — Company, branch and tenant scope**
Which company, branch and tenant does the data belong to, and what enforces that boundary?
`DISCONFIRM:` a record exists that belongs to no scope, or to more than one.

**STD-Q28 — Cross-boundary visibility**
Can a user of one company, branch or tenant see, reach or affect another's data — by screen,
report, search, export, or external call?
`DISCONFIRM:` any route returns another scope's data.
*A single positive here is a critical finding, not a note.*

**STD-Q29 — Permission and record-level access**
Beyond menu visibility, what limits which individual records a user may read, change or delete?
`DISCONFIRM:` menu access alone determines record access.

**STD-Q30 — Audit trail and configuration ownership**
What is recorded about who changed what and when, who can change the configuration behind this
capability, and can the trail itself be altered?
`DISCONFIRM:` a change of financial or permission consequence leaves no trace, or the trace can
be edited.

---

### F. Goods movement and the inventory–accounting bridge — Q31–Q35
*Added on Boss correction, 2026-09-22: in practice almost every module touches Inventory and
Account, so both belong in the common floor. Logically this section sits between B and C —
it is appended here to avoid renumbering a set already under review.*

**STD-Q31 — Physical quantity effect**
Does this capability create, consume, reserve or move physical quantity, and between which places?
`DISCONFIRM:` quantity on hand changes without a goods movement anyone can point to.

**STD-Q32 — What actually moves the goods**
Which event moves the goods, and is it the same event that confirms the business document?
`DISCONFIRM:` goods move before the document has reached a state that authorises the movement.

**STD-Q33 — Inventory-to-accounting bridge**
Does the goods movement produce an accounting entry, at what moment, and at what value?
`DISCONFIRM:` goods move with no valuation entry, or the entry carries a value the business
cannot explain.
*This is the join between Q14 (posting trigger) and Q31 (quantity effect). Most large ERP
errors live exactly here: goods moved in one period, cost recognised in another.*

**STD-Q34 — Shortage and negative quantity**
What happens when there is not enough stock — blocked, warned, or allowed to go negative?
`DISCONFIRM:` quantity on hand goes below zero with no control and no record of who allowed it.

**STD-Q35 — Unit of measure**
Can the quantity be expressed in more than one unit, how is conversion performed, and where does
the rounding land?
`DISCONFIRM:` converting to another unit and back does not return the original quantity.


---

## 5. What this set does NOT cover — deliberately

These 35 are the **floor common to every module**. They do not go deep into any one domain.
Depth is the job of the ≥40 module-specific questions from Tester + Odoo Functional.

Not covered here, and expected in the module-specific set:
warehouse strategies and replenishment rules · bill of material explosion and cost roll-up ·
payroll calculation · pricing and discount cascade · specific Thai report layouts ·
e-Tax invoice submission · industry-specific flows.

---

## 6. Gaps, risks and blockers

| ID | Item | Severity |
|---|---|---|
| `RT-QB-001` | RED TEAM drafted these questions and cannot certify them. Tester + Odoo Functional must review before freeze. | PROCESS |
| `RT-QB-002` | Thin modules may not reach 40 real module-specific questions. Under Rule ๔ the correct response is a Blocker, not padding. Boss decides per case. | MEDIUM |
| `RT-QB-003` | Q23 and Q24 can establish observed behaviour but not legal correctness. `LEGAL_TAX_REVIEW_REQUIRED` stands. | MEDIUM |
| `RT-QB-004` | Lane A answers from source, Lane B from runtime. Some questions (Q10 concurrency, Q28 cross-boundary) are hard to answer from source alone and will skew toward Lane B. Expected, and should be measured rather than assumed away. | LOW |
| `RT-P3-001` | **WITHDRAWN 2026-09-22 — raised in error.** TECHNOLOGY_STACK_STANDARD v1.0 (Approved Baseline, 2026-07-06) §25 already replaced "Odoo-first" with "Open ERP-first"; §4/§24 mandate FastAPI/Python 3.12; ADR-0006 already ruled "not the Odoo runtime … Concept Match only". No conflict existed. | **WITHDRAWN** |
| `RT-P3-002` | Backend runtime is an open decision, not a conflict — Baseline §24 says FastAPI/Python, ALL TEAM D1 proposes Node.js, study still running. ROOM A output is runtime-neutral (Concept Match only). Architecture Review due before ROOM B build, not before ROOM A study. | DECISION POINT |
| `RT-GOV-001` | Claude Project Instructions §3.1 still reads "Odoo-first", contradicting the Approved Baseline. Every new AI session inherits the stale term. | **HIGH — open, owner Boss** |

---

## 7. Required next action

| # | Action | Owner |
|---|---|---|
| 1 | Review and amend the 35 | Tester + Odoo Functional |
| 2 | Freeze `QUESTION_BANK_STANDARD_35_V1.00` | Boss |
| 3 | Author ≥40 module-specific questions for the first Gxx wave, same schema | Tester + Odoo Functional |
| 4 | Pass every question through `vocab_lint` before it reaches Lane B | CI |
| 5 | Add the CI rule: a question without `DISCONFIRMING_OBSERVATION` is rejected | build team |

---

```text
This output is a draft for independent review only.
It is not Boss Final Approval.
RED TEAM drafted this question bank and therefore cannot certify it.
No question enters production use until Tester and Odoo Functional have reviewed it and
Boss has frozen it.
```
