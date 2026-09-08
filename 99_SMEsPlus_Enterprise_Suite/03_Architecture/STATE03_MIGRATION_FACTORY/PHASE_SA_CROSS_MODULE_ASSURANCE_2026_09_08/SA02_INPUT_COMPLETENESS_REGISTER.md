# SA02 — INPUT COMPLETENESS REGISTER
## CP-SA-20 — INPUT COMPLETENESS

Status: **HOLD** — inputs mapped for evidenced domains; six domains cannot supply an input register.
Governing law: master prompt §3.

---

## 1. Status vocabulary (master prompt §3)

`INPUT-COMPLETE` · `INPUT-GAP` · `INPUT-CONTRADICTION` · `INPUT-EVIDENCE-INSUFFICIENT`

No unsupported assumption is classified complete. Where Phase S recorded a *negative* — a
gate that does not exist — that negative is itself an input fact and is recorded as such,
not as a gap.

---

## 2. SA-D01 Sales — input register

Evidence: `claude/group-a-sales-inventory-purchase-dr002` @ `8b0993d8`, Sales capability model
and business-fact ownership matrix; `research/account-p02-order-to-cash-2026-09-04-001` for the AR side.

| Input | Owner (authoritative) | Mandatory | Status | Note |
|---|---|---|---|---|
| Ordered quantity | Sales — pure user input, never derived | Yes | `INPUT-COMPLETE` | Recorded as a commercial-intent fact owned solely by Sales |
| Product identity on every real line | Product master | Yes | `INPUT-COMPLETE` | Evidenced as the only structural confirmation gate besides commitment state |
| Per-product billing basis (bill on order vs on fulfilment) | Product master (read-only to Sales) | Yes | `INPUT-COMPLETE` | Drives billable-now quantity |
| Customer credit limit | Customer master | No | `INPUT-COMPLETE` **as a negative** | Evidence records it as **advisory only, never a gate**. This is a determined fact, not a missing control — but see SA02-F-01 |
| Stock availability at confirmation | Inventory | No | `INPUT-COMPLETE` **as a negative** | Evidence records confirmation is **not gated** by availability |
| Fulfilment quantities | Inventory (read back) | Yes | `INPUT-COMPLETE` | Sales never writes physical-movement facts |
| Already-billed quantity | Accounting (read backward) | Yes | `INPUT-COMPLETE` | Declared a round-trip dependency |
| Company / accessible-branch context | Organization master | Yes | `INPUT-COMPLETE` | Same accessible-branch check on both commercial sides |
| Price determination inputs | — | Yes | **`INPUT-EVIDENCE-INSUFFICIENT`** | SA-D21 thin (18 blobs). What determines price is not evidenced |
| Supply Nature of the line | — | Yes | **`INPUT-EVIDENCE-INSUFFICIENT`** | `SA05-F-02`: the resolution rule is undetermined |
| Accounting state that should block cancellation | Accounting / AR | Yes | **`INPUT-CONTRADICTION`** | See §6 — Group A A1 |

### SA02-F-01 — two advisory-only inputs on the sell side, both hard on the buy side

Credit limit and stock availability are **advisory** at sell-side confirmation. The buy side
carries a **hard, test-confirmed** amount-threshold approval gate. The same evidence records
that the sell side has no equivalent hard commercial gate.

This is not presented as a defect to fix by symmetry. It is an **input completeness fact with a
design consequence**: SMEsPlus must decide deliberately whether a commercial commitment can be
made that the business cannot fund or fulfil. Carried to `SA13`/`SA19` as a design position,
not silently inherited.

---

## 3. SA-D02 Purchase — input register

