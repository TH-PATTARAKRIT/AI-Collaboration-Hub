# P01 → P11 — SERIES-18 DIRECT VERIFICATION SUPPLEMENT

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S18-16`

> **THIS IS A DELTA SUPPLEMENT. IT DOES NOT REPLACE ANY PRIOR P01 HANDOFF.**
> `P01_CORE_RECON_HANDOFF_PACK.md` and
> `P01_P11_EVIDENCE_VERSION_DEPLOYMENT_SUPPLEMENT.md` remain in force in full.
> Nothing here withdraws anything there. This adds what could not be known before a same-series
> deployment was available.

---

## 1. THE ONE THING P11 SHOULD TAKE FROM THIS RUN

P01 has, for the first time in five rounds, checked its source findings against a deployment of
**the same generation**. The result changes how several previously separate items should be counted.

> **Five P01 findings that P11 has been carrying as separate items are not five items. They are
> one configuration setting with five consequences.**

The setting is `product.category.property_valuation = manual_periodic`, global, unoverridden, in
every one of 126 categories across all 4 companies of database `551ab874`. It closes the gate at
`stock_valuation_layer._validate_accounting_entries`, and everything downstream stops:

| P01 finding | Why it is unreachable in this deployment |
|---|---|
| Goods-received clearing bridge | gate closed |
| Clearing account reconciled only if flagged | nothing posts, so nothing reconciles |
| Price-difference replay engine | gate closed **and** no price-difference account configured |
| Correction deletes derived journal items | no such items exist to delete |
| Anglo-saxon accounting (company 1) | eligibility requires `real_time` |

**P11 should carry this as one decision, not five blockers.**

---

## 2. SAME-GENERATION DEPLOYMENT DISCOVERY

| Item | Value |
|---|---|
| Database | `551ab874-9acb-11f1-b150-6ec7a480be3d` (`idemo18_uat`), archive 2026-08-30 |
| Series | 18, on **361 of 361** installed modules |
| Companies | 4 configured, **2 transacting** |
| Journal entries | 15,522 (13,773 posted) |
| Valuation layers | 47,801 — of which **96.2% are migrated series-14 history**. The defensible series-18 runtime set is **558** (over-determination-free core **541**; purchase-linked **61**), *not* the 1,812 first published — see `ERR-P01-27` |
| Vendor bills | 1,904 |
| Purchase orders | 13,887 |

Peer P04 records **two further** series-18 identities (`4b766580`, `96548e18`). Everything P01
states is bounded to `551ab874`.

---

## 3. SOURCE ↔ DEPLOYMENT OUTCOMES

| Outcome | Count | Detail |
|---|---|---|
| Confirmed same-generation | **5** (2 strengthened) | `P01_S18_SAME_GENERATION_FINDING_RECONCILIATION.md §1` |
| **Contradicted for series 18** | **1** | the bill-line account override is a **series-19 mechanism**; the file carrying it does not exist in the series-18 tree |
| Configured, not executed | 3 | clearing bridge, clearing reconciliation, anglo-saxon |
| Not reachable (policy / configuration / no lock) | 3 | |
| Not installed | 3 | inter-company rules, landed costs, vendor-advance module |
| Narrowed by counter-example | 1 | "landed cost installed **everywhere**" |
| New this run | 5 | |
| **Withdrawn** | **0** | every finding stays bound to the population it was measured in |

---

## 4. THE VALUATION-POLICY DISTINCTION — THE ITEM MOST LIKELY TO BE MIS-CARRIED

Two deployments in this estate report **zero** valuation layers linked to journal entries.

| | Series 18 (`551ab874`) | Series 19 (`E-1`) |
|---|---|---|
| Policy | `manual_periodic` — periodic | intends posting |
| Stock journal | **configured, all 4 companies** | **unset, 44 of 44** |
| Clearing account | configured, 171 of 504 (category, company) pairs | — |
| The zero means | **the policy working as specified** | **a configuration gap** |
| Remediation | **none** — changing it is a business decision | set the company stock journal |

> **SAME SHAPE / DIFFERENT CAUSE.** If P11 reconciles these as one item, it will either declare a
> correctly-configured periodic system defective, or offer "the policy explains it" as a defence
> for a system whose journal is genuinely missing. **Both errors are available and both are wrong.**

---

## 5. GRNI / CLEARING ACCOUNT — CONFIGURED, NOT EXECUTED

- `210300 "Uninvoiced Receipts"`, `liability_current`, **reconcilable**, one per company.
- Effective configuration: **171 of 504** (category, company) pairs. Company 1 resolves for **all**
  126 categories via its company default; companies 2 and 3 carry an explicit `false`; company 4
  has no default row.
- **Journal items on those accounts: 0.** Journal items in the four `STJ` valuation journals: **0.**
  Positive controls: 144 distinct accounts and 6 journals return non-zero from the same counter.
- Inventory (`130000`) carries 2,940 items, **all** in journal 45 `MIG26 "COA Migration 2026"` —
  migrated entries only.

---

## 6. THE NUMBER P11 AND P08 BOTH NEED

> **฿29,029,467.66 tax-exclusive** across **1,580 purchase order lines** is **received and not
> invoiced**, and is **recognised nowhere in the ledger** — no receipt entry, no clearing balance,
> **no accrual**. Of that, **฿27,490,865.80 on 1,411 lines is backed by an actual goods receipt**;
> the remaining **฿1,538,601.86 on 169 service lines** is an operator-typed quantity with no
> receipt document and should not be read as *received*.

Companies: 1 → ฿14,692,566.42; 2 → ฿14,336,901.24. Unit: one PO line, **tax-exclusive**, THB
(single currency, rate 1.0 on all 13,887 orders; discount zero on every line — both by
enumeration), excluding orders in `cancel` or `draft`. Counterpart: 183 lines
invoiced-not-received, **฿1,663,518.07**. A further 18 lines are **over-received**
(`qty_received > product_qty`) carrying ฿1,669,526.29.

*As first published this was ฿30,080,689.78, which summed two tax bases — 312 of the 1,580 lines
carry VAT-inclusive unit prices. Overstated by ฿1,051,222.12, 3.49%. Corrected as `ERR-P01-28`
after adversarial challenge; the superseded figure is preserved in the error log.*
Accrual control: **0 of 15,522** journal entries carry `accru` in `ref` (positive control: 15,434
have a non-empty `ref`).

**This is a timing position, not a missing transaction**, and under periodic valuation no
receipt-time entry is expected. It is a **completeness question at a reporting date**, and it is
**P08's judgement and the Boss's decision**, not P01's.

---

## 7. A SECOND ITEM FOR P08 AND P11

**10 of 1,904 vendor bills** carry their balancing line on an account that is **not** of type
`liability_payable` — nine on `218001 เจ้าหนี้อื่น` (`liability_current`, ฿1,788.27) and one on
`221002` finance lease (`liability_non_current`, ฿11,181.00). All posted, all company 2, total
**฿12,969.27**.

Immaterial in amount, structural in kind: **a payables ageing or a payment-matching routine scoped
to the payable account type will not see these liabilities.** That is a subledger-to-ledger
reconciliation difference — P11's and P08's scope, not P01's.

---

## 8. A LINEAGE OBSERVATION P11 MAY BE ABLE TO USE

In this deployment `stock_move` carries `created_purchase_request_line_id`: **the requisition
identity survives all the way into the goods movement**, not merely into the purchase order.
1,504 of 3,398 request lines reach a purchase order.

Offered as an **observation about this deployment**. It is **not** a design position, and P01 does
not define P11's architecture.

---

## 9. WHAT THIS SUPPLEMENT DOES *NOT* GIVE P11

- **No runtime execution.** Nothing has been executed in any of the five rounds. The seven priority
  edge cases remain `HOLD — RUNTIME WRITE AUTHORIZATION REQUIRED`.
- **No statutory conclusion.** The deployed withholding mechanism is **four OCA/Ecosoft modules**,
  not `l10n_th` — a P01 attribution corrected this run (`ERR-P01-33`). Whether P01's series-16
  withholding finding concerns this same family at an earlier version is **NOT DECIDABLE** here,
  and **no transfer is made**. Statutory correctness is **P07's**:
  `HOLD — STATUTORY EVIDENCE REQUIRED`. See `P01_S18_WHT_DEPLOYMENT_REALITY.md`.
- **No decision.** Whether periodic valuation is right for this business, and whether the unaccrued
  received-not-invoiced position is acceptable, are **Boss decisions**. They appear below as
  options, without a recommendation.
- **No exit-criteria improvement claimed.** See §11.

---

## 10. BOSS-DECISION IMPACT — OPTIONS, NOT RECOMMENDATIONS

**Decision D-S18-01 — the valuation policy in the series-18 line.**

The configuration in `551ab874` is built for a perpetual bridge: the clearing account exists, is
correctly typed, is reconcilable, and is mapped across four companies and the fifteen categories
carrying this business's material flows; the valuation journals exist in every company; anglo-saxon
accounting is switched on in company 1. **The single switch that would engage all of it is set to
periodic.** And the series-14 predecessor **did** post to an `STJ` stock journal — 15,434 of 15,522
journal entries carry refs of the form `[v14 STJ/… ] STJ/2026/04/0505`.

| Option | What it means |
|---|---|
| **A** | Periodic was chosen deliberately. Nothing is wrong. The ฿30.08M position is managed by periodic count and manual accrual — **neither of which is evidenced in this database**. |
| **B** | The setting was lost or defaulted during migration from the series-14 system. The configuration around it is the evidence of the original intent. |
| **C** | Undetermined. Requires the migration specification, a configuration decision record, or the predecessor's own settings — **none of which P01 holds**. |

**P01 does not choose.** The distinction is not decidable from the artefacts available, and
choosing between A and B is a business and audit judgement.

---

## 11. EXIT CRITERIA — NO IMPROVEMENT CLAIMED

`EC-01` … `EC-08` are **unchanged** by this run: **0 satisfied, 8 not satisfied** on the
package-wide test as last assessed, and this run does not move any of them. It adds same-generation
evidence, it corrects the evidence base twice more (`ERR-P01-24`, `ERR-P01-25`), and it raises the
estate floor from six identities to eight.

**`EC-06` (declare *and prove* the search boundary) deteriorates rather than improves**: this run
found **two further population-selection defects**, one of them in the source path set on which
every P01 code citation rests. A round that discovers its own evidence base is wronger than it
thought has not improved its exit position — it has improved its **honesty about it**, which is not
the same thing and must not be reported as the same thing.

---

## 12. REMAINING BLOCKERS RELEVANT TO P11

| ID | Blocker | Status |
|---|---|---|
| `DEP-P01-01` | Deployed copy identity | **OPEN** — 10 of 16 custom modules have no version-matching source on this host; 7 have no copy at all |
| `DEP-P01-06` | Tenant residue | **PARTIALLY RESOLVED** — unchanged this run |
| `S18-B-01` | Two further series-18 identities (`4b766580`, `96548e18`) unread by P01 | **OPEN** |
| `S18-B-02` | Whether periodic was intended or lost in migration | **OPEN — external evidence required** |
| `S18-B-03` | The P01 source path set does not contain the deployment's custom code | **OPEN — re-declaring it changes the evidence base of five published rounds; raised, not done unilaterally** |
| `S18-B-04` | Estate population still open (≥ 8 identities, ≥ 39 artefacts, no total) | **OPEN** |
| — | Runtime execution of the seven priority edge cases | **HOLD — RUNTIME WRITE AUTHORIZATION REQUIRED** |
| — | Thai WHT / PND statutory basis | **HOLD — STATUTORY EVIDENCE REQUIRED** → P07 |
