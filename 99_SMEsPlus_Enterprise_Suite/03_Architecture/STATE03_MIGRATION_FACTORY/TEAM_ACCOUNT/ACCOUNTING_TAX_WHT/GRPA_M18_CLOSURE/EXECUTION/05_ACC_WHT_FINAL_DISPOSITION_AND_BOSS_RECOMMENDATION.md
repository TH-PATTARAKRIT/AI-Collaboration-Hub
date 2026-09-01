# ACC-WHT GRPA-M18 Closure — Team A5: Final Disposition & Boss Recommendation

Session: `SMEPLUS-26-09-01-ACC-WHT-GRPA-M18-CLOSURE-001`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `audit/account-wht-grpa-m18-closure-010`
Evidence base: CORR-007A, commit `deceb7339b39eba309236782f159f8393224f5fd`, branch `audit/inventory-core-corr007a-grpa-m18-wht-50twi-009`
Date: 2026-09-02
Mode: Evidence-first / clean-room / **no development authorization**

Boss Domain Ruling recap (governing this entire session): WHT is Accounting/Tax-owned, not Inventory-owned; it has a purchase side (company withholds from a vendor, issues 50 TWI, files PND3/PND53) and a sales side (customer withholds from the company, company records a WHT credit/receivable and keeps the received certificate); WHT is service-only and does not involve product stock or `stock.move`; GRPA-M18 is to be removed from the Inventory Core Backbone High blocker list and owned end-to-end by the Account Team.

## Boss WHT Decision — Recorded (Partial Acceptance Only)

Boss has reviewed this package and issued the following explicit ruling, recorded here verbatim in substance:

- **ACCEPTED:** GRPA-M18 removal from the Inventory High blocker list, and transfer to Accounting/Tax ownership (§3–§4 below).
- **NOT ACCEPTED:** full closure of Account WHT. Session remains open.
- **`ACC-WHT-06` standing status: HIGH**, unless and until `l10n_th_withholding_tax_multi` is proven to be part of the required deployed module set — a decision reserved to Boss/Accounting-Tax, not this audit.
- **Required next action (completed in this round):** a targeted proof of `l10n_th_withholding_tax_multi` against six specific requirements — produced as `09_ACC_WHT_MULTI_MODULE_TARGETED_PROOF.md`, referenced throughout §2's `ACC-WHT-06` row and §8 below.
- Standing constraints reaffirmed by Boss: no WHT closure declaration, no Gate PASS, no Team B authorization, no Team C authorization, no Development authorization. Boss remains sole Final Approver.

---

## 1. Independent Challenge Pass (Team A5 vs. Teams A1–A4)

Per the same "no unsupported closure" discipline CORR-007A's Team 5 applied, this team independently re-verified — not merely re-read — a representative, load-bearing sample of every team's citations directly against the source tree at `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE/`, using `shasum -a 256` and `grep -n` run fresh in this session, independent of any of the four teams' own tool calls.

**Re-verified directly by Team A5 (all confirmed exact matches, no discrepancies in substance):**

| Claim | Team | Independently re-run by A5 | Result |
|---|---|---|---|
| `payment_id.amount == price_unit * 0.97` (net-of-WHT payment) | A1 | `grep -n "0.97\|price_unit" tests/test_withholding_tax.py` | Confirmed at line 159 exactly as cited |
| Payment-register wizard has zero `payment_type` references (no inbound/outbound gate) | A2 | `grep -n "payment_type" wizard/account_payment_register.py` | Confirmed — zero matches |
| `account.account.wt_account` is a single undirected boolean (no receivable/payable split) | A2 | `grep -n "wt_account\b" models/account_withholding_tax.py` | Confirmed at lines 15, 31 |
| `_compute_wt_tax_id` branches on `move_type`, not on `stock`/product type | A1, A2 | Direct read of `models/account_move.py:17-28` | Confirmed exactly as both teams cite it |
| Two files named `tax_report_pnd.py` exist, one `_inherit`-without-`_name` overrides the other | A4 | `find` + `grep -n "_name\|_inherit"` on both files | Confirmed — override pattern verified directly |
| "WHT Condition" column hardcoded to literal `'1'` | A4 | `grep -n "'1'" models/tax_report_pnd.py` | Confirmed at line 47: `'1' as wht_condition` |
| `res.partner.branch` field exists at `l10n_th_partner/models/res_partner.py:15`, module out of the cert dependency chain | A3 | Direct read of file + manifest chain walk | Confirmed |
| Zero `stock.move`/`stock.quant`/`stock.picking` references anywhere in the WHT module family | A1, A2, A4 | Independent repo-wide grep across all 7 WHT-related module directories + all 4 relevant manifests | **Confirmed — zero matches, own independent grep, not a re-statement** |

