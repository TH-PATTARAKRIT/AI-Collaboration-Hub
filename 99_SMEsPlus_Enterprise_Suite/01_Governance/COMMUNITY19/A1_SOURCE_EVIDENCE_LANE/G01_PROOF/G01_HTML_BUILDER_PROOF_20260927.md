# G01 PLATFORM_BASE — Module `html_builder` — PROOF (Stage 2)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2; Reconciliation recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `html_builder` |
| Date | 2026-09-27 |
| Upstream REC | `G01_RECONCILIATION/G01_HTML_BUILDER_REC_20260927.md` (13 REC items) |
| Upstream A2 | sha256 `745b25b560cbcac864b19c59ab5f9f32db69e142db169e3f47ca279465760b3d` (4 proof requirements PR-HBLD-01..04) |
| Upstream A1 / Lane A | sha256 `2cfc3d1e…3332` / `76275bbb…deec` (full values in REC intake) |
| Question gate | W1-B06 HOLD-LOCAL (recomputed `a01a5d72…7035` ≠ manifest `58e86d15…fa94`). MVQ lineage: **NOT A3-ELIGIBLE (gate HOLD)**. Standard 55 (W1-STD, recomputed MATCH) is the only lineage lens. |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/html_builder/<path>` |
| Runtime device | OFFLINE (last recorded 2026-09-24T12:53Z) |
| Lane B | None exists (search recorded in REC section 3) |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** (one cross-module SOURCE case NOT-EXECUTED for an unmet precondition; see PC-HBLD-05) |

## 2. Predeclaration

- 8 proof cases (6 SOURCE/CONFIG + 2 RUNTIME), fixed in `predeclared_proof_cases.tsv` sha256 `2203bab7a4d6ebdd38a61dccda74340a5c02c66774a6c5644e48441a2b22f307`, written 2026-09-27T15:10:27Z **before** this controller fetched any source (shared with the other three modules).
- PC-HBLD-07 and PC-HBLD-08 are static checks for REC-HBLD-08 (C08 count) and REC-HBLD-02 (assets-only), in addition to the 4 A2 PRs.
- Predeclared special outcomes: PC-HBLD-05 → NOT-EXECUTED if save-path enumeration is impossible; PC-HBLD-06 → INCONCLUSIVE if the helper is not found in the enumerable file set.

## 3. Source retrieval and blob verification

The 6 Lane A pointer files were fetched and hashed with `git hash-object` (log `blobcheck.txt` sha256 `fa3e505373e76ef0d9ddd3c6420878b5d2b960a1c27c57afd75381e790b93f17`).

| Path | Blob (recorded = computed) | Result |
|---|---|---|
| `__manifest__.py` | f55fb07044ff6db8e5aee583226f781f3575b498 | MATCH |
| `__init__.py` | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 (0 bytes) | MATCH |
| `tests/__init__.py` | 171a01d1dcfcea9b4b4774f1ba1b86d2d303fec7 | MATCH |
| `tests/test_html_builder_assets_bundle.py` | 7792507bfa3f17176bed0e978a7b85a5673ae8c0 | MATCH |
| `i18n/html_builder.pot` | dd82b4946129d8d1368c4c4ae89b22781912d2a9 | MATCH |
| `static/src/builder.js` | 8ff24b4cfbd9ad95f500d0f2bcda16b00c943e61 | MATCH |

6 of 6 match. Absence probes (HTTP 404): `models/__init__.py`, `controllers/__init__.py`, `controllers/main.py`, `security/ir.model.access.csv`.

Additional retrieval for PC-HBLD-06 / PC-HBLD-05: the 79 static source files referenced in the translation template were fetched from the anchor (79 × HTTP 200; per-file blobs logged in `hb_static_fetch.txt` sha256 `bc2fe4be74593fab7977d515ac426fe38fc2c1b53474a207bcae6a92abd3b743`; file list `potfiles.txt` sha256 `b1b86d8e1a6abb30b98586ec6b7eead39b9c3ad0ec00c2dc3e1dde1e726c57da`). Only `static/src/builder.js` has a Lane A recorded blob (MATCH); the other 78 have no upstream record to compare against.

## 4. Proof cases and results

| PC | PR / REC | Layer | Preconditions | Steps | Expected | Fail condition | Result | Evidence |
|---|---|---|---|---|---|---|---|---|
| PC-HBLD-01 | PR-HBLD-01 / REC-HBLD-06, 11 | SOURCE/CONFIG | Blobs verified | Read builder-bundle remove directives and the test assertion | Directives remove all edit-pattern files (any type) and dark SCSS; the test asserts only the absence of the edit-SCSS suffix | Test covers all removal patterns, or directives absent | **PASS** | `__manifest__.py`@f55fb070 L28–40 (removes L38–39); `tests/test_html_builder_assets_bundle.py`@7792507b L8 (post-install tag), L16–19 |
| PC-HBLD-02 | PR-HBLD-01 | RUNTIME | Test instance | Run the post-install test; list the resolved builder bundle | Test passes; no edit-pattern or dark file | Any present | **NOT-EXECUTED** (device OFFLINE; ready to run) | — |
| PC-HBLD-03 | PR-HBLD-02 / REC-HBLD-07, 10 | CONFIG | Same | Read manifest frontend and primary-variables contributions | Background SCSS in the public frontend bundle; a variables glob in the shared primary-variables bundle | Either absent | **PASS** | `__manifest__.py`@f55fb070 L24–26, L41–43 |
| PC-HBLD-04 | PR-HBLD-02 | RUNTIME | Public page | Inspect compiled frontend CSS | Background rules present outside edit mode | Absent | **NOT-EXECUTED** | — |
| PC-HBLD-05 | PR-HBLD-03 / REC-HBLD-09 | SOURCE (cross-module) | Save-path enumeration possible (needs a full file listing) | Enumerate save paths; review server authorization in the owning modules | Server-side authorization per save path | Any path without it | **NOT-EXECUTED** — precondition unmet: no listing API (GitHub API 403 for this session; manifest uses globs), so save paths cannot be fully enumerated, and the owning-module review is outside this module. Lead observation only (not a result): the 79 enumerable files contain model-method calls for saving, renaming and deleting snippets on the UI view model and a name-search call; their server-side authorization lives in other modules and was not reviewed | `hb_static/…snippet_service.js` L281, L308, L436; `…select_many2x.js` L109 (fetched copies) |
| PC-HBLD-06 | PR-HBLD-04 / REC-HBLD-04 | SOURCE (bounded) | Enumerable set = 79 files from the translation template | Search for the helper named in the manifest comment | Usage classified runtime vs test-only | Not found → INCONCLUSIVE | **INCONCLUSIVE** — 0 occurrences of the helper and 0 imports from the mail client package in the 79 enumerable `static/src` files. `static/tests/**` (included in the unit-test bundle) is not enumerable. The result is consistent with a test-only coupling but does not prove it | `__manifest__.py`@f55fb070 L19–21, L64–67; `hb_static_fetch.txt` |
| PC-HBLD-07 | REC-HBLD-08 (C08, OM-H05) | SOURCE | Blobs verified | Count template entries and distinct referenced static files by type | 527 translatable entries (+1 header); 79 files = 32 JS + 47 XML; no Python references | Other counts | **PASS** (528 entry blocks including the header entry; 79 / 32 / 47; 0 Python) | `i18n/html_builder.pot`@dd82b494 |
| PC-HBLD-08 | REC-HBLD-02 (C02) | SOURCE | Same | Check init size; probe models/controllers/security | Init 0 bytes; probes 404 | Any probe 200 or non-empty init | **PASS** | `__init__.py`@e69de29b (0 bytes); 4 × 404 in `blobcheck.txt` |

### Result totals

| Result | Count | Cases |
|---|---|---|
| PASS | 4 | PC-HBLD-01, 03, 07, 08 |
| FAIL | 0 | — |
| INCONCLUSIVE | 1 | PC-HBLD-06 (predeclared outcome) |
| NOT-EXECUTED | 3 | PC-HBLD-02, 04 (RUNTIME, device OFFLINE); PC-HBLD-05 (SOURCE cross-module, precondition unmet) |

No failures were recorded. Static PASS confirms only the source-visible precondition.

## 5. Effect on REC items

| REC item | Status after Proof |
|---|---|
| REC-HBLD-06 (UNKNOWN_PENDING_PROOF) | Source precondition PASS (PC-HBLD-01). Stays pending until PC-HBLD-02 runs. |
| REC-HBLD-08 (GAP) | A2 count correction confirmed on source: 527 translatable entries; 79 / 32 / 47 files. |
| REC-HBLD-10, 11 (GAP) | Confirmed on source (PC-HBLD-03, PC-HBLD-01); runtime effect pending for REC-HBLD-10. |
| REC-HBLD-04 (MATCH) | Runtime vs test-only coupling still unclassified (PC-HBLD-06 INCONCLUSIVE). CRQ-HBLD-1 stays open. |
| REC-HBLD-09 (MATCH) | Cross-module authorization review not executed (PC-HBLD-05). CRQ-HBLD-2 stays open and should route to the `html_editor` / website / mass-mailing proofs. |
| REC-HBLD-12, 13 (GAP, no PR) | No proof case; A2 source basis stands. |

## 6. Runtime pack (ready to run when the device is online)

Isolated instance at anchor `8d05257d` with `html_builder` installed through a consumer (website or mass mailing). PC-HBLD-02: run the post-install test and dump the resolved builder-bundle file list. PC-HBLD-04: fetch a public page's compiled frontend CSS outside edit mode and search for the builder background rules. Record results as observed; do not re-run failures.

## 7. A3 eligibility and challenge surface

**A3 may challenge now (claim level only):** the REC classifications (only one UNKNOWN_PENDING_PROOF; C08 as GAP); the 4 executed static cases; the INCONCLUSIVE and NOT-EXECUTED reasons for PC-HBLD-05/06 and whether a wider enumeration is required; the Standard 55 lineage (4 STD-QIDs; most items no fit); clean-room compliance and lineage hashes.

**A3 may not:** treat either RUNTIME case as proven, treat the PC-HBLD-05 lead observation as a result, or challenge at MVQ-QID level — **MVQ lineage is NOT A3-ELIGIBLE (W1-B06 gate HOLD)**.

## 8. Limitations

- One anchor commit. Client JS/XML behaviour was not analysed beyond the text search in PC-HBLD-05/06. The static inventory is still a lower bound (79 files).
- No runtime execution; no fabricated results. No external service contacted beyond the source host.
- No Formal Coverage; no percentages; no QID answered.
- Clean room: neutral summaries; identifiers are pointers; no code reproduced. Inputs not edited; no git operations. Scratch: `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/rec_ui4`.
