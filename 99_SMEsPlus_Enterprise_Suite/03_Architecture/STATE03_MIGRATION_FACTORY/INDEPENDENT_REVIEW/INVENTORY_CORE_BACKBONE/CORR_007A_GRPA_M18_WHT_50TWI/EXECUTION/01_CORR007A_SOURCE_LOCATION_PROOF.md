# CORR-007A — Team 1: Source Location Proof

Session: `SMEPLUS-26-09-01-CORR007A-GRPA-M18-WHT-50TWI-001`
Project: SMEsPlus ENTERPRISE SUITE
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `audit/inventory-core-corr007a-grpa-m18-wht-50twi-009`
Base audit branch: `audit/inventory-core-corr006-boss-high-reproof-008`
Base CORR-006 commit: `46a848375b4878f6d4b3e82cfeab4e2e6d6cb552`
Timestamp: 2026-09-01
Mode: Evidence-first / clean-room / no development authorization

## 1. Evidence Intake

Boss-supplied evidence, located on the local controlled machine (not embedded in the git repository):

| Item | Path | SHA-256 |
|---|---|---|
| `l10n_th_withholding_tax_cert_form.zip` | `ACCOUNT/01 ACCOUNT/SOURCE CODE/addons_extra/l10n_th_withholding_tax_cert_form.zip` | `5988085deba46ff9796ef43c51d4d83209011d2e1c935e495a3d7949542b2c0a` |
| `WithholdingCert.jpg` (form baseline image, inside the zip) | `.../l10n_th_withholding_tax_cert_form/static/src/img/WithholdingCert.jpg` | `8e0969a3229a36b28f7fd4bf1107387de808a71f8345f1473267c90ee161c94b` |

Both required evidence items were confirmed present on disk before this session proceeded. The zip contains 78 entries (39 real files + 39 macOS `__MACOSX` resource-fork siblings, 0 discarded). The extracted-on-disk copy at `ACCOUNT/01 ACCOUNT/SOURCE CODE/addons_extra/l10n_th_withholding_tax_cert_form/` matches the zip's file listing 1:1 (verified via `unzip -l`).

Note: `WithholdingCert.jpg` exists in two locations inside the module: `static/src/img/WithholdingCert.jpg` (SHA-256 above; **this is the file actually referenced by the report template**, see Team 3) and `static/src/img/fix/WithholdingCert.jpg` (SHA-256 `c77939e4fe85828d3e434f6792657b03353d2513b7184dc6f055181fee718f10`, unreferenced by any XML/Python/SCSS in the module — a spare/backup copy, same pixel dimensions 1076×1523, different byte content). This distinction matters for Team 3's render-path proof.

## 2. Module Identity — `l10n_th_withholding_tax_cert_form`

Source: `ACCOUNT/01 ACCOUNT/SOURCE CODE/addons_extra/l10n_th_withholding_tax_cert_form/__manifest__.py`
SHA-256: `dfc9a1978d6072fe5c8310e798f4a4c81527140fe3d45b22b51861255d5c8bd9`

```
name: "Thai Localization - Withholding Tax Certificate Form"
version: 19.0.1.0.2
author: Ecosoft, Odoo Community Association (OCA), SMEsPlus
license: AGPL-3
depends: ["web", "l10n_th_withholding_tax_cert", "l10n_th_amount_to_text"]
data: ["data/paper_format.xml", "data/report_data.xml", "reports/layout.xml", "views/withholding_tax_cert.xml"]
assets: web.report_assets_common -> static/scss/style_report.scss
```

What this proves: this module is the **print/report layer only**. It does not define the `withholding.tax.cert` model — it inherits it (`_inherit = "withholding.tax.cert"`) from its dependency `l10n_th_withholding_tax_cert`.
What it does NOT prove: it does not by itself prove field-level statutory correctness — see Team 2.

## 3. Full File Inventory — `l10n_th_withholding_tax_cert_form`

