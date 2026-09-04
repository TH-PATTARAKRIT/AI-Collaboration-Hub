# MCC_J — FRESH EXPERT AND AUDIT CHALLENGE

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**
> `Independent Review ≠ Truth. Verified Evidence = Truth Basis.`
> **Every finding accepted below was re-read at primary source by this session before acceptance.**
> Findings reduced or rejected on verification are in §6. Layer 2 citations: `LAYER2_MCC_EVIDENCE/MCC_E02`.

---

## 1. Constitution

Six perspectives, none of them an author of this or any prior round, in two disjoint panels.

| Perspective | Assignment |
|---|---|
| `MCCX-1` | Functional / accounting semantics — challenge the `FX-08` disposition, every balanced-but-wrong case, and any accounting semantic the package still does not address |
| `MCCX-2` | Database / identity / integrity — try to break the raw-SQL absence, the constraint's unbypassability, `T0-08` and `T0-09`; find an unenumerated integrity population |
| `MCCX-3` | Integration / localization / migration — the Thai deployment, the upgrade residual, the v19 aggregator |
| `MCCX-4` | Code / UI / state-control architecture — client-vs-server enforcement, the lock-exception path, the unbounded state-control surface |
| `MCCX-5` | SaaS tenant / company isolation — is the reduction into `GB-01` legitimate, and what becomes tenant-crossing under a shared-database mapping |
| `MCCX-6` | Independent audit veto |

---

## 2. Result in one line

> **The challenge returned 12 accepted findings the package did not carry, invalidated 3 of its
> conclusions, corrected 4 of its counts, confirmed 8 of its claims, and issued `NO VETO` — while
> demonstrating that `GB-06` was live inside the package that declares `GB-06`'s remedy exercised.**

---

## 3. Package claims INVALIDATED — verified before acceptance

### `J-01` — `BW-28` reads correct consolidation semantics as an error. `MCCX-1`.

The reporting currency table joins on the **company's** functional currency, never on the journal
item's transaction currency, and companies sharing the consolidating company's currency are emitted at
**rate 1 by construction**. The posting resolver translates *transaction → functional*; the currency
table translates *subsidiary functional → group presentation*. Under IAS 21 these are different
measurement objects that **must** use different rate sources.

> **`BW-28` is WITHDRAWN as registered, and `MCC_B` §5's 6-include / 6-exclude symmetry — named there
> as "what `GB-03` is really about" — counts scoping rules across two measurement objects as one
> population.** The symmetry must be re-derived per object before it can carry a conclusion.

### `J-02` — a class-`A` absence was asserted over a control the round had itself listed. `MCCX-1`.

`BW-28` recorded *"Detecting control? **None**. Evidence the control exists? **None found.**"*
The multicurrency revaluation report computes the retranslation difference per line and per account,
**and its rate is user-overridable per currency**, with a warning raised when it is overridden. An
accountant supplying the correct closing rate sees a par-valued or 2010-valued balance as an enormous
adjustment. **The file is item 10 of this round's own 20-file surface, and this round never asked what
it does.** Bounded limit accepted: the control covers only open balance-sheet monetary items in a
foreign currency on non-excluded accounts, so for `J-04` the "no detecting control" statement stands.

### `J-03` — `T0-09` instance 2 falls. The empty constraint definition is a deliberate idiom. `MCCX-2`.

An empty definition string is the ORM's **delegation** marker: the framework drops any existing
constraint of that name and registers a **post-init assertion that the matching custom index exists**,
which raises if it does not. The defect at that site is the index's **scope**, not its declaration
form. **`T0-09` is left with one bounded instance and is therefore not bounded** — and `MCCX-4` then
found a third instance on the period lock itself (`J-08`).

---

## 4. New findings ACCEPTED — verified at primary source

### `J-04` — a whole foreign operation consolidated at par. `MCCX-1`. **Replaces `BW-28` as `BW-28a`.**

