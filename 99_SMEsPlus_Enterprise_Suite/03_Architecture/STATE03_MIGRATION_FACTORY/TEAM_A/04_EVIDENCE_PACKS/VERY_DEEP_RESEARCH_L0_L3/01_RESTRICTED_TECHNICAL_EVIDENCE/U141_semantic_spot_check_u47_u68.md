# U141 — Semantic Spot-Check U47–U68 (GAP-045)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: CLAUDE-VERIFIED
- Unit: U141
- Gap addressed: GAP-045 (U47–U68 GATE_PASS_ONLY — zero semantic review)
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope: 25 semantic verifications across 5 evidence files in the U47–U68 range

---

## METHODOLOGY

Units selected: U47 (78 KB), U62 (75 KB), U57 (74 KB), U50 (69 KB), U64 (45 KB).
Five claims with specific file:line pointers selected from each unit.
Each claim verified by reading the actual source file at the stated line range.
Classification: C1 = source-verified (file exists, line valid, anchor matches, statement accurate);
PARTIAL = approximately correct but minor inaccuracy; FAIL = wrong or absent.

---

## VERIFICATION RESULTS

### U47 — account_bank_statement_line.py and related files

**Claim U47-V1** — `account/models/account_bank_statement_line.py:278–280`
Evidence: `_compute_internal_index` encodes date + complement-of-sequence + id as a string using MAXINT=2147483647.
Verification: Lines 278–280 read:
```
st_line.internal_index = f'{st_line.date.strftime("%Y%m%d")}' \
                          f'{MAXINT - st_line.sequence:0>10}' \
                          f'{st_line._origin.id:0>10}'
```
Result: C1 — formula matches exactly; `st_line.` prefix is the loop-variable form of the shorthand in evidence.

**Claim U47-V2** — `account/models/account_bank_statement_line.py:390`
Evidence: On `create`, `move_type` is forced to `'entry'` (line 390).
Verification: Line 390: `vals['move_type'] = 'entry'` with comment "Force the move_type to avoid inconsistency".
Result: C1 — exact match.

**Claim U47-V3** — `account/models/account_bank_statement_line.py:420`
Evidence: `action_post()` is automatically called (line 420).
Verification: Line 420: `st_lines.move_id.action_post()` with comment "No need for the user to manage their status".
Result: C1 — exact match.

**Claim U47-V4** — `account/models/res_currency.py:123–140`
Evidence: `_create_currency_table` creates a `TEMPORARY TABLE account_currency_table ON COMMIT DROP` with an index and ANALYZE.
Verification: Lines 123–140 contain `CREATE TEMPORARY TABLE account_currency_table ... ON COMMIT DROP`, `CREATE INDEX account_currency_table_index ...`, and `ANALYZE account_currency_table`.
Result: C1 — exact match.

**Claim U47-V5** — `account/wizard/accrued_orders.py:24`
Evidence: `_get_default_date` returns the last day of the previous month using `date_utils.get_month(today)[0] - relativedelta(days=1)`.
Verification: Line 24: `return date_utils.get_month(fields.Date.context_today(self))[0] - relativedelta(days=1)`
Result: C1 — semantically exact; evidence used `today` as shorthand for `fields.Date.context_today(self)`.

---

### U50 — base module remaining (ir_module, ir_ui_view, ir_qweb)

**Claim U50-V1** — `base/models/ir_module.py:140`
Evidence: `STATES` constant at line 140 defines the six states.
Verification: Line 140: `STATES = [('uninstallable',...), ('uninstalled',...), ('installed',...), ('to upgrade',...), ('to remove',...), ('to install',...)]` — six entries.
Result: C1 — exact match.

**Claim U50-V2** — `base/models/ir_module.py:57–73`
Evidence: `assert_log_admin_access` decorator raises `AccessDenied` if `env.is_admin()` is False.
Verification: Lines 57–73 define the decorator; line 68: `if not self.env.is_admin():`, line 70: `raise AccessDenied()`.
Result: C1 — exact match.

**Claim U50-V3** — `base/models/ir_ui_view.py:209`
Evidence: `_compute_arch` reads from file in dev-xml mode when `arch_updated` is False.
Verification: Line 209: `def _compute_arch(self):`; line 225: `'xml' in config['dev_mode'] and not view.arch_updated` controls file reading.
Result: C1 — exact match.

**Claim U50-V4** — `base/models/ir_ui_view.py:724`
Evidence: `_get_inheriting_views` uses a recursive CTE.
Verification: Line 724: `def _get_inheriting_views(self):`; lines 742–: `WITH RECURSIVE ir_ui_view_inherits AS (...)`.
Result: C1 — exact match.

**Claim U50-V5** — `base/models/ir_qweb.py:423`
Evidence: `_SAFE_QWEB_OPCODES` constant at line 423 is a whitelist of Python bytecodes.
Verification: Line 423: `_SAFE_QWEB_OPCODES = _EXPR_OPCODES.union(to_opcodes([...]))` with comment "security safe eval opcodes".
Result: C1 — exact match.

---

### U57 — stock module remaining

**Claim U57-V1** — `stock/models/stock_lot.py:25`
Evidence: `_name = 'stock.lot'` with `_check_company_auto = True`.
Verification: Line 25: `_name = 'stock.lot'`; line 28: `_check_company_auto = True`.
Result: C1 — exact match.

**Claim U57-V2** — `stock/models/stock_rule.py:31–39`
Evidence: `Procurement` is a `NamedTuple` with fields `product_id, product_qty, product_uom, location_id, name, origin, company_id, values`.
Verification: Lines 31–39 confirm class definition and all eight typed fields.
Result: C1 — exact match.

