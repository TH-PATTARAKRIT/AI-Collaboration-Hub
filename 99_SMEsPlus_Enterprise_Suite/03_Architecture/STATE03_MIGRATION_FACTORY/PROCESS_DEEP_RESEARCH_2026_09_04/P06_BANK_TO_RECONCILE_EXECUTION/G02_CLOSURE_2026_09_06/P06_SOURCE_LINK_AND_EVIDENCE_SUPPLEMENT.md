# P06_SOURCE_LINK_AND_EVIDENCE_SUPPLEMENT.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-P10-DELTA-DOMAIN-PURE-CLOSURE-003]`
**Session:** P06 — G02 P10-DELTA DOMAIN-PURE BOUNDED CLOSURE (CP-P06G07)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Supplements:** `12_P06_SOURCE_LINK_REGISTER.md` — the package's controlling denominator document. **Not superseded.**

---

## 1. Source links added this round

Every citation in this round's artefacts, with the file and line actually read. **Path aliases:** `$V18E` = `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons` · `$V19A` = `…/ODOO/ODOO-COMMUNITY/SMEsPlus19/odoo-19.0+e.20260312/odoo/addons` · `$V19B` = `…/CLAUDE AI/SMEsPlus/SMEsPlus19/SMEsPlus/odoo-19.0+e.20260417/odoo/addons`.

| ID | Claim | Source, exact |
|---|---|---|
| `SL-G-01` | Deferral generation is triggered by posting, not by settlement | `$V18E/account_accountant/models/account_move.py:109-115` (`_post` → `_generate_deferred_entries`) |
| `SL-G-02` | The recognition module triggers P06's statement-line cron eleven lines below, and still never runs recognition off a settlement | `$V18E/account_accountant/models/account_move.py:117-122` (`action_post` → `auto_reconcile_bank_statement_line._trigger()`) |
| `SL-G-03` | The deferral entry's account pair is (the P&L line's own account, the company deferral account) | `$V18E/account_accountant/models/account_move.py:297-298`; `deferred_account` assigned at `:268`; `partner_id` at `:290`; `date` inherited from `line.move_id.date` at `:295` |
| `SL-G-04` | Zero occurrences of `deferred` in P06's five core files | `$V18E/account/models/{account_payment,account_bank_statement_line,account_move_line,account_partial_reconcile,account_reconcile_model}.py` — line counts 1171 / 854 / 3524 / 657 / 388, `deferred` = 0 in each; tree-wide positive control `deferred_start_date` → **15 files** |
| `SL-G-05` | The accrual entry carries no structured source reference | `$V18E/account/wizard/accrued_orders.py:235-242` (`move_vals`) |
| `SL-G-06` | The accrual's only link to its business object is a chatter message | `$V18E/account/wizard/accrued_orders.py:257-262` (`order.message_post`) |
| `SL-G-07` | The accrual's structural reversal is created with `cancel` defaulted to `False`, so the pair is left unreconciled | `$V18E/account/wizard/accrued_orders.py:253` |
| `SL-G-08` | The accrual account domain does not require `reconcile=True` | `$V18E/account/wizard/accrued_orders.py:51` (`account_type in liability_current \| asset_current`) |
| `SL-G-09` | `_reverse_moves` writes the same `reversed_entry_id` for every reversal, with no type qualifier | `$V18E/account/models/account_move.py:4760`, `:4779-4783` |
| `SL-G-10` | `reversed_entry_id` is declared once and is indexed | `$V18E/account/models/account_move.py:564-571` — `index='btree_not_null'`, `readonly=True`, `copy=False`; inverse `reversal_move_ids` at `:572` |
| `SL-G-11` | The auto-reconcile wizard's one-to-one grouping key | `$V18E/account_accountant/wizard/account_auto_reconcile_wizard.py:118` — `['account_id','partner_id','currency_id','amount_residual_currency:abs_rounded']` |
| `SL-G-12` | Its candidate domain | same file `:101-108` — `account_id.reconcile = True`, `amount_residual_currency != 0`, `amount_residual != 0`, optional partner filter |
| `SL-G-13` | Its zero-balance strategy has **no amount key at all** | same file `:141-143` — `groupby ['account_id','partner_id','currency_id'] having sum(amount_residual_currency) = 0` |
| `SL-G-14` | The wizard never reads `reversed_entry_id` | `grep -c reversed_entry_id` → **0** in all three builds |
| `SL-G-15` | **The reconciliation widget never reads it either** | `$V18E/account_accountant/models/bank_rec_widget.py` — 1,780 lines, `grep -c reversed_entry_id` → **0** |
| `SL-G-16` | The widget's candidate domain admits an unreconciled, posted accrual pair | `$V18E/account/models/account_bank_statement_line.py:515-537` (`_get_default_amls_matching_domain`) — `reconciled = False`, `parent_state = 'posted'`, accounts where `reconcile = True` |
| `SL-G-17` | **The widget's domain mixes two scopes in one query** | same, `:517-520` vs `:526` — eligible **accounts** are scoped `company_ids child_of company_id.root_id.id` (**the fiscal root**), while eligible **lines** are scoped `company_id child_of self.company_id.id` |
| `SL-G-18` | `om_data_remove`'s delete lists | `…/SMEsPlus_19.0.20260418/01_extra/addons_extra/om_data_remove/models/model.py:18-21` (SQL construction), `:45-46`, `:92-93`, `:148-150`, `:167-174`, `:221-224`, **`:344` (`mail.message`, a separate list)** |

