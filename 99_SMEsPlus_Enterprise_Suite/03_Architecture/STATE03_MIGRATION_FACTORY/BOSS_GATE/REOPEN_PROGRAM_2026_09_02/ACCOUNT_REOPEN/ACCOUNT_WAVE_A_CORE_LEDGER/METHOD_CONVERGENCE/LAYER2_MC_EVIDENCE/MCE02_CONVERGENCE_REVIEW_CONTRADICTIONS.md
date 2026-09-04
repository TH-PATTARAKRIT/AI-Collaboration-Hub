# MCE02 — CONTRADICTIONS TO `MCE00`, FOUND BY FRESH INDEPENDENT REVIEW (LAYER 2)

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001`

> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.** Vendor tokens and `file:line` citations.
> **`DR-NC-06` lineage rule applies: `MCE00` is NOT edited. This file governs where they conflict.**

Two fresh reviewers, neither an author of this package, reviewed `MCE00` and the baseline. Every
claim below was **re-verified against primary source by this session before acceptance.** The
verification result, not the reviewer's assertion, is what is recorded.

---

## 1. `MCE00` claims CONTRADICTED — verified

### `MCX-01` — `MCE-006` is INVALID. The configuration-key population is not 5, and not closed.

**Claim contradicted:** *"the population is `5`, complete … `SB-01` no longer requires an unbounded
search."*

**Re-verified (`models/sequence_mixin.py:154-161`):**
```
@api.constrains(lambda self: (self._sequence_field, self._sequence_date_field))
def _constrains_date_sequence(self):
    # Make it possible to bypass the constraint to allow edition of already messed up documents.
    # /!\ Do not use this to completely disable the constraint as it will make this mixin unreliable.
    constraint_date = fields.Date.to_date(self.env['ir.config_parameter'].sudo().get_param(
        'sequence.mixin.constraint_start_date',
        '1970-01-01'
    ))
```

A **sixth** key exists in the declared scope, and it is **material**: it is the documented bypass of
the constraint that keeps entry numbering aligned with the accounting date — the `X-04` control.
Database-wide, no company dimension, read under elevated privilege.

**Cause of the miss:** the enumerating command matched only single-line
`get_param('literal')` forms. This call spans lines. **The population count was bounded by the
regular expression, not by the source** — and the scope statement did not declare the pattern.

**Aggravating fact:** the key is documented **three times inside this package's own parent**
(`E00:193`, `X4:788`, `C1:461`). It was not a hard find; it was a find the method could not make.

**Disposition:** `P-10a` reverts from `CONVERGED` to `HOLD`. Population **≥6, of which ≥3 material**.
`AC-06`/`SB-01` is **NOT closed**.

### `MCX-02` — `MCE-007` is INVALID in its central mechanism, and regresses an accepted finding.

**Claim contradicted:** *"the automated external-rate feed writes `company.id`, the acting/iterated
company, **which may be a branch** … invisible to `_get_rates` … **this is the production path**."*

**Re-verified — two independent facts, both fatal to that narrative:**

1. `base/models/res_currency.py:458-462`:
```
@api.constrains('company_id')
def _check_company_id(self):
    for rate in self:
        if rate.company_id.sudo().parent_id:
            raise ValidationError("Currency rates should only be created for main companies")
