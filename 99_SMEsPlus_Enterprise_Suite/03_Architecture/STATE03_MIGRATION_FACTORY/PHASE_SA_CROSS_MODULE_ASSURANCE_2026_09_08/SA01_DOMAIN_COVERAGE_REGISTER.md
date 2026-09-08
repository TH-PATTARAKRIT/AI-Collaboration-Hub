# SA01 — DOMAIN COVERAGE REGISTER
## CP-SA-10 — DOMAIN COVERAGE LOCKED

Status: **CP-SA-10 CLOSED (execution status)**
Parent: `SA00_PHASE_S_EVIDENCE_BASELINE.md`

---

## 1. Purpose

Identify every material domain SMEsPlus must assure, bind each to its Phase S evidence, and
classify the strength of that evidence. The master prompt §10 supplies an initial seventeen
work packages and requires additional packages to be created automatically where material
gaps are detected. This register does that.

---

## 2. Domain coverage classification scheme

| Class | Meaning |
|---|---|
| `EVIDENCED — OPERATIONAL + ACCOUNTING` | Phase S established both how the domain operates and its accounting consequence |
| `EVIDENCED — ACCOUNTING LENS ONLY` | The accounting consequence is established; the module's own operating semantics are not |
| `EVIDENCED — OPERATIONAL LENS ONLY` | Operating semantics established; accounting consequence not yet reconciled |
| `THIN` | Evidence exists but is insufficient to assure input/output/routing |
| `NOT EVIDENCED` | No package is subject-scoped to this domain |

No domain is classified from a single instrument. Each row cites the measured figures from
`SA00` §6/§7 and the owning evidence branch.

---

## 3. The seventeen mandated domains

| ID | Domain | Coverage class | Primary evidence (branch @ SHA) | Blobs |
|---|---|---|---|---|
| SA-D00 | Master Data / Identity / Organization / Tenant / Company | `EVIDENCED — OPERATIONAL + ACCOUNTING` | `design/inventory-multitenant-invariant-set-2026-09-04-001` @ `dcb92278`; `research/account-wave-a-mcc-2026-09-04-001` @ `78840777` | 856 |
| SA-D01 | Sales + AR | `EVIDENCED — ACCOUNTING LENS ONLY` | AR: `research/account-p02-order-to-cash-2026-09-04-001`; Sales operations: Group A @ `8b0993d8` | 297 |
| SA-D02 | Purchase + AP | `EVIDENCED — ACCOUNTING LENS ONLY` | AP: `research/account-p01-procure-to-pay-2026-09-04-001` @ `b820b29b`; Purchase operations: Group A @ `8b0993d8` | 448 |
| SA-D03 | Inventory / Warehouse / Location / Reservation / Delivery / Return | `EVIDENCED — OPERATIONAL + ACCOUNTING` | `audit/inventory-deep-research-r4-l12-2026-09-04-001` @ `fc0b1688`; `design/inventory-multitenant-invariant-set-2026-09-04-001` @ `dcb92278`; Group A @ `8b0993d8` | 1,367 |
| SA-D04 | Manufacturing / BOM / Work Center / WIP / FG / Scrap | `EVIDENCED — ACCOUNTING LENS ONLY` | `research/account-p03-manufacture-to-cost-2026-09-04-001` @ `bc767a81` | 512 |
| SA-D05 | Supply Routing — Buy / MTO / Manufacture / Dropship / Kit / Service | **`THIN`** | scattered; no subject-scoped package | **81** |
| SA-D06 | Accounting Event / GL / Journal / Posting | `EVIDENCED — OPERATIONAL + ACCOUNTING` | `corr/p08-one-prompt-final-2026-09-08-001` @ `ea78e160`; BD-ACC-01 @ `79d70278` | 612 |
| SA-D07 | Tax / VAT / WHT / Statutory | `EVIDENCED — OPERATIONAL + ACCOUNTING` | `research/account-p07-th-tax-compliance-2026-09-04-001`; BD-ACC-02 @ `79d70278` | 1,217 |
| SA-D08 | Payment / Bank / Cash / Reconciliation | `EVIDENCED — OPERATIONAL + ACCOUNTING` | `corr/p06-one-prompt-final-2026-09-08-001` @ `a533fe92` | 1,493 |
| SA-D09 | Asset / Depreciation / Disposal | `EVIDENCED — OPERATIONAL + ACCOUNTING` | asset deep L1–L6 + DR continuation; `research/account-p04-acquire-to-retire-2026-09-04-001` | 416 |
| SA-D10 | Expense / Employee Expense / Cost Recognition | `EVIDENCED — ACCOUNTING LENS ONLY` | `research/account-p05-expense-to-pay-2026-09-04-001` @ `205e0ac3` | 55 (91 subject files) |
| SA-D11 | Analytic / Dimension / Cost Control | `EVIDENCED — ACCOUNTING LENS ONLY` | `corr/p09-one-prompt-final-2026-09-08-001` @ `1d54c7e4`; Boss decision `fa57d10f` | 790 |
| SA-D12 | Period Close / Year Close / Adjustment / Reversal | `EVIDENCED — ACCOUNTING LENS ONLY` | `corr/p08-one-prompt-final-2026-09-08-001` @ `ea78e160` | 248 |
| SA-D13 | Approval / Workflow / Segregation of Duties | `EVIDENCED — OPERATIONAL LENS ONLY` | Group A @ `77e93d44` (multi-approve boundary); item **A2 evidence missing** | 1,048 |
| SA-D14 | Cross-Company / Multi-Company / Tenant Boundary | `EVIDENCED — OPERATIONAL + ACCOUNTING` | `dcb92278`; `research/account-wave-a-mcc-2026-09-04-001` @ `78840777`; BD-ACC-02 | 507 |
| SA-D15 | Audit / Traceability / Evidence / Standards | `EVIDENCED — OPERATIONAL LENS ONLY` | pervasive; **no consolidated standards map** — see `SA11` | 2,559 (saturated term) |
| SA-D16 | Cross-Domain End-to-End Reconciliation | `EVIDENCED — ACCOUNTING LENS ONLY` | `corr/p11-one-prompt-final-2026-09-08-001` @ `490ccdd8`; Group A @ `8b0993d8` file 06 | 338 |

