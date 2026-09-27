# G01 PLATFORM_BASE — RED TEAM A2 Review — `mail`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional/semantic verifier of A1 conclusions). Independent of A1; A1 package not repaired |
| Group / Module | G01 PLATFORM_BASE / `mail` ("Discuss") |
| Reviewed input | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_MAIL_A1_PACKAGE_20260927.md` — sha256 `dde12053f968e2b55bc906da7175840d119386bb051f6b21a80885e209ff092f` |
| Upstream Lane A | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_MAIL_LANE_A_PASS1_20260927.md` — sha256 `8511f925843c54984cc4fb0edf589c8e3421640e38e996551d236b7958be22e6` (matches the value recorded in the A1 header) |
| Bank (topic lens only) | `GMVQ/G01_PLATFORM_BASE/G01_MAIL_GMVQ_MVQ_50_V1.00_DRAFT.md` — sha256 `0d6d7fcc4d6fef3be30ee281ee7096e8fc1fdb9e94d96ff120d0f5e79a10bf7d` (W1-B01, ELIGIBLE; not edited, no QID answered) |
| Excluded | `G01_LANE_A_PASS2/G01_MAIL_LANE_A_PASS2_20260927.md` exists in the tree but is NOT an input to this A2 cycle and was not opened |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/mail/` (raw fetch + local `git hash-object`; see section 2) |
| Lane B | None supplied |
| Date | 2026-09-27 |
| Disposition | **A2 PASS WITH FINDINGS** |

Disposition rationale: all 30 claims are traceable and none is contradicted outright; there are 26 VERIFIED and 4 PARTIAL. The four A1 contradictions (K1 to K4) stand, but K1 and K4 need refinement (section 5). The findings are refinements, omissions and proof items, not structural defects, so there is no return to A1. The findings and proof requirements go forward to Reconciliation and Proof.

Clean room: this review states behaviour in neutral terms. It does not reproduce vendor code. Identifiers and line numbers are evidence pointers only. There are no percentages and no Formal Coverage claim.

## 1. Test plan (declared before verdicts)

| TP | Test | Applies to | Method | Pass criterion |
|---|---|---|---|---|
| TP1 | Lineage | Whole package | sha256 of the A1 package, the Lane A packet and the bank; compare with the hashes A1 recorded | Hashes match |
| TP2 | Evidence integrity | All (SC) evidence plus any file A2 re-reads | Re-fetch at the anchor commit and run `git hash-object`; compare with the Lane A blob SHA-1 values | Every blob matches |
| TP3 | Independent semantic re-read | Every HIGH claim, every contradiction (K1 to K4) and every CRQ focus item: K1 activity OR rule; K2 token channel routes; K3 company-context emptying; K4 access-param warning; the mail_message.py L1361 comment; 26 rules with no company scope; `/mail/unfollow`; guest-context post/update | Read the cited function or section and check the claim's WHAT, operation by operation | The claim states the behaviour at the right scope (operation, actor, route) with no over- or under-statement |
| TP4 | MED claims | C14, C21, C28, C29 | Targeted re-read of the cited evidence | Same as TP3 |
| TP5 | Business-meaning review | Messaging, activities, followers, attachments, channels in a multi-company SaaS ERP | Ask for each claim whether the RISK wording matches what the rule means for tenants and companies | Risk neither inflated nor missed |
| TP6 | Omission sweep | Files re-read in TP3/TP4 only (no new scope) | Note behaviour that bears on the bank topics but is absent from A1 | Omissions listed, not fixed |
| TP7 | Lane B classification | All claims | No Lane B supplied. Classify as NOT_APPLICABLE or UNCORROBORATED, and flag MISSING_REQUIRED_RUNTIME_PROOF only for claims that are inherently runtime | Never FAIL for missing Lane B |
| TP8 | Proof requirements | Runtime-dependent claims, cross-company message and attachment visibility first | Write falsifiable cases, each with an expected result and a fail condition | Each case traces to a claim or finding |

Verdict scale: VERIFIED (the source supports the claim as stated), PARTIAL (the core is supported but the scope or wording is materially off or incomplete), NOT_VERIFIED (not supported, or could not be checked), OUT_OF_SCOPE.

## 2. Lineage and evidence integrity (TP1, TP2)

- TP1: all three sha256 values were computed and match. The A1 header's Lane A hash equals the computed value.
- TP2: 33 blobs were fetched at the anchor (HTTP 200) and all match the Lane A SHA-1 values. The one exception is `tools/discuss.py`, which is not in the Lane A table; its blob is `692708b5` and it was read only to check the guest-context mechanism. Files re-hashed: `__manifest__.py`, `__init__.py`, `security/ir.model.access.csv`, `security/mail_security.xml`, `data/ir_cron_data.xml`, `data/ir_config_parameter_data.xml`, `data/mail_groups.xml`, `models/{mail_message, mail_thread, mail_followers, mail_activity, mail_activity_type, mail_mail, mail_tracking_value, mail_notification, mail_alias, mail_alias_domain, models, mail_template, mail_render_mixin, ir_attachment, ir_mail_server, res_users, res_partner}.py`, `models/discuss/{discuss_channel, discuss_channel_member}.py`, `controllers/{thread, attachment, mail, google_translate}.py`, `controllers/discuss/{public_page, gif}.py`. No mismatch.
- The copies are kept in the session scratchpad (`.../scratchpad/a2_mail`) and are not committed.

## 3. Claim verdict table

| Claim | Conf. (A1) | A2 verdict | A2 basis (independent re-read) |
|---|---|---|---|
| C01 | HIGH | VERIFIED | Manifest dependency list and purpose match |
| C02 | HIGH | VERIFIED | The partner model inherits the activity and blacklist-thread behaviours; the channel inherits the thread behaviour |
| C03 | HIGH | VERIFIED | Generic model/id link, stored record-company field, employee-only flag, seven message types. See SF-06: the company field is stamped but never used as an access input in this module |
| C04 | HIGH | VERIFIED | Access rows are public read, portal CRUD and internal CRUD; custom `_check_access` and `_search` narrow them |
| C05 | HIGH | **PARTIAL** | Delete maps to document write (confirmed). But the "non-internal users are denied internal-class messages" rule is scoped by operation: on the record-level check for read and create it covers only comment-type messages, while write and delete cover all types. The search path applies the internal-class filter to every type. So the claim flattens two different mechanisms (SF-01) |
| C06 | HIGH | VERIFIED | Default post operation is write, the channel lowers it to read, and the base layer validates the value. Only message creation uses the post operation; message write and delete use document write |
| C07 | HIGH | VERIFIED | Admin-only access rows confirmed for each listed entity; followers, aliases and alias domains are read-only for internal users |
| C08 | HIGH | VERIFIED | Post: resolves the thread with post access, then posts with elevated privilege; no auto-follow without write. Update: author, guest author or admin, with elevated privilege after the check. See SF-03 and SF-04 for omissions |
| C09 | HIGH / LOW | VERIFIED | The model helper warns on unknown params and then checks access with the company context emptied. The effect of an empty context is still base-owned (G9). K4 framing is refined in section 5 |
| C10 | HIGH | VERIFIED | Exactly 26 rule records, none with a company term. No rule exists at all for messages, followers, outgoing mail or aliases, so their isolation is entirely in code or inherited from the parent |
| C11 | HIGH / LOW | VERIFIED | The L1361 unresolved allowed-company comment is confirmed, as is the inbox push with the context emptied (~L3381). A third emptying site in the channel broadcast was missed (SF-02). The read check is evaluated for the *triggering* identity, not for each push recipient (SF-05) |
| C12 | HIGH | VERIFIED | Self-follow needs read; if read fails the call returns quietly instead of raising. Following for others needs write, and the target list is filtered to active partners with elevated privilege. Internal users may unfollow themselves with no rights check, "no matter the current company" per the in-source comment. Uniqueness confirmed |
| C13 | HIGH | VERIFIED | Public, CSRF off, keyed hash over the path plus sorted params using the database secret; no timestamp or expiry. **Addition:** the confirmation page shows the record's display name, read with elevated privilege, to any token holder, including anonymous ones. This part of CRQ-MAIL-04 is answered from source (SF-07) |
| C14 | MED | VERIFIED | The message redirect searches under the caller's access, so "not found" and "no access" give the same outcome. The legacy param resolves with elevated privilege, but both branches fall back identically. The redirect also *extends* the company cookie (SF-08, omission) |
| C15 | HIGH | VERIFIED | Invitation check in constant time; the group restriction overrides the token; token routes are gated by a parameter. The parameter is **not seeded**, so the routes are off by default. See SF-09: the token is caller-chosen, shares the namespace of existing channel invitation secrets, and a GET request creates records |
| C16 | HIGH | **PARTIAL** | K1's OR structure is confirmed. Correction: when the rule fails, write and delete fall back to **document write**, not post access. Post access only affects creation. A1's risk wording ("any document they can post to") overstates it for models whose post operation is lower than write. For free-floating activities, read is assignee-only but write/delete also let the creator through the rule (SF-10) |
| C17 | HIGH | VERIFIED | Field-level read filter; tracking entries with no field are visible only to system admins |
| C18 | HIGH | VERIFIED | Editor-group guard on unsafe expressions at save, restricted rendering seeded ON (noupdate). The template rule restricts create, write and delete only; read is not restricted |
| C19 | HIGH | VERIFIED | Thread rule confirmed. The channel override drops the tracking-value condition and keeps comment-only. The admin edit path (C08) means sent comments can be edited by someone other than the author |
| C20 | HIGH | VERIFIED | Five states, no copy, retry only from failed, cancel. Auto-delete runs after success or after an invalid/missing address failure; other failures keep the mail (precision note) |
| C21 | MED | VERIFIED | The queue job runs as the root user with batch 1000 and propagates failures to notifications. The failure path then triggers the L1361 status push under the job identity (SF-05) |
| C22 | HIGH | VERIFIED | Seven statuses (internal key "pending" is labelled Sent, "sent" is labelled Delivered), partial unique on message+partner, two check constraints |
| C23 | HIGH | VERIFIED | Pipeline order and loop parameters (defaults 120 min / 20) confirmed. The contact policy **defaults to everyone** (SF-11, omission). The author is matched to a partner by email |
| C24 | HIGH | VERIFIED | Behaviour confirmed. Omitted: a cap of 10,000 deletions per run, and a global search with no company filter (answers part of CRQ-MAIL-10 from source) |
| C25 | HIGH | VERIFIED | Eight jobs, intervals as stated, fetch job inactive |
| C26 | HIGH | VERIFIED | Alias unique per (name, domain or none); bounce and catchall uniqueness; the post-init hook migrates the global params |
| C27 | HIGH | VERIFIED | Rule and constraints confirmed. Business meaning: open channels with no group restriction are visible to **every** internal, portal and public user with no company term, and post access is read (SF-12) |
| C28 | MED | **PARTIAL** | Upload uses the post-access thread check; delete uses ownership (write or scoped token), not thread access; the PDF preview and thumbnail routes are extra public routes. **Wrong detail:** the zip route does *not* attach guest context and has no module-level access check; it depends on base binary streaming. The upload company can come from the client cookie when the thread has no company (SF-13) |
| C29 | MED | **PARTIAL** | Translation sends the message body to the external API, and the result is cached with elevated privilege and shared per language. The GIF provider receives **search terms**, not message content, so "message content can go to ... a GIF provider" overstates it. Web push and personal SMTP are confirmed |
| C30 | HIGH | VERIFIED | The notification-type constraint, the inbox group and per-owner server uniqueness are confirmed. Cleanup is an autovacuum routine, not a dedicated job record (wording only) |

Counts: VERIFIED 26, PARTIAL 4 (C05, C16, C28, C29), NOT_VERIFIED 0, OUT_OF_SCOPE 0.

## 4. Semantic findings (business meaning, multi-company SaaS lens)

- **SF-01 Internal-note leakage is split across two mechanisms (C05, BR2).** Listing and search hide every non-public-class message from portal and public users. The per-record check for read and create hides only *comment-type* internal-class messages. A non-comment message (system notification, email, auto-comment) with no subtype or an internal flag, on a document the portal user can read, is therefore excluded from search but not from a direct by-id read at the record-check layer. BR2 ("never see internal-class messages") is too strong until proven. See PR-09.
- **SF-02 Company-context emptying is wider than K3 states.** There are three emptying sites: the thread-access helper, the inbox push, and the channel header broadcast. The post controller also empties the context when it decides whether an internal poster may set the message type and subtype. A1 names the first two.
- **SF-03 The public post route merges a client-supplied context into the request before the elevated post (C08).** A1 does not mention this. Non-internal posters, and posters without create-mode access, are forced to comment type and subtype, so internal notes cannot be posted that way. The authoring fields are removed for non-internal creators. Which other context keys influence the elevated post is unverified. See PR-10.
- **SF-04 Recipient eligibility at post time.** Internal users can address any partner they can read. Share users need a scoped mention token for each partner. Internal users can also address all users of a role, resolved with elevated privilege. This matters for cross-company addressing and is not in A1.
- **SF-05 The notification-status push (L1361) checks the wrong identity for part of its audience.** The parent-record read check runs as the identity that triggered the status change. The payload, which includes the thread display name, goes to that identity *and* to the message author. When the trigger is the root-user queue job (C21), the check is made under the job identity. Author-side cross-company exposure is therefore not covered by the check. This sharpens CRQ-MAIL-01. See PR-04.
- **SF-06 The record company on a message is informational only in this module.** It is stamped at post time (from the record's company, falling back to the environment company) but used by no rule or access function in the files read. Company isolation of messages rests entirely on access to the parent record plus the author, recipient and notified exceptions. A notified or recipient user reads the message whatever the record's company (see PR-01b).
- **SF-07 The unsubscribe page reveals the record name (C13).** A valid token lets an unauthenticated holder see the record's display name. There is no expiry and no binding to the current partner email, so a forwarded or leaked email gives lasting record-name disclosure and an unsubscribe capability for that partner.
- **SF-08 The redirect widens the active-company set (C14).** For a logged-in user, the view redirect retries the read check with the cookie companies plus a suggested company. On success it writes the widened set back to the company cookie. Base decides whether cookie company ids are validated against the user's companies (see PR-12). The bank's "reply/action lands in the wrong company" topic applies here.
- **SF-09 Token channel semantics (K2, C15).** The creation token is chosen by the caller and doubles as the channel's invitation secret. A token that matches an existing channel's secret joins that channel, whatever its type, subject to the group restriction. Records are created on GET and there is no module-level rate limit. A new channel has no group restriction, so it is readable by every user under the C27 rule once someone knows its id.
- **SF-10 Activity authority (K1, C16).** Anyone with write on the parent document can edit, reschedule or delete another user's activity. The activity itself holds no audit record for this in the files read. A reader or poster without write cannot. For free-floating activities, the creator who is not the assignee can write or delete but not read.
- **SF-11 Inbound default is open (C23).** New aliases accept mail from everyone by default. Sender-to-partner matching is by email address alone, so spoofing resistance depends on the policy an admin picks and on transport checks outside this module.
- **SF-12 Channels are cross-company by construction (C27).** There is no company term on channels or members. Open channels are tenant-wide spaces across all companies in a database. For an SMEsPlus multi-company tenant this is a design decision, not a defect, but A1 does not name it.
- **SF-13 Attachment company attribution (C28).** Uploads to a thread with no company take their company from the request's company cookie, preferring the user's main company when it appears in that cookie. Attachment deletion needs ownership (write on the attachment, or a scoped token), not thread access. A guest who uploaded holds a token and can delete their own uploads.
- **SF-14 Activity systray (omission; bank topic "count changes attributable to protected activity").** A user's assigned activities on records they cannot read, even across all their companies, still count and are listed under a generic activities bucket instead of being hidden (`res_users.py` ~L457).

## 5. Contradiction re-verification (K1 to K4)

| K | A1 status | A2 result |
|---|---|---|
| K1 | CONFIRMED-FROM-SOURCE | **CONFIRMED, REFINED.** The rule-OR-document logic holds for write and delete, but the document operation is *write*, not "post/write" (C16 PARTIAL). The docstring mentions the post operation, but the executed path maps activity write/delete to document write. Lane A item 29's reading ("rule restricts") is still wrong |
| K2 | CONFIRMED | **CONFIRMED.** Four route patterns (chat and meet, each with and without a name), parameter-gated, parameter not seeded. Plus SF-09 |
| K3 | CONFIRMED | **CONFIRMED, and wider** (SF-02) |
| K4 | CONFIRMED | **PARTIAL.** At the model-helper level the warning-only behaviour is confirmed (and the same pattern exists in the message-level getter, which A1 does not mention). But every controller entry point read (`thread.py`, `attachment.py`) **filters** keyword params to the allowlist *before* calling the helper. In the base helper, the params grant nothing. Lane A item 35 is therefore correct for the HTTP surface and wrong only for direct model callers. The residual risk is limited to overrides in other modules that consume those params |

Also re-verified: the L1361 unresolved company comment (present, verbatim intent: "if necessary"); 26 rules with no company term (confirmed); `/mail/unfollow` CSRF off with a signed token (confirmed, plus SF-07); guest-context post and update (confirmed; guest identity comes from a cookie token via the module's decorator, which partly addresses G3 for these routes).

## 6. Omissions (A1 not repaired; for Reconciliation)

- O1: Client context merged on the post route (SF-03).
- O2: Mention-token and role-based recipient resolution on post (SF-04).
- O3: Third company-emptying site in the channel broadcast (SF-02).
- O4: Identity mismatch in the status push; author is a recipient (SF-05).
- O5: Record company on messages is unused for access (SF-06).
- O6: Record-name disclosure on the unsubscribe page (SF-07).
- O7: Company cookie widening on redirect (SF-08); cookie-derived attachment company (SF-13).
- O8: Default alias policy is "everyone" (SF-11).
- O9: Activity cleanup capped at 10,000 per run, with a global search and no company filter (C24).
- O10: Activity systray shows unreadable-record activities (SF-14).
- O11: Additional public attachment routes (PDF first page, thumbnail update) are missing from the Lane A route list; this adds to G11.
- O12: The search-versus-record-check difference for the internal-class filter (SF-01).
- O13: Translation cache is shared across users per language (C29).

## 7. Lane B classification

No Lane B evidence was supplied, and none is required for A2 to pass. There is no FAIL on Lane B grounds.

| Class | Claims |
|---|---|
| NOT_APPLICABLE (static structure or declaration, not observable on a user surface) | C01, C02, C03, C04, C07, C10, C17, C22, C25, C26, C30 |
| UNCORROBORATED (user-observable, no Lane B, source-only) | C06, C12, C14, C18, C19, C20, C23, C27, C29 |
| UNCORROBORATED + MISSING_REQUIRED_RUNTIME_PROOF (inherently runtime: effect depends on base semantics, configuration, identity or execution path) | C05, C08, C09, C11, C13, C15, C16, C21, C24, C28 |

## 8. Proof requirements (falsifiable; cross-company message and attachment visibility first)

Setup common to PR-01 to PR-05 and PR-12: a single database with companies A and B, where record Rb (a thread-enabled model with a company field) belongs to B. User Ua has companies {A} only. User Uab has companies {A,B} with only A active. Portal user P has read access on Rb through the standard sharing path.

| PR | Claim / finding | Case | Expected (source-predicted) | Fail condition |
|---|---|---|---|---|
| PR-01a | C10, SF-06 | Ua (not follower, not recipient) tries to read a comment on Rb via list/search, direct by-id read, the thread message fetch route, `/mail/message/<id>` and the translation route | Every path denies or returns nothing; the redirect gives the same result as for a non-existent id | Any path returns the body, subject, author or attachment names of the message |
| PR-01b | SF-06, BR1 | Ua is made an explicit recipient of a message on Rb | The message body is readable by Ua through the recipient exception, whatever the company | Not readable (claim BR1 wrong). Either outcome must be recorded as a design input for SMEsPlus |
| PR-02 | C09, G9, CRQ-02 | Uab (active A) and Ua each post to Rb via the public post route and upload an attachment via the upload route | Record the outcome for Uab. For Ua: denied (not found) | Ua succeeds in posting or uploading to Rb |
| PR-03 | C28, SF-13 | Ua calls the zip, PDF-first-page and delete routes for an attachment on Rb, and uploads to a company-less thread with a forged company cookie naming B | Zip and preview return no bytes of the Rb attachment; delete refused; forged upload not stamped with company B | Any bytes returned, deletion succeeds, or the attachment is stamped with a company outside Ua's set |
| PR-04 | C11, SF-05, L1361 | Uab authors an email-notified message on Rb; Uab is then removed from B; a delivery failure is forced through the queue job | No status push to Uab carries Rb's display name | The push payload to Uab contains Rb's display name or message data |
| PR-05 | C11 (~L3381) | Follower Ua (inbox preference) is notified of a message on Rb | Inbox payload limited to the message and notification data Ua is entitled to under BR1 | Payload includes fields of Rb that Ua cannot read under the ORM |
| PR-06 | C16, K1, SF-10, CRQ-03 | U2, with write on document D but neither creator nor assignee, edits and deletes U1's activity; U3, with read-only on D, tries the same | U2 succeeds; U3 refused. Record whether any audit record of U2's change exists | U2 refused, or U3 succeeds |
| PR-07 | C13, SF-07, CRQ-04 | Replay a captured unsubscribe link while logged out, after the partner loses read on the record, and with the partner id changed | Original link succeeds and shows the record name; tampered link raises an access error | Original link rejected (expiry exists), or tampered link succeeds |
| PR-08 | C15, SF-09, CRQ-05 | Token routes with the parameter off; with it on, an anonymous GET on new tokens and on an existing group-restricted channel's secret | Off: not found. On: each new token creates one channel plus a guest; a group-restricted channel is refused | Creation while off, or joining a group-restricted channel without the group |
| PR-09 | C05, SF-01 | P reads, by id, a non-comment message with no subtype on a document P can read, then searches for it | Search excludes it; outcome of the by-id read recorded | Search returns it; or the by-id read returns the body while BR2 is asserted as absolute |
| PR-10 | C08, SF-03 | P and a guest post via the public route with extra context keys and an internal-note subtype | Message stored as a comment with the public comment subtype; author forced to the caller | Internal-class message created, or author or subscription altered by client context |
| PR-11 | C24, CRQ-10 | Overdue activities older than 3 years seeded in both companies, and more than 10,000 in total | One run deletes up to 10,000 across both companies; no per-company control | Company-scoped deletion, or more than 10,000 deleted in one run |
| PR-12 | SF-08 | Uab opens a view link to Rb while active in A; Ua opens it with a forged cookie naming B | Uab: redirected and cookie widened to include B. Ua: fallback, no access | Ua reaches Rb, or the forged cookie is persisted as allowed |
| PR-13 | SF-14 | Ua is assigned an activity on Rb | Systray counts it under a generic bucket without Rb's name | Rb's name or fields are exposed through the systray |

Proof requirement count: 14 (PR-01a and PR-01b counted separately).

## 9. Limitations

- A2 is SOURCE-STATIC like A1. Re-reading source shows behaviour in code, not whether it can be reached at runtime or how it behaves under a given configuration. Base-layer semantics of an empty or cookie-supplied company context were not traced (G9 stays open).
- Scope was limited to the A1 evidence set, plus `tools/discuss.py` to check guest context. Wizards, `mail_thread.py` outside the re-read sections, Enterprise overrides and overrides from other modules were not studied. PASS-2 of Lane A was not consulted.
- Line references are approximate and valid only at the anchor commit.
- No percentages, no Formal Coverage claim, no git operations on the repository, and no vendor code reproduced.
