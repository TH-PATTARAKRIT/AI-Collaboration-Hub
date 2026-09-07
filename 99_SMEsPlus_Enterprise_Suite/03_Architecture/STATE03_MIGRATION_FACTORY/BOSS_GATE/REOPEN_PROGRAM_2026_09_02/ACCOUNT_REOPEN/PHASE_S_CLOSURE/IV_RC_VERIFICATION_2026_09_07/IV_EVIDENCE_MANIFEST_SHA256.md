# IV EVIDENCE MANIFEST — SHA-256

Session: `SMEPLUS-26-09-07-ACC-PHASE-S-INDEPENDENT-RC-VERIFY-001`
Branch: `audit/account-phase-s-iv-rc-2026-09-07-001` · base `2e2b8dec555454435a462420b6abe5cfde9e7139`
Date: 2026-09-07

## A. INPUTS READ (read-only, at immutable SHA `2e2b8de`)

SHA-256 of blob content as read from the frozen tree.

| SHA-256 | Path |
|---|---|
| `2d0ca3aea51715f576f0f7a29dc05493f6e3922cd6a9d171b93ab892cc17f87e` | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/PHASE_S_CLOSURE/BOSS_DECISION_Q_BOSS_03_AND_INDEPENDENT_VERIFIER_APPOINTMENT_2026_09_07.md` |
| `714fb428ad4fc647aec5dfcb073c9a0e74aaed0a102117f921ad1c3e9ea0f7d6` | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/PHASE_S_CLOSURE/NEXT_PROMPT_CLAUDE_PHASE_S_REMEDIATION_2026_09_07.md` |
| `47b0ccb76314361b1dbce5e3b2cafdf573aa7d29eda1f77933b2d613a9dc2b0e` | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/PHASE_S_CLOSURE/NEXT_PROMPT_CHATGPT_PHASE_S_INDEPENDENT_RC_VERIFICATION_2026_09_07.md` |

## B. OUTPUTS PUBLISHED BY THIS SESSION

| SHA-256 | File |
|---|---|
| `228259882a84b030c62248b3808cb45ea1fd22f40d8874722a8b96bebae2c622` | `00_IV_APPOINTMENT_AND_PRECONDITION.md` |
| `cf68bf1337a68fce8e06dff2faf8aa8a5e4a854f6e9924aad34e25fcf397399b` | `01_11_IV_OUTPUTS_NOT_PRODUCED.md` |
| `9d69c835c930773e6327e3fa696add4683ee56e712f63a4089a64e7f83494ae6` | `IV_CHECKPOINT_REGISTER.md` |
| `c59f615dcbd5e9266e4afbdf65e27c10ed4fc4825b06affb284ea2727b821a6e` | `IV_AUTO_RESUME_STATE.md` |

(`IV_EVIDENCE_MANIFEST_SHA256.md` cannot hash itself and is excluded; its own hash is the commit blob SHA recorded at push.)

## C. EVIDENCE NOT AVAILABLE TO THIS SESSION

| Required input | Declared by | Status |
|---|---|---|
| `04_RC01_RC06_VERIFIER_HANDOFF_MATRIX.md` | Verification prompt §1 | ABSENT — 0 occurrences across all remote branches |
| `03_P08_RC05_REPRODUCIBILITY_PACKAGE.md` (instrument, frozen inputs, per-input SHA-256, predicates, tolerance semantics, controls) | Boss `Q-BOSS-03` §2; remediation prompt §5 | ABSENT — Workstream C not executed |
| `01_P11_CO_F_01_PIN_INSTRUMENT_REPAIR.md` (repaired pin-honouring instrument + pin table) | Remediation prompt §3 | ABSENT — Workstream A not executed |
| `02_P11_CO_F_02_STALE_INBOUND_REPAIR.md` | Remediation prompt §4 | ABSENT — Workstream B not executed |
| `05_REMEDIATION_EVIDENCE_MANIFEST.md` | Remediation prompt §7 | ABSENT |

No RC input was hashed because no RC input was published.

## D. POPULATION AND INSTRUMENT DECLARATION

- **POPULATION:** every ref under `refs/remotes/origin` in a fresh clone of `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub.git`, fetched `+refs/heads/*:refs/remotes/origin/*` on 2026-09-07.
- **PATTERN:** exact literal filename match (`grep -c`) and exact literal token match (`git grep -l -F`). Both published with their commands in `00_...` §2.
- **PATH SET:** whole tree of each remote ref — `git ls-tree -r --name-only <ref>` with no path restriction.
- **UNIT:** file path present in the tree of a remote branch (checks P-2, P-3); file containing token (P-1); commit (P-4).
- **ELIGIBILITY:** no branch excluded. Every remote ref enumerated, including `origin`, `origin/SMEsPlus` and all `claude/*`, `audit/*`, `corr/*`, `research/*`, `control/*`, `design/*`, `prompt/*` refs.
- **TOOL:** `git` (`2.50.1`), `shasum -a 256`, `grep` (BSD), `zsh` on darwin 25.6.0.
