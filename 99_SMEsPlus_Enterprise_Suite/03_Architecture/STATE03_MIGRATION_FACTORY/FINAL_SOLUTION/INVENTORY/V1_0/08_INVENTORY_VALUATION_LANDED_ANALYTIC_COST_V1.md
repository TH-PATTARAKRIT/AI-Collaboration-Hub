# 08 — Inventory Valuation, Landed Cost and Analytic Cost v1.0

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V1-001` | Jira: `ERPPLUS-139`
Status: `SMEsPlus-OWNED COSTING DESIGN — INVENTORY SIDE ONLY — OWNERSHIP OF POLICY IS AN OPEN JOINT DECISION`
Clean-room: Layer 1. No reference-ERP costing implementation, account vocabulary, method enumeration or computation code is described. Thai costing norms are `HOLD / EVIDENCE REQUIRED` and routed to the Accounting-Tax track.

---

## 1. The Open Question at the Centre of This File

**Which concept owns valuation policy?** Four candidates exist: the product category, the product itself, the warehouse, or a standalone versioned policy object referenced by whichever of the others applies.

This session does **not** choose. It is a Joint Accounting ↔ Inventory decision (`JT-01`, `GAP-FS-01`), and it is the single largest open item in the Inventory design. Everything below is written so that it remains valid whichever owner is chosen — the policy is treated as a versioned, effective-dated *thing* that products resolve to, without asserting where it lives.

**Inventory's requirement of whatever owner is chosen:**

| # | Requirement |
|---|---|
| 1 | The policy resolves to exactly one effective policy per product, per company, per date — never ambiguous. |
| 2 | The policy is versioned with an effective date; changing it never silently restates history. |
| 3 | Every valuation fact records the policy version that produced it. |
| 4 | The policy in force is printed on every valuation report. |
| 5 | Moving a product to a different policy is an approved action with a stated treatment for existing stock, not an ordinary edit. |
| 6 | If a single object carries both valuation policy and an operational behaviour such as put-away, that dual role must be a deliberate, documented decision rather than an accident of structure (`GAP-FS-02`). |

---

## 2. Costing Methods — Business Description Only

SMEsPlus must support the costing methods a Thai SME accountant may legitimately be using. The choice of which are permitted, and under what conditions, is `HOLD / EVIDENCE REQUIRED` and routed to the Accounting-Tax track — this session describes them as business behaviours and asserts no norm.

| Method | Business behaviour | Where it fits | What it demands of Inventory |
|---|---|---|---|
| Weighted average | Every receipt blends into a single running average cost per product | Fast-moving goods with stable prices | Receipts must be applied in a deterministic order; the running average must be reproducible as of a date |
| First in, first out | Each issue consumes the oldest remaining cost layer | Perishable and batch goods, and where margin per shipment matters | Cost layers must be tracked and consumed in a stated order; layer history must survive |
| Standard cost | A fixed planned cost is used, and variances are recognised separately | Manufacturing, and businesses managing to a budget | Variance must be computed and surfaced, never absorbed silently |
| Specific identification | Cost follows the individual lot or serial | High-value serialised goods | Cost is carried at lot or serial identity |

**Design position (Inventory side):** whichever methods are permitted, the method is a property of the *policy*, not of the transaction, and a transaction may never quietly use a different method from the one the policy names.

---

## 3. Valuation Timing

Two patterns exist, and the choice between them is a Joint decision (`JT-03`), not an Inventory decision.

| Pattern | Behaviour | Consequence Inventory must support |
|---|---|---|
| Continuous | Each boundary-crossing movement carries its value immediately | Facts must be emitted at validation, in order, with the cost basis resolved at that moment |
| Periodic | Value is established at period end from quantities and costs | Facts must still be emitted as movements happen, but the value may be resolved at close; the period-end computation must be reproducible |

Inventory's design supports both by separating the *movement fact* (always emitted immediately, always immutable) from the *valuation fact* (emitted with a cost basis and a policy version, whose resolution timing the policy dictates).

---

## 4. Landed Cost Design

### 4.1 Purpose

To reflect what the goods actually cost to bring into the warehouse — not just the supplier's price, but freight, duty, insurance, brokerage, inland transport and handling — so that margin and stock value are honest.

### 4.2 Cost types and allocation bases

| Cost type (candidate) | Typical basis | Note |
|---|---|---|
| Sea or air freight | By value, weight or volume | Volume basis matters for bulky low-value goods |
| Import duty | By value, or explicitly per line | Duty rates differ by goods class, so an explicit per-line entry must be possible |
| Insurance | By value | |
| Brokerage and clearance | By value or by shipment, spread evenly | |
| Inland transport | By weight or volume | |
| Handling and inspection | By quantity | |

All Thai labels for these types are `UNVALIDATED - THAI USER REVIEW REQUIRED`.

### 4.3 Design rules

| # | Rule | Reason |
|---|---|---|
| `LC-01` | A cost bill may be allocated to a receipt line exactly once. | Double allocation silently inflates stock value. |
| `LC-02` | The allocation statement must show the base amount, the basis, and the resulting amount per line, before validation. | The user must be able to check the arithmetic. |
| `LC-03` | Where the goods have already been sold, the system says so explicitly and routes the residual to Accounting. It never silently adjusts a cost basis with no stock behind it. | This is the most common landed-cost error and the hardest to detect afterwards. |
| `LC-04` | Where a product's policy uses a fixed planned cost, applying landed cost must be handled as a variance question, not as a cost-basis edit. | Otherwise the standard is no longer a standard. |
| `LC-05` | Allocation is subject to the period guard. | A late freight bill must not silently restate a closed period. |
| `LC-06` | The eligibility rule — which products and which receipts may receive landed cost at all — is **Joint** and is not set here. | Accounting consequence. |
| `LC-07` | Recoverable input VAT must not be capitalised into stock value if Thai rules so require. **`HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track.** | This session makes no statutory claim. |

