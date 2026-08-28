# SYSTEM_RESEARCH_MASTER_INDEX — Team A

| Field | Value |
|---|---|
| Last update | 2026-08-28 — session SMEPLUS-26-08-28-MIG-A-EXPERT-DR-001 |
| STATE / STEP | STATE03 — Architecture / STEP: TBD — BASELINE REQUIRED |
| Research position | A0 ✅ · A1 ✅ (metadata-level inventory closed) · A2 seeded · A3 proposed · A4+ not started |

## Where is everything?

| Question | Answer |
|---|---|
| What sources exist? | `01_SOURCE_REGISTRY/A1_SOURCE_LANDSCAPE.md` §2 (S-01…S-10) |
| Governance verification? | `01_SOURCE_REGISTRY/A0_GOVERNANCE_VERIFICATION.md` |
| Full tree statistics? | `01_SOURCE_REGISTRY/SOURCE_TREE_INVENTORY.md` |
| All modules? | `01_SOURCE_REGISTRY/MODULE_MASTER_REGISTER.md` + `MODULE_MASTER_REGISTER_FULL.csv` (1,504 rows) |
| Hashes / chain of custody? | `01_SOURCE_REGISTRY/SOURCE_MANIFEST.md` + `.sha256` |
| Database evidence? | `01_SOURCE_REGISTRY/DATABASE_DUMP_REGISTER.md` |
| Baseline reconciliation? | `01_SOURCE_REGISTRY/SOURCE_BASELINE_RECONCILIATION.md` |
| What is quarantined? | `05_QUARANTINE/CLEAN_ROOM_QUARANTINE_REGISTER.md` (12 CLASS-D + E/F controls) |
| What is unknown? | `09_OPEN_QUESTIONS/UNKNOWN_AND_EVIDENCE_GAP_REGISTER.md` (Q-01…G-11) |
| Session log? | `10_SESSION_ARCHIVE/SESSION_SMEPLUS-26-08-28-MIG-A-EXPERT-DR-001_LOG.md` |
| Prior Team A evidence? | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/06 MIGRATION FACTORY/TEAM A_SOURCE_EXTRACTION_OBSERVATION/` (referenced, preserved) |
| Approved scope baseline? | `ACCOUNT/01 ACCOUNT/STEP040303_FINAL_SCOPE/` (134 modules) + STEP040304R4 closeout (591 models) |

## Domain research status (17 working domains — research index, NOT product scope)

| Domain | Status | Evidence pack |
|---|---|---|
| D-01 Accounting core | NOT STARTED (proposed first) | — |
| D-02 AR/AP/Payments | NOT STARTED (proposed #3) | — |
| D-03 Tax & Thai statutory | NOT STARTED (proposed #2) | — |
| D-04…D-17 | NOT STARTED | — |

Domain list and ordering rationale: `01_SOURCE_REGISTRY/A1_SOURCE_LANDSCAPE.md` §4–§5.

## Verified / Unknown / Quarantined / Ready

- **Verified this session:** module counts & licenses (1,504), Odoo 19.0 Enterprise series,
  disjoint-partition structure, dump identity & creator (pg 18.4), archive↔extraction integrity,
  baseline lineage 1,436 → 1,502 → 1,504.
- **Unknown:** 11 registered items (Q-01…G-11) — zero unregistered unknowns claimed.
- **Quarantined:** 12 CLASS-D modules + Class E/F observation sets Q-E01…Q-E04.
- **Ready for ChatGPT review:** A0/A1 registry pack (this directory) — as an *inventory* evidence
  pack; first *domain* evidence pack will follow D-01 research.
