# 57 — BIDIRECTIONAL COST-INTEGRITY TEST

**LAYER 2 — AUDIT QUARANTINE.**

> **TEST A — can one economic cost be counted twice?**
> **TEST B — can one economic cost be lost entirely?**
>
> A costing model may not be certified on TEST A alone.

---

## 1. Results per cost type

| Cost | TEST A — duplicable? | TEST B — losable? | Observed in the deployed data |
|---|---|---|---|
| **Direct material** | latent, via `M7` + `M10` | **YES — observed** | 49 finished moves unvalued, 280 valued zero, 1,386 consumptions unvalued (`P03R-F-02`) |
| **Machine / work centre** | **YES — latent** (`DC-01`, `DC-06`) | **YES — observed** | zero in `iSMEs`; 59 of 60 unrated in `iTEST02` |
| **Direct labour** | **YES — latent** (`DC-02`) | **YES — observed** | 0 of 27 time logs carry a cost |
| **Depreciation** | no path | **YES — total** | never reaches inventory in any database |
| **Maintenance / energy / indirect labour / overhead** | no path | **YES — total** | never reaches inventory |
| **Extra unit cost** | residue (`DC-03`) | no | 0 of 10,927 orders |
| **Analytic attribution** | **YES — latent** (`DC-14`, `M4`+`M5`) | **YES** — netting (`33`, P09) | neither fires; 0 distributions |
| **Finished-goods value** | — | **NO — the opposite: EXPLOSION** | 30 rows to ±10²¹ (`55`) |

## 2. The result

> **`P03R-F-07`. Every conversion-cost element fails TEST B. Six of eight cost types can
> also fail TEST A. And one — finished-goods value — fails in a third direction the test
> pair does not name: it *explodes*.**

**TEST A passes almost everywhere in the live data, and that is worthless as assurance.**
Nothing duplicates because almost nothing is costed. A certification based on TEST A would
have declared this model sound while inventory sat at material cost only, with a −48.7 %
valuation distortion inside it.

## 3. The third failure mode the directive's pair does not cover

TEST A and TEST B are a two-sided test around a correct value: *counted twice* or *lost*.
`55` documents a third: **the value is present, unique, and wrong by eighteen orders of
magnitude**, because the mechanism faithfully propagated a corrupt input.

> **A cost-integrity test pair that asks only "twice or zero?" cannot detect
> "once, and absurd".**

`R-17` (magnitude validation) is the requirement this generates, and `71` records it as the
most important design implication of the entire P03 package.

**Proposed for SMEsPlus and not adopted here — TEST C: is the amount plausible against the
cost object's own history?** `DESIGN CANDIDATE`.

## 4. Bidirectional summary by database

| | `iSMEs` | `iTEST02` |
|---|---|---|
| TEST A failures observed | **0** | **0** |
| TEST A failures latent | 7 | 7 |
| **TEST B failures observed** | **conversion cost entirely; 49+280+1,386 material gaps** | **conversion cost entirely — periodic valuation, no valuation layers** |
| TEST C failures observed | **30 rows, ±10²¹, −48.7 %** | none — no valuation table |

**Neither database passes.** They fail differently, and only running both tests in both
databases shows it.
