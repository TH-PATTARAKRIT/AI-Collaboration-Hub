# P01 — FINAL OPEN DEPENDENCY REGISTER (AT RESEARCH-SCOPE FREEZE)

Session: `SMEPLUS-26-09-05-G01-P01-P2P-CONTROLLED-SCOPE-FREEZE-HANDOFF-001` · Baseline `a02ec8b`

**Every open item has a named owner and an exact next action.** Nothing is parked without one.

| ID | Item | Class | Owner | Exact next action | Blocks |
|---|---|---|---|---|---|
| `S16-B-05` | `ON DELETE SET NULL` + installed `om_data_remove` reproduce the "0 of N linked" signature published for series 18 and 19 | **EVIDENCE INTEGRITY — highest ranked** | **P06 + P11** | Three tests in the s18/s19 deployments — `P01_TO_P11_HANDOFF.md §6` | Reliance on two earlier rounds' zero-link findings |
| `S16-B-01` | Price differences capitalised into inventory; no P&L variance line observed | ACCOUNTING POLICY | **P08** → Boss | Decide treatment; confirm no other P&L route | — |
| `S16-B-02` | Advance → bill deduction lineage unmeasured; P05 disagreement preserved. **Narrowed:** the exposure is **immaterial here** — 9 posted unreconciled non-internal supplier payments, −฿1,534,955.07, against 14,258 reconciled | EVIDENCE | **P01 + P05** | Lineage join remains available; **no round warranted on materiality grounds** | Vendor-advance conclusions |
| `S16-B-03` | `purchase_mrp` kit price-difference correction gap — **latent here** | CROSS-PROCESS | **P03** | `P01_TO_P03_HANDOFF.md §2.2` | P03 cost model |
| `S16-B-04` | No period lock of any kind on 169,143 posted entries | CONTROL | **P08** → Boss | Reporting/close judgement | Period-close assurance |
| `S16-C-14` | Subledger/ledger divergence ฿6,462,975,089,678,637.13; **8 posted GL items > ฿1bn**; ฿39.2m misallocated | DEFECT | **P01** (root cause) + **P08** (reporting) | Root cause is `purchase_stock/_get_price_unit`; conditions live | Inventory valuation reliability |
| `S16-C-15` | ~40–45 valuation layers genuinely unexplained (after 245 `consu` + 1,209 price-difference resolved) | EVIDENCE | **P01** | Characterise the residual rows before classifying | — |
| `S16-C-18` | Buddhist-era date extent **disputed between two experts** | EVIDENCE | **P08** | Reconcile the two enumerations, or adopt the common floor | Period-bounded reporting |
| **`S16-B-06`** | **The GRNI account was never decomposed by originating transaction.** Only ~45% of its gross movement is PO-driven; **51 items across 28 manual entries carry −฿1,742,591,244.82** of chart-of-accounts reclassification, unmentioned in six rounds | **MATERIAL DELTA — inside already-extracted evidence** | **P01** | (1) read the 28 reclassification entries in full — closes the account-mapping-history question `ir_property` cannot answer; (2) run the origin decomposition across the remaining 261 accounts; (3) establish the non-PO bill path and the 298 lines reaching GRNI; (4) explain the 190 done return moves with no valuation layer and the 182 GRNI items whose layer points at a non-`done` move. **No new extraction required for any of these** | Any downstream reliance on the GRNI decomposition |
| `S16-B-07` | **`mail_tracking_value` (571,522 rows) has never been opened.** Three surviving conclusions — *immutable reversal*, *no lock date*, *WHT posted after the rate was zeroed* — are claims about what happened to records over time | EVIDENCE | **P01** | Join to the 169,143 posted moves; filter Number/Date/Account/Untaxed Amount for changes dated after posting; isolate the `WHT3%` value change and read its date and author | Three C-2 claims |
| `S16-B-08` | **Scrap and inventory adjustments post into the purchase clearing account**; locations 14/16 have NULL valuation accounts (control: location 15 carries 1068/1068). **No inventory-loss account exists** — 2,257 scrap entries expense to `4010002`, indistinguishable from consumption | CONFIGURATION | **P08** + **Boss** | Configuration ruling, not research | P&L interpretation of scrap |
| `S16-B-09` | **190 of 477 done return moves produced no valuation layer**; 182 GRNI items reference a layer whose stock move is not `done` | EVIDENCE — **RISKY** | **P01** | Cause not established | Return/refund accounting |
| `GAP-P01-07` | **41 of 651 tables extracted (6.3%)**, no declared selection rule — **and it bounds affirmative claims, not only negatives** | METHOD | **P01** | Declare the rule or widen extraction | Every negative in round 6 **and** three affirmative C-2 claims |
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
4b. `S16-B-06` findings changing the composition of the GRNI account materially.
5. Discovery of a database identity not in the current estate floor (**≥ 8 identities / ≥ 39 artefacts**, no total stated).
