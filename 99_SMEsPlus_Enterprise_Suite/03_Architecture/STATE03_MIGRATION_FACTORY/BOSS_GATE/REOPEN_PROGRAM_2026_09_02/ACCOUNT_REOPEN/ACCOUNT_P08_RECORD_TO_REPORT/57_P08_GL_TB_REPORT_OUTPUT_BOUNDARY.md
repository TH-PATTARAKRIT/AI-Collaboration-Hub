# P08_GL_TB_REPORT_OUTPUT_BOUNDARY

Prompt `[SMEPLUS-26-09-06-P08-R2R-DOMAIN-PURE-BOUNDED-CLOSURE-002]` · **PHASE S** · answers `CQ-P08-08`

Where P08's responsibility for a reported figure ends. Consolidates `11`, `41` §7, `45` hops 5–9.

---

## 1. Nothing between the item and the statement is stored

| Object | Stored? | Class |
|---|---|---|
| Journal item | **yes — the sole store of the monetary fact** | `FACT VERIFIED` |
| General ledger | **no** — a query shape over items | `A VERIFIED ABSENCE`, 22 roots, 7-observation limit |
| Subledger (party) | **no** — the same rows filtered by account | `FACT VERIFIED` |
| Trial balance | **no** — computed on demand | `FACT VERIFIED` |
| Financial statements | **no** — line formulas over accounts | `FACT VERIFIED` |
| Period balances | **no** — there is no period object to hold them | `A VERIFIED ABSENCE` |
| **Report-layer side stores** | **YES — three of them, holding figures not derived from journal items at all** | `FACT VERIFIED` |

> **Consequence P08 must publish with every output: a GL, TB or statement figure is a derivation performed at read time over a mutable item set. There is no stored intermediate and no as-of reconstruction. A report re-run later is not the report that was run before.**

## 2. What the derivation reads — and what it cannot see

**Reads:** account, date, debit, credit, currency amount, currency, company, partner, journal, entry, display type, posting state.

**Does not read:** essentially any provenance field. A scoped search of core reporting for five origin pointers returns **zero hits** — `B NOT FOUND IN SEARCHED SCOPE`, bounded to **18.0 core reporting**, and **the deployed estate adds a custom reporting module this bound does not cover** (`UNRESOLVED`).

**Cannot see, because the item does not carry it:**

| Missing at item level | Measured |
|---|---|
| The entry's own number | **41.89% of posted items** cannot name their entry |
| Origin | **17.00%** carry no provenance mark of any kind |
| Authorship / mode | **no field exists** |
| **Tax period** | **0 of 61,157** entries carrying one propagate it to their whole item set |

**The statements aggregate the object that carries the least meaning. That is the single sharpest statement in this package, and the tax-period measurement is its most consequential instance, because that dimension is statutory.**

## 3. Integrity of the reported figure

| Property | Standing |
|---|---|
| The trial balance balances | **yes — and it is close to a tautology**: the only enforced invariant is the one the TB is expressed in |
| The TB balances in transaction currency | **not enforced at any layer**; measured residual **4 posted entries**, all from a 1:1 rate fallback |
| Two identical-looking items are the same thing | **no** — 6,494 groups covering 23,419 items are indistinguishable on every stored attribute |
| A prior-period figure can be reproduced as of that date | **no** — no bitemporal record |
| A statement figure can be traced to its source document | **for 3.9% of posted entries, not at all** |
| A statutory register renders completely | **admission is by literal match on a stored name**, and one query carries **no company predicate** |

## 4. Where P08's responsibility ends

| P08 owns | P08 does **not** own |
|---|---|
| That the ledger holds the figures a report aggregates | Whether a statement layout satisfies a standard or a statute |
| That the derivation is at read time with no stored intermediate | Which taxes belong in which statutory register — **P07** |
| That provenance is unavailable at the level reports read | Whether a given cost was correctly attributed — **P03, P09** |
| That company scope is or is not applied in a selection | Whether a filed figure was correct — **P07**, `HOLD — STATUTORY EVIDENCE REQUIRED` |
| That no as-of reconstruction exists | The reconciliation architecture built on that fact — **P11** |

**Disposition: `FACT VERIFIED — CLOSED FOR CURRENT P08 EVIDENCE`, with one named `UNRESOLVED` (the deployed reporting module) and the remainder routed.**
