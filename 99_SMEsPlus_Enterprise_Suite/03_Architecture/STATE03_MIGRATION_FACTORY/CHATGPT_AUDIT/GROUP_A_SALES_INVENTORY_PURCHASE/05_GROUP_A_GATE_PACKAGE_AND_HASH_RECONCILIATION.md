> GROUP A — Sales + Inventory + Purchase | Independent Evidence Reviewer | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-31-GRPA-SIP-IER-004 | Cluster E — Gate Package / Hash / Remaining-Gap Consistency

# 05 — GATE PACKAGE AND HASH RECONCILIATION

## 01 — Independent SHA-256 recomputation

All 19 numbered evidence files plus both session-prompt files were exported directly from the frozen commit
(`git show 8b0993d824cf726fa52edd687272ff54b0977c42:<path>`) into a local scratch directory and hashed with
`shasum -a 256`, independently of any value already written in Team A's manifests.

**Result: 100% match.** All 19 hashes in `20_GROUP_A_FINAL_SHA256_MANIFEST.txt` (files 01–19) reproduced exactly
against the independently-computed values. Both session-prompt hashes (00a/00b) in `17_GROUP_A_EVIDENCE_MANIFEST.md`
also reproduced exactly. No mismatch, no missing file, no extra file.

```
Independently computed             Manifest 20 claim                    File
47ae338f...e3459d6   ==  47ae338f...e3459d6   01_SHARED_MASTER_DEPENDENCY_MAP.md
3728375f...5346054   ==  3728375f...5346054   02_INVENTORY_CAPABILITY_MODEL.md
28817fb0...bbaa8d33   ==  28817fb0...bbaa8d33   03_SALES_CAPABILITY_MODEL.md
a2ced563...9cbd9396   ==  a2ced563...9cbd9396   04_PURCHASE_CAPABILITY_MODEL.md
585141204929f...c45b   ==  585141204929f...c45b   05_INTEGRATED_E2E_LIFECYCLE_MAP.md
a1a4c402...913eb9f3b6f  ==  a1a4c402...913eb9f3b6f  06_CROSS_MODULE_EVENT_AND_DEPENDENCY_MAP.md
0579e819...db31ebf   ==  0579e819...db31ebf   07_BUSINESS_FACT_OWNERSHIP_AND_HANDOFF_MATRIX.md  [08 hash below]
5de88d50...db31ebf   ==  5de88d50...db31ebf   08_SOURCE_DATABASE_SEMANTIC_TRACEABILITY_MATRIX.md
4103c7df...481527a   ==  4103c7df...481527a   09_QUANTITY_SEMANTICS_REGISTER.md
0aacc494...932a3b   ==  0aacc494...932a3b   10_EXCEPTION_PARTIAL_RETURN_CANCELLATION_MATRIX.md
12b642a7...485979   ==  12b642a7...485979   11_THAILAND_BUSINESS_REALITY_AND_VARIATION_REGISTER.md
0a8a045f...b79b15c   ==  0a8a045f...b79b15c   12_PERSONA_USER_FITNESS_OBSERVATION_MATRIX.md
822a5b8e...4991c2   ==  822a5b8e...4991c2   13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md
b398c1d9...6b0d5   ==  b398c1d9...6b0d5   14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md
e6422295...c084da61f  ==  e6422295...c084da61f  15_EXTERNAL_DEPENDENCY_AND_SYSTEM_RISK_OBSERVATION_REGISTER.md
4f919023...955215c2   ==  4f919023...955215c2   16_FIT_GAP_CANDIDATE_PACK.md
c62d0d5c...451962e   ==  c62d0d5c...451962e   17_GROUP_A_EVIDENCE_MANIFEST.md
324a1dda...966a612   ==  324a1dda...966a612   18_TEAM_A_EVIDENCE_GATE_CANDIDATE_REPORT.md
23295b73...111808bd14  ==  23295b73...111808bd14  19_TEAM_A_CORRECTIVE_CLOSURE_REPORT.md
```
(Full 64-character values independently verified; abbreviated here for readability — see this review's own
`09_GROUP_A_INDEPENDENT_REVIEW_SHA256_MANIFEST.txt` methodology note for the exact recomputation command.)

**File 20 self-hash check**: confirmed file 20 correctly excludes itself — the file lists 01–19 only, and this
review's independent hash of `20_GROUP_A_FINAL_SHA256_MANIFEST.txt` itself (`2a3049c7...9ef38`) does not appear
inside the file, consistent with the documented self-hash limitation.

## 02 — Stale-statement check

**No newly-discovered stale statement was found.** The one wording overstatement that existed in this evidence
chain — `18_TEAM_A_EVIDENCE_GATE_CANDIDATE_REPORT.md`'s original "18/18, SHA-256 verified" phrasing, which
conflated the 16 content deliverables + 2 session prompts (18 items, correctly hashed) with the impression that
*all 18 numbered deliverable files* (which would need to include 17 and 18 themselves) were self-hashed — was
**already self-identified and corrected by Team A in CORR-003**, before this review began (see `18`'s §08 table
row, `17`'s new §01a section, and `19`'s item 8). This review independently confirms the correction is accurate:
16 content deliverables + 2 session prompts = 18 rows in manifest 17, which is what the file actually contains;
files 17/18/19/20 are separately and correctly covered (or self-excluded) via manifest 20. **This is recorded
here as a positive finding about Team A's own self-correction discipline, not as a defect newly found by this
review.**

## 03 — Cross-file count consistency

| Check | File 14 (Gap Register) | File 18 (Gate Report) | File 19 (Closure Report) | Consistent? |
|---|---|---|---|---|
| Critical count after CORR-003 | 0 (all 3 struck through, R6/R7/R8) | 0 (§05 addendum) | 0 (§07 table) | **Yes** |
| High count after CORR-003 | 3 open (#4, #5, #8) + 3 closed (struck through: #6/#7/#9 via R8/R7) | 3 (§05 addendum) | 3 — items 4, 5, 8 (§07 table) | **Yes** |
| Medium count | 10 (§03, includes 1 already-closed-before-CORR-003 item #17, correctly noted "listed for completeness") | not separately restated | 10, unchanged (§07 table) | **Yes** |
| Low count | 4 (§04) | not separately restated | 4, unchanged (§07 table) | **Yes** |
| Resolved (audit-trail) count | R1–R8 = 8, plus Cluster D wording fix = 9 (§05) | not separately restated | 9 (§07 table: "5 → 9") | **Yes** |

No inconsistency found across the three files' gap counts.

## 04 — "0 Critical" support check

Independently confirmed the "0 Critical" status is substantively earned, not merely re-labeled: all three
original Critical items (orphaned approval schema; Purchase cancellation cascade; `_run_buy()`/MTO/`'buy'`
registration) were independently re-derived from primary evidence by this review in Clusters A/B/C above and
found to hold. The status change from Critical→0 reflects real closure, not a definitional relabeling.

## 05 — Overall Cluster E verdict

**`VERIFIED`.** Hash integrity: 100% independently reproduced. Gate package internal consistency: no
contradiction found across files 14/18/19. No previously-undisclosed stale statement found — the one that
existed was already caught and corrected by Team A itself. See `06_GROUP_A_REMAINING_GAP_GATE_IMPACT_REGISTER.md`
for the remaining open-gap Gate-impact classification.
