# G01 PLATFORM_BASE — RED TEAM Reconciliation DELTA D1 — `web`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | SMEsPlus RECONCILIATION controller — DELTA cycle D1, Stage 1 of a two-stage REC + PROOF delta run. Stage 2 is recorded in `G01_PROOF/G01_WEB_PROOF_DELTA_D1_20260927.md` |
| Group / Module | G01 PLATFORM_BASE / `web` |
| Date | 2026-09-27. Input hashes taken at run start and re-taken at 15:18:24Z UTC (identical). Proof predeclared at 15:18:51Z, source fetched from 15:19:01Z |
| Nature | Delta addendum. Base REC `G01_WEB_REC_20260927.md` and every other input stay unedited. Where this delta and the base disagree on the net state of an item, the supersede map (section 4) governs. Base text is not rewritten |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, raw fetch, blob-verified with `git hash-object` (scratch only) |
| Question bank / freeze | `GMVQ/G01_PLATFORM_BASE/G01_WEB_GMVQ_MVQ_50_V1.00_DRAFT.md` sha256 `259839a2c0f265b9519d23bad3b25b8d74dd5a89b9410e01d3560e0a42fcd558` (= FREEZE_W1-B01 bank entry). Freeze hash `558ec88047aef5c8e7ea0e2675b1c43ef358ec29b172d6878068330f3fba7177`. FREEZE manifest sha256 `d0edfb228d849b5633cdd1dccea95667305831c2c264f43432c337c4fa3d1351` |
| Join key | MODULE `web` + QID + freeze hash. Lineage only. **No QID is answered** |
| **Disposition** | **REC DELTA D1 COMPLETE — HANDOFF TO PROOF DELTA.** 46 delta items classified (MATCH 29, UNKNOWN_PENDING_PROOF 10, CONTRADICTION 1, GAP 6), plus 2 carried without delta (A2 OUT_OF_SCOPE) and 8 folded. D01–D18 now carry reconciliation credit. Base REC-WEB-15 moves to CONTRADICTION — RESOLVED (source layer), and base REC-WEB-29 moves from GAP to UNKNOWN_PENDING_PROOF. Base PC-WEB-11 FAIL is consistent with D1 and stays preserved |

### 0.1 Parent artifacts (immutable; sha256 at intake)

Paths are relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

| Input | Path | sha256 | Cross-check |
|---|---|---|---|
| A1 DELTA D1 | `G01_A1_PACKAGES/G01_WEB_A1_DELTA_D1_20260927.md` | `bdf81cf5df68b405148c30bd030c174c3f23707beca86867c26e44338ad600c2` | Equals the value in the A2 D1 header and the base REC intake |
| A2 DELTA D1 review | `G01_A2_REVIEWS/G01_WEB_A2_DELTA_D1_REVIEW_20260927.md` | `3886d78cbeb90d5a3c1003ff5d65c7d0e4c6980ea278d338e338345db9554a5f` | Equals the arrival hash that the base REC recorded, unopened, at 15:14Z. The file is unchanged since then. Disposition "A2 DELTA PASS WITH FINDINGS". VERIFIED 36, PARTIAL 1 (D18), NOT_VERIFIED 0, OUT_OF_SCOPE 2. PR-WD1..PR-WD8 |
| Lane A PASS-2 | `G01_LANE_A_PASS2/G01_WEB_LANE_A_PASS2_20260927.md` | `2ae1f05ee3d7e9e3cd5ca4b90c812048f1765a3dbc2ce2870f36cfc307adbc3a` | Equals the value in the D1 and A2 D1 headers |
| Base REC (read-only) | `G01_RECONCILIATION/G01_WEB_REC_20260927.md` | `9e2a4a370ffb4e9a010e81633da1e85f0db4c2a762f8c26322ef38074e5abc2d` | Lists D01–D18 as PENDING DELTA with no credit (its 0.3) |
| Base PROOF (read-only) | `G01_PROOF/G01_WEB_PROOF_20260927.md` | `a72724e8c7f1f5eb3b3f7707b511de3383b45b5b0b1f2d88e67db58771719d57` | PC-WEB-11 FAIL (the empty-result skip holds on the non-grouped path only) |
| Parent A1 package (reference) | `G01_A1_PACKAGES/G01_WEB_A1_PACKAGE_20260927.md` | `814ee37e33365f37cb981f2bac9d245790e48e05e7b14075f1e322cd0520394b` | Equals the D1 and A2 D1 headers |
| Base A2 review (reference) | `G01_A2_REVIEWS/G01_WEB_A2_REVIEW_20260927.md` | `fdbab76741d60433f6a52ff0f3d4fb12ba1ccf47567e51e61c987f7dd5f0cd55` | Equals the A2 D1 header |
| Question bank | `../GMVQ/G01_PLATFORM_BASE/G01_WEB_GMVQ_MVQ_50_V1.00_DRAFT.md` | `259839a2…d558` (full value in header) | Equals FREEZE_W1-B01 |

