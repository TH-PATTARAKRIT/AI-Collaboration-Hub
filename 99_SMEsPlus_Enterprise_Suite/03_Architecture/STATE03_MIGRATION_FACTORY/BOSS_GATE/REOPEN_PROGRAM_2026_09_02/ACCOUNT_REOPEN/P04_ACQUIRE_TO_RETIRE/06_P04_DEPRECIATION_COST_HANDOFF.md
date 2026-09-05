# 06 — P04 DEPRECIATION AND COST HANDOFF

Layer: **2 — audit quarantine**.

How depreciation leaves P04 and reaches product cost. This is the file that
carries the **AAS+ veto's second limb** — the requirement to prove that exactly
**one** mechanism carries machine depreciation into product cost.

---

## 1. What the prior packages established, imported unchanged

| Imported | Source |
|----------|--------|
| TAS 2 ¶12 **requires** production-equipment depreciation to enter inventory conversion cost — absorption is not merely permitted | P3, standard text |
| TAS 2 ¶13 constrains the method: normal-capacity basis; the per-unit fixed charge **may not rise** when output falls; unallocated overhead is a **period expense**; planned maintenance sits **inside** normal capacity; the per-unit charge is **reduced** in abnormally high production | P3, standard text |
| Variable production overhead is allocated on **actual use** | P3, TAS 2 ¶13 |
| The reference product has **no normal-capacity mechanism anywhere** | P3 |
| `BD-02` is ambiguous between a normal-capacity reading and an actual-hours reading; the actual-hours reading is **REJECTED — INVALID ASSUMPTION** | P3 |
| The AAS+ **veto on implementation start** stands until `BLK-07` is decided **and** the single-mechanism condition is proved | P3, **not discharged** |
| Two live mechanisms were counted, and a third proposed | P3 |

## 2. The count of live mechanisms is larger than previously recorded

### 2.1 Declared enumeration

| Element | Declaration |
|---------|-------------|
| POPULATION | Every code path in the reference build by which a work-centre, machine or overhead cost acquires a monetary value and reaches either the general ledger or the analytic ledger in connection with a manufacturing order |
| PATTERN | Rate-field and cost-computation sweep: the hourly-cost fields, the cost-calculation methods, the labour-posting method, the work-in-progress wizard, the standard-cost-from-bill-of-materials path, and the analytic-entry creation helpers; each followed to its offsetting entry |
| PATH SET | The manufacturing, manufacturing-accounting, work-order, work-order-human-resources, project-manufacturing and inventory-accounting modules of the reference build |
| UNIT | One distinct monetisation path, defined by its own rate field **or** its own driver quantity **or** its own destination ledger |

### 2.2 Result — nine paths

| # | Path | Rate | Driver | Destination |
|---|------|------|--------|-------------|
| **M1** | Machine rate into finished-goods value | work-centre hourly cost | **actual** duration | **GL** — finished-move valuation, credited to the production account |
| **M2** | Labour relief entry | same | same | **GL** — a standalone entry, Dr production account / Cr the work centre's expense account |
| **M3** | Employee rate | employee hourly cost | logged productivity duration | **GL**, folded into M1 and M2 |
| **M4** | Work-centre analytic | work-centre hourly cost **only** | work-order duration | **ANALYTIC ONLY** — one-sided |
| **M5** | Order/project analytic | **the identical value as M4** | same | **ANALYTIC ONLY** — a second distribution of the same amount |
| **M6** | Employee analytic | employee cost | productivity duration | **ANALYTIC ONLY** |
| **M7** | Extra unit cost | a free-text float on the order | quantity | **GL** — capitalized into finished-goods value, **with no relief entry** |
| **M8** | Work-in-progress wizard | date-bounded cost calculation | date-bounded | **GL** — Dr work-in-progress, Cr valuation and an overhead account; auto-reversed the next day |
| **M9** | Standard cost from the bill of materials | work-centre hourly cost **+** employee cost × a ratio | **planned** duration, not actual | **GL**, baked into standard price |

> **P04-F-42.** The same work-centre hour is monetised by **several independent
> paths** — analytic-only and general-ledger. Under the unit declared in §2.1 the
> count is **7**; under a per-posting-artefact unit it is **9**; under the
> strictest per-computation unit it is **6**. See §2.3, which was corrected after
> independent challenge showed the headline figure of 9 was not reproducible from
> the declared unit.
> The prior count of "two live mechanisms, and a third proposed" is **understated
> under every one of the three units**.
> Class: **FACT VERIFIED** as to the paths; the **count is unit-dependent and the
> unit is declared**. Severity: this **materially widens the AAS+ veto's second
> limb**, it does not satisfy it.

