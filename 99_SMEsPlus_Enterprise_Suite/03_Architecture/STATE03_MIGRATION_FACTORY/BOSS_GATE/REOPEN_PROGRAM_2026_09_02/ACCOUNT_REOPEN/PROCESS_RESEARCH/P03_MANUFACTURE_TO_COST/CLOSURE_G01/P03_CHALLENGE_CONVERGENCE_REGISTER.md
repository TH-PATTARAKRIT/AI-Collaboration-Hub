# P03 — CHALLENGE CONVERGENCE REGISTER

**LAYER 2 — AUDIT QUARANTINE.** Four AAS-03 challengers. Dissent preserved; consensus not
forced. Per `smeplus-adversarial-section-not-summary-rule`, **§5 is the citable output.**

Three mandated disproof attempts, each run to succeed.

---

## 1. MANDATED — disprove *the current explanation of `P03R-F-01`*

**Challenger: Leadership Database Design (E2). PARTIALLY SUSTAINED — and it corrects P03.**

**The attack.** P03's explanation now rests on P01's naming of
`purchase_stock::_get_price_unit` and its three defects. **P03 has never read that code.** The
series-16 tree does not exist in P03's path set (`MD-01`, `MD-06`). P03 is therefore accepting
a peer's **source** claim about a tree it cannot open — precisely what
`smeplus-peer-intake-discipline` warns against, and what `smeplus-independent-review-false-negative-lesson`
says must be verified rather than inherited.

**What survives, and what does not:**

| Component of the explanation | Basis | Verdict |
|---|---|---|
| The **event family** — a vendor goods receipt is where the break first appears | **P03's own measurement**: `WH/IN/03634`, unit 31 → 712,186.25, with ordinary receipts at ~30 interleaved on the same days | **HOLDS — P03-owned** |
| The **compounding** — average costing escalates it to 5.2 × 10¹⁶ over five days | **P03's own measurement** | **HOLDS — P03-owned** |
| Manufacturing is the **amplifier, not the origin** | **P03's own attribution** of the 30 rows, 18 manufacturing-origin | **HOLDS — P03-owned**, and independently confirmed by P01's withdrawal |
| The **specific function and its three defects** | **P01's read of a tree P03 cannot open** | **INHERITED, NOT VERIFIED** |
| The **18 zero-`qty_received` lines** | P01's measurement | **INHERITED, NOT VERIFIED** |

> **Correction `CC-01`.** P03 must state the origin mechanism as **attributed to P01, not
> verified by P03**, and must not present it as a P03 finding. The event-family attribution
> is P03's and stands on its own data.

**E2's residual dissent, preserved:** two sessions agreeing does not make a claim verified when
one of them supplied the only source read. `smeplus-shared-blind-spot-agreement` applies.

## 2. MANDATED — disprove *the current interpretation of the valuation-layer filter chain*

**Challenger: Lead Code & UI Architect (E4). PARTIALLY SUSTAINED — two corrections.**

**Attack 1 — the instruments are not independent.** P03 claims its series-18 result
"independently corroborates" P01's series-16 result. **Both used the same probe**:
`def _get_stock_valuation_layers`. A participant that intervened by a different mechanism —
a differently-named method, a monkeypatch, an `_inherit` that replaces rather than filters —
would be **invisible to both**. This is `smeplus-shared-blind-spot-agreement` exactly: three
instruments once agreed on 39 because all three shared one pattern.

> **Correction `CC-03`.** The corroboration is real but is **pattern-bounded**: two trees,
> **one probe**. P03 states the bound rather than claiming independence it does not have.

**Attack 2 — "removed in series 19" overstates.** **SUSTAINED.** The mechanism was
**restructured**; `property_price_difference_account_id` still exists on the product category
in v19. Corrected in place as `CC-02`.

**Attack 3 — is the MRO/commutativity claim P03's or P01's?** It is **P01's reasoning**, which
P03 re-derived structurally: `.filtered()` narrowings commute and cannot reintroduce. **P03
verified the two overrides are narrowings in series 18** and can assert commutativity for that
series on its own evidence. **NOT DISPROVED.**

## 3. MANDATED — disprove *the current fixed-overhead injection-gap conclusion*

**Challenger: Leader Functional Design (E1). NOT DISPROVED — and the conclusion is split.**

**The strongest attack:** P03 read series 18; the deployment runs series 16. A fixed-overhead
path could have existed in 16 and been removed by 18. P03 cannot exclude it.

**Sustained for the source half, and it forces a split:**

| Half | Status |
|---|---|
| *No fixed-overhead mechanism exists in the source read* | **bounded to series 18/19** — cannot be asserted of series 16 |
| *No fixed-overhead cost is exercised in any of the four deployments* | **version-independent** — measured in the databases themselves. **Survives entirely** |

**E1 pressed a second line and failed:** if `mrp_maintenance` and `hr_hourly_cost` were absent
from the read, the negative would be weak. They are **installed** in two deployments and still
supply no path — which **strengthens** the measured half.

> **Correction `CC-04`.** The fixed-overhead conclusion is restated as two claims with
> different evidence bases, not one. The measured claim is the load-bearing one.

## 4. Fourth challenger

**Lead Integration & Localization (E3).**

| Report | Content |
|---|---|
| **SUPPORTED** | The P01 intake is complete and the supersession check was performed correctly — the base handoff is *newer* than the correction delta, and reading only the later-named file would have been an error |
| **MISSING** | P03 never established **which deployment SMEsPlus must migrate**. Every conclusion is about four databases whose relevance is unestablished — `UNR-P03-10`, open since round 3 |
| **RISKY** | P03 accepted P01's series-16 evidence while unable to open series-16 source. Correct as intake; **risky as foundation** |
| **CHALLENGED** | *"`iTEST02` is a test system"* rests on 32 GL lines and an absent valuation table. That is strong, but P03 never read `ir_default` for the company-dependent valuation fallback (`UNR-P03-18`) |
| **EVIDENCE NEEDED NEXT** | A series-16 addons tree. It settles `MD-01`, and nothing else does |

## 5. Corrections carried forward — the citable output

| ID | Correction | Effect |
|---|---|---|
| **`CC-01`** | The `P03R-F-01` origin **mechanism** is **attributed to P01, not verified by P03**. Only the event-family and amplification halves are P03's | Attribution corrected throughout `P03_VALUATION_GL_DIVERGENCE_CLOSURE.md` |
| **`CC-02`** | *"Removed in series 19"* → **restructured**; the price-difference account survives | Corrected in place |
| **`CC-03`** | The 16-vs-18 chain corroboration is **pattern-bounded** — two trees, one probe — not instrument-independent | Bound stated |
| **`CC-04`** | The fixed-overhead conclusion **splits** into a version-bounded source claim and a version-independent measured claim | Restated as two claims |

**Four corrections. All four are P03's own overstatements**, and three were produced by the
mandated disproofs rather than by P03's own reading.

## 6. Convergence

Two further challenge passes were run against the corrected answers. **No new material A/B
delta emerged**: the residual objections (E2 §1, E3 "MISSING"/"CHALLENGED") all reduce to
`MD-01` and `UNR-P03-10`/`UNR-P03-18`, which are **named holds with named owners**, not
unexplored paths.

> **Convergence reached.** The recursion stops because every surviving objection is a
> *declared unavailable evidence item*, not a search that has not been run.
