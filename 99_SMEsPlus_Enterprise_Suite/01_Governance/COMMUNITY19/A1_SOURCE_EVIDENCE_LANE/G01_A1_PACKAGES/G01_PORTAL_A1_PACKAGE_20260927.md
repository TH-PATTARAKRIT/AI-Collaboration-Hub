# G01 PLATFORM_BASE — RED TEAM A1 PACKAGE — Module `portal`

| Field | Value |
|---|---|
| Role | RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `portal` |
| Lane A input | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_PORTAL_LANE_A_PASS1_20260927.md` |
| Lane A sha256 | `af066bfb151f94842d6dc6f9295cd47be5d8b31f1ee6434a530b254e60ae826f` |
| Anchor commit | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/portal/`) |
| Topic lens (not answered) | `GMVQ/G01_PLATFORM_BASE/G01_PORTAL_GMVQ_MVQ_40_V1.00_DRAFT.md` (sha256 `91b63eef1df5426f22d4bc0b296dc05cb4b3e9e1d7e1b09e38370c5d03963d3a`) |
| Freeze batch / hash | W1-B03 / `1247c218ba4e2e6a57e259427030f4350881da56a5a28c59901a20f8b2d3a5d3` (ELIGIBLE) |
| Lane B dependency | None. A1 does not wait for Lane B. |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |
| Clean-room | Neutral WHAT/WHY/RISK only. No code, schema, ORM or workflow is reproduced or recommended for reuse. Identifiers are pointers only. |

## 1. Claims

Layer for every claim: SOURCE-STATIC. Evidence paths are relative to `addons/portal/`. Blob = git SHA-1. `[SC]` = re-verified in the spot-check (Section 10).

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence (path @ blob) | Conf. |
|---|---|---|---|
| A1-G01-PRTL-C01 | WHAT: a per-record access token (random UUID) is minted lazily the first time a portal or share URL is built, and the write runs with elevated rights. WHY: documents become shareable without upfront provisioning. RISK: any user who can read a record can create a bearer credential for it. | `models/portal_mixin.py` @ d24085d8 [SC] | HIGH |
| A1-G01-PRTL-C02 | WHAT: the module has no path that rotates, expires or revokes a document token. The token is also excluded from duplication. RISK: the token is a long-lived bearer credential for the life of the record. | `models/portal_mixin.py` @ d24085d8 [SC] | HIGH (absence within module) |
| A1-G01-PRTL-C03 | WHAT: building a share URL requires the caller to pass a read check before the token is embedded. It can also add a partner id with a signed hash and signup parameters. WHY: this identifies the chatter author and eases onboarding. | `models/portal_mixin.py` @ d24085d8 [SC] | HIGH |
| A1-G01-PRTL-C04 | WHAT: the central document gate loads the record as superuser and tries the caller's normal read check first. If that fails, it falls back to a constant-time token comparison. On success it returns the record with superuser rights. RISK: once the gate passes, later operations on the returned record bypass ACL and record rules, so each downstream route must limit what it does with it. | `controllers/portal.py` @ e6b03c24 [SC] | HIGH |
| A1-G01-PRTL-C05 | WHAT: the gate distinguishes "record missing" from "access denied" with separate error kinds. RISK: a caller may be able to probe whether a record exists (existence disclosure), subject to how routes render these errors (runtime). | `controllers/portal.py` @ e6b03c24 [SC] | MED |
| A1-G01-PRTL-C06 | WHAT: the chatter author hash is an HMAC-SHA256 keyed by the database secret over the database name, the token value and the partner id. It is validated in constant time, and a parent-record hash hook exists. WHY: it binds a posting identity to one record and one partner. | `models/mail_thread.py` @ 971d3f79; `utils.py` @ b83ac0a1 [SC] | HIGH |
| A1-G01-PRTL-C07 | WHAT: a holder of a valid token or hash can post, edit their own messages and react as the resolved customer partner. RISK: a leaked link grants the ability to impersonate the customer in the chatter. | `controllers/thread.py` @ 8384c8d5; `controllers/message_reaction.py` @ bd84a5e2; `utils.py` @ b83ac0a1 | MED (not spot-checked) |
| A1-G01-PRTL-C08 | WHAT: revoking access requires the contact to currently have portal access. It syncs the edited email, clears the partner signup type (which invalidates the signup token) and archives the portal user. The user stays in the portal group, and internal users are never archived. | `wizard/portal_wizard.py` @ 368f4c1d [SC] | HIGH |
| A1-G01-PRTL-C09 | WHAT: the revoke path does not touch document access tokens or chatter hashes. RISK: a revoked customer who kept earlier share or notification links may still reach those documents through the token fallback in C04 (runtime reachability unproven). | `wizard/portal_wizard.py` @ 368f4c1d; `controllers/portal.py` @ e6b03c24 [SC] | MED |
| A1-G01-PRTL-C10 | WHAT: granting access requires a valid email that is not used as another user's login, and the contact must not already have access. The user is created with elevated rights in the partner's company (falling back to the current company), moved from the public group to the portal group, and sent a set-password invitation. | `wizard/portal_wizard.py` @ 368f4c1d [SC] | HIGH |
| A1-G01-PRTL-C11 | WHAT: the module's ACL covers only its three wizard models: create, read and write for partner managers, with no delete. It defines no groups and no record rules. WHY: document visibility is left to business modules and to the token gate. RISK: portal safety depends entirely on downstream rules and route discipline. | `security/ir.model.access.csv` @ 6506676a [SC] | HIGH |
| A1-G01-PRTL-C12 | WHAT: company scoping appears only when users are created (partner company) and when reports are rendered (record company; a multi-company record set is refused). There is no company rule on portal data. | `wizard/portal_wizard.py` @ 368f4c1d; `controllers/portal.py` @ e6b03c24 | MED |
| A1-G01-PRTL-C13 | WHAT: customer self-edits pass through a fixed allow-list of contact and address fields. Only the user's own partner and typed child addresses under the commercial entity can be edited. VAT can be edited only on the commercial entity, and archiving the main address is refused. | `models/res_partner.py` @ d8f075eb; `controllers/portal.py` @ e6b03c24 | MED |
| A1-G01-PRTL-C14 | WHAT: changing a password requires the old password and refreshes the session token. Deactivating an account requires re-typing the login and passing an interactive credential check, then runs with elevated rights and logs the user out. | `controllers/portal.py` @ e6b03c24 | MED |
| A1-G01-PRTL-C15 | WHAT: portal users may create API keys only when a config param is on, and that setting is visible only in debug mode. RISK: a hidden toggle widens external programmatic access. | `models/res_users_apikeys_description.py` @ 44c0008f; `views/res_config_settings_views.xml` @ 862a3586 | MED |
| A1-G01-PRTL-C16 | WHAT: the share wizard sends one public token link to every recipient when the record already has a token or B2C signup is off. Otherwise non-users get individual signup links. RISK: forwarding a single link spreads the same bearer authority. | `wizard/portal_share.py` @ b0491d4e | MED |
| A1-G01-PRTL-C17 | WHAT: chatter message fetch, attachment and avatar reads run with elevated rights after the thread access check, filtered to share-visible messages. RISK: the visibility set is defined in `mail` and is not proven here (G2). | `controllers/portal_thread.py` @ 363bc48c; `models/mail_message.py` @ 17976457 | MED |

