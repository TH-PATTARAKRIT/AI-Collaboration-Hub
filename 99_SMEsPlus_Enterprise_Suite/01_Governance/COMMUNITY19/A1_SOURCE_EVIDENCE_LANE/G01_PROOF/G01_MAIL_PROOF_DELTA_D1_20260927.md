# G01 PLATFORM_BASE — RED TEAM Proof DELTA D1 — `mail`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | RED TEAM **PROOF — DELTA cycle D1**. Stage 2 of a two-stage REC + PROOF delta run |
| Group / Module | G01 PLATFORM_BASE / `mail` ("Discuss") |
| Date | 2026-09-27 |
| Nature | Addendum. The base PROOF `G01_MAIL_PROOF_20260927.md` has **not** been edited. Base cases PC-MAIL-01..41 and their results stand. This file adds PC-MAIL-D-01..23 |
| Upstream REC DELTA | `G01_RECONCILIATION/G01_MAIL_REC_DELTA_D1_20260927.md`, sha256 `bb5de020246be21a802880bfa3d0b411a6c430c84237cf57ae6e14bc59b8812f`. 50 counted rows: MATCH 19, CONTRADICTION 9, UPP 18, GAP 4. One more row (D14) is a merged duplicate |
| Parent artifacts (sha256 at intake 2026-09-27T15:16:23Z) | A1 D1 `e3febb2e0fc0b50fd14b69c362798d673517d3e9eb1696980b18b380075f8c7f`; A2 D1 `8e6f5dc847e4ad52960098aa34fc15678c01d718f9e21d8afe00c313eeccdf9e`; Lane A PASS-2 `b2cdaa0cf60f6554828d7fcabd97ebb2ebd3735df090d9fb446f3bef8a6ea21b`; base REC `d5c8ea38e8436a431f3183754b38f312d99b3f613fb8716084ea367d9a6bada4`; base PROOF `2f83f7cfab848c3b7a41b8c54802de8ebd57dabfaaa902b01078d86989441273`; base A2 `e587bf12e221a2d8be6e32f056ee37d1c4b88dbc8495a87a7b6e0d80287d56e8`; bank `0d6d7fcc4d6fef3be30ee281ee7096e8fc1fdb9e94d96ff120d0f5e79a10bf7d` (= FREEZE_W1-B01; freeze `558ec88047aef5c8e7ea0e2675b1c43ef358ec29b172d6878068330f3fba7177`) |
| Predeclaration | Cases were written to the scratchpad at **2026-09-27T15:17:31Z**, before any source fetch (the first fetch began after that time and the last completed at 15:18:05Z). File: `scratchpad/rec_mail_d1/PC_MAIL_D_CASES_PREDECLARED.md`, frozen read-only copy `…frozen.md`, both sha256 `d65394799e9b1e307beb35505b37c58bc1f0a2df404eb4b06d5641a47087fe66`. Reproduced in Appendix A (content verbatim; only heading levels were demoted) |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`. Each blob was verified with `git hash-object` (section 2). Copies are in `scratchpad/rec_mail_d1/src/`, with per-file sha256 in `src_sha256.txt` (`d343db0f…a9f9`). Fetch log `fetch_log.txt` (`7026a5b3…1127`). Execution log `exec_results.txt` (`6ac2cb53…cb80`) |
| External endpoints | Only the raw source host above was contacted. The publisher-warranty URL, link-preview targets, push endpoints, the GIF provider and the translation API were **not** contacted |
| Runtime device | **OFFLINE** per the controller brief. It was not probed in this cycle, and no runtime case was run, simulated or inferred |
| **Disposition** | **PROOF DELTA PARTIAL — SOURCE/CONFIG EXECUTED (13 PASS, 0 FAIL), RUNTIME NOT-EXECUTED (10)** |

Clean-room note: results are neutral paraphrases of observed source behaviour. Identifiers and ~L pointers are evidence pointers only. No vendor code is reproduced, and nothing recommends reusing vendor schema, ORM, workflow, UI or naming. No percentages. No Formal Coverage claim. No git operations. No existing file was edited.

## 1. Case design

- The 10 A2 D1 proof requirements PR-MD1..10 map **one to one** to runtime cases PC-MAIL-D-01..10. Setup, expected result and fail condition come from A2 D1 section 6.
- The static basis for each PR, for each delta CONTRADICTION (including the 3 conflict resolutions) and for the two R-a items (D13, D16) is covered by SOURCE / CONFIG cases **PC-MAIL-D-11..23**. These were predeclared and then executed.
- D14 / CRQ-MAIL-18 is a duplicate of base PR-04 (DUP-1). **No new case was created**; base PC-MAIL-05 (runtime) and base PC-18 and PC-36 (static, PASS) cover it.
- A static PASS confirms only that the source reads as the prediction assumes. **It is never counted as a result for the linked runtime case.**

## 2. Blob verification (executed)

All 35 files returned HTTP 200. The expected value is the full blob from the Lane A PASS-2 or PASS-1 tables where one exists, otherwise the A2 D1 8-hex prefix (`odoo/http.py`, `mail_push_device.py`).

| # | File | Expected | Computed `git hash-object` | Result |
|---|---|---|---|---|
| 1 | addons/mail/models/discuss/mail_guest.py | 9c7c2192… | 9c7c2192c6d5da4f8b334c967a094c381b6c2786 | MATCH |
| 2 | odoo/http.py | ebfc2ac8 (A2) | ebfc2ac8d268a45aaf4b8cde8c9ce8b480d58dbb | MATCH |
| 3 | addons/mail/tools/link_preview.py | 18515419… | 18515419263f8fc005029601a5c7bc821cc9f727 | MATCH |
| 4 | addons/mail/models/mail_link_preview.py | 153d3026… | 153d3026c1f392519078fa17a6e47a1c2b075689 | MATCH |
| 5 | addons/mail/tools/web_push.py | e660da83… | e660da83af7f5b0282b10b64367c0bfb8559da97 | MATCH |
| 6 | addons/mail/models/mail_push_device.py | 5a5a521b (A2) | 5a5a521ba25f1550e15c5fa235595e06bbf5ec92 | MATCH |
| 7 | addons/mail/security/ir.model.access.csv | 29275551… | 29275551e7ca156899fa03985765fb2828de0b06 | MATCH |
| 8 | addons/mail/models/update.py | 05603784… | 05603784124c160005a75d3c77afee94c72d2f62 | MATCH |
| 9 | addons/mail/data/ir_cron_data.xml | d72aacbe… | d72aacbe8f9e17e84d4dd62dfc3642a1ba4dc9fd | MATCH |
| 10 | odoo/tools/config.py | 433ff84b… | 433ff84b625a69e08cce9f42911aa608d3e615ee | MATCH |
| 11 | addons/mail/models/__init__.py | 553bd767… | 553bd76763256a3cdd19b1863da6d8983eef76f8 | MATCH |
| 12 | addons/mail/wizard/mail_compose_message.py | 32fdf959… | 32fdf95981c9ea92af0d506711414decb32d2cd1 | MATCH |
| 13 | addons/mail/models/mail_composer_mixin.py | 57f7a65a… | 57f7a65ac0654fa88fadea44c1c63a9847919bc2 | MATCH |
| 14 | addons/mail/models/ir_config_parameter.py | edbfc4f5… | edbfc4f5c22d7414416c4dd839f425405db4f850 | MATCH |
| 15 | addons/mail/data/ir_config_parameter_data.xml | 1f556c60… | 1f556c605ddc3dbd13dbf68554cabec78dc47906 | MATCH |
| 16 | addons/mail/data/mail_groups.xml | 4b4125ed… | 4b4125ed11ba10696bb321cf40f7573ec4387ec8 | MATCH |
| 17 | addons/mail/models/mail_activity_plan.py | aefe528e… | aefe528e2d1517e2145abe568cd543445b42a1ac | MATCH |
| 18 | addons/mail/models/mail_activity_plan_template.py | 55106089… | 5510608988e2a99942d7d24aeeb83ff17c8086c3 | MATCH |
| 19 | addons/mail/models/mail_activity.py | 66d9cd79… | 66d9cd7994a49fc01d62d4992b64501cc26bfc48 | MATCH |
| 20 | addons/mail/models/mail_template.py | f95b8f53… | f95b8f53dd95166603eadd42013907b77a23870f | MATCH |
| 21 | addons/mail/security/mail_security.xml | 0219605e… | 0219605e445b1f0f545e78f15aa6bca9084a0b5b | MATCH |
| 22 | addons/mail/wizard/mail_template_reset.py | 33036193… | 33036193b1dec7d16c21712c2a462d5864513577 | MATCH |
| 23 | addons/mail/wizard/mail_followers_edit.py | aa7e46ba… | aa7e46bade32f1f16f31ef1f0804db4659edb7e8 | MATCH |
| 24 | addons/mail/wizard/mail_activity_schedule.py | 0e67cb0e… | 0e67cb0efe1b4903c7118d568b47d41de66f6220 | MATCH |
| 25 | addons/mail/wizard/mail_blacklist_remove.py | f4347d54… | f4347d54b9d9a7aebe79cd2693962b85bbb1bef0 | MATCH |
| 26 | addons/mail/wizard/base_partner_merge_automatic_wizard.py | 3a99a177… | 3a99a177281a2787e2a9786447f993c769f3bd75 | MATCH |
| 27 | addons/mail/wizard/mail_template_preview.py | 23b0e077… | 23b0e07760dc59d393dc165ef8513080c290f013 | MATCH |
| 28 | addons/mail/models/mail_alias_mixin.py | 88cecd64… | 88cecd644378ce58ad57a5b2c199eeffa9eefc58 | MATCH |
| 29 | addons/mail/models/mail_alias.py | 3d5c8fb2… | 3d5c8fb2b32e82bc9a20f6cde25f036675d02989 | MATCH |
| 30 | addons/mail/controllers/attachment.py | 70db479c… | 70db479c69e1ed277b56e2199b9c77d6ff63dc97 | MATCH |
| 31 | addons/mail/controllers/discuss/gif.py | f5eba191… | f5eba191836f3ebc7ffd8177e13c41e489d3f31b | MATCH |
| 32 | addons/mail/models/models.py | 1edb1f78… | 1edb1f78d952f754d364ac7d6e7863f7ef58bbf5 | MATCH |
| 33 | addons/mail/models/mail_thread.py | c1f8a83b… | c1f8a83bbd4d6667c1ee7cd38b78cef71ad8f374 | MATCH |
| 34 | addons/mail/controllers/thread.py | 57ab2401… | 57ab2401542aff66eb0cf4b4329bcf92cbda0912 | MATCH |
| 35 | addons/mail/models/discuss/discuss_channel.py | 57e38f34… | 57e38f3446071bd42ef4b80583a4b16f31c97423 | MATCH |

That is 35 of 35 matching, with no mismatch and no BLOCKED case.

## 3. Static cases — executed (SOURCE / CONFIG)

| PC | Links (REC DELTA row) | Layer | Actual observation (neutral; approximate line pointers) | Result |
|---|---|---|---|---|
| PC-MAIL-D-11 | PR-MD1; D01 (D1-24), D02 (D1-25), N1 (D1-43) | SOURCE | The guest cookie setter (guest L135-147) passes HttpOnly and an expiry 365 days ahead, with no Secure or SameSite argument. Both framework cookie wrappers (http L1597, L1784) default to Secure off and SameSite unset. The guest secret is a random UUID, restricted to the system group, read-only and not copied (L29). The model has no method that rotates or revokes it. Token check: sudo load, then constant-time compare (L50-60) | PASS |
| PC-MAIL-D-12 | PR-MD2, PR-MD3; D03 (D1-26), N6 (D1-48) | SOURCE | The fetch (tool L24-33) is a GET with redirects, 3 s timeout, streamed, a browser-like user agent **and** a link-preview identifying header. There is no private, loopback or address filter in the tool or model. The per-message cap (model L73-79) counts previews already linked, found or **successfully** fetched, and breaks above 5. Failed fetches are not counted. The throttle (L110-119) counts stored preview rows for the domain created in the last 10 s, against a parameter defaulting to 99. HTML og:title (falling back to the `<title>` tag), description, type, site name, image and MIME type are stored (tool L87-104; model fields L24-29) and sent on the message bus channel (L101-104) | PASS |
| PC-MAIL-D-13 | PR-MD4; D04 (D1-27), G14 (D1-51), N6 | SOURCE+CONFIG | Send (web_push L143-179): only hosts ending `.invalid` are refused, the token lives 12 h, POST timeout 5 s. Registration (push_device L47-73) is a public `@api.model` method. It checks only that the supplied VAPID public key equals the stored one. The endpoint has no scheme or host validation. An existing row found by the caller-supplied `previousEndpoint` (or the endpoint itself) is rewritten to the caller's partner on a sudo recordset; otherwise a row is created under sudo. The device ACL is system-group only (csv L68) | PASS |
| PC-MAIL-D-14 | PR-MD5; D05 (D1-28), D06 (D1-29), K7 (D1-42), G4 (D1-03), C25 (D1-12) | SOURCE+CONFIG | Payload (update L45-61): db uuid, db name, db create date, version, language, base URL, installed application names, enterprise code, and 4 user counts (active; active with login in the last 15 days; share; active share), with no company filter. When the running user's partner has a company, that company's name, email and phone are added. Transport: POST form field, 30 s (L74). Response parsed as a literal (L76). Each message is posted as a comment on the all-employees channel, obtained from a sudo environment, addressed to the root partner, with errors swallowed (L95-101). Six `database.*` parameters are set under sudo (L104-110). Cron (cron L15-25): root user, weekly, priority 1000, first run +7 days, code passes a null mode, inside `noupdate="1"` (L3). The default cron-list action hides it (L27-29). Config (config L215): file-only option, default `http://` vendor URL. Model imported by the roster (`__init__` L70) | PASS |
| PC-MAIL-D-15 | PR-MD6; D08 (D1-31), CRQ-07 (D1-19), N2 (D1-44), G12 (D1-49) | SOURCE | Targets (compose L790-796): the stored domain is searched in the caller's environment, else the explicit id list is evaluated. Mass mail (L839-853): the docstring states access is checked implicitly while values are prepared. There is no explicit per-record access call. Outgoing mails are created under sudo per batch, then notifications are created. Batch size is the parameter, else the class attribute 50, else 50 (L45, L846-849). The exclusion list defaults on (L204). The responsible-user field (L136-138) is declared and referenced nowhere else in the file (1 occurrence) | PASS |
| PC-MAIL-D-16 | PR-MD7, PR-MD8; D11 (D1-34), CRQ-11 (D1-21), N3 (D1-45), C18 (D1-11), G2 (D1-01) | SOURCE | Field rendering (mixin L141-207): for non-editors with a template, the bypass marker is used only when the value equals the template value. For the body, the template body is forced back when the user cannot edit the body or it still equals the template. Language rendering (L114-139): on equality for non-editors the record is switched to **`sudo()` (superuser mode)**, not to the bypass marker. Body equality (L64-87) compares the body with the raw template value and with a sanitised variant. The mixin rule (L106-112) is "editor or no template". The wizard override (compose L682-688) sets the body **editable for every non-mass-mail composer**, and only mass mail falls back to the mixin rule. D1's sentence "non-editors can edit the body only when no template is set" does not hold in comment mode. A2 is supported | PASS |
| PC-MAIL-D-17 | PR-MD9; D12 (D1-35), K5 (D1-40), K6 (D1-41), G13 (D1-50), C24 (D1-15) | SOURCE+CONFIG | Toggle (icp L87-103): only inside the set-param routine. A falsy value applies the editor group to internal users; a truthy value removes it. Record create and write (L113-127) sanitise only and **do not toggle**. Seed (data L3-11, noupdate): gc years 3, restrict rendering 1, both loaded as data records. Groups (L15-21): the editor group has no implied members except through the system group. Catalogue comments: gc "0 (skipped) by default" (L54-55); restrict rendering "ICP used … to add or remove [editor group] to internal users … Not activated by default" (L61-64) | PASS |
| PC-MAIL-D-18 | PR-MD10; D15 (D1-38), C10 (D1-08) | SOURCE+CONFIG | The plan company defaults to the current company (plan L20-21). The plan-line company is related to the plan (template L20). The plan-line responsible user has a company-check attribute (L52). Neither file sets a model-level automatic company check. The activity model has no company field. The template model has no company field, and its warning about cross-company partner merging is at L419-422. Plan rules (security L251-262) are 1=1 for the system group only. Internal users are read-only on plans and plan lines (csv L44-47). Filtering happens only in the scheduling wizard (schedule L446 "no company or wizard company"; L120-122 mixed-company refusal) | PASS |
| PC-MAIL-D-19 | D13 (D1-36, rule R-a); G2 (D1-01) | SOURCE+CONFIG | Follower edit calls document unsubscribe and subscribe (L36, L44), so the thread rules apply. Preview: the model list is filled under sudo (L24-25), and rendering calls the template's generation in the current user's environment (L66-88). Reset ACL is editor group only (csv L61). Blacklist removal ACL is system only (csv L56). Partner merge posts a chatter message listing merged partners' names, emails and ids (merge L9-15). Schedule wizard: for upload-type activities it checks, as the assignee, the create-operation access on the documents (L455-469). Every D13 sub-statement holds | PASS |
| PC-MAIL-D-20 | D16 (D1-39, rule R-a) | SOURCE | The alias mixin creates the alias under sudo with the owning record's company (mixin L48-51). The alias default domain is the current company's (alias L45). Multi-company checks (L100-175) refuse a company-bound domain that does not match the owner or target document company | PASS |
| PC-MAIL-D-21 | CF-2: C28 (D1-13), CRQ-09 (D1-20), N1 (D1-43) | SOURCE | Upload (L49-50): public, guest decorator. Delete (L98-108): public, guest decorator. It requires attachment ownership (write or a scoped token), then deletes under sudo. Zip (L110-118): public, **no** guest decorator and no module-level access check; it browses the ids in the request environment. PDF-first-page (L120-127): guest decorator | PASS |
| PC-MAIL-D-22 | CF-3: C29 (D1-14) | SOURCE | GIF search sends the search term, locale, country and paging, plus the API key and **the database name as client key** (L32-46). The categories and posts calls send the same key and client key with GIF ids (L57-86). No message content is sent | PASS |
| PC-MAIL-D-23 | CF-1: K1–K4 (D1-23) | SOURCE | Mapping (models L65-83): read→read, create→post access, write/unlink→**write**. Thread helper (thread L5130-5141): disallowed kwargs only log a warning, and access is checked with the allowed-company context emptied. Controllers (thread controller L18-56) pass only allowlisted kwargs. Emptying sites: thread L3381 (inbox push) and L5138 (helper), channel L1120 (broadcast), controller L158 (type/subtype decision). That is 4 sites | PASS |

