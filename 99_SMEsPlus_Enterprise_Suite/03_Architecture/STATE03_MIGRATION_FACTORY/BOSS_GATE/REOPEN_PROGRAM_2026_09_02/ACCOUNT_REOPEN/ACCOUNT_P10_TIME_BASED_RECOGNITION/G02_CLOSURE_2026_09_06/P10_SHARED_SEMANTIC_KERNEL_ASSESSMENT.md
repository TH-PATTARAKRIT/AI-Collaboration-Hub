# P10 — SHARED SEMANTIC KERNEL ASSESSMENT  (`CQ-P10-09`)

**Terminal disposition: `DESIGN CANDIDATE` throughout. Nothing here is architecture, adopted, or frozen. P10 does not decide P11-owned programme architecture.**

---

## 1. The Six Candidate Elements, Assessed

| Element | Can it be shared safely? | Basis | Class |
|---|---|---|---|
| **Event identity** | **NOT P10's to share.** The accounting-event object belongs to `D-5`; P10 specialises rather than authors, and attaches `AASP-COND-01` | Peer's class-`A` finding over its 22-root set, plus P10's own class-`A` search over one root | `BOSS DECISION REQUIRED` |
| **Period grid** | **Blocked.** The ledger has no period object; a period is a date range and closing one is moving a date | Peer-supplied, class `B` — P10 has not re-derived it | `UNRESOLVED — DECISION/EVIDENCE REQUIRED` |
| **Convention library** | **YES — and it changes from *build* to *adopt-and-extend*.** A complete standards-named library of eight conventions already exists in the declared root | This round's finding; three engines, not two | `DESIGN CANDIDATE` |
| **Correction algebra** | **Partly.** The three *outcomes* are common; *which* applies is domain-specific and the *operations* are not shared at all | Four behaviours across four mechanisms; row 1 of the comparison contradicts full sharing | `DESIGN CANDIDATE`, qualified |
| **Scope resolution** | **Adopted, not owned.** The rules are programme-wide positions from peers, not P10 inventions | `SCP-08`, `SCP-09`, `MA-11` | `DESIGN CANDIDATE` |
| **Period-vs-posting separation** | **Necessary and not sufficient**, and the *obligation* sits with the ledger owner | Depreciation carries its period and is still relocated | `FACT-SUPPORTED FUNCTIONAL REQUIREMENT` for the requirement; `CROSS-PROCESS` for the obligation |

## 2. The Element the Prior Round Gave Away and This Round Restores

**Attribution construction.**

The prior round classified the nets-to-zero attribution as a shared-posting-layer property and returned it to the ledger owner. **That was wrong.** The shape is constructed by **each mechanism's own generator**, not by the shared posting layer.

**Instance count: four**, and they fail in three different ways.

| Mechanism | Shape | Failure |
|---|---|---|
| Deferral, validation path | same distribution on both legs, opposite signs | **exact netting** |
| Asset depreciation | same distribution on both legs | **exact netting** |
| Deferral, grouped path | two *different* ratios on different grouping keys | **residue, not a clean zero** |
| Accrual counterpart | weighted over a denominator including lines with nothing to accrue, skipping lines with no distribution | **sums to less than 100%** |

> **Four independent mechanism-level implementations of one idea, failing three different ways.** That is the strongest available evidence for a shared allocation layer in the entire package — independent re-implementation did not even fail the same way twice.

**And the accounting significance is settled against the counter-reading.** Correcting the emission so only the profit-and-loss leg carries the attribution leaves the total unchanged and correctly phased — **so the both-legs shape buys nothing.** What it costs is the whole time dimension: the netting **survives period bounding**, so a period-scoped management report shows **zero movement** from the entire deferral machinery. Cumulatively correct; **by period exactly as wrong as no deferral at all** — which is the level P10 owns.

## 3. The Kernel, As It Now Stands

**Three elements P10 can carry, all `DESIGN CANDIDATE`:**

1. **Convention library** — adopt-and-extend, not build.
2. **Correction algebra** — three outcomes, domain-selected, operations not shared.
3. **Attribution construction** — the strongest, on four independent instances.

**Two elements relocated:** event identity to `D-5`; period-versus-posting separation to the ledger owner as an obligation.
**One element blocked:** the period grid, on a ledger concept that does not exist.

**Sequencing, corrected:** the prior round said the whole kernel was *"sequenced after `D-5` and not independently decidable"*. **Too strong.** Elements 1 and 3 are decidable now. Element 2 is specifiable now and **enforceable** only once there is something to address.

## 4. What Belongs in Separate Domain Engines

Confirmed domain-owned, and two of these were candidates for sharing before being tested:

**object · lifecycle · posting pattern · business rules · termination condition · residue policy**

- **Termination condition** — depreciation terminates on **value**, deferral on **count**. Two different recurrences; a shared loop gives one of them behaviour it must not have.
- **Residue policy** — four mechanisms, four assertions about who owns a difference, including one that **refuses** residue because its schedule is an external contractual document.

**And deferred revenue and deferred expense are ONE domain**, not two. Their independent settings are a configuration surface, not a domain boundary.

## 5. The Boss's Standing Warning, Honoured Both Ways

> *Never assume asset depreciation and deferred recognition share an implementation merely because both use schedules.*

They do not — they differ on object, lifecycle, posting pattern, termination and residue.
**And the converse is equally forbidden:** the reference's asset object is described as covering **asset *and revenue* recognition** and still carries deferred-revenue commentary in its board computation. They were one engine in this product line.

**Neither "they are the same" nor "they are wholly different" is supportable.**

## 6. Disposition

`CQ-P10-09`: **`DESIGN CANDIDATE`** for the three carried elements · **`BOSS DECISION REQUIRED`** for event identity (`D-5`) · **`CROSS-PROCESS OWNER — HANDOFF PUBLISHED`** for the period grid and the period-versus-posting obligation.

**Architecture is P11-owned. This is input.**
