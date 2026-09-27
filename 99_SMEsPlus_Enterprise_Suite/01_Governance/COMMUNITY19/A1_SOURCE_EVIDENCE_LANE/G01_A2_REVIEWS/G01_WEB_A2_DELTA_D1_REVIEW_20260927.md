# G01 PLATFORM_BASE — RED TEAM A2 DELTA Review of A1 Delta D1 — `web`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 DELTA (functional/semantic verifier). Independent of A1; the A1 delta is verified, not repaired |
| Group / Module | G01 PLATFORM_BASE / `web` |
| Reviewed input | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_WEB_A1_DELTA_D1_20260927.md` sha256 `bdf81cf5df68b405148c30bd030c174c3f23707beca86867c26e44338ad600c2` |
| Parent A1 package | `G01_A1_PACKAGES/G01_WEB_A1_PACKAGE_20260927.md` sha256 `814ee37e33365f37cb981f2bac9d245790e48e05e7b14075f1e322cd0520394b` (matches the D1 header) |
| Upstream Lane A PASS-2 | `G01_LANE_A_PASS2/G01_WEB_LANE_A_PASS2_20260927.md` sha256 `2ae1f05ee3d7e9e3cd5ca4b90c812048f1765a3dbc2ce2870f36cfc307adbc3a` (matches the D1 header) |
| Base A2 review (reference only; used for the conflict sweep) | `G01_A2_REVIEWS/G01_WEB_A2_REVIEW_20260927.md` sha256 `fdbab76741d60433f6a52ff0f3d4fb12ba1ccf47567e51e61c987f7dd5f0cd55` |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, fetched raw, blob SHA-1 from `git hash-object` (scratch only) |
| Lane B | None supplied |
| Date | 2026-09-27 |
| **Disposition** | **A2 DELTA PASS WITH FINDINGS.** D1 is traceable, and no disposition change or new claim is contradicted by source. One claim is PARTIAL (D18). Precision findings and omissions are listed in section 4, and none of them sends D1 back to A1. D1 converges with the base A2 web review, and no verdict conflict was found (section 4.3). Findings and proof requirements go forward to REC and PROOF |

Clean room: this review states behaviour in neutral terms and reproduces no vendor code. Identifiers and line numbers (~L) are evidence pointers only, valid at the anchor commit. There are no percentages and no Formal Coverage claim, and no git operations were run on the repository.

## 1. Test plan (predeclared)

The plan file is `scratchpad/a2_delta_d1/TEST_PLAN_WEB.md`, sha256 `079ebf6ff845daf7619a05874786227378e815429a85441e62bcc031b8c79326`. Declared timestamp: **2026-09-27T15:03:14Z** (file mtime 15:03:14.63Z). It was written after the input sha256 intake and before any source was fetched or re-read. The source fetch ran after that time.

| TP | Test | Pass criterion | Result |
|---|---|---|---|
| TP-W1 | Lineage: sha256 of D1, parent and PASS-2 against the D1 header | Equal | PASS |
| TP-W2 | Re-fetch every cited blob (P1–P11, E20, E21, E24, E25) at the anchor and compare with the D1 evidence key | All match | PASS: 15 of 15 match (HTTP 200), including P9, P10, P11 and E20, which A1 did not re-fetch. `odoo/exceptions.py` (`6baf8608…`) was also fetched, only to check exception inheritance for D15 |
| TP-W3 | Independent semantic re-read of every HIGH item and contradiction: X-WEB-01, X-WEB-02, master-password rate limiting, `/web/become` GET/CSRF, the `ir.binary` access order, logo raw SQL and any-origin access | The WHAT holds at the stated scope | Done (section 3) |
| TP-W4 | MED claims D09 (session binding), D13 (read-check), D14, D15, D16, D18 | Same | Done. A2 read all six regions |
| TP-W5 | Each disposition change follows from verified claims | Coherent | Done |
| TP-W6 | Conflict sweep against the base A2 web review | Conflicts flagged | None material (section 4.3) |
| TP-W7 | Lane B classification | Never FAIL for missing Lane B | Section 5 |
| TP-W8 | Proof requirements | Falsifiable, each with expected and fail conditions | Section 6 |

Verdict scale: VERIFIED (the source supports the item as stated), PARTIAL (the core is supported but the scope or wording is materially off), NOT_VERIFIED, OUT_OF_SCOPE.

## 2. Evidence integrity (TP-W2)

All re-fetched blobs match: `orm/models.py` 11f50c4e, `orm/environments.py` ec6b89fc, `service/db.py` 63c314a7, `tools/config.py` 433ff84b, `http.py` ebfc2ac8, `ir_binary.py` e7feca93, `ir_attachment.py` 905ae118, `controllers/pivot.py` a687d2d1, `controllers/database.py` 434b915c, `controllers/export.py` cb750f19, `controllers/home.py` 292aaa75, `controllers/binary.py` 7b7b84f7, `tools/misc.py` 6d275059, `service/security.py` d332199c and `res_users.py` 9d42d77a. There were no mismatches. D1's spot-check log (11 of 11 MATCH) is reproduced independently.

## 3. Verdict table

### 3.1 Disposition changes (D1 section 1)

| Item | D1 disposition | A2 verdict | A2 basis (independent re-read) |
|---|---|---|---|
| X-WEB-01 | RESOLVED (no platform-wide contradiction) | VERIFIED | The export-data method refuses unless the caller is admin or holds the export group (models ~L889). Admin means superuser mode or the Access Rights group, and the user-level admin test also counts the superuser uid (environments ~L182–185, res_users ~L1181–1183). The export routine builds records from the caller's environment by browse or search, then calls export-data in the grouped branch (~L573) and per batch in the flat branch (~L616). There is no sudo on that path. Omission carried from base A2 OM-W02: in the flat branch an empty record set never reaches export-data |
| X-WEB-02 | CONFIRMED-FROM-SOURCE (conditional) | VERIFIED | All five routes (create, duplicate, drop, backup, restore) test whether the stored secret still verifies as the default and a non-empty secret was supplied. If so, they call change-password through the dispatcher with the default as the old secret. The dispatcher's master check passes, the `list_db` decorator applies, and the new value is hashed and saved (db ~L413–417, config ~L1033–1034, ~L935–978). Precision (AO-W2): the save is best-effort. A file write error is only reported to stderr, and the in-memory hash changes either way |
| CRQ-WEB-01 | CLOSED | VERIFIED | Follows from D01. The empty-set residual is noted under X-WEB-01 |
| CRQ-WEB-02 | NARROWED (rate limiting open) | VERIFIED | A2 ran a keyword sweep for rate limiting, lockout, throttling, sleep, attempts and brute force over db.py, database.py, http.py, config.py and security.py. The only rate-limit hits are the websocket options. Each attempt pays the hash cost of the stored secret (pbkdf2, 600k rounds) once it is hashed, but that cost is not a lockout (AO-W5). The item remains open for proof |
| CRQ-WEB-03 | Open, evidence strengthened | VERIFIED | Follows from D07 |
| CRQ-WEB-04 | Open, scope widened | VERIFIED | Follows from D11 |
| CRQ-WEB-05 | Open, reconfirmed | VERIFIED | Follows from D17 |
| CRQ-WEB-06 | NARROWED | VERIFIED | Follows from D12–D15. NG-3 and NG-5 stay open |
| CRQ-WEB-07 | CLOSED | VERIFIED | The list endpoint returns the framework DB list, which calls the unforced service listing. That listing refuses when listing is off (db ~L440–442; database.py ~L178–185) |
| CRQ-WEB-08 | Unchanged | OUT_OF_SCOPE | Not addressed by D1 |
| C05 | Controller absence HIGH; platform absence REFUTED | VERIFIED | As for X-WEB-01 |
| C10 | Service enforcement raised to HIGH (static) | VERIFIED | Follows from D05 and D06 |
| C11 | HIGH, extended | VERIFIED | Follows from D07. Persistence precision in AO-W2 |
| C12 | Resolved, now HIGH | VERIFIED | Follows from D06 |
| C13 | HIGH, extended | VERIFIED | Follows from D11 |
| C14 | HIGH, reconfirmed | VERIFIED | Follows from D17 |
| C15 | Enforcement in `base` raised to HIGH (static) | VERIFIED | A2 read the ladder and the attachment hook (D12, D13) |
| BR-2 | Superseded by BR-2' | VERIFIED | Consistent with base A2 ("BR-2 CONTRADICTED by source") |
| BR-3 | Refined by BR-3' | VERIFIED | Follows from D06 and D07 |
| G-2, G-3, G-A1-1, G-A1-2 | CLOSED / CLOSED static with NG-1 residual / NARROWED | VERIFIED | Coherent with the verified claims |
| G-1, G-A1-3, G-A1-4, G-5 | Unchanged | OUT_OF_SCOPE | Not addressed |

### 3.2 New claims (D01–D18)

| Claim | A1 conf. | A2 verdict | A2 basis |
|---|---|---|---|
| D01 | HIGH | VERIFIED | As for X-WEB-01. The coupling risk holds: an Access Rights holder passes the gate without the export group. Omission: the empty-set path skips the gate (base A2 OM-W02) |
| D02 | HIGH | VERIFIED | The row builder is underscore-private and reached only through export-data. The generic read APIs are not gated by the export group. The `json.py` pointer was not re-read and is not needed for the WHAT |
| D03 | HIGH / LOW | VERIFIED | The route is authenticated-user and readonly. It builds the sheet only from the client JSON, with no model read and no group check. Injection part: A2 found no workbook option that disables string-to-formula conversion and no prefix neutralisation. The same holds for the record XLSX writer, which only replaces carriage returns. The library default is not source-verified here (PR-WD8) |
| D04 | HIGH | VERIFIED | The default is a file-only literal. The crypt context holds a strong hash scheme plus plaintext marked deprecated. An empty stored value refuses, and an empty supplied value fails the check |
| D05 | HIGH | VERIFIED | The dispatcher exempts exactly four methods. Backup and restore call the check directly and then call functions gated by `list_db` |
| D06 | HIGH | VERIFIED | The decorator is on create, duplicate, drop, dump, dump-manifest, restore (both), rename, change-password and migrate. The listing default is on (config ~L415). When listing is refused, the page renderer falls back to the current DB (database.py ~L38–41) |
| D07 | HIGH / conditional | VERIFIED | Precision: the bootstrap call sits outside each route's error handling. With listing off, it raises instead of rendering the error page (converges with base A2 C11). The persistence caveat is AO-W2 |
| D08 | HIGH | VERIFIED | All mutating manager routes are no-login, POST and CSRF-off. The framework enforces CSRF only for methods outside GET/HEAD/OPTIONS/TRACE on routes that keep CSRF on (http ~L225, ~L2487) |
| D09 | HIGH / MED | VERIFIED | A2 read session binding (http ~L1812–1850). A session DB that fails the filter is logged out, and a DB header is honoured only if it passes the filter. A header that conflicts with a session DB is forbidden |
| D10 | HIGH | VERIFIED | Duplicate has no membership check (db ~L185). Drop checks only the forced list (~L233–235). Backup checks the filtered list (database.py ~L134) |
| D11 | HIGH | VERIFIED | Authenticated-user, http type, readonly, no methods restriction. The check is on the Settings group (res_users ~L1177–1179), after which the session is rebound to the superuser, the cache cleared and the token recomputed. Precision: the framework sets the session cookie without a SameSite attribute (http ~L2189–2194; the cookie wrapper defaults to secure off and SameSite none). Whether the cookie travels on a cross-site navigation therefore depends on the browser's default (PR-W05 in the base review). No audit log line is written at the route |
| D12 | HIGH | VERIFIED | Order confirmed: existence (by xmlid, or registered model plus exists), then the field token, then the content hook, then the read check (ir_binary ~L44–55) |
| D13 | HIGH / MED | VERIFIED | Hook: the token is compared in constant time and a mismatch raises. Then the public flag, then a portal user's read check, then the base hook, which denies. A2 read the read-check detail (ir_attachment ~L540–580). Public attachments are readable. For non-system users, an unlinked attachment created by someone else is forbidden. Otherwise the linked record decides. Omission (AO-W4): field-bound attachments also require field-group access for non-system users |
| D14 | MED | VERIFIED | The field-access check returns true under superuser mode (models ~L3375–3386). The streamer calls that check on the elevated record (ir_binary ~L70–85) |
| D15 | MED | VERIFIED | The content route maps every user-error family to not-found. Access and missing errors both inherit from user error (exceptions.py). The image route serves a placeholder, or not-found when a download is requested |
| D16 | MED | VERIFIED | The elevated lookup domain is public, URL-bearing, bound to the view model with id 0 and created by the superuser. Otherwise the bundle is generated in the caller's environment |
| D17 | HIGH | VERIFIED | No-login, CORS any-origin, raw SQL on the company table by caller id, or else on the session uid's company or the superuser's company. No ORM check. Precision: the enumeration signal is "company has a logo". A company without a logo and a non-existent id both return the same placeholder (binary.py ~L302–307), so ids are enumerable only for companies with logos (PR-WD5) |
| D18 | MED | **PARTIAL** | The extension allowlist and the addons-path containment are confirmed. However, the name is joined to the fonts directory and then passed to the generic path resolver, which contains the result only to an addons or root path (misc ~L196–250). A name carrying parent segments (possible through the JSON-RPC body) can therefore reach any font-extension file under an addons path, not only the module's fonts directory. The impact is low (font files only), but "reads only from the module's fonts directory" is overstated |

**Counts.** Disposition changes (21 rows): VERIFIED 19, PARTIAL 0, NOT_VERIFIED 0, OUT_OF_SCOPE 2. New claims (18): VERIFIED 17, PARTIAL 1, NOT_VERIFIED 0, OUT_OF_SCOPE 0. **Total: VERIFIED 36, PARTIAL 1, NOT_VERIFIED 0, OUT_OF_SCOPE 2.**

## 4. Findings

### 4.1 A2 observations (not in D1; A1 is not repaired)

- **AO-W1 (content cache semantics).** The content and image routes mark a stream public whenever the request carries any access-token argument, whether or not that token was the source of access (binary.py ~L78–79, ~L200–201). For a non-attachment model, an invalid token falls through to the caller's own read check. A readable private record would then be served with public cache-control whenever a positive max-age applies (http ~L690–697). For attachments, a mismatched token raises and ends as not-found. This refines base A2 SF-W05 and bears on shared caches (PR-WD6).
- **AO-W2 (bootstrap persistence).** The secret change is applied in process memory first. The file save swallows write errors to stderr. On a read-only config file the adopted secret holds until restart and then reverts to the default. How the in-memory value spreads across multiple worker processes was not examined.
- **AO-W3 (error surface).** The bootstrap pre-step raises outside route error handling when listing is off, so the unauthenticated caller gets a framework error rather than the manager page. This duplicates base A2 C11.
- **AO-W4 (attachment field groups).** The attachment read check enforces field-group access for field-bound attachments, for non-system users. D13 omits this.
- **AO-W5 (master-secret attempt cost).** No lockout was found. Once the secret is hashed, each attempt costs one strong hash verification. The default plaintext state has no such cost.

### 4.2 D1 claim-level findings

- **F-W1 (D18 PARTIAL).** Font-route containment is at the addons-path level, not at the fonts directory.
- **F-W2 (D17 precision).** Logo enumeration covers only companies that have a logo.
- **F-W3 (D01 omission).** The empty-set export bypass is not carried into D1, although base A2 recorded it.

### 4.3 Conflict sweep against the base A2 web review

No verdict conflict was found. Several D1 conclusions match base A2 conclusions reached independently: X-WEB-01 (base: REFUTED as a contradiction; D1: RESOLVED), X-WEB-02 (both confirmed), C12 resolved, BR-2 corrected, the rate-limit gap (base OM-W04 matches D1 G-D1-1), `/web/become` over GET (base OM-W01 matches D1 D11) and pivot XLSX (base OM-W06 matches D1 D03). Two gaps in D1: it does not carry base OM-W02 (empty-set export), and it does not carry base SF-W05 (token means cache visibility; AO-W1 extends this). REC should treat the two lines as one conclusion and not count them twice.

## 5. Lane B

No Lane B evidence was supplied, and no item fails for its absence.

| Class | Items |
|---|---|
| NOT_APPLICABLE (structural or definitional) | D02, D04, D05, D12, D13, D14, D16 |
| UNCORROBORATED (user-surface, clear from source) | D01 (see base PR-W01), D08, D09, D15, D18 |
| UNCORROBORATED + MISSING_REQUIRED_RUNTIME_PROOF (depends on config, browser or deployment) | D03 (injection part), D06, D07, D10, D11, D17; CRQ-WEB-02 residual (rate limiting); AO-W1 |

## 6. Proof requirements (new; base A2 PR-W01 to PR-W08 still apply and are not repeated)

| PR | Claim / finding | Case | Expected (source-predicted) | Fail condition |
|---|---|---|---|---|
| PR-WD1 | D07, AO-W2 | Default secret, listing on, config file set read-only. Unauthenticated create with secret S. Then restart the server | Before restart S is accepted and the default is refused. A write error goes to stderr. After restart the default is accepted again | S survives the restart, or S is not adopted before the restart |
| PR-WD2 | CRQ-WEB-02, G-D1-1, AO-W5 | With the secret hashed, send 50 consecutive wrong-secret backup requests from one address straight to the app (no proxy), then one correct request | All 50 are refused with the same error, no lockout or added delay beyond hash cost, and the correct request succeeds | A lockout, throttle or delay escalation is observed. That would refute the negative finding, and the result must be recorded |
| PR-WD3 | D10 | dbfilter hides DB X, which is owned by the same PostgreSQL role. The master secret holder duplicates X, backs up X, and drops a copy of X | Duplicate succeeds, backup is refused as unknown, drop succeeds | Duplicate or drop is refused because of the filter, or backup succeeds |
| PR-WD4 | D11 | Record the Set-Cookie attributes of the session cookie at login, then repeat base PR-W05(c) in at least two browser engines | No SameSite and no Secure attribute set by the app. The cross-site outcome is recorded for each engine | The app sets SameSite=Strict (bounds D11), or a switch happens for a non-system user |
| PR-WD5 | D17, F-W2 | Unauthenticated cross-origin logo requests for (a) a company with a logo, (b) an existing company without a logo, (c) a non-existent id | (a) returns that logo with an any-origin header; (b) and (c) return identical placeholders | (a) is refused, or (b) and (c) can be told apart |
| PR-WD6 | AO-W1 | An internal user who can read record R (a non-attachment model with an image field) requests it through the image route with a unique param and a bogus access-token argument | Response is 200 with public cache-control | Private cache-control, or refusal |
| PR-WD7 | D18 | Font-route JSON-RPC call with a name that climbs out of the fonts directory to another font-extension file under an addons path, then to a non-font file | The font file is returned and the non-font file is refused | The font file is refused (containment is tighter than the source shows), or the non-font file is returned |
| PR-WD8 | D03, G-D1-2 | Pivot XLSX export with a client cell value starting with `=` | The cell is stored as a literal string | The cell is stored as a formula |

Proof requirement count: **8**.

## 7. Limitations

- SOURCE-STATIC at one commit. No runtime, configuration, proxy, browser or multi-process state was observed.
- The negative findings (no rate limiting, no audit at `/web/become`) come from bounded keyword sweeps of the files listed, not an exhaustive search. Overrides from other modules (NG-3), token minting (NG-5) and the JS client (NG-6) were not read.
- The spreadsheet library's default conversion of strings to formulas is third-party behaviour and was not verified from source.
- A2 read framework files beyond D1's evidence only to test D1's WHAT. That reading is A2 evidence, not an A1 repair.
- No percentages, no Formal Coverage, no QIDs answered, no git operations. No vendor code is reproduced.
