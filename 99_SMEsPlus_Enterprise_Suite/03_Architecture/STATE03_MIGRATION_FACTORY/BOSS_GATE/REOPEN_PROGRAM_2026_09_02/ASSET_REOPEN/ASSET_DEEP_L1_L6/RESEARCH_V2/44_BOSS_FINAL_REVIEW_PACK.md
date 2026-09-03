# 44 — BOSS FINAL REVIEW PACK
**LAYER 1 — CLEAN ROOM.** This is the only file in this package cleared to seed
downstream SMEsPlus material. It contains no reference-system model names, field
names, file paths or line references.

Session `SMEPLUS-26-09-04-ASSET-DEEP-L1-L6-001` · 2026-09-04
Boss is the sole Final Approver. Nothing here is an approval, a freeze, or a
development authorisation.

---

## A. ASSET DOMAIN STATUS

**Terminal state: Asset Deep Levels 1–6 complete to maximum available evidence.
Material blockers remain. Ready for Boss Final Review Gate.**

All six levels executed. Nothing skipped. Six items still block **design**
decisions; none of them blocks **understanding** of the domain.

## B. DEEP LEVEL 1–6 COVERAGE

| Level | Subject | Coverage |
|---|---|---|
| 1 | Domain, scope, capability, boundary | Complete — 34 capabilities classified |
| 2 | Menu, screen, field, source learning | Complete — full field register, visibility analysis, seven misleading labels identified |
| 3 | Function forensic | Complete — 26 functions verified, 1 contradicted, 15 gaps |
| 4 | Cross-module relationships | Complete — exhaustive negative established across the whole reference product |
| 5 | Whole-system semantic model | Complete — full lifecycle, four-truths model, all Boss hypotheses tested |
| 6 | Contradiction, boundary, failure | Complete — 60+ failure cases; 8 attacks declared unexecutable |

## C. WHAT WE KNOW NOW

1. **The reference system's depreciation engine is genuinely well built.** It is
   immutable by construction — a posted entry is never edited, only reversed. Its
   arithmetic self-corrects, so a schedule always totals exactly to the amount to be
   depreciated, with no balancing adjustment. Sixteen adversarial tests, including
   29 February, month-end acquisition and single-day periods, all balanced to the
   satang. **These properties are worth transferring to SMEsPlus.**

2. **The engine offers two incompatible ways of counting days**, chosen by one
   setting. One treats every month as 30 days and every year as 360 — February and
   January depreciate identically and leap years do not exist. The other uses the
   real calendar. **The first is the product's default.**

3. **The difference is invisible annually and large monthly.** On a 1.2 million baht
   asset over five years:

   | | Real-calendar basis | 30/360 basis | Difference |
   |---|---|---|---|
   | A 31-day month | 20,372.40 | 20,000.00 | +1.86% |
   | **February (28 days)** | **18,400.87** | **20,000.00** | **−8.00%** |
   | February (29 days) | 19,058.05 | 20,000.00 | −4.71% |
   | **Full year** | **239,868.57** | **240,000.00** | **−0.05%** |

   Because the design routes depreciation into **monthly** product cost, this is not
   a presentational matter. Under the default, February's machine cost is overstated
   by 8% every year — and no annual reconciliation will ever reveal it.

4. **The "Thai daily depreciation" the business relies on was built by this
   project's own vendor, on the previous system generation.** No copy of it was found
   anywhere in the current generation's code in this workspace.

5. **But it is reproducible by a setting.** This session reconstructed both
   arithmetics and ran them side by side. They agree to within **0.03 baht per
   period** and **0.01 baht cumulative** on a 1.2 million baht asset, across
   month-start, mid-month, short-month and month-end acquisitions. **The capability
   is not lost. What is unverified is whether the right setting is selected.**

6. **Thai law does require pro-rating from the acquisition date.** Confirmed from
   the Revenue Department's own published text of the Revenue Code and of the
   governing Royal Decree. The Decree's rates by asset class are **maximums, not
   required schedules**.

7. **The two halves of a machine are modelled twice and never joined.** The
   financial record knows the cost and knows nothing operational. The operational
   record knows the machine and knows nothing financial. Nothing in the reference
   product connects them.

8. **This project already built the only bridge that exists** — a manual dropdown on
   the financial record pointing at the machine record.

9. **Production costing already works — from the wrong input.** Machine cost does
   reach work orders, work-in-progress, finished goods and cost of sales, and it does
   post to the ledger. It starts from **an hourly rate a person types in**, with no
   connection to depreciation and no machine dimension at all.

10. **Maintenance records no cost at all.** Not "the cost does not flow" — a
    maintenance request has **no money field of any kind**. Its only effect on
    production is to block machine availability.

