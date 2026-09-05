# P03 MATERIAL DELTA REGISTER — G01 BOUNDED-DEEP CLOSURE

**LAYER 2 — AUDIT QUARANTINE.** Prompt `SMEPLUS-26-09-06-G01-P03-M2C-BOUNDED-DEEP-CLOSURE-002`.
Baseline `7fca09a` · branch HEAD at intake `0a50717`.

Every delta declares: **affected CQ · why prior evidence is insufficient · exact bounded
evidence surface · expected stop condition · outcome.**

---

## MD-01 — **P03's source basis does not match the deployment**

| Field | Content |
|---|---|
| **Class** | `B — SAME-SCOPE MATERIAL CONTRADICTION` |
| **Affected CQ** | `CQ-P03-02`, `-03`, `-04`, `-05`, `-07`, `-10` — every source-based claim |
| **Trigger** | P01 final handoff names the deployment core as **series-16** `odoo-16.0+e.20230401` |
| **Why prior evidence insufficient** | P03 rounds 1–4 read **v18 Enterprise b20250608** for every code claim. The deployment carrying 9,807 MOs, 74,982 valuation layers and 447,384 GL lines is **series 16** |
| **Bounded surface** | `ir_module_module.latest_version` in the `iSMEs` dump; then `find` for a series-16 addons root across `/Volumes/*` and `$HOME` excluding `~/Library` |
| **Stop condition** | deployed series established **and** series-16 root located or declared absent |
| **Outcome** | **CONFIRMED.** `base 16.0.1.3`, `mrp 16.0.2.0`, `mrp_account 16.0.1.0`, `stock_account 16.0.1.1`, `purchase_mrp 16.0.1.0`, `purchase_stock 16.0.1.2` — all **series 16**. **No series-16 source tree exists in the declared path set.** Positive control: the search pattern fires **28 times**, all series 18 or 19 |

> **This is the `smeplus-version-basis-defect-rule` defect, in P03, for four rounds.**
> P09 read v18 while deployments ran v16 and v19; P03 did the same and did not check.

## MD-02 — **How much does the version mismatch damage the findings?**

| Field | Content |
|---|---|
| **Class** | `A — IN-SCOPE DERIVED SUBQUESTION` (derived from MD-01) |
| **Affected CQ** | `CQ-P03-03`, `-05`, `-07`, `-10` |
| **Why prior evidence insufficient** | MD-01 establishes the mismatch but not its consequence. A finding stable across series is differently exposed from one that changes |
| **Bounded surface** | The three load-bearing functions only — `_cal_price`, `_post_labour` (`mrp_account/models/mrp_production.py`) and `_cal_cost` (`mrp/models/mrp_workorder.py`) — in the two series available on this host (18, 19) |
| **Stop condition** | each function classified stable / changed between the two available series |
| **Outcome** | **BOTH FILES DIFFER 18 → 19.** Per-finding results in `P03_DEPLOYED_CODE_IDENTITY_DELTA.md` §3. `DC-04` is **fixed in v19**; `DC-07` and `DC-09` survive **verbatim**; `_cal_price`'s cost source and `_post_labour`'s counterpart account both **changed** |

## MD-03 — **Is manufacturing a participant in the valuation-layer filter chain?**

| Field | Content |
|---|---|
| **Class** | `A — IN-SCOPE DERIVED SUBQUESTION` |
| **Affected CQ** | `CQ-P03-02` |
| **Why prior evidence insufficient** | P01 enumerated the chain in series-16 and found three participants. P03 must verify that **no manufacturing module joins it**, which is P03's own boundary and not P01's to assert |
| **Bounded surface** | `def _get_stock_valuation_layers` across the series-18 and series-19 addons roots; and specifically all `mrp*` modules |
| **Stop condition** | participant list enumerated per series; `mrp*` participation established |
| **Outcome** | **Series 18: exactly 3 — `stock_account` (base), `stock_landed_costs`, `purchase_mrp` — identical to P01's series-16 set.** **Series 19: zero; `purchase_mrp/models/account_move.py` does not exist.** **No `mrp*` module defines the method in either series.** Positive control: v19 root holds 1,427 modules and `_cal_price` greps clean |

## MD-04 — **An undeclared volume in P03's path set**

| Field | Content |
|---|---|
| **Class** | `B — SAME-SCOPE MATERIAL CONTRADICTION` (evidence integrity) |
| **Affected CQ** | `CQ-P03-10` |
| **Why prior evidence insufficient** | Rounds 1–4 declared `/Volumes/iMacSys` and `~/Downloads` as the path set. `/Volumes/iMac` — a **second mounted volume with its own `/Users/admin`** — was never declared or searched |
| **Bounded surface** | `ls /Volumes/`; then the same `purchase_mrp` probe across every mount |
| **Stop condition** | every mount enumerated and probed |
| **Outcome** | **3 mounts: `iMacSys`, `iMac`, `ChatGPT Installer`.** `/Volumes/iMac` holds series 18 and 19 trees only — **no series-16 source, so MD-01 is not repaired by it.** The undeclared bound is real and is recorded; its material effect on MD-01 is **nil** |

## MD-05 — **`'version': '1.0'` cannot identify a series**

| Field | Content |
|---|---|
| **Class** | `E — NON-MATERIAL / CORROBORATIVE`, retained as a method control |
| **Affected CQ** | `CQ-P03-10` |
| **Outcome** | Every one of the located `purchase_mrp` manifests reads `'version': '1.0'`. The series comes from the **server**, which stamps `16.0.1.0` into `ir_module_module`. **The manifest is not a version discriminator**; the instrument failed and is reported as failed rather than as a result — `smeplus-scope-stated-as-description` |

## MD-06 — **P01's cited series-16 root does not resolve here**

| Field | Content |
|---|---|
| **Class** | `C — CROSS-PROCESS` — routed to P01, **not adjudicated** |
| **Affected CQ** | `CQ-P03-02`, `-10` |
| **Outcome** | P01 cites `…/16 ODOO 16 ENTERPRISE/odoo-16.0+e.20230401/odoo/addons`. **That path does not resolve within P03's declared path set** (3 mounts + `$HOME` less `~/Library`). P03 **does not conclude P01 is wrong** — P01 may have read it from a root not mounted in this session. Recorded as a locator that P03 could not reproduce, and routed |

---

## Deltas raised and **rejected** as non-material

| Candidate | Class | Why rejected |
|---|---|---|
| Re-run the kit census on series-18/19 deployments, as P01 suggests | `E` | The kit question is P03-owned, but the census answers *"are kits purchased"* — already answered **0** by a history-visible control in the only deployment with purchase history. Re-running it on a 10-entry and a 32-line deployment adds no material evidence |
| Sweep the custom `Odoo16/addons` root (59 modules) for cost overrides | `E` | Bounded probe showed it holds **no** core manufacturing/purchase module; P03's round-3 custom-addon sweep already covered the custom surface with a positive control |
| Full re-derivation of all 15 `DC-*` against series 16 | `C/D` | **Impossible — no series-16 source exists in the path set.** Converting MD-01 into a re-derivation would be a search that cannot terminate. Dispositioned as `UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE` instead |
| Whole-estate hunt for a series-16 tree beyond the 3 mounts | forbidden by §9 | Would be a whole-estate sweep. The declared path set is stated instead, with its bound |
