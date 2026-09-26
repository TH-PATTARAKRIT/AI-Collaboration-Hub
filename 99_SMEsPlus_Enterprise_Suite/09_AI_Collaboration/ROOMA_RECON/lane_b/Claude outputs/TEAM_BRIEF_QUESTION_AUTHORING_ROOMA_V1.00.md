# ROOM A — TEAM BRIEF: WRITING THE QUESTIONS
## For Odoo Core / Functional · Tester / QA · SaaS Foundation

**Version:** V1.00
**Date:** 2026-09-22 · Asia/Bangkok
**Prepared by:** RED TEAM (internal audit)
**Status:** `PREPARED ONLY` — awaiting ALL TEAM veto (`SMEPLUS-26-09-22-019`) and Boss freeze
**Read this before writing a single question.**

---

## 1. What we are actually doing, in five lines

We are studying Odoo 19 Community on a clean server to learn **what an ERP must do** — not to copy
how Odoo does it. Two agents study the same module **blind to each other**: one reads source, one
only observes the running system. A third party compares their answers.

**Your job is to write the questions they both answer.** If the question is good, a disagreement
between the two agents means we found something real. If the question is weak, the disagreement
means nothing and someone wastes a day.

---

## 2. Why the questions must be written *before* anyone starts

The two study agents are deliberately isolated. They cannot agree on what to look at while they
work — that would destroy the independence. So the question list is the only thing that makes
their answers comparable.

```
Team writes questions → questions frozen → Lane A and Lane B answer the SAME numbered
questions, separately → the Reconciler compares cell to cell
```

Once either agent has filed its first answer for a group, **that group's questions cannot change**.
A change invalidates every answer already filed. Write them properly the first time.

---

## 3. Who owns what

### 3.1 Odoo Core / Functional Team — 167 modules
**Groups 3–13** — master data, accounting, inventory, manufacturing, purchase, sales, CRM, events,
project, people.

You write the **module-specific questions** — the ones only someone who has implemented Odoo for
Thai customers would think to ask. You are the only people in this programme who know where real
customers actually get hurt.

Output per module: **≥40 questions.** Modules like `account` and `stock` should have far more —
100+ is expected and welcome. The floor is a floor, not a target.

### 3.2 Tester / QA Team — every question, every group
You own **testability**. A question that cannot fail is not a question.

Two duties:
1. **Review the standard 35** (`QUESTION_BANK_STANDARD_35_V1.00`) and amend it. It was drafted by
   RED TEAM from the Constitution; it has not been reviewed by anyone who writes tests.
2. **Gate every module-specific question** on one rule: does it have a
   `DISCONFIRMING_OBSERVATION` — a concrete result that would prove the expectation wrong? If not,
   reject it back to the author. CI enforces the same rule, but you catch it first and cheaper.

You also own the **negative paths**. Functional teams naturally write "what does it do"; testers
write "what happens when it goes wrong". The second set is where the findings are.

### 3.3 SaaS Foundation Team — 52 modules
**Groups 1, 2, 16** — platform base, identity and access, technical integration.

⚠️ **Your work is different from the other two teams.** SaaS Foundation is already designed
(ADR-0002 Multi-Tenant, ADR-0006 RBAC/ABAC/RLS). We are **not** rebuilding it from Odoo.

Your question is never *"what should we build?"* — it is:

> **"Odoo handles this situation somehow. Does our Foundation say what happens in that
> situation? If not, that is a gap in our design."**

Output: **GAP statements in business language.**
You may **not** output data structures, field names, API shapes, or hierarchy designs taken from
Odoo. The recipient is the Foundation Architect, not the ROOM B builder.

---

## 4. The rules every question must satisfy

| # | Rule |
|---|---|
| 1 | **35 standard questions** are answered for every module, without exception. No module is "too small". |
| 2 | **≥40 module-specific questions** per module. Combined floor: **≥75 answered per module.** |
| 3 | **No padding.** A question exists to test a hypothesis, never to reach a count. |
| 4 | **Every question carries a `DISCONFIRMING_OBSERVATION`.** No disconfirming observation → CI rejects it. |
| 5 | **No Odoo technical vocabulary in the question text.** No model names, no field names, no module names. A lint blocks them before they reach the observing agent. |
| 6 | **Cannot reach 40 real questions for a module?** Raise a Blocker for Boss. Do not invent 40. |

