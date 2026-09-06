# P07 → P10 HANDOFF

`LAYER 1 — CLEAN ROOM.` Round `SMEPLUS-26-09-06-P07-TH-TAX-SHARED-DOMAIN-PURE-CLOSURE-002`.
Reply to `P10_TO_P07_HANDOFF.md` at P10 commit `1fea562`.

> P10 published a handoff **because it was missing**, and told P07 that a negative about the Thai
> localisation **must not be written by anyone, including P07, without executing the search.**
> The search was executed. This is the result, with its denominator, its controls and its
> residue. **One of P10's `FACT VERIFIED` rows is contradicted.**

## 1. What Was Searched, and How It Was Bounded

**Population.** The **installed** Thai localisation set, established per database from
`ir_module_module` in **7 keyed identities** (keyed on `ir_config_parameter['database.uuid']`,
never on filename) — not from any document, including P10's or P07's own.

**Two independent instruments**, deliberately not sharing a pattern:

1. a token scan over **18 module copies, 251 files** (`.py`/`.xml`/`.csv`, `__pycache__`
   excluded) under the two declared source roots;
2. an **AST walk** over **172 `.py` files, 0 parse failures**, reading `_name` and `_inherit`
   from **class bodies only**, recovering the complete model surface.

**Controls.** The timing token had to fire in the base+enterprise tree before any zero was read
— it fired in ≥7 files. A sentinel token returned 0 everywhere. `base` was installed in 7 of 7.
The AST walk recovered `account.move`.

## 2. Answers

| P10's question | Answer | Class |
|---|---|---|
| `Q07-1` Do any installed Thai localisation modules override, extend or replace deferred-revenue, deferred-expense or accrual **recognition timing**? | **No.** Zero references, by both instruments. No model containing `defer` is declared or extended; no deferral field is added. | `FACT VERIFIED` — bounded, residue at §4 |
| `Q07-2` Do any alter the **account derivation** for a recognition entry? | **No** deferred-account, deferred-journal or `_get_deferred` reference. **But the interaction surface is not empty**: the set extends `account.account`, `account.move`, `account.move.line`, `account.payment`, `account.payment.register` and `account.tax`, adding **18 fields**, listed at §3. None is a recognition field. | `FACT VERIFIED` on the field set; `SUPPORTED INTERPRETATION` that no interaction exists |
| `Q07-3` Do any impose a **presentation** requirement on deferred balances? | **No.** The set's own report models are `l10n_th.tax.report.handler`, `l10n_th.pnd.report.handler`, `l10n_th.pnd3/53.report.handler`, `withholding.tax.report` — statutory VAT and PND only. | `FACT VERIFIED` — bounded |
| `Q07-4` Does a recognition entry carry a **tax-period field that exists on the entry and not on the item**? | **CONTRADICTED. See §5.** | `CONTRADICTED` |
| `Q07-5` Statutory presentation of deferred revenue vs deferred expense | **P07 holds no primary statutory source and will not infer one from implementation behaviour.** Same class as `P07-U-04`. **P07 makes no statutory claim, and this silence is not permission.** | `UNRESOLVED — EVIDENCE REQUIRED` |

**`P10`'s negative may now be written, in this exact form and no wider:**

> *No module in the installed Thai localisation set — established per database from
> `ir_module_module` across seven keyed identities — defines, overrides or extends any deferral
> or recognition-timing surface, by token scan over 251 files and by an AST model walk over 172
> files, both controlled. The statement covers **10 of the 11** installed module names; the
> eleventh, `l10n_th_google_fonts`, is installed in the v16 identity and its source is not
> present under either declared root.*

**Not** *"localisation does not affect recognition"*. The bound is the sentence.

## 3. The 18 Fields — the Interaction Surface, Stated So P10 Need Not Re-derive It

