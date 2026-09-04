# P01 — PRIMARY EVIDENCE BASE (LAYER 2 — AUDIT QUARANTINE)

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Process: `P01 — Procure-to-Pay`
Branch: `research/account-p01-procure-to-pay-2026-09-04-001`
Classification: **LAYER 2 — AUDIT QUARANTINE. Boss / PMO / AI-Audit only.**
Reason for quarantine: this file carries reference-system file paths, identifiers and line
numbers. Under the Clean Room Learning Directive these may not be transcribed into any
Layer 1 deliverable, any Team B package, or any implementation artefact.

Downstream Layer 1 documents cite the **evidence IDs** in this file (`EV-P01-nn`), never the
paths.

---

## 1. DECLARED SOURCE ROOTS (PATH SET)

Discovery command (whole-volume, full depth, no maxdepth):

```
find /Volumes/iMacSys -name "__manifest__.py" -type f
```

Result: **31,513** manifest files across the volume. These are not 31,513 distinct modules —
the volume holds many parallel copies of several product generations. Grouping by containing
directory (`awk -F'/' '{NF-=2; OFS="/"; print}' | sort | uniq -c | sort -rn`) returns the
module-bearing roots. The five roots below were selected as the P01 evidence path set; every
other root is recorded as **CLASS C — NOT YET SEARCHED**, not as absent.

| Tag | Root | Module count | Generation | Role |
|---|---|---|---|---|
| `R1` | `CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons` | 790 | v18 enterprise, build 20250608 | Generation cited as target by prior SMEsPlus rounds |
| `R2` | `CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons_archive` | 959 | v18 archive | Modules present in the build but outside the active addons root |
| `R3` | `CLAUDE AI/SMEsPlus/SMEsPlus19/SMEsPlus/odoo-19.0+e.20260417/odoo/addons` | 1,433 | v19 enterprise, build 20260417 | Later generation present in the workspace |
| `R4` | `ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/smeplus-custom/addons` | 65 | project custom, v18 line | Project's own addon set |
| `R5` | `ODOO/ODOO-COMMUNITY/ODOO19/SMEsPlus-SMEsPlus_Extra19` | 83 | project custom, v19 line | Project's own addon set |

All roots are relative to `/Volumes/iMacSys/`.

**Roots deliberately NOT searched in this session (CLASS C — NOT YET SEARCHED):** every other
root returned by the discovery command, including but not limited to the `MIGRATION/ODOO18/*`
build variants (18.0.1 / 18.0.2 / 18.0.3 / 18.0.4 / 18.0.5), `MIGRATION/SMEsPlus19/*`
(00_community / 01_extra_module / 02_enterprise / 96_combined / 97_e-Taxing),
`ODOO/ODOO-COMMUNITY/SMEsPlus19/*`, `ODOO/ODOO-COMMUNITY/Odoo18/t8master/*`,
`ODOO/ODOO-COMMUNITY/Odoo14/addons`, `ODOO/SOURCE CODE/ODOO 12|18|19`,
`SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/*`, `95_BHPRO_PROJECT/*`, `97_OCC_PROJECT*`,
`96_SWR_PROJECT`, `VING/*`, `WCF`, `PROJECT`, `FACEBOOK`.
No claim in this package is a claim about those roots.

---

## 2. P01 MODULE POPULATION — DENOMINATOR DECLARATIONS

### 2.1 Population A — "modules that declare a dependency on the purchase module"

- **POPULATION:** installable modules in a root.
- **UNIT:** one module directory containing a manifest file.
- **PATTERN:** parse the `depends` list out of each manifest with a regex + literal-eval, then
  select modules where the purchase module appears in `depends`, plus the purchase module
  itself. Script preserved at §6.1.
- **PATH SET:** `R1`, `R2`, `R3`, `R4`, `R5`.
- **FALSE-NEGATIVE MODES (declared):** (a) a manifest whose `depends` list is built
  programmatically rather than as a literal is not matched; (b) a module that participates in
  procure-to-pay without depending on the purchase module is **not** in this population — and
  several material ones do not (the Thai withholding-tax set, landed costs, the core
  accounting module, the payment-deduction module). Population A is therefore **not** the P01
  denominator on its own. It is one bounded slice.

