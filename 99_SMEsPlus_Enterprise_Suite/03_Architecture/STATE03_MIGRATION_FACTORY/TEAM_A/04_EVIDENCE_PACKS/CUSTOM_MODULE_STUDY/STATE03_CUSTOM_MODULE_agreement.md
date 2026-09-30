> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: agreement

## 0. Header
- Module: agreement
- License (confirmed in manifest): AGPL-3 (addons/agreement/__manifest__.py:13)
- Author (manifest): Akretion, Yves Goldberg (Ygol Internetwork), Odoo Community Association (OCA) (addons/agreement/__manifest__.py:9-11)
- Version (manifest): 19.0.1.0.0 (addons/agreement/__manifest__.py:7)
- Path: addons_Extramodule/addons/agreement
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- A lightweight register of commercial agreements (contracts/frameworks) per partner, with code, name, partner, agreement type, sale-or-purchase domain, signature/start/end dates, active flag, company, and a "template" flag (agreement/models/agreement.py:9-48).
- Chatter and activities are available on the agreement (agreement/models/agreement.py:11); key fields are change-tracked (agreement.py:13-14,20,41,46-48).
- Optional agreement types classify agreements and pre-set the sale/purchase domain (agreement/models/agreement_type.py:8-17; agreement.py:57-63).
- Display name is shown as "[code] name" (agreement.py:65-67). Copying an agreement auto-suffixes the code with "(copy)" because code is mandatory (agreement.py:77-83).
- No link to sale orders, purchase orders or invoices exists in this module (no such fields in models/agreement.py).

## 2. Attachment to CORE
- Depends on mail (manifest:14): uses mail.thread and mail.activity.mixin (agreement/models/agreement.py:11).
- References core res.partner (top-level partners only) and res.company (agreement.py:15-26). No inheritance of any core model; no core method overridden. ALTERS CORE CONTROL: none.
- The partner field is filtered to partners without a parent (agreement.py:19), i.e. companies/top-level contacts only.

## 3. New objects, security, automation, external calls
- New models: agreement (agreement.py:9), agreement.type (agreement_type.py:8).
- Security groups (security/agreement_security.xml:22-28): "Use agreement type" and "Use agreement template" (feature-toggle groups that show the type and template fields in the form: views/agreement.xml:34-42). The XML comment states groups are not assigned to users by XML (agreement_security.xml:30-34).
- ACLs (security/ir.model.access.csv:2-5): all internal employees read-only on agreement and agreement.type; only the system administrators group has full create/write/delete.
- Record rule (agreement_security.xml:11-17): agreement visible when company empty or within the user's allowed companies. Company scoping applies to agreement only; agreement.type is not company scoped.
- Menus: root "Agreements" with sub menus Agreements, Reporting (empty container), Settings (empty container) (views/agreement_menu.xml:2-27). The agreement.type action exists (views/agreement_type.xml:71-73) but no menu item referencing it was found in views (grep of views/agreement_menu.xml and agreement_type.xml).
- Automation: none. External calls: none. Demo data exists (demo/demo.xml, manifest:22).
- Uniqueness intent: unique(code, partner, company) with message "This agreement code already exists for this partner!" (agreement.py:69-75) - see section 4.

## 4. Odoo 19 compatibility
- Class attribute _sql_constraints on agreement (agreement/models/agreement.py:69-75). In the Community 19 tree this attribute triggers a warning that it is no longer supported and models.Constraint should be used (core:orm/model_classes.py:162-164). Business consequence: the uniqueness rule on code+partner+company is probably NOT enforced in the database under Odoo 19 (based on core warning text; runtime behaviour not executed).
- self.env._ used (agreement.py:53,82): present in core 19 (core:orm/environments.py:315).
- _compute_display_name override (agreement.py:65): standard in 19 (not verified against core file beyond naming).
- Other references (mail.thread, mail.activity.mixin, chatter tag, web_ribbon widget core:web/static/src/views/widgets/ribbon/ribbon.js:71) exist.

## 5. Custom-to-custom dependencies
- None declared.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether any other custom module in the suite links documents to agreement records (out of scope of this module).
- UNKNOWN - EVIDENCE INSUFFICIENT: how the agreement type list is meant to be reached in the UI (no menu found).
- UNKNOWN - EVIDENCE INSUFFICIENT: runtime effect of the unsupported _sql_constraints attribute (not executed).
