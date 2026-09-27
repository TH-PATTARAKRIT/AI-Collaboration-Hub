# G01 PLATFORM_BASE — RED TEAM Reconciliation DELTA D1 — `mail`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | RED TEAM **RECONCILIATION (REC) — DELTA cycle D1**. Stage 1 of a two-stage REC + PROOF delta run. Stage 2 is `G01_PROOF/G01_MAIL_PROOF_DELTA_D1_20260927.md` |
| Group / Module | G01 PLATFORM_BASE / `mail` (display name "Discuss") |
| Date | 2026-09-27 |
| Nature | Addendum. The base REC `G01_MAIL_REC_20260927.md` has **not** been edited. This file records only the D1 reconciliation and the resulting net state of the affected base REC IDs (section 4) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Question bank / join key | `GMVQ/G01_PLATFORM_BASE/G01_MAIL_GMVQ_MVQ_50_V1.00_DRAFT.md`, sha256 `0d6d7fcc4d6fef3be30ee281ee7096e8fc1fdb9e94d96ff120d0f5e79a10bf7d`. This equals the FREEZE_W1-B01 `bank_files` entry. Freeze hash `558ec88047aef5c8e7ea0e2675b1c43ef358ec29b172d6878068330f3fba7177`; manifest sha256 `d0edfb228d849b5633cdd1dccea95667305831c2c264f43432c337c4fa3d1351`. MODULE `mail` + QID + freeze hash. The mapping is lineage only; **no QID is answered** |
| **Disposition** | **REC DELTA D1 COMPLETE — HANDOFF TO PROOF DELTA.** There are 51 delta rows. One of them (D14) is a duplicate merged into base REC-MAIL-38, which leaves **50 counted**: MATCH 19, CONTRADICTION 9, UNKNOWN_PENDING_PROOF 18, GAP 4. All 3 D1-vs-base-A2 conflicts are resolved in favour of base A2, and the source supports that result (section 3). REC closes no CONTRADICTION |

### 0.1 Parent artifacts (immutable; sha256 recorded at intake 2026-09-27T15:16:23Z)

Paths are relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

| Input | Path | sha256 | Cross-check |
|---|---|---|---|
| A1 DELTA D1 | `G01_A1_PACKAGES/G01_MAIL_A1_DELTA_D1_20260927.md` | `e3febb2e0fc0b50fd14b69c362798d673517d3e9eb1696980b18b380075f8c7f` | Equals the value in the A2 D1 header and the base REC excluded-input row |
| A2 DELTA D1 review | `G01_A2_REVIEWS/G01_MAIL_A2_DELTA_D1_REVIEW_20260927.md` | `8e6f5dc847e4ad52960098aa34fc15678c01d718f9e21d8afe00c313eeccdf9e` | "A2 DELTA PASS WITH FINDINGS": VERIFIED 29, PARTIAL 11, NOT_VERIFIED 0, OOS 2. Raises PR-MD1..10 and flags CF-1..3 and DUP-1..3 |
| Lane A PASS-2 | `G01_LANE_A_PASS2/G01_MAIL_LANE_A_PASS2_20260927.md` | `b2cdaa0cf60f6554828d7fcabd97ebb2ebd3735df090d9fb446f3bef8a6ea21b` | Equals the value in the D1 and A2 D1 headers |
| Base REC (read-only reference) | `G01_RECONCILIATION/G01_MAIL_REC_20260927.md` | `d5c8ea38e8436a431f3183754b38f312d99b3f613fb8716084ea367d9a6bada4` | 56 items: MATCH 25, CONTRADICTION 6, UPP 18, GAP 7 |
| Base PROOF (read-only reference) | `G01_PROOF/G01_MAIL_PROOF_20260927.md` | `2f83f7cfab848c3b7a41b8c54802de8ebd57dabfaaa902b01078d86989441273` | 27 static PASS, 14 runtime NOT-EXECUTED |
| Base A2 (read-only reference) | `G01_A2_REVIEWS/G01_MAIL_A2_REVIEW_20260927.md` | `e587bf12e221a2d8be6e32f056ee37d1c4b88dbc8495a87a7b6e0d80287d56e8` | Equals the value in the A2 D1 header |
| Bank | see header | `0d6d7fcc…bf7d` | Equals FREEZE_W1-B01 |
| Not used | `G01_A3_CHALLENGES/G01_MAIL_A3_STATIC_20260927.md` | — | Not present at intake. This delta does not depend on A3 |

