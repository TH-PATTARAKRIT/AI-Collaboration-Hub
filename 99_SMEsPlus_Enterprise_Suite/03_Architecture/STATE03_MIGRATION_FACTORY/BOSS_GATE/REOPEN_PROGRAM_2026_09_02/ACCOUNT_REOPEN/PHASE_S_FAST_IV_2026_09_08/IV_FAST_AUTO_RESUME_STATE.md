# IV FAST — AUTO RESUME STATE

## Current state

| | |
|---|---|
| Session | `[SMEPLUS-26-09-08-ACC-PHASE-S-FAST-FINAL-CLOSEOUT-001]` |
| Branch | `audit/account-phase-s-fast-iv-2026-09-08-001` |
| Executing model | **Claude Opus 5 — not the appointed verifier** |
| Appointed verifier | **ChatGPT GPT-5.6 Sol**, lineage `audit/account-phase-s-independent-gpt56sol-2026-09-07-002` @ `9a5699e` |
| Terminal state | `IV-CLOSEOUT-B — BOUNDED MATERIAL BLOCKER REMAINS — EXACT ITEM NAMED` |
| RC results | 0 PASS · 0 FAIL · **6 HOLD** |
| `PHASE S` | **NOT CLOSED** |

## NEXT EXACT ACTION

**The next action does not belong to this lineage.** `[[smeplus-resume-state-is-an-instruction]]`
records that a prior round's NEXT EXACT ACTION sat unconsumed for a whole round — so it is stated
here as an address, not a task list for whoever reads next.

**Addressed to Boss:** decide `B-1`, `B-2`, `B-3` in `11_` §3. **`B-1` is unblockable today.**

**Addressed to ChatGPT GPT-5.6 Sol, on lineage `-002`, if Boss answers `B-1`:**

1. Resume on `-002`, not on this branch. This branch is **supporting evidence, not a substitute
   lineage**, and its author is disqualified from every lane.
2. Execute Lane A in any order — **no host is required**: `RC-02` @ `9d4ecdc`, `RC-03` @ `692ea27`,
   `RC-04` @ `b5f5a21`. Scope for each is restated verbatim at `02_`/`03_`/`04_` §1.
3. Do **not** adopt any figure from `07_`, `05_` §4 or the owner packages as a result. The SHA-256
   verifications are input-integrity facts; the owner's `169,143` and every `0` in the tolerance
   ladder are **published to be contradicted**.
4. On Lane B release, execute `RC-01` → `RC-05` → `RC-06`. `05_` §5 names the exact
   `pg_restore` 18.6 path; do not let a different `pg_restore` enter from `PATH`.

## Frozen inputs for the resume, all read back at 40 characters

```
RC-01  2079a2594a6a76eb91bdb528f22eaf928d42c0d6   corr/p09-phase-s-final-2026-09-07-001
RC-02  9d4ecdc744fbbb0e502a0b907f59c301bdf7812c   corr/p11-phase-s-remediation-2026-09-07-001
RC-03  692ea27e11533bc72ef0123fa4d1e3524179bf6e   corr/p06-iev-phase-s-final-2026-09-07-001
RC-04  b5f5a211763568a4212d08954c835412f7728a0a   corr/p06-source-phase-s-final-2026-09-07-001
RC-05  e368d11da6f7e4973469ff5608d676ec2d13811c   corr/p08-phase-s-rc05-prep-2026-09-07-001
RC-06  9d4ecdc744fbbb0e502a0b907f59c301bdf7812c   (depends on RC-05)
RC-07  d685176c2416210dfb67c01d862a911741530949   NOT REQUIRED
handoff 0941161824f4d447d9e0816e492a90b99bcfaecc  blob 961b2ecfd11d29f34a7de5bbcdd1664547673453
BOSS   6cb99464c4a3b9065c7cd9ae5014c13a7d6968b7   Q-BOSS-03 + verifier appointment
BOSS   2930723fbd45d8c4dada26197963ad6285d6c502   Q-BOSS-02 structural independence
P07    ee2be30ebf155e241510b3c7133c69419eb060a0   unmoved
```

## What must NOT be resumed

No Phase SA, no Phase A/B/C, no Functional Design, no schema or API design, no implementation, no
merge, no release, no peer-owner mutation, no Veto self-discharge, **no declaration that Phase S is
CLOSED.**
