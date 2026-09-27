# G01 PLATFORM_BASE — RED TEAM A3 Independent Challenge (STATIC scope) — `auth_signup`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, independent adversarial challenger. This reviewer authored no upstream stage (Lane A, A1, A2, REC, PROOF) |
| Group / Module | G01 PLATFORM_BASE / `auth_signup` |
| Date | 2026-09-27 |
| Scope | STATIC only. Runtime is **NOT-EXECUTED**: it has neither passed nor failed |
| Question bank | `GMVQ/G01_PLATFORM_BASE/G01_AUTH_SIGNUP_GMVQ_MVQ_40_V1.00_DRAFT.md`, sha256 `bf215a348a6efdb3fe0a171589fa9705832655a5f00c44f0b54c49c4cfade9e2`. This equals the `bank_files` entry in FREEZE_W1-B02. It holds 40 QIDs with no duplicates, which matches the freeze QA record ("PASS — 40 MVQ") |
| Freeze | `FREEZE_W1-B02.json` sha256 `bccaa2e1a0006429ff60ce7c9790862ea2e49d589da5d9a7919923b7cd504a2b`; freeze_hash `cd966040f720456420057fe98fdb1176fbb9b0e85b456891f4dab82ea3ba0202`. The replay file marks it ELIGIBLE |
| Join key | MODULE `auth_signup` + QID + freeze hash above |
| Source anchor | `odoo/odoo@8d05257d83f9128953f580a066db67c48fcdb96f`. A3 fetched its own copies at 2026-09-27T15:17:48Z–15:17:51Z, with follow-ups for the clone test. Each copy was checked with `git hash-object` (see §2) |
| Intake hashes | `scratchpad/a3_asgn_bset/intake.sha256` holds 14 inputs. The hash of that file is `cd3d6932…e59b` |
| **Disposition** | **A3 STATIC PASS WITH DEFECTS (route to PROOF, with A2 authoring the new proof requirements; minor items to REC and Integration Control)** |

### 0.1 Intake (sha256, recorded 2026-09-27 ~15:17 UTC; every value equals the one recorded in the REC/PROOF headers)

| Input | sha256 |
|---|---|
| Lane A `G01_LANE_A_PASS1/G01_AUTH_SIGNUP_LANE_A_PASS1_20260927.md` | `9470d090c3ed164634954ae0cb0cfe0d5ae92fb981d51a0a4fc3ccaa4addfa54` |
| A1 `G01_A1_PACKAGES/G01_AUTH_SIGNUP_A1_PACKAGE_20260927.md` | `da32ca500989cf1befc9d48dc689c6ad6ee447705f1054e50226ee93ac0fe69e` |
| A2 `G01_A2_REVIEWS/G01_AUTH_SIGNUP_A2_REVIEW_20260927.md` | `e5ce1b56ab35903665d02b3c58d184e2ba334ba72e8d09578ae0ff07f5dd28f9` |
| REC `G01_RECONCILIATION/G01_AUTH_SIGNUP_REC_20260927.md` | `18d7b4ef959f9de14f5e4d14112eefd925a7808239117712a9f759dba25dd4f6` |
| PROOF `G01_PROOF/G01_AUTH_SIGNUP_PROOF_20260927.md` | `deee3cf05169f7073ade39593a98b3b62d1899c912fa33a57b4bdb90504d0caf` |
| Bank | `bf215a348a6efdb3fe0a171589fa9705832655a5f00c44f0b54c49c4cfade9e2` |
| FREEZE_W1-B02.json | `bccaa2e1a0006429ff60ce7c9790862ea2e49d589da5d9a7919923b7cd504a2b` |

Clean-room note: every statement below is a neutral WHAT/WHY/RISK paraphrase. File names and identifiers are evidence pointers only. No vendor code is reproduced, and nothing here recommends reusing vendor schema, ORM, workflow, UI or naming. There are no percentages and no Formal Coverage claim. Git use was read-only. Inputs were not edited.

## 1. Challenge log

