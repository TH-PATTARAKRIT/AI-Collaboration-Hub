# 32A — `CORE-05` — DETERMINISTIC KIND / CATEGORY REFUSAL RULE

## `CHECKPOINT E (part 2) — CORE-05 SPECIFIED · 0 SILENT FALLBACKS`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7-RETURN-CORR1-001]` · Boss: **SOLE FINAL APPROVER**

> **Numbered `32A_` because prompt §12 names no output file and `33_`…`37_` are reserved by §14.
> Ordering is preserved; no identifier collides.**

**Authority:** `CC-D-01`, ruled at `22_` §3 — **(a)** *"KIND governs **admissibility**; CATEGORY governs
**measurement**; **a deterministic refusal rule is mandatory** where CATEGORY requires a policy that KIND
cannot legally/semantically use"* · **(b)** *"Service carries **an explicit recorded determination that no
cost recognition arises** where the applicable rule produces no recognized cost."*

**Scope of this act:** a **specification**, within SMEs Core authority, of an obligation a Boss ruling
created. **It elects nothing. `0` Boss items arise.**

---

## 1. The two axes, and the exact collision

| Axis | Governs | Values | Authority |
|---|---|---|---|
| **KIND** | **admissibility** — whether a thing can hold stock and carry cost at all | Goods · Consumable · Service · Raw Material · WIP · Finished Goods | product type |
| **CATEGORY** | **measurement** — how carried cost is recognised and computed | `Periodic \| Perpetual` (`BD-ACC-03A`) × `Standard \| Average \| FIFO` (`BD-ACC-03B`) | **Product Category only** |

**The collision:** CATEGORY is assignable **independently** of KIND. A Category configured
`Perpetual + FIFO` can be assigned to a Service, and `Perpetual` requires *recognition at the physical
movement* (`JT-04`, `SC-BD-05`) while a Service **has no physical movement** — `XMC-H-17`: *"for a service
there is **no physical fact, only an assertion**, with no event record."*

> **What each measurement policy REQUIRES of the KIND:**
>
> | Policy | Required of KIND |
> |---|---|
> | `Perpetual` | a **physical movement event** to recognise against |
> | `Periodic` | a **closing stock position** to value at period end |
> | `Standard` | a **cost-carrying object** to which a standard attaches |
> | `Average` | a **carried cost pool** with quantity |
> | `FIFO` | **ordered cost layers** consumed in acquisition sequence |

---

## 2. Decision precedence — deterministic, ordered, total

```
STEP 1  ADMISSIBILITY   — read KIND. Determine which of {movement, closing position,
                          cost object, cost pool, ordered layers} the KIND admits.
STEP 2  MEASUREMENT     — read CATEGORY. Determine which of those five the policy REQUIRES.
STEP 3  INTERSECTION    — every requirement of STEP 2 must be admitted by STEP 1.
STEP 4  OUTCOME         — all admitted        -> PROCEED, value under CATEGORY policy
                        - one or more absent  -> REFUSE, with the code at §4
                        - KIND admits none    -> CC-D-01(b) EXPLICIT RECORDED DETERMINATION
```

**Precedence rule, stated once:** **KIND is evaluated first and is never overridden by CATEGORY.**
A Category policy cannot confer on a KIND a capability the KIND does not have. This is `XMC-C-D6`'s
precedence — *physical > policy > commercial* — applied to the measurement axis.

**Totality:** every `KIND × CATEGORY` pair resolves to exactly one of `PROCEED` / `REFUSE` /
`RECORDED DETERMINATION`. **There is no fourth outcome and no default branch.**

---

## 3. The matrix — `6` KINDs × `5` requirements

| KIND | movement | closing position | cost object | cost pool | ordered layers | `Perpetual` | `Periodic` | `Standard` | `Average` | `FIFO` |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Goods (stockable)** | ✔ | ✔ | ✔ | ✔ | ✔ | PROCEED | PROCEED | PROCEED | PROCEED | PROCEED |
| **Raw Material** | ✔ | ✔ | ✔ | ✔ | ✔ | PROCEED | PROCEED | PROCEED | PROCEED | PROCEED |
| **WIP** | ✔ | ✔ | ✔ | ✔ | ✔ | PROCEED | PROCEED | PROCEED | PROCEED | PROCEED |
| **Finished Goods** | ✔ | ✔ | ✔ | ✔ | ✔ | PROCEED | PROCEED | PROCEED | PROCEED | PROCEED |
| **Consumable** | ✔ | **✘** | ✔ | **✘** | **✘** | PROCEED | **`KCR-02`** | PROCEED | **`KCR-03`** | **`KCR-04`** |
| **Service** | **✘** | **✘** | **✘** | **✘** | **✘** | **`KCR-01`** | **`KCR-02`** | **`KCR-05`** | **`KCR-03`** | **`KCR-04`** |

**`WIP` note:** admissible on all five, and separately **`GATED`** on overhead absorption — `B-6`
(`POH-D-01` ruled, **`POH-D-02` withheld**, veto limb `2` outstanding). **Admissibility is not readiness;
scenarios `16`/`17` remain `GATED` at `27_`.**

**`Consumable` basis, declared because the evidence is thinner than the rest:** the corpus treats
Consumable as *"consumable / expense **immediate expense**"* (`PT-01` §5.3; `X-18`, `E2E-10`). An
immediately expensed item carries **no closing position and no cost pool**, so `Periodic`, `Average` and
`FIFO` have nothing to operate on. **If Boss or Functional Design later determines that a Consumable is
expensed at ISSUE rather than at RECEIPT, it carries a pool until issue and this row changes to all
`PROCEED`.** **Named as a Round-2 attack target rather than asserted.**

---

## 4. Refusal codes, and what each one does

