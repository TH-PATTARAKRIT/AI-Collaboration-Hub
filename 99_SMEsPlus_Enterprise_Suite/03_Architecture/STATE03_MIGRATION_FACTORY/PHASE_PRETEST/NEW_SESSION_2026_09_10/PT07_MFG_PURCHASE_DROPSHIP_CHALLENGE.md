# PT-07 — MANUFACTURING / PURCHASE / DROPSHIP CHALLENGE

## `CP-PT-07 — SUPPLY ROUTING CHALLENGED`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]`
Branch: `architecture/account-phase-pretest-new-session-2026-09-10-001` · head consumed `5b3ebb44`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **The manufacturing veto is NOT lifted. `E2E-04` is NOT TRAVERSABLE. `0` vetoes discharged.**

---

## 1. Result

| | |
|---|---|
| Supply routes challenged | **Manufacturing · Purchase · Dropship · Make-or-buy · MTO** |
| **Material findings** | **`3`** — `PT07-F-01`, `-F-02`, `-F-03` |
| **`PT07-F-01`** | **the standing manufacturing veto is absent from the veto register's population of `6`** |
| `E2E-04` shortage→supply hop | **UNROUTED — structural, not an election** |
| Fixed-overhead injection path | **NONE** (`R-22 GAP`) |
| Manufacturing variance mechanisms recognised | **`1 of 9`** |
| Dropship | **Boss-ruled `SC-BD-08` option (a)** — no route-specific exception; `F3` leaves the decision list |
| Purchase control floor | **the cross-module entry sits BENEATH it** (`XMC-H-03`) |
| Vetoes discharged by this checkpoint | **`0`** |

---

## 2. `PT07-F-01` — MATERIAL: a veto that is carried, not lifted, and not in the population of six

### The two statements, both carried in Boss's own authorization

`SC-60`, one sentence, carrying both as **separate** items:

> *"…**six vetoes active and zero discharged**; … **manufacturing veto not lifted**; …"*

### The veto register's population

`SC-04_VETO_AUTHORITY_HANDOFF_REGISTER.md` enumerates the six and declares its exclusions:

| The six | Issuer | Trigger subject |
|---|---|---|
| `AAS-V-01` | AAS+ | handoff element 10 recorded as supplied |
| `CF-V-01` | AAS+ | element 10's **authority** half |
| `RC-V-01` | AAS+/Boss | **implementation start** against the invariant set |
| `AAS-V-03` | AAS+ | a cross-context grant carrying **valuation** content (two limbs: `F6`, `F1` COGS) |
| `CF-V-02` | AAS+ | citing `CF-I-06`/`CF-I-08` as reducing `RC-F-03`/`RC-F-07` |
| `AAS-V-02` | AAS+/Boss | implementation start before `MTI-D-01`/`-02`/`-03` ruled |

**Declared exclusions:** *"`MNT-V-01` is a CORR3 **verdict**, not a veto; `DB-V-01`/`-02` are **substrings**
of `P08` identifiers."*

### The measurement

**UNIT:** one occurrence in `SC-04`. **Positive control:** `AAS-V-01` → **`3`** (the instrument fires).

| Token | Occurrences in the veto register |
|---|---:|
| `BLK-07` | **`0`** |
| `BLK-08` | **`0`** |
| `manufactur` | **`0`** |
| `machine` | **`0`** |

**The canonical veto register contains no reference to the standing manufacturing veto, in any form.**

### What the manufacturing veto actually is

From `SC-19`, at primary text:

- **Two limbs.** Limb 1 = `BLK-07`. **Limb 2** = *"prove exactly one mechanism carries machine cost into
  product cost."*
- **Limb 2 is defective as written:** its own reviewer records that it *"tests for uniqueness where the
  answer is zero"*, so **"it cannot be discharged in either direction as written."**
- **Lifting requires both limbs:** *"Deciding `BLK-07` alone would not lift the veto."*
- **Restating a limb is reserved to the veto's issuer and Boss** — AAS+'s half is **outstanding**.

### The defect

**The veto instrument is neither a member of the population nor a declared exclusion.** `SC-04` accounts
for `MNT-V-01` and `DB-V-01`/`-02` by name and reason; **it does not account for this one at all.**

**And `SC-19` — the file that discusses the manufacturing veto at length — closes with:**

> *"Vetoes remain **6** in force · `0` discharged · `0` self-discharged."*

> **One file describes a seventh standing veto in detail and asserts the count is six, in the same
> document.** Either the count is `7`, or the manufacturing veto is tracked outside the veto system and
> the register's exclusion list is incomplete. **Both readings cannot be true, and neither is written down.**

### Why it is material

**`8C-CLARIFICATION-01` and the Boss authorization both carry `6 vetoes / 0 discharged` as a tolerance-zero
carry-forward.** A carry-forward figure whose population excludes an active, named, unlifted veto **without
saying so** is a denominator defect on a control count — the class the programme has recorded most often.

### Disposition

