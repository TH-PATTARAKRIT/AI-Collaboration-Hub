# SA_AR_R2_04 — `SC` INTAKE CONFORMANCE CHECK

Session `[SMEPLUS-26-09-09-PHASE-SA-AUTHORITY-RESOLUTION-001]` — round 2, post-ruling addendum
Subject: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` at **`2139088b`** (2026-09-10 01:09:38 +0700),
`TERMINAL A — READY FOR BOSS PHASE SA FINAL DECISION`, deliverables `SC-00` … `SC-06`.
**This checks one thing only: Boss's binding intake condition. It is not a review of the `SC` package.**

---

## 1. The condition

Boss ruled `BOSS-ROUTE-01 = SC`, and:

```
SC track MUST consume afe664c6 (AR-F-01, AR-F-02) as input = YES
```

**The `SC` package was published *before* that ruling was given.** It could not have known, exactly as
round 1 could not have known of the `SC` authorization. **No fault attaches to either round.** This note
exists so the condition can be met going forward, not to allocate blame.

## 2. Citation measurement

`git grep -F -c <token> 2139088b -- '<SC package>/*'`

| Token | Hits |
|---|---:|
| `afe664c6` | **0** |
| `AR-F-01` | **0** |
| `AR-F-02` | **0** |
| `SA_AR_` | **0** |
| `AUTHORITY-RESOLUTION` / `AUTHORITY_RESOLUTION` | **0** |
| `b1f07939` | **0** |
| **Positive control** `9d5bc2db` | **10** |
| **Positive control** `F3` | **45** |
| **Positive control** `SMT` | **91** |

**The controls fire.** The zeros are real: the `SC` package cites no artefact of the `AR` round.

## 3. `AR-F-01` — **NOT a defect in `SC`. Independently and better handled.**

The working hypothesis on opening this check was that `SC` had inherited the parent's **26** and repeated
the `F5` count-by-identifier error for a fourth round. **That hypothesis is wrong and is recorded here as
wrong.**

`SC-01` §1.0 — *"The count unit, declared before any number"* — states the unit **before** the total,
names **both** readings present in the parent, and says why it chose the one it chose:

> *"On that unit `F5` is **8** (three restatement subjects plus `POH-D-01`…`POH-D-05`), **not** the
> 'six decisions' its own family card states. **The two readings are both in the parent and they
> differ**; this register uses the one the 26 is built from, so the delta is comparable. Mixing them is
> the programme's recorded count-unit-vs-population defect and is the reason the unit is declared before
> the total rather than after it."*

**That is the control working, not failing.** `AR-F-01` and `SC-01` §1.0 identify the *same* contradiction
in the parent from opposite ends and make **different, each-declared** choices:

| | Unit chosen | `F5` | Total | Rationale |
|---|---|---:|---:|---|
| `AR-F-01` | **decision**, per the primary register `SA_CORR3_03` | **6** | **24** | the register defines six decisions and no more |
| `SC-01` §1.0 | **atom, as `SA_FINAL_02` §2/§3 counts them** | **8** | **26 → 25** | comparability of the delta against the parent |

**Both are defensible and they are not the same number.** `SC-06`'s headline **25** is on the `SC` unit;
on the `AR` unit the same population is **23**. **Boss should be told which unit a headline is on** —
that, not either number, is the finding.

**No correction is proposed to `SC` on this item.**

## 4. `AR-F-02` — **materially unconsumed, and it lands on a live Boss card**

This one is a real gap.

Both rounds cite the same single Phase SA precedent, `SA_CORR3_07`, on the `FG-F-06` scope question —
**and they read it at different depths**:

| | Reading of the precedent | Effect on Reading A |
|---|---|---|
| `SC-04` line 157, as a **ground for Reading A** | *"`SA_CORR3_07` has already applied this constitution to grade a Phase SA package `PROVISIONAL / NON-CANONICAL`"* — **concept level** | **strengthens** it |
| `AR-F-02` (`SA_AR_05` §3.4) | that phrase is **§9, the AAS+ / Design Handoff Rule** — *"AAS+ may explore designs in parallel only as `PROVISIONAL / NON-CANONICAL` while parent Very Deep Research is not yet complete"* — **not §4's Module Exit Rule and not `EC-07`** — **clause level** | **weakens** it |

**`SC-04` §6 puts the `FG-F-06` scope card to Boss with the precedent on the Reading A side of the
ledger, unqualified.** Under `AR-F-02` that precedent does not reach §4 or `EC-07` at all — it is
evidence that the constitution was applied to Phase SA **in a different clause**, for a different
purpose.

**What turns on it:** under Reading A, `EC-07` requires two consecutive clean independent passes,
**zero** have occurred, and `SC-04` line 158 correctly records that `B-7` then becomes **gate-blocking**
rather than merely valuable. The precedent is one of the load-bearing supports for that reading.
**Boss is being asked to rule `FG-F-06` on a ledger where one support is stated at concept level and its
clause-level narrowing is absent.**

### Recommended correction — for the `SC` track's owner, not applied here

Add `AR-F-02` to the `SC-04` §6 card on the **Reading B / "what weakens Reading A"** side, in one line:

> *The single Phase SA precedent `SA_CORR3_07` applies **§9** (AAS+ / Design Handoff, `PROVISIONAL /
> NON-CANONICAL`), **not §4's Module Exit Rule and not `EC-07`**. It shows the constitution touching
> Phase SA, not that `EC-07` binds a Phase SA exit.*

Both rounds already agree on the conclusion that matters — **`AR-F-02`'s own §3.4 records
*"Neither reading is unreasonable, and the text does not settle it"*, and `CF-D-01` fixes who resolves
it: *"only Boss may state what a Boss ruling covers."*** The gap is the completeness of the ledger Boss
rules on, not the recommendation.

## 5. Result

| Intake item | State |
|---|---|
| `AR-F-01` — decision count / `F5` unit | **satisfied in substance by an independent, declared treatment.** No correction proposed. Boss should be told the headline's unit: **25 on the `SC` unit, 23 on the `AR` unit** |
| `AR-F-02` — the precedent applies §9, not §4 / `EC-07` | **NOT consumed. Material.** Lands on the `FG-F-06` card `SC-04` §6 that Boss is being asked to rule |
| PMO closure re-measured at head | `SC-00` re-measured independently — **satisfied** |
| Four published instrument failures | not cited; **no observed consequence** in the `SC` package |

> ### `1 of 2 named intake items is materially unconsumed.`

**Nothing in the `SC` package is withdrawn or contradicted by this note**, and no `SC` deliverable was
modified. `2139088b` is another session's branch and was **read only**. This note is published on the
`AR` control branch, which this session owns.