### 3.1 Refinements observed during execution (not new claims; no credit taken; for A3)

- **RD1 (PC-D-12)**: new preview rows are created only after the per-message loop ends. The per-domain throttle therefore cannot count the current message's own fetches either, so a single message's outbound requests to one domain are not bounded by the throttle.
- **RD2 (PC-D-13)**: reassignment of a device row is keyed on a caller-supplied `previousEndpoint`. The companion unregister method deletes any device row matching a supplied endpoint under sudo, with no ownership check (push_device L75-84).
- **RD3 (PC-D-14)**: in the scheduled run the "calling user" is the root user, so the optional company name, email and phone come from the root user's partner company. Whether remote message bodies are escaped when posted was not traced.
- **RD4 (PC-D-17)**: the group toggle fires only through the set-param routine. Creating or writing the parameter record directly (data load, or editing the parameter record) changes the value without changing group membership, so the parameter value and the group state can diverge. This bears on K5, G13 and CRQ-21, and PC-D-09 should record it.
- **RD5 (PC-D-11)**: the framework cookie wrapper also sets max-age 0 when the cookie category is not consented. The guest cookie uses the default "required" category.
- **RD6 (PC-D-16)**: A2's "full superuser record" for language rendering is, at source level, superuser *mode* on the same user (`sudo()`), which bypasses access rights and record rules.

