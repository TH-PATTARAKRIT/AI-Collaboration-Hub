# P11 — UNIFIED ACCOUNTING EVENT REGISTER

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room
Model 2 of 15.

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. Definition adopted, and why it is not the obvious one

Wave A's definition is adopted verbatim and is load-bearing:

> An **accounting event** is an occurrence after which the ledger asserts something it did not assert
> before.

The obvious alternative — *"an accounting event is a journal entry"* — is **rejected**, and the reason
is the most consequential design position in the inherited evidence base. Wave A `06` §2 established
that in the reference model the journal entry is simultaneously the representation of the event **and
the event's only durable record**, and traced five separate downstream problems to that collapse:
duplicate detection, correction semantics, period re-attribution, migration provenance, and the audit
question *"what did we recognise, as distinct from how we wrote it down"*.

`P11-DERIVED, SUPPORTED INTERPRETATION:` the cross-process view **strengthens** that position rather
than merely inheriting it. Three of the fifteen unified models below — ownership, double-counting
control, and reversal/correction — are unstatable without a separate accounting-event identity. A
whole-system reconciliation is the first vantage point from which that is visible, because it is the
first place where the same business fact is seen arriving from two directions.

---

## 2. Class A — accounting events the ledger emits on its own initiative

Carried from `SL-01` `07`. **These are the dangerous ones**, and P11's cross-process reading makes
four of them worse than the single-domain reading did.

| id | Accounting event | Emitted by | Visible at the moment it occurs? | Cross-process consequence P11 adds |
|---|---|---|---|---|
| `UAE-01` | Exchange difference recognised (`AE-11`) | reconciliation | partly — a separate entry | Its **account selection is `UNK`** and its period may be re-attributed. `P06` produces it, `P08` reports it, `P07` may be affected — **no process owns it** |
| `UAE-02` | Match removed → exchange entry reversed (`AE-12`) | user unmatch | partly | A `P06` operational act silently emits a **new posted `P08` fact** |
| `UAE-03` | Cash-basis tax recognised (`AE-13`) | reconciliation | **no** | **Dated today when its natural period is locked — it can cross a fiscal year boundary.** `P06` acts; `P07`'s return content changes; `P08`'s comparatives change. `XM-02`, Thai consequence `HOLD` |
| `UAE-04` | Entry re-dated on posting (`AE-02`) | lock violated | only while draft | Every producer's *intended* recognition date can be overwritten after handoff |
| `UAE-05` | Entry re-dated on document-date change (`AE-03`) | any document-date edit on a non-sale document | **no** | **Fires with no lock configured.** A `P01` clerical edit re-attributes a period with no accounting justification |
| `UAE-06` | Entry re-dated on duplication or reversal (`AE-04`) | copy or reverse into a locked period | partly | A reversal and its original can sit in different **years** |
| `UAE-07` | Tax lock date set by return posting (`AE-18`) | `P07` posting a return | yes | A `P07` act sets a `P08` governance state automatically |
| `UAE-08` | Analytic lines deleted on un-post (`AE-05`) | any un-post | **the state change is; the destruction is not** | A `P08` correction destroys `P09`'s attribution subledger, unrecoverably |
| `UAE-09` | Classifications merged (`AE-20`) | user | **no — no record of any kind is created** | Posted history across **every** process is retargeted with no tracking written |

> **Four of the nine are invisible at the moment they occur** (`UAE-03`, `UAE-05`, `UAE-08` in its
> destructive half, `UAE-09`). Wave A named this. P11's addition is that **all four cross a process
> boundary**: the actor is in one process and the consequence lands in another. An invisible event
> inside one domain is a usability defect. An invisible event that crosses a domain boundary is an
> **ownership defect**, because the receiving domain cannot be accountable for a fact it was never
> told about.

## 3. Class B — accounting events a producer requests