### 0.2 Lane B

No Lane B / Gemini runtime observation for `mail` was supplied, and none was found. The base REC section 0.2 search stands, and this cycle added no new Lane B artifact. Every Lane B cell is UNCORROBORATED or NOT_APPLICABLE. Absence of Lane B evidence is never a FAIL.

Clean-room note: every statement is a neutral WHAT/WHY/RISK paraphrase. Identifiers and ~L pointers are evidence pointers only. No vendor code is reproduced, and nothing recommends reusing vendor schema, ORM, workflow, UI or naming. No percentages. No Formal Coverage claim. No git operations. No existing file was edited.

## 1. Classification rules (predeclared; base REC section 1 rules apply, with the D1 additions below)

- **MATCH**: A1 D1 and A2 D1 agree, or A2 strengthens without disagreeing, and the source supports the item. Runtime corroboration is optional.
- **CONTRADICTION**: A2 D1 marks the item PARTIAL **because it disagrees with the A1 D1 content or disposition**, or D1 conflicts with the base A2 review (CF-n). Both statements are preserved.
- **UNKNOWN_PENDING_PROOF (UPP)**: A1 and A2 agree at source level, but the claim or its stated risk depends on runtime, configuration or identity. This also covers a carried gap that has a declared proof case.
- **GAP**: evidence is missing, and no proof case in scope can settle it this cycle.
- **D1 addition R-a**: when A2 D1 marks an item PARTIAL **only because A2 did not re-read the cited evidence** (D13, D16), and asserts no disagreement, REC routes it to a predeclared static case. If that case PASSes, the class is MATCH; otherwise it is UPP.
- **D1 addition R-b**: an A2 OUT_OF_SCOPE row ("unchanged, not addressed") takes the base REC class of its underlying items.
- **D1 addition R-c (dedupe)**: a D1 item that A2 identifies as the same finding as a base item is merged into that base REC ID and excluded from the delta count.
- **Conflict rule**: when D1 conflicts with base A2, the base A2 correction prevails where a hash-verified static re-read supports it (PC-MAIL-D-21, D-22, D-23). The superseded D1 wording is quoted and kept.

## 2. Reconciliation table

PC-D-nn means PC-MAIL-D-nn in the PROOF DELTA. The static cases PC-D-11..23 were executed and all PASS. The runtime cases PC-D-01..10 are NOT-EXECUTED. "Base PC-nn" means a case in the base PROOF.

### 2.1 D1 disposition changes to parent items (23 rows, mirroring A2 D1 section 3.1)

