# P06_SOURCE_LINK_REGISTER.md

**Session ID:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001
**Process:** P06 — Bank-to-Reconcile (Treasury / Settlement / Reconciliation)
**Mode:** /L99999.99999
**Repository:** TH-PATTARAKRIT/AI-Collaboration-Hub
**Canonical branch:** SMEsPlus
**Working branch:** research/account-p06-bank-to-reconcile-2026-09-04-001
**Branch base commit:** `88f52cd7ba6dc40b8951c4bfc4e0016af7cbb7ad` (origin/SMEsPlus, "governance: approve canonical evidence acquisition flow")
**Date:** 2026-09-04
**Classification:** **LAYER 2 — AUDIT QUARANTINE.** This package cites reference-ERP `file:line` and verbatim source fragments. It is Boss / PMO / AI-Audit only. It MUST NOT be transcribed into any Layer 1 clean-room reference package or any Team B handoff.

---

## 1. Purpose

This register declares **every** evidence source consulted by session P06, the **exact search boundary** applied to each, and the **class** of any negative claim derived from it. It is the controlling denominator document for the whole P06 package. No finding in any other P06 file is admissible unless its source appears here.

---

## 2. Evidence Layer Model

| Layer | Meaning | P06 use |
|---|---|---|
| L2-SRC | Reference-ERP source tree (read-only, on this workstation) | Primary evidence for all behavioural findings |
| L2-CUST | Project custom addon source (multiple non-identical copies) | Primary evidence for delta findings; deployment NOT determinable |
| L2-RUN | Runtime extracts captured from a live UAT database | Configuration evidence only |
| L1-REPO | This repository's own governance/specification documents | Scope, ownership and gap evidence |
| EXT-JIRA | Jira site `scgl.atlassian.net` | Work-item existence evidence |

---

## 3. Source Register

### S-01 — Reference ERP v18 Enterprise source tree
- **Path root (`$V18E`):** `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons`
- **Layer:** L2-SRC
- **Build identifier as recorded in the path:** `18.0+e.20250608`
- **Access verified:** 2026-09-04, by directory listing.
- **Modules in scope for P06 (PATTERN: `ls $V18E | grep -iE "^account|^payment|bank|recon|check|batch"`), 57 directory hits, of which the P06-relevant PATH SET is:**
  `account`, `account_accountant`, `account_payment`, `payment`, `account_batch_payment`, `account_accountant_batch_payment`, `account_check_printing`, `account_accountant_check_printing`, `account_bank_statement_import` (+ `_camt`, `_csv`, `_ofx`, `_qif`), `account_bank_statement_extract`, `account_online_synchronization`, `account_online_payment`, `account_iso20022`, `account_qr_code_emv`, `account_auto_transfer`, `account_inter_company_rules`, `account_reports`, `account_reports_cash_basis`, `account_followup`, and the `payment_*` provider set (`adyen, aps, asiapay, authorize, buckaroo, custom, demo, flutterwave, mercado_pago, mollie, nuvei, paypal, razorpay, razorpay_oauth, stripe, worldline, xendit`).
- **DENOMINATOR DECLARATION —** POPULATION: directories directly under `$V18E`. PATTERN: the grep above. PATH SET: `$V18E` only, depth 1. UNIT: addon directory. **Modules outside this pattern were not enumerated for P06 and any negative derived from this set is Class B, not Class A.**

### S-02 — Project custom addon set, v18 line
- **Path root (`$CUST18`):** `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/smeplus-custom/addons`
- **Layer:** L2-CUST
- **Population:** 68 entries at depth 1 (UNIT: directory or archive entry; `ls | wc -l` on 2026-09-04).
- **P06-relevant subset (PATTERN `grep -iE "bank|pay|recon|cash|chq|cheque"` plus manual inclusion of date/posting-control modules):**
  `account_payment_multi_deduction`, `dev_print_cheque`, `full_payment_custom`, `hr_expense_petty_cash`, `invoice_promptpay`, `payment_2c2p`, `print_payment_remittance_adviec`, `scgl_purchase_advance_payment`, `cr_effective_date_entries`, `scgl_tax_period_date`, `automatic_invoice_and_post`, `cap_auto_invoice`, `l10n_th_withholding_tax*`.
