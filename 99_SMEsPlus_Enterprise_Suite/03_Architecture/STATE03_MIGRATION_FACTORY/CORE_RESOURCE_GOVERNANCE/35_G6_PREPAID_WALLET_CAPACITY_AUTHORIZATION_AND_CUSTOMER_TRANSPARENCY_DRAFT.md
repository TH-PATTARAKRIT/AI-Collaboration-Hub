# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G6 — Prepaid Wallet, Capacity Authorization & Customer Transparency Draft

Status: DRAFT FOR SPECIALIST REVIEW AND INDEPENDENT CHALLENGE
Gate: G6 — Metering / Wallet
Owner: SaaS Team under SMEs Core
Final Approver: Boss only
Build / Merge / Production: HOLD

## 1. Purpose

Define a non-surprise, prepaid-first financial authorization model that prevents unsecured additional consumption, prevents wallet double-spend, preserves customer/business continuity, and keeps operational service-credit evidence separate from statutory accounting truth.

Mandatory inherited rules:
- Prepaid Before Usage for additional chargeable consumption.
- 30-Day Notice != 30-Day Credit.
- No Unsecured Postpaid Overage.
- No Surprise Billing.
- No Evidence = No Chargeable Usage.
- Wallet balance does not reset at billing period end.
- Usage counters may reset while historical evidence remains auditable.

## 2. Architecture Alternatives

### Option A — Mutable `wallet_balance` field as financial truth
Disposition: REJECT.
Reason: race conditions, weak auditability, poor dispute reconstruction, silent adjustment risk and no reservation lineage.

### Option B — Immutable operational wallet ledger + derived balances
Disposition: RECOMMEND.
Reason: supports credit/debit/reserve/release/adjustment history, concurrency control, dispute reconstruction and reconciliation while keeping current balances efficiently derivable.

### Option C — Treat wallet ledger as statutory GL/subledger
Disposition: REJECT for G6.
Reason: G1 explicitly separates Usage Evidence Ledger from accounting GL/subledger. Operational wallet evidence must reconcile to Accounting but cannot silently become statutory posting architecture.

### Option D — Allow postpaid settlement after variable usage
Disposition: REJECT as default additional-consumption model.
Reason: contradicts prepaid-before-usage and no-unsecured-postpaid invariants. Contractually secured Enterprise/reserved arrangements may use a separate secured authorization source, not an unsecured negative wallet.

## 3. Canonical Wallet Components

### 3.1 Wallet Ledger
Append-only operational service-credit records such as:
- FUNDING_CONFIRMED
- RESERVE
- RESERVE_RELEASE
- USAGE_SETTLEMENT
- BASE_SUBSCRIPTION_SETTLEMENT
- ADD_ON_SETTLEMENT
- REFUND / CREDIT_ADJUSTMENT
- DEBIT_ADJUSTMENT
- CHARGEBACK / FUNDING_REVERSAL
- EXPIRY only where contractually valid for a specific funding instrument; not assumed globally

Every entry links to source authorization/payment/order/usage/adjustment evidence and audit actor/system provenance.

### 3.2 Derived Balances
Conceptual, not implementation-specific:

`Funded / Secured Spendable Balance`
- `Settled Deductions`
- `Active Reserved Balance`
+/- `Approved Compensating Adjustments`
= `Available Balance`

Rules:
- Reserved Balance is not final consumption.
- Available Balance is the amount available for new authorization.
- Balance computation is currency-scoped.
- No silent cross-currency arithmetic.

### 3.3 Authorization Source
A chargeable workload may be covered by:
1. Prepaid Service Credit / Wallet;
2. prepaid Add-on / reserved capacity;
3. explicitly secured contractual credit/capacity approved under commercial policy.

Unsecured future payment expectation is not an authorization source.

## 4. Reservation State Machine

Candidate state machine:

`REQUESTED -> AUTHORIZED/HELD -> EXECUTING -> SETTLED`
with terminal alternatives:
`RELEASED / EXPIRED / CANCELLED / FAILED_RECONCILIATION / HELD_FOR_REVIEW`

Rules:
- authorization is atomic/fencing-equivalent against Available Balance so concurrent requests cannot double-spend the same credit;
- reservation has identity, Tenant, currency, workload reference, maximum authorized amount/quantity, created/effective/expiry time and rule version;
- retries use the same reservation/idempotency lineage;
- expiry cannot silently revoke an in-flight integrity-critical transaction; lease-aware handling follows G2;
- actual consumption is settled from evidence and unused reserved amount is released;
- reservation amount is not customer usage.

Exact database locking/isolation mechanism is not frozen.

## 5. Included vs Additional Consumption

### Included Entitlement
If usage is within active included entitlement and no separate charge is contractually required:
- meter for visibility/capacity governance;
- do not deduct wallet merely because raw resources were consumed;
- technical admission/fairness rules still apply.

### Additional Chargeable Usage
Before execution/activation:
- confirm event/workload classification;
- estimate bounded chargeable exposure where preflight is required;
- prove available prepaid/secured authorization;
- reserve required credit/capacity;
- execute with runtime checkpoints for material/unbounded work;
- settle measured actual consumption;
- release unused reserve.

## 6. Preventing Negative Wallet / Under-Reservation

No new variable chargeable workload may knowingly create unsecured negative Available Balance.

Controls:
- bounded non-interruptible work must reserve a safe maximum exposure before start;
- interruptible/heavy work must checkpoint and re-authorize before crossing remaining reservation;
- if actual demand accelerates, pause/defer optional work and require top-up/secured authorization;
- if a platform-required integrity completion must continue after an already accepted business transaction and additional customer authorization cannot be obtained safely, the platform must preserve business truth and may absorb the unavoidable platform cost rather than manufacture unsecured customer debt.

