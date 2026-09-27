# G01 PLATFORM_BASE — RED TEAM A3 Independent Challenge (STATIC scope) — `mail`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, the independent adversarial challenger. Scope is STATIC only |
| Independence | A3 did not author Lane A, A1, A2, REC or PROOF for `mail`. Every source reading below was re-fetched and re-hashed by A3. It does not rely on the PROOF scratch copies |
| Group / Module | G01 PLATFORM_BASE / `mail` |
| Date | 2026-09-27 (intake 15:1x Z; written 15:18 Z) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Runtime | The 14 runtime cases PC-MAIL-01..14 are **NOT-EXECUTED**. They are neither passed nor failed |
| Out of scope | A1 delta D1 and Lane A PASS-2 (not opened) |
| **Overall disposition** | **A3 STATIC PASS WITH DEFECTS (route to REC, PROOF; A2 for proof-requirement gap; lineage note to MASTER/Integration Control)**. No A2-side CONTRADICTION reading was refuted. No defect is blocking, but none is closed. The package still needs runtime before MASTER consolidation |

### 0.1 Intake hashes (sha256, taken as the first A3 action; saved to scratchpad `a3_mail/intake.sha256`)

Paths are relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

| Input | sha256 | Agrees with upstream record |
|---|---|---|
| `G01_LANE_A_PASS1/G01_MAIL_LANE_A_PASS1_20260927.md` | `8511f925843c54984cc4fb0edf589c8e3421640e38e996551d236b7958be22e6` | yes (REC 0.1) |
| `G01_A1_PACKAGES/G01_MAIL_A1_PACKAGE_20260927.md` | `dde12053f968e2b55bc906da7175840d119386bb051f6b21a80885e209ff092f` | yes |
| `G01_A2_REVIEWS/G01_MAIL_A2_REVIEW_20260927.md` | `e587bf12e221a2d8be6e32f056ee37d1c4b88dbc8495a87a7b6e0d80287d56e8` | yes |
| `G01_RECONCILIATION/G01_MAIL_REC_20260927.md` | `d5c8ea38e8436a431f3183754b38f312d99b3f613fb8716084ea367d9a6bada4` | equals committed HEAD (6302d8f); no working-tree diff |
| `G01_PROOF/G01_MAIL_PROOF_20260927.md` | `2f83f7cfab848c3b7a41b8c54802de8ebd57dabfaaa902b01078d86989441273` | equals committed HEAD (811e8ae) |
| `../GMVQ/G01_PLATFORM_BASE/G01_MAIL_GMVQ_MVQ_50_V1.00_DRAFT.md` | `0d6d7fcc4d6fef3be30ee281ee7096e8fc1fdb9e94d96ff120d0f5e79a10bf7d` | equals the `bank_files` entry in FREEZE_W1-B01 |
| `../GMVQ/G01_PLATFORM_BASE/FREEZE_W1-B01.json` | `d0edfb228d849b5633cdd1dccea95667305831c2c264f43432c337c4fa3d1351` | freeze_hash field `558ec880…7177` matches the value REC and PROOF quote |

### 0.2 Exit hashes

At exit, A3 re-ran sha256 over all 7 inputs and they were unchanged; the values are in the table above. A3 edited no input. It cannot record this file's own hash inside itself, so that hash is in the A3 hand-off message.

### 0.3 Source re-verification by A3 (`git hash-object` on fresh fetches)

- All 19 `addons/mail/` files that PROOF section 2 relies on returned HTTP 200. Each matches its recorded blob. `tools/discuss.py` matches as well (`692708b5629e…`).
- Extra files A3 fetched to test the claims (not in Lane A, so they have no recorded blob; A3 hashes are shown):
  - base `odoo/addons/base/models/ir_binary.py`: `e7feca93…`
  - base `odoo/addons/base/models/ir_attachment.py`: `905ae118…`
  - `odoo/orm/models.py`: `11f50c4e…`
  - `odoo/orm/environments.py`: `ec6b89fc…`
  - `addons/mail/wizard/mail_compose_message.py`: `32fdf959…`

