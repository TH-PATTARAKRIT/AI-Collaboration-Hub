# Source Map (candidate) — `account_payment_interco`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `account_payment_interco` |
| Display name | Intercompany Payment - Account |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `fc25ec23edf34500` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/account_payment_interco/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `account_payment`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / Enable Intercompany payments to reconcile with their invoices on post.
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `account.move`, `res.company`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `account.move`, `res.company`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 13 of 13 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: account_payment_interco ("Intercompany Payment - Account")
Source revision: 19.0.post20260921 (Odoo 19.0 Community). Pointers `module/path:LINE`; (TEST) = test-derived.
Manifest: summary "Enable Intercompany payments to reconcile with their invoices on post"; category Accounting; depends `account_payment`; no `auto_install` (installed on demand) (account_payment_interco/__manifest__.py:2-6).

## A. Capabilities
1. Settle an invoice/bill of company X that was paid online by a payment recorded in a different company Y of the same database. When the invoice is posted, the module creates clearing entries in both companies and reconciles them so the invoice shows as paid (account_payment_interco/models/account_move.py:30-37 trigger; :39-120 settlement).
2. Per-company configuration of the clearing journal and two clearing accounts (payable, receivable) (account_payment_interco/models/res_company.py:8-26), exposed in Accounting settings under default accounts, visible only to the multi-company group (account_payment_interco/views/res_config_settings_views.xml:8-13). Payable and receivable accounts are mandatory once a journal is chosen (:31-32,43-44).
3. CONDITIONAL: inert unless the conditions in B are all true; with no journal/accounts set nothing happens (account_payment_interco/models/account_move.py:11-13).

## B. Objects and flow (how inter-company payments are handled)
- Objects: account.move (invoice, bill, credit note), payment transactions linked to the invoice (owner account_payment, account_payment/models/account_move.py:16-19), the resulting account.payment, and two new journal entries per settlement.
- Eligibility filter (account_payment_interco/models/account_move.py:7-28): the move is an invoice-type document; payment state is not paid / partial / in payment; the invoice's company has a clearing journal; it has a transaction with a payment; the payment belongs to another company; direction check: customer-side documents need the invoice company's clearing receivable account and the paying company's clearing payable account, vendor-side documents need the reverse pairing; and at least one such payment is in state in-process or paid and its company has its own clearing journal.
- Trigger point: right after a move is posted (`_post`), for transactions in state authorized or done (:30-36). Upstream, the payment module posts draft invoices when a transaction is confirmed and reconciles payments with invoices (account_payment/models/payment_transaction.py:98-108,192-204), which is what reaches this hook (TEST sequence: payment posted, transaction set done and post-processed, then invoice checked, account_payment_interco/tests/test_interco_clearing.py:178-215,218-255).
- Step 1, in the paying company: for each payment, a clearing entry in that company's clearing journal moves the payment's counterpart balance (partner account) to that company's clearing account (payable for sales documents, receivable for purchase documents), with the invoice company's partner as counter-party, and is reconciled with the payment's counterpart line (:45-82).
- Step 2, in the invoicing company: an entry "Interco Settlement - <payment memos>" in its own clearing journal posts the invoice's total receivable/payable balance against its clearing account (partner = paying company) and reconciles the partner-account line with the invoice's receivable/payable lines (:84-120).
- Resulting state (TEST): invoice payment state "paid" and its receivable/payable line reconciled; both entries posted; entry lines carry label "<partner> / <document>", balance sign +/- by direction; payment's destination line reconciled with zero residual (test_interco_clearing.py:128-172). Test scenario spans two companies with different currencies (KES/USD) and conversion (:38,57-60,65-76,100-107).
- Lifecycle changes: only the invoice payment state changes as a result of reconciliation; the module adds no new state. The clearing entries are posted immediately (:80,117).

## C. Validations, automation, security, multi-company
- No constraints or exceptions raised by module code; ineligible moves are silently skipped (:33).
- Settings-level guards: journal domain type "general" with company check; account domains require reconcilable payable / receivable types (account_payment_interco/models/res_company.py:8-26).
- Elevated access: eligibility and transaction lookup are done on an elevated (sudo) recordset (account_payment_interco/models/account_move.py:33,35); the clearing methods are then invoked on those records, so cross-company postings likely run with elevated rights (inference from code; no test of a restricted user).
- Company handling: entries are created under the target company context (`with_company`) for each side (:57,96). Multi-company implications: both companies must be configured (journal + the relevant account) or the filter excludes the invoice (:11-27); currency handling uses payment currency on the paying side and invoice-company currency on the invoicing side (:66,105,112).
- No record rules, ACL or groups of its own; settings block restricted to `base.group_multi_company` (views :12).

## D. Handoffs
- account_payment owns payment transactions and their post-processing; account owns entries, reconciliation and payment states; payment module owns provider/transaction states (authorized/done).
- Accounting effects: two posted entries per settlement, one per company, with inter-company clearing balances left open in accounts to be netted by the group (nothing in the module nets them: UNKNOWN — EVIDENCE INSUFFICIENT).
- Approval: none. Audit trail: entries reference the payment memo / settlement memo (:60,99). No external integration or event emission.
- Sale/purchase are used only in tests to create documents (test_interco_clearing.py:179,219 `ensure_installed`); the manifest does not depend on them.

## E. Configuration that changes outcomes
- Company fields: clearing journal, payable account, receivable account, on each participating company (account_payment_interco/models/res_company.py:8-26; related settings fields account_payment_interco/models/res_config_settings.py:7-24).
- Outstanding-account setup on payment method lines and provider journal decide payment state in-process vs paid (TEST helper :19-30); multi-currency rates on both companies (TEST :65-76).

## F. Effective extension path
- Extends account.move, res.company, res.config_settings. No other Community module depends on it or references the `account_interco_*` fields (grep of manifests and sources); extenders: none found.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: partial payments and exchange-difference handling; the settlement amount is taken from the invoice's receivable/payable line balances (:85-88,106-113) rather than from the payment amount.
- UNKNOWN — EVIDENCE INSUFFICIENT: treatment of refunds/credit notes beyond the code branches (:14-22); no test covers them.
- UNKNOWN — EVIDENCE INSUFFICIENT: how the group nets the residual inter-company clearing balances and any Enterprise consolidation behaviour.
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour if the invoice is posted before the payment exists (only the "payment already recorded, invoice posted later" ordering is exercised by the hook).

