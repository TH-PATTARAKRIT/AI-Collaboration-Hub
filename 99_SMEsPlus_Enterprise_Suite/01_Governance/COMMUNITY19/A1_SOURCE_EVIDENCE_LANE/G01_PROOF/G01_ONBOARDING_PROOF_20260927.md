# G01 PLATFORM_BASE — Module `onboarding` — PROOF (Stage 2)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2; Reconciliation recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `onboarding` |
| Date | 2026-09-27 |
| Upstream REC | `G01_RECONCILIATION/G01_ONBOARDING_REC_20260927.md` (26 REC items) |
| Upstream A2 | sha256 `8f1ab5f7313f49ab16e77725a79dd02c75f4cd24d4a57a46d260cbb899386089` (10 proof requirements PR-ONBD-01..10) |
| Upstream A1 / Lane A | sha256 `50b0f4d6…71a9` / `c2f11c68…f651` (full values in REC intake) |
| Question gate | W1-B09 HOLD-LOCAL (freeze hash not reproducible; recomputed `0eecca3c…6614` ≠ manifest `f9f50636…5530`). MVQ lineage: **NOT A3-ELIGIBLE (gate HOLD)**. Standard 55 (W1-STD `c64693ee…f5c213`, recomputed MATCH) is the only lineage lens. |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/onboarding/<path>` |
| Runtime device | OFFLINE (last recorded 2026-09-24T12:53Z, `MASTER_CONTROLLED_HANDOFF_STATE_20260927.md`) |
| Lane B | None exists (search recorded in REC section 3) |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** |

## 2. Predeclaration

- 19 proof cases for this module (10 SOURCE/CONFIG + 9 RUNTIME). Every A2 proof requirement has one static case; PR-ONBD-08 is source-only (cross-module search), so it has no runtime twin.
- Cases, expected and fail conditions were written to a scratchpad file **before this controller fetched any source**: `predeclared_proof_cases.tsv` sha256 `2203bab7a4d6ebdd38a61dccda74340a5c02c66774a6c5644e48441a2b22f307`, written 2026-09-27T15:10:27Z (source fetch began after it; blob log closes 15:11:12Z). The file is shared with the `html_builder`, `web_hierarchy` and `web_unsplash` proofs (67 cases in all).
- Static predicates are the source-visible preconditions of the A2 predictions, taken from the A2 PR "Expected" column and A2 verdict basis.
- INCONCLUSIVE was predeclared as a permitted outcome only for PC-ONBD-15 (bounded cross-module search without a listing API).
- RUNTIME cases stay NOT-EXECUTED while the device is OFFLINE. They are ready to run and carry no invented result.

## 3. Source retrieval and blob verification

All 20 files in the Lane A pointer table were fetched from the anchor on 2026-09-27 and hashed with `git hash-object` (scratchpad only; no repository git operations). Log: `blobcheck.txt` sha256 `fa3e505373e76ef0d9ddd3c6420878b5d2b960a1c27c57afd75381e790b93f17` (all four modules).

| Path | Blob (recorded = computed) | Result |
|---|---|---|
| `__manifest__.py` | eaa50cca7d2c90c315d667811d90e0da328fa884 | MATCH |
| `__init__.py` | dc5e6b693d19dcacd224b7ab27b26f75e66cb7b2 | MATCH |
| `models/__init__.py` | 0e27595dad9c06d42f912e26af49eb37975f7368 | MATCH |
| `models/onboarding_onboarding.py` | 9ed728d6cbc8b6f45b090222c8b6f54a3f2de0cb | MATCH |
| `models/onboarding_onboarding_step.py` | 262186464fc868d9c5623f131e9832433cac3623 | MATCH |
| `models/onboarding_progress.py` | 26dacc185dcd6533fc7212cf72021f5f06474595 | MATCH |
| `models/onboarding_progress_step.py` | 311a0fef450dfadbe4f835e3fa4085b5813d1bce | MATCH |
| `security/ir.model.access.csv` | f99bf429ceb2f8b24b2d247afc4e3c3cf5b351cc | MATCH |
| `views/onboarding_views.xml` | 7688f73dda173608c7b8875d39f97cb7c8712044 | MATCH |
| `views/onboarding_menus.xml` | f036c70072cabf473f29c0dc1bb12e0a24dbe30f | MATCH |
| `views/onboarding_templates.xml` | 58cd0c2d3307fa793e0feb3218e11c0b1eb009b5 | MATCH |
| `static/src/scss/onboarding.scss` | 767ca652b9ebc2d851745e1e0e1dce030add501a | MATCH |
| `static/src/scss/onboarding.variables.scss` | 7698cf85528be46f6b8a00f78e1e4f220188b98c | MATCH |
| `static/src/scss/onboarding.variables.dark.scss` | 3736c78ab21c2ee89e11545de6295a59d9c0870f | MATCH |
| `i18n/onboarding.pot` | e506e7cbfec073f6ed731b8a3e883f53b1c8ecfd | MATCH |
| `tests/__init__.py` | efa3fd7505243e1ade826239f04b39f82ed7e731 | MATCH |
| `tests/case.py` | 3fa1aa8f0d4c97bdd056407c9f2224101b5b2948 | MATCH |
| `tests/common.py` | acd18d6ab1cbe233c2e1fad9b6752bce4d10ab7a | MATCH |
| `tests/test_onboarding.py` | 32649804ad896c28c186c369f7960d2a760bbe44 | MATCH |
| `tests/test_onboarding_concurrency.py` | 801def35ee5074177f34f6372f95008b0ac71220 | MATCH |

20 of 20 blobs match; 0 mismatches. Absence probes: `controllers/__init__.py`, `controllers/main.py`, `controllers/onboarding.py` all HTTP 404.

## 4. Proof cases and results

Evidence cites `path`@short blob with line ranges in the fetched copy. Neutral summaries only; no code reproduced.

| PC | PR / REC | Layer | Preconditions | Steps | Expected | Fail condition | Result | Evidence |
|---|---|---|---|---|---|---|---|---|
| PC-ONBD-01 | PR-ONBD-01 / REC-ONBD-06, 08 | SOURCE | Blobs verified | Read the panel render-state routine | Consolidation (just_done → done) runs before the closed-flag branch; nothing restores just_done on reopen | Closed branch first, or a restore | **PASS** | `models/onboarding_progress.py`@26dacc18 L53–78 (consolidation L72, closed branch L74); `models/onboarding_progress_step.py`@311a0fef L23–26; toggle `onboarding_progress.py` L49–51 does not touch step state |
| PC-ONBD-02 | PR-ONBD-01 | RUNTIME | Synthetic consumer panel | Validate, close, render, reopen, render | 1st render closed; 2nd shows done, no just_done | Step still just_done | **NOT-EXECUTED** (device OFFLINE; ready to run) | — |
| PC-ONBD-03 | PR-ONBD-02 / REC-ONBD-20 | SOURCE | Same | Read step-progress keys, consolidation target and panel links | Step progress unique per (step, company-or-none), not per panel; consolidation writes those shared records; global steps carry no company | Step state per panel | **PASS** | `models/onboarding_progress_step.py`@311a0fef L13, L19, L21, L23–26; `models/onboarding_onboarding_step.py`@26218646 L47–63, L130 |
| PC-ONBD-04 | PR-ONBD-02 | RUNTIME | Step shared by A and B | Validate; render A; render B | B shows done | B shows just_done | **NOT-EXECUTED** | — |
| PC-ONBD-05 | PR-ONBD-03 / REC-ONBD-15 | SOURCE/CONFIG | Same | Read ACL; scan module Python for elevation | Only `base.group_system` rows non-zero; "all" and internal-user rows all zero; no elevation in module runtime code | Any other grant or elevation | **PASS** (scope note: `models/` and package init have zero elevation calls; `tests/` build superuser environments and switch user in the test harness only, which is not module runtime code — disclosed for A3) | `security/ir.model.access.csv`@f99bf429 L2–13; scan of `models/*.py`, `__init__.py` |
| PC-ONBD-06 | PR-ONBD-03 | RUNTIME | Internal non-system user | Render and validate without elevation | Access error | Succeeds | **NOT-EXECUTED** | — |
| PC-ONBD-07 | PR-ONBD-04 / REC-ONBD-11 | SOURCE | Same | Read the per-company compute | Non-stored compute = (any company-bearing tracker) OR (any linked per-company step); no persisted one-way flag | Stored flag, or logic that never reverts | **PASS** — confirms A2's reading on source: with no company tracker and no per-company step the compute yields false, so the flag is not one-way. The code comment states the sticky intent, but it holds only through company trackers. Source side of the REC-ONBD-11 CONTRADICTION is confirmed against A1's "can only move from global to per-company" | `models/onboarding_onboarding.py`@9ed728d6 L22–24 (non-stored), L45–54 (comment L47–49) |
| PC-ONBD-08 | PR-ONBD-04 | RUNTIME | One per-company step, no trackers | Switch step to global; repeat after deleting company trackers | Reverts to global both times | Stays per-company | **NOT-EXECUTED** | — |
| PC-ONBD-09 | PR-ONBD-05 / REC-ONBD-22 | SOURCE | Same | Read the tracker step-link recompute and its callers | Recompute resolves step progress in the current context company and assigns it to every tracker of the panel | Per-tracker company used | **PASS** | `models/onboarding_progress.py`@26dacc18 L41–44; `models/onboarding_onboarding_step.py`@26218646 L47–54 (context-company resolution); callers `onboarding_onboarding.py`@9ed728d6 L71–77, step write L89–90 |
| PC-ONBD-10 | PR-ONBD-05 | RUNTIME | Trackers for A and B | From A add a step; inspect B | B linked to A's step progress | B stays B-scoped | **NOT-EXECUTED** | — |
| PC-ONBD-11 | PR-ONBD-06 / REC-ONBD-17 | SOURCE | Same | Read the open-callback constraint | Constraint triggers only on the step's panel-link field, not on the callback-name field | Also on callback field | **PASS** (whether writing the link from the panel side triggers it is framework behaviour and remains for PC-ONBD-12) | `models/onboarding_onboarding_step.py`@26218646 L65–72 (L65 dependency list = panel link only); callback field L30–33 |
| PC-ONBD-12 | PR-ONBD-06 | RUNTIME | Step without callback | (a) link from panel side; (b) clear callback on linked step | Record (a); (b) no error | (b) raises | **NOT-EXECUTED** | — |
| PC-ONBD-13 | PR-ONBD-07 / REC-ONBD-13 | SOURCE | Same | Read current-progress resolution | Filter company in (context, none) with no ordering/limit tie-break; result used as a single record | Limit/ordering picks one | **PASS** | `models/onboarding_onboarding.py`@9ed728d6 L56–69 (filter L60–61; single-record field reads L63–65) |
| PC-ONBD-14 | PR-ONBD-07 | RUNTIME | Global + company tracker co-exist | Read current state | Singleton-type error | One silently chosen | **NOT-EXECUTED** | — |
| PC-ONBD-15 | PR-ONBD-08 / REC-ONBD-16 | SOURCE (cross-module, bounded) | No listing API (GitHub API returned 403 for this session) | Probe 27 candidate controller paths in 9 modules; search each fetched file for "onboarding" | Owner identified with auth mode | Not found → INCONCLUSIVE; FAIL only if in-module absence disproved | **INCONCLUSIVE** — in-module absence re-confirmed (3 × 404). 10 candidate files fetched (in `web`, `base_setup`, `account`, `website`, `sale`, `payment`, `mail`); 0 mention "onboarding". Owner not located within the bounded set. This is **not** proof that the route is dead documentation | Probe log `xmod_probe.txt` sha256 `27ac7ee2bc3fce7b7acc097b66bec39f1c2244e5d481e37fbe6af4bd0ae542d5` |
| PC-ONBD-16 | PR-ONBD-09 / REC-ONBD-19 | SOURCE | Same | Read the rendering-values routine | Single-record assertion on the current tracker; no tracker creation in the render path | Render creates a tracker | **PASS** (panel assertion L126; the render-state routine asserts a single tracker at `onboarding_progress.py` L60; tracker creation exists only in the separate search-or-create helper, which the render path does not call) | `models/onboarding_onboarding.py`@9ed728d6 L125–135, L107–123; `models/onboarding_progress.py`@26dacc18 L60 |
| PC-ONBD-17 | PR-ONBD-09 | RUNTIME | Panel without tracker | Render | Single-record assertion error | Succeeds | **NOT-EXECUTED** | — |
| PC-ONBD-18 | PR-ONBD-10 / REC-ONBD-03 | SOURCE | Same | Read both unique indexes, the concurrency test and model error handling | Functional unique index on (panel\|step, company-or-none) for both trackers; test expects one winner + one violation; no catch in model code | Index missing or violation caught | **PASS** (test tagged non-standard, post-install) | `models/onboarding_progress.py`@26dacc18 L28; `models/onboarding_progress_step.py`@311a0fef L21; `tests/test_onboarding_concurrency.py`@801def35 L15, L58–61, L73–77; no exception handling in `models/` |
| PC-ONBD-19 | PR-ONBD-10 | RUNTIME | Test runner | Run the concurrency test | One tracker, one violation | Two trackers / no violation | **NOT-EXECUTED** | — |

### Result totals

| Result | Count | Cases |
|---|---|---|
| PASS | 9 | PC-ONBD-01, 03, 05, 07, 09, 11, 13, 16, 18 |
| FAIL | 0 | — |
| INCONCLUSIVE | 1 | PC-ONBD-15 (predeclared outcome) |
| NOT-EXECUTED | 9 | PC-ONBD-02, 04, 06, 08, 10, 12, 14, 17, 19 (all RUNTIME) |

No failures were recorded. A static PASS confirms only the source-visible precondition; it is **not** runtime proof of the A2 prediction.

## 5. Effect on REC items

| REC item | Status after Proof |
|---|---|
| REC-ONBD-11 (CONTRADICTION) | Source side confirmed (PC-ONBD-07 PASS): the per-company flag is a live, non-stored compute, not a one-way state. Runtime confirmation pending (PC-ONBD-08). |
| REC-ONBD-03, 06, 08, 13, 15 (UNKNOWN_PENDING_PROOF) | Source preconditions PASS. They stay UNKNOWN_PENDING_PROOF until the RUNTIME cases run. |
| REC-ONBD-17, 19, 20, 22 (GAP with PR) | Source preconditions PASS; the A2 refinement or omission is confirmed on source. Runtime effect pending. |
| REC-ONBD-16 (MATCH, supplementary PR-ONBD-08) | In-module absence confirmed; route owner still unknown (PC-ONBD-15 INCONCLUSIVE). GAP-1 stays open. |
| REC-ONBD-21, 23–26 (GAP, no PR) | No proof case; A2 source basis stands. A3 may challenge them. |

## 6. Runtime pack (ready to run when the device is online)

Authorized, isolated test instance at anchor `8d05257d` with a synthetic consumer module that declares panels, steps and callbacks, and creates trackers (the tests' "simulate role of controller" pattern). Two companies (A, B) and three users (system, internal non-system, portal). PC-ONBD-19 needs the non-standard, post-install test tag enabled. For each case record the render output, the stored states before and after, the company and user context, and raw errors. Record FAIL outcomes as they occur; do not re-run to obtain a pass.

## 7. A3 eligibility and challenge surface

**A3 may challenge now (claim level only):**
1. REC classifications, especially REC-ONBD-11 CONTRADICTION (A1 one-way scope claim) and the choice of GAP for REC-ONBD-17 (C17 PARTIAL).
2. The 10 executed SOURCE/CONFIG cases: predicate sufficiency, line citations, blob verification, and the scope note on PC-ONBD-05 (test-harness elevation excluded).
3. PC-ONBD-15 INCONCLUSIVE: the bounded candidate set and whether a wider search is needed.
4. The GAP items without a proof requirement (REC-ONBD-21, 23–26).
5. Standard 55 lineage (16 STD-QIDs mapped; REC-ONBD-02, 14, 25 no fit), clean-room compliance and lineage hashes.

**A3 may not:** treat any RUNTIME outcome as proven (9 cases NOT-EXECUTED; Lane B UNCORROBORATED), or challenge at MVQ-QID level — **MVQ lineage is NOT A3-ELIGIBLE (W1-B09 gate HOLD)** until GMVQ re-freezes W1-B09 canonically.

## 8. Limitations

- One anchor commit. Framework internals (constraint triggering on inverse links, singleton errors, image serving, transaction isolation of the render write) and the client JS were not read.
- No runtime execution took place and no results were fabricated. No external service was contacted beyond the source host.
- No Formal Coverage claim; no percentages; no QID answered.
- Clean room: neutral summaries; identifiers and line numbers are evidence pointers; no code reproduced.
- Inputs were not edited; no git operations. Scratch: `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/rec_ui4`.
