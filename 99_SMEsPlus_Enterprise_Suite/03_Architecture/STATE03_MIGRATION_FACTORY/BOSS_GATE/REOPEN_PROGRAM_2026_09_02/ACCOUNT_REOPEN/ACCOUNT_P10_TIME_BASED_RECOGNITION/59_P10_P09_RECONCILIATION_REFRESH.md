# P10 ↔ P09 — RECONCILIATION REFRESH

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D19` (part 2).

---

## 1. Delta Check

| Peer | Last consumed | Current head | Delta |
|------|---------------|--------------|-------|
| `P09` Plan-to-Analyze | `9a3bded` | **`70f8d20`** | **2 commits** — an entire analytic-economic-integrity sub-package, 13+ new documents. **Consumed** |

The analytic process has published a **symmetric-allocation event sweep** that overlaps `P10-F-38` directly. This is the most consequential peer delta of the round.

## 2. The Overlap — and why both findings stand

The peer's sweep asks: *does any event type other than depreciation allocate both legs of a balanced pair?* Its row for deferred recognition reads, after its own adversarial challenge:

> Deferred recognition **is not the asset module's builder** — it lives in the reporting module and builds its two legs from **different denominators**: a per-key ratio for the profit-and-loss legs, an aggregate ratio for the balance-sheet leg. **Not a clean zero — a residue case.** Not zero with more than one grouping key; and the move is immediately reversed, producing a **second, cross-move pair the sweep's unit cannot see.**

**That is the grouped path.** P10's finding, after its own narrowing, is about the **validation path**, which lives in a different module and writes **the same** distribution to both legs.

| Path | Builder | Legs | Net | Found by |
|------|---------|------|-----|----------|
| **Grouped / manual** | reporting module | two **different** ratios | **residue, not zero** | `P09` |
| **Validation** | accountant module | the **same** distribution, opposite signs | **exact zero** | `P10` |

> **Both are true, of different paths, and neither package covers the other's.** The peer's sweep states it examined the reporting module's builder; it does not address the validation builder. P10's finding does not address the residue behaviour.
>
> **Returned to `P09`: its row 5 covers one of the deferral mechanism's two generation paths.** The other path produces a clean zero and is the one **every deployed company is configured for**.

## 3. The Peer's Denominator Warning — adopted against P10's own finding

The peer's sweep declares its own denominator inadequate, after challenge:

| Pattern form | Sites |
|---|---|
| Declared pattern — key followed by a colon in a values dictionary | **45**, 11 modules |
| Record-attribute assignment | 19 |
| Subscript assignment | 18 |
| **Union** | **82 sites, 23 modules** |

**+82 % sites, +109 % modules** — and **the single write site the peer's headline finding rests on is a subscript assignment, not a member of the declared 45.** The peer found it by reading the function, not by the sweep.

**P10 adopts this against itself.** `P10-F-38` was also found by **reading the function**, and P10 has **not** swept for other attribution write sites in its own mechanisms.

> **`P10-F-38`'s scope is therefore: two paths of one mechanism, found by reading, not by an executed sweep.** Whether other recognition mechanisms write attributions in the same shape is **class `C` — NOT SEARCHED**. P10 does not claim otherwise, and the earlier phrasing *"two independent mechanism-level implementations"* is a floor, not a population.

## 4. Positions Consumed From the Delta

| # | Peer item | P10 class | Effect |
|---|-----------|-----------|--------|
| `A9-1` | Three mechanism families reproduce the exact zeroing; two more fail differently by leaving a residue | class `B` — peer-supplied, not re-derived by P10 | Widens the defect family well beyond P10's scope |
| `A9-2` | The cash-basis pair is **worse** than depreciation because no surface can see past it | class `B` | Outside P10's scope; recorded |
| `A9-3` | The defect is *"predominantly core accounting, not the asset module"* | class `B` | **Supports** P10's correction that the attribution shape is a mechanism property, not an asset property |
| `A9-4` | The declared denominator is a lower bound; 12 further modules unreasoned | class `B`, **adopted as a constraint on P10's own claim** | See §3 |

## 5. Does Any P10 Recognition Path Inherit the Peer's Risks?

| Peer risk | Does P10 inherit it? |
|-----------|----------------------|
| Analytic zeroing | **Yes** — the validation path, exactly. `P10-F-38` |
| Double counting | **Unknown** — P10 has not enumerated its recognition entries against the peer's double-counting classes. `class C` |
| Line eligibility | **Yes, and the cause was corrected** — P10 first adopted the peer's product-row explanation; the real gate is a context key set only by user-interface buttons. Recognition entries are programmatic and never carry it |
| Thai chart account-type issue | **Not assessed** — `class C`. Routed to the tax process |
| Management attribution scope | **Yes** — the structure carrying attribution has no company field; P10 adopts the peer's position that a company-scoped requirement may not be enforced through it |

## 6. What P10 Returns

1. **The validation path is not covered by the peer's sweep**, and it is the configured path in every deployed company.
2. **The deferral mechanism has generated zero entries in all four deployed databases** — so on today's data neither path has produced an analytic record at all. The defect is capability, not exposure.
3. P10 adopts the peer's denominator warning and re-scopes its own finding accordingly.
