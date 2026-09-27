# G01 PLATFORM_BASE — RED TEAM Reconciliation (REC) — `web_tour`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of a two-stage REC + PROOF run; Stage 2 is recorded separately in `G01_PROOF/G01_WEB_TOUR_PROOF_20260927.md`) |
| Group / Module | G01 PLATFORM_BASE / `web_tour` |
| Date | 2026-09-27 (intake 15:03Z UTC; this record written ~15:12Z UTC) |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/web_tour/` plus the `base` server-action and attachment files A2 read for C11 |
| Question bank | `GMVQ/G01_PLATFORM_BASE/G01_WEB_TOUR_GMVQ_MVQ_40_V1.00_DRAFT.md`, sha256 `fdc06e0b530f327b2eec9ffddd3abff4104d387acb43c2fade99344854986f37`. This **equals** the `bank_files` entry in `FREEZE_W1-B05.json`. Freeze hash `cc81bc57f3686bfec5eda5fff354599e4d2ba5a9855078e9c2eaa13a6ca91bd3` (matches the brief). W1-B05 is ELIGIBLE (canonical replay MATCH; floor delta noted) per `QUESTION_GATE_G01_FREEZE_REPLAY_20260927.md` |
| Join key | MODULE `web_tour` + QID + freeze hash above. Lineage only. **No QID is answered here** |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (24 REC items; 2 CONTRADICTION items, one of them — C11 "Export JS by read-only" — resolved at source by A2, runtime pending) |

### 0.1 Input intake (immutable; sha256 recorded at intake 2026-09-27T15:03Z)

Paths are relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

| Input | Path | sha256 | Cross-check |
|---|---|---|---|
| A1 package | `G01_A1_PACKAGES/G01_WEB_TOUR_A1_PACKAGE_20260927.md` | `d794e25f34cbd6a821661764b3cec356df1219625510605261a9b1fc7546d315` | Equals the A1 hash consumed by A2 |
| A2 review | `G01_A2_REVIEWS/G01_WEB_TOUR_A2_REVIEW_20260927.md` | `b7d585137777cb92900a51b044e8a7bc91482c70d1b6b7e3f66456d7064381b4` | Disposition "A2 PASS WITH FINDINGS"; 3 proof requirements PR-T01..PR-T03; Export-JS-by-read-only RISK refuted statically |
| Lane A PASS-1 | `G01_LANE_A_PASS1/G01_WEB_TOUR_LANE_A_PASS1_20260927.md` | `111e1959eb255d339ac921a3981c090b0bbb9a77d9db1273c2b15d8a96b387d0` | Equals the value in the A1 and A2 headers |
| Question bank | see header | `fdc06e0b…6f37` | Equals the FREEZE_W1-B05 entry |
| FREEZE manifest | `../GMVQ/G01_PLATFORM_BASE/FREEZE_W1-B05.json` | `7884f78d25ca0d28c1fe59104f59ee7b7f19ecd1a1f292a349d3f8e1ad69bd6a` | freeze_hash `cc81bc57…91bd3`; `formal_coverage` NOT AUTHORIZED |
| Freeze replay record | `../GMVQ/G01_PLATFORM_BASE/QUESTION_GATE_G01_FREEZE_REPLAY_20260927.md` | `52430ca13a7d59f1a979f213879959133d48332be72f205c2fb9a31db60810e2` | W1-B05: bank bytes MATCH, 40 MVQ QIDs, canonical replay MATCH, ELIGIBLE (floor delta: 40 < governed 48; recorded there, not remediated here) |

No A1 delta exists for `web_tour`.

### 0.2 Lane B evidence-pool search (recorded)

- Same search as the `web` REC (shared run): `grep -ril -E 'web_tour|G01-WEB'` over `99_SMEsPlus_Enterprise_Suite` returned 43 files; filtering paths for `lane_b|laneb|gemini|evidence_pool|observ|runtime` returned **no match** (rc=1). `find` for `*lane_b*`, `*laneb*`, `*gemini*`, `*evidence_pool*` returned **no files**.
- Conclusion: **no Lane B / Gemini runtime evidence exists for `web_tour`**. Every item's Lane B column is UNCORROBORATED or NOT_APPLICABLE. Never FAIL for absence.

Clean-room note: neutral WHAT/WHY/RISK paraphrase only; identifiers are evidence pointers; no vendor code reproduced; no reuse of vendor schema, ORM, workflow, UI or naming recommended. No percentages, no Formal Coverage, no git operations, inputs not edited.

## 1. Classification rules (predeclared)

Identical to the `web` REC in this run (`G01_WEB_REC_20260927.md` §1): MATCH / GAP / CONTRADICTION (RESOLVED or OPEN) / UNKNOWN_PENDING_PROOF; Lane B UNCORROBORATED or NOT_APPLICABLE only.

Scope of REC items: A1 claims C01–C15; A2 omissions OM-T01..OM-T06; A2 semantic finding SF-T01 (completion is self-asserted) as its own item because it carries a distinct business meaning; carried gaps G-2 and G-4. Folded: Lane A G-1 (no controllers) → C14; G-3 (view XML partly examined) → C13; G-A1-1 → C11; G-A1-2 → C04; SF-T02 → C05; SF-T03 → C10; SF-T04 → C06; SF-T05 → C01; CRQ-WTOUR-01 → C11; CRQ-WTOUR-02 → C05; CRQ-WTOUR-03 → C04; CRQ-WTOUR-04 → C06; CRQ-WTOUR-05 → C10.

## 2. Reconciliation table

PC = proof case in `G01_PROOF/G01_WEB_TOUR_PROOF_20260927.md`. SOURCE cases (PC-WTOUR-04..14) executed; RUNTIME cases (PC-WTOUR-01..03) NOT-EXECUTED (device offline).

| REC ID | Item | A1 (claim / conf.) | A2 verdict | REC class | Basis for class | Lane B | Proof link | QID lineage (MODULE `web_tour`) |
|---|---|---|---|---|---|---|---|---|
| REC-WTOUR-01 | C01 (+SF-T05) | Onboarding + scripted walkthroughs; depends on web only; auto-install; LGPL; one engine for onboarding and tests / HIGH | VERIFIED | MATCH | PC-WTOUR-14 PASS | NOT_APPLICABLE | PC-WTOUR-14 | — |
| REC-WTOUR-02 | C02 | Guide fields (unique name, start URL, computed sharing link, translatable completion message, sequence, custom flag, consumed users); steps cascade with guide / HIGH | VERIFIED (+completion message is HTML; sharing link not encoded — OM-T02) | MATCH | Agreement; additions do not disagree | NOT_APPLICABLE | PC-WTOUR-13 | Q001, Q009, Q010, Q011, Q013, Q014, Q015, Q017, Q018, Q019, Q035 |
| REC-WTOUR-03 | C03 | Current guide only for internal users with onboarding on; first non-custom unconsumed in order / HIGH | VERIFIED (order: sequence, name, id) | MATCH | PC-WTOUR-04 PASS | UNCORROBORATED | PC-WTOUR-04 | Q002, Q004, Q005, Q006, Q007, Q008 |
| REC-WTOUR-04 | C04 (+G-A1-2, CRQ-WTOUR-03) | Consume: by name; sudo set-link; unknown name silent; idempotent / HIGH (logic) / LOW (concurrency) | VERIFIED; concurrency unverified (PR-T01) | UNKNOWN_PENDING_PROOF | Logic re-read (PC-WTOUR-05 PASS). Concurrent consumption is database/runtime behaviour | UNCORROBORATED | PC-WTOUR-05; PC-WTOUR-01 | Q003, Q004, Q020, Q021, Q023, Q028, Q034, Q040 |
| REC-WTOUR-05 | C05 (+SF-T02, CRQ-WTOUR-02) | Consumption per user DB-wide, no company dimension / HIGH | VERIFIED (extended: guides themselves have no company field) | MATCH | A2 extends in the same direction (PC-WTOUR-11 PASS). CRQ-WTOUR-02 remains a design decision | UNCORROBORATED | PC-WTOUR-11 | Q003, Q034 |
| REC-WTOUR-06 | C06 (+SF-T04, CRQ-WTOUR-04) | Onboarding default true only for admins with no demo data and no test / HIGH | VERIFIED (nuance: "admin" = Access-Rights admin or superuser) | MATCH | Nuance does not disagree (PC-WTOUR-10 PASS) | UNCORROBORATED | PC-WTOUR-10 | — |
| REC-WTOUR-07 | C07 | Self-toggle of own flag under sudo / HIGH | VERIFIED (+OM-T05) | MATCH | PC-WTOUR-10 PASS | UNCORROBORATED | PC-WTOUR-10 | Q005 |
| REC-WTOUR-08 | C08 | System group CRUD on guides/steps; internal users read-only; no record rules / HIGH | VERIFIED | MATCH | PC-WTOUR-08 PASS | NOT_APPLICABLE | PC-WTOUR-08 | — |
| REC-WTOUR-09 | C09 | By-name retrieval and JSON builder are public, RPC-callable; every internal user can read every guide / HIGH | **PARTIAL** — RISK holds; the JSON builder is private and reachable only via the by-name and current-guide methods | **CONTRADICTION** (A1 vs A2) — OPEN | Callable surface differs. Proof re-read supports A2 (PC-WTOUR-12 PASS). Both preserved | UNCORROBORATED | PC-WTOUR-12 | Q012, Q032 |
| REC-WTOUR-10 | C10 (+SF-T03, CRQ-WTOUR-05) | Export: steps structurally serialised; name and URL interpolated directly into script / HIGH (construction) / LOW (exploitability) | VERIFIED (exploitability bounded by system-group authoring; supply-chain integrity concern) | UNKNOWN_PENDING_PROOF | Construction confirmed (PC-WTOUR-06 PASS). The generated-file outcome for a quote-bearing name/URL is runtime (PR-T03) | UNCORROBORATED | PC-WTOUR-06; PC-WTOUR-03 | Q009, Q024, Q025 |
| REC-WTOUR-11 | C11 (+G-A1-1, CRQ-WTOUR-01) — "Export JS" by read-only users | WHAT: code server action bound to guide form, no group; export public, runs as caller. RISK: read-only internal user **might** trigger export and create an attachment / MED | **PARTIAL** — WHAT confirmed; **RISK refuted statically** (server action without groups needs write on its model; linked attachment create needs write on the record) | **CONTRADICTION** (A1 RISK vs A2) — RESOLVED AT SOURCE, RUNTIME PENDING | A2's refutation is supported by the Proof re-read of the base run guard and attachment create check (PC-WTOUR-07 PASS) and by the ACL rows (PC-WTOUR-08 PASS). A1's hypothesis is preserved unedited. Runtime confirmation (PR-T02) pending | UNCORROBORATED | PC-WTOUR-07, 08, 09; PC-WTOUR-02 | Q040 |
| REC-WTOUR-12 | C12 | Export does not touch consumed progress / HIGH | VERIFIED | MATCH | Agreement (export body re-read in PC-WTOUR-06) | NOT_APPLICABLE | PC-WTOUR-06 | Q026 |
| REC-WTOUR-13 | C13 (+G-3) | Menu under a technical parent from base; no menu-level group / HIGH (line) / MED (inherited) | VERIFIED; inherited parent visibility not re-read | MATCH | Line-level agreement (PC-WTOUR-09 PASS). Inherited visibility remains outside this module | NOT_APPLICABLE | PC-WTOUR-09 | — |
| REC-WTOUR-14 | C14 (+Lane A G-1) | No HTTP controllers; session bootstrap extended with flag and current guide / HIGH | VERIFIED | MATCH | PC-WTOUR-14 PASS | NOT_APPLICABLE | PC-WTOUR-14 | — |
| REC-WTOUR-15 | C15 | No crons, no config parameters / HIGH | VERIFIED | MATCH | PC-WTOUR-14 PASS (keyword search) | NOT_APPLICABLE | PC-WTOUR-14 | — |
| REC-WTOUR-16 | OM-T01 | (not stated) | OM-T01 LOW — each export creates a new attachment, no dedup; readable by guide readers | MATCH | New attachment per call confirmed (PC-WTOUR-06). Readability follows the attachment read inheritance A2 read; not separately re-read | UNCORROBORATED | PC-WTOUR-06 | Q024, Q027 |
| REC-WTOUR-17 | OM-T02 | (not stated) | OM-T02 LOW — sharing link embeds raw name without URL encoding | MATCH | PC-WTOUR-13 PASS | UNCORROBORATED | PC-WTOUR-13 | Q010, Q011 |
| REC-WTOUR-18 | OM-T03 | (not stated) | OM-T03 INFO — progress bound to record not name; delete drops progress rows | UNKNOWN_PENDING_PROOF | Record-id binding visible in consume/selection (PC-WTOUR-04/05). Relation-row removal on delete is ORM behaviour in base, not read; no predeclared case — carried for A3/runtime | UNCORROBORATED | — | Q029 |
| REC-WTOUR-19 | OM-T04 | (not stated) | OM-T04 LOW — current-guide search on every session-info build | MATCH | Session extension re-read (PC-WTOUR-14 PASS) | UNCORROBORATED | PC-WTOUR-14 | Q039 |
| REC-WTOUR-20 | OM-T05 | (C07 addition) | OM-T05 LOW — self-toggle has no internal-user check; portal users can call it | MATCH | PC-WTOUR-10 PASS | UNCORROBORATED | PC-WTOUR-10 | Q005 |
| REC-WTOUR-21 | OM-T06 | (not stated) | OM-T06 LOW — by-name retrieval returns custom guides; nonexistent name errors in private builder, not clean not-found | MATCH | Static: the by-name method passes an empty set to the builder, which indexes the first read row (PC-WTOUR-12 re-read). User-facing error form not runtime-checked | UNCORROBORATED | PC-WTOUR-12 | Q012 |
| REC-WTOUR-22 | SF-T01 | (C04 framing: unknown names ignored) | SF-T01 — "consumed" is a client-asserted dismissal marker, not training evidence | MATCH | Consume accepts any existing name with no step verification (PC-WTOUR-05 PASS). Consistent with A1 C04 | UNCORROBORATED | PC-WTOUR-05 | Q028, Q030, Q031 |
| REC-WTOUR-23 | G-2 | JS client (runner, pointer, recorder) not studied | VERIFIED as gap | GAP | Client-side step execution and guards unevidenced | NOT_APPLICABLE | — | — |
| REC-WTOUR-24 | G-4 | Tests and static assets not reviewed | VERIFIED as gap | GAP | — | NOT_APPLICABLE | — | — |

### 2.1 Class counts

| Class | Count | Items |
|---|---|---|
| MATCH | 17 | C01, C02, C03, C05, C06, C07, C08, C12, C13, C14, C15, OM-T01, OM-T02, OM-T04, OM-T05, OM-T06, SF-T01 |
| CONTRADICTION | 2 | C09 (A1 vs A2 — OPEN); C11 (A1 RISK vs A2 — RESOLVED AT SOURCE, RUNTIME PENDING) |
| UNKNOWN_PENDING_PROOF | 3 | C04, C10, OM-T03 |
| GAP | 2 | G-2, G-4 |
| **Total** | **24** | 15 A1 claims + 6 A2 omissions + 1 A2 semantic finding + 2 carried gaps |

Lane B column: UNCORROBORATED 15, NOT_APPLICABLE 9 (C01, C02, C08, C12, C13, C14, C15, G-2, G-4). No FAIL for absence.

### 2.2 Contradiction handling (both sources preserved)

- **C11 — Export JS by read-only users.** A1 hypothesised a possible bypass (MED); A2 refuted it statically; Proof re-read agrees with A2. It is recorded RESOLVED AT SOURCE only; PC-WTOUR-02 (runtime) is required before the item can be treated as closed. A1's text is not rewritten.
- **C09.** A1 said the JSON builder is public; A2 and the Proof re-read show it is private. The RISK (all internal users read all guides) is agreed. OPEN for A3 because the surfaces differ.

## 3. QID lineage map (frozen bank; lineage only, not answers)

Join key: MODULE `web_tour` + QID + freeze hash `cc81bc57f3686bfec5eda5fff354599e4d2ba5a9855078e9c2eaa13a6ca91bd3`.

| QID | Topic (paraphrased) | Mapped REC items |
|---|---|---|
| G01-WEB_TOUR-Q001 | Unique guide name | REC-02 (C02) |
| G01-WEB_TOUR-Q002 | Next guide excludes completed | REC-03 (C03) |
| G01-WEB_TOUR-Q003 | Completion only for the consumer | REC-04 (C04), REC-05 (C05) |
| G01-WEB_TOUR-Q004 | Internal-user population only | REC-03 (C03), REC-04 (C04) |
| G01-WEB_TOUR-Q005 | Disabling guidance stops selection | REC-03 (C03), REC-07 (C07), REC-20 (OM-T05) |
| G01-WEB_TOUR-Q006 | Custom guides not auto-queued | REC-03 (C03) |
| G01-WEB_TOUR-Q007 | Deterministic by sequence | REC-03 (C03) |
| G01-WEB_TOUR-Q008 | Deterministic on sequence ties | REC-03 (C03) |
| G01-WEB_TOUR-Q009 | Start location preserved | REC-02 (C02), REC-10 (C10) |
| G01-WEB_TOUR-Q010 | Sharing link correctness | REC-02 (C02), REC-17 (OM-T02) |
| G01-WEB_TOUR-Q011 | Rename updates sharing link | REC-02 (C02), REC-17 (OM-T02) |
| G01-WEB_TOUR-Q012 | Fetch by name only if exists | REC-09 (C09), REC-21 (OM-T06) |
| G01-WEB_TOUR-Q013 | Completion message rendered | REC-02 (C02) |
| G01-WEB_TOUR-Q014 | Step ordering | REC-02 (C02) |
| G01-WEB_TOUR-Q015 | Trigger preserved | REC-02 (C02) |
| G01-WEB_TOUR-Q017 | Tooltip position | REC-02 (C02) |
| G01-WEB_TOUR-Q018 | Delete removes dependent steps | REC-02 (C02) |
| G01-WEB_TOUR-Q019 | Delete does not touch other guides' steps | REC-02 (C02) |
| G01-WEB_TOUR-Q020 | Repeated completion no duplicates | REC-04 (C04) |
| G01-WEB_TOUR-Q021 | Concurrent completion converges | REC-04 (C04) |
| G01-WEB_TOUR-Q023 | Completion + next-guide coherence | REC-04 (C04) |
| G01-WEB_TOUR-Q024 | Export file tied to guide | REC-10 (C10), REC-16 (OM-T01) |
| G01-WEB_TOUR-Q025 | Export preserves start and order | REC-10 (C10) |
| G01-WEB_TOUR-Q026 | Export does not alter completion | REC-12 (C12) |
| G01-WEB_TOUR-Q027 | Repeated exports traceable | REC-16 (OM-T01) |
| G01-WEB_TOUR-Q028 | Consume only existing guides | REC-04 (C04), REC-22 (SF-T01) |
| G01-WEB_TOUR-Q029 | Completion after rename | REC-18 (OM-T03) |
| G01-WEB_TOUR-Q030 | Completion after step changes | REC-22 (SF-T01) |
| G01-WEB_TOUR-Q031 | Empty guide / false completion impression | REC-22 (SF-T01) |
| G01-WEB_TOUR-Q032 | Payload minimality | REC-09 (C09) |
| G01-WEB_TOUR-Q034 | Own history, not shared state | REC-04 (C04), REC-05 (C05) |
| G01-WEB_TOUR-Q035 | Translation keeps identity/history | REC-02 (C02) |
| G01-WEB_TOUR-Q039 | Heavy activity isolation | REC-19 (OM-T04) |
| G01-WEB_TOUR-Q040 | Attribution of completion/export | REC-04 (C04), REC-11 (C11) |

**Mapped: 34 QIDs.** **No evidence yet: 6 QIDs**, namely Q016 (step with no body content), Q022 (concurrent next-guide requests), Q033 (internal identifiers in step payload), Q036 (translated step semantics), Q037 (malformed step action bounded), Q038 (long guide without silent truncation). No mapping answers a QID.

## 4. Handoff

- To: PROOF (Stage 2, same run, separate record): `G01_PROOF/G01_WEB_TOUR_PROOF_20260927.md`.
- Proof addresses the 3 UNKNOWN_PENDING_PROOF and 2 CONTRADICTION items at SOURCE layer where possible, and holds PR-T01..PR-T03 as ready-to-run RUNTIME cases. OM-T03 has no predeclared case and is carried. The 2 GAP items are carried forward.

## 5. Limitations

- REC used only the inputs in 0.1 and the static proof results from Stage 2. No runtime evidence exists.
- QID mapping is topical lineage judged by this controller; not a coverage measure. No Formal Coverage, no percentages.
- The bank is below the governed MVQ floor of 48 (freeze replay record); this is a GMVQ/MASTER matter and does not change REC classes.