When the consolidating root holds **no rate row for a subsidiary's functional currency**, that
subsidiary's **entire** balance sheet and income statement are translated into the group presentation
currency at **1.0**, silently, with no warning line and no reconciling item. A third par substitution
sits inside the day-weighted average builder, where it contaminates a *blended* rate rather than
replacing one. **This becomes `T0-07`'s headline instance.** It is a consolidation-presentation
failure, not an FX-scoping failure, and it is more severe than what it replaces.

### `J-05` — the entry-balance invariant is enforced in ONE currency dimension only. `MCCX-1`. **NEW BOUNDARY.**

The balance assertion is a SQL `HAVING` over the sum of the **company-currency** balance, joined
through the company's currency. **The transaction-currency amount appears nowhere in it**, and no
constraint anywhere sums it. The only constraint touching it governs the **sign** relationship, never
a total.

A foreign-currency move has **two** balance dimensions and one is unconstrained. That dimension is the
input to unrealised revaluation, to residual-amount tracking and to realised FX on settlement.
**The whole balanced-but-wrong taxonomy presupposes one dimension.**

### `J-06` — the balance assertion itself is suppressible by context. `MCCX-1`. **NEW BOUNDARY, and it is the most severe finding of the round.**

The assertion is wrapped in a recursion-disabling context manager. **Any caller placing the
corresponding key in the context posts an entry with no debit = credit assertion at all.** Three
shipped production consumers exist, in the point-of-sale session path.

> **`unbalanced-and-posted` is reachable.** That is a worse state than balanced-but-wrong, and the
> taxonomy this round spent a phase proving has **no cell for it**. The key sits inside the bucket of
> 48 generic suppression tokens that `MCE-005` counted and no round ever assessed. **It is that
> bucket's most severe member and it was never opened.**

### `J-07` — a referential action manufactures the company-less rate row. `MCCX-2`. **A route no enumeration in the programme contains.**

The rate row's company field is **not required and declares no delete behaviour**, so the ORM resolves
it to the framework default and emits a real foreign key with **`ON DELETE SET NULL`**. The company
model's delete has **no guard**, and the accounting addon adds none.

> **Deleting a company converts every rate row it owned into a company-less rate row — at the database
> layer, by the foreign key, with no ORM call, no Python constraint, no log line and no
> revalidation.**
>
> This round's three bypass enumerations — 12 candidates, 12 rows, 10 routes — are all enumerations of
> **write paths**. **Not one contains a referential action.** The pattern is structurally blind to a
> defect that lives in what the source *does not say*, and the act that triggers it — deleting a
> legacy or template company — is routine administration. `MCC_E01 MCCX-01`'s framing that
> company-less rows are *"not shipped; they are user-creatable"* is corrected: they are also
> **system-manufactured**.

**Verified counter-fact, recorded because it bounds the finding:** the company hierarchy field
declares `restrict`, so a branch cannot be promoted to a root by deleting its parent — the database
refuses. The set-null lands only where a company delete succeeds.

### `J-08` — the lock-date wizard's company field is inert over an elevated write. `MCCX-4`. **Third `T0-09` instance, on the period lock itself.**

The shipped wizard declares its company field **required and readonly**, displays it, and **never uses
it**: the write targets the acting company and is performed under elevated privilege, gated only by
group membership. An accounting manager holding **no write right on the company model** can therefore
set that company's fiscal-year, tax, sale, purchase **and hard** lock dates. The file is in **neither**
the 18-file nor the 26-file Wave A surface.

### `J-09` — the lock-exception defect is wider than registered, and this round's mechanism attribution was wrong. `MCCX-4`.

| This round said | Verified |
|---|---|
| *"the model's own create routine explicitly honours a caller-supplied company"* | **MIS-ATTRIBUTED.** The create routine uses the supplied id only to look up the original lock date; the company field is honoured by **generic ORM create**, because readonly is inert. *This is the same mis-attribution defect this round convicts a parent evidence file of.* |
| — | **A sharper bypass, unnamed:** the single company **read** in create — the only step that could raise on a foreign company — executes **only if the original-lock-date key is absent from the values**. Supply that key and **no read of the target company happens at all**. |
| *"relaxes that company's lock"* | **UNDERSTATED, and this is the material half.** The consumption path iterates the company **and every ancestor** under elevated privilege, with a source comment saying so. **One exception created against the root, with no user and no expiry, relaxes the soft lock for every company in the entire root tree, for every user, forever — from a create right alone.** |
| reachability | **QUALIFIED.** The shipped UI hard-codes the acting company, so the cross-company *create* is reachable by direct RPC, not through any screen. The *revoke* path is UI-reachable and unqualified |