## 4. Runtime cases — NOT-EXECUTED (device OFFLINE; ready to run)

Common setup RT-D is in Appendix A. The capture listener runs on loopback inside the disposable test host. The real publisher URL and all third-party endpoints stay uncontacted.

| PC | PR | REC DELTA link | Static basis (PASS) | Status |
|---|---|---|---|---|
| PC-MAIL-D-01 | PR-MD1 | D1-24, D1-10, D1-43 | PC-D-11 | NOT-EXECUTED |
| PC-MAIL-D-02 | PR-MD2 | D1-26, D1-48 | PC-D-12 | NOT-EXECUTED |
| PC-MAIL-D-03 | PR-MD3 | D1-26 | PC-D-12 (+RD1) | NOT-EXECUTED |
| PC-MAIL-D-04 | PR-MD4 | D1-27, D1-48, D1-51 | PC-D-13 (+RD2) | NOT-EXECUTED |
| PC-MAIL-D-05 | PR-MD5 | D1-28, D1-29 | PC-D-14 (+RD3) | NOT-EXECUTED |
| PC-MAIL-D-06 | PR-MD6 | D1-31, D1-19, D1-44 | PC-D-15 | NOT-EXECUTED |
| PC-MAIL-D-07 | PR-MD7 | D1-34, D1-21, D1-45 | PC-D-16 | NOT-EXECUTED |
| PC-MAIL-D-08 | PR-MD8 | D1-34 | PC-D-16 (+RD6) | NOT-EXECUTED |
| PC-MAIL-D-09 | PR-MD9 | D1-35, D1-40, D1-50 | PC-D-17 (+RD4) | NOT-EXECUTED |
| PC-MAIL-D-10 | PR-MD10 | D1-38 | PC-D-18 | NOT-EXECUTED |

