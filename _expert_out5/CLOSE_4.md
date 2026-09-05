# CLOSE_4 — AAS-03 Expert 4 (Lead Code & UI Architect)
## Targeted challenge: C-6 `purchase_mrp` kit gap / P01→P03 handoff. READ-ONLY. Not a re-review.

**Overall: CHALLENGED.** The kit arithmetic reproduces exactly, but the *mechanism sentence is wrong* and
*"LATENT here" is contradicted by this deployment's own data*: the override carries no kit predicate, and
13 posted bill lines already reach it non-vacuously with zero kits involved.

---

## Instrument validation (positive controls, run first)
```
python3 c6.py / c6b.py / c6c.py  (COPY-block parsers over the s16 dumps)
 POS CONTROL svl rows: 74982 | with account_move_id: 57863
 POS CONTROL price_diff NOT NULL: 1267 | price_diff nonzero: 1123
```
C-2's 57,863/74,982 and C-5's 1,267/1,123 reproduce to the digit off my own loader. The instrument is sound.

---

## F1 — Source locator: SUPPORTED, but C-6 states no path and no line
C-6 names a module and a method, never a file:line. The locator is:

`.../odoo-16.0+e.20230401/odoo/addons/purchase_mrp/models/account_move.py:10-14`
```python
class AccountMoveLine(models.Model):
    _inherit = "account.move.line"
    def _get_stock_valuation_layers(self, move):
        """ Do not handle the invoice correction for kit. It has to be done manually """
        layers = super()._get_stock_valuation_layers(move)
        return layers.filtered(lambda svl: svl.product_id == self.product_id)
```
Version: `purchase_mrp/__manifest__.py` `'version': '1.0'` → `16.0.1.0`; `installed.txt` line `purchase_mrp 16.0.1.0`. Matches.
Custom tree carries no competing override: `grep -rn "_get_stock_valuation_layers\|_get_valued_in_moves\|bom_type='phantom'" /Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/addons` → 0 hits, against a
positive control of 453 `.py` files / 184 containing `_inherit` in that same tree.
**Limit:** version string and file content are not proof of deployed code identity. Not closed.

## F2 — Described behaviour: CHALLENGED. C-6 reports the docstring, not the code.
C-6: *"overrides `_get_stock_valuation_layers` so kit purchases skip the invoice price-difference correction."*
**The override has no kit predicate at all.** No `_bom_find`, no `bom_type='phantom'`, no `bom_line_id`.
It filters **every** vendor-bill line on **every** deployment where the module is installed. The word "kit"
exists only in the docstring. Compare the module's *other* three overrides, which all do test for kits
(`purchase_mrp/models/stock_move.py:21,28`, `purchase.py:57,82`) — the author gated those and not this one.

The population it filters is set by `purchase_stock/models/account_move_line.py:10-13`:
`_get_valued_in_moves` → `self.purchase_line_id.move_ids` (done, qty≠0), i.e. keyed to the **PO line's**
product. The filter compares against `self.product_id`, the **bill line's** product. Those two are the same
object only by convention. **Whenever they differ, the filter empties `layers` and
`stock_account/models/account_move.py:290-292` takes `if not layers: continue`** — the price-difference
correction is silently skipped with no kit anywhere in the picture.

## F3 — "LATENT here": CHALLENGED on this deployment's data.
`aml.product_id != purchase_order_line.product_id`, product lines, posted, in_invoice:
```
aml with purchase_line_id (pos. control) : 14,335
  aml.product == POline.product (control): 14,312
  aml.product != POline.product          :     23   (5 have NULL product -> fail caller gate)
  ... NOT NULL, display_type='product'   :     18   all (in_invoice, posted)
  ... of which base _get_stock_valuation_layers() returns >=1 non-landed-cost layer : 13
```
For all 13, **every** returned layer's `product_id` equals the PO-line product and none equals the bill-line
product, so `.filtered()` returns empty and the correction is skipped.
Positive control: 13,369 of 14,265 matched rows also return ≥1 base layer, so the detector fires.
Synthetic injection: matched row 135718 re-labelled to product `-999` flips 0→1 and its 3 base layers are all
dropped by the filter — the predicate can fire.
Examples: aml 2167 (bill prod 11293 / PO prod 11292), aml 482476-482492 (six lines on bills 185983/185986),
aml 308365, aml 4229.

**So the modified input is already hit in series 16.** "LATENT here" is not safe as written; the honest
statement is *"no **kit** path is reachable here; a non-kit path through the same modified input is reachable
and fires on 13 posted lines."*

**Not overclaimed:** I have not shown these 13 would have produced a *non-zero* correction absent
`purchase_mrp`, and I did not evaluate the `cost_method != 'standard'` caller gate per product. A spread check
is uninformative at this n: 0 of 7 affected bills carry any SVL vs 680 of 9,661 (7.0%) matched bills — expected
0.5 at n=7, so 0 discriminates nothing. **Live-input reachability is established; materiality is not.**

## F4 — The kit test itself: right answer, insufficient test. C-6 is missing its own strongest control.
Reproduced exactly: `mrp_bom` = **983 rows, all `type='normal'`** (942 active / 41 archived — C-6 does not
disclose the split), **0 phantom**; **0 of 10,490** PO lines carry a product whose template has a phantom BoM.
Two things C-6 should carry and does not:
- Stronger same-run figure: **0 of 10,490** PO lines reference *any* BoM, active or archived. Not "no kits" —
  *no BoM product was ever purchased at all*.
