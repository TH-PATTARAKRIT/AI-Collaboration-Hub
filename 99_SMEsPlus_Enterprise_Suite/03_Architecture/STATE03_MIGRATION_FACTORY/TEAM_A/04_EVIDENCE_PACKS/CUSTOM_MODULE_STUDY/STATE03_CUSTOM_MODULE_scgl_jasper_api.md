> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_jasper_api

Module: scgl_jasper_api
License (confirmed in manifest): LGPL-3 (scgl_jasper_api/__manifest__.py:19)
Author (manifest): SCG Legacy Co., Ltd. (scgl_jasper_api/__manifest__.py:16)
Version (manifest): 19.0.1.0.0 (scgl_jasper_api/__manifest__.py:3)
Path: addons_Extramodule/addons/scgl_jasper_api
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Publishes web addresses that an external JasperReports server can call to fetch pictures (product, partner, employee, signature) for printed reports (scgl_jasper_api/controllers/main.py:55-84; scgl_jasper_api/__manifest__.py:5-14).
- Stores a user signature image, either as a record per user (new model) or as a picture field on the user (scgl_jasper_api/models/scgl_signature_image.py:4-31; scgl_jasper_api/models/res_users.py:9-12).
- Intends to link checker / approver / authorizer signatures to a purchase order so the printed PO shows who signed (scgl_jasper_api/models/purchase_order.py:11-28, 34-62).

## 2. Attachment to CORE
- purchase.order (core:purchase): ADDS three signature links and three onchange helpers (scgl_jasper_api/models/purchase_order.py:11-62). Adds behavior only when the user, level-1 or level-2 approver fields change; no core method is overridden.
- res.users (core:base): ADDS field `signature_image` (scgl_jasper_api/models/res_users.py:9-12), shown after the core email-signature field in both the admin user form and the self-service preferences form (scgl_jasper_api/views/res_users_view.xml:9-11, 20-22). The self-service form is a core view (core:base/views/res_users_views.xml:403), so users can maintain their own picture; whether this field is self-writable at the ORM level is UNKNOWN.
- Routes: ADDS public HTTP routes (section 3). No core route is replaced.
- Nothing in this module BLOCKS/ALTERS posting, lock dates, valuation, numbering. Security note: it exposes data to unauthenticated callers (see section 3) - ALTERS CORE CONTROL (access to record data via public route, bypassing record rules by elevated read).

## 3. New objects, security, automation, external calls
- New model scgl.signature.image: user, related partner, picture, filename, active flag, note, computed name (scgl_jasper_api/models/scgl_signature_image.py:10-38). ACL: internal users read-only; system administrators full (scgl_jasper_api/security/ir.model.access.csv:2-3). No record rules, no company field (single global set), no cron.
- Public route 1: /pictures/<model>/<id>/<field> for a whitelist of five models (scgl_jasper_api/controllers/main.py:26-32, 57-84). Auth is public, read under elevated rights (line 75), and the field name is taken from the URL with no check that it is a picture field, and no token. Any field value on a whitelisted record may be returned as an image response.
- Public route 2: /pictures/scgl.signature.image/<user_id>/<token> (scgl_jasper_api/controllers/main.py:97-144). Guarded by a single shared token that is hard-coded as a constant in source (scgl_jasper_api/controllers/main.py:15). Token value not reproduced here. It reads the picture field on the user, not the new model (line 132-133). Comparison is a plain string match (line 112).
- Missing picture returns a 1x1 transparent PNG; errors are logged (scgl_jasper_api/controllers/main.py:35-47, 140-144).
- External calls: none outbound. The JasperReports server calls IN to these routes; the report query builds the address (comments at scgl_jasper_api/controllers/main.py:93-95). Server host names are not configured in this module.
- Signature list/form views exist but are not loaded (commented out in manifest data: scgl_jasper_api/__manifest__.py:23; file scgl_jasper_api/views/scgl_signature_image_views.xml).

## 4. Odoo 19 compatibility
- Mismatch: purchase.order domains and searches use a `role` field on scgl.signature.image (scgl_jasper_api/models/purchase_order.py:14, 21, 27, 40, 50, 60); the model has no such field (scgl_jasper_api/models/scgl_signature_image.py:10-38). Lookups by role would fail at search time.
- Mismatch: onchange helpers reference `level1_user_id` / `level2_user_id` (scgl_jasper_api/models/purchase_order.py:44, 54); these do not exist in Community purchase (grep of core:purchase and core:base found none). They are defined by a sibling non-listed module (purchase_request_level_approve_po/models/purchase_order.py:61), which this manifest does not declare as a dependency.
- Mismatch: manifest text lists routes /pur/po/signature/checker|approver|authorizer/... (scgl_jasper_api/__manifest__.py:9-11) but no such route exists in the controller (scgl_jasper_api/controllers/main.py:57-104).
- Mismatch: `_sql_constraints` is used for the one-signature-per-user rule (scgl_jasper_api/models/scgl_signature_image.py:46-52). Community 19 logs it as no longer supported and asks for models.Constraint (core:odoo/orm/model_classes.py:162-164), so uniqueness is likely not enforced.
- Views inherit core `base.view_users_form` and `base.view_users_form_simple_modif`, both present (core:base/views/res_users_views.xml:96, 403); field `signature` present (core:base/models/res_users.py:226).

## 5. Custom-to-custom dependencies
- Declared: none of the scgl_* family (scgl_jasper_api/__manifest__.py:20).
- Undeclared, by field usage: a purchase-request approval module supplying level1_user_id / level2_user_id (see section 4). Its license and code were not studied.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the Jasper report SQL in production uses either route and with what hosts (report definitions are outside this module).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the shared token has been rotated or is duplicated in report files (out of scope; value deliberately not recorded).
- UNKNOWN - EVIDENCE INSUFFICIENT: how the signature-image records get a role or are populated, since the field and the view are absent/unloaded.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the module installs on a database lacking the approval fields (not run).
