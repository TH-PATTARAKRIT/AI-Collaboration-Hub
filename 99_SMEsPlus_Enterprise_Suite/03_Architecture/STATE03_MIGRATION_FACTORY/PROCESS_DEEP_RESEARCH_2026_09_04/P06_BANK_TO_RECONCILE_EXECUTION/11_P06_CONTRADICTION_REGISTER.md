# P06_CONTRADICTION_REGISTER.md

**Session:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001 · **Process:** P06 Bank-to-Reconcile
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001 (base `88f52cd`)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Updated under:** `[SMEPLUS-26-09-04-ACC-REV2-CORR1]` — §5 records the scope revalidation impact.

---

## 1. What counts as a contradiction here

Three kinds, kept separate because they carry different weight:

- **Type I — internal to the reference implementation.** Two parts of the same system assert incompatible things. These are the strongest findings: no interpretation is required, only two quotes.
- **Type II — between the implementation and its own documentation.** A docstring, help text, field label or manifest describes behaviour the code does not perform. These matter because a designer reading the model will build the wrong thing.
- **Type III — between this package and its own prior statements, or between evidence sources.** Recorded so that no summary can quietly resolve them.

---

## 2. Type I — internal contradictions in the reference

| ID | Contradiction | Evidence A | Evidence B | Severity |
|---|---|---|---|---|
| C-01 | A field labelled **"Is Matched With a Bank Statement"** is set `True` in two branches where **no bank statement exists** | label `$V18E/account/models/account_payment.py:54` | `:436-450` — `is_matched = pay.state == 'paid'` when no outstanding account; `is_matched = True` when the journal default account is used | **HIGH** |
| C-02 | An invoice may be reported **settled** while its ledger residual is non-zero | `$V18E/account/models/account_move.py:1213-1218` | residual is the basis of `reconciled` at `account_move_line.py:778-780` | **HIGH** |
| C-03 | A field named **"Payment Tolerance"**, switched **off**, widens acceptance instead of narrowing it | label/help `$V18E/account/models/account_reconcile_model.py:284-289` | `$V18E/account_accountant/models/account_reconcile_model.py:520-521` | **HIGH** |
| C-04 | Enabling the **audit trail** converts a hard refusal into a silent un-reconcile | `$V18E/account/models/account_bank_statement_line.py:445-452` (tracked branch → `button_cancel`) | `$V18E/account/models/account_move.py:5283` (`button_draft` → `remove_move_reconcile`) | **HIGH** |
| C-05 | The lock-date regime **blocks locking** a period containing unreconciled statement lines, but does **not block un-reconciling** inside a locked period | `$V18E/account/models/company.py:519-528` | zero lock hits across the reconcile primitives — see attack A6 denominator | **HIGH** |
| C-06 | A **hash chain** asserted over accounting immutability excludes the reconciliation relation entirely | `$V18E/account/models/account_move.py:3832-3842` | 0 hits for hash fields over `account_partial_reconcile.py` and `account_full_reconcile.py` | **HIGH** |
| C-07 | `payment.state` is a **computed** field that also drives its own dependencies, and is simultaneously **directly writable** | `$V18E/account/models/account_payment.py:48` (`readonly=False`) | `:411-425` mutual recursion with `account_move.py:1132-1219` | MEDIUM |
| C-08 | Two call sites of the same duplicate-detection method use **different state tuples**, one containing a value absent from the v18 selection | `$V18E/account/models/account_payment.py:753` | `$V18E/account/wizard/account_payment_register.py:889` (`'posted'`) vs the selection at `account_payment.py:38-51` | **HIGH** |
| C-09 | An identity constraint is enforced **database-globally** while its dedup filter runs with **no company domain at all** | `$V18E/account_bank_statement_import/models/account_bank_statement.py:14-19` | `.../account_journal.py:261-267` (`sudo()` search, no domain) | **HIGH** |
| C-10 | A **detection** query searches for repeats of an identifier the system's own filter is supposed to make unrepeatable | `$V18E/account_online_synchronization/models/account_online.py:284-306` | `.../account_journal.py:281-294` | MEDIUM |
| C-11 | A **payment token** is visible to a wider scope than the transactions made with it | `$V18E/payment/security/payment_security.xml:31-35` (`parent_of`) | `:14-18` (`in`) | **HIGH** |
| C-12 | `is_complete` on a bank statement compares a computed figure against a **default copy of itself** | `$V18E/account/models/account_bank_statement.py:189-192` | `:173-176` (`balance_end_real = balance_end`) | **HIGH** |
| C-13 | A guard asserting **same company** tests `root_id`; a matching domain in the same flow uses `child_of root_id` while another uses `child_of company_id` | `$V18E/account/models/account_move_line.py:2336-2340` | `$V18E/account/models/account_bank_statement_line.py:518` vs `:525` | **HIGH** (see §5) |
| C-14 | A guard admitting a bank account by company **explicitly skips** when the company is `False` | `$V18E/account/models/account_journal.py:469` | `$V18E/base/models/res_bank.py:86` (optional, derived) | **HIGH** |
| C-15 | Provider-fee support is **declared** in seed data with no implementing method | `$CUST18/payment_2c2p/data/payment_acquirer_data.xml:23-24` | `_send_refund_request` NOT FOUND in that module | MEDIUM |
| C-16 | An enterprise wizard exists and is wired in JavaScript, with **no Python producer** for the action that opens it | `$V18E/account_accountant_batch_payment/models/account_batch_payment_rejection.py:5-7` | `open_batch_rejection_wizard` — 2 hits, both JS | MEDIUM (see T-01) |
| C-17 | A batch reports **`reconciled`** while one of its members was rejected by the bank | `$V18E/account_batch_payment/models/account_batch_payment.py:120-123` | `$V18E/account/models/account_payment.py:1074-1075` | **HIGH** |
| C-18 | A QR code is marked **reusable** while carrying a fixed amount | `$CUST18/invoice_promptpay/models/account_move.py:67-68` | `:75` (tag 54) — and the reference does the opposite at `$V18E/account_qr_code_emv/models/res_bank.py:68` | **HIGH** |
| C-19 | A customer reference is computed **twice, differently**, in the same file | `$CUST18/invoice_promptpay/models/account_move.py:46-48` | `:77-79` | MEDIUM |
| C-20 | A module declares an external dependency, imports it, and does not use it | `$CUST18/invoice_promptpay/__manifest__.py:13` + `models/account_move.py:2` | the hand-rolled payload at `:66-85` | LOW |
| C-21 | A webhook returns **success** to the provider for a callback the state guard refused | `$V18E/payment/models/payment_transaction.py:794-805` | `$V18E/payment/controllers/` return paths | **HIGH** |
| C-22 | A raw `write()` overwrites `provider_reference` **even when the state transition was refused** | `$CUST18/payment_2c2p/models/payment_transaction.py:137-158` | `$V18E/payment/models/payment_transaction.py:781-805` | **HIGH** |
| C-23 | A field declared `Char` is assigned a dict | `$CUST18/payment_2c2p/models/payment_transaction.py:38` | `:140` | LOW |
| C-24 | Two modules declare the **same class name** with different `_inherit` targets, landing the same field on different models | `$CUST18/full_payment_custom/module/ir_action_report.py:6-8` | `$CUST18/print_payment_remittance_adviec/module/ir_action_report.py:7-8` | MEDIUM |
| C-25 | A module contains **two divergent copies** of the same override, only one imported | `$CUST18/hr_expense_petty_cash/models/account_move.py:10-20` | `models/account_invoice.py:10-20` + `models/__init__.py:4-7` | **HIGH** |
| C-26 | Assigning a payment account **silently changes** the target GL account's `reconcile` flag | `$V18E/account/models/account_payment_method.py:170-186` | — a configuration write mutating chart-of-accounts state | **HIGH** |
| C-27 | An import path **silently flips** an account's `reconcile` configuration and logs it at INFO | `$V18E/account/models/account_move_line.py:3106-3110` | — | **HIGH** |
| C-28 | A protected-field guard on an expense-linked payment omits two of its intended fields through a **missing comma** | `$CUST18/../hr_expense/models/account_payment.py:22-25` — but see T-03 | — | MEDIUM |

