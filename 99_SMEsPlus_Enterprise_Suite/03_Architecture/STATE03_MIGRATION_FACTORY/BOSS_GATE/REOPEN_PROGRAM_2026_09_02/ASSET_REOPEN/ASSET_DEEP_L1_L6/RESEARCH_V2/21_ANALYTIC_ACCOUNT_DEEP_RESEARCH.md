# 21 — ANALYTIC ACCOUNT DEEP RESEARCH
**LAYER 2 — AUDIT QUARANTINE**

Answers §27 and §50. Analytic is mandatory in this research because it is the only
management dimension the reference asset domain actually carries.

## 1. Where analytic lives on an asset

The asset inherits an **analytic mixin**, giving it a single `analytic_distribution`
field: a mapping of analytic account (or combination of accounts) to percentage.

It is **computed and stored, and user-overridable**. `FACT VERIFIED`

## 2. How it is derived — balance-weighted inheritance

At creation from a vendor bill, the asset's distribution is computed from its source
lines:

```
for each source line with a distribution:
    for each account in that distribution:
        weight[account] += percentage × line balance

distribution[account] = weight[account] ÷ total balance of all source lines
```

So a two-line source where 70% of the money carried Cost Centre A and 30% carried
Cost Centre B yields a 70/30 asset distribution. If the total balance is zero the
computation is skipped. If no source line carries a distribution, the asset's
existing value is preserved rather than being cleared.

`FACT VERIFIED`

Note the ordering established in `14` §4: **the bill beats the asset model.** Where
both offer a distribution, the source line's wins.

## 3. How it reaches the journal

Each depreciation entry is prepared from the asset. The distribution is read **at
preparation time** and written onto **both** lines — the expense line and the
accumulated-depreciation line.

One deliberate subtlety: the key is set **only if a distribution exists**. When the
asset has none, the key is omitted entirely rather than written as empty, so that
the accounting layer's own distribution computation can still populate it.

`FACT VERIFIED`

**Consequence for reporting:** analytic appears on the balance-sheet side as well as
the expense side. Any analytic report that does not filter by account type will
double-count depreciation.

## 4. The lineage, end to end

```
vendor bill line distribution
   → (balance-weighted) → asset distribution
      → (copied at preparation) → depreciation entry, both lines
         → analytic lines
            → analytic reporting
```

Every arrow is a **copy at a moment in time**, not a live reference.

## 5. What happens when the analytic changes mid-life — §27's core question

| Question | Answer |
|---|---|
| Does future depreciation change? | **Yes** — subsequent entries carry the new distribution |
| Does historical depreciation change? | **No** — posted entries are untouched |
| Can posted analytic be modified? | Only by editing the posted entry directly, subject to lock dates; the asset provides no mechanism |
| What audit trail exists? | **None on the asset.** The distribution field is not tracked, so a change leaves no chatter entry |

The correction Expert 2 insisted on at Level 3 applies here: the distribution is
**not frozen**. It is *copied at preparation time*. The change is allowed and applied
asymmetrically, and **nothing anywhere reports that an asset's current distribution
differs from the distribution on its own posted history.**

`FACT VERIFIED` · exposure uncounted on the UAT — `UNR-11`

## 6. Multi-dimensional analytic

Supported by the underlying mixin: a distribution key can name a **combination** of
accounts across analytic plans (for example department + project + cost centre
simultaneously), with one percentage.

So the dimension the Boss wants for department / project / cost-centre attribution
of depreciation **exists and is already carried onto every depreciation entry**.

`FACT VERIFIED`

## 7. Validation — what is not checked

| Check | Present on the asset? |
|---|---|
| Distribution sums to 100% | **No** |
| Analytic account not archived | **No** |
| Analytic account company matches | **No** |
| Analytic plan applicability | **No** |
| Any warning on change | **No** |

`FAIL-A02` … `FAIL-A06`. Whatever validation exists is in the accounting layer, not
in the asset domain.

## 8. Analytic on the production side — for comparison

The work centre also carries a distribution, and work orders write analytic lines
from it with a manufacturing-order category, updating them whenever the recorded
duration changes.

**So both halves of the Boss's costing design already write analytic lines** — the
asset half from depreciation, the production half from work-order duration. They
are written to the same analytic ledger, from different sources, with no
relationship between them.

That is a genuine opportunity: **analytic is the one dimension where the two truths
already meet in the same table.** It is also a trap — meeting in a table is not
reconciliation, and nothing prevents the same cost being represented twice.

`FACT VERIFIED`

## 9. Roles analytic plays — §50 answered

| Role | Does analytic serve it here? |
|---|---|
| Financial dimension | Yes — it is on real journal items |
| Management dimension | Yes |
| **Cost allocation mechanism** | **No.** Analytic *records* attribution; it does not compute or allocate anything |
| Reporting mechanism | Yes |
| Reconciliation mechanism | No |

The third row matters. A recurring temptation in this programme is to treat analytic
as the allocation engine. It is not. It is a **tag**. Deciding *how much* cost goes
*where* is upstream of it, and that upstream logic is exactly what does not exist
(`08` §6 links 7 and 8).

## 10. For SMEsPlus

1. Analytic distribution on the asset is **inherited from the invoice**, so the
   quality of asset analytic is determined by the quality of accounts-payable
   coding. That is an operational control, not a system feature.
2. Analytic appears on **both sides** of the depreciation entry. Any consumer must
   filter.
3. There is **no divergence report**. If SMEsPlus keeps the copy-at-posting model —
   and it should, for auditability — it must add one.
4. Analytic is the meeting point of the two truths, and it is the cheapest place to
   start proving the costing concept before any structural change is made.