---

## 4. Additional domains created by this register

The master prompt §10 requires additional work packages where material gaps are detected.
Five modules are the subject of **standing Boss decisions on `origin/SMEsPlus`** yet appear in
none of the seventeen mandated packages. A Boss decision creating a module boundary, with no
domain package to assure it, is a coverage gap by construction.

| ID | Domain | Boss decision creating it | Coverage class | Blobs |
|---|---|---|---|---|
| **SA-D17** | Service delivery / service order → completion evidence | `e47f0f2f` Service menu structure | **`THIN`** | 16 |
| **SA-D18** | Project (operational) ↔ Analytic Accounting boundary | `fa57d10f` Project and Analytic Accounting boundary | **`THIN`** | 4 |
| **SA-D19** | Quality / inspection / quality hold | `4c469f8e` Quality menu naming | **`THIN`** | 20 |
| **SA-D20** | Equipment (operational) + Maintenance | `36c62ab3` Equipment vs Fixed Asset boundary; `a11c9e7b` Work Order vs Maintenance Order naming | **`THIN`** | 13 / 34 |
| **SA-D21** | Commercial policy — pricing, discount, credit control | thin-evidence finding SA00-F-01; extension points named in `02_BOSS_DECISION_CORE_EXTENSION_BOUNDARY` | **`THIN`** | 18 / 16 |

### 4.1 Instrument contrast (the classification is measured, not assumed)

The same instrument, same corpus, same unit (unique text blob), run against domains known to
be well evidenced, returns figures an order of magnitude larger:

| Domain measured | Blobs |
|---|---|
| Tax (control — known deep) | 1,216 |
| Manufacturing BOM / work center (control — known present) | 154 |
| Maintenance | 34 |
| Quality | 20 |
| Service delivery | 16 |
| Equipment (operational) | 13 |
| Project (operational) | **4** |

**SA01-F-01.** ~~Five modules … are evidenced between 4 and 34 blobs, against 154–1,216 for domains
of comparable architectural weight.~~

