# VDR_CRITICAL_AREA_RECONSTRUCTION_MATRIX.md
# Critical Areas against the reconstructed population — denominators not reconstructible

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 17.

---

## 1. The instruction and the obstacle

§23: *"Do NOT reuse Critical Area denominators blindly. Rebuild each Critical Area from the certified
Hop-0 Population."*

**The rebuild cannot be completed, for two reasons, both of which are findings:**

1. **The Hop-0 population is not certified** — two independent discovery methods corroborate 49.5% of it. Rebuilding a Critical Area denominator on an uncertified population reproduces the defect this round exists to remove.
2. **The area-mapping instrument keys on prior learning identifiers**, so it cannot map the 17,429 newly discovered entities without being rebuilt itself. It is an instrument, and no uncertified instrument may produce official coverage.

**What can be done is to test whether the prior denominators survive the reconstruction, and that is
below.**

## 2. Prior Critical Area memberships against the reconstructed Hop-0

| # | Critical Area | Prior members | Present in Hop-0 | Lost |
|---|---------------|-------------:|-----------------:|-----:|
| 1 | Financial Posting | 16 | 16 | 0 |
| 2 | Stock Ownership | 46 | 45 | 1 |
| 3 | Stock Quantity | 26 | 25 | 1 |
| 4 | Inventory Valuation | 12 | 12 | 0 |
| 5 | **Security** | 270 | 252 | **18** |
| 6 | Tenant Isolation | 0 | 0 | 0 |
| 7 | Company Isolation | 75 | 73 | 2 |
| 8 | Approval Control | 9 | 9 | 0 |
| 9 | Audit Trail | 32 | 32 | 0 |
| 10 | Identity | 61 | 59 | 2 |
| 11 | Immutability | 47 | 47 | 0 |
| 12 | **Period Close** | 16 | 13 | **3** |
| 13 | Reversal | 47 | 46 | 1 |
| 14 | Data Integrity | 251 | 251 | 0 |
| 15 | Cross-Module Financial Handoff | 4 | 4 | 0 |
| | **TOTAL** | **912** | **884** | **28** |

**96.9% of prior Critical Area memberships survive the reconstruction.** The 28 that do not fall outside
the narrower anchor rule or are of a kind the new methods do not emit; **none is evidence that a prior
member was wrong.**

## 3. What is NOT known, and it is the larger half

**How many of the 17,429 newly discovered entities belong to a Critical Area is unmeasured.**

Judged by kind, the newly discovered set is dense in exactly the classes the Critical Areas draw from:
**406 access lines, 29 record rules, 15 groups** (Security, Company Isolation) · **58 constraints**
(Data Integrity, Immutability) · **3,382 fields** (every area) · **19 server actions and 14 report
actions**, including — from the previous round's challenge — **the valuation-closing job and the
procurement scheduler**, which bear directly on Financial Posting, Inventory Valuation and Audit Trail.

> **Every Critical Area denominator in this programme is therefore a floor, not a count.** No area can
> be reported at 100% against a denominator that is known to be incomplete, and none is.

## 4. Coverage

| | |
|---|---|
| Critical Areas at 100% | **0 of 15** |
| Critical Areas whose denominator is certified | **0 of 15** |
| Required | 15 of 15 at 100%, on a certified denominator |
| | **FAIL** |

## 5. Tenant Isolation — the one area whose zero is not a measurement problem

**Zero population, and the instrument is proved able to find isolation vocabulary** — company terms
return 67, 219 and 32 hits where tenant terms return none. **The reference system has no tenant
concept.** That determination is unaffected by the population reconstruction, because a reconstruction
cannot create a concept the reference system does not have.

**It remains the single most consequential line in the programme**, and it is a design input rather than
a research gap.
