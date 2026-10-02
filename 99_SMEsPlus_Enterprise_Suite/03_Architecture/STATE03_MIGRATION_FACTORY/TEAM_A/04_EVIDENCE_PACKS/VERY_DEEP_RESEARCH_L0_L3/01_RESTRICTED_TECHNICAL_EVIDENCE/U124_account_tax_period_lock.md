# U124 — account: Tax Report Period Lock (GAP-027)
**Unit ID:** U124 | **G Group:** G01 | **Priority:** P1 | **Analyst:** DeepSeek Worker

---

## Executive Summary

GAP-027 ("tax_lock_date enforcement — L7 not proven") is **CLOSED at C1 level** for all core lock enforcement behaviours. The `tax_lock_date` field exists in the Community `account` module on `res.company`, is enforced at journal entry write/post/delete/unlink via `account.move.line._check_tax_lock_date()`, and is propagated to UI as a blocking alert via `account.move.tax_lock_date_message`. A per-user exception system (`account.lock_exception`) is present in Community and allows temporary relaxation of the lock for specific users. The auto-set mechanism (automatic advance of `tax_lock_date` when tax closing entry is posted) is **documented in the field help string** in Community but its trigger code is NOT present in `account` Community — it is implemented in a separate module (likely `account_tax_report` which is Enterprise/l10n). This auto-set aspect is **ABSENT** in Community: the date must be manually set via company write. Five lock date types exist in Community: `fiscalyear_lock_date`, `tax_lock_date`, `sale_lock_date`, `purchase_lock_date`, `hard_lock_date`.

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|----------|-------------|---------|--------|-------|-----------|-------|---------------------|-------------|
| U124-C01 | F-TAXLOCK-FIELD | `account/models/company.py:81-86` | `tax_lock_date = fields.Date(string="Tax Return Lock Date", tracking=True, ...)` | C1 | Always | C1,TH | `res.company.tax_lock_date` is a tracked `fields.Date` with help text stating "The tax lock date is automatically set when the tax closing entry is posted." It is listed in `SOFT_LOCK_DATE_FIELDS` at line 59. | Tax period lock date field definition on company model |
| U124-C02 | F-TAXLOCK-FIELD | `account/models/company.py:109` | `user_tax_lock_date = fields.Date(compute='_compute_user_tax_lock_date')` | C1 | Always | C1 | `res.company.user_tax_lock_date` is a computed field that applies active user lock exceptions before returning the effective date, via `_get_user_lock_date('tax_lock_date', ignore_exceptions)`. | Per-user effective tax lock date computed field |
| U124-C03 | F-TAXLOCK-COMPUTE | `account/models/company.py:421-426` | `def _compute_user_tax_lock_date(self)` | C1 | Always | C1 | `_compute_user_tax_lock_date` depends on `tax_lock_date` and context key `uid,ignore_exceptions`. It calls `_get_user_lock_date('tax_lock_date', ignore_exceptions)` which searches `account.lock_exception` for active exceptions narrowing the lock date for the current user. | User-aware tax lock date computation with exception support |
| U124-C04 | F-TAXLOCK-VIOLATION | `account/models/company.py:675-710` | `def _get_lock_date_violations(self, accounting_date, fiscalyear=True, sale=True, purchase=True, tax=True, hard=True)` | C1 | `tax=True` | C1,TH | `_get_lock_date_violations` checks `tax_lock_date` when `tax=True` by calling `_get_violated_soft_lock_date('tax_lock_date', date)`. Returns list of `(violated_date, field_name)` tuples. Called from `_get_violated_lock_dates` with `tax=has_tax`. | Multi-type lock date violation checker including tax period |
| U124-C05 | F-TAXLOCK-CHECK | `account/models/account_move_line.py:1526-1543` | `def _check_tax_lock_date(self)` | C1 | `line._affect_tax_report()` | C1,TH | `_check_tax_lock_date` iterates posted move lines; for each line that `_affect_tax_report()` (has `tax_ids`, `tax_line_id`, or tax `tax_tag_ids`), calls `company._get_lock_date_violations(move.date, fiscalyear=False, sale=False, purchase=False, tax=True, hard=True)`. Raises `UserError` with lock date info if violated. | Tax lock date hard-enforcement on posted journal entry lines |
| U124-C06 | F-TAXLOCK-TRIGGER-WRITE | `account/models/account_move.py:3950-3956` | `move.line_ids._check_tax_lock_date()` | C1 | posted move, date/state/name change | C1,TH | In `account.move.write`, when a posted move has its `name`, `date`, or `state` changed, `_check_tax_lock_date()` is called on all move lines before and after the ORM write. | Tax lock enforcement on journal entry date or state change |
| U124-C07 | F-TAXLOCK-TRIGGER-WRITE2 | `account/models/account_move.py:4001-4002` | `posted_move.line_ids._check_tax_lock_date()` | C1 | post after date change | C1,TH | After the ORM write in `account.move.write`, any move that ends up in posted state has its lines re-checked against the tax lock date. | Post-write tax lock date re-verification on all posted moves |
| U124-C08 | F-TAXLOCK-TRIGGER-CREATE | `account/models/account_move_line.py:1794-1795` | `lines._check_tax_lock_date()` | C1 | `ignore_tax_lock_date` not sentinel | C1,TH | In `account.move.line.create`, after ORM creation, `_check_tax_lock_date()` is called unless context key `ignore_tax_lock_date` equals the module-private `_ignore_tax_lock_date` sentinel object defined at line 17. | Tax lock enforcement on creation of new journal entry lines |
| U124-C09 | F-TAXLOCK-TRIGGER-UNLINK | `account/models/account_move_line.py:2001-2004` | `self._check_tax_lock_date()` | C1 | `ignore_tax_lock_date` not sentinel | C1,TH | In `account.move.line.unlink`, `_check_tax_lock_date()` is called before deletion unless the sentinel context key is set. | Tax lock enforcement on deletion of journal entry lines |
| U124-C10 | F-TAXLOCK-TRIGGER-WRITE3 | `account/models/account_move_line.py:1882,1888,1925` | `_check_tax_lock_date()` | C1 | write with tax-affecting fields | C1,TH | In `account.move.line.write`, `_check_tax_lock_date()` is called on `tax_lock_check_ids` both before and after the ORM write, and on statement lines during unreconcile operations. | Tax lock enforcement on journal entry line write operations |
| U124-C11 | F-TAXLOCK-MESSAGE | `account/models/account_move.py:745,1932-1936` | `tax_lock_date_message = fields.Char(compute='_compute_tax_lock_date_message')` | C1 | draft/posted move with date in locked period | C1,TH | `account.move.tax_lock_date_message` computes `_get_lock_date_message(accounting_date, affects_tax_report)` which returns a warning string if any lock dates are violated, naming the lock dates and the rescheduled accounting date. | Tax lock date warning message on journal entry form |
| U124-C12 | F-TAXLOCK-ALERT | `account/models/account_move.py:2464-2467` | `alerts['account_tax_lock_date'] = {... 'message': self.tax_lock_date_message}` | C1 | `has_account_group and self.tax_lock_date_message` | C1,TH | The `_get_move_display_info` (or alerts) method populates an `account_tax_lock_date` alert entry when `tax_lock_date_message` is non-empty, shown to users with the `group_account_user` group. | UI alert for tax period lock date on journal entry |
| U124-C13 | F-TAXLOCK-RESCHEDULING | `account/models/account_move.py:6714-6751` | `def _get_accounting_date(self, invoice_date, has_tax, lock_dates=None)` | C1 | lock dates violated | C1,TH | `_get_accounting_date` advances the accounting date past the latest violated lock date (`lock_dates[-1][0] + timedelta(days=1)`) and then rounds up to end-of-month or end-of-year depending on sequence format. This auto-rescheduling applies to tax lock date violations when `has_tax=True`. | Automatic date rescheduling past tax lock date on posting |
| U124-C14 | F-TAXLOCK-EXCEPTION | `account/models/account_lock_exception.py:54,79-82,149-150` | `('tax_lock_date', 'Tax Return Lock Date')` in selection; `tax_lock_date` computed field with `_search_tax_lock_date` | C1 | Active exception for user | C1 | `account.lock_exception` model supports `lock_date_field='tax_lock_date'`. Creates a temporary relaxation of the tax lock date for a specific user or all users, with optional `end_datetime`. The `_get_user_lock_date` method in company searches for such exceptions. | Per-user temporary exception to tax period lock date |
| U124-C15 | F-TAXLOCK-SOFT-LIST | `account/models/company.py:57-67` | `SOFT_LOCK_DATE_FIELDS = ['fiscalyear_lock_date', 'tax_lock_date', 'sale_lock_date', 'purchase_lock_date']` | C1 | Always | C1 | Five lock date types exist in Community: `fiscalyear_lock_date` (Global), `tax_lock_date` (Tax Return), `sale_lock_date` (Sales), `purchase_lock_date` (Purchase), `hard_lock_date` (Hard, irreversible). Only the first four are "soft" (can have exceptions). | Five-type lock date taxonomy in Community accounting |
| U124-C16 | F-TAXLOCK-VALIDATE | `account/models/company.py:552-605` | `def _validate_locks(self, values)` | C1 | Always | C1 | `_validate_locks` is called from `res.company.write`. It validates hard_lock_date changes (cannot decrease), checks for draft entries in hard-locked period, and checks for unreconciled bank statement lines. Note: **no specific validation** for decreasing `tax_lock_date` — soft lock dates can be rolled back. | Lock date change validation on company write |
| U124-C17 | F-TAXLOCK-AFFECT-TAX | `account/models/account_move_line.py:1522-1524` | `def _affect_tax_report(self): return self.tax_ids or self.tax_line_id or self.tax_tag_ids.filtered(lambda x: x.applicability == "taxes")` | C1 | Always | C1,TH | A journal entry line affects the tax report if it has `tax_ids`, a `tax_line_id`, or `tax_tag_ids` with `applicability=="taxes"`. Only such lines trigger tax lock date enforcement. | Tax-affecting line detection for lock enforcement |
| U124-C18 | F-TAXLOCK-AFFECT-MOVE | `account/models/account_move.py:5315-5316` | `def _affect_tax_report(self): return any(line._affect_tax_report() for line in (self.line_ids | self.invoice_line_ids))` | C1 | Always | C1,TH | `account.move._affect_tax_report` returns True if any line (including invoice lines) affects the tax report. Used in `_compute_tax_lock_date_message` to determine whether the tax lock date warning is relevant. | Move-level tax report impact detection |
| U124-C19 | F-TAXLOCK-AUTOSET | `account/models/company.py:85` | `"The tax lock date is automatically set when the tax closing entry is posted."` (field help text only) | ABSENT | Tax closing entry post | GAP,C1 | The auto-set mechanism (advancing `tax_lock_date` when a tax period closing entry is posted) is **documented in the field help string** but no code implementing this auto-set is present in the Community `account` module. The triggering code is in a separate module (Enterprise or `account_tax_report`). In Community, `tax_lock_date` must be manually written via company settings. | Auto-advance of tax lock date on closing entry post — absent in Community |
| U124-C20 | F-TAXLOCK-POS | `point_of_sale/models/res_company.py:44-67` | `@api.constrains('fiscalyear_lock_date', 'tax_lock_date', ...) def validate_lock_dates(self)` | C1 | Open POS sessions | C1,TH | POS module adds a constraint on `res.company.tax_lock_date`: cannot advance the lock date if open POS sessions have `start_at` on or before `user_tax_lock_date`. Ensures POS closing entries can still be posted. | POS-session guard on tax lock date advancement |
| U124-C21 | F-TAXLOCK-TAX-TAGS-WIZ | `account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:25-32` | `tax_lock_date = self.company_id.tax_lock_date; wizard.date_from = tax_lock_date + timedelta(days=1)` | C1 | `tax_lock_date` set | C1 | The tax tag update wizard defaults `date_from` to `tax_lock_date + 1 day`, preventing retroactive tag updates in locked periods. Shows `display_lock_date_warning = True` if `date_from < tax_lock_date`. | Tax tag update wizard respects tax lock date boundary |

