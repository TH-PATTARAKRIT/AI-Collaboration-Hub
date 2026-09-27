# G01 PLATFORM_BASE — RED TEAM Reconciliation (REC) — `auth_signup`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of a two-stage REC + PROOF run; Stage 2 is recorded separately in `G01_PROOF/G01_AUTH_SIGNUP_PROOF_20260927.md`) |
| Group / Module | G01 PLATFORM_BASE / `auth_signup` |
| Date | 2026-09-27 |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/auth_signup/` (+ core files named in the Proof package) |
| Question bank | `GMVQ/G01_PLATFORM_BASE/G01_AUTH_SIGNUP_GMVQ_MVQ_40_V1.00_DRAFT.md`, sha256 `bf215a348a6efdb3fe0a171589fa9705832655a5f00c44f0b54c49c4cfade9e2`. This **equals** the `bank_files` entry in `FREEZE_W1-B02.json`. Freeze hash `cd966040f720456420057fe98fdb1176fbb9b0e85b456891f4dab82ea3ba0202`. W1-B02 is ELIGIBLE per `QUESTION_GATE_G01_FREEZE_REPLAY_20260927.md` |
| Join key | MODULE `auth_signup` + QID + freeze hash above. Mapping is lineage only. **No QID is answered here** |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (36 REC items; 5 CONTRADICTION items carried into Proof, none closed by REC) |

### 0.1 Input intake (immutable; sha256 recorded at intake, 2026-09-27 ~15:03 UTC)

Paths are relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

| Input | Path | sha256 | Cross-check |
|---|---|---|---|
| A1 package | `G01_A1_PACKAGES/G01_AUTH_SIGNUP_A1_PACKAGE_20260927.md` | `da32ca500989cf1befc9d48dc689c6ad6ee447705f1054e50226ee93ac0fe69e` | Matches the A1 hash recorded in the A2 header |
| A2 review | `G01_A2_REVIEWS/G01_AUTH_SIGNUP_A2_REVIEW_20260927.md` | `e5ce1b56ab35903665d02b3c58d184e2ba334ba72e8d09578ae0ff07f5dd28f9` | Disposition "A2 PASS WITH FINDINGS"; 12 proof requirements (PR-ASGN-01..12) |
| Lane A packet | `G01_LANE_A_PASS1/G01_AUTH_SIGNUP_LANE_A_PASS1_20260927.md` | `9470d090c3ed164634954ae0cb0cfe0d5ae92fb981d51a0a4fc3ccaa4addfa54` | Matches the hash recorded in both A1 and A2 headers |
| Cross-module A2 (interaction only) | `G01_A2_REVIEWS/G01_BASE_SETUP_A2_REVIEW_20260927.md` | `9e913ee76c3e1c34418a7e1d1ae93e4df1c65636abbd101849cc79cb3b651a31` | Used only for the bulk-invite interaction (REC-ASGN-31) |
| Question bank | see header | `bf215a34…fade9e2` | Equals FREEZE_W1-B02 entry; 40 QIDs |
| FREEZE manifest | `../GMVQ/G01_PLATFORM_BASE/FREEZE_W1-B02.json` | `bccaa2e1a0006429ff60ce7c9790862ea2e49d589da5d9a7919923b7cd504a2b` | freeze_hash `cd966040…0202` |

### 0.2 Lane B evidence-pool search (recorded, 2026-09-27 15:03 UTC)

- `grep -ril auth_signup /home/user/AI-Collaboration-Hub/99_SMEsPlus_Enterprise_Suite` → 43 files. Filtering those for `lane_b|lane b|laneb|gemini|evidence_pool|evidence pool` → 13 files; every hit is a governance statement of absence ("Lane B dependency: None", "No Lane B material viewed", freeze-rule text). None contains a runtime observation.
- `find /home/user/AI-Collaboration-Hub -iname '*lane_b*' -o -iname '*gemini*' -o -iname '*evidence_pool*'` → **no files**.
- Conclusion: **no Lane B / Gemini runtime evidence exists for `auth_signup`**. Absence is not failure. Every Lane B cell is UNCORROBORATED or NOT_APPLICABLE.

Clean-room note: every statement is a neutral WHAT/WHY/RISK paraphrase. Identifiers are evidence pointers only. No vendor code is reproduced; nothing recommends reusing vendor schema, ORM, workflow, UI or naming. No percentages. No Formal Coverage claim. No git operations. Inputs were not edited.

## 1. Classification rules (predeclared; same rules as `G01_BASE_AUTOMATION_REC_20260927.md`)

- **MATCH**: A1 and A2 agree and a source re-read supports the claim; no A2 proof requirement attaches to the claim itself.
- **GAP**: evidence missing and no static or runtime proof in scope can settle it now.
- **CONTRADICTION**: A1 and A2 disagree (A2 PARTIAL / NOT_VERIFIED correction), or the source disagrees with intent the source itself declares (displayed default, help text, docstring).
- **UNKNOWN_PENDING_PROOF**: A1 and A2 agree at source level (or A2 adds an omission A1 did not state) but the claim or its risk is runtime/config-dependent (A2 MISSING_REQUIRED_RUNTIME_PROOF).
- **Lane B**: UNCORROBORATED (behavioural) or NOT_APPLICABLE (structural / source-only gap). Never FAIL for absence.
- **Scope**: A1 claims C01–C24; A2 omissions O1–O9 as REC items; carried gaps not absorbed elsewhere. Fold-ins: G1→C03/O1; G2→C09 (X-ASGN-02); G3→C05/O3/O4; G6→C24; G7→C10; G8→C07 (F5); G9→O9; F5→C07; F9→C21; F10→C09.

## 2. Reconciliation table

PC = proof case in `G01_PROOF/G01_AUTH_SIGNUP_PROOF_20260927.md`. Static cases PC-ASGN-01..21 executed; runtime cases PC-ASGN-22..33 (= PR-ASGN-01..12) pending.

| REC ID | Item | A1 (claim / conf.) | A2 verdict | REC class | Basis for class | Lane B | Proof link | QID lineage (MODULE `auth_signup`) |
|---|---|---|---|---|---|---|---|---|
| REC-ASGN-01 | C01 | Auto-install on setup/mail/web; no ACL/rule files / HIGH | VERIFIED | MATCH | Manifest re-read (PC-20) | NOT_APPLICABLE | PC-20 | — |
| REC-ASGN-02 | C02 | Uninvited registration only when scope = free sign-up / HIGH | VERIFIED | MATCH | Gate re-read; public form cannot inject a partner (PC-01) | UNCORROBORATED | PC-01 | Q006 |
| REC-ASGN-03 | C03 (X-ASGN-01) | Scope default inconsistent: settings default + seed = free sign-up, runtime fallback = invitation only / HIGH | VERIFIED (strengthened → F1) | **CONTRADICTION** (source vs declared intent) | The settings surface declares "free sign-up" as the default while enforcement falls back to "invitation only" when the row is absent. A1 and A2 agree it exists; source confirms (PC-01). Effect runtime | UNCORROBORATED | PC-01; PC-22 | Q006 |
| REC-ASGN-04 | C04 | Install-time seeds non-updatable; upgrade does not re-assert / HIGH | VERIFIED | UNKNOWN_PENDING_PROOF | Function tags in non-updatable blocks skipped outside initial install (PC-03 PASS). Upgrade effect is runtime (PR-ASGN-02) | NOT_APPLICABLE | PC-03; PC-23 | — |
| REC-ASGN-05 | C05 | Signed expiring payload binding partner, users, last login, type; no stored token; single-use by construction / HIGH | VERIFIED (+F2–F4) | UNKNOWN_PENDING_PROOF | HMAC-signed, scope-separated, database-secret keyed, pending type cleared on use (PC-04). Replay rejection is runtime (PR-ASGN-05) | UNCORROBORATED | PC-04; PC-26 | Q001, Q002, Q028 |
| REC-ASGN-06 | C06 | Validity 4 h reset / 144 h enrollment, unseeded code defaults / HIGH | VERIFIED (edge F3 → REC-ASGN-27) | MATCH | Defaults re-read (PC-04) | UNCORROBORATED | PC-04 | Q002, Q029 |
| REC-ASGN-07 | C07 (+G8, F5) | Reset and enrollment links share one scope; distinguished by embedded type vs pending type / MED | VERIFIED; G8 settled — interchangeable across routes | UNKNOWN_PENDING_PROOF | No route-to-type binding (PC-06 PASS). Cross-route effect is runtime (PR-ASGN-06) | UNCORROBORATED | PC-06; PC-27 | Q012 |
| REC-ASGN-08 | C08 | Invalid-link error echoes the token; reflected-input risk / MED | **PARTIAL** — echo only in model-layer text; public pages pre-validate and show fixed text; output escaped | **CONTRADICTION** (A1 vs A2) | Source re-read supports A2 (PC-12 PASS). Both statements preserved | UNCORROBORATED | PC-12; PC-29 | Q037 |
| REC-ASGN-09 | C09 (X-ASGN-02, F10) | Status compute (login date) vs search (log rows) may disagree / HIGH | **PARTIAL** — literal only; login date is a projection of log rows, divergence refuted | **CONTRADICTION** (A1 vs A2; "paper-only") | Source re-read supports A2 (PC-11 PASS). A1 risk statement preserved; residual only via direct write of the writable related field | UNCORROBORATED | PC-11 | Q018, Q040 |
| REC-ASGN-10 | C10 (+G7) | Status search supports inclusion only; negation relies on core / MED | VERIFIED; G7 settled | MATCH | Core negation fallback re-read (PC-11) | UNCORROBORATED | PC-11 | Q040 |
| REC-ASGN-11 | C11 (+F7 part) | Anonymous reset: login then e-mail; distinct "no account" / "multiple accounts" texts / HIGH | VERIFIED (extended F7) | UNKNOWN_PENDING_PROOF | Distinct texts rendered to anonymous caller (PC-08). End-to-end observability runtime (PR-ASGN-03) | UNCORROBORATED | PC-08; PC-24 | Q011, Q037 |
| REC-ASGN-12 | C12 | `signup_email` privileged lookup redirects with login of non-Invited user / HIGH | VERIFIED | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-09). Disclosure is runtime (PR-ASGN-04) | UNCORROBORATED | PC-09; PC-25 | Q011, Q037 |
| REC-ASGN-13 | C13 | Registration refused when any user (incl. archived) holds the e-mail; disclosing message / HIGH | VERIFIED (scope note: applies to invited-partner creation too) | MATCH | Archive-inclusive e-mail and login checks (PC-10) | UNCORROBORATED | PC-10 | Q007, Q011, Q022, Q023 |
| REC-ASGN-14 | C14 | New users cloned from template user; missing template blocks / HIGH | VERIFIED (scope note) | MATCH | Template copy and failure re-read (PC-10) | UNCORROBORATED | PC-10 | Q034 |
| REC-ASGN-15 | C15 | Existing-user enrollment writes non-identity values; geolocation not overwriting; type cleared / MED | VERIFIED | MATCH | Re-read (PC-17) | UNCORROBORATED | PC-17 | Q019 |
| REC-ASGN-16 | C16 | Create auto-invites; mail failure cancels type, user kept / MED | VERIFIED (+ wrong-template silent return) | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-17). Recoverable admin-visible state is runtime (PR-ASGN-12) | UNCORROBORATED | PC-17; PC-33 | Q024 |
| REC-ASGN-17 | C17 | Archive/delete cancel pending signup; archived users cannot be reset/invited / MED | VERIFIED | MATCH | Re-read (PC-17) | UNCORROBORATED | PC-17 | Q023 |
| REC-ASGN-18 | C18 | Link generation privileged then requires write rights on users/partners / HIGH | **PARTIAL** — check only on the single-partner entry point, model-level only; multi-partner builder unchecked | **CONTRADICTION** (A1 vs A2) | Source re-read supports A2 (PC-14 PASS). Both preserved | UNCORROBORATED | PC-14 | Q009 |
| REC-ASGN-19 | C19 | Link/token values in query copied into session / MED | **PARTIAL** — only two named params copied, not the emailed `token`; session fallback omitted (F8) | **CONTRADICTION** (A1 vs A2) | Source re-read supports A2 (PC-07 PASS). Both preserved | UNCORROBORATED | PC-07; PC-30 | Q013 |
| REC-ASGN-20 | C20 | Captcha keys + anti-framing; 404 when disabled and no link; captcha outside module / HIGH | VERIFIED (nuance: session fallback counts as link) | UNKNOWN_PENDING_PROOF | Declarations confirmed (PC-15). Enforcement without a provider is runtime (PR-ASGN-10) | UNCORROBORATED | PC-15; PC-31 | Q015 |
| REC-ASGN-21 | C21 (+F9) | Reset attempts logged; admin reset action restricted to access-rights managers / HIGH | VERIFIED (nuance F9: method has no explicit gate) | UNKNOWN_PENDING_PROOF | Logging and action group confirmed; method gate absent, protection via field-level group (PC-16). Non-manager RPC effect runtime (PR-ASGN-11) | UNCORROBORATED | PC-16; PC-32 | Q033 |
| REC-ASGN-22 | C22 | Daily privileged reminder, 5-day window, self-disabling, no resend tracking / MED | VERIFIED | MATCH | Re-read (PC-18) | UNCORROBORATED | PC-18 | Q029 |
| REC-ASGN-23 | C23 | Bulk invite re-sends to still-Invited matches; rest delegated to base_setup / MED | VERIFIED (interaction note → REC-ASGN-31) | MATCH | Re-read (PC-19) | UNCORROBORATED | PC-19 | Q026 |
| REC-ASGN-24 | C24 (+G6, X-ASGN-03) | Retrieval flags accepted but ignored; random helper unused / HIGH | VERIFIED | MATCH | Re-read (PC-21) | NOT_APPLICABLE | PC-21 | — |
| REC-ASGN-25 | O1 / F1 (HIGH) | (A1 stated display/enforcement split, not the save effect) | O1 HIGH — missing scope row: any unrelated General Settings save persists "free sign-up" and opens public self-registration | UNKNOWN_PENDING_PROOF | Save routine writes every parameter-bound field whose stored value differs, an absent row counting as different (PC-02 PASS). Tenant-wide exposure change is runtime (PR-ASGN-01) | UNCORROBORATED | PC-02; PC-22 | Q006 |
| REC-ASGN-26 | O2 / F2 | (not stated) | O2 MED — re-sent same-type link leaves the earlier unused link valid | UNKNOWN_PENDING_PROOF | No per-issue nonce; re-issue changes no bound attribute (PC-05 PASS). Runtime PR-ASGN-05 | UNCORROBORATED | PC-05; PC-26 | Q003 |
| REC-ASGN-27 | O3 / F3 | (not stated) | O3 MED — validity parameter zero → link never expires; non-integer errors | UNKNOWN_PENDING_PROOF | Zero hours yields a zero expiry stamp that the verifier treats as "no expiry" (PC-04 PASS). Runtime PR-ASGN-07 | UNCORROBORATED | PC-04; PC-28 | Q002, Q029 |
| REC-ASGN-28 | O4 / F4 | (not stated; G3) | O4 LOW-MED — payload readable (signed, not encrypted); keyed on per-database secret; clone keeping the secret would accept links | UNKNOWN_PENDING_PROOF | Encoding and key source confirmed (PC-04). Clone behaviour runtime/config; no A2 PR — A3 may request one | UNCORROBORATED | PC-04 | Q032, Q036 |
| REC-ASGN-29 | O5 / F8 | (C19 partial) | O5 MED — session-stored token reused by sign-up/reset pages when none supplied | UNKNOWN_PENDING_PROOF | Fallback confirmed (PC-07 PASS). Pre-seeding exploitability runtime (PR-ASGN-09) | UNCORROBORATED | PC-07; PC-30 | Q013 |
| REC-ASGN-30 | O6 / F6 | (not stated) | O6 LOW-MED — whitelisted `error`/`message` params rendered (escaped) on public pages; content spoofing | UNKNOWN_PENDING_PROOF | Whitelist, escaping and form suppression confirmed (PC-13, PC-12). Runtime PR-ASGN-08 | UNCORROBORATED | PC-13; PC-29 | Q037 |
| REC-ASGN-31 | O8 (cross base_setup F3) | (C23 did not state it) | O8 MED — users reactivated by base_setup bulk invite receive no invitation | UNKNOWN_PENDING_PROOF | Re-invite search uses default active filtering and runs before reactivation; reactivation is a write, not a create (PC-19 PASS). Runtime: base_setup PC-BSET-24 (PR-BSET-07) | UNCORROBORATED | PC-19; PC-BSET-24 | Q023, Q026 |
| REC-ASGN-32 | O7 / F7 | (C11 partial) | O7 MED — anonymous reset reveals a matched user's display name (no e-mail) and mail-server state; sign-up renders raw exception text (escaped) | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-08 PASS). Runtime PR-ASGN-03 | UNCORROBORATED | PC-08; PC-24 | Q011, Q037 |
| REC-ASGN-33 | O9 (+G9) | (C20; G9) | O9 MED — captcha-free, rate-limit-free posture when no provider installed, not framed as enumeration risk | UNKNOWN_PENDING_PROOF | No throttling construct in module controller (PC-15). Enforcement elsewhere is runtime (PR-ASGN-10) | UNCORROBORATED | PC-15; PC-31 | Q015 |
| REC-ASGN-34 | G4 (partial) | Base login-uniqueness constraint not read | Partially settled (domain helpers read; constraint not) | GAP | Not read in this lineage | NOT_APPLICABLE | — | — |
| REC-ASGN-35 | G5 | Static JS not reviewed | Open | GAP | Out of scope | NOT_APPLICABLE | — | — |
| REC-ASGN-36 | A2 §8 unreviewed core | CSRF defaults for public routes, session rotation on authentication, redirect sanitisation | Not reviewed (A2 limitation) | GAP | Nothing in scope reads them | NOT_APPLICABLE | — | — (relevant to Q013, Q014, Q016; see §3) |

### 2.1 Class counts

| Class | Count | Items |
|---|---|---|
| MATCH | 11 | C01, C02, C06, C10, C13, C14, C15, C17, C22, C23, C24 |
| CONTRADICTION | 5 | C03 (source vs declared intent), C08, C09, C18, C19 (A1 vs A2) |
| UNKNOWN_PENDING_PROOF | 17 | C04, C05, C07, C11, C12, C16, C20, C21, O1, O2, O3, O4, O5, O6, O7, O8, O9 |
| GAP | 3 | G4 (partial), G5, A2 §8 unreviewed core areas |
| **Total** | **36** | 24 A1 claims + 9 A2 omissions + 3 carried gaps |

Lane B: UNCORROBORATED 30, NOT_APPLICABLE 6 (C01, C04, C24, REC-34, REC-35, REC-36). No FAIL for absence.

### 2.2 Contradiction handling (both sources preserved)

- C08, C09, C18, C19: A1 statements and A2 corrections both stand in their packages; REC does not rewrite A1. The Stage-2 static re-read supports A2 in each case (PC-12, PC-11, PC-14, PC-07). Items remain CONTRADICTION until A3 reviews them. X-ASGN-02 (C09) is recorded as paper-only: the literal difference exists, the semantic divergence does not.
- C03 / X-ASGN-01: A1 and A2 agree; the contradiction is inside the source (declared default vs enforced fallback). Its practical consequence (O1) is carried as REC-ASGN-25.
- A2 HIGH item O1 is not a contradiction between reviewers; it is carried as UNKNOWN_PENDING_PROOF with static basis confirmed.

## 3. QID lineage map (frozen bank; lineage only, not answers)

Join key: MODULE `auth_signup` + QID + freeze hash `cd966040f720456420057fe98fdb1176fbb9b0e85b456891f4dab82ea3ba0202`. A mapping means "this REC item is topically relevant evidence for the question". It does not answer the QID or satisfy any disconfirming observation.

| QID | Topic (paraphrased) | Mapped REC items |
|---|---|---|
| G01-AUTH_SIGNUP-Q001 | One-time invitation not replayable | REC-05 (C05) |
| G01-AUTH_SIGNUP-Q002 | Expired/revoked invitation unusable | REC-05 (C05), REC-06 (C06), REC-27 (O3) |
| G01-AUTH_SIGNUP-Q003 | Explicit resend rule for prior links | REC-26 (O2) |
| G01-AUTH_SIGNUP-Q006 | Disabled self-registration has no alternate path | REC-02 (C02), REC-03 (C03), REC-25 (O1) |
| G01-AUTH_SIGNUP-Q007 | Identifier normalisation / duplicates | REC-13 (C13) |
| G01-AUTH_SIGNUP-Q009 | Inviter authority revalidated | REC-18 (C18) |
| G01-AUTH_SIGNUP-Q011 | Registration messages non-disclosure | REC-11 (C11), REC-12 (C12), REC-13 (C13), REC-32 (O7) |
| G01-AUTH_SIGNUP-Q012 | Enrollment vs recovery credentials not substitutable | REC-07 (C07/F5) |
| G01-AUTH_SIGNUP-Q013 | Fresh session, not attacker-chosen pre-session | REC-19 (C19), REC-29 (O5) |
| G01-AUTH_SIGNUP-Q015 | High-rate attempts constrained | REC-20 (C20), REC-33 (O9) |
| G01-AUTH_SIGNUP-Q018 | Verification status auditable | REC-09 (C09) |
| G01-AUTH_SIGNUP-Q019 | Prefilled values revalidated server-side | REC-15 (C15) |
| G01-AUTH_SIGNUP-Q022 | Shared/alias addresses do not merge people | REC-13 (C13) |
| G01-AUTH_SIGNUP-Q023 | Inactive identity reactivation rule | REC-13 (C13), REC-17 (C17), REC-31 (O8) |
| G01-AUTH_SIGNUP-Q024 | Partial failure leaves recoverable state | REC-16 (C16) |
| G01-AUTH_SIGNUP-Q026 | Bulk invitation per-recipient checks | REC-23 (C23), REC-31 (O8) |
| G01-AUTH_SIGNUP-Q028 | Two tabs, same one-time enrollment | REC-05 (C05) |
| G01-AUTH_SIGNUP-Q029 | Dormant invitation lifecycle | REC-06 (C06), REC-22 (C22), REC-27 (O3) |
| G01-AUTH_SIGNUP-Q032 | Cloned environment invitations | REC-28 (O4) |
| G01-AUTH_SIGNUP-Q033 | Invitation lifecycle audit trail | REC-21 (C21) |
| G01-AUTH_SIGNUP-Q034 | Admin vs self enrollment converge | REC-14 (C14) |
| G01-AUTH_SIGNUP-Q036 | Link from another environment rejected | REC-28 (O4) |
| G01-AUTH_SIGNUP-Q037 | Templates reveal minimum information | REC-08 (C08), REC-11, REC-12, REC-30 (O6), REC-32 (O7) |
| G01-AUTH_SIGNUP-Q040 | Coherent final identity state across paths | REC-09 (C09), REC-10 (C10) |

**Mapped: 24 QIDs.** **No evidence yet: 16 QIDs** — Q004 (company context on completion), Q005 (forwarded invitation authority), Q008 (concurrent enrollment), Q010 (role changed before use), Q014 (anti-forgery on submission; unreviewed per REC-36), Q016 (post-enrollment redirect; unreviewed per REC-36), Q017 (unverified identity privileges), Q020 (server-side password policy), Q021 (Unicode normalisation), Q025 (retry after ambiguous timeout), Q027 (invitation removal preserves audit), Q030 (company deletion invalidates invitations), Q031 (snapshot restore), Q035 (primary identifier change), Q038 (queued delivery context), Q039 (enrollment cannot post transactions). No mapping answers a QID.

## 4. Handoff

- To: PROOF (Stage 2, same run, separate record): `G01_PROOF/G01_AUTH_SIGNUP_PROOF_20260927.md`.
- Proof must address the 17 UNKNOWN_PENDING_PROOF items and the 5 CONTRADICTION items. The 3 GAP items are not closable by Proof in this scope and are carried forward.

## 5. Limitations

- REC used only the immutable inputs in 0.1 and, for classification support, the static proof results from Stage 2. No runtime evidence exists.
- QID mapping is topical lineage judged by this controller; it is not a coverage measure. No Formal Coverage claim. No percentages.
- Other installed modules (captcha providers, portal, website) may override behaviour here; classifications assume `auth_signup` plus declared dependencies.
