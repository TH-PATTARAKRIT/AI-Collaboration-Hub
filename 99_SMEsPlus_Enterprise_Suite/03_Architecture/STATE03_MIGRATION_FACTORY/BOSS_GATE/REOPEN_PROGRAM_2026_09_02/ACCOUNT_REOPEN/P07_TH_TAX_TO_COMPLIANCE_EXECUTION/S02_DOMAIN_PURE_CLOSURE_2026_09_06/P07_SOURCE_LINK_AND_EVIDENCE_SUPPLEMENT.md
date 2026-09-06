# P07 — SOURCE LINK AND EVIDENCE SUPPLEMENT

Round `SMEPLUS-26-09-06-P07-TH-TAX-SHARED-DOMAIN-PURE-CLOSURE-002`.
`LAYER 2 — AUDIT QUARANTINE`. Supplement to `13_P07_SOURCE_LINK_REGISTER.md`; it does not
replace it.

> **Publish the command and its output, not the pattern.** Every pass below was declared before
> execution, has a denominator, and has a control that had to fire before its result was read.

## 1. Declared Evidence Populations For This Round

Two populations only. **Neither is a new root.** No unbounded walk, no `/Volumes` traversal, no
CloudStorage traversal, no archive sweep, no repository census — all forbidden by
`COMMON_CLOSURE_EXECUTION_CONSTITUTION_V1 §6` and none performed.

| Population | Definition | Size |
|---|---|---|
| `POP-DB` | One snapshot per **keyed database identity**, keyed at run time on `ir_config_parameter['database.uuid']`, never on filename | **7 identities** — `a1430edc`, `66d1b52a`, `1f6338ae`, `f4a44cce` (v19), `551ab874`, `a6664233` (v18), `45a8e08e` (v16) |
| `POP-SRC` | The **declared PATH SET** (`13 §2`) **plus** the declared comparison surface `efaplus-custom` proven to supply the installed copies (`P07-F-64`, `REV-E-48`) | 2 roots, 4 members |

`POP-DB` reproduces `22 §13`'s census exactly — 7 of 7 identities recovered, no eighth. That is
a **reproduction, not a new census**, and it moves no number in `22 §13`, which stays a floor.

## 2. The Passes, Declared