| Root | Modules | In population A |
|---|---|---|
| `R1` | 790 | 12 |
| `R2` | 959 | 8 |
| `R3` | 1,433 | 17 |
| `R4` | 65 | 5 |
| `R5` | 83 | 11 |

Population A members, by root:

- `R1`: account_budget · account_invoice_extract_purchase · approvals_purchase ·
  partner_commission · project_purchase · purchase · purchase_edi_ubl_bis3 ·
  purchase_product_matrix · purchase_requisition · purchase_stock · sale_purchase ·
  sale_purchase_inter_company_rules
- `R2`: account_3way_match · l10n_din5008_purchase (+dup) · l10n_in_purchase (+dup) ·
  l10n_pe_reports_stock (+dup) · purchase_intrastat
- `R3`: as `R1` plus account_3way_match · account_budget_purchase · l10n_din5008_purchase ·
  l10n_pe_reports_stock · purchase_accountant · purchase_intrastat
- `R4`: cr_effective_date_entries · import_bridge_axis · purchase_request ·
  scgl_advance_expense_request · scgl_purchase_advance_payment
- `R5`: 19_bhpro_purchase_ext · account_3way_match · courier_type ·
  cr_effective_date_entries · import_bridge_axis · purchase_discount_catalog ·
  purchase_order_lines_discount · purchase_request · scgl_advance_expense_request ·
  scgl_product_image · scgl_purchase_advance_payment

### 2.2 Population B — "modules whose files mention any P01 chain entity"

- **POPULATION:** installable modules in a root.
- **UNIT:** one module directory (a module counts once no matter how many hits it contains).
- **PATTERN:** walk every `.py`, `.xml`, `.csv`, `.js` file in the module, lower-case the
  contents, and test for the literal substrings listed in §6.2 (order, requisition, request,
  receipt/picking, valuation layer, landed cost, journal entry, payment, withholding, wht,
  partial reconcile, supplier info, tax, currency rate, fiscal position, quant, full reconcile).
  Script preserved at §6.2.
- **PATH SET:** `R1`, `R2`, `R3`, `R4`, `R5`.
- **FALSE-NEGATIVE MODES (declared):** (a) a module that reaches the chain only through an
  inherited method and never names the entity is not matched; (b) files with other extensions
  (`.po`, `.sql`, `.json`, `.rst`, binary) are not read; (c) dynamically-composed model names
  are not matched; (d) the token list is author-chosen and is therefore **not** a proof of
  completeness — it is a declared, reproducible slice.

| Root | Modules | Touch ≥1 chain entity | Touch the purchase-order entity |
|---|---|---|---|
| `R1` | 790 | 211 | 39 |
| `R2` | 959 | 557 | 12 |
| `R3` | 1,433 | 557 | 49 |
| `R4` | 65 | 30 | 7 |
| `R5` | 83 | 39 | 14 |

### 2.3 Population C — "journal-entry creation sites inside the P01 module set"

- **POPULATION:** call sites that construct a journal entry or a journal item.
- **UNIT:** one source line containing one such call.
- **PATTERN:** `grep -rnE "env\['account\.move(\.line)?'\](\.sudo\(\))?\.(create|new)"`
  over the module set, excluding `/tests/`.
- **PATH SET:** `R1`, modules: purchase · purchase_stock · purchase_requisition ·
  purchase_requisition_stock · purchase_mrp · stock_account · stock_landed_costs · account ·
  account_payment · purchase_edi_ubl_bis3 · account_invoice_extract_purchase.
- **FALSE-NEGATIVE MODES (declared):** (a) creation through a variable or an alias
  (`Move = self.env['account.move']` then `Move.create(...)`) is not matched; (b) creation
  through `_reverse_moves`, `copy()`, `_post()` internals, or a wizard in another module is
  not matched; (c) creation in modules outside the listed set is not matched. This count is a
  **floor, not a total.**

