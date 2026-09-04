> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.**
> This review carries `file:line -- method` citations into a reference ERP source tree.
> Boss / PMO / AI-Audit visible only. Must NOT be transcribed into any Layer 1 clean-room package,
> into Team B design input, or into any downstream reference package. Its clean-room derivatives are
> the numbered files in the package root, which cite `EV-0NN` / `COR-0N` identifiers only.

# C1 — INDEPENDENT ADVERSARIAL CHALLENGE REGISTER

Session: `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`
Wave: `WAVE A — CORE LEDGER & CLOSING`
Unit: **INDEPENDENT ADVERSARIAL CHALLENGE UNIT** (did not author `E00_PRIMARY_EVIDENCE_BASE.md`)
Constitution basis: principle 7 — independent reviewers must not review their own work.
Date: 2026-09-04

> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.**
> This file carries `file:line` citations into a reference ERP source tree. Boss / PMO / AI-Audit
> visible only. It must NOT be transcribed into any Layer 1 clean-room package, into Team B design
> input, or into any downstream reference package.

## Source of truth actually read by this unit

| Ref | Path | Access |
|---|---|---|
| `SRC-A` | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account/` | read-only, this session |
| `SRC-B` | `.../addons/account_reports/` | read-only, this session |
| `SRC-C` | `.../addons/base/models/`, `.../odoo/fields.py` | read-only, this session |
| `SRC-E` | `.../addons/account_accountant/` (enterprise) | read-only, this session — **not cited anywhere in E00** |
| `SRC-F` | `.../addons/l10n_th/`, `.../addons/l10n_th_reports/` | read-only, this session — **not cited anywhere in E00** |

Tree scale as measured by this unit: **791 module directories**, of which **exactly two are
localization modules** (`l10n_th`, `l10n_th_reports`). E00 states "797-module reference tree" twice.
This matters for every categorical negative in E00 (see Challenge 12).

### Evidence-class legend (applied to this unit's own statements too)

`VERIFIED FACT` · `REFERENCE BEHAVIOUR` · `INFERENCE` · `RECOMMENDATION` · `UNKNOWN — EVIDENCE REQUIRED`

### Classification legend (Part 2)

Exactly five permitted values: `CONFIRMED BY EVIDENCE` · `CONTRADICTED` · `UNKNOWN` · `HOLD` · `VETO`.
No approval is granted anywhere in this document. Boss is sole final approver.

---

# PART 1 — FALSIFICATION OF THE EVIDENCE BASE

| Claim | Verdict | Citation read | Note |
|---|---|---|---|
| **EV-002** — account code uniqueness has NO database constraint (Python-only) | `CONFIRMED` (and materially deepened) | `account/models/account_account.py:19-21` (class `AccountAccount` opens), `:1037` `_ensure_code_is_unique`, `:1012` (create), `:1030-1033` (write), `:1455-1474` (`_sql_constraints` at `:1468` belongs to `AccountGroup`, constrains prefix length only); `odoo/fields.py:774`, `:463-473` | `VERIFIED FACT`: the account model declares no `_sql_constraints`, no `_auto_init` override and no `create_index` call. I searched the whole file and the six modules that inherit `account.account` (`account_disallowed_expenses`, `spreadsheet_account`, `account_reports`, `account_base_import`, `account_accountant`, `account_asset`) — none adds one. **Stronger than E00 states:** `code` is backed by `code_store`, declared `company_dependent=True`, and `odoo/fields.py:774` returns column type `jsonb` for any company-dependent field. The code is a key inside a JSONB blob keyed by company id. A conventional SQL unique index on (code, company) is therefore not merely absent — it is **structurally unavailable** in this storage shape, and `fields.py:465` additionally forbids a company-dependent field from being `required`. E00 frames this as an omission; it is a consequence of the storage design. Second gap E00 missed: `account_account.py:1032` re-runs the check only when `{'company_ids','code','code_mapping_ids'}` intersect the write vals — a write that targets `code_store` directly skips `_ensure_code_is_unique` entirely. |
| **EV-003** — the account model has no `active` field | `CONFIRMED` | `account/models/account_account.py:52` (`deprecated = fields.Boolean(...)`); grep for `active` across the model returns only local variables, comments and `active_company_root_id` (`:155,183,188,402,504,527,537,986,1143`); `_inherit = ['mail.thread']` at `:21`; `mail/models/mail_thread.py` declares no `active` field on the mixin | `VERIFIED FACT`. Searched: `account/models/account_account.py` plus all six inheriting modules listed above plus the `mail.thread` mixin — **not found** in those paths. The archive mechanism is genuinely absent from `account.account`. |
| **EV-009** — backdated entry silently re-dated to `lock_date + 1` rather than rejected, at `account_move.py:3127-3129` | `CONTRADICTED` (citation misattributed; rule materially different; counterexample exists) | `account/models/account_move.py:3113-3131` — lines 3127-3129 sit inside **`copy_data`**, the duplication path, not any write or post path. Real rule: `:5655-5691` `_get_accounting_date`; post path `:4932-4936`; compute path `:800-815` `_compute_date`. Counterexample: `:2377-2394` `_check_fiscal_lock_dates` **raises `UserError`**, invoked from `:3231-3237`, `:3239-3241`, `:3282-3284` | See **Challenge 1 (`VETO`)**. Three separate defects: (a) the cited lines are `copy_data`; (b) `lock_date + 1 day` is only an intermediate value inside `_get_accounting_date` — the returned date is then reshaped by the journal's **sequence-numbering reset pattern**, differently for sale and non-sale documents; (c) for non-sale documents `_get_accounting_date` is called **unconditionally from `_compute_date` with no lock date involved at all**. And an error path does exist: `_check_fiscal_lock_dates` raises on a posted move whose date/name/state change violates the lock. |
| **EV-010** — hash omits `amount_currency`, `currency_id`, tax fields, `analytic_distribution`, **and** the write guards do not block editing them on a hashed entry | `CONFIRMED WITH CAVEAT` — first half confirmed and hardened; second half **overstated** | Hash fields: `account_move.py:3832-3839`; `account_move_line.py:3283-3289`; `MAX_HASH_VERSION` `account_move.py:46`. Chain builder `:3990-4021`. Guards: `account_move.py:3207-3213`; `account_move_line.py:1554-1563`. **Other guards E00 missed:** `account_move_line.py:3365-3375` `_get_lock_date_protected_fields` — `'fiscal'` list contains `amount_currency` and `currency_id`; `'reconciliation'` list contains both as well; enforced at `:1576-1581` and `:1586-1600` via `_check_fiscal_lock_dates` / `_check_reconciliation` (`:1292-1297`). Also `:1573-1574` — `tax_ids` / `tax_line_id` are **unconditionally** refused on a posted line | I tried hardest to break this one. **Hardening for E00:** I searched all 791 module directories for any override of `_get_integrity_hash_fields` — **none exists outside `account/` and its own tests** (`account/tests/test_account_inalterable_hash.py` only reads it). No localization, no enterprise module, no separate hash covers `amount_currency`. **Correction to E00:** `amount_currency` on a hashed entry is *not* unguarded. Three further guards fire: the tax-lock guard, the fiscal-lock guard (`amount_currency`, `currency_id` are in the `'fiscal'` protected list) and the reconciliation guard. The residual exposure is real but narrow and must be stated precisely — see **Challenge 10**. E00's table row for tax fields is also wrong for `tax_ids`/`tax_line_id`, which are hard-blocked on any posted line regardless of hashing. `analytic_distribution` is in **no** guard list and is the genuinely unprotected field. |
| **EV-016** — there is NO fiscal-year model and NO year-end closing entry anywhere in the tree | `CONTRADICTED` on the first half; `CONFIRMED` on the second | **`account_accountant/models/account_fiscal_year.py:11` — `_name = 'account.fiscal.year'`.** A stored model with `name`, `date_from`, `date_to`, `company_id` (all `required=True`), an anti-overlap constraint (`:22-55`) and a constraint at `:41-42` refusing a fiscal year on a child company. Menu `account_accountant/views/account_accountant_menuitems.xml:6`, gated on group `account_accountant.group_fiscal_year`. ACL `account_accountant/security/ir.model.access.csv:7-9`. Consumed at `account_accountant/models/res_company.py:162,185,193`, `account_accountant/models/res_currency.py:10`, `account_reports/models/account_report.py:5095`. Second half: searched all 791 module dirs for `closing entr`, `closing move`, `year closing`, `cierre`, `clôture`, `Abschluss`, `_close_fiscalyear`, `year_end_closing` — only the **tax** closing entry (`account_reports/models/account_move.py`) and PoS session closing appear; `equity_unaffected` is handled at report time only (`account_reports/models/account_general_ledger.py:199-223, 314-343`, `account/models/company.py:740-766`) | See **Challenge 4**. E00's categorical negative is false and the module it missed is Enterprise `account_accountant`, which is in the declared build. The **substance** of E00's conclusion survives (no posted year-close, no carry-forward entry, no reopen operation), but the reasoning that got there — "the year boundary is purely a reporting construct, expressible as two integers on the company" — does not, because an explicit override entity exists precisely for the case the two integers cannot express (an irregular or changed fiscal year), and it is **root-company-only**. |
| **EV-020** — `COMPANY_OFFSET = 10000` id arithmetic aliases once `company_id >= 10000` | `CONFIRMED WITH CAVEAT` — arithmetic correct, trigger condition misstated | `account/models/account_code_mapping.py:4` (`COMPANY_OFFSET = 10000`), `:36-43` (`create` builds ids as `account_id * COMPANY_OFFSET + company_id`), `:45-54` (`_search` same encoding), `:56-62` (`_compute_account_id` = `id // COMPANY_OFFSET`, `_compute_company_id` = `id % COMPANY_OFFSET`), `:64-70` (`_compute_code` / `_inverse_code` resolve `account_id.with_company(company_id)` from the decoded pair) | The aliasing is real and I could find **no bound on it** — no guard, no assert, no domain restriction, no ceiling on `company_id`. Worked example: account `5`, company `10003` encodes to `60003`, which decodes to account `6`, company `3`. `_inverse_code` then writes the code onto the wrong account for the wrong company. **Correction to E00:** E00 says the failure begins "the moment a deployment holds ten thousand or more company records". That is the wrong trigger. The encoding depends on the **`res_company` primary-key value**, not the row count. A tenant with twelve companies aliases if the `res_company` id sequence has advanced beyond 10000 — which it does through ordinary create/delete churn, data imports, or a restored or merged database, all of which advance a Postgres sequence without leaving rows behind. `INFERENCE:` the finding is therefore worse than E00 states, not better, and it is reachable long before a deployment is large. Secondary observation E00 missed: `_search` at `:47-52` iterates `self.env.user.company_ids`, i.e. the **user's** allowed companies, not the account's `company_ids`. |
| **EV-021** — an accounting manager can create a lock exception with no user and no end date (permanent, global); reason optional; access-control reading | `CONFIRMED WITH CAVEAT` on the exception shape; `CONTRADICTED` on "append-only"; column labelling in E00 is wrong | ACL header `account/security/ir.model.access.csv:1` — `id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink`. Row `:18` `base.group_user` → `1,0,0,0`. Row `:19` `account.group_account_manager` → `1,0,1,0`. These are the only two rows for this model in the whole tree. Model: `account/models/account_lock_exception.py:37-40` (`user_id` — "An exception w/o user_id is an exception for everyone", **`default=lambda self: self.env.user`**), `:42-44` (`reason`, no `required`), `:46-48` (`end_datetime`, no `required`, "valid forever"), `:16-19` (**`active` field, default True**), `:20-28` (`state` computed active/revoked/expired), `:258-267` **`action_revoke`**, `:242` `copy` raises, `:274-300` `_get_audit_trail_during_exception_domain` | Three corrections. **(1)** E00 labels the tuple "create/write/delete permissions are `1,0,1,0` and `1,0,0,0`". The four columns are `read,write,create,unlink`, not create/write/delete, and E00's "respectively" reads against its own prose order (users named first, manager second), which inverts the two rows. The **values** E00 quotes are correct and its prose conclusion — manager may read and create, not write, not unlink — is correct. **(2)** E00's consequence "exceptions are append-only" is `CONTRADICTED`: `action_revoke` at `:258-267` gates on `group_account_manager` then calls `record.sudo().active = False` and `record_sudo.end_datetime = now()`. The ACL is bypassed by `sudo()` inside the model's own action. Exceptions are revocable by any accounting manager. **(3)** E00 states the "permanent global unlock" risk without noting that `user_id` **defaults to the acting user** (`:40`) — the global form requires the field to be deliberately cleared. E00 also missed a compensating control it should have credited: `_get_audit_trail_during_exception_domain` (`:274-300`) builds a domain that lists what was changed during the exception window. |

