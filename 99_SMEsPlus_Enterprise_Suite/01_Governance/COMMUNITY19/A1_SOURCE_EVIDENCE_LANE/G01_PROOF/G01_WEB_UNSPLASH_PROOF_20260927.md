# G01 PLATFORM_BASE — Module `web_unsplash` — PROOF (Stage 2)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2; Reconciliation recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `web_unsplash` |
| Date | 2026-09-27 |
| Upstream REC | `G01_RECONCILIATION/G01_WEB_UNSPLASH_REC_20260927.md` (26 REC items) |
| Upstream A2 | sha256 `7f5695dab66aceb1205ab39f8c9bf13cfd23bb8450f01defba545856cdb3580e` (13 proof requirements PR-UNSP-01..13) |
| Upstream A1 / Lane A | sha256 `56fbe9f1…8829` / `9e1ae1b0…b5ea` (full values in REC intake) |
| Question lineage | No module MVQ bank. MVQ lineage: **NOT A3-ELIGIBLE (bank absent)**. Standard 55 (W1-STD `c64693ee…f5c213`, recomputed MATCH) only. |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/web_unsplash/<path>` |
| External provider | **Not contacted.** No request was sent to the image provider, its CDN or any other external service; the only host used was the source host |
| Runtime device | OFFLINE (last recorded 2026-09-24T12:53Z) |
| Lane B | None exists (search recorded in REC section 3) |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** |

## 2. Predeclaration

- 26 proof cases (13 SOURCE + 13 RUNTIME), one static and one runtime case per A2 proof requirement, fixed in `predeclared_proof_cases.tsv` sha256 `2203bab7a4d6ebdd38a61dccda74340a5c02c66774a6c5644e48441a2b22f307`, written 2026-09-27T15:10:27Z **before** this controller fetched any source (shared with the other three modules).
- Every RUNTIME case is declared against a **local mock** of the provider; none may send traffic to the real provider.
- PC-UNSP-22 and PC-UNSP-24 are observation cases (recorded either way), as A2 defined PR-UNSP-11/12.

## 3. Source retrieval and blob verification

Log `blobcheck.txt` sha256 `fa3e505373e76ef0d9ddd3c6420878b5d2b960a1c27c57afd75381e790b93f17`.

| Path | Blob (recorded = computed) | Result |
|---|---|---|
| `__manifest__.py` | 32cfd99d9b25c7bb9b7a7e42fc5592b8abb21f78 | MATCH |
| `__init__.py` | 7d34c7c054abd3105d5bb41fe9674111e1c27c16 | MATCH |
| `controllers/__init__.py` | 7fc0cd7cb934f5bf6ce85580e1b55623ea0e6ee6 | MATCH |
| `controllers/main.py` | 00cf725f2366dbaf88fa5baeb1b729f5ba4a1962 | MATCH |
| `models/__init__.py` | 1c72f271b8164155ee5580332fbf720b62f49abd | MATCH |
| `models/ir_qweb_fields.py` | 378935726fbaed412399ec4ea70fa5bce758b2bc | MATCH |
| `models/res_config_settings.py` | 3136eaef7fe32bf679c23cb094ae66c33069dd57 | MATCH |
| `models/res_users.py` | 3d4d2d8885bab0ac00acc3ed6cd4ef92bf82eb92 | MATCH |
| `views/res_config_settings_view.xml` | 0eeb25183ef895c8bde40eaf1fc2ac1fcc83724b | MATCH |
| `tests/__init__.py` | d059700a7b1ce50340c555f0c270b0cfa26d752a | MATCH |
| `tests/test_unsplash.py` | 31b8a1afd22d7789445a613dcf56112322b447b6 | MATCH |
| `static/src/frontend/unsplash_beacon.js` | 189939d2190ab306a041fcee8d69e57d7216c84a | MATCH |
| `static/src/unsplash_service.js` | fb8e66fe6a7ca1f7d25adbbdf8c3e6238c08e947 | MATCH |

13 of 13 match. Absence probe: `security/ir.model.access.csv` HTTP 404.

## 4. Proof cases and results

`main.py` = `controllers/main.py`@00cf725f. Line numbers refer to the fetched copy.

| PC | PR / REC | Layer | Preconditions | Steps | Expected | Fail condition | Result | Evidence |
|---|---|---|---|---|---|---|---|---|
| PC-UNSP-01 | PR-UNSP-01 / REC-UNSP-04 | SOURCE | Blobs verified | Read the app-id route | Public auth; parameter read with elevation; value returned | Non-public, or no elevation | **PASS** | `main.py` L147–149 |
| PC-UNSP-02 | PR-UNSP-01 | RUNTIME | App id configured | Anonymous JSON-RPC call | App id returned | Denied | **NOT-EXECUTED** (device OFFLINE; ready to run) | — |
| PC-UNSP-03 | PR-UNSP-02 / REC-UNSP-06, 26 | SOURCE | Same | Read the save route and manage predicate | Access-rights admin OR website restricted editor, both checked with elevation; else not-found; elevated writes without validation | Other groups, or validation | **PASS** | `main.py` L151–157; `models/res_users.py`@3d4d2d88 L9–16 (comment on missing website dependency L11–14) |
| PC-UNSP-04 | PR-UNSP-02 | RUNTIME | Restricted editor; plain user | Call the save route | Editor stores; plain user not-found | Opposite | **NOT-EXECUTED** | — |
| PC-UNSP-05 | PR-UNSP-03 / REC-UNSP-07, 19 | SOURCE | Same | Read the search route | Framework user-level auth with no group check; all caller parameters forwarded; server key set after them | Group restriction, parameter filtering, or caller key wins | **PASS** (whether "user" auth admits portal users is framework runtime behaviour → PC-UNSP-06) | `main.py` L130–145 (key set L138, outbound call L139) |
| PC-UNSP-06 | PR-UNSP-03 | RUNTIME | Portal user; local mock provider | Call with an extra parameter and a caller key | Extra parameter forwarded; server key used | Refused / dropped / caller key | **NOT-EXECUTED** | — |
| PC-UNSP-07 | PR-UNSP-04 / REC-UNSP-09 | SOURCE | Same | Read the image fetch | Prefix check on the submitted string only; no redirect option; no post-redirect host check | Redirects disabled or final host checked | **PASS** | `main.py` L84–88 |
| PC-UNSP-08 | PR-UNSP-04 | RUNTIME | Local mock host that redirects to an internal address | Submit an allowed-prefix URL (mock-resolved) | Internal address fetched | Not followed / re-checked | **NOT-EXECUTED** | — |
| PC-UNSP-09 | PR-UNSP-05 / REC-UNSP-10 | SOURCE | Same | Read both allow-list guards | Both skipped under the framework's process-wide current-test marker | Bypass keyed to a config flag, or absent | **PASS** | `main.py` L34 (notify), L84 (image) |
| PC-UNSP-10 | PR-UNSP-05 | RUNTIME | Test running in the same process | Submit a non-allow-listed URL (mock) | Fetched | Rejected | **NOT-EXECUTED** | — |
| PC-UNSP-11 | PR-UNSP-06 / REC-UNSP-11 | SOURCE | Same | Read the three outbound calls and the loop | No timeout on any call; body read whole; no item cap; no rate limit | Any timeout / cap | **PASS** | `main.py` L37, L88, L93, L139 (no timeout argument); loop L81–126 (no item cap) |
| PC-UNSP-12 | PR-UNSP-06 | RUNTIME | Local mock slow / large host | Submit | Worker blocked; body buffered | Module-level timeout or cap | **NOT-EXECUTED** | — |
| PC-UNSP-13 | PR-UNSP-07 / REC-UNSP-12, 22 | SOURCE | Same | Map each loop statement to handler coverage | Disallowed URL raises a generic exception; image processing and a missing URL field sit outside the narrow handlers; notify for item n is sent before item n+1 | All caught per item | **PASS** — confirms the A2 widening: abort causes are (a) disallowed URL, (b) missing URL field (string check on an absent value inside the try, not a handled type), (c) image-processing failure (outside the try); provider notify is sent at the end of each iteration | `main.py` L82–99 (handlers L94–99 cover connection and timeout only), L101–102, L126 |
| PC-UNSP-14 | PR-UNSP-07 | RUNTIME | Local mock | 3-item batches (bad URL; non-image) | Request fails; record item-1 persistence; notify for item 1 sent (to mock) | Batch completes | **NOT-EXECUTED** | — |
| PC-UNSP-15 | PR-UNSP-08 / REC-UNSP-15 | SOURCE | Same | Read path and name construction | Raw caller item key used in path and name | Key sanitised | **PASS** (only the query is sanitised, L59–65, L72–73) | `main.py` L81, L106–114, L119 |
| PC-UNSP-16 | PR-UNSP-08 | RUNTIME | Test instance | Key with separators / dot segments | Stored path unsanitised | Sanitised / rejected | **NOT-EXECUTED** | — |
| PC-UNSP-17 | PR-UNSP-09 / REC-UNSP-15 | SOURCE | Same | Read extension handling in the loop | Extension appended to the shared query variable across iterations | Per-item local variable | **PASS** | `main.py` L72–73, L104, L107 |
| PC-UNSP-18 | PR-UNSP-09 | RUNTIME | Test instance | Two items, same query | Second item has two extensions | One each | **NOT-EXECUTED** | — |
| PC-UNSP-19 | PR-UNSP-10 / REC-UNSP-17 | SOURCE | Same | Read the image-field save-back override | Provider-prefix path + record id → first attachment matching URL AND (same model+record OR public); no match → empty; no id → default handling | Other matching | **PASS** | `models/ir_qweb_fields.py`@37893572 L10–30 (prefix L16, id L17–19, lookup L21–27 with limit one, default path L30) |
| PC-UNSP-20 | PR-UNSP-10 | RUNTIME | Public attachment on record A | Save B's image field referencing A's path | B gets A's binary | Empty or own binary | **NOT-EXECUTED** | — |
| PC-UNSP-21 | PR-UNSP-11 / REC-UNSP-20 | SOURCE | Same | Read key transport and error handling | Key sent as query parameter; notify failure logged with exception text; search call has no connection-error handler | Key in header/body only, or errors sanitised | **PASS** (source precondition only; whether the key actually appears in log/error text depends on library messages → PC-UNSP-22) | `main.py` L21–23, L36–39, L138–139 |
| PC-UNSP-22 | PR-UNSP-11 | RUNTIME | Local mock unreachable | Trigger notify and search failures; inspect log and RPC error | Recorded either way | — (observation) | **NOT-EXECUTED** | — |
| PC-UNSP-23 | PR-UNSP-12 / REC-UNSP-21 | SOURCE | Same | Read save-route value handling | Values written as received, no presence check | Presence check or skip | **PASS** (framework handling of an absent value is runtime → PC-UNSP-24) | `main.py` L153–156 |
| PC-UNSP-24 | PR-UNSP-12 | RUNTIME | Restricted editor | Save with no values | Recorded either way | — (observation) | **NOT-EXECUTED** | — |
| PC-UNSP-25 | PR-UNSP-13 / REC-UNSP-16 | SOURCE | Same | Read the notify routine and its caller | Notify URL taken from the caller's item, prefix-checked only; key appended; docstring describes it as the provider download URL | URL derived from a trusted provider response | **PASS** (confirms CONTRADICTION-UNSP-1 on source) | `main.py` L25–39 (docstring L26–27), L126 |
| PC-UNSP-26 | PR-UNSP-13 | RUNTIME | Local mock | Submit a non-provider notify URL under the prefix (mock-resolved) | Request sent with server key (to mock) | Not sent | **NOT-EXECUTED** | — |

### Result totals

| Result | Count | Cases |
|---|---|---|
| PASS | 13 | PC-UNSP-01, 03, 05, 07, 09, 11, 13, 15, 17, 19, 21, 23, 25 |
| FAIL | 0 | — |
| NOT-EXECUTED | 13 | PC-UNSP-02, 04, 06, 08, 10, 12, 14, 16, 18, 20, 22, 24, 26 (all RUNTIME) |

No failures were recorded. Static PASS confirms only the source-visible precondition.

## 5. Effect on REC items

| REC item | Status after Proof |
|---|---|
| REC-UNSP-04, 06, 07, 09, 10, 11, 15, 17 (UNKNOWN_PENDING_PROOF) | Source preconditions PASS. They stay UNKNOWN_PENDING_PROOF until the RUNTIME cases run. |
| REC-UNSP-12 (GAP, more batch-stop conditions) | A2 widening confirmed on source (PC-UNSP-13): three abort causes. Rollback of earlier items remains runtime (PC-UNSP-14). |
| REC-UNSP-19 (GAP, portal users) | Route has no group check (PC-UNSP-05). Portal admission is framework runtime (PC-UNSP-06). |
| REC-UNSP-20, 21 (GAP, key in errors; credential clearing) | Source preconditions PASS; the effect is an observation case (PC-UNSP-22, 24). |
| REC-UNSP-22 (GAP, notifications not rolled back) | Ordering confirmed (notify at the end of each iteration, PC-UNSP-13). Runtime pending. |
| REC-UNSP-16 (MATCH, CONTRADICTION-UNSP-1) | Source-internal contradiction confirmed (PC-UNSP-25). |
| REC-UNSP-23..26 (GAP, no PR) | No proof case; A2 source basis stands. REC-UNSP-26 predicate reference confirmed in PC-UNSP-03 evidence. |

## 6. Runtime pack (ready to run when the device is online)

Isolated instance at anchor `8d05257d` with **all provider hosts resolved to a local mock** (DNS override or outbound proxy that answers locally and blocks real egress). Users: anonymous, portal, internal, website restricted editor (website installed), access-rights admin. Record the outbound request as captured by the mock, raw JSON-RPC responses, server log lines, attachment rows and filestore entries. PC-UNSP-10 needs a request served while a test is running in the same process. Do not re-run failures.

## 7. A3 eligibility and challenge surface

**A3 may challenge now (claim level only):** REC classifications (8 UNKNOWN_PENDING_PROOF; C12 and SF-U01 as GAP; no A1-vs-A2 CONTRADICTION); the 13 executed static cases, their predicates and citations; blob verification; Standard 55 lineage (13 STD-QIDs; REC-UNSP-05, 09, 20 no fit); clean-room compliance; the claim that no external service was contacted.

**A3 may not:** treat any RUNTIME outcome as proven (13 NOT-EXECUTED; Lane B UNCORROBORATED), or challenge at MVQ-QID level — **MVQ lineage is NOT A3-ELIGIBLE (bank absent)** until GMVQ authors a `web_unsplash` bank.

## 8. Limitations

- One anchor commit. Not read: the `html_editor` attachment helper, core serving protection and path-based serving, framework parameter semantics, group checks for a missing group, JSON-RPC error serialization, HTTP library redirect and timeout defaults, and the globbed JS directories.
- No runtime execution; no fabricated results; no traffic to the provider.
- No Formal Coverage; no percentages; no QID answered.
- Clean room: neutral summaries; identifiers (routes, parameter keys, hosts) are pointers; no code reproduced. Inputs not edited; no git operations. Scratch: `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/rec_ui4`.