| Module (`R1`) | Sites |
|---|---|
| account | 16 |
| stock_account | 7 |
| purchase_stock | 3 |
| purchase | 2 |
| purchase_requisition | 0 |
| purchase_requisition_stock | 0 |
| purchase_mrp | 0 |
| stock_landed_costs | 0 |
| account_payment | 0 |
| purchase_edi_ubl_bis3 | 0 |
| account_invoice_extract_purchase | 0 |

---

## 3. EVIDENCE ITEMS

Citation format: `<root>:<module>/<path>:<line>`.

| ID | Evidence | Citation | Classification |
|---|---|---|---|
| `EV-P01-01` | Order confirmation writes only status and an approval timestamp; no accounting document, no journal entry, no payable is produced | `R1:purchase/models/purchase_order.py:516-538` | FACT VERIFIED (scope `R1`) |
| `EV-P01-02` | Order cancellation is blocked while any related vendor bill is in a state other than cancelled or draft | `R1:purchase/models/purchase_order.py:541-545` | FACT VERIFIED (scope `R1`) |
| `EV-P01-03` | A company-level "lock" setting drives an order to a terminal state immediately on approval | `R1:purchase/models/purchase_order.py:519` | FACT VERIFIED (scope `R1`) |
| `EV-P01-04` | Receipt valuation entries are produced **only** when the item is storable; consumable and service items produce none | `R1:stock_account/models/stock_move.py:707-709` | FACT VERIFIED (scope `R1`) |
| `EV-P01-05` | Receipt valuation entries are produced **only** when the item's valuation mode is real-time; under periodic valuation a valuation layer is written but no journal entry | `R1:stock_account/models/stock_valuation_layer.py:81`, `:240` | FACT VERIFIED (scope `R1`) |
| `EV-P01-06` | The accounting date of the receipt valuation entry is: a context override if present, else the date of a linked invoice line, else **the system's current date in the acting user's timezone** — not the goods-movement date | `R1:stock_account/models/stock_move.py:670-675` | FACT VERIFIED (scope `R1`) |
| `EV-P01-07` | The credit account of an incoming receipt is a location-level override if set, otherwise the category-level goods-received clearing account | `R1:stock_account/models/stock_move.py:531-532` | FACT VERIFIED (scope `R1`) |
| `EV-P01-08` | Missing clearing / valuation account or missing valuation journal raises a blocking error at receipt time, not at configuration time | `R1:stock_account/models/stock_move.py:491-497` | FACT VERIFIED (scope `R1`) |
| `EV-P01-09` | On a vendor bill, the expense account of a line is silently replaced by the goods-received clearing account when the item is storable **and** real-time valued **and** the company runs the interim-account model | `R1:stock_account/models/account_move.py:263-274` | FACT VERIFIED (scope `R1`) |
| `EV-P01-10` | The clearing account is reconciled between receipt and bill **only if that account carries the "allow reconciliation" flag**; if it does not, both entries land there and are never matched, and no error is raised | `R1:stock_account/models/account_move.py:214` | FACT VERIFIED (scope `R1`) |
| `EV-P01-11` | Resetting a posted vendor bill to draft, or cancelling it, **deletes** the interim/correction journal items rather than reversing them | `R1:stock_account/models/account_move.py:56-70` (lines 60 and 70) | FACT VERIFIED (scope `R1`) |
| `EV-P01-12` | Duplicating a journal entry strips the interim/correction journal items | `R1:stock_account/models/account_move.py:27-35` | FACT VERIFIED (scope `R1`) |
| `EV-P01-13` | The price-difference engine determines which receipt layer a bill line settles by replaying history ordered by **the audit-log tracking records of the entry's status field**, falling back to the record's creation timestamp | `R1:purchase_stock/models/account_move_line.py:64-78` (line 68 selects the tracking records) | FACT VERIFIED (scope `R1`) |
| `EV-P01-14` | Price difference on already-consumed quantities is posted to the item's expense account against the clearing account; **if the item has no expense account the price difference is silently not posted at all** | `R1:purchase_stock/models/account_move_line.py:271-296` | FACT VERIFIED (scope `R1`) |
| `EV-P01-15` | Price-difference journal items are generated only under real-time valuation | `R1:purchase_stock/models/account_move_line.py:249-253` | FACT VERIFIED (scope `R1`) |
| `EV-P01-16` | A second, independent path posts an accrual expense and liability **directly from a purchase order**, sized from received-not-billed quantity, with an automatic reversal entry at a later date | `R1:account/wizard/accrued_orders.py:246-258` (entry created at line 251) | FACT VERIFIED (scope `R1`) |
| `EV-P01-17` | In that accrual path the accumulator that is supposed to collect the affected orders is initialised empty and **never written to**, in both generations; consequently no note is ever posted to the order and the order carries no record that an accrual exists | `R1:account/wizard/accrued_orders.py:143,243,259` and `R3:account/wizard/accrued_orders.py:151,364,390-391` | FACT VERIFIED (scope `R1`,`R3`; full-file grep of the identifier) |
| `EV-P01-18` | Fixed assets are auto-created at **vendor-bill posting**, driven by a flag on the **general-ledger account of the bill line**, executed with elevated privilege | `R1:account_asset/models/account_move.py:130-139`, `:198-242` | FACT VERIFIED (scope `R1`) |
| `EV-P01-19` | Resetting a bill to draft deletes any still-draft assets created from it | `R1:account_asset/models/account_move.py:186-189` | FACT VERIFIED (scope `R1`) |
| `EV-P01-20` | A vendor payment produces **no journal entry at all** unless an outstanding-payments account is configured on the payment | `R1:account/models/account_payment.py:1002` (inside `_generate_journal_entry`) | FACT VERIFIED (scope `R1`) |
| `EV-P01-21` | Foreign-exchange difference entries are created by the reconciliation engine in the core accounting module, i.e. at settlement, not at bill or receipt | `R1:account/models/account_move_line.py:2853` | FACT VERIFIED (scope `R1`) |
| `EV-P01-22` | A manual inventory-revaluation wizard can create a journal entry that changes the value of previously-received goods | `R1:stock_account/wizard/stock_valuation_layer_revaluation.py:232` | FACT VERIFIED (scope `R1`) |
| `EV-P01-23` | The three-way-match capability is **not present in the active `R1` addons root**; it is present in `R2` (archive), `R3` and `R5` | roots enumerated per §2.1 | FACT VERIFIED (scope: the five declared roots) |
| `EV-P01-24` | The goods-received clearing account model (`stock_input`/`stock_output` resolution keys) has **no runtime definition or use anywhere in `R3`**; the 19 residual occurrences of the category field name are 16 stale translation catalogues and 3 test files. `R3` instead resolves a valuation account plus a "stock variation" account (`account_stock_variation_id`: 127 files in `R3`, 0 files in `R1`) | whole-root grep of `R3`, all file types; `R1` comparison grep | FACT VERIFIED, CLASS A within the stated scope (`R3` addons root, all file types) |
| `EV-P01-25` | The v18 price-difference engine (~358 lines: history replay, layer matching, price-difference journal items and valuation layers) is **absent from the corresponding `R3` file, which is 33 lines**; the interim-account override and interim reconciliation methods are absent from the corresponding `R3` file | file-level line counts and definition-list comparison, `R1` vs `R3` | FACT VERIFIED (scope `R1` vs `R3`) |

