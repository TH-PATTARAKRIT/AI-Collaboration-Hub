# 02 — Package Enumeration and SHA-256 Reproduction

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Enumerate A0–A20 at the frozen commit and independently reproduce A19's manifest | Independent Evidence Reviewer | This artifact | 2026-09-01 | Boss | **VERIFIED — 20/20 EXACT MATCH** | Confirms package integrity; no tampering or drift detected |

## 1. Directory enumeration

`ls -la` of `.../DEEP_RESEARCH_DR002/EXECUTION/` at commit `b31597f` returned exactly 21 physical files: `A0` through `A20` inclusive (`A1`–`A9`, `A10`–`A20`), with `A19` being the `.txt` manifest and the other 20 being `.md` deliverables. This matches the "expected controlled package A0–A20, A19 = manifest" description — verified by direct listing, not assumed from the prompt's own description of itself.

## 2. Independent SHA-256 reproduction

Command run (from `EXECUTION/`, exactly as A19's own header documents as the reproduction procedure):

```
find . -maxdepth 1 -type f -name "*.md" | sed 's#^\./##' | sort | xargs shasum -a 256
```

Result: **20 hashes computed, diffed against the 20 entries in `A19_INVENTORY_DEEP_RESEARCH_SHA256_MANIFEST.txt`. Zero differences.** Every hash matches exactly, character-for-character, including the trailing `-` sha256sum-with-name column-alignment format A19 itself uses.

| Check | Result |
|---|---|
| Missing paths (in manifest, not on disk) | 0 |
| Unexpected paths (on disk, not in manifest) | 0 |
| Duplicate paths | 0 |
| Hash mismatches | 0 |

## 3. Manifest self-reference boundary

A19 documents its own limitation explicitly: "a manifest file cannot self-hash," so it covers the 20 other deliverables (A0–A18, A20) and does not list a hash for itself. This review confirms that boundary is genuine and not a way to hide tampering: `A19`'s own byte content was read directly (not merely hash-compared) as part of [Phase 2 full-package read], and its header's documented regeneration procedure was executed verbatim by this review with an identical result — meaning a third party (this review) can independently regenerate the same 20 hashes from the same procedure, which is the practical substitute for a manifest self-hash.

Physical file count reconciliation: 21 files in `EXECUTION/` = 20 covered by A19 + A19 itself. Matches A19's own stated count exactly.

## 4. Disposition

**Package integrity: VERIFIED.** The frozen TEAM A DR-002 evidence package has not been altered, truncated, or substituted between the commit's creation and this independent review's read of it. This finding is a precondition for every subsequent finding in this review — all downstream verdicts in [03](03_IER003_PRIMARY_CLAIM_REPERFORMANCE_REPORT.md)–[16](16_IER003_BOSS_GATE_RECOMMENDATION.md) are verdicts about the *content* of a package now confirmed to be exactly what TEAM A committed.

No Evidence = No Progress.
