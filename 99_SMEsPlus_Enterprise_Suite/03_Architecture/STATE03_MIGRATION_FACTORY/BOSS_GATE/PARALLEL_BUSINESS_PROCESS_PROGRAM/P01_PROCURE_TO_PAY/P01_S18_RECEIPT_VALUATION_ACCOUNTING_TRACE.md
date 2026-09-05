# P01 — SERIES-18 RECEIPT → VALUATION → ACCOUNTING DIRECT TRACE

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S18-03`

**What is new here.** Every previous P01 trace crossed generations: a mechanism read in one
series, a population measured in another. This one does not. Source, configuration, policy and
records are all series 18, all from the same deployment.

Each transition below is reported in four columns that must not be merged:
**source-supported mechanism** (the code says it) · **configured mechanism** (this deployment sets
it up) · **deployed records** (rows exist) · **runtime action not directly evidenced** (what we
still cannot see without executing).


> ### PEER DELTA APPLIED — BOUND TO ONE IDENTITY
>
> Peer **P04** (`9e377e30`, `P04-F-101`) records **three** series-18 database identities on this
> host, not one: `551ab874` (361 modules — the one analysed here), `4b766580` (478 modules), and
> `96548e18` (`T805efaplus`, 123 modules, never transacted). **Everything in this document is
> bounded to `551ab874` @ 2026-08-30** and is not a claim about the series-18 generation as
> deployed elsewhere. See `P01_S18_PEER_DELTA_HANDOFF.md §2.2`.

---

## 1. THE CHAIN, END TO END

| # | Transition | Source mechanism | Configured | Deployed records | Not directly evidenced |
|---|---|---|---|---|---|
| 1 | Purchase Request → Purchase Order | `purchase_request` 18.0.1.10.0, `purchase_request_line.purchase_state`, `stock_move.created_purchase_request_line_id` | yes | 1,043 requests; 3,398 lines; **1,504 lines linked to a PO** | the approval UI actions themselves |
| 2 | PO confirmation | `purchase.order.button_confirm`; custom guard `scgl_product_category_company` `_scgl_validate_product_company_scope` | yes | 13,887 POs, 13,735 in `purchase` | whether the guard has ever refused (§6) |
| 3 | PO → Receipt | `purchase_stock`, `stock.picking` incoming | yes | 2,516 incoming pickings, **1,305 done**; 3,158 moves linked to a PO line, 3,124 done | **the move population is not a clean one-to-one receipt set** — `purchase_request` overrides `_prepare_merge_moves_distinct_fields`, `_merge_moves_fields`, `_prepare_merge_move_sort_method` and `stock.picking._action_done`; the counts are what the data says, their reading as distinct receipts is not established (§9.1) |
| 4 | Receipt → Valuation layer | `stock_move._create_in_svl` → `stock.valuation.layer` | yes | **1,403** of 3,124 done PO-linked moves carry layers (2,146 layers, **฿22,953,527.29**) — **2,085 of those layers are migrated**, 61 are runtime output. 1,480 done storable receipts carry **no** layer | the loader did not build layers move-by-move (`P01_S18_PERIODIC_PERPETUAL_POLICY_PROOF.md §8.4`) |
| 5 | **Valuation layer → Journal entry** | `stock_valuation_layer._validate_accounting_entries` (`R1:…:74-95`), gated `valuation == 'real_time'` | **gate closed** — policy is `manual_periodic` on 126/126 categories × 4/4 companies | **0 of 47,801** layers carry `account_move_id`; **0 of the corrected 558**; **0 of the 541 core**; **0 of the 61 purchase-linked** | `account_move_line_id` has a **second writer that is not valuation-gated** (`ERR-P01-26`); and a Python method override in a custom module would leave no database trace (10 of 16 unverifiable) |
| 6 | Journal entry → Stock journal | `stock_move.py:199-206` `journal_id = company.account_stock_journal_id` / category `property_stock_journal` | **yes**, all four companies (`STJ`) | **0 items** in journals 16/24/32/40 | — |
| 7 | Journal entry → Clearing account | `_get_accounting_data_for_valuation` returns the input account for an in-move | **yes**, 171 of 504 (category, company) pairs | **0 items** on accounts 176/62/100/138 | — |
| 8 | Receipt → Vendor Bill | `purchase_stock`, `purchase_order_line.qty_invoiced` | yes | 1,904 vendor bills; 2,606 of 3,375 bill product lines carry a `purchase_line_id` | which user created which bill |
| 9 | **Bill line → account** | v19 overrides this to the valuation account; **v18 has no such override** (§4) | n/a | 3,375 product lines → **expense**; top accounts 186 (1,062) and 72 (966), both `510000 Cost of Revenue` | — |
| 10 | Bill → AP | `account.move` payment-term line on the partner payable | yes | 1,904 payment-term lines; **1,894** on a payable account, **10 are not** (§7) | — |
| 11 | AP → Payment | `account.payment` | yes | 3,508 payments, **1,183 supplier** | — |
| 12 | Payment → Reconciliation | `account.partial.reconcile` / `account.full.reconcile` | yes | 5,071 partial, 2,343 full; **1,370 of 1,894** bill AP lines reconciled | — |

---

## 2. THE BREAK IS AT STEP 5, AND IT IS A DESIGNED BREAK

Steps 1–4 execute. Steps 6 and 7 are configured and never fire. The chain does not break because
something failed; it breaks because **step 5's gate is closed by configuration**, and steps 6 and 7
are downstream of it.

Proved in `P01_S18_PERIODIC_PERPETUAL_POLICY_PROOF.md`:
`if not svl.…product_id.valuation == 'real_time': continue`, and the policy is `manual_periodic`
for every product in every company, read from both storage locations, with no product-level
override possible in this generation.

**No accounting entry at receipt is the specified behaviour of this configuration.**

---

## 3. WHAT THE LEDGER ACTUALLY CONTAINS INSTEAD

| Path | Items | Where |
|---|---|---|
| Valuation path (`STJ` journals) | **0** | — |
| Clearing account `210300` | **0** | — |
| Inventory `130000` (account 169) | 2,940 | **all** in journal 45 `MIG26 "COA Migration 2026"`, all `entry`, all posted, 2026-01-03 → 2026-08-25 |
| Vendor bill expense | 2,814 items of type `expense_direct_cost`, 477 of type `expense` | journals `AP` |

Inventory value in this ledger is **entirely migrated**. Nothing the series-18 runtime has done
since 2026-08-18 has moved inventory value into the general ledger, and under periodic valuation
nothing was supposed to.

---

## 4. STEP 9 IS A CONFIGURATION DIFFERENCE, NOT A GENERATION DIFFERENCE — `ERR-P01-30`

> **The first published version of this section was wrong, and wrong in a way that mattered.**
> It said the bill-line override to the stock account is *"a series-19 mechanism, NOT REACHABLE in
> series 18"*. **The mechanism exists in series 18.** Found by AAS-03 Expert C; verified here
> before adoption.

**How the error was made.** The search unit was a **file name**. The series-19 tree carries the
behaviour in `stock_account/models/account_move_line.py`; the series-18 `stock_account/models/`
directory has no file of that name, and that was read as the behaviour being absent. **The class
is in `account_move.py`.**

`R1:stock_account/models/account_move.py:264-279`, verbatim:

```
class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    ...
    def _compute_account_id(self):
        super()._compute_account_id()
        input_lines = self.filtered(lambda line: (
            line._eligible_for_cogs()
            and line.move_id.company_id.anglo_saxon_accounting
            and line.move_id.is_purchase_document()
        ))
        for line in input_lines:
            fiscal_position = line.move_id.fiscal_position_id
            accounts = line.with_company(line.company_id).product_id.product_tmpl_id.get_product_accounts(fiscal_pos=fiscal_position)
            if accounts['stock_input']:
                line.account_id = accounts['stock_input']

    def _eligible_for_cogs(self):
        self.ensure_one()
        return self.product_id.is_storable and self.product_id.valuation == 'real_time'
