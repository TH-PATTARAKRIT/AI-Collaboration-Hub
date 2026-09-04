# P11 — UNIFIED SOURCE LINK REGISTER

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Process `P11 Central Core Accounting Reconciliation`
Repository `TH-PATTARAKRIT/AI-Collaboration-Hub` · Canonical branch `SMEsPlus`
Working branch `research/account-core-reconciliation-2026-09-04-001`
Date `2026-09-04` · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver. No AI may declare Final Approval.**

---

## 1. Declared research universe — before any count

Per `SMEPLUS-DR-EXIT-8C-001` `EC-01` and the denominator rule this programme has repeatedly failed
and repeatedly re-learned, P11 declares its **population, pattern, path set and unit before counting
anything**. None of the four is author-chosen from a convenient list.

| Dimension | Declaration |
|---|---|
| **POPULATION** | Every git ref reachable from `origin` in `TH-PATTARAKRIT/AI-Collaboration-Hub`, plus every sibling session clone on the execution volume matching `ACCOUNT_P??_*_2026_09_04_EXECUTION` |
| **PATTERN** | (a) `git ls-remote --heads origin` — every branch, no name filter applied before the count; (b) `git ls-tree -r` over **every** ref for path segments matching `^P(0[1-9]\|10)_`; (c) `git ls-files --others --exclude-standard` in each sibling clone |
| **PATH SET** | `refs/remotes/origin/*` — all 134 refs, not a chosen subset; and the parent volume directory, not a chosen subdirectory |
| **UNIT** | One git ref; one tracked file path; one untracked file path |

**What P11 does NOT declare, and the omission is deliberate and disclosed.** P11 does **not** declare
a reference-ERP source root. It never reads reference source. Every behavioural statement in this
package is **inherited** from a peer package and carries that package's own root boundary, which under
`MCU-21` is **undeclared in all of them**. See `P11_FINAL_BLOCKER_REGISTER.md` `P11-B-01`.

---

## 2. Evidence classes used in this package

Never merged, always labelled:

| Class | Meaning | Citable as evidence? |
|---|---|---|
| `PEER-PUBLISHED` | An artefact at a named branch and commit SHA on `origin` | **Yes** |
| `BOSS-APPROVED` | A Boss decision artefact on the canonical `SMEsPlus` branch | **Yes, and it governs** |
| `PEER-WIP` | A file existing only as an uncommitted working-tree file in a sibling clone | **No.** Recorded for programme-state purposes only |
| `P11-DERIVED` | A reconciliation conclusion produced by this session from two or more of the above | Yes, as a conclusion — never as a primary fact |
| `UNKNOWN — EVIDENCE REQUIRED` | Not established | No |

---

## 3. Boss-approved controls that govern this reconciliation

| id | Artefact | Branch | Status |
|---|---|---|---|
| `BC-01` | `.../ACCOUNT_INVENTORY_JOINT/02_BOSS_APPROVAL_JOINT_22_SCENARIO_CROSS_PROOF_BASELINE_2026_09_02.md` | `SMEsPlus` @ `88f52cd` | `BOSS APPROVED / EFFECTIVE` |
| `BC-02` | `.../ACCOUNT_INVENTORY_JOINT/03_BOSS_APPROVAL_INVENTORY_TO_ACCOUNTING_MINIMUM_HANDOFF_DATA_CONTRACT_2026_09_02.md` | `SMEsPlus` @ `88f52cd` | `BOSS APPROVED / EFFECTIVE` |
| `BC-03` | `00_Project_Governance/SMEPLUS_VERY_DEEP_RESEARCH_8_CRITERIA_UNIVERSAL_EXIT_CONSTITUTION.md` | `SMEsPlus` @ `88f52cd` | `BOSS APPROVED / PROJECT-WIDE MANDATORY` |
| `BC-04` | `.../ACCOUNT_FULL_DEEP_RESEARCH/GB08_BOSS_RULING_FX_RATE_OWNERSHIP_AND_MISSING_RATE_POLICY_2026_09_04.md` | `SMEsPlus` @ `88f52cd` | Boss ruling, FX rate ownership |
| `BC-05` | `.../INVENTORY_REOPEN/.../24,26,28_BOSS_RULING_..._MTI_D01/D02/D03` | `design/inventory-mti-ruling-conformance-2026-09-05-001` @ `bd096ff` | Boss rulings D-01, D-02, D-03 |

`BC-01` and `BC-02` are the two controls P11 exists to generalise. Both are written **Inventory →
Accounting only**. See `P11-F-02`.

