# 00 — README: LAYER, METHOD AND READING ORDER

**Session:** `SMEPLUS-26-09-04-ACC-P03-M2C-REV2-001`
**Process:** P03 — Manufacture-to-Cost
**Branch:** `research/account-p03-manufacture-to-cost-2026-09-04-001`
**Base:** `origin/SMEsPlus` @ `88f52cd`
**Date:** 2026-09-04
**Control level:** `/L99999.99999`
**Approver:** Boss — Sole Final Approver

---

## 1. Layer classification

| Layer | Content | Audience |
|---|---|---|
| **Layer 2 — AUDIT QUARANTINE** | Files `01`–`19` in this directory. They cite reference-ERP source as `file:line — method`. | Boss / PMO / AI-Audit only |
| **Layer 1 — CLEAN ROOM** | File `24_P03_CORE_RECON_HANDOFF_PACK.md` only. Vendor model, field, path and menu names are scrubbed. | May travel to Core Accounting Reconciliation and, on Boss release, to Team B |

Every Layer 2 file carries the banner **LAYER 2 — AUDIT QUARANTINE** at its head.
Citations in Layer 2 files must not be transcribed into any Layer 1 or reference package.
Governing control: Clean Room Learning Directive v2.0 (Policy A), Council 08 invariant.

## 2. What this session is, and is not

**It is** a forensic reading of how one economic manufacturing cost travels from a
business event to WIP, to finished goods and to COGS in the reference product, and a
statement of what SMEsPlus must therefore own, forbid or decide.

**It is not** an implementation, a design approval, or a re-opening of the Asset track.
No production code is written. No branch is merged. No gate is declared passed.

## 3. Prior evidence this session is bound by, and must not silently resolve

| Lineage | Branch | Binding effect on P03 |
|---|---|---|
| Asset Deep L1–L6 | `origin/research/asset-deep-l1-l6-2026-09-04-001` | Two day conventions; Operation–Equipment gap |
| **Asset DR Continuation** | `origin/research/asset-deep-continuation-2026-09-04-001` | **`BLK-07` and `BLK-08` remain open. The AAS+ veto on starting costing implementation stands. `12_MANUFACTURING_COST_CLASSIFICATION_MATRIX.md` is the adopted cost taxonomy and P03 does not re-derive it.** |
| COGS Deep Research / Targeted Resolution | `origin/audit/cogs-deep-research-2026-09-02-001`, `origin/research/cogs-targeted-resolution-2026-09-03-001` | COGS remains terminal HOLD. `JT-01/04/05` NOT DECIDABLE |
| Inventory R4 L1–L12 + MTI | `origin/research/...`, `origin/ruling/inventory-mti-d0{1,2,3}-...` | Inventory valuation and multi-tenant invariants are owned there, not here |
| Account Wave A (Core / CORR1 / MCC / AASR / Final Closure / GB-08) | `origin/research/account-wave-a-*` | Core ledger findings — notably the system-derived accounting date — are inherited, not re-proved |

**P03 adds no closure to any Asset, COGS or Inventory blocker.** Where a P03 finding
touches one, it is recorded as a dependency in `14_P03_DEPENDENCY_REGISTER.md` and the
prior blocker's status is quoted unchanged.

## 4. Method

1. Governance read first: `PROJECT_CONSTITUTION.md` v1.4, the Understand-Transfer-Preserve
   addendum, `SYSTEM_RESEARCH_MASTER_INDEX.md`, `END_TO_END_BUSINESS_PROCESS_MATRIX.md`.
2. Primary source read second — **not** the working tree. Per
   `smeplus-primary-source-evidence-locations`, primary evidence lives outside the clone.
   The declared source root for this session is in `17_P03_SOURCE_LINK_REGISTER.md` §1.
3. Semantic trace applied in the mandated order:
   `Module → Model → Field → Function → Event → Runtime → Database → Operational Truth →
   Cost Event → Accounting Event → Journal → WIP/FG → COGS → Report/Close`.
   FK-first interpretation was not used.
4. Canonical principle enforced throughout:
   **ONE BUSINESS FACT → ONE EVENT OWNER → ONE ACCOUNTING EFFECT**, and its P03 form
   **ONE ECONOMIC COST → ONE COST INJECTION PATH INTO WIP.**
5. Every negative claim carries its search scope, per
   `smeplus-deep-research-negative-claim-standard`. `NO EVIDENCE FOUND` is never written
   as `DOES NOT EXIST`.
6. Every enumeration declares POPULATION + PATTERN + PATH SET + UNIT, per
   `smeplus-denominator-completeness-rule`.

## 5. Classification vocabulary

Every assertion in this package carries exactly one:

`FACT VERIFIED` · `SUPPORTED INTERPRETATION` · `DESIGN CANDIDATE` ·
`BOSS CONTROLLED DECISION` · `CONTRADICTED` · `UNRESOLVED`

## 6. Reading order

| # | File | Read it for |
|---|---|---|
| 01 | `P03_PROCESS_MAP.md` | The chain, and where cost enters it |
| 02 | `P03_COST_COMPONENT_REGISTER.md` | Every cost element and its injection path |
| 03 | `P03_WIP_FG_TRACE.md` | The WIP and FG account behaviour end to end |
| 04 | `P03_MACHINE_COST_OWNERSHIP_MATRIX.md` | Who owns machine cost, and the Asset dependency |
| **05** | **`P03_DOUBLE_COUNTING_ATTACK.md`** | **The core result of this session** |
| 06–08 | Event registers and the GL matrix | Event ownership and accounting effect |
| 09–11 | MO cost trace, variance, scrap/rework | Execution-path forensics |
| 12 | `P03_CROSS_PROCESS_OWNERSHIP.md` | Boundaries with P01, P02, Inventory, Asset |
| 13–18 | Control registers | Dependencies, contradictions, evidence, revisions |
| 19 | `P03_AAS03_CHALLENGE.md`, `P03_AAS_PLUS.md`, `P03_PMO.md` | Adversarial review and dissent |
| 20 | `P03_CORE_RECON_HANDOFF_PACK.md` | **Layer 1.** What Core Accounting Reconciliation receives |

## 7. Terminal state of this session

`READY FOR CORE ACCOUNTING RECONCILIATION` — with the qualifications recorded in
`21_P03_PMO.md` §4. This is a readiness statement about a **handoff**, not an approval of
any design and not a gate closure.
