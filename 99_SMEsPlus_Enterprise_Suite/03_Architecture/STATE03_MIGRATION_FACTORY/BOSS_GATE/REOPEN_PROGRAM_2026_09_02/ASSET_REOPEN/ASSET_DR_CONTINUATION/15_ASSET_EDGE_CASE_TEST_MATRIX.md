# 15 — ASSET EDGE CASE TEST MATRIX (LEVEL 17)

**LAYER 2 — AUDIT QUARANTINE.**

All 27 cases required by §5 Level 17, each with expected behaviour, control, accounting
effect, cost effect, correction method and evidence requirement. "Expected" means the
**SMEsPlus design's** required behaviour; where the reference product behaves
differently that is stated, because the difference is the specification.

`REF` column: **W** = reference product does this correctly · **X** = does it wrongly ·
**–** = has no behaviour at all.

---

## `EC-01` — Asset fully depreciated but still operating · `REF: –`

| | |
|---|---|
| Expected | Statutory depreciation stops at the residual. Internal usage (`10`) begins the following day, **detected** from the derived residual reaching zero, since no status exists |
| Control | Detection rule, not a status read |
| Accounting effect | **None.** No statutory entry |
| Cost effect | Management ledger only. Statutory product cost unchanged |
| Correction | Restate the internal-usage start date; re-run the management ledger from that date |
| Evidence | The derived residual value; the last posted depreciation entry |

## `EC-02` — Equipment under maintenance the entire month · `REF: X`

| | |
|---|---|
| Expected | Zero productive hours. **Planned** maintenance is inside normal capacity and is absorbed through the rate for other machines' output; **unplanned** maintenance is a period expense classified MAINTENANCE-UNPLANNED. The whole month's depreciation is attributed, none capitalised for this machine |
| Control | `09` §8 reconciliation must close to zero |
| Accounting effect | Full period depreciation to expense, classified |
| Cost effect | No absorption. Product cost unaffected — **correct under TAS 2 ¶13**, which forbids raising the per-unit charge when production ceases |
| Correction | Reclassify the cause; re-run the period's split |
| Evidence | Maintenance request with type and dates; calendar leaves |
| Reference behaviour | Depreciation lands in expense unclassified; no non-productive record exists |

## `EC-03` — Equipment breaks down mid-production · `REF: X`

| | |
|---|---|
| Expected | Hours before the breakdown are productive. The interruption is a time log with an availability-category reason, classified BREAKDOWN, expensed |
| Control | Blocking reason mandatory on any non-productive log |
| Accounting effect | Split between absorbed and period expense |
| Cost effect | The order carries only the hours it actually consumed |
| Correction | Amend the log; re-run the period |
| Evidence | Time logs with reason and timestamps |
| Reference behaviour | The log can exist; it carries no cost, so the breakdown is invisible in cost terms |

## `EC-04` — No production demand for the whole month · `REF: X`

| | |
|---|---|
| Expected | Zero productive hours; full depreciation to period expense, classified NO_DEMAND |
| Control | Reconciliation closes; NO_DEMAND is separately reported as a management signal |
| Accounting effect | Full depreciation expensed |
| Cost effect | None. **A naïve 100%-attribution implementation would divide by zero here** — `09` §2 |
| Correction | n/a |
| Evidence | Absence of scheduled work orders against available calendar time |

## `EC-05` — Equipment changes work centre · `REF: X`

| | |
|---|---|
| Expected | A **dated assignment record** closes and a new one opens. Cost before the change belongs to the old work centre, after to the new |
| Control | Assignment is a dated record, never an editable field |
| Accounting effect | None directly |
| Cost effect | Period-split allocation across two work centres |
| Correction | Correct the assignment dates; re-run affected periods |
| Evidence | The assignment history |
| Reference behaviour | A single field write. **No history. All prior attribution is retrospectively falsified with no trace** |

## `EC-06` — Equipment removed from a work centre · `REF: X`

