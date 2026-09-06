# P10 — PERIOD CLOSE / LOCK INTERACTION MATRIX  (`CQ-P10-08`)

**Terminal disposition: `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** for behaviour · **`BOSS DECISION REQUIRED`** for canonical SMEsPlus policy.

---

## 1. The Matrix

| Action | Behaviour | Silently changes the accounting period? | Tested? |
|---|---|---|---|
| Deferral generation, grouped path, into a locked period | **REFUSE** | no | **yes** |
| Deferral generation, validation path, into a locked period | **RELOCATE** | **YES** | exercised; **the dates are not asserted** |
| Deferral generation into a period not ending at a month end | **REFUSE** | no | — |
| Asset board posting into a locked period | **RELOCATE** | **YES** | **yes — and the relocation is the asserted result** |
| Asset disposal before the lock | **REFUSE** | no | present |
| Asset account/journal change at or before the lock | **PROCEED, silently skipped** | no — the change is dropped | — |
| Accrual creation and its reversal | **RELOCATE** (no pre-check) | **YES** | none |
| Loan confirmation | **PROCEED** (no lock handling) | **YES** via the shared routine | none |
| Corrective reversal on teardown | **RELOCATE** — re-dated through the accounting-date helper | **YES** | **yes** — January entry, February reversal |
| Reopening a closed period | **nothing re-derives** | n/a | — |

## 2. Which Locks Actually Bind

Five lock fields exist on the company — verified independently in the **deployed 19.0+e schema**: a general cut-off, a tax cut-off, a sales-document cut-off, a purchase-document cut-off and an irrevocable cut-off.

> **CORRECTED — `G02-R-10`. The word "bind" is struck, and it contradicted §1 of this same document.**
>
> ~~*only the fiscal-year lock and the irreversible lock ever bind them*~~. §1 above records the behaviour as **`RELOCATE`**, and the ledger owner has `FACT VERIFIED` that the irrevocable lock refuses a **reopen**, not a **posting**: an entry aimed at an irrevocably locked period is **relocated forward and posted**. A relocating control does not bind. P10 also imported a *fiscal-year* semantic the owner's own enumeration does not carry — it enumerates a **general cut-off**, and records the first four as **relaxable**.
>
> **Two controls are missing from this matrix entirely (`G02-R-10`):** the **lock exception**, which lowers one relaxable cut-off for one user or for everyone, with no required justification and an unbounded window; and the **entry seal**, which the owner records as the one genuinely irreversible control. P10's lineage knew the exception route existed at class `C` and did not carry it into closure.

> **OPEN — `G02-R-11`. The tax-lock exclusion rests on an untested premise.**
>
> "Recognition entries carry no tax" is the sole ground for excluding the tax lock, and P10 never tested it. The ledger owner has `FACT VERIFIED` a tax-period carrier populated on **61,157 posted entries**, differing from the accounting date on 5,228. **P10's own differencing pass confirms a tax-period carrier is present on the entry and absent from the item in the deployed 19.0+e schema.** Whether a *recognition* entry carries it is the question P10 did not ask. Routed to `P08`.

## 3. Relocation Is Not One Convention

The landing period is chosen by the journal's **sequence numbering format**: month-reset → that month's end; year-reset → **31 December**. Same lock, same charge, different period.

> A defensible accounting convention does not change its answer because a sequence resets yearly instead of monthly. **This is the strongest single argument that the relocation is a misstatement rather than a convention** — and both readings are carried to the Boss, because the convention reading is what any vendor will argue.

## 4. Deployed Reachability

**1 of 46 distinct companies has any period lock set**, and that company's database holds ten journal entries, no recognition entries and no assets. The one database with production volume has **no lock**.

| State | Count of the four databases |
|---|---|
| Code capability present | **4** |
| Configuration reachable | **1** |
| Deployment exposed | **0** |
| Observed execution | **0 confirmed**; 3 candidate signatures, cause undetermined |

**The lock-triggered relocation is NOT REACHABLE in three of four and DORMANT in the fourth.**

## 5. The Path This Matrix Does Not Reach

A **second mutation path fires with no lock configured at all**, triggered by an upstream document-date edit. It needs no configuration, is reachable by construction in all four databases, and its exposure is **unknown**.

> **A ruling scoped to the lock path would not dispose of it.** It is owned jointly by the ledger process and the cross-process process; P10 records it and routes it.

## 6. Canonical Policy — not inferred from the reference

The Boss boundary is explicit: *do not infer canonical SMEsPlus policy from reference behaviour.* P10 therefore records the behaviour and states the options without choosing, and notes the two constraints that changed this round:

1. the peer boundary that would exclude the status quo is an **OPEN blocker** — `UNRESOLVED != ADOPTED`, so the status-quo option is **live**;
2. that boundary's close condition is **refined**: where a mutation path has no violation to detect, a **trace is mandatory, not alternative** — so **refusal alone is not a complete answer**.

## 7. Disposition

- The matrix: **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**
- Which locks bind: **WITHDRAWN — `G02-R-10`.** The behaviour is `RELOCATE`, not bind; the enumeration is the ledger owner's, not P10's, and P10 published it without citing the owner's verified rows
- Deployed reachability: **`FACT VERIFIED`** within the four databases
- Canonical SMEsPlus close policy: **`BOSS DECISION REQUIRED`**
- The lock-free mutation path: **`CROSS-PROCESS OWNER — HANDOFF PUBLISHED`** (P08 / P11)