| Path (relative to module root) | Role | SHA-256 |
|---|---|---|
| `__manifest__.py` | Module manifest / dependency declaration | `dfc9a1978d6072fe5c8310e798f4a4c81527140fe3d45b22b51861255d5c8bd9` |
| `__init__.py` | Package init | (not cited as evidence — trivial import stub) |
| `models/withholding_tax_cert.py` | Model extension: adds `amount_pension_fund`, `amount_socialsecurity_fund`, `amount_provident_fund`; adds `_compute_desc_type_other`, `_group_wt_line` helpers | `0cb35b49b926d48a5b2bf60025eec2fbb62c9abb302ee9db78f0d26f9e6255b2` |
| `views/withholding_tax_cert.xml` | Backend form-view extension exposing the 3 fund fields | `9eda88a7c6c2e3553bb4502958639bc48d65d01d2e123c6843d37d99331d7a59` |
| `reports/withholding_report_pdf.py` | `AbstractModel` `report.withholding_tax_pdf` — supplies `_get_report_values()` for the QWeb rendering context | `4b565bfb52319c0d3b5baed7e6bd231a06cd69daaf7fcc4b057fd55aa4f40f9c` |
| `reports/layout.xml` | QWeb templates `withholding_layout_report` + `withholding_tax_pdf` — the actual certificate layout, background image, and field placement | `c6d08973a58ada4d63f8c02462de80fe2a16571e4f5f8fa81f51e18394245aff` |
| `data/report_data.xml` | `ir.actions.report` record `withholding_tax_pdf_report` — wires the report action to the model, template, and paper format | `51b604e00db7f9f0079316cd260a4ccd8979f478d23a4cd232732b7972caeda1` |
| `data/paper_format.xml` | `report.paperformat` record `paperformat_withholding_tax` (A4, zero margins, 90dpi) | `7e4e9830e880c7700eae2c7ea77779cfb05e13c73a7837dceeb72d05d5ba40e2` |
| `static/scss/style_report.scss` | CSS: `position: fixed` pixel-offset placement of every field box over the background image (446 lines) | `cd82528354ec39f84e889608967bf3659f4865f6a084bc6e49a96bb363eda60c` |
| `static/src/img/WithholdingCert.jpg` | Certificate background image — **the official 50-twi form scan**, referenced by `reports/layout.xml` | `8e0969a3229a36b28f7fd4bf1107387de808a71f8345f1473267c90ee161c94b` |
| `static/src/img/fix/WithholdingCert.jpg` | Unreferenced spare copy of the same image | `c77939e4fe85828d3e434f6792657b03353d2513b7184dc6f055181fee718f10` |
| `static/fonts/THSarabunNew Bold.ttf` | Thai government-standard font used for print rendering | (binary, not content-cited) |
| `tests/test_wt_cert_form.py` | Odoo unit test `test_01_print_wt_cert_form` — calls `render_qweb_pdf()` on a constructed certificate | `5f6fc77382f13711c12b88279b7b66fd67f3c3a2ea2645940edf3e77139dad2b` |
| `readme/DESCRIPTION.rst` | Module description | `85d8a872026b351ec24408c439ce58353ebc0244911db9a7222f2385518f3de2` |

No sequence (`ir.sequence`) record exists in this module — the certificate `name` field is computed, not sequence-generated (see Team 2, `GRPA-M18-B`, certificate number).
Security: no `ir.model.access.csv` or security XML in this module — access control for `withholding.tax.cert` is owned entirely by the base module (`l10n_th_withholding_tax_cert/security/`), not duplicated here.

## 4. Dependency Chain (as manifest-declared, traced upward)

```
l10n_th_withholding_tax_cert_form  (this zip — print layer)
  depends on -> l10n_th_withholding_tax_cert     (base model: withholding.tax.cert, wizard, security)
                  depends on -> l10n_th_withholding_tax   (WHT tax computation on account.move / account.payment)
                                  depends on -> l10n_th_reports   (PND3/PND53 filing export — see Team 4)
  depends on -> l10n_th_amount_to_text           (Thai amount-in-words conversion, res.currency.amount_to_text)
```

Evidence:
- `l10n_th_withholding_tax_cert/__manifest__.py` (SHA-256 `c935212ebf19f4bc224f5104a1ded92fe0a17f4fc5f9c75104ec61b164a90a95`): `depends: ["l10n_th_withholding_tax"]`
- `l10n_th_withholding_tax/__manifest__.py`: `depends: ["account", "l10n_th_reports"]`
- `l10n_th_amount_to_text/models/res_currency.py:19` defines `amount_to_text(self, amount)`, called by `reports/layout.xml:384`.

**Material finding:** `l10n_th_partner` (the module that defines `res.partner.branch`, see Team 2 field mapping) is **not** in this dependency chain at any level. It is a separate, optional module present elsewhere in the same local source tree, architecturally disconnected from the WHT certificate stack.

## 5. Base Model Module — `l10n_th_withholding_tax_cert` (dependency, already present in the controlled local source tree, not part of the Boss-uploaded zip)

Location: `ACCOUNT/01 ACCOUNT/SOURCE CODE/addons_extra/l10n_th_withholding_tax_cert/`
This module defines the `withholding.tax.cert` model that the uploaded zip's report prints. It was already present in the project's controlled source tree prior to this session (same tree used for CORR-006), consistent with CORR-006's evidence-sourcing convention.

Key file cited: `models/withholding_tax_cert.py` (SHA-256 `7df08a7d94b1473b06e4c74df45e25594f2fc139af45778a9ce14c9810a79088`), 427 lines — defines `withholding.tax.cert` and `withholding.tax.cert.line`, all fields used by the print layout (see Team 2).

What this proves: the model that the Boss-uploaded print module targets is real, present in the same controlled tree, and its field set is fully readable.
What it does NOT prove: that this base module was itself part of the Boss-supplied evidence upload — it was not; it is cited as supporting context only, and is flagged as such throughout this package.

## 6. What This Team's Evidence Proves / Does Not Prove

Proves:
- The 50-twi withholding tax certificate print module exists in source, is a real, structurally complete Odoo 19 module (manifest, models, views, report action, QWeb template, paper format, test, i18n), and was supplied by Boss as a verifiable zip.
- The module's background image is present at the exact static path the report template references.

Does not prove:
- Statutory/legal correctness of the certificate content (Team 5 / Legal boundary).
- That the certificate has been rendered end-to-end inside a live Odoo runtime in this session (Team 3 — no Odoo runtime was provisioned; out of session scope).
- That PND3/PND53 filing/export is handled by this module (it is not — see Team 4).