## 2. `SL-G-19` — the producer set for `reversed_entry_id`, enumerated

Raised by AAS-03 `E1-G-02`: a reversal-type taxonomy designed against two values when more producers exist would be wrong on arrival. **Executed.**

**DENOMINATOR.** POPULATION: every site in `$V18E/account` and `$V18E/account_accountant` that calls `_reverse_moves` or assigns `reversed_entry_id`. PATTERN: `grep -rn --include='*.py' "_reverse_moves(\|reversed_entry_id.*=\|reversed_entry_id':"`, tests excluded, field declarations excluded. UNIT: producer. **RESULT: 7.**

| # | Producer | Site | `cancel` | Pair auto-reconciled? |
|---|---|---|---|---|
| 1 | Reversal / credit-note wizard | `account/wizard/account_move_reversal.py:143` | `is_cancel_needed` | **conditional** |
| 2 | **Accrual structural reversal** | `account/wizard/accrued_orders.py:253` | **defaulted `False`** | **NO** |
| 3 | `_unlink_or_reverse` | `account/models/account_move.py:4830` | `True` | yes |
| 4 | Credit note, direct assignment | `account/models/account_move.py:6266` | n/a | n/a |
| 5 | **Reversal on full-unreconcile** | `account/models/account_full_reconcile.py:34` | `True` | yes |
| 6 | **Reversal on partial-unreconcile** | `account/models/account_partial_reconcile.py:133` | `True` | yes |
| 7 | **Deferral `unlink` reversal** | `account_accountant/models/account_move.py:140` | **defaulted `False`** | **NO** |

**SL-F-01 — Seven producers, not two. Two of the seven leave the pair unreconciled, and both are structural.** `E1-G-02` is upheld: a two-value taxonomy would have been wrong.

**SL-F-02 — And two of the seven are P06's own primitives.** Producers 5 and 6 fire **when a reconciliation is undone**. **P06's own unreconcile path manufactures `reversed_entry_id` pairs.** They use `cancel=True` and so are auto-reconciled — but they are indistinguishable, by field, from a corrective reversal. **This was not visible before the producer set was enumerated, and it means `P06-B-59` is not only about foreign objects arriving in P06's population; P06 creates the same ambiguity itself.**

## 3. `SL-G-20` — deployed configuration, read from an artefact already in evidence

