# Sales-Side Withholding Tax — Source-Code Proof

## Session Metadata

| Field | Value |
|---|---|
| Deliverable | `02_ACC_WHT_SALES_SIDE_PROOF.md` |
| Team | Team A2 — Sales-side WHT Proof Team |
| Repo | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Branch | `audit/account-wht-grpa-m18-closure-010` |
| Evidence base | CORR-007A, commit `deceb7339b39eba309236782f159f8393224f5fd` |
| Report date | 2026-09-02 |
| Mode | Evidence-first / clean-room / **no development authorization** |
| Source tree examined (read-only) | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE/addons_extra/` and `.../SOURCE CODE/02 OTHER/l10n_th_reports/` (Odoo Thai-localization addons — REFERENCE tree only, not the SMEsPlus target architecture) |
| Scope | Sales-side (customer-withheld) withholding-tax handling: is there a distinct code path, a WHT-receivable GL concept, and a received-certificate evidence-tracking mechanism? |
| Out of scope | Purchase-side (vendor) WHT process (owned by Team A1, see `01_ACC_WHT_PURCHASE_SIDE_PROOF.md`), 50-twi print-layout audit (CORR-007A), Gate PASS declaration, Team B/C authorization |
| Related prior deliverable | `01_ACC_WHT_PURCHASE_SIDE_PROOF.md` (same directory) — read for context/format only; its hashes for shared files (`l10n_th_withholding_tax/__manifest__.py`, `l10n_th_withholding_tax_multi/__manifest__.py`, `l10n_th_withholding_tax_report/__manifest__.py`, `02 OTHER/l10n_th_reports/__manifest__.py`, `02 OTHER/l10n_th_reports/models/tax_report_pnd.py`) were independently re-computed here and match exactly, confirming the tree was unchanged between the two audits. |

**Governing constraints applied:** every factual claim below cites an exact file path and line range, with a SHA-256 of the file computed via `shasum -a 256` at the time of this audit. Where the source does not contain a feature, this document says **NOT FOUND** rather than inferring intent from purchase-side symmetry. No statement here constitutes a declaration of Thai Revenue Department statutory compliance — anything requiring that judgment is flagged **LEGAL_TAX_REVIEW_REQUIRED**. This is a read-only audit; no application source code was modified, installed, or executed.

---

## 1. What Was Searched, and How

### 1.1 Files read in full (not excerpted)

| # | File | SHA-256 | Lines |
|---|---|---|---|
| 1 | `addons_extra/l10n_th_withholding_tax/__manifest__.py` | `903d9061ba5c16e68f0155309edb263088f1b5253b93ff8dc3b8bf3de12f1995` | 24 |
| 2 | `addons_extra/l10n_th_withholding_tax/models/account_move.py` | `eeee0f520afc86ccafe80d016b9dfb242647ae29f792044263aeef30a5391aca` | 117 |
| 3 | `addons_extra/l10n_th_withholding_tax/models/account_payment.py` | `a5978b249b8aec8e203516fe6b64ff2de3437b94195f1e1941e6e6f794ec49bb` | 13 |
| 4 | `addons_extra/l10n_th_withholding_tax/wizard/account_payment_register.py` | `725b3dc9e7f13f784732a7e775952a70578828ce7ba18a2f6090308de1c0e57a` | 93 |
| 5 | `addons_extra/l10n_th_withholding_tax/models/account_tax.py` | `7af94ba85aa8a88cc4f9fcda91f4ac6eccd8545482e5812f31dc1d7486b51f3a` | 32 |
| 6 | `addons_extra/l10n_th_withholding_tax/models/account.py` | `09919ff4091c27a67dd67fa686972cb3f9ebdb9483f19f3c2234d7d7d90c69a6` | 109 |
| 7 | `addons_extra/l10n_th_withholding_tax/models/account_withholding_tax.py` | `ea813264c2bb7b9d41b4fdc4544f4d709f56ebe5c2422ac317bfe5e098eca446` | 32 |
| 8 | `addons_extra/l10n_th_withholding_tax/models/product.py` | `85bad9505a97a45bcec3144d6662cd4124f98bd5d72f19c9aa1e737a7daf333b` | 10 |
| 9 | `addons_extra/l10n_th_withholding_tax/models/tax_report_pnd.py` | `41726222e1effd5774f40cde15c6cdf79e2ab5195eb44ef0cbe5fc5ce03401f5` | 103 |
| 10 | `addons_extra/l10n_th_withholding_tax/tests/test_withholding_tax.py` | `5e112150b36b2f1ce2dd86f04b0635782691b125a0b20f7c5851fb1f5a2a3af5` | 220 |
| 11 | `addons_extra/l10n_th_withholding_tax_multi/__manifest__.py` | `01c6c0558fd7230d055469325c8f386317b34dcd985518f3a2b975293b0bf8e5` | 16 |
| 12 | `addons_extra/l10n_th_withholding_tax_multi/models/account_payment.py` | `3a1dfd190766e026a670af4cc262b741a3c44701cd718ae80384590abeda6307` | 124 |
| 13 | `addons_extra/l10n_th_withholding_tax_cert/__manifest__.py` | `c935212ebf19f4bc224f5104a1ded92fe0a17f4fc5f9c75104ec61b164a90a95` | 23 |
| 14 | `addons_extra/l10n_th_withholding_tax_cert/models/withholding_tax_cert.py` | `7df08a7d94b1473b06e4c74df45e25594f2fc139af45778a9ce14c9810a79088` | 426 |
| 15 | `addons_extra/l10n_th_withholding_tax_cert/models/account_move.py` | `8522f9f26d085605e0b18e2f80f033060edc06b164bf33f2d56ea08cf66986d2` | 39 |
| 16 | `addons_extra/l10n_th_withholding_tax_cert/models/account_payment.py` | `4fa2797f2b89edef00498fe615a7972b6e2b36947cf5340fdaa43350df5e5dbb` | 43 |
| 17 | `addons_extra/l10n_th_withholding_tax_cert/models/account_account.py` | `f1c4515f9c2a959377d49e9504b39f1fc4490b267cc3c1cf0d087e9677bd9326` | 33 |
| 18 | `addons_extra/l10n_th_withholding_tax_cert/wizard/create_withholding_tax_cert.py` | `b3b38f8d4734dcb220d7e425fcbf27a8157f9019619b686a29f11b04e88dd214` | 208 |
| 19 | `addons_extra/l10n_th_withholding_tax_cert/migrations/19.0.1.5/post-migrate.py` | `8e7ee7ebbff383c1a05d89b0237cf92cc778ff0239dae95c67f45a154b4b0590` | 112 |
| 20 | `addons_extra/l10n_th_withholding_tax_report/__manifest__.py` | `6944ca4421e3dea353304ea3526a6fdcdac68c08f33c6bbf48b5ab77a7603204` | 40 |
| 21 | `addons_extra/l10n_th_withholding_tax_report/report/report_withholding_tax_xlsx.py` | `d13a679590de6f0c50a341bd7cb3c1e32dc10c9466566b537f2304b403405434` | 424 |
| 22 | `addons_extra/l10n_th_withholding_tax_report/models/report_withholding_tax.py` | `9950b71f2a482ff9ad8fff96a78831c55a3e9642cc2efcd6decde1f367820174` | 161 |
| 23 | `addons_extra/l10n_th_withholding_tax_report/wizard/withholding_tax_report_wizard.py` | `253b1b5307f41803949567ed1736ae56a3a6d9d874a779ce93aaad720fad7db0` | 250 |
| 24 | `addons_extra/l10n_th_withholding_tax_cert_form/__manifest__.py` | `dfc9a1978d6072fe5c8310e798f4a4c81527140fe3d45b22b51861255d5c8bd9` | 23 |
| 25 | `02 OTHER/l10n_th_reports/__manifest__.py` | `e5018a7020328dc6ace63e2e3e2d13c1775a58d372bf042372851a0778a88c93` | 24 |
| 26 | `02 OTHER/l10n_th_reports/models/tax_report_pnd.py` | `346ab7b52ddba341accac959369439d7b249167db6e882a3ffaafd0eba62a33f` | 145 |

`l10n_th_withholding_tax_cert_form/` was additionally located and its manifest read (item 24) because it is the certificate PRINT module downstream of `l10n_th_withholding_tax_cert`; it was not deep-audited beyond confirming it adds no direction-aware fields (it depends only on `web`, `l10n_th_withholding_tax_cert`, `l10n_th_amount_to_text` — no new model files touch sales-side concepts). This module was previously audited in depth for print-layout purposes by CORR-007A and is referenced, not re-audited, here.

### 1.2 Greps executed (exact commands, verbatim)

```
grep -rn -i "payment_type" \
  addons_extra/l10n_th_withholding_tax addons_extra/l10n_th_withholding_tax_multi \
  addons_extra/l10n_th_withholding_tax_cert addons_extra/l10n_th_withholding_tax_report \
  addons_extra/l10n_th_withholding_tax_cert_form
  → 0 matches

