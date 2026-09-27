# G01 PLATFORM_BASE — RED TEAM Proof Package — `base_setup`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2 of a two-stage REC + PROOF run) |
| Group / Module | G01 PLATFORM_BASE / `base_setup` |
| Date | 2026-09-27 |
| Upstream REC | `G01_RECONCILIATION/G01_BASE_SETUP_REC_20260927.md` (34 REC items: MATCH 13, CONTRADICTION 5, UNKNOWN_PENDING_PROOF 12, GAP 4) |
| Inputs (sha256 at intake) | A1 `3e37b467fb26899f96af1f44cc17db63a7855b3696ca96a72ab5e3f489a90970`; A2 `9e913ee76c3e1c34418a7e1d1ae93e4df1c65636abbd101849cc79cb3b651a31`; Lane A `59d3d312c3f5bff8dba13b24bb66a648f357b418677a9e74f242d0929f6ae4ce`; bank `2161184604279f38a59f8e56db288f53d4e706d4ec85cb5ba2a224e883a26d62` equals FREEZE_W1-B04; freeze hash `9e31f2d27dfb959e555cf8ff117d829969e8122fe5e5544bbaf737b6ddea0377` |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`, fetched 2026-09-27 15:04:59 UTC (portal and `odoo/orm/fields.py` follow-ups by 15:07:46 UTC); every blob verified with `git hash-object` (section 2) |
| Predeclaration | Scratchpad `rec_asgn_bset/PROOF_CASES_PREDECLARED.md` (shared with `auth_signup`), stamped 2026-09-27T15:04:44Z, sha256 `97055575538b3e51678d029d26b1b009984a37e5cdf6fc2cbb09a971577ec01f`. **No source was fetched before this stamp** in this run |
| Runtime device | THPATTARAKRIT-SOLUTION-SERVICE-2.local: **OFFLINE**. Probe 2026-09-27 15:09:20 UTC: `getent hosts` rc=2; HTTP probe to port 8069 → curl rc=6 (could not resolve host) |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** |

Clean-room note: results are neutral paraphrases of observed source behaviour. Identifiers are evidence pointers only. No vendor code is reproduced; nothing recommends reusing vendor schema, ORM, workflow, UI or naming. No percentages. No Formal Coverage claim. No git operations. Inputs were not edited. Source copies in scratchpad only (`rec_asgn_bset/src/`, blob log `rec_asgn_bset/blobs.txt`).

## 1. Case design

- The 11 A2 proof requirements (PR-BSET-01..11) become **runtime cases PC-BSET-18..28**, one to one, procedures/expected/fail taken unchanged from A2 §7 and restated in section 4.
- The static prediction basis for REC items becomes **SOURCE / CONFIG static cases PC-BSET-01..17**, predeclared and **executed now**.
- A static PASS confirms only a source reading. **It is never counted as a runtime result.**
- Layers: SRC, SRC(core), CFG, RT as in the auth_signup Proof package.

## 2. Blob verification (executed)

| File | Expected blob (Lane A / A2 log) | Computed `git hash-object` | Result |
|---|---|---|---|
| `addons/base_setup/__manifest__.py` | 92ae94dd… (E1/R1) | 92ae94dd346f4f755bd269a4f0f866738416c930 | MATCH |
| `addons/base_setup/models/res_config_settings.py` | 7de29781… (E5/R2) | 7de297811c8722411552e9bdc4ba12b1d2201029 | MATCH |
| `addons/base_setup/models/res_users.py` | ba102d65… (E6/R3) | ba102d652e5cc2ad3b7af2f9b860897427ae7c23 | MATCH |
| `addons/base_setup/models/ir_http.py` | 4e7bb7df… (E7/R4) | 4e7bb7df171c1c59592178b01f34d4fe5d00cd47 | MATCH |
| `addons/base_setup/models/kpi_provider.py` | 4211916c… (E8/R5) | 4211916c589872d4bc4597f601fba0fbfa2b1d67 | MATCH |
| `addons/base_setup/controllers/main.py` | cce2c3f7… (E9/R6) | cce2c3f7609f7659ca0e034ba4e34a10014f4b32 | MATCH |
| `addons/base_setup/controllers/kpi.py` | 69c9c21c… (E10/R7) | 69c9c21c1aa03bb90589d7c56f5c5b9bee6fe3e8 | MATCH |
| `addons/base_setup/data/base_setup_data.xml` | e0d02590… (E11/R8) | e0d02590384d7e6a23dd6287b227ffb13358fbac | MATCH |
| `addons/base_setup/views/res_config_settings_views.xml` | f97b9b25… (E12/R9) | f97b9b257d32480312e4ca826fed780ee99ca19e | MATCH |
| `odoo/addons/base/models/res_users.py` (core) | 9d42d77a… (A2 C1) | 9d42d77ae8ec19028c99b3c668294569ded3a86a | MATCH |
| `odoo/orm/models.py` (core) | 11f50c4e… (A2 C2) | 11f50c4e0b676fbb4b8a45e9703326946348ff98 | MATCH |
| `odoo/addons/base/security/ir.model.access.csv` (core) | 29785e02… (A2 C3) | 29785e02c9795cd27a0b6b5652853d03995b9c35 | MATCH |
| `odoo/modules/module.py` (core) | 488a2a06… (A2 C4) | 488a2a063d4c2ccde0b7bb80727880050c3ff2d0 | MATCH |
| `odoo/addons/base/models/res_config.py` (core) | 50464416… (A2 C5) | 504644162d067988dd7d3dcb90cd7e1a065c9fc3 | MATCH |
| `odoo/orm/fields.py` (core, new read) | — (no prior record) | c5101a770890ddf937213beca88fdab9ac3f8e1b | RECORDED (first read; anchor-fetched) |
| `addons/portal/models/__init__.py` (cross-module, new read) | — | f49f180354e695c6ec17b960cc7ea28f007e5b94 | RECORDED |
| `addons/portal/models/res_users_apikeys_description.py` (cross-module, new read) | — | 44c0008fd902b3ac08c57d0eb036b5c5c29bf0ef | RECORDED |
| `addons/auth_signup/models/res_users.py` (cross-module) | 1a0280b8… (auth_signup E8) | 1a0280b8c37a11072caabe7640342b4f3f553514 | MATCH |

14 of 14 previously recorded blobs match; 3 new reads recorded (no prior value to compare).

## 3. Static cases — executed (SOURCE / CONFIG)

| Case | Layer | Links (REC) | Expected (predeclared) | Fail (predeclared) | Actual (observed, paraphrased; file lines) | Result |
|---|---|---|---|---|---|---|
| PC-BSET-01 | CFG | REC-01, REC-22 (C01, C22) | Deps base/web; auto-install; no security files; no job data | Job or security files present | Depends on base and web; auto-install and installable; data list is one seed file and two views — no ACL, record-rule or job file (manifest L14-26) | PASS |
| PC-BSET-02 | CFG | REC-02 (C02) | Menu restricted to system admin; blocks dev-mode / multi-company | Menu open wider | General Settings menu restricted to the system-administrator group (views L218-224). Layout/edit/preview, import, feedback, PWA and performance blocks restricted to developer mode; inter-company block to multi-company; API-key block to system administrators (L50, L82-90, L94, L124-135, L193) | PASS |
| PC-BSET-03 | SRC+SRC(core) | REC-03 (C03) | Only footer writable pass-through; layout/name/country read-only | Layout/name writable | Footer related field explicitly writable (settings L33). Layout (L37) and company name (L42) are related without a writable flag; country code explicitly read-only (L44). Core: related fields default to read-only unless declared otherwise (fields L452-458) | PASS |
| PC-BSET-04 | SRC+SRC(core) | REC-05 (C05) | Group created on demand + registered non-updatable, as caller; implied groups applied to new internal users | Elevated creation or no registration | When the default-access reference is missing, a group is created and an external-id record with the non-updatable flag is created, both without elevation, then the form opens (settings L58-79). Core: default groups for new employees = employee group plus the implied groups of that default group (base res_users L203-212) | PASS |
| PC-BSET-05 | SRC | REC-06, REC-07, REC-29 (C06, C07, O6) | Normalise; archive-inclusive match by login/e-mail; reactivation flips active only; no active-user same-e-mail check; new users with a context flag only | Groups reset, or active-e-mail check present | E-mails normalised (base_setup res_users L13); fails closed without normalised-e-mail field (L16-17); archived users matched by raw/normalised login or normalised e-mail with archive filter off (L20-22); each is reactivated by setting active only (L23-24); remaining e-mails create users with login = normalised e-mail under a context flag (L27-35). No search for **active** users holding the e-mail. The flag is consumed only for partners without users (auth_signup res_partner L46), so it is inert here; the invitation comes from auth_signup's create hook | PASS |
| PC-BSET-06 | SRC(core) | REC-07, REC-24 (C07, O1 HIGH) | Reactivation does not reset groups; key check needs owner active, unexpired, scope unset or remote-call → pre-archive keys usable after reactivation | Archive revokes keys / strips groups | Core user write on activation only unarchives the partner before the generic write (base res_users L596-606); no group change. Key check: owner active, index match, scope null or requested scope, not expired (L1725-1750). Keys are removed only on self-service account deletion (L962-967) and by expiry GC (L1715-1722) — not on archive. A pre-archive unexpired key therefore validates again once the owner is active | PASS |
| PC-BSET-07 | SRC(core)+SRC | REC-15, REC-26 (C15, O3 HIGH) | No role/share/group check on owner; unscoped keys accepted; roster of active internal users | Owner role check, or unscoped rejected | KPI path verifies the key with the remote-call scope only (kpi L102-105), then returns id, name, login, latest log date for all active non-share users (L126-138). The key check has no share, internal or group term (base res_users L1736-1750). Core comment notes the remote-call scope effectively means a global (unscoped) key (L388). Portal: base allows only internal users to create keys (L1834-1836); the portal module relaxes this for portal users when the `portal.allow_api_keys` parameter is set (portal res_users_apikeys_description L11-20) | PASS |
| PC-BSET-08 | SRC | REC-13, REC-14, REC-16 (C13, C14, C16) | Auth none, no session save; >500 → validation error; missing/mismatch/bad key omitted; per-provider rollback; errors captured | Bound absent / failures surfaced | Route: JSON-RPC, no auth, session not saved (kpi L149). More than 500 pairs → validation error before any DB work (L166-167). Per database: connect failure → omitted silently (L88-92); version mismatch → error log naming the DB, omitted (L95-100); bad key → error log naming the DB, omitted (L102-105); any other exception → logged, omitted (L170-176). Each provider call is followed by a rollback outside tests; provider exceptions become error entries (L107-124) | PASS |
| PC-BSET-09 | SRC(core)+SRC | REC-17, REC-27 (C17, O4) | Manifests of all addons on path read regardless of install state; dynamic import; cached per worker | Discovery filtered by installed state | Provider discovery iterates every addon manifest found on the addons path (kpi L20-71 → module L318-331, directory listing only) and imports the declared function; result cached per worker (kpi L20). No install-state filter in either file | PASS |
| PC-BSET-10 | SRC+CFG+SRC(core) | REC-11, REC-30 (C11 / X-BSET-01, O7) | No explicit group check; no elevation; registry read for system admins only; count enforces model access → non-admins get access error | Route elevated, or registry readable by internal/portal | Demo-status route: authenticated session, counts module-registry records with demo flag, no group check and no elevation (main L53-59). Module-registry ACL: one row granting system administrators full rights (ACL L25). Count goes through the search layer, which checks model read access for non-superusers (models L1360-1372 → L5364-5366). A1's "any logged-in user" exposure is not supported at source | PASS |
| PC-BSET-11 | SRC | REC-09, REC-10 (C09, C10) | Auth user; explicit access-rights-manager check; active internal + pending (no log row), limit 10 | No group check | Data route: authenticated; raises access denied unless access-rights manager (main L10-14); raw counts of active non-share users and of those with no log row; up to 10 pending ids/logins newest first; counts not company-scoped (L16-42) | PASS |
| PC-BSET-12 | SRC+SRC(core) | REC-12 (C12, X-BSET-02) | Counter uses ORM count; default active filter applied → same basis as dashboard | Raw count bypassing active filter | Settings counter: elevated ORM count of non-share users (settings L104-108). Core search adds the active=true term unless the domain names the active field or the context disables it; elevation does not change this (models L5368-5375) | PASS |
| PC-BSET-13 | SRC | REC-08 (C08) | User-facing error when normalised-e-mail field absent | Silent proceed | Raises a user error asking for the Discuss application when the normalised-e-mail field is missing (base_setup res_users L16-17) | PASS |
| PC-BSET-14 | CFG+SRC | REC-19 (C19) | Non-updatable, not force-created; internal users only | Emitted to all | Seed record in a non-updatable block with force-create off (data L3-7). Session info adds the flag only for internal users (ir_http L9-13) | PASS |
| PC-BSET-15 | SRC | REC-20, REC-21, REC-04 (C20, C21, C04) | Profiling bound param, no enforcement; counters privileged, all companies; toggles present | Expiry enforced here / company-scoped | Profiling-until is a parameter-bound date-time field (settings L46); no enforcement logic in module. Company and user counts are elevated with no company term; language count is global (L98-114). Fifteen `module_*` install toggles and one implied-group toggle declared (L14-36) | PASS |
| PC-BSET-16 | SRC | REC-28 (O5) | No server database-filter check in module path | DB filter applied | The KPI path opens a connection to the named database directly (kpi L88-89); no database-list or database-filter reference anywhere in the controller (search for dbfilter/db_list/db_filter: none) | PASS |
| PC-BSET-17 | SRC | REC-18 (C18) | Abstract, empty hook | Stored or non-empty | Abstract model with one hook returning an empty list (kpi_provider L4-25) | PASS |

**Static totals: 17 executed — PASS 17, FAIL 0.** No failed static result exists to preserve.

### 3.1 Refinements observed (for A3; they do not change any verdict)

- R1 (PC-07): "accepts no-scope keys" is the designed meaning of the remote-call scope in core (an unscoped key is the global key). The risk A2 identifies is breadth of the credential class (any active owner, any role), not an unintended scope bypass.
- R2 (PC-07): portal-owned keys can reach the KPI roster only where the portal module is installed **and** the `portal.allow_api_keys` parameter is set. This narrows A2 F1's conditional ("if the deployment lets portal users create keys") to a named configuration switch.
- R3 (PC-06): archive does not remove keys; self-service account deletion does. Admin-side archive followed by bulk-invite reactivation therefore revives keys, while self-deletion does not.
- R4 (PC-11): the dashboard data route uses the controller's cursor attribute rather than the request environment's cursor for its raw counts; binding of that attribute lives in core HTTP code not read here (REC-31, G2).
- R5 (PC-08): version-mismatch and bad-key cases log the database name server-side at error level, while connect failures do not log; this is a server-log distinction, not a response-body one (relevant to PC-20).

## 4. Runtime cases — NOT-EXECUTED (runtime unavailable)

Common preconditions: a disposable server built from the anchored source (`8d05257d…`) hosting at least two databases (one with `base_setup` + `mail` + `auth_signup`; one excluded by the server's database filter), named users (system admin, access-rights manager, ordinary internal, portal), API keys (scoped/unscoped), `portal.allow_api_keys` on/off, and a test addon on the addons path declaring KPI providers but not installed. Status for all: **NOT-EXECUTED — runtime device THPATTARAKRIT-SOLUTION-SERVICE-2.local OFFLINE (probe 2026-09-27 15:09:20 UTC)**. Ready to run; no result claimed.

| Case | Layer | Links (REC) | Steps (ready to run; A2 PR procedure) | Expected | Fail condition | Status |
|---|---|---|---|---|---|---|
| PC-BSET-18 | RT | PR-BSET-01; REC-15, REC-26 | Call KPI summary with a valid remote-call key of an ordinary internal user; repeat with a portal user's key where portal keys are enabled | Internal-user roster returned in both cases | Request rejected or roster omitted for a verified key | NOT-EXECUTED |
| PC-BSET-19 | RT | PR-BSET-02; REC-26 | Use a key created with no scope | Accepted | Rejected | NOT-EXECUTED |
| PC-BSET-20 | RT | PR-BSET-03; REC-14, REC-28 | Compare responses and timing for a non-existent DB vs an existing DB with a bad key | Identical bodies (empty); timing may differ | Bodies differ (existence disclosed in body) | NOT-EXECUTED |
| PC-BSET-21 | RT | PR-BSET-04; REC-28 | Name a database excluded by the server's database filter, with a valid key | Included (no filter in module path) | Omitted (then locate core enforcement) | NOT-EXECUTED |
| PC-BSET-22 | RT | PR-BSET-05; REC-11, REC-30 | Call demo-status as portal user, ordinary internal user, system administrator | Access error for first two; boolean for administrator | Non-administrator receives boolean | NOT-EXECUTED |
| PC-BSET-23 | RT | PR-BSET-06; REC-12 (confirmatory) | With archived internal users present, compare settings counter and dashboard active count | Equal | Differ | NOT-EXECUTED |
| PC-BSET-24 | RT | PR-BSET-07; REC-07, REC-24, REC-25 (+ auth_signup REC-31) | Archive a user holding groups and an unexpired key; bulk-invite the e-mail | Reactivated with same groups; key usable; no invitation mail | Groups reset, key rejected, or invitation sent | NOT-EXECUTED |
| PC-BSET-25 | RT | PR-BSET-08; REC-29 | Active user with login ≠ e-mail; bulk-invite that e-mail | Second user created | Rejected or merged | NOT-EXECUTED |
| PC-BSET-26 | RT | PR-BSET-09; REC-16, REC-17, REC-27 | Provider that writes (no commit); provider that commits; provider in an addon on path but not installed | First not durable; second durable; third executed | First durable; or third not executed | NOT-EXECUTED |
| PC-BSET-27 | RT | PR-BSET-10; REC-03 | Multi-company admin edits footer in settings under company B | Only company B footer changes; layout unchanged by save | Other company changed or layout written | NOT-EXECUTED |
| PC-BSET-28 | RT | PR-BSET-11; REC-05 | Remove default-access group reference; open the action | Group created, attributable to acting admin in audit fields | Creation unattributed or elevated | NOT-EXECUTED |

**Runtime totals: 11 cases — NOT-EXECUTED 11, PASS 0, FAIL 0.**

## 5. Summary of results

| Layer | Cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| SRC (module) | 7 (PC-05, PC-08, PC-11, PC-13, PC-15, PC-16, PC-17) | 7 | 0 | 0 |
| SRC(core) / mixed SRC+core | 6 (PC-03, PC-04, PC-06, PC-07, PC-09, PC-12) | 6 | 0 | 0 |
| CFG / CFG+SRC(+core) | 4 (PC-01, PC-02, PC-10, PC-14) | 4 | 0 | 0 |
| RT | 11 (PC-18..28) | 0 | 0 | 11 |
| **Total** | **28** | **17** | **0** | **11** |

REC item status after Proof:
- 5 CONTRADICTION items (C03, C06, C10, C11, C17): the A2 side is **source-confirmed** in each (C11: A1 exposure claim refuted at source). They remain CONTRADICTION for A3; runtime effect pending for C03 (PC-27), C11 (PC-22), C17 (PC-26).
- 12 UNKNOWN_PENDING_PROOF items: static basis confirmed for all; **all remain UNKNOWN_PENDING_PROOF** until runtime.
- 13 MATCH items unchanged (C12 confirmatory runtime PC-23 optional). 4 GAP items carried forward.

## 6. A3 eligibility

**Disposition: PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.**

A3 can challenge **now** (static scope):
1. REC classifications and counts (34 items), including C11 as CONTRADICTION (A1 refuted), the MATCH treatment of C12/X-BSET-02 and X-BSET-03 despite PR-BSET-06, and the fold-ins.
2. The 17 executed static cases PC-BSET-01..17 and refinements R1–R5 — especially whether R1/R2 narrow the HIGH finding O3 (KPI key breadth; portal keys conditional on a named parameter).
3. The HIGH finding O1 (REC-24): the static chain "archive keeps keys and groups → reactivation revives both → no invitation" across base, base_setup and auth_signup (PC-05, PC-06, auth_signup PC-19).
4. QID lineage (25 mapped, 16 no evidence yet of 41), join key and freeze hash, clean-room compliance, input integrity, and predeclaration timing (stamp precedes first fetch).

**Blocked** until the runtime device is available:
- All 11 runtime cases PC-BSET-18..28 — in particular KPI roster exposure and key classes (PC-18, PC-19), existence disclosure and DB-filter reach (PC-20, PC-21), demo-status denial (PC-22), reactivation effect (PC-24) and provider durability/uninstalled execution (PC-26).
- Closing any UNKNOWN_PENDING_PROOF item or settling runtime effect of any CONTRADICTION item. A full A3 → MASTER handoff is **not** eligible yet; this package is eligible for **A3 static-scope challenge only**.

## 7. Limitations

- No runtime executed; no runtime result claimed. Static PASS confirms source readings only.
- Core HTTP controller cursor binding, settings install/implied-group machinery, server database-filter handling in the HTTP layer, and static JS were not read (REC-31..34).
- Other installed modules may widen the module-registry ACL (C11) or add archive hooks (C07/O1).
- No percentages, no Formal Coverage claim, no git operations. Inputs not edited.
