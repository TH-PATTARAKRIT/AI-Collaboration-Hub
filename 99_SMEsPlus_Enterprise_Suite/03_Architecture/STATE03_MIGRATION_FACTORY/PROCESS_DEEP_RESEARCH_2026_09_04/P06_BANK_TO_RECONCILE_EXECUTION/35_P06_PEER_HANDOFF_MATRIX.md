# P06_PEER_HANDOFF_MATRIX.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION (CP-C11)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Constraint observed:** *"Do NOT adjudicate peer architecture."* Every entry below states P06's position and the peer's position; where they differ, **both stand** and the matter is routed.

---

## 1. Peer population, verified

`git ls-remote --heads origin "refs/heads/research/*"` → 19 refs. The process subset:

| Process | Branch | Read? |
|---|---|---|
| P01 Procure-to-Pay | **NOT PUBLISHED** | **PEER DEPENDENCY OPEN** |
| P02 Order-to-Cash | `research/account-p02-order-to-cash-2026-09-04-001` | **read** |
| P03 Manufacture-to-Cost | `…p03-manufacture-to-cost…` | **read** |
| P04 Acquire-to-Retire | `…p04-acquire-to-retire…` | **read** |
| P05 Expense-to-Pay | `…p05-expense-to-pay…` | **read** |
| P06 Bank-to-Reconcile | `…p06-bank-to-reconcile…` | this session |
| P07 Thai Tax-to-Compliance | `…p07-th-tax-compliance…` | **read** |
| P08 GL / Record-to-Report | **NOT PUBLISHED** | **PEER DEPENDENCY OPEN** |
| P09 Plan-to-Analyze | `…p09-plan-to-analyze…` | **read** |
| P10 Time-Based Recognition | `…p10-time-based-recognition…` | **read** |
| P11 Central Core Reconciliation | `research/account-core-reconciliation-2026-09-04-001` | **read** |

**7 of 9 peers read. P01 and P08 remain unpublished.**
**This closes the greater part of `P06-B-03`**, which at prior close was total.

---

## 2. THE MATERIAL FINDING — P11 already ingested P06, and it reverses P06's assumed position

**PH-F-01 — P06 is a PRODUCER of accounting events, not only a consumer. P11 says so explicitly, and P06's own package did not.**
`P11_SETTLEMENT_RECONCILIATION_ARCHITECTURE.md` §1:
> *"Reconciliation is a **producer** of accounting events, not only a consumer. Three accounting events are emitted **by the act of matching**: the exchange difference, its reversal on unmatch, and cash-basis tax recognition."*
> *"`P06` is therefore not a downstream consumer of `P02` and `P01`. It is a producing process … and **it owns none of the three events it emits**"*

P06's own Cross-Process Ownership file framed P06 as terminal — *"P06 owns nothing else"*. **That framing is incomplete and is corrected here.** P06 emits three accounting events, and P11 assigns their ownership to the ledger rather than to P06.

**P06's position:** it accepts the producer characterisation as correct and better than its own. It does **not** contest P11's ownership assignment for `UBE-36` (FX at settlement) and `UBE-38` (cash-basis tax at settlement) — P06's own Event-to-GL Matrix already recorded FX gain/loss as *"ASSIGNED — the account determination is a company/journal configuration owned by Core Accounting; P06 only triggers the event."*
**Recorded as CONVERGENT, not as a conflict.** Where P06 must be sharper: an event P06 *emits* but does not *own* still requires P06 to name its recognition date and its owning process — which is exactly what P11's `SRP-05` demands.

**PH-F-02 — P11 has `P06-B-27` on its own minutes-to-close list, and this continuation has closed it.**
`ACCOUNTING_BOSS_FINAL_GATE_PACK.md` decision `D-3`: *"Authorise the four UAT queries — `Q-04`, `Q-01`, `Q-02`, **`P06-B-27`**"*.
**`P06-B-27` is now CLOSED — SOURCE EVIDENCE VERIFIED, without a UAT query**, because the answer is in the model definition rather than the data. P11 may strike it from `D-3`. See `22_` and `23_`.
**This is the single most useful thing this continuation returns to the programme.**