grep -rn -i "inbound\|outbound" \
  addons_extra/l10n_th_withholding_tax addons_extra/l10n_th_withholding_tax_multi \
  addons_extra/l10n_th_withholding_tax_cert addons_extra/l10n_th_withholding_tax_report \
  addons_extra/l10n_th_withholding_tax_cert_form
  → 0 matches

grep -rn -i "wht.*receiv\|receiv.*wht\|withholding.*credit\|withholding.*receiv" \
  addons_extra "02 OTHER/l10n_th_reports"
  → 0 matches (whole addons_extra tree, per governing rule)

grep -rn -i "receivable" \
  addons_extra/l10n_th_withholding_tax addons_extra/l10n_th_withholding_tax_cert \
  addons_extra/l10n_th_withholding_tax_multi addons_extra/l10n_th_withholding_tax_report \
  addons_extra/l10n_th_withholding_tax_cert_form
  → 0 matches

grep -rn "type_tax_use" \
  addons_extra/l10n_th_withholding_tax addons_extra/l10n_th_withholding_tax_cert \
  addons_extra/l10n_th_withholding_tax_multi addons_extra/l10n_th_withholding_tax_report \
  addons_extra/l10n_th_withholding_tax_cert_form
  → 3 matches, all in models/account_move.py:57, :89 and models/account.py:89 (see §2)

