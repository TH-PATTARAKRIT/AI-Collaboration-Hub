# G01 PLATFORM_BASE — RED TEAM A3 Independent Challenge (STATIC, CLAIM-LEVEL) — `html_editor`

## 0. Header

| Item | Value |
|---|---|
| Role | RED TEAM A3, the independent adversarial challenger |
| Independence | A3 did not author Lane A, A1, A2, REC or PROOF for this module. It fetched its own source copies (scratchpad `a3_hrou_hedt/src`) |
| Date | 2026-09-27 |
| Scope | STATIC, CLAIM-LEVEL only. Runtime cases R01..R10 are **NOT-EXECUTED**: they have neither passed nor failed. QID-level lineage is **NOT A3-ELIGIBLE** because W1-B07 is DELTA-RECHECK and awaits a canonical re-freeze. This is recorded here, and the QID answers are not challenged |
| Intake hashes (sha256) | Lane A `e0e59e77ce408839e7a0bb64197443c0f9ca8a68d394329adc92bca7236df10e`; A1 `e96156fa82878ab6580ea08c74e1dc07a1b8be86c0283ade761f53fcaa81a1c4`; A2 `6e0784636cfda87a5e7f86e343627e989ccd88a6c5db21e08f7cd9963a3fca75`; REC `6677f36de93e588de97f55946fce1d7f8904a534854c7a81ca38aec46e83eae8`; PROOF `eb8dcbced4686fbc6b27cd4d68df8836d28613478652e38cf17831ee4446eb7b` (intake file sha256 `92f95bab…4040`) |
| Exit hashes | Re-hashed at exit and identical to intake (see §7) |
| Source anchor | odoo/odoo@`8d05257d83f9128953f580a066db67c48fcdb96f`, fetched from raw.githubusercontent.com only, with `git hash-object` checks (`blob_log_a3.txt` sha256 `a49692fb…0c1e`). Fetcher blob `18515419263f8fc005029601a5c7bc821cc9f727` re-verified. All overlapping blobs equal PROOF's values |
| Network | **No SSRF probing** and no request to any arbitrary host. Nothing was fetched through the link-preview route or any listener |
| **Disposition** | **A3 STATIC PASS WITH DEFECTS (route to A2; PROOF notes)**. One challenge is sustained (the SVG impact statement omits a platform mitigation). The SSRF and dependency conclusions are upheld. MASTER handoff is not eligible while runtime and the re-freeze are pending |

Clean-room: A3 records neutral paraphrase and evidence pointers only. No vendor code is reproduced here. There are no percentages and no Formal Coverage. Git was used read-only.

## 1. Challenge log

| # | Target | A3 attempt to disprove | Evidence (anchor blob) | Disposition |
|---|---|---|---|---|
| CH-2 | REC-HEDT-05/33/35, PC-HEDT-02/03: no SSRF guard, redirects followed, body unbounded, reachable from a public route | (a) Route auth: the external preview route is `jsonrpc`, `auth=public`, POST, and passes the caller URL straight to the fetcher (controller `df0db6c7`). It is db-bound, and there is no CSRF gate on jsonrpc. (b) Fetcher: GET with redirects allowed, a 3 s per-operation timeout, streaming, and no host, IP or private-range check. HTML is accumulated in 8 KB chunks until a head-close marker, with no ceiling (`18515419`). (c) Upstream guard in the client: no session or adapter is configured by the caller, and no proxy or allow-list is set in module, fetcher or `odoo/http.py` (`ebfc2ac8`). (d) Rate limiting: a search of module, fetcher and `odoo/http.py` found no construct | as listed | **UPHELD** at source. Refinements that calibrate strength without changing the verdict: (i) the HTTP client itself only mounts http/https adapters, so the scheme is effectively constrained by the client, not by the module; PC-HEDT-02's "no scheme allow-list" is accurate for the file only. (ii) Read-back is partial: only 2xx responses with `image/*` (URL and MIME) or `text/html` (title, description, image, site name) return data, and everything else returns false, which leaves a status/timing oracle. (iii) Egress through deployment-level proxy environment variables, which the client honours by default, could impose controls that source cannot decide. That is a deployment item |
| CH-3a | REC-HEDT-10, PC-HEDT-04: modify_image stores caller bytes as SVG | (a) Who can call: `auth=user`, so any authenticated user at route level, portal included. (b) Checks: a read check on the source's linked record only when the source is record-bound, and a write check on the caller-chosen target model and record. The default target is the view model with id 0, which is a model-level write check. The caller may name any model or record it can write. When the caller supplies bytes, the source's own content is not read. (c) Closed PROOF's R2 at source: the base attachment layer forces `text/plain` for XML-like MIME (SVG included) when the context flag is set **or the acting real user lacks write access on views**. The check drops elevation, so the elevated copy does not bypass it (base `ir_attachment` `905ae118`). The superuser MIME write in modify_image therefore restores SVG for exactly the users the core guard targets. A superuser write passes the same check. (d) Existing-attachment dedup returns a match without the access checks, but the lookup runs in the user's environment | controller `df0db6c7`; base `ir_attachment` `905ae118`; allow-list `49820e8d` | **UPHELD and sharpened** (static) |
| CH-3b | A2 SF-HEDT-03 / REC: "public SVG served from the application origin is an active-content concern" | Looked for a platform mitigation on serving. Found one: the platform sets `nosniff` on every response and adds `Content-Security-Policy: default-src 'none'` to every response whose content type starts with `image/`, unless a CSP is already present (`odoo/http.py` `ebfc2ac8`, CSP setter called on the dispatch paths). A2, REC and PROOF do not account for this, and it materially limits script execution when a stored SVG is opened directly | `ebfc2ac8` | **CHALLENGE-SUSTAINED (A2; carried by REC)**. This is a strength calibration, not a reversal: the SVG storage path stands. The impact statement must name the CSP mitigation and its bounds, and R04/R05 must capture the response headers of the served SVG |
| CH-3c | C02 (open) and PC-HEDT-05/07: undeclared mail/iap/website deps; "imports resolve from addons path, not install state" | Checked the declared deps: `base, bus, web` (`6f0356c5`). The module-level imports of mail and iap tool packages are present. Import set-up: the loader appends readable configured addons directories to the addons package search path. The only meta-path hook targets the upgrade namespace. No install-state gate exists (`odoo/modules/module.py` `488a2a06`) | as listed | **UPHELD**. C02 correctly stays an open CONTRADICTION. Caveat for R06: importing a submodule of an uninstalled addon executes that addon's package initialiser. Whether this has side effects remains undecided at source |
| CH-4 | C04 / X-HEDT-03 RESOLVED against A1 | Checked that the slug and unslug calls go through the request-dispatch model on the environment and are never imported from http_routing, and that base defines both | controller `df0db6c7`; base `ir_http` `d9d2a00b` | **UPHELD** |
| CH-5 | Predeclaration | Cases file `a660285f…d5dd` matches, mtime 15:04:59.69Z. The earliest source mtime is 15:05:16Z. The committed stub (`209f3b1`) equals the cases file | scratchpad, git read-only | **UPHELD**. Git proves stub content, not the claimed 15:05:07Z write time |
| CH-5b | Re-execution of static PASS cases | Re-ran PC-HEDT-02, 03, 04, 06, 07 and 10 on independent copies. All reproduce. The query-string editor flags are injected into context with no requester check | as above | **UPHELD**. Weak conditions flagged: PC-04 depended on unread downgrade logic (now closed by CH-3a); PC-02's scheme leg (CH-2 i); PC-07 tests the import gate but not import side effects (already deferred to R06) |
| CH-5c | Overclaim, Lane B misuse, clean room | "Exploitability" appears only in negated or pending form: A1 "not a finding of exploitability", A2 "exploitability pending runtime proof", and PROOF/REC "exploitability unproven". Lane B is recorded as absent, with no FAIL for absence. There are no code blocks and no verbatim code | inputs | **UPHELD** |