No runtime result is recorded or implied.

## 5. Summary of results

| Layer | Cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| SOURCE | 8 (PC-D-11, 12, 15, 16, 20, 21, 22, 23) | 8 | 0 | 0 |
| SOURCE+CONFIG | 5 (PC-D-13, 14, 17, 18, 19) | 5 | 0 | 0 |
| RUNTIME | 10 (PC-D-01..10) | 0 | 0 | 10 |
| **Total** | **23** | **13** | **0** | **10** |

Blob verification: 35 of 35 MATCH.

REC DELTA status after Proof:
- The **3 conflict resolutions** (CF-1, CF-2, CF-3) are source-confirmed on the base A2 side (PC-D-23, 21, 22). The superseded D1 wording stays recorded in the REC DELTA section 3.
- The 9 delta CONTRADICTION items are source-confirmed on the A2 side where A2 disagreed: G2 closure (PC-D-16, 19), C18 amendment and D11 (PC-D-16), D03 (PC-D-12), CRQ-09 and C28 (PC-D-21), CRQ-11 (PC-D-16) and K1–K4 (PC-D-23). K5 is interpretive, and PC-D-17 records the exact comment text. **All stay CONTRADICTION for A3.** None is closed.
- The 18 UPP items have their static basis confirmed. **All stay UPP** until their runtime cases (PC-D-01..10, base PC-MAIL-04, 05, 09) run.
- The R-a items D13 and D16 are MATCH on PC-D-19 and PC-D-20.
- D14 is merged into base REC-38. Base PC-MAIL-05 remains its only runtime case.

