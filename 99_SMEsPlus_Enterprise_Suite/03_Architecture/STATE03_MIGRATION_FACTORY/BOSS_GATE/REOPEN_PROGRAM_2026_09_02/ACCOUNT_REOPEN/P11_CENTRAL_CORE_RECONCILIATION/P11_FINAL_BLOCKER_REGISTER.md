# P11 — FINAL BLOCKER REGISTER

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room
Every blocker ends as **exactly one** of the ten permitted statuses. No vague status is used.

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. P11's own blockers

| id | Blocker | Final status |
|---|---|---|
| `P11-B-01` | **`P01`–`P10` have published nothing.** 0 artefacts at 0 commits across 10 processes | **`HOLD — PEER PROCESS REQUIRED`** |
| `P11-B-02` | **No accounting-event identity exists** (`UAE-29`). `C1` fails 44 of 44; `DC-01` unguardable; 9 of 23 dependencies sit downstream | **`HOLD — BOSS DECISION REQUIRED`** — the root |
| `P11-B-03` | **0 of 17 double-counting classes has a working guard.** 4 of the 17 are root-independent design failures | **`HOLD — BOSS DECISION REQUIRED`** |
| `P11-B-04` | **The programme has no declared output path.** Six sibling sessions wrote to six locations; this is a seventh | **`HOLD — BOSS DECISION REQUIRED`** (`P11-F-01`) |
| `P11-B-05` | **`BC-02` binds Inventory → Accounting only.** Nine producing processes hand facts to the ledger under no contract | **`HOLD — BOSS DECISION REQUIRED`** (`P11-F-02`) |
| `P11-B-06` | **`DC-09` double cost absorption.** TAS 2 ¶12 requires absorption; building it without an explicit relief of the period-expense line charges depreciation twice. **No relief mechanism exists in anything the programme has read** | **`HOLD — BOSS DECISION REQUIRED`** — new at P11 |
| `P11-B-07` | **`DC-07` candidate double tax recognition** — `M-02` auto-reverses on unmatch, `M-03` is not stated to | **`HOLD — SOURCE EVIDENCE REQUIRED`** — new at P11 |
| `P11-B-08` | **Four objects have no determinable scope**: tax configuration, equipment/machine ownership, budget, migration/replay batch | **`HOLD — SCOPE EVIDENCE REQUIRED`** |
| `P11-B-09` | **`AASR`'s parent baseline predates its parent's closure** — `V-SYS-2` applied to `AASR` itself | **`HOLD — CONTRADICTION`** (`P11-C-01`) |
| `P11-B-10` | **The `22`-scenario cross-proof baseline stands at 0 of 22 evidenced** — 30 of 30 producer debit/credit cells withheld, 0 of 10 handoffs contract-compliant | **`HOLD — PEER PROCESS REQUIRED`** |
| `P11-B-11` | **Analytic is not a subledger of record**, so no `P09` figure reconciles to the ledger across a correction | **`HOLD — BOSS DECISION REQUIRED`** |
| `P11-B-12` | **`P05` and `P10` producer contracts are not established at all** | **`HOLD — PEER PROCESS REQUIRED`** |
| `P11-B-13` | **The unified event-to-GL matrix has not been reconciled against the published peer matrices** (`P03`, `P04`, `P06` each publish one; `P06` alone carries 31 event→entry rows) | **`HOLD — PEER PROCESS REQUIRED`** |
| `P11-B-14` | **The exception to "unrelated independent companies = separate tenants by default" is undeclared, and no granting authority is named** (`P11-SR-01`) | **`HOLD — BOSS DECISION REQUIRED`** → `D-11` |
| `P11-B-15` | **Whether a company hierarchy may span a tenant boundary is unruled, and no enforced tenant-assignment invariant exists** (`P11-SR-02`) | **`HOLD — BOSS DECISION REQUIRED`** → `D-12` |
| **`P11-B-16`** | **`T0-13` — an accounting fact may be SILENTLY MUTATED, at any scope.** Widened at Delta 04: the defect needs **no tenant boundary and no company hierarchy** — inside a single company an entry aimed at a locked period is already re-dated with no refusal and no trace (`P04-F-68`, `FACT VERIFIED`). **Reachable today, so it stands whatever the Boss rules on `D-12`.** Close condition: **refuse, OR record an attributable trace** | **`HOLD — BOSS DECISION REQUIRED`** · **tolerance-zero** · **present defect, not prospective risk** |

