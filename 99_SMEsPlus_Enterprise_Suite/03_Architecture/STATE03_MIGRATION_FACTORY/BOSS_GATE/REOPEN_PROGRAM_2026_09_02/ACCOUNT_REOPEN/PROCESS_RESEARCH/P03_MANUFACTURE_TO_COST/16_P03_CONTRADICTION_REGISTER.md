# 16 — P03 CONTRADICTION REGISTER

**LAYER 2 — AUDIT QUARANTINE.**

A contradiction is two behaviours in the system that cannot both be correct. It is a
stronger claim than a defect and is used sparingly.

---

## 1. Contradictions

| ID | Contradiction | Both sides | Class |
|---|---|---|---|
| `CTR-P03-01` | Overlapping time logs are **merged** for display and **summed** for costing | `mrp_workorder/models/mrp_workorder.py:757-767` (merged) vs `mrp/models/mrp_workorder.py:582-587` (summed) | **CONTRADICTED** |
| `CTR-P03-02` | Efficiency is computed, shown to a user, and refused as an accounting fact | `mrp/models/mrp_workorder.py:325-328` vs the absence of any variance event — `10` §3 | **CONTRADICTED** |
| `CTR-P03-03` | The company guard is applied and then omitted three lines later in one function | `mrp_account/models/mrp_production.py:74` vs `:77` | **CONTRADICTED** |
| `CTR-P03-04` | The rate snapshot is honoured by every display path and ignored by every posting path | `04` §3 | **CONTRADICTED** |
| `CTR-P03-05` | Capitalisation is gated on cost method; relief is gated on valuation mode | `mrp_account/models/mrp_production.py:63-64` vs `:74` | **CONTRADICTED** |
| `CTR-P03-06` | A cost rate that produces a `COMPANY`-scoped financial effect sits on a record permitted to have **no company** | `mrp/models/mrp_workcenter.py:43` vs `:497` — `18` §4 | **CONTRADICTED** |
| `CTR-P03-07` | **The production-account help text names as permanent the residue that is cleared, and omits the one that remains** | `mrp_account/models/product.py:126-128` vs `mrp_account/models/mrp_production.py:82-84` — `25` §4 | **CONTRADICTED** |

## 2. Gaps — absent rather than contradictory

| ID | Gap | Class |
|---|---|---|
| `P03-GAP-01` | Manufacturing appears in **0 of 10** target end-to-end processes and **0 of 15** module specifications — `01` §6 | `FACT VERIFIED` |
| `P03-GAP-02` | The joint / co-product cost model is owned by no track — `12` §3 | `FACT VERIFIED` |
| `P03-GAP-03` | No fixed-overhead absorption model, and therefore no capacity denominator — `02` §2 | `FACT VERIFIED` |
| `P03-GAP-04` | No rework object — `11` §3 | `FACT VERIFIED`, scope declared |
| `P03-GAP-05` | No normal/abnormal scrap distinction — `11` §1 | `FACT VERIFIED`, scope declared |
| `P03-GAP-06` | **No tenant boundary exists anywhere in the reference manufacturing source** — `18` §1 | `FACT VERIFIED`, scope declared |
| `P03-GAP-07` | Master data may be owned by **no** scope via an empty company — `SCOPE-01`, `18` §2 | `FACT VERIFIED` |

### Round 3 — runtime findings

| ID | Finding | Class |
|---|---|---|
| `P03T-F-01` | Conversion cost is **zero** across 9,807 completed manufacturing orders; FG carries material cost only | `FACT VERIFIED` |
| `P03T-F-02` | No project custom addon overrides any manufacturing cost model — positive control fired on all three roots | `FACT VERIFIED` |
| `P03T-F-03` | Zero work centres, routing operations, work orders and time logs in all three readable deployments | `FACT VERIFIED` |
| `P03T-F-04` | 4 of 15 cost-injection mechanisms are live; none is a conversion-cost mechanism | `FACT VERIFIED` |
| `P03T-F-05` | **Every** conversion-cost element exhibits zeroing; **none** exhibits double counting in live data | `FACT VERIFIED` |
| `P03T-F-06` | Fixed overhead has no path, and the assumed analytic route is structurally incapable | `FACT VERIFIED` |
| `P03T-F-07` | The system has too many mechanisms **and** none in use — the veto's limb is unanswerable as written | `SUPPORTED INTERPRETATION` |
| `P03-GAP-08` | Indirect labour and the overhead pool are owned by **no** process | `FACT VERIFIED` |

