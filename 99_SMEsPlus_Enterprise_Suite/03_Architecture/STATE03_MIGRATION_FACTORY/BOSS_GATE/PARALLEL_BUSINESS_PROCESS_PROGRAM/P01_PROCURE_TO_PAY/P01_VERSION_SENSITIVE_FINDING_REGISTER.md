# P01 — VERSION-SENSITIVE FINDING REGISTER

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.**

Every material P01 finding is re-classified by the **evidence class that actually supports it**,
to stop version leakage. The estate's real shape:

| Deployment | Series | Source root in P01's path set? | Accounting history |
|---|---|---|---|
| `E-1` (two archives, one estate) | **19.0** | yes (`R3`, `R5`) | 16 journal entries |
| `E-2` | **16.0** | **NO — none at all** | **183,590 journal entries** |
| `E-3` | **19.0** | yes | 10 journal entries |
| — | 18.0 | yes (`R1`, `R2`, `R4`) | **no deployment exists** |

> **The two are disjoint: the series P01 has source for has no deployment, and the deployment
> with history has no source.** That asymmetry governs this whole register.


> ### ⚠ SUPERSEDED IN PART — `ERR-P01-23`
>
> This document states that **no deployed series-18 database exists** and that P01's source and
> deployment evidence **do not overlap on any series**. **Both are false.** A series-18
> deployment exists on this host with **4 companies, 15,522 journal entries, 47,801 valuation
> layers, and the goods-received clearing account configured**. See
> `P01_SERIES18_DEPLOYMENT_DISCOVERY.md`. **No accounting finding is withdrawn** — each remains
> bound to the database it was measured in.

---

## 1. THE REGISTER

| Finding | Evidence class | Note |
|---|---|---|
| Order confirmation creates no accounting effect | **V18 SOURCE VERIFIED** + **V19 SOURCE VERIFIED** | Cross-version invariant in source; **no deployment check** |
| Receipt valuation gated on item type and valuation mode | **V18 SOURCE VERIFIED** | v19 differs — see below |
| Receipt entry date is not the movement date | **V18 SOURCE VERIFIED**; refined for v19 | v19 removes the middle branch |
| Goods-received clearing bridge exists | **V18 SOURCE VERIFIED** | **No deployed representative anywhere** |
| Clearing account reconciled only if flagged | **V18 SOURCE VERIFIED** | as above |
| Price-difference replay engine, using audit-log ordering | **V18 SOURCE VERIFIED** | **absent in v19 source**; no v18 deployment exists to check it against |
| **v19 recognises inventory at invoicing, not at receipt** | **V19 SOURCE VERIFIED** | the product's own configuration label and bill-line rule |
| **No valuation account resolves in the v19 estate** | **V19 DEPLOYMENT VERIFIED** | `E-1`; **`E-3` not measured for this** — class C |
| Bill is the only universal accounting event | **V18 + V19 SOURCE VERIFIED** | **CROSS-VERSION INVARIANT (source only)** |
| Three-way match is advisory, not a control | **V18/V19 SOURCE VERIFIED**; **installed in `E-3`** | Never observed exercised |
| Order reset-to-draft has no server-side guard | **V18 + V19 SOURCE VERIFIED** | **CROSS-VERSION INVARIANT (source only)** |
| Accounting-invoicing group holds write on the order and its lines | **V18 + V19 SOURCE VERIFIED** | as above |
| Bill↔order matching lacks a vendor clause on the reference branches | **V18 SOURCE VERIFIED** | v19 not separately re-derived — class C |
| Period lock re-dates rather than refuses | **V18/V19 SOURCE VERIFIED** | **the lock field vocabulary itself differs in series 16**, so this must be stated per series |
| Draft purchase-document dates rewritten with no lock involved | **V16 DEPLOYMENT VERIFIED** (expert-reported) | measured on the only deployment with history |
| Correction deletes derived journal items | **V18 SOURCE VERIFIED** | |
| A deletion audit record is written | **V18/V19 SOURCE VERIFIED**, **V19 DEPLOYMENT VERIFIED** (expert-reported) | **and V16 DEPLOYMENT shows zero deletions logged** |
| Cross-company auto-generation, guard cannot execute | **V19 SOURCE VERIFIED** + **V19 DEPLOYMENT VERIFIED** | `E-1`; not installed in `E-2` |
| Withholding: repeated full withholding, linear | **CUSTOM SOURCE VERIFIED** — in a copy **no deployment runs** | **DEPLOYMENT-DEPENDENT / UNVERIFIED IN ANY DEPLOYMENT** |
| PND mapping conflict between two shipped copies | **CUSTOM SOURCE VERIFIED**; deployed owner identified | Neither mapping observed governing |
| Vendor advance defaults to an expense account | **CUSTOM SOURCE VERIFIED** | Deployed product-level account unset in `E-1`; **class D** in `E-2` |
| Landed cost installed everywhere, exercised nowhere | **DEPLOYMENT VERIFIED across the estate** | usability counts under challenge |
| Referential links are `ON DELETE SET NULL` | **V16 + V19 DEPLOYMENT VERIFIED** | **CROSS-VERSION INVARIANT (deployment)** — the strongest class in this register |

