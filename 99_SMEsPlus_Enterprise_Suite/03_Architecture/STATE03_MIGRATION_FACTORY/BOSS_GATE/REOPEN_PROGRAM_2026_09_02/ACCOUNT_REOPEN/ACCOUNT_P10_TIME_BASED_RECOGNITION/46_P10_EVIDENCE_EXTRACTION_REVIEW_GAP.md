# P10 — EVIDENCE EXTRACTION / REVIEW GAP

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D09` (part 1).

---

## 1. The Instance

The prior round's shipped probe extracted the **company table** from every readable archive. That table contains all five period-lock columns. The probe then reported, for each archive, **the artefact's byte size** and nothing else.

The question *"is the silent re-date reachable in the deployed estate?"* was answered by those columns. It was recorded instead as `P10-U-20`, *"obtainable and not obtained"*, and the package went on to assert live exposure that the same columns disprove.

**The evidence was extracted, retained, and never read.**

## 2. The Five-Stage Forensic

| Stage | What happened |
|-------|---------------|
| **Extracted** | The full company table of three archives — 195, 188 and 141 columns wide — including `fiscalyear_lock_date`, `hard_lock_date`, `tax_lock_date`, `sale_lock_date`, `purchase_lock_date` |
| **Retained** | Written to disk as artefacts of 1.6 MB, 1.5 MB and 42 KB. Still present |
| **Displayed** | For the lock columns: **nothing**. The probe printed the artefact's byte size as an emptiness control, plus four deferral-configuration columns it had been written to look for |
| **Inspected by the author** | Only what was displayed |
| **Conclusion drawn from display rather than from retained evidence** | *"The deployed estate runs the path that silently re-dates, in every one of the 44 companies examined"* — a claim about lock-driven behaviour, drawn from a display that contained no lock data |

## 3. Why the Existing Control Did Not Catch It

The byte-size control was adopted from a peer's lesson, and it is a good control **for what it controls**: it distinguishes an empty extraction from an empty table.

It says nothing about whether a human or a probe ever looked inside. A 1.6 MB artefact and a 1.6 MB artefact whose relevant column was never printed are indistinguishable to it.

> **The control proved the evidence existed. Nothing proved the evidence was read.**

## 4. The Rule

> **`EVIDENCE EXTRACTED ≠ EVIDENCE REVIEWED.`**
>
> For every question a probe is run to answer, the probe must **print the field that answers it**, or the record must state explicitly that the field was extracted and not inspected.
>
> A byte-size control proves an extraction is non-empty. It is not evidence that anything was read, and it may not be cited as though it were.

## 5. Why This Is a Distinct Defect Class

| Defect | What is missing |
|--------|-----------------|
| `R-08` | The search — the evidence was never obtained |
| **This** | The reading — the evidence was obtained and not looked at |
| Declared-pattern-not-run | The execution — the declared search was narrower than stated |
| Executed-not-quoted | The publication — the search ran and its output was not published |

Four distinct failures, all of which produce the same symptom: **a confident claim with no evidence behind it and an artefact that looks like evidence.** A package can satisfy any three and commit the fourth.

## 6. Retrospective Application

| Probe | Question it was run for | Field that answers it | Printed? |
|-------|------------------------|----------------------|----------|
| Company table extraction | Deferral configuration | four configuration columns | **yes** |
| Same extraction | Lock reachability | five lock columns | **no** — the defect |
| Deferral relation extraction | Have deferral entries been generated? | row count | yes, with size |
| Asset table extraction | *not run in the prior round* | — | — |
| Schema extraction | Which structures exist? | probe hit counts | yes |

One of five. The failure was not systemic in the probe design; it was that **the probe was written for one question and its output was used for another**.

## 7. Applied Going Forward

Every probe shipped in this round prints the field that answers its question, and every unread extraction is declared. `43` §5 lists four such declarations rather than leaving them silent.