The scratch record is at `scratchpad/rec_web_d1/`: `intake_sha256.txt` sha256 `49d3ea4bf5418e448803c36b01c0f9d6da43ed54b31a883aa087d1d6ff7b5ee5`.

### 0.2 Lane B

`find` over the repository (excluding `.git`) for `*lane_b*`, `*laneb*`, `*gemini*` and `*evidence_pool*` returned no files. **No Lane B runtime evidence exists for `web`.** Every item is UNCORROBORATED or NOT_APPLICABLE, and nothing fails for lack of Lane B. The classes follow A2 D1 section 5 where A2 assigned one.

Clean room: every statement is a neutral WHAT/WHY/RISK paraphrase. Identifiers are evidence pointers only. No vendor code is reproduced, and no vendor schema, ORM, workflow or naming is recommended. No percentages. No Formal Coverage. No git operations. No input was edited.

## 1. Classification rules (same as base REC section 1)

- **MATCH**: A1 D1 and A2 D1 agree (A2 VERIFIED, including nuance that does not disagree) at source level, and the item is not inherently runtime- or configuration-dependent. An A2 omission counts as MATCH when a proof source re-read confirms it and its effect does not depend on runtime.
- **UNKNOWN_PENDING_PROOF**: A1 and A2 agree at source level, but the claim or its stated risk depends on runtime, configuration, a browser or a library, or a runtime proof requirement exists.
- **CONTRADICTION**: A1 and A2 disagree (A2 PARTIAL or REFUTED), or a proof re-read disagrees with a stage statement. Both statements are kept. The item is **RESOLVED** only when the originating side itself converges (as for X-WEB-01 in the base). Otherwise it is **OPEN**.
- **GAP**: evidence is missing, and no source or runtime case in scope can settle it.
- **Folded**: an item that A2 D1 or D1 itself marks as a duplicate of another item is folded into that item and not counted twice (A2 D1 section 4.3).

## 2. Reconciliation — D1 disposition changes (A1 D1 section 1 against A2 D1 section 3.1)

PC-WEB-D-nn refers to the proof delta. PC-WEB-nn refers to the base proof.

