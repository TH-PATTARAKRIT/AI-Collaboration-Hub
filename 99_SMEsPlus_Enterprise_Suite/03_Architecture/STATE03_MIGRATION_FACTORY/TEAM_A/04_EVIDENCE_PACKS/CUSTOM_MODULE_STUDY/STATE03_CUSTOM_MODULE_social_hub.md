> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: social_hub

## 0. Header
- Module: social_hub
- License (confirmed in manifest): LGPL-3 (social_hub/__manifest__.py:40)
- Author (manifest): Lead Developer (Custom build for SOMCHART) (social_hub/__manifest__.py:38)
- Version (manifest): 19.0.1.0.2 (social_hub/__manifest__.py:4)
- Path: addons_Extramodule/addons/social_hub
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Stand-alone social media hub (no paid-edition dependency): connect Facebook Page, X (Twitter) and LinkedIn accounts with the company's own access token, publish posts immediately or on schedule to one or several accounts, pull back the feed and comments, and turn comments that contain buying keywords into CRM leads automatically or by button (manifest:6-22; models/social_hub_account.py:76-145; models/social_hub_post.py:45-99; models/social_hub_comment.py:60-108).
- A simulation mode (default on) generates fake posts/comments/ids without any external call, for trial use (models/social_hub_account.py:50-53, :80-81, :119-120, :129-130, :150-176).
- Keywords for lead detection are one setting stored as a system parameter, with a Thai/English default list (models/res_config_settings.py:10-15; models/social_hub_comment.py:51-57).

## 2. Attachment to CORE
- Depends declared: base, mail, crm (manifest:41).
- Core objects used: `mail.thread` / `mail.activity.mixin` (chatter and tracking on accounts and posts, models/social_hub_account.py:36; models/social_hub_post.py:15), `crm.lead` (created from comments, models/social_hub_comment.py:78-92; core fields `contact_name` and `type` at core:crm/models/crm_lead.py:175, :123-125), `res.config.settings` (models/res_config_settings.py:5-15), `ir.cron`.
- No core method overridden; only creation of `crm.lead` records with a lead type. Notes: core sets the default lead type by a group check (core:crm/models/crm_lead.py:125); this module forces type "lead" regardless of whether leads are enabled in the CRM settings (models/social_hub_comment.py:81). Effect on the CRM UI when leads are disabled is not tested. No ALTERS CORE CONTROL.

## 3. New objects, security, automation, external calls
- New models: platform registry (`social.hub.media`, three records loaded once: data/social_hub_media_data.xml:3-22), accounts (`social.hub.account`), composed posts (`social.hub.post`) with per-account results (`social.hub.live.post`), pulled posts (`social.hub.stream.post`) and comments (`social.hub.comment`).
- Security: two new groups, user and manager; user group implies the internal user group and manager implies user (security/social_hub_security.xml:3-11). ACL: users read media; read/write (no create/delete) accounts; full access on posts, results, stream posts and comments; managers full on all (security/ir.model.access.csv:2-13). No record rules and no company field on any model, so nothing is scoped by company (all accounts, posts and leads sit in one shared space; inference from model definitions). Menus have no group restriction (views/social_hub_menus.xml:9-36); non-members see the menu but hit access errors (inference). The comment in the security file says every internal user can use the module immediately (security/social_hub_security.xml:12-14), but the implied-group direction means the user group grants internal-user rights, not the reverse; membership must still be granted (inference from the group definition).
- Secret handling: the access token field is visible only to the system administrator group (models/social_hub_account.py:46-47) and is read with elevated access when calling the platform (models/api_clients.py:34). The Facebook client sends the token as a URL query parameter rather than a header (models/api_clients.py:103, :113, :135); other platforms use an authorization header (:168, :237). Error text from the platform (first 300 characters) is shown to the user and logged (models/api_clients.py:78, :85, :215, :302; models/social_hub_account.py:85-86).
- Automation: two cron jobs, publish scheduled posts every 15 minutes and create leads from candidate comments hourly (data/ir_cron_data.xml:4-23; models/social_hub_post.py:85-99; models/social_hub_comment.py:97-108). Cron runs with system rights, so it acts across all accounts irrespective of who created them.
- External calls: HTTPS calls to the Facebook Graph API (v19.0), X API v2 and LinkedIn v2 endpoints, timeout 15 seconds (models/api_clients.py:20, :92-94, :159-161, :228-230). Content sent: post text and optional link; data pulled: post text, counts, comment text and author names. Personal data of commenters is stored in comments and copied into lead descriptions (models/social_hub_comment.py:82-91). Retention/deletion policy: none in code.
- Business effect to note: publishing is not gated by an approval step; any user in the user group can post to connected accounts (models/social_hub_post.py:45-49; ACL row `access_social_hub_post_user`).

## 4. Odoo 19 compatibility
- Old-style `_sql_constraints` used in two models (models/social_hub_comment.py:35-38; models/social_hub_stream_post.py:26-29); not supported in Community 19 (core:odoo/orm/model_classes.py:162-163), so the two uniqueness rules are likely not created in the database (inference); duplicate handling for stream posts is done in code by lookup before create (models/social_hub_account.py:95-112).
- Manifest history notes two Odoo 19 fixes on group definitions (manifest:26-32); the module uses `_compute_display_name` per 17+ (models/social_hub_stream_post.py:38-43).
- Compute methods without `@api.depends` on non-stored fields (e.g. models/social_hub_account.py:60) are acceptable for non-stored; not checked further.
- `requests` library used directly (models/api_clients.py:16); presence in the deployed environment not checked.
- Manifest sets `application` true (manifest:54): appears as an app.

## 5. Custom-to-custom dependencies
- None declared.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether simulation mode is on or off in the deployed database (default on).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether current platform API versions and permissions still match the hard-coded endpoint versions.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether real tokens are stored in the deployed database.
- UNKNOWN — EVIDENCE INSUFFICIENT: how leads created automatically are assigned to sales teams or users (no assignment in this module).
