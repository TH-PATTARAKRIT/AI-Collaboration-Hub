# 70 — AAS+ VETO RECHECK, LIVE / LATENT

**LAYER 2 — AUDIT QUARANTINE.** Dissent preserved. **Not Boss approval.**

---

## 1. The veto, retrieved from source — not from a summary

`ASSET_DR_CONTINUATION/22` §3 and P03 `20` §5. Two limbs:

1. **`BLK-07`** — the allocation denominator — must be decided. **Boss. Still open.**
2. It must be proved that **exactly one** mechanism carries machine cost into product cost.

## 2. Ground-by-ground re-evaluation

| Ground | Source defect | Current deployment exposure | **Future configuration exposure** | Required control | Evidence |
|---|---|---|---|---|---|
| `G-1` more than one mechanism reaches product cost | `M1`+`M2`+`M9`+`M7` | **none — nothing posts** | **full**, the moment valuation is automated | structural mutual exclusion (`R-18`) | `38`, `53` |
| `G-2` no mutual exclusion anywhere | 7 duplication defects | none active | **full** | configuration validation | `56` §2 |
| `G-3` depreciation reaches cost centres via analytic | **premise DISPROVED** | n/a | n/a | — | `33`, P04-F-49, P09 |
| `G-4` no capacity denominator | no overhead pool | total | total | `BLK-07` first | `58` |
| `G-5` **the rate is unbounded** — *new this round* | `_cal_price` validates nothing | **LIVE — `55`** | full | magnitude validation (`R-17`) | `55` |
| `G-6` **the worst configuration is the default** — *new this round* | `expense_account_id` optional | **60 of 60 unset** | full | mandatory absorption account | `53`, `56` |

## 3. Live vs latent — and why it does not weaken the veto

Measured: **1 live, 11 latent, 3 unreachable** (`53` §2). A reader could argue the veto
should narrow because eleven defects do not fire.

**AAS+ rejects that reading, on the evidence:**

> The defects are latent **because the system is unconfigured, not because it is
> controlled.** 59 of 60 work centres have no rate; 60 of 60 have no expense account; 0 of
> 60 have an analytic distribution; valuation is periodic. **Every one of those is a field an
> administrator is expected to fill in.** Filling them is what a working SMEsPlus
> manufacturing installation would do on day one.

A veto whose subject is *architecture* is not discharged by *configuration emptiness*. The
question is what happens when the fields are filled, and the answer is `56` §2: **no mutual
exclusion, no validation, no collision check exists anywhere.**

## 4. The new ground the runtime evidence produced

`G-5` is the strongest ground now available, and it did not exist before this round:

> `55` — a corrupt input propagated through `_cal_price` into finished-goods value at
> **10²¹**, and the valuation ledger diverged from a balanced general ledger by −48.7 %.
> **The cost-injection path validates nothing.** This is not latent. It happened, in the
> production-scale database, and 18 of the 30 corrupt rows are manufacturing-origin.

## 5. Final status

> ## **VETO STRENGTHENED**

| Reason | |
|---|---|
| 1 | The one-mechanism proof **fails on three of four tests** and returns **zero** on the runtime test — it cannot be discharged in either direction (`38` §6–§7) |
| 2 | **No mutual exclusion exists** across 15 mechanisms and 7 duplication defects |
| 3 | **A premise is disproved** (`G-3`) — the veto's reasoning must be restated; its conclusion is unaffected |
| 4 | **A new ground appeared** — `G-5`, and it is the only ground supported by an observed live failure |
| 5 | **`G-6`** — the most dangerous configuration is the out-of-the-box one |

**Not narrowed**, despite eleven latent defects, for the reason in §3.

## 6. What AAS+ explicitly declines

- To **respecify limb 2**. `38` §7 shows it tests for uniqueness where the answer is zero.
  Respecifying a veto limb is **AAS+/Boss's act at the final gate**, not P03's.
- To evaluate P04's **third option** on `BLK-07`.
- To treat `iTEST02`'s configuration as production exposure. It has **32 GL lines**.
- To claim independence. `69` and this file are **self-review**; P04 and P09 supplied the
  only external challenge, and it corrected P03 four times.

## 7. Dissent preserved

| Expert | Position |
|---|---|
| `E1` | If material-only costing is deliberate policy, the "zeroing" framing is wrong and the veto's fifth ground overstates. **Refused as unanswerable** — `52` §3 refuses to infer intent — and preserved as the strongest objection |
| `E4` | The valuation fallback for 3,977 categories was **not read from `ir_default`**; §3's conclusion rests on the absent valuation table and a 32-line ledger. **Preserved as `UNR-P03-18`** |
