# 22 — FINAL BLOCKER REGISTER (LEVEL 24)

**LAYER 2 — AUDIT QUARANTINE.**

Each blocker ends as exactly one of the eight permitted statuses. No vague status is
used.

---

## 1. Final status of every blocker

| ID | Item | Final status |
|---|---|---|
| `BLK-01` | Which day convention the 280 live assets use | **HOLD — UAT REQUIRED** |
| `BLK-02` | Whether several assets share one machine record | **HOLD — UAT REQUIRED** |
| `BLK-03` | Does Thai practice permit depreciation absorbed into inventory? | **CLOSED — EVIDENCE VERIFIED** |
| `BLK-04` | How off-balance accounts are treated in Thai statutory statements | **CLOSED — EVIDENCE VERIFIED** |
| `BLK-05` | May internal usage accumulate without bound? | **CLOSED — BOSS DECISION** |
| `BLK-06` | Where does unabsorbed depreciation go? | **CLOSED — BOSS DECISION** |
| `BLK-07` | Is the allocation denominator normal capacity or actual hours? | **HOLD — DESIGN DECISION REQUIRED** |
| `BLK-08` | Does MAINTENANCE split into planned and unplanned? | **HOLD — DESIGN DECISION REQUIRED** |

**Closed: 4. Open: 4.**

## 2. Closure evidence

### `BLK-03` — CLOSED, EVIDENCE VERIFIED

TAS 2 ¶12, standard text per ประกาศสภาวิชาชีพบัญชี ที่ 34/2562: fixed production
overhead — expressly including the depreciation and maintenance of factory buildings,
factory equipment and right-of-use assets used in the production process — forms part of
the conversion cost of inventories. Corroborated from the asset side by TFAC's TAS 16
manual.

**The finding exceeds the question: absorption is required, not merely permitted.**

### `BLK-04` — CLOSED, EVIDENCE VERIFIED

ประกาศกรมพัฒนาธุรกิจการค้า, prescribed line items แบบ 2 for a private limited company:
exhaustive text search of all four prescribed statements returns **no** off-balance,
memorandum or *นอกงบดุล* line item. Off-balance amounts have **no statutory presentation
surface**.

Residual sub-question on bookkeeping standing is carried as `UNR-C-04`, Low, non-blocking.

### `BLK-05` — CLOSED, BOSS DECISION

`BD-01`. No cap, no cut-off, no reduction of residual book value; the terminating
condition is operational eligibility, not an amount. Nothing found this session opposes
it; the platform makes its isolation structurally enforceable.

### `BLK-06` — CLOSED, BOSS DECISION

`BD-02`, reinforced by TAS 2 ¶13, which independently requires unallocated production
overhead to be recognised as an expense in the period incurred.

## 3. Open blockers — what closes each

### `BLK-07` — HOLD, DESIGN DECISION REQUIRED · **the critical one**

| | |
|---|---|
| Question | Is the productive allocation rate `period depreciation ÷ normal capacity hours` (recommended) or `period depreciation ÷ actual productive hours`? |
| Why it cannot be researched | `BD-02` is genuinely ambiguous between the two. Both satisfy "100% attributed". Only one complies with TAS 2 ¶13 |
| What decides it | A Boss ruling, informed by `09` §2–§3 |
| Recommendation | **Normal capacity.** The alternative breaches the standard, is undefined in an idle month, and capitalises idleness into inventory |
| Consequence of deferring | AAS+ veto stands. No costing implementation may begin |
| Owner | Boss |

### `BLK-08` — HOLD, DESIGN DECISION REQUIRED

| | |
|---|---|
| Question | Does MAINTENANCE split into planned (absorbed through the rate) and unplanned (period expense)? |
| Why it cannot be researched | TAS 2 ¶13 requires the distinction; `BD-02` does not make it. Reconciling them is a decision |
| What decides it | A Boss ruling |
| Recommendation | **Split.** The data already exists as a first-class field; the cost of not splitting is misstating inventory and period expense in opposite directions at once |
| Consequence of deferring | The non-productive model cannot be finalised. Does not block anything else |
| Owner | Boss |

### `BLK-01` — HOLD, UAT REQUIRED

