# P01 — SERIES-16 THAI WHT: SOURCE BEHAVIOUR vs STATUTORY REQUIREMENT

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S16-06` · Deployment `45a8e08e`

> ## THE BOUNDARY, STATED BEFORE ANY EVIDENCE
>
> Everything in this document is **observed system behaviour**. **None of it is a statement about what Thai
> tax law requires.** Source behaviour is not statutory truth. Every question of statutory correctness is
> classified `UNRESOLVED — STATUTORY EVIDENCE REQUIRED` and routed to peer process **P07**, which owns it.
> P01 does not interpret the Revenue Code, and nothing here may be cited as compliance.

---

## 1. WHY THIS DEPLOYMENT MATTERS FOR WHT

P01's earlier withholding findings came from a **series-16 custom wizard source copy** that, at the time, no
known deployment ran (`ERR-P01-13`). This deployment is series 16 **and** exercises withholding heavily.

| Measure | Value |
|---|---|
| `withholding_tax_cert` rows | **5,201** — done 5,191 / cancel 5 / draft 5 |
| Date range | 2023-10-01 … 2026-07-13 |
| Supplier payments | **19,575** of 22,468 |
| **Supplier payments carrying `wt_tax_id`** | **4,941 (25.24%)** |
| Certificates linked to a payment | **3,794 of 5,201** |

---

## 2. WHT IS NOT APPLIED TO EVERY PURCHASE — AND THAT IS THE POINT

**Only 25.24% of supplier payments carry a withholding tax.** Three quarters do not.

The prompt's caution — *do not force WHT into stock purchase where business/tax conditions do not apply* —
is borne out by the data: this is a **selective** application, not a blanket one. Which purchases attract it,
and whether that selection is correct, is **not** determined here.

**Any P01 statement implying withholding applies generally to procurement would be contradicted by this
deployment.** No such statement is made.

---

## 3. THE PND FORM MAPPING IS STORED DATA, NOT AN INFERENCE

`withholding_tax_cert.income_tax_form` across all 5,201 certificates:

| Form | Certificates |
|---|---|
| `pnd53` | **4,437** |
| `pnd3` | **751** |
| `pnd1` | 13 |

**FACT VERIFIED as a distribution.** P01's earlier `PND MAPPING CONTRADICTION` finding concerned two shipped
source copies disagreeing about a mapping, and concluded that *neither mapping governs where an operator picks
the form*. This deployment shows the field **populated on every certificate**, which is consistent with that
conclusion and does not resolve it: a populated field does not reveal **who or what populated it**.

**Whether the form selection is correct for each income type is `UNRESOLVED — STATUTORY EVIDENCE REQUIRED` → P07.**

---

## 4. A GAP IN THE CERTIFICATE→PAYMENT CHAIN

**3,794 of 5,201 certificates carry a `payment_id`. 1,407 (27.05%) do not.**

A withholding certificate is evidence of tax withheld from a payment. **More than a quarter of the
certificates in this deployment are not linked to a payment record.**

Possible readings — none of them established here — include certificates raised against bills rather than
payments, migrated historical certificates, or a broken link. **CLASSIFICATION:
`UNRESOLVED — EVIDENCE REQUIRED`**, and it is handed to **P07** (statutory sufficiency of certificate
evidence) and **P11** (lineage), not adjudicated by P01.

---

## 5. A FIELD THIS PACKAGE DELIBERATELY DOES NOT INTERPRET

`account_payment.wt_cert_cancel` is set on **15,874 of 19,575** supplier payments — the large majority,
including payments that carry no `wt_tax_id`. A boolean true on most rows is more consistent with a default
than with a business event.

**No interpretation is offered.** Reading a majority-true flag as "certificates were cancelled" would be an
inference from a field name, and P01 has already published one finding built that way
(`ERR-P01-21`, where a field name led to the wrong document type). It is recorded as an observation with its
denominator and left open.

---

## 6. WHAT AAS-03 EXPERT 3 WAS ASKED TO DISPROVE

1. That the deployed WHT mechanism is the one P01 previously analysed. The deployed stack is
   `l10n_th_withholding_tax 16.0.1.0.1`, `l10n_th_withholding_tax_cert` **`16.0.14.0.1.0.0`**,
   `_cert_form 16.0.1.0.1`, `_report 16.0.1.0.0` — and the `16.0.14.*` signature means a **series-14 module
   body on a series-16 engine** (`ERR-P01-41`, read from the series-16 `adapt_version`).
2. That withholding is correctly scoped to applicable purchases.
3. What actually determines `income_tax_form`.

Their findings are carried in `P01_S16_AAS03_FOUR_EXPERT_CHALLENGE.md`. **No statutory conclusion is admitted
from an expert either.**

---

## 7. CLASSIFICATION

| Item | Classification |
|---|---|
| 5,201 certificates exist; 5,191 done | **FACT VERIFIED** |
| WHT applies to 4,941 of 19,575 supplier payments (25.24%) | **FACT VERIFIED** |
| PND distribution pnd53 4,437 / pnd3 751 / pnd1 13 | **FACT VERIFIED** |
| 1,407 certificates carry no payment link | **FACT VERIFIED**; cause **UNRESOLVED — EVIDENCE REQUIRED** |
| The deployed cert module is a series-14 body on a series-16 engine | **FACT VERIFIED** |
| Whether withholding rates, bases or timing are statutorily correct | **UNRESOLVED — STATUTORY EVIDENCE REQUIRED → P07** |
| Whether PND form selection is statutorily correct | **UNRESOLVED — STATUTORY EVIDENCE REQUIRED → P07** |
| Whether a certificate without a payment link satisfies statutory evidence | **UNRESOLVED — STATUTORY EVIDENCE REQUIRED → P07** |
| `wt_cert_cancel` semantics | **NOT INTERPRETED — deliberately** |