### 3.1 Cross-generation file-level comparison (evidence for `EV-P01-25`)

| File | `R1` lines | `R3` lines | Changed lines |
|---|---|---|---|
| purchase_stock/models/account_move_line.py | 358 | 33 | 351 |
| purchase_stock/models/account_invoice.py | 176 | 135 | 73 |
| stock_account/models/account_move.py | 334 | 175 | 215 |
| stock_account/models/stock_move.py | 789 | 684 | 1157 |
| purchase/models/purchase_order.py | 1267 | 1415 | 760 |
| purchase/models/account_invoice.py | 542 | 558 | 64 |

Method: `wc -l` on each side and `diff <a> <b> | grep -c '^[<>]'`. This is a file-level diff,
not a token checklist.

---

## 4. WHAT THIS FILE DOES **NOT** ESTABLISH

- It does not establish which generation or which copy is deployed anywhere. That is
  `DEP-P01-01`, unresolved.
- It does not establish any behaviour of the roots listed as CLASS C — NOT YET SEARCHED.
- It does not establish runtime *behaviour*. Every item in §3 is read from source, and no
  transaction was executed in this session. **It does, however, now rest partly on deployed
  database schemas** — see §12, added later in the session after an independent expert
  established that readable dumps of three live databases exist. Behavioural confirmation is
  still recorded as required evidence, not as a completed step.
