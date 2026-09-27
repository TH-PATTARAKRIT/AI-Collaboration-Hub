# G01 PLATFORM_BASE — Module `html_builder` — RECONCILIATION (Stage 1)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of REC + PROOF; Proof recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `html_builder` |
| Date | 2026-09-27 (intake 2026-09-27T15:06:49Z) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/html_builder/`) |
| Question lineage | MVQ bank W1-B06 = **HOLD-LOCAL / FREEZE-INTEGRITY** (freeze hash not reproducible). **MVQ lineage: NOT A3-ELIGIBLE (gate HOLD).** Lineage lens used here = Standard 55 only (W1-STD). |
| Lane B | None exists (search recorded in section 3) |
| Next stage | PROOF → `G01_PROOF/G01_HTML_BUILDER_PROOF_20260927.md` |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (13 REC items: 7 MATCH, 5 GAP, 0 CONTRADICTION, 1 UNKNOWN_PENDING_PROOF) |

Format reference: `G01_RECONCILIATION/G01_BUS_REC_20260927.md` and `G01_RESOURCE_REC_20260927.md`.

## 2. Intake (immutable inputs, sha256 recorded at intake)

Paths are relative to `99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/`.

| Input | Path | sha256 | Check |
|---|---|---|---|
| Lane A | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_HTML_BUILDER_LANE_A_PASS1_20260927.md` | `76275bbb39379c2736d2b8411bdcb331771aa28f378bfef5c1eeb574f143deec` | Equals the value recorded in the A1 and A2 headers |
| A1 | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_HTML_BUILDER_A1_PACKAGE_20260927.md` | `2cfc3d1e75a6a3a7db1c123c5aac73ea87802aaeaef17e74c15e3d5b050a3332` | Equals the value recorded in the A2 header |
| A2 | `A1_SOURCE_EVIDENCE_LANE/G01_A2_REVIEWS/G01_HTML_BUILDER_A2_REVIEW_20260927.md` | `745b25b560cbcac864b19c59ab5f9f32db69e142db169e3f47ca279465760b3d` | A2 PASS WITH FINDINGS; 9 claims (8 VERIFIED, 1 PARTIAL: C08); 5 omissions (OM-H01..H05); 4 proof requirements (PR-HBLD-01..04) |
| MVQ bank (not used for lineage) | `GMVQ/G01_PLATFORM_BASE/G01_HTML_BUILDER_GMVQ_MVQ_40_V1.00_DRAFT.md` | `893a84d23035083c95d1da81dc12ce1559acba09093325b47f64ff8c2410ba56` | Equals the `FREEZE_W1-B06.json` bank entry, but the manifest `freeze_hash` `58e86d15…ba56`… does **not** reproduce with the canonical formula (recomputed `a01a5d72…7035`). Agrees with `QUESTION_GATE_G01_FREEZE_REPLAY_20260927.md`: HOLD-LOCAL. |
| Standard 55 | `GMVQ/G01_PLATFORM_BASE/QUESTION_BANK_STANDARD_55_V2.00.md` | `f6726f111932aecce4432daf3e412d0c9de3291fa45fa8908e9e89ee79cb540d` | Equals the `FREEZE_W1-STD.json` entry |
| Freeze manifest (STD) | `GMVQ/G01_PLATFORM_BASE/FREEZE_W1-STD.json` | `370b92b43d56a99d6e6e444916356eb56e305fdf6bb86b4c7cd0d885a7ff317d` | `freeze_hash` `c64693ee…f5c213` recomputed — MATCH; `html_builder` is in the module list |

Inputs were only read; none edited. No git operations.

## 3. Lane B evidence-pool search (recorded)

Same search as the `onboarding` REC section 3 (log `laneb_search.txt` sha256 `21b8a78d400b23d6da3f2ecdefd7b315143b81f8b6f2b73c9927bd6802d0ce7f`): 4 filename hits (none mentions `html_builder`), 22 content hits (all Lane A / A1 / A2 / REC / GMVQ / governance documents; none a runtime observation). Runtime device OFFLINE since 2026-09-24T12:53Z. **Result: no Lane B runtime evidence exists for `html_builder`.** Nothing is FAIL for lack of Lane B.

## 4. Classification rules applied

Same as the `onboarding` REC section 4 (MATCH / GAP / CONTRADICTION / UNKNOWN_PENDING_PROOF, with UNKNOWN_PENDING_PROOF used only where A2 classed the claim MISSING_REQUIRED_RUNTIME_PROOF).

## 5. Reconciliation table

C01–C09 are the A1 claims `A1-G01-HBLD-Cnn`. OM-H05 (translation count) is the same finding as the C08 PARTIAL and is folded into REC-HBLD-08. **No QID is answered.** MVQ lineage: NOT A3-ELIGIBLE (gate HOLD).

| REC ID | Source item | A1 position (summary) | A2 verdict / correction | REC class | Lane B | Proof link | MODULE+STD-QID lineage |
|---|---|---|---|---|---|---|---|
| REC-HBLD-01 | C01 | Reusable client-side HTML builder; declared consumers website builder and mass-mailing editor | VERIFIED | MATCH | NOT_APPLICABLE | — | html_builder+STD-Q01 |
| REC-HBLD-02 | C02 | No server-side Python (empty init; models/controllers 404) | VERIFIED (security path 404 too) | MATCH | NOT_APPLICABLE | — | html_builder+STD-Q03 |
| REC-HBLD-03 | C03 | No `data` key: no views, menus, ACL, rules, seed data, crons | VERIFIED | MATCH | NOT_APPLICABLE | — | — (no clear fit) |
| REC-HBLD-04 | C04 | Depends on base, `html_editor`, `mail`; mail only for a client helper | VERIFIED; refinement: helper looks like a JS test helper, which would make the coupling test-only (not established) | MATCH | NOT_APPLICABLE | (PR-HBLD-04) | — (no clear fit) |
| REC-HBLD-05 | C05 | Three new bundles + four contributions; builder bundle removes edit-only and dark SCSS | VERIFIED; refinement: removal covers every edit-pattern file, not only SCSS | MATCH | NOT_APPLICABLE | — | — (no clear fit) |
| REC-HBLD-06 | C06 | Only server-side guard is a post-install bundle test; separation not enforced at runtime | VERIFIED; the test is narrower than the removal rules (REC-HBLD-11) | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-HBLD-01 | — (no clear fit) |
| REC-HBLD-07 | C07 | Background SCSS injected into the public frontend bundle | VERIFIED | MATCH | UNCORROBORATED | (PR-HBLD-02) | — (no clear fit) |
| REC-HBLD-08 | C08 (+ OM-H05) | ≥ 79 static files with strings (32 JS, 47 XML); 528 message IDs | PARTIAL — 79/32/47 reproduce; **527** translatable entries (528 includes the header entry). Lower-bound framing stays correct | GAP | NOT_APPLICABLE | (PC-HBLD-07) | — (no clear fit) |
| REC-HBLD-09 | C09 | No groups/ACL/elevation; persistence authorization lives in other modules (unverified) | VERIFIED | MATCH | NOT_APPLICABLE | (PR-HBLD-03) | html_builder+STD-Q29, Q54 |
| REC-HBLD-10 | OM-H01 | (not in A1) | Variables contribution to the shared primary-variables bundle reaches every bundle compiled from it (wider than C07) | GAP | UNCORROBORATED | PR-HBLD-02 | — (no clear fit) |
| REC-HBLD-11 | OM-H02 | (not in A1) | Bundle test checks only the edit-SCSS suffix, not other edit-pattern files or dark SCSS | GAP | NOT_APPLICABLE | PR-HBLD-01 | — (no clear fit) |
| REC-HBLD-12 | OM-H03 | (Lane A noted; A1 omitted) | No installable/auto-install/application keys; module reached only through consumer dependencies | GAP | NOT_APPLICABLE | — | html_builder+STD-Q03 |
| REC-HBLD-13 | OM-H04 | (not in A1) | Unit-test bundle includes the full builder bundle | GAP | NOT_APPLICABLE | — | — (no clear fit) |

### Counts

| Class | Count | Items |
|---|---|---|
| MATCH | 7 | REC-HBLD-01, 02, 03, 04, 05, 07, 09 |
| GAP | 5 | REC-HBLD-08, 10, 11, 12, 13 |
| CONTRADICTION | 0 | — |
| UNKNOWN_PENDING_PROOF | 1 | REC-HBLD-06 |
| **Total** | **13** | 9 A1 claims + 4 A2 omission items |

Lane B column: NOT_APPLICABLE 10; UNCORROBORATED 3 (REC-HBLD-06, 07, 10). FAIL: 0.

## 6. MODULE+STD-QID lineage summary (Standard 55, W1-STD)

- **MVQ lineage (W1-B06 bank): NOT A3-ELIGIBLE (gate HOLD).** No MVQ QID mapped.
- **Mapped STD-QIDs (4 distinct):** Q01, Q03, Q29, Q54. The module is assets-only, so most Standard-55 questions (lifecycle, approval, accounting, tax, tenant, inventory) have no topical fit to server-side evidence here. This is recorded as no fit, not as an answer.
- REC items with no clear fit: REC-HBLD-03, 04, 05, 06, 07, 08, 10, 11, 13.

## 7. Carried forward

- Evidence gaps GAP-1..GAP-3 (client behaviour not analysed; static inventory is a lower bound; consumers not confirmed) remain open.
- CRQ-HBLD-1..3 carried unchanged. CRQ-HBLD-1 depends on PR-HBLD-04 (runtime vs test-only mail coupling).
- A2 business findings SF-H01..SF-H03 carried as context.

## 8. Handoff to PROOF

All 4 A2 proof requirements (PR-HBLD-01..04) pass to Proof, plus static checks for REC-HBLD-02 and REC-HBLD-08.

## 9. Limitations

- REC reconciles documents; the source re-read is Proof Stage 2. No Lane B evidence exists.
- No Formal Coverage; no percentages; no QID answered; no bank edited.
- Clean room: neutral summaries; identifiers are pointers; no code reproduced.
