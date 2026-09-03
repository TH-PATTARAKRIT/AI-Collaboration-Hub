# 15 — ASSET FUNCTION FORENSIC
**LAYER 2 — AUDIT QUARANTINE**

Answers §21 — every acquisition route, traced.

## 1. The routes, with their determinants

For each route: what triggers it, where each material value comes from, and what
state the asset lands in.

### R1 — Manual creation

| Determinant | Source |
|---|---|
| Trigger | User |
| Original value | Typed |
| Acquisition date | Typed; defaults to today |
| Prorata date | = acquisition date (or the fiscal year start, in *no prorata* mode) |
| Accounts / journal | From a model if chosen, else from defaults, else blank |
| Analytic | Typed |
| Initial state | `draft` |

### R2 — Auto-created from a vendor bill *(the primary route)*

| Determinant | Source |
|---|---|
| Trigger | **Posting** a bill whose line uses an account flagged to create assets |
| Eligibility | The account can create assets (fixed or non-current asset types only), the line has a positive total, is not a tax line, and has no asset already |
| Name | The bill line label — **and posting fails with an error if the line has no label and no product** |
| Original value | The line balance, **plus non-deductible tax**, **divided by integer quantity** if the account splits per line |
| Acquisition date | The bill's invoice date — or, for a reversal, the **reversed** entry's invoice date |
| Accounts | From the model(s) linked to that account |
| Analytic | **Inherited from the bill line** |
| Company / currency | From the line |
| Initial state | `draft`, or `open` if the account is set to create-and-validate |
| Multiplicity | **One asset per model linked to the account.** Two models on one account creates two assets from one line |

Two behaviours here are easy to miss and both matter:

- **Decimal quantities are truncated downward.** A line for 2.7 units creates 2
  assets, each worth the line balance ÷ 2.
- **An account with two asset models linked produces two assets** from a single
  bill line — not a choice, a duplication by design.

### R3 — Turn an existing posted entry into an asset

Retro-active. The move line becomes the asset's source and its account becomes the
fixed-asset account. Guarded: all source lines must be posted, from one account,
and must not net to zero.

### R4 — Value increase (child asset)

Created by the modify wizard, not by a user directly. Original value = the residual
increase + the salvage increase. Acquisition and prorata dates = **the day after**
the operation date. Its source line is the revaluation entry's own asset-account
line. It is **confirmed automatically**. `FACT VERIFIED` — `24`.

### R5 — Migration / opening balances

Two mechanisms, and the distinction matters:

- **Original value** carries the gross cost.
- **Already depreciated on import** carries the accumulated depreciation, and it
  **reduces the board without producing any journal entry**.

That second field is the sanctioned way to create a sub-ledger position that has no
GL history behind it. It is why `FAIL-G02` exists.

### R6 — API / data load

Ordinary create. **Bypasses onchange logic**; constraints still apply *if* the ORM
is used. `FAIL-X12`.

## 2. Routes that do not exist

| Claimed route | Status |
|---|---|
| Purchase order → asset | `VERIFIED GAP` |
| Goods receipt → asset | `VERIFIED GAP` |
| Product → asset | `VERIFIED GAP` |
| Equipment → asset | `VERIFIED GAP` natively; the custom link runs the other way and creates nothing |
| Expense → asset | Not present in this module |

**Capitalisation is invoice-driven.** A machine that has arrived, been installed and
started producing is not an asset until its bill is posted.

## 3. Confirm — what actually happens

1. State → `open` for the whole set, immediately.
2. Per asset: a tracking message with the depreciation parameters, and a message on
   each source bill.
3. If no board exists, compute it.
4. Validate the board invariant.
5. **Post every entry that is not already posted** — including future ones.
6. If a database check fails, the whole thing is refused with a message naming the
   asset.
7. Custom: **the linked equipment's status is flipped** to *To Assets* — `19`.

Step 5 is the one to remember: **confirming writes the asset's entire remaining
life to the ledger** — `06` §3.1.

## 4. Value determination, consolidated

```
original_value = Σ(source line balances)
                 ÷ (integer quantity, if the account splits per line)
                 + non-deductible tax value
```

`total_depreciable_value = original_value − salvage_value`

`value_residual = original − salvage − imported − Σ(posted depreciation)`

`book_value = value_residual + salvage + Σ(children book values)`
— and **minus salvage again** once the asset is closed with all entries posted.

`FACT VERIFIED`
