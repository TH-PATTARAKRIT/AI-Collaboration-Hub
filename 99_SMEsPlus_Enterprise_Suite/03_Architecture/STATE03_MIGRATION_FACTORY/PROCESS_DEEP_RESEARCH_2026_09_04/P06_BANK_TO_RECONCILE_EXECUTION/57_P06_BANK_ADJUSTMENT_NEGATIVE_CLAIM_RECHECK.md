# P06_BANK_ADJUSTMENT_NEGATIVE_CLAIM_RECHECK.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S11)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Rule observed:** *"Do not silently upgrade a scoped negative to universal absence."*

---

## 1. What has been established, across three passes

| Pass | Scope | Patterns | Result |
|---|---|---|---|
| Round 1 | 6 v18 modules | `bank_fee\|bank_charge\|transaction_fee\|interest` | 0 definitions |
| Round 3 | same 6 modules | **13 disjoint tokens** — `commission\|charges\|levy\|duty\|surcharge\|deduction\|net_amount\|gross_amount\|settlement_amount\|payout\|merchant_fee\|processing_fee\|discount_fee\|acquirer` | 0 definitions; 2 non-definitional hits |
| Round 3 | both v18 `l10n_*` packs | fee + return patterns | 0 files |
| **Round 4** | **V19E `account` + `account_accountant` + `payment`** | fee patterns | **2 files: `chart_template.py` (a chart-of-accounts row) and a test. 0 model/field definitions** |

---

## 2. Final classification

**`NO DEFINITION IN VERIFIED POPULATION`.**

Stated in full:
> **No model or field defining a bank fee, bank interest, provider commission, merchant/processing/discount fee, surcharge, levy, gross/net/settlement amount, payout or acquirer was found in: the six declared v18 accounting and payment modules, both v18 localisation packs, or the v19 `account`, `account_accountant` and `payment` modules — under three independently-worded pattern sets across four passes.**

**What this is NOT:**
- **NOT** `DEPLOYED ABSENCE VERIFIED` — no target registry exists (`P06-B-44`).
- **NOT** universal absence — the v18 tree is filtered (791 of an unknown full population), and the v19 sweep covered three modules, not 1422.
- **NOT** `VERSION-DEPENDENT` — the finding holds in both generations.
- **NOT** `PEER-OWNED` — no peer claims it; P10 asked P06 and P06 answered by absence (`X-08`).

---

## 3. The one adjacent artefact, restated

`$V18E/account_iso20022/models/account_batch_payment.py:18-21` — `iso20022_charge_bearer`, a four-value enum (`CRED`/`DEBT`/`SLEV`/`SHAR`) written out as `ChrgBr` on the **outbound** instruction, defaulting to `"SHAR"`.

**It declares who is contractually liable for bank charges on money leaving. It carries no amount and captures nothing inbound.**

**BAR-F-01 — This is the same asymmetry as `P06-B-48`** (a globally-unique outbound UETR with no inbound counterpart). **The reference models what it sends and does not model what it receives.** Two independent instances of one pattern.

---

## 4. The alternative reading, still not disposed of

Carried from round 3's challenge (E3-C-02) and **unchanged**:

> Thai SMEs demonstrably incur bank charges. That the platform models none may mean **(a)** the capability is missing — P06's reading — or **(b)** it is handled outside the ERP by business convention, which would make this a *business-process* finding rather than a platform defect.

**P06 cannot distinguish these from source.** `P06-OQ-95` — resolvable only by asking the business how bank charges are handled today. **It remains the cheapest unanswered question in the package and it needs no technical evidence at all.**

---

## 5. Consequence that survives every qualification

Whatever the reading, the **mechanism** available today is a reconcile-model write-off line, and for a variable fee that means a regex over the bank's free-text narrative — where **a `ValueError` is swallowed to `0.0` and a non-match also yields `0.0`** (`$V18E/account_accountant/models/account_reconcile_model_line.py:96-107`), after which zero-amount write-off lines are dropped entirely.

**A mis-specified regex books a zero fee, the entry balances, the statement reconciles, and the expense is simply absent.** That is a silent, self-concealing failure and it does not depend on how the negative is scoped.