### 4.4 What landed cost does not do

It does not move quantity. It does not create stock. It does not choose accounts. It does not decide whether a cost is capitalisable — that is an accounting judgement Inventory carries out, not one it makes.

---

## 5. Analytic and Allocation Cost for Decision Support

This section is deliberately separated from §2–§4, because it serves a different purpose and must never be confused with it.

**Statutory and financial valuation** answers: *what is the stock worth, for the books.*
**Analytic cost** answers: *what is this product, customer, channel or warehouse actually costing us, for a decision.*

| Aspect | Financial valuation | Analytic cost |
|---|---|---|
| Audience | Accountant, auditor, tax authority | Owner, sales manager, warehouse manager |
| Governed by | Costing policy, statutory constraints | Management judgement |
| Must reconcile to the ledger | Yes | No |
| May include costs not capitalisable into stock | No | Yes |
| Immutable once closed | Yes | Re-computable at will |

### 5.1 Analytic cost design (candidate, `UNVALIDATED - THAI USER REVIEW REQUIRED`)

| Element | Design |
|---|---|
| Cost pools | Warehouse operating cost, transport cost, handling cost, holding cost of capital, obsolescence provisioning |
| Allocation drivers | Movements handled, storage volume-days, order lines picked, value held |
| Dimensions | Product, category, warehouse, channel, customer group, supplier |
| Outputs | True margin per product and channel; cost-to-serve per customer group; carrying cost of slow-moving stock; the cost of an adjustment or scrap trend |

### 5.2 Governing rules

| # | Rule |
|---|---|
| `AC-01` | An analytic figure must **never** be presented in the same view as a financial valuation figure without a visible label distinguishing them. |
| `AC-02` | Every analytic figure states its cost pool, its driver and its period, so two readers reach the same conclusion. |
| `AC-03` | Analytic cost never feeds a valuation fact and never affects the ledger. |
| `AC-04` | Changing an allocation driver re-computes analytic history; that is acceptable for analytics and would be unacceptable for valuation, and the difference must be explained to the user. |
| `AC-05` | Analytic cost is a `CONDITIONAL` capability, off by default, appropriate for the established tier only. |

---

## 6. Valuation Report Requirements

| # | Requirement |
|---|---|
| `VR-01` | The report header names the costing policy and version used, and the as-of date. |
| `VR-02` | The report is reproducible: the same as-of date always yields the same figures. |
| `VR-03` | The report shows the period's movement of value — opening, receipts, issues, adjustments, scrap, landed cost, manufacturing, closing — not just a closing figure. |
| `VR-04` | A companion reconciliation view compares the computed value to the ledger balance and itemises every difference. |
| `VR-05` | The export path is acceptance-tested before the report is relied on by an accountant or auditor. |
| `VR-06` | Drill-through from any figure to the movements behind it is available. |
| `VR-07` | Negative or zero-cost stock is surfaced as an exception, never averaged away silently. |

---

## 7. Open Items From This File

| ID | Item | Owner | Blocking? |
|---|---|---|---|
| `GAP-FS-01` | Which concept owns valuation policy; how the period close is designed. | Joint | **Yes — blocks the valuation report and the close.** |
| `JT-02` | Permitted costing methods and the rules for changing one. | Joint | Yes |
| `JT-03` | Continuous versus periodic valuation timing. | Joint | Yes |
| `JT-04` | Cost-of-goods-sold recognition timing. | Joint | Yes |
| `JT-05` / `C-03` | Cost basis for a customer return. | Joint | Yes |
| `JT-06` | Late supplier bill after close. | Joint | Yes |
| `JT-08` / `LC-06` | Landed-cost eligibility and posting structure. | Joint | Yes for importers |
| `JT-09` | Work-in-progress recognition timing. | Joint | Yes where manufacturing applies |
| `TH-HOLD-03` | Thai import duty and VAT treatment in landed cost. | Accounting-Tax track | `HOLD / EVIDENCE REQUIRED` |
| `TH-HOLD-05` | Thai costing norms. | Accounting-Tax track | `HOLD / EVIDENCE REQUIRED` |
| `GAP-FS-12` | Whether analytic cost belongs in Inventory v1.0 at all, or in a later management-reporting release. | Boss | No — scope question |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
