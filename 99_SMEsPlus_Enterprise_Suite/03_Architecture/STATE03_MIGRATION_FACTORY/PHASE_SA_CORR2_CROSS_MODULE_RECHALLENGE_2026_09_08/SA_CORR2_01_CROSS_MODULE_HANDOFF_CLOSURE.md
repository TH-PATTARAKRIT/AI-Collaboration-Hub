# SA_CORR2_01 — CROSS-MODULE HANDOFF CLOSURE
## CP-SA-C2-10 — CROSS-MODULE HANDOFFS RECONCILED

Session: `[SMEPLUS-26-09-08-PHASE-SA-CORR2-XMOD-001]`
Branch: `architecture/account-phase-sa-corr2-cross-module-rechallenge-2026-09-08-001`
Evidence frame: `SA_CORR2_00` §2 (183 branches · U1 2,748 blobs · U2 2,606 paths · controls fire)

---

## 1. The rule this register enforces

Master prompt §3:

> No handoff is complete merely because both modules have separate evidence packs.
> The producer output and consumer input must be proven **semantically compatible**.

The parent package proved this at the level of *interface shape*. This register tests it at the
level of **meaning**, and the first two tests below show why that distinction is not academic:
in both cases both modules had evidence, and in both cases nobody had read the other's.

---

## 2. The defect class this round closes

`SA14-F-01` established that five of six registered contradictions are **boundary defects**, not
domain defects. `SA_CORR2_00` adds the reason they survive a correction round:

> **Every party searches its own directory.** The parent package searched the Account programme's
> path set and concluded the input was absent. CORR1 corrected that by searching Group A's path
> set — and concluded a *second* item was undetermined that the Account path set answers. The
> instrument changed; the habit did not.

The corrective discipline applied throughout this register: **for every cross-module question,
search BOTH parties' path sets in BOTH parties' vocabularies, and say which path set each answer
came from.**

---

## 3. `XD-01` — the sell-side cancellation gate, decomposed question by question

CORR1 restated `SA00-F-03` and concluded *"the answers largely exist"*, reframing Boss Decision 1
to *deliver the existing semantics and decide the one residual question*.

**That reframing is itself re-framed here.** The three questions were tested one at a time. They
do not have one answer between them; they have three different statuses, and two of the three are
not answerable by any amount of research.

### 3.1 Instrument

| Clause | Declaration |
|---|---|
| POPULATION | `SA_CORR2_00` §2 corpus, 183 branches |
| PATH SET | both parties: `.../GROUP_A_SALES_INVENTORY_PURCHASE/**` (all five branches) **and** `.../ACCOUNT_REOPEN/**` |
| PATTERN | per question, declared in each row below and executed |
| UNIT | unique path (U2) for counts; verbatim quotation for content |
| POSITIVE CONTROL | `BD-ACC-01` → 34 blobs, join → 34 paths. Fires |
| CROSS-CHECK | `\bcancel` under `P02_ORDER_TO_CASH` returns **23** unique paths under four different units (paths 23 / blobs 23 / branch-path pairs 23 / any path named P02 23). Reproducible |

### 3.2 Question 1 — *which Customer Invoice / AR lifecycle state should be treated as equivalent in blocking weight to Purchase's "open vendor bill" gate, if any?*

**Status: `NOT ANSWERED — AND NOT ANSWERABLE BY RESEARCH`.**

The Account programme establishes, `FACT VERIFIED`, what the reference estate **does**:

> `| Object | Can it be cancelled after taking effect? | What is destroyed |`
> `| Order | yes — status only | nothing financial |`
> — `ACCOUNT_PROCESS_DEEP_RESEARCH/P02_ORDER_TO_CASH/11_P02_EDGE_CASE_MATRIX.md` §4

So the reference estate answers the question with **"none"** — no invoice state blocks a sales-order
cancellation. That is a *measured fact about the reference*, and under the Clean Room / Nature DNA
constitution **a reference behaviour is learning, never a determination**. Inheriting "none" by
default is source-copying by omission — the exact defect `SA12-F-01` names.

