# 03 — P02 DELIVERY → INVENTORY OUTPUT → COGS FORENSIC TRACE

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`

## 0. The Question This File Answers

> **When does inventory leave, and when does cost of sales arise — and are they the same event?**

Answer, stated once and then evidenced:

> **They are not the same event, they are not owned by the same document, they are not driven by
> the same quantity, and they are not valued by the same rule.**

## 1. The Trace, Hop By Hop

```
 [H1] Order line                    quantity ordered
        |
 [H2] Outflow movement              quantity planned
        |
 [H3] Movement line + picked marker quantity actually handled   <-- OPERATIONAL TRUTH
        |
 [H4] Movement completion gate      quantity > 0 AND any line picked
        |
 [H5] Valuation layer               quantity × costing-method cost  <-- VALUATION TRUTH
        |
 [H6] Valuation journal entry       Dr outbound stock acct / Cr inventory   <-- FIRST GL EFFECT
        |
        |   ......... the chain BREAKS here. Nothing carries H5 forward. .........
        |
 [H7] Invoice line                  quantity billed                <-- BILLING TRUTH
        |
 [H8] Cost re-derivation            re-reads the layers from scratch
        |
 [H9] Cost journal lines            Dr expense / Cr outbound stock acct     <-- SECOND GL EFFECT
        |
 [H10] Best-effort matching of H6 and H9 in the outbound stock account
