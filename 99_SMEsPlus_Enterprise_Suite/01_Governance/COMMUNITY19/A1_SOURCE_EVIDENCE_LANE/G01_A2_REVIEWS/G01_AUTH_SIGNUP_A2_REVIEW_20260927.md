# G01 PLATFORM_BASE — RED TEAM A2 REVIEW — `auth_signup`

| Item | Value |
|---|---|
| Role | RED TEAM A2 (functional / semantic verifier of A1 conclusions) — independent of A1; A1 package not repaired |
| Group / Module | G01 PLATFORM_BASE / `auth_signup` |
| A1 package | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_AUTH_SIGNUP_A1_PACKAGE_20260927.md` |
| A1 package sha256 | `da32ca500989cf1befc9d48dc689c6ad6ee447705f1054e50226ee93ac0fe69e` |
| Upstream Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_AUTH_SIGNUP_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `9470d090c3ed164634954ae0cb0cfe0d5ae92fb981d51a0a4fc3ccaa4addfa54` (matches value recorded in A1 header) |
| Topic lens (not answered) | `GMVQ/G01_PLATFORM_BASE/G01_AUTH_SIGNUP_GMVQ_MVQ_40_V1.00_DRAFT.md`, batch W1-B02, ELIGIBLE; sha256 `bf215a348a6efdb3fe0a171589fa9705832655a5f00c44f0b54c49c4cfade9e2` (matches A1 header prefix/suffix) |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Lane B | None in repository for this module — see §6 |
| Date | 2026-09-27 |
| Disposition | **A2 PASS WITH FINDINGS** |

Clean-room: statements are neutral WHAT / WHY / RISK abstractions; identifiers and line numbers are evidence pointers only; no reference code is reproduced; no QID is answered; no percentage and no Formal Coverage claim.

## 1. Test plan (predeclared before verdicts)

| # | Test | Method | Pass condition |
|---|---|---|---|
| T1 | Lineage | sha256 of A1 package, Lane A packet, bank; compare with A1 header | Hashes consistent |
| T2 | Blob re-fetch | Re-fetch every file cited by HIGH or contradiction claims at the anchor; `git hash-object`; compare with Lane A blob | All blobs match |
| T3 | Independent semantic re-read | Read the full text of re-fetched module files (not A1 excerpts) and restate behaviour in own words before comparing with A1 | Claim meaning matches source meaning |
| T4 | Core gap settlement | For HIGH / contradiction items resting on core behaviour, fetch the core file at the anchor and record blob: signing helper, login-date field basis, domain negation, default archive filtering, settings save semantics, data-file function tags, request-param whitelist | Gap either settled or explicitly left open |
| T5 | Mandated focus items | Scope default b2c vs b2b fallback; status computed vs searched; account enumeration; token echo; token signing | Each gets an explicit verdict and a business-meaning note |
| T6 | Business-meaning review | SaaS identity / onboarding lens: self-registration policy, identity uniqueness, credential lifecycle, disclosure, recoverability | Overclaims and omissions listed |
| T7 | Lane B classification | Search repo for Lane B material for this module | Classified NOT_APPLICABLE / UNCORROBORATED, never FAIL |
| T8 | Proof requirements | Only for inherently runtime claims; each falsifiable with expected result and fail condition | Listed in §7 |

### T1/T2/T4 evidence (re-fetch log, 2026-09-27)

| # | Path (anchor) | Blob (git hash-object) | vs Lane A |
|---|---|---|---|
| R1 | addons/auth_signup/__manifest__.py | 994203390e26eaa1c45eb34014d1487753113851 | MATCH E1 |
| R2 | addons/auth_signup/models/res_users.py | 1a0280b8c37a11072caabe7640342b4f3f553514 | MATCH E8 |
| R3 | addons/auth_signup/models/res_partner.py | 02aab00061cebd39df9711fd188ac0c2c681c3dd | MATCH E7 |
| R4 | addons/auth_signup/models/res_config_settings.py | f72a458da9b101fe2fa3f899d3c61330aa4fcfff | MATCH E5 |
| R5 | addons/auth_signup/models/ir_http.py | fa7cd42caa7e209d0230b4cbf2dae5068ed1f225 | MATCH E6 |
| R6 | addons/auth_signup/controllers/main.py | 96d8b71fe7c987f3007f9bd9f49ab5a12bbc1f6f | MATCH E9 |
| R7 | addons/auth_signup/data/ir_config_parameter_data.xml | df7690a08de224e5fe0869ec64bdb5eb58454900 | MATCH E10 |
| R8 | addons/auth_signup/data/ir_cron_data.xml | 5824f4a9941ed914a203e6feea5cece437214cb3 | MATCH E11 |
| R9 | addons/auth_signup/views/res_users_views.xml | c777d2650ec4e05b7830aa1fc7b482c8049c64a2 | MATCH E14 |
| R10 | addons/auth_signup/views/auth_signup_login_templates.xml | 7b15b871b1ca289e904d8a7450a1c775ed7965d9 | MATCH E15 |
| C1 | odoo/tools/misc.py (signing / HMAC helpers) | 6d27505917a80a2cf9d3b3c6faa6bf8bca86acfd | A2 core read (A1 gap G3) |
| C2 | odoo/addons/base/models/res_users.py (login-date field, log model, login/e-mail domain helpers) | 9d42d77ae8ec19028c99b3c668294569ded3a86a | A2 core read (A1 gaps G2, G4) |
| C3 | odoo/orm/domains.py (operator normalisation, search-method negation fallback) | 63724c20d83a5acbbba385eaa43854b8ad3db7e8 | A2 core read (A1 gap G7) |
| C4 | odoo/orm/models.py (default archive filter in search) | 11f50c4e0b676fbb4b8a45e9703326946348ff98 | A2 core read |
| C5 | odoo/addons/base/models/res_config.py (settings read default / save) | 504644162d067988dd7d3dcb90cd7e1a065c9fc3 | MATCH Lane A E18 |
| C6 | odoo/tools/convert.py (data-file function tag in noupdate) | 9c522c972229704cad61b3050825d476240b9243 | A2 core read |
| C7 | addons/web/controllers/home.py (public request-param whitelist) | 292aaa75a2c35b71acb3c97488a6dc2c96309c9f | A2 core read |

Result: 10/10 module blobs match Lane A; lineage consistent. Scratch copies only in session scratchpad.

## 2. Claim verdict table

Verdict key: VERIFIED = source meaning matches claim; PARTIAL = core statement holds but scope, mechanism or implied risk is over- or under-stated; NOT_VERIFIED = source contradicts or cannot support; OUT_OF_SCOPE = not decidable in source layer. "Re-read" = independent semantic re-read performed (all HIGH and all contradiction/CRQ items).

| Claim | A1 conf. | Re-read | Verdict | A2 basis (own restatement) |
|---|---|---|---|---|
| C01 | HIGH | Y | VERIFIED | R1: auto-install, deps setup/mail/web, data list has no ACL or record-rule files. |
| C02 | HIGH | Y | VERIFIED | R2 L95-98: uninvited path (no partner in values) refused unless scope value is exactly "free sign-up"; any other or absent value refuses. Public form values cannot inject a partner (R6 L153-163 take only login/name/password/lang). |
| C03 | HIGH | Y | VERIFIED (strengthened) | R2 L88-89 fallback "invitation only"; R4 default "free sign-up"; R7 seed "free sign-up"; C5 L268: settings read shows field default when row absent. Additional effect found — see F1: any later settings save persists "free sign-up". |
| C04 | HIGH | Y | VERIFIED | R7 seeds are function calls inside a noupdate block; C6 L272-274: such calls are skipped in any mode other than initial install. Re-install re-runs them. |
| C05 | HIGH | Y | VERIFIED (with omissions F2-F4) | R3 L171-200: token = signed payload of partner, its user list, latest login timestamp, pending type; nothing stored; R2 L49-51 clears pending type on use → replay fails. C1 L1812-1862: HMAC-SHA256 keyed on the database secret, scope-separated, constant-time compare, embedded expiry. Payload is signed, not encrypted. |
| C06 | HIGH | Y | VERIFIED (edge F3) | R3 L184-188 defaults 4 h reset / 144 h other; params not seeded (R7). Edge: a zero value yields a non-expiring token (C1 expiry-0 semantics). |
| C07 | MED | Y | VERIFIED; A1 gap G8 settled | Shared scope "signup"; validity compares embedded type with current pending type only. R2 `signup` and R6 L96-97 / L48 do not bind token type to route: either token type is consumable on either route (sign-up route additionally logs in). See F5. |
| C08 | MED | Y | PARTIAL | Echo exists in the model-layer error text (R3 L129). But the public pages pre-validate any token while building the page context (R6 L142-150) and replace failures with a fixed "invalid token" text, so the echo is reachable from public routes only if a token becomes invalid between page-context build and submit; output is escaped (R10 uses escaping output). RISK is overstated as a public reflected-input surface. Separately, `error`/`message` request params are whitelisted (C7 L27-29) and rendered (escaped) — see F6. |
| C09 | HIGH | Y | PARTIAL (contradiction X-ASGN-02 semantically refuted) | Literal difference true (compute = login-date presence; search = log-row existence). C2 L233: the login-date field is itself a related projection of the log rows' creation date, and log GC (C2 L143-151) keeps the latest row per user. Both bases therefore resolve to "has at least one log row". The asserted RISK (filter vs displayed status disagree) is not supported by source; residual only via direct write to the (writable) related field — runtime-confirmable, low. |
| C10 | MED | Y | VERIFIED; A1 gap G7 settled | C3 L1299-1321: "!=" is normalised to "not in"; C3 L1007-1029: when the field search returns "not implemented" for a negative operator, core evaluates the positive operator and negates. "Not Invited" therefore resolves to "has log rows". |
| C11 | HIGH | Y | VERIFIED (extended F7) | R2 L135-141: login match first, then e-mail (case-insensitive exact); zero / multiple raise distinct texts; R6 L113-114 render the raw text to the anonymous caller. Success text also differs. Extension: a matched user without e-mail yields an error naming that user (R2 L193-194 via R6 L108-109). Archived users are excluded by default archive filtering (C4 L5370-5375) and appear as "no account". |
| C12 | HIGH | Y | VERIFIED | R6 L77-80 / L116-119: privileged lookup by exact e-mail restricted to non-Invited users; redirect carries that user's login. Param is whitelisted (C7). Reachable on sign-up page when free sign-up is on, and on reset page when reset is on (both on by default seed). Invited users are not disclosed, so the response also reveals "has logged in at least once". |
| C13 | HIGH | Y | VERIFIED (scope note) | R2 L99-101 archive-inclusive e-mail check with disclosing text; R6 L68-72 adds an archive-inclusive login check with the same text. Scope note: the check applies to every new-user creation through this helper, i.e. also invited partners without a user, not only uninvited registration. |
| C14 | HIGH | Y | VERIFIED (scope note) | R2 L111-129: copy of configured template user; missing template → failure; login collision surfaces as sign-up error. Applies to invited-partner creation too. |
| C15 | MED | Y | VERIFIED (scope note) | R2 L54-65: login/name dropped for existing user; geolocation/lang protection applies in both existing-user and new-user branches. |
| C16 | MED | Y | VERIFIED | R2 L269-280. Also: a wrong-type template makes the send path return silently with pending type left set (R2 L173-181). |
| C17 | MED | Y | VERIFIED | R2 L160-161, L282-292. |
| C18 | HIGH | Y | PARTIAL | R3 L29-36: the right check is model-level write permission (no record-level test) and exists only on the single-partner URL entry point; the multi-partner URL builder (R3 L38-85) has no check and is invoked privileged by mail flows. A separate gate (internal user or admin) protects the auth-param helper (R3 L90-96). Claim generalises one entry point to "link generation". |
| C19 | MED | Y | PARTIAL | R5: only two named params (signup-token and login) are copied, not the `token` param used in emailed links. Omitted consequence: the public pages fall back to the session-stored token when none is supplied (R6 L140-141) — see F8. |
| C20 | HIGH | Y | VERIFIED (nuance) | R6 L39-44, L87-92, headers L83-84 / L122-123. Nuance: "no link supplied" includes the session-stored token fallback. Captcha enforcement is outside the module. |
| C21 | HIGH | Y | VERIFIED (nuance F9) | R6 L103-105 logs requested login, acting user, remote address; R9 L35-42 server action bound to access-rights managers. The underlying method itself carries no group gate; protection for other callers is indirect (pending-type field restricted to the same group, R3 L27). |
| C22 | MED | Y | VERIFIED | R2 L232-258, R8: daily, superuser; window is the full calendar day five days back; requires inviter e-mail; self-disables; no resend tracking. |
| C23 | MED | Y | VERIFIED (interaction note) | R2 L260-267. Interaction: the re-invite search runs before base_setup's reactivation and uses default archive filtering, so reactivated archived users receive no invitation (cross-ref base_setup A2 F4). |
| C24 | HIGH | Y | VERIFIED | R3 L15-18 helper unused in fetched files; R3 L119-130 flags accepted but behaviour always raises. |

Verdict counts: VERIFIED 20, PARTIAL 4 (C08, C09, C18, C19), NOT_VERIFIED 0, OUT_OF_SCOPE 0. Total 24.

Contradiction re-classification (A2 view; A1 table not edited):

| ID | A1 class | A2 result |
|---|---|---|
| X-ASGN-01 scope default | CONFIRMED-FROM-SOURCE | CONFIRMED; impact larger than stated (F1) |
| X-ASGN-02 status basis | CONFIRMED-FROM-SOURCE | Literal only; semantic divergence REFUTED by core (C2 L233) |
| X-ASGN-03 retrieval flags | CONFIRMED-FROM-SOURCE | CONFIRMED; no behavioural consequence observed (only caller passes raising flags) |

## 3. Semantic findings (business meaning — SaaS identity / onboarding)

- **F1 (HIGH, extends C03).** When the scope parameter row is absent, the settings screen displays "free sign-up" (field default) while runtime enforces "invitation only". Because the settings save routine writes every bound parameter whose stored value differs from the displayed value (C5 L330-347), any unrelated General Settings save by an administrator silently persists "free sign-up" and opens public self-registration. Business meaning: a tenant-wide exposure change can be caused by an unrelated administrative action with no explicit decision. For SMEsPlus, the effective default must have one authoritative value across display, storage and enforcement.
- **F2 (MED, omission on C05).** Re-issuing a link of the same type does not invalidate an earlier unused link of that type; the binding attributes (partner, user list, last login, type) are unchanged. Multiple reset links can therefore be simultaneously valid until expiry or first login. Relevant to the bank's "resend rule" topic.
- **F3 (MED, edge on C06).** A validity parameter set to zero produces a link with no expiry (signing helper treats zero as "never expires"). A non-integer value causes an error at link generation. No validation exists in the module.
- **F4 (LOW-MED, omission on C05).** The token payload is signed but not encrypted: partner id, user ids, last-login timestamp and type are readable by anyone holding the link. The key is the per-database secret shared across all signing scopes (scope-separated). A copied database that keeps the same secret would accept the original's links — cross-environment question for proof.
- **F5 (MED, settles G8/C07).** Enrollment and recovery links are interchangeable across routes; only the sign-up route logs the user in. The bank topic "enrollment credentials cannot be substituted for recovery credentials" is not enforced by route in this module.
- **F6 (LOW-MED, new).** The public request-param whitelist includes `error` and `message`; both are rendered on sign-up/reset pages (escaped), and a present `error` suppresses form processing while `message` hides the form. Enables content spoofing on a trusted login surface (no script injection evidenced).
- **F7 (MED, extends C11).** Beyond "no account" vs "multiple accounts", the anonymous reset path can disclose a matched user's display name (user without e-mail) and mail-server configuration state (delivery-failure texts). Sign-up path renders raw exception text after a generic prefix (escaped) on unexpected creation failures (R6 L73-75).
- **F8 (MED, extends C19).** A token placed in the session by any earlier request is reused by the sign-up/reset pages when no token is supplied. Session-fixation-style pre-seeding of a victim session with an attacker-chosen token is a plausible surface; runtime proof required.
- **F9 (LOW, nuance on C21).** Reset/invite authority for non-manager callers rests on a field-level restriction rather than an explicit method gate; implicit controls are fragile under customisation.
- **F10 (INFO).** Status-basis concern (X-ASGN-02) is refuted; SMEsPlus design should still define "confirmed" from one authoritative event rather than two projections.

Overclaims: C08 (public reflected echo), C09 (status divergence risk), C18 (generalised access check), C19 (all link values copied).

## 4. Omissions (not in A1)

| # | Omission | Severity | Link |
|---|---|---|---|
| O1 | Settings save persists displayed default when scope row absent | HIGH | F1 |
| O2 | Same-type reissue leaves earlier links valid | MED | F2 |
| O3 | Zero validity → non-expiring link | MED | F3 |
| O4 | Payload readable; database-secret keying; clone behaviour | LOW-MED | F4 |
| O5 | Session-stored token fallback on public pages | MED | F8 |
| O6 | Whitelisted `error`/`message` params rendered on public pages | LOW-MED | F6 |
| O7 | Name / mail-config disclosure on anonymous reset; raw exception text on sign-up | MED | F7 |
| O8 | Reactivated users (via base_setup bulk invite) receive no invitation | MED | C23 note |
| O9 | Captcha-free, rate-limit-free posture when no provider installed is not framed as a business risk for enumeration in A1 §4 | MED | C20, G9 |

## 5. Gap disposition (A1 §6)

| Gap | A2 status |
|---|---|
| G1 | Confirmed + extended (F1) |
| G2 | Settled — refuted as semantic divergence (C09) |
| G3 | Settled — signing algorithm, key source, expiry handling read from core (C05, F3, F4) |
| G4 | Partially settled — login exact match, e-mail case-insensitive exact match (C2 L748-754); base login-uniqueness constraint not read |
| G5 | Open (static JS not reviewed) |
| G6 | Unchanged — presence only |
| G7 | Settled (C10) |
| G8 | Settled — interchangeable (F5) |
| G9 | Open — runtime only (PR-ASGN-10) |

## 6. Lane B classification

No Lane B / runtime observation material exists in the repository for `auth_signup` (search of the governance tree returned none). Classification for every claim: **NOT_APPLICABLE** for source-only structural claims (C01, C04 install semantics, C24) and **UNCORROBORATED** for all behaviour claims. No FAIL is assigned on the basis of absent Lane B.

## 7. Proof requirements (MISSING_REQUIRED_RUNTIME_PROOF — inherently runtime claims only)

| PR | Claim(s) | Procedure | Expected (from source) | Fail condition |
|---|---|---|---|---|
| PR-ASGN-01 | C03, F1 | Delete scope row; open settings; request public sign-up page anonymously; then save an unrelated setting and re-request | Settings shows free sign-up; sign-up page not-found; after save, row = free sign-up and page available | Page available while row absent, or save does not recreate row |
| PR-ASGN-02 | C04 | Set scope to invitation-only; upgrade module; read row | Row unchanged | Row reverts to free sign-up |
| PR-ASGN-03 | C11, F7 | Anonymous reset with unknown id, duplicate-matching id, matched user lacking e-mail, valid id | Four distinguishable responses; third names the user | Responses indistinguishable |
| PR-ASGN-04 | C12 | Anonymous GET of sign-up and reset pages with e-mail of a confirmed user and of an invited user | Redirect with login for confirmed; no redirect for invited | No redirect for confirmed, or redirect for invited |
| PR-ASGN-05 | C05, F2 | Consume a reset link, replay it; separately issue two reset links without use and test the first | Replay rejected; first of two still valid | Replay accepted, or first link rejected |
| PR-ASGN-06 | C07, F5 | Submit an enrollment link to the reset route and a reset link to the sign-up route | Both accepted; sign-up route logs in, reset route does not | Either rejected by type |
| PR-ASGN-07 | F3 | Set reset validity to zero; issue link; test after default window | Link still valid | Link rejected as expired |
| PR-ASGN-08 | C08, F6 | Anonymous pages with invalid token and with crafted `error`/`message` params | Fixed invalid-token text, submitted value not echoed; crafted texts shown escaped | Token echoed on public page, or unescaped rendering |
| PR-ASGN-09 | C19, F8 | Visit any page with signup-token param; later open sign-up page without token | Page context uses the session token | Session token ignored |
| PR-ASGN-10 | C20, G9 | No captcha provider installed; burst anonymous reset/sign-up requests | No throttling observed in this module path | Throttling observed (then locate enforcing layer) |
| PR-ASGN-11 | C21, F9 | Internal non-manager invokes reset/invite on another user via RPC | Denied (field restriction) | Mail sent / pending type written |
| PR-ASGN-12 | C16 | Mail server unavailable; create user with e-mail | User exists, status Invited, no pending type, resend available to admin | User creation rolled back, or pending type left set |

Count: 12 proof requirements. Non-required (source-settled, optional confirmation): status filter vs display agreement (C09/C10).

## 8. Limitations

- All verdicts are SOURCE-STATIC at one anchor commit; source presence is not runtime reachability.
- Core files read only to settle specific gaps; base login-uniqueness constraint, captcha providers, session rotation on authentication, CSRF defaults for public routes, redirect sanitisation and static JS were not reviewed.
- Other installed modules may override any method here; findings assume `auth_signup` + its declared dependencies only.
- No QID answered; bank used only as topic lens. No percentages; claim counts are not a denominator; no Formal Coverage.
- A1 package not modified; corrections are recorded here for Reconciliation.