Closes on query `Q-01`. Blocks the **migration** decision, not the design — `19` §2
mandates an explicit recorded convention per asset regardless of what the live data shows.

### `BLK-02` — HOLD, UAT REQUIRED

Closes on queries `Q-02` and `Q-03`. Blocks the **per-machine costing** design: a
duplicated machine's cost pool doubles, silently.

## 4. UAT session — the exact queries

All read-only. No create, update, delete or post. Estimated total: under ten minutes.

| ID | Query | Closes | Priority |
|---|---|---|---|
| `Q-01` | Count of assets grouped by prorata computation mode, across all 280 asset records; plus the provenance of the Asset Model export | `BLK-01`, `CTR-01` | **1** |
| `Q-02` | Count of assets with the machine link populated; and the count of machine records referenced by more than one asset | `BLK-02` | **1** |
| `Q-03` | Parent/child relationships among the 280 assets | `BLK-02`, `UNR-06` | 2 |
| `Q-04` | The installed-module list of the running system | **Caps every negative finding in this and the previous package** | **1** |
| `Q-05` | Count of equipment records and work centres with an empty company | `CTR-C-10` — **added by AAS+** | 2 |
| `Q-06` | Distribution of machine count per work centre | Sizes the capture burden — **added by AAS+** | 2 |
| `Q-07` | Count of work centres with a non-zero hourly rate | Whether any machine cost is in finished goods today | 3 |
| `Q-08` | Assets whose analytic distribution differs from that on their own posted entries | Divergence detection | 3 |
| `Q-09` | Assets whose posted depreciation does not sum to the depreciable amount | `CTR-06` — a data-quality check never run | 3 |

**`Q-04` is listed at priority 1 deliberately.** Every "does not exist" in both research
packages is bounded by the source trees in this workspace. That qualifier cannot be
dropped until the running system's installed modules are known, and it is one query.

**No result for any of these is inferred, estimated or assumed anywhere in this
package.**

## 5. Non-blocking items carried forward

| ID | Item | Severity |
|---|---|---|
| `UNR-C-01` | Whether Thai **tax** accepts depreciation absorbed into inventory, and the timing difference | Medium |
| `UNR-C-02` | Internal-usage rate base — three candidates, none evidence-based (`10` §3) | Medium — Boss selection |
| `UNR-C-03` | How a standard-costed product complies with TAS 2 (`CTR-C-09`) | **Medium-High** — AAS+ finding 1 |
| `UNR-C-04` | Bookkeeping standing of a memorandum ledger under the Accounting Act | Low |
| `UNR-C-05` | Is SETUP productive? | Medium — Boss |
| `UNR-C-06` | IDLE and NO_DEMAND — one cause or two? | Low — Boss |
| `UNR-C-07` | Franchise/royalty on production — conversion cost or period cost | Low — per contract |
| `UNR-C-08` | Who sets normal capacity, and the review cadence | Medium |
| `UNR-C-09` | Component depreciation — how components aggregate into one machine cost pool | Medium |
| `HOLD-01`…`HOLD-06` | Statutory items in `18` §6 | Low–Medium |
| The 21 non-blocking items in `LIN-02` `41` Tier 3 | Carried unchanged except `UNR-17`, now answered by `C-03` | — |

## 6. Rejected

| Item | Reason |
|---|---|
| The reading of `BD-02` that divides period depreciation across actual productive hours | **REJECTED — INVALID ASSUMPTION.** It breaches TAS 2 ¶13, is undefined at zero output, and capitalises idleness into inventory. Recorded as rejected so it is not rediscovered as an obvious simplification during build |
| Treating the work-centre hourly rate as the cost bucket for depreciation | **REJECTED — INVALID ASSUMPTION.** Challenged at its strongest in `07` §3 and defeated on the business requirement |
| Using the machine record's own cost field as a cost-pool source | **REJECTED — INVALID ASSUMPTION.** It is a second, inert, unreconciled source of truth (`06` §4) |
| Relying on the work-order rate snapshot as a rate guarantee | **REJECTED — INVALID ASSUMPTION.** Neither the valuation nor the ledger path reads it (`CTR-C-06`) |
