# Source Map (candidate) — `account_check_printing`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `account_check_printing` |
| Display name | Check Printing Base |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `53cf328860b8087d` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/account_check_printing/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (1): `base_accounting_kit` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / Check printing basic features
- Inventory of user-facing artifacts (counts): menu items 0, views 6, window actions 0, server actions 1, reports 0, mail templates 0, scheduled jobs 0, wizards 2, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `print.prenumbered.checks` (Print Pre-numbered Checks)
- Objects extended from other modules (5): `account.journal`, `account.payment.method`, `account.payment`, `res.company`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `account.journal`, `account.payment.method`, `account.payment`, `res.company`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 3 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 47 of 47 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — account_check_printing
Source revision: 19.0.post20260921 | Module: "Check Printing Base" (account_check_printing/__manifest__.py:5) | depends: account (:14) | License LGPL-3 (:26)
Basis: static reading; tests read only by test name/assertion outline. Manifest states this is the base for country-specific check templates (:10-11).

## A. Capabilities and optionality
- A1. Adds a "Checks" outbound payment method for bank-type journals, allowing vendor payments to be paid by printed check. account_check_printing/data/account_check_printing_data.xml:5-9; account_check_printing/models/account_payment_method.py:13
- A2. Optional: installed through the accounting setting "Allow check printing and deposits" (company-dependent, accountant group). account/models/res_config_settings.py:85; account/views/res_config_settings_views.xml:246-248
- A3. Not auto_install; the module itself provides no printable layout: the company layout list contains only "None (disabled)" until another module adds entries. account_check_printing/models/res_company.py:9-16. UNKNOWN — EVIDENCE INSUFFICIENT whether any Community module ships a layout (grep for layout additions found none in this tree; l10n_latam_check extends payments but layout provision not verified).
- A4. Print action on payments (list/kanban "Print Checks", restricted to accountant group), plus a "Print Check" button on the payment form when a layout exists. account_check_printing/data/account_check_printing_data.xml:11-21; account_check_printing/views/account_payment_views.xml:9
- A5. Actions "Unmark Sent" and "Void Check" on the form. Void = reset to draft then cancel. account_check_printing/views/account_payment_views.xml:10-11; account_check_printing/models/account_payment.py:205-207
- A6. Dashboard shortcut on bank journals: count of checks still to print and link to list. account_check_printing/models/account_journal.py:96-120; account_check_printing/views/account_journal_views.xml:8-19
- A7. Pre-numbered check flow via a small wizard when the journal does not do manual numbering. account_check_printing/models/account_payment.py:173-200; account_check_printing/wizard/print_prenumbered_checks.py:21-32
- A8. Check stub (summary of paid bills/refunds), amount in words, multi-page stub option. account_check_printing/models/account_payment.py:98-104,225-350

## B. Objects, relationships, lifecycle
- B1. Payment (account.payment, owner account) gets: check number, amount in words, sequencing flag, stub logic. account_check_printing/models/account_payment.py:15-31
- B2. Bank journal (account.journal) gets: manual-numbering flag, a private numbering sequence (created automatically per journal, gap-free, padding 5), next check number, optional journal-specific layout. account_check_printing/models/account_journal.py:19-41,79-94
- B3. Company gets layout choice, date-label option, multi-page stub option and three margins (top/left/right). account_check_printing/models/res_company.py:11-44
- B4. Lifecycle handled with the payment states of account (draft -> in process -> paid, plus sent flag). Ready-to-print = check method + state in process + not yet sent. account_check_printing/models/account_journal.py:98-102; account/models/account_payment.py:39,54
- B5. Sequence choice: with manual numbering on, the number is drawn from the journal sequence at posting time; without it, the user types the first pre-printed number in the wizard and following payments get consecutive numbers. account_check_printing/models/account_payment.py:155-160; account_check_printing/wizard/print_prenumbered_checks.py:22-29
- B6. Printing marks the payment as sent and returns the report chosen from the journal layout, falling back to the company layout. account_check_printing/models/account_payment.py:209-220
- B7. Wizard first posts drafts, flags in-process payments as sent, assigns numbers, then prints. account_check_printing/wizard/print_prenumbered_checks.py:25-30

