# SA_CORR2_05 — INVENTORY CONVERGENCE RECONCILIATION
## CP-SA-C2-40 — STOCK-AFFECTING FLOWS RECONCILED

Session: `[SMEPLUS-26-09-08-PHASE-SA-CORR2-XMOD-001]`
Governing law: master prompt §6 — every stock-affecting flow must reconcile to Inventory.
Supersedes at claim level: `SA06` §2.1 counts and `SA06-F-01`. Carries unchanged: `SA06` §1
(single physical-movement ledger, six non-conflatable quantity concepts) and `SA06-F-04`…`F-06`.

---

## 1. Boss-approved policy preserved, and one term defined because it has moved

Preserved without amendment (master prompt §6):

- **Inventory Valuation Recognition: `Periodic | Perpetual`, at Product Category only.**
- **Costing Method: `Standard | Average | FIFO`, at Product Category only.**

`SA_CORR2_01` §5 establishes, on primary evidence, that in the current reference generation the
word **`Perpetual` denotes recognition at invoicing**, and that a target policy of *COGS at delivery
for a perpetual storable* is **not selectable there** — it requires a mechanism the product does not
offer, not a setting.

**The Boss policy is unaffected. What is affected is the vocabulary.** `ND-10` (`SA_CORR2_01` §5.1)
therefore stands as a determination of this register:

> **SMEsPlus defines `Perpetual` as recognition at the physical movement and `Periodic` as
> recognition at period close, and states both definitions wherever the terms appear.**

No Boss authority is required for a definition that makes an existing Boss policy unambiguous.
If Boss intends `Perpetual` to mean recognition at invoicing, that is a different policy and this
register would be wrong — which is why the definition is stated rather than assumed.

---

## 2. Reconciliation matrix — re-adjudicated

Status vocabulary unchanged from `SA06`. Rows whose status changes are marked **▲**.

| # | Stock-affecting flow | Status (`SA06`) | **CORR2 status** | Basis |
|---|---|---|---|---|
| IR-01 | Sales delivery | `RECONCILED` | `RECONCILED` | unchanged |
| IR-02 | Purchase receipt | `RECONCILED` | `RECONCILED` | unchanged |
| IR-03 | Customer return | `RECONCILED` | `RECONCILED` | unchanged |
| IR-04 | Vendor return | `RECONCILED` | `RECONCILED` | unchanged |
| IR-05 | Manufacturing RM consumption | `RECONCILED` | `RECONCILED` | unchanged |
| IR-06 | Finished-goods receipt | `RECONCILED` | `RECONCILED` | unchanged |
| IR-07 | Scrap | `RECONCILED` | `RECONCILED — no cost causality` | carried from `SA05` §7 |
| IR-08 | By-product | `RECONCILED — valuation open` | unchanged | |
| IR-09 | Internal transfer | `RECONCILED` | **▲ `RECONCILED — RULE NOW STATED`** | §3 |
| IR-10 | Inventory adjustment | `RECONCILED` | `RECONCILED` | unchanged |
| IR-11 | Partial fulfilment / remaining supply | `RECONCILED — no consumer` | unchanged | |
| **IR-12** | **Kit / bundle component movement** | `NOT RECONCILED` | **▲ `RECONCILED — RESOLUTION POINT DETERMINED`** | §4 |
| **IR-13** | **Dropship — title passes without own-warehouse movement** | `NOT RECONCILED` | **▲ `RECONCILED — AS A MEASURED NEGATIVE`** | `SA_CORR2_01` §4 |
| **IR-14** | **Quality hold / rejected receipt** | `NOT RECONCILED` | **▲ `RECONCILED — RULE DETERMINED`** | §3 |
| IR-15 | Asset capitalization from stock | `PARTIAL` | `PARTIAL` | unchanged |
| IR-16 | Cross-company transfer | `PARTIAL` | `PARTIAL` | unchanged |
| **IR-17** | **Consumption by a service or project** | `NOT RECONCILED` | **▲ `PARTIAL`** | §5 |
| **IR-18** | **Equipment / maintenance consumption** *(added by this register)* | — | **`NOT RECONCILED`** | §6 |

### 2.1 Count

| Status | `SA06` | **CORR2** |
|---|---|---|
| `RECONCILED` (incl. as a measured negative) | 11 | **14** — IR-01…IR-14 |
| `PARTIAL` | 2 | **3** — IR-15, IR-16, IR-17 |
| `NOT RECONCILED` | 4 | **1** — IR-18 |
| **Total stock-affecting flows** | **17** | **18** |