| Input | Owner | Mandatory | Status | Note |
|---|---|---|---|---|
| Ordered quantity | Purchase — user input | Yes | `INPUT-COMPLETE` | |
| Product identity on every real line | Product master | Yes | `INPUT-COMPLETE` | Only structural confirmation gate |
| Commitment total value + configured threshold + approver group membership | Organization / policy | Yes | `INPUT-COMPLETE` | The real hard approval gate; test-confirmed |
| Per-product billing basis (on ordered vs on received) | Product master | Yes | `INPUT-COMPLETE` | Payables-side equivalent of the sell-side policy |
| Vendor supply terms | Vendor master | Yes | `INPUT-COMPLETE` | Purchase carries **no price list**; it uses vendor supply records |
| Approved internal demand signal | Demand request | Yes | `INPUT-COMPLETE` | Hard gate: conversion blocked unless demand is approved |
| Receipt quantities | Inventory (read back, completed movements only) | Yes | `INPUT-COMPLETE` | |
| Already-billed quantity | Accounting (read backward) | Yes | `INPUT-COMPLETE` | |
| Approval workflow internal logic | three identified approval modules | Yes | **`INPUT-EVIDENCE-INSUFFICIENT`** | Group A **A2**, status `EVIDENCE MISSING / BOSS DECISION REQUIRED` |

### SA02-F-02 — an approval input whose recording half was never exercised

Group A evidence records that on the buy-side commitment, approver **assignment** is populated
on 98.5% of rows while the fields recording that approval **actually happened** are populated
on **zero of 27,874 rows**.

For Phase SA this is an input-completeness statement of the strongest kind: *the fact that an
approval occurred* has never been captured in the evidenced estate. An approval control whose
evidence half is unexercised cannot be assumed to produce audit evidence in SMEsPlus.

Routed to `SA11` (audit evidence requirement) and `SA13` (SoD).

---

## 4. SA-D03 Inventory — input register

| Input | Owner | Mandatory | Status |
|---|---|---|---|
| Fulfilment demand from the sell side (arrives **indirectly**, via the rule engine) | Sales | Yes | `INPUT-COMPLETE` |
| Receipt expectation from the buy side (arrives **directly and synchronously**) | Purchase | Yes | `INPUT-COMPLETE` |
| Planned quantity + source / intermediate / final destination (three distinct location concepts) | Inventory | Yes | `INPUT-COMPLETE` |
| Warehouse, location, unit of measure, product master | Master data | Yes | `INPUT-COMPLETE` |
| Per-transfer-type remaining-supply policy (ask / always / never) | Policy | Yes | `INPUT-COMPLETE` |
| Replenishment thresholds per product + location, plus scheduler trigger | Policy | Yes | `INPUT-COMPLETE` |
| Human execution of the transfer | Operator | Yes | `INPUT-COMPLETE` |
| Quality inspection outcome | Quality | Conditional | **`INPUT-EVIDENCE-INSUFFICIENT`** | SA-D19 thin |

### SA02-F-03 — the two demand paths into Inventory are structurally different

Sell-side demand reaches Inventory **indirectly**, through a procurement rule engine. Buy-side
expectation reaches Inventory **directly and synchronously**. Both are evidenced; the asymmetry
is real, not an artefact.

Consequence for SMEsPlus: an inventory event's **latency and failure mode differ by origin**.
A synchronous creation fails with its parent transaction; an indirect creation may not. Any
SMEsPlus contract stating "a confirmed commitment produces a movement" is true on one side and
eventually-true on the other. Carried to `SA04` and `SA09`.

---

## 5. SA-D06 Accounting Event — input register

| Input | Owner | Mandatory | Status |
|---|---|---|---|
| Business fact from the source module | Source module (BD-ACC-01) | Yes | `INPUT-COMPLETE` |
| Canonical Accounting Event Identity | Accounting Core (BD-ACC-01) | Yes | `INPUT-COMPLETE` |
| Billable-now quantity | Sales / Purchase | Yes | `INPUT-COMPLETE` |
| Tax determination | shared tax engine — **neither commercial module computes tax itself** | Yes | `INPUT-COMPLETE` |
| Tax substitution (fiscal position) rule base | — | Yes | **`INPUT-EVIDENCE-INSUFFICIENT`** | Group A open item #4, recorded as *a black box in this evidence set* |
| Inventory valuation / costing policy | Product Category (BD-ACC-03A/03B) | Yes | `INPUT-COMPLETE` |
| Cost element inputs for manufactured goods | Manufacturing | Partly | `INPUT-GAP` | P03 records fixed-overhead elements with no injection path |

