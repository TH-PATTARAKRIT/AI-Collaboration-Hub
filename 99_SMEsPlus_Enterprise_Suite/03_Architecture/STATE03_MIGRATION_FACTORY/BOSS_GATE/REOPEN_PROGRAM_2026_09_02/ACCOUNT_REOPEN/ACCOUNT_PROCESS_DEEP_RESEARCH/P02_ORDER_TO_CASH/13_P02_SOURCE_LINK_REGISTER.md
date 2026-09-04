# 13 — P02 SOURCE LINK REGISTER

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`

## 0. Handling Rule

**These citations must not be transcribed into any downstream clean-room reference package, Functional
Design document, or Team B artefact.** They exist so Boss, PMO and AI-Audit can re-derive every
`FACT VERIFIED` in this package independently. The clean-room handoff is
`19_P02_CORE_RECON_HANDOFF_PACK.md`, which carries none of them.

## 1. Evidence Root

| Field | Value |
|---|---|
| Root | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons` (referenced below as `R`) |
| Nature | Reference ERP source tree — **learning / benchmark only** |
| Build identifier | as embedded in the root path above |
| Access | read-only; **no file in the reference tree was modified during this session** |
| Database access | **none.** No runtime execution, no query, no dump. Every statement in this package is static-source derived unless explicitly marked otherwise. |
| Secondary roots consulted | ORM core module of the same distribution (T4 only) |

## 2. Register — `EV-P02-001` … `EV-P02-069`

