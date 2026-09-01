# CORR-007B — Boss Addendum 4: Multi-Lens Functional Challenge of `N-A12-01`

Session: `SMEPLUS-26-09-02-CORR007B-3HIGH-CLOSURE-001` (Boss Addendum 4, `N-A12-01`)
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `audit/inventory-core-corr007b-3high-closure-010`
Base commit: `deceb7339b39eba309236782f159f8393224f5fd`
Timestamp: 2026-09-02
Mode: Evidence-first / clean-room / no development authorization / read-only

## 0. Provenance statement — read before the rest of this file

Boss's fourth addendum asked to reopen `N-A12-01` through a "4-role AI Expert Panel" (Functional Design,
Database Design, Integration & Localization, Code & UI Architecture) with independent reporting
authority separate from Team A/B/C/PMO. This session raised a direct concern with Boss before writing
this file: there are not four independent parties available here — there is one model (this session)
responding to a sequence of prompts. Boss selected the option to proceed with **four analytical lenses,
honestly labeled** rather than a literal independent-panel framing.

Accordingly: **every section below was produced by this single session**, applying four different
professional viewpoints to the same evidence base (this file, `08`, and `09`), not by four separate
reviewers with separate authority. No section in this file should be cited elsewhere as an independent
confirmation from a distinct party. Where a lens finds nothing new beyond files 08/09, that is stated
plainly rather than padded to look like an independent discovery.

## 1. Functional Design lens

**Question**: does the proven mechanism (files 08–09) actually describe a coherent, testable business
workflow, or only a pile of correct-but-disconnected method citations?

- The workflow is coherent and was already diagrammed in file 08 §2 (Mermaid flowchart). Re-checked here
  for completeness against Boss's 10-point list in this addendum: all 10 points (Product Category
  valuation policy, Manual/Automated, Periodic/Perpetual, monthly close, month 12, GL reconciliation,
  retained earnings, cut-off/backdate, opening balance carry-forward, source+dump evidence) trace to a
  specific section in file 08 or 09 — no point is unaddressed. Cross-reference table:

| Boss's challenge point | Addressed in |
|---|---|
| 1. Product Category-level valuation policy | File 09 §1 |
| 2. Manual vs Automated inventory valuation | File 09 §3 |
| 3. Periodic vs Perpetual accounting behavior | File 08 §17, File 09 §4 |
| 4. Monthly close workflow | File 08 §7, §17–18; File 09 §8 |
| 5. Month 12 year-end close | File 08 §22 |
| 6. Inventory valuation to GL reconciliation | File 08 §7 (`stock_valuation_report.py`) |
| 7. Retained earnings under Equity | File 08 §22 (`equity_unaffected`, G-6) |
| 8. Stock move cut-off / backdate control | File 08 §4, §21 |
| 9. Opening balance carry-forward | File 08 §8, §19 |
| 10. Source + dumpfile business semantics | Files 01–09 throughout, `06_SHA256_MANIFEST.txt` |

- **New from this lens**: a minimal UAT scenario set that Team B would need to actually test the
  mechanism (not run this session — no environment was installed or executed; this is a test-plan
  artifact, not a test result):
  1. Set a category to Perpetual/standard cost; validate a receipt; confirm an `account.move` is created
     and posted immediately, debiting Stock Valuation, crediting the source location's
     `valuation_account_id` (`stock_move.py:215-224`).
  2. Set a category to Periodic; validate the same receipt; confirm **no** `account.move` is created
     (`_should_create_account_move()` returns `False`).
  3. Run `action_close_stock_valuation` for that Periodic category's company; confirm one "Stock
     Closing" entry now covers the accumulated value gap.
  4. Attempt to validate a picking backdated into a locked fiscal period; confirm `ValidationError`
     (`stock_picking.py:13-19`); set `stock_account.skip_lock_date_check`; confirm the same picking now
     validates with no audit trail of who enabled the bypass (this is G-2, reproduced as a test case).
  5. Run a second closing after the first; confirm its computation only considers moves dated after the
     first closing's date (`_get_last_closing_date`, proving §19's carry-forward claim empirically, not
     just by reading the code).