---

# PART 2 — INDEPENDENT ATTACK

Twelve challenges the research team did not report.

---

## CHALLENGE 1 — The accounting date of a purchase document is set by the journal's numbering format, with no lock date involved

**CHALLENGE.** E00 declares EV-009 "the single most load-bearing semantic in section F" and states the
rule as: intended date ≤ lock date ⇒ `date = lock_date + 1 day`. That rule is not what the reference
implementation does, and the lines cited to prove it are in the record-duplication path.

**TARGET.** EV-009 in full, and every downstream statement that rests on it — EV-015 (which cites
"the same lock-shift as EV-009"), and the Wave D carry-forward that defers the Thai period-attribution
question on the strength of this description.

**EVIDENCE.**

`VERIFIED FACT` — `account/models/account_move.py:3113-3131`. Lines 3127-3129 are inside
`copy_data(self, default=None)`, which begins at `:3113`. They govern **duplicating** a move. They are
not on any write path, post path or user-entry path.

`VERIFIED FACT` — the operative routine is `_get_accounting_date` at `account/models/account_move.py:5655-5691`.
Its structure, read verbatim from source:

```
lock_dates    = lock_dates or self._get_violated_lock_dates(invoice_date, has_tax)   # :5669
highest_name  = self.highest_name or self._get_last_sequence(relaxed=True)           # :5671
number_reset  = self._deduce_sequence_number_reset(highest_name)                     # :5672
if lock_dates:
    invoice_date = lock_dates[-1][0] + timedelta(days=1)                             # :5674
if self.is_sale_document(include_receipts=True):
    if lock_dates:
        if not highest_name or number_reset == 'month':
            return min(today, date_utils.get_month(invoice_date)[1])                 # :5677-5678
        elif number_reset == 'year':
            return min(today, date_utils.end_of(invoice_date, 'year'))               # :5679-5680
else:
    if not highest_name or number_reset in ('month', 'year_range_month'):
        if (today.year, today.month) > (invoice_date.year, invoice_date.month):
            return date_utils.get_month(invoice_date)[1]                             # :5683-5684
        else:
            return max(invoice_date, today)                                          # :5685-5686
    elif number_reset == 'year':
        if today.year > invoice_date.year:
            return date(invoice_date.year, 12, 31)                                   # :5687-5688
        else:
            return max(invoice_date, today)                                          # :5689-5690
return invoice_date                                                                  # :5691
```

