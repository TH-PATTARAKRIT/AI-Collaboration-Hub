# 28 — BUSINESS SEMANTIC CLOSURE REGISTER

# `16 SEMANTICS · DETERMINED · UNSPECIFIED · INTERNALLY CONTROLLABLE · WAS 9`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Authority: `§18` of the ruling prompt · Boss: **SOLE FINAL APPROVER**

> **`§18`: *"Close autonomously everything below Boss/external authority."* `§31`: *"DO NOT … enter
> Functional Design."*** Both are obeyed, and §1 explains why they do not conflict.

---

## 1. THE DISTINCTION THAT GOVERNS THIS FILE — corrected before publication

**My first draft of this section argued that specifying these semantics at Pre-Test would *invert the
gate*, because specification is Functional Design's act. That is wrong, and the corpus contains its own
counter-example.**

> **`CORE-05` was **SPECIFIED inside the Pre-Test arc, by SMEs Core** — `32A_`, the deterministic
> `KIND × CATEGORY` refusal rule: `6` codes, a total decision procedure, `0` silent fallbacks.**
> Its own scope line reads: *"a **specification**, within SMEs Core authority, of an obligation a Boss
> ruling created. **It elects nothing. `0` Boss items arise.**"*

**So the true position is three-way, not two-way:**

| | **(a) DETERMINE the gap** | **(b) SPECIFY the semantic** | **(c) DESIGN the solution** |
|---|---|---|---|
| The act | name it, own it, phase it, give it a closure criterion | state the business rule, from existing authority | screens, flows, data model |
| Whose authority | **Pre-Test / audit** | **SMEs Core** — precedent `32A_` | **Functional Design** |
| Available at this gate? | **YES — and it is this session's job** | **YES — but it is a design act, not an audit act** | **NO** |
| Done here? | **YES, all `16`** | **NO — see below** | **NO** |

**Why (b) is not performed in this session, stated plainly rather than dressed up as a gate rule:**

1. **This is a remediation and audit session.** Writing `16` business specifications is a **design wave**
   with different authority, different inputs and different review. Producing them inside an audit
   package would be **exactly the invention `§31` prohibits** — an auditor specifying the thing it is
   auditing.
2. **Several are not pure determinations.** `BS-15` carries an election `32A_` itself routes to *"Boss or
   Functional Design"*; `BS-04`, `BS-12` and `BS-14` require **creating objects**, not deriving rules
   from existing authority as `32A_` did.
3. **`§28` cuts both ways.** It forbids escalating what SMEs Core can resolve — **and these are for SMEs
   Core to resolve, in an SMEs Core session.**

> **Consequence for the terminal state, and it is the important one:** the `16` are
> **INTERNALLY CONTROLLABLE AND NOT CLOSED**. Under `§25` criterion `9` they **block independent-rerun
> eligibility**. **The next act is an SMEs Core specification wave — not a Boss decision, and not the
> independent rerun.** (`32_` §4.)

## 2. THE `16`

