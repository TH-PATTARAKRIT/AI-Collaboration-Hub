# P10 — DEFERRED EXPENSE TRACE

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1 · **DELTA-FIRST**

This trace is written as a **delta against `02_P10_DEFERRED_REVENUE_TRACE.md`**. Everything not listed below is identical, and identical *by construction* — the two directions are the same code with a direction switch (`E-P10-003`), not two implementations. That fact is itself a finding: see §6.

---

## 1. What Is Genuinely Different

| # | Aspect | Deferred revenue | Deferred expense | Evidence |
|---|--------|------------------|------------------|----------|
| `D1` | Source document direction | Customer invoice | Vendor bill | `E-P10-003` |
| `D2` | Eligible account types | income, other income | expense, cost of goods sold, depreciation expense | `E-P10-017` |
| `D3` | Counterpart account | deferred revenue (liability) | deferred expense / prepayment (asset) | `E-P10-018` |
| `D4` | Journal | deferred revenue journal | deferred expense journal | `E-P10-018` |
| `D5` | Generation method setting | independent setting | independent setting | `E-P10-018` |
| `D6` | Allocation rule setting | independent setting | independent setting | `E-P10-018` |
| `D7` | Report surface | deferred revenue report | deferred expense report | `E-P10-043` |

## 2. The Consequence Nobody Expects — `P10-F-17`

`D5` and `D6` are **independent per direction**. A company may therefore be configured to recognise revenue on a 30/360 basis at source-document validation, and expense on an actual-day basis by monthly grouping — or any of the other eleven combinations.

For a matched pair — a service resold at a margin, where the purchased service and the sold service cover the *same window* — the two sides of the margin are then allocated by different rules onto different journal shapes. The monthly margin reported is an artefact of configuration, and it re-converges only at the end of the window.

Nothing in the reference product warns about, detects, or prevents an asymmetric pair. Classification: `VERIFIED FACT` that the settings are independent (`E-P10-018`); `INFERENCE` for the margin distortion, which is arithmetic on that fact and is reproducible on paper but has not been reproduced at runtime in this session.

**This is the single strongest argument found in this session for a shared allocation kernel with a policy layer** (Option B), because under Option A nothing structurally prevents the pair from diverging, whereas a kernel can carry a "matched window" constraint. It is recorded as an input to the decision, not as the decision.

## 3. Prepayment

The reference product has **no separate prepayment concept**. A prepaid expense is a deferred expense whose deferral account happens to be an asset. There is no prepayment object, no prepayment report, and no distinction between "prepaid" (cash paid in advance) and "deferred" (cost incurred in advance of benefit). Class: this is a `VERIFIED ABSENCE` **within reference root `RR-1`, searched by the mechanism enumeration `P10_ENUM_02`** — see `NC-07` for the boundary statement. It is not a claim that no ERP distinguishes them.

For SMEsPlus this matters because Thai practice commonly separates ค่าใช้จ่ายจ่ายล่วงหน้า (prepaid expense, an asset arising from payment) from ค่าใช้จ่ายรอตัดบัญชี (deferred charge, an asset arising from incurrence). Whether SMEsPlus must present them separately is a **statutory presentation question routed to the Accounting-Tax track**, marked `HOLD / EVIDENCE REQUIRED` — see `11_P10_CONTRADICTION_REGISTER.md` `P10-C-05`.

## 4. Accrued vs Deferred on the Expense Side

The two are implemented by different mechanisms with no relationship (`M1` vs `M2` in `01` §4). A vendor bill received late is handled by the accrual wizard; the same cost, if billed in advance, is handled by the deferral fields. **The same expense, recognised over the same period, is therefore modelled by two unrelated mechanisms depending only on the timing of the vendor's invoice.**

For the Boss's `ONE ECONOMIC FACT -> ONE RECOGNITION EVENT PATH` rule this is the deepest violation found: it is not two paths for one fact, it is two *models* for one fact, and they are not reconcilable to each other by any stored link.

## 5. Everything Else

Identical to `02`, including: the monthly-only grid (`P10-F-12`), the absent event identity (`P10-F-07`), the silent lock re-dating (`P10-F-05`), the currency-free recognition lines (`P10-F-04`), the two-path divergence (`P10-F-06`), the account-change block as the only in-flight guard, and the absence of a catch-up path.

## 6. The Finding That the Symmetry Itself Produces

Because deferred revenue and deferred expense are the same code, **every defect in this package is a paired defect**. There is no case where the revenue side is protected and the expense side is not. That is favourable for remediation cost and unfavourable for risk concentration: a single defect in the allocation rule affects both sides of the income statement simultaneously and in the same direction, so the *net* effect on profit can be small while both gross figures are wrong. Detection by margin analysis is therefore unreliable, in exactly the way the prior Asset round found that annual reconciliation could not detect a wrong day convention.

## 7. Scope Determination (`REV2-CORR1`)

Identical to `02` §10 in every row. The direction switch does not change scope ownership: both are COMPANY-scoped financial effects whose allocation rule is currently resolved at the executing scope rather than the owning scope (`P10-F-02`).
