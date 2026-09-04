# 25 — BOSS FINAL GATE PACK

**LAYER 1 — CLEAN ROOM.** This is the only file in this package cleared to seed
downstream SMEsPlus material. It contains no reference-system model names, field names,
file paths or line references.

Session `SMEPLUS-26-09-04-ASSET-DR-CONT-001` · 2026-09-04
Boss is the sole Final Approver. **Nothing here is an approval, a freeze, or a
development authorisation.**

Boss should not need to read any other artefact. Where a detail is needed, the artefact
is named.

---

## 1. Executive summary

Research from Level 7 to Level Final is complete. Six blockers were reported at the last
gate; on reconciliation there were seven. **Four are now closed.** Two closed because the
Boss decided them. **Two closed on primary Thai statutory evidence obtained for the first
time in this session** — and the answers were better than hoped.

The headline is this: **Thai accounting standards do not merely permit the SMEsPlus
costing proposition — they require it.** The depreciation of production machinery must be
absorbed into the cost of inventory. That was the precondition for the whole design, and
it is now settled from the standard's own text.

But the same paragraph that settles it also **constrains how**. The allocation must be
based on **normal capacity** — what the machine would normally produce — and **not** on
whatever hours it actually happened to run. Anything left unallocated must be charged to
the period as an expense. This matters because the most natural way to implement the
Boss's 100% attribution rule breaks that requirement, while a second, equally faithful
way satisfies it. **The Boss's instruction does not choose between them, and this session
will not choose on the Boss's behalf.** That is the single decision this gate most needs.

Two new blockers therefore replace the two that closed. The arithmetic is coincidental;
the substance moved a long way.

Two blockers remain unchanged, both needing minutes on the pilot system, which this
session could not reach.

## 2. What we knew before

Levels 1–6 established the mechanism of the reference system in full. In short: the
depreciation engine is genuinely well built and immutable by construction; it offers two
incompatible ways of counting days and the wrong one is the default; the "Thai daily
depreciation" the business relies on was built by this project's own vendor on the
previous system generation and is reproducible by configuration; the financial and
operational records of a machine are modelled twice and joined nowhere except by a
custom manual link whose maintenance behaviours largely do not run; production costing
works end-to-end but starts from an hourly rate a person types in; and maintenance
records no cost at all.

Six items blocked design: two answerable on the pilot system, four needing a decision.

## 3. What new deep research proved

1. **Thai accounting standards require the depreciation of production equipment to be
   part of the cost of inventory.** Established from the standard's own text, which names
   the depreciation and maintenance of factory buildings and factory equipment expressly.
   This was the largest open question in the programme.
2. **They also prescribe the basis.** Fixed production overhead is allocated on **normal
   capacity**, taking account of capacity lost to **planned** maintenance. The per-unit
   charge **must not rise** when production falls or stops. Anything unallocated is
   **expensed in the period**. In an unusually busy period the per-unit charge must be
   **reduced** so that stock is not carried above cost.
3. **Off-balance amounts have no place in Thai statutory financial statements.** The
   prescribed statement formats contain no line for them. The management ledger cannot
   appear in the statutory accounts — which is exactly the isolation required.
4. **The platform makes that isolation structural, not a matter of discipline.** Any
   accounting entry that mixes off-balance and ordinary accounts is refused outright.
   The management ledger **cannot** reach work in progress, finished goods or expense.
5. **No mechanism for normal capacity, or for the difference between absorbed and actual
   cost, exists anywhere in the reference product** — across all 797 of its modules. This
   is not a gap to be configured around. It must be built.
6. **The reference product treats a fixed cost as if it were variable.** It charges
   machine cost as actual hours times a rate. For depreciation, the standard does not
   permit that.
7. **A usable downtime structure already exists** — named causes grouped into a small set
   of categories, recorded against real time intervals, able to represent idleness with
   no job attached, and measured against the working calendar so weekends do not become
   downtime. It carries no money. **The structure is the hard part and it is already
   there.**
