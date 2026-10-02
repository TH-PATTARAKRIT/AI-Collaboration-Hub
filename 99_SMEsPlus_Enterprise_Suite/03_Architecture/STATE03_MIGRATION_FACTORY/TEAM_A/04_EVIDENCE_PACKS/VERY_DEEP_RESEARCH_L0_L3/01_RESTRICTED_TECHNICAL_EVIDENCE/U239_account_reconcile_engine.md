# U239 — account.partial.reconcile / account.full.reconcile Reconciliation Engine — Restricted Technical Evidence

## RESTRICTED TECHNICAL EVIDENCE

RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION

Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

**Unit:** U239 — reconciliation engine (partial reconcile, full reconcile, residual amounts, matching number, exchange-difference moves, unreconcile, lock-date interplay)
**Module key:** account_reconcile_engine
**Release:** odoo-19.0.post20260921 (Community tree only)
**Release root:** `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/` (addons under `odoo/addons`, ORM core under `odoo/orm`)
**Research date:** 2026-10-03
**Evidence method:** static source reading and repository-wide text search only. No Odoo instance was started. No database was consulted: the live database was not inspected, so every foreign-key action, stored value and runtime ordering statement below is derived from source and flagged RT where it depends on a live system.
**Pointer convention:** every pointer is a path relative to `odoo/addons` (or starting `odoo/orm`) followed by a line range, written out in full each time. Each pointer carries exactly one range.
**Neutral companion:** `02_NEUTRAL_KNOWLEDGE/U239_account_reconcile_engine_NEUTRAL.md` (26 claim rows, ids U239-C01 to U239-C26)
**Handoff packet:** `04_HANDOFF_PACKETS/U239_handoff_packet.json`

### Source integrity (files read in full or in the cited ranges)

| File (relative to addons) | Lines | SHA-256 |
|---|---|---|
| account/models/account_partial_reconcile.py | 732 | 49dcf877bec40f72e4297ee8dbffe04323ada395a9c09752c8ee3ff1d9f97bcb |
| account/models/account_full_reconcile.py | 60 | 2a39c9641551469f9413d01a6f65ba95050d0ef81bbb8f2c3e78539236a8951d |
| account/models/account_move_line.py | 3833 | 75e3077b3a49786a3aa5a64d353de4233cd32e92fe6b7a0e47bd7f9a95693012 |
| account/models/account_move.py | 7489 | bc88290beed3909d3c3a14c89e2dbadee5239c0969b076da3537434750d456fb |
| account/models/company.py | 1157 | 52244ff1df15595af700fc84e98a2ab4f51035e0769a1456c11e6a1539091a8a |
| account/models/account_account.py | 1658 | 75ad6073152c2419558703e5760eb2b93db33ab3cb758dfee258418acc921c11 |
| l10n_th/models/template_th.py | 43 | 6560e295c18839dbf06483bd1b8252b3611e8640683dbd25a46a497d8a2887a2 |
| account/security/ir.model.access.csv | 146 | 4d2520a2a7f76d370714bc7a2873614f727c85358428acb03932a75f3d6c2d47 |

---

## 0. Scope boundary and related units

In scope: the reconciliation engine implemented on journal items (`account.move.line`) plus the two engine models `account.partial.reconcile` and `account.full.reconcile`, the matching number, the exchange-difference entry, unreconcile paths, lock-date touch points inside the engine, and the Thai defaults that feed it.

Pointer-only (not analysed here; owned by other units): U101 (cash-basis tax entries), U103 and U123 (tax exigibility, year-end foreign-exchange revaluation), U114, U124 and U220 (lock dates), U204 and U12 (payment state; CAP-U12-03), U238 (account.move model), U136 (reconcile model), U126 (bank reconciliation), U79 (move lifecycle). For U136, U126 and U79 this document asserts nothing beyond the carried ids.

Localization scope is Thailand only. Country-pack hits found by repository-wide search are listed as "noted, not analysed" in section 9.

## 1. Data model

### 1.1 account.partial.reconcile

Declared at `account/models/account_partial_reconcile.py:10-12`.

| Field | Type and behaviour | Pointer |
|---|---|---|
| debit_move_id, credit_move_id | Many2one to journal item, required, indexed | `account/models/account_partial_reconcile.py:15-20` |
| full_reconcile_id | Many2one to the full-reconcile record, no copy, btree_not_null index | `account/models/account_partial_reconcile.py:21-23` |
| exchange_move_id | Many2one to account.move, btree_not_null index | `account/models/account_partial_reconcile.py:24-24` |
| draft_caba_move_vals | Json; source comment says it is used at invoice posting to decide whether the partial can be kept | `account/models/account_partial_reconcile.py:26-28` |
| company_currency_id | related, not stored | `account/models/account_partial_reconcile.py:31-35` |
| debit_currency_id, credit_currency_id | stored related, precomputed | `account/models/account_partial_reconcile.py:36-45` |
| amount | Monetary in company currency, always positive | `account/models/account_partial_reconcile.py:48-50` |
| debit_amount_currency | Monetary in debit line currency | `account/models/account_partial_reconcile.py:51-53` |
| credit_amount_currency | Monetary in credit line currency | `account/models/account_partial_reconcile.py:54-56` |
| company_id | stored, precomputed, writable compute; takes the debit line's company when its move is an invoice, else the credit line's | `account/models/account_partial_reconcile.py:59-63` and compute at `account/models/account_partial_reconcile.py:92-99` |
| max_date | stored, precomputed; comment says it serves aged reports | `account/models/account_partial_reconcile.py:64-68` and compute at `account/models/account_partial_reconcile.py:84-90` |
| constraint on currencies | ValidationError when either currency is missing | `account/models/account_partial_reconcile.py:74-78` |

Foreign-key actions (INFERENCE from ORM defaults, live database not inspected, RT): the ORM default for a required Many2one without an explicit ondelete is restrict and for a non-required one is set null (`odoo/orm/fields_relational.py:274-282`). Therefore the two journal-item links on a partial are restrict, while the partial's `full_reconcile_id`, its `exchange_move_id`, and the journal item's `full_reconcile_id` are set null. The full-reconcile unlink comment about zombies corroborates the set-null behaviour (`account/models/account_full_reconcile.py:48-54`).

### 1.2 account.full.reconcile

Model declared at `account/models/account_full_reconcile.py:5-7`. The only fields are `partial_reconcile_ids` and `reconciled_line_ids` (`account/models/account_full_reconcile.py:9-10`). There is no name, no sequence, no exchange-move link, no date and no company field on this model in this tree.