| REC-D ID | D1 item | A1 D1 disposition | A2 D1 verdict | REC class | Basis | Lane B | Proof link |
|---|---|---|---|---|---|---|---|
| REC-WEB-D01 | X-WEB-01 | RESOLVED: no platform-wide contradiction | VERIFIED. Omission: an empty flat set never reaches export-data | MATCH | A1 D1 and A2 D1 agree. Supported by base PC-WEB-09/10 PASS and PC-WEB-D-19 PASS. The empty-set residual is folded into base REC-WEB-27 (section 3.3) | UNCORROBORATED | PC-WEB-09, 10; PC-WEB-D-19; runtime PC-WEB-01 |
| REC-WEB-D02 | X-WEB-02 | CONFIRMED-FROM-SOURCE, conditional | VERIFIED, plus AO-W2 precision (persistence is best-effort) | UNKNOWN_PENDING_PROOF | Agreement at source. The takeover depends on configuration and runtime. Supported by PC-WEB-15/16 PASS and PC-WEB-D-10 PASS | UNCORROBORATED | PC-WEB-D-10; runtime PC-WEB-03, PC-WEB-D-01 |
| REC-WEB-D03 | CRQ-WEB-01 | CLOSED (answered by D01) | VERIFIED | MATCH | Agreement. The CRQ asked whether a server-side gate exists, and it does. Residuals REC-WEB-25/27/31 stay open in the base | UNCORROBORATED | PC-WEB-10 |
| REC-WEB-D04 | CRQ-WEB-02 | NARROWED; the rate-limit residual stays open. Folds A1 G-D1-1 and A2 AO-W5 | VERIFIED. A2 found no limiter in five files; the only defence is the per-attempt hash cost | UNKNOWN_PENDING_PROOF | Both lines agree on the negative at source (PC-WEB-D-11 PASS, five files). A runtime case, PR-WD2, now exists. Proxy and deployment controls are outside source | UNCORROBORATED | PC-WEB-D-11; runtime PC-WEB-D-02 |
| REC-WEB-D05 | CRQ-WEB-03 | Open, evidence strengthened (design decision) | VERIFIED | MATCH | The disposition is agreed. The underlying behaviour is REC-WEB-D02/D26 (UNKNOWN_PENDING_PROOF) | UNCORROBORATED | — |
| REC-WEB-D06 | CRQ-WEB-04 | Open, scope widened (GET, no CSRF) | VERIFIED | MATCH | The disposition is agreed. The underlying behaviour is REC-WEB-D30 (UNKNOWN_PENDING_PROOF) | UNCORROBORATED | — |
| REC-WEB-D07 | CRQ-WEB-05 | Open, reconfirmed | VERIFIED | MATCH | The disposition is agreed. The underlying behaviour is REC-WEB-D36 | UNCORROBORATED | — |
| REC-WEB-D08 | CRQ-WEB-06 | NARROWED; NG-3 and NG-5 open | VERIFIED | MATCH | Agreement. The residuals are REC-WEB-D44 (NG-3) and REC-WEB-D46 (NG-5) | UNCORROBORATED | — |
| REC-WEB-D09 | CRQ-WEB-07 | CLOSED (D06) | VERIFIED | MATCH | Agreement. The list endpoint refuses when listing is off (base PC-WEB-16) | UNCORROBORATED | PC-WEB-16 |
| — | CRQ-WEB-08 | Unchanged | OUT_OF_SCOPE | Carried, no delta | Base REC-WEB-19 stands | — | — |
| REC-WEB-D10 | C05 | Controller absence stays HIGH; platform absence REFUTED | VERIFIED | MATCH | Agreement (PC-WEB-09/10) | UNCORROBORATED | PC-WEB-09, 10 |
| REC-WEB-D11 | C10 | Service enforcement raised to HIGH (static) | VERIFIED | MATCH | Agreement (PC-WEB-16) | UNCORROBORATED | PC-WEB-16 |
| REC-WEB-D12 | C11 | HIGH, extended (persisted; `list_db` gate) | VERIFIED; AO-W2 | MATCH (for the confidence change) | The confidence change is a static fact. The behaviour stays UNKNOWN_PENDING_PROOF under REC-WEB-D02/D26 | UNCORROBORATED | PC-WEB-D-10 |
| REC-WEB-D13 | C12 | Resolved, now HIGH | VERIFIED | MATCH | Agreement (PC-WEB-16) | UNCORROBORATED | PC-WEB-16 |
| REC-WEB-D14 | C13 | HIGH, extended | VERIFIED | MATCH (for the confidence change) | Static agreement. The behaviour is REC-WEB-D30 | UNCORROBORATED | PC-WEB-17, PC-WEB-D-13 |
| REC-WEB-D15 | C14 | HIGH, reconfirmed | VERIFIED | MATCH (for the confidence change) | Static agreement. The behaviour is REC-WEB-D36 | UNCORROBORATED | PC-WEB-19 |
| REC-WEB-D16 | C15 | Enforcement in `base` raised to HIGH (static) | VERIFIED | MATCH | A1 D1 now states the access ladder the way A2 reads it (PC-WEB-21 PASS). Effect on base REC-WEB-15: see section 4 | UNCORROBORATED | PC-WEB-21 |
| REC-WEB-D17 | BR-2 → BR-2' | Superseded | VERIFIED | MATCH | Agreement with base A2 ("BR-2 contradicted") | UNCORROBORATED | PC-WEB-10, 12 |
| REC-WEB-D18 | BR-3 → BR-3' | Refined | VERIFIED | MATCH | Agreement (PC-WEB-15/16) | UNCORROBORATED | PC-WEB-15, 16 |
| REC-WEB-D19 | G-2, G-A1-2 CLOSED; G-3 CLOSED static with NG-1 residual; G-A1-1 NARROWED | as stated | VERIFIED | MATCH | Coherent with the verified claims. The residuals are REC-WEB-D42 (NG-1), D44 (NG-3) and D46 (NG-5) | NOT_APPLICABLE | — |
| — | G-1, G-A1-3, G-A1-4, G-5 | Unchanged | OUT_OF_SCOPE | Carried, no delta | Base REC-WEB-35/08/23/37 stand | — | — |

## 3. Reconciliation — D1 new claims and A2 D1 findings

### 3.1 New claims D01–D18