| Pass | CQ / delta | Question | Denominator | Positive control | Failure control | Stop condition |
|---|---|---|---|---|---|---|
| `EP-1` | `MD-02`, `CQ-P07-08` | Which Thai localisation modules are **installed** per identity? | `ir_module_module` rows per identity (707–1,559); unit = installed module row | `base` must be installed in every identity | sentinel name `l10n_th_nonexistent_control` must be absent everywhere | per-identity table over all 7 |
| `EP-2` | `MD-01`, `Q07-1`…`3` | Does any installed Thai localisation module reference a deferral / recognition surface? | 18 module **copies**, 251 `.py`/`.xml`/`.csv` files, `__pycache__` excluded | the timing token must fire inside `02 OTHER` (base+enterprise) — **if it returns 0 there the pattern is broken, not the answer** | sentinel token `zzq_sentinel_token_must_not_exist` | per-module-name hit table |
| `EP-2b` | same | **Second, independent instrument** for the same question — which models does the set touch at all? | 172 `.py` files parsed by AST, **0 parse failures**; unit = (module, model) from **class body `_name`/`_inherit` only** | the walk must recover `account.move` | — | complete `_name`/`_inherit` union |
| `EP-3` | `MD-03`, `Q07-4`, `CQ-P07-02` | Do the tax-period carriers exist in the **deployed schema**, at entry and at item level? | `COPY` column list of `account_move` and `account_move_line` per identity | column `date` must be present on `account_move_line` in every identity | — | per-identity presence table |
| `EP-4` | `MD-03`, `CQ-P07-02` | **Which installed module owns the carriers**, and what fields does the localisation add to shared accounting models? | (a) installed module names per identity; (b) `fields.*` assignments in class bodies whose `_inherit`/`_name` is a shared accounting model | (a) `base` installed everywhere; (b) the walk must recover fields on `account.move.line` | — | owner named; field table complete |
| `EP-5` | `CQ-P07-04`, `CQ-P07-07` | Do the two candidate code bodies agree on `_compute_wht_amount`; is the field carried in the deployed schema; who reads it? | 2 file copies; 7 identities; 36 token occurrences across `POP-SRC` | column `name` on `account_move` in every identity | — | both bodies parsed, reader set enumerated |
| `EP-6` | `CQ-P07-04`, `CQ-P07-07` | Does the **stored** `wht_amount` agree with the value recomputable from the move's **own** lines? | every `account_move` row with `wht_amount != 0` — **1,186 of 183,590** in `45a8e08e`, **4 of 15,522** in `551ab874` | **at least one move must match; if none does, the instrument is wrong and the result is uninterpretable** | — | matched / mismatched counts |
| `EP-6b` | `CH-B` challenge | Can a **withholding-rate edit after posting** account for the 199 mismatches? | the 199, split by whether the move's own lines carry any `wt_tax_id` at all | the split must exhaust the 199 | — | class `R` / class `Z` counts, and the ratio distribution within `R` |
| `EP-7` | `CQ-P07-04` | Is the only consumer of the **stored** `wht_amount` actually installed anywhere? | `ir_module_module` state per identity for 4 named modules | `l10n_th_withholding_tax` must read `installed` where the field exists | — | per-identity install state |
| `EP-8` | `CQ-P07-09` | Do `tax_base_amount` and `price_subtotal` differ on a withholding-bearing line? | every `account_move_line` row carrying `wt_tax_id` — **17,878** in `45a8e08e`, 4 in `551ab874` | both columns must be present in both identities | — | non-null and equal/different counts |

## 3. `EP-1` — The Installed Thai Localisation Set

Controls: `base` installed in **7 of 7** — PASSED. Sentinel absent in **7 of 7** — PASSED.

Union of installed `l10n_th*` names across `POP-DB` = **11**:
`l10n_th`, `l10n_th_amount_to_text`, `l10n_th_base_location`, `l10n_th_google_fonts`,
`l10n_th_partner`, `l10n_th_reports`, `l10n_th_reports_ext`, `l10n_th_withholding_tax`,
`l10n_th_withholding_tax_cert`, `l10n_th_withholding_tax_cert_form`,
`l10n_th_withholding_tax_report`.

Per-identity counts are tabulated in `P07_MATERIAL_DELTA_AND_PEER_INPUT_REGISTER.md §4`.
`P07-F-106`.

**Widening control, so the pattern is not doing silent exclusion work.** The same pass also
collected every installed module matching `l10n_` (identical set — no non-Thai localisation is
installed anywhere) and every installed name carrying a bare `th` token outside `l10n_`
(**empty in all 7**). The prefix is therefore not narrowing the answer.

## 4. `EP-2` / `EP-2b` — Two Instruments, Both Zero, Both Controlled

**`EP-2` positive control fired**: `deferred_start_date` occurs in **≥7 files** under
`02 OTHER`, e.g. `02 OTHER/sale_subscription_stock/tests/test_sale_subscription_stock_order.py`.
The pattern can fire. **Failure control returned 0 everywhere.**

| module name | copies | files | `Q07-1` timing | `Q07-2` accounts | `Q07-3` presentation |
|---|---:|---:|---:|---:|---:|
| `l10n_th` | 1 | 17 | 0 | 0 | 0 |
| `l10n_th_amount_to_text` | 2 | 12 | 0 | 0 | 0 |
| `l10n_th_base_location` | 2 | 26 | 0 | 0 | 0 |
| `l10n_th_partner` | 2 | 32 | 0 | 0 | 0 |
| `l10n_th_reports` | 1 | 9 | 0 | 0 | 0 |
| `l10n_th_reports_ext` | 2 | 8 | 0 | 0 | 0 |
| `l10n_th_withholding_tax` | 2 | 44 | 0 | 0 | 0 |
| `l10n_th_withholding_tax_cert` | 2 | 34 | 0 | 0 | 0 |
| `l10n_th_withholding_tax_cert_form` | 2 | 24 | 0 | 0 | 0 |
| `l10n_th_withholding_tax_report` | 2 | 45 | 0 | 0 | 0 |
| **total** | **18** | **251** | **0** | **0** | **0** |