| Code | Fires when | User-facing semantic (plain, no jargon) | Posting | Inventory | Audit event |
|---|---|---|:-:|:-:|---|
| **`KCR-01`** | CATEGORY requires a **movement event**; KIND admits none (`Perpetual` × Service) | *"This category recognises cost when goods move. A service does not move. Choose a category that recognises cost on performance, or change the product type."* | **PROHIBITED** | **PROHIBITED** | **`KCR-EVT-01`** |
| **`KCR-02`** | CATEGORY requires a **closing stock position**; KIND carries none (`Periodic` × Service/Consumable) | *"This category values what is left at period end. This product type never holds a closing balance."* | **PROHIBITED** | **PROHIBITED** | `KCR-EVT-01` |
| **`KCR-03`** | CATEGORY requires a **carried cost pool** (`Average` × Service/Consumable) | *"This category averages the cost of what is held. This product type holds nothing to average."* | **PROHIBITED** | **PROHIBITED** | `KCR-EVT-01` |
| **`KCR-04`** | CATEGORY requires **ordered layers** (`FIFO` × Service/Consumable) | *"This category consumes cost in the order it was acquired. This product type has no acquisition layers."* | **PROHIBITED** | **PROHIBITED** | `KCR-EVT-01` |
| **`KCR-05`** | CATEGORY requires a **cost object** for a standard (`Standard` × Service) | *"A standard cost attaches to a thing that is made or bought. A service is neither."* | **PROHIBITED** | **PROHIBITED** | `KCR-EVT-01` |
| **`ND-09-B`** | **`CC-D-01`(b)** — the applicable rule produces **no recognized cost** and the configuration is otherwise valid | *"No cost is recognised for this line, and that determination has been recorded."* | **`0` cost posting; the determination IS posted as a record** | none | **`KCR-EVT-02`** |

### 4.1 Prohibitions — absolute

| | |
|---|---|
| **Posting prohibition** | on any `KCR-01`…`-05`, **no accounting event of any kind is created.** Not a zero-value posting, not a suspense posting, not a deferred posting |
| **Inventory prohibition** | **no movement fact is created.** A refused line does not reserve, receive, issue or adjust |
| **`0` silent fallback** | **there is no branch in which the system selects a different policy, substitutes a default, or proceeds at zero cost without a recorded determination.** §12's requirement, met by construction: §2 STEP 4 is total |
| **`ND-09-B` is not a fallback** | it is a **recorded positive determination** with its own event, reached only where the configuration is valid and the rule genuinely yields no cost. It is never reached by failing `KCR-01`…`-05` |

### 4.2 Audit events

| Event | Carries |
|---|---|
| **`KCR-EVT-01`** refusal | KIND · CATEGORY · the requirement not admitted · the code · who · when · the attempted document identity · **non-dismissible** |
| **`KCR-EVT-02`** no-cost determination | KIND · CATEGORY · the rule applied · the basis for zero · who · when · the document identity |

**Both inherit `M-1`…`M-6` (`SC-BD-07`): every firing emits an event; the event's **emission is not
configurable**, only the outcome is.** A configuration that could suppress `KCR-EVT-01` would turn a
refusal into a silent skip — the exact defect `M-6` exists to prevent.

---

## 5. Override policy

| | |
|---|---|
| **Is `KCR-01`…`-05` overridable?** | **NO.** These are **control floors**, and `SC-BD-07` §5 binds: *"no override may lower a control **floor**."* A KIND that cannot produce an input does not acquire the ability by configuration |
| **What IS configurable** | the **Category assignment itself**. The correct remedy for a refusal is to assign a Category whose policy the KIND admits, or to change the product type — **both of which are evented configuration acts with their own approval** |
| **Company-scoped override** | **not available on this control.** Distinguish from `F2`'s commercial control defaults (`XD1-P1`, `TV6-BOSS-01`, over-receipt tolerance), which **are** Company-configurable because both branches are semantically coherent. **Here one branch is incoherent** |
| **`ND-09-B`** | not an override; a determination. Recorded, not suppressible |

---

## 6. Status and residuals

| | |
|---|---|
| **`CORE-05`** | **DISCHARGED as a specification.** Precedence, totality, per-KIND matrix, `6` codes, prohibitions, `2` audit events and the override policy are stated |
| **Build obligation** | **Functional Design.** `CC-D-01` created it; this file specifies it; **nothing here is built** |
| **Boss item?** | **NO.** `CC-D-01` already ruled the precedence; this applies it |
| **Residual `1`** | the **Consumable** row's basis (§3) — expensed at receipt vs at issue. **Declared, not hidden** |
| **Residual `2`** | `WIP` remains `GATED` on `B-6` — admissibility is not readiness |
| **Residual `3`** | `IR-17` remains **`PARTIAL`** and is **not** converted by this file, per `CC-D-01`'s own Boss constraint |

---

## 7. Checkpoint

> ## `CHECKPOINT E (part 2) — CORE-05 SPECIFIED`
>
> **KIND × CATEGORY resolved deterministically: `5` measurement requirements tested against `6` KINDs,
> **every pair resolving to exactly one of `PROCEED` / `REFUSE` / `RECORDED DETERMINATION`** ·
> `6` codes (`KCR-01`…`-05`, `ND-09-B`) with posting and inventory prohibitions **absolute** ·
> **`0` silent fallbacks — §2 STEP 4 is total by construction** · `2` audit events inheriting `M-1`…`M-6`,
> **emission not configurable** · refusals are **control floors and not overridable** ·
> `3` residuals declared, `1` of them named as a Round-2 target · **`0` Boss items · `0` built.**

No Evidence = No Progress. Do not invent a silent fallback. Boss is the sole Final Approver.