- **KNOWN COPY AMBIGUITY (carried forward, NOT resolved by this session):** near-identical custom copies also exist at `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/custom/addons` and `/Volumes/iMacSys/CLAUDE AI/MIGRATION/ODOO18/18.0.4_smeplus_v2/addons`. **Which copy is deployed is unknown to this session.** Every custom-module finding in this package is therefore qualified "as read from the stated copy" and none asserts deployed behaviour.

### S-03 — Legacy v14 tree (project custom modules)
- **Path root (`$CUST14`):** `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo14/addons`
- **Layer:** L2-CUST
- **P06-relevant subset (same PATTERN as S-02):** `account_payment_multi_deduction`, `account_payment_return`, `cheque_control`, `dev_print_cheque`, `dev_purchase_down_payment`, `hr_expense_petty_cash`, `hr_expense_petty_cash_sequence`, `invoice_promptpay`, `l10n_th_promptpay`, `om_account_bank_statement_import`, `om_hr_payroll`, `om_hr_payroll_account`, `payment_2c2p`, `pdc_generate_cheque_reference`, `post_dated_cheque_mgt_app`, `print_payment_remittance_adviec`.
- **Use:** establishes the *v14 → v18 migration delta* for the treasury domain. Presence in v14 and absence from the S-02 pattern hit-list is reported as **Class B (not found in searched scope)**, never as "removed".

### S-04 — Runtime bank-journal extract, live UAT
- **File:** `~/Downloads/OCC/OCC_JOURNAL_BANK_RUNTIME_VERIFIED_C1_C2_v2.3_L99.99.csv`
- **Layer:** L2-RUN
- **Content:** 12 bank journals across 2 companies (C1: 6 journals; C2: 6 journals), each with runtime journal id, legacy default account, physical bank account number, and target GL account. Status column reads `VERIFIED_LIVE_UAT` on all 12 rows.
- **Source basis stated inside the file:** `account.journal (2).xlsx + account.account(1).xlsx`.
- **DENOMINATOR:** POPULATION: rows in that CSV. UNIT: bank journal. PATH SET: that one file. **This is NOT a complete census of bank journals in the live system — it is the census of what that extract contains.** Any claim of the form "the system has N bank journals" is Class B against this source.
- **PII CONTROL:** the file contains real bank account numbers. They are **not** reproduced in any P06 deliverable; findings reference journal code only.

### S-05 — This repository's specification baseline
- **Path:** `99_SMEsPlus_Enterprise_Suite/` at branch base `88f52cd`.
- **Layer:** L1-REPO
- **Files read:** `BOOT_SEQUENCE.md`, `AI_SESSION_BOOTSTRAP.md`, `REGISTER_INDEX.md`, `END_TO_END_BUSINESS_PROCESS_MATRIX.md`, `MODULE_SPEC_ACCOUNTING.md` (index-level), `CROSS_MODULE_DEPENDENCY_MATRIX.md` (index-level).
- **Search executed:** `grep -rn -iE "bank.to.reconcile|\bP06\b" --include="*.md" --include="*.yaml"` over the entire checkout at `88f52cd`.
- **Result:** **0 hits.** DENOMINATOR: POPULATION: all `*.md` and `*.yaml` files tracked at `88f52cd`. PATTERN: as shown. PATH SET: repository root, recursive. UNIT: matching line. **Class A negative within that declared scope:** the identifier "P06" and the phrase "Bank-to-Reconcile" are not present in the canonical branch at `88f52cd`. This does **not** mean the process is undefined elsewhere — see S-07.

