# Source Map (candidate) — `contacts`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `contacts` |
| Display name | Contacts |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c980712064b9fffb` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/contacts/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `mail`
- Direct dependents in 300-module list (3): `base_address_extended`, `crm`, `mail_plugin`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (4): `l10n_cl`, `l10n_latam_base`, `l10n_tr_nilvera_einvoice_extended`, `mass_mailing`
- Custom / third-party modules that declare a dependency (name — license only) (8): `partner_company_type` — AGPL-3, `19_contact_reference_sequence` — OPL-1, `bh_parent_company` — LGPL-3, `monday_odoo_connector` — AGPL-3, `base_location` — AGPL-3, `base_accounting_kit` — LGPL-3, `monday_smesplus_connector` — AGPL-3, `contact_reference_sequence` — OPL-1

## 3. Capabilities / functions
- Manifest category / summary: Sales/CRM / Centralize your address book
- Inventory of user-facing artifacts (counts): menu items 12, views 0, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `res.users`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.users`, `res.partner`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 18 of 18 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: contacts (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities
- Address-book application: home-page entry showing partners (customers, vendors, others) in list, card, form and activity views (contacts/__manifest__.py:6-13,21; contacts/views/contact_views.xml:3-8).
- OPTIONAL application (application flag, depends on base and mail only) (contacts/__manifest__.py:14,21). Not auto-installed.
- Contains no new business data model: it is a presentation layer over the base partner record (contacts/models/res_partner.py:6-7; contacts/views/contact_views.xml:6).

## B. Business objects and lifecycle
- Uses base Partner, Contact Tags, Industries, Countries, States, Country Groups, Banks, Partner Bank Accounts through menu entries only (contacts/views/contact_views.xml:56-95).
- New contacts default to "company" type via the menu action's default context (contacts/views/contact_views.xml:9; (TEST) contacts/tests/test_ui.py:22-32).
- Demo data: sample message with a scheduled notification on a demo partner (contacts/data/mail_demo.xml:5-17).

## C. Validations, automation, security
- Menu is visible to internal users and to the Contact Creation group (contacts/views/contact_views.xml:38-42). Configuration submenu limited to system administrators (contacts/views/contact_views.xml:50-54).
- No access files, groups, record rules or company scoping added by this module (contacts/__manifest__.py:15-17 lists only a view file). Partner-level access is governed by base: UNKNOWN — EVIDENCE INSUFFICIENT here.
- Customer-facing tax label follows the company country's VAT label on partner views ((TEST) contacts/tests/test_ui.py:35-52).

## D. Handoffs
- Partner data and its access: base. Chatter, activities: mail. The Contacts app is registered as a back-office root menu for partners (contacts/models/res_partner.py:9-10) and replaces the generic partner icon in the activity systray (contacts/models/res_users.py:9-18).
- Sales-side contact use (CRM, orders): crm/sale, see F.

## E. Configuration
- Activity-icon behaviour is fixed; no settings. Default "company" creation is only via this app's action (contacts/views/contact_views.xml:9). A user-defined default on company type would override it ((TEST) contacts/tests/test_ui.py:27-32).

## F. Extension path (modules depending on it)
- base_address_extended, crm, l10n_cl, l10n_latam_base, l10n_tr_nilvera_einvoice_extended, mail_plugin, mass_mailing (manifest dependency scan).

## G. Not verified
- Which optional partner tabs appear per installed module: UNKNOWN — EVIDENCE INSUFFICIENT.
- Tour test contacts/static/tests/tours/debug_menu_set_defaults.js exists (TEST), not analysed.

