# G01 PLATFORM_BASE — RED TEAM Proof Package — `auth_signup`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2 of a two-stage REC + PROOF run) |
| Group / Module | G01 PLATFORM_BASE / `auth_signup` |
| Date | 2026-09-27 |
| Upstream REC | `G01_RECONCILIATION/G01_AUTH_SIGNUP_REC_20260927.md` (36 REC items: MATCH 11, CONTRADICTION 5, UNKNOWN_PENDING_PROOF 17, GAP 3) |
| Inputs (sha256 at intake) | A1 `da32ca50…fe69e`; A2 `e5ce1b56ab35903665d02b3c58d184e2ba334ba72e8d09578ae0ff07f5dd28f9`; Lane A `9470d090…4addfa54`; bank `bf215a34…fade9e2` equals FREEZE_W1-B02; freeze hash `cd966040f720456420057fe98fdb1176fbb9b0e85b456891f4dab82ea3ba0202` |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`, fetched 2026-09-27 15:04:59 UTC (portal / fields.py follow-ups by 15:07:46 UTC); every blob verified with `git hash-object` (section 2) |
| Predeclaration | Scratchpad `rec_asgn_bset/PROOF_CASES_PREDECLARED.md` (shared with `base_setup`), stamped 2026-09-27T15:04:44Z, sha256 `97055575538b3e51678d029d26b1b009984a37e5cdf6fc2cbb09a971577ec01f`. **No source was fetched before this stamp** in this run |
| Runtime device | THPATTARAKRIT-SOLUTION-SERVICE-2.local: **OFFLINE**. Probe 2026-09-27 15:09:20 UTC: `getent hosts` rc=2; HTTP probe to port 8069 → curl rc=6 (could not resolve host) |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** |

Clean-room note: results are neutral paraphrases of observed source behaviour. Identifiers are evidence pointers only. No vendor code is reproduced; nothing recommends reusing vendor schema, ORM, workflow, UI or naming. No percentages. No Formal Coverage claim. No git operations. Inputs were not edited. Source copies are held in the scratchpad only (`rec_asgn_bset/src/`, blob log `rec_asgn_bset/blobs.txt`).

## 1. Case design

- The 12 A2 proof requirements (PR-ASGN-01..12) become **runtime cases PC-ASGN-22..33**, one to one, with procedure, expected and fail condition taken unchanged from A2 §7 and restated in section 4.
- The static prediction basis for every REC item needing proof becomes a **SOURCE / CONFIG static case PC-ASGN-01..21**, predeclared (hash above) and **executed now**.
- A static PASS confirms only that the source reads as predicted. **It is never counted as a result for the linked runtime case.**
- Layers: SRC = module code; SRC(core) = core file at the same anchor; CFG = manifest/data/view/ACL declarations; RT = disposable runtime built from the anchor.

## 2. Blob verification (executed)

| File | Expected blob (Lane A / A2 log) | Computed `git hash-object` | Result |
|---|---|---|---|
| `addons/auth_signup/__manifest__.py` | 99420339… (E1/R1) | 994203390e26eaa1c45eb34014d1487753113851 | MATCH |
| `addons/auth_signup/models/res_users.py` | 1a0280b8… (E8/R2) | 1a0280b8c37a11072caabe7640342b4f3f553514 | MATCH |
| `addons/auth_signup/models/res_partner.py` | 02aab000… (E7/R3) | 02aab00061cebd39df9711fd188ac0c2c681c3dd | MATCH |
| `addons/auth_signup/models/res_config_settings.py` | f72a458d… (E5/R4) | f72a458da9b101fe2fa3f899d3c61330aa4fcfff | MATCH |
| `addons/auth_signup/models/ir_http.py` | fa7cd42c… (E6/R5) | fa7cd42caa7e209d0230b4cbf2dae5068ed1f225 | MATCH |
| `addons/auth_signup/controllers/main.py` | 96d8b71f… (E9/R6) | 96d8b71fe7c987f3007f9bd9f49ab5a12bbc1f6f | MATCH |
| `addons/auth_signup/data/ir_config_parameter_data.xml` | df7690a0… (E10/R7) | df7690a08de224e5fe0869ec64bdb5eb58454900 | MATCH |
| `addons/auth_signup/data/ir_cron_data.xml` | 5824f4a9… (E11/R8) | 5824f4a9941ed914a203e6feea5cece437214cb3 | MATCH |
| `addons/auth_signup/views/res_users_views.xml` | c777d265… (E14/R9) | c777d2650ec4e05b7830aa1fc7b482c8049c64a2 | MATCH |
| `addons/auth_signup/views/auth_signup_login_templates.xml` | 7b15b871… (E15/R10) | 7b15b871b1ca289e904d8a7450a1c775ed7965d9 | MATCH |
| `odoo/tools/misc.py` (core) | 6d275059… (A2 C1) | 6d27505917a80a2cf9d3b3c6faa6bf8bca86acfd | MATCH |
| `odoo/addons/base/models/res_users.py` (core) | 9d42d77a… (A2 C2) | 9d42d77ae8ec19028c99b3c668294569ded3a86a | MATCH |
| `odoo/orm/domains.py` (core) | 63724c20… (A2 C3) | 63724c20d83a5acbbba385eaa43854b8ad3db7e8 | MATCH |
| `odoo/orm/models.py` (core) | 11f50c4e… (A2 C4) | 11f50c4e0b676fbb4b8a45e9703326946348ff98 | MATCH |
| `odoo/addons/base/models/res_config.py` (core) | 50464416… (Lane A E18 / A2 C5) | 504644162d067988dd7d3dcb90cd7e1a065c9fc3 | MATCH |
| `odoo/tools/convert.py` (core) | 9c522c97… (A2 C6) | 9c522c972229704cad61b3050825d476240b9243 | MATCH |
| `addons/web/controllers/home.py` (core) | 292aaa75… (A2 C7) | 292aaa75a2c35b71acb3c97488a6dc2c96309c9f | MATCH |
| `addons/base_setup/models/res_users.py` (cross-module) | ba102d65… (base_setup E6) | ba102d652e5cc2ad3b7af2f9b860897427ae7c23 | MATCH |

18 of 18 blobs match.

## 3. Static cases — executed (SOURCE / CONFIG)

| Case | Layer | Links (REC) | Expected (predeclared) | Fail (predeclared) | Actual (observed, paraphrased; file lines) | Result |
|---|---|---|---|---|---|---|
| PC-ASGN-01 | CFG+SRC | REC-02, REC-03 (C02, C03, X-ASGN-01) | Getter fallback invitation-only; field default free sign-up; seed free sign-up in non-updatable block; uninvited path gated | Any value differs or no gate | Scope reader falls back to the invitation-only value (res_users L88-89). Settings field default is free sign-up (res_config_settings L13-20). Data file sets free sign-up and reset enabled via function calls inside a non-updatable block (data L3-7). Uninvited creation (no partner in values) refused unless scope equals free sign-up (res_users L96-98) | PASS |
| PC-ASGN-02 | SRC(core) | REC-25 (O1/F1 HIGH), REC-03 | Read shows field default when row absent; save writes each parameter-bound field whose stored value differs, absent row counting as different | Save writes only explicitly changed fields, or absent row not written | Settings read takes the stored parameter, falling back to the field default (res_config L264-268). Save reads the stored value with no default (absent → false) and writes the form value whenever it differs (L330-347). A save of any other setting therefore persists free sign-up when the row is missing | PASS |
| PC-ASGN-03 | CFG(core) | REC-04 (C04) | Function calls in non-updatable block skipped outside initial install | Re-executed on upgrade | The data loader returns without evaluating a function tag when the block is non-updatable and the mode is not initial install (convert L272-276) | PASS |
| PC-ASGN-04 | SRC+SRC(core) | REC-05, REC-06, REC-27, REC-28 (C05, C06, O3, O4) | Payload partner/users/last login/type; HMAC scoped, DB-secret keyed, embedded expiry; 4 h / 144 h; zero → no expiry; not encrypted | Stored/encrypted token, or zero expires normally | Token payload lists partner id, its user ids, latest login timestamp and pending type (res_partner L189-190); defaults 4 h reset / 144 h other read from unseeded parameters (L184-188). Signing: HMAC-SHA256 over scope + message, key = database secret parameter, constant-time compare (misc L1781-1810, L1840-1862). Payload is base64 of plain JSON after version, expiry and digest (L1836-1837) — readable, not encrypted. A zero-hour setting leaves the expiry stamp at zero (L1828-1833), and the verifier accepts a zero stamp as never expiring (L1860) | PASS |
| PC-ASGN-05 | SRC | REC-26 (O2) | No per-issue nonce; re-issue changes no bound attribute | Nonce/counter or stored-token invalidation | Re-issue only writes the same pending type (res_partner L113-116; res_users L165). Validity compares only partner, user list, login date and type (res_partner L194-201). No nonce, counter or stored token exists | PASS |
| PC-ASGN-06 | SRC | REC-07 (C07, F5) | Both routes accept any valid token regardless of route; only type-vs-pending compared | Route binds token type | Sign-up route (main L39-48) and reset route with token (L96-97) both call the same sign-up routine (L165-175 → res_users L47-51). Neither passes or checks an expected type. Only the embedded type vs current pending type is compared (res_partner L199). The sign-up route also logs in; the reset route does not | PASS |
| PC-ASGN-07 | SRC | REC-19, REC-29 (C19, O5) | Two named params copied to session; page context falls back to session token | No session fallback | Pre-dispatch copies only `auth_signup_token` and `auth_login` from the query into the session (ir_http L14-18); emailed links use `token` (res_partner L58). Page context uses the session token when the request has none (main L140-141) | PASS |
| PC-ASGN-08 | SRC | REC-11, REC-32 (C11, O7) | Login then e-mail; distinct zero/multiple texts to anonymous caller; no-e-mail error names user | Uniform response | Resolution by login, then case-insensitive e-mail (res_users L135-137); distinct generic exceptions for none/many (L138-141); rendered raw to caller (main L113-114). A matched user without e-mail raises a user error naming the user (res_users L193-194), shown via L108-109. Mail-server failures map to two distinct configuration texts (L150-154) | PASS |
| PC-ASGN-09 | SRC | REC-12 (C12) | Privileged exact-e-mail lookup, non-Invited only, redirect with login | Gated or absent | On both pages, when `signup_email` is present and no POST is processed, an elevated search by exact e-mail restricted to status not Invited returns a redirect carrying that user's login (main L77-80, L116-119). Param is whitelisted (home L27-29) | PASS |
| PC-ASGN-10 | SRC | REC-13, REC-14 (C13, C14) | Archive-inclusive e-mail + login check with disclosing text; template copy; missing template fails | Archive excluded / no template dependency | E-mail check with archive filter off and "already registered" text (res_users L99-101); controller repeats an archive-inclusive login check with the same text (main L69-72). New user = copy of the configured template user; missing template raises (res_users L111-129) | PASS |
| PC-ASGN-11 | SRC(core) | REC-09, REC-10 (C09, C10, X-ASGN-02) | Login date is a related projection of log rows; negative operator falls back to positive + negate | Login date independently stored | Core login date is a related, writable projection of the log rows' creation date (base res_users L233); log order is newest first (L133-135); log GC keeps the latest row per user (L143-151). Module status compute uses login-date truthiness, search uses log-row existence (module res_users L25-35) — same basis. A negative operator not implemented by the search method is resolved by evaluating the inverse and negating (domains L1007-1029); `!=` normalises to `not in` (L1299-1321) | PASS |
| PC-ASGN-12 | SRC | REC-08 (C08) | Model error includes token; public pages pre-validate and show fixed text; output escaped | Raw token reflected unescaped | Model-level error text interpolates the token (res_partner L129). Page context pre-resolves the token; an invalid token yields no info, the resulting failure is caught and replaced by a fixed "invalid token" text, and form processing is skipped because an error is present (main L142-150, L46, L94). Templates render error and message with escaping output (templates L56-57, L75-76, L98-99) | PASS |
| PC-ASGN-13 | SRC(core) | REC-30 (O6) | Whitelist includes error and message | Not whitelisted | Public sign-up parameter whitelist includes `error` and `message` (home L27-29). A present message hides the form (templates L38, L81) | PASS |
| PC-ASGN-14 | SRC | REC-18 (C18) | Write-right check only on single-partner entry; multi builder unchecked | Check on both | Single-partner URL entry runs the builder elevated, then checks model-level write on users (internal targets) or partners (portal targets) other than self (res_partner L29-36). The multi-partner builder has no check (L38-85). A separate internal-or-admin gate protects the auth-param helper (L95-96) | PASS |
| PC-ASGN-15 | SRC | REC-20, REC-33 (C20, O9) | Captcha keys; not-found when disabled and no token; anti-framing headers; no throttling in module | Rate limiting present | Routes declare captcha keys "signup" and "password_reset" (main L39, L87); not-found when feature off and no token (incl. session token) (L43-44, L91-92); frame-ancestor headers set (L83-84, L122-123). No throttling or rate-limit construct in the module controller (search for rate/limit/throttle: only query-size `limit=1` usages) | PASS |
| PC-ASGN-16 | SRC+CFG | REC-21 (C21, F9) | Logging login/user/remote address; action restricted to access-rights managers; method has no explicit gate | Explicit gate in method | Reset attempt logged with requested login, acting user and remote address (main L103-105). Server action bound to users and restricted to the access-rights-manager group (views L36-43). The reset/invite methods carry no group check (res_users L144-230); the pending-type field is restricted to the same group (res_partner L27) and is written without elevation (res_users L165) | PASS |
| PC-ASGN-17 | SRC | REC-15, REC-16, REC-17 (C15–C17) | Login/name dropped; invite on create unless suppressed; mail failure cancels type, user kept; archive/delete cancel | Mail failure rolls back user | Existing-user branch drops login and name; geolocation/lang values dropped when partner has them (res_users L54-65). Create sends a sign-up invite unless suppressed; on mail delivery failure only the pending type is cancelled (L269-280). A wrong-type template returns silently with pending type set (L173-181). Archive and delete cancel pending type (L282-292); archived users rejected for reset/invite (L160-161) | PASS |
| PC-ASGN-18 | CFG+SRC | REC-22 (C22) | Daily, superuser, 5-day window, self-disable | Different cadence/identity | Job: daily interval, runs as root user, calls the reminder with batch 100 (cron L3-12). Reminder: internal users created within the full day five days back, with no log rows and inviter e-mail set; self-deactivates when the template is missing; no resend tracking (res_users L232-258) | PASS |
| PC-ASGN-19 | SRC (cross-module) | REC-23, REC-31 (C23, O8) | Re-invite search on still-Invited runs before reactivation with default active filter → reactivated users get no invite | Reactivated users included | auth_signup bulk invite first searches still-Invited users with default (active-only) filtering, removes their e-mails, delegates the rest, then re-invites only the found set (res_users L260-267). base_setup reactivates archived matches by setting active (base_setup res_users L20-24) — a write, which does not pass through the create-time invitation hook (auth_signup res_users L269-280) | PASS |
| PC-ASGN-20 | CFG | REC-01 (C01) | Auto-install; deps base_setup/mail/web; no ACL/rule files | Security files present | Manifest: auto-install and bootstrap on; depends on base_setup, mail, web; data list has no ACL or record-rule file (manifest L7-27) | PASS |
| PC-ASGN-21 | SRC | REC-24 (C24, X-ASGN-03) | Random helper unused; flags accepted, always raises | Helper used / flags honoured | The 20-character random helper is defined (res_partner L15-18) and referenced nowhere else in the fetched module files. The retrieval method accepts validity/raise flags and raises on any invalid token regardless (L118-130) | PASS |

**Static totals: 21 executed — PASS 21, FAIL 0.** No failed static result exists to preserve.

### 3.1 Refinements observed (for A3; they do not change any verdict)

- R1 (PC-06): reset and enrollment links are interchangeable **across routes**, but a link still verifies only while the partner's current pending type equals the embedded type. Issuing a reset after an enrollment invite (type change) invalidates the outstanding enrollment link, and vice versa.
- R2 (PC-12): the fixed "invalid token" text on public pages is produced by catching a failure that occurs when the token-info lookup returns nothing; it is an incidental catch-all, not an explicit validation branch.
- R3 (PC-01/PC-09): the public parameter whitelist also includes `partner_id`, but the sign-up value builder keeps only login, name and password (main L153-163), so it cannot reach the uninvited-path gate. Consistent with A2 C02.
- R4 (PC-11): the login-date field is declared writable; a direct write would alter the newest log row's creation date. This is the only residual divergence path for X-ASGN-02, and it is runtime/customisation-dependent.

## 4. Runtime cases — NOT-EXECUTED (runtime unavailable)

Common preconditions: a disposable database built from the anchored source (`8d05257d…`) with `auth_signup` and its dependencies installed, a controllable outgoing mail server (capture sink), no captcha provider module unless stated, and named test users. Record verbatim outcomes. Status for all: **NOT-EXECUTED — runtime device THPATTARAKRIT-SOLUTION-SERVICE-2.local OFFLINE (probe 2026-09-27 15:09:20 UTC)**. Ready to run as written; no result is claimed.

| Case | Layer | Links (REC) | Steps (ready to run; A2 PR procedure) | Expected | Fail condition | Status |
|---|---|---|---|---|---|---|
| PC-ASGN-22 | RT | PR-ASGN-01; REC-03, REC-25 | Delete the scope parameter row; open General Settings; anonymously GET the sign-up page; then save an unrelated setting and re-request | Settings shows free sign-up; page not-found; after save, row = free sign-up and page available | Page available while row absent, or save does not recreate row | NOT-EXECUTED |
| PC-ASGN-23 | RT | PR-ASGN-02; REC-04 | Set scope to invitation-only; upgrade the module; read the row | Row unchanged | Row reverts to free sign-up | NOT-EXECUTED |
| PC-ASGN-24 | RT | PR-ASGN-03; REC-11, REC-32 | Anonymous reset with unknown id, duplicate-matching id, matched user lacking e-mail, valid id | Four distinguishable responses; third names the user | Responses indistinguishable | NOT-EXECUTED |
| PC-ASGN-25 | RT | PR-ASGN-04; REC-12 | Anonymous GET of sign-up and reset pages with e-mail of a confirmed user and of an invited user | Redirect with login for confirmed; none for invited | No redirect for confirmed, or redirect for invited | NOT-EXECUTED |
| PC-ASGN-26 | RT | PR-ASGN-05; REC-05, REC-26 | Consume a reset link and replay it; separately issue two reset links without use and test the first | Replay rejected; first of two still valid | Replay accepted, or first link rejected | NOT-EXECUTED |
| PC-ASGN-27 | RT | PR-ASGN-06; REC-07 | Submit an enrollment link to the reset route and a reset link to the sign-up route (pending type matching each) | Both accepted; sign-up route logs in, reset route does not | Either rejected by type | NOT-EXECUTED |
| PC-ASGN-28 | RT | PR-ASGN-07; REC-27 | Set reset validity to zero; issue link; test after the default window | Link still valid | Link rejected as expired | NOT-EXECUTED |
| PC-ASGN-29 | RT | PR-ASGN-08; REC-08, REC-30 | Anonymous pages with an invalid token and with crafted `error` / `message` params | Fixed invalid-token text, submitted value not echoed; crafted texts shown escaped | Token echoed on public page, or unescaped rendering | NOT-EXECUTED |
| PC-ASGN-30 | RT | PR-ASGN-09; REC-19, REC-29 | Visit any page with the signup-token param; later open the sign-up page without a token in the same session | Page context uses the session token | Session token ignored | NOT-EXECUTED |
| PC-ASGN-31 | RT | PR-ASGN-10; REC-20, REC-33 | No captcha provider installed; burst anonymous reset / sign-up requests | No throttling observed in this module path | Throttling observed (then locate enforcing layer) | NOT-EXECUTED |
| PC-ASGN-32 | RT | PR-ASGN-11; REC-21 | Internal non-manager invokes reset/invite on another user via RPC | Denied (field restriction) | Mail sent / pending type written | NOT-EXECUTED |
| PC-ASGN-33 | RT | PR-ASGN-12; REC-16 | Mail server unavailable; create a user with e-mail | User exists, status Invited, no pending type, resend available to admin | User creation rolled back, or pending type left set | NOT-EXECUTED |

**Runtime totals: 12 cases — NOT-EXECUTED 12, PASS 0, FAIL 0.**

## 5. Summary of results

| Layer | Cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| SRC (module, incl. cross-module PC-19) | 12 (PC-05..10, PC-12, PC-14, PC-15, PC-17, PC-19, PC-21) | 12 | 0 | 0 |
| SRC(core) / CFG(core) (incl. mixed PC-04) | 5 (PC-02, PC-03, PC-04, PC-11, PC-13) | 5 | 0 | 0 |
| CFG / CFG+SRC | 4 (PC-01, PC-16, PC-18, PC-20) | 4 | 0 | 0 |
| RT | 12 (PC-22..33) | 0 | 0 | 12 |
| **Total** | **33** | **21** | **0** | **12** |

REC item status after Proof:
- 5 CONTRADICTION items (C03, C08, C09, C18, C19): the A2 side (or, for C03, the source-internal split) is **source-confirmed**. They remain CONTRADICTION for A3; practical effect pending for C03 (PC-22), C08 (PC-29), C19 (PC-30). C09 and C18 have no runtime case in A2; A3 may request one.
- 17 UNKNOWN_PENDING_PROOF items: static basis confirmed for all; **all remain UNKNOWN_PENDING_PROOF** until runtime runs. O4 (REC-28) has no runtime case in A2 (clone/secret behaviour) — flagged for A3.
- 11 MATCH items unchanged. 3 GAP items carried forward.

## 6. A3 eligibility

**Disposition: PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.**

A3 can challenge **now** (static scope):
1. REC classifications and counts (36 items), including C03 as source-vs-intent CONTRADICTION rather than MATCH, the fold-ins (G1/G2/G3/G6/G7/G8/G9, F5/F9/F10), and the treatment of X-ASGN-02 as paper-only.
2. The 21 executed static cases PC-ASGN-01..21: falsifiability of each expected/fail pair, sufficiency of the observations, and refinements R1–R4.
3. The HIGH finding O1 (REC-25): whether the static reading of the settings save routine is complete (e.g., client-side dirty-field handling in the web client, not read here).
4. The cross-module bulk-invite interaction (PC-19) shared with base_setup REC-BSET-24/25.
5. QID lineage (24 mapped, 16 no evidence yet), join key and freeze hash, clean-room compliance, input integrity and predeclaration timing (stamp precedes first fetch).

**Blocked** until the runtime device is available:
- All 12 runtime cases PC-ASGN-22..33 — in particular the policy exposure from a settings save (PC-22), link replay/reissue/zero-validity (PC-26, PC-28), cross-route substitution (PC-27), anonymous enumeration (PC-24, PC-25) and session-token reuse (PC-30).
- Closing any UNKNOWN_PENDING_PROOF item or settling the practical effect of any CONTRADICTION item. A full A3 → MASTER handoff is **not** eligible yet; this package is eligible for **A3 static-scope challenge only**.

## 7. Limitations

- No runtime executed; no runtime result claimed. Static PASS confirms source readings only.
- Web-client JS (which fields a settings save sends), captcha provider modules, CSRF defaults, session rotation on authentication and redirect sanitisation were not read (REC-34..36).
- Other installed modules may override any method read here.
- No percentages, no Formal Coverage claim, no git operations. Inputs not edited.