Numerical safety margins remain G8 evidence.

## 7. Funding Confirmation

Funding is spendable only when the approved payment/settlement policy considers it confirmed.

States may distinguish:
- PENDING FUNDING — not spendable by default;
- CONFIRMED FUNDING — spendable;
- REVERSED/CHARGEDBACK — compensating wallet entry, never history deletion.

Exact payment rails and settlement timing are outside G6 mechanism freeze.

## 8. Base Subscription / Rental

The recurring base subscription is a known commercial obligation and should be covered before the relevant service term according to contract.

Candidate control:
- forecast/reserve upcoming base rental from wallet where wallet-funded;
- notify projected insufficiency early;
- do not describe the 30-day forecast as a credit extension;
- grace/read-only/suspension sequence remains an open commercial/service-continuity policy and must not destroy customer data or accounting truth.

## 9. Wallet Depletion / Service Continuity

When Available Balance is insufficient:
1. deny/defer NEW optional/additional chargeable workload lacking authorization;
2. block activation of new paid Add-ons/reserved capacity until funded;
3. preserve already-settled customer data and audit history;
4. preserve integrity-critical completion where technically necessary and already committed, subject to physical safety;
5. apply Protected Mode deterministically rather than arbitrary whole-ERP shutdown;
6. customer exit/export/read access follows separate contract/data-right policy and cannot imply unlimited free heavy processing.

Whole-service suspension/read-only thresholds remain un-frozen pending commercial/legal/UX validation.

## 10. 30-Day Forecast Model

Primary policy: notify when forecasted insufficiency/depletion falls within 30 days.

Forecast inputs may include:
- Available Balance;
- Active Reservations;
- scheduled/base subscription obligations;
- current measured additional usage;
- recent burn rate;
- known scheduled heavy jobs/add-ons;
- seasonality/growth only when enough evidence exists.

Customer-facing forecast must expose confidence/quality where material and distinguish:
- current measured/settled amount;
- reserved/pending amount;
- estimated/projected amount;
- final closed statement amount.

No false precision: low-confidence forecasts should show uncertainty/range or a clear low-confidence status rather than a misleading exact date.

Exact smoothing/seasonality algorithm and reminder cadence remain open.

## 11. Customer Transparency Contract

Customer dashboard must be able to show:
- current Tier / Package;
- included entitlement and active Add-ons;
- current usage by customer-understandable unit;
- remaining included allowance;
- wallet currency and current spendable/available balance;
- active reserved balance and reason;
- current settled period cost/deductions;
- projected month-end usage/cost;
- projected insufficiency/depletion date;
- required/recommended top-up or Package/Add-on action;
- status of blocked/deferred actions and reason code;
- drill-down from statement/deduction to Usage Evidence lineage;
- data freshness / provisional/final status where appropriate.

Customer-facing raw CPU/RAM/DB/I/O complexity is not required unless contractually chosen as the commercial unit.

## 12. Dispute, Refund and Correction

- Never delete settled usage/wallet history to resolve a dispute.
- Corrections use explicit reversal/credit/debit entries linked to original evidence.
- Disputed items may be marked HELD/DISPUTED without rewriting source usage facts.
- Closed statement corrections create explicit adjustment lineage.
- Manual wallet adjustment requires reason, actor, authorization evidence and separation-of-duties controls appropriate to amount/risk.

## 13. Currency Rule

A wallet/funding instrument is currency-scoped.

No balance arithmetic may combine currencies without an explicit FX conversion event/rule and evidence. Final FX/tax/accounting policy is outside G6 and requires Accounting/Commercial review.

## 14. Third-Party / Pass-Through Services

Third-party services may create separately contracted chargeable units only if:
- customer disclosure exists;
- vendor/service identity is controlled;
- quantity evidence is trustworthy/reconcilable;
- duplicate/internal retry amplification is excluded;
- prepaid/secured authorization exists;
- failed/unaccepted service rules are explicit.

Raw vendor invoice/cost is not automatically the customer usage unit.

## 15. New Organization Hierarchy Application

Wallet owner = Tenant by default.

Organization Root / Company / Branch may be statement allocation dimensions. A Company/Branch cannot spend another Tenant's wallet or bypass Tenant authorization. Future sub-wallets, departmental budgets or cost centers require a separate controlled design; G6 does not invent them.

## 16. Draft Invariants

G6-W01 Wallet truth is append-only operational ledger + derived balances, not one mutable balance field alone.
G6-W02 Financial authorization must prevent concurrent double-spend.
G6-W03 Reservation != usage; settlement reconciles actual and releases unused reserve.
G6-W04 New additional chargeable usage cannot knowingly create unsecured negative balance.
G6-W05 Pending funding is not spendable until confirmed under policy.
G6-W06 Chargebacks/refunds/corrections are compensating entries, not historical rewrite.
G6-W07 Operational wallet ledger != statutory GL/subledger.
G6-W08 Wallet arithmetic is currency-scoped.
G6-W09 30-day forecast is preparation, not credit.
G6-W10 Protected Mode restricts new optional/growth work first where safe; it must not corrupt committed business truth.
G6-W11 Customer dashboard distinguishes measured/settled/reserved/projected/final states.
G6-W12 No wallet thresholds, auto-top-up, grace days, currency list, prices or suspension policy are frozen at G6 draft.

## 17. Open Items for Challenge

- exact auto-top-up policy;
- minimum reserve percentage/value;
- service grace/read-only/suspension sequence;
- refund/chargeback commercial treatment;
- tax/VAT/accounting recognition of service credit;
- FX handling;
- forecast algorithm and confidence model;
- notification channels/cadence;
- customer dispute SLA;
- payment settlement confirmation sources.