> ### SUPERSEDED BY CORR2 — `SA_CORR2_03` §2 (`C2-F-07`, `C2-F-08`)
>
> **The figures in §3, §4 and §4.1 of this register were produced by an undeclared instrument.**
> `SA00` §6 states the rule — *"MENTION = blob contains any **declared** term"* — and **no term is
> declared anywhere in the package**; §7 gives prose labels, which are descriptions of a search, not
> a search. The counts are therefore **not reproducible**, and CORR2 could not reproduce any of them.
>
> Re-measured over a corpus 1.39× larger, **with the pattern published and executed**, and with two
> known-deep control domains run through the identical instrument:
>
> | Domain | here | CORR2 | controls |
> |---|---|---|---|
> | SA-D05 supply routing | 81 | **343** | Tax **777** |
> | SA-D17 service | 16 | **273** | Inventory **730** |
> | SA-D18 project / analytic | 4 | **331** | |
> | SA-D19 quality | 20 | **69** | |
> | SA-D20 equipment / maintenance | 13 / 34 | **349** | |
> | SA-D21 commercial policy | 18 / 16 | **195** | |
>
> The contrast this finding rests on — *an order of magnitude* — becomes **2.1× to 11.3×**. Four of
> the six sit within 2.2×–4.1× of a domain this register calls deep. **Only `SA-D19` Quality survives
> as genuinely thin**, and even there the figure is 69, not 20.
>
> **`SA00` §6 stated the correct caveat** — *"MENTION is a **floor**, not a coverage measure"* — and
> this register used the floor as a coverage measure. **The caveat travelled one file and died.**
>
> The creation of `SA-D17`…`SA-D21` as domains **stands**: Boss boundary decisions with no domain
> package is a real coverage gap. Only their `THIN` classification is superseded.

---

## 5. Coverage summary

| Class | Domains | Count |
|---|---|---|
| `EVIDENCED — OPERATIONAL + ACCOUNTING` | D00, D03, D06, D07, D08, D09, D14 | 7 |
| `EVIDENCED — ACCOUNTING LENS ONLY` | D01, D02, D04, D10, D11, D12, D16 | 7 |
| `EVIDENCED — OPERATIONAL LENS ONLY` | D13, D15 | 2 |
| `THIN` | D05, D17, D18, D19, D20, D21 | 6 |
| `NOT EVIDENCED` | — | 0 |
| **Total domains** | | **22** |

No domain is `NOT EVIDENCED`. Every domain has at least some locatable evidence — a negative
claim of total absence would not survive the search, and none is made.

### 5.1 The shape of the gap

Seven of twenty-two domains are assured on both lenses. Seven more are understood only
through their accounting consequence — SMEsPlus knows what a sale *posts*, less about how a
sale is *taken*. Six are thin, and four of those six (D17, D18, D19, D20) exist only because
Boss has already ruled on their boundary.

**This is the central Phase SA condition: SMEsPlus can currently prove what its transactions
mean to the ledger far better than it can prove how those transactions arise, route and
interlock.** Cross-module assurance is precisely the property the evidence base is weakest on.

---

## 6. Domain-to-checkpoint routing

| Domain class | Routed to |
|---|---|
| `EVIDENCED — OPERATIONAL + ACCOUNTING` | full SA02–SA10 treatment |
| `EVIDENCED — ACCOUNTING LENS ONLY` | SA02 input register carries an explicit `INPUT-EVIDENCE-INSUFFICIENT` where the operating semantic is required for routing |
| `EVIDENCED — OPERATIONAL LENS ONLY` | SA07 accounting reconciliation carries the open item |
| `THIN` | `SA16_TARGETED_VERY_DEEP_RESEARCH_REGISTER.md` — targeted re-entry trigger raised |

---

`CP-SA-10 — CLOSED (execution status)`: all material domains are identified and bound to
evidence. This is not a statement that the domains are assured. Six are thin and are routed to
targeted Very Deep Research.

Boss remains the sole Final Approver.

---

## 7. Corrections applied to this register

A correction is applied to the register text itself, by population. Recording it in a log
while leaving the claim standing would be a false assurance.

| # | Correction | How found | Verification |
|---|---|---|---|
| SA01-C-01 | The Inventory R4 L1–L12 execution package was cited to `prompt/inventory-deep-research-r4-l12-2026-09-04-001`. It is not there. The package is on **`audit/inventory-deep-research-r4-l12-2026-09-04-001` @ `fc0b1688`**, 26 files. | SMEs Core inventory-domain extraction | Re-verified independently before adopting: the `prompt/` branch carries 1,109 files and **0** matching `R4_L12` by any pattern; the `audit/` branch carries **26** under `DEEP_RESEARCH_R4_L12_EXECUTION/`. The listing command is the same on both, so the zero is a measured absence |
| SA01-C-02 | The multi-tenant invariant set was referred to by a single figure. There are **two live totals**: **50** at R1 (`dcb92278`) and **58** at R2 conformed (`bd096ffa`, 50 carried + 8 added, 14 re-specified). | SMEs Core inventory-domain extraction | Both status lines quoted in `SA10` |

**Population scope of SA01-C-01:** the whole package was searched for the wrong branch string,
not only the row where it was noticed. Occurrences before: 1. After: 0.
