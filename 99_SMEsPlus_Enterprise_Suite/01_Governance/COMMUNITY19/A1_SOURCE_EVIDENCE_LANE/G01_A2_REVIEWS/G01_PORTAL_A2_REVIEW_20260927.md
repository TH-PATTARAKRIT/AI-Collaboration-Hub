# G01 PLATFORM_BASE — RED TEAM A2 Review — `portal`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional/semantic verifier of A1 conclusions). Independent of A1. The A1 package was not repaired or rewritten |
| Group / Module | G01 PLATFORM_BASE / `portal` |
| A1 package (input, immutable) | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_PORTAL_A1_PACKAGE_20260927.md` |
| A1 package sha256 | `aef3388923e91d7bd8659b6a7a3ab6da21898500decb9b891f8bb807c6ed957d` |
| Lane A packet (input, immutable) | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_PORTAL_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `af066bfb151f94842d6dc6f9295cd47be5d8b31f1ee6434a530b254e60ae826f`. Matches the value recorded in the A1 header |
| Question bank (topic lens only) | `GMVQ/G01_PLATFORM_BASE/G01_PORTAL_GMVQ_MVQ_40_V1.00_DRAFT.md`, sha256 `91b63eef1df5426f22d4bc0b296dc05cb4b3e9e1d7e1b09e38370c5d03963d3a` (W1-B03, ELIGIBLE). No QID is answered |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/portal/` (raw.githubusercontent.com) |
| Test plan | Scratchpad `a2_prtl_utm/test_plan_predeclared.txt`, sha256 `38a1b67a0ede45182ea96ae7bad67356873fd6a04464528b84b2640ff3d68065`. Its scope is the dispatch brief's focus list, which was fixed before any work began. The file itself was written at 2026-09-27 14:56 UTC, after the source re-read had started. Stated here for lineage honesty |
| Lane B | No Lane B runtime evidence exists in the repository for this module. This is not treated as a failure (see section 6) |
| Date | 2026-09-27 |
| **Disposition** | **A2 PASS WITH FINDINGS** |

Disposition reasons:
1. All 17 A1 claims were re-read against the source: 14 are VERIFIED and 3 are PARTIAL (C07, C13, C16). None is NOT_VERIFIED, and no HIGH claim overstates its source.
2. The central contradiction candidate (C09: document links outlive revoke) is confirmed at the static level and made stronger. The token gate never looks at the user account, and the chatter identity hash is bound to the unchanging record token. Runtime proof is still required.
3. A1 gap G8 (re-grant) is settled statically: re-grant reactivates the same archived user.
4. A1 omitted several behaviours that matter for a customer portal. The main ones are O1 (the share wizard mints the token when it is opened, so the individual signup-link branch looks unreachable for portal documents), O2 (token-minting paths without an explicit read check), O3 (the token gate has no archive or company filter) and O5 (a B2B portal contact can rename the parent company). These are routed to Reconciliation/Proof. They are not A1 defects that block handoff.

Clean-room note: every statement is a neutral WHAT/WHY/RISK paraphrase. Identifiers are evidence pointers only. No vendor code is reproduced or recommended for reuse. No percentages. No Formal Coverage claim. No git operations were performed. Source copies are held only in the scratchpad (`a2_prtl_utm/portal/`).

## 1. Test plan (executed as declared)

| Test | Scope | Method | Result |
|---|---|---|---|
| T1 Lineage | A1 package, Lane A packet, bank | sha256 of each file, compared with the A1 header | PASS. Lane A and bank hashes match the A1 header |
| T2 Blob integrity | 17 cited files (portal_mixin, mail_thread, mail_message, res_partner, res_users_apikeys_description, res_config_settings, controllers portal/portal_thread/thread/message_reaction/mail, utils, portal_wizard, portal_share, ACL csv, settings view, manifest) | Fetch at the anchor; `git hash-object` compared with the Lane A table | PASS. 17 of 17 match the recorded SHA-1 |
| T3 Semantic re-read | All HIGH claims (C01–C04, C06, C08, C10, C11) and all MED claims (C05, C07, C09, C12–C17) | Full read of portal_mixin, mail_thread, utils, portal_wizard, portal_share, res_partner, thread, message_reaction, mail controller, portal_thread and the API-key model. Targeted read of controllers/portal.py (gate, address submit and validation, security, deactivate, attachment removal, report) | Done. Section 2 |
| T4 Contradiction / CRQ focus | Lazy elevated token creation; no rotation or expiry; token fallback returning an all-rights record; revoke semantics including C09; no record rules; re-grant (G8) | Trace every token-minting call site. Trace the gate inputs (does it consult user, company or active state?). Trace revoke side effects and re-grant user lookup | Done. Sections 2 and 3 |
| T5 Business meaning | Customer-portal access control in a multi-company SaaS | Adversarial re-read of the share, notification, gate, chatter, address and account paths | Done. Sections 3 and 4 |
| T6 Lane B classification | Every claim | NOT_APPLICABLE / UNCORROBORATED / MISSING_REQUIRED_RUNTIME_PROOF | Done. Section 5 |
| T7 Proof requirements | Runtime-inherent claims and findings | Falsifiable cases, each with an expected result and a fail condition | Done. Section 6 |

