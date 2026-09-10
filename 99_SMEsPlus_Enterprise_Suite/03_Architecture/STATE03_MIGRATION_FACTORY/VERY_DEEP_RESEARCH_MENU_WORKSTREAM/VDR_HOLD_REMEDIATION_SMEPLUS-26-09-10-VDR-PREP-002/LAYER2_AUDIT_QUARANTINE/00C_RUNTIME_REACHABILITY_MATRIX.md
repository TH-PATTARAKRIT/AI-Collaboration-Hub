# 00C_RUNTIME_REACHABILITY_MATRIX.md
# Workstream C — Runtime Reachability Matrix (Inventory)

Session `[SMEPLUS-26-09-10-VDR-PREP-002]` · Owner: **LESA + Technical Evidence**
**LAYER 2 — AUDIT QUARANTINE.**

---

## 1. The blocker this closes

The prior Pilot carried `GAP-INV-09`: **no runtime evidence base was established**, so `reachability`
was `UNMEASURED` on all 5,074 Learning Items and *nothing* in the package was ranked by whether it can
actually fire. That was the single largest bound on the whole package.

**It is now partly closed, with real deployment evidence.**

## 2. Runtime evidence base — what was found and how

No database server was running and none was started. **Two deployment artefacts were read directly
from disk, without a server**, and both are Odoo-format database dumps:

| Ref | Artefact | Format | Read by | Rows recovered |
|-----|----------|--------|---------|----------------|
| **E** | a plain-SQL database dump, 60 MB | plain SQL, 848 table blocks | direct parse of the COPY blocks | 34,164 identity rows + 8 tables |
| **T** | a custom-format database dump, 62 MB, 1,395 table-data entries | PostgreSQL custom archive v1.16 | archive client, `--data-only`, to stdout | 196,890 identity rows + 13 tables |

**Both are series 19.** Their platform version rows read `19.0.1.3` — **the same generation as the
source root R1 that every Pilot finding was derived from.** This is the single most important property
of this evidence base: reachability is being measured on the generation the findings describe.

### Method note — an artefact that needed a newer client read as unreadable, not absent
Artefact **T** was initially reported by the installed client as *"unsupported version (1.16) in file
header"*. A second, newer client on the same host read it without difficulty. **A dump that needs a
newer client is unreadable, not absent** — and the first result would have been published as "no
runtime evidence available" for the second time in this programme.

### Method note — a truncating pipe produced a 0% result that was false
The first identity-table extraction returned **584 rows** and yielded **0 of 62 menus present** — a
clean, uniform, catastrophic false negative. The table actually holds **34,164** rows; the extraction
had been killed mid-stream by a pipe that closed early. The defect was caught by a coverage assertion
comparing rows returned against rows in the source block. **Recorded as `CORR-F-32`, and it is the
third time in this programme that a truncating pipe has produced a false negative.**

## 3. Deployment profile — five deployments, three generations

**Corrected after re-challenge.** The first version of this section reported **two** deployments and
stated that neither carried stock. The artefact census named **five** database identities; **all five
have now been examined**, and three of them are transacted.

| Ref | Generation | Modules installed | Domain modules (of 149) | Inventory menus (of 62) | Movements | On-hand rows |
|-----|-----------|------------------:|------------------------:|------------------------:|----------:|-------------:|
| `E` | 19.0.1.3 | 216 | 33 (22.1%) | **46 (74.2%)** | 0 | 0 |
| `T` | 19.0.1.3 | 486 | 69 (46.3%) | **52 (83.9%)** | 48 | 0 |
| **`B`** | **19.0.1.3** | 251 | 34 (22.8%) | **46 (74.2%)** | **14,441** | **3,642** |
| `U` | **18.0.1.3** | 361 | 25 | not enumerated | **51,081** | **2,462** |
| `S` | **16.0.1.3** | 190 | 13 | not enumerated | **103,949** | **27,196** |