- `create` (`account/models/account_full_reconcile.py:12-45`): accepts only link or set commands for the two relations, otherwise raises ValueError (`account/models/account_full_reconcile.py:14-21`); pops both keys without a default (`account/models/account_full_reconcile.py:22-23`); disables tracking (`account/models/account_full_reconcile.py:24-24`); first raw UPDATE sets the journal items' full-reconcile link (`account/models/account_full_reconcile.py:26-31`) with cache invalidation (`account/models/account_full_reconcile.py:32-33`); second raw UPDATE sets the partials' link (`account/models/account_full_reconcile.py:35-40`) with invalidation (`account/models/account_full_reconcile.py:41-42`); finally calls the matching-number updater (`account/models/account_full_reconcile.py:44-44`).
- `unlink` (`account/models/account_full_reconcile.py:47-60`): reconciled lines are captured, super is called, survivors are re-read and matching numbers refreshed (`account/models/account_full_reconcile.py:55-59`).

### 1.3 Journal-item mirror fields

| Field group | Pointer |
|---|---|
| amount_residual, amount_residual_currency, reconciled (stored computes) | `account/models/account_move_line.py:246-258` |
| full_reconcile_id (label "Matching", no copy, btree_not_null, readonly) | `account/models/account_move_line.py:259-265` |
| matched_debit_ids (partials where this line is the credit side, inverse on credit_move_id) | `account/models/account_move_line.py:266-271` |
| matched_credit_ids (partials where this line is the debit side, inverse on debit_move_id) | `account/models/account_move_line.py:272-277` |
| reconciled_lines_ids (compute with inverse) | `account/models/account_move_line.py:278-281` |
| reconciled lines excluding exchange variant | `account/models/account_move_line.py:283-286` |
| helper fields used by the client | `account/models/account_move_line.py:289-298` |
| exchange_move_ids | `account/models/account_move_line.py:299-302` |
| matching_number | `account/models/account_move_line.py:304-310` |
| is_account_reconcile (related) | `account/models/account_move_line.py:311-314` |

Naming oddity worth carrying forward: `matched_debit_ids` holds partials in which the line sits on the credit side; `matched_credit_ids` the reverse.

### 1.4 Links on account.move

- `exchange_diff_partial_ids` One2many, inverse `exchange_move_id`: `account/models/account_move.py:200-204`.
- Cash-basis links `tax_cash_basis_rec_id`, `tax_cash_basis_origin_move_id`, `tax_cash_basis_created_move_ids`: `account/models/account_move.py:270-274`, `account/models/account_move.py:275-281`, `account/models/account_move.py:282-287`.
- `always_tax_exigible` field `account/models/account_move.py:291-291`, compute (true when not an invoice and no cash-basis values) `account/models/account_move.py:1012-1020`.

### 1.5 Access rows (account/security/ir.model.access.csv)

| Line | Row id | Group | Rights (read, write, create, unlink) |
|---|---|---|---|
| 97 | access_account_partial_reconcile_readonly | readonly accountant group | 1,0,0,0 |
| 98 | access_account_partial_reconcile_group_invoice | invoicing group | 1,1,1,1 |
| 99 | access_account_partial_reconcile | account user group | 1,1,1,1 |
| 100 | access_account_full_reconcile_group_readonly | readonly accountant group | 1,0,0,0 |
| 101 | access_account_full_reconcile_group_invoice | invoicing group | 1,1,1,1 |
| 102 | access_account_full_reconcile | account user group | 1,1,1,1 |

Pointers: `account/security/ir.model.access.csv:97-102`. Extra partial-reconcile rows outside account: `sale/security/ir.model.access.csv:10-10` (salesman, read only), `sale_stock/security/ir.model.access.csv:12-12` (stock manager, full rights), `purchase/security/ir.model.access.csv:29-29` (purchase user, read only). No record rules for these two models were found in `account/security/account_security.xml` (text search).

## 2. matching_number

Convention (OBSERVATION): a fully reconciled group carries the decimal string of its full-reconcile id; a partially reconciled group carries the letter P followed by the smallest partial id in the connected graph. An imported marker starts with I.

- Field: Char "Matching #", no copy, btree index; the source comment mentions the import prefix: `account/models/account_move_line.py:304-310`.
- Updater: `account/models/account_partial_reconcile.py:193-238`. It expands to all lines of each group (`account/models/account_partial_reconcile.py:195-195`), merges graphs keeping the smaller number (`account/models/account_partial_reconcile.py:203-224`), flushes the full-reconcile link (`account/models/account_partial_reconcile.py:226-226`), writes through a raw SQL statement with a case on whether the line has a full-reconcile link (`account/models/account_partial_reconcile.py:227-235`), invalidates the cache (`account/models/account_partial_reconcile.py:237-237`) and clears the number, through the ORM, on lines that left every graph (`account/models/account_partial_reconcile.py:238-238`).
- Constraint: regex accepts optional P with digits, or I followed by text (`account/models/account_move_line.py:1597-1597`). The method `_constrains_matching_number` (`account/models/account_move_line.py:1593-1610`) raises a plain Exception, not ValidationError, for bad format (`account/models/account_move_line.py:1598-1598`), P without partials (`account/models/account_move_line.py:1602-1602`), P with a full reconcile (`account/models/account_move_line.py:1604-1604`), decimal without a full reconcile (`account/models/account_move_line.py:1606-1606`), decimal differing from the full id (`account/models/account_move_line.py:1608-1608`), and partials without a number (`account/models/account_move_line.py:1610-1610`). Only the "temporary number in a real matching" case raises ValidationError (`account/models/account_move_line.py:1599-1600`).
- Input sanitising: a truthy matching number that does not start with I is prefixed with I unless context `skip_matching_number_check` is set: `account/models/account_move_line.py:1693-1712`, specifically `account/models/account_move_line.py:1705-1710`.
- INFERENCE: the engine writes the number by raw SQL, so the Python constraint is not exercised on the engine path (RT: not run).
- Import markers are consumed by `_reconcile_marked` (`account/models/account_move_line.py:3157-3178`): it enables `reconcile` on the account when needed (`account/models/account_move_line.py:3175-3177`) and reconciles under `no_exchange_difference` and `no_cash_basis` (`account/models/account_move_line.py:3178-3178`). It is called from posting at `account/models/account_move.py:5776-5776`.
- Group helpers: `account/models/account_move_line.py:3403-3433`. `_reconciled_lines` (`account/models/account_move_line.py:3403-3408`) has no caller found; `_reconciled_by_number` reads through sudo `_read_group` (`account/models/account_move_line.py:3410-3419`); `_filter_reconciled_by_number` ignores I numbers (`account/models/account_move_line.py:3421-3429`); `_all_reconciled_lines` (`account/models/account_move_line.py:3431-3433`). The view action is at `account/models/account_move_line.py:3736-3740`.

## 3. Pipeline

### 3.1 Business purpose

