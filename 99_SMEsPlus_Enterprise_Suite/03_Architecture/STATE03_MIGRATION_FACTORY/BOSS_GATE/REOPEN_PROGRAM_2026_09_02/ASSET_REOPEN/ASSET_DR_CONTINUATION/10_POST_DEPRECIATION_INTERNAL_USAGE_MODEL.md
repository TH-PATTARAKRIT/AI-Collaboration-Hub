# 10 — POST-DEPRECIATION INTERNAL USAGE MODEL (LEVEL 12)

**LAYER 2 — AUDIT QUARANTINE.**
Everything in this document is **DESIGN CANDIDATE** except where a row is explicitly
classified otherwise. The mechanism has **no precedent** in the reference product, in
TAS 2, in TAS 16 or in the DBD prescribed statements — it is original SMEsPlus design
and is treated as such throughout.

---

## 1. The case

An asset's accounting depreciation is complete. Book value is the residual, or zero.
The machine continues to run and continues to produce. Under `BD-01` the business
wants that continued contribution measured, without cap, without cut-off, and without
touching the statutory figures.

## 2. What the evidence permits

| Question | Answer | Class |
|---|---|---|
| Does a "fully depreciated" state exist to trigger on? | **No.** The state list is model / draft / running / on hold / closed / cancelled. A run-out asset is simply *running* | `FACT VERIFIED` |
| Can the condition be detected? | **Yes** — the derived residual value reaching zero | `FACT VERIFIED` |
| Is the financial residual protected until then? | **Yes**, for the whole running life | `FACT VERIFIED` |
| Can an off-balance ledger touch financial WIP, FG or expense? | **No — structurally impossible.** Any entry mixing off-balance and on-balance lines is refused by a model constraint | `FACT VERIFIED` (`05` §7) |
| Do off-balance amounts appear in Thai statutory statements? | **No.** The DBD prescribed forms contain no such line | `FACT VERIFIED` (`03` `BLK-04`) |
| Does any standard address a memorandum usage accumulator? | **No** — they do not contemplate one | `FACT VERIFIED` by silence |

The design space is therefore wide and the guardrails are strong. **The isolation
`BD-01` requires is enforceable by construction, not by discipline.**

## 3. The rate base — three candidates, one recommended

`BD-01` fixes that the accumulator is unbounded. It does not fix what accrues per day.

| # | Candidate | Formula | For | Against |
|---|---|---|---|---|
| **A** | **Residual over original lifetime** | `residual ÷ original lifetime days` | Carried from the baseline. Derived entirely from data already held; needs no new judgement; continuous with the depreciation that preceded it | The residual is often a token — the one-baht convention is common in Thailand. A one-baht residual produces a rate of essentially zero and the accumulator measures nothing |
| **B** | **Last effective depreciation rate, frozen** | The daily rate in force in the final period, continued | Continuous in magnitude with the machine's real historical charge; needs no new judgement; immune to a token residual | Perpetuates whatever the original life assumed; a machine that outlives a deliberately short tax life accrues a rate that was never economically meaningful |
| **C** | **Assessed continuing-use value over extended life** | A management estimate, reviewed | Economically the most meaningful; matches what "lifetime contribution" means in the Boss's language | Requires a periodic human judgement, which is a governance surface and a manipulation surface |

**Recommendation: B, with A as the fallback where no depreciation history exists
(migrated assets), and C available as an override that must be recorded, dated and
attributed.**

The reasoning is that **A fails on the most common Thai configuration**. A residual of
one baht over 1,826 days is 0.0005 baht per day. Under `BD-01` that accumulator will
run forever and never reach a number anyone can use. The baseline flagged this as
`UNR-19` — whether A is what the Boss intends — and the evidence now suggests it is not
adequate on its own.

`BLK-09` (`22` §5): the Boss must select. This is not decidable from evidence.

## 4. Effective date and rate maintenance

| Point | Candidate |
|---|---|
| Start | The day after the last statutory depreciation period ends. **Detected**, since no status exists |
| Rate changes | Take effect prospectively only. The accumulator is never restated |
| Rate history | Every rate is a **dated record**, never a mutable field. Non-negotiable — the reference product's habit of silently mutating rate-bearing fields with no audit trail is the specific behaviour the baseline said not to copy |
| Review cadence | Annually, alongside the useful-life and residual review **TAS 16 already requires** (`18` §3). Reusing an existing mandatory control rather than inventing a new one |
| Suspension | While the machine is not operationally eligible for production use — the terminating condition `BD-01` sets |

## 5. Production allocation, WIP and financial-statement isolation

**The hard rule, and it is the whole design:**

> Internal usage is allocated in the **management ledger only**. It never enters
> financial work in progress, financial finished goods, financial cost of sales or
> financial expense. It has no effect on inventory carrying value in the statutory
> financial statements.

