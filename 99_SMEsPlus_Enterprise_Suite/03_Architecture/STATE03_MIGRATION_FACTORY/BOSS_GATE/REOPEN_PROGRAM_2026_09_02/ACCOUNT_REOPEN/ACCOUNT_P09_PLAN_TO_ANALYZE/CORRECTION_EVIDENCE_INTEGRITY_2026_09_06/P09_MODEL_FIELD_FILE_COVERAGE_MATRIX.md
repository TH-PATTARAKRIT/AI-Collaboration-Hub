# P09_MODEL_FIELD_FILE_COVERAGE_MATRIX

**Prompt:** `SMEPLUS-26-09-06-P09-P2A-EVIDENCE-INTEGRITY-TARGETED-CORRECTION-003` · **PHASE S** · **AI EOS = OFF**
**Layer:** 1 — clean-room. Module and file identifiers are held in Layer 2 (`E03`); this matrix carries the structure and the measured counts.

---

> ## ⚠ CORRECTED AFTER INDEPENDENT CHALLENGE
> Statements here were **contradicted by the four AAS-03 challenges and re-verified against source by the author before adoption.** Corrections are inline; superseded wording is retained. Full list: `P09_AAS03_CORRECTION_CHALLENGE_RECORD`.

---

## 1. THE MATRIX SHAPE

`declared root → file → model declared or extended → material field / function → P09 semantic role → domain ownership`

Every row is a **file**, because ownership is a property of the file (`P09_CORRECTED_EVIDENCE_POPULATION_REGISTER` §4).

---

## 2. THE P09-OWNED FILES — 10 files, 3 modules

| # | Owning module class | Model(s) declared | Fields | Methods | P09 semantic role |
|---|---|---|---|---|---|
| 1 | analytic | dimension value | 13 | 8 | the axis member — identity and classification |
| 2 | analytic | assignment rule | 4 | 6 | pre-fills an allocation from master data |
| 3 | analytic | **management record**, plus a plan-column mixin | 13 | 13 | **the P09 fact table** |
| 4 | analytic | the allocation mixin | 3 | 15 | allocation carrier and its arithmetic |
| 5 | analytic | the axis, and the obligation rule | — | — | the axis itself; whether it must be filled |
| 6 | plan | plan header | 10 | 9 | intended amount, state, revision lineage |
| 7 | plan | plan line | 17 | 7 | intended / achieved / committed / theoretical |
| 8 | plan | plan report model | 12 | 5 | the consumption query |
| 9 | plan | plan split wizard | 4 | 2 | splitting an intended amount |
| 10 | **financial reporting** | **a SECOND planning family — header and item** | 8 | 5 | **an account-keyed intended amount — previously unenumerated** |

**Row 10 is the correction.** It sits in a module whose other ~30 files extend report, ledger, partner and company models — an adjacent-domain module carrying one P09-owned file.

---

## 3. THE EXTENDING FILES — ~~39 files, 27 modules~~ **42 files, 26 modules** *(corrected)*

These are **producers and consumers writing into P09's surface**. They are P09 **evidence facts**. They are **not** P09-owned, and **no adjacent-domain internal lifecycle was researched**.

Measured per model, unit = file *(a file may extend more than one model, so the column sums above 42)*:

| P09 model extended | Files | What this tells P09 |
|---|---|---|
| **the management record (fact table)** | ~~16~~ **17** | **CORRECTED — an off-by-one inside the author's own population**, independent of the population defect |
| the dimension value | 8 | producers attach their objects to the axis member |
| the obligation rule | 7 | domains declare whether the axis is mandatory in their context |
| the allocation mixin | ~~7~~ **10** | **CORRECTED** — understated by 43 %; three carriers sat in non-first list positions |
| the plan-column mixin | **1** | **ADDED — this row was absent from the published matrix** |
| the axis | 1 | |
| the assignment rule | 1 | |
| the plan header | 1 | a project-side extension |
| the plan line | 1 | a project-side extension |
| the second planning family | **0** | **nothing extends it** |

**The count that matters: P09 owns one file that declares its fact table, and the estate holds ~~sixteen~~ SEVENTEEN that reshape it.** That ratio is the structural statement of P09's position — it owns a surface that seventeen other files author into.

**Nothing *inherits* the second planning family** — confirmed independently by two challengers. **But *"self-contained"* is `CONTRADICTED`**: an adjacent master model carries a **reverse relation** into its item collection. The true statement is narrower than the one published — *nothing extends it by inheritance; it is referenced from outside.*

---

## 4. FIELD / FUNCTION LAYER — WHERE THE CORRECTION BITES

| Surface | Corrected fact |
|---|---|
| plan header | **5 states, not 4**; the fifth carries a deletion path (previously corrected, re-confirmed here) |
| plan header | the company field is **required and defaulted** in the root read |
| plan line | 17 fields — intended, achieved, committed, theoretical, each with a percentage, plus the over-plan boolean |
| **second planning family header** | `name` required, `company_id` **required**, an item collection |
| **second planning family item** | **`account_id` required — a specific account**; `amount` is a **plain float with no currency**; a **single required date**, not a window |
| over-plan computations | **3**, of which **2 sit in P09-authored files attached to an adjacent-domain carrier** |

---

## 5. WHAT THE MATRIX DOES NOT COVER

| Blind spot | Class |
|---|---|
| models reached by a variable-held name or **raw SQL** | **CLASS CORRECTED: A — measured. 12 files in 3 unseen modules** |
| P09 semantics on a carrier that **does not declare or inherit** a P09 model | **CLASS CORRECTED: A — measured. 164 files across 51 modules** |
| non-source carriers (views, data files) | **C — not searched** |
| roots outside the declared one | **B — boundary declared, not chased** |

**The second blind spot is the honest residue of the correction**: fixing a name-based instrument with a model-based one trades one blind spot for another. Both must be run; neither alone is complete.
