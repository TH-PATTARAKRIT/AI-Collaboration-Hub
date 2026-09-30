> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: date_range

## 0. Header
- Module: date_range
- License (confirmed in manifest): LGPL-3 (date_range/__manifest__.py:10)
- Author (manifest): ACSONE SA/NV, Odoo Community Association (OCA) (date_range/__manifest__.py:9)
- Version (manifest): 19.0.1.2.0 (date_range/__manifest__.py:6)
- Path: addons_Extramodule/addons_extra/date_range
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- A master list of named date periods (e.g. fiscal years, quarters, months, weeks) grouped by "date range type" (date_range/models/date_range.py:8-39; models/date_range_type.py:12-33).
- Business rules: end must not precede start; ranges of the same type in the same company must not overlap unless the type allows overlap (models/date_range.py:57-102; models/date_range_type.py:22-24).
- Period generator wizard: creates many consecutive periods at once from a start date, duration and unit, ending by end date or count; names are built from a prefix or from an admin-written naming expression (wizard/date_range_generator.py:16-85,116-139; expression evaluated at wizard/date_range_generator.py:174).
- Automatic generation: a daily scheduled job creates future periods for types configured with auto-generation settings (data/ir_cron_data.xml:3-13; models/date_range_type.py:127-150).
- Reusable search mixin: any model can inherit it to gain a "Period" filter in its search view that maps a chosen period to the model's date field (models/date_range_search_mixin.py:9-102). This module itself applies the mixin only to a test model (tests/models.py:7); no production model in this module inherits it.

## 2. Attachment to CORE
- Depends on web (manifest:12). Adds standalone models; no core model is inherited in production code.
- Menu placement: under core Technical menu base.menu_custom (views/date_range_view.xml:205-209; core:base/views/base_menus.xml:20), which core restricts to the developer-mode group.
- The mixin overrides get_view and get_views on models that opt in (date_range/models/date_range_search_mixin.py:63-102): ADDS after core - injects a technical Many2one search field "Period" into search views and relabels it. Core methods at core:base/models/ir_ui_view.py:3138 and 2905. Applies only to models that inherit the mixin. ALTERS CORE CONTROL: no.
- Imports domain helpers from odoo.osv.expression (mixin line 6); present in core 19 (core:osv/expression.py:139,158,159).

## 3. New objects, security, automation, external calls
- New models: date.range, date.range.type (persistent), date.range.generator (wizard), date.range.search.mixin (abstract).
- ACLs (security/ir.model.access.csv:2-6): employees read-only on date.range and date.range.type; system administrators full access; generator wizard system administrators only.
- Record rules (security/date_range_security.xml:3-16): both date.range and date.range.type visible when company is empty or among the user's allowed companies. date.range uses check_company auto (models/date_range.py:12). Extra company consistency check prevents changing a type's company if ranges of another company exist (models/date_range_type.py:79-97).
- Automation: cron "Auto-generate date ranges" daily, active by default (data/ir_cron_data.xml:3-13); failures per type are logged as warnings and skipped (models/date_range_type.py:139-150).
- External calls: none. Note: the naming expression is admin-authored text executed via core safe_eval (wizard/date_range_generator.py:174); write access is limited to system administrators by ACL.

## 4. Odoo 19 compatibility
- Class attribute _sql_constraints used on date.range (models/date_range.py:41-47) and date.range.type (models/date_range_type.py:71-77): core 19 logs that this attribute is no longer supported and expects models.Constraint (core:orm/model_classes.py:162-164). The name uniqueness rules per company are therefore probably not database-enforced (not executed). The overlap rule is a Python constraint and does not depend on this.
- The overlap constraint issues a raw database query through the cursor (models/date_range.py:74-96) - not judged further.
- Cron record uses state "code" and no numbercall (commented) (data/ir_cron_data.xml:7,11) - consistent with 19 style.
- Test file present under tests/ - not checked.

## 5. Custom-to-custom dependencies
- None declared (depends web only). A second copy exists at addons_Extramodule/addons/date_range; a recursive file comparison of the two copies reported no differences. The module l10n_th_withholding_tax_report (not in this assignment) lists date_range as a dependency (l10n_th_withholding_tax_report/__manifest__.py:14).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: which production models in the suite inherit date.range.search.mixin (none inside this module).
- UNKNOWN - EVIDENCE INSUFFICIENT: which of the two identical copies of date_range (addons or addons_extra) is the deployed one.
