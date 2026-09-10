# 04 — E2E COMPOSITION CLOSURE

## `SHIP → INVOICE → RETURN-AFTER-CLOSE → DOWNSTREAM-CONSUMED`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-CORRECTIVE-CLOSURE-001]` · Boss: **SOLE FINAL APPROVER**

> **§7: the three open items must become individually traceable. No aggregate *"covered"* statement.**

---

## 1. The three open items, separated

| Item | Claim | Status **now** | Delta since `PT-09` |
|---|---|---|---|
| **O-1** | Correction after a completed movement — **the only route is a return; the corrected-entry link does not exist** | **OPEN** | none |
| **O-2** | The return's **value basis** | **CLOSED — `JT-05` = ORIGINAL COST** (`SC-BD-05`, `2 of 2`) | **MATERIAL — it was open at `PT-09`** |
| **O-3** | **Reversal after a downstream module has consumed the output** | **OPEN — no representation anywhere** | none |

**`1 of 3` closed by a Boss ruling this round resolved; `2 of 3` remain.**

---

## 2. Transition-by-transition

| # | Transition | Business semantic | Source event | Ownership | Accounting impact | Inventory impact | Document lifecycle | Period-close behaviour | Reversal behaviour | Downstream consumer | Reconciliation proof | Exception path | Audit evidence | Status |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **T1** | **SHIP** | goods leave; **COGS recognised at the physical movement** (`JT-04` RULED) | movement posted | Inventory = Stock Truth | **COGS + revenue-side cost binding** (`XMC-C-C6`) | on-hand ↓, reservation released | delivery record | pre-close | reversible by return only | Accounting; AR | el.`3`+`4` both carried | short-ship → partial | movement + event | **WRITABLE** |
| **T2** | **INVOICE** | commercial claim | invoice posted | Accounting = Financial Truth | AR + revenue + **tax** | none | invoice | pre-close | credit note | AR; Tax | invoice ↔ movement | `H-05` **draft invoice consumes billable qty, posts nothing, freely deletable** | entry | **WRITABLE with named defect** |
| **T3** | **PERIOD CLOSE** | period locked | close run | Accounting | closing position | valuation summary | period object **specified `XMC-C-A15`** | **lock binds the ENTRY, not the path (`ND-07`)** | — | GL; reporting | `0` proven | **two lock-defeat paths (`PT08-F-02`)**, one leaving **no record of any kind** | close record | **`PTE-3` + DEFECT** |
| **T4** | **RETURN AFTER CLOSE** | goods come back **into a closed period** | return movement | Inventory | **reversal at ORIGINAL COST (`JT-05` RULED)** | on-hand ↑ | return doc + **reversal event referencing the original** (`XMC-C-A8`) | **UNSPECIFIED — the composition gap** | new event; **original unchanged byte-for-byte** | Accounting; Tax | **`H-07` matching rows are FREELY DESTRUCTIBLE across a closed period, and cash-basis tax keys off it** | **`O-1`: correction must become a return; corrected-entry link DOES NOT EXIST** | reversal event | **`HOLD` — `O-1`** |
| **T5** | **DOWNSTREAM-CONSUMED** | another module already consumed T1/T2's output | consumer's own act | consumer module | **UNSPECIFIED** | **UNSPECIFIED** | **UNSPECIFIED** | **UNSPECIFIED** | **UNSPECIFIED** | **UNKNOWN** | **none** | **`O-3`: no representation anywhere** | **none** | **`HOLD` — `O-3`** |

---

## 3. `CC-F-04` — the three defects compose into one unrecoverable state

**Each is separately recorded. Composed, they describe a business event with no defined outcome:**

1. **T4 × `O-1`** — a post-close correction **must** become a return, and the corrected-entry link that
   would tie the return to the original **does not exist**.
2. **T4 × `H-07`** — the reversal must leave the original *"unchanged byte-for-byte"* (`XMC-C-A8`,
   `PTX-03`), while the settlement matching it depends on is **freely destructible across a closed
   period**. **The reference survives; the fact it points at may not.**
3. **T5 × `O-3`** — if a downstream module already consumed the output, **there is no specified behaviour
   at all**.

> **Composed: goods ship, are invoiced, the period closes, the customer returns them, and a downstream
> module has already consumed the original fact. The value basis is now ruled. Everything else about that
> state is undefined — and it is an ordinary SME transaction, not an edge case.**

**`JT-05` closing `O-2` is real progress and it does not close the composition:** knowing a return
reverses at **original cost** does not say **how the original is found** (`O-1`), **whether it still
exists** (`H-07`), or **what the downstream consumer does** (`O-3`).

---

## 4. Checkpoint

> **`3` items individually traced across `5` transitions; **`0` aggregate statements** · **`O-2` CLOSED by
> `SC-BD-05` = original cost** · `O-1` and `O-3` **OPEN** · `CC-F-04`: the composition remains
> undefined, and the newly-ruled value basis does not reach the three mechanisms that make it usable ·
> **`T4` and `T5` = `HOLD`.**

