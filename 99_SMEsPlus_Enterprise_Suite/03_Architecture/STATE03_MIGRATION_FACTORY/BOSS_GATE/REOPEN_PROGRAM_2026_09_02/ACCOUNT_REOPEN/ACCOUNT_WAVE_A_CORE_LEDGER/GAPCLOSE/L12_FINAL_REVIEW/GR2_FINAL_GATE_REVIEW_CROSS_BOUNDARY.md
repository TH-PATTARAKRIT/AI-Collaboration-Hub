# GR2 — FINAL INDEPENDENT GATE REVIEW 2 — CROSS-BOUNDARY

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GAPCLOSE-001` · Layer 2 / audit quarantine
Reviewer 2 — independent. Did not author the package; not involved in `CORR1`, `L12_FRESH_REVIEW`, or `GAPCLOSE` authorship.

**Assignment.** Not the four named blockers (Reviewer 1 owns those). The wider gate question:

> Can ANY financial fact cross a tenant or company boundary, anywhere in the accounting domain —
> beyond the FX rate case already found?

Plus: new `BALANCED BUT WRONG` cases, and over-claimed conclusions.

**Research only. Approves nothing. Boss is sole Final Approver.**

---

## 0. Search boundary for this whole document

Every negative below is bounded by this scope. Nothing outside it was searched.

| Dimension | Boundary |
|---|---|
| Tree searched | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/` |
| Read in depth | `addons/account/models/`, `addons/account/security/`, `addons/account_reports/models/account_report.py`, `addons/account_inter_company_rules/models/`, `addons/base/models/{res_company,res_currency,ir_sequence,ir_config_parameter}.py`, `addons/base/security/base_security.xml`, `odoo/models.py` |
| Swept by grep only | all `*.xml` under `addons/` for `ir.rule` `model_id` references; all `get_param(` call sites in `account*`; all `sudo()` call sites in `addons/account/models/` |
| **NOT searched** | any running instance or database · `account_accountant` · `account_asset` · `account_batch_payment` · `account_iso20022` · `account_online_synchronization` · localization (`l10n_*`) modules · the JavaScript/OWL layer · `ir.rule` records created at runtime or by data files not matching the grep pattern · upgrade scripts |
| Method | static reading only. **No code was executed. No behaviour was observed.** Every claim is a reading of source, or an inference from it, and is labelled as such. |

**Label key used throughout:** `VERIFIED FACT` (read directly in the cited source) · `REFERENCE BEHAVIOUR` (what the reference system does, as designed) · `INFERENCE` (derived, not directly read) · `RECOMMENDATION` · `UNKNOWN — EVIDENCE REQUIRED`.

**Negative classes:** `A. VERIFIED ABSENCE` (scope stated) · `B. NOT FOUND IN SEARCHED SCOPE` · `C. NOT YET SEARCHED` · `D. UNKNOWN` · `E. CONTRADICTED`. No `B`/`C`/`D` in this document is written as an `A`.

---

## 1. The framework-level fact that governs everything below

Before the object-by-object matrix, one mechanism explains most of it.

**`VERIFIED FACT`** — `odoo/models.py:4307-4317`, the default company-consistency domain:

```
if not companies:
    return [('company_id', '=', False)]
...
return [('company_id', 'in', to_company_ids(companies) + [False])]
```

and `odoo/models.py:188-204`, the `parent_of` variant used by most accounting models:

```
return [('company_id', 'in', [ ...ancestors... ] + [False])]
```

> **`VERIFIED FACT`.** In the reference framework, **"no company" means "every company"**. A record with a
> null company passes the company-consistency check for every company in the database, unconditionally.
> This is not a defect in one model. It is the framework's definition of company consistency.

**`VERIFIED FACT`** — `odoo/models.py:4353-4360`. If a model declares `_check_company_auto = True` and
`check_company=True` fields but has **neither** `company_id` **nor** `company_ids`, `_check_company`
writes a log warning and `continue`s. **The check is silently skipped.** (Reached by
`account.cash.rounding` — §2 row 10.)

**`VERIFIED FACT`** — `odoo/models.py:5529-5549` and `:5797`. `_where_calc` builds a query from a domain
and **does not apply record rules**; `_apply_ir_rules` is invoked from `_search` only. Any code path that
reaches the database through `_where_calc` has **no record-rule defence in depth** — its company scoping
is whatever domain that code chose to write. (Reached by the financial report engine — §2 row 21.)

**`VERIFIED FACT`** — `addons/base/models/res_company.py:117-118`. `root_id` is the first element of
`parent_path`, i.e. the topmost ancestor of any `res.company` hierarchy. It is not a special "branch"
marker. Wherever the accounting code tests `root_id`, the boundary it is enforcing is **the whole
company tree**, not the company.