### 2.3 The unit caveat — stated because the comparison invites a false one

Adopted from `15` Level 4, expert E3.

**Corrected after independent challenge. Executed strictly, the unit declared
in §2.1 yields SEVEN, not nine.**

The declared unit is disjunctive — own rate field, **or** own driver quantity,
**or** own destination ledger. Applied literally:

- **M1 and M2 collapse into one.** They share the rate, the driver, and the
  destination ledger (both produce general-ledger entries).
- **M4 and M5 collapse into one.** Both consume the *identical* computed value
  and both write to the analytic ledger.

**The honest count under the declared unit is 7.** The figure 9 is only reachable
under a **different** unit — *own posting artefact*, which separates a valuation
write from a standalone relief entry, and separates two distributions of one
value into two sets of analytic lines. Reaching 9 by re-reading "destination
ledger" as "destination entry" would be **changing the unit after the count**,
which `00` §4 forbids. It is corrected here rather than defended.

| Unit | Count |
|------|-------|
| Own rate field **or** own driver **or** own destination **ledger** — as declared in §2.1 | **7** |
| Own posting artefact — a stricter separation of what actually lands | **9** |
| Own monetary **computation** — the strictest reading | **6** (M5 and M3 fold in) |

**Neither figure is comparable to the prior count of two, because the prior count
declared no unit at all.** A reader setting any of these against "two" is
comparing different measurements, not observing a discovery.

The paths are not equally distinct, and the package says so:

| Path | Distinct by | Strength |
|------|-------------|----------|
| M1, M2 | destination (valuation vs a standalone relief entry) | strong — they are separate entries |
| M7, M8, M9 | own driver **and** own destination | strong |
| M3, M6 | own rate field **and** own driver | strong as inputs; their **destination** is shared with M1/M2 and M4 |
| M4 | own destination ledger (analytic, one-sided) | strong |
| **M5** | a **second distribution of the same value** to different analytic accounts | **weakest** — a second call, not a second computation. It satisfies **none** of the three declared disjuncts and is the reason the strict count is 7 |

What does **not** change under any unit, and is the point of the enumeration:

- the same work-centre hour is monetised **more than twice**;
- at least two of the paths **do not reconcile with each other** (P04-F-43,
  P04-F-44) and one produces a **live ledger mismatch**;
- the veto's single-mechanism proof must therefore be discharged against a
  **declared** enumeration, not against a count carried forward by assertion —
  and the enumeration must state its unit, which is why this section exists.

## 3. Six ways the paths fail to reconcile

| ID | Failure | Class |
|----|---------|-------|
| **P04-F-43** | **M1 and M2 reconcile to each other; M7 does not.** The finished move credits the production account with components + work-centre cost + extra cost, while the relief entry debits only the work-centre cost. The extra cost is left as a **permanent credit residual** on the production account. The product-category field's own help text describes a residual that the relief entry actually clears, and does not mention the one that genuinely remains | FACT VERIFIED |
| **P04-F-44** | **Under standard costing the general ledger genuinely mismatches.** The finished-move price is written **only** for first-in-first-out and average cost methods. Under standard cost the finished move credits the production account with the **standard** overhead computed on **planned** duration (M9), while the relief entry — which has **no cost-method guard at all** — debits the **actual** overhead (M2). The difference is stranded on the production account with **no variance account and no report line pointing at it** | FACT VERIFIED, **High** |
| **P04-F-45** | **M4 and M5 post the identical amount twice into the analytic ledger.** The project bridge re-distributes the very value the work-centre path has already distributed, under a different distribution. Where the two distributions resolve to the same analytic account — an ordinary single-plan configuration — the analytic ledger **carries the work-centre cost twice**. No guard, no collision check | FACT VERIFIED (mechanism); **incidence is a data question** |
| **P04-F-46** | **M4 diverges numerically from M1 and M2.** M4 uses the work-centre rate alone; M1 and M2 use a calculation that includes employee cost. Whenever an employee rate is non-zero, the analytic ledger and the general ledger **disagree on the value of the same work order** | FACT VERIFIED |
| **P04-F-47** | **The labour relief entry has no idempotence marker.** It writes an entry reference onto the productivity record but never reads it back as a guard. Whether a second entry into that path is reachable is **UNRESOLVED** — it requires runtime tracing | Mechanism FACT VERIFIED; reachability UNRESOLVED |
| **P04-F-48** | **The relief entry credits an expense account.** If the underlying payroll or utility expense was not independently booked there, that account carries a **permanent credit balance** | FACT VERIFIED |