grep -rn -i "attachment\|received\|receiv\|issue" \
  addons_extra/l10n_th_withholding_tax_cert  (all .py and .xml files)
  → 0 matches

grep -rn "stock\.move\|stock\.quant\|stock\.picking" \
  addons_extra/l10n_th_withholding_tax addons_extra/l10n_th_withholding_tax_cert \
  addons_extra/l10n_th_withholding_tax_multi addons_extra/l10n_th_withholding_tax_report \
  addons_extra/l10n_th_withholding_tax_cert_form
  → 0 matches

grep -rn "stock" <all 5 module __manifest__.py files>
  → 0 matches

grep -rn "stock\.move\|stock\.quant\|stock\.picking\|\"stock\"\|'stock'" \
  "02 OTHER/l10n_th_reports"
  → 0 matches
```

### 1.3 Directory/manifest inspection

- Full recursive `find` listing of `l10n_th_withholding_tax`, `l10n_th_withholding_tax_cert`, `l10n_th_withholding_tax_multi`, `l10n_th_withholding_tax_report`, `l10n_th_withholding_tax_cert_form` — every file name inspected for direction-suggestive naming (`customer`, `received`, `sale`, `issued`, etc.) — none found beyond what is cited in §2–§4.
- `depends` key of all five module manifests read in full — confirmed dependency chain is `account` → `l10n_th_reports` → `l10n_th_withholding_tax` → {`l10n_th_withholding_tax_cert`, `l10n_th_withholding_tax_multi`} → {`l10n_th_withholding_tax_report`, `l10n_th_withholding_tax_cert_form`}. No `stock`, `sale`, or `purchase` addon appears as a hard dependency of any of these five manifests.

---

## 2. Findings — Inbound/Outbound (Sale/Purchase) Symmetry Check

### 2.1 The tax/config layer IS side-aware (not merely generic)

`addons_extra/l10n_th_withholding_tax/models/account_move.py` (SHA-256 `eeee0f520afc86ccafe80d016b9dfb242647ae29f792044263aeef30a5391aca`):

- Lines 17–28, `AccountMoveLine._compute_wt_tax_id`:
  ```python
  if rec.move_id.move_type in ("out_invoice", "out_refund", "in_receipt"):
      rec.wt_tax_id = rec.product_id.wt_tax_id
  elif rec.move_id.move_type in ("in_invoice", "in_refund", "out_receipt"):
      rec.wt_tax_id = rec.product_id.supplier_wt_tax_id
  ```
  This explicitly branches by `move_type`. Customer-facing move types (`out_invoice`, `out_refund`) pull the WHT tax from `product.wt_tax_id`; vendor-facing move types (`in_invoice`, `in_refund`) pull from `product.supplier_wt_tax_id`. (Note: `in_receipt`/`out_receipt` are grouped with the *opposite* side of what their name suggests — `in_receipt` uses the customer-side field, `out_receipt` uses the supplier-side field — cited verbatim as found; this asymmetric grouping is itself a candidate defect worth separate review but does not change the sale/purchase-symmetry conclusion.)
- Lines 39–103, `AccountMove._compute_tax_domain`: defines `PURCHASE_TYPES = frozenset(('in_receipt','in_invoice','in_refund'))` (line 49) and `SALE_TYPES = frozenset(('out_receipt','out_invoice','out_refund'))` (line 50), then builds a **separate WHT-tax candidate pool for each side**:
  - Purchase pool (lines 53–61): `account.tax` search `[('type_tax_use','in',('purchase','none',False))]` and `account.withholding.tax` search `[('type','in',('purchase','none',False))]`.
  - Sale pool (lines 85–93): `account.tax` search `[('type_tax_use','in',('sale','none',False))]` and `account.withholding.tax` search `[('type','in',('sale','none',False))]`.
- `addons_extra/l10n_th_withholding_tax/models/product.py` (SHA-256 `85bad9505a97a45bcec3144d6662cd4124f98bd5d72f19c9aa1e737a7daf333b`), lines 9–10: two distinct `Many2one` fields exist — `wt_tax_id` (customer/sales-side default) and `supplier_wt_tax_id` (vendor/purchase-side default). Confirms a dedicated sales-side configuration point exists at the product level.
- `addons_extra/l10n_th_withholding_tax/models/account_withholding_tax.py` (SHA-256 `ea813264c2bb7b9d41b4fdc4544f4d709f56ebe5c2422ac317bfe5e098eca446`), line 19: `type = fields.Selection([('sale','Sales'),('purchase','Purchase'),('none','None')])` — a first-class field distinguishing sale-type from purchase-type WHT tax records.
- `addons_extra/l10n_th_withholding_tax/models/account.py` (SHA-256 `09919ff4091c27a67dd67fa686972cb3f9ebdb9483f19f3c2234d7d7d90c69a6`), line 89: `"type": rec.type_tax_use` inside `update_wt()` — when an `account.tax` flagged `wt_tax=True` is created/written, the derived `account.withholding.tax.type` is auto-populated straight from Odoo's own `type_tax_use` (`'sale'`/`'purchase'`/`'none'`) field on that tax. This is the concrete mechanism that lets a sale-type withholding tax record exist at all.

**Conclusion for this sub-question:** Odoo's standard `type_tax_use` (`sale`/`purchase`/`none`) is present and actively used (confirmed by the `type_tax_use` grep, 3 hits, all cited above) — and the module builds genuinely separate sale-side and purchase-side selection pools on top of it. This is not "generic/no side-specific handling" — there is a real, working sale-side code path at the tax-configuration and invoice-line level.

### 2.2 The payment layer has NO explicit inbound/outbound gate — but is also unverified for sales-side money flow

- `addons_extra/l10n_th_withholding_tax/models/account_payment.py` (SHA-256 `a5978b249b8aec8e203516fe6b64ff2de3437b94195f1e1941e6e6f794ec49bb`), full 13-line file: adds one field, `wt_tax_id` (lines 9–13). No `payment_type` reference anywhere.
- `addons_extra/l10n_th_withholding_tax/wizard/account_payment_register.py` (SHA-256 `725b3dc9e7f13f784732a7e775952a70578828ce7ba18a2f6090308de1c0e57a`), full 93-line file: `_compute_amount()` (lines 38–72) reduces `self.amount` by the sum of `wt_tax_id.amount/100 * price_subtotal` over `account.move.line` records carrying `wt_tax_id` (lines 45–52), regardless of the parent move's `move_type`. No `payment_type` or `inbound`/`outbound` check exists anywhere in this file (confirmed by grep, §1.2).
- `addons_extra/l10n_th_withholding_tax_multi/models/account_payment.py` (SHA-256 `3a1dfd190766e026a670af4cc262b741a3c44701cd718ae80384590abeda6307`), full 124-line file: same pattern — `_update_vals_multi_deduction` (lines 37–82) and `_compute_payment_difference_handling` (lines 11–25) operate on `account.move.line.wt_tax_id` generically. No `payment_type` reference anywhere.

Because `wt_tax_id` population is itself move_type-aware (§2.1) and the payment-register override is move_type-agnostic, **by code inspection alone** the same automatic write-off/reconciliation mechanism that nets a vendor bill payment by the WHT amount would also fire when registering a customer's incoming payment against an `out_invoice` line that carries `wt_tax_id`.

**However, this is not proven by the test suite.** `addons_extra/l10n_th_withholding_tax/tests/test_withholding_tax.py` (SHA-256 `5e112150b36b2f1ce2dd86f04b0635782691b125a0b20f7c5851fb1f5a2a3af5`, 220 lines total — the file ends at line 220):
- `test_01_create_payment_withholding_tax` (lines 104–159) and `test_02_create_payment_withholding_tax_product` (lines 161–200) — both purchase-side (`in_invoice`) — carry the test all the way through `account.payment.register`, assert `writeoff_account_id`, `payment_difference`, `writeoff_label`, and finally assert `payment_id.amount == price_unit * 0.97` (line 159 / line 200) — i.e., they prove the net-payment mechanism end-to-end for purchase-side.
- `test_03_withholding_tax_customer_invoice` (lines 202–220) is the **only** sales-side test. It creates an `out_invoice` (line 212) with a product configured for customer-side WHT (line 206–208, `customer=True` → sets `product.wt_tax_id`), asserts `invoice_line_ids.wt_tax_id` is set and its account matches (lines 217–219), and calls `invoice_id.action_post()` (line 220). **The file ends there.** It does not invoke `account.payment.register`, does not assert a `payment_difference`/`writeoff_account_id`, and does not assert a net payment amount. No test in this codebase demonstrates the sales-side money flow (customer pays net-of-WHT, a WHT-receivable/write-off line is posted) actually working.

**Conclusion for this sub-question:** the payment/reconciliation code path is structurally symmetric (no direction gate), but its correctness for the sales side is **unverified by any test in the reference tree** — it is a plausible-by-inspection code path, not a proven one.

---

## 3. GL Account / WHT-Receivable Findings

- `addons_extra/l10n_th_withholding_tax/models/account.py`, lines 12–16: `account.account.wt_account = fields.Boolean(..., help="If check, this account is for withholding tax")`. This is a **single, undirected boolean flag**. It does not distinguish an asset/receivable-type WHT account (tax credit owed to SMEsPlus by the Revenue Department) from a liability/payable-type WHT account (tax SMEsPlus owes the Revenue Department on behalf of a vendor).
- `addons_extra/l10n_th_withholding_tax/models/account_withholding_tax.py`, lines 12–18: `account.withholding.tax.account_id` is a **single** `Many2one` to `account.account`, domain `[("wt_account", "=", True)]`, `required=True`. The same field is used regardless of whether `type` (line 19) is `'sale'` or `'purchase'` — there is no `account_id_receivable` / `account_id_payable` pair, no computed default that differs by `type`, and no constraint tying `type='sale'` to an asset-classed account.
- Grep for `"receivable"` (case-insensitive) across all five WHT modules → **0 matches** (§1.2). Grep for the compound patterns `wht.*receiv|receiv.*wht|withholding.*credit|withholding.*receiv` across the **entire** `addons_extra/` tree and `02 OTHER/l10n_th_reports/` → **0 matches**.

**Verdict: NOT FOUND.** There is no dedicated "WHT receivable / tax credit" GL account concept anywhere in the examined code. The only account-side hook is the generic `wt_account` boolean, which an administrator could manually apply to a receivable-classed account for sales-side use — but nothing in the schema models, enforces, or defaults that direction. This is a configuration possibility, not a built feature.

---

## 4. Certificate-Received Tracking Findings

`addons_extra/l10n_th_withholding_tax_cert/models/withholding_tax_cert.py` (SHA-256 `7df08a7d94b1473b06e4c74df45e25594f2fc139af45778a9ce14c9810a79088`, full 426-line file read):

- The model `withholding.tax.cert` has exactly one partner-linking field: `supplier_partner_id` (lines 139–147, "Supplier"), with a related `supplier_taxid` (lines 168–172). **There is no `customer_partner_id` field** anywhere in this file.
- `_onchange_supplier_partner_id` (lines 202–209) sets `income_tax_form` to `"pnd53" if self.supplier_partner_id.is_company else "pnd3"` — PND3/PND53 are the Thai forms filed by a **withholding agent** (i.e., SMEsPlus when it withholds from a vendor); there is no equivalent onchange or form code keyed off a customer relationship.
- The only Selection fields on the model are: `state` (`draft`/`done`/`cancel`, lines 90–97 — a document workflow state for the certificate SMEsPlus itself is producing, not an inbound/outbound direction marker), `income_tax_form` (`pnd1`/`pnd3`/`pnd3a`/`pnd53`, lines 173–180, defined at lines 9–14 — all four are Revenue-Department filing forms used by the withholding agent), and `tax_payer` (`withholding`/`paid_one_time`, lines 188–195, 66). **No `type`, `direction`, `cert_type`, or `wt_cert_type` selection field exists** distinguishing "certificate we issued to a vendor" from "certificate we received from a customer."
- The only binary/file field on the model is `signature = fields.Binary()` (line 196) — used to hold SMEsPlus's own signature for the certificate it prints and issues. There is no `attachment`, `scan`, `received_document`, or similarly named field for storing an inbound, customer-issued PDF/scan as evidence.
- `action_create_withholding_tax_cert` (lines 352–365) and the wizard `create.withholding.tax.cert` (`addons_extra/l10n_th_withholding_tax_cert/wizard/create_withholding_tax_cert.py`, SHA-256 `b3b38f8d4734dcb220d7e425fcbf27a8157f9019619b686a29f11b04e88dd214`, full 208-line file read) can only originate a certificate from an `account.payment` or an `account.move` whose `move_type == 'entry'` (enforced at lines 41–56 of the wizard — `UserError` raised otherwise: *"You can create withholding tax from Payment or Journal Entry only"*). Sales invoices (`out_invoice`) are not a valid source model for this wizard at all — the workflow is structurally "we generate an outgoing document," not "we record an incoming one."
- Grep for `attachment|received|receiv|issue` (case-insensitive) across every `.py` and `.xml` file in `l10n_th_withholding_tax_cert/` → **0 matches** (§1.2).
- `addons_extra/l10n_th_withholding_tax_cert/models/account_move.py` and `.../models/account_payment.py` (both read in full, 39 and 43 lines respectively) each only add `wt_cert_ids` (One2many back-reference) and a computed `wt_cert_cancel` boolean — no direction-aware or received-document field on either.
- Note: `withholding.tax.cert` inherits `mail.thread`/`mail.activity.mixin` (line 74), which gives every record Odoo's generic chatter with ad-hoc file attachments. This is a platform-level capability available on virtually any Odoo record, not a dedicated field, workflow, or required step for retaining a customer-issued certificate as tax evidence — flagged here explicitly so this generic capability is not mistaken for a purpose-built feature.
- `addons_extra/l10n_th_withholding_tax_report/report/report_withholding_tax_xlsx.py` (SHA-256 `d13a679590de6f0c50a341bd7cb3c1e32dc10c9466566b537f2304b403405434`) and `.../wizard/withholding_tax_report_wizard.py` (SHA-256 `253b1b5307f41803949567ed1736ae56a3a6d9d874a779ce93aaad720fad7db0`) both key exclusively off `cert_id.supplier_partner_id` (e.g. xlsx report line 338, 355; wizard line 169, 172, 176) and restrict `income_tax_form` to `[("pnd3","PND3"),("pnd53","PND53")]` (wizard line 22, `models/report_withholding_tax.py` line 17) — i.e. the "internal review/summary xlsx report" flagged by CORR-007A as not-deep-inspected is confirmed, on full read, to report **only** WHT the company withheld from suppliers (PND3/PND53 filings). It has no output column, filter, or data source representing WHT withheld *from* SMEsPlus by a customer.

**Verdict: NOT FOUND.** There is no field, state, attachment slot, or workflow anywhere in the examined tree for recording that SMEsPlus received a withholding-tax certificate from a customer as evidence of a sales-side WHT credit. The entire `withholding.tax.cert` model, its creation wizard, and its xlsx/text/qweb reports are built exclusively around SMEsPlus as the certificate **issuer** (vendor-facing), not as a certificate **recipient** (customer-facing).

---

## 5. Reconciliation Mechanism (Invoice Amount vs. Net Amount Received)

- The `account.payment.register` override (§2.2) is a real, working reconciliation mechanism **when triggered**: it computes the WHT amount from `wt_tax_id`-bearing lines, reduces the registered payment amount by that sum, and routes the difference to a write-off line on `wt_tax_id.account_id` with `payment_difference_handling = 'reconcile'` (`wizard/account_payment_register.py` lines 59–67, 89–93). This is the mechanism that, for purchase-side, avoids any need for a manual journal entry — proven by `test_01`/`test_02` (§2.2).
- For sales-side, the same code is reachable (no `move_type`/`payment_type` gate — §2.2) but is **not exercised by any test**, and — separately — even if the payment nets correctly, there is still no dedicated WHT-receivable account *type* (§3) and no certificate-evidence retention (§4) to substantiate the resulting tax-credit balance for a CIT filing.
- **Conclusion:** if a company configures `product.wt_tax_id`, flags a receivable-classed account as `wt_account=True`, and manually assigns it as the sale-type `account.withholding.tax.account_id`, the payment-register wizard *should*, by code inspection, automatically post the net-of-WHT receipt and the WHT write-off line without a manual JE. This is a plausible, code-supported claim, not a demonstrated one — it is unverified by the test suite and is not paired with any built-in way to retain the customer's certificate as evidence. **LEGAL_TAX_REVIEW_REQUIRED**: whether an un-evidenced, un-tested automatic posting is adequate for Thai Revenue Department substantiation of a WHT credit claim is a statutory-judgment question outside this audit's authority.

---

## 6. Stock/Inventory Dependency Check

Explicit grep evidence (commands reproduced from §1.2):

```
$ grep -rn "stock\.move\|stock\.quant\|stock\.picking" \
    addons_extra/l10n_th_withholding_tax \
    addons_extra/l10n_th_withholding_tax_cert \
    addons_extra/l10n_th_withholding_tax_multi \
    addons_extra/l10n_th_withholding_tax_report \
    addons_extra/l10n_th_withholding_tax_cert_form
