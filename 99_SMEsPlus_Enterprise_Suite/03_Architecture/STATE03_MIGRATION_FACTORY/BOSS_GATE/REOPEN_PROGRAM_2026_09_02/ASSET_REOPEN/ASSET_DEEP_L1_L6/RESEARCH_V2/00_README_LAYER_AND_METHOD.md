# ASSET DEEP RESEARCH L1–L6 — LAYER, METHOD AND READING ORDER

Session: `SMEPLUS-26-09-04-ASSET-DEEP-L1-L6-001`
Date: 2026-09-04
Branch: `research/asset-deep-l1-l6-2026-09-04-001`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Terminal state: see `01_EXECUTIVE_SUMMARY.md`.

## Clean-room layer of this package

**This whole folder is LAYER 2 — AUDIT QUARANTINE.**

Reason: the governing prompt (§20, §5, §9) mandates function→code→model→field→
database→journal tracing. That is impossible without naming reference-ERP models,
fields, files and line numbers. Those tokens are evidence, not design.

- Layer 2 (this folder, files `01`–`43`, `45`, `46`): Boss / PMO / AI-Audit only.
  Contains reference-ERP model names, field technical names, file paths and line
  ranges. **Must not be transcribed into any Team-B-facing reference package.**
- Layer 1 (file `44_BOSS_FINAL_REVIEW_PACK.md`): clean-room business learning.
  Written with no vendor model/field/file tokens. This is the only file in this
  package cleared to seed downstream SMEsPlus design material.

A mechanical clean-room scan of `44` is recorded in `43_PMO_GOVERNANCE_VERIFICATION.md`.

## Evidence roots used by this session

| ID | Root | Type | Notes |
|----|------|------|-------|
| `EV-CODE` | reference ERP v18 Enterprise source tree, build `20250608` | Primary source code | The version family the target UAT runs |
| `EV-CUST` | project custom addon set, v18 line | Primary source code | Custom/localisation extensions |
| `EV-LEG` | legacy v14 source tree (standard + custom) | Primary source code | Predecessor system |
| `EV-RT` | runtime ORM read-out captured 2026-08-26 against UAT db `idemo18_uat` | Runtime system evidence | `search_read` / `search_count` results |
| `EV-XLS` | Asset Model export captured 2026-08-27 | Runtime export | Method / duration / account triple per model |
| `EV-HND` | Asset Actual Mapping execution handoff, 2026-08-26 | Project record | Controlled model list, population counts |
| `EV-LAW` | Thai Revenue Department official publications | Statutory | See `28_SOURCE_LINK_REGISTER.md` |
| `EV-SIM` | analytic reproduction of the board algorithm | Derived | **Not** a runtime execution — see `17` |

## Method note that governs every numeric claim in this package

`EV-SIM` is a line-by-line Python transcription of the reference ERP's own board
algorithm, run to reproduce the scenarios in `40_TEST_MATRIX.md`. It is classified
**SUPPORTED INTERPRETATION**, never FACT VERIFIED, because it was not executed
inside the reference ERP runtime. Where a scenario is also corroborated by `EV-RT`
or `EV-HND`, that is stated explicitly.

## Reading order for Boss

1. `44_BOSS_FINAL_REVIEW_PACK.md` — the consolidated pack (Layer 1).
2. `01_EXECUTIVE_SUMMARY.md` — status and headline findings.
3. `29_RESEARCH_ERROR_AND_REVISION_LOG.md` — what the previous session got wrong.
4. `37_CONTRADICTION_REGISTER.md` and `41_UNRESOLVED_EVIDENCE_REGISTER.md`.