Raised by AAS-03 `E2-G-02`. **READ-ONLY parse of `dump.sql`. Nothing connected, restored or written.**
Artefact: `/Volumes/iMacSys/95_BHPRO_PROJECT/DOCUMENT/iEVING_2026-03-31_06-48-41/dump.sql`. **POPULATION:** all 241 rows of `account_account`. **STATE BASIS: `active = 't'` for all 241** — declared, so the count is not silently mixing archived rows.

**`reconcile` by `account_type` — with its discriminating spread:**

| `account_type` | `reconcile = t` | `= f` |
|---|---|---|
| **`liability_current`** | **40** | **0** |
| **`asset_current`** | **15** | 8 |
| `asset_receivable` | 9 | 0 |
| `liability_payable` | 7 | 0 |
| `asset_cash` | 14 | 1 |
| `expense` | **0** | 65 |
| `asset_fixed` | **0** | 22 |
| `income` | **0** | 12 |
| *(all types)* | **85** | **156** |

**The instrument discriminates:** the flag varies 85/156 overall, is 100% true for `liability_current` and 0% true for `expense` and `asset_fixed`. **A negative control fires where it should.**

**SL-F-03 — `P06-B-59`'s precondition is satisfied on the only deployed database in evidence.** The accrual wizard offers exactly `liability_current` (purchase) and `asset_current` (sale). **Every one of the 40 `liability_current` accounts is reconcilable.** Executed by name pattern, not eyeballed: **20 of the 40** carry the prefix *"ค้างจ่าย -"* (accrued —), plus *"ค่าใช้จ่ายค้างจ่าย"* (accrued expenses, id 55) and *"ค่าใช้จ่ายค้างจ่ายอื่น ๆ"* (other accrued expenses, id 202). Among the 15 reconcilable `asset_current`: **5** named *"ค่าใช้จ่ายจ่ายล่วงหน้า…"* (prepaid expense), plus *"รายรับค้างรับ"* (accrued revenue, id 146) and *"รายจ่ายค้างจ่าย"* (id 147). **These are literally the accrual and prepayment accounts, and they are reconcilable.**

**`P06-B-59` moves from `SOURCE-REACHABLE / CONFIGURATION-DEPENDENT` to `REACHABLE — CONFIGURATION VERIFIED on `iEVING`.`** *(Not on the SMEsPlus target — `P06-OQ-98` is unchanged.)*

**SL-F-04 — And `P06-B-60` resolves in the worst available way.** `res_company`, both companies:
```
deferred_expense_journal_id = 3   deferred_expense_account_id = 3
deferred_revenue_journal_id = 3   deferred_revenue_account_id = 51
generate_deferred_expense_entries_method = on_validation
generate_deferred_revenue_entries_method = on_validation
```
Resolving those account ids against `account_account`:

| Setting | Account id | Name | Type | `reconcile` |
|---|---|---|---|---|
| `deferred_expense_account_id` | **3** | **`บัญชีพักเงินฝากธนาคาร` — BANK SUSPENSE ACCOUNT** | `asset_current` | **TRUE** |
| `deferred_revenue_account_id` | **51** | `เงินเบิกเกินบัญชีธนาคาร` — bank overdraft | `liability_current` | **TRUE** |

> **The deferred *expense* account is configured as the BANK SUSPENSE ACCOUNT.**
>
> `02_` BER-F-02 is one of this package's foundational findings: **"the counterpart of every new bank event is the journal suspense account, and its absence is a hard stop."** On this deployment, **every deferral entry the recognition mechanism generates would post into the same reconcilable account that every unmatched bank event posts into** — both partner-attributed, both left open, both admitted by the widget domain (`SL-G-16`) and by the auto-reconcile grouping key (`SL-G-11`).
>
> **And the mechanism is armed:** `on_validation` means deferral entries generate on posting, with no operator step.
>
> **Raised as `P06-B-61` — CRITICAL, criterion `C5` (systemic duplicate financial effect) and `C6` (bypass of a fundamental control).** Classification of the *configuration* is `FACT VERIFIED`; classification of the *consequence* is `SUPPORTED INTERPRETATION`, because — see below — it has never fired here.

