# 12 — P02 CONTRADICTION REGISTER

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`

Per the execution constitution: **prior conclusions are not deleted.** Where this session's own earlier
reading was wrong, the original statement is preserved alongside the correction.

## 1. Material Contradictions

### C-01 — "Delivery relieves inventory to an interim account" is not true by default for a Thai company

| Field | Content |
|---|---|
| **Original reading** | Carried into this session from the generic chart's behaviour: delivery debits an interim asset, and the invoice moves it to expense. |
| **Contradicted by** | The Thai chart template sets **no** split-recognition boolean — and chart installation **defaults it to off** — and defines **no** stock input, output or valuation account among its **27** accounts. `EV-P02-042`, `EV-P02-043`, `EV-P02-044` |
| **Correct statement** | For a Thai company as shipped: real-time valuation cannot be enabled without the implementer first creating three accounts **per company**; with valuation left at its manual default, **the O2C process produces no automatic cost-of-sales entry at any point.** |
| **Materiality** | Maximum. Any P02 accounting design assuming perpetual valuation is assuming a configuration the Thai localisation does not deliver. |
| **Disposition** | Recorded in `01_P02_PROCESS_MAP.md` S5 and `07_P02_EVENT_TO_GL_MATRIX.md` §2.3. Routed to Core Accounting Reconciliation as **P02-X-01**. |

### C-02 — The rounding line on an invoice is not the tax-rounding residue

| Field | Content |
|---|---|
| **Original reading** | The rounding-type line carries the tax-rounding difference. |
| **Contradicted by** | It is the **cash-rounding** line, produced only when a cash-rounding rule is configured. `EV-P02-064` |
| **Correct statement** | **Two** rounding residues exist. The global-rounding tax delta is absorbed **inside the tax amounts themselves** — pushed onto the largest contributing bucket, then distributed one currency unit at a time — with no dedicated line and no separate account (`EV-P02-063`). The cash-rounding residue gets its own line and, under its default strategy, **carries tax tags and therefore reaches the VAT return** (`EV-P02-065`). |
| **Materiality** | High for tax reconciliation: a reviewer looking for the tax-rounding difference as a line will not find it, and the line they do find is a different thing that affects the return. |
| **Disposition** | Recorded in `04_P02_REVENUE_AR_TRACE.md` §3.3. |

### C-03 — The down-payment state helper does not report receipt

| Field | Content |
|---|---|
| **Original reading** | It reports whether a deposit has been received. |
| **Contradicted by** | It returns only draft, cancel or empty, and reads the parent document's status only. T2 §4 |
| **Correct statement** | A posted-and-unpaid and a posted-and-paid down payment are **indistinguishable** through it. Its only use is deciding what prints on the order. |
| **Materiality** | Moderate. It removes a control a designer might assume exists. |
| **Disposition** | Recorded in `09_P02_PAYMENT_RECONCILIATION_MATRIX.md` §5. |

### C-04 — Cost-of-sales generation has no idempotency guard: exploitability unresolved

| Field | Content |
|---|---|
| **The verified half** | **`FACT VERIFIED`** — the generator iterates product lines and creates a new pair of cost lines each time it runs; the set it iterates **excludes cost lines**, so existing pairs are invisible to it; and the origin field it writes is **never read for duplicate prevention** (complete denominator: 4 occurrences root-wide). `EV-P02-016`, `EV-P02-028`, `EV-P02-050` |
| **The unresolved half** | Whether a document can traverse the posting routine, have cost lines created, and then **not** post — leaving them on a draft document that a later post duplicates. The mechanism exists (`EV-P02-015`, `EV-P02-031`); whether any caller reaches it with a future-dated sale document is **not established**. |
| **Evidence required to close** | A runtime reproduction on a database: post a future-dated customer invoice for a storable, real-time-valued product through a soft-post caller, then post it again and count the cost lines. **This session had no database access and could not execute it.** |
| **Status** | `UNRESOLVED — EVIDENCE REQUIRED` |
| **Why it does not gate the design position** | The **absence of the guard** is itself the finding. `DC-03-02` requires idempotency by construction regardless of whether the reference is exploitable today. |

### C-05 — Two incompatible definitions of "this movement is a return"

| Field | Content |
|---|---|
| **Contradiction** | Valuation asks whether the movement carries an originating-move link. Accounting asks whether the source location is the customer location. T1 C1 |
| **Consequence** | A manually created inbound picking from the customer location with no originating-move link is **booked with the return account pair and the storno flag while being valued at current standard price**. The journal entry says *return*; the valuation layer says *receipt*. |
| **Materiality** | High — it is a direct violation of one-fact-one-definition. |
| **Disposition** | `08_P02_RETURN_CREDIT_REFUND_MATRIX.md` §5; `DC-08-03`. |

### C-06 — Linking a credit note to its order line makes its cost **less** accurate

| Field | Content |
|---|---|
| **Contradiction** | The intuitive expectation is that linking improves traceability. T1 C3 |
| **Actual behaviour** | The base layer computes the original-cost answer by reading the source document's own cost line; the sales-inventory layer then **overwrites it entirely** whenever an order line is present. The base lookup is **dead code for every order-originated credit note**. |
| **Materiality** | High — it inverts a designer's expectation about the value of provenance. |
| **Disposition** | `08` §4; `DC-08-02`. |

### C-07 — A future reversal date silently changes the cost basis

| Field | Content |
|---|---|
| **Contradiction** | "Full reversal" is expected to mean *exact reversal of the original entry*. T1 C2 |
| **Actual behaviour** | The full-reversal flag is computed as *not auto-posted and (modify or general entry)*. A future date sets auto-posting, so the flag goes false and the operation **silently degrades** to a re-derived cost basis at a later day's standard price. |
| **Materiality** | High. **The cost basis of a "full reversal" depends on whether the user picked today or tomorrow.** |
| **Disposition** | `08` §4; `DC-08-02`. |

### C-08 — The in-code comment on intercompany pricing is contradicted by the code beneath it

| Field | Content |
|---|---|
| **Contradiction** | A comment states the mirrored price is net of discount. T4 §4 |
| **Actual behaviour** | Price and discount are carried as **two separate fields**; the discount is not netted in. |
| **Materiality** | Low for P02 directly; **high as a reliance warning** — this package treats comments as claims to be tested, never as evidence. |
| **Disposition** | Recorded here and in T4 §4. |

### C-09 — Two incompatible answers to "which company's configuration applies"

| Field | Content |
|---|---|
| **Contradiction** | The **record's** company, or the **environment's**? T4 §2, §3 |
| **Actual behaviour** | Valuation mode, costing method, stock journal and the three stock accounts are company-dependent, and the consistency check validates them against the **environment** company, not the record's. One live consequence: the interim-account matching routine resolves the interim account **with no company context at all**, in direct contrast to the sibling cost-of-sales builder in the same file. Where the two differ, **matching silently does nothing.** |
| **Materiality** | Maximum under the scope correction. It is the difference between scope-as-ownership and scope-as-ambient-state. |
| **Disposition** | `20_P02_SCOPE_OWNERSHIP_MATRIX.md` SF-03. Added to this register by that file's §8. |

### C-10 — The durability ordering is inverted relative to accounting importance

| Field | Content |
|---|---|
| **Contradiction** | One expects accounting records to be the most durable artefacts in the system. |
| **Actual behaviour** | **The physical event is immutable** (a completed delivery cannot be cancelled or reversed); **the accounting event is reversible** (a posted invoice can be reset to draft, destroying its cost lines, and re-posted at a different cost); **and the settlement history is freely destructible, even across a closed period.** |
| **Materiality** | Maximum — it is the structural summary of this package. |
| **Disposition** | `11_P02_EDGE_CASE_MATRIX.md` §4; `18_P02_PMO.md` §2. |

## 2. Contradictions Between Evidence Tracks

**None found.** The four tracks were run independently against the same root with independently declared
denominators. Where two tracks touched the same mechanism — the posting routine's lock-date shift (T1 C5,
T3 §1, T4 §6b) and the currency fallback (T2 §3, T4 §4) — they agree, and each reached it by a different
path. Agreement reached independently is **corroboration**; it is recorded as such and is **not** treated
as additional proof of correctness.

## 3. Contradictions With Prior Sessions

| Prior finding | P02's position | Disposition |
|---|---|---|
| Core ledger: **silent 1:1 FX fallback** | **Confirmed independently** from the O2C side, and **extended**: there is a second, earlier arm — the **undated earliest-rate** arm — which is more likely to fire and less visible than the 1:1 arm. | **Material delta supplied.** Routed to the existing FX ruling track as **P02-X-03 / D-04**. Not re-adjudicated. |
| Core ledger: **system-derived accounting date** | **Confirmed** and localised to the sale side: a blank document date on a customer invoice becomes today, while the same blank on a vendor bill is a hard error. | Recorded; not re-adjudicated. |
| Core ledger: **no year-close entry** | **Confirmed** with a complete denominator: six patterns over the whole root; the only closing-entry generator found is for VAT. **Open caveat:** localisation modules were not separately enumerated as their own denominator. | Recorded with the caveat attached. |
| Core ledger: **hard lock defeated by a contacts-role partner merge** | **Confirmed independently**, and the complete denominator established: the bypass sentinel appears on **5 lines in 3 files with exactly 2 use sites, both in partner merge**. | **Denominator supplied.** Routed as **P02-X-04**. |
| Inventory: **COGS terminal HOLD; the reference perpetual pattern is unstable across versions** | **Not re-adjudicated.** P02 supplies the O2C-side evidence — the three-outcome configuration trap and the Thai-chart default shape — and routes the decision. | `DEPENDENCY OPEN` **D-01**. |
| Inventory: **multi-tenant invariant set and ruling conformance** | **Not restated and not re-adjudicated.** P02 consumes the boundary rules; it does not define them. | `DEPENDENCY OPEN` **D-02**. |

## 4. Self-Corrections Made During This Session

Preserved per the constitution — **wrong prior conclusions are not deleted.**

| # | Original statement | Correction | Trigger |
|---|---|---|---|
| SC-1 | "With the Thai chart installed and real-time valuation on, the outflow routine raises a hard error at delivery." | Real-time valuation **cannot be switched on at all** without the three accounts — a validation constraint refuses the change. The runtime guard exists as a **second** line of defence, and its presence is itself evidence that the configuration constraint is not considered sufficient. | Reading the category constraint after writing the first draft. |
| SC-2 | "The document date is what a tax authority sees; the accounting date is what the ledger sees — the two diverge." | Sharper: **the tax report keys on the accounting date too.** The printed tax invoice shows the original date, while **both** the VAT return and the ledger use the later period. | T3 §1. |
| SC-3 | "Split recognition off means cost is recognised at delivery." | Only if the outbound stock account happens to be an expense account. **A third outcome exists** — split recognition off with an interim outbound account — in which **cost of sales is recognised nowhere**. | Reading the account resolution independently of the boolean. |

**`SUPPORTED INTERPRETATION`.** All three self-corrections came from **re-reading primary source after
writing a conclusion**, not from a reviewer. That is the pattern the negative-claim standard warns about:
a first-pass reading produces a plausible statement that primary source then narrows. It is recorded here
as method evidence, not as a defect in the finding.

## 5. Verification Of Track Findings By The Primary Session

`Independent Review != Truth. Verified Evidence = Truth Basis.`

Track findings were **not** accepted on the track's authority. The primary session independently
re-derived, from the same root:

| Finding | Re-derived independently? |
|---|---|
| The standard-price top-up in the cost re-derivation | **yes** — read before T1 reported it |
| The lock-date silent shift | **yes** — read before T3 and T4 reported it |
| The absence of an idempotency guard on cost generation | **yes** — the 4-occurrence denominator was run by the primary session |
| The Thai chart's 27 accounts and 18 taxes | **yes** — counted directly |
| The picked-marker valuation gate | **yes** |
| The two-arm currency fallback | **yes — re-derived after the first draft.** See §6. |
| The shared inter-company transit location | **yes — re-derived after the first draft, and one overstatement corrected.** See §6. |
| The withholding tag asymmetry | **yes — re-derived after the first draft.** See §6. |

**At first drafting, three material findings rested on a single track's reading.** All three were
subsequently re-derived by the primary session from the same root; the record of that re-derivation, and
the one correction it produced, is §6. **No material finding in this package now rests on an
unverified single-track reading.**

## 6. Independent Re-Derivation Record

| Finding | Re-derived from | Outcome |
|---|---|---|
| **Two-arm currency fallback** | `R/base/models/res_currency.py:121-141` read directly | **Confirmed exactly.** The three-arm construct is present at `:140`: latest rate at or before the date; **the earliest rate of any date, with no date filter, ordered ascending** (`:133-136`); then the literal `1.0`. The second `or 1.0` one layer up is present at `:157`. |
| **Withholding tag asymmetry** | `R/l10n_th/data/template/account.tax-th.csv:26-29` and `:58-73` read directly | **Confirmed exactly.** All four sale-side withholding taxes carry an **empty tag column on all four of their repartition rows**; all eight purchase-side ones carry a full tag set on all four. |
| **Shared inter-company transit location** | `R/stock/data/stock_data.xml:54-60` and `R/stock/models/res_company.py:185-215` read directly | **Confirmed with one material qualification the track omitted — see C-11.** |
| **Interim-account matching runs without a company context** (T4 §3, the evidence behind C-09) | `R/stock_account/models/account_move.py:183-215` read directly | **Confirmed exactly.** The account resolver is called at `:207` with **no company context**, while the sibling cost-of-sales builder in the same file sets one at `:109` before resolving accounts at `:123`. The five skip conditions are also confirmed as stated: not an invoice; split recognition off; no linked completed customer-direction movement; product not under real-time valuation; interim account not flagged reconcilable. |
| **Delivery immutability** | `R/stock/models/stock_move.py:1971-1973` read directly | **Confirmed**, with one nuance the package did not state: the refusal carries an exception for **scrapped** movements. |

### C-11 — The transit-location rewiring is gated, and the track did not say so

| Field | Content |
|---|---|
| **Track statement** | *"Creating any company rewires stock routing on every other company in the database"* — T4 §5. |
| **What the primary session found on re-derivation** | The rewiring routine **returns early** unless the acting user holds the multi-company group — `R/stock/models/res_company.py:203-204`. |
| **Corrected statement** | The shared, company-less transit location **is** a database-global record (`R/stock/data/stock_data.xml:54-60`), and creating a company **does** unarchive it database-wide unconditionally (`R/stock/models/res_company.py:187-189`). But the **rewiring of every other company's partner stock locations** happens **only when the acting user holds the multi-company group.** The unqualified claim is an overstatement. |
| **What survives unchanged** | The object still has **no owning scope**, the unarchive is still unconditional, and the routine still enumerates the whole company table as superuser once the gate is passed. `20_P02_SCOPE_OWNERSHIP_MATRIX.md` SF-04 stands; only its scale claim is narrowed. |
| **Method significance** | **This is the only material overstatement found in ~2,000 lines of track output across four tracks, and it was found by re-derivation, not by the track's own review.** It is direct evidence for the standing rule that a track's headline table is not citable — only its verified branch is. |

**`SUPPORTED INTERPRETATION`.** One overstatement in four tracks is a good result for the track method
and a poor argument for skipping re-derivation: the overstatement was in the single most
scope-significant finding of the whole package.
