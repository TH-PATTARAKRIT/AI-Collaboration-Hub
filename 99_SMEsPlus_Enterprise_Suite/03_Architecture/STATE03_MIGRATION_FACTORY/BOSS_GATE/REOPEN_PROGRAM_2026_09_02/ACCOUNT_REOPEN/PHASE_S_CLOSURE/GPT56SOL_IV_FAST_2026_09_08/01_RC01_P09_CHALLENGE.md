# 01_RC01_P09_CHALLENGE

RC: `RC-01` · Owner: P09 · Frozen surface: `2079a2594a6a76eb91bdb528f22eaf928d42c0d6`
Result: **`RC-FAIL — MATERIAL DEFECT FOUND`**

## Independent reproduction
The owner-published `q1.py` was re-executed against the declared host source root. Reproduced:
- reference-relation denominator: **192 files / 52 modules**;
- inside K-1: **23 / 14**;
- outside K-1: **169 / 52**;
- planning outside: **10 / 3** — 6 test, 4 non-test;
- non-planning B2 residue: **159 / 51**;
- `23 + 169 = 192`; `10 + 159 = 169`.

The L1/L2/L8 control instrument also re-executed successfully: K-2 and K-3 control tables held; K-2 planning result = `1 of 12`; K-3 outside = `169`, planning = `10`, B2 = `159`.

## Material findings
### RC01-F1 — M-1 rationale is internally false
`OWNER_QUEUE_2026_09_07/Q_P09_01_L4_AUTHORITY_RESOLUTION.md` states the reference relation is a fourth relation **disjoint from declaration/inheritance/K-1 by construction**. The same executed evidence gives **23 files inside K-1 that are also in the reference relation**. The universal disjointness statement is therefore false.

The narrower defensible statement is: **B2 is outside K-1 by the partition definition**. The arithmetic is not challenged; the authority rationale is.

### RC01-F2 — stale `CO-02b` carrier remains live
`FINAL_BOUNDED_COMPLETION_2026_09_06/P09_FINAL_BOUNDED_COMPLETION_REGISTER.md` still carries `CO-02b` as a live candidate handoff and uses present-tense consumption / `already shipped` language. The later L1-L8 authority withdraws that deployment wording and supersedes the earlier row, but the earlier carrier itself is not marked superseded.

### RC01-F3 — stale `CH-09` carrier remains live
`PHASE_S_DOMAIN_PURE_CLOSURE_2026_09_06/P09_CANDIDATE_HANDOFF_REGISTER.md` still carries `CH-09` as a current candidate-handoff row. The later authority says `CH-09 — TOMBSTONE / WITHDRAWN` with successors `CO-01`, `CO-02a`, `CO-03`. The source carrier was never marked tombstoned/superseded in place.

### RC01-F4 — false P11 publication negatives survive in three prior carriers
Uncorrected current-looking statements remain in:
1. `P09_04_DENOMINATOR_SIGN_PLATFORM_2026_09_05/P09_AUTO_RESUME_STATE.md`;
2. `SUPPLEMENT_CRITICAL_EVIDENCE_2026_09_05/S13_P09_ASSET_CONTRADICTION_REFRESH.md`;
3. `SUPPLEMENT_CRITICAL_EVIDENCE_2026_09_05/P09_AUTO_RESUME_STATE.md`.

They still say P11 has no published branch. P11 is published; later P09 files already withdraw this premise.

## Negative control on propagation
Exact-token search for P09 `CH-09` / `CO-02b` in frozen P06/P08/P11 ACCOUNT_REOPEN packages returned **0 exact peer citations** after excluding unrelated prefixed families such as `ACC-R-CH-09`. Therefore the stale P09 rows have not been proven to have closed a peer dependency.

## Gate impact
`M-2` is now independently executed and **fails**. `AAS+-VETO-04` remains undischarged. No reset is justified: correction is bounded to the exact carriers and rationale above.