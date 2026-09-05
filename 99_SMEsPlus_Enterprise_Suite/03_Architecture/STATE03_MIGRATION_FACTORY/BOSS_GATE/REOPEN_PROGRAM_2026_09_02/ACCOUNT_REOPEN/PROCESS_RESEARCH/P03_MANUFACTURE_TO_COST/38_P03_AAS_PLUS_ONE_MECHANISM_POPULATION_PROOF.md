# 38 — AAS+ ONE-MECHANISM POPULATION PROOF

**LAYER 2 — AUDIT QUARANTINE.**

The veto's second limb, retrieved from the authoritative source rather than a summary:

> `ASSET_DR_CONTINUATION` / P03 `20` §5 — no costing implementation may begin until
> `BLK-07` is decided **and** it is proved that **exactly one** mechanism carries machine
> cost into product cost.

This file executes that proof against a declared population. It does not discharge it.

---

## 1. The unit problem must be settled first

The limb says *"into product cost"*. Product cost is inventory carrying value. So the
governing unit is **U1 — writer of inventory carrying value**. But a proof under U1 alone
would miss `M4`/`M5`/`M6`, which carry machine cost into **management** cost, and `M9`,
which carries it into a **standard price** that becomes inventory value.

**The proof is therefore executed against all three relevant units** — `27` §5.

## 2. Test 1 — U1, financial product cost

Members that write inventory carrying value **from machine cost**: `M1`, `M2`, `M9`
(indirectly, via standard price), `M7` (when a human types a machine cost into it).

| Mechanism | Distinct economic cost? | Injects financial cost? | Duplicates another? | Can coexist with another on one order? | Mutual exclusion enforced? |
|---|---|---|---|---|---|
| `M1` | No — same hour as `M2` | **Yes** | pairs with `M2` | **Yes** | **No** — they are designed to pair |
| `M2` | No — same hour as `M1` | **Yes** | relieves `M1` | **Yes** | **No** |
| `M9` | Same hour, **planned** not actual | via standard price | **Yes — against `M1`** | **Yes**, for standard-costed products | **No** — `DC-04` is exactly this |
| `M7` | Depends what a human typed | **Yes** | **possibly `M1`** — nothing prevents entering machine cost here | **Yes** | **No** |

> **Test 1 result: FAILED.** Under U1 the machine hour reaches product cost through a
> pair (`M1`+`M2`) that is *designed* to be two, plus `M9` which duplicates it for
> standard-costed products with **no cost-method guard on the relief side**, plus `M7`
> which is an unvalidated free float. **Exactly one is not proved; the opposite is.**

## 3. Test 2 — U2, the full monetisation surface

Seven paths under P04's declared unit. Machine-cost members: `M1`, `M2`, `M4`, `M8`, `M9`.

| Pair | Both executable on one order? | Reconcile? |
|---|---|---|
| `M1` ↔ `M2` | Yes, by design | Yes — except for `extra_cost` (`DC-03`) |
| `M1` ↔ `M4` | Yes | **No** — different duration **and** different content (`DC-05`) |
| `M1` ↔ `M9` | Yes, standard-costed | **No** — live GL mismatch (`DC-04`) |
| `M1` ↔ `M8` | Yes, at period end | `M8` self-reverses; different account family (`03` §3) |
| `M4` ↔ `M5` | Yes, where the project bridge is installed | **No collision check** (`DC-14`) |

> **Test 2 result: FAILED.** Five of the pairs can coexist on one production event; **four
> do not reconcile**. No configuration validation exists that would prevent any pairing.

## 4. Test 3 — U3, duplicate records rather than duplicate cost

> **Test 3 result: FAILED for records, PASSED for financial cost.** `M4`/`M5` duplicate
> analytic records (`DC-14`); no mechanism duplicates a *financial* injection of the same
> machine hour into WIP — the `M1`/`M2` pair is a matched capitalise-and-relieve, not a
> double injection. **This is the one favourable result in the proof and it is recorded as
> such rather than omitted.**

## 5. Test 4 — the runtime test the prior rounds could not run

| Mechanism | Reachable in `iSMEs`? |
|---|---|
| `M1`, `M2`, `M4`, `M9`-operation-term | **No** — 0 work centres, 0 work orders |
| `M3`, `M6`, `M5`, `M8`, `M11` | **No** — modules not installed |
| `M7` | reachable; **0 of 10,764 rows non-zero** |

> **Test 4 result: ZERO mechanisms carry machine cost into product cost in the only
> deployment where manufacturing executes.**

## 6. The proof's verdict

| Test | Unit | Result |
|---|---|---|
| 1 | U1 — financial product cost | **FAILED** — more than one, and they mismatch |
| 2 | U2 — monetisation surface | **FAILED** — five coexisting pairs, four irreconcilable |
| 3 | U3 — posting artefacts | **FAILED for records; PASSED for financial cost** |
| 4 | runtime | **ZERO** — none reachable |

> **The single-mechanism condition is NOT satisfied, and cannot be satisfied by the
> reference product's structure.** It is not *nearly* one mechanism; it is a surface of
> seven with no mutual exclusion, no configuration validation and no collision check
> anywhere.

## 7. The finding that reframes the limb

Tests 1–3 fail; Test 4 returns zero. Both at once:

> **`P03T-F-07`. The system simultaneously has too many mechanisms and none in use.** The
> veto's limb — *prove exactly one* — is currently unanswerable in the useful direction:
> a proof that one mechanism carries machine cost cannot be constructed against a
> deployment where **zero** do.

**Consequence for the veto, stated for AAS+ and not decided here:** the limb as written
tests the wrong thing for the current state. Discharging it requires first that a
mechanism *exist and execute*, then that it be unique. `45` records AAS+'s response.
