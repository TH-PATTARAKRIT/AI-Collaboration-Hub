# 34 — G02-P02 DELIVERED-NOT-INVOICED / CUT-OFF MEASURE

`LAYER 2 — AUDIT QUARANTINE.` Task **C5**. Baseline `ff8be51`.

**Status: `MEASURED` across 8 deployed databases and 4 generations.** Offline extraction only.

> ## ⚠ CORRECTION BANNER — `C-34` / `RE-29`, RAISED BY AAS-03 EXPERT 1 AND CONFIRMED
>
> **The measure below uses `qty_invoiced`, which counts DRAFT invoices.** `sale/models/sale_order_line.py:916-924`
> accumulates every invoice line whose move `state != 'cancel'`. The reference ships a **separate
> accounting counter**, `qty_invoiced_posted`, whose own docstring reads *"for accounting purposes, we
> only want the quantities of the posted invoices"* — and it is **not stored**, so it cannot be read
> from an archive.
>
> **Re-measured on `iSMEs` (`45a8e08e`) with a posted-only instrument** built by joining
> `sale_order_line` → `sale_order_line_invoice_rel` → `account_move_line` → `account_move`
> (`state='posted'`, `move_type IN ('out_invoice','out_refund')`):
>
> | basis | delivered > invoiced | invoiced > delivered |
> |---|---|---|
> | `qty_invoiced` (draft-inclusive) — **as published below** | **47** | 789 |
> | **posted only — the accounting basis** | **1,145** | 792 |
>
> **1,877 of 4,901 confirmed lines carry a draft invoice** inflating `qty_invoiced`.
>
> **Two consequences, both material:**
> 1. **The delivered-not-invoiced exposure was understated 24×** — 1,145 lines (23.4%), not 47 (1.0%).
> 2. **`P02-F-34b`'s direction REVERSES.** On the accounting basis delivered-not-invoiced (1,145)
>    **exceeds** billed-ahead (792) — 1.4:1 toward delivery, not 17:1 the other way. **The sentence
>    "the dominant cut-off exposure is billing ahead of performance" is WITHDRAWN for `iSMEs`.**
>
> **Bound:** only `iSMEs` has been re-measured on the posted basis. **Every other row in §2 remains
> draft-basis and is therefore a floor, not a measure.** Re-measuring the other seven is the first
> named next action.
>
> **`P02-F-34e` (Expert 1, CH-5) — ACCEPTED, NOT YET EXECUTED.** Neither basis segments by the line's
> product `invoice_policy`. For an `order`-policy product, `invoiced > delivered` is the **designed**
> state, not an exposure. The 792 and the 2,564 must be split by policy before P10 acts on them.
> `invoice_policy` is **not** on `sale_order_line` (verified: column absent) — it resolves from the
> product, so the segmentation needs a `product_template` join and is not done here.

---

## 1. Denominator

**POPULATION** — every confirmed sale order line (`state IN ('sale','done')`) in the 8 deployed
databases that carry a `sale_order_line` table with `qty_delivered`. **PATTERN** — `qty_delivered >
qty_invoiced` at line level. **PATH SET** — the artefacts named per row (per `P02-F-30a`, a figure names
its artefact, not just its uuid). **UNIT** — one **sale order line**.

**Why the line and not the order.** An order can be part-delivered and part-invoiced simultaneously;
measuring at order level would net two opposite exposures into one and hide both.

## 2. The Measure

| uuid | gen | artefact | confirmed lines | **delivered > invoiced** | invoiced > delivered | matched | neither |
|---|---|---|---|---|---|---|---|
| `5d5164c4` | 14.0 | `odoo_cff_golive_99-…` | 96,411 | **2,088** | 986 | 75,233 | 18,104 |
| `25e88cd4` | 14.0 | `iErpOCC_2024-06-10` | 27,293 | **253** | 2,564 | 14,498 | 9,978 |
| `45a8e08e` | 16.0 | `iSMEs_2026-07-11` | 4,901 | **47** | 789 | 3,063 | 1,002 |
| `1d1f5d3e` | 18.0 | `iSMEs182_2025-01-18` | 22 | 0 | 2 | 3 | 17 |
| `4b766580` | 18.0 | `pankhamhom_2026-01-21` | 25 | **4** | 4 | 5 | 12 |
| `551ab874` | 18.0 | `4e640e74-….dump` | 34,590 | 0 | 0 | 0 | **34,590** |
| `66d1b52a` | 19.0 | `BK12MAY26_2026-08-03` | 9,098 | **1,201** | 0 | **0** | 7,897 |
| `a1430edc` | 19.0 | `iTEST02_2026-06-14` | 1 | 0 | 0 | 0 | 1 |

**`P02-F-34a`. Delivered-not-invoiced is real and cross-generational: 3,593 lines across 5 databases and
4 generations.**

## 3. Two Findings The Direction Reveals

