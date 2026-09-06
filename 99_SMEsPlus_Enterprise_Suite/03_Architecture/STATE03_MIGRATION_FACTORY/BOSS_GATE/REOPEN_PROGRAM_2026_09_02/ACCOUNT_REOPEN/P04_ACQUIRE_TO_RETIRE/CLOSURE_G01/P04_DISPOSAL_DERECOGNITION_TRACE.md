# P04 — DISPOSAL / SALE / SCRAP / RESIDUAL LIFECYCLE

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P04-10`. Source basis series 18. Continues `07` of the
base package; **prior findings stand and are not restated.**

---

## 1. States and the derecognition path

`state`: `draft` → `open` → (`paused`) → `close`; plus `model`.

`set_to_close(invoice_line_ids, date, message)`:
1. **raises** if `disposal_date <= fiscal lock date`;
2. **raises** if a child gross-increase is still running;
3. sets `state='close'` on the asset **and all children**;
4. builds disposal moves via `_get_disposal_moves(...)`;
5. posts a chatter message — *"Asset sold"* if invoice lines were supplied, else *"Asset
   disposed"*.

`disposal_date` is a **stored compute**: for a closed asset it is `max(depreciation move
dates)`, otherwise `False`.

## 2. The two lock behaviours inside one model — new

| Path | Lock handling |
|---|---|
| `set_to_close` | **raises `UserError`** — *"You cannot dispose of an asset before the lock date"* |
| `write()` account re-assignment | `if move.date > lock_date:` — **silently skips** locked moves, no error, no message |

> **`P04-F-155`. The same module enforces the fiscal lock by refusing one operation and by
> silently declining half of another.** A user who re-assigns the depreciation account on an
> asset with posted history gets **partial application** — future moves change, locked moves
> keep the old account — and **is told nothing**. `FACT VERIFIED`, series 18.
> This is a different mechanism from the previously published re-dating finding and does not
> replace it.

## 3. Residual book value to derecognition

| Element | Behaviour |
|---|---|
| Depreciable base | `original_value − salvage_value` |
| End-of-life clamp | `_get_depreciation_amount_end_of_lifetime`: if `residual < amount` **or** `days_until_period_end >= asset_lifetime_days`, the period amount **becomes the residual** |
| Consequence | The board **cannot overshoot**; the final period absorbs the remainder |
| `salvage_value` at close | **never depreciated** — it is excluded from the base, so it remains in book value until derecognition |
| Book value | `_get_own_book_value` = residual + `salvage_value` |

> So **the not-depreciable value is exactly the amount still sitting on the balance sheet when
> depreciation finishes** — which is the quantity the Boss policy calls the *financial residual
> book value* and rules must **not** be consumed by internal managerial usage. §4 confirms the
> product agrees by omission: nothing consumes it.

## 4. Continued internal usage after full depreciation

Nothing in `account_asset` reacts to *"fully depreciated"* other than the clamp in §3. There is
**no** state for it, **no** event, **no** hook. A fully depreciated asset simply sits at
`state='open'` with `value_residual = 0` and `salvage_value` intact.

> **Confirms, from the asset side, that `CQ-P04-06` has no existing mechanism to configure** —
> it is a build, not a setting.

## 5. Equipment is not released — carried from `CQ-P04-03`

Disposal closes the asset and posts the disposal moves. **It does not touch `name_asset`, and
it does not reset the equipment's `status`.** With `'eqp'` never written anywhere
(`P04-F-149`), the equipment of a disposed asset stays permanently marked *To Assets*.

> **The financial life of the asset ends and the operational record it points at is left in a
> terminal state with no owner.** Routed to **P05** (maintenance-owned records) and carried in
> the Design Input Pack as `UNRESOLVED — DECISION/EVIDENCE REQUIRED`.

## 6. Correction / reversal

Prior package findings stand: the derecognition entry is **left in draft and is silently
deletable**, and a blank account link **drops the corresponding leg**. `CQ-P04-01` §2 now
supplies the cause of the second: the accounts are filled only by the form-time model copy.

## 7. Disposition

> **`CQ-P04-10` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**, series 18.
> New finding `P04-F-155`. Residual semantics confirmed and aligned with the carried policy.
> **Equipment release on disposal is an open design decision, not a defect to fix in place** —
> the estate has no concept to fix.