**SHA-256 manifest check:** Team A5 independently recomputed SHA-256 for 50 distinct evidence files cited across all four team documents (full list in `06_ACC_WHT_SHA256_MANIFEST.txt`), using a fresh Python `hashlib.sha256` pass (not shell `shasum`, as an independent implementation check) against the same source tree. **All 50 files exist and all 50 recomputed hashes match every inline citation in the body text of documents 01–04, with one exception noted below.**

**Discrepancy found and corrected — appendix truncation in `04_ACC_WHT_PND3_PND53_FILING_PROOF.md`:** the Appendix table at the end of Team A4's document contains SHA-256 strings truncated by 1–2 trailing hex characters (e.g., `02 OTHER/l10n_th_reports/models/tax_report_pnd.py` is cited in the appendix as ending `...eba62a3` — 62 characters — while the correct, 64-character hash, matching both this team's own inline citation in §1.2/§2 of the same document and Team A5's independent recomputation, is `...eba62a33f`). This affects **only the convenience appendix table** — every inline citation used to support an actual finding in the body of document 04 is correct and matches. This is reported here as a data-hygiene finding, not a substantive-conclusion error: no disposition in document 04 rests on the truncated appendix values. The canonical, corrected, independently-verified hash for every cited file is in `06_ACC_WHT_SHA256_MANIFEST.txt`, which supersedes all four teams' individual appendices for audit-trail purposes.

**Boss-only decision boundary check:** none of the four team documents declares Gate PASS, Team B authorization, or Team C authorization. Confirmed by direct read of each document's closing section.

**Unsupported-closure check:** no team declared a disposition stronger than its own evidence supports. Notably, both A1 (purchase-side) and A2 (sales-side) actively argued *against* over-closing their own findings — A1 flagged that "service-only" is not code-enforced despite strong mechanics evidence; A2 explicitly flagged that its own PARTIAL recommendation could reasonably be REMAINS HIGH if evidence-retention is treated as a hard requirement, rather than rounding up to look more resolved. This is the correct posture and this team concurs with both self-assessments.

**Legal/tax boundary check:** no team asserts Thai Revenue Department statutory compliance anywhere. All four teams affirmatively flag `LEGAL_TAX_REVIEW_REQUIRED` items rather than resolving materiality themselves. Confirmed by direct read.