Clean-room note: this record holds only neutral WHAT/WHY/RISK paraphrases and identifier pointers. It reproduces no vendor code, uses no percentages and makes no Formal Coverage claim. Git was used read-only.

## 1. Challenge log

### CH-1 Re-derivation of REC items from source (10 items re-derived)

| Target | A3 re-derivation (source, anchor) | Refuted? | Disposition |
|---|---|---|---|
| REC-05 / C05 CONTRADICTION (and REC-39) | Message per-record check: for read and create, a non-internal user is excluded from internal-class messages only when the message type is comment. For write and unlink the exclusion applies to every type. The search path adds the share domain for every non-internal user, whatever the type. A2's operation-dependent scope holds. A1 BR2 ("never, whatever their rights") is too absolute at source level | No | UPHELD (A2 side) |
| REC-16 / REC-31 (C16, K1) | Activity write and unlink use the rule, or else the message-operation mapping. The base mapping in `models/models.py` sends write and unlink to document **write** and create to post access. The activity docstring still says "post access or write" (R2 confirmed) | No | UPHELD (A2 side) |
| REC-28 / C28 | Upload resolves the thread with post access and carries the guest context. Delete is gated on attachment ownership, not thread access, and then runs elevated. Zip is public and has no guest-context decorator. It browses the ids in the request env and streams them through base. See CH-1a | No (A2 side holds) | UPHELD, with the wording defect in CH-1a |
| REC-29 / C29 | The GIF search sends the search term, the API key and **the database name as client key**. No message content goes out (R1 confirmed). Translation sends the message body | No | UPHELD |
| REC-34 / K4 | The model helper only logs disallowed params (it does not raise), and its base allowlist is empty. The HTTP getters filter kwargs to the model allowlist before calling the helper, for both message and thread | No | UPHELD |
| REC-33 / K3 (MATCH "broader") | Four emptying sites confirmed: thread helper, inbox push, channel broadcast, post controller. A2 only extends A1 in the same direction, so MATCH (not CONTRADICTION) is the correct class | No | UPHELD |
| REC-10 / PC-15 (no company in record rules) | 26 `ir.rule` records, zero "company" hits, 14 distinct models. No rule on message, followers, outgoing mail or alias | No | UPHELD |
| REC-40 / PC-17 (message record-company unused in access) | Referenced only at the stamping sites in thread (post, bulk post, reset, field list). The message search override, the per-record check and forbidden-access code never read it. A3 addition: the composer wizard also stamps it (not an access use; wizard is G2 scope). PC-17's absence claim covers only fetched files | No | UPHELD (scope limitation noted) |
| REC-11 / REC-38 (L1361 identity) | The unresolved allowed-company comment sits at L1361. The read check runs in the triggering env at L1364. The payload goes to the current user and the author (L1371-1379). See CH-1c | Partially qualified | INCONCLUSIVE on "no per-recipient check" (CH-1c) |
| REC-42 / O7b (attachment company from cookie) | For a company-less thread the company is taken from the `cids` cookie: main company if present, else the first id. It goes into an **elevated** create. That path never builds an environment from the cookie ids, so base's company-membership validation (CH-1b) does **not** apply | No; A3 finds the risk *stronger* than "runtime-dependent" | UPHELD |
| REC-43 / O7a (redirect widening cookie) | The retry adds the suggested company, and the cookie is written only after the widened check succeeds. See CH-1b: base limits that widening to companies the user belongs to | Qualified | CHALLENGE-SUSTAINED (REC/PROOF), see CH-1b |

**CH-1a Zip route: "no access check" is true only at module level. CHALLENGE-SUSTAINED (owner PROOF; REC wording).**

A3 checked outside `mail`, as the brief asked:

- Base binary streaming hands an attachment straight to the attachment's own stream builder.
- That builder reads stored fields (mimetype, name, checksum, store name and so on) on the recordset in the **request env**. Because it is not elevated, the ORM fetch runs the attachment model's access-filtering search.
- That search limits attachments to those whose parent record the caller can access; public attachments are allowed for read. The fetch then raises an access error for any forbidden id.

