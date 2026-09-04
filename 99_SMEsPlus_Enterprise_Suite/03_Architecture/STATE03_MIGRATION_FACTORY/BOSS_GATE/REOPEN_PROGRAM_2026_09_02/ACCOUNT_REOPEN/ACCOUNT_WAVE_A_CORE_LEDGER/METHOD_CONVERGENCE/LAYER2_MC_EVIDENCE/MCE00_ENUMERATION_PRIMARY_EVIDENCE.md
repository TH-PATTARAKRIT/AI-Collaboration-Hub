# MCE00 — METHOD CONVERGENCE ENUMERATION EVIDENCE (LAYER 2 / AUDIT QUARANTINE)

Session: `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001`
Branch: `research/account-wave-a-mc-2026-09-04-001`
Parent baseline commit: `56288c4` (GAPCLOSE `dd61e40` + standard `aea4853` + prompt)
Date: 2026-09-04

> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.**
> Contains `file:line` citations and vendor tokens against a reference ERP source tree.
> Boss / PMO / AI-Audit visible only. MUST NOT be transcribed into any Layer 1 file,
> Team B design input, or downstream reference package. The Layer 1 derivatives are the
> `METHOD_CONVERGENCE/*` register, matrix and report files, which are vendor-token free.

## MCE-000 — Evidence source registry (re-verified this session)

