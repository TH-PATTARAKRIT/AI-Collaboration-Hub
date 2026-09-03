# 10 — DEEP LEVEL 5: WHOLE-SYSTEM ASSET SEMANTIC MODEL
**LAYER 2 — AUDIT QUARANTINE**

Levels 1–4 established what exists. Level 5 assembles it into one lifecycle and
tests the Boss's design hypotheses against it. **Nothing in this level is a design
approval.** Design candidates are labelled as such throughout.

## 1. The whole lifecycle — §55

| Stage | What the reference system does | Evidence |
|---|---|---|
| Acquire | Vendor bill posted on a flagged account | `FACT VERIFIED` |
| Recognise | Asset row created in `draft`, value = bill line balance | `FACT VERIFIED` |
| Capitalise | **Not a distinct step.** Value is assigned at recognition; there is no accumulation stage | `VERIFIED GAP` |
| Configure | Method, duration, period, computation mode, three accounts, journal, salvage, analytic | `FACT VERIFIED` |
| Start | Confirm → `open`, and **the entire remaining board is computed and posted at once** | `FACT VERIFIED` |
| Period calculation | Cumulative-difference formula on the chosen day convention | `FACT VERIFIED` — `16` |
| Financial posting | Dr expense / Cr accumulated, dated at period end | `FACT VERIFIED` |
| Analytic attribution | Distribution copied onto both lines at preparation time | `FACT VERIFIED` — `21` |
| **Operational use** | **Not modelled.** The asset does not know it is being used | `VERIFIED GAP` |
| **Maintenance** | Happens to the *equipment*, invisibly to the asset, and costs nothing | `VERIFIED GAP` |
| **Production use** | **Not modelled** | `VERIFIED GAP` |
| **Cost allocation** | **Not modelled from the asset** | `VERIFIED GAP` |
| Modify | Catch-up, reverse the future, rebuild forward. History untouched | `FACT VERIFIED` |
| Pause / resume | Calendar shift; the end date moves out | `FACT VERIFIED` |
| **Fully depreciated** | **Not a state.** The board stops producing lines; the asset stays `open` | `VERIFIED GAP` |
| **Continue operating** | Invisible | `VERIFIED GAP` |
| **Post-depreciation usage** | No concept anywhere | `VERIFIED GAP` — SMEsPlus original |
| Sell / dispose | Cost out, accumulated out, proceeds in, balance to gain or loss | `FACT VERIFIED` — `25` |
| Derecognise | `close`; salvage removed from book value | `FACT VERIFIED` |
| Audit / reporting | Chatter tracking + the Depreciation Schedule report | `FACT VERIFIED` |

**Nine of twenty lifecycle stages are absent from the reference system**, and every
one of the nine is on the operational side. This is the Level-1 boundary statement
proved out over the full lifecycle.

## 2. The Four Truths — §56

The prompt's four-truths separation is not an analytical convenience. It is
**forced by the evidence**, because the system genuinely holds these four things
in different places with different owners and no reconciliation between them.

### A. Financial truth — `EXISTS, COMPLETE`

Original value, depreciable base, accumulated depreciation, book value, salvage,
gain or loss on disposal. Owner: the journal entries. Complete, immutable,
guarded, auditable.

### B. Operational truth — `EXISTS, SEPARATE`

Equipment identity, category, serial number, location, work centre, maintenance
history, MTBF, MTTR, downtime, availability. Owner: the equipment and maintenance
records. Complete for scheduling. **Contains no money.**

### C. Cost truth — `PARTIALLY EXISTS`

Work-centre hourly rate → work-order cost → WIP → finished goods → COGS, plus
analytic lines and a labour GL entry. Owner: the work centre and the valuation
layers.

**Complete downstream of the rate. Empty upstream of it.** The rate is typed in by
a person. Truth A never reaches it. Truth B never reaches it.

### D. Management truth — `DOES NOT EXIST`

Post-depreciation internal usage, lifetime economic contribution, off-balance
management cost. **No trace of any of it in the reference system.** Entirely
SMEsPlus original construction.

### The bridges

| Bridge | Status |
|---|---|
| A ↔ B | **One custom manual field.** Consumed by nothing but a status flip. Half of it is dead code |
| A ↔ C | **Absent** — the rate is not derived from depreciation |
| B ↔ C | **Absent for cost**; present for capacity only |
| A/B/C ↔ D | **Absent** — D does not exist |

> Level 5's central statement: **the reference system holds two complete truths and
> one half-truth, and builds no bridge between any of them.** SMEsPlus's proposition
> is precisely the bridges. That is a legitimate and well-evidenced differentiator —
> and it also means SMEsPlus is building the part nobody else has built, with the
> risks that implies.

## 3. Boss design hypotheses, tested against the evidence

### 3.1 Active depreciation feeding production cost — §57

**Hypothesis:** depreciation recognised in a period forms an eligible equipment
cost pool; productive usage carries it into WIP and then FG.

| Component | Verdict | Basis |
|---|---|---|
| A depreciation figure exists per period per asset | `FACT VERIFIED` | The posted entry |
| That figure can be attributed to a machine | **`DESIGN CANDIDATE`** | Requires the Asset↔Equipment link to be reliable — it currently is not (`19`) |
| A machine can be attributed to an operation | **`DESIGN CANDIDATE`** | `Operation → Equipment` does not exist (`08` §3) |
| Usage can carry the pool into WIP/FG | `FACT VERIFIED` **as machinery** | Links 2–6 exist (`08` §6) |
| Absorbed ≠ actual must be handled | **`VERIFIED GAP`** | `GAP-ABS-VAR` — nothing computes variance |
| Thai practice permits the absorption | **`UNRESOLVED`** | `UNR-03` |

