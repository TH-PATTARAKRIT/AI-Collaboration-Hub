# SA06 — INVENTORY RECONCILIATION MATRIX
## CP-SA-40 — INVENTORY RECONCILIATION

Status: **HOLD**
Governing law: master prompt §7.1 — **every stock-affecting flow must reconcile to Inventory.**

---

## 1. The architectural fact this matrix rests on

Group A evidence (`8b0993d8`) records that Inventory holds **the single physical-movement
ledger for the whole suite** — other domains extend the same movement records rather than
keeping separate ledgers.

Phase SA position: **SMEsPlus adopts a single physical-movement ledger as an independent
design determination.** Rationale — a second ledger creates a reconciliation obligation that
can fail silently, and BD-ACC-01 makes the accounting event depend on movement facts, so a
divergence between two stock ledgers becomes a divergence in the general ledger. This is
adopted because it is right for SMEsPlus, not because the reference estate does it.

Corollary adopted with it: **quantity concepts must not be conflated.** Six are evidenced as
distinct — On-Hand, Reserved, Available, Incoming, Outgoing, Forecasted — and a seventh
distinction is state-dependent: the same movement quantity means *"reserved so far"* before
completion and *"actually moved"* after. SMEsPlus will name these separately.

---

## 2. Reconciliation matrix

| # | Stock-affecting flow | Reconciles to Inventory | Evidence | Status |
|---|---|---|---|---|
| IR-01 | Sales delivery | Yes — completed movement drives delivered quantity | Group A `8b0993d8`; R4 inventory programme | `RECONCILED` |
| IR-02 | Purchase receipt | Yes — direct synchronous receipt expectation, completed movement drives received quantity | Group A | `RECONCILED` |
| IR-03 | Customer return | Yes — return transfer; the traceability primitive sits on the movement | Group A | `RECONCILED` |
| IR-04 | Vendor return | Yes — structurally identical | Group A | `RECONCILED` |
| IR-05 | Manufacturing raw-material consumption | Yes | P03 `bc767a81` | `RECONCILED` |
| IR-06 | Finished-goods receipt | Yes | P03 | `RECONCILED` |
| IR-07 | Scrap | Yes | P03 (265 blobs on scrap / by-product / variance) | `RECONCILED` |
| IR-08 | By-product | Yes | P03 | `RECONCILED — valuation open` |
| IR-09 | Internal transfer | Yes | Inventory programme | `RECONCILED` |
| IR-10 | Inventory adjustment | Yes | Inventory programme | `RECONCILED` |
| IR-11 | Partial fulfilment / remaining supply | Yes — self-referential remaining-supply record | Group A | `RECONCILED — no commercial consumer (`SA03-F-01`)` |
| IR-12 | Kit / bundle component movement | **Undetermined** — component resolution point unknown | — | **`NOT RECONCILED`** — `SA05` BN-07 |
| IR-13 | Dropship — title passes without own-warehouse movement | **Undetermined** — whether a non-physical inventory event is required | — | **`NOT RECONCILED`** — `SA05` BN-05 |
| IR-14 | Quality hold / rejected receipt | **Undetermined** — is a rejection an inventory event, a return, or neither | — | **`NOT RECONCILED`** — `SA05` BN-17 |
| IR-15 | Asset capitalization from stock | Conditional — Boss `36c62ab3` separates Equipment from Fixed Asset | P04, asset programme | `PARTIAL` |
| IR-16 | Cross-company transfer | Yes physically; company-scoped tax interaction under BD-ACC-02 open | Inventory programme | `PARTIAL` |
| IR-17 | Consumption by a service or project | **Undetermined** | — | **`NOT RECONCILED`** — SA-D17, SA-D18 |

### 2.1 Count

| Status | Count |
|---|---|
| `RECONCILED` | 11 |
| `PARTIAL` | 2 |
| `NOT RECONCILED` | 4 |
| **Total stock-affecting flows** | **17** |

---

## 3. SA06-F-01 — the four unreconciled flows are the four that do not move goods normally

IR-12 kit, IR-13 dropship, IR-14 quality rejection and IR-17 service/project consumption are
precisely the flows where **the physical movement is unusual, indirect, or absent**. Every
flow that moves a normal item from a normal location to another normal location reconciles.

The rule "every stock-affecting flow must reconcile to Inventory" (§7.1) is satisfied wherever
the flow is obviously stock-affecting. It is unsatisfied wherever **whether the flow is
stock-affecting at all is the open question.** That is the harder half of the rule and it is
the half that is open.

## 4. SA06-F-02 — an unenforced negative-stock boundary sits directly under the accounting event

`SA09-F-02` records that stock cannot go negative only by application-layer convention, with
no database-level guarantee, and that the bin-key uniqueness is reconciled after the fact by a
merge routine.