| ID | Question a designer would otherwise have to answer by invention | Module | Boundary | Business rule required | Authority | SMEs Core? | Arch.? | AAS+? | Stat.? | Boss? | Evidence | **(b) status** |
|---|---|---|---|---|---|:-:|:-:|:-:|:-:|:-:|---|---|
| **`BS-01`** | Who consumes the remaining-supply record, what originates the orphan input, and what route carries **Asset → Equipment**? | Sales, Asset | `BC-09` | a named consumer for each output and a named producer for each input | `PT-04`, `B10′` | **Y** | Y | — | — | — | `10_` §2 #1; `XMC-H-09` *"the Equipment consumer has no evidenced route"* | **DETERMINED** |
| **`BS-02`** | How does a correction reference **what it corrects**? | Accounting | `BC-05` | a corrected-entry link with identity and direction | `O-1` | **Y** | — | — | — | — | `10_` §2 #2; `X-11`: *"only correction route is a return; corrected-entry link **does not exist**"* | **DETERMINED** |
| **`BS-03`** | What happens when a **consumed** fact is reversed? | Accounting, Inventory | `BC-05`, `BC-13` | reversal semantics after downstream consumption | `O-3` | **Y** | Y | — | — | — | `10_` §2 #3 | **DETERMINED** |
| **`BS-04`** | What **is** an accounting period — its identity, states, and a lock the accounting date cannot pass? | Accounting | **`BC-12`** | an accounting-period object | `XMC-H-12`; `17_` §2.4 | **Y** | **Y** | — | — | — | *"**There is no accounting-period object**"*; date *"silently movable past a lock"*; producer *"waiting for a lock source with no object behind it"* | **DETERMINED** |
| **`BS-05`** | **What makes two executions of a migration batch the same execution?** (`MF03-MS-01`) | Migration | `BC-16` | **element `15` — the Idempotency Identity** | `X-22`; `CORR1-F-03` | **Y** | — | — | — | — | `25_` §6. **Decides `MF-03`'s classification in either direction** | **DETERMINED** |
| **`BS-06`** | How does a migrated opening balance carry **`FIFO` layers**? | Migration, Inventory | `BC-16`, `BC-05` | `HX-24` payload carrying `(quantity, unit cost, acquisition sequence)` per layer | `CORE-07` / `CORR1-F-02` | **Y** | — | — | — | — | `29_`§3 of `CORR1`: *"an aggregate cannot reconstruct layers: **infinitely many layer sets share one total**"* | **DETERMINED** |
| **`BS-07`** | How is a **goods receipt matched to its bill at line level**? | Purchase, Inventory, Accounting | **`BC-17`** | a receipt↔bill matching identity | `X-01` | **Y** | Y | — | — | — | `X-01`: *"the goods-received bridge is a **swept suspense account, not item-matched**"* | **DETERMINED** |
| **`BS-08`** | What guarantees internal-transfer neutrality, and **what detects its loss**? | Inventory | `XMC-H-15`/`-16` | valuation-account mapping semantics **+ an independent check** | `SA06-F-05` | **Y** | **Y** | — | — | — | *"protected only by configuration; **no independent check exists**"*; `R4-F-18` | **DETERMINED** |
| **`BS-09`** | What **is** the demand-approval gate, and why may a system-raised document bypass it? | Purchase | `BC-03` | the approval mechanism and its bypass rule | `XMC-H-03` | **Y** | Y | — | — | — | *"the write **bypasses the demand-approval gate** every human-raised purchase must pass"*; `X-12`: *"approval mechanism absent"* | **DETERMINED** |
| **`BS-10`** | What may reduce or release a **reservation**, and what records it? | Inventory | `BC-01`, `BC-13` | reservation lifecycle semantics | `X-12` | **Y** | — | — | — | — | *"an adjustment can **silently reduce a reservation**"* | **DETERMINED** |
| **`BS-11`** | What rule decides **make** vs buy vs dropship? | Sales, Manufacturing, Purchase | `BC-02`, `BC-03` | the Supply Nature resolution rule | `ND-01` | **Y** | — | — | — | — | *"the Supply Nature rule deciding **make** is itself **undetermined**"*; `ND-01` **rejects** routing by product configuration and document type, with no replacement stated | **DETERMINED** |
| **`BS-12`** | What **is** a Quality object — identity, states, transitions? | Quality | `BC-14` | the Quality object | `XMC-H-14` | **Y** | Y | — | — | — | *"the **Quality object itself is absent** — `0` blobs, two shapes, firing positive controls"* | **DETERMINED** |
| **`BS-13`** | What event records **service performance**, and how does one duration become costed rows? | Service / Project | `BC-15` | a performance event record; a deterministic cost-row derivation | `XMC-H-17` | **Y** | Y | — | — | — | *"no physical fact, only an assertion, with no event record"*; *"**three costed rows from one duration**, with two report surfaces reading different row sets"* | **DETERMINED** |
| **`BS-14`** | What **is** tenant / company isolation — element `10`? | Architecture | `X-15` | the isolation semantic and its `8` proofs | `SA17` §2b | **Y** | **Y** | — | — | — | *"this scenario **is** element `10`; `0 of 8` isolation proofs; **two** lock-defeat paths, the second leaving no record"* | **DETERMINED** |
| **`BS-15`** | Is a **Consumable** expensed at **receipt** or at **issue**? | Inventory | `BC-05` | the expensing point | `32A_` §3 | **Y** | — | — | — | (Y) | `32A_` states its own dependency: *"**If Boss or Functional Design later determines** … it carries a pool until issue and **this row changes to all `PROCEED`**"* | **DETERMINED** |
| **`BS-16`** | Is the product **standard cost** established independently of the migration? | Inventory, Migration | `BC-16` | the standard-cost origin at cutover | `BD-ACC-03B` | **Y** | — | — | — | — | `CORR2-MF-02`: *"in a cutover the standard cost is **itself migrated data**"* — stated, never tested | **DETERMINED** |

**`16` semantics · `16` determined · `0` specified · `0` invented.**

---

## 3. WHY THE COUNT ROSE FROM `9` TO `16`

**None of the `7` new entries is a new defect. All `7` existed and were not visible as semantics.**

| New | Where it was hiding |
|---|---|
| `BS-07` receipt↔bill matching | inside scenario `X-01`, never registered as an FD blocker |
| `BS-08` neutrality + independent check | inside the `XMC-H-15`/`-16` `N/A`, which `BOSS-CORR1-01` §2.3 forced open |
| `BS-09` approval gate | inside `XMC-H-03`'s *"control breach"*, treated as a boundary gap |
| `BS-10` reservation lifecycle | inside `X-12`, treated as an adjustment defect |
| `BS-11` Supply Nature *make* rule | inside `XMC-H-02`, treated as a routing gap |
| `BS-12` Quality object | inside `XMC-H-14`, outside the declared `12` until the ruling brought it in |
| `BS-13` service event record | inside `XMC-H-17`, outside the declared `12` until the ruling brought it in |
| `BS-15` Consumable expensing point | inside `32A_`'s own declared basis |
| `BS-16` standard-cost independence | inside `CORR2-MF-02`, raised and never measured |

