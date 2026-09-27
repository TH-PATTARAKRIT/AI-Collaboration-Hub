# G01 PLATFORM_BASE — RED TEAM A3 Independent Challenge (STATIC scope) — `base_setup`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, independent adversarial challenger. This reviewer authored no upstream stage (Lane A, A1, A2, REC, PROOF) |
| Group / Module | G01 PLATFORM_BASE / `base_setup` |
| Date | 2026-09-27 |
| Scope | STATIC only. Runtime is **NOT-EXECUTED**: it has neither passed nor failed |
| Question bank | `GMVQ/G01_PLATFORM_BASE/G01_BASE_SETUP_GMVQ_MVQ_40_V1.00_DRAFT.md`, sha256 `2161184604279f38a59f8e56db288f53d4e706d4ec85cb5ba2a224e883a26d62`. This equals the `bank_files` entry in FREEZE_W1-B04. The bank holds **41** QIDs (Q001–Q041) with no duplicates, which matches the freeze QA record (`W1_B04_OVQDT_REVIEW_20260925.md`: "Governed module-specific floor PASS — 41 / 41 / 42 MVQ", with base_setup first) and the replay file (W1-B04 41/41/42, ELIGIBLE, floor delta) |
| Freeze | `FREEZE_W1-B04.json` sha256 `27db90332c140e569d4ab7f3a6d2fe7f5d0aae5f375065b5ab2ffe2d95f4d4f9` (equals the entry in `FREEZE_W1-B04.sha256.txt`). freeze_hash `9e31f2d27dfb959e555cf8ff117d829969e8122fe5e5544bbaf737b6ddea0377` |
| Join key | MODULE `base_setup` + QID + freeze hash above |
| Source anchor | `odoo/odoo@8d05257d83f9128953f580a066db67c48fcdb96f`. A3 fetched its own copies at 2026-09-27T15:17:48Z–15:17:51Z and checked each with `git hash-object` (see §2) |
| Intake hashes | `scratchpad/a3_asgn_bset/intake.sha256` (14 inputs, shared with the auth_signup A3 file) |
| **Disposition** | **A3 STATIC PASS WITH DEFECTS (route to PROOF; one lineage item to Integration Control)** |

### 0.1 Intake (sha256, recorded 2026-09-27 ~15:17 UTC; every value equals the one recorded in the REC/PROOF headers)

| Input | sha256 |
|---|---|
| Lane A `G01_LANE_A_PASS1/G01_BASE_SETUP_LANE_A_PASS1_20260927.md` | `59d3d312c3f5bff8dba13b24bb66a648f357b418677a9e74f242d0929f6ae4ce` |
| A1 `G01_A1_PACKAGES/G01_BASE_SETUP_A1_PACKAGE_20260927.md` | `3e37b467fb26899f96af1f44cc17db63a7855b3696ca96a72ab5e3f489a90970` |
| A2 `G01_A2_REVIEWS/G01_BASE_SETUP_A2_REVIEW_20260927.md` | `9e913ee76c3e1c34418a7e1d1ae93e4df1c65636abbd101849cc79cb3b651a31` |
| REC `G01_RECONCILIATION/G01_BASE_SETUP_REC_20260927.md` | `05e752c04a10c3a5fbf9d8977c8683b627110c0be3db6de925176f7ac0adb06a` |
| PROOF `G01_PROOF/G01_BASE_SETUP_PROOF_20260927.md` | `c9f0c353ca9cda7d40e840385d59dd64b72260a706d8926cba4a8e240e506faf` |
| Bank | `2161184604279f38a59f8e56db288f53d4e706d4ec85cb5ba2a224e883a26d62` |
| FREEZE_W1-B04.json | `27db90332c140e569d4ab7f3a6d2fe7f5d0aae5f375065b5ab2ffe2d95f4d4f9` |

