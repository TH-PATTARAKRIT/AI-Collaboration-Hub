# B99 — Final checkpoint and restore cleanup (current authorized plan)

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** No V-level, Module/Function Complete, coverage percentage, denominator freeze, Gate PASS or Clean-Room approval is asserted. FORMAL COVERAGE = N/A until canonical denominator validation.

## 1. Restore cleanup evidence (closes the B00 §4 "Cleanup: OPEN" item)
| Check | Result (2026-10-02) |
|---|---|
| Original ZIP (`iTest19C_2026-09-21_11-12-55.zip`) sha256 after all work | `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c` — **unchanged** (matches contract) |
| Source tree modified during this work | **No** — no file in the read-only Community tree has a modification time after 2026-10-01 00:00 (excluding `.DS_Store`); register workbook mtime unchanged (2026-09-21 19:01) |
| In-database `drop database` | **Refused** by the server (two sessions still attached); not forced |
| Private PostgreSQL 18.6 cluster | stopped (`pg_ctl stop -m fast`: "server stopped"); **cluster data directory deleted**; Unix-socket directory deleted; extracted `dump.sql` and `manifest.json` copies deleted; restore logs deleted; the read-only copy of the verifier's statutory seed register deleted |
| Residual processes / listeners | 0 postgres processes; nothing listening on the research port; the one pre-existing unrelated host postgres process was never touched |
| Re-creation | the contract is reproducible in ≈6 s from the unchanged ZIP (extract `dump.sql`, init a private cluster, `psql -f`); any later DELTA research can re-restore without further approval |

Because the whole cluster was deleted, the failed in-DB drop has no residual effect.

## 2. State at this checkpoint
- Units: B00–B02, U01–U29, C01–C02, TXA1, TXA2, TXC, TXS, plus correction packets `U04-R1 … U24-R1`, `U06-R1`, `U07-R1`, `U07-R2`, `U08-R1`, `U10-R1…R3`, `U11-R1`, `U11-R2`, `U12-R1`, `C01-R1`, `B01-R1`, `B02-R1`, `SCOPE-R1`, `TXS-R1` (20 correction requests, all with a terminal disposition on PR #74 except routine re-verification of U29).
- Evidence indexed: 13,648+ claims (U29 adds 410) in the restricted layer; neutral layer separate; every unit passes the pointer/anchor/neutral-leak script; the controller independently reproduced headline findings for each unit before hand-off (spot-check, not independent verification).
- Thai Tax Core lane: all ten required completion outputs assembled and reviewed `ACCEPTED` as a faithful assembly by the verifier; statutory register verified with 4 of 5 conflicts resolved.
- AWT backlog: 704 runtime-only items (78 C1-bound) — nothing inferred.

## 3. Open items (none blocks the critical path)
1. Verifier re-verification of `U29` (routine).
2. Thai statutory unknowns: Sec. 70 rate basis (CONFLICT), 1% e-withholding 2026–27, post-2027 VAT rate, mandatory e-Tax adoption date, representative-office and ownership-keyed rules — `UNKNOWN — STATUTORY SOURCE REQUIRED` / UNVERIFIED.
3. Boss/PMO decisions: register hash mismatch; whether the Thailand-only rule extends to non-localization region-specific modules (Peppol family, SEPA QR, country payment gateways); stray non-source file in the read-only tree (SP-01); canonical denominator validation.
4. Authorized runtime environment (L5/AWT) — not provisioned; all RT items wait on it.
5. L4 independent challenge remains with the verifier lane.