| | |
|---|---|
| Expected | Assignment closes. The machine still depreciates; with no work centre it produces nothing, so its whole depreciation is non-productive, classified IDLE |
| Control | An unassigned machine that is still in the costing scope must be **reported**, not silently ignored |
| Accounting effect | Depreciation to period expense |
| Cost effect | None |
| Correction | Reassign, dated |
| Evidence | Assignment history |

## `EC-07` — Equipment transferred between sites · `REF: –`

| | |
|---|---|
| Expected | Where sites are within one company: a dated site change; normal capacity may change with it. Across companies: **not a transfer** — either an asset disposal and acquisition, or a usage-rights arrangement (`14` §4 `LK-04`) |
| Control | Cross-company movement must be refused as a field edit |
| Accounting effect | Within company none; across companies a disposal/acquisition or an intercompany charge |
| Cost effect | Normal capacity and rate recomputed prospectively |
| Correction | Dated correction of the site record |
| Evidence | Site history |
| Reference behaviour | Sites are not modelled at all |

## `EC-08` — Asset sold mid-month · `REF: W`

| | |
|---|---|
| Expected | Depreciation to the disposal date; disposal entry; costing stops at that date; internal usage, if running, is frozen and closed (`10` §6) |
| Control | Lock-date guard — already present |
| Accounting effect | Cost out, accumulated depreciation out, proceeds in, balance to gain or loss |
| Cost effect | Partial-month absorption on days owned |
| Correction | Reverse the disposal; re-post |
| Evidence | Disposal entry; posted customer invoice |
| Note | The **residual does not survive** as an identifiable amount — `05` §9 |

## `EC-09` — Asset disposed but equipment still referenced · `REF: X`

| | |
|---|---|
| Expected | Disposal **must** retire the machine from the costing scope. A machine with no live asset contributes no depreciation and must not appear in a cost pool |
| Control | Disposal→retirement is mandatory and must fail loudly if it cannot complete |
| Accounting effect | None beyond the disposal |
| Cost effect | **The machine's cost pool becomes zero.** If it still carries hours, those hours are unattributed and reported |
| Correction | Retire the machine; re-run |
| Evidence | Asset state; machine state |
| Reference behaviour | **The retirement behaviour exists in a file the module never loads.** Sold machines stay active, silently. This is the single most actionable defect carried from the baseline and re-verified this session |

## `EC-10` — Asset book value reaches zero · `REF: –` | see `EC-01`

## `EC-11` — Residual greater than zero · `REF: W`

| | |
|---|---|
| Expected | Depreciation stops at the residual; internal usage begins from there |
| Control | Residual protected for the running life — verified present |
| Cost effect | **The internal-usage rate base matters here.** A one-baht residual makes candidate A meaningless — `10` §3 |
| Evidence | Asset residual value |

## `EC-12` — Internal usage accumulation exceeds residual book value · `REF: –`

| | |
|---|---|
| Expected | **Permitted and expected** under `BD-01`. No cap, no cut-off, no reduction of residual book value |
| Control | The accumulator is off-balance; the residual is on-balance; the platform pattern forbids one entry touching both (`05` §7) |
| Accounting effect | **None, structurally guaranteed** |
| Cost effect | Management ledger only |
| Correction | Dated correction entry in the management ledger |
| Evidence | Management ledger; statutory ledger — the two must show no arithmetic relationship |

## `EC-13` — Several manufacturing orders use the same machine · `REF: W`

| | |
|---|---|
| Expected | Hours split by time log; each order carries its own hours at the rate in force |
| Control | Sum of order hours ≤ machine available hours; a breach is a data error and is reported |
| Cost effect | Correct by construction |
| Evidence | Time logs at machine grain |

## `EC-14` — One operation uses several machines · `REF: –`

| | |
|---|---|
| Expected | **Must be supported.** Either several machine-time logs against one operation, or the operation is decomposed. Not expressible today (`06` §2) |
| Control | Each machine's hours attributed separately; no averaging |
| Cost effect | The order carries each machine at its own rate — the core of `BD-03` |
| Correction | Amend logs |
| Evidence | Machine-grain time logs |

## `EC-15` — Machine-hour evidence missing · `REF: –`

