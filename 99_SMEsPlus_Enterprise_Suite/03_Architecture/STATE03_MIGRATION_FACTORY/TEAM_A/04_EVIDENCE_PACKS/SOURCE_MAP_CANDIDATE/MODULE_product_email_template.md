# Source Map (candidate) — `product_email_template`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `product_email_template` |
| Display name | Product Email Template |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d437841a1d6c8ae9` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/product_email_template/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / —
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `account.move`, `product.template`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `account.move`, `product.template`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 23 of 23 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: product_email_template
Source revision: 19.0.post20260921 | Path root: odoo/addons | Method: read-only source reading, neutral wording

## A. Capabilities
- Lets a product carry an optional email template; when a customer invoice containing that product is confirmed (posted), the template is sent through the invoice's message thread (product_email_template/models/product.py:6-16; product_email_template/models/account_move.py:9-29). Purpose example: send training agenda/material on invoicing a course (product_email_template/__manifest__.py:`description`).
- Optional module, depends only on `account`; no auto-install (product_email_template/__manifest__.py:`depends`).
- Product form gets an "Automatic Email at Invoice" block on the Invoicing tab; the choice list is limited to templates written for invoices (account.move) and the quick-create form is a simplified body/attachments form (product_email_template/views/product_views.xml:8-19; product_email_template/views/mail_template_views.xml:3-20).
- The Invoicing tab on the product form becomes visible only to Invoicing and Accounting read-only groups (product_email_template/views/product_views.xml:20-22).

## B. Business objects / lifecycle
- Extends product template (adds one link field to mail template) and journal entry/invoice (account.move) (product_email_template/models/product.py:11-16; models/account_move.py:6-7). No new object, no states.
- Trigger: any posting of moves runs the mail step after the standard posting; only customer invoices (not credit notes, vendor bills, entries) are processed (product_email_template/models/account_move.py:25-29, 13-14).
- One message per invoice line whose product has a template; a repeated product on two lines gives two messages (product_email_template/models/account_move.py:16-22; TEST product_email_template/tests/test_account_move.py:24-46 shows one message for one line). Message is posted as a normal comment with light notification layout (models/account_move.py:15-22).
- No guard against re-sending when an invoice is reset to draft and posted again: none found in this module (inference from models/account_move.py:25-29; not tested).
- Under an elevated (superuser-sudo) call the message is sent as the system user so a sender address exists (product_email_template/models/account_move.py:10-12; TEST tests/test_account_move.py:48-70, portal-like public user scenario).

## C. Validations / security / multi-company
- No constraints, no access file, no record rule in this module (manifest `data` lists views only). Access follows the product, mail template, and invoice rules of their owner modules.
- Template selection domain restricts to invoice-model templates (views/product_views.xml:11); this is a UI domain, not an enforced constraint. UNKNOWN — EVIDENCE INSUFFICIENT whether a template of another model could be stored through code.
- Company scoping: product field is company-independent in this module (no company_dependent flag, models/product.py:13); template/company visibility is governed by owner modules. UNKNOWN — EVIDENCE INSUFFICIENT for cross-company templates.
- Recipients, sender, attachments are taken from the template definition (message_post_with_source, models/account_move.py:18-22); recipient rules live in `mail`. UNKNOWN — EVIDENCE INSUFFICIENT for who receives the mail when a template has no recipient settings.

## D. Handoffs
- Invoice posting: owned by `account` (override of posting step, models/account_move.py:25-29).
- Message/template rendering, email queue, notification layout: owned by `mail` (models/account_move.py:18-22).
- Product data and Invoicing tab: owned by `product` / `account` (views/product_views.xml:6,8).
- Audit trail: the sent email appears in the invoice's message history (models/account_move.py:18).
- No accounting entry, stock or approval effect.

## E. Configuration that changes outcomes
- Per-product template link (Invoicing tab). Template content, recipients, attachments (in mail template).
- Only when a template is set on the product; no company-level switch or setting exists in this module.

## F. Extension path
- No Community module lists product_email_template as a manifest dependency (manifest grep: none).
- Modules extending the product template object (product.template), any feature: account, event_booth_sale, event_product, event_sale, hr_expense, l10n_account_withholding_tax, l10n_ar_website_sale, l10n_de, l10n_eg_edi_eta, l10n_gr_edi, l10n_hr_edi, l10n_hu_edi, l10n_id_efaktur_coretax, l10n_in, l10n_in_pos, l10n_my, l10n_my_edi, l10n_pl, l10n_ro_cpv_code, l10n_tr, l10n_tr_nilvera_einvoice_extended, loyalty, mrp, mrp_account, partnership, point_of_sale, pos_discount, pos_loyalty, pos_sale, pos_self_order, product_email_template, product_expiry, product_matrix, purchase, purchase_stock, repair, sale, sale_expense, sale_gelato, sale_product_matrix, sale_project, sale_purchase, sale_stock, sale_timesheet, stock, stock_account, stock_delivery, stock_landed_costs, website_event_booth_sale, website_event_sale, website_sale_collect, website_sale_gelato, website_sale_slides, website_sale_stock, website_sale_stock_wishlist, website_sale_wishlist.
- Modules extending the invoice/entry object (account.move) form a very long list (about 110 modules: account_*, l10n_*, sale, purchase, stock_account, point_of_sale, website_sale, hr_expense, etc.); whether any of them override the posting step in a way that interacts with this module: UNKNOWN — EVIDENCE INSUFFICIENT.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour for payment-terminal / point-of-sale / subscription invoices posted in background.
- UNKNOWN — EVIDENCE INSUFFICIENT: email failure handling (queue retries) - owned by `mail`, not read.