## 2. Lineage

- `git log --follow` (read-only): Lane A `07cca3c`; A1 `e4eba78`; A2 `442993c`; REC `811e8ae`; PROOF `209f3b1` (the stub) followed by `1cdc739` and `f510676`, which have identical length. The working tree equals HEAD.
- Hygiene note for Integration Control: the commit messages name unrelated modules (for example, the A2 review arrived under "mail, auth_signup, base_setup reviews"). The lineage can be followed by path only.
- QID lineage (13 mapped / 27 no evidence): **NOT A3-ELIGIBLE** until the W1-B07 canonical re-freeze. It was not challenged.

## 3. Defects routed

| ID | Owner | Defect | Severity | Required action |
|---|---|---|---|---|
| A3-HEDT-D1 | A2 (REC carries) | The SF-HEDT-03 and REC-HEDT-10 impact statements omit the platform `image/*` CSP (`default-src 'none'`) and `nosniff` headers | Medium (calibration) | Restate the impact with the mitigation and its bounds, for example embedding contexts and responses that already carry a CSP |
| A3-HEDT-N1 | PROOF (note) | PROOF's R2 is closed at source: the core downgrade applies to XML-like MIME for users without view write, and the superuser reset reverses it | Info | Update R2. R05 expected text should cite a non-designer editor specifically |
| A3-HEDT-N2 | PROOF (note) | R04 and R05 do not capture the headers of the served SVG | Info | Add header capture (CSP and content type) to R04 and R05 |
| A3-HEDT-N3 | PROOF (note) | PC-HEDT-02 scheme leg: the client constrains schemes to http/https | Info | Annotate. The verdict is unchanged |

## 4. Runtime / gate-blocked items

- R01..R10 are NOT-EXECUTED because the device is OFFLINE. They have neither passed nor failed. Network cases need a sandbox with local stubs only.
- All 11 UNKNOWN_PENDING_PROOF items stay open (C05, C08, C09, C10, C20, O1, O6, O7, SF-02, SF-06, CRQ-02).
- C02's runtime effect depends on R06.
- Six GAP items are carried forward.
- QID-level challenge is blocked by the W1-B07 re-freeze.
- MASTER handoff: **PENDING RUNTIME + RE-FREEZE**.

## 5. Limitations

- Static only. There was no SSRF probing and no runtime result.
- The media-library save path (PC-08), Vimeo (PC-09), UUID egress (PC-12) and ACL files were not re-executed.
- The JS editor layer, the core sanitiser, image processing and the binary-serving access rules were not read.
- Whether the CSP holds in every serving path (for example, a reverse proxy stripping headers) is a deployment and runtime question.
- There are no percentages and no Formal Coverage. Git was used read-only, and the inputs were not edited.

## 6. A3 exit

**A3 STATIC PASS WITH DEFECTS (route to A2; PROOF notes)**, at claim level. MASTER handoff is pending runtime (R01..R10) and the W1-B07 re-freeze.

## 7. Exit integrity

The five input hashes were re-computed at exit and are identical to the intake hashes in §0.