- **The retrospective control.** BoM `type` is mutable and `max(mrp_bom.write_date) = 2026-07-11`, i.e. BoMs
  were edited up to the dump — so a current-state type census cannot answer *"could a BoM have become
  `normal` after the fact?"*. The receipt-time fingerprint of a kit explosion is `stock_move.bom_line_id`
  (set by `mrp`, propagated onto purchase moves by `purchase_mrp/models/stock_move.py:13-17`):
  ```
  moves with bom_line_id NOT NULL (pos. control)                : 34,492
  moves with bom_line_id NOT NULL AND purchase_line_id NOT NULL :      0
  moves (purchase_line_id, done, qty!=0)                        : 13,297
    move.product == POline.product (pos. control)               : 13,297
    move.product != POline.product                              :      0
  ```
  **0 of 34,492.** No kit was ever exploded onto a purchase line in this history. The conclusion survives —
  but on evidence C-6 does not present. As published, the kit claim rests on a current-state census that
  cannot see a reverted row, which is the identical defect C-3 already withdrew for `ir_property`.

## F5 — "skip" is only the all-or-nothing case. RISKY for P03.
The filter *truncates*; it empties only when the overlap is nil. On partial overlap (kit whose bill line names
one component), the surviving path mis-scales rather than skips, and both errors point the same way:
- `stock_account/models/account_move.py:344-346`: `out_qty = po_line.qty_received - sum(layers.remaining_qty)`
  — full-kit `qty_received` against a truncated layer set → `out_qty` inflates → `total_to_correct` shrinks.
- line 360: `unit_valuation_difference = price_unit - layers_price_unit[layer]` — whole bill-line price against
  a component layer whose unit cost was already scaled by `bom_line._get_cost_share()`
  (`purchase_mrp/models/stock_move.py:19-24`) → the difference is wrong by ~1/cost_share.
P03 needs "correction computed on the wrong basis", not just "correction skipped".

## F6 — Handoff completeness: MISSING. The module's footprint is larger than C-6's one sentence.
`purchase_mrp` carries **four** valuation-relevant overrides; C-6 names one:
| Locator | Effect | Status here |
|---|---|---|
| `models/account_move.py:10` `_get_stock_valuation_layers` | unconditional product filter | **live on 13 rows** |
| `models/stock_move.py:19` `_get_price_unit` | wraps **`purchase_stock/models/stock_move.py::_get_price_unit`** — the exact method C-2 names as the cost-explosion root cause | inert (no `bom_line_id` on purchase moves) |
| `models/purchase.py:50` `_compute_qty_received` | rewrites `qty_received`, which is the entry condition `qty_invoiced > qty_received` of that same root cause | inert |
| `models/stock_move.py:26` `_get_valuation_price_and_qty` | raises `UserError` on zero kit valuation | off (`anglo_saxon_accounting = FALSE`, C-4) |
Also: `__manifest__.py` `'auto_install': True`. P03 cannot treat this module as opt-in — it installs itself
wherever `mrp` and `purchase_stock` coexist, which is every environment P03 owns.

## F7 — Boundary: C-6 is not overstepping into P03; it is handing P03 P01's own writer.
The writer is `account.move.line._create_in_invoice_svl` in `stock_account`, driven by a **vendor bill** — the
same method family as C-4 and C-5, and C-2 says the cost-explosion path is "P01's own". Routing "kits" to P03
is defensible; routing *this method's non-kit failure mode* out of P01 is not, and F2/F3 show the two are the
same code with no predicate separating them. Recommend the split be stated explicitly rather than by module
name: **P01 keeps `_get_stock_valuation_layers` behaviour on non-kit bill lines; P03 takes kit cost-share
and BoM-explosion valuation.**

Second boundary point: **"LATENT" is a severity pre-classification, not a fact handed over.** It is P01's
reading of reachability in P01's deployment, and it will rank the item in P03's register before P03 measures
anything. C-6 already says "no conclusion is implied for deployments not measured" — that disclaimer and the
word "LATENT" in the same paragraph do not survive together. State reachability as measured
(`0 of 34,492 kit-exploded purchase moves in series 16`) and let P03 rank.

---

## Verdict by attack line
| Attack | Verdict |
|---|---|
| Source locator and version | **SUPPORTED** (path/line absent from C-6; code identity not proven) |
| Described behaviour | **CHALLENGED** — override is unconditional; C-6 states the docstring's intent |
| "0 of 10,490 PO lines" is the right test | **MISSING** — right answer, insufficient test; retrospective control (`bom_line_id`) omitted, and BoM type is mutable to 2026-07-11 |
| "LATENT here" | **CHALLENGED** — 13 posted bill lines hit the modified input non-vacuously, no kit involved |
| Handoff gives P03 what it needs | **MISSING** — 1 of 4 overrides named; `auto_install` undisclosed; "skip" hides the mis-scaling case |
| P01 overstepping | **RISKY** — not overstepping; under-stepping. P01's own writer is being routed away, and "LATENT" pre-ranks P03's item |

## EVIDENCE NEEDED NEXT
1. **Runtime, not source.** Nothing in six rounds was executed (C-9). Post one vendor bill whose line product
   differs from the PO line product, with and without `purchase_mrp` loaded, and diff the created SVL set.
   That is the only test that converts F3 from reachability to materiality.
2. **The 13 rows, valued.** Compute what `_get_stock_layer_price_difference` would have returned for
   aml 2167, 4229, 308365, 482476-482492, 510850, 512089, 529080, 531840 absent the filter. Currently unmeasured.
3. **Deployed code identity.** Hash the running `purchase_mrp/models/account_move.py` against the series-16
   core file. Version strings do not identify code.
4. **How 18 bill lines came to name a different product than their PO line.** That is a separate defect with a
   separate owner and C-6 does not mention it exists.
5. **Kit-active peer deployments.** Re-run the two controls (`mrp_bom.type` census **and**
   `bom_line_id ∧ purchase_line_id`) on series 18 and 19 before P03 inherits a "kits are used elsewhere" premise
   nobody has measured.
