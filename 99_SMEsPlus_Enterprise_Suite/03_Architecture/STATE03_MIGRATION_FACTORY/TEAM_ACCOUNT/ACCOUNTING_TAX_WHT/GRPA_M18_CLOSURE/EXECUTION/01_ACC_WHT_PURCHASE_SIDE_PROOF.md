# Purchase-Side Withholding Tax — Accounting Process Proof

## Session Metadata

| Field | Value |
|---|---|
| Deliverable | `01_ACC_WHT_PURCHASE_SIDE_PROOF.md` |
| Team | Team A1 — Purchase-side WHT Proof Team |
| Repo | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Branch | `audit/account-wht-grpa-m18-closure-010` |
| Evidence base | CORR-007A, commit `deceb7339b39eba309236782f159f8393224f5fd`, branch `audit/inventory-core-corr007a-grpa-m18-wht-50twi-009` (50-twi print module audit — out of scope here, referenced only) |
| Report date | 2026-09-02 |
| Mode | Evidence-first / clean-room / **no development authorization** |
| Source tree examined (read-only) | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE/addons_extra/` (Odoo Thai-localization addons — REFERENCE tree only, not the SMEsPlus target architecture) |
| Scope | Purchase-side (vendor) withholding-tax accounting process: configuration → bill → payment → GL posting → certificate linkage → PND3/PND53 boundary |
| Out of scope | 50-twi certificate PRINT layout gaps (owned by CORR-007A / parallel team), deep audit of `tax_report_pnd.py` filing logic (owned by another team), Gate PASS declaration, Team B/C authorization |

**Governing constraints applied:** every claim below is cited to an exact file path and line range, with a SHA-256 of the file computed via `shasum -a 256` at the time of this audit. Where the source does not contain a feature, this document says **NOT FOUND** rather than inferring intent. No statement in this document constitutes a declaration of Thai Revenue Department statutory compliance — anything requiring that judgment is explicitly flagged for legal/tax review.

---

## 1. Module Identity & Dependency Chain

### 1.1 Primary module: `l10n_th_withholding_tax`

File: `addons_extra/l10n_th_withholding_tax/__manifest__.py`
SHA-256: `903d9061ba5c16e68f0155309edb263088f1b5253b93ff8dc3b8bf3de12f1995`

- Name: "Thai Localization - Withholding Tax", version `19.0.1.4` (line 6)
- `depends`: `["account", "l10n_th_reports"]` (line 11)
- `data` (line 12–20): `security/security.xml`, `security/ir.model.access.csv`, `wizard/account_payment_register_views.xml`, `views/account_view.xml`, `views/account_move_view.xml`, `views/account_withholding_tax.xml`, `views/product_view.xml`

This confirms the module depends directly on core `account` (standard Odoo accounting) and on `l10n_th_reports` (the Thailand accounting-reports package that supplies the PND report engine — see §6).

### 1.2 Downstream (forward) dependents

Located via `grep -rl "l10n_th_withholding_tax" --include="__manifest__.py"` across the full `addons_extra` tree:

| Module | Depends on `l10n_th_withholding_tax`? | Purpose (from manifest) |
|---|---|---|
| `l10n_th_withholding_tax_cert` | Yes — `addons_extra/l10n_th_withholding_tax_cert/__manifest__.py` line 11 (`"depends": ["l10n_th_withholding_tax"]`) | Withholding Tax Certificate (50-twi) data model — audited in depth by CORR-007A; only the linkage points are examined here (§5) |
| `l10n_th_withholding_tax_multi` | Yes — `addons_extra/l10n_th_withholding_tax_multi/__manifest__.py` line 11 (`"depends": ["l10n_th_withholding_tax", "account_payment_multi_deduction"]`) | Multi-line WHT support for payments with several WHT lines/products in one bill |
| `l10n_th_withholding_tax_report` | Yes — `addons_extra/l10n_th_withholding_tax_report/__manifest__.py` line 8–14 (depends on `l10n_th_withholding_tax_cert`, `l10n_th_partner`, `date_range`, `report_xlsx_helper`, `account`) — SHA-256 `6944ca4421e3dea353304ea3526a6fdcdac68c08f33c6bbf48b5ab77a7603204` | Standalone xlsx/report wizard for withholding tax reporting, distinct from the built-in `l10n_th_reports` PND engine |
| `l10n_th_withholding_tax_cert_form` | Yes — `addons_extra/l10n_th_withholding_tax_cert_form/__manifest__.py` line 8 (`"depends": ["web", "l10n_th_withholding_tax_cert", "l10n_th_amount_to_text"]`) — SHA-256 `dfc9a1978d6072fe5c8310e798f4a4c81527140fe3d45b22b51861255d5c8bd9` | The 50-twi PRINT layout module — this is the module CORR-007A already audited; NOT re-audited here |

### 1.3 `l10n_th_reports` (upstream dependency)

File: `02 OTHER/l10n_th_reports/__manifest__.py`
SHA-256: `e5018a7020328dc6ace63e2e3e2d13c1775a58d372bf042372851a0778a88c93`

- `depends`: `["l10n_th", "account_reports"]`, `auto_install: True`
- Contains `models/tax_report_pnd.py` (SHA-256 `346ab7b52ddba341accac959369439d7b249167db6e882a3ffaafd0eba62a33f`, 145 lines) which defines the abstract base model `l10n_th.pnd.report.handler`. `l10n_th_withholding_tax/models/tax_report_pnd.py` (§6) inherits and extends this model's `_rows` method — this is the concrete module boundary between the accounting-process module and the PND3/PND53 filing engine.

### 1.4 Secondary module: `l10n_th_withholding_tax_multi`

File: `addons_extra/l10n_th_withholding_tax_multi/__manifest__.py`, SHA-256 `01c6c0558fd7230d055469325c8f386317b34dcd985518f3a2b975293b0bf8e5`
- `depends`: `["l10n_th_withholding_tax", "account_payment_multi_deduction"]` (line 11)
- Adds support for **multiple** WHT deduction lines on a single payment (via `account.payment.deduction`, an OCA `account_payment_multi_deduction` model), where the base module only cleanly supports one WHT rate per payment ("Useful for case 1 tax only" — see §4.2 and §4.4).

---

## 2. Purchase-Side Business Process Trace

### 2.1 Step 1 — How is WHT "applicability" configured?

**Finding: there is NO partner-level "subject to withholding tax" flag.** WHT applicability is configured at the **product** level and/or applied **manually at the invoice-line / payment level**. This was verified by an explicit grep:

```
grep -rn "res\.partner|res_partner|partner_id\.|is_company" l10n_th_withholding_tax/models l10n_th_withholding_tax/wizard l10n_th_withholding_tax/views
```

Result: the only `res.partner` touchpoints are:
- `models/account_move.py:66` — `if rec.partner_id.is_company:` — used only to decide which **pool** of WHT tax records (`account.withholding.tax`) to offer in the line's selection domain (company vendor → PND53-tagged pool; individual vendor → PND3-tagged pool). This gates *which rate list is shown*, not *whether WHT applies at all*.
- `models/tax_report_pnd.py:47–50, 82–85` — `res_partner` / `res_partner_company_type` joined purely to pull address/VAT/company-type display fields for the PND report output (§6), not a configuration flag.

There is **no `partner.py` or `res_partner.py` file** in `l10n_th_withholding_tax` at all (`find l10n_th_withholding_tax -iname "*partner*"` returned nothing).

Actual configuration mechanism, in order of how a WHT tax record is even created:

1. **Account-level flag** — `account.account.wt_account` (Boolean), `addons_extra/l10n_th_withholding_tax/models/account.py:12–16`. Marks a GL account as eligible to be used as a WHT payable/asset account. Enforced by a `@api.constrains("account_id")` on `account.withholding.tax` (`models/account_withholding_tax.py:28–32`) which raises `ValidationError` if the account isn't flagged.
2. **Tax-level flag** — `account.tax.wt_tax` (Boolean), `models/account.py:22–26`. When set, `create()`/`write()`/`toggle_active()` overrides (`models/account.py:28–37, 101–109`) auto-generate/sync a matching `account.withholding.tax` record via `update_wt()` (`models/account.py:48–99`).
3. **Product-level WHT tax assignment (purchase side)** — `product.template.supplier_wt_tax_id`, a `Many2one` to `account.withholding.tax`, `addons_extra/l10n_th_withholding_tax/models/product.py:10`. This is the field that determines default WHT on a **vendor bill**.
4. **Manual override at the invoice line** — `account.move.line.wt_tax_id`, `models/account_move.py:9–15`, is a stored, non-readonly `Many2one` computed field (`compute="_compute_wt_tax_id", store=True, readonly=False` — i.e., it defaults from the product but a user can change it per line).
5. **Manual override at payment time** — `account.payment.wt_tax_id` and `account.payment.register.wt_tax_id` (§4).

**Conclusion for Q1:** WHT is a product/tax-config-driven and line-level-editable attribute, not a partner attribute. `partner_id.is_company` only narrows which WHT-rate pool is offered (PND3 vs PND53 segregation), confirmed at `models/account_move.py:52–83`.

### 2.2 Step 2 — Rate/amount computation

Rate source: `account.withholding.tax.amount` (Float, percentage), `models/account_withholding_tax.py:20–22`. Not tied to the product's price list or a percentage-of-tax-base computed elsewhere — it is a flat, manually configured percentage per `account.withholding.tax` record (e.g., "Withholding Tax 3%" with `amount = 3`, confirmed by test fixture `tests/account_withholding_tax_test.xml:8–12`).

Computation formula, cited twice in the codebase:
- On the bill (informational aggregate): `account.move.wht_amount`, computed field, `models/account_move.py:34, 105–117`:
  ```python
  rec.wht_amount = sum(inv_lines.mapped(lambda l: l.wt_tax_id.amount / 100 * l.price_subtotal))
  ```
  (line 115–117) — i.e. `rate% × line price_subtotal`, summed across invoice lines that carry a `wt_tax_id`.
- At payment time (the value that actually drives the write-off/GL line): `wizard/account_payment_register.py:50–52`:
  ```python
  amount_wt = sum(inv_lines.mapped(lambda l: l.wt_tax_id.amount / 100 * l.price_subtotal))
  ```
  identical formula, then reduced by any WHT already paid on prior partial payments (lines 54–57, walking `move.matched_payment_ids` and their posted `move_line_ids` that carry `wt_tax_id`).

**Conclusion for Q2:** rate source = `account.withholding.tax.amount` (flat %, manually configured, optionally auto-synced from a flagged `account.tax` record); base = invoice line `price_subtotal` (i.e., tax-exclusive line amount); no product-cost or FX-rate-dependent computation found.

### 2.3 Step 3 — Does the vendor bill (`account.move`, `move_type = in_invoice`) get affected directly?

**Finding: WHT is recorded on the bill as a reference field only — it does NOT create a separate GL line on the bill itself.** Evidence:

- `account.move.line.wt_tax_id` (`models/account_move.py:9–15`) is set on the invoice line but is **not** one of the tax computation fields that Odoo's standard `_compute_totals`/`_compute_tax_ids` machinery turns into a debit/credit line at bill-posting time; it exists purely as a data-carrying field consumed later, at payment time (§2.4) and by the PND report SQL (§6).
- `account.move.wht_amount` (`models/account_move.py:34`) is a **computed, non-stored-to-ledger** Float — it is a UI-visible read-only aggregate (`views/account_move_view.xml:38–40`, marked `invisible="1"` in the form but present in the view tree), not a journal entry.
- No `account.move.line` create/write override was found that inserts an extra WHT credit/debit line during `action_post()` of the bill itself. `models/account_move.py` contains no `action_post` override at all (confirmed by reading the full 117-line file — only `_compute_wt_tax_id`, `_compute_tax_domain`, `_compute_wht_amount` are defined).
- `account_tax.py` (`models/account_tax.py`, full file, 32 lines) only hooks `_add_accounting_data_to_base_line_tax_details` and `_prepare_base_line_grouping_key` — these inject **tax-grid tags** (`tax_tag_ids`) for reporting purposes onto the base line, not an actual WHT payable/receivable GL line.

**Conclusion for Q3:** WHT is **applied only at payment time**, not at bill-posting time. The bill (`in_invoice`) carries a WHT *marker* (`wt_tax_id` per line, `wht_amount` aggregate) that is read later by the payment-registration flow — it does not itself generate a WHT payable journal entry.

### 2.4 Step 4 — "Payment net of WHT": trace of `account_payment.py` and the payment-register wizard

This is the operative mechanism, confirmed by both source code and the module's own passing unit tests.

**Field carriers:**
- `account.payment.wt_tax_id` — `addons_extra/l10n_th_withholding_tax/models/account_payment.py:9–13`, docstring: *"Optional hidden field to keep wt_tax. Useful for case 1 tax only"*.
- `account.payment.register.wt_tax_id` — `wizard/account_payment_register.py:10–14`, same docstring, on the transient wizard model.

**Mechanism — `wizard/account_payment_register.py`:**

1. `_compute_amount()` override (lines 30–72) fires when the wizard is opened from `account.move.line` (`self._context.get("active_model") == "account.move.line"`, line 45).
2. It sums `wt_tax_id.amount/100 * price_subtotal` across the WHT-flagged lines being paid (lines 47–52), then **subtracts any WHT already deducted on prior partial payments of the same move** (lines 54–57).
3. If `amount_wt` is non-zero (line 59): `self.amount -= amount_wt` (line 60) — **the payment amount is reduced by the WHT amount**; `self.show_payment_difference = True` (line 62) forces Odoo's standard "payment difference" UI/logic to activate; if there is exactly one distinct WHT rate involved, `self.wt_tax_id`, `self.writeoff_account_id = self.wt_tax_id.account_id`, and `self.writeoff_label = self.wt_tax_id.display_name` are set (lines 64–67) — i.e. the WHT amount is routed through Odoo's native **write-off line** mechanism, targeting the WHT `account.account` configured on the `account.withholding.tax` record.
4. `_compute_payment_difference_handling()` (lines 89–93) forces `payment_difference_handling = 'reconcile'` whenever `wt_tax_id` is set — this is what causes Odoo core to actually generate the write-off journal item when the payment is created.
5. `_create_payment_vals_from_wizard()` (lines 16–26) — when `payment_difference_handling == "reconcile"` and `wt_tax_id` is set, tags the resulting `write_off_line_vals` with `tax_tag_ids = self.wt_tax_id.tax_tag_ids.ids` (lines 21–25) — this is what makes the WHT write-off line show up correctly in the tax-grid-driven PND report (§6).

**Confirmed empirically by the module's own test suite** (`tests/test_withholding_tax.py`, SHA-256 `5e112150b36b2f1ce2dd86f04b0635782691b125a0b20f7c5851fb1f5a2a3af5`, 220 lines):
- `test_01_create_payment_withholding_tax` (lines 104–159): creates an `in_invoice` for 100.0, sets `wt_tax_id` = 3% WHT on the line (line 124), posts it, opens the payment-register wizard, and asserts:
  - `register_payment.writeoff_account_id == invoice_id.invoice_line_ids.wt_tax_id.account_id` (lines 148–151) — write-off targets the configured WHT account.
  - `register_payment.payment_difference == price_unit * 0.03` (line 152) — the deducted amount is exactly 3% of 100.
  - `payment_id.amount == price_unit * 0.97` (line 159) — **the actual posted payment is net of WHT (97, not 100)**.
- `test_02_create_payment_withholding_tax_product` (lines 161–200): identical assertions, but the WHT is sourced from `product.supplier_wt_tax_id` instead of a manual line edit — confirms product-level auto-fill (§2.1 item 3) flows through to the same net-payment mechanism.

**Multi-WHT variant (`l10n_th_withholding_tax_multi`):** `models/account_payment.py` (SHA-256 `3a1dfd190766e026a670af4cc262b741a3c44701cd718ae80384590abeda6307`) generalizes step 3 above using `account.payment.deduction` records instead of a single write-off (`_update_vals_multi_deduction`, lines 37–82): each distinct `wt_tax_id` on the paid lines becomes its own deduction row with `account_id = wt.account_id`, `amount = wt.amount/100 * line.price_subtotal` net of amounts already paid (lines 53–81), routed through `_prepare_deduct_move_line` (lines 85–92) which also carries `tax_tag_ids` and a new `wt_move_line` back-reference (`models/account_payment.py:122–124`, added to `account.move.line`).

**Conclusion for Q4:** Yes — the payment amount is reduced by the WHT amount, and a separate journal line (a "write-off"/"deduction" line targeting the configured WHT `account.account`) is created as part of the **same** `account.payment` journal entry generated by `action_create_payments()`. It is not a fully separate `account.move`; it is an additional line on the payment's own move, distinguished by `account_id` (the WHT account) and (for case-1 single-rate) `wt_tax_id`/`tax_tag_ids` metadata, or (for multi-rate) via `account_payment_deduction` records feeding additional move lines.

### 2.5 Step 5 — GL accounts touched

See §3 (GL Account Mapping Table) for the consolidated view. Field-level citations:

- `account.account.wt_account` (Boolean) — `models/account.py:12–16` — flags an account as eligible to hold WHT postings.
- `account.withholding.tax.account_id` (Many2one → `account.account`, `domain=[("wt_account", "=", True)]`, `required=True`, `ondelete="restrict"`) — `models/account_withholding_tax.py:12–18` — this is **the** field that determines which GL account receives the WHT write-off/deduction credit at payment time (consumed at `wizard/account_payment_register.py:66` as `self.writeoff_account_id = self.wt_tax_id.account_id`).
- The vendor's own payable account (`account.account` with `internal_type = 'payable'`) — standard Odoo core field, not redefined by this module; it is debited/credited as normal by the underlying `account.payment`/`account_payment_register` core logic, reduced by the WHT write-off.

---

## 3. GL Account Mapping Table

| Role | Field | Type | Defining file : line | Notes |
|---|---|---|---|---|
| WHT-eligible account flag | `account.account.wt_account` | Boolean | `models/account.py:12` | Gate on which accounts can be chosen as a WHT account; enforced by `account.withholding.tax._check_account_id` constraint (`models/account_withholding_tax.py:28–32`) |
| WHT rate/account config record | `account.withholding.tax.account_id` | Many2one → `account.account` | `models/account_withholding_tax.py:12–18` | `domain=[("wt_account", "=", True)]`, `ondelete="restrict"` |
| WHT rate | `account.withholding.tax.amount` | Float (%) | `models/account_withholding_tax.py:20–22` | Flat percentage, not tax-bracket-computed |
| WHT type (segregates PND pools) | `account.withholding.tax.type` | Selection (`sale`/`purchase`/`none`) | `models/account_withholding_tax.py:19` | Used by `_compute_tax_domain` in `models/account_move.py:59–83` to filter which WHT records are offered per move-type/partner |
| Tax-grid tag(s) for reporting | `account.withholding.tax.tax_tag_ids` | Many2many → `account.account.tag` | `models/account_withholding_tax.py:23` | Propagated onto the payment write-off line via `wizard/account_payment_register.py:21–25` |
| Line-level WHT marker (bill) | `account.move.line.wt_tax_id` | Many2one → `account.withholding.tax`, computed/stored/editable | `models/account_move.py:9–15` | Source: product (`supplier_wt_tax_id` for purchase) or manual edit |
| Bill-level WHT aggregate (informational only, not posted) | `account.move.wht_amount` | Float, computed, stored | `models/account_move.py:34, 105–117` | Not a ledger line — UI aggregate |
| Payment-level WHT marker | `account.payment.wt_tax_id` | Many2one → `account.withholding.tax` | `models/account_payment.py:9–13` | "Useful for case 1 tax only" (single-rate case) |
| Payment write-off target account | `account.payment.register.writeoff_account_id` (Odoo core field, populated by this module) | Many2one → `account.account` | Set at `wizard/account_payment_register.py:66` from `wt_tax_id.account_id` | This is where the WHT credit actually posts |
| Multi-rate deduction line WHT marker | `account.payment.deduction.wt_tax_id` | Many2one → `account.withholding.tax` | `l10n_th_withholding_tax_multi/models/account_payment.py:98–102` | Multi-module only |
| Multi-rate deduction source line | `account.payment.deduction.wt_move_line` / `account.move.line.wt_move_line` | Many2one → `account.move.line` | `l10n_th_withholding_tax_multi/models/account_payment.py:103, 122–124` | Traces the deduction back to its originating invoice line |
| Vendor payable account | Odoo core (`account.account`, `account_type = liability_payable`) | — | Not redefined by this module | Reduced by net-of-WHT payment amount via core AP logic |

---

## 4. Purchase-Side Certificate Linkage (Forward Trace to `withholding.tax.cert`)

Module: `l10n_th_withholding_tax_cert` (already deep-audited for the *print* side by CORR-007A at commit `deceb7339b39eba309236782f159f8393224f5fd`; this section only confirms the *data-linkage* point, per task scope).

File: `addons_extra/l10n_th_withholding_tax_cert/models/withholding_tax_cert.py`
SHA-256: `7df08a7d94b1473b06e4c74df45e25594f2fc139af45778a9ce14c9810a79088` (426 lines)

- `withholding.tax.cert.payment_id` — `Many2one` → `account.payment`, `models/withholding_tax_cert.py:103–113`. Domain restricts to `[('partner_id', '=', supplier_partner_id), ('wt_cert_cancel', '=', True)]`.
- `withholding.tax.cert.move_id` — `Many2one` → `account.move`, `models/withholding_tax_cert.py:120–130`. Domain restricts to `[('journal_id.type', '=', 'general'), ('wt_cert_cancel', '=', True), ('state', '=', 'posted')]` — i.e. journal entries, not invoices directly.
- `_compute_wt_cert_data()` (lines 237–285): `record.name = record.payment_id.name or record.move_id.name` (line 252) — this is the exact field CORR-007A cited for certificate numbering.
- **The linking mechanism that pulls the actual WHT amounts onto the certificate is `_get_wt_move_line()`** (lines 309–320):
  ```python
  if payment:
      return payment.move_line_ids.filtered(lambda l: l.account_id.id in wt_account_ids)
  if move:
      return move.line_ids.filtered(lambda l: l.account_id.id in wt_account_ids)
  ```
  i.e. it re-reads the **posted journal items of the payment** (or manual journal entry) whose `account_id` is flagged `wt_account = True`. `wt_account_ids` is sourced from `_get_wt_account_ids()` (lines 219–235), an `@tools.ormcache`-decorated search of `account.account` where `wt_account = True` — the same flag defined in `models/account.py:12` in the base module (§2.1 item 1).
- `_prepare_wt_line()` (lines 291–307) then builds each `withholding.tax.cert.line` from `move_line.wt_tax_id.amount` (rate) and `abs(move_line.balance)` (posted amount) — i.e. it reads the **already-posted GL line's actual debit/credit balance**, not a re-derivation from the bill.
- Certificate creation itself is **not automatic**: `action_create_withholding_tax_cert()` (lines 352–365) is explicitly documented as *"This function is called from either account.move or account.payment"* — i.e. a user-triggered wizard action (`create.withholding.tax.cert`, confirmed present at `wizard/create_withholding_tax_cert.py` in the file listing), not a `post()`-time automatic side effect.

**Conclusion for Q6:** the purchase-side WHT certificate is populated by reading back the posted GL journal item created by the payment-register write-off (§2.4) on an account flagged `wt_account = True` (§2.1/§3) — the certificate is generated from **actual posted ledger data**, not from the bill's `wht_amount` estimate, and generation is a manual, user-initiated wizard action rather than an automatic trigger on payment posting.

---

## 5. Relationship to PND3/PND53 Filing (Module Boundary Only — Not Deep-Audited)

Confirmed module boundary, per task instructions (another team owns `tax_report_pnd.py` in depth):

- `addons_extra/l10n_th_withholding_tax/models/tax_report_pnd.py` (SHA-256 `41726222e1effd5774f40cde15c6cdf79e2ab5195eb44ef0cbe5fc5ce03401f5`, 103 lines) defines `class L10n_ThPndReportHandler(models.AbstractModel): _inherit = 'l10n_th.pnd.report.handler'` (lines 4–5) — it **extends**, does not define, the PND report engine. The base abstract model `l10n_th.pnd.report.handler` lives in the separate, upstream-dependency module `02 OTHER/l10n_th_reports/models/tax_report_pnd.py` (SHA-256 `346ab7b52ddba341accac959369439d7b249167db6e882a3ffaafd0eba62a33f`, 145 lines) — confirming the manifest-declared dependency chain in §1.1/§1.3.
- The extension's `_rows()` method (lines 7–104) is a raw SQL query with two `UNION`-ed branches:
  - Branch 1 (lines 20–53): reads `account_move_line` joined directly to `account_tax` via `tax_line_id` — i.e., standard (non-WHT) tax lines.
  - Branch 2 (lines 55–93): reads `account_move_line` joined to `account_withholding_tax` (`awt`) on `account_move_line.wt_tax_id`, further joined to `account_tax` — **this is the purchase-side WHT branch**, filtered by `account_move_line.payment_id IS NULL AND account_move_line__move_id.payment_state != 'not_paid'` (lines 91–92), i.e., it reads the WHT write-off/deduction GL lines created by the payment-register flow described in §2.4, on already (at least partially) paid moves.
- **This confirms the data flow for Q7**: the same `account.move.line` records carrying `wt_tax_id` that are created at payment time (§2.4) and read into `withholding.tax.cert` (§4) are *also* the rows read by the PND3/PND53 report SQL — all three consumers (certificate, PND report, and the payment write-off itself) key off the same GL data, not three independent computations.
- No deeper audit of filing correctness, PND3-vs-PND53 form-selection logic, or the report wizard was performed here — that is explicitly out of this team's scope.

---

## 6. Stock/Inventory Dependency Check (Explicit Grep Evidence)

Per governing rule 4, the following greps were run across all three examined modules (`l10n_th_withholding_tax`, `l10n_th_withholding_tax_multi`, `l10n_th_withholding_tax_cert`) — full source, not samples:

```
grep -rn "stock\.move|stock\.quant|stock\.picking|stock_move|stock_quant|stock_picking" \
  l10n_th_withholding_tax l10n_th_withholding_tax_multi l10n_th_withholding_tax_cert
