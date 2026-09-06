# P10 — RECOGNITION PERIOD vs POSTING DATE  (`CQ-P10-02`)

**Terminal disposition: `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** for the four semantics and the lock behaviour · **`BOSS DECISION REQUIRED`** for whether a posting constraint may alter a recognition period.

---

## 1. The Four Concepts, Separated

| Concept | Definition | Carrier in the reference | Owner |
|---|---|---|---|
| **Economic / recognition period** | The period an amount economically belongs to, derived from base, window, grid and convention | **none for deferrals** — only the period *end*, as the entry's date. **Depreciation carries a period-beginning date** | `P10` |
| **Scheduled date** | The date the schedule says the entry should carry | the entry's date at creation | `P10` |
| **Accounting posting date** | The date the entry actually carries when posted, against which locks, sequences and hashes evaluate | the same field | `P08` |
| **Lock date** | The boundary past which posting is constrained | five named company fields; recognition entries post to general journals and carry no tax, so **only the fiscal-year lock and the irreversible lock ever bind them** | `P08` |

> **For deferrals, three of these four concepts share one field.** That is the collapse, stated precisely.

## 2. Lock Behaviour — `REFUSE` / `RELOCATE` / `PROCEED`

| Path | Behaviour | Tested? |
|---|---|---|
| Deferral, grouped generation | **REFUSE**, with an explicit error | **yes** — a dedicated test asserts the refusal |
| Deferral, validation generation | **RELOCATE** — the date is silently overwritten by the shared posting routine | a test **exercises** this path under a lock and **asserts only the entry count, not the dates** |
| Asset board | **RELOCATE** | **yes — and the test asserts the relocation as the expected result** |
| Asset disposal | **REFUSE** | present |
| Accrual | **RELOCATE** (no pre-check of its own) | none |
| Loan | **PROCEED / RELOCATE** (no lock handling of its own) | none |

**The positive control, and its exact strength:** an executed test shows a charge scheduled for the last day of 2020 posting as the last day of July 2021 under a mid-2021 fiscal-year lock — so **one fiscal year shows nothing and the next shows double**. The test's *stated subject* is changing a computation method with draft moves before a lock; **the relocation is recorded incidentally, while testing something else**. That is decisive for *specified, not accidental*, and weaker than *the vendor asserts a misstatement as correct*.

**The relocation is not one convention.** The landing period is selected by the journal's **sequence numbering format** — a month-reset sequence lands at that month's end, a year-reset sequence lands at **31 December**. Same lock, same charge, different period, decided by a non-accounting attribute.

**And the silence is a choice.** The same routine posts a chatter message **six lines above** the relocation branch, announcing a deferred accounting date. Recording the original period the same way costs nothing another process owns.

## 3. Does a Posting Constraint Alter the Recognition Period?

**In the reference: yes, silently, and irreversibly** — reopening a period re-derives nothing.

**For SMEsPlus: `BOSS DECISION REQUIRED`.** Six options are classified without choosing; the full statement with evidence for and against each is at the prior round's `39` and `40` and is not restated here.

Two constraints on the decision, both of which changed since the prior round:

1. **The peer boundary that would exclude the status quo is an OPEN blocker**, status `HOLD — BOSS DECISION REQUIRED`. `UNRESOLVED != ADOPTED`. The status-quo option is therefore **restored and live**, conditionally excluded only if the Boss adopts that boundary.
2. **That boundary's close condition has been refined**: where a mutation path has **no violation to detect**, an attributable trace is **mandatory, not alternative** — because a second mutation path fires with **no lock configured**, so there is nothing to refuse. **Refusal alone is not a complete answer.**

## 4. The Correction That Governs the Design

**Carrying the period is necessary and not sufficient.**

Depreciation **carries** its period-beginning date and is **still silently relocated**, because the lock evaluates the posting date and nothing reads the period. A design can hold the field and never consult it — which is what the reference does today.

> **Requirement:** a recognition period must be **carried** *and* the divergence between period and posting date must be **reportable and reconcilable**. The first without the second reproduces the defect with better data.

## 5. Deployed Reachability — measured, and it changes the decision's character

| | |
|---|---|
| Companies with any period lock | **1 of 46 distinct companies** (1 of 90 company-rows) |
| That company's database | 10 journal entries in total, **no recognition entries, no assets** |
| Databases with production volume | **one**, and it has **no lock** |
| Candidate relocation signatures found | **3** in 30,032 asset-linked entries — all posted, all one date, period-beginnings months earlier |

**Those three are not diagnostic.** A legitimate catch-up stub, which the asset engine deliberately cuts at a modification date, leaves the identical trace. Distinguishing them needs the modification history of three assets, which was not read. **`UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`.**

> **The Boss is not choosing how to remediate a live misstatement. On the lock path there is nothing live to remediate in the four databases examined.** That makes the disruptive options cheaper and the decision earlier than the prior round implied — and it says nothing about the **lock-free** path, which needs no configuration and whose exposure is unknown.

## 6. Disposition

- The four semantics and their carriers: **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**
- Lock behaviour classified `REFUSE`/`RELOCATE`/`PROCEED` per path: **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**
- Whether a posting constraint may alter a recognition period: **`BOSS DECISION REQUIRED`**, coupled to the peer boundary and to `D-5`
- Whether the three candidate signatures are relocations: **`UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`**
