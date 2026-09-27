# G01 PLATFORM_BASE — Module `http_routing` — RED TEAM A2 Review

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional/semantic verifier of A1 conclusions). Independent of A1; A1 package not repaired. |
| Governed group / module | G01 PLATFORM_BASE / `http_routing` |
| Date | 2026-09-27 |
| A1 package (input, immutable) | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_HTTP_ROUTING_A1_PACKAGE_20260927.md` sha256 `57f9b3513e2caf3012f346dab09c9a3b457df32bdce004d59897a719e066a158` |
| Lane A packet (upstream, immutable) | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_HTTP_ROUTING_LANE_A_PASS1_20260927.md` sha256 `9dfcb95f2521ec078ee425e4755054844d54eb3e4233b8d83c04b03f9bfa612c` (matches hash recorded in A1 header) |
| Topic-lens bank | `GMVQ/G01_PLATFORM_BASE/G01_HTTP_ROUTING_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `b5cecfd676a6534ee4abdf0892ef9de2fdd835bc07e66da3606fbc26d11844c0` (W1-B08). Gate: **DELTA-RECHECK — non-canonical freeze basis**. A2 verification proceeds; **QID-level lineage is NOT A3-eligible until canonical re-freeze**. No QID answered. |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` via raw.githubusercontent; blob ids via `git hash-object` in scratchpad (no repo git ops) |
| Lane B | None supplied. |
| **Disposition** | **A2 VERIFIED WITH FINDINGS — HANDOFF TO REC.** 18 VERIFIED, 2 PARTIAL, 0 NOT_VERIFIED, 0 OUT_OF_SCOPE (20 items). Two A1 CRQs resolved at source (mitigated), one CRQ escalated to source-indicated exposure (anonymous traceback via debug flag). 6 proof requirements. |

### 0.1 Source re-check (independent A2 fetch)

| Path | Lane A blob | A2 computed | Match | Use |
|---|---|---|---|---|
| `addons/http_routing/__manifest__.py` | 9321b408… | 9321b4082f847cd079780946e3fc1335059211fb | YES | C01, X-01 |
| `addons/http_routing/__init__.py` | ad6393ee… | ad6393eeedf4aa6485f38cdd5ea0230cd89e205c | YES | C02 |
| `addons/http_routing/controllers/main.py` | a0c0d359… | a0c0d3597f0f1a9209339f58aad2b03893ec374d | YES | C15, C16 |
| `addons/http_routing/models/ir_http.py` | d508ceb8… | d508ceb82321dbda60e7fcdc1554b74eb17d3c49 | YES | C03–C12, C17 |
| `addons/http_routing/models/ir_qweb.py` | 39ffe927… | 39ffe9272cdc70767cf698b9b010d36d18678a8c | YES | C03, X-02 |
| `addons/http_routing/views/http_routing_template.xml` | 5c5e7d00… | 5c5e7d00a6f2c38b7973de87f57e564a4e336250 | YES | C13, C14 |
| Out-of-module (A2 context reads, not Lane A scope) | — | base `ir_http.py` d9d2a00b9bc7d3e7f439b7ff4ecc46488876953a; base `ir_qweb.py` 6fbe7711403a166dae36b4d5fe0b35499eb54659; `odoo/http.py` ebfc2ac8d268a45aaf4b8cde8c9ce8b480d58dbb; web `models/ir_http.py` bd03fa8e5e43ec580a63a068121f5a292215ac66; web `controllers/session.py` 2fbcfc872381751ac3336b2549babcca159d76cc; web `controllers/webclient.py` e94d5478a1d0836b7b0b8057dfca1b4142cb845c; manifests html_editor 6f0356c5…, web 72f3f257…, bus 2fdfb246…, portal 0df9206a…, website aaff2bc9… | n/a | Used only to settle A1 evidence gaps EG1/EG2 and CRQs |

## 1. Test plan (predeclared before verdicts)