Match debit-side and credit-side journal items on the same account and, where residuals remain, record how much of each side was consumed, so that open-item balances (invoices, payments, statement lines) fall to zero and their state follows.

### 3.2 Outline

1. `reconcile()` (`account/models/account_move_line.py:3142-3144`) calls the plan method with the recordset as the only group and returns None.
2. `_reconcile_plan` (`account/models/account_move_line.py:2796-2819`; docstring `account/models/account_move_line.py:2798-2812` describes a plan as a list of recordsets or nested sub-plans with sub-groups reconciled first) optimises the plan (`account/models/account_move_line.py:2815-2815`) under the balance-check and dynamic-line-sync context managers (`account/models/account_move_line.py:2817-2818`) and delegates to the sync worker (`account/models/account_move_line.py:2819-2819`).
3. `_optimize_reconciliation_plan` (`account/models/account_move_line.py:2688-2781`): sorts lines by maturity date or date, currency, currency amount and balance, or only the first two keys under context `reduced_line_sorting` (`account/models/account_move_line.py:2712-2742`, `account/models/account_move_line.py:2713-2726`); per-currency sub-nodes only when more than one currency is present (`account/models/account_move_line.py:2733-2742`); children and leaves (`account/models/account_move_line.py:2744-2755`, `account/models/account_move_line.py:2757-2766`); entry validation per top-level node (`account/models/account_move_line.py:2777-2777`); returns plan and all lines (`account/models/account_move_line.py:2781-2781`).
4. `_reconcile_plan_with_sync` (`account/models/account_move_line.py:2821-2989`) — steps in order:
   - prefetch (`account/models/account_move_line.py:2826-2828`);
   - pre-hook capturing invoices not yet paid or in payment (`account/models/account_move_line.py:2783-2788`);
   - residual value map (`account/models/account_move_line.py:2837-2845`);
   - per plan, `_prepare_reconciliation_plan` (`account/models/account_move_line.py:2611-2649`) with contexts forwarded (`account/models/account_move_line.py:2852-2857`);
   - exchange value list appended only when the exchange values have line values (`account/models/account_move_line.py:2861-2862`);
   - one bulk create of partials (`account/models/account_move_line.py:2866-2866`);
   - `add_caba_vals` hook (`account/models/account_move_line.py:2867-2868`);
   - slicing of partials per plan (`account/models/account_move_line.py:2870-2873`);
   - exchange-move creation (`account/models/account_move_line.py:2876-2876`) and linking (`account/models/account_move_line.py:2880-2891`);
   - cash-basis block (`account/models/account_move_line.py:2894-2902`);
   - full-reconcile batch detection (`account/models/account_move_line.py:2907-2941`);
   - prefetch (`account/models/account_move_line.py:2946-2949`);
   - full-reconcile creation with link commands (`account/models/account_move_line.py:2951-2966`; comment `account/models/account_move_line.py:2952-2953`);
   - an unreachable cash-basis rounding block (`account/models/account_move_line.py:2968-2987`, see section 12);
   - post-hook (`account/models/account_move_line.py:2989-2989`; body `account/models/account_move_line.py:2790-2794`) which calls the invoice-paid hook on invoices that became paid or in payment.

### 3.3 Validation at entry

`_check_amls_exigibility_for_reconciliation` (`account/models/account_move_line.py:2651-2686`) gathers P numbers of non-reconciled lines (`account/models/account_move_line.py:2657-2660`) and drops reconciled lines carrying them (`account/models/account_move_line.py:2661-2661`). It then raises UserError for: already reconciled line (`account/models/account_move_line.py:2666-2667`), a cancelled parent entry (`account/models/account_move_line.py:2668-2669`), more than one account (`account/models/account_move_line.py:2670-2675`), more than one company root (`account/models/account_move_line.py:2676-2680`), and a non-reconcilable account unless it is of cash or credit-card type (`account/models/account_move_line.py:2681-2686`). Off-balance lines cannot be reconciled: `account/models/account_move_line.py:1496-1505`.

### 3.4 Planning and pairing

`_prepare_reconciliation_plan` (`account/models/account_move_line.py:2611-2649`) handles children first (`account/models/account_move_line.py:2640-2646`), then the parent over lines not yet fully reconciled; with more than one partner it sorts by partner id (`account/models/account_move_line.py:2627-2628`). `_prepare_reconciliation_amls` (`account/models/account_move_line.py:2544-2609`) puts positive balance or positive currency amount on the debit side (`account/models/account_move_line.py:2557-2562`), negative on the credit side (`account/models/account_move_line.py:2563-2568`), pairs them through the single-partial method (`account/models/account_move_line.py:2595-2595`), advances a side whose values became None (`account/models/account_move_line.py:2602-2607`) and returns results with the ids of fully reconciled lines (`account/models/account_move_line.py:2609-2609`).

### 3.5 Single partial

`_prepare_reconciliation_single_partial` (`account/models/account_move_line.py:2235-2542`); returned keys are listed in its docstring (`account/models/account_move_line.py:2237-2249`).

- Reconciliation currency: the debit line's currency if foreign and present in both sides' available dicts, else the credit line's under the same test, else the company currency (`account/models/account_move_line.py:2281-2290`).
- A side without reconciliation values means skip (`account/models/account_move_line.py:2295-2304`); amounts (`account/models/account_move_line.py:2306-2307`); exchange line mode (`account/models/account_move_line.py:2315-2321`); comparison flags (`account/models/account_move_line.py:2324-2327`); rounding range helper (`account/models/account_move_line.py:2329-2341`).
- Company-currency branch `account/models/account_move_line.py:2344-2365`; foreign branch `account/models/account_move_line.py:2367-2438`. In the foreign branch the rounding-tolerance test (`account/models/account_move_line.py:2418-2426`) means that when each partial amount lies inside the other's rounding range, the partial becomes the smaller of the two remaining company residuals and no exchange difference arises.
- Residual bookkeeping `account/models/account_move_line.py:2514-2541`; partial values carry amount, both currency amounts and both line ids (`account/models/account_move_line.py:2519-2525`).

### 3.6 Rate selection and residual helper

`_prepare_move_line_residual_amounts` (`account/models/account_move_line.py:2157-2233`):

- payment detection: origin payment or statement line (`account/models/account_move_line.py:2171-2172`);
- Odoo rate: the forced rate from context `forced_rate_from_register_payment` wins; if the other line is a payment and this one is not, the other line's accounting rate is used; invoices use the invoice date, otherwise the line date (`account/models/account_move_line.py:2174-2183`);
- accounting rate is the absolute ratio of currency amount to balance (`account/models/account_move_line.py:2185-2189`);
- the foreign-rate branch applies only when the line is in company currency, on a receivable or payable account, with a non-zero residual and the counterpart in a foreign currency (`account/models/account_move_line.py:2215-2225`); the alternative same-foreign-currency branch is `account/models/account_move_line.py:2226-2232`.

