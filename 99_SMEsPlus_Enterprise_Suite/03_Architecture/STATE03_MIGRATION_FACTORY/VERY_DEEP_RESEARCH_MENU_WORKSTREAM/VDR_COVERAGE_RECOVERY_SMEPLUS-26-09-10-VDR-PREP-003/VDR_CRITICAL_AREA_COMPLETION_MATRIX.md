# VDR_CRITICAL_AREA_COMPLETION_MATRIX.md
# Fifteen Critical Areas — measured completion

Session `[SMEPLUS-26-09-10-VDR-PREP-003]` · Layer: **LAYER 1 — CLEAN-ROOM.**
Denominators from the frozen population `POPULATION_V3` (5,074 items, 30,741 applicable cells).
Grades per `VDR_COVERAGE_MEASUREMENT_SPEC.md` §4.

---

## 1. Provenance of the fifteen — retrieved, not invented

§10 of the commissioning prompt states: *"DO NOT invent the fifteenth category. Retrieve it from the
canonical prior framework/evidence."*

The fifteen were read verbatim from **`VDR_COVERAGE_RULE.md` §6** in the frozen PREP-001 package. The
category that reads as "the fifteenth" is not a new one: **Identity and Immutability are two separate
entries** in the canonical list, and earlier summaries had collapsed them into one line. No category
was authored in this session.

## 2. Matrix

`Pop` = items mapped to the area (an item may map to more than one). `Cells` = applicable dimension
cells over those items. `Verified` = cells at **RESEARCH-VERIFIED**. `Unverified` = the remainder.
`Coverage %` is the RESEARCH-VERIFIED cell ratio, per §4 of the measurement spec.

| # | Critical Area | Pop | Cells | Verified | Unverified | Determined % | **Coverage %** | Function-Complete items | Open Critical Gaps | Status |
|---|---------------|----:|------:|---------:|-----------:|-------------:|---------------:|------------------------:|--------------------|--------|
| 1 | Financial Posting | 16 | 118 | 49 | 69 | 100.0% | **41.5%** | 0 | `CRITICAL-GAP-01` | **INCOMPLETE** |
| 2 | Stock Ownership | 46 | 322 | 138 | 184 | 100.0% | **42.9%** | 0 | `CRITICAL-GAP-04` | **INCOMPLETE** |
| 3 | Stock Quantity | 26 | 182 | 78 | 104 | 100.0% | **42.9%** | 0 | — | **INCOMPLETE** |
| 4 | Inventory Valuation | 12 | 90 | 37 | 53 | 100.0% | **41.1%** | 0 | `CRITICAL-GAP-01` | **INCOMPLETE** |
| 5 | Security | 270 | 898 | 540 | 358 | 100.0% | **60.1%** | 0 | `CRITICAL-GAP-02`, `-03` | **INCOMPLETE** |
| 6 | Tenant Isolation | **0** | 0 | 0 | 0 | n/a | **NOT COMPUTABLE** | 0 | — | **NO REFERENCE POPULATION** |
| 7 | Company Isolation | 75 | 389 | 191 | 198 | 100.0% | **49.1%** | 0 | `CRITICAL-GAP-02`, `-04` | **INCOMPLETE** |
| 8 | Approval Control | 9 | 63 | 27 | 36 | 100.0% | **42.9%** | 0 | — | **INCOMPLETE** |
| 9 | Audit Trail | 32 | 224 | 96 | 128 | 100.0% | **42.9%** | 0 | `CRITICAL-GAP-03`, `-05` | **INCOMPLETE** |
| 10 | Identity | 61 | 393 | 173 | 220 | 100.0% | **44.0%** | 0 | `CRITICAL-GAP-06` | **INCOMPLETE** |
| 11 | Immutability | 47 | 186 | 79 | 107 | 100.0% | **42.5%** | 0 | `CRITICAL-GAP-05` | **INCOMPLETE** |
| 12 | Period Close | 16 | 112 | 48 | 64 | 100.0% | **42.9%** | 0 | — | **INCOMPLETE** |
| 13 | Reversal | 47 | 325 | 57 | 268 | 100.0% | **17.5%** | 0 | — | **INCOMPLETE — lowest** |
| 14 | Data Integrity | 251 | 1,629 | 721 | 908 | 100.0% | **44.3%** | 0 | `CRITICAL-GAP-05` | **INCOMPLETE** |
| 15 | Cross-Module Financial Handoff | 4 | 8 | 8 | 0 | 100.0% | **100.0%** | 4 | — | **COMPLETE** |

