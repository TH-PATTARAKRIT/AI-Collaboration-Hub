# 35 — G02-P02 EIGHT BUSINESS SCENARIOS — FINAL ASSURANCE

`LAYER 2 — AUDIT QUARANTINE.` Task **C6**. Baseline `ff8be51`.

`24` analysed all eight against **two source generations**. `L-07` in `30` recorded that as a coverage
gap once four generations became readable. This file **restates each scenario's basis** rather than
inheriting it, and **closes the two items `24` explicitly left open** with deployed measurement.

---

## 1. Disposition

| # | Scenario | Basis in `24` | Added this round | **Final disposition** |
|---|---|---|---|---|
| 1 | Drop-shipping | v18 + v19 source | — | **PEER DEPENDENCY — P01** |
| 2 | Credit control | v18 + v19 source | **deployed measurement, 11 databases** | **P02 DESIGN GAP + EVIDENCE REQUIRED** (§2) |
| 3 | Unrealised FX revaluation | v18 + v19 source | — | **PEER DEPENDENCY — P08 / P06** |
| 4 | Bill-and-hold | v18 + v19 source | `P02-F-34b/c` cut-off measure | **PEER DEPENDENCY — P10** |
| 5 | Outbound consignment | v18 + v19 source | — | **P02 DESIGN GAP** (revenue-trigger question) |
| 6 | Warranty / return provision | v18 + v19 source | — | **PEER DEPENDENCY — P08** |
| 7 | Freight charges | v18 + v19 source | **deployed custom module read** (`CA-03`) | **VERIFIED BUT ROUTED — P07 / P08** (§4) |
| 8 | Serial / lot COGS | v18 + v19 source | **deployed measurement, 7 databases** | **P02 RETAINS — v19 defect, LIVE population** (§3) |

**Generation basis, stated honestly.** Scenarios 1, 3, 4, 5, 6 rest on **v18 + v19 source only**. The two
v14 deployments and the two v16 deployments were **not** re-analysed for them — v16 contributes 59
module directories on this host and v14 127, far short of a distribution (`31` §1). **Those five
scenarios are therefore `SOURCE GAP` for generations 14.0 and 16.0**, and that is a residual gap this
round does not close.

---

## 2. Scenario 2 — Credit Control: The Open Item Closes Somewhere Awkward

`24` left open *"whether any tenant sets differing per-company credit limits"*. Measured across all 11
material deployments (`res_partner.credit_limit`, offline extraction):

| deployment | gen | partners | credit_limit set |
|---|---|---|---|
| `25e88cd4` iErpOCC | 14.0 | 5,732 | **1,204 (21.0%)** |
| `5d5164c4` odoo_cff | 14.0 | 16,306 | 0 |
| `551ab874`, `4b766580`, `1d1f5d3e`, `57d32e15` | 18.0 | 10,399 | 0 |
| `a1430edc`, `66d1b52a`, `1f6338ae` | 19.0 | 34,787 | 0 |
| `45a8e08e` iSMEs, `a1cdeab8` | 16.0 | — | **column does not exist in 16.0** |

**`P02-F-35a`. Exactly one deployment uses credit limits — and it is the one whose code cannot be read.**
1,204 customer credit limits are configured in `iErpOCC`, a 14.0 deployment carrying `inherit_sales`,
`inherit_inventory` and `inherit_log_occ`, **all `SOURCE GAP`** (`31` §3).

**The bounded claim.** `N-1` (no credit-limit hard block) was established against **v18 and v19** source.
It **does not transfer** to 14.0: the v14 root here is partial and the sales override is unreadable.
So P02 must say: *1,204 credit limits exist in a live deployment, and whether that generation enforces
them is `EVIDENCE REQUIRED` — not "advisory only".* Asserting the v18/v19 finding there would be exactly
the source-versus-deployed conflation this round exists to prevent.

---

## 3. Scenario 8 — Serial / Lot COGS: The Population Is **Not** Empty

`24` left open *"the deployed population of lot-valuated products"*. Measured (`product_template.lot_valuated`):

| deployment | gen | templates | **lot_valuated** |
|---|---|---|---|
| `57d32e15` pfp-staging | 18.0 | 51 | **7** |
| `4b766580` pankhamhom | 18.0 | 105 | **1** |
| `a1430edc` iTEST02 | **19.0** | 83,753 | **1** |
| `551ab874`, `1d1f5d3e`, `66d1b52a`, `1f6338ae` | 18.0/19.0 | 5,194 | 0 |
| `45a8e08e`, `25e88cd4`, `5d5164c4` | 16.0 / 14.0 | — | column absent |

**`P02-F-35b`. Nine lot-valuated product templates exist across three deployments, and one is on 19.0 —
the generation where `24` found the `lot_valuated + standard` divergence was introduced.** The scenario-8
defect therefore has a **non-empty deployed population**. It stays **`P02 RETAINS`** and is **not**
downgraded to latent. The population is small (1 template on v19), so the exposure is bounded — but it
is not zero, and "bounded" and "absent" are different dispositions.

---

## 4. Scenario 7 — Freight: Deployed Evidence Added

`CA-03` in `32` read `scgl_occ_transportation_costs`, installed in `551ab874`. Freight is computed and
stored **on the sale order** as `net_cost` / `unit_cost` / `total_cost` and **never posted**. So in that
deployment freight reaches neither COGS, revenue nor tax through this module — consistent with `24`'s
source finding (`N-6`: no freight cost account in the delivery modules) and now **corroborated in a
deployment by a different instrument**. Routing to **P07** (tax) and **P08** (account) is unchanged.

---

## 5. `RE-27` — A Control That Caught A False Zero In This Round

**Both §2 and §3 were first measured with a broken predicate.** The set-value test read
`v != "f" && v != "0" && v+0 != 0`. For a PostgreSQL boolean the `COPY` value is `t`, and `"t"+0 == 0`,
so **every true boolean was silently counted as unset.** The first run reported `lot_valuated = 0`
everywhere — a clean, plausible, publishable zero.

**It was caught by a positive control, not by inspection:** the same instrument was run against
`product_template.sale_ok`, which cannot plausibly be zero. It returned **0**, which is how the defect
surfaced. After the fix, `sale_ok` returns 1,568/3,722 and 70,730/83,753, and `lot_valuated` returns
**9, not 0**.

**Consequence if unfixed:** scenario 8 would have been downgraded from a retained defect to "latent, no
deployed population" — a real severity change, published on an artefact of the instrument. Numeric
columns were unaffected, so §2's 1,204 stands unchanged and was re-verified after the fix.

**This is the fifth instance in P02 of a control that could not fire**, and the second in this round
(`RE-25` was the injection sized to 40 fields when the column sat at 45).

---

## 6. Negative Claims Requiring A Disjoint Second Instrument

The prompt requires that any material negative resting on one search form gets a second instrument or a
positive control. Status of `24` §4:

| Claim | Second instrument this round | Status |
|---|---|---|
| `N-1` no credit-limit hard block | **Deployed measurement** (§2) — disjoint from source grep | Held for v18/v19; **withdrawn for 14.0/16.0** |
| `N-6` no freight cost account | **Custom-module read** (`CA-03`) — disjoint instrument, deployed | **Corroborated** |
| Scenario 8 population | **Deployed measurement + positive control** (§3, `RE-27`) | **Corrected — population non-empty** |
| `N-2` … `N-5`, `N-7`, `N-8` | **None added.** Still single-instrument source negatives, v18/v19 only | **`EVIDENCE REQUIRED`** — carried to `37` |

**Six of the eight negative claims still rest on one instrument and two generations.** That is stated
rather than quietly inherited.
