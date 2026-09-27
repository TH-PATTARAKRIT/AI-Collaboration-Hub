# G01 PLATFORM_BASE — RED TEAM A1 PACKAGE — `base_setup`

| Item | Value |
|---|---|
| Role | RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `base_setup` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_BASE_SETUP_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `59d3d312c3f5bff8dba13b24bb66a648f357b418677a9e74f242d0929f6ae4ce` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (paths under `addons/`) |
| Topic lens (not answered) | `GMVQ/G01_PLATFORM_BASE/G01_BASE_SETUP_GMVQ_MVQ_40_V1.00_DRAFT.md` — batch W1-B04, freeze_hash `9e31f2d27dfb959e555cf8ff117d829969e8122fe5e5544bbaf737b6ddea0377`, bank sha256 `21611846…26d62` (matches freeze record), ELIGIBLE |
| Lane B | Not consumed; A1 does not wait for Lane B |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Clean-room: all statements are neutral WHAT / WHY / RISK abstractions. Identifiers are evidence pointers only. Nothing here recommends reuse of reference schema, ORM, workflow or UI. No QID is answered; bank used only as a topic lens.

## 1. Claims

Evidence IDs (E#) refer to the Lane A pointer table; blob = git blob SHA-1. Layer for all claims: SOURCE-STATIC.

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence (path, blob) | Conf. |
|---|---|---|---|
| A1-G01-BSET-C01 | WHAT: module is the general-settings anchor for initial setup; auto-installs with base/web; ships no ACL/record-rule files. WHY: other modules (e.g. auth_signup) extend its settings surface. | E1 `base_setup/__manifest__.py` 92ae94dd…; E12 | HIGH |
| A1-G01-BSET-C02 | WHAT: general-settings menu is restricted to system administrators; some blocks further restricted to developer mode or multi-company groups. | E12 `views/res_config_settings_views.xml` f97b9b25… | HIGH |
| A1-G01-BSET-C03 | RISK: several settings fields are company-related pass-throughs (report footer, layout, company identity); saving settings writes to the company record, not only to a parameter store. | E5 `models/res_config_settings.py` 7de29781… (spot-checked) | MED |
| A1-G01-BSET-C04 | WHAT: optional capabilities are exposed as install toggles; install/uninstall mechanics live in base settings machinery, not in this module. | E5 (spot-checked); gap G3 | MED |
| A1-G01-BSET-C05 | WHAT: opening "default access for new users" creates the governing group on demand if absent and registers it as non-updatable data before opening it. WHY: this group determines rights of newly created internal users. RISK: silent creation by a UI action. | E5 7de29781… (spot-checked) | HIGH |
| A1-G01-BSET-C06 | WHAT: bulk invite normalises e-mails, reactivates archived users matching by login or normalised e-mail (instead of duplicating) and creates new users with login = normalised e-mail and a prepared enrollment link. | E6 `models/res_users.py` ba102d65… (spot-checked) | HIGH |
| A1-G01-BSET-C07 | RISK: reactivation in bulk invite only flips the active flag; no change of prior group membership is evident in the module. Previously held rights may be restored on reactivation. | E6 ba102d65… (spot-checked) | MED |
| A1-G01-BSET-C08 | WHAT: bulk invite fails closed with a user-facing error when the normalised-e-mail capability (Discuss/mail layer) is absent. | E6 ba102d65… (spot-checked) | HIGH |
| A1-G01-BSET-C09 | WHAT: dashboard data route requires an authenticated session and explicitly checks the access-rights-manager group before returning active and pending internal-user counts plus up to 10 pending user ids/logins. | E9 `controllers/main.py` cce2c3f7… (spot-checked) | HIGH |
| A1-G01-BSET-C10 | WHAT: "pending" is defined as an active internal user with no login-log record. WHY: consistent with auth_signup's status search basis, not with its status compute basis (see auth_signup X-ASGN-02). | E9 cce2c3f7… (spot-checked) | HIGH |
| A1-G01-BSET-C11 | WHAT: demo-status route requires an authenticated session but performs no explicit group check; any logged-in user (including non-admin, if the session type permits) can learn whether demo data is active. | E9 cce2c3f7… (spot-checked) | HIGH |
| A1-G01-BSET-C12 | WHAT: settings active-user counter counts non-share users with no explicit active filter in its condition; dashboard route filters active explicitly. Whether archived users are excluded in the counter depends on core default archive filtering (not fetched). | E5 7de29781…, E9 cce2c3f7… (spot-checked) | MED |
| A1-G01-BSET-C13 | WHAT: KPI summary route is unauthenticated (no session, no session save) and accepts a list of [database, API key] pairs, rejecting lists above 500. | E10 `controllers/kpi.py` 69c9c21c… (spot-checked) | HIGH |
| A1-G01-BSET-C14 | WHAT: each database is evaluated independently: skipped if not found, if its base version series differs from the running server, or if the key fails remote-call-scoped verification. Skipped databases are silently omitted. WHY: explicit anti-enumeration intent. | E10 69c9c21c… (spot-checked) | HIGH |
| A1-G01-BSET-C15 | RISK: for any database whose key verifies, the response includes the full list of active internal users (id, name, login, last-login timestamp). No group/role check on the key's owner is performed in the module; any user holding a valid remote-call key appears sufficient. | E10 69c9c21c… (spot-checked) | HIGH |
| A1-G01-BSET-C16 | WHAT: KPI providers are rolled back after each call (outside tests); provider exceptions are captured into an errors list (addon, provider, message) rather than aborting the summary. Per-database exceptions are logged and omitted. | E10 69c9c21c… (spot-checked) | HIGH |
| A1-G01-BSET-C17 | RISK: providers are discovered by manifest declaration and dynamically imported; any installed addon can inject code into the unauthenticated KPI path. Discovery result cached per worker. | E10 | MED |
| A1-G01-BSET-C18 | WHAT: abstract KPI provider exposes an empty summary hook for extension. | E8 `models/kpi_provider.py` 4211916c… | HIGH |
| A1-G01-BSET-C19 | WHAT: a visual-effect flag is seeded (non-updatable, not force-created) and emitted to internal-user sessions only. | E7 4e7bb7df…, E11 e0d02590… | MED |
| A1-G01-BSET-C20 | WHAT: profiling-enable-until is a settings-bound parameter; expiry enforcement lives outside this module. | E5 (spot-checked); gap G7 | LOW |
| A1-G01-BSET-C21 | WHAT: company/user/language counters run privileged across all companies (not scoped to the current company). RISK: system-wide counts may be read as company-specific. | E5 7de29781… (spot-checked) | MED |
| A1-G01-BSET-C22 | WHAT: no scheduled jobs in the module. | E1 | HIGH |

## 2. Business rules (source-static)
- BR1 Settings surface is admin-only by menu restriction; data route re-checks group server-side (C02, C09).
- BR2 Bulk invite never duplicates an archived matching identity; it reactivates it (C06).
- BR3 KPI access per database requires a valid remote-call-scoped key for that database; one key does not unlock another (C14).
- BR4 KPI request size bounded at 500 pairs (C13).
- BR5 KPI providers must be side-effect free; enforced by rollback (C16).

## 3. States / transitions
- Internal user (dashboard view): active + no login log = pending → first login log = active (C10).
- Archived user → active via bulk invite reactivation (C06, C07).
- Default-access group: absent → created on first open → persistent non-updatable (C05).

## 4. Exceptions / failure modes
- Missing Discuss layer → bulk invite error (C08).
- Non-manager calling dashboard data → access denied (C09).
- More than 500 credential pairs → validation error (distinct from silent omission) (C13).
- Unknown DB / version mismatch / bad key → silent omission, server-side log (C14).
- Provider failure → error entry in response; other providers continue (C16).
- No external layout set → layout edit action returns nothing (Lane A #11).

## 5. Cross-module handoffs
- `auth_signup`: extends settings form, dashboard data (resend flag) and bulk invite (re-invite); enrollment links/mails originate there.
- `base`: settings machinery (toggles, implied groups, parameter binding), groups, API-key verification helper, user/company/language actions.
- `web`: document layout configurator, report preview.
- `mail`/Discuss: normalised e-mail prerequisite.
- Any addon declaring KPI providers (injection point into C17 path).

## 6. Evidence gaps (carried from Lane A + A1)
- G1 Active-user count basis (see X-BSET-02 — CANDIDATE, depends on core default archive filtering).
- G2 Controller-level cursor binding in core not verified.
- G3 Base settings machinery not analysed.
- G4 API-key verification helper and manifest loader not fetched (which users may hold rpc-scoped keys; key expiry).
- G5 Static JS (invite widget) not reviewed.
- G6 Demo-status route exposure beyond logged-in users not implied.
- G7 (A1) Profiling expiry enforcement location not identified.
- G8 (A1) Group-membership effect of reactivation not evidenced beyond the active flag.

## 7. CRQ candidates (runtime / proof required)
| CRQ | Question for proof | Links |
|---|---|---|
| CRQ-BSET-01 | With a valid rpc key of a low-privilege (or portal, if permitted) user, does KPI summary return the internal user list? | C15, G4 |
| CRQ-BSET-02 | Does KPI summary reveal DB existence through timing or through the 500-pair error path? | C13, C14 |
| CRQ-BSET-03 | Can a non-admin internal user call demo-status successfully? | C11 |
| CRQ-BSET-04 | Do settings counter and dashboard active count differ when archived internal users exist? | C12 |
| CRQ-BSET-05 | Does bulk-invite reactivation restore prior group memberships? | C07, G8 |
| CRQ-BSET-06 | Does a settings save by a multi-company admin alter another company's layout/footer? | C03 |
| CRQ-BSET-07 | Can an addon's KPI provider produce a durable side effect despite rollback? | C16, C17 |
| CRQ-BSET-08 | Is the default-access group creation audited and attributable? | C05 |

## 8. Contradictions
| ID | Contradiction | Classification |
|---|---|---|
| X-BSET-01 | Demo-status route has no group check while sibling dashboard route enforces manager group | CONFIRMED-FROM-SOURCE (E9 re-fetched, verified) |
| X-BSET-02 | Active-user count: settings counter lacks explicit active filter; dashboard route filters active | CANDIDATE — literal difference verified, but core default archive filtering (not fetched) may make results equal |
| X-BSET-03 | "Last login" in KPI output derives from login-log records, while auth_signup status compute uses a login-date field | CANDIDATE — cross-module; depends on how the login-date field is populated in base (not fetched) |

## 9. Spot-check log
Method: `curl` raw file at anchor → `git hash-object` → compare with Lane A blob → inspect for claim text. Fetch copies kept in scratchpad only.

| # | Path | Lane A blob | Re-computed blob | Match | Claim verified |
|---|---|---|---|---|---|
| S1 | base_setup/controllers/kpi.py | 69c9c21c1aa03bb90589d7c56f5c5b9bee6fe3e8 | 69c9c21c1aa03bb90589d7c56f5c5b9bee6fe3e8 | YES | Unauthenticated, no session save; 500-pair bound; version/key checks with silent omission; rpc-scoped key; per-provider rollback; returns internal users with id/name/login/last login — VERIFIED; no role check on key owner — A1 refinement (C15) |
| S2 | base_setup/controllers/main.py | cce2c3f7609f7659ca0e034ba4e34a10014f4b32 | cce2c3f7609f7659ca0e034ba4e34a10014f4b32 | YES | Data route manager-group check + active filter + pending via no login log, limit 10 — VERIFIED; demo-status no group check — VERIFIED |
| S3 | base_setup/models/res_config_settings.py | 7de297811c8722411552e9bdc4ba12b1d2201029 | 7de297811c8722411552e9bdc4ba12b1d2201029 | YES | Active-user counter: privileged, non-share condition only, no explicit active term — VERIFIED (divergence effect not verified, see X-BSET-02); default-group on-demand creation — VERIFIED |
| S4 | base_setup/models/res_users.py | ba102d652e5cc2ad3b7af2f9b860897427ae7c23 | ba102d652e5cc2ad3b7af2f9b860897427ae7c23 | YES | Normalisation, archived reactivation by login/normalised e-mail, Discuss prerequisite error, create with prepared link context — VERIFIED |

Result: 4/4 blobs match; no Lane A claim refuted. Lane A #10 ("does not filter on active flag") downgraded from implied divergence to CANDIDATE pending core ORM evidence.

## 10. Provenance
- Input: Lane A packet (sha256 above), evidence E1–E13 at anchor commit.
- Spot-check fetches: `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/<path>`, 2026-09-27.
- Topic lens: frozen bank W1-B04 (read only, not edited, no QID answered).
- No Lane B material consulted.

## 11. Limitations
- Source presence ≠ runtime reachability; every claim is SOURCE-STATIC.
- No Formal Coverage claim; claim count is not a denominator.
- Single anchor commit; no version comparison.
- Core helpers (settings machinery, API-key check, ORM archive filtering) not fetched — see gaps.