### S-06 — Jira, site `scgl.atlassian.net`
- **Cloud id:** `67b5858f-f930-4950-af26-aa7662000e77`
- **Connectivity:** verified live on 2026-09-04 by an authenticated user-info call (account `712020:78643345-6186-4c7c-a0e5-822018bc6913`). **This session did not inherit any prior session's "unauthorized" status; it tested and obtained access.**
- **Query 1 (population):** `project = ERPPLUS` → **totalCount = 146** issues.
- **Query 2 (P06 relevance):** `project = ERPPLUS AND (summary ~ "bank" OR summary ~ "payment" OR summary ~ "reconcil" OR summary ~ "treasury" OR summary ~ "settlement" OR summary ~ "cash")` → **totalCount = 0**.
- **DENOMINATOR:** POPULATION: 146 ERPPLUS issues. PATTERN: the six `summary ~` terms above. PATH SET: project ERPPLUS, summary field only. UNIT: issue. **Class A within that scope:** as at 2026-09-04 there is no ERPPLUS work item whose *summary* names bank, payment, reconciliation, treasury, settlement or cash. **Class B for anything wider:** description/comment bodies were not searched, and other projects (BHPICL, VING, WCFDIG) were not enumerated for P06.
- **Observed adjacent evidence (free-text query across all visible projects):** project `WCFDIG` carries a family of Thai-language accounting report items including receipt-book, payment-book, cash-balance and bank-receipt-correction reports (e.g. `WCFDIG-22`, `WCFDIG-23`, `WCFDIG-44`, `WCFDIG-21`, `WCFDIG-3x`). These belong to a **different programme** and are recorded here as a pointer only. **This session does not adjudicate whether WCFDIG scope binds SMEsPlus** — that is a Boss-level decision.

### S-07 — The P06 process definition itself
- **Only source:** the Boss session prompt `[SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001]` that opened this session.
- **Finding:** the "P0x" process taxonomy (P01…P06) exists in the **prompt stream**, not in the repository at `88f52cd`. See S-05 and the cross-process ownership file.
- **Sibling sessions:** working clones for P01 (P2P), P02 (O2C), P03 (M2C), P04 (A2R) and P05 (E2P) exist on this workstation, each on its own `research/account-p0N-*-2026-09-04-001` branch created from the same base `88f52cd`. **A remote check on 2026-09-04 (`git ls-remote --heads origin "refs/heads/research/*"`) returned 10 `research/*` heads, none of them `research/account-p01…p05-*`.** DENOMINATOR: POPULATION: remote heads under `refs/heads/research/`. PATTERN: that refspec. UNIT: ref. **Class A within that scope and instant:** the P01–P05 packages were unpublished at the time of this fetch. Class B thereafter — they may publish at any moment, and this package must be re-checked against them before any cross-process closure.

---

## 4. Sources Deliberately NOT Consulted (Class C — not yet searched)

Declared so that no later summary can silently upgrade a Class-C to a Class-A.

| Ref | Source | Why not consulted |
|---|---|---|
| NC-01 | Live UAT / production database (any direct query) | No database connection was attempted or available to this session. All runtime evidence is second-hand via S-04. |
| NC-02 | Reference-ERP v19 line | Out of scope; the target generation for this programme is the v18 line per S-01. |
| NC-03 | Bank host-to-host / ISO 20022 counterparty specifications from any Thai bank | Statutory/contractual documents not held on this workstation. Any claim about what a Thai bank actually transmits is **HOLD / EVIDENCE REQUIRED**. |
| NC-04 | Thai statutory requirements for bank reconciliation retention, cheque handling, or e-payment recordkeeping | Routed to the Accounting-Tax track. Marked HOLD throughout this package. |
| NC-05 | `t8master` and `18.0.4_smeplus_v2` custom copies, read in full | Only version strings and presence were compared; full behavioural diff of every copy was not performed. |
| NC-06 | Jira description and comment bodies across all projects | Only `summary` was pattern-matched (S-06). |
| NC-07 | Confluence space content | Not searched. |

---

## 5. Negative-Claim Discipline Applied

This package applies `SMEPLUS_DEEP_RESEARCH_NEGATIVE_CLAIM_STANDARD` classes:

- **A** — verified absence *within a stated scope*
- **B** — not found in searched scope
- **C** — not yet searched
- **D** — unknown
- **E** — contradicted

Rule enforced: **B, C and D are never restated as A**, including in summary tables, gate reports and the handoff pack. A named negative-claim audit step is recorded in the PMO file.

---

## 6. Register Integrity

Any P06 finding citing a path not listed in §3 is **inadmissible** and must be raised as a contradiction. Any negative claim in this package that does not carry a class letter and a declared boundary is a defect of this package, not of the system under study.

---

# End
