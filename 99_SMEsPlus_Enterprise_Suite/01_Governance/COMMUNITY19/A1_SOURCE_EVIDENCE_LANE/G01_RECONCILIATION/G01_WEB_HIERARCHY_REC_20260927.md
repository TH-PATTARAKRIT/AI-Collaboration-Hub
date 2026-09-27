# G01 PLATFORM_BASE — Module `web_hierarchy` — RECONCILIATION (Stage 1)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of REC + PROOF; Proof recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `web_hierarchy` |
| Date | 2026-09-27 (intake 2026-09-27T15:06:49Z) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/web_hierarchy/`) |
| Question lineage | **No module MVQ bank exists** (GMVQ backlog, per `QUESTION_GATE_G01_FREEZE_REPLAY_20260927.md` item 6). **MVQ lineage: NOT A3-ELIGIBLE (bank absent).** Lineage lens = Standard 55 only (W1-STD). |
| Lane B | None exists (search recorded in section 3) |
| Next stage | PROOF → `G01_PROOF/G01_WEB_HIERARCHY_PROOF_20260927.md` |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (17 REC items: 10 MATCH, 6 GAP, 0 CONTRADICTION, 1 UNKNOWN_PENDING_PROOF) |

Format reference: `G01_RECONCILIATION/G01_BUS_REC_20260927.md` and `G01_RESOURCE_REC_20260927.md`.

## 2. Intake (immutable inputs, sha256 recorded at intake)

Paths are relative to `99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/`.

| Input | Path | sha256 | Check |
|---|---|---|---|
| Lane A | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_WEB_HIERARCHY_LANE_A_PASS1_20260927.md` | `ec340b9b9d84e1f96a5e3a1c029e9dcc6bd086e4e345cacf7879db9f7adf74ac` | Equals the value recorded in the A1 and A2 headers |
| A1 | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_WEB_HIERARCHY_A1_PACKAGE_20260927.md` | `45c325c42cd33aca747b18e11875086246257c9a1ef289453c53eef2115434a2` | Equals the value recorded in the A2 header |
| A2 | `A1_SOURCE_EVIDENCE_LANE/G01_A2_REVIEWS/G01_WEB_HIERARCHY_A2_REVIEW_20260927.md` | `48bdd133401eca8a9353e8f386086b5defab97984cc54625e4c02ac3b6f41f17` | A2 PASS WITH FINDINGS; 12 claims (11 VERIFIED, 1 PARTIAL: C10); 6 omissions (OM-W01..W06); 7 proof requirements (PR-WHIR-01..07) |
| Standard 55 | `GMVQ/G01_PLATFORM_BASE/QUESTION_BANK_STANDARD_55_V2.00.md` | `f6726f111932aecce4432daf3e412d0c9de3291fa45fa8908e9e89ee79cb540d` | Equals the `FREEZE_W1-STD.json` entry |
| Freeze manifest (STD) | `GMVQ/G01_PLATFORM_BASE/FREEZE_W1-STD.json` | `370b92b43d56a99d6e6e444916356eb56e305fdf6bb86b4c7cd0d885a7ff317d` | `freeze_hash` `c64693eee3957388907637ad028ebdeea6fbeb19a093d1c459c5289f45f5c213` recomputed with the canonical formula — MATCH; `web_hierarchy` is in the module list |

Inputs were only read; none edited. No git operations.

## 3. Lane B evidence-pool search (recorded)

Same search as the `onboarding` REC section 3 (log `laneb_search.txt` sha256 `21b8a78d400b23d6da3f2ecdefd7b315143b81f8b6f2b73c9927bd6802d0ce7f`): 4 filename hits (none mentions `web_hierarchy`), 22 content hits (none a runtime observation). Runtime device OFFLINE since 2026-09-24T12:53Z. **Result: no Lane B runtime evidence exists for `web_hierarchy`.** Nothing is FAIL for lack of Lane B.

## 4. Classification rules applied

Same as the `onboarding` REC section 4.

## 5. Reconciliation table

C01–C12 are the A1 claims `A1-G01-WHIR-Cnn`. OM-W02 (parent inclusion bypasses search filtering) is the same finding as the C10 PARTIAL and is folded into REC-WHIR-10. **No QID is answered.**

| REC ID | Source item | A1 position (summary) | A2 verdict / correction | REC class | Lane B | Proof link | MODULE+STD-QID lineage |
|---|---|---|---|---|---|---|---|
| REC-WHIR-01 | C01 | Hidden technical module adding a hierarchy view type; depends on `web`; no data, no tables | VERIFIED | MATCH | NOT_APPLICABLE | — | web_hierarchy+STD-Q01 |
| REC-WHIR-02 | C02 | Hierarchy view mode on action view lines cascades on uninstall (configuration lost by design) | VERIFIED | MATCH | NOT_APPLICABLE | — | web_hierarchy+STD-Q53 |
| REC-WHIR-03 | C03 | View type registered; template-based; default icon | VERIFIED | MATCH | NOT_APPLICABLE | — | — (no clear fit) |
| REC-WHIR-04 | C04 | Root attribute allow-list; only field children + one templates node; skipped when not validating | VERIFIED; refinement: names only, not values or template content (REC-WHIR-16) | MATCH | UNCORROBORATED | — | web_hierarchy+STD-Q08 |
| REC-WHIR-05 | C05 | Parent field not required and not type-checked server-side | VERIFIED | MATCH | UNCORROBORATED | (PR-WHIR-03) | web_hierarchy+STD-Q05, Q08 |
| REC-WHIR-06 | C06 | Read helper on every model; parent-field name unvalidated; caller specification mutated in place | VERIFIED | MATCH | UNCORROBORATED | (PR-WHIR-04) | web_hierarchy+STD-Q08 |
| REC-WHIR-07 | C07 | Single match: record + parent + siblings + own children (REFINEMENT-WHIR-1); multi: the set; none: empty | VERIFIED; grandparent never included | MATCH | UNCORROBORATED | — | web_hierarchy+STD-Q36 |
| REC-WHIR-08 | C08 | Child-id lists by grouped read under a synthetic key; single-match grouping excludes parents in the result | VERIFIED | MATCH | UNCORROBORATED | — | web_hierarchy+STD-Q38 |
| REC-WHIR-09 | C09 | No recursion, depth limit or cycle check; one expansion only | VERIFIED; self-parent edge in REC-WHIR-14 | MATCH | UNCORROBORATED | (PR-WHIR-06) | — (no clear fit) |
| REC-WHIR-10 | C10 (+ OM-W02) | No elevation; reads under caller rights; neighbourhoods may be silently truncated | PARTIAL — caller-rights scoping verified; "silent truncation" holds for siblings, children and child-id lists, but **not for the parent node**, which is added by following the relation (not by a search). An unreadable parent most likely raises an access error for the whole call (inference) | GAP | UNCORROBORATED | PR-WHIR-01, PR-WHIR-02 | web_hierarchy+STD-Q29, Q36, Q37, Q38 |
| REC-WHIR-11 | C11 | No routes; reachable via generic model-method RPC (inference, MED) | VERIFIED (public method) | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-WHIR-07 | web_hierarchy+STD-Q03, Q54 |
| REC-WHIR-12 | C12 | No cron, config, settings, constraints or Python tests | VERIFIED | MATCH | NOT_APPLICABLE | — | — (no clear fit) |
| REC-WHIR-13 | OM-W01 | (not in A1) | **Multi-match mode has no result limit**: every match is read, with child-id grouping for all (resource risk) | GAP | UNCORROBORATED | PR-WHIR-05 | web_hierarchy+STD-Q55 |
| REC-WHIR-14 | OM-W03 | (not in A1) | Self-referencing parent could appear twice (recordsets concatenated, not merged) (inference) | GAP | UNCORROBORATED | PR-WHIR-06 | — (no clear fit) |
| REC-WHIR-15 | OM-W04 | (not in A1) | Ordering argument also applied to the grouped read; display-name privilege in framework read not read | GAP | UNCORROBORATED | — | web_hierarchy+STD-Q36 |
| REC-WHIR-16 | OM-W05 | (not in A1) | View validation checks attribute names only; values not validated | GAP | NOT_APPLICABLE | — | web_hierarchy+STD-Q08 |
| REC-WHIR-17 | OM-W06 | (not in A1) | Leaf records carry no child-list key (absence, not empty list) | GAP | UNCORROBORATED | — | — (no clear fit) |

### Counts

| Class | Count | Items |
|---|---|---|
| MATCH | 10 | REC-WHIR-01, 02, 03, 04, 05, 06, 07, 08, 09, 12 |
| GAP | 6 | REC-WHIR-10, 13, 14, 15, 16, 17 |
| CONTRADICTION | 0 | — |
| UNKNOWN_PENDING_PROOF | 1 | REC-WHIR-11 |
| **Total** | **17** | 12 A1 claims + 5 A2 omission items |

Lane B column: NOT_APPLICABLE 5 (REC-WHIR-01, 02, 03, 12, 16); UNCORROBORATED 12. FAIL: 0.

## 6. MODULE+STD-QID lineage summary (Standard 55, W1-STD)

- **MVQ lineage: NOT A3-ELIGIBLE (bank absent).** A3 challenge at QID level is limited to Standard 55 until GMVQ authors a module bank.
- **Mapped STD-QIDs (11 distinct):** Q01, Q03, Q05, Q08, Q29, Q36, Q37, Q38, Q53, Q54, Q55. (Q08 and Q36 carry the most items.)
- REC items with no clear fit: REC-WHIR-03, 09, 12, 14, 17.
- Standard-55 sections B, C, D and F have no topical fit. Recorded as no fit, not as an answer.

## 7. Carried forward

- Evidence gaps GAP-1..GAP-3 (static inventory; client-side parent-field enforcement and cycle handling; consumer dependence on server validation) remain open.
- CRQ-WHIR-1..5 carried. A2 split of CRQ-WHIR-3 (silent truncation for children vs hard failure for an unreadable parent) recorded against REC-WHIR-10. New CRQ candidate for result bounding recorded against REC-WHIR-13.
- REFINEMENT-WHIR-1 (siblings **and** own children) confirmed by A1 and A2; carried in REC-WHIR-07.

## 8. Handoff to PROOF

All 7 A2 proof requirements (PR-WHIR-01..07) pass to Proof. Items needing proof: REC-WHIR-10, 11, 13, 14 (supplementary: REC-WHIR-05, 06, 09).

## 9. Limitations

- REC reconciles documents; the source re-read is Proof Stage 2. No Lane B evidence exists.
- No Formal Coverage; no percentages; no QID answered; no bank edited.
- Clean room: neutral summaries; identifiers are pointers; no code reproduced.