| TP | Target | Method | Pass criterion for VERIFIED |
|---|---|---|---|
| TP1 | Lineage | sha256 of A1 + Lane A + bank; compare to A1 header | Hashes match A1-recorded values |
| TP2 | Blob integrity | Re-fetch every cited file at anchor; `git hash-object` | Equal to Lane A pointer table |
| TP3 | HIGH claims (C01, C04, C06, C08, C10, C12–C17) and all contradictions/CRQs | Independent semantic re-read of the cited function, plus one hop into the delegated base/web function where A1 left an evidence gap | Claim WHAT matches source; WHY/RISK not overstated or understated |
| TP4 | MED claims (C02, C03, C05, C07, C09, C11, C18) | Re-read the specific function (A1 did not) | Same as TP3 |
| TP5 | Business meaning | Evaluate claims as rules for a SaaS URL-routing layer (canonical URLs, language, error exposure, redirects, public endpoints, tenancy) | Material omissions/overclaims listed |
| TP6 | Lane B | Classify each claim without Lane B | NOT_APPLICABLE / UNCORROBORATED; never FAIL |
| TP7 | Runtime-inherent claims | Convert to falsifiable proof requirements | Expected + fail condition stated |

Verdict scale: VERIFIED (source supports claim as stated), PARTIAL (core fact true; scope, attribution or risk mis-stated), NOT_VERIFIED (source contradicts or does not support), OUT_OF_SCOPE.

## 2. Claim verdict table

| Item | A1 conf. | A2 verdict | A2 independent basis (neutral) |
|---|---|---|---|
| C01 | HIGH | VERIFIED | Hidden category; sole dependency web; data = two view files; post-init hook declared; no security/cron/demo data. |
| C02 | MED | VERIFIED | Hook sets the live request (if any) to non-frontend and non-multilang. |
| C03 | MED | **PARTIAL** | No new model (inherit-only) — true. RISK "global to every HTTP request, not opt-in per route" is overbroad: the match wrapper runs for every request, but language redirect, canonical-slug redirect and frontend error pages activate only for routes flagged as website/multilang (and for unmatched paths). Opt-in is per route flag. |
| C04 | HIGH | **PARTIAL** | Name-slug + id format, id-only fallback, error on missing id — true. "Slug/unslug helpers are defined here" is an overclaim: the platform base layer already defines id-only slug/unslug on the same abstract model; this module overrides them with the human-readable form. Consumers therefore do not strictly depend on this module to call the helpers (relevant to HEDT X-03). |
| C05 | MED | VERIFIED | Negative id retried as absolute value when negative record absent; raw value kept in context; self-described limited support. |
| C06 | HIGH | VERIFIED | GET/HEAD on frontend-multilang routes: rebuilt path compared to requested; mismatch → 301 with lang prefix when non-default. A2 note: redirect goes through the local-forced helper (see C10). |
| C07 | MED | VERIFIED | Precedence URL → cookie → context → default; nearest-lang = exact then language-prefix match; evaluation under temporary public auth, real env restored in a finally block. |
| C08 | HIGH | VERIFIED | Default partner-language default read elevated; else first active language. |
| C09 | MED | VERIFIED | Nine documented cases present. Nuance: bot case also forces request language to default; POST never redirects; unmatched case logs warning and continues. |
| C10 | HIGH | VERIFIED | Double-slash → 301 with explicit local flag; all other language redirects use the query-preserving helper. **A2 closes A1's open RISK:** the platform redirect helper defaults to local mode, stripping scheme and host and leading slash/backslash characters before emitting Location (see CRQ-HROU-05). |
| C11 | MED | VERIFIED | Non-multilang if path *contains* `/static/` (anywhere, not only prefix) or starts with `/web/`; matched endpoint must be website-flagged and multilang (default for http type); no endpoint → multilang; exception → false + warning. |
| C12 | HIGH | VERIFIED | Frontend-only; public user ensured; debug handler invoked; rollback; user/HTTP error mapping; 404/403 fallback hook; per-code template, 4xx generic fallback, render failure → 418 generic template. |
| C13 | HIGH | VERIFIED (risk escalated) | Seven `editable or debug` gates confirmed; traceback string is always computed into template values. **A2 settles A1 EG1 partially:** the web layer sets the session debug mode from a URL query parameter for any requester without an authentication check, the error handler calls that routine, and the template engine populates `debug` from the session. Source therefore indicates an anonymous requester can obtain the debug block (traceback) on frontend error pages. Runtime proof required (PR-HROU-01). |
| C14 | HIGH | VERIFIED | 404 embeds image from html_editor shape route and links `/contactus`; neither provider declared. |
| C15 | HIGH | VERIFIED (gap narrowed) | Public, readonly route; elevated read of frontend module list; caller comma-list appended. A2 one-hop read: the web handler and the base translation loader apply **no** installed-state or allow-list filter to caller names; the result hash is memoised keyed by the caller-controlled module set and language. |
| C16 | HIGH | VERIFIED (CRQ resolved) | Override flags website/non-multilang, default `/odoo`, passes redirect unchanged. Parent logs out then redirects with the platform helper in its default local mode → off-site targets are stripped to a local path. |
| C17 | HIGH | VERIFIED | Rewrite lookup memoised in a dedicated routing cache keyed by path + query; reroute limit 10. |
| C18 | MED | VERIFIED | No groups/ACL/rules; no company parameter in routing/language resolution at this layer. Note: company scoping of the stored default (if any) is a base concern, unread. |
| X-HROU-01 | — | VERIFIED (impact qualified) | Contradiction real. Semantic qualifier: html_editor, web and bus are all auto-install, so the shape image provider is normally present wherever web is; `/contactus` stays unresolved without website. Both references are link/image attributes, so absence should yield a broken image or dead link, not a render failure (source inference; PR-HROU-02). |
| X-HROU-02 | — | VERIFIED (as non-contradiction) | The template-engine warning concerns requests lacking the frontend attribute; backend passthrough in error handling is consistent with it. A1's CANDIDATE status is appropriate. |