### `J-10` — the Thai statutory VAT export carries no company filter. `MCCX-3`. **Directly material to the deployment.**

The Thai VAT report handler builds a domain with date, journal type and payment state only, then calls
a bare search on the entry model with **no company term**. The governing record rule admits **every
company the user has active**. The workbook is then stamped with the acting company's name, VAT number
and **Thai branch name**.

> **A Thai Revenue Department filing artefact attributed to one legal entity can contain another
> entity's invoices.** The sibling withholding-tax handler in the same module scopes correctly through
> the report engine, so the defect is a divergence *within one localisation module*.
>
> This is a **third verified member** of the class this round carried as `MCU-04` / `MCU-11` with two
> members — and it is inside the only localisation SMEsPlus deploys.

### `J-11` — `account.report` has no company dimension, no record rule, and full manager CRUD. `MCCX-5`. **`MCU-04` is closable.**

The report-definition model carries a country and **no company field**. The accounting-manager role
holds **create, write and unlink**. **No record rule targets it anywhere in the primary tree** — a
declared enumeration of every reference to the model in XML returns a cron, a server action and a
binding, and **zero rules**. Two server actions carrying arbitrary server-side code are bound to it,
one granted to the ordinary accounting-user role.

> **`MCU-04` was carried as `REMAINS GATING — HOLD` on the ground that it is a tenant question. It is
> not.** The mechanism is fully determined by source and is determined here. Only its *consequence*
> under a given tenant mapping is conditional. **This is a real closure this round left on the table.**

### `J-12` — three of the four objects reduced into `GB-01` are research-closed. `MCCX-5`.

| Object | Reduction into `GB-01` legitimate? |
|---|---|
| Company-less rate row | **YES.** Mechanism research-complete; the remaining question — *is a company-less rate row legitimate in SMEsPlus at all* — is genuinely policy |
| Cross-branch reconciliation | **NO.** A defect in the reference implementation regardless of tenant mapping. It reduces to *fix or forbid* |
| Lock-exception cross-company path | **NO.** Not one element depends on the tenant mapping |
| Report definitions without a company dimension | **NO.** `J-11` |

> **Routing a research-closed defect into an open design decision is the same class of move as routing
> a blocker to a later Wave — which this round forbids and re-tests for.** Three of four are so routed.

### `J-13` — the crossing class has ≥7 verified members, not 1. `MCCX-5`.

A declared enumeration over the accounting addon returns **245 boundary-crossing sites** (144
excluding elevation calls, 112 elevation calls), of which the panel assessed **40 of 144 and 0 of
112**. The root-level-guard shape this round named with **one** member has at least **seven**:
the reconciliation guard, **two identical guards in the payment register**, and **four
shallowest-company selectors** that silently drop the other company. Account **code** resolution
additionally runs at root scope under elevation, outside every record rule.

### `J-14` — the v19 aggregator's reachability is both understated and overstated. `MCCX-3`.

**Understated as to surface:** the client emits the aggregator for **every monetary field**, in list,
pivot **and** graph views, opt-out rather than opt-in — so the record-rule-bypassing raw-SQL join
**executes** on essentially every grouped read of an accounting model. **Overstated as to visible
consequence:** all three view models **discard** the value and display the plain sum when a group
contains a single currency; the wrong figure surfaces only on groups spanning two or more currencies.
A **fifth** fallback semantic sits beneath it in the same expression.

### `J-15` — a migration risk with no artefact to review. `MCCX-3`. **New, subordinate to `GB-08`.**

