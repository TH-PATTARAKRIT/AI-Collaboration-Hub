# P06_PAYMENT_PROVIDER_TRACE.md

**Session:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001 · **Process:** P06 Bank-to-Reconcile
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001 (base `88f52cd`)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Scope model:** `[SMEPLUS-26-09-04-ACC-REV2-CORR1]` applied.

---

## 1. The full trace

```
customer action → payment.transaction (state machine)
                        │  state = 'done'
                        ▼
                  _post_process           ← NOT called by the webhook (PPT-F-05)
                        │
                        ▼
                 _create_payment  →  account.payment  →  account.move  →  reconcile
                        │
                        ▼
              …later… bank statement line for the provider's settlement (net of fees)
```

**The single most important finding in this file is the gap on the third arrow.**

---

## 2. Transaction state machine

**PPT-F-01 — Six states, one guard function, five source-state tuples.**
`$V18E/payment/models/payment_transaction.py:58-62` — `draft, pending, authorized, done, cancel, error`.
All five setters delegate to `_update_state(allowed_states, target_state, state_message)` (`:678-750`):

| Setter | `allowed_states` |
|---|---|
| `_set_pending` | `('draft',)` |
| `_set_authorized` | `('draft', 'pending')` |
| `_set_done` | `('draft', 'pending', 'authorized', 'error')` |
| `_set_canceled` | `('draft', 'pending', 'authorized')` |
| `_set_error` | `('draft', 'pending', 'authorized')` |

**PPT-F-02 — Out-of-order and replayed callbacks are silent no-ops. The webhook still returns success.**
`$V18E/payment/models/payment_transaction.py:781-783` classifies three ways; only `to_process` is written. A same-state replay logs at INFO (`:788-793`); an **illegal** transition logs at WARNING (`:794-805`) — **no exception, no rollback, and the provider is told the callback succeeded.**
**Consequence:** a provider whose callback is rejected by the state guard has no way to learn it. From the provider's side the transaction is confirmed; from the system's side nothing happened. There is no reconciliation between the two views.

**PPT-F-03 — `error → done` is honoured; `done → anything` is refused.**
`done` appears as a source in no tuple. A confirmed transaction cannot be un-confirmed through the setters — but a late `done` after an `error` **is** accepted, and it resets the post-processing flag (`:806-811`, `'is_post_processed': False`) so accounting re-runs.

**PPT-F-04 — `extra_allowed_states=()` lets any subclass widen the guard per call**, including re-admitting `done` (`:667,684,701,719,737`). No caller in the searched scope uses it.

**PPT-F-05 — No amount or currency re-validation exists in the base state machine.**
PATTERN `amount|currency` inside `_update_state` and the `_set_*` bodies (`:667-834`): no comparison against notification data. Verification is delegated entirely to each provider module.

---

## 3. Where accounting is created — and where it is not

**PPT-F-06 — Only `done` triggers accounting.**
`$V18E/account_payment/models/payment_transaction.py:107` — `for tx in self.filtered(lambda t: t.state == 'done'):`. Draft invoices are auto-posted first (`:108-109`). `cancel` cancels an already-created payment (`:132-133`). **`pending`, `authorized` and `error` produce no accounting entry** — PATTERN for those states in `_post_process` (`:99-133`): NOT FOUND.

**PPT-F-07 — `_create_payment` creates AND posts AND reconciles in one call.**
`$V18E/account_payment/models/payment_transaction.py:196-197` — `payment = self.env['account.payment'].create(payment_values)` / `payment.action_post()`; reconciliation at `:207-213` matching on `payment.destination_account_id`.
Journal and company come from the **provider**, not from the invoice (`:161-162`).
Payment creation is guarded by three conditions (`:117-122`): not a validation operation, `not tx.payment_id`, and no settled child transaction.

**PPT-F-08 — THE CRITICAL FINDING: accounting is created OUTSIDE the webhook transaction.**
**DENOMINATOR:** POPULATION: all `.py`/`.xml`/`.js` under `$V18E/payment`. PATTERN: `_post_process`. UNIT: call site. **Non-test call sites = 3**, and **none is a provider notification path**:
1. **The customer's browser poll** — `$V18E/payment/controllers/post_processing.py:51-53`, on `/payment/status/poll`. The transaction is resolved **from the browser session** (`:24,82-90`, `MONITORED_TX_ID_KEY`), so a webhook-only completion with no returning browser never reaches it.
2. **The cron** — `$V18E/payment/models/payment_transaction.py:853-864`, one commit per transaction, rollback-and-retry on contention. Search key `is_post_processed = False`, retry window **4 days** (`:846-852`), cadence 10 minutes, and **it ships INACTIVE** (`$V18E/payment/data/payment_cron.xml:8-12`, `<field name="active" eval="False"/>`).
3. `account.payment.action_post` in the bridge, for the token-payment direction (§5).

