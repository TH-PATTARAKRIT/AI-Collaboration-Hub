# G01 PLATFORM_BASE — RED TEAM A3 Independent Challenge (STATIC, CLAIM-LEVEL) — `http_routing`

## 0. Header

| Item | Value |
|---|---|
| Role | RED TEAM A3, the independent adversarial challenger |
| Independence | A3 did not author Lane A, A1, A2, REC or PROOF for this module. It fetched its own source copies (scratchpad `a3_hrou_hedt/src`) rather than reusing upstream copies |
| Date | 2026-09-27 |
| Scope | STATIC, CLAIM-LEVEL only. Runtime cases R01..R06 are **NOT-EXECUTED**: they have neither passed nor failed. QID-level lineage is **NOT A3-ELIGIBLE** because W1-B08 is DELTA-RECHECK and awaits a canonical re-freeze. This is recorded here, and the QID answers are not challenged |
| Intake hashes (sha256) | Lane A `9dfcb95f2521ec078ee425e4755054844d54eb3e4233b8d83c04b03f9bfa612c`; A1 `57f9b3513e2caf3012f346dab09c9a3b457df32bdce004d59897a719e066a158`; A2 `6368e95b0bf49d6a8f698257d9e0e254675fcb3874407b70b4aaa1d2a63795d7`; REC `b20ab28814a7586ac8de4d436d9572bfd292f9f9ff27bdc84b622882c54e215a`; PROOF `fac9922f3ff1515edd7f0a63315f2cbebae214799e9eaba475ed0d64ae610bf8` (intake file `scratchpad/a3_hrou_hedt/intake.sha256`, sha256 `92f95bab…4040`) |
| Exit hashes | Re-hashed at exit and identical to intake for all five inputs, so the inputs were not modified (see §7) |
| Source anchor | odoo/odoo@`8d05257d83f9128953f580a066db67c48fcdb96f`, fetched from raw.githubusercontent.com only. Every blob was checked with `git hash-object` and logged in `scratchpad/a3_hrou_hedt/blob_log_a3.txt` (sha256 `a49692fb…0c1e`, 18 entries). All A3 blobs for files that PROOF also read equal PROOF's values |
| Network | No request to any arbitrary host. No SSRF probing. No runtime device was used |
| **Disposition** | **A3 STATIC PASS WITH DEFECTS (route to PROOF, REC)**. One challenge is sustained (C03, low severity). The core escalation (debug via URL leading to a traceback) is upheld and sharpened. MASTER handoff is not eligible while runtime and the re-freeze are pending |

Clean-room: A3 records neutral paraphrase and evidence pointers only. No vendor code is reproduced here. There are no percentages and no Formal Coverage. Git was used read-only (`log`, `show`, `status`).

## 1. Challenge log

