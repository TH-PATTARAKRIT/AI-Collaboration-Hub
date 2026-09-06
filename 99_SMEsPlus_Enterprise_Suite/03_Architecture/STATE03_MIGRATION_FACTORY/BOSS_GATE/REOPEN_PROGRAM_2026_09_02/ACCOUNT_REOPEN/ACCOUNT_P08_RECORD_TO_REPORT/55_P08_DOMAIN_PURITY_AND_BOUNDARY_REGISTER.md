# P08_DOMAIN_PURITY_AND_BOUNDARY_REGISTER

Prompt `[SMEPLUS-26-09-06-P08-R2R-DOMAIN-PURE-BOUNDED-CLOSURE-002]` · **PHASE S**

Two jobs. **(1)** Audit the existing P08 package for material that crossed into a peer domain, and re-classify it without discarding evidence. **(2)** State, for each adjacent domain, the **minimum interface fact P08 retains** and the path P08 stops.

---

## 1. Contamination audit of the existing package

**ENUMERATION.** POPULATION: all 22 P08 artefacts written in the two prior rounds (`33`–`54`). PATTERN: case-insensitive match on eleven peer-domain lifecycle terms — petty cash, expense claim/report/sheet, purchase-order line, sales order, manufacturing, work-in-progress, depreciation method/schedule/convention, bank statement import, withholding, statutory VAT register, asset register/lifecycle/re-evaluation. PATH SET: the package directory, Layer 1 only. UNIT: **one artefact**. POSITIVE CONTROL: the pattern returns hits in 9 artefacts, so it fires; each hit was then read individually rather than counted.

**9 artefacts matched. 7 are clean on reading. 2 carry genuine contamination.**

| Artefact | Matched text | Assessment |
|---|---|---|
| `36` | peer findings on locked-period re-dating and on manufacturing cost posting | **CLEAN.** Both are recorded as **received interface facts** with ownership assigned explicitly to the peer (`PEER-OWNED`, `PEER DEPENDENCY OPEN`). P08 asserts the ledger effect, not the producer's decision |
| `41` | *withholding* and *purchase-order line* appear as **names of origin predicates carried on a journal item** | **CLEAN.** A pointer stored on the item is a ledger-boundary attribute. P08 counts them; it does not interpret them |
| `46` | a peer branch name in a listing | **CLEAN** |
| `49` | two withholding modules listed as **explicitly not searched** | **CLEAN.** A declared non-search is the opposite of contamination |
| `53`, `54` | this round's own files, citing the above | **CLEAN** |
| **`42` `B-24`** | *"The withholding figure on the vendor-facing document is recomputed from current master data, not read from the ledger."* | **CONTAMINATED.** How a withholding figure is computed is **P07**. How a vendor-facing document is produced is **P01/P05** |
| **`47` §7, two rows** | which tax groups are excluded from a statutory register, and that two statutory reporting stacks exist | **CONTAMINATED.** Which taxes belong in which statutory register is **P07** |

### 1.1 Re-classification — evidence retained, path stopped

**No evidence is discarded.** Each contaminated item is reduced to the interface fact P08 owns; the remainder is routed.

| Item | **Minimum interface fact P08 retains** | Routed |
|---|---|---|
| `42` `B-24` | **A document-producing output recomputes a monetary figure from current master data instead of reading the posted ledger.** That is a **derived output that does not agree with the ledger by construction** — a P08 output-boundary fact, and it belongs beside the three report-layer stores already recorded in `CQ-P08-08` | the tax computation → **P07**; the document → **P01/P05**. `EXTERNAL DOMAIN BOUNDARY — DO NOT RESEARCH HERE` |
| `47` §7 tax-group rows | **A statutory register output admits rows by matching a stored name against a literal, and one such query carries no company predicate.** The **literal-match fragility** and the **missing company predicate** are P08 boundary and scope facts | which taxes *ought* to appear → **P07**, and any statutory reading → `HOLD — STATUTORY EVIDENCE REQUIRED` |

**`P08-CONTRA-44`.** Two published items asserted peer-domain facts. Both are re-scoped here rather than withdrawn, because **the ledger-boundary half of each is sound and load-bearing.**

---

## 2. Boundary register — what P08 retains and where P08 stops

For each adjacent domain: the interface fact P08 keeps, and the path P08 does not walk.

| Domain | **Interface fact P08 retains** | **Path P08 STOPS** |
|---|---|---|
| **P01 Procure-to-Pay** | A purchase-side ledger effect arrives; **26.8% carry an origin pointer** — the weakest provenance of any class | why a purchase document is created, approved, matched or priced |
| **P02 Order-to-Cash** | A sale-side ledger effect arrives and is **exempt from accounting-date derivation**; 84.1% carry a pointer | revenue recognition policy, order lifecycle, delivery |
| **P03 Manufacture-to-Cost** | A valuation ledger effect arrives carrying an entry-level pointer | cost build-up, work-in-progress, routing, overhead absorption |
| **P04 Acquire-to-Retire** | An asset ledger effect arrives, commonly **bulk-generated**; a **separate asset register exists and the kernel imposes no reconciliation obligation on it** | depreciation method, convention, schedule, disposal or re-evaluation logic |
| **P05 Expense-to-Pay** | An expense ledger effect arrives; **the posting state it relies on sits outside the integrity seal** | claim lifecycle, approval, petty cash, advances |
| **P06 Bank-to-Reconcile** | A settlement instruction arrives with **an as-of date P08 does not control** — 46.4% recorded after it, 44.3% before | statement import, matching rules, bank feed behaviour |
| **P07 TH Tax Compliance** | A **tax-period stamp arrives on the entry**, is populated on 61,157 posted entries, differs from the accounting date on 5,228, and **reaches no entry's full item set**; a register output selects **without a company predicate** | which taxes belong in which register, rates, exigibility, and **every statutory question** |
| **P09 Plan-to-Analyze** | An analytic attribution rides on the item; **P08 does not decide whether it is a fact or an attribution** | analytic model, allocation, budget |
| **P10 Time-Based Recognition** | A recognition ledger effect arrives; it is **indistinguishable at the ledger from any other generated entry** | schedule generation, deferral policy |
| **P11 Core Reconciliation** | P08 supplies what the ledger can and cannot offer a reconciliation — `58` | **the whole-accounting reconciliation architecture** |
| Inventory / MRP, Asset / Maintenance internals | valuation and asset effects as above | all internals |

## 3. Rules P08 applied this round

1. **P08 may prove what the ledger receives, stores, validates, posts, reverses, locks and reports.** Every row of `54` is one of those.
2. **P08 may not prove how another process decided to generate an event.** Where a producer's behaviour was needed, it is recorded as a **received interface fact, attributed, and not re-derived**.
3. **A peer's finding is not P08 evidence until P08 verifies it at the ledger boundary.** Where P08 verified (the seal field set, the raw-statement path), the row says so. Where P08 did not, the row says that instead.
4. **Statutory readings are never made.** `HOLD — STATUTORY EVIDENCE REQUIRED` throughout.

## 4. Standing

| | |
|---|---|
| Artefacts audited | **22** |
| Matched the contamination pattern | **9** |
| Clean on reading | **7** |
| **Contaminated and re-scoped** | **2** |
| Evidence discarded | **0** |
| Adjacent domains with a declared boundary | **11** |

**Disposition: `OUT OF P08 SCOPE — DOMAIN PURITY PRESERVED` for the routed halves; `FACT VERIFIED — CLOSED` for the retained interface facts.**