| # | Challenge target | A3 attempt to disprove (static re-derivation; paraphrased, file lines) | Disposition |
|---|---|---|---|
| CH-01 | HIGH chain O1 / REC-ASGN-25: when the invitation-scope row is missing, an unrelated General Settings save writes "free sign-up" and opens public registration | **Refutation attempt:** the web client might send only the fields the user changed, so the scope value would never reach the server. **Result: refuted by source.** The ORM create path fills every field missing from the payload through default values (models L4802 → L1559-1592). The settings default-value routine reads each parameter-bound field from the stored parameter and falls back to the field's declared default when the row is absent (res_config L264-268). The declared default is free sign-up (module settings L13-20). On save, the routine compares the form value with the raw stored value, which is false when the row is absent, and writes the value when they differ (res_config L330-347, after the administrator check at L351-370). The enforcement reader falls back to invitation-only (module res_users L88-89). The public sign-up page is enabled only when the scope equals free sign-up (controller L43, L132). The chain therefore holds whether or not the client sends only changed fields, which settles PROOF §6 item 3 statically. **Severity note:** the precondition is a non-default state. The install seed already writes free sign-up (data L3-7), so on a default install public registration is already open. The HIGH exposure applies where an operator removed the row, or migrated or restored without it, and believes the invitation-only fallback is in force | **UPHELD (strengthened)**; runtime PC-ASGN-22 still required |
| CH-02 | HIGH chain (b), the KPI key check | This belongs to MODULE `base_setup`. See the base_setup A3 file, CH-02 | N/A here |
| CH-03 | HIGH chain (c) / O8 (REC-ASGN-31): users reactivated by the bulk invite get no invitation | The bulk invite in this module searches still-Invited users with the default active-only filter. It removes their e-mails, delegates the rest to base_setup, and then re-invites only the users it found (module res_users L260-267). base_setup reactivates archived matches with a plain write (base_setup res_users L20-24), and a write does not reach the create-time invitation hook (L269-280). No alternative path sends an invitation to a reactivated user | **UPHELD** (runtime shared with PC-BSET-24) |
| CH-04 | CONTRADICTION C09 / X-ASGN-02 "paper-only" | The core login date is a writable related projection of the newest log row (base res_users L231-233, log order newest first L133-135). The module's status compute uses the login date, and its search uses log-row existence (module L25-35), so both rest on the same basis. A direct write to the login date on a user with no log rows changes nothing, so the two cannot diverge that way. The only residual path is rewriting the newest row's timestamp, which cannot flip the existence test | **UPHELD** (paper-only). No proof requirement is needed; see CH-07 |
| CH-05 | CONTRADICTIONs C08, C19 and C03 (source vs declared intent) | Re-read with the A3 blob copies. The A2 side is confirmed in each case, and the REC treatment of C03 as a source-internal CONTRADICTION is sound because the declared default and the enforcement fallback differ (CH-01) | **UPHELD** |
| CH-06 | O4 / REC-ASGN-28 (link-signing key reuse in cloned environments; Q032, Q036). No runtime case exists | Links are HMAC-signed with the per-database secret (misc L1782-1795). **New static reads:** the platform's database-duplicate operation and its restore-as-copy operation both force the default parameters to regenerate, including the secret (db service L206-208, L380-382 → config-parameter init L45-57). A restore that is not flagged as a copy, or any clone made outside the platform (a raw database dump), keeps the secret, so links issued in one copy verify in the other. The REC/A2 statement "a clone keeping the secret would accept links" is correct but does not say which clone paths keep the secret. The QIDs mapped to it (Q032, Q036) need a runtime answer | **CHALLENGE-SUSTAINED (PROOF; A2 to author the proof requirement)**: add a runtime case with three variants: platform duplicate, restore not flagged as copy, and external dump clone. In each, replay a link issued before cloning |
| CH-07 | C09 has no runtime case | The residual path in CH-04 cannot change the status outcome. A runtime case would test nothing that is at risk | **UPHELD** (no requirement needed) |
| CH-08 | C18 / REC-ASGN-18 (link issuance authority; Q009). No runtime case exists | A2's correction stands: the multi-partner builder has no rights check (res_partner L38-85). **A3 finds a further gap on the single-partner entry as well:** the write-rights check runs only when the partner already has another internal or portal user (L29-36). For a partner with **no users** there is no check at all. With the "signup valid" context the builder prepares a sign-up type and signs a token with elevated rights (L46-47, L55-58). That token takes the invited path, which the free sign-up gate does not apply to (module res_users L96-98). The builders are private (underscore) methods and cannot be called over RPC, so exposure depends entirely on server-side callers in other modules (portal sharing and invite flows, mail notification links). None of those callers were read. PC-ASGN-14's fail condition ("check on both") cannot detect this gap | **CHALLENGE-SUSTAINED (PROOF; A2 to author the proof requirement)**: (1) a static enumeration of cross-module callers of both builders at the anchor; (2) a runtime case in which a non-manager internal user triggers each reachable flow for a partner that has no user and for one owned by another user, and records whether a usable sign-up link is issued |
| CH-09 | Predeclaration timing (15:04:44Z stamp before the 15:04:59Z fetch) | The predeclared file's mtime is 15:04:44.22Z and its sha256 `97055575…ec01f` matches the header. The earliest fetched source file's mtime is **15:04:53.45Z** (manifest), and the batch ends at 15:04:59.98Z. The stamp precedes the first fetch. The header's "fetched 15:04:59" is the end of the batch, not its start, which is an imprecision only. Timestamps are self-attested filesystem mtimes. Predeclaration shows only that expectations were not written after this run's fetch; they were derived from A2, which had already read the source | **UPHELD** (precision note) |
| CH-10 | Re-execution of static PASS cases (5 re-run) | PC-ASGN-01 (getter L88-89, default L13-20, seed L3-7, gate L96-98): **PASS confirmed.** PC-ASGN-02 (L264-268, L330-347): **PASS confirmed**, and CH-01 adds the create-fill path. PC-ASGN-04 (zero validity gives a zero expiry stamp, which the verifier accepts as never expiring; misc L1828-1833, L1860; defaults 4/144 h at res_partner L184-188): **PASS confirmed.** PC-ASGN-11 (CH-04): **PASS confirmed.** PC-ASGN-19 (CH-03): **PASS confirmed.** The line references in the PROOF rows match the anchored blobs | **UPHELD** |
| CH-11 | Weak conditions | PC-ASGN-02's fail condition did not cover the path where the client sends only changed fields; CH-01 now covers it, so no defect remains. PC-ASGN-14's fail condition cannot detect unchecked reachability (CH-08). PC-ASGN-15 ("no throttling in module") is sound as a negative, but it cannot rule out enforcement in another layer, which is correctly deferred to PC-31 | Weakness recorded under CH-08 |
| CH-12 | REC stage separation | Both REC files state that classification used "the static proof results from Stage 2", and the "Basis for class" column cites PC-xx PASS. This mixes stages: REC classification should rest on A1/A2 plus its own re-read, and should not rely on downstream Proof verdicts. It changes no class, because A3's own re-read reproduces every basis cited | **CHALLENGE-SUSTAINED (REC; low, non-blocking)**: record the basis as REC re-read rather than Proof outcome, or state the dependency explicitly |
| CH-13 | Overclaim / Lane B misuse | No percentages. "Formal Coverage" appears only in denials. No Lane B material is used. A3's search found no `*lane_b*`, `*gemini*` or `*evidence_pool*` file in the repository, so all Lane B cells are UNCORROBORATED or NOT_APPLICABLE, and none is counted as FAIL. No runtime result is claimed. Proof R1–R4 are correctly marked as not changing verdicts | **UPHELD** |
| CH-14 | QID mapping fit (4 sampled) | Q006 (disabled self-registration has no alternate path) ↔ REC-02/03/25: good fit. Q012 (enrollment and recovery credentials not substitutable) ↔ REC-07: exact fit. Q032 (clone cannot send usable invitations toward production) ↔ REC-28: partial fit; the secret dimension is covered, but base-URL targeting is not evidenced. Q018 (verification status changes auditable and attributable) ↔ REC-09: **weak fit**. C09 concerns the status computation basis, not auditability or attribution of the change event. No mapping is presented as an answer | **UPHELD** with note: Q018 should carry "topical only, no audit evidence" |
| CH-15 | Clean-room scan (REC + PROOF) | No code blocks and no copied statements. Pattern scan for definitions, imports, SQL and ORM calls returned no matches. Identifiers such as the query parameter names and config keys appear as evidence pointers only | **UPHELD** |

