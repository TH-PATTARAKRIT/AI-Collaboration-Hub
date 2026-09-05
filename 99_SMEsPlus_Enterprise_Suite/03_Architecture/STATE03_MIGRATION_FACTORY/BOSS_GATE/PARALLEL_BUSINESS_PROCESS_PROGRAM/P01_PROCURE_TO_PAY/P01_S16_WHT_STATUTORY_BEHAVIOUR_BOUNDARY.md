# P01 — SERIES-16 THAI WHT: SOURCE BEHAVIOUR vs STATUTORY REQUIREMENT

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S16-06` · Deployment `45a8e08e`

> ## THE BOUNDARY, STATED BEFORE ANY EVIDENCE
>
> Everything in this document is **observed system behaviour**. **None of it is a statement about what Thai
> tax law requires.** Source behaviour is not statutory truth. Every question of statutory correctness is
> classified `UNRESOLVED — STATUTORY EVIDENCE REQUIRED` and routed to peer process **P07**, which owns it.
> P01 does not interpret the Revenue Code, and nothing here may be cited as compliance.


> ### MATERIALLY EXTENDED BY AAS-03 EXPERT 3 — VERIFIED BEFORE ADOPTION
>
> **The withholding amounts in this ledger are not produced by the withholding module's arithmetic.**
> Re-derived independently here. The statutory boundary in the header is unchanged and still governs.

---

## 0. THE HEADLINE, AND IT IS NOT A ROUNDING QUESTION

`account_withholding_tax` holds **7 rate records**. Six are sane. The seventh:

| id | name | `amount` | `write_date` |
|---|---|---|---|
| 5 | WHT15% | 15 | 2023-10-04 |
| 1 | WHT1% | 1 | 2023-10-04 |
| 3 | WHT5% | 5 | 2023-10-04 |
| 6 | WHT10% | 10 | 2023-10-04 |
| 4 | WHT0.5% | 0.5 | 2023-10-20 |
| 7 | WHT2% | 2 | 2023-11-08 |
| **2** | **WHT3%** | **0** | **2023-12-29 02:59:30** |

> **A rate record named `WHT3%` carries the value `0`.**

**It is the most-used rate in the deployment**: **2,038 of the 4,945** payments carrying a `wt_tax_id` point
at it — and **1,866 of those were created after it was zeroed**.

The module's expression is `wt_tax_id.amount / 100 * price_subtotal`. At `amount = 0` **it evaluates to 0.00**.
Yet withholding is posted:

| Account `1137` = `2260000 Withholding Tax` (`liability_current`) | Value |
|---|---|
| Journal items | 5,863 — **posted 5,675**, cancelled 185, draft 3 |
| **Posted** Dr / Cr | ฿26,007,030.14 / ฿26,139,905.55 |
| **Posted items dated on/after the rate was zeroed** | **4,719, crediting ฿21,556,228.06** |

*(state basis declared, per `ERR-P01-45`)*

**A rate valued 0 cannot produce ฿21.5 million of withholding.** AAS-03 Expert 3 traced the amounts to the
operator entering net cash into a `payment_difference_handling = "reconcile"` write-off — so the posted figure
is **hand-entered**, and the rate record beside it is **decorative**. **89 of the 91 configured product
defaults point at this same 0% record.**

**CLASSIFICATION: `FACT VERIFIED`** — the rate record's value, its usage count, and the posted amounts are all
measured. **That the write-off is the source of the amounts is `SUPPORTED INTERPRETATION`**, carried from
Expert 3 with attribution.

**Statutory implications are NOT drawn.** Whether hand-entered withholding satisfies Thai requirements is
`UNRESOLVED — STATUTORY EVIDENCE REQUIRED` → **P07**.

---

## 0.1 VERSION MATCHING DOES NOT IDENTIFY THIS CODE — AND A BETTER INSTRUMENT EXISTS

`l10n_th_withholding_tax_cert` has **4 distinct `.py` variants on this host all sharing `16.0.14.0.1.0.0`**;
`..._report` has **6 sharing `16.0.1.0.0`** (its manifest literally declares `'version': '1.0.0'`).

**Expert 3 discriminated using the deployment's own `ir_model_fields` registry** rather than the version
string: only one variant declares a `signature` field, and the registry has it. **That is a materially better
instrument than anything P01 has used for code identity**, and it is adopted.

The identified variant differs from the **2021 Odoo-14.0 source by exactly one line** (`signature =
fields.Binary()`) — otherwise byte-identical. This **confirms and sharpens** the `16.0.14.*` reading: a
**series-14 body on a series-16 engine**, now established by content rather than by a version prefix.

It also carries a latent defect: a `move_id.type == "entry"` comparison against a field the registry confirms
**does not exist** (`account.move` has 183 fields, none named `type`). **It has never fired — `move_id` is
NULL on all 5,201 certificates.**

---

## 0.2 WHAT ELSE EXPERT 3 ESTABLISHED

| Finding | Measurement |
|---|---|
| **Certificates anchored to nothing** | **1,407 (27.05%), ฿9,537,106.08** — no payment, no journal entry; 1,470 of 1,499 lines carry no journal-item reference. Confirmed with two independent tools |
| Certificate numbering | **1,417 have no number; 202 share 75 numbers** (up to 9 to a number) |
| **The only arithmetic control is a tautology** | `base` is back-derived from `amount`, so 6,048/6,048 "consistent" proves nothing — **and it is skipped entirely at rate 0**: 111 lines, ฿5,698,486.81 of base, never checked |
| Withholding items with no certificate | **2,029 posted items (36.70%, ฿12,065,773.78)**; and 1,543 of 5,232 WHT-bearing payments (29.49%) have no certificate |
| **Withholding IS applied to goods** | **338 goods lines** (282 consumable + 56 storable), **195 raw-rice material lines**, **151 lines posting to the GRNI account `2900000`**, 64 to a fixed-asset account |
| Configuration coverage | only **2.30%** of the catalogue is configured, and **54.01% of applied withholding could not have come from any product default** — hand-keyed or overridden |
| PND selection | **no code path determines `income_tax_form`** — an operator field on a wizard, no default, no derivation. Yet **0 of 506 suppliers ever received two different forms** across 5,201 certificates: a perfect rule held **only in operator habit** |
| Submission file | hardcodes income code **"2"**, differing from the certificate on **99.81%** of lines; exports the year **Gregorian in field 14 and Buddhist-era in field 16**; **cannot select the 13 `pnd1` certificates at all**; filters on the editable `cert.date`, which falls in a different month from the payment for **437 certs / ฿2,725,891.46** |

*(The report module's on-disk copy is **uncommitted**, 246 lines ahead of a 2023 commit, with an unchanged
version string — a further reason version strings do not identify this code.)*

**`withholding_tax_report` extracting to 0 rows is NOT reported as a negative** — it is a `TransientModel` and
the ORM vacuums it. Expert 3 flagged this explicitly, and it is exactly the "empty table is not an absence"
discipline this package requires.

---

## 0.3 CORRECTION TO §2 BELOW

§2 says withholding *"is not applied to every purchase"* and reads that as selective application consistent
with the prompt's caution. **The 25.24% figure stands** (it is supplier payments carrying `wt_tax_id`;
across all partner types the count is 4,945).

**But the inference drawn from it was too comfortable.** Withholding **is** applied to goods, raw materials
and even lines posting to the goods-received clearing account. The selectivity is real; **the assumption that
it tracks a service/goods distinction is not supported**, and 54.01% of it cannot be traced to any configured
default. **Whether the selection is correct is `UNRESOLVED — STATUTORY EVIDENCE REQUIRED` → P07.**

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
