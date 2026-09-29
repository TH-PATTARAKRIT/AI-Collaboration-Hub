# Source Map (candidate) — `base`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `base` |
| Display name | Base |
| Manifest version | 1.3 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `0ad4109fd814b921` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/base/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): —
- Direct dependents in 300-module list (25): `analytic`, `auth_ldap`, `auth_oauth`, `base_address_extended`, `base_automation`, `base_setup`, `base_sparse_field`, `bus`, `calendar`, `contacts`, `fleet`, `html_builder` … (+13)
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (19): `l10n_cn`, `l10n_ec`, `l10n_fr`, `l10n_gt`, `l10n_hn`, `l10n_ma`, `l10n_mz`, `l10n_pt`, `l10n_us`, `test_assetsbundle`, `test_converter`, `test_inherit` … (+7)
- Custom / third-party modules that declare a dependency (name — license only) (39): `product_sequence` — LGPL-3, `partner_company_type` — AGPL-3, `19_bhpro_product_part` — OPL-1, `nthub_binary_field_preview` — LGPL-3, `19_bhpro_purchase_ext` — OPL-1, `order_line_sequence` — AGPL-3, `19_sale_lazada` — OPL-1, `product_brand_sale` — AGPL-3, `app_icon_hide` — LGPL-3, `19_bhpro_menu_general` — OPL-1, `scgl_inventory_lot_filter` — LGPL-3, `19_attachment_dedup_fix` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 66, views 177, window actions 66, server actions 2, reports 2, mail templates 0, scheduled jobs 2, wizards 22, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (124): `base.partner.merge.line` (Merge Partner Line); `base.partner.merge.automatic.wizard` (Merge Partner Wizard); `base.module.uninstall` (Module Uninstall); `wizard.ir.model.menu.create` (Create Menu Wizard); `base.language.import` (Language Import); `base.module.upgrade` (Upgrade Module); `base.module.update` (Update Module); `base.language.export` (Language Export); `base.language.install` (Install Language); `ir.default` (Default Values); `res.lang` (Languages); `properties.base.definition.mixin` (Properties Base Definition Mixin); `ir.mail_server` (Mail Server); `ir.rule` (Record Rule); `base` (Base); `_unknown` (Unknown); `ir.model` (Models); `ir.model.fields` (Fields); `ir.model.inherit` (Model Inheritance Tree); `ir.model.fields.selection` (Fields Selection); `ir.model.constraint` (Model Constraint); `ir.model.relation` (Relation Model); `ir.model.access` (Model Access); `ir.model.data` (Model Data); `ir.autovacuum` (Automatic Vacuum) … (+99)
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 1 field(s); company-consistency auto-check declared on 1 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `base.partner.merge.automatic.wizard` ← Community: `account`, `loyalty`, `mail`, `website`, `website_slides`; open-license custom/third-party scanned: —
- `base.module.uninstall` ← Community: `base_import_module`, `mail`; open-license custom/third-party scanned: —
- `base.language.install` ← Community: `website`; open-license custom/third-party scanned: —
- `res.lang` ← Community: `http_routing`, `point_of_sale`, `spreadsheet`, `survey`, `website`; open-license custom/third-party scanned: —
- `properties.base.definition.mixin` ← Community: `mass_mailing`, `test_orm`; open-license custom/third-party scanned: —
- `ir.mail_server` ← Community: `google_gmail`, `mail`, `mass_mailing`, `microsoft_outlook`; open-license custom/third-party scanned: —
- `ir.rule` ← Community: `website`; open-license custom/third-party scanned: —
- `base` ← Community: `base_import`, `base_sparse_field`, `hr`, `html_editor`, `mail`, `phone_validation`, `sms`, `transifex`, `web`, `web_hierarchy` … (+1); open-license custom/third-party scanned: —
- `ir.model` ← Community: `bus`, `mail`, `marketing_card`, `mass_mailing`, `sms`, `spreadsheet`, `web`, `website`; open-license custom/third-party scanned: —
- `ir.model.fields` ← Community: `base_sparse_field`, `mail`, `website`; open-license custom/third-party scanned: —
- `ir.model.data` ← Community: `website`; open-license custom/third-party scanned: —
- `ir.actions.report` ← Community: `account`, `account_edi`, `account_edi_ubl_cii`, `hr_expense`, `l10n_ch`, `l10n_de`, `l10n_din5008`, `l10n_th`, `purchase`, `sale` … (+3); open-license custom/third-party scanned: `account_financial_report`, `l10n_th_withholding_tax_report`, `mis_builder`, `report_xlsx`, `report_xlsx_helper`
- `ir.http` ← Community: `account`, `auth_password_policy_portal`, `auth_password_policy_signup`, `auth_signup`, `auth_timeout`, `barcodes`, `barcodes_gs1_nomenclature`, `base_import_module`, `base_setup`, `bus` … (+32); open-license custom/third-party scanned: `web_responsive`
- `res.country` ← Community: `base_address_extended`, `base_vat`, `l10n_ar`, `l10n_cl`, `payment`, `point_of_sale`, `pos_self_order`; open-license custom/third-party scanned: `base_location_geonames_import`
- `res.country.group` ← Community: `account`, `product`; open-license custom/third-party scanned: —
- `res.country.state` ← Community: `l10n_in`, `point_of_sale`; open-license custom/third-party scanned: `l10n_th_base_location`
- `ir.attachment` ← Community: `account`, `account_edi`, `api_doc`, `attachment_indexation`, `bus`, `cloud_storage`, `cloud_storage_azure`, `cloud_storage_google`, `cloud_storage_migration`, `hr_expense` … (+14); open-license custom/third-party scanned: `19_attachment_dedup_fix`
- `res.users.settings` ← Community: `bus`, `calendar`, `google_calendar`, `im_livechat`, `mail`, `microsoft_calendar`, `project`, `web`; open-license custom/third-party scanned: —
- `res.bank` ← Community: `l10n_cl`, `l10n_mx`, `l10n_pe`, `l10n_us_account`; open-license custom/third-party scanned: —
- `res.partner.bank` ← Community: `account`, `account_qr_code_emv`, `account_qr_code_sepa`, `base_iban`, `hr`, `l10n_ar`, `l10n_au`, `l10n_br`, `l10n_ch`, `l10n_hk` … (+7); open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: —