| Ref | Source | Location | Access |
|---|---|---|---|
| `SRC-A` | Reference ERP Enterprise source, v18 line, build 20250608 — accounting addon | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account/` | Read, verified this session |
| `SRC-C` | Framework base models and security | `.../odoo/addons/base/` | Read, verified this session |
| `SRC-E` | Framework ORM core | `.../odoo/models.py` | Read, verified this session |
| `SRC-F` | Whole addons tree — used only to BOUND negative claims | `.../odoo/addons/` (797 directories) | Read, verified this session |

**Access correction of record.** The parent package's `E00` cited `SRC-A`/`SRC-B`/`SRC-C` only.
`SRC-E` (ORM core) and `SRC-F` (whole-tree bounding) were reachable in every prior round and were
not used. Two of this round's closures depend on them. See `MCE-014`.

---

## MCE-001 — Wave A source surface: verified denominators

Wave A model set fixed as the 21 models whose semantics are Core Ledger & Closing (scopes A–H of
register `02`). Each located by `_name` declaration.

| Model | Definition site | File LOC |
|---|---|---|
| `account.account` | `models/account_account.py:20` | 1597 |
| `account.group` | `models/account_account.py:1456` | (same file) |
| `account.account.tag` | `models/account_account_tag.py:9` | 108 |
| `account.root` | `models/account_root.py:10` | 38 |
| `account.code.mapping` | `models/account_code_mapping.py:12` | 73 |
| `account.journal` | `models/account_journal.py:34` | 1069 |
| `account.journal.group` | `models/account_journal.py:15` | (same file) |
| `account.move` | `models/account_move.py:87` | 6297 |
| `account.move.line` | `models/account_move_line.py:21` | 3524 |
| `account.full.reconcile` | `models/account_full_reconcile.py:6` | 71 |
| `account.partial.reconcile` | `models/account_partial_reconcile.py:10` | 657 |
| `account.lock_exception` | `models/account_lock_exception.py:13` | 326 |
| `sequence.mixin` | `models/sequence_mixin.py:24` | 509 |
| `account.financial.year.op` | `wizard/setup_wizards.py:11` | 163 |
| `account.move.reversal` | `wizard/account_move_reversal.py:11` | 190 |
| `account.resequence.wizard` | `wizard/account_resequence.py:12` | 170 |
| `account.automatic.entry.wizard` | `wizard/account_automatic_entry_wizard.py:14` | 553 |
| `account.secure.entries.wizard` | `wizard/account_secure_entries_wizard.py:13` | 265 |
| `account.merge.wizard` | `wizard/account_merge_wizard.py:9` | 351 |
| `account.merge.wizard.line` | `wizard/account_merge_wizard.py:215` | (same file) |
| `validate.account.move` | `wizard/account_validate_account_move.py:7` | 83 |

**Verified denominators — Wave A primary source surface**

| Population | Verified denominator | Method |
|---|---|---|
| Wave A source files | **18** | file list above |
| Wave A source lines | **16,044** | `wc -l` over the 18 files |
| Wave A field declarations | **397** | `^\s+<name> = fields\.` over the 18 files |
| Wave A method definitions (`def`) | **750** | `^\s+def ` over the 18 files |
| Models declared in the whole accounting addon | **59** | `_name =` unique, whole addon |

Field/method distribution (largest units): `account_move.py` 125 fields / 315 defs;
`account_move_line.py` 77 / 139; `account_journal.py` 38 / 48; `account_account.py` 33 / 84.

---

## MCE-002 — Control-layer denominators

| Population | Verified denominator | Site |
|---|---|---|
| `_sql_constraints` blocks in Wave A files | **6 blocks / 11 tuples** | `account_account.py:1468` (group prefix, 1) · `account_account_tag.py:19` (1) · `account_journal.py:29`,`:227` (2) · `account_move.py:713` (1) · `account_move_line.py:429` (6) |
| `@api.constrains` decorators in Wave A files | **32** | 9 of 18 files |
| Explicit failure raises in Wave A files | **153** | `raise (UserError\|ValidationError\|RedirectWarning\|AccessError)` |
| `ir.model.access` rows, accounting addon | **132** | `security/ir.model.access.csv` |
| … of which target Wave A models | **35** | as above |
| `ir.rule` records, accounting addon | **31** | `security/*.xml` |
| distinct models covered by an `ir.rule` there | **20** | enumerated in `MCE-004` |
| `ir.rule` records, framework base | **31** | `base/security/*.xml` |
| Menu items, accounting addon | **52** | `views/*.xml` |
| `ir.ui.view` records, accounting addon | **126** | `views/*.xml` |
| … naming a Wave A model | **46** | per-model table in `MCE-003` |
| `ir.actions.act_window` records | **59** | `views/`, `wizard/` |
| Object buttons (`type="object"`) in views | **55** | `views/*.xml` |

**Note on `account.move` state.** `account_move.py:144-156` — exactly three states:
`draft`, `posted`, `cancel`. `account_lock_exception.py:20-26` — three states:
`active`, `revoked`, `expired`.

---

## MCE-003 — View coverage per Wave A model

| Model | `ir.ui.view` records |
|---|---|
| `account.move` | 17 |
| `account.move.line` | 15 |
| `account.journal` | 5 |
| `account.account` | 4 |
| `account.group` | 3 |
| `account.full.reconcile` | 1 |
| `account.lock_exception` | 1 |
| **`account.partial.reconcile`** | **0** |

---

## MCE-004 — RECORD-RULE COVERAGE: bounded verified absence

**Bounded scope declared:** every `ir.rule` record in `addons/account/security/*.xml` (31 records,
20 distinct model refs) **and** a token search for `model_account_partial_reconcile` /
`model_account_full_reconcile` across **all 797 addon directories**.

Models carrying an `ir.rule` in the accounting addon (complete enumeration):

`account_move` (4) · `account_move_line` (4) · `account_tax_repartition_line` · `account_tax_group` ·
`account_tax` · `account_report_external_value` · `account_reconcile_model_line` ·
`account_reconcile_model` · `account_payment_term` · `account_payment` · `account_move_send_wizard` ·
`account_move_send_batch_wizard` · `account_journal_group` · `account_journal` ·
`account_invoice_report` · `account_group` · `account_fiscal_position` ·
`account_bank_statement_line` · `account_bank_statement` · `account_account`.

| Wave A model | `ir.rule` refs |
|---|---|
| `account.move` | 5 |
| `account.move.line` | 5 |
| `account.account` · `account.journal` · `account.journal.group` · `account.group` | 1 each |
| **`account.full.reconcile`** | **0** |
| **`account.partial.reconcile`** | **0** |
| **`account.lock_exception`** | **0** |
| `account.root` · `account.code.mapping` · `account.account.tag` | 0 |

**Whole-tree bounding result.** Across all 797 addon directories, the tokens
`model_account_partial_reconcile` and `model_account_full_reconcile` appear **only** in
`ir.model.access.csv` files (`account`, `sale`, `sale_stock`, `purchase`) and in `i18n/*.po`
translation catalogues. **No `ir.rule` XML record anywhere in the tree targets either model.**

**Access granted to those unruled models** (`account/security/ir.model.access.csv`):

```
access_account_partial_reconcile,...,model_account_partial_reconcile,account.group_account_user,1,1,1,1
access_account_partial_reconcile_group_invoice,...,account.group_account_invoice,1,1,1,1
access_account_full_reconcile,...,model_account_full_reconcile,account.group_account_user,1,1,1,1
access_account_full_reconcile_group_invoice,...,account.group_account_invoice,1,1,1,1
```

**Class: `A — VERIFIED ABSENCE within a fully enumerated bounded scope.`**
The reconciliation models carry full create/write/unlink rights for ordinary accounting and
invoicing roles and **no company record rule at any layer**, while every other financially material
Wave A model carries one. This **upgrades `X-06`** from `PARTIALLY VERIFIED` / class `B —
NOT FOUND` to a bounded verified absence.

---

## MCE-005 — COMPANY-SCOPING MECHANISM ENUMERATION

`_check_company_domain` overrides in the accounting addon — **11**, all `parent_of` variants:

`account_payment_term.py:15` · `account_tax.py:30`,`:120`,`:2861` · `partner.py:34`,`:304`,`:325` ·
`account_journal.py:18`,`:43` · `account_account.py:25` (`check_companies_domain_parent_of`) ·
`account_account.py:1460`.

Framework semantics — `odoo/models.py:188-194`:

> `check_company_domain_parent_of` … lets a record be used if either `record.company_id = False`
> (implies shared between all companies), **or** `record.company_id` is a **parent of** any of the
> given companies.

`odoo/models.py:207-212` — `check_companies_domain_parent_of` — same over `company_ids`.

**`account.move` and `account.move.line` declare NO `_check_company_domain` override** and therefore
use the framework default (exact company), while `account.journal` uses `parent_of`. This is the
mechanism behind `AC-03`: a parent company's journal is admissible to a descendant company's entry.

Privilege-elevation surface (`.sudo()` call sites):

| File | sites |
|---|---|
| `models/account_move.py` | 15 |
| `models/account_account.py` | 13 |
| `models/partner.py` | 6 |
| `models/account_journal.py` · `models/account_move_line.py` · `models/account_lock_exception.py` | 3 each |
| `models/sequence_mixin.py` | 1 |
| **`account/models/` total** | **93** |
| `models/account_partial_reconcile.py`, `models/account_full_reconcile.py` | 0 |

Root-vs-company divergence surface: **37** `root_id` references across **11** files in
`account/models/` (`account_tax`, `company`, `partner`, `account_move_line`, `account_account`,
`account_payment`, `res_currency`, `product`, `res_config_settings`,
`account_bank_statement_line`, `chart_template`).

Raw-SQL surface (record-rule bypass): **62** `cr.execute` sites in `account/models/`, led by
`account_account.py` (18), `account_journal_dashboard.py` (13), `sequence_mixin.py` (4),
`account_move.py` (4).

Named bypass tokens: `BYPASS_LOCK_CHECK` **5** sites · `bypass_lock_check` **3** ·
`defer_account_code_checks` **3** · `check_move_validity` **1** · `tracking_disable` **7** ·
`skip_*` **48**.

---

## MCE-006 — `ir.config_parameter` population: GATING UNKNOWN CLOSED

`AC-06` recorded `SB-01` as a **class, not an instance**, and left the extent unbounded.

**Bounded enumeration.** Every `get_param` / `set_param` key literal in `account/models/` and
`account/wizard/` — the population is **5**, complete:

| # | Key | Wave A materiality |
|---|---|---|
| 1 | `account.disable_partial_exchange_diff` | **MATERIAL** — suppresses FX-difference posting; database-wide, no company dimension |
| 2 | `account.skip_create_bank_account_on_reconcile` | **MATERIAL** — alters reconciliation side effects; database-wide |
| 3 | `account.pdf_generation_batch` | non-material — batch size |
| 4 | `account.display_name_in_footer` | non-material — presentation |
| 5 | `account.use_invoice_terms` | non-material — presentation (Wave B) |

**Class: `A — VERIFIED, bounded.`** `AC-06`'s class claim is confirmed *and now closed*: the class
has exactly **5** members in Wave A's addon, of which **2** are semantically material and both are
database-wide. `SB-01` no longer requires an unbounded search.

---

## MCE-007 — RATE-TABLE SCOPING: SIX RULES, NOT FOUR

`FX-08`/`G10` recorded **four** distinct company-scoping rules over one rate table.
Bounded enumeration of every read and write path to `res.currency.rate` across all 797 addons
yields **six**.

| # | Site | Scope expression | Layer | In `G10`'s four? |
|---|---|---|---|---|
| 1 | `base/security/base_security.xml:62-66` | `['\|', ('company_id','parent_of',company_ids), ('company_id','=',False)]` | record rule | yes |
| 2 | `base/models/res_currency.py:128-136` `_get_rates` | `('company_id','in',(False, company.root_id.id))` | ORM read | yes |
| 3 | `currency_rate_live/models/res_config_settings.py:286,290` | `('company_id','=',company.id)` — **acting** company | write (automated feed) | yes |
| 4 | `base/models/res_currency.py:294-308` `_select_companies_rates` | raw SQL | raw SQL, bypasses record rules | yes |
| 5 | **`base/models/res_currency.py:365-366`** | **`default = lambda self: self.env.company.root_id`** | **write default** | **NO — new** |
| 6 | **`account/models/res_currency.py:229`** | **`_check_company_domain(main_company)`** → `company_id = False OR parent_of main_company` | **ORM read (currency table)** | **NO — new** |

**Closure of residual `FX08-R2`** (`G03` §7, class `C — NOT YET SEARCHED`: "whether other rate
writers use root or acting company"). **Now searched and closed.** The complete writer set is:

- **Rule 5** — direct model create defaults `company_id` to **`env.company.root_id`** (the root);
- **Rule 3** — the **automated external-rate feed** writes **`company.id`**, the *acting/iterated*
  company, which may be a branch.

Rate rows written by the automated feed for a branch company are matched by rule 1 (record rule) and
rule 6, and are **invisible** to rule 2 (`_get_rates`, the posting-time resolver), which matches only
`NULL` or root. **This is the production path**: the automated feed, not manual entry, is the normal
rate source.

`company_id` is **not** `required` (`base/models/res_currency.py:365-366`) and is editable in the UI
at `base/views/res_currency_views.xml:20,44,169`, gated only by `base.group_multi_company`.

`_sql_constraints` (`base/models/res_currency.py:368-371`):
`unique (name,currency_id,company_id)`. **`INFERENCE:`** under PostgreSQL's default
`NULLS DISTINCT`, this constraint does **not** prevent multiple null-company rates for the same
currency and date. Not executed against a live database this session.

---

## MCE-008 — `AC-01` re-verified; `AC-02` CORRECTED

**`AC-01` — CONFIRMED.** `account/security/ir.model.access.csv`:
`access_res_currency_rate_account_manager,res.currency.rate account manager,base.model_res_currency_rate,group_account_manager,1,1,1,1`.
A routine accounting-manager role holds full create/write/unlink on the rate table. In framework
base, only `group_system` holds write; every other base grant is read-only. The accounting addon
**widens** the framework's own grant.

**`AC-02` — CONTRADICTED IN TWO PARTICULARS.** `AC-02` as accepted in `G09` states the raw-SQL path
"matches `rate.company_id = <main root>` (**excluding null rows**)" and describes it as "the
**consolidation currency table**".

Read directly at `base/models/res_currency.py:294-308`:

```
SELECT r.currency_id,
       COALESCE(r.company_id, c.id) as company_id,
       ...
FROM res_currency_rate r
JOIN res_company c ON (r.company_id is null or r.company_id = c.id)
```

1. The join **includes** null-company rows and, via `COALESCE`, **attributes each null row to every
   company in the database**. It does not exclude them. The true behaviour is **broader** than
   `AC-02` recorded, in the same direction as `SB-05`.
2. `_select_companies_rates` has exactly **one** consumer in this build:
   `product_margin/models/product_product.py:149`. It is **not** the accounting consolidation
   currency table. The accounting currency table is the separate path at
   `account/models/res_currency.py:218-240` (rule 6 above).

**Disposition.** `AC-02`'s **class** — raw SQL over the rate table, bypassing record rules,
defaulting to par — is **real and confirmed** (rule 4 remains). Its **mechanism description** and
**consumer attribution** are corrected here. Instance-level correction; no new class.

---

## MCE-009 — `SB-05` core re-verified independently

`base/security/base_security.xml:62-66` — the rate record rule's `domain_force` is
`['|', ('company_id','parent_of',company_ids), ('company_id','=',False)]`.
The null-company row is admitted by an **explicit disjunct**, not by omission. Confirms `G02`/`B1`.

---

## MCE-010 — Register `02` internal arithmetic does not reconcile

Recount of `02_ACCOUNT_WAVE_A_FUNCTION_COVERAGE_REGISTER.md` from its own row cells against its own
§ "Coverage summary" table:

| Scope | Rows | Row-cell `SC` | Summary `SC` | Δ |
|---|---|---|---|---|
| A | 26 | 14 | 14 | 0 |
| B | 19 | **13** | 12 | **+1** |
| C | 25 | 17 | 17 | 0 |
| D | 18 | 13 | 13 | 0 |
| E | 18 | **13** | 12 | **+1** |
| F | 17 | 16 | 16 | 0 |
| G | 15 | **12** | 11 | **+1** |
| H | 17 | **10** | 9 | **+1** |
| **Total** | **155** | **108** | **104** | **+4** |

`PC` totals mirror the difference (row cells 37, summary 41). `EO` (3) and `NC` (7) reconcile exactly.

The headline **67.1% (104/155)** is therefore **not reproducible** from the register's own rows,
which yield **69.7% (108/155)**. Four rows still carry `SC` while the summary counts them `PC`.

The four scopes are exactly those whose affirmative cells later rounds contradicted. The still-`SC`
row text includes:

- `B-18` Multi-company isolation — *"Journal-to-company is exclusive"* — contradicted by `AC-03`
  (`account_journal.py:42-43` `parent_of`);
- `G-14` Reopening — *"soft locks move backward freely; the hard lock never does"* — contradicted by
  `X-05` (`account/models/partner.py:791-806`, explicit `BYPASS_LOCK_CHECK`);
- `H-17` Multi-company behaviour — *"rates are held per company group"* — contradicted by `SB-05`,
  `AC-01`, `AC-02` and `MCE-007`.

**Class: `A — VERIFIED.`** Whichever figure is intended, the canonical register is internally
inconsistent at the gate baseline, and three contradicted affirmative claims remain live in it in
their original wording. This is `GB-05` (unaudited affirmative claims) still present in the
package's most-cited coverage artefact.

---

## MCE-011 — `G06` negative-claim scan: denominator defect

`G06` §1 declares its scope as **"45 canonical Wave A files"** (parent `01`–`26`, `CORR1/C01`–`C13`,
`GAPCLOSE/G02`–`G05`).

Measured against the canonical package as it stands at the gate baseline:

| Measure | Value |
|---|---|
| Canonical package files (`*.md`) | **64** |
| Canonical package lines | **14,575** |
| Files inside `G06`'s declared scope | **45** |
| Lines inside `G06`'s declared scope | **6,113** |
| **Files never scanned** | **19** |
| **Lines never scanned** | **8,462 (58.1%)** |

Never scanned (LOC): `X3` 1256 · `X4` 1038 · `X1` 955 · `X2` 946 · `C1` 800 · `GR1` 757 ·
`E01` 630 · `E00` 608 · `L12B` 365 · `GR2` 272 · `L12A` 174 · `G10` 160 · `G09` 110 · `G06` 102 ·
`G08` 77 · `G07` 74 · `G01` 74 · `PACKAGE_MANIFEST` 42 · `G11` 22.

The unscanned set contains **every expert review (`X1`–`X4`), every fresh independent review
(`L12A`, `L12B`, `GR1`, `GR2`), the adversarial challenge register (`C1`), both Layer-2 evidence
files (`E00`, `E01`), and the final gate report itself (`G10`)**.

Raw negative-strength token load, unscanned set (19 files):

| Token | Hits |
|---|---|
| `cannot` | 125 |
| `never` | 105 |
| `there is no` | 63 |
| `anywhere` | 45 |
| `does not exist` | 12 |
| `always` | 9 |
| `no such` | 8 |
| `no control` | 5 |
| `impossible` | 3 |
| `no validation` | 2 |
| `no support` | 0 |
| **Total raw** | **377** |

`G06` §2 reports **200** raw hits over its 45-file scope. The unscanned remainder carries
**377** — **1.9×** the load that was triaged, and none of it has been triaged.

**Class: `C — NOT YET SEARCHED`**, quantified. The negative-claim control that `G06` §7 recommends
making mandatory has itself never been applied to 58.1% of the package by volume, including every
independent review it cites as satisfying `DR-NC-05`.

---

## MCE-012 — Evidence-lineage divergence at the baseline

The working copy of the parent GAPCLOSE execution folder was at `dd61e40` while
`origin/research/account-wave-a-gapclose-2026-09-04-001` was at `56288c4`, two commits ahead
(`aea4853` adding the Method Convergence Standard, `56288c4` adding this round's prompt).

A working-tree search for `SMEPLUS_DEEP_RESEARCH_METHOD_CONVERGENCE_STANDARD.md` in the stale clone
returns nothing. Declaring the standard absent on that basis would have been a false negative of
exactly the class `DR-NC-01` governs. Recorded as a live instance of the
`[[smeplus-deep-research-negative-claim-standard]]` failure mode: **a negative result from a stale
or partial working surface is not a finding of absence.**

---

## MCE-013 — Population-vs-taxonomy comparison (basis for the `GB-04` root cause)

| Population enumerated this round | Verified denominator | Enumerated by any prior Wave A round? |
|---|---|---|
| Wave A method definitions | 750 | No |
| Wave A field declarations | 397 | No |
| Explicit failure raises | 153 | No — `19` L6 holds a curated edge-case list |
| `ir.model.access` rows (addon) | 132 | No — individual rows cited reactively |
| `ir.ui.view` records (addon) | 126 | No |
| `.sudo()` sites (addon models) | 93 | No |
| `cr.execute` sites (addon models) | 62 | No |
| `ir.actions.act_window` | 59 | No |
| Object buttons | 55 | No |
| Menu items | 52 | No |
| `root_id` references | 37 | No |
| `@api.constrains` | 32 | No |
| `ir.rule` records (addon) | 31 | No |
| `_check_company_domain` overrides | 11 | No |
| `_sql_constraints` tuples | 11 | No |
| Named bypass-token sites | 8 | No |
| `ir.config_parameter` keys | 5 | No |
| Rate-table scoping rules | 6 | Partially — 4 of 6, reactively |
| **Wave A "functions"** | **155** | **Yes — the only enumerated population** |

**Every** material finding of rounds 2 and 3 (`SB-05`, `FX-07`, `FX-08`, `B-05`, `X-04`, `X-05`,
`X-06`, `AC-01`…`AC-06`) originates in one of the populations marked "No".

---

## MCE-014 — Reviewer-discovery dependency, quantified

| Round | Material findings originating with the author | Material findings originating with a reviewer |
|---|---|---|
| Core (`f8bc069`) | — | 4 expert reviews + 1 challenge unit raised the corrections landing in `CORR1` |
| `CORR1` (`93ad4d5`) | 0 | `L12A`/`L12B` — 2 fresh reviewers |
| `GAPCLOSE` (`dd61e40`) | 0 | `GR1`/`GR2` — 6 self-claims contradicted, 3 crossings, 10 balanced-but-wrong |

`G10` §7.2 states the same conclusion in prose. This round quantifies its cause: the author's
enumeration surface was a 155-row hand-authored business taxonomy; the reviewers' discovery surface
was the source mechanism set (750 methods, 93 sudo sites, 62 SQL sites, 31 rules …). The author
could not have found what the taxonomy has no cell to hold.

---

## MCE-015 — Enumeration commands (repeatability)

All counts above are reproducible from `SRC-A`/`SRC-C`/`SRC-E`/`SRC-F` with the scripts retained at
`scratchpad/enum/enum1.sh` … `enum14.sh`, `ncscan.sh` … `ncscan3.sh`, `locate.sh` of this session.
Each is a single-pass `grep`/`wc` over a declared path set; none depends on judgement.
`MC-04` repeatability rests on this property.
