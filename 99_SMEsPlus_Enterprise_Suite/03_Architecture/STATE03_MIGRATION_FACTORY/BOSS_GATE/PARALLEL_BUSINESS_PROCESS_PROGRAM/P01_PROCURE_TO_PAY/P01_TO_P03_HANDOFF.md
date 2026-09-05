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
in the same module. Entry condition is `qty_invoiced > qty_received`. **The live firing set has since been narrowed from 49 lines
to a named 18**: of the 49 invoiced-not-received lines, **18 carry `qty_received = 0.000000`** — the exact
zero-denominator subset for the missing guard, at unit prices to ฿3,271,028.04. *(Returns were tested as an
alternative trigger and ruled out: 76 PO lines carry a done `to_refund` return, 49 satisfy the entry
condition, **intersection 0**.)*

**What this means for P03:** manufacturing and unbuild documents **propagate** an already-corrupt unit cost;
they do not originate it. **P03 is a propagation route, not the owner.** P01 owns the defect.

**P01 states no conclusion about P03's own cost mechanisms.**

---

## 2. THE ITEM P01 IS HANDING OVER — CORRECTED AFTER CHALLENGE

> ### THIS SECTION WAS WRONG WHEN FIRST WRITTEN. P01 REPORTED A DOCSTRING AS BEHAVIOUR.

**Module:** `purchase_mrp` — manifest `'version': '1.0'` → `16.0.1.0`, **INSTALLED**, and
**`'auto_install': True`** — it installs itself wherever `mrp` and `purchase_stock` coexist. **P03 cannot
treat it as opt-in.**

**Locator:** `purchase_mrp/models/account_move.py:10-14`, series-16 core `odoo-16.0+e.20230401`.
**The whole method:**

```python
def _get_stock_valuation_layers(self, move):
    """ Do not handle the invoice correction for kit. It has to be done
    manually """
    layers = super()._get_stock_valuation_layers(move)
    return layers.filtered(lambda svl: svl.product_id == self.product_id)
```

### 2.1 What P01 said, and what the code does

**P01 said:** *"kit purchases skip the invoice price-difference correction."*

**The code contains no kit predicate.** Verified: no `bom_type`, no `_bom_find`, no `bom_line_id`, no
`phantom` anywhere in the file. **The word "kit" exists only in the docstring.** The filter is
**unconditional** and applies to **every vendor-bill line in every deployment where the module is installed**.

**And the author knew the difference:** the module's other three overrides **do** gate on kits —
`purchase.py:57`, `purchase.py:82` and `stock_move.py:28` all call
`_bom_find(..., bom_type='phantom')`. **This one was not gated.**

**The mechanism:** the layer population comes from `purchase_stock/models/account_move_line.py:10-13`
(`_get_valued_in_moves` → `self.purchase_line_id.move_ids`), keyed to the **PO line's** product. The filter
compares against **the bill line's** product. **When those differ, `layers` empties**, and
`stock_account/models/account_move.py:290-292` takes `if not layers: continue` — **the correction is silently
skipped, with no kit involved.**

### 2.2 "LATENT here" is withdrawn — the filter is LIVE in this deployment

| Measure | Value |
|---|---|
| `account_move_line` with a `purchase_line_id` *(positive control)* | **14,335** |
| …bill product **==** PO-line product *(control)* | 14,312 |
| …bill product **≠** PO-line product | **23** |
| …of those, valid product lines on posted `in_invoice` | 18 |
| **…where the base method returns ≥ 1 layer — the filter actively drops them** | **13** |

*Synthetic injection control: re-labelling a matched row to product `-999` flips it 0 → 1 and its 3 layers are
all dropped.* **Reachability established. Materiality NOT established** — P01 has not shown these 13 would
have produced a non-zero correction, and did not evaluate the `cost_method != 'standard'` gate.

**The word "LATENT" is removed from this handoff.** It was both wrong and, as AAS-03 Expert 4 noted, **a
severity pre-classification** — it would have ranked the item in P03's register before P03 measured anything,
which cannot stand in the same document as *"no conclusion is implied for deployments not measured."*

### 2.3 The kit census was the right answer from a test that could not see a reverted row

P01 published *"983 BoMs all `type='normal'`, 0 phantom, 0 of 10,490 PO lines reference a kit."* Reproduced —
**and insufficient**: **BoM `type` is mutable** (`max(mrp_bom.write_date) = 2026-07-11`), so a current-state
census cannot answer *"could a BoM have become `normal` after the fact"*. **That is the identical defect P01
already withdrew for `ir_property` in round 6** — and it was repeated here.

