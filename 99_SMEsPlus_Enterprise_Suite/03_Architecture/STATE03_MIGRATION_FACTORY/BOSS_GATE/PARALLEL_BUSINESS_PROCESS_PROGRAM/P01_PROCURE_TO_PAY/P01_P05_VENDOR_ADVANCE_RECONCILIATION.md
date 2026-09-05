# P01 ↔ P05 — VENDOR ADVANCE RECONCILIATION

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.**

P05 Expense-to-Pay records: *"Advance to vendor — P01 owns it … **PEER DEPENDENCY OPEN — P01
must state whether it owns vendor advances.**"*

---

## 1. P01's ANSWER

> **Yes. P01 accepts ownership of the vendor-advance business event.**

Basis:

| Evidence | Class |
|---|---|
| The project's custom vendor-advance capability sits on the purchase capability and is inside P01's transitive module closure | FACT VERIFIED |
| **It is installed in all three readable deployments** — both v19 and the v18 one | **FACT VERIFIED**, class A within those three databases |
| In the base capability, vendor advances are **bill-first**: the down-payment routine has exactly one caller in the whole root, a wizard converting existing vendor-bill lines into down-payment lines on an order. There is no order-side advance wizard in the base | FACT VERIFIED, negative class **A within `R1`** |

The custom module exists precisely because the base shape did not fit: it **adds** the
order-side advance the base lacks.

---

## 2. WHAT THE FINANCIAL EFFECT ACTUALLY IS — AND THE PROBLEM WITH IT

The advance is raised as a vendor bill for a **deposit product**, and that product's expense
account is defaulted from the deposit product's own expense account. The wizard's field is
labelled an **expense** account.

> **A vendor advance is therefore booked, by default, to a profit-and-loss expense account —
> not to a prepayment or advance-to-supplier asset account.**

Classification: **FACT VERIFIED** for the default resolution and the field's role, scope `R4`
and `R5` source. **SUPPORTED INTERPRETATION** for the consequence below — not runtime-confirmed.

**The consequence.** If the advance is expensed on payment and the eventual goods or services
are expensed again on the final vendor bill, the same cost is recognised twice unless the
advance is explicitly netted. The netting relies on a down-payment marker on the order line,
mirroring the base mechanism. **Whether that netting actually occurs was not established** —
`HOLD — RUNTIME EVIDENCE REQUIRED`.

This is a `DOUBLE LIABILITY` / double-cost surface under directive §3.6 and it is **live**,
because the module is installed everywhere.

### Convergence with P05

P05 independently reports that on **its** advance path the disbursement debits a P&L expense
account and that **no advance asset account exists** on that path. Two different advance
mechanisms, two processes, **the same accounting shape**. That makes it a pattern in the custom
layer rather than an isolated defect, and it is the strongest reason to treat it as a design
question rather than a bug report.

---

## 3. THE TWO COPIES BEHAVE DIFFERENTLY

The module ships in two copies, and they are **not** identical where it matters:

| | `R4` (v18 line) | `R5` (v19 line) |
|---|---|---|
| Bill-creation modes offered | includes a "regular bill" mode | that mode is **commented out** |
| Default mode | the regular-bill mode | the **percentage** mode |

Everything else in the module is byte-identical or differs only trivially.

Since the module is installed in **all three** deployments and the copies differ, **the same
business capability offers different options and a different default depending on which
deployment a user is in.** Classification: **FACT VERIFIED** (symmetric file comparison);
**which copy each deployment runs is `DEP-P01-01`**, still open.

---

## 4. THE OWNERSHIP BOUNDARY, STATED FOR P11

| Fact | Owner | Note |
|---|---|---|
| Advance **to a vendor** | **P01** | Answered here |
| Advance **to an employee** | **P05** | P05 owns it; P01 does not touch it |
| The money leaving the bank | **P06** | P06 records advances received before an obligation exists as an *unowned window*; the vendor-side mirror is the same shape |
| Whether an advance is an **asset or an expense** | **Boss / target-design decision** | P01 states only what the reference does. It does not decide the target treatment |
| Withholding on an advance payment | **P07** for the statutory question | Interacts with the compounding finding |

---

## 5. WHAT P01 DOES NOT DECIDE HERE

- Whether the target design should treat a vendor advance as a prepayment asset. That is a
  design decision, and P01 makes no target-architecture decisions.
- P05's employee-advance semantics — those are P05's, and P01 does not adjudicate them.
- Whether the observed expense default is lawful or compliant — no statutory source was
  consulted.

## 6. WHAT REMAINS OPEN

| ID | Item | Status |
|---|---|---|
| `VA-01` | Does the down-payment marker actually net the advance against the final bill? | **HOLD — RUNTIME EVIDENCE REQUIRED** |
| `VA-02` | Which copy of the module each deployment runs | `DEP-P01-01` |
| `VA-03` | Whether any deployment has configured a prepayment asset account instead of the expense default | **PARTIALLY RESOLVED, this session.** In the v19 deployment the deposit-type products carry **no product-level expense account at all** (both matching products, value unset), so the advance resolves to the *category* expense account — i.e. an expense, and certainly not a deliberately-chosen prepayment asset. In the v16 deployment the probe **cannot answer**: that generation stores such values in the generic property store, not as a column, so a column probe is the wrong instrument — **class D, not an absence.** The v18 half stays `HOLD — DATABASE EVIDENCE REQUIRED` |
| `VA-04` | The unowned window P06 describes, on the vendor side | **P11 RECONCILIATION REQUIRED** |