## 2. Lineage

**A3 blob verification** (fetched from the anchor; `git hash-object`). Every blob matches PROOF §2:
`1a0280b8` module res_users · `f72a458d` module settings · `02aab000` res_partner · `96d8b71f` controller · `df7690a0` parameter data · `ba102d65` base_setup res_users · `50464416` core res_config · `9d42d77a` core res_users · `11f50c4e` core models · `6d275059` core misc (re-hashed from the REC scratch copy).
New A3 reads recorded (no prior value to compare): `odoo/service/db.py` `63c314a72de738d044e542e32bc045c21f987531`; `odoo/addons/base/models/ir_config_parameter.py` `21c82bf62ed0fec4b4307c935f8a2b4ebaff4321`. Log: `scratchpad/a3_asgn_bset/blobs.txt`.

**Git lineage** (read-only `git log --oneline --follow`). All inputs are clean in the working tree, so HEAD equals the working copy:

| Artifact | Commit(s) |
|---|---|
| Lane A | `7fab4ed` Lane A G01 PASS-1 (names auth_signup) |
| A1 | `07cca3c` A1 packages (names auth_signup) |
| A2 | `919fada` "A2 G01: portal, utm reviews" (15:00:33Z). **The commit message does not name auth_signup** |
| REC | `95f51c5` "in-flight REC/Proof/A3 artifacts checkpoint" (15:10:47Z) |
| PROOF | `61d6288` "A2 G01: web and mail delta D1 reviews" (15:13:51Z). **The commit message does not name auth_signup** |
| Bank / FREEZE_W1-B02 | `b0f6dfd` (single commit each; bank hash equals the freeze entry) |

