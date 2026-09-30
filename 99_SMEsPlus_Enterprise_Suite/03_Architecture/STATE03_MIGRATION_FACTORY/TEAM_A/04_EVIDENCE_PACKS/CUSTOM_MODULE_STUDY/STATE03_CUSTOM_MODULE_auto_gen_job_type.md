> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: auto_gen_job_type

## 0. Header
- Module: auto_gen_job_type
- License (confirmed in manifest): LGPL-3 (auto_gen_job_type/__manifest__.py:90)
- Author (manifest): BHPRO (auto_gen_job_type/__manifest__.py:88)
- Version (manifest): 19.0.1.7.0 (auto_gen_job_type/__manifest__.py:4)
- Path: addons_Extramodule/addons/auto_gen_job_type
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Gives every confirmed sales order a business reference code built from the customer's brand code, the order's job type code and a running number, for example in the style Brand-JobType-00001 (manifest description, auto_gen_job_type/__manifest__.py:6-27; models/auto_gen_config.py:22-233).
- Format is configurable per company: up to five ordered positions chosen from brand, job type, running number, year (4 or 2 digits), month, day or none; separator, digit padding (1 to 12), prefix and suffix; a live preview is computed (models/auto_gen_config.py:10-19,49-122,194-233,238-249). Only one active configuration per company is allowed (models/auto_gen_config.py:133-148).
- Running numbers are kept per combination of company, customer, brand and job type in a counter table, so each combination counts independently (models/auto_gen_counter.py:6-72,77-119).
- Brand fallback: if the customer has no brand of its own but is flagged as a head-office brand, the first brand registered under it is used (models/sale_order.py:50-73; description manifest:29-35).
- Audit history: each confirmation adds a history row (version, code, customer, brand, job type, running number, format snapshot, user, time, note); confirming an order that already has a code keeps the code but bumps the version and records a history row (models/sale_order.py:78-104,122-263; models/auto_gen_history.py:5-94).
- Cancel with reason: cancelling a single order that has a code opens a pop-up requiring a reason (max 255 characters), stores it in the history as a "cancelled" event, then proceeds with the standard cancellation (models/sale_order.py:320-363; wizards/auto_gen_cancel_wizard.py:9-147).
- Manual "Generate Code" button on draft/sent orders re-creates the code without bumping the version or history (models/sale_order.py:280-301; views/sale_order_views.xml:17-25).
- Menus: Sales > Configuration > Auto Gen Job Type with configuration and counter screens (views/menu_views.xml:5-22).

## 2. Attachment to CORE
- Depends on sale_management, bh_parent_company, sale_job_type (manifest:91-95). Core object extended: sale.order (models/sale_order.py:7). Core views inherited: sale.view_order_form (core:sale/views/sale_order_views.xml:252), sale.view_order_tree (:179), sale.view_quotation_tree (:206); menu sale.menu_sale_config (core:sale/views/sale_menus.xml:97).
- Override of core action_confirm (core:sale/models/sale_order.py:1168): ADDS BEFORE core. It generates or bumps the code for each order, then calls core (models/sale_order.py:109-120). ALTERS CORE CONTROL: the code generation raises a user error when brand, job type or customer required by the configured format is missing, or when a brand/job type has no code, which BLOCKS confirmation until fixed (models/sale_order.py:172-208,213-222; auto_gen_counter.py:84-88). It also applies only when the active configuration's "generate on confirm" flag is on (models/sale_order.py:143-145).
- Override of core action_cancel (core:sale/models/sale_order.py:1326): REPLACES the direct cancel for a single order that carries a code by first returning a reason wizard; other cases call core directly (models/sale_order.py:331-342). Core action_cancel raises an error for locked orders (core:sale/models/sale_order.py:1328); after the wizard, core is called with a context flag to skip the wizard (wizards/auto_gen_cancel_wizard.py:145-147). ALTERS CORE CONTROL: adds a mandatory reason step in front of cancellation (bulk cancels of several orders skip the step).
- Fields brand_id, job_type_id (on sale.order), partner fields is_hq_brand / hq_brand_ids and models bh.brand and sale.job.type come from the other two custom modules, not from core (grep of core sale/base found none).

## 3. New objects, security, automation, external calls
- New models: auto.gen.job.type.config, auto.gen.job.type.counter, auto.gen.job.type.history, auto.gen.job.type.cancel.wizard (transient). New sale.order fields: auto_gen_code, auto_gen_version, history one2many and count (models/sale_order.py:10-45).
- ACLs (security/ir.model.access.csv:2-13): salesperson group read-only on configuration, read/write/create on counter and history (no delete), full on the cancel wizard; sales manager group full on all; system administrators full on all. No record rules; company scoping only via a company field on configuration and counter (models/auto_gen_config.py:41-46; models/auto_gen_counter.py:19-25), and lookups use the current company (models/sale_order.py:143; models/auto_gen_counter.py:89-95). The history model has no company field.
- Note: the history model is described as an immutable log (models/auto_gen_history.py:6) but salespeople hold write permission on it (csv:8) and the history fields are read-only in the model definition only; whether the view blocks edits was not verified.
- Sudo use: configuration lookup, counter increments and history writes are done with elevated rights (models/sale_order.py:93,143,223,252,349), so salespeople need not hold rights on them.
- Data: default configuration record (data/auto_gen_config_data.xml:6-12). A configuration is auto-created if none is active (models/auto_gen_config.py:184-188).
- Migration script for 19.0.1.6.0 drops an old uniqueness rule on history and adds the event type column (migrations/19.0.1.6.0/pre-migrate.py:13-40; description at file top). Uses direct database statements (not reproduced).
- Concurrency: counter increments use a database row lock to avoid duplicate numbers (models/auto_gen_counter.py:105-117).
- Manual regenerate temporarily changes the shared configuration flag "overwrite_existing" and restores it afterwards (models/sale_order.py:291-300), a shared-record write that other users' transactions could observe.
- Automation: none scheduled. External calls: none.

## 4. Odoo 19 compatibility
- _sql_constraints on the counter (models/auto_gen_counter.py:58-62) is unsupported in core 19 (core:orm/model_classes.py:162-164); uniqueness of company+customer+brand+job type is probably not DB-enforced; concurrent first-time creation could create duplicate counters (not executed). The history model sets an empty list (models/auto_gen_history.py:100).
- name_get override on the history model (models/auto_gen_history.py:102-107): name_get not present in core 19 base models (grep core:base/models earlier); likely inactive, so the record label falls back to the record name field.
- Counter redefines display_name as a stored computed field with its own compute (models/auto_gen_counter.py:53-56,64-72): behaviour under core 19's display_name handling not verified.
- References to models/fields from other custom modules are not verified here (bh.brand, sale.job.type, sale.order.brand_id, job_type_id).
- Core action names and view ids used exist (pointers in section 2).
- Concurrency: the running number is issued using the current user company (models/auto_gen_counter.py:89) rather than the order's company; for multi-company use this could mix counters (not verified).

## 5. Custom-to-custom dependencies
- bh_parent_company (brand master) and sale_job_type (job type master) - manifest:91-95; both exist as folders under addons_Extramodule/addons (directory listing); not studied here.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: definitions of brand_id, job_type_id, is_hq_brand, hq_brand_ids (in other custom modules).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the history view forbids edits by salespeople.
- UNKNOWN - EVIDENCE INSUFFICIENT: how bulk/automated (non-UI) cancellations of coded orders are meant to be audited (they bypass the reason step).
- UNKNOWN - EVIDENCE INSUFFICIENT: printed or downstream use of the generated code (no report inheritance found in this module).
