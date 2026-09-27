# G01 PLATFORM_BASE — RED TEAM A1 Package — `web`

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `web` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_WEB_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `a06cace5e4366454549c9641b8397c00286dd5f3e2b38b3447d8ddfba069a708` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/web/` |
| Question bank (lens only) | `GMVQ/G01_PLATFORM_BASE/G01_WEB_GMVQ_MVQ_50_V1.00_DRAFT.md` (sha256 `259839a2…d558`, matches `FREEZE_W1-B01.json`) |
| Freeze | batch W1-B01, freeze hash `558ec88047aef5c8e7ea0e2675b1c43ef358ec29b172d6878068330f3fba7177`, ELIGIBLE |
| Lane B dependency | None. A1 does not wait for Lane B; no runtime evidence consumed |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Clean-room note: claims are neutral WHAT / WHY / RISK statements. Identifiers (route names, group names, file names) are evidence pointers only. No vendor code is reproduced, and no reuse of vendor schema, ORM, workflow, UI or naming is recommended. No QIDs are answered. The bank was used only as a topic lens: predictable identifiers and token links, public content exposure, export and bulk extraction, admin/database surfaces, privilege switching, company context, CSRF/replay and injection into downloaded files.

Evidence key (blob SHA-1 from Lane A; "V" = re-verified by A1 spot-check): E1 `__manifest__.py` 72f3f257… V; E4 `models/models.py` 867fba72…; E5 `models/ir_http.py` bd03fa8e… V; E6 `models/base_document_layout.py` 22081a0e…; E7 `models/res_users_settings_embedded_action.py` d405c082…; E20 `controllers/binary.py` 7b7b84f7… V; E21 `controllers/database.py` 434b915c… V; E24 `controllers/export.py` cb750f19… V; E25 `controllers/home.py` 292aaa75… V; E26 `controllers/json.py` 1d1b408e… V; E23 `controllers/domain.py` 6a71bbe1…; E33 `controllers/view.py` dfc38f00…; E30 `controllers/report.py` 59346f1c…; E31 `controllers/session.py` 2fbcfc87…; E36 `security/ir.model.access.csv` a46f838b…; E37 `security/web_security.xml` 58d06cd0…

## 1. Claims

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-WEB-C01 | WHAT: `web` is the always-installed client/RPC foundation. Its only dependency is `base`, and it installs automatically. WHY: every UI module assumes it is present. RISK: a platform redesign must supply an equivalent always-present client and data API. | E1 (S1) | HIGH | SOURCE-STATIC |
| A1-G01-WEB-C02 | WHAT: A generic client data API is attached to every model: spec-driven read, search-read, save, resequence, grouped read with an auto-unfold cap, search-panel ranges and batched onchange. RISK: one generic surface reaches every business model, so its authority rests on each model's own ACLs and record rules. | E4 | MED (structural scan only, Lane A G-4) | SOURCE-STATIC |
| A1-G01-WEB-C03 | WHAT: Generic onchange requires write access, or create access for new records, except on the user model, where self-writable fields are allowed. RISK: the self-edit exemption is a deliberate special case that any redesign must control. | E4 (~L2027) | MED | SOURCE-STATIC |
| A1-G01-WEB-C04 | WHAT: Routes use four auth levels: authenticated user (RPC, action, export, report, session, pivot), public (content, image, assets, translations, bundles, manifest, barcode, profiling toggle), none (root/webclient, login, health, filestore, company logo, database manager, fonts), and bearer (versioned JSON). RISK: public and none routes must enforce record access downstream. | Lane A §2.4-16; E20, E25, E26 (S3, S4, S6) | HIGH | SOURCE-STATIC |
| A1-G01-WEB-C05 | WHAT: The CSV and XLSX export routes are authenticated-user routes. Their shared export routine resolves records from caller-supplied model, ids or domain, merges a caller-supplied context, and exports under the caller's identity. No check for the export-permission group appears in the export controller. By contrast, the experimental JSON route refuses users who lack that group. RISK: bulk-export permission may exist only as a UI/client convention for the CSV/XLSX path. The check may instead be enforced in `base` (the export-data method) or in the client, neither of which was read. | E24 (S2); E26 (S4) | HIGH (absence in controller) / LOW (absence platform-wide) | SOURCE-STATIC |
| A1-G01-WEB-C06 | WHAT: The session payload exposes to the client whether the user holds the export-permission group. WHY: it drives client-side feature visibility. RISK: a client-visible flag is not a server guard. | E5 (S7) | HIGH | SOURCE-STATIC |
| A1-G01-WEB-C07 | WHAT: Every export writes a server log line with the actor, the record count, the model, the remote address, the field list and an id sample or domain. WHY: extraction audit. RISK: the audit record is a log line and not a stored audit entity, so retention depends on log handling. | E24 (S2) | HIGH | SOURCE-STATIC |
| A1-G01-WEB-C08 | WHAT: CSV export neutralises cell values that start with formula-leading characters, and CSV refuses grouped export. WHY: spreadsheet formula-injection mitigation. RISK: whether XLSX applies an equivalent mitigation was not examined. | E24 (S2) | HIGH (CSV) / LOW (XLSX) | SOURCE-STATIC |
| A1-G01-WEB-C09 | WHAT: The experimental JSON view routes are gated twice: the route is active only on demo databases or when a config flag is set, and the user must hold the export-permission group. A versioned variant uses bearer auth. | E26 (S4) | HIGH | SOURCE-STATIC |
| A1-G01-WEB-C10 | WHAT: The database-manager routes that change state (create, duplicate, drop, backup, restore, change master password) accept POST, need no login and are CSRF-exempt. Backup and restore check the master password directly. Create, duplicate, drop and change-password pass it to a service RPC outside this module. RISK: this is a high-impact, cross-tenant administrative surface outside tenant authentication. | E21 (S5) | HIGH (route shape) / LOW (enforcement in service) | SOURCE-STATIC |
| A1-G01-WEB-C11 | WHAT: (spot-check observation) If the server master password is still the default value, a create, duplicate, drop, backup or restore request that carries a master password first sets that value as the new master password and then continues. WHY: forces a non-default master password on first use. RISK: the first unauthenticated caller to reach the manager on a default-configured server chooses the master password. | E21 (S5) | HIGH | SOURCE-STATIC |
| A1-G01-WEB-C12 | WHAT: The database list endpoint needs no login. The selector and manager templates read the `list_db` config. Whether the list endpoint itself honours `list_db` depends on a framework helper that was not read. RISK: database names could be enumerated. | E21 (S5); E25 | MED | SOURCE-STATIC |
| A1-G01-WEB-C13 | WHAT: `/web/become` switches the session to the superuser for any user in the system group, clears the caches and recomputes the session token. Other users are simply redirected. RISK: system-group membership is equivalent to superuser, with no second factor or reason capture visible in the route. | E25 (S6) | HIGH | SOURCE-STATIC |
| A1-G01-WEB-C14 | WHAT: The company-logo routes (three aliases) need no login and allow any cross-origin caller. They read the logo with direct SQL, either for a caller-supplied company id or for the session user's company, falling back to the superuser. RISK: any company's logo in the database can be fetched by id without the ORM, record rules or tenant scope. Exposure is limited to the logo, but the tenant boundary is bypassed. | E20 (S3) | HIGH | SOURCE-STATIC |
| A1-G01-WEB-C15 | WHAT: The generic content and image routes are public. They resolve records through a binary helper in `base` using model, id, field, xmlid or an access token, and a token makes the stream public. Assets are looked up under sudo. The image placeholder is read under sudo. RISK: access to public content depends wholly on the binary helper and the token rules in `base`, which were not read. | E20 (S3) | HIGH (route shape) / LOW (enforcement) | SOURCE-STATIC |
| A1-G01-WEB-C16 | WHAT: The filestore route needs no login but always returns not-found. It logs a misconfiguration error when x-sendfile is enabled. WHY: it is a sentinel for proxy misconfiguration and not a content path. | E20 (S3) | HIGH | SOURCE-STATIC |
| A1-G01-WEB-C17 | WHAT: The health route needs no login and optionally probes the database server, returning pass or fail with an uncached JSON body. RISK: unauthenticated callers can learn whether the database is up. | E25 (S6) | HIGH | SOURCE-STATIC |
| A1-G01-WEB-C18 | WHAT: Sudo is used in action resolution, asset attachment lookup, domain-validation search, export property definitions, custom-view fetch (followed by an owner check), the language list, the web-manifest menu lookup, config params and the company hierarchy in session info. RISK: each site needs a guard after it; only the custom-view owner check and the export property-definition rationale were seen. | Lane A §2.4-19; E24, E5 (S2, S7) | MED | SOURCE-STATIC |
| A1-G01-WEB-C19 | WHAT: Session info builds the allowed companies plus their ancestor companies under sudo, because users may lack access to parents. The company-selection cookie is normalised and cleared on logout. RISK: the names and ids of disallowed ancestor companies may reach the client. | E5 (S7) | MED | SOURCE-STATIC |
| A1-G01-WEB-C20 | WHAT: Per-user embedded-action preferences are unique per (user setting, action, record). Internal users see only their own rows, and the system group sees all. Preference strings must be unique ids that are integers or "false". Set is an upsert. | E7; E36; E37 | HIGH | SOURCE-STATIC |
| A1-G01-WEB-C21 | WHAT: The document-layout configurator is transient. The system group can read, write and create it, but not unlink. A company create or write that touches branding re-renders one shared style attachment for all companies. RISK: one company's branding change triggers a global re-render. | E6; E36; E4 | MED | SOURCE-STATIC |
| A1-G01-WEB-C22 | WHAT: Custom view edit refuses views not owned by the caller. Domain validation runs an explain-only query and returns a boolean. The action loader raises a dedicated missing-action error. | E33; E23; Lane A §2.3-12 | MED | SOURCE-STATIC |
| A1-G01-WEB-C23 | WHAT: The debug mode comes from a query argument checked against an allowlist. A public route toggles profiling through the profile model. RISK: whether the profiling toggle needs a privileged user is decided in `base` and was not verified here. | E5; Lane A §2.6-27 | MED | SOURCE-STATIC |
| A1-G01-WEB-C24 | WHAT: Config levers include the upload size cap, the active-ids limit (default 20000), quick login, the web app name, the JSON-route enable flag, the base URL, the speedscope CDN, and the server keys list_db, x_sendfile and data_dir. | Lane A §2.6-26 | MED | SOURCE-STATIC |

## 2. Business rules
- BR-1: Data access from the client goes through one generic API per model. Authority comes from the target model's ACLs and record rules, not from `web` (C02).
- BR-2: The permission to export in bulk is enforced in the controller only on the JSON path. For CSV/XLSX, the server-side guard in this module is limited to the authenticated-user requirement (C05, C09).
- BR-3: Database lifecycle operations are authorised by a server-wide master secret, not by user identity (C10, C11).
- BR-4: The system group can take the superuser identity on demand (C13).
- BR-5: Preferences are strictly per user. Branding is per company, but it is rendered into one shared artifact (C20, C21).

## 3. States / transitions
- No document state machine exists in this module (Lane A §2.3-13).
- Session identity transition: authenticated system user → superuser through the become route, with the token recomputed (C13).
- Master password state: default → caller-chosen on the first database-manager call that carries a password (C11).
- Company context: the cookie value is normalised on each request and cleared at logout (C19).

## 4. Exceptions / failure modes
- A missing action raises a dedicated error. A non-owned custom view is refused. An unsupported search-panel field type raises a user error. Temporal fill combined with limit or offset is refused (C22; Lane A §2.3-11).
- A failed export is wrapped as a generic server error payload carrying serialised exception data (E24). RISK: exception detail may reach the client.
- A failed company-logo read falls back to the default logo with a warning (C14).
- The health route returns fail/500 when the DB probe fails (C17).
- A failed change of the master password renders an error that includes the exception text (E21).

## 5. Cross-module handoffs
- `base`: the binary/token helper (content and image), the export-data method, the profile model, the master-password check in the service layer, the definition of the export-permission group, the definition of the system group, and user self-writable fields.
- Framework (`odoo/service`, `odoo/http`): the database service RPC, the database-list helper and the session token computation.
- `web_tour`: extends session info. Downstream modules append to the asset bundles. `base_setup` supplies a show-effect param.

## 6. Evidence gaps (Lane A carried forward + A1)
- G-1 (Lane A): the JS client was not studied, so all client-side guards, including the export-button visibility, are unevidenced.
- G-2 (Lane A): no server-side export-group enforcement for CSV/XLSX was found in the controller. `base` export-data and the client are unread.
- G-3 (Lane A): master-password enforcement for create/duplicate/drop/change-password lives in `odoo/service`, which is unread.
- G-4 (Lane A): `models/models.py`, `export.py` and `json.py` were scanned structurally. A1 read the export base routine and the JSON gate only.
- G-5 (Lane A): the static tree and the tests were not reviewed.
- G-A1-1: the `ir.binary` record-resolution and token rules in `base` are unread, so C15 enforcement is unknown.
- G-A1-2: whether the list-database helper honours `list_db` is unknown (C12).
- G-A1-3: the XLSX formula-injection handling was not examined (C08).
- G-A1-4: whether the profiling-toggle authority check lives in `base` was not verified (C23).

## 7. CRQ candidates
- CRQ-WEB-01: Confirm, in `base` export-data or elsewhere on the server, whether CSV/XLSX export requires the export-permission group. If it does not, bulk-export permission is client-only (C05).
- CRQ-WEB-02: Read the `odoo/service` database-manager functions to confirm master-password checks for create, duplicate, drop and change-password, and whether they are rate-limited (C10).
- CRQ-WEB-03: Determine how a design should treat first-use master-password takeover on default-configured servers (C11).
- CRQ-WEB-04: Decide whether a superuser switch for administrators needs step-up auth, a reason and an audit trail (C13).
- CRQ-WEB-05: Decide whether company assets (the logo) served without authentication by a guessable id breach the tenant boundary (C14).
- CRQ-WEB-06: Verify the token and record-access rules behind public content and image routes (C15).
- CRQ-WEB-07: Confirm whether the database list endpoint is suppressed when listing is disabled (C12).
- CRQ-WEB-08: Check whether exposing disallowed ancestor-company data in session info is acceptable under tenant isolation (C19).

## 8. Contradictions
| ID | Statement | Classification |
|---|---|---|
| X-WEB-01 | The JSON route requires the export-permission group server-side. The CSV/XLSX export routes carry no such check in the controller, and the session merely advertises the flag to the client. | **CONTRADICTION CANDIDATE**. The spot-check confirms the absence in `controllers/export.py` (blob verified), but enforcement may exist in `base` or the client, so it is not CONFIRMED-FROM-SOURCE platform-wide. |
| X-WEB-02 | The Lane A description "gated by master password" for all database-manager operations does not cover the default-password branch, where a supplied value becomes the new master password (C11). | **CONTRADICTION CANDIDATE** (a nuance to the Lane A wording, not a Lane A error). The branch is source-verified; its effect in the service layer is unread. |

## 9. Spot-check log (A1 re-fetch from raw.githubusercontent.com at anchor commit; `git hash-object` compared)
| # | Path | Recorded blob | Recomputed blob | Result | Claim(s) checked |
|---|---|---|---|---|---|
| S1 | addons/web/__manifest__.py | 72f3f257…9e93 | 72f3f25791583968056ca4a42ab3e9cd13db9e93 | MATCH | C01 |
| S2 | addons/web/controllers/export.py | cb750f19…e69 | cb750f193c5548fe70a01422d644c66805a20e69 | MATCH | C05, C07, C08: no export-group check found; export under caller identity; audit log line; CSV formula guard |
| S3 | addons/web/controllers/binary.py | 7b7b84f7…41b1 | 7b7b84f771eeb5a0f096500f7530a48c956f41b1 | MATCH | C14 (none-auth + any-origin + direct SQL logo), C15, C16 |
| S4 | addons/web/controllers/json.py | 1d1b408e…a38d | 1d1b408ea56cd92249b743012dd6eb039caba38d | MATCH | C09: demo/config gate + export-group check confirmed |
| S5 | addons/web/controllers/database.py | 434b915c…4b48 | 434b915ceb3a935c1fdbee248d4a4ed7a8533b48 | MATCH | C10, C11, C12: none-auth/POST/csrf-exempt; direct check only on backup/restore; default-password branch |
| S6 | addons/web/controllers/home.py | 292aaa75…309c9f | 292aaa75a2c35b71acb3c97488a6dc2c96309c9f | MATCH | C13 (system group → superuser, token recomputed), C17 |
| S7 | addons/web/models/ir_http.py | bd03fa8e…ac66 | bd03fa8e5e43ec580a63a068121f5a292215ac66 | MATCH | C06, C19: export flag in session; sudo ancestor companies; cookie normalise/clear |
Result: 7 of 7 re-fetched blobs match (HTTP 200 each). The Lane A blob SHAs for these paths are confirmed.

## 10. Provenance
- Input: the Lane A packet (sha256 above). A1 re-fetched only the 7 files listed in section 9, from the anchor commit, into a session scratchpad outside the repository. None of that content is reproduced here.
- Topic lens: the frozen W1-B01 bank. Its hash was verified against the freeze manifest, and it was not edited. No QIDs were answered.
- No Lane B, runtime, DB or config state consumed. No git operations performed.

## 11. Limitations
- Source presence is not runtime reachability. Proxy rules, `list_db`/server flags, installed modules and deployment settings can change what is exposed.
- All claims are SOURCE-STATIC at a single commit. No Formal Coverage is claimed and no completion percentage is implied.
- Claims marked LOW or MED depend on unread `base`, framework or JS code. A2 must not treat them as confirmed.