| | |
|---|---|
| Status | **OPEN — MATERIAL** |
| This session's action | **carries `6` as the ruled/reported figure AND records that the population is not established as complete.** It does **not** renumber to `7` — **re-scoping a veto population is not SMEs Core's act** |
| Owner | **AAS+ (issuer) and Boss (ratifier)** |
| What would close it | the veto register naming the manufacturing veto as a **member** (count → `7`) or as a **declared exclusion with a reason**, on issuer authority |
| Routed to | **`PT-11`**, `PT-13`, **`PT-14` B-7** |

---

## 3. Manufacturing — the routes and what blocks them

### 3.1 `E2E-04` — the one untraversable flow, and why it is not an election

**Route:** Sales → Manufacture → RM shortage → Purchase → Receipt → Production → Delivery.

**The break, at primary text:** the target manufacturing state machine's shortage state *"exits **only on
reservation completing, never on procurement being raised**. **A shortage can therefore be entered and
never left by supply.**"*

**Two clauses, and the second is the structural one:**

| Clause | Nature |
|---|---|
| `C2-D-01` soft-vs-hard fulfiller binding | **Boss election** — ruled at `SC-BD-02`: **`SOFT BINDING CONFIRMED`** |
| **the missing procurement exit** | **A DEFECT, NOT AN ELECTION** — `SC-BD-02` §8.3: *"`C2-D-01`'s shortage-exit half **was a defect, not an election**; SMEs Core specified a supply-raised exit; **that specification stands and is not a Boss item**"* |

**`SC-BD-02` §8.4, binding:** ***"`E2E-04` is NOT re-graded `TRAVERSABLE` by this ruling."***

> **The Boss ruling settled the election half and explicitly declined to move the grade.** A prior round
> re-graded this row by **suppressing the second clause of its own source sentence** and the re-grade was
> withdrawn (`CHF-03`). **This checkpoint does not re-grade it either**, and records that the *specified*
> supply-raised exit is a SMEs Core specification that **exists** while the **target state machine still
> lacks the exit** — i.e. the gap is between specification and the modelled behaviour, not in the
> specification.

### 3.2 Cost accumulation — two named absences

| Obligation | State |
|---|---|
| **Fixed production overhead → product cost** | **`R-22 GAP` — the fixed-overhead elements have NO INJECTION PATH.** Absorption denominator ruled **normal capacity** (`SC-BD-06`), but the **carrier does not exist** |
| **Manufacturing variance** | **NO VARIANCE MECHANISM EXISTS — `1 of 9` variances recognised** |
| **Machine cost → product cost** | **veto limb 2, undischargeable as worded** (§2) |
| Absorption method election | **`POH-D-02` WITHHELD** — straight-line vs units-of-production, pending **Thai statutory evidence** |
| Over-absorption cap strength | **statutory `HOLD`** (`SC-SMT-11`) |

> **`PT07-F-02` — MATERIAL: the absorption denominator is ruled and the mechanism that would apply it does
> not exist.** Boss ruled *normal capacity* as the denominator; `R-22` records that fixed-overhead elements
> have no injection path; and limb 2 asks for proof that *exactly one* mechanism carries machine cost
> **"where the answer is zero."** **Three independent records agree that the carrier is absent, while the
> policy that would use it is settled.** A Pre-Test row asserting overhead absorption is therefore
> `PTE-3` **and additionally blocked on a non-existent mechanism** — a stronger statement than
> execution-dependence, and it must not be flattened into it.

### 3.3 Make-or-buy

| | |
|---|---|
| Routing template | **exists** — `XMC-F-03`, *"make-or-buy on demand"* |
| Template's reach | carries routing for `BN-01`, `BN-04`, `BN-05`, `BN-06`, `BN-16` **and the manufacture natures** |
| Caution | ***"no Phase SA register has read it"*** |
| **The trigger that SELECTS make** | **UNDETERMINED** — Set-A routing rule 2 |
| Make-to-stock vs make-to-order contrast | **`0` corpus representation** → `PT-S-03` |

---

## 4. Purchase

| Obligation | State |
|---|---|
| Procurement / replenishment / dropship → Purchase | **route HOLDS** |
| **Control floor** | **`XMC-H-03` — the cross-module entry sits BENEATH Purchase's control floor** |
| Governing determination | **`ND-03`: an automatic cross-module document may NOT enter a module below that module's control floor** |
| Over-receipt tolerance | **UNDEFINED** (`X-05`) — the default was originated by a prior round's own challenge and **routed to Boss** |
| Purchase return basis | **`PENDING — INVENTORY INTERNAL RESOLUTION FIRST`** |
| Prior-period attribution on late vendor bills | **NO MECHANISM EXISTS AT ALL** (`X-02`) |
| Goods-received bridge | **a swept suspense account, NOT item-matched** — weakens element 12 (`X-01`) |