| | |
|---|---|
| Expected | The hours are recorded as **unattributed** and reported. **They must not fall back to a work-centre average** — a silent fallback reintroduces exactly the averaging `BD-03` rejects, invisibly (`11` §5) |
| Control | The reconciliation exposes unattributed hours; a threshold blocks the costing close |
| Accounting effect | The related depreciation goes to period expense as OTHER, which is itself a reported control breach |
| Cost effect | Under-absorption, visible |
| Correction | Supply the machine identity; re-run |
| Evidence | The count of logs lacking machine identity |

## `EC-16` — Machine-hour evidence wrong · `REF: –`

| | |
|---|---|
| Expected | Correctable before the costing close; a dated correction after it |
| Control | Plausibility checks — hours exceeding calendar availability, overlapping logs on one machine, logs against a machine not assigned to that work centre on that date |
| Cost effect | Cost shifts between jobs; the period total is unchanged, so the reconciliation will **not** catch it. Only the plausibility checks will |
| Correction | Dated correction |
| Evidence | Log history |
| Note | This is the main manipulation surface of a machine-hour driver (`11` §2) and needs the checks named above rather than reliance on the reconciliation |

## `EC-17` — Backdated operation · `REF: X`

| | |
|---|---|
| Expected | Accepted before the operational close; refused after it unless that close is explicitly reopened with a reason |
| Control | The three-close model (`13` §2) |
| Accounting effect | If the accounting period is closed, a correction entry in the next open period |
| Cost effect | The period's rate is recomputed in full, never patched (`13` §7) |
| Evidence | Close status; reopen record |

## `EC-18` — Closed accounting period · `REF: W`

| | |
|---|---|
| Expected | Postings refused. **Including the asset confirm path**, which the reference product does not explicitly guard (`05` §5) |
| Control | Explicit guard on every posting path, including confirm and pause |
| Accounting effect | Refusal, with a message naming the lock and the date |
| Correction | Post to the next open period as a dated correction |
| Evidence | Lock dates in force |

## `EC-19` — Manufacturing order cancelled after cost allocation · `REF: X`

| | |
|---|---|
| Expected | Allocation reversed by a **dated correction**, never deleted. The reversed depreciation returns to the non-productive pool for that period, classified |
| Control | Reversal only; no deletion of posted allocation |
| Accounting effect | Reversing entries |
| Cost effect | Absorbed falls; non-productive rises by the same amount; the reconciliation still closes |
| Correction | n/a — this *is* the correction |
| Evidence | Reversal entries |
| Reference behaviour | Cancelling a work order **deletes** its analytic lines outright. Deletion, not reversal — the opposite of the immutability discipline the same product applies to depreciation entries. **SMEsPlus must not copy this** |

## `EC-20` — Production return / reversal · `REF: W`

| | |
|---|---|
| Expected | The finished-goods layer reverses at the value it carried, including its machine cost |
| Control | Valuation-layer reversal at original value, not at a recomputed one |
| Cost effect | Absorbed cost returns to inventory or to expense according to the return's destination |
| Evidence | Valuation layers |

## `EC-21` — Scrap after production · `REF: W`

| | |
|---|---|
| Expected | Scrap carries its absorbed machine cost. **Abnormal** scrap is a period expense under TAS 2 ¶16, not an inventory cost |
| Control | Normal versus abnormal scrap must be distinguishable — the reference product does not distinguish them |
| Accounting effect | Normal: stays in cost of production. Abnormal: expensed |
| Cost effect | Abnormal scrap must not inflate the cost of good units |
| Correction | Reclassify; re-run |
| Evidence | Scrap records with a normal/abnormal flag — **to be built** |

## `EC-22` — Cost revaluation · `REF: W`

| | |
|---|---|
| Expected | An asset re-evaluation changes the remaining depreciable base **prospectively**; the machine rate changes from the next period. Prior periods are never restated |
| Control | Re-evaluation is lock-guarded — verified present |
| Accounting effect | Per the re-evaluation |
| Cost effect | Prospective rate change only |
| Correction | Reverse the re-evaluation |
| Evidence | Re-evaluation record |

## `EC-23` — Equipment inactive · `REF: X`