```

**`FACT VERIFIED` — P02-F-15 (STRUCTURAL, HEADLINE) — restated after independent challenge.** The
relation **exists on the model** — the valuation layer carries a link to an accounting document line
(`EV-P02-085`) — and **the cost generator does not populate it**. Across the whole reference root that
link is written in exactly **one** non-test place, and it is on the **purchase** side (`EV-P02-086`).

The accurate statement is therefore not "no reference exists" but **"the reference exists and the sales
side does not wire it"** — which matters, because §7 shows the same unwired link disables a control that
would otherwise protect the cost lines. Two findings collapse into one root cause and one fix.

With that correction the substance stands: there is **no populated reference from the cost journal line
back to the valuation layer that relieved the inventory**. The cost lines are keyed to the *invoice line*
that originated them (`EV-P02-050`), not to the outflow. H9 does not consume H5; it independently
re-computes a value from the same underlying layers (`EV-P02-021`). H5 and H9 are therefore two
independent valuations of the same physical event, reconciled afterwards by balance matching in a clearing
account rather than by identity.

This is the single most important structural finding in P02. Every double-COGS and
valuation-divergence case below is a consequence of it.

## 2. H4 — The Completion Gate (operational vs financial completion)

Three conditions must all hold for a completed outflow to be valued. `FACT VERIFIED` `EV-P02-022`:

1. the movement is not already completed,
2. its quantity is non-zero,
3. **at least one of its movement lines carries the picked marker.**

Condition 3 is a separate, stored, writable boolean (`EV-P02-038`, `EV-P02-051`).

**`FACT VERIFIED` — P02-F-16 (TOLERANCE-ZERO CANDIDATE) — reachability corrected after independent
challenge.** A movement can reach completed status with no picked line, in which case **no valuation
layer, no inventory relief and no journal entry exist**, with no exception, no queue and no report.

**The original statement did not say how that state is reached, and the answer both narrows and sharpens
the finding.** Validating a picking in which **nothing** is picked does *not* reach it: the validation
routine force-sets the picked marker on every movement when the picking has quantities and no picked
movement (`EV-P02-087`), and that set propagates to the movement lines (`EV-P02-088`).

**The reachable case is the MIXED picking.** The force-set is skipped as soon as **any** movement is
picked. Every *other* movement that has a quantity but no picked line then reaches completion and is
silently dropped from valuation. **That is one ordinary user action — part-picking a multi-line delivery —
not an exotic state.**

**`FACT VERIFIED` — P02-F-16b (THE FIELD A REVIEWER WOULD QUERY CONCEALS IT).** After completion the
**movement** reads as picked while its **lines** do not, because the movement-level marker is computed as
*completed or any line picked* (`EV-P02-089`) whereas the valuation gate reads the **line** marker and
runs before completion. A reconciliation query written against the movement-level field — the obvious one
— **will not return a single one of these.** The original claim that the hole is "undetectable because
there is nothing to query" was wrong in a way that **understated** it: it **is** queryable, on the
movement-line marker, and the natural field actively hides it.

**`DESIGN CANDIDATE` DC-03-01.** In SMEsPlus, physical completion and valuation must be one atomic
transaction. A completed outflow without a valuation record must be structurally unrepresentable,
not merely discouraged.

## 3. H5/H6 — What The Outflow Actually Posts

| Element | Value | Evidence |
|---|---|---|
| Debit | the configured **outbound stock account** (from the product category, or a location override) | `EV-P02-024` |
| Credit | the configured **inventory valuation account** | `EV-P02-024` |
| Amount | quantity × cost determined by the costing method | `EV-P02-032` |
| Gate | product must be storable **and** under real-time valuation | `EV-P02-023`, `EV-P02-052` |
| Exclusion | movements restricted to a third-party owner are skipped | `EV-P02-025` |

**`FACT VERIFIED` — P02-F-17.** The outflow entry **is not cost of sales**. It is an inventory
reclassification. Whether it ever becomes cost of sales depends on configuration that lives on two
other objects — see `01_P02_PROCESS_MAP.md` S5 and `02_P02_INVOICE_POLICY_MATRIX.md` §1.

**`FACT VERIFIED` — P02-F-18.** Non-storable products leave the business with **no cost effect at
all** in this process. Their cost was expensed on purchase. This is correct, but it means the
statement "P02 recognises cost of sales" is false for an entire product class, and any margin report
built on P02 alone will be wrong for it.

## 4. H8 — The Cost Re-derivation (the valuation-truth divergence)

This is the most defect-dense mechanism in P02. It has two entry points.

### 4.1 Entry point A — invoice line linked to an order line

The cost per unit is computed by walking the **order line's own outflow movements**, consuming
their valuation layers in creation order, skipping the quantity already covered by previously
posted cost lines, and taking the value of the layers consumed. `FACT VERIFIED` `EV-P02-021`,
`EV-P02-020`, `EV-P02-032`.

**The fallback:** when the billed quantity exceeds what the available layers can cover, the shortfall
is valued at **the product's current standard price** and added to the total.
`FACT VERIFIED` `EV-P02-019`.

The per-unit cost written to the journal is then `total valuation ÷ billed quantity` —
an average. `FACT VERIFIED` `EV-P02-020`.

**`FACT VERIFIED` — P02-F-19 (DOUBLE-VALUATION / PHANTOM-COST CLASS).** Under invoice-on-order, or
whenever billed quantity exceeds delivered quantity for any reason, cost of sales contains a
component priced at a **current master-data value** rather than at the cost of any inventory that
actually moved. That component:

- has no valuation layer behind it,
- has no inventory relief behind it,
- credits the outbound stock account with nothing to match it,
- and is **never subsequently corrected** when the goods are finally delivered, because the delivery
  will create its own layer and its own entry while the cost line has already been posted at a
  different value.

**`FACT VERIFIED` — P02-F-20 (AVERAGING DESTROYS PER-UNIT TRUTH).** Because the journal carries
`total ÷ quantity`, a line that mixes real layer costs with standard-price fallback, or that mixes
consigned (excluded) and owned stock, records a **per-unit cost that equals none of the real costs**.
The total is preserved; the unit cost in the ledger is a fiction. Any downstream unit-margin or
per-lot costing analysis reading that field is reading a derived average, not a cost.

### 4.2 Entry point B — invoice line with no order line behind it

The delivery-aware path is skipped entirely and the cost is the product's **standard price**,
full stop. `FACT VERIFIED` `EV-P02-021` (the delivery-aware branch is conditional on an order line
being present), `EV-P02-019` (the base behaviour it falls back to).

**`FACT VERIFIED` — P02-F-21.** A manually raised customer invoice for a storable product under
real-time valuation **creates cost of sales at standard price and credits the outbound stock
account**, with no delivery, no layer, and no inventory movement anywhere in the system.
This is a complete, self-contained phantom-COGS path requiring only the ability to raise an invoice.

## 5. H9 — Generation Of The Cost Journal Lines

| Property | Finding | Tag | Evidence |
|---|---|---|---|
| Trigger | the invoice **post** routine, before the posting decision is taken | `FACT VERIFIED` | `EV-P02-015` |
| Eligibility | product is storable **and** under real-time valuation | `FACT VERIFIED` | `EV-P02-018` |
| Quantity | the **invoice line** quantity | `FACT VERIFIED` | `EV-P02-016` |
| Accounts | debit = expense from the product's accounts (or the journal default); credit = the outbound stock account | `FACT VERIFIED` | `EV-P02-016` |
| Sign | inverted for credit notes | `FACT VERIFIED` | `EV-P02-016` |
| Skip | skipped when the computed amount or the unit price rounds to zero | `FACT VERIFIED` | `EV-P02-016` |
| **Expense account fallback** | when the product's accounts yield no expense account the debit goes to **the journal's default account** — and on a sale journal the chart sets that to the **income** account (`EV-P02-090`, `EV-P02-091`). Cost of sales is then debited to Income, netting revenue against itself on the same document, with no error. | `FACT VERIFIED` | `EV-P02-090` |
| Idempotency | **absent as a guard** — `FACT VERIFIED`. **Exploitability is `UNRESOLVED — EVIDENCE REQUIRED`** and the two halves must not be collapsed into one tag. See §6. | split — see §6 | `EV-P02-016`, `EV-P02-028` |
| Reversibility | reset-to-draft and cancel both **delete** the cost lines | `FACT VERIFIED` | `EV-P02-017` |
| Copying | cost lines are stripped when a document is duplicated | `FACT VERIFIED` | `EV-P02-053` |

**`FACT VERIFIED` — P02-F-22 (ELIGIBILITY MISMATCH) — one of its two instances refuted after
independent challenge.** The eligibility test for creating a cost line is *storable + real-time
valuation*. The test for creating a valuation entry at outflow is *storable + real-time valuation*
**and additionally** not owner-restricted and with a picked line. The invoice-side test is **strictly
weaker**, and that remains true.

The package originally claimed **two** confirmed phantom-cost paths follow from it. Only one does.

### 5a. Owner-restricted stock — claim refuted for the order-linked path

**`CONTRADICTED`.** The cost re-derivation **subtracts owner-excluded quantity from the shortfall before
the standard-price top-up** (`EV-P02-020`). For a wholly owner-restricted delivery on an order-linked
invoice: nothing is valued, the shortfall reduces to zero, no top-up occurs, the computed unit cost is
zero, and the generator's own zero-skip then **creates nothing** (`EV-P02-016`). **No phantom cost line is
produced.**

The path survives **only** on entry point B — an invoice line with no order line behind it — where the
delivery-aware branch is never entered and the base behaviour returns standard price unconditionally
(`EV-P02-021`, `EV-P02-019`). That is already recorded as P02-F-21 and is not a second, independent
finding.

**Corrected count: P02-F-22 has ONE confirmed instance — the unpicked-completion case — not two.**

## 6. The Idempotency Question — DOUBLE COGS ATTACK

**`FACT VERIFIED`.** The cost generator iterates the document's **product** lines and creates a new
pair of cost lines for each eligible one. The set it iterates is defined by a filter that
**excludes cost lines** (`EV-P02-028`), so previously generated cost lines are invisible to it.
There is no key, no constraint and no lookup preventing a second generation. The technical link
field that records which invoice line a cost line came from is written but **never read for
duplicate prevention** — its only reader is the cost re-derivation, which uses it to *exclude
already-posted quantities*, not to block regeneration. `EV-P02-050`, `EV-P02-021`.

**What actually prevents duplication today — corrected after independent challenge.** The package
originally located the protection in transaction behaviour. The real primary protection is simpler and
stronger: **the interactive path never uses soft mode.** The manual post action calls the routine in
**hard** mode (`EV-P02-029`), and in hard mode nothing is deferred, so no document reaches the deferred
state with cost lines attached along that path. The auto-post job likewise defers nothing, because its own
search is bounded to dates at or before today (`EV-P02-030`). Documents that do post are then protected by
the state check that refuses to post an already-posted document (`EV-P02-054`).

**A partial control does exist, and it is not this one.** The origin field **is** read — to net
already-posted cost quantity out of the re-derivation (`EV-P02-050`). That is duplicate control **at the
value level, within one document's computation**. It does **not** prevent a second pair of lines from
being created. The distinction matters: a second pair generated after the netting has already run would be
valued at zero rather than doubling the cost — so the exposure, if reachable, is more likely to be
**duplicate lines** than **duplicate value**. Establishing which is part of the C-04 test.

**The residual exposure, narrowed.** `SUPPORTED INTERPRETATION` — P02-F-23. Soft mode defers future-dated
documents and leaves them in draft (`EV-P02-031`), and the cost generator has already run by that point
(`EV-P02-015`). A document that traverses this path retains a pair of cost lines while remaining in draft;
a later post creates a second pair, and the state check does not fire because the document is still draft.
The generator's exclusion filter guarantees it will not notice the existing pair.

**The precondition is narrower than originally implied:** it requires a **future-dated sale document
posted through a soft-mode caller**. Enumerating soft-mode callers in the sales domain finds them **only
in the subscription module**, which is outside this package's declared path set. So the exposure is real in
mechanism and **unestablished in reachability**, and it stays `UNRESOLVED — EVIDENCE REQUIRED`.

**Evidence required to close this** (`UNRESOLVED — EVIDENCE REQUIRED`, tracked as C-04 in
`12_P02_CONTRADICTION_REGISTER.md`): a runtime reproduction on a database, posting a future-dated
customer invoice for a storable, real-time-valued product through a soft-post caller, then posting
it again and counting the cost lines. This session had **no database access** and could not execute
it. The claim is therefore **not** advanced to `FACT VERIFIED`.

Regardless of that outcome:

**`DESIGN CANDIDATE` DC-03-02 (mandatory).** In SMEsPlus, cost-of-sales generation must be
**idempotent by construction** — a uniqueness constraint on (accounting document line, cost effect)
— not by relying on the ordering of a posting routine.

## 7. Reset-To-Draft: The Cost/Revenue Asymmetry

**`FACT VERIFIED` — P02-F-24b (THE CONTROL EXISTS AND IS NOT WIRED FOR SALES).** Raised by the independent
challenge, verified by the primary session. The reference **does** carry a guard that hides the
reset-to-draft action entirely when a document's lines carry valuation layers (`EV-P02-092`). It would
prevent exactly the destruction described below.

It never fires on a customer invoice, because the link it tests is written in **one** non-test place in the
whole reference root, and that place is on the **purchase** side (`EV-P02-086`). A customer invoice's cost
lines never populate it, so the action stays available and the cost half of the entry stays destructible
while the revenue half does not.

**This is the same unwired link as P02-F-15.** One root cause — the sales-side cost generator does not
record which valuation layer it consumed — produces both the missing traceability and the inoperative
guard. It also makes the fix cheap: **the control is already built.**

**`FACT VERIFIED` — P02-F-24.** Resetting a posted customer invoice to draft **deletes** its cost
lines (`EV-P02-017`). The revenue and receivable lines survive the round trip as ordinary document
lines and are simply re-derived on the next post. The two halves of the same accounting event
therefore have **different durability**:

| Half | On reset-to-draft | On re-post |
|---|---|---|
| Revenue / receivable / tax | retained as document content | re-derived from the same content → same result |
| Cost of sales | **destroyed** | re-derived from the layer state **as it is now** → may differ |

If inventory has moved between the two posts — a later receipt at a different price, a FIFO vacuum
run, a revaluation — the re-posted cost is a **different number** for the same shipment, with no
record that it changed. `SUPPORTED INTERPRETATION` for the divergence; `FACT VERIFIED` for each
mechanism (`EV-P02-017`, `EV-P02-020`, `EV-P02-055`).

## 8. H10 — Matching In The Outbound Stock Account

After posting, the system attempts to match the invoice's outbound-stock-account line against the
delivery's, per product. `FACT VERIFIED` `EV-P02-041`. It is skipped when:

- the account is not flagged reconcilable, or
- the product is not under real-time valuation, or
- no completed customer-direction movement is linked to the invoice's order lines.

**`FACT VERIFIED` — P02-F-25.** Matching is a **cleanup**, not a control. It cannot fail loudly; it
simply does not happen. The invariant "everything delivered is either invoiced or visible as an
unbilled position" is therefore not enforced anywhere — it is only *usually* achieved.

## 9. Summary Table — Answers To The Directive's Explicit Questions

| Question | Answer | Tag |
|---|---|---|
| **When does inventory leave?** | At outflow completion, provided the quantity is non-zero and at least one movement line is marked picked. | `FACT VERIFIED` |
| **When does COGS arise?** | Configuration-dependent: at invoice post (split recognition on), at outflow (split recognition off *and* the outbound account is an expense account), or **never** (split recognition off and the outbound account is an interim asset — the Thai chart default). | `FACT VERIFIED` |
| **Who owns the COGS event?** | The **invoice**, in the split-recognition configuration. Not the outflow. | `FACT VERIFIED` |
| **What quantity drives COGS?** | The **invoice line** quantity. | `FACT VERIFIED` |
| **What value drives COGS?** | A re-derivation over the order line's layers, topped up at **current standard price** when the layers are insufficient, then averaged over the billed quantity. | `FACT VERIFIED` |
| **Is COGS equal to the inventory relieved?** | Only when billed quantity equals delivered quantity, the delivery was valued, and no reset-to-draft occurred in between. | `SUPPORTED INTERPRETATION` |

## 10. Negative Claims

| Claim | Classification | Search boundary |
|---|---|---|
| No link exists from a cost journal line to the valuation layer that relieved the inventory | `NOT FOUND IN SEARCHED SCOPE` | Searched the inventory-accounting and sales-inventory-accounting layers for the cost-line origin field and every field written by the cost generator. The only origin recorded is the invoice line. Localisation and enterprise reporting layers were **not** searched. |
| No idempotency guard exists on cost-of-sales generation | `NOT FOUND IN SEARCHED SCOPE` | Searched every reader of the cost-line origin field across the whole reference addon root (4 occurrences, complete). No occurrence performs a duplicate check. |
| No exception report exists for completed outflows without valuation | `NOT YET SEARCHED` | Reporting layers were out of scope for this track. Must be searched before the claim is used. |
