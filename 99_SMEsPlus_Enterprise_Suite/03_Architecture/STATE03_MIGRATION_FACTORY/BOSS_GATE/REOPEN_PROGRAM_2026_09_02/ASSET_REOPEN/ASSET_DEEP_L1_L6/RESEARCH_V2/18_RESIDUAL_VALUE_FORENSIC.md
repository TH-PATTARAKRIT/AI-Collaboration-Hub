# 18 — RESIDUAL VALUE FORENSIC
**LAYER 2 — AUDIT QUARANTINE**

Answers §25. The Boss's post-depreciation design rests on this deliverable, so
every claim is separated into what the source does and what remains a design
question.

## 1. Terminology — three different things share the word "residual"

| Term as used in the reference product | Meaning | Boss's usual word |
|---|---|---|
| **Not Depreciable Value** (`salvage_value`) | The amount excluded from the depreciable base | **Residual / salvage** |
| **Depreciable Value** (`value_residual`) | The amount still to be depreciated | "remaining to depreciate" |
| **Book Value** | Depreciable value + not-depreciable value + children | Net book value |

The product's *Depreciable Value* is a residual **in the mathematical sense** and is
not the Boss's residual. Whenever this package says "residual" without qualification
it means the Boss's — the not-depreciable amount. `04` §4 `UI-05` records the
resulting UI confusion.

## 2. Is the residual depreciated?

**No.** It is removed from the base before the engine ever sees it:

```
depreciable base = original value − not-depreciable value
```

Every board line is computed against that base. No depreciation line can touch the
residual. `FACT VERIFIED`

## 3. Does it remain in Book Value?

**Yes, for the whole life of a running asset.** Book value is
`depreciable value + residual + children`. When depreciation completes, depreciable
value reaches zero and **book value equals the residual exactly**.

Reproduced (`40` T08): 12,000 asset, 1,000 residual, 12 monthly periods, calendar-day
mode. Total depreciated = 11,000.00 across 12 lines. Final book value = 1,000.00.

`FACT VERIFIED` (source) + `SUPPORTED INTERPRETATION` (the numbers, `EV-SIM`)

## 4. Can it change mid-life?

Yes, through the modify wizard, and the behaviour is **asymmetric**:

| Direction | Behaviour |
|---|---|
| **Increase** the residual | The increase is capped at the current book value. Any excess above what can be taken from the depreciable value creates a **child asset** carrying the salvage increase |
| **Decrease** the residual | The freed amount returns to the depreciable base and is spread over the remaining life |

Both are bounded by:
```
new_residual = min(current_book_value − min(new_salvage, old_salvage), requested_depreciable)
new_salvage  = min(current_book_value − new_residual, requested_salvage)
```

The system will not let the two together exceed the asset's current book value.
`FACT VERIFIED`

## 5. After depreciation completes

The asset **stays `open`**. There is no "fully depreciated" state (`10` §3.2).
Depreciable value is zero, so the board loop's first guard exits immediately and no
further lines are generated. Book value sits at the residual indefinitely.

`FACT VERIFIED`

**This confirms the mechanical premise of the Boss's §58 hypothesis:** financial
depreciation stops, residual book value persists, and the asset remains a live
record. What is *not* provided is any signal that this has happened — no state, no
flag, no field, no report. SMEsPlus must detect the condition itself.

## 6. On disposal — the boundary condition the design must handle

This is the finding that most affects the Boss's design, and it has two parts.

**Part 1 — book value drops by the residual at closure.** The book-value computation
carries a second clause: when the asset is `close` **and** all its entries are
posted, the residual is subtracted. So the same field reads `residual` the moment
before closure and `zero` the moment after.

**Part 2 — the disposal entry writes out the full original cost.** The entry is:

```
Cr  Fixed asset account          original value          (the full gross cost)
Dr  Accumulated depreciation     depreciation to date
Dr/Cr  proceeds accounts         (sale only)
Dr/Cr  gain or loss account      the balancing difference
```

The residual is not written out separately. It is **the part of the original cost
that was never depreciated**, so it falls into the balancing difference — the gain
or loss.

### How to read this

Expert 3's characterisation, adopted after challenge at Level 6:

> **The derecognition is correct and standard.** Writing out gross cost against
> accumulated depreciation with the balance to gain/loss is the right treatment.
> What is non-obvious is that book value **also** silently drops by the residual at
> closure, so the gain/loss figure and the book value the user last saw are computed
> on different bases. That is a presentation inconsistency inside a correct
> accounting treatment.

There is a second, related inconsistency: the stored *net gain on sale* is computed
as `proceeds − book_value` **after** the state has already been set to `close`. So
it uses the post-closure book value, which excludes the residual, while the journal
entry's gain/loss includes it. **The stored figure and the posted figure can differ
by exactly the residual.** The stored one is invisible in the standard form (`04`
§3), so the discrepancy is not user-visible — which makes it more dangerous for a
downstream design that reads the field, not less.

`FACT VERIFIED` — book-value clause, disposal builder, and the ordering in the
closure routine. Recorded as `CTR-05`.

## 7. Residual and tax

Not separable. There is one residual, used for both book and tax, because there is
only one schedule (`12` §7). Royal Decree 145 does not prescribe a residual; Thai
practice commonly uses a nominal 1 baht per asset, which the engine handles
correctly (`40` T09).

`FACT VERIFIED` (engine) / `HOLD — EVIDENCE REQUIRED` (the statutory status of the
1-baht convention).

## 8. Consolidated answer to §25

| Question | Answer | Class |
|---|---|---|
| Is residual depreciated? | No — excluded from the base | `FACT VERIFIED` |
| Does it remain in book value? | Yes, while running | `FACT VERIFIED` |
| Can it change? | Yes, bounded, asymmetric | `FACT VERIFIED` |
| Can it change mid-life? | Yes | `FACT VERIFIED` |
| What happens after completion? | Book value = residual; asset stays `open`; **no state signals it** | `FACT VERIFIED` |
| Does the asset stay active? | Yes | `FACT VERIFIED` |
| Does residual remain indefinitely? | Yes, until derecognition | `FACT VERIFIED` |
| How is it used at disposal? | **Absorbed into gain/loss**; book value drops by it at closure | `FACT VERIFIED` |
| Relation to tax? | None — one schedule only | `VERIFIED GAP` |
| Accounting vs tax vs internal-usage residual | **Not separated by the product.** Separating them is SMEsPlus original | `DESIGN CANDIDATE` |

## 9. What SMEsPlus must decide

1. Whether the residual must survive disposal as an **identifiable** amount. The
   reference behaviour does not provide that.
2. Whether the management ledger's residual reference base is the **financial**
   residual or an independent figure. If financial, it disappears at disposal
   (`FAIL-R08`) and the management ledger loses its reference.
3. What happens to accumulated internal usage at disposal — unaddressed in the
   Boss's hypothesis, raised by Expert 3 at Level 5.
