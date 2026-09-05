# P01 — LANDED COST ACCOUNTING TRACE

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.** Landed cost was **outside** the previous round's module denominator (`ERR-P01-04`);
this is its first P01 trace.

---

## 1. STATUS

| | |
|---|---|
| In the P01 dependency closure | **yes** — added by the transitive correction |
| Installed | **in all four databases** |
| **Exercised** | **zero landed-cost records in any of them** (positive control printed by the expert) |
| Therefore | **INSTALLED, NEVER USED** |

That combination is the finding: a capability switched on everywhere and used nowhere, whose
defects are consequently **latent but armed**.

---

## 2. THE CHAIN

| Step | Effect |
|---|---|
| Business source | additional costs — freight, duty, handling — to be absorbed into the value of received goods |
| Allocation basis | across the receipt lines it is applied to |
| Inventory effect | the receipt's value is increased |
| Valuation effect | v18 adjusts the valuation layer; **v19 has no valuation layer**, so the adjustment lands differently |
| Journal effect | an adjustment entry, **subject to the same account resolution that resolves to nothing in the v19 deployments** |
| AP effect | the vendor's freight bill is an ordinary vendor bill; landed cost only re-allocates its value |
| Period effect | see §3 |

---

## 3. THE DEFECTS FOUND

### `LC-01` — v19 books only what is still on hand, and says nothing about the rest

v19 apportions the cost by remaining quantity. **If the goods have already been sold, the
journal-entry builder returns nothing — and the landed cost is still marked done.**

> No journal entry. No warning. The cost is recorded as applied and has no accounting effect.

v18's path for re-expensing the already-sold portion **is gone**.

Classification: **FACT VERIFIED** (expert) — a **v19 regression**. Not re-derived by this
session.

### `LC-02` — the cost-price update is commented out in shipped v19 code

The block that would update the item's standard cost is **commented out** in the shipped source.

### `LC-03` — for 43 of 44 companies, landed cost cannot work at all

On the deployed configuration, landed costs either **raise an error** (where the cost method is
standard) or **post nothing** (where valuation is periodic) for **43 of 44 companies**.

Combined with §1 — installed everywhere, used nowhere — this is coherent: **the capability
could not have been used successfully even if someone had tried.**

---

## 4. THE EDGE CASES THE DIRECTIVE REQUIRED

| Case | Finding |
|---|---|
| Landed cost **before** the bill | ordinary path |
| Landed cost **after** the bill | ordinary path |
| **After the goods are sold or consumed** | **`LC-01` — silently no effect in v19** |
| Partial receipt | apportioned by remaining quantity — so a partly-consumed receipt is partly absorbed and the remainder silently dropped |
| Multiple receipts | allocation spans them; **not separately verified** |
| **Cross-period allocation** | **not established — class C.** The interaction with the re-dating period lock is untested and is a priority test |

---

## 5. OWNERSHIP

P11 holds landed-cost ownership open as a **joint P01 ↔ Inventory decision with an audit veto
retained**.

P01's position: **P01 owns the landed-cost *event* as a purchase-side cost; Inventory owns the
*absorption* into item value.** P01 asserts this as a position, **not a decision** — the joint
decision and the veto are P11's.

P01 now supplies what that decision needs: the capability is installed everywhere, exercised
nowhere, carries a v19 regression that loses value silently, and cannot function on 43 of 44
deployed companies.

---

## 6. OPEN

| ID | Item | Status |
|---|---|---|
| `LC-04` | Cross-period landed-cost allocation against the re-dating lock | **class C — priority test** |
| `LC-05` | Whether `D4` — the database with the fullest module set — holds landed-cost records | **class C, known-reachable** |
| `LC-06` | Re-derivation of `LC-01`..`LC-03` by a party other than the expert | **not done** — all three are expert-reported |