So base enforces access implicitly. A2's own wording ("depends on base binary streaming") is accurate. The overstatements are in PROOF section 6 ("the unchecked zip route") and REC 2.3 / REC-52 ("no … access check" read as a finding).

A3 inference, statically predicted and not proven: the missing guest context tends toward *fail-closed* behaviour. Token-bearing guests lose access; unauthorized users do not gain it. PC-MAIL-04's expected "no bytes" is consistent with this.

Action: correct the wording. PC-04 stays required, because runtime decides the outcome.

**CH-1b Company-context semantics can be read statically in base. CHALLENGE-SUSTAINED (owner REC and PROOF).**

REC-09, REC-11, REC-43 and PROOF section 7 route "empty or cookie-supplied allowed-company context" to runtime. A3 read `odoo/orm/environments.py` (companies property) at the anchor:

- An **empty** context resolves to **all of the user's companies**. The base comment explains why.
- A non-empty context that names a company outside the user's set raises an access error, unless the env is superuser.

This settles two things statically:

1. The emptying sites (K3) widen visibility to the acting user's full company membership, not beyond it.
2. A forged cookie on the redirect route cannot add a company the user does not belong to. The UNKNOWN_PENDING_PROOF items keep their runtime cases, but the stated risk should be narrowed: "cross-company within the user's membership", not "arbitrary company".

This does not apply to REC-42, where cookie ids go into an elevated create (CH-1 table).

Action: PROOF should add a cross-module SOURCE case for the base company resolution. REC should restate the risks for REC-09, REC-11, REC-33 and REC-43.

**CH-1c L1361 "no per-recipient read check". INCONCLUSIVE (advisory to PROOF).**

- The method makes no explicit per-recipient check. That part is confirmed.
- However, the payload for each recipient is serialised under that recipient's user. The serialiser's fields (thread display name, body) default to non-elevated reads.
- Implicit ORM enforcement may therefore raise an access error during serialisation, instead of leaking. Only a missing-record error is caught at that point.

Static reading cannot settle this. PC-MAIL-05 has only two outcomes, "push carries Rb name" and "no push". It should also record a third: a serialisation or access exception that aborts the push or the queue batch.

### CH-2 Re-execution of static PASS cases (9 re-executed)

Re-executed on A3's own fetches:

| Case | Result |
|---|---|
| PC-15 | PASS reproduced |
| PC-17 | PASS reproduced, with the scope note in CH-1 |
| PC-18 | PASS reproduced, but see CH-1c |
| PC-19 | PASS reproduced |
| PC-20 | PASS reproduced |
| PC-21 | PASS reproduced |
| PC-24 | PASS reproduced |
| PC-25 | PASS reproduced (literal reading). The fail condition "Guest decorator or explicit check present" was falsifiable, but it tests the wrong question for the risk (CH-1a) |
| PC-27, PC-28, PC-29, PC-30, PC-33, PC-39 | PASS reproduced |

PC-28 detail: the token is an HMAC over the path plus sorted params, keyed with the database secret, and compared in constant time. The rendered page always shows the display name read elevated. The link back is hidden only for logged-in users without read access.

Weak or unfalsifiable conditions (CHALLENGE-SUSTAINED, owner PROOF):
- **PC-MAIL-02**: the fail column reads "Not readable (BR1 wrong); either outcome recorded". Every outcome counts as success, so the case is not falsifiable.
- **PC-MAIL-03**: Uab's leg is "outcome recorded", with no fail condition for Uab.
- **PC-MAIL-10**: the by-id leg fails only "while BR2 asserted absolute". A1 BR2 *is* stated as absolute, so that condition should be pinned now, not left conditional.
- **PC-MAIL-18**: part of the expected result is the presence of a code *comment* (FIXME). That tests text, not behaviour.
- **PC-32, 36, 37, 38, 40**: fail condition "Differs". This is falsifiable against the specific expected value, but under-specified.

These are design-quality defects. They do not invalidate the static PASS results.

### CH-3 Predeclaration integrity