### Why rule 5 exists

One agent is blind to source on purpose. If your question says *"check `period_lock_date` on
`res.company`"*, you have just told it the answer and the independence is gone. Write the same
question behaviourally:

> *"Can an entry be recorded into an accounting period that has already been closed? If it is
> prevented, where is that configured, and who can change it?"*

Same question. No leak.

---

## 5. Question record — copy this template

```yaml
QID:            G04-STOCK-Q17          # group-module-sequence
MODULE:         stock
TYPE:           MODULE                 # STANDARD | MODULE
AUTHOR:         <your name / team>
RISK_TIER:      CRITICAL | HIGH | NORMAL

HYPOTHESIS: >
  What you expect the system to do, in business language.

WHY_IT_MATTERS: >
  What goes wrong in a real customer's business if this is not true.
  Statutory, financial, or data-isolation consequence if there is one.

DISCONFIRMING_OBSERVATION: >            # ← mandatory. CI rejects without it.
  The concrete result that would prove the hypothesis false.

EXPECTED_SURFACE: S1, S6                # where you expect it to be observable
PRECONDITIONS: >
  Settings or data that must be true first.
```

**Observation surfaces**

| ID | Surface |
|---|---|
| S1 | Walking the screens |
| S2 | Field metadata |
| S3 | Database structure |
| S4 | Access rules |
| S5 | Scheduled jobs |
| S6 | **Doing a real transaction and reading what changed** — the most valuable |

---

## 6. What a good question looks like — and a bad one

### ✅ Good — Functional Team

```yaml
QID: G10-ACCOUNT-Q41
HYPOTHESIS: >
  A payment recorded against a customer invoice in a foreign currency posts an exchange
  difference at the payment date, not the invoice date.
WHY_IT_MATTERS: >
  If it uses the invoice date, the gain or loss lands in the wrong period and the
  filed financial statement is wrong.
DISCONFIRMING_OBSERVATION: >
  The exchange difference entry carries the invoice date, or no difference is posted at all.
EXPECTED_SURFACE: S6
```

### ✅ Good — Tester / QA

```yaml
QID: G05-STOCK-Q23
HYPOTHESIS: >
  Confirming a delivery for more than the quantity on hand is blocked, and the message
  names the shortfall.
WHY_IT_MATTERS: >
  Silent negative stock destroys inventory valuation and nobody notices for months.
DISCONFIRMING_OBSERVATION: >
  The delivery confirms and quantity on hand becomes negative, with no warning and no record
  of who allowed it.
EXPECTED_SURFACE: S1, S6
```

### ✅ Good — SaaS Foundation

```yaml
QID: G02-IDENTITY-Q08
HYPOTHESIS: >
  When a user's session expires while an approval is half-completed, the approval does not
  take effect and the document returns to its previous state.
WHY_IT_MATTERS: >
  Our Foundation defines session lifetime and it defines approval workflow, but it does not
  state what happens when the two collide.
DISCONFIRMING_OBSERVATION: >
  The approval takes effect anyway, or the document is left in a state that is neither
  approved nor pending.
EXPECTED_SURFACE: S1
OUTPUT: GAP STATEMENT to Foundation Architect
```

### ❌ Bad — and why

```yaml
"Does this module work correctly?"
   → cannot fail. No disconfirming observation exists.

"Check the account_move_line table for the analytic_distribution field."
   → technical vocabulary. Leaks the answer to the blind agent. Lint blocks it.

"What are the menus in this module?"
   → tests nothing. This is a padding question to reach 40.

"Is the code well written?"
   → not observable at runtime. Out of scope for this study.
```

---

## 7. Study sequence — write the questions for a group just before that group starts

Boss's rule: **do not write all 12,000 questions up front.** Write one group's questions, hand them
over, and start. Write the next group while the previous one is being studied.

