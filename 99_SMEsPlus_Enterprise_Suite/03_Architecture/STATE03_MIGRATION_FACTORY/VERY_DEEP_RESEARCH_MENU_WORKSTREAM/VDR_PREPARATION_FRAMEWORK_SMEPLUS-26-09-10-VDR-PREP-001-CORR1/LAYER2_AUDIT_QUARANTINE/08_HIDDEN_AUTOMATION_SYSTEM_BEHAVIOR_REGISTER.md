# 08_HIDDEN_AUTOMATION_SYSTEM_BEHAVIOR_REGISTER.md
# Register 08 — Hidden Automation & System Behaviour (Inventory Pilot)

Session `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]` · **LAYER 2 — AUDIT QUARANTINE** · Generation: **R1 (series-19)**

---

## 1. What "hidden" means here

Behaviour that changes data or changes what a user sees, **without a user action that names it**.
Four mechanisms were enumerated:

| Mechanism | Population | Instrument |
|-----------|-----------:|-----------|
| Scheduled jobs | 26 | XML record census, second-shape validated at 26 = 26 |
| Stored computed values | 168 | AST field census |
| Persistence interceptions (create / write / delete / copy) | 141 | AST method census |
| Deletion guards | 15 | AST decorator census |
| Menu-open side effects | **2 located** | targeted source resolution, see §3 |

---

## 2. Scheduled jobs

| Learning ID | Scheduled job | Bound object | Interval | Declared active | Module | Evidence |
|---|---|---|---|---|---|---|
| LI-INV-AUTOMATION-0001 | Starshipit: Fetch Pending Shipping Prices | stock.picking | 1/hours | True | delivery_starshipit | delivery_starshipit/data/ir_cron_data.xml |
| LI-INV-AUTOMATION-0002 | BR EDI: Update status of marked POS orders | pos.order | 1/days | (default: active) | l10n_br_edi_pos | l10n_br_edi_pos/data/ir_cron.xml |
| LI-INV-AUTOMATION-0003 | Send delivery guides to SRI | stock.picking | 1/days | True | l10n_ec_edi_stock | l10n_ec_edi_stock/data/cron_data.xml |
| LI-INV-AUTOMATION-0004 | Generate Annual Sales Closing | account.sale.closing | 12/months | (default: active) | l10n_fr_pos_cert | l10n_fr_pos_cert/data/account_sale_closure_cron.xml |
| LI-INV-AUTOMATION-0005 | Generate Daily Sales Closing | account.sale.closing | 1/days | (default: active) | l10n_fr_pos_cert | l10n_fr_pos_cert/data/account_sale_closure_cron.xml |
| LI-INV-AUTOMATION-0006 | Generate Monthly Sales Closing | account.sale.closing | 1/months | (default: active) | l10n_fr_pos_cert | l10n_fr_pos_cert/data/account_sale_closure_cron.xml |
| LI-INV-AUTOMATION-0007 | KE eTIMS: Receive Customs Imports from the OSCU | l10n_ke_edi.customs.import | 1/days | (default: active) | l10n_ke_edi_oscu_stock | l10n_ke_edi_oscu_stock/data/ir_cron_data.xml |
| LI-INV-AUTOMATION-0008 | KE eTIMS: Send Stock Operations | stock.move | 1/days | (default: active) | l10n_ke_edi_oscu_stock | l10n_ke_edi_oscu_stock/data/ir_cron_data.xml |
| LI-INV-AUTOMATION-0009 | UY: Update DGI State - Pickings | stock.picking | 1/days | (default: active) | l10n_uy_edi_stock | l10n_uy_edi_stock/data/ir_cron.xml |
| LI-INV-AUTOMATION-0010 | MPS: replenish automated schedules | mrp.production.schedule | 1/days | (default: active) | mrp_mps | mrp_mps/data/ir_cron_data.xml |
| LI-INV-AUTOMATION-0011 | delete_preparation_order | pos.prep.order | 1/days | True | pos_enterprise | pos_enterprise/data/preparation_display_cron.xml |
| LI-INV-AUTOMATION-0012 | POS Pricer: tags update synchronization | pricer.store | 12/hours | True | pos_pricer | pos_pricer/data/pricer_ir_cron.xml |
| LI-INV-AUTOMATION-0013 | UrbanPiper: Notify future delivery orders | pos.order | 5/minutes | (default: active) | pos_urban_piper_enhancements | pos_urban_piper_enhancements/data/ir_cron.xml |
| LI-INV-AUTOMATION-0014 | Amazon: sync feeds | amazon.account | 9999/months | (default: active) | sale_amazon | sale_amazon/data/amazon_cron.xml |
| LI-INV-AUTOMATION-0015 | Amazon: sync available inventory | amazon.account | 30/minutes | (default: active) | sale_amazon | sale_amazon/data/amazon_cron.xml |
| LI-INV-AUTOMATION-0016 | Amazon: sync orders | amazon.account | 60/minutes | (default: active) | sale_amazon | sale_amazon/data/amazon_cron.xml |
| LI-INV-AUTOMATION-0017 | Amazon: sync delivery orders | stock.picking | 30/minutes | (default: active) | sale_amazon | sale_amazon/data/amazon_cron.xml |
| LI-INV-AUTOMATION-0018 | Lazada: sync inventory | lazada.shop | 4/hours | (default: active) | sale_lazada | sale_lazada/data/ir_cron.xml |
| LI-INV-AUTOMATION-0019 | Lazada: sync orders | lazada.shop | 60/minutes | (default: active) | sale_lazada | sale_lazada/data/ir_cron.xml |
| LI-INV-AUTOMATION-0020 | Shopee: sync inventory | shopee.shop | 30/minutes | (default: active) | sale_shopee | sale_shopee/data/shopee_cron.xml |
| LI-INV-AUTOMATION-0021 | Shopee: sync orders | shopee.shop | 60/minutes | (default: active) | sale_shopee | sale_shopee/data/shopee_cron.xml |
| LI-INV-AUTOMATION-0022 | Shopee: sync shipping labels | stock.picking | 30/minutes | (default: active) | sale_shopee | sale_shopee/data/shopee_cron.xml |
| LI-INV-AUTOMATION-0023 | Shopee: retry sync shipping labels | stock.picking | 9999/months | (default: active) | sale_shopee | sale_shopee/data/shopee_cron.xml |
| LI-INV-AUTOMATION-0024 | Procurement: run scheduler | stock.rule | 1/days | True | stock | stock/data/stock_sequence_data.xml |
| LI-INV-AUTOMATION-0025 | Stock Account: Inventory Valuation Closing | res.company | 1/days | True | stock_account | stock_account/data/stock_account_data.xml |
| LI-INV-AUTOMATION-0026 | Product: send email regarding products availability | product.product | 1/hours | (default: active) | website_sale_stock | website_sale_stock/data/ir_cron_data.xml |
**Reading rule:** "declared active" reports the value of the activation attribute **as declared in the
record**. Where the attribute is absent the record does not state it and the platform default applies.
`(default: active)` therefore means *not declared*, **not** *proven active*. This distinction is
recorded because reading an absent attribute as "inactive" would invert the finding.

