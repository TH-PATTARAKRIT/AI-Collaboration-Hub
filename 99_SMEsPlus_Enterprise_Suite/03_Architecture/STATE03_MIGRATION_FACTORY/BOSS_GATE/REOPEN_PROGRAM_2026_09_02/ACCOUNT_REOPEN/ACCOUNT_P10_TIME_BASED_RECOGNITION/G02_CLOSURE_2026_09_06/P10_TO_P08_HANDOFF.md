# P10 → P08 HANDOFF  (Record-to-Report — period close, GL, FX, reporting)

Published, not executed. **P10 does not define core ledger close semantics.** Everything below is an observation of ledger behaviour or a requirement addressed to its owner.

---

## 1. Obligations P10 Places on P08

| # | Obligation | Why |
|---|---|---|
| `OB-1` | **Author the accounting-event object**, or rule that none will exist — `D-5` | Three processes are blocked on one undefined object. P10 **specialises**, it does not duplicate, and attaches `AASP-COND-01` |
| `OB-2` | **Provide somewhere to record the period an amount belongs to**, distinct from the date its entry carries | The ledger has **no period object**; a period is a date range and closing one is moving a date |
| `OB-3` | On a constraint-driven date change: **refuse, or record an attributable trace — and where the mutation path has no violation to detect, the trace is MANDATORY, not alternative** | Restated this round to carry the peer's **refined** close condition. The earlier wording offered two interchangeable alternatives; on the lock-free path only one exists |
| `OB-4` | **Attribution on a posted, hashed, locked entry is freely editable and untracked** | It is absent from every lock-date list, every integrity-hash list, and the tracked-field set. Two of the three were re-derived from source by an independent party |
| `OB-5` | **State the currency model for a programmatic entry that carries no currency of its own** | P10's recognition lines carry none, and **no foreign-amount integrity check exists anywhere** |
| `OB-6` | **The relocation landing period is selected by the journal's sequence numbering format** | Month-reset lands at month end; year-reset lands at 31 December. A convention whose answer changes with a numbering format is not a convention |

## 2. What P10 Reports as Ledger Behaviour

| Observation | Class |
|---|---|
| Only the fiscal-year lock and the irreversible lock ever bind a recognition entry — recognition posts to general journals and carries no tax | `FACT VERIFIED` |
| Relocation is **specified**, asserted by an executed test in which one fiscal year shows nothing and the next shows double | `FACT VERIFIED`; the test's stated subject is something else, so the assertion is **incidental** |
| The silence is a **choice** — the same routine posts a chatter message six lines above the relocation branch | `FACT VERIFIED` |
| Reopening a period re-derives nothing | `A` — verified absence within the searched module set |
| **1 of 46 distinct companies** in the four examined databases has any lock configured | `FACT VERIFIED` within that population |

## 3. The Path This Handoff Cannot Close

A **second mutation path fires with no lock configured**, triggered by an upstream document-date edit. It requires no configuration, is reachable by construction, and its exposure is **unknown**. **A ruling scoped to the lock path does not dispose of it.** Owned jointly by P08 and P11.

## 4. Bounding

P10 read one reference generation; the deployed estate runs a **newer major generation**. Every source claim above is bounded to the generation read. P10 states this rather than letting P08 inherit it silently.

---

## CORRECTIONS TO THIS HANDOFF AFTER ADVERSARIAL CHALLENGE

**P10 handed the ledger owner a mis-stated inventory of the owner's own control set. Withdrawn and
restated — `G02-R-10`.**

| Was | Now |
|---|---|
| "Only the general and irrevocable cut-offs **bind** recognition entries" — dispositioned `FACT VERIFIED` | **WITHDRAWN.** The behaviour is **`RELOCATE`**, which P10's own matrix records one section earlier, and P08's `PC-29a` is `FACT VERIFIED` that the irrevocable cut-off refuses a **reopen**, not a **posting**. A relocating control does not bind |
| A *fiscal-year* semantic on the first cut-off | **Struck.** P08's `PC-07` enumerates it as a **general** cut-off and records the first four as **relaxable** |
| No row for the **cut-off exception** | **Added.** `PC-10`/`PC-12`: it lowers one relaxable cut-off for one user or for everyone, longest preset unlimited, justification not required. P10's matrix presented binding as unconditioned |
| No row for the **entry seal** | **Added.** `PC-30`: the one genuinely irreversible control is the entry seal, not the period cut-off |

**P10 should have cited `PC-07`, `PC-29a`, `PC-10` and `PC-30` rather than publishing a determination
about P08's control set as P10's own verified fact. This is the closest the round came to defining
rather than consuming.**

### Additional obligations

| # | Obligation |
|---|---|
| `OB-7` | **Exact question, replacing P10's premise.** P10 excluded the tax cut-off on the ground that recognition entries carry no tax, and never tested it. P08 has `FACT VERIFIED` a tax-period carrier populated on **61,157 posted entries**, differing from the accounting date on 5,228. **P10's own schema pass confirms that carrier exists on the entry and is absent from the item in the deployed generation.** *Does a recognition entry carry it, and does the tax cut-off bind it?* (`G02-R-11`) |
| `OB-8` | **Pin the measurement.** The rate and date at which a recognition base was measured must be **stored on the fact and pinned as-of**, not recomputed on read. P08's `FX-01`/`FX-02`/`FX-11` establish that the factor is recomputed from current master data on every read and that amending a rate silently changes closed-period figures. P10 asserted its frozen base was "internally consistent" and should have routed its **durability** |
| `OB-9` | **Foreign-amount integrity has no owner.** P10 verified that foreign amounts need not sum to zero on a foreign-currency entry and that nothing catches it, because balance validation sums company-currency amounts only. That is a **double-entry integrity** statement, not a recognition one. It is routed here; P10 does not own it |
| `OB-10` | **The monetary / non-monetary classification** of a recognition base. Whether a deferred balance retranslates at all is a classification of the **item**, not a property of the entry, and no currency column can be specified without it. P10 routes the **classification question**, not merely "FX policy" |

### Peer identifiers, previously absent — `G02-R-15`

P10 referred to every peer object descriptively. Named: the programme-wide tolerance-zero boundary is
**`T0-13` / `P11-B-16`**, status **`HOLD — BOSS DECISION REQUIRED`**; the second, cut-off-free
re-dating path is **`UAE-05`**, which **P11 already owns and has named** — P10 re-routed it as new.

### P08's own status, previously unrecorded

P08's package stands at **`RECOMMEND HOLD`**, carrying a challenge veto that **no downstream process
may rely on the draft's persistence-layer control set**. P10 placed obligations on P08 without
recording either. Recorded now: **these obligations are addressed to a package on hold, and P10 relies
on none of its control set.**
