# CORR-007A — Team 4: PND3/PND53 Filing Boundary Statement

## 1. Purpose

Separate what this session proves (the 50-twi **certificate**, given to the payee as proof of withholding) from what CORR-006 already assessed and left `HIGH REMAINS` (the **PND3/PND53 statutory filing/export** to the Thai Revenue Department). These are two different legal instruments produced by two different, non-overlapping source modules.

## 2. Module-boundary evidence

| Concern | Module | Path | Status |
|---|---|---|---|
| 50-twi certificate print (this session) | `l10n_th_withholding_tax_cert_form` | `ACCOUNT/01 ACCOUNT/SOURCE CODE/addons_extra/l10n_th_withholding_tax_cert_form/` | Examined in full — Teams 1–3 |
| `withholding.tax.cert` base model | `l10n_th_withholding_tax_cert` | `ACCOUNT/01 ACCOUNT/SOURCE CODE/addons_extra/l10n_th_withholding_tax_cert/` | Examined (dependency context) |
| PND3/PND53 CSV filing/export | `l10n_th_reports` | `ACCOUNT/01 ACCOUNT/SOURCE CODE/02 OTHER/l10n_th_reports/models/tax_report_pnd.py` | Examined in CORR-006 §5.5 (base commit `46a848375b4878f6d4b3e82cfeab4e2e6d6cb552`), **not re-examined in this session** — cited by reference only |
| WHT summary/audit xlsx report (internal review tool, not statutory e-filing) | `l10n_th_withholding_tax_report` | `ACCOUNT/01 ACCOUNT/SOURCE CODE/addons_extra/l10n_th_withholding_tax_report/` | Manifest read only, not deep-inspected — see §4 |

grep-verified (Team 1 §4): no file inside `l10n_th_withholding_tax_cert_form` or `l10n_th_withholding_tax_cert` imports, calls, or references `tax_report_pnd` or any CSV/e-filing export routine. The only overlap is that both the certificate module and the PND3/PND53 filing module read from the *same underlying data* (`withholding.tax.cert` and the WHT amounts on `account.move`/`account.payment`) — but they are separate code paths producing separate output artifacts (a printed PDF certificate vs. a CSV filing export).

## 3. Confirmed separation

**Certificate only, not filing.** `l10n_th_withholding_tax_cert_form` produces a `qweb-pdf` report (`data/report_data.xml:16`, `report_type = qweb-pdf`) addressed to the payee. It contains no CSV writer, no e-filing schema, and no reference to Revenue Department upload formats. CORR-006 already independently confirmed the PND3/PND53 CSV export lives entirely in `l10n_th_reports/models/tax_report_pnd.py:74-145` (PND53 handler lines 74-108, PND3 handler lines 111-145), a file this session did not need to touch because it is out of this session's scope (certificate proof only).

## 4. `l10n_th_withholding_tax_report` — noted but not conflated

This module's manifest (`ACCOUNT/01 ACCOUNT/SOURCE CODE/addons_extra/l10n_th_withholding_tax_report/__manifest__.py`) declares an xlsx-based "Withholding Tax Report" with its own wizard, template, and menu, depending on `report_xlsx_helper`, `date_range`, `l10n_th_partner`, and `l10n_th_withholding_tax_cert`. By name and dependency shape this appears to be an **internal review/summary report** (a "withholding tax book" listing), not the statutory PND3/PND53 e-filing artifact itself. This session did not deep-inspect its internals (out of the GRPA-M18-A/B/C/D/E scope defined for CORR-007A) and makes **no disposition claim** about it. If Accounting/Tax later needs to know whether this module could serve as a filing aid, that requires a separate targeted review — flagged here only so it is not silently missed.

## 5. Recommendation

- `GRPA-M18-D` (PND3/PND53 monthly filing/export correctness) is **unaffected by this session's findings**. CORR-006's `HIGH REMAINS — Accounting/Tax statutory validation required` disposition on the PND3/PND53 side stands untouched.
- Per task decision logic Case D: classify `GRPA-M18-D` as `CONTROLLED CARRY-FORWARD TO ACCOUNTING/TAX`. Do not close it using 50-twi certificate evidence — the certificate module contains no filing/export logic to close it with.
- Do not let `GRPA-M18-D`'s unresolved status keep the Inventory Evidence Gate blocked. PND3/PND53 statutory filing correctness is an Accounting/Tax-domain concern; it has no code-level touchpoint with the Inventory Core Backbone review this GRPA-M18 finding originated under, once separated from the certificate proof completed in this session.

## 6. What this proves / does not prove

Proves: the certificate module examined by Teams 1-3 is structurally and functionally separate from the PND3/PND53 filing module CORR-006 flagged. Closing the certificate does not, and must not, imply closing the filing item.

Does not prove: PND3/PND53 statutory correctness one way or the other — that determination was made in CORR-006 and is not revisited here. Does not prove or disprove whether `l10n_th_withholding_tax_report` has any bearing on filing — explicitly out of scope, explicitly not claimed either way.