> **`PT07-F-03` — the routing rule and the control determination are in direct tension, and both are
> current.** Set-A rule 3 records the dropship/procurement route as *holding* **and** as entering beneath
> Purchase's control floor; `ND-03` states that such an entry **may not** occur. **A route that "holds"
> while violating a Nature-DNA determination is not a route that holds — it is a route with a named
> control breach.** `SC-45`'s summary drops this qualification entirely (`PT05-F-01`).
> **Carried to `PT-12` as a control-breach row, not a routing success.**

---

## 5. Dropship — ruled, and what the ruling did not do

**`SC-BD-08`, `F3`:**

| | |
|---|---|
| Question | Does `BD-ACC-03A`'s Product-Category valuation authority reach a route with **no internal end**? |
| **Ruling** | **`OPTION (a)` — apply `BD-ACC-03A` as ruled, with NO route-specific exception.** `F3` **leaves the Boss decision list entirely** |
| Location semantics | the **counterparty pair** — supplier origin, customer destination — recorded as **external endpoints with reason, NOT `N/A`** |
| Vetoes | **`None discharged`** — *"`F3` carries no veto"* |
| Pre-Test effect | **not entry-gating**; ***"no exception class exists to build or test"*** |
| `C2-D-02` | **CLOSED** — cost binds to the same canonical Accounting Event Identity as revenue; **the remaining variable is the date, which is `F1`'s and was not asked twice** |

**Carried weakness, published in the ruling itself:**

> *"'resolves the movement chain' does not by itself exclude resolving to a **zero-length chain**
> (`SC-02` §6.1). This is a specification item for Functional Design, not a Boss decision."*

**And the reference system, held at arm's length:** the direct-shipment capability is *"installed in
**`0` of `3`** readable deployments, measured on two differently-shaped instruments."*

> **The ruling was made on SMEsPlus policy grounds while the reference implementation of the same feature
> is installed nowhere in the readable estate. No vendor implementation became policy — and the `0 of 3`
> is published rather than used as a reason to skip the route.**

**Still open on the dropship route:** `H-02` movement→valuation hop **`SEMANTICALLY INCOMPATIBLE — MEASURED`** ·
`H-03` cost→revenue **`NO IDENTITY`** · control-floor bypass `SA03-F-02` · `XMC-D-01` Boss election.

---

## 6. What `PT-12` must carry on the supply routes

| Row | Class | Blocking condition |
|---|---|---|
| `E2E-04` shortage→supply | **`PTE-3` + STRUCTURAL** | the target state machine has no supply exit; **not closable by a Boss election** |
| `X-16` / `E2E-03` overhead absorption | **`PTE-3` + NO MECHANISM** | `R-22 GAP`; veto limb 2 undischargeable as worded |
| `X-17` variance | **`PTE-3` + NO MECHANISM** | `1 of 9` recognised |
| `E2E-05` / `X-18` dropship | **`PTE-3`** | `H-02`, `H-03`, `XMC-D-01`; zero-length-chain spec item |
| Purchase cross-module entry | **`PTE-3` + CONTROL BREACH** | beneath the control floor, against `ND-03` |
| `PT-S-03` MTS vs MTO | **`PTE-3` + UNSPECIFIED** | the selection trigger is undetermined |
| Machine cost → product cost | **`PTE-4` EXTERNAL AUTHORITY** | AAS+ must re-word limb 2 first |
| `POH-D-02` absorption method | **`PTE-4` EXTERNAL AUTHORITY** | Thai statutory evidence absent |

---

## 7. Checkpoint

> ## `CP-PT-07 — SUPPLY ROUTING CHALLENGED`
>
> **`PT07-F-01` MATERIAL — the standing manufacturing veto (two limbs, limb 2 undischargeable **in either
> direction** as worded) is **absent from the veto register's population of six**: `0` occurrences of
> `BLK-07`, `BLK-08`, *manufactur* or *machine* in `SC-04`, positive control `3`. It is neither a member
> nor a declared exclusion, while `SC-19` asserts *"vetoes remain 6"* in the same file that describes it.
> **`6` carried as reported; population NOT established as complete; renumbering is not SMEs Core's act.**** ·
> **`PT07-F-02` — the absorption denominator is RULED (normal capacity) and the mechanism to apply it DOES
> NOT EXIST; three independent records agree the carrier is absent** ·
> **`PT07-F-03` — the procurement route "holds" while entering beneath Purchase's control floor, which
> `ND-03` forbids; carried as a control breach, not a routing success** ·
> `E2E-04` **NOT re-graded** — the shortage-exit half is a **defect, not an election**, per the Boss ruling
> itself · dropship **ruled**, `F3` off the list, `0` vetoes discharged, zero-length-chain weakness carried ·
> variance `1 of 9` · reference capability `0 of 3` deployments, published and **not** used as policy.
>
> **`0` vetoes discharged · `0` re-grades · `0` Boss elections answered.**

Next checkpoint: `PT-08 — SaaS / Tenant / Company / Security Boundary Matrix`.

No Evidence = No Progress. Never Skip Gate. Truth over Pass. SMEs Core may not discharge another authority's veto.
Boss remains the sole Final Approver.
