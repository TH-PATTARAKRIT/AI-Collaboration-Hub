# VDR_CRITICAL_AREA_COMPLETION_MATRIX.md
# Fifteen Critical Areas — measured completion · **register R2 (corrected)**

Session `[SMEPLUS-26-09-10-VDR-PREP-003]` · Layer: **LAYER 1 — CLEAN-ROOM.**
Denominators from `POPULATION_V4` — 5,074 items, **30,906** applicable cells.
Grades per `VDR_COVERAGE_MEASUREMENT_SPEC.md` §4; every cell that left a denominator is in
`VDR_EXCLUSION_REGISTER.md`.

> ### R2 correction notice — read before the table
>
> The R1 baseline of this file published **"1 of 15 Critical Areas at 100%"**. That result did not
> survive independent challenge. It existed because 180 cells the specification's own rule table marks
> applicable had been reclassified as `NA` after failing, and 90 of those were the runtime cells of the
> four items that made up the only complete area (`CH-01`, `CH-04`).
>
> **All 180 cells are restored. The corrected result is 0 of 15.** Alongside it, four dimensions whose
> grade never varied within a class have been retracted from RESEARCH-VERIFIED to DETERMINED (`CH-03`),
> because a class label is not a depth measurement.
>
> **This round did not improve on PREP-002's 0 of 15.** The R1 figures are preserved in the git history
> as audit lineage; they are not the figures of record.

---

## 1. Provenance of the fifteen — retrieved, not invented

§10 of the commissioning prompt states: *"DO NOT invent the fifteenth category. Retrieve it from the
canonical prior framework/evidence."*

The fifteen were read from **`VDR_COVERAGE_RULE.md` §6** in the frozen PREP-001 package. What reads as
"the fifteenth" is not new: **Identity and Immutability are two separate entries** there, and earlier
summaries had collapsed them. Independently verified during the challenge round: the fifteen match
**name-for-name and in identical order**. Nothing was authored here.

**One modality was not carried and is restored:** the canonical heading reads *"Critical Areas
(**minimum set**)"* — fifteen is a **floor**, and a domain may add to it. The Inventory domain has not
been assessed for additions (`CH-27`).

## 2. Matrix

`Pop` = items mapped to the area. `Cells` = applicable dimension cells over those items.
`Verified` = cells at RESEARCH-VERIFIED. `Coverage %` is the RESEARCH-VERIFIED cell ratio.

| # | Critical Area | Pop | Cells | Verified | Unverified | Determined % | **Coverage %** | Open Critical Gaps | Status |
|---|---------------|----:|------:|---------:|-----------:|-------------:|---------------:|--------------------|--------|
| 1 | Financial Posting | 16 | 118 | 1 | 117 | 100.0% | **0.8%** | `CRITICAL-GAP-01` | **INCOMPLETE** |
| 2 | Stock Ownership | 46 | 322 | 0 | 322 | 100.0% | **0.0%** | `CRITICAL-GAP-04` | **INCOMPLETE** |
| 3 | Stock Quantity | 26 | 182 | 0 | 182 | 100.0% | **0.0%** | — | **INCOMPLETE** |
| 4 | Inventory Valuation | 12 | 90 | 1 | 89 | 100.0% | **1.1%** | `CRITICAL-GAP-01` | **INCOMPLETE** |
| 5 | Security | 270 | 898 | 0 | 898 | 100.0% | **0.0%** | `CRITICAL-GAP-02`, `-03` | **INCOMPLETE** |
| 6 | Tenant Isolation | **0** | 0 | 0 | 0 | n/a | **NOT COMPUTABLE** | — | **NO REFERENCE POPULATION** |
| 7 | Company Isolation | 75 | 389 | 0 | 389 | 100.0% | **0.0%** | `CRITICAL-GAP-02`, `-04` | **INCOMPLETE** |
| 8 | Approval Control | 9 | 63 | 0 | 63 | 100.0% | **0.0%** | — | **INCOMPLETE** |
| 9 | Audit Trail | 32 | 224 | 0 | 224 | 100.0% | **0.0%** | `CRITICAL-GAP-03`, `-05` | **INCOMPLETE** |
| 10 | Identity | 61 | 393 | 1 | 392 | 100.0% | **0.3%** | `CRITICAL-GAP-06` | **INCOMPLETE** |
| 11 | Immutability | 47 | 186 | 0 | 186 | 100.0% | **0.0%** | `CRITICAL-GAP-05` | **INCOMPLETE** |
| 12 | Period Close | 16 | 112 | 0 | 112 | 100.0% | **0.0%** | — | **INCOMPLETE** |
| 13 | Reversal | 47 | 335 | 0 | 335 | 100.0% | **0.0%** | — | **INCOMPLETE** |
| 14 | Data Integrity | 251 | 1,629 | 0 | 1,629 | 100.0% | **0.0%** | `CRITICAL-GAP-05` | **INCOMPLETE** |
| 15 | Cross-Module Financial Handoff | 4 | 12 | 0 | 12 | 66.7% | **0.0%** | — | **INCOMPLETE** |

