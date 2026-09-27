# G01 PLATFORM_BASE — Module `web` — LANE A PASS-2 (Depth / Gap Closure, DELTA)

| Item | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Slot | T5 |
| Group / Module | G01 PLATFORM_BASE / `web` |
| Parent packet | `99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_WEB_LANE_A_PASS1_20260927.md` |
| Parent sha256 | `a06cace5e4366454549c9641b8397c00286dd5f3e2b38b3447d8ddfba069a708` (unmodified) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Date | 2026-09-27 |
| Status | **LANE A PASS-2 COMPLETE — HANDOFF TO A1 (DELTA)** |

This is a delta packet. It adds to PASS-1 and does not restate it. Everything here is static source reading. Source presence does not show runtime reachability, and no configuration or deployment state was observed. No Formal Coverage is claimed and no QIDs are answered. Line numbers are approximate pointers.

## 1. Gap Closure Table

| Gap (brief / PASS-1 id) | Result | Pointer |
|---|---|---|
| (a) Server-side `group_allow_export` enforcement for CSV/XLSX (PASS-1 G-2, #21) | **CLOSED** | F-1..F-4; `odoo/orm/models.py` ~L880-891 |
| (b) DB manager: master password, list_db, dbfilter (PASS-1 G-3, #17) | **CLOSED** (static) | F-5..F-11 |
| (c) `/web/become` full read (PASS-1 #18) | **CLOSED** | F-12..F-13 |
| (d) Public/no-login content, image and logo routes: access check after sudo (PASS-1 #16, #19) | **CLOSED** for the routes in scope; **NARROWED** for downstream overrides (NG-3) | F-14..F-21 |

## 2. Evidence Pointer Table (blobs are git blob SHA-1 of the file as fetched at the anchor)

| Path | git blob SHA-1 | Used for |
|---|---|---|
| `addons/web/controllers/export.py` | cb750f193c5548fe70a01422d644c66805a20e69 | Full export flow (~L553-638), CSV/XLSX routes (~L640, ~L688) |
| `addons/web/controllers/json.py` | 1d1b408ea56cd92249b743012dd6eb039caba38d | Export-group gate on `/json` (~L69) |
| `addons/web/controllers/pivot.py` | a687d2d1dbd443c0b49c2e1b259a2dd2c9767bb1 | Pivot XLSX export (~L16) |
| `addons/web/controllers/database.py` | 434b915ceb3a935c1fdbee248d4a4ed7a8533b48 | DB manager routes (~L59-185) |
| `addons/web/controllers/home.py` | 292aaa75a2c35b71acb3c97488a6dc2c96309c9f | Login DB list / list_db flag (~L122-148), `/web/become` (~L162-171) |
| `addons/web/controllers/binary.py` | 7b7b84f771eeb5a0f096500f7530a48c956f41b1 | Content, image, asset, filestore, logo and font routes |
| `odoo/orm/models.py` | 11f50c4e0b676fbb4b8a45e9703326946348ff98 | `export_data` gate (~L880-891); default `_can_return_content` (~L5854); field-group check (~L3375-3402); `check_access` (~L4106) |
| `odoo/orm/environments.py` | ec6b89fc3b752d3c52eb220e95437dbd4db134fd | `is_admin` / `is_system` semantics (~L178-190) |
| `odoo/addons/base/models/res_users.py` | 9d42d77ae8ec19028c99b3c668294569ded3a86a | `_is_system` / `_is_admin` group mapping (~L1177-1183) |
| `odoo/addons/base/models/ir_model.py` | ca0c48b566843ece9948c8c5e7f759714a3faf8e | Negative search: no export-group reference |
| `odoo/service/model.py` | 83af887271543fb27671754ffa61d92ea7949629 | Negative search: no export-specific gate |
| `odoo/service/db.py` | 63c314a72de738d044e542e32bc045c21f987531 | list_db decorator (~L46), master-password check (~L60), drop/list/dispatch (~L233, ~L440-527) |
| `odoo/http.py` | ebfc2ac8d268a45aaf4b8cde8c9ce8b480d58dbb | `db_list` / `db_filter` (~L372-418), `dispatch_rpc` (~L428), session DB binding (~L1813-1851), CSRF on HTTP dispatch (~L2487) |
| `odoo/tools/config.py` | 433ff84b625a69e08cce9f42911aa608d3e615ee | `admin_passwd` default (~L207), `dbfilter` (~L276), `list_db` (~L415), password verify/set (~L1033-1047) |
| `odoo/service/security.py` | d332199c6178ea451535d0997473d7d6c8844c15 | Session-token compute and check |
| `odoo/addons/base/models/ir_binary.py` | e7feca93dc31cc8ee7228df68c1f169d2dcae340 | `_find_record` access ladder (~L23-55), `_record_to_stream` (~L57-83) |
| `odoo/addons/base/models/ir_attachment.py` | 905ae118b8c8e5050fdc33eb1631c88e3926b888 | Attachment `_check_access` (~L514-600), `_can_return_content` (~L965-978), `_to_http_stream` (~L913) |
| `odoo/exceptions.py` | 6baf8608fd66845bcb164539a6a0331f7e66ab20 | Exception hierarchy (access and missing errors are user-error subclasses) |
| `odoo/tools/misc.py` | 6d27505917a80a2cf9d3b3c6faa6bf8bca86acfd | Limited field access token verify (~L1902); addons-path file containment (~L196) |

Blobs cited: **19**. The six `addons/web/controllers/*` blobs are identical to the PASS-1 values, so the web controllers did not drift between passes. The other 13 blobs are new in this pass.

## 3. Findings (delta)

### (a) Export authorization
- **F-1** WHAT: the export-group check runs server-side inside the ORM's generic export-data method, which every model inherits. The method refuses with a user error unless the environment is admin (superuser mode, or the user holds the Access Rights group `base.group_erp_manager`) or the user holds `base.group_allow_export`. (`odoo/orm/models.py` ~L889)
- **F-2** WHAT: the CSV and XLSX routes (`auth='user'`) both go through one shared base flow. That flow selects records with the caller's own environment (search by domain, or browse by ids), then calls the export-data method: once in the grouped branch, and once per prefetch batch in the flat branch. So the gate in F-1 applies to both formats. The controller itself has no group check, which confirms the PASS-1 observation. It logs the user, the record count, the remote address and the field names. (`addons/web/controllers/export.py` ~L553-638)
- **F-3** WHAT: the row builder is a private method (leading underscore), so the public entry points to export rows are the gated method and the `/json` route, which has its own group check. WHY: the gate sits on the export verb, not on data visibility. RISK: the same field values can still be reached through ordinary read, search-read and read-group APIs, subject only to ACLs and record rules. The export group controls bulk file export, not data confidentiality. (`odoo/orm/models.py` ~L678, ~L880; `addons/web/controllers/json.py` ~L69)
- **F-4** WHAT: `/web/pivot/export_xlsx` (`auth='user'`) turns a table payload supplied by the client into XLSX. It reads no model data and has no export-group check. RISK: this is not a data-access bypass, because the caller supplies the data, but it is an export surface outside the gate. (`addons/web/controllers/pivot.py` ~L16-40)
- Negative: no export-group reference was found in `ir_model.py` or `odoo/service/model.py`.

### (b) Database manager
- **F-5** WHAT: the master password is stored as a hash in server configuration. Its file-only default is the literal `admin`, and an empty stored value blocks all master authentication. The check fails when the supplied password is empty or does not match. (`odoo/tools/config.py` ~L207, ~L1036-1047; `odoo/service/db.py` ~L60-63)
- **F-6** WHAT: the DB service dispatcher runs the master-password check first for every method except four: exist, list, language list and version. Create, duplicate, drop and change-password reach it through the RPC dispatch. Backup and restore call the check directly in the controller. (`odoo/service/db.py` ~L516-527; `addons/web/controllers/database.py` ~L126-167)
- **F-7** WHAT: the `list_db` setting (off via `--no-database-list`) is enforced by a decorator on the service functions: create, duplicate, drop, dump, dump manifest, restore, rename, change admin password and migrate. With `list_db` off, these raise access-denied whatever password is supplied. Listing also raises unless it is forced internally. The manager and selector pages still render when listing is off: the listing error is caught and only the current DB is shown. The login page gets a flag that hides the manager link. `/web/database/list` returns the listing call's error. (`odoo/service/db.py` ~L46-51, ~L440-442, ~L489-491; `database.py` ~L30-40, ~L178; `home.py` ~L147-148)
- **F-8** WHAT: first-caller bootstrap. On create, duplicate, drop, backup and restore, if the stored master password still equals the default and the request carries a non-empty master password, the controller first sets the master password to the supplied value, then continues. RISK: on a deployment that keeps the default, any unauthenticated caller who reaches these POST routes can set the master password and then run DB operations. This depends on configuration and was not runtime-verified. (`addons/web/controllers/database.py` ~L73-75, ~L96-98, ~L113-115, ~L129-131, ~L153-155)
- **F-9** WHAT: all mutating manager routes are `auth='none'`, POST and `csrf=False`. The HTTP dispatcher applies CSRF only when a route leaves CSRF enabled. So these routes rely on the master password and `list_db`, not on session or CSRF. (`database.py`; `odoo/http.py` ~L2487-2496)
- **F-10** WHAT: `dbfilter` (a host/domain regex with `%h`/`%d` placeholders) is applied in two places. First, the web DB list returns only matching names. Second, request binding: a session DB or an `X-Odoo-Database` header that fails the filter is not bound, and a mismatched session is logged out. If there is no filter but `db_name` is set, that list is used as an allowlist instead. (`odoo/http.py` ~L389-418, ~L1813-1851)
- **F-11** WHAT: dbfilter coverage of manager operations is uneven. Backup checks the target name against the filtered web list. Drop checks only against the unfiltered, forced service list, which covers DBs owned by the connecting role. Duplicate uses the source name with no filter membership check. Restore refuses an existing name. RISK: dbfilter is a routing and visibility control, not an authorization boundary for manager operations. On a shared PostgreSQL role, a master-password holder can act on DBs that the filter hides. (`database.py` ~L133; `odoo/service/db.py` ~L185-197, ~L233-235, ~L334-338)

### (c) `/web/become`
- **F-12** WHAT: the route is `auth='user'`, type http and `readonly=True`, with no methods restriction, so it accepts GET. If the current user passes the system-group check (`base.group_system`, evaluated in sudo), it sets the session's user to the superuser id, clears the registry cache, and recomputes the session token for the new uid. It then redirects to the post-login target. A non-system user is redirected without any change. (`addons/web/controllers/home.py` ~L162-171; `res_users.py` ~L1177-1179; `odoo/service/security.py`)
- **F-13** RISK: after the switch, the session runs as the superuser. Superuser mode skips ACLs, record rules and field groups (see `_has_field_access` and `is_admin` in environments). The switch is reachable by GET, and CSRF is only enforced on unsafe methods (`http.py` ~L2487), so the switch can be triggered cross-site against a logged-in system user. Its effect is limited to that user's own session. The only gate is the system group. No audit log was found at the route itself.

### (d) Public / no-login content routes
- **F-14** `/web/content*` and `/web/image*` (`auth='public'`) both resolve records through the ir.binary record finder. It finds the record by xmlid, or by model and id where the model must be in the registry, then checks existence. It then applies an access ladder in order: (1) a valid time-limited field access token (HMAC-style, scoped to "binary", with expiry), giving a sudo record; (2) the model's may-return-content hook, giving a sudo record; (3) otherwise a normal read access check (ACL plus record rules) as the caller, often the public user. (`ir_binary.py` ~L23-55; `odoo/tools/misc.py` ~L1902-1922)
- **F-15** The base may-return-content hook returns false for all models. The attachment override returns true in three cases: a matching stored access token (compared in constant time, and a mismatch raises access-error); the attachment being flagged public; or a portal user who passes a read check. (`odoo/orm/models.py` ~L5854-5868; `ir_attachment.py` ~L965-978)
- **F-16** The attachment read check makes public attachments readable. Otherwise a non-system user is denied when the attachment is unlinked and was created by someone else, or when it is bound to a field whose groups the user lacks. Linked attachments inherit the read access of their target record. (`ir_attachment.py` ~L514-600)
- **F-17** Streaming: for non-attachment models, the field must be binary and the field-group check applies. That check passes under sudo, so a token or hook grant bypasses field groups by design. Stored files resolve through a safe join under the DB's filestore directory. (`ir_binary.py` ~L57-83, ~L107-120; `ir_attachment.py` ~L913-928; `odoo/orm/models.py` ~L3375-3387)
- **F-18** Denial behaviour differs by route. Content turns a user error, which includes access-error and missing-error, into a 404. Image serves a placeholder image instead (under sudo, stream not public), or a 404 when download is requested. RISK: a denial is not distinguishable as 403, which is neutral for leakage but matters for observability. (`binary.py` ~L77-80, ~L191-209; `odoo/exceptions.py`)
- **F-19** `/web/assets/*` (public): the sudo attachment search is constrained to public, URL-bearing attachments owned by superuser and attached to the view model with id 0. On a miss, the bundle is generated under the caller's uid. (`binary.py` ~L91-160)
- **F-20** `/web/binary/company_logo`, `/logo` and `/logo.png` (`auth='none'`, CORS `*`): they read the company logo by raw SQL, with no ORM access check. The company is taken from the optional `company` query id, or from the session user's company, falling back to the superuser's company. RISK: any company's logo on the bound DB can be fetched by id without a session, cross-origin. Low sensitivity, but it enumerates company ids. (`binary.py` ~L258-310)
- **F-21** `/web/filestore/*` (`auth='none'`) always returns 404 and logs a misconfiguration error when x-sendfile is on. `/web/sign/get_fonts` (`auth='none'`) reads only from the module's fonts directory, with an extension allowlist and addons-path containment. (`binary.py` ~L53-60, ~L312-339; `odoo/tools/misc.py` ~L196-250)

## 4. New Gaps
- **NG-1** `odoo/service/common.py` was not examined. Any deployment-level blocking of `/web/database/*`, such as reverse-proxy rules, is outside source and not established.
- **NG-2** Whether `/web/become` switches are recorded in any audit trail (for example device log or session history) is not established statically.
- **NG-3** Other modules can override the may-return-content hook (for example website, mail, portal, which are outside `web`/`base`) and widen public content access. Those overrides were not read.
- **NG-4** The public/none routes listed in PASS-1 but outside the brief's content/image/logo scope were not deepened: translations, bundle, manifest, report barcode, set_profiling.
- **NG-5** The generation and distribution points of the limited field access token (who can mint one, and its lifetime) were not traced.
- **NG-6** Client-side (JS) gating of the export UI is still unstudied (PASS-1 G-1).

## 5. Limitations
Static source only, at a single anchor commit, fetched raw. No runtime, config file, proxy, or DB state was observed. Configuration-dependent risks (F-8, F-11) are conditional. Nothing here is a design recommendation. The statements are neutral WHAT/WHY/RISK abstractions, and no source code is reproduced.