Clean-room note: every statement below is a neutral WHAT/WHY/RISK paraphrase. File names and identifiers are evidence pointers only. No vendor code is reproduced, and nothing here recommends reusing vendor schema, ORM, workflow, UI or naming. There are no percentages and no Formal Coverage claim. Git use was read-only. Inputs were not edited.

## 1. Challenge log

| # | Challenge target | A3 attempt to disprove (static re-derivation; paraphrased, file lines) | Disposition |
|---|---|---|---|
| CH-01 | HIGH chain O1 / REC-BSET-24: bulk-invite reactivation restores groups and revives unexpired API keys without an invitation | **Refutation attempts:** (i) archiving might remove keys; (ii) reactivation might reset groups; (iii) an invitation might follow reactivation. **Result: none holds.** (i) Keys are removed only on self-service account deletion (core res_users L967) and by the expiry clean-up (L1715-1722). Archiving has no key hook, and the key check requires only that the owner is active, the key is unexpired, and its scope is unset or matches the requested scope (L1725-1750). (ii) The core user write on activation only unarchives the partner before the generic write (L596-606), and the group fields are untouched. (iii) The bulk invite reactivates matches with a plain write (base_setup res_users L20-24). auth_signup's re-invite search covers active users only and runs before that write, and the create-time invitation hook is not reached (auth_signup res_users L260-280) | **UPHELD**; runtime PC-BSET-24 required |
| CH-02 | HIGH chain O3 / REC-BSET-26: `/kpi/summary` checks the API key but no role; accepts no-scope keys; portal keys pass only when `portal.allow_api_keys` is on | **Chain upheld.** The route has no authentication and saves no session (kpi L149). The key is checked with the remote-call scope only (L102-105). That check accepts keys with no scope or with the remote-call scope, and rejects keys with any other scope. It has no share, internal or group term (core res_users L1736-1750). The response then lists the id, name, login and latest log date of every active non-share user (kpi L126-138). **"Portal keys only when the parameter is on" is disproved as stated.** That parameter governs only **creation** (base creation gate L1834-1836; portal override L11-20). Changing a user's groups does not remove keys: the core write (L596-640) has no key clean-up, and only deletion and expiry remove them. An internal user who creates a key and is later **demoted to portal (share)** keeps a key that still passes the KPI check with no parameter set. The same applies to keys generated by server code for any user (the generator accepts a null scope, L1591-1593). PROOF refinement R2 and the REC-BSET-26 basis sentence therefore narrow the HIGH finding more than the source supports | **UPHELD (chain)**; **CHALLENGE-SUSTAINED against the PROOF R2 narrowing (PROOF)**: withdraw or correct R2, and add a runtime variant to PC-BSET-18: an internal user creates a key, is demoted to portal, and calls the KPI summary with `portal.allow_api_keys` unset. Expected per static reading: roster returned |
| CH-03 | CONTRADICTION C11 / X-BSET-01: non-admins get an access error on the demo-status route | The route requires an authenticated user, has no group check and no elevation (main L53-59). It counts module-registry records through `search_count` → `_search`, which checks model read access for non-superusers (models L1360-1372 → L5364-5366). The only ACL row for the module registry in core grants system administrators full rights (core ACL L25). A non-administrator therefore gets an access error, and A1's claim that "any logged-in user learns demo state" is refuted at source for core plus base_setup. An additional module ACL could widen this, which remains a runtime or configuration matter | **UPHELD**; PC-BSET-22 required |
| CH-04 | X-BSET-02 resolved (C12 as MATCH) | The settings counter is an elevated ORM count of non-share users (settings L104-108). Default archive filtering applies whatever the elevation, unless the context disables it (models L5368-5375). **Caveat found:** the settings save path itself runs with archive filtering disabled (res_config L302 set_values, L370 execute). If the counter were recomputed in that context, it would include archived users. On the normal display path (form load) the context keeps the default filter, so the resolution holds for what the administrator sees | **UPHELD** with caveat. Recommend PROOF keep PC-BSET-23 as a required confirmatory case (form load and immediately after save), not an optional one |
| CH-05 | CONTRADICTIONs C03, C06, C10, C17 | Re-read of the settings pass-throughs (only the footer is writable), the bulk-invite link attribution (the context flag is inert; the link comes from the auth_signup create hook), the pending-user basis (log rows on both sides), and provider discovery (every manifest on the path). The A2 side is confirmed in each | **UPHELD** |
| CH-06 | Predeclaration timing | This uses the shared predeclaration file: mtime 15:04:44.22Z, sha256 `97055575…ec01f` matches. The earliest fetch is at 15:04:53.45Z, so the stamp precedes it. The header's "15:04:59" is the end of the batch. **Note:** the follow-up reads of the portal module (15:05:59Z–15:06:00Z) and of core field definitions (15:07:27Z) were not listed as preconditions in the predeclared PC-BSET-07 and PC-BSET-03 rows. The PC-BSET-03 PASS (layout and name read-only) depends on the core read-only default for related fields, which came from that later read. This extends the evidence without changing the expectation, so it is acceptable, but it should be recorded as a post-predeclaration addition | **UPHELD** (note) |
| CH-07 | Re-execution of static PASS cases (5 re-run) | PC-BSET-05 (base_setup res_users L14, L16-17, L20-24, L27-35): **PASS confirmed.** PC-BSET-06 (CH-01): **PASS confirmed.** PC-BSET-07 (CH-02): the source readings are confirmed and the **PASS stands on its predeclared expected/fail pair**; only refinement R2 overclaims. PC-BSET-10 (CH-03): **PASS confirmed.** PC-BSET-12 (CH-04): **PASS confirmed**. **Weak condition:** its fail condition ("raw count bypassing active filter") does not consider a context with archive filtering disabled | **UPHELD** (weakness recorded in CH-04) |
| CH-08 | Items with no runtime case | For base_setup, every UNKNOWN_PENDING_PROOF item has a runtime case (PC-18..28). The only new requirement comes from CH-02 (demoted-user key variant). The shared auth_signup items (clone signing key O4, link builder C18) are routed in the auth_signup A3 file | See CH-02 |
| CH-09 | Overclaim / Lane B misuse | No percentages. "Formal Coverage" appears only in denials. No Lane B material is used, and A3 found no Lane B, Gemini or evidence-pool file in the repository. No runtime result is claimed. Overclaim found: PROOF R2 (CH-02) | Covered by CH-02 |
| CH-10 | QID mapping fit (4 sampled) | Q011 (reactivation does not restore stale privileges blindly) ↔ REC-06/07/24/25: exact fit. Q018 (endpoint authorisation equals the visible settings interface) ↔ REC-09/11/30: good fit. Q033 (telemetry accepts only remote-call-scoped credentials) ↔ REC-15/26: good fit, and CH-02 adds the demoted-owner dimension. Q022 (environment/demo indicators) ↔ REC-11: partial fit, covering who can read the indicator but not whether it prevents actions in the wrong environment. Q003 (save does not reset unrelated settings) has no evidence under the MODULE join key. A3 checked this: the only parameter-bound fields base_setup declares are one boolean and one date-time with no declared default, so the absent-row mechanism does not reset them. The REC note that the auth_signup finding is adjacent but not mapped is correct under MODULE + QID | **UPHELD** |
| CH-11 | Clean-room scan (REC + PROOF) | No code blocks and no copied statements. The pattern scan returned no matches. Identifiers appear as evidence pointers only | **UPHELD** |

