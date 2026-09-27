# G01 PLATFORM_BASE — RED TEAM A2 REVIEW — `base_setup`

| Item | Value |
|---|---|
| Role | RED TEAM A2 (functional / semantic verifier of A1 conclusions) — independent of A1; A1 package not repaired |
| Group / Module | G01 PLATFORM_BASE / `base_setup` |
| A1 package | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_BASE_SETUP_A1_PACKAGE_20260927.md` |
| A1 package sha256 | `3e37b467fb26899f96af1f44cc17db63a7855b3696ca96a72ab5e3f489a90970` |
| Upstream Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_BASE_SETUP_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `59d3d312c3f5bff8dba13b24bb66a648f357b418677a9e74f242d0929f6ae4ce` (matches value recorded in A1 header) |
| Topic lens (not answered) | `GMVQ/G01_PLATFORM_BASE/G01_BASE_SETUP_GMVQ_MVQ_40_V1.00_DRAFT.md`, batch W1-B04, ELIGIBLE; sha256 `2161184604279f38a59f8e56db288f53d4e706d4ec85cb5ba2a224e883a26d62` (matches A1 header prefix/suffix) |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Lane B | None in repository for this module — see §6 |
| Date | 2026-09-27 |
| Disposition | **A2 PASS WITH FINDINGS** (one HIGH claim NOT_VERIFIED — C11 / X-BSET-01 — must be carried into Reconciliation as such) |

Clean-room: statements are neutral WHAT / WHY / RISK abstractions; identifiers and line numbers are evidence pointers only; no reference code is reproduced; no QID is answered; no percentage and no Formal Coverage claim.

## 1. Test plan (predeclared before verdicts)

| # | Test | Method | Pass condition |
|---|---|---|---|
| T1 | Lineage | sha256 of A1 package, Lane A packet, bank; compare with A1 header | Hashes consistent |
| T2 | Blob re-fetch | Re-fetch every file cited by HIGH or contradiction claims; `git hash-object`; compare with Lane A | All blobs match |
| T3 | Independent semantic re-read | Full-text re-read of module files; restate behaviour before comparing with A1 | Claim meaning matches source meaning |
| T4 | Core gap settlement | Fetch at anchor: API-key credential helper (key-owner constraints), default archive filtering, base user write on (un)archive, default-group semantics, model ACL for module registry, addon-manifest discovery | Gap settled or explicitly left open |
| T5 | Mandated focus items | KPI summary user-data exposure and key-owner role check; demo-status group; active-user count vs archived; reactivation restoring rights | Explicit verdict + business meaning |
| T6 | Business-meaning review | SaaS admin/onboarding lens: admin authority, tenant/company scope, identity lifecycle, telemetry exposure | Overclaims and omissions listed |
| T7 | Lane B classification | Search repo for Lane B material | NOT_APPLICABLE / UNCORROBORATED, never FAIL |
| T8 | Proof requirements | Inherently runtime claims only; falsifiable, expected + fail condition | Listed in §7 |

### T1/T2/T4 evidence (re-fetch log, 2026-09-27)

| # | Path (anchor) | Blob (git hash-object) | vs Lane A |
|---|---|---|---|
| R1 | addons/base_setup/__manifest__.py | 92ae94dd346f4f755bd269a4f0f866738416c930 | MATCH E1 |
| R2 | addons/base_setup/models/res_config_settings.py | 7de297811c8722411552e9bdc4ba12b1d2201029 | MATCH E5 |
| R3 | addons/base_setup/models/res_users.py | ba102d652e5cc2ad3b7af2f9b860897427ae7c23 | MATCH E6 |
| R4 | addons/base_setup/models/ir_http.py | 4e7bb7df171c1c59592178b01f34d4fe5d00cd47 | MATCH E7 |
| R5 | addons/base_setup/models/kpi_provider.py | 4211916c589872d4bc4597f601fba0fbfa2b1d67 | MATCH E8 |
| R6 | addons/base_setup/controllers/main.py | cce2c3f7609f7659ca0e034ba4e34a10014f4b32 | MATCH E9 |
| R7 | addons/base_setup/controllers/kpi.py | 69c9c21c1aa03bb90589d7c56f5c5b9bee6fe3e8 | MATCH E10 |
| R8 | addons/base_setup/data/base_setup_data.xml | e0d02590384d7e6a23dd6287b227ffb13358fbac | MATCH E11 |
| R9 | addons/base_setup/views/res_config_settings_views.xml | f97b9b257d32480312e4ca826fed780ee99ca19e | MATCH E12 |
| C1 | odoo/addons/base/models/res_users.py (API-key helper, key model, user write, default groups, log model, login-date field) | 9d42d77ae8ec19028c99b3c668294569ded3a86a | A2 core read (A1 gaps G4, G8) |
| C2 | odoo/orm/models.py (default archive filter) | 11f50c4e0b676fbb4b8a45e9703326946348ff98 | A2 core read (A1 gap G1) |
| C3 | odoo/addons/base/security/ir.model.access.csv (module-registry ACL) | 29785e02c9795cd27a0b6b5652853d03995b9c35 | A2 core read (A1 gap G6) |
| C4 | odoo/modules/module.py (addon manifest discovery) | 488a2a063d4c2ccde0b7bb80727880050c3ff2d0 | A2 core read |
| C5 | odoo/addons/base/models/res_config.py (settings save) | 504644162d067988dd7d3dcb90cd7e1a065c9fc3 | A2 core read |

Result: 9/9 module blobs match Lane A; lineage consistent.

## 2. Claim verdict table

Verdict key as in the auth_signup A2 review. "Re-read" = independent semantic re-read performed.

| Claim | A1 conf. | Re-read | Verdict | A2 basis (own restatement) |
|---|---|---|---|---|
| C01 | HIGH | Y | VERIFIED | R1: deps base/web, auto-install, no security files in data list. |
| C02 | HIGH | Y | VERIFIED | R9 L218-224 menu restricted to system administrators; blocks restricted to developer mode / multi-company; API-key block to system administrators (L124). |
| C03 | MED | Y | PARTIAL | R2 L33: only the report footer is a writable company pass-through in this module. Layout (L37) and company name / country code (L42-45) are related but read-only by default here, so a save does not write them. Risk direction correct, scope overstated. |
| C04 | MED | Y | VERIFIED | R2 declares 15 install-toggle fields; mechanics in base settings machinery (C5), not here. |
| C05 | HIGH | Y | VERIFIED (strengthened) | R2 L58-79: group created and registered as non-updatable data on demand, no privilege elevation (runs as caller). C1 L203-212: new internal users receive the implied groups of this group, confirming the WHY. |
| C06 | HIGH | Y | PARTIAL | R3 L12-37: normalisation, archive-inclusive match by login or normalised e-mail, reactivation instead of duplicate, new users with login = normalised e-mail — confirmed. "Prepared enrollment link" mis-attributed: base_setup only sets a context flag; the link is produced by auth_signup's create hook when installed, and the flag itself is honoured only for partners without users (inert on this path). Without auth_signup no link exists. |
| C07 | MED | Y | VERIFIED (strengthened, A1 gap G8 settled at base level) | R3 L23-24 flips only the active flag. C1 L596-606: base user write on reactivation only unarchives the partner; archive does not strip groups. Prior group membership is therefore restored. Additionally, the API-key helper accepts keys of any active owner (C1 L1725-1750), so unexpired keys issued before archive become usable again on reactivation — see F3. |
| C08 | HIGH | Y | VERIFIED | R3 L16-17 fails closed with user-facing error when the normalised-e-mail field is absent. |
| C09 | HIGH | Y | VERIFIED | R6 L10-51: logged-in session required; explicit access-rights-manager check; active internal count, pending count, up to 10 pending ids/logins. Counts are cross-company (raw queries). |
| C10 | HIGH | Y | PARTIAL | Definition of pending (active, internal, no log row) VERIFIED. The WHY ("consistent with search basis, not compute basis") is not supported: the login-date field is a related projection of log rows (C1 L233), so both auth_signup bases and this definition coincide. |
| C11 | HIGH | Y | **NOT_VERIFIED** | R6 L53-59: no explicit group check — literal part true. But the count runs on the module registry model without privilege elevation, and C3 L25 grants read on that model to system administrators only. Model-level read check applies to search/count (C2 L5364-5366). Non-administrators, including portal and ordinary internal users, receive an access error rather than the demo flag. The claimed exposure to "any logged-in user" is contradicted by core ACL (absent other modules granting wider read). X-BSET-01 is therefore a literal difference without the claimed security effect. |
| C12 | MED | Y | VERIFIED (contradiction X-BSET-02 settled) | R2 L104-108 count uses the ORM; C2 L5368-5375 adds the active filter by default (privilege elevation does not change it). Settings counter and dashboard active count share the same basis; archived users excluded from both. |
| C13 | HIGH | Y | VERIFIED | R7 L148-167: no auth, no session save, more than 500 pairs → validation error before any database work. |
| C14 | HIGH | Y | VERIFIED (nuance F5) | R7 L88-105: missing DB, version mismatch, bad key → omitted; comment states anti-scanning intent. Also non-Odoo databases or malformed entries raise and are omitted via the outer handler (R7 L171-176). Version-mismatch and bad-key cases are logged server-side with the database name. |
| C15 | HIGH | Y | VERIFIED (strengthened) | R7 L126-145 returns id, name, login, last-login for all active internal users. No role check in module; C1 L1725-1750 helper constraints are only: owner active, scope unset or remote-call, not expired. No internal/share or group condition on the key owner. |
| C16 | HIGH | Y | VERIFIED (limit F6) | R7 L107-124: per-provider rollback (outside tests), errors captured; outer per-database handler logs and omits. |
| C17 | MED | Y | PARTIAL | Discovery is broader than "installed addon": C4 L318-331 reads every manifest on the addons path regardless of installation state in the target database; R7 L20-71 imports and caches per worker. A provider shipped by an addon never installed in a database still executes against that database's cursor. |
| C18 | HIGH | Y | VERIFIED | R5: abstract model, empty summary hook. |
| C19 | MED | Y | VERIFIED | R8 non-updatable, not force-created; R4 emitted only for internal users. |
| C20 | LOW | Y | VERIFIED | R2 L46 settings-bound parameter; no enforcement in module. |
| C21 | MED | Y | VERIFIED | R2 L98-114 privileged, all-company counts; language count global. |
| C22 | HIGH | Y | VERIFIED | R1 data list contains no job definitions. |

Verdict counts: VERIFIED 17, PARTIAL 4 (C03, C06, C10, C17), NOT_VERIFIED 1 (C11), OUT_OF_SCOPE 0. Total 22.

Contradiction re-classification (A2 view; A1 table not edited):

| ID | A1 class | A2 result |
|---|---|---|
| X-BSET-01 demo-status vs data route | CONFIRMED-FROM-SOURCE | Literal difference only; security effect REFUTED by core model ACL (C3 L25) |
| X-BSET-02 active-user count basis | CANDIDATE | RESOLVED — no divergence (C2 default archive filter) |
| X-BSET-03 KPI last-login vs auth_signup login date | CANDIDATE | RESOLVED — both derive from log rows (C1 L233); KPI uses latest creation date, field uses most recent row by id; equivalent except for pathological id/date inversion |

## 3. Semantic findings (business meaning — SaaS administration / onboarding)

- **F1 (HIGH, C15).** A single valid remote-call key held by any active user — including a low-privilege internal user, and a portal user if the deployment lets portal users create keys — yields the full roster of active internal users with logins and last-activity timestamps, through an unauthenticated route. For a multi-tenant SaaS this is an identity-inventory disclosure decoupled from the administrator authority that the visible settings dashboard requires (C09). Keys with no scope are also accepted.
- **F2 (HIGH, C11 correction).** The demo-status route is effectively administrator-only through model ACL, not through an explicit check. Business meaning: exposure is lower than A1 states, but protection is implicit and would silently widen if another module grants read on the module registry. SMEsPlus should require explicit endpoint-level authorisation.
- **F3 (HIGH, C07 extension).** Bulk-invite reactivation restores prior groups and revives unexpired API keys of the archived user, and (per auth_signup interaction) sends no new invitation. A deactivated identity can regain full prior authority, including headless API access, through an onboarding action whose UI intent is "invite by e-mail". Bank topic "reactivation does not restore stale access" is contradicted at source level.
- **F4 (MED, new).** Bulk invite does not detect an existing active user whose e-mail matches but whose login differs; auth_signup only removes still-Invited matches. A second identity with the same e-mail can be created (source-inferred; proof PR-BSET-08). An existing active login equal to the e-mail will instead fail the whole batch on login uniqueness.
- **F5 (MED, C14 nuance).** Silent omission hides existence in the response body, but existing vs missing databases take different code paths (connect failure vs version/key queries and error logging) — timing side channel plausible. No server database-filter check is applied inside the module path: any database reachable by the server's database connection can be named.
- **F6 (MED, C16/C17).** Rollback does not prevent a provider from committing explicitly or acting outside the database (network, files). Providers receive a raw cursor and user id with no access-rule context. Combined with C17 (addons-path-wide discovery), the unauthenticated route executes third-party code per credential that passes key check.
- **F7 (LOW, C09/C21).** Dashboard and settings counts are system-wide; on a multi-company tenant a company-limited administrator may read them as company counts (bank topic "counts clearly identified").

Overclaims: C03 (layout/identity write-through), C06 (link preparation attributed to base_setup), C10 (WHY), C11 (any logged-in user), C17 (installed-only).

## 4. Omissions (not in A1)

| # | Omission | Severity | Link |
|---|---|---|---|
| O1 | API keys revived on reactivation | HIGH | F3 |
| O2 | Reactivated users receive no invitation / notification | MED | F3; auth_signup A2 O8 |
| O3 | Key helper accepts unscoped keys; no owner share/internal check | HIGH | F1 |
| O4 | Addons-path-wide provider discovery (not installed-only) | MED | C17, F6 |
| O5 | No database-filter enforcement in KPI path; timing side channel | MED | F5 |
| O6 | Duplicate identity by e-mail through bulk invite | MED | F4 |
| O7 | Demo-status protection is ACL-implicit | MED | F2 |

## 5. Gap disposition (A1 §6)

| Gap | A2 status |
|---|---|
| G1 | Settled — no divergence (C12) |
| G2 | Open — controller cursor binding not read (no claim depends on it beyond C09 which uses the request's own database) |
| G3 | Partially read — save semantics only (C5) |
| G4 | Settled for key checks (C15); manifest loader settled (C17); which users may create keys remains runtime/config |
| G5 | Open (static JS) |
| G6 | Settled — ACL-restricted (C11) |
| G7 | Open |
| G8 | Settled at base level (C07); other installed modules may add archive hooks |

## 6. Lane B classification

No Lane B / runtime observation material exists in the repository for `base_setup`. Classification: **NOT_APPLICABLE** for structural claims (C01, C04, C18, C19, C22) and **UNCORROBORATED** for all behaviour claims. No FAIL assigned on the basis of absent Lane B.

## 7. Proof requirements (MISSING_REQUIRED_RUNTIME_PROOF — inherently runtime claims only)

| PR | Claim(s) | Procedure | Expected (from source) | Fail condition |
|---|---|---|---|---|
| PR-BSET-01 | C15, F1 | Call KPI summary with a valid remote-call key of an ordinary internal user; repeat with a portal user's key where portal keys are enabled | Internal-user roster returned in both cases | Request rejected or roster omitted for a verified key |
| PR-BSET-02 | C15, O3 | Use a key created with no scope | Accepted | Rejected |
| PR-BSET-03 | C14, F5 | Compare responses and timing for non-existent DB vs existing DB with bad key | Identical bodies (empty); timing may differ | Bodies differ (existence disclosed in body) |
| PR-BSET-04 | F5 | Name a database excluded by the server's database filter, with a valid key | Included (no filter in module path) | Omitted (then locate core enforcement) |
| PR-BSET-05 | C11, F2 | Call demo-status as portal user, ordinary internal user, system administrator | Access error for first two; boolean for administrator | Non-administrator receives boolean |
| PR-BSET-06 | C12 | With archived internal users present, compare settings counter and dashboard active count | Equal | Differ |
| PR-BSET-07 | C07, F3 | Archive user holding groups and an unexpired key; bulk-invite the e-mail | Reactivated with same groups; key usable; no invitation mail | Groups reset, key rejected, or invitation sent |
| PR-BSET-08 | F4 | Active user with login ≠ e-mail; bulk-invite that e-mail | Second user created | Rejected or merged |
| PR-BSET-09 | C16, C17, F6 | Provider that writes (no commit); provider that commits; provider in an addon on path but not installed | First not durable; second durable; third executed | First durable; or third not executed |
| PR-BSET-10 | C03 | Multi-company admin edits footer in settings under company B | Only company B footer changes; layout unchanged by save | Other company changed or layout written |
| PR-BSET-11 | C05 | Remove default-access group reference; open action | Group created, attributable to acting admin in audit fields | Creation unattributed or elevated |

Count: 11 proof requirements.

## 8. Limitations

- All verdicts are SOURCE-STATIC at one anchor commit; source presence is not runtime reachability.
- Core reads limited to gap settlement; settings machinery beyond save, database-filter handling in the HTTP layer, portal key-creation policy and static JS not reviewed.
- Other installed modules may extend ACLs (affects C11) or add archive/reactivation hooks (affects C07).
- No QID answered; bank used only as topic lens. No percentages; claim counts are not a denominator; no Formal Coverage.
- A1 package not modified; corrections are recorded here for Reconciliation.