**`EP-2b`, the second instrument** — 172 `.py` files, **0 parse failures**, class bodies only
(the `REV-E-59` defect is not repeated: no regex over method bodies). Control recovered
`account.move` — PASSED.

Models the installed Thai localisation set **declares**: `account.withholding.tax`,
`withholding.tax.cert`, `withholding.tax.cert.line`, `create.withholding.tax.cert`,
`withholding.tax.report`, `withholding.tax.report.wizard`, `report.withholding.tax.report.xlsx`,
`report.withholding_tax_pdf`, `l10n_th.tax.report.handler`, `l10n_th.pnd.report.handler`,
`l10n_th.pnd3.report.handler`, `l10n_th.pnd53.report.handler` — **12**.

Models it **extends**: `account.account`, `account.chart.template`,
`account.generic.tax.report.handler`, `account.move`, `account.move.line`, `account.payment`,
`account.payment.register`, `account.tax`, `ir.actions.report`, `ir.ui.view`, `product.template`,
`res.city.zip`, `res.company`, `res.country.state`, `res.currency`, `res.partner`,
`res.partner.bank`, `res.partner.company.type`, `res.users`, `city.zip.geonames.import`,
`mail.thread`, `mail.activity.mixin`, `report.report_xlsx.abstract`, plus its own two —
**26**.

**Models containing `defer`: none. Models on the recognition surface: none.**

### 4.1 The complete field-level footprint on shared accounting models — 18 fields

| model | module | field | type |
|---|---|---|---|
| `account.account` | `l10n_th_withholding_tax` | `wt_account` | Boolean |
| `account.move` | `l10n_th_withholding_tax` | `wht_amount` | Float *(stored)* |
| `account.move` | `l10n_th_withholding_tax` | `tax_ids` | Many2many *(computed, **not** stored)* |
| `account.move` | `l10n_th_withholding_tax` | `wt_tax_ids` | Many2many *(computed, **not** stored)* |
| `account.move` | `l10n_th_withholding_tax_cert` | `wt_cert_ids` | One2many |
| `account.move` | `l10n_th_withholding_tax_cert` | `wt_cert_cancel` | Boolean |
| `account.move.line` | `l10n_th_withholding_tax` | `wt_tax_id` | Many2one |
| `account.payment` | `l10n_th_withholding_tax` | `wt_tax_id` | Many2one |
| `account.payment` | `l10n_th_withholding_tax_cert` | `move_line_ids` | One2many |
| `account.payment` | `l10n_th_withholding_tax_cert` | `wt_cert_ids` | One2many |
| `account.payment` | `l10n_th_withholding_tax_cert` | `wt_cert_cancel` | Boolean |
| `account.payment.register` | `l10n_th_withholding_tax` | `wt_tax_id` | Many2one |
| `account.payment.register` | `l10n_th_withholding_tax` | `amount_wt_computed` | Boolean |
| `account.tax` | `l10n_th_withholding_tax` | `wt_tax` | Boolean |
| `res.company` | `l10n_th_partner` | `branch` | Char |
| `res.partner` | `l10n_th_partner` | `branch` | Char |
| `res.partner` | `l10n_th_partner` | `name_company` | Char |
| `res.partner` | `l10n_th` | `l10n_th_branch_name` | Char |

**Eighteen fields, eight models, and not one of them is a tax point, a tax date or a tax
period.** `P07-F-105`.

**Two corroborations, recorded as corroborations and not as new findings:**
- `res.company.branch` and `res.partner.branch` are defined by **one module**, and a **fourth**
  branch representation `l10n_th_branch_name` by another module installed beside it in 6 of 7
  identities. That is `P07-F-06` / `P07-C-02` measured at field level. **No finding moves.**
