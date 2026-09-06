# P04 — ANALYTIC BRIDGE

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P04-09`. Source basis series 18.

---

## 1. The chain, link by link, with each link classified

| # | Link | Mechanism | Class |
|---|---|---|---|
| 1 | Asset Model → Asset | `_onchange_model_id`: `analytic_distribution = model.analytic_distribution or self.analytic_distribution` | **UI-only copy** (`P04-F-145`) |
| 2 | Source journal item → Asset | `_compute_analytic_distribution` aggregates `original_move_line_ids.analytic_distribution` | **computed**, at creation from the originating line |
| 3 | Asset → Depreciation move | `write()`: if the move is **draft** and `analytic_distribution` is in `vals`, `move.line_ids.analytic_distribution = vals[...]` | **propagated on edit only** |
| 4 | Depreciation move → Journal items | same statement — **all `line_ids`** | **see §2** |
| 5 | Journal item → Analytic account | standard `account.analytic.line` generation | reference behaviour |

## 2. The defect is in link 4, and it is one line of code

```
move.line_ids.analytic_distribution = vals['analytic_distribution']
```

> **`P04-F-153`. The distribution is written to every line of the depreciation entry — both
> the expense debit and the accumulated-depreciation credit — so the analytic account receives
> the charge and its exact contra, and nets to zero.** This is the **source cause** of the
> measured *"analytic route nets to zero"* already published in this package. The measurement
> and the mechanism are now joined. `FACT VERIFIED`, series 18.

**Two further limits on the same statement:**

- **`if move.state == 'draft'`** — posted depreciation entries are **never** re-tagged. An
  asset given an analytic distribution after its board is posted tags nothing.
- The propagation runs **only inside `write()` when `analytic_distribution` is in `vals`.**
  It is not a stored related field and not a compute; an entry created by any other route
  carries whatever it was created with.

## 3. Inheritance vs configuration

| Question | Answer |
|---|---|
| Is the asset's distribution inherited from the model? | Only in the form (link 1) |
| Is it inherited from the source journal item? | **Yes** — link 2 is a real compute, and it is the only automatic route |
| Can it be configured per depreciation line? | Not by design; lines take the move's value |
| Does it survive posting? | **No further changes after posting** (§2) |

## 4. Non-production applicability

The Boss policy input requires analytic distribution to be present in **non-production and
management-cost design**. The chain above is generic — it is not manufacturing-specific and
carries no dependency on MO, work centre or equipment. **The bridge is therefore usable for
non-production cost objects exactly as far as it works at all**, which §2 bounds to: draft
entries only, and netting to zero on both legs.

## 5. Financial vs managerial boundary

The asset's three accounts are domain-restricted: `account_asset_id` excludes `off_balance`,
and both depreciation accounts exclude `off_balance` along with receivable, payable, cash and
credit-card types.

> **`P04-F-154`. The reference asset engine cannot post to an off-balance account — all three
> account fields exclude that type by domain.** So the Boss policy input *"Off-Balance is an
> Account Type; off-balance double entries pair with off-balance"* **cannot be implemented on
> `account.asset`'s own accounts.** Any managerial/off-balance internal-usage tracking
> (`CQ-P04-06`) must be a **separate posting mechanism**, not a configuration of the asset.
> `FACT VERIFIED`, series 18. **This is a hard constraint on the design, not a preference.**

## 6. Scope and access

`analytic_distribution` is a JSON map of analytic-account id → percentage; analytic accounts
carry their own plan and company. **Scope is COMPANY at the account, and the distribution
inherits whatever the source line carried.** Consistent with P09's standing conclusion, which
this package accepts with attribution: **the analytic dimension is schema, not data.**

## 7. Disposition

> **`CQ-P04-09` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`.** Five links classified; the
> net-to-zero defect has its source cause; two further limits (draft-only, edit-only) are
> new; and the off-balance exclusion is a hard design constraint.
> New findings `P04-F-153`, `P04-F-154`.