The cross-version divergence is a **pure behavioural change with no schema change**, so it arrives
through an ordinary point-release upgrade with **no migration script, no data migration and no upgrade
artefact of any kind**. A v18 minor upgrade silently changes the company scope of every FX conversion
on a Wave A measurement; a later v18 → v19 migration silently changes it back and adds the new
aggregator. **There is no control point at which either change is visible to a
migration-acceptance process**, and `MCC_D`'s framing of the residual as answerable by *"one
`SELECT`"* is true of the rate-row half and false of this one.

---

## 5. Package counts CORRECTED

| # | This round published | Verified | Source |
|---|---|---|---|
| `J-C1` | *"the primary tree holds 2 localisations; the archive holds **904** … 2 of **906**"* | **454 distinct, 456 total.** 450 of the 904 are duplicate copies that **this round's own declared pattern excludes**. And **the archive tree contains no Thai localisation at all — the Thai modules are both inside the searched tree.** The finding's magnitude is overstated and its risk direction for the actual deployment is **inverted** | `MCCX-3` |
| `J-C2` | `MCC_E00 §MCC-E-005` rows 5 and 6, record rules *"apply"* | **BYPASSED.** Both framework helpers read the rate collection under **elevated privilege**. `T0-07`'s record-rule-bypassing **read** surface is **10**, not 8 — 8 raw-SQL plus 2 elevated ORM readers | `MCCX-6` |
| `J-C3` | *"5 migration directories"* in the primary tree | **4.** The fifth is a JavaScript test directory. The archive tree holds **70 more** that `MCC_E00` never searched, while `MCC_F` asserts the class-`A` negative over *"the migration and upgrade directories of every root"* — **two of this round's own files state two different scopes for one class-`A` claim.** The panel searched the wider set; **the conclusion holds** | `MCCX-3` |
| `J-C4` | `BW-35` — *"11 sites, complete", class `A`* | **The 11 reproduce; the path set does not.** The lineage field is referenced at **144 further sites in 30+ modules** outside the accounting addon, including a **field redeclaration** in the archive tree. **The panel executed the widened search and the conclusion survives** — there is no constraint on the field anywhere in either tree. **`BW-35`'s conclusion is re-established as class `A` over the corrected path set, on the panel's evidence, not this round's.** Recorded on the face of the gate report as the audit panel required | `MCCX-6` |

---

## 6. Challenge findings REDUCED or REJECTED on verification

| Claim | Outcome |
|---|---|
| `MCCX-2`: *"the `T0-09` guards are absent to the machine"* was the package's wording, and the panel's counter that they generate a client-side field domain | **ACCEPTED, and it changes the wording not the substance.** The control is **present in the view layer and absent at write** — a different finding with a different remedy. The package's wording is corrected |
| `MCCX-2`: config-key population is **7**, not 6, and *"zero `set_param` sites"* is contradicted | **ACCEPTED IN FULL — see §7.** The seventh key is a test-support key, so the **material** population remains 6 with 3 material; **the claim as this round wrote it is contradicted** |
| `MCCX-1`: `BW-31` (the v19 aggregator) | **The panel declined to test it** and returned `UNKNOWN`, stating it did not open the v19 trees. `MCCX-3` did test it and confirmed it. **Recorded so that the confirmation is attributed to the panel that performed it** |
| `MCCX-6`: veto criterion (d) is met on its face for `BW-35` | **The panel declined the veto and stated its reason.** This session **accepts the decline and the condition attached to it** |
| `MCCX-4`: the state-control surface floor of ~165 shipped objects | **ACCEPTED AS A FLOOR, NOT A DENOMINATOR** — the panel itself declares four untested false-negative modes and classes its completeness `UNKNOWN`. Recorded at that strength |

---

## 7. The finding this round must record against itself

### `J-16` — `GB-06` was live inside the package that declares `GB-06`'s remedy exercised. `MCCX-6`.

The `MCU-15` closure was appended to two files and **not propagated to three others**. At the moment
the audit panel read the package it simultaneously published:

- *"Gating-unknown closure — **8 of 17**"* in two files, and *"**9 of 17 (52.9%)**"* in a third;
- *"floor **35** cases"* and *"floor **36** cases"* **in the same file**;
- *"`MCU-15` — **STILL ZERO AND STILL NEVER SEARCHED**, class `C`"* in one section and
  *"`MCU-15` closes"* in another section of the same file;
