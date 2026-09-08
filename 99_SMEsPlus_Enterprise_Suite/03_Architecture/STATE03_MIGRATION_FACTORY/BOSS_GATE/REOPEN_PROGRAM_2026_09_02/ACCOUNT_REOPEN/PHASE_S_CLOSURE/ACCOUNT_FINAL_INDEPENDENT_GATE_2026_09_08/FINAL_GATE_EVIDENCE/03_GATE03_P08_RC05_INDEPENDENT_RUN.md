# GATE 03 — P08 RC-05 INDEPENDENT FOUR-INPUT RUN

Verifier: GPT-5.6 Sol independent verifier
Timestamp: 2026-09-08T20:19:00+0700
Control branch: `audit/gpt56sol-account-phase-s-final-independent-gate-2026-09-08-001`

Owner/surface: P08 @ `ca577be...`. Four frozen inputs were hash-checked before execution.

Independent result: DB-SM 169,143 / 417,700 lines; DB-BK 16 / 563; DB-EV 6 / 15; DB-T2 5 / 14. Computed and stored balance unbalanced counts are `0/0/0/0` at exact, 1e-7, 1e-4, 0.005 for every input; positive extraction controls are non-zero.

Controls: injection 0.01 => `1/1/1/1`; injection 0.001 => `1/1/1/0`; missing input exit 2 fail-closed; missing restore tool exit 2 fail-closed. Pre-run prediction commit `78f5378...` precedes owner result commit `f0cf287...`; final P08 head preserves both. Claims are scoped to **four frozen RC-05 extracts, not a deployment census**. Retired HO namespace, explicit manifest self-exclusion, and four-input install-state propagation are present.

Evidence: `RAW_EVIDENCE/P08_RC05_*`.

**Status: PASS. RC-05 is independently executed and reproducible.**
