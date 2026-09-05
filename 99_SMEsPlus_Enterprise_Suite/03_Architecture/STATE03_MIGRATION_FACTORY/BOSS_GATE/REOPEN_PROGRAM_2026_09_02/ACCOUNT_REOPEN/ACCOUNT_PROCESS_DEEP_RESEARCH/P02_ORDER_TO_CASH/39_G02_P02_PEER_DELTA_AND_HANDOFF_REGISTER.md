# 39 — G02-P02 PEER DELTA AND G02 ROUTING REGISTER

`LAYER 2 — AUDIT QUARANTINE.` Task **C10**. Baseline `ff8be51`.

**G02 — Sales / Revenue / Cash.** Closure sequence **P02 → P10 → P06**. Shared controls **P07 / P08 /
P09**. Final convergence **P11**.

---

## 1. Peer Delta Consumed This Round

**Material Delta only.** No unchanged peer package was re-read.

| Peer | Delta consumed | Effect on P02 |
|---|---|---|
| **P04** (Acquire-to-Retire) | The `@api.onchange` lead — a value enforced only in the form and bypassed by import/script | **Executed and did not apply** to `property_valuation` (`27` §12, `SC-15`/`SC-16`). Running it nonetheless produced `C-33`/`RE-24` and `P02-F-05c`. Their own handler is **not on this host** and was **not adopted**. |
| **P04** | `~/OCC_BACKUP` outside P02's path set; key on `database.uuid`; *"a test run only when it confirms is not a test"* | Absorbed in earlier rounds; the uuid rule is now the identity key throughout `28`/`31`. |
| **P06** (Bank-to-Reconcile) | `om_data_remove` **installed** and deletes ledger data unauthorised; the four canonical bank states are not independent | **Consumed as context, not adopted as a P02 finding.** P02's stage 9 in `36` defers the "bank confirmed" question to P06 entirely. |
| **P05** (Expense-to-Pay) | Thai WHT implemented **twice** | **Corroborated independently**: `CA-05` finds three `l10n_th_withholding_tax*` variants plus a custom `scgl_wht_control` installed in the same estate. Routed to P07, not adjudicated. |
| **P01** (Procure-to-Pay) | Deployed v19 databases lack the GRNI account and the valuation-layer table | **Independently confirmed by P02 on a disjoint instrument**: `P02-F-28c` finds `stock_valuation_layer` absent in **all four** deployed 19.0 databases. Two sessions, two methods, same structural fact. |

**Not consumed:** P03, P08, P09, P10, P11 packages were not re-read this round — **no Material Delta was
identified for P02's questions**, and re-reading unchanged peer packages is forbidden by §8/C10.
**`UNRESOLVED != ADOPTED`:** no peer's open blocker has been promoted into a P02 boundary.

---

## 2. Outbound Routing — Exact Evidence And Exact Question

### → **P10** (Time-Based / Revenue Recognition) — the next process in G02

| Item | Evidence | Exact question for P10 |
|---|---|---|
| **Billing ahead of performance dominates** | `P02-F-34b`: `iSMEs` 789 lines (16.1%) invoiced-ahead vs 47 delivered-not-invoiced; `iErpOCC` 2,564 vs 253 | Under `BP-03`, does revenue recognise on billing or on performance — and what happens to the 3,353 lines already billed ahead? |
| **Bill-and-hold** | `24` scenario 4: no hold concept; representable only as invoice-on-order | Is bill-and-hold in scope for SMEsPlus, and if so what is the recognition trigger? |
| **A v19 deployment delivering and never invoicing** | `P02-F-34c`: `BK12MAY26`, 1,201 delivered-not-invoiced, **0 matched, ever** | Is this a configuration state P10's model must tolerate? |
| **Un-invoiced balance exists in sales, not in the ledger** | `P02-F-34d`, `SF-H` | Should the obligation position (`DC-38-01`) be P10-owned or P02-owned? |

