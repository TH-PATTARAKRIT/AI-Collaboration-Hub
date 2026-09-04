# 05 — ASSET ACCOUNTING FORENSIC REPORT (LEVEL 8)

**LAYER 2 — AUDIT QUARANTINE.** Contains reference-ERP model and field technical names.

Scope: the 22 subjects listed in §5 Level 8 of the governing prompt. Levels 1–6
established the mechanism in detail; this report does **not** repeat that work. It
does three things the baseline did not: it re-verifies the load-bearing mechanisms
from primary source, it separates **financial accounting truth** from **management
cost allocation** subject by subject, and it records what the separation costs.

---

## 1. The separation, stated once

Everything in this report belongs to exactly one of two columns.

| | **Financial accounting truth** | **Management cost allocation** |
|---|---|---|
| Governed by | TFRS/TAS, the Revenue Code, DBD prescribed forms | Boss policy |
| Recorded in | The statutory ledger | The management ledger |
| May be restated | Only by a valid accounting event | Freely, by policy, with audit trail |
| Presented in the statutory statements | Yes | **No — there is no line for it** (`03` `BLK-04`) |
| Bound by the residual | Yes — protected | **No** (`BD-01`) |

The single most important structural finding of this session is that the reference
platform makes this separation **enforceable rather than aspirational**. See §7.

---

## 2. The 22 subjects — status after re-verification

| # | Subject | Column | Mechanism status | Notes |
|---|---|---|---|---|
| 1 | Capitalisation | Financial | Present, indirect | Created from vendor bill lines through an account flag; there is no capitalisation *stage* and no assets-under-construction concept |
| 2 | Asset model | Financial | Present, **inert in practice** | A template that copies method, duration, accounts and analytic distribution at creation and governs nothing afterwards. On the pilot data **all 280 assets carry no model link** |
| 3 | Category / type semantics | Neither | **Absent as behaviour** | The grouping object carries no behaviour whatsoever. Class-based rules — the shape Thai tax law uses — have nowhere to live |
| 4 | Acquisition cost | Financial | Present | `original_value`, from the originating bill lines |
| 5 | Depreciation start | Financial | Present, **three-valued** | `prorata_computation_type` ∈ {`none`, `constant_periods`, `daily_computation`}. Default `constant_periods`. `none` **backdates the start to the fiscal-year opening**, which is a different accounting answer, not a rounding difference |
| 6 | Depreciation schedule | Financial | Present, and good | The schedule **is** the set of journal entries. There is no separate table to reconcile. This property is worth transferring |
| 7 | Depreciation method | Financial | Present, three | `linear`, `degressive`, `degressive_then_linear`. No units-of-production method, and none is required by Thai law |
| 8 | Useful life | Financial | Present, **ambiguous label** | `method_number` is a count of *periods*; `method_period` sets whether a period is 1 or 12 months. A duration of 60 therefore means five years or sixty, depending on a second field |
| 9 | Residual value | Financial | Present, protected | Excluded from the depreciable base for the whole running life |
| 10 | Accumulated depreciation | Financial | Derived, not stored | A consequence of the posted entries |
| 11 | Book value | Financial | Derived, not stored | Correct by construction |
| 12 | Disposal | Financial | Present, standard | Cost out, accumulated depreciation out, balance to gain or loss |
| 13 | Retirement | Financial | Present | Same path as disposal, without proceeds |
| 14 | Sale | Financial | Present | Requires a **posted customer invoice** |
| 15 | Impairment | Financial | **Absent** | No impairment concept exists |
| 16 | Write-off | Financial | Present as disposal | Not distinguished from retirement |
| 17 | Maintenance vs capitalisation | Financial | **Absent as a decision** | Nothing in the product distinguishes a repair from an improvement. `24`(baseline) records that a capital improvement is expressible only as a re-evaluation |
| 18 | Reclassification | Financial | **Absent** | No transfer, split or merge |
| 19 | Accounting-period interaction | Financial | Partial — see §5 | |
| 20 | Year-end adjustment | Financial | Absent as a concept | No year-end true-up; the arithmetic self-corrects instead |
| 21 | Manual adjustment controls | Financial | **Weak** — see §6 | |
| 22 | Correction / reversal | Financial | Present, and good | A posted entry is never edited. Draft entries are unlinked; posted entries are reversed |

`FACT VERIFIED` for every row, from primary source, this session or in the baseline.

---

## 3. The day convention, re-verified

The three modes and their arithmetic:

| Mode | Lifetime in days | Period share | Effect |
|---|---|---|---|
| `none` | `periods × 30` | Constant | **Start date is moved to the fiscal-year opening.** Depreciation is charged for a period the entity did not own the asset |
| `constant_periods` **(default)** | `periods × 30` | Constant | Every month is 30 days, every year 360. February and January are identical. Leap years do not exist |
| `daily_computation` | Real calendar days between prorata date and end | Days in the actual period | Real calendar |

The constants are literal in source: thirty days per month, three hundred and sixty
per year.

**This is not a presentation matter, because depreciation is destined for monthly
product cost.** `08` §2 re-derives the numbers.

**`none` deserves separate condemnation.** It is not a less precise pro-ration; it is
the absence of pro-ration plus a backdated start. Thai law requires deduction in
proportion to the period **from acquisition**. A mode that starts at the fiscal-year
opening produces a figure the Revenue Code does not permit. SMEsPlus must not offer it.

