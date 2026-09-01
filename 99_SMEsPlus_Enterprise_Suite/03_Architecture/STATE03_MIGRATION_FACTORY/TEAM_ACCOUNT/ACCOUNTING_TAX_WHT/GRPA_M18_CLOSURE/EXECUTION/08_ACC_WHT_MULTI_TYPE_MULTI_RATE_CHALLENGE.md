# ACC-WHT-06 — Multiple WHT Types/Rates in One Document: Boss Challenge Response

## Session Metadata

| Field | Value |
|---|---|
| Deliverable | `08_ACC_WHT_MULTI_TYPE_MULTI_RATE_CHALLENGE.md` |
| Trigger | Boss Challenge Addendum, mid-session, 2026-09-02: "ACC-WHT-06 Multiple WHT Types In One Document" |
| Team | Team A5 (independent audit), performing this challenge directly per Boss instruction — not delegated to a new sub-team, given the tight coupling to findings A1/A2/A4 already produced and independently verified in this session |
| Repo | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Branch | `audit/account-wht-grpa-m18-closure-010` |
| Evidence base | This session's own `01`-`04` deliverables (purchase-side, sales-side, 50-twi gaps, PND3/PND53), all independently spot-verified in `05_ACC_WHT_FINAL_DISPOSITION_AND_BOSS_RECOMMENDATION.md` §1 |
| Date | 2026-09-02 |
| Mode | Evidence-first / clean-room / **no development authorization** |
| Source tree examined (read-only) | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE/addons_extra/` and `.../02 OTHER/l10n_th_reports/` |
| Worked example used throughout | One vendor bill/payment carrying two service lines: freight/transportation (WHT 1%) and installation (WHT 3%) — Boss's own example |

**Governing constraints applied, unchanged from the rest of this session:** every claim cites an exact file path and line range; SHA-256 of every file quoted was independently computed in this session (see `06_ACC_WHT_SHA256_MANIFEST.txt`, Section A/B/C — all files below are already in that manifest, no new files were introduced). Where the source does not support a capability, this document says so plainly rather than assuming symmetry with the single-rate case. No statement here is a declaration of Thai Revenue Department statutory compliance.

---

## 1. At What Level Is WHT Modeled? (Required Proof Item 1)

Directly re-derived from source, not assumed:

| Level | Modeled? | Evidence |
|---|---|---|
| **Purchase Order** (`purchase.order`) | **NOT FOUND — WHT is never modeled at PO level.** | `grep -rn "purchase.order\|purchase_order\|PurchaseOrder"` across `l10n_th_withholding_tax`, `l10n_th_withholding_tax_multi`, `l10n_th_withholding_tax_cert` → **zero matches**. WHT in this reference tree only ever attaches once a document becomes an `account.move` (vendor bill) or `account.payment`. |
| **Bill header** (`account.move`) | Aggregate/informational only, not the source of truth. | `account.move.wht_amount` (`l10n_th_withholding_tax/models/account_move.py:34, 105-117`) is a computed, non-stored-to-ledger Float — a UI read-only sum of the line-level values (see previously-established finding in `01_ACC_WHT_PURCHASE_SIDE_PROOF.md` §2.3). It does not carry a rate or type of its own. |
| **Bill line** (`account.move.line`) | **YES — this is the actual source of truth.** | `account.move.line.wt_tax_id` (`models/account_move.py:9-15`), a stored, editable `Many2one` to `account.withholding.tax`. Each `account.withholding.tax` record carries its own `amount` (rate, Float) and `type` (`sale`/`purchase`/`none`) — `models/account_withholding_tax.py:19-22`. **Nothing in the schema constrains two lines on the same bill to reference the same `account.withholding.tax` record** — each line's `wt_tax_id` is computed independently via `_compute_wt_tax_id` (`models/account_move.py:17-28`), sourced from that line's own `product_id.wt_tax_id`/`supplier_wt_tax_id`, or manually overridden. |
| **Payment** | Aggregation + (conditionally) a single write-off routing field. | `account.payment.wt_tax_id` (`models/account_payment.py:9-13`) — explicitly documented in its own docstring as *"Useful for case 1 tax only"* (i.e., the single-rate case — see §2 below). |
| **Certificate line** (`withholding.tax.cert.line`) | **YES, one row per contributing GL line.** | `withholding_tax_cert.py:284-285`: `for line in wt_move_lines: record.wt_line += CertLine.new(record._prepare_wt_line(line))` — one `withholding.tax.cert.line` per posted journal item flagged `wt_account=True`, each with its own `wt_percent`/`amount` (`_prepare_wt_line`, lines 292-307). |
| **Report line** (PND3/PND53 CSV) | **YES, one row per `account_move_line.id`, no aggregation.** | Both the base handler (`02 OTHER/l10n_th_reports/models/tax_report_pnd.py:33`) and the WHT-aware override (`addons_extra/l10n_th_withholding_tax/models/tax_report_pnd.py:14-21`) key their `ROW_NUMBER() OVER (ORDER BY ..., account_move_line.id / move_line_id)` window function on the individual journal-item id — confirmed by direct read, **no `GROUP BY` clause exists anywhere in either file.** |

**Conclusion:** WHT type/rate is fundamentally a **line-level** concept in this reference tree (never PO-level, never enforced as a single bill-level value), aggregated only for payment-amount-reduction purposes, and re-expanded back to line granularity on both the certificate and the PND export. This line-level design is what makes a multi-rate document possible *in principle* — but, as §2-§7 show, several of the consuming mechanisms do not fully honor that line-level granularity in practice.

---

## 2. Can Multiple WHTType/WHTRate Entries Exist in the Same Document? (Required Proof Item 2)

### 2.1 Same bill — YES, structurally unconstrained

Confirmed in §1: `account.move.line.wt_tax_id` is computed/editable per line with no cross-line uniqueness constraint anywhere in `account_move.py`, `account_tax.py`, or `account_withholding_tax.py` (all three files re-read in full for this challenge; no `@api.constrains` spanning multiple lines of the same move was found). A bill with a freight line (`wt_tax_id` → 1% record) and an installation line (`wt_tax_id` → 3% record) is representable exactly as-is on the model.

### 2.2 Same payment — SPLIT FINDING, depends on which module is active

**Base module (`l10n_th_withholding_tax`) alone — HIGH GAP.** Direct read of `wizard/account_payment_register.py:38-72` (`_compute_amount`):

```python
amount_wt = sum(inv_lines.mapped(lambda l: l.wt_tax_id.amount / 100 * l.price_subtotal))  # line 50-52, correctly sums ALL lines regardless of rate
...
if amount_wt:
    self.amount -= amount_wt                                    # line 60 — total reduction IS correct, multi-rate-safe
    self.show_payment_difference = True                          # line 62
    wt_tax = inv_lines.mapped("wt_tax_id")                        # line 63 — the SET of distinct WHT taxes across all paid lines
    if wt_tax and len(wt_tax) == 1:                                # line 64 — ⚠ gate: exactly one distinct rate
        self.wt_tax_id = wt_tax
        self.writeoff_account_id = self.wt_tax_id.account_id
        self.writeoff_label = self.wt_tax_id.display_name
