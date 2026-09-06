# P04 — ACTIVE-PERIOD DEPRECIATION ATTRIBUTION

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P04-05`. Source basis series 18.

---

## 1. What the estate actually does with a period's depreciation

| Step | Mechanism | Evidence |
|---|---|---|
| Board generation | `compute_depreciation_board`, per `method` / `method_number` / `method_period` / prorata type | `CQ-P04-02` |
| Posting | one journal entry per period: **debit** `account_depreciation_expense_id`, **credit** `account_depreciation_id` | reference |
| Analytic tag | written to **both** lines when set on a draft move → **nets to zero** | `P04-F-153` |
| Productive vs non-productive split | **does not exist** | §2 |
| Interface to Operation / MO / WIP / FG | **does not exist** | `CQ-P04-07`, P03 `CQ-P03-06` |

## 2. The attribution the policy requires, against what exists

| Boss policy input | Estate status |
|---|---|
| Productive depreciation → WIP/FG | **No path.** P03: no equipment cost enters an MO, WIP or FG in **0 of 4** deployments |
| Non-productive → a named operational cause | **No anchor.** Causes live on work centres; depreciation lives on assets; no join (`CQ-P04-08`) |
| **No unclassified depreciation** | **Unachievable today** — 100 % of depreciation is unclassified in the estate's own terms, because there is no classification at all |
| Analytic must not be omitted | Available but **nets to zero** as wired (`P04-F-153`) |

> **P04 states only that the reference product provides no mechanism.** Whether SMEsPlus
> builds one, and on which denominator, is **`BLK-07` / `P04-BD-05` — Boss-owned and not
> closed by this run.**

## 3. The 100 % reconciliation invariant

Stated as a contract for the design, since nothing implements it:

> For every asset and every period:
> **period depreciation = Σ productive allocations + Σ non-productive attributions**, exactly,
> with a named cause on every non-productive component and **no residue**.

**Two preconditions the estate does not meet**, both established in this closure:
1. an **Equipment Usage Event** must exist (`CQ-P04-07` §3) — it does not;
2. the **cardinality** of asset↔equipment must be resolved (`P04-F-149` — many-to-one,
   unconstrained), or an equipment's usage cannot be attributed to one asset's depreciation.

## 4. Denominator — the Boss decision, restated precisely

`BLK-07`: *period depreciation ÷ normal capacity hours* or *÷ actual productive hours*, with a
third option registered at `P04-BD-05` (units-of-production as the TAS 16 **method**, with
normal capacity as the TAS 2 **absorption denominator**).

> **`BOSS DECISION REQUIRED — DECISION PACKAGE READY`.** No evidence in this run displaces the
> standing recommendation or the third option. **The carried policy names three permissible
> drivers with no mandatory default**, which is consistent with leaving `BLK-07` open.

## 5. Double-count prevention

| Risk | Control today |
|---|---|
| Depreciation absorbed twice (productive and non-productive) | none needed yet — no absorption exists |
| Equipment expensed on receipt **and** capitalised | **none** — `P04-F-151`, unmeasured, `P04-B-53` |
| Two assets claiming one equipment | **none** — `P04-F-149` |

## 6. Disposition

> **`CQ-P04-05` — `BOSS DECISION REQUIRED — DECISION PACKAGE READY`.**
> The factual half is `FACT VERIFIED`: **no productive/non-productive attribution mechanism
> exists**, with denominators declared and corroborated from both sides (P03 manufacturing,
> P04 asset). The design half is Boss-owned at `BLK-07` / `P04-BD-05`, unchanged.
