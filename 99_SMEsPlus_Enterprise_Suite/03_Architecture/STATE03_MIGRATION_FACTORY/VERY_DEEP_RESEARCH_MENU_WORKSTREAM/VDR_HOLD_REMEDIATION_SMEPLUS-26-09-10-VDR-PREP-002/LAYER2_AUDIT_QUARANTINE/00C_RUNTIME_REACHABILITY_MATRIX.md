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

## 3. Deployment profile

| | **E** | **T** |
|---|---|---|
| Platform generation | **19.0.1.3** | **19.0.1.3** |
| Modules known / installed | 1,494 / **216** | 1,548 / **486** |
| Domain modules installed (of 149) | **33 (22.1%)** | **69 (46.3%)** |
| Inventory menus present (of 62) | **46 (74.2%)** | **52 (83.9%)** |
| Menus absent **despite** their module being installed | **0** | **0** |
| Scheduled jobs total / active | 56 / 50 | 76 / 66 |
| On-hand quantity rows | **0** | **0** |
| Stock movement rows | 0 | 48 |

**The zero-anomaly result is the strongest single line in this table.** Every absent Inventory menu on
both deployments is absent **because its module is not installed** — not one is missing for an
unexplained reason. Menu presence is fully explained by module installation.

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

### RR-F-01 — The write-by-read routine is **not suppressed** on either deployment (**CRITICAL**)
The system parameter said to suppress the quantity-maintenance routine is **absent from the parameter
table on both deployments**. The routine therefore runs on every open of the physical-counting menu
and the location/quantity menu, on both.

**`HA-F-01` moves from `UNMEASURED` to `LIVE`.** It is not a theoretical source property.

### RR-F-02 — The procurement scheduler has actually executed on both deployments (**CRITICAL**)
The job behind the *Run Scheduler* menu — the one that runs as superuser, creates downstream purchase
and manufacturing documents and commits in chunks — is **active and carries a real last-run timestamp
on both deployments**. `HA-F-01` row 4 is `LIVE`.

### RR-F-03 — The valuation-closing job is live, and it is the object of an open eligibility question
The inventory valuation closing job is active and has run on both. It is one of the 10 jobs the Pilot's
ownership filter **excluded** because it is declared on the company object rather than an Inventory
object — the question raised as `BOSS-DEC-12`. **It is live, it is inventory valuation, and the
mechanical rule put it outside the domain.** The eligibility question is not academic.

### RR-F-04 — Neither deployment has any on-hand quantity, and one has no movements at all
On-hand rows: **0 and 0**. Movement rows: 0 and 48. **The Inventory domain is installed and configured
on both deployments and effectively never transacted on either.**

This bounds everything: **structural reachability is measured; transactional reachability is not.**
Whether a movement-time behaviour fires correctly cannot be established from these artefacts, and no
amount of further reading of them will change that. Recorded as `GAP-INV-09B`.

### RR-F-05 — The series-19 valuation object exists, is heavily populated, and holds no movement values (**CRITICAL**)
On deployment **T**, the object that replaced the series-18 valuation ledger holds **85,832 rows**.
Every row is a **product price change**. Its movement reference is null on **all 85,832**, and its
lot reference is null on all 85,832.

**The series-18 ledger recorded a value per stock movement. Its series-19 replacement, as actually
populated on a real deployment, records product price changes and carries no movement-level valuation
at all.** The table for the series-18 object **does not exist** in this database.

This is runtime confirmation of `OD-F-05` and it makes `CRITICAL-GAP-01` materially stronger:
the per-movement valuation history the prior programme's COGS work relied on **is not merely renamed —
it is not being written**. Direct input to `BOSS-DEC-01`.

## 7. Declared limits of this evidence base

| Limit | Status |
|-------|--------|
| Three deployments examined of **six** database identities located | census completed **after** the choice was made; 3 identities and all cloud storage remain unexamined — see §8 |
| No application server was run | no UI execution, no controlled test transaction, no security-response test |
| No on-hand quantity on either deployment | transactional reachability **UNMEASURED** (`GAP-INV-09B`) |
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
| **Distinct database identities** | **6** |
| Roots swept | the primary volume, the second volume, and six home sub-trees |
| **Declared exclusion (evidence-affecting)** | cloud-storage trees — traversal stalls on placeholder files. **Not swept.** |

### The six database identities, and the choice that was wrong

| Identity | Newest artefact | Generation | Examined? |
|----------|-----------------|-----------|-----------|
| `E` | 2026-07-23 (24.9 MB) | — | **the 2026-03-31 copy was examined — an older one** |
| `T` | 2026-07-14 (64.3 MB) | — | **the 2026-06-14 copy was examined — an older one** |
| **`S`** | 2026-07-11 (155.4 MB — the largest artefact on the host) | **16.0.1.3** | **examined after the census, see §10** |
| `U` | 2026-08-30 (45.6 MB) | not established | **no** |
| `B` | 2026-08-03 (35.7 MB dump + 29.5 MB backup, marked `19.0+e`) | not established | **no** |
| — | — | | |

> **Two of the two deployments first examined were chosen by convenience, and for both a newer copy
> exists that was not used.** The census was run *after* the choice, not before it. The programme's
> own rule — *rank the population before choosing* — was violated, and only running the census
> exposed it. Recorded as `GAP-INV-17`, and the largest artefact turned out to change the picture
> materially (§10).

**Residual bound:** 3 of 6 identities remain unexamined, and cloud storage was not swept.

## 9. What the two series-19 deployments could not measure

Both carry **zero on-hand quantity**. Structural reachability is measured; **transactional
reachability is not** (`GAP-INV-09B`).

## 10. The census's decisive find — a transacted deployment, in the wrong generation

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

### RR-F-06 — The per-movement valuation chain exists in series 16 and does not exist in series 19 (**CRITICAL**)

Measured on the series-16 transacted deployment against the series-19 deployment:

| | series 16 (transacted) | series 19 (`T`) |
|---|---|---|
| Valuation-ledger table | **present** | **absent** |
| Valuation rows | **74,982** | — |
| Rows per stock movement | **0.72** | — |
| Rows carrying a **stock-movement** reference | **73,511 — 98.0%** | — |
| Rows carrying an **accounting-entry** reference | **57,863 — 77.2%** | — |
| Rows carrying a value | 74,982 — 100% | — |
| Replacement object rows | — | **85,832** |
| …of which carry a **movement** reference | — | **0 — 0.0%** |
| …content | — | product price changes |

> **In series 16 the domain maintains a per-movement valuation ledger, 98% of whose rows bind to a
> stock movement and 77% to an accounting entry. In series 19 that ledger does not exist, and the
> object that replaced it carries no movement binding at all on a real deployment.**

This is the movement → value → posting audit chain, measured on both sides. Its disappearance is not a
rename and not a source-reading artefact: **it is visible in the data of two real deployments.**

`CRITICAL-GAP-01` is now supported by source evidence, deployment-schema evidence and **row-level
population evidence across two generations.** It is the primary input to `BOSS-DEC-01`.

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