## 2. Claim verdict table

Verdict key:
- VERIFIED: a source re-read supports the claim as written.
- PARTIAL: the core is supported, but part of the claim is inaccurate or its scope is materially incomplete.
- NOT_VERIFIED: the source does not support the claim.
- OUT_OF_SCOPE: the claim cannot be judged within module scope.

| Claim | A1 conf. | A2 verdict | A2 basis (source re-read, paraphrased) |
|---|---|---|---|
| C01 | HIGH | VERIFIED | The ensure-token helper writes a random UUID with elevated rights only when the token is empty. Refinement: there are three minting call sites, not one. They are the share-URL builder, the portal-URL builder and the customer notification grouping. Only the share-URL builder performs an explicit read check (O2). |
| C02 | HIGH | VERIFIED | The module has no rotate, expire or clear path for the token. The token field is excluded from duplication. Consequence A1 did not draw: the chatter hash is computed over the token, so hashes never change either (O4). |
| C03 | HIGH | VERIFIED | The share-URL builder runs a read check before it embeds the token. It optionally adds pid plus a signed hash and the partner's signup parameters, and in redirect mode it points at the generic mail-view route. |
| C04 | HIGH | VERIFIED | The gate loads the record under the superuser identity, confirms it exists, tries the caller's read check, and on failure accepts a constant-time match against the stored token. It returns the superuser-bound record on both success paths. Omission: the gate consults no active or archive state, no company and no user state (O3). |
| C05 | MED | VERIFIED | Separate missing-record and access-denied errors are raised. Counter-evidence A1 did not cite: the only in-module caller (pending-attachment removal) turns both into one identical message, so in-module disclosure is absent. Downstream routes remain unproven (G6). |
| C06 | HIGH | VERIFIED | HMAC-SHA256 keyed by the database secret over the database name, the post-token field value and the partner id. Validation is constant time. A parent-hash hook defaults to none. A missing token field raises an error. |
| C07 | MED | **PARTIAL** | The core is supported: a valid hash+pid or token resolves a partner who becomes the post author, can edit their own messages and can react. Missing scope condition: author substitution and the edit rule apply only when the request runs as the public (not logged-in) user. Reactions use it only when the mail core resolved no partner. With a token only, the resolved identity is the first customer partner of the record, so a leaked link lets an anonymous holder act as that customer. |
| C08 | HIGH | VERIFIED | Revoke requires active portal status. It syncs the edited email, clears the partner signup type and archives the user only if they are a portal user. Group membership is unchanged. Note: the claim that the signup token is invalidated rests on an in-source comment and on auth_signup semantics, which were not read here. |
| C09 | MED | VERIFIED (static) | Revoke touches no document token or hash. Stronger than A1 stated: the gate fallback and the chatter token/hash validators take only the record and the supplied secret as input. None of them consults the requesting user or partner's account state. Runtime reachability through downstream public routes is still to be proven (PR-P1). |
| C10 | HIGH | VERIFIED | Preconditions (valid and unused login email, no existing portal or internal access) are enforced through the email-state compute. The user is created elevated under the partner's company, falling back to the current company, with only that one company allowed. The user is activated, portal is added, public is removed, signup is prepared and the invitation is sent. **Settles G8:** the linked-user lookup includes archived users, so a re-grant reactivates the same archived user instead of creating a new one. |
| C11 | HIGH | VERIFIED | Three ACL rows, all partner-manager only, with create, read and write and no delete. The manifest data list contains no group or record-rule file. |
| C12 | MED | VERIFIED | Company handling appears only in user creation (C10) and report rendering (record company; a set spanning more than one company is refused). The gate and chatter paths have no company check (O3). |
| C13 | MED | **PARTIAL** | The allow-list (which also includes a second zip alias and the company-name field), the own/child-address ownership rule, VAT only on the commercial entity and the refusal to archive the main address are all verified. Materially incomplete: when a contact edits their own main address and supplies a company name, the submit path renames the parent commercial company with elevated rights (O5). Any contact can also edit every invoice, delivery or other address under the whole commercial entity. |
| C14 | MED | VERIFIED | Password change requires the old password and a matching confirmation, then refreshes the current session token. Deactivation requires re-typing the login and an interactive credential check, then calls the deactivation routine elevated and logs out. Security pages send anti-framing headers. |
| C15 | MED | VERIFIED | When the base check fails, API-key creation is allowed only if the parameter is set and the user is a portal user. Other non-internal users are refused. The settings toggle sits in a debug-only block. Note: changing it still requires settings access, so the setting is hidden, not unguarded. |
| C16 | MED | **PARTIAL** | The dispatch rule is verified: every recipient gets the public path when the record has a token or B2C signup is off. Inaccurate: it is not one identical link. Each recipient's link carries its own pid and hash, and all of them share the same bearer token. Material omission: the wizard mints the token when it is opened, which appears to make the signup branch unreachable for portal documents (O1). |
| C17 | MED | VERIFIED | Message fetch validates thread access (core check, then hash/pid or token), then runs an elevated fetch restricted to the website-message types, the share-visible domain (defined in mail, G2) and non-empty messages. The avatar route validates the thread the same way. |