## 2. Business rules
- BR1: A document can be reached externally through either the caller's own read right or a matching record token. The token path needs no login (C04).
- BR2: The token is created once, on demand, and stays stable. There is no expiry or rotation policy in the module (C01, C02).
- BR3: Creating a share link requires the sharer to have read access (C03).
- BR4: A contact holds at most one access state (none, portal or internal). Grant and re-invite require a unique, valid email (C10).
- BR5: Revoking access archives the portal user and invalidates the signup token. It does not invalidate record tokens (C08, C09).
- BR6: Customers can self-edit only allow-listed identity and address fields, only on partners they own (C13).

## 3. States / transitions
- Contact access state: none → portal (grant) → archived portal user (revoke) → portal (grant or re-invite path; runtime needed to confirm re-activation). Internal is a terminal state for this wizard, which never archives internal users.
- Document token: absent → present (lazy creation on the first URL build). The module has no transition back.
- Signup token: set (grant or re-invite) → cleared (revoke).
- Pending attachment: pending, not linked to a message → removable. Once linked it cannot be removed through the portal route.

## 4. Exceptions / failure modes
- Grant, revoke and re-invite raise user-facing errors for an invalid or duplicate email, existing access, or missing portal access (C08, C10).
- The document gate raises separate missing-record and access-denied errors (C05).
- Reports: types other than html, pdf and text are refused, and multi-company record sets are refused (C12).
- A signed hash on a model with no token field raises an error (C06).
- Address edits: a non-owned partner returns Forbidden, and archiving the main address is refused (C13).