## 2. Lineage

**A3 blob verification** (fetched from the anchor; `git hash-object`). Every blob matches PROOF §2:
`ba102d65` base_setup res_users · `69c9c21c` kpi controller · `cce2c3f7` main controller · `7de29781` settings · `50464416` core res_config · `9d42d77a` core res_users · `29785e02` core ACL · `11f50c4e` core models · `44c0008f` portal key-description · `1a0280b8` auth_signup res_users. Log: `scratchpad/a3_asgn_bset/blobs.txt`.

**Git lineage** (read-only `git log --oneline --follow`). All inputs are clean in the working tree:

| Artifact | Commit(s) |
|---|---|
| Lane A | `7fab4ed` (names base_setup) |
| A1 | `07cca3c` (names base_setup) |
| A2 | `0aad8c0` "A2 G01: base_sparse_field, google_recaptcha reviews". **The commit message does not name base_setup** |
| REC | `811e8ae` "REC/Proof G01: base_sparse_field, google_recaptcha" (15:12:19Z). **The commit message does not name base_setup** |
| PROOF | **Two commits:** `b31a0e8` checkpoint (15:15:22Z), then `37823e6` "REC/Proof G01: web …, privacy_lookup" (15:16:10Z) |
| Bank | `59f30db` |
| FREEZE_W1-B04 | `87c69f4` |

