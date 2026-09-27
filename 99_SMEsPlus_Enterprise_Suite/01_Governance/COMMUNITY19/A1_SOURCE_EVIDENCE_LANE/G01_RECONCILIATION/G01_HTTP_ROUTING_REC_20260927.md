# G01 PLATFORM_BASE — RED TEAM Reconciliation (REC) — `http_routing`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of a two-stage REC + PROOF run; Stage 2 is recorded separately in `G01_PROOF/G01_HTTP_ROUTING_PROOF_20260927.md`) |
| Group / Module | G01 PLATFORM_BASE / `http_routing` |
| Date | 2026-09-27 (intake 15:04:03 UTC) |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/http_routing/` |
| Question bank | `GMVQ/G01_PLATFORM_BASE/G01_HTTP_ROUTING_GMVQ_MVQ_40_V1.00_DRAFT.md`, sha256 `b5cecfd676a6534ee4abdf0892ef9de2fdd835bc07e66da3606fbc26d11844c0` — **equals** the bank entry in `FREEZE_W1-B08.json`. Freeze hash `b5402bab2164ac8314ed4e470e747fb846c1cc63500db688209131be1dda46a7`. Gate per `QUESTION_GATE_G01_FREEZE_REPLAY_20260927.md`: **DELTA-RECHECK** (canonical replay MISMATCH; reproducible only under the manifest-declared non-canonical basis) |
| Join key | MODULE `http_routing` + QID + freeze hash above. Lineage only; **no QID is answered**. **QID lineage is NOT A3-ELIGIBLE until canonical re-freeze of W1-B08** |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (27 REC items; 3 CONTRADICTION items, of which 1 resolved against A1 at source; 10 UNKNOWN_PENDING_PROOF) |

### 0.1 Input intake (immutable; sha256 recorded at intake 2026-09-27 15:04 UTC)

Paths relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

| Input | Path | sha256 | Cross-check |
|---|---|---|---|
| A1 package | `G01_A1_PACKAGES/G01_HTTP_ROUTING_A1_PACKAGE_20260927.md` | `57f9b3513e2caf3012f346dab09c9a3b457df32bdce004d59897a719e066a158` | Equals the A1 hash recorded in the A2 header |
| A2 review | `G01_A2_REVIEWS/G01_HTTP_ROUTING_A2_REVIEW_20260927.md` | `6368e95b0bf49d6a8f698257d9e0e254675fcb3874407b70b4aaa1d2a63795d7` | "A2 VERIFIED WITH FINDINGS"; 18 VERIFIED, 2 PARTIAL (C03, C04); 6 proof requirements PR-HROU-01..06 |
| Lane A packet | `G01_LANE_A_PASS1/G01_HTTP_ROUTING_LANE_A_PASS1_20260927.md` | `9dfcb95f2521ec078ee425e4755054844d54eb3e4233b8d83c04b03f9bfa612c` | Equals the hash recorded in A1 and A2 headers |
| Question bank | see header | `b5cecfd6…11844c0` | Equals FREEZE_W1-B08 `bank_files` entry |
| FREEZE manifest | `../GMVQ/G01_PLATFORM_BASE/FREEZE_W1-B08.json` | `06ccf568b253bba053dd66841d590b8c46079633aeea9a918d8cd7a6e7f98a35` | freeze_hash `b5402bab…a46a7`; basis declared as batch/module/bank/standard/review (non-canonical) |
| Freeze replay gate | `../GMVQ/G01_PLATFORM_BASE/QUESTION_GATE_G01_FREEZE_REPLAY_20260927.md` | `52430ca13a7d59f1a979f213879959133d48332be72f205c2fb9a31db60810e2` | W1-B08 = DELTA-RECHECK |

Inputs were re-hashed at close of run; all unchanged.

### 0.2 Lane B evidence-pool search (recorded)

- Command: `grep -ril http_routing /home/user/AI-Collaboration-Hub/99_SMEsPlus_Enterprise_Suite` → 27 files: A1/A2/Lane A artifacts under `A1_SOURCE_EVIDENCE_LANE` (10), GMVQ bank/freeze/status files (10), one TEAM_A architecture file, two inventory CSVs under `07_Output_From_AI`, four `V2.0/THAI` handoff documents. None is a runtime observation.
- Those hits filtered for `lane_b|laneb|lane b|gemini|evidence_pool|evidence pool` matched only A1/A2/Lane A packets (statements "Lane B: none"/"did not use Lane B") and a GMVQ checkpoint rule text — no Lane B evidence content.
- `find` for names `*lane_b*`, `*gemini*`, `*evidence_pool*` → **no files**.
- Conclusion: **no Lane B / Gemini evidence pool exists for `http_routing`.** Absence is not failure; every Lane B cell is UNCORROBORATED or NOT_APPLICABLE.

Clean-room note: neutral WHAT/WHY/RISK paraphrase only; identifiers are evidence pointers. No vendor code reproduced; nothing recommends reusing vendor schema, ORM, workflow, UI or naming. No percentages. No Formal Coverage claim. No git operations. Inputs not edited.

## 1. Classification rules (predeclared)

- **MATCH**: A1 and A2 agree and the source re-read supports the claim; runtime corroboration optional.
- **CONTRADICTION**: A1 vs A2 disagreement (A2 PARTIAL/NOT_VERIFIED), or source vs declared intent/manifest. Both statements are preserved. "RESOLVED against A1" is recorded only where the disagreement is a pure source-existence fact fully decided by an executed static case.
- **UNKNOWN_PENDING_PROOF**: A1/A2 agree at source level (or A2 adds a source-read omission) but the claim or its risk is inherently runtime.
- **GAP**: evidence missing and no static or runtime case in this scope settles it.
- **Lane B**: UNCORROBORATED (request-time behaviour) or NOT_APPLICABLE (declarative/structural or source-only gap). Never FAIL.
- **Scope**: A1 C01–C18, X-HROU-01/02; A2 omissions O1–O5; residual A1 evidence gaps not absorbed by a claim (EG1-residual, EG4). EG2→C15, EG3→C14/X-HROU-01. CRQ-HROU-06 (company-scoped language policy; A2 OUT_OF_SCOPE design) folded into C18 and routed to design.

## 2. Reconciliation table

PC = proof case in the PROOF package (static PC-HROU-01..10 executed; runtime PC-HROU-R01..R06 NOT-EXECUTED).

| REC ID | Item | A1 (claim / conf.) | A2 verdict | REC class | Basis | Lane B | Proof link | QID lineage (`http_routing`; NOT A3-ELIGIBLE until re-freeze) |
|---|---|---|---|---|---|---|---|---|
| REC-HROU-01 | C01 | Hidden module, dep `web` only, post-init hook, 2 view files / HIGH | VERIFIED | MATCH | Manifest re-read (PC-07) | NOT_APPLICABLE | PC-07 | — |
| REC-HROU-02 | C02 | Post-init hook clears frontend/multilang flags / MED | VERIFIED | MATCH | Blob verified (PC-01) | NOT_APPLICABLE | PC-01 | Q030, Q039 |
| REC-HROU-03 | C03 | No persistent model; RISK "global to every request, not opt-in per route" / MED | **PARTIAL** — behaviour opt-in per route flag | **CONTRADICTION** (A1 vs A2) | Source supports A2: non-website endpoints return from match before any language/canonical logic (PC-09 PASS). Both statements preserved; open for A3 | NOT_APPLICABLE | PC-09 | Q029 |
| REC-HROU-04 | C04 | Slug/unslug "defined here and consumed by other modules" / HIGH | **PARTIAL** — base already defines id-only helpers; module overrides | **CONTRADICTION — RESOLVED against A1** (existence fact) | Base platform layer defines `_slug`/`_unslug` returning id-only form; this module overrides with name-slug (PC-08 PASS). A1 ownership wording not supported; format facts (name+id, id fallback, error on missing id) stand | NOT_APPLICABLE | PC-08 | Q001, Q002, Q003 |
| REC-HROU-05 | C05 | Negative id retried as absolute value / MED | VERIFIED | MATCH | A1/A2 agree | NOT_APPLICABLE | PC-01 | Q002, Q004 |
| REC-HROU-06 | C06 | Canonical 301 on frontend multilang GET/HEAD / HIGH | VERIFIED | UNKNOWN_PENDING_PROOF | Method gate GET/HEAD confirmed (PC-10); rename/old-slug behaviour is runtime | UNCORROBORATED | PC-10; R06 | Q001, Q005, Q021, Q022 |
| REC-HROU-07 | C07 | Lang precedence URL > cookie > context > default, under temporary public auth / MED | VERIFIED | MATCH | A1/A2 agree | UNCORROBORATED | — | Q005, Q011, Q012 |
| REC-HROU-08 | C08 | Default lang via elevated default read else first active / HIGH | VERIFIED | MATCH | A1/A2 agree | NOT_APPLICABLE | — | Q011 |
| REC-HROU-09 | C09 | Nine routing cases; bots no redirect; POST never redirected / MED | VERIFIED (bot also forces default lang) | UNKNOWN_PENDING_PROOF | POST exclusion confirmed statically (PC-10); per-case effects runtime | UNCORROBORATED | PC-10; R06 | Q013–Q018, Q022 |
| REC-HROU-10 | C10 | Double-slash 301 local; others via query-preserving helper; open-redirect safety unread / HIGH | VERIFIED — A2 closes RISK (helper local by default) | UNKNOWN_PENDING_PROOF | Helper default local mode strips scheme/host and leading slash/backslash (PC-04 PASS); Location headers are runtime | UNCORROBORATED | PC-04; R05 | Q007, Q009, Q013, Q023 |
| REC-HROU-11 | C11 | `/static/`, `/web/` never multilang / MED | VERIFIED (contains `/static/` anywhere) | MATCH | A2 refinement is narrower wording, not disagreement | NOT_APPLICABLE | — | Q010 |
| REC-HROU-12 | C12 | Frontend error handling: rollback, mapping, 404/403 fallback, per-code template, 418 on render failure / HIGH | VERIFIED | MATCH | Error path re-read in PC-02/03 | UNCORROBORATED | PC-02, PC-03 | Q031, Q032, Q033, Q034, Q036, Q037 |
| REC-HROU-13 | C13 | Debug block when `editable or debug`; anonymous exposure depends on upstream grant / HIGH | VERIFIED — **risk escalated**: debug settable from URL by any requester | UNKNOWN_PENDING_PROOF | Static chain confirmed end-to-end (PC-02 PASS, PC-03 PASS): URL parameter → session debug with no requester check → error handler invokes it → render values take debug from session → debug block with traceback. Refinement R1: the 404 template has **no** debug block; the six other error templates and the generic fallback do. Runtime disclosure pending | UNCORROBORATED | PC-02, PC-03; R01 | Q035, Q037 |
| REC-HROU-14 | C14 | 404 embeds html_editor shape image and `/contactus`; neither provider declared / HIGH | VERIFIED | UNKNOWN_PENDING_PROOF | References and manifests confirmed (PC-07); rendered effect without providers is runtime. (REC sets Lane B UNCORROBORATED; A2 table had NOT_APPLICABLE) | UNCORROBORATED | PC-07; R02 | Q032, Q036 |
| REC-HROU-15 | C15 | Public translations route appends caller module names / HIGH | VERIFIED — no filter in delegated handler/loader; memo keyed by caller set | UNKNOWN_PENDING_PROOF | No module-name filter at source (PC-06 PASS; only `lang` is filtered to installed languages). Payload/cache effects runtime. (Lane B UNCORROBORATED; A2 had NOT_APPLICABLE) | UNCORROBORATED | PC-06; R03 | Q026, Q027, Q040 |
| REC-HROU-16 | C16 | Logout override default `/odoo`; sanitation parent-owned / HIGH | VERIFIED — CRQ resolved (local helper) | UNKNOWN_PENDING_PROOF | Parent logs out then redirects via local-default helper (PC-05 PASS); Location header runtime | UNCORROBORATED | PC-05, PC-04; R04 | Q028 |
| REC-HROU-17 | C17 | Rewrite lookup ORM-cached; reroute limit 10 / HIGH | VERIFIED | MATCH | A1/A2 agree | NOT_APPLICABLE | PC-01 | Q019, Q038 |
| REC-HROU-18 | C18 (+CRQ-06) | No groups/ACL/rules; no company dimension / MED | VERIFIED | MATCH | A1/A2 agree; CRQ-HROU-06 is a design question routed to SaaS/functional design | NOT_APPLICABLE | — | Q040 |
| REC-HROU-19 | X-HROU-01 | Declared deps `web` vs html_editor/`/contactus` references / CONFIRMED | VERIFIED (impact qualified by auto-install) | **CONTRADICTION** (source vs manifest) | Confirmed (PC-07): deps `web` only; html_editor, web, bus auto-install. `/contactus` provider not located in website `controllers/main.py` at anchor — provider attribution stays A2's, unverified here | NOT_APPLICABLE | PC-07; R02 | Q036 |
| REC-HROU-20 | X-HROU-02 | Template-engine warning vs backend passthrough / CANDIDATE | VERIFIED as non-contradiction | MATCH | Both agree it is not a conflict | NOT_APPLICABLE | — | Q029, Q030 |
| REC-HROU-21 | O1 | (not stated) | Error handler calls debug handler itself | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-02 step b) | UNCORROBORATED | PC-02; R01 | Q035 |
| REC-HROU-22 | O2 | (not stated) | Language cookie (re)set by any link | GAP | A2 source statement; no static or runtime case defined in this proof scope | UNCORROBORATED | — | Q024 |
| REC-HROU-23 | O3 | (not stated) | `editable` supplied by other modules; html_editor injects from query string; reach into error values unread | UNKNOWN_PENDING_PROOF | Injection into request context confirmed (HEDT PC-HEDT-10); whether it reaches error-template values is unread → runtime | UNCORROBORATED | PC-HEDT-10; R01, PC-HEDT-R09 | Q035 |
| REC-HROU-24 | O4 | (not stated) | No rate limit on translations route | UNKNOWN_PENDING_PROOF | No throttle in module/handler read (PC-06); infra unknown | UNCORROBORATED | PC-06; R03 | Q026, Q027 |
| REC-HROU-25 | O5 | (not stated) | html_editor/web/bus auto-install | MATCH | Manifests confirm (PC-07) | NOT_APPLICABLE | PC-07 | — |
| REC-HROU-26 | EG1-residual | Base/web internals: fallback serving, bot detection, public auth method, language URL-code field | Partially settled (debug, redirect, logout) | GAP | Remaining internals unread in this lineage | NOT_APPLICABLE | — | Q015, Q034 |
| REC-HROU-27 | EG4 | Tests not reviewed | — | GAP | Not read | NOT_APPLICABLE | — | — |

### 2.1 Class counts

| Class | Count | Items |
|---|---|---|
| MATCH | 11 | C01, C02, C05, C07, C08, C11, C12, C17, C18, X-HROU-02, O5 |
| CONTRADICTION | 3 | C03 (A1 vs A2; open), C04 (A1 vs A2; **RESOLVED against A1**), X-HROU-01 (source vs manifest) |
| UNKNOWN_PENDING_PROOF | 10 | C06, C09, C10, C13, C14, C15, C16, O1, O3, O4 |
| GAP | 3 | O2, EG1-residual, EG4 |
| **Total** | **27** | 18 A1 claims + 2 A1 contradictions + 5 A2 omissions + 2 carried gaps |

Lane B: UNCORROBORATED 13 (C06, C07, C09, C10, C12, C13, C14, C15, C16, O1, O2, O3, O4); NOT_APPLICABLE 14. No FAIL for absence.

### 2.2 Contradiction handling (both sources preserved)

- **C04 — RESOLVED against A1.** A1: helpers "defined here". A2: base defines id-only helpers; this module overrides. Executed static case PC-HROU-08 finds both definitions (base returns id-only; this module adds the name slug). A1's format facts stand; its ownership statement does not. Cross-reference: HEDT C04 / X-HEDT-03 resolved on the same evidence.
- **C03 — open.** A2's narrower scope is supported by PC-HROU-09; REC does not rewrite A1; A3 reviews.
- **X-HROU-01 — confirmed contradiction between source references and manifest.** Practical impact (broken image vs render failure; dead link) needs runtime (R02).

### 2.3 Escalation carried (A2)

Anonymous debug-mode enable via URL parameter → traceback on frontend error pages: static chain complete (PC-HROU-02/03 PASS). Not a runtime finding. Note R1 for the runtime case: a plain nonexistent-path 404 renders the 404 template, which carries no debug block; the traceback exposure path is the 500/4xx/403/400/415/422/generic templates.

## 3. QID lineage map (frozen bank W1-B08; lineage only — NOT A3-ELIGIBLE until canonical re-freeze)

Join key: MODULE `http_routing` + QID + freeze hash `b5402bab2164ac8314ed4e470e747fb846c1cc63500db688209131be1dda46a7` (DELTA-RECHECK basis). A mapping means topical relevance only; it does not answer the QID or satisfy its disconfirming observation.

| QID | Topic (paraphrased) | Mapped REC items |
|---|---|---|
| Q001 | Durable identity across rename | REC-04, REC-06 |
| Q002 | Slug resolves exact record | REC-04, REC-05 |
| Q003 | Malformed slug fails safely | REC-04 |
| Q004 | Negative ids deterministic | REC-05 |
| Q005 | Localisation keeps identity | REC-06, REC-07 |
| Q007 | Query params preserved | REC-10 |
| Q009 | External URLs not rewritten | REC-10 |
| Q010 | Static/backend paths excluded | REC-11 |
| Q011 | Language precedence | REC-07, REC-08 |
| Q012 | Near-match locale | REC-07 |
| Q013 | Missing prefix redirect | REC-09, REC-10 |
| Q014–Q018 | POST, bot, default prefix, alias, trailing slash | REC-09 |
| Q019 | Reroute terminates | REC-17 |
| Q021 | Numeric → canonical slug | REC-06 |
| Q022 | Unsafe methods not canonicalised | REC-06, REC-09 |
| Q023 | Double-slash local | REC-10 |
| Q024 | Language cookie | REC-22 |
| Q026, Q027 | Translation module boundary | REC-15, REC-24 |
| Q028 | Logout destination | REC-16 |
| Q029 | Template helpers context | REC-03, REC-20 |
| Q030 | Stale frontend state | REC-02, REC-20 |
| Q031 | Status per exception | REC-12 |
| Q032 | Nested 404 → 500 | REC-12, REC-14 |
| Q033 | Rollback before fallback | REC-12 |
| Q034 | Fallback metadata | REC-12, REC-26 |
| Q035 | Tracebacks only for authorised | REC-13, REC-21, REC-23 |
| Q036 | Minimal 500 render | REC-12, REC-14, REC-19 |
| Q037 | Bounded fallback render | REC-12, REC-13 |
| Q038 | Deterministic rewrite inspection | REC-17 |
| Q039 | Init clears stale state | REC-02 |
| Q040 | Bound to active DB / customer | REC-15, REC-18 |

**Mapped: 36 QIDs. No evidence yet: 4** — Q006 (localisation fallback without restricted metadata), Q008 (canonical-domain query exclusion), Q020 (language set before model args), Q025 (frontend session info). No mapping answers a QID.

## 4. Handoff

- To PROOF (Stage 2, separate record): `G01_PROOF/G01_HTTP_ROUTING_PROOF_20260927.md`.
- Proof addresses the 10 UNKNOWN_PENDING_PROOF and 3 CONTRADICTION items. The 3 GAP items are carried forward.

## 5. Limitations

- REC used only the immutable inputs in 0.1 plus static proof results from Stage 2 for classification support. No runtime evidence exists.
- QID mapping is controller-judged topical lineage, not coverage; QID lineage is NOT A3-ELIGIBLE until W1-B08 is canonically re-frozen.
- No percentages; no Formal Coverage; no git operations; inputs not edited.