| EV | `path:line` | Subject |
|---|---|---|
| 001 | `R/sale/models/sale_order.py:1197`, `:1207` | Confirmation overwrites the order date with the system clock |
| 002 | `R/sale/models/sale_order_line.py:237-242` | Delivered quantity is **stored with the read-only attribute cleared** at the data layer |
| 003 | `R/sale_stock/models/sale_order_line.py:182`, `:194-209` | Delivered quantity = completed outbound minus completed inbound |
| 004 | `R/sale/models/sale_order_line.py:954-980` | Billable quantity: ordered-minus-invoiced vs delivered-minus-invoiced |
| 005 | `R/sale/models/sale_order_line.py:909-924` | Invoiced-quantity counter includes **drafts**; refunds subtract only when linked |
| 006 | `R/sale/models/sale_order_line.py:927-940` | A second counter, **posted only**, for accounting purposes |
| 007 | `R/sale/models/sale_order_line.py:984-1012` | Billing status, including the upselling branch |
| 008 | `R/sale/models/product_template.py:40-46` | The invoice-policy selection — **2 values, complete denominator** |
| 009 | `R/sale/models/sale_order.py:1461` | Invoice grouping keys: company, partner, currency |
| 010 | `R/sale/models/sale_order.py:1512-1596` | Order-to-invoice creation; grouping is the default; **the date argument is documented as unused** |
| 011 | `R/sale/models/sale_order.py:1392-1428` | Invoice header preparation — **no document date is set** |
| 012 | `R/account/models/account_move.py:4884-4890` | Blank document date → **today** for a sale document; **hard error** for a purchase document |
| 013 | `R/account/models/account_move.py:4932-4936` | Lock-date violation **silently moves the accounting date**; no refusal |
| 014 | `R/account/models/account_move.py:5655-5691` | The forward-shift target computation |
| 015 | `R/stock_account/models/account_move.py:38-53` | Cost lines are created **before** the posting decision; matching attempted after |
| 016 | `R/stock_account/models/account_move.py:77-168` | The cost-line generator: invoice-line quantity, accounts, sign, zero-skip |
| 017 | `R/stock_account/models/account_move.py:56-71` | Reset-to-draft and cancel **unlink** the cost lines |
| 018 | `R/stock_account/models/account_move.py:276-278` | Cost eligibility: storable **and** real-time valuation |
| 019 | `R/stock_account/models/product.py:859-863` | Base cost fallback = the product's **standard price** |
| 020 | `R/stock_account/models/product.py:865-909` | Layer consumption, the **standard-price top-up** at `:906-907`, and the divide-by-quantity averaging at `:909` |
| 021 | `R/sale_stock/models/account_move.py:151-202` | Delivery-aware cost re-derivation; **overwrites** the base answer when an order line is present |
| 022 | `R/stock_account/models/stock_move.py:335-352` | The valuation gate: not already done, non-zero quantity, **at least one picked line** |
| 023 | `R/stock_account/models/stock_move.py:703-750` | Outflow entry: Dr outbound stock / Cr valuation; non-storable early return |
| 024 | `R/stock_account/models/stock_move.py:531-538` | Source and destination account resolution |
| 025 | `R/stock_account/models/stock_move.py:695-701` | Owner-restricted movements are excluded from valuation |
| 026 | `R/account/models/account_move_line.py:547-628` | Receivable and revenue account derivation, with fiscal-position remapping |
| 027 | `R/account/models/account_move_line.py:613` | Account selection **by historical frequency** for a product-less line |
| 028 | `R/account/models/account_move.py:330-336` | The product-line set **excludes cost lines** — they are invisible to the generator |
| 029 | `R/account/models/account_move.py:5227-5249` | The manual post path calls the posting routine in **hard** mode |
| 030 | `R/account/models/account_move.py:5430-5455` | The auto-post job; its domain is date-at-or-before-today |
| 031 | `R/account/models/account_move.py:4921-4930` | **Soft** mode defers future-dated documents, leaving them in draft |
| 032 | `R/stock_account/models/stock_valuation_layer.py:161-195` | Layer consumption in creation order, net of returns |
| 033 | `R/sale/models/sale_order_line.py:213-217` | Creating or writing a line on a confirmed order launches procurement |
| 034 | `R/stock_account/models/stock_move.py:385-401` | Cross-company sanity check; single-step cross-company movement is refused |
| 035 | `R/sale/models/sale_order.py:41-46` | The order status enumeration — **4 values, complete denominator** |
| 036 | `R/sale/models/sale_order.py:1137-1173` | Order confirmation |
| 037 | `R/sale/models/sale_order.py:1260-1264` | Lock and **unlock** — a reversible boolean, not a state |
| 038 | `R/stock/models/stock_move.py:123` | The picked marker on the movement |
| 039 | `R/stock/models/stock_picking.py:566-572` | The movement status enumeration — **6 values, complete denominator** |
| 040 | `R/account/models/company.py:142` | The company-level split-recognition boolean |
| 041 | `R/stock_account/models/account_move.py:183-247` | Interim-account matching — conditional, best-effort, silent when skipped |
| 042 | `R/account/models/chart_template.py:483-484` | Chart installation **defaults the split-recognition boolean to off** |
| 043 | `R/l10n_th/models/template_th.py:9-31` | The Thai chart template — **sets no split-recognition boolean and no stock accounts** |
| 044 | `R/l10n_th/data/template/account.account-th.csv` | The Thai chart — **27 accounts, complete denominator** |
| 045 | `R/stock_account/models/product.py:964-970` | Real-time valuation **cannot be enabled** without the three stock accounts |
| 046 | `R/stock_account/models/product.py:915-950` | Valuation mode and the three accounts are **company-dependent** properties |
| 047 | `R/stock_account/models/stock_move.py:491-497` | Runtime guard raising when an account cannot be resolved at outflow |
| 048 | `R/sale/models/product_template.py:170-171` | Goods default to **invoice-on-order** when the policy is empty |
| 049 | `R/stock/models/stock_picking.py:1585` | The backorder remainder has its picked marker cleared |
| 050 | `R/stock_account/models/account_move.py:257-261` | The cost-line origin field — written, **never read for duplicate prevention** |
| 051 | `R/stock/models/stock_move_line.py:41` | The picked marker on the movement line — stored, writable |
| 052 | `R/stock_account/models/stock_valuation_layer.py:75-81` | Entry validation is gated on real-time valuation |
| 053 | `R/stock_account/models/account_move.py:27-36` | Cost lines are stripped on copy unless the copy is a cancelling reversal |
| 054 | `R/account/models/account_move.py:4892-4894` | A document already posted cannot be posted again |
| 055 | `R/stock_account/models/product.py:409`, `:539-542` | The FIFO vacuum and its expense entries — inventory value can move after the fact |
| 056 | `R/account/models/account_move_line.py:71` and `R/account_reports/models/account_report.py:802` | **The tax report keys on the accounting date**, not the document date |
| 057 | `R/account/models/account_move.py:5713-5717` | The pre-post lock warning — advisory, not retained |
| 058 | `R/sale/models/sale_order_line.py:1378-1416` | Invoice-line preparation: price, discount and tax set copied verbatim |
| 059 | `R/sale/models/sale_order_line.py:508` and `R/account/models/account_move_line.py:869` | Tax recomputation **does not depend on the fiscal position** on either side |
| 060 | `R/sale/models/sale_order.py:1418` | The document's fiscal position is copied from the order's stored value |
| 061 | `R/sale/models/sale_order.py:1327-1340` | Tax update is a **manual button** that records what it applied |
| 062 | `R/account/models/account_tax.py:1383` | Tax is computed on the **post-discount** unit price |
| 063 | `R/account/models/account_tax.py:1644-1646`, `:1683-1697` | Global-rounding residue absorbed **inside the tax amounts** |
| 064 | `R/account/models/account_move.py:2620-2650` | The rounding-type line is the **cash-rounding** line, a different mechanism |
| 065 | `R/account/models/account_move.py:2635` | Under its default strategy the cash-rounding line **carries tax tags** |
| 066 | `R/account/models/account_move.py:4832-4993` | The posting routine — **no constraint ties a customer invoice to an order** |
| 067 | `R/account/models/account_move_line.py:777-780` | Two residuals; settled only when **both** are zero |
| 068 | `R/account/models/account_move_line.py:719`, `:757-760` | Residuals exist only on reconcilable accounts |
| 069 | `R/account/models/account_move.py:5228-5231` | Abnormal-amount / abnormal-date detection is **disabled by default** |
| 070 | `R/sale/views/sale_order_views.xml:460`, `:606` | The delivered-quantity field is rendered **read-only unless the derivation method is manual** — the interface-level qualification of `EV-P02-002` |
| 071 | `R/sale/models/sale_order_line.py:827-840` and `R/sale_stock/models/sale_order_line.py:182-192` | The derivation method: **manual** for services and for goods without the inventory module; **outflow-derived** for goods with it |
| 072 | `R/account/models/account_move.py:630-635` | The origin field on the accounting document is a **character field**, read-only, with no relation behind it |
| 073 | `R/sale/models/account_move.py:23`, `:46-48` | A header-level source-order **count** exists as a computed, non-stored traversal through the per-line link — a derivable view, not a stored relation |
| 074 | `R/account/models/account_move.py:691`, `:1831-1835` | A computed duplicate-document field exists on the accounting document |
| 075 | `R/account/models/account_move.py:1867-1875` | The **outbound** match condition: same total amount **and** the same document date, within the same company, partner and document type |
| 076 | `R/account/models/account_move.py:5026-5037` | Its **only** behavioural consumer — suppression of automatic posting, on the **purchase** side only |
| 077 | `R/account/models/account_move.py:753-759` | The supporting index is created **for purchase documents only** |