Ordering is consistent: A2 was committed before the REC intake (~15:03Z), which came before the predeclaration (15:04:44Z), the fetch (15:04:53Z) and the REC/PROOF commits. Each file has a single commit, so there are no silent revisions. Commit messages do not identify this module for A2 and PROOF, which is a traceability defect (see §3).

## 3. Defects routed

| ID | Defect | Owner stage | Blocking for MASTER? |
|---|---|---|---|
| D-ASGN-A3-01 | O4 has no proof requirement, and its wording does not say which clone paths keep the signing secret (CH-06) | PROOF (A2 authors the proof requirement) | Yes for Q032/Q036 lineage; not for other items |
| D-ASGN-A3-02 | C18 has no proof requirement. Userless partners get no rights check on single-partner entry, and cross-module callers were not enumerated (CH-08) | PROOF (A2 authors the proof requirement; static caller trace first) | Yes for Q009 lineage |
| D-ASGN-A3-03 | REC classification basis relies on Stage-2 Proof outcomes (CH-12) | REC | No |
| D-ASGN-A3-04 | The A2 and PROOF artifacts rode in commits whose messages name other modules (§2) | Integration Control | No |
| D-ASGN-A3-05 | The Q018 mapping is a weak topical fit (CH-14) | REC | No |

## 4. Runtime-blocked items

All runtime cases PC-ASGN-22..33 are **NOT-EXECUTED** because runtime device THPATTARAKRIT-SOLUTION-SERVICE-2.local is offline. Priority for MASTER readiness:
- PC-ASGN-22 (O1 settings-save exposure; CH-01 strengthens the static basis)
- PC-ASGN-26 / 28 (link replay, re-issue, zero validity)
- PC-ASGN-27 (cross-route substitution)
- PC-ASGN-24 / 25 (anonymous enumeration)
- PC-ASGN-30 (session-token fallback)
- PC-ASGN-33 (mail-failure state)
- PC-BSET-24 (shared reactivation case)

New runtime cases requested: the O4 clone variants (D-01) and the C18 reachability case (D-02).

All 17 UNKNOWN_PENDING_PROOF items and the practical effect of C03, C08 and C19 stay open until runtime runs. A full A3 → MASTER handoff is **not** eligible. This is a static-scope disposition only: `MASTER HANDOFF PENDING RUNTIME`.

## 5. Limitations

- Static only. No runtime executed and no runtime result claimed.
- Web-client JS was not read. CH-01 does not need it because the server fills missing fields itself.
- Captcha providers, CSRF defaults, session rotation and redirect sanitisation were not read (REC-34..36 remain GAP).
- Cross-module callers of the link builders were not read (D-02).
- Other installed modules may override any method cited here.
- Timestamps used for the predeclaration check are filesystem mtimes written by the same environment.
- freeze_hash was taken from the freeze record and its sidecar; A3 did not recompute it.
- No percentages. No Formal Coverage claim. Git use was read-only. Inputs were not edited.
