# 50-TWI Withholding Tax Certificate — Gap Closure Re-Verification

## Session Metadata

| Field | Value |
|---|---|
| Deliverable | `03_ACC_WHT_50TWI_GAP_CLOSURE.md` |
| Session role | Team A3 — 50-TWI Certificate Gap Closure Team |
| Repository (nominal) | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Branch (this session) | `audit/account-wht-grpa-m18-closure-010` |
| Evidence base (prior session) | CORR-007A, commit `deceb7339b39eba309236782f159f8393224f5fd`, branch `audit/inventory-core-corr007a-grpa-m18-wht-50twi-009` |
| Date | 2026-09-02 |
| Mode | Evidence-first, clean-room re-verification, read-only, **no development authorization** |
| Source tree examined (read-only, outside repo) | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE/addons_extra/` |
| Git verification of CORR-007A commit | **Not performed.** Task instructions explicitly prohibit running git commands in this session, and the working directory (`AI-Collaboration-Hub`) is reported by the environment as not a detected git repository. The commit hash above is recorded as the evidence-base citation only; it is not independently confirmed here. |
| Explicit non-actions | No Gate PASS declared. No Team B/C authorization. No source code written or modified. No checkboxes/fields added. |

---

## Re-Verification Methodology and Hash-Comparison Note

Each of the four files central to the three gaps was read in full and hashed independently with `shasum -a 256`. Dependency claims were re-derived from `__manifest__.py` files by walking the `depends` chain manually (same method attributed to CORR-007A Team 1), not assumed from the prior report's prose. The official form image (`WithholdingCert.jpg`) was opened directly with the Read tool (this agent has image-reading capability) and, where finer detail was needed, cropped and upscaled locally with Python/Pillow (`PIL` 12.3.0, available in this environment) for closer visual inspection — this is independent visual confirmation, not a re-statement of CORR-007A's description.

**Recomputed hashes, compared against the prior report's cited values:**

| # | File | Recomputed SHA-256 | Lines | Prior report hash (as given in task) | Match? |
|---|---|---|---|---|---|
| 1 | `l10n_th_withholding_tax_cert/models/withholding_tax_cert.py` | `7df08a7d94b1473b06e4c74df45e25594f2fc139af45778a9ce14c9810a79088` | 426 | `7df08a7d94b1473b06e4c74df45e25594f2fc139af45778a9ce14c9810a79088` | **YES — exact match** |
| 2 | `l10n_th_withholding_tax_cert_form/reports/layout.xml` | `c6d08973a58ada4d63f8c02462de80fe2a16571e4f5f8fa81f51e18394245aff` | 449 | `c6d08973a58ada4d63f8c02462de80fe2a16571e4f5f8fa81f51e18394245aff` | **YES — exact match** |
| 3 | `l10n_th_partner/models/res_partner.py` | `70c770de01f29c8cb4618a4db3dfafb105d0db4e9ec42a234d78dbb8b2433dd7` | 80 | not given (line-15 citation only) | line-15 claim independently confirmed (see Gap 1) |
| 4 | `l10n_th_withholding_tax_cert_form/static/scss/style_report.scss` | `cd82528354ec39f84e889608967bf3659f4865f6a084bc6e49a96bb363eda60c` | 446 | not previously cited | new citation, this audit |

**Finding on the "malformed hash" premise in the task instructions:** the task brief asserted that the prior report's hashes "look unusually short/malformed... a real SHA-256 is 64 hex chars" and asked this session to flag any discrepancy. Independent character-count verification (`printf '%s' "<hash>" | wc -c`, cross-checked with Python `len()`) shows **both prior-cited hash strings are exactly 64 hexadecimal characters** — standard, well-formed SHA-256 output — and both **match this session's independently recomputed hashes character-for-character**. There is no malformation and no mismatch. Per the "No invention" rule, this session does not adopt the task brief's framing without verification: the correct, verified conclusion is **the two files central to Gaps 2 and 3 are byte-for-byte unchanged since CORR-007A**, and the "malformed hash" premise supplied in the task instructions does not hold up under independent recount. This is reported as an explicit finding rather than silently ignored, per instruction.

No prior hash was supplied for `res_partner.py` (only a line-number citation) or for `style_report.scss` (not cited at all by CORR-007A); both are now hashed and on record above for any future re-audit.

---

## Gap 1 — Branch Number

**Claim under test:** `res.partner.branch` exists in `l10n_th_partner/models/res_partner.py`, but `l10n_th_partner` is not a manifest dependency of the WHT certificate stack, and the print template never references `.branch`; the official form also has no distinct "branch" box for this certificate type.

**Re-verification:**

1. **Field exists as claimed.** `l10n_th_partner/models/res_partner.py:15`:
   ```python
   branch = fields.Char(string="Tax Branch", help="Branch ID, e.g., 0000, 0001, ...")
   ```
   Confirmed by direct read. SHA-256 of this file: `70c770de01f29c8cb4618a4db3dfafb105d0db4e9ec42a234d78dbb8b2433dd7`.

2. **Dependency chain re-derived manually, not assumed.**
   - `l10n_th_withholding_tax_cert_form/__manifest__.py` → `"depends": ["web", "l10n_th_withholding_tax_cert", "l10n_th_amount_to_text"]`
   - `l10n_th_withholding_tax_cert/__manifest__.py` → `"depends": ["l10n_th_withholding_tax"]`
   - `l10n_th_withholding_tax/__manifest__.py` → `"depends": ["account", "l10n_th_reports"]`
   - `l10n_th_amount_to_text/__manifest__.py` → `"depends": ["base"]`
   - `l10n_th_partner/__manifest__.py` → `"depends": ["partner_company_type", "partner_firstname"]`

   `l10n_th_partner` does not appear anywhere in this chain (`web`, `l10n_th_withholding_tax_cert`, `l10n_th_amount_to_text`, `account`, `l10n_th_reports`, `base` — none of these is or (per available manifests) transitively pulls in `l10n_th_partner`). Separately confirmed: `l10n_th_partner` **is** a dependency of a different, sibling module — `l10n_th_withholding_tax_report` (the WHT *reporting/listing* module, not the certificate *print* module) — via `grep -rl "l10n_th_partner" */__manifest__.py`. This shows the `branch` field is reachable elsewhere in the Thai localization suite, just not in the print stack under audit. Claim confirmed independently.

3. **No template reference.** `grep -ni "branch"` against `l10n_th_withholding_tax_cert_form/reports/layout.xml` (449 lines, full file read) returns zero matches. The same search against `l10n_th_withholding_tax_cert_form/views/withholding_tax_cert.xml` and all of `l10n_th_withholding_tax_cert/` (models, views) also returns zero matches. `.branch` is not read, computed, or displayed anywhere in the certificate stack. Claim confirmed.

4. **Official form has no distinct branch box — independently confirmed visually.** `l10n_th_withholding_tax_cert_form/static/src/img/WithholdingCert.jpg` (1076×1523, grayscale JPEG) was opened directly and, for the payer/payee identification blocks, cropped and 2× upscaled for legibility. Both the "ผู้มีหน้าที่หักภาษี ณ ที่จ่าย" (payer) and "ผู้ถูกหักภาษี ณ ที่จ่าย" (payee) blocks show exactly two ID-number lines each:
   - `เลขประจำตัวผู้เสียภาษีอากร (13 หลัก)*` — a 13-digit taxpayer-ID box grid, and
   - a second, unlabeled-as-branch line reading only `เลขประจำตัวผู้เสียภาษีอากร` (taxpayer ID number, no "13 หลัก" qualifier) with its own box grid.

   No box on the form carries a "สาขา" (branch) label anywhere in the payer or payee section. This independently corroborates the CORR-007A description that the 50-ทวิ form has no distinct branch box for this certificate type. (Observation, not a legal conclusion: the second unlabeled ID line most plausibly represents a legacy/alternate taxpayer-ID format field rather than a branch code, but this cannot be asserted definitively from the image alone.)

5. **Side note (not part of Gap 1, recorded for completeness):** `l10n_th_withholding_tax_cert_form/static/src/img/fix/WithholdingCert.jpg` is a second, differently-hashed image (`c77939e4fe85828d3e434f6792657b03353d2513b7184dc6f055181fee718f10`, RGB JFIF vs. the active grayscale Exif JPEG) sitting in a `fix/` subfolder. `grep -rn "img/fix"` across the module returns no references — it is not wired into any template or asset bundle. It was not analyzed further; flagged only so a future team does not mistake it for the live form asset.

**Disposition: RESOLVED (as "not a gap").** The `branch` field's absence from the certificate print path is not a code defect: it reflects (a) a real manifest-dependency boundary that was not accidentally broken, and (b) an official form that itself has no branch box for this certificate. There is nothing to fix in the print template. No `LEGAL_TAX_REVIEW_REQUIRED` flag needed for this gap — the underlying question ("does the form need a branch box") is answered directly by the form image, not by a statutory interpretation question.

---

## Gap 2 — Tax-Form Checkboxes (ภ.ง.ด. selection)

**Claim under test:** the official form has 7 checkbox positions (ภ.ง.ด.1ก / ภ.ง.ด.1ก พิเศษ / ภ.ง.ด.2 / ภ.ง.ด.3 / ภ.ง.ด.2ก / ภ.ง.ด.3ก / ภ.ง.ด.53) but `INCOME_TAX_FORM` only supports 4 (pnd1, pnd3, pnd3a, pnd53).

**Re-verification:**

1. **Model selection field — confirmed exactly as claimed.** `l10n_th_withholding_tax_cert/models/withholding_tax_cert.py:9-14`:
   ```python
   INCOME_TAX_FORM = [
       ("pnd1", "PND1"),
       ("pnd3", "PND3"),
       ("pnd3a", "PND3a"),
       ("pnd53", "PND53"),
   ]
   ```
   Exactly 4 options. Used at line 173-180 (`income_tax_form` field on `withholding.tax.cert`), and re-imported (not redefined) in `wizard/create_withholding_tax_cert.py:7,29` — so the constraint is single-sourced in one place, not duplicated, but is nonetheless enforced in two UI surfaces (the record form and the creation wizard) plus the i18n `.po` file (`l10n_th_withholding_tax_cert/i18n/th.po` has selection-label entries only for pnd1/pnd3/pnd3a/pnd53).

2. **Template renders exactly 4 checkbox blocks, one per selection value.** `l10n_th_withholding_tax_cert_form/reports/layout.xml:169-180`:
   ```xml
   <t t-if="o.income_tax_form == 'pnd1'"><p class="choice_pnd1a">X</p></t>
   <t t-if="o.income_tax_form == 'pnd3'"><p class="choice_pnd3">X</p></t>
   <t t-if="o.income_tax_form == 'pnd3a'"><p class="choice_pnd3a">X</p></t>
   <t t-if="o.income_tax_form == 'pnd53'"><p class="choice_pnd53">X</p></t>
   ```
   No `t-if` blocks exist for a pnd1-special, pnd2, or pnd2a value — because those values cannot exist on the model in the first place (the Selection field would reject them).

3. **CSS layer — no dead/unused positioning classes for the missing 3 checkboxes.** Full read of `l10n_th_withholding_tax_cert_form/static/scss/style_report.scss` (446 lines) shows exactly 4 checkbox-position classes: `.choice_pnd1a` (line 101-106), `.choice_pnd3` (107-112), `.choice_pnd3a` (113-118), `.choice_pnd53` (119-124). There is **no** `.choice_pnd1a_special`, `.choice_pnd2`, or `.choice_pnd2a` class anywhere in the file, not even commented out or unused. This distinguishes the situation from a "flip a flag" fix: the print layout has zero pre-existing pixel coordinates for the 3 missing checkbox positions — they are **entirely absent**, not "present but dead."

4. **Official form — independently confirmed to show 7 checkbox positions.** Direct visual inspection of `WithholdingCert.jpg` (cropped/upscaled region around the "ลำดับที่ ... ในแบบ" row) shows, verbatim and in this exact layout:
   ```
   (1) ภ.ง.ด.1ก      (2) ภ.ง.ด.1ก พิเศษ    (3) ภ.ง.ด.2     (4) ภ.ง.ด.3
   (5) ภ.ง.ด.2ก      (6) ภ.ง.ด.3ก          (7) ภ.ง.ด.53
   ```
   Exactly 7 checkboxes, exactly the labels claimed by CORR-007A. Confirmed independently, not copied from the prior report.

**Is this a config-only fix or does it require new template/layout work?** New template/layout work. Adding the 3 missing options is not just a Selection-list edit: each new option needs (a) a new `t-if` block in `layout.xml` following the established pattern (trivial, same pattern as the existing 4), but also (b) a **new** CSS rule in `style_report.scss` with a correct `position: fixed; top: …px; …px;` pixel coordinate measured against the 1076×1523 background image — coordinates that do not exist yet anywhere in the codebase and would need to be derived from the form image itself (a measurement/layout task, not a data-entry task), plus (c) i18n label additions. The *pattern* to follow is well-established and low-risk (13 income-type rows and 4 form checkboxes already use identical `position: fixed` CSS + `t-if` conventions), but "requires new template work" is the accurate characterization, not "quick config fix."

**Materiality reasoning (non-binding, not a legal conclusion):** ภ.ง.ด.1ก and ภ.ง.ด.1ก พิเศษ are used for annualized/summary withholding on employee salary income under Section 40(1) — filed by employers once a year, not per-transaction. ภ.ง.ด.2 and ภ.ง.ด.2ก relate to withholding on categories not obviously central to a services SaaS ERP's typical AP-vendor-payment WHT certificate flow (the module's own onchange logic at `withholding_tax_cert.py:202-209` only ever auto-selects between `pnd3` and `pnd53` based on whether the supplier is a company). Whether SMEsPlus's customer base will ever realistically need to issue a ภ.ง.ด.2, ภ.ง.ด.2ก, or ภ.ง.ด.1ก พิเศษ certificate — or whether Thai Revenue Department rules require the *capability* to exist regardless of actual usage frequency — is a statutory determination this audit is not authorized to make.

**Disposition: `ACCOUNTING/TAX CONFIGURATION` pending `LEGAL_TAX_REVIEW_REQUIRED` sign-off on materiality**, with the fix-complexity finding that closing it is **REQUIRES FORM UPDATE** work (new template + new measured CSS positions), not a same-day config change. Gap is confirmed **still present**.

---

## Gap 3 — WHT-Condition Checkboxes (ผู้จ่ายเงิน selection)

**Claim under test:** the official form has 4 condition checkboxes (หัก ณ ที่จ่าย / ออกให้ตลอดไป / ออกให้ครั้งเดียว / อื่นๆ) but `TAX_PAYER` only supports 2 (withholding, paid_one_time).

**Re-verification:**

1. **Model selection field — confirmed exactly as claimed.** `l10n_th_withholding_tax_cert/models/withholding_tax_cert.py:66`:
   ```python
   TAX_PAYER = [("withholding", "Withholding"), ("paid_one_time", "Paid One Time")]
   ```
   Used at line 188-195 (`tax_payer` field, `required=True`, default `"withholding"`). Confirmed used consistently (not duplicated) in `views/withholding_tax_cert.xml:59,108,137,139` and `i18n/th.po:479,585,685` — no hidden third/fourth option anywhere else in the module.

2. **Template renders exactly 2 checkbox blocks.** `l10n_th_withholding_tax_cert_form/reports/layout.xml:412-417`:
   ```xml
   <t t-if="o.tax_payer == 'withholding'"><p class="choich_withholding_tax">X</p></t>
   <t t-if="o.tax_payer == 'paid_one_time'"><p class="choich_paid_one_time">X</p></t>
   ```

3. **CSS layer — no dead classes for the missing 2 conditions.** `style_report.scss:408-421` defines exactly `.choich_withholding_tax` and `.choich_paid_one_time` (both `position: fixed; top: 1350px;` with different `left`/`right` offsets). No class exists (dead or otherwise) for "ออกให้ตลอดไป" (issued permanently) or "อื่นๆ" (other). Same finding as Gap 2: entirely absent, not dead-but-present.

4. **Official form — independently confirmed to show 4 condition checkboxes.** Direct visual inspection of the "ผู้จ่ายเงิน" row on `WithholdingCert.jpg` shows, verbatim:
   ```
   ผู้จ่ายเงิน  ☐ (1) หัก ณ ที่จ่าย   ☐ (2) ออกให้ตลอดไป   ☐ (3) ออกให้ครั้งเดียว   ☐ (4) อื่นๆ (ระบุ)
   ```
   Exactly 4 checkboxes. `withholding` maps to option (1); `paid_one_time` maps to option (3). Options (2) "ออกให้ตลอดไป" and (4) "อื่นๆ (ระบุ)" have no corresponding model value. Confirmed independently.

**Is this a config-only fix or does it require new template/layout work?** Same finding as Gap 2: new template/layout work, not config-only. Two new `t-if` blocks (trivial, same pattern) plus two new measured CSS position rules near the existing `top: 1350px` row (not yet present anywhere in the file) plus i18n additions. Note also that option (4) "อื่นๆ (ระบุ)" is a free-text "specify" checkbox on the official form — supporting it fully would also imply a supporting text field on the model (there is no equivalent of the `wt_cert_income_desc` free-text pattern used elsewhere in this file for `tax_payer`), which is a materially larger change than options (1)-(3) alone.

**Materiality reasoning (non-binding, not a legal conclusion):** "ออกให้ตลอดไป" (issued to cover all future payments/permanently) is typically used for certain categories of recurring withholding (e.g., interest, dividends) where the payer commits the certificate's validity forward rather than issuing per-payment; "อื่นๆ" is a residual/catch-all. For a services SaaS ERP whose WHT certificate flow is triggered per AP payment/journal entry (see `_compute_wt_cert_data` in `withholding_tax_cert.py:237-285`, which computes one certificate per `payment_id`/`move_id`), the "ออกให้ครั้งเดียว" (issued once) and "หัก ณ ที่จ่าย" pattern already covered by the 2 existing options may represent the dominant realistic usage pattern — but whether Thai tax law requires the form to expose all 4 conditions regardless of a given business's actual usage pattern is again a statutory question this audit is not authorized to answer.

**Disposition: `ACCOUNTING/TAX CONFIGURATION` pending `LEGAL_TAX_REVIEW_REQUIRED` sign-off on materiality**, with the fix-complexity finding that closing it is **REQUIRES FORM UPDATE** work (new template + new measured CSS positions, and possibly a new free-text field for the "อื่นๆ" case). Gap is confirmed **still present**.

---

## Summary Disposition Table

| Gap | Still present? | Fix complexity | Disposition |
|---|---|---|---|
| 1. Branch number (`res.partner.branch` not surfaced on WHT cert) | **N — not a defect.** Field exists in `l10n_th_partner` but that module is genuinely outside the certificate stack's dependency chain, and the official 50-ทวิ form has no branch box to render it into. | N/A | **RESOLVED** (confirmed non-issue by design + form layout) |
| 2. Tax-form checkboxes (7 on form vs. 4 in `INCOME_TAX_FORM`) | **Y — confirmed still present.** 3 of 7 official checkbox positions (ภ.ง.ด.1ก พิเศษ, ภ.ง.ด.2, ภ.ง.ด.2ก) have no selection value, no template block, and no CSS position anywhere in the codebase. | Requires new template work (new `t-if` blocks + newly-measured CSS `position: fixed` coordinates + i18n), following an existing low-risk pattern but not a same-day config toggle. | **ACCOUNTING/TAX CONFIGURATION pending LEGAL_TAX_REVIEW_REQUIRED** (materiality of ภ.ง.ด.1ก พิเศษ / 2 / 2ก for SMEsPlus's realistic use cases vs. statutory requirement to support them regardless) |
| 3. WHT-condition checkboxes (4 on form vs. 2 in `TAX_PAYER`) | **Y — confirmed still present.** "ออกให้ตลอดไป" and "อื่นๆ" have no selection value, no template block, no CSS position; "อื่นๆ" also implies a missing free-text field. | Requires new template work (new `t-if` blocks + newly-measured CSS coordinates + i18n); "อื่นๆ" option additionally implies new free-text field, larger than options (1)-(3) alone. | **ACCOUNTING/TAX CONFIGURATION pending LEGAL_TAX_REVIEW_REQUIRED** (materiality of "issued permanently" / "other" conditions for SMEsPlus's realistic use cases vs. statutory requirement) |

---

## What This Proves / Does Not Prove

**This audit proves:**
- All three gaps were independently re-derived from current source, not copied from CORR-007A's citations. Every file/line claim above was confirmed by this session's own `Read`, `grep`, and `shasum` calls.
- `l10n_th_withholding_tax_cert/models/withholding_tax_cert.py` and `l10n_th_withholding_tax_cert_form/reports/layout.xml` are byte-for-byte unchanged since CORR-007A (hash match, both 64-char well-formed SHA-256).
- The task brief's claim that the prior report's hashes were malformed does not hold up under direct verification — both cited hashes are correctly formatted and correctly matching; this is reported as a finding rather than silently accepted.
- The official form image was independently opened and visually inspected (not merely taken on the prior report's word) and corroborates the prior report's box-count claims for all three gaps: no branch box, 7 tax-form checkboxes, 4 condition checkboxes.
- For Gaps 2 and 3, the CSS layer was checked specifically for "dead" (present-but-unused) positioning classes to distinguish a quick-config fix from real template work — none were found; the missing boxes are entirely absent from the layout, which is why both gaps are classified as requiring form/template updates rather than simple selection-list edits.

**This audit does not prove / explicitly does not attempt:**
- Whether SMEsPlus is legally required to support ภ.ง.ด.1ก พิเศษ, ภ.ง.ด.2, ภ.ง.ด.2ก, "ออกให้ตลอดไป," or "อื่นๆ" under Thai Revenue Department rules, irrespective of actual usage frequency. That determination is explicitly out of scope and flagged `LEGAL_TAX_REVIEW_REQUIRED` for both Gap 2 and Gap 3.
- Verification of the CORR-007A commit hash (`deceb7339b39eba309236782f159f8393224f5fd`) against actual git history — no git commands were run in this session per task instructions, and the working directory is reported as not a detected git repository by this environment.
- Any statement of Gate PASS status. This session does not authorize Team B or Team C to proceed, and does not certify compliance readiness — it only reclassifies the three named gaps with independently-gathered evidence.
- Correctness or fitness of the unreferenced `static/src/img/fix/WithholdingCert.jpg` asset — noted as an orphaned file for a future team's awareness, not analyzed further, and irrelevant to the three gaps in scope.
- Any source-code change. No selection options, checkboxes, CSS rules, or fields were added, edited, or removed. This is a read-only audit deliverable only.
