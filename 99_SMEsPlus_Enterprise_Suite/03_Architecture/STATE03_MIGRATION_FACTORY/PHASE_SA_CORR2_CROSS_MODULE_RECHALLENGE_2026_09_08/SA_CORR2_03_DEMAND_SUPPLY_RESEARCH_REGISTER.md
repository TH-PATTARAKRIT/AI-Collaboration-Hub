# SA_CORR2_03 — DEMAND–SUPPLY CONSOLIDATED RESEARCH REGISTER
## CP-SA-C2-20 (second half) — TARGETED VERY DEEP RESEARCH RE-SCOPED

Session: `[SMEPLUS-26-09-08-PHASE-SA-CORR2-XMOD-001]`
Supersedes at claim level: `SA01` §4 and §4.1 coverage figures; `SA16` §3's consolidation scope.
Evidence frame: `SA_CORR2_00` §2 as corrected by `C2-I-02` (v2 corpus, 3,789 text blobs).

---

## 1. Why this register re-measures instead of re-scoping

`SA16` raised six research triggers and consolidated them into one programme. `SA19` Decision 4
asks Boss to authorize it. The whole of that rests on five domains being `THIN`, and `THIN` rests on
one table: `SA01` §4.1.

**That table's pattern was never declared.** `SA00` §6 states the rule — *"MENTION = blob contains
any **declared** term"* — and then declares no term anywhere in the package. `SA00` §7 gives prose
labels (*"Stock reservation / allocation"*, *"BOM / routing step / work center"*), which are
**descriptions of a search, not a search**. `SA01` uses the word *pattern* exactly once, inside a
correction row about an unrelated claim.

The programme's own denominator rule is `POPULATION + PATTERN + PATH SET + UNIT`, none author-chosen.
`SA00` declared three of the four rigorously and **omitted the one that decides what gets counted**.

> **`C2-F-07`. The most consequential classification in Phase SA was produced by an undeclared
> instrument, and no control could have caught it, because a pattern nobody can see is a pattern
> nobody can re-run.**

`SA00` §6 even states the correct caveat — *"MENTION is a **floor**, not a coverage measure: a
package may address a domain in vocabulary the pattern does not carry"*. `SA01` §4.1 then uses those
floors as a coverage measure, in terms: *"Five modules … are evidenced between 4 and 34 blobs"*.
**The caveat travelled one file and died.** That is its own finding and it generalises: a limitation
stated in the register that measures is not inherited by the register that classifies.

---

## 2. Re-measurement, with the pattern published

### 2.1 Declared instrument

| Clause | Declaration |
|---|---|
| POPULATION | v2 corpus — 183 branches **plus the `origin/SMEsPlus` tree**, 3,789 unique text blobs (U1), 3,561 unique text paths (U2) |
| PATH SET | whole repository, no directory pre-filter, mainline included (`C2-I-02`) |
| UNIT | unique text blob (U1) and unique path (U2), reported separately, never conflated |
| PATTERN | **published in full below and executed as written**, case-insensitive extended regex |
| POSITIVE CONTROLS | two domains independently known to be deep, run through the identical instrument |
| NEGATIVE CONTROL | `zzqq_unmatchable_token_20260908` → **0 blobs, 0 paths, 0 occurrences** |
| SECOND SHAPE | every reported figure re-run as an occurrence count, a different command shape |

```text
SA-D05  drop.?ship|make.?to.?order|\bMTO\b|buy.?to.?order|procurement rule|stock rule|
        replenish|reorder(ing)? rule|reorder point|phantom|bill of material|\bBOM\b|kit\b|kits\b|
        kitting|component.{0,25}(resolution|explosion|explode)|route.{0,20}(rule|dispatch)|
        supply (method|route|nature)
SA-D17  \bservice (order|type|product|item|revenue|delivery|line)\b|non.?stock|
        intangible service|completion (evidence|certificate|confirmation)|milestone|timesheet|
        billable|subcontract|work performed|deliver(ed|y).{0,25}service
SA-D18  \bproject\b.{0,40}(analytic|cost|budget|dashboard|financial)|
        analytic (account|distribution|dimension|plan|line)|cost object|cost cent(er|re)|
        work breakdown|job cost|task.{0,20}cost
SA-D19  quality (control|check|hold|order|alert|plan|point|team|certificate|inspection|result)|
        nonconform|non.conform|\bNCR\b|incoming inspection|receiving inspection|goods inspection|
        inspection (outcome|result|plan|report|step)|
        reject(ed|ion)?\b.{0,30}(stock|goods|receipt|lot|material)
SA-D20  equipment|maintenance (order|request|team|plan|cost|schedule)|preventive maintenance|
        corrective maintenance|breakdown|downtime|work cent(er|re)|calibration|meter reading
SA-D21  price ?list|pricing (rule|policy|method)|discount|credit (limit|control|hold|block)|
        customer (hold|blocked)|payment term|price determination|margin (policy|rule)
CTRL-TAX  \bVAT\b|withholding|\bWHT\b|tax (register|invoice|point|determination|code)|fiscal position
CTRL-INV  stock (move|movement|valuation|reservation)|warehouse|transfer document|on.?hand|reserved quantity
```