Verdict counts: VERIFIED 14, PARTIAL 3, NOT_VERIFIED 0, OUT_OF_SCOPE 0.

### 2b. A1 gaps and CRQs: what the source settles

- G8: settled statically (C10). A re-grant reactivates the same archived user. A runtime confirmation is still listed (PR-P6), because user creation and activation behaviour also depend on base.
- G5: within the module, confirmed absent. Other modules are not examined.
- CRQ-PRTL-03: the source confirms the premise. Revoke leaves document tokens and chatter hashes valid. Because hashes derive from the token, invalidating the token alone would also invalidate every hash for that record.
- CRQ-PRTL-04: the premise is incomplete. Minting does not always sit behind an explicit read check (O2).
- CRQ-PRTL-07: the in-module caller already hides the difference. The CRQ applies to downstream routes.

## 3. Semantic findings (business meaning: customer-portal access control, multi-company SaaS)

- S1 **The record token is the real access principal, not the portal user.** After first issue, reaching a document externally depends only on knowing the token. User identity, active state, company membership and revocation play no part. The portal user account governs only the logged-in `/my` area and ACL-based reads. For SaaS access control this means revoking a customer is account-level, not document-level. A1 captured this in pieces (C04, C09) but did not state it as the governing model.
- S2 **The chatter identity is bearer-derived.** The signed hash binds (database, record token, partner). It never expires, survives revoke and is valid for any pid it was issued for. An anonymous holder of a notification link can post as that customer indefinitely (C06, C07, C09).
- S3 **All-rights handle.** The gate returns a superuser-bound record even when the caller passed the ordinary read check. So downstream code handles an elevated record in both the token case and the logged-in case. A1 C04 is correct. The business consequence is that the least-privilege boundary depends on the discipline of every downstream route (CRQ-PRTL-02 stands).
- S4 **Company scoping is an account attribute, not a data boundary.** A portal user is pinned to a single allowed company. Which company is chosen depends on the partner's company or, if that is empty, on the grantor's active company, so it is non-deterministic for shared partners. The token path ignores company entirely.

## 4. Omissions (not in A1 claims)

| ID | Omission | Evidence (path @ blob) | Severity |
|---|---|---|---|
| O1 | The share wizard computes the share link on open (default values and a compute), and that mints the token. At send time the record therefore already has a token, so all recipients get the public link. The individual signup-link branch looks unreachable for portal documents shared through the wizard. Merely opening and cancelling the wizard leaves a permanent token. | `wizard/portal_share.py` @ b0491d4e; `models/portal_mixin.py` @ d24085d8 | HIGH (static), runtime proof PR-P3 |
| O2 | Token-minting paths without an explicit read check: the public-named portal-URL builder, and customer notification grouping, which mints elevated whenever a message notifies the customer. Enforcement then relies on implicit ORM read enforcement when the token field is read, which is not proven here. | `models/portal_mixin.py` @ d24085d8; `models/mail_thread.py` @ 971d3f79 | MED, PR-P4 |
| O3 | The token gate has no active/archive filter (it only checks existence), no company check and no document-state check. Archived or cancelled documents, and documents of any company, stay reachable by token unless a downstream route filters them. | `controllers/portal.py` @ e6b03c24 | MED, PR-P5 |
| O4 | Hash lifetime is tied to token lifetime. With no rotation there is no way to invalidate an individual customer's chatter identity without invalidating everyone's. | `models/mail_thread.py` @ 971d3f79; `utils.py` @ b83ac0a1 | MED |
| O5 | B2B master-data exposure: a portal contact editing their own main address can submit a company name, and the submit path then renames the parent commercial company with elevated rights. Other commercial fields on sub-addresses are blocked. | `controllers/portal.py` @ e6b03c24; `models/res_partner.py` @ d8f075eb | MED, PR-P7 |
| O6 | Revoke leaves the user in the portal group, and re-grant reactivates the same user. Whether that user's API keys (C15) and other sessions are refused while archived and restored on re-grant is decided outside this module. | `wizard/portal_wizard.py` @ 368f4c1d; `models/res_users_apikeys_description.py` @ 44c0008f | MED, PR-P8 |
| O7 | The pending-attachment removal route is public and uses the gate with the attachment's own token. It deletes only pending, unlinked attachments. A1 mentions it only under states. | `controllers/portal.py` @ e6b03c24 | LOW |
| O8 | The authenticated route that writes a message's internal flag has no portal-specific guard (Lane A P-S8). A1 did not carry it into a claim or gap. Its safety rests on mail ACL and rules, which were not read. | `controllers/portal_thread.py` @ 363bc48c | LOW (carried gap) |
| O9 | The grant wizard expands the selected partners to their contact/other children using elevated reads. The grantor may be shown children they could not otherwise read. | `wizard/portal_wizard.py` @ 368f4c1d | LOW |