- It does not establish any statement about Thai law, Thai tax administration, or accounting
  standards. No authoritative statutory source was consulted in this session.

---

## 5. SCRUB NOTE

Every Layer 1 deliverable in this package was mechanically scanned for reference-system
identifiers before commit. The scan command and its result are recorded in the evidence
manifest. This file, and this file alone, is exempt, by design.

---

## 6. PRESERVED SCRIPTS

### 6.1 Population A enumeration

```python
import os, re, ast
ROOTS = {...five roots as tabulated in §1...}
def depends(p):
    s = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r"['\"]depends['\"]\s*:\s*(\[[^\]]*\])", s, re.S)
    if not m: return []
    try: return [str(x) for x in ast.literal_eval(m.group(1))]
    except Exception: return re.findall(r"['\"]([a-z0-9_]+)['\"]", m.group(1))
for tag, root in ROOTS.items():
    mods = {d: depends(os.path.join(root, d, "__manifest__.py"))
            for d in sorted(os.listdir(root))
            if os.path.isfile(os.path.join(root, d, "__manifest__.py"))}
    sel = sorted(m for m, dep in mods.items() if 'purchase' in dep or m == 'purchase')
    print(tag, len(mods), len(sel), sel)
```

### 6.2 Population B enumeration

```python
TOKENS = ["purchase.order","purchase.requisition","purchase.request","stock.picking",
          "stock.valuation.layer","stock.landed.cost","account.move","account.payment",
          "withholding","wht","account.partial.reconcile","product.supplierinfo",
          "account.tax","res.currency.rate","account.fiscal.position","stock.quant",
          "account.full.reconcile"]
# for each module: walk .py/.xml/.csv/.js, lower-case, substring test, module counts once
```

### 6.3 Population C enumeration

```
grep -rnE "env\['account\.move(\.line)?'\](\.sudo\(\))?\.(create|new)" <module> --include="*.py" | grep -v "/tests/"
```

---

## 7. EVIDENCE ADDENDUM — CROSS-COMPANY AUTO-GENERATION

| ID | Evidence | Citation | Classification |
|---|---|---|---|
| `EV-P01-26` | Company resolution from a partner runs `self.sudo().search([('partner_id','parent_of',partner_id)], limit=1)` — elevated privilege, ancestor match on the contact hierarchy, first match silently wins | `R1:account_inter_company_rules/models/res_company.py:31-35` | FACT VERIFIED (scope `R1`) |
| `EV-P01-27` | Approving a purchase order whose partner resolves to another company auto-creates a sales order in that other company, executed with that company's designated user and company context | `R1:sale_purchase_inter_company_rules/models/purchase_order.py:12-19` | FACT VERIFIED (scope `R1`) |
| `EV-P01-28` | Posting a customer invoice whose partner resolves to another company auto-creates the inverse vendor bill in that company | `R1:account_inter_company_rules/models/account_move.py:11-23` | FACT VERIFIED (scope `R1`) |
| `EV-P01-29` | The "create as" user for cross-company generation **defaults to the superuser** | `R1:account_inter_company_rules/models/res_company.py:22-27` | FACT VERIFIED (scope `R1`) |
| `EV-P01-30` | A company-level setting causes the auto-generated cross-company document to be **created and posted**, not left in draft | `R1:account_inter_company_rules/models/res_company.py:8-15` and `account_move.py:65-66` | FACT VERIFIED (scope `R1`) |
| `EV-P01-31` | No guard restricting the two companies to a common tenant, economic group, or the acting user's allowed companies was found | scope searched: the three files cited in `EV-P01-26`..`EV-P01-28` only | **CLASS B — NOT FOUND IN SEARCHED SCOPE** |

