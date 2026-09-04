# P04 — ACQUIRE-TO-RETIRE — LAYER, METHOD AND READING ORDER

Session: `SMEPLUS-26-09-04-ACC-P04-A2R-REV2-001`
Date: 2026-09-04
Process: P04 — Acquire-to-Retire
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Canonical branch: `SMEsPlus` (not merged, by design)
Working branch: `research/account-p04-acquire-to-retire-2026-09-04-001`
Mode: UPDATE / CONTINUATION — prior Asset research is imported, not reset.
Terminal status: see `19_P04_CORE_RECON_HANDOFF_PACK.md`.

## 1. Clean-room layer of this package

**This whole folder is LAYER 2 — AUDIT QUARANTINE.**

The governing prompt mandates the semantic trace
`Module → Model → Field → Function → Event → Runtime → DB → Operational Truth
→ Accounting Event → Journal → Subledger → Report/Close`.
That trace cannot be carried out without naming reference-ERP models, fields,
files and line numbers. Those tokens are **evidence, not design**.

| Layer | Files | Audience | Rule |
|-------|-------|----------|------|
| Layer 2 — audit quarantine | `00`–`18` | Boss / PMO / AI-Audit only | Contains reference-ERP model names, technical field names, file paths and line ranges. **Must not be transcribed into any Team-B-facing reference package.** |
| Layer 1 — clean-room business learning | `19_P04_CORE_RECON_HANDOFF_PACK.md` | Cleared to seed downstream SMEsPlus design material | Written with no vendor model / field / file / menu tokens. |

A mechanical clean-room token scan of file `19` is recorded in `17_P04_PMO.md`.
Scrub list applied: `stock.*`, `product.*`, `ir.*`, `quant`, `orderpoint`,
`picking(-type)`, `_action_*`, `sudo`, `.py`, plus asset-domain technical names.

No implementation. No merge. No production change. This session produces
research evidence only.

## 2. Evidence roots used by this session

| ID | Root | Type | Notes |
|----|------|------|-------|
| `EV-CODE` | Reference ERP v18 Enterprise source tree, build `20250608` | Primary source code | 797 modules. The version family the target UAT runs. |
| `EV-CUST` | Project custom addon set, v18 line | Primary source code | Custom / localisation extensions. |
| `EV-LEG` | Legacy v14 source tree (standard + custom) | Primary source code | Predecessor system. |
| `EV-RT` | Runtime ORM read-out captured 2026-08-26 against UAT db `idemo18_uat` | Runtime system evidence | `search_read` / `search_count` results. **Field set and domain are bounded — see §4.** |
| `EV-HND` | Asset Actual Mapping execution handoff, 2026-08-26 | Project record | Controlled model list, population counts, traceability rules. |
| `EV-PRIOR` | Three completed Asset research packages (see `08_P04_PRIOR_EVIDENCE_RECONCILIATION.md`) | Prior audited evidence | Imported as PRIOR EVIDENCE / PRIOR HYPOTHESIS / BOSS CONTROLLED DECISION / AUDIT LINEAGE. |
| `EV-LAW` | Thai statutory and standard-setter publications | Statutory | See `13_P04_SOURCE_LINK_REGISTER.md`. |

## 3. Classification vocabulary

Every material statement in this package carries exactly one of:

- **FACT VERIFIED** — read directly from primary source, runtime evidence, or an
  authoritative statutory text, and reproducible by the reader from the citation.
- **SUPPORTED INTERPRETATION** — a reading that the evidence supports but does not
  compel; an alternative reading exists.
- **DESIGN CANDIDATE** — a proposed SMEsPlus behaviour. Not evidence. Not approved.
- **BOSS CONTROLLED DECISION** — a decision reserved to, or already taken by, the Boss.
- **CONTRADICTED** — an earlier claim this session disproved. The correction is stated.
- **UNRESOLVED** — the evidence needed to decide does not exist in reach of this session.