| REC ID | D1 item | D1 disposition | A2 D1 verdict | REC class | Basis | Lane B | Proof link | Base REC affected | QID lineage |
|---|---|---|---|---|---|---|---|---|---|
| REC-MAIL-D1-01 | G2 wizards | CLOSED-STATIC (+N2, N3) | PARTIAL (closure too strong → NARROWED) | **CONTRADICTION** | A1 says closed, A2 says narrowed. The static checks (PC-D-19) show the D13 sub-statements hold, but D11 is misdescribed (PC-D-16), and N2 and N3 remain runtime questions. REC adopts **NARROWED**. The D1 word "CLOSED-STATIC" is superseded | NOT_APPLICABLE | PC-D-15, 16, 19 | REC-51 | Q037 |
| REC-MAIL-D1-02 | G3 guest decorator / Store | CLOSED-STATIC (+N1) | VERIFIED | MATCH | Mechanism re-read (PC-D-11). Per-route coverage is carried as N1 (D1-43) | NOT_APPLICABLE | PC-D-11 | REC-52 | — |
| REC-MAIL-D1-03 | G4 publisher egress | CLOSED-STATIC | VERIFIED | MATCH | PC-D-14. The runtime effect is carried by D05 and D06 | UNCORROBORATED | PC-D-14 | REC-53 | — |
| REC-MAIL-D1-04 | G5 unstudied features | NARROWED | VERIFIED | MATCH | Link preview and web push are now studied. Everything else is still open | NOT_APPLICABLE | PC-D-12, 13 | REC-54 | — |
| REC-MAIL-D1-05 | G8 company FIXME | NARROWED | VERIFIED | MATCH | Scope is stated precisely (D14). Runtime is still open under REC-11 and REC-38 | UNCORROBORATED | base PC-18 | REC-10, 11 (fold) | Q032 |
| REC-MAIL-D1-06 | G9 empty-company semantics | UNCHANGED OPEN | VERIFIED | MATCH (no change) | No change asserted | UNCORROBORATED | base PC-20 | REC-09 | Q032 |
| REC-MAIL-D1-07 | G1, G6, G7, G10, G11 | UNCHANGED | OUT_OF_SCOPE | GAP (R-b) | Carried. G10 and G11 stay folded into REC-13 and REC-47 as in the base | NOT_APPLICABLE | — | REC-50, 55, 56 | — |
| REC-MAIL-D1-08 | C10 no company rules | REAFFIRMED | VERIFIED | MATCH | PC-D-18 re-checked the plan rules: the system group has 1=1 and there is no company term | NOT_APPLICABLE | PC-D-18; base PC-15 | REC-10 | Q001, Q025 |
| REC-MAIL-D1-09 | C11 status push | REFINED by D14 | VERIFIED (= SF-05) | UPP | Author vector = base O4/SF-05. Runtime effect pending | UNCORROBORATED | base PC-18, 36; base PC-MAIL-05 | REC-11, 38 | Q007, Q023, Q032, Q048 |
| REC-MAIL-D1-10 | C15 guest identity | REFINED by D01, D02 | VERIFIED | UPP | Guest resolution is now known statically. Anonymous creation and cookie posture are runtime | UNCORROBORATED | PC-D-11; PC-D-01; base PC-MAIL-09 | REC-15 | Q031 |
| REC-MAIL-D1-11 | C18 template guard | AMENDED by D09–D12, K5 | PARTIAL | **CONTRADICTION** | The save-time vs render-time split is agreed (D09, D10, D12 MATCH). The amendment carries D11's inaccuracies (D1-34) and K5's ambiguity (D1-40) | UNCORROBORATED | PC-D-16, 17 | REC-18 | Q037 |
| REC-MAIL-D1-12 | C25 scheduled jobs | REFINED by D05, D06 | VERIFIED | MATCH | PC-D-14 cron record | NOT_APPLICABLE | PC-D-14 | REC-25 | Q045 |
| REC-MAIL-D1-13 | C28 attachment routes | REFINED by D02 (keeps "routes accept guest context") | PARTIAL (**CF-2**) | **CONTRADICTION** → resolved for base A2 | PC-D-21: upload, delete and PDF-first-page carry the guest decorator. Zip has **no** guest decorator and no module-level check. Delete works by ownership. See section 3 CF-2 | UNCORROBORATED | PC-D-21; base PC-24..26; base PC-MAIL-04 | REC-28 | Q001, Q014, Q050 |
| REC-MAIL-D1-14 | C29 outbound services | EXTENDED by D03–D05 | VERIFIED (**CF-3** noted) | MATCH (extension) | The extension holds (PC-D-12, 13, 14). The base C29 wording stays CONTRADICTION under REC-29: the GIF provider gets search terms plus the database name, not message content (PC-D-22). See section 3 CF-3 | UNCORROBORATED | PC-D-12, 13, 14, 22 | REC-29 | Q023 |
| REC-MAIL-D1-15 | C24 activity cleanup | UNCHANGED; K6 | VERIFIED | MATCH | The seed is 3. The comment says 0 (PC-D-17) | UNCORROBORATED | PC-D-17 | REC-24 | Q045 |
| REC-MAIL-D1-16 | Parent H6 → K7 | CORRECTED | VERIFIED | MATCH | The publisher model is defined in `mail` and imported by its roster (PC-D-14) | NOT_APPLICABLE | PC-D-14 | none (H6 was not a REC item) | — |
| REC-MAIL-D1-17 | CRQ-MAIL-01 | REFINED, OPEN | VERIFIED | UPP | Same as base PR-04 | UNCORROBORATED | base PC-MAIL-05 | REC-11, 38 | Q023, Q032 |
| REC-MAIL-D1-18 | CRQ-MAIL-05 | OPEN; G3 dependency removed | VERIFIED | UPP | Guest issuance volume is runtime | UNCORROBORATED | base PC-MAIL-09 | REC-15 | Q031 |
| REC-MAIL-D1-19 | CRQ-MAIL-07 | REFINED, OPEN | VERIFIED | UPP | Mass mail creates mail elevated after the implicit read (PC-D-15) | UNCORROBORATED | PC-D-15; PC-D-06 | REC-21 | Q007, Q038 |
| REC-MAIL-D1-20 | CRQ-MAIL-09 | OPEN; dependency moved to N1 | PARTIAL (**CF-2**) | **CONTRADICTION** → resolved for base A2 | The zip and delete parts are already answered from source (PC-D-21). Only the runtime byte exposure remains | UNCORROBORATED | PC-D-21; base PC-MAIL-04 | REC-28 | Q014 |
| REC-MAIL-D1-21 | CRQ-MAIL-11 | REFINED, OPEN | PARTIAL | **CONTRADICTION** | The named path is misdescribed. PC-D-16 supports A2: comment-mode body is always editable, and language rendering is elevated to superuser mode | UNCORROBORATED | PC-D-16; PC-D-07, 08 | REC-18 | Q037, Q050 |
| REC-MAIL-D1-22 | CRQ-MAIL-02, 03, 04, 06, 08, 10, 12 | UNCHANGED | OUT_OF_SCOPE | UPP (R-b) | Carried open questions. Base runtime cases apply | UNCORROBORATED | base PC-MAIL-01..14 as mapped | as base | as base |
| REC-MAIL-D1-23 | K1–K4 | "UNCHANGED (still CONFIRMED-FROM-SOURCE)" | PARTIAL (**CF-1**) | **CONTRADICTION** → resolved for base A2 | PC-D-23: K1 document operation = write; K3 has 4 emptying sites; K4 is filtered at the HTTP layer and only warned at model level. See section 3 CF-1 | NOT_APPLICABLE | PC-D-23; base PC-20..22, 29 | REC-31, 32, 33, 34 | Q001, Q014, Q032, Q050 |

