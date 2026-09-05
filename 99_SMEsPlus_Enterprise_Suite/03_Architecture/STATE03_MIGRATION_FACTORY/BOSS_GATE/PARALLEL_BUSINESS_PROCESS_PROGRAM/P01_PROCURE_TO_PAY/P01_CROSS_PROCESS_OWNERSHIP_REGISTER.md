# P01 — CROSS-PROCESS OWNERSHIP REGISTER

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.**

Supersedes nothing: `P01_CROSS_PROCESS_OWNERSHIP.md` from the previous round is retained in full
as audit lineage. This register is the **cross-process view after peer intake**, with ten peer
packages published.

Invariant: `ONE BUSINESS FACT → ONE CANONICAL EVENT OWNER → ONE ACCOUNTING EFFECT PATH`.

---

## 1. OWNERSHIP AFTER PEER INTAKE

| Business fact | P01 position | Peer position | Status |
|---|---|---|---|
| Commitment to buy | **P01 owns** | none contested | **SETTLED** |
| Goods physically received | **P01 owns** | none contested | **SETTLED** |
| First valuation of received goods | **P01 owns**; Inventory owns everything after | P11 holds valuation-policy ownership `NOT DECIDABLE` | **P11 OPEN** |
| Vendor payable | **P01 owns** | P05 notes an expense line can reach vendor AP **without any purchase document** | **CONTESTED — second route exists** |
| Received-not-billed obligation | **two candidate representations in P01** | P10 reaches the **same unassignable boundary** from the accrual side and offers two designs | **JOINTLY ESCALATED TO P11** |
| Capital-versus-expense classification | P01 **should** own it | P04: *"P01 must own it; today nobody does"* — no field exists on order or receipt | **CONFIRMED GAP — jointly evidenced** |
| Asset creation | P01 owns the **trigger**; P04 owns the asset | P04 agrees, and adds that the link to the initiating event is owned by nobody | **SETTLED on the boundary; a gap remains inside it** |
| Purchase tax | P01 supplies the base | P07 owns determination | **ROUTED** |
| Withholding | **unresolved in P01** | P07: created at **payment**, reported from a **P01 artefact** — two claims on one fact | **P11 / P07 OPEN** |
| Payment execution | P01 supplies the obligation | P06: payment intent has **four entry points, no single author** | **CONTESTED** |
| Bill payment status | authored by P01's document | **P06 mutates it** — two writers, one fact | **CONTESTED** |
| Settlement and FX | P01 consumes | P06 owns | **SETTLED** |
| Vendor advance | **P01 owns** — answered this round | P05 asked; P06 flags the pre-obligation window | **ANSWERED; window open** |
| Landed cost | P01 supplies the trace | P11 `DEP-07`, joint with Inventory, **audit veto retained** | **P11 OPEN — P01 input now supplied** |
| Price-difference account scope | P01 supplies evidence | P11 `DEP-06`, contradiction with Inventory | **P11 OPEN** |
| Subcontract purchase | P01 marks the boundary | P03 owns manufacturing | **ROUTED — INSTALLED BUT NOT EXERCISED** in the fourth database (`ERR-P01-15`). An expert additionally reports the v18 credit-split construct is **gone in v19**, and owes P03 a correction to its `OWN-03` premise |
| Analytic allocation on the bill line | P01 territory | P09 found the defect and **handed it over without adjudicating** | **P01 ACCEPTS INTAKE** |
| Service period on a bill line | **P01 owes P10** | P10 needs it; P01 found no such field | **P01 GAP** |
| Cross-company document generation | P01 is a **trigger surface** | P08 holds the intercompany settlement boundary open | **P11 OPEN — now LIVE, see §2** |
| Prior-period attribution | P01 evidences re-dating | P11 `DEP-15`: **no mechanism exists in the reference at all** | **CONFIRMED — P11 owns** |

---

## 2. THE TOLERANCE-ZERO ITEM, ESCALATED

Previously assessed as a risk. **This round establishes it is live.**

Both intercompany bridges are **installed in both deployed v19 databases** and in **neither**
v16 one. **CORRECTED (`ERR-P01-21`): the bill path is triggered by a *customer invoice* — a P02
object — not by a vendor bill.** So on the v19 line, approving a purchase order, or posting a
customer invoice, whose counterparty
resolves to another company **will** create a document in that other company — as the superuser
by default, optionally auto-posted.

Under the scope-aware constitution the defect is not that the effect is cross-company. It is
that a **COMPANY-scoped financial effect** is raised in a company whose ownership of that effect
is **inferred from a TENANT-scoped contacts hierarchy**, resolved with elevated privilege,
first match winning. `REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY`; the observed behaviour is to
proceed.

Whether any tenant test exists is **class B** and is under independent challenge this round.

**Disposition: `TOLERANCE-ZERO — HOLD`, escalated from latent to live.**

---

## 3. DOUBLE-COUNTING ATTACK — RESULTS AFTER PEER INTAKE

| Attack | Result | Class |
|---|---|---|
| DOUBLE RECEIPT | not found | **B** — scope: the declared creation-site population |
| DOUBLE VALUATION | **v18: two live representations of received-not-billed. v19 deployments: none at all** | FACT VERIFIED that both paths exist in v18 |
| DOUBLE LIABILITY | **found — a second route.** P05: an expense line can post to vendor AP with no purchase document | **PEER-REPORTED**, not re-derived by P01 |
| DOUBLE AP | not found within P01's own paths | **B** |
| DOUBLE TAX | routed to P07 | **C** |
| DOUBLE WHT | **compounding across partial payments** — under disproof challenge | FACT VERIFIED pending challenge |
| DOUBLE PAYMENT | not found | **B** |
| DOUBLE RECONCILIATION | P06 owns; two writers on payment status | **PEER-REPORTED** |
| DUPLICATE LANDED COST | assigned to an expert; landed cost is **installed everywhere** | **C pending** |
| DUPLICATE SUBCONTRACT COST | **installed but not exercised** in `D4` | **C** |
| **CORRECTION BY SILENT DELETION** | **found** — derived journal items deleted on reset-to-draft and cancel; under disproof challenge | FACT VERIFIED pending challenge |
| **DOUBLE EXPENSE ON VENDOR ADVANCE** | **new this round** — advance defaults to an expense account; netting unproven | SUPPORTED INTERPRETATION |

---

## 4. WHAT P01 HANDS EACH PEER

| Peer | Handoff |
|---|---|
| **P02** | The vendor-side mirror answer; independent corroboration that the valuation chart is unwired |
| **P03** | Landed-cost and subcontract evidence, boundary marked, **not decided** |
| **P05** | Vendor-advance ownership **accepted**; WHT rating contested |
| **P06** | No payment entry without an outstanding account; corroboration of the four-entry-point problem |
| **P07** | WHT arithmetic, PND mapping contradiction, certificate population — **statutory determination is P07's** |
| **P08** | Period-lock re-dating; correction by deletion; **and that in the v19 deployments no receipt ever reaches the ledger**, which changes what a period comparative means |
| **P09** | Acceptance of the bill-line analytic overwrite as P01 territory |
| **P10** | The missing service-period field; P01's half of the accrual boundary |
| **P11** | All of the above, the scope matrix, and 32 classified unresolved items |

**P01 makes no target-architecture decision and no Boss-level decision anywhere in this
register.**
