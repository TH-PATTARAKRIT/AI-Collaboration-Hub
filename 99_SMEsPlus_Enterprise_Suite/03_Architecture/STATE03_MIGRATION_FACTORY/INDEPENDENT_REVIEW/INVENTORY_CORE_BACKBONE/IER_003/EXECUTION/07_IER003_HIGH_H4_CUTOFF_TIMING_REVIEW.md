# 07 — High H4 (N-A7-03 / N-A9-02): Inventory Date / Cutoff / Period-Lock — Independent Verdict

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Independently locate Inventory-side date facts and the Inventory↔Accounting cutoff boundary | Independent Evidence Reviewer | `stock/models/stock_move.py:28-31,149,193`; `stock_account/models/stock_picking.py` (full file); `01 ACCOUNT/account` lock-date model; DB schema | 2026-09-01 | Boss | **VERIFIED CLOSED — MAJOR CORRECTION** | Directly unblocks Cross-Proof scenario 6, previously TEAM A's own highest-priority named gap |

## TEAM A's claim (A14 Part 2, N-A7-03/N-A9-02; A15 §1, A16 scenario 6)

> "No date/effective-date fields and any period-lock mechanism [were] located in the files read this pass... Status: `EVIDENCE_MISSING`... the single most material gap blocking full confidence in [Cross-Proof] scenario 6."

This was explicitly named in A18 §2 item 6 as "the single highest-priority follow-up item" in the entire DR-002 package.

## What this review found

### Inventory-side date fields — exist, exact citations

Direct read of `stock/models/stock_move.py`:

```python
28:  date = fields.Datetime(...)
31:  date_deadline = fields.Datetime(...)
149: delay_alert_date = fields.Datetime('Delay Alert Date', help='Process at this date to be on time', compute="_compute_delay_alert_date", store=True)
193: reservation_date = fields.Date('Date to Reserve', compute='_compute_reservation_date', store=True, ...)
```

Plus, confirmed via DB schema query, `stock.picking` carries `scheduled_date` and `date_done` (both used directly in the mechanism below).

### The connecting mechanism — found in the exact module TEAM A's own A9 studied most deeply

`stock_account/models/stock_picking.py` (full file, 32 lines):

```python
class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.constrains("scheduled_date", "date_done")
    def _check_backdate_allowed(self):
        if self.env['ir.config_parameter'].sudo().get_param('stock_account.skip_lock_date_check'):
            return
        for picking in self:
            if picking._is_date_in_lock_period():
                raise ValidationError(...)

    def _is_date_in_lock_period(self):
        self.ensure_one()
        lock = []
        if self.state == "done":
            lock += self.company_id._get_lock_date_violations(self.scheduled_date.date(), fiscalyear=True, ..., hard=True)
        if self.date_done:
            lock += self.company_id._get_lock_date_violations(self.date_done.date(), fiscalyear=True, ..., hard=True)
        return bool(lock)
```

This is a `@api.constrains` guard: **it is impossible to record or backdate a `stock.picking`'s scheduled/done date into a locked fiscal period**, unless the `stock_account.skip_lock_date_check` system parameter is explicitly set. A dedicated test exists confirming this is deliberate, tested behavior, not incidental: `stock_account/tests/test_account_move.py::test_backdate_picking_with_lock_date` (parametrized across `sale_lock_date`/`purchase_lock_date`/`tax_lock_date`/`fiscalyear_lock_date`/`hard_lock_date`).

### Accounting-side period-lock model — confirmed via DB schema

`res_company` carries `fiscalyear_lock_date`, `tax_lock_date`, `sale_lock_date`, `purchase_lock_date`, `hard_lock_date`. A dedicated override/exception model exists: `account_lock_exception` (`lock_date_field`, `lock_date`, `company_lock_date`) — allowing scoped, audited exceptions to an otherwise-hard lock.

### Why TEAM A missed this

A9's own scope statement (§0) says it read `stock_account/models/` — and indeed cites `stock_account/models/account_move.py`, `stock_account/models/account_move_line.py`, `stock_account/models/stock_lot.py` extensively. `stock_picking.py` is a short (32-line), easily-overlooked file in the same directory that was evidently not opened. This is a real, narrow research gap — not a fabrication and not a structural absence — closed by a single additional file read plus one schema query.

## Independent verdict

**`VERIFIED CLOSED`**

- Evidence read: `stock/models/stock_move.py` (date fields), `stock_account/models/stock_picking.py` (full file, the enforcement mechanism), `stock_account/tests/test_account_move.py` (confirming test), DB schema for `res_company`/`account_lock_exception`.
- What remains unknown: whether this mechanism's specific lock-type flags (`fiscalyear=True, hard=True`, but `sale=False, purchase=False, tax=False` in this particular call) are the correct/complete set for SMEsPlus's own target design — an Accounting-owned design question, not a source-evidence gap.
- **Inventory Gate blocking: NO** — was previously the single most material open item; now closed with primary-source evidence.
- Stock Truth impact: Direct, now positively characterized — Inventory's `stock.move.date`/`stock.picking.scheduled_date`/`date_done` are the fields Accounting's lock-date mechanism reads; the boundary DR-002 asked for (§0 of A9: "Inventory knows the stock fact and valuation handoff evidence; Accounting owns final financial truth") is now precisely demonstrated in code, not merely asserted.
- Accounting interface impact: Direct — this **is** Cross-Proof scenario 6's evidence requirement, now supplied.
- Dependent-module impact: Sales, Purchase, Accounting — unchanged from TEAM A's assessment, now de-risked.
- Migration impact: Medium, unchanged, but now informed — a migration must be aware that backdating a done picking's date across a lock boundary is actively guarded against by this constraint (relevant to any bulk-load/migration script that writes historical `stock.picking` rows directly).
- **Next owner / next action**: None required to close this item. Recommended: fold this citation into A7/A9/A14/A16 (Cross-Proof scenario 6 readiness should be upgraded from "NOT READY" to "Inventory side ready") in TEAM A's next pass — see [11](11_IER003_ACCOUNTING_X_INVENTORY_CROSS_PROOF_READINESS.md) and [14](14_IER003_TARGETED_TEAM_A_CORRECTIVE_RECOMMENDATION.md).

No Unknown was converted to a Fact by inference — every citation above is a direct file read or a direct schema query, not a deduction.