### 2.2 New claims D01–D16 and new contradictions K5–K7 (19 rows)

| REC ID | Item | A1 D1 (claim / conf.) | A2 D1 verdict | REC class | Basis | Lane B | Proof link | QID lineage |
|---|---|---|---|---|---|---|---|---|
| REC-MAIL-D1-24 | D01 | Guest cookie: long-lived HttpOnly, no Secure/SameSite passed, no rotation / HIGH, LOW | VERIFIED (+AO-M1) | UPP | PC-D-11: framework wrapper defaults are Secure off and no SameSite; no rotation routine. The effective posture behind a proxy, and revocation, are runtime | UNCORROBORATED | PC-D-11; PC-D-01 | Q031 |
| REC-MAIL-D1-25 | D02 | Guest decorator: constant-time compare, non-elevated return, context guest must be a real record / HIGH | VERIFIED | MATCH | PC-D-11 (guest model token check) and A2 re-read | NOT_APPLICABLE | PC-D-11 | Q050 |
| REC-MAIL-D1-26 | D03 | Link preview SSRF, "a handful" cap, throttle / HIGH, LOW | PARTIAL (F-M2, AO-M4) | **CONTRADICTION** | A1 understates the volume. PC-D-12 supports A2: the cap counts only successful previews, the throttle counts only stored previews from the last 10 s, and HTML title / Open Graph fields are stored and bus-sent. Both statements preserved | UNCORROBORATED | PC-D-12; PC-D-02, 03 | Q023, Q031 |
| REC-MAIL-D1-27 | D04 | Web push to stored endpoint; only `.invalid` refused / HIGH, LOW | VERIFIED (+AO-M2) | UPP | PC-D-13: public model registration method, endpoint not validated, sudo reassignment. RPC reachability by role is runtime | UNCORROBORATED | PC-D-13; PC-D-04 | Q023 |
| REC-MAIL-D1-28 | D05 | Weekly root job sends instance and usage payload / HIGH | VERIFIED | UPP | PC-D-14 field list. Actual egress depends on deployment and network | UNCORROBORATED | PC-D-14; PC-D-05 | — |
| REC-MAIL-D1-29 | D06 | Plain-http default; remote content posted to a channel; 6 params overwritten / HIGH | VERIFIED | UPP | PC-D-14. Whether remote bodies are escaped when posted was not traced | UNCORROBORATED | PC-D-14; PC-D-05 | Q044 |
| REC-MAIL-D1-30 | D07 | Composer ACL, creator rule, modes, schedule only single comment / HIGH | VERIFIED | MATCH | A2 re-read, plus ACL rows seen in PC-D-19 | NOT_APPLICABLE | — | Q037, Q050 |
| REC-MAIL-D1-31 | D08 | Mass mail implicit-read authorisation; elevated mail creation / HIGH, MED | VERIFIED | UPP | PC-D-15. Whether the implicit read is sufficient (N2) is runtime | UNCORROBORATED | PC-D-15; PC-D-06 | Q037, Q038, Q050 |
| REC-MAIL-D1-32 | D09 | Restriction predicate / HIGH | VERIFIED | MATCH | A2 re-read | NOT_APPLICABLE | — | Q037 |
| REC-MAIL-D1-33 | D10 | Template protection at save time / HIGH | VERIFIED (+AO-M3) | MATCH | A2 re-read. AO-M3 (the Access Rights admin is exempt at render time but not at save time) is an A2 addition, not a disagreement | NOT_APPLICABLE | — | Q037 |
| REC-MAIL-D1-34 | D11 | Composer equality elevation; "non-editors can edit body only when no template" / HIGH, MED | PARTIAL (F-M1, AO-M5) | **CONTRADICTION** | PC-D-16 supports A2. The wizard override makes the body editable outside mass mail; language rendering on equality runs in superuser mode, not with the bypass marker. D1 sentence superseded | UNCORROBORATED | PC-D-16; PC-D-07, 08 | Q037, Q050 |
| REC-MAIL-D1-35 | D12 | Parameter toggles editor group; seed 1 / HIGH | VERIFIED | MATCH | PC-D-17. Refinement RD4 (toggle only in set-param) is for A3 | UNCORROBORATED | PC-D-17; PC-D-09 (confirmation) | Q037 |
| REC-MAIL-D1-36 | D13 | Preview, reset, follower edit, blacklist, merge, schedule / MED | PARTIAL (not re-read) | MATCH (R-a) | PC-D-19 PASS: every sub-statement holds at the anchor | UNCORROBORATED | PC-D-19 | Q037, Q003, Q025 |
| REC-MAIL-D1-37 | D14 | Status push to author without author check / HIGH, LOW | VERIFIED (**DUP-1** of SF-05 / PR-04) | UPP — **MERGED into REC-MAIL-38 (R-c); not counted** | Same finding as base O4/SF-05. CRQ-MAIL-18 is merged into base PR-04 / PC-MAIL-05. No new proof case | UNCORROBORATED | base PC-18, 36; base PC-MAIL-05 | Q002, Q007, Q023, Q032, Q048 |
| REC-MAIL-D1-38 | D15 | Templates and activities have no company; plan company only enforced in wizard / HIGH, LOW | VERIFIED | UPP | PC-D-18. Enforcement outside the wizard is runtime | NOT_APPLICABLE | PC-D-18; PC-D-10 | Q024, Q025 |
| REC-MAIL-D1-39 | D16 | Alias company and domain validation / MED | PARTIAL (mixin not re-read) | MATCH (R-a) | PC-D-20 PASS: the mixin creates the alias under the owner record's company | NOT_APPLICABLE | PC-D-20 | Q024, Q041 |
| REC-MAIL-D1-40 | K5 | Catalogue comment "not activated by default" vs seed 1 → comment stale | PARTIAL (comment ambiguous) | **CONTRADICTION** | PC-D-17 records the exact comment. It describes adding the editor group to internal users, which is "not activated by default"; that is consistent with the restricted seed on A2's reading and stale on A1's. Interpretive, with no behavioural effect. Both readings preserved for A3 | NOT_APPLICABLE | PC-D-17 | Q037 |
| REC-MAIL-D1-41 | K6 | GC comment says 0; seed is 3 | VERIFIED | MATCH | PC-D-17 | NOT_APPLICABLE | PC-D-17 | Q045 |
| REC-MAIL-D1-42 | K7 | Publisher model is internal to `mail` | VERIFIED | MATCH | PC-D-14 | NOT_APPLICABLE | PC-D-14 | — |

