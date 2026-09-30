> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: cr_effective_date_entries

- Module: cr_effective_date_entries
- License (confirmed in manifest): AGPL-3 (cr_effective_date_entries/__manifest__.py:16)
- Author (manifest): SuitePark Info Tech (cr_effective_date_entries/__manifest__.py:5)
- Version (manifest): 19.0.0.0 (cr_effective_date_entries/__manifest__.py:3)
- Path: addons_Extramodule/addons_extra/cr_effective_date_entries
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Back-dating tool: from list/form of sales orders, purchase orders or transfers, a user opens a small dialog, picks a date/time and confirms; the module rewrites the dates of the selected document and its related stock and accounting records (wizard/effective_date.py:15-89; views/effective_date_action.xml:4-35). A red warning tells the user the change affects the order and related entries (wizard/effective_date_wiz_view.xml:14-16).
- Sale order branch: sets order date (wizard/effective_date.py:39-46). Purchase order branch: sets order date and confirmation date (lines 48-56). Transfer branch: re-dates stock moves, move lines, the transfer's scheduled/deadline/done dates, and re-dates and re-posts the linked accounting entries (lines 58-89).

## 2. Attachment to CORE
- `sale.order` and `purchase.order`: fields `date_order` (sale core:sale/models/sale_order.py:93; purchase core:purchase/models/purchase_order.py:88) and `date_approve` (core:purchase/models/purchase_order.py:90, read-only in core UI) are overwritten directly, after confirmation. ALTERS CORE CONTROL (confirmation-date/approval-date trail).
- `account.move` (linked entries): for each linked entry the wizard sends it back to draft, clears its number, sets a new accounting date and invoice date, and posts again (wizard/effective_date.py:62-68). ALTERS CORE CONTROL: posting and numbering (entry number is cleared and re-assigned on re-post; core control on draft/post, core:account/models/account_move.py:6180, 6269). Core lock-date checks are not bypassed in code read (core:account/models/account_move.py:2823-2835 applies on write/post), so a locked period may still block the wizard; effect not run.
- `stock.move` / `stock.move.line` / `stock.picking`: direct date rewriting of moves, move lines and the transfer completion date (wizard/effective_date.py:70-89), including on transfers already done. ALTERS CORE CONTROL: stock movement history dates.
- Valuation: for each valuation layer of the move, the creation timestamp is rewritten with a direct database statement outside the ORM (wizard/effective_date.py:74-77). ALTERS CORE CONTROL: valuation/cost history (bypasses ORM access rules and audit fields). Not reproduced here; see section 4 for whether the target exists in Community 19.
- Override `stock.picking._set_scheduled_date` (wizard/effective_date.py:11-13): REPLACES core behavior. Core version refuses changes on cancelled transfers, skips done transfers and updates the dates of stock moves (core:stock/models/stock_picking.py:925-931); the module version has none of those guards and updates move-line dates instead. Applies to every user and every transfer once the module is installed, not only to wizard use. ALTERS CORE CONTROL.
- Wizard `change_to_effective_date_wizard` only opens the dialog; a debug print of active ids remains (wizard/effective_date.py:24).

## 3. New objects, security, automation, external calls
- New model: transient wizard `effective_date.entries.wiz` (wizard/effective_date.py:15-20).
- Group "Change Effective Date" (security/security.xml:3-5); wizard ACL only for that group (security/ir.model.access.csv:2). No implied group, no category, no default members. No record rules.
- Three server actions bound to the Action menu of sales order, purchase order and stock transfer (list and form) (views/effective_date_action.xml:4-35); server actions carry no group restriction, so the entry appears to all users but the wizard model is accessible only to the group above.
- Crons: none. External calls: none.

## 4. Odoo 19 compatibility
- Checked by grep in Community tree.
- MISMATCH: model `stock.valuation.layer` (wizard/effective_date.py:74) has no model definition in Community 19 addons (only mentions in tests/demo/docstrings; core:stock_account/models/stock_lot.py:91 mentions the phrase in a helper docstring). The transfer branch would fail when it looks up the model.
- MISMATCH: `account.move.stock_move_id` (wizard/effective_date.py:62) not defined; Community 19 has `account.move.stock_move_ids` (core:stock_account/models/account_move.py:8) and `stock.move.account_move_id` (core:stock_account/models/stock_move.py:51).
- Suspect logic: lists of recordsets are passed where ids are expected (wizard/effective_date.py:41-44, 50-53); not run, likely errors. In the transfer branch `invoice_ids` is False so the branch loops all linked entries.
- Present in core 19: `stock.picking.date_deadline`, `date_done`, `scheduled_date` inverse `_set_scheduled_date` (core:stock/models/stock_picking.py:595-606, 925), `sale.order.invoice_ids`, `purchase.order.invoice_ids`.

## 5. Custom-to-custom dependencies
- None declared (depends: stock, account, sale, purchase; manifest:7-9).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether period lock dates and fiscal-year locks are respected end-to-end in the wizard (depends on runtime and company settings).
- UNKNOWN - EVIDENCE INSUFFICIENT: how the customer intends valuation entries to be re-dated in the 19 valuation model, given the layer model is absent.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether users outside the group can trigger the global `_set_scheduled_date` replacement through normal transfer editing (it is unconditional in code, wizard/effective_date.py:11).
- UNKNOWN - EVIDENCE INSUFFICIENT: intended treatment of invoices/bills of sale and purchase branches (variables computed but not used afterwards, lines 41-44, 50-53).
