# 02 — DEEP LEVEL 1: ASSET DOMAIN / SCOPE / CAPABILITY / BOUNDARY
**LAYER 2 — AUDIT QUARANTINE**

## 1. What "Asset" is in the reference ERP — from source, not from the menu

The asset record is a **single self-describing model** that plays four roles at
once, distinguished only by its `state` field:

| Role | How it is expressed | Consequence |
|------|--------------------|-------------|
| Template ("Asset Model") | `state = 'model'` | The same table, same fields |
| Live asset | `state` in `draft / open / paused` | |
| Retired asset | `state` in `close / cancelled` | |
| Value-increase component | `parent_id` set | A **child asset**, not a field on the parent |

This is the first Level-1 boundary fact and it is not visible from the menu:
**"Asset Model" is not a separate concept.** It is the same object with a
different status. Everything a live asset can carry, a model can carry.

`FACT VERIFIED` — model definition, `_name = 'account.asset'`, single `state`
selection with six values, `EV-CODE` asset model file L18–L47.

Second boundary fact: the model's own description string is
`'Asset/Revenue Recognition'`. The same engine drives **deferred revenue**, with
signs inverted. Every formula in this package is written for positive-value
assets; the code paths carry `if ... > 0 else` branches throughout for the
negative case. Any SMEsPlus adoption of the semantics must decide explicitly
whether it inherits that dual purpose.

`FACT VERIFIED` — `_description`, and sign-branching in the board amount clamp.

## 2. What creates an Asset — complete route inventory

| Route | Exists | Mechanism | Evidence |
|-------|--------|-----------|----------|
| Manual creation | Yes | Direct create in `draft` | `FACT VERIFIED` |
| From a vendor bill line | Yes | Account-driven: an account flagged *Create in draft* / *Create and validate* auto-generates on posting | `FACT VERIFIED` |
| Multiple assets from one bill line | Yes | Account flag *Multiple Assets per Line*; splits by **integer** quantity, decimals truncated down | `FACT VERIFIED` |
| From an Asset Model template | Yes | Copies configuration onto a new draft asset | `FACT VERIFIED` |
| From an existing journal entry, retro-actively | Yes | "Turn as an asset" action on a posted move line | `FACT VERIFIED` |
| As a value increase of an existing asset | Yes | Re-evaluate wizard creates a **child asset** with `parent_id` | `FACT VERIFIED` |
| Migration / opening balance | Yes | Dedicated *already depreciated amount on import* field | `FACT VERIFIED` |
| API / data load | Yes | Ordinary ORM create | `FACT VERIFIED` |
| **From a Product** | **No** | No product field on the asset model; no asset field on product | `VERIFIED GAP` |
| **From a Purchase Order or a Receipt** | **No** | Only the *vendor bill* route exists. Goods receipt does not create assets | `VERIFIED GAP` |
| **From Equipment** | **No** (native) | Custom module only, and in the Asset→Equipment direction only | `VERIFIED GAP` (native) |

The Purchase/Receipt gap is worth stating plainly because it is commonly assumed
to exist: **capitalisation is triggered by the invoice, not by the physical
receipt of the asset.** In the reference ERP an asset cannot come into existence
from a warehouse event. See `08_LEVEL4_CROSS_MODULE_MATRIX.md` §4.

## 3. Capability inventory — §11 of the governing prompt, answered item by item

Legend: `NATIVE` implemented in the reference product · `CUSTOM` implemented only
by a project module · `ABSENT` verified not to exist · `PARTIAL` exists but not
with the semantics the name implies.

| # | Capability | Status | Note |
|---|-----------|--------|------|
| 1 | Asset Model | `NATIVE` | Same model, `state='model'` |
| 2 | Asset Creation | `NATIVE` | 8 routes, §2 |
| 3 | Asset Acquisition | `NATIVE` | Acquisition date drives prorata date |
| 4 | Asset Capitalization | `PARTIAL` | Value comes from the **bill line balance**, not from a capitalisation process. No multi-source accumulation, no CIP/AUC stage |
| 5 | Asset Value | `NATIVE` | Original / depreciable / book / salvage, all distinct — `24` |
| 6 | Depreciation | `NATIVE` | 3 methods × 3 prorata modes — `16` |
| 7 | Asset Modification | `NATIVE` | One wizard, five actions — `24` |
| 8 | Asset Pause | `NATIVE` | Genuine calendar-shift semantics — `30` |
| 9 | Asset Resume | `NATIVE` | Accumulates paused days — `30` |
| 10 | Asset Transfer | `ABSENT` | No transfer action of any kind |
| 11 | Asset Split | `ABSENT` | The only "split" is at creation, by bill-line quantity |
| 12 | Asset Merge | `ABSENT` | |
| 13 | Asset Revaluation | `PARTIAL` | **Upward** revaluation creates a *child asset*, it does not restate the parent. **Downward** posts a value-decrease line. Neither is an IAS-16 revaluation model — no revaluation surplus, no OCI, no reserve |
| 14 | Asset Impairment | `ABSENT` | No impairment concept. A downward re-evaluation is the nearest mechanism and it is accounted as depreciation, not impairment |
| 15 | Asset Disposal | `NATIVE` | — `25` |
| 16 | Asset Sale | `NATIVE` | Requires a posted customer invoice — `25` |
| 17 | Asset Scrap | `PARTIAL` | No scrap action. "Dispose" with no invoice is the closest, and it is not linked to inventory scrap |
| 18 | Asset Cancellation | `NATIVE` | Reverses posted entries, deletes drafts, resets paused days |
| 19 | Asset Reporting | `NATIVE` | A dedicated Depreciation Schedule report |
| 20 | Asset Reconciliation | `ABSENT` | No sub-ledger↔GL reconciliation function. See `22` |
| 21 | Asset Closing | `PARTIAL` | Closure is a by-product of disposal/full depreciation, not a period-close routine |
| 22 | Asset Tax | `ABSENT` | **No tax book.** One schedule only. See `36`/`26` |
| 23 | Asset Analytic | `NATIVE` | Distribution inherited from the source bill — `21` |
| 24 | Asset↔Equipment link | `CUSTOM` | — `19` |
| 25 | Asset↔Maintenance | `ABSENT` | No relation, native or custom |
| 26 | Asset↔Product | `ABSENT` | |
| 27 | Asset↔Purchase | `ABSENT` | Bill only, not PO |
| 28 | Asset↔Vendor Bill | `NATIVE` | The primary acquisition route |
| 29 | Asset↔Accounting | `NATIVE` | Three-account triple + journal |
| 30 | Asset↔MRP / Work Center / Operation | `ABSENT` | Zero references — `27` |
| 31 | Asset↔Costing | `ABSENT` | — `36` |
| 32 | Fully Depreciated Asset | `PARTIAL` | Reached implicitly when residual hits zero; the asset stays `open` and there is **no distinct "fully depreciated" state** |
| 33 | Residual / Salvage Value | `NATIVE` | Excluded from base, protected for life — `18` |
| 34 | Post-Depreciation Usage Cost | `ABSENT` | No such concept anywhere — SMEsPlus original |

