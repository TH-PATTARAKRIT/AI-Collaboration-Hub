# VDR_COVERAGE_MEASUREMENT_SPEC.md
# Coverage Measurement Specification — the mathematics of every published percentage

Session `[SMEPLUS-26-09-10-VDR-PREP-003]` · Layer: **LAYER 1 — CLEAN-ROOM.**
Status: **v2.0 — corrected after independent challenge.** Supersedes v1.0 and the informal coverage
arithmetic of PREP-001 and PREP-002.

---

## 1. The defect this specification exists to repair

PREP-002 reported **Overall Verified Coverage: NOT COMPUTABLE**. The cause was recorded as
`CORR-F-38`: the population register carried **one ordinal `research_status` per row**, so an item
satisfying three independent dimensions could not be represented, and any three-dimension count over
it was **zero by construction**.

**The repair is structural.** Every Learning Item now carries **nine independent dimension columns**,
each taking one of three values, plus a recorded condition and — where `NA` — an explicit reason.

## 2. The nine dimensions

| # | Dimension | What it asserts about the item |
|---|-----------|-------------------------------|
| 1 | `PROCESS` | what happens when it runs |
| 2 | `CONFIGURATION` | what configuration condition governs it |
| 3 | `OPTIONAL_FUNCTION` | what optional capability activates it |
| 4 | `SOURCE` | where it is declared, in which root, at which generation |
| 5 | `RUNTIME` | whether it can be reached, and whether it was observed |
| 6 | `DATA_MODEL` | what data it holds or touches |
| 7 | `SECURITY` | what access control governs it |
| 8 | `CROSS_MODULE` | what it references outside the domain |
| 9 | `EDGE` | its reverse / cancel / return path |

## 3. Applicability — a DECLARED RULE TABLE, not a per-row judgement

A dimension is `NA` for a Learning Item **only** because of the item's **class**, by a rule table fixed
before measurement. `NA` is never assigned to an individual row, and **unknown is never `NA`** (§5).

| Class | PROC | CONF | OPT | SRC | RUN | DATA | SEC | XMOD | EDGE |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| MENU · MENUX · ACTION | ● | ● | ● | ● | ● | – | ● | – | – |
| VIEW | – | ● | ● | ● | ● | – | ● | – | – |
| BUTTON | ● | ● | ● | ● | ● | – | ● | – | ● |
| FIELD | – | ● | ● | ● | ● | ● | ● | ● | – |
| SETTING | – | ● | ● | ● | ● | ● | – | ● | – |
| AUTOMATION | ● | ● | ● | ● | ● | ● | – | ● | ● |
| BEHAVIOUR | ● | – | – | ● | ● | ● | – | ● | ● |
| CONSTRAINT | – | – | – | ● | ● | ● | – | – | – |
| RULE · ACL | – | – | – | ● | ● | – | ● | – | – |
| GROUP | – | ● | ● | ● | ● | – | ● | – | – |
| SEQUENCE | – | ● | – | ● | ● | ● | – | – | – |
| SYSPARAM | – | ● | ● | ● | ● | – | – | – | – |
| OBJECT | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| GATEDELEM | – | ● | ● | ● | ● | – | ● | – | – |
| HANDOFF | – | – | – | ● | ● | – | – | ● | – |

**Total applicable dimension cells: 30,906** over 5,074 items. That is the denominator of every
cell-level percentage in this programme.

> **v1.0 published 30,741, and that figure was wrong.** 180 cells this table marks applicable had been
> reclassified as `NA` *after failing their grade*, taking both affected denominators down with them
> (`CH-01`). All 180 are restored; 15 left by the container rule. The table above did not change — the
> register was corrected to obey it. Full lineage in `VDR_EXCLUSION_REGISTER.md`.

## 4. TWO GRADES — and why they must never be merged

This is the specification's most important clause, and it was written **after** a single-grade model
produced **100% on every dimension** — a result that was a symptom, not an achievement. The predicate
had drifted from *"meets the depth standard"* to *"the condition is established"*.

| Grade | Means | Evidence required |
|-------|-------|-------------------|
| **NOT DETERMINED** | the condition is **not** established — the honest value where an instrument could not reach | the failure recorded per item |
| **DETERMINED** | the item's condition on that dimension is **established from evidence, including a determination of "none"** | a census that is instrument-validated (second shape, positive control drawn **from the corpus**, coverage assertion, zero re-test) and whose result is recorded per item |
| **RESEARCH-VERIFIED** | the dimension meets the **depth standard** the commissioning prompt defines | §6's twenty process facets · §7's config OFF-vs-ON consequence across nine axes · §8's thirteen optional-function attributes including deactivation behaviour |