---

## 3. Findings

### HA-F-01 — Opening a menu mutates data (**CRITICAL**)
The **physical counting** menu is bound to a server action which calls a method that, before returning
any screen, **executes a maintenance routine over the on-hand quantity records**. The same routine runs
when the **location / quantity** menu is opened.

Two properties make this a first-order control finding:

1. **It is a write performed by a read.** A user who opens a report menu changes stored data. There is
   no user action that names the mutation, no confirmation and no audit entry for it.
2. **It is suppressible by an invisible switch.** The routine is skipped when a **system parameter** is
   set. That parameter appears on **no configuration screen** — it is class C in Register 03 and is
   settable only through the technical parameter table.

**Disposition for SMEsPlus: `MUST NOT INHERIT`.** A read must not write. If a maintenance routine is
required it must be an explicitly scheduled, audited job. Raised as `BOSS-DEC-08`.

### HA-F-02 — The same menu shows a different population depending on the user's role (**CRITICAL**)
The counting menu's code sets a default filter *"only my counts"* when the user holds the operational
inventory group **but not** the managerial one. **Two users, one menu, two different record sets, no
visible filter difference.**

This is not access control — the records are readable — it is a **silent default projection**. For an
audit-relevant function (physical counting) a projection that changes with role and is not surfaced to
the user is a control weakness. Raised as `CRITICAL-GAP-03`.

### HA-F-03 — A menu's list may be editable or read-only depending on runtime role state
The location/quantity menu resolves to a code path that chooses list editability from whether the user
is in "inventory mode". **Whether a screen is editable is not a property of the screen.** Any Figma or
Functional-Design artefact that specifies one editability state for this screen would be specifying
one of at least two real behaviours.

### HA-F-04 — 168 stored computed values are cached derivations (**CRITICAL**)
Carried from Register 05 `OD-F-03`. Each is a value that reports read, that can disagree with its
inputs, and whose refresh is governed by a dependency declaration rather than by a business event.
**In a quantity- and valuation-bearing domain this is the largest silent-divergence surface measured.**

### HA-F-05 — Persistence is intercepted in 141 places
Carried from Register 04 `FN-F-02`. Every one is a place where "save" does something other than save.
**Classification of these 141 into business rule vs plumbing is a prerequisite to Functional Design**,
because the first class must be re-expressed in SMEsPlus and the second must not.

### HA-F-06 — 15 deletion guards define what cannot be deleted, and they are the only such statement
There is no declarative immutability anywhere in the domain — 32 change-tracked fields
(Register 05 `OD-F-04`) and 15 deletion guards are the entire enforced-permanence surface, against
59 access rows that grant deletion (Register 07 `SS-F-04`). **Permanence is the exception.**

### HA-F-07 — Scheduled-job population grows 30% between generations
R2 (series-18): 19–20 jobs across two independent comparators. R1 (series-19): 26.
The growth is concentrated in marketplace-integration jobs. **A background-behaviour inventory built on
series-18 understates the target generation by roughly a third.**

### HA-F-08 — No declarative automation-rule records exist in this domain, and the zero has been re-tested
A search for platform automation-rule records across all 149 modules returns **0**, re-tested in a
second form over the whole module set. **Scope: R1, the 149-module Inventory set, declarative records
only.** It does **not** mean the domain has no automation — §1 counts 350 automated behaviours by other
mechanisms. It means **none of them is declared as data; they are all code.**

**Consequence:** a tenant administrator cannot see, audit or disable any of them. For a SaaS product
this is a design decision that must be taken deliberately. Raised as `BOSS-DEC-09`.

---

## 4. Coverage state

| Item | Population | Verified (`S4`) | State |
|------|-----------:|----------------:|-------|
| Scheduled jobs | 26 | 2 (the two menu-side-effect routines) | 7.7% |
| Stored computed values | 168 | 0 | 0% |
| Persistence interceptions | 141 | 0 | 0% |
| Deletion guards | 15 | 0 | 0% |
| Menu-open side effects | 2 located | 2 | **the search was targeted, not exhaustive — the true population is unmeasured** |

**The last row is the register's own declared blind spot.** Two side effects were found by resolving
seven server-action menus. **No systematic search for menu-open side effects across all 200 actions has
been performed**, so the population is a **floor of 2**, not a census. Recorded as `GAP-INV-08` with its
size explicitly unknown rather than implied to be 2.
