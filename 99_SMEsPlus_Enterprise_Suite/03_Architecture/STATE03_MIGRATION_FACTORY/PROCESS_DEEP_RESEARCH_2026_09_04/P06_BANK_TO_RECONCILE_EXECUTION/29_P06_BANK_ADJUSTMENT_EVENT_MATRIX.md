# P06_BANK_ADJUSTMENT_EVENT_MATRIX.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION (CP-C08)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Status of the prior finding:** **RE-VERIFIED BY INDEPENDENT SEARCH — SURVIVES UNCHANGED.**

---

## 1. The independent re-search

Prior round PATTERN: `bank_fee | bank_charge | transaction_fee | interest`.
**This round PATTERN (13 tokens, deliberately disjoint):** `commission | charges | levy | duty | surcharge | deduction | net_amount | gross_amount | settlement_amount | payout | merchant_fee | processing_fee | discount_fee | acquirer`.
**PATH SET:** `$V18E/{account, account_accountant, payment, account_payment, account_online_synchronization, account_iso20022}`, `*.py`, `/tests/` excluded. **UNIT:** matching line.

| token | lines | token | lines |
|---|---|---|---|
| `commission` | **0** | `settlement_amount` | **0** |
| `charges` | 1 | `payout` | 1 |
| `levy` | **0** | `merchant_fee` | **0** |
| `duty` | **0** | `processing_fee` | **0** |
| `surcharge` | **0** | `discount_fee` | **0** |
| `deduction` | **0** | `acquirer` | **0** |
| `net_amount` / `gross_amount` | **0** / **0** | | |

Filtered to definitions (`fields\.|_name = |_inherit = `): **0 lines.**
The two surviving raw hits are non-definitional — a comment (`account_payment/models/payment_transaction.py:115`) and a `help=` string (`account_iso20022/models/account_batch_payment.py:24`).

> **ALTERNATIVE READING, added by AAS-03 E3-C-02 and NOT disposed of.** Thai SMEs demonstrably incur bank charges. That the platform models none may mean (a) the capability is missing — P06's reading — or (b) it is handled outside the ERP by business convention, which would make this a *business-process* finding rather than a platform defect. **P06 cannot distinguish these from source.** Resolvable only by asking the business how bank charges are handled today. `P06-OQ-95`.

**BAE-F-00 — The prior Class-A negative survives a second, independently-worded pass. There is no bank fee, bank interest, commission, merchant/processing/discount fee, surcharge, levy, gross/net/settlement amount, payout or acquirer concept in the declared scope.**

**Scope honesty:** localisation packs (`$V18E/l10n_*`) were **NOT** searched, and several jurisdictions ship bank-charge handling there. **The Class-A negative is valid for the six declared modules and must not be generalised to `$V18E` as a whole.** Carried as `P06-OQ-90`.

---

## 2. The one adjacent artefact, and what it is not

**BAE-F-01 — ISO 20022 declares *who bears* bank charges. It does not carry an amount and it does not capture one.**
`$V18E/account_iso20022/models/account_batch_payment.py:18-21`:
```
iso20022_charge_bearer = fields.Selection(
    selection=[('CRED', 'Creditor'), ('DEBT', 'Debtor'), ('SLEV', 'Service Level'), ('SHAR', 'Shared')],
```
written out as `ChrgBr` on the outbound instruction — `models/account_journal.py:236-237`, defaulting to `"SHAR"`.

**This is a contractual liability declaration on money leaving. Nothing books the fee when the bank actually deducts it.** The system can tell the bank who should pay the charge and has no object for the charge itself. That asymmetry — outbound intent modelled, inbound reality unmodelled — is the same shape as the UETR finding (`P06-B-48`), and it is worth naming as a pattern: **the reference models what it sends and not what it receives.**

---

## 3. The adjustment event matrix

