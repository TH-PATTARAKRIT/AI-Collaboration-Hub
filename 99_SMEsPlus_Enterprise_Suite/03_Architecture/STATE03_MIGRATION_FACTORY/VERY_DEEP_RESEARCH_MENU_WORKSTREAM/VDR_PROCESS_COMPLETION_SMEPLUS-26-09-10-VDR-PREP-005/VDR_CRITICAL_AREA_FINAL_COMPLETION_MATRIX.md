# VDR_CRITICAL_AREA_FINAL_COMPLETION_MATRIX.md
# Fifteen Critical Areas, per dimension

Session `[SMEPLUS-26-09-10-VDR-PREP-005]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 08.
Population **V6** · 5,074 items · 30,759 applicable cells.

---

## 1. Matrix

Per-dimension columns are the research-verified share **within that area**. A dash means the dimension
is not applicable to any item in the area.

| # | Critical Area | Pop | Cells | Proc | Config | Opt | Runtime | Sec | XMod | Edge | **Coverage** | Gaps | Status |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 1 | Financial Posting | 16 | 118 | 100% | 0% | 0% | 75% | 0% | 0% | 100% | **26.3%** | `-01` | **INCOMPLETE** |
| 2 | Stock Ownership | 46 | 322 | — | 0% | 0% | 96% | 0% | 0% | — | **28.0%** | `-04` | **INCOMPLETE** |
| 3 | Stock Quantity | 26 | 182 | — | 0% | 0% | 92% | 0% | 0% | — | **27.5%** | — | **INCOMPLETE** |
| 4 | Inventory Valuation | 12 | 90 | 100% | 0% | 0% | 58% | 0% | 0% | 100% | **24.4%** | `-01` | **INCOMPLETE** |
| 5 | Security | 270 | 898 | — | 0% | 0% | 32% | 0% | — | — | **9.7%** | `-02` `-03` | **INCOMPLETE** |
| 6 | Tenant Isolation | **0** | 0 | — | — | — | — | — | — | — | **NOT COMPUTABLE** | — | **NO REFERENCE POPULATION** |
| 7 | Company Isolation | 75 | 389 | — | 0% | 0% | 95% | 0% | 0% | — | **28.8%** | `-02` `-04` | **INCOMPLETE** |
| 8 | Approval Control | 9 | 63 | — | 0% | 0% | 44% | 0% | 0% | — | **20.6%** | — | **INCOMPLETE** |
| 9 | Audit Trail | 32 | 224 | — | 0% | 0% | 69% | 0% | 0% | — | **24.1%** | `-03` `-05` | **INCOMPLETE** |
| 10 | Identity | 61 | 393 | 100% | 0% | 0% | 87% | 0% | 0% | 100% | **26.2%** | `-06` | **INCOMPLETE** |
| 11 | Immutability | 47 | 186 | 100% | — | — | 0% | — | 0% | 100% | **41.4%** | `-05` | **INCOMPLETE** |
| 12 | Period Close | 16 | 112 | — | 0% | 0% | 88% | 0% | 0% | — | **26.8%** | — | **INCOMPLETE** |
| 13 | Reversal | 47 | 335 | 81% | 0% | 0% | 0% | 0% | 0% | 81% | **22.7%** | — | **INCOMPLETE** |
| 14 | Data Integrity | 251 | 1,629 | — | 0% | 0% | 80% | 0% | 0% | — | **27.7%** | `-05` | **INCOMPLETE** |
| 15 | Cross-Module Financial Handoff | 4 | 12 | — | — | — | 100% | — | 0% | — | **33.3%** | — | **INCOMPLETE** |

**Critical Areas at 100%: 0 of 15.** Required: 15 of 15. → **HOLD.**

**737 distinct items** mapped to at least one area; 912 memberships.

## 2. What the per-dimension columns show that a single percentage hid

Every area sits between 20% and 42%, and the *shape* is nearly identical across all fourteen populated
areas: **process and edge are high where they apply, runtime is moderate to high, and configuration,
optional function, security and cross-module are zero everywhere.**

That is not fourteen independent results. **It is one result, repeated:** four dimensions were retracted
this round because their grade was a string test over the register's own columns, and no area can rise
above the dimensions available to it.

## 3. The three areas that differ, and why

### Immutability — 41.4%, the highest
Its population is constraints and behaviours. **Process is 100% and edge is 100%**, because both have
instruments. Runtime is 0% — constraints are observed through a constraint record, and that route was
retracted this round as a shared join key.

### Reversal — 22.7%, and its own subject is now measured
**Process 81% and edge 81%.** The reverse path is established for the majority of its 47 items for the
first time: across the domain, **43 cancel paths and 23 reverse/return paths**, measured by the AST
instrument. PREP-003 published `EDGE 2/47` from a hand-written two-identity list; PREP-004 published
12.94% from an authored string. **This is the first figure in the programme that came from reading code.**

### Security — 9.7%, the lowest, and it is a measurement defect
Its 270 items are access rules, record rules and groups. **Their security dimension scores 0 of 270** —
because the standard asks *what governs this item*, and for an access-control object that question is
backwards. **The dimension's standard does not fit the class.** This is recorded as a defect in the
measurement, not as a property of the domain, and it is the clearest thing to repair next.

## 4. Tenant Isolation — unchanged and still the most consequential line

**Zero population.** The reference system has no tenant concept; its isolation axis is company. The
instrument was proved able to find isolation vocabulary — company terms return 67, 219 and 32 hits —
so the zero is a determination, not a silent failure.

**SMEsPlus is specified as multi-tenant. Its most critical isolation axis has no reference population to
learn from, compare against, or challenge.** It must be designed without the comparative evidence every
other area has.

## 5. Contribution to the disposition

§21 bars CONDITIONAL PASS while any Critical Area is below 100%. **Fourteen are below; one is not
computable.** This matrix contributes **HOLD**.
