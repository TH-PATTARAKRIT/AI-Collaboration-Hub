# AI06 — P09_ANALYTIC_RUNTIME_TRUTH_MATRIX

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Layer:** 1 — clean-room.

---

## 1. THE FOUR TRUTHS THE DIRECTIVE ASKS TO BE COMPARED

| Truth | Definition | Available to this session? |
|---|---|---|
| **UI truth** | what a user sees on screen | **NO** — no running system |
| **Stored truth** | what is in the database | **PARTIAL** — two real dumps located, neither containing the relevant rows |
| **Runtime truth** | what the code does when it executes | **NO execution.** Source-derived only |
| **Report truth** | what a management report presents | **derived from source**, not observed |

## 2. THE MATRIX — AND ITS HONEST STATE

| Comparison | Result | Class |
|---|---|---|
| UI truth vs stored truth | **NOT DECIDABLE** — no runtime access | HOLD |
| stored truth vs runtime truth | **NOT DECIDABLE** — no deployment contains a depreciation entry carrying an allocation (`AI05` §2) | HOLD |
| runtime truth vs report truth | **derived from source and internally consistent**: the algebra produces two mirror records; the surfaces then diverge by whether they bucket on the general account (`AI04` §3) | SUPPORTED INTERPRETATION |
| report truth vs report truth | **the divergence is itself established from source**: budget consumption and the profit-and-loss analytic column show the full cost; the analytic balance shows zero; project profitability shows nothing | FACT VERIFIED (source) |

## 3. WHY NO RUNTIME EVIDENCE WAS PRODUCED

Two independent reasons, both recorded rather than glossed:

1. **No running deployment is reachable from this session.** A full-volume sweep found no live database connection, no configured connection parameters usable read-only, and no running server.
2. **Creating a transaction to observe the behaviour is prohibited.** The continuation directive permits read-only runtime investigation only, and states that where write execution is required and no explicit authority exists, the session must not write. **Reproducing this defect requires posting a depreciation entry on an asset carrying an allocation — a write.** No such authority exists.

**Recorded as: `HOLD — RUNTIME WRITE AUTHORIZATION REQUIRED`** for any reproduction, and **`HOLD — RUNTIME EVIDENCE REQUIRED`** for observation of an existing case.

## 4. WHAT THIS COSTS THE CONCLUSION — AND WHAT IT DOES NOT

**It does not weaken the algebra.** `AI02` Corollary 1 is arithmetic over a source-stated formula and the double-entry invariant. A proof does not require a witness, and no runtime observation could make `+X` and `−X` sum to something other than zero.

**It does weaken three things**, and each is stated rather than absorbed:

| Weakened | Why | Where routed |
|---|---|---|
| the **incidence** claim | no deployment observed carrying the precondition | `DEP-P09-14` |
| the **surface divergence** claim | derived from reading each report's filter, not from running the reports | `DEP-P09-15` |
| the **accrued-orders residue** magnitude | requires real tax ratios | `SW-U-03` |

## 5. THE CHEAPEST PATH TO CLOSING THIS

Stated concretely so it is actionable rather than aspirational:

1. **Re-run the existing asset trace with the allocation field added to its field list.** A prior session already captured 280 asset records read-only through an existing script; adding one field name to that script's selection closes the incidence question for that deployment at near-zero cost and with no write.
2. **Read-only query access** to any deployment with posted depreciation, to count symmetric pairs directly.
3. **A sandbox reproduction** — but this requires write authority that does not exist and must be granted explicitly.

Items 1 and 2 are **read-only** and within the directive's permission. Item 3 is not.

## 6. CHECKPOINT

**CP-AI06 — RUNTIME / REPORT TRUTH RECONCILED TO THE EXTENT PERMITTED.** Runtime truth: **HOLD**. Report truth: source-derived and internally consistent. Auto-continue.
