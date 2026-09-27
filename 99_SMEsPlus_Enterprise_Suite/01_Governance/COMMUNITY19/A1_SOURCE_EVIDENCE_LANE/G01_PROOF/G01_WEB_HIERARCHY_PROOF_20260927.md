# G01 PLATFORM_BASE — Module `web_hierarchy` — PROOF (Stage 2)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2; Reconciliation recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `web_hierarchy` |
| Date | 2026-09-27 |
| Upstream REC | `G01_RECONCILIATION/G01_WEB_HIERARCHY_REC_20260927.md` (17 REC items) |
| Upstream A2 | sha256 `48bdd133401eca8a9353e8f386086b5defab97984cc54625e4c02ac3b6f41f17` (7 proof requirements PR-WHIR-01..07) |
| Upstream A1 / Lane A | sha256 `45c325c4…34a2` / `ec340b9b…74ac` (full values in REC intake) |
| Question lineage | No module MVQ bank. MVQ lineage: **NOT A3-ELIGIBLE (bank absent)**. Standard 55 (W1-STD `c64693ee…f5c213`, recomputed MATCH) only. |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/web_hierarchy/<path>` |
| Runtime device | OFFLINE (last recorded 2026-09-24T12:53Z) |
| Lane B | None exists (search recorded in REC section 3) |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** |

## 2. Predeclaration

- 14 proof cases (7 SOURCE + 7 RUNTIME), one static and one runtime case per A2 proof requirement, fixed in `predeclared_proof_cases.tsv` sha256 `2203bab7a4d6ebdd38a61dccda74340a5c02c66774a6c5644e48441a2b22f307`, written 2026-09-27T15:10:27Z **before** this controller fetched any source (shared with the other three modules).
- RUNTIME cases stay NOT-EXECUTED while the device is OFFLINE; ready to run; no invented results.

## 3. Source retrieval and blob verification

Log `blobcheck.txt` sha256 `fa3e505373e76ef0d9ddd3c6420878b5d2b960a1c27c57afd75381e790b93f17`.

| Path | Blob (recorded = computed) | Result |
|---|---|---|
| `__manifest__.py` | 4415a3857877d3c7bad740228d632aa1c78bb067 | MATCH |
| `__init__.py` | d6210b1285d37ef0ef813097b4de4d889ad7012e | MATCH |
| `models/__init__.py` | 89107c88c34ba277c9f06b381359038ecbe092cf | MATCH |
| `models/ir_actions.py` | e95d2c87dd7989c17e11de87aa72d30acd3c4c4d | MATCH |
| `models/ir_ui_view.py` | ce1d68e9a6948c85da5df8244bded7c5f6106550 | MATCH |
| `models/models.py` | 88136e7d2b2bd4545ef6c63e2d4d3ef8c56eeaca | MATCH |

6 of 6 match. Absence probes (HTTP 404): `controllers/__init__.py`, `security/ir.model.access.csv`, `tests/__init__.py`.

## 4. Proof cases and results

| PC | PR / REC | Layer | Preconditions | Steps | Expected | Fail condition | Result | Evidence |
|---|---|---|---|---|---|---|---|---|
| PC-WHIR-01 | PR-WHIR-01 / REC-WHIR-10 | SOURCE | Blobs verified | Scan module Python for elevation; read the helper's search and grouped read | No elevation; search and grouped read run under the caller's environment | Any elevation | **PASS** (0 elevation calls in all 6 files) | `models/models.py`@88136e7d L13, L22, L29–34 |
| PC-WHIR-02 | PR-WHIR-01 | RUNTIME | Rules hide one sibling and one child | Call the helper | Hidden records absent, no error | Returned, or error | **NOT-EXECUTED** (device OFFLINE; ready to run) | — |
| PC-WHIR-03 | PR-WHIR-02 / REC-WHIR-10 | SOURCE | Same | Read the single-match branch | Parent obtained by following the record's relation (not via search) and included in the final read set | Parent obtained via a rule-filtered search | **PASS** — confirms the source basis of the C10 PARTIAL: the parent is added by relation traversal, then read together with the rest | `models/models.py`@88136e7d L17–22 (parent added L19–20), L36 (final read) |
| PC-WHIR-04 | PR-WHIR-02 | RUNTIME | Caller cannot read the parent | Single-match call | Access error for the whole call | Result returned | **NOT-EXECUTED** | — |
| PC-WHIR-05 | PR-WHIR-03 / REC-WHIR-05 | SOURCE | Same | Read hierarchy view validation | Parent/child field names are allow-listed only; no presence or type check | Presence or type check present | **PASS** | `models/ir_ui_view.py`@ce1d68e9 L7–20 (allow-list, 12 names), L31–54 (children and attribute-name checks only; skip when not validating L32–33) |
| PC-WHIR-06 | PR-WHIR-03 | RUNTIME | Test instance | Install a view without parent field and one with a bogus field | Both pass server validation | Either rejected | **NOT-EXECUTED** | — |
| PC-WHIR-07 | PR-WHIR-04 / REC-WHIR-06 | SOURCE | Same | Read the helper's parameter handling | Parent-field name not validated against model fields; caller specification mutated in place when the parent is missing | Explicit validation present | **PASS** | `models/models.py`@88136e7d L9–12 |
| PC-WHIR-08 | PR-WHIR-04 | RUNTIME | Test instance | Call with a bogus parent field | ORM-level error | Domain-specific message | **NOT-EXECUTED** | — |
| PC-WHIR-09 | PR-WHIR-05 / REC-WHIR-13 | SOURCE | Same | Read the search calls | No limit passed; multi-match returns the full set | Limit present | **PASS** (neither search call nor the grouped read passes a limit; the ordering argument is also passed to the grouped read, confirming REC-WHIR-15) | `models/models.py`@88136e7d L13, L22–24, L29–34 (order L33) |
| PC-WHIR-10 | PR-WHIR-05 | RUNTIME | Large model | Always-true domain | All rows returned | Capped | **NOT-EXECUTED** | — |
| PC-WHIR-11 | PR-WHIR-06 / REC-WHIR-09, 14 | SOURCE | Same | Read recordset combination; look for recursion or cycle checks | Recordsets concatenated (duplicates possible), not unioned; no recursion or cycle check | Union used, or recursion present | **PASS** (both additions in the single-match branch concatenate; one expansion only; no recursion) | `models/models.py`@88136e7d L20, L22 |
| PC-WHIR-12 | PR-WHIR-06 | RUNTIME | Self-parent record | Single-match call | Duplicate row | No duplicate, or loop | **NOT-EXECUTED** | — |
| PC-WHIR-13 | PR-WHIR-07 / REC-WHIR-11 | SOURCE | Same | Read the helper declaration; confirm no controllers | Public (non-underscore) model method, not marked private; no controllers package | Private/underscore method | **PASS** | `models/models.py`@88136e7d L9–10; `controllers/__init__.py` 404 |
| PC-WHIR-14 | PR-WHIR-07 | RUNTIME | Internal user | Call via generic model-method RPC | Reachable under caller rights | Not reachable | **NOT-EXECUTED** | — |

### Result totals

| Result | Count | Cases |
|---|---|---|
| PASS | 7 | PC-WHIR-01, 03, 05, 07, 09, 11, 13 |
| FAIL | 0 | — |
| NOT-EXECUTED | 7 | PC-WHIR-02, 04, 06, 08, 10, 12, 14 (all RUNTIME) |

No failures were recorded. Static PASS confirms only the source-visible precondition.

## 5. Effect on REC items

| REC item | Status after Proof |
|---|---|
| REC-WHIR-10 (GAP, C10 PARTIAL) | Source basis for both halves confirmed (PC-WHIR-01, 03): siblings/children via caller-scoped search; parent via relation traversal. Whether an unreadable parent errors or truncates is runtime (PC-WHIR-04). |
| REC-WHIR-11 (UNKNOWN_PENDING_PROOF) | Source precondition PASS (PC-WHIR-13). Reachability pending (PC-WHIR-14). |
| REC-WHIR-13 (GAP, unbounded multi-record result) | Confirmed on source (PC-WHIR-09). Runtime scale effect pending (PC-WHIR-10). |
| REC-WHIR-14 (GAP, self-parent duplicate) | Construction confirmed (PC-WHIR-11). Outcome pending (PC-WHIR-12). |
| REC-WHIR-05, 06, 09 (MATCH, supplementary PR) | Source confirmed; runtime twins pending. |
| REC-WHIR-15, 16, 17 (GAP, no PR) | No proof case; A2 source basis stands (REC-WHIR-15 ordering pass-through also seen in PC-WHIR-09). |

## 6. Runtime pack (ready to run when the device is online)

Isolated instance at anchor `8d05257d` with a self-referencing model and record rules configured to hide chosen records from a test user. Record raw RPC responses, row counts, error types and the user context. PC-WHIR-10 needs a model with a large synthetic row count; record memory and time if available. Do not re-run failures.

## 7. A3 eligibility and challenge surface

**A3 may challenge now (claim level only):** REC classifications (C10 as GAP rather than CONTRADICTION; C11 as the only UNKNOWN_PENDING_PROOF); the 7 executed static cases and their citations; blob verification; Standard 55 lineage (11 STD-QIDs; 5 items no fit); clean-room compliance.

**A3 may not:** treat any RUNTIME outcome as proven, or challenge at MVQ-QID level — **MVQ lineage is NOT A3-ELIGIBLE (bank absent)** until GMVQ authors a `web_hierarchy` bank.

## 8. Limitations

- One anchor commit. The JS view (client parent-field enforcement, cycle traversal) and framework internals (read routine, record-rule application to relation traversal, display-name privilege) were not read.
- No runtime execution; no fabricated results. No external service contacted beyond the source host.
- No Formal Coverage; no percentages; no QID answered.
- Clean room: neutral summaries; identifiers are pointers; no code reproduced. Inputs not edited; no git operations. Scratch: `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/rec_ui4`.
