# P10 — ASSET POPULATION AND EXPOSURE CORRECTION

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Corrections `P10-R-12` and `P10-R-13`, raised **during** this round and against this round's own documents.

---

## `P10-R-12` — the asset count mixed two units

| | |
|---|---|
| **Written** | *"769 asset schedules across the estate"* — in `22`, `34` `W-14`, `43`, `44`, and in the correction that replaced the earlier *"zero recognition entries"* claim |
| **Wrong because** | The row count includes records whose state is **`model`** — asset **templates**, not assets. It was a count of rows presented as a count of schedules |
| **Prompted by** | A peer delta whose commit subject reads *"a peer's warning overturned a negative finding — the v18 line has no assets at all"*. P10 tested it against its own extracts and the peer is right |
| **The corrected figures** | |

| DB | Rows | `model` | Real assets (`open`/`close`/`draft`/`cancelled`) |
|----|------|---------|--------------------------------------------------|
| A | 36 | **36** | **0** |
| B | 36 | **36** | **0** |
| C | 685 | 16 | **669** — 664 open, 2 closed, 2 draft, 1 cancelled |
| D | 12 | **12** | **0** |
| **TOTAL** | 769 | **100** | **669, all in one database** |

**Three of four deployed databases contain no assets at all — only templates.** The 769 figure was a row count; the schedule count is 669, and its distribution is the opposite of what "across the estate" implies.

**This is the programme's count-unit defect, committed in `43`, in a section that declares the unit before use and congratulates itself for doing so.** Declaring a unit for the *database* denominator did not stop a different unit being conflated two sections later.

## `P10-R-13` — `TZ-1` was closed on a three-of-four population

| | |
|---|---|
| **Written** | `49` `TZ-1`: **CLOSED — EVIDENCE VERIFIED.** *"No recognition entry has been re-dated anywhere in the readable population"* |
| **Wrong because** | The probe ran against A, B and D. **C was never probed** — and C is the only database with real assets. A closure over a population that excludes the only populated member is not a closure |
| **Found by** | P10, while following the same peer delta that produced `P10-R-12`. Not by a challenge |

**What probing C actually shows:**

| Probe | C | Artefact |
|-------|---|----------|
| Journal entries | **183,590** | 91,957,095 bytes |
| Entries carrying an asset link | **30,038** | same |
| Of which posted | **17,513** | same |
| With both a date and a period-beginning date | **30,032** | same |
| **Date year later than period-beginning year** | **3** | same |
| Positive control — rows with a populated date | 183,590 of 183,590 | same |

The three: all posted, all dated `2025-09-30`, with period-beginning dates in October and December **2024**.

## The Finding, Stated Honestly

**Three entries carry the signature a re-date would leave. That signature is not diagnostic.**

Two mechanisms produce it:

1. **A re-date** — the entry's date was moved forward, away from the period it belongs to. A defect.
2. **A legitimate catch-up stub** — the asset engine deliberately cuts a stub entry at a modification date, covering a period that began earlier. **Correct behaviour, and it leaves exactly the same trace.**

**C has no lock date set on its single company**, so the lock-triggered path cannot have produced them. That leaves the legitimate catch-up as the likely explanation and the **lock-free** mutation path as the other candidate.

Distinguishing them requires the modification history of the three assets, which has not been read.

> **Classification: `UNRESOLVED — EVIDENCE REQUIRED`.** Three candidate signatures in 30,032 asset-linked entries. Not evidence of a defect; not evidence of its absence.

## Corrected `TZ-1` Status

> **`TZ-1`: PARTIAL — not closed.**
>
> - A, B, D: no lock, and **no recognition entries of any kind** — nothing could have been re-dated. `FACT VERIFIED`.
> - C: 30,032 asset-linked entries, **3 candidate signatures**, cause undetermined, no lock present. `UNRESOLVED — EVIDENCE REQUIRED`.

The prior statement — *closed, negatively, across the whole readable population* — is withdrawn.

## What Survives Unchanged

- **No deferral entry exists in any deployed database.** `FACT VERIFIED`, four of four.
- **1 of 90 companies has any period lock configured.** `FACT VERIFIED`.
- The lock-triggered re-date is **NOT REACHABLE** in A, B and C and **DORMANT** in D. Unchanged, and now stronger: D has no assets either.
- The capability-versus-exposure separation at `45` stands; only the asset row in its supporting data changes.

## Method Note

Both corrections came from **following a peer's commit subject into P10's own already-extracted data**. Neither needed new evidence — `P10-R-12` needed a column P10 had extracted and not grouped, and `P10-R-13` needed a probe P10 had written and not run against the fourth archive.

That is the `EVIDENCE EXTRACTED ≠ EVIDENCE REVIEWED` rule of `46` firing against the round that wrote it, **twice**, within hours.