**`P02-F-34b` — WITHDRAWN FOR `iSMEs` BY `C-34` (see banner). As originally written:** on the largest Thai deployment the exposure runs the *other* way. In `iSMEs`,
**invoiced-ahead-of-delivery is 789 lines (16.1%)** against 47 delivered-not-invoiced (1.0%) — a 17:1
ratio. In `iErpOCC` it is 2,564 vs 253, **10:1**. **The dominant cut-off exposure in the two Thai
deployments is billing ahead of performance, not delivery ahead of billing.**

That is a **revenue-recognition** exposure, and it is **P10-owned** (`BP-03` is explicit that revenue on
billing versus performance is a separate open decision). P02 measures it and routes it; **P02 does not
decide it.**

**`P02-F-34c` — one v19 deployment has delivered 1,201 lines and invoiced nothing, ever.** `BK12MAY26`
shows 1,201 delivered-not-invoiced, **0** invoiced-ahead, and **0 matched** — no sale line in that
database has ever been invoiced against delivery. Combined with `P02-F-28c` (v19 has no valuation-layer
table) and its **zero `cogs` markers over 563 journal lines**, this is a deployment where goods leave and
neither cost nor revenue follows through this path.

## 4. The Date Dimension — Age Of The Position

Measured on `iSMEs` (`45a8e08e`), the strongest readable case: for each of the 47 lines, the **latest
`state='done'` `stock_move.date`** — the physical outflow.

| Year of last physical outflow | lines |
|---|---|
| 2024 | **21** |
| 2025 | 19 |
| 2026 | 1 |

41 of 47 have a completed physical outflow; 6 are flagged for invoicing with no `done` movement.
**Oldest 2024-02-02; archive snapshot 2026-07-11 — 2 years 5 months.** **40 of 41 positions are more
than a year old.**

## 5. `P02-F-34d` — The Correction This Round Makes To Its Own Framing

A first draft of this file was going to say no first-class position exists. **That is wrong, and the
source refutes it:**

- `sale.order.line.invoice_status` and `sale.order.invoice_status` — stored Selection;
- `sale.order.amount_to_invoice`, string **"Un-invoiced Balance"** (`sale/models/sale_order.py:239`);
- `sale.order.line.amount_to_invoice` / `untaxed_amount_to_invoice`;
- `untaxed_amount_to_invoice` is even exposed on the sales **report** object.

And the data agrees: **all 47 lines carry `invoice_status = 'to invoice'`. Every one.**

**So the system knows, names the balance, and can report it. What it never does is account for it.**

| Dimension | Present? |
|---|---|
| Operational status | **Yes** — `invoice_status='to invoice'`, correct on 47/47 |
| Sales-side monetary balance | **Yes** — `amount_to_invoice`, "Un-invoiced Balance" |
| **General-ledger position** | **No** — no account, no journal entry, no subledger |
| **Ageing by date** | **No** — the balance is a computed *current* figure with no ageing dimension |
| **Accounting date** | **No** — the position has no accounting date at all, only movement dates |

**The failure is not detection. It is that a correctly-detected operational fact never becomes an
accounting fact, and therefore never ages, never appears in a close, and never reconciles.** A position
open for two years and five months is visible on a sales screen and invisible to the ledger.

## 6. Two-Subsystem Reconstruction — Confirmed, With Its Exact Shape

To obtain §4 required joining `sale_order_line` (sales) to `stock_move` (inventory) on `sale_line_id`
and filtering `state='done'`. **The accounting subsystem contributed nothing** — it holds no record of
the position. So the answer to *"is the state visible only by reconstructing two subsystems"* is:
**the operational state needs two subsystems (sales + stock); the accounting state needs three, and the
third has no data to contribute.**

## 7. Method Notes And Bounds

- **Not used:** a convenient movement date where an accounting entry date exists. Per `RE-18`, §4 is
  explicitly the **physical outflow** date and is labelled as such; it is **not** offered as a
  period-bearing accounting date, because these positions have none.
- **No obligation ledger is inferred.** The benchmark has none; it remains a SMEsPlus `DESIGN CANDIDATE`
  (`38`).
- **`551ab874`'s 34,590 "neither" lines** are a UAT database with confirmed orders and no fulfilment —
  correctly excluded from exposure, and a useful negative control that the pattern does not fire on
  untransacted data.
- **Bound:** amounts and cost basis are not published here. `qty_delivered − qty_invoiced` is a quantity;
  converting to value requires the line's price and cost basis per generation, and for the two v14
  deployments the cost basis is governed by 409 unreadable custom modules (`31`). **Quantity is
  measured; value is `EVIDENCE REQUIRED`.**

## 8. Routing

| To | What |
|---|---|
| **P10** | `P02-F-34b` (billing ahead of performance, 789 and 2,564 lines) and `P02-F-34c`. Revenue timing is P10-owned under `BP-03`. |
| **P08** | The absence of any GL position or ageing for a two-year-old delivered balance — a close-integrity question. |
| **P11** | The design candidate: a first-class, ageable, scope-aware obligation position with an accounting date. |