**SL-F-05 — Configured is not exercised, and the distinction is executed rather than assumed.** `account_move_deferred_rel` — the m2m that links a deferral entry to its originating invoice — has **0 rows**, and `account_move` has **0 rows**. **The deferral mechanism has never generated an entry on this database.** *This is consistent with P10's own §3 bound, reached independently from P06's own artefact; **P10's deployment evidence is not cited here and was not used**.* `P06-B-61` is therefore a **latent** critical, not a firing one — and its latency on `iEVING` is explained by `P06_IEVING_LEDGER_STATE_FORENSIC.md`, which finds the whole ledger empty.

## 4. `SL-G-21` — the evidence base, enumerated at last

Raised by AAS-03 `E3-G-04`, and the standing subject of `P06-B-55` and `REV-E-10` / `REV-E-19`. **Two undeclared reference trees were discovered in two consecutive rounds. The population had never been executed. It has now been.**

**DENOMINATOR.** POPULATION: Odoo distribution roots on this workstation. PATH SET: `/Volumes`, `maxdepth 7` (name sweep) and `maxdepth 9` (structural sweep). PATTERN — **two independent patterns, deliberately**: (A) `-type d -name "odoo-*"`; (B) `-type f -path "*/addons/account/models/account_move.py"`, reduced to its root. UNIT: distribution root. **RESULT: 16 distinct roots in the union** (8 by name, 10 by structure, overlapping).

```
CLAUDE AI/MIGRATION/ODOO18/Odoo19_community
CLAUDE AI/MIGRATION/ODOO18/enterprise
CLAUDE AI/MIGRATION/ODOO18/odoo-18.0+e.20250608
CLAUDE AI/MIGRATION/ODOO18/odoo-18.0.post20260605
CLAUDE AI/MIGRATION/ODOO18/odoo-18_community
CLAUDE AI/MIGRATION/SMEsPlus19/02_enterprise
CLAUDE AI/SMEsPlus/SMEsPlus18/01_base_community
CLAUDE AI/SMEsPlus/SMEsPlus19/SMEsPlus/odoo-19.0+e.20260417          <- REV-E-19
CLAUDE AI/SMEsPlus/SMEsPlus_19.0.20260418/…/02_enterprise/odoo-19.0+e.20260417
CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608                            <- $V18E, declared basis
ODOO/ODOO-COMMUNITY/ODOO19
ODOO/ODOO-COMMUNITY/Odoo18/t8master
ODOO/ODOO-COMMUNITY/SMEsPlus19/SOURCE CODE
ODOO/ODOO-COMMUNITY/SMEsPlus19/enterprise
ODOO/ODOO-COMMUNITY/SMEsPlus19/odoo-19.0+e.20260312                  <- $V19A, declared basis
ODOO/SOURCE CODE/ODOO 18/odoo-18.0.post20260605
```
**POSITIVE CONTROL: both previously declared bases appear in the output.** The two patterns disagree — pattern A misses six roots that do not follow the `odoo-*` naming, pattern B misses two that lack the canonical `odoo/addons` layout. **Either pattern alone would have produced another false negative. That is why both were run.**

**SL-F-06 — The package researched two of sixteen.** That is not a defect in the two — `$V18E` and `$V19A` are the correct targets and six core findings plus this round's four are invariant across them. **It is a defect in every negative the package has ever scoped to "the tree", because "the tree" was never a declared set.** `P06-B-55` is **restated**: *the evidence base is 2 of 16 enumerated distribution roots; every tree-scope negative inherits that boundary, and the boundary is now a number rather than an adjective.*

**Deliberately NOT done:** re-running any prior analysis against the other fourteen. That is widening, it is prohibited, and it is recorded as **`P06-OQ-125`**.

## 5. Executed counts, at publication

