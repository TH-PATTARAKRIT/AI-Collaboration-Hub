# P11 — UNIFIED EVENT-TO-GL MATRIX

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room
Model 3 of 15.

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. Why this matrix is mostly empty, and why that is the correct state

`SL-01` `08` withheld debit and credit for every event whose posting pattern it had not read from
primary source, and named the owning Wave for each cell. Fourteen producer events were left explicitly
`UNKNOWN — EVIDENCE REQUIRED`.

**P11 was commissioned to fill exactly those cells from `P01`–`P10`.** `P01`–`P10` have published
nothing (`P11_SOURCE_LINK_REGISTER.md` §5). Therefore:

> ### The unified matrix inherits Wave A's empty cells unchanged and fills **none** of them.
>
> Filling them from convention would convert inference into apparent fact, would pre-empt ten
> unstarted gates, and would produce a Boss Gate Pack whose central artefact is fabricated. **The
> matrix is presented empty, with the reason, rather than complete and wrong.**

This is the load-bearing statement of the entire P11 gate and it is not softened.

---

## 2. Part 1 — the five events with a verified ledger effect

Carried verbatim in substance from `SL-01` `08`. These are the **only** rows in the whole system with
a posting pattern verified from primary source. All five are core-ledger events; **none belongs to a
producing process.**

| id | Event | Journal | Debit | Credit | Close impact | Reversal |
|---|---|---|---|---|---|---|
| `M-01` | Opening position established | nominated opening journal | per-account opening debit | per-account opening credit, **balanced to current-year earnings** | subject to lock like any entry | ordinary |
| `M-02` | Exchange difference on settlement | nominated exchange journal | the difference computed from the three amounts on the matching record | as debit | **re-dated if its natural date is locked** | **automatic** — unmatching reverses it |
| `M-03` | Cash-basis tax on settlement | nominated cash-basis journal | proportional mirror of the document's tax lines, scaled by matched percentage; **account pairs `UNK`** | as debit | **dated today when its natural period is locked — can cross a fiscal year** | reversible, **cannot be reset to draft** |
| `M-04` | Entry reversed | the original's journal | **exact mirror of the original** | exact mirror | **re-dated into the first open period if the original's period is locked** — original and reversal can sit in different years | reversible |
| `M-05` | Period made final | — | **NOT APPLICABLE — closing posts nothing** | NOT APPLICABLE | subsequent postings re-dated | soft moves back; hard never |

`M-05`'s `NOT APPLICABLE` is a **finding**, not a gap, and is marked with its reason as the standard
requires: the reference model has no closing entry.

## 3. Part 2 — producer events: ledger interface verified, posting pattern withheld

| Unified event | Process | Journal | Debit | Credit | Ledger-side constraint P11 can state | Owning gate |
|---|---|---|---|---|---|---|
| `UAE-10` vendor bill | `P01` | purchase | `UNK` | `UNK` | **purchase lock applies; and the accounting date moves to the end of the document's month even with no lock configured** | `P01` |
| `UAE-11` goods received value | `P01`/Inv | inventory | `UNK` | `UNK` | not open items; **timing governed by `JT-03`, which has no stable reference pattern** | `P01` + `JT-03` |
| `UAE-12` price difference | `P01` | `UNK` | `UNK` | `UNK` | **account scope contradicted — `JT-02` open** | `JT-02` |
| `UAE-13` customer invoice | `P02` | sale | `UNK` | `UNK` | receivable is an open item; **sale lock applies; re-dating capped at today** | `P02` |
| `UAE-14` cost of sales | `P02`/Inv | inventory or general | `UNK` | `UNK` | not open items; **recognition timing `NOT DECIDABLE` (`JT-04`)** | `JT-04` |
| `UAE-15` return cost | `P02`/Inv | inventory | `UNK` | `UNK` | **cost basis `NOT DECIDABLE` (`JT-05`)** | `JT-05` |
| `UAE-16` conversion cost absorbed | `P03` | inventory | `UNK` | `UNK` | **occurs only under FIFO/average; under standard costing work-centre cost never enters finished-goods value**; and the ledger half occurs only under perpetual valuation | `P03` + `BLK-07` |
| `UAE-17` unabsorbed overhead expensed | `P03`/`P04` | general | `UNK` | `UNK` | **required by TAS 2 ¶13 and by `BD-02`; no mechanism exists** | `BLK-07` |
| `UAE-18` depreciation | `P04` | general or nominated asset journal | `UNK` | `UNK` | company currency; not open items; **two day conventions selected by one untracked setting** | `P04` + `BLK-01` |
| `UAE-19` asset disposal | `P04` | general | `UNK` | `UNK` | not open items | `P04` |
| `UAE-20` employee expense | `P05` | purchase | `UNK` | `UNK` | payable item; purchase lock; **producer contract not established** | `P05` |
| `UAE-21` payment / settlement | `P06` | bank or cash | `UNK` | `UNK` | matched against the open item; **emits `M-02` where measurement moved**; **unreconciled lines block period locking** | `P06` |
| `UAE-22` tax on document | `P07` | per tax config | `UNK` | `UNK` | tax items are **outside hash coverage** | `P07` |
| `UAE-23` withholding | `P07` | `UNK` | `UNK` | `UNK` | `HOLD — STATUTORY EVIDENCE REQUIRED` | `P07` |
| `UAE-25` deferred release | `P10` | general | `UNK` | `UNK` | not open items; **producer contract not established** | `P10` |

**15 rows. 30 withheld debit/credit cells. 0 filled by P11.**

## 4. The cells that are NOT blocked on `P01`–`P10`

An honest matrix distinguishes *"nobody has done the work"* from *"the work was done and the answer is
that it cannot be decided"*. Six of the fifteen rows above are in the **second** state, and
commissioning the producing process will not move them:

| Row | Blocked on | Named missing input |
|---|---|---|
| `UAE-11` | `JT-03` | The reference ERP has **no single stable pattern across versions** — imitation is unavailable |
| `UAE-12` | `JT-02` | An unresolved contradiction on price-difference account scope |
| `UAE-14` | `JT-04` `NOT DECIDABLE` | `SME-Q-03` business input, `TH-NEW-01` statutory, two documentation sub-facts |
| `UAE-15` | `JT-05` `NOT DECIDABLE` | `SME-Q-02`, `TH-NEW-02`, a live FIFO-return test |
| `UAE-16`/`UAE-17` | `BLK-07` `HOLD — DESIGN DECISION` | A Boss ruling on normal capacity vs actual hours |
| `UAE-23` | Thai statutory | Authoritative statutory evidence |

> **`P01`–`P10` publishing in full would leave six of these fifteen rows exactly as they are.** The
> peer dependency is therefore **necessary but not sufficient** for this matrix. Both facts are
> reported; reporting only the first would understate the blocker, and reporting only the second
> would excuse it.

## 5. Consequence for `BC-01`

The Boss-approved 22-scenario cross-proof requires, per scenario, the accounting effect and the
16-element handoff proof. With 30 of 30 producer debit/credit cells withheld, **no scenario in the
22-scenario baseline can be evidenced end to end today.** Combined with `SL-07` `16` §3.1 —
*zero of ten material Inventory→Accounting handoffs is contract-compliant* — the cross-proof baseline
stands at **0 of 22 evidenced**.

That figure is stated as the mechanical consequence it is, not as an assessment of anyone's work.
