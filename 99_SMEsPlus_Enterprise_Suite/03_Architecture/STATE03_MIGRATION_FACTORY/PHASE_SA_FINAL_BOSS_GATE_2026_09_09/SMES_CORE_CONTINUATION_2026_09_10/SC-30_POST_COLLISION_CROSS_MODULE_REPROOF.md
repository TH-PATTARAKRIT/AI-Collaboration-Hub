# SC-30 — POST-COLLISION CROSS-MODULE RE-PROOF

## CP-SA-SC-240 — CROSS-MODULE BASELINE RE-PROVEN, AUTHORITY-SENSITIVE ROWS BOUNDED

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · head consumed `2cfb57eb`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

---

## 1. Result, and the honest limit on it

> # `THE MODEL RE-PROVES. THE AUTHORITY-SENSITIVE ROWS CANNOT BE FINALISED, AND ARE NOT.`

**`05_` §9 asks for a re-run against *"the canonicalized authority baseline."* That baseline is
canonicalized only conditionally** (`SC-29` §4) — the `FG-F-06` collision is undisposed. **So this file
separates what is determinable from what is not, rather than re-running everything against an undetermined
base and reporting a number that would have to be withdrawn.**

| | |
|---|---|
| Routing convergence rules | **6 of 6 hold** — §2 |
| 22 joint cross-proof scenarios | **10 / 12 / 0** — unchanged, re-derived |
| 18 end-to-end scenarios | **9 / 9 / 0**, `1` `NOT TRAVERSABLE` — unchanged |
| Rows changed by the `FG-F-06` disposition | **`0` scenario rows.** `FG-F-06` changes **whether the gate is open**, not what any row contains — §3 |
| Tolerance-zero paths affected by `EC-04` | **3**, all **`0`-closed** — §4 |
| Veto-sensitive paths | **6 vetoes, 0 discharged** — unchanged |
| **Progress-biased reclassification** | **`0`** — §6 |

---

## 2. Routing convergence — re-run, 6 of 6

| Mandatory rule | Result |
|---|---|
| Stock-affecting → Inventory | **HOLDS** |
| Manufacturing-required → Manufacturing | **HOLDS** |
| Procurement / dropship-required → Purchase | **HOLDS** — and `SC-BD-08` ruled `F3` **option (a)**: the direct-shipment route resolves a movement chain under the product category's ruled policy, **no route-specific exception**. The reference's dropship capability remains **installed in `0` of 3 deployments**, so no vendor implementation became SMEsPlus policy |
| Every material business flow → Accounting semantic reconciliation | **HOLDS** — 29 of 29 flows carry an explicitly determined semantic; **14 carry a named open element**, unchanged |
| One output may feed multiple consumers | **HOLDS** — `XMC-H-09` (Asset → Equipment, missing consumer) remains the one recorded defect |
| `INPUT → PROCESS → OUTPUT → DOWNSTREAM ROUTING → NEXT MODULE INPUT` closes | **HOLDS** at the level of route |

**Inventory convergence:** valuation facts arise under `BD-ACC-03A`'s Product-Category policy; the
direct-shipment chain records **counterparty endpoints** (supplier origin, customer destination) as
external, **not `N/A`**. **Accounting convergence:** cost recognition binds to the **same canonical
Accounting Event Identity** as the revenue recognition (`XMC-C-C6` + `BD-ACC-01`), Tenant + Company bounded.

---

## 3. `SC-F-16` — the `FG-F-06` disposition changes `0` scenario rows

**Measured rather than assumed.** The disposition determines **whether Phase SA may exit**, not what any
scenario contains. Tested against the three classes that could plausibly move:

| Candidate class | Moves on the disposition? | Why |
|---|---|---|
| Scenario **content** (the 22 and the 18) | **NO** | Neither reading changes a semantic, a routing rule or an expected value |
| Scenario **category** (1 / 2 / 3) | **NO** | Category 2 = "the named break is a Boss election"; the elections are the same under both readings |
| **Gate admissibility** of the 16 rulings | **YES — and it is not a scenario row** | `SC-24` §2 element 9; routed to `SC-AUTH-01` |

> **The authority collision is a gate-level fact, not a model-level one.** That is why the cross-module
> baseline re-proves cleanly while the gate does not open — and it is worth stating plainly, because a
> reader could reasonably expect an authority crisis to have disturbed the model. **It did not.**

---

## 4. Tolerance-zero paths under the `EC-04` reconciliation

| Boundary | Path | State |
|---|---|---|
| `CF-I-03` `D3` cross-tenant | Inventory → Accounting handoff, element 10 authority half | **specified, not executed** |
| Privileged-bypass enumeration | authorization surface across all modules | **enumerated, not executed** |
| `SA10` tenant/company boundary matrix | SaaS tenant/company assurance | **`TOLERANCE-ZERO — HOLD`** |

**`0 of 3` closed. None reclassified. None moved into Pre-Test to open the gate.** `SC-26`.

**Cross-tenant / company leakage:** the only sanctioned cross-company means remains `MTI-22`; `SC-BD-03`
ruled `MTI-D-04` = **no cross-company grant in v1**, so `CF3-P-04` is **struck** and the isolation suite's
exception set is **empty and known**. `BD-ACC-02`'s statutory boundary is untouched on every branch.

---

## 5. Scenario classification — re-derived

| Population | Class 1 | Class 2 | **Class 3** | Total |
|---|---:|---:|---:|---:|
| 22 joint cross-proof | 10 | 12 | **0** | 22 ✓ |
| 18 end-to-end | 9 | 9 | **0** | 18 ✓ |
| 198 dimension cells | `185 C` · `13 B` · `9` statutory `S` | | **`0 G`** | |

**`0 of 22` verified · `0 of 58` invariants proven · `0 of 18` contracts proven — unchanged, and
unchangeable at Phase SA by construction.**
**`1` `NOT TRAVERSABLE`: `E2E-04`. Deliberately not re-graded** — a prior re-grade was withdrawn under
challenge and reinstating it on this executor's own specification is held for the independent reviewer.

---

## 6. Progress-bias control — run against this file

`05_` §9: *"Do not inflate progress by reclassifying unresolved items into later phases without scope
evidence."*

| Test | Result |
|---|---|
| Any item moved from Class 3 to Class 1/2 this round? | **`0`** |
| Any tolerance-zero item reclassified as non-tolerance-zero? | **`0`** |
| Any runtime obligation relabelled as specification-complete? | **`0`** |
| Any `NOT TRAVERSABLE` upgraded? | **`0`** — and the one available upgrade was **declined** |
| Any count improved by changing its unit? | **`0`** — `F5 = 6` re-derived at primary source, not re-sliced |

---

## 7. Checkpoint

> ## `CP-SA-SC-240 — CROSS-MODULE BASELINE RE-PROVEN`
> **6 of 6 routing rules hold · 22 scenarios `10/12/0`, 18 E2E `9/9/0`, both re-derived · **`SC-F-16`: the
> `FG-F-06` disposition changes `0` scenario rows — the collision is gate-level, not model-level** ·
> 3 tolerance-zero paths, `0` closed, **`0` reclassified** · 6 vetoes, `0` discharged · `0` progress-biased
> reclassifications on a five-test control · `0 of 22` verified, unchanged.**

No Evidence = No Progress. Never Skip Gate. Do not inflate progress by reclassification.
Boss remains the sole Final Approver.