**16 blockers. 0 closed by this session.** `P11-B-13`…`P11-B-16` added by Deltas 01–03.

## 2. Inherited blockers P11 carries forward without weakening

| id | Blocker | Status as its owner declared it |
|---|---|---|
| `GB-01`…`GB-08` | Account Wave A's eight | **`HOLD`**; `GB-08` `BOSS DECISION REQUIRED` |
| `MCU-21` | **The reference core root set is undeclared. 22 roots exist** | **`HOLD — BOSS DECISION`**; cost to close **hours, mechanical** |
| `T0-01`…`T0-12` | Twelve inherited tolerance-zero boundaries | **`UNRESOLVED` ×12, `0` resolved.** `CONDITIONAL PASS` unavailable **by rule** |
| `MCU-01`…`MCU-20` | 17 standing gating unknowns, 8 ledger-gating | **`HOLD`** |
| `JT-01`…`JT-12` | Twelve Joint decisions | **12 open; `JT-01`/`JT-04`/`JT-05` `NOT DECIDABLE`** |
| `BLK-01`, `BLK-02` | Asset UAT items | **`HOLD — UAT REQUIRED`** |
| `BLK-07`, `BLK-08` | Asset design decisions | **`HOLD — DESIGN DECISION REQUIRED`**; AAS+ veto on costing implementation |
| `GAP-FS-07`, `GAP-FS-08`, `RISK-U03`, `RISK-C02` | Inventory structural gaps behind contract elements 10, 14, 15 | **open** |
| `CF-F-04`, `CF-F-05` | Inventory MTI conformance structural gaps | **open** |
| `RC-V-01`, `AAS-V-02`, `AASR-VETO-01`, Asset costing veto | Four standing vetoes | **none discharged** |

## 3. What closes what — ranked by cost, not by severity

| Cost | Items | Work |
|---|---|---|
| **One query each, minutes** | `Q-04` installed-module list (**caps every negative finding in two packages**), `Q-01` day convention, `Q-02` duplicate machine records | UAT, read-only, under ten minutes total |
| **A declaration, hours** | `MCU-21` root set; `P11-B-04` output path; `P11-B-08` four scope determinations | No new research. Closing `MCU-21` **re-scopes `MCU-18`, `MCU-19b`, `GB-07`, `GB-08` and every class `A` absence at once** |
| **A Boss decision, no research closes it** | `P11-B-02` event identity, `GB-08`, `BLK-07`, `JT-03`, `P11-B-05` contract scope, `P11-B-06` absorption relief | — |
| **Business-SME input — no AI may answer** | `SME-Q-02`, `SME-Q-03` → `JT-04`, `JT-05` | — |
| **Thai statutory** | `TH-NEW-01`, `TH-NEW-02`, `TX-H01`…`TX-H07` | Authoritative evidence only |
| **A running instance** | `MCU-01`, `MCU-19`, `MCU-20`, `T0-03`, `T0-07` runtime half, the live FIFO-return test | — |
| **Peer publication** | `P11-B-01`, `P11-B-10`, `P11-B-12`, and 15 of the 30 withheld cells | `P01`–`P10` |

> **The cheapest column is also the most leveraged.** Four queries and three declarations —
> **hours of mechanical work, no new research** — would close or re-scope `Q-01`, `Q-02`, `Q-04`,
> `MCU-21`, `MCU-18`, `MCU-19b`, `GB-07`, `P11-B-04`, `P11-B-08`, and bound every class `A` negative
> claim in the programme. **None of it is blocked on `P01`–`P10`.**
