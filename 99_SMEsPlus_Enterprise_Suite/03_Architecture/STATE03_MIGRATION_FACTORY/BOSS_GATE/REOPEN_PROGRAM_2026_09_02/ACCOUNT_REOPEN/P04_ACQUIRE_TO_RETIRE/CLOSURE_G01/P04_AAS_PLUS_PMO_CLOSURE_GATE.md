# P04 — AAS+ RECONCILIATION AND PMO CLOSURE GATE

**LAYER 2 — AUDIT QUARANTINE.** Prompt §10.

---

## PART A — AAS+ RECONCILIATION

### A.1 Agreements between P04 and P03

| Item | Status |
|---|---|
| Operation → specific Equipment does not exist | **Agreed, independently derived on both sides, same series** |
| Equipment → Asset absent in the reference product | **Agreed** — P03 from manufacturing, P04 from the asset side with a firing control |
| Work-centre membership ≠ cost absorption | **Agreed**; P03 measured it, P04 adds the cardinality reason |
| The allocation denominator is Boss-owned | **Agreed.** P03 routed it to this register; P04 keeps it open |

### A.2 Where P04 goes beyond P03, and where it stops

P03 reported the asset↔equipment link as absent **in the reference product**. P04 confirms that
and adds the half P03 did not examine: **a custom module supplies a one-directional link**, with
a dead duplicate beside it. **P04 does not extend this into manufacturing** — the interface
contract in `CQ-P04-07` §3 names P03/MRP as producer and stops at the boundary.

### A.3 Corrections made against P04 itself in this run

| # | Correction | Found by |
|---|---|---|
| 1 | *"Model policy applies only in a form"* — **false**; `_auto_create_asset` calls the onchange explicitly | **P04's own mandated disproof** |
| 2 | *"`equipment_sequence` cannot install"* — **false**; installed at `18.0.1.6`, the file is never imported | The installed set |
| 3 | *"Two day conventions"* — there are **three**; `none` is not a rounding variant | Field selection read in full |
| 4 | *"30/360"* — the non-daily branch **scales boundary months by real length** | The function read in full |
| 5 | *"Partly dead code"* — right but uncharacterised; now exactly 3 of 8 files, one of them the older duplicate link | Import graph |

### A.4 Dissent preserved

**C-2's positional-indexing risk** (`line_ids[::2]`) is recorded as a structural risk and **not**
elevated to a finding: no entry shape violating the assumption was observed. A reader may
reasonably rank it higher than this package does.

### A.5 Unavailable evidence

| Item | Class |
|---|---|
| Series-16 source for the v16 deployment | `UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`, `P04-B-51`. **Reliance on P03's enumeration declared** |
| Runtime cardinality and expense/capitalise overlap | `P04-B-53` — source-scoped run cannot measure it |
| `ir.rule` company restriction | `P04-B-54` — a second instrument, not examined |

---

## PART B — PMO GATE

### B.1 Is P04 sufficiently understood to serve as controlled SMEsPlus functional-design input?

> **Qualified YES, for the functions in the Design Input Pack, and NO for anything requiring
> the allocation denominator.**

**Sufficient:** asset lifecycle; depreciation policy and its application paths; the day
convention and its deployed usage; asset↔equipment as it actually exists; non-asset equipment;
the analytic bridge and its net-to-zero cause; disposal and residual semantics; the
off-balance constraint.

**Not sufficient, and named:** anything downstream of `BLK-07`. DF-08 and DF-09 cannot be
specified before the denominator is chosen, and DF-10 cannot be structured before the
off-balance chart decision (**P08**) and the cardinality decision.

### B.2 Ownership split

| Owner | Items |
|---|---|
| **P04** | DF-01…DF-06, DF-10 (asset side), DF-11, DF-13; `BLK-07` custody; `P04-BD-05`…`-09` |
| **P03 / MRP** | The Equipment Usage Event producer side (DF-07) |
| **P05** | Repair/vendor expense; non-asset equipment expensing; stranded equipment records |
| **P07** | Day-convention statutory admissibility; every tax limb |
| **P08** | Off-balance chart structure; period-lock integrity; analytic reporting consequence |
| **P11** | Six surviving architecture contradictions; six Boss decisions |
| **Inventory / MRP** | Interface contract only — **no execution** |

### B.3 Does any new broad research require separate authorisation?

> **Yes — three, and none was started.**
> 1. Mounting and reading a **series-16** addons tree (`P04-B-51`) — outside this host's
>    declared path set.
> 2. A **runtime** pass over the keyed archives for cardinality and expense/capitalise overlap
>    (`P04-B-53`, `P04-B-55`).
> 3. A **record-rule** pass for company scope (`P04-B-54`).
>
> Each is bounded and named. **None is authorised by this prompt**, and none was performed.

### B.4 Gate conditions **not** discharged

- `AAS+` veto on implementation start — **stands**.
- PMO conditions from the base package — **stand**.
- `0 of 4` inherited blockers closed; **7 new blockers registered**.
- **No PASS. No Final Freeze. No merge. No implementation authorisation.**