## 6. A3 eligibility

**Disposition: PROOF DELTA PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.**

A3 can challenge **now**, within static scope:
1. The REC DELTA classifications, rules R-a, R-b and R-c, the D14 merge, and the 3 conflict resolutions against PC-D-21, 22 and 23.
2. The 13 executed static cases, including whether each expected/fail pair was falsifiable, and refinements RD1–RD6.
3. The supersede map: G3 and G4 moved to closed-static, G2 and G5 were narrowed, and the base net totals are MATCH 27, CONTRADICTION 6, UPP 18, GAP 5.
4. The QID lineage change (Q038 mapped; 16 QIDs with no evidence), and the choice not to map Q039 and Q047.
5. Proof-design gaps: there is no case for publisher message escaping (RD3), N5 or G12, and no D1-specific case for D14 (merged by design).

**Blocked** until the runtime device is available: PC-MAIL-D-01..10. This covers guest cookie replay, link-preview SSRF and volume, push endpoint SSRF by role, publisher egress capture, mass-mail explicit ids, comment-mode unsafe body, superuser-mode language rendering, install-time editor group and cross-company plans. Closing any UPP item, or settling the practical effect of any CONTRADICTION, is also blocked. A full A3 → MASTER handoff is **not** eligible yet.

## 7. Limitations

- No runtime was executed and no runtime result is claimed. Static PASS results confirm source readings at the anchor only.
- Framework semantics were not traced: RPC reachability of public model methods, root-identity access checks, proxy cookie rewriting and network egress controls. Overrides from other modules or Enterprise were also not traced.
- Line pointers are approximate and valid only at the anchor.
- No percentages, no Formal Coverage claim, no git operations. No existing file was edited. A3 static work on `mail` was not consulted.

