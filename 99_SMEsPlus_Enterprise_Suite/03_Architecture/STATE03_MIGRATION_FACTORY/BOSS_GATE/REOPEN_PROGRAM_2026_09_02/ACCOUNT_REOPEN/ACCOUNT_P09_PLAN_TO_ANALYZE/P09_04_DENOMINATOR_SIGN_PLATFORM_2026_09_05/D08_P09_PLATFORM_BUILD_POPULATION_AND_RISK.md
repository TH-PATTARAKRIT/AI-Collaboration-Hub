# D08 — P09_PLATFORM_BUILD_POPULATION and D09 — PLATFORM_BUILD_RISK_MATRIX

**Checkpoints:** `CP-P09D07`, `CP-P09D08` · **Layer:** 1 — clean-room.
**P09 ranks risk. P09 does NOT select the canonical build — that is a P11 / AAS+ / PMO / Boss domain.**

---

## 1. BUILD DENOMINATOR — CORRECTED

| Round | Stated | Verdict |
|---|---|---|
| P09#04 | "two candidate builds with opposite filters" | **CONTRADICTED** |
| **P09#05** | **four candidate v19 builds carrying the budget module** | measured |

**Unit = one build tree containing the budget module's consumption query.** Three carry Gate A; **one** carries Gate B.

## 2. THE POPULATION

| # | Build | Gate | Notes |
|---|---|---|---|
| 1 | migration enterprise tree | **A** | |
| 2 | migration combined tree | **A** | |
| 3 | source-code enterprise tree | **A** | |
| 4 | **the primary v19 enterprise tree** | **B — admits balance-sheet types** | the divergent one |

**Provenance of the divergence — upstream change or local modification — is `NOT DECIDABLE`:** no version history is available in any tree.

## 3. RISK MATRIX

| Dimension | Gate-A builds (3) | Gate-B build (1) |
|---|---|---|
| **management-accounting integrity** | zeroing confined to net-balance surfaces | **zeroing reaches budget consumption as well** |
| **`TH-F-01` exposure** | none — the v19 Thai template types correctly | none |
| **`TH-F-02` exposure** | **none** | **present — 169,954 records, −277 M swing** |
| **zeroing risk** | entry-level, confirmed at 99.99 % | entry-level **plus** budget-surface |
| **double-counting risk** | unchanged — source-only, unexercised | unchanged |
| **scope integrity** | unchanged | unchanged |
| **Thai chart compatibility** | template correct in v19 | template correct in v19 |
| **asset interaction** | depreciation cost visible in consumption | **depreciation cost collapses in consumption** |
| **P03 cost interaction** | unchanged | unchanged |
| **P08 ledger interaction** | account-type semantics conventional | **account-type semantics materially different — P08 must rule** |

**Ranked risk: the Gate-B build carries one additional CRITICAL exposure that the other three do not.** That is a risk statement, not a recommendation, and **not a selection**.

## 4. WHAT MUST BE DECIDED, AND BY WHOM

| Question | Owner |
|---|---|
| which build each deployment actually runs | **runtime evidence** — `HOLD — RUNTIME EVIDENCE REQUIRED` |
| whether Gate B's account-type reading is correct | **P08** |
| which build SMEsPlus adopts | **P11 / AAS+ / PMO / Boss — NOT P09** |

## CHECKPOINT
**`CP-P09D07`, `CP-P09D08` — COMPLETE — EVIDENCE VERIFIED.** Build denominator corrected from 2 to 4; risk ranked; **no selection made**. Auto-continue.