### 3.7 Full-reconcile detection and lifecycle

A line counts as reconciled when its reconciled flag is true; false when it has no partials (`account/models/account_move_line.py:2911-2913`); with multiple currencies the company residual must be zero, otherwise the currency residual (`account/models/account_move_line.py:2907-2941`). A batch is the plan lines plus lines that share a non-I matching number (`account/models/account_move_line.py:2921-2921`, `account/models/account_move_line.py:2927-2927`); the batch dict carries only the lines and a fully-reconciled flag (`account/models/account_move_line.py:2935-2938`). Creation: `account/models/account_move_line.py:2951-2966`.

Residual compute (`account/models/account_move_line.py:813-880`): lines need residuals when the account is reconcilable or of cash or credit-card type (`account/models/account_move_line.py:820-820`); a raw SQL aggregate over partials grouped by side with currency decimal rounding (`account/models/account_move_line.py:831-851`); other lines get zero and not reconciled (`account/models/account_move_line.py:860-863`); residual equals the rounded balance minus debit partial amounts plus credit partial amounts (`account/models/account_move_line.py:875-875`), currency variant (`account/models/account_move_line.py:876-876`), reconciled when both are zero (`account/models/account_move_line.py:877-880`).

## 4. Exchange-difference engine

OBSERVATION: in this tree the exchange-difference entry is built per partial, not when a group becomes fully reconciled.

- Builder trigger inside the single partial: `account/models/account_move_line.py:2440-2510`. Company-currency recon branch uses currency-residual amounts (`account/models/account_move_line.py:2445-2457`); foreign branch uses company residual amounts (`account/models/account_move_line.py:2459-2500`): the fully matched side fixes the remaining company amount (`account/models/account_move_line.py:2460-2468`, `account/models/account_move_line.py:2481-2489`), and the other side contributes only when its exchange amount is positive for debit or negative for credit (`account/models/account_move_line.py:2469-2479`, `account/models/account_move_line.py:2490-2500`). Exchange date is the later of the two line dates (`account/models/account_move_line.py:2505-2508`); posting is requested only when both parent entries are posted (`account/models/account_move_line.py:2510-2510`).
- Suppression: contexts `no_exchange_difference` and `no_exchange_difference_no_recursive` (`account/models/account_move_line.py:2442-2442`).
- Company configuration: exchange journal (`account/models/company.py:133-133`, general type), income account (`account/models/company.py:134-138`, income group), expense account (`account/models/company.py:139-143`, expense types). Getter for the account: expense account when the amount is positive, else income (`account/models/account_move_line.py:2991-2997`).
- Builder `_prepare_exchange_difference_move_vals` (`account/models/account_move_line.py:2999-3085`): company from the invoice move if any, else the move, else a keyword (`account/models/account_move_line.py:3011-3014`); returns None without a company (`account/models/account_move_line.py:3015-3016`) — INFERENCE: unreachable from the single in-engine call site; `date.min` when no journal (`account/models/account_move_line.py:3019-3019`); move date is the maximum of the journal accounting date and each line date (`account/models/account_move_line.py:3021-3032`); entry type, name slash, always tax exigible (`account/models/account_move_line.py:3027-3027`); zero amounts skipped (`account/models/account_move_line.py:3040-3047`); the line values mirror the original line, including its full-reconcile link (`account/models/account_move_line.py:3060-3060`) and a set command on the reconciled-lines relation (`account/models/account_move_line.py:3065-3065`), plus a counter line on the exchange account (`account/models/account_move_line.py:3067-3076`); analytic keyword (`account/models/account_move_line.py:3079-3080`). Return keys: move values and to_reconcile (`account/models/account_move_line.py:3085-3085`; documented `account/models/account_move_line.py:3008-3008`, built `account/models/account_move_line.py:3029-3029` and `account/models/account_move_line.py:3083-3083`).
- Creator `_create_exchange_difference_moves` (`account/models/account_move_line.py:3088-3140`): empty input returns early (`account/models/account_move_line.py:3096-3097`); UserError when the journal is missing (`account/models/account_move_line.py:3105-3109`), when the expense account is missing (`account/models/account_move_line.py:3116-3120`) or the income account is missing (`account/models/account_move_line.py:3121-3125`); creation under `no_exchange_difference=True` and `move_reverse_cancel=False` (`account/models/account_move_line.py:3128-3128`), with a comment that reconciliation is handled through the reconciled-lines relation (`account/models/account_move_line.py:3129-3129`); posting with soft=False and analytic validation off for values flagged to post (`account/models/account_move_line.py:3131-3138`).
- How the exchange line gets reconciled: the inverse of the reconciled-lines relation (`account/models/account_move_line.py:1468-1472`) calls the plan method (`account/models/account_move_line.py:1469-1469`). Read side: `account/models/account_move_line.py:1293-1299`, exchange-move compute `account/models/account_move_line.py:1277-1280`, excluding-exchange variant `account/models/account_move_line.py:1301-1307`.
- Linking the exchange move to its partial: the engine takes, in a loop, the first not-yet-used exchange move whose lines' reconciled-lines contain one of the partial's two lines, one-to-one through used sets (`account/models/account_move_line.py:2880-2891`). INFERENCE (UNKNOWN, RT): when partials share lines the pairing may not match the originating partial.
- Posting an invoice adds an existing partial's exchange move to the posting set: `account/models/account_move.py:5735-5737`.
- Docstring drift: the builder docstring still describes the entry as fixing lines "when fully reconciled in foreign currency" (`account/models/account_move_line.py:3001-3002`), while the code creates it per partial.
- `to_reconcile` is built but not consumed anywhere in Community. The only call sites are `account/models/account_move_line.py:2503-2503` and `account/models/account_move_line.py:2876-2876`. The payment-register wizard's own `to_reconcile` keys (`account/wizard/account_payment_register.py:1134-1134`, `account/wizard/account_payment_register.py:1205-1205`, `account/wizard/account_payment_register.py:1242-1242`, `account/wizard/account_payment_register.py:1281-1281`) are a different dictionary.
- Tax exigibility: exchange entries are always exigible, via `_get_tax_exigible_domain` (`account/models/account_move_line.py:3455-3473`; pointer U101 and U103).

## 5. Cash-basis trigger (pointer to U101)

