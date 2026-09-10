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
| Menu-open side effects | **4 of a population of 9** | census, see `HA-F-01`; corrected twice, see `CORR-F-22`/`CORR-F-23` |

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

### HA-F-01 — Opening a menu mutates data — 4 menus of a population of 9 (**CRITICAL**)

> **Corrected after independent challenge.** This finding was published as *"2 located, population
> unknown"*, then corrected by the producer to *"3 of 8"*, and is corrected again here to **4 of 9**.
> Both earlier figures were wrong, in the same direction, for two different instrument reasons
> (`CORR-F-22`, `CORR-F-23`). The number moved every time it was checked by a different party.

**Population (declared):** every menu **in the whole root** whose action is a server action bound to
an object this domain owns, **plus** menus bound to a server action that the platform generates from a
scheduled-job record rather than declaring in XML. **9 menus.** The ninth was invisible to the
producer's action census because its action record does not exist in source — it is materialised at
install time from a scheduled job. Found by challenge (`CORR-F-23`).

| Menu | Object | What opening it does |
|------|--------|----------------------|
| **Physical counting** | on-hand quantity | runs a maintenance routine over quantity records |
| **Location / quantity view** | on-hand quantity | the same maintenance routine |
| **Replenishment** | replenishment rule | **creates and deletes replenishment-policy records.** Its own documentation states it *creates manual reorder rules for missing products in each warehouse* and *removes rules that have been replenished* |
| **Run scheduler** | replenishment rule | **runs the full procurement scheduler as superuser**: confirms replenishment, creates downstream purchase and manufacturing orders, reserves stock, commits in chunks, and then runs the same quantity maintenance routine |

Four properties make this a first-order control finding:

1. **It is a write performed by a read.** No user action names the mutation, there is no confirmation,
   and there is no audit entry for it.
2. **Two of the four write business policy, not derived rows.** A replenishment rule is a policy
   record. The fourth creates procurement documents in other domains.
3. **The scheduler menu runs with elevated privilege and commits mid-transaction.** Its own source
   comment states the functions are run as superuser to avoid inter-company and access-rights issues —
   i.e. the privilege escalation is deliberate and documented, and a menu click invokes it.
4. **The maintenance routine operates outside the ORM.** See `HA-F-09`.

**Disposition for SMEsPlus: `MUST NOT INHERIT`.** A read must not write. If a maintenance routine is
required it must be an explicitly scheduled, audited job. `BOSS-DEC-08` remains **open and undecided**;
the sentence above is this register's **candidate position**, not a decision.

### HA-F-09 — The maintenance routine bypasses the ORM entirely (**CRITICAL**) — *found by challenge*
The routine invoked by `HA-F-01`'s first two menus is composed of a merge step, a reservation-cleaning
step and a zero-row removal step. The merge step issues a raw `UPDATE` followed by a raw `DELETE`
against the quantity table, and the removal step issues a raw `SELECT` **with no company predicate**
and then deletes with superuser privilege.

Because these are executed as SQL rather than through the object layer:

- **no access-control check applies**;
- **no row-level rule applies**, so the statement is **not company-scoped**;
- **no deletion guard and no change-tracking can fire** — there is no hook for them to fire on.

The earlier text said there is *"no audit entry"* for the mutation. That understated it:
**no audit mechanism could fire**, because the layer that would fire it is not involved.

Both methods are model-level and are invoked from the menu path on an empty record set, so the
narrowing that would restrict them to selected rows does not apply. **The statement operates on the
whole table, across every company.**

### HA-F-10 — The suppression parameter covers 2 of 5 call sites (**CRITICAL**) — *found by challenge*
The routine has **five** non-test call sites. The system parameter guards **two** of them — the two
menu paths. The other three run it unconditionally:

| Call site | Guarded? |
|-----------|----------|
| physical-counting menu path | yes |
| location/quantity menu path | yes |
| **procurement scheduler** | **no** |
| **package unpacking** | **no** |
| **a statutory tax-report builder (one country localisation)** | **no** |

The third is the most serious: a **statutory report that produces a filed return mutates and deletes
quantity rows while building it**, with no guard.

**Setting the parameter therefore creates a false assurance.** An administrator who sets it to stop
reads from writing has stopped two of five, and the register previously described it as *the* switch.

### HA-F-11 — The parameter is not in the toggle population at all (**CRITICAL for method**) — *found by challenge*
`HA-F-01` and Register 03 `FT-F-04` both classified this parameter as a **class C system-parameter
toggle**. It is not. It has **no configuration-settings field**, **no data record**, and **no
declaration of any kind** anywhere in the root; it exists only as a string read at runtime. It is not
among the 7 class-C rows and it is not in the 237-row toggle population.

**It is a sixth mechanism the `FT-F-01` taxonomy does not have: an undeclared runtime parameter.**
The taxonomy was incomplete by exactly the case this register calls its most severe control finding.
Recorded as framework correction `CORR-F-24`; `FT-F-01` corrected in Register 03.

