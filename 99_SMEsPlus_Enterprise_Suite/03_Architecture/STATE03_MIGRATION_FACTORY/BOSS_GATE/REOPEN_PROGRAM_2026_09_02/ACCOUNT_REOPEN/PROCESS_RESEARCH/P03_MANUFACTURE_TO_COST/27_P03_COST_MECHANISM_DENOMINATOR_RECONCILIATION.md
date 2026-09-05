# 27 — P03 COST MECHANISM DENOMINATOR RECONCILIATION

**LAYER 2 — AUDIT QUARANTINE.** Highest methodological priority of this round.

---

## 1. The rule being applied

`smeplus-denominator-completeness-rule`: every count declares **POPULATION + PATTERN +
PATH SET + UNIT**, none author-chosen. `smeplus-count-unit-vs-population-lesson`:
declaring a population does not save a count whose **unit** is conflated. Counts here are
**executed**, not asserted.

## 2. A correction to P03's own record, before anything else

P03#02 file `25` §2 stated that P04 counts **nine**. **That is wrong, and it is P03's
error, not P04's.**

P04's *message* said nine. **P04's pushed branch says seven.** P04 had already corrected
itself under independent challenge, in
`06_P04_DEPRECIATION_COST_HANDOFF.md` §2.3, before P03 wrote `25`:

> *"Corrected after independent challenge. Executed strictly, the unit declared in §2.1
> yields SEVEN, not nine."*

P03 read the message and not the branch. `smeplus-peer-intake-discipline` states the rule
that was available and not applied: **a peer's message is a summary; a peer's pushed
branch is the source.** Recorded as research error `RE-P03-11` in `22` §6.

## 3. Four units, four counts — all executed

| Unit | Definition | Count | Source |
|---|---|---|---|
| **U1 — inventory-value writer** | one function that changes the carrying value of inventory | **2** | P03 `01` §3, unit declared retrospectively in `25` §2 |
| **U2 — monetisation path** | own rate field **or** own driver **or** own destination **ledger** | **7** | P04 `06` §2.3, corrected figure |
| **U3 — posting artefact** | own artefact that actually lands (a valuation write ≠ a standalone entry; two distributions of one value = two line sets) | **9** | P04 `06` §2.3 |
| **U4 — monetary computation** | one distinct arithmetic result | **6** | P04 `06` §2.3 |

**All four are internally correct. None supersedes another. Publishing one number without
its unit is the defect, not the number.**

### Reconciliation between U1 and the rest

U1 = 2 is **not** an under-count of U2 = 7. They measure different things:

| Path | In U2/U3? | In U1? | Why |
|---|---|---|---|
| M1 finished-move valuation | Yes | **Yes** | writes inventory carrying value |
| M2 labour relief entry | Yes | **Yes** | the paired GL relief; without it M1 creates value from nothing |
| M3 employee rate | Yes | No | an *input* to M1/M2, not a separate writer |
| M4 work-centre analytic | Yes | **No** | analytic ledger only — never touches inventory value |
| M5 project analytic | Yes (U3) | **No** | analytic ledger only |
| M6 employee analytic | Yes | **No** | analytic ledger only |
| M7 extra unit cost | Yes | No — folded into M1 | it is an addend inside M1's formula, not a separate writer |
| M8 WIP wizard | Yes | **No** | a self-reversing accrual; never changes inventory carrying value |
| M9 standard cost from BOM | Yes | **No** | sets a product-master price; a planning act, not a posting |

**Five of the nine never touch inventory value at all.** That is the substantive content
of the reconciliation, and it is the reason both counts are right.

## 4. P03's declared denominator for this round

| Element | Declaration |
|---|---|
| **POPULATION** | Every code path in the declared source root by which a manufacturing cost acquires a monetary value and reaches the general ledger, the analytic ledger, or a product-master price |
| **PATTERN** | Executed identifier sweep — `costs_hour`, `employee_costs_hour`, `hourly_cost`, `_cal_cost`, `_total_cost_per_hour`, `_cal_price`, `_post_labour`, `extra_cost`, `_compute_bom_price`, `_create_or_update_analytic_entry`, `_perform_analytic_distribution`, `account_production_wip*`, `property_stock_account_production_cost_id` |
| **PATH SET** | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/` — 797 modules, `tests/` excluded |
| **UNIT** | stated per count; four units are published in §3 and never mixed |

## 5. The count that actually governs the AAS+ veto

The veto's second limb asks: *does exactly **one** mechanism carry machine cost into
**product cost**?* That question is about **product cost**, so the governing unit is **U1**,
not U2/U3/U4.

Under U1 the live population is **2**, and they are a matched pair — capitalise, then
relieve — so the veto's limb is **not** failed by their existence. It is failed by the four
ways the pair fails to reconcile (`DC-03`, `DC-04`, `DC-07`, and `DC-01`'s inflated input).

**However** — and this is the correction to P03#02's acceptance of P04's framing — the
veto cannot be discharged by counting under U1 alone, because `M4`/`M5`/`M6` do carry
machine cost into **management** cost, and `M9` carries it into a **standard price** that
becomes inventory value for standard-costed products. A proof restricted to U1 would miss
both.

> **Governing statement.** The veto's second limb must be discharged against **U1 for
> financial product cost (2), U2 for the full monetisation surface (7), and U3 where the
> question is duplicate *records* rather than duplicate *cost* (9).** One number cannot
> discharge it. `38_P03_AAS_PLUS_ONE_MECHANISM_POPULATION_PROOF.md` executes all three.

## 6. Known unknown population

| Unknown | Effect |
|---|---|
| `iTEST02` unreadable | Its installed-module set could add or remove reachable mechanisms — `UNR-P03-07` |
| Custom addon sets not in the declared PATH SET | `smeplus-p05-expense-to-pay-status` records that P05's surface lived in custom addons, not the reference tree. **P03 has not swept the custom addon sets** — `UNR-P03-08`, and it is this round's largest self-identified gap |
| Any deployment not represented by the three readable dumps | Reachability conclusions in `26` §4 do not extend to it |

## 7. `UNR-P03-08` — CLOSED in this round

The custom addon sweep declared in §6 was **executed rather than left open**.

- **POPULATION:** the three project custom addon roots named in
  `smeplus-primary-source-evidence-locations`.
- **PATTERN:** `grep -rl --include="*.py" -E "_cal_cost|_cal_price|_post_labour|costs_hour|_total_cost_per_hour|extra_cost|_compute_bom_price"`, and second form `_inherit = "mrp.*"`.
- **UNIT:** one `.py` file containing ≥1 match.

| Root | `.py` files | Positive control `models.Model` | Cost-identifier hits | `mrp.*` inheritance |
|---|---|---|---|---|
| `smeplus-custom/addons` (68 modules) | 518 | **146** | **0** | **0** |
| `t8master/custom/addons` (57 modules) | 448 | **133** | **0** | **0** |
| `18.0.4_smeplus_v2/addons` (50 modules) | 359 | **99** | **0** | **0** |

**The positive control fires on all three roots**, so the zeros are real searches, not
silent failures — the control `smeplus-executed-not-quoted-rule` requires.

> **`P03T-F-02`. No project custom addon overrides, extends or inherits any manufacturing
> cost model.** The manufacturing cost surface is entirely reference-product code.
> `FACT VERIFIED`, scope declared.

This distinguishes P03 from P05, where the process surface lived in the custom addons.
Recording the difference matters: the P05 lesson does **not** generalise to P03, and this
is the evidence that settles it rather than an assumption either way.