Allocation follows exactly the model in `09` — the same machine, the same normal
capacity, the same productive and non-productive causes, the same reconciliation
identity — but posted into the off-balance ledger and reported in management reporting
only.

**Why this cannot leak, structurally:**

1. Every internal-usage entry is composed **entirely** of off-balance accounts.
2. The platform pattern in `05` §7 refuses any entry that mixes classes.
3. The DBD prescribed statements have **no line** in which an off-balance balance could
   appear.

**Why the isolation must nevertheless be tested:** because a design can leak through a
different door. If internal usage were ever allowed to update a product's standard cost,
or to feed a valuation adjustment, it would reach inventory without ever posting an
on-balance line. `15` `EC-27` tests exactly that. The structural firewall protects the
journal; it does not protect a valuation field.

## 6. Disposal — the boundary the design does not yet cover

At disposal the entry writes out the **full original cost**; the residual is not
preserved as an identifiable amount and falls into gain or loss. **A management ledger
that references the financial residual loses its reference at that moment.**

| Option | Consequence |
|---|---|
| Freeze the accumulator at disposal and keep it as a closed historical record | Preserves lifetime contribution as a reportable figure. Requires a terminal memorandum entry |
| Close the accumulator to a management "disposed machines" account | Keeps the off-balance ledger balanced and self-contained |
| Do nothing | The accumulator dangles against a machine that no longer exists, and the off-balance ledger never closes |

**Recommendation: the first two together** — freeze the machine's accumulator, and post
a terminal off-balance entry closing it to a disposal-of-contribution account, so that
the ledger balances and the lifetime figure survives.

**Second-order point that must not be lost:** the internal-usage rate under candidate A
depends on the residual. If the design ever reads the residual *after* disposal it will
read a value that no longer exists. Candidate B does not have this problem, which is a
further argument for it.

## 7. Re-entry — a fully depreciated asset becomes depreciable again

A capital improvement can make a run-out asset depreciable again, at any time. `BD-01`
is silent.

**Recommendation — DESIGN CANDIDATE:**

1. **Suspend** internal usage from the effective date of the improvement. Statutory
   depreciation resumes and is again the primary measure; running both would count the
   same machine twice.
2. **Do not reverse** anything already accumulated. It measured real past contribution.
3. **Resume** internal usage when the new statutory depreciation completes, at a rate
   recomputed on the new basis.
4. **Report** the suspension and resumption as events on the machine's history.

The alternative — running both concurrently — is rejected: the machine would carry a
statutory charge and a management charge for the same hours, and any report combining
them would double count.

## 8. Double-entry control in the off-balance ledger

`BD-01` calls the concept a management/control allocation. It should still be **double
entry**, for three reasons: the platform's constraint (`05` §7) forces every line of an
entry to be off-balance, so a single-sided posting is not expressible; a self-balancing
ledger is auditable and a list of numbers is not; and the reconciliation identity in
`09` §8 needs two sides to reconcile.

Minimal account set — **candidate**, subject to chart-of-accounts design:

| Account | Nature |
|---|---|
| Internal usage — accumulated contribution | Credit-side accumulator, per machine |
| Internal usage — absorbed to production | Debit, mirrors productive absorption |
| Internal usage — non-productive, by cause | Debit, one per cause |
| Internal usage — disposed contribution | Terminal close-out |

All of type off-balance. No other type may appear in these entries.

## 9. Period close, correction and audit trail

| Point | Rule |
|---|---|
| Close | The internal-usage period closes **after** the costing close and independently of the accounting close — `13` §2 |
| Correction | By reversal only. Never by editing a posted management entry. The reference product's immutability discipline is the right precedent and is worth copying wholesale |
| Retrospective change | Permitted in the management ledger where the accounting ledger would forbid it — **but only as a dated correction entry**, never as a silent restatement |
| Audit trail | Every rate is dated and attributed. Every allocation names the machine, the period, the cause, the hours and the rate record it used |
| Reporting | Management reporting only. **Never** a statutory statement, a tax return, or an inventory valuation |

## 10. The proof `BD-01` demands

> *Internal usage must not silently recreate statutory depreciation.*

It cannot, on four independent grounds, each verified rather than asserted:

1. **Account class.** Every internal-usage line is off-balance. A statutory
   depreciation line is on-balance. The platform refuses to mix them in one entry.
2. **Timing.** Internal usage begins **only after** statutory depreciation has
   completed. The two never run for the same period on the same asset — and §7 makes
   that explicit for the one case where they otherwise would.
3. **Base.** Statutory depreciation depreciates the depreciable base and stops at the
   residual. Internal usage begins from the residual or from a frozen rate and has no
   base to exhaust.
4. **Presentation.** Off-balance amounts have **no line** in the Thai prescribed
   statements, so no internal-usage figure can appear in a statutory statement even by
   accident.

Grounds 1 and 4 are `FACT VERIFIED` from primary evidence obtained this session.
Grounds 2 and 3 are properties of this design and hold only if it is built as specified.
