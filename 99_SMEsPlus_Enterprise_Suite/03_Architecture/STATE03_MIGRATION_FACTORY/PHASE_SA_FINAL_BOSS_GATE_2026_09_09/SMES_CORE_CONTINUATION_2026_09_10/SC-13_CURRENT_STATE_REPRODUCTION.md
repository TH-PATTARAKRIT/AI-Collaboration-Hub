# SC-13 — CURRENT STATE REPRODUCTION

## `CP-SA-SC-110 — CURRENT STATE REPRODUCED`

Session `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · Branch `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Baseline cited by the prompt `89ba9c7d` · **Head consumed by this round `ce987553`**
Prompt `04_…GAP_REMEDIATION_AND_REMAINING_DECISION_PROMPT.md` (`a8c7054f`)
**Boss is the SOLE FINAL APPROVER. Checkpoint completion is not Boss approval.**

**Prompt §2: *"Do not force those counts. Reproduce them before use."* Twelve items were put to
reproduction. Eleven reproduce. One does not, and it is item 1.**

---

## 1. ⚠ Item 1 — `FG-F-06 = READING B` DOES NOT REPRODUCE

**Two opposed Boss rulings on `FG-F-06` exist on this branch.**

| Record | Ruling | Head cited | Commit |
|---|---|---|---|
| `SC-BD-01_FG_F06_BOSS_RULING.md` | **`READING B` — does not bind this exit** | `6d08bcc5` | `e113258f` |
| `SC-CONTRA-01_FG_F06_READING_A_AND_GATE_CONTRADICTION.md` | **`READING A` — binds this exit** | `7eeb5d8e` | `ce987553` |

**Both were filed after Boss instructions to two executors. Neither executor could cite the other's.**

**`SC-CONTRA-01` arrived after the `04_` prompt was written** (`ce987553` at 08:23:35 vs `a8c7054f` at
08:21:29), so the prompt's §2 item 1 could not have accounted for it. **§2 item 1 is therefore not a
reproducible fact at this head; it is one side of an open contradiction.**

### 1.1 What this round refuses to do about it

**It does not choose.** `EC-05` requires a material contradiction to be *dispositioned*; `CF-D-01` fixes
who may: *"only Boss may state what a Boss ruling covers."* A later commit timestamp is evidence about
when a record was written, **not** about which instruction Boss intends to stand.

**It also does not stall on it.** Everything in §§3–9 of the prompt is **team work that SMEs Core owes
under either reading** — a recommendation is not a ruling, and a specification is not a gate. That work is
executed. **Only the §10 ruling interface is withheld**, because presenting decisions for ruling
presupposes a gate whose precondition is disputed.

## 2. The eleven items that do reproduce

| # | Item | Instrument A | Instrument B | Result |
|---:|---|---|---|---|
| 2 | `BOSS-ROUTE-01 = CLOSED — ROUTE = SC` | `SC-08` §1 | `SC-BD-01` §2 / resume state | **reproduces** |
| 3 | 23 decisions total | `SC-11` §2 family-total column | sum of the eight per-family rows | **23 = 23** |
| 4 | 16 ruled | `SC-11` §2 | count of `SC-BD-02`…`SC-BD-09` family records = **8 families**, member-level sum = 16 | **reproduces** |
| 5 | 7 open | `SC-11` §2 | 23 − 16 | **reproduces** |
| 6 | exact open-ID list | `SC-11` §2 | `SC-12` §2 row-by-row | **`POH-D-01` `POH-D-02` `POH-D-03` `POH-D-04` `POH-D-05` `RC-D-03` `RC-D-04`** — 7 ids, both shapes identical |
| 7 | Category 3 = 1, SMEs Core-owned | `SC-12` §5 | `SC-BD-F-01` in `SC-11` §3 | **reproduces** — reason: `RC-D-03`/`RC-D-04` carry no recommendation |
| 8 | 6 vetoes / 0 discharged | distinct ids in `SC-04` | distinct ids in `SC-11` §4 | **`AAS-V-01` `AAS-V-02` `AAS-V-03` `RC-V-01` `CF-V-01` `CF-V-02`** — 6 both shapes |
| 9 | acts approved: `B-7`, `C4-D-01`, `C4-D-02`, Thai panel | `SC-BD-10` §2 | `SC-11` §5 | **reproduces — 4** |
| 10 | `AAS-V-02` ratification not selected | `SC-BD-10` §3 | `SC-12` §3 | **reproduces** |
| 11 | `POH-D-06` ruled, AAS+ concurrence still required | `SC-BD-06` §6 | primary source `POH-F-06` L211–212 | **reproduces at primary text** |
| 12 | Pre-Test not started | `SC-05`, `SC-12` §8 | no Pre-Test artefact exists on the branch | **reproduces** |

