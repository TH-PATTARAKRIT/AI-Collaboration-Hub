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