`lock_date + 1 day` is an **intermediate** value at `:5674`. The value actually returned is then chosen
by `number_reset` — the reset pattern deduced from the journal's document-numbering format — and by
whether the document is a sale document.

`VERIFIED FACT` — `account/models/account_move.py:800-815`, `_compute_date`, `@api.depends('invoice_date','company_id')`:

```
accounting_date = move.invoice_date                                                  # :807
if not move.is_sale_document(include_receipts=True):
    accounting_date = move._get_accounting_date(move.invoice_date, move._affect_tax_report())   # :808-809
if accounting_date and accounting_date != move.date:
    move.date = accounting_date                                                      # :810-811
```

For a **non-sale** document `_get_accounting_date` is called **unconditionally**. There is no lock-date
predicate. The `else` branch at `:5682-5690` executes whether or not any lock date exists.

`INFERENCE` (labelled, not promoted) — worked consequence, no lock dates configured, today 2026-09-04,
purchase journal with monthly number reset: a vendor bill with `invoice_date` 2026-07-15 satisfies
`(2026,9) > (2026,7)` and is booked at `date_utils.get_month(2026-07-15)[1]` = **2026-07-31**. The same
bill dated 2026-09-01 falls to `max(2026-09-01, today)` = **2026-09-04**. Neither result is the document
date and neither involves a lock date. Change the journal's numbering format to annual reset and the
same bill books to 2026-12-31 or to today instead. `UNKNOWN — EVIDENCE REQUIRED:` runtime confirmation
of these three outcomes on a live instance; the reasoning above is read from source, not executed.

`VERIFIED FACT` — the counterexample E00 asked for exists. `account/models/account_move.py:2377-2394`
`_check_fiscal_lock_dates` raises `UserError("You cannot add/modify entries prior to and inclusive of: …")`.
It is invoked at `:3235`, `:3240` and `:3282-3284`. Lock-date violation is therefore **not** uniformly
silent: it is silent on the soft re-date path and loud on the posted-move write path. It carries a
context bypass at `:2378` (`bypass_lock_check is BYPASS_LOCK_CHECK`, sentinel defined at `:83`).

**CLASSIFICATION: `VETO`.**

Exact evidence and reason, as required for a veto. E00 asserts one uniform semantic — *"if the intended
date is on or before that lock date, the values dictionary is rewritten so that `date = lock_date + 1 day`"*
— cited to `account_move.py:3127-3129`, and designates it the load-bearing semantic of section F. Source
at `:3113-3131` shows those lines are `copy_data`. Source at `:5655-5691` and `:800-815` shows the
operative rule is (i) different in form, (ii) **asymmetric between sale and non-sale documents**, (iii)
parameterised by the journal's **document-numbering reset pattern**, and (iv) **active with no lock date
present at all** for non-sale documents. A semantic model built on E00's statement would place vendor
bills on the wrong recognition date in the ordinary, unlocked case. This is the definition of a wrong
financial recognition point, and it invalidates the section-F semantic as written. The veto is on
EV-009's **stated rule and citation**, not on the existence of soft re-dating, which is real.

**REQUIRED RESOLUTION.**
1. EV-009 withdrawn and re-drafted against `:5655-5691` and `:800-815`, with the `copy_data` citation removed.
2. The sale / non-sale asymmetry stated explicitly, as two rules, not one.
3. The dependency of recognition date on numbering format recorded as a distinct finding, and put to Boss as a `Tolerance = 0` candidate: in SMEsPlus, **document numbering must not be an input to the recognition date**.
4. `_check_fiscal_lock_dates` (`:2377-2394`) recorded as the rejecting path, with its `bypass_lock_check` sentinel.
5. EV-015 re-checked, since it cites EV-009 as its mechanism.
6. The Wave D Thai carry-forward re-opened — it was deferred on a description of the mechanism that does not hold. Thai statutory consequence remains `HOLD / EVIDENCE REQUIRED`, Accounting-Tax track.

---

## CHALLENGE 2 — The integrity hash rounds company-currency amounts to the foreign currency's decimal precision

**CHALLENGE.** The hash serialiser rounds `debit` and `credit` — which are **company-currency** fields —
using the decimal places of the line's **transaction** currency. Two materially different company-currency
amounts can therefore produce an identical hash.

**TARGET.** EV-010's conclusion that "for a single-currency ledger the hash is sound". It is not sound
whenever a line carries a transaction currency with fewer decimal places than the company currency.

**EVIDENCE.**

`VERIFIED FACT` — `account/models/account_move_line.py:113-121`: `debit` and `credit` are
`fields.Monetary(..., currency_field='company_currency_id')`. `:123-127`: `balance` likewise.

`VERIFIED FACT` — `account/models/account_move.py:3994-4001`, inside `_calculate_hashes`:

```
def _getattrstring(obj, field_name):
    field_value = obj[field_name]
    if obj._fields[field_name].type == 'many2one':
        field_value = field_value.id
    if obj._fields[field_name].type == 'monetary' and hash_version >= 3:
        return float_repr(field_value, obj.currency_id.decimal_places)
    return str(field_value)
```

The precision argument is `obj.currency_id.decimal_places` — the line's transaction currency — applied to
a value denominated in `company_currency_id`. `currency_id` is `required=True` on every line
(`account_move_line.py:142-148`), so it is always populated and always the one used.

`INFERENCE` (labelled) — company currency THB (2 dp), line transaction currency JPY (0 dp): company-currency
`debit` values 1234.56 and 1234.99 both serialise as `"1235"` and produce the same `sha256` input. The
entry is materially altered and the integrity report reports it intact.

`VERIFIED FACT` — no override of `_get_integrity_hash_fields` and no override of `_calculate_hashes`
exists anywhere in the 791 module directories (searched `--include=*.py` across the whole addons tree;
the only other occurrences are in `account/tests/test_account_inalterable_hash.py:214,221`, which read
the method). No localization corrects this.

