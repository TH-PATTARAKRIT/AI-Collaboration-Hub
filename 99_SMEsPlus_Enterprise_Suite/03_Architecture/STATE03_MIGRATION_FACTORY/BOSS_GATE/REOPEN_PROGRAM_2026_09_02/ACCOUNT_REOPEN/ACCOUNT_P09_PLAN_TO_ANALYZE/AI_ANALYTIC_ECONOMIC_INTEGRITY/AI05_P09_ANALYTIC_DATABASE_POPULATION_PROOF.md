# AI05 — P09_ANALYTIC_DATABASE_POPULATION_PROOF

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Layer:** 1 — clean-room.

> ## ⚠ THIS DOCUMENT WAS REWRITTEN AFTER ITS FIRST VERSION WAS CONTRADICTED
>
> The first version concluded: *"In every deployment for which real data was located, no asset carries an analytic allocation at all"*, and framed the defect as **latent and armed**.
>
> **That was wrong, and the error was in the evidence base, not the reasoning.** An independently tasked reviewer found a deployed database dump the evidence strand had missed. The research team then re-ran the extraction directly.
>
> **The defect is observed, historical, and at scale.** The corrected measurement is in §3.

---

## 1. THE EVIDENCE-BASE FAILURE, STATED FIRST

The first version declared nine artefacts and **two** usable database dumps. **There are four dumps in one directory alone**, and the largest of them — 155 MB, the only one containing a populated accounting deployment — was not among them.

**Root cause, identified exactly:** the evidence strand's own listing command ended in `| head -100`. The directory holds **2,553 files**. The truncation silently removed the artefact that mattered. **The command ran, returned a result, and the result was a false negative produced by the command's own tail.**

This is the programme's `evidence-base-is-itself-a-claim` failure mode, recurring — and this time the defeat was not a wrong path or a wrong pattern but a **display limit**. A negative result must be produced by a search that could have returned the positive.

**No conclusion drawn from the first version's population statement survives.**

## 2. THE CORRECTED ARTEFACT INVENTORY

| # | Artefact | Assets | Carrying an allocation | Usable? |
|---|---|---|---|---|
| 1 | **deployment `S`** — 155 MB custom-format dump | **685** | **670** | **YES — decisive** |
| 2 | deployment `B` — 35 MB | 36 | 0 | template-only |
| 3 | deployment `E` — 24 MB | 36 | 0 | template-only |
| 4 | deployment `T` — 64 MB | — | — | **NOT DECIDABLE** — the local restore client rejects its header version |
| 5–9 | traces, workbooks, handoff documents, an unrelated schema script | — | — | as previously recorded |

**Correction of record:** the first version stated *"asset rows in those dumps: 12 and 12"*. The correct figure for artefacts 2 and 3 is **36 and 36**. The substance for those two — all category templates, no allocations — holds; the count did not.

## 3. THE MEASUREMENT — RE-RUN BY THE RESEARCH TEAM, NOT ACCEPTED ON REPORT

Extraction performed directly by the author against deployment `S`, read-only, after the reviewer's claim:

| Quantity | Value |
|---|---|
| asset records | **685** |
| **carrying an allocation** | **670** — 664 open, 2 closed, 2 draft, 1 template, 1 cancelled |
| journal rows | 447,384 |
| **management records** | **339,382** |
| allocation rules configured | 1,327 |
| distinct accumulated-depreciation accounts in use | 10 |
| distinct depreciation-expense accounts in use | 19 |

**The decisive test** — the direct observable the zeroing theorem predicts, grouping management records by the general account of each leg:

| Leg | Records | Sum |
|---|---|---|
| accumulated depreciation (**balance sheet**) | **17,716** | **+101,778,591.13** |
| depreciation expense (**profit and loss**) | **18,483** | **−104,739,812.94** |
| **NET** | | **−2,961,221.81** |
| **GROSS** | | **206,518,404.07** |

> ### **98.57 % of the depreciation attribution in this deployment is annihilated.**

The sign pattern matches the symbolic trace exactly: the balance-sheet leg positive, the expense leg negative. The reviewer additionally identified three analytic accounts netting to **exactly 0.00** with matched record counts (221/221, 564/564, 99/99) — clean symmetric-pair witnesses.

**Classification: `FACT VERIFIED` against deployed data.** Not a code-path conclusion, not a projection, not latent.

## 4. WHAT THIS CHANGES

| First version said | Corrected |
|---|---|
| the precondition is **not present** in any deployment | it is present on **670 of 685** assets in a real deployment |
| the defect is **latent and armed** | the defect is **firing, historically, at scale** |
| *"the question does not arise"* for historical correctness | **17,716 historical management records are annihilating 18,483 others**, and the population is identifiable |
| `HOLD — DATABASE EVIDENCE REQUIRED` | **CLOSED BY EVIDENCE.** `DEP-P09-14` is discharged |
| the no-allocation branch is *"the ordinary state"* | contradicted — this deployment carries **1,327** allocation rules |

**The retrospective-identification requirement changes character.** It was a design requirement for a future system. It is now a **remediation obligation over an existing, measurable population**, and P09 can state its size.

## 5. WHAT IS STILL OPEN

| ID | Item | Class |
|---|---|---|
| `DEP-P09-23` | deployment `T` — restore client rejects the header version | **NOT DECIDABLE** with the local client |
| `DEP-P09-24` | per-period attribution: join the management record dates to fiscal periods and quantify the period-level understatement | **DATA AVAILABLE, NOT YET RUN** |
| `DEP-P09-25` | explain two large one-sided analytic balances and a small offset observed by the reviewer — distribution edits, a plan migration, or a further mechanism | **UNRESOLVED** |
| `DEP-P09-26` | the same measurement for the other four symmetric mechanisms in this deployment | **DATA AVAILABLE, NOT YET RUN** |

**These are now data questions with the data in hand, not evidence-acquisition questions.** That is a materially better position than the first version described, arrived at by being wrong in public.

## 6. THE STANDING RULE THIS SESSION ADDS

**A negative result is only as good as the command that produced it — including its output limits.** Path set, pattern and unit were all declared correctly here. The defeat was a `head` on the listing. **Any enumeration that bounds a claim shall be run without an output limit, or shall report the count separately from the listing.**

## 7. CHECKPOINT

**CP-AI05 — DATABASE POPULATION QUANTIFIED, AFTER CORRECTION.** Observed incidence: **670 of 685 assets**; observed annihilation: **98.57 %**. Auto-continue.
