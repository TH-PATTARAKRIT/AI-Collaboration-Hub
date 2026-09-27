# G01 PLATFORM_BASE — RED TEAM A2 DELTA Review of A1 Delta D1 — `mail`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 DELTA (functional/semantic verifier). Independent of A1; the A1 delta is verified, not repaired |
| Group / Module | G01 PLATFORM_BASE / `mail` ("Discuss") |
| Reviewed input | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_MAIL_A1_DELTA_D1_20260927.md` sha256 `e3febb2e0fc0b50fd14b69c362798d673517d3e9eb1696980b18b380075f8c7f` |
| Parent A1 package | `G01_A1_PACKAGES/G01_MAIL_A1_PACKAGE_20260927.md` sha256 `dde12053f968e2b55bc906da7175840d119386bb051f6b21a80885e209ff092f` (matches the D1 header) |
| Upstream Lane A PASS-2 | `G01_LANE_A_PASS2/G01_MAIL_LANE_A_PASS2_20260927.md` sha256 `b2cdaa0cf60f6554828d7fcabd97ebb2ebd3735df090d9fb446f3bef8a6ea21b` (matches the D1 header) |
| Base A2 mail review (reference, so verdicts are not duplicated) | `G01_A2_REVIEWS/G01_MAIL_A2_REVIEW_20260927.md` sha256 `e587bf12e221a2d8be6e32f056ee37d1c4b88dbc8495a87a7b6e0d80287d56e8` |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, fetched raw; blob SHA-1 computed with `git hash-object` (scratch only) |
| Lane B | None supplied |
| Date | 2026-09-27 |
| **Disposition** | **A2 DELTA PASS WITH FINDINGS.** Every D1 item is traceable and none is refuted. 11 items are PARTIAL. Most important: D11's composer elevation description is inaccurate in two respects, and D03 understates outbound request volume. D1 also conflicts with the base A2 review in three places (K1–K4 status, C28 guest context, C29 base). These go to REC; D1 is not returned to A1 |

Clean room: this review states behaviour in neutral terms and reproduces no vendor code. Identifiers and ~L pointers are evidence pointers only. There are no percentages, no Formal Coverage claim and no git operations.

## 1. Test plan (predeclared)

The plan file is `scratchpad/a2_delta_d1/TEST_PLAN_MAIL.md`, sha256 `a95aa733dc9fa6b3d74b28075676295d3becd253138798e7ea688812cdbf1d24`. Declared timestamp: **2026-09-27T15:03:14Z**. It was written after the input sha256 intake and before any source fetch or re-read.

| TP | Test | Pass criterion | Result |
|---|---|---|---|
| TP-M1 | Lineage: sha256 of D1, parent, PASS-2 and base A2 | D1 header values match | PASS |
| TP-M2 | Re-fetch the SC set P1–P18 plus P16/P25/P28/P29/P30/P19/P27, `models/__init__.py`, `models/mail_push_device.py` and `controllers/webclient.py`; `git hash-object` | Match the D1 key | PASS: every blob with a D1 key value matches (P1–P19, P25, P27–P30). The extra A2 files have no D1 key value: `__init__` 553bd767, `mail_push_device` 5a5a521b, `webclient` da5b8d5b. `odoo/http.py` ebfc2ac8 was re-fetched for the framework cookie defaults |
| TP-M3 | Independent semantic re-read of HIGH items and contradictions: guest cookie flags, publisher egress and plain-http default, SSRF link preview and web push, K5/K6/K7, template save-time vs render-time, composer elevation, author bus payload | The WHAT holds at the stated scope | Done (section 3) |
| TP-M4 | MED claims D13, D16 | Re-read where fetched | Partly (only P19, P25, P28 re-read) |
| TP-M5 | Disposition changes follow from verified claims | Coherent | Done |
| TP-M6 | Conflict and duplicate sweep against base A2 | Flagged, not re-verdicted | Section 4.3 |
| TP-M7 | Lane B classification | Never FAIL | Section 5 |
| TP-M8 | Proof requirements, deduplicated against base PR-01 to PR-13 | Falsifiable | Section 6 |

Verdict scale: VERIFIED, PARTIAL, NOT_VERIFIED, OUT_OF_SCOPE.

## 2. Evidence integrity (TP-M2)

HTTP 200 and a blob match for P1 692708b5, P2 9c7c2192, P3 18515419, P4 153d3026, P5 e660da83, P6 05603784, P7 433ff84b, P8 d72aacbe, P9 32fdf959, P10 57f7a65a, P11 25ef82e3, P12 f95b8f53, P13 edbfc4f5, P14 1f556c60, P15 4b4125ed, P16 4a70962d, P17 66d9cd79, P18 aefe528e, P19 23b0e077, P25 3d5c8fb2, P27 55106089, P28 29275551, P29 0219605e and P30 44c9e2d2. There were no mismatches. D1's 18-of-18 spot-check is reproduced independently. P20–P24, P26, P31, P32 and P33 were not re-fetched.

## 3. Verdict table

### 3.1 Disposition changes (D1 section 1)

| Item | D1 disposition | A2 verdict | A2 basis |
|---|---|---|---|
| G2 (wizards) | CLOSED-STATIC with N2/N3 residual | **PARTIAL** | The composer part is verified (D07, D08). The closure also rests on D13 (preview, reset, follower edit, blacklist, partner merge, activity schedule), and A2 re-read only preview and the access CSV for those. A1 itself marks D13 MED/not re-fetched, and D11 is inaccurate (below). A closure is too strong. The accurate status is NARROWED |
| G3 (guest decorator, Store) | CLOSED-STATIC; N1 residual | VERIFIED | The decorator and guest resolution were re-read (D01, D02). A2 also answers the framework-default half of N1 (AO-M1) |
| G4 (publisher egress) | CLOSED-STATIC | VERIFIED | D05 and D06 were re-read in full |
| G5 | NARROWED | VERIFIED | Link preview and web push were studied |
| G8 | NARROWED | VERIFIED | Follows from D14 |
| G9 | UNCHANGED OPEN | VERIFIED | No change asserted |
| G1, G6, G7, G10, G11 | UNCHANGED | OUT_OF_SCOPE | Not addressed |
| C10 | REAFFIRMED | VERIFIED | The rule file has no company term. Converges with base A2 C10 |
| C11 | REFINED by D14 | VERIFIED | Converges with base A2 SF-05. The two are one finding, not two |
| C15 | REFINED by D01, D02 | VERIFIED | |
| C18 | AMENDED by D09–D12, K5 | **PARTIAL** | The save-time and render-time split is verified (D09, D10, D12). But the amendment imports D11's inaccuracies and K5's ambiguity |
| C25 | REFINED by D05, D06 | VERIFIED | |
| C28 | REFINED by D02 | **PARTIAL (conflict)** | D1 keeps C28's premise that the upload, delete and zip routes "accept a guest context", with per-route coverage left to N1. Base A2 already found (C28 PARTIAL) that the zip route does not attach guest context and that delete works by ownership. D1 does not carry this |
| C29 | EXTENDED by D03–D05 | VERIFIED (conflict noted) | The extension is sound. Note that base A2 marked C29 PARTIAL because the GIF provider receives search terms, not message content. D1 extends a claim that is itself partly overstated |
| C24 | UNCHANGED; see K6 | VERIFIED | |
| H6, corrected by K7 | CORRECTED | VERIFIED | The model is defined in `mail` and imported by its model roster (`models/__init__` imports `update`) |
| CRQ-MAIL-01 | REFINED, OPEN | VERIFIED | Same as base PR-04 |
| CRQ-MAIL-05 | OPEN; G3 dependency removed | VERIFIED | |
| CRQ-MAIL-07 | REFINED, OPEN | VERIFIED | Follows from D08 |
| CRQ-MAIL-09 | OPEN; dependency moved to N1 | **PARTIAL (conflict)** | Base A2 already answered part of this from source: zip has no guest context, and delete is ownership-based with a guest token. D1's dependency chain ignores that |
| CRQ-MAIL-11 | REFINED, OPEN | **PARTIAL** | The path it names ("non-editors can edit the body only when no template is set") is misdescribed (see D11) |
| CRQ-MAIL-02, 03, 04, 06, 08, 10, 12 | UNCHANGED | OUT_OF_SCOPE | |
| K1–K4 | "UNCHANGED (still CONFIRMED-FROM-SOURCE)" | **PARTIAL (conflict)** | Base A2 found K1 CONFIRMED but REFINED (the document operation is write, not post), K3 WIDER (three company-emptying sites) and K4 PARTIAL (controllers filter params before the helper). D1's "unchanged" status does not reflect the A2 outcome |

### 3.2 New claims (D01–D16) and contradictions (K5–K7)

| Item | A1 conf. | A2 verdict | A2 basis (independent re-read) |
|---|---|---|---|
| D01 | HIGH / LOW | VERIFIED | The secret is a random UUID, restricted to the Settings group and not copied. The cookie is set HttpOnly with a 365-day expiry and no Secure or SameSite argument. A2 addition (AO-M1): the framework cookie wrapper defaults to secure off and SameSite none (http ~L1784–1790), so the app layer emits neither attribute. No rotation or revocation routine was seen |
| D02 | HIGH | VERIFIED | The decorator reads the cookie, then a sudo load, a constant-time compare and a non-elevated return (empty on mismatch). The context guest is honoured only when it is a real guest-model instance. The timezone write happens only when the cursor is writable. There is a websocket request fallback |
| D03 | HIGH / LOW | **PARTIAL** | Confirmed: GET with redirects, 3 s timeout, streamed, browser-like user agent plus an identifying header, and no address filter. Understated: (a) the per-message cap counts only *successful* previews and breaks after more than 5 (up to 6). (b) The per-domain throttle counts only stored previews in the last 10 s. Failed or non-HTML fetches therefore increment neither, so the number of outbound requests per message is bounded only by the number of links. (c) For a text/HTML response the page title or Open Graph fields are stored and broadcast to message readers. That is response-reading SSRF for HTML targets (PR-MD2, PR-MD3) |
| D04 | HIGH / LOW | VERIFIED | POST to the stored endpoint, 5 s timeout, 12 h token, and only `.invalid` refused. A2 addition (AO-M2, partly answering G14): device registration is a public model method. It requires only the server's own public VAPID key, stores the caller-supplied endpoint with no scheme or host check, and can reassign an existing endpoint row to the caller. The registry itself is ACL'd to the Settings group but written under sudo |
| D05 | HIGH | VERIFIED | Payload: db uuid, db name, create date, version, active users, users active in the last 15 days, share users, active share users, installed application names, enterprise code, base URL and language. When the running user's partner has a company, that company's name, email and phone are added. The job runs as the root user, weekly, hidden from the default job list, with priority 1000 and first run after 7 days. User counts are unfiltered by company |
| D06 | HIGH | VERIFIED | The URL is a file-only option whose default uses plain http. The job posts with a 30 s timeout, parses the response as a literal, and posts each message elevated as a comment in the all-employees channel addressed to the root partner, swallowing per-message errors. Six `database.*` parameters are overwritten. The null mode re-raises. The job sits in a no-update block. Note: whether plain-string remote messages are escaped on post was not re-read |
| D07 | HIGH | VERIFIED | Internal users have read, write and create on the composer but not delete. The creator-only rule covers read and write. Scheduling is refused unless the wizard is in single-record comment mode |
| D08 | HIGH / MED | VERIFIED | A domain is searched in the caller's environment, else an explicit id list is used. Mail rows are created under sudo per batch. The batch size is a parameter, else 50. The responsible-user field is declared and not otherwise referenced in the file (G12 confirmed) |
| D09 | HIGH | VERIFIED | The restriction predicate is: not unrestricted-model, no private bypass marker, not admin (Access Rights), not editor |
| D10 | HIGH | VERIFIED | Templates are flagged unrestricted. On create, write and translation update, a non-editor saving unsafe content is refused; only superuser mode is exempt. Templates also reject abstract models and test-render on save. Asymmetry (AO-M3): the render predicate exempts Access Rights admins, but the save check does not. An Access Rights admin without the editor group can render unrestricted content in other models yet cannot save unsafe templates |
| D11 | HIGH / MED | **PARTIAL** | Equality-based elevation for non-editors is confirmed. Two inaccuracies. (1) Language rendering, on equality, runs the parent render on a **full superuser** record, not under the bypass marker. Record reads for the template's language expression skip ACLs and rules. (2) The composer wizard overrides the edit rule: outside mass mail, the body is **always** editable, including by non-editors on a template-based composer. Only mass mail falls back to "editor or no template". The body then renders elevated only while it still equals the template (sanitised comparison), so the equality test is the actual guard. D1's sentence "non-editors can edit the body only when no template is set (and not in mass mail)" is inverted for comment mode |
| D12 | HIGH | VERIFIED | Setting the parameter to a false value makes internal users imply the editor group, and a true value removes it. Seed is 1, and the system group implies editor. Precision: the toggle tests the value's truthiness, so the string forms "0" and "False" count as true (restricted) |
| D13 | MED | **PARTIAL** | A2 confirmed only that the preview access row is internal-user and that the preview model list is filled with sudo. Reset, follower edit, blacklist removal, partner merge and activity scheduling (P20–P24) were not re-read |
| D14 | HIGH / LOW | VERIFIED | The read check and existence probe run as the current environment, with the unresolved company note. The author, when it has a non-public user, receives the payload built as its main user with no check of its own. The payload has author, body, date, type, filtered notifications, thread model label and display name. The caller is the failure path in outgoing mail. Duplicate of base A2 SF-05 and PR-04 |
| D15 | HIGH / LOW | VERIFIED | Templates have no company field, and the source warns of a cross-company partner merge. Activities have no company field. Plans have a company defaulting to the current one, and plan lines take it through a related field. Plan lines have a company-check attribute, and no automatic company-check flag was found. The only plan rules are 1=1 rules for the Settings group, and internal users have read-only ACL on plans |
| D16 | MED | **PARTIAL** | Alias domain and company validation and the current-company default domain are confirmed (P25 ~L45, ~L101–175, ~L259). "Created in the owning record's company" depends on the alias mixin (P26), which was not re-read |
| K5 | — | **PARTIAL** | The seed is 1 and only system admins get the editor group, as stated. But the catalogue comment is ambiguous: "not activated by default" can be read as "the editor group for all internal users is not activated", which agrees with the seed. This is a documentation inconsistency at most and has no effect on behaviour |
| K6 | — | VERIFIED | The comment says the overdue-activity cleanup is 0 (skipped) by default. The seed is 3. Unambiguous |
| K7 | — | VERIFIED | The publisher model is defined in `mail` and imported by its roster |

**Counts.** Disposition changes (23 rows): VERIFIED 15, PARTIAL 6, NOT_VERIFIED 0, OUT_OF_SCOPE 2. New claims (16): VERIFIED 12, PARTIAL 4. New contradictions (3): VERIFIED 2, PARTIAL 1. **Total: VERIFIED 29, PARTIAL 11, NOT_VERIFIED 0, OUT_OF_SCOPE 2.**

### 3.3 New CRQ candidates (traceability check; no verdicts counted)

| CRQ | A2 note |
|---|---|
| CRQ-MAIL-13 | Well-formed. Scope should add failed-fetch volume and HTML metadata read-back (D03 PARTIAL) |
| CRQ-MAIL-14 | Partly answered statically (AO-M2): any caller of the registration method can set an arbitrary endpoint. Who can reach that method over RPC remains a runtime question |
| CRQ-MAIL-15 | Well-formed. Plain-http default is confirmed statically |
| CRQ-MAIL-16 | Well-formed |
| CRQ-MAIL-17 | Well-formed. Scope should include comment-mode body editability and full-superuser language rendering (D11) |
| CRQ-MAIL-18 | **Duplicate** of base A2 PR-04 and SF-05. REC should merge them |
| CRQ-MAIL-19 | The app-layer half is answered (AO-M1: no Secure or SameSite). Proxy-added attributes and rotation or revocation remain |
| CRQ-MAIL-20 | Well-formed. No plan company rule exists for internal users |
| CRQ-MAIL-21 | Answered statically: the seed is loaded as a data record without the toggle, and the group data never gives internal users the editor group, so install state matches the restricted seed. Runtime confirmation only (PR-MD9) |

## 4. Findings

### 4.1 A2 observations (not in D1; A1 is not repaired)

- **AO-M1 (cookie defaults).** The framework response-cookie wrapper defaults to Secure off and no SameSite. The guest cookie, and the session cookie, therefore carry no Secure or SameSite attribute at the application layer. Browser defaults and any reverse proxy decide the effective posture.
- **AO-M2 (push registration).** Endpoint registration trusts a caller-supplied endpoint and can reassign an existing endpoint row to the caller. This makes the D04 SSRF path reachable by whoever can call the method.
- **AO-M3 (admin asymmetry).** The Access Rights admin is unrestricted at render time but not exempt at template save time.
- **AO-M4 (link-preview read-back).** HTML titles and Open Graph fields from fetched targets become message data visible to channel readers.
- **AO-M5 (language elevation).** The composer's language rendering uses full superuser elevation on equality, which is broader than the bypass marker used for other fields.

### 4.2 D1 claim-level findings

- **F-M1 (D11 PARTIAL).** The comment-mode body is always editable, and language rendering is elevated to superuser.
- **F-M2 (D03 PARTIAL).** The cap and throttle do not bound failed outbound fetches.
- **F-M3 (G2 closure too strong).** It rests on D13, which was not re-read.
- **F-M4 (K5 PARTIAL).** The comment is ambiguous and has no behavioural effect.
- **F-M5 (D16 PARTIAL).** The owner-company part depends on an unread mixin.

### 4.3 Conflicts with the base A2 mail review (flagged for REC)

| # | D1 position | Base A2 position | Note |
|---|---|---|---|
| CF-1 | K1–K4 "UNCHANGED (still CONFIRMED-FROM-SOURCE)" | K1 refined, K3 wider, K4 PARTIAL | The base A2 outcome governs for REC. D1 should not be read as re-confirming K4 as written |
| CF-2 | C28 refined, keeping "routes accept guest context"; CRQ-09 moved to N1 | C28 PARTIAL: zip has no guest context, and delete works by ownership | Part of N1 is already answered by base A2 |
| CF-3 | C29 extended | C29 PARTIAL (the GIF provider gets search terms) | The extension is valid, but the base claim needs the A2 correction |
| DUP-1 | D14 and CRQ-MAIL-18 | SF-05 and PR-04 | Same finding. Merge them and do not count it twice |
| DUP-2 | G3 closed via D02 | C15 note that guest identity comes from the cookie decorator | Convergent |
| DUP-3 | C18 amended; K5 | C18 VERIFIED (seeded ON, noupdate) | Convergent on the seed. A2 delta adds the D11 inaccuracies |

## 5. Lane B

No Lane B evidence was supplied, and no item fails for its absence.

| Class | Items |
|---|---|
| NOT_APPLICABLE (structural, declaration or documentation) | D02, D07, D09, D10, D15, D16, K5, K6, K7 |
| UNCORROBORATED (user-surface, clear from source) | D12, D13 |
| UNCORROBORATED + MISSING_REQUIRED_RUNTIME_PROOF (network, config, identity or deployment dependent) | D01, D03, D04, D05, D06, D08, D11, D14 (via base PR-04) |

## 6. Proof requirements (new; base A2 PR-01 to PR-13 still apply, and D14 is covered by base PR-04)

| PR | Claim / finding | Case | Expected (source-predicted) | Fail condition |
|---|---|---|---|---|
| PR-MD1 | D01, AO-M1, CRQ-19 | Anonymous visitor joins a public channel so that a guest is created, with no proxy. Capture Set-Cookie. Then delete the guest record and replay the cookie | HttpOnly, expiry about 365 days, no Secure, no SameSite. The replay after deletion yields no guest identity | Secure or SameSite emitted by the app, or the deleted guest's cookie still authenticates |
| PR-MD2 | D03, AO-M4, CRQ-13 | Internal user posts a message linking (a) a loopback HTML listener with a title, and (b) an external URL that redirects to it | The listener receives GETs carrying the link-preview header. The title appears in the stored preview and is broadcast to channel members | No request reaches the listener, or no internal metadata is stored |
| PR-MD3 | D03, F-M2 | Message with 20 links to distinct internal endpoints that return 404 or non-HTML | 20 outbound requests | 6 or fewer requests (the cap applies to failures) |
| PR-MD4 | D04, AO-M2, CRQ-14 | (a) Internal user and (b) portal user call device registration with the server's public VAPID key and an endpoint pointing to an internal listener. Then trigger a push to each | The POST reaches the listener for each role that can call the method, and the roles able to register are recorded | Registration succeeds but no POST is sent, or a POST goes to a `.invalid` host |
| PR-MD5 | D05, D06, CRQ-15 | Point the publisher URL at a local capture service and run the job manually. The service replies with two messages and an enterprise section. Then deactivate the job and run the scheduler | The captured body holds exactly the D05 fields, the messages are posted in the all-employees channel, and six parameters are overwritten. The default URL scheme is recorded as http. After deactivation there is no egress | Extra or missing fields, messages not posted, egress after deactivation |
| PR-MD6 | D08, CRQ-16 | Mass mail with an explicit id list that includes records the user cannot read | Rendering fails with an access error, and no outgoing mail is created for unreadable records | Mail is created with content from unreadable records |
| PR-MD7 | D11, F-M1, CRQ-17 | Non-editor on a template-based composer in comment mode edits the body to include an unsafe expression and sends it. Repeat in mass mail | Comment mode: the body is editable, restricted rendering rejects or leaves the expression literal, and nothing is evaluated. Mass mail: the body cannot be edited | The unsafe expression is evaluated |
| PR-MD8 | D11, AO-M5 | Template whose language expression reads a field of a related record the non-editor cannot read. The non-editor sends with that template unchanged | The language resolves (superuser elevation) and no access error occurs. Record the outcome as a design input | An access error is raised (elevation narrower than the source shows) |
| PR-MD9 | D12, CRQ-21 | Fresh install: list internal users holding the editor group, then set the parameter off and on through settings | Only system admins hold it after install. Off grants it to internal users, and on removes it | Internal users hold the editor group after install, or the toggle has no effect |
| PR-MD10 | D15, CRQ-20 | A user whose only active company is A creates activities directly from a plan of company B, outside the wizard | Allowed, because no record rule blocks it | Refused by a record rule |

Proof requirement count: **10**.

## 7. Limitations

- SOURCE-STATIC at one commit. Runtime reachability, proxy cookie rewriting, network egress controls and Enterprise or other-module overrides were not observed.
- P20–P24, P26, P31–P33 and the Discuss controllers that call link preview and device registration were not re-read. D13 and D16 stay PARTIAL on that basis, and the RPC reachability of the registration method is framework behaviour that was not re-read.
- Whether remote publisher messages are escaped when posted was not traced.
- No percentages, no Formal Coverage, no QIDs answered, no git operations. No vendor code is reproduced.
