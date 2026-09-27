# G01 PLATFORM_BASE — RED TEAM PROOF Addendum R1 (A3 remediation, batch B3B) — `web`, `web_tour`, `http_routing`, `html_editor`, `mail`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **PROOF**. Addendum only; the original Proof and Proof-delta documents are NOT edited |
| Group / Modules | G01 PLATFORM_BASE / `web`, `web_tour`, `http_routing`, `html_editor`, `mail` |
| Date | 2026-09-27 |
| **REC consumed (pinned)** | `G01_RECONCILIATION/G01_B3B_REC_ADDENDUM_R1_20260927.md` sha256 **`94291f21f0c33da30b7353000b2a54ca5bd1e574e3182f7f94e998abc6735b1d`** (frozen 2026-09-27T15:49:29Z, before this stage's predeclaration). Parent RECs it amends (pinned; equal to A3 intake): web `9e2a4a370ffb4e9a010e81633da1e85f0db4c2a762f8c26322ef38074e5abc2d`; web D1 `b89931533a23ace1fc25d9cecd5febd2e305b84cf83e4e94aa0a2f40f2c00985`; web_tour `b875cc2864bbe03fa9773802b54417062f9f2ce643e240ebd3c08906bdd59c55`; http_routing `b20ab28814a7586ac8de4d436d9572bfd292f9f9ff27bdc84b622882c54e215a`; html_editor `6677f36de93e588de97f55946fce1d7f8904a534854c7a81ca38aec46e83eae8`; mail `d5c8ea38e8436a431f3183754b38f312d99b3f613fb8716084ea367d9a6bada4`; mail D1 `bb5de020246be21a802880bfa3d0b411a6c430c84237cf57ae6e14bc59b8812f` |
| Upstream A2 addendum | `G01_A2_REVIEWS/G01_B3B_A2_ADDENDUM_R1_20260927.md` sha256 `d9eee187342b1c648c50a2d2bb9c4e6d38f81b074c35335aadd2183237cc975b` |
| Parent Proofs (superseded in part; pinned; equal to A3 intake) | `G01_PROOF/G01_WEB_PROOF_20260927.md` `a72724e8c7f1f5eb3b3f7707b511de3383b45b5b0b1f2d88e67db58771719d57`; `G01_PROOF/G01_WEB_PROOF_DELTA_D1_20260927.md` `93c3cf17105da8e57fb3c8d791bca1264d2cc09fc06394e632f7a6b772bd27fd`; `G01_PROOF/G01_WEB_TOUR_PROOF_20260927.md` `96c82939d402cc7c9270b084a3ab53d537fb85e1156e29fec673e7e79e5f7fa8`; `G01_PROOF/G01_HTTP_ROUTING_PROOF_20260927.md` `fac9922f3ff1515edd7f0a63315f2cbebae214799e9eaba475ed0d64ae610bf8`; `G01_PROOF/G01_HTML_EDITOR_PROOF_20260927.md` `eb8dcbced4686fbc6b27cd4d68df8836d28613478652e38cf17831ee4446eb7b`; `G01_PROOF/G01_MAIL_PROOF_20260927.md` `2f83f7cfab848c3b7a41b8c54802de8ebd57dabfaaa902b01078d86989441273`; `G01_PROOF/G01_MAIL_PROOF_DELTA_D1_20260927.md` `09f1e1ac9e69ed8a7903f4825e9dfed8b00126552e8b8d9e4782a603f3b5ed3c` |
| A3 reports | web `a9e45066528fc584f38c8f7395c5aec971a70a41908bccbf53753ad128ef3583`; web_tour `e250bd923ea3bf2b0788512362b95ee315ace377c5d0e00e3edcadbee0f85a9f`; http_routing `d1e32ae9a74f63603dbdd76f63deba296f90e90de4dafaccbbfbee0ed9d21297`; html_editor `d51187b446cd5aba0de82e62ce4c848f13aff7aa1d33ed3b31ee271d69281ecb`; mail `ada5f82a06d4f73d286a8f73c3f51ad1a0ad564a28568eb1f1e4706e683f414f` |
| Challenge IDs addressed (Proof parts) | **web:** D-W4 (PC-WEB-15 split), D-W5 (REC hash pin), A3 §5 (empty grouped/flat runtime case), D-W2 (static cases for new notes). **web_tour:** D-T2 (REC hash pin), A3-T-09 (OM-T03 case), D-T1 (static case). **http_routing:** A3-HROU-D1 (unmatched-branch static case; R05 extension), A3-HROU-N1 (R02 expected text), A3-HROU-N2 (R01 legs). **html_editor:** A3-HEDT-N1 (R2 closed), A3-HEDT-N2 (header capture), A3-HEDT-N3 (scheme annotation). **mail:** A3-D1 (zip "unchecked" wording in PROOF §6), A3-D2 (cross-module base company case), A3-D3 (PC-05 third outcome), A3-D4 (PC-02/03/10/18 design), A3-D5 (cases for REC-36/45), A3-D6 (Q019 static support), A3-D7 (Proof now pins a frozen REC) |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`. No other host contacted |
| Runtime device | OFFLINE (unchanged). All RUNTIME cases NOT-EXECUTED; nothing fabricated |
| Scratch | `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/remed_b3b/` |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

### 0.1 C1-B process-rule compliance (this Proof addendum)

| Rule (MASTER C1-B) | Compliance |
|---|---|
| 1. Preserve A2 `MISSING_REQUIRED_RUNTIME_PROOF` labels | **Complied.** Every runtime case below that derives from an A2 PR is marked with the A2 label; Proof does not re-label any REC Lane B cell (REC R1 section 1 carries the restorations) |
| 2. Post-declaration text tagged `POST-DECLARATION` | **Complied.** Expected and fail text in section 2 is reproduced from the predeclared file unchanged. Any observation added beyond it, and any source file fetched beyond the predeclared list, is tagged **POST-DECLARATION** in section 3 |
| 3. REC scans all A1 item classes | **Upstream (REC R1 section 7).** Proof adds cases for the newly carried items (A1 X3 via PC-MAIL-44; A1N notes via PC-WEB-31..34, PC-WTOUR-15, PC-HROU-12/14) |
| 4. Order A2 → REC (sha256) → Proof predeclare → Proof execute; header records REC sha256 | **Complied.** A2 R1 hashed 15:47:12Z → REC R1 frozen 15:49:29Z (sha256 in header) → predeclaration hashed 15:50:28Z → first Proof fetch 15:50:36Z → execution log 15:51:36Z |
| 5. Predeclared cases hashed + UTC before first Proof source fetch | **Complied.** See section 1: cases file sha256 and UTC stamp recorded 15:50:28.02Z; first Proof source fetch started 15:50:36.00Z into a fresh directory (`src_proof/`) created after the stamp |

Clean-room note: neutral summaries and pointers only; no vendor code reproduced. No QID answered. No percentages. No Formal Coverage. No git operations. No existing artifact edited.

## 1. Predeclaration record (before any Proof source fetch)

| Item | Value |
|---|---|
| Cases file | `remed_b3b/PROOF_CASES_PREDECLARED_B3B_R1.md` (file mtime 2026-09-27T15:50:24.64Z) |
| sha256 | **`d3b62b3d9c6f5e08b8f9dafcec01ebd58c1ce2aeb475044f0d0f194099894259`** (`predeclared_R1.sha256`) |
| UTC stamp | **2026-09-27T15:50:28.019724719Z** (`predeclared_R1.ts`) |
| First Proof source fetch | `proof_fetch_start.ts` = 2026-09-27T15:50:36.004860677Z; `src_proof/` did not exist before this (checked) |
| Proof blob log | `blob_log_proof.txt` sha256 `886b91251e92a0989c7198101867209fcdea6be59a296d802f27ceaf6e6ee2f3` (25 files, all HTTP 200) |
| Execution log | `exec_R1.txt` sha256 `0ab9fbc33afa3bd2e23fcb4d1d76b8f91bdd5c8cdc43d536b5eaa13108210d59` (15:51:36Z) |
| Disclosure | The A2/REC owner-stage re-derivation read the same anchor files earlier (15:36:51Z, `src_rederive/`, log sha256 `b614470cb255a4a33d20b40485f290d181ebf90c9f1c8ce74272005413a7ceb4`). Predeclaration precedes Proof execution, not all reading. Each case keeps a fail branch that would contradict the A2 R1 reading, to counter confirmation bias |
| Limitation | The cases file lives in scratch and is not git-committed; the sha256 + UTC stamp + fresh-directory ordering is the available evidence. mtimes are not tamper-evident |

### 1.1 Blob verification (fresh Proof fetch; `git hash-object`)

21 predeclared files MATCH the blobs pinned by earlier stages or by A2 R1: export.py `cb750f19`, tools/misc.py `6d275059`, orm/models.py `11f50c4e`, tools/config.py `433ff84b`, service/db.py `63c314a7`, web home.py `292aaa75`, odoo/http.py `ebfc2ac8`, tools/osutil.py `e77a96d7`, web binary.py `7b7b84f7`, web_tour tour.py `575bf0a5`, http_routing ir_http.py `d508ceb8`, website_data.xml `ddf87b43`, http_routing template `5c5e7d00`, html_editor main.py `df0db6c7`, web ir_http.py `bd03fa8e`, base ir_attachment.py `905ae118`, base ir_binary.py `e7feca93`, orm/environments.py `ec6b89fc`, mail_message.py `4a70962d`, mail attachment.py `70db479c`, mail ir_cron_data.xml `d72aacbe` (equals the parent mail Proof value).

**POST-DECLARATION** (files fetched after the first execution pass, to confirm the superuser-mode premise of PC-MAIL-44; the case text was not changed): `odoo/orm/utils.py` blob `06f6ef71772858462e5f0923941a0450ac662749`; `odoo/addons/base/data/res_users_data.xml` `3cca8531297cdc922a247796457548f608ac7cf8`; `odoo/addons/base/models/ir_cron.py` `e8762b920da6a68fd655dccf1a936671838c561d`; `odoo/addons/base/data/base_data.sql` `25d0cc7443c3347c237e99bca4c939ce071c59da`. No earlier stage pinned these; recorded only.

## 2. Cases (as predeclared) and results

### 2.1 SOURCE / CONFIG cases — EXECUTED

| PC | REC link | Layer | Expected (predeclared, summary) | Fail condition (predeclared, summary) | Observed (neutral; approx. lines) | Result |
|---|---|---|---|---|---|---|
| **PC-WEB-29** | REC-WEB-27, R1-05 (OM-W02R1) | SRC | Grouped branch only when group-by and not import-compatible, ORM export called on the whole set before grouping; flat branch batches with a splitter that yields nothing for empty input; header row; log after both branches; ORM gate = admin or export group | Flat branch calls ORM export for an empty set; grouped branch skips it; condition differs; no log on empty flat path | Condition at export.py L572; grouped pre-call L573; flat batching L615-616; splitter yields nothing when the first piece is empty (misc.py L693-697); log with record count L622-624; gate orm/models.py L889 | **PASS** |
| **PC-WEB-15Ra** | REC-WEB-11 | CFG | list_db default on; master secret file-only with well-known literal default; verify false on empty; set hashes in memory only, no file write | Any default differs; set writes the file | config.py L207 (file-only, literal default), L415 (listing default on, disabled by "no database list"), L1033-1034 (set: in-memory hash only), L1036-1047 (verify: false on empty; upgrade on success) | **PASS** |
| **PC-WEB-15Rb** | REC-WEB-11 | SRC | Declared dependency with 15Ra. Service change function calls set, then saves only the master-secret key; management decorator refuses when list_db off | No save after set; no list_db gate | service/db.py L413-417 (set then save of that key), L46-49 (decorator refuses when listing off) | **PASS**. Together with 15Ra this reproduces the parent PC-WEB-15 "set persists a hash" without a hidden cross-case dependency (A3 D-W4). Parent PC-WEB-15 PASS is not re-labelled |
| **PC-WEB-31** | REC-WEB-R1-01 | SRC | Client page frame-deny (+no-store); login same-origin framing + frame-ancestors-self policy | Either header set absent or different | home.py L79-80 (client page), L152-153 (login) | **PASS** (bounded to two routes) |
| **PC-WEB-32** | REC-WEB-R1-02 | SRC | Filename = model description + technical name + fixed extension, sanitised, attachment disposition RFC 6266, fixed content type; no request parameter in filename | Request parameter feeds filename; inline; no sanitiser | export.py L537-538 (name), L629-636 (sanitiser → disposition helper; content type), L655 / L703 (CSV / XLSX types); disposition helper builds an attachment disposition with RFC 6266 encoding (http.py L353-369) | **PASS** |
| **PC-WEB-33** | REC-WEB-R1-03 | SRC | Both export routes serialise the exception into the server-error payload; serialiser includes a formatted traceback | No traceback field; exception not serialised | export.py L649-651, L697-699; serialiser traceback field http.py L478 | **PASS** |
| **PC-WEB-34** | REC-WEB-R1-04 | SRC | Content and image routes keep the stream's default no-sources policy; stream sets no-sniff; post-dispatch no-sniff + image policy when absent; asset route disables stream policy | Content/image route overrides policy; defaults differ | binary.py L82/L89 and L210/L217 (no policy override), L156/L163 (asset route disables); http.py L617 (stream default policy), L685 (no-sniff), L2457 (post-dispatch calls setter), L2796-2806 (setter: no-sniff; adds policy to image types lacking one) | **PASS** |
| **PC-WTOUR-15** | REC-WTOUR-25, 26 | SRC | Guide id and step ids deleted; empty content key omitted | Any id retained; placeholder for empty content | tour.py L56 (guide id removed), L104 (step id removed), L108-109 (empty content key deleted) | **PASS** |
| **PC-HROU-11** | REC-HROU-03 (unmatched branch) | SRC | First-match not-found strips a language segment with no route flag; redirect allowed for non-POST by default; language resolution under temporary public identity; final not-found forces both frontend flags | Returns before language logic; flags not forced; redirect needs a route flag | ir_http.py L379-381 (not-found branch), L388 (redirect permission defaults to allowed when no multilang flag exists), L403 (temporary public identity), L476-479 (flags forced true, re-raise); error handler handles frontend requests only (L574) | **PASS** |
| **PC-HROU-12** | REC-HROU-19 | CFG | Website data declares a published page record with URL `/contactus`; 404 template links it | No such record | website_data.xml L495-496 (page record, URL), published flag in the same record; template L134 (link) | **PASS** |
| **PC-HROU-13** | REC-HROU-13 | SRC | Shape route public/http/website-flagged; bad-request on invalid colour; handler forces public user and calls the requester-unchecked debug handler; 400 template has the debug block; 404 has none | Route not public/flagged; no bad-request; 400 lacks block; debug handler checks requester | html_editor main.py L550 (route flags), L119/L122 (bad-request); http_routing ir_http.py L580-581 (public user; debug handler); web ir_http.py L51-52 (debug from query string, no requester check); template 400 at L81 with block at L88; 404 at L119 with no block before the 415 template (blocks at L107 belong to 403, L162 to 415) | **PASS** |
| **PC-HROU-14** | REC-HROU-28, 29 | SRC | Rebuild failure falls back to quoted requested path; canonical output drops the query string | Name-bearing slug on failure; canonical keeps query string | ir_http.py L150-152 (fallback on not-found/access/missing), L157-158 (canonical join without query string) | **PASS** |
| **PC-HEDT-13** | REC-HEDT-10, 08 | SRC | SVG served via content/image routes gets SVG type, no-sniff and no-sources policy; shape SVG responses get the policy from post-dispatch | SVG responses on these paths would carry no policy | Same lines as PC-WEB-34; the image-type test in the setter (http.py L2803) covers the SVG content type; the shape route sets only content type and cache headers, so post-dispatch adds the policy | **PASS** |
| **PC-HEDT-14** | REC-HEDT-10 (R2 closure) | SRC | XML-like MIME (SVG included; office XML excepted) forced to plain text when the context flag is set OR the actor (superuser dropped) lacks view write | Condition differs | ir_attachment.py L418-428 | **PASS**. Closes parent Proof refinement R2 at source |
| **PC-MAIL-18R** | REC-MAIL-11, 38 | SRC | Read probe in triggering env; only missing-record error caught; recipients current user (unless public) + author; per-recipient serialisation under that user; no per-recipient check before serialisation | Per-recipient check exists; recipients differ; other exceptions caught | mail_message.py (method L1352-1380): probe L1364; missing-record catch L1367; current-user recipient L1372; author recipient L1374-1375; serialisation under each recipient's user L1379 | **PASS** (replaces the parent PC-MAIL-18 dependency on comment text; the parent PASS is not re-labelled) |
| **PC-MAIL-42** | REC-MAIL-09, 11, 33, 43 | SRC (cross-module) | Empty context → all user's companies; foreign ids → access error unless superuser; lazy; superuser id always superuser mode; with-user drops superuser mode; read probe true in superuser mode | Empty → main company only or beyond; foreign accepted; with-user keeps superuser | environments.py L64-67 (superuser id ⇒ superuser mode), L266-283 (empty ⇒ all user companies; foreign ids ⇒ access error unless superuser); orm/models.py L4128 (probe true in superuser mode), L6001 (with-user drops superuser mode) | **PASS** |
| **PC-MAIL-43** | REC-MAIL-28, 61 | SRC (cross-module) | Zip route public, no guest decorator, browses ids in request env; base streaming reads stored fields on the non-elevated record; fetch filters by access and raises for forbidden ids; attachment search admits public read, filters linked by linked-record access, unlinked only system/creator | Elevated read; no raise; no access filter | attachment.py L110-117 (route; no guest decorator in L107-118), L23 (base streaming per record); ir_binary.py L70 (attachment converted by its own stream builder on the same record); orm/models.py L3802 (access-filtered search), L3824 (access error for forbidden ids); ir_attachment.py L633 (filter skipped only in superuser/bypass), L638 (public), L645 (unlinked: creator) | **PASS**. Supports A3 CH-1a: the zip route is not "unchecked"; base enforces read access implicitly |
| **PC-MAIL-44** | REC-MAIL-11, 38, 57 | SRC | With PC-42: in a superuser-mode environment the probe passes for every record; only the missing-record error is caught; deleted-without-cascade records are skipped | Probe per recipient or superuser dropped; other exceptions caught | Probe runs in `self.env` (L1364); only missing-record caught (L1367-1369, in-source comment on deletion without cascade). Queue cron user is the root user (ir_cron_data.xml L9). **POST-DECLARATION** support: the root user record is id 1 (base_data.sql L134-135), the superuser id is 1 (orm/utils.py L19), and cron jobs build their environment with the job's user id (ir_cron.py L482); with environments.py L64-67 the queue-job environment is therefore in superuser mode | **PASS**. Limitation: the failure path from the queue into the status push is taken from parent PC-MAIL-36 (mail_mail.py L280-286) and was not re-read here |

### 2.2 RUNTIME cases — NOT-EXECUTED (device OFFLINE; ready to run; authorised sandbox only)

All cases below derive from A2 or A2 R1 proof requirements and carry the A2 label **MISSING_REQUIRED_RUNTIME_PROOF**.

| PC | = PR | REC link | Setup / action (predeclared) | Expected (predeclared) | Fail condition (predeclared) | Result |
|---|---|---|---|---|---|---|
| PC-WEB-30 | PR-W09 | REC-WEB-R1-05, 27 | User without export group and without Access Rights; empty domain; (a) XLSX grouped, import-compat off; (b) CSV flat; (c) CSV flat import-compat on | (a) refused, no file; (b), (c) header-only file and one info log with zero records | (a) returns a file; or (b)/(c) refused | **NOT-EXECUTED** |
| PC-WTOUR-16 | PR-T04 | REC-WTOUR-18 (OM-T03) | U consumed guide G (name N); system user deletes G, creates G2 named N; U requests current guide and consumes N | G2 offered as unconsumed (if eligible); consume links U to G2 only | G2 treated as consumed without a new consume; or delete refused due to progress rows | **NOT-EXECUTED** |
| PC-HROU-R01b | PR-HROU-01R1 (b) | REC-HROU-13 | DB without website; anonymous GET shape route with invalid colour, plain and with debug param | Plain: 400 without debug block. Debug param: 400 with debug block and traceback | Block without param; or no block with param | **NOT-EXECUTED** |
| PC-HROU-R01c | PR-HROU-01R1 (c) | REC-HROU-13 | Same route, non-numeric animation-speed parameter | 500 template; block only with debug param | Block without param; no block with param; non-500 status | **NOT-EXECUTED** |
| PC-HROU-R01d | PR-HROU-01R1 (d) | REC-HROU-13 | Frontend request whose template rendering raises a nested not-found | Promoted to 500; block only with debug param | 404 rendered; or block visibility differs | **NOT-EXECUTED** |
| PC-HROU-R02R | PR-HROU-02R1 | REC-HROU-19, 14 | (i) without website; (ii) with website; unknown frontend path; follow `/contactus` | (i) 404 template, shape image loads, `/contactus` not found; (ii) same 404, `/contactus` served | (i) 418/500/render error or `/contactus` served; (ii) `/contactus` not served | **NOT-EXECUTED** |
| PC-HROU-R05b | PR-HROU-05 extension | REC-HROU-10, 03 | Multilang DB; unmatched crafted paths with language prefix and slash/backslash host-like segments, GET | Every 3xx Location is local | Any off-host Location | **NOT-EXECUTED** |
| PC-HEDT-R04b | PR-HEDT-04R1 | REC-HEDT-08 | SVG created via media-library stub; fetch via content and image routes; open directly and in object/iframe | SVG content type, no-sources policy, no-sniff; embedded script does not execute | Policy absent/permissive; script executes | **NOT-EXECUTED** |
| PC-HEDT-R05b | PR-HEDT-05R1 | REC-HEDT-10 | Editor **without** view write stores SVG via modify_image; same capture | Stored MIME SVG (reset) and same headers; script does not execute | As R04b; or stored MIME plain text | **NOT-EXECUTED** |
| PC-MAIL-02R | PR-01bR1 | REC-MAIL-40 | Ua ({A}) explicit recipient of comment on Rb (B); by-id read | Body returned | Refused / no body | **NOT-EXECUTED** |
| PC-MAIL-03R | PR-02R1 | REC-MAIL-08, 09 | Ua ({A}) and Uab ({A,B}, active A) post and upload to Rb | Ua refused (not found); Uab succeeds | Ua succeeds; or Uab refused | **NOT-EXECUTED** |
| PC-MAIL-05R | PR-04R1 | REC-MAIL-11, 21, 38 | Uab authors on Rb; loses B; delivery failure via queue job; capture bus payloads | (i) Rb data in Uab payload = FAIL; (ii) none, no error = PASS; (iii) access error in serialisation = PASS for disclosure if no Rb data reached Uab, plus a separately reported robustness observation (abort scope) | — (outcomes as stated) | **NOT-EXECUTED** |
| PC-MAIL-10R | PR-09R1 | REC-MAIL-05, 39 | Portal P; non-comment internal-class message on readable document D | Search excludes; by-id read returns body | Fail A: search returns it. Fail B: by-id refused | **NOT-EXECUTED** |
| PC-MAIL-45 | PR-14 | REC-MAIL-36 | Ua addresses (a) unreadable Pb (company B, no token), (b) shared Ps, (c) role R including Ub ({B}) | (a) Pb not a recipient; (b) Ps notified; (c) Ub resolved and notified | (a) Pb notified; (b) Ps not notified; (c) Ub not resolved | **NOT-EXECUTED** |
| PC-MAIL-46 | PR-15 | REC-MAIL-45 | Default-policy alias; inbound with sender = internal user Ui's address from an unrelated host; sandbox gateway without transport authentication | Accepted; author = Ui's partner | Rejected by the module; or author not Ui's partner | **NOT-EXECUTED** |

### 2.3 Totals (this addendum)

| Layer | Cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| SOURCE / CONFIG | 18 (PC-WEB-29, 15Ra, 15Rb, 31, 32, 33, 34; PC-WTOUR-15; PC-HROU-11, 12, 13, 14; PC-HEDT-13, 14; PC-MAIL-18R, 42, 43, 44) | 18 | 0 | 0 |
| RUNTIME | 15 (PC-WEB-30; PC-WTOUR-16; PC-HROU-R01b, R01c, R01d, R02R, R05b; PC-HEDT-R04b, R05b; PC-MAIL-02R, 03R, 05R, 10R, 45, 46) | 0 | 0 | 15 |

No runtime result is claimed or inferred. A static PASS confirms only that the source reads as predicted.

## 3. Status of parent cases and wording (not re-declared, not edited)

| Parent item | Status after R1 |
|---|---|
| PC-WEB-11 (FAIL) | **FAIL preserved** as a failed result against its predeclared (A2-inherited) expectation. Its observation is re-confirmed by PC-WEB-29 PASS against the corrected A2 R1 expectation. The parent case is not re-declared |
| PC-WEB-15 (PASS) | Stands; its compound cross-case condition is now made explicit by PC-WEB-15Ra + 15Rb (A3 D-W4). Future cases declare cross-case dependencies explicitly |
| Parent web / web_tour Proof headers ("REC … (this run)") | Superseded for lineage by this header, which pins the parent REC sha256 values and the REC R1 sha256 (A3 D-W5, D-T2) |
| PC-HROU-09 (PASS) | Stands for its stated (matched-endpoint) branch; A3-HROU-D1 weak-condition finding accepted; the unmatched branch is covered by PC-HROU-11 |
| PC-HROU-R01, R02, R05, R06 | Retained as declared. R01 legs extended by R01b–d; R02 expected text superseded for consumption by R02R; R05 extended by R05b. **R06 not extended (DISPUTED in part, A3-HROU-D1):** the canonical-slug redirect runs in pre-dispatch for a matched endpoint only (parent PC-HROU-10); an unmatched path raises not-found in the match step and never reaches pre-dispatch (PC-HROU-11 L476-480), so an unmatched-path leg of R06 has no reachable behaviour to test |
| Parent http_routing Proof limitation "`/contactus` provider not found" | Closed at source by PC-HROU-12 |
| PC-HEDT-04 (PASS) and refinement R2 | PASS stands; R2 closed by PC-HEDT-14. R04/R05 retained; header legs added (R04b/R05b) |
| PC-HEDT-02 (PASS) | **Annotation (A3-HEDT-N3):** "no scheme allow-list" is accurate for the module and fetcher files; the HTTP client mounts only http/https adapters, so the effective scheme set is client-constrained. Verdict unchanged |
| Parent mail Proof §6 item 4 wording "the unchecked zip route (PC-25)" | **Withdrawn for consumption.** Replaced by: "the zip route, which has no guest context and no module-level check; access is enforced implicitly by base streaming (PC-MAIL-43)" (A3-D1) |
| Parent mail Proof §7 routing of base company semantics to runtime | Superseded for the static part by PC-MAIL-42 and PC-MAIL-44. Runtime cases stay required |
| PC-MAIL-02, 03, 05, 10 | Retained as declared, NOT-EXECUTED; superseded for consumption by PC-MAIL-02R, 03R, 05R, 10R (falsifiable forms). When run, the parent cases' records must be kept alongside, not overwritten |
| PC-MAIL-18 (PASS) | PASS stands; its comment-text leg is not relied on. PC-MAIL-18R is the behaviour-only replacement |
| PC-MAIL-32, 36, 37, 38, 40 ("Differs" fail conditions) | PASS stands; A3's under-specification note is accepted for future declarations (fail conditions will name the specific differing value). No re-execution was required by A3 |

## 4. Effect on REC items (for A3)

- REC-WEB-27: static support for CONTRADICTION — RESOLVED (source layer) via PC-WEB-29; residual REC-WEB-R1-05 awaits PC-WEB-30.
- REC-WEB-R1-01..04, REC-WTOUR-25/26, REC-HROU-28/29: static support PASS for the new MATCH items (Q042, Q046, Q034, Q015, Q033, Q016, Q008, Q006 lineage; the last two provisional).
- REC-HROU-03: both branches now have static cases (PC-HROU-09 matched; PC-HROU-11 unmatched); stays CONTRADICTION — OPEN.
- REC-HEDT-10/08: serving mitigation confirmed at source (PC-HEDT-13); downgrade condition confirmed (PC-HEDT-14); exploitability remains runtime (R04b/R05b).
- REC-MAIL-09/33/43: base semantics confirmed (PC-MAIL-42). REC-MAIL-11/38: the queue-job path is in superuser mode, so the gate is not narrowed there (PC-MAIL-44; supports the partial DISPUTE in A2 R1 6.3 and REC R1 6.2). REC-MAIL-28: implicit base read check confirmed (PC-MAIL-43). REC-MAIL-57 (Q019): static support PC-MAIL-44.
- All UNKNOWN_PENDING_PROOF items stay open until their runtime cases run.

## 5. Limitations

- Static source at one commit; line pointers approximate. No runtime, browser, proxy, database or mail-transport state observed.
- Negative/absence results are bounded to the files named. The mail queue failure path (parent PC-MAIL-36) was not re-read in R1.
- The predeclaration evidence is a scratch file with sha256 + UTC stamp + directory ordering; it is not git-committed.
- No Formal Coverage, no percentages, no git operations, no QID answered, no existing artifact edited.
