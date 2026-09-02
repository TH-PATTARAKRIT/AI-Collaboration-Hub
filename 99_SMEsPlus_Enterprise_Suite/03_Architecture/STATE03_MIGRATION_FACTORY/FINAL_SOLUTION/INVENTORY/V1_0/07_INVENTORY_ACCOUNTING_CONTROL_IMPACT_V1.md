# 07 — Inventory Accounting and Control Impact v1.0

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V1-001` | Jira: `ERPPLUS-139`
Status: `SMEsPlus-OWNED ACCOUNTING-INTERFACE DESIGN — INVENTORY SIDE ONLY — NOT APPROVED, CLOSES NO JOINT DECISION`
Clean-room: Layer 1. No account names, no posting structures, and no reference-ERP accounting vocabulary are copied. Where a Thai statutory rule would be needed, this file marks it `HOLD / EVIDENCE REQUIRED` and routes it to the Accounting-Tax track rather than asserting it.

---

## 1. The Interface Rule

**Inventory emits facts. Accounting decides postings.**

Inventory never writes a journal entry, never selects an account, and never decides recognition timing. It emits a **valuation fact** — a structured, immutable statement that a quantity of value moved, why, when, and against what reference — and Accounting owns everything that happens next.

This is the single most important boundary in the module, for three reasons: it keeps stock truth and financial truth separately provable; it lets Accounting change posting policy without rewriting Inventory; and it stops Inventory from making decisions it has no authority to make.

### 1.1 What a valuation fact carries

| Element | Meaning |
|---|---|
| Event type | Receipt, issue, return in, return out, adjustment, scrap, landed cost, manufacturing consumption, manufacturing output, transit (informational) |
| Quantity and unit | In the base unit, with the unit named |
| Cost basis and amount | The cost applied and the method version that produced it |
| Effective date | The movement date, subject to the period guard |
| References | Source document, movement fact, product, category, warehouse, lot where applicable |
| Reason and approver | For adjustments, scrap, returns and overrides |
| Policy version | Which valuation policy version was in force |

Accounting receives this and decides the entry. Inventory does not know, and must not encode, which accounts are involved.

---

## 2. Accounting Impact by Stock Event

| Event | Quantity effect | Value effect | Fact emitted | Boundary crossed |
|---|---|---|---|---|
| Purchase receipt | Increase | Increase | Receipt valuation fact | Supplier → internal |
| Customer delivery | Decrease | Decrease (cost of goods sold) | Issue fact | Internal → customer |
| Customer return in | Increase | Increase (reversal) | Reversing issue fact — **cost basis unresolved, `C-03`** | Customer → internal |
| Supplier return out | Decrease | Decrease (reversal) | Reversing receipt fact | Internal → supplier |
| Internal movement | None (place changes) | None | **No fact** | Internal → internal |
| Warehouse-to-warehouse transfer (same company) | None net | None | **No fact**; transit balance is informational | Internal → transit → internal |
| Inter-company transfer | Decrease in one company, increase in the other | Yes, in both | Two facts in two companies — **Joint design required** | Crosses a company boundary |
| Inventory adjustment (gain) | Increase | Increase | Gain fact with reason and approver | Adjustment counterpart → internal |
| Inventory adjustment (loss) | Decrease | Decrease | Loss fact with reason and approver | Internal → adjustment counterpart |
| Scrap | Decrease | Decrease | Loss fact with reason, approver and evidence pack | Internal → loss |
| Landed cost allocation | None | Increase on the affected receipt lines | Value-change fact per line | No quantity boundary; value only |
| Manufacturing consumption | Decrease | Decrease (into work in progress) | Consumption fact | Internal → production |
| Manufacturing output | Increase | Increase (from work in progress) | Output fact | Production → internal |
| Period close | None | None new | Close snapshot and reconciliation summary | **Joint** |
| Migration opening balance | Increase from zero | Increase | Certified opening fact — **requires human certification, `G-5`** | Adjustment counterpart → internal |

**The general rule stated once:** value moves when the ownership boundary is crossed. Everything else moves goods, not money.

---

## 3. Control Impact by Stock Event

| Event | Separation of duties | Reason required | Threshold escalation | Period guard | Immutability | Additional control |
|---|---|---|---|---|---|---|
| Receipt | Validator ≠ order approver | On over-receipt | Over tolerance | Yes | Done facts immutable | Duplicate validation refused |
| Delivery | Picker ≠ validator where tenant size allows | On lot override | No | Yes | Yes | Expired-lot block |
| Return in | Inspector ≠ approver | Always | By value | Yes | Yes | Reference to original delivery flagged when absent |
| Return out | Requester ≠ approver | Always | By value | Yes | Yes | Cannot exceed net received |
| Internal movement | None required | On put-away override | No | Yes | Yes | Both ends must be internal |
| Adjustment | **Counter ≠ approver — mandatory** | **Always, from a controlled list** | **Yes, with anti-splitting detection** | Yes | Yes | Stale counts expire rather than apply |
| Scrap | **Requester ≠ approver — mandatory** | **Always, from a controlled list** | **Yes** | Yes | Yes | Evidence pack; witness where a formal procedure applies |
| Landed cost | Accounting approval | On method choice | By value | Yes | Yes | One allocation per bill per receipt line |
| Manufacturing movements | Production ≠ warehouse validator | On variance | By value | Yes | Yes | Consumption variance surfaced |
| Feature switch change | Administrator, with Accounting acknowledgement where valuation is affected | Always | N/A | N/A | Audited | No silent regeneration of configuration |
| Period close | Accounting owns | N/A | N/A | Sets the guard | Snapshot immutable | Reconciliation before close |

---

## 4. The Period Guard

**Design position: Inventory owns a native period guard.**

Accounting supplies the lock date. Inventory refuses any movement dated into a locked period *itself*, at the point of entry, rather than relying on a downstream accounting bridge to reject the resulting entry. The reason is that a movement recorded into a closed period is a stock-truth defect before it is an accounting defect: the stock card becomes non-reproducible, and the prior-period valuation silently changes.

| Guard element | Design |
|---|---|
| Lock source | Accounting sets the lock date per company and period |
| Enforcement point | Inventory, at movement entry and at validation |
| Exception path | A named grantor, a written reason, an expiry date, and a permanent record — never a global toggle |
| Global bypass | **Not permitted.** A blanket bypass switch is explicitly rejected by this design; it makes the guard unauditable |
| Late-arriving cost | An explicit rule is required for a supplier bill that arrives after close and would change a closed-period cost basis. **Unresolved — Joint decision.** |

---

## 5. Reconciliation Requirements

| ID | Requirement | Frequency |
|---|---|---|
| `RC-01` | Conservation: sum of movements in, minus sum of movements out, equals on-hand, per product and place. | Continuous, with an alarm on breach |
| `RC-02` | Stock card as of a date reproduces the same figures on every run. | On demand |
| `RC-03` | Valuation as of period end agrees with the general ledger, with every reconciling item explained. | Each period |
| `RC-04` | Transit balances net to zero, or every open transit item is aged and explained. | Weekly |
| `RC-05` | Reservations never exceed on-hand. | Continuous |
| `RC-06` | Adjustment and scrap registers agree with the movements behind them and with the facts emitted. | Each period |
| `RC-07` | Landed-cost allocations sum to the cost bills they came from. | Each allocation |
| `RC-08` | Opening balance at cutover agrees, in quantity and value, with the accountant's opening trial balance, with human certification. | Once, at cutover |
| `RC-09` | Every valuation fact emitted has been received and dispositioned by Accounting — none silently lost. | Each period |
| `RC-10` | Every report export opens correctly and matches the on-screen figures. | Before each release of a report to an accountant or auditor |

`RC-10` exists because the evidence chain records a prior benchmark lesson: a reconciliation export that was defective in practice. A report that cannot be exported correctly is not a report an accountant can use.

---

## 6. Thai Statutory Items — All Held

None of the following is asserted by this session. Each is `HOLD / EVIDENCE REQUIRED` and is **routed to the Accounting-Tax track**. This session is not a Thai tax authority and has no legal evidence source.

| ID | Statutory question | Status | Routed to |
|---|---|---|---|
| `TH-HOLD-01` | The required format, columns and title of a Thai statutory stock report, and whether the stock card design satisfies it. | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |
| `TH-HOLD-02` | The procedure and evidence Thai authorities require before scrapped or destroyed stock is deductible. | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |
| `TH-HOLD-03` | The treatment of import duty and import VAT in landed cost, including whether recoverable input VAT must be excluded. | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |
| `TH-HOLD-04` | Whether and how product kind (goods versus service) correlates with withholding-tax applicability. | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |
| `TH-HOLD-05` | Accepted Thai costing norms and whether a chosen costing method is constrained by them. | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |
| `TH-HOLD-06` | Whether a warehouse must correspond to a registered tax branch, and the consequence of divergence. | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |
| `TH-HOLD-07` | Requirements for a witnessed annual physical count and its documentation. | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |
| `TH-HOLD-08` | Sector-specific traceability obligations for food, pharmaceutical and cosmetic goods. | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track, for onward legal routing |
| `TH-HOLD-09` | The link between a delivery document and a tax invoice, and any required document numbering conventions. | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |

---

## 7. Joint Decisions Inventory Cannot Make

| ID | Decision | Why Inventory cannot make it |
|---|---|---|
| `JT-01` | Which concept owns valuation policy — category, product, warehouse, or a standalone versioned policy. | It determines the accounting result, so it is Accounting's call as much as Inventory's. |
| `JT-02` | Costing method per policy and the rules for changing it. | Accounting consequence. |
| `JT-03` | Whether inventory value is recognised continuously as movements happen, or periodically at close. | Accounting consequence. |
| `JT-04` | The timing of cost-of-goods-sold recognition — at dispatch or at invoice. | Sales and Accounting both have a stake. |
| `JT-05` | The cost basis applied to a customer return. **Carried as `C-03`.** | Accounting consequence. |
| `JT-06` | The rule for a supplier bill arriving after period close. | Accounting consequence. |
| `JT-07` | The design of the period close itself and what the closing snapshot must contain. | Accounting owns close. |
| `JT-08` | Landed-cost eligibility rules and posting structure. | Accounting consequence. |
| `JT-09` | Work-in-progress recognition timing for manufacturing consumption and output. | Accounting consequence. |
| `JT-10` | Inter-company transfer treatment and inter-company invoicing. | Both companies' Accounting. |
| `JT-11` | Certification of the cutover opening balance. **Carried as `G-5`.** | Requires the accountant's opening trial balance. |
| `JT-12` | Period lock date policy and who may grant a backdating exception. | Accounting owns the lock. |

**This session closes none of these.** Every one is registered in file 12 and surfaced in file 14.

---

## 8. What Inventory Guarantees to Accounting

If the Joint decisions above are made, Inventory undertakes to deliver:

1. A valuation fact for every boundary-crossing movement, with no silent omissions.
2. A stated, versioned policy behind every cost figure.
3. A reproducible as-of-date position for quantity and value.
4. A native period guard with a recorded exception path and no global bypass.
5. An immutable movement history with reversal-only correction.
6. A reconciliation set (`RC-01` … `RC-10`) that can be run on demand.
7. A reason and an approver on every exception that changes value without a physical trade.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
