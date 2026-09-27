# GMVQ CANDIDATE ROSTER-NOT-VERIFIED HOLDING AREA

**Status: CANDIDATE / ROSTER NOT VERIFIED / NOT FOR DOWNSTREAM CONSUMPTION**

Prepared: 2026-09-27/28 (Asia/Bangkok)
Prepared by: GMVQ (Question Factory role, this session)
Boss Decision reference: "PRESERVE HOLD + PRESERVE WORK AS NON-CANONICAL CANDIDATE" (2026-09-27, verbal/chat form, reproduced below)

## What this directory is

This directory holds GMVQ-authored G02–G16 question-bank artifacts and their supporting
registers, copied from the GMVQ device-local working area into this feature branch as
**CANDIDATE** material only, per explicit Boss instruction. It is a sibling of — and
strictly separate from — the canonical governed path:

`99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/GMVQ/`

Nothing in the canonical `GMVQ/` folder was modified, moved, or overwritten to create this
directory. In particular:

- `GMVQ/OVQDT_G02_G16_ROSTER_HOLD_20260925_1521.md` (commit `5a42fd85`) remains untouched
  and in force. This directory does NOT supersede, edit, or replace that HOLD document.
- `GMVQ/G01_PLATFORM_BASE/` (canonical, already-committed G01 material) remains untouched.
  No G01 content is duplicated or re-ingested here.

## Why this exists

Module-specific G02–G16 question banks depend on a canonical module roster
(`GROUP_STRUCTURE_V2_CORE.tsv`, expected SHA-256
`203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf`) that could not be
located/verified this session (gap **G-09**, consistent with the pre-existing HOLD document
above, which independently identified the same missing artifact). Because the roster cannot
be verified, module membership for G02–G16 is provisional/reconstructed, and Boss ruled that
work must be preserved but must NOT be treated as governed, frozen, or authoritative until
the roster is verified.

## Governing constraints (Boss Decision, verbatim intent — 7 points)

1. All authored artifacts in this directory are CANDIDATE / ROSTER NOT VERIFIED / NOT FOR
   DOWNSTREAM CONSUMPTION.
2. Ingestion into this feature branch is permitted only because: (a) this path is clearly
   separate from canonical governed banks; (b) every artifact here is marked
   CANDIDATE / ROSTER NOT VERIFIED; (c) MASTER, RED TEAM, and downstream consumers must NOT
   consume this directory as governed evidence; (d) nothing here is frozen or declared
   AUTHORING COMPLETE from a provisional roster; (e) SHA-256/provenance of every original
   file is preserved — see `00_INGEST_REGISTER.tsv`.
3. The existing HOLD document is not overwritten or superseded by this directory.
4. When `GROUP_STRUCTURE_V2_CORE.tsv` (or a Boss-approved equivalent canonical roster) is
   verified by SHA-256, G02–G16 module membership must be reconciled against it and each
   authored bank classified as MATCH / REMAP / REMOVE / NEW REQUIRED. Only MATCH/validated
   artifacts may then be promoted into the canonical `GMVQ/` path.
5. G01 is not touched by this directory and is not re-ingested.
6. Other GMVQ work not blocked by the roster issue continues under AUTO PROCESS; the GMVQ
   programme as a whole is not halted by this HOLD.
7. A separate git-push-credential issue on this device (see session report to Boss) is a
   technical matter only and does not change this governance disposition.

## What is NOT asserted by this directory

- No claim of Formal Coverage.
- No claim that any module-specific bank is frozen, governed, complete-and-verified, or
  ready for Lane A / Lane B start.
- No claim that MVQ-floor counts recorded in `00_INGEST_REGISTER.tsv` are anything other
  than a mechanical, reproducible count (grep count of lines beginning `QID:` per file);
  they are not an independent QA sign-off.
- No claim that groups listed with an existing audit-defect-queue file have had that queue's
  findings re-verified or closed this session — see each queue file directly.

## Contents

- `00_CANDIDATE_STATUS_README.md` — this file.
- `00_INGEST_REGISTER.tsv` — per-file ingest register (Group ID, Module ID/name, source and
  destination paths, source and destination SHA-256, mechanical bank question count, MVQ
  floor status, QA status, freeze status, blocker/status, source revision timestamp,
  ingestion disposition). SHA-256 of this register at time of writing:
  `559921a148a8f19e774f2d28ece933e949cd6fa41caf47dab6a7fbeafc0d4e46`
- `G02_IDENTITY_ACCESS/` … `G15_PRODUCTIVITY/` — copied question-bank `.md` files, one
  directory per group, `cp -p` byte-preserving copy from the GMVQ device-local working area.
- `00_REGISTERS_AND_AUDIT/` — supporting registers and group briefs referenced above.

## Integrity note

Source-to-destination SHA-256 comparison for all 154 ingested artifacts (147 question-bank
files + 7 supporting registers/briefs) was performed at build time: 0 hash mismatches,
0 missing sources. Full detail in `00_INGEST_REGISTER.tsv`. One filename correction was made
during this build: the supporting file is actually named
`G09_G11_INDEP_AUDIT_RECORD.md` at source (not `..._DEFECT_QUEUE_RECORD.md` as an earlier
listing assumed); it was located and ingested under its correct source name.

## Governance statement

This directory and its contents are PREPARED ONLY. They carry no Boss Final Approval, do not
authorize any merge, release, STATE closure, or gate approval, and do not constitute governed
or frozen evidence under project instructions §5.3 / §5.4. This is an execution/preservation
action taken under explicit Boss Decision, not an independent governance ruling.