| Wave | Group | Modules | Questions to author | Owner |
|---:|---|---:|---:|---|
| **1** | 01 PLATFORM_BASE | 21 | ~840 | **SaaS** |
| **2** | 02 IDENTITY_ACCESS | 11 | ~440 | **SaaS** |
| **3** | 03 MASTER_DATA + 04 ACCOUNT_BASE | 20 | ~800 | **Functional + QA** |
| **4** | 05 INVENTORY + 10 ACCOUNT_PROCESS | 27 | ~1,080 | **Functional + QA** |
| **5** | 07 PURCHASE + 08 SALES + 09 CRM | 51 | ~2,040 | **Functional + QA** |
| **6** | 06 MANUFACTURING + 11 EVENTS | 20 | ~800 | **Functional + QA** |
| **7** | 12 PROJECT + 13 PEOPLE | 49 | ~1,960 | **Functional + QA** |
| **8** | 14 COLLABORATION + 15 DASHBOARD | 27 | ~1,080 | Functional + QA |
| **9** | 16 TECHNICAL_INTEGRATION | 20 | ~800 | **SaaS** |
| **10** | 17 WEBSITE + 18 THEME + 19 COSMETIC | 53 | ~2,120 | **on hold — pending T6** |

### Two sequencing rules that are not negotiable

**Wave 3 must be done as one unit.** Accounting is embedded in master data — `product.template`
carries income and expense accounts, `product.category` carries stock valuation accounts,
`res.partner` carries receivable and payable, `res.company` carries 38 account fields. Studying
products without the accounts attached to them produces an incomplete answer.

**Wave 4 must be done as one unit.** The inventory-to-accounting bridge — goods moved in one
period, cost recognised in another — is where the largest ERP errors live. It cannot be tested if
inventory and accounting are studied in different waves.

---

## 8. Before a group's questions are frozen — checklist

- [ ] Every module in the group has ≥40 module-specific questions, or a raised Blocker explaining why not
- [ ] Every question has a `DISCONFIRMING_OBSERVATION` that names a concrete failing result
- [ ] No question contains an Odoo model name, field name, or module name
- [ ] Negative paths are present, not only happy paths (QA sign-off)
- [ ] Questions that touch Thai statutory matters are flagged `LEGAL_TAX_REVIEW_REQUIRED`
- [ ] Questions that touch tenant, company or branch boundaries are flagged `CRITICAL`
- [ ] QA has reviewed for testability
- [ ] Boss has frozen the set

**After freeze: no changes.** A change invalidates every answer already filed against it.

---

## 9. The five findings behind this plan

Everything above rests on measurements taken from the live instance on 2026-09-22, not on opinion.

| # | Finding |
|---|---|
| 1 | Product is base — referenced by 113 modules (38%) against `sale` 50 (17%) |
| 2 | Accounting is embedded in master data — `product.template` 6 account fields, `product.category` 7, `res.partner` 6, `res.company` 38 |
| 3 | `account` has two layers — chart, tax and periods are referenced by a third of the system; invoice and payment lifecycle are not |
| 4 | Theme is a pure leaf — nothing in the system depends on it |
| 5 | The real core models hide inside `base` — `res.users` touched by 74 modules, `res.partner` 51, `res.company` 46 |

---

## 10. What to send back, and to whom

| Team | Deliverable | Format | To |
|---|---|---|---|
| Functional | Module-specific questions per module | the YAML template in §5 | QA first, then freeze |
| QA | Amended standard 35 + testability sign-off | same | Boss for freeze |
| SaaS | Questions + GAP statements | same, marked `OUTPUT: GAP STATEMENT` | Foundation Architect |

Questions go into the repository per group, one file per module, before that group's study begins.

---

```text
This brief is PREPARED ONLY. It is not Boss Final Approval.
It depends on ALL TEAM accepting SMEPLUS-26-09-22-019 and on Boss freezing the question bank.
RED TEAM drafted the standard 35 and this brief, and cannot certify either.
RT-P3-001 was WITHDRAWN 2026-09-22 — raised in error by RED TEAM; no Odoo-first conflict existed.
The backend runtime (FastAPI/Python per Approved Baseline, vs Node.js per ALL TEAM D1) is an open
decision, not a blocker: this study's output is Concept Match only and is runtime-neutral.
```
