# VDR_FOUR_WAY_REACHABILITY_CERTIFIED_MATRIX.md
# Four axes over the reconstructed Hop-0 — provisional until the instruments are certified

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 15.

---

## 1. Status of every number below

> **PROVISIONAL.** §14 forbids official coverage from an uncertified instrument. These figures are
> produced by `INS-01` and `INS-02`, which are **built and self-tested but not yet certified**. They are
> published so the shape is visible, and they are **not** the round's official coverage.

## 2. The result, over the 24,553-entity Hop-0 population

| Classification | n | % |
|----------------|--:|--:|
| **BOTH** — source resolves **and** runtime observed | **4,537** | **18.5%** |
| **RUNTIME ONLY** — observed, source does not resolve | **13,941** | **56.8%** |
| **SOURCE ONLY** — source resolves, observed nowhere | **6,075** | **24.7%** |
| NEITHER | 0 | 0% |

| Axis | Numerator / Denominator | Result |
|------|------------------------|-------:|
| Source Presence *(file **and** line)* | 7,741 / 24,553 | **31.53%** |
| Source resolving to a file only | 2,871 / 24,553 | 11.69% |
| Runtime Observation | 18,478 / 24,553 | **75.26%** |

## 3. What the shape says

**Runtime sees three-quarters of the domain; source resolution reaches under a third.** That is the
inverse of every prior round, and it is not a regression — it is what happens when the population stops
being built from source pointers.

- **13,941 entities are runtime-only.** Most are fields on domain models owned by other modules: real surface, present on real deployments, with no pointer into the declared source root.
- **6,075 are source-only.** Declared and installed nowhere across five deployments and three generations.
- **Only 18.5% are corroborated by both.**

## 4. Independence — tested, not asserted

§21 requires that no axis substitute for another. Over the comparable population the two axes disagree
on **81.5%** of entities. **An axis that could be inferred from another would agree with it.**

## 5. Against the threshold

| Dimension | Result | Floor | |
|-----------|-------:|------:|--|
| Source Presence | 31.53% | 96% | **FAIL** |
| Runtime Observation | 75.26% | 96% | **FAIL** |
| Configuration Reachability | *not measured this round* | 96% | **NOT MEASURED** |
| Optional Function Reachability | *not measured this round* | 96% | **NOT MEASURED** |

**Two axes measured, both far below the floor; two not measured at all.** No averaging is applied, and
none would help.

## 6. Why this is the honest number and the previous one was not

PREP-005 published Source Presence at 53.78% and Runtime at 53.02% over a 5,074-item population. The
same instruments over the reconstructed 24,553-item population give **31.53%** and **75.26%**.

**Neither pair is wrong arithmetically. The denominator changed by a factor of five**, and that is the
whole finding: a coverage percentage is a statement about a population, and this programme's population
was a fifth of the surface it claimed to describe.
