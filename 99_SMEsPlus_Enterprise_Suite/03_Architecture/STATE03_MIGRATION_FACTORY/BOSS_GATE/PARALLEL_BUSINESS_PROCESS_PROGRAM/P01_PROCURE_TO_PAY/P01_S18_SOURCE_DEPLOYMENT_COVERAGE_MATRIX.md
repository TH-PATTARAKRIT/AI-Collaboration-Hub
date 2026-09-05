# P01 — SERIES-18 SOURCE ↔ DEPLOYMENT COVERAGE MATRIX

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S18-02`

**Source population:** the material P01 findings recorded in `P01_VERSION_SENSITIVE_FINDING_REGISTER.md §1`
that were previously limited by the absence of a same-series deployment. **No target count was
manufactured**; the matrix contains exactly those the register carries, plus findings this run
produced. Findings whose evidence class is `V16 DEPLOYMENT` or `V19 DEPLOYMENT` only are included
where a series-18 check is now possible, and marked where it is not.

Column meanings: **INSTALLED** — the module is in `ir_module_module` with `state = installed`.
**CONFIG** — the configuration the mechanism requires is present. **POPULATION** — deployed rows
exist that the mechanism would act on. **EFFECT** — an observable financial effect in the ledger.


> ### PEER DELTA APPLIED — BOUND TO ONE IDENTITY
>
> Peer **P04** (`9e377e30`, `P04-F-101`) records **three** series-18 database identities on this
> host, not one: `551ab874` (361 modules — the one analysed here), `4b766580` (478 modules), and
> `96548e18` (`T805efaplus`, 123 modules, never transacted). **Everything in this document is
> bounded to `551ab874` @ 2026-08-30** and is not a claim about the series-18 generation as
> deployed elsewhere. See `P01_S18_PEER_DELTA_HANDOFF.md §2.2`.

---

## 1. THE MATRIX

| # | Finding | Source module | Model / function | Source locator | Expected event semantic | Installed | Config prerequisite | Config | Deployed population | Observable effect | Classification now | Evidence gap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-01 | Order confirmation creates no accounting effect | `purchase` | `purchase.order.button_confirm` / `button_approve` | `R1:purchase/models/purchase_order.py:516-545` | state + `date_approve` only | yes 18.0.1.2 | none | n/a | 13,887 POs, 13,735 confirmed | **no journal entry references a PO** | **CONFIRMED SAME-GENERATION** | none |
| C-02 | Receipt valuation gated on item type and valuation mode | `stock_account` | `_validate_accounting_entries` | `R1:stock_account/models/stock_valuation_layer.py:74-95` | gate on `valuation == 'real_time'` | yes 18.0.1.1 | valuation policy | **`manual_periodic` 126/126 × 4/4** | 47,801 layers; **558** business-document runtime layers, core **541** | **0 journal links** on all three denominators | **CONFIRMED SAME-GENERATION — gate closed**, scoped to 43,227 rows; over-determined for 4,574 | `account_move_line_id` has a **non-valuation-gated writer** (`ERR-P01-26`); method-level override unverifiable for 10 of 16 custom modules |
| C-03 | Goods-received clearing bridge exists | `stock_account` | `_get_accounting_data_for_valuation` → `_account_entry_move` | `R1:…/stock_move.py:477, 703` | interim liability at receipt | yes | input account + stock journal | **171 of 504 pairs; journals 4/4** | 1,403 PO receipt moves carrying 2,146 layers, ฿22,953,527.29 — but **2,085 of those layers are migrated**; **61** are runtime layers | **0 items on `210300`** | **CONFIGURED · NOT EXECUTED · POLICY-DEPENDENT** | the runtime claim rests on **61** layers; intent unresolved |
| C-04 | Clearing account reconciled only if flagged | `stock_account` | `_stock_account_anglo_saxon_reconcile_valuation` | `R1:stock_account/models/account_move.py:183-235` | reconcile interim vs bill | yes | `reconcile = true` on the account | **true, all four** | — | **no items to reconcile** | **LATENT — CONFIG PRESENT, NOT REACHED** | would need `real_time` to observe |
| C-05 | Price-difference replay engine using audit-log ordering | `purchase_stock` | `account_move_line` replay from `mail.tracking_value` | `R1:purchase_stock/models/account_move_line.py:68, 277` | price difference at bill | yes 18.0.1.2 | expense/price-difference account | `property_account_creditor_price_difference_categ` **NULL 126/126** | `price_diff_value != 0` on **0 of 47,801** | **none** | **NOT REACHABLE — configuration absent and policy closed** | none |
| C-06 | Bill-line account redirected to a stock account | `stock_account` | `AccountMoveLine._compute_account_id` / `_eligible_for_cogs` | **`R1:stock_account/models/account_move.py:264-279`** (v18, in `account_move.py`); `R3:…/account_move_line.py:13-24` (v19) | v18 → **input/clearing** account; v19 → **valuation** account | **yes — present in v18** | `anglo_saxon_accounting` **and** `real_time` | **gate 1 already true in co 1; gate 2 closed; `stock_input` already resolves on 126/126 in co 1** | 3,375 bill product lines | **all to expense** (186: 1,062; 72: 966) | **CONFIGURATION-DEPENDENT — REACHABLE IN PRINCIPLE, NOT EXERCISED.** ~~CONTRADICTED FOR SERIES 18~~ **CORRECTED — `ERR-P01-30`** | the v19 difference is the **target account**, not the existence of the mechanism |
| C-07 | Bill is the only universal accounting event | `account` | `account.move._post` | cross-version | expense + payable at bill | yes | — | — | 1,904 bills; 6,914 items | **yes — the only P2P ledger event** | **CONFIRMED SAME-GENERATION · STRENGTHENED** | none |
| C-08 | Three-way match is advisory, not a control | `purchase_stock` | `qty_received` / `qty_invoiced` | `R1:purchase/models/purchase_order_line.py` | quantities inform, do not block | yes | — | — | 21,102 lines; **1,580 received-not-invoiced ฿29,029,467.66 tax-exclusive** (1,411 receipt-backed ฿27,490,865.80 + 169 operator-typed service lines ฿1,538,601.86); 183 invoiced-not-received ฿1,663,518.07 | **divergence persists and is unaccrued** | **CONFIRMED SAME-GENERATION · STRENGTHENED · now quantified** | none |
| C-09 | Order reset-to-draft has no server-side guard | `purchase` | `purchase.order.button_draft` | `R1:purchase/models/purchase_order.py:522-524` | bare `write({'state':'draft'})` | yes | — | — | 10 draft orders; 1,746 draft moves | not separately measured | **CONFIRMED SAME-GENERATION (source)** | reachability not measured in this deployment |
| C-10 | Period lock re-dates rather than refuses | `account` | `_get_lock_date_violations(hard=True)` | `R1:account/models/company.py:713-729` | silent re-date | yes | a lock date | **NONE — all five lock fields NULL on 4/4 companies** | — | — | **NOT REACHABLE — NO LOCK CONFIGURED** | the finding cannot be exercised here |
| C-11 | Correction deletes derived journal items | `stock_account` | `line_ids.filtered(display_type == 'cogs').unlink()` | `R1:stock_account/models/account_move.py:60, 70` | silent deletion on draft/cancel | yes | `real_time` to have cogs lines | closed | 1,746 draft moves | **no cogs lines exist to delete** | **NOT REACHABLE — POLICY-DEPENDENT** | — |
| C-12 | Cross-company auto-generation; guard cannot execute | `account_inter_company_rules` | `_find_company_from_partner` | `R1/R3:account_inter_company_rules/models/account_move.py:15` | auto-create counterpart doc | **not installed** | — | — | — | — | **NOT INSTALLED — NOT REACHABLE** | class A absence within the 361 installed modules |
| C-13 | Landed cost installed everywhere, exercised nowhere | `stock_landed_costs` | — | — | cost allocation to receipts | **not installed** | — | — | **no tables in the archive** | — | **NOT INSTALLED — NARROWED**: the estate-wide claim now has a counter-example | — |
| C-14 | Vendor advance defaults to an expense account | custom | `scgl_purchase_advance_payment` | `R4:…/wizard/purchase_advance.py:51, 178` | down-payment control inert | **not installed** | — | — | — | — | **NOT INSTALLED — NOT REACHABLE** | — |
| C-15 | Withholding: repeated full withholding, linear | custom (series-16 wizard) | — | series-16 custom copy | full base per partial payment | **four OCA/Ecosoft modules**, not `l10n_th` — a P01 attribution corrected this run (`ERR-P01-33`); the *multi*-rate module is **uninstalled** | rate records + `wt_tax_id` on the bill line | 40 rate records, 16 active | 1,183 supplier payments, **0** carrying `wt_tax_id`; 4 of 40,353 bill lines; 332 certificates, **bulk-loaded** under `__system__` | 358 items on generic `232000`, 330 raised in **bank** journals; **PND-keyed accounts `214001/2/3` hold zero in all four companies**; register vs ledger differ by ฿935.96 | **INSTALLED · CONFIGURED · certificate layer EXERCISED by migration · payment-time application NOT EXERCISED** | whether the series-16 finding concerns this same OCA family at an earlier version is **NOT DECIDABLE**; statutory questions → **P07** |
| C-16 | PND mapping conflict between two shipped copies | custom | — | — | form selection | — | — | — | — | — | **UNCHANGED — not a series-18 question** | → P07 |
| C-17 | Referential links are `ON DELETE SET NULL` | core schema | FK definitions | deployment | orphaning on delete | yes | — | — | 1,122 tables | not re-measured this run | **UNCHANGED — cross-version deployment invariant** | series-18 FK sweep not run |
| **N-01** | **Anglo-saxon accounting enabled in company 1 and inert** | `stock_account` | `_eligible_for_stock_account` | `R1:stock_account/models/account_move.py:278` | COGS lines at bill | yes | `anglo_saxon_accounting` + `real_time` | **co 1 true; policy closed** | 1,904 bills | **no anglo-saxon lines** | **NEW — CONFIGURED · NOT EXECUTED · POLICY-DEPENDENT** | — |
| **N-02** | **Custom company-scope guard executes but cannot refuse** | `scgl_product_category_company` 18.0.1.5.0 | `PurchaseOrder.button_confirm` + `@api.constrains` | version-matched source copy | refuse cross-company products | yes | category scope + allow flags | **`scgl_allow_purchase` true 126/126; scope set on 16/126** | 13,735 confirmed POs | **no refusal possible for 110/126** | **NEW — INSTALLED · REACHABLE · EXERCISED · non-restrictive by configuration** | whether it has ever refused: unobservable at rest |
| **N-03** | **Ten vendor bills whose liability is outside the payables subledger** | `account` | payment-term line account | — | AP control account | yes | partner payable | overridden per bill | **10 of 1,904**, ฿12,969.27 | **liabilities outside AP ageing** | **NEW — FACT VERIFIED**; intent **UNRESOLVED** | configuration owner needed |
| **N-04** | **Inventory reaches the GL only through migrated entries** | — | — | — | — | — | — | — | account 169: 2,940 items, **all** journal 45 `MIG26` | **no runtime valuation posting since 2026-08-18** | **NEW — FACT VERIFIED** | — |
| **N-05** | **The series-14 predecessor posted to an `STJ` stock journal; series 18 does not** | — | — | — | — | — | — | — | 15,434 of 15,522 refs carry `v14 … STJ/…` | — | **NEW — SUPPORTED INTERPRETATION** | migration specification / predecessor settings |

---

## 2. WHAT THE MATRIX SHOWS

| Outcome | Count | Findings |
|---|---|---|
| **CONFIRMED SAME-GENERATION** | 5 | C-01, C-02, C-07, C-08, C-09 |
| of which **STRENGTHENED** | 2 | C-07, C-08 |
| **CONTRADICTED for series 18** | **0** | ~~C-06~~ — the contradiction was **my own error**, corrected as `ERR-P01-30` |
| **CONFIGURED · NOT EXECUTED (policy)** | 3 | C-03, C-04, N-01 |
| **NOT REACHABLE — policy or configuration** | 3 | C-05, C-10, C-11 |
| **NOT INSTALLED** | 3 | C-12, C-13, C-14 |
| **DEPLOYMENT-DEPENDENT / different mechanism** | 1 | C-15 |
| **UNCHANGED — not a series-18 question** | 2 | C-16, C-17 |
| **NEW this run** | 5 | N-01 … N-05 |

**22 findings carried, 5 new.** Nine previously source-only findings now have a same-series
deployed check. **One is contradicted for this generation** (C-06) and one estate-wide claim is
narrowed by counter-example (C-13).

---

## 3. THE PATTERN IN THE "NOT REACHABLE" COLUMN

Six findings are unreachable in this deployment, and five of the six are unreachable **for the
same single reason**: the valuation policy is periodic, which closes the gate at C-02 and
everything downstream of it.

That is not six independent conclusions. It is **one configuration setting with six consequences**,
and it should be reported to the Boss as one decision, not six findings. Recorded as such in
`P01_P11_S18_DIRECT_VERIFICATION_SUPPLEMENT.md`.

---

## 4. WHAT THIS MATRIX DOES NOT DO

- It does not withdraw any finding measured in `D1`, `D2`, `D3` or `D4`. Every finding remains
  bound to the population in which it was measured. `NOT REACHABLE HERE` is a statement about
  **this deployment**, never about the finding.
- It does not claim any mechanism **executed**. Every "exercised" cell is an inference from records
  to execution and is labelled where it matters.
- It does not resolve `C-15`. The deployed withholding mechanism is **four OCA/Ecosoft modules**
  — not `l10n_th`, which supplies no withholding code at all (`ERR-P01-33`). Series-16 copies of
  **those same OCA modules** exist on this host, so whether P01's series-16 finding concerns an
  earlier version of this same family or a genuinely bespoke wizard is **NOT DECIDABLE** from this
  evidence base. **No transfer is made in either direction.** Statutory correctness is **P07's**.
  Full detail in `P01_S18_WHT_DEPLOYMENT_REALITY.md`.