```

When `len(wt_tax) > 1` (freight + installation, two distinct `account.withholding.tax` records), **the `if` body at lines 64-67 never executes**: `self.wt_tax_id` stays empty, `writeoff_account_id` and `writeoff_label` are never populated by this module. Downstream, `_compute_payment_difference_handling` (lines 89-93) only forces `payment_difference_handling = 'reconcile'` `if record.wt_tax_id:` — which is now false. **Consequence: the payment amount is still correctly reduced by the combined WHT total, but no write-off journal line is auto-created by this module, and `wt_tax_id` is never set on any resulting GL line.** Practically, Odoo core falls back to its own default payment-difference handling (commonly "keep open," requiring manual reconciliation) — and even if a user manually reconciles the difference, nothing in this module tags the resulting line(s) with `wt_tax_id`, `tax_tag_ids`, or a WHT account. Both the certificate mechanism (`_get_wt_move_line`, filters on `account_id ∈ wt_account_ids`) and the PND override branch (joins on `account_move_line.wt_tax_id`) require exactly the metadata this code path fails to produce in the multi-rate case. **This confirms the docstring's "case 1 tax only" caveat is not a documentation nicety — it is an accurate description of a real functional boundary, independently re-derived from the conditional logic itself, not merely quoted from the comment.**

**With `l10n_th_withholding_tax_multi` also installed — RESOLVED.** Direct read of `l10n_th_withholding_tax_multi/models/account_payment.py`:

- `_compute_payment_difference_handling` (lines 11-25) explicitly checks `if len(lines.mapped("wt_tax_id")) > 1:` (line 23) and sets `payment_difference_handling = 'reconcile_multi_deduct'` (line 25) — a distinct handling mode specifically for the multi-rate case.
- `_update_vals_multi_deduction` (lines 37-82) iterates **every WHT-tagged move line individually** (`for line in move_lines.filtered(lambda x: x.wt_tax_id.id != False):`, line 53) and builds one `account.payment.deduction` record per line (lines 72-81), each carrying its own `wt_tax_id`, `account_id` (from that specific tax record's configured account — i.e., freight's 1% account and installation's 3% account can differ), `base_amount`, and `amount`.
- `_prepare_deduct_move_line` (lines 85-92) propagates `wt_tax_id` and `tax_tag_ids` onto the resulting posted `account.move.line` — which is exactly the metadata the certificate and PND mechanisms need.

**Conclusion for this sub-question:** multiple WHT rates in one payment are **only correctly posted, tagged, and traceable if `l10n_th_withholding_tax_multi` is installed alongside the base module.** With the base module alone, the payment amount is arithmetically correct but the WHT metadata (account routing, `wt_tax_id` tagging) required by every downstream consumer is silently dropped for all lines once more than one distinct rate is involved.

### 2.3 Same certificate — YES for amounts, PARTIAL for statutory income-type classification

`_compute_wt_cert_data` (`withholding_tax_cert.py:237-285`) builds `wt_line` by iterating **every** journal item on the source payment/entry whose account is `wt_account=True` (`_get_wt_move_line`, lines 310-320) — this is not limited to one rate. Each resulting `withholding.tax.cert.line` independently captures `wt_percent = move_line.wt_tax_id.amount` and `amount = abs(move_line.balance)` (`_prepare_wt_line`, lines 292-307) — **so a single certificate genuinely can, and (given correctly-tagged GL lines) will, show two lines with two different rates**, e.g. 1% on the freight amount and 3% on the installation amount, matching Boss's "one certificate with multiple income lines" scenario.

**However:** `wt_cert_income_type` — the statutory income-type classification (one of the 14 codes in `WHT_CERT_INCOME_TYPE`, e.g. "5. ค่าจ้างทำของ ค่าบริการ ค่าเช่า ค่าขนส่ง ฯลฯ") — **is defined as a field on `withholding.tax.cert.line` itself (`line 375-377`, so the schema supports a different income type per line), but the code that populates it does not vary it per line.** `_prepare_wt_line` sources it from `self._context.get("wt_cert_income_type")` (line 295) — a single value read from the *certificate-creation wizard* (`create_withholding_tax_cert.py`, field `wt_cert_income_type`, lines 31-33), chosen **once per certificate**, before any line is built, and applied identically to every `wt_line` row constructed in that single `_compute_wt_cert_data` pass (the loop at lines 284-285 does not change `self._context` between iterations). Confirmed directly in `create_wt_cert()` (`create_withholding_tax_cert.py:88-136`, esp. line 127: `"wt_cert_income_type": self.wt_cert_income_type`) and in the batch variant `create_wt_cert_multi()` (lines 138-188, esp. `shared_ctx` at 173-178) — even the "multi" wizard is multi only in the sense of *creating one certificate per selected document in a batch*, not splitting one document's multiple rates across differently-classified lines.

**Finding, stated precisely:** the data model *allows* per-line income-type differentiation (the field exists on the line, and a user could manually edit each line's `wt_cert_income_type` after creation via the `_onchange_wt_cert_income_type` onchange at lines 416-420), but the **automated create-flow never uses that capacity** — it always stamps every line on a given certificate with the single income type the preparer picked for the whole document. In Boss's freight/installation example, both happen to fall under the same statutory code (`"5"`, which the source list bundles ค่าจ้างทำของ/services, ค่าเช่า/rental, and ค่าขนส่ง/transport together — see `WHT_CERT_INCOME_TYPE` line 62), so this specific pair may not trigger a visible misclassification. But nothing in the code guarantees that for an arbitrary pair of income types on one document, and no validation warns the preparer if the lines' actual underlying WHT rates imply different statutory categories than the one selected. **This is a genuine, source-confirmed gap — not resolvable without either (a) code changes to source `wt_cert_income_type` per-line from something on the move line itself (e.g., product category or the WHT tax record), or (b) a manual per-line review step by the preparer, which nothing in the UI currently prompts for.**

### 2.4 Same PO — Not applicable (§1: WHT is never modeled at PO level in this tree).

---

## 3. Are Stockable Product Lines Excluded from WHT? (Required Proof Item 3)

**NOT FOUND — no exclusion exists.** This reconfirms, for this specific challenge, the finding already established in `01_ACC_WHT_PURCHASE_SIDE_PROOF.md` §7 (independently re-checked here rather than merely cited): `product.template.supplier_wt_tax_id` and `product.template.wt_tax_id` (`models/product.py:9-10`) carry **no `domain=` argument and no product-type conditional** — a stockable product can be assigned a WHT tax exactly like a service product. `_compute_wt_tax_id` (`models/account_move.py:17-28`) branches purely on `move_id.move_type`, never on `product_id.type`/`detailed_type`. A fresh grep for `detailed_type|product_type|'service'|type_service|consu` across `l10n_th_withholding_tax`, `_multi`, and `_cert` returns zero matches. **Stockable-product-line exclusion is a business/configuration convention SMEsPlus (or any deploying company) must enforce by policy — it is not a code-level guarantee.**

---

## 4. Can Service/Charge Lines Carry Different WHT Types/Rates? (Required Proof Item 4)

**YES, confirmed.** Two independent mechanisms both support this: (a) at the **product** level, each `product.template` has its own `supplier_wt_tax_id`/`wt_tax_id`, so two different service products naturally default to two different rates (§1); (b) at the **line** level, `account.move.line.wt_tax_id` is `store=True, readonly=False` (`models/account_move.py:9-15`), meaning even two lines using the *same* product could be manually overridden to different rates if needed. Both are cited and already exercised structurally in §2.1.

---

## 5. Posting Behavior for Multiple WHT Rates in One Payment (Required Proof Item 5)

Fully covered in §2.2. Summary: **base module alone → payment amount correct, GL/certificate/report traceability broken (HIGH GAP)**; **base + `l10n_th_withholding_tax_multi` → correct per-rate posting, each rate its own deduction line with its own account routing (RESOLVED)**.

---

## 6. 50-TWI Output Behavior — One Certificate or Split by Rate? (Required Proof Item 6)

**One certificate per source document (payment or journal entry), containing multiple income lines when multiple WHT-tagged GL lines exist on that document — not split into multiple certificates by rate/type.** Confirmed directly: `_get_wth_cert_model_view` (`withholding_tax_cert.py:344-350`) selects between a single-record view and a `create_withholding_tax_cert_multi` view based only on **how many source documents (`active_ids`) were selected** for cert creation, not on how many distinct WHT rates exist within one document. `create_wt_cert_multi()` (`create_withholding_tax_cert.py:138-188`) loops `for active_id in active_ids` — i.e., **one certificate per selected payment/entry**, full stop; there is no code path anywhere in this module that takes one document with two rates and produces two separate certificates from it. This directly answers Boss's item 6: the behavior is **"one certificate with multiple income lines,"** not **"multiple certificates split by WHT type/rate."**

---

## 7. PND3/PND53 Output Behavior — Grouping (Required Proof Item 7)

**No grouping/aggregation at all — one CSV row per underlying `account_move_line.id`, in both the base handler and the WHT-aware override**, re-confirmed by direct full read of both files in this challenge (not merely cited from document 04):

- `02 OTHER/l10n_th_reports/models/tax_report_pnd.py:33`: `ROW_NUMBER() OVER(ORDER BY account_move_line__move_id.date, partner.name, account_move_line__move_id.name, account_move_line.id)` — no `GROUP BY`. This is the **base handler**, which joins on `account_move_line.tax_line_id` (standard Odoo tax lines, line 57) — **not** `wt_tax_id` at all. On its own, without the override below, this handler would not read the WHT write-off/deduction lines created by the payment-register mechanism (§2.2) — it reads a structurally different kind of tax line.
- `addons_extra/l10n_th_withholding_tax/models/tax_report_pnd.py:14-21`: same window-function pattern, no `GROUP BY`, **UNION of two branches** — Branch 1 mirrors the base handler's standard tax-line query; Branch 2 (lines 55-93) joins `account_move_line.wt_tax_id → account_withholding_tax → account_tax`, which **is** the branch that reads the payment-register/multi-deduction write-off lines from §2.2, filtered by `account_move_line.payment_id IS NULL AND ...payment_state != 'not_paid'`.

**Consequence for Boss's item 7 (grouping by payee, payment date, WHT type, certificate, and rate):** the export does **not** group by any of these dimensions — every qualifying journal line is its own row, each independently carrying its own payee (via the joined `partner`), date, and rate-derived `tax_type`/`wht_amount`. **This means a correctly-posted multi-rate payment (i.e., one where `l10n_th_withholding_tax_multi` produced properly-tagged deduction lines, §2.2) *would* appear as two separate, correctly-typed rows in the PND export** — freight as a `-1`/`'Transportation'` row, installation as a `-3`/`'Service'` row, both under the same payee/date. There is no report-level re-aggregation that would collapse or conflate them. This is a genuinely positive finding **conditional on** the payment having been posted with per-line WHT tagging in the first place (§2.2's base-module gap) — if the base module alone silently drops `wt_tax_id` tagging for a multi-rate payment, **neither PND branch would see that payment's WHT lines at all**, since Branch 2's join requires a non-null `wt_tax_id`.

---

## 8. Partial Payment Behavior — Proration (Required Proof Item 8)

**Split finding, mirroring §2.2's module-dependent pattern.**

**Base module (`wizard/account_payment_register.py:54-57`):**
```python
for move in inv_lines.mapped('move_id'):
    for payment in move.matched_payment_ids.filtered(lambda x: x.state not in ('canceled','rejected')):
        payment_move = payment.move_line_ids.filtered(lambda x: x.wt_tax_id and x.move_id.state=='posted')
        amount_wt -= sum(payment_move.mapped('debit'))-sum(payment_move.mapped('credit'))
