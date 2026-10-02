# STATE03 VDR — Second-Pass Execution Plan
## DIAGNOSTIC ARTIFACT — NOT GATE PASS — NOT BOSS APPROVAL

**Produced by:** U69 Mandatory Reconciliation Boundary  
**Date:** 2026-10-02  
**Scope:** U70–U99+ second-pass unit assignments  
**Purpose:** Define the ordered execution plan for depth completion following first-pass evidence (U01–U68)

---

## Phase 1: U69 Reconciliation (THIS UNIT — COMPLETED)

**Objective:** Map all 692 modules to G01–G16, assess L1–L12 depth for U01–U68, generate Five Proof Layer assessment, produce second-pass queue and gap register.

**Outputs delivered:**
- `STATE03_U01_U68_DEPTH_RECONCILIATION.md`
- `STATE03_692_MODULE_G01_G16_MAPPING.tsv`
- `STATE03_L1_L12_DEPTH_MATRIX.tsv`
- `STATE03_FIVE_PROOF_LAYER_MATRIX.tsv`
- `STATE03_U69_PLUS_SECOND_PASS_QUEUE.tsv`
- `STATE03_SECOND_PASS_EXECUTION_PLAN.md` (this file)
- `STATE03_SECOND_PASS_GAP_REGISTER.tsv`
- `STATE03_SECOND_PASS_RUNTIME_BACKLOG.tsv`

**Key findings:**
- 67 of 68 evidence files present; U55 MISSING
- L1–L3 PASS for U01–U46 (high-claim, gate-passed); GAP/UNKNOWN for U47–U68
- L4 PASS for chain units; GAP for 30+ isolated units
- L5–L12 GAP/NOT_PROVEN across virtually all units
- P2 (Runtime Reachability) NOT_PROVEN across all 68 units
- P5 (Reconciliation/Adversarial) NOT_PROVEN across all 68 units

---

## Phase 2: P0 Critical Depth — U70–U75 (Accounting Controls + Multi-Company)

**Priority:** ZERO-TOLERANCE. These units target C1-rated functions that block migration gate.

### U70 — Account Lock Dates (PCO-F01)
**Target modules:** `account` (lock date enforcement)  
**Source path:** `account/models/account_move.py` — write protection logic  
**L-levels:** L3 (method-level), L4 (cross-module trigger), L7 (control enforcement), L8 (immutability)  
**Proof layers:** P2 (runtime trial write attempt), P3 (group check), P4 (lock_date_account/everything)  
**Objective:** Prove that posting to a locked period raises ValidationError and identify every bypass pathway.

### U71 — Multi-Company Isolation (MCT-F01/F02/F05)
**Target modules:** `account`, `stock`, `sale`, `purchase` (company_id domain rules)  
**Source path:** `base/security/ir.rule` multi-company rules; `account/models/account_journal.py` company binding  
**L-levels:** L3, L4, L7, L9  
**Proof layers:** P3 (record rule audit), P4 (cross-company transaction trigger)  
**Objective:** Audit all ir.rule records with company_id/allowed_company_ids domain across installed modules; prove MCT-F02 intercompany journal generation source path.

### U72 — Stock Valuation with Perpetual Flag (GRV-F04/IAV-F03/PCO-F03)
**Target modules:** `stock_account`, `stock` (SVL creation), `mrp_account` (MO close valuation)  
**Source path:** `stock_account/models/stock_move.py` — `_account_entry_move()` ; `stock/models/stock_valuation_layer.py`  
**L-levels:** L3, L7, L8  
**Proof layers:** P2 (trace with perpetual flag ON), P3 (valuation config dependency)  
**Objective:** Prove the exact code path for SVL creation and account.move generation when perpetual valuation is active.

### U73 — Audit Trail Immutability (RCN-F02/RCN-F03)
**Target modules:** `account` (account.move lock after posting), `stock_account` (SVL immutability)  
**Source path:** `account/models/account_move.py` — `_check_move_validity()`, `button_draft()` constraints  
**L-levels:** L7, L8, L11  
**Proof layers:** P2, P3, P5  
**Objective:** Prove immutability constraints on posted journal entries; prove audit log double-entry on backdated moves.

### U74 — Three-Way Match / Bill Control (GRV-F06)
**Target modules:** `purchase`, `stock`, `account_payment` (bill control policy)  
**Source path:** `purchase/models/purchase_order_line.py` — `qty_invoiced`, `qty_received`, `invoice_status`  
**L-levels:** L3, L4, L7  
**Proof layers:** P3, P4  
**Objective:** Prove the qty_received vs qty_invoiced constraint and the three-way match blocking mechanism.

### U75 — Period Cutoff / Month-End Stock Closing (PCO-F03/PCO-F04)
**Target modules:** `account`, `stock_account` (accrued_orders wizard)  
**Source path:** `account/wizard/account_accrued_orders_wizard.py`  
**L-levels:** L3, L7, L11  
**Proof layers:** P2, P3, P4  
**Objective:** Prove accrued-orders wizard flow, interim stock account clearing entries, and period close account.move generation.

