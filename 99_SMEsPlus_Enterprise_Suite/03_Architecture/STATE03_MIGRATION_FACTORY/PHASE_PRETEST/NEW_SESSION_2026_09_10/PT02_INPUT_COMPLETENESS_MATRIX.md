# PT-02 — INPUT COMPLETENESS MATRIX

## `CP-PT-02 — INPUTS BOUNDED, NOT COMPLETE`

*(master-prompt checkpoint name: `CP-PT-02 — INPUTS COMPLETE OR BOUNDED`; the evidence supports only `BOUNDED` — §7)*

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]`
Branch: `architecture/account-phase-pretest-new-session-2026-09-10-001` · head consumed `05173c0e`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **`0 of 22` verified · `EC-04` `0/3` · `6` vetoes in force · `E2E-04` `NOT TRAVERSABLE`.**

---

## 1. Result

| | |
|---|---|
| Input instrument used | **Boss-approved 16-element Minimum Handoff Data Contract** — blob `b4c39831`, `BOSS APPROVED / EFFECTIVE` |
| Boundary denominator | **`12`** — Boss-ruled `XMC-D-02 = EXTEND TO ALL BOUNDARIES` (`SC-BD-02`) |
| Elements **supplied or conditionally supplied** | **`9 of 16`** |
| Elements **NOT supplied** | **`7 of 16`** — elements `4`, `7`, `10`, `12`, `13`, `14`, `15` |
| Of those, elements with **no carrier at all** | **`3`** — elements `10`, `14`, `15` |
| Scenarios of the 22 blocked on elements `4`/`7` | **`11 of 22`** — enumerated, not estimated |
| `HOLD` rows in the 22-scenario register | **`22 of 22`** |
| Material unknowns **resolvable by SMEs Core and therefore resolved or actioned here** | **`0`** — §6, each tested individually |
| **Findings raised by this checkpoint and then DISPROVED by its own author** | **`1`** — `PT02-F-02`, withdrawn at §5.1 |
| **`CP-PT-02` disposition** | **`BOUNDED`, not `COMPLETE`** — §7 |

> **The checkpoint's allowed outcome is `INPUTS COMPLETE **OR** BOUNDED`. The honest one is `BOUNDED`.**
> Inputs are **not** complete: seven of sixteen mandatory elements are unsupplied, and three of those have
> no carrier in the design at all.

---

## 2. The instrument, and the standard it sets

**Primary text, `03_BOSS_APPROVAL_INVENTORY_TO_ACCOUNTING_MINIMUM_HANDOFF_DATA_CONTRACT_2026_09_02.md`,
blob `b4c39831`, Jira `ERPPLUS-140`, status `BOSS APPROVED / EFFECTIVE`.**

**The standard for an element being supplied is Boss's own, and it is three conjuncts:**

> *"must prove that the following information is **known, traceable, and evidence-backed**"*

**A specification satisfies none of the three on its own** (`SA_CORR2_04` §3, applied to element 10 and
carried here to **every** element — including the ones it would be pleasant to close).

**Boss's own disposition rule for a missing field, carried verbatim:**

> *"Blank values are not acceptable for material fields. If a field is not applicable, record `N/A` plus
> reason. If it is unknown or unsupported, record `HOLD / EVIDENCE REQUIRED`; **do not infer or fabricate
> the value**."*

**And Boss's own bar on declaring a scenario proven** — a scenario may **not** be `VERIFIED` if any
material element is missing, ambiguous, unsupported by evidence, contradictory across domains, dependent
on an unapproved assumption, unable to link reversal to original, unable to prevent duplicate effects, or
missing company/tenant context.

### 2.1 Scope — the contract was written for one boundary and Boss extended it to twelve

| | |
|---|---|
| Contract's **own** declared scope | **Inventory → Accounting, one direction** — stated four times (title, §1, §4, §5); verified verbatim as `XMC-F-12` |
| Boss ruling `SC-BD-02` | **`XMC-D-02 = EXTEND TO ALL BOUNDARIES`** — one general contract with **declared per-boundary applicability** |
| Boundary denominator | **`1` → `12`** |
| Binding condition (`SC-SMT-08`) | an applicability declaration **carries the contract's authority**. **A boundary may propose; it may not declare.** |

> **`13 of the 16` elements are domain-general.** Only elements `6` (UOM), `8` (product/lot/serial) and
> `9` (warehouse/location) are stock-shaped — and the contract already handles that with its
> `N/A`-plus-reason rule. **The extension is therefore an increment, not a re-scope.**

---

## 3. Element-by-element completeness across the population

**UNIT:** one contract element. **DENOMINATOR:** `16`. **BASIS:** primary Phase SA registers.

| # | Element | State | Evidence |
|---:|---|---|---|
| 1 | `WHAT happened` | **SUPPLIED** | every scenario names its business event |
| 2 | `WHO owns the fact` | **SUPPLIED** | `Inventory = Stock Truth`, `Accounting = Financial Truth` — contract §2, `BD-ACC` rulings |
| 3 | `WHEN physical event occurred` | **SUPPLIED** | physical movement timestamp is the Perpetual trigger (`ND-10`) |
| **4** | **`WHEN financial recognition occurs`** | **NOT SUPPLIED** | **`11 of 22`** scenarios blocked `el.4/7`; recognition-point split — **`BP-02` (COGS at delivery) not selectable** (`X-03`); Boss `F1` (`JT-04`/`JT-05`) |
| 5 | `HOW MUCH quantity` | **SUPPLIED** | controlled quantity present on every movement |
| 6 | `WHICH UOM` | **SUPPLIED** (stock-shaped; `N/A`+reason elsewhere) | — |
| **7** | **`WHAT valuation / cost basis applies`** | **NOT SUPPLIED** | same **`11 of 22`**; COGS residual is Boss `F1` **plus a statutory `HOLD`**; `X-13` scrap has **no cost causality**, salvage **undefined** |
| 8 | `WHICH Product / Lot / Serial` | **SUPPLIED where applicable** | — |
| 9 | `WHICH Warehouse / Location` | **SUPPLIED where applicable** | dropship records **counterparty endpoints as external, not `N/A`** (`SC-45` §2) |
| **10** | **`WHICH Company / Tenant`** | **NOT SUPPLIED — NO CARRIER** | **specified, not built.** `0 of 8` isolation proofs · `0 of 60` negative cases (52 rejection cells + `S-01`…`S-08`) · `0 of 13` enforcement surfaces. **`X-15` *is* element 10**; **two** lock-defeat paths, the second leaving no record |
| 11 | `WHICH Source Document` | **SUPPLIED** | — |
| **12** | **`WHICH Original Event`** | **NOT SUPPLIED — WEAKENED** | the goods-received bridge is **a swept suspense account, not item-matched** (`X-01`), which **breaks correlatability at the point the contract needs it** |
| **13** | **`WHICH Reversal / Correction`** | **NOT SUPPLIED** | **the corrected-entry link does not exist** (`X-11`); the only correction route after a completed movement is a return; reversal **basis** is `JT-05` **NOT DECIDABLE** |
| **14** | **`WHICH Migration / Replay Batch`** | **NOT SUPPLIED — NO CARRIER** | **the provenance reference does not exist and must be originated** (`X-20`); `MTI-42` prohibits inferring context at migration (`X-21`) |
| **15** | **`WHICH Idempotency Identity`** | **NOT SUPPLIED — NO CARRIER** | **specified, not built, not verified.** *"none has been designed"* — a **SMEs Core design act, open**. **`X-22` *is* element 15.** Carrier is table-global; **`0 of 13,814` rows carry a deduplication key** |
| 16 | `WHAT Evidence proves it` | **SUPPLIED as a register** | evidence references exist throughout; their **sufficiency** is what every other row tests |

### 3.1 The tally, and the part that matters most

| Class | Elements | Count |
|---|---|---:|
| Supplied / conditionally supplied | `1`, `2`, `3`, `5`, `6`, `8`, `9`, `11`, `16` | **`9`** |
| **Not supplied — carrier exists but is blocked or weakened** | `4`, `7`, `12`, `13` | **`4`** |
| **Not supplied — NO CARRIER IN THE DESIGN AT ALL** | **`10`**, **`14`**, **`15`** | **`3`** |
| Total | | **`16`** |

> **The three no-carrier elements are the load-bearing ones.** Element `10` is tenant/company isolation,
> element `15` is the join key on which every cross-module retry and duplicate test depends, and element
> `14` is migration provenance. **`X-15` *is* element 10 and `X-22` *is* element 15** — two of the
> twenty-two scenarios are not scenarios that *use* a missing element, they **are** the missing element.

---

## 4. Scenario-level missing mandatory inputs — Population A (`22`)

**Measured, not estimated:** `22 of 22` rows sit at `HOLD`; **`12` `DEPENDENCY` + `10` `STRUCTURAL` = `22`** ✔;
**`11`** rows carry `el.4/7` — scenarios **`1, 2, 3, 4, 5, 6, 8, 9, 16, 17, 19`**, enumerated by command.

| Scenario | Missing mandatory input |
|---|---|
| `X-01` | el.`4`/`7`; **el.`12` weakened** — bridge is a swept suspense account, not item-matched |
| `X-02` | el.`4`/`7`; **no prior-period attribution mechanism exists at all** |
| `X-03` | el.`4`/`7`; **`BP-02` not selectable** — the recognition point cannot be chosen |
| `X-04` | el.`4`/`7` (`JT-04` `CONFLICTING` discharged) |
| `X-05` | el.`4`/`7`; **over-receipt tolerance undefined** |
| `X-06` | el.`4`/`7`; `H-05` — draft invoice consumes billable quantity, posts nothing, freely deletable |
| `X-07` | **`R-17` `NO CONSUMER`** — the remainder-supply record has no consumer at all; cancellation leaves **no document trail** |
| `X-08` | el.`4`/`7`; return basis `PENDING` |
| `X-09` | el.`4`/`7`; **`JT-05` NOT DECIDABLE** — original-cost vs current-cost |
| `X-10` | `C-01` symmetry; `C2-F-01` durability precondition |
| `X-11` | **el.`13` — the corrected-entry link does not exist** |
| `X-12` | **approval mechanism absent**; an adjustment can **silently reduce a reservation** |
| `X-13` | **salvage undefined**; scrap has **no cost causality** |
| `X-14` | `R4-F-18` — **no independent check exists**; neutrality is configuration-protected only |
| `X-15` | **el.`10` in its entirety** — `0 of 8`, `0 of 60`, `0 of 13` |
| `X-16` | el.`4`/`7`; **fixed-overhead elements have no injection path**; `R-22` `GAP` |
| `X-17` | el.`4`/`7`; **no variance mechanism exists** — one of nine recognised |
| `X-18` | **two-axis classification tie-break undefined**; `BD-ACC-01` **silent for services** |
| `X-19` | el.`4`/`7`; **no accounting-period object exists** |
| `X-20` | **el.`14` — the provenance reference does not exist and must be originated** |
| `X-21` | **el.`14`**; `MTI-42` prohibits inferring context at migration |
| `X-22` | **el.`15` in its entirety** — `UAE-29` is the root |

## 4.1 Population B (`18`) — required inputs not yet established

Carried from `SA17` §2 **without re-grading**:

| Scenario | Required input not yet established |
|---|---|
| `E2E-01` | Boss `F2` (`TV6-BOSS-01`, `XD1-P1`), `TV6-BOSS-02` |
| `E2E-02` | **none** — approval internal logic open (A2) |
| `E2E-03` | Boss `F5` (`B-6`, `POH-D-02`) |
| **`E2E-04`** | **Boss `F4` (`C2-D-01`) — and the missing procurement exit.** `NOT TRAVERSABLE`; **not re-graded here** |
| `E2E-05` | Boss `F3` (`XMC-D-01`, `C2-D-02`) |
| `E2E-06` | order→purchase linkage and reservation semantics |
| `E2E-07` | **none** — both blockers closed |
| `E2E-08` | **none** — `XMC-C-C2` specifies asserter, time, basis, obligation |
| `E2E-09` | Equipment-side semantics |
| `E2E-10` | — |
| `E2E-11` / `E2E-12` | Boss `F1` (`JT-05`) |
| `E2E-13` | by-product valuation; **Boss `F1` for the cost side** (`F1`'s own card omitted this scenario — `CHF-18`) |
| `E2E-14` | period object specified; **analytic data; statutory register content** |
| `E2E-15` | **element 15 — specified, not built** |
| `E2E-16` | the Quality **object** (absent) |
| `E2E-17` | Boss `F5` (`BLK-08`) |
| `E2E-18` | derivation mechanism; reversal behaviour |

## 4.2 Population C (`7`) — inputs required by the added scenarios

| Scenario | Mandatory input status |
|---|---|
| `PT-S-01` tax | **el.`4`/`7` + statutory content.** `POH-D-02` **withheld** pending Thai statutory evidence; `BD-ACC-02` company-scoped; `R-19` `HARD` — *"neither module computes tax itself"* |
| `PT-S-02` direct buy→sell | inherits `X-01` + `X-03` — el.`4`/`7` and el.`12` |
| `PT-S-03` MTS vs MTO | **the selection input itself is undefined** — the contrast has `0` corpus representation |
| `PT-S-04` partial invoice / payment | inherits `X-05`/`X-06`; **partial payment has `0` corpus representation** |
| `PT-S-05` return before / after invoice | **the timing discriminator is undefined**; inherits `JT-05` |
| `PT-S-06` reversal after downstream consumption | **el.`13` + el.`15`** — both no-carrier or broken |
| `PT-S-07` out-of-order / stale / partial failure | **el.`15`** — no carrier; ordering has `0` corpus representation |

---

## 5. `PT02-F-01` — an input defect the element view exposes that the scenario view hides

**`X-07` backorder carries `R-17 NO CONSUMER`.**

The 16-element contract's proof standard `P5` requires that **every downstream consumer is enumerated,
and a missing consumer is a defect**. `X-07`'s remainder-supply record has **no consumer at all**, and
never-mode remainder cancellation leaves **no document trail**.

> **This is not a missing input to a known consumer. It is a produced output with nobody to receive it —
> the contract's `P5` clause failing in the one direction a per-scenario reading does not look.**

**Consequence for `PT-04`:** the output/consumer matrix must test **producer→∅** as a distinct failure
class, not only consumer→missing-input. **Carried forward.**

## 5.1 `PT02-F-02` — RAISED, THEN **DISPROVED BY PRIMARY TEXT**, BY ITS OWN AUTHOR

> ### `PT02-F-02` IS WITHDRAWN. The finding was wrong, and the reason it was wrong is instructive enough to publish in full rather than delete.

### What was claimed

That element 15's **design** half — *"a design act"*, *"none has been designed"* — was an **open,
current-scope SMEs Core specification obligation**, and therefore a candidate contradiction with
`MATERIAL PHASE-SA GAP = 0` and a clause-5 dumping breach.

### What disproves it

**The quoted source was `SA_CORR4_07` §3 (CORR4). It is superseded on this exact claim by `SA_CORR5_01`
(CORR5) — a later round whose entire subject is the adjudication of element 15's design.**

`SA_CORR5_01_ELEMENT15_IDEMPOTENCY_ADJUDICATION.md`, `CP-SA-C5-10`, executed under `BD-ACC-01`'s express
grant (*"Phase SA may design the technical representation independently"*), exercised **narrower than
granted** — business-semantic clauses only, no identifier format, no schema, no generation scheme.

**Its finding `C5-01-F-01` addresses the exact sentence this finding was built on, verbatim:**

> *"The object the programme has recorded as **"does not exist"** and **"none has been designed"** exists
> as a specified identity basis (`P2`), a Boss-ruled ownership model (`P1`), a consumer obligation (`P3`,
> `P4`), a scoping half (`P5`), an act-level attempt-identity contract in a Team B design (`P13`) and an
> adopted V1 design naming the attempt component (`P14`) — in seven documents that do not cite each other.
> **What has never existed is one adjudicated statement** of which position governs which question…
> **That is an adjudication … and this file is it.**"*

**The design exists:** `XMC-C-A1`…`A13` specify the deterministic identity basis in **six parts** —
tenant · company · owning source domain · business-fact occurrence as its owner identifies it ·
recognition role · policy version in force at recognition — with exclusions (`A5`), retry (`A6`), replay
(`A7`), reversal (`A8`), correction (`A9`), fail-closed scope (`A10`), consumer reliances (`A11`/`A12`)
and namespace (`A13`). `SA_CORR5_01` located **`15` candidate positions** over `327` paths and adjudicated
among them. **`22`-scenario row 22 is graded `SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED` on that basis.**

### Why the error happened — the defect is mine, and it is a known class

| | |
|---|---|
| Defect class | **superseded-source citation.** `SA_CORR4_07` was read as current; `SA_CORR5_01` supersedes it on this claim |
| What made it plausible | `SA17` (final, correct) says element 15 is ***"specified, not built, not verified"***. **`specified` = the design act is done; `not built` = the runtime half is open.** The two halves were **collapsed**, and CORR4's stale sentence was used to reinterpret `specified` as *not designed* |
| What would have caught it sooner | asking **"is this the latest artefact on *this claim*"** — not on this topic, not in this package. **Supersession binds at claim level** |
| What did catch it | following row 22's own pointer (`SA_CORR5_01`) instead of stopping at the summary that suited the finding |

### What survives, and what does not

| Claim | Verdict |
|---|---|
| Element 15's **design** half is an open SMEs Core specification gap | **DISPROVED** |
| It is a clause-5 dumping breach | **DISPROVED** — falls with the above |
| Candidate contradiction with `MATERIAL PHASE-SA GAP = 0` | **WITHDRAWN** |
| Element 15 is **specified, not built, not verified** | **STANDS** — unchanged carry-forward |
| The **runtime** half is execution-dependent and open | **STANDS** — `SC-58` §2 row 2 correct as written |
| **`C-02`** — whether idempotency is **gate-blocking** — is an open **Boss severity election** | **STANDS** (`F8`) |
| Element 15 has **no built carrier**; `0 of 13,814` rows carry a deduplication key | **STANDS** — §3 row 15 unchanged |

**§3's element-15 row is NOT amended:** *"NOT SUPPLIED — NO CARRIER"* remains correct, because
**`supplied` is the contract's three-conjunct standard — known, traceable AND evidence-backed — and a
specification satisfies none of the three on its own.** The design existing does not make the element
supplied. **The `9 / 4 / 3` element tallies in §3.1 are unchanged.**

> **What this costs and what it buys.** The session loses a material finding it had already published.
> It keeps the rule that produced it: **a negative about someone else's work is a claim, and it is
> tested against the latest artefact on that claim before it is allowed to stand.** It was not, and one
> round of following a pointer disproved it.

## 6. Material unknowns — which could SMEs Core still resolve?

**Master prompt `PT-02`: *"Any material unknown that can still be researched by SMEs Core must be resolved
before proceeding."*** **Each unknown was tested against the `SC-58` discriminating test.**

| Unknown | Researchable by SMEs Core now? | Ground |
|---|---|---|
| el.`4`/`7` recognition point + cost basis | **NO** | **Boss election `F1`** (`JT-04`/`JT-05`) plus a statutory `HOLD`. Researching it further **cannot** produce the election |
| el.`10` isolation proofs | **NO** | requires an implementation; `0 of 8`, `0 of 60`, `0 of 13` — a **run**, not a document |
| el.`14` provenance reference | **NO — but note** | *"must be originated"* is a **design** act; it is **owned by element 14's Functional Design scope**, and originating it here would be **Functional Design, which is NOT AUTHORIZED** |
| el.`15` **design** identity | **N/A — ALREADY DONE** | **§5.1.** Adjudicated at `SA_CORR5_01` under `BD-ACC-01`'s grant. **Not an open unknown.** The runtime half remains execution-dependent |
| el.`12` bridge item-matching | **NO** | a target-system structural fact already measured |
| el.`13` corrected-entry link | **NO** | the link **does not exist**; creating it is design |
| Thai statutory content (`PT-S-01`) | **NO** | **external authority** — `POH-D-02` withheld |
| MTS/MTO discriminator, partial payment, event ordering | **NO** | `0` corpus evidence; originating them is **design** |

> **`0` unknowns were resolvable-and-unresolved**, and the one candidate (element 15 design) turned out
> **already adjudicated** at `SA_CORR5_01` — see §5.1, where this checkpoint's own finding is withdrawn.
>
> **The remaining unknowns are unresolvable *here* for three distinct reasons, and the distinction is
> load-bearing:** Boss election (el.`4`/`7`), external authority (Thai statutory), or **because
> originating the missing object would be Functional Design, which this session is NOT AUTHORIZED to
> perform** (el.`13`, el.`14`, the MTS/MTO discriminator). **The third class is the one at risk of being
> mistaken for a dumped gap; it is named here so `PT-13` and B-7 can test that reading rather than
> inherit it.**

---

## 7. Why the disposition is `BOUNDED`, not `COMPLETE`

| Allowed outcome | Applies? |
|---|---|
| `INPUTS COMPLETE` | **NO.** `7 of 16` mandatory elements unsupplied; `3` have no carrier |
| **`INPUTS BOUNDED`** | **YES.** Every missing input is **named, owned, and classified**; `0` are unaccounted for; `0` were inferred or fabricated, per the contract's own prohibition |

**Bounded means:** the missing set is **closed and enumerated** — not that it is small.

---

## 8. Checkpoint

> ## `CP-PT-02 — INPUTS BOUNDED`
>
> **Instrument = the Boss-approved 16-element contract (blob `b4c39831`), applied at its own three-conjunct
> standard *known, traceable and evidence-backed*, with `SC-BD-02`'s `12`-boundary extension ·
> **`9 of 16` elements supplied, `7` not, and `3` of those have NO CARRIER (`10`, `14`, `15`)** ·
> `22 of 22` scenarios at `HOLD`, `11` blocked on el.`4`/`7`, enumerated by command · `12 DEPENDENCY +
> 10 STRUCTURAL = 22` ✔ · **`PT02-F-01`: `X-07` is a produced output with no consumer — a `P5` failure the
> per-scenario view hides** · **`PT02-F-02`: RAISED AND THEN DISPROVED BY ITS OWN AUTHOR** — element 15's design half is
> **already adjudicated** (`SA_CORR5_01`, `15` positions over `327` paths); the finding rested on a
> **superseded** CORR4 sentence. Withdrawn in full at §5.1, with the defect class named. **`0` element
> tallies change** · `0` unknowns resolvable-and-unresolved · `0` values
> inferred or fabricated.**
>
> **Disposition `BOUNDED`, NOT `COMPLETE`. `E2E-04` not re-graded. `0 of 22` verified.**

Next checkpoint: `PT-03 — Process Semantic and Control Matrix`.

No Evidence = No Progress. Never Skip Gate. Truth over Pass. Falsify before Accept.
Boss remains the sole Final Approver.
