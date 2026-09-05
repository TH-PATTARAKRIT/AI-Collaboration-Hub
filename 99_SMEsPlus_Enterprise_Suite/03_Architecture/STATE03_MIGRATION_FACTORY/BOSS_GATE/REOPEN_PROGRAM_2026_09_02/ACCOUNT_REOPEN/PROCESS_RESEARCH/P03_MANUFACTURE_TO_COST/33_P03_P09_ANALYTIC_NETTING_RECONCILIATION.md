# 33 — P03 / P09 ANALYTIC NETTING RECONCILIATION

**LAYER 2 — AUDIT QUARANTINE.**

P09 — Plan-to-Analyze owns the management-accounting architecture. **P03 does not redefine
it.** This file reconciles P03's cost view against P09's analytic view and states where
each owns the answer.

---

## 1. P09's position, read from its branch

`origin/research/account-p09-plan-to-analyze-2026-09-04-001`, files `AI02`–`AI05`, and
P09's own post-publication amendment accepting P04's correction:

- The analytic amount is the **negated signed balance × share**.
- An asset depreciation writes the distribution onto **both** rows of the entry.
- Analytic-line creation runs over all rows with **no account-type filter**.
- Therefore the two management records are **mirror images and net to zero**.
- Mandatory-plan validation has **two** gates that skip programmatic posts — one of which
  restricts it to product-type rows.
- The management dimension is **physical schema plus a JSON payload**, not scoped
  relational data; an analytic plan has **no company field at all**.

## 2. P03's independent verification

P03 verified the netting mechanism from source before adopting it — `25` §5:
`account_asset/models/account_move.py:297-299` sets `analytic_distribution` on
`move_line_1` **and** `move_line_2`. The lines are equal and opposite. **Confirmed.**

## 3. The four separations the directive requires

| Measure | Depreciation entry | Work-centre analytic (`M4`) |
|---|---|---|
| **Analytic record count** | **2** — one per journal line | **1** — one-sided |
| **Gross analytic movement** | `+x` and `−x`, gross `2x` | `−x`, gross `x` |
| **Net analytic movement** | **0** | **−x** |
| **Economic management cost** | **0 at balance level; `x` at line level** | `x` |

**The asymmetry is the finding.** Depreciation enters the analytic ledger balanced and
therefore invisible to any cost-centre total; the work-centre path enters one-sided and
therefore *is* visible. Two cost elements, two incompatible analytic conventions, in one
ledger.

## 4. Disposition

> **ANALYTIC NETTING — RECORD-ONLY NETTING VERIFIED.**
>
> Two analytic records are created and persist. Their **net balance is zero**. An analytic
> report that filters or groups by general-ledger account, or excludes balance-sheet
> accounts, shows the full charge; any report that **sums the cost centre** — which is what
> a cost centre is for — shows **zero**.

This is `EVENT-TYPE SPECIFIC`: it holds for entries whose two legs both carry the
distribution (depreciation, disposal gain/loss), and not for the one-sided manufacturing
analytic path. **Both qualifiers are required**; stating either alone misreports it.

**P03, P04 and P09 agree on this, independently, from three directions.** `16` §4 records
that a clean cross-check is itself a finding; this is the strongest one in the package.

## 5. Consequence for P03 specifically

The AAS+ veto rested partly on the premise that *depreciation already reaches production
cost centres through the analytic distribution*.

> **That premise is true at line level and false at balance level, so it cannot support the
> veto's reasoning as written.** It is not a mechanism that can carry depreciation into
> product cost, and `02` §5 already records the same conclusion from the P03 side.

**P03 does not amend the veto on this basis** — the veto is AAS+-owned and is re-evaluated
in `45`. P03 supplies the evidence and states its effect.

## 6. Boundary — what P03 does **not** claim

| Question | Owner |
|---|---|
| Whether the analytic ledger *should* be balanced or one-sided | **P09** |
| Whether a cost object should be first-class | **P09** — it records that none exists and 10 de facto ones share one record type |
| Whether analytic plans should be company-scoped | **P09** (`MA-11`), reinforced by P03 `36` |
| Whether depreciation *should* reach product cost | **Asset track** — `BLK-07`, open |
| Whether the manufacturing analytic path reconciles to the GL | **P03** — it does not; `DC-05` |

**`PEER DEPENDENCY OPEN — P09`** on the first three rows. This session did not wait.