- **Content is UPHELD.** Git commit `ece5c2d` (15:05:02Z) holds a 57-line pre-execution version of the PROOF file. Its sha256 is `ab9a427da177…1235`, exactly the snapshot hash PROOF claims.
- Its tables are byte-identical, ignoring blank lines, to PROOF Appendix A in HEAD (`811e8ae`) and to the scratch file `rec_mail/PC_MAIL_CASES_PREDECLARED.md`. The scratch file's sha256 is `05f17cf8…8955`, as claimed.
- **Timing limitation.** The first scratch source fetch has mtime 15:04:57Z, which is *before* the git commit at 15:05:02Z. Git therefore proves the declaration existed within 5 s after the first fetch, not before it.
- The claim "declared 15:04:34Z before any fetch" rests on mutable filesystem mtimes: declaration 15:04:34.69Z, first fetch 15:04:57.35Z. Those times are consistent with the claim but are not tamper-evident.
- Disposition: UPHELD for content; timing is plausible but not independently provable.

### CH-4 Lineage

See section 2. Disposition: UPHELD for content integrity. CHALLENGE-SUSTAINED (owner MASTER / Integration Control; labelling only) because the commit subjects are misleading. Also CHALLENGE-SUSTAINED (owner REC; process): the REC file was not frozen before PROOF ran.

- REC's final version (commit at 15:10:22Z) cites PROOF case results in its Basis column. REC 6 admits this ("for classification support, the static proof results from Stage 2").
- So the REC→PROOF handoff was not one-way. A3 checked every class against A1/A2 alone, and the class values do not depend on the PROOF results. The defect is procedural.

### CH-5 Proof-requirement gaps, overclaim, Lane B, QID mapping, clean room

- **REC-36 (O2) and REC-45 (O8) have no runtime case.** CHALLENGE-SUSTAINED (owner A2 for the missing PR; PROOF to add cases).
  - REC-36 (addressing any readable partner; role expansion elevated) maps to HIGH-tier Q005 and Q006.
  - REC-45 (alias open to everyone by default) maps to Q010 and Q011 (spoofed attribution).
  - Both have a falsifiable runtime form: cross-company addressing by Ua, and a spoofed-sender inbound to a default alias. Both should have proof requirements.
- **Overclaim.** The zip wording is covered in CH-1a and the base-semantics deferral in CH-1b. No PASS was counted toward runtime; PROOF 1 and 5 say this explicitly. No percentages or Formal Coverage anywhere. Otherwise UPHELD.
- **Lane B.** No Lane B artifact exists, and A3's `find` for lane_b, gemini or evidence_pool also returned none. REC does not treat that absence as a failure. The UNCORROBORATED/NOT_APPLICABLE tally recounts to 32/24, matching REC. UPHELD.
- **REC counts.** Recount from the table: 56 items, MATCH 25, CONTRADICTION 6, UNKNOWN_PENDING_PROOF 18, GAP 7. There are 33 mapped QID rows, plus 17 listed as having no evidence, which makes up the 50 in the bank. UPHELD.
- **QID mapping fit.**
  - A3 sampled five mapped QIDs: Q001, Q014, Q024, Q032 and Q045. Each is topically apt.
  - A3 then searched Lane A, A1 and A2 for the listed no-evidence QIDs: Q042 (reply-to), Q020 (archive), Q049 (automation), Q013 (active content), Q029 (duplicate inbound). None has evidence, so "no evidence" is correct for them.
  - **CHALLENGE-SUSTAINED (owner REC):** REC scope covers only C, K, O, SF-12 and G items. It drops A1 sections 2–7: business rules BR1–BR10, exceptions X1–X7, handoffs H1–H6 and candidate questions CRQ-MAIL-01..12. REC's scope rules neither reconcile nor carry them.
  - Consequence: A1 X3 (status push skips records deleted without cascade) is topical evidence for **Q019**, which REC lists as "no evidence". Q026 (threading determinism) is arguably touched by C23 route resolution.
  - CRQ-MAIL-09 (zip/delete by guests) has no REC disposition, although C28 covers its substance.