8. **Maintenance already distinguishes planned from unplanned work.** That distinction
   turns out to be exactly what the standard requires, and it needs no new data capture.
9. **Component depreciation is required** by Thai standards where a component's cost is
   significant — a machine's frame, mould and belt each with their own life. Neither the
   reference product nor the current design supports it.
10. **Life and residual value must be reviewed at least annually.** No such review
    mechanism exists today. It can carry two other controls with it at no extra cost.

## 4. What changed from Levels 1–6

Four mechanism corrections. None reverses a business conclusion; all four change what
must be built.

| Was | Now |
|---|---|
| The machine rate is fixed onto a job when the job is created | **Fixed at completion, not creation** |
| That fixing protects the cost | **It does not.** The valuation and the accounting entry both ignore it and read the current rate. A stored value nothing consumes |
| Off-balance isolation is enforced on the asset side | **Enforced across the whole platform, on every entry.** Stronger and more useful |
| One piece of the custom link is dead code | **Four pieces are.** Two are harmless superseded duplicates; two are not |

And one defect not previously recorded: **the custom link's claim on a machine is
one-way.** Confirming an asset marks a machine as claimed. **Nothing ever unmarks it** —
not cancellation, not deletion, not disposal. A machine claimed by a cancelled asset is
permanently invisible to every future asset, with no way back through the screen.

## 5. Boss decisions incorporated

| Decision | Status | Effect |
|---|---|---|
| Internal usage accumulates without cap | **Incorporated in full.** Closes a blocker | The isolation it requires is now structurally guaranteed, not merely promised |
| Every period 100% attributed, non-productive classified by cause | **Incorporated, and extended by statute.** Closes a blocker | Raises the two new decisions in §10 |
| The work centre is not a generic averaging bucket | **Vindicated.** The reference model structurally cannot do what it asks | Sets the first two build steps |
| One allocation method per context | **One declared departure** | The standard requires two methods — one for fixed cost, one for variable. Boss confirmation requested |

**No Boss assertion about the business was contradicted by anything found.**

## 6. Verified architecture

Four kinds of truth, kept apart, because every serious failure found in this research is
a collapse between two of them:

- **Financial** — what we paid and what it is worth. Governed by law and standards.
- **Operational** — which machine exists, where it is, what it did.
- **Costing** — how much of the financial truth attaches to which product. Governed by
  the standard, within Boss policy.
- **Management** — what a machine still contributes after its accounting life. Governed
  by Boss policy alone.

Costing writes to the statutory accounts. **Management never does.**

## 7. Design candidates

All design content is a candidate. Nothing is frozen. The main ones:

- A machine dimension on the production operation, so a job can name the machine it used.
- A unique, same-company, two-way link between the financial record and the machine.
- Machine-to-resource-group membership as a **dated record**, not a field, so history
  survives.
- A **normal capacity register** per machine, dated.
- A machine cost pool, with fixed and variable cost held **separately**.
- A period reconciliation, per machine, that must close to exactly zero — and which
  **gates** the close.
- An off-balance management ledger for post-accounting-life usage.
- Depreciable **components** within an asset.

## 8. Contradictions

Sixteen open — six inherited, ten new; five serious. The three the Boss should know
about:

1. **Two ways to read the 100% rule.** One breaks the standard. Both satisfy the
   instruction as written. §10.
2. **The date problem.** The accounting entry for machine cost is dated on the day it is
   posted, not the day production happened. Complete a December job on 3 January and the
   cost lands in January, permanently, with nothing flagging it.
3. **Machine cost only reaches stock value under two of the three costing methods**, and
   only reaches the accounts under one of the two valuation modes. A design that assumes
   it always does will be quietly wrong for a whole class of products.

And one that has now been reported twice without changing anyone's plan: on the previous
system generation, **daily depreciation and the machine link were attached to two
different asset records.** No single old record ever had both. Any migration target
described as "the old system's asset, with its machine link, depreciating daily" is a
composite that never existed.

