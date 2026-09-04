# 09 — ACCOUNT WAVE A — CONVERGENCE TEST `MC-01` … `MC-10`

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001` · Layer 1 clean-room
Tests as written in `SMEPLUS-DR-MC-001` §6. **No test is marked met without evidence.**

Verdict vocabulary: `MET` · `PARTIALLY MET` · `NOT MET` · `NOT EVALUABLE`.
The word `PASS` is not used as a verdict in this package.

---

## `MC-01` — Population Boundedness · **NOT MET**

*"The material research universe is explicitly defined and bounded, or the unbounded remainder is
explicitly declared and proven non-gating."*

**Achieved.** 24 populations acquired a verified, source-derived denominator, from a starting point of
zero (file `02`). 5 populations are explicitly declared `UNBOUNDED / NOT YET ENUMERABLE` with no
percentage claimed over them.

**Why it still fails.** The Wave A **source surface itself** was under-bounded by this round.
`MCE-001` fixed it at 18 files / 16,044 lines. The corrected surface is **26 files / 21,883 lines**
(`MCX-11`, `MCE02` §5). The 18-file set excluded:

- the partner/contact model — the site of `X-05`, the round's most severe finding;
- the framework currency-rate model — the site of `SB-05` and `FX-08`;
- the company model — **every lock date in Wave A** and the fiscal-year definition;
- a 1,158-line inherited extension of the journal model carrying 13 raw-SQL and 10 elevation sites.

A Wave A denominator that omits the sites of the programme's three most severe findings is not
bounded. **`MC-01` fails on this round's own artefact.**

Six further material populations were enumerated **nowhere** — raw DDL, the compute/dependency graph,
cascade deletes, scheduled actors, server actions, and the audit-trail surface (`MCX-09`, `MCX-13`,
`MCX-14`, `MCX-10`, `MCX-15`).

## `MC-02` — Systematic Enumeration · **PARTIALLY MET**

*"Coverage comes from deterministic enumeration, not ad-hoc browsing or reviewer discovery alone."*

**Met in kind, for the first time in the programme.** Every count in `MCE00` is produced by a
single-pass mechanical command over a declared path set, retained and re-runnable (`MCE01`). All
17 denominators an independent reviewer recounted reproduced exactly, bar declared method
ambiguities (`MCE02` §3).

**Not met in extent.** Two enumerations were bounded by the *matching pattern* rather than by the
source, and both produced false closures:

- `MCE-006` matched only single-line configuration-key reads and declared a population "complete" at
  5. The sixth member is material and is documented three times in this package's own parent
  (`MCX-01`).
- `MCE-007` declared a "complete" writer set and missed three further scoping rules in one file
  (`MCX-03`).

Deterministic enumeration is only as bounded as its pattern, and a pattern is author-derived. **The
scope statement must declare the pattern, not only the path.** That is the correction carried to
`ER-CORE`.

## `MC-03` — Independent Delta Test · **NOT MET**

*"A fresh independent reviewer runs the same bounded scope and returns no new material class of
finding."*

Two fresh reviewers returned **eleven new material classes** between them, of which this session
verified against primary source and accepted:

`MCX-07` merge unions company scope onto posted ledger identity by raw SQL with no lock check ·
`MCX-08` silent destructive fallback · `MCX-09` raw-DDL control population · `MCX-10` unattended
GL-posting actor · `MCX-11` the lock-date model outside the model set · `MCX-12` inherited-extension
blind spot · `MCX-13` compute/dependency graph · `MCX-14` cascade deletes · `RB-01` finding-loss
through consolidation · `RB-02` no correction-propagation channel · `RB-06` a gate metric redefined
mid-row.

**`MC-03` fails decisively, and it is the test that matters most**, because it is the direct measure
of whether the loop `SMEPLUS-DR-MC-001` exists to stop has been broken. It has not.

## `MC-04` — Repeatability · **PARTIALLY MET**

*"A second independent pass using the same scope and method produces materially equivalent coverage
and conclusions."*

**Met for the mechanical layer.** An independent reviewer re-ran the enumerations from primary source
and reproduced **17 of 17** headline denominators, with three declared-method discrepancies
(privilege de-elevation, constraint tuples, object buttons) and one arithmetic error in a bounding
figure (791 addon directories, not 797).

**Not met for conclusions.** The same rerun **contradicted two of the round's three claimed
closures**. Coverage reproduced; conclusions did not.

The second reviewer could not evaluate repeatability at all — the retained scripts were not located
from the package, so the reproducibility basis is asserted rather than demonstrated to a reader.
**The scripts must ship inside the evidence package, not beside it.**

## `MC-05` — Negative Claim Compliance · **NOT MET**

*"All material negative claims comply with `DR-NC`. `Not found` is not promoted to `verified absent`
without proportional evidence."*

Established over **41.9%** of the package by volume and asserted over 100% of it. 19 files / 8,462
lines — including every expert review, every fresh review, the challenge register and both Layer-2
evidence files — carry **377 untriaged negative-strength tokens**, 1.9× the load that was triaged
(file `07`).

**And the round's own file breached it.** `MCE00` made four unbounded "complete" / "only" claims;
the two that said *complete* without declaring a search pattern are the two that were falsified
(`MCE02` §2).

**Genuine progress, recorded:** the first **four** claims in the programme to reach class
`VERIFIED ABSENCE` — because bounding a population is what makes a legitimate absence claim possible
at all. `MCE-004` is the model: a whole-tree claim backed by a whole-tree search, independently
re-verified and unchanged.

## `MC-06` — Unknown Classification · **MET for the enumerated population; parent count CONTRADICTED**

Every unknown identifiable this round is classified; every routed item names its destination; the one
item hidden by routing was recovered and reclassified `GATING` (file `06`).

The parent figure of **41** is contradicted in every input term and was never enumerable from the
package's own tables. Independent enumeration yields **59**, of which **17 are `GATING`**, plus **5
ids cited in the registers but written up nowhere**.

**The standard's rule applies:** *"For every `GATING` unknown, close it or remain `HOLD`."*
None of the 17 is closed. Three were opened by this round.

## `MC-07` — Contradiction Closure · **NOT MET as reported**

*"All material contradictions are dispositioned with evidence and lineage."*

**On the substance the test is arguably satisfiable:** all 16 registered contradictions carry evidence
and lineage.

**On the reporting it fails outright.** `G10` §4 states *"Contradiction resolution — 100% (16 of 16
registered contradictions resolved or explicitly bounded)"*. The register it cites states, verbatim:

> **"None of the fifteen contradictions is resolved by this session, and none can be."**

Twelve of the sixteen read *"stands"*; two worsened; two were narrowed. **Zero are closed.** The gate
figure reaches 100% by widening the metric to *"resolved **or explicitly bounded**"* inside the cell —
"explicitly bounded" is a scoping statement, not a closure. The same register also disagrees with
itself on its own denominator (16 rows, text says fifteen).

A metric redefined at the gate, in the gate's favour, is a governance defect independent of the
evidence beneath it.

## `MC-08` — Tolerance-Zero Closure · **NOT MET**

*"No unresolved tolerance-zero issue remains."* Re-tested this round.

| id | Boundary | Status |
|---|---|---|
| `T0-01` | Entry balance | **UNRESOLVED — verified defect.** No storage-level enforcement; suppressible; escalated to externally reachable |
| `T0-02` | Posting without a measurement | **UNRESOLVED — worsened.** Trigger widened; the only detecting control is contaminated |
| `T0-03` | Deletion or rewrite of a posted fact | **UNRESOLVED — worsened.** Seven production bypass sites, plus `MCX-07`, on which the lock control is **not on the path at all** |
| `T0-04` | Tenant isolation | **UNRESOLVED — severity raised.** Creatable by a routine accounting role; no database boundary; the configuration-key class is **larger than reported** (`MCX-01`) |
| `T0-05` | Over-reconciliation | **UNRESOLVED — widened.** Upgraded this round to a class-`A` verified absence: **no record rule on either reconciliation model anywhere in the tree**, with full write rights for ordinary accounting roles (`MCE-004`) |
| `T0-06` | No cross-company rewrite of a posted fact | **UNRESOLVED — verified defect**, reachable with contacts rights alone |
| **`T0-07`** | **Cross-company rate resolution in raw SQL, outside every record rule, with an undeclared par fallback** | **UNCHARACTERISED — and was on no list.** Raised by a final-round reviewer as a tolerance-zero candidate; absent from every blocker and every tolerance-zero list (`MCU-05`) |

**Seven by evidence, six by record. Six are unresolved verified defects; the seventh was lost between
the review that raised it and the gate report that omitted it.** `MC-08` fails.

## `MC-09` — Evidence Lineage · **NOT MET**

*"Every material conclusion is traceable to evidence, correction lineage, and final disposition."*

Traceable **into** the evidence; broken **on the way back out**. Two independent breaks:

1. **No correction from the final round reaches any Layer 1 register.** Every correction notice on
   files `01`–`26` names only the middle round. The final round's contradictions exist **only** under
   its own directory. A reader of the canonical boundary register — cited by every other Level — has
   no pointer of any kind to the round that contradicted its first four rows (`RB-02`, `RB-03`).
2. **Reviewer findings are consolidated by re-narration, not by id.** Eight of a final reviewer's
   nine numbered findings occur nowhere outside that reviewer's own file. One of them was a
   tolerance-zero candidate (`T0-07`), and it was lost (`RB-01`). Two were balanced-but-wrong cases
   the reviewer explicitly asked to be registered; the register stands at 27 without them, so the
   true floor is **29**.

**This is the single most consequential result of the round.** `GB-04` says the enumeration method has
not converged. `MC-09` says something worse and cheaper to fix: **even when a finding is made, there
is no channel by which it becomes a corrected artefact.** Without that channel, no amount of
enumeration can converge, because each round's findings do not reduce the next round's error.

Arithmetic consequences already visible: the coverage register's rows and summary disagree by 4
(`MCE-010`); its own correction notice is applied in neither body nor summary, which if applied
invalidates the published **95.5%** evidence-coverage figure carried in three gate reports (`RB-08`);
the unknown register has 5 orphan ids (`RB-07`).

## `MC-10` — New-Finding Delta Threshold · **NOT MET**

*"A fresh review adds no material finding that changes architecture, financial/operational semantics,
control design, SaaS boundary, migration requirement, or Gate recommendation."*

The fresh review added findings that change **control design** (`MCX-07`, `MCX-08`, `MCX-09`,
`MCX-10`), the **SaaS boundary** (`MCX-07` widens an account's company scope onto posted facts), and
the **method** (`MCX-11`, `RB-02`). It also **invalidated two of this round's three claimed
closures**.

Applying the standard's own instance-vs-class rule honestly: `MCX-03` (≥9 rate rules, not 6) and
`MCX-06` (count corrections) are **non-material instance delta** and would not by themselves break
convergence. `MCX-01`, `MCX-02`, `MCX-07` … `MCX-15`, `RB-01` and `RB-02` are **new classes**.
§7 of the standard is unambiguous: *"If a fresh round discovers a new material finding class,
convergence is `NOT ACHIEVED`."*

---

## Result

| Test | Verdict |
|---|---|
| `MC-01` Population Boundedness | **NOT MET** |
| `MC-02` Systematic Enumeration | `PARTIALLY MET` |
| `MC-03` Independent Delta | **NOT MET** |
| `MC-04` Repeatability | `PARTIALLY MET` |
| `MC-05` Negative Claim Compliance | **NOT MET** |
| `MC-06` Unknown Classification | `MET` for the enumerated population; parent count **CONTRADICTED** |
| `MC-07` Contradiction Closure | **NOT MET as reported** |
| `MC-08` Tolerance-Zero Closure | **NOT MET** |
| `MC-09` Evidence Lineage | **NOT MET** |
| `MC-10` New-Finding Delta | **NOT MET** |

**7 not met · 2 partially met · 1 met.**

> # `NOT CONVERGED`

## What this round nevertheless established

Recorded so the result is not read as a null round:

1. **24 verified denominators**, from zero. The exposure surface behind `GB-04` is now a number —
   **192 sites, 9 assessed** — instead of an unbounded worry.
2. **Four claims reached `VERIFIED ABSENCE`**, the first in the programme, including the
   reconciliation-model record-rule gap, independently re-verified and unchanged.
3. **One accepted reviewer finding corrected** — the raw-SQL rate path **includes** null-company rows
   and attributes them to every company, the opposite of what the gate package recorded, and in the
   more dangerous direction.
4. **The `GB-04` root cause is closed** (file `04`): enumeration ran over an author-derived taxonomy
   of business functions while every material finding inhabited source-derived mechanism populations.
   Eleven of eleven findings fit the pattern.
5. **A second, independent cause was found that no round had named** — the absence of a
   correction-propagation channel (`MC-09`). It is cheaper to fix than the enumeration gap and blocks
   convergence just as hard.
6. **The enumeration rules are reusable.** Seven of them are domain-independent and run unchanged on
   any SMEsPlus module with a company boundary (`MCE01`).