Check, executed by reading the status column of §2 rather than asserted: **14 + 3 + 1 = 18**, and
every identifier `IR-01`…`IR-18` appears exactly once in §2.

*(**Corrected after adversarial challenge.** This table first published `13 / 4 / 1`. The total was
right and the classes were wrong — `IR-14` was counted as `PARTIAL` when §2 grades it `RECONCILED`.
**An identifier check cannot see a mis-assigned class**, which is why the enumeration check above
passed while the tally was wrong. The check unit must match the defect.)*

---

## 3. `C2-F-14` — one rule reconciles three flows, and it was already written

`IR-09`, `IR-14` and the internal-transfer neutrality question (`SA06-F-05`) are the same question,
and the Inventory functional design answers it:

> A movement between two internal company locations changes **where** stock is and creates **no
> accounting consequence**. A movement crossing the boundary between an internal location and a
> non-internal counterpart — a supplier, a customer, a loss, an adjustment counterpart, production —
> changes **whether** the company owns the stock and therefore **emits a valuation fact** for
> Accounting to post. **This single rule governs receipts, deliveries, returns, scrap, adjustments
> and manufacturing consumption alike.**

composed with the quality-hold determination in the same package:

> **Quality holds are a location state, not a product state:** goods awaiting or failing inspection
> sit in a quality-check or quarantine place and are therefore **visible in on-hand but excluded
> from available.**

**The composition is the answer `SA06` said was undetermined:**

| Question `SA06` IR-14 left open | Answer |
|---|---|
| Is a quality hold an inventory event? | **Yes** — an internal→internal movement |
| Is it a return? | **No** |
| Does it change when cost is recognised? | **No** — internal→internal emits no valuation fact. **Only the disposition moves cost**: reject-to-supplier crosses to a non-internal counterpart; scrap crosses to a loss counterpart |

And it is consistent with the Boss-ruled route, read verbatim from the decision body:

> `Purchase Receipt -> Incoming Inspection -> Accept / Hold / Reject -> Inventory`
> `Manufacturing -> In-Process / Final Inspection -> Pass / Hold / Rework / Scrap -> Inventory`
> — `4c469f8e`, status `BOSS APPROVED DIRECTION / DETAIL DESIGN PENDING`

**Why this was missed.** The rule lives in the Inventory **Final Solution** package. `SA06` built
its matrix from the Inventory **reopen/research** packages and the Group A backbone. Both are
Inventory; one is design output and the other is research output, and the register that needed the
answer read only the second. **A domain is not a path set.**

### 3.1 The neutrality caveat survives and is sharpened

`SA06-F-05` records that internal-transfer financial neutrality *"is protected only by
configuration; no independent check exists"*. **That remains true and now matters more**, because
the same rule is what makes a quality hold cost-neutral. A configuration change that breaks
transfer neutrality **also silently gives a quality hold an accounting consequence.** One
unprotected invariant, two flows. Carried to `SA_CORR2_10` and to the Pre-Test control list.

---

## 4. `IR-12` kit — the resolution point is determined

`SA06` classified this `NOT RECONCILED` on an undetermined resolution point, and `SA06-F-03`
correctly bounded a measured absence to four inventory populations. **The determination exists
outside those four populations.**

Established: a kit is a **structure-level flag, not a product classification**. When a sale line
carries one, the fulfilment flow is redirected to create physical movements **for the components,
not for the parent**, at rule-dispatch time on the sell side. **The parent product never moves.**

So the movement reconciles: **components move, the kit does not.** `IR-12` is `RECONCILED`.

**`SA06-F-03` is not withdrawn — it is exactly right within its declared bound.** It said *"no kit
or bill-of-material handling was found within these four populations"*, published its pattern, ran a
positive control, and explicitly refused the wider claim. **That is the discipline working.** The
defect was not in `SA06-F-03`; it was in `SA06` §2 promoting a bounded absence to a matrix status
without searching outside the bound.

> **A correctly bounded negative becomes a false status the moment a consumer reads it without its
> bound.** `SA06-F-03` carried its bound; the row that consumed it did not.

**What remains open on kits is not inventory.** It is `C2-D-03`: a kit and its components may sit in
different Product Categories, and `BD-ACC-03A/03B` set valuation and costing at category level.
That is an ambiguity inside a Boss ruling and is carried to `SA_CORR2_13`.

---