## 4. Negative-claim standard (mandatory)

`NO EVIDENCE FOUND` is **not** `FUNCTION DOES NOT EXIST`.

Every negative statement in this package is written as
*"not found under `<declared path set>` using `<declared pattern>`"*
and never as *"does not exist"*.

Every enumeration in this package declares four things before it counts anything:

| Element | Meaning |
|---------|---------|
| POPULATION | What is being counted |
| PATTERN | The exact match expression used |
| PATH SET | The exact directories searched |
| UNIT | What one row of the count represents |

None of the four may be author-chosen after the fact. Where a prior capture's own
query was bounded (for example a runtime read-out whose identifier list was
hand-picked), that bound is stated at the point of use and the result is **not**
promoted to a population statement.

## 5. Reading order for Boss

1. `19_P04_CORE_RECON_HANDOFF_PACK.md` — the consolidated Layer-1 pack and terminal status.
2. `10_P04_BLOCKER_REGISTER.md` — what is stopping progress.
3. `09_P04_BOSS_DECISION_REGISTER.md` — what only the Boss can decide, and what is already decided.
4. `01_P04_UPSTREAM_CAPITALIZATION_TRACE.md` — the headline new finding of this session.
5. `12_P04_CONTRADICTION_REGISTER.md` and `08_P04_PRIOR_EVIDENCE_RECONCILIATION.md`.
6. `16_P04_AAS_PLUS.md` and `17_P04_PMO.md` — independent challenge and governance.

## 6. File index

| # | File | Content |
|---|------|---------|
| 00 | `00_README_LAYER_AND_METHOD.md` | This file |
| 01 | `01_P04_UPSTREAM_CAPITALIZATION_TRACE.md` | Every path by which an asset comes into existence |
| 02 | `02_P04_ASSET_LIFECYCLE_MAP.md` | Acquire-to-retire lifecycle, end to end |
| 03 | `03_P04_ASSET_EVENT_REGISTER.md` | Every lifecycle event, its trigger and its owner |
| 04 | `04_P04_ASSET_TO_GL_MATRIX.md` | Event → journal entry → account |
| 05 | `05_P04_ASSET_EQUIPMENT_RELATIONSHIP.md` | Asset ↔ equipment ↔ work centre ↔ operation |
| 06 | `06_P04_DEPRECIATION_COST_HANDOFF.md` | Depreciation → cost absorption handoff |
| 07 | `07_P04_DISPOSAL_DERECOGNITION_MATRIX.md` | Transfer, sale, disposal, scrap, derecognition |
| 08 | `08_P04_PRIOR_EVIDENCE_RECONCILIATION.md` | Import of the three prior Asset packages |
| 09 | `09_P04_BOSS_DECISION_REGISTER.md` | Boss-controlled decisions, standing and open |
| 10 | `10_P04_BLOCKER_REGISTER.md` | Blockers with close conditions |
| 11 | `11_P04_CROSS_PROCESS_OWNERSHIP.md` | One fact → one owner → one accounting effect |
| 12 | `12_P04_CONTRADICTION_REGISTER.md` | Contradictions, open and closed |
| 13 | `13_P04_SOURCE_LINK_REGISTER.md` | Every source cited |
| 14 | `14_P04_EVIDENCE_MANIFEST.md` | Manifest and hashes |
| 15 | `15_P04_AAS03_CHALLENGE.md` | Four-expert challenge at every material level |
| 16 | `16_P04_AAS_PLUS.md` | Independent adversarial review, disagreement preserved |
| 17 | `17_P04_PMO.md` | Governance verification |
| 18 | `18_P04_REVISION_LOG.md` | Revisions and corrections made during this session |
| 19 | `19_P04_CORE_RECON_HANDOFF_PACK.md` | Layer-1 handoff to Core Accounting Reconciliation |

The required output filenames from the governing prompt are preserved verbatim;
the numeric prefix is ordering only.