## 9. Remaining unknowns

Nine non-blocking items, listed in the blocker register. The three worth naming:

- **How a standard-costed product complies.** The requirement is stated; the mechanism
  is not designed. Raised by the independent audit against this research.
- **What rate the internal usage accumulator should accrue at.** Three candidates, none
  supported by evidence. The obvious one — based on the residual value — **fails on the
  most common Thai configuration**, where the residual is one baht.
- **Whether the Revenue Department accepts the same absorbed figure for tax.** Not
  researched. It does not block, because the accounting treatment is mandatory either way.

## 10. Remaining blockers — four

| # | Blocker | Type | Who closes it |
|---|---|---|---|
| 1 | **Is the allocation rate based on normal capacity, or on actual hours?** | Decision | **Boss** |
| 2 | **Does planned maintenance get treated differently from unplanned?** | Decision | **Boss** |
| 3 | Which day-counting convention the 280 live assets actually use | Verification | One query |
| 4 | Whether more than one asset points at the same machine | Verification | Two queries |

**Blocker 1 is the important one.** Dividing a month's depreciation across that month's
actual hours attributes 100% and satisfies the instruction — and it means that in a slow
month every product costs more, which the standard expressly forbids, and in an idle
month the sum is undefined. Dividing instead by **normal capacity** and treating the
remainder as a classified period expense attributes 100% just as completely, and
complies. **Recommendation: normal capacity.**

**Blocker 2.** The standard puts planned maintenance *inside* normal capacity, so it is
recovered through the rate; unplanned breakdown is outside and must be expensed. The
Boss's list treats maintenance as one thing. Treating it as one thing misstates stock
value and period expense in opposite directions at the same time. **Recommendation:
split it.** The data already exists.

## 11. UAT results and requirements

**No UAT was performed. No result is claimed, estimated or inferred.** The pilot system
was not reachable from this session: the local runtime's database access was refused by
the execution environment, and no network route to that database exists in this
workspace. This is declared, not worked around.

Nine read-only queries are specified in the blocker register. Four are priority one and
together take under ten minutes. One of them — **listing which modules are actually
installed on the running system** — should be done first, because *every* statement in
both research packages that says "this does not exist" is bounded by the source code
available here, and that qualifier cannot be removed any other way.

## 12. Thai accounting and statutory status

| Point | Status |
|---|---|
| Depreciation of production equipment must be absorbed into inventory | **Proven — standard text** |
| Fixed overhead allocated on **normal capacity** | **Proven — standard text** |
| Unallocated overhead expensed in the period | **Proven — standard text** |
| Planned maintenance is inside normal capacity | **Proven — standard text** |
| Per-unit charge reduced in unusually high production | **Proven — standard text** |
| Depreciation pro-rated from acquisition; class rates are ceilings | **Proven — statute** |
| Off-balance amounts have no line in the statutory statements | **Proven — regulator's prescribed forms** |
| Component depreciation required where significant | **Standard interpretation** — from the standard-setter's own manual, which states it is not part of the standard |
| Life and residual reviewed at least annually | **Standard interpretation**, same basis |
| The pro-ration unit is specifically the **day** | **Practice, not proven statute.** Held |
| Tax treatment of absorbed depreciation | **Not researched.** Held, non-blocking |

## 13. Asset → machine → resource group → operation → job

Buying a machine creates **two** records, by two people, from two documents. The
reference product joins them nowhere. This project added the only join that exists — a
manual, optional pointer on the financial record — and three of its four intended
behaviours never run.

Beyond that pointer, the chain is: many machines belong to one resource group; a
production step names the **resource group**; a job's time is recorded against the
**resource group**. **The machine appears nowhere after the pointer.** A resource group
holding three machines charges every job the same rate, whichever machine ran.

That is why the Boss's toll-gate concern is structurally correct, and why the first two
things to build are the repaired link and the machine dimension on the operation. They
are unglamorous and they are the entire foundation.