**Count: 28 Type I contradictions, of which 17 are rated HIGH.**
**DENOMINATOR:** POPULATION: contradictions surfaced by the eight evidence streams of this session over the S-01/S-02/S-03 path sets. UNIT: contradiction. **This is not a claim to have found every contradiction in the reference** — it is the set this session's declared searches surfaced. Class B for anything outside it.

---

## 3. Type II — implementation versus its own documentation

| ID | Where | What the documentation says | What the code does |
|---|---|---|---|
| D-01 | `$V18E/account/models/account_payment.py:70-73` | *"When an internal transfer is posted, a paired payment is created. They are cross referenced through this field"* | The field is **never written**. 2 occurrences tree-wide; no producer. |
| D-02 | `$V18E/account/models/account_payment.py:754-761` | duplicates "are not reconciled … represent a credit in the same account receivable … are in the suspense account" | **None of those conditions appears in the SQL** at `:788-806`. |
| D-03 | `$V18E/account_online_payment/__manifest__.py:4` | *"allows customers to pay their invoices online"* | The module is **outbound supplier payment initiation** through a bank aggregator (`models/account_batch_payment.py:22-27`). |
| D-04 | `$V18E/account/wizard/account_payment_register.py:566-577` | *"There are payments in progress. Make sure you don't pay twice."* | The field carrying it is **never read** by `_create_payments`. |
| D-05 | `$V18E/account/models/account_journal.py:182-184` | help text names a *"cash register"* | No cash register, session or till-close model exists outside point-of-sale. |
| D-06 | `$V18E/account_inter_company_rules/i18n/*.po` | catalogue entries for `field_account_payment__auto_generated` | **No corresponding Python** in this snapshot. |
| D-07 | `$CUST18/payment_2c2p/models/payment_transaction.py:147` | status `"001"` message is prefixed `Error:` | It maps to `_set_pending()` — a normal, non-error state. |