- Trigger: any company among the plan lines has cash-basis exigibility and the line account is receivable or payable type (`account/models/account_move_line.py:2894-2896`). It runs unless `move_reverse_cancel` or `no_cash_basis` is set (`account/models/account_move_line.py:2898-2898`); the entries are created with `no_exchange_difference_no_recursive` set false (`account/models/account_move_line.py:2900-2902`), followed by storing draft values.
- Partial-side methods: collector `account/models/account_partial_reconcile.py:244-362` (journal UserError `account/models/account_partial_reconcile.py:276-279`), helper preparers `account/models/account_partial_reconcile.py:364-532`, entry creator `account/models/account_partial_reconcile.py:534-713` (date is the later of settlement date and fiscal lock date plus one day, `account/models/account_partial_reconcile.py:552-554`; post with soft=False `account/models/account_partial_reconcile.py:690-690`; follow-up reconcile with `add_caba_vals` `account/models/account_partial_reconcile.py:710-712`), draft values accessors `account/models/account_partial_reconcile.py:715-732`.
- Entry side: `_collect_tax_cash_basis_values` at `account/models/account_move.py:4124-4180` returns None unless an on-payment tax exists (`account/models/account_move.py:4177-4178`).
- Thai default: the company flag is set (section 11), yet the Thai tax data has no on-payment taxes, so the collector returns None and nothing is produced by default. Do not read this as a statement about Thai tax law.

## 6. Residual and state propagation

- Account side: stored `reconcile` compute (`account/models/account_account.py:665-674`), check `account/models/account_account.py:27-31`, toggles `account/models/account_account.py:965-1007` (turning off is blocked by pending partials, `account/models/account_account.py:990-999`; residual reset by raw SQL for lines without full reconcile), invoked from write at `account/models/account_account.py:1063-1068`. UNKNOWN (RT): enabling the flag on cash or credit-card accounts with pre-existing partials resets residuals without looking at partials (`account/models/account_account.py:965-981`).
- Payment state (pointer U204 and U12): partial create asks `_get_to_update_payments(from_state='in_process')` and sets state paid (`account/models/account_partial_reconcile.py:159-159`), then updates the matching number (`account/models/account_partial_reconcile.py:160-160`); the selector (`account/models/account_partial_reconcile.py:163-191`) considers payments without outstanding account in the requested state, compares the signed amount with the partial amount (`account/models/account_partial_reconcile.py:175-175`) and has group-payment logic (`account/models/account_partial_reconcile.py:178-190`). Unlink captures payments in state paid (`account/models/account_partial_reconcile.py:115-115`) and returns them to in process (`account/models/account_partial_reconcile.py:153-153`).
- Invoice paid hook: `account/models/account_move_line.py:2790-2794`; Community sale overrides the post step and the hook at `sale/models/account_move.py:120-133` and `sale/models/account_move.py:135-145`; the auto-reconcile call is at `sale/models/account_move.py:132-132`; the sale order reads `tx.payment_id.is_reconciled` at `sale/models/sale_order.py:1421-1425`.
- No scheduled behaviour: no cron reference in the three engine files (text search, no hits).

## 7. Unreconcile matrix

Core: `remove_move_reconcile` (`account/models/account_move_line.py:3146-3148`) simply unlinks the matched partials and does no lock, state or rights check of its own. The partial's unlink (`account/models/account_partial_reconcile.py:105-154`) does this in order:

1. capture payments to reset (`account/models/account_partial_reconcile.py:115-115`);
2. find cash-basis entries by origin partial (`account/models/account_partial_reconcile.py:117-117`) and exchange entries (`account/models/account_partial_reconcile.py:119-119`);
3. capture full-reconcile records (`account/models/account_partial_reconcile.py:122-122`) and all affected lines (`account/models/account_partial_reconcile.py:125-125`);
4. super unlink (`account/models/account_partial_reconcile.py:128-128`), then unlink the full-reconcile records (`account/models/account_partial_reconcile.py:131-131`);
5. reverse non-draft side entries, shifting the reversal date past a violated lock via the violated-lock-dates helper (`account/models/account_move.py:6753-6753`; used at `account/models/account_partial_reconcile.py:138-148`, latest lock plus one day at `account/models/account_partial_reconcile.py:143-143`, reversal call `account/models/account_partial_reconcile.py:148-148`); draft side entries are unlinked (`account/models/account_partial_reconcile.py:149-149`);
6. refresh matching numbers of surviving lines (`account/models/account_partial_reconcile.py:151-152`) and reset payment state (`account/models/account_partial_reconcile.py:153-153`).

Callers:

| Caller | Pointer | Behaviour |
|---|---|---|
| journal item write | `account/models/account_move_line.py:1860-1886` | protected reconciliation fields (account, date, balance, currency amount, currency) per `account/models/account_move_line.py:3485-3495`; account-only change allowed if the whole matching group is in the same write (`account/models/account_move_line.py:1870-1874`); statement-line set computed before removal (`account/models/account_move_line.py:1876-1878`); lock-violating statement lines filtered (`account/models/account_move_line.py:1879-1885`); the rest undone (`account/models/account_move_line.py:1886-1886`) |
| journal item unlink | `account/models/account_move_line.py:1991-2026` | unreconcile at `account/models/account_move_line.py:1995-1995`, before lock checks (`account/models/account_move_line.py:2001-2004`) and before super (`account/models/account_move_line.py:2024-2024`); the posted guard is an ondelete hook (`account/models/account_move_line.py:1959-1966`) that runs inside super, after the unreconcile; hashed guard `account/models/account_move_line.py:1982-1989` |
| move unlink | `account/models/account_move.py:4079-4088` | unreconcile `account/models/account_move.py:4083-4083`, line unlink under `dynamic_unlink` (`account/models/account_move.py:4084-4084`) |
| cancel button | `account/models/account_move.py:6384-6396` | draft step (`account/models/account_move.py:6387-6389`), unreconcile (`account/models/account_move.py:6394-6394`), payments canceled (`account/models/account_move.py:6395-6395`) |
| reverse with cancel | `account/models/account_move.py:5495-5539` | unreconciles originals (`account/models/account_move.py:5510-5510`), reverse posted under `move_reverse_cancel` (`account/models/account_move.py:5537-5537`), reversed lines reconciled by `account/models/account_move.py:5474-5492` (call `account/models/account_move.py:5775-5775`, reconcile `account/models/account_move.py:5491-5491`) |
| statement-line undo | `account/models/account_bank_statement_line.py:460-476` | removal at `account/models/account_bank_statement_line.py:468-468` |
| outstanding widget | `account/models/account_move.py:6239-6248` and `account/models/account_move.py:6250-6257` | assign calls reconcile (`account/models/account_move.py:6248-6248`); remove unlinks partials |
| match-entries action | `account/models/account_move_line.py:3150-3155` | thin wrapper |