| # | Target | A3 attempt to disprove | Evidence (anchor blob) | Disposition |
|---|---|---|---|---|
| CH-1 | REC-HROU-13 / PC-HROU-02, 03 — anonymous debug via URL leads to a traceback on error pages | (a) Looked for a requester check in the debug setter. None found: the setter normalises only the value (allowed modes, truthy→`1`, falsy→empty). It runs in pre-dispatch and is called explicitly again by the frontend error handler (web `ir_http` `bd03fa8e`; http_routing `ir_http` `d508ceb8`). (b) Looked for an auth gate in the error handler. It does the reverse: when no uid is present it forces the public user, and only then sets debug. (c) Checked whether session persistence could defeat the chain. It cannot, because debug is set in-memory and rendering happens in the same request. (d) Checked whether rendering skips the `debug` value. The view renderer calls the template engine directly, with no minimal-context flag (base `ir_ui_view` `4700d806`), and the engine takes `debug` from the session (base `ir_qweb` `6fbe7711`). (e) Checked whether the website layer gates it. The website override gates only `editable` (on the designer group) and does not touch `debug` (website `ir_http` `02d7d74a`). (f) Checked the template list. There are seven gated templates: generic, 4xx, 400, 403, 415, 422 and 500. The 404 template has no debug block. The 418 fallback renders the generic template, which does carry the block (template `5c5e7d00`). (g) Checked the traceback source. The traceback is computed unconditionally in the exception values | All the listed blobs | **UPHELD**. A3 sharpens it: precondition = frontend request (website-flagged route, or an unmatched path) that ends in a non-404 HTTP error. A concrete public path exists without `website`. html_editor's public, website-flagged shape route raises a 400 on colour-validation failure (html_editor controller `df0db6c7`, helper raising BadRequest). By static inference, that path reaches the 400 template's debug block. Calling this "anonymous" is accurate at source level. Disclosure itself stays runtime (R01) |
| CH-1b | R1 refinement (the 404 leg) | Checked whether a 404 can still reach the traceback. Yes, indirectly: a 404 whose template exception has a nested path is promoted to 500. The designer-only `page_404` is website-owned | `d508ceb8`, `02d7d74a` | **UPHELD** (PROOF's R1 is correct. The promotion to 500 is noted for R01 design) |
| CH-4a | C04 RESOLVED against A1 (slug helpers) | Checked that base defines `_slug`/`_unslug` and that http_routing only overrides them and adds `_unslug_url` | base `ir_http` `d9d2a00b`; module `d508ceb8` | **UPHELD** |
| CH-4b | C03 CONTRADICTION: REC basis "source supports A2 (opt-in per route)"; PC-HROU-09 PASS | Looked for request-wide behaviour that does not depend on route flags. Found one: when the first match fails (NotFound), the module strips a candidate language segment and runs the language-resolution and redirect branch. It then re-matches, and on NotFound it forces `is_frontend` and `is_frontend_multilang` to true. So **every unmatched path** gets frontend treatment regardless of any route flag (and goes on to the frontend error handler). A2's scope holds only for *matched* endpoints | `d508ceb8`, match step | **CHALLENGE-SUSTAINED (PROOF, REC)**. PC-HROU-09's fail condition ("applied regardless of flags") was tested only on the matched-endpoint branch, which is a weak condition. REC's basis overstates the support for A2. C03 should stay CONTRADICTION with both sides partly supported. Severity is low, and the classification does not change |
| CH-4c | X-HROU-01 CONTRADICTION (manifest `['web']` vs html_editor shape and `/contactus`) | Tried to show the providers are declared. They are not (manifest `9321b408`). Resolved PROOF's open point: `/contactus` is provided by `website` as a page **data record** (URL `/contactus`), not by a controller route | website `data/website_data.xml` `ddf87b43` | **UPHELD**. PROOF's "provider not located" limitation is closed at source level. A2's website attribution is correct. The runtime effect stays with R02 |
| CH-5 | Predeclaration | Hashed the cases file: `a660285f…d5dd` matches. File mtime is 15:04:59.69Z. The earliest source-copy mtime in `rec_hrou_hedt/src` is 15:05:16Z. The stub committed in `209f3b1` equals the cases file byte for byte (after its 4-line header) | scratchpad and git (read-only) | **UPHELD**. Note: git proves stub content, not the claimed 15:05:07Z write time. The commit time is 15:06:34Z |
| CH-5b | Re-execution of static PASS cases | Re-ran PC-HROU-02, 03, 08, 09 and 10 on independent copies. 02, 03, 08 and 10 reproduce. 09 reproduces for its stated branch but has the weak condition described in CH-4b | as above | **UPHELD** (09 flagged) |
| CH-5c | Overclaim, Lane B misuse, clean room | Searched all five inputs for exploitability or runtime-confirmation language. Found only "runtime confirmation still listed as proof" (A2 SF-HROU-02), which is not an overclaim. Lane B is recorded as absent: UNCORROBORATED or NOT_APPLICABLE, never FAIL, so there is no misuse. There are no code blocks and no verbatim code | inputs | **UPHELD** |

Observation (outside module scope, not a stage defect): the platform JSON-RPC exception serialiser in `odoo/http.py` (`ebfc2ac8`) always includes a formatted traceback in the error payload, whatever the debug state. The debug-URL chain is therefore not the only traceback-disclosure path on the platform. This belongs to the core HTTP layer, not `http_routing`. It is recorded as a GAP for whichever stage owns the platform-core review.

## 2. Lineage

- `git log --follow` (read-only): Lane A `07cca3c`; A1 `42612ef`; A2 `837c661`; REC `95f51c5`; PROOF `209f3b1` (the predeclaration stub, 36 lines) followed by `fc6e7c3` (the final version, 122 lines). The working tree equals HEAD for all five files.
- Hygiene note for Integration Control (not a stage defect): several commits that carry these files have messages naming unrelated modules. For example, the A1 package came in with "base_sparse_field, google_recaptcha", and the final PROOF came in with "A3 base_automation … REC/Proof mail". The lineage can still be followed by path, but not by commit message.
- QID lineage (36 mapped / 4 no evidence): **NOT A3-ELIGIBLE** until the W1-B08 canonical re-freeze. It was not challenged.

## 3. Defects routed

| ID | Owner | Defect | Severity | Required action |
|---|---|---|---|---|
| A3-HROU-D1 | PROOF | PC-HROU-09's fail condition does not cover the NotFound branch, where frontend and multilang flags are forced true and language resolution runs whatever the route flags are | Low | Add a static case for the unmatched-path branch, and extend R05/R06 design to unmatched paths |
| A3-HROU-D2 | REC | REC-HROU-03's basis states "source supports A2" without qualification | Low | Restate as partly supporting each side (matched endpoints favour A2; unmatched paths show request-wide behaviour). Keep CONTRADICTION open |
| A3-HROU-N1 | PROOF (note) | The `/contactus` provider is now located (website page data record). R02 should expect a dead link without `website`, and a served page with it | Info | Update R02 expected text at the next revision |
| A3-HROU-N2 | PROOF (note) | R01 should include a public website-flagged route that raises 400 (for example, html_editor shape colour validation) with the debug parameter, plus a 404-promoted-to-500 variant | Info | Add as R01 legs |

## 4. Runtime / gate-blocked items

- R01..R06 are NOT-EXECUTED because the device is OFFLINE. They have neither passed nor failed.
- All 10 UNKNOWN_PENDING_PROOF items stay open (C06, C09, C10, C13, C14, C15, C16, O1, O3, O4).
- Three GAP items are carried forward unchanged.
- QID-level challenge is blocked by the W1-B08 re-freeze.
- MASTER handoff: **PENDING RUNTIME + RE-FREEZE**.

## 5. Limitations

- Static only. No runtime result is claimed, and the traceback disclosure itself is not demonstrated.
- The redirect cases PC-HROU-04/05/06/07 were not re-executed (at least three cases per module were; see CH-5b).
- Bot detection, fallback serving internals and ACLs were not read. Session-store save rules were read only as far as needed for CH-1(c).
- There are no percentages and no Formal Coverage. Git was used read-only, and the inputs were not edited.

## 6. A3 exit

**A3 STATIC PASS WITH DEFECTS (route to PROOF, REC)**, at claim level. MASTER handoff is pending runtime (R01..R06) and the W1-B08 re-freeze.

## 7. Exit integrity

The five input hashes were re-computed at exit and are identical to the intake hashes in §0.