```

**The conclusion survives; the cause is replaced.**

| | First published | Corrected |
|---|---|---|
| No bill line posts to a clearing or valuation account | **correct** | **correct** |
| Why | *the code does not exist in this generation* | **the code exists and is gated by two configuration values** |
| Gate 1 — `anglo_saxon_accounting` | not considered | **already `true` in company 1** |
| Gate 2 — `valuation == 'real_time'` | — | closed everywhere (126/126 × 4/4) |
| `accounts['stock_input']` truthiness | — | **already 176 on 126 of 126 categories in company 1** |

**Note the difference this makes.** The first version implied the deployment is *structurally
immune* to bill-line redirection. It is not. In company 1, **two of the three conditions are
already satisfied**, and the third is a single company-dependent field value.

There is a genuine generation difference alongside it, and it has **three** parts, not one:

| | v18 (`account_move.py:264`) | v19 (`account_move_line.py:13`) |
|---|---|---|
| **Target account** | `accounts['stock_input']` — the **GRNI/clearing** account | `accounts['stock_valuation']` |
| **`anglo_saxon_accounting` gate** | **required** | **removed** |
| Valuation gate | `real_time`, inside `_eligible_for_cogs` | `real_time`, inline |
| Dropship exclusion | none | `_eligible_for_stock_account()` excludes dropshipped |

**The second row is a migration exposure this package did not carry.** In v18 the override cannot
fire in companies 2, 3 and 4 because `anglo_saxon_accounting` is **FALSE** in all three. **v19 drops
that gate.** On a migration to series 19, the only remaining condition in those three companies
would be the valuation policy — and the bill-line redirection would become live for them in a way
it structurally cannot be today.

**This is stated as an exposure to be tested, not as a prediction.** It is handed to P11 and
recorded as `EVIDENCE REQUIRED NEXT`.

**The generation split is clean in both directions and does not rest on one tree:** across every
`stock_account` tree on this host, **15 of 15 series-18 trees lack
`stock_account/models/account_move_line.py`, and 8 of 8 series-19 trees carry it**, with no
counterexample. And the governing v18 predicate is **build-invariant**: 14 of the 15 series-18 trees
carry a byte-identical `_eligible_for_cogs` body, and the fifteenth has no `account_move.py` at all.
That matters because **6 distinct contents of that file exist among those 15 trees**
(`ERR-P01-39`).

**CLASSIFICATION: CONFIGURATION-DEPENDENT — REACHABLE IN PRINCIPLE, NOT EXERCISED.**
Deployed records agree that it is not exercised: 3,375 vendor-bill product lines, largest accounts
`510000 Cost of Revenue` in each company, none to a valuation or clearing account.

**Method note, recorded because the class recurs.** The search unit (a file name) did not match the
claim unit (a behaviour). This is the same failure shape as `ERR-P01-23` (a directory standing in
for a population) and `ERR-P01-28` (days standing in for periods): **the unit of the search must be
the unit of the claim.**

---

## 5. ANGLO-SAXON ACCOUNTING IS ENABLED IN ONE COMPANY AND INERT

| Company | `anglo_saxon_accounting` |
|---|---|
| 1 | **true** |
| 2, 3, 4 | false |

`R1:stock_account/models/account_move.py:278`:
`return self.product_id.is_storable and self.product_id.valuation == 'real_time'`

Company 1 has anglo-saxon accounting switched on and **no product that satisfies the second
condition**. The setting is live and can never take effect under the current policy.

**CLASSIFICATION: CONFIGURED, NOT EXECUTED — POLICY-DEPENDENT.** This is a second, independent
instance of the same shape as the clearing account: the configuration anticipates perpetual
valuation and the policy switch does not.

---

## 6. THE CUSTOM COMPANY-SCOPE GUARD AT STEP 2 — EXECUTES, CANNOT REFUSE

`scgl_product_category_company` 18.0.1.5.0 is installed **and** has a version-matching source copy
on this host — one of only 6 of 16 that do. It adds to `purchase.order`:

```
def button_confirm(self):
    self._scgl_validate_product_company_scope()
    return super().button_confirm()