## 6. Actions / states / validation / automation / security
- State fields found: `base.partner.merge.automatic.wizard` → ['option', 'selection', 'finished']; `base.module.update` → ['init', 'done']; `base.language.export` → ['choose', 'get']; `ir.model` → ['manual', 'base']; `ir.model.fields` → ['manual', 'base']; `res.users.deletion` → ['todo', 'done', 'fail']; `ir.module.module` → ['uninstallable', 'uninstalled', 'installed', 'to upgrade', 'to remove', 'to install']; `ir.actions.server` → ['object_write', 'object_create', 'object_copy', 'code', 'webhook', 'multi']
- Validation: 46 declarative constraint method(s), 41 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Base: Auto-vacuum internal data every ? ?; Base: Portal Users Deletion every ? ?
- Security: groups declared 2 (`default_user_group`, `base.group_portal`); record rules 32 (of which company-scoped by text 7); access rows 146

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 3 of 60 source pointers resolve to an existing file and in-range line (57 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note - module `base`

Revision: `19.0.post20260921` (Odoo Community, clean-room study, read-only).
Tree root used for pointers: `odoo-19.0.post20260921/`. Short prefix `B/` = `odoo/addons/base/`; `O/` = `odoo/orm/`.
Manifest: `B/__manifest__.py` - name "Base", version 1.3, no dependencies, category Hidden, described as the kernel needed for every installation.
Skeleton cross-referenced: `/Users/admin/STATE03_RESTRICTED_LOCAL/sourcemap/base.json`.
Scope of this note is business meaning only; no code is reproduced. Anything not read is listed in section G.

## A. Capabilities by business area (core / optional / conditional)

CORE (always present because `base` is always installed)
- Organisation identity: legal-entity records ("companies") with a hierarchy of branches, each backed by one partner record. `B/models/res_company.py:31`.
- People and access: internal, portal and public user types, permission groups with inheritance, table-level access rights and row-level rules. `B/models/res_users.py:155`, `B/models/res_groups.py:9`, `B/models/ir_rule.py:15`, `B/models/ir_model.py:2080`.
- Master data for parties: partners (customers/vendors/contacts/addresses), tags, industries, bank and bank-account records, countries/states, languages. `B/models/res_partner.py:184`, `B/models/res_bank.py:16,73`.
- Currencies and dated exchange rates with conversion and rounding services. `B/models/res_currency.py:20,346`.
- Numbering: configurable document sequences (prefix, suffix, padding, step, optional per-date-range sub-sequences). `B/models/ir_sequence.py:85,295`.
- Files: attachment store (database or file storage), access follows the linked record. `B/models/ir_attachment.py:61`.
- Scheduling: scheduled actions (cron) with failure tracking and auto-deactivation. `B/models/ir_cron.py:91`.
- Server actions (update record, create record, duplicate, run code, webhook, multi-step) - the execution primitive other modules trigger. `B/models/ir_actions.py:567`.
- System parameters (key/value per database) and stored user/company default values. `B/models/ir_config_parameter.py:29`, `B/models/ir_default.py:13`.
- Module lifecycle (install/upgrade/uninstall, dependency and exclusion tracking, country-based auto-install of localization modules). `B/models/ir_module.py:157`.
- Technical audit columns (created-by/created-on/updated-by/updated-on) added to every persisted model unless a model opts out. `O/models.py:283,296`.
- Application log table for server-side and client-side log lines. `B/models/ir_logging.py:5`.
- Settings framework (res.config.settings) that maps a settings screen to groups, modules and system parameters. `B/models/res_config.py:99,149`.

OPTIONAL / SEPARATE MODULES (not in `base`; confirmed present in tree)
- Event-driven automation rules (create/update/archive/time-based triggers, stage/user/tag/state/priority set): module `base_automation`, `base_automation/models/base_automation.py:98-186`. `base` itself provides only the server action that such rules run.
- Field-change tracking / chatter: module `mail` (`mail/models/mail_tracking_value.py`). `base` has no tracking of individual field changes.
- Tax-ID format validation: module `base_vat`. Bank-account number validation: `base_iban`. Structured street fields: `base_address_extended`. Settings screen: `base_setup`.
- Partner merge is a wizard shipped inside `base` but exposed to users only via menu/security data (see C).

CONDITIONAL
- Multi-company switcher rights and multi-currency rights are auto-toggled by data, not chosen manually (see C, "Automatic group toggles").
- Localization auto-install when a company gets a country and matching modules are not yet installed. `B/models/res_company.py:207-244`.
- Attachment storage location depends on a system parameter (E).

## B. Business objects, neutral relationships, lifecycle

Company (`res.company`)
- Every company owns exactly one partner (required link). Name, email, phone, website, tax ID and company registry are mirrored from that partner (`B/models/res_company.py:48,81-85`); address fields are computed from the partner (`:137`, `:69-78`).
- Parent/branch tree with stored path; root company resolved per record (`:51-56`, `:131`). Company name is unique (`:97`). Currency is required.
- Lifecycle: created together with its partner when none is supplied (`:289-312`); creator and the system user are added to the company's allowed users automatically (`:325-328`); its currency is force-activated (`:331`); a country triggers localization install (`:333-336`). Hierarchy cannot be changed after creation (`:357-358`). Archiving cascades to branches (`:381-382`).

User (`res.users`)
- A user is an extension of a partner (identity fields live on the partner); the partner link is required and protected from deletion. `B/models/res_users.py:163-165,214`.
- Holds: unique login (`:216`,`:274`), default company (required) and list of allowed companies (`:245-250`), explicitly assigned groups plus computed "all groups including implied" (`:257-259`), home action, settings record, devices, API keys, login log.
- User type (internal vs shared/portal/public) is computed from whether the user belongs to the internal-user group (`:460-465`).
- Role helper: "User" or "Administrator" (`:272`, `:429-445`).
- Lifecycle: internal users get a personal settings record at creation, an avatar is generated when no image, partner active flag follows user (`:579-594`). Deactivating the current user or activating the technical superuser is refused (`:597-600`). Admin and template/public users cannot be deleted (`:648-661`). Portal users may request their own deletion; a daily job later removes them (`:934-990`; `B/models/res_users_deletion.py:37`; `B/data/ir_cron_data.xml:13`).

Group (`res.groups`)
- Belongs optionally to a "privilege" (a labelled family of groups) which belongs to a module category (`B/models/res_groups_privilege.py:4-14`, `B/models/res_groups.py:36`). Name unique per privilege (`:39`).
- Implication graph: "implied" and "implied-by" many-to-many, transitive closure computed both ways (`:69-77`, `:246-270`).
- Carries access-right lines, record rules, menu and view visibility, API-key max duration.

Partner (`res.partner`)
- Individual or company (`is_company`), optional parent, address type (contact/invoice/delivery/other), tags, industry, salesperson, bank accounts, optional owning company, language, timezone, tax ID (`vat`), company registry. `B/models/res_partner.py:213-309`.
- Commercial partner = the company itself, or the nearest company ancestor for a person (`:515-520`). Stored and recursive.
- "Partner share" flag = true when the partner has no internal user (customer or portal) (`:443-448`).
- Lifecycle: create syncs commercial and address data with parent/children (`:927-948`, `:770-827`); archiving blocked while an active user is linked (`:856-870`); deletion blocked while any user is linked (`:950-964`).

Currency and rate
- Currency: unique 3-letter code, required symbol, positive rounding factor, active flag, display position. `B/models/res_currency.py:27-57`.
- Rate: dated, per currency, per root company (or global); one rate per day per currency per company; must be strictly positive. `:353-386`. Rates may only be recorded on top-level companies (`:473-477`).

Sequence: named/coded numbering series, optional company, two implementations - "standard" (fast, may skip numbers) and "no gap" (slower, consecutive). `B/models/ir_sequence.py:132`.
Attachment: file or URL linked to a model+record(+field), optional company, public flag, access token, checksum, size, mime type. `B/models/ir_attachment.py:453-478`.
Scheduled action: wraps one server action; interval, next/last run, priority, run-as user, failure count. `B/models/ir_cron.py:106-122`.
Server action: model, type (update/create/duplicate/code/webhook/multi), optional group restriction, usage flag (manual vs scheduled). `B/models/ir_actions.py:600-650`. History of code edits kept (100 per action). `:503-521`.

## C. Validations, automation, security model, multi-company

Validations / constraints (business meaning)
- Company: unique name; no archiving while active users use it as default company (`B/models/res_company.py:409-420`); branch currency must equal the root's, and is copied down when the root changes (`:426-433`, `:366-379`).
- User: default company must be among allowed companies while active (`res_users.py:501-509`); a user cannot be in two of internal/portal/public at once, including via implication (`:535-547`; also `res_groups.py:82-113`); at least one administrator must remain (`:550-554`); home action cannot be a record-dependent or reload action (`:512-533`); login unique.
- Partner: contacts must have a name (`res_partner.py:326`); no cyclic hierarchy (`:546`); a company-type partner that represents a company must carry that company (`:551-561`); barcode unique (`:647`); company-owner change refused if incompatible with linked users' companies (`:889-897`).
- Duplicate-detection hints (not blocking): same tax ID (with EU prefix variants) or same registry number computed as a warning field (`:451-488`).
- Currency: code unique; rounding positive; a currency used by a company cannot be deactivated (`res_currency.py:108-118`).
- Sequence: one sub-range per date span (`ir_sequence.py:301`).
- Attachment: no circular self-reference (`ir_attachment.py:494`).
- Config parameter: default system keys cannot be renamed (`ir_config_parameter.py:110-114`).

Security model
- Access is evaluated in two layers. (1) Table-level access lines per group and per operation (read/write/create/delete); a user is allowed if any of their groups (including implied) grants it; lines without a group apply to everyone; superuser bypasses all. `B/models/ir_model.py:2142-2196`. (2) Row-level rules: rules without groups are "global" and are ANDed together; rules with groups are ORed among the groups the user holds, and that result is ANDed with the global ones. `B/models/ir_rule.py:113-172`. Superuser skips rules (`:126`).
- Rule expressions can reference the current user, the set of currently enabled companies, and the current company (`ir_rule.py:38-52`).
- Group implication chain seeded in data (`B/security/base_groups.xml`): Administrator implies "Access Rights" manager, which implies internal User (`:26-40`); "Technical Features" is implied by User and Administrator (`:56-59`); Export-allowed and Contact-creation groups are implied by Administrator (`:61-73`); Portal and Public are separate, mutually exclusive user types (`:75-91`); Multi Companies and Multi Currencies are standalone marker groups (`:48-54`).
- Default groups for new internal users = internal-user group plus whatever is implied by the data record "Default access for new users" (`res_users.py:203-211`, `base_groups.xml:113-116`). Portal signup template user recorded through system parameter `base.template_portal_user_id` (`base_groups.xml:97-108`).
- Table-level access shipped (147 lines) `B/security/ir.model.access.csv`. Notable: partners - read for internal users, read for portal/public, full for Contact-creation group (`:73-76`); companies - read for everyone, full for Access Rights managers (`:42-45`); currencies and rates - read for everyone, full for Administrator (`:59-66`); sequences - read for users, full for Administrator (`:29-32`); attachments - full for internal users, none for portal/public (`:3-4`); crons and config parameters - Administrator only (`:5-7`, `:118`); server actions - Administrator only (`:107`).
- Self-service: a user can read and write only a short whitelist of own fields without admin rights (`res_users.py:176-200`, `:597-612`).
- Authentication protections: login cooldown after repeated failures per source address (`res_users.py:1215-1307`); API keys stored hashed, with expiry and group-driven maximum duration (`:1519-1720`, `res_groups.py:32`); session token built from listed fields (`:829-897`).
- Attachment access follows the linked record: public files readable by all; otherwise access to the parent record (and field) is required; unlinked files only for creator or admin (`ir_attachment.py:514-588`).

Record rules on base models (all in `B/security/base_security.xml`)
- Partner: visible when partner has no internal user, OR partner's company is an ancestor-or-equal of an enabled company, OR partner has no company (`:12-20`). Portal/public: read only own commercial entity tree (`:22-30`).
- Partner bank and currency rate: same "no company, or ancestor of an enabled company" test (`:56-66`).
- Company record itself: employees/portal/public see only companies currently enabled for them; Access Rights managers see all (`:105-131`, note: no hierarchy expansion here).
- Users: internal users always visible; shared users visible only when they share an enabled company (`:141-146`). Portal users see users of their own commercial entity (`:148-153`).
- Personal-scope rules: filters, defaults (own vs all for Administrator), view customisations, devices, API keys, user settings.
- NOT ruled by company in `base`: sequences, attachments, cron, config parameters, groups. Sequence lookup by code applies its own company filter instead (see multi-company).

Multi-company mechanics
- The "enabled companies" list travels with each request context; first entry is the current company. Validation: every id must be in the user's own allowed list unless running as superuser. If no context, current = user default company and enabled = all allowed companies. `O/environments.py:215-283`.
- User's allowed companies come from active companies linked to the user, cached (`res_users.py:726-730`).
- Switching current company inside code = `with_company` re-orders the list (`O/models.py:6021-6031`).
- Company-consistency check across relations: related records must share the company of the parent record or have none; property (company-dependent) links are checked against the owning company. `O/models.py:4003-4075`. Default relation-domain helper "no company, or ancestor of allowed company" is `O/models.py:169`.
- Company-dependent fields: the value is stored per company in one structured column, with a fallback default when a company has none (`O/fields.py:466-476,783-800`). In `base` the only such field is the partner barcode (`res_partner.py:309`). Commercial-field sync can propagate company-dependent values to every company (`res_partner.py:720-749`).
- Stored default values can be scoped by user and by company (`B/models/ir_default.py:24-26,81-175`).
- Sequence by code: picks a sequence of the current company, else a company-less one, ordered so the company one wins (`ir_sequence.py:279-292`); the sequence company field defaults to current company (`:150`).
- Currency rates always resolve against the root company of the given company; branches never hold rates (`res_currency.py:120-140,273-282`, `:473`). Branch inherits root currency.
- Branch helpers: which branches of a company are enabled for the user, whether all branches are selected (`res_company.py:436-470`).
- Automatic group toggles: adding a second allowed company gives a user the Multi Companies group; dropping to one removes it (`res_users.py:1352-1383`). More than one active currency grants Multi Currencies to all internal users; falling to one removes it (`res_currency.py:84-106`).

Automation and scheduling
- Cron engine: picks due jobs, runs the linked server action as the scheduler user, loops up to 10 times for batched work, treats "no progress + exception" as failure. Counters: minimum 5 consecutive failures and 7 days before automatic deactivation, then admin is notified. `B/models/ir_cron.py:30-38,458-520,571-623`. Job cannot be edited or deleted while running (`:697-720`).
- Shipped jobs: daily "auto-vacuum" (runs every method marked as cleanup across all models, random order, requires admin + cron context) and daily portal-user deletion (batch 50). `B/data/ir_cron_data.xml`, `B/models/ir_autovacuum.py:22-60`.
- Cleanup tasks in `base`: user login logs (`res_users.py:143`), expired API keys (`:1714`), file-store orphan files (`ir_attachment.py:191`), server action history beyond 100 (`ir_actions.py:520`), profiler data, device logs.
- Server action run: needs group membership if the action lists groups, otherwise write access on the model AND on the specific records; runs with elevated rights afterwards (`ir_actions.py:1151-1240`). Webhook type posts a JSON body containing model, record id, action name and selected fields (`:1040-1082`). Code type is syntax-checked on save (`:960`). Its log helper writes to the log table (`:1111-1123`).

Audit / logging
- Every standard model gets created-by/on and updated-by/on (`O/models.py:283-296`). The log table `ir.logging` has its own four audit columns (`B/models/ir_logging.py:22-25`).
- Per-login records (`res.users.log`, one row per login, own-row visibility rule) and device sessions (`res_users.py:134-152`, `B/models/res_device.py:16,174`).
- Partner merge writes a note of what was merged (`B/wizard/base_partner_merge.py:475`).
- Field-level change history is NOT in `base` (see A, `mail`).

Partner merge wizard (`B/wizard/base_partner_merge.py:412-473`)
- Limits: at most 3 contacts per merge; no parent/child pairs; not for contacts tied to more than one user; same email required unless the actor is the administrator. Re-points foreign keys and reference fields to the survivor, aligns linked users' company, merges bank accounts, then deletes the sources.

## D. Handoffs to other modules

- account: extends company, partner, currency, groups, attachments, bank accounts (module lists in F). Consumes: company currency, root-company rate lookup, partner commercial entity and tax ID, partner-bank uniqueness, sequence services, "parent-of enabled company" rule pattern (`account/security/account_security.xml:141-143`).
- sale / purchase / stock / mrp / point_of_sale / product: extend company and partner; use company-dependent partner fields, `address_get` to choose invoice/delivery addresses (`res_partner.py:1121-1159`), sequences by code, attachments on documents, and the server-action/cron primitives.
- mail: extends company, partner, users, groups, attachments, cron and server actions; supplies tracking and messaging; server-action types "send email/activity/followers" are added there (see the help text at `ir_actions.py:600-622`). Mail server records (`ir_mail_server.py`) live in `base`.
- base_automation: adds rule triggers and extends cron/server actions (F).
- Partner merge relies on other modules' relations discovered generically (`base_partner_merge.py:79-330`); it also has a "journal item" exclusion option for accounting data (`:72`).
- Localization modules (`l10n_*`) extend company/partner heavily; base auto-installs them by country (`res_company.py:207-244`).

## E. Configuration / defaults that change outcomes

- System parameters read by `base` code: `ir_attachment.location` (default file storage; alternative database), `base.login_cooldown_after` and `base.login_cooldown_duration`, `base.template_portal_user_id`, `base.default_max_email_size` (data default 10, `B/data/ir_config_parameter_data.xml`), `web.base.url` and its freeze flag, `report.url`, `report.print_delay`, `password.hashing.rounds`, `base.enable_programmatic_api_keys`, `base.programmatic_api_keys_limit`, `base.profiling_enabled_until`, `database.is_neutralized`.
- Seeded on database creation: database secret, uuid, creation date, base URL, cooldown 10 failures / 60 seconds (`B/models/ir_config_parameter.py:18-25`). The code fallback when the key is absent is 5 failures (`res_users.py:1301`). Both values are stated as read; which prevails depends on the parameter existing.
- Seed data: one main company "My Company" with USD, the technical superuser, an `admin` user, an inactive public user, an inactive portal template user (`B/data/res_company_data.xml`, `res_users_data.xml`, `base_groups.xml:97-105`). Most non-USD currencies ship inactive (`B/data/res_currency_data.xml`, 170 currency records).
- Noupdate: main company and the "Default access for new users" group are created once and preserved on upgrade (`res_company_data.xml`, `base_groups.xml:110-118`).
- Sequence implementation choice (standard vs no-gap), padding, step, per-date-range option.
- Currency rounding factor drives decimal places (`res_currency.py:163-169`).
- Company: currency (delegated to root), country (triggers localization), report layout/paper format/colours/fonts (`res_company.py:87-94`).
- Module install state: modules can auto-install when dependencies are met; upgrade/uninstall are wizard-driven (`ir_module.py:408-500,696-750`; wizards in `B/wizard/base_module_*.py`).
- Neutralization script (for copied/test databases): disables mail servers, all crons except auto-vacuum, and webhooks, sets the neutralized flag (`B/data/neutralize.sql`).
- Settings framework persists three kinds of choices - group membership, module installation, system parameters - from one screen (`res_config.py:178-350`).

## F. Effective extension path in Community (module names only; derived from the skeleton JSONs and cross-checked on samples)

res.company (120 modules besides base): account, account_check_printing, account_edi_proxy_client, account_payment_interco, account_peppol, account_peppol_response, auth_ldap, barcodes, base_vat, hr, hr_attendance, hr_expense, hr_holidays, hr_presence, hr_recruitment, hr_timesheet, lunch, mail, mass_mailing, mrp, mrp_account, mrp_subcontracting, mrp_subcontracting_dropshipping, partner_autocomplete, partnership, payment, point_of_sale, product, purchase, purchase_stock, resource, sale, sale_management, sale_stock, sms, sms_twilio, snailmail, stock, stock_account, stock_dropshipping, stock_landed_costs, stock_sms, web, website, website_sale, website_mass_mailing, sale_gelato, social_media, spreadsheet_account, project_timesheet_holidays, plus many `l10n_*` localization/e-invoicing modules (l10n_ar, l10n_au, l10n_br, l10n_ca, l10n_de, l10n_es*, l10n_fr*, l10n_in*, l10n_it_edi*, l10n_mx, l10n_nl, l10n_pl*, l10n_sa_edi*, l10n_se, and others).

res.users (53): auth_ldap, auth_oauth, auth_passkey, auth_password_policy, auth_signup, auth_timeout, auth_totp, auth_totp_mail, auth_totp_portal, base_import, base_setup, bus, calendar, contacts, crm, crm_livechat, digest, gamification, google_calendar, google_gmail, hr, hr_attendance, hr_gamification, hr_holidays, hr_homeworking, hr_recruitment, im_livechat, lunch, mail, mail_bot, mass_mailing, mass_mailing_sms, microsoft_account, microsoft_calendar, microsoft_outlook, phone_validation, point_of_sale, project, project_hr_skills, project_todo, resource, sale_stock, sales_team, stock, web, web_tour, web_unsplash, website, website_forum, website_profile, website_sale_wishlist, website_slides (plus test_uninstall).

res.partner (127): account, account_add_gln, account_edi_ubl_cii, account_peppol, auth_signup, base_address_extended, base_geolocalize, base_vat, bus, calendar, contacts, crm, delivery, event, google_address_autocomplete, hr, hr_holidays, im_livechat, loyalty, mail, mail_plugin, mass_mailing, mrp_subcontracting, partner_autocomplete, partnership, payment, phone_validation, point_of_sale, portal, pos_hr, pos_loyalty, pos_sale, pos_self_order, privacy_lookup, product, project, purchase, purchase_stock, sale, snailmail, stock, survey, web, website, website_crm_partner_assign, website_customer, website_partner, website_sale, website_slides, and many `l10n_*` modules.

res.groups (6): account, auth_timeout, bus, im_livechat, mail, website_slides.
res.currency (6): account, l10n_ar, l10n_cl, point_of_sale, product, spreadsheet. res.currency.rate: l10n_eg_edi_eta, spreadsheet.
ir.sequence: point_of_sale. ir.attachment (24): account, account_edi, mail, product, mrp, website, hr_expense, cloud_storage*, attachment_indexation, and others. ir.cron: base_automation, mail. ir.actions.server: base_automation, mail, sms, website. ir.rule: website. ir.config_parameter: analytic, auth_oauth, crm, mail, sale. res.partner.bank (17): account, base_iban, hr, l10n_* (ar, au, br, ch, hk, id, kh, mx, sg, th, us, vn), account_qr_code_emv, account_qr_code_sepa.
res.config.settings: 125 modules (one settings section per functional module).

## G. Not verified

- Field-by-field behaviour of the following was not read: UNKNOWN — EVIDENCE INSUFFICIENT for `ir_mail_server.py`, `ir_ui_view.py`, `ir_ui_menu.py`, `ir_qweb*.py`, `ir_asset.py`, `assetsbundle.py`, `ir_actions_report.py`, `res_lang.py`, `res_country.py`, `res_users_settings.py`, `res_device.py` internals, `ir_profile.py`, `ir_filters.py`, `ir_exports.py`, `ir_binary.py`, `ir_http.py`.
- Detailed cron scheduling internals (worker locking, `_process_jobs` loop, retry timing): UNKNOWN — EVIDENCE INSUFFICIENT beyond the pointers cited.
- Whether the cooldown effective in a live database is 10 or 5 failures depends on the stored parameter at runtime: UNKNOWN — EVIDENCE INSUFFICIENT (only static source read).
- Exact per-user effect of "Default access for new users" beyond its implied groups in other modules' data: UNKNOWN — EVIDENCE INSUFFICIENT.
- Behaviour of `check_company` on every downstream field (defined per module): UNKNOWN — EVIDENCE INSUFFICIENT for the full set.
- Completeness of the extension lists in F is derived from the skeleton JSON "inherit" entries plus spot checks; modules that extend via other mechanisms (delegation, mixins) may be missed: UNKNOWN — EVIDENCE INSUFFICIENT.
- Line pointers are for the stated revision only; runtime behaviour (registry loading, upgrade scripts in `odoo/upgrade`) was not exercised: UNKNOWN — EVIDENCE INSUFFICIENT.
- Complete list of all 147 access lines and all 37 rule references in base data views: only the models named above were reviewed.

