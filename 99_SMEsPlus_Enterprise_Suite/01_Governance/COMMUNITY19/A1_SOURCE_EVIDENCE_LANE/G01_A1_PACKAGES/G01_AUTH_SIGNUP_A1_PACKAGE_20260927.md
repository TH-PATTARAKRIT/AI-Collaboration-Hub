# G01 PLATFORM_BASE — RED TEAM A1 PACKAGE — `auth_signup`

| Item | Value |
|---|---|
| Role | RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `auth_signup` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_AUTH_SIGNUP_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `9470d090c3ed164634954ae0cb0cfe0d5ae92fb981d51a0a4fc3ccaa4addfa54` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (paths under `addons/`) |
| Topic lens (not answered) | `GMVQ/G01_PLATFORM_BASE/G01_AUTH_SIGNUP_GMVQ_MVQ_40_V1.00_DRAFT.md` — batch W1-B02, freeze_hash `cd966040f720456420057fe98fdb1176fbb9b0e85b456891f4dab82ea3ba0202`, bank sha256 `bf215a34…fade9e2` (matches freeze record), ELIGIBLE |
| Lane B | Not consumed; A1 does not wait for Lane B |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Clean-room: all statements are neutral WHAT / WHY / RISK abstractions. Identifiers are evidence pointers only. Nothing here recommends reuse of reference schema, ORM, workflow or UI. No QID is answered; bank used only as a topic lens.

## 1. Claims