- `wt_account` on `account.account` is `P07-F-63`'s flag; `wt_tax_id` on `account.move.line` is
  `P07-F-52`'s field. Both confirmed present in the installed set.

## 5. `EP-3` / `EP-4` — The Tax-Period Carriers

Controls: `date` present on `account_move_line` in **7 of 7** — PASSED. `base` installed in
**7 of 7** — PASSED.

| identity | gen | `account_move.tax_period` | `account_move_line.tax_period_date` | `scgl_tax_period_date` installed | `smesplus_tax_period_date` installed |
|---|---|---|---|---|---|
| `a1430edc` | v19 | **present** | **present** | **yes** | no |
| `66d1b52a` | v19 | **present** | **present** | **yes** | no |
| `45a8e08e` | v16 | **present** | **present** | **yes** | no |
| `1f6338ae` | v19 | absent | absent | no | no |
| `f4a44cce` | v19 | absent | absent | no | no |
| `551ab874` | v18 | absent | absent | no | no |
| `a6664233` | v18 lab | absent | absent | no | no |

**Three findings fall out of one table.**

1. **The entry-level and item-level carriers are co-present and co-absent, always.** They are
   defined by one module, so "the entry has it and the item does not" is not a state this
   estate can be in. `P07-F-107`. P10's `Q07-4` `FACT VERIFIED` is **CONTRADICTED**.
2. **The carriers exist in 3 of 7 identities, and are read for selection in none** (`04 §3`,
   `P07-F-03`). Present-and-inert, at both levels.
3. **The installed module is `scgl_tax_period_date`. `smesplus_tax_period_date` — the name this
   package cites throughout — is installed in 0 of 7 identities.** `REV-E-92`. **No finding
   moves**: `P07-F-74` established that all five copies hash to one tree, differing only in the
   manifest `author`, so every claim drawn from the cited path holds for the installed module.
   The citation named a module nobody runs, and the code it named is the code that runs.

`deferred_start_date` / `deferred_end_date` are present on `account_move_line` in **6 of 7**
identities (absent only in the 41-module lab `a6664233`) and **absent in the v16 identity
`45a8e08e`, which nevertheless carries `tax_period_date`** — so the two surfaces have different
version histories. Recorded as an **interface fact for P10**, not analysed here.

## 6. `EP-5` — The Two Candidate Bodies Disagree

`13 §2.1` records `efaplus-custom` as a declared comparison surface with a known overlap. Two
copies of `l10n_th_withholding_tax/models/account_move.py` exist under `POP-SRC`:

| copy | sha256[:12] | `_compute_wht_amount` writes to | stored |
|---|---|---|---|
| `<A>` declared PATH SET — `addons_extra/…` | `eeee0f520afc` | **`rec.wht_amount`** — correct per-record | `store=True` |
| `<B>` declared comparison surface — `efaplus-custom/addons/…` | `c028c9a25360` | **`self.wht_amount`**, inside `for rec in self:` | `store=True` |

`<B>`, verbatim:

    @api.depends("invoice_line_ids")
    def _compute_wht_amount(self):
        self.wht_amount = 0
        for rec in self:
            inv_lines = rec.invoice_line_ids.filtered("wt_tax_id")
            amount_wt = sum(
                inv_lines.mapped(lambda l: l.wt_tax_id.amount / 100 * l.price_subtotal)
            )
            self.wht_amount = amount_wt

On a recordset of more than one move, every iteration writes the **whole recordset**; the value
that survives is the **last** record's. It is `store=True`, so it persists. `P07-F-108`.

**This is the first claim in this package for which `P07-U-01` — which copy is deployed — is
load-bearing.** `P07-F-78` closed `P07-U-28` by showing that for the **four cited** behavioural
claims both bodies agree; that finding stands exactly as written, and **its scope was those four
claims.** `account_move.py`'s `_compute_wht_amount` was not among them because no published
finding cited it. A discharge is scoped to the claims it tested. `REV-M-96`.

