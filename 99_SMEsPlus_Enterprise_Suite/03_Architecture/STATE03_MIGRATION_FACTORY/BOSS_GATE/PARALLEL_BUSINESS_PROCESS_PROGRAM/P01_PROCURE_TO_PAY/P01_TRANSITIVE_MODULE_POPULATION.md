# P01 — TRANSITIVE MODULE POPULATION

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.** Supersedes Population A of the previous round; that population is preserved as
audit lineage, not deleted (`ERR-P01-04`).

---

## 1. THE DENOMINATOR, DECLARED IN FULL

- **POPULATION:** modules in the procure-to-pay dependency chain.
- **UNIT:** one module directory containing a manifest, counted once, in the root where it
  physically lives.
- **PATTERN:** seed on the purchase capability; iterate to a fixed point adding any module whose
  declared dependency list intersects the current set. A **custom** root is resolved against the
  base root it layers on, because a custom module's dependencies are satisfied from the base
  tree; only modules physically present in the custom root are then counted for that root.
- **PATH SET:** the five declared roots (`R1` v18 enterprise, `R2` v18 archive, `R3` v19
  enterprise, `R4` custom v18-line, `R5` custom v19-line).
- **DECLARED FALSE-NEGATIVE MODES:**
  (a) a manifest whose dependency list is built programmatically rather than as a literal is not
  parsed;
  (b) **a module that participates in procure-to-pay without any dependency edge to the purchase
  capability is not reached** — the Thai withholding-tax set, the core accounting module, the
  stock-accounting module and the payment-deduction module are all in this class. This is the
  decisive residual gap and it is why the content-token population from the previous round is
  retained alongside this one rather than replaced;
  (c) modules in roots outside the path set are not reached;
  (d) `auto_install` relationships are not modelled;
  (e) modules present only in a deployed database and in no searched root would not appear.

---

## 2. OLD DENOMINATOR / CORRECTED DENOMINATOR / DELTA

| Root | Old (direct only) | Corrected (transitive closure) | Delta |
|---|---|---|---|
| `R1` v18 enterprise (790 modules) | 12 | **35** | +23 |
| `R2` v18 archive (959) | 8 | **10** | +2 |
| `R3` v19 enterprise (1,433) | 17 | **45** | +28 |
| `R4` custom v18 (65) | 5 | **6** | +1 |
| `R5` custom v19 (83) | 11 | **13** | +2 |
| **Union across roots** | — | **65 distinct module names** | — |

### What the closure added that the directive had explicitly required

**Landed cost** (`stock_landed_costs`, `mrp_landed_costs`, and three project/subcontract landed-cost
bridges) and **subcontract purchase** (`mrp_subcontracting_purchase`,
`mrp_subcontracting_landed_costs`, `mrp_subcontracting_dropshipping`) were **outside the old
denominator**, together with purchase-manufacturing, purchase-repair, requisition-stock,
dropshipping, the purchase-approval-stock bridge, and — in the custom v19 root — the
multi-level approval configuration module.

---

## 3. INSTALLED-STATUS CLASSIFICATION

This is the material advance of this continuation: the deployed databases record which modules
are actually installed, so every member of the population can be classified rather than assumed.

- **POPULATION:** module rows in the deployed module registry of each readable database.
- **UNIT:** one module name with state `installed`.
- **PATH SET:** the three readable database dumps — `D1` (v19, active), `D2` (v19, near-empty),
  `D3` (v16, heavily used). The fourth dump is **not readable — class C**.
- **FALSE-NEGATIVE MODE:** a module installed in a deployment whose dump is not readable, or in
  any deployment not represented here, is invisible.

Installed counts: `D1` 251 · `D2` 232 · `D3` 190.

Of the 65 union members: **18 are installed in at least one readable deployment; 47 are not
installed in any.**

| Module | `D1` v19 | `D2` v19 | `D3` v16 | Classification |
|---|:--:|:--:|:--:|---|
| purchase | ● | ● | ● | INSTALLED VERIFIED |
| purchase_stock | ● | ● | ● | INSTALLED VERIFIED |
| purchase_mrp | ● | ● | ● | INSTALLED VERIFIED |
| **stock_landed_costs** | ● | ● | ● | **INSTALLED VERIFIED** |
| **mrp_landed_costs** | ● | ● | ● | **INSTALLED VERIFIED** |
| sale_purchase | ● | ● | ● | INSTALLED VERIFIED |
| sale_purchase_stock | ● | ● | ● | INSTALLED VERIFIED |
| spreadsheet_dashboard_purchase_stock | ● | ● | ● | INSTALLED VERIFIED |
| **scgl_purchase_advance_payment** | ● | ● | ● | **INSTALLED VERIFIED** (project custom) |
| **sale_purchase_inter_company_rules** | ● | ● | — | INSTALLED in v19 only |
| **sale_purchase_stock_inter_company_rules** | ● | ● | — | INSTALLED in v19 only |
| purchase_accountant | ● | ● | — | INSTALLED in v19 only (no v18 equivalent exists) |
| purchase_edi_ubl_bis3 | ● | ● | — | INSTALLED in v19 only |
| account_invoice_extract_purchase | ● | — | — | INSTALLED in one deployment |
| **purchase_request** | — | — | ● | INSTALLED in v18 only (project custom) |
| **approvals_purchase** | — | — | ● | INSTALLED in v18 only |
| **approvals_purchase_stock** | — | — | ● | INSTALLED in v18 only |
| account_budget | — | — | ● | INSTALLED in v18 only |