| REC-D ID | Claim | A1 D1 (conf.) | A2 D1 verdict | REC class | Basis | Lane B (A2 D1 §5) | Proof link |
|---|---|---|---|---|---|---|---|
| REC-WEB-D20 | D01: export gate in the ORM export method (superuser, Access Rights or export group); CSV/XLSX reach it in the caller's environment; the Access Rights group is coupled to the export permission | HIGH | VERIFIED. Omission F-W3 (empty set) | MATCH | Agreement, supported by PC-WEB-10 and PC-WEB-D-19. D01's phrase "calls that method in both the grouped and flat branches" does not hold for an empty flat set. That is recorded under REC-WEB-27 (section 3.3) and is not a separate contradiction, because A2 raised it as an omission, not a disagreement | UNCORROBORATED | PC-WEB-10; PC-WEB-D-19; runtime PC-WEB-01 |
| REC-WEB-D21 | D02: the export gate governs the export action, not confidentiality | HIGH | VERIFIED | MATCH | Agreement (base PC-WEB-12) | NOT_APPLICABLE | PC-WEB-12 |
| REC-WEB-D22 | D03: pivot XLSX formats a client payload with no export gate; injection handling not examined | HIGH / LOW | VERIFIED. No workbook option or neutralisation found; the library default is unverified | UNKNOWN_PENDING_PROOF | The route-level absence is confirmed (PC-WEB-D-17 PASS). Whether a leading `=` becomes a formula is library/runtime behaviour. Folds A1 G-D1-2 | UNCORROBORATED + runtime | PC-WEB-D-17; runtime PC-WEB-D-08, PC-WEB-02 |
| REC-WEB-D23 | D04: master-secret storage, default literal, empty acts as a kill-switch | HIGH | VERIFIED | MATCH | Agreement (PC-WEB-15; PC-WEB-D-10 crypt context) | NOT_APPLICABLE | PC-WEB-15 |
| REC-WEB-D24 | D05: the dispatcher checks the secret for all but four methods; backup and restore check it directly | HIGH | VERIFIED | MATCH | Agreement (PC-WEB-16) | NOT_APPLICABLE | PC-WEB-16 |
| REC-WEB-D25 | D06: `list_db` off refuses all management functions; pages degrade; listing is on by default | HIGH | VERIFIED | UNKNOWN_PENDING_PROOF | Static agreement (PC-WEB-15/16). The deployment exposure depends on configuration and runtime (A2 D1 §5) | UNCORROBORATED + runtime | PC-WEB-16; runtime PC-WEB-04 |
| REC-WEB-D26 | D07: first-caller bootstrap persists the secret and passes the `list_db` gate | HIGH / conditional | VERIFIED; precision AO-W2/AO-W3 | UNKNOWN_PENDING_PROOF | Static agreement (PC-WEB-16, PC-WEB-D-10) | UNCORROBORATED + runtime | PC-WEB-D-10; runtime PC-WEB-03, PC-WEB-D-01 |
| REC-WEB-D27 | D08: mutating manager routes need no login, use POST and have CSRF off | HIGH | VERIFIED | MATCH | Agreement (PC-WEB-16/17 CSRF rule) | UNCORROBORATED | PC-WEB-17 |
| REC-WEB-D28 | D09: dbfilter semantics and session/header binding | HIGH / MED | VERIFIED (A2 read session binding; a conflicting header is forbidden) | MATCH | A2 raises the MED part through its own read. There is no disagreement | UNCORROBORATED | — |
| REC-WEB-D29 | D10: dbfilter does not bound duplicate or drop; backup is bounded | HIGH | VERIFIED | UNKNOWN_PENDING_PROOF | Static agreement, re-confirmed (PC-WEB-D-12 PASS). The effect depends on the PostgreSQL role and configuration | UNCORROBORATED + runtime | PC-WEB-D-12; runtime PC-WEB-D-03 |
| REC-WEB-D30 | D11: `/web/become` accepts GET, is outside CSRF, has no step-up and no audit | HIGH | VERIFIED; precision on cookie SameSite/Secure | UNKNOWN_PENDING_PROOF | Static agreement (PC-WEB-17, PC-WEB-D-13 PASS). Whether a cross-site switch happens depends on the browser | UNCORROBORATED + runtime | PC-WEB-D-13; runtime PC-WEB-05, PC-WEB-D-04 |
| REC-WEB-D31 | D12: public content access ladder | HIGH | VERIFIED | MATCH | Agreement (PC-WEB-21) | NOT_APPLICABLE | PC-WEB-21 |
| REC-WEB-D32 | D13: attachment content hook and read check | HIGH / MED | VERIFIED; omission AO-W4 | MATCH | Agreement. AO-W4 is separate (REC-WEB-D40) | NOT_APPLICABLE | PC-WEB-D-18 (hook), PC-WEB-D-20 |
| REC-WEB-D33 | D14: elevation passes the field-group check | MED | VERIFIED | MATCH | A2 read the region, so the item is no longer A1-unverified | NOT_APPLICABLE | — |
| REC-WEB-D34 | D15: denial shows as not-found or a placeholder | MED | VERIFIED | MATCH | A2 read the region | UNCORROBORATED | — |
| REC-WEB-D35 | D16: elevated asset lookup is constrained | MED | VERIFIED | MATCH | A2 read the region | NOT_APPLICABLE | — |
| REC-WEB-D36 | D17: logo aliases use raw SQL, any origin and a caller-supplied company id | HIGH | VERIFIED; precision F-W2 (only companies with a logo can be enumerated) | UNKNOWN_PENDING_PROOF | Static agreement. F-W2 is re-confirmed at source (PC-WEB-D-14 PASS: a missing row and an empty logo give the same placeholder). The cross-origin effect is runtime. Folds F-W2 | UNCORROBORATED + runtime | PC-WEB-D-14; runtime PC-WEB-06, PC-WEB-D-05 |
| REC-WEB-D37 | D18: the font route reads only from the module's fonts directory | MED | **PARTIAL**: containment is at the addons-path or root-path level. Folds F-W1 | **CONTRADICTION — OPEN** | A1 D1 (and Lane A PASS-2 F-21): fonts directory only. A2 D1: addons/root-path containment, so parent segments can reach other font-extension files. The proof re-read supports A2 (PC-WEB-D-16 PASS: the joined path is normalised, then contained only to addons or root paths; an absolute name also bypasses the fonts directory). Both statements are kept. The item stays OPEN because the originating side has not converged. Impact is low (font extensions only) | UNCORROBORATED | PC-WEB-D-16; runtime PC-WEB-D-07 |