The word in Group A's question is **"should"**. Nothing in any evidence pack can answer a *should*.

### 3.3 Question 2 — *does a posted Customer Invoice constitute a financial exposure that should block cancellation, symmetric to a posted vendor bill?*

**Status: `NOT ANSWERED — DECISION`. But the facts needed to decide it are now assembled.**

The exposure is no longer a matter of judgement about magnitude. It is enumerated:

> `| BE-14 | **Customer invoice posted** | accounting document (posted) | **YES — revenue, receivable,`
> `tax, and cost of sales** | document number + optional integrity hash | name/date locked only under`
> `hash or lock date | FACT VERIFIED EV-P02-015 |`
> — `.../P02_ORDER_TO_CASH/05_P02_BUSINESS_EVENT_REGISTER.md`

A posted customer invoice creates **four** simultaneous exposures — revenue, receivable, tax and
cost of sales. A posted vendor bill, whose gate Group A wants symmetry with, creates payable and
expense. **The sell-side exposure is the larger of the two**, and it includes a *statutory* element
(tax) that the buy side's gate was never protecting.

**This is new information for the decision and it did not exist in either party's register.** It is
produced here by reading the two parties' evidence against each other, which is what the joint
cross-proof was constituted to do and never did.

### 3.4 Question 3 — *what do "posted", "locked", "reconciled", "reversed" mean precisely for a Customer Invoice in Accounting's own model?*

