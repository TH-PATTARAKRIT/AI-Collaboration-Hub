# VDR_PRIOR_RESEARCH_REVALIDATION_REPORT.md
# Prior conclusions re-derived on the current generation — not referred upward

Session `[SMEPLUS-26-09-10-VDR-PREP-004]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 09.

---

## 1. What this report takes back from the Boss

PREP-003 closed by asking the Boss: *"`BOSS-DEC-01` — must the valuation conclusions be re-derived in
the current generation before any design relies on them?"*

**That was a misrouted question.** §2 of this round's instruction lists *"Should this conclusion be
re-derived?"* verbatim among the questions the Boss shall not be asked. The answer is determinable by
evidence, the evidence was on this host, and the team's job was to go and get it.

**It has been re-derived. The result is below, and `BOSS-DEC-01` is withdrawn from the Boss decision
list.**

## 2. Method

| Clause | Value |
|--------|-------|
| **POPULATION** | every movement row on the transacted current-generation deployment |
| **UNIT** | one movement row |
| **PATTERN** | direct extraction of the movement, valuation, category and accounting-line tables; no server started |
| **STATE BASIS** | declared in the same line as every number below — the omission that produced the previous round's unreconciled denominator |
| **CONFIGURATION BASIS** | read from the deployment's own category records, not assumed |

### `PR4-F-01` — the unreconciled denominator is RESOLVED, and both prior figures were right

PREP-003 carried **14,441** in a column headed *Completed movements* and **3,680** in three other
places, and could not reconcile them from inside the frozen package. Measured directly:

| State | Rows |
|-------|-----:|
| assigned | 6,336 |
| **done (completed)** | **3,680** |
| confirmed | 2,294 |
| cancel | 2,131 |
| **all states** | **14,441** |

**Both numbers were correct and one was mislabelled.** 14,441 is every movement row; 3,680 is the
completed subset. The **column heading was wrong**, not the retraction — the retraction's *"100% of
3,680 completed movements"* stands exactly as published. `CH-17` is **CLOSED**.

### `PR4-F-02` — the "every deployment runs periodic valuation" premise is FALSE

PREP-002 and PREP-003 both rested a conclusion on the claim that *"every located current-generation
deployment runs periodic valuation, under which no movement posts, in any generation."* That claim was
never tested against a deployment's own configuration records.

Read from the transacted deployment's own category records:

| Setting | Value | Categories |
|---------|-------|-----------:|
| valuation | **real time (perpetual)** | **27 of 37** |
| valuation | not set | 10 |
| cost method | average | 28 |
| cost method | standard | 2 |
| cost method | not set | 7 |

**The deployment is configured for perpetual valuation, not periodic.** The configuration control that
was offered as the explanation did not exist. **This is a retraction of the explanation, not of the
retraction it explained** — `RR-F-06`'s withdrawal stands on the state-basis argument, which is
independently confirmed in §3.

### `PR4-F-03` — under perpetual valuation, on a transacted current-generation deployment, **no movement is linked to any accounting entry**

Three independent measurements, each with its control:

| Measurement | Result |
|-------------|--------|
| Completed movements carrying a per-movement value | **3,680 of 3,680 — 100%** |
| Of those, value ≠ 0 | **2,431**; the remaining **1,249 completed movements carry a value of exactly zero** |
| Completed movements linked to an accounting entry | **0 of 3,680** |
| The same link across **all** 14,441 rows (positive control: could the column ever hold a value?) | **0 of 14,441 — the column is never populated on this deployment** |
| The dedicated valuation-ledger table | **absent from the dump entirely** — 0 entries in its table of contents |
| A stock reference on the accounting-line table | **no such column exists** — the accounting line carries no movement, valuation or quantity link |

**Under a perpetual configuration, completed movements are expected to produce accounting entries.
On this deployment, no such link is located by any of the three routes that could carry one.**

> **Stated at the width the evidence supports.** This establishes *no link located by three named
> routes* — not *no link exists*. Enumerating every possible writer before attributing a null to one
> mechanism is a discipline this programme has on record, and it is applied here rather than claimed.

### Why this is stronger than the conclusion it supersedes

| Prior conclusion | Status | Replacement |
|------------------|--------|-------------|
| *"The valuation ledger is the per-movement valuation record"* | **SUPERSEDED** | the value is carried on the movement row itself; the ledger table does not exist here |
| *"The current generation is not writing per-movement valuation"* | **already retracted; retraction CONFIRMED** | 100% of completed movements carry one |
| *"Periodic configuration explains the absence of postings"* | **CONTRADICTED** | the deployment is configured perpetual |
| *"Inventory emits facts; Accounting decides postings"* | **VALID, and now sharpened** | inventory emits a valued fact; **on this deployment nothing consumes it** |
| *"A completed movement fact is immutable; corrections are new reversing facts"* | **VALID** | unchanged; corroborated by the terminal-by-construction documents |
| The 19-menu accounting-dependency lock | **VALID WITH DELTA** | the dependency is real and the measured gap is wider than stated: not a changed object, but **no link at all** |

### `PR4-F-05` — the discriminating spread across five deployments and three generations

A zero is only interpretable against a population that should *not* show the effect. Measured across
every deployment, with the state basis and the configuration basis declared in the same rows:

| Deployment | Gen | Valuation configuration | Movements | Completed | Carrying a per-movement value | Accounting-linked |
|-----------|----:|------------------------|----------:|----------:|------------------------------:|------------------:|
| `BK12MAY26` | 19 | **real time × 27 of 37** | 14,441 | 3,680 | **3,680 (100%)** | 0 |
| `iEVING` | 19 | **real time × 28 of 37** | 13 | 8 | 4 | 0 |
| `iTEST02` | 19 | unset × 3,977; periodic × 3 | 55 | 2 | 2 | 0 |
| `idemo18_uat` | 18 | unset × 126 | 51,081 | 46,048 | **0** | 0 |
| `iSMEs` | 16 | *(setting absent)* | 103,949 | 81,909 | **0** | 0 |

**Two clean discriminations, and the second is the one that matters:**

1. **The per-movement value is a generation-19 phenomenon.** Every generation-19 deployment populates
   it; **neither the 18 nor the 16 deployment populates it on 127,957 completed movements between
   them.** Those two are the negative control this comparison previously lacked, and they behave
   exactly as a negative control should.
2. **Where the value lives moved between generations.** In 16 and 18 it lives in the dedicated valuation
   ledger — the 16-generation deployment carries 74,982 such rows. In 19 that table is **absent from the
   dump entirely** and the value is on the movement row. `CRITICAL-GAP-01`'s "the object was replaced"
   is now **measured, with both sides of the replacement observed**, rather than inferred from an
   absence.

The accounting-link column is null on **all five deployments across all three generations**, which tells
us it is **not the link mechanism in any generation** — in 16 and 18 the link runs through the valuation
ledger. That is why §5's claim is bounded to *routes located*, not to *links existing*.

### `PR4-F-04` — 1,249 completed movements carry a value of exactly zero

34% of completed movements are valued at zero. On an average-cost configuration this is possible for
genuine reasons (zero-cost products, internal transfers between valued locations), and it is also the
signature of a costing input that never arrived. **Determined: the zeros exist. Not determined: which
cause produced them** — that needs the per-product cost history, which is a bounded next measurement,
not a Boss question.

## 8. Classification of every prior material conclusion

| Conclusion | Class | Evidence |
|-----------|-------|----------|
| Inventory emits facts; Accounting decides postings | **VALID** | §5 |
| Completed movement facts are immutable | **VALID** | prior + corroborated |
| Valuation ledger is the per-movement record | **SUPERSEDED** | §5 |
| Current generation writes no per-movement value | **CONTRADICTED** *(already retracted)* | §5 |
| Periodic configuration explains the absence | **CONTRADICTED** | §4 |
| 19-menu accounting dependency | **VALID WITH DELTA** | §5 |
| Valuation report menu has no current counterpart | **VALID** | prior, unchanged |
| Conclusions derived from prior-generation valuation behaviour | **UNVERIFIED in the current generation** | unchanged |

**All prior evidence is preserved as audit lineage. Nothing was silently replaced, and every movement
above carries the measurement that produced it.**

## 9. What remains genuinely open, and to whom it belongs

| Item | Owner |
|------|-------|
| Which cause produced the 1,249 zero-valued completions | **team** — bounded measurement, next round |
| Whether the missing inventory→accounting link is a configuration defect or the current generation's design | **team — MEASURED THIS ROUND, §6.** A second perpetual current-generation deployment behaves identically, and the two prior-generation deployments show the value living in the ledger instead. Not a Boss question, and no longer an open one |
| Where the generation-19 accounting link runs, if it runs at all | **team** — the three located routes are exhausted; the next measurement is the accounting entry population itself |
| Whether SMEsPlus adopts a design in which inventory value is consumed by accounting, and on what event | **BOSS — genuine architecture policy**, and only after the two rows above are closed |