Evidence IDs (E#) refer to the Lane A pointer table; blob = git blob SHA-1. Layer for all claims: SOURCE-STATIC.

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence (path, blob) | Conf. |
|---|---|---|---|
| A1-G01-ASGN-C01 | WHAT: capability auto-installs once its prerequisites (setup, mail, web) are present and ships no ACL/record-rule files. WHY: exposure is governed by configuration values, not by module presence. | E1 `auth_signup/__manifest__.py` 99420339… | HIGH |
| A1-G01-ASGN-C02 | WHAT: open (uninvited) self-registration is permitted only when the invitation-scope setting equals the "free sign-up" value; otherwise uninvited registration is rejected. | E8 `models/res_users.py` 1a0280b8… (spot-checked) | HIGH |
| A1-G01-ASGN-C03 | RISK: the invitation-scope default is inconsistent across layers — settings default and install-time seed both select "free sign-up", while the runtime reader falls back to "invitation only" if the parameter is absent. Effective policy depends on whether the seed row exists. | E5 f72a458d…, E10 df7690a0…, E8 1a0280b8… (all spot-checked) | HIGH |
| A1-G01-ASGN-C04 | WHAT: install-time seeds (scope = free sign-up, password reset = enabled) are non-updatable; a module upgrade will not re-assert them after admin change or deletion. | E10 df7690a0… (spot-checked) | HIGH |
| A1-G01-ASGN-C05 | WHAT: enrollment/reset links carry a signed, expiring payload binding partner, its user set, last-login marker and link type; no token is stored. WHY: any subsequent login, change of linked users, or type change invalidates outstanding links (single-use by construction). | E7 `models/res_partner.py` 02aab000… (spot-checked) | HIGH |
| A1-G01-ASGN-C06 | WHAT: default validity is 4 h for reset links and 144 h for enrollment links; both are overridable by parameters that are not seeded (code-level defaults). | E7 02aab000… (spot-checked), E10 | HIGH |
| A1-G01-ASGN-C07 | WHAT: reset and enrollment links share one signing scope and are distinguished only by the embedded type compared against the partner's current pending type. | E7 02aab000… (spot-checked) | MED |
| A1-G01-ASGN-C08 | WHAT: the invalid/expired-link error message echoes the submitted token value back. RISK: reflected input in an error surface. | E7 02aab000… (spot-checked) | MED |
| A1-G01-ASGN-C09 | WHAT: user status (Invited / Confirmed) is computed from the presence of a last-login date but searched via existence of login-log records. RISK: filters/lists and displayed status can disagree when the two bases diverge. | E8 1a0280b8… (spot-checked) | HIGH |
| A1-G01-ASGN-C10 | WHAT: status search supports only the inclusion operator; public controllers query with a "not Invited" condition. WHY/RISK: correct evaluation relies on core domain negation handling outside this module. | E8 1a0280b8…, E9 96d8b71f… (spot-checked) | MED |
| A1-G01-ASGN-C11 | WHAT: public password reset resolves by login first, then e-mail; zero or multiple matches raise generic errors whose distinct texts ("no account" / "multiple accounts") are rendered verbatim to the anonymous requester. RISK: account enumeration. | E8 1a0280b8…, E9 96d8b71f… (both spot-checked) | HIGH |
| A1-G01-ASGN-C12 | WHAT: a `signup_email` query value on public signup/reset pages triggers a privileged lookup; for a matching non-Invited user the response redirects to login with that user's login pre-filled. RISK: enumeration / identifier disclosure. | E9 96d8b71f… (spot-checked) | HIGH |
| A1-G01-ASGN-C13 | WHAT: uninvited registration is refused when any user, including archived, already holds the e-mail; message states the e-mail is already registered. RISK: registration-path enumeration where non-disclosure is required. | E8 1a0280b8…, E9 96d8b71f… (spot-checked) | HIGH |
| A1-G01-ASGN-C14 | WHAT: new self-registered users are cloned from a configured template user; missing/deleted template blocks registration. WHY: template governs default rights for public users. | E8 1a0280b8…; E13 | HIGH |
| A1-G01-ASGN-C15 | WHAT: link-based enrollment for an existing user writes only non-identity values (login/name protected); geolocation-type values never overwrite existing partner data; pending type cleared on use. | E8 | MED |
| A1-G01-ASGN-C16 | WHAT: creating a user with an e-mail auto-sends an invitation unless suppressed by context; mail failure cancels the pending type but the user remains created. RISK: silent partial state (user exists, no usable link). | E8 | MED |
| A1-G01-ASGN-C17 | WHAT: archiving or deleting a user cancels pending signup; archived users cannot be reset or invited. | E8 | MED |
| A1-G01-ASGN-C18 | WHAT: link generation executes privileged but then requires write rights on users (internal targets) or partners (portal targets) other than self. | E7 02aab000… (spot-checked) | HIGH |
| A1-G01-ASGN-C19 | WHAT: link/token values present in request query are copied into the server session on each request pre-dispatch. | E6 `models/ir_http.py` fa7cd42c… | MED |
| A1-G01-ASGN-C20 | WHAT: signup and reset routes declare captcha keys and anti-framing headers; both return not-found when the feature is disabled and no link is supplied. Captcha enforcement lives outside the module. | E9 96d8b71f… (spot-checked) | HIGH |
| A1-G01-ASGN-C21 | WHAT: reset attempts are logged with requested login, acting user and remote address; admin reset action restricted to access-rights managers. | E9 (spot-checked), E14 | HIGH |
| A1-G01-ASGN-C22 | WHAT: a daily privileged job reminds inviters about internal users created exactly five days earlier with no login record; it self-disables if its template is missing and does not track resends. | E8, E11 | MED |
| A1-G01-ASGN-C23 | WHAT: bulk invite from settings re-sends to still-Invited matches and delegates the remainder to base_setup. | E8; base_setup E6 | MED |
| A1-G01-ASGN-C24 | WHAT: a validity/raise-flag parameter pair on link retrieval is accepted but ignored (always raises); a random-token helper is defined but unused. Presence only — no intent inferred. | E7 02aab000… (spot-checked) | HIGH |

## 2. Business rules (source-static)
- BR1 Uninvited registration requires scope = free sign-up (C02); invited registration always allowed with a valid link (C05).
- BR2 One e-mail = one identity across active and archived users on the uninvited path (C13).
- BR3 Links self-invalidate on login, user-set change or type change; expiry 4 h reset / 144 h enrollment by default (C05, C06).
- BR4 New public identities inherit the template user's rights (C14).
- BR5 Archived users are excluded from reset/invite (C17).

## 3. States / transitions
- User status: Invited → Confirmed on first recorded login (compute: login date; search: login-log rows) (C09).
- Partner pending-type: none → enrollment | reset (on invite/reset request) → none (on use, archive, delete, or mail failure) (C15–C17).
- Link: issued → valid until expiry or until any bound attribute changes → invalid (C05).

## 4. Exceptions / failure modes
- Template user missing → registration fails (C14).
- Mail server failure → mapped user-facing error; on user create, pending type cancelled, user retained (C16).
- Reset with zero / multiple matches → distinct messages to anonymous caller (C11).
- Invalid/expired link → error echoing token (C08).
- Reset skipped during install mode or data import (Lane A #14).

## 5. Cross-module handoffs
- `base_setup`: settings-form anchor, dashboard data route extended with resend flag, bulk-invite chain (C23).
- `base`: user/partner models, login/e-mail domain helpers, login uniqueness, template-user parameter, group definitions.
- `web`: login controller and templates; captcha-skip constant.
- `mail`: templates, delivery exceptions, bus notification to inviter on first internal login.
- Captcha providers (external consumers of captcha keys).

## 6. Evidence gaps (carried from Lane A + A1)
- G1 Invitation-scope default contradiction (now CONFIRMED-FROM-SOURCE, see §9).
- G2 Status compute vs search basis (CONFIRMED-FROM-SOURCE, see §9).
- G3 Signing primitives (algorithm, key source, clock handling) in core tools not fetched.
- G4 Login/e-mail domain helpers and base login-uniqueness constraint not fetched.
- G5 Static JS not reviewed.
- G6 Unused helpers/flags (C24) — presence only.
- G7 (A1) Negation handling of status search in core domain layer not verified (C10).
- G8 (A1) Whether a reset-type link can be consumed on the enrollment route (and vice versa) not established from fetched files (C07).
- G9 (A1) Rate limiting beyond captcha hooks not evidenced in module.

## 7. CRQ candidates (runtime / proof required)
| CRQ | Question for proof | Links |
|---|---|---|
| CRQ-ASGN-01 | With the scope parameter row deleted, is uninvited registration blocked while the settings UI shows "free sign-up"? | C03 |
| CRQ-ASGN-02 | After an upgrade, does a changed/deleted seed remain as-is (no re-seed)? | C04 |
| CRQ-ASGN-03 | Anonymous reset for unknown vs duplicate identifier: are the distinct messages observable end-to-end? | C11 |
| CRQ-ASGN-04 | Does the `signup_email` redirect disclose login for existing users without authentication? | C12 |
| CRQ-ASGN-05 | Can status filter and displayed status disagree (login log present but no login date, or vice versa)? | C09, C10 |
| CRQ-ASGN-06 | Is a consumed link rejected on replay; does a second link issuance invalidate the first? | C05 |
| CRQ-ASGN-07 | Can a reset link be submitted to the enrollment route (or vice versa) with effect? | C07, G8 |
| CRQ-ASGN-08 | Is the echoed token in error output escaped (no reflected injection)? | C08 |
| CRQ-ASGN-09 | Mail failure on user creation: is the resulting user state recoverable/visible to admin? | C16 |
| CRQ-ASGN-10 | Is captcha/rate limiting actually enforced when no provider module is installed? | C20, G9 |

## 8. Contradictions
| ID | Contradiction | Classification |
|---|---|---|
| X-ASGN-01 | Scope default: settings default + seed = free sign-up; runtime fallback = invitation only | CONFIRMED-FROM-SOURCE (E5, E8, E10 re-fetched, blobs match, text verified) |
| X-ASGN-02 | Status: compute basis = last-login date; search basis = login-log records | CONFIRMED-FROM-SOURCE (E8 re-fetched, verified) |
| X-ASGN-03 | Retrieval flags documented as optional but behaviour always raises | CONFIRMED-FROM-SOURCE (E7 re-fetched, verified) |

## 9. Spot-check log
Method: `curl` raw file at anchor → `git hash-object` → compare with Lane A blob → inspect for claim text. Fetch copies kept in scratchpad only.

| # | Path | Lane A blob | Re-computed blob | Match | Claim verified |
|---|---|---|---|---|---|
| S1 | auth_signup/models/res_users.py | 1a0280b8c37a11072caabe7640342b4f3f553514 | 1a0280b8c37a11072caabe7640342b4f3f553514 | YES | Scope reader falls back to invitation-only; status compute vs search bases differ; reset raises distinct no-account / multiple-accounts texts; uninvited path blocked unless free sign-up — VERIFIED |
| S2 | auth_signup/models/res_config_settings.py | f72a458da9b101fe2fa3f899d3c61330aa4fcfff | f72a458da9b101fe2fa3f899d3c61330aa4fcfff | YES | Settings default = free sign-up, bound to scope param — VERIFIED |
| S3 | auth_signup/data/ir_config_parameter_data.xml | df7690a08de224e5fe0869ec64bdb5eb58454900 | df7690a08de224e5fe0869ec64bdb5eb58454900 | YES | Non-updatable seed: scope free sign-up, reset enabled; validity params not seeded — VERIFIED |
| S4 | auth_signup/controllers/main.py | 96d8b71fe7c987f3007f9bd9f49ab5a12bbc1f6f | 96d8b71fe7c987f3007f9bd9f49ab5a12bbc1f6f | YES | Generic exception text rendered to caller; `signup_email` privileged lookup + login-prefilled redirect; reset attempt logging; anti-framing headers — VERIFIED |
| S5 | auth_signup/models/res_partner.py | 02aab00061cebd39df9711fd188ac0c2c681c3dd | 02aab00061cebd39df9711fd188ac0c2c681c3dd | YES | Signed payload binding; 4 h / 144 h defaults; retrieval flags ignored; token echoed in error; random helper unused — VERIFIED |

Result: 5/5 blobs match; no Lane A claim refuted. A1 refinements: C08, C10 (new observations from S4/S5).

## 10. Provenance
- Input: Lane A packet (sha256 above), evidence E1–E18 at anchor commit.
- Spot-check fetches: `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/<path>`, 2026-09-27.
- Topic lens: frozen bank W1-B02 (read only, not edited, no QID answered).
- No Lane B material consulted.

## 11. Limitations
- Source presence ≠ runtime reachability; every claim is SOURCE-STATIC.
- No Formal Coverage claim; claim count is not a denominator.
- Single anchor commit; no version comparison.
- Core helpers (signing, domain helpers, captcha providers) not fetched — see gaps.