---

## 2. THE FOUR CLASSES THAT MATTER MOST

### 2.1 `CROSS-VERSION INVARIANT VERIFIED` — deployment-level
Only one finding reaches this class: **the order-line links from bill lines and receipt
movements are `ON DELETE SET NULL` in both the series-16 and series-19 deployed schemas.**
Verified in deployed schemas of two different series. **This is the most durable finding in the
package.**

### 2.2 `V18 SOURCE VERIFIED`, no deployment anywhere
The **entire clearing-bridge account of procure-to-pay** — the mechanism this programme spent
three rounds tracing. It is verified in source and **cannot be verified against any running
system in this estate**.

### 2.3 `V16 DEPLOYMENT VERIFIED`, no source read
Everything measured in the only deployment with real accounting history. **P01 has read no
series-16 source**, so no v16 deployment observation can currently be traced to the code that
produced it.

### 2.4 `CUSTOM SOURCE VERIFIED`, in a copy no deployment runs
The withholding arithmetic. Verified in source; the deployed module version matches no copy in
the declared path set.

---

## 3. VERSION LEAKAGE FOUND AND STOPPED

| Leak | Correction |
|---|---|
| The clearing-bridge account was written as *"how procure-to-pay works"* | It is how **series 18** works in source, and **no deployment runs it** |
| *"the v18 bridge demonstrably operates — 57,863 linked records"* | Those are **series-16** records, and the bridge fires on 49.4% of receipts, not universally |
| Period-lock findings stated generally | The lock **field set differs by series**; a series-16 deployment has a lock field the later series do not, and lacks three the later series have |
| *"both v19 deployments show X"* | **One estate observed twice** — not two witnesses (`ERR-P01-17`) |

---

## 4. THE STRUCTURAL CONCLUSION

> ~~**P01's source analysis and P01's deployment evidence do not overlap on any series.**~~
>
> **FALSE — `ERR-P01-23`. They overlap on series 18 and 19.** A deployed series-18 system exists
> with 15,522 journal entries and the clearing account configured. The series-16 core gap stands.

Source: series 18 (primary), 19 (comparison). Deployment history: series 16.
The only bridge between them is series 19, which has 26 journal entries across two deployments.

**This is the deepest evidence-base finding in the P01 programme**, and it is a fact about the
estate, not a research defect. It cannot be repaired by more analysis of what is here. It
requires either a series-16 source root (one exists, unsearched) or a series-18/19 deployment
with real history (none exists here).

`HOLD — SOURCE EVIDENCE REQUIRED` and `HOLD — DATABASE EVIDENCE REQUIRED`, jointly.
