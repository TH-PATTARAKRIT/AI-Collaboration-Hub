# P06_FAILED_PAYMENT_SEMANTIC_HARDENING.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S12)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Scope:** material delta only. `30_P06_RETURNED_PAYMENT_LIFECYCLE.md` stands.

---

## 1. What `rejected` carries — tested field by field

`$V18E/account/models/account_payment.py:44` declares it; `:1075-1076` is the only setter:
```
def action_reject(self):
    self.state = 'rejected'
```

| Does it preserve… | Answer |
|---|---|
| failure reason | **NO** |
| bank reason code | **NO** |
| provider response | **NO** |
| date of rejection | **NO** — only `tracking=True` on the state field, i.e. a chatter message |
| link to the original transaction | **NO** |
| retry history | **NO** |
| re-opened AR/AP | **NO** — the reconciliation is untouched |

**FPS-F-01 — `rejected` is a single enum value with no payload whatsoever.** It is not a boolean only because the selection has five members; semantically it carries exactly one bit more than a boolean.

**FPS-F-02 — And its only durable trace is deletable.** The rejection is recorded as a `tracking=True` chatter entry — a `mail.message` with a `mail.tracking_value`. Both are in `om_data_remove.remove_message`, and `mail_tracking_value` **cascades** from `mail_message` (`59_` DPG-F-03). **The one record that a payment was rejected is destroyed by an operation that does not name it.**

---

## 2. Does the flag make records vanish from business queues? — YES, and that is the sharp finding

**FPS-F-03 — `rejected` removes the payment from the batch quorum, so a batch containing a bank-rejected payment still reports success.**
`$V18E/account_batch_payment/models/account_batch_payment.py:120`:
```
... p.state not in ('canceled', 'rejected'))
```
The state computation filters rejected members **out** before testing whether all members are matched and sent. A ten-payment batch with one rejection computes to `reconciled`.

**The same flag that records the failure is the flag that hides it.** That is not a side effect — it is the only consumer of the value found in the searched scope.

---

## 3. Peer corroboration gained this round

| Source | Finding |
|---|---|
| **P07 `X-09`** | *"A reversal must not silently remove a row from an already-filed period"* — `A-09`: if a reversal returns the invoice to `not_paid`, the PND branch stops reporting it, **retroactively changing a filed period with no trace** |
| **P07 `A-15`** | *"the **reported** figure can change without any ledger change"* |
| **P08 `KRN-INV-01`** | the remedy: *"A **reversal** is a `K2` in its own right, **linked to the `K2` it reverses**"* |
| **P08 `P08-RQ-PC-09`** | *"a reversal is dated on or after the fact it reverses, or the operation is refused"* — because today *"A reversal takes any date the operator supplies, **including one earlier than the entry it reverses**"* |

**FPS-F-04 — Three processes independently require the same thing: a reversal must be a new, linked, dated fact.** P06's `P07-R-03`, P08's `KRN-INV-01`, P07's `X-09`. **That convergence is the strongest design signal in the peer round.**

---

## 4. Requirements — hardened

| ID | Requirement |
|---|---|
| `FPS-R-01` | A failure state carries a **cause, a counterparty reference, a timestamp and a link to the instruction that failed**. A bare enum is not a state. |
| `FPS-R-02` | A failure record is **not deletable** and is not a cascade target of any relation. |
| `FPS-R-03` | A failure **must not remove the item from any quorum, queue or completeness test**. It must make the aggregate fail, not disappear. |
| `FPS-R-04` | A failure **re-opens the obligation** and restarts its ageing from the failure date. |
| `FPS-R-05` | A reversal is a **new fact linked to the fact it reverses**, dated on or after it. *(Adopted from P08 `KRN-INV-01`.)* |
| `FPS-R-06` | Where a fact has been reported to an authority, a later failure produces a **new fact in a new period**, visibly linked — never a retroactive change. *(From P07 `A-09`.)* |
