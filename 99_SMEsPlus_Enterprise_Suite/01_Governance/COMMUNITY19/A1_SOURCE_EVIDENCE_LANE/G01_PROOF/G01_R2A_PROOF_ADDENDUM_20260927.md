# G01 PLATFORM_BASE — RED TEAM Proof Addendum (Remediation Cycle R2, batch R2A) — `auth_signup`, `base_automation`, `bus`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **PROOF**. This is an addendum only. No parent Proof package, parent Proof addendum, A2, or REC artifact is edited. Append-only lineage |
| Group / Modules | G01 PLATFORM_BASE / `auth_signup`, `base_automation`, `bus` |
| Cycle | Remediation Cycle R2, batch R2A |
| Date | 2026-09-27 |
| **REC consumed (rule 4)** | `G01_RECONCILIATION/G01_R2A_REC_ADDENDUM_20260927.md`, sha256 **`5cb08842fe3c1f1fc642e185903de580251f2314cdcda042ac233a42008278d5`**, frozen 2026-09-27T16:34:38.829Z — **before** this Proof's predeclaration |
| A2 consumed | `G01_A2_REVIEWS/G01_R2A_A2_ADDENDUM_20260927.md`, sha256 `1a51ec1f84e995aea5a1c06f1b513d109b9d691ed4cec37adef7c2d5c25e2313`, frozen 2026-09-27T16:33:22.013Z |
| **Predeclaration (rule 5)** | Scratch `r2_batchA/logs/proof_r2a_cases_predeclared.txt`, sha256 **`4442bba28ef3e4e577c87a26d7bf62e4b821ce272435661aa0a4afadf0c42ddf`**, timestamp **2026-09-27T16:35:01.548Z**, file read-only thereafter |
| Proof-stage source fetch | Started **after** predeclaration: `fetch_start` = **2026-09-27T16:35:14.443Z** (13 s after the predeclaration stamp), ended 2026-09-27T16:35:16.495Z. Log: `r2_batchA/logs/proof_r2a_exec_log.txt`, sha256 `bfb9f9f0c30a324ccd0a7f4d49b73343ea7b2f3269ec433bb3d04e06e5cd481b` |
| Stage order achieved | A2 addendum (16:33:22Z) → REC addendum hashed (16:34:38.829Z) → Proof predeclared and hashed (16:35:01.548Z) → Proof fetch and execution (from 16:35:14.443Z) |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`; every file checked with `git hash-object` (§2) |
| Runtime device | THPATTARAKRIT-SOLUTION-SERVICE-2.local: still recorded **OFFLINE** by every upstream Proof artifact in this cycle; not re-probed here (no new information since the last upstream probe) |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** (disposition for every module remains PARTIAL: source/config executed, runtime pending) |

### 0.1 Parent artifacts (sha256; unchanged)

| Parent | sha256 |
|---|---|
| `G01_A3_CHALLENGES/G01_B3A_A3_RECHECK_R1_20260927.md` | `a63547079815bab5d682aab52ca4974ff79ffa24ea9b840eac0d400d543c7699` |
| `G01_A3_CHALLENGES/G01_BATCH2_A3_RECHECK_R1_20260927.md` | `52a0e7f1b9b98f46a962025b38b1cf518851653aeb11a613e7e7d5d9a5043261` |
| `G01_PROOF/G01_B3A_PROOF_ADDENDUM_R1_20260927.md` | `d64cdefeb70da1e89216a8007d537bef3f3f16961e0ee744122f6f52845583ce` |
| `G01_PROOF/G01_BATCH2_PROOF_ADDENDUM_R1_20260927.md` | `141fb8558c59303a9e6395d4bd6fd2b26bf5fb865d6d094988153108fd0854f9` |

### 0.2 Residual IDs addressed here

R-ASGN-1, R-ASGN-2 (Proof-owned parts: supersede PC-ASGN-36 and PR-ASGN-13's wording), R-BAUT-1 (supersede PC-BAUT-64R1's (ii-b) expected text only), R-BUS-1 (supersede PC-BUS-22's design note), R-BUS-3 (supersede PC-BUS-23's citation). R-BUS-2 is a REC-owned lineage correction (§3 of the REC addendum); Proof records no case for it.

**Independence and blindness disclosure.** The same controller wrote the A2 and REC addenda of this batch and performed their source re-reads before predeclaring here. The predeclared expectations are therefore **not blind** to source; they are falsifiable re-reads, and A3 should weigh them as such (consistent with MD-04/MD-09, which govern eventual *runtime* execution by a different author, not this static predeclaration).

Clean-room note: neutral paraphrase only; identifiers and line numbers are pointers. No vendor code is reproduced. No percentages. No Formal Coverage claim. No QID answered. No git operations. No existing artifact was edited.

### 0.3 MASTER process-rule compliance (this addendum)

| Rule | Compliance | Evidence |
|---|---|---|
| 1. Preserve A2 `MISSING_REQUIRED_RUNTIME_PROOF` | **MET**. Every runtime case below carries its A2 label; no Proof text reclassifies a label | §4 |
| 2. Post-declaration text tagged `POST-DECLARATION` | **MET**. No observation below exceeds the predeclared file's Expected/Fail text; nothing required tagging in this batch (all wording matches the sealed predeclaration verbatim in substance) | §§2–3 |
| 3. REC scans all A1 classes | **NOT APPLICABLE** (REC duty; met in the REC addendum §3) | — |
| 4. REC hashed before Proof; Proof header records REC hash | **MET**. REC hash `5cb08842…8d5` at 16:34:38.829Z; predeclaration 16:35:01.548Z; execution after | Header |
| 5. Cases sha256 + UTC before the first Proof source fetch | **MET**. Predeclared file hashed and timestamped at 16:35:01.548Z; the Proof-stage fetch folder (`src_proof/`) and its earliest file both post-date that stamp (fetch_start 16:35:14.443Z, 13 s later) | Header; exec log |
| MD-07 (anchor-only admissibility) | **MET**. All 8 files re-fetched by this stage are raw-URL anchor fetches, `git hash-object`-verified; 4 are exact re-verifications of blobs already pinned by the B3a/batch-2 stages (no drift), and 4 are manifest files newly fetched for the boundary check in §3.1, quoted only for their `depends` list | §2 |
| MD-08 (bounded completeness) | **MET**. §3.1 carries the A2/REC boundary statement into the executed case rather than dropping it; PC-ASGN-36R2's PASS is judged against the bounded table, not against an unqualified "no other caller exists" claim | §3.1 |

---

## 1. Supersede map

| Old case | New case | Reason | Old verdict status |
|---|---|---|---|
| PC-ASGN-36 (parent B3a, PASS) | **PC-ASGN-36R2** | R-ASGN-2: supersedes the candidate table with the manifest-`depends`-and-`__init__`-chain enumeration and its stated boundary | Superseded. The parent PASS is kept in lineage and no longer separately counted; PC-ASGN-36R2 replaces it |
| PR-ASGN-13 (parent B3a, RUNTIME) | **PR-ASGN-13R2** | R-ASGN-1: wording only — adds the freeze-parameter branch to the procedure | Superseded (was, and remains, NOT-EXECUTED) |
| PC-BAUT-64R1 (parent B3a, RUNTIME) | **PC-BAUT-64R2** | R-BAUT-1: wording of the (ii-b) expected text only; fail condition unchanged | Superseded (was, and remains, NOT-EXECUTED) |
| PC-BUS-22 (parent batch-2, RUNTIME) | **PC-BUS-22R1** | R-BUS-1: design note only — records keep-alive open time and remaining lifetime so Case A cannot give a false FAIL | Superseded (was, and remains, NOT-EXECUTED) |
| PC-BUS-23 (parent batch-2, CONFIG/SOURCE, PASS) | **PC-BUS-23R1** | R-BUS-3: citation only — corrects which `set_cookie` method is named | Superseded. The parent PASS verdict is preserved, not overturned |

---

## 2. Blob verification (Proof-stage fetch, executed after predeclaration)

Log: `r2_batchA/logs/proof_r2a_exec_log.txt`, sha256 `bfb9f9f0c30a324ccd0a7f4d49b73343ea7b2f3269ec433bb3d04e06e5cd481b`. Fetch window 2026-09-27T16:35:14.443Z–16:35:16.495Z.

| Path | Blob | Prior record | Match |
|---|---|---|---|
| `odoo/addons/base/models/res_users.py` | `9d42d77ae8ec19028c99b3c668294569ded3a86a` | B3a A2 addendum §0.3 | **MATCH** |
| `odoo/addons/base/models/ir_actions.py` | `45d06ee4210b6e5559c6c96ab82ddc238a891a52` | B3a A2 addendum §0.3 | **MATCH** |
| `odoo/http.py` | `ebfc2ac8d268a45aaf4b8cde8c9ce8b480d58dbb` | batch-2 A2 addendum header | **MATCH** |
| `addons/portal/models/portal_mixin.py` | `d24085d8da0a56a8b078d0d073aa85d6016f6d79` | B3a A2 addendum §0.3 | **MATCH** |
| `addons/portal/__manifest__.py` | `0df9206a8a580649d9c2e81905e3e92a6a109587` | new pointer (no prior baseline; content is the `depends` list only) | — |
| `addons/survey/__manifest__.py` | `9ce3993427534ffcf32ea4164c27c67448309cf7` | new pointer | — |
| `addons/hr/__manifest__.py` | `d9d3f8fb63a472739c3a478ed8876297918b33c2` | new pointer | — |
| `addons/website_sale/__manifest__.py` | `b21579515c5558d1e7a4d5c0e37199040e45eb70` | new pointer | — |

No drift at the anchor on any re-verified file.

---

## 3. Static cases — executed (predeclared expected/fail in substance; sha256 `4442bba2…2ddf`)

### 3.1 `auth_signup` — PC-ASGN-36R2

| Case | Links | Expected | Fail condition | Actual (paraphrased) | Result |
|---|---|---|---|---|---|
| PC-ASGN-36R2 | C18-R1, REC-ASGN-18, R-ASGN-2 | A table confirming the five anchored call sites via a manifest-`depends`-and-`__init__`-chain method, with the enumeration's boundary stated | Any of the five sites absent at the anchor on re-fetch, or the boundary statement omitted | `addons/portal/__manifest__.py` (re-fetched, blob `0df9206a…`) lists `'depends': [..., 'auth_signup']`, confirming portal's edge to `auth_signup` and therefore the reachability basis for: portal share wizard, portal mail-thread notification, portal-mixin share-URL builder, and portal grant wizard (all four already anchor-content-verified by the B3a A3 re-check). `addons/survey/__manifest__.py` (re-fetched, blob `9ce39934…`) lists `'depends': ['auth_signup', ...]` directly, confirming the survey start page's reachability basis. `website_slides`'s reachability remains transitive (through `website_mail → portal`, not re-walked in this addendum beyond the A2 addendum's own chain read). `addons/hr/__manifest__.py` (blob `d9d3f8fb…`) and `addons/website_sale/__manifest__.py` (blob `b2157951…`) each list no `auth_signup` dependency, corroborating the B3a A3 content finding that neither calls either builder. The table carries the boundary statement from A2 §2.4 (historical 23-module roster manifest-checked; six named canonical addons; portal-mixin callers and the wider addon universe explicitly out of scope) unedited | **PASS** |

POST-DECLARATION observations: none — the executed table matches the predeclared Expected text in substance with no additions.

### 3.2 `bus` — PC-BUS-23R1

| Case | Links | Expected | Fail condition | Actual | Result |
|---|---|---|---|---|---|
| PC-BUS-23R1 | REC-BUS-14, R-BUS-3 | Same PASS verdict as PC-BUS-23; citation corrected to `FutureResponse.set_cookie` (the method the request-path session-cookie save actually invokes), not `Response.set_cookie` | Any divergence found between the two methods' defaults on re-read | Re-read of `odoo/http.py` (blob `ebfc2ac8…`, unchanged): the request-path session-save line calls `self.future_response.set_cookie(...)`. `FutureResponse.set_cookie` and `Response.set_cookie` are two distinct method definitions in the same file with an identical default-argument signature (`secure=False`, `samesite=None` unless overridden by the caller). No divergence between the two found. The session cookie is set with `httponly=True` and a `max_age`; no explicit `secure` or `samesite` argument is passed on this path | **PASS** (framework, static; unchanged verdict from PC-BUS-23. Browser cross-site behaviour remains runtime: PC-BUS-08R1) |

POST-DECLARATION observations: none.

---

## 4. Runtime cases — wording-only supersessions, still NOT-EXECUTED (device offline; no result claimed)

| Case | Links | Steps (wording per predeclaration) | Expected | Fail condition | A2 label | Status |
|---|---|---|---|---|---|---|
| PR-ASGN-13R2 | O4-R1, R-ASGN-1 | As PR-ASGN-13 (issue a link on D; platform-duplicate, non-copy-restore and external copies), **plus**: record whether `web.base.url.freeze` is set on D before copying; after copying, as a system-group user, log in once with a request context carrying a base location; check `web.base.url` on the copy afterward | If the freeze parameter was unset on D, the copy's base URL is rewritten to the login's base location after that one login. If it was set, the copy's base URL stays at the reset local default | The base URL changes on a login when the freeze parameter was set, or stays fixed on a login when it was unset | MISSING_REQUIRED_RUNTIME_PROOF | NOT-EXECUTED |
| PC-BAUT-64R2 | O14-R2, REC-BAUT-38, REC-BAUT-11, R-BAUT-1 | As PC-BAUT-64R1 variants (i) default job user, (ii-a) settings-group U, (ii-b) non-settings V | (ii-b) **FAILED at the server-action gate (`_can_execute_action_on_records`, invoked before `_run`); rule search never reached**; nothing stamped; last-run unchanged; failure counter incremented. (i)/(ii-a) unchanged from PC-BAUT-64R1 | (ii-b) any record stamped, run not FAILED, or observed failure located at the rule search rather than the gate | MISSING_REQUIRED_RUNTIME_PROOF | NOT-EXECUTED |
| PC-BUS-22R1 | REC-BUS-28, R-BUS-1 | As PC-BUS-22 (Case A: no further publish for 120 s; Case B: publish N2 at 70 s), **plus**: record the affected socket's keep-alive open time and configured timeout | Case A: N1 not delivered within 120 s, provided the socket's keep-alive lifetime has more than 120 s remaining at the pause's start. Case B: N1 delivered with or before N2 | Case A: N1 delivered within about 50–65 s with no further trigger, **or** the socket's keep-alive expired inside the 120 s window without that being recorded (invalidates, does not confirm loss) | MISSING_REQUIRED_RUNTIME_PROOF | NOT-EXECUTED |

Runtime totals for this addendum: **3 wording-superseded cases, all NOT-EXECUTED** (unchanged execution status from their parent cases; only Expected/Fail wording changed).

---

## 5. Effective case ledger after this addendum (per module)

Superseded cases are kept in lineage but not double-counted. No PASS is converted to FAIL, and no FAIL is converted to PASS, by this addendum.

| Module | Static cases this addendum | Runtime cases this addendum (wording only) | Net static PASS/FAIL change | Net runtime NOT-EXECUTED change |
|---|---|---|---|---|
| auth_signup | 1 executed (PC-ASGN-36R2, PASS, supersedes PC-ASGN-36) | 1 (PR-ASGN-13R2, wording only) | +0 net (one-for-one supersession) | +0 net (one-for-one supersession) |
| base_automation | 0 | 1 (PC-BAUT-64R2, wording only) | — | +0 net (one-for-one supersession) |
| bus | 1 executed (PC-BUS-23R1, PASS, supersedes PC-BUS-23) | 1 (PC-BUS-22R1, wording only) | +0 net (one-for-one supersession) | +0 net (one-for-one supersession) |

REC effect: no class change by Proof. All UNKNOWN_PENDING_PROOF items and the runtime effect of every CONTRADICTION item remain open (REC-ASGN-18 stays CONTRADICTION; REC-BUS-28 and REC-BAUT-38/11 stay UNKNOWN_PENDING_PROOF). **Disposition for each module: PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.** Eligible for A3 re-check only; A3 → MASTER full handoff for these three modules remains not eligible until the runtime layer executes.

## 6. A3 re-check surface

A3 may re-check now: the supersede map (§1); the two executed static cases and their citations (§3); predeclaration integrity (sealed 16:35:01.548Z, before the Proof-stage fetch started at 16:35:14.443Z); the manifest-`depends` boundary statement carried unedited from A2 into PC-ASGN-36R2; and the R-BUS-2 rescan recorded in the REC addendum (Proof performed no case for it, by design — it is a lineage-only correction). Runtime outcomes remain blocked: no runtime prediction is proven.

## 7. Limitations

- No runtime executed; no runtime result claimed. Static PASS confirms source and manifest readings only and never counts for a runtime case.
- PC-ASGN-36R2 confirms reachability edges via `depends` declarations and previously anchor-verified `__init__`/content chains; it does not itself re-walk every `__init__` chain from scratch, and it inherits the A2 addendum's disclosed gap (portal-mixin callers unverified; wider Odoo/OCA addon universe not tree-listed).
- The predeclared expectations are not blind (same controller did the A2/REC re-read); timing rests on scratch files and timestamps that are not externally anchored.
- Runtime device status is carried from the last upstream probe, not re-probed by this addendum.
- No percentages. No Formal Coverage claim. No git operations. No existing file was edited. Source copies are in scratchpad `r2_batchA/src_proof/` only.