## 5. Cross-module handoffs
- `mail`: thread and message access, notification access buttons that carry the token, pid and hash, the `/mail/view` redirect, and share-visible message filtering.
- `auth_signup`: signup preparation, the invitation template and the signup type used by revoke.
- `base`: user template, portal, public and partner-manager groups, API-key descriptions and the deactivation routine.
- Downstream business modules: inherit the portal document capability and override the access URL, warning, parent-hash hook and counters. Downstream record rules decide real visibility (C11).
- Soft references: `web_tour`, a website restricted-editor group, and an optional VAT check (accounting).

## 6. Evidence gaps (carried from Lane A, plus A1 additions)
- G1 (Lane A): the deactivation routine and user-template creation are defined outside portal and were not read.
- G2 (Lane A): the share-visible message domain and the core thread-access check are in `mail` and were not read.
- G3 (Lane A): JS/SCSS assets, including client-side token handling, were not reviewed.
- G4 (Lane A): whether the share action is reachable from contact screens can only be confirmed at runtime.
- G5 (Lane A): no token expiry or rotation was found in portal. Whether another module provides one is unknown.
- G6 (A1): how routes render the missing-record versus denied errors (existence disclosure) needs runtime evidence.
- G7 (A1): whether a revoked user's earlier links still open documents needs runtime evidence.
- G8 (A1): whether re-granting access re-activates the archived user or creates a new one is not proven statically here.

## 7. CRQ candidates
- CRQ-PRTL-01: Should external document credentials have expiry, rotation and explicit revocation, independent of the user account? (C01, C02, C09)
- CRQ-PRTL-02: Should an access gate return a least-privilege handle instead of an all-rights handle, so that each route's permitted operations are explicit? (C04)
- CRQ-PRTL-03: Should revoking customer access also invalidate all outstanding document links and chatter identities for that customer? (C08, C09)
- CRQ-PRTL-04: Should minting a share credential require a distinct share permission instead of plain read? (C01, C03)
- CRQ-PRTL-05: Should external access carry tenant or company scoping in the portal layer itself? (C11, C12)
- CRQ-PRTL-06: Should the API-key enablement for external users be a governed, audited setting instead of a hidden toggle? (C15)
- CRQ-PRTL-07: Should missing and forbidden external requests be indistinguishable to the caller? (C05)

## 8. Contradictions
- None were found between Lane A and the source. Every spot-checked claim matched.
- Refinement, not a contradiction: Lane A P-B7 omits that revoke also syncs the edited partner email before archiving. This is CONFIRMED-FROM-SOURCE and folded into C08.
- CANDIDATE tension: the GMVQ lens topic "revocation takes effect across saved links" versus C09, where revoke leaves record tokens intact. This needs runtime proof.

## 9. Provenance
- Input: Lane A PASS-1 packet (sha256 above), 31 blobs at the anchor commit.
- Spot-check source: `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/portal/<path>`, fetched on 2026-09-27 into the session scratchpad and not committed.
- The GMVQ bank was used only as a topic lens. No QID is answered and the bank was not edited.

## 10. Spot-check log (6 files; `git hash-object` vs the Lane A blob)

| # | File | Recorded blob | Recomputed | Claim content checked | Result |
|---|---|---|---|---|---|
| 1 | `models/portal_mixin.py` | d24085d8da0a56a8b078d0d073aa85d6016f6d79 | identical | lazy UUID token with elevated write; no expiry/rotation; read check before embedding in share URL; not copied | MATCH |
| 2 | `controllers/portal.py` | e6b03c24fa227c362a20d6811cfa5c59cf717f02 | identical | superuser load, read check, constant-time token fallback, superuser record returned; separate missing/denied errors | MATCH |
| 3 | `wizard/portal_wizard.py` | 368f4c1d369892aaefb4e16b5632e6e7b3486cc8 | identical | revoke: portal-only precondition, signup type cleared, user archived, internal users untouched; record tokens untouched | MATCH |
| 4 | `security/ir.model.access.csv` | 6506676a9e55e5ccb7f2d578b1c7804efbb2142e | identical | 3 rows, partner manager, no unlink; no rules | MATCH |
| 5 | `utils.py` | b83ac0a1415ab9c1c5b7acd8c8d5c2c38c3417d1 | identical | constant-time hash and token validation | MATCH |
| 6 | `models/mail_thread.py` | 971d3f790238ae0359f6236fc1a8230b50a97ed0 | identical | HMAC-SHA256 keyed by the database secret | MATCH |

## 11. Limitations
- SOURCE-STATIC only. Source presence does not prove runtime reachability, and statements of absence cover only this module's files.
- There is no Formal Coverage claim and no percentages. A2 verification, Lane B corroboration and Proof are still pending.
- Claims that were not spot-checked (C07, C13–C17) rely on Lane A blob pointers and carry at most MED confidence.