### 2.3 Gaps carried or added by D1 (9 rows)

| REC ID | Gap | A2 D1 position | REC class | Basis | Lane B | Proof link | QID lineage |
|---|---|---|---|---|---|---|---|
| REC-MAIL-D1-43 | N1: cookie defaults and per-route guest decorator coverage | Cookie half answered (AO-M1) | GAP (narrowed) | Cookie defaults: PC-D-11. Routes known to date: zip has no decorator; upload, delete and PDF-first-page do (PC-D-21). A complete route-by-route list across all controllers was not produced. Runtime posture is in PC-D-01 | UNCORROBORATED | PC-D-11, 21; PC-D-01 | Q014, Q050 |
| REC-MAIL-D1-44 | N2: implicit-read sufficiency in mass mail | Well-formed (CRQ-16) | UPP | PC-D-15 static basis | UNCORROBORATED | PC-D-06 | Q037, Q038 |
| REC-MAIL-D1-45 | N3: body-equality edge cases | Scope widened (CRQ-17) | UPP | PC-D-16 records the comparison over raw and sanitised values | UNCORROBORATED | PC-D-07 | Q037 |
| REC-MAIL-D1-46 | N4: identity on the mail-failure caller | Covered by base PR-04 | UPP | Base PC-36: the queue cron runs as the root user, and the failure path calls the status push. Whether that identity bypasses the read check is base semantics and runtime | UNCORROBORATED | base PC-MAIL-05 | Q007, Q032 |
| REC-MAIL-D1-47 | N5: all-employees channel definition not located | — | GAP | Not read this cycle | NOT_APPLICABLE | — | — |
| REC-MAIL-D1-48 | N6: no private-network filter for link preview or push | Scope widened (CRQ-13, 14) | UPP | PC-D-12 and 13 find no filter in the module. A framework or network guard is runtime | UNCORROBORATED | PC-D-02, 03, 04 | Q031 |
| REC-MAIL-D1-49 | G12: composer responsible-user field unused in file | Confirmed | GAP | PC-D-15 finds it declared only. Use by other modules is out of scope | NOT_APPLICABLE | — | — |
| REC-MAIL-D1-50 | G13: install-time group state vs seed | Answered statically (CRQ-21) | UPP | PC-D-17: the seed is a data record and the toggle lives only in set-param; the group data grants the editor group to the system group only. Runtime confirmation is PC-D-09 | UNCORROBORATED | PC-D-17; PC-D-09 | Q037 |
| REC-MAIL-D1-51 | G14: who may register push devices | Partly answered (AO-M2) | UPP | PC-D-13: a public model method writes under sudo. Reachability by role is runtime | UNCORROBORATED | PC-D-13; PC-D-04 | Q023 |

