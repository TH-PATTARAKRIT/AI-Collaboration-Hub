# ACCOUNT WAVE A — FINAL BALANCED-BUT-WRONG REGISTER

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-FC-001` · Layer 1 clean-room
Canonical source: `MCC_00` §1 and `MCC_G_BALANCED_BUT_WRONG_FIXED_POINT_PROOF.md`.

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. Position — unchanged by this round

| Figure | Canonical | This round |
|---|---|---|
| Classes searched | **19 of 19** | unchanged |
| Register floor, **established** under `MCC_G` §1's four-question test | **32** | unchanged |
| Register floor, **asserted** (test not applied to 4 cases) | **36** | unchanged |
| Cases added by this round | — | **0** |
| Cases withdrawn by this round | — | **0** |

**This round did not open the balanced-but-wrong surface.** It re-verified two members
(`BW-31`, and `BW-30`'s mechanism) and added none. Reported as scope, not as stability.

---

## 2. Members re-verified this round

| id | Case | Result |
|---|---|---|
| `BW-31` | v19 aggregates monetary columns **at today's rate**, outside every record rule, with a par fallback | **REPRODUCED EXACTLY** from `odoo/orm/models.py` `_read_group_select`. Constructed SQL read directly: raw `FROM "res_currency_rate"`, `COALESCE(rate, 1.0)`, `today = Date.context_today(self)`. **Not a new finding — a repeatability datum** |
| `BW-31` reachability | *"every monetary field, list + pivot + graph, opt-out not opt-in"* | **REPRODUCED EXACTLY** at `relational_model/utils.js:545`, `pivot_model.js:1088`, `graph_model.js:337`; single-currency discard confirmed at `utils.js:596`, `pivot_model.js:992` |
| `BW-28a` | Consolidating root holds no rate row for a subsidiary's functional currency → that subsidiary's **entire** balance sheet and income statement are affected | **NOT RE-TESTED this round.** Stands on `MCC_J` `J-01`/`J-04` |

---

## 3. The class that still has no cell

> ### `T0-12` — `unbalanced-and-posted`
>
> The taxonomy classifies **balanced** ledgers that are **wrong**. `T0-12` establishes a ledger that is
> **not balanced** and **is posted**. **There is no cell for it, and this round did not create one** —
> creating a taxonomy cell without enumerating its members would be the empty-class error `ER-CORE-4`
> exists to prevent, and that error has a **2-of-2 record** of the empty class turning out to contain a
> verified defect on first search.
>
> **The correct next action is to search it, not to classify it.** Named as a Wave A residual.

---

## 4. Third finding class, proposed by this round

Neither *balanced-but-wrong* nor *declared-but-inert* covers `FC-F1`:

| Class | Definition | Example |
|---|---|---|
| **balanced-but-wrong** | The ledger reconciles and the number is wrong | `BW-01`…`BW-36` |
| **declared-but-inert** (`T0-09`) | A control is present to a reader and absent to the machine | 16 company-consistency guards |
| **`executed-and-wrong` — NEW** | A control **executes**, **is read by every consumer**, and is **itself wrong** | **`MCC_00`** — the canonical figures register that governs every published figure, whose §1 contradicts its own §2 |

**Proposed, not asserted.** It has **one** member. Per `ER-CORE-4` a class with one member is a
hypothesis; it is recorded so the next round searches it rather than assuming it is unique.