- **Functional Design lens verdict**: mechanism is coherent and testable. It does not resolve G-5
  (migration cutover cross-proof) or G-6 (no year-end retained-earnings entry) — those remain Team B /
  Accounting decisions, not functional-design ambiguities.

## 2. Database Design lens

**Question**: does the actual customer dump schema support the mechanism proven from source, and are
there structural DB findings (tables, indexes, migration semantics) not visible from source alone?

- `Evidence_CSV/Dump_Index_Inventory.csv`: `account_move_line_account_id_date_idx` (btree,
  `account_id, date`) exists on `account_move_line` in the real dump. This is precisely the access
  pattern `stock_accounting_value(at_date)` needs (`account_id IN (...) AND date <= at_date`,
  `res_company.py:96-114`) — the schema is indexed to support the as-of-date reconciliation query
  efficiently, not just correctly. This is new evidence beyond source-code reading: the *dump* schema
  independently corroborates the *source* design's query pattern.
- `Evidence_CSV/Dump_Table_Inventory.csv`: `stock_valuation_adjustment_lines` (16 columns) exists in the
  real dump. Initially flagged as a possible legacy-orphan candidate (same pattern as `GRPA-M15`'s
  `purchase_request_id`); checked directly — its columns (`cost_id`, `cost_line_id`, `former_cost`,
  `additional_landed_cost`, `final_cost`) match the **Landed Costs** feature, and the table is real and
  current: `stock_landed_costs/models/stock_landed_cost.py` (module present in source, hashed in the
  manifest). **Not a gap** — reported as a checked-and-cleared item rather than omitted, so it is visible
  that this table was investigated, not skipped.
- **Database Design lens verdict**: no new schema-level gap found. The dump is consistent with, and in
  the index case actively supports, the mechanism proven from source. This lens does not change
  `N-A12-01`'s disposition; it corroborates files 08–09 from an independent data angle (the CSVs, not the
  `.py` source) rather than merely re-reading the same files.

## 3. Integration & Localization lens

**Question**: does Thai localization (WHT/VAT/PND) touch inventory period close in any way this package
has not yet examined? (`GRPA-M18`/WHT itself remains untouched and out of scope — this checks only
whether the *inventory closing mechanism* has a Thai-specific dependency, which would be new information
even though the WHT item itself is not being reopened.)

- Checked `__manifest__.py` `depends` for `l10n_th`, `l10n_th_reports`, and the `addons_extra/l10n_th_*`
  modules (withholding tax, WHT certs, base location, amount-to-text). `l10n_th/__manifest__.py`:
  `'depends': ['account_qr_code_emv', 'account']` — no `stock` or `stock_account` dependency. None of the
  other `l10n_th_*` manifests declare a `stock`/`stock_account` dependency either.
- **Finding**: Thai localization in this source baseline is entirely an Accounting/Tax-domain concern
  (invoices, WHT certificates, PND filing) and has **no code path into inventory valuation, closing, or
  lock-date behavior**. The period-close mechanism proven in files 08–09 is generic Odoo reference
  behavior with no Thai-specific variant or override.
- **Integration & Localization lens verdict**: no integration gap found between Thai localization and
  `N-A12-01`'s mechanism, because there is no integration between them at all in this source baseline.
  This is a negative-but-useful finding: SMEsPlus should not assume Thai statutory close-book behavior
  (e.g., a mandated year-end closing entry, relevant to G-6) is handled anywhere in the Inventory or
  generic Accounting layers — if required, it is new scope, not an existing-but-unexamined integration.

## 4. Code & UI Architecture lens

**Question**: beyond "does the mechanism work," is the reference implementation itself well-structured,
and does the UI genuinely expose the workflow the way files 08–09 describe?