---

## 4. Peer-published evidence actually consumed

All SHAs verified this session by `git rev-parse` against `origin`.

| id | Package | Branch | HEAD SHA | Terminal state as that package declares it |
|---|---|---|---|---|
| `SL-01` | Account Wave A — Method Convergence Closure + Final Closure + GB-08 | `research/account-wave-a-mcc-2026-09-04-001` | `78840777e6b56aa12704d220b0728d0db48377b6` | **`HOLD WITH EXACT REMAINING BLOCKERS`** · `NOT CONVERGED` |
| `SL-02` | Account Wave A — AAS+ Redesign (parallel, provisional) | `research/account-wave-a-aasr-2026-09-04-001` | `7c0a3cef4cb67c528ba9b3fcc32e431ae2a64f98` | **`PROVISIONAL / NON-CANONICAL`** · `AASR-VETO-01` upheld |
| `SL-03` | Account Wave A — Method Convergence | `research/account-wave-a-mc-2026-09-04-001` | `b6cc260b570818f64719b7470a72d573e2ac3e7b` | `NOT CONVERGED` |
| `SL-04` | Account Wave A — Gap Closure | `research/account-wave-a-gapclose-2026-09-04-001` | `56288c47b83804c609a4b1be1fb29f9d2ce60a1f` | Gate report; superseded by `SL-01` |
| `SL-05` | Account Wave A — CORR1 | `research/account-wave-a-corr1-2026-09-04-001` | `93ad4d5eac00aee97c42008cc93ea868671f4150` | Corrections accepted into the core package |
| `SL-06` | Account Wave A — Core Ledger L1–L12 | `research/account-wave-a-core-2026-09-04-001` | `f8bc069f520f91eff23e269e82d94f9fd5adb813` | Superseded by `SL-05`/`SL-01` corrections |
| `SL-07` | Inventory Deep Research R4 L1–L12 | `audit/inventory-deep-research-r4-l12-2026-09-04-001` | `fc0b16888ddaea1648abea4ee7d78fe3132861d4` | `HOLD — ACCOUNTING COGS GAP EVIDENCE REQUIRED` |
| `SL-08` | Inventory R4 AAS+/PMO Review | `review/inventory-r4-aas-pmo-review-2026-09-04-001` | `e218e5b550a2a8f839f295876f0a3ff1ce3e69d4` | `HOLD` on reliance |
| `SL-09` | Inventory Multi-Tenant Invariant Set | `design/inventory-multitenant-invariant-set-2026-09-04-001` | `dcb92278769d6a8239a5183ec4890e230a7caf68` | 50 invariants; element 10 specified-not-built |
| `SL-10` | Inventory MTI Ruling Consolidation | `governance/inventory-mti-ruling-consolidation-2026-09-04-001` | `a57bd555ed3dbb3e351032be7a5025d17bedb7e3` | `RC-V-01` veto; `AAS-V-02` not discharged |
| `SL-11` | Inventory MTI Ruling Conformance | `design/inventory-mti-ruling-conformance-2026-09-05-001` | `bd096ffaef4cb2da9ef8db43c52db30dce2a3f9e` | `CF-F-04`/`CF-F-05` structural gaps |
| `SL-12` | Asset Deep L1–L6 | `research/asset-deep-l1-l6-2026-09-04-001` | `78067d23e0b2bc09aaa28b75fe768ab73de96ce8` | Terminal state B |
| `SL-13` | Asset DR Continuation | `research/asset-deep-continuation-2026-09-04-001` | `54db9e1a9457f962198e51b9c9abae3cba7c4b20` | 4 blockers closed · 4 open · **AAS+ veto on implementation start** |
| `SL-14` | Asset Function Deep Research | `audit/asset-function-deep-research-2026-09-03-001` | `57cdb99159fcf0d02f76e3f42d7a7decd8d383e1` | Prior lineage |
| `SL-15` | COGS Deep Research `ERPPLUS-142` | `audit/cogs-deep-research-2026-09-02-001` | `a959327938cc1168c93e1e4a89bd1dcf846871c5` | `HOLD / EVIDENCE REQUIRED` |
| `SL-16` | COGS Fact Verification | `research/cogs-fact-verification-2026-09-03-001` | `178cd06f7e9923bb3f876e17664f4833e534833c` | `PARTIAL FACT BASELINE` |
| `SL-17` | COGS Targeted Resolution | `research/cogs-targeted-resolution-2026-09-03-001` | `8a90f60b629eea2c1d34b39eb08123f0c16acd97` | `PARTIAL RESOLUTION` · `JT-01/04/05` `NOT DECIDABLE` |
| `SL-18` | COGS Joint Closure | `audit/cogs-joint-closure-2026-09-03-001` | `13219268caa67a8e9bd32a062a346edc958e78ab` | **Governance container only — 4 files, no closure deliverable** |
| `SL-19` | Account Batch A Research Routing | `audit/account-batch-a-research-routing-2026-09-02-001` | `2b54417cec8b4f8dbccac64a5228116fa484d5af` | All Account gates open/blocked |
| `SL-20` | Account Menu Process Deep Study | `audit/account-menu-process-deep-study-2026-09-02-001` | `5183e9f6ef4272e68c65d831580886e341118d53` | Prior lineage |
| `SL-21` | Canonical baseline | `SMEsPlus` | `88f52cd7ba6dc40b8951c4bfc4e0016af7cbb7ad` | Canonical |