**Menus absent despite their module being installed: 0, on all three series-19 deployments.**
**186 menu observations, 0 anomalies.** Independent re-challenge extended this test far beyond the 62
Inventory menus — to every menu declared by every installed module — reaching **1,557 menu and 345
action observations, still zero anomalies.**

**The newer copies change nothing structural.** Re-challenge opened the newer copies of `E` and `T`
that this session had not used: identical menu presence, identical suppression-parameter state, domain
module sets within one module. They do carry a small number of completed, valued movements.

## 4. Reachability roll-up — menus

| Class | Menus | Share |
|-------|------:|------:|
| `RUNTIME REACHABLE` — present on **both** deployments | **46** | 74.2% |
| `RUNTIME REACHABLE` — present on **one** of two | 6 | 9.7% |
| `OPTIONAL MODULE DEPENDENT` — installed on neither | 10 | 16.1% |
| `RUNTIME UNREACHABLE` with module installed | **0** | 0% |
| **Measured** | **62** | **100%** |

The 10 optional-dependent menus are the five country-localisation surfaces and dropshipping. They are
`SOURCE PRESENT / RUNTIME UNREACHABLE` on everything observed.

## 5. Reachability roll-up — scheduled jobs, and what actually ran

Of the 26 scheduled jobs in the domain module set, **11 are present on at least one deployment, all 11
are active, and all 11 carry a last-run timestamp — they have executed.**

| Job | E | T |
|-----|---|---|
| **procurement scheduler** | active, last ran 2026-03-31 | active, last ran 2026-06-14 |
| **inventory valuation closing** | active, last ran 2026-03-31 | active, last ran 2026-06-14 |
| master production schedule replenish | not installed | active, last ran 2026-06-13 |
| marketplace order / inventory / picking sync (5 jobs) | active, all ran 2026-03-18…03-31 | not installed |
| point-of-sale preparation-display cleanup | active, last ran 2026-03-31 | not installed |
| web availability e-mail | not installed | active, last ran 2026-06-14 |

## 6. The findings that move from LATENT to LIVE

### RR-F-01 — The write-by-read routine is **not suppressed** on ANY deployment (**CRITICAL — confirmed by re-challenge**)
The system parameter said to suppress the quantity-maintenance routine is **absent from the parameter
table on all four deployment copies examined**, including a **transacted** one. Re-challenge confirmed
the key is the correct one — it guards the routine at both call sites in source — and confirmed its
absence with a positive control on a parameter that *is* present.

**`HA-F-01` moves from `UNMEASURED` to `LIVE`**, on a deployment carrying 3,642 on-hand rows and
14,441 movements. It is not a theoretical source property.

### RR-F-02 — The procurement scheduler has actually executed on every deployment carrying it (**CRITICAL — confirmed**)
The job behind the *Run Scheduler* menu — the one that runs as superuser, creates downstream purchase
and manufacturing documents and commits in chunks — is **active and carries a real last-run timestamp
on all three series-19 deployments**, including the transacted one (last run 2026-08-03).
Re-challenge reproduced every timestamp to the second. `HA-F-01` row 4 is `LIVE`.

### RR-F-03 — The valuation-closing job is live, and it is the object of an open eligibility question
The inventory valuation closing job is active and has run on both. It is one of the 10 jobs the Pilot's
ownership filter **excluded** because it is declared on the company object rather than an Inventory
object — the question raised as `BOSS-DEC-12`. **It is live, it is inventory valuation, and the
mechanical rule put it outside the domain.** The eligibility question is not academic.

### RR-F-04 — CORRECTED — transactional reachability in the target generation is small-N, not zero
The first version of this finding said *"neither deployment has any on-hand quantity"* and concluded
that transactional reachability was unmeasurable. **Two of the deployments it was drawn from were
indeed empty. Three others were not, and one of those three is in the target generation.**

| Deployment | generation | on-hand rows | movements | completed movements |
|---|---|---:|---:|---:|
| `E`, `T` | 19 | 0 | 0 / 48 | 0 |
| **`B`** | **19** | **3,642** | **14,441** | **3,680** |
| `U` | 18 | 2,462 | 51,081 | not enumerated |
| `S` | 16 | 27,196 | 103,949 | 81,909 |

