# 30 — P05 PEER HANDOFF MATRIX

`LAYER 2 — AUDIT QUARANTINE`

**Rule observed throughout:** P05 preserves evidence and routes it. **P05 does not decide peer
canonical architecture.** Every row below is an observation with its evidence, not an adjudication.

## 1. → P01 — Procure-to-Pay  ·  **HIGHEST PRIORITY HANDOFF IN THIS PACKAGE**

`scgl_purchase_advance_payment` is **installed in all four distinct databases evidenced** evidenced
(`24 §3`). Two defects in it are therefore live, and both are P01's territory.

| ID | Observation | Evidence | Class | P01 must decide |
|---|---|---|---|---|
| `H-P01-1` | **Vendor down payments are never deducted from the final bill.** `deduct_down_payments` has four references and its **only** consumer is commented out; the live branch calls a core action that knows nothing of the flag. The vendor is billed the full order value **in addition to** the down-payment bill. | `wizard/purchase_advance.py:51, 178-179`; declared search: whole custom tree, pattern `deduct_down_payments`, class **A** | FACT VERIFIED | whether this is a live duplicate-payment exposure in its process, and its remediation |
| `H-P01-2` | **Any internal user can create a vendor bill.** The wizard's ACL grants full CRUD on `purchase.advance.payment.bill` to `base.group_user`, and `_create_bill` creates the `account.move` with `.sudo()`, bypassing `account.group_account_invoice`. | `security/ir.model.access.csv:2`; `wizard/purchase_advance.py:203` | FACT VERIFIED | authorisation model for advance billing |
| `H-P01-3` | Percentage down payment computed on the wrong base with the wrong tax field — `taxes_id` (customer) instead of `supplier_taxes_id`, and `all([])` is `True`, so the percentage applies to tax-**inclusive** `amount_total`. | `wizard/purchase_advance.py:26, 94, 116` | FACT VERIFIED | correctness of the deposit base |
| `H-P01-4` | The module forks a feature core already ships (`is_downpayment`, `_create_downpayments`), and its button replacement covers 2 of the 4 core buttons — the two list-header "Create Bills" buttons bypass the wizard entirely. | `purchase/models/purchase_order.py:611-645`; `view/purchase_view.xml:8-17` vs `purchase/views/purchase_views.xml:140,146,555,597` | FACT VERIFIED | fork vs core |
| `H-P01-5` | Ownership question P05 will not answer: does P01 own **vendor** advances? P05 owns employee advances. `scgl_purchase_advance_payment` sits on `purchase`. | `09 §2` | OPEN | canonical ownership |
| `H-P01-6` | An expense line can name a `vendor_id` and post to vendor-facing accounts **without any purchase document**. | `hr_expense.py:180, 923, 942, 951, 961` | FACT VERIFIED | whether that is permitted in P01's model |

**Status: `PEER DEPENDENCY — P01`. Open. P05 asserts nothing about P01's canonical ownership.**

## 2. → P06 — Bank-to-Reconcile

| ID | Observation | Evidence | Class |
|---|---|---|---|
| `H-P06-1` | The declared immutability guard on expense-linked payments does not contain `journal_id` or `ref`; both are editable on a posted-linked payment. | `hr_expense/models/account_payment.py:20-28`; AST reproduction at `14 §3` | FACT VERIFIED |
| `H-P06-2` | On the company-paid branch the claim asserts `payment_state='paid'` and `amount_residual=0` as soon as any move is non-draft — **before any bank movement**. The source comment states this openly. | `hr_expense_sheet.py:209-229` | FACT VERIFIED |
| `H-P06-3` | The advance cash-return path creates a journal entry against the payment journal's default account **with no `account.payment` object** — the cash movement is invisible to payment-based reconciliation tooling. | `advance_request_reconcile.py:62-92` | FACT VERIFIED (module latent) |
| `H-P06-4` | Neither advance-clearing builder sets `currency_id` or `amount_currency`; a foreign-currency clearing reconciliation has no defined behaviour. Outcome held class **D**. | `21 NC-10`, `NC-D-01` | FACT VERIFIED (mechanism) / **D** (outcome) |
| `H-P06-5` | Payment-batch bank-account selection reads the employee's bank account under `sudo()` and otherwise takes an arbitrary first partner bank account. | `hr_expense/wizard/account_payment_register.py:13-22` | FACT VERIFIED |

**Status: `PEER DEPENDENCY — P06`. Open.**

## 3. → P07 — Thailand Tax-to-Compliance  ·  **STATUTORY OWNERSHIP IS P07's**

> **P05 records mechanical source and database facts. P05 asserts no Thai statutory rule and makes no
> compliance determination.** Every statutory question below is `HOLD — STATUTORY EVIDENCE REQUIRED`
> and is **P07's to answer**.