### 3.2 A2 D1 observations and D1 gaps (not already folded)

| REC-D ID | Item | Source line(s) | REC class | Basis | Lane B | Proof link |
|---|---|---|---|---|---|---|
| REC-WEB-D38 | **AO-W1 (A2 extra finding)**: any access-token query argument marks the content/image stream public, whether or not that token granted access. A readable private non-attachment record can then be served with public cache-control when max-age > 0 | A2 D1 only. A1 D1 silent. The base A1 C15 wording "a token makes the stream public" was classed a contradiction in base REC-WEB-15 | UNKNOWN_PENDING_PROOF | Source re-read confirms both mechanisms (PC-WEB-D-15 PASS: flag on argument presence; PC-WEB-D-18 PASS: public directive when public and max-age > 0; an attachment token mismatch raises). The shared-cache effect depends on proxy and runtime. Precision found in proof: only the URL query-string argument sets the flag | UNCORROBORATED + runtime | PC-WEB-D-15, D-18; runtime PC-WEB-D-06, PC-WEB-D-09 |
| REC-WEB-D39 | AO-W2: bootstrap persistence is best-effort (memory first, write errors to stderr) | A2 D1. Consistent with A1 D07, which says "persists" without the failure branch | UNKNOWN_PENDING_PROOF | PC-WEB-D-10 PASS (static). Restart and multi-worker behaviour are runtime | UNCORROBORATED | PC-WEB-D-10; runtime PC-WEB-D-01 |
| REC-WEB-D40 | AO-W4: the attachment read check also requires field-group access for field-bound attachments (non-system users) | A2 D1, and Lane A PASS-2 F-16. D13 omits it | MATCH | PC-WEB-D-20 PASS. The effect is structural | NOT_APPLICABLE | PC-WEB-D-20 |
| REC-WEB-D41 | G-D1-3: how the Access Rights group is granted in `base` data (the coupling in D01) | A1 D1 | GAP | Data files not read in any lineage stage | NOT_APPLICABLE | — |
| REC-WEB-D42 | NG-1: `service/common.py` and deployment-level blocking of DB-manager paths | PASS-2, A1 D1 | GAP | Outside source for the deployment part. `common.py` not read | NOT_APPLICABLE | — |
| REC-WEB-D43 | NG-2: audit trail for superuser switches beyond the route | PASS-2, A1 D1 | GAP | Route-level absence is shown (base PC-WEB-17). Other layers not read | NOT_APPLICABLE | — |
| REC-WEB-D44 | NG-3: other modules' content-hook overrides | PASS-2, A1 D1 | GAP | Not read | NOT_APPLICABLE | — |
| REC-WEB-D45 | NG-4: translations, bundle, manifest, barcode and profiling public routes not deepened | PASS-2, A1 D1 | GAP | Overlaps base REC-WEB-23 (profiling, static PASS). The rest is unread | NOT_APPLICABLE | — |
| REC-WEB-D46 | NG-5: minting and lifetime of the field-access token | PASS-2, A1 D1 | GAP | Not traced | NOT_APPLICABLE | — |

### 3.3 Folded items (recorded, not counted)

