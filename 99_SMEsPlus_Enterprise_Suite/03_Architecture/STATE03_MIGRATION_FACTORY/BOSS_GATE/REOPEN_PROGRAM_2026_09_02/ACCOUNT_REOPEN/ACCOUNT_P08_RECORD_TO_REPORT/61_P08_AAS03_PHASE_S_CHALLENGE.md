# P08_AAS03_PHASE_S_CHALLENGE

Prompt `[SMEPLUS-26-09-06-P08-R2R-DOMAIN-PURE-BOUNDED-CLOSURE-002]` · **PHASE S** · surface frozen at `ea688bd` before launch

Four experts challenged **only** files `53`–`58`. None saw another's work. **Every material claim was re-run by the author against source or data before adoption**, and where a challenger was wrong the author says so.

| Expert | Lane | Verdict | Veto |
|---|---|---|---|
| **E1** Leader Functional Design | ledger semantics, finality, candidate completeness, contamination | `RECOMMEND HOLD` | `AAS03-E1-VETO-01`, 6 conditions |
| **E2** Leadership Database Design | every number re-derived; eligibility predicate | `RECOMMEND HOLD` | `AAS03-E2DB-V-01`, 6 conditions |
| **E3** Lead Integration & Localization | source-event boundary, tax/FX interface, scope, handoffs | `RECOMMEND HOLD` | `AAS03-E3-VETO-01`, 6 conditions |
| **E4** Lead Code & UI Architect | reachability, source-vs-runtime, version basis, citations | `RECOMMEND HOLD` | `AAS03-E4-VETO-01`, 7 conditions |

---

## 1. What all four agree on

**The arithmetic held.** Between them the experts re-derived essentially every published figure — the five arriving classes, 41.89%, 20.95%/0.12%, 63,773/100,580, 61,157/5,228/1,316, 17,513, 56,589, 174,977, 30 Buddhist-Era entries, 18 items naming 5 vanished entries, 6-of-89 and 29-of-109, 0 seals, 0 locks, 15 unlocated modules — and **not one arithmetic error was found.** E2 additionally ran **synthetic injection controls** on the three headline zeros: each moved 0→1 when a matching row was written, so the zeros are real and not silence from a dead predicate.

**And every material defect was one of four things:** a wrong predicate, a wrong unit, the wrong instrument for the claim, or a fact stated outside the scope its evidence supports.

> **`P08-M-22`. This is now the fourth consecutive round in which the arithmetic survived and the interpretation did not. The failure mode is stable, and it is not carelessness with numbers.**

## 2. The corrections that matter most

| ID | What was published | What is true | Found by |
|---|---|---|---|
| `P08-CONTRA-68` | *"There is no accounting-period object"* — an **absolute**, and the basis of what `58` hands **P11** | True only of the **declared 18.0 root set**. The 19.0 line carries a dated, recurring return object across 97 files; **both 19.0 databases carry its linking column on the entry table**; and **that source tree sits on this host, 1,428 modules, never searched** | E4 |
| `P08-CONTRA-62` | collision-freedom of the deployed numbering — `UNRESOLVED` | **It fails.** 4,722 numbers each borne by two posted entries — **9,444 entries, 5.58%** — all across journals. The number is unique within a journal and is **not an entry identifier** | E2, E4 independently |
| `P08-CONTRA-54` | *"Nothing makes a posted entry final"* | A **default-on guard** refuses to write **nine named fields** on a posted entry, estate-wide, no configuration. P08 measured the **optional seal** and concluded about **immutability** | E1 |
| `P08-CONTRA-55` | *"Settlement referential integrity — **holds**"*, the one control ranked unconditional | A module **installed on all three databases** deletes settlements, then items, then entries in **raw SQL** — the exact order that defeats the constraint — with no company or state predicate, a commit per table, and a reset of the number sequence to 1 | E3, E4 |
| `P08-CONTRA-65` | the author's own denominator correction, `0 of 6` and `0 of 29` | **Over-corrected.** A seal and a lock are **preventive**; conditioning on *having already posted* is selection on the outcome the control governs. Capability scope: **0 of 7** companies, **0 of 75** journals | E2 |
| `P08-CONTRA-58` | *"0 of 61,157 propagate the tax period to their whole item set"* — the *"most consequential instance"* | The mechanism stamps **tax lines only**: **54.3% ineligible**, 29.6% worked, **16.1% is the real defect** — and the deployed consumer reads the **entry** carrier through a join, refuting the consequence clause | E3 |
| `P08-CONTRA-63` | *"96.1% carry an origin pointer"* to P11; *"26.8%, the weakest of any class"* to P01 | **Three incompatible predicates for one phrase**, none declared. Structured pointers only: **78.03%** of entries, and **21.97%** carry none — not 3.9% | E1, E2, E4 |
| `P08-CONTRA-70` `-71` | *"seven of nine controls present and unengaged"* — the package's **self-declared central structural finding** | Does not follow from its own table. Two rows are **absences**, one is **unreachable on the database holding 99.987% of posted entries**, and three collapse into one entailment | E1, E4 |
| `P08-CONTRA-67` | *"Version discipline, carried on every row"* | **47 of 299 rows marked; 252 unmarked (84.3%)**, and the two artefacts that **leave P08** carry none at all across 55 rows | E4 |
| `P08-CONTRA-74` | the deployed reporting module — `UNRESOLVED` | **A fabricated blocker.** Its source was inside the path set the package had already declared | E4 |