**Consolidated:** the hypothesis is **coherent and buildable**, and three of its six
components are unbuilt. The cheapest correct sequencing is: fix the Asset↔Equipment
link first, add the equipment dimension to the operation second, derive the rate
third, and design variance handling fourth — **not** the other way round.

The Boss's own framing already contains the right caution: *depreciation cost pool
≠ automatically FG cost*. The evidence supports that caution — absorption depends
on actual usage, and unabsorbed depreciation must go somewhere. Nothing in the
reference system decides where. That is a **Boss policy decision**, recorded as
`UNR-18`, not a research finding.

### 3.2 Post-depreciation internal usage — §58–§61

**Hypothesis:** when financial depreciation completes, financial depreciation
becomes zero, residual book value is unchanged, and internal equipment usage cost
continues for as long as the machine produces.

| Component | Verdict | Basis |
|---|---|---|
| Financial depreciation stops at zero residual | `FACT VERIFIED` | The board's residual cap and end-of-lifetime override (`16` §6) |
| Residual book value is unchanged by depreciation | `FACT VERIFIED` | Salvage excluded from the base at the top of the engine (`18`) |
| The asset stays usable and visible afterwards | `FACT VERIFIED` — but see the caution | It stays `open`; there is **no "fully depreciated" state** to detect |
| Internal usage cost continues | **`DESIGN CANDIDATE`** | No precedent found in the reference system or in any accounting standard consulted |
| Residual is a **reference base**, not amortised | **`DESIGN CANDIDATE`** | Original construction |
| Cumulative internal usage may exceed residual | **`DESIGN CANDIDATE`, contested** | See `12` `FAIL-R05` and the AAS+ note in `11` |

**A finding the Boss should see before this design is finalised:** because there is
no "fully depreciated" state, **the trigger for switching an asset into internal
usage mode has to be constructed.** SMEsPlus cannot simply react to a status
change; it must detect the condition (residual reached zero, machine still in
production) itself, and define what happens if a later re-evaluation makes the
asset depreciable again. That re-entry case is not in the Boss's hypothesis and it
is a real path — `F09` can add value to a fully depreciated asset at any time.

### 3.3 The residual-derived internal usage rate — §59

**Hypothesis:** the internal usage basis derives proportionally from the original
depreciation rate — and, if the source is day-based, it must derive from a daily
basis, not a monthly one.

**The Boss's instruction not to hard-code monthly logic is correct and is now
proven necessary.** `16` §3 establishes that the system has *two* day conventions,
and `17` establishes that the correct one gives 1826-day lifetimes and month
amounts varying by 8%. A monthly-hard-coded internal rate would be wrong in exactly
the same way, every February.

Conceptually:

```
original daily rate  =  depreciable base ÷ actual lifetime days
internal daily basis =  residual book value × (original daily rate ÷ depreciable base)
                     =  residual book value ÷ actual lifetime days
```

which simplifies to **residual ÷ the asset's original lifetime in days**. Whether
that simplification is what the Boss intends is a design question, not a research
finding; it is recorded as `UNR-19`.

`DESIGN CANDIDATE`. No source precedent. No accounting-standard precedent.

### 3.4 Residual protection — §60

**`FACT VERIFIED` while running, with one boundary condition the design must
handle.**

Salvage is excluded from the depreciable base and no depreciation line ever touches
it. But **on closure the system subtracts salvage from book value**, and the
disposal entry writes out the **full original cost** against accumulated
depreciation, letting the residual fall into gain or loss. See `18` §6.

So residual is protected right up to derecognition and then absorbed. If the Boss's
design requires the residual to survive *as an identifiable amount* through
disposal, the reference behaviour does not provide it.

### 3.5 Off-balance — §62

| Boss statement | Verdict |
|---|---|
| Off-Balance is an account type | `FACT VERIFIED` — it is a real account classification |
| Customers can create their own accounts of that type | `FACT VERIFIED` |
| A Dr/Cr pair within off-balance can carry internal usage | **`DESIGN CANDIDATE`** |
| No cross-entry between off-balance and financial WIP/FG/expense | **Aligned with source, and stronger than the Boss stated it** |

The last row is the important one. The reference product **actively forbids
off-balance accounts on all three asset accounts by field domain** (`04` §2.5).
The boundary the Boss asked to be maintained by policy is, on the asset side,
already enforced by the product.

**What is not established:** whether off-balance accounts are permitted on the
work-centre expense account or anywhere in the valuation path (`UNR-17`), and
whether Thai statutory reporting tolerates the construction at all. Both open.

## 4. The semantic model SMEsPlus would need

Stated as a **model**, not a design, and derived from the four-truths analysis:

1. **One physical machine, one identity.** The reference system's split into two
   unlinked objects is the root defect. Everything else follows from it.
2. **The financial sub-ledger stays immutable.** Inherit catch-up + reverse +
   rebuild verbatim (`06` §3.2). Do not invent a mutable board.
3. **Value is a derivation, not a column.** Inherit that too (`04` §6).
4. **The day convention is an explicit decision, per company, recorded.** Not a
   default (`16` §3.4).
5. **The cost pool and the allocation driver are separate steps** — §48. The
   evidence supports the Boss's insistence here: the reference system's single
   hourly rate conflates them, and that is precisely why it cannot answer
   "which machine".
6. **Management truth is a separate ledger with a separate boundary.** It must not
   be able to reach financial book value. The reference product's own account-domain
   restriction is the precedent for enforcing that structurally rather than by
   policy.

## 5. Four Expert opinions

See `11_LEVEL5_FOUR_EXPERT_OPINIONS.md`.
