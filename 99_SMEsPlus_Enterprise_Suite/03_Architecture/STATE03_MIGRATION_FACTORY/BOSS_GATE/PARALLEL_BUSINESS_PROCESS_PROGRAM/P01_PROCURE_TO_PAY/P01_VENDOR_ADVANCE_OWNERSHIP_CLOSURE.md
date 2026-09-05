# P01 — VENDOR ADVANCE OWNERSHIP CLOSURE

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.**

P01 accepted ownership of the vendor-advance event in the prior round. The directive requires
more than recording the acceptance: **trace the actual accounting and event model.** This does
that, and finds a defect.

---

## 1. THE EVENT MODEL, TRACED

| # | Business event | Document | Accounting effect |
|---|---|---|---|
| 1 | An advance is agreed | a down-payment line is added to the purchase order, flagged as such, with a section header | **none** |
| 2 | The advance is billed | a **vendor bill** for a deposit product | **Dr expense account · Cr accounts payable** |
| 3 | The advance is paid | payment | Dr payable · Cr outstanding payments |
| 4 | Goods or services arrive | receipt | per the receipt rules of the series |
| 5 | The final bill is raised | vendor bill for the order | **Dr expense/inventory · Cr payable — for the FULL order amount** |
| 6 | The advance is deducted from the final bill | **intended, and does not happen — see §3** | — |

## 2. THE ACCOUNT — THE ADVANCE IS AN EXPENSE, NOT AN ASSET

The deposit product's expense account is used, defaulted from the product's own expense account,
and the wizard field is itself labelled an **expense** account.

> **A vendor advance is booked to profit and loss on payment. There is no advance-to-supplier
> asset.**

Classification: **FACT VERIFIED** (custom source, both copies).
Deployed check: in the series-19 estate the deposit-type products carry **no product-level
expense account**, so resolution falls to the category expense account — still an expense.
In the series-16 deployment the probe **cannot answer** (that series stores such values
elsewhere) — **class D, not an absence.**

Convergence: peer **P05** independently found the same shape on its own advance path — a
profit-and-loss debit with no advance asset account. **Two mechanisms, two processes, one
accounting shape.** That makes it a pattern in the custom layer, not an isolated defect.

---

## 3. THE DEFECT — THE DEDUCTION CONTROL IS INERT

> **`Deduct down payments` is a visible checkbox, defaulted ON, that does nothing.**

Verified across both shipped copies:

| Evidence | Count |
|---|---|
| Declared as a Boolean field with **`default=True`** | 1 |
| Rendered in the wizard view, with a label the user reads | **3 view references** |
| Referenced in executable code | **0** |
| Referenced in **commented-out** code | **1** — the single line that would have passed it into bill creation |

The live code path calls the ordinary bill-creation action **with no deduction argument at all**.

- **POPULATION:** every reference to the control's identifier in the module.
- **PATTERN:** recursive text search for the identifier across the module, both copies.
- **PATH SET:** both custom roots.
- **RESULT:** 5 references per copy — 1 field declaration, 3 view, 1 commented-out.
- **FALSE-NEGATIVE MODES:** dynamic attribute access would not be matched; a deduction performed
  elsewhere under a different name would not be matched. **Class B, not A**, for "no deduction
  happens anywhere" — §5 states what would settle it.

Classification: **FACT VERIFIED** that the control is not wired.
**SUPPORTED INTERPRETATION** that the consequence is double recognition.

### Consequence

Step 2 recognises the cost when the advance is billed. Step 5 recognises the **full** order
amount again. Nothing subtracts step 2 from step 5.

> **The same cost is recognised twice, and the control the user believes prevents it is inert
> and defaulted on.**

---

## 4. THE REACHABILITY QUALIFIER — AND IT MATTERS

The inert deduction sits inside the branch for the **"regular bill"** creation method.

In the **series-19-line copy**, that method is **commented out of the selection list** and the
default is the percentage method. So on that copy the branch is **not reachable through the
user interface**, though it remains reachable programmatically.

| Copy | "Regular bill" option | Double-recognition branch |
|---|---|---|
| series-18-line | present, and the **default** | **reachable through the interface** |
| series-19-line | **commented out** | **not reachable through the interface**; reachable by other means |

**Which copy each deployment runs is `DEP-P01-01`, still open.** So the *severity* of this
defect is deployment-dependent even though the *defect* is present in both copies.

This is the reachability discipline applied to P01's own new finding: a defect that cannot be
reached through the interface is not the same risk as one that is the default path.

---

## 5. WHAT WOULD SETTLE IT

| ID | Question | Status |
|---|---|---|
| `VA-05` | Does any other code deduct the advance from the final bill? | **class B** — a search of this module only. Would be settled by a whole-root search for the deduction behaviour under any name |
| `VA-06` | Which copy each deployment runs | `DEP-P01-01` |
| `VA-07` | Whether double recognition actually occurs | **HOLD — RUNTIME EVIDENCE REQUIRED.** One advance, one final bill, one ledger read |
| `VA-08` | Whether any deployment configured an advance **asset** account | series-19: no product-level account set. Series-16: **class D** |

---

## 6. OWNERSHIP, STATED FOR P11

| Fact | Owner |
|---|---|
| Advance **to a vendor** | **P01** — accepted, and now traced rather than merely accepted |
| Advance **to an employee** | **P05** — P01 does not touch it |
| The money movement itself | **P06** — which records the pre-obligation window as unowned |
| Whether an advance is an **asset or an expense** | **Boss / target design.** P01 states only what the reference does |
| Withholding on an advance payment | **P07** for the statutory question |

**P01 makes no target-architecture decision here**, and does not adjudicate P05's or P06's
semantics.

---

## 7. STATUS

| Item | Status |
|---|---|
| Ownership | **CLOSED — P01 owns the vendor-advance event** |
| Event model | **TRACED** — six steps, step 6 does not occur |
| Accounting treatment | **expense, not asset** — FACT VERIFIED in source |
| Deduction control | **INERT — FACT VERIFIED** |
| Double recognition | **SUPPORTED INTERPRETATION** — `HOLD — RUNTIME EVIDENCE REQUIRED` |
| Severity | **deployment-dependent** on which copy is installed |
