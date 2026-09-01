# l10n_th_withholding_tax_multi — Targeted Proof (Boss WHT Decision Follow-Up)

## Session Metadata

| Field | Value |
|---|---|
| Deliverable | `09_ACC_WHT_MULTI_MODULE_TARGETED_PROOF.md` |
| Trigger | Boss WHT Decision — Partial Acceptance Only (post-`08`): *"ACC-WHT-06 remains HIGH unless `l10n_th_withholding_tax_multi` is proven as part of the required deployed module set. ... Create a targeted proof for `l10n_th_withholding_tax_multi`."* |
| Team | Team A5 (independent audit), continuing directly from `08_ACC_WHT_MULTI_TYPE_MULTI_RATE_CHALLENGE.md` |
| Repo | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Branch | `audit/account-wht-grpa-m18-closure-010` |
| Working location | An isolated `git worktree` checked out from this branch's tip (`358ea9a`), separate from the shared `AI-Collaboration-Hub` folder, per Boss's instruction to stop using the shared directory after the earlier branch-collision incident |
| Date | 2026-09-02 |
| Mode | Evidence-first / clean-room / **no development authorization** |
| Source tree examined | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE/addons_extra/l10n_th_withholding_tax_multi/` |

**What this document does NOT do:** it does not decide whether `l10n_th_withholding_tax_multi` *is* part of the intended SMEsPlus reference/target module baseline — that remains a Boss/Accounting-Tax decision, restated at the end of this document, not resolved by it. This document answers only the six specific proof requirements Boss asked for, so that decision can be made with full evidence.

---

## 0. New Primary Evidence Not Previously Cited

`08` relied on static reading of the module's business-logic files. This document adds a file not previously read in this session: **`addons_extra/l10n_th_withholding_tax_multi/tests/test_withholding_tax_multi.py`** (SHA-256 `519bef123449293235d018439c50830f02712f1c4565082a0420dcd23690d989`, 269 lines, full file read, independently computed via Python `hashlib.sha256`) — four test cases (`test_01` through `test_04`), each constructing a real `account.move`/`account.payment.register` cycle via Odoo's `Form` test helper and asserting on the *actual resulting posted records*, not merely on intermediate wizard state. This is materially stronger evidence than anything cited in `08`: it is the module's own author-written oracle for what "correct" multi-rate behavior looks like, and — critically for proof items 3–4 below — `test_04` asserts directly on `payment.move_line_ids` (the actual posted GL lines), which is exactly the artifact the 50-twi certificate and PND3/PND53 mechanisms consume.

**Standing caveat, unchanged from every other document in this session:** no live Odoo runtime was installed or executed in this session. Every claim below reports what the test file *asserts*, not *observed passing test output*. This is static source verification of the test's own logic and target values, not a live test run.

Test fixture (`addons_extra/l10n_th_withholding_tax_multi/tests/account_withholding_tax_test.xml`, SHA-256 `3cecf13e670db1922e9c98ee47db0ac31c4379c6bc52e6dc4681974b45c12d7a`, full file, independently computed via Python `hashlib.sha256`):
```xml
<record id="account_withholding_tax_data_5" model="account.withholding.tax">
    <field name="name">Withholding Tax 5%</field>
    <field name="account_id" ref="l10n_th_withholding_tax.withholding_income_tax_account"/>
    <field name="amount" eval="5"/>