## Appendix A — Predeclared cases (verbatim copy of PC_MAIL_D_CASES_PREDECLARED.frozen.md, sha256 d65394799e9b1e307beb35505b37c58bc1f0a2df404eb4b06d5641a47087fe66, declared 2026-09-27T15:17:31Z before any source fetch)

### PC-MAIL-D predeclared proof cases — mail DELTA D1 (written BEFORE any source fetch)

Declared: see declared_time.txt (UTC) written in the same step. Intake of inputs: 2026-09-27T15:16:23Z.
Anchor: odoo/odoo@8d05257d83f9128953f580a066db67c48fcdb96f. Every fetched file must hash (`git hash-object`) to the expected blob (full value from Lane A PASS-2 / PASS-1 tables, or the A2 D1 8-hex prefix where no full value exists). Mismatch => case BLOCKED (not PASS, not FAIL).
Runtime device: offline. No external endpoint other than the raw source host is contacted (NOT the publisher URL, NOT any link-preview / push / GIF / translation endpoint).
Static PASS confirms a source reading only; it is never counted as the result of a runtime case.

Common runtime setup RT-D (from A2 D1 section 6 + base RT-SETUP): disposable DB built from anchor, `mail` installed, no reverse proxy; companies A and B; internal user Ui (non-editor), internal user Ue (template editor), portal user P, admin Adm; a local capture listener L on loopback (HTTP) inside the test host only.

#### Runtime layer (PR-MD1..10 -> PC-MAIL-D-01..10; device offline => NOT-EXECUTED this cycle)

| PC | PR | Layer | Preconditions | Steps | Expected | Fail |
|---|---|---|---|---|---|---|
| PC-MAIL-D-01 | PR-MD1 (D01, AO-M1, CRQ-19) | RUNTIME | RT-D; public channel with guest access; no proxy | Anonymous browser joins public channel -> guest created; capture Set-Cookie for guest cookie; delete guest record; replay cookie on a guest-aware route | Cookie HttpOnly, ~365 d expiry, no Secure, no SameSite; after deletion replay yields no guest identity | App emits Secure or SameSite; or deleted guest's cookie still authenticates |
| PC-MAIL-D-02 | PR-MD2 (D03, AO-M4, CRQ-13) | RUNTIME | RT-D; L serves HTML with <title> on loopback; an external-looking host redirecting to L (local DNS/hosts only) | Ui posts message with (a) loopback URL to L, (b) redirecting URL; inspect L log, stored preview rows, bus payload to channel members | L receives GETs; title stored in preview and broadcast to channel members | No request reaches L, or no internal metadata stored |
| PC-MAIL-D-03 | PR-MD3 (D03, F-M2) | RUNTIME | RT-D; 20 distinct loopback endpoints on L returning 404 or non-HTML | Ui posts one message with 20 links; count L requests | 20 outbound requests | <= 6 requests (cap applies to failures) |
| PC-MAIL-D-04 | PR-MD4 (D04, AO-M2, CRQ-14) | RUNTIME | RT-D; server public VAPID key known; L as push endpoint | (a) Ui, (b) P call device registration with endpoint -> L; trigger a push to each; also try endpoint host ending `.invalid` | POST reaches L for each role able to call the method; roles recorded; `.invalid` host not contacted | Registration succeeds but no POST sent; or POST sent to `.invalid` host |
| PC-MAIL-D-05 | PR-MD5 (D05, D06, CRQ-15) | RUNTIME | RT-D; publisher URL option set to L (config file) — the real publisher URL is never contacted | Run publisher job manually; L replies with 2 messages + enterprise section; inspect L body, all-employees channel, `database.*` params; record default URL scheme from config; deactivate job; run scheduler | Body has exactly D05 fields; 2 messages posted in all-employees channel; 6 params overwritten; default scheme http; no egress after deactivation | Extra/missing fields; messages not posted; egress after deactivation |
| PC-MAIL-D-06 | PR-MD6 (D08, CRQ-16, N2) | RUNTIME | RT-D; records R1 readable and R2 unreadable by Ui on a thread model | Ui runs composer mass-mail with explicit id list [R1,R2] and a template reading R2 fields | Access error on R2; no outgoing mail for R2 | Outgoing mail created with content from R2 |
| PC-MAIL-D-07 | PR-MD7 (D11, F-M1, CRQ-17) | RUNTIME | RT-D; template T on a thread model; Ui non-editor | Comment mode: Ui opens composer with T, edits body to include an unsafe expression, sends; repeat in mass-mail mode | Comment mode: body editable; expression rejected or left literal, not evaluated. Mass mail: body not editable | Unsafe expression evaluated |
| PC-MAIL-D-08 | PR-MD8 (D11, AO-M5) | RUNTIME | RT-D; template T2 whose language expression reads a field of a related record Ui cannot read | Ui sends with T2 unchanged | Language resolves, no access error (superuser elevation); outcome recorded as design input | Access error raised |
| PC-MAIL-D-09 | PR-MD9 (D12, K5, G13, CRQ-21) | RUNTIME | Fresh install | List internal users in editor group; set restrict-rendering off via settings, list again; set on, list again | After install only system admins hold editor group; off -> internal users gain it; on -> removed | Internal users hold editor group after install; or toggle has no effect |
| PC-MAIL-D-10 | PR-MD10 (D15, CRQ-20) | RUNTIME | RT-D; user Ua with only company A active; activity plan PB of company B | Ua creates activities directly from PB (outside the scheduling wizard) on a record Ua can write | Allowed (no record rule blocks) | Refused by a record rule |