| ID | Adjustment event | First-class? | Owner | Account determination | Capture path |
|---|---|---|---|---|---|
| BA-01 | **Bank fee / charge** | **NO** | **none** | free-choice write-off | reconcile-model line, incl. regex over bank narrative |
| BA-02 | **Bank interest received** | **NO** | **none** | free-choice write-off | as BA-01 |
| BA-03 | **Bank interest paid** | **NO** | **none** | free-choice write-off | as BA-01 |
| BA-04 | **Provider commission** | **NO — not modelled in v18** | **none** | free-choice write-off | manual |
| BA-05 | **Net vs gross settlement** | **NO** | **none** | — | **unhandled** — `P06-B-25` |
| BA-06 | Payment difference (short) | mechanism only | P06 | free choice, no type restriction | tolerance or manual write-off |
| BA-07 | Payment difference (over) | mechanism only | P06 | — | tolerance **bypassed**; auto-reconcile permitted |
| BA-08 | FX difference at settlement | **YES** | P-CORE config | company gain/loss accounts | exchange-difference move |
| BA-09 | Early-payment discount | **YES** | company config | dedicated gain/loss accounts | EPD counterpart lines |
| BA-10 | Cash over/short | **YES** | journal config | journal profit/loss accounts | statement difference |
| BA-11 | Cash-basis tax | **YES** | company config | 3-deep silent fallback | CABA move |
| BA-12 | Withholding at settlement | custom only | P07 | custom modules mutate the settled amount | **HOLD — statutory** |
| BA-13 | Charge-bearer declaration | **YES, outbound only** | COMPANY | n/a — no amount | ISO 20022 `ChrgBr` |

**5 of 13 are first-class. 5 have no owner at all** (BA-01…BA-05). Those five are the routine economics of holding a bank account.

---

## 4. The capture mechanism for the unowned five, and why it is unsafe

The only available mechanism is a reconcile-model write-off line. For a *variable* fee that means a regex over the bank's free-text narrative:
`$V18E/account_accountant/models/account_reconcile_model_line.py:96-107`:
```
elif self.amount_type == 'regex':
    match = re.search(self.amount_string, st_line.payment_ref)
...
    extracted_balance = float(extracted_match_group.replace(decimal_separator, '.'))
```
and at `:104-107` **a `ValueError` is swallowed to `0.0`, and a non-match also yields `0.0`.**

**BAE-F-02 — A mis-specified or drifted regex silently books a zero fee.** The entry still balances, the statement still reconciles, and the expense is simply absent — because the amount that failed to parse is the amount that was not posted. Zero-amount write-off lines are then dropped entirely (`account_reconcile_model.py:33-37`), so no trace remains.
**This is the worst failure mode in the file: it is silent, it is self-concealing, and it produces a clean-looking reconciliation.**

**BAE-F-03 — And the target format cannot be validated here.** Thai bank statement narratives are not held by this session (NC-03). No regex design can be assessed. **HOLD — STATUTORY / VENDOR EVIDENCE REQUIRED.**

---

## 5. Provider settlement — the concrete gap

A provider that settles a batch **net of commission** produces one bank credit that does not equal the sum of the transactions it settles.

- v18 has **no fee fields on `payment.provider` or `payment.transaction`** — `fees`, `fees_active`, `_compute_fees`: **NOT FOUND**, re-confirmed this round under 13 different tokens.
- `account_payment` posts **no** provider fee to the GL — PATTERN `fee` over that module, recursive `.py`: **0**.
- Therefore the difference is absorbed manually, via BA-01's regex path, or it sits in suspense where **no ageing report can see it** (EC-F-01).

**Requirement:** net settlement must be decomposable into **gross + fee against a single bank credit**, with a proof that the parts reconcile to the whole. `P06-B-25` remains open and is now the best-evidenced gap in this file.

---

## 6. Blocker impact

| ID | Status |
|---|---|
| `P06-B-17` no owner for fees/interest/commission | **remains open — re-verified by independent search**, evidence class upgraded |
| `P06-B-25` net-vs-gross settlement | **remains open**, mechanism now fully traced |
| `P06-B-40` | **PARTIALLY CLOSED** — second pass done for this negative and the identity negative |
| `P06-OQ-90` | **NEW** — `l10n_*` packs not searched; the negative is scoped to six modules |
| `P06-OQ-32` Thai narrative formats | remains **HOLD** |

---

# End