Run **after** the last content file of this round was written, per the sequencing correction in `P06_CONTRADICTION_AND_REVISION_SUPPLEMENT.md` §7 — *a count taken before the last file is a count of a package that no longer exists.*

*(Command output is inserted below by the publication step; the commands are declared here so the numbers are reproducible rather than asserted.)*
```
grep -oh 'P06-B-[0-9]\+'  *.md G02_CLOSURE_2026_09_06/*.md | sort -u | wc -l
grep -oh 'P06-OQ-[0-9]\+' *.md G02_CLOSURE_2026_09_06/*.md | sort -u | wc -l
grep -oh 'REV-E-[0-9]\+'  *.md G02_CLOSURE_2026_09_06/*.md | sort -u | wc -l
ls *.md G02_CLOSURE_2026_09_06/*.md | wc -l
```
**RESULTS — see §6.**

## 6. Publication counts

**Executed 2026-09-06, after the last content file of this round was written.**

> **THIS IS A PUBLICATION SNAPSHOT, NOT A STANDING COUNT [REV-E-23, 2026-09-06].** The figures below were correct at the G02 close (`6442925`). Two later rounds have added `B-64`, `B-65`, `OQ-128`, `REV-E-22`, `REV-E-23` and six files. **The standing authority is `G02_CLOSURE_2026_09_06/P06_AUTO_RESUME_STATE.md` EXECUTED COUNTS, re-executed at each publication.** *Every per-round count in this package is round-local; only the resume record is current.*

| Unit | POPULATION | **RESULT** | Contiguity |
|---|---|---|---|
| Blockers | distinct `P06-B-*` across all 82 package files | **63** | ids `B-01` … `B-63`, **contiguous** |
| Open questions | distinct `P06-OQ-*` | **74** | **NOT contiguous** — 74 distinct over an id space reaching `OQ-127`. *Stated because a maximum id is not a count, and this package has confused the two before (`REV-E-06`)* |
| Author errors | distinct `REV-E-*` | **21** | contiguous |
| Package files | `*.md` + `G02_CLOSURE_2026_09_06/*.md` | **82** | 70 prior + 12 this round |
| **In-place corrections applied to prior registers** | statements carrying a dated `[REV-E-…, 2026-09-06]` marker | **30 occurrences in 15 files** | greppable, per `P06_AUTO_RESUME_STATE.md`. *The first census of this returned **17 in 9** because the grep pattern required a `]` immediately after the date and one marker family carries a trailing clause. Corrected by matching the family prefix instead — **the fifth instance this round of a pattern that could not fire**, and it was caught by the count disagreeing with the applied edits* |

**These counts were taken as the last action before publication.** `REV-E-08` recorded that two published counts went stale between execution and package close; the fix is procedural and this is it.

## 7. Negative claims made this round, with their class

Per the package's negative-claim standard (**`NO EVIDENCE FOUND` ≠ `FUNCTION DOES NOT EXIST`**), every negative asserted this round, with its class and its control:

| Negative | Class | Control that makes it safe |
|---|---|---|
| No settlement-triggered recognition exists | **A — bounded, controlled** | 6 named files, whole-file; tree-wide positive control returned 15 files |
| The accrual carries no structured source link | **A** | one file, one dict, read in full |
| Neither matching engine reads `reversed_entry_id` | **A** | `grep -c` = 0 on two named files across three builds; the same token returns 7 producers elsewhere in the same trees |
| `ir_logging` has 0 rows on `iEVING` | **A** | whole-dump control: 848 tables, 223 populated, top table 34,164 rows |
| The deferral mechanism has never generated an entry on `iEVING` | **A** | `account_move_deferred_rel` = 0 **and** `account_move` = 0; both under the same controlled parser |
| No `addons_path` on this workstation places any `om_data_remove` copy | **B — bounded to 4 config files** | unchanged from `58_` DMR-F-07; **not re-run** |
| The v18-only analyses hold under v19 | **NOT CLAIMED** | never tested. `P06-OQ-123` |