#### Source / config layer (static basis; EXECUTE this cycle)

| PC | Links | Layer | File(s) (expected blob) | Steps | Expected (PASS) | Fail |
|---|---|---|---|---|---|---|
| PC-MAIL-D-11 | PR-MD1; D01; AO-M1; N1 | SOURCE | addons/mail/models/discuss/mail_guest.py (9c7c2192c6d5da4f8b334c967a094c381b6c2786); odoo/http.py (A2 prefix ebfc2ac8) | Read guest cookie setter; read framework response cookie wrapper defaults; grep guest model for token rotation/revocation routine | Guest cookie set HttpOnly, ~365 d, no Secure/SameSite argument; framework wrapper default Secure off and SameSite not set / none; no rotation/revocation routine in guest model | Secure or SameSite passed by the module; or framework default Secure on / SameSite set; or a rotation routine exists |
| PC-MAIL-D-12 | PR-MD2, PR-MD3; D03; F-M2; AO-M4; N6 | SOURCE | addons/mail/tools/link_preview.py (18515419263f8fc005029601a5c7bc821cc9f727); addons/mail/models/mail_link_preview.py (153d3026c1f392519078fa17a6e47a1c2b075689) | Read fetch call (redirects, timeout, stream, UA); search for private/loopback address filtering; read per-message cap loop and per-domain throttle query; read what fields of an HTML response are stored and whether they are broadcast | GET with redirects, 3 s, streamed; no address filter; cap counts only successfully created previews; throttle counts stored previews in a recent window; HTML title / OG fields stored and sent to readers | Address filter present; or cap/throttle counts every attempt; or no response content stored |
| PC-MAIL-D-13 | PR-MD4; D04; AO-M2; G14 | SOURCE+CONFIG | addons/mail/tools/web_push.py (e660da83af7f5b0282b10b64367c0bfb8559da97); addons/mail/models/mail_push_device.py (A2 prefix 5a5a521b); addons/mail/security/ir.model.access.csv (29275551e7ca156899fa03985765fb2828de0b06) | Read endpoint host check in send; read registration method visibility, VAPID-key check, endpoint validation, reassignment of existing endpoint, sudo write; read push-device ACL | Only `.invalid` refused; registration method is public-callable (no leading underscore), requires only matching public VAPID key, no scheme/host check, can reassign existing endpoint row, writes under sudo; ACL system-only | Host/scheme validation present; or registration private; or no sudo write |
| PC-MAIL-D-14 | PR-MD5; D05; D06; K7; N5 | SOURCE+CONFIG | addons/mail/models/update.py (05603784124c160005a75d3c77afee94c72d2f62); addons/mail/data/ir_cron_data.xml (d72aacbe8f9e17e84d4dd62dfc3642a1ba4dc9fd); odoo/tools/config.py (433ff84b625a69e08cce9f42911aa608d3e615ee); addons/mail/models/__init__.py (553bd76763256a3cdd19b1863da6d8983eef76f8) | Enumerate payload keys; read transport (timeout, method), response parsing, message posting target and privilege, `database.*` keys overwritten; cron record user/interval/noupdate/mode; config default URL scheme and file-only flag; model import | Payload = D05 field list; POST 30 s; literal parse; elevated comment post to all-employees channel to root partner, per-message errors swallowed; six `database.*` params; cron weekly, root, null mode, noupdate; default URL `http://`; model defined in mail and imported | Field list differs; https default; no channel post; param set differs; cron not root |
| PC-MAIL-D-15 | PR-MD6; D08; G12; N2 | SOURCE | addons/mail/wizard/mail_compose_message.py (32fdf95981c9ea92af0d506711414decb32d2cd1) | Read mass-mail target resolution (domain vs explicit ids), any explicit per-record access check, sudo mail creation, batch-size parameter fallback, blacklist default; grep responsible-user field references | Domain searched in caller env, else explicit id list; no explicit per-record access check; outgoing mail created sudo; batch fallback 50; blacklist on by default; responsible-user field declared only | Explicit access check on ids present; or mail created non-elevated; or field used in file |
| PC-MAIL-D-16 | PR-MD7, PR-MD8; D11; F-M1; AO-M5; N3 | SOURCE | addons/mail/models/mail_composer_mixin.py (57f7a65ac0654fa88fadea44c1c63a9847919bc2); addons/mail/wizard/mail_compose_message.py (32fdf959...) | Read field-render elevation on equality; read language-render elevation mechanism; read mixin body-edit rule and wizard override of body-edit compute | Field render elevated via bypass marker on equality for non-editors; language render on equality uses full superuser record; wizard override: body editable outside mass mail regardless of template; mass mail falls back to editor-or-no-template | Language render uses bypass marker only; or wizard body-edit in comment mode requires no template (D1 wording) |
| PC-MAIL-D-17 | PR-MD9; D12; K5; K6; G13; CRQ-21 | SOURCE+CONFIG | addons/mail/models/ir_config_parameter.py (edbfc4f5c22d7414416c4dd839f425405db4f850); addons/mail/data/ir_config_parameter_data.xml (1f556c605ddc3dbd13dbf68554cabec78dc47906); addons/mail/data/mail_groups.xml (4b4125ed11ba10696bb321cf40f7573ec4387ec8) | Read param-setting override (truthiness test, group toggle); read seed record type and values (restrict rendering, gc years); read editor group implied-by; read the catalogue comments for both params | Toggle only in set routine, truthiness-based; seed loaded as data record (restrict = 1, gc = 3); editor group implied by system group only; catalogue comments say "not activated by default" (restrict) and "0 (skipped) by default" (gc) | Seed restrict = 0; or group data gives internal users editor group; or comment text absent |
| PC-MAIL-D-18 | PR-MD10; D15; CRQ-20 | SOURCE+CONFIG | addons/mail/models/mail_activity_plan.py (aefe528e2d1517e2145abe568cd543445b42a1ac); addons/mail/models/mail_activity_plan_template.py (5510608988e2a99942d7d24aeeb83ff17c8086c3); addons/mail/models/mail_activity.py (66d9cd7994a49fc01d62d4992b64501cc26bfc48); addons/mail/models/mail_template.py (f95b8f53dd95166603eadd42013907b77a23870f); addons/mail/security/mail_security.xml (0219605e445b1f0f545e78f15aa6bca9084a0b5b); ir.model.access.csv | Plan company field + default; plan-line company related; model-level auto company-check flag; activity/template company field absence; template cross-company partner warning; plan rules and ACLs | Plan company defaults to current; plan line related; no model auto-check flag; no company field on activity/template; warning present; plan rules have no company term; internal users read-only on plans | Company rule on plans; or auto-check flag present; or company field on activity/template |
| PC-MAIL-D-19 | D13 residual (A2 PARTIAL: P20-P24 not re-read); G2 | SOURCE+CONFIG | wizard/mail_template_reset.py (33036193b1dec7d16c21712c2a462d5864513577); wizard/mail_followers_edit.py (aa7e46bade32f1f16f31ef1f0804db4659edb7e8); wizard/mail_activity_schedule.py (0e67cb0efe1b4903c7118d568b47d41de66f6220); wizard/mail_blacklist_remove.py (f4347d54b9d9a7aebe79cd2693962b85bbb1bef0); wizard/base_partner_merge_automatic_wizard.py (3a99a177281a2787e2a9786447f993c769f3bd75); wizard/mail_template_preview.py (23b0e07760dc59d393dc165ef8513080c290f013); ir.model.access.csv | Check each D13 sub-statement: reset editor-only (ACL); follower edit reuses subscribe/unsubscribe; blacklist remove admin-only (ACL); merge logs partner names+emails; schedule wizard impersonation create check for upload assignee; preview renders as current user, model list sudo | Every D13 sub-statement holds | Any sub-statement contradicted |
| PC-MAIL-D-20 | D16 residual (A2 PARTIAL: P26 not re-read) | SOURCE | models/mail_alias_mixin.py (88cecd644378ce58ad57a5b2c199eeffa9eefc58); models/mail_alias.py (3d5c8fb2b32e82bc9a20f6cde25f036675d02989) | Read alias creation values in mixin (company source); alias domain/company validation; default domain | Mixin creates alias with owner record's company (or fallback); validation binds domain to owner/target company; default domain from current company | Alias company not derived from owner record |
| PC-MAIL-D-21 | CF-2 (C28 / CRQ-09) | SOURCE | controllers/attachment.py (70db479c69e1ed277b56e2199b9c77d6ff63dc97) | Read decorators of upload, delete, zip routes; delete access basis | Upload and delete carry guest-context decorator; zip route has no guest-context decorator and no module-level access check; delete by ownership | Zip has guest decorator or explicit check; or delete uses thread access |
| PC-MAIL-D-22 | CF-3 (C29) | SOURCE | controllers/discuss/gif.py (f5eba191836f3ebc7ffd8177e13c41e489d3f31b) | Inspect outbound parameters of GIF search/categories | Search term (+ key, client key) sent; no message content | Message content sent |
| PC-MAIL-D-23 | CF-1 (K1, K3, K4) | SOURCE | models/models.py (1edb1f78d952f754d364ac7d6e7863f7ef58bbf5); models/mail_thread.py (c1f8a83bbd4d6667c1ee7cd38b78cef71ad8f374); controllers/thread.py (57ab2401542aff66eb0cf4b4329bcf92cbda0912); models/discuss/discuss_channel.py (57e38f3446071bd42ef4b80583a4b16f31c97423) | K1: document operation mapping for write/unlink; K4: helper warn-only vs controller allowlist filtering; K3: count company-context emptying sites | K1: write/unlink -> document write; K4: controllers filter kwargs before helper, helper warns only; K3: >= 3 emptying sites across thread/channel/controller | Mapping to post access; or controllers pass raw kwargs; or <= 2 sites |