| | |
|---|---|
| Expected | An inactive machine whose asset is still live **still depreciates**. Its depreciation is fully non-productive — IDLE — and must still be attributed |
| Control | The costing scope is driven by the **asset's** state, not by the machine's archive flag |
| Accounting effect | Depreciation to expense, classified |
| Cost effect | None |
| Evidence | Machine active flag; asset state |
| Note | Deriving costing scope from the machine's archive flag would let archiving a machine silently remove real depreciation from the reconciliation. This is the trap `EC-09` creates from the other direction |

## `EC-24` — Work centre inactive · `REF: X`

| | |
|---|---|
| Expected | Machines assigned to it produce nothing. Their depreciation is non-productive, classified IDLE or NO_DEMAND |
| Control | As `EC-23` — scope follows the asset |
| Cost effect | None |
| Evidence | Work centre active flag; assignment history |

## `EC-25` — Cross-company production attempt · `REF: X`

| | |
|---|---|
| Expected | **Refused.** A machine may only be used by its owning company, unless a dated usage-rights record exists, in which case the charge is an explicit intercompany transaction |
| Control | Mandatory company on every costing record; same-company constraint on the asset↔machine link (`14` §5) |
| Accounting effect | Either refusal, or two entries in two companies |
| Cost effect | **No implicit transfer of depreciation between legal entities, ever** |
| Evidence | Company fields; usage-rights record |
| Reference behaviour | Achievable today by leaving the machine's company empty — `14` `LK-01` |

## `EC-26` — Currency difference · `REF: X`

| | |
|---|---|
| Expected | The asset, its depreciation, the machine rate and the absorbed cost are all in the **company's** currency. No foreign-currency asset exists in the reference product |
| Control | Rate and pool computed in company currency; presentation conversion only |
| Accounting effect | None new |
| Cost effect | None, provided no conversion happens inside the rate derivation |
| Evidence | Currency on each record |
| Note | An asset acquired in a foreign currency is capitalised at the rate on acquisition and depreciates in company currency. That is standard and is not a costing problem — it becomes one only if a design converts at allocation time |

## `EC-27` — Manual journal against a system-controlled account · `REF: X`

| | |
|---|---|
| Expected | **Refused** for accumulated depreciation, the absorption account, WIP and the finished-goods valuation account. These are system-controlled |
| Control | An account-level flag marking system control, enforced at posting |
| Accounting effect | Refusal |
| Cost effect | Prevents the sub-ledger and the ledger being separated by hand |
| Correction | Correct at source, through the sub-ledger |
| Evidence | Account configuration |
| Reference behaviour | No such control exists. There is also an import field for already-depreciated amounts, which is a **sanctioned** way to make the sub-ledger and the ledger disagree, with **no reconciliation report anywhere in the product** |
| **Second limb — the leak that has no journal line** | The structural firewall (`05` §7) protects the *journal*. It does **not** protect a *valuation field*. If internal usage (`10`) were ever permitted to update a product's standard cost or a valuation adjustment, it would reach statutory inventory **without any on-balance line being posted**. This must be tested explicitly, because the firewall creates a false sense that leakage is impossible |

---

## Summary

| Reference-product verdict | Count | Cases |
|---|---|---|
| **W** — behaves correctly | 7 | `EC-08`, `EC-11`, `EC-13`, `EC-18`, `EC-20`, `EC-21`, `EC-22` |
| **X** — behaves wrongly for this design | 13 | `EC-02`, `EC-03`, `EC-04`, `EC-05`, `EC-06`, `EC-09`, `EC-17`, `EC-19`, `EC-23`, `EC-24`, `EC-25`, `EC-26`, `EC-27` |
| **–** — no behaviour at all | 7 | `EC-01`, `EC-07`, `EC-10`, `EC-12`, `EC-14`, `EC-15`, `EC-16` |

**The three cases the design should be judged on**, because getting them wrong is both
likely and silent: `EC-09` (disposed asset, live machine — the defect that already
exists), `EC-15` (missing machine identity falling back to an average), and `EC-27`
second limb (leakage through a valuation field rather than a journal line).
