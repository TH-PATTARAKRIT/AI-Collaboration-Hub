# S13 — P09_ASSET_CONTRADICTION_REFRESH

**Checkpoint:** `CP-P09S13` · **Layer:** 1 — clean-room.

---

## 1. THE TWO ITEMS

| ID | What it is |
|---|---|
| **`HOLD-AS-01`** | whether a prior Asset package's costing-veto premise — *"depreciation already reaches production cost centres through the analytic distribution"* — survives the finding that the attribution annihilates |
| **`DIS-09`** | the same disagreement, preserved as a dissent between two parallel evidence tracks |

## 2. PEER EVIDENCE CONSUMED THIS CHECKPOINT

| Peer | Head at consumption | Change since last consumption | Action |
|---|---|---|---|
| P04 — Acquire-to-Retire | `6953856` | **unchanged** | not reprocessed, per the idempotence rule |
| P03 — Manufacture-to-Cost | `506cf65` | **unchanged** | not reprocessed |
| P07 — TH Tax Compliance | `9a99c01` | first consumption | consumed |
| P08 — Record-to-Report | `4bdf8a2` | first consumption | consumed |
| P10 — Time-Based Recognition | `f9b40b3` | first consumption | consumed |
| P02 — Order-to-Cash | `89928aa` | not materially relevant | recorded only |
| P11 — Core Reconciliation | **no branch published** | — | **`HOLD — PEER PROCESS RECONCILIATION REQUIRED`** |

**No peer commit changed materially since P09 last consumed it.** Under the idempotent-resume rule, the reconciliation checkpoint is **not reopened**.

## 3. CLASSIFICATION

| Item | Status |
|---|---|
| **`HOLD-AS-01`** | **CONTRADICTION STRENGTHENED** |
| **`DIS-09`** | **UNCHANGED — preserved verbatim** |

### Why strengthened, and why still not adjudicated

The premise under dispute is that depreciation *reaches* production cost centres analytically. This supplement measures that in deployed data: the records reach the cost centre and **98.57 % of their value annihilates on arrival**. The premise is therefore **weaker than when the dispute opened** — the records exist, the value does not survive.

**P09 still does not adjudicate.** Strengthening one side of a two-track disagreement is not authority to close it. Three reasons, stated so the restraint is testable:
1. the prior Asset package's premise may rest on evidence P09 has not seen;
2. the surfaces disagree — an account-bucketed consumption view *does* show the full cost, so "reaches the cost centre" is true on some surfaces and false on others, and which surface the premise meant is not P09's to decide;
3. **cross-track reconciliation is a Boss-level decision.**

**Routed to P11 as `HOLD — CROSS-PROCESS RECONCILIATION REQUIRED`.**

## CHECKPOINT

**`CP-P09S13` — COMPLETE — EVIDENCE VERIFIED.** `HOLD-AS-01` strengthened, `DIS-09` unchanged, neither adjudicated. Auto-continue.