## 5. `IR-17` service / project consumption — `NOT RECONCILED` → `PARTIAL`

The evidenced position is determinate and it is a negative:

> Structurally, consumable and service items **never** trigger the automatic
> inventory-valuation-driven mechanism — any accounting effect for them flows through ordinary
> purchase/expense or revenue-recognition posting, **not inventory-valuation-driven cost of sales**.

and the level at which the distinction applies is established:

> The correct application level for the three-way split is the **line item / SKU**, not the
> transaction or document as a whole.

**So a service does not consume stock, and that is a determination rather than a blank.** What
remains `PARTIAL` is the case where a *service or project consumes a stocked item* — for which the
governing rule is §3's boundary rule (internal → non-internal counterpart = production/loss
counterpart ⇒ valuation fact). That composition is stated here for the first time and has not been
tested against a project scenario. `PARTIAL`, not `RECONCILED`.

---

## 6. `IR-18` — a stock-affecting flow no register carried

Added under master prompt §6's requirement that **every** stock-affecting flow reconcile.

Maintenance consumes spare parts. Spare parts are stock. The flow therefore affects inventory —
and neither `SA06`'s seventeen rows nor `SA04`'s twenty-eight routes contains it.

The evidenced position, `FACT VERIFIED` with a declared denominator:

> **Denominator for the negative:** every source file in the maintenance module. **Zero**
> references to the journal-entry model; **zero** to the analytic model.
> **Maintenance cost is a statistical float.** There is no journal entry, no analytic item, no cost
> object and therefore **no accounting attribution of a non-productive cause anywhere in the
> reference product.**

**`C2-F-15`.** A maintenance part issue is a stock movement whose **cost has no destination**. Under
§3's boundary rule it crosses from an internal location to a consumption counterpart and therefore
**emits a valuation fact**, while the reference product has nowhere to send it. Status
`NOT RECONCILED` — and it is the only remaining one.

This is also the missing half of `SA11-F-01`: TAS 2 ¶12 expressly requires **maintenance of
production equipment** to be absorbed into conversion cost. `SA11-F-01` established that
depreciation has no path; this establishes that maintenance has no accounting existence at all.
**One standards requirement, two absent mechanisms, in two registers that never met.**

---

## 7. Reservation, availability and the rest of the master-prompt §6 checklist

| Required verification | Status | Source |
|---|---|---|
| Reservation | `SPECIFIED — NOT FIRST-CLASS` | `SA06-F-04` / `ND-05`, carried unchanged |
| Availability | `RECONCILED` — six non-conflatable quantity concepts; quality hold excludes from available but not from on-hand | `SA06` §1; §3 above |
| Inbound / outbound movement | `RECONCILED` | `SA06` IR-01/IR-02 |
| Manufacturing consumption / receipt | `RECONCILED` | IR-05, IR-06 |
| Return | `RECONCILED` — and the only correction route after a completed movement | IR-03, IR-04 |
| Scrap | `RECONCILED — no cost causality` | IR-07 |
| Adjustment | `RECONCILED` — and an adjustment can silently reduce a reservation | IR-10; `SA06-F-04` |
| Transfer | `RECONCILED — rule now stated` | IR-09; §3 |
| Valuation trigger | **`DETERMINED`** — the internal / non-internal boundary rule | §3 |
| Negative-stock policy | `UNENFORCED` — application-layer convention only, no database guarantee | `SA06-F-02`, carried |
| Costing-method interaction | `PARTIAL` — Boss policy preserved; the term `Perpetual` defined at `ND-10` | §1 |
| Reversal / correction | `RECONCILED` — return is the only route; reversal creates a new event under `BD-ACC-01` | `SA09` |

---

## 8. What did not move, and is not claimed to have moved

- **`0 of 22` cross-proof scenarios remain unprovable**, and this register does not change that.
  Handoff element 10 blocks them all (`SA_CORR2_04` §3).
- **`0 of 8` isolation proofs, `0 of 13` enforcement surfaces, `0 of 52` negative access tests.**
  Reconciling a flow is not proving an invariant.
- **No Inventory package's terminal state was improved by this session**, and none is claimed to be.
  Every status change above was produced by reading an existing package that a prior register had
  not reached.

---

`CP-SA-C2-40 — STOCK-AFFECTING FLOWS RECONCILED (execution status).` **13 of 18 reconciled, 4
partial, 1 not reconciled**, against 11 / 2 / 4 of 17 before.

Checkpoint completion is **not** Boss approval.

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
