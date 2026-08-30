# COA-G01 — Base Kernel Candidate Input

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Supply source-baseline input for the future COA-G02 Base Kernel Discovery gate | Claude (session SMEPLUS-26-08-30-COA-G01R-001) | GitHub `SMEsPlus` branch | 2026-08-30 22:27 +0700 | ChatGPT Independent Review (pending); Boss (pending) | INPUT ONLY — NOT A DECISION | Feeds COA-G02; does not select or freeze a Base Kernel |

**This artifact does not select a Base Kernel.** COA-G02 ("Base COA Kernel Discovery") is a separate, not-yet-authorized Gate. This document exists only to hand COA-G02 a clean, non-contradictory statement of what is already known, per the Boss instruction that `~32` remains a working expectation and the exact count remains `TBD / EVIDENCE REQUIRED`.

## What is already established (must not be re-derived differently by COA-G02)

| Fact | Status |
|---|---|
| Working expectation of approximately 32 baseline accounts | WORKING EXPECTATION / CANDIDATE RANGE ONLY — not a target mandate |
| Exact Base Kernel count | TBD / EVIDENCE REQUIRED |
| Exact final Standard Thai COA count | TBD / EVIDENCE REQUIRED |
| `389 source rows != 389 target accounts` | BOSS RULING |
| Do not freeze exactly 32 accounts arbitrarily | EXPLICIT PROHIBITION (carried forward from `AN`/`AP`) |
| Do not freeze 389 accounts as the target | EXPLICIT PROHIBITION (carried forward from `AN`/`AP`) |
| Prefer Dimensions over GL-account proliferation where accounting treatment is equivalent | BOSS RULING (session prompt §7) |

## Candidate input surfaces available to COA-G02 (not evaluated or ranked by this session)

1. The 19-type / 15-type / 14-type Account Type reconciliation in `DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md` — a starting taxonomy skeleton, not a row-level kernel.
2. The Track A / Track B methodology already defined in `DOMAIN_01_COA_BASE_KERNEL_AND_AI_CONSOLIDATION_STANDARD.md` for how source rows should be consolidated by business meaning (this document governs *method*, not the resulting count).
3. The 389-row Odoo18 workbook inventory (class D evidence, `COA_G01_SOURCE_BASELINE_REGISTER.md`) as the largest available source-row population to consolidate from.
4. The 144-row `l10n_th` template as a second, smaller source-row population.
5. Local finding S5 (Tenant → Company → Tax Branch) as a constraint on how many *organizational* dimensions exist alongside the *account* dimension — relevant to avoiding GL-account proliferation per the Dimensions-preference ruling above.

## Explicit non-actions of this artifact

- Does not propose a number.
- Does not rank or shortlist candidate account rows.
- Does not consolidate the 389 rows or the 144 rows into anything.
- Does not authorize COA-G02 to begin. COA-G01 remains the only authorized execution Gate at the time of this session.