## 3. Unresolved

| ID | Item | Class |
|---|---|---|
| `UNR-P03-01` | Whether the target SMEsPlus configuration uses multi-operator work orders — governs `DC-01`'s magnitude, not its existence | `UNRESOLVED` |
| `UNR-P03-02` | Whether setup and cleanup time is charged once per backorder split — `09` §4 | `UNRESOLVED` |
| `UNR-P03-03` | Performance budget for P03 flows, unsettable until `DEP-09` — `13` §6 | `UNRESOLVED` |
| `UNR-P03-04` | Whether `AE-06`'s subtraction-derived component cost stays correct after a bill correction — `12` §2 | `UNRESOLVED`, routed to P01 |
| `SCOPE-Q-01` | Analytic plan — `TENANT` or `COMPANY`? | **HOLD — SCOPE EVIDENCE REQUIRED** |
| `SCOPE-Q-02` | Productivity-loss taxonomy — `PLATFORM` with tenant extension, or `TENANT`? | **HOLD — SCOPE EVIDENCE REQUIRED** |
| `SCOPE-Q-03` | May one tenant's BOM reference another tenant's product? | **HOLD — SCOPE EVIDENCE REQUIRED** |
| `UNR-P03-05` | Incidence of `DC-14` — whether both analytic distributions resolve to a common account in the target configuration | `UNRESOLVED` |
| `UNR-P03-06` | Whether a second labour relief post is reachable — `DC-15` | `UNRESOLVED` |

## 4. Contradictions with **prior SMEsPlus evidence** — none

P03 checked its findings against the Asset, COGS, Inventory and Account Wave A lineages.

| Prior finding | P03 result |
|---|---|
| `ASSET_DR_CONTINUATION/07` §3 — work centre rejected as cost bucket | **Consistent.** P03 reaches the same place from the cost-injection side |
| `ASSET_DR_CONTINUATION/12` §2 — no fixed/variable distinction exists in the manufacturing cost chain | **Consistent and independently confirmed** — `02` §2 |
| `CTR-C-06` — the work-order rate snapshot is not read by valuation or ledger | **Confirmed**, with the mechanism named — `04` §3 |
| Account Wave A — system-derived accounting date | **Recurs in P03** as `DC-09` |
| Account Wave A — silent 1:1 FX fallback pattern | **Same pattern class** as `DC-07`'s silent COGS fallback |
| `smeplus-asset-deep-l1-l6-findings` — partly dead custom link | **Same class** as `DC-10` |

**No contradiction with prior SMEsPlus evidence was found.** Recorded explicitly, because a
clean result on this check is itself a finding and its absence would have been material.

### Peer cross-check — P04 Acquire-to-Retire

| P04 claim | P03 result |
|---|---|
| Extra unit cost never relieved | **Agrees** — `DC-03`, reached independently |
| Analytic ledger and GL disagree on one work order | **Agrees** — `DC-05`, reached independently |
| The operation has no equipment field | **Agrees** — `04` §2, and Asset `07` §2 makes three |
| Standard-costing GL mismatch | **Agrees**, and P04 supplies the standard's content — `03` §4 |
| Nine monetisation paths vs P03's two | **Not a contradiction — a unit difference.** P03's `01` §3 declared no unit and is corrected; `25` §2 |
| M5 is the weakest of the nine | **P03 dissents — it is stronger than P04 rates it.** `DC-14`, `25` §3 |
| Equipment register is `TENANT`, company-optional correct | **Agrees for the register; P03 dissents on extending it to the asset.** `25` §6 |

**One agreement corrected P03, one dissent is preserved for P11, and no claim was adopted
without independent source verification.**

## 5. A correction this session applied to itself

One hypothesis was raised, tested and **discarded** — that raw-material scrap escapes GL
posting. It is documented in full at `05` §9, including the reasoning that made it
plausible and the single call site that falsified it.

Recorded here because `smeplus-deep-research-negative-claim-standard` treats an untested
plausible negative as the specific failure mode that independent review exists to catch,
and because a register that shows only confirmed findings gives no evidence that anything
was ever tested and rejected.
