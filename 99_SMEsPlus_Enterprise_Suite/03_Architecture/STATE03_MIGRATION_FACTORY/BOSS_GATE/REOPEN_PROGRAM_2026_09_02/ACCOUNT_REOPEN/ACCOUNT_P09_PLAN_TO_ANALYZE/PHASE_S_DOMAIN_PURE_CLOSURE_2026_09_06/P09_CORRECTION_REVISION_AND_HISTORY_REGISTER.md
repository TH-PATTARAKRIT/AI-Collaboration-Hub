# P09_CORRECTION_REVISION_AND_HISTORY_REGISTER

**Prompt:** `SMEPLUS-26-09-06-P09-P2A-DOMAIN-PURE-BOUNDED-CLOSURE-002` · **Phase S** · **AI EOS NOT ACTIVE**
**Layer:** 1 — clean-room. **Answers `CQ-P09-07` and `CQ-P09-08`.**

---

> ## ⚠ CORRECTED AFTER INDEPENDENT CHALLENGE
> Statements in this file were **contradicted by the AAS-03 challenges and re-verified against source by the author before adoption.** Corrections are marked inline; superseded wording is retained. The full list is in `P09_AAS03_INDEPENDENT_CHALLENGE_RECORD`.

---

## 1. THE PLANNING STATE MACHINE, AS EVIDENCED

| Stored value | Caption | Meaning |
|---|---|---|
| `draft` | Draft | being prepared |
| `confirmed` | **"Open"** | in force |
| `revised` | Revised | superseded by a successor |
| `done` | Done | finished |
| **`canceled`** | **Canceled** | **ADDED AFTER CHALLENGE — this state was MISSED, and it is the consequential one** |

> **CORRECTION — THERE ARE FIVE STATES, NOT FOUR, AND THE FIFTH CARRIES A DELETION PATH.**
> A cancel action sets `canceled`, and the unlink guard permits **deletion of a plan in `draft` or `canceled` only**. So a plan can be cancelled and then **destroyed**.
> **A destruction path for a management plan was absent from the register whose subject is correction and history.** That is the substantive miss; the miscount is the smaller half of it.
> Worse: the generation control then re-published the four-state vocabulary as **invariant across generations**, *converting a miscount into a claim of robustness*. A control that repeats an error confirms the error.

**CR-R8 (added) — Cancellation and deletion of a plan shall be separate, and a plan that any actual has ever consumed shall not be deletable at all.** The evidenced behaviour permits cancel-then-delete, which destroys management intent while its consumption history survives elsewhere.

**CR-01 — ~~One state's~~ TWO fields' stored values and captions disagree.** A systematic scan of every selection declaration in the four modules returns **two** divergences, not one; the second is on the obligation object this package treats as P09-owned (EV-P09-209 §10.3). The value is `confirmed`; the label reads "Open". Any P09 requirement must name the **stored value**, because a caption is not behaviour. This is the programme's *UI label vs executable behaviour* rule materialising inside P09's own vocabulary (EV-P09-204).

---

## 2. WHAT CHANGES WHEN EACH THING CHANGES

The prompt asks what happens when plan, forecast, actual reference, dimension or assumption changes.

| What changes | Evidenced behaviour | Consequence |
|---|---|---|
| **the plan amount** | remains writable after confirmation — the lock is a **view attribute**, not a server guard | the revision object can be **bypassed entirely** |
| **the plan, by revision** | a successor is created; confirming it flips the predecessor to `revised` | lineage preserved, one plan live at a time |
| **the forecast** | ~~**NO OBJECT EXISTS**~~ → **NOT FOUND IN THE FOUR MODULES SEARCHED** | **CORRECTED.** The original wording was an unbounded negative — the exact restatement this package forbids one file away. A `*forecast*` module carrying a stored intent/achieved/ratio triple, joined to the management fact table, exists in the same root (EV-P09-208 §9.7) |
| **the actual reference** | actuals are **recomputed on every read**, never stored | a closed period's consumption can change silently, retrospectively |
| **the allocation on a posted fact** | freely editable — absent from every lock-date list, every integrity-hash list, and the tracked-field set; no chatter entry, no tracking value, no hash break | **management truth has no period control** |
| **the dimension structure** | re-parenting an axis rewrites historical records by direct statement; deleting one drops the column and its history | **management history is silently mutable and destructible** |
| **the assumption** (e.g. which accounts a plan governs) | governed by account **type** only, resolved inside the reporting query | changing a chart's typing changes past plan consumption |

**CR-02 — ~~Five of seven~~ FIVE OF SIX eligible changes rewrite history with no trace.** *(Corrected: the seven-row denominator included "the forecast", which is not a change and cannot rewrite history — an ineligible member in an author-chosen denominator.)* Only the plan revision preserves lineage, and it is the one a user can bypass.

---

## 3. THE COMPOSITE CORRECTION FINDING

Stated once, plainly, because it is the most consequential thing P09 knows about correction:

> **After a period is closed and its entries are hashed, the management allocation of every posted amount in that period remains freely editable by any holder of the analytic group, without audit — and every plan-consumption figure over that period changes silently as a result.**

This round did **not** re-research it; it is held from prior evidence and is unchanged. It is restated here because `CQ-P09-08` asks the question it answers.

---

## 4. WHAT CORRECTION AND REPLANNING MUST MEAN

`CANDIDATE PROCESS SEMANTIC` — meaning only.

| # | Requirement |
|---|---|
| **CR-R1** | a confirmed plan amount shall be **immutable**; change shall occur only by revision |
| **CR-R2** | a revision shall carry the reason, the author and the date, and shall be a dated event rather than a copy |
| **CR-R3** | period close shall bind management truth exactly as it binds ledger truth |
| **CR-R4** | correction in a closed period shall be a **dated reallocation event in an open period**, carrying a reference to the record it corrects — never an in-place edit |
| **CR-R5** | an axis shall be **retirable, never deletable**, once any record references it; re-parenting shall be a versioned operation with an audit record |
| **CR-R6** | a plan-consumption figure presented for a closed period shall be **stored and re-derivable to the same value** |
| **CR-R7** | scenario alternatives and revision successors are **different objects** and shall not share a mechanism |

---

## 5. WHAT HISTORY MUST BE PRESERVED FOR PHASE SA

The prompt requires preserving evidence for a later Strengthening recheck **without retrofitting it now**. Recorded, not acted on:

| Preserve | For which PHASE SA control |
|---|---|
| the four planning states and the caption mismatch | semantic integrity |
| the revision parent/child structure and its bypass | exception / reversal / correction |
| the mutability of allocations after close | financial integrity |
| the three time bases and the unstored figures | testability / evidence |
| the scope determinations and `S12` | scope / ownership |
| the sign convention and the aggregation widening | reconciliation readiness |

**No PHASE SA control was executed, scored or retrofitted in this round.**

---

## 6. DISPOSITIONS

| ID | Disposition |
|---|---|
| `CR-01`, `CR-02` | `FACT VERIFIED — CLOSED FOR CURRENT P09 EVIDENCE` |
| the composite correction finding | `FACT VERIFIED — CLOSED FOR CURRENT P09 EVIDENCE` |
| `CR-R1` … `CR-R7` | `BOSS DECISION REQUIRED — DECISION PACKAGE READY` |
| forecast-change behaviour | **CORRECTED** → `UNRESOLVED — SPECIFIC P09 EVIDENCE UNAVAILABLE`; the earlier `no object exists` disposition is **withdrawn** |