### Not installed in any readable deployment — 47 members, including:

`account_3way_match` · `purchase_requisition` (+ `_sale`, `_stock`) · `purchase_repair` ·
`mrp_subcontracting` and every subcontracting bridge · `stock_dropshipping` ·
`purchase_intrastat` · `cr_effective_date_entries` · `l10n_th_withholding_tax_multi` ·
`account_payment_multi_deduction` · `multi_level_approval_configuration` ·
`scgl_advance_expense_request`.

---

## 4. WHICH PRIOR FINDINGS THIS CHANGES

| Prior finding | Effect of installed-status evidence |
|---|---|
| Three-way matching is a report, not a control | **Strengthened and re-scoped: it is not installed in any readable deployment.** The whole three-way-match analysis is `SOURCE ONLY — NOT INSTALLED VERIFIED`. There is no three-way match running anywhere we can see |
| A custom effective-date tool rewrites valuation timestamps by direct SQL | **Latent, not live** — not installed in any readable deployment |
| A second withholding path exists | **The second path is latent** — the multi-payment withholding module is installed nowhere. The single installed path is the one carrying the arithmetic defect |
| Cross-company auto-generation is a tolerance-zero risk | **LIVE, and only in v19.** Both intercompany bridges are installed in both v19 deployments and in neither v18 one. This moves the item from latent to live for the v19 line |
| Vendor advances are bill-first in the base | **The project's custom vendor-advance module is installed in all three deployments** — so the business is not using the base shape anywhere |
| Landed cost was out of scope | **In scope and installed everywhere.** It was the largest single omission |
| Subcontract purchase was out of scope | **In scope by dependency, but installed nowhere** — latent |
| Three requisition mechanisms coexist | In the v16 deployment the **approvals** pair is installed and the base requisition module is not; the project's own purchase-request module is also installed there. So two requisition mechanisms are live in v18 and none in v19 |

---

## 5. WHAT THIS POPULATION STILL DOES NOT COVER

Declared, not concealed:

- Every member of false-negative mode (b) — modules reaching procure-to-pay without a dependency
  edge. The content-token population from the previous round remains the instrument for those,
  and it is **not** superseded by this document.
- The 47 not-installed members are **source capability only**. Findings drawn from them describe
  what the software can do, never what any observed deployment does.
- Any deployment other than the three readable ones — **class C**.

---

# ADDENDUM — THE FOURTH DATABASE, AND THE CLAIMS IT FALSIFIES

## A.1 The fourth dump is readable

It was recorded above, and throughout this package, as *"not readable by the available
tooling — class C"*. **That was wrong.** It is readable with a newer restore binary, which was
already installed on this machine alongside the older one. Found by an independent expert.
`ERR-P01-15`.

`D4` is **generation 19.0** and carries **453 installed modules** — nearly double any other database
in the estate.

## A.2 Corrected installed-status denominator

| | Three databases (as published above) | **Four databases** |
|---|---|---|
| Union closure members | 65 | 65 |
| **Installed in ≥1 deployment** | 18 | **37** |
| **Not installed in any** | 47 | **28** |

**Nineteen members are installed only in `D4`** — that is, they were invisible to the
three-database base:

`account_3way_match` · `mrp_subcontracting_purchase` · `mrp_subcontracting_landed_costs` ·
`purchase_requisition` · `purchase_requisition_sale` · `purchase_requisition_stock` ·
`purchase_repair` · `purchase_intrastat` · `purchase_mrp_workorder_quality` ·
`purchase_discount_catalog` · `purchase_order_lines_discount` · `19_bhpro_purchase_ext` ·
`mrp_mps` · `project_purchase` · `project_purchase_stock` · `project_stock_landed_costs` ·
`project_mrp_stock_landed_costs` · `sale_purchase_project` · `scgl_product_image`

`mrp_subcontracting` and `mrp_subcontracting_account` are likewise installed in `D4`.

## A.3 The claims this falsifies — stated plainly

| Claim published earlier in this package | Status |
|---|---|
| *"Three-way matching is **not installed in any readable deployment**"* | **FALSE.** It is installed in `D4` |
| *"Subcontract purchase is in scope by dependency but **installed nowhere** — latent"* | **FALSE.** The subcontracting family is installed in `D4` |
| *"`purchase_requisition` is **not installed anywhere**; two requisition mechanisms are live in the v16 deployment and none in v19"* | **FALSE.** The base requisition family is installed in `D4` |
| *"47 of 65 members are source-capability only"* | **WRONG COUNT.** 28 of 65 |

Each of those was a **class-A-shaped statement bounded to a scope that wrongly excluded the most
relevant database.** The bound was stated honestly every time; the bound itself was the error.

An independent expert additionally reports that `D4` holds **zero subcontract transactions**, so
the correct status for subcontracting is **INSTALLED BUT NOT EXERCISED** — not *latent*, and not
*in use*. That report is **peer-derived and not re-derived by this session**.

## A.4 What `D4` is, and why it matters most

`D4` is the only database in the estate that has three-way matching, subcontracting and the
requisition family installed together, and — per the same expert — **the only one with any
period lock date set**.

**It is therefore the single most relevant database to P01, and it is the one the evidence base
excluded.** Every population statement in this package should be read as bounded to the three
databases it was computed over, unless it appears in this addendum.

## A.5 Not yet done

`D4`'s data was **not** analysed by this session beyond the module registry — no valuation,
receipt, bill, payment or lock data was read from it. **Class C, and now a known-reachable
class C rather than a believed-unreachable one.** It is the highest-value remaining work in P01.