### 2.4 Class counts

| Class | Count | Items |
|---|---|---|
| MATCH | 19 | D1-02, 03, 04, 05, 06, 08, 12, 14, 15, 16 (dispositions); D02, D07, D09, D10, D12, D13, D16, K6, K7 |
| CONTRADICTION | 9 | D1-01 (G2), D1-11 (C18), D1-13 (C28/CF-2), D1-20 (CRQ-09/CF-2), D1-21 (CRQ-11), D1-23 (K1–K4/CF-1); D03, D11, K5 |
| UNKNOWN_PENDING_PROOF | 18 | D1-09, 10, 17, 18, 19, 22; D01, D04, D05, D06, D08, D15; N2, N3, N4, N6, G13, G14 |
| GAP | 4 | D1-07 (G1/G6/G7/G10/G11), N1, N5, G12 |
| **Counted total** | **50** | |
| Merged duplicate (not counted) | 1 | D1-37 (D14 + CRQ-MAIL-18) → base REC-MAIL-38 / PR-04 / PC-MAIL-05 |

Lane B column over the 50 counted rows: UNCORROBORATED 31, NOT_APPLICABLE 19. There is no FAIL for absence.

A2 D1 cross-check: all 29 A2 VERIFIED rows are MATCH or UPP here, with D14 merged. The 11 A2 PARTIAL rows are CONTRADICTION (9: G2, C18, C28, CRQ-09, CRQ-11, K1–K4, D03, D11, K5) or MATCH via R-a (2: D13, D16). The 2 A2 OOS rows follow R-b.

## 3. Conflict resolutions (D1 vs base A2) and dedupe

| # | Superseded D1 wording (kept verbatim in D1; not edited) | Base A2 position | Source check (hash-verified) | Resolution / net statement |
|---|---|---|---|---|
| **CF-1** | §1.4: "K1-K4: UNCHANGED (still CONFIRMED-FROM-SOURCE)" | K1 CONFIRMED, REFINED (document op is write); K2 CONFIRMED; K3 CONFIRMED and wider; K4 PARTIAL | PC-D-23 PASS. Document-operation mapping: read→read, create→post access, write/unlink→**write**. Company-context emptying at 4 sites (thread inbox push, thread-access helper, channel broadcast, post controller). Controllers filter kwargs to the allowlist before the helper, and the helper only warns | **Base A2 prevails.** Net: K1 = rule OR document *write* (not "post/write"). K2 unchanged. K3 = 4 sites. K4 = warn-only at model level, filtered at HTTP. D1 must not be read as re-confirming K1 or K4 as A1 first wrote them. Base REC-31 and REC-34 stay CONTRADICTION; REC-32 and REC-33 stay MATCH |
| **CF-2** | §1.2 C28: "public attachment routes accept guest context … per-route coverage still N1"; §1.3 CRQ-09: "dependency moved from G3 to N1" | C28 PARTIAL: zip has no guest context and no module-level check; delete works by ownership | PC-D-21 PASS. Upload, delete and PDF-first-page carry the guest decorator. Zip carries none and browses ids with no module check. Delete requires attachment ownership (write or scoped token) | **Base A2 prevails.** Net C28: the guest context applies to upload, delete and PDF-first-page, not to zip. Zip access is decided entirely in base binary streaming (base R5). The zip and delete parts of CRQ-09 are answered statically; only byte exposure remains (base PC-MAIL-04). REC-28 stays CONTRADICTION |
| **CF-3** | §1.2 C29: "EXTENDED by D03, D04, D05" with no correction of the base statement that message content goes to a GIF provider | C29 PARTIAL: the GIF provider receives search terms, not message content | PC-D-22 PASS. GIF requests carry the search term (or GIF ids), the API key and the **database name as client key**. There is no message content | **Base A2 correction prevails**, and the D1 extension is accepted. Net C29: message body → translation API (cached elevated per language); search terms and database name → GIF provider; notification payload → push endpoints; user-influenced outbound GETs → link preview targets; instance and usage data → publisher endpoint (weekly). REC-29 stays CONTRADICTION on the original A1 wording |
| **DUP-1** | D14 and CRQ-MAIL-18 presented as new | SF-05 / O4 / PR-04 | Base PC-18 and PC-36 (already PASS) | **Merged** into REC-MAIL-38. Counted once. PR-04 / PC-MAIL-05 is the single runtime case. No PC-MAIL-D case was created for it |
| DUP-2 | G3 closed via D02 | C15 note (cookie decorator) | PC-D-11 | Convergent. Recorded under D1-02 |
| DUP-3 | C18 amended; K5 | C18 VERIFIED (seed on, noupdate) | PC-D-17 | Convergent on the seed. The D11 inaccuracies are recorded under D1-11 and D1-34 |

## 4. Supersede map — net state of affected base REC IDs after D1

The base file is unchanged. This table records the net state to read alongside it.