`_handle_notification_data` (`:626-636`) does **not** call `_post_process`.

**Consequence — a real window, with a real upper bound.** Between the provider confirming and the accounting existing there is a period in which `payment.transaction.state = 'done'` and **no journal entry exists**. Its length is bounded only by the customer's browser returning, or by a cron that is **disabled by default**, over a 4-day retry horizon.
And that cron is itself toggled by provider state: `$V18E/payment/models/payment_provider.py:354-368` — if every provider is disabled the cron goes inactive and **no deferred accounting runs at all**.
**Classification: CONFIRMED DEFECT for P06 purposes.** Raised as `P06-B-30`.

---

## 4. Idempotency

**PPT-F-09 — Exactly one uniqueness constraint exists in the whole chain, and it is on the *internal* reference.**
**DENOMINATOR:** POPULATION: all `_sql_constraints` declarations under `$V18E/payment/models` + `$V18E/account_payment/models`. UNIT: constraint block. **TOTAL = 1**:
`$V18E/payment/models/payment_transaction.py:122-124` — `('reference_uniq', 'unique(reference)', "Reference must be unique!")`.

**PPT-F-10 — The PROVIDER's own reference has no constraint, no index, and is never read for matching.**
`$V18E/payment/models/payment_transaction.py:48-50` — `provider_reference` is a bare readonly `Char`.
PATTERNS `unique(provider_reference`, `unique (provider_reference`, `provider_reference_uniq` over the **entire `$V18E` tree**: **0 hits. Class A within that scope.**
And it is written but never used: PATTERN `provider_reference` over `$V18E/payment` + `$V18E/account_payment`, py+xml, excluding `/i18n/`: **3 occurrences** — the field definition, a form-view widget, and one f-string in the payment memo (`$V18E/account_payment/models/payment_transaction.py:150`). **No `search`, no domain, no constraint.**
**Two transactions can carry the same provider reference.** For a treasury process this is the identity that matters — it is the only thing a bank or provider settlement report will key on — and the system neither constrains it nor looks it up.

**PPT-F-11 — Reference generation is a non-atomic read-then-write.**
`$V18E/payment/models/payment_transaction.py:353-379` — a `search_count`, then a Python regex loop over an ORM search to find the highest sequence suffix. Concurrency is caught only by the `reference_uniq` constraint (PPT-F-09), which **raises rather than retries**.
A caller-supplied reference bypasses generation entirely (`:165-166`).

**PPT-F-12 — Webhook idempotency rests on two mechanisms, neither of them the provider reference.**
(a) the state guard, which no-ops a repeated `done` (PPT-F-02); (b) `not tx.payment_id` at `$V18E/account_payment/models/payment_transaction.py:119` — **an ORM read, not a database constraint.** Combined with PPT-F-08's separate-transaction execution, (b) is a read-then-write across transactions.

---

## 5. The reverse direction, and `account_online_payment`

**PPT-F-13 — Token payments post-process synchronously, and failures are cancelled rather than left draft.**
`$V18E/account_payment/models/account_payment.py:137-141` — `tx._send_payment_request()` then `transactions._post_process()`; `:146-149` — payments whose transaction did not reach `done` are `action_cancel()`ed.
One transaction per payment is enforced at application level only (`:185-189`).
Invoice ↔ transaction is **many-to-many** (`$V18E/account_payment/models/payment_transaction.py:12-15`).

**PPT-F-14 — `account_online_payment` is not part of this chain at all, and its manifest text is unreliable.**
`$V18E/account_online_payment/__manifest__.py:5` — `'depends': ['account_online_synchronization', 'account_batch_payment', 'account_iso20022']`. It does **not** depend on `payment` or `account_payment`.
It is **outbound** supplier payment initiation through the bank aggregator (`models/account_batch_payment.py:22-27,57-60`), despite a manifest summary at `:4` describing inbound customer checkout. **Treat that manifest text as unreliable.**
It carries its own status vocabulary with no overlap (`models/account_batch_payment.py:4-11,19`), its own cron (`:143-149`), and — notably — **the strongest guard in the whole payment domain**: `models/account_payment.py:11-13` — *"You cannot modify a payment that has already been sent to the bank."*
It also adds a wall-clock-derived ISO 20022 `end_to_end_id` (`:17-19`), truncated to the last 30 characters and recomputed on `journal_id` change — **not stable across recompute triggers.**
`'auto_install': True` (`__manifest__.py:16`) — it activates itself whenever its three dependencies are present.
PATTERN `payment.transaction|payment_transaction_id|payment.provider` over that module: **NOT FOUND.** There is no linkage between the two payment worlds.

---

## 6. The custom provider — `payment_2c2p`

