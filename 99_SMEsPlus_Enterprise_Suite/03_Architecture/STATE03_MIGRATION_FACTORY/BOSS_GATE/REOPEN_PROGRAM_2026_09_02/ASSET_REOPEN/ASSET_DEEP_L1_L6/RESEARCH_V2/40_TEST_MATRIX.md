# 40 — TEST MATRIX
**LAYER 2 — AUDIT QUARANTINE**

§83, T01–T40.

## Method and its limits — read first

| Method | Meaning | Class |
|---|---|---|
| `SIM` | Executed against `EV-SIM` — a line-by-line transcription of the reference board algorithm from primary source | **`SUPPORTED INTERPRETATION`**. Not a runtime execution |
| `SRC` | Determined by reading the primary source path | `FACT VERIFIED` |
| `RT` | Corroborated by runtime evidence | `FACT VERIFIED` |
| `BLK` | **Could not be executed this session.** Needs the running system | `UNRESOLVED` |

Standing assumption for every `SIM` row: fiscal year = calendar year, not verified
per company.

Standard test asset unless stated: 1,200,000.00 · straight line · monthly periods ·
no not-depreciable amount.

## Depreciation arithmetic

| ID | Scenario | Method | Result |
|---|---|---|---|
| T01 | Straight line, 31-day month | `SIM` | Daily mode 20,372.40 · 30/360 mode 20,000.00 · **+1.86%** |
| T02 | Straight line, 30-day month | `SIM` | Daily 19,715.23 · 30/360 20,000.00 · **−1.42%** |
| T03 | February, 28 days | `SIM` | Daily 18,400.87 · 30/360 20,000.00 · **−8.00%** |
| T04 | February, 29 days (2028) | `SIM` | Daily 19,058.05 · 30/360 20,000.00 · **−4.71%** |
| T05 | Mid-month acquisition (15 Jan) | `SIM` | **61 lines** both modes. First 11,171.96 daily / 10,967.74 30-360 |
| T05b | Month-end acquisition (30 Apr, 31st, 29 Feb) | `SIM` | Single-day first period; totals exact in every case |
| T06 | 60 months producing 61 lines | `SIM` | **Reproduced.** 60 lines when acquired on the 1st; 61 when acquired mid-month |
| T07 | Partial first + partial final reconciliation | `SIM` | **Exactly one full period, to the cent, in both modes.** 30/360: 10,967.74 + 9,032.26 = 20,000.00. Daily: 11,171.96 + 9,200.44 = 20,372.40 |
| T07b | Rounding drift across 61 periods | `SIM` | **Zero** in every scenario tested. No plug entry ever required |
| T07c | **Custom Thai method vs standard calendar-day mode** | `SIM` | **Equivalent within 0.03 THB per period, 0.01 cumulative**, across four acquisition patterns — `17` §3 |

## Residual

| ID | Scenario | Method | Result |
|---|---|---|---|
| T08 | Residual exists (1,000 of 12,000) | `SIM` | 11,000.00 depreciated over 12 lines; final book value exactly 1,000.00 |
| T09 | Residual = 1 | `SIM` | 11,999.00 depreciated; 1.00 retained. Held |
| T10 | Fully depreciated asset | `SRC` | Depreciable value 0; **asset stays `open`; no state signals it** |
| T11 | Fully depreciated + equipment still active | `SRC` | **Not representable.** No mechanism, no record, no report |
| T12 | Fully depreciated + equipment removed from production | `SRC` | Not representable |

## Lifecycle

| ID | Scenario | Method | Result |
|---|---|---|---|
| T13 | Asset modified | `SRC` | Catch-up, reverse future, rebuild. History untouched. Children cascaded |
| T14 | Asset paused | `SRC` | Catch-up entry posted; state → paused. **No lock-date check in this module** |
| T15 | Asset resumed | `SRC` | Paused days accumulated; **schedule shifts and the end date extends**; total unchanged |
| T16 | Sold above book value | `SRC` | Difference to the company gain account. Posted and stored figures can differ by the residual — `CTR-05` |
| T17 | Sold below book value | `SRC` | Difference to the company loss account |
| T18 | Disposed mid-period | `SRC` | Catch-up to the disposal date, then the disposal entry |
| T19 | Analytic changed mid-life | `SRC` | **Future entries only. No audit trail, no divergence report** |
| T20 | Multi-company | `SRC` / `RT` | Company checks on every relational field. Runtime: all 280 assets in one company; three others empty |
| T21 | Period locked | `SRC` | Guarded on disposal and re-evaluate. **Not guarded on confirm or pause in this module** — `UNR-09` |
| T22 | Asset Model changed | `SRC` / `RT` | **No effect.** Runtime: **all 280 assets have no model linked at all** |

## Equipment and production

| ID | Scenario | Method | Result |
|---|---|---|---|
| T23 | Equipment without an asset | `SRC` | Normal, and the majority case |
| T24 | Equipment linked to an asset | `SRC` | Custom `Many2one`. Status flips on confirm. **Three of four intended behaviours inert** |
| T25 | Equipment in a work centre | `SRC` | Supported. Carries **capacity, not cost** |
| T26 | Operation **not** using that equipment | `SRC` | **The distinction cannot be expressed** |
| T27 | Operation using that equipment | `SRC` | **Cannot be expressed** |
| T28 | Several machines in one work centre | `SRC` | Supported structurally; **indistinguishable for costing** |
| T29 | Machine-hour allocation | `SRC` | **Measurement does not exist.** Duration is recorded against the work centre |
| T30 | Work-centre-hour allocation | `SRC` | **Available** — this is what the reference chain already uses |
| T31 | Production-quantity allocation | `SRC` | **Available** from the manufacturing order |
| T32 | Production incomplete / WIP | `SRC` | Work-order cost accrues; absorbed only on completion |
| T33 | No finished goods yet | `SRC` | No absorption, no labour entry |
| T34 | Maintenance period | `SRC` | Blocks work-centre capacity. **No cost** |
| T35 | Breakdown | `SRC` | Corrective request. **No cost** |
| T36 | Idle | `SRC` | **Not recorded at all** |

## Management ledger

| ID | Scenario | Method | Result |
|---|---|---|---|
| T37 | Post-depreciation off-balance usage | `SRC` | **No concept.** `DESIGN CANDIDATE` |
| T38 | Cumulative internal usage exceeding residual | — | **Not evaluable.** Contested — `D5-01`, `UNR-B3` |
| T39 | Disposal after internal usage | `SRC` | **The residual is absorbed into gain/loss at disposal**, so the management ledger loses its reference base — `18` §6 |
| T40 | Financial book value unaffected by off-balance usage | `SRC` | **Structurally supported**: off-balance accounts are excluded from all three asset accounts by field domain. The boundary is enforced, not merely policy |

## Tests that could not be executed

| ID | Test | Blocking |
|---|---|---|
| T-B1 | Confirm into a locked period | `UNR-09` |
| T-B2 | Duplicate equipment links, counted | `UNR-08` |
| T-B3 | Analytic divergence, counted | `UNR-11` |
| T-B4 | Import-field usage, counted | `UNR-26` |
| T-B5 | Computation mode of the 217 running assets | **`UNR-02` — highest priority** |
| T-B6 | Sell a linked asset and observe the equipment | `UNR-13` |
| T-B7 | Board invariant violations from migration | `UNR-25` |
| T-B8 | Transactional failure mid-modify | `UNR-10` |

## Counts

| | |
|---|---|
| Scenarios defined | 40 + 6 supplementary |
| Executed by simulation | 11 |
| Determined from source | 27 |
| Corroborated by runtime | 3 |
| **Blocked** | **8** |