---

## 4. Where the financial and management columns already meet

One place, and only one: the **analytic distribution**.

- It is inherited from the originating vendor bill line, weighted by value.
- It is copied onto every depreciation entry **as that entry is created**.
- Changing it on the asset rewrites only entries still in draft. Posted entries keep
  the old distribution.
- Nothing reports the divergence between an asset's current distribution and the
  distributions actually carried by its own posted entries.

It is a **tag, not an engine**: it records where cost went; it does not decide.

**Design consequence.** This is simultaneously the cheapest place to prove the costing
concept before any structural change, and the first place double counting will appear
if the design is careless — because if depreciation reaches product cost *both* through
an analytic tag *and* through a derived machine rate, nothing in the platform notices.

---

## 5. Accounting-period interaction — what is guarded and what is not

| Path | Lock-date guard | Verified |
|---|---|---|
| Disposal | **Yes** — explicit refusal before the lock date | Source |
| Modify / re-evaluate | **Yes** | Source (baseline) |
| Write to an asset that would rewrite entry accounts | **Yes, partially** — accounts and journal are rewritten only on entries dated **after** the lock date | Source, this session |
| **Confirm** (`validate`) | **No explicit guard in this module** | Source |
| Pause | **No explicit guard in this module** | Source |

Confirm is the exposure that matters: confirming an asset generates and posts its
**entire depreciation life at once**. If an asset with a past acquisition date is
confirmed while an earlier period is locked, whether it is stopped depends entirely on
the posting layer beneath, which cannot be determined from this module.

Five lock dates exist at company level — fiscal year, tax, sale, purchase and a **hard**
lock — each with a per-user variant. The hard lock is the one that cannot be overridden.

**Design ruling for SMEsPlus (`19` §7):** guard the confirm path explicitly. The
correct behaviour is identical whether or not the platform beneath happens to catch it,
so this does **not** need the UAT to decide — only to describe the current system.

---

## 6. Manual adjustment controls — the weakness

The following can be changed on a running asset **with no audit trail and no report of
the divergence**:

- the day convention,
- the depreciation method,
- the depreciation and expense accounts,
- the analytic distribution.

The first is the most dangerous, because the label on that field says "Computation"
and gives no indication that it silently selects between two arithmetics that differ
by eight per cent in February.

There is also an import field for already-depreciated amounts. It is the sanctioned
way to make the sub-ledger and the ledger disagree, and nothing reconciles them —
because there **is** no sub-ledger-to-ledger reconciliation report.

---

## 7. The structural firewall — the session's most useful positive finding

The platform enforces a model-level constraint on every journal entry:

> If any line of an entry uses an account of type **off-balance**, then **every** line
> of that entry must use an account of that type. Off-balance lines may carry no tax
> and may not be reconciled.

This is a validation constraint on the journal-item model, not a UI domain and not a
policy. `sudo()` does not bypass it.

**Four consequences, all favourable:**

1. An off-balance management ledger **cannot** post into financial WIP, finished goods
   or expense. Not "should not" — cannot. `BD-01`'s isolation requirement is
   enforceable at the platform layer.
2. The management ledger is necessarily **self-contained double entry**. It cannot
   half-post.
3. This is a **pattern SMEsPlus should copy verbatim** — the baseline recommended
   enforcing boundaries structurally, and here is the exact mechanism to imitate.
4. It answers the baseline's open item on whether off-balance accounts are permitted
   in the production-costing path. They are **selectable and not postable** — which
   creates the trap in §8.

---

## 8. The trap the firewall creates

The work-centre object carries an **expense account** field. Unlike the asset module's
account fields, it has **no domain excluding off-balance accounts**. A configurer can
therefore select an off-balance account there.

Nothing complains at configuration time. The labour entry generated at manufacturing
order completion would then contain one off-balance line and one on-balance stock
line, violating the constraint. **The failure surfaces when a manufacturing order is
marked done — not when the account is chosen.**

Classified `FACT VERIFIED` from source (absence of the domain; presence of the
constraint; the entry's two-account construction). The user-visible failure mode is
`SOURCE-SUPPORTED INTERPRETATION` — it follows necessarily from the three verified
facts but has not been executed. Registered as `CTR-C-05` in `17`.

**SMEsPlus ruling:** every account selector on a costing object carries the same
exclusion domain the asset module already applies. Cheap, and it moves the failure
from month-end to configuration time.

---

## 9. Two boundary conditions the design still does not cover

Both carried unchanged from the baseline; neither is closed by anything found this
session.

1. **At disposal the residual does not survive as an identifiable amount.** The entry
   writes out the full original cost; the residual falls into gain or loss. Any
   management ledger that references the financial residual **loses its reference at
   that moment**. Addressed as a candidate in `10` §6.
2. **A fully depreciated asset can become depreciable again** through a capital
   improvement, at any time. What internal usage does then is undefined. Addressed as
   a candidate in `10` §7.

And one thing that is missing rather than uncovered: **there is no "fully depreciated"
status.** The state list is model, draft, running, on hold, closed, cancelled. An asset
whose value has run to zero is still simply *running*. The switch into internal-usage
mode must therefore be **detected** by SMEsPlus — by testing the derived value — not
observed from a status.
