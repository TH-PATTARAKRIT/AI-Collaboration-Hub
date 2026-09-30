> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: tracking_history

## 0. Header
- Module: tracking_history
- License (confirmed in manifest): LGPL-3 (tracking_history/__manifest__.py:5)
- Author (manifest): MPP, SMEsPlus Co.,Ltd (tracking_history/__manifest__.py:14)
- Version (manifest): 19.0.1.1 (tracking_history/__manifest__.py:4)
- Path: addons_Extramodule/addons_extra/tracking_history
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Audit-style lookup of chatter messages by person: a wizard asks for an author, a date range and one or more models, and then opens a list of the messages that person wrote in that period (manifest:6-12; wizards/log_note_history_wizard.py:5-40; wizards/log_note_history_wizard_view.xml:4-24).
- Adds a stored "Module" label on every chatter message, derived from the model the message belongs to, with fixed business names for sales, purchase, purchase request, product, contact, users, companies, employees, lot/serial, inventory, accounting and dashboards, and a capitalised prefix for anything else (models/mail_message.py:7-49).
- Menu placement: "Tracking History" under the Technical section of the Email menu (wizards/log_note_history_wizard_view.xml:35-36). The Technical root menu is restricted to developer-mode users in core (core:base/views/base_menus.xml:20 shows the root with the debug-mode group), so the entry is visible only in that mode (inference through inheritance of parent visibility). Menu item itself has no own group.
- Nothing is hidden by this module.

## 2. Attachment to CORE
- Depends declared: mail (manifest:17-19).
- Core objects extended: `mail.message` (new stored field, models/mail_message.py:4-7) and the core message form (views/mail_message_views.xml:4-11; core:mail/views/mail_message_views.xml:21), menu `mail.mail_menu_technical` (core:mail/views/mail_menus.xml:106).
- Field `module_name` is a stored compute triggered by `model` (models/mail_message.py:9-10): ADDS. No core method overridden. No ALTERS CORE CONTROL.
- The results are shown through the core message model, whose search applies the per-document access checks of core (core:mail/models/mail_message.py:317, :453), so the list is intended to be limited to messages of documents the viewer may read (inference from core; not tested here).
- Model list used for filtering: only the FIRST selected model's prefix is used, and the filter is "model name starts with that prefix followed by a dot" (wizards/log_note_history_wizard.py:16-28). Other selected models are ignored, and choosing one model reveals all models of the same application prefix.

## 3. New objects, security, automation, external calls
- New models: wizard `log.note.history.wizard` (transient) and a report model `log.note.history.report` declared without a database view or table creation code (reports/log_note_history_report.py:4-16, `_auto` false).
- ACL: both models, all internal users, full read/write/create/delete (security/ir.model.access.csv:2-3). No record rules, no groups, no company scoping.
- Data-volume note: the stored label is recomputed for all existing messages on install (dependency on the model field, models/mail_message.py:9); size not known.
- Automation: none. External calls: none.

## 4. Odoo 19 compatibility
- The wizard returns an action on `mail.message` but points it at three views built for the other model `log.note.history.report` (wizards/log_note_history_wizard.py:29-38 vs views/log_note_history_report_views.xml:6-8, :23-26, :48-51). The fields those views use (author as text, subject, body, module label, model, date, related id) do not match `mail.message` field types (author is a partner link on the core model). The view/model mismatch may fail when opened; not runtime-tested.
- The report model has no `init` and no table creation for the non-auto model (reports/log_note_history_report.py:4-16); it cannot be read as a database-backed model unless created elsewhere. Marked risk.
- `search_view_id` is passed as a list (wizards/log_note_history_wizard.py:35), while an action expects an id/pair; behaviour not verified.
- Core references exist in Community 19: message form, technical menu, message model (pointers above).

## 5. Custom-to-custom dependencies
- None declared. The label logic mentions `purchase.request` (models/mail_message.py:21-24), a non-core model, only by name.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the wizard works end to end in Odoo 19 (view/model mismatch).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether users who can open the wizard can see messages outside their document access (depends on core message search behaviour, not tested).