- **Clean room.** REC and PROOF contain no code blocks, function bodies or SQL. Short identifier fragments are used as pointers only: `default='everyone'`, `limit=10_000`, `process_email_queue(batch_size=1000)`, `has_access('read')`. UPHELD. Advisory: prefer prose over literal call signatures in downstream design artifacts.

## 2. Lineage (read-only git)

| File | Commits (`git log --follow`) | Note |
|---|---|---|
| Lane A PASS-1 | `da535e1` 14:50:12Z | Subject names mail |
| A1 package | `42612ef` 14:53:53Z | Subject names base_sparse_field, google_recaptcha only |
| A2 review | `0aad8c0` 15:01:36Z | Subject names base_sparse_field, google_recaptcha only |
| PROOF | `ece5c2d` 15:05:02Z (MASTER in-flight checkpoint: pre-execution declaration only); `811e8ae` 15:12:19Z (final) | The checkpoint captures on-disk state (timing only). The final version is additive: Appendix A is unchanged from the checkpoint |
| REC | `6302d8f` 15:10:22Z | Subject names resource, resource_mail only. This is the single commit; it came after the PROOF checkpoint |

- The author field is "Claude" on every commit, so git cannot tell stage authors apart. No commit shows a content change to an upstream stage's file after its first commit, other than the additive PROOF completion.
- HEAD equals the intake hashes for all five pipeline files.

## 3. Defects routed

| ID | Owner | Defect | Blocking? |
|---|---|---|---|
| A3-D1 | PROOF (REC wording) | Zip route described as "unchecked". Base enforces attachment read access in the request env (CH-1a) | No |
| A3-D2 | PROOF, REC | Base company-context semantics (empty means all of the user's companies; foreign ids are rejected) can be read statically but were deferred to runtime. Restate the risks for REC-09, REC-11, REC-33 and REC-43. REC-42 is unaffected (CH-1b) | No |
| A3-D3 | PROOF | PC-MAIL-05 lacks an exception/abort outcome (CH-1c) | No |
| A3-D4 | PROOF | PC-MAIL-02 is not falsifiable; PC-03 and PC-10 fail conditions are record-only; PC-18 depends on comment text (CH-2) | No |
| A3-D5 | A2, then PROOF | REC-36 and REC-45 have no proof requirement or runtime case (CH-5) | No |
| A3-D6 | REC | BR, X, H and CRQ items are neither reconciled nor carried. Q019 is mis-listed as having no evidence, because A1 X3 exists (CH-5) | No |
| A3-D7 | REC (process) | REC was not frozen before PROOF; its Basis column cites PROOF results (CH-4) | No |
| A3-D8 | MASTER / Integration Control | Commit subjects do not name `mail` for the A1, A2, REC and PROOF commits (lineage labelling) | No |

No A2-side reading of the six CONTRADICTION items (C05, C16, C28, C29, K1, K4) was refuted. They should stay CONTRADICTION, with both statements preserved, until MASTER consolidation. A3 recommends that A1 not be rewritten.

## 4. Runtime-blocked items

- PC-MAIL-01..14 are all NOT-EXECUTED; A3 infers no result from them. Their status is recorded in PROOF section 4.
- All 18 UNKNOWN_PENDING_PROOF items remain open.
- The runtime effect of C05, C16, C28 and K1 remains open (PC-10, PC-01, PC-07, PC-04).
- CH-1c: whether the author-side push leaks, is suppressed or raises.
- The CH-1a prediction that zip is fail-closed for guests. It is statically inferred only.
- The runtime legs of the proposed new cases for REC-36 and REC-45.
- A3 → MASTER full handoff: **pending runtime**.

## 5. Limitations

- Static scope only. A3 read the anchor files named above. Wizards (except a grep of the composer), JS, views, tests and other-module overrides were not studied.
- Base files were read to test specific claims only, not traced in full. The GitHub code search that pointed A3 to the composer wizard indexes the default branch, not the anchor. The anchor file itself was then fetched and hashed.
- The predeclaration timing evidence depends on mutable filesystem mtimes.
- The freeze hash was compared to the manifest field, not recomputed, because its algorithm is not stated.
- No percentages, no Formal Coverage claim. Git read-only. Inputs were not edited.