**Claim U57-V3** — `stock_picking_batch/models/stock_picking_batch.py:60`
Evidence: `is_wave = fields.Boolean('This batch is a wave')`.
Verification: Line 60: `is_wave = fields.Boolean('This batch is a wave')`.
Result: C1 — exact match.

**Claim U57-V4** — `stock_picking_batch/models/stock_picking_batch.py:185–186`
Evidence: `sequence_code = 'picking.wave' if vals.get('is_wave') else 'picking.batch'`.
Verification: Line 186: `sequence_code = 'picking.wave' if vals.get('is_wave') else 'picking.batch'`.
Result: C1 — exact match.

**Claim U57-V5** — `stock/models/stock_scrap.py:152–163`
Evidence: `do_scrap` gets a sequence reference, creates and executes a scrap move with context `is_scrap=True`, then conditionally calls `do_replenish()`.
Verification: Lines 152–163 confirm: `ir.sequence.next_by_code('stock.scrap')`, `_create_scrap_move()`, `move.with_context(is_scrap=True)._action_done()`, `if scrap.should_replenish: scrap.do_replenish()`.
Result: C1 — exact match.

---

### U62 — account_peppol module

**Claim U62-V1** — `account_peppol/models/res_company.py:70–79`
Evidence: `account_peppol_proxy_state` tracks five states: `not_registered`, `sender`, `smp_registration`, `receiver`, `rejected`.
Verification: Lines 70–79 define the Selection field with exactly those five values.
Result: C1 — exact match.

**Claim U62-V2** — `account_peppol/models/res_company.py:29–51`
Evidence: `PEPPOL_ENDPOINT_RULES` and `PEPPOL_ENDPOINT_WARNINGS` (hard and soft validation) with rules for EAS codes 0007, 0088, 0184, 0192, 0208.
Verification: Lines 29–51 define `PEPPOL_ENDPOINT_RULES` (0007, 0088, 0184, 0192, 0208), `PEPPOL_ENDPOINT_WARNINGS` (0151, 0201, 0210, 0211, 9906, 9907), and `PEPPOL_ENDPOINT_SANITIZERS`.
Result: C1 — exact match.

**Claim U62-V3** — `account_peppol/tools/peppol_iap_connector.py:12–15`
Evidence: `PEPPOL_PROXY_URLS = {'prod': 'https://peppol.api.odoo.com', 'test': 'https://peppol.test.odoo.com'}`.
Verification: Lines 12–15 show exactly that dict definition.
Result: C1 — exact match.

**Claim U62-V4** — `account_peppol/models/account_edi_proxy_user.py:17`
Evidence: `BATCH_SIZE = 50` (documents per cron run).
Verification: Line 17: `BATCH_SIZE = 50`.
Result: C1 — exact match.

**Claim U62-V5** — `account_peppol/models/account_move.py:16–28`
Evidence: `peppol_move_state` selection with states `ready, to_send, skipped, processing, done, error`.
Verification: Lines 16–28 define the Selection field with all six stated values.
Result: C1 — exact match.

---

### U64 — point_of_sale session lifecycle

**Claim U64-V1** — `point_of_sale/models/pos_session.py:372`
Evidence: `action_pos_session_open` at line 372 opens sessions in `opening_control` state and reads last session balance.
Verification: Line 372: `def action_pos_session_open(self):`, logic matches: filters `opening_control`, reads `cash_register_balance_end_real` from last session.
Result: C1 — exact match.

**Claim U64-V2** — `point_of_sale/models/pos_session.py:388`
Evidence: `action_pos_session_closing_control` at line 388 transitions state to `closing_control`.
Verification: Line 388: `def action_pos_session_closing_control(self, ...):`, line 396: `session.write({'state': 'closing_control', ...})`.
Result: C1 — exact match.

**Claim U64-V3** — `point_of_sale/models/pos_session.py:424`
Evidence: `_validate_session` at line 424, calls `_check_if_no_draft_orders` and `_check_invoices_are_posted`.
Verification: Line 424: `def _validate_session(self, ...):`, lines 434–435 call both check methods.
Result: C1 — exact match.

**Claim U64-V4** — `point_of_sale/models/pos_session.py:312`
Evidence: `_check_pos_config` at line 312 prevents more than one non-rescue open session.
Verification: Line 312: `def _check_pos_config(self):`, raises `ValidationError` if count > 1.
Result: C1 — exact match.

**Claim U64-V5** — `point_of_sale/models/pos_session.py:872`
Evidence: `_create_account_move` at line 872 creates `account.move` keyed to `config_id.journal_id`.
Verification: Lines 872–884: `def _create_account_move(self, ...):`, `self.env['account.move'].create({'journal_id': self.config_id.journal_id.id, ...})`.
Result: C1 — exact match.

---

## SUMMARY

| File | Claims | C1 | PARTIAL | FAIL |
|------|--------|-----|---------|------|
| U47 | 5 | 5 | 0 | 0 |
| U50 | 5 | 5 | 0 | 0 |
| U57 | 5 | 5 | 0 | 0 |
| U62 | 5 | 5 | 0 | 0 |
| U64 | 5 | 5 | 0 | 0 |
| **TOTAL** | **25** | **25** | **0** | **0** |

**GAP-045 STATUS: CLOSED** — All 25 sampled pointers in the U47–U68 range confirmed valid. No fabricated claims detected. All line-number references were exact or semantically equivalent. The U47–U68 evidence is of equivalent quality to U01–U46 (verified by U130).