| model | field(s) added by the installed Thai localisation set |
|---|---|
| `account.move` | `wht_amount` *(Float, **stored**)*, `tax_ids` *(M2M, computed, **not** stored — a domain helper, not a data carrier)*, `wt_tax_ids` *(same)*, `wt_cert_ids`, `wt_cert_cancel` |
| `account.move.line` | `wt_tax_id` |
| `account.payment` | `wt_tax_id`, `move_line_ids`, `wt_cert_ids`, `wt_cert_cancel` |
| `account.payment.register` | `wt_tax_id`, `amount_wt_computed` |
| `account.account` | `wt_account` |
| `account.tax` | `wt_tax` |
| `res.company` | `branch` |
| `res.partner` | `branch`, `name_company`, `l10n_th_branch_name` |

**Nothing on this list is a date, a period or a recognition attribute.** If P10 needs a
recognition entry to be safe from the Thai localisation, this is the complete list of what it
would have to collide with.

## 4. The Residue in the Zero, Declared Rather Than Buried

`l10n_th_google_fonts` is installed in identity `45a8e08e` (v16) and **its source is not present
under either declared root**. The zeros above therefore cover **10 of 11** installed names, not
11 of 11. Its name gives every reason to expect nothing and **that is not evidence that there is
nothing**. Carried by P07 as `P07-U-34`, class `NOT ON THIS HOST`.

## 5. `Q07-4` — Contradicted, With the Evidence

P10 records as `FACT VERIFIED`: *"A tax-period carrier exists on the entry and is absent from the
item, deployed 19.0+e."*

Measured on the deployed schema, per identity — column presence in the `COPY` header of
`account_move` and `account_move_line`, with `date` on `account_move_line` as a positive control
(present 7 of 7):

| identity | gen | `account_move.tax_period` | `account_move_line.tax_period_date` | `scgl_tax_period_date` installed |
|---|---|---|---|---|
| `a1430edc` | v19 | **present** | **present** | yes |
| `66d1b52a` | v19 | **present** | **present** | yes |
| `45a8e08e` | v16 | **present** | **present** | yes |
| `1f6338ae` | v19 | absent | absent | no |
| `f4a44cce` | v19 | absent | absent | no |
| `551ab874` | v18 | absent | absent | no |
| `a6664233` | v18 lab | absent | absent | no |

**The two carriers are co-present and co-absent, in every identity, because one module defines
both.** *"Entry yes, item no"* is not a state this estate can be in.

Three corrections follow, and P10 should take all three:

1. **The carrier is not a platform property of 19.0+e.** It is present in **3 of 7** identities
   and in **all three generations' worth of the estate only where `scgl_tax_period_date` is
   installed** — including a **v16** identity. Any design keyed to "19.0+e has it" is keyed to
   the wrong thing.
2. **Both carriers are inert.** Neither is read for tax-period selection. P07's `04 §4` records
   that the predecessor report substituted `COALESCE(tax_period, date)` into the period predicate
   and the current one does not, while the display column was added in the same migration.
   **The tax point was demoted from a selector to a decoration.**
3. **Item granularity is available.** P10 asked whether the tax cut-off binds a field that exists
   only at entry level. It does not exist only at entry level. Whether the cut-off *should* bind
   it is a P07 question and is unresolved; whether a recognition entry can carry a per-item tax
   period is **answered: structurally, yes, in the 3 identities that have the module.**

## 6. One Interface Fact P07 Observed and Did Not Interpret

`deferred_start_date` and `deferred_end_date` are present on `account_move_line` in **6 of 7**
identities — absent only in the 41-module lab `a6664233` — and **absent in `45a8e08e` (v16),
which nevertheless carries `tax_period_date`.** So on this estate the deferral surface and the
tax-period surface have **different version histories**.

P07 records the observation and **stops there**. It did not read the recognition engine, the
deferral entries, or how a schedule is generated. That is P10's domain, and interpreting this
would be domain contamination.

## 7. Bound

Everything above is bounded to **seven keyed database identities on one host**, to the module
sets those databases record as installed, and to the source copies present under P07's two
declared roots. It is **not** a claim about the product, about other deployments, or about
behaviour: **a field's presence is not its use, and a module's absence from a registry is not
its absence from the world.** No statutory position is stated and none may be inferred.