**Mid-session Boss Challenge Addendum (ACC-WHT-06):** Boss issued a mandatory challenge item mid-session, requiring proof of whether one PO/bill/payment can carry multiple WHT types/rates (worked example: freight at 1% + installation at 3% on the same vendor bill). This is answered in full in `08_ACC_WHT_MULTI_TYPE_MULTI_RATE_CHALLENGE.md`, performed directly by Team A5 given its tight coupling to A1/A2/A4's already-verified findings. **Headline result: a genuine HIGH GAP was found** — the base `l10n_th_withholding_tax` module's payment-registration write-off mechanism only correctly tags a WHT GL line when exactly one distinct rate is involved across the paid lines (`wizard/account_payment_register.py:64`, `if wt_tax and len(wt_tax) == 1:`); with two or more distinct rates on one payment (Boss's own example), the payment amount still nets correctly but the WHT account routing and `wt_tax_id` tagging are silently dropped for every line, breaking both certificate and PND3/PND53 traceability. This is resolved only if `l10n_th_withholding_tax_multi` is also installed — which is a real, present module in the source tree, but whether it is part of the intended reference/target module combination is a fact this audit cannot determine from source alone and must be a Boss/Accounting-Tax decision. **This finding materially reinforces, rather than merely adds to, the existing PARTIAL disposition on `ACC-WHT-01`** (purchase-side WHT, §2 below) — multi-rate documents (a company withholding at different statutory rates for different services on the same bill) are a realistic, not edge-case, scenario for a services business, so this is not a peripheral gap.

---

## 2. GRPA-M18 (ACC-WHT) Disposition Table

| Sub-item | Description | Disposition | Basis |
|---|---|---|---|
| `ACC-WHT-01` | Purchase-side WHT (vendor bill → payment → GL → 50-twi certificate) | **PARTIAL** | Team A1: configuration (product/tax/account flags, not partner), rate computation, and deferred-to-payment net-of-WHT posting are all found and cited to exact lines, corroborated by the module's own (read, not executed) test assertions (`payment.amount == price_unit * 0.97`). Certificate is populated from posted GL data, not from bill estimates. **Not RESOLVED** because: no live Odoo execution was performed in this session (static read only); "service-only" is a configuration convention, not a code-enforced constraint — `product.supplier_wt_tax_id` carries no product-type domain; certificate generation is a manual wizard action, not automatic on payment posting; stock-dependency coverage was not extended to `l10n_th_withholding_tax_report`/`l10n_th_withholding_tax_cert_form` (though Team A5 independently closed this gap — see §1 — with a fresh repo-wide grep across all 7 modules, zero matches). |
| `ACC-WHT-02` | Sales-side WHT (customer withholds → net receipt → WHT receivable/credit → certificate retained) | **PARTIAL** | Team A2: a genuine, side-aware code path exists at the tax-configuration/invoice-line layer (`type_tax_use`/`account.withholding.tax.type = 'sale'`, dedicated `product.wt_tax_id`, `move_type`-branching compute), exercised up to invoice-posting by the module's own `test_03_withholding_tax_customer_invoice`. **Two structurally significant pieces are confirmed NOT FOUND** by exhaustive grep and full-file read: (a) a dedicated WHT-receivable/tax-credit GL account type — only a single undirected `wt_account` boolean shared by both directions exists; (b) any tracking of a customer-issued certificate as sales-side evidence — the entire `withholding.tax.cert` model, its creation wizard, and its xlsx report are built exclusively around SMEsPlus as certificate *issuer*, with `supplier_partner_id` as the only partner link and no `customer_partner_id`, no direction field, no attachment/received-document field. The payment-reconciliation mechanism that would net a customer receipt automatically is code-reachable (no direction gate — independently confirmed, §1) but **unverified by any test** for the sales side, unlike purchase-side which has two passing tests proving the money math end-to-end. |
| `ACC-WHT-03` | 50-TWI field-mapping gaps (branch number, tax-form checkboxes, WHT-condition checkboxes) from CORR-007A | **PARTIAL / REQUIRES FORM UPDATE** (mixed — see breakdown) | Team A3 independently re-derived all three gaps from current source (not copied from CORR-007A) and additionally opened the form image directly for visual re-confirmation: **Branch number → RESOLVED (not a defect)** — `l10n_th_partner` is genuinely outside the certificate stack's dependency chain, and the official form itself has no branch box for either payer or payee on this certificate type. **Tax-form checkboxes (3 of 7 missing) → ACCOUNTING/TAX CONFIGURATION pending LEGAL_TAX_REVIEW_REQUIRED**, fix classified as **REQUIRES FORM UPDATE** — the CSS layer has zero dead/unused positioning classes for the 3 missing checkboxes, meaning they are entirely absent from the print layout, not merely disabled; this is new template/layout work (measured pixel positions), not a same-day config toggle. **WHT-condition checkboxes (2 of 4 missing) → same classification**, with the added note that the "อื่นๆ (other)" option would also require a new free-text field on the model. |
| `ACC-WHT-04` | PND3/PND53 filing/export proof | **RESOLVED-AS-STRUCTURE (code path) / CONTROLLED CARRY-FORWARD (statutory layout)** | Team A4's deep inspection (the module was only cited by reference in CORR-007A, never previously deep-audited) confirms both PND3 and PND53 are backed by real, tested, callable CSV export methods with a defined 16-column layout. However: (a) **a previously-uncited structural finding** — two files are both named `tax_report_pnd.py`, and the one in `l10n_th_withholding_tax` silently monkey-patches (`_inherit`-without-`_name`) the core `_rows()` query method of the one in `l10n_th_reports`, meaning actual runtime output is deployment-dependent (different `Branch Number` source field, different `Title` derivation, added payment-state filtering) — independently confirmed by Team A5 (§1); (b) the "WHT Condition" export column is hardcoded to the literal `'1'` for every row, independently confirmed by Team A5 (§1); (c) tax-type mapping is keyed off raw WHT percentage, not an income-type code, covering only 4 categories with everything else silently blanked; (d) no Buddhist-era date conversion, no CSV escaping, no BOM/encoding handling; (e) PND3-vs-PND53 payee routing relies on a fragile case-insensitive substring match on a tag name, in a different module, applied only on the purchase side, never re-validated at export time; (f) **no official Thai Revenue Department specification is referenced anywhere in code, comments, tests, or i18n files** — statutory-layout correctness cannot be assessed from source alone. |
| `ACC-WHT-05` | Legal/Tax statutory review boundary | **LEGAL_TAX_REVIEW_REQUIRED** | No official Thai Revenue Department verification was performed or is claimed anywhere in this package. Consolidated list of every LEGAL_TAX_REVIEW_REQUIRED item raised across all four teams is in §5 below. |
| `ACC-WHT-06` | Multiple WHT types/rates in one document (Boss Challenge Addendum, added mid-session) — see `08_ACC_WHT_MULTI_TYPE_MULTI_RATE_CHALLENGE.md` and `09_ACC_WHT_MULTI_MODULE_TARGETED_PROOF.md` | **HIGH — Boss standing ruling, not yet downgraded** | WHT is modeled at the **line** level (never PO-level — zero `purchase.order` references found), and a single bill can freely carry multiple distinct `wt_tax_id` values across lines (no cross-line constraint). At **payment** time, the base module (`l10n_th_withholding_tax` alone) only correctly routes a WHT write-off to a GL account when `len(wt_tax) == 1` (`wizard/account_payment_register.py:64`) — with 2+ distinct rates on one payment, the amount still nets correctly but **no line is tagged with a WHT account or `wt_tax_id`**, breaking certificate and PND traceability for the entire payment. **Boss has ruled this stays HIGH unless `l10n_th_withholding_tax_multi` is proven part of the required deployed module set.** Document `09` supplies that targeted proof: purchase-side multi-rate payment posting (Boss item 1) and line-level WHT tagging survival (Boss item 2) are now backed by **direct test-oracle evidence** (`test_withholding_tax_multi.py`, tests 02 and 04 — a multi-rate payment reaches `state == "posted"`, and a settled vs. deferred rate on the same payment are independently, correctly tagged on the actual posted GL lines). 50-twi certificate output with multiple rates (item 3) and PND3/PND53 output with multiple rates (item 4) are supported only by **chained evidence** (static mechanism trace + the same test's posted-line facts) — no test in the module directly creates a certificate or exports a PND CSV, so these remain plausible, not directly proven. Sales-side behavior (item 5) is **confirmed NOT tested anywhere in this module** — all four of its tests are purchase-side (`in_invoice`) only, compounding the existing sales-side gap in `ACC-WHT-02`. The certificate's income-type-per-line limitation (schema supports per-line values; create-flow code stamps one wizard-selected value across every line) is unaffected by the multi module either way. **The module-baseline decision itself — whether `l10n_th_withholding_tax_multi` (and its out-of-tree OCA dependency `account_payment_multi_deduction`, confirmed absent from this source tree) is part of SMEsPlus's intended reference/target combination — remains Boss's to make; this audit does not make it.** |

---

## 3. Domain Ownership — Final Confirmation (Mandatory Proof Questions, Section A)

| Question | Answer | Basis |
|---|---|---|
| Is WHT Accounting/Tax-owned? | **Yes** | Every mechanism examined across purchase side, sales side, certificate issuance, and PND3/PND53 filing operates on `account.move`, `account.payment`, `account.tax`, `account.withholding.tax`, and `res.partner` — pure accounting-domain models. Zero touchpoints with any inventory model. |
| Is any part of WHT Inventory-owned? | **No** | No `product.type`/`detailed_type` gate exists anywhere (WHT applies identically to a stockable-flagged product as to a service product, per A1 §7) — but this is a code-level *absence of restriction*, not an inventory dependency. Applicability is governed entirely by whether a WHT tax is configured on the line, never by anything inventory-domain. |
| Is any `stock.move` required? | **No** | Independently re-confirmed by Team A5 with a fresh, repo-wide grep across all 7 WHT-related modules (`l10n_th_withholding_tax`, `_multi`, `_cert`, `_cert_form`, `_report`, `l10n_th_partner`, `l10n_th_reports`) plus all their manifests — zero matches for `stock.move`, `stock.quant`, or `stock.picking`, and zero `"stock"` string anywhere in any manifest `depends` list. |
| Is any product stock movement created by WHT? | **No** | Same evidence as above; no code path in any examined module writes to, reads from, or references a stock model. |
| Is WHT service-only? | **Configuration convention, not a code guarantee** | Thai WHT statutorily applies mainly to services/rent/professional fees, and SMEsPlus's realistic use case is services-only — but Team A1 confirmed no code-level domain/constraint prevents a stockable product from being marked WHT-eligible (`product.supplier_wt_tax_id` has no `domain=` argument at all). This distinction matters for whichever team eventually designs the SMEsPlus target implementation: "no stock.move dependency" (proven) and "service-only" (a business convention, unenforced) are two separate claims and must not be conflated. |

**Conclusion: GRPA-M18 has no Inventory Core Backbone dependency of any kind, confirmed by two independent audit passes (CORR-007A's original narrower check, and this session's full-module-family re-check).**

---

## 4. Does GRPA-M18 Still Block the Inventory Evidence Gate?

**No.** This was already the CORR-007A / Boss Domain Ruling position entering this session, and nothing found in this session's deeper accounting-process audit contradicts it — every new finding (the two-files-same-name PND monkey-patch, the sales-side receivable/certificate gaps, the hardcoded WHT-condition column) is an **Accounting/Tax-domain** finding, not an Inventory-domain one. GRPA-M18 is confirmed removable from the Inventory Core Backbone High blocker list and is fully re-owned by Accounting/Tax, tracked going forward as `ACC-WHT-01` through `ACC-WHT-05` above.

---

## 5. Consolidated LEGAL_TAX_REVIEW_REQUIRED Register

For Boss / Legal-Tax routing, every statutory-judgment item raised by any team, in one place:

1. Materiality of ภ.ง.ด.1ก พิเศษ, ภ.ง.ด.2, ภ.ง.ด.2ก tax-form checkboxes for SMEsPlus's realistic use cases vs. a possible statutory requirement to support them regardless of usage frequency (Team A3, `ACC-WHT-03`).
2. Materiality of "ออกให้ตลอดไป" (issued permanently) and "อื่นๆ" (other) WHT-condition checkboxes, same question (Team A3, `ACC-WHT-03`).
3. Whether Thai Revenue Department rules require a specific GL account classification (receivable/asset) for WHT credits claimed via CIT filing, and whether the generic shared `wt_account` boolean mechanism would satisfy that if manually configured correctly (Team A2, `ACC-WHT-02`).
4. Whether un-evidenced (no certificate-tracking), automatically-posted WHT credits are adequate substantiation for a claim, or whether physical/scanned certificate retention is a hard statutory requirement the system must actively support (Team A2, `ACC-WHT-02`).
5. Column order/column set of the PND3/PND53 CSV export vs. actual RD e-filing requirements — no official specification was available to this audit (Team A4, `ACC-WHT-04`).
6. Whether the hardcoded `'1'` "WHT Condition" value is correct for every row in every circumstance, or whether Thai WHT forms require row-level condition differentiation (Team A4, `ACC-WHT-04`, independently re-confirmed by Team A5).
7. Whether the 4-category, rate-keyed tax-type mapping (vs. the many statutory WHT income-type categories) produces materially wrong/blank filings for realistic transaction volumes (Team A4, `ACC-WHT-04`).
8. Whether Buddhist-era date conversion, CSV escaping, and character encoding/BOM handling are required for actual RD e-filing submission (Team A4, `ACC-WHT-04`).
9. Whether the fragile, tag-name-substring-based PND3-vs-PND53 payee classification (purchase-side only, unenforced at export time) reliably produces statutorily-correct routing for edge cases (Team A4, `ACC-WHT-04`).
10. Which of the two competing `_rows()` implementations (base vs. OCA-override) is the intended production configuration, since they produce materially different result sets — this is a deployment/statutory-sign-off scoping question, not resolvable from source (Team A4, `ACC-WHT-04`, independently re-confirmed by Team A5).

None of the above can be resolved by further source-code reading. All require either an official Revenue Department specification, a licensed tax advisor's judgment, or a Boss decision on acceptable business risk.

---

## 6. Non-Legal Engineering-Risk Register (Flagged Separately From the Statutory Axis)

Per Team A4's explicit recommendation, these affect correctness/consistency independent of any legal-tax judgment and should be tracked regardless of how the LEGAL_TAX_REVIEW_REQUIRED items above resolve:

1. The `tax_report_pnd.py` monkey-patch (two files, same name, silent override) makes PND3/PND53 output non-deterministic across deployments — same input data can produce different output CSVs depending on which modules are installed.
2. The `INCOME_TAX_FORM` and `TAX_PAYER` selection-list gaps on the 50-twi certificate model (`ACC-WHT-03`) are template/layout work, not one-line fixes, and should be scoped as such if the SMEsPlus target implementation needs them.
3. Certificate issuance (purchase-side) is a manual, user-triggered wizard action, not automatic on payment posting — a gap between Odoo reference behavior and any future "auto-issue on payment" requirement, if such a requirement exists for SMEsPlus.
4. The sales-side payment/reconciliation code path, while structurally reachable, has zero test coverage in the reference tree — a functional-completeness gap independent of the legal question of whether the resulting credit is adequately evidenced.
5. **(HIGH GAP, added via ACC-WHT-06)** The base `l10n_th_withholding_tax` module's payment-registration write-off mechanism does not correctly tag GL lines for documents carrying more than one distinct WHT rate — it silently drops WHT account routing and `wt_tax_id` tagging for the entire payment rather than erroring or partially degrading. This is resolved only if `l10n_th_withholding_tax_multi` is also part of the deployed module set. See `08_ACC_WHT_MULTI_TYPE_MULTI_RATE_CHALLENGE.md` §2.2, §5, §9.
6. **(added via ACC-WHT-06)** The 50-twi certificate's statutory income-type classification (`wt_cert_income_type`) is stamped uniformly across every line of a multi-rate certificate from a single wizard-selected value, even though the underlying schema supports per-line differentiation. No validation warns a preparer if a document's lines imply genuinely different statutory income categories. See `08_ACC_WHT_MULTI_TYPE_MULTI_RATE_CHALLENGE.md` §2.3.

---

## 7. Team B / Team C Authorization

- Team B (Inventory Design) authorized from this task: **NO**
- Team C (Development) authorized from this task: **NO**

---

## 8. Boss Decision Options

**Boss has already selected, in substance, Option B below** (see the "Boss WHT Decision — Recorded" box at the top of this document) — domain transfer accepted, full closure explicitly withheld, `ACC-WHT-06` held at HIGH pending the module-baseline sub-decision. The four options are retained here as the reasoning record and because Option B's module-baseline question is itself still open pending Boss's review of document `09`.

**A. ACCEPT ACCOUNT WHT CLOSURE** — accept `ACC-WHT-01` (purchase-side) and `ACC-WHT-03`'s branch-number sub-item as sufficiently evidenced for now, explicitly understanding: purchase-side is PARTIAL (static-read only, "service-only" unenforced, manual certificate issuance); the two 50-twi checkbox gaps remain open pending form-update work and legal-tax materiality sign-off; PND3/PND53 code path is sound but statutory-layout correctness is unverified against an official spec; sales-side WHT is the weakest finding in this package (real code, but no receivable-account type, no certificate-evidence tracking, no test coverage) and would need explicit separate acceptance or escalation.

**B. ACCEPT PARTIAL CLOSURE WITH CONTROLLED ACCOUNTING/TAX CARRY-FORWARD** — accept the domain-ownership finding (GRPA-M18 is definitively removed from Inventory, confirmed by two independent audit passes) and the purchase-side/PND-structure findings as adequate evidence-gathering for now, while explicitly carrying forward as open Accounting/Tax work: (i) the sales-side receivable-account-type and certificate-evidence gaps (`ACC-WHT-02`), (ii) the two 50-twi form-update items (`ACC-WHT-03`), (iii) the multi-rate payment-posting HIGH GAP and certificate income-type-per-line gap (`ACC-WHT-06`) — **including a required Boss/Accounting-Tax decision on whether `l10n_th_withholding_tax_multi` is part of the intended module baseline, since that single decision resolves or leaves open the HIGH GAP**, (iv) the ten LEGAL_TAX_REVIEW_REQUIRED items in §5, and (v) the six engineering-risk items in §6. **This is the disposition this team's evidence most directly supports** — every sub-item has a named owner (Accounting/Tax), a clear description of what's missing, and no sub-item is being closed on insufficient evidence.

**C. KEEP WHT HIGH UNDER ACCOUNTING/TAX** — if Boss judges the sales-side gaps (no receivable account type, no certificate-evidence retention, zero test coverage of the money flow) to be disqualifying on their own, `ACC-WHT-02` specifically (or all of GRPA-M18) can remain High under Accounting/Tax ownership pending a dedicated design/fix cycle — Team A2 explicitly flagged that this reading of its own evidence is defensible, not a stretch.

**D. REQUEST LEGAL/TAX REVIEW** — route the consolidated register in §5 to a qualified Thai tax advisor before any of `ACC-WHT-01` through `ACC-WHT-04` is treated as more than a code-structure finding. Given that no team in this package had access to an official Revenue Department specification, and given ten distinct statutory-judgment items were surfaced, this option is not mutually exclusive with A, B, or C — it can and arguably should be layered on top of whichever closure option Boss selects.

This team's own recommendation, for what it is worth: **Option B**, layered with **Option D** for the specific items in §5. Nothing in this package supports Option A (full closure) without explicitly carve-outs matching Option B's list, and nothing in this package supports treating the finding as a hard block (Option C) given how much of the purchase-side and PND-structure mechanics were positively, directly confirmed. Boss remains the sole Final Approver.

---

## 9. Final Status

**ACCOUNT WHT GRPA-M18 PARTIAL — CONTROLLED ACCOUNTING/TAX CARRY-FORWARD REQUIRED**

Per Boss's own recorded decision (top of this document): the Inventory-to-Accounting/Tax domain transfer is **ACCEPTED**; full WHT closure is **explicitly NOT accepted**; `ACC-WHT-06` stands at **HIGH** pending Boss's own review of the targeted module proof now supplied in `09_ACC_WHT_MULTI_MODULE_TARGETED_PROOF.md`. `08` answered whether multi-rate documents are possible at all (yes, with a base-module HIGH GAP); `09` answers, specifically for `l10n_th_withholding_tax_multi`, the six proof items Boss required — two (purchase-side payment posting, line-level tagging) now have direct test-level evidence; two (certificate and PND output with multiple rates) remain chained-evidence-only, not directly tested; sales-side is confirmed untested by this module. None of this constitutes this audit deciding the module-baseline question — that decision, and whether it moves `ACC-WHT-06` off HIGH, remains Boss's alone.

This is not a Gate PASS. This is not Team B or Team C authorization. This is not a statutory legal sign-off. Boss remains the sole Final Approver of the disposition and decision options presented above.