**Status: `ANSWERED — by existing evidence, at `FACT VERIFIED`.** This is the one CORR1 was right about.

| Term | Established meaning | Evidence |
|---|---|---|
| **draft** | Consumes billable quantity but posts nothing. **A draft already reduces what the sell side believes it may still bill.** | `BE-13`, `FACT VERIFIED` `EV-P02-005` |
| **posted** | Revenue, receivable, tax and cost of sales all arise. Carries a document number and an *optional* integrity hash | `BE-14`, `FACT VERIFIED` `EV-P02-015` |
| **locked** | **Not a state of the invoice.** Name and date are immutable **only** under a hash or a lock date — two independent, optional mechanisms. Absent both, a posted invoice's accounting date is *"silently movable past a lock"* | `BE-14`; `06_P02_ACCOUNTING_EVENT_REGISTER.md`, `FACT VERIFIED` `EV-P02-013` |
| **reset to draft** | Reversible. **Cost lines are destroyed; revenue lines are retained as content.** Renumberable when unhashed | `BE-15`, `FACT VERIFIED` `EV-P02-017` |
| **cancelled** | Cost lines destroyed | `BE-16`, `FACT VERIFIED` `EV-P02-017` |
| **reversed** | A credit note posts and reverses revenue, receivable, tax **and** cost | `BE-18`, `FACT VERIFIED` |
| **reconciled** | Matching, not an entry. And **matching rows are freely destructible, across a closed period** | `AE-04`; `11_P02_EDGE_CASE_MATRIX.md` §4, `FACT VERIFIED` T2 §2, §7 |

### 3.5 `C2-F-01` — the answer to Question 3 makes Question 2 *harder*, not easier

The Account programme's own conclusion on this material is:

> **`FACT VERIFIED` — P02-F-47.** The durability ordering is inverted relative to accounting
> importance: **the physical event is immutable, the accounting event is reversible, and the
> settlement history is freely destructible.**
> — `.../P02_ORDER_TO_CASH/11_P02_EDGE_CASE_MATRIX.md` §4

Group A asked which invoice state should carry **blocking weight**. The evidence answers that in
the reference estate **no invoice state is durable enough to carry weight at all**: posted is
reversible, locked is optional, reconciled is destructible across a closed period.

> **A gate can only be built on a fact that cannot be quietly undone. Question 2 is therefore not
> "which state blocks" but "which state SMEsPlus will make durable enough to block with".**

That is a design determination with a stated consequence, and it is the form in which Boss should
receive Decision 1. It is materially different from CORR1's framing (*deliver the semantics, decide
the residual*) and materially different from the parent package's framing (*the input is absent*).

### 3.6 Disposition of `XD-01`

| Question | Status | Owner | Action |
|---|---|---|---|
| Q1 which state *should* block | `NOT ANSWERED — NORMATIVE` | **Boss** | Decide, informed by §3.3 and §3.5 |
| Q2 does a posted invoice constitute blocking exposure | `NOT ANSWERED — DECISION`, facts now assembled | **Boss** | Decide |
| Q3 what the states mean | **`ANSWERED`** | Accounting → Group A | **Deliver** `BE-13`…`BE-18` + `AE-04` into Group A's register. No research required |
| The durability precondition (`C2-F-01`) | **`RAISED BY CORR2`** | **Boss** | Must be decided *with* Q1/Q2 — deciding a gate without deciding durability produces a gate that can be undone |

`XD-01` status: **`OPEN — BOSS AUTHORITY REQUIRED`**, narrowed from three unanswered questions to
**two decisions plus one delivery**, with the durability precondition added.

---

## 4. `BN-05` dropship — the `HOLD` ground CORR1 retreated to is answered

### 4.1 What CORR1 said, and what was actually available

CORR1 retained `HOLD` on the ground that *"whether title passage without own-warehouse movement
requires a recorded inventory event is undetermined, and that is accounting-material."*

**Instrument.** PATTERN `drop.?ship` (case-insensitive), POPULATION the 183-branch corpus, UNIT
unique path (U2), no directory pre-filter, attributed to programme afterwards.

| Path attribution | Paths (U2) |
|---|---|
| `STATE03_MIGRATION_FACTORY` (Group A design/verification tree and Phase SA) | 30 |
| **`ACCOUNT_REOPEN`** | **20** — of which **16 in `P02_ORDER_TO_CASH`** |
| `GROUP_A_SALES_INVENTORY_PURCHASE` | 12 |
| `INVENTORY_REOPEN` | 11 |
| other | 3 |
| **Total** | **76** |

CORR1 reported the corpus-wide figure and then read **only the Group A hit**. The twenty
Account-programme paths were never opened.

### 4.2 What the Account programme establishes — `FACT VERIFIED`

> **`FACT VERIFIED` — TC-31.** In v19 a dropshipped sale is excluded on **three** independent paths,
> verified:
> 1. **No stock-side entry** — the delivery gate requires the movement to be an inflow or an
>    outflow, **and a dropship movement is neither**.
> 2. **No invoice cost line** — the cost generator's own predicate skips any line whose movements
>    are dropshipped.
> 3. **No vendor-bill account redirect** — the same predicate gates the purchase-side substitution,
>    so the bill keeps its ordinary expense account.
>
> The prior generation had a **purpose-built** dropship entry for exactly this case. **The current
> generation's sell-side leg posts revenue and receivable and nothing else**; cost recognition
> displaces entirely to the vendor bill, at the bill's date, **with nothing linking it to the sale.**
> — `.../P02_ORDER_TO_CASH/22_P02_TARGETED_CLOSURE_DEPLOYED_EVIDENCE.md` §15.3

Corroborated independently from the buy side:

> `Dropship exclusion | none [prior generation] | [current] excludes dropshipped`
> — `.../P01_PROCURE_TO_PAY/P01_S18_RECEIPT_VALUATION_ACCOUNTING_TRACE.md`

and bounded by deployment measurement:

> `Drop-ship, subcontracting, consignment and intercompany are **correctly absent, each ruled out
> with a control.**`
> — `.../P01_PROCURE_TO_PAY/P01_S16_RECEIPT_TO_VENDOR_BILL_AP_TRACE.md` §1

### 4.3 `C2-F-02` — the question is answered, and the answer is worse than "undetermined"

**A dropship movement IS recorded as an inventory event.** It exists as a movement. It is simply
**neither an inflow nor an outflow** — a third category the valuation gate does not recognise.

So the question *"does title passage without own-warehouse movement require a recorded inventory
event?"* is not open. The reference records the event and then **excludes it from valuation on
three independent paths**, with the consequence that:

- the sell-side leg recognises **revenue, receivable and tax, and no cost**;
- the cost lands on the vendor bill, at the **bill's** date, **unlinked to the sale**;
- so the matching of cost to revenue for a dropship sale is **not late — it is absent**, and no
  identity connects the two sides.

| Register | Was | Now | Basis |
|---|---|---|---|
| `SA05` BN-05 | `HOLD` — title-passage question undetermined | **`PARTIAL`** — the inventory-event question is **answered**; what remains is the SMEsPlus determination of where dropship cost is recognised and what links it to the sale | §4.2 |
| `SA06` IR-13 | `NOT RECONCILED` | **`RECONCILED — AS A MEASURED NEGATIVE`**: a dropship movement is recorded and is deliberately outside valuation. SMEsPlus must decide whether it adopts that | §4.2 |
| `SA07` AR-24 | `NOT RECONCILED` / `UNKNOWN` | **`PARTIAL`** — recognition point is established for the reference (revenue at invoice, cost at vendor bill, unlinked). The SMEsPlus determination is open | §4.2 |
| `SA15` E2E-05 | `NOT TRAVERSABLE` | **`TRAVERSABLE WITH A NAMED BREAK`** — every hop now has an evidenced producer and consumer; the break is the missing cost-to-revenue identity and the control-floor bypass `SA03-F-02` | §4.2 + `SA03-F-02` |

### 4.4 `C2-F-02b` — the third-order form of the same defect: CORR1 retreated to its **own coinage**

The parent package's falsified headline rested on `cancellation.gate`, which `SA20` §2.1 correctly
identified as **Group A's own coinage** — a phrase the Account programme was never going to write.

**CORR1's replacement `HOLD` ground was stated as "title passage without own-warehouse movement".**
Measured:

| Clause | Declaration |
|---|---|
| PATTERN | `title (passage\|transfer)\|transfer of title\|passage of title` |
| POPULATION | the 183-branch corpus |
| UNIT | unique path (U2) |
| RESULT | **6 paths — every one of them inside `PHASE_SA_CROSS_MODULE_ASSURANCE_2026_09_08/` itself. `ACCOUNT_REOPEN` = 0.** |
| POSITIVE CONTROL | `drop.?ship` over the same population, same command shape → 20 paths in `ACCOUNT_REOPEN`. The instrument reaches that path set |

> **"Title passage" is Phase SA's own coinage.** A `HOLD` retained on a phrase that exists nowhere
> outside the register retaining it cannot be closed by any other party, because no other party
> can write it. The Account programme *does* answer the question — in its own vocabulary, which
> speaks of whether a movement is an inflow or an outflow and whether it is valued.

This is the **third** occurrence of one defect in three consecutive rounds: the parent searched its
own vocabulary, CORR1 corrected that and searched its own **directory**, and CORR1's replacement
ground was stated in its own **coinage**. The class is not "a bad pattern". It is:

> **A party states the open question in the words it already uses, and those words are the one
> string the answering party will not have written.**

The control that catches it is not a better pattern. It is **requiring the question to be restated
in the answering party's vocabulary before the negative is published** — and the cheapest form of
that is to run the instrument against the other party's path set with a positive control proving it
reaches there.

### 4.4 Nature DNA determination `ND-09` — arising from this closure

> **A cross-module fulfilment that produces revenue must produce a cost recognition bound to the
> same identity, or an explicit, recorded determination that it does not.**

Independent rationale: `BD-ACC-01` gives the Accounting Core a canonical, immutable Accounting
Event Identity precisely so that related facts can be joined. The evidenced reference behaviour is
the counter-example — two halves of one commercial act, recognised in two modules, on two dates,
with **no identity between them**. SMEsPlus inverts this. This is learning declined, not inherited.

---

## 5. `C2-F-03` — a `CONFLICTING` flag inside the Account programme is resolvable on existing primary evidence

Found while testing §4. Two Account-programme packages hold incompatible positions on what
**Perpetual** valuation means, and one of them says in terms that it must not be silently resolved:

| Source | Position | Status it carries |
|---|---|---|
| `.../04_MENU_B_PRODUCT_CATEGORY_ACCOUNTING_FIELD_REGISTER.md` | *"the Perpetual method 'impacts the stock valuation account at the invoice level' rather than at each stock movement, described as a 'significant shift'… This directly contradicts the interim-account mechanism observed and well-corroborated"* | **`CONFLICTING` — "must not be silently resolved — it is material to `JT-04`"**, and `PROVISIONAL` because it was *"observed via a single documentation-derived summary rather than a directly quoted field label"* |
| `.../P02_ORDER_TO_CASH/22_P02_TARGETED_CLOSURE_DEPLOYED_EVIDENCE.md` §15.2 | The current generation's own interface labels read **`Periodic (at closing)`** and **`Perpetual (at invoicing)`**, default `periodic` | **`FACT VERIFIED` — TC-29**, read from the product's own field label |

**Resolution.** The programme's own standing rule is that **a summary may locate a source but may
never be the evidence**, and that a secondary source is never silently upgraded to primary. One of
these two is a documentation-derived summary that says so about itself; the other is a primary
read of the product's own label. **They do not have equal weight, and the conflict resolves in one
direction.**

**`C2-F-03`: `JT-04`'s `CONFLICTING` flag is discharged on existing evidence. In the current
reference generation, "Perpetual" means "at invoicing", primary-source confirmed.** No research is
required; a `PROVISIONAL` secondary observation was standing against a `FACT VERIFIED` primary one
in a sibling package, and no control compared them because each was inside its own package.

### 5.1 The consequence, which is larger than the flag

> **`FACT VERIFIED` — TC-30.** `BP-02` — *for a normal perpetual storable target, COGS is recognised
> at delivery* — **is not selectable** on the current generation: choosing "Perpetual" selects *at
> invoicing*, by definition. `BP-02` therefore requires a mechanism the product does not offer, not
> a setting. — `.../22_P02_TARGETED_CLOSURE_DEPLOYED_EVIDENCE.md` §15.2

The master prompt §6 mandates the SMEsPlus determination
`Inventory Valuation Recognition: Periodic | Perpetual, at Product Category only`.

**That determination is sound and is preserved. What cannot be preserved is the assumption that
`Perpetual` can be *learned* from the reference.** In the current generation the word denotes a
different recognition point than the one SMEsPlus intends. Recording `Perpetual` in a SMEsPlus
register without defining it would import an ambiguity that a reader would resolve from the
reference — which is inheritance by vocabulary.

**Nature DNA determination `ND-10`:** *SMEsPlus defines `Perpetual` explicitly as recognition at
the physical movement, and `Periodic` as recognition at period close, and states both definitions
wherever the terms appear.* Independent rationale: the same two words denote two different
recognition points across two generations of one reference product; a term whose meaning moved
once will move again, and a definition is the only thing that survives it.

---

## 6. Handoff matrix — `UPSTREAM OUTPUT → HANDOFF CONTRACT → DOWNSTREAM REQUIRED INPUT`

Only handoffs whose status **changes** in this round are listed in full; unchanged handoffs are
consumed by pointer to `SA03`/`SA04` under `AUTO-C2-01` (delta first) and are not re-derived.

| # | Upstream output | Handoff contract | Downstream required input | Owner | Trigger / timing | Company / tenant | INV | ACC | Tax / payment | Reversal | Status | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `H-01` | Customer-invoice lifecycle state | **none published** — `XD-06`, a ruling with no contract | Sell-side cancellation gate | Accounting Core | on state change | Tenant + Company (`BD-ACC-01`) | none | revenue, AR, tax, COGS at `posted` | tax arises at `posted` | credit note reverses all four | **`CONTRACT REQUIRED`** — content now known (§3.4), interface still unpublished | `BE-13`…`BE-18`, `AE-04` |
| `H-02` | Dropship movement (neither inflow nor outflow) | **none** | Inventory valuation gate | Inventory | on movement | Company | movement recorded, **valuation excluded** | **no cost in the sell-side leg** | — | — | **`SEMANTICALLY INCOMPATIBLE — MEASURED`**: the producer emits a movement the consumer's gate cannot classify | `TC-31` |
| `H-03` | Dropship cost, on the vendor bill | **none** | Sell-side cost of sales | Purchase / AP | at bill date | Company | — | expense, ordinary account | — | — | **`NO IDENTITY`** — *"nothing linking it to the sale"* | `TC-31` |
| `H-04` | Sell-side subcontract-service line confirmed | direct **write** into Purchase | Buy-side commitment | Sales | on line confirmation | Company | — | — | — | — | **`BELOW THE CONSUMER'S CONTROL FLOOR`** — bypasses the demand-approval gate every human-raised purchase must pass (`SA03-F-02`) | `SA03-F-02` |
| `H-05` | Draft customer invoice | implicit | Sell-side billable-now quantity | Accounting | on draft creation | Company | — | **none posted** | — | freely deleted | **`COMPATIBLE — WITH A NAMED HAZARD`**: *a draft already consumes billable quantity* while posting nothing, so an unposted, freely-deletable document reduces what Sales believes it may bill | `BE-13`, `EV-P02-005` |
| `H-06` | Posted invoice accounting date | implicit | Period membership | Accounting | on posting | Company | — | period assignment | tax period | — | **`UNSAFE`** — the accounting date is *"silently movable past a lock"*; and there is **no accounting-period object** (`G-11`) | `EV-P02-013`; `SA13` §4.2 `G-11` |
| `H-07` | Matching / reconciliation state | implicit | Settlement history | Accounting | on match | Company | — | — | cash-basis tax keys off it | **matching rows freely destructible across a closed period** | **`NOT DURABLE`** | `T2` §2, §7 |

