# P01 → P03 (MANUFACTURE-TO-COST) — CONTROLLED HANDOFF

Session: `SMEPLUS-26-09-05-G01-P01-P2P-CONTROLLED-SCOPE-FREEZE-HANDOFF-001`
Group: **G01 — Supply / Cost / Payable** · Checkpoint `CP-03`
Baseline: `a02ec8b6628daf145c03fa49397448a7f29605ea`

> **P01 hands P03 a question and its evidence. P01 does not hand P03 a conclusion, and has not started P03 work.**

---

## 1. FIRST — A ROUTING P01 WITHDRAWS

In round 6 P01 routed the valuation cost-explosion (30 layers to ±1.5e21 THB, per-unit costs to
฿52,616,504,567,828,624) to **P03 as owner**, on the reasoning that the documents involved were `WH/MO/…`
manufacturing and `UB/…` unbuild.

**That routing was wrong and is withdrawn.** The root cause is in **P01's own path**:

**Locator:** `purchase_stock/models/stock_move.py::_get_price_unit`, series-16 core
`odoo-16.0+e.20230401` (version-ranked to the deployment, 144/144).

```
if float_compare(line.qty_invoiced, received_qty, precision_rounding=...) > 0:
    for invoice_line in line.invoice_lines:
        invoiced_value += invoice_line.price_unit * invoice_line.quantity
        invoiced_qty   += invoice_line.product_uom_id._compute_quantity(...)
    remaining_value = invoiced_value - receipt_value
    remaining_qty   = invoiced_qty - line.product_uom._compute_quantity(received_qty, ...)
    price_unit = float_round(remaining_value / remaining_qty, precision_digits=price_unit_prec)
```

Three defects, all read in source: **no zero-guard on `remaining_qty`**; `invoice_lines` summed **unsigned**
so refund lines *increase* the base; **no cancelled-bill filter**. All three contradict `_compute_qty_invoiced`
in the same module. Entry condition is `qty_invoiced > qty_received`.

**What this means for P03:** manufacturing and unbuild documents **propagate** an already-corrupt unit cost;
they do not originate it. **P03 is a propagation route, not the owner.** P01 owns the defect.

**P01 states no conclusion about P03's own cost mechanisms.**

---

## 2. THE ITEM P01 IS ACTUALLY HANDING OVER — THE KIT CORRECTION GAP

**Module:** `purchase_mrp 16.0.1.0` — **INSTALLED** in the series-16 deployment (`ir_module_module`).
**Locator:** `purchase_mrp` overrides **`_get_stock_valuation_layers`**, filtering the layer set to the bill
line's own product. The source carries the explicit comment:

> *"Do not handle the invoice correction for kit. It has to be done manually."*

**Consequence in principle:** a **kit** purchase does not receive the automatic invoice price-difference
correction that a non-kit purchase receives. The correction is left to a manual step.

### 2.1 In THIS deployment it is LATENT — with the measurement

| Test | Result |
|---|---|
| `mrp_bom` rows | **983** |
| …of `type = 'normal'` | **983** |
| …**phantom** BoMs (a kit) | **0** |
| `purchase_order_line` rows referencing a kit | **0 of 10,490** |

**The gap cannot fire here.** *(Reported by AAS-03 Expert 4; the boundary is under targeted challenge in
`P01_G01_CLOSURE_AAS03_CHALLENGE.md`.)*

### 2.2 What P03 must answer, and what P01 must not

**P01 does not know, and does not assert:**
- whether any other deployment in the estate uses kits;
- whether the manual correction the comment refers to is performed anywhere;
- what the correct RM / WIP / FG cost treatment is when a kit purchase price differs from its bill.

**Questions for P03:**
1. In deployments where phantom BoMs exist, does the kit purchase price difference reach RM/WIP/FG cost at all?
2. Is the "manual" correction a defined procedure, or an assumption in a vendor comment?
3. Does the P03 cost model depend on the purchase price difference having been applied before manufacturing consumes the component?
4. Given §1, does P03's cost chain have its own guard against a corrupt incoming unit cost, or does it inherit whatever `_get_price_unit` produced?

**Explicitly out of scope for this handoff:** no conclusion is implied for any deployment P01 did not measure.
The only deployment measured for kit activity is `45a8e08e`.

---

## 3. EVIDENCE LOCATORS

| Item | Locator |
|---|---|
| Deployment | `~/Downloads/iSMEs_2026-07-11_05-03-27.dump`, `database.uuid 45a8e08e-5dcd-11ee-90f5-5242ea102159`, `swr.smeplus.asia`, 1 company |
| Series-16 core (ranked 144/144) | `…/16 ODOO 16 ENTERPRISE/odoo-16.0+e.20230401/odoo/addons` |
| Custom source root | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/addons` — 45 of 46 deployed non-core modules |
| Extracts | `…/scratchpad/s16/T_*.sql` (**41 of 651 tables — 6.3%**, see §5) |

---

## 4. METHOD CONTROL P03 SHOULD CARRY

> **An installed module that modifies a writer's INPUT can materially change behaviour without being a writer.**

`purchase_mrp` alters what `_prepare_in_invoice_svl_vals` receives while containing **no assignment** to
`stock_valuation_layer.account_move_id`. A writer enumeration scoped to writers is **correct and not
sufficient**. This cost an expert a missed finding on its first pass and is recorded so P03 does not repeat it.

---

## 5. LIMITS OF THIS HANDOFF

- **41 of 651 tables (6.3%) were extracted**, with no declared selection rule (`GAP-P01-07`). Every negative
  above is bounded by that.
- Nothing has been executed at runtime in six rounds. All behaviour is read from source and records.
- The kit-latency finding is a **single-deployment** measurement.