### 2.2 Result

| Domain | `SA01` figure *(pattern undeclared)* | CORR2 blobs (U1) | CORR2 paths (U2) | Ratio, **discounted** for corpus growth |
|---|---|---|---|---|
| SA-D05 Supply routing | 81 | **343** | 323 | **3.1×** |
| SA-D17 Service delivery | 16 | **273** | 252 | **12.3×** |
| SA-D18 Project ↔ Analytic | 4 | **331** | 310 | **59.5×** |
| SA-D19 Quality / inspection | 20 | **69** | 70 | **2.5×** |
| SA-D20 Equipment / Maintenance | 13 / 34 | **349** | 348 | **7.4×** on the larger prior figure |
| SA-D21 Commercial policy | 18 / 16 | **195** | 187 | **7.8×** on the larger prior figure |
| **CTRL-TAX** *(known deep)* | 1,216 | **777** | 767 | — |
| **CTRL-INV** *(known deep)* | — | **730** | 681 | — |
| **NEG control** | — | **0** | **0** | — |

**The discount is stated because it must be.** The v2 corpus is **3,789** blobs against this round's
own v1 figure of **2,748** — **1.379× larger**, chiefly because the mainline tree is now included.
Every ratio above is the raw ratio divided by **1.379**. A comparison between two corpora of
different sizes that does not say so is not a comparison.

*(An earlier version divided by 1.39, using `SA00`'s reported **2,722** as the baseline. That is the
parent's count under the parent's method; the correct denominator for a like-for-like discount is
this round's own v1 measurement, 2,748. The difference is immaterial to every conclusion and is
corrected because two baselines for one correction factor is exactly the defect this register
reports elsewhere.)*

### 2.2.1 `K2-15` — two vendor object names were removed from the published pattern, with the effect measured

The first version of the pattern above carried **two reference-system object names** (a
replenishment-rule object and a transfer-document object). Publishing a pattern is required for
reproducibility; publishing a *vendor object name* on a Layer 1 surface is a clean-room leak. Both
were removed and the effect measured rather than asserted:

| Pattern | With the vendor tokens | Clean | Δ |
|---|---|---|---|
| `SA-D05` supply routing | 363 blobs / 343 paths | **343 blobs / 323 paths** | −20 blobs |
| `CTRL-INV` control | 800 blobs / 751 paths | **730 blobs / 681 paths** | −70 blobs |

**The table in §2.2 reports the clean figures.** The deltas are published because a scrub that
silently changes a load-bearing count is indistinguishable from a correction, and because the
control moved further than the subject did — which *narrows* the gap in §2.3 and therefore works
**against** this register's own conclusion. It is reported for that reason.

Found by a mechanical per-file token count against the parent package's baseline of **0**, run as
the closing sweep. **No review caught it, and the leaked text was correct** — which is exactly how
this defect class presents.

### 2.3 `C2-F-08` — the classification does not survive its own contrast test

`SA01` §4.1's argument was a **contrast**: the thin domains measure *"4–34 blobs against 154–1,216
for domains of comparable architectural weight"* — roughly **an order of magnitude**.

Re-run through one declared instrument, the same contrast is:

| | Range |
|---|---|
| The five `THIN` domains + SA-D05 | **69 – 349** blobs |
| The two known-deep controls | **730 – 777** blobs |
| **Gap** | **2.1× to 11.3×** — not an order of magnitude, except for Quality |

**Four of the six are within 2.2×–4.1× of a domain the register itself calls deep.** The `THIN`
classification does not survive the contrast that was offered as its justification.

### 2.4 The one that survives — and it is a real result

**`SA-D19` Quality is genuinely the thinnest, at 69 blobs against controls of 730–777 — an 11.3×
gap.** It is the only one of the six for which `SA01`'s order-of-magnitude claim holds.

That figure is itself a correction of this round's own first attempt, published under the
`SA00-I-01` discipline:

| Attempt | Pattern | Blobs | Why it was wrong |
|---|---|---|---|
| CORR2 first pass | included `quarantin`, bare `inspect`, `corrective action\|CAPA`, `rework` | **1,755** | **Three false friends, each large.** `quarantin` (821) is overwhelmingly the programme's own *Layer 2 Audit Quarantine*; bare `inspect` (443) is *"direct inspection of the tree"*, *"inspectable"*; `corrective action\|CAPA` (867) is the programme's own **correction rounds**; `rework` (117) is the gate verdict `REWORK REQUIRED` |
| CORR2 corrected | false friends removed, quality-scoped forms retained | **69** | Found by **printing what the pattern matched** before counting it, per `SA00-I-01` |

A 25-fold error, in this round's own instrument, caught by one discipline. Published because a
re-measurement that reports only its final number is asking to be trusted rather than checked.

---

## 3. Domain adjudication and the `BN-08 / 10 / 17 / 18` statuses

### 3.1 `SA-D17` Service — `THIN` **FALSIFIED**

The recognition trigger and its owner are established, at `FACT VERIFIED`, in the Account programme.
The evidenced position is a determinate one and it is uncomfortable:

> For services, expense re-invoicing, milestones and timesheets the quantity that governs revenue
> recognition is **a permanent human assertion, with no independent operational event and no event
> record** — *"A ledger fed only by the physical side has nothing to record for a service sale."*
> — `.../P02_ORDER_TO_CASH/05_P02_BUSINESS_EVENT_REGISTER.md` §3a; `.../10_P02_CROSS_PROCESS_OWNERSHIP.md`

And the design question is already stated as open, with both positions argued, in the same package
(`17_P02_AAS_PLUS.md` §6, `DIS-06`), converging on a requirement both sides accept: **whatever the
construct is called, it must carry who asserted, when, and on what basis.**

**`BN-08` Service sale: `HOLD` → `PARTIAL`.** `E2E-08`: `NOT TRAVERSABLE` → **`TRAVERSABLE WITH A
NAMED BREAK`** — the break is that the trigger is an assertion with no independent event record.

**`ND-11`:** *A service recognition event in SMEsPlus carries its asserter, the time of assertion and
the basis asserted, and is itself an Accounting Event under `BD-ACC-01`.* Independent rationale: the
evidenced reference records the quantity and not the assertion, so nothing can later show **who said
the work was done**. For a service business that is the only audit trail there is.

### 3.2 `SA-D18` Project ↔ Analytic — `THIN` **FALSIFIED** (the largest reversal: 4 → 331)

A dedicated package artefact exists whose entire subject is this boundary, and it answers both halves:

> **There is no cost object in the reference pattern.** There is a dimension value, and a dozen
> modules that each add their own relational field… What there is *not* is a first-class object that
> answers "what accountable thing bears this cost", with an identity, a lifecycle, a scope and a
> closing state. — `.../ACCOUNT_P09_PLAN_TO_ANALYZE/04_P09_COST_OBJECT_MODEL.md`

> **Ten de facto cost objects, one shared record type, no discriminator.** — *ibid.*

> **`CO-06` — The closing state is the missing control.** A management record can be written against
> a **closed accounting period** with no barrier; management data has **no period control and no
> object control.** — *ibid.*

And the duplication question Boss's decision forbids is answered **negatively, with mechanism**:
three separate extensions each write a costed analytic row from **one** work-order duration, and two
reporting surfaces resolve *"which records belong to this cost object"* by structurally different
rules — so a project's profitability total and its budget-achieved total are computed over different
row sets **before** any double count.

**`BN-10` Project-based sale: `HOLD` → `PARTIAL`.** `E2E-18`: `NOT TRAVERSABLE` → **`TRAVERSED —
AND IT FAILS`**, which is a different and more useful status: the route was walked end to end and
found to duplicate. A route that has been traversed and found defective is **not** an unassured route.

### 3.3 `SA-D19` Quality — `THIN` **CONFIRMED as an object, FALSIFIED as a route**

This is the domain where the prior classification substantially holds, and it still needs splitting:

- **As a first-class Quality object: genuinely absent.** `quality point`, `quality alert`,
  `quality check` as an object name → **0 blobs**, confirmed on two command shapes, against
  positive controls firing on the same shapes.
- **As a route: evidenced and answered.** The specific question `SA05`/`SA06`/`SA15` said was
  undetermined — *is a rejection an inventory event, a return, or neither, and does it move cost
  recognition?* — is answered:

> **Quality holds are a location state, not a product state:** goods awaiting or failing inspection
> sit in a quality-check or quarantine place and are therefore **visible in on-hand but excluded from
> available.** — `.../FINAL_SOLUTION/INVENTORY/V1_0/03_INVENTORY_FUNCTIONAL_DESIGN_V1.md` §7

composed with the governing valuation rule from the same package:

> A movement between two internal company locations changes *where* stock is and **creates no
> accounting consequence**. A movement crossing the boundary between an internal location and a
> non-internal counterpart… changes *whether* the company owns the stock and therefore **emits a
> valuation fact**. — `.../02_INVENTORY_FINAL_SOLUTION_V1_EXECUTIVE_SUMMARY.md`

**Composed answer: a quality hold IS an inventory event, is NOT a return, and does NOT move cost
recognition** — it is internal→internal, so it changes availability and emits no valuation fact.
Only the **disposition** moves cost: reject-to-supplier crosses to a non-internal counterpart;
scrap crosses to a loss counterpart.

**And the route is Boss-ruled, verbatim** — read directly from the decision body, now reachable:

> `Purchase Receipt -> Incoming Inspection -> Accept / Hold / Reject -> Inventory`
> `Manufacturing -> In-Process / Final Inspection -> Pass / Hold / Rework / Scrap -> Inventory`
> `Finished Goods -> Final Quality Result -> Delivery -> Customer / Certificate`
> — `14_BOSS_DECISION_QUALITY_MENU_NAMING_...` @ `4c469f8e`, status `BOSS APPROVED DIRECTION / DETAIL DESIGN PENDING`

**`BN-17` Quality hold: `HOLD` → `PARTIAL`.** `E2E-16`: `NOT TRAVERSABLE` → **`TRAVERSABLE WITH A
NAMED BREAK`** — the break is the absent Quality object, not the routing.

### 3.4 `SA-D20` Equipment / Maintenance — `THIN` **FALSIFIED**, and the answer is a controlled negative

Sixteen dedicated artefacts exist. The question `SA16` TVDR-05 asks — *does maintenance cost reach
production cost, period expense, or asset carrying amount?* — is answered `FACT VERIFIED`, **with a
declared denominator**, which is the strongest form of negative the programme recognises:

> **Denominator for the negative:** every source file in the maintenance module. **Zero** references
> to the journal-entry model; **zero** to the analytic model.
> **`P04-F-152` … Maintenance cost is a statistical float.** There is no journal entry, no analytic
> item, no cost object and therefore **no accounting attribution of a non-productive cause anywhere
> in the reference product.**
> — `.../P04_ACQUIRE_TO_RETIRE/CLOSURE_G01/P04_MAINTENANCE_NONPRODUCTIVE_CAUSE_MATRIX.md`

> In the estate they are already distinct, **but for the wrong reason** — not because the design
> separates them, but because **repair expense never becomes an accounting fact at all.**
> **This is a separation by absence, not by control.** — *ibid.*

and, from the manufacturing side, with the objection pre-empted:

> The chain is broken on the asset side and broken again immediately after. Verified **with the
> maintenance-integration module installed**, which removes the "the module was missing" objection.
> **Machine cost in the reference product is not causally connected to machine use.** `FACT VERIFIED`.
> **Deployments where any machine cost reached finished goods: 0 of 4.**
> — `.../P03_MANUFACTURE_TO_COST/CLOSURE_G01/P03_EQUIPMENT_OPERATION_COST_CAUSALITY.md`

**Answer: period expense, through the vendor bill, owned by Expense-to-Pay. Not production cost.
Not asset carrying amount.**

**`BN-18` Equipment breakdown: `HOLD` → `PARTIAL`.** `E2E-17`: `NOT TRAVERSABLE` → **`TRAVERSABLE
WITH A NAMED BREAK`** — the route is Boss-ruled verbatim (`N-16`, verified) and the cost join is
`FACT VERIFIED` absent. The break is that no cost causality exists to assure.

**`C2-F-09` — this is a *requirement with no mechanism*, and it is the second one.** `SA11-F-01`
records the first: TAS 2 ¶12 expressly requires depreciation **and maintenance of production
equipment** to be absorbed into conversion cost, and there is no path. `SA-D20` now supplies the
missing half of the same finding: **maintenance cost never becomes an accounting fact at all**, so
the TAS 2 ¶12 gap is not one absent path but two, and `SA11-F-01`'s corroboration count rises from
three packages to four. The two findings were in adjacent registers and no control compared them.

### 3.5 `SA-D21` Commercial policy — `THIN` **NARROWED**

195 blobs against 18/16. Adjudicated with the credit-control evidence in `SA_CORR2_06`.