Two non-identical copies exist. **No claim is made about which is deployed** (S-02 copy ambiguity; NC-05).

| | CUST18 copy | CUST14 copy |
|---|---|---|
| Version string | `1.0.1` | **`1.0.2` — higher** |
| API generation | `payment.provider` / `code` (v17+) | `payment.acquirer` / `provider` (pre-v15) |
| Install guard | asserts serie 18 (`__init__.py:30-34`) | none |
| Licence key | `Other proprietary` | **absent** |
| State transitions | via framework `_set_*` — **guarded** | **direct `state` write — UNGUARDED** |
| Amount re-validation | **absent** | **present** |
| Bad-signature handling | raises `ValidationError` | **logs a warning and continues** |
| Multi-match check | absent | present |
| Lookup key | `order_id` | `invoice_no` |
| Creates accounting | **no** | **no** |

**PPT-F-15 — The newer-API copy carries a LOWER version string than the older-API copy.** `1.0.1` (CUST18) versus `1.0.2` (CUST14). Recorded as evidence, not adjudicated.

**PPT-F-16 — The CUST14 copy bypasses the framework state machine entirely.**
`$CUST14/payment_2c2p/models/payment.py:199-222` writes `state='done'` directly. PATTERN `_set_transaction|_set_done|_set_pending|_set_canceled|_set_error` over that module: **NOT FOUND.** Every guard in §2 is absent on that path.
**And the v14 base `payment` module is not present in the evidence set** — `$CUST14/../payment` does not exist. So whether the v14 framework's `write()` intercepted a direct `state='done'` and fired post-processing **could not be verified**. This is the single most consequential open question in this file: it decides whether that copy creates accounting implicitly or not at all. **Class D**, `P06-OQ-50`.

**PPT-F-17 — The CUST18 copy verifies the signature, but with three weaknesses, each quoted.**
- Comparison is a plain `!=` on uppercased hex (`models/payment_transaction.py:123`); PATTERN `compare_digest`: **NOT FOUND** — not constant-time.
- The digest is built with `.get(k, '')` (`:62-63`), so **a missing field and an empty field are indistinguishable** in the signed payload.
- Missing-field validation uses `and` where `or` is required (`:107-114`), so a payload with a reference but no hash passes that check. The downstream effect is contained — a `None` hash still fails the comparison — but the check does not do what it reads as doing.

**PPT-F-18 — The raw `write()` after the setter is unconditional.**
`$CUST18/payment_2c2p/models/payment_transaction.py:137-158` — `provider_reference`, channel, raw response and `state_message` are written **even when the setter refused the transition**.
**Consequence: on a rejected or duplicate callback the state is correctly preserved, but the stored provider reference is overwritten with the LAST callback received — not the one that produced the `done`.** Given PPT-F-10 (the provider reference is the only key a settlement report can use), this quietly destroys the one field that could tie a confirmed transaction to a bank settlement line.
The raw response is stored in a field declared `Char` but assigned the whole notification dict (`:38`, `:140`) — the audit trail is a string coercion, not structured data.

**PPT-F-19 — The custom provider creates no accounting, so it inherits the PPT-F-08 window in full.**
PATTERNS `_post_process|_create_payment|account.payment|account.move` over both copies: **NOT FOUND.** The notify route returns `''` (`controllers/main.py:42`); the return route redirects to `/payment/status` (`:52`).
**For 2C2P, an accounting entry depends on the customer's browser reaching the status page, or on a cron that ships disabled.** A server-to-server notification alone never books anything.

**PPT-F-20 — Declared refund support is not backed by an implementation.** Seed data declares `support_refund = partial` (`data/payment_acquirer_data.xml:23-24`); PATTERN `_send_refund_request` over the module: **NOT FOUND.** Seed data also ships dummy credentials, and any provider state other than `enabled` — **including `test`** — routes to the demo host (`models/payment_provider.py:54-60`).

**PPT-F-21 — The CUST14 return route cancels a sale order on unverified input.**
`$CUST14/payment_2c2p/controllers/main.py:110-119` — on `payment_status == "003"` it browses `int(post.get("order_id"))` and calls `order.action_cancel()` **before** `to_c_to_p_validate_data(**post)` runs at `:119`. The cancel executes on attacker-supplied, unverified data.
**Classification: CONFIRMED DEFECT in that copy as read.** Deployment is not asserted. Raised as `P06-B-31`.

---

## 7. PromptPay and QR — print-only