```
**A rate row cannot carry a branch company at all.** Any create or write naming a company with a
parent raises.

2. `currency_rate_live/models/res_config_settings.py:1326-1332` — `run_update_currency` searches
`[('currency_next_execution_date','<=',today), ('parent_id','=',False)]`. **The cron iterates root
companies only.**

**Aggravating fact:** the parent package already held the correct position. `GR1-F-02`
(`GR1:337-346`) states *"the rate-maintenance UI is not root-scoped, while the cron is"*, citing
`res_config_settings.py:1326-1331`. **`MCE-007` inverted a correction its own parent round had
accepted** — the precise failure `MCE-014` describes in others.

**Consequence beyond `MCE-007`.** `FX-08` is one of the four blockers `G10` reports as
**closed with evidence** and is the basis of `GB-03`. Its mechanism as recorded in `G03` is
*"the writer stores `company_id = <branch>` and the resolver looks for `company_id ∈ (NULL, <root>)`"*.
`_check_company_id` appears to forbid the writer half. **`_check_company_id` has zero occurrences
anywhere in the parent package** (searched: all 64 baseline files).

> **`MCD-02` — GATING.** `FX-08` requires targeted re-verification against
> `base/models/res_currency.py:458-462`. This session does **not** declare `FX-08` invalid — `G03`
> holds verified facts not re-read here, and a constraint can be bypassed by paths that do not go
> through it (raw SQL: `P-21d` = 62 sites). What is established is that a **model-level constraint
> layer material to `FX-08` was never enumerated by any round, including this one.**

**Disposition:** `MCE-007` rules 3 and 5 **withdrawn as characterised**. `P-08a` reverts from
`ENUMERATED` to `HOLD`. Residual `FX08-R2` is **re-opened**.

### `MCX-03` — the rate-scoping rule count is ≥9, not 6.

Three further scoping expressions in one file, unlisted by `MCE-007`:

| # | Site | Expression | Nulls |
|---|---|---|---|
| 7 | `base/models/res_currency.py:458-462` `_check_company_id` | root-only write constraint | n/a |
| 8 | `base/models/res_currency.py:393-396` `_get_latest_rate` | `x.company_id == (self.company_id or env.company.root_id)` | **excludes** |
| 9 | `base/models/res_currency.py:399-405` `_get_last_rates_for_companies` | `x.company_id == company or not x.company_id` | **includes** |

Rules 8 and 9 are **sibling methods in one file that disagree about whether a null-company rate
counts.** That is a new instance-pair of the `SB-05` class, and it strengthens `SB-05` rather than
weakening it: the inconsistency is *internal to the framework's own rate resolution*.

### `MCX-04` — bounding denominator wrong: 791 addon directories, not 797.

`find addons -maxdepth 1 -mindepth 1 -type d | wc -l` → **791** (790 with a manifest).
Every whole-tree negative claim in `MCE00` cites 797. **The conclusions are unaffected** — the
searches ran over the real tree, not over the stated number — but the stated scope is wrong and is
corrected here.

### `MCX-05` — `_sql_constraints` count wrong, and one counted constraint does not exist.

`account_move_line.py:429` holds **4** tuples, not 6. Corrected total: **9 tuples in 6 blocks**, not 11.

**More material — `account_move.py:713-715`:**
```
_sql_constraints = [(
    'unique_name', "", "Another entry with the same name already exists.",
)]
```
**The definition string is empty.** The declared constraint is a no-op. The real control is raw DDL
in `_auto_init` (`account_move.py:730-735`):
```
CREATE UNIQUE INDEX account_move_unique_name
                 ON account_move(name, journal_id)
              WHERE (state = 'posted' AND name != '/')
