# P04 — ASSET MODEL → ASSET POLICY INHERITANCE

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P04-01`. Source basis **series 18** (`MD-P04-01`).
Evidence: `account_asset/models/account_asset.py`, reference tree, module `account_asset` —
installed at `18.0.1.0` in the 361-module deployment.

---

## 1. There is no inheritance. There is a form-time copy of ten fields.

The Asset Model is not a separate model. It is an `account.asset` record with `state='model'`,
referenced by `model_id`. Everything an asset takes from it is taken by **one `@api.onchange`**:

```
@api.onchange('model_id')
def _onchange_model_id(self):
    model = self.model_id
    if model:
        self.method                        = model.method
        self.method_number                 = model.method_number
        self.method_period                 = model.method_period
        self.method_progress_factor        = model.method_progress_factor
        self.prorata_computation_type      = model.prorata_computation_type
        self.analytic_distribution         = model.analytic_distribution or self.analytic_distribution
        self.account_asset_id              = model.account_asset_id
        self.account_depreciation_id       = model.account_depreciation_id
        self.account_depreciation_expense_id = model.account_depreciation_expense_id
        self.journal_id                    = model.journal_id
```

**Ten fields. An onchange fires only in an interactive form.**

> **`P04-F-145` — issued, disproved by its own author, and reissued narrower.**
>
> **First form, WITHDRAWN:** *"the Asset Model supplies policy only when a human opens a
> form."* The mandated disproof pass searched for any invocation of `_onchange_model_id`
> outside the form and **found one**: `account_move.py:252`, inside `_auto_create_asset`.
> The automatic capitalisation path — a posted bill on an account with `create_asset != 'no'`
> — **does** apply the model. The first form was **wrong** and is recorded, not deleted.
>
> **Reissued form, `FACT VERIFIED`, series 18:** **the model policy is not a property of the
> asset record; it is an action that exactly three call sites perform.**
>
> ```
> assets = self.env['account.asset'].with_context({}).create(create_list)
> for asset, vals, invoice, validate in zip(...):
>     if 'model_id' in vals:
>         asset._onchange_model_id()          # a post-create repair
> ```
>
> `create()` itself still reads `model_id` for **nothing** — it forces `state`, re-asserts
> `original_value`, and in the `original_asset` context back-links the source asset. The
> automatic path works **only because it re-calls the onchange immediately afterwards**, and
> only when `'model_id' in vals`.
>
> | Call site | Applies policy? |
> |---|---|
> | Form view (`@api.onchange`) | yes |
> | `_auto_create_asset` — explicit call | yes |
> | The module's own test suite — 10 explicit calls | yes |
> | **ORM `create()`, import, API, automated action, custom module, data migration** | **no** |
>
> **The failure mode is a fourth caller.** Anything that sets `model_id` in `create()` and
> does not replicate the two-step gets an asset whose method, duration, prorata type, three
> accounts and journal are at field defaults — and three of those have **no default at all**.

## 2. What a non-form asset gets instead

| Field | Model-copied value | Standalone default if the copy never runs |
|---|---|---|
| `method` | model's | **`linear`** |
| `method_number` (Duration) | model's | **`5`** |
| `method_period` | model's | **`'12'` — years** |
| `method_progress_factor` | model's | **`0.3`** |
| `prorata_computation_type` | model's | **`constant_periods`** (field is `required=True`) |
| `analytic_distribution` | model's, else keeps its own | **empty** |
| `account_asset_id` | model's | **empty — no default** |
| `account_depreciation_id` | model's | **empty — no default** |
| `account_depreciation_expense_id` | model's | **empty — no default** |
| `journal_id` | model's | **empty — no default** |

> **This joins two findings that were separate.** `P04-F-23` established that a blank account
> link **silently drops the corresponding leg**, producing an unbalanced entry that surfaces
> only when someone posts it. §1 now supplies the cause: **the Asset Model is the only thing
> that would have filled those three accounts and the journal, and it fills them only in the
> form.** The defect and its cause were in the same package for two days without being joined.

## 3. One field is a live reference. Ten are snapshots.

```
@api.depends('original_value', 'model_id')
def _compute_salvage_value(self):
    if asset.model_id.salvage_value_pct != 0.0:
        asset.salvage_value = asset.original_value * asset.model_id.salvage_value_pct
```

> **`P04-F-146`. Changing a model's not-depreciable percentage silently recomputes the
> not-depreciable value of every asset that references it. Changing the model's method,
> duration, prorata type, accounts or journal changes nothing on any existing asset.**
> One field tracks the model for the asset's whole life; the other ten were copied once, in a
> form, and are thereafter unrelated to it. `FACT VERIFIED`, series 18.

**Why it matters beyond tidiness:** an accountant who edits a model reasonably expects either
*"this changes future assets only"* or *"this changes everything"*. The product does **both at
once**, on different fields, with no indication in either direction. `salvage_value` is also
not a cosmetic field — it is the depreciable-base floor.

## 4. Later model change — the direct answer to the CQ

| Question | Answer | Basis |
|---|---|---|
| Does an existing asset follow a later model edit? | **No**, for all ten copied fields | onchange semantics; no `related=`, no stored compute on any of the ten |
| Any exception? | **Yes, one**: `salvage_value`, via `salvage_value_pct` | `@api.depends('model_id')` |
| Is the asset→model link retained after copying? | **Yes** — `model_id` persists, so the record *looks* governed by the model | field is a plain `Many2one`, not `ondelete`-guarded here |
| Can the model be identified from the asset later? | Yes | `model_id` |

> The retained link is what makes this hard to notice: **the asset keeps pointing at a model
> it no longer obeys.**

## 5. Scope

`model_id` carries `domain="[('company_id', '=', company_id)]"` — a model may be selected only
within the asset's own company. **COMPANY-scoped by construction**, and consistent with
`P04-BD-09`, which asks whether that is the intended ownership. `CQ-P04-11` carries it.

## 6. Disposition

> **`CQ-P04-01` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**, bounded to **series 18**.
> Two new findings: `P04-F-145` (UI-only policy transfer), `P04-F-146` (one live field among
> ten snapshots). One prior finding gains its cause (`P04-F-23`).
> **Design consequence is not decided here** — it is carried into the Design Input Pack as a
> `DESIGN CANDIDATE` and, for the model-change-propagation question, as
> `UNRESOLVED — DECISION/EVIDENCE REQUIRED`.
