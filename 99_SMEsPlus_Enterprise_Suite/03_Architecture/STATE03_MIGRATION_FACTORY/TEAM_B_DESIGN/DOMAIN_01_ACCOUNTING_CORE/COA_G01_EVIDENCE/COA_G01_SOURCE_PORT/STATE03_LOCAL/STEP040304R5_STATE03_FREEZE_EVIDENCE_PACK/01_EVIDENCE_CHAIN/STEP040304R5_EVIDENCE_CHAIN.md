# STATE03 FREEZE EVIDENCE PACK — PART 1: EVIDENCE CHAIN

Prompt: SMEPLUS-26-08-23-STEP040304R5 | Date: 2026-08-23
Nature: **packaging only.** No new research, no module moved, no restore, no scope change,
no new architecture decision. Every statement traces to a prior step's artefact on disk.

## PROJECT IDENTITY
SMEsPlus is a new **100% clean-room multi-tenant SaaS ERP**, backend in **Node.js**.
Odoo / Salesforce / SAP B1 are reference and benchmark only. Odoo source and the database
dump are evidence instruments used to prove business behaviour, data structure, functional
scope, dependency boundaries, Thai localization requirements, and architecture risk.
No code copied, cloned, migrated or reused. Proprietary/OEEL/OPL source body never read.

## THE CHAIN — TEN STEPS, TEN ARTEFACT PACKS ON DISK
| Step | Produced | Key result |
|---|---|---|
| STEP040301 | Source index & module manifest | 1,502 modules indexed; 3 archives sealed and hashed |
| STEP040302 | Thailand-core filter | Boundary defect found: path excluded most Thai IP |
| STEP040302R1 | Accounting non-TH quarantine | 267 modules quarantined, 0 loss |
| STEP040302R2A | Non-TH localization quarantine | 315 modules quarantined, 0 loss |
| STEP040303 | Final scope rebuild | 134-module scope; 5 deps found in quarantine |
| STEP040303R1 | Boss review & approval | Scope approved; rulings closed |
| STEP040304 | Thailand deep research | FE1–FE8; AF1–AF8 |
| STEP040304R1 | Website/eCommerce V2 hold | 127 held; 6 backend deps protected |
| STEP040304R2 | STATE03 reconciliation | Findings restated as S1–S6 under clean-room identity |
| STEP040304R3A/B/C | Database evidence, mapping, restore | Provenance closed; GAP-1 closed 58/69; route (c) struck |
| STEP040304R4 | Deep research closeout | D5 closed; S7–S11 added |

## CUSTODY AND INTEGRITY — VERIFIED AT THIS STEP
Sealed source archives, SHA-256 re-verified today, unchanged since STEP040301:
| Archive | SHA-256 | Status |
|---|---|---|
| 01_ACCOUNT.zip | 3a40f249…7c1b9ba1 | OK |
| addons_extra.zip | f66767af…037d0f52 | OK |
| 02_OTHER.zip | f263c81e…a24d1d5b | OK |

Database evidence of record — single dump, three byte-identical copies:
`d67fff6dbd3a957a5089e3bd7f982b1f8a98b954e8be2e40e6c227a70339d8c0`

Module universe, re-counted today:
| Location | Modules |
|---|---:|
| 03_LEARNING (active) | 729 |
| addons_extra (Boss Extra) | 69 |
| Quarantine R1 (accounting non-TH) | 262 |
| Quarantine R2A (non-TH localization) | 315 |
| V2 hold (website/eCommerce/theme) | 127 |
| **TOTAL** | **1,502** — exact match to STEP040301 |

Nothing was ever deleted at any point in STEP0403. Every quarantine and hold is reversible
by script, and three independent recovery paths exist (quarantine folders, 04_BACKUP with
1,433 modules, and the sealed archives).

## RESEARCH COVERAGE
| | Modules |
|---|---:|
| Approved research scope | 134 |
| Source-readable (clean-room) | 115 |
| Permanently black-box | 19 |
| Researched, yielded models | 110 |
| Data/asset-only, no models (correctly none) | 4 |
Extracted: 1,215 class declarations, 591 distinct models.

## DATABASE EVIDENCE
Pre-existing V2.0 evidence set, gate-closed G01–G14 all PASS:
1,395 tables · 13,940 columns · 6,682 constraints · 5,141 FK edges · 1,714 indexes ·
27,682 field-level mappings · 6,260 UI records · 473 security records · 4,377 business rules.
Extended at STEP040304R3B with Boss Extra source-to-dump mapping: 222 model declarations
across 58 modules (11 black-box permanently unmappable from source).