**Critical Areas at 100%: 1 of 15.** Required by §10: **15 of 15**. → **HOLD.**

Items mapped to at least one Critical Area: **912** (union; areas overlap).

## 3. What blocks each area — the unverified dimensions, named

An area is below 100% because specific dimension cells are `DETERMINED` but not `RESEARCH-VERIFIED`.
Ratios are verified/applicable within the area.

| # | Area | Dimensions holding it below 100% |
|---|------|----------------------------------|
| 1 | Financial Posting | PROCESS 0/3 · CONFIGURATION 0/16 · OPTIONAL_FUNCTION 0/16 · RUNTIME 1/16 · SECURITY 0/16 · EDGE 0/3 |
| 2 | Stock Ownership | CONFIGURATION 0/46 · OPTIONAL_FUNCTION 0/46 · RUNTIME 0/46 · SECURITY 0/46 |
| 3 | Stock Quantity | CONFIGURATION 0/26 · OPTIONAL_FUNCTION 0/26 · RUNTIME 0/26 · SECURITY 0/26 |
| 4 | Inventory Valuation | PROCESS 0/3 · CONFIGURATION 0/12 · OPTIONAL_FUNCTION 0/12 · RUNTIME 1/12 · SECURITY 0/12 · EDGE 0/3 |
| 5 | Security | CONFIGURATION 0/44 · OPTIONAL_FUNCTION 0/44 · RUNTIME 0/270 |
| 6 | Tenant Isolation | *no population to block* — see §4 |
| 7 | Company Isolation | CONFIGURATION 0/41 · OPTIONAL_FUNCTION 0/41 · RUNTIME 0/75 · SECURITY 34/75 |
| 8 | Approval Control | CONFIGURATION 0/9 · OPTIONAL_FUNCTION 0/9 · RUNTIME 0/9 · SECURITY 0/9 |
| 9 | Audit Trail | CONFIGURATION 0/32 · OPTIONAL_FUNCTION 0/32 · RUNTIME 0/32 · SECURITY 0/32 |
| 10 | Identity | CONFIGURATION 0/61 · OPTIONAL_FUNCTION 0/49 · RUNTIME 1/61 · SECURITY 0/49 · EDGE 0/1 |
| 11 | Immutability | PROCESS 0/15 · RUNTIME 0/47 · DATA_MODEL 32/47 · CROSS_MODULE 0/15 · EDGE 0/15 |
| 12 | Period Close | CONFIGURATION 0/16 · OPTIONAL_FUNCTION 0/16 · RUNTIME 0/16 · SECURITY 0/16 |
| 13 | Reversal | PROCESS 2/37 · CONFIGURATION 0/47 · OPTIONAL_FUNCTION 0/47 · RUNTIME 0/47 · SECURITY 0/47 · **EDGE 2/47** |
| 14 | Data Integrity | CONFIGURATION 0/219 · OPTIONAL_FUNCTION 0/219 · RUNTIME 0/251 · SECURITY 0/219 |
| 15 | Cross-Module Financial Handoff | none |

**One pattern accounts for almost all of it.** `CONFIGURATION`, `OPTIONAL_FUNCTION` and `RUNTIME` are
near-zero in **thirteen of fourteen** populated areas. These three are exactly the dimensions whose
RESEARCH-VERIFIED bar requires evidence this session did not produce at scale: the OFF-vs-ON
consequence (§7), deactivation behaviour (§8), and **element-level runtime observation** rather than
module-level reachability (§9). The areas are not failing independently; they are failing on three
shared, named, measurable deficits.

Two area-specific deficits sit on top of that pattern:

- **Reversal at 17.5%** is the lowest, and it is low on its own subject matter: `EDGE 2/47`. Of the 47
  reversal elements, the reverse/cancel/return path is research-verified for **two**. An area named
  Reversal that cannot evidence its own reversal path is the single most pointed result in this matrix.