---

## 3. THE ONE TRUE CONTRADICTION — P06 versus P02, unregistered anywhere

**PH-F-03 — P02 publishes the opposite verdict on P06's headline finding, tagged `FACT VERIFIED`.**

| | Claim |
|---|---|
| **P06 headline (i)** | the four states are **not independent**; there is **no bank-confirmation field** |
| **P02 `P02-F-43`** | *"The reference process **does** keep these separate, and does it well … **This separation must be preserved in SMEsPlus.**"* — `09_P02_PAYMENT_RECONCILIATION_MATRIX.md` §1 |

**P02's own package supplies the reconciliation**, in the very next section — `P02-F-44`:
> *"**A payment may post no journal entry at all** … the intermediate state disappears entirely — the payment is **declared matched at creation**; the 'money received but not yet cleared' position **does not exist**; **bank reconciliation has nothing to reconcile.**"*

**P06's assessment:** the two packages are describing **the same four-branch mechanism** (`account_payment.py:436-455`) and reaching different verdicts because they weight different branches. P02 evaluates the **outstanding-account configuration**, where the separation is real and works. P06 evaluates **all four branches**, three of which defeat it. Both are correct within their stated configuration; **neither headline is correct unconditionally.**

**The precise reconciliation P06 proposes, and does not impose:**
> The separation of payment / posting / bank-confirmation / settlement **exists only in the outstanding-account configuration**. In the direct-to-bank configuration it collapses at creation. Therefore it is a **configuration-dependent property, not a system property** — and a design may not rely on it without mandating the configuration.

**Status: NOT REGISTERED ANYWHERE.** `P11_CONTRADICTION_REGISTER.md` runs `P11-C-01`…`P11-C-07` and has no row for it, because P11 ingested P02 and P06 in separate deltas and did not cross-read them.
**P06 raises it as `P06-XC-01` and routes it to P11 as a candidate `P11-C-08`.** P06 does **not** adjudicate it.

---

## 4. Corroboration P06 gained from peers

Each of these is a peer finding that **independently supports** a P06 finding, reached from different evidence.

| P06 finding | Peer corroboration |
|---|---|
| A4a / B-27 — reconciliation crosses the company boundary | **P02 `SF-06`**: *"**Reconciliation crosses legal entities on a shared root** … Journal items of two different legal entities that share one root are reconcilable."* **P02 reached this independently and states the legal-entity consequence outright.** Strong corroboration of `22_`'s conclusion. |
| A6 — reconcile/unreconcile outside the close regime | **P02 `P02-F-46`** (tolerance-zero): *"The unreconcile path is not lock-date gated … **zero** call sites in the partial-reconciliation model."* Independent derivation with the same denominator. |
| A6 — same | **P09 `CN-06`**: a posted entry is protected by a lock date, a tax lock, **a reconciliation guard** and a hash chain — and the management allocation is in none of them. A second class of unbound fact. |
| PC-F-05 RELOCATE | **P04 `P04-F-61`**: a depreciation entry aimed at a locked period is *"silently **re-dated forward**, not rejected … **the hard lock is covered too**"*, and critically — *"**The silent re-dating is the accounting core's generic posting routine.**"* **This generalises P06's finding: RELOCATE is not a reconciliation quirk, it is the core posting behaviour.** |
| PC-F-02 lock inheritance | **P04 `P04-B-43`**: the effective hard lock is *"the **maximum over the whole parent chain**, computed with elevated privilege and **including archived companies**"*, irreversible. **Extends P06's finding with two facts P06 did not have: elevated privilege, and archived companies.** |
| Headline (iii) identity fails open | **P11 Delta 01 §3.2** adopts P06's `H-03` verbatim as *"the mechanism P11 could only name"*. Escalated to `P11-B-02`, *"the root"*. |
| Headline (iii) | **P05 `SR-07`**: *"the reconciliation identity is not stable"* — convergent from the expense side. |
| Headline (i) | **P05 `SR-01`**: *"Settlement status on this branch is an **assumption, not an observation**"* — the expense-side instance of P06's `is_matched` finding. |
| FX at settlement | **P02 §4**: a **two-stage** silent fallback — the latest rate on or before the date, then *"the **earliest rate of ANY date, with no date filter at all**"*, then 1.0. *"**None of the three paths logs, warns, or raises.**"* **P06 documented four parity fallbacks; P02 supplies the more dangerous middle arm P06 missed.** |
| CPO-F-01 no process taxonomy in the repo | **P03 §7** independently derived. Registered by P11 as `P11-F-04`. |
| Write-off account unconstrained | **P02**: *"**The write-off account is unconstrained** … Nothing prevents writing an unrecoverable receivable off to a **revenue** account."* |