**Counts:** `NATIVE` 15 · `PARTIAL` 6 · `CUSTOM` 1 · `ABSENT` 12.

Item 32 deserves emphasis because the Boss's post-depreciation design depends on
it: **the reference ERP has no "fully depreciated" state.** An asset whose
depreciable value reaches zero simply stops generating lines while remaining
`open`. Any SMEsPlus concept of "the asset is done depreciating but still
working" has to be constructed, not inherited.

## 4. What destroys / derecognises an Asset

| Path | State after | GL effect | Reversible |
|------|-------------|-----------|------------|
| Dispose (no invoice) | `close` | Cost out, accumulated depreciation out, balancing loss | Only by reset-to-running, which itself posts corrections |
| Sell (invoice required) | `close` | As above plus proceeds; balance to gain/loss | As above |
| Cancel | `cancelled` | **Every posted depreciation entry reversed** | Reset to draft |
| Archive (`active=False`) | unchanged | None | Yes — but **only permitted when the asset is already `close` or `model`**; a running asset cannot be archived |
| Delete | gone | — | **Only permitted while `draft` or `model`** and with no posted entries |

`FACT VERIFIED` — unlink guard, cancel routine, disposal move builder, archive guard.

One integrity invariant found here is important enough to carry into Level 6: a
constraint enforces that **for any asset in `open` state, the last depreciation
line must leave a remaining value of exactly zero.** The board is therefore not
merely a projection — it is a validated closed set, and every operation that
touches it (modify, pause, resume, dispose) must leave that invariant true or the
write is rejected. See `37` `CTR-06`.

## 5. Adjacent domain map — §12 answered

| Domain | Classification | Basis |
|--------|---------------|-------|
| Vendor Bill | **IN-SCOPE CORE** | The acquisition trigger and the value source |
| Accounting (journal, accounts, GL, lock dates, fiscal year) | **IN-SCOPE CORE** | The engine is a GL producer; fiscal year drives period boundaries |
| Analytic | **IN-SCOPE CORE** | Carried on every depreciation line |
| Multi-company | **IN-SCOPE CORE** | `company_id` required; currency is derived from it and is **not independently settable** |
| Equipment | **CROSS-MODULE DEPENDENCY (custom only)** | One custom `Many2one` |
| Product | **ADJACENT EVIDENCE** | No relation. Product matters only because it is upstream of the bill line |
| Purchase / Receipt | **ADJACENT EVIDENCE** | No relation |
| Maintenance | **ADJACENT EVIDENCE** | Related to Equipment, never to Asset |
| MRP / Work Center / Operation / Routing / MO / Work Order / WIP / FG / COGS | **OUT-OF-SCOPE for the reference Asset domain** — and therefore **IN-SCOPE for SMEsPlus design** | Verified zero coupling. This is the differentiator, `27` |
| Tax | **ADJACENT — GAP** | No tax book exists |
| Reporting | **IN-SCOPE CORE** | |
| SaaS security | **IN-SCOPE CORE** | Three grants only: accounting read-only (read), accounting user (full), invoicing (read + create, no write, no delete). No asset-specific role, no record rules beyond company |

## 6. Domain boundary statement

> The reference Asset domain is a **closed financial sub-ledger**. It is bounded
> upstream by the vendor bill and downstream by the general ledger and the
> analytic dimension. It has **no operational surface at all**: it does not know
> what the asset physically is, where it is, whether it is running, who is using
> it, or what it produces.
>
> Every operational fact about the same physical machine lives in a **separate,
> unconnected domain** (Equipment / Maintenance / Work Center), which in turn has
> **no financial surface**.
>
> The two halves of the same real-world object are modelled twice and never
> reconciled. That is the structural finding of Level 1, and it is the thing
> SMEsPlus is actually proposing to fix.

## 7. Four Expert opinions

See `03_LEVEL1_FOUR_EXPERT_OPINIONS.md`.