**PPT-F-22 — Across all four QR modules examined, QR generation creates no payment and no bank event.**
**DENOMINATOR:** PATH SET: `$CUST18/invoice_promptpay`, `$CUST14/invoice_promptpay`, `$CUST14/l10n_th_promptpay`, `$V18E/account_qr_code_emv` (+ `$V18E/l10n_th`). PATTERNS: `payment.transaction|account.payment|payment.provider|payment.acquirer|account.bank.statement|_set_done|action_post`. UNIT: hit. **RESULT = 0 across the custom modules.** **Class A within that declared scope.**
The reference module's only database write is caching which QR method was used (`$V18E/account/models/account_move.py:5771-5774`).

**PPT-F-23 — The QR encodes the LIVE outstanding amount at render time, with no record of what was printed.**
Custom: `$CUST18/invoice_promptpay/models/account_move.py:30,74-75` uses `self.amount_residual`. Reference: `$V18E/account/models/account_move.py:5769` likewise.
**Two prints of the same invoice at different times encode different amounts, and nothing stores either.**

**PPT-F-24 — The custom module marks the QR REUSABLE while embedding an amount.**
`$CUST18/invoice_promptpay/models/account_move.py:67-68` — tag `01` set to `"11"`, with the in-code comment *"11 for reusable, 01 for one-time"* — while tag `54` carries the amount (`:75`).
The reference module does the opposite: `$V18E/account_qr_code_emv/models/res_bank.py:68` — `(1, '12'), # Dynamic QR Codes`.
**A reusable code carrying a fixed amount can be scanned repeatedly, and nothing in the system records or deduplicates the resulting credits.** Combined with A1 (four of seven ingestion doors attach no identity), a repeated PromptPay credit is indistinguishable from a duplicate import.

**PPT-F-25 — The customer reference embedded in the QR is computed twice, inconsistently.**
`$CUST18/invoice_promptpay/models/account_move.py:46-48` strips `/` from the move name; `:77-79` does **not**. The Odoo default move-name format contains `/` (e.g. `INV/2026/00001`).
**The reference a bank will report back is the tag-62 variant, which differs from the variant the module computes elsewhere.** Given that the reference string is the only link from a PromptPay credit back to its invoice (PPT-F-22), an inconsistent reference is the difference between automatic and manual matching.
The module also declares `promptpay` as an external dependency and imports it, then hand-rolls the payload without using it (`__manifest__.py:13`, `models/account_move.py:2`), and re-implements CRC-16 locally rather than calling the reference module (`:10-21`).

**PPT-F-26 — Thai PromptPay IS natively supported in the reference v18 line** via `l10n_th`, gated on `country_code == 'TH'` (`$V18E/l10n_th/models/res_bank.py:11,50,58`). The custom module duplicates a capability the platform already has, less correctly (PPT-F-24, PPT-F-25).

---

## 8. Scope determinations (CORR1)

| Object | Scope | Note |
|---|---|---|
| Provider *contract* | **HOLD** — plausibly TENANT | SCOPE-F-06 |
| Provider *settlement binding* | COMPANY | the money lands in one company's bank |
| Payment token | COMPANY-owned, **visible wider** | SCOPE-F-07, attack A4c |
| Payment transaction | COMPANY | derived from provider |
| Provider reference | COMPANY | **unconstrained** — PPT-F-10 |
| QR payload | COMPANY | encodes a company invoice |

---

## 9. Requirements arising

| ID | Requirement |
|---|---|
| PPT-R-01 | Accounting must be created in the same transaction as the confirmation, or a durable queue must guarantee it with a monitored age. Never a disabled cron plus a browser poll. |
| PPT-R-02 | The provider reference must be a constrained, indexed, searchable identity, and must never be overwritten by a later callback. |
| PPT-R-03 | A callback the state guard refuses must be surfaced, not logged and forgotten. |
| PPT-R-04 | Provider settlement must be decomposable into gross plus fee against a single bank credit (see FFI-R-03). |
| PPT-R-05 | Signature verification must be constant-time, must distinguish a missing field from an empty one, and must fail closed. |
| PPT-R-06 | No state may be written outside the guarded transition API. |
| PPT-R-07 | A QR carrying an amount must be one-time, and what was printed must be recorded. |
| PPT-R-08 | Reference construction must be single-sourced. |

## 10. Open items

| ID | Item | Class |
|---|---|---|
| P06-OQ-50 | Whether the v14 framework's `write()` fired post-processing on a direct `state='done'`. The v14 base `payment` module is absent from the evidence set. | D |
| P06-OQ-51 | Provider identifier stability across pending→posted is a provider-side contract not in the codebase. | D |
| P06-OQ-52 | Which copy of `payment_2c2p` and `invoice_promptpay` is deployed. Requires server config and the module registry. | D |
| P06-OQ-53 | The CUST18 module adds a `required=True` `provider_id` to `payment.method`; whether that conflicts with base seed data for other providers was not assessed. | C |
| P06-OQ-54 | `_get_invoice_next_payment_values`, driving the early-payment-discount branch of `_create_payment`, was not read. | C |

---

# End
