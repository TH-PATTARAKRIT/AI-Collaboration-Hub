# P11 — `D-3b` EVIDENCE SELECTION CONTROL — **v5**

`[SMEPLUS-26-09-06-…-CORR2-PHASES-001]` · `CP-P11C2-03` · **PHASE S** · Layer 1 clean-room

> **`D-3b` is a Boss authorisation request, not a research plan.** v4 was found to certify
> *"2 of 2 ⇒ complete"* over a population of **≥ 9**, because it had **no population element**.
> v5 adds `E0` and `E6` and **narrows** what the authorisation permits.
>
> **`D-3b` does NOT mean "open every dump for every claim".** It means: *for a named claim, declare the
> population first, select from it by a published rule, and open only what that rule selects.*

---

## 1. The seven elements

| id | Element | v4 | **v5** |
|---|---|---|---|
| **`E0`** | **Candidate population declaration** | **absent — the defect** | **mandatory, and it is the first act** |
| `E1` | Claim type → ranking unit | present | unchanged |
| `E2` | Denominator + unit | present | unchanged |
| `E3` | Tool / client capability **and version** | present | unchanged |
| `E4` | Generation / format coverage required **by that claim** | present | tightened (§4) |
| `E5` | Exclusions **with reason and authority** | present | tightened (§5) |
| **`E6`** | **Independent denominator challenge** | **absent** | **mandatory before publication** |

## 2. `E0` — candidate population declaration

**Before any artefact is opened**, publish:

1. **The population**, enumerated by a command, with the command shown.
2. **A ranking of that population** on a property relevant to the claim — size, generation, record
   count — *published before selection*.
3. **The selection rule** and what it selects.
4. **What the rule excludes and why.**

> **`E0` exists because of two measured failures, one per side of the programme.**
> `P07` built a runtime section on a database with **23** move lines because it sat inside the declared
> path set; the one it never opened had **447,384**. **P11** ranked dumps *after* choosing and found the
> largest on the host — **155 MB, 2.4× the next** — had never been opened, with the sizes present in the
> first directory listing P11 ran.

**`E0` is satisfied only by a ranking published before the selection, never by one reconstructed after.**

## 3. `E1` — claim type determines the ranking unit

| Claim type | Ranking unit | Never rank by |
|---|---|---|
| *"mechanism X has never run"* | **rows in the table the mechanism writes** | file size, filename, directory order |
| *"attribute A is unpopulated"* | **rows in the table carrying A** | number of databases |
| *"module M is not installed"* | **installed-module rows per database**, all databases | source-tree presence |
| *"the estate exhibits behaviour B"* | **databases of the relevant generation** | total databases |
| *"amount totals T"* | **posting lines in scope**, with the state basis declared | entries, accounts, or documents |

> **The unit failure this programme keeps repeating:** `P09` corrected its denominator **four
> consecutive rounds** — an author-chosen list, then a pattern excluding its own subject, then
> **accounts counted for entries**, then **a silent sub-population inside an unchanged sentence**.
> **The unit was finally right and the population narrowed anyway.**

## 4. `E4` — generation coverage is a property of the claim

A claim about the **deployed estate** requires **every generation in the estate**: **16.0, 18.0, 19.0**.
A claim about the **source line** requires the generation actually read, and **may not be stated of any
deployment** (`P11_B17_SCOPE_REPAIR_CORR2.md`).

**Now established and binding on any future `D-3b` execution:** **31 core trees across five series** —
14.0 ×1, 16.0 ×3, 17.0 ×2, 18.0 ×15, 19.0 ×10 — and **every 14/16/17 tree is under `/Users/admin`,
none on `/Volumes`** (`P01` `ERR-P01-41`). **A path-set that covers one volume cannot support the word
*anywhere*.**

## 5. `E5` — an exclusion needs an authority, not a reason

An exclusion must name **who is entitled to make it** and **what evidence would reverse it**. A stated
reason with no authority **stops the audit** and is how three separate packages lost a database.

**Standing exclusions for `D-3b`, with authority:**

| Excluded | Authority | Reversal |
|---|---|---|
| `~/Library` app-data trees | P11, to avoid an ~855-prompt TCC storm | a targeted path, named in advance |
| Any **write** to any database | the controlling prompt §15 | Boss, separately |
| Peer-owned source trees | domain purity, §4 of the prompt | route to owner |

## 6. `E6` — independent denominator challenge

**Before publication**, a party that did not choose the population must answer:

1. What is the population **the claim's wording** covers?
2. What is the population **actually measured**?
3. **Are they the same set?** If not, the claim is re-worded or the population re-drawn — **never both
   left as published**.
4. What would be in the population under a **different defensible reading**, and how large is it?

> **`E6` is the control that would have caught every one of the four `P09` denominator errors and both
> of P11's.** The measured failure mode is not a wrong count — it is **a correct count over a
> population narrower than the sentence containing it**.

## 7. What `D-3b` v5 authorises, exactly

| Requested | Bounded to |
|---|---|
| **Read-only** extraction from named database artefacts | the artefacts a published `E0` ranking selects **for one named claim** |
| Client version | declared per execution, with the version string recorded |
| Generation coverage | every generation the claim's scope requires (`E4`) |
| Output | counts and aggregates into P11 registers. **No content copied into the package** |

**Not requested and not authorised:** any write; any install/uninstall; any configuration change; any
restore; any destructive test; any extraction from a database not named by an `E0` ranking.

## 8. Status

**`AUTHORIZATION REQUIRED — EXACT EVIDENCE ACTION NAMED`.**

`D-3b` remains **undecided by P11** and is Boss-reserved. **P11 has performed no extraction under it,
in CORR1 or CORR2.** Four of the seven elements are pre-discharged by specification; `E0` and `E6` are
newly specified here; `E3` is discharged per-execution and cannot be discharged in advance.

**`CP-P11C2-03` — COMPLETE — EVIDENCE VERIFIED.**