## 3. Controlling artefacts unaltered by `SC-CONTRA-01`

| Shape | Instrument | Result |
|---|---|---|
| 1 | `git diff --name-only 89ba9c7d..HEAD` over `SC-BD-*`, `SC-08`…`SC-12` | **0 files changed** |
| 2 | blob identity of `SC-BD-01` | `7996b707` at `89ba9c7d` **and** at `HEAD` — **identical** |

**`SC-CONTRA-01`'s claim not to have touched them is verified, not accepted.**

## 4. `SC-GAP-F-01` — a correction to this session's own `SC-BD-03`

**`SC-BD-03` §6 and `SC-06` line 214 record that `CF-V-02`'s *first limb closes* on the `MTI-D-04` ruling.
That is overstated, and primary source says so.**

`SA_CORR5_09_VETO_RECONCILIATION.md` **line 37**, the veto's own release path, verbatim:

> *"**`MTI-D-04` + `RC-D-04` ruled and the mapping layer specified** (lifts the first limb); **`RC-D-03`
> ruled and Private Company escalation criteria stated** (second limb)"*

and its status cell: *"**`STILL ACTIVE`** — a wording control on two root causes whose closure is
**Boss-gated** (`RC-F-03` → `MTI-D-04`/`RC-D-04`; `RC-F-07` → `RC-D-03`)."*

| | `SC-BD-03` / `SC-06` said | Primary source requires |
|---|---|---|
| `CF-V-02` limb 1 | *"first limb closes"* on `MTI-D-04` | `MTI-D-04` **and** `RC-D-04` ruled **and the mapping layer specified** |
| `CF-V-02` limb 2 | not addressed | `RC-D-03` ruled **and Private Company escalation criteria stated** |

> ### `CF-V-02` LIMB 1 IS **NOT** CLOSED. Three conditions are required and one is met.

**Root cause:** `SC-BD-03` inherited `SC-06`'s consequence clause without checking it against the veto's
own release path — the unmeasured-consequence-clause class. **`SC-BD-03`'s §6 heading claim
(*"NO VETO IS DISCHARGED"*) was and remains correct**; what was wrong is the narrower *"first limb closed"*
statement inside it. **No veto count changes: 6 in force, 0 discharged.**

**Consequence, and it is the reason this round's work matters:** the release path names **two SMEs Core
*specification* obligations** — *"the mapping layer specified"* and *"Private Company escalation criteria
stated"*. **Those are exactly `SC-15` and `SC-14`.** Ruling `RC-D-03`/`RC-D-04` alone would not lift either
limb; the specifications must exist too.

## 5. Checkpoint

> ## `CP-SA-SC-110 — CURRENT STATE REPRODUCED, WITH TWO EXCEPTIONS PUBLISHED`
> **11 of 12 items reproduce on two shapes each · item 1 `FG-F-06 = READING B` **does not reproduce** —
> two opposed Boss rulings coexist and only Boss may disposition them (`EC-05`) · controlling artefacts
> verified byte-identical · **`SC-GAP-F-01`**: `CF-V-02` limb 1 is **not** closed, correcting this
> session's own `SC-BD-03` against primary source.**