**Which body is deployed is `SUPPORTED INTERPRETATION`, not `FACT`.** `P07-F-64` establishes
that `efaplus-custom` supplies 24–35 of the installed modules in each in-generation database and
that all four in-generation databases are owned by role `efaplus`; `P07-F-65` establishes that
both bodies declare the same version string, so **no manifest can decide it**.

### 6.1 Who reads the stored field — 36 occurrences, one consumer

| occurrence | what it does |
|---|---|
| `<A>/addons_extra/l10n_th_withholding_tax/models/account_move.py:34,106,115` | the definition and its compute |
| `<A>/addons_extra/l10n_th_withholding_tax/views/account_move_view.xml:39` | `<field name="wht_amount" invisible="1"/>` — present, not displayed |
| `<A>/addons_extra/l10n_th_withholding_tax/models/tax_report_pnd.py:37,72` | **local SQL alias** — recomputed, does not read the stored field |
| `<A>/02 OTHER/l10n_th_reports/models/tax_report_pnd.py:46` | **local SQL alias** — recomputed |
| `<A>/addons_extra/print_voucher_request/module/report_designer.py:51,53,61` | **local dict key** — recomputed from `l.wt_tax_id.amount / 100 * l.price_subtotal` |
| `<A>/addons_extra/print_payment_remittance_adviec/report/…/body.xml:184,187,207` | **the only consumer of the stored value**: `amount = inv.amount_total - inv.wht_amount` |

**Install state of the only consumer:** `print_payment_remittance_adviec` is `uninstalled` in
**6 of 7** identities and **not present in the module registry** of the seventh. `P07-F-110`.

`print_voucher_request` **is** installed in 3 of 7 — and it recomputes; it does not read the
stored field. **The distinction matters and it was checked rather than assumed** (`REV-E-94`).

## 7. `EP-6` — The Stored Value Measured Against the Transaction

**Instrument validated before the result was read.** Positive control: 980 of 1,186 moves in
`45a8e08e`, and 4 of 4 in `551ab874`, reproduce exactly. The recomputation is right.

| identity | moves | `wht_amount != 0` | matches own lines | **mismatches** | non-zero with **no** withholding line at all |
|---|---:|---:|---:|---:|---:|
| `45a8e08e` (v16) | 183,590 | 1,186 | 980 | **199** | **7** |
| `551ab874` (v18) | 15,522 | 4 | 4 | **0** | 0 |
| `a1430edc`, `66d1b52a`, `1f6338ae`, `f4a44cce` (v19) | 10 / 16 / 6 / 0 | 0 | — | — | — |
| `a6664233` (v18 lab) | 0 | column absent | — | — | — |

**`FACT VERIFIED`: in `45a8e08e`, 199 of 1,186 stored withholding amounts — 16.8% — disagree
with the amount recomputable from the move's own withholding lines, and 7 moves store a non-zero
withholding amount while carrying no withholding-tax line at all.** `P07-F-109`.

**The cause is not decidable from a database, and is not claimed.** Two explanations fit the
same evidence exactly:

- the `<B>` compute wrote another record's value across the batch; or
- lines were edited after the last recompute and the stored value went stale.

**A database records the result of a write, never the write sequence.** This is the same class
as `P07-U-20` and `P07-U-29`, and it is settleable only by a controlled execution. Opened as
`P07-U-35`, class `EVIDENCE NEVER RECORDED`.

**What was deliberately not claimed.** 19 of the 199 mismatching moves store a value equal to
some *other* move's correct value — the last-record-wins signature. **That number is not
offered as evidence**, because the coincidence base rate was not computed: 627 distinct values
over 1,186 moves, with 79 values shared by more than one move and one run of 193. A repeated
monthly charge produces the same shape. **The signature is present and its base rate is
unestablished, which means it supports nothing.**

**`551ab874`'s clean 4 of 4 neither confirms nor refutes** — n=4 is not a denominator.