**PH-F-04 — Nine independent corroborations. Not one peer contradicted a P06 finding on the merits.** The single conflict (PH-F-03) is a verdict difference over a shared mechanism, not a disputed fact.

---

## 5. New evidence P06 must absorb from peers

**PH-F-05 — P05 supplies an eighth ingestion/settlement door P06 did not count.**
`08_P05_SETTLEMENT_RECONCILIATION.md` `SR-04`: the advance cash-return path *"creates a journal entry against the payment journal's default account **without an `account.payment`**. The cash movement **will not appear in payment listings, payment-based reports, or the bank-reconciliation matching model that keys on payments.**"*
**Consequence for P06:** cash can move through a bank journal with **no payment object at all**, invisible to the matching model. This is a settlement door outside all seven P06 enumerated. **`P06-B-53`**, and the door denominator must be reopened at P11.

**PH-F-06 — P05 concedes it creates and posts payments it does not own.**
`09_P05_CROSS_PROCESS_OWNERSHIP.md`: *"| **Payment execution** | **No — settlement/treasury owns it** | P05 nevertheless **creates and posts** payments on the company-paid branch, at approval | … | **HIGH** — `EX-03` |"*
And P11 assigns `UBE-33` *"Employee reimbursed"* to **P06**.
**So P06 owns a payment door that P05 operates.** This is `P06-B-04` (four payment-intent entry points) confirmed from the other side, with an owner now named.

**PH-F-07 — P09 makes a class-B claim about P06's own widget that P06 should answer.**
`09_P09_CROSS_PROCESS_OWNERSHIP.md`: for P06, an analytic value is *"copied from the matched ledger row where one exists, else from rules"*, and *"**can a later step change it silently? YES**, same overwrite shape; **not independently traced for a state guard — class B**"*.
**P06's response:** the mechanism is consistent with what P06 verified — the widget clears and rebuilds every line of the statement entry (RM-F-01), which would indeed overwrite any value not re-supplied. **P06 confirms the shape and cannot confirm the analytic specifics**, which it did not trace. Recorded as **`P06-OQ-92`**; P09's class B is appropriate and should stay class B.

---

## 6. Answering the peer questions addressed to P06

**PH-F-08 — P10 `X-08`: are bank-side prepayments and interest accruals P10 events or P06 events?**
`10_P10_CROSS_PROCESS_OWNERSHIP.md`: *"| `X-08` | **`P06` B2R** | Whether bank-side prepayments and interest accruals are P10 events or P06 events | `PEER DEPENDENCY OPEN` |"*

