# P10 — LOCK-DATE EXPOSURE RECALCULATION

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoints `CP-P10D07` and `CP-P10D11` (obtainable EC-04 work).

---

## 1. Denominators, Declared Before Use

| Denominator | Value |
|-------------|-------|
| Distinct deployed databases | **4** |
| Databases readable | **4** |
| Databases examined for lock dates | **4** |
| **Company-rows across the four images** | 90 (44 + 44 + 1 + 1) |
| **Distinct companies** | **46** — **CORRECTED, `67` §1.** Two databases hold **identical company sets** (intersection 44); they are two restores of one tenant lineage |

The prior round said *"all 44 companies"* and *"the entire deployed estate"*. The estate is **90 companies in four databases**, of which 88 are in two databases and 2 are single-company databases.

## 2. Lock-Date Population — executed, with positive control

| DB | Companies | With a fiscal-year lock | Without | Other lock fields |
|----|-----------|------------------------|---------|-------------------|
| A | 44 | **0** | 44 | all five lock columns unset in all 44 |
| B | 44 | **0** | 44 | all five unset in all 44 |
| C | 1 | **0** | 1 | **CORRECTED, `67` §6 `P10-R-19`:** three lock columns **do** exist here, including a differently-named period-lock field found on no other archive. The zero is real; the earlier explanation was false |
| **D** | **1** | **1** | 0 | fiscal-year, tax, sale and purchase all set to the same date; the irreversible hard lock **unset** |
| **TOTAL** | **90** | **1** | **89** | |

**Positive control — CORRECTED, `67` §4 `P10-R-17`.** This control was **asserted and never executed**: the shipped probe prints the lock columns and the row count, and no sibling column or sample value. **Both challenge classes supplied it independently and the zeros are read zeros** — creation timestamp, name and currency populated 44 of 44, and a **lock-family sibling** populated in every row of every archive. The conclusion stands on someone else's control.

**1 of 46 distinct companies** — equivalently **1 of 90 company-rows across four database images** — carries any period lock.

Both statements are true and they use **different units**. The earlier bare *"1 of 90 companies"* conflated them, which is the programme's own count-unit defect committed in the document written to repair a denominator.

**Independently re-derived by two challenge classes** across the four archives **plus three additional snapshots**, all agreeing. **FACT VERIFIED.**

## 3. Has the Defect Actually Fired? — the obtainable EC-04 work, executed

The lock-triggered re-date can only have occurred where a lock exists. That is **one company, in database D**. So the question reduces to: does D contain any scheduled recognition entry whose date was moved?

**Executed against D:**

| Probe | Result | Artefact |
|-------|--------|----------|
| Total journal entries | **10** | 7,967 bytes |
| Entries carrying an asset link | **0** | same |
| Entries with both a date and a depreciation period-beginning date | **0** | same |
| Entries whose date year differs from their period-beginning year | **0** | same |
| Entries dated after the lock whose period began on or before it | **0** | same |
| Deferral entries | **0** | 913 bytes, header only |
| **Positive control** — rows with a populated date | **10 of 10** | same |

> **CORRECTED — `P10-R-13`, see `52`.** This section first read: *"`P10-U-20` is CLOSED, negatively, across the whole readable population."* **The probe had not been run against database C**, which is the only database holding real assets. A closure over a population excluding its only populated member is not a closure.
>
> **`P10-U-20`: PARTIAL.**
> - **A, B, D** — no lock, and **no recognition entries of any kind**. Nothing could have been re-dated. `FACT VERIFIED`.
> - **C** — 183,590 journal entries, **30,038 carrying an asset link**, **3** whose date year is later than their period-beginning year, all posted, all dated the same day. C has **no lock**, so the lock path cannot have produced them; a legitimate catch-up stub produces the identical signature. `UNRESOLVED — EVIDENCE REQUIRED`.

This remains genuine EC-04 progress — the question moved from unobtained to partially answered with a stated denominator and positive controls — but it is not a closure.

## 4. Recognition Mechanism Presence vs Entry Presence

| DB | Deferral mechanism installed | Deferral entries | Asset schedules | Asset entries |
|----|------------------------------|------------------|-----------------|---------------|
| A | yes, configured in 43 of 44 companies | **0** | **0** (36 templates) | not counted — `C` |
| B | yes, configured in 43 of 44 | **0** | **0** (36 templates) | not counted — `C` |
| C | **no — absent from the schema** | n/a | **669** (+16 templates) | **30,038**, 17,513 posted |
| D | yes | **0** | **0** (12 templates) | **0** |

**The deferral mechanism has never generated an entry anywhere in the readable estate.** The asset mechanism has **669 real assets, all in a single database**, which holds 30,038 asset-linked entries and **no lock date**. The other three databases hold asset **templates only** and no assets at all.

## 5. What This Does and Does Not Change

**Does not change:** the source finding. The re-date behaviour exists in code, is specified, and is recorded by an executed test on the asset mechanism. Nothing here softens that.

**Does change:** every statement in the prior package about *live exposure*. There is none, on the lock path, anywhere in the readable estate.

**Does not reach:** the **lock-free** mutation path, which by construction needs no lock. This recalculation says nothing about it, and the peer's own refinement makes it the more important of the two. Recorded as unresolved.