**CLASSIFICATION: `CONFIRMED BY EVIDENCE`.**

**REQUIRED RESOLUTION.** Recorded as a new contradiction alongside `CONTRA-01`. For SMEsPlus: any
integrity digest must serialise each amount at the precision of **its own** denominating currency, and
that pairing must be part of the digest input, not an ambient property read from a sibling field.
`RECOMMENDATION:` Boss decision required on whether digest coverage is a `Tolerance = 0` control.

---

## CHALLENGE 3 — The hash chain does not span periods, is keyed on database row ids, and the verifier has no completeness check

**CHALLENGE.** E00 describes the hash as a chained integrity mechanism without examining the chain's
scope, its keying, or what the verification routine actually detects. All three are weaker than implied.

**TARGET.** EV-010 and EV-011's characterisation of hashing as the immutability mechanism.

**EVIDENCE.**

`VERIFIED FACT` — chain scope. `account/models/account_move.py:3884-3941` `_get_chain_info`: the chain's
`common_domain` is `[('journal_id','=',journal.id), ('sequence_prefix','=', last_move_in_chain.sequence_prefix)]`
(`:3895-3898`), the predecessor is the highest-`sequence_number` hashed move **within that prefix**
(`:3899-3903`), and `_get_chains_to_hash` (`:3946-3990`) groups by `journal_id` then by `sequence_prefix`
(`:3958-3959`). `INFERENCE:` because `sequence_prefix` changes at each period reset, each period is an
**independent chain with its own genesis**. Deleting or rebuilding one period's chain leaves every other
chain verifying intact. The chain is not evidence of cross-period completeness.

`VERIFIED FACT` — keying on row id. `account/models/account_move.py:4014-4016`: line values enter the
digest under the key `'line_%d_%s' % (line.id, fname)`. The digest is bound to **physical database
primary keys**. `INFERENCE:` any migration, restore-into-new-database, or id-renumbering invalidates
every stored hash, and a hash cannot be recomputed from a logical export. This is directly material to
SMEsPlus, whose programme is a migration.

`VERIFIED FACT` — chain order. `_calculate_hashes` chains in recordset order; `_get_chain_info` searches
`order='sequence_number'` (`:3918`). The chain therefore asserts **numbering order**, while the hashed
field set includes `date`. Given Challenge 1, numbering order and date order diverge routinely.

`VERIFIED FACT` — verification is incomplete. `account/models/company.py:911-990` `_check_hash_integrity`:
- `:955-956` — `if prefix_result['corrupted_move']: continue`. Once one corrupted move is found in a
  prefix, the rest of that prefix is not checked. The report gives existence, never extent.
- `:952,959-962` — `current_hash_version` is initialised to `1` **inside the fetch-batch loop** and walks
  upward until the stored hash matches. A hash stored at version 1 verifies as intact, and version 1
  covers only `['date','journal_id','company_id']` / `['debit','credit','account_id','partner_id']`
  (`account_move.py:3835-3836`, `account_move_line.py:3286-3287`) — **`name` is not covered at v1**.
  Because the counter resets per `INTEGRITY_HASH_BATCH_SIZE` batch, verification behaviour depends on
  batch boundaries.
- `:911-990` contains **no sequence-gap check**. Gap detection exists only at hashing time
  (`account_move.py:3921-3933`, `:3977-3986`). `INFERENCE:` truncating a chain by removing its
  highest-numbered hashed moves leaves nothing for the verifier to compare against.
- `:926` — the query runs under `sudo()`; `:931` orders by `secure_sequence_number ASC NULLS LAST,
  sequence_prefix, sequence_number ASC` and `:957` selects the predecessor from **two different chain
  definitions** depending on whether `secure_sequence_number` is set. Two chain semantics are walked by
  one report.

`VERIFIED FACT` — hashing is coupled to bank reconciliation: `account_move.py:3931-3933` sets an
`'unreconciled'` warning and `:3970-3971` raises *"An error occurred when computing the inalterability.
All entries have to be reconciled."*

**CLASSIFICATION: `CONFIRMED BY EVIDENCE`.**

**REQUIRED RESOLUTION.** EV-010/EV-011 extended with chain scope, id-keying, verifier completeness and the
reconciliation coupling. For SMEsPlus, put to Boss: (a) must an integrity digest survive migration —
if yes it cannot be keyed on physical ids; (b) must the chain be continuous across period boundaries;
(c) must verification report **extent** of corruption, not first occurrence. `RECOMMENDATION` only —
no design is adopted here.

---

## CHALLENGE 4 — A fiscal-year entity exists in the declared build and was not found

**CHALLENGE.** EV-016 opens with a categorical negative — *"A search for a fiscal-year model definition
across the entire 797-module reference tree returns no result"* — and builds its whole conclusion on it.
The model exists, in the Enterprise module that gives this build its name.

**TARGET.** EV-016, and E00's stated evidence-search method.

**EVIDENCE.**

`VERIFIED FACT` — `account_accountant/models/account_fiscal_year.py:11` — `_name = 'account.fiscal.year'`,
`_description = 'Fiscal Year'`. Fields `name`, `date_from`, `date_to`, `company_id`, all `required=True`
(`:14-20`). `@api.constrains('date_from','date_to','company_id')` at `:22-55` refuses inverted dates and
refuses any overlap between fiscal years of one company.

`VERIFIED FACT` — `account_accountant/models/account_fiscal_year.py:41-42`:
`if fy.company_id.parent_id: raise ValidationError('You cannot have a fiscal year on a child company.')`.
Fiscal-year overrides are **root-company only**. A subsidiary in a group cannot carry a divergent fiscal
year.

`VERIFIED FACT` — it is wired in, not vestigial: registered `account_accountant/models/__init__.py:7`;
menu `account_accountant/views/account_accountant_menuitems.xml:6` behind group
`account_accountant.group_fiscal_year`; ACL `account_accountant/security/ir.model.access.csv:7-9`
(readonly `1,0,0,0`, basic `1,0,0,0`, manager `1,1,1,1`); consumed by
`account_accountant/models/res_company.py:162,185,193`, `account_accountant/models/res_currency.py:10`
and `account_reports/models/account_report.py:5095`.

`VERIFIED FACT` — EV-016's second half stands. I searched all 791 module directories for
`closing entr|closing move|year closing|cierre|clôture|Abschluss|_close_fiscalyear|year_end_closing|closing_entry|end_of_year`
and for `unaffected_earnings|equity_unaffected`. The only "closing entry" is the **tax** closing
(`account_reports/models/account_move.py`) and PoS session closing. The profit-and-loss-to-equity
attribution is computed at report time only (`account_reports/models/account_general_ledger.py:199-223,
314-343`; `account/models/company.py:740-766`). **Searched those paths, no posted year-end closing entry
found.**

