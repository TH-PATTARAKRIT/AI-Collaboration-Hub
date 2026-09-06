# P04 — ASSET ↔ EQUIPMENT RELATIONSHIP

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P04-03`. Source basis **series 18** and custom addons
`18.0.x`. Deployment basis: the 361-module installed set.

---

## 1. The reference product has no relation at all — measured, with a control

| Direction | Probe | Result |
|---|---|---|
| `account_asset` → `maintenance.equipment` | grep module tree | **0** |
| `maintenance`, `mrp_maintenance` → `account.asset` | grep module trees | **0** |
| **positive control** — definition of `account.asset` | `_name = 'account.asset'` | **1 hit**, `account_asset/models/account_asset.py:19` |

> **Independent corroboration of P03.** P03 reached *"Equipment → Asset: no reference in either
> direction"* from the manufacturing side; P04 reaches it from the asset side, in the same
> series, with a firing control. **Two processes, opposite directions, one answer** — and
> unlike P03's version defect, this one is a same-series comparison.

## 2. The relation exists only in a custom module — and three of its eight model files are dead

Module **`equipment_sequence`**, `18.0.1.6`, author SCGL, `depends: base, maintenance,
account_asset, product_stock_equipment`. Present in **both** declared custom trees, byte-equal
in the files examined. **Installed** — `equipment_sequence 18.0.1.6` appears in the 361-module
installed set alongside `account_asset 18.0.1.0`, `maintenance`, `mrp_maintenance` and
`product_stock_equipment`.

`models/__init__.py` imports **five** of the **eight** `.py` files present:

| File | Imported? | Consequence |
|---|---|---|
| `maintenance_equipment_category`, `maintenance_equipment`, `account_asset`, `stock_picking`, `conf_prefix` | **yes** | live |
| **`om_asset_asset.py`** | **NO** | never registered |
| `equipment_sequence.py`, `equipment_category_sup.py` | **NO** | never registered |

## 3. The dead file is what a reader would find first

`om_asset_asset.py` declares `_inherit = 'account.asset.asset'` — the **OdooMates / pre-v14**
model name.

| Test | Result |
|---|---|
| definitions of `account.asset.asset` across all three declared trees | **0** |
| positive control, `account.asset` | **1** |
| files that `_inherit` it | exactly the two copies of `om_asset_asset.py` |
| `om_account_asset` installed? | **not in the installed set** |

> **`P04-F-148`. The module installs only because the file that would break it is not
> imported.** An `_inherit` of an undefined model raises at registry build. `equipment_sequence`
> is recorded installed, so the class never loaded — and the reason is one missing line in
> `models/__init__.py`. **`Source present ≠ registered`, one level below `source present ≠
> installed`: the module is installed and part of it is not.** `FACT VERIFIED`.
>
> This is the precise form of the *"partly dead code"* this package recorded earlier without
> characterising it. **The earlier statement was right and unevidenced; it is now evidenced and
> narrower** — it is not the link that is dead, it is a **duplicate, older copy** of the link.

## 4. The live relation

`models/account_asset.py`, `_inherit = 'account.asset'`:

| Property | Value |
|---|---|
| **Field** | `name_asset`, `Many2one('maintenance.equipment')`, label *"Equipment"* |
| **Direction** | **asset → equipment only.** No reverse field on equipment |
| **Cardinality** | **many-to-one, unconstrained** — no unique index, no SQL constraint, no `@api.constrains`. **Many assets may point at one equipment record** |
| **Domain** | `[('status', '=', 'eqp')]` — only equipment not yet converted |
| **Derived** | `group_ref`, `related='name_asset.ref_mt'` |
| **Lifecycle hook** | `validate()` writes the equipment's `status` to `'tass'` |

**The lifecycle hook is live.** v18 `account.asset` defines `validate()` at line 854 and the
form button is `name="validate"` — so the override fires and the status flip happens.

## 5. Two constructs inside the live class are dead, and one control is absent

| Construct | v18 core | Effect |
|---|---|---|
| `name_get()` | **removed in v17** — `0` definitions in v18 `models.py`; replaced by `_compute_display_name` (line 1756) | the override is **never called**; the *"name: group reference"* display never appears |
| `states={'draft': [('readonly', False)]}` | **not a field attribute in v18** — no occurrence in `fields.py` | silently ignored. The field carries **no `readonly`**, so `name_asset` is **editable in every state, including after validation and after full depreciation** |

> **`P04-F-149`. The equipment link can be repointed at any time, and the status transition has
> no reverse.** Every write of `status` in both custom trees is `'tass'` — **4 occurrences, all
> one direction, 0 writes of `'eqp'`** (`'eqp'` occurs 12 times, all as the field default or a
> domain filter). So repointing a validated asset flips the **new** equipment to `tass` and
> **leaves the old one stranded** in a state that removes it from the selectable domain
> forever. Nothing — not unlink, not disposal, not derecognition — returns equipment to
> `eqp`. `FACT VERIFIED`, with the write-direction census as its denominator.

## 6. Scope and multi-company

`maintenance.equipment` and `account.asset` are both company-scoped in the reference product;
`name_asset` carries **no company domain**, unlike `model_id`, which does. **An asset in one
company can therefore reference equipment in another** unless a record rule intervenes.
Whether one does is a **record-rule question, not a field question**, and it is carried to
`CQ-P04-11` as a named check rather than asserted here.

## 7. Disposition

> **`CQ-P04-03` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**, series 18 / `18.0.x`.
> Reference product: **no relation**. Custom estate: **one live one-directional Many2one**, one
> **dead duplicate**, an **irreversible** status transition, **no cardinality control**, and
> **no company constraint**.
> New findings `P04-F-148`, `P04-F-149`. The irreversibility is carried into the Design Input
> Pack as `UNRESOLVED — DECISION/EVIDENCE REQUIRED`, and into `P04_TO_P05_HANDOFF.md` because
> it strands maintenance-owned records.