**`GAP-INV-09B` as published is withdrawn.** Transactional reachability in the target generation is
**measured on one deployment**, not unmeasurable. It remains **small-N** — one deployment, one
configuration (periodic valuation), one company set — and no application server was run, so no
controlled test transaction, security response or state-transition test exists. Recorded at that
weight as `GAP-INV-09C`.

### RR-F-05 / RR-F-06 — **WITHDRAWN AND REPLACED.** The per-movement valuation chain did **not** disappear in series 19 (**CRITICAL RETRACTION**)

> **This register published, as its most consequential finding and as the primary input to
> `BOSS-DEC-01`, that the series-18 valuation ledger "is not merely renamed — it is not being
> written", and that its replacement "carries no movement-level valuation at all".**
> **Both statements are false.** Independent re-challenge falsified them and the producer verified the
> falsification against a transacted target-generation deployment before accepting it.

**What is actually true.** Per-movement valuation exists in series 19. It was **relocated from a
separate append-only ledger table onto the movement row itself**:

| | series 16 / 18 | **series 19** |
|---|---|---|
| Where the value lives | a dedicated ledger table, one row per valuation event | **columns on the movement row** — value, remaining quantity, remaining value, accounting-entry reference |
| Ledger table present | yes | **no — correctly observed** |
| Per-movement value present | yes | **YES — this register said no** |

**Measured on the transacted series-19 deployment (14,441 movements, 3,680 completed):**

| | value |
|---|---|
| completed movements carrying a **value** | **3,680 — 100.0%** |
| completed movements carrying a **non-zero** value | 2,431 — 66.1% |
| movements carrying an **accounting-entry** reference | **0 — 0.0%** |

**Why the original claim was wrong, in two independent ways.**

1. **The wrong object was identified as the replacement.** The object examined records *"the history of
   manual update of a value"* — by its own source documentation. It is a price-change log, not the
   valuation record. **The header of the movement extract committed in this package already carried
   the value and accounting-reference columns, and it was not read.**
2. **The comparison had no state basis and no configuration control.** A movement is valued when it
   completes. The deployment the claim was measured on had **zero completed movements**. And the
   accounting-link half is confounded by configuration, not generation: the transacted series-19
   deployment runs **periodic** valuation on all 44 companies, under which **no movement creates an
   accounting entry in any generation**. The series-16 comparator's 77.2% reflects *that* database's
   real-time setting.

### RR-F-07 — what survives, stated at its true weight (**MATERIAL**, not CRITICAL)

The **structure** changed and that change is real and design-relevant:

- an **append-only ledger with its own row identity** became **mutable columns on the transaction row**;
- the value is a plain writable column with no change-tracking (prior package `OD-F-07`) — a concern
  the relocation **strengthens**, because there is no longer a separate immutable record;
- the accounting linkage is **not observable** on any deployment located here, because every located
  series-19 deployment runs periodic valuation. **Whether the movement → posting link is populated
  under real-time valuation in series 19 is UNMEASURED.**

`CRITICAL-GAP-01` is **re-stated at this weight**: not *"the chain is gone"* but *"the chain moved from
an append-only ledger to mutable transaction columns, and its accounting half is unmeasured in the
target generation."* **`BOSS-DEC-01` must not be decided on the withdrawn claim.** Recorded as
`GAP-INV-21`.

### RR-F-08 — the earlier "no transacted target-generation deployment" bound is also false
Two artefacts named in this package's own census, and not opened, are series-19 **and transacted** —
one with 3,642 on-hand rows and 14,441 movements. Newer copies of the two deployments that *were*
used also carry stock. **`GAP-INV-09B` as published is wrong**; transactional reachability in the
target generation is **small-N, not zero**.

## 7. Declared limits of this evidence base

