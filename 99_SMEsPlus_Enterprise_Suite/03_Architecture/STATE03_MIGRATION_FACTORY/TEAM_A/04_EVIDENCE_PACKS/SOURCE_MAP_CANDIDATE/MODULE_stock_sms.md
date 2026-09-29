# Source Map (candidate) — `stock_sms`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `stock_sms` |
| Display name | Stock - SMS |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `5043e4bf7320d632` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/stock_sms/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `stock`, `sms`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Inventory / Send text messages when final stock move
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 2, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `confirm.stock.sms` (Confirm Stock SMS)
- Objects extended from other modules (3): `res.company`, `stock.picking`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.company`, `stock.picking`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 39 of 39 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — stock_sms
Source revision: 19.0.post20260921 | Module: "Stock - SMS" (stock_sms/__manifest__.py:5) | License LGPL-3 (:22)
Basis: static reading of the source tree only; no runtime observation. No tests exist for this module (no tests folder present).

## A. Capabilities and optionality
- A1. Sends a text message (SMS) to the customer when an outgoing delivery is completed — conditional (per company setting + customer phone present + outgoing operation type). stock_sms/models/stock_picking.py:46-57
- A2. One-time warning wizard shown at the first delivery validation per company, asking the user whether SMS confirmations should be kept on or turned off. stock_sms/models/stock_picking.py:10-16,31-44; stock_sms/wizard/confirm_stock_sms.py:13-30
- A3. Company-level choice of which SMS template is used; default template "Delivery: Send by SMS Text Message" is supplied as seed data (noupdate). stock_sms/models/res_company.py:16-20; stock_sms/data/sms_data.xml:3-10
- A4. Optional/auto-installed: module is auto_install and depends on stock + sms, so it appears whenever both are present. stock_sms/__manifest__.py:10,18
- A5. Switching on "Text Confirmation" in Inventory settings triggers installation of this module (owned by stock). stock/models/res_config_settings.py:82-85
- A6. Activation is also on by default for companies without a template when the module is installed (post-install hook sets the text-confirmation flag on and assigns the default template). stock_sms/__init__.py:8-17; stock_sms/__manifest__.py:19
- A7. Uninstall hook switches text confirmation off for companies using the SMS type. stock_sms/__init__.py:20-27; stock_sms/__manifest__.py:21

## B. Objects, relationships, lifecycle
- B1. Delivery (stock.picking, owned by stock) is extended; no new persistent business object. The wizard confirm.stock.sms is a temporary record that holds the list of deliveries being validated. stock_sms/wizard/confirm_stock_sms.py:7-11
- B2. Company (res.company) gains a link to an SMS template limited to templates about deliveries, plus a "warning already shown" marker. stock_sms/models/res_company.py:16-21
- B3. Lifecycle hook point: the SMS logic sits on the delivery-validation path. Warning is evaluated in the pre-completion hook (stock owns the hook, called from button_validate); the SMS itself is sent in the post-completion confirmation step. stock/models/stock_picking.py:1436,1495,1288,1304; stock_sms/models/stock_picking.py:10,46
- B4. Wizard outcomes: "send" records the warning as seen and re-runs validation of the originally selected deliveries; "don't send" also switches the company text confirmation off, then re-runs validation. stock_sms/wizard/confirm_stock_sms.py:13-30
- B5. The wizard reads the originally selected deliveries from a context key set by stock's validate action. stock_sms/wizard/confirm_stock_sms.py:18; stock/models/stock_picking.py:1434-1435

## C. Validations, automation, security, multi-company
- C1. Gating for both warning and SMS: company text-confirmation flag is on with type "sms", delivery type is outgoing, and the customer (partner) has a phone value. stock_sms/models/stock_picking.py:21-23,49; stock/models/res_company.py:213-215
- C2. Warning is skipped when the company has already seen it, when the context carries a skip flag, and when running under automated tests. stock_sms/models/stock_picking.py:12,26,48
- C3. SMS is not sent when the skip flag is present or under tests. stock_sms/models/stock_picking.py:48
- C4. Template is read with elevated rights because ordinary users may lack read access to it. stock_sms/models/stock_picking.py:51-52
- C5. Access: stock managers get full create/read/update/delete on SMS templates; stock users can create/read/update the wizard but not delete. stock_sms/security/ir.model.access.csv:2-3
- C6. Record rule: stock managers' write/create/delete on SMS templates is limited to templates whose target model is stock.picking (read permission excluded from the rule). stock_sms/security/sms_security.xml:4-10
- C7. Multi-company: the template choice, warning marker and enablement flag are stored per company; the warning marker is written per company of the selected deliveries with elevated rights. stock_sms/models/res_company.py:16-21; stock_sms/wizard/confirm_stock_sms.py:15-17,23-28
- C8. Settings field is required in the UI only when text confirmation is on and type is SMS. stock_sms/views/res_config_settings_views.xml:14-17

## D. Handoffs to other modules
- D1. Delivery completion / hook owner: stock (button_validate, _pre_action_done_hook, _send_confirmation_email). stock/models/stock_picking.py:1420,1495,1304
- D2. Message dispatch: sms module (_message_sms_with_template; message not queued, sent immediately). sms/models/mail_thread.py:79; stock_sms/models/stock_picking.py:53-57
- D3. Credit purchasing widget for SMS credits shown in settings (IAP; owner sms/iap). stock_sms/views/res_config_settings_views.xml:19
- D4. The e-mail confirmation counterpart is stock-owned and is chained first (super call) before the SMS. stock/models/stock_picking.py:1304-1312; stock_sms/models/stock_picking.py:47
- D5. No accounting, valuation or approval handoff in this module; UNKNOWN — EVIDENCE INSUFFICIENT for audit-log behaviour of the SMS beyond the SMS module's own record.

## E. Configuration that changes outcomes
- E1. Company: "Stock Text Confirmation" flag and type (only SMS offered). stock/models/res_company.py:50-51
- E2. Company: SMS template (default seeded template; text mentions company name, order origin if present, tracking reference if the field exists). stock_sms/data/sms_data.xml:8
- E3. Company: "warning already received" marker; once set the confirmation wizard never reappears for that company. stock_sms/models/res_company.py:21; stock_sms/models/stock_picking.py:26
- E4. Install/uninstall hooks change the flag for all companies as noted in A6/A7.

## F. Extension path (Community modules that extend the key objects; names only)
- stock.picking (base owner stock; also extended by): delivery_stock_picking_batch, l10n_ar_stock, l10n_in_ewaybill_stock, l10n_in_purchase_stock, l10n_in_sale_stock, l10n_in_stock, l10n_it_stock_ddt, l10n_ro_edi_stock, l10n_ro_edi_stock_batch, l10n_tr_nilvera_edispatch, mrp, mrp_subcontracting, mrp_subcontracting_dropshipping, mrp_subcontracting_purchase, point_of_sale, pos_repair, pos_sale, product_expiry, project_stock, purchase_stock, repair, sale_project_stock, sale_stock, stock_account, stock_delivery, stock_dropshipping, stock_fleet, stock_picking_batch, website_sale_stock (stock_sms included).
- res.company (SMS-relevant): stock, stock_sms, sms, sms_twilio (plus many localisation modules; not enumerated further).
- res.config.settings: stock, stock_sms, sms_twilio, pos_sms.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour on failed SMS delivery (no error handling visible in this module); dispatch details live in the sms module.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the result is identical when validation is triggered from Point of Sale, mobile or API paths (only the standard validate path was read).
- UNKNOWN — EVIDENCE INSUFFICIENT: cost or IAP credit behaviour (owned by sms/iap; not read).