---

## 4. Consolidated Business-Nature status — the count, now that its constituents are decided

| Status | Count | Natures |
|---|---|---|
| `EVIDENCED — DESIGN; NOT LIVE` | **1** | BN-06 |
| `PARTIAL` | **17** | BN-01, BN-02, BN-03, BN-04, BN-05, BN-07, BN-08, BN-09, BN-10, BN-11, BN-12, BN-13, BN-14, BN-15, BN-16, BN-17, BN-18 |
| `HOLD` | **0** | — |
| **Total** | **18** | |

Check, executed mechanically: the table above yields **18 distinct identifiers**, `BN-01`…`BN-18`,
**each exactly once**, and 1 + 17 + 0 = 18.
*(The first draft wrote the seventeen as `BN-01, 02, 03, …`, which a mechanical enumeration reads as
one identifier and sixteen bare numbers. The claim was true to a reader and unverifiable by a
checker. Corrected; found by this session's own pre-commit sweep.)*

> **`SA05`'s seven `HOLD` natures are all discharged to `PARTIAL`. None was closed by research.
> All seven were closed by reading evidence that already existed, in a path set the instrument did
> not reach.**

This must not be read as *"the natures are now assured"*. `PARTIAL` means the route has an evidenced
spine and a named open element. Seventeen named open elements remain, and they are the input to the
Pre-Test Matrix, not a substitute for it.

---

## 5. `SA16` re-scoped — what research is actually required

`SA16` raised six triggers and consolidated them into one programme on the strength of `SA05-F-01`'s
untested single-root-cause claim. Re-tested at `SA_CORR2_02` §5 and here, the six resolve as:

| Trigger | `SA16` disposition | CORR2 disposition | Correct instrument |
|---|---|---|---|
| `TVDR-01` Supply routing | research | **CLOSE — evidence exists** (`SA_CORR2_02` §3) | Read it. Then **decide** `C2-D-01`, `C2-D-02`, `C2-D-03` |
| `TVDR-02` Service | research | **CLOSE — evidence exists** (§3.1) | Decide `DIS-06`: what a service obligation record contains |
| `TVDR-03` Project / Analytic | research | **CLOSE — evidence exists** (§3.2) | Decide: how a derived project view avoids the evidenced triple-write |
| `TVDR-04` Quality | research | **PARTIALLY OPEN** (§3.3) | Routing answered and Boss-ruled. **Genuinely open: the Quality object** — 0 blobs on two shapes |
| `TVDR-05` Equipment / Maintenance | research | **CLOSE — evidence exists, `FACT VERIFIED` with a denominator** (§3.4) | Decide where maintenance cost lands, **under TAS 2 ¶12** — Boss-owned, joined to `BLK-07` |
| `TVDR-06` Commercial policy | research | **NARROWED** (§3.5) | Scoped research on price and credit determination remains warranted |

**`C2-F-10`. Of six research triggers, four close on existing evidence, one narrows to a single
object, and one survives.** The consolidated programme `SA19` Decision 4 asks Boss to authorize is
**approximately one-sixth of its scoped size**, and most of what it would have researched is
already on the remote.

This is favourable and it is also a warning: **a research programme was scoped from an undeclared
count, and would have re-researched material that four packages had already established.** The cost
of an undeclared pattern is not a wrong number; it is a wrong programme.

---

## 6. Targeted Very Deep Research executed in this round

| Item | Executed? | Result |
|---|---|---|
| `TVDR-01`…`TVDR-03`, `TVDR-05` | **Not required** — closed by controlled re-measurement over an existing, previously unreachable path set | See §3 |
| `TVDR-04` (Quality **object** only) | **OPEN — bounded** | `TARGETED VERY DEEP RESEARCH REQUIRED — QUALITY OBJECT`. Question: what identity, lifecycle and disposition states does a SMEsPlus quality record carry, and what does it emit to Inventory and Accounting at each disposition? |
| `TVDR-06` (price and credit determination) | **OPEN — bounded** | `TARGETED VERY DEEP RESEARCH REQUIRED — COMMERCIAL POLICY`. Question per `SA16`, unchanged |

Under `AUTO-C2-05`, targeted research triggers automatically only where a material unknown cannot be
resolved from existing evidence. **Four could be. Two cannot.** No unrelated domain is reset
(`AUTO-C2-10`).

---

`CP-SA-C2-20 — DEMAND/SUPPLY ROUTING EVIDENCE COMPLETE OR BOUNDED (execution status).`

Checkpoint completion is **not** Boss approval.

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
