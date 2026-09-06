# 67 — P05 DOMAIN PURITY AND BOUNDARY REGISTER

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05C-02` · Prompt `SMEPLUS-26-09-06-G01-P05-E2P-DOMAIN-PURE-BOUNDED-CLOSURE-002`
Baseline consumed: `3f50b26859ea4d50b1d8e9095689209c38e0683b`

## 1. The Rule Being Enforced

> **P05 may know what an expense means financially and operationally at the P05 boundary.
> P05 must not learn how the originating external domain works internally.**

`PHASE S = DOMAIN PURITY FIRST.` `AI EOS = NOT ACTIVE.`

## 2. Retrospective Audit — contamination already in the P05 package

This register is not only forward-looking. Prior P05 rounds **did** cross domain boundaries. Each
instance is classified below, the minimum interface fact is retained, and **no adjacent-domain
research was performed in this continuation to resolve any of them.**

| ID | Trigger | Adjacent domain | Why out of P05 functional scope | Minimum P05 boundary fact RETAINED | Handoff needed? | Adjacent research executed here? |
|---|---|---|---|---|---|---|
| `DP-01` | `scgl_advance_expense_request/__manifest__.py` declares `depends: [... "account_asset"]` | **P04 Asset** | Asset lifecycle, capitalisation and depreciation are P04-owned | An employee-advance module *declares* an asset dependency. P05 records the declaration only. **P05 does not know, and did not investigate, why.** | **Yes** — `CH-08` | **NO** |
| `DP-02` | `hr_payroll_expense` — expense reimbursement through payslip | **HR / Payroll** | Payslip construction, payroll runs and salary rules are not P05 | An expense obligation may be settled through a payroll instrument instead of a payment. That is a **settlement route**, not an expense-recognition fact. | **Yes** — `CH-05` | **NO** |
| `DP-03` | `sale_expense` — expense re-invoiced to a customer | **P02 Order-to-Cash** | Customer invoicing, revenue and fulfilment are P02 | An expense may carry a flag marking it re-invoiceable, and a reference to a sales document. P05 owns the flag's presence, not the downstream billing. | **Yes** — `CH-06` | **NO** |
| `DP-04` | Withholding tax rates, PND forms, certificate content, filing periods | **P07 Thailand Tax-to-Compliance** | Statutory interpretation is P07's exclusively | P05 carries WHT *attributes* and produces a withheld-amount event at settlement. **No statutory rule is asserted anywhere in the P05 package** (independently audited, `62`). | **Yes** — `CH-04` | **NO** |
| `DP-05` | `account_disallowed_expenses` — installed on the v18 target | **P07 Tax** | Deductibility and add-back are statutory | The module is **report-only**: no write path to any journal (class A). P05 records that it produces **no P05 accounting effect**. | No | **NO** |
| `DP-06` | Payment registration, outstanding accounts, bank statement matching | **P06 Bank-to-Reconcile** | Settlement execution and bank matching are P06 | P05 hands off a **settlement-ready payable**. P05 does not own the payment instrument, its clearing, or its reconciliation. | **Yes** — `CH-03` | **NO** |
| `DP-07` | Journal entry immutability, hash chains, period locks, force-cancel | **P08 Record-to-Report** | Ledger integrity policy and period architecture are P08 | P05 emits an accounting-relevant event. Whether the ledger permits its later mutation is **P08's control**, not P05's. | **Yes** — `CH-07` | **NO** |
| `DP-08` | Analytic distribution, cost centres, project attribution | **P09 Plan-to-Analyze** | Plan/budget/forecast architecture is P09 | P05 can carry an analytic attribution on the expense debit line and must publish it. Where the dimension *comes from* and what it is *used for* are P09's. | **Yes** — `CH-02` | **NO** |
| `DP-09` | Expenses that plausibly relate to a period rather than an instant (e.g. prepaid, service spanning months) | **P10 Time-Based Recognition** | Deferral schedules, amortisation methods and time grids are P10 | P05 can determine an obligation exists, its amount, counterparty and company. P05 **cannot** decide the recognition profile. This is declared as **not decidable inside immediate Expense-to-Pay semantics**. | **Yes** — `CH-09` | **NO** |
| `DP-10` | Expense descriptions naming machines, equipment, repairs | **P04 Asset/Equipment/Maintenance** | Equipment state, maintenance orders, downtime, routing | The description is a **string on a P05 obligation**. P05 classifies the obligation, not the machine. Canonical example from the prompt §5.3, and P05 conforms. | No | **NO** |
| `DP-11` | Product/category expense-account resolution reaching inventory-valuation accounts | **Inventory / Manufacturing** | Receipt, valuation layers and costing internals | P05 owns the *account resolution chain for an expense line*. It stops at the account. | No | **NO** |
| `DP-12` | **Ownership of the withholding *mechanics* modules** — the package treats them as part of the P05 surface (they are read for the P05-side interface) while P07 owns the statute | **P07** | Added after AAS-03 Expert 3 observed this boundary was applied **consistently but never stated as a rule**. | **Stated rule:** P05 may read a withholding module to establish *what attribute P05 must carry and what event P05 must emit*. P05 may **not** derive from it any statement about what a return requires, what a certificate must contain, or when tax is due. Mechanics are readable; statute is not P05's. | Yes — `CH-04` | **NO** |

**Adjacent-domain deep research executed in this continuation: NONE.** No P04, P06, P07, P08, P09,
P10, P11, Inventory or Manufacturing source, database or register was read.

## 3. Contamination Found and Corrected in This Continuation

| ID | Contamination | Correction |
|---|---|---|
| `DPC-01` | Prior rounds recorded P01/P06/P07/P08/P09 findings as **P05 findings** in `10`, `26`, `34`, `44` before routing them. They were routed, but they were also *counted* inside P05's own registers (e.g. `TZ-08` core-ledger immutability; `TZ-11b` payroll; `E1-15` `sale_expense`). | Those items are **re-labelled `EXTERNAL DOMAIN BOUNDARY`** in `68 §4`. They remain in the lineage; they no longer count as P05-owned closure items. |
| `DPC-02` | `47`/`49` reason about **vendor down-payment accounting semantics** — what the deduction *should* do. That is P01's model. | The evidence is retained; the reasoning about correct behaviour is **withdrawn to a routed question**, already applied at `RE-25`. Re-confirmed here. |
| `DPC-03` | `07 §6` characterises `account_disallowed_expenses` mechanics in some depth. | Bounded: only the **no-GL-write-path** fact is P05-relevant. The percentage/time-slice mechanics are `EXTERNAL DOMAIN BOUNDARY — P07`. |

## 4. Boundary Protection Statements

| Domain | P05 protection statement |
|---|---|
| **P04 Asset/Equipment/Maintenance** | P05 has **not** determined whether any expense should be capitalised. `DP-01`'s asset dependency is recorded as a declaration only. P05 did **not** wait for P04 and did **not** consume P04 output. |
| **P10 Time-Based Recognition** | P05 asserts only that certain obligations are **not fully decidable** within immediate expense semantics. It has produced **no** schedule, method, or period logic. P05 did **not** wait for P10. |
| **P06 Bank-to-Reconcile** | P05 stops at *settlement-ready*. It defines no payment execution or matching semantics. |
| **P07 Tax** | Zero statutory assertions. All nine statutory questions routed (`51`), all class `D`. |
| **P08 Record-to-Report** | P05 emits an accounting-relevant event; ledger integrity policy and period close remain P08's. |
| **P09 Plan-to-Analyze** | P05 publishes an attribution; it defines no dimension architecture. |
| **Inventory / Manufacturing** | Not entered. |

## 5. Parallel-Independence Confirmation

**P04 and P10 are running independently. This continuation did not wait for either, did not consume
either, and did not treat either as a prerequisite.** No P05 closure question below is blocked on
P04 or P10 completion; where their domains touch P05, a Candidate Handoff is recorded instead
(`CH-08`, `CH-09`) — which is the mechanism the prompt prescribes.