---

## 8. EVIDENCE ADDENDUM — THREE-WAY MATCH, DOWN PAYMENTS, SUBCONTRACT

| ID | Evidence | Citation | Classification |
|---|---|---|---|
| `EV-P01-32` | Three-way match is implemented as an advisory status field on the bill (`release_to_pay`: yes / no / exception) plus a per-line status, with an explicit manual-override flag (`force_release_to_pay`) | `R2:account_3way_match/models/account_invoice.py:21-42` | FACT VERIFIED (scope `R2`) |
| `EV-P01-33` | The module's models contain **no** blocking construct — no exception raise and no constraint. The only matches for `raise` / `UserError` / `api.constrains` / `_check` in its models directory are two company-domain helpers in the dashboard file | pattern: `grep -rn "raise\|UserError\|api.constrains\|_check" <module>/models/` | FACT VERIFIED; negative claim **CLASS A within the module's `models/` directory**, class **C** for its views and for other modules |
| `EV-P01-34` | In `R3`, the status field is referenced only inside its own module — no other non-test python file consumes it | pattern: `grep -rln "release_to_pay" R3 --include="*.py" \| grep -v /tests/` → 2 files, both in the module | FACT VERIFIED; negative claim **CLASS A within `R3` non-test python**, class **C** for XML, JS and other roots |
| `EV-P01-35` | A line goes to `exception` when its price differs from the order price, where the comparison converts currency **at today's date**, not at the bill or order date | `R2:account_3way_match/models/account_invoice.py:120-126` | FACT VERIFIED (scope `R2`) |
| `EV-P01-36` | A bill line **not linked to a purchase order** defaults to `exception` | `R2:account_3way_match/models/account_invoice.py:135-136` | FACT VERIFIED (scope `R2`) |
| `EV-P01-37` | The down-payment routine has exactly one caller in `R1`: a wizard converting existing vendor-bill lines into down-payment lines on an order, creating the order if none exists. No order-side advance wizard exists in `R1` | pattern: `grep -rn "_create_downpayments" R1 --include="*.py"` excluding tests → 2 hits (1 def, 1 caller): `R1:purchase/models/purchase_order.py:625` and `R1:purchase/wizard/bill_to_po_wizard.py:65`; cross-checked by listing `wizard/` in all five `purchase*` modules | FACT VERIFIED; negative claim **CLASS A within `R1`** |
| `EV-P01-38` | On receipt of a subcontracted item the credit is split into a component-cost line and a subcontracting-service-cost line, and the valuation price is forced rather than derived. The source's own comment states the service-cost figure may not represent the real cost of the service | `R1:mrp_subcontracting_account/models/stock_move.py:11-43` | FACT VERIFIED (scope `R1`) |

---

## 9. EVIDENCE ADDENDUM — EXPERT FINDINGS INDEPENDENTLY RE-VERIFIED BY THE SESSION

Under `EC-07`, *Independent Review ≠ Truth; Verified Evidence = Truth Basis.* Each item below
was raised by an independent expert and then **re-derived from source by this session** before
being admitted. The re-derivation is recorded, including where it refined the expert's wording.

