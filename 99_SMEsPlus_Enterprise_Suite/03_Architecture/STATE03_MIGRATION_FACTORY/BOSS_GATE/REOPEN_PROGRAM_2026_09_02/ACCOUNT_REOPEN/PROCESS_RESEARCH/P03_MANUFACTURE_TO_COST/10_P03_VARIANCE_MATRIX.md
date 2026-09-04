# 10 — P03 VARIANCE MATRIX

**LAYER 2 — AUDIT QUARANTINE.**

---

## 1. The question

Standard costing produces variances. Actual costing does not. A system that claims both
must say which variances it recognises, where they post, and when they close.

## 2. What the reference product recognises

**Enumeration.** POPULATION: the module set declared in `02` §3.
PATTERN: identifiers and account roles containing `variance`, plus the price-difference
account role. UNIT: one model, field or account role.

| Variance an ERP would normally recognise | Recognised here? | Where it actually goes |
|---|---|---|
| Material **price** variance | No | Absorbed into the valuation layer at purchase — P01's territory |
| Material **usage / quantity** variance | **No** | Actual consumption is simply what `_cal_price` capitalises |
| Labour **rate** variance | **No** | The rate in force at posting is the only rate — `DC-06` |
| Labour **efficiency** variance | **No** | Actual duration is capitalised; expected duration is display only |
| Machine / work-centre **rate** variance | **No** | As above |
| **Overhead spending** variance | **Not possible** | No overhead pool exists |
| **Overhead volume / capacity** variance | **Not possible** | No capacity denominator exists |
| Standard-cost **revaluation** difference | Partly | Falls out as a residue on the production account — `DC-04` |
| Subcontract **price** difference, standard-costed | **Yes — the only real one** | `mrp_subcontracting_account/models/stock_move.py:24-29`, routed to the price-difference account |

**Result: one of nine.** `FACT VERIFIED`.

## 3. Why this is structural, not a missing report

Variance requires two numbers: an expectation and an actual. The reference product holds
both — `duration_expected` and `duration` — but:

1. `_cal_price` capitalises the **actual** and never reads the expectation
   (`mrp_account/models/mrp_production.py:50`).
2. When there is no actual, the expectation **is written into** the actual
   (`DC-08`), destroying the difference rather than recording it.
3. `duration_percent` (`mrp/models/mrp_workorder.py:325-328`) computes the efficiency gap
   — **as a display percentage, never as an amount, never posted.**

> The information needed for an efficiency variance is computed and then discarded.

`FACT VERIFIED`. Recorded as `CTR-P03-02` — a system that measures a variance, shows it
to a user, and refuses to account for it.

## 4. The residue that behaves like an unnamed variance

For a standard-costed, real-time-valued product, `DC-04` leaves
`R + W − (standard × qty)` on the production account. That quantity **is** the total
manufacturing variance — material, labour and absorption combined, undecomposed and
unlabelled.

Consequences:
- It cannot be analysed, because nothing separates its causes.
- It has no closing entry, so it accumulates across periods.
- It is indistinguishable from the `DC-03` `extra_cost` residue sitting in the same
  account with the opposite sign.

**Two unrelated defects net against each other in one account.** A site with both may show
a small production-account balance and conclude that costing is working.

`FACT VERIFIED`, **conditioned by AAS-03 `C-02`**: the two residues meet in one account
only where the same company and product category carry **both** a standard-costed,
real-time-valued product (`DC-04`) **and** manually entered `extra_cost` (`DC-03`). That is
a mixed-costing configuration, not the default one.

Where it does occur it is the most dangerous property found in this session, because it
defeats the one control — a non-zero production-account balance — that would otherwise
catch either defect.

## 5. Cross-reference — not resolved here

`ASSET_DR_CONTINUATION/22` §5 carries `UNR-C-03`, *how a standard-costed product complies
with TAS 2*, at **Medium-High**. §4 above is the mechanism. **The question stays open on
that register**; P03 supplies evidence to it and closes nothing.

## 6. What SMEsPlus must decide — `BOSS CONTROLLED DECISION`

| ID | Decision | Why it cannot be researched |
|---|---|---|
| `BD-P03-01` | Does SMEsPlus recognise manufacturing variance as first-class accounting events, or capitalise actuals only? | Both are defensible under TAS 2. The choice determines whether `AE-13` exists at all |
| `BD-P03-02` | If variance is recognised, which of the nine in §2 are in scope for SMEs? | Scope, not fact — a cost/benefit judgement about SME operators |

Neither is decided here. Both are recorded in `14_P03_DEPENDENCY_REGISTER.md`.

**`BD-P03-01` is downstream of `ASSET_DR_CONTINUATION` `BLK-07`** — a capacity denominator
must exist before a volume variance can be defined — and must not be taken before it.