**Silent revision:** between `b31a0e8` and `37823e6`, one line of the PROOF file changed. In PC-BSET-05, the reference for the e-mail normalisation step moved from L13 to L14. The document carries no revision note. The correction is accurate, since the anchored blob has normalisation at L14, and no verdict changed. It is still an unrecorded post-commit edit, made in a commit labelled for other modules. The sha256 of the first committed version is `c48e3273…e047`; the current file is `c9f0c353…afaf`.

## 3. Defects routed

| ID | Defect | Owner stage | Blocking for MASTER? |
|---|---|---|---|
| D-BSET-A3-01 | PROOF R2 and the REC-BSET-26 basis understate the HIGH KPI finding: keys survive demotion to portal, so the portal-key path does not depend on the parameter (CH-02) | PROOF (REC to amend its basis wording; A2 informed) | Yes: the HIGH finding must not be presented as narrowed |
| D-BSET-A3-02 | PC-BSET-18 lacks the demoted-owner variant (CH-02) | PROOF | Yes for Q019/Q027/Q033 runtime closure |
| D-BSET-A3-03 | PC-BSET-23 is marked optional, and PC-BSET-12's fail condition ignores the save-path context (CH-04) | PROOF | No (recommended) |
| D-BSET-A3-04 | Post-predeclaration evidence (portal, core fields) was not flagged as an addition (CH-06) | PROOF | No |
| D-BSET-A3-05 | The PROOF file was silently revised after commit, and the A2/REC/PROOF commits are labelled for other modules (§2) | Integration Control | No (record a change note) |

## 4. Runtime-blocked items

All runtime cases PC-BSET-18..28 are **NOT-EXECUTED** because runtime device THPATTARAKRIT-SOLUTION-SERVICE-2.local is offline. Priority for MASTER readiness:
- PC-BSET-18/19 (KPI roster exposure and key classes, plus the new demoted-owner variant)
- PC-BSET-24 (reactivation revives groups and keys with no invitation)
- PC-BSET-22 (demo-status denial)
- PC-BSET-20/21 (existence disclosure, database-filter reach)
- PC-BSET-26 (provider durability, uninstalled-provider execution)
- PC-BSET-23 (counter basis, recommended as required)
- PC-BSET-25, 27, 28

All 12 UNKNOWN_PENDING_PROOF items and the runtime effect of C03, C11 and C17 stay open. A full A3 → MASTER handoff is **not** eligible. This is a static-scope disposition only: `MASTER HANDOFF PENDING RUNTIME`.

## 5. Limitations

- Static only. No runtime executed and no runtime result claimed.
- Not read: the core HTTP cursor binding (G2), the settings install and implied-group machinery beyond save (G3), static JS (G5), where profiling expiry is enforced (G7), and the server database-filter layer.
- Other installed modules may widen the module-registry ACL or add archive, demotion or key hooks that would change CH-01, CH-02 or CH-03.
- Predeclaration timestamps are filesystem mtimes written by the same environment.
- freeze_hash was taken from the freeze record and its sidecar; A3 did not recompute it.
- No percentages. No Formal Coverage claim. Git use was read-only. Inputs were not edited.
