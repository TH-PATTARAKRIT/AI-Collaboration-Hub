# P01 — SUBCONTRACT PURCHASE: DEPLOYMENT REALITY

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.** Produced under an explicit **disproof** assignment.

---

## 1. VERDICT ON *"ZERO SUBCONTRACT TRANSACTIONS"*

> ### `REFINED` — and **partly CONTRADICTED**

The single estate-wide "0" merged two different things:

| Deployment | What the count actually is |
|---|---|
| `E-1`, `E-2` | **UNDEFINED — the subcontract columns do not exist there.** The modules are not installed, so there is nothing to count |
| `E-3` | **MEASURED ZERO** — 0 subcontract manufacturing orders of 163, and 0 of 55 stock movements |

> **A single "0" reported across the estate presented an *undefined* as a *measured zero* — a
> class B result published at class A.** Exactly the defect family this round exists to repair,
> found this time in a number rather than in a boundary.

---

## 2. THE CONTRADICTION INSIDE THE MEASURED ZERO

In `E-3`, where the count is genuinely zero:

> **One subcontract bill of materials exists, with one subcontractor assigned.**

So the deployment is **not merely installed** — it is **partly configured**. The statement
*"installed but not configured"* is **CONTRADICTED**; the correct statement is
**installed, minimally configured, and never transacted**.

---

## 3. THE MODULE POPULATION — VERIFIED, WITH A CAVEAT THAT MATTERS

| Item | Result |
|---|---|
| Population size | **10 verified** |
| **But** | **it is not the same 10 across series.** The series-16 deployment carries a studio-generated subcontracting module the later series do not, and lacks a subcontracting-landed-cost bridge the later series have |

- **UNIT:** one module name in the deployed registry.
- **Consequence:** *"ten subcontracting modules"* is a count of a **set that differs by series**.
  A cross-series statement about "the subcontracting family" is a statement about **two different
  families with the same name**.

---

## 4. THE CLASSIFICATION

| Deployment | Status |
|---|---|
| `E-1` | **NOT INSTALLED** |
| `E-2` (the operating one) | **NOT INSTALLED** — so subcontracting has never run where the accounting happens |
| `E-3` | **INSTALLED · MINIMALLY CONFIGURED · NOT EXERCISED** |

---

## 5. WHY THE ZERO EXISTS — THE SEVEN-WAY TEST

| Candidate | Assessment for `E-3` |
|---|---|
| No business need | plausible — `E-3` is an order-import staging database |
| Configuration incomplete | **partly** — a bill of materials and a subcontractor exist; nothing else does |
| Module unavailable | excluded |
| Workflow unreachable | **UNKNOWN — class D** |
| Data absent | **yes** — 55 stock movements in total |
| Deployment policy | **UNKNOWN — class D** |

**The most defensible reading:** `E-3` is a staging database that received orders in bulk and
never ran manufacturing. The zero is a property of that database's purpose, not of the
capability.

---

## 6. WHAT THIS DOES TO THE PRIOR FINDINGS

| Prior finding | Status |
|---|---|
| The valuation credit-split construct, verified for series 18 and gone in series 19 | **UNCHANGED** — a source finding, unaffected |
| The correction owed to P03 | **UNCHANGED and already issued** as a delta |
| *"Installed but not exercised"* | **REFINED** to *installed, minimally configured, not exercised — in one deployment; not installed in the other two* |
| Severity | **LATENT**, and now with a reachability qualifier: the operating deployment does not have the modules at all |

---

## 7. OPEN

| ID | Item | Status |
|---|---|---|
| `SUB-05` | Whether the subcontract chain can complete in `E-3` | **HOLD — RUNTIME EVIDENCE REQUIRED** |
| `SUB-06` | What the series-16 studio subcontracting module does | **class C** — its source is in the custom root now located |
| `SUB-07` | P03's response to the delta correction | **PEER DEPENDENCY OPEN** |
