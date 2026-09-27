# G01 PLATFORM_BASE — RED TEAM A3 Independent Challenge (STATIC scope) — `portal`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, the independent adversarial challenger |
| Independence statement | This A3 reviewer did not author Lane A, A1, A2, REC or PROOF for `portal` or `utm`. The goal was to disprove the upstream conclusions, not to confirm them. No upstream artifact was edited. A3 re-fetched the source and re-read it on its own terms instead of trusting upstream paraphrase |
| Group / Module | G01 PLATFORM_BASE / `portal` |
| Date | 2026-09-27. Intake hash 15:14 UTC. First A3 source fetch 15:15:02Z. Exit re-hash at the end of the run |
| Scope | STATIC only. Runtime cases PC-PRTL-14..22 are **NOT-EXECUTED** because the runtime device is offline. They are neither passed nor failed |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`. A3 re-fetched the files into scratchpad `a3_prtl_utm/src/`. `git hash-object` equals the Lane A/Proof blob for: `controllers/portal.py` e6b03c24, `models/portal_mixin.py` d24085d8, `models/mail_thread.py` 971d3f79, `wizard/portal_wizard.py` 368f4c1d, `wizard/portal_share.py` b0491d4e, `utils.py` b83ac0a1 and `controllers/mail.py` aef21b45. There is one extra cross-module blob that A3 used as context only: `addons/sale/controllers/portal.py` 181e72142b45849d356c98a877e4a03165617b0f |
| **Overall disposition** | **A3 STATIC PASS WITH DEFECTS (route to PROOF; Integration Control)**. There is no static FAIL of a verdict that the handoff relies on. MASTER handoff also remains **pending runtime** |

### 0.1 Lineage hashes (sha256), intake and exit

Paths are relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`. The intake list is saved at scratchpad `a3_prtl_utm/intake.sha256`.

| Input | sha256 at intake | sha256 at exit | Git lineage (read-only `git log --oneline --follow`) |
|---|---|---|---|
| Lane A `G01_LANE_A_PASS1/G01_PORTAL_LANE_A_PASS1_20260927.md` | `af066bfb151f94842d6dc6f9295cd47be5d8b31f1ee6434a530b254e60ae826f` | identical | 1 commit `d7eb909`, 14:49:20Z. Working tree clean |
| A1 `G01_A1_PACKAGES/G01_PORTAL_A1_PACKAGE_20260927.md` | `aef3388923e91d7bd8659b6a7a3ab6da21898500decb9b891f8bb807c6ed957d` | identical | 1 commit `07cca3c`, 14:51:32Z. Clean |
| A2 `G01_A2_REVIEWS/G01_PORTAL_A2_REVIEW_20260927.md` | `695171c76157d86ee7cd290c2caab1c8f331f54eb451e5b207272bc65bd26ec0` | identical | 1 commit `42e6a0c`, 14:58:46Z, **message "A1 G01: base package"** (mislabelled, see D-PRTL-A3-03). Clean |
| REC `G01_RECONCILIATION/G01_PORTAL_REC_20260927.md` | `abb7e72d2af65878915c93d64529f89f996500726986861b51836af90f7c9d84` | identical | 1 commit `6302d8f`, 15:10:22Z, **message "REC/Proof G01: resource, resource_mail"** (mislabelled). Clean |
| PROOF `G01_PROOF/G01_PORTAL_PROOF_20260927.md` | `09190a38d42cd41631374925c12449a549d3c1450525218619da05bcb8dbd49a` | identical | 1 commit `811e8ae`, 15:12:19Z, **message "REC/Proof G01: base_sparse_field, google_recaptcha"** (mislabelled). Clean |
| Bank `../GMVQ/G01_PLATFORM_BASE/G01_PORTAL_GMVQ_MVQ_40_V1.00_DRAFT.md` | `91b63eef1df5426f22d4bc0b296dc05cb4b3e9e1d7e1b09e38370c5d03963d3a` | identical | Commit `b0f6dfd`. **Equals the FREEZE_W1-B03 `bank_files` entry** |
| Freeze `../GMVQ/G01_PLATFORM_BASE/FREEZE_W1-B03.json` | `74ba2caeaf9a4450ff126256df5e1a7b8bdd4018b2907248b9ccec0e5bbb565e` | identical | freeze_hash `1247c218…d3a5d3`, **recomputed by A3 and identical** (batch, sorted modules, sorted file:sha256) |
| Proof predeclaration (scratch) `rec_prtl_utm/PROOF_CASES_PREDECLARED.md` | `5438a46fdaecedaa6af02125ef605d673aff390095a04033b7209c4d75cb14e9` (equals the Proof header) | — | Not committed. mtime 15:02:39.9Z |
| A2 test plan (scratch) `a2_prtl_utm/test_plan_predeclared.txt` | `38a1b67a0ede45182ea96ae7bad67356873fd6a04464528b84b2640ff3d68065` (equals the A2 header) | — | Not committed. mtime 14:56:31Z |