### 6.1 `C2-F-04` — three of seven changed handoffs fail for the same reason

`H-01`, `H-02` and `H-03` are all failures of **identity**, not of data:

- `H-01` — the fact exists and no interface publishes it;
- `H-02` — the movement exists and the consumer's classification has no category for it;
- `H-03` — both halves of one commercial act exist and nothing joins them.

This is `XD-06` — *a ruling without a contract* — expressed three times. `BD-ACC-01` already assigns
the canonical Accounting Event Identity to the Accounting Core. **What is missing is not a decision;
it is the published contract that the decision presupposes.** It is a design obligation, correctly
owned by SMEs Core, and it is the single highest-leverage item in this register: three handoffs, and
`H-06`/`H-07`'s durability problems, all reduce to it.

---

## 7. Handoffs deliberately NOT re-opened (`AUTO-C2-01`, `AUTO-C2-10`)

Consumed by pointer, unchanged, not re-derived: `R-01`…`R-19`, `R-21`, `R-23` in `SA04` §1; the
Inventory single-movement-ledger determination (`SA06` §1); the four approval interface facts
(`SA08` §3); the cross-company relationship register (`SA10` §6). Failure containment applies —
nothing in §§3–6 above resets any of them.

---

## 8. Checkpoint

`CP-SA-C2-10 — CROSS-MODULE HANDOFFS RECONCILED (execution status).`

**Reconciled and closed:** the `XD-01` question set is decomposed into two decisions and one
delivery; `BN-05`/`IR-13`/`AR-24`/`E2E-05` move on measured evidence; `JT-04`'s `CONFLICTING` flag
is discharged.

**Reconciled and open:** seven handoffs carry a named status, of which `H-01`, `H-02`, `H-03` are
one root cause (`XD-06`) and `H-04` is a control-floor breach.

Checkpoint completion is **not** Boss approval.

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