> **`CORR2-BSC-01` — MATERIAL. Declaring the configuration and optional-function populations, and
> widening the boundary set, did not create gaps — it made `7` existing ones countable.**
> `23_` §4 predicted this: *"all `7` would still be incomplete if the function were mandatory."*
> **The correct reading of `9 → 16` is that the earlier `9` was an undercount produced by dimensions
> that were not being measured.**

---

## 4. WHAT IS **NOT** A BUSINESS SEMANTIC — the `4` authority blocks

**Separated, because they are not closable by design work at any gate.**

| ID | Item | Owner | Why not a semantic |
|---|---|---|---|
| `FD-17` | **`SC-SMT-01`** — reconciliation control for the `Average` return-reversal residual | **BOSS** | `SC-03` classifies it **`BOSS-ONLY DECISION`**; a designer may not elect it. **Not re-asked** (`§20`) |
| `FD-18` | **`CORE-03`** — veto limb-`2` re-wording | **AAS+ issuer, EXTERNAL** | only the issuer may author it; `0` AAS+-authored records exist |
| `FD-19` | **Tax substitution rule base** | **Thai statutory, EXTERNAL** | *"a **black box** in this evidence set"*; **no statutory claim may be invented** |
| `FD-20` | **Fixed-overhead normal-capacity register** + **`POH-D-02`** | **BOSS + Thai statutory** | *"a dated normal-capacity register per machine is a required object that **does not exist**"*; `POH-D-02` **withheld pending statutory evidence** |

---

## 5. THE CONTROLLING QUESTION

> ## **CAN FUNCTIONAL DESIGN BEGIN WITHOUT INVENTING MISSING BUSINESS SEMANTICS?**
>
> # `NO`

**`16` semantics would have to be invented — up from `9`.** `§10` item `8` and `§9` item `D` both
forbid handoff while any remains.

**And `4` of the `16` are structural rather than detailed** — `BS-04` (there is no accounting-period
object), `BS-12` (there is no Quality object), `BS-14` (there is no isolation semantic) and `BS-05`
(there is no idempotency identity) are **missing objects**, not missing rules. **A designer cannot
route around a missing object.**

---

## 6. CLOSURE CRITERIA — what each will look like when closed

| ID | Closed when |
|---|---|
| `BS-01` | every output names a consumer and every input names a producer, in a register, with `0` orphans |
| `BS-02` | a correction carries an identifier resolving to what it corrects, and the link is queryable |
| `BS-03` | reversal-after-consumption has a defined outcome for each consuming boundary |
| `BS-04` | an accounting-period object exists with identity, states and a lock, **and no posting path can date past it** |
| `BS-05` | an idempotency identity is defined such that a replayed batch is recognised; **`MF-03` then classifies in one direction or the other** |
| `BS-06` | `HX-24`'s payload carries layers, **or** `FIFO` categories are ruled out of migration scope |
| `BS-07` | a receipt line and a bill line share a matching identity; the suspense bridge is item-matched |
| `BS-08` | the neutrality rule is specified **and** an independent check exists that fires when it is defeated |
| `BS-09` | the approval gate is specified and every entry path is shown to pass it or to be an evidenced exception |
| `BS-10` | reservation reduction and release are enumerated acts, each recorded |
| `BS-11` | the *make* decision has a stated rule with retained inputs, per `ND-01` |
| `BS-12` | a Quality object exists with identity, states and transitions |
| `BS-13` | a service performance event exists; one duration derives a deterministic set of cost rows read identically by every surface |
| `BS-14` | element `10` is specified and `8 of 8` isolation proofs are stated as testable propositions |
| `BS-15` | the Consumable expensing point is determined; `32A_`'s Consumable row is re-derived |
| `BS-16` | the standard-cost origin at cutover is stated and the `Standard` asymmetry is tested against it |

---

## 7. CHECKPOINT

> **`16` business semantics enumerated, each with module, boundary, authority, owner, evidence and a
> closure criterion · **determination DISCHARGED on all `16`; specification OPEN on all `16`** ·
> **§1 corrected before publication — `32A_` proves SMEs Core CAN specify inside Pre-Test, so these are
> internally controllable, not gate-blocked** · **`0` semantics invented here** ·
> count rose `9 → 16`, and **`CORR2-BSC-01`: all `7` additions were pre-existing gaps made countable**,
> not new defects · `4` authority blocks separated as not-semantics ·
> **`4` of the `16` are missing OBJECTS, not missing rules** ·
> **FUNCTIONAL DESIGN CANNOT BEGIN.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the SOLE FINAL APPROVER.**