| Item | Folded into | Note |
|---|---|---|
| AO-W3 (the bootstrap raises outside error handling when listing is off) | Base REC-WEB-11 | A2 D1 says it duplicates base C11 |
| AO-W5 (per-attempt hash cost, no lockout) | REC-WEB-D04 | Same residual |
| G-D1-1 (no rate limit) | REC-WEB-D04 | Same residual; base OM-W04 |
| G-D1-2 (XLSX formula injection) | REC-WEB-D22; base REC-WEB-08 | Same library question |
| F-W1 (D18 PARTIAL) | REC-WEB-D37 | — |
| F-W2 (logo enumeration precision) | REC-WEB-D36 | — |
| **F-W3 (the empty-set export bypass is not carried into D1)** | **Base REC-WEB-27** | See the consistency record below |
| NG-6 (client-side export UI) | Base REC-WEB-35 (G-1) | Same gap |

**Consistency record: empty-result exports against base PC-WEB-11 FAIL.**
- **A1 D1** says nothing about empty-result exports. Its D01 wording ("calls that method in both the grouped and flat branches") is true for non-empty sets and silent on the empty flat case. Lane A PASS-2 F-2 is also silent. No D1 statement contradicts PC-WEB-11.
- **A2 D1** makes two statements. In the X-WEB-01 row it says "in the flat branch an empty record set never reaches export-data". That wording is scoped and **consistent** with the PC-WEB-11 observation (the skip happens on the non-grouped path only). In the D01 row it says "the empty-set path skips the gate". That wording is unscoped and repeats the over-breadth of base OM-W02 that PC-WEB-11 narrowed.
- **Proof delta** PC-WEB-D-19 (PASS) re-observed the same state as PC-WEB-11: the grouped path calls export-data on the full set, empty or not, before grouping, so the gate runs; the flat path over an empty id set makes no call, writes a header-only file and still writes the log line with count 0.
- **Net:** base REC-WEB-27 stays **CONTRADICTION — OPEN**. The A2 X-WEB-01 wording converges with the proof, but the D01-row wording does not, so the originating side has not fully converged. The PC-WEB-11 FAIL stays preserved as a failed result. For A3.

### 3.4 Class counts (delta items only)

| Class | Count | Items |
|---|---|---|
| MATCH | 29 | D01 X-WEB-01, D03, D05, D06, D07, D08, D09, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19 (17 disposition rows); D20 (D01), D21 (D02), D23 (D04), D24 (D05), D27 (D08), D28 (D09), D31 (D12), D32 (D13), D33 (D14), D34 (D15), D35 (D16) (11 claims); D40 (AO-W4) |
| UNKNOWN_PENDING_PROOF | 10 | D02 X-WEB-02, D04 CRQ-WEB-02 residual; D22 (D03), D25 (D06), D26 (D07), D29 (D10), D30 (D11), D36 (D17); D38 AO-W1, D39 AO-W2 |
| CONTRADICTION | 1 | D37 (D18), OPEN |
| GAP | 6 | D41 G-D1-3, D42 NG-1, D43 NG-2, D44 NG-3, D45 NG-4, D46 NG-5 |
| **Total classified** | **46** | 19 disposition rows + 18 claims + 9 A2/D1 findings and gaps |
| Carried, no delta | 2 | CRQ-WEB-08; G-1/G-A1-3/G-A1-4/G-5 row |
| Folded | 8 | Section 3.3 |

Cross-check with A2 D1: its 36 VERIFIED items land in MATCH or UNKNOWN_PENDING_PROOF, its 1 PARTIAL (D18) is the single CONTRADICTION, and its 2 OUT_OF_SCOPE are the two carried rows. Lane B across the 46 items: NOT_APPLICABLE 15 (D19, D21, D23, D24, D31, D32, D33, D35, D40, D41–D46) and UNCORROBORATED 31. Nothing fails for absence.

## 4. Net-state supersede map for affected base REC items

The base REC text is unchanged. This table records the net state after D1. It is lineage, not a rewrite.