**The receipt-time fingerprint does answer it**, and the conclusion survives on that evidence instead:

| Test | Result |
|---|---|
| Moves with `bom_line_id` NOT NULL *(positive control)* | **34,492** |
| Moves with `bom_line_id` **AND** `purchase_line_id` NOT NULL | **0** |
| Done purchase moves whose product ≠ PO-line product | **0 of 13,297** |

**No kit has ever been purchased in this deployment** — established by a control that *can* see history.

### 2.4 "Skip" understates it — partial overlap MIS-SCALES

The filter **truncates**; it empties only when overlap is nil. On **partial** overlap the correction is
computed on a wrong basis: `out_qty = po_line.qty_received - sum(layers.remaining_qty)`
(`stock_account/models/account_move.py:344`) uses the full quantity against a truncated layer set, and
`unit_valuation_difference = price_unit - layers_price_unit[layer]` (`:360`) sets a whole-product price
against a component layer already scaled by `_get_cost_share()`.

**P03 needs "computed on the wrong basis", not "skipped".**

### 2.4a THE FULL FILTER CHAIN — bound now closed, and it strengthens §2.1

AAS-03 Expert 4 returned after publication having completed a sweep it had previously worked around with
targeted greps, closing an undeclared path-set bound on its own negative. **Verified here.** Exactly **three**
definitions of `_get_stock_valuation_layers` exist in the series-16 core, and **none** in the custom root:

| # | Participant | Effect |
|---|---|---|
| 1 | `stock_account/models/account_move.py:322` — **the base** | returns `valued_moves.stock_valuation_layer_ids`, direction-filtered (`_is_in` / `_is_out` for refunds) |
| 2 | `stock_landed_costs/models/account_move.py:75` | `layers.filtered(lambda svl: not svl.stock_landed_cost_id)` — **drops landed-cost layers** |
| 3 | `purchase_mrp/models/account_move.py:10` | `layers.filtered(lambda svl: svl.product_id == self.product_id)` — **drops layers whose product ≠ the bill line's** |

**Both overrides are `.filtered()` narrowings of their super's result.** Two consequences P03 can rely on:

- **MRO order cannot change the final set** — narrowings commute.
- **There is no fourth participant, and none of the three can reintroduce a dropped layer.** So the mechanism
  in §2.1 is complete, and **the 13 live rows in §2.2 cannot be rescued by another module.**

**A third participant P01 had not named: `stock_landed_costs`.** It is **installed** in this deployment and
**`stock_landed_cost` holds 0 rows**, so it is inert here — **but it silently drops landed-cost layers from
the price-difference correction wherever landed costs are used.** P03 should carry it for the same reason it
carries §2.5.

### 2.5 THREE FURTHER OVERRIDES P01 FAILED TO DISCLOSE

P01 named **one** of `purchase_mrp`'s four valuation-relevant overrides. The two that matter most:

| Override | Why it matters |
|---|---|
| `stock_move.py:19 _get_price_unit` | **wraps the exact method P01 names as the cost-explosion root cause** |
| `purchase.py:50 _compute_qty_received` | **rewrites `qty_received`** — that root cause's *entry condition* |

Both are inert in this deployment. **Both were undisclosed, and either would change how P03 reads the
handoff.**

### 2.6 What P03 must answer — and the boundary, restated

**A boundary correction P01 accepts:** the writer here is
`account.move.line._create_in_invoice_svl`, driven by a **vendor bill** — the same family P01 elsewhere calls
its own. **Routing "kits" to P03 is right; routing this method's *non-kit* failure mode away from P01 is not**,
because §2.1 shows **no predicate separates them**. **The split is by behaviour, not by module name:**

- **P01 retains** the unconditional product-mismatch filter and its 13 live rows.
- **P03 receives** the kit-specific question: where phantom BoMs exist, does the kit purchase price difference
  reach RM/WIP/FG cost at all, and is the "manual" correction a defined procedure or an assumption in a comment?

**Also unexplained and unowned:** how **18 bill lines came to name a different product than their PO line** at
all. A separate defect, unmentioned before this challenge.

**Explicitly out of scope:** no conclusion is implied for any deployment P01 did not measure. Before P03
inherits any "kits are used elsewhere" premise, **both controls — the BoM census and the
`bom_line_id ∧ purchase_line_id` fingerprint — must be re-run on the series-18 and series-19 deployments.**

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
