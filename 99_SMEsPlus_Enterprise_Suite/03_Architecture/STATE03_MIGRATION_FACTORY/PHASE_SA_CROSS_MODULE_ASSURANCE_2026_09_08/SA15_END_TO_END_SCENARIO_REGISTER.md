# SA15 — END-TO-END SCENARIO REGISTER

Status: **HOLD** — 15 mandated scenarios plus 3 added; 6 traversable end-to-end on current evidence.
Governing law: master prompt §12.

---

## 1. Traversability classification

| Class | Meaning |
|---|---|
| `TRAVERSABLE` | Every hop has an evidenced producer, consumer and compatible interface |
| `TRAVERSABLE WITH NAMED BREAK` | The spine is evidenced; one or more named hops carry an open item |
| `NOT TRAVERSABLE` | At least one hop cannot be routed at all on current evidence |

A scenario is not called traversable because its *shape* is drawable. It is called traversable
when every hop in it appears in `SA04`'s evidenced set.

---

## 2. Mandated scenarios

| ID | Scenario | Class | Breaks / blockers |
|---|---|---|---|
| E2E-01 | Customer → Sales → Stock → Delivery → AR → Payment → Bank → Accounting | `TRAVERSABLE WITH NAMED BREAK` | commercial entry (SA-D21) unevidenced; cancellation gate `XD-01` |
| E2E-02 | Purchase demand → Purchase → Receipt → AP → Payment → Bank → Accounting | `TRAVERSABLE` | approval internal logic open (A2) but the flow routes |
| E2E-03 | Sales → Manufacture → RM → Production → FG → Delivery → AR → Accounting | `TRAVERSABLE WITH NAMED BREAK` | BOM/routing semantics thin; fixed-overhead injection path (R-22) |
| E2E-04 | Sales → Manufacture → RM shortage → Purchase → Receipt → Production → Delivery → Accounting | **`NOT TRAVERSABLE`** | shortage→purchase trigger undetermined (BN-04, TVDR-01) |
| E2E-05 | Sales → Dropship → Purchase → Vendor-to-customer → AR/AP → Accounting | **`NOT TRAVERSABLE`** | BN-05 `HOLD`; inventory event for title passage undetermined (IR-13); control bypass `SA03-F-02` |
| E2E-06 | Sales → MTO/Buy → Purchase → Receipt → Delivery → Accounting | `TRAVERSABLE WITH NAMED BREAK` | order→purchase linkage and its reservation semantics unevidenced (BN-06) |
| E2E-07 | Sales → Kit → Component inventory → Delivery → Accounting | **`NOT TRAVERSABLE`** | component resolution point and costing level undetermined (BN-07, IR-12, AR-25) |
| E2E-08 | Service → Delivery/completion evidence → AR → Payment → Accounting | **`NOT TRAVERSABLE`** | completion evidence undetermined (BN-08, AR-26, TVDR-02) |
| E2E-09 | Purchase → Asset capitalization → Depreciation → Accounting | `TRAVERSABLE WITH NAMED BREAK` | derecognition defect (AR-17); Equipment side thin |
| E2E-10 | Expense → Approval → Payable/Payment → Accounting | `TRAVERSABLE WITH NAMED BREAK` | P05 terminal HOLD (AR-18) |
| E2E-11 | Sales return → Inventory return → Credit/reversal → Accounting | `TRAVERSABLE` | return is the most fully evidenced area in the corpus |
| E2E-12 | Purchase return → Inventory return → Debit/reversal → Accounting | `TRAVERSABLE` | structurally identical |
| E2E-13 | Manufacturing scrap / by-product / variance → Inventory → Accounting | `TRAVERSABLE WITH NAMED BREAK` | by-product valuation open (IR-08, AR-12) |
| E2E-14 | Month close → Inventory valuation → AR/AP → Bank → Tax → GL → Financial reporting | `TRAVERSABLE WITH NAMED BREAK` | AR-20 close, AR-21 analytic, AR-22 tax all `PARTIAL` against recorded Phase S terminal states |
| E2E-15 | Correction / reversal / retry / duplicate event | `TRAVERSABLE` | strongest area: idempotency and ordering-independence established (`SA09`) |

## 3. Scenarios added by this register (master prompt §12 requires automatic addition)

| ID | Scenario | Why added | Class |
|---|---|---|---|
| **E2E-16** | Quality inspection → hold/release/reject → Inventory availability → cost recognition timing | Boss ruled the Quality boundary (`4c469f8e`); a quality hold sits on the accounting path, not beside it | **`NOT TRAVERSABLE`** |
| **E2E-17** | Manufacturing work order → equipment breakdown → maintenance order → completion → work order resumes | The route is stated verbatim in Boss decision `a11c9e7b` §3, so it is an approved flow with no assurance | **`NOT TRAVERSABLE`** |
| **E2E-18** | Project → operational progress → source facts (Sales/Purchase/Inventory/Timesheet) → analytic dimension → derived project financial view | Boss ruled the Project ↔ Analytic boundary (`fa57d10f`) including *"Project dashboards must not create duplicate financial truth"* | **`NOT TRAVERSABLE`** |

## 4. Traversability summary

Counted by enumerating the identifiers in each class, not by asserting a total.

| Class | Scenarios (enumerated) | Count |
|---|---|---|
| `TRAVERSABLE` | E2E-02, E2E-11, E2E-12, E2E-15 | 4 |
| `TRAVERSABLE WITH NAMED BREAK` | E2E-01, E2E-03, E2E-06, E2E-09, E2E-10, E2E-13, E2E-14 | 7 |
| `NOT TRAVERSABLE` | E2E-04, E2E-05, E2E-07, E2E-08, E2E-16, E2E-17, E2E-18 | 7 |
| **Total** | 15 mandated + 3 added | **18** |

Check: 4 + 7 + 7 = 18, and every identifier E2E-01…E2E-18 appears exactly once above.

## 5. SA15-F-01 — the four fully traversable scenarios are all corrections, returns or receipts

E2E-02 purchase-to-pay, E2E-11 sales return, E2E-12 purchase return and E2E-15
correction/reversal/retry are the only end-to-end flows that traverse without a named break.

Every one of them is a flow that **undoes or receives**. Not one of the fully traversable
scenarios is a *forward sale to a customer*. E2E-01, the simplest and most common transaction
an SME performs, carries two named breaks.

**This is the single most important sentence in this register:** SMEsPlus can currently prove
end-to-end that it can receive goods, return goods and reverse mistakes. It cannot yet prove
end-to-end that it can sell something.

## 6. SA15-F-02 — the three added scenarios are all Boss-approved routes with no assurance behind them

E2E-16, E2E-17 and E2E-18 exist because Boss has already ruled on their boundaries. E2E-17's
route is written out step by step inside the Boss decision itself.

A ruled boundary with no assured flow is a specific and avoidable risk: the decision is
correct, and there is nothing yet that can be tested against it. Raised here so that Boss is
not the first detector.

## 7. Handoff to Pre-Test Matrix

This register does **not** execute the Pre-Test Matrix (master prompt §21). Scenario priority
for the next phase is carried to `SA17`, ordered by the principle that a scenario the business
performs daily and cannot traverse ranks above a scenario it performs rarely and can.

---

`SA15 — HOLD`. Four of eighteen end-to-end scenarios traverse without a named break; seven
cannot be traversed at all.

Boss remains the sole Final Approver.