| ID | Evidence | Citation | Re-verification outcome |
|---|---|---|---|
| `EV-P01-39` | Auto-matching a vendor bill to a purchase order uses a common domain of company, order state and invoicing status — **with no vendor clause**. The two branches that match on a quoted order reference therefore do not test the vendor at all. Only the last-resort amount-based branch adds a vendor clause | `R1:purchase/models/account_invoice.py:361-364` (domain), `:374`, `:380` (reference branches), `:427-428` (amount branch) | **CONFIRMED, refined.** The expert stated the matching "does not verify the vendor"; precisely, the vendor clause is present on one branch and absent on the two reference branches |
| `EV-P01-40` | `TOLERANCE = 0.02` is a module-level hard-coded, currency-agnostic float, identical in both generations | `R1:purchase/models/account_invoice.py:12`; `R3:purchase/models/account_invoice.py:13` | **CONFIRMED** |
| `EV-P01-41` | On a match, existing vendor-bill lines are **cleared and replaced** by the order's lines. This fires for both `total_match` and `po_match`, and `po_match` is by construction the case where the totals did **not** match within tolerance and no matching subset was found on a scanned bill | `R1:purchase/models/account_invoice.py:330-331` (clear), `:457-460` (branch), `:400-409` (`po_match` determination) | **CONFIRMED.** The expert's characterisation of `po_match` is correct: its own branch comment is "We did not find a match for the invoice total" |
| `EV-P01-42` | A wizard creates a purchase order **from the vendor bill's own line values** and calls the order's confirm method in the same transaction | `R1:purchase/wizard/bill_to_po_wizard.py:13-40`, confirm at `:33` | **CONFIRMED.** Distinct from the down-payment action on the same wizard (`EV-P01-37`); both actions exist |
| `EV-P01-43` | The order reset-to-draft method is a bare status write with **no guard of any kind** — no state test, no test for existing bills or receipts, no group restriction — in **both** generations | `R1:purchase/models/purchase_order.py:522-524`; `R3:purchase/models/purchase_order.py:621-623` | **CONFIRMED.** Contrast with the cancel method, which does guard (`EV-P01-02`) |
| `EV-P01-44` | The shipped access-control file grants the accounting-invoicing group **write** on the purchase order, on purchase order lines, and on the bill-matching object — read+write, no create, no delete. **Identical in both generations.** The read-only accounting group gets read only | `R1:purchase/security/ir.model.access.csv:4,5,9,10,12,13`; `R3:purchase/security/ir.model.access.csv:5,10,13` | **CONFIRMED and widened**: the expert cited only the order-line grant; the same group also has write on the order itself. See `ERR-P01-03` — this session first wrote that the wider grant was `R3`-only, which was wrong: it is present in `R1` too |

---

## 10. POPULATION A′ — TRANSITIVE DEPENDENCY CLOSURE (SUPERSEDES POPULATION A)

- **POPULATION:** modules in the procure-to-pay dependency chain.
- **UNIT:** one module directory containing a manifest.
- **PATTERN:** seed = the purchase module; iterate to fixed point, adding any module whose
  `depends` list intersects the current set. A **custom** root is resolved against the base
  root it layers on (`R4`→`R1`, `R5`→`R3`), because a custom module's dependencies are
  satisfied from the base tree; only modules physically in the custom root are then counted
  for that root.
- **PATH SET:** `R1`, `R2`, `R3`, `R4`, `R5`.
- **FALSE-NEGATIVE MODES (declared):** (a) manifests whose dependency list is not a literal are
  not parsed; (b) a module that participates without any dependency edge to the chain is not
  reached — the Thai withholding-tax set, the payment-deduction module and the core accounting
  module are all in this class, which is why Population B exists; (c) modules in roots not
  searched are not reached; (d) `auto_install` relationships are not modelled.

| Root | Direct (Population A) | Closure (Population A′) | Added by closure |
|---|---|---|---|
| `R1` | 12 | **35** | 23 |
| `R2` | 8 | 10 | 2 |
| `R3` | 17 | **45** | 28 |
| `R4` | 5 | 6 | 1 |
| `R5` | 11 | **13** | 2 |

Members added by the closure in `R1` (identical set in `R3` apart from localisation modules):
approvals_purchase_stock · mrp_landed_costs · mrp_mps · mrp_subcontracting_dropshipping ·
mrp_subcontracting_landed_costs · mrp_subcontracting_purchase · project_account_budget ·
project_mrp_stock_landed_costs · project_purchase_stock · project_stock_landed_costs ·
purchase_mrp · purchase_mrp_workorder_quality · purchase_repair · purchase_requisition_sale ·
purchase_requisition_stock · sale_purchase_project · sale_purchase_stock ·
sale_purchase_stock_inter_company_rules · spreadsheet_dashboard_purchase_stock ·
stock_dropshipping · **stock_landed_costs** · test_main_flows · test_sale_purchase_edi_ubl