**P06 ANSWERS IT: the question resolves by absence.**
There is **no bank interest concept in the searched scope** — re-verified this continuation under 13 alternative tokens across six modules, zero field or model definitions (`29_`, BAE-F-00). There is therefore **no bank-side interest accrual object for either process to own.**
- If interest is to be **accrued over time**, it is a P10 recognition event and P06 supplies only the cash event when it lands.
- If interest is **recognised when the bank credits it**, it is a P06 bank event — and P06 has no object for it either.
**Either way P10 may close `X-08` as answered: the object does not exist in the reference and must be designed, and P06 recommends the boundary be drawn at accrual (P10) versus receipt (P06).** That recommendation is P06's position, not a determination.

**PH-F-09 — P07's three BLOCKING dependencies on P06.**
`10_P07_CROSS_PROCESS_OWNERSHIP.md` marks `X-07` (payment event, date, currency, amount), `X-08` (partial payment / allocation) and `X-09` (payment reversal / cancellation) as **BLOCKING for P07**, with P06 named owner.
**P06's position:** it accepts ownership of all three, and must report that **all three are defective in the reference**:
- payment **date** is user-settable and changing it *silently drops the entire withholding* (P05 `TX-03`, HIGH);
- **allocation** per invoice exists but the settled amount is mutated by two mutually-unaware custom subsystems (`P06-B-13`, P05 `TX-04`/`TX-05`);
- **reversal linkage** does not exist — `action_reject` is a bare flag with no cause and no unwind (RPL-F-01).
**P06 does not resolve P07's statutory question. Both packages hold it identically, which is the correct outcome.**

---

## 7. Handoff matrix

| To | P06 supplies | P06 requires | Status |
|---|---|---|---|
| **P01** | vendor-payment settlement mechanics, the batch-rejection gap, cheque and PDC absence | payable ownership, payment-intent authorship | **PEER DEPENDENCY OPEN — not published** |
| **P02** | the `is_matched` four-branch mechanism; the configuration-dependence reconciliation (§3) | resolution of `P06-XC-01` | **CONFLICT ROUTED to P11** |
| **P03** | — | — | corroborates `CPO-F-01` only |
| **P04** | — | its lock-cascade findings, absorbed | **absorbed** |
| **P05** | the payment-door inventory; confirmation that P06 owns the reimbursement door | closure of `EX-03` (payments emitted outside the owner) | **routed** |
| **P07** | payment date, allocation, reversal linkage, FX policy — **all three accepted and all three reported defective** | nothing; P07's statutory HOLD mirrors P06's | **accepted, defects declared** |
| **P08** | the full period-close input set (`28_` §5), incl. lock inheritance across possibly-distinct legal entities | the close architecture | **PEER DEPENDENCY OPEN — not published** |
| **P09** | confirmation of the overwrite shape; class B retained | — | **answered** |
| **P10** | **`X-08` answered** (§6) | — | **closed by P06** |
| **P11** | `P06-B-27` **closed** (strike from `D-3`); `P06-XC-01` raised; 31 event→GL rows still to reconcile; net-new scope rows for bank account, provider and token | reconciliation of all of it | **delivered** |

---

## 8. What P06 asks P11 to carry

1. **`P06-B-27` is closed.** Remove it from the `D-3` UAT list; the answer is in the model, not the data.
2. **Register `P06-XC-01`** (P02-F-43 vs P06 headline (i)) as a cross-package contradiction — candidate `P11-C-08`.
3. **P06 accepts the producer characterisation** and does not contest `UBE-36` / `UBE-38` ownership.
4. **`P06-B-53`** — the payment-object-less cash door P05 found — reopens P06's door denominator and belongs in the unified event register.
5. **P06's scope rows for bank account, payment provider and payment token are net-new** to `P11_SCOPE_OWNERSHIP_MATRIX.md`, and `A4b` is a `DENY` case under P11's own Delta 02 rule.
6. **Two P06 headlines are unopposed and uncorroborated** — custom-module bank-statement coverage, and the v14→v18 cheque/returned-payment gap. P06 is the sole denominator holder for both and carries their declared boundaries.

---

# End