## 3. Semantic findings (business meaning for a SaaS URL-routing layer)

| ID | Finding | Effect on A1 |
|---|---|---|
| SF-HROU-01 | **Error-detail exposure is caller-triggerable.** The "error details only in editable/debug rendering" rule (A1 BR5) is formally true but misleading as a security rule: debug is a requester-controlled session flag, not an authorisation. For a SaaS target, tracebacks to anonymous users are a disclosure risk (paths, module names, SQL fragments). | BR5 needs qualification; CRQ-HROU-01 escalated from open to source-indicated exposure. |
| SF-HROU-02 | **Redirect safety is centralised and local-by-default.** Language, canonical and logout redirects all pass through the platform helper in local mode; the double-slash normaliser runs before language redirects on redirect-capable requests. Open-redirect risk via these paths is mitigated at source. | CRQ-HROU-02 and CRQ-HROU-05 resolved (mitigated); runtime confirmation still listed as proof. |
| SF-HROU-03 | **Public translation endpoint amplification.** Arbitrary caller module names are loaded and memoised per distinct set; an anonymous requester can vary the key space (cache growth) and may learn which module names produce translation payloads (on-disk presence). Effect of unknown names inside the code-translation loader is unread. | CRQ-HROU-03 narrowed to runtime/limit question. |
| SF-HROU-04 | **Canonical URLs follow display names.** A rename silently moves the canonical URL (301 from the old slug still resolves by id). Business meaning: id is the durable key; slug is cosmetic but SEO-bearing. A1 captured this correctly (BR1, C06). | None. |
| SF-HROU-05 | **Language default is global, not tenant/company scoped at this layer.** For a multi-company SaaS target, default language and URL-language policy are single-valued per database here. | Supports CRQ-HROU-06 (design question). |
| SF-HROU-06 | **Slug helper ownership.** Base supplies id-only helpers; this module enriches them. Downstream modules calling the helpers degrade to id-only URLs rather than fail if this module is absent. | C04 PARTIAL; feeds HEDT X-03 NOT_VERIFIED. |

## 4. Omissions (not in A1)

- O1: `_handle_error` invokes the debug-mode handler itself, so even requests that fail before normal pre-dispatch can set debug from the query string (links to SF-HROU-01).
- O2: The language cookie is (re)set on redirects and on every frontend dispatch where it differs — a persistent client-side preference that can be set by any link; relevant to shared-device/SEO behaviour.
- O3: The `editable` truthiness used by the error templates is supplied by other modules' context/qweb preparation; html_editor injects an `editable` context key from the query string for any request (see HEDT review). Whether that reaches the error-template value set is unread.
- O4: `/website/translations` is readonly and sitemap-excluded but has no rate limit visible in module or delegated handler.
- O5: A1 did not note that html_editor/web/bus are auto-install, which materially reduces the X-HROU-01 impact for the image reference.