---

## Phase 3: P1 Core Business Depth — U76–U85

**Priority:** HIGH. Full end-to-end chain proofs for the core SMEsPlus business flows.

### U76 — Full Order-to-Cash (L5/L11)
**Chain:** SO confirm → picking validate → invoice post → payment → reconcile  
**Target modules:** `sale`, `sale_stock`, `stock`, `stock_account`, `account`, `account_payment`  
**L-levels:** L4, L5, L11  
**Proof layers:** P4, P5  
**Objective:** Trace every state transition and account.move created in the chain; prove final receivable reconciliation.

### U77 — Full Procure-to-Pay (L5/L11)
**Chain:** PO confirm → receipt validate → SVL create → vendor bill → payment → reconcile  
**Target modules:** `purchase`, `purchase_stock`, `stock_account`, `account`, `account_payment`  
**L-levels:** L4, L5, L11  
**Proof layers:** P4, P5  

### U78 — Full MRP MO Lifecycle (L5)
**Chain:** BOM create → MO create → consume components → produce FG → close → account entries  
**Target modules:** `mrp`, `mrp_account`, `stock`, `stock_account`  
**L-levels:** L3, L4, L5, L7  
**Proof layers:** P2, P3, P4  

### U79 — Account Entry Full Lifecycle (L4/L7/L11)
**Target modules:** `account` (deep)  
**L-levels:** L4, L7, L8, L11  

### U80 — Stock Valuation AVCO/FIFO Deep (L7/L8)
**Target modules:** `stock_account` (perpetual AVCO, FIFO recomputation)  
**L-levels:** L3, L7, L8  

### U81 — Full Payment/Bank Reconciliation (L5/L11)
**Target modules:** `account_payment`, `account` (bank statement)  
**L-levels:** L4, L5, L11  

### U82 — EDI/UBL/PEPPOL Full Send Flow (L3/L4)
**Target modules:** `account_edi_ubl_cii`, `account_peppol`, `account_edi_proxy_client`  
**L-levels:** L3, L4  

### U83 — MRP Subcontracting + Purchase (L4)
**Target modules:** `mrp_subcontracting`, `mrp_subcontracting_purchase`, `purchase_stock`  
**L-levels:** L3, L4, L7  

### U84 — COGS Timing at Delivery (L7/L8)
**Target modules:** `sale_stock`, `stock_account`, `account`  
**L-levels:** L3, L7, L8  

### U85 — POS Full Session Lifecycle (L5)
**Target modules:** `point_of_sale`, `account`, `account_payment`  
**L-levels:** L3, L4, L5, L7  

---

## Phase 4: P2 Supporting Depth — U86–U94

**Priority:** MEDIUM. Secondary domain depth to bring G09/G12/G13/G13/G14 to L4.

| Unit | Domain | Primary Target |
|------|--------|----------------|
| U86 | CRM | crm.lead→sale.order full pipeline |
| U87 | Project/Timesheet | project→analytic→invoice chain |
| U88 | HR Leave/Work Entry | hr.leave→work_entry→payroll prep |
| U89 | Website eCommerce | website_sale cart→checkout→SO |
| U90 | Marketing Automation | mass_mailing→event→CRM lead |
| U91 | Expense Chain | hr_expense→project_sale_expense→invoice |
| U92 | Website Content | blog/forum/slides platform |
| U93 | Batch Picking | stock_picking_batch→delivery |
| U94 | Payment Webhooks | Stripe/PayPal webhook→account.move |

---

## Phase 5: Critical Recovery + Cross-Module Synthesis — U95–U99

### U95 — U55 Recovery (P0)
**Action:** Identify gap modules, produce full L1–L3 evidence file  
**Blocking:** All coverage counts incomplete until U55 recovered

### U96 — Landed Costs (P1)
**Target:** `stock_landed_costs`, `mrp_landed_costs`  
**Function-IDs:** GRV-F05 (C1-rated)

### U97 — Survey Integration (P2)
**Target:** `survey`, `survey_crm`

### U98 — Python Tax + Tag Update (P1)
**Target:** `account_tax_python`, `account_update_tax_tags`  
**Note:** L7/L12 critical — Python eval in accounting context is an adversarial target

### U99 — Multi-Company Record Rule Audit (P0)
**Target:** All installed modules (ir.rule scan)  
**L-levels:** L7, L9  
**Proof layer:** P3, P5

---

## Execution Notes

1. **U95 (U55 recovery) is blocking** — assign before any new P0 unit can claim 692/692 coverage
2. **U70, U71, U99** are the three highest-risk open items for migration go/no-go
3. **Runtime evidence (P2)** cannot be obtained without executing Odoo — these items should move to the AWT (Automated Workflow Test) backlog once runtime environment is provisioned
4. **No fabrication** — every source pointer in second-pass units must be a real path:line actually read
5. **Canonical denominator (692)** remains frozen pending Boss approval — do not adjust until authorized

---

*This plan is a DIAGNOSTIC artifact. It does not constitute Gate PASS, Formal Coverage measurement, V-level assignment, or Boss Approval.*