| Base item | Base class (base REC) | Net class after D1 | Change and reason |
|---|---|---|---|
| REC-WEB-05 X-WEB-01 (+C05, BR-2, G-2, CRQ-WEB-01) | CONTRADICTION — RESOLVED ("A1-D1 agreement, no credit") | **CONTRADICTION — RESOLVED** (unchanged) | "Agreement, no credit" becomes **credited**: REC-WEB-D01, D10, D17 and D03 are MATCH on A1 D1 + A2 D1 VERIFIED. The residuals stay in REC-WEB-25, 27 and 31 |
| REC-WEB-08 C08 (+G-A1-3) | UNKNOWN_PENDING_PROOF | UNKNOWN_PENDING_PROOF (unchanged) | Widened to the pivot route (D03, G-D1-2). New runtime case PC-WEB-D-08 alongside PC-WEB-02. Static route-level absence re-confirmed by PC-WEB-D-17 |
| REC-WEB-10 C10 | MATCH | MATCH (unchanged) | Strengthened by D05 and D06 (REC-WEB-D24, D25) |
| REC-WEB-11 C11 / X-WEB-02 | UNKNOWN_PENDING_PROOF | UNKNOWN_PENDING_PROOF (unchanged) | D1 credit (REC-WEB-D02, D26). AO-W2 adds a restart-reversion branch (PC-WEB-D-01). AO-W3 folded here |
| REC-WEB-12 C12 (+CRQ-WEB-07) | UNKNOWN_PENDING_PROOF | UNKNOWN_PENDING_PROOF (unchanged) | CRQ-WEB-07 CLOSED is credited (REC-WEB-D09). The deployment exposure is still runtime (PC-WEB-04) |
| REC-WEB-13 C13 (+CRQ-WEB-04) | UNKNOWN_PENDING_PROOF | UNKNOWN_PENDING_PROOF (unchanged) | Credited by D11 (REC-WEB-D30). The cookie-attribute precondition is confirmed statically (PC-WEB-D-13). New runtime case PC-WEB-D-04 |
| REC-WEB-14 C14 (+CRQ-WEB-05) | UNKNOWN_PENDING_PROOF | UNKNOWN_PENDING_PROOF (unchanged) | Credited by D17 (REC-WEB-D36). The enumeration scope is narrowed to companies with a logo (F-W2, PC-WEB-D-14). New runtime case PC-WEB-D-05 |
| **REC-WEB-15 C15 (+CRQ-WEB-06)** | CONTRADICTION — OPEN (A1 "token makes stream public" vs A2 "token governs cache; access by token, hook or read check") | **CONTRADICTION — RESOLVED (source layer)**; runtime pending | The originating side has converged: A1 D1 (C15 row + D12) states the access ladder as A2 reads it, and A2 D1 VERIFIED it. Base PC-WEB-21 PASS supports it. The cache aspect of A1's original wording survives as a separate item, REC-WEB-D38 (AO-W1), which is UNKNOWN_PENDING_PROOF. Runtime PC-WEB-07 is still pending. The A1 text is kept unedited |
| REC-WEB-23 C23 | UNKNOWN_PENDING_PROOF | UNKNOWN_PENDING_PROOF (unchanged) | NG-4 records that the profiling toggle was not deepened in PASS-2 (REC-WEB-D45) |
| REC-WEB-25 SF-W02a (Access Rights bypass) | UNKNOWN_PENDING_PROOF ("A1 did not state") | UNKNOWN_PENDING_PROOF (unchanged) | "A1 did not state" is superseded: A1 D1 D01 now states the coupling risk, so A1 and A2 agree. The user-visible effect is still runtime/client (PC-WEB-01; G-1). G-D1-3 (REC-WEB-D41) is added as a GAP |
| REC-WEB-26 OM-W01 | UNKNOWN_PENDING_PROOF ("C13 did not state") | UNKNOWN_PENDING_PROOF (unchanged) | Superseded "not stated": A1 D1 D11 now states GET, no CSRF and no audit. NG-2 is carried as REC-WEB-D43 |
| REC-WEB-27 OM-W02 (empty-result) | CONTRADICTION — OPEN (A2 vs PC-WEB-11 FAIL) | **CONTRADICTION — OPEN** (unchanged) | Consistency record in 3.3. D1 is silent (A1) or split (A2). PC-WEB-D-19 re-observes the same state. F-W3 folded |
| **REC-WEB-29 OM-W04 (+CRQ-WEB-02 residual)** | GAP | **UNKNOWN_PENDING_PROOF** | A runtime case is now in scope: PR-WD2 becomes PC-WEB-D-02. The static negative is widened from two files to five (PC-WEB-D-11 PASS). A1 D1 (G-D1-1) and A2 D1 now agree. Folds AO-W5 |
| REC-WEB-31 OM-W06 | MATCH | MATCH (unchanged) | A1 D1 now states it (D02, D03). The pivot injection part moves to REC-WEB-08/D22 |
| REC-WEB-35 G-1 | GAP | GAP (unchanged) | NG-6 folded |
| REC-WEB-11 / REC-WEB-30 (OM-W05, error text) | UNKNOWN_PENDING_PROOF / MATCH | unchanged | AO-W3 is related (a framework error instead of the page when listing is off). It is folded into REC-WEB-11 and not recounted |
| Base 0.3 "PENDING DELTA" block | D01–D18 no credit | **Superseded**: D01–D18 and the D1 dispositions are reconciled here | — |