## D. WHAT WE THOUGHT BEFORE THAT WAS WRONG

The previous Asset session recorded that no source code or database access existed
and worked from public documentation. **That was incorrect.** Complete source for
both system generations, this project's own custom modules, and live read-outs of
the pilot database were all available. Every prior conclusion was re-derived.

| Prior conclusion | Now |
|---|---|
| No code or data access exists | **Corrected** — it did |
| No native machine↔asset link | **Confirmed**, and upgraded from inference to proof |
| Maintenance cost does not flow to production | **Confirmed and strengthened** — no maintenance cost exists to flow |
| Thai daily depreciation: partially supported | **Split** — pro-ration now proven from statute; the *daily unit* remains practice, not proven statute |
| Post-depreciation usage formula is original design | **Confirmed** |
| No contradictions found | **Superseded** — six are now registered |

Two further corrections were made **within** this session and are preserved in full,
because both nearly produced serious errors:

- A custom module was briefly judged unable to load. Reading its package initialiser
  showed otherwise — **and that same check is what uncovered a real defect** (see I).
- The custom Thai method was briefly judged **non-compliant**, because it appeared to
  charge a full month in the acquisition month. Read together with the routine that
  calls it, it prorates correctly. **The accusation was withdrawn before it was made.**

## E. BOSS ASSERTIONS VERIFIED

| Assertion | Result |
|---|---|
| Depreciation should be computed on a daily basis, from total calendar days including leap years | **Confirmed as a description of the mechanism** |
| A job should carry only the cost of the machines it actually used | **Confirmed** — and the reference model structurally cannot do it |
| Production allocation configuration belongs to the production context, not to the asset template | **Supported** — the asset template governs nothing after creation, and on the pilot database governs nothing at all |
| Financial residual must not be reduced by internal usage | **Confirmed** — the residual is excluded from depreciation and protected for the whole running life |
| Off-balance must not cross into financial work-in-progress, finished goods or expense | **Confirmed and stronger than stated** — the product already forbids off-balance accounts on the asset's own accounts, structurally |
| Do not hard-code monthly logic; derive from a daily basis | **Confirmed, and shown to be necessary** — this is the assertion the evidence most strongly vindicates |

## F. BOSS ASSERTIONS CONTRADICTED

**None about the business.** Two carried an implicit technical assumption the
evidence does not support:

1. That daily computation is what the system does **by default**. It is one of three
   options, and it is not the default.
2. That the daily **unit** is a legal requirement. Pro-ration from acquisition is
   legally required; that the unit is the *day* rather than the *month* is standard
   Thai practice and is **not stated** in the statutory text retrieved.

## G. WHAT THE REFERENCE SYSTEM CONTAINS

A closed financial sub-ledger: acquisition from supplier invoices, three
depreciation methods, three day conventions, pause and resume, re-evaluation up and
down, disposal and sale with gain or loss, cancellation with full reversal, a
depreciation schedule report, and a management-accounting dimension carried on every
entry.

## H. WHAT IT DOES NOT CONTAIN

No tax book. No asset transfer, split or merge. No impairment. No revaluation
reserve. No component depreciation. No capitalisation or under-construction stage.
No "fully depreciated" status. No sub-ledger-to-ledger reconciliation. No
foreign-currency assets. No connection whatsoever to machines, maintenance, work
centres, operations or production cost.

**The absent tax book is the largest single gap for a Thai deployment**, because the
statutory rates are ceilings and the accounting life is the company's own judgement
— which is exactly the situation that produces a book/tax difference. A system with
one schedule cannot hold two answers.

## I. WHAT IS CUSTOM — AND WHAT IS BROKEN IN IT

The machine↔asset bridge is a custom addition by this project's vendor. Forensic
review found **three of its four intended behaviours do not execute**, and none of
them reports an error:

1. **Selling or disposing of an asset was meant to retire the linked machine record.
   It does not.** The code exists in a file the module never loads. Sold machines
   stay active in the operational register.
2. The rule restricting the link to draft assets **does not apply**; the link can be
   changed on running and closed assets.
3. The display behaviour that was meant to show the machine's reference **never
   fires**.

Additionally, the link has **no uniqueness rule**: several assets may claim the same
machine, with nothing preventing, warning or reporting it.

**This is the single most actionable finding in the package.** It is also a warning
about a class of risk: custom code that is present, reviewed, believed in, and
silently doing nothing.

## J. WHAT SMEsPLUS SHOULD LEARN

1. The schedule **is** the ledger entries — not a separate table that must be
   reconciled to them.
2. Never edit a posted entry. Catch up, reverse the future, rebuild forward.
3. Compute each period from the cumulative total, not by repeating a per-period
   amount. Rounding then cannot drift.