</record>
```
This defines `wt_account_5` = 5% rate, used alongside the base module's own `wt_account_3` = 3% rate fixture (`l10n_th_withholding_tax/tests/account_withholding_tax_test.xml`, already cited in `01`/`06`). **Both fixture tax records point to the same underlying GL account** (`l10n_th_withholding_tax.withholding_income_tax_account`, test code `X152000`, typed as a **current-asset** account in the test fixture, `wt_account=True`). This is a test-data coincidence, not a code constraint — each `account.withholding.tax` record independently carries its own `account_id` (§3, `01_ACC_WHT_PURCHASE_SIDE_PROOF.md` §2.5), so a real deployment could route different rates to different accounts; the test simply didn't exercise that variation. Noted so this is not mistaken for a "rates share one account" rule.

---

## 1. Does It Fix Multiple WHT Type/Rate Behavior in One Bill/Payment? (Required Proof Item 1)

**Yes — confirmed at test-oracle level, not merely by static code reading.**

`test_02_create_payment_multi_withholding_tax_multi_line` (lines 134-176): builds one vendor bill with two lines, `invoice_line_ids[0].wt_tax_id = wt_account_3` (3%), `invoice_line_ids[1].wt_tax_id = wt_account_5` (5%) — **Boss's exact freight/installation shape, two distinct rates on one document.** Registers **one** payment for the whole bill and asserts, in order:
```python
self.assertEqual(payment.payment_difference_handling, "reconcile_multi_deduct")   # line 160
self.assertTrue(payment.deduction_ids)                                              # line 162
deduct_3 = payment.deduction_ids.filtered(lambda l: l.wt_tax_id == self.wt_account_3)  # line 163-165
self.assertEqual(payment.payment_difference, sum(payment.deduction_ids.mapped("amount")))  # line 168-170
payment.post()                                                                       # line 171
self.assertEqual(payment.state, "posted")                                            # line 172
self.assertEqual(payment.amount, (price_unit * 2) + sum(payment.deduction_ids.mapped("amount")))  # line 173-176
```
This is the module's own assertion that: the multi-deduct mode activates, per-rate deduction records are created and independently filterable by their own `wt_tax_id`, the total difference matches the sum of the per-line deductions, **and the payment successfully reaches `state == "posted"`** — directly superseding `08`'s static-only finding that the *base module alone* leaves the payment difference unresolved for a multi-rate document (`08` §2.2). With the multi module active, the module's own test claims a clean post.

**Unexpected but important finding, not previously surfaced:** `test_03_create_payment_one_withholding_tax_multi_line` (lines 178-214) uses **two lines with the SAME rate** (`wt_account_3` on both) and *still* asserts `payment_difference_handling == "reconcile_multi_deduct"` (line 203) and non-empty `deduction_ids` (line 205). This means the multi-deduct path is triggered by **"more than one WHT-tagged line," not "more than one distinct rate."** The exact triggering condition, `l10n_th_withholding_tax_multi/models/account_payment.py:23`, is `if len(lines.mapped("wt_tax_id"))>1:` where `lines = moves.line_ids` (**all** journal items on the move, not just the invoice lines) — this session cannot fully resolve from static reading alone whether Odoo's `.mapped()` on a Many2one field returns a length-2 result here because of the empty/`False` value contributed by the bill's own payable-control line, or for some other reason; what the source **can** confirm is that the test's own oracle exercises and expects multi-deduct behavior even for a same-rate, two-line bill. This is a positive finding for robustness (it does not appear to special-case "must differ"), but it is reported as an open, not-fully-explained mechanism rather than asserted with full certainty, consistent with this session's no-invention rule.

---

## 2. Is Line-Level WHT Tagging Preserved? (Required Proof Item 2)

**Yes — this is the single strongest piece of evidence in this document, directly asserted against posted GL lines.**

`test_04_create_payment_multi_withholding_keep_open` (lines 216-269) is constructed specifically to distinguish per-line tagging: same two-rate bill as `test_02` (3% + 5%), but the 3% deduction is explicitly marked `open = True` (deferred, not settled in this payment) while the 5% deduction is left to settle normally. After `payment.post()`:
```python
line_wt_3 = payment.move_line_ids.filtered(lambda l: l.wt_tax_id == self.wt_account_3)  # line 254-256
line_wt_5 = payment.move_line_ids.filtered(lambda l: l.wt_tax_id == self.wt_account_5)  # line 257-259
self.assertTrue(line_wt_5)   # line 260 — the SETTLED 5% deduction produced a wt_tax_id-tagged posted line
self.assertFalse(line_wt_3)  # line 261 — the DEFERRED (open) 3% deduction produced NO wt_tax_id-tagged line
```
This is a direct, line-granular assertion on `payment.move_line_ids` — the actual posted journal items, not wizard/transient state — proving two things simultaneously: (a) **each rate's deduction independently and correctly carries its own `wt_tax_id` through to the posted GL line** (confirming Boss's proof item 2 directly), and (b) the module correctly *excludes* a deferred/not-yet-settled rate from being tagged, rather than incorrectly tagging it as paid. Source basis for the tagging mechanism itself: `_prepare_deduct_move_line` (`models/account_payment.py:85-92`, previously cited in `08` §2.2) explicitly sets `wt_tax_id`, `tax_tag_ids`, and `wt_move_line` on the resulting move line from the deduction record's own fields — this test is the run-time (as-designed) confirmation that this static mechanism does what it claims.

The test continues: a **second, separate payment** for exactly the deferred amount (`price_unit * 0.03`, line 266) is posted, and `payment.move_line_ids.mapped("full_reconcile_id")` is asserted true (line 269) — confirming the deferred rate is correctly settled and reconciled in a later, independent payment. This is also relevant to Boss's original partial-payment proof item from `08` §8: it demonstrates correct per-rate deferral and later settlement, not just a same-payment multi-rate split.

---

## 3. 50-TWI Output With Multiple WHT Rates (Required Proof Item 3)

**Chained proof: test-level payment evidence (above) + previously-established static certificate mechanism (`08` §2.3, `01` §4) — no test in this module directly exercises certificate creation, so this remains a chained inference, not a single directly-asserted fact. Reported precisely as such.**

Chain of evidence:
1. `test_04` (§2 above) proves a posted `account.move.line` exists with `wt_tax_id == wt_account_5` after a multi-rate payment.
2. `wt_account_5.account_id` is `l10n_th_withholding_tax.withholding_income_tax_account` (test fixture, §0), which is flagged `wt_account=True` (base module's own test fixture, already cited in `01`/`06`) — so this posted line satisfies `_get_wt_move_line`'s filter (`account_id in wt_account_ids`, `withholding_tax_cert.py:310-320`, cited in `08` §1).
3. `_prepare_wt_line` (`withholding_tax_cert.py:292-307`, cited in `08` §2.3) would therefore build a `withholding.tax.cert.line` from this posted line with `wt_percent = move_line.wt_tax_id.amount` (= 5) and `amount = abs(move_line.balance)`.
4. Since `_compute_wt_cert_data` iterates **every** qualifying line on the payment (not just one), a certificate created from this payment would show **two** `wt_line` rows — one for the settled 5% deduction (tagged), and **none** for the deferred 3% deduction (since it was never tagged with `wt_tax_id` while open, per `test_04`'s own assertion) until that second, later payment is made and a *separate* certificate (or an amended one) is created from it.

**Conclusion:** with the multi module active and correctly functioning as its own tests assert, a multi-rate payment **does** produce the GL-level data the certificate mechanism needs to show multiple correctly-rated lines — but this session found **no test anywhere in this module that actually creates a `withholding.tax.cert` record and asserts on its `wt_line` contents**. This is a **gap in the module's own test coverage**, not a defect in the mechanism as statically traced — it means the certificate-side outcome, while well-supported by chained evidence, is not directly, independently test-asserted the way the payment-posting outcome is in §1-§2. The certificate's income-type-per-line limitation (single wizard-selected value applied to every line, `08` §2.3) is **unaffected by the multi module** — that gap lives entirely in `l10n_th_withholding_tax_cert`, a module the multi module does not touch or extend.

---

## 4. PND3/PND53 Output With Multiple WHT Rates (Required Proof Item 4)

**Same chained-evidence character as §3: strong, but not directly test-asserted anywhere in this module.**

The PND3/PND53 override query (`addons_extra/l10n_th_withholding_tax/models/tax_report_pnd.py:86-92`, cited in `08` §7) requires, per row: `account_move_line.wt_tax_id` non-null, `account_move_line.payment_id IS NULL`, `account_move_line__move_id.payment_state != 'not_paid'`. From `test_04`: the settled 5% deduction line has `wt_tax_id` set (§2 above); after the *second* payment fully settles the residual and `full_reconcile_id` is set (line 269), the underlying bill's `payment_state` would be expected to reach `'paid'` (standard Odoo reconciliation behavior, not itself re-verified in this source tree, since `payment_state` computation lives in Odoo core `account` module, out of this session's controlled tree) — satisfying the `!= 'not_paid'` condition. **No test in `l10n_th_withholding_tax_multi` or `l10n_th_reports` directly queries or asserts on PND3/PND53 CSV output for a multi-rate document** — `l10n_th_reports/tests/test_tax_report.py` (cited in `04`/`06`) tests PND3/PND53 with single-rate, multi-*tax-amount* invoices (two different taxes on two lines, but examined for their independent row output, not specifically framed as a "multi-WHT-rate-on-one-payment" scenario routed through the multi-deduction module). **This is therefore the weakest-evidenced of the four required proof items**: plausible and consistent with every mechanism traced, but with no direct end-to-end test connecting "multi-rate payment via `l10n_th_withholding_tax_multi`" to "correct multi-row PND3/PND53 CSV output" anywhere in this source tree.

---

## 5. Purchase-Side vs. Sales-Side Behavior, Proven Separately (Required Proof Item 5)

**Purchase-side: proven at test-oracle level (all four tests, §1-§2). Sales-side: NOT FOUND — no test, and this is a real, newly-confirmed gap, not an assumption.**

All four tests in `test_withholding_tax_multi.py` construct their invoice via `_create_invoice(..., invoice_type, ...)` with the literal string `"in_invoice"` passed at every call site (lines 106, 140, 184, 222) — **zero occurrences of `"out_invoice"` anywhere in this test file**, confirmed by direct re-read of the full 270-line file. Cross-checked against `08` §2.2's static finding (re-confirmed here): `l10n_th_withholding_tax_multi/models/account_payment.py` contains no `payment_type`/`move_type` conditional anywhere (zero grep hits, re-run in this session), so the code path is *structurally* reachable for a sales-side (`out_invoice`, customer-withheld) multi-rate scenario exactly as it is for purchase-side — but **no test anywhere in this module exercises that path**, and this session found no evidence (test, code comment, or documentation) that anyone has verified it. This directly compounds the sales-side gap already established in `02_ACC_WHT_SALES_SIDE_PROOF.md` (no WHT-receivable account type, no certificate-evidence tracking, and — per that document's own finding — the base module's *own* sales-side test, `test_03_withholding_tax_customer_invoice`, stops at `action_post()` and never reaches payment registration at all). **The multi module does not close that gap; it does not touch it.** Purchase-side multi-rate behavior is well-evidenced; sales-side multi-rate behavior remains entirely unevidenced, on top of sales-side single-rate payment/reconciliation already being unevidenced.

---

## 6. Remaining Legal/Tax Review Items (Required Proof Item 6)

No new legal/tax questions are introduced by this document beyond what `05` §5 and `08` already registered. Restated here for completeness, with this document's specific contribution noted:

1. (Unchanged from `05`/`08`) Whether Thai Revenue Department rules require a specific GL account classification for WHT credits, and the ten other items already in `05` §5 — none are resolved or newly implicated by the multi-module test evidence in this document.
2. **(New, specific to this document)** Whether the fixture-observed pattern of routing multiple different WHT rates to the **same** GL account (§0) is acceptable Thai accounting/tax practice, or whether statutory/audit-trail requirements expect rate-level account segregation — this session found no code-level constraint either way (each `account.withholding.tax` record can independently point to a different account; the test simply didn't exercise that), so this is a configuration/policy question for Accounting/Tax, not a code gap.
3. **(New, specific to this document)** The out-of-tree `account_payment_multi_deduction` (OCA base module) dependency — required by `l10n_th_withholding_tax_multi/__manifest__.py:11`, confirmed **absent from this source tree** (`find` returned zero results, §0) — means the actual mechanics of how a `deduction_ids` record becomes a posted `account.move.line` at `payment.post()` time cannot be independently source-verified in this session. This session's confidence in §1-§2 rests on this addon's own test assertions (which reference that mechanism's outcomes) plus this addon's own override code (which is in-tree and was directly read) — not on having read the underlying OCA module itself. This is a **scope boundary**, not a legal/tax item, but it is a real limit on how far "proven" extends and should be read alongside the disposition below.

---

## 7. Disposition for This Targeted Proof

| Proof item | Finding | Confidence basis |
|---|---|---|
| 1. Fixes multi-rate payment posting | **YES** | Direct test assertion (`test_02`), payment reaches `state == "posted"` |
| 2. Line-level WHT tagging preserved | **YES** | Direct test assertion (`test_04`) on actual posted `move_line_ids` |
| 3. 50-twi output with multiple rates | **LIKELY, chained evidence only — no direct test** | Static mechanism trace (`08` §2.3) + `test_04`'s posted-line evidence; no test creates a certificate |
| 4. PND3/PND53 output with multiple rates | **LIKELY, chained evidence only — no direct test, weakest of the four** | Static query trace (`08` §7) + inferred `payment_state` progression; no test connects the two |
| 5. Purchase-side proof | **YES, test-level** | All four tests, purchase-side only |
| 5. Sales-side proof | **NOT FOUND** | Zero tests; compounds existing gap in `02` |

**This document does not upgrade `ACC-WHT-06`'s overall status to RESOLVED.** Per Boss's standing decision, `ACC-WHT-06` remains **HIGH** pending Boss/Accounting-Tax's own determination of whether `l10n_th_withholding_tax_multi` (and its out-of-tree OCA dependency, `account_payment_multi_deduction`) will actually be part of the deployed/reference module set — a decision this audit is not authorized to make. What this document adds: the purchase-side payment-posting and line-tagging questions (items 1-2) now have **direct test-level evidence**, not merely static code reading, meaningfully strengthening the case *if* Boss decides the module is in scope. Items 3-4 (certificate and PND output) remain **plausible but not directly test-proven**, and item 5 confirms the sales-side gap is **not addressed** by this module at all. No Gate PASS. No Team B or Team C authorization. Boss remains sole Final Approver.
