# P01 → P11 — SERIES-16 SAME-GENERATION DELTA HANDOFF

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S16-14`

> **DELTA ONLY. This does not replace `P01_CORE_RECON_HANDOFF_PACK.md`,
> `P01_P11_EVIDENCE_VERSION_DEPLOYMENT_SUPPLEMENT.md` or
> `P01_P11_S18_DIRECT_VERIFICATION_SUPPLEMENT.md`. All remain in force in full.**

> ### CORRECTED AFTER AAS-03 EXPERT 2 — READ THIS BEFORE THE FIGURES
>
> **The GRNI residual handed to P11 below as ฿72,097,814.25 was an all-states figure.** Posted-only the
> account nets to **−฿7,048,692.08** — the opposite sign. **P11 must not carry the original number.**
> Two further items changed: the price-difference engine **does** fire (฿2,246,313,274.64 across 1,123
> layers, routed to six unenumerated accounts), and the Buddhist-era leakage is **484 values across 14
> columns in 11 tables**, not 30 in one.

---

## 1. THE ONE THING THAT CHANGES P11's PICTURE

P11 has been reconciling against two deployments in which **no inventory value reached the general ledger from
a goods receipt**, and P01 supplied a cause for each: in series 19 a missing stock journal, in series 18 a
periodic valuation policy.

> **In the series-16 deployment the receipt→valuation→clearing→bill bridge runs end to end.**
> 57,863 of 74,982 valuation layers post. The GRN clearing account carries 13,736 items and a net
> **฿72,097,814.25**. Vendor bills relieve it with **6,653 lines totalling ฿4,516,394,611.47**.

**This is the positive control.** It establishes that the mechanism P01 described from source is real and
operable, that the two zeros were about configuration and policy rather than a non-existent mechanism, and
that P11 may treat the source model as sound and the deployments as differently configured.

---

## 2. THE POLICY QUESTION NOW HAS AN INTERNAL CONTROL

Series 16 is a **mixed population**: global `manual_periodic`, with **15 of 30 categories** overriding to
`real_time`. One database, one codebase, one period, two policies.

| Policy | Posts | Does not post |
|---|---|---|
| `real_time` | **56,654** | 1,044 |
| `manual_periodic` | 1,209 | **16,075** |

P11 no longer needs a cross-deployment comparison to test the policy claim. **It is testable inside one
database**, with a coverage control (0 of 74,982 unresolved).

---

## 3. THREE OPEN CONTRADICTIONS P11 MUST NOT INHERIT AS SETTLED

| ID | Contradiction | Status |
|---|---|---|
| `S16-C-14` | **The inventory subledger and the GL disagree by ~10¹⁵ on 30 valuation layers** — values to ±1.5e21 against balanced GL entries of ฿31,622,699.37 | **OPEN.** GL is intact; the subledger is not. Root cause → **P03** (manufacturing/unbuild cost path) and **P08** |
| `S16-C-15` | **296** real_time non-zero layers unposted; **1,209** periodic layers posted, across 9 categories. Policy-change tested and **refuted** by time distribution | **OPEN** |
| `S16-C-18` | **484 BE values across 14 columns in 11 tables** + 11 at year 8202, bidirectional — invisible to every period-bounded query, and the trial balance still balances | **OPEN, 16× wider than published** → **P08** |

---

## 4. ITEMS ROUTED, WITH THEIR OWNERS

| To | Item | Measurement |
|---|---|---|
| **P08** | No period lock of any kind, on 169,143 posted entries | all three series-16 lock dates NULL |
| **P08** | **5,601 of 36,865 posted vendor bills (15.19%) dated EARLIER than their own invoice date**; 2,037 (5.53%) in a different month | clean-dated population; 2 BE rows excluded and declared |
| **P08** | Buddhist-era dates | **484 values, 14 columns, 11 tables**; + 11 at year 8202 |
| **P08**, **P11** | GRN posted-only net **−฿7,048,692.08**, and the ฿83.1M of cancelled/draft items that produced the withdrawn ฿72,097,814.25 figure | account 39; 53 cancelled + 17 draft items, one cancelled entry alone ฿90,351,213.15 |
| **P03**, **P08** | The 10¹⁵ subledger divergence, on `WH/MO/…` and `UB/…` documents with **negative unit costs** | 30 of 74,982 layers |
| **P07** | **A rate record named `WHT3%` carries the value `0`** — the most-used rate, 2,038 payments — yet ฿21,556,228.06 of withholding is posted after it was zeroed. **The posted amounts are hand-entered, not computed** | `account_withholding_tax` id 2; account `2260000`, 5,675 posted items |
| **P07** | **1,407 certificates (27.05%), ฿9,537,106.08, anchored to nothing** — no payment, no journal entry | two independent tools |
| **P07** | **2,029 posted withholding items (36.70%, ฿12,065,773.78) carry no certificate**; 1,417 certificates have no number, 202 share 75 numbers | — |
| **P07** | The submission file hardcodes income code **"2"** (differs from the certificate on **99.81%** of lines), exports the year **Gregorian in one field and Buddhist-era in another**, and **cannot select the 13 `pnd1` certificates at all** | report module, uncommitted on-disk copy |
| **P07** | PND form has **no code path** — operator-chosen — yet **0 of 506 suppliers ever received two different forms**. A perfect rule held only in habit | 5,201 certificates |
| **P07** | Whether withholding at **25.24% of supplier payments** is correctly scoped | `UNRESOLVED — STATUTORY EVIDENCE REQUIRED` |
| **P11** | Receipt→bill identity is carried by **document text**, not a foreign key | valuation-layer `description` strings |
| **P11** | `stock_landed_costs` **installed, 0 rows** | latent capability |

---

## 5. A SHAPE WARNING P11 MUST CARRY WITH EVERY FIGURE

**37,055 vendor bills against 5,881 purchase orders — 6:1.** Most purchasing here never passes through a
purchase order.

Therefore the three-way-match position (**79 lines, ฿12,678,776.50** received-not-invoiced) describes a
**minority of purchasing** and is not a whole-business control statistic. And comparisons with the series-18
OCC deployment — 4 companies, 1,904 bills, 13,887 orders, the **inverse** ratio — are comparisons between
**different businesses**, not between generations alone.

**`45a8e08e` is a rice miller at `swr.smeplus.asia`. `551ab874` is a concrete business at `occ.smeplus.cloud`.**
Every cross-generation statement in P01 now spans two different companies as well as two code generations, and
P11 should not attribute a difference to the generation without first excluding the business.

---

## 6. DECISION-AUTHORITY BOUNDARY

- Nothing above is a decision. Each item is a measurement plus an owner.
- P01 does **not** overrule P05 on the vendor-advance module; that disagreement is **preserved unresolved**
  (`S16-B-02`).
- P01 does **not** interpret Thai tax law. Every statutory question is `UNRESOLVED — STATUTORY EVIDENCE
  REQUIRED` and belongs to **P07**, whose current head (`3548b343`) was consumed delta-only and contains no
  WHT statutory position bearing on these items.
- Whether the GRN residual, the cut-off profile or the missing period lock are acceptable are **Boss
  decisions**, presented as findings, not recommendations.