## 3. Track Evidence

Citations produced by the four parallel research tracks are held in their own extracts, each carrying its
own declared denominator:

| Track | Extract | Subject |
|---|---|---|
| T1 | `L2_AUDIT_QUARANTINE/T1_RETURN_CREDIT_REFUND_EVIDENCE.md` | Return / credit note / refund / reversal |
| T2 | `L2_AUDIT_QUARANTINE/T2_PAYMENT_RECONCILIATION_EVIDENCE.md` | Receipt / settlement / reconciliation / deposits / FX / bad debt |
| T3 | `L2_AUDIT_QUARANTINE/T3_TAX_VAT_WHT_THAI_EVIDENCE.md` | VAT / withholding / tax point / tax period / Thai localisation |
| T4 | `L2_AUDIT_QUARANTINE/T4_SCOPE_BOUNDARY_AND_CLOSE_EVIDENCE.md` | Company boundary / intercompany / period close |

References of the form `T1 §4a.3` in the Layer-2 deliverables resolve into those extracts.

## 4. Reproduction Instructions

Every `FACT VERIFIED` in this package is reproducible with read-only shell inspection of the root in §1.
No tooling, no database, no execution. A reviewer disputing any finding should:

1. open the cited `path:line`;
2. check the finding against the **branch**, not the method name;
3. where the finding is a **negative claim**, re-run the pattern stated in that claim's search boundary
   and confirm the population count, **before** treating the absence as established.

Per `SMEPLUS_DEEP_RESEARCH_NEGATIVE_CLAIM_STANDARD`: `NO EVIDENCE FOUND != FUNCTION DOES NOT EXIST.`
