> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: auto_database_backup

## 0. Header
- Module: auto_database_backup
- License (confirmed in manifest): LGPL-3 (auto_database_backup/__manifest__.py:48)
- Author (manifest): Cybrosys Techno Solutions (auto_database_backup/__manifest__.py:32)
- Version (manifest): 19.0.1.0.0 (auto_database_backup/__manifest__.py:25); the display name still says "Odoo18" (manifest:22-23)
- Path: addons_Extramodule/addons_extra/auto_database_backup
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Scheduled, automatic full backup of a chosen database (data plus attached-file storage) to a chosen destination, with optional retention clean-up and success/failure email notice (auto_database_backup/models/db_backup_configure.py:59-65,616-1132).
- WHERE BACKUPS GO - one configuration record chooses exactly one destination (models/db_backup_configure.py:90-99):
  1. Local storage: a folder path on the ERP server itself (backup_path field :121; local branch :632-667).
  2. FTP server (plain FTP client, host/port/user/password/path fields :131-138; branch :669-716).
  3. SFTP server (branch :718-767; host-key policy accepts unknown servers automatically, :574 and :720).
  4. Google Drive (OAuth consent, upload to a folder by id; branch :769-848; endpoints :53-56,791-826).
  5. Dropbox (client id/secret + refresh token flow; branch :850-898; wizard for the authorization code, wizard/dropbox_auth_code.py:28-58).
  6. Microsoft OneDrive (via Microsoft Graph; branch :899-955; endpoints :53,376,428,465).
  7. Nextcloud (branch :956-1050) - the client libraries for this path are commented out of the imports (models/db_backup_configure.py:28,36; manifest external list :44-46), so this destination refers to names that are not defined in the file and would fail at run time; errors in each branch are caught and stored in the exception field (e.g. :1004-1010).
  8. Amazon S3 bucket/folder (branch :1051-1132; connection test :246-286).
- Backup content: database dump; in "zip" format also a copy of the file storage and a manifest listing installed modules and versions (models/db_backup_configure.py:1134-1195); "dump" format is the database dump only, held in memory before writing (:1171-1177).
- Retention: "Remove Old Backups" with a number field labelled as days but used in local code as a count of files to keep (models/db_backup_configure.py:157-161,645-650).
- Notification: optional email to a chosen user on success or failure (models/db_backup_configure.py:164-167; data/mail_template_data.xml:5-9,111-115).
- Scheduling: each configuration creates its own scheduled job with daily/weekly/monthly interval and a start time (models/db_backup_configure.py:1197-1250; static cron file is fully commented out, data/ir_cron_data.xml:5-30).

## 2. Attachment to CORE
- Depends on base and mail (manifest:36); uses mail.thread and mail.activity.mixin on its own model (models/db_backup_configure.py:64).
- Uses core database services directly: database list and master-password check (core:service/db.py:440 list_dbs, core:service/db.py:60 check_super), PostgreSQL tool lookup (core:tools/misc.py:153,163), zip helper (core:tools/osutil.py:54). It re-implements the dump logic of core rather than calling core dump_db (core:service/db.py:282) and its own manifest builder duplicates core:service/db.py:266.
- Core models used: ir.cron (created/updated per configuration, models/db_backup_configure.py:1216-1250), ir.model, mail.template, res.users.
- No core method is overridden. ADDS only. ALTERS CORE CONTROL: yes in effect - it copies the whole database and file storage out of the server boundary to third-party or remote locations by a scheduled job running as the technical superuser account (models/db_backup_configure.py:1239), bypassing the core database-manager route that requires the master password interactively; the master password is instead stored in a field on the record and re-checked by the core function on save (models/db_backup_configure.py:83-84,559-568).
- Menu: under core Technical menu base.menu_custom (views/db_backup_configure_views.xml:315-319; core:base/views/base_menus.xml:20, developer mode group).

## 3. New objects, security, automation, external calls
- New models: db.backup.configure (persistent, chatter-enabled), dropbox.auth.code (transient wizard).
- Sensitive data stored in database fields on the configuration record: the Odoo database master password; FTP, SFTP and Nextcloud passwords; Dropbox client secret and refresh token; OneDrive and Google Drive client secret, access and refresh tokens; AWS access and secret keys (a credential-like value exists at each of models/db_backup_configure.py:83,128,136,141-146,177-186,195-211,226,233-236; values not reproduced). The form masks some inputs (views/db_backup_configure_views.xml:33,62,78,89,95-96,104,109) but this is display-level only; fields carry no group restriction and chatter tracking is only on selected fields.
- ACLs (security/ir.model.access.csv:2-3): ALL internal users (base.group_user) have read/write/create/delete on db.backup.configure and on the Dropbox wizard, while the only menu is in the developer/technical area. There is no record rule and no company scoping. Consequence: any internal user with RPC/API access could read or change backup configurations, including credentials and destinations (access control is not restricted to administrators in this module's own security file).
- Public callbacks (controllers/auto_database_backup.py:29-43,45-54): two HTTP routes (OneDrive, Google Drive) with no login requirement that, given a request state naming a configuration id, use elevated rights to exchange the returned authorization code for tokens, mark the configuration active and redirect to a URL taken from the request state. Effect: unauthenticated callers can trigger token exchange attempts and activation for any configuration id, and an open redirect target is accepted.
- Automation: one scheduled job per configuration, executed as the technical superuser, running the backup routine for that configuration id (models/db_backup_configure.py:1237-1239). Cron is created on create/write when frequency, start time or active changes (models/db_backup_configure.py:1197-1214).
- EXTERNAL CALLS (business level): outbound to whichever destination is configured (FTP/SFTP host, Google Drive API, Dropbox, Microsoft Graph, Nextcloud host, AWS S3) and to the token endpoints of Google and Microsoft. The full database dump plus file storage leaves the server. FTP carries data and credentials unencrypted (plain FTP client, models/db_backup_configure.py:669-716).

## 4. Odoo 19 compatibility
- Class attribute _sql_constraints on db.backup.configure (models/db_backup_configure.py:117-119) is reported unsupported by core 19 (core:orm/model_classes.py:162-164); uniqueness of backup prefix probably not enforced in the database.
- create is declared with the single-record decorator and takes one dict (models/db_backup_configure.py:1196-1200); core 19 create takes a list of dicts (core:orm/decorators.py:357-372 documents both forms). Multi-record create calls not verified.
- Core helpers used exist in 19: list_dbs, check_super, find_pg_tool, exec_pg_environ, zip_dir (pointers above).
- Nextcloud imports commented out but referenced (models/db_backup_configure.py:28,36 vs :294,969-970) - would raise name errors.
- The zip-format path copies the entire file storage into a temporary directory before zipping (models/db_backup_configure.py:1150-1153): disk space demand equals database dump plus file storage.
- Module manifest lists external Python libraries dropbox, boto3, paramiko (manifest:44-46); module import fails at load if they are missing.
- Retention wording versus behaviour mismatch: field is described as days (models/db_backup_configure.py:159-161) but local retention keeps the newest N files (:645-650); other destinations have "Remove by backup counts" comments at :700,742,819,879,936,992,1081.

## 5. Custom-to-custom dependencies
- None declared.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: which backup destination (if any) is configured or intended in the SMEsPlus deployment; no configuration records or data were read.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether backups are encrypted at rest at the destination (no encryption step found in the module code read).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether any Google/Microsoft/Dropbox application registrations exist for the deployment.
- UNKNOWN - EVIDENCE INSUFFICIENT: restore procedure (this module has no restore code).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the ACL breadth (all internal users) is mitigated elsewhere (e.g. by another module's rules).
