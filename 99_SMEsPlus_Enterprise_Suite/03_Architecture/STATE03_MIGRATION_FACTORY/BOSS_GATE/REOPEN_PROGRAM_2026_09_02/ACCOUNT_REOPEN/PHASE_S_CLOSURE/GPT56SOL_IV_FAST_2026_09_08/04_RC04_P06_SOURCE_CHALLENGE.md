# 04_RC04_P06_SOURCE_CHALLENGE

RC: `RC-04` · Owner: P06 source · Frozen surface: `b5f5a211763568a4212d08954c835412f7728a0a`
Result: **`RC-FAIL — MATERIAL DEFECT FOUND`**

## Q-P06-03 independently reproduced
On the declared publication scopes:
- P06-B population = **67**;
- P06-OQ population = **68**;
- AASP-VETO population = **7** (`01…07`);
- `P06-B-58` is re-scaled from 16 to **21 author errors**.

The corrected source carriers for Q-P06-03 are consistent with these bounded counts.

## Q-P06-04 independently reproduced on the host archive
Population: `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons_archive`
- directories = **961**;
- corrected ERE search = **76 files**;
- positive control `bounce` = **66 files**;
- impossible-token negative control = **0**;
- widened `post-dated` spelling = **2 files**.

The previous archive negative is therefore correctly withdrawn; the concepts exist in the archived distribution and are absent from the loadable set, not from the entire v18 distribution.

## Material failure — stale validation control remains live
File:
`G02_RECOVERY_2026_09_06/P06_VERIFICATION_TOOL_DEFECT_REGISTER.md`

The live validation row still states:
- `65 P06-B-*`;
- max id = 65;
- contiguous = YES.

Nine lines later the same file defines/mentions `P06-B-66` and `P06-B-67`. Independent recursive enumeration returns **67 unique IDs, 1…67 contiguous, no gaps**.

This is a control-integrity defect: a validation row marked YES certifies a figure that the same frozen file supersedes.

## Required bounded correction
Correct only this validation carrier to **67**, retain 65 as marked-superseded lineage, re-run/publish contiguity enumeration, then fresh-challenge the changed validation row. Do not reopen Q-P06-03/04 research or reset P06.