**Three of the four named `UNRESOLVED` items were closed by challenge, and all three were answerable from evidence already in hand.** `P08-M-21`.

## 3. Where a challenger was wrong — verified and recorded

| Claim | Author verification |
|---|---|
| **E1:** the lock is consulted first, so *"sale documents are exempt"* is inverted | **PARTLY WRONG.** The exemption is **path-specific**: the derivation is not called at all for sale documents on the document-date-change path, and *is* called for all types on the posting path. E1 read the callee and generalised across 10 call sites. **Adopted as a qualification, not as an inversion** |
| **E1:** *"invoice_date is NULL on 129,577 of 129,577"* | **CORRECT — and the author's first re-check wrongly contradicted it** because of a string-escaping bug in the author's own script. Re-run correctly, E1 is right. **Recorded because the author nearly rejected a correct finding on a broken instrument** |
| **E3:** the root-set denominator is 22, so `N of 21` is wrong | **PARTLY RIGHT.** The declared set is 22; class-`A` negatives were expressed over the subset carrying each pattern. Both numbers were legitimate and **the surface never said which was which** — that is the real defect |
| **E4:** 4,895 mis-prefixed entries | **4,995** on the author's re-run — 2.95%. Immaterial delta, same substance |
| **E4:** *"15 artefacts"* in the unaudited population | **12** on the author's re-run. Same substance: the audit covered **22 of 64** |

**Reviewer findings are not automatically true. Five were adjusted on verification; none of the five adjustments rescued a published P08 claim.**

## 4. Vetoes

**Four independent vetoes, 25 lifting conditions between them.** They converge on five demands:

1. **Publish every predicate in executable form beside its result** — `AAS+-VETO-01` C-1, now demonstrably load-bearing on the package's most-travelled number.
2. **Give every control a three-way reachability status** — exists in 16.0 / 18.0 / 19.0 — and a verdict of engaged, unengaged-by-configuration, or unreachable-in-this-line.
3. **Carry the version marker on every row**, especially the two artefacts that leave P08.
4. **Re-run the domain-purity audit over all 64 artefacts** with a pattern not derived by the author.
5. **Read the 19.0 source line** that two of three deployed databases run and that sits unsearched on this host.

**None is discharged by this round.** The corrections above are **applied**; the conditions are about **method**, and method is not discharged by fixing the instances it produced.

## 5. Standing

| | |
|---|---|
| Material corrections adopted | **20** (`P08-CONTRA-48` … `-74`, excluding the five reviewer errors) |
| **Self-caught before challenge** | **5** — `P08-CONTRA-43` … `-47` |
| **Caught only by challenge** | **20** |
| Reviewer claims rejected or adjusted on verification | **5** |
| New findings the package did not have | **6** — `P08-F-51` … `-54`, plus the multi-currency-entry and scheduler-posted populations |
| Vetoes standing | **5** — four new, plus `AAS+-VETO-01` undischarged |
