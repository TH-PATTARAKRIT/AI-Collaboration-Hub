# 25 — ACCOUNT_WAVE_A_CHECKPOINT LINEAGE

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

Checkpoints were recorded after every Level and execution continued automatically, as instructed.
**No checkpoint is a Boss approval.** Execution did not stop for routine confirmation at any point.

| Level | Deliverable | Checkpoint | Contradictions raised | Unknowns raised | Continued |
|---|---|---|---|---|---|
| Bootstrap | `EV-023` | recorded in `E00` | — | `GAP-B01` | yes |
| L1 Domain understanding | file 01 | §8 | `CONTRA-03` | `GAP-A04`, `GAP-B01` | yes |
| L2 UI / field / configuration forensic | file 03 | §end | `CONTRA-01` | `GAP-A04` | yes |
| L3 Function forensic | file 04 | §end | `CONTRA-03`, `CONTRA-04` | `GAP-C01`–`C03` | yes |
| L4 Cross-module dependency | file 05 | §end | `CONTRA-04` reinforced | expense and deferred contracts | yes |
| L5 Whole-system semantic model | file 06 | §end | `CONTRA-05` | `GAP-E03` | yes |
| L6 Contradiction / failure / edge case | file 19 | §end | `CONTRA-01a`–`CONTRA-11` | `FE-02`, `FE-22`, `GAP-C04` | **yes — no material blocker arose** |
| L7 Control & internal control | file 14 | §end | `CONTRA-05`, `CONTRA-11` | `GAP-C04` | yes |
| L8 Identity & immutability | file 15 | §end | `CONTRA-07`, `CONTRA-03` | — | yes |
| L9 SaaS / multi-tenant boundary | file 16 | §end | `CONTRA-02`, `SB-01`, `SB-03`, `SB-04` | `GAP-S01` | yes |
| L10 Migration semantics | file 17 | §end | — | `MD-01`–`MD-06` | yes |
| L11 Reconciliation proof | file 18 | §end | `CONTRA-05`, `08`, `09` surfaced as proof failures | `GAP-E03` | yes |
| L12 Adversarial challenge | file 24 | §end | `VETO-01` accepted | — | to Final Gate |

## Expert review lineage (AAS-03)

Four expert reviews plus one independent challenge unit were commissioned in parallel against the
evidence base, each required to verify primary source independently.

| Unit | Returned | Findings | Corrections accepted |
|---|---|---|---|
| Expert 1 — Functional Design | yes | 10 | `COR-01`, `COR-02`, `COR-03`, `COR-04`, `COR-08` |
| Expert 2 — Database Design | yes | 9 | `COR-05`, `COR-06`, `COR-07`, `COR-08`, `COR-09` |
| Expert 3 — Integration & Localization | yes | 13 | `COR-14`, `COR-17`, `COR-20` |
| Expert 4 — Code & UI Architecture | yes | 14 | `COR-07`, `COR-15`, `COR-16`, `COR-18`, `COR-19` |
| Independent Challenge Unit | yes | 8 challenges + 7 independent findings | `COR-10`–`COR-13`; `VETO-01` |

**20 corrections accepted, each re-verified against primary source by the research team before
incorporation.** No expert report was accepted on its own authority.

## Evidence lineage

| Anchor | Value |
|---|---|
| Repository | `AI-Collaboration-Hub` |
| Branch | `research/account-wave-a-core-2026-09-04-001` |
| Base commit | `8d2c8aa`, from `origin/SMEsPlus` |
| Primary reference source | Enterprise build `18.0+e.20250608`, modules `account`, `account_accountant`, `account_reports`, `l10n_th`, `l10n_th_reports`, framework base |
| Prior-session evidence cited | Inventory v2.0 (`HELD`), COGS Deep Research (`HOLD`) and Targeted Resolution (`PARTIAL RESOLUTION`), Asset Deep L1–L6 (terminal state B), Account Batch A routing (all gates open) — each cited **with its own terminal state**, none re-adjudicated |

## Governance compliance record

| Requirement | Record |
|---|---|
| `No Evidence = No Progress` | every material conclusion carries an `EV`/`COR` reference or is marked `UNKNOWN — EVIDENCE REQUIRED`; 28 open unknowns declared rather than filled |
| `Never Skip Gate` | Levels 1–12 executed; four additional Levels beyond the Asset baseline |
| `No repeated question without a material delta` | no question re-asked; corrections superseded prior claims additively |
| Independent review (principle 7) | five independent units; the research team reviewed none of its own conclusions |
| No self-approval | no gate moved, no approval issued, no implementation authorised |
| Clean-room boundary | Layer 2 quarantine separated from Layer 1; vendor tokens confined to the quarantine files |
| Thai statutory discipline | seven statutory items `HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track; all Thai names candidate / UNVALIDATED |
| Prohibited verdict vocabulary | mechanical scan run across the package; two incidental occurrences found and corrected before commit |
| No source modification | nothing under the reference source tree was written |