### → **P06** (Bank-to-Reconcile) — later in G02

| Item | Evidence | Exact question |
|---|---|---|
| **Multi-deduction settlement** | `CA-04`: `account_payment_multi_deduction` creates **N write-off lines** from one registration | Does the reconciliation model admit a receipt settled to arbitrary accounts at registration time? |
| **Outstanding-account separation** | `P02-F-43` as corrected: separation exists **only** in the outstanding-account configuration | Is that configuration a control or a convention? |
| **Unreconcilable outbound accounts** | `TC-16`: 11 outbound stock accounts, `reconcile = false`, two generations, two businesses | Matching is impossible in principle on these accounts — is that P06's problem or P02's? |

### → **P07** (Thailand Tax / Localisation)

| Item | Evidence | Exact question |
|---|---|---|
| **WHT implemented multiple times** | `CA-05`: 3 OCA variants + `scgl_wht_control` installed | Which is authoritative for SMEsPlus? **P02 does not decide Thai law.** |
| **Freight tax source** | `24` `N-6`/`N-7` + `CA-03` (freight never posted in a real deployment) | Is freight a taxable supply in the Thai treatment, and from which product does the tax derive? |
| **VAT support export prints the accounting date under "Invoice Date"** | earlier P02 finding | Is that acceptable statutory presentation? |

### → **P08** (Record-to-Report / Close)

| Item | Evidence | Exact question |
|---|---|---|
| **A close that does not close** | `CA-02`: cron named "close old periods" archives `date.range` rows, sets **no lock**, blocks **no** posting; skips company-specific ranges | Does P08's close model depend on any such control? |
| **Valuation ledger vs GL** | `TZ-08`: disagreement up to 9×10¹⁶, undetected; `SF-F`: 47,242 layers → 0 entries | What is the tie-out control, and what detects this? |
| **A two-year-old un-aged position** | `34` §4: oldest 2024-02-02 against a 2026-07-11 snapshot | Must the close recognise delivered-not-invoiced? |
| **Unrealised FX, warranty/return provision** | `24` scenarios 3 and 6 | Both routed; nothing automated exists to route. |

### → **P09** (Plan-to-Analyze)

| Item | Evidence | Exact question |
|---|---|---|
| Analytic route on the O2C leg | P09's own root cause (analytic dimension is schema, not data) + `CA-04` binding `analytic.mixin` into payment registration | Does an analytic dimension survive the settlement path? |

### → **P01 / P03** — counterparts only, no adjudication

| Item | Evidence |
|---|---|
| Drop-shipping displaces cost recognition entirely to the vendor bill, unlinked to the sale (`24` scenario 1) | **P01-owned.** P02 states the O2C-side absence only. |
| v19 valuation-layer absence confirmed on four deployed databases | Corroborates P01 by a **disjoint instrument**; P02 claims no purchase-side conclusion. |

### → **P11** (Final Convergence)

| Item | Status |
|---|---|
| Three scope holds — currency-rate, chart-of-accounts, intercompany execution | routed in `20`, **undecided** |
| `DC-38-01` … `DC-38-06` design candidates | `38` §3 — proposals, not decisions |
| **`C-04` Boss authorisation** | `33` — the single P02-owned item requiring a decision |
| **`BP-03`** revenue billing-vs-performance | Boss-reserved; P02 supplies measurement only |
| The invariant `ONE BUSINESS FACT → ONE CANONICAL EVENT OWNER → ONE ACCOUNTING EFFECT PATH` | `36` stage 13 shows the benchmark does not satisfy it |

---

## 3. What P02 Does **Not** Route

- Any conclusion about the **189 unreadable modules**. They are named as a gap, not routed as a finding.
- Any Thai statutory determination.
- Any peer's `UNRESOLVED` item promoted to a boundary.
- Any decision reserved to Boss under `BP-01`/`BP-02`/`BP-03`.
