# SUPERSEDED — DO NOT USE (marked 2026-07-14)

Status: SUPERSEDED / CONFLICTING DUPLICATE
Authoritative replacement: repository-root copies under `99_SMEsPlus_Enterprise_Suite/`
Authoritative gate status: `CURRENT_GATE_STATUS.md` (HOLD — NEED EXECUTION EVIDENCE)

## Why this folder is marked

`ACC_GAP_CLOSURE_METADATA_FIX/` holds nested copies of Batch 01 governance files:

| Nested file | Compared to root copy |
|---|---|
| `ACC_GAP_CLOSURE_BATCH01_MANIFEST_SHA256.txt` | **DIFFERS** from the root manifest — a conflicting status source |
| `L99_REVIEW_BATCH_VERIFICATION_REPORT.md` | Identical to root at time of marking |
| `REVIEW_BATCH_INDEX.md` | Identical to root at time of marking |

Because the nested manifest disagrees with the authoritative root manifest
(`99_SMEsPlus_Enterprise_Suite/ACC_GAP_CLOSURE_BATCH01_MANIFEST_SHA256.txt`), this
folder is a duplicate/conflicting status source and must not be used for gate,
manifest, or verification decisions.

## Controlling rule

- The **root** `ACC_GAP_CLOSURE_BATCH01_MANIFEST_SHA256.txt` (frozen and rebuilt
  2026-07-14) is the single authoritative Batch 01 manifest.
- The files in this folder are retained for history only and are **not** authoritative.
- This marker does not delete or alter the historical copies; it only records that
  they are superseded and conflicting.

No gate is approved by this marker. Final status remains HOLD — NEED EXECUTION EVIDENCE.