## 8. `EP-6` Consequence For Tax Truth — Four Computations, Three Bases

Assembled from `EP-5` §6.1, all within P07's own domain:

| # | Where | Formula | Base |
|---|---|---|---|
| 1 | `account.move.wht_amount` stored compute | `wt_tax_id.amount / 100 * price_subtotal` | line `price_subtotal` |
| 2 | PND query, branch 1 | `ROUND(ABS(tax.amount * account_move_line.tax_base_amount / 100))` | **`tax_base_amount`** |
| 3 | PND query, branch 2 — **same file, 35 lines later** | `ROUND(ABS(tax.amount * account_move_line.price_subtotal / 100))` | `price_subtotal` |
| 4 | voucher / remittance report Python | `l.wt_tax_id.amount / 100 * l.price_subtotal` | line `price_subtotal` |

**Four independent computations of one statutory number, over three different bases, with no
shared definition and no reconciliation between them.** `P07-F-111`.

This sits **on** `P07-F-11`'s surface and does not restate it: `P07-F-11` is about *which rows*
each branch selects; this is about *what arithmetic* each site performs. Whether
`tax_base_amount` and `price_subtotal` can differ on a withholding line — and therefore whether
branches 1 and 2 can report different amounts for one payment — **was tested**, because leaving
it open would have left `CQ-P07-09` resting on an unmeasured assumption. `EP-8`, §8.1.
**`P07-U-36` is CLOSED on evidence.**

## 9. Blind Spots Of This Round, Declared

| # | Blind spot | Effect |
|---|---|---|
| `BS-01` | `l10n_th_google_fonts` installed in `45a8e08e`, source absent from both declared roots | the `Q07-1`…`3` zero covers **10 of 11** installed names — `P07-U-34` |
| `BS-02` | Token lists in `EP-2` are author-chosen | mitigated, not removed, by `EP-2b` — a structural instrument that shares no pattern with it. Two instruments is not proof. |
| `BS-03` | `EP-6` cannot distinguish a wrong-record write from a stale value | `P07-U-35`, `EVIDENCE NEVER RECORDED` |
| `BS-04` | Which of the two bodies is deployed | `P07-U-01`, `NOT ON THIS HOST` — and now load-bearing for `P07-F-108`/`P07-F-109` |
| `BS-05` | `POP-DB` is what **this host** holds | no finding is denominated over customers, sites or installations. Unchanged from `22 §13.5`. |
| `BS-06` | `P07-U-32`'s 20 unread artefacts could hold an eighth identity | would change `POP-DB`. Not opened — Class E for every declared CQ. |


### 8.1 `EP-8` — the two bases are not interchangeable, and one of them is empty

**Population:** every `account_move_line` row carrying `wt_tax_id`, in the two identities that
exercise withholding. **Control:** both columns present in both identities — verified.

| identity | lines with `wt_tax_id` | `tax_base_amount` non-null | `price_subtotal` non-null | both non-null and **equal** | both non-null and **different** |
|---|---:|---:|---:|---:|---:|
| `45a8e08e` (v16) | **17,878** | **624** (3.5%) | 17,878 (100%) | 10 | **614** |
| `551ab874` (v18) | 4 | 1 | 4 | 0 | 1 |

And in **614 of the 624** populated cases `tax_base_amount` is **`0.0`** while `price_subtotal`
is non-zero.

**`FACT VERIFIED`: on a withholding-bearing line, `tax_base_amount` is null in 96.5% of cases and
zero in 98.4% of the remainder, while `price_subtotal` is populated in 100%.** A computation of
the form `tax.amount * tax_base_amount / 100` therefore yields **null or zero for essentially
every withholding-bearing line in the exercised population**, while the same computation on
`price_subtotal` yields the real figure. `P07-F-112`.

**What is claimed and what is not.** This measures **two columns**, not the PND query's row
selection — which is `P07-F-11`'s subject and is not restated here. The claim is that **the two
bases are not interchangeable and one of them is empty on the population that matters**; it is
not a claim about which branch selects which row.