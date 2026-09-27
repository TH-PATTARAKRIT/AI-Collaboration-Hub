# G01 PLATFORM_BASE — RED TEAM Proof Package — `portal`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller. This is Stage 2 of a two-stage REC + PROOF run |
| Group / Module | G01 PLATFORM_BASE / `portal` |
| Date | 2026-09-27 |
| Upstream REC | `G01_RECONCILIATION/G01_PORTAL_REC_20260927.md`. 33 REC items: MATCH 13, CONTRADICTION 4, UNKNOWN_PENDING_PROOF 10, GAP 6 |
| Inputs (sha256 at intake 15:00:53Z) | A1 `aef33889…957d`; A2 `695171c7…6ec0`; Lane A `af066bfb…826f`; bank `91b63eef…3d3a` = FREEZE_W1-B03 entry; freeze hash `1247c218ba4e2e6a57e259427030f4350881da56a5a28c59901a20f8b2d3a5d3` (recomputed, identical) |
| Predeclaration | Scratchpad `rec_prtl_utm/PROOF_CASES_PREDECLARED.md` (it holds both the portal and the utm cases), sha256 `5438a46fdaecedaa6af02125ef605d673aff390095a04033b7209c4d75cb14e9`. It was written and hashed at **2026-09-27T15:02:42Z**, before any Proof source fetch. The first fetch was at 15:02:59Z and execution ended at 15:07:04Z. The hash was re-verified as unchanged at 15:10Z |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`. Every blob was verified with `git hash-object` (section 2) |
| Runtime device | THPATTARAKRIT-SOLUTION-SERVICE-2.local is **OFFLINE**. At 2026-09-27T15:10:48Z, `getent hosts` returned rc=2 and the curl probe returned "Could not resolve host" |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** |

Clean-room note: results are neutral paraphrases of observed source behaviour. Identifiers are evidence pointers only. No vendor code is reproduced, and nothing recommends reusing vendor schema, ORM, workflow, UI or naming. No percentages. No Formal Coverage claim. No git operations. Inputs were not edited. Source copies are held in the scratchpad only (`rec_prtl_utm/src/`).

## 1. Case design

- **Static cases PC-PRTL-01..13 (SOURCE / CONFIG).**
  - One case for each A1 HIGH claim, which re-confirms A2's verdict independently (process deviation PD-PRTL-01).
  - One case for the static half of each A2 proof requirement where the source decides it.
  - All of these were **executed now**.
- **Runtime cases PC-PRTL-14..22** map one to one onto A2 PR-P1..PR-P9. Setup, expected result and fail condition are taken unchanged from A2 §6 and restated in §4 so the cases can run without further authoring.
- **A static PASS confirms only that the source reads as the static prediction assumes.** It is never counted as a result for the linked runtime case.

## 2. Blob verification (executed)

All files are under `addons/portal/`. The expected value is the Lane A blob. The computed value is `git hash-object`.

| File | Blob (expected = computed) | Result |
|---|---|---|
| `__manifest__.py` | 0df9206a8a580649d9c2e81905e3e92a6a109587 | MATCH |
| `models/portal_mixin.py` | d24085d8da0a56a8b078d0d073aa85d6016f6d79 | MATCH |
| `models/mail_thread.py` | 971d3f790238ae0359f6236fc1a8230b50a97ed0 | MATCH |
| `models/mail_message.py` | 179764577eb2216b6c7ae8a9ede2ed54a146106d | MATCH |
| `models/res_partner.py` | d8f075eb4038182d04afdab4ea4f78724e167eb5 | MATCH |
| `models/res_users_apikeys_description.py` | 44c0008fd902b3ac08c57d0eb036b5c5c29bf0ef | MATCH |
| `controllers/portal.py` | e6b03c24fa227c362a20d6811cfa5c59cf717f02 | MATCH |
| `controllers/portal_thread.py` | 363bc48c39bb0b30dc082b2be9154a66d405923b | MATCH |
| `controllers/thread.py` | 8384c8d57d0163c6546fa5868d165e99327d2b83 | MATCH |
| `controllers/message_reaction.py` | bd84a5e258d609bf919b6280a53945d6dc4d21bd | MATCH |
| `controllers/mail.py` | aef21b45f04ef933521f41dd7013f0a9e9b01e1f | MATCH |
| `utils.py` | b83ac0a1415ab9c1c5b7acd8c8d5c2c38c3417d1 | MATCH |
| `wizard/portal_wizard.py` | 368f4c1d369892aaefb4e16b5632e6e7b3486cc8 | MATCH |
| `wizard/portal_share.py` | b0491d4e3517118f94fa7dc439b46f324bf8f5f3 | MATCH |
| `security/ir.model.access.csv` | 6506676a9e55e5ccb7f2d578b1c7804efbb2142e | MATCH |
| `views/res_config_settings_views.xml` | 862a35865bc3bde0080282165436e058c59c9759 | MATCH |

16 of 16 blobs match.

## 3. Static cases — executed (SOURCE / CONFIG)

The expected result and the fail condition are the predeclared ones, in substance.

| Case | Layer | Links | Expected (predeclared) | Fail condition (predeclared) | Actual (observed, paraphrased) | Result |
|---|---|---|---|---|---|---|
| PC-PRTL-01 | SOURCE | C01, O2, REC-01, REC-21 | The ensure-token helper writes a random UUID elevated, only when empty. **Three** call sites (share-URL builder, portal-URL builder, customer-notification grouping). Only the share-URL builder has an explicit read check | Helper does not elevate or writes when non-empty; **call-site count differs**; a non-share caller has an explicit read check | Helper: confirmed (elevated write of a random UUID only when the token is empty). Explicit read check: only the share-URL builder has one; confirmed. **Call sites: 5 invocations in 4 functions, not 3.** Besides the three A2 named, the module-level **records-pager helper** in `controllers/portal.py` (lines ~96–121) mints tokens for the previous and next records in the caller's portal session history and embeds tokenized URLs for them. It has no explicit read check, and it runs on the record handle it is given (downstream page-view values pass the document, which is typically the elevated handle returned by the gate) | **FAIL** (on the call-site-count condition). The C01 core holds. The A2 refinement "three minting call sites" is refuted as incomplete, and O2 is **widened** (see §3.1 R1) |
| PC-PRTL-02 | SOURCE | C02, O4, REC-02, REC-23 | No rotate/expire/clear path; token not copied; hash derived from the token field | Any path writes/clears/rotates the token; token copied; hash not token-derived | The only write of the token field in module Python is the ensure-token helper (write-if-empty). The field is marked not-copied. The signed hash takes the post-token field value as an input | PASS |
| PC-PRTL-03 | SOURCE | C03, REC-03 | Read check precedes token embedding; optional pid+hash and signup params | Token embedded without a preceding read check | In the share-URL builder, an explicit read check runs immediately before the token is ensured and embedded. pid+hash and partner signup parameters are optional. In redirect mode the builder targets the generic mail-view route | PASS |
| PC-PRTL-04 | SOURCE | C04, C09, O3, S1, REC-04/09/18/22 | Elevated load; existence check; caller read check; constant-time token fallback; elevated record returned; no user, active, company or state input | Gate consults user account, active/archive, company or document state; or returns a non-elevated record | The gate browses the record, re-binds it to the superuser and checks existence only (no active filter). It tries the caller's read check. On access error it accepts a constant-time match of the supplied token against the stored one, and re-raises otherwise. It returns the superuser-bound record on both paths. No user, partner, company, active or state input | PASS |
| PC-PRTL-05 | SOURCE | C05, O7, REC-05/26 | Distinct missing and denied errors; the in-module caller maps both to one message | Single error kind; or the in-module caller exposes the difference | A missing-record error is raised before the access check, and the access error is re-raised on token failure. The only in-module caller (public pending-attachment removal) catches both and raises one identical user message. That caller then deletes only attachments that are pending and linked to no message (O7 confirmed) | PASS |
| PC-PRTL-06 | SOURCE | C06, C09, S2, REC-06/18/23 | HMAC-SHA256 keyed by the DB secret over (dbname, token value, pid); constant time; validators take only record + supplied secret | Other key or inputs; non-constant-time compare; validator consults user/partner account state | Confirmed: HMAC-SHA256 keyed by the database secret parameter over (db name, post-token field value, pid). It raises an error if the model lacks the token field. The parent-hash hook defaults to none. Both validators compare in constant time, using only the record plus the supplied hash/pid or token. The partner resolver returns the pid partner elevated (hash path) or the record's first customer partner (token path), with no active-state check | PASS |
| PC-PRTL-07 | SOURCE | C07 (static half of PR-P9), REC-07 | Author substitution and edit rule apply only when the request runs as the public user; reactions use the portal partner only when the core resolved none | Substitution applies to logged-in users too | Post-data author substitution is gated on "current user is public". The edit-own-message override is also gated on public. The reaction override applies only when the core resolved no partner, and then clears the guest | PASS (supports A2's scope correction) |
| PC-PRTL-08 | SOURCE | C08, C09, REC-08/09 | Revoke requires portal access; syncs email; clears signup type; archives the portal user only; group unchanged; no token/hash touched | Any token/hash invalidation; internal user archived; no precondition | Precondition: an error unless the contact is currently portal. Then: sync the edited email, clear the partner signup type elevated, and archive the linked user only if that user is portal. There is no group change and no document token or hash is touched | PASS |
| PC-PRTL-09 | SOURCE | C10, G8 (static half of PR-P6), REC-10/19 | The lookup includes archived users; grant re-activates the existing user, adds portal, removes public, sends invite; creation elevated in partner company with fallback | The lookup excludes archived users (a new user would be created) | The linked-user compute reads the partner's users with the active filter off and takes the first. Grant creates a user only if none is linked (elevated, partner company, else current company, with only that company allowed). It then writes active=true, adds portal, removes public, prepares signup and sends the invite. **Re-grant therefore reactivates the same archived user.** An archived *internal* user is reported as internal, and grant refuses | PASS |
| PC-PRTL-10 | CONFIG | C11, REC-11 | 3 rows, partner-manager only, no delete; no group/rule file in the data list | Extra rows, delete granted, or a rule/group file present | Exactly 3 ACL rows (share wizard, grant wizard, wizard line), all partner-manager, with read/write/create and no delete. The manifest data list has 8 entries (ACL, mail template, 4 views, 2 wizard views) and no group or record-rule file | PASS |
| PC-PRTL-11 | SOURCE | C16, O1 (static half of PR-P3), REC-16/20 | Share link computed on open via the share-URL builder (mints the token); send uses the public path when a token exists or B2C is off; per-recipient pid+hash | Opening the wizard does not mint a token; or the send condition differs | Both the wizard's default-values step and its share-link compute call the share-URL builder in redirect mode with token sharing on, which ensures (mints) the token. At send time, the public branch is taken when the record has a token **or** B2C invitation scope is off. Otherwise only partners with users get the public link, and the rest get signup links. The public link is built per recipient with that recipient's pid and hash over the shared token. For portal-mixin records, the token already exists at send time, so the signup branch is statically unreachable | PASS (supports A2 O1; contradicts the second sentence of A1 C16) |
| PC-PRTL-12 | SOURCE | C13, O5 (static half of PR-P7), REC-13/24 | Own-main-address submit with a company name renames the commercial parent elevated; VAT only on the commercial entity; main-address archive refused | No parent rename path | After an elevated write of the address values, if a company name was submitted, the partner is not its own commercial entity, and that entity is a company, then the partner's own company-name value is cleared and the **parent commercial company is renamed elevated**. Validation drops the company name unless the edited partner is the current partner, and blocks commercial fields on sub-addresses. Archiving the main address is refused | PASS |
| PC-PRTL-13 | SOURCE / CONFIG | C15, REC-15 | Portal users allowed only when the parameter is set; other non-internal users refused; toggle debug-only | Allowed without the parameter; toggle not debug-restricted | When the base key-creation check fails: the parameter set plus a portal user means allowed; the parameter set plus any other user means an explicit refusal; the parameter unset means the original error is re-raised. The settings checkbox sits inside a block restricted to the debug-mode group | PASS |

### 3.1 Observations recorded during execution (for A3; not predeclared, so they carry no PASS or FAIL)

- **R1 (widens O2 / C01): records-pager token minting.**
  - A module-level pager helper builds previous and next URLs for documents that neighbour the current one in the caller's portal session history. For records with an access URL, it mints (ensures) and embeds each neighbour's token.
  - The helper performs no explicit read check. If the current document is the gate's elevated handle, the neighbours are browsed from that elevated environment.
  - Exposure depends on what the session-history list contains. That list is filled by downstream list routes and is not settled here.
  - Runtime proof is needed. A suggested extension to PR-P4 (PC-PRTL-17): open a document by token only, with no login and with a crafted or previous session history, and check whether neighbour token links render for records the caller cannot read.
- **R2 (C07 detail).**
  - On the token-only path, the partner resolver reads the record's customer partners, not a pid.
  - In the edit-own-message override, the thread is taken in the request's (public) environment, not elevated. Whether that read succeeds for a public user is a runtime question, and it bears on PR-P9.
- **R3 (C06/S2 detail).**
  - The signed hash is computed even when the token field is empty: the token input is then an empty value. The share-URL builder can add pid and hash while token sharing is off.
  - Such a hash is also permanent. It is noted for completeness only.
- **R4 (C09 wording).** The pid partner returned on the hash path is loaded elevated without an active-state check. This is consistent with S2: an archived customer's pid still resolves.

## 4. Runtime cases — NOT-EXECUTED (runtime device OFFLINE; ready to run)

Common preconditions for every runtime case:
- A disposable database built from the anchor commit, with `portal` plus one downstream module that ships a portal document route (for example a sales or invoicing module), and a mail catcher.
- Two companies and two customer partners with email addresses.
- The executor records the HTTP response code and body and the database state before and after each case.

| Case | A2 PR | Links | Setup / action (from A2, unchanged) | Expected (static reading) | Fail condition | Result |
|---|---|---|---|---|---|---|
| PC-PRTL-14 | PR-P1 | C09, S1, S2, REC-09/18 | Grant portal to a customer and send a document notification. Revoke. Open the saved tokenized link without login, then post in the chatter with the saved pid and hash | The document renders, and the post is attributed to the revoked customer | Access is refused, or the post is rejected or attributed to the public user | NOT-EXECUTED |
| PC-PRTL-15 | PR-P2 | C05, REC-05 | On a downstream document route, without login, request a non-existent id and an existing id without a token | The responses are distinguishable | The responses are identical (claim refuted for that route) | NOT-EXECUTED |
| PC-PRTL-16 | PR-P3 | C16, O1, REC-16/20 | Enable B2C signup. Open the share wizard on a portal document with no token, then cancel, and check the token. Reopen and send to a partner with no user | A token exists after the cancel, and the recipient gets the public token link | No token after the cancel, or a signup link is sent | NOT-EXECUTED |
| PC-PRTL-17 | PR-P4 | C01, O2, REC-01/21 (+R1 extension) | As a user without read on a portal document, call the portal-URL builder on it, and trigger a customer notification from a context without read. Extension R1: token-only view with a session history that includes unreadable ids | An access error is raised and no token is written. R1: record whether neighbour tokens render | A token is written or a URL is returned. R1: neighbour token links render for unreadable records | NOT-EXECUTED |
| PC-PRTL-18 | PR-P5 | C04, O3, REC-04/22 | Archive a portal document; separately use a document of another company. Open each by token without login | Record-only. Static expectation: both open unless a downstream route filters them | O3 holds if either opens (record which) | NOT-EXECUTED |
| PC-PRTL-19 | PR-P6 | C10, G8, REC-10/19 | Grant, revoke, re-grant the same contact | The same user id is reactivated and a new invite is sent | A new user is created, or re-grant errors | NOT-EXECUTED |
| PC-PRTL-20 | PR-P7 | C13, O5, REC-13/24 | As a portal contact whose parent is a company, submit the own-address form with a different company name | The parent company name changes | The name is unchanged, or the submit is rejected | NOT-EXECUTED |
| PC-PRTL-21 | PR-P8 | C15, O6, REC-25 | Enable portal API keys. The portal user creates a key. Revoke and call the API with the key. Re-grant and call again | The key is refused while archived. Record the behaviour after re-grant | The key is accepted while archived | NOT-EXECUTED |
| PC-PRTL-22 | PR-P9 | C07, REC-07 | Without login, post with the token only. Then post while logged in as another portal user | Anonymous: the author is the record's customer. Logged in: the author is the logged-in user | The anonymous author is public/guest, or the logged-in post is attributed to the customer | NOT-EXECUTED |

**Runtime totals: 9 cases. NOT-EXECUTED 9, PASS 0, FAIL 0.** No runtime result is claimed.

## 5. Summary of results

| Layer | Cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| SOURCE (including SOURCE+CONFIG) | 12 (PC-01..09, 11, 12, 13) | 11 | 1 (PC-01) | 0 |
| CONFIG | 1 (PC-10) | 1 | 0 | 0 |
| RUNTIME | 9 (PC-14..22) | 0 | 0 | 9 |
| **Total** | **22** | **12** | **1** | **9** |

HIGH-impact A2 verdict re-confirmation (PD-PRTL-01):
- C01 core, C02, C03, C04, C06, C08, C10, C11 and O1 are all independently re-confirmed.
- **One A2 refinement is refuted**: the "three call sites" part of C01, by PC-01 FAIL.
- The A2 VERIFIED verdict on the C01 claim itself stands.

REC item status after Proof:
- **CONTRADICTION (4).**
  - C07, C13 and C16: the static re-read supports A2's correction (PC-07, PC-12, PC-11).
  - O1: the static re-read supports A2 against the second sentence of A1 C16 (PC-11).
  - All four stay CONTRADICTION for A3. Their runtime effects are pending (PC-22, PC-20, PC-16).
- **UNKNOWN_PENDING_PROOF (10).** The static basis is confirmed for all 10. O2 is widened by R1. **All 10 remain UNKNOWN_PENDING_PROOF** until the runtime cases run.
- **MATCH (13).** Unchanged.
- **GAP (6).** Carried forward. Proof cannot close them in this scope.

## 6. A3 eligibility

**Disposition: PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.**

A3 can challenge **now** (static scope):
1. The REC classifications and counts (33 items), including the fold-ins G6→C05 and G7→C09, and the MATCH treatment of O4, O7 and O9.
2. The 13 executed static cases. In particular:
   - the **PC-PRTL-01 FAIL**: A2's call-site count was refuted by the records-pager minting site (R1);
   - whether the expected/fail pairs were truly falsifiable.
3. The 4 CONTRADICTION items (C07, C13, C16, O1). Both sources are preserved.
4. **Process deviation PD-PRTL-01.** A2's test plan was written after its source re-read began. Proof re-confirmed the HIGH-impact verdicts independently and found one refinement that did not hold, which is relevant to how much weight A2's unreplayed MED-level refinements deserve.
5. QID lineage (24 mapped, 16 with no evidence yet), the join key and freeze hash (recomputed), input integrity (the sha256 intake table and 16/16 blobs), predeclaration timing (15:02:42Z predeclared, 15:02:59Z first fetch) and clean-room compliance.
6. Observations R1–R4.

**Blocked** until the runtime device is available:
- The 9 runtime cases PC-PRTL-14..22. The most material are: revoked-customer link survival and impersonation (PC-14), minting without read including R1 (PC-17), archive and cross-company reach by token (PC-18), and parent-company rename (PC-20).
- Closing any UNKNOWN_PENDING_PROOF item, or settling the practical effect of any CONTRADICTION item.
- A full A3 → MASTER handoff is **not** eligible yet. This package is eligible for **A3 static-scope challenge only**.

## 7. Limitations

- No runtime was executed and no runtime result is claimed. A static PASS confirms a source reading only.
- The following were not read: `mail` (thread access, share-visible domain), `auth_signup` (signup token semantics) and `base` (user activation, API-key authentication, deactivation). Effects that depend on them stay runtime-pending.
- JS/SCSS assets were not read (REC GAP G3).
- The format reference (base_automation REC/PROOF) appeared after predeclaration and was used for layout only.
- No percentages, no Formal Coverage claim, no git operations. Inputs were not edited.
