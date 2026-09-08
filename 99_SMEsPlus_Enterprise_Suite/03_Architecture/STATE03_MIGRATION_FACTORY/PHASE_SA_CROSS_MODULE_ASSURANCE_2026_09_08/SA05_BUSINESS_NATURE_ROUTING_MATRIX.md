# SA05 — BUSINESS NATURE ROUTING MATRIX

Status: **HOLD** — routing shape determined; four routes cannot be closed on current evidence.
Governing law: master prompt §6 — routing is determined by Business Nature, not module name.

---

## 1. The determination Phase SA must make

Master prompt §6 supplies an illustrative routing tree and states it is *"illustrative, not a
fixed architecture"*. Phase SA must independently determine the correct SMEsPlus routing for
every Business Nature.

`SA00` §7 measured the evidence available to make that determination: **supply routing is the
least-evidenced of all twenty-two domains (81 blobs, 3.0% of corpus)**. This register
therefore separates what can be *determined* from what must be *researched*, and does not
present the second as the first.

---

## 2. SMEsPlus routing principle — determined

### 2.1 The determination

> **Routing is resolved per order line from a Supply Nature, which is a resolved attribute of
> the line — not a property of the module that created the document, and not a property of the
> product master alone.**

### 2.2 Why this and not the alternatives

| Alternative considered | Why not selected |
|---|---|
| Route by **module** (a sale always goes to Inventory) | Contradicted by dropship and service, where no stock movement occurs in the seller's own warehouse. Master prompt §24 prohibits "assume Sales always means Inventory". |
| Route by **product master flag alone** | A product may be stocked for one customer and dropshipped for another, in the same company, in the same period. A single master flag cannot express a per-line decision. |
| Route by **document type** (separate order types per nature) | Forces the commercial user to know the fulfilment strategy at order entry, and fragments one customer order into several documents when a basket mixes natures. Rejected on user-fitness grounds. |
| Route by **resolved line attribute** (selected) | A single customer order can carry lines of different natures; each line routes independently; the commercial document stays whole. |

### 2.3 Clean-room rationale

This determination is derived from the business requirement that one customer order may mix
a stocked item, a manufactured item and a service. It is not inherited from any reference
system's document or state model. Common terminology (order, line, delivery) is reused because
it is semantically correct, not because a reference system uses it.

### 2.4 Nature DNA — what SMEsPlus does differently

The Supply Nature is **resolved and then recorded as an immutable fact on the line**, with the
resolution inputs retained. A later change of policy does not silently re-route work already
in flight, and an auditor can reconstruct why a given line took the route it took. The
resolution is Tenant + Company bounded.

**Status of §2:** `DETERMINED — shape`. The *shape* is determined. The *resolution rule*
(which inputs decide the nature, in what precedence) is **not** determined — see §5.

---

## 3. Routing matrix by Business Nature

`INV` = inventory impact required. `ACC` = accounting recognition required.
Status values: `DETERMINED` / `PARTIAL` / `HOLD`.

