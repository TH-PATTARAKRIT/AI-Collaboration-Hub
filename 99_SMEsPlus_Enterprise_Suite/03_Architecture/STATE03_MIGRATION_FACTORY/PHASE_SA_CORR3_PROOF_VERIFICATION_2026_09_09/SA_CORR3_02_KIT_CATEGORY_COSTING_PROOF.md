# SA_CORR3_02 — KIT / PRODUCT CATEGORY COSTING PROOF
## CP-SA-C3-10 (C2-D-03 limb) — DETERMINE WHETHER EXISTING BOSS POLICY ALREADY RESOLVES THE CASE

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR3-PROOF-001]` · Finding prefix `KIT-`
Governing law: CORR3 master prompt §5 — *"Determine whether existing Boss policy already resolves the
case. Escalate only if a genuine policy choice remains after proof."*
Frame: **`CORR3-FRAME`**, adopted by pointer. **`BD-ACC-03A` and `BD-ACC-03B` are preserved intact and
this proof proposes no amendment to either.**

> **Orchestrator intake note.** Same-model executor; `INTERNAL ADVERSARIAL SELF-CHALLENGE`; **not
> adopted on its word.** The runtime claims were the ones most worth checking and they **verify**: all
> four named database archives exist on the execution host with the exact names and dates reported —
> `iSMEs_2026-07-11`, `iTEST02_2026-07-14`, `iEVING_2026-07-23`, `BK12MAY26_2026-08-03`. This executor
> genuinely read evidence at rest rather than reasoning from the corpus, and it **discharged an open
> recommendation two prior sessions had left standing.** The primary `BD-ACC-03A`/`03B` text it quotes
> was independently confirmed at blob `1db097c7…`.

---

## 1. The verdict, stated first

CORR2 escalated `C2-D-03` to Boss in these words, read from its own register row:

> `C2-D-03` | When a kit and its components sit in different Product Categories, **which category's
> valuation and costing policy governs?** | **Boss** … | **No amount of research resolves an ambiguity
> in a ruling**

> **`C2-D-03` rests on a false presupposition.** The question *"which single category's policy governs
> a kit?"* presupposes that a kit transaction has **one** valuation subject requiring **one** policy.
> It does not. `BD-ACC-03A`/`03B` bind policy to the **Product Category of a valued object**, and a kit
> transaction contains **as many valued objects as it contains moving stocked component products** —
> the parent among them only if the parent is itself a stocked object, **which is a configuration
> SMEsPlus must forbid for an independent accounting reason** (§9). **The ruling returns a determinate
> answer for every enumerated case, and returns it without a plural.**

| | |
|---|---|
| **Verdict on CORR2's claim** | **FALSIFIED.** Research resolved it. §11 gives the measurement |
| **True conflict with `BD-ACC-03A`/`03B`?** | **None.** §8 tests for one and does not find one |
| **Reclassification of `C2-D-03`** | From class **D** (*genuine Boss policy decision*) to class **A** (*SMEs Core can resolve — study/proof required*), **now resolved** |
| **Residual genuinely open** | One **scope** item, not a policy ambiguity: whether SMEsPlus adopts a kit construct at all (`KIT-G-01`). Owner Product / Team B, open since the Inventory reopen |
| **New design obligation SMEs Core can specify without Boss** | `KIT-D-01` — a kit parent must not itself be a valued stock object (§9) |

---

## 2. Instruments, denominators, controls

### 2.1 `INSTR-1` — corpus instrument

PATTERN `\bkits?\b|phantom` (-i); PATH SET `CORR3-FRAME`; UNIT blob and path.
**RESULT: 96 blobs; 68 distinct paths.** Positive controls `BD-ACC-01` = 55, `clean.room` = 1,266;
negative control 0.

**Instrument trap recorded (`KIT-M-02`).** The token `phantom` is **polysemous in this corpus**. In the
kit population it names a structure-level explosion flag; in the COGS and order-to-cash packages it
names a *phantom-cost* defect class — an unrelated finding about cost lines created with no stock
behind them. **A count of `phantom` is not a count of kits.** Every kit figure below was re-derived
from the structure-flag sense only. **An unpublished single-token search here would have inflated the
kit population by the whole COGS/landed-cost lineage.**

### 2.2 `INSTR-2` — runtime instrument, evidence at rest — **NEW THIS ROUND**

The corpus's kit reachability claims are all single-deployment. P01 left an open recommendation:

> Before P03 inherits any "kits are used elsewhere" premise, **both controls … must be re-run on the
> series-18 and series-19 deployments.**

P03 declined it on a stated materiality ground and **recorded the decline as a rejected delta.**
**This round executes it. That open recommendation is now `DISCHARGED`.**

| Clause | Declaration |
|---|---|
| POPULATION | **4 of 4** database archives at rest in the host download store, **enumerated by directory listing, not chosen**: `iSMEs` (2026-07-11), `iTEST02` (2026-07-14), `iEVING` (2026-07-23), `BK12MAY26` (2026-08-03) |
| PATH SET | the host download store. **Complement declared:** `/Volumes/iMac`, `/Volumes/iMacSys` and `$HOME` were **not** swept — `KIT-U-03` |
| GENERATION SPLIT | `iSMEs` is the earlier generation (651 data-bearing tables; category valuation policy held in a **generic property store**). The other three are later (875 / 881 / 1,315 tables; valuation and costing held **as fields on the category record**). **Every count below is generation-qualified** |
| TOOLING | An archive-reader utility at **two** major versions. The earlier **cannot read** the `iTEST02` format and fails with an explicit unsupported-version error; the later reads all four. **Both were located on the host before any negative was written — a capability negative was not asserted, it was checked and then refuted** |

**Controls: four reproductions, one second-shape validation, one injection, one disclosed failure.**

| # | Control | Result |
|---|---|---|
| R1 | Reproduce P01/P03's published structure-line movement figures on `iSMEs` | **34,492** movements; **0** carrying both a structure-line and a purchase-line link. **Reproduces exactly** |
| R2 | Reproduce P01's published structure count on `iSMEs` | **983**. Exact |
| R3 | Reproduce the service-typed-yet-storable anomaly on `iTEST02` | **989**. Exact |
| R4 | Reproduce *"3 of 3,980 categories override"* | **3 of 3,980**. Exact |
| S1 | **Second shape** — raw token scan instead of positional field extraction | Identical per-deployment kit-flag counts (0/0/0/0) |
| I1 | **Injection control** — substitute the kit flag onto the structure records and re-measure | **0 → 983.** The predicate can fire |
| **F1** | **Disclosed instrument failure (`KIT-M-01`)** | The first execution split records on **whitespace instead of tab**, returning `iSMEs` movements = 15,427 and both-links = 14,087 — **plausible, internally consistent, and wrong.** Caught **only** because it failed to reproduce R1. **Recorded because a reader must know this instrument has a silent-failure mode producing publishable-looking numbers, and that reproduction of a peer's published control — not self-consistency — is what detected it** |

**Denominator delta disclosed (`KIT-U-04`).** `iTEST02` holds **83,755** product master records; the
prior register declares **83,753**. Delta = **2**, unreconciled, and **no conclusion depends on it.**

---

## 3. The ruling, read from its own primary text and status field

From `01_BOSS_APPROVED_ARCHITECTURE_RULINGS.md`, blob `1db097c7`. Header `Authority: Boss — Sole Final
Approver` / `Status: APPROVED`. Both rulings carry `CLOSED / BOSS APPROVED`:

> **BD-ACC-03A** — Allowed policy values: `Periodic | Perpetual`. **Policy authority: Product
> Category.** Product must not override this policy.
> **BD-ACC-03B** — Allowed policy values: `Standard | Average | FIFO`. **Policy authority: Product
> Category.** Product must not override this policy.

and, one section later, the boundary `C2-D-03` never cites but which is load-bearing:

> **Product > Accounting boundary** — At Product level the approved override surface is limited to
> Income Account, Expense Account, **Price Difference Account**. … Periodic/Perpetual and
> Standard/Average/FIFO are **not** Product-level override controls.

**Three clauses `C2-D-03` does not engage, and that decide it:**

**(a) *"Policy authority: Product Category"* is a *binding* rule, not a *selection* rule.** It says
where the policy for a product lives. **It does not say a document, an order line or a commercial offer
has one policy.** Reading it as *"each transaction resolves to a single category's policy"* is an
**addition** to the ruling, not a reading of it. And the ruling's own closing sentence — *"These
rulings supersede any unresolved Phase S question that asks the same decision without a material
delta"* — makes clear they are meant to be **applied**; `C2-D-03` supplies no material delta, it
supplies a case the ruling already covers.

**(b) The ruling is silent on kits because it is scoped to *products*, and its subject is a *valued
object*.** A policy for valuation recognition and costing method is a policy about **how a quantity of
stock is measured**. It attaches to a thing that is measured. **Nothing that is never measured needs
one.**

**(c) The ruling already permits heterogeneity across categories inside one company, by
construction.** Placing authority *at* the category **is** a grant of per-category divergence. §6 shows
this is not theoretical: it is **live and measured**. **A kit adds no new heterogeneity that a two-line
invoice for two ordinary products does not already produce.**

---

## 4. Clean-room semantics: two distinct constructs, neither a product classification

**`C2-D-03` conflates them under one word.**

| | **Construct A — logical kit (structure-flagged explosion)** | **Construct B — selector bundle** |
|---|---|---|
| What it is | A flag on a **product structure definition**, not a value of any product classification field | A **sell-side commercial offer** letting a customer choose one item per group |
| What moves | **The components. The parent never moves.** Fulfilment is redirected at rule-dispatch time | Neither — it **resolves through its constituent entries** to real products |
| Can it be bought? | Yes, as a document-level object: the buy side **apportions the parent's price across the component layers by a cost-share step** | **No** — forced non-purchasable when the type is set |
| Parent's own nature | **An ordinary goods-type product carrying its own storability value.** No constraint forces it non-storable | n/a |
| Classification status | **Not a member of the Stockable / Consumable / Service split** — it must be resolved to components *before* the split is applied | Same |

The operative determination, from `SA_CORR2_05` §4:

> Established: a kit is a **structure-level flag, not a product classification**. When a sale line
> carries one, the fulfilment flow is redirected to create physical movements **for the components, not
> for the parent** … **The parent product never moves.** So the movement reconciles: **components move,
> the kit does not.**

And, **already written down in the corpus before `C2-D-03` was raised**, the accounting consequence —
in an Account-side matrix row whose four accounting-effect columns each read *"Per constituent"*:

> | `V-10` | Combo / kit | Bundle sold | Resolves to constituent items before classification |
> **Accounting sees constituent lines only** | … | Per constituent | Per constituent | Per constituent |
> Per constituent |

> **`KIT-F-01`. The answer CORR2 escalated as unresearchable was already recorded in the corpus, in an
> accounting register, in the form "per constituent" — and was not consumed, because the consuming
> registers reached for the word *kit* rather than for the valued object. The determination was not
> missing; it was not joined to.**

### 4.1 The level rule already exists, was already accepted, and already covers this

`SA_CORR2_05` §5 settles the level: *"The correct application level for the three-way split is the
**line item / SKU**, not the transaction or document as a whole."* And the Account-side matrix had
already applied that to a mixed document — row `V-09`, a repair invoice carrying parts and labour on
one document, resolved **"Per line"** across every accounting column, noting *"Parts move stock; labour
does not."*

> **`KIT-F-02`. A kit is the same shape of case as `V-09`, which the corpus resolved without
> escalation. One commercial document, several valued objects, each carrying its own policy. There is
> no principle in the kit case that was not already applied and accepted in the mixed-document case.
> `C2-D-03` escalated a case class the programme had already closed at a different label.**

---

## 5. Reachability — measured on four deployments (new)

CORR2 recorded kit reachability on **one** deployment. This round measures **four**.

**Structure definitions carrying the kit-explosion flag**

| Deployment | Generation | Structures | **Kit-flagged** | Other flags |
|---|---|---|---|---|
| `BK12MAY26` | later | 0 | **0** | — |
| `iEVING` | later | 1 | **0** | 1 ordinary manufacturing |
| `iSMEs` | earlier | 983 | **0** | 942 ordinary active + 41 archived |
| `iTEST02` | later | 87 | **0** | 85 active + 1 archived + 1 subcontracted |
| **TOTAL** | | **1,071** | **0** | |

Second shape identical; injection control flips 0 → 983.

**Movement-level fingerprint** — the structure-type flag is **mutable**, so a current-state census
cannot answer *"could a structure have been kit-flagged and later changed?"* The movement fingerprint
can, because a movement raised by explosion carries a permanent structure-line link.

| Deployment | Movements | Structure-line link | Purchase-line link | **BOTH** |
|---|---|---|---|---|
| `BK12MAY26` | 14,441 | 0 | 2,855 | **0** |
| `iEVING` | 13 | 0 | 4 | **0** |
| `iSMEs` | 103,949 | **34,492** *(positive control)* | 14,153 | **0** |
| `iTEST02` | 55 | 0 | 40 | **0** |
| **TOTAL** | **118,458** | **34,492** | **17,052** | **0** |

**Selector bundle:** **0 of 87,967** product master records across all four; the store is **present and
empty** in three and **absent** in the earlier generation. *(Stated deliberately: an absent store and an
empty store are different facts, and a size- or existence-only check cannot tell them apart.)*

> **`KIT-F-03` — `DEPLOY: LATENT, on a four-deployment denominator.`** Across **1,071 structure
> definitions, 118,458 movements and 87,967 product master records spanning two platform generations**,
> the kit construct is used **zero** times and the selector bundle **zero** times. **P01's open
> recommendation is discharged and its single-deployment conclusion now holds on four.**

**What this does NOT establish.** `NO EVIDENCE FOUND ≠ FUNCTION DOES NOT EXIST`. The construct is
**present in the schema of all four** and is reachable **by configuration alone** — no code change is
required to create a kit. The correct statement: **the kit case is structurally available and
empirically unexercised.** A finding ranking the kit case by measured frequency would rank it at the
bottom; **a finding ranking it by *design obligation* must not, because SMEsPlus is being designed and
the frequency measured here is a property of a reference estate, not of SMEsPlus's future customers.**

---

## 6. The premise of `C2-D-03` is factually TRUE — and it is not about kits

### 6.1 Do parents and components sit in different categories?

| Deployment | Structures with resolvable components | **Parent category ≠ ≥1 component category** |
|---|---|---|
| `iSMEs` | 976 | **976 (100 %)** |
| `iTEST02` | 87 | 2 |
| `iEVING` | 1 | 1 |
| **TOTAL** | **1,064** | **979** |

> **`KIT-F-04`. The premise is not merely possible — in the largest structure population it is
> universal.** CORR2 was right about the configuration.

### 6.2 Does that spanning cross a *policy* boundary?

Measured on `iSMEs`, where 26 of 30 categories carry an explicit costing method and 15 of 30 an
explicit recognition mode:

| Boundary crossed | Count of 976 |
|---|---|
| Costing method differs, **counting fallback to platform default** | **507** |
| Recognition mode differs, counting fallback | **512** |
| Costing method differs where **both** categories carry an explicit policy | **22** |
| Recognition mode differs where **both** are explicit | **0** *(all 15 explicit are Perpetual)* |

Across the estate, **mixed costing methods inside one company are the norm, not the exception**:
4,084 categories measured across four deployments.

> **`KIT-F-05` — the finding that dissolves the escalation.** A parent and its components sitting under
> **different costing methods** is **LIVE, not latent** — 22 structures on a tolerance-zero measure, up
> to 507 counting the fallback. **But not one of those 979 category-spanning structures, and not one of
> those 22 policy-spanning structures, is a kit. Every single one is an ordinary manufacturing
> structure whose parent is a separately valued manufactured finished good.**
>
> **The case that is live is the manufactured-FG case, which `BD-ACC-03A`/`03B` resolves without residue
> (§7.3). The case CORR2 escalated — a kit parent that is not itself a valued object — is the one that
> never arises, and it never arises for a structural reason, not a statistical one.**

**CORR2 observed a real configuration, correctly, and attached it to the wrong construct.** The 100 %
spanning rate it would have found had it measured is **a fact about bills of material, not about
kits**.

---

## 7. Case register

| # | Case | Does `BD-ACC-03A`/`03B` resolve it? | Status |
|---|---|---|---|
| **K-01** | **Logical kit — the parent as a valuation subject** | **Not engaged — there is no subject.** The ruling binds policy to the Category *of a valued object*; the parent is not one | **`NOT APPLICABLE — EVIDENCE-BACKED`**, non-arising **proved** at §7.1, complement stated at K-02 |
| **K-02** | **Kit parent that is itself storable — the complement of K-01** | **Not resolved — and it must not be.** The ruling correctly declines to bless a configuration that double-counts. **A design invariant, not a policy choice** | **`GENUINE DESIGN OBLIGATION — SMEs CORE AUTHORITY, NOT BOSS`** → `KIT-D-01` |
| **K-03** | **Stock bundle — a genuinely stocked, assembled parent** | **YES.** The finished good's own category governs it; each component's category governs that component | **`RESOLVED BY EXISTING BOSS POLICY`** |
| **K-04** | **Component-level consumption on a kit sale** | **YES.** Each component is a valued object; its own category's recognition mode and costing method govern | **`RESOLVED BY EXISTING BOSS POLICY`** |
| **K-05** | **Manufactured kit / finished good** | **YES**, on both legs independently | **`RESOLVED`**, with a separate, **pre-existing, unrelated** gap carried not created: fixed production overhead has no injection path (`BLK-07`) |
| **K-06** | **Components in different categories from each other** | **YES**, and this is the ruling operating as designed | **`RESOLVED`** |
| **K-07** | **Parent category vs component categories — the literal `C2-D-03` question** | **YES — by dissolution.** Under K-01 the parent's category governs **nothing about valuation**; it may still govern the parent's income/expense account defaults — **a different surface, expressly separated by the Product > Accounting boundary.** The two categories govern **disjoint** things. **No contest, therefore no ambiguity** | **`RESOLVED`** |
| **K-08** | **Valuation recognition on a kit sale** | **YES, literally.** Category authority **is** a grant of per-category divergence. **And the kit adds nothing**: a two-line invoice for two ordinary products in differently-configured categories produces the identical split, already live | **`RESOLVED`** — §7.2 tests whether this hides a real gap and finds it does not |
| **K-09** | **`Standard \| Average \| FIFO` behaviour** | **YES.** Applied per component, per that component's category | **`RESOLVED`** |
| **K-10** | **COGS recognition on a kit sale** | **YES** for the *level* question, which is what `C2-D-03` asks. The **trigger event** is a separate, pre-existing item and **not kit-specific** | **`RESOLVED` for level**; trigger carried as `KIT-U-01` |
| **K-11** | **Returns of a kit** | **YES.** The reversing valuation facts attach to the same valued objects under the same categories | **`RESOLVED`**, bounded residual `KIT-U-02` |
| **K-12** | **Partial delivery of a kit** | **YES.** Partial delivery changes *how much* moves, **never *whose category governs*.** The valued object is unchanged | **`RESOLVED` for the category question.** Recognition-timing evidence is `PROVISIONAL`/`HOLD` in its own lineage and **is not made worse by kits** |
| **K-13** | **Substitution of a kit component** | **Cannot be tested — the construct is not specified anywhere in the programme.** Pattern `component substitut\|substitute component\|alternative component` = **0 blobs**, against a positive control of **360** on the `substitut` root — **the root fires, the compound does not** | **`NOT APPLICABLE — EVIDENCE-BACKED` for this round**, on a declared and controlled negative. **Complement:** if SMEsPlus later specifies substitution, K-13 re-opens — **but the answer is already determined by K-04**, since a substitute component is a different valued object under its own category |
| **K-14** | **Price difference on a kit purchase** | **YES — and the ruling is on the *right* side of this.** It places the **Price Difference Account at Product level**, i.e. at the *valued object*. The reference estate's defect is that its filter anchors on the **document line's** product. **The ruling's shape contradicts the defect** | **`RESOLVED`**; the ruling is **corroborated, not challenged** |
| **K-15** | **Inventory ↔ accounting reconciliation for a kit** | **YES.** Nothing in a kit changes the reconciliation unit | **`RESOLVED`** |
| **K-16** | **Selector bundle** | **Not engaged** — never a valued object on any path | **`NOT APPLICABLE — EVIDENCE-BACKED`**, non-arising proved **by measurement and by the non-purchasable constraint** |

**Register totals, derived from the rows:** `RESOLVED BY EXISTING BOSS POLICY` = **12** (K-03…K-12,
K-14, K-15) · `NOT APPLICABLE — EVIDENCE-BACKED` = **3** (K-01, K-13, K-16) · genuine obligation = **1**
(K-02, and it is **SMEs Core**, not Boss) · **`GENUINE POLICY GAP` requiring Boss = 0.**
**12 + 3 + 1 = 16.** ✓

### 7.1 Proving non-arising for K-01, rather than asserting it

**Structural, in three steps, each separately evidenced:**

1. **A valuation fact requires a movement of a valued object.** The programme's own boundary rule, not
   this register's premise: *"internal→internal emits no valuation fact. Only the disposition moves
   cost."*
2. **The kit parent supplies no such movement.** *"The parent product never moves"* — fulfilment is
   redirected to raise component movements at rule dispatch.
3. **Therefore the parent has no valuation quantity, no cost layer and no recognition event.** A policy
   governing *when a stock value is recognised* and *how a stock cost is computed* **has nothing to
   attach to. There is no contest between the parent's category and the components' categories, because
   the parent's category is never asked the question.**

**Empirical corroboration, kept subordinate to the structural proof:** 0 kit-flagged structures of
1,071; 0 kit-purchase fingerprints of 118,458 movements; two generations. **Corroboration only — the
structural argument would hold on a deployment full of kits.**

**The complement, stated:** the argument holds **only while the parent is not independently a valued
stock object.** If the parent is configured storable, a count adjustment, an internal transfer to a
non-internal counterpart, or a direct receipt **does** raise a parent movement — and then the parent's
category governs it, correctly, under the ruling. **That configuration is not forbidden anywhere**, and
it is the whole of K-02. **The complement of the non-arising claim is exactly one configuration, and it
is named, its guard measured (none exists), and turned into an obligation rather than left as a silent
assumption.**

### 7.2 Testing whether K-08 hides a real gap (the case for the other side)

The most credible route to a genuine gap: *one commercial promise produces cost in two different
periods, because component A's category is Perpetual and component B's is Periodic. Surely that needs a
policy?* **It does not survive, for two independent reasons.**

- **It is not kit-specific.** An ordinary two-line invoice for two ordinary products in
  differently-configured categories produces the identical split. **A gap that is not about kits cannot
  be `C2-D-03`.**
- **It is already the ruling's designed and live outcome.** In `iSMEs`, 15 categories are explicitly
  Perpetual and 15 fall to the default. **Heterogeneous recognition inside one company is operating
  now.** `BD-ACC-03A` placed authority at the category with full knowledge that a company holds many.

> **`KIT-F-06`. The strongest available argument for escalation collapses because the phenomenon it
> describes is general, already permitted by the ruling's own text, and already live in the measured
> estate.** If Boss ever wishes to constrain mixed recognition, that is a **new** ruling about
> `BD-ACC-03A`'s scope, not a resolution of an ambiguity inside it — **and nothing in the kit case
> creates the occasion for it.**

### 7.3 K-03 / K-05, the case that actually is live

Every one of the 979 category-spanning structures is this case, and the ruling resolves it with **no
residue and no plural**: the finished good is a valued object → **its own category** governs; each
component is a valued object → **its own category** governs each; consumption transfers value from
component categories into the finished good's cost. **The two policies are not in competition; they
operate on different objects at different points of the chain.**

The one genuinely broken thing here — fixed production overhead having no injection path — is
**pre-existing, separately owned, and completely independent of kits and categories.** It is carried,
not claimed, and **`C2-D-03` is explicitly not permitted to absorb it.**

### 7.4 The apportionment step — where the accounting substance actually lives

The buy-side evidence discloses a mechanism the escalation never mentions: when a kit is purchased, the
parent's price is **apportioned across the component valuation layers by a cost-share step**, and the
correction defect arises precisely because a whole-parent unit price is later set against *"a component
layer already scaled by"* that step.

> **`KIT-F-07`. This is the substantive accounting answer, and it confirms the same conclusion from the
> opposite direction: even where a kit *is* transacted as a single document line, the reference estate
> does not value the kit — it apportions the kit's cost onto the components and values each component.
> The valued objects are the components, on the buy side as on the sell side. `BD-ACC-03B` then applies
> per component, per its own category, to an apportioned share. Nothing anywhere values a kit.**

And the defect is instructive rather than threatening: the correction anchors on the **document line's
product** instead of the **valued object**; the ruling anchors on the **valued object and its
category**. **The ruling's shape is the fix for the defect, not a victim of it.**

### 7.5 What was measured about COGS, and what was deliberately not inherited

The programme's COGS lineage states, in its own mandatory single-event section:

> **There is no single universal trigger across the reference ERP's own documented configurations — the
> trigger is itself a configured choice, and it has changed in kind across versions.**

with three different answers from one product family. **This is the reason `C2-D-03` cannot be answered
by pointing at a reference behaviour, and also the reason it does not need to be.** The trigger question
is unstable and belongs to its own item. **The *level* question — which object's category governs — is
stable across all three regimes, because in all three the thing being valued is the moving stocked
product.**

---

## 8. Is there a TRUE conflict with `BD-ACC-03A` / `BD-ACC-03B`?

Tested four ways. **No conflict found on any.**

| Test | Result |
|---|---|
| Does any kit case require a **fourth** recognition value beyond `Periodic \| Perpetual`? | **No** |
| Does any kit case require a **fourth** costing method? | **No** |
| Does any kit case require **Product-level override** — the one thing both rulings expressly forbid? | **No.** The sharpest test and the one that matters. Every case resolves by asking a **category** about a **valued object**. **Not one case needs a product to override its category. The prohibition is never approached, let alone breached** |
| Does any kit case require a policy authority other than Product Category? | **No** |

> **`KIT-F-08`. `C2-D-03` is not a conflict with `BD-ACC-03A`/`03B`. It is a case the rulings already
> decide, misread as a case they fail to decide — and the misreading came from treating the *document
> line* as the policy subject instead of the *valued object*. Both rulings stand unamended, and this
> proof strengthens rather than qualifies them:** the Product > Accounting boundary's placement of the
> **Price Difference Account at Product level** turns out to be **precisely the anchor the reference
> estate got wrong** (§7.4).

---

## 9. `KIT-D-01` — the one obligation this study creates, and why it is not Boss's

> **The obligation.** *A product that is the parent of a kit structure must not itself be a valued stock
> object. SMEsPlus must enforce this as an invariant, at configuration time, with a blocking control —
> not as a convention.*

**Why it is necessary (evidence, not assertion).**

- The parent is *"an ordinary goods-type product with its own storability value"*. **Nothing forces it
  non-storable.**
- **No guard exists anywhere.** Corpus pattern for a kit-parent storability constraint returns **0
  blobs** against a **56-blob** positive control on the storability-field root — the instrument fires
  and finds nothing. In the reference estate, **zero table-level constraints of any kind** exist on the
  product master, and that same section documents **989 live records already violating a supposedly
  absolute storability invariant** — proof that the ORM-level discouragement relied on elsewhere **does
  not hold in practice on real data.**
- **The exposure is a double count, not a policy ambiguity.** If both parent and components are valued,
  one economic quantity of goods is measured **twice**. **That overstates inventory and misstates cost
  of sales. It is an error of measurement, not a choice between two defensible policies.**

**Why SMEs Core may specify it and Boss need not decide it.** It follows from **accounting substance**
(inventory must be measured once), not a preference between alternatives — **there is no second
defensible option to choose between**; it **preserves `BD-ACC-03A`/`03B` unamended**, removing an
*incoherent configuration* rather than moving policy authority; it touches **no Boss-reserved surface**;
and it is a **design invariant for Phase SA**, not implementation.

**Reachability, honestly stated.** `LATENT` on the four-deployment denominator — 0 kit structures exist,
so the configuration has never been created. **Ranked as an obligation on the *design* ground, not a
frequency ground: SMEsPlus is being designed for customers who have not yet configured anything, and a
measured frequency of zero in a reference estate is not a prediction about them. Stated so the ranking
cannot be mistaken for a reachability claim.**

---

## 10. What SMEsPlus should adopt, and what it explicitly declines to copy

**Adopted, on independent justification** (never "the reference does it"): valuation policy binds to
the **valued object**, and a valued object is one that moves across the internal boundary — *this is
what an inventory measurement basis **is***, and it is the programme's own already-accepted line-item
level rule; a kit is a **structure-level construct**, never a product classification — *a construct that
resolves to components cannot also be a member of the set it resolves into*; a kit's cost is
**apportioned onto components**, each valued under its own category — *the only treatment preserving a
single measurement of a single quantity, and the only one surviving a component being sold, returned or
written down separately*; a kit parent must not be a valued stock object; and price-difference
correction must target **the valued object**, never the document line's product.

**Explicitly declined, each with its reason:**

| Declined | Reason |
|---|---|
| The reference's kit-purchase price-difference handling | **Not a design.** `FACT VERIFIED` that the whole of it is a two-line comment saying it must be done manually, with **no procedure, wizard, report, flag or reconciliation surface** behind it. Copying it would import an unowned manual step disguised as a feature |
| The **document-line product anchor** in the correction filter | **Demonstrably wrong: 13 live rows actively drop valuation layers**, against a **14,335** positive control, with a synthetic injection flipping the measure **0 → 1**. And the mismatch is **unrecoverable** — the participants are all narrowings, they commute, and a dropped layer cannot be reintroduced |
| The reference's COGS recognition trigger | *"No single universal trigger … it has changed in kind across versions."* **A pattern unstable across its own generations is not a target** |
| The reference's two-field product classification shape | Already quarantined, and the quarantine is **strengthened** by 989 live records violating the invariant that shape supposedly guarantees |
| The reference's selector-bundle construct | **0 of 87,967** records across 4 deployments; its store absent entirely in one generation; and it carries a live tax finding on the direct-invoice route |
| Any **assumption that a manual step exists** because a comment says so | The programme has been bitten by reading a docstring as a mechanism. **P01's own kit-gated interpretation was withdrawn on exactly this ground** |

---

## 11. Verdict on CORR2's claim, with the measurement

**CORR2's claim, verbatim:** *"This is an ambiguity inside a Boss ruling. **No research resolves it.**"*

> ### Verdict: **`FALSIFIED`.**

| Metric | Value |
|---|---|
| Enumerated cases in the mandate | **16** |
| Cases resolved by **quoting a clause of the existing ruling** | **12** |
| Cases that **cannot arise**, with non-arising proved and complement stated | **3** |
| Cases surviving both tests as a **genuine Boss policy gap** | **0** |
| Cases producing a **genuine obligation SMEs Core may specify** | **1** |
| Documentary evidence the claim's own package already held and did not consume | **an accounting register row reading "Per constituent" in four columns**, plus an already-accepted level rule and an already-resolved same-shape case |
| New runtime evidence produced this round | **4 deployments** (CORR2 had 1); **1,071** structures, **118,458** movements, **87,967** product records, **4,084** categories |
| Kit constructs found in that population | **0** |
| Category-spanning structures found | **979 of 1,064** — **the premise is true** |
| Policy-spanning structures found | **22** both-sides-explicit, **507** counting fallback — **the phenomenon is LIVE** |
| **Of those, how many are kits** | **0** |

**Why the claim failed, precisely.** CORR2 made **one** error, and **not an error of diligence** — its
measurement work was sound and its bounded negatives properly declared. **The error was of *subject*:
it asked *"which category governs the kit?"* when the ruling's subject is the *valued object*. Because a
kit has no valuation subject, the question has no referent, and a question with no referent reads as an
ambiguity from inside. The ruling was never ambiguous; the question was never answerable as posed.**

**Two uncomfortable corollaries:**

> **`KIT-F-09`.** CORR2 attached a **true and important** observation to the **wrong construct**. Had it
> measured rather than reasoned, it would have found the observation attaches to ordinary manufacturing
> structures, whose case the ruling resolves plainly. **The premise was right, the referent was wrong,
> and no amount of further reasoning about kits could have surfaced that — only a measurement of the
> structure population could.**

> **`KIT-F-10`.** The sentence *"no research resolves it"* is **itself a claim about the evidence base,
> and it was published without a search of the evidence base being declared.** The answer was already
> inside CORR2's own corpus, one register away, at a different label. **A negative about what research
> can achieve requires the same declared population, pattern, path set and unit as any other negative.
> It received none.**

---

## 12. Consequences carried to other registers — stated for their owners, not applied here

| Register / row | Current | Proposed | Ground |
|---|---|---|---|
| `SA05` `BN-07` Kit / bundle | **`HOLD`** | **`DETERMINED`** — the components carry the cost; the parent is not a valued object | §7.1, §7.4 |
| `SA_CORR2_02` §3.4 `BN-07` residual | `DECISION` (Boss) | **`RESOLVED — NO BOSS DECISION REQUIRED`** | §11 |
| `SA_CORR2_06` `AR-25` | `PARTIAL — LEVEL DETERMINED, POLICY AMBIGUOUS` | **`RECONCILED`** — level **and** policy determined per constituent | K-04, K-10 |
| `SA15` `E2E-07` | `NOT TRAVERSABLE` | **`TRAVERSABLE`** — **both stated blockers now closed** | §7 |
| `SA_CORR2_04` row 11 | `ADVANCED, AND ESCALATED` | **`ADVANCED — DE-ESCALATED`** for the valuation-policy half. **The routing/put-away half is a different question and is not touched** | §8 |
| `CORR-007B` §11 gaps 1–3 | `Open — Team B / Boss` | **`SUPERSEDED — EVIDENCE-BACKED`** by `BD-ACC-03A`/`03B` | primary text |
| P01's open recommendation to re-run both kit controls | Open; declined by P03 with reason | **`DISCHARGED`** — executed here on 4 of 4 host archives | §5 |
| `C2-D-03` classification | **D** | **A**, and now resolved | §11 |

**Carried unchanged and deliberately not absorbed:** `BLK-07` fixed production overhead and the COGS
trigger instability are real, separately owned, and **not kit or category questions. `C2-D-03` must not
be used to launder them.**

**Evidence-lineage item, independently re-verified on the wider frame (`KIT-F-11`).** CORR2 recorded a
planned artefact on kit cost correction as named-but-absent. **Verified here on the wider `CORR3-FRAME`
with a third command shape:** it is named at line 281 of its commissioning prompt and **occurs zero
times as a path or basename across all 3,715 paths / 3,445 distinct basenames** — positive control: 25
basenames contain `COGS`, so the basename instrument fires. **CORR2's finding stands and is now wider:
the artefact does not exist on any of the 184 branches.** Its subject matter is nonetheless
**substantively covered** elsewhere. **A missing artefact is a lineage defect, not necessarily a
knowledge gap, and the two must be reported separately.**

---

## 13. Findings register

| ID | Finding | Class | Reachability |
|---|---|---|---|
| `KIT-F-01` | The accounting answer ("per constituent") was already recorded before `C2-D-03` was raised, and not consumed because consumers searched for the word *kit* rather than the valued object | Evidence-location | n/a |
| `KIT-F-02` | A kit is the same case class as a mixed parts-and-labour document, resolved "per line" without escalation | Method | n/a |
| `KIT-F-03` | Kit and selector-bundle constructs **unused in 4 of 4 deployments** — 0 of 1,071 structures, 0 of 118,458 movements, 0 of 87,967 product records. **Discharges P01's open recommendation** | Deployment | **`LATENT`** — present in schema, reachable by configuration alone |
| `KIT-F-04` | Parents and components sit in different categories in **979 of 1,064** structures. CORR2's premise is true | Deployment | **`LIVE`** |
| `KIT-F-05` | Policy-boundary spanning is **live** (22 / 507) — **and not one instance is a kit** | Deployment | **`LIVE`** |
| `KIT-F-06` | The strongest argument for escalation is **not kit-specific and is already the ruling's live, permitted outcome** | Analysis | `LIVE` as a phenomenon; not a gap |
| `KIT-F-07` | Kit purchase cost is **apportioned onto components** — the reference estate itself never values a kit | Source | `LATENT` |
| `KIT-F-08` | **No true conflict with the rulings on any of four tests.** In particular **no case requires Product-level override** | Analysis | n/a |
| `KIT-F-09` | CORR2 attached a true observation to the wrong construct. **Only a measurement could have surfaced it** | Method | n/a |
| `KIT-F-10` | *"No research resolves it"* is a claim about the evidence base, published with **no declared population, pattern, path set or unit** | Governance / method | n/a |
| `KIT-F-11` | The named-but-absent kit artefact confirmed absent on the **wider** frame by a third shape — and its subject matter substantively covered elsewhere. **Lineage defect ≠ knowledge gap** | Evidence lineage | n/a |
| `KIT-M-01` | The runtime instrument has a **silent failure mode** — whitespace vs tab — producing **plausible, internally consistent, wrong** figures, caught **only** by failing to reproduce a peer's published control | Method | n/a |
| `KIT-M-02` | The token `phantom` is **polysemous**; a single-token count would have inflated the kit population by the whole COGS lineage | Method | n/a |
| `KIT-D-01` | **A kit parent must not itself be a valued stock object.** No guard exists (0 blobs against a 56-blob control; zero table-level constraints; 989 live violations of a comparable "absolute" invariant). **SMEs Core authority** | Design obligation | `LATENT`, **ranked on design ground not frequency** |
| `KIT-G-01` | Whether SMEsPlus adopts a kit construct at all is an **unanswered scope decision**, owned by Product / Team B, open since the Inventory reopen | Scope | n/a |

---

## 14. Residual uncertainty

1. **`KIT-U-01` — the COGS trigger event.** The *level* question is resolved; the *trigger* is not, and
   its own lineage records three different answers, two `PROVISIONAL`. **Not a kit question and not made
   worse by kits.**
2. **`KIT-U-02` — return re-explosion.** That a credit note reverses revenue, receivable, tax **and
   cost** is `FACT VERIFIED`. That a *return document* for a kit re-explodes to component movements is
   **inferred from the forward path, not evidenced.** The policy answer is unaffected; the mechanism is
   unproven.
3. **`KIT-U-03` — archive path set.** Enumerated exhaustively **within** the host download store.
   `/Volumes/iMac`, `/Volumes/iMacSys` and `$HOME` **not swept.** **Authority for the exclusion: none
   beyond time — a real bound, not a justified one, and it is not dressed as justified. This programme
   has twice found decisive evidence outside an undeclared path set.**
4. **`KIT-U-04`** — the 2-record denominator delta, unreconciled; no conclusion depends on it.
5. **`KIT-U-05` — generation coverage.** §6.2's policy-spanning was computed on `iSMEs` **only**, the
   only deployment with both a substantial structure population and a configured category population.
   **The 507 / 22 figures are single-deployment and must not be generalised.**
6. **`KIT-U-06`** — nothing was executed at runtime. All behaviour read from records at rest and
   documentary evidence. **No kit was configured, transacted, or observed.**

---

## 15. What could NOT be proven, and the exact proof gap

| # | Not proven | The gap | What would close it |
|---|---|---|---|
| 1 | That a kit **cannot** be configured with a storable parent | Proved **no guard exists**; **did not** prove the configuration is *possible*, because **no kit exists in any measured deployment to test it on** | A controlled install: create a kit with a storable parent, attempt an independent parent movement, observe whether a parent valuation fact is raised. **Read-only evidence cannot close this** — the same limit P03 recorded |
| 2 | Whether the kit purchase price difference reaches component cost | Inherited unresolved and **not closed here**. My four-deployment measurement **widens the denominator behind that negative from 1 to 4 but does not change its kind** | A controlled kit purchase with a bill price differing from the order price |
| 3 | That return of a kit re-explodes | `KIT-U-02` | A worked return trace |
| 4 | That no archive outside the download store holds kit usage | `KIT-U-03` — **an undeclared path set, disclosed rather than concealed** | A `/Volumes` + `$HOME` sweep, **with the pruning exclusions themselves declared** |
| 5 | That `KIT-D-01` is the **only** invariant needed | I enumerated 16 cases **from the mandate's own list** and found one obligation. **I did not prove the case list is complete — a mandate's list is not a denominator** | An independent party deriving the case set from the ruling's own clauses and comparing |

---

## 16. What a challenger should attack first

1. **The load-bearing claim: *"the parent never moves."*** Everything in §7.1 rests on it, and it comes
   from **one** determination in `SA_CORR2_05` §4. **I did not re-derive it from primary source; I read
   it from a peer's determination.** If the parent moves on **any** path — a receipt, a count
   adjustment, an internal transfer, a manufacturing output — **K-01 becomes a live case and `C2-D-03`
   becomes real again. This is the single highest-value attack, and I flag it rather than letting it sit
   as a quiet inheritance.** Aggravating factor: the same determination describes the redirect as
   happening *"on the sell side"*, and §7.4 shows the **buy** side handles kits by a **different**
   mechanism. **Two sides, two mechanisms, and only one of them is quoted in support of "never moves."**
2. **My reclassification of `KIT-D-01` as SMEs Core authority rather than Boss.** This programme has a
   recorded defect of promoting its own reasoning over a reserved decision. I argue double counting has
   no second defensible option — **but that argument is mine, it rescues my own conclusion that no Boss
   escalation is needed, and a test that rescues your own proposal is not yours to adopt.**
3. **The case list's completeness.** §7's 16 rows come from the mandate's enumeration. **A mandate's
   list is not a denominator.**
4. **`INSTR-2`'s silent failure mode.** One instrument produced two different, plausible answers for the
   same question. The failure and the control that caught it are published — **but the reader should
   re-run at least one figure independently rather than trust the disclosure. R1–R4 are the right place
   to start, because they are the only reason the failure was found.**
5. **The 22 / 507 figures.** Single-deployment, and the 507 depends on treating an unset category as
   falling to a platform default — **a treatment asserted from documentation and not independently
   verified. The 22 does not depend on it; the 507 does.**
6. **The verdict "falsified" rather than "narrowed".** The gentler reading is that CORR2 was right that a
   *policy* choice exists and wrong only about where it sits. **A challenger should test whether §11's
   measurement supports "falsified" or only "re-scoped" — §7.2 is where that distinction is decided.**

---

`SA_CORR3_02 — TARGETED RESEARCH COMPLETE — PROOF ESTABLISHED.`
**`C2-D-03` is resolved by existing Boss policy. No Boss decision is requested by this artifact.**
**`BD-ACC-03A` and `BD-ACC-03B` stand unamended.**

Checkpoint completion is **not** Boss approval. Boss remains the sole Final Approver.
