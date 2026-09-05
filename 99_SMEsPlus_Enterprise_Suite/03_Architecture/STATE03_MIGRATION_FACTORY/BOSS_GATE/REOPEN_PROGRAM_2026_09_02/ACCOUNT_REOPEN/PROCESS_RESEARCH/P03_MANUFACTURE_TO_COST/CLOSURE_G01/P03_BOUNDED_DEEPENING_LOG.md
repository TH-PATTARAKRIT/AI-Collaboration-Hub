# P03 — BOUNDED DEEPENING LOG

**LAYER 2 — AUDIT QUARANTINE.** Every material search logged **before** execution, per §9.
**Closure became deeper. It did not become wider.**

---

## 1. Search log

| # | CQ | Purpose | Population / boundary | Unit | Stop condition | Result |
|---|---|---|---|---|---|---|
| S-01 | pre | Verify baseline and remote parity | P03 branch only | one commit | HEAD verified | Remote had advanced `7fca09a`→`0a50717`; fast-forwarded |
| S-02 | CQ-01 | Locate + consume the P01 authoritative handoff | P01 tree **at `b820b29` only** | one file | handoff read | 2 P03-directed handoffs; supersession checked |
| S-03 | CQ-10 | Establish the deployed series | `ir_module_module` in the `iSMEs` dump | one module row | series established | **series 16** — `MD-01` |
| S-04 | CQ-10 | Locate a series-16 addons root | `/Volumes/*` + `$HOME` less `~/Library`, `-name odoo-16.0+e*` then `-name purchase_mrp` | one directory | found or declared absent | **absent**; positive control fires 28× |
| S-05 | CQ-10 | Enumerate the true path set | `ls /Volumes/` | one mount | mounts enumerated | 3 mounts; `/Volumes/iMac` was **undeclared** — `MD-04` |
| S-06 | CQ-03/05/07 | Version-sensitivity of the 3 load-bearing functions | those 3 functions, in the 2 available series | one function body | each classified | both files **differ** — `MD-02` |
| S-07 | CQ-02 | Enumerate filter-chain participants | `def _get_stock_valuation_layers`, series 18 + 19 roots; and all `mrp*` | one definition | list complete | 3 / 0; **no `mrp*` participant** — `MD-03` |
| S-08 | CQ-02 | Positive control on the v19 zero | v19 root | one file / one grep | control fires | 1,427 modules; control fires; zero is real |
| S-09 | CQ-02 | Re-test the v19 "no selector" zero after challenge | v19 `stock_account/models/` only | one occurrence | resolved | zero real, but **mechanism moved not removed** — `CC-02` |

**Nine logged searches. Every one bounded to a named module, function, table or mount.**

## 2. Searches explicitly **not** performed

| Not done | Why |
|---|---|
| Whole-host `find` | forbidden by §9 |
| Complete `/Volumes` walk | replaced by `ls /Volumes/` + a targeted probe per mount |
| Google Drive / CloudStorage walk | no CQ requires it |
| Backup / archive census | no CQ requires it |
| Full addons-tree sweep of any series | replaced by the declared participant path |
| Re-running the kit census on the 18/19 deployments (P01's suggestion) | 10 journal entries and 32 GL lines respectively — corroborative only; recorded as a **rejected delta** |
| Full re-derivation of 15 `DC-*` against series 16 | **impossible** — no series-16 source exists. Dispositioned rather than hunted |
| Any P01, P04, P08, P11 or Inventory research programme | forbidden; all routed by handoff |

## 3. Deepening that occurred, and it stayed inside scope

| Delta | Deepened into | Stayed in scope because |
|---|---|---|
| `MD-01` | the deployed version and the availability of matching source | it is the **evidence basis** of P03's own CQs, not another process's subject |
| `MD-02` | 3 named functions, 2 trees | the minimum needed to bound MD-01's damage |
| `MD-03` | one method name across two roots | P03's own boundary question — *do we participate?* |
| `CC-01`…`CC-04` | re-reading P03's own claims | correction, not new territory |

**No delta was converted into a sweep.** The one delta that could have been — `MD-01`, whose
natural response is "go find a series-16 tree" — was **bounded to the declared path set and
then dispositioned as unavailable**, because hunting further would have been the exact
broadening §3 forbids.

## 4. Stop condition reached

Recursion stopped when every surviving challenger objection reduced to a **named unavailable
evidence item with a named owner** — `MD-01`/`MD-06` (series-16 source), `UNR-P03-10`
(migration target), `UNR-P03-18` (`ir_default` fallback) — rather than to a search that had
not been run.

> **Closure stopped because the remaining questions need evidence that does not exist here,
> not because effort ran out.**