- **Immutability** shows `DATA_MODEL 32/47` — the 32 constraints are verified, the 15 behaviours are
  not; and `PROCESS 0/15` means no immutability-enforcing behaviour has its twenty facets established.

## 4. Tenant Isolation — a DETERMINED absence, not an unmeasured gap

Tenant Isolation is the one area with **zero population**, and the reason is a finding, not a
shortfall in effort:

> **The reference system has no tenant concept.** Its isolation axis is company, not tenant. A census
> across the frozen population found no element whose subject is a tenant boundary.

Under the measurement spec this is recorded as **DETERMINED = the condition is "none"**, with the
evidence being the census itself. It is **not** `N/A`: §5 of the commissioning prompt is explicit that
*"Unknown does not equal N/A"*, and this is neither — it is a measured zero.

**Consequence for SMEsPlus, stated plainly:** SMEsPlus is specified as multi-tenant. Its most critical
isolation axis therefore has **no reference population to learn from, compare against, or challenge**.
Tenant isolation cannot be derived here; it must be designed, and it must be designed without the
comparative evidence every other Critical Area enjoys. This is carried to the Boss as a decision input,
not resolved by this session.

## 5. Open Critical Gaps, per §11 — individually, with current state

| Gap | Statement (current, post-PREP-002 correction) | Areas | State |
|-----|-----------------------------------------------|-------|-------|
| `CRITICAL-GAP-01` | The valuation object was replaced between the generation most prior research used and the target generation. **The stronger form was retracted**: the ledger table is absent, but the per-movement value **is present on the movement row** — 100% of 3,680 completed movements on a transacted target-generation deployment carry one. Re-stated at MATERIAL weight | 1, 4 | **OPEN** |
| `CRITICAL-GAP-02` | Persistent objects with no row-level isolation: **13 of 47 (27.7%)** — re-stated *smaller*; the original 22 of 47 was wrong, and the four core movement objects it named as unisolated are in fact company-scoped | 5, 7 | **OPEN at corrected magnitude** |
| `CRITICAL-GAP-03` | The counting screen applies a role-dependent record filter — as a **visible, removable search facet**, not a silent injection. Re-graded **CRITICAL → MATERIAL** | 5, 9 | **OPEN as MATERIAL** |
| `CRITICAL-GAP-04` | **16** record rules admit company-less records, now including lot/serial numbers and movement lines; a shipped transit location is cross-company visible, cross-company editable and valued by no company | 2, 7 | **OPEN — strengthened** |
| `CRITICAL-GAP-05` | Opening a menu mutates data in **4 of 9** cases; one runs the full procurement scheduler as superuser with intermediate commits; the maintenance routine runs raw SQL outside the object layer, table-wide and cross-company; the switch said to suppress it guards **2 of its 5** call sites and is itself undeclared. **Now LIVE on a transacted deployment** | 9, 11, 14 | **OPEN** |
| `CRITICAL-GAP-06` | The reference object — 2nd most populated in the domain, joining **91% of movements and 99.9% of sales orders** — has no controls, no validations, no behaviours and no record rule, and is reachable only through a technical-only group. Covered by **no** prior research | 10 | **OPEN** |

**Six of six remain open.** §11 requires each to be closed individually with evidence. None met that bar
in this session. Three moved — `-01` retracted-and-re-stated, `-02` corrected downward, `-03`
re-graded — and every movement is recorded with its lineage preserved, per §17 of PREP-002.

## 6. Challenge result

Left deliberately unfilled at the time of writing. Per §15 the review package is frozen before SMEs
Core opens its challenge, and **`GOV-01` must not recur** — no mutation of this file while reviewers
hold it. Challenge outcomes are recorded in `SMES_CORE_PREP003_CHALLENGE_REPORT.md` against the frozen
SHA, and any correction they force invalidates this round and creates a new baseline rather than
editing this table in place.

## 7. Disposition contribution

§21 bars CONDITIONAL PASS while any Critical Area is below 100%. **Fourteen are.** This matrix
contributes **HOLD**, and no reading of it supports anything else.