```
**Scoped by journal, not by company** — and journals are parent-inclusive (`AC-03`). This is the
`X-04` numbering control, and it is **not where the declared constraint says it is**.

**Disposition:** `P-15` corrected to **9 declared tuples, of which 1 is empty**, plus a **previously
unenumerated raw-DDL population** (`MCX-09`).

### `MCX-06` — minor count corrections

| `MCE00` | Corrected | Note |
|---|---|---|
| `account.move` 17 views | **20** | 3 further records in `views/account_report.xml` missed |
| 93 `.sudo()` sites | **94 lines / 95 occurrences** | 93 reachable only by excluding the de-elevation `.sudo(False)` at `account_move.py:3937`; the exclusion was not declared |
| 55 object buttons | **NOT PROVEN** | Not reproducible by any stated method (39 by `<button ... type="object">`, 92 by bare `type="object"`). Method undeclared — the row is withdrawn |

---

## 2. `MCE00`'s own unbounded negative claims — self-audit result

Reviewer A applied `DR-NC-01`…`06` to `MCE00`. **The finding is accepted in full:**

> `MCE00` applies the negative-claim standard rigorously to `MCE-004` and `MCE-008`, and **not at all**
> to `MCE-006` and `MCE-007` — the two claims this review contradicts.

The two invalidated closures are exactly the two claims that said **"complete"** without declaring a
search pattern. `MCE-004`, which declared its scope in full ("every `ir.rule` in the addon; token
search across the whole tree"), survived independent re-verification unchanged.

**This is the round's sharpest result about itself.** The convergence round committed the defect it
was convened to diagnose, in the same shape, and the control that caught it was the same control that
has caught every previous round: fresh independent review.

---

## 3. `MCE00` claims CONFIRMED under independent re-verification

| Claim | Verdict |
|---|---|
| `MCE-001` 18 files / 16,044 LOC / 397 fields / 750 methods | **CONFIRMED**, all four recounted exactly |
| `MCE-002` 153 raises · 132 access rows · 31 + 31 record rules · 52 menus · 126 views · 59 actions · 32 constraint hooks | **CONFIRMED**, each recounted |
| `MCE-002` 62 raw-SQL sites · `MCE-005` 37 root-refs / 11 files · 11 scoping overrides · 59 models | **CONFIRMED** |
| **`MCE-004`** no record rule targets either reconciliation model, anywhere in the tree | **CONFIRMED** — independently re-searched; class-`A` verified absence stands |
| `MCE-003` `account.partial.reconcile` has **0** views | **CONFIRMED** |
| **`MCE-008`** the raw-SQL path **includes** nulls via `COALESCE` and attributes them to every company; sole consumer is the product-margin report | **CONFIRMED in both particulars** — `AC-02` as accepted by `G09` was wrong; the correction stands |
| `MCE-009` the rate record rule admits null by explicit disjunct | **CONFIRMED** |
| `MCE-010` register `02`: rows 108 `SC` vs summary 104 `SC`, Δ+4 in scopes B/E/G/H; `B-18`, `G-14`, `H-17` still `SC` and contradicted | **CONFIRMED cell by cell** by the second reviewer, plus a further defect — `MCX-10` |
| `MCE-011`, `MCE-012`, `MCE-013`, `MCE-014` | Not re-verified by either reviewer; declared as such |

---

## 4. NEW material findings from the review — verified against primary source

Each was read directly by this session before acceptance.

| # | Finding | Evidence | Class |
|---|---|---|---|
| `MCX-07` | **Account merge unions company scope onto posted ledger identity and retargets posted items by raw SQL with no lock check on the path.** `company_ids_to_write = accounts.sudo().company_ids` (union of every merged account's companies) → `_update_foreign_keys_generic` raw `UPDATE` → `account_to_merge_into.sudo().company_ids = company_ids_to_write` | `wizard/account_merge_wizard.py:143`, `:163`, `:211`; `base/wizard/base_partner_merge.py:153-154`; lock enforcement only at `account_move.py:3235,3240,3282`, `account_move_line.py:1578,1703`; access `1,1,1,1` for accounting manager | **NEW INSTANCE of the `X-05` class, on a more central axis** — `X-05` rewrites the counterparty; this rewrites the **account** of a posted item *and* widens the account's company scope. Unlike `X-05` there is no bypass token — **the lock control is simply not on this path** |
| `MCX-08` | **Silent raw-SQL `DELETE` fallback.** On any constraint violation during the retarget `UPDATE`, rows are deleted with no ORM path, no log and no message, inside `mute_logger` | `base/wizard/base_partner_merge.py:152-159` | **NEW CLASS** — silent destructive fallback. Triggerability on the journal-item table specifically is **NOT PROVEN** (not executed) |
| `MCX-09` | **Raw-DDL population never enumerated.** 5 `init`/`_auto_init` definitions in the Wave A files; the real entry-number uniqueness control lives here, journal-scoped, company-blind, behind an empty declared constraint | `account_move.py:713-715`, `:729-734`; `account_move_line.py:1403`; `sequence_mixin.py:50`; `account_lock_exception.py:99` | **NEW CLASS** |
| `MCX-10` | **Unattended GL-posting actor.** A scheduled job posts draft entries via `_autopost_draft_entries`, searching with **no company filter** and swallowing failures per record | `data/service_cron.xml:3-12`; `account_move.py:5430-5451` | **NEW CLASS** — scheduled actors. `P-20a` counted 2 jobs but assessed neither |
| `MCX-11` | **`res.company` is outside the Wave A model set** although it holds all five lock dates, the five effective-lock computed fields, the fiscal-year definition, and the FX-difference posting targets | `account/models/company.py` — 1,052 LOC, 7 elevation sites | **NEW CLASS — `MCE-001`'s own denominator fails `MC-01`** |
| `MCX-12` | **`account.journal` is only partially enumerated.** A 1,158-LOC inherited extension carrying 13 raw-SQL and 10 elevation sites, with eight multi-company aggregate reads over posted amounts, is outside the 18-file surface | `account/models/account_journal_dashboard.py:25`, `:237,426,478,583,657,712,721,1115` | **NEW CLASS** — inherited-extension blind spot |
| `MCX-13` | **Compute/depends graph never enumerated.** 161 dependency declarations, 228 computed fields, 94 stored-computed fields in the Wave A files — the mechanism determining whether a posted fact can be silently re-measured outside the posting and lock path | counted over the 18 files | **NEW CLASS** |
| `MCX-14` | **Cascade-delete population never enumerated.** 20 delete-behaviour declarations in the Wave A files, **4 of them cascade**; plus cascade on the rate table's currency reference | counted over the 18 files; `base/models/res_currency.py:364` | **NEW CLASS** |
| `MCX-15` | Further unenumerated populations: 10 server actions · 27 onchange handlers · 30 tracked fields · 41 index declarations · 57 seed records · 4 controller modules | counted | **NEW CLASS** ×1 (entry points and audit-trail surface) |

## 5. CORRECTED Wave A source surface

The 18-file surface is superseded. Adding the eight boundary-carrier files the review identified:

| | Files | LOC | Methods | Fields | Failure paths |
|---|---|---|---|---|---|
| `MCE-001` as published | 18 | 16,044 | 750 | 397 | 153 |
| **Corrected** | **26** | **21,883** | **1,030** | **633** | **188** |
| `MCE-001` coverage of the corrected surface | 69% | **73%** | 73% | 63% | 81% |

Added: `account/models/company.py` (1,052) · `account/models/partner.py` (1,052) ·
`account/models/account_journal_dashboard.py` (1,158) · `base/wizard/base_partner_merge.py` (758) ·
`account/models/account_move_line_tax_details.py` (516) · `base/models/res_currency.py` (489) ·
`base/models/res_company.py` (478) · `account/models/res_currency.py` (336).

**The 18-file surface excluded the sites of `X-05` (`partner.py:791-806`), `SB-05` and `FX-08`
(`base/models/res_currency.py`), and every lock date in Wave A (`company.py`).** A convergence round
whose Wave A denominator omits the sites of the programme's three most severe findings has not
satisfied `MC-01`, and this file records that without qualification.