`INFERENCE` — the model is a **reporting-period override**, not a closing entity: it has no state, no
open/close action, and no link to journal entries. EV-016's *conclusion* therefore survives. Its
*reasoning* does not: E00 argues the year boundary is "purely a reporting construct" expressible as two
integers on the company, and the reference implementation shipped a separate stored entity precisely
because the two integers cannot express an irregular or changed fiscal year.

**CLASSIFICATION: `CONTRADICTED`.**

**REQUIRED RESOLUTION.** EV-016 amended: state the model, its root-company-only constraint, its
group-gating, and its role as a reporting-period override. Restate the surviving negative with scope
attached. E00's search method for categorical negatives must be re-run for every other categorical
negative it makes (see Challenge 12). The SMEsPlus design question changes shape: not "should there be a
fiscal-year entity" but "must an irregular or changed fiscal year be a first-class record, and must
subsidiaries be permitted to diverge from the group" — Boss decision, not decided here.

---

## CHALLENGE 5 — Rate types (current, closing, historical, average) do exist, in a file E00 declared verified

**CHALLENGE.** EV-018 concludes *"There is no rate type dimension — no separate spot, average, closing or
historical rate"*, and files its own follow-up question — whether the reporting layer synthesises an
average rate — as `UNKNOWN`, deferred to Wave G. Both statements are answered inside `SRC-A`, the module
E00 lists as "Read, verified this session".

**TARGET.** EV-018's consequence paragraph and its deferral.

**EVIDENCE.**

`VERIFIED FACT` — `account/models/res_currency.py:130-134`:
`CREATE TEMPORARY TABLE account_currency_table (company_id, period_key, date_from, date_next, rate_type, rate) ON COMMIT DROP`.
A `rate_type` column exists.

`VERIFIED FACT` — `account/models/res_currency.py:113-121`: when `use_cta_rates` is set the builders are
`_get_table_builder_closing`, `_get_table_builder_historical` and `_get_table_builder_average`; otherwise
`_get_table_builder_current`. `:148-155` emits the literal rate types `'average'`, `'historical'`,
`'closing'`; `:157` emits `'current'`.

`VERIFIED FACT` — the types are consumed in reporting: `account_reports/models/account_report.py:1415` —
income, expense and `equity_unaffected` accounts are translated at `'average'`, the remainder at the
other types.

`VERIFIED FACT` — EV-018's **stored-model** claim is correct and unchallenged: `base/models/res_currency.py`
holds one scalar per (date, currency, company) with a unique constraint. The four rate types are
**derived at report time from that single stored scalar**, not stored.

`VERIFIED FACT` — a correctness defect inside the derivation, unreported by E00.
`account/models/res_currency.py:227-241` `_get_currency_table_fiscal_year_bounds` builds historical
fiscal-year bounds by taking the **current** fiscal year and replaying its month/day pattern backwards
over civil years (`for civil_year in range(...): year_delta = relativedelta(years=...)`). It assumes the
fiscal year has never changed. `account_accountant/models/res_currency.py:8-26` overrides this to splice
in real `account.fiscal.year` records — but only when `account_accountant` is installed.
`INFERENCE:` for an entity that changed its fiscal-year end, closing-rate bounds for historical years are
silently wrong unless the Enterprise module is present. This is the same gap as Challenge 4, surfacing as
a numeric error rather than a missing entity.

`VERIFIED FACT` — group boundary: every builder joins `res_currency_rate` on
`rate.company_id = %(main_company_id)s` where `main_company_id = main_company.root_id.id`
(`:171,175`, `:203,208`). Rates are read from the **root** company only; a subsidiary cannot carry its own
rate for consolidated reporting.

**CLASSIFICATION: `CONTRADICTED`.**

**REQUIRED RESOLUTION.** EV-018's consequence paragraph withdrawn and re-drafted: the stored model has one
rate per day; the **reporting layer materialises four rate types from it**, and the requirement E00 says
"has no carrier in this structure" does have a carrier — a derived one, with the fiscal-year defect above.
EV-018's `UNKNOWN — deferred to Wave G` is closed by `_get_table_builder_average`. `RECOMMENDATION:`
E00's deferral discipline needs a rule — a question may not be deferred to a later wave while its answer
sits in a module already declared read.

---

## CHALLENGE 6 — Lock exceptions are revocable through a sudo path inside the model, so the access-control reading does not carry the control conclusion

**CHALLENGE.** EV-021 reasons from the ACL (`perm_write=0`, `perm_unlink=0`) to the control conclusion
*"exceptions are append-only and logged"*. The model bypasses its own ACL.

**TARGET.** EV-021's consequence paragraph, and more generally E00's method of inferring a control
property from an access-control row.

**EVIDENCE.**

`VERIFIED FACT` — `account/models/account_lock_exception.py:258-267`:

```
def action_revoke(self):
    if not self.env.user.has_group('account.group_account_manager'):
        raise UserError(...)
    for record in self:
        if record.state == 'active':
            record_sudo = record.sudo()
            record_sudo.active = False
            record_sudo.end_datetime = fields.Datetime.now()
```

`sudo()` bypasses `perm_write=0`. Any accounting manager can revoke. `_recreate` at `:243-253` calls
`self.sudo().action_revoke()` as part of its normal flow.

`VERIFIED FACT` — `:16-19` the model carries an `active` field (`default=True`), and `:20-28` a `state`
selection computed `revoked` when `not active`. The revocation concept is first-class in the model; the
ACL simply does not govern the path that uses it.

`VERIFIED FACT` — `:37-40`, `user_id` carries `default=lambda self: self.env.user`. The "applies to
everyone" form requires the field to be cleared deliberately.

`VERIFIED FACT` — compensating control E00 did not credit: `:274-300`
`_get_audit_trail_during_exception_domain` composes a domain over messages and tracking values bounded by
the exception's `create_date`, `end_datetime`, `lock_date` and `company_lock_date`, restricted to
`create_uid = user_id` where a user is named. The system can enumerate what changed during the window.
`INFERENCE:` that control **degrades exactly in the case E00 flags as the risk** — with no `user_id` the
`create_uid` restriction is dropped, and with no `end_datetime` the upper time bound is dropped, so the
"permanent global" exception is also the one whose audit domain is least selective.

`VERIFIED FACT` — `:242` `copy` raises `UserError('You cannot duplicate a Lock Date Exception.')`.
`:97-106` an index is created on `(company_id, user_id, end_datetime) WHERE active = TRUE`.

**CLASSIFICATION: `CONTRADICTED`.**

**REQUIRED RESOLUTION.** EV-021's "append-only" withdrawn; replaced with: creation is manager-gated and
chatter-logged, revocation is manager-gated through an in-model `sudo()` path, and the record is not
immutable. Credit the audit-trail domain as a compensating control and record its degradation in the
unbounded case. `RECOMMENDATION:` for SMEsPlus, an override record must carry a mandatory reason, a
mandatory expiry, a named subject, and must be immutable in fact rather than by access-control row —
Boss decision.

---

## CHALLENGE 7 — Six named context flags disable core ledger controls on the write path; E00 records four of them piecemeal and never as a pattern