## 14. Depreciation → work in progress → finished goods

Of nineteen links from asset to cost of sales, **ten already exist and work.** The
absorption machinery — job cost, work in progress, finished goods valuation, the
accounting entry, cost of sales — is complete and reusable.

What is missing is the **front** of the chain — deriving the rate from depreciation, and
giving the operation a machine — and now, from the statutory evidence, the **control**
end: normal capacity, and the difference between what was absorbed and what should have
been. Neither exists anywhere in the reference product.

## 15. Post-depreciation internal usage

The mechanical premise holds and the isolation is now guaranteed by the platform itself.
The model is specified: it starts when the accounting life ends — **detected**, because
no "fully depreciated" status exists to observe — accrues at a dated rate, allocates
exactly like the costing model but into the management ledger only, and is corrected only
by dated entries.

Three holes are now filled with candidates rather than left open: what happens at
disposal, what happens if the asset becomes depreciable again, and how the ledger stays
balanced. **One remains genuinely open: the rate itself.** The candidate carried from the
last gate is based on the residual value, and on a one-baht residual it produces a rate
of essentially zero. A different basis is recommended. §9.

## 16. Productive versus non-productive

Attribute 100% by **classifying** the period's depreciation, not by **spreading** it:

> Productive absorbed = actual productive hours × (period depreciation ÷ normal capacity
> hours).
> Non-productive = everything left, decomposed by cause, charged to the period.

The identity closes by construction, every period, exactly. The causes are those the Boss
listed, plus the planned/unplanned split, and **"other" is a control, not a bucket** — a
non-zero balance there means evidence is missing and must be reported, not absorbed.

## 17. Allocation driver

The evidence settles one thing and deliberately leaves another open.

**Settled:** for depreciation and other fixed production cost, the only compliant driver
is machine hours **measured against normal capacity**. Work-centre averaging was
challenged at its strongest — including the strongest argument in its favour — and it
fails, because it cannot answer the question the business asked.

**Left open, correctly:** the driver for **variable** production cost. The standard
requires actual use there, and what a cost actually varies with differs by cost — power
with machine hours, packaging with quantity. This is where the per-context choice belongs.

## 18. Period close

Three closes, not one, in a fixed order: **operational** (hours and machines stop
changing), then **costing** (the rate is struck and the split computed), then
**accounting**. The costing rate cannot be struck while hours can still move.

Two rules follow from defects found: cost belongs to the period the **hours** happened
in, not the period the job finished in; and the accounting entry carries the **costing
period's** date, not the date someone pressed the button.

Once the accounting period closes, the statutory figures are frozen and corrections go to
the next open period. **The management ledger may be corrected retrospectively** — by
dated entry, never by silent restatement. That asymmetry is the practical benefit of
keeping the two ledgers genuinely separate.

## 19. Multi-company and SaaS

**This is the one area the independent audit failed outright**, and the failure is in the
current state, not in the research.

Machines, resource groups, bills of materials and production steps can all be created
**with no company at all** — and a record with no company is visible to, and usable by,
**every** company on the system. Separately, the asset visibility rule lets a user in a
subsidiary see the parent company's assets.

For a group of related companies this is a convenience. **For a SaaS where companies are
unrelated customers, it is a disclosure and a route for one customer's depreciation to
end up in another customer's product cost.**

Required: company mandatory and non-empty on every costing record; the asset-to-machine
link constrained to one company; strict asset visibility with no upward traversal; and
shared machines handled as an explicit, dated usage-rights arrangement with a real
intercompany charge — never by leaving the company blank.

And one principle that must not be compromised: **tenant is not a company.** Company
isolation is relative and permits legitimate crossings. Tenant isolation must be
absolute, and it belongs above the application, where a crossing query is not merely
refused but not expressible.

## 20. Correction and reversal

A posted entry is never edited: catch up, reverse the future, rebuild forward. This
discipline is already present on the depreciation side of the reference product and is
worth copying wholesale.