## 5. Lane B classification

No Lane B evidence supplied. No claim is FAIL on that basis.

| Claims | Classification |
|---|---|
| C01, C02, C03, C04, C05, C08, C11, C14, C15, C17, C18, X-HROU-01, X-HROU-02 (structural / static definitions) | NOT_APPLICABLE (source-static; runtime corroboration not required to hold the claim) |
| C06, C07, C09, C10, C12, C13, C16 (request-time behaviour) | UNCORROBORATED (runtime behaviour; see proof requirements where inherently runtime) |

## 6. CRQ outcomes (A2)

| CRQ | A2 outcome |
|---|---|
| CRQ-HROU-01 debug/editable for anonymous | **SOURCE-INDICATED YES** (debug via query param, no auth gate) → PR-HROU-01 |
| CRQ-HROU-02 logout off-site redirect | **RESOLVED AT SOURCE — mitigated** (local-forced helper) → PR-HROU-04 confirms |
| CRQ-HROU-03 translations filtering | **SOURCE-INDICATED: no filter**; unknown-name handling unread → PR-HROU-03 |
| CRQ-HROU-04 404 without providers | **SOURCE-INDICATED: degraded assets only, no render failure**; html_editor normally present (auto-install) → PR-HROU-02 |
| CRQ-HROU-05 language redirect host injection | **RESOLVED AT SOURCE — mitigated** → PR-HROU-05 confirms |
| CRQ-HROU-06 company-scoped language policy | OUT_OF_SCOPE for verification (design decision) — route to SaaS/functional design |

## 7. Proof requirements (MISSING_REQUIRED_RUNTIME_PROOF — inherently runtime)

| PR | Claim(s) | Setup / action | Expected (per source) | Fail condition |
|---|---|---|---|---|
| PR-HROU-01 | C13, CRQ-01 | Authorized sandbox DB with website-flagged route; unauthenticated client requests a nonexistent frontend path and a controlled 500 path, once plain and once with the debug query parameter set | Plain: no debug block. With debug param: debug block incl. traceback rendered to the anonymous client | Safety hypothesis ("details only for authorised debug") is FALSIFIED if traceback appears for anonymous; A2 source reading is FALSIFIED if no debug block appears in any debug-param case |
| PR-HROU-02 | C14, X-01, CRQ-04 | DB with web (+auto-installs) and http_routing but no website; request unknown frontend path | HTTP 404 with 404 template; shape image loads (html_editor auto-installed); contact link 404s | Status 418/500, or template render error |
| PR-HROU-03 | C15, CRQ-03 | Anonymous GET of translations route with (a) installed names, (b) non-installed on-disk names, (c) random names; repeat with many distinct sets | 200 each; (b) may return translation payloads; no rejection of (c); memo entries grow per distinct set | Caller names are filtered/rejected, or non-installed modules never return payloads (would narrow SF-HROU-03) |
| PR-HROU-04 | C16, CRQ-02 | Authenticated session; logout with redirect set to absolute external URL, scheme-relative, and backslash-prefixed forms | Location header is a local path for all forms | Any Location pointing off-host |
| PR-HROU-05 | C10, CRQ-05 | Multilang DB (≥2 frontend languages); GET crafted paths with lang prefix + slash/backslash host-like segments | All 3xx Location headers local | Any off-host Location |
| PR-HROU-06 | C06, C09, SF-04 | Record on a multilang route; GET by old slug after rename, by bare id, and POST by bare id | GET → 301 to current canonical slug; POST → no redirect | GET served without redirect on mismatch, or POST redirected |

## 8. Limitations

- Source presence ≠ runtime reachability; all outcomes above are source-level; proofs listed are not executed.
- One-hop reads into base/web/http core were made only to settle A1 evidence gaps; wider base behaviour (fallback serving, bot detection, code-translation loader internals, company scoping of stored defaults) remains unread.
- QID-level lineage not A3-eligible until canonical re-freeze of W1-B08 (DELTA-RECHECK basis).
- Clean room: neutral WHAT/WHY/RISK only; no vendor code reproduced; identifiers are evidence pointers.
- No percentages; no Formal Coverage claimed; no git operations performed.