---

## 6. SA02-F-04 — the one `INPUT-CONTRADICTION` in the register

**Subject.** What accounting fact, if any, must block cancellation of a sell-side commitment.

**The contradiction.** The buy-side commitment carries a *dual* cancellation gate — commercially
frozen **OR** an outstanding supplier billing document exists. The sell-side commitment carries
a *single* gate — commercially frozen only. Group A designed the asymmetry deliberately and
then declined to invent the missing half, recording verbatim:

> `HOLD — WAITING FOR ACCOUNTING/AR-AP AUTHORITY`

and stating what it would not invent: *"the AR/customer-invoice internal lifecycle … any
posted/locked/reconciled semantics; which specific Accounting fact, if any, should hard-block
Sales-side cancellation."*

**The three questions Group A asked Accounting**, verbatim from
`claude/team-b-group-a-sip-nonacct-corr-010` @ `e4418644`,
`.../TEAM_B_DESIGN/GROUP_A_SALES_INVENTORY_PURCHASE/CORRECTIVE_CORR_010/34_CORR010_ACCOUNTING_HOLD_AND_RESIDUAL_DEPENDENCY_MATRIX.md`
§ *A1 — Sales-Side Cancellation-Gate Symmetry (Accounting/AR-AP Dependency)*
(byte-identical blob on the terminal branch `77e93d44`):

> 1. What is the Customer Invoice/AR lifecycle state (draft, posted, partially paid, fully paid) that should be treated as equivalent in blocking weight to Purchase's "open vendor bill" gate, if any?
> 2. Does an Accounting-posted (not merely drafted) Customer Invoice against a Sales commitment line constitute a financial exposure Accounting considers should block that commitment's cancellation — symmetric to how a posted vendor bill blocks Purchase's?
> 3. What does "posted," "locked," "reconciled," or "reversed" mean, precisely, for a Customer Invoice in Accounting's own model — and which of those states, if any, should be the exact fact GROUP A's Sales cancellation gate checks?

**Why this is an `INPUT-CONTRADICTION` and not an `INPUT-GAP`.** The Account programme *did*
establish customer-invoice lifecycle semantics — it ran P02 Order-to-Cash and P08
Record-to-Report and closed Phase S. The input therefore **exists** in one programme and is
**recorded as missing** in another. Two verified programmes hold incompatible positions on
whether this input is available. That is a contradiction between programmes, not an absence.

**Escalation status.** Group A itself recorded: *"Boss decision required: (a) require a
symmetric Sales-side gate once Accounting supplies the answers above, or (b) accept the current
asymmetry as a disclosed risk trade-off. Not decided by this session."*

Carried to `SA14` as contradiction `XD-01` and to `SA19` as the first Boss decision requested.

---

## 7. Domains that cannot supply an input register

| Domain | Reason |
|---|---|
| SA-D05 Supply Routing | 81 blobs; the routing input itself is undetermined |
| SA-D17 Service | 16 blobs; completion-evidence input unknown |
| SA-D18 Project | 4 blobs |
| SA-D19 Quality | 20 blobs; inspection-outcome input unknown |
| SA-D20 Equipment / Maintenance | 13 / 34 blobs |
| SA-D21 Commercial policy | 18 / 16 blobs |

All six are `INPUT-EVIDENCE-INSUFFICIENT` and are routed to `SA16` triggers TVDR-01…TVDR-06.

---

`CP-SA-20 — HOLD`. Inputs are complete for the evidenced domains, carry one contradiction and
one gap, and cannot be stated for six domains.

Boss remains the sole Final Approver.