(no output — exit code 1, i.e., zero matches)

$ grep -rn "stock" <all five __manifest__.py "depends" files, and 02 OTHER/l10n_th_reports/__manifest__.py>
(no output — exit code 1, i.e., zero matches)
```

Manifest `depends` keys, read in full and reproduced:
- `l10n_th_withholding_tax`: `["account", "l10n_th_reports"]`
- `l10n_th_withholding_tax_cert`: `["l10n_th_withholding_tax"]`
- `l10n_th_withholding_tax_multi`: `["l10n_th_withholding_tax", "account_payment_multi_deduction"]`
- `l10n_th_withholding_tax_report`: `["account", "report_xlsx_helper", "date_range", "l10n_th_partner", "l10n_th_withholding_tax_cert"]`
- `l10n_th_withholding_tax_cert_form`: `["web", "l10n_th_withholding_tax_cert", "l10n_th_amount_to_text"]`
- `l10n_th_reports` (upstream, `02 OTHER/`): `["l10n_th", "account_reports"]`

**Verdict: CONFIRMED — no `stock.move`, `stock.quant`, or `stock.picking` dependency, reference, or import exists anywhere in the withholding-tax module family examined (models, wizards, reports, or manifests).** This matches the expected posture stated in the audit brief.

---

## 7. What This Proves / Does Not Prove

**Proves:**
- A genuine, side-aware sales-side code path exists at the tax-configuration and invoice-line layer: `type_tax_use`/`account.withholding.tax.type` = `'sale'`, a dedicated `product.wt_tax_id` field, and a `move_type`-branching compute method that populates it correctly on `out_invoice`/`out_refund` lines (§2.1). This is not invented or inferred from purchase-side symmetry — it is directly cited, working code, and it is exercised (up to invoice posting) by `test_03_withholding_tax_customer_invoice`.
- No stock/inventory coupling exists in this module family (§6) — confirmed by direct grep, not assumption.
- The payment-register reconciliation mechanism contains no explicit block on sales-side use (§2.2, §5) — the plumbing is not deliberately purchase-only.

**Does not prove:**
- That the sales-side payment/reconciliation flow actually works end-to-end. `test_03` stops at `action_post()`; no test in the reference tree registers a payment against a WHT-bearing `out_invoice` or asserts a net-of-WHT receipt amount. This is an evidentiary gap, not a confirmed defect — the code may work, but nothing in this tree demonstrates it.
- That a WHT-receivable (tax-credit-asset) GL account concept exists. It does not (§3) — only a single undirected `wt_account` boolean shared by both directions.
- That the system tracks a customer-issued withholding tax certificate as sales-side evidence in any form — field, attachment slot, state, or workflow. It does not (§4). The entire certificate subsystem (model, wizard, and report) is built exclusively from the withholding-agent/issuer (i.e., purchase-side) perspective, with `supplier_partner_id` as its only partner link and PND3/PND53 (agent-filed forms) as its only report scope.
- That any manual-journal-entry alternative is documented, guided, or enforced for sales-side WHT. None was found; if the automatic mechanism in §5 is not actually exercised or is found not to work for `out_invoice`, the practical fallback (manual JE plus manual document retention) exists only as an unstated assumption, not as a documented or system-supported path.

---

## 8. Disposition Input for the Boss Recommendation Team

**Recommendation: PARTIAL.**

Reasoning:
- This is not **NOT FOUND** / REMAINS-HIGH-with-zero-basis: real, side-aware code exists (product-level `wt_tax_id`, `type='sale'` on `account.withholding.tax`, a `move_type`-branching compute, and a payment-register mechanism with no direction gate). Declaring "nothing exists" would misrepresent the evidence in §2.1 and §2.2.
- This is not **RESOLVED**: two structurally significant, operationally load-bearing pieces are confirmed **NOT FOUND** by direct, exhaustive grep and full-file read — (a) a dedicated WHT-receivable/tax-credit GL account concept (§3), and (b) any tracking of a customer-issued certificate as sales-side evidence (§4). Both are normally necessary to substantiate a WHT credit claim at year-end CIT filing. In addition, the one payment-reconciliation mechanism that *could* make this work automatically (§2.2, §5) is **unverified by any test** for the sales side, unlike the purchase side where two tests prove it end-to-end.
- Net assessment: sales-side WHT in this reference tree is a **half-built, unevidenced, untested capability** riding on generic/shared infrastructure — plausible by code inspection, but missing the GL-account typing and certificate-evidence retention that would make it a complete, audit-ready feature, and missing test proof that the money actually nets correctly.
- Flag for the Boss team's own weighting: if "audit-ready evidence retention" and "a dedicated receivable account type" are treated as hard requirements (rather than nice-to-haves an implementer could bolt on using the existing generic `wt_account` boolean and Odoo chatter), this finding would also support **REMAINS HIGH**. This document does not resolve that judgment call — it surfaces the exact gaps (§3, §4) and the exact evidentiary gap (§2.2, §5) so the Boss team can weigh severity with full information, consistent with the instruction not to inflate or paper over this finding.

**LEGAL_TAX_REVIEW_REQUIRED** items surfaced by this audit (statutory-judgment questions, not answered here):
1. Whether Thai Revenue Department rules require a specific GL account classification (receivable/asset) for WHT credits claimed via CIT filing, and whether the generic `wt_account` boolean mechanism found here would satisfy that if manually configured correctly.
2. Whether an un-evidenced (no certificate-tracking) automatic posting is adequate substantiation for a WHT credit claim, or whether physical/scanned certificate retention is a hard statutory requirement that the system must actively support.

No Gate PASS is declared. No authorization is given to Team B or Team C by this document.