→ exit code 1 (no matches)

grep -rni "stock" \
  l10n_th_withholding_tax l10n_th_withholding_tax_multi l10n_th_withholding_tax_cert \
  --include="*.py" --include="*.xml" --include="*.csv" --include="*.rst"
→ exit code 1 (no matches, case-insensitive, any file type)

grep -rn "detailed_type|product_type|'service'|\"service\"|type_service|consu" \
  l10n_th_withholding_tax l10n_th_withholding_tax_multi l10n_th_withholding_tax_cert
→ exit code 1 (no matches)

grep -rni "valuation|qty_available|standard_price|cost_method" \
  l10n_th_withholding_tax l10n_th_withholding_tax_multi l10n_th_withholding_tax_cert
→ exit code 1 (no matches)
```

**Verdict: NONE FOUND.** There is no reference to `stock.move`, `stock.quant`, `stock.picking`, product stock/valuation fields (`qty_available`, `standard_price`, `cost_method`), or any inventory-adjacent terminology anywhere in the three modules' Python, XML, CSV, or RST files. This directly confirms the task owner's working hypothesis for these three modules as examined.

**Caveat on scope:** this check covers only the three modules explicitly in scope (`l10n_th_withholding_tax`, `l10n_th_withholding_tax_multi`, `l10n_th_withholding_tax_cert`). It does **not** cover `l10n_th_withholding_tax_report`, `l10n_th_withholding_tax_cert_form`, or `l10n_th_reports` — those were only opened at the manifest level for dependency-chain purposes (§1) and were not grepped for stock references. If a definitive "WHT has zero inventory touchpoints anywhere in the full dependency graph" claim is needed, those three modules should be grepped as a follow-up (out of this session's assigned scope).

---

## 7. Is WHT Genuinely Service-Only, or Does It Also Apply to Stockable Products?

**Finding: WHT is NOT gated by product type in the code.** Evidence:

- `product.template.supplier_wt_tax_id` (`models/product.py:10`) is added to `product.template` with **no domain, no type filter, and no conditional visibility tied to `product.type`/`detailed_type`** — the field definition is a bare `fields.Many2one(comodel_name="account.withholding.tax")` with no `domain=` argument at all.
- The view that exposes it, `views/product_view.xml:10–12`, inserts the field unconditionally after `supplier_taxes_id` on the product form — no `attrs`/`invisible` condition based on product type was found in the 15-line file (read in full).
- `account.move.line._compute_wt_tax_id()` (`models/account_move.py:17–28`) branches purely on **`move_id.move_type`** (`in_invoice`/`in_refund`/`out_receipt` → pull `product_id.supplier_wt_tax_id`), never on the product's `type`/`detailed_type` (storable/consumable/service). A line for a stockable product with `supplier_wt_tax_id` set would populate `wt_tax_id` exactly the same way as a service product.
- The grep in §6 (`detailed_type|product_type|'service'|type_service|consu`) returned zero matches anywhere in the three modules — confirming there is no code path that excludes stockable/consumable products from WHT eligibility.

**Conclusion for Q9:** WHT applicability in this code is governed entirely by whether a `supplier_wt_tax_id` (or a manually-set `wt_tax_id` on the line) is present — it is **product-type-agnostic**. The "service-only" characterization is a **business/configuration convention** (Thai WHT statutorily applies mainly to services, rent, professional fees, etc., not to goods purchases) that would have to be enforced by *how the company configures which products carry `supplier_wt_tax_id`*, not by anything the code itself restricts. No code-level gate prevents a stockable product from being marked WHT-eligible. This distinction is significant: the "no stock.move dependency" finding (§6) and the "service-only" question (§9) are separate claims — the former is confirmed true (no execution-time coupling to inventory transactions), the latter is **not enforced by code** and should not be assumed as a system guarantee.

---

## 8. What This Proves / Does Not Prove

**What this document proves (static source verification only):**
- The exact fields, files, and line ranges that implement purchase-side WHT configuration, computation, payment-time posting, GL account routing, and certificate/report data linkage, as they exist in this reference source tree at the time of this audit.
- That WHT posting is deferred to payment time via Odoo's native write-off/deduction mechanism, not posted on bill validation.
- That the certificate and PND-report consumers both read from the same posted GL data (the payment write-off line), not independent recomputations.
- That no `stock.*` model or product-stock-valuation field is referenced anywhere in the three in-scope modules.
- That product type does not gate WHT eligibility in code.
- The module dependency chain (`account` + `l10n_th_reports` → `l10n_th_withholding_tax` → `l10n_th_withholding_tax_cert`/`_multi`/`_report` → `l10n_th_withholding_tax_cert_form`).

**What this document does NOT prove:**
- **No live Odoo runtime was installed, migrated, or executed.** This is 100% static source-code reading plus `grep`/`shasum`/`wc` inspection — no ORM was booted, no database schema was created, no ir.model.access.csv permission simulation was run, and the module's own test suite (`tests/test_withholding_tax.py`) was read but **not executed** in this session. The test assertions cited in §2.4 are reported as *what the test file asserts*, not as *observed passing test output* — running them was outside the read-only mandate of this audit.
- Whether this accounting flow, as implemented, satisfies Thai Revenue Department statutory withholding-tax requirements (rate correctness by income-type category, PND3/PND53 form eligibility rules, filing deadlines, etc.) — **this requires legal/tax review and is explicitly not asserted here.**
- Whether the SMEsPlus target architecture (Node.js) should replicate this exact data model (product-level WHT field + payment-time write-off + backward-read certificate) — this document describes the Odoo reference behavior only, per the task's "reference/benchmark, not target architecture" framing. No implementation recommendation is made.
- Full inventory-dependency coverage across the *entire* WHT-related dependency graph — `l10n_th_withholding_tax_report`, `l10n_th_withholding_tax_cert_form`, and `l10n_th_reports` were opened only for manifest/dependency purposes, not grepped for stock references (see caveat in §6).
- Correctness or completeness of the multi-WHT (`l10n_th_withholding_tax_multi`) reconciliation math beyond what is directly readable in the 124-line `models/account_payment.py` — the module's own commented-out code (`account_payment.py:27–35, 116–119`) suggests active development/refinement was still in progress in the reference tree at the time of this snapshot.
- Any statement about the print/PDF rendering of the 50-twi certificate — that is CORR-007A's domain, referenced but not re-examined here.

---

## 9. Disposition Input for Boss Recommendation Team

**Recommended disposition for "purchase-side WHT": PARTIAL**

Reasoning:

- **Strong evidence FOUND** for the core accounting mechanics the task asked to verify: configuration path (product/tax/account flags, not partner), rate computation formula, deferred-to-payment posting behavior, GL account routing via `wt_account`/`account_withholding_tax.account_id`, and forward linkage from posted GL data into the certificate model and PND report SQL. These are all cited to exact lines and corroborated by the module's own (read, not executed) test assertions.
- **Confirmed NONE FOUND** for any stock/inventory coupling in the three in-scope modules — this directly supports the task owner's hypothesis and should reduce risk on that specific question.
- However, this is graded **PARTIAL rather than RESOLVED** because:
  1. No live execution/test run was performed — all findings are static-read conclusions on a reference (Odoo) tree, not a runtime-verified accounting cycle. The Boss team should not treat this as equivalent to a functionally-verified process.
  2. The "service-only" assumption is **not code-enforced** (§7) — it is a configuration convention that a real deployment could violate. Any downstream design (Team B/C) that assumes structural service-only enforcement would be building on an incorrect premise; this needs to be explicitly flagged to whichever team designs the SMEsPlus equivalent.
  3. Certificate generation is a **manual, wizard-triggered action**, not automatic on payment posting (§4) — if the eventual SMEsPlus requirement is "certificate auto-issues on payment," that is a gap between the Odoo reference behavior and a hypothetical target requirement, not something this reference tree already does.
  4. Full stock-dependency coverage was not extended to `l10n_th_withholding_tax_report` / `l10n_th_withholding_tax_cert_form` / `l10n_th_reports` (§6 caveat) — a completeness gap, not a contradicting finding.
  5. No legal/tax review has validated that this Odoo reference flow is even statutorily correct for Thai PND3/PND53 filing — that determination is out of this team's authority and is explicitly not claimed here.

This team does **not** declare Gate PASS and does **not** authorize Team B (Inventory Design) or Team C (Development) to proceed on the basis of this document alone — that authority is out of scope for Team A1.

---

## Appendix A — Full File Evidence Manifest (SHA-256, computed via `shasum -a 256`)

Every file read during this audit, for independent spot-check. Paths are relative to `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE/`.

| # | File | Lines | SHA-256 |
|---|---|---|---|
| 1 | `addons_extra/l10n_th_withholding_tax/__manifest__.py` | 24 | `903d9061ba5c16e68f0155309edb263088f1b5253b93ff8dc3b8bf3de12f1995` |
| 2 | `addons_extra/l10n_th_withholding_tax/models/account.py` | 109 | `09919ff4091c27a67dd67fa686972cb3f9ebdb9483f19f3c2234d7d7d90c69a6` |
| 3 | `addons_extra/l10n_th_withholding_tax/models/account_move.py` | 117 | `eeee0f520afc86ccafe80d016b9dfb242647ae29f792044263aeef30a5391aca` |
| 4 | `addons_extra/l10n_th_withholding_tax/models/account_payment.py` | 13 | `a5978b249b8aec8e203516fe6b64ff2de3437b94195f1e1941e6e6f794ec49bb` |
| 5 | `addons_extra/l10n_th_withholding_tax/models/account_tax.py` | 32 | `7af94ba85aa8a88cc4f9fcda91f4ac6eccd8545482e5812f31dc1d7486b51f3a` |
| 6 | `addons_extra/l10n_th_withholding_tax/models/account_withholding_tax.py` | 32 | `ea813264c2bb7b9d41b4fdc4544f4d709f56ebe5c2422ac317bfe5e098eca446` |
| 7 | `addons_extra/l10n_th_withholding_tax/models/product.py` | 10 | `85bad9505a97a45bcec3144d6662cd4124f98bd5d72f19c9aa1e737a7daf333b` |
| 8 | `addons_extra/l10n_th_withholding_tax/models/tax_report_pnd.py` | 103 | `41726222e1effd5774f40cde15c6cdf79e2ab5195eb44ef0cbe5fc5ce03401f5` |
| 9 | `addons_extra/l10n_th_withholding_tax/wizard/account_payment_register.py` | 93 | `725b3dc9e7f13f784732a7e775952a70578828ce7ba18a2f6090308de1c0e57a` |
| 10 | `addons_extra/l10n_th_withholding_tax/wizard/account_payment_register_views.xml` | 17 | `0075dc52046f0c0a8378748dd6ba7ff91098b8addd41663c667561266c9be95b` |
| 11 | `addons_extra/l10n_th_withholding_tax/views/account_move_view.xml` | 43 | `593130c2441d7a58ea3cbb5883a845013ddd26d944e696647b865daa7704be31` |
| 12 | `addons_extra/l10n_th_withholding_tax/views/account_view.xml` | 23 | `37a1d118473b2d7bec390cf9e50325c93ce9fe5e54408cfdb13748cfe5049841` |
| 13 | `addons_extra/l10n_th_withholding_tax/views/account_withholding_tax.xml` | 78 | `5d00000cf566f23d5d5215327427e33201bbc968543c700d1cf50d9c8a1b514a` |
| 14 | `addons_extra/l10n_th_withholding_tax/views/product_view.xml` | 15 | `b8a0fb0c56174895314d713a824351e0d69e8955f6c1a8d740a059eff1273bf7` |
| 15 | `addons_extra/l10n_th_withholding_tax/tests/test_withholding_tax.py` | 220 | `5e112150b36b2f1ce2dd86f04b0635782691b125a0b20f7c5851fb1f5a2a3af5` |
| 16 | `addons_extra/l10n_th_withholding_tax/tests/account_withholding_tax_test.xml` | 13 | `d128525603fc37f1c27e07ede47e71ff347f947335168cc0fc9c812ad3e7fde5` |
| 17 | `addons_extra/l10n_th_withholding_tax/security/ir.model.access.csv` | 2 | `67f42aa27328c880ca6fedb0925b11d146159dad95d1365eb4ff3f668a21fab0` |
| 18 | `addons_extra/l10n_th_withholding_tax/security/security.xml` | 7 | `cdc99ccbde3f2929ad2d01bf31c9093ba67015d16850c2437b824ac170b885f9` |
| 19 | `addons_extra/l10n_th_withholding_tax/readme/CONFIGURATION.rst` | 14 | `a07c04dd587cf24b1ce1f7908b07c00e3042102800f270728926a8601c7fa38c` |
| 20 | `addons_extra/l10n_th_withholding_tax/readme/USAGE.rst` | 10 | `17baa84533c52813bc8342c7828ddb715140cd4debc666a6d63bbd62e380e719` |
| 21 | `addons_extra/l10n_th_withholding_tax/readme/DESCRIPTION.rst` | 2 | `fb67fd4f163319e8c112762c2cdfd95cfcfa86c7dd964ecf6c0c96ec813537dc` |
| 22 | `addons_extra/l10n_th_withholding_tax_multi/models/account_payment.py` | 124 | `3a1dfd190766e026a670af4cc262b741a3c44701cd718ae80384590abeda6307` |
| 23 | `addons_extra/l10n_th_withholding_tax_multi/views/account_payment_view.xml` | 23 | `a12d64e133b64b56d25b9eba8273d4a13b6ec2be0965d76c0c92887d1d2f9085` |
| 24 | `addons_extra/l10n_th_withholding_tax_multi/README.rst` | 108 | `fccb905dcd1a903e6947e8cf34f85ec403e791c854d64db4c5f0f836f6f7f0cb` |
| 25 | `addons_extra/l10n_th_withholding_tax_multi/__manifest__.py` | 16 | `01c6c0558fd7230d055469325c8f386317b34dcd985518f3a2b975293b0bf8e5` |
| 26 | `addons_extra/l10n_th_withholding_tax_cert/models/withholding_tax_cert.py` | 426 | `7df08a7d94b1473b06e4c74df45e25594f2fc139af45778a9ce14c9810a79088` |
| 27 | `addons_extra/l10n_th_withholding_tax_cert/models/account_payment.py` | 43 | `4fa2797f2b89edef00498fe615a7972b6e2b36947cf5340fdaa43350df5e5dbb` |
| 28 | `addons_extra/l10n_th_withholding_tax_cert/models/account_move.py` | 39 | `8522f9f26d085605e0b18e2f80f033060edc06b164bf33f2d56ea08cf66986d2` |
| 29 | `addons_extra/l10n_th_withholding_tax_cert/__manifest__.py` | 23 | `c935212ebf19f4bc224f5104a1ded92fe0a17f4fc5f9c75104ec61b164a90a95` |
| 30 | `02 OTHER/l10n_th_reports/models/tax_report_pnd.py` | 145 | `346ab7b52ddba341accac959369439d7b249167db6e882a3ffaafd0eba62a33f` |
| 31 | `02 OTHER/l10n_th_reports/__manifest__.py` | 24 | `e5018a7020328dc6ace63e2e3e2d13c1775a58d372bf042372851a0778a88c93` |
| 32 | `addons_extra/l10n_th_withholding_tax_report/__manifest__.py` | 40 | `6944ca4421e3dea353304ea3526a6fdcdac68c08f33c6bbf48b5ab77a7603204` |
| 33 | `addons_extra/l10n_th_withholding_tax_cert_form/__manifest__.py` | 23 | `dfc9a1978d6072fe5c8310e798f4a4c81527140fe3d45b22b51861255d5c8bd9` |

Rows 32–33 were read at the manifest level only (dependency-chain confirmation, §1.2); their internal models/views were not examined (out of scope — `l10n_th_withholding_tax_cert_form` is CORR-007A's domain, `l10n_th_withholding_tax_report` is the parallel PND3/PND53 team's domain).