**CHALLENGE.** E00 notes `defer_account_code_checks` (EV-002), `skip_readonly_check` (EV-022) and
`force_delete` (EV-011) individually, each as a local observation. They are instances of one systemic
design property: the ledger's controls are Python guards, each with a documented keyword that turns it
off, and the set is larger than E00 reports.

**TARGET.** EV-002, EV-011, EV-022, and the absence of any systemic control-design finding in E00.

**EVIDENCE.**

`VERIFIED FACT` — the flags, each read at its guard site:

| Flag | Guard it disables | Citation |
|---|---|---|
| `bypass_lock_check` (sentinel `BYPASS_LOCK_CHECK`) | the lock-date rejection itself | `account/models/account_move.py:83`, `:2378`; used `account/models/partner.py:804-805` |
| `skip_readonly_check` | the posted-move readonly field list | `account/models/account_move.py:3249-3251` |
| `force_delete` | audit-trail deletion block **and** sequence-chain deletion block | `account/models/account_move.py:3330-3347`, `:3350-3358` |
| `skip_account_deprecation_check` | the deprecated-account posting block | `account/models/account_move.py:4911`; `account/models/account_move_line.py:1212` |
| `defer_account_code_checks` | account-code uniqueness | `account/models/account_account.py:1004`, `:1030-1033` |
| `skip_is_manually_modified` | the manual-modification marker | `account/models/account_move.py:3264-3265` |

`VERIFIED FACT` — counted across `account/`, `account_accountant/` and `account_reports/`, excluding
tests: **28 non-test call sites** set one of these flags. They appear in
`account/models/account_move.py`, `account/models/account_move_line.py`, `account/models/partner.py`,
`account/models/account_bank_statement_line.py`, `account_accountant/models/bank_rec_widget.py`,
`account_accountant/models/account_move.py`, `account_asset/models/account_asset.py`,
`account_reports/models/account_deferred_reports.py`.

`VERIFIED FACT` — a seventh, of a different kind, already recorded by E00 as EV-007: the configuration
parameter `sequence.mixin.constraint_start_date` (`account/models/sequence_mixin.py:154-179`), which is
tenant-writable data rather than a call-site keyword.

`INFERENCE` — none of these flags leaves an accounting-level trace. `force_delete` writes to the
application logger (`account/models/account_move.py:3366-3367`, `_logger.info`), i.e. outside the tenant
database; the other five write nothing. A control that can be silently disabled per call site is a
control whose effectiveness cannot be asserted from the schema.

**CLASSIFICATION: `CONFIRMED BY EVIDENCE`.**

**REQUIRED RESOLUTION.** A consolidated bypass register for Wave A, listing every guard and its disable
mechanism, replacing the three scattered mentions. Put to Boss as a `Tolerance = 0` candidate under
constitution principle 13: in SMEsPlus, any path that disables a ledger integrity control must be
enumerable, permissioned, and must write an accounting-visible record — not an application log line.

---

## CHALLENGE 8 — The Thai localization is in the tree, was never read, and it settles two questions E00 deferred

**CHALLENGE.** E00 raises Thai VAT and WHT period attribution as an `INFERENCE` and defers it to Wave D
as not decidable. `l10n_th` and `l10n_th_reports` are in the same build, are the only two localization
modules present, and are cited nowhere in EV-000 through EV-023.

**TARGET.** EV-000's evidence-source registry, EV-009's Wave D deferral, and E00's treatment of the
chart of accounts.

**EVIDENCE.**

`VERIFIED FACT` — the modules are present:
`l10n_th/models/template_th.py`, `l10n_th/data/template/account.account-th.csv`,
`l10n_th/data/template/account.tax-th.csv`, `l10n_th/data/account_tax_report_data.xml`,
`l10n_th_reports/models/tax_report_pnd.py`, `l10n_th_reports/models/tax_report_vat.py`.

`VERIFIED FACT` — the reference Thai chart of accounts is **27 accounts** (28 CSV lines including the
header) with columns `id,name,code,account_type,reconcile` only
(`l10n_th/data/template/account.account-th.csv`). It carries no group structure, no dimension, no
statutory mapping. `l10n_th/models/template_th.py:10-31` maps four property accounts and eight company
defaults, and nothing else.

`VERIFIED FACT` — **the WHT report is driven by the field Challenge 1 shows is reshaped.**
`l10n_th_reports/models/tax_report_pnd.py:32,55` — the PND extract orders and dates every row by
`account_move_line__move_id.date`, the move's **accounting** date, the same field that
`_get_accounting_date` rewrites. `INFERENCE:` the mechanical coupling between the re-dating rule and the
period a withholding row lands in is a **code fact readable in this tree**, not an open question. E00
deferred it as undecidable without opening the module.

`VERIFIED FACT` — **semantic conflation in the reference WHT design.**
`l10n_th_reports/models/tax_report_pnd.py:47-53`:

```
CASE tax.amount
    WHEN -1 THEN 'Transportation'
    WHEN -2 THEN 'Advertising'
    WHEN -3 THEN 'Service'
    WHEN -5 THEN 'Rental'
    ELSE ''
END tax_type
```

The tax **rate** field carries the withholding **category**, encoded as a negative number, and the same
field is simultaneously used as an arithmetic rate at `:45`
(`ROUND(ABS(tax.amount * account_move_line.tax_base_amount / 100), …)`). One field, two concepts, one of
them a magic-number enumeration. `:44` hardcodes `'1' as wht_condition`.

`HOLD / EVIDENCE REQUIRED` — whether that encoding, the 27-account chart, or the PND column set satisfy
any Thai statutory requirement. **This unit asserts no Thai law.** Routed to the Accounting-Tax track.

**CLASSIFICATION: `CONFIRMED BY EVIDENCE`** for the evidence-gap and the conflation;
**`HOLD`** for every statutory question arising from it.

**REQUIRED RESOLUTION.**
1. `SRC-F` added to EV-000 and both modules read before Wave A is presented as complete.
2. EV-009's Wave D deferral re-scoped: the mechanical coupling is decidable now; only the statutory consequence is `HOLD`.
3. The rate/category conflation recorded as a named anti-pattern for the SMEsPlus tax model: a rate field must never carry a classification.
4. The 27-account chart recorded as a `VERIFIED FACT` bearing on any Boss decision that assumes a usable Thai baseline exists in the reference tree.

---

## CHALLENGE 9 — EV-002's control weakness is understated: uniqueness is not merely unconstrained, it is unconstrainable in this storage shape

**CHALLENGE.** E00 presents the missing database constraint as an omission that SMEsPlus should correct
with a `Tolerance = 0` control. The omission follows from a storage decision E00 itself documents in
EV-001 without connecting the two — and there is a second uncovered write path.

**TARGET.** EV-002's `INFERENCE` paragraph, and the seam between EV-001 and EV-002.

**EVIDENCE.**

`VERIFIED FACT` — `account/models/account_account.py:50-51`: `code` is computed/searchable/inverse-backed
by `code_store = fields.Char(company_dependent=True)`.

`VERIFIED FACT` — `odoo/fields.py:774`:
`return ('jsonb','jsonb') if self.company_dependent or self.translate else self._column_type`.
The column materialised for `code_store` is `jsonb`, keyed by company id.

`VERIFIED FACT` — `odoo/fields.py:463-469`: a `company_dependent` field cannot be `required` and cannot be
`translate`d; the framework warns rather than permitting it.

`INFERENCE` (labelled) — a unique index over "the code for company X" would have to index a **key inside
a JSONB document**, per company, with the set of companies unknown at schema time. A conventional unique
constraint cannot express it. EV-002's "no `_sql_constraints`" is therefore a **consequence** of EV-001's
storage design, not an independent oversight. E00 records both facts and does not join them, and its
`Tolerance = 0` recommendation is made without acknowledging that satisfying it forecloses the
per-company-code design EV-001 endorses.

`VERIFIED FACT` — second uncovered path. `account/models/account_account.py:1032`:
`if not self.env.context.get('defer_account_code_checks') and {'company_ids','code','code_mapping_ids'} & vals.keys():`.
`code_store` is not in that set. A write addressing `code_store` directly does not trigger
`_ensure_code_is_unique` at all — a bypass that needs no context flag.

**CLASSIFICATION: `CONFIRMED BY EVIDENCE`.**

**REQUIRED RESOLUTION.** EV-002 amended to state the JSONB storage shape and the `code_store` write path.
The `Tolerance = 0` recommendation re-put to Boss as an explicit trade-off: **per-company account codes
and database-enforced code uniqueness are mutually exclusive under this storage shape.** SMEsPlus must
choose which it wants; E00 currently recommends both. Clean-room: the trade-off is transferable, the
storage design is not proposed for copying.

---

## CHALLENGE 10 — EV-010's write-guard claim is overstated, and it names the wrong field as the exposure

**CHALLENGE.** EV-010 states that the fields outside the hash "are therefore neither blocked on write nor
detected by the integrity report". The detection half is correct. The blocking half is not: three further
guards cover `amount_currency`, and one covers tax fields outright. Meanwhile the field that genuinely
has no guard at all is one E00 lists but does not single out.

**TARGET.** EV-010's consequence paragraph and `CONTRA-01` as currently drafted.

**EVIDENCE.**

`VERIFIED FACT` — `account/models/account_move_line.py:3365-3375`:

```
tax_fnames            = ['balance', 'tax_line_id', 'tax_ids', 'tax_tag_ids']
fiscal_fnames         = tax_fnames + ['account_id', 'journal_id', 'amount_currency', 'currency_id', 'partner_id']
reconciliation_fnames = ['account_id', 'date', 'balance', 'amount_currency', 'currency_id', 'partner_id']
```

`amount_currency` and `currency_id` appear in **both** the fiscal and the reconciliation protected sets.

`VERIFIED FACT` — enforcement, `account/models/account_move_line.py:1576-1600`: on a line whose
`parent_state == 'posted'`, a change to any `protected_fields['fiscal']` member calls
`move_id._check_fiscal_lock_dates()` (which raises, per Challenge 1); a change to any
`protected_fields['reconciliation']` member calls `_check_reconciliation()` (`:1292-1297`), which raises
if the line carries any `matched_debit_ids` or `matched_credit_ids`.

`VERIFIED FACT` — `account/models/account_move_line.py:1573-1574`: on a posted line, a change to
`tax_ids` or `tax_line_id` raises **unconditionally** — *"You cannot modify the taxes related to a posted
journal item"*. EV-010's table row asserting tax fields are editable is wrong for these two.

`VERIFIED FACT` — `analytic_distribution` (`account/models/account_move_line.py:393-395`) appears in
**none** of the three protected sets, is not in `account_move.py:3247-3252`'s unmodifiable list, and is not
hashed. Its inverse `_inverse_analytic_distribution` (`:1184-1190`) **unlinks and recreates** the analytic
lines of any posted line, without any lock, hash or reconciliation check.

`INFERENCE` (labelled) — the accurate residual exposure for `amount_currency` on a hashed entry is the
intersection: hashed **and** not reconciled **and** dated outside every applicable lock date. That window
is real and routine — an entry hashed at post time in the still-open current period sits inside it — but
it is narrower than E00 asserts, and an auditor who tests E00's statement against a reconciled or locked
entry will find it does not reproduce, which damages the whole register's credibility. For
`analytic_distribution` no such intersection is needed: it is editable on any posted, hashed, reconciled,
locked entry, and the edit destroys and rebuilds the analytic subledger.

**CLASSIFICATION: `CONFIRMED BY EVIDENCE`.**

**REQUIRED RESOLUTION.** `CONTRA-01` re-drafted with the exact residual window stated as a conjunction,
and with `analytic_distribution` promoted to the headline exposure, cross-referenced to EV-012 (which
already establishes analytic lines as derived artefacts with no independent history). The Wave A
statement to Boss should be: the hash secures a **subset** of the posting; two other mechanisms —
lock dates and reconciliation state — cover an overlapping but different subset; and one dimension is
covered by none of the three.

---

## CHALLENGE 11 — Managers can delete mid-chain and create sequence gaps; a detective control for exactly this exists and E00 does not mention it

**CHALLENGE.** EV-005 and EV-006 present numbering integrity as resting on a partial unique index and
otherwise uncontrolled. Both halves need correction: deletion can open gaps that the index cannot see,
and a stored, indexed, dashboard-surfaced gap detector exists.

**TARGET.** EV-005, EV-006 and EV-011.

**EVIDENCE.**

`VERIFIED FACT` — `account/models/account_move.py:3350-3358` `_unlink_forbid_parts_of_chain`:

```
if not (
    self.env.user.has_group('account.group_account_manager')
    or any(self.company_id.mapped('quick_edit_mode'))
    or self._context.get('force_delete')
    or self.check_move_sequence_chain()
):
    raise UserError("You cannot delete this entry, as it has already consumed a sequence number and is not the last one in the chain. …")
```

The condition short-circuits on group membership. An accounting manager deletes a move from the middle of
a numbering chain with **no error and no warning**. The docstring at `:3330-3337` states the intent is a
warning for managers; no warning is emitted at this call site.

`VERIFIED FACT` — the detective control E00 omits: `account/models/account_move.py:300`
`made_sequence_gap = fields.Boolean(compute='_compute_made_sequence_gap', store=True)`; computed at
`:929-940` as `move.sequence_number > 1 and (move.sequence_number - 1) not in previous_numbers`;
maintained on deletion and on write at `:2186`, `:3258`, `:3361`, `:4995-5011`; backed by a partial index
`where="made_sequence_gap = TRUE"` at `:751`; surfaced on the accounting dashboard at
`account/models/account_journal_dashboard.py:144,164`.

`VERIFIED FACT` — `:929-931`: **every unposted move is flagged `made_sequence_gap = True`**, so the
indicator conflates "a number is missing" with "a number is not yet posted".

`INFERENCE` — E00's numbering sections therefore misstate the control posture in both directions: it
omits a preventive weakness (manager mid-chain deletion) and omits a detective strength (the stored gap
flag), and the detective control it omits is itself semantically overloaded.

**CLASSIFICATION: `CONFIRMED BY EVIDENCE`.**

**REQUIRED RESOLUTION.** EV-005/EV-006 extended with both. For SMEsPlus, put to Boss: whether numbering
**completeness** is a distinct control objective from numbering **uniqueness** — the reference
implementation treats uniqueness as a database property and completeness as a dashboard hint, and the two
are not interchangeable for an audit trail.

---

## CHALLENGE 12 — Every categorical negative in E00 is scoped to a trimmed build, and the register does not say so

**CHALLENGE.** E00 twice describes the reference tree as "797-module" and uses that scale to license
tree-wide negatives — most consequentially EV-016's *"across the entire 797-module reference tree returns
no result"*, which is false (Challenge 4). The tree does not contain what that phrasing implies, and the
register's negatives are not scoped as the constitution's evidence discipline requires.

**TARGET.** EV-000, EV-016, EV-018, and E00's method for asserting absence.

**EVIDENCE.**

`VERIFIED FACT` — `ls -d */ | wc -l` in
`/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/` returns **791** module
directories, not 797.

`VERIFIED FACT` — `ls -d l10n_*` in the same directory returns **exactly two** entries: `l10n_th` and
`l10n_th_reports`. This is not a full-localization build. Any negative of the form "no localization
implements X" is unsupportable from this tree, because the localization layer is almost entirely absent
from it.

`VERIFIED FACT` — EV-016's tree-wide negative is falsified by a module inside the tree
(`account_accountant`, Challenge 4). EV-018's consequence is falsified by a file inside the module E00
declared verified (`account/models/res_currency.py`, Challenge 5). Two of E00's categorical negatives are
wrong; both were checkable within the declared sources.

`VERIFIED FACT` — the constitution provisions E00 itself quotes at EV-023 include *"No Evidence = No
Progress"* and principle 10 — module-level completion does not prove system readiness. A tree-wide negative
asserted without a stated search scope is the same defect principle 10 names, inverted.

`INFERENCE` — E00's `VERIFIED FACT` class is defined as "read directly from primary source this session;
citation given". A negative has no citation by construction. Classifying an unscoped negative as
`VERIFIED FACT` is a category error in the register's own taxonomy, and it is the mechanism by which
EV-016 and EV-018 entered the evidence base as facts.

**CLASSIFICATION: `CONFIRMED BY EVIDENCE`.**

**REQUIRED RESOLUTION.**
1. EV-000 corrected to 791 module directories and annotated that the localization layer comprises two Thai modules only.
2. Every categorical negative in E00 re-issued in the form *"searched `<paths>`, `<patterns>`, not found"*, or downgraded to `UNKNOWN — EVIDENCE REQUIRED`.
3. The evidence-class legend amended: a negative may not be classified `VERIFIED FACT` without an explicit search scope.
4. This unit re-ran EV-016's and EV-018's negatives with scope attached; the remaining tree-wide negatives in E00 have **not** been re-run by this unit and stand as `UNKNOWN` until they are.

---

# CHALLENGE UNIT POSITION

This unit did not author the evidence base and does not approve it. **Boss is sole final approver.**

The evidence base is substantially sound on the mechanics it read directly: EV-001, EV-002, EV-003,
EV-004, EV-005, EV-006, EV-007, EV-008, EV-011, EV-012, EV-013, EV-014, EV-017, EV-019, EV-022 and
EV-023 survived the checks this unit ran against them, and EV-010's core — that the digest covers a
subset of the posting and that no module in the tree extends it — is confirmed and hardened.

It fails on a specific and repeatable pattern: **where E00 asserts an absence, or reasons from a single
citation to a general semantic, it is unreliable.** Two categorical negatives are false (EV-016, EV-018).
One load-bearing semantic is cited to the wrong function and stated as a rule the source does not
implement (EV-009). One control conclusion is drawn from an access-control row that the model's own
`sudo()` path bypasses (EV-021). Three of these four were checkable inside sources E00 already declared
read. The Thai localization — the closest-fit primary source in the entire tree for a Thai SME
programme — is present in the build and cited nowhere.

One `VETO` is issued, on EV-009. It is not issued on the existence of soft re-dating, which is real and
correctly identified as important. It is issued because the stated rule is wrong in form, wrong in
scope, asymmetric between document types in a way E00 does not mention, and — decisively — active with
no lock date present at all, driven by the journal's numbering format. A semantic model built on EV-009
as written would place vendor bills on the wrong recognition date in the ordinary unlocked case. Section
F cannot proceed on EV-009 in its current form.

Wave A is **not** ready to move forward on this evidence base. Required before it is: the six amendments
in Part 1, the twelve resolutions in Part 2, and a re-run of every remaining categorical negative with
search scope attached.

All Thai statutory questions raised anywhere in this document are `HOLD / EVIDENCE REQUIRED` and are
routed to the Accounting-Tax track. No Thai law is asserted here. No reference code or schema is proposed
for copying; every transfer identified is a semantic or a control objective.

## Classification counts

**Part 1 — falsification verdicts (7 claims)**

| Verdict | Count | Claims |
|---|---|---|
| `CONFIRMED` | 2 | EV-002, EV-003 |
| `CONFIRMED WITH CAVEAT` | 3 | EV-010, EV-020, EV-021 |
| `CONTRADICTED` | 2 | EV-009, EV-016 |
| `UNKNOWN` | 0 | — |

`EV-016` is contradicted on its first half and confirmed on its second; `EV-021` is confirmed with caveat
on the exception shape and contradicted on its "append-only" conclusion. Both are counted once, at their
governing verdict.

**Part 2 — challenge classifications (12 challenges)**

| Classification | Count | Challenges |
|---|---|---|
| `CONFIRMED BY EVIDENCE` | 8 | 2, 3, 7, 8, 9, 10, 11, 12 |
| `CONTRADICTED` | 3 | 4, 5, 6 |
| `UNKNOWN` | 0 | — |
| `HOLD` | 1 | 8 (statutory component only; the evidence component is `CONFIRMED BY EVIDENCE`) |
| `VETO` | 1 | 1 |

Challenge 8 carries two classifications by construction — its code findings are evidenced, its statutory
consequences are held — and is counted in both rows.

**Cross-cutting attack categories exercised:** unsupported assumption (1, 12), missing evidence (5, 8, 11),
semantic conflation (8, 11, 3), UI-driven design bias (10 — E00 reasons from the readonly field list
rather than from the guard set), legacy architecture leakage (9 — E00 recommends both per-company codes
and database uniqueness, importing the reference storage shape without its trade-off), wrong
source-of-truth assumption (5), wrong financial recognition point (1), broken audit trail (3, 7),
SaaS/tenant boundary failure (EV-020 note, 4, 5), control weakness (6, 7, 11), reconciliation
impossibility (3 — hashing is gated on bank reconciliation completeness), generalisation from one module
or version to "the system" (12).

---

*End of C1 Adversarial Challenge Register.*
