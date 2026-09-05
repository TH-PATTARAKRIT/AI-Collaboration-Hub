# 38 — G02-P02 BOSS POLICY / SOURCE FACT SEPARATION

`LAYER 2 — AUDIT QUARANTINE.` Task **C9**. Baseline `ff8be51`.

**Two rules govern this file.** A source fact may **not** overwrite Boss policy. A Boss policy may **not**
be labelled `FACT VERIFIED` from reference evidence. Every row below is typed accordingly.

---

## 1. BOSS-CONTROLLED — Policy. Not Derived From Evidence. Not Re-Decided Here.

| ID | Policy | Type | P02's only permitted role |
|---|---|---|---|
| **BP-01** | **Invoice Policy ≠ COGS Recognition Policy.** | `BOSS POLICY` | Keep the two separated in every deliverable. P02 has done so since `00` §3b. |
| **BP-02** | For the normal **Perpetual + Storable** SMEsPlus target, **physical delivery / stock-out is the COGS recognition trigger.** Invoice timing is separate. | `BOSS POLICY` | Report what benchmarks do; **never** present a benchmark's behaviour as a reason to weaken this. |
| **BP-03** | Revenue recognition on **billing vs performance** remains a separate open decision. | `BOSS POLICY — OPEN` | Present evidence and implications only. **P02 has measured it (`P02-F-34b`) and routed it to P10. P02 has not decided it.** |

**`P02-F-38a` — the pressure `BP-02` is under, stated so it cannot be applied silently.** The benchmark
generation SMEsPlus targets, **19.0, recognises cost at invoice and labels that option "Perpetual (at
invoicing)"**, with the option defaulting to `periodic`. So on v19 the Boss target — cost at delivery —
**is not selectable through the standard setting at all**. This is a **`SOURCE FACT`**, and it is
recorded as a **constraint the design must overcome**, not as a reason to change `BP-02`. Deciding
otherwise is a Boss act.

---

## 2. SOURCE / DEPLOYMENT FACT — What Each Generation And Deployment Actually Does

| ID | Fact | Class | Evidence |
|---|---|---|---|
| SF-A | v18 recognises cost at **invoice post**, gated on `res_company.anglo_saxon_accounting`; entry credits an **interim** account | `STANDARD SOURCE FACT` (v18) | `EV-P02-102` ff. |
| SF-B | v19 **deletes** `stock.valuation.layer`, removes the anglo gate, credits **stock valuation directly**, relabels the option **"Perpetual (at invoicing)"**, defaults `periodic` | `STANDARD SOURCE FACT` (v19) | `EV-P02-112` ff.; **`P02-F-28c`: table absent in all four deployed 19.0 databases** |
| SF-C | v18 has a **one-directional** `@api.constrains` requiring the three stock accounts when `property_valuation='real_time'`; **v19 has no such guard** | `STANDARD SOURCE FACT` | `EV-P02-045`, `EV-P02-118`; `C-33` |
| SF-D | On a fresh v18 Thai install, `anglo_saxon_accounting = false` on all four companies; `property_valuation` defaults **globally** to `manual_periodic`; the two stock-account defaults are `false`; no default exists for the valuation account | **`DEPLOYED BEHAVIOUR VERIFIED`** (runtime, read-only) | `P02-F-33b/c/d` |
| SF-E | **`display_type='cogs'` occurs zero times in 17 databases / 4 generations / 2,553,914 journal lines**, every zero injection-controlled | **`DEPLOYED REALITY`** | `EV-P02-123` |
| SF-F | `551ab874`: **47,242 valuation layers, 0 carrying an accounting entry**, against a spread reaching 100% | **`DEPLOYED REALITY`** | `EV-P02-125` |
| SF-G | Delivered-not-invoiced: **3,593 lines across 5 databases / 4 generations**; in the two Thai deployments the **opposite** direction dominates (789 and 2,564 lines billed ahead of delivery) | **`DEPLOYED REALITY`** | `34` |
| SF-H | The sales subsystem **does** carry a first-class un-invoiced balance (`invoice_status`, `amount_to_invoice`, "Un-invoiced Balance"); the **ledger** carries no position and no ageing | `STANDARD SOURCE FACT` + `DEPLOYED REALITY` | `P02-F-34d` |
| SF-I | **189 P02-relevant installed modules have no readable source**, including `inherit_sales` / `inherit_inventory` on two generations, and the entire `cu_*`/`cff_*` estate of the 1.7M-line deployment | `SOURCE GAP` | `31` |