## 5. Lane B classification

No Lane B evidence exists in the repository for `portal`. No claim is marked FAIL for lack of Lane B.

| Class | Claims |
|---|---|
| NOT_APPLICABLE (definitional or static structure; runtime observation adds nothing) | C02, C06, C11, C12, C15 |
| UNCORROBORATED (source-verified; runtime observation would corroborate but is not required) | C03, C08, C10, C13, C14, C17 |
| MISSING_REQUIRED_RUNTIME_PROOF (inherently runtime: reachability, rendering or cross-module effect) | C01 (minting without read, O2), C04 (downstream use of the elevated handle, O3), C05 (G6), C07, C09 (G7), C16 (O1) |

## 6. Proof requirements

Each case lists its setup, the expected result based on the static reading, and the condition under which the static reading fails.

| ID | Claim(s) | Setup / action | Expected (per static reading) | Fail condition |
|---|---|---|---|---|
| PR-P1 | C09, S1, S2 | Grant portal access to a customer and send a document notification. Revoke. Open the saved tokenized link in a session with no login, then post in the chatter using the saved pid and hash. | The document renders and the post is attributed to the revoked customer. | Access is refused, or the post is rejected or attributed to the public user. |
| PR-P2 | C05, G6 | On a downstream document route, request an id that does not exist and an existing id without a token, both without login. | The two responses are distinguishable (claim holds). | The responses are identical (claim refuted for that route). |
| PR-P3 | C16, O1 | Enable B2C signup. Open the share wizard on a portal document with no token, then cancel. Check the token. Reopen and send to a partner who has no user account. | A token exists after the cancel, and the recipient receives the public token link, not an individual signup link. | No token after the cancel, or a signup link is sent. |
| PR-P4 | C01, O2 | As a user with no read right on a portal document, call the portal-URL builder on it, and trigger a customer notification from a context without read. | An access error is raised and no token is written. | A token is written, or a URL is returned. |
| PR-P5 | C04, O3 | Archive a portal document, and separately use a document of a company the requester does not belong to. Open each with its token and no login. | Downstream route discipline is unknown, so record whether each opens. Static expectation: both open unless a downstream route filters them. | Record which it is. The O3 omission holds if either opens. |
| PR-P6 | C10, G8 | Grant, revoke, then re-grant the same contact. | The same user id is reactivated and a new invitation is sent. | A new user is created, or re-grant errors. |
| PR-P7 | C13, O5 | As a portal contact whose parent is a company, submit the own-address form with a different company name. | The parent company's name changes. | The name is unchanged, or the submit is rejected. |
| PR-P8 | C15, O6 | Enable portal API keys. The portal user creates a key. Revoke, then call the API with the key. Re-grant and call again. | The key is refused while archived. Record whether it works again after re-grant. | The key is accepted while archived. |
| PR-P9 | C07 | With no login, post with the token only (no pid or hash). Then repeat while logged in as another portal user. | Anonymous: the author is the record's customer. Logged in: the author is the logged-in user, not the customer. | The anonymous author is the public user or guest, or the logged-in post is attributed to the customer. |

Proof requirement count: 9.

## 7. Limitations

- SOURCE-STATIC only. `mail`, `auth_signup` and `base` (the core thread-access check, share-visible domain, signup token handling, deactivation routine and API-key authentication) were not read. Effects that depend on them are marked as proof requirements, not as verified.
- JS/SCSS assets were not reviewed (A1 G3 carried). Client-side token handling is unverified.
- `models/mail_message.py` was integrity-checked and scanned for token use, but not read in full.
- The test plan file was written after the source re-read had begun (see header). Its scope matches the dispatch brief.
- No Formal Coverage claim and no percentages. The GMVQ bank was used only as a topic lens (revocation across saved links, company isolation). No QID is answered.