**Critical Areas at 100%: 0 of 15.** Required by §10: 15 of 15. → **HOLD.**

**Function-Complete (research-complete) items: 0, in every area including area 15.**

**Membership:** **737 distinct items** are mapped to at least one Critical Area; **912 area-memberships**
in total, because 175 memberships are second or later mappings of an item already counted. The R1 text
labelled 912 a union — it is the sum (`CH-08`).

## 3. Why every area is at or near zero

Under R1 the areas sat around 42%. Almost all of that was `SOURCE`, `DATA_MODEL`, `CROSS_MODULE` and
`SECURITY` — four dimensions whose RESEARCH-VERIFIED grade **never varied within a class**, so every
item of an eligible class received it and no item could fail. `SOURCE` alone was an unconditional
literal supplying 53.5% of all verified cells. Those four are now graded **DETERMINED**, which is what
they are.

What remains verified is what a per-item predicate actually decided:

| Dimension | Research-verified | of applicable | What the grade required |
|-----------|------------------:|--------------:|-------------------------|
| `RUNTIME` | **77** | 5,071 | the element observed on a deployment — not its module inferred |
| `CONFIGURATION` | **7** | 4,109 | the OFF-vs-ON consequence traced across nine axes |
| `OPTIONAL_FUNCTION` | **7** | 4,097 | thirteen attributes including deactivation behaviour |
| `PROCESS` · `SOURCE` · `DATA_MODEL` · `SECURITY` · `CROSS_MODULE` · `EDGE` | **0** | | see §4 |
| **All cells** | **91** | **30,906** | **0.29%** |

The three areas above zero are above it by a single runtime observation each.

## 4. The six dimensions now at zero, and why

| Dimension | R1 published | Why it is zero |
|-----------|-------------:|----------------|
| `SOURCE` | 5,074 (100%) | the predicate was `v='VERIFIED'` with no condition — it could not return anything else. 186 of its "reproducible pointers" resolve to no file; 2,159 carry no line (`CH-03`) |
| `DATA_MODEL` | 1,986 (69.4%) | constant within every eligible class; the evidence field is empty on all 1,986 |
| `CROSS_MODULE` | 2,032 (69.9%) | constant within every eligible class |
| `SECURITY` | 270 (6.7%) | **inverted.** The 270 graded verified are the security objects themselves, with an empty condition field; the 3,788 items carrying the actual enumeration were graded not-verified. The Security area's population *is* the set that defined its own verified cells |
| `EDGE` | 2 (0.17%) | a hand-written two-identity list, both rows with empty evidence (`CH-11`) |
| `PROCESS` | 17 (1.15%) | none of the 17 carries a facet record; 10 sit at the register's lowest status; and the report declares nine of the twenty facets not covered at all, so "all twenty established" contradicts its own text (`CH-12`) |

## 5. Tenant Isolation — a DETERMINED absence, unchanged by the correction

> **The reference system has no tenant concept.** Its isolation axis is company. A census across the
> frozen population found no element whose subject is a tenant boundary.

Recorded as **DETERMINED = the condition is "none"**, evidenced by the census. Not `N/A`: §5 is explicit
that *unknown does not equal N/A*, and this is neither — it is a measured zero.

**For SMEsPlus this is the most consequential single line in the matrix.** SMEsPlus is specified as
multi-tenant; its most critical isolation axis has **no reference population to learn from, compare
against, or challenge**. It cannot be derived here. It must be designed, without the comparative
evidence every other Critical Area has. Carried to the Boss as a decision input.

## 6. Open Critical Gaps

Six open, **zero closed** — see `VDR_OPEN_CRITICAL_GAP_CLOSURE_REGISTER.md`, which addresses each
individually as §11 requires. Three moved during this session; movement is not closure.

## 7. Challenge result

**Round R1 challenged by three independent reviewers against frozen SHA `a146e004`; the package was not
touched while they held it, verified by two independent units.** 56 findings returned, 36 adopted.
Full disposition in `SMES_CORE_PREP003_CHALLENGE_REPORT.md`. **The challenge reduced this matrix's
headline from 1 of 15 to 0 of 15.**

## 8. Disposition contribution

§21 bars CONDITIONAL PASS while any Critical Area is below 100%. **Fourteen are below 100%, and one is
not computable** — a distinction the R1 text collapsed (`CH-24`). This matrix contributes **HOLD**, and
no reading of it supports anything else.
