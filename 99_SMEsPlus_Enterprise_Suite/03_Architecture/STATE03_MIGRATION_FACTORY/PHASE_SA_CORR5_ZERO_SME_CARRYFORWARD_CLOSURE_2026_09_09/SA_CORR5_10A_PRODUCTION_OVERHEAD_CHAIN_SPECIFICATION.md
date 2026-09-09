# SA_CORR5_10A — PRODUCTION-OVERHEAD CHAIN — SMEs CORE SPECIFICATION CLOSURE

## Supplement to CP-SA-C5-100 (scenarios 16 and 17)

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR5-ZERO-SME-CARRYFORWARD-001]`
Branch: `architecture/phase-sa-corr5-zero-sme-carryforward-closure-2026-09-09-001`
Raised by internal self-challenge `CHC-07` (`SA_CORR5_11`): `SA_CORR3_03` §11 names three gaps
*"closable by SMEs Core design work requiring no Boss decision and no statutory resolution"* —
`POH-G-01`, `POH-G-02`, `POH-G-04` (variance) — and neither CORR4 nor the first freeze of CORR5 executed
them. **This file executes them at Phase SA specification level, and additionally specifies the
`POH-G-03` mutual-exclusion rule (build remains runtime) — four items, not three (`CHD-07`).** Authority: the closure act's
*conceptual/domain design* and *interface/boundary definition*; business-semantic only.
Boss: **SOLE FINAL APPROVER**

---

## 1. What is consumed, not re-originated (`AUTO-C5-02`)

`SA_CORR3_03` in full — the seven-link chain (§4), the three-axis element classification and 21-row
matrix (`L2`, design candidate), the normal-capacity machine-hour driver for fixed overhead (`L3`,
*"comes from statute, not from analysis preference"*), the specified absorption arithmetic for the
depreciation pool with its closure identity (`L4`), the identified events (`L6`), the three-closes
order and per-machine zero-reconciliation gate (`L7`, design candidate), `POH-F-09`…`-14`, the Boss
residue `POH-D-01`…`-06` (§9, **untouched here**), `BD-02` (under-absorption destination **CLOSED**),
`BLK-08`'s substance (planned-maintenance capacity subtracted from the denominator, never charged
twice); `SA_CORR3_04` (maintenance classification, 9 of 12 routes); `BD-ACC-01`, `BD-ACC-03A`/`03B`;
`XMC-C-A1`…`A14`; `MTI-38`; the adopted inventory design's WIP boundary (*consumption decreases stock
"into work in progress"; output increases stock "from work in progress"*).

---

## 2. `POH-G-01` — the pool object, the capacity-denominator object, and the capture mechanism

| Object | Specification (semantic) | Lineage |
|---|---|---|
| **Fixed-overhead pool** (`OH-POOL`) | A **company-scoped** cost object (`CTX` mandatory, `MTI-04`) that accumulates, per costing period, the period amounts of the fixed-and-absorbable elements the `L2` matrix classifies (six classes: depreciation, planned maintenance, standing utilities, indirect labour, factory supervision, facility cost). One pool **per absorption driver scope** — by default per work centre / machine group, because the driver is a machine hour (`L3`). Each element's amount enters the pool as an **evented fact** carrying its source (§2.1), its classification row, the costing period and the `CTX` | `L2`, `L3`, `L4`(i) |
| **Capacity denominator** (`OH-CAP`) | A **dated, attributed register entry** per driver scope and costing period: normal capacity in driver units (machine hours) **net of planned maintenance** (`BLK-08` substance), with effective-from, author, review date, and the estimate basis. **Versioned; a change never re-computes a closed period** (`MTI-36` pattern). Owner of the figure and review cadence = `POH-D-05` (Boss residue, unchanged) | `L3`, `L4`(ii), `POH-D-05` |
| **Absorption rate** | Derived, never stored as truth: `pool amount ÷ normal capacity` per period per scope; the arithmetic of `L4` generalised from the depreciation numerator to the pool total. **The closure identity holds per element and per pool:** `productive absorbed + non-productive (idle / no-demand / unabsorbed) = period pool amount`, exact, every period | `L4` |

### 2.1 Capture mechanism per element — what puts an amount into the pool

| Element (from `L2`) | Source fact | Capture rule |
|---|---|---|
| Depreciation | asset sub-ledger period charge (already characterised) | period charge is the pool entry; the asset's **production / non-production classification** gates entry (`SA_CORR3_04` classification; an asset without it **cannot** enter — fail closed) |
| Planned maintenance | maintenance order cost (parts issue + labour) on a production asset | enters the pool **only** through the planned-maintenance route; the same cost never also generates a period charge (`BLK-08`) — the exclusion is §4 |
| Standing utilities, indirect labour, factory supervision, facility cost | **a period accrual or a posted vendor bill / payroll fact tagged to the pool scope** | the tag is a required attribute of the source fact; an untagged fact **cannot** be absorbed and is expensed under `BD-02`'s destination as *unabsorbable by omission* — and that omission is reported (§5). **No inference from account code or name** (the `MTI-20`/`MTI-42` rule) |

**Reference behaviour deliberately not inherited** (`SA12-F-01` clause): the reference's practice of
loading overhead as a per-unit surcharge on the product cost with no pool, no denominator and no
variance — *"work-centre averaging eliminated structurally"* (`L3`).

---

## 3. `POH-G-02` — the receiver

**WIP value composition (semantic):** the value of work in progress for a production order is the sum
of three components, each an evented accounting fact under `BD-ACC-01` with its own recognition role:
**(i)** material consumed at the category costing method (`BD-ACC-03B`); **(ii)** direct labour /
machine time at the rate in force when logged (`L7`); **(iii)** **absorbed fixed overhead** = driver
units consumed × the period absorption rate of the pool scope. Finished-goods receipt carries the sum
into stock; the production order is the **cost object** that receives (iii). **`L5` therefore has a
receiver: the production order's WIP value, component (iii).** The Inventory Final Solution's WIP
counterpart gains the absorbed component as a *value-composition* obligation, not a schema.

---

## 4. `POH-G-03` — the mutual-exclusion rule (specification; the build is runtime)

**Exactly-one-mechanism rule:** every fixed-overhead amount is absorbed through **exactly one** pool in
**exactly one** period. Enforced as three testable clauses: (a) a source fact tagged to a pool cannot
also be posted directly to a production cost object; (b) planned-maintenance cost that reduced the
denominator cannot also enter the pool as a period charge; (c) an amount absorbed in period *p* is
frozen after the costing close and a correction is a dated event in *p+1* (`L7` freeze-after-close).
**Detection report:** per pool per period, the closure identity of §2 published with population /
assessed / not-assessable counts; a non-zero residual is a `BREACH`, never silently re-absorbed
(`MTI-19`'s *raises, does not repair* pattern). **Discharging veto limb 2 is the issuer's and Boss's
act (`POH-D-06`); this file specifies the mechanism the discharge would test.**

---

## 5. `POH-G-04` — the absorbed-vs-actual variance as a fact with an owner, a mechanism and a destination

| Attribute | Specification |
|---|---|
| **The fact** | `OVERHEAD ABSORPTION VARIANCE` per pool scope per costing period = period pool amount − absorbed amount; sign carries under- (positive) / over- (negative) |
| **Owner** | **Manufacturing (costing)** owns the fact; **Accounting Core** owns the event identity (`BD-ACC-01`); identity basis = (tenant, company, Manufacturing, occurrence = (pool scope, costing period), role = *absorption variance*, policy version) — deterministic, replay-safe (`XMC-C-A3`) |
| **Under-absorption destination** | **`BD-02` — CLOSED by Boss**: period expense; **not** capitalised into inventory (TAS 2 ¶13 direction, statutory confirmation `HOLD / EVIDENCE REQUIRED` as to presentation) |
| **Over-absorption** | the corpus's one candidate — cap absorption at the period's pool amount — is **adopted as the default rule for every pool, single- or multi-element** (SMEs Core position): absorption may not exceed the period pool amount; when the cap binds, the shortfall is **reported**. **The cap's *strength* is a declared statutory dependency (`SA_CORR3_03` §10 item 4) — `HOLD / EVIDENCE REQUIRED`**; and the multi-element worked case `SA_CORR3_03` §13.1 says is owed **is not written here** — `RT-POH-04` states the test, not the analysis (`CHD-07`). An over-absorption **credit** therefore cannot arise under the cap; **if Boss later elects uncapped absorption, the credit's destination is a new Boss item** — recorded, not created |
| **Idle / no-demand split** | carried as two reason classes on the non-productive component (`POH-D-04` keeps both unless Boss merges them) |
| **Timing** | costing close, after operational close, before accounting close (`L7` order); the variance event carries the costing period's date and is refused if that period is locked (`XMC-C-A15`) |
| **Statutory presentation** | `HOLD / EVIDENCE REQUIRED` — Thai Accounting-Tax track; the fact and its destination do not depend on it (`SA_CORR3_03` §10) |

---

## 6. What remains, exactly

| Item | Class | Owner |
|---|---|---|
| `POH-D-01`…`POH-D-06` | **Boss residue — unchanged, not re-asked** | Boss |
| Build of pool, denominator register, capture tags, exclusion checks, variance close | **runtime** — `RT-POH-01` pool closure identity holds to the unit; `-02` untagged fact expensed and reported; `-03` planned maintenance never double-charged (synthetic injection `0 → 1`); `-04` multi-element cap binds and reports; `-05` variance event idempotent under replay | Pre-Test / Build |
| Statutory presentation of over/under-absorption | `HOLD / EVIDENCE REQUIRED` | Thai Accounting-Tax track |
| `L2` classification adoption, `L7` close model adoption | **document-owner adoption acts** on design candidates already written (the Account programme's cost registers) — non-material once this file cites them as the governing candidates | Account programme |

**Scenarios 16 and 17:** the SMEs Core design gaps `POH-G-01`, `-02`, `-04` are closed at specification
level; the remaining `B` on both rows is exactly `POH-D-01`/`-02`/`-06` (Boss residue, `B-6`), and
`SA_CORR5_10` rows 16–17 are corrected to say so.

## 7. Residual

Everything in §2–§5 is originated here from `SA_CORR3_03`'s candidates and reviewed only by the
diff-scoped self-challenge. The load-bearing choices to attack: one pool per driver scope (§2) — which
**generalises `L3`/`L7`'s per-machine register and gate to a work-centre / machine-group scope without
the source saying so** (`CHD-17`); the tag-not-infer capture rule (§2.1); adopting the cap as the
universal over-absorption rule (§5). `OH-CAP`'s attribute list (§2) inherits `L3`/`POH-D-05`'s candidate
wording and is the closest thing here to a record specification; it is stated as the semantic minimum,
not a schema.

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
