# S11 — P09_ZEROING_DOUBLE_COUNTING_INTERACTION

**Checkpoint:** `CP-P09S11` · **Layer:** 1 — clean-room.

---

## 1. THE FIVE QUESTIONS

| Question | Answer |
|---|---|
| same event? | **No.** Zeroing is an asset/accrual/cash-basis event; the duplication is a manufacturing duration change |
| different events? | **Yes** — they are independent mechanisms with no shared code path |
| configuration-dependent? | **Both.** Zeroing needs the source object to carry an allocation; duplication needs two allocations to name the same axis value |
| can they offset accidentally? | **Yes — on a shared axis value.** Zeroing removes cost that duplication adds back |
| can they conceal each other in reports? | **Yes, and this is the finding** |

## 2. THE CONCEALMENT

Both mechanisms terminate at the **same object** — an axis value's balance and its consumption figures. Neither carries a marker distinguishing its contribution.

```
axis value "Production Cost Centre"
   ├─ depreciation      → +X and −X   → net 0        (cost that should be there, and is not)
   └─ machine duration  → −Y and −Y   → net −2Y      (cost counted once too often)
                                        ─────────
                          reported     −2Y, and it looks like a plausible machine cost
```

**A reviewer checking totals finds nothing wrong.** The figure is non-zero, of plausible magnitude, and internally consistent. **Net-total correctness is not evidence of semantic correctness** — the directive's own warning, now demonstrated with two independently verified mechanisms.

## 3. WHY THIS IS NOT SPECULATION, AND WHERE IT STOPS

| Element | Status |
|---|---|
| the zeroing mechanism | **FACT VERIFIED**, and **measured** in a live deployment |
| the duplication mechanism | **FACT VERIFIED in source**, **unexercised** in every deployment measured |
| both reaching one axis value | **structurally possible — no bar, purely configuration** |
| **the two co-occurring in any real deployment** | **NOT OBSERVED.** The deployment with the zeroing has **no** manufacturing analytic records at all, and the bridge module is not even installed |

> **The interaction is real as a design property and has not been observed to occur.** Stated that way and no stronger.

## 4. THE PRIOR VERSION OF THIS SECTION IS SUPERSEDED

An earlier round argued a masking interaction between depreciation and machine-hour rates, on the premise that such rates recover ownership cost. **That premise was uncited and was withdrawn.** The interaction described here is a **different** one — between two *verified* mechanisms rather than between one mechanism and an assumption — and it needs no costing-policy premise.

## 5. WHAT THIS REQUIRES OF SMEsPlus

**AI-X-01.** Every management record shall carry the **mechanism** that produced it, as data. Without it, no report can decompose a cost-centre figure into its contributions, and no reviewer can detect either defect from the total.

**AI-X-02.** A cost-centre figure shall be **decomposable by mechanism on demand**. A single scalar that several mechanisms write into, with no attribution, cannot be audited — and both defects here are invisible precisely because it is one.

## CHECKPOINT

**`CP-P09S11` — COMPLETE — EVIDENCE VERIFIED.** Interaction established as a design property; co-occurrence explicitly not observed. Auto-continue.