`INFERENCE` (not separately tested): consequently, every "same company" guard written as a `root_id`
comparison permits any two distinct legal entities in one hierarchy.

---

## 2. PART 1 — COMPANY / TENANT BOUNDARY MATRIX

`Cross?` answers the assigned question: **can a financial fact (an amount, a measurement, a
classification, a period, a settlement) belonging to one company/tenant be created, altered, measured or
reported using another's data?**

| # | Object | Scoping rule | Record rule? | DB constraint? | Can a financial fact cross? | Citation |
|---|---|---|---|---|---|---|
| 1 | `account.account` | `company_ids` m2m; `_check_company_domain = check_companies_domain_parent_of` | **Yes** — `account_comp_rule`, `[('company_ids','parent_of',company_ids)]`, global | **No.** Python `@api.constrains` only | **YES, within a root tree.** An account assigned only to an ancestor company is postable-to by every descendant. Its **code** is stored per **root**, not per company | `account/security/account_security.xml:171-175`; `account/models/account_account.py:24-25,103-123,148,400`; `models.py:207-222` |
| 2 | `account.journal` | `_check_company_domain = check_company_domain_parent_of` | **Yes** — `journal_comp_rule`, `[('company_id','parent_of',company_ids)]`, global | **No** | **YES.** A journal owned by an ancestor company accepts entries from **every descendant company**, and the UI offers it: `suitable_journal_ids` is built from the same `parent_of` domain | `account_security.xml:165-169`; `account/models/account_journal.py:17-18`; `account/models/account_move.py:179-186, 831-834, 885-892` |
| 3 | `account.move` / `account.move.line` | `company_id in company_ids` (exact, not `parent_of`) | **Yes** — `account_move_comp_rule`, `account_move_line_comp_rule`, global | **No** company constraint tying `move.company_id` to `journal_id.company_id` | The **record** does not cross. Its **number** and its **derived accounting date** do — see row 4 | `account_security.xml:147-157`; `account/models/account_move.py:193-198, 2148-2151` |
| 4 | **Entry numbering path** (`sequence.mixin` + `_get_last_sequence_domain`) | **journal only** | **Bypassed** — both reference-move searches use `self.sudo()` | **No** | **YES — this is the strongest new crossing.** Raw WHERE is `journal_id = %(journal_id)s AND name != '/'` with **no company clause**; the two reference searches are `sudo()` and company-unscoped. In a shared journal (row 2) company A's next number, and via `_deduce_sequence_number_reset` → `_get_accounting_date` its **accounting period**, are derived from company B's entries | `account/models/account_move.py:3479-3503` (esp. `:3485, :3490, :3496, :3498`); `account/models/account_move.py:5655-5690`; `account/models/sequence_mixin.py:267-295` |
| 5 | `account.partial.reconcile` | `company_id` **computed from one side only** | **NONE FOUND** (class `B`, boundary §0) | **No** | **YES.** (a) `_check_amls_exigibility_for_reconciliation` tests `len(self.company_id.root_id) > 1` — **root, not company** — so a settlement between two distinct companies in one tree is explicitly permitted. (b) `create()` performs **no** company, account, or residual check, so a direct `create` is subject to no company guard at all | `account/models/account_move_line.py:2335-2339`; `account/models/account_partial_reconcile.py:54-58, 86-94, 139-144`; ACL `ir.model.access.csv:104-106` |
| 6 | `account.full.reconcile` | **no company field at all** | **NONE FOUND** (class `B`) | **No** | **YES, mechanically.** `create()` writes `account_move_line.full_reconcile_id` by **raw SQL `UPDATE`**, bypassing the ORM, its record rules and every company check. `account.partial.reconcile._update_matching_number` does the same for `matching_number` over the transitive reconciliation graph | `account/models/account_full_reconcile.py:6-9, 52-58`; `account_partial_reconcile.py:194-203` |
| 7 | `ir.config_parameter` | **no company dimension** — fields are `key`, `value` only | n/a | `unique(key)` only | **YES — confirms `SB-01`, and the register understates the class.** Beyond the numbering/date control, the same store carries `account.disable_partial_exchange_diff`, which **suppresses FX-difference journal entries for every tenant in the database** | `base/models/ir_config_parameter.py:29-41`; `account/models/sequence_mixin.py:157-161`; `account/models/account_move_line.py:2482` |
| 8 | `ir.sequence` | `[('code','=',c), ('company_id','in',[env.company.id, False])]`, `order='company_id'` — note `env.company`, **not** `root_id` | **NONE FOUND anywhere in the build** (class `B`, whole-tree `*.xml` grep) | `None` observed | **YES, structurally.** A null-company sequence is consumed by every company in the database. Consumed by payment numbering and cheque numbering | `base/models/ir_sequence.py:89, 146, 273-281`; `account/models/account_payment.py:378`; `account_check_printing/models/account_payment.py:149` |
| 9 | `res.currency.rate` | `company_id` nullable, defaults to `env.company.root_id`; resolver filters `(False, root_id)` | Yes — but the rule **explicitly permits** `company_id = False` | uniqueness only | **YES — the already-known case (`SB-05`, `FX-08`).** Re-verified independently; `G02`/`G03` evidence is sound as far as it goes | `base/models/res_currency.py:128-131, 365-371`; `base/security/base_security.xml:62-66` |
| 10 | `account.cash.rounding` | **no company field at all**, yet declares `_check_company_auto = True` and two `check_company=True` account fields | **NONE FOUND** (class `B`) | **No** | **YES.** Because the model has no company field, `_check_company` **silently skips it** (`models.py:4353-4360`). The record is database-global with no rule; its `rounding`, `strategy` and `rounding_method` are **measurement rules that change an invoice total**, editable by `account.group_account_invoice` in any tenant | `account/models/account_cash_rounding.py:15-41`; `models.py:4353-4360`; ACL `ir.model.access.csv:2-3` |
| 11 | `account.payment.term` | `company_id` **nullable**; `check_company_domain_parent_of` (adds `False`) | Yes — but permits `('company_id','=',False)` | **No** | **YES.** A null-company payment term is selectable by every company; it determines **due dates and the percentage split of an invoice across them** — a settlement/period fact. Editable by `account.group_account_manager` in any tenant. The inter-company generator copies a payment term **only when it is null-company** (row 20) | `account/models/account_payment_term.py:12-27`; `account_security.xml:243-247`; ACL `:111-113` |
| 12 | `account.account.tag` | **no company field**; keyed on `(name, applicability, country_id)` | **NONE FOUND** (class `B`) | `unique(name, applicability, country_id)` | Reporting classification only. Tags drive tax-report aggregation; move-line access is separately scoped. **`UNKNOWN — EVIDENCE REQUIRED`** whether the aggregation path is company-scoped in every engine | `account/models/account_account_tag.py:9-19`; ACL `:82-85` |
| 13 | `account.report`, `.line`, `.expression`, `.column` | **no company dimension at all** (`country_id` and `chart_template` only) | **NONE FOUND** (class `B`) | **No** | **YES, for reported measurement.** A report definition — including `integer_rounding`, `currency_translation`, and every line's computation formula — is a database-global object that `account.group_account_manager` in **any** tenant may create, write and unlink, and that **every** tenant's figures are then computed by | `account/models/account_report.py` (`account.report` field block, no `company_id`); ACL `account/security/ir.model.access.csv:136-140` |
| 14 | `account.report.external.value` | `company_id` | **Yes** — `report_external_value_comp_rule`, `[('company_id','in',company_ids)]` | — | **No** crossing found (class `B`). **This is the one report-side object that is properly scoped** — noted to be fair to the reference | `account_security.xml:332-335` |
| 15 | `account.journal.group` ("Ledger") | `company_id` **nullable**, help text: *"If none is provided, available for all companies"* | Yes — but permits `('company_id','=',False)` | `unique(company_id, name)` — NULLs distinct, so duplicates possible | **YES, for reporting scope.** A null-company ledger group appears in **every** company's report filters, and its `excluded_journal_ids` m2m carries **no company restriction** | `account/models/account_journal.py:17-31`; `account_security.xml:159-163` |
| 16 | `account.tax`, `account.tax.group`, `account.group`, `account.fiscal.position`, `account.reconcile.model(.line)` | `parent_of` | Yes, all `parent_of`, global | **No** | **YES, within a root tree.** An ancestor's tax rate, fiscal position, account group or reconcile model computes amounts and picks accounts for a descendant company's postings | `account_security.xml:177-210, 225-235` |
| 17 | `account.tax.repartition.line` | rule permits `('company_id','=',False)` | Yes — with the `False` disjunct | **No** | **`UNKNOWN — EVIDENCE REQUIRED`** whether a null-company repartition line is reachable in practice. If it is, it carries a **tax amount split and destination account** across every company | `account_security.xml:195-199` |
| 18 | `account.lock_exception` | `company_id`, taken from `vals` unchecked in `create` | **NONE FOUND** (class `B`) | index only | **`UNKNOWN — EVIDENCE REQUIRED`.** ACL denies `create` and `unlink` to every listed group including `account.group_account_manager` (`1,0,1,0`), so the reachable creation path was not traced. The **absence of a record rule on a lock-control object** is nonetheless a finding | `account/models/account_lock_exception.py:13-105, 189-215`; ACL `:18-19` |
| 19 | `res.partner` → `account.move.line.partner_id` | **none** | **Bypassed** — `self.sudo().env['account.move'].search([('partner_id','in',self.ids)])`, no company clause | **No** | **YES — reachable through ordinary UI with no accounting rights.** Re-parenting a shared contact rewrites `partner_id` on the journal items, and `commercial_partner_id` on the moves, of **every company in the database** that ever invoiced that partner, with `bypass_lock_check=BYPASS_LOCK_CHECK` explicitly defeating the hard lock date | `account/models/partner.py:17, 791-806`; `account/models/account_move.py:83, 2377-2379`; `account/models/account_move_line.py:1576-1580, 3365-3375` |
| 20 | `account_inter_company_rules` | `_find_company_from_partner` = `self.sudo().search([('partner_id','parent_of',pid)], limit=1)` — **whole database, no root restriction, no ordering stated** | Bypassed by `sudo()` | **No** | **YES, by design, and the boundary is the database.** Posting a customer invoice in company A creates — and, if `intercompany_document_state == 'posted'`, **posts** — a vendor bill in company B, carrying A's `price_unit`, `quantity`, `discount`, `currency_id`, `invoice_date`, `invoice_date_due`, `payment_reference`, and A's document number in `ref`/`invoice_origin`. It runs `with_user(company_b.intercompany_user_id)`, whose **default is `SUPERUSER_ID`** | `account_inter_company_rules/models/res_company.py:22-34`; `.../account_move.py:11-23, 71-101, 104-130` |
| 21 | Financial report engine (`account_reports`) | `('company_id','in', get_report_company_ids(options))` — **the only** company restriction | **NONE** — the query is built with `_where_calc`, which does not apply record rules; only `check_access('read')` (model-level) is called | **No** | **YES, structurally.** The report's company scope is a **request parameter**: `options['companies']`, and in the `forced_companies` branch it is taken **straight from caller-supplied `previous_options` and browsed with no validation against `self.env.companies`**. See §4 `OC-05` for what this does and does not prove | `account_reports/models/account_report.py:1276-1288, 2060-2101, 6401-6405`; `odoo/models.py:5529-5549, 5797` |
| 22 | `account.code.mapping` | identity = `account_id * 10000 + company_id` | n/a (`_auto = False`, `_table_query = '0'`) | n/a | Confirms `SB-02` / `COR-18` mechanically: the encoding aliases once a `res.company` id reaches 10,000. Read path materialises only `env.user.company_ids`; the **write** path decodes to a possibly different `(account, company)` pair | `account/models/account_code_mapping.py:4, 37-58` |
| 23 | `account.bank.statement` | `company_id` is `related='journal_id.company_id', store=True`; `journal.company_id` is `required=True` | Yes — `[('company_id','in', company_ids + [False])]` | — | The rule's `+ [False]` disjunct appears **unreachable** given the related+required chain. Class **`B` — NOT FOUND IN SEARCHED SCOPE**; not asserted as absence | `account/models/account_bank_statement.py:57-60`; `account/models/account_journal.py:132`; `account_security.xml:213-217` |

### 2.1 Direct answer to the assigned question

> **`VERIFIED FACT` (on the code) / `INFERENCE` (on the consequence).**
> **Yes. Financial facts can cross a company boundary at several places beyond the FX rate case, on at
> least three mechanisms that are independent of each other and of FX:**
>
> 1. **A period.** Rows 2 + 4 — a shared journal makes company A's accounting date a function of company B's entry names, through `sudo()`, company-unscoped reads.
> 2. **A classification.** Row 19 — a contact edit in any tenant rewrites the counterparty of posted journal items in every other company, bypassing the hard lock.
> 3. **A settlement.** Rows 5 + 6 — reconciliation's own guard is written on `root_id`, and the underlying records have no record rule and are written by raw SQL.
>
> Plus a measured amount (rows 10, 11, 16), a reported figure (rows 13, 21), and a whole generated document (row 20).

---

## 3. PART 2 — NEW `BALANCED BUT WRONG` CASES

None of these appears in the package's fifteen (`C12` Part 2). Each satisfies `Debit = Credit` and leaves the seven equations of `C12` intact.

| # | Case | How it arises | Controls it satisfies | Detectable? | Evidence |
|---|---|---|---|---|---|
| `NBW-16` | **Wrong period, sourced from another company** | A parent company's journal is offered to a descendant company's move (`suitable_journal_ids`, `parent_of`). The numbering scan reads the journal **without a company clause and under `sudo()`**; the resulting `highest_name` decides `sequence_number_reset`, which decides the derived accounting date | Balance ✓ · lock date ✓ (this path needs no lock, per the package's own `A2-03`) · numbering-uniqueness ✓ · hash ✓ | **No.** The stored move carries no trace of which company's entry supplied the reference name | `account_move.py:3485, 3490, 3496, 3498, 5671-5672`; `:885-892` |
| `NBW-17` | **Retroactive counterparty rewrite across every company** | `res.partner.write({'parent_id': ...})` → sudo, DB-wide search of `account.move` → `line_ids.partner_id` and `move.commercial_partner_id` rewritten with `bypass_lock_check` | Balance ✓ · all seven equations ✓ · hard lock **bypassed by design** · hashed moves **are** refused, so unhashed moves absorb it silently | **No,** for unhashed moves. It retroactively changes subledger attribution and ageing, and `P-04` (`Subledger ↔ Control Account`) is already `NOT PROVABLE` | `partner.py:791-806`; `account_move.py:2377-2379`; `account_move_line.py:1554-1563, 3365-3375` |
| `NBW-18` | **Cross-company settlement inside one root** | `_check_amls_exigibility_for_reconciliation` tests `len(self.company_id.root_id) > 1`. Two different legal entities under one root are accepted by it. `_compute_company_id` then stamps the partial with **one** side, and the exchange-difference and cash-basis entries are booked entirely in that one company | Balance ✓ · same-account ✓ · posted-only ✓ · `Reconciled + Residual = Original` ✓ **per company taken separately** | **Partially** — only by a query that compares the two lines' `company_id`, which no shipped control performs in the searched scope | `account_move_line.py:2335-2339`; `account_partial_reconcile.py:86-94, 239, 512-520` |
| `NBW-19` | **Settlement created with no guard at all** | `account.partial.reconcile.create()` runs **no** company, account, residual or state check — every guard lives in `_reconcile_plan`. The model has **no record rule**, and `account.group_account_invoice` holds full CRUD | Balance ✓ (the partial is not a posting) · every equation ✓ | **Partially** — `P-06` would detect an over-settlement but not a mis-companied one | `account_partial_reconcile.py:139-144`; ACL `:104-106`; **no `ir.rule` found**, class `B` |
| `NBW-20` | **Reconciliation state written by raw SQL** | `account.full.reconcile.create()` and `_update_matching_number` issue direct `UPDATE account_move_line` statements. `_all_reconciled_lines()` walks the transitive graph, which may include other companies' lines | Nothing applies — the ORM, its record rules and its company checks are all bypassed | **No.** No application-level trace | `account_full_reconcile.py:52-58`; `account_partial_reconcile.py:194-203` |
| `NBW-21` | **Wrong amount from a database-global measurement rule** | `account.cash.rounding` has no company field, so `_check_company` **silently skips** it; no record rule. Changing `rounding` / `rounding_method` / `strategy` changes the rounded total and the rounding line of every company's invoices that reference it. `account.payment.term` with a null company does the same to due dates and the split of an invoice across them | Balance ✓ · account-company check ✓ (the rounding line's account is separately checked) | **No.** Neither object is versioned; the invoice records the result, not the rule that produced it | `account_cash_rounding.py:15-41`; `models.py:4353-4360`; `account_payment_term.py:12-27` |
| `NBW-22` | **Wrong reported figure from a definition owned by another tenant** | `account.report` / `.line` / `.expression` carry **no company dimension** and **no record rule**; `account.group_account_manager` in any tenant may edit them. The engine reaches the database through `_where_calc`, which applies **no record rules**, so the company clause the engine writes itself is the only boundary | The ledger is untouched; every equation ✓ | **No,** from the ledger. Only by diffing report definitions against a known-good baseline, which the reference does not retain | `account_report.py` field block; ACL `:136-140`; `account_reports/.../account_report.py:2060-2101`; `models.py:5529-5549` |
| `NBW-23` | **Duplicate/derived event manufactured in another company under superuser** | `account_inter_company_rules`: posting a sale document in A creates a purchase document in B, selected by a **database-wide** `sudo` partner→company search with `limit=1`, gated only by a flag on **B**, executed as B's `intercompany_user_id` (**default `SUPERUSER_ID`**), and auto-posted when B is set to `posted` | Both documents balance ✓ · both are validly numbered ✓ · `auto_invoice_id` does link them | **Partially.** `auto_invoice_id` is a typed link — one of the "typed origin links" `BW-08` already credits. But the package's `BW-06` duplicate detector covers reference collisions, not this generation path, and the `limit=1` company selection has no stated ordering | `res_company.py:22-34`; `account_move.py:11-23, 71-101` |
| `NBW-24` | **FX difference recognition suppressed database-wide** | `account.disable_partial_exchange_diff` is read from `ir.config_parameter` — which has **no company dimension** — via `sudo().get_param`. When set, no exchange-difference entry is created on any partial, for any tenant | `Reconciled + Residual = Original` ✓ in transaction currency; the ledger stays balanced; no error is raised | **No.** Identical to `SB-01` in mechanism but it suppresses a **measurement**, not a numbering control | `account_move_line.py:2482`; `ir_config_parameter.py:29-41` |
| `NBW-25` | **A hash chain that spans companies** | `restrict_mode_hash_table` and `secure_sequence_number` are **per journal**. A journal shared by a parent and its descendants (row 2) produces one chain interleaving several companies' entries | The chain verifies ✓ | Verifiable only as a whole. **`INFERENCE`, not read as an explicit statement in the source** — it follows from journal-keyed hashing plus multi-company journals. Distinct from `SB-03`, which is about storage-row identity | `account_move.py:3832-3860`; `account_journal.py:17-18`; `account_move.py:885-892` |

**Ten new cases. Seven are undetectable by the equation set; two partially; one only in aggregate.**

Combined with `C12`'s fifteen, the register is not closed — which is itself the finding (§4 `OC-04`).

---

## 4. PART 3 — OVER-CLAIMED CONCLUSIONS FOUND

| # | Claim | Where | What the evidence actually supports | Class |
|---|---|---|---|---|
| `OC-01` | **"Journal — keyed to one company — tenant-safe in a shared database: **yes**"** and **"Entry — one company, via journal — **yes**"** | `16_L9_...SAAS_BOUNDARY_REGISTER.md` §2, rows 1–2, cited to `EV-006` | **`CONTRADICTED`.** `account.journal._check_company_domain = check_company_domain_parent_of`, and `account.move._compute_suitable_journal_ids` builds the selector from that same domain. A journal owned by an ancestor company is offered to, and accepted by, **every descendant company's** entries. The journal is keyed to a company **and all its descendants**. The "yes" verdicts on rows 1–2 do not hold, and rows 3 (Item) and the whole "journal is the control domain" model inherit the error | **`E`** |
| `OC-02` | **"Numbering/date control parameter — nothing; no company dimension at all"** presented as **one** structure in a 15-row register, and as **one** failure `SB-01` | `16_L9_...` §2 row 12 and §3 `SB-01`, cited to `COR-16` | The **mechanism** is verified and correct. The **scoping is too narrow**: `ir.config_parameter` is a database-wide store with no company dimension **for every key it holds**, and at least one other accounting key — `account.disable_partial_exchange_diff` — suppresses a **measurement** (FX difference recognition) for every tenant. `SB-01` should be a **class of failure**, not an instance. This understates severity rather than overstating it, but it is still a mis-scoped conclusion | **`E`** (as scoped) |
| `OC-03` | **"Company boundary is enforced for journals, entries and liquidity accounts"** | `CORR1/C10_..._GATE_REPORT.md` §5, answer 15–16 | "Enforced" is correct for **liquidity accounts** (`_check_company_consistency` refuses `asset_cash` with more than one company — though as a Python constraint, **not** a database constraint) and for **entries** at the record-rule level. It is **not** correct for **journals** (`OC-01`). The sentence also omits that several accounting objects — `account.partial.reconcile`, `account.full.reconcile`, `account.report` and its lines, `account.cash.rounding`, `account.account.tag`, `account.lock_exception`, `ir.sequence` — have **no record rule found at all** in the searched scope | **`E`** in part; **`B`** for the omission |
| `OC-04` | **"Everything except the four named items is ready for the Boss Final Research Gate"** and **"none [of the four] would change a decision in the transfer register"** | `C10` §6 ("What the hold is not") and §8 | These are **completeness claims about the unsearched remainder**, not findings. `§3` above adds ten balanced-but-wrong cases and `§2` adds at least three independent cross-boundary mechanisms, none of which is one of the four named items. Two of them (`NBW-16`, `NBW-17`) would change transfer-register decisions: the journal must not be a shared numbering domain across companies, and a shared master-data edit must never rewrite a posted fact. A `NOT SEARCHED` remainder cannot be declared ready | **`C` presented as `A`** |
| `OC-05` | **`forced_companies` — my own restraint on it** | this document, §2 row 21 | **`VERIFIED FACT`:** `previous_options['forced_companies']` is browsed with **no validation** against `self.env.companies`, and the report query is built with `_where_calc`, which applies **no record rules**. **`NOT PROVEN`:** that this reaches a company outside the user's own `company_ids` — line `:1288` reads `c.name`, which would apply the `res.company` employee rule `[('id','in', company_ids)]` (`base_security.xml:119-125`) and is expected to raise. What **is** established is narrower and still material: **the report's company scope is a caller-supplied request parameter with no defence in depth** — precisely the class `C09` named and `C12`'s readiness criterion 3 prohibits | **`B`** — recorded as `B`, not promoted |
| `OC-06` | **"Liquidity account — one company; sharing refused — tenant-safe: yes"** | `16_L9_...` §2 row 4, cited to `EV-019` | **`CONFIRMED WITH CAVEAT`.** The refusal is real (`_check_company_consistency`) but it is an **ORM-level `@api.constrains`**, not a database constraint, and it is triggered only on `company_ids` and `account_type`. Any path that writes the relation table without the ORM — of which this package has now found two in the reconciliation code (`NBW-20`) — is not covered. "yes" should read "yes, at ORM level only" | **`A` with stated scope** |
| `OC-07` | **`G02` §2.4 rate precedence** | `GAPCLOSE/G02_..._SB05_TARGETED_CLOSURE.md` | **Not an over-claim — noted for the opposite reason.** `G02` correctly labels the `NULLS LAST` precedence an `INFERENCE` and does not promote it. That inference is nonetheless **load-bearing** for the severity of `SB-05`, and it rests on PostgreSQL default ordering that this reviewer also did not execute. It remains `INFERENCE` on both sides | `B` — correctly scoped by the author |
| `OC-08` | **`C12` "A ledger can satisfy all seven equations and be wrong in thirteen identified ways"** | `C12` Part 3 | **`CONFIRMED WITH CAVEAT`.** The wording "identified" is properly scoped and this reviewer does not fault it. The caution is for the reader, not the author: the number is a **floor**, and `C10`'s executive summary — *"fifteen distinct 'balanced but wrong' cases were identified"* — reads at a gate as an enumeration of a closed set. Ten more were found in one independent round | `B` |

### 4.1 Governance observation

`C10` §7.1 records that over-scoped negatives are this programme's recurring defect, and that three were
authored by `CORR1` after it wrote the rule against them. This round adds a second pattern, distinct
from the first:

> **`INFERENCE`.** The package's negatives are now well policed. Its **positives** are not. `OC-01`,
> `OC-03` and `OC-06` are all **affirmative** claims — "keyed to one company", "tenant-safe: yes",
> "enforced" — and all three are wrong or over-strong. `C10` §7.3 proposes weighting positives as the
> *stronger* class at gates. On this evidence that proposal is unsafe as stated: an unverified
> **positive** is exactly as dangerous as an over-scoped negative, and is currently subject to no
> equivalent audit step.
>
> `RECOMMENDATION:` extend `DR-NC-05` to cover affirmative safety claims — every "yes / enforced /
> safe / keyed to" cell in a register must carry its own citation and enforcement level (database
> constraint / record rule / ORM constraint / none). Boss decision.

---

## 5. PART 4 — `REVIEWER 2 POSITION`

### 5.1 Position

**`CONFIRMED`** — the assigned question is answered, and the answer is adverse.

> **Financial facts can cross a company boundary in the accounting domain at several places beyond the
> FX rate case.** At least three mechanisms are independent of FX and of each other: a **period**
> (`NBW-16`), a **classification on a posted fact** (`NBW-17`), and a **settlement** (`NBW-18`/`NBW-19`).
> A measured amount, a reported figure and a whole generated document also cross.

**`CONFIRMED`** — the outermost enforced boundary in the accounting domain is not the company and not
consistently the company group. In the searched scope it is, variously: the **company** (moves, move
lines), the **root company tree** (accounts, journals, taxes, fiscal positions, reconciliation guards,
account codes, currency rates), and the **database** (`ir.config_parameter`, `ir.sequence`,
`account.cash.rounding`, `account.account.tag`, `account.report` and its lines, the inter-company
partner→company resolution). This is broader than `L9` §2 records.

**`CONTRADICTED`** — `L9` §2 rows 1–2 ("Journal / Entry — tenant-safe: yes") and `C10` §5 answer 15–16
("enforced for journals").

**`CONTRADICTED`** — `C10` §6/§8 "everything except the four named items is ready".

**`HOLD`** — every Thai statutory question touched by these findings (statutory numbering continuity,
statutory retention of the counterparty on a posted document, statutory FX recognition). **No Thai law
is asserted here from memory.** Routed to **`WAVE-D TAX` / Accounting-Tax track**, `EVIDENCE REQUIRED`.

**`UNKNOWN — EVIDENCE REQUIRED`** — rows 12, 17, 18 and 23 of the matrix; the reachability of
`forced_companies` beyond `user.company_ids` (`OC-05`); and everything in the §0 not-searched list.

### 5.2 Gate recommendation

> # `RECOMMEND HOLD`

**This is a recommendation only. Boss is the sole Final Approver. Nothing here is an approval, a freeze, a gate movement, or an implementation authorisation.**

**Reasons.**

1. **The gate's own decision rule is triggered, and by more than the FX case.** `C10` §6 holds the gate
   because two of four open items concern cross-tenant integrity, which this programme's constitution
   designates a `Tolerance = 0` candidate. This review finds **three further, independent cross-boundary
   mechanisms**, none of them among the four. The reason to hold is stronger now, not weaker.

2. **At least one crossing is reachable with no accounting rights at all.** `NBW-17` needs only write
   access to a contact. It rewrites a posted journal item's counterparty in **every** company in the
   database and **explicitly bypasses the hard lock date**. That is the one control the package
   identifies as unconditionally immutable.

3. **The affirmative claims in the register are not reliable yet.** `OC-01` is a direct contradiction of
   a "tenant-safe: yes" cell that other levels depend on. Until affirmative safety claims are audited
   the way negatives now are, a gate cannot rely on the register's "yes" column.

4. **The completeness claim is not supportable.** One independent round, static reading only, no
   execution, produced ten new balanced-but-wrong cases and three new crossings. `C10`'s "everything
   except the four named items is ready" is a claim about an unsearched remainder.

**Why `HOLD` and not `FAIL`.** Nothing found invalidates the semantic model. Every finding **sharpens**
it in the direction the package already chose: storage-level invariants, event identity, provenance,
tamper-evidence on business identity, and no invariant expressible as a request parameter. `C12`'s
three-part readiness criterion would catch or contain most of what is above. The research is sound and
its method is working — this round is evidence that the method works, not that it failed.

**Why not `RECOMMEND CONDITIONAL PASS`.** The same reason `C10` gave, now with more instances: that
recommendation would carry unverified cross-tenant integrity questions into design.

**Why not `RECOMMEND PASS`.** Not available on this evidence.

### 5.3 What would close this, as a `RECOMMENDATION` for Boss

| # | Item | Nature |
|---|---|---|
| `R2-01` | Re-derive `L9` §2 with an **enforcement-level column** — database constraint / record rule / ORM constraint / none — and re-verify every "yes" | register correction |
| `R2-02` | Decide the SMEsPlus rule for the journal: **one journal belongs to exactly one company**, and the numbering domain is `(company, journal, period)` — never journal alone | `EXTEND` candidate |
| `R2-03` | Decide that **no shared master-data edit may ever rewrite a posted fact**, and that no code path may carry a lock-bypass token | `REJECT` candidate |
| `R2-04` | Decide that a **settlement links facts of exactly one company**, enforced by database constraint, not by an application guard on the root | `EXTEND` candidate |
| `R2-05` | Decide that every **measurement rule and report definition carries a tenant dimension** — extends `TI-01` from configuration to measurement and reporting | `EXTEND` candidate |
| `R2-06` | Extend `DR-NC-05` to affirmative safety claims (§4.1) | governance |

`R2-01`…`R2-06` are proposed for Boss decision and are **not adopted by this session**.

---

## CHECKPOINT — GR2

| Item | Record |
|---|---|
| Scope completed | 23-row company/tenant boundary matrix; 10 new balanced-but-wrong cases; 8 over-claim assessments; 1 governance observation |
| Verified findings | `_where_calc` applies no record rules · numbering path is company-unscoped and `sudo()` · reconciliation guard is written on `root_id` · partner re-parent rewrites posted items DB-wide with the lock bypassed · `account.report`, `account.cash.rounding`, `account.account.tag`, `account.full.reconcile` have no company dimension and no record rule · `intercompany_user_id` defaults to `SUPERUSER_ID` |
| Contradictions raised | `OC-01`, `OC-02`, `OC-03`, `OC-04` |
| Unknowns | matrix rows 12, 17, 18, 23; `forced_companies` reachability; the entire §0 not-searched list |
| Method limits | static reading only; **no code executed, no instance observed** |
| Recommendation | `RECOMMEND HOLD` |

`CHECKPOINT GR2 RECORDED.` **Not Boss approval. Approves nothing.**