4. Treat value as a derivation, never as a stored column.
5. Make status read-only and every transition a guarded operation.
6. Enforce boundaries structurally, the way the product already forbids off-balance
   accounts on asset accounts — not by policy.
7. Copy the cancellation audit message: every reversed entry listed, with the net
   effect on both accounts.

## K. WHAT SMEsPLUS SHOULD NOT COPY

1. The 30/360 convention as a default.
2. The option that backdates depreciation to the start of the financial year.
3. Labels that misdescribe behaviour — most of all the one that silently chooses
   between two day conventions.
4. Five different accounting events behind one button.
5. Fields that change money and are invisible on screen.
6. A single hourly rate that merges the cost pool and the allocation basis — this is
   precisely why the reference model cannot answer "which machine".
7. Changing the day convention, the method, the accounts or the management dimension
   **with no audit trail** — as the reference product allows today.

## L. VERIFIED FUNCTION GAPS

Machine-to-operation link · machine cost pool · depreciation-to-production-rate
derivation · maintenance cost · idle and downtime cost · absorption variance · tax
book · capitalisation stage · asset transfer · impairment · component depreciation ·
reconciliation · fully-depreciated status · divergence reporting.

## M. MACHINE ↔ ASSET FINDINGS

See G, H and I. In one sentence: **buying a machine creates two records, by two
people, from two documents, joined by an optional manual dropdown whose maintenance
behaviours do not run.**

## N. MANAGEMENT-DIMENSION FINDINGS

The dimension is inherited from the supplier invoice, weighted by value, then copied
onto every depreciation entry as it is created. Changing it affects **future entries
only**, silently, with no audit trail and no report of the divergence.

It is a **tag, not an allocation engine** — it records where cost went; it does not
decide.

It is also the one place the financial and production sides already meet in the same
ledger, which makes it **the cheapest place to prove the costing concept before any
structural change** — and the first place double-counting will appear if the design
is careless.

## O. DEPRECIATION ENGINE FINDINGS

See C1–C3. Additionally: "duration" means a number of **periods**, whose length is
set by a different field, so a duration of 60 can mean five years or sixty. A
mid-month purchase correctly produces **61 monthly entries** for a five-year asset,
and the partial first and partial last entries sum to exactly one full period.

## P. DAILY CALCULATION FINDINGS

See C4 and C5. The custom Thai method and the product's real-calendar setting are
**numerically equivalent within rounding**. The remedy for the migration is a
setting, not a rebuild — **once we confirm which setting the live assets carry.**

## Q. RESIDUAL FINDINGS

The residual is excluded from depreciation and protected for the entire running life
— the design premise holds.

**Two boundary conditions the design does not yet cover:**

1. **At disposal the residual does not survive as an identifiable amount.** The
   entry writes out the full original cost, and the residual falls into the gain or
   loss. If the management ledger references the financial residual, it loses its
   reference at that moment.
2. **A fully depreciated asset can be made depreciable again** at any time by a
   capital improvement. What internal usage does then is undefined.

There is also **no "fully depreciated" status to react to**. The switch into internal
usage mode must be **detected** by SMEsPlus, not observed.

## R. DISPOSAL FINDINGS

Correct and standard: full original cost out, accumulated depreciation out, proceeds
in, balance to gain or loss, with the management dimension on every line. Selling
requires a posted customer invoice.

One inconsistency: the system **also** stores a separate gain figure computed on a
different basis, which can differ from the posted one by exactly the residual. It is
not shown on screen. **SMEsPlus must not read that stored figure.**

## S. CROSS-MODULE FINDINGS

Across the whole reference product — 797 modules — the asset record is referenced by
**three**, none of them operational. This is an exhaustive negative, not a failed
search.

## T. PRODUCTION COST EXTENSION FINDINGS

**This is the finding that most changes the size of the work.**

Of nineteen links from asset through to cost of sales, **ten already exist and
work**. The absorption machinery — work order cost, work-in-progress, finished goods
valuation, the ledger entry, cost of sales — is complete and reusable.

What is missing is the **front** of the chain: deriving the rate from depreciation,
and giving the operation a machine dimension so that usage can be measured per
machine rather than per work centre.

**Recommended order, and the reason for it:**

1. **Repair the machine↔asset link** — everything keys on it and today it is
   optional, duplicable and partly inert.
2. **Give the operation a machine dimension** — without it the machine-hour basis has
   no measurement.
3. **Derive the cost pool from the asset sub-ledger.**
4. **Design what happens to unabsorbed cost, and to the variance between absorbed and
   actual** — the reference chain computes neither.
5. **Handle timing**: the reference chain recognises machine cost when the order
   **completes**, not when the machine ran, and copies the rate onto a work order when
   it is created. Both will defeat a monthly-derived rate unless designed around.