**`P02-F-38b` — the separation this file exists to protect.** `SF-A`/`SF-B` say benchmarks recognise cost
**at invoice**. `BP-02` says SMEsPlus recognises **at delivery**. **These do not conflict — they are
different kinds of statement.** The correct reading is that the benchmark cannot supply `BP-02`
off-the-shelf on 19.0, so `BP-02` becomes a **build requirement**, not a configuration choice. Any
document that reports "the reference does it at invoice" as though it settled the policy would be
committing exactly the error §9 of the prompt forbids.

---

## 3. DESIGN CANDIDATE — Proposed, Not Decided, Not Evidence

| ID | Candidate | Origin | Status |
|---|---|---|---|
| DC-38-01 | **Obligation ledger** — a first-class, ageable, scope-aware delivered-not-invoiced position with an accounting date | P02 | `DESIGN CANDIDATE`. **Not inferred from the benchmark**, which has none (`SF-H`). Strengthened by `34` §4: positions up to **2 years 5 months** old, un-aged. |
| DC-38-02 | **Event identity** — one business fact → one canonical event owner → one accounting effect path | P02 invariant | `DESIGN CANDIDATE`. Stage 13 of `36` shows the benchmark has none. |
| DC-38-03 | **Two-date model** — occurrence date and accounting date as distinct, both mandatory | P02 | `DESIGN CANDIDATE`. `36` §2 shows the benchmark carries one or the other, never both, and the join stage has never run. |
| DC-38-04 | **Close-means-closed** | P02 | `DESIGN CANDIDATE`. `CA-02` shows a deployed module that *appears* to close periods and sets no lock. |
| DC-38-05 | **Deterministic account derivation** | P02 | `DESIGN CANDIDATE`. Supported by cost-of-sales reaching **Revenue** via journal default, and by `TC-16` (`reconcile=false` on 11 outbound stock accounts). |
| DC-38-06 | **Scope-aware resolution: missing scope = DENY** | `CORR1` | `DESIGN CANDIDATE`. `CA-01` is the nearest real implementation and defaults to *global = allowed*; it implements *conflict = deny*. |

---

## 4. UNRESOLVED — Named, Owned, Not Decided

| ID | Question | Owner | Why it is not P02's to close |
|---|---|---|---|
| U-1 | Revenue on billing vs performance | **Boss / P10** | `BP-03` reserves it. P02 supplies `SF-G`. |
| U-2 | Thai VAT / WHT statutory treatment | **P07** | Statutory. P02 records module presence only (`CA-05`). |
| U-3 | Currency-rate scope; chart-of-accounts scope; intercompany execution scope | **P11** | Three scope holds routed in `20`, undecided. |
| U-4 | `C-04` cost-of-sales idempotency | **Boss authorisation** | `33`. Read-only routes exhausted and evidenced. |
| U-5 | Behaviour of 189 unreadable modules | **EVIDENCE REQUIRED** | No source. No conclusion drawn. |
| U-6 | Whether 14.0 enforces the 1,204 configured credit limits | **EVIDENCE REQUIRED** | `P02-F-35a`. The v18/v19 negative does not transfer. |
| U-7 | Value (not quantity) of the delivered-not-invoiced position | **EVIDENCE REQUIRED** | `34` §7. Cost basis is governed by unreadable custom code in the largest deployments. |

**No unnamed `OPEN` remains in P02's own scope.** Every item above has an owner and a closure condition.