| Base REC ID | Base class | Net class after D1 | What changes |
|---|---|---|---|
| REC-MAIL-09 (C09, G9) | UPP | UPP | No change (D1-06) |
| REC-MAIL-10 (C10, G8) | MATCH | MATCH | Reaffirmed. Plan rules confirmed as system 1=1 only (D1-08) |
| REC-MAIL-11 (C11, G8) | UPP | UPP | G8 narrowed. Author vector folded into REC-38 (D1-05, 09) |
| REC-MAIL-15 (C15) | UPP | UPP | Guest resolution known statically (D01, D02). Adds runtime PC-D-01 |
| REC-MAIL-18 (C18) | MATCH | MATCH (base wording) + delta CONTRADICTION on the D1 amendment (D1-11) | The base seed-on and editor-guard claim stands. The amendment is open for A3 because of D11 and K5 |
| REC-MAIL-21 (C21) | UPP | UPP | CRQ-07 linked to PC-D-06 (D1-19) |
| REC-MAIL-24 (C24) | UPP | UPP | K6 (comment says 0, seed is 3) noted |
| REC-MAIL-25 (C25) | MATCH | MATCH | Publisher job characterised (D05, D06 UPP) |
| REC-MAIL-28 (C28) | CONTRADICTION | CONTRADICTION | CF-2 resolved for base A2. D1 guest-context wording superseded |
| REC-MAIL-29 (C29) | CONTRADICTION | CONTRADICTION (base wording) + extension MATCH | CF-3. Net C29 statement in section 3 |
| REC-MAIL-31 (K1) | CONTRADICTION | CONTRADICTION | CF-1. D1 "unchanged" superseded |
| REC-MAIL-32 (K2) / REC-MAIL-33 (K3) | MATCH / MATCH | MATCH / MATCH | K3 net = 4 sites |
| REC-MAIL-34 (K4) | CONTRADICTION | CONTRADICTION | CF-1 |
| REC-MAIL-38 (O4, SF-05) | UPP | UPP | Absorbs D14 and CRQ-MAIL-18 (DUP-1) |
| REC-MAIL-50, 55, 56 (G1, G6, G7) | GAP | GAP | Unchanged |
| REC-MAIL-51 (G2) | GAP | **GAP (NARROWED)** | The composer and the other 6 wizards are characterised statically (D07–D13). Residual: N2, N3, the D11 contradiction and G12. D1 "CLOSED-STATIC" not adopted |
| REC-MAIL-52 (G3) | GAP | **MATCH (CLOSED-STATIC)** for the decorator and guest resolution | Residual per-route coverage is carried as D1-43 (N1, GAP) |
| REC-MAIL-53 (G4) | GAP | **MATCH (CLOSED-STATIC)** | Runtime effect carried by D1-28 and D1-29 (UPP) |
| REC-MAIL-54 (G5) | GAP | GAP (NARROWED) | Link preview and web push are studied |

Base net totals, read with this delta: MATCH 27, CONTRADICTION 6, UPP 18, GAP 5 (56 items). REC-52 and REC-53 moved from GAP to MATCH, and no other base class changed.

## 5. QID lineage update (lineage only; not answers)

Join key: MODULE `mail` + QID + freeze `558ec880…7177`. New delta mappings are in the tables above, and they add evidence to QIDs that were already mapped: Q001, 002, 003, 007, 014, 023, 024, 025, 031, 032, 037, 041, 044, 045, 048, 050.

"No evidence yet" list, updated from the base's 17:
- **Q038** (per-recipient render isolation in batch) **moves to mapped**. D08 and N2 describe batched, per-record preparation of mail values in mass-mail mode (REC-MAIL-D1-31, D1-44). Lineage only; the disconfirming observation is not tested.
- **Q039** (dynamic attachments per-recipient context) **stays unmapped**. D08 shows per-target company on mail values, but dynamic attachment generation was not traced, so the fit is not clear.
- **Q047** (cloned environment outbound) **stays unmapped**. The publisher egress (D05, D06) is instance telemetry, not delivery of customer messages.
- Remaining no-evidence: **16 QIDs**: Q012, Q013, Q015, Q016, Q019, Q020, Q026, Q028, Q029, Q034, Q039, Q040, Q042, Q046, Q047, Q049. Mapped: **34 QIDs**.

## 6. Handoff

- To: PROOF DELTA (Stage 2, same run), `G01_PROOF/G01_MAIL_PROOF_DELTA_D1_20260927.md`.
- Proof must cover PR-MD1..10 (runtime PC-MAIL-D-01..10) and the static basis for every delta CONTRADICTION, UPP and R-a item (PC-MAIL-D-11..23).
- The 9 delta CONTRADICTION items stay open for A3. The 4 GAP items are carried.
- Proof-design notes for A3: D05/D06 remote-message escaping has no case. N5 and G12 have no case. The base proof-design gaps (REC-36 and REC-45 without a runtime case) are unchanged.

## 7. Limitations

- REC used only the immutable inputs in 0.1, plus the hash-verified static results of Stage 2 for classification support (rules R-a and the conflict rule). No runtime evidence exists.
- Base-layer semantics (root identity and access checks, proxy cookie rewriting, network egress controls) and overrides from other modules or Enterprise are not traced.
- The QID mapping is topical lineage judged by this controller. It is not a coverage measure. No Formal Coverage claim is made, no percentages are used, and no git operations were run. No existing file was edited. A3 static work on `mail` was not consulted.