**Not one of the twenty-one carries a terminal state stronger than `HOLD`, `PARTIAL` or `PROVISIONAL`.**
There is no `PASS` anywhere in P11's inherited evidence base. That is the single most important fact
about this reconciliation and it is stated first, not last.

---

## 5. P01–P10 — the register P11 was commissioned to consume

| Process | Expected branch | On `origin`? | Commits | Published artefacts | Class |
|---|---|---|---|---|---|
| `P01` Procure-to-Pay | `research/account-p01-procure-to-pay-2026-09-04-001` | **No** | 0 | **0** | `PEER-WIP` |
| `P02` Order-to-Cash | `research/account-p02-order-to-cash-2026-09-04-001` | **No** | 0 | **0** | `PEER-WIP` |
| `P03` Manufacture-to-Cost | `research/account-p03-manufacture-to-cost-2026-09-04-001` | **No** | 0 | **0** | `PEER-WIP` |
| `P04` Acquire-to-Retire | `research/account-p04-acquire-to-retire-2026-09-04-001` | **No** | 0 | **0** | `PEER-WIP` |
| `P05` Expense-to-Pay | `research/account-p05-expense-to-pay-2026-09-04-001` | **No** | 0 | **0** | none observed |
| `P06` Bank-to-Reconcile | `research/account-p06-bank-to-reconcile-2026-09-04-001` | **No** | 0 | **0** | `PEER-WIP` |
| `P07` Tax-to-Compliance | `research/account-p07-th-tax-compliance-2026-09-04-001` | **No** | 0 | **0** | none observed |
| `P08` Record-to-Report | `research/account-p08-record-to-report-2026-09-04-001` | **No** | 0 | **0** | `PEER-WIP` |
| `P09` Plan-to-Analyze | `research/account-p09-plan-to-analyze-2026-09-04-001` | **No** | 0 | **0** | none observed |
| `P10` Time-Based Recognition | `research/account-p10-time-based-recognition-2026-09-04-001` | **No** | 0 | **0** | none observed |

> ## `PEER DEPENDENCY OPEN × 10`
> **0 of 10 peer processes have published any artefact at any commit SHA.**

Reproduction: `LAYER2_P11_EVIDENCE/p11_scripts/peer_intake.sh`, output at
`LAYER2_P11_EVIDENCE/peer_intake_output.txt`. Snapshot of unpublished work-in-progress:
`p11_scripts/peer_wip_snapshot.sh`, output at `peer_wip_snapshot_output.txt`,
`SNAPSHOT_UTC=2026-09-04T22:41:38+0700`.

**The snapshot is time-bounded and says so.** The peer sessions were observed to be *actively
writing* during this session — `P01`'s working tree changed between two runs of the intake script
minutes apart. Any count of peer work-in-progress is a reading at an instant, not a stable
population, and is reported as such rather than as a finding about how much work exists.

---

## 6. Why unpublished peer work is not consumed

`SMEPLUS_CANONICAL_EVIDENCE_ACQUISITION_FLOW_STANDARD` and the standing programme rule require every
finding to be reported at `Repository / Branch / Commit SHA / Direct GitHub Link`. An uncommitted
working-tree file has none of the four. It cannot be verified by a reviewer, cannot be re-read at a
fixed state, and can change or vanish between two reads — as one of them did during this session.

**P11 therefore reads no peer work-in-progress file as evidence and reconciles none of it.** Their
existence is recorded because it changes the correct classification of the peer dependency from *"not
started"* to *"in flight, unpublished"* — and those two states have different remedies. It is not
recorded as a finding about their content.
