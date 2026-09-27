# G01 PLATFORM_BASE — RED TEAM Reconciliation (REC) — `html_editor`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of a two-stage REC + PROOF run; Stage 2 is recorded separately in `G01_PROOF/G01_HTML_EDITOR_PROOF_20260927.md`) |
| Group / Module | G01 PLATFORM_BASE / `html_editor` |
| Date | 2026-09-27 (intake 15:04:03 UTC) |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/html_editor/` (+ `addons/mail/tools/link_preview.py` for the SSRF settlement) |
| Question bank | `GMVQ/G01_PLATFORM_BASE/G01_HTML_EDITOR_GMVQ_MVQ_40_V1.00_DRAFT.md`, sha256 `a421e3177abd55333a3647ead363f5e29389223581755b76273cdb84106ba619` — **equals** the bank entry in `FREEZE_W1-B07.json`. Freeze hash `ea24b270cf375fc108735ca6e15d68500dd9b5cfb69e849bd2eb673a232d332e`. Gate: **DELTA-RECHECK** (canonical replay MISMATCH; reproducible under the manifest-declared non-canonical basis) |
| Join key | MODULE `html_editor` + QID + freeze hash above. Lineage only; **no QID is answered**. **QID lineage is NOT A3-ELIGIBLE until canonical re-freeze of W1-B07** |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (39 REC items; 6 CONTRADICTION items, of which 2 resolved against A1 at source; 11 UNKNOWN_PENDING_PROOF) |

### 0.1 Input intake (immutable; sha256 recorded at intake 2026-09-27 15:04 UTC)

Paths relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

| Input | Path | sha256 | Cross-check |
|---|---|---|---|
| A1 package | `G01_A1_PACKAGES/G01_HTML_EDITOR_A1_PACKAGE_20260927.md` | `e96156fa82878ab6580ea08c74e1dc07a1b8be86c0283ade761f53fcaa81a1c4` | Equals the A1 hash recorded in the A2 header |
| A2 review | `G01_A2_REVIEWS/G01_HTML_EDITOR_A2_REVIEW_20260927.md` | `6e0784636cfda87a5e7f86e343627e989ccd88a6c5db21e08f7cd9963a3fca75` | "A2 VERIFIED WITH FINDINGS (PARTIAL)"; 22 VERIFIED, 1 PARTIAL (C02), 2 NOT_VERIFIED (C04, X-HEDT-03); 10 proof requirements PR-HEDT-01..10; CRQ-HEDT-01 SSRF resolved at source (fetcher blob 18515419…) |
| Lane A packet | `G01_LANE_A_PASS1/G01_HTML_EDITOR_LANE_A_PASS1_20260927.md` | `e0e59e77ce408839e7a0bb64197443c0f9ca8a68d394329adc92bca7236df10e` | Equals the hash in A1 and A2 headers |
| Question bank | see header | `a421e317…ba619` | Equals FREEZE_W1-B07 `bank_files` entry |
| FREEZE manifest | `../GMVQ/G01_PLATFORM_BASE/FREEZE_W1-B07.json` | `c2bef1c1599818e881b429fa163e5a221e6de2f957e2b898dc50010b1f826416` | freeze_hash `ea24b270…d332e`; declared basis non-canonical |
| Freeze replay gate | `../GMVQ/G01_PLATFORM_BASE/QUESTION_GATE_G01_FREEZE_REPLAY_20260927.md` | `52430ca13a7d59f1a979f213879959133d48332be72f205c2fb9a31db60810e2` | W1-B07 = DELTA-RECHECK |
| Cross-module (read only) | `G01_RECONCILIATION/G01_HTTP_ROUTING_REC_20260927.md` (this run) | — | Shared evidence for C04 / X-HEDT-03 (PC-HROU-08) |

Inputs were re-hashed at close of run; all unchanged.

### 0.2 Lane B evidence-pool search (recorded)

- Command: `grep -ril html_editor /home/user/AI-Collaboration-Hub/99_SMEsPlus_Enterprise_Suite` → 45 files: A1/A2/Lane A artifacts (15, incl. html_builder, web_unsplash, mail packages that reference html_editor), GMVQ files (10), `02_Functional_Design` iTEST02 FK/sensitive-column inventory CSVs (4), TEAM_A architecture (3), `07_Output_From_AI` CSVs (2), `V2.0/THAI` handoff docs (11). None is a runtime observation.
- Filter `lane_b|laneb|lane b|gemini|evidence_pool|evidence pool` over those hits matched only A1/A2/Lane A packets ("Lane B: none" statements) and a GMVQ checkpoint rule text.
- `find` for `*lane_b*`, `*gemini*`, `*evidence_pool*` → **no files**.
- Conclusion: **no Lane B / Gemini evidence pool exists for `html_editor`.** Every Lane B cell is UNCORROBORATED or NOT_APPLICABLE; never FAIL.

Clean-room note: neutral WHAT/WHY/RISK paraphrase only; identifiers are evidence pointers. No vendor code reproduced; no reuse of vendor schema, ORM, workflow, UI or naming recommended. No percentages. No Formal Coverage. No git operations. Inputs not edited.

## 1. Classification rules (predeclared)

Same rules as the `http_routing` REC of this run: MATCH / CONTRADICTION (A1 vs A2, or source vs declared intent/manifest; "RESOLVED against A1" only for a pure source-existence fact decided by an executed static case) / UNKNOWN_PENDING_PROOF (runtime-inherent) / GAP (no case in scope). Lane B UNCORROBORATED or NOT_APPLICABLE, never FAIL.

Scope: A1 C01–C21, X-HEDT-01..04; A2 omissions O1–O7; A2 semantic findings that add a claim not carried by any A1 item (SF-HEDT-02 link-preview worker exhaustion, SF-HEDT-06 query-string editor flags) and CRQ-HEDT-02 (rate limiting, has its own PR); residual A1 gaps EG1, EG3, EG6, EG7. Folded: EG2→C05, EG4→SF-06, EG5→C02, SF-01→C05, SF-03→C08/C10, SF-04 and CRQ-HEDT-08 (UUID policy, OUT_OF_SCOPE)→C20 (policy routed to privacy/design), SF-05→O2, SF-07→C15.

## 2. Reconciliation table

PC = proof case (static PC-HEDT-01..12 executed; runtime PC-HEDT-R01..R10 NOT-EXECUTED).

| REC ID | Item | A1 (claim / conf.) | A2 verdict | REC class | Basis | Lane B | Proof link | QID lineage (`html_editor`; NOT A3-ELIGIBLE until re-freeze) |
|---|---|---|---|---|---|---|---|---|
| REC-HEDT-01 | C01 | Hidden, auto-install; deps base/bus/web; ACL-only data / HIGH | VERIFIED | MATCH | Manifest re-read (PC-05) | NOT_APPLICABLE | PC-05 | — |
| REC-HEDT-02 | C02 (+EG5) | Undeclared mail/iap imports + ICE model call; "may fail at import on DB lacking mail/iap" / HIGH | **PARTIAL** — reverse dependency (mail→html_editor) makes the gap structural; import failure not established (import resolves by addons path, not install state) | **CONTRADICTION** (A1 vs A2; open) | Module-level imports from the mail and iap tool packages and the mail ICE-server model call confirmed (PC-05). Addon imports resolve through a namespace package whose search path is the configured addons path, with no install-state gate (PC-07). Supports A2 at source; load behaviour decided only by runtime R06 | NOT_APPLICABLE | PC-05, PC-07; R06 | — |
| REC-HEDT-03 | C03 | Website model browse + `website.*` footer keys; website undeclared / HIGH | VERIFIED | MATCH | Custom-snippet naming browses the website model; four website footer keys named (PC-05) | NOT_APPLICABLE | PC-05; R06 | — |
| REC-HEDT-04 | C04 | Slug/unslug helpers "defined in http_routing, which is not declared" / HIGH | **NOT_VERIFIED** | **CONTRADICTION — RESOLVED against A1** | Calls go through the platform request-dispatch model; base defines id-only `_slug`/`_unslug` (PC-HEDT-06, PC-HROU-08 PASS). No missing http_routing dependency. Residual behaviour (id-only illustration URLs without http_routing) → R06 | NOT_APPLICABLE | PC-06, PC-HROU-08; R06 | — |
| REC-HEDT-05 | C05 (+EG2, SF-01) | Public POST link-preview passes caller URL to mail fetcher; safeguards unread / HIGH | VERIFIED — **CRQ-01 resolved at source: no safeguards** | UNKNOWN_PENDING_PROOF | Fetcher (blob 18515419…): no host/IP/private-range/loopback/metadata block, redirects followed, 3 s per-operation timeout, streamed read with no byte cap until head-close marker, metadata returned to anonymous caller (PC-02, PC-03 PASS). Exploitability/egress controls runtime only | UNCORROBORATED | PC-02, PC-03; R01, R02 | Q017, Q018, Q019 |
| REC-HEDT-06 | C06 | HEAD to user URL, 10 s / HIGH | VERIFIED (HEAD precedes rights-bypass decision) | MATCH | A1/A2 agree; CRQ-03 confirmed no host list | UNCORROBORATED | — | Q028 |
| REC-HEDT-07 | C07 | Converter GETs non-local `src` on save, 2.5 s / HIGH | VERIFIED | MATCH | A1/A2 agree | UNCORROBORATED | — | — |
| REC-HEDT-08 | C08 (+SF-03) | Media library: no timeouts, superuser public create, remote MIME / HIGH | VERIFIED | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-08): POST and per-URL GET without timeout; superuser create; MIME from remote header; no origin check | UNCORROBORATED | PC-08; R04 | Q028 |
| REC-HEDT-09 | C09 | Vimeo oEmbed over plain HTTP; thumbnail URL from response fetched / HIGH | VERIFIED (reachability only via downstream callers) | UNKNOWN_PENDING_PROOF | Confirmed; no in-module caller (PC-09) | UNCORROBORATED | PC-09; R08 | — |
| REC-HEDT-10 | C10 (+SF-03) | modify_image: read src / write target, elevated copy, superuser MIME reset / HIGH | VERIFIED — risk sharpened: caller bytes + SVG in allow-list | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-04 PASS): caller-supplied bytes and MIME accepted when MIME is in the image allow-list, which includes SVG; elevated copy; superuser MIME write when the stored type was downgraded to plain text. Core downgrade itself is base behaviour → runtime | UNCORROBORATED | PC-04; R05 | Q028, Q029, Q030 |
| REC-HEDT-11 | C11 | Other elevated paths / HIGH | VERIFIED | MATCH | A1/A2 agree | NOT_APPLICABLE | — | Q018 |
| REC-HEDT-12 | C12 | Exactly three public routes / HIGH | VERIFIED | MATCH | Route decorators re-listed (PC-05/03) | NOT_APPLICABLE | PC-03 | — |
| REC-HEDT-13 | C13 | Internal preview returns raw exception text / HIGH | VERIFIED | MATCH | Confirmed (PC-11) | UNCORROBORATED | PC-11 | Q018, Q019 |
| REC-HEDT-14 | C14 | Base64 type allow-list only when image-flagged; no byte cap / MED | VERIFIED | MATCH | A1/A2 agree | NOT_APPLICABLE | — | Q030 |
| REC-HEDT-15 | C15 (+SF-07) | Removal blocked while view arch references URL / MED | VERIFIED (business qualifier: views only) | MATCH | Claim technically agreed; A2's BR3 qualifier preserved | NOT_APPLICABLE | — | Q028 |
| REC-HEDT-16 | C16 | Shape colour/params restrictions / MED | VERIFIED | MATCH | A1/A2 agree | NOT_APPLICABLE | — | — |
| REC-HEDT-17 | C17 | History mixin: sanitize required, cap 300, user id+name / MED | VERIFIED | MATCH | A1/A2 agree | NOT_APPLICABLE | — | Q004 |
| REC-HEDT-18 | C18 | Sanitize-override edit-prevention marker / MED | VERIFIED (enforcement client-side, unread) | MATCH | A1/A2 agree | UNCORROBORATED | — | Q001, Q004, Q005, Q007 |
| REC-HEDT-19 | C19 | Collaborative divergence check; channel access checks / MED | VERIFIED | MATCH | A1/A2 agree | UNCORROBORATED | — | Q036, Q037 |
| REC-HEDT-20 | C20 (+SF-04, CRQ-08) | Database UUID sent to media/AI endpoints / HIGH | VERIFIED | UNKNOWN_PENDING_PROOF | UUID in media search, media download and AI payloads (PC-12). Egress observation runtime; acceptability is policy (routed to privacy/design) | UNCORROBORATED | PC-12; R07 | Q040 |
| REC-HEDT-21 | C21 | Two test models in production path, system ACL / MED | VERIFIED | MATCH | A1/A2 agree | NOT_APPLICABLE | PC-01 | — |
| REC-HEDT-22 | X-HEDT-01 | Declared deps vs mail/iap imports + ICE call / CONFIRMED | VERIFIED (qualified: structural) | **CONTRADICTION** (source vs manifest) | Confirmed (PC-05); mail declares html_editor as a dependency (reverse edge); iap declares web/base_setup and is auto-install | NOT_APPLICABLE | PC-05; R06 | — |
| REC-HEDT-23 | X-HEDT-02 | Declared deps vs website model/keys / CONFIRMED | VERIFIED | **CONTRADICTION** (source vs manifest) | Confirmed (PC-05); website declares html_editor and http_routing as dependencies (reverse edge) | NOT_APPLICABLE | PC-05; R06 | — |
| REC-HEDT-24 | X-HEDT-03 | Declared deps vs http_routing slug helpers / CONFIRMED | **NOT_VERIFIED** | **CONTRADICTION — RESOLVED against A1** | As REC-HEDT-04: helpers exist in base (PC-06, PC-HROU-08). A1's contradiction does not hold | NOT_APPLICABLE | PC-06, PC-HROU-08 | — |
| REC-HEDT-25 | X-HEDT-04 | "Whitelisted origin" comment vs no origin check / CONFIRMED | VERIFIED | **CONTRADICTION** (source comment vs code) | No origin check before superuser create (PC-08); trust reduces to the configured endpoint and transport | NOT_APPLICABLE | PC-08; R04 | Q028 |
| REC-HEDT-26 | O1 | (not stated) | Internal preview falls back to the external fetcher for non-record URLs | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-03). No dedicated runtime case; R01 setup reusable with an authenticated client (A3 may require a dedicated case) | UNCORROBORATED | PC-03; R01 (setup) | Q018 |
| REC-HEDT-27 | O2 (+SF-05) | (not stated) | mail→html_editor and website→html_editor reverse deps | MATCH | Manifests confirm (PC-05) | NOT_APPLICABLE | PC-05 | — |
| REC-HEDT-28 | O3 | (not stated) | html_editor, web, bus auto-install | MATCH | Manifests confirm (PC-05, PC-HROU-07) | NOT_APPLICABLE | PC-05 | — |
| REC-HEDT-29 | O4 | (not stated) | Public image-in-shape route resolves record image by key; access delegated | GAP | Binary-service access rules unread; no case in scope | UNCORROBORATED | — | Q028 |
| REC-HEDT-30 | O5 | (not stated) | Converter reads `/web/image/...` binaries under user rights at save | GAP | Not re-read in this proof scope; no case | UNCORROBORATED | — | Q028 |
| REC-HEDT-31 | O6 | (not stated) | Media search forwards arbitrary caller params + UUID | UNKNOWN_PENDING_PROOF | Caller keyword params forwarded with UUID added (PC-12) | UNCORROBORATED | PC-12; R07 | Q040 |
| REC-HEDT-32 | O7 | (not stated) | Vimeo request embeds caller URL unencoded | UNKNOWN_PENDING_PROOF | Confirmed (PC-09) | UNCORROBORATED | PC-09; R08 | — |
| REC-HEDT-33 | SF-HEDT-02 | (C08 partial) | Worker exhaustion: link preview per-op timeout + unbounded body; media download no timeout | UNKNOWN_PENDING_PROOF | No byte cap and per-operation timeout confirmed (PC-02) | UNCORROBORATED | PC-02, PC-08; R03, R04 | Q019 |
| REC-HEDT-34 | SF-HEDT-06 (+EG4) | EG4 consumers of query-string flags unread | Editable/translation flags injected from query string for any requester | UNKNOWN_PENDING_PROOF | Injection into request context without requester check confirmed (PC-10); consumers unread | UNCORROBORATED | PC-10; R09 | Q001 |
| REC-HEDT-35 | CRQ-HEDT-02 | Rate limiting on public preview? | No throttle in module or fetcher | UNKNOWN_PENDING_PROOF | Source shows no throttle (PC-02/03); infra unknown | UNCORROBORATED | R10 | Q018 |
| REC-HEDT-36 | EG1 | Core sanitiser policy unread | — | GAP | Not read | NOT_APPLICABLE | — | Q004, Q005 |
| REC-HEDT-37 | EG3 | Core upload size/resolution caps unread | — | GAP | Not read | NOT_APPLICABLE | — | Q030 |
| REC-HEDT-38 | EG6 | JS globs / DOMPurify not studied | — | GAP | JS out of scope | NOT_APPLICABLE | — | — |
| REC-HEDT-39 | EG7 | Tests not read | — | GAP | Not read | NOT_APPLICABLE | — | — |

### 2.1 Class counts

| Class | Count | Items |
|---|---|---|
| MATCH | 16 | C01, C03, C06, C07, C11, C12, C13, C14, C15, C16, C17, C18, C19, C21, O2, O3 |
| CONTRADICTION | 6 | C02 (A1 vs A2; open), **C04 (RESOLVED against A1)**, X-HEDT-01 (source vs manifest), X-HEDT-02 (source vs manifest), **X-HEDT-03 (RESOLVED against A1)**, X-HEDT-04 (comment vs code) |
| UNKNOWN_PENDING_PROOF | 11 | C05, C08, C09, C10, C20, O1, O6, O7, SF-02, SF-06, CRQ-02 |
| GAP | 6 | O4, O5, EG1, EG3, EG6, EG7 |
| **Total** | **39** | 21 A1 claims + 4 A1 contradictions + 7 A2 omissions + 3 A2 findings/CRQ + 4 carried gaps |

Lane B: UNCORROBORATED 18 (C05, C06, C07, C08, C09, C10, C13, C18, C19, C20, O1, O4, O5, O6, O7, SF-02, SF-06, CRQ-02); NOT_APPLICABLE 21. No FAIL for absence.

### 2.2 Contradiction handling (both sources preserved)

- **C04 and X-HEDT-03 — RESOLVED against A1.** A1: undeclared dependency on http_routing for slug helpers. A2: helpers exist in base. PC-HEDT-06 and PC-HROU-08 show the calls resolve through the platform model and base defines id-only helpers. A1's package is not rewritten; its statement is recorded as not supported.
- **C02 — open.** A1's failure mode ("may fail at import") vs A2 (structural reverse dependency; import resolves by code presence). Static cases support A2 at source (PC-05, PC-07); runtime R06 decides.
- **X-HEDT-01, X-HEDT-02** — genuine manifest-vs-source contradictions; A2 qualifies them as intentional inversion (reverse dependents), which REC records without judging it a defect.
- **X-HEDT-04** — source comment vs code; practical effect depends on who controls the configured endpoint (R04).

### 2.3 Escalations carried (A2)

- SSRF: link_preview fetcher has no host/IP/private-range blocking, follows redirects, 3 s per-operation timeout, unbounded body read, metadata returned to the anonymous caller; internal preview falls back to the same fetch (REC-05, REC-26, REC-33). Static only; no live probe was made.
- modify_image: a non-admin with write access to the target can store own bytes typed as SVG (REC-10). Static only.

## 3. QID lineage map (frozen bank W1-B07; lineage only — NOT A3-ELIGIBLE until canonical re-freeze)

Join key: MODULE `html_editor` + QID + freeze hash `ea24b270cf375fc108735ca6e15d68500dd9b5cfb69e849bd2eb673a232d332e` (DELTA-RECHECK basis). Mapping is topical relevance only; no QID answered.

| QID | Topic (paraphrased) | Mapped REC items |
|---|---|---|
| Q001 | Edit mode respects editable boundaries | REC-18, REC-34 |
| Q004 | Untrusted HTML sanitised before durable | REC-17, REC-18, REC-36 |
| Q005 | Sanitisation preserves allowed content | REC-18, REC-36 |
| Q007 | Protected content not mutable | REC-18 |
| Q017 | Link creation valid destination | REC-05 |
| Q018 | Link preview does not expose restricted content | REC-05, REC-11, REC-13, REC-26, REC-35 |
| Q019 | Metadata fetch failure does not block editing | REC-05, REC-13, REC-33 |
| Q028 | Image insertion only intended media, no cross-tenant | REC-06, REC-08, REC-10, REC-15, REC-25, REC-29, REC-30 |
| Q029 | Image crop one coherent change | REC-10 |
| Q030 | Image processing failure keeps original | REC-10, REC-14, REC-37 |
| Q036 | Concurrent edits converge | REC-19 |
| Q037 | Collaboration reveals only authorised scope | REC-19 |
| Q040 | External assistance within data boundary | REC-20, REC-31 |

**Mapped: 13 QIDs. No evidence yet: 27** — Q002, Q003, Q006, Q008–Q016, Q020–Q027, Q031–Q035, Q038, Q039 (client-side editing behaviour; the JS layer is out of scope, EG6). No mapping answers a QID.

## 4. Handoff

- To PROOF (Stage 2, separate record): `G01_PROOF/G01_HTML_EDITOR_PROOF_20260927.md`.
- Proof addresses the 11 UNKNOWN_PENDING_PROOF and 6 CONTRADICTION items; the 6 GAP items are carried forward.

## 5. Limitations

- Only the inputs in 0.1 and Stage-2 static results were used. No runtime evidence exists; no live SSRF or third-party network probing was performed.
- QID mapping is controller-judged topical lineage, not coverage; NOT A3-ELIGIBLE until W1-B07 canonical re-freeze.
- No percentages; no Formal Coverage; no git operations; inputs not edited.