| id | Accounting event | Requesting process | Recognition trigger | Determined? |
|---|---|---|---|---|
| `UAE-10` | Purchase obligation recognised | `P01` | bill validation | yes — pattern `UNK` |
| `UAE-11` | Goods-received value recognised | `P01`/Inventory | receipt validation | **timing depends on `JT-03` perpetual/periodic — no stable reference pattern exists to imitate** |
| `UAE-12` | Price difference recognised | `P01` | bill vs receipt | **`JT-02` open** |
| `UAE-13` | Revenue recognised | `P02` | invoice validation | yes — pattern `UNK` |
| `UAE-14` | Cost of sales recognised | `P02`/Inventory | **`JT-04` `NOT DECIDABLE` — dispatch or invoice** | **no** |
| `UAE-15` | Return cost recognised | `P02`/Inventory | **`JT-05` `NOT DECIDABLE` — original or current basis** | **no** |
| `UAE-16` | Conversion cost absorbed | `P03` | order completion | **partly — `BLK-07` `HOLD`; and absorption occurs only under FIFO/average** |
| `UAE-17` | Unabsorbed overhead expensed | `P03`/`P04` | period | **`BD-02` + TAS 2 ¶13 require it; the mechanism does not exist (`link 18`, `link 19` `ABSENT`)** |
| `UAE-18` | Depreciation recognised | `P04` | period run | yes |
| `UAE-19` | Asset derecognised | `P04` | disposal | yes — pattern `UNK` |
| `UAE-20` | Expense obligation recognised | `P05` | approval | **`UNKNOWN — EVIDENCE REQUIRED`** |
| `UAE-21` | Settlement recognised | `P06` | payment / matching | yes |
| `UAE-22` | Tax recognised on document | `P07` | posting | yes — pattern `UNK` |
| `UAE-23` | Withholding recognised | `P07` | payment | `HOLD — STATUTORY EVIDENCE REQUIRED` |
| `UAE-24` | Opening position recognised | `P08` | cutover | yes |
| `UAE-25` | Deferred amount released | `P10` | period run | **`UNKNOWN — EVIDENCE REQUIRED`** |

## 4. Class C — accounting events that must exist and do not

Carried from `SL-01` `07` "Events the reference model does NOT have", re-tested across all ten
processes. **P11 confirms all five are absent and adds two.**

| id | Absent event | Cross-process consequence | Disposition |
|---|---|---|---|
| `UAE-26` | **Period close** — there is no closer, no close date, no basis, no artefact, only a moved date | `P08` cannot produce a close artefact; `P01`…`P07` cannot know what was included | `HOLD — DESIGN DECISION` |
| `UAE-27` | **Year-end result transfer** — current-year earnings is computed at report time and never posted | Retained earnings has no posted provenance in any process | `HOLD — DESIGN DECISION` |
| `UAE-28` | **Revaluation / unrealised FX** — no carrier found in the scope read | `P06` and `P08` both need it; neither owns it | `HOLD — EVIDENCE REQUIRED` (`GAP-H01`) |
| `UAE-29` | **Accounting-event recognition distinct from entry creation** — no event identity | **Duplicates are undetectable across every one of the ten processes.** Root of `XM-01` | `HOLD — BOSS DESIGN DECISION` · the root blocker |
| `UAE-30` | **Approval before posting** — posting authority is a single permission; no maker-checker | Every process inherits a single-permission posting authority | `HOLD — DESIGN DECISION` |
| `UAE-31` | **Absorbed-versus-actual variance recognition** — `ABSENT` in 797 modules | `P03` cannot close the loop between `UAE-16` and `UAE-17`; TAS 2 ¶13 compliance is unprovable | **NEW at P11** — `HOLD — DESIGN DECISION` |
| `UAE-32` | **Prior-period attribution of a late cost** — *no prior-period attribution mechanism exists in the reference ERP at all* | `JT-06`; affects `P01` late bills, `P03` late costs, `P08` close | **NEW at P11** — `HOLD — DESIGN DECISION`; largely original design work |

> `UAE-31` and `UAE-32` are recorded as **new at P11** rather than inherited. Each was stated inside a
> single-domain package — `UAE-31` in `SL-13` `08` as an absent chain link, `UAE-32` in `SL-07` `17`
> §4 as a note on `JT-06`. Neither was registered as a **missing accounting event**. Promoting them
> to that status is a P11 contribution and is disclosed as one.

---

## 5. The arithmetic, stated so it can be checked

| Line | Count |
|---|---|
| Class A — ledger-emitted | **9** |
| Class B — producer-requested | **16** |
| Class C — required and absent | **7** (5 inherited + 2 new at P11) |
| **Total registered** | **32** |
| Of Class B, recognition **not determined** | **6** — `UAE-11`, `UAE-12`, `UAE-14`, `UAE-15`, `UAE-16`, `UAE-17` |
| Of Class B, producer contract **not established at all** | **2** — `UAE-20`, `UAE-25` |
| Of all 32, debit/credit pattern **verified from primary source** | **5** — and all five are Wave A's own (`M-01`…`M-05`) |

> ### `27 of 32 accounting events have no verified posting pattern.`
> That is not a P11 failure. It is `SL-01` `08`'s explicit and correct position — the producing
> processes own their posting patterns, and **`P01`–`P10` have published nothing**. P11 reports the
> ratio rather than filling the cells from convention, which would convert inference into apparent
> fact.
