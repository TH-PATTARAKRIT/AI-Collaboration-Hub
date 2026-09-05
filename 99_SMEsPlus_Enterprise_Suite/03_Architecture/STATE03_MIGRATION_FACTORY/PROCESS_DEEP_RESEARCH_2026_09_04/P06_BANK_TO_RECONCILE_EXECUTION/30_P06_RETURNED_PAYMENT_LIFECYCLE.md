# P06_RETURNED_PAYMENT_LIFECYCLE.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION (CP-C09)
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. The seven concepts, separated

The prompt requires these classified separately, and they genuinely are different events with different accounting consequences.

| # | Concept | Business meaning | v18 reference | Custom estate |
|---|---|---|---|---|
| R-1 | **Post-dated cheque** | an instrument held, not yet presentable | **NOT FOUND** | v14: `post_dated_cheque_mgt_app` (16 `.py`), `pdc_generate_cheque_reference` — **not migrated** |
| R-2 | **Bounced cheque** | presented and dishonoured | **NOT FOUND** | v14 PDC app: state `bounced` |
| R-3 | **Returned bank transfer** | credited then reversed by the bank | **NOT FOUND** — no `payment.return` model, no return-reason code | v14: `account_payment_return` (OCA, "Mature") — **not migrated** |
| R-4 | **Failed electronic payment** | the instruction never executed | **PRESENT, thin** — `account.payment.state = 'rejected'`; `payment.transaction.state = 'error'` | — |
| R-5 | **Provider refund** | merchant-initiated return | **PRESENT** — `operation = 'refund'`, `action_refund`, `_send_refund_request` | — |
| R-6 | **Provider chargeback / dispute** | payer-initiated reversal | **NOT FOUND** | — |
| R-7 | **Payment reversal (accounting)** | correcting our own entry | **PRESENT** — `account.move.reversal`, `reversed_entry_id`, `payment_state = 'reversed'` | — |

**DENOMINATOR:** PATH SET `$V18E/{account, account_accountant, account_batch_payment, account_iso20022, account_online_synchronization, payment}`, `*.py`, `/tests/` excluded. PATTERNS per row. UNIT: model/field/state definition.
Token counts: `payment_return` **0** · `bounce` **0** · `dishonour`/`dishonor` **0**/**0** · `recall` **0** · `nsf` **0** · `insufficient` **0** · `chargeback|charge_back|dispute` **0**.
**Class A within that declared six-module scope.** Localisation packs were **not** searched — `P06-OQ-90` applies here too.

---

## 2. What `rejected` actually is

**RPL-F-01 — `account.payment.state = 'rejected'` is a status flag with no ledger consequence.**
`$V18E/account/models/account_payment.py:44` declares it; exactly one method sets it — `:1075-1076`:
```
def action_reject(self):
    self.state = 'rejected'
```
No accounting reversal. No journal entry. No statement line. No link to a returned bank item. No reason code. No bank reference. No timestamp beyond field tracking.
Its only downstream consumer is an **exclusion filter** — `$V18E/account_batch_payment/models/account_batch_payment.py:120`: `... p.state not in ('canceled', 'rejected'))`.

**RPL-F-02 — And that exclusion is the mechanism by which a batch reports success despite a failure.** Because rejected members are filtered out of the batch quorum, a ten-payment batch with one bank rejection still computes to `reconciled`. The flag that records the failure is the same flag that hides it from the batch state.
**Classification: FACT VERIFIED.** This is the cleanest single illustration of `P06-B-06` — the system has nowhere to put "the bank said no", so it puts it in a filter.

**RPL-F-03 — At the provider layer, a post-settlement reversal is indistinguishable from an authorisation failure.** `payment.transaction.state` has one `error` value (`$V18E/payment/models/payment_transaction.py:60-61`) with a free-text `state_message`. There is no distinct state for "settled, then reversed".

---

## 3. The lifecycle P06 must specify

A returned item is **not** a correction of our own entry. It is a **new external event that reverses a settlement we had already recorded as complete**. The reference conflates the two, which is why R-3 and R-7 collapse onto the same mechanism.

**Required lifecycle:**

```
 settled ──[external return event ingested]──> RETURNED
                                                 │
                     ┌───────────────────────────┼───────────────────────────┐
                     ▼                           ▼                           ▼
        obligation re-opened          return charge captured        cause recorded
        (residual restored)           (a bank fee — BA-01)          (reason code + bank ref)
```

**Non-negotiables:**
1. A return is **ingested**, never asserted internally. It is a bank event with its own identity.
2. The original settlement is **superseded, not erased**. Both must remain legible — the reference's `remove_move_reconcile` erases (attack A5).
3. The obligation's residual is **restored**, and the ageing restarts from the return date, not the original due date.
4. A return **carries a cause**: bank reason code, bank reference, return date.
5. A return frequently carries a **charge** — which lands in BA-01, the event with no owner.
6. `post-dated` is a **holding state before presentation**, not a return. It needs a maturity date and an ageing view.

---

## 4. Thai relevance, stated with its boundary

> **ALTERNATIVE READING, added by AAS-03 E3-C-02 and NOT disposed of.** Thai businesses demonstrably hold post-dated cheques. The platform modelling none may mean the capability is missing, or that it is handled outside the ERP by convention — a *business-process* finding rather than a defect. **P06 cannot distinguish these from source.** `P06-OQ-95`.

Post-dated cheques are ordinary Thai commercial practice, and the v14 custom estate implemented them at length — a delegated payment model with six state-transition wizards, plus a separate reference register.

**What is FACT VERIFIED:** those modules exist in the v14 tree; no counterpart exists in any of the three v18 custom roots under both a directory-name pattern and a model-name pattern (169 module directories, zero files).
**What is NOT established:** that the v14 modules were installed, used, or hold data. That is `P06-OQ-82`, answerable only from the v14 database.
**What is HOLD — STATUTORY EVIDENCE REQUIRED:** whether Thai law or accounting standards impose specific treatment for post-dated cheques or returned items. Routed to the Accounting-Tax track. This session takes no statutory position.

**The capability question stands regardless of past usage**, because the commercial practice is current. That is a business-semantics judgement, recorded as **SUPPORTED INTERPRETATION**, not as FACT VERIFIED.

---

## 5. Blocker impact

| ID | Status |
|---|---|
| `P06-B-34` post-dated cheque not migrated | **remains open — independently re-verified**; v18 reference confirmed to have no PDC concept at all |
| `P06-B-35` returned payment not migrated | **remains open — independently re-verified**; no `payment.return` model, no return-reason code, no chargeback concept |
| SSM-F-03 `rejected` carries no cause | **strengthened** — RPL-F-02 shows the flag actively conceals the failure at batch level |
| T-05 (missing returned-item transition) | **CONFIRMED as a gap**, with the required lifecycle now specified |
| `P06-OQ-90` | applies — `l10n_*` not searched |

---

# End