Steps 1 and 2 are unglamorous and are the entire foundation.

## U. POST-DEPRECIATION INTERNAL USAGE FINDINGS

The mechanical premise is verified. The mechanism has **no precedent** in the
reference system or in any accounting standard consulted — it is original SMEsPlus
design, correctly treated as a design candidate throughout.

The instruction to derive from a **daily**, not monthly, basis is **vindicated**: the
two conventions differ by 8% in February.

**Three holes the hypothesis does not yet cover**, raised independently by the
reviewers: no terminating rule for the accumulating usage; no defined behaviour at
disposal once the residual is absorbed; and no defined behaviour if the asset becomes
depreciable again.

## V. OFF-BALANCE FINDINGS

Confirmed as an account classification. The boundary Boss asked to be maintained by
policy is, on the asset side, **already enforced by the product structurally** — which
is a good precedent to follow.

**Two things are unestablished and both matter:** whether off-balance accounts are
permitted anywhere in the production-costing path, and **how accounts of that class
are treated in Thai statutory financial statements**. The management ledger rests on
the second.

## W. THAI ACCOUNTING AND TAX FINDINGS

| Point | Status |
|---|---|
| Depreciation must be deducted in proportion to the period from acquisition | **Proven from statute** |
| Rates by asset class are **maximums**, not schedules | **Proven from statute** |
| Part accounting periods are apportioned | **Proven from statute** |
| The apportionment unit is specifically the **day** | **Practice, not proven statute** — routed to the Accounting-Tax track |
| Thai standards require useful-life and residual review, and component depreciation | Reference system provides **neither** |
| Whether depreciation may be absorbed into inventory value under Thai practice | **Unknown, and it gates the costing design** |

## X. CONTRADICTIONS

| # | Contradiction | Severity |
|---|---|---|
| 1 | The configured depreciation method has no verified implementation on the target generation | **High** — reduced by finding it reproducible by a setting |
| 2 | The machine-link module's disposal behaviour does not execute | Medium; **High as a class of defect** |
| 3 | On the old system, the daily-depreciation capability and the machine-link capability were attached to **two different asset records** — no single legacy record ever had both | Medium |
| 4 | Confirming an asset silently changes an operational record, with no way back | Medium |
| 5 | The posted gain on disposal and the stored gain can differ by the residual | Low in the ledger; Medium for anything reading the stored value |
| 6 | The rule guaranteeing a schedule closes to zero is enforced only by the application, and the live data was bulk-loaded | Medium |

**Contradiction 3 deserves a moment.** Any recollection of "the old system's asset,
with its machine link, depreciating daily" is a composite of two different records.
This matters because that composite has been serving as the migration target.

## Y. UNRESOLVED ITEMS THAT BLOCK DESIGN

| # | Item | Why unknown | Impact | Owner |
|---|---|---|---|---|
| 1 | **Which day convention the 217 live assets actually use** | Not captured in the read-out; the model export's origin is unclear | Every monthly figure, and the migration of 280 assets | **One pilot-database query** |
| 2 | **Whether several assets share one machine record** | Nothing constrains or reports it | A duplicated machine's cost pool doubles | **One pilot-database query** |
| 3 | **Whether Thai practice permits depreciation absorbed into inventory** | Not a software question | **Gates the whole costing design** | Accounting-Tax track |
| 4 | **How off-balance accounts appear in Thai statutory statements** | Never established | Gates the management ledger | Accounting-Tax track |
| 5 | **May internal usage accumulate without bound?** | No precedent; reviewers split | Whether lifetime contribution is durable or ever-growing | **Boss** |
| 6 | **Where unabsorbed depreciation goes** | A policy choice | Product cost accuracy | **Boss** |

**Four of the six need a decision, not research. Two need minutes on the pilot
system.**

**Everything in this package that says "does not exist" is bounded by the code
available in this workspace.** The installed module list of the live system was never
obtained. That qualifier cannot be dropped until it is.

## Z. AAS+ RECOMMENDATIONS

1. **Run one pilot-system evidence session.** Nine open items close in it, including
   the highest-priority blocker.
2. **Route the two Thai questions to the Accounting-Tax track now**, in parallel.
   They gate the design and neither is answerable from software.
3. **Repair the machine↔asset link before designing anything that depends on it.**
4. **Decide the two Boss policy questions**: the bound on internal usage, and the
   treatment of unabsorbed depreciation.
5. **Treat the day convention as an explicit, recorded decision per asset** — not as
   an inherited default.
6. **Do not treat any "does not exist" finding as final** until the live system's
   installed modules are known.

**Recommended terminal state: READY FOR BOSS FINAL REVIEW GATE.**
No approval, freeze, or development authorisation is claimed or implied.