> **`NOT_DETERMINED` must exist in the register, or `DETERMINED` is not a test.** v1.0 contained not one
> `NOT_DETERMINED` cell in 30,741 — so `DETERMINED` was a synonym for *applicable*, and its 100.00% on
> all nine dimensions was true by construction (`CH-01`). v2.0 carries 132 of them.
>
> **A determination of "none" is a result, not a gap — but it is not depth.** Knowing that an element
> carries no configuration gate is real evidence; knowing what changes when a capability is switched
> off is a different and much larger claim.

**Both grades are published for every dimension. Neither is presented as the other.**

## 5. Formula set

For dimension `d` over population `Q`:

```
APPLICABLE(d,Q)   = |{ i ∈ Q : rule_table[class(i)][d] = applicable }|
DETERMINED(d,Q)   = |{ i ∈ APPLICABLE : grade(i,d) ∈ {DETERMINED, RESEARCH-VERIFIED} }|
RESEARCH_VER(d,Q) = |{ i ∈ APPLICABLE : grade(i,d) = RESEARCH-VERIFIED }|

Determined Coverage %(d,Q)        = DETERMINED(d,Q)   / APPLICABLE(d,Q)
Research-Verified Coverage %(d,Q) = RESEARCH_VER(d,Q) / APPLICABLE(d,Q)
```

Item-level:

```
DETERMINED-COMPLETE(i) ⇔ ∀d applicable to i : grade(i,d) ≥ DETERMINED
RESEARCH-COMPLETE(i)   ⇔ ∀d applicable to i : grade(i,d) = RESEARCH-VERIFIED

Overall Verified Coverage = |{ i ∈ APPLICABLE_POPULATION : RESEARCH-COMPLETE(i) }|
                            ────────────────────────────────────────────────────
                                        |APPLICABLE_POPULATION|
```

**`Overall Verified Coverage` is defined on RESEARCH-COMPLETE, never on DETERMINED-COMPLETE.**
Using the weaker grade would report 100% and mean nothing.

## 6. Eligibility and exclusion rules

| Rule | Statement |
|------|-----------|
| **ELIGIBILITY** | every item in the frozen population is eligible for every dimension the rule table marks applicable |
| **REGISTERED EXCLUSION ONLY** | a cell leaves a denominator **only** by the class rule table or by a row in `VDR_EXCLUSION_REGISTER.md`. A per-row `NA` that is in neither is a defect, not an exclusion |
| **NO POST-HOC `NA`** | a cell may never be reclassified `NA` after it has been graded. The direction of that edit is always toward a better number |
| **EXCLUSION** | an item leaves the applicable population only by an entry in the exclusion register, carrying **Learning ID · reason · evidence · reviewer · status**. No silent exclusion |
| **`NA` is not exclusion** | an `NA` cell removes a *cell* from a dimension denominator, by the class rule table, with a recorded reason. The item stays in the population |
| **Denominator stability** | once coverage calculation begins the denominator is frozen. A material change forces a **new population version**, recalculation of every affected metric, and preservation of the prior calculation |

## 7. Evidence and status required, per dimension, for RESEARCH-VERIFIED

| Dimension | Evidence required |
|-----------|-------------------|
| `PROCESS` | all twenty §6 facets determined, including calculation semantics, retry, and cancel/reverse/return semantics — **not** the eleven mechanically-derivable facets alone |
| `CONFIGURATION` | the OFF-vs-ON consequence determined across §7's nine axes |
| `OPTIONAL_FUNCTION` | §8's thirteen attributes, **including deactivation behaviour** |
| `SOURCE` | a reproducible pointer with root and content-verified generation — **resolvable to file *and* line**. v1.0 graded this by an unconditional literal that could not fail, and 186 of its pointers resolve to no file at all (`CH-03`) |
| `RUNTIME` | **element observed** on a deployment — module installation alone is `DETERMINED`, not research-verified |
| `DATA_MODEL` | the item's own declared type, attributes, relations and constraints |
| `SECURITY` | the access grants and record rules that govern it, enumerated |
| `CROSS_MODULE` | its boundary-crossing relations, enumerated from a system-wide census |
| `EDGE` | the reverse / cancel / return path established, including its absence proved |

## 8. What this specification does not permit

- No qualitative estimate. Every percentage resolves to two integers from the frozen register.
- No collapsing of the two grades, and no single headline that hides which grade it uses.
- No dimension marked `NA` without a reason recorded in the same row.
- No denominator change after calculation begins without a new population version.
- **No percentage may rise because a predicate was relaxed.** If a number improves, the evidence that
  moved it must be identifiable. **v1.0 breached this clause, in the document that states it.**
- **A grade that never varies within a class is a class label, not a measurement**, and may not be
  published as RESEARCH-VERIFIED. Four dimensions failed this test in v1.0 and are corrected (`CH-03`).
- **A positive control must be drawn from the corpus being searched**, never from the searcher's
  vocabulary, and must be able to fail the way the predicate fails.