Stage chronology from commit times: Lane A 14:49, then A1 14:51, A2 14:58, REC 15:10 and Proof 15:12. The order is consistent, and no file has more than one commit, so nothing was rewritten.

Clean-room note: every statement below is a neutral paraphrase. Identifiers and line numbers are evidence pointers only. No vendor code is reproduced or recommended. No percentages. No Formal Coverage claim. Git use was read-only. Inputs were not edited.

## 1. Challenge log

| # | Challenge | A3 independent evidence (paraphrased; pointer @ blob) | Disposition |
|---|---|---|---|
| CH-P1 | **PC-PRTL-01 FAIL.** Does the ensure-token helper really have 5 invocations in 4 functions rather than A2's 3? | A3 grepped every invocation in module Python and found exactly five: the share-URL builder (`portal_mixin.py` l.65), the portal-URL builder (l.134), customer-notification grouping (`mail_thread.py` l.35, elevated), and the **records-pager helper** called twice, for the previous record (`controllers/portal.py` l.104) and the next record (l.111). That is 5 invocations in 4 functions. The helper itself writes a random UUID elevated, only when the token is empty (l.34–39). The predeclared fail condition was "call-site count differs", so the FAIL follows the predeclared rule. | **UPHELD.** The FAIL applies to **A2's refinement** ("three minting call sites"), not to the C01 core. A2's VERIFIED verdict on C01 stands. Lane A also missed the pager site: it lists a pager template (Lane A l.124) but no minting. Root origin is Lane A, and A2 carried it forward |
| CH-P2 | **Is "no read check" on the pager accurate, and does it fit the exposure framing in Proof R1?** | (a) The pager has no explicit read check. It browses the neighbour ids from the environment of the record it is given. Its only in-module caller, the page-values builder (`controllers/portal.py` l.982–1017), passes the gate's result, which is superuser-bound (l.961–980). So the neighbours are superuser-bound as well, and **even implicit ORM read enforcement is bypassed**. That makes this site stronger than A2's two O2 sites, which run in the caller environment. (b) However, the id list comes from **server-side session state**, not from client input. Downstream list routes fill it from the caller's own search results, and those routes require login (verified in the `sale` portal controller @ 181e7214, l.106–115). The pager only runs when the current document id is in that list. | **CHALLENGE-SUSTAINED (PROOF), LOW-MED.** "No read check" is accurate and understated: the pager bypasses implicit enforcement too. But R1's framing overstates reach. A token-only, not-logged-in visitor **cannot craft** a session history. The realistic exposure is **stale history**: the neighbour ids were readable when the list was built, and access was lost later in the same logged-in session. The PC-PRTL-17 R1 extension ("crafted or previous session history") cannot be run as written. Suggested rewrite: log in as a portal user, open a list route, remove that user's access to a neighbour record, open the current record, and check whether a neighbour token link renders and whether a token was minted |
| CH-P3 | **Re-derive REC-09/18 (C09 + S1/S2): do a revoked user's document links and chatter identity still work?** | The gate (l.961–980) takes only the model, id and supplied token. It checks existence under the superuser, tries the caller's read check, and falls back to a constant-time token compare. It never reads user, partner, active, company or document state. Revoke (`portal_wizard.py` l.167–187) syncs email, clears the partner signup type elevated and archives a portal user. It touches no document token. The chatter hash is an HMAC over (db name, token field value, pid) keyed by the database secret (`mail_thread.py` l.65–82). The validators (`utils.py` l.10–17) compare the supplied hash or token to the recomputed value in constant time and take no account state. | **UPHELD** (static). The runtime effect (PC-PRTL-14) is still pending |
| CH-P4 | **Re-derive REC-19 (re-grant reactivates the archived user).** Could the email-uniqueness precondition block re-grant, because the archived user has the same login? | The linked-user compute reads the partner's users with the active filter off and takes the first (l.111–114). The group compute marks an archived portal user as neither portal nor internal (l.117–131), so grant is allowed. The uniqueness test looks up users with the same login including archived ones, but **excludes the partner's own linked user id** (l.262–266). Re-grant is therefore not blocked. Grant writes active=true, adds portal and removes public (l.159). | **UPHELD.** Nuance: when a partner has several users, "first" follows default ordering. That is a runtime detail for PC-PRTL-19 |
| CH-P5 | **Re-derive REC-20 / O1 (the share wizard mints the token on open).** | The wizard's default-values step (`portal_share.py` l.11–18) and the share-link compute (l.41–48) both call the share-URL builder, which runs a read check and then ensures the token. Minting happens only for models that have a token field (`portal_mixin.py` l.63–65). Send picks the public path when a token exists or B2C is off (l.98–108). | **UPHELD**, with a scope nuance. A2 limits O1 to "portal documents", and that is correct: for models without a token field the signup branch stays reachable. The minting user is the wizard opener, who must hold wizard ACL and read access on the record |
| CH-P6 | **Re-execute static PASS cases** (PC-02, PC-04, PC-08, PC-09, PC-11) | PC-02: the only write of the token field is the ensure helper (l.38), and the field is not-copied (l.16). PC-04: see CH-P3. PC-08: see CH-P3. PC-09: see CH-P4. PC-11: see CH-P5. | **UPHELD** (5 of 5 re-executed) |
| CH-P7 | **Weak or unfalsifiable conditions** | PC-PRTL-18 (PR-P5) is "record-only": its fail condition records an outcome and cannot falsify the claim. PC-PRTL-10 and PC-PRTL-13 are falsifiable. PC-PRTL-01's expected result embedded A2's count, and it falsified correctly, which shows the predeclaration worked. A3 also observed something upstream did not record: the token field's custom search accepts only the `in`/`not in` operators (`portal_mixin.py` l.21–24), which blocks pattern search on tokens. This bears on Q002 and supports C04. | **CHALLENGE-SUSTAINED (A2 authoring of PR-P5 / PROOF restatement), LOW.** PC-PRTL-18 should state a falsifiable outcome, for example "an archived document opens by token". The search-operator observation is informational |
| CH-P8 | **Predeclaration timing** (15:02:42Z predeclared vs 15:02:59Z first fetch) | Scratch evidence: the predeclaration file mtime is 15:02:39.9Z. `predeclared_time.txt` says 15:02:42Z. The recorded hash equals the current file hash. `exec_start.txt` says 15:02:59Z, and the earliest Proof source file has mtime 15:02:59.67Z. The predeclared PC-PRTL-01 row contains "three call sites" as the expectation. | **UPHELD** |
| CH-P9 | **PD-PRTL-01** (A2's plan was written after its source re-read began). Does it undermine any A2 verdict that REC or Proof relied on? | The A2 portal source files have mtimes from 14:53:43Z. The plan was written at 14:56:31Z, about 3 minutes later. The plan holds scope items only (T1–T7) and no expected outcomes, so it never worked as a falsification device, and that did not change when it was written. Proof re-confirmed every HIGH verdict. The refuted item was an enumeration refinement, which is the kind of error an early plan would not have prevented. REC MATCH items that rest on A2 alone, with no Proof or A3 replay: C14 (password/deactivation) and C17 (chatter fetch). | **UPHELD**: no verdict relied on by REC or Proof is undermined. Advisory: C14 and C17 MATCH carry A2-only weight (see Limitations) |
| CH-P10 | **Lineage, overclaim and Lane B misuse** | Each input has one commit, and the committed blob equals the current file. Three commits carry messages naming unrelated modules (see 0.1). REC was committed at 15:10:22Z, after Proof finished at 15:07:04Z, and it cites PC results "for classification support only". The two stages are declared as one run. No runtime claim appears anywhere. Lane B: none exists, none is used, and no absence is marked FAIL. | Overclaim: **UPHELD** (none found). Lane B: **UPHELD** (no misuse). Commit labels: **CHALLENGE-SUSTAINED (Integration Control), LOW**, content unaffected. REC–Proof coupling: noted, not sustained, because it is declared |
| CH-P11 | **QID mapping fit (sample of 3) and bank hash** | Q003 (revocation effective across saved links) ← REC-09/18: fits. Its disconfirming observation is exactly the static C09 reading. Q004 (credential scoped to record/action) ← REC-01/21: fits. Q021 (archived-record visibility rule) ← REC-22 (O3): fits. The bank sha256 equals the freeze entry, and the freeze hash was recomputed as identical. No QID is answered. | **UPHELD** |
| CH-P12 | **Clean-room scan** of all five inputs | A3 scanned for code-shaped fragments (function definitions, `self.`/`sudo()` calls, imports, UUID/HMAC calls). The hits were false positives inside prose, such as "itself.". No percentages were found. "Formal Coverage" appears only in disclaimers. | **UPHELD** |

## 2. Lineage

- **Chain:** Lane A `af066bfb…` → A1 `aef33889…` → A2 `695171c7…` → REC `abb7e72d…` → PROOF `09190a38…` → this A3. Every stage header cites its predecessor's sha256, and A3 re-verified each one.
- **Join key:** MODULE `portal` + QID + freeze hash `1247c218ba4e2e6a57e259427030f4350881da56a5a28c59901a20f8b2d3a5d3`, recomputed as identical.
- **Blob integrity:** A3 matched 7 re-fetched portal blobs, including the gate, pager, wizard and mixin files.
- **Origin of the call-site omission:** it starts in Lane A, which enumerated no pager minting. A1 inherited it (C01 says "on first URL build"). A2 refined it to 3 sites, and Proof caught it.

## 3. Defects routed

| ID | Severity | Owner stage | Defect | Action requested |
|---|---|---|---|---|
| D-PRTL-A3-01 | LOW-MED | PROOF (runtime case authoring) | The PC-PRTL-17 R1 extension assumes a client can craft session history, which it cannot. R1 also understates that the pager works on the superuser handle | Rewrite the R1 extension as the stale-history scenario in CH-P2, and restate R1's severity basis |
| D-PRTL-A3-02 | LOW | A2 (PR-P5) / PROOF | PC-PRTL-18 fail condition is record-only and cannot falsify | Add a falsifiable outcome |
| D-PRTL-A3-03 | LOW | Integration Control | The A2, REC and Proof portal files were committed under messages naming other modules | Record a lineage erratum. No content change is needed |
| (carried) | — | A2 / Lane A | The "three call sites" refinement is incomplete (PC-PRTL-01 FAIL) | Already recorded by Proof. MASTER should cite the 5/4 count |

## 4. Runtime-blocked items (NOT-EXECUTED; not passed, not failed)

- PC-PRTL-14..22 (PR-P1..P9) are blocked, and all 10 UNKNOWN_PENDING_PROOF items remain open. In priority order:
  - PC-14: revoked-customer link survival and impersonation.
  - PC-17: minting without read, with the R1 extension rewritten as in D-PRTL-A3-01.
  - PC-18: archive and cross-company reach by token.
  - PC-20: parent-company rename.
  - PC-16: share wizard mint-on-open.
- The 4 CONTRADICTION items (C07, C13, C16, O1) have a static reading that supports A2. Their runtime effect is pending.
- The 6 GAP items (O8, G1–G5) are carried to MASTER.

## 5. Limitations

- Static only. `mail`, `auth_signup` and most of `base` were not read, and neither were the JS/SCSS assets.
- The `sale` portal controller was read only to see how the session history list is filled. Other downstream portal modules may fill it differently.
- A3 did not re-read C14 (password/deactivation) or C17 (chatter fetch). Their MATCH rests on A2 alone.
- A3 did not independently re-execute PC-PRTL-03, 05, 06 (beyond the hash/validator lines), 07, 10, 12 or 13.
- No percentages. No Formal Coverage claim. Read-only git. Inputs were not edited.