Added in `R5`: `19_bhpro_master_data` · **`multi_level_approval_configuration`**.

**Landed costs and subcontracting purchase — both named explicitly in the session directive —
were outside Population A.** See `ERR-P01-04`.

---

## 11. EVIDENCE ADDENDUM — EXPERT FINDINGS RE-VERIFIED (ROUND 2)

| ID | Evidence | Citation | Re-verification outcome |
|---|---|---|---|
| `EV-P01-45` | The two-step purchase-approval threshold is satisfied unconditionally for any member of the purchasing-manager group; and the threshold amount, stored on the order's company, is converted **from the acting user's active company's currency**, not from the order's company's currency | `R1:purchase/models/purchase_order.py:1112-1121` | **CONFIRMED**, both halves, by direct read |
| `EV-P01-46` | The guard blocking a reduction of ordered quantity below received quantity exists in `R1`; in `R3` the message survives only in translation catalogues, one of them marked obsolete, and no equivalent guard was found in the module's code | `R1:purchase_stock/models/purchase_order_line.py:167-174`; `R3` message search across code and catalogues | **CONFIRMED.** Negative for `R3` is class **B** (scope: that module's code plus a message search) |
| `EV-P01-47` | Field spellings in this session's own expert brief were wrong: there is **no** `period_lock_date`. The lock-date fields are `fiscalyear_lock_date`, `tax_lock_date`, `sale_lock_date`, `purchase_lock_date`, `hard_lock_date` | `R1:account/models/company.py:73,78,84,89,94` | **CONFIRMED — the brief was wrong, the expert was right.** See `ERR-P01-05` |
| `EV-P01-48` | On a lock-date violation the posting routine **rewrites the entry's date** to a permitted date rather than refusing to post | `R1:account/models/account_move.py:4934-4936` | **CONFIRMED** by direct read |
| `EV-P01-49` | The context override that can force a valuation entry's period has exactly **one** setter in `R1`: the inventory-adjustment path. It is therefore not reachable from a purchase receipt | `R1:stock_account/models/stock_quant.py:71`; full-root grep of the key, 8 hits, 1 setter | **CONFIRMED.** This **refines** `EV-P01-06`: for P2P, branch 1 is unreachable |
| `EV-P01-50` | Currency conversion resolves as `COALESCE(dated rate, fallback rate, 1.0)`. Identical expression in both generations; the later generation adds further unconditional `or 1.0` fallbacks | `R1:base/models/res_currency.py:140`; `R3:base/models/res_currency.py:138,155,422,430` | **CONFIRMED** by direct read of both |
| `EV-P01-51` | Entry hashing and the audit trail are booleans declared **with no default**, i.e. off unless switched on | `R1:account/models/account_journal.py:123`; `R1:account/models/company.py:257` | **CONFIRMED** by direct read |
| `EV-P01-52` | Thai withholding on a **partial vendor payment**: the already-withheld amount is subtracted as `debit − credit`. The withholding write-off on a vendor payment is a credit, so the expression is negative and the subtraction **increases** the amount withheld on each subsequent payment | `R4:l10n_th_withholding_tax/wizard/account_payment_register.py:57` | **CONFIRMED** by direct read; the arithmetic is as the expert states |
| `EV-P01-53` | The certificate form classification is **inverted between two shipped copies of the same module**: one maps a corporate counterparty to one form, the other maps it to the other. Same file, same lines, opposite mapping | `R4:l10n_th_withholding_tax_cert/models/withholding_tax_cert.py:196,198` vs `R5:` same path and lines | **CONFIRMED** by direct read of both copies |

**Note on `EV-P01-52` and `EV-P01-53`:** these are statements about **source behaviour only**.
Which form is correct under Thai law is `HOLD — STATUTORY EVIDENCE REQUIRED`, and which copy is
deployed is `DEP-P01-01`.