| Limit | Status |
|-------|--------|
| **All five** located database identities examined | the census was still run **after** the first two were chosen, and cloud storage remains unswept — see §8 |
| No application server was run | no UI execution, no controlled test transaction, no security-response test |
| Transactional evidence is **small-N** — one target-generation deployment, one configuration | `GAP-INV-09C` |
| Element classes below the menu | field, view, button and behaviour reachability is **inferred from module installation**, not observed per element |
| The two structurally-measured deployments are series 19; the only transacted one is series 16 | **no deployment provides transactional reachability for the target generation** |

## 8. Artefact census — completed, and it corrects the choice of evidence

Two full-traversal censuses stalled on cloud-storage placeholder files. A third, **candidate-first**
census completed: enumerate files over 10 MB whose name matches a database-artefact pattern, then
**verify each by content signature**.

| | |
|---|---|
| Candidates enumerated | **236** |
| Verified database artefacts | **15** (2 of which are this session's own extraction output) |
| **Distinct database identities** | **5** |
| Roots swept | the primary volume, the second volume, and six home sub-trees |
| **Declared exclusion (evidence-affecting)** | cloud-storage trees — traversal stalls on placeholder files. **Not swept.** |

### The six database identities, and the choice that was wrong

| Identity | Newest artefact | Generation | Examined? |
|----------|-----------------|-----------|-----------|
| `E` | 2026-07-23 | 19.0.1.3 | **yes** — the older copy was used first; re-challenge opened the newer one |
| `T` | 2026-07-14 | 19.0.1.3 | **yes** — the older copy was used first; re-challenge opened the newer one |
| `S` | 2026-07-11 (the largest artefact on the host) | **16.0.1.3** | **yes** — examined after the census |
| `U` | 2026-08-30 | **18.0.1.3** | **yes** — examined after the census |
| `B` | 2026-08-03 | **19.0.1.3, transacted** | **yes** — examined after the census; it falsified two published claims |

**The count was published as 6. It is 5** — the sixth row of the original table was blank, and the
census's fifteen artefacts resolve to five database names once this session's own extraction output is
excluded. Corrected after re-challenge.

> **Both deployments first examined were chosen by convenience, and for both a newer copy existed
> that was not used.** The census was run *after* the choice, not before it. The programme's own rule
> — *rank the population before choosing* — was violated.
>
> **The cost was not hypothetical.** The three artefacts left unopened contained a transacted
> target-generation deployment, a transacted series-18 deployment, and newer copies carrying completed
> valued movements. **Two published claims were false because those artefacts were listed and not
> opened**, and both were caught by independent re-challenge rather than by the producer.

**Residual bound:** all five identities are now examined; **cloud storage remains unswept**, and the
ordering defect is historical fact. `GAP-INV-17` narrows but does not close.

## 9. What this evidence base still cannot measure

- **No application server was run.** No UI execution, no controlled test transaction, no security
  response, no state-transition test. Everything here is read from data at rest.
- **One configuration only.** Every located series-19 deployment runs **periodic** valuation, so the
  movement → accounting-entry link is **unobservable** in the target generation (`GAP-INV-21`).
- **Element-level observation covers 1.4% of the population**; the rest is module inference, and
  re-challenge produced a **counter-example** to that inference (`RR-F-09`).

### RR-F-09 — the module-installation inference is falsified at field level (**MATERIAL — found by re-challenge**)
This register argued that module installation is a sound proxy because **186 menu observations across
three deployments produced 0 anomalies** — extended by re-challenge to 1,557 menu and 345 action
observations, still 0.

**At field level the inference fails.** Re-challenge tested the population's 1,846 field items against
each deployment's own field registry — a table this session never extracted — and found **one field
whose module is installed and which is absent from the deployment**, on both the old and the new copy
of that database, with a positive control on a sibling field that is present.

**One counter-example is enough.** Class B is a **necessary condition, not a measurement**, and the
96.3% figure is an **upper bound**. The zero-anomaly evidence was real but its unit — the menu — was
too coarse to detect the failure. Recorded as `CORR-F-40`: *a proxy validated at one granularity is
not validated at a finer one.*

## 10. Cross-generation valuation evidence

The largest artefact on the host, never examined before this census, is a **heavily transacted**
Inventory deployment:

| | value |
|---|---|
| Stock movements | **103,949** |
| On-hand quantity rows | **27,196** |
| Generation | **16.0.1.3 — series 16, NOT the target generation** |
| Domain modules installed | 13 of 149 |

**This is the only transacted Inventory deployment located on this host, and it is three generations
behind the source that every Pilot finding was derived from.**

Two consequences, in opposite directions, both stated:

- **Favourable:** the domain *is* transacted somewhere in the estate. The Inventory function is real
  operational software here, not a demonstration install.
- **Unfavourable:** **transactional reachability for the target generation remains unmeasurable.**
  Measurements taken on this deployment describe series 16 and must not be read as series-19
  behaviour — the error this programme has made before.

### The three-generation valuation comparison — retained, with its interpretation withdrawn

| Generation | Movements | Ledger-table rows | Movement-linked | Accounting-linked |
|---|---:|---:|---:|---:|
| 16 (transacted) | 103,949 | **74,982** | **98.0%** | 77.2% |
| 18 (transacted) | 51,081 | **47,801** | **94.0%** | 0.0% |
| **19 (transacted)** | **14,441** | **table absent — value is on the movement row instead** | **100% of completed movements carry a value** | **0.0% — and the deployment runs periodic valuation** |

**The measurements are correct and were reproduced to the digit by re-challenge. The inference drawn
from them was wrong — see `RR-F-05 / RR-F-06`.** Two columns cannot be read as a trend: the
accounting-link column moves 77.2% → 0.0% between two *earlier* generations and is governed by a
configuration setting, not by generation. Recorded as `GAP-INV-20`.

Per completed movement rather than per movement, the series-16 ledger density is **0.92**, not 0.72 —
cancelled movements are never valued and belong in neither numerator nor denominator.

## 11. Matrix — menus

| Learning ID | Menu identity | Label | Module | Source present | Module installed (E / T) | Menu reachable (E / T) | Runtime entry point | Reachability class |
|---|---|---|---|:--:|:--:|:--:|---|---|
| LI-INV-MENU-0001 | `delivery_iot.iot_cached_printers_action` | Reset Linked Printers | `delivery_iot` | Y | n / Y | n / Y | client action | **RUNTIME REACHABLE (1 of 2 deployments)** |
| LI-INV-MENU-0002 | `delivery_iot.iot_cached_printers_section` | Reporting | `delivery_iot` | Y | n / Y | n / Y | container (no action) | **RUNTIME REACHABLE (1 of 2 deployments)** |
| LI-INV-MENU-0003 | `l10n_cl_edi_stock.menu_sii_chile` | Chilean SII | `l10n_cl_edi_stock` | Y | n / n | n / n | container (no action) | **OPTIONAL MODULE DEPENDENT — not installed anywhere observed** |
| LI-INV-MENU-0004 | `l10n_cl_edi_stock.menu_stock_l10n_cl_dte_caf` | Cafs | `l10n_cl_edi_stock` | Y | n / n | n / n | window action | **OPTIONAL MODULE DEPENDENT — not installed anywhere observed** |
| LI-INV-MENU-0005 | `l10n_mx_edi_stock.menu_stock_config_settings_mx` | Mexico | `l10n_mx_edi_stock` | Y | n / n | n / n | container (no action) | **OPTIONAL MODULE DEPENDENT — not installed anywhere observed** |
| LI-INV-MENU-0006 | `l10n_mx_edi_stock.menu_stock_mx_customs_document_type` | Custom Document Type | `l10n_mx_edi_stock` | Y | n / n | n / n | window action | **OPTIONAL MODULE DEPENDENT — not installed anywhere observed** |
| LI-INV-MENU-0007 | `l10n_mx_edi_stock.menu_stock_mx_customs_regime` | Customs Regime | `l10n_mx_edi_stock` | Y | n / n | n / n | window action | **OPTIONAL MODULE DEPENDENT — not installed anywhere observed** |
| LI-INV-MENU-0008 | `l10n_pe_edi_stock.menu_stock_config_settings_pe` | Peru | `l10n_pe_edi_stock` | Y | n / n | n / n | container (no action) | **OPTIONAL MODULE DEPENDENT — not installed anywhere observed** |
| LI-INV-MENU-0009 | `l10n_pe_edi_stock.menu_stock_pe_vehicles` | Vehicles | `l10n_pe_edi_stock` | Y | n / n | n / n | window action | **OPTIONAL MODULE DEPENDENT — not installed anywhere observed** |
| LI-INV-MENU-0010 | `l10n_tr_nilvera_edispatch.menu_l10n_tr_nilvera` | GİB e-Dispatch | `l10n_tr_nilvera_edispatch` | Y | n / n | n / n | container (no action) | **OPTIONAL MODULE DEPENDENT — not installed anywhere observed** |
| LI-INV-MENU-0011 | `l10n_tr_nilvera_edispatch.menu_l10n_tr_nilvera_trailer_plate` | GİB Plate Numbers | `l10n_tr_nilvera_edispatch` | Y | n / n | n / n | window action | **OPTIONAL MODULE DEPENDENT — not installed anywhere observed** |
| LI-INV-MENU-0012 | `mrp.mrp_operation_picking` | Manufacturings | `mrp` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0013 | `mrp_mps.stock_mrp_mps_report_menu` | Master Production Schedule | `mrp_mps` | Y | n / Y | n / Y | client action | **RUNTIME REACHABLE (1 of 2 deployments)** |
| LI-INV-MENU-0014 | `stock.in_picking` | Receipts | `stock` | Y | Y / Y | Y / Y | server action -> code -> window action (3 hops) | **RUNTIME REACHABLE** |
| LI-INV-MENU-0015 | `stock.int_picking` | Internal | `stock` | Y | Y / Y | Y / Y | server action -> code -> window action (3 hops) | **RUNTIME REACHABLE** |
| LI-INV-MENU-0016 | `stock.menu_action_inventory_tree` | Physical Inventory | `stock` | Y | Y / Y | Y / Y | server action -> code | **RUNTIME REACHABLE** |
| LI-INV-MENU-0017 | `stock.menu_action_location_form` | (from action) | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0018 | `stock.menu_action_production_lot_form` | (from action) | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0019 | `stock.menu_action_rules_form` | (from action) | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0020 | `stock.menu_action_warehouse_form` | (from action) | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0021 | `stock.menu_attribute_action` | (from action) | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0022 | `stock.menu_delivery` | Delivery | `stock` | Y | Y / Y | Y / Y | container (no action) | **RUNTIME REACHABLE** |
| LI-INV-MENU-0023 | `stock.menu_package` | Packages | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0024 | `stock.menu_packaging_types` | Package Types | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0025 | `stock.menu_pickingtype` | Operations Types | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0026 | `stock.menu_procurement_compute` | (from action) | `stock` | Y | Y / Y | Y / Y | action record absent from source | **RUNTIME REACHABLE** |
| LI-INV-MENU-0027 | `stock.menu_product_category_config_stock` | (from action) | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0028 | `stock.menu_product_in_config_stock` | Products | `stock` | Y | Y / Y | Y / Y | container (no action) | **RUNTIME REACHABLE** |
| LI-INV-MENU-0029 | `stock.menu_product_stock` | Stock | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0030 | `stock.menu_product_variant_config_stock` | Products | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0031 | `stock.menu_putaway` | Putaway Rules | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0032 | `stock.menu_reordering_rules_replenish` | Replenishment | `stock` | Y | Y / Y | Y / Y | server action -> code | **RUNTIME REACHABLE** |
| LI-INV-MENU-0033 | `stock.menu_routes_config` | Routes | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0034 | `stock.menu_stock_adjustments` | Adjustments | `stock` | Y | Y / Y | Y / Y | container (no action) | **RUNTIME REACHABLE** |
| LI-INV-MENU-0035 | `stock.menu_stock_config_settings` | Configuration | `stock` | Y | Y / Y | Y / Y | container (no action) | **RUNTIME REACHABLE** |
| LI-INV-MENU-0036 | `stock.menu_stock_general_settings` | Settings | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0037 | `stock.menu_stock_inventory_control` | Products | `stock` | Y | Y / Y | Y / Y | container (no action) | **RUNTIME REACHABLE** |
| LI-INV-MENU-0038 | `stock.menu_stock_procurement` | Procurement | `stock` | Y | Y / Y | Y / Y | container (no action) | **RUNTIME REACHABLE** |
| LI-INV-MENU-0039 | `stock.menu_stock_references` | (from action) | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0040 | `stock.menu_stock_root` | Inventory | `stock` | Y | Y / Y | Y / Y | container (no action) | **RUNTIME REACHABLE** |
| LI-INV-MENU-0041 | `stock.menu_stock_scrap` | Scrap | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0042 | `stock.menu_stock_transfers` | Transfers | `stock` | Y | Y / Y | Y / Y | container (no action) | **RUNTIME REACHABLE** |
| LI-INV-MENU-0043 | `stock.menu_stock_uom_form_action` | Units & Packagings | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0044 | `stock.menu_stock_warehouse_mgmt` | Operations | `stock` | Y | Y / Y | Y / Y | container (no action) | **RUNTIME REACHABLE** |
| LI-INV-MENU-0045 | `stock.menu_storage_categoty_config` | Storage Categories | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0046 | `stock.menu_valuation` | Locations | `stock` | Y | Y / Y | Y / Y | server action -> code | **RUNTIME REACHABLE** |
| LI-INV-MENU-0047 | `stock.menu_warehouse_config` | Warehouse Management | `stock` | Y | Y / Y | Y / Y | container (no action) | **RUNTIME REACHABLE** |
| LI-INV-MENU-0048 | `stock.menu_warehouse_report` | Reporting | `stock` | Y | Y / Y | Y / Y | container (no action) | **RUNTIME REACHABLE** |
| LI-INV-MENU-0049 | `stock.menu_wms_barcode_nomenclature_all` | (from action) | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0050 | `stock.out_picking` | Deliveries | `stock` | Y | Y / Y | Y / Y | server action -> code -> window action (3 hops) | **RUNTIME REACHABLE** |
| LI-INV-MENU-0051 | `stock.product_product_menu` | Product Variants | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0052 | `stock.stock_move_line_menu` | (from action) | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0053 | `stock.stock_move_menu` | Moves Analysis | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0054 | `stock.stock_picking_type_menu` | Overview | `stock` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0055 | `stock_delivery.menu_action_delivery_carrier_form` | (from action) | `stock_delivery` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0056 | `stock_delivery.menu_delivery_zip_prefix` | (from action) | `stock_delivery` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0057 | `stock_dropshipping.dropship_picking` | Dropships | `stock_dropshipping` | Y | n / n | n / n | window action | **OPTIONAL MODULE DEPENDENT — not installed anywhere observed** |
| LI-INV-MENU-0058 | `stock_enterprise.stock_dashboard_menuitem` | Performance | `stock_enterprise` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0059 | `stock_landed_costs.menu_stock_landed_cost` | Landed Costs | `stock_landed_costs` | Y | Y / Y | Y / Y | window action | **RUNTIME REACHABLE** |
| LI-INV-MENU-0060 | `stock_picking_batch.menu_stock_jobs` | Jobs | `stock_picking_batch` | Y | n / Y | n / Y | container (no action) | **RUNTIME REACHABLE (1 of 2 deployments)** |
| LI-INV-MENU-0061 | `stock_picking_batch.stock_picking_batch_menu` | (from action) | `stock_picking_batch` | Y | n / Y | n / Y | window action | **RUNTIME REACHABLE (1 of 2 deployments)** |
| LI-INV-MENU-0062 | `stock_picking_batch.stock_picking_wave_menu` | (from action) | `stock_picking_batch` | Y | n / Y | n / Y | window action | **RUNTIME REACHABLE (1 of 2 deployments)** |