## C. Validations, security, multi-company
- C1. Check number must be digits only; also enforced in the wizard and on the journal's next-number field. account_check_printing/models/account_payment.py:47-51; account_check_printing/wizard/print_prenumbered_checks.py:15-19; account_check_printing/models/account_journal.py:59-60
- C2. Uniqueness: among posted payments in the same journal, the same numeric check number may not repeat. account_check_printing/models/account_payment.py:63-96 (TEST: tests/test_print_check.py:286-)
- C3. Journal next number cannot be lower than the sequence's current position and cannot exceed 2,147,483,647. account_check_printing/models/account_journal.py:62-75 (TEST: tests/test_print_check.py:352-,369-)
- C4. Printing rejects payments that are not check-method, or already sent; all selected payments must share one journal; missing/invalid layout gives a redirect to accounting settings. account_check_printing/models/account_payment.py:165-171,209-218
- C5. Security: wizard access limited to accounting users (read/write/create, no delete); print server action bound to that group. account_check_printing/security/ir.model.access.csv:2; account_check_printing/data/account_check_printing_data.xml:16. No record rules defined in this module.
- C6. Multi-company: layout, margins, stub options are stored on the company; the journal sequence is created with the journal's company; company scoping of payments follows account. account_check_printing/models/res_company.py:11-44; account_check_printing/models/account_journal.py:88-94
- C7. Margin-right and date-label settings are shown only for Canadian company country. account_check_printing/views/res_config_settings_views.xml:24-32

## D. Handoffs
- D1. Payment posting, journal entries, reconciliation, sent/unsent: account. Check number is part of the payment's move-line display label. account_check_printing/models/account_payment.py:134-153; account/models/account_payment.py:1127
- D2. Payment method availability and default outbound method lines for bank journals: account (extended here). account_check_printing/models/account_journal.py:13-17
- D3. Reporting/layout: report actions owned by whichever layout module registers them (key = report xml id). account_check_printing/models/res_company.py:9-10
- D4. Stub content comes from reconciled bills/refunds of the payment's journal entry (account), converting residual amounts if no entry yet. account_check_printing/models/account_payment.py:289-331
- D5. Check number changes trigger payment/journal-entry sync via the trigger-field list. account_check_printing/models/account_payment.py:130-132
- D6. Post-install hook creates sequences for existing bank journals. account_check_printing/__init__.py:7-8; account_check_printing/__manifest__.py:24

## E. Configuration that changes outcomes
- E1. Company layout ("None" disables printing). E2. Journal layout override. E3. Journal manual numbering (changes who assigns numbers). E4. Multi-page stub (crop after 9 lines or spread over pages). account_check_printing/models/account_payment.py:9,334-348. E5. Margins/date label. E6. Payment method "check_printing" must be enabled on the journal's outbound lines. account_check_printing/views/account_journal_views.xml:29-30

## F. Extension path (module names only)
- account.payment: account_check_printing, account_payment, hr_expense, l10n_account_withholding_tax, l10n_ar_withholding, l10n_au, l10n_ch, l10n_in, l10n_latam_check, l10n_nz, l10n_ph, l10n_pl_bank_verification, point_of_sale, pos_online_payment, website_payment.
- account.journal: account, account_check_printing, account_debit_note, account_edi, account_payment, account_peppol, l10n_latam_check and many l10n_* / point_of_sale.
- account.payment.method: account_check_printing, account_payment, l10n_latam_check.
- res.company / res.config.settings: account, account_check_printing (among many).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: which report layouts exist and their paper geometry (layout modules not present or not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: how l10n_latam_check interacts with this module's numbering.
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of the account-side payment flow when a printed check is later voided after bank reconciliation.
- UNKNOWN — EVIDENCE INSUFFICIENT: full test coverage summary beyond the test names read (test_print_check.py:26-369).