| ID | Mechanical observation (P05) | Statutory question (P07) | Evidence |
|---|---|---|---|
| `H-P07-1` | **Two independent WHT subsystems are installed together in 4 of 5 real databases — and the divergence is now MEASURED.** In a production database, **5,426 of 5,863 journal lines (92.55%) posted to the withholding account carry no `tax_line_id`** and would be dropped by the enterprise PND CSV export's inner join, while remaining visible to the tag-based on-screen report. | Does that divergence affect a filed return, and by what amount? | `l10n_th_reports/models/tax_report_pnd.py:29-64`; `l10n_th/data/account_tax_report_data.xml:192,203,...`; `l10n_th_withholding_tax/wizard/account_payment_register.py:21-25` |
| `H-P07-2` | **CORRECTED — see `39 RE-11`.** One **exact duplicate** certificate exists in 5,201 (payment 659, certs 124/126, identical certificate number and line). The originally reported "32 payments" was overstated ~30×: 21 of the 32 are one certificate per **distinct payee** on bulk payment runs, 8 are same-payee **rate splits**, 2 are done+draft pairs. *(An earlier draft labelled the per-payee group "(legitimate)" — **withdrawn**: that pre-answered, in P05's own column, the very question this row routes to P07. P05 records the structure and does not rule on whether it is permitted. Raised by AAS-03 Expert 3.)* Structurally, **no UNIQUE constraint and no index exist** on the certificate table in v16 or any v19 registry, so nothing prevents duplication. | Is a payment permitted multiple certificates — one per payee, and more than one per payee at different rates? Is the one exact duplicate a reportable incident? | `25 §3`, `§4b DB-01` |
| `H-P07-3` | **CORRECTED AND INVERTED — see `39 RE-10`.** The certificate's printed `date` is **correct in 97.79%** of payment-linked rows. The create-time artefact is on the column named **`payment_date`**, which equals `create_date::date` in **100.00% of 5,201 rows** and matches the real payment date in only **16.05%**. | Which column does the filing consume? If any process reads `payment_date` as the payment's date, it is wrong 84% of the time. | `25 §3` |
| `H-P07-4` | **13 `pnd1` certificates cannot be exported** by either report path; the wizard offers only `pnd3`/`pnd53` and the formatter would raise. | Are `pnd1` certificates in scope for this filing? | `25 §3`; `07 TX-15` |
| `H-P07-5` | Cancelled certificates are **included** in the statutory text and XLSX exports as blanked rows that still carry sequence number, VAT id, rate and date. | Does that match the void-row convention? | `07 TX-16` |
| `H-P07-9` | **1,417 certificates (27%) carry no certificate number at all** — `name` is NULL — and **1,414 of those are state `done`**. A further **75 certificate numbers are shared** by more than one certificate. | Must a statutory certificate carry a unique identifier? | `25 §4b DB-04` |
| `H-P07-10` | **362 of 6,159 certificate lines (5.9%) are orphaned** — `cert_id` is NULL — because the FK is `ON DELETE SET NULL`. Deleting a certificate leaves its statutory lines behind rather than removing them. | Are orphaned statutory lines a retention or a correction problem? | `25 §4b DB-03` |
| `H-P07-12` | All seven configured withholding codes point at **one** GL account, so the account cannot discriminate rate or income type; and the code named **`WHT3%` carries a configured rate of `0`**. | Is a zero-rate `WHT3%` code intended? | `07 TX-01a` |
| `H-P07-11` | **At v19 the statutory columns became nullable**: `date`, `income_tax_form` and `supplier_partner_id` are `NOT NULL` at v16 and nullable at v19, while `payment_date` stays `NOT NULL`. The single v19 certificate already has NULL `income_tax_form` and NULL `supplier_partner_id`. | Is a certificate with no payee and no tax form admissible? | `25 §4b DB-06` |
| `H-P07-6` | The PND text file's cleanup never runs — the override targets a method core does not have — so the exported file retains qweb-escaped entities and surrounding whitespace. | Is the file as emitted acceptable? | `07 TX-19` |
| `H-P07-7` | The two subsystems use **different branch identifiers** (`partner.company_registry` vs `partner.branch`). | Which is correct for the return? | `07 §2` |
| `H-P07-8` | A WHT configuration record conflates statutory reference (rate, form class) with company mapping (GL account), forcing the rate to be duplicated per company with nothing keeping copies equal; the duplication mechanism is itself defective. | Are Thai WHT rates uniform across companies of one taxpayer? | `07 TX-17`; `22 §3 R-03` |

**Status: `PEER DEPENDENCY — P07`. Open. `HOLD — STATUTORY EVIDENCE REQUIRED` on all eight.**

## 4. → P08 — Record-to-Report

| ID | Observation | Evidence | Class |
|---|---|---|---|
| `H-P08-1` | **A hashed, inalterable journal entry can be forced to `cancel`** by a raw `state` write, because `'state'` is not a member of `_get_integrity_hash_fields()`. Reconciliation partials survive against the cancelled move. **The P05 trigger is latent; the core gap is not — it belongs to P08.** | `ENT18/account/models/account_move.py:3208-3214, 3836, 5351-5352`; enumerated at `10 EC-13a` | FACT VERIFIED |
| `H-P08-2` | Four code paths sever the claim↔entry link (`ondelete='set null'`, `_reverse_moves`, `button_cancel`, `Command.clear()`), and the guard against partial deletion reads the field the other three have already cleared. | `hr_expense/models/account_move.py:12, 85-90, 92-95, 97-103`; `hr_expense_sheet.py:602-604` | FACT VERIFIED |
| `H-P08-3` | Journal entries are created at **approval**, under `sudo()`, explicitly so approvers need no accounting rights; refusal then `unlink()`s the draft entry. | `hr_expense_sheet.py:711-721, 727-734, 746-760` | FACT VERIFIED |
| `H-P08-4` | Accounting date is derived from the clock in two of three branches; one branch computes the first open period **after** the lock date and books there. | `hr_expense_sheet.py:798-822` | FACT VERIFIED |
| `H-P08-5` | Approval is enforced in the action, not on the field — `approval_state` is a plain Selection with no guard, and an employee's own record rule has no state clause. | `hr_expense_sheet.py:79-86`; `security/ir_rule.xml:49-54` | FACT VERIFIED |
| `H-P08-6` | An expense report can reach `done`/"Paid" with no entry and no payment, and remain deletable. Live in 2 of 6 registries. | `hr_expense_extract/models/hr_expense.py:23, 180-223` | FACT VERIFIED |
| `H-P08-7` | A period can close containing **draft** expense entries, since entries are created at approval and posted later. | `03 §1`; `08 §4` | FACT VERIFIED |

**Status: `PEER DEPENDENCY — P08`. Open.**

## 5. → P09 — Plan-to-Analyze

| ID | Observation | Evidence | Class |
|---|---|---|---|
| `H-P09-1` | Analytic distribution reaches the ledger on the **expense debit line only**; tax lines and the payable/outstanding credit line carry none. An analytic report summing a full entry will not balance by dimension. | `hr_expense.py:916, 1015` | FACT VERIFIED |
| `H-P09-2` | The **entire** advance and petty-cash chain carries no analytic dimension — class **A** within the five files. A cost funded that way is invisible to project/department analytics. | `06 §2` | FACT VERIFIED (modules latent) |
| `H-P09-3` | The default distribution keys on the account **code prefix**, so analytic allocation is coupled to chart numbering; renumbering silently re-routes analytics. | `hr_expense.py:516-527` | FACT VERIFIED |
| `H-P09-4` | It also keys on the employee's **work contact** and its partner categories — not on the employee, department or cost centre. | `hr_expense.py:522-523` | FACT VERIFIED |
| `H-P09-5` | P09's own published finding — *"analytic dimension is schema, not data"* — is consistent with `H-P09-1`/`H-P09-2` observed from a different surface. Offered as convergence, not as adjudication. | P09 branch `research/account-p09-plan-to-analyze-2026-09-04-001` | SUPPORTED INTERPRETATION |

**Status: `PEER DEPENDENCY — P09`. Open.**

## 6. → P11 — Core Accounting Reconciliation

| ID | Item routed | Why it is P11's |
|---|---|---|
| `H-P11-1` | **Cross-process duplicate control.** Three duplicate classes are undetected and one is structural (`E3-02`: the advance system and the claim system share no code path). Detection must key on the **cost event**, which no single process owns. | spans P01, P05, P08 |
| `H-P11-2` | **Event identity.** P05 reaches independently the conclusion Account Wave A reached for the core ledger: the claim↔entry relation cannot be a reconciliation key. A non-severable identity is a platform primitive. | spans all |
| `H-P11-3` | **Scope semantics.** P05's four `CORR1` contributions: reference scope ≠ financial scope; an object whose balance is a company's GL position is company-scoped by derivation; statutory reference belongs at PLATFORM; an operation must determine its executing scope **before** resolving its authoriser. | `22 §3`; `31` |
| `H-P11-4` | **Two WHT subsystems.** Which is the system of record is a cross-process determination (P05 observes, P07 owns statute, P11 reconciles). | `07 §2` |
| `H-P11-5` | **The severity inversion.** P05's most consequential live findings sit in P01's territory. Sequencing across processes is P11's. | `26 §5` |
| `H-P11-6` | Six of ten P05 handoff elements are unsuppliable or partial (`28`). P11 must plan on that, not on a complete expense subledger. | `28` |

**Status: `PEER DEPENDENCY — P11`. Open.**

## 7. Peer Branch State at Publication

| Peer | Branch | Last seen |
|---|---|---|
| P01 | *(none pushed)* | working clone at base only |
| P02 | `research/account-p02-order-to-cash-2026-09-04-001` | `47c2b18` |
| P03 | `research/account-p03-manufacture-to-cost-2026-09-04-001` | `812cc5c` |
| P04 | `research/account-p04-acquire-to-retire-2026-09-04-001` | `f206ac5` |
| P06 | `research/account-p06-bank-to-reconcile-2026-09-04-001` | `4146bb1` |
| P09 | `research/account-p09-plan-to-analyze-2026-09-04-001` | `0d792d9` |
| P07, P08, P10, P11 | not found among remote branches | — |

**P05 has read no peer package content.** The handoffs above are P05-derived observations offered to
peers, not reconciliations of peer findings. That reconciliation is P11's.