**Net base class counts after D1 (37 base items; lineage view):** MATCH 18 (unchanged), CONTRADICTION 5 (X-WEB-01 RESOLVED and C15 now RESOLVED; C03, C04 and OM-W02 OPEN), UNKNOWN_PENDING_PROOF 9 (the 8 base items + OM-W04), GAP 5 (OM-W03, OM-W08, G-1, G-4, G-5).

## 5. QID lineage updates (frozen bank; lineage only, not answers)

Join key: MODULE `web` + QID + freeze hash `558ec880…7177`. A mapping means the item is topically relevant evidence. It answers no QID and satisfies no disconfirming observation.

### 5.1 Added mappings (D1 items on already-mapped QIDs)

| QID | Added delta items |
|---|---|
| Q003 context switch invalidates stale state | D30 (D11: token recomputed on switch) |
| Q004 state change needs authorised context | D02, D24, D25, D26, D27, D30, D39 |
| Q005 read-only navigation causes no durable change | D30 (GET-reachable, readonly-flagged route changes the session) |
| Q008 identifier tampering | D29 (D10), D31 (D12), D36 (D17), D37 (D18) |
| Q011 sensitive values in addresses | D38 (AO-W1: token in the query string) |
| Q012 temporary link expiry and scope | D31, D32, D46 (NG-5) |
| Q013 authorisation at download time | D31, D32, D33, D35, D40 |
| Q014 preview/inline paths share the boundary | D31, D34 |
| Q016 browser caching of protected pages | D38 |
| Q017 server-side cache keyed by authorisation | D38, D35 (D16) |
| Q019 host/domain selects the boundary | D09, D25, D28 (D09), D29 (D10) |
| Q025 conflicting scope indicators | D28 (D09: a DB header that conflicts with the session DB is forbidden, per A2 D1) |
| Q030 client-side validation not sole enforcement | D01, D20, D41 |
| Q033 sort/group/filter exposure | D21 (D02) |
| Q034 error page exposure | AO-W3 (folded into REC-WEB-11) |
| Q036 repeated invalid authentication | D04 |
| Q037 abuse-control scope | D04 |
| Q047 not-found vs denied non-disclosure | D34 (D15), D36 (D17 placeholder uniformity) |
| Q050 equivalent paths converge on the same controls | D01, D20, D21, D22 |

### 5.2 Newly mapped QIDs (removed from the "no evidence" list)

| QID | Topic (paraphrased) | Delta item(s) | Why topical |
|---|---|---|---|
| G01-WEB-Q022 | Cookie scope and secure context | D30 (D11 precision) | A2 D1 and PC-WEB-D-13: the session cookie is set with no SameSite argument, and the wrapper defaults Secure off |
| G01-WEB-Q046 | Download filename/metadata and unsafe path behaviour | D37 (D18) | A caller-supplied font name is resolved as a path. Containment is addons-level, not directory-level |
| G01-WEB-Q048 | Timing/size side channel | D32 (D13 constant-time token compare), D34 (D15 uniform not-found), D36 (D17 identical placeholders) | Static non-disclosure controls relevant to side channels. Timing is not measured |

Considered and **not** mapped: Q020 (proxy metadata). D09's DB header is an application header, not forwarding metadata, and host-pattern selection is already under Q019. Q023/Q024 (session after reset or renewal). D11's token recompute is a privilege switch, not revocation.

**Mapped QIDs now: 29. No evidence yet: 21 QIDs**: Q002, Q006, Q007, Q009, Q015, Q018, Q020, Q021, Q023, Q024, Q026, Q028, Q029, Q038, Q039, Q040, Q041, Q042, Q043, Q044, Q049. No mapping answers a QID.

## 6. Handoff

- To the PROOF DELTA (Stage 2, same run): `G01_PROOF/G01_WEB_PROOF_DELTA_D1_20260927.md`. It predeclares PC-WEB-D-01..D-09 (runtime: PR-WD1..8 plus the cache-public finding) and PC-WEB-D-10..D-20 (source/config), and executes the source/config cases.
- For A3: REC-WEB-D37 (D18) OPEN; base REC-WEB-27 OPEN with the D1 consistency record; base REC-WEB-15 newly RESOLVED at source (A3 may challenge whether AO-W1 is enough reason to keep it open); REC-WEB-29 reclassified from GAP.

## 7. Limitations

- REC used only the inputs in 0.1 and, for classification support, the static results of the proof delta and the base proof. No runtime evidence exists.
- Classes that rest on proof re-reads are bounded to the regions read at one commit. Negative results (rate limiting, audit) come from keyword sweeps of named files.
- QID mapping is topical lineage judged by this controller. It is not a coverage measure. No Formal Coverage, no percentages, no git operations. No input was edited.