It is worth noting that **the same product does the opposite elsewhere** — cancelling a
job **deletes** its cost records rather than reversing them. Copying "the reference
product's approach" without saying which part is being copied would import the wrong one.

## 21. Audit trail

Every rate, every capacity figure and every machine assignment is a **dated record**,
never an editable field. Every allocation names the machine, the period, the cause, the
hours and the rate record it used. Cancellation reverses; it never deletes. No value is
stored that nothing reads. System-controlled accounts refuse manual journals. And a
reconciliation between the asset sub-ledger and the general ledger exists and is run —
which it does not, today, anywhere in the reference product.

## 22. Independent audit result

Thirteen areas reviewed. Six cleared, six held, **one failed** (multi-tenant safety),
and **one veto issued**:

> **No implementation of the costing model may begin before the normal-capacity decision
> is taken and before it is proved that only one mechanism carries machine depreciation
> into product cost.**

The second half of that veto deserves the Boss's attention. **Two mechanisms already
carry machine depreciation into product cost today**, and this design proposes a third.
Any two of them running together will double every product's machine cost — and because
each one reconciles perfectly against itself, **no report in the design would detect it.**
A design that double counts and reconciles is worse than one that visibly fails.

The audit also raised six findings against this research, of which the sharpest is that
the migration-target composite in §8 has now been reported twice and acted on zero times.

**The audit was performed by the same session that did the work. It is a structured
self-challenge, not an independent review. No human has reviewed this package.**

## 23. PMO recommendation

**APPROVE WITH CONDITIONS.**

PMO does **not** recommend a controlled design freeze at this gate. The normal-capacity
decision determines the central arithmetic of the whole costing model; freezing now would
freeze an ambiguity rather than resolve one.

Conditions: the two Boss decisions in §10, and the pilot-system query session in §11.

## 24. Design freeze readiness

**Not ready, and the reason is specific rather than general.** The domain is understood.
The architecture is coherent and traceable to evidence. What is not settled is one
arithmetic choice at the centre of it, and one data question that decides whether
per-machine costing is even sound on the current data.

Both are close. Neither needs more research.

## 25. Explicit Boss decisions still required

| # | Decision | Recommendation |
|---|---|---|
| 1 | **Normal capacity or actual hours as the allocation denominator?** | **Normal capacity.** The alternative breaches the standard and is undefined in an idle month |
| 2 | **Split maintenance into planned and unplanned?** | **Yes.** The data already exists; not splitting misstates stock and expense in opposite directions |
| 3 | Accept two allocation drivers — one for fixed cost, one for variable? | **Yes.** The standard requires different bases; a single driver cannot serve both |
| 4 | What rate should internal usage accrue at? | **Continue the last effective depreciation rate**, with the residual-based method as a fallback for migrated assets. The residual-based method alone fails on a one-baht residual |
| 5 | Is setup time productive? | **Yes** — it is caused by, and traceable to, a specific job |
| 6 | Are "idle" and "no demand" one cause or two? | **Two** — they mean different things to management, even though they are accounted for identically |
| 7 | Authorise the pilot-system query session? | **Yes** — read-only, under ten minutes, closes two blockers and caps every negative finding |

---

## 26. Governance record

| | |
|---|---|
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Branch | `research/asset-deep-continuation-2026-09-04-001` |
| Base | `origin/SMEsPlus` at `8d2c8aa` |
| Merged to `SMEsPlus` | **No** |
| Pull request opened | **No** |
| Production code written | **No** |
| Live system modified | **No** — and not read either |
| Architecture frozen | **No** |
| Boss approval claimed | **No** |
| Predecessor branches | Both intact on the remote and unmodified |
| Jira | See the session hand-off note accompanying this pack |

**Terminal state: READY FOR BOSS FINAL GATE.**

Boss options at this gate: **approve controlled design freeze · approve with conditions ·
return for targeted research · reject.**