---

## Key Architecture Findings

### 5 Lock Date Types (Community)
- `fiscalyear_lock_date` — Global (affects all journals)
- `tax_lock_date` — Tax Return (affects tax-bearing entries only)
- `sale_lock_date` — Sales (affects sales journals only)
- `purchase_lock_date` — Purchase (affects purchase journals only)
- `hard_lock_date` — Hard lock (irreversible, no exceptions)

### Enforcement Chain (tax_lock_date)
1. `res.company.tax_lock_date` → set by accountant manually (Community) or automatically by tax closing entry (Enterprise)
2. `res.company.user_tax_lock_date` → computed effective date after applying `account.lock_exception` per user
3. `res.company._get_lock_date_violations(tax=True)` → called from move and line write/create/unlink
4. `account.move.line._check_tax_lock_date()` → raises `UserError` if any tax-affecting line falls in locked period
5. `account.move.tax_lock_date_message` → UI warning shown before posting

### GAP-027 Status
The gap was "L7 — not proven". This research proves:
- **PROVEN (C1)**: `tax_lock_date` field exists, is enforced at ORM layer, blocks write/post/delete on tax-bearing entries, has per-user exception support, and shows UI warnings.
- **ABSENT (Community)**: Auto-set on tax closing entry post — requires Enterprise `account_tax_report` module.
- **GAP-027: PARTIAL** — Core enforcement is proven (C1). Auto-set automation is absent in Community (requires separate module).

---

## File References

| File | Lines | Purpose |
|------|-------|---------|
| `account/models/company.py` | 57-67, 81-112, 421-426, 552-605, 607-710 | Lock date field definitions, computation, validation, violation checking |
| `account/models/account_move.py` | 745, 1932-1936, 2464-2467, 3950-3956, 4001-4002, 5315-5316, 6714-6751 | Move-level lock enforcement, rescheduling, alerts |
| `account/models/account_move_line.py` | 17, 1522-1524, 1526-1543, 1794-1795, 1882, 1888, 1925, 2001-2004 | Line-level lock enforcement, sentinel pattern, _affect_tax_report |
| `account/models/account_lock_exception.py` | 11-200 | Per-user lock exception model |
| `point_of_sale/models/res_company.py` | 44-67 | POS session guard on tax lock date |
| `account_update_tax_tags/wizard/account_update_tax_tags_wizard.py` | 25-32 | Tax tag wizard respects tax lock date |
