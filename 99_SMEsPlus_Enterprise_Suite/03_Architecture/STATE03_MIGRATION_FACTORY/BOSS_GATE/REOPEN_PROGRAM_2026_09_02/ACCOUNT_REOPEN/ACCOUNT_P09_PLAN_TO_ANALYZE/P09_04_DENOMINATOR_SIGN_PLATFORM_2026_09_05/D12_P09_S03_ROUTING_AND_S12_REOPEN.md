# D12 — P09_S03_ROUTING_COMPLETENESS, S12 SCOPE REOPEN, CROSS-COMPANY MANAGEMENT REPORTING

**Checkpoints:** `CP-P09D11`, `CP-P09D12`, `CP-P09D13` · **Layer:** 1 — clean-room.

---

## 1. `S03` ROUTING — 14 ITEMS, ROUTING COMPLETED

The prior round claimed a complete list of four. An independent sweep of the whole package found **14**. All 14 are now routed by **semantic ownership**, not convenience.

| # | Finding | Owner | Status |
|---|---|---|---|
| 1 | v18 template mistypes two accumulated-depreciation accounts | P08 semantics · P04 mapping | routed |
| 2 | **the v19 template already fixes it** | P04 · P08 | routed — supersedes #1 as a live risk |
| 3 | the localisation module is third-party authored, deployed at two major versions | **P07** | **newly routed** |
| 4 | `TH-F-02` — the divergent build's gate | **P08** owns the semantics; P09 owns only the consequence | **re-routed — P09 had kept the classification half** |
| 5 | **9 deployed code-block/type contradictions**, incl. the material one | **P08**; statutory reading **P07** | **newly routed** |
| 6 | whether any typing is a statutory misclassification | **P07** | HOLD — STATUTORY |
| 7 | Thai cost-centre / department segregation requirements | **P07** | HOLD — STATUTORY |
| 8 | whether the tenant department extension satisfies Thai practice | **P07** | **newly routed** — HOLD |
| 9 | a statutory withholding module differing across deployment copies | **P07** | HOLD |
| 10 | ten Thai-named modules carry zero management-accounting references | P07 confirmation | routed |
| 11 | cash-basis firing depends on a tax-exigibility configuration | **P07** | HOLD |
| 12 | Thai requirements bearing on budgetary control | **P07** | **newly routed** — HOLD |
| 13 | **Thai constraint on cross-company management reporting** | **P07** + **P11** | **newly routed — see §3** |
| 14 | statutory export formats outside the declared patterns | **P07** | **newly routed** — HOLD |

**5 previously unrouted items are now routed. 8 remain `HOLD — STATUTORY EVIDENCE REQUIRED`. P09 adjudicates none of them.**

## 2. `S12` — SCOPE REOPEN

**Status: `OPEN — SCOPE EVIDENCE REQUIRED`. It is NOT closed merely because it became measurable.**

| Element | State |
|---|---|
| prior finding | cross-company mirroring keeps company-less shared axis values, producing opposite-signed records in two companies on one shared object |
| **prior stated cause** | "partial by the inter-company margin" — **CONTRADICTED**: price and quantity are preserved exactly on the mirror |
| **correct drivers** | company-currency divergence; tax-inclusion policy being a company-level setting; per-tax analytic flags differing after fiscal-position remap; wholesale drop of composite keys; the receiving company's own defaults; and draft-state automation |
| incidence, measured | **0 of 5 deployments carry all three preconditions; 2 of 5 carry two of three** — both with inter-company installed, one holding three company-less axis values |
| **required scope evidence to close** | a deployment with ≥2 companies, inter-company enabled, **and** a company-less axis value in a mirrored allocation |

**Why it stays open:** the mechanism is verified, the cause statement is now correct, and the incidence is zero — but **zero incidence across five databases is not evidence of impossibility**, and one configuration act arms it.

## 3. CROSS-COMPANY MANAGEMENT REPORTING — THE COUPLING

Item 13 couples directly to `S12`, which is why leaving it unrouted mattered.

| Concern | Scope |
|---|---|
| the analysis axis | **TENANT** — the axis object carries no company at all |
| the axis **value** | TENANT where company-less; COMPANY where company-set |
| the journal rows | **COMPANY** |
| the management records | **COMPANY** — each inherits its own posting company |
| **the aggregate over them** | **TENANT** — and this is the unguarded step |

**The separation the directive asks for:**

| | Verdict |
|---|---|
| **cross-company management REPORTING** | **structurally reachable and unguarded.** The balance surface admits company-less records into every company's view and converts at the reading date |
| **cross-company financial MUTATION** | **not found.** Each company's ledger is correct and untouched; no financial effect crosses |

> **The exposure is a reporting and aggregation exposure, not a financial-integrity one.** That distinction matters for severity and P09 states it explicitly.

**Whether a Thai statutory constraint bears on cross-company management reporting is `HOLD — STATUTORY EVIDENCE REQUIRED`, routed to P07, and coupled to `S12` for P11.**

## CHECKPOINT
**`CP-P09D11`, `CP-P09D12`, `CP-P09D13` — COMPLETE — EVIDENCE VERIFIED.** Auto-continue.