- Module structure: `stock_account` separates concerns cleanly — `models/` (business logic),
  `wizard/` (transient UX for adjustment naming), `report/` (the reconciliation report model),
  `static/src/stock_valuation/` (a modern OWL/JS component tree: `controller.js`, `filters/`,
  `line/`, `buttons_bar/` — confirmed via full directory listing this session).
  `data/stock_account_data.xml` carries the cron and category defaults (file 08 §7). This is a
  reasonably well-factored module by ordinary Odoo standards.
- `static/src/stock_valuation/controller.js` (93 lines, read in full this session — **this resolves file
  08's gap G-4**, which had flagged the manual-trigger UI path as not fully source-verified):
  `actionGenerateEntry()` (lines 73-82) calls `orm.call("res.company", "action_close_stock_valuation",
  args)` with the report screen's currently-selected date, and does **not** pass `auto_post` — meaning
  the manual UI path uses the Python method's default (`auto_post=False`), so a manually-triggered
  closing is created as a draft `account.move` for review, while only the cron path
  (`_cron_post_stock_valuation`, file 08 §7) auto-posts. **G-4 is now resolved**, not merely narrowed:
  the manual trigger is confirmed to be date-selectable and review-before-post by design.
- **Code-quality finding, reported as found rather than smoothed over**: `stock_account/report/
  stock_valuation_report.py:140-144` —
  ```python
  def action_print_as_pdf(self):
      return

  def action_print_as_xlsx(self):
      return
  ```
  Both PDF and XLSX export methods are **empty stubs** in this source baseline, despite the JS
  controller's `actionPrintReport()` calling them from real "Print" buttons. This session did not
  determine whether this is (a) genuinely incomplete in this edition, (b) implemented via an
  Enterprise-only override module not present in this source tree, or (c) intentionally deferred — only
  that, as read, these two methods do nothing. This is a real, source-verified gap in the reference
  system's export feature, independent of the accounting mechanism itself, and should not be assumed
  functional by SMEsPlus without further check.
- **Code & UI Architecture lens verdict**: the accounting/workflow logic is well-factored and the UI
  genuinely exposes it as described. One concrete, previously-unflagged defect found (dead PDF/XLSX
  export stubs) — named as G-7 below. One previously-open gap (G-4) is resolved by this lens's direct
  read of the JS controller.

## 5. Consolidated gap register update

| Gap | Status after this file |
|---|---|
| G-1 (sequencing) | Unchanged — still open |
| G-2 (correction governance asymmetry) | Unchanged — still open; reproduced as UAT case 4 (§1) |
| G-3 (picking-level, not per-move, enforcement) | Unchanged — still open |
| G-4 (manual-trigger UI path not verified) | **RESOLVED THIS SESSION** — §4, JS controller read in full |
| G-5 (migration cutover cross-proof) | Unchanged — still open, still requires Accounting evidence |
| G-6 (no year-end P&L→Retained Earnings entry) | Unchanged, and independently reinforced by §3 (no Thai-specific override exists to rely on instead) |
| G-7 (new) — PDF/XLSX export stubs are empty in `stock_valuation_report.py` | **NEW**, named this session (§4) |

Net: 7 named gaps, one resolved, one new — not a wash used to make the count look smaller; both changes
are individually justified above.

## 6. Evidence integrity

All source files read in full for this challenge (`controller.js`, `stock_valuation_report.py` print
methods, `l10n_th`/`l10n_th_reports` manifests, `stock_landed_cost.py`) are hashed in
`06_CORR007B_SHA256_MANIFEST.txt` §E4/§E5. CSV evidence (`Dump_Index_Inventory.csv`,
`Dump_Table_Inventory.csv`) was already hashed under `01_...DRIFT_PROOF.md`'s citations where
applicable; the specific rows quoted here are reproducible from those same hashed files.

## 7. Disposition

This file does not close `N-A12-01`. It resolves one gap (G-4), adds one new gap (G-7), and
independently corroborates the existing mechanism proof from two angles files 08–09 had not used (dump
schema/index evidence; Thai-localization dependency graph). See
`11_CORR007B_N_A12_01_REVISED_FUNCTIONAL_DESIGN_DISPOSITION.md` for the consolidated final position.
