# P10 — AUDIT / SOURCE-TO-RECOGNITION LINEAGE TRACE  (`CQ-P10-10`)

**Terminal disposition: `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`.**

---

## 1. The Chain, Traced End to End

`origin document/event → recognition policy → schedule → recognition line → posting → correction/reversal → reporting`

| Link | Carried by | Survives? |
|---|---|---|
| Origin document → policy | the company's settings, read at generation | **not recorded on the entry** — which company's settings applied is unrecoverable |
| Policy → schedule | computed and **discarded** inside one call | **no schedule object exists** |
| Schedule → recognition line | the line's date and amount | **the period is not carried**; only the period *end*, as the date |
| Recognition line → posting | the same record | the line **is** the posting — they are one object |
| Posting → correction | per-entry: unlink, cancel (**unreachable**), or reverse | **partially** — an unlinked entry ceases to exist |
| Correction → reporting | the reversal's own date | **the reversal can land in a different period from what it corrects** |
| Any link → the source line | **move-level only** for deferrals; line-level only for the loan | **partially** |

## 2. Immutable References — what exists and what does not

| Reference | Present? |
|---|---|
| Entry → source **document** | **yes**, on every generated deferral entry; written by raw SQL on the grouped path, bypassing the ORM |
| Entry → source **line** | **no** |
| Entry → **schedule version** | **no** — no schedule object, so no version |
| Entry → **recognition period** | **no** for deferrals; **yes** for depreciation |
| Entry → **policy applied** | **no** |
| Entry → **actor and reason** for a correction | **no** |
| Order → **accrual entry** | **no** — the code that would write it iterates a collection that is never populated |

**Two are dead code and one is bypassed:** the accrual's chatter link never executes; a second copy of the deferred-line builder has **no caller anywhere in the root**; and the grouped path writes its relation with raw SQL.

## 3. What Reporting Actually Shows

The two recognition reports **recompute the expected spread from the two date fields on every render**. They are a **model of what should have been recognised**, not a record of what was.

> **Where a posting was relocated by a lock, the report and the ledger disagree — and the report is the one that is right about the economics.** That divergence is not reported, reconciled, or detectable from either side alone.

## 4. Attribution Lineage — separately broken

The management-side attribution is **absent from every lock-date list, every integrity-hash list, and the tracked-field set** — so attribution on a **posted, hashed, locked** recognition entry is freely editable and untracked. Two of those three were re-derived from source by an independent party this round and can be carried as verified.

## 5. Audit Needs Supported by Evidence

Each is derived from an **observed absence**, not from preference:

| # | Requirement | Derived from |
|---|---|---|
| `AL-1` | A recognition event must reference its **origin line**, not only its origin document | move-level-only anchoring |
| `AL-2` | It must carry its **recognition period**, distinct from its posting date | the collapse, and depreciation's counter-example |
| `AL-3` | It must record the **policy version** that produced it | policy is read at generation and never recorded |
| `AL-4` | A correction must record **actor, reason and prior version** | none of the three exists |
| `AL-5` | A correction must be **reconcilable to what it corrects**, including across periods | the reversal lands elsewhere |
| `AL-6` | An estimate must reference the **actual that settles it** | the accrual has no link, and the code that would make one is dead |
| `AL-7` | The divergence between recognition period and posting date must be **reportable** | the report and the ledger disagree undetectably |
| `AL-8` | Attribution must be **immutable once posted**, or its mutation must be tracked | it is neither |

## 6. Disposition

`CQ-P10-10`: **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**, bounded to the declared root and to four databases in which the deferral mechanism has never executed. The eight requirements are `FACT-SUPPORTED FUNCTIONAL REQUIREMENT`s and carry into the design pack.
