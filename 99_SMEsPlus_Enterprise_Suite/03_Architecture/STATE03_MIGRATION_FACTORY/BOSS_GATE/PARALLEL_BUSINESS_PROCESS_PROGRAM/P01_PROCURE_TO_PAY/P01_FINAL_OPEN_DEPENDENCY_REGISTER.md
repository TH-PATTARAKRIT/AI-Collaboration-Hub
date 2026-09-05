# P01 — FINAL OPEN DEPENDENCY REGISTER (AT RESEARCH-SCOPE FREEZE)

Session: `SMEPLUS-26-09-05-G01-P01-P2P-CONTROLLED-SCOPE-FREEZE-HANDOFF-001` · Baseline `a02ec8b`

**Every open item has a named owner and an exact next action.** Nothing is parked without one.

| ID | Item | Class | Owner | Exact next action | Blocks |
|---|---|---|---|---|---|
| `S16-B-05` | `ON DELETE SET NULL` + installed `om_data_remove` reproduce the "0 of N linked" signature published for series 18 and 19 | **EVIDENCE INTEGRITY — highest ranked** | **P06 + P11** | Three tests in the s18/s19 deployments — `P01_TO_P11_HANDOFF.md §6` | Reliance on two earlier rounds' zero-link findings |
| `S16-B-01` | Price differences capitalised into inventory; no P&L variance line observed | ACCOUNTING POLICY | **P08** → Boss | Decide treatment; confirm no other P&L route | — |
| `S16-B-02` | Advance → bill deduction lineage unmeasured; P05 disagreement preserved | EVIDENCE | **P01 + P05** | Join 22,468 payments to 447,384 items via the two reconcile tables (all extracted, no new evidence needed) | Vendor-advance conclusions |
| `S16-B-03` | `purchase_mrp` kit price-difference correction gap — **latent here** | CROSS-PROCESS | **P03** | `P01_TO_P03_HANDOFF.md §2.2` | P03 cost model |
| `S16-B-04` | No period lock of any kind on 169,143 posted entries | CONTROL | **P08** → Boss | Reporting/close judgement | Period-close assurance |
| `S16-C-14` | Subledger/ledger divergence ฿6,462,975,089,678,637.13; **8 posted GL items > ฿1bn**; ฿39.2m misallocated | DEFECT | **P01** (root cause) + **P08** (reporting) | Root cause is `purchase_stock/_get_price_unit`; conditions live | Inventory valuation reliability |
| `S16-C-15` | ~40–45 valuation layers genuinely unexplained (after 245 `consu` + 1,209 price-difference resolved) | EVIDENCE | **P01** | Characterise the residual rows before classifying | — |
| `S16-C-18` | Buddhist-era date extent **disputed between two experts** | EVIDENCE | **P08** | Reconcile the two enumerations, or adopt the common floor | Period-bounded reporting |
| `GAP-P01-07` | **41 of 651 tables extracted (6.3%)**, no declared selection rule | METHOD | **P01** | Declare the rule or widen extraction | Every negative in round 6 |
| `NEAR-MISS-P01-09` | Round-5/6 "freeze" declared and not enforced | PROCESS | **P01** | Content-hash the frozen set; hand the digest to challengers | Review integrity |
| `DEP-P01-01` | Deployed copy identity across the estate | EVIDENCE | **P01** | Apply `METHOD-P01-03` (registry field set) | — |
| `DEP-P01-06` | Tenant residue | EVIDENCE | **P01** | Unchanged since round 4 | — |
| — | Thai WHT / PND statutory basis — **six routed items** | **STATUTORY** | **P07** | `HOLD — STATUTORY EVIDENCE REQUIRED` | Any compliance statement |
| — | Runtime execution of the seven priority edge cases | AUTHORITY | **Boss** | `HOLD — RUNTIME WRITE AUTHORIZATION REQUIRED` | Behavioural confirmation |

## MATERIAL-DELTA TRIGGERS THAT WOULD REOPEN P01

1. `S16-B-05` returning **positive** in either the series-18 or series-19 deployment.
2. Runtime write authorization being granted.
3. Statutory authority arriving from P07 that changes a P01 classification.
4. A deployment with **kit/phantom BoM** activity entering scope (would make `S16-B-03` live).
5. Discovery of a database identity not in the current estate floor (**≥ 8 identities / ≥ 39 artefacts**, no total stated).