| # | Business Nature | Determined route | INV | ACC | Status | Basis / blocker |
|---|---|---|---|---|---|---|
| BN-01 | Stocked goods sale | Order → Reserve → Pick/pack/ship → Deliver → Inventory out → AR recognition → Payment → Reconcile | Yes | Yes | `PARTIAL` | Inventory movement + reservation evidenced (`dcb92278`, R4). AR recognition evidenced (P02). **Cancellation-gate symmetry open — Group A A1.** |
| BN-02 | Manufacture-to-order sale | Order → Demand → Manufacturing order → RM requirement → RM issue → Production → FG receipt → Deliver → AR → Accounting | Yes | Yes | `PARTIAL` | Manufacturing cost flow evidenced (P03 `bc767a81`). **BOM/routing operating semantics thin (48 blobs).** |
| BN-03 | Manufacture-to-stock sale | Production planned independently of the order; sale then routes as BN-01 | Yes | Yes | `PARTIAL` | Same basis as BN-02; the decoupling point is not evidenced. |
| BN-04 | RM shortage during manufacture | Manufacturing → shortage → Purchase → Receipt → Inventory → Production resumes | Yes | Yes | **`HOLD`** | The shortage→purchase trigger is a supply-routing decision; SA-D05 evidence is 81 blobs. Trigger, ownership and reservation interaction not evidenced. |
| BN-05 | Dropship sale | Order → Purchase to vendor → Vendor ships to customer → AP + AR recognition → Accounting | **No** own-warehouse movement | Yes | **`HOLD`** | No subject-scoped evidence found for dropship in the corpus. Whether SMEsPlus records a non-physical inventory event for title passage is **undetermined** — this is an accounting-material question, not a convenience. |
| BN-06 | Buy-to-order / MTO purchase | Order → Purchase → Receipt → Inventory → Deliver → AR → Accounting | Yes | Yes | `PARTIAL` | Purchase→receipt→AP evidenced (P01 `b820b29b`). The order-to-purchase linkage and its reservation semantics are not. |
| BN-07 | Kit / bundle sale | Order → Component resolution → Component inventory movement → Deliver → AR → Accounting | Yes | Yes | **`HOLD`** | Component resolution point (order entry vs delivery), and whether the kit or its components carry the cost, are undetermined. Directly governed by BD-ACC-03A/03B, which set valuation and costing at Product Category — **a kit and its components may sit in different categories, so the kit's costing policy is ambiguous by construction.** |
| BN-08 | Service sale | Order → Service delivery / completion evidence → AR recognition → Payment → Accounting | No | Yes | **`HOLD`** | SA-D17 is `THIN` (16 blobs). The *completion evidence* that triggers recognition is not evidenced. Boss has ruled the Service menu (`e47f0f2f`) without an underlying process study. |
| BN-09 | Time-based / subscription recognition | Contract → Period recognition schedule → Periodic recognition → AR → Accounting | No | Yes | `PARTIAL` | P10 evidenced (`1fea562c`), terminal HOLD; recognition event collapsed into the posting act is its recorded root cause. |
| BN-10 | Project-based sale | Project → operational progress → source facts from Sales/Purchase/Inventory/Timesheet → Analytic dimension → Accounting | Varies | Yes | **`HOLD`** | Boss decision `fa57d10f` sets the Project ↔ Analytic boundary. SA-D18 is `THIN` (4 blobs) — the least-evidenced domain in the entire register. |
| BN-11 | Asset acquisition | Purchase → Receipt → Capitalization → Asset register → Depreciation → Accounting | Conditional | Yes | `PARTIAL` | P04 + asset deep research evidenced. Boss `36c62ab3` separates Equipment from Fixed Asset; the Equipment side (SA-D20) is thin. |
| BN-12 | Non-stock expense purchase | Purchase/Expense → Approval → Payable → Payment → Accounting | No | Yes | `PARTIAL` | P05 evidenced (`205e0ac3`), terminal HOLD. |
| BN-13 | Sales return | Return authorisation → Inventory return → Credit/reversal → Accounting | Yes | Yes | `PARTIAL` | Group A exception matrix (`8b0993d8` file 10). Reversal event identity governed by BD-ACC-01. |
| BN-14 | Purchase return | Return → Inventory return → Debit/reversal → Accounting | Yes | Yes | `PARTIAL` | Same basis. |
| BN-15 | Scrap / by-product / production variance | Production → Scrap or by-product → Inventory adjust → Accounting | Yes | Yes | `PARTIAL` | P03 evidenced (265 blobs on scrap/by-product/variance). Fixed-overhead injection path is a recorded P03 open item. |
| BN-16 | Internal transfer | Location A → Location B; company-crossing transfers are a separate nature | Yes | Conditional | `PARTIAL` | Inventory programme evidenced. Cross-company transfer interacts with BD-ACC-02 company-scoped tax. |
| BN-17 | Quality hold / inspection outcome | Receipt or production → Inspection → Release or reject → route to Inventory or Return | Yes | Conditional | **`HOLD`** | SA-D19 `THIN` (20 blobs). Boss ruled the Quality menu (`4c469f8e`); no process evidence. Quality hold changes *when* stock becomes available and *when* cost is recognised — it is on the accounting path, not beside it. |
| BN-18 | Equipment breakdown during production | Work Order → breakdown → Maintenance Request → Maintenance Order → completion → Work Order resumes | Conditional | Conditional | **`HOLD`** | Route is stated verbatim in Boss decision `a11c9e7b` §3. SA-D20 `THIN`. Whether maintenance cost reaches production cost is undetermined. |

### 3.1 Routing status summary

