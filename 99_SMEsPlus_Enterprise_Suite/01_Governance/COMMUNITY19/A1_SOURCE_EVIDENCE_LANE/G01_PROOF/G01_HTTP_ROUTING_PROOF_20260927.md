# G01 PLATFORM_BASE — RED TEAM Proof Package — `http_routing`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2 of a two-stage REC + PROOF run) |
| Group / Module | G01 PLATFORM_BASE / `http_routing` |
| Date | 2026-09-27 |
| Upstream REC | `G01_RECONCILIATION/G01_HTTP_ROUTING_REC_20260927.md` (27 items: MATCH 11, CONTRADICTION 3, UNKNOWN_PENDING_PROOF 10, GAP 3) |
| Inputs (sha256 at intake) | A1 `57f9b351…a158`; A2 `6368e95b…95d7`; Lane A `9dfcb95f…c12c`; bank `b5cecfd6…11844c0` = FREEZE_W1-B08; freeze hash `b5402bab…a46a7` (DELTA-RECHECK) |
| Predeclaration | Cases file `scratchpad/rec_hrou_hedt/PROOF_CASES_PREDECLARED.md`, sha256 `a660285fc3698a57c9d13363ef551950768383a63f599450ebee106479e2d5dd`, written 2026-09-27T15:04:59Z; a stub of this file carrying the same cases was written to `G01_PROOF/` at 15:05:07Z. **First source fetch began after 15:05:07Z.** |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`; every blob verified by `git hash-object` in scratchpad (blob log `rec_hrou_hedt/blob_log.txt`, sha256 `9e124cd5701b1075b384266c388257aca0b70baef91b7dd4efd93a07d6bb556e`, 15:09:19Z) |
| Runtime device | **OFFLINE** (per controller brief). Not probed; no live request, SSRF or third-party network probing attempted |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** |

Clean-room note: results are neutral paraphrases of observed source behaviour; identifiers are evidence pointers only; no vendor code reproduced. No percentages. No Formal Coverage. No git operations on the repository. Inputs not edited. Source copies remain in scratchpad only.

## 1. Case design

- A2 proof requirements PR-HROU-01..06 → **runtime cases PC-HROU-R01..R06**, one to one; setup/expected/fail unchanged from A2 §7 (restated in §4).
- Static prediction bases → **SOURCE/CONFIG cases PC-HROU-01..10**, predeclared (hash above) and executed now.
- A static PASS confirms only that the source reads as predicted; **it is never counted as a result for any runtime case**.
- Layers: SRC = source read (module and one-hop base/web/http core); CFG = manifests/views/data; RT = runtime.

### 1.1 Predeclared static cases (verbatim intent; see cases file for full text)

| Case | Layer | Preconditions | Steps | Expected | Fail condition |
|---|---|---|---|---|---|
| PC-HROU-01 | SRC | none | Fetch 6 module files; hash | Blobs = Lane A pointers | Any mismatch |
| PC-HROU-02 | SRC | web, base, http_routing sources | (a) web debug handler; (b) error handler call; (c) render values `debug` source; (d) template gates | Chain present; no auth/group gate on (a) | Auth/group/internal gate on debug set, or handler not invoked, or template debug not from session |
| PC-HROU-03 | SRC | — | Error value preparation | Traceback computed unconditionally | Traceback only when authorised |
| PC-HROU-04 | SRC | http core | Redirect helper | Default local; strips scheme/host and leading `/`/`\`; query helper delegates | Non-local default or no stripping |
| PC-HROU-05 | SRC | web session controller | Parent logout + override | Local-default redirect; override passes value unchanged | Parent uses non-local redirect with caller value |
| PC-HROU-06 | SRC | web webclient, base loader | Translations delegation | Caller list appended; no installed/allow-list filter | Filter present |
| PC-HROU-07 | CFG | manifests | Deps; 404 refs; auto_install of html_editor/web/bus | deps `web` only; refs present; auto_install True | Dep declared, or html_editor not auto_install |
| PC-HROU-08 | SRC | base ir_http | Slug helper definitions | Base defines `_slug`/`_unslug`; module overrides | Absent in base |
| PC-HROU-09 | SRC | — | Match step route-flag gating | Language/canonical logic gated by website/multilang flags | Applied regardless of flags |
| PC-HROU-10 | SRC | — | Method gates | Canonical 301 only GET/HEAD; POST not language-redirected | Gate absent |

## 2. Blob verification (executed 2026-09-27 ~15:06 UTC)

| File | Expected (Lane A / A2) | Computed | Result |
|---|---|---|---|
| `addons/http_routing/__manifest__.py` | 9321b408… | 9321b4082f847cd079780946e3fc1335059211fb | MATCH |
| `addons/http_routing/__init__.py` | ad6393ee… | ad6393eeedf4aa6485f38cdd5ea0230cd89e205c | MATCH |
| `addons/http_routing/controllers/main.py` | a0c0d359… | a0c0d3597f0f1a9209339f58aad2b03893ec374d | MATCH |
| `addons/http_routing/models/ir_http.py` | d508ceb8… | d508ceb82321dbda60e7fcdc1554b74eb17d3c49 | MATCH |
| `addons/http_routing/models/ir_qweb.py` | 39ffe927… | 39ffe9272cdc70767cf698b9b010d36d18678a8c | MATCH |
| `addons/http_routing/views/http_routing_template.xml` | 5c5e7d00… | 5c5e7d00a6f2c38b7973de87f57e564a4e336250 | MATCH |
| `addons/web/models/ir_http.py` (one-hop) | bd03fa8e… (A2) | bd03fa8e5e43ec580a63a068121f5a292215ac66 | MATCH |
| `addons/web/controllers/session.py` (one-hop) | 2fbcfc87… (A2) | 2fbcfc872381751ac3336b2549babcca159d76cc | MATCH |
| `addons/web/controllers/webclient.py` (one-hop) | e94d5478… (A2) | e94d5478a1d0836b7b0b8057dfca1b4142cb845c | MATCH |
| `odoo/addons/base/models/ir_http.py` (one-hop) | d9d2a00b… (A2) | d9d2a00b9bc7d3e7f439b7ff4ecc46488876953a | MATCH |
| `odoo/addons/base/models/ir_qweb.py` (one-hop) | 6fbe7711… (A2) | 6fbe7711403a166dae36b4d5fe0b35499eb54659 | MATCH |
| `odoo/http.py` (one-hop) | ebfc2ac8… (A2) | ebfc2ac8d268a45aaf4b8cde8c9ce8b480d58dbb | MATCH |
| Manifests: web / bus / html_editor / website | 72f3f257… / 2fdfb246… / 6f0356c5… / aaff2bc9… (A2) | 72f3f25791583968056ca4a42ab3e9cd13db9e93 / 2fdfb24697ca638a1f1cc0ebfa1884ebdbc81d03 / 6f0356c53e7ea2902dbda178d1b33c57fe06c41c / aaff2bc93eb79dddb42b4c699b84bf4fb0813bb5 | MATCH |
| `addons/website/controllers/main.py` (new, context for `/contactus`) | — | 6aac48a846c063d4f88075d9967c1afe7cdf6328 | recorded |

## 3. Static cases — executed

| Case | Linked REC / PR | Actual observation (neutral) | Verdict |
|---|---|---|---|
| PC-HROU-01 | all | Six module blobs equal Lane A pointers (§2) | **PASS** |
| PC-HROU-02 | REC-13, REC-21 / PR-01 | (a) Web layer's debug handler sets the session debug mode from the `debug` URL query argument whenever present; the value is normalised to allowed mode names but **no authentication, group or user check** exists; it runs in pre-dispatch for every request. (b) The frontend error handler ensures a public user if none, then explicitly calls the debug handler before building error values. (c) Base template engine sets render value `debug` from the session debug mode unless minimal-context rendering is requested; the error pages are rendered via the view renderer without that flag. (d) Seven templates gate the debug block on `editable or debug` (generic HTTP error, 4xx, 400, 403, 415, 422, 500); the debug block prints error message, template-expression details and the full traceback | **PASS** |
| PC-HROU-03 | REC-13 | Error values always include a formatted traceback of the exception, computed without any debug/editable condition | **PASS** |
| PC-HROU-04 | REC-10, REC-16 / PR-04, PR-05 | Platform redirect default `local=True`; local mode drops scheme and host, strips leading slash/backslash characters and re-prefixes a single `/`; query-preserving variant delegates with the same local default; the double-slash normaliser passes `local=True` explicitly; language redirects use the query-preserving helper with default local | **PASS** |
| PC-HROU-05 | REC-16 / PR-04 | Override keeps default `/odoo` and passes the caller value unchanged to the parent; parent logs out (keeping db) and redirects via the local-default helper | **PASS** |
| PC-HROU-06 | REC-15, REC-24 / PR-03 | Public route reads frontend module list elevated and appends the caller's comma list; web handler splits it and passes it on unfiltered; only the `lang` argument is filtered to installed languages; hash memoised keyed by the frozen module set and language; base loader iterates each supplied name through the code-translation lookup. No rate-limit construct in either file | **PASS** |
| PC-HROU-07 | REC-01, REC-14, REC-19, REC-25 / PR-02 | Manifest deps `['web']`; data = template file + language views file; 404 template embeds `/html_editor/shape/http_routing/404.svg` and links `/contactus`; html_editor, web, bus manifests `auto_install: True`; website declares html_editor and http_routing as deps. `/contactus` provider not found in website `controllers/main.py` (outside the expected set; provider stays A2's attribution) | **PASS** |
| PC-HROU-08 | REC-04 / HEDT REC-04, REC-24 | Base request-dispatch model defines `_slug` (returns id as string) and `_unslug` (int parse, else none); this module overrides both with the name-slug form and adds `_unslug_url` | **PASS** |
| PC-HROU-09 | REC-03 | In the match step, when a matched endpoint is not website-flagged the module marks the request non-frontend and returns immediately, before any language resolution or redirect; frontend-multilang is derived from website flag and multilang flag (default true for `http` type) | **PASS** |
| PC-HROU-10 | REC-06, REC-09 / PR-06 | Redirect permission in the match step requires non-POST and frontend-multilang; canonical-slug 301 in pre-dispatch only for GET/HEAD | **PASS** |

### 3.1 Refinements observed (for A3; no verdict change)

- **R1** The 404 template has **no** `editable or debug` block. A plain nonexistent frontend path therefore renders no traceback even with the debug parameter; the traceback path is the 500/4xx/400/403/415/422 and generic templates. PR-HROU-01 (restated as R01 unchanged) expects "Plain: no debug block. With debug param: debug block incl. traceback" for both a nonexistent path and a 500 path — the 404 variant is expected per source to show no debug block; A3 should read R01's 404 leg with this in mind.
- **R2** The allowed-mode list in the debug handler restricts the **value**, not the **requester**.
- **R3** The 500 template is self-contained (no frontend layout) but still includes the debug block.
- **R4** `lang` on the translations route is filtered to installed languages; `mods` is not.

## 4. Runtime cases — NOT-EXECUTED (device OFFLINE; ready-to-run)

Environment for all: authorised disposable database built from the anchor commit; no third-party hosts.

| Case | = PR | Setup / action | Expected (per source) | Fail condition | Status |
|---|---|---|---|---|---|
| PC-HROU-R01 | PR-HROU-01 | Website-flagged route; anonymous client requests a nonexistent frontend path and a controlled 500 path, plain and with the debug query parameter | Plain: no debug block. Debug param: debug block with traceback on the 500 path (404 leg: see R1) | Traceback shown to anonymous FALSIFIES the safety hypothesis; no debug block on any debug-param 500 FALSIFIES the source reading | NOT-EXECUTED |
| PC-HROU-R02 | PR-HROU-02 | web (+auto-installs) + http_routing, no website; unknown frontend path | 404 with 404 template; shape image loads; contact link 404s | 418/500 or render error | NOT-EXECUTED |
| PC-HROU-R03 | PR-HROU-03 | Anonymous translations GET with installed, non-installed on-disk, random names; many distinct sets | 200 each; non-installed may return payloads; no rejection; memo growth | Names filtered/rejected | NOT-EXECUTED |
| PC-HROU-R04 | PR-HROU-04 | Authenticated logout with absolute, scheme-relative, backslash-prefixed redirect values | Location local for all | Any off-host Location | NOT-EXECUTED |
| PC-HROU-R05 | PR-HROU-05 | ≥2 frontend languages; crafted lang-prefixed paths with slash/backslash host-like segments | All 3xx local | Any off-host Location | NOT-EXECUTED |
| PC-HROU-R06 | PR-HROU-06 | Record on multilang route; GET old slug after rename, bare id; POST bare id | GET → 301 to current slug; POST no redirect | GET served on mismatch, or POST redirected | NOT-EXECUTED |

## 5. Summary of results

| Layer | Cases | PASS | FAIL | INCONCLUSIVE | NOT-EXECUTED |
|---|---|---|---|---|---|
| SOURCE / CONFIG | PC-HROU-01..10 | 10 | 0 | 0 | 0 |
| RUNTIME | PC-HROU-R01..R06 | 0 | 0 | 0 | 6 |

REC effects: CONTRADICTION C04 recorded RESOLVED against A1 (PC-08). C03 and X-HROU-01 remain CONTRADICTION (static support for A2 / confirmed source-vs-manifest). All 10 UNKNOWN_PENDING_PROOF items stay open (static basis confirmed; runtime pending). GAP items unchanged.

## 6. A3 eligibility

**Disposition: PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.**

A3 may challenge **now — claim level (yes)**:
1. REC classifications and counts (27), including the C04 resolution and the C03/X-HROU-01 open contradictions.
2. The 10 executed static cases: falsifiability of each expected/fail pair, sufficiency of observations, refinements R1–R4.
3. The escalation "anonymous debug via URL → traceback" as a **static** chain (PC-02/03), and the redirect-mitigation reasoning (PC-04/05).
4. Input integrity, blob verification, predeclaration timing, clean-room compliance, Lane B absence record.

A3 may **not** challenge at **QID level (no)**: the QID lineage (36 mapped / 4 no evidence) is **NOT A3-ELIGIBLE until canonical re-freeze of W1-B08**.

**Blocked** until runtime is available: R01..R06; closing any UNKNOWN_PENDING_PROOF item; any sufficiency judgement needing runtime. Full A3 → MASTER handoff not eligible.

## 7. Limitations

- No runtime executed; no runtime result claimed. Static PASS confirms source readings only.
- One-hop reads limited to files in §2; fallback serving, bot detection, public auth internals, language URL-code field and tests unread (REC GAP items).
- No percentages; no Formal Coverage; no git operations on the repository; inputs not edited.