## 4. The finding that inverts a prior premise

The AAS+ veto rests partly on the statement that *"depreciation already reaches
production cost centres through the analytic distribution"* — one of the two
live mechanisms counted. This session traced that path.

**Both** lines of a depreciation entry carry the asset's analytic distribution,
and the analytic-line creation runs with **no filter on account type**. The
accumulated-depreciation line is a credit; the expense line is a debit. The
analytic amounts are computed from the signed balance and are therefore mirror
images.

> **`P04-F-49` is LATENT in the only same-generation deployment** — see `01` §6A.8 / `P04-F-99`: the analytic dimension is installed with one plan and **zero analytic accounts**, and **0 of 40,353** move lines carry a distribution, so the cancellation has never occurred there. The source finding below is unchanged; its effect is conditional on a first analytic account existing. What is live is that **no attribution exists at all**.
>
> **P04-F-49.** **They cancel — in net balance, not in existence.** Stated
> precisely, after independent challenge sharpened it:
>
> **Two analytic lines are created**, one per entry line, each carrying its own
> general-ledger account and the same distribution. Their amounts are exact
> mirrors, so **the net analytic balance of a depreciation entry is zero**.
>
> The difference matters, and it decides what `BD-02` needs:
> - An analytic report that **groups or filters by general-ledger account**, or
>   that excludes balance-sheet accounts, **shows the full depreciation charge on
>   the cost centre.** The attribution exists at line level.
> - Any report that **sums the cost centre** — which is what a cost centre is
>   for — **shows zero**.
>
> So the prior premise that *"depreciation already reaches production cost
> centres through the analytic distribution"* is **true at line level and false
> at balance level**. It is not a mechanism that can carry cost into product cost,
> because the amount that would be carried nets to nothing; but the data is
> present and a **report change** — not new behaviour — recovers it.
> Class: **FACT VERIFIED.** Carried to `12` as `P04-CTR-02`.

And the complementary case is worse:

> **P04-F-50.** When an asset carries **no** analytic distribution, the
> distribution key is omitted, so each line computes its own distribution from
> the distribution-model rules keyed on **its own account code**. The
> accumulated-depreciation account and the depreciation-expense account have
> different codes, so the two lines can receive **different** distributions —
> producing a **non-zero, unbalanced analytic residue with no economic meaning**.
> Class: **FACT VERIFIED.** Severity **High**.

> **P04-F-64.** **The same construction applies to the disposal entry.** Every
> line of the disposal entry — asset cost, accumulated depreciation, the
> neutralised income line **and the gain or loss line** — carries the asset's
> distribution, and the entry is balanced. So **the gain or loss on disposal also
> nets to zero in the analytic ledger**, by identical construction. A second
> `BD-02` breach, and one this session did not see until independent challenge
> pointed at it.
> Class: **FACT VERIFIED.**

### 4.1 What this does to the veto

It does not lift it. It **changes its shape**, and makes it harder:

- the count of paths is **nine**, not three;
- one of the two paths the veto named as live is **not live in the way stated** —
  it nets to zero when configured, and produces meaningless residue when not;
- a **new** genuine general-ledger mismatch was found (P04-F-44) which is
  independent of the depreciation question and which no prior package recorded;
- the single-mechanism proof the veto requires must now be discharged against a
  population of nine, established by a declared enumeration — not against a
  count of two carried forward by assertion.

> **P04-F-51.** The AAS+ veto's second limb is **further from discharge after
> this session than before it**. That is the correct outcome of an honest
> enumeration and is stated plainly rather than presented as progress.

## 5. Mandatory analytic plans do not apply to any asset path

*Latency, added at `P04-F-99`: with one plan and **zero** analytic accounts in the only v18 deployment, a mandatory plan could not bind there in any case. The source finding stands; the consequence is dormant.*

Analytic-plan applicability — optional, mandatory, unavailable — is enforced
**only when a validation flag is present in the execution context**. That flag
is set **only from user-interface posting actions**.

> **P04-F-52.** **No programmatic posting carries the flag.** Depreciation
> entries, disposal entries, inventory valuation entries, the labour relief
> entry, deferred-recognition entries, and the automatic asset confirmation all
> **bypass mandatory-plan validation entirely**. A second, independent block
> applies as well: validation is restricted to product-type lines, and
> depreciation entries have none.
> Class: **FACT VERIFIED.** Severity **High** for `BD-02`.