| Status | Count | Business Natures |
|---|---|---|
| `DETERMINED` | 0 | — |
| `PARTIAL` | 11 | BN-01, 02, 03, 06, 09, 11, 12, 13, 14, 15, 16 |
| `HOLD` | 7 | BN-04, 05, 07, 08, 10, 17, 18 |

**No Business Nature is fully determined.** Eleven have an evidenced spine with a named
open element; seven cannot be routed on current evidence.

---

## 4. SA05-F-01 — the routing law and the evidence base are inversely correlated

The master prompt makes Business-Nature routing the constitutional core of Phase SA (§6) and
prohibits seven specific routing assumptions (§24). The measured evidence base is weakest on
exactly that subject: SA-D05 supply routing is the lowest-coverage domain of twenty-two.

Every one of the seven `HOLD` natures depends on a domain classified `THIN` in `SA01`:

| HOLD nature | Depends on thin domain |
|---|---|
| BN-04 RM shortage → purchase | SA-D05 |
| BN-05 Dropship | SA-D05 |
| BN-07 Kit / bundle | SA-D05 |
| BN-08 Service | SA-D17 |
| BN-10 Project-based | SA-D18 |
| BN-17 Quality hold | SA-D19 |
| BN-18 Equipment breakdown | SA-D20 |

This is a single root cause with seven symptoms, not seven independent gaps. Closing SA-D05,
D17, D18, D19 and D20 closes all seven. This is recorded as one targeted research programme in
`SA16`, not seven.

---

## 5. SA05-F-02 — the Supply Nature resolution rule is undetermined, and it is decision-shaped

§2 determines that routing resolves from a per-line Supply Nature. It does **not** determine
what resolves that nature. Candidate inputs, each with a real business case:

- product master default;
- product category policy (already the authority for valuation and costing under BD-ACC-03A/03B);
- customer or customer-segment agreement (a dropship customer);
- warehouse or company policy;
- explicit per-line user selection;
- availability at the moment of order confirmation (dynamic resolution).

Precedence between them is a **policy decision with accounting consequence**: it determines
whether a given sale creates a stock movement at all, and therefore whether COGS arises and
when. It is not a technical detail and cannot be defaulted silently.

**Classification:** this is a genuine Boss-authority matter under master prompt §26 — it is a
material alternative selection with cross-domain effect. It is carried to `SA19`, with the
alternatives and their consequences stated, **after** targeted research bounds them. It is
**not** escalated as a raw question.

---

## 6. Inventory and accounting convergence check on this matrix

Per master prompt §7.1 and §7.2, every row above carries an explicit INV and ACC column, and
no row is left blank. Rows where inventory impact is `No` (BN-05 dropship, BN-08 service,
BN-09 subscription, BN-12 expense) are **deliberate determinations that no stock movement
occurs**, not unexamined blanks — though BN-05's is itself `HOLD` because title passage may
require a non-physical inventory event.

No row carries `ACC = No`. Every Business Nature in SMEsPlus has an accounting consequence to
determine, consistent with master prompt §7.2.

---

`SA05 — HOLD`. The routing shape is determined; seven of eighteen Business Natures cannot be
routed on current evidence, from one root cause, routed to targeted Very Deep Research.

Boss remains the sole Final Approver.

---

## 7. Addendum — evidence strengthening two `HOLD` natures

**BN-07 Kit / bundle.** The `HOLD` is now supported by a bounded measured absence rather than
by an undetermined design point: a declared pattern over four inventory-package populations
returns zero files, with a positive control confirming the pattern fires (`SA06-F-03`). The
permitted claim is *not found within those populations* — the routing determination remains
outstanding either way.

**BN-15 Scrap / by-product / variance** (recorded `PARTIAL` above) — the manufacturing lineage
records that all scrap is abnormal in effect, that there is no normal/abnormal distinction and
no re-absorption mechanism, and that the operation link is informational so **scrap has no cost
causality**. Co-products are not modelled as a distinct concept. One variance of nine is
recognised, and the information needed for an efficiency variance *"is computed and then
discarded"*.

This does not change BN-15's `PARTIAL` classification — the route exists and stock reconciles —
but it moves the open element from *valuation detail* to *cost causality*, which is a design
question for SMEsPlus rather than a configuration one. Carried to `SA16` as scope for the
manufacturing side of the consolidated programme.