Under BD-ACC-01 the accounting event depends on the movement fact. A stock quantity that can go
negative or be double-written is therefore not only an operational concern — it is an input to
the ledger. **SMEsPlus must own this invariant in its core**, per the extension constitution
`02_BOSS_DECISION_CORE_EXTENSION_BOUNDARY` `CE-05`, which forbids extensions breaking financial,
transaction or reconciliation invariants. An invariant the core does not enforce cannot be
protected from extensions by that rule.

Carried to `SA12` (clean-room / Nature DNA) and `SA19`.

---

`CP-SA-40 — HOLD`. Eleven of seventeen stock-affecting flows reconcile; four cannot be
reconciled until the supply-routing and quality triggers are determined.

Boss remains the sole Final Approver.

---

## 5. Addendum — SMEs Core inventory-domain evidence intake

### SA06-F-03 — the kit / bill-of-material absence is a measured absence, with the pattern published

`IR-12` was classified `NOT RECONCILED` above on the strength of an undetermined resolution
point. The inventory-domain extraction supplies a stronger and properly bounded statement:

| Clause | Declaration |
|---|---|
| POPULATION | all files of the R4 L1–L12 execution package (`fc0b1688`, 26 files) **and** the three multi-tenant invariant package folders (`dcb92278` 17, `bd096ffa` 18, `a57bd555` 17) |
| PATTERN | case-insensitive `\bkits?\b\|phantom\|bill of material` |
| UNIT | one file with ≥ 1 match |
| RESULT | **0 files across all four populations** |
| POSITIVE CONTROL | the identical pattern returns 1 and 9 hits on two manufacturing-lineage files — **the pattern fires** |

The permitted form of this claim is therefore *"no kit or bill-of-material handling was found
within these four populations"* — **not** *"no kit handling exists"*. The extraction records
that whether this is a scope decision or an omission is not determinable from these packages.
Carried to `SA16` TVDR-01 as a bounded question, not asserted as a defect.

### SA06-F-04 — a reservation is not a first-class fact, and an adjustment can silently break a customer promise

Recorded in the R4 lineage (`fc0b1688`): reservation is held as a *quantity on the balance
record* rather than as an independent, addressable reservation record. The consequence, quoted:

> An adjustment can therefore reduce a reservation without any actor intending to break a
> customer promise.

Status in its own register: *"Semantic drift confirmed as structurally possible … a reservation
must be a first-class, addressable fact if the promise it represents is to survive an
adjustment. Carried, not closed."* The associated concurrency conflict is recorded as an
unarbitrated conflict *"reconciled to a hold, not settled"*, and the reservation-policy default
(reserve at order confirmation vs at warehouse pick time) is an open gap requiring user validation.

**Phase SA determination (Nature DNA, ND-05).** SMEsPlus makes **a reservation a first-class,
addressable business fact with its own identity and lifecycle.** Independent rationale: a
reservation is a *promise to a customer*, and `SA03` already shows the commercial side reads
availability only advisorily. If the promise is a derived quantity, no control can detect that
it was silently consumed, and no audit can show who consumed it. This is SMEsPlus choosing
differently from the evidenced reference shape, and the reason is stated.

Consequence to carry: on-hand, reserved and incoming are recorded in that lineage as *"not
three separate risks; they are one missing capability expressed three times"* — a deterministic
identity that makes a retry safe. That is handoff element 15, and it is one of the three
elements recorded as unsuppliable.

### SA06-F-05 — internal-transfer financial neutrality is protected only by configuration

R4 records that internal-to-internal movement must not produce a value event, and that this
neutrality *"is protected only by configuration; no independent check exists"*.

This bears directly on `IR-09`/`AR-10`. A neutrality that depends on configuration is a
neutrality that a configuration change silently revokes. **SMEsPlus position:** context-internal
transfer neutrality is an invariant the core asserts and a control verifies, not a
configuration outcome. Carried to `SA17`.

### SA06-F-06 — the three unsuppliable handoff elements are not downstream of the accounting dependency

Quoted from the Inventory Boss review package:

> **None of these three is caused by the Accounting COGS Gap. All three are Lane A.**

and

> no material Inventory-to-Accounting handoff can be declared verified, and 0 of the 22
> Boss-approved cross-proof scenarios can be proven — even if every one of `JT-01` through
> `JT-12` were resolved tomorrow.

`0 of 10` material Inventory-to-Accounting handoffs are contract-compliant, and elements 10, 14
and 15 fail on **every one** of them.

**Why Phase SA records this prominently.** It is the clearest available counter-example to the
natural assumption that the accounting dependency is the programme's single blocker. It is not.
Resolving every accounting question would leave the inventory-to-accounting handoff contract
still uncompliant, because the missing pieces are identity, provenance and context guarantees
that Inventory itself must originate.
