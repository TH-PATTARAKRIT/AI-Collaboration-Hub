# 68 — P08 RECONCILIATION REFRESH

**LAYER 2 — AUDIT QUARANTINE.**
**P08 LAST CONSUMED SHA: `4bdf8a2`.** **P03 defines no core-ledger architecture.**

---

## 1. The item P08 most needs from this round

> **`P03R-F-01`. The inventory valuation subsidiary ledger and the general ledger have
> diverged.** 25 valuation rows carry values up to ±1.5×10²¹ and name journal entries that
> **exist and carry entirely different, sane amounts** — 25 mismatched, 0 matched. The GL
> itself is balanced (447,384 lines summing to 0.00) and contains **no** outlier line.

This is a **subsidiary-ledger integrity** question and therefore P08's, not P03's.
P03 supplies the evidence and the row identifiers; it makes no determination about
core-ledger design.

## 2. Handoff register

| # | Item | Class | P08 decides |
|---|---|---|---|
| `H08P03-1` | Subsidiary ↔ general ledger divergence, 25 rows, examples with entry ids | **FACT VERIFIED** | whether the GL or the valuation ledger is authoritative, and how divergence is detected |
| `H08P03-2` | **`R-16`** — every entry generated from a business event needs an identity **written and read** as the duplication guard. `DC-15`: the marker is written on every time log and read only in tests | **FACT VERIFIED** (absence) | the accounting-event identity. **This is the same dependency P09 raises as `DEP-P09-01`** — two processes, one gap |
| `H08P03-3` | Three WIP account resolvers at two levels for one concept (`08` §2); `mrp_accountant` absent in the manufacturing database | FACT VERIFIED | the WIP representation |
| `H08P03-4` | **`DC-09`** — the relief entry takes the posting date, not the event date. Now **live** wherever `DC-07` fires | FACT VERIFIED | period attribution; the same root cause P10 reports |
| `H08P03-5` | P04's locked-period silent re-dating sits in the accounting core and would hit `_post_labour`. **P04's finding, P08's ownership** — P03 confirms applicability only | cited | — |
| `H08P03-6` | **`TZ-09`** — the 30 corrupt rows **nearly cancel**. Any partial correction breaks the cancellation and releases ~10²¹ into the ledger. **Remediation sequencing is a Boss decision** | FACT VERIFIED | — |

## 3. Duplicate vs zero financial effect

| Question | P03's measured answer |
|---|---|
| Duplicate financial effect from manufacturing? | **None observed.** `M1`/`M2` are a matched capitalise-and-relieve pair; `38` Test 3 passed for financial cost |
| Zero financial effect? | **Yes, extensively** — conversion cost entirely; 49 unvalued finished moves; 1,386 unvalued consumptions |
| Wrong financial effect? | **Yes — two kinds.** Misdirected (`DC-07`, product COGS credited, 60 of 60 work centres) and **absurd** (`55`) |

**The third row is the one P08 should weigh.** A ledger that is balanced, duplicate-free and
non-zero can still be wrong, and both of P03's wrong-value findings pass every balance
check.

## 4. Period close

`13` stands. Added this round: the production account's two residues cannot be assessed in
`iSMEs` (nothing posts) and are unmeasured in `iTEST02`. **`UNR-P03-17`** — a production-
account balance decomposition in `iTEST02` is the natural next measurement and was not run.
Recorded rather than claimed.