```
This subtracts **all** previously-paid WHT amounts, summed across every rate together, from the newly-computed **total** `amount_wt`. This is arithmetically self-consistent for a *single-rate* document across multiple partial payments (matching what `test_01`/`test_02` in `tests/test_withholding_tax.py` actually exercise — both are single-rate scenarios). It does **not** track "how much of rate A vs. rate B has been paid so far" as separate figures — but per §2.2, the base module's write-off mechanism never correctly activates for a multi-rate document in the first place, so this aggregate-proration logic is effectively moot for the multi-rate case: **there is nothing correctly tagged for it to prorate against on subsequent partial payments.**

**With `l10n_th_withholding_tax_multi` (`models/account_payment.py:37-82`):** proration is **per-line, per-tax-record**, using a composite key `key = str(line.id)+'_'+str(wt.id)` (or, for the already-paid lookup, `str(payment_move.wt_move_line.id)+'_'+str(payment_move.wt_tax_id.id)`, lines 47, 57) — each specific invoice line's specific WHT rate is tracked independently (lines 58-69: `if amount_paid: if amount_topay >= amount_paid: ... else: ...`). This correctly handles the case where, e.g., the freight WHT was fully paid in an earlier partial payment but the installation WHT was not — each is prorated against its own history, not a blended total.

**Conclusion:** partial-payment proration for a multi-rate document is **only correctly line-and-rate-specific with `l10n_th_withholding_tax_multi` installed.** The base module's proration logic is aggregate-only and, more fundamentally, sits downstream of a write-off mechanism that does not correctly engage for multi-rate documents at all.

---

## 9. Overall Verdict for ACC-WHT-06 (Required Proof Items 9-10)

Per Boss's explicit instruction — *"If the current source only supports one WHT type per document/payment, mark as HIGH GAP. If source supports multiple WHT lines, cite exact source paths and line numbers."* — both conditions are true, of two different, both-present modules in the same reference tree, so this team reports both rather than collapsing them into one answer:

- **`l10n_th_withholding_tax` in isolation: HIGH GAP.** The payment-registration write-off mechanism (`wizard/account_payment_register.py:59-67, 89-93`) is explicitly, structurally single-rate-only (`if wt_tax and len(wt_tax) == 1:`) — its own docstring says as much (`"Useful for case 1 tax only"`, lines 9-13 and mirrored at `models/account_payment.py:9-13`). For a document with more than one distinct WHT rate, the payment amount nets correctly but **no GL line is created with the correct WHT account/tag**, which breaks both the 50-twi certificate (`_get_wt_move_line` needs a `wt_account`-flagged line) and the PND3/PND53 export's WHT-aware branch (needs a non-null `wt_tax_id` on the line) for **every** line of that payment, not just the "extra" one.

- **`l10n_th_withholding_tax` + `l10n_th_withholding_tax_multi` together: multiple WHT lines are supported, cited exactly.** Per-line deduction creation: `l10n_th_withholding_tax_multi/models/account_payment.py:37-82` (`_update_vals_multi_deduction`) and `:85-92` (`_prepare_deduct_move_line`). Per-rate partial-payment proration: same file, `:42-51` (paid-amount lookup) and `:58-69` (remaining-amount calculation). Multi-line certificate capture (module-independent, already true in the base cert module): `withholding_tax_cert.py:284-285, 292-307`. Multi-row, ungrouped PND export (module-independent once lines are correctly tagged): `02 OTHER/l10n_th_reports/models/tax_report_pnd.py:33` and `addons_extra/l10n_th_withholding_tax/models/tax_report_pnd.py:14-21, 55-93`.

- **Open question this audit cannot resolve from source alone:** whether `l10n_th_withholding_tax_multi` is part of the module combination Accounting/Tax intends to treat as the reference baseline going forward. If it is not, `ACC-WHT-06` for the **payment-posting** dimension specifically must be treated as `HIGH GAP` without qualification. If it is, that dimension moves to `RESOLVED (module-dependent)`, but the **certificate income-type-per-line** gap (§2.3) remains open regardless of which module combination is in use, since it exists in the base `l10n_th_withholding_tax_cert` module and is not touched by `l10n_th_withholding_tax_multi` at all.

---

## 10. Disposition Table for `ACC-WHT-06`

| Sub-item | Disposition | Basis |
|---|---|---|
| WHT modeling level | **RESOLVED (documented)** | Line-level source of truth, never PO-level; §1 |
| Multiple rates on same bill | **RESOLVED** | No cross-line constraint; §2.1 |
| Multiple rates on same payment — base module only | **HIGH GAP** | `len(wt_tax) == 1` gate silently drops WHT metadata for all lines when violated; §2.2, §5 |
| Multiple rates on same payment — base + multi module | **RESOLVED** | Per-line deduction records, correctly tagged; §2.2, §5 |
| Stockable-line exclusion | **NOT FOUND (unenforced convention)** | Re-confirmed; §3 |
| Service lines with different rates | **RESOLVED** | §4 |
| 50-twi certificate — amounts/rates per line | **RESOLVED** | §2.3, §6 |
| 50-twi certificate — statutory income-type per line | **PARTIAL / GAP** | Schema supports it; create-flow code does not use that capacity; §2.3 |
| PND3/PND53 — multi-rate row separation | **RESOLVED, conditional on correct upstream tagging** | No grouping, one row per line; §7 — but depends on the payment-posting gap above being closed first |
| Partial payment proration — base module only | **HIGH GAP (moot — see above)** | Aggregate-only, and sits downstream of a mechanism that doesn't engage correctly for multi-rate; §8 |
| Partial payment proration — base + multi module | **RESOLVED** | Per-line-per-tax composite-key tracking; §8 |

**This document does not declare Gate PASS and does not authorize Team B or Team C.** Per Boss's instruction, Account WHT closure (`05_ACC_WHT_FINAL_DISPOSITION_AND_BOSS_RECOMMENDATION.md`) is updated to reflect `ACC-WHT-06` as a required, now-answered, but not-fully-resolved item — see that document's updated §2 and §8.
