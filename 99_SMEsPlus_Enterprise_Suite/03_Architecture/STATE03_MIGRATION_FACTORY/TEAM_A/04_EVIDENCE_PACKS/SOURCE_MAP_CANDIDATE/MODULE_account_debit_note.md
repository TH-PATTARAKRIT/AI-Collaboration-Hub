# Source Map (candidate) — `account_debit_note`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `account_debit_note` |
| Display name | Debit Notes |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c9cdddc5b465d1d5` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/account_debit_note/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (8): `l10n_co`, `l10n_ec`, `l10n_hu_edi`, `l10n_in`, `l10n_it_edi`, `l10n_latam_invoice_document`, `l10n_pe`, `l10n_sa`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / Debit Notes
- Inventory of user-facing artifacts (counts): menu items 0, views 6, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `account.debit.note` (Add Debit Note wizard)
- Objects extended from other modules (2): `account.move`, `account.journal`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `account.debit.note` ← Community: `l10n_hu_edi`, `l10n_latam_invoice_document`, `l10n_sa`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `account.move`, `account.journal`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 31 of 31 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — account_debit_note
Source revision: 19.0.post20260921 | Module: "Debit Notes" (account_debit_note/__manifest__.py:5) | depends: account (:15) | License LGPL-3 (:25)
Basis: static reading; one test file read (2 tests). Not auto_install (no such key in manifest) — optional module, installed explicitly.

## A. Capabilities and optionality
- A1. Lets an accountant raise a "debit note" against a posted customer invoice, customer credit note, vendor bill or vendor credit note, keeping a link to the original document. account_debit_note/wizard/account_debit_note.py:8-13,34-39; account_debit_note/models/account_move.py:10
- A2. Entry points: a "Debit Note" button on posted documents (invoicing group) and a bound list/kanban action, both leading to the same wizard. account_debit_note/views/account_move_view.xml:19-24; account_debit_note/wizard/account_debit_note_view.xml:30-38
- A3. Option to copy the original lines into the debit note (shown only when the origin is not a credit note). account_debit_note/wizard/account_debit_note_view.xml:16; account_debit_note/wizard/account_debit_note.py:22-24
- A4. Optional dedicated numbering series for debit notes per sales/purchase journal. account_debit_note/models/account_journal.py:7-18; account_debit_note/views/account_journal_views.xml:9
- A5. Invoice PDF titles switch to "Debit Note" wording (draft, proforma, cancelled variants and date label) when the document has an origin link. account_debit_note/views/report_invoice.xml:4-51
- A6. Navigation aids: smart button with debit-note count on the origin, "Debit Note" search filters on entries, invoices and journal items. account_debit_note/views/account_move_view.xml:8-15,28-63

## B. Objects, relationships, lifecycle
- B1. A debit note is an ordinary accounting document (account.move, owner account) with an extra "original document debited" link (read-only, not copied on duplication) and its reverse list of debit notes. account_debit_note/models/account_move.py:10-13
- B2. Wizard (temporary, account.debit.note) holds selected posted documents, date (default today), reason, optional specific journal, copy-lines flag. account_debit_note/wizard/account_debit_note.py:16-24
- B3. Created document type: credit-note origins become a normal invoice/bill (customer credit note -> customer invoice; vendor credit note -> vendor bill); invoices/bills keep their type. account_debit_note/wizard/account_debit_note.py:54-58 (TEST: tests/test_out_debit_note.py:26,45)
- B4. New document is created by duplicating the origin with overridden values: reference (origin number plus optional reason), date, invoice date, journal (wizard journal, else origin's), payment terms cleared, link to origin. account_debit_note/wizard/account_debit_note.py:59-67,75-78
- B5. Result state: draft (must then be confirmed/posted through account's normal flow). (TEST) account_debit_note/tests/test_out_debit_note.py:27,46
- B6. Lines are dropped unless copy-lines is set (test: default vendor-credit-note case has no lines). account_debit_note/wizard/account_debit_note.py:68-69 (TEST: tests/test_out_debit_note.py:25,44). Note: the exclusion for credit-note origins in the code compares the type to a nested list at :68; the form hides the flag for credit notes instead (view :16). UNKNOWN — EVIDENCE INSUFFICIENT on effect if the flag were forced on for a credit-note origin without running it.
- B7. Returned action opens the single new note in form, or a list for several. account_debit_note/wizard/account_debit_note.py:80-95

## C. Validations, security, multi-company
- C1. Wizard refuses: any non-posted document; any document that itself has an origin link (already a debit note); any type outside the four listed. account_debit_note/wizard/account_debit_note.py:34-39
- C2. Wizard selection domain restricts to posted entries. account_debit_note/wizard/account_debit_note.py:17
- C3. Access: wizard model read/write/create for the invoicing group (account.group_account_invoice), no delete. account_debit_note/security/ir.model.access.csv:2. No new record rules or groups.
- C4. Journal choice in the wizard is limited to sales or purchase journals according to origin type. account_debit_note/wizard/account_debit_note_view.xml:19; account_debit_note/wizard/account_debit_note.py:49-52
- C5. Multi-company: no explicit handling; the copy inherits the origin's company through duplication and journal choice follows account's journal/company rules. UNKNOWN — EVIDENCE INSUFFICIENT for cross-company restrictions.
- C6. Wizard shows a country-code field derived from the origin's company; use elsewhere not found in this module. account_debit_note/wizard/account_debit_note.py:28

## D. Handoffs
- D1. Posting, journal items, tax, receivable/payable, payment and reconciliation: account (this module only creates the draft). account_debit_note/wizard/account_debit_note.py:77
- D2. Sequence: with dedicated series on, the last-number search is split between documents with and without an origin link, and new series numbers start with the letter D for invoices and bills. account_debit_note/models/account_move.py:37-51
- D3. Chatter message on the copy states "created from" the origin. account_debit_note/models/account_move.py:53-57
- D4. Copy includes sale/purchase business links via context flag (owned by sale/purchase modules). account_debit_note/wizard/account_debit_note.py:75
- D5. E-invoicing consumers read the origin link: account_edi_ubl_cii, l10n_* EDI localisations (see F). No inventory or approval handoff.

## E. Configuration that changes outcomes
- E1. Journal "Dedicated Debit Note Sequence": computed default true for sale and purchase journals, editable, stored. account_debit_note/models/account_journal.py:15-18
- E2. Wizard choices: date, reason, journal, copy lines (see B2).

## F. Extension path (module names only)
- account.move (many modules, partial): account, account_debit_note, account_edi, account_edi_ubl_cii, account_fleet, account_payment, account_peppol, hr_expense, purchase, sale, sale_stock, point_of_sale, stock_account, website_sale and many l10n_* modules.
- account.journal: account, account_check_printing, account_debit_note, account_edi, account_payment, account_peppol, point_of_sale and l10n_* modules.
- Modules that reference debit_origin_id: account_debit_note, account_edi_ubl_cii, l10n_bg_ledger, l10n_br, l10n_ec, l10n_fr_pdp, l10n_hu_edi, l10n_hu_edi_receive, l10n_in, l10n_in_edi, l10n_in_ewaybill_irn, l10n_it_edi, l10n_latam_invoice_document, l10n_lk_invoice, l10n_my_edi, l10n_sa, l10n_sa_edi, l10n_tw_edi_ecpay, l10n_uy.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: tax/analytic effects of the copied document beyond account's standard duplication.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether a debit note document can itself receive another debit note through paths other than the wizard.
- UNKNOWN — EVIDENCE INSUFFICIENT: legal treatment per country (owned by l10n_* modules; not read).

