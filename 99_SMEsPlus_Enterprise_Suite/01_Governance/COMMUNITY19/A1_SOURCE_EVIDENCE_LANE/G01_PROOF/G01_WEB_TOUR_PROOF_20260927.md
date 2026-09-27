# G01 PLATFORM_BASE — RED TEAM PROOF — `web_tour`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2 of a two-stage REC + PROOF run; Stage 1 is `G01_RECONCILIATION/G01_WEB_TOUR_REC_20260927.md`) |
| Group / Module | G01 PLATFORM_BASE / `web_tour` |
| Date | 2026-09-27 |
| Upstream | A1 `d794e25f…d315`; A2 `b7d58513…81b4`; Lane A PASS-1 `111e1959…87d0`; REC `G01_WEB_TOUR_REC_20260927.md` (this run) |
| Bank / freeze | W1-B05, bank sha256 `fdc06e0b…6f37` = FREEZE_W1-B05 entry; freeze hash `cc81bc57f3686bfec5eda5fff354599e4d2ba5a9855078e9c2eaa13a6ca91bd3`; ELIGIBLE |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`; every file blob-verified with `git hash-object` before use |
| Runtime device | **OFFLINE** — RUNTIME cases NOT-EXECUTED, ready to run. Nothing fabricated |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** |

Clean-room note: neutral statements of observed behaviour only; identifiers are evidence pointers; no vendor code reproduced. No percentages, no Formal Coverage, no git operations on the repository, inputs unedited.

## 1. Predeclaration record

- Cases file: `scratchpad/rec_web/PROOF_CASES_WEB_WEBTOUR_PREDECLARED.txt` (shared with `web`), declared **2026-09-27T15:05Z**, sha256 `32cafe38c3bbc4101faa2aca922063b7a3eaa226970c101952a0e8f71dbec6fb`, recorded before the first source fetch (15:05:46Z). No case was changed after execution. Section 3 reproduces the `web_tour` cases as declared.

## 2. Source fetch and blob verification

| Path at anchor | HTTP | Recomputed blob | Recorded (Lane A / A2) | Result |
|---|---|---|---|---|
| addons/web_tour/models/tour.py | 200 | 575bf0a5953a383c2733c7775ec699f6e73724ac | 575bf0a5… | MATCH |
| addons/web_tour/models/res_users.py | 200 | 9ab9decb169d9902b0a51494694447f972b5236d | 9ab9decb… | MATCH |
| addons/web_tour/models/ir_http.py | 200 | 1e7889a99ee503313d0dc65c2ffe4ab89ac01df2 | 1e7889a9… | MATCH |
| addons/web_tour/security/ir.model.access.csv | 200 | 71ea4517ba59b0a592677b7cc6e6c3ccaec14619 | 71ea4517… | MATCH |
| addons/web_tour/views/tour_views.xml | 200 | c80188dc901a523a0ffb2ec0c3a78b33d828dc1b | c80188dc… | MATCH |
| addons/web_tour/__manifest__.py | 200 | 5945c1565cf76b2ec760a3c7a0e90e26e072b5f2 | 5945c156… | MATCH |
| addons/web_tour/__init__.py | 200 | 0650744f6bc69b9f0b865e8c7174c813a5f5995e | 0650744f… | MATCH |
| odoo/addons/base/models/ir_actions.py | 200 | 45d06ee4210b6e5559c6c96ab82ddc238a891a52 | 45d06ee4… (A2 prefix) | MATCH |
| odoo/addons/base/models/ir_attachment.py | 200 | 905ae118b8c8e5050fdc33eb1631c88e3926b888 | 905ae118… | MATCH |

9 of 9 MATCH. Content kept in the scratchpad only.

## 3. Cases, execution and results

### 3.1 RUNTIME cases (A2 PR-T01..PR-T03) — NOT-EXECUTED, ready to run

| Case | REC link | Preconditions | Steps | Expected | Fail | Result |
|---|---|---|---|---|---|---|
| PC-WTOUR-01 | REC-04 C04 | One internal user, one guide | Two concurrent consume calls for the same name | One membership row; coherent next guide | Duplicate row, or unhandled user-facing error | **NOT-EXECUTED** (device offline) |
| PC-WTOUR-02 | REC-11 C11 | Internal user not in the system group | (a) Run bound "Export JS" on a guide; (b) call export directly by RPC | Both refused with access error; no new attachment | Download action returned or attachment created | **NOT-EXECUTED** |
| PC-WTOUR-03 | REC-10 C10 | System user; guide name and start URL containing a double quote | Export; inspect generated script | Literal breaks/terminates early (per source) | Correctly escaped name and URL (refutes C10) | **NOT-EXECUTED** |

### 3.2 SOURCE cases — EXECUTED

| Case | Layer | REC link | Expected (predeclared) | Observed (paraphrase) | Result |
|---|---|---|---|---|---|
| PC-WTOUR-04 | SOURCE | REC-03 C03 | Internal + flag gate; excludes custom and consumed; ordered (sequence, name, id) | Current guide returned only when the user exists, has the flag and is internal; search excludes custom guides and those the user consumed; model order is sequence, name, id; first result or false | **PASS** |
| PC-WTOUR-05 | SOURCE | REC-04 C04, REC-22 SF-T01 | Lookup by name as caller; set-link under sudo; unknown name no-op; returns current guide | Internal-user check; name search as caller; if found, the user is linked to the consumed set under elevation with a set-link command (idempotent); unknown names do nothing; current guide returned in all cases. No step-completion verification exists | **PASS** |
| PC-WTOUR-06 | SOURCE | REC-10 C10, REC-12 C12, REC-16 OM-T01 | Steps via JSON serialisation; name and URL interpolated into script literals; attachment linked to guide | Steps serialised with a JSON dump; name and URL placed directly inside quoted literals of the generated script; attachment filename uses the raw name; a new attachment linked to the guide is created on every call; the consumed set is not touched; a download URL on the content route is returned | **PASS** |
| PC-WTOUR-07 | SOURCE | REC-11 C11 | Server action without groups needs write on its model; linked attachment create needs write on the target | Server-action run checks per action: if the action has groups, the user must share one; otherwise the user must pass a write access check on the action's model, else an access error (and a warning log). Attachment access maps create/unlink to a write check on the linked record, and create refuses when the linked record is not writable | **PASS** — supports A2's refutation of the C11 RISK |
| PC-WTOUR-08 | SOURCE | REC-08 C08 | 4 rows; system CRUD; internal read-only | 4 rows: system group full CRUD on guide and step; internal users read-only on both | **PASS** |
| PC-WTOUR-09 | SOURCE | REC-11 C11 (WHAT), REC-13 C13 | Code server action bound to guide model without groups; menu without group attribute | Server action of code type, model and binding model = guide, binding view type form, no group field; menu item under a base technical parent with no group attribute (no "groups" token in the file) | **PASS** |
| PC-WTOUR-10 | SOURCE | REC-06 C06, REC-07 C07, REC-20 OM-T05 | Default true only for admin + no demo + not test; self-toggle under sudo on current user only; no internal check | Stored editable computed flag, depends on creation date: true only if the user is admin (Access-Rights predicate) and the elevated count of demo-flagged modules is zero and no test is running. The model-level toggle writes the current user's flag under elevation with no internal-user check | **PASS** |
| PC-WTOUR-11 | SOURCE | REC-05 C05 | No company field on guide or step; consumed relation plain users | Neither model declares a company field; the consumed set is a plain relation to users | **PASS** |
| PC-WTOUR-12 | SOURCE | REC-09 C09, REC-21 OM-T06 | By-name getter public; JSON builder private | The by-name getter is a public model method; the JSON builder is underscore-prefixed (private). The getter passes its search result, possibly empty, to the builder, which takes the first read row | **PASS** — supports A2 |
| PC-WTOUR-13 | SOURCE | REC-17 OM-T02 | Sharing URL from raw name, not URL-encoded | Computed as base URL + fixed path + query parameter carrying the raw name; no encoding step | **PASS** |
| PC-WTOUR-14 | SOURCE | REC-01 C01, REC-14 C14, REC-15 C15, REC-19 OM-T04 | Depends web only; auto-install; LGPL-3; init imports models only; no cron/config reads; session info adds flag + current guide | Manifest: depends on web only, auto-install true, LGPL-3. Package init imports models only. Keyword search for cron / config-parameter / server-config reads across the fetched module files: no hit. Session-info extension adds the flag and calls the current-guide method on every build | **PASS** |

### 3.3 Result counts

| Layer | Cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| SOURCE | 11 (PC-WTOUR-04..14) | 11 | 0 | 0 |
| CONFIG | 0 (module reads no config; PC-WTOUR-14 confirms absence) | — | — | — |
| RUNTIME | 3 (PC-WTOUR-01..03) | 0 | 0 | 3 |
| **Total** | **14** | **11** | **0** | **3** |

## 4. Proof status of REC items (status, not a measure)

| REC class | Items | Proof status |
|---|---|---|
| CONTRADICTION (2) | C11 (RESOLVED AT SOURCE) | PC-WTOUR-07/08/09 PASS; runtime PC-WTOUR-02 pending |
| | C09 (OPEN) | PC-WTOUR-12 PASS supports A2 |
| UNKNOWN_PENDING_PROOF (3) | C04, C10 | Source PASS (PC-05, PC-06); runtime PC-01, PC-03 pending |
| | OM-T03 | No predeclared case; carried |
| GAP (2) | G-2, G-4 | Not closable in scope |

## 5. Disposition

**PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.** 11 of 11 SOURCE cases PASS against blob-verified source; 3 RUNTIME cases NOT-EXECUTED (device offline), ready to run. The "Export JS by read-only user" hypothesis is refuted at source layer only.

## 6. What A3 may challenge now (source layer)

1. **C11 resolution**: whether the base write-check on the action's model and the attachment write mapping (PC-WTOUR-07) close every path — for example other modules granting write on guides, or a caller holding write via a group other than the system group.
2. **SF-T01 / Q028–Q031**: whether a client-asserted "consumed" marker is being over-read as completion evidence downstream.
3. **C05 / SF-T02**: DB-global guides and progress in a multi-company tenant model.
4. **OM-T03**: carried without a proof case (ORM relation behaviour on delete not read).
5. **C10**: exploitability is bounded by system-group authoring; A3 may challenge the supply-chain framing (SF-T03) before PC-WTOUR-03 runs.

## 7. Limitations

- Static source at one commit; no runtime, DB or client (JS) state observed.
- The JS runner/recorder, inherited menu-parent groups and HTML sanitisation of the completion message were not read.
- No Formal Coverage, no percentages, no git operations on the repository, inputs unedited.