```

plus an `@api.constrains` on `purchase.order.line`. Products must belong to a category permitted
for the order's company.

**Deployed configuration:**

| Control | Value |
|---|---|
| `scgl_allow_purchase` | **true on 126 of 126 categories** |
| Categories with an explicit company scope (`scgl_product_category_company_rel`) | **16 of 126** (32 rows) |
| Categories with no scope — the module documents *"Empty Companies means All Companies"* | **110 of 126** |
| Of the 15 GRNI-configured categories, how many are scoped | 3 |

**The guard runs on every purchase order confirmation and permits everything for 110 of 126
categories.** This is the same shape as P01's series-19 finding that the company-consistency guard
"executes but is vacuous" — and here the cause is provable: **configuration, not code.** The code
is capable of refusing; the data never asks it to.

### 6.1 The hook surface is wider than first reported

An AST enumeration of the version-matching source gives the module's full surface, and the first
version of this section named two of its ten hooks:

```
product.category     15 methods incl. _search, 2 @api.constrains
product.template     11 methods incl. name_search, 2 @api.constrains
product.product      _scgl_assert_company_allowed, name_search
sale.order           _scgl_validate_product_company_scope, action_confirm
sale.order.line      @api.constrains('product_id','order_id')
purchase.order       _scgl_validate_product_company_scope, button_confirm
purchase.order.line  @api.constrains('product_id','order_id')
stock.move           @api.constrains('product_id','company_id')
stock.picking        _scgl_validate_product_company_scope, action_confirm, button_validate
account.move         _scgl_validate_product_company_scope, action_post      <-- not first reported
account.move.line    @api.constrains('product_id','move_id')                <-- not first reported
```

**The guard also wraps `account.move.action_post` and constrains `account.move.line`.** The vacuity
finding is unchanged in direction — 110 of 126 categories still permit everything — but its **scope
was understated**: the same non-restrictive guard sits on **every journal posting, every picking
validation and every sale confirmation**, not only on purchase-order confirmation.

**CLASSIFICATION: INSTALLED, CONFIGURED, REACHABLE, EXERCISED — and non-restrictive for 87% of
categories by configuration, across ten hooks rather than two.** Not a code defect. A control that
has been switched to permit, on a wider surface than first reported.

---

## 7. TEN VENDOR BILLS WHOSE LIABILITY SITS OUTSIDE THE AP SUBLEDGER

Of 1,904 payment-term (balancing) lines on vendor bills, **1,894 are on an account of type
`liability_payable`. Ten are not.** All ten are posted, all in company 2:

| Account | Code | Type | Bills | Total credit |
|---|---|---|---|---|
| 391 | `218001` เจ้าหนี้อื่น (other payables) | `liability_current` | 9 | ฿1,788.27 |
| 393 | `221002` เจ้าหนี้เช่าซื้อ/ลีสซิ่ง - ระยะยาว (finance lease, long term) | `liability_non_current` | 1 | ฿11,181.00 |

Moves: `AP2026/01/000105`, `AP2026/02/000026`, `AP2026/02/000104`, `AP2026/03/000092`,
`AP2026/04/000054`, `AP2026/05/000087`, `AP2026/06/000005`, `AP2026/06/000006`,
`AP2026/07/000030`, `AP2026/07/000083`.

**The amount is small — ฿12,969.27 in total — and the mechanism is not.** These liabilities are
outside the payables subledger: they do not appear in an ageing keyed on `liability_payable`, and
standard payment matching against the partner's payable account will not reach them. Nine of the
ten are a recurring small monthly amount in company 2, which is consistent with a deliberate
mapping rather than an accident; the tenth is a finance-lease liability correctly typed as
non-current but reached through a vendor bill.

**CLASSIFICATION: FACT VERIFIED (10 of 1,904).** Whether this is intended is
**UNRESOLVED — EVIDENCE REQUIRED**; it needs the configuration owner, not more querying. Handed to
P08 and P11 because the consequence is a subledger-to-ledger reconciliation difference, which is
their scope, not P01's.

---

## 8. WHAT REMAINS NOT DIRECTLY EVIDENCED

Read-only evidence at rest cannot show:

- that any specific runtime path **executed** — only that its records exist. Every "EXERCISED"
  classification in this package is an inference from records to execution, and it is labelled as
  such;
- **who** performed an action, beyond `create_uid` / `write_uid`;
- whether the custom company-scope guard has ever **refused** a confirmation. A refusal leaves no
  row. Its non-restrictiveness (§6) is proved from configuration, not from an absence of refusals;
- what would happen under a **changed** policy. Every "would become live if the policy changed"
  statement in this package is a source-supported prediction, not an observation.

### 9.1 Two installed modules bound what the counts in this document can mean

**`purchase_request` 18.0.1.10.0** overrides the stock-move **merge fields, merge sort key** and
`stock.picking._action_done`. Every move count here — 3,158 purchase-linked, 3,124 done, 1,403
carrying valuation layers — is counted over a table whose merge semantics an installed module
changes. **The figures are what the data says; their interpretation as a one-to-one receipt
population is not established.**

**`om_data_remove` 18.0.1.0.0 is installed.** The only source copy located is version **19.0.1.1**,
so its content is **not evidence about the deployed module** — but that copy deletes by raw SQL
(`sql = "delete from %s" % t_name`), names **`stock.valuation.layer`** in its target list, and
separately deletes rows from **`ir_default`** — the exact table the valuation-policy proof reads.
Peer **P06** records this module as deleting ledger data without authorisation in another
deployment.

**This disproves nothing**: a raw `DELETE` leaves no trace, so the absence of evidence of a purge is
expected either way. **It bounds the claims.** The 47,801 valuation layers and the single global
`ir_default` row for `property_valuation` are the **post-hoc state of tables a resident, installed
module can silently empty.** Every count in this package is a count of what remains.

Executing any of these requires a runtime, which the standing constraint forbids without explicit
authorization. Recorded as `HOLD — RUNTIME WRITE AUTHORIZATION REQUIRED` for the seven priority
edge cases in `P01_EDGE_CASE_TEST_MATRIX.md`, unchanged from previous rounds.