### HA-F-02 — CORRECTED — the counting menu opens pre-filtered by role, as a visible facet
The counting menu's code sets a default filter *"my counts"* when the user holds the operational
inventory group **but not** the managerial one. Two users open one menu and see two different record
sets.

> **This finding was published as "no visible filter difference" and "no visible indication".
> That was wrong**, and independent challenge falsified it. The mechanism is the platform's
> *default search facet*: it renders in the search bar as a **labelled, removable chip**. The records
> remain readable and the filter is one click from being cleared.

**Corrected statement:** for a non-manager the counting screen opens **pre-filtered to the counts
assigned to that user**, shown as a removable facet. It is a **default projection, not a silent one.**

The design consequence survives the correction and the control consequence does not:
- **Survives:** two users of an audit-relevant screen see different populations by default, and
  nothing in the menu tells them the projection depends on their role. Anyone reading a count total
  off this screen without clearing the facet reads a partial figure.
- **Does not survive:** this is not concealment and not an access-control effect.

`CRITICAL-GAP-03` is **re-graded from CRITICAL to MATERIAL**, because its severity rested entirely on
the invisibility clause that has now been disproved.

### HA-F-03 — A menu's list may be editable or read-only depending on runtime role state
The location/quantity menu resolves to a code path that chooses between an editable and a read-only
list according to whether the user is in "inventory mode" **and** holds the managerial group — and
"inventory mode" is itself set for any holder of the operational group. **Whether a screen is editable
is not a property of the screen.**

Any Figma or Functional-Design artefact specifying one editability state for this screen would be
specifying one of at least two real behaviours.

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
59 access rows that grant deletion (Register 07 `SS-F-04`). **Permanence is the exception, and where
it exists it is written in code, not declared.**

Two of the 15 guards were read in full (Register 04 `FN-F-04`): each refuses deletion of a completed
document, **overriding an access grant that says deletion is permitted.** The other 13 have not been
read. **A permission model derived from access grants alone overstates what can actually be deleted,
by an amount this Pilot has not measured** — a floor of 2 objects, an unknown ceiling.

### HA-F-07 — Scheduled-job population grows 30% between generations
R2 (series-18): 19–20 jobs across two independent comparators. R1 (series-19): 26.
The growth is concentrated in marketplace-integration jobs. **A background-behaviour inventory built on
series-18 understates the target generation by roughly a third.**

### HA-F-08 — CORRECTED — no module ships automation rules as data, and the zero carries no information
A search for platform automation-rule records returns **0** across **all 1,433 modules** of the root,
not merely the 149-module domain set.

> **The register previously presented this as a re-tested zero and treated it as a domain property.
> Independent challenge established that it is neither.** The re-test re-ran the same *class* of query,
> which is not a second form; and **no positive control is available anywhere in the root**, because
> automation rules are records users create at run time — no module ships any. **A source census of
> this object can only ever return zero.**

**Corrected statement, with its scope:** *no module in the root ships automation rules as declarative
data.* That is a **platform** property, not a property of the Inventory domain. Under `GAP-INV-09`
(no runtime evidence) this census **cannot distinguish** "the domain has none" from "a deployment has
fifty".

**The consequence clause survives on other evidence.** The claim that tenant administrators cannot
see, audit or disable the domain's automated behaviour rests on the other four mechanisms —
26 scheduled jobs, 168 stored computed values, 141 persistence interceptions and 15 deletion guards,
all of which are code — and does not need this zero. `BOSS-DEC-09` stands.

**Method lesson recorded as `CORR-F-25`: a zero re-test is only a control if the second form can
distinguish the two hypotheses.** Re-running a query of the same class against the same evidence base
is repetition, not corroboration.

---

## 4. Coverage state

| Item | Population | Verified (`S4`) | State |
|------|-----------:|----------------:|-------|
| Scheduled jobs | 26 | 2 (the two menu-side-effect routines) | 7.7% |
| Stored computed values | 168 | 0 | 0% |
| Persistence interceptions | 141 | 0 | 0% |
| Deletion guards | 15 | 0 | 0% |
| Menu-open side effects | **9** (declared population) | 9 resolved, 4 mutate | **100% of the declared population** |
| Non-menu write-by-read entry points | **floor of 3** — product form, lot form, relocate wizard | 0 | **declared gap `GAP-INV-14`** |

`GAP-INV-08` is **CLOSED**: the population is no longer a floor, it is a census over a declared
population — every menu in the whole root bound to a server action on an owned object.

**The residual bounds, stated rather than implied:**

1. The trace follows **2 hops** and detects writers by their call form. A writer reached at hop 3 or
   later, or through a dynamically-named call, would not be seen.
2. **The unit is the menu.** Independent challenge identified **three further entry points to the same
   mutating routine that are not menus** — a control on the product form, a control on the lot form,
   and a relocation wizard. **A blind spot declared in the unit *menu* does not cover them.**
   Recorded as `GAP-INV-14`; the write-by-read surface is a floor of **4 menus plus 3 non-menu
   entry points**, and no census of the non-menu unit has been run.

**Declaring a blind spot in the wrong unit is the same defect as not declaring it.**
