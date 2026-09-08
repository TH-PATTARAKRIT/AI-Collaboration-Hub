# [SMEPLUS-26-09-08-ACC-PHASE-S-BOUND-CORR-RELEASE-001]
# NEXT PROMPT — PHASE S BOUNDED CORRECTION RELEASE

Status: **PREPARED — REQUIRES BOSS RELEASE DECISION**
Boss: Sole Final Approver
Parent IV terminal: `IV-CLOSEOUT-B — BOUNDED MATERIAL BLOCKER REMAINS — EXACT ITEMS NAMED`
Verifier branch: `audit/account-phase-s-gpt56sol-b123-2026-09-08-001`

## Purpose
Release only the bounded owner corrections independently identified by GPT-5.6 Sol. This is not a reset, not a new research wave, and not authority to start the next phase.

## Wave 1 — independent owner corrections, may execute in parallel after Boss release
1. P06: `CORRECTION_PROMPTS/P06_RC04_OWNER_BOUNDED_CORRECTION_PROMPT.md`
2. P09: `CORRECTION_PROMPTS/P09_RC01_OWNER_BOUNDED_CORRECTION_PROMPT.md`
3. P08: `CORRECTION_PROMPTS/P08_RC05_OWNER_BOUNDED_CORRECTION_PROMPT.md`

Each owner must publish a new immutable SHA and stop for fresh GPT-5.6 Sol delta challenge. Owners may not challenge or certify their own repair.

## Wave 2 — P11 dependent propagation
Only after final corrected P08/P09 SHAs exist:
4. P11: `CORRECTION_PROMPTS/P11_RC06_OWNER_BOUNDED_CORRECTION_PROMPT.md`

## Wave 3 — P11 pre-existing Phase S closure blockers
5. P11: `CORRECTION_PROMPTS/P11_B35_B36_PHASE_S_CLOSURE_CORR4_PROMPT.md`

This removes the P11 B-35/B-36 closure blockers and dispositions B-39 as a version split. It may consume named peer evidence read-only but may not mutate peers.

## Verification return path
After every owner publication:
- GPT-5.6 Sol fresh-challenges only changed material surfaces plus proven propagation surfaces;
- no repeated full research without material delta;
- failed delta returns to the exact owner only;
- passing deltas return to cross-package verification → Veto disposition → closure criteria.

## Final stop
If all closure criteria pass:
`CP-SC-14 — READY FOR BOSS PHASE S FINAL DECISION`.

Otherwise:
`IV-CLOSEOUT-B — BOUNDED MATERIAL BLOCKER REMAINS — EXACT ITEM NAMED`.

Do not start Functional Design, Phase SA/A/B/C, implementation, merge, or release. AI does not declare Phase S closed.