Guards: set-to-draft (`account/models/account_move.py:6269-6284`) does not unreconcile; `_check_draftable` (`account/models/account_move.py:6348-6373`) blocks exchange entries (`account/models/account_move.py:6363-6364`), cash-basis entries (`account/models/account_move.py:6365-6371`) and hashed entries (`account/models/account_move.py:6372-6373`); `_can_be_unlinked` (`account/models/account_move.py:5541-5546`) uses the exchange link. `_unlink_or_reverse` (`account/models/account_move.py:5551-5567`) has no application caller in Community (tests only: `account/tests/test_kpi_provider.py:19-22`). Posting unlinks draft partials whose draft cash-basis values changed (`account/models/account_move.py:5725-5755`, unlink at `account/models/account_move.py:5744-5747` and `account/models/account_move.py:5754-5755`). `_check_reconciliation` (`account/models/account_move_line.py:1545-1550`) has no caller anywhere in Community.

## 8. Lock-date interplay (pointers to U114, U124, U220)

`reconcile()` itself performs no lock-date check. Engine-side touch points: reversal date shift in the partial unlink (`account/models/account_partial_reconcile.py:142-143`); statement-line filter in journal item write (`account/models/account_move_line.py:1879-1885`); checks in journal item unlink (`account/models/account_move_line.py:2003-2004`, after the unreconcile); `_check_fiscal_lock_dates` with sentinel `bypass_lock_check` (`account/models/account_move.py:2823-2840`); tax lock check (`account/models/account_move_line.py:1526-1543`); company helpers (`account/models/company.py:642-654`, `account/models/company.py:656-673`, `account/models/company.py:675-710`, `account/models/company.py:712-721`, `account/models/company.py:723-739`). The cash-basis date also respects the user fiscal lock (`account/models/account_partial_reconcile.py:552-554`). The exchange journal's accounting-date helper that feeds the exchange move date: `account/models/account_journal.py:520-527` (field at `account/models/account_journal.py:275-275`).

## 9. Callers and extension points

Non-test callers of `.reconcile()` found by text search:
`account_payment_interco/models/account_move.py:82-82`, `account_payment_interco/models/account_move.py:120-120`, `point_of_sale/models/pos_order.py:1171-1171`, `point_of_sale/models/pos_order.py:1237-1237`, `account_payment/models/payment_transaction.py:209-209`, `account/wizard/account_automatic_entry_wizard.py:478-478`, `account/wizard/account_automatic_entry_wizard.py:482-482`, `account/wizard/account_payment_register.py:1215-1215`, plus the engine's own `account/models/account_move_line.py:3178-3178`, `account/models/account_move_line.py:2987-2987` (inside the unreachable block), `account/models/account_move.py:5491-5491`, `account/models/account_move.py:6248-6248`.

Callers of the plan method directly: `point_of_sale/models/pos_session.py:1416-1416` (with `no_cash_basis`), `pos_online_payment/models/pos_session.py:73-73`, `account/wizard/account_automatic_entry_wizard.py:421-421`, `account/models/account_move_line.py:1469-1469`, `account/models/account_partial_reconcile.py:712-712`.

Callers of `remove_move_reconcile`: `account/models/account_move_line.py:1878-1878`, `account/models/account_move_line.py:1995-1995`, `account/models/account_move_line.py:3155-3155`, `account/models/account_bank_statement_line.py:468-468`, `account/models/account_move.py:4083-4083`, `account/models/account_move.py:5510-5510`, `account/models/account_move.py:6394-6394`.

Country packs (noted, not analysed): `l10n_latam_check/models/account_payment.py:192-192`, `l10n_latam_check/wizards/l10n_latam_payment_mass_transfer.py:120-120`, `l10n_latam_check/models/l10n_latam_check.py:123-123`, `l10n_latam_check/models/l10n_latam_check.py:130-131`, `l10n_in/wizard/l10n_in_withhold_wizard.py:243-243`.

No Community addon outside account defines or overrides an engine method. The sale module overrides the post step and paid hook only (section 6). purchase, purchase_stock and sale_stock have no engine override; stock_account has no reconcile hits (ABSENT). Valuation-side reads of `move_reverse_cancel`: `stock_account/models/account_move.py:22-22`, `stock_account/models/account_move.py:33-33`, `purchase_stock/models/account_invoice.py:114-114`.

## 10. Context-key matrix

| Key | Set | Read | Effect |
|---|---|---|---|
| no_exchange_difference | `account/wizard/account_automatic_entry_wizard.py:421-421`, `account/models/account_move_line.py:3128-3128`, `account/models/account_move_line.py:3178-3178` | `account/models/account_move_line.py:2442-2442`; forwarded `account/models/account_move_line.py:2854-2854` | suppresses exchange entry |
| no_exchange_difference_no_recursive | reset false at `account/models/account_move_line.py:2901-2901`; set true only in test `account/tests/test_account_move_reconcile.py:5992-5992` | `account/models/account_move_line.py:2442-2442`; forwarded `account/models/account_move_line.py:2855-2855` | suppresses exchange entry in follow-up passes |
| no_cash_basis | `point_of_sale/models/pos_session.py:1416-1416`, `account/wizard/account_automatic_entry_wizard.py:421-421`, `account/models/account_move_line.py:3178-3178` | `account/models/account_move_line.py:2898-2898` | skips cash-basis entries |
| move_reverse_cancel | `account/models/account_move.py:5537-5537`; set false `account/models/account_move_line.py:3128-3128` | `account/models/account_move_line.py:2898-2898`, `account/models/account_move.py:5474-5491`, `purchase_stock/models/account_invoice.py:114-114` | skips cash-basis for reverse-cancel |
| forced_rate_from_register_payment | `account/wizard/account_payment_register.py:1206-1206` | `account/models/account_move_line.py:2175-2175`, `account/models/account_partial_reconcile.py:332-333` | forces the rate |
| reduced_line_sorting | callers outside engine | `account/models/account_move_line.py:2713-2713` | shorter sort key |
| add_caba_vals | `account/models/account_partial_reconcile.py:712-712` | `account/models/account_move_line.py:2867-2867` | stores draft cash-basis values |
| skip_matching_number_check | callers | `account/models/account_move_line.py:1708-1708` | no I auto-prefix |
| force_delete, dynamic_unlink | `account/models/account_move.py:4081-4081` | `account/models/account_move_line.py:1962-1962`, `account/models/account_move_line.py:1970-1970` | unlink guards |
| validate_analytic | exchange creator | `account/models/account_move_line.py:3138-3138` | skips analytic validation |
| bypass_lock_check | callers | `account/models/account_move.py:2824-2824` | sentinel for fiscal check |
| ignore_tax_lock_date | callers | `account/models/account_move_line.py:2001-2001` | tax lock bypass |

## 11. Thai relevance

PRESENT (defaults feeding the engine):
- `l10n_th/models/template_th.py:28-28`: income exchange account id is the Thai gain account; `l10n_th/models/template_th.py:29-29`: expense exchange account id is the Thai loss account; `l10n_th/models/template_th.py:41-41`: `tax_exigibility` is set as the string True (the same string form also appears in other country templates: noted, not analysed).
- Account data: `l10n_th/data/template/account.account-th.csv:80-80` is code 421300 "Gain on Exchange Rate" (income_other, reconcile false); `l10n_th/data/template/account.account-th.csv:141-141` is code 621200 "Loss on Exchange Rate" (expense, reconcile false); `l10n_th/data/template/account.account-th.csv:7-7` and `l10n_th/data/template/account.account-th.csv:54-54` are trade receivables and payables (reconcile true).
- The exchange journal is not Thai-specific: the generic root template builds the EXCH journal (`account/models/chart_template.py:719-720`; definition `account/models/chart_template.py:1149-1193`, exchange journal at `account/models/chart_template.py:1175-1180`, name "Exchange Difference", general type, code EXCH). `l10n_th` defines no journal override.
- Tax data header `l10n_th/data/template/account.tax-th.csv:1-1` has no exigibility column and the file has zero on-payment hits, so the cash-basis collector returns None by default (section 5).
- Currency of the Thai company was not read from the template; no statement is made about it.

ABSENT (extension): `l10n_th` contains no engine override and no reconcile call. Directory listing of `l10n_th/` (images excluded): `__init__.py`, `__manifest__.py`, `demo/demo_company.xml`, `tests/__init__.py`, `tests/test_l10n_th_emv_qr.py`, `models/__init__.py`, `models/account_move.py`, `models/ir_actions_report.py`, `models/res_bank.py`, `models/res_partner.py`, `models/template_th.py`, `i18n/l10n_th.pot`, `i18n/th.po`, `data/account_tax_report_data.xml`, `data/template/account.account-th.csv`, `data/template/account.asset-th.csv`, `data/template/account.tax-th.csv`, `data/template/account.tax.group-th.csv`, `views/report_invoice.xml`. `l10n_th/models/account_move.py` only extends the invoice report name. The only reconcile-adjacent hit is a test reading `amount_residual` at `l10n_th/tests/test_l10n_th_emv_qr.py:69-69`, which is not an engine override.

## 12. Dead or unused code observed

- Cash-basis rounding block `account/models/account_move_line.py:2968-2987` reads `caba_lines_to_reconcile` and `exchange_move` keys that no batch dict sets (the batch append at `account/models/account_move_line.py:2935-2938` sets only the lines and the flag; the key name appears in the entire `odoo/` tree only at `account/models/account_move_line.py:2972-2972`, `account/models/account_move_line.py:2975-2975`, `account/models/account_move_line.py:2977-2977`). The block is unreachable.
- `to_reconcile` in the exchange builder output is not consumed (section 4).
- `_check_reconciliation` and `_unlink_or_reverse` have no application caller (section 7).

## 13. Ten-dimension summary

| Dimension | Summary |
|---|---|
| Happy path | `reconcile()` sorts and validates, builds partial values, bulk-creates partials, creates exchange entries per partial when a foreign amount shifts, creates a full-reconcile record when every line has zero residual, updates matching numbers by raw SQL, then runs the paid hook (`account/models/account_move_line.py:2821-2989`) |
| Reversal | Unlinking partials resets residuals (stored compute), removes full-reconcile records, reverses or unlinks cash-basis and exchange entries, resets payment state (`account/models/account_partial_reconcile.py:105-154`) |
| Multi-company | Entry check rejects lines from more than one company root (`account/models/account_move_line.py:2676-2680`); partial company follows the debit line when its move is an invoice (`account/models/account_partial_reconcile.py:92-99`); the exchange builder resolves company per line move (`account/models/account_move_line.py:3011-3014`); the group helper reads through sudo (`account/models/account_move_line.py:3410-3419`) |
| Side effects | Payment state change (`account/models/account_partial_reconcile.py:159-159`), exchange and cash-basis entries, matching numbers, invoice paid hook, sale auto-reconcile on posting (`sale/models/account_move.py:132-132`) |
| Configuration | Company exchange journal and gain and loss accounts (`account/models/company.py:133-143`), cash-basis flag per company, account reconcile flag (`account/models/account_account.py:665-674`) |
| Validation | Entry checks (`account/models/account_move_line.py:2651-2686`), off-balance guard (`account/models/account_move_line.py:1496-1505`), matching-number constraint (`account/models/account_move_line.py:1593-1610`), partial currency constraint (`account/models/account_partial_reconcile.py:74-78`) |
| Roles | Account user group has full rights on both models; readonly group read only; invoicing group full rights; salesman and purchase user read only on partials (`account/security/ir.model.access.csv:97-102`; `sale/security/ir.model.access.csv:10-10`; `purchase/security/ir.model.access.csv:29-29`); no record rules found |
| Scheduled | None found in the engine files |
| Exceptions | UserError for entry validity and missing exchange configuration (`account/models/account_move_line.py:3105-3125`), plain Exception in the matching-number constraint, ValueError in full-reconcile create (`account/models/account_full_reconcile.py:14-21`) |
| Accounting implications | Exchange entries are posted always exigible and move rate differences to the company gain or loss account; unreconcile reverses them in the original period unless a lock forces a later date; full-reconcile records carry no date or exchange link of their own |

Short D1/D2/D3 flavour: D1 (what it is) — an engine of partial records plus a thin full-reconcile marker, driven from journal items. D2 (how it behaves) — per-partial exchange entries, raw-SQL matching numbers, unreconcile that reverses side entries. D3 (where it bites) — no lock check in `remove_move_reconcile`, first-match exchange linking, constraint exceptions that are not ValidationError, unreachable rounding block.

## 14. UNKNOWN and RT list

1. Exchange-move link heuristic (`account/models/account_move_line.py:2880-2891`) may mismatch when partials share lines. RT.
2. Leftover loop variable `move` near `account/models/account_move.py:5749-5749` and its effect on cash-basis draft handling (U101). RT.
3. Live database foreign-key actions (only ORM defaults read). RT.
4. Operator precedence in the reverse reconcile condition at `account/models/account_move.py:5487-5490`. RT.
5. Rollback behaviour of journal item unlink, which unreconciles (`account/models/account_move_line.py:1995-1995`) before the posted guard runs. RT.
6. Whether cash-basis is attempted for exchange-line partials in a company with the flag on (U101). RT.
7. Account-level reconcile toggle with pre-existing partials on cash or credit-card accounts (`account/models/account_account.py:965-981`). RT.
8. Timing of the full-reconcile link copied into exchange line values (`account/models/account_move_line.py:3060-3060`): normally empty at build time because the full reconcile is created later (`account/models/account_move_line.py:2966-2966`). INFERENCE.
9. Raw-SQL matching-number writes bypass the Python constraint. INFERENCE.
10. Builder None-return path unreachable from the single call site. INFERENCE.
11. Load-time conversion of the string-valued exigibility in templates.
12. Group helper reads through sudo, so record rules are not applied when gathering matching groups (`account/models/account_move_line.py:3410-3419`).
13. No runtime or database verification was possible.

## 15. FUNCTION MAPPING REQUIRED

No existing function id in `00_CONTROL/EXISTING_FUNCTION_ID_INDEX_53.json` matches this unit. Neighbours reviewed and rejected: PDT-F04, RCN-F01, RCN-F02, RCN-F03, and PCO-F01 (a lock-date policy neighbour only). Proposed new function ids (26):

| Claim | Function id | Class and flag |
|---|---|---|
| U239-C01 | partial-reconcile-fields | STRUCTURAL CORE |
| U239-C02 | partial-reconcile-company-date-checks | COMPUTE CORE |
| U239-C03 | full-reconcile-declaration | STRUCTURAL CORE |
| U239-C04 | full-reconcile-create-unlink | BEHAVIOR CORE |
| U239-C05 | line-reconcile-mirror-fields | STRUCTURAL CORE |
| U239-C06 | line-residual-compute | COMPUTE CORE |
| U239-C07 | matching-number-convention | COMPUTE CORE |
| U239-C08 | reconcile-entry-plan | ROUTING CORE |
| U239-C09 | plan-sort-split-validate | ORDERING CORE |
| U239-C10 | single-partial-matching | COMPUTE CORE |
| U239-C11 | reconcile-rate-selection | COMPUTE CORE |
| U239-C12 | partial-creation-full-detection | BEHAVIOR CORE |
| U239-C13 | exchange-suppress-contexts | BEHAVIOR CORE |
| U239-C14 | exchange-move-builder | COMPUTE CORE |
| U239-C15 | exchange-move-creation-link | BEHAVIOR CORE |
| U239-C16 | caba-engine-trigger | ROUTING CORE |
| U239-C17 | partial-create-payment-state | BEHAVIOR CORE |
| U239-C18 | partial-unlink-cascade | BEHAVIOR CORE |
| U239-C19 | line-write-unlink-unreconcile | BEHAVIOR CORE |
| U239-C20 | draft-cancel-guards | BEHAVIOR CORE |
| U239-C21 | reconcile-access-rows | STRUCTURAL CORE |
| U239-C22 | thai-exchange-defaults | MODULE |
| U239-C23 | thai-no-reconcile-extension | MODULE |
| U239-C24 | sale-reconcile-hooks | MODULE |
| U239-C25 | matching-number-validation-migration | MIGRATION_FLAG |
| U239-C26 | unused-values-dead-block-migration | MIGRATION_FLAG |

## 16. MIGRATION FLAGS

### 16.1 OBSERVED in this tree (Odoo 19 Community)

1. `reconcile()` returns None (`account/models/account_move_line.py:3142-3144`).
2. matching_number format and the I auto-prefix (`account/models/account_move_line.py:1597-1597`, `account/models/account_move_line.py:1705-1710`).
3. Engine writes matching numbers by raw SQL (`account/models/account_partial_reconcile.py:227-235`).
4. Exchange-difference entries are created per partial (`account/models/account_move_line.py:2876-2876`).
5. The full-reconcile model has no name and no exchange link (`account/models/account_full_reconcile.py:9-10`).
6. `to_reconcile` from the exchange builder is unused (`account/models/account_move_line.py:3085-3085`).
7. Cash-basis rounding block is dead (`account/models/account_move_line.py:2968-2987`).
8. `_check_reconciliation` has no caller (`account/models/account_move_line.py:1545-1550`).
9. `_unlink_or_reverse` has no application caller (`account/models/account_move.py:5551-5567`).
10. String-valued exigibility in the Thai template (`l10n_th/models/template_th.py:41-41`).
11. `remove_move_reconcile` has no engine-side lock check while the partial unlink shifts reversal dates (`account/models/account_move_line.py:3146-3148`; `account/models/account_partial_reconcile.py:138-148`).
12. Exchange-move first-match linking heuristic (`account/models/account_move_line.py:2880-2891`).

### 16.2 PRIOR-VERSION-KNOWLEDGE (hedged, not verified in this tree)

- **PRIOR-VERSION-KNOWLEDGE:** the Char matching_number with the P and decimal convention is believed to have been introduced around version 17.0, replacing the older name carried by the full-reconcile record.
- **PRIOR-VERSION-KNOWLEDGE:** earlier majors are believed to name the pairing method `_prepare_reconciliation_partials`; this tree uses `_prepare_reconciliation_amls`.
- **PRIOR-VERSION-KNOWLEDGE:** the exchange move was believed to be reconciled through an explicit loop over `to_reconcile`; this tree uses the reconciled-lines inverse.
- **PRIOR-VERSION-KNOWLEDGE:** older `reconcile()` is believed to document a summary-dictionary return; this tree returns None.
- **PRIOR-VERSION-KNOWLEDGE:** older `_check_reconciliation` is believed to have had a live role; here it has no caller.
- **PRIOR-VERSION-KNOWLEDGE:** the dead cash-basis rounding block is believed to be residue of an earlier design.
- **PRIOR-VERSION-KNOWLEDGE:** the builder docstring (`account/models/account_move_line.py:3001-3002`) is believed to describe earlier behaviour, where some majors created exchange entries only when a group became fully reconciled.
- **PRIOR-VERSION-KNOWLEDGE:** earlier majors are believed to carry a name and an exchange-move field on the full-reconcile record; both are ABSENT here.

Any migration mapping that depends on these prior-version items must be re-verified against the older source before use.

## 17. Source files verified

Read in full or in cited ranges: `account/models/account_partial_reconcile.py`, `account/models/account_full_reconcile.py`, `account/models/account_move_line.py`, `account/models/account_move.py`, `account/models/company.py`, `account/models/account_account.py`, `account/models/account_journal.py`, `account/models/account_bank_statement_line.py`, `account/models/chart_template.py`, `account/security/ir.model.access.csv`, `account/wizard/account_payment_register.py`, `account/wizard/account_automatic_entry_wizard.py`, `l10n_th/models/template_th.py`, `l10n_th/data/template/account.account-th.csv`, `l10n_th/data/template/account.tax-th.csv`, `l10n_th/models/account_move.py`, `sale/models/account_move.py`, `sale/models/sale_order.py`, `odoo/orm/fields_relational.py`. Text-search only: other callers, ACL rows in sale, sale_stock and purchase, country packs (noted, not analysed), the stock valuation reads, cron references.
