# CORR-007A — Team 3: Render / Print Proof

## 1. Render chain (static trace, file-by-file)

```
User action: "Print" on a withholding.tax.cert record
        |
        v
ir.actions.report  "withholding_tax_pdf_report"          data/report_data.xml:13-23  (SHA-256 51b604e0…caeda1)
  model = withholding.tax.cert
  report_type = qweb-pdf
  report_name = "l10n_th_withholding_tax_cert_form.withholding_tax_pdf"
  binding_model_id = model_withholding_tax_cert   (auto-adds a Print menu entry on the record)
  paperformat_id = paperformat_withholding_tax     (data/paper_format.xml, A4, 0 margin, 90dpi)
        |
        v
QWeb template "withholding_tax_pdf"                        reports/layout.xml:440-448
  wraps web.html_container, iterates docs, calls ->
        |
        v
QWeb template "withholding_layout_report"                   reports/layout.xml:2-437
  root <div t-attf-style="background-image:url(
     '/l10n_th_withholding_tax_cert_form/static/src/img/WithholdingCert.jpg');
     background-size:300mm 424mm; width:300mm; height:424mm;">
  -> all field boxes below are absolutely positioned (CSS "position: fixed",
     static/scss/style_report.scss) on top of this exact background image.
        |
        v
AbstractModel "report.withholding_tax_pdf"                  reports/withholding_report_pdf.py:7-21
  _get_report_values(docids, data) supplies {doc_ids, doc_model, docs, report_type}
  to the QWeb rendering context ("docs" = withholding.tax.cert recordset).
```

## 2. Background-image identity proof

This is the strongest single piece of render-path evidence in this session: `reports/layout.xml:5` hard-codes the background-image URL to
`/l10n_th_withholding_tax_cert_form/static/src/img/WithholdingCert.jpg`, which — under Odoo's static-asset URL convention — resolves to exactly the file at `l10n_th_withholding_tax_cert_form/static/src/img/WithholdingCert.jpg` inside this module. That file's SHA-256 (`8e0969a3229a36b28f7fd4bf1107387de808a71f8345f1473267c90ee161c94b`) is the same file inspected visually by Team 2 as the Boss-supplied form baseline (both came from the same zip; the module ships its own copy of the identical evidence file Boss uploaded separately as `WithholdingCert.jpg`).

In other words: **the printed PDF's background is not an approximation or a redraw of the official 50-twi form — it is a direct raster embed of the same image file supplied as evidence**, with computed field values overlaid on top via pixel-offset CSS (`style_report.scss`, e.g. `.number_payment { position: fixed; top: 100px; }`, `.company_vat { margin-left: 730px; position: fixed; top: 156px; }`, confirmed by direct inspection, lines 14-65).

The second copy at `static/src/img/fix/WithholdingCert.jpg` (SHA-256 `c77939e4fe85828d3e434f6792657b03353d2513b7184dc6f055181fee718f10`) is not referenced anywhere in the module's XML, Python, or SCSS (grep-verified) — it is dead/spare asset, not part of the active render path. Not a blocker; noted for completeness.

## 3. Source-level test evidence

`tests/test_wt_cert_form.py` (SHA-256 `5f6fc77382f13711c12b88279b7b66fd67f3c3a2ea2645940edf3e77139dad2b`), class `TestWTCertForm`, method `test_01_print_wt_cert_form`:

```python
def test_01_print_wt_cert_form(self):
    wt_cert = self._create_direct_wt_cert()
    self.withholdin_tax_cert_form.render_qweb_pdf(wt_cert.id)
```

This test constructs a real `withholding.tax.cert` record (partner, income tax form `pnd3`, one `wt_line`) and calls `render_qweb_pdf()` — the actual Odoo QWeb-to-PDF rendering entry point — on the exact report action wired in `data/report_data.xml`. This is source-level proof that the module's author(s) intended, and structured the code for, an end-to-end render to actually succeed (no mocking of the render call).

## 4. What was NOT executed in this session, and why

**No live Odoo instance was started, and no PDF was actually generated in this session.**

Blocker (by design, not by failure): the session's Strict Scope explicitly prohibits (a) installing the module unless separately authorized, and (b) connecting to production. Actually rendering `render_qweb_pdf()` requires a running Odoo server with this module and its full dependency chain (`l10n_th_withholding_tax_cert`, `l10n_th_withholding_tax`, `l10n_th_reports`, `l10n_th_amount_to_text`, `web`) installed against a live PostgreSQL database — none of which this audit session is authorized to stand up. This is a **controlled limitation**, not a missing-evidence gap: every file in the render chain was located, read in full, and cross-checked line-by-line (§1–§3 above); only the final "click render, inspect output pixels" step was not performed.

## 5. Disposition input for Team 5

Static render-chain proof is **complete**: action → Python context provider → wrapper template → layout template → background image → CSS-positioned field boxes, every link verified by direct file inspection with SHA-256 citation. A source-level automated test exercises the exact same call path. The only unproven step is live execution, which is out of this session's authorized scope by design (no install, no production connection) rather than because evidence is missing or contradictory.

This corresponds to the task's **Case C** disposition logic: the chain is proven but live render/print execution was not performed. Recommended language for Team 5: `GRPA-M18-C = RESOLVED AS STATIC CHAIN PROOF (COMPLETE) — LIVE RENDER NOT EXECUTED (session-scope controlled limitation: no Odoo runtime authorized); subject to Boss acceptance of this limitation.` Team 5 must independently confirm this is not a self-declared Gate PASS.