**Count: 7.** Every one of these would mislead a designer reading the model rather than the code. **D-01 is the most dangerous**, because it describes a control (paired transfer legs) that a treasury design would reasonably assume exists.

---

## 4. Type III — internal to this package, and between evidence sources

| ID | Contradiction | Resolution |
|---|---|---|
| T-01 | An enterprise wizard is present but its trigger is absent (C-16). **Two readings:** the evidence copy is an incomplete checkout, or the wizard is unreachable in this build. | **NOT RESOLVED.** Both readings are recorded. Resolve by diffing the module against a known-good 18.0 enterprise distribution. `P06-OQ-63`. This session does **not** choose. |
| T-02 | The newer-API custom provider copy carries a **lower** version string than the older-API copy (`1.0.1` < `1.0.2`). | **NOT RESOLVED.** Recorded as evidence. No deployment claim is made. |
| T-03 | The missing-comma finding (C-28) was reported by one evidence stream against `hr_expense/models/account_payment.py`. **That path exists in both `$V18E/hr_expense` and, by module name, in the custom scope.** The stream's own citation is to the reference tree. | **PARTIALLY RESOLVED.** The finding is retained with its citation as given, and flagged: **the exact tree must be re-confirmed before the finding is relied on.** `P06-OQ-80`. Recorded rather than silently attributed. |
| T-04 | The Bank Event Register declared **6 ingestion doors** in its denominator, then enumerated **7**. | **RESOLVED IN PLACE.** The correction is recorded inside that file rather than applied silently: the module-borne denominator is 6; the complete denominator including manual keying is 7. All downstream counts use 7. |
| T-05 | The Scope Ownership Matrix asserted **one** pre-correction `tenant` occurrence before the scan was run; the scan returned **two**. | **RESOLVED.** Corrected in place, with the correction itself recorded (Scope Matrix R-08). |
| T-06 | The repository's own process matrix has **no** bank/payment/reconciliation process, while the Boss prompt defines P06 as a process. | **NOT RESOLVED — this is a governance gap, not a technical one.** `P06-B-01`. |
| T-07 | Jira holds **0** ERPPLUS items matching the P06 domain, while a different project (`WCFDIG`) carries a family of Thai accounting report items that overlap it semantically. | **NOT RESOLVED. This session does not adjudicate whether WCFDIG scope binds SMEsPlus** — that is a Boss-level decision. Recorded as a pointer only. |
| T-08 | P01–P05 sibling packages were unpublished at fetch time, so every cross-process ownership assignment is a **proposal**, not a reconciliation. | **NOT RESOLVED — PEER DEPENDENCY OPEN.** Per CORR1 §7 this session does not stop for it. `P06-B-03`. |

---

## 5. Scope revalidation impact on this register (CORR1)

Per CORR1 §6, contradictions materially affected by the superseded "Tenant+Company everywhere" wording:

| ID | Pre-correction status | Post-correction status | Reason |
|---|---|---|---|
| C-13 | recorded as an unqualified same-company guard failure | **retained as a Type I contradiction, but its *severity as a defect* is now HOLD** | The two domains in the same flow (`root_id` at `:518` vs `company_id` at `:525`) genuinely contradict each other regardless of scope — that part stands. Whether the `root_id` guard is *wrong* depends on whether branch companies are one legal entity. SCOPE-F-04, `P06-B-27`. |
| C-14 | recorded as a company-boundary failure | **strengthened** | Under CORR1, unprovable ownership is a DENY condition. An unowned bank account is not merely a weak guard, it is an object that should not exist. |
| C-11 | not previously recorded as a contradiction | **newly raised** | Only visible once OWNERSHIP ≠ AVAILABILITY was applied. This contradiction was **produced by the correction**, and is the clearest evidence that applying it mid-session was worthwhile. |
| C-09 | recorded as a collision risk | **reframed and strengthened** | The contradiction is now correctly stated as *enforcement scope wider than the owner, with a filter narrower than nothing*. |

**No contradiction was withdrawn.** One (C-13) had its defect classification downgraded to HOLD while its status as a contradiction was retained — the distinction matters and is recorded deliberately.

---

## 6. Register discipline

Every entry above cites at least two independent locations, or one location plus a declared zero-hit search boundary. An entry that cannot do so is not a contradiction and does not belong here.

**Negative-claim audit:** this register was scanned as a named, separate step for the tokens `does not exist`, `there is no`, `never`, `always`, `only`, `nothing`, `anywhere`. Results are recorded in the PMO file. **No Class B, C or D negative in this package has been restated as Class A** — the restatement point is where the upgrade historically happens, and the summaries in the AAS+ and Handoff files were checked against this register, not against their own headline tables.

---

# End