- *"`REMAINS GATING — HOLD`"* and *"`CLOSED — VERIFIED DEFECT`"* for one id in one register.

> **The master reconciliation states that the correction channel "now exists and was demonstrated".
> The channel demonstrably did not carry this round's own last correction, made by this round, hours
> after the channel was specified.**
>
> This is accepted without qualification. It is the strongest single piece of evidence in the package
> for its own conclusion: **`ER-CORE-3` is a rule that has to be executed by a mechanism, not by an
> intention.** An author who has just written the propagation rule, and who is propagating their own
> correction, still failed to propagate it — because propagation was a habit and not a step.
>
> **`GB-06` therefore closes no further than the parent round left it, and the remedy proposed in
> `MCC_K` §4 must be re-specified as a mechanical check, not an authoring rule.** See §8.

### `J-17` — the package mutated during independent review. `MCCX-6`.

The panel enumerated 9 files at the start of its review and 20 at the end; two files grew and four
appeared. **No reviewer verdict on a package can be relied on without a content hash.**
Accepted, and acted on: the gate report records the package state by **roll-up digest**, and the
evidence manifest carries a per-file digest.

---

## 8. Consolidated challenge position

| Measure | Result |
|---|---|
| Perspectives | 6, in 2 disjoint panels, none an author |
| Package conclusions **invalidated** | **3** (`J-01`, `J-02`, `J-03`) |
| Package counts **corrected** | **4** (`J-C1` … `J-C4`) |
| **New findings accepted**, verified at source | **12** (`J-04` … `J-15`) |
| … of them **tolerance-zero severity** | **5** — `J-05`, `J-06`, `J-08`, `J-10`, and `J-07` |
| Package claims **independently confirmed** | **8** — the branch-currency structural argument; the undated earliest-rate fallback; the 2010-dated seeding counts; cross-branch settlement in full; the raw-SQL **statement** absence, on an independent method across every root; the hierarchy-immutability block; the client-side-only nature of readonly; and cross-version instability, reproduced verbatim |
| **Vetoes issued** | **0** — with one condition attached to `J-C4`, accepted and carried into the gate report |
| Panel gate recommendation | **`HOLD`**, reached independently by both panels |

### The audit panel's own summary, accepted verbatim in substance

> *The package's evidence base is sound where it could be reached; every Layer-2 citation re-read
> verified at `file:line`; and its two most consequential findings reproduce independently. Its defects
> are of one kind, and it is the kind the package itself names:* **the population, the path set and the
> unit are still being chosen by the author of the claim they bound.**

---

## 9. What the challenge changes in the gate position

1. **The tolerance-zero count moves 10 → 12**, and one of the two new boundaries is the first
   **`unbalanced-and-posted`** finding in the programme. **None of the twelve is resolved.**
2. **`MCU-04` becomes closable as a verified defect** rather than a deferred tenant question — a real
   closure this round left on the table, recovered by the challenge.
3. **`GB-01` should carry an enumerated seven-row consequence table** rather than a general statement,
   so the Boss decision is made against a list.
4. **`GB-06` does not improve.** The channel failed on this round's own last correction.
5. **The Thai deployment risk is re-pointed**: the unsearched-tree finding is materially *smaller* for
   Thailand than this round stated, and a **statutory filing defect inside the deployed Thai
   localisation** is materially *larger* than anything this round found there.
6. **`FX-08`'s disposition is unchanged and better evidenced.** Two panels reached it independently.

---

> ### FIGURE-GOVERNANCE NOTICE — appended mechanically, package-wide
>
> **`MCC_00_CANONICAL_FIGURES_REGISTER.md` governs every published figure and disposition in this
> package.** Where a figure in this file differs from a row in `MCC_00`, **`MCC_00` governs**; the text
> here stands unedited so the lineage is visible (`DR-NC-06`).
>
> This notice was appended to **every** Layer-1 file by one command, after the independent audit panel
> found that this round had failed to propagate its own last correction to three of its own files
> (`MCC_J` `J-16`). It is the mechanism, not the intention, that `ER-CORE-3` requires.