Consequence for the 100 %-attribution requirement: **the estate cannot enforce
that a depreciation charge is attributed at all**, by any configuration. A
mandatory analytic plan — the obvious control — does not fire on the entries
that matter.

## 6. Distribution ownership and drift

| Behaviour | Consequence |
|-----------|-------------|
| The asset's distribution is written from the source bill line at creation — then **overwritten by the asset model's distribution** if the account has a model attached | The model wins over the transaction. On the live population **no asset carries a model**, so the bill line's distribution stands |
| The asset **never consults** the account-prefix distribution rules that govern every manual journal item | A distribution rule that an accountant believes is universal is **invisible to assets** |
| Changing the asset's distribution rewrites it **only on draft entries** | The asset and its **posted history permanently disagree** |
| The gross-increase entry and the child asset it creates carry **no distribution at all** | **Every subsequent depreciation of a capitalized addition is un-analytic** |

> **P04-F-53.** Capitalizing an addition to an asset **silently drops that
> addition out of analytic attribution**, at the exact point where the addition
> begins depreciating. Under `BD-02` this is a breach of the 100 %-attribution
> requirement produced by the reference behaviour itself.
> Class: **FACT VERIFIED.** Severity **High**.

## 7. New statutory evidence bearing on `BLK-07`

From `07_P04_DISPOSAL_DERECOGNITION_MATRIX.md` §4.3, obtained this session:

> **TAS 16 governs the size of the depreciation charge. TAS 2 governs its
> absorption into inventory. They are different questions.**

Under TAS 16 the **units-of-production** method expressly contemplates a period
charge of **zero when there is no production**. Under TAS 2 ¶13 the per-unit
fixed charge **may not rise** when output falls, and unallocated overhead is a
period expense.

This dissolves the apparent symmetry that made the two readings of `BD-02` look
equally defensible:

| Reading | What it actually does | Verdict |
|---------|----------------------|---------|
| *Period depreciation ÷ actual productive hours* | Holds the **charge** fixed and varies the **per-unit absorption** upward as output falls | **Breaches TAS 2 ¶13.** Already rejected by P3; this session adds that it is not rescued by TAS 16 either, because TAS 16 permits varying the **charge**, not the absorption rate |
| *Period depreciation ÷ normal capacity hours*, remainder to period expense | Holds the **absorption rate** fixed and lets the unabsorbed remainder fall to expense | **Satisfies both standards** |
| *Units-of-production charge, absorbed at normal capacity* | Varies the **charge** under TAS 16 **and** absorbs at normal capacity under TAS 2 | **Also satisfies both** — and is a **third option not previously on the table** |

> **P04-F-54.** A **third compliant option** exists for `BLK-07` that no prior
> package considered: adopt units-of-production as the **TAS 16 depreciation
> method** and normal capacity as the **TAS 2 absorption denominator**. It
> satisfies both standards, it makes an idle month's charge genuinely zero
> rather than merely unabsorbed, and it aligns the depreciation charge with the
> Boss's operational instinct about machine usage.
> Class: **DESIGN CANDIDATE**, resting on **FACT VERIFIED** statutory readings.
> It is offered to the Boss as a third option at `BLK-07`, **not** as a
> recommendation that displaces P3's.

Two consequences that must be stated with it, so it is not adopted casually:

1. Units-of-production requires a **reliable expected-total-output estimate per
   asset**, reviewed annually. Nothing in the estate holds one.
2. It **changes the depreciation charge itself**, which has tax consequences
   (`HOLD-02`, `HOLD-05`) that this session did not research.

Registered as blocker **P04-B-27**.

## 8. Handoff position

| Question | Position |
|----------|----------|
| Does depreciation reach product cost today? | **Through the general ledger, no** — no route feeds a machine's depreciation into the work-centre rate. **Through the analytic ledger, no** — it nets to zero (P04-F-49) |
| How many mechanisms would have to be proved off? | **Seven** under the declared unit, **nine** counting each posting artefact separately — enumerated in §2, with the unit question settled in §2.3 |
| Is the veto dischargeable by this session? | **No.** Both limbs remain open, and the second is wider |
| What is new for the Boss? | A **third compliant option** at `BLK-07` (§7); a **real general-ledger mismatch** under standard costing (P04-F-44); the **analytic cancellation** (P04-F-49); the **un-analytic capitalized addition** (P04-F-53); and the fact that **mandatory plans cannot enforce attribution** (P04-F-52) |
