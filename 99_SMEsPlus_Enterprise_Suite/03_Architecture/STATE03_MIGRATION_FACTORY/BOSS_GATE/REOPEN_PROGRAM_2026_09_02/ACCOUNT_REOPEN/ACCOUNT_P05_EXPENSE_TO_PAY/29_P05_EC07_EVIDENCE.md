# 29 — P05 `EC-07` EVIDENCE

`LAYER 2 — AUDIT QUARANTINE`

## 1. Authoritative Definition — quoted, not invented

From `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/SMEPLUS_VERY_DEEP_RESEARCH_8_CRITERIA_UNIVERSAL_EXIT_CONSTITUTION.md`
(`SMEPLUS-DR-EXIT-8C-001`), criterion `EC-07`:

> **EC-07 — Two Consecutive Clean Independent Passes**
> Before Final Research Gate, at least two consecutive fresh independent passes must complete without
> any of the following:
> - new material population
> - new material finding class
> - new gating unknown
> - reopened tolerance-zero issue
> - new Gate-changing contradiction
> - evidence-integrity failure
>
> Reviewer findings must themselves be independently verified before acceptance.
> `Independent Review != Truth.` `Verified Evidence = Truth Basis.`

**Unit of measurement:** a *pass* is one fresh independent review round. The counter advances only
when a pass completes **clean** on all six disqualifiers. A pass that raises any one of them resets
the count to zero.

## 2. Pass Ledger

| Pass | Round | Disqualifiers raised | Clean? |
|---|---|---|---|
| — | Primary research (author) | not a pass — the author is not independent | n/a |
| **1** | Four AAS-03 experts, original round (`16`) | **new material population** (`l10n_th_reports`, a second WHT subsystem, unscoped by the author); **new material finding class** (60 new findings); **new gating unknowns**; **7 new tolerance-zero boundaries**; **new Gate-changing contradictions** (12 author findings corrected) | **NO** |
| **2** | Four AAS-03 experts, targeted closure round (`36`) | see §3 | see §3 |

## 3. Pass 2 Measurement

Pass 2 was executed as part of this continuation: four fresh independent challenges with disjoint
mandates, briefed to attack the new evidence rather than confirm it. Its disqualifier measurement is
recorded in `36 §5` once the verdicts are consolidated.

**Independent of that measurement, `EC-07` cannot be satisfied by this continuation**, for a reason
that is structural rather than a matter of what pass 2 found:

> `EC-07` requires **two consecutive clean** passes. Pass 1 was demonstrably not clean — it produced a
> new material population, 60 new findings and 7 new tolerance-zero boundaries. Therefore even a
> perfectly clean pass 2 yields the sequence `dirty → clean`, which is **one** clean pass, not two
> consecutive. The earliest possible satisfaction of `EC-07` is after a **pass 3** that is also clean.

## 4. Why the Counter Still Reads Zero

Pass 2 additionally raised disqualifiers of its own — most consequentially a **new material
population**: this continuation located six real `ir_module_module` registries and a
production-scale database that pass 1 did not know existed, and the package had asserted their
non-existence (`39 RE-07`). Under `EC-07`'s own terms, discovering a material population resets the
counter rather than advancing it.

| Disqualifier | Raised in pass 2? | Evidence |
|---|---|---|
| New material population | **YES** — six module registries; 183,590 journal entries; 5,201 certificates | `24`, `25` |
| New material finding class | **YES** — empirical confirmation is a class the package did not previously hold, and the severity inversion is new | `25 §3`, `26 §5` |
| New gating unknown | **PARTLY** — `U-01`/`U-02` narrowed rather than added, but the v18-target residue is newly named | `24 §5`, `25 §6` |
| Reopened tolerance-zero issue | **NO** — none reopened; reach was re-classified, none closed | `26` |
| New Gate-changing contradiction | to be measured | `36 §5` |
| Evidence-integrity failure | **YES** — `RE-07`: the package asserted evidence did not exist when it did | `39` |

## 5. Status

> **`EC-07`: NOT SATISFIED — the counter reads 0 of 2.**
> Blocker classification: **INTERNAL**. It is not waiting on an external party. It requires two
> further consecutive independent passes that each complete clean — which in turn requires the
> underlying instability to stop, i.e. no new material population and no new finding class.
>
> The most likely remaining source of a new material population is the one named in `24 §4`: an
> Odoo 18 database carrying the P05 surface. Until that is either produced or shown not to exist,
> a future pass can still reset the counter.

## 6. Honest Note on Trajectory

The counter has not merely failed to advance — the two passes so far have each *found more* than the
one before, which is the signature of research that has not converged. Pass 1 found 60 findings the
author missed. Pass 2 found an entire evidence class the author had declared non-existent. That is
the relevant signal for `EC-02` as well as `EC-07`, and it is recorded here rather than left to be
inferred from a table.
