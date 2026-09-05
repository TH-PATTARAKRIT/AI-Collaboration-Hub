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
| **Evidence required to close** | A runtime reproduction: post a future-dated customer invoice for a storable, real-time-valued product through a soft-post caller, then post it again and count the cost lines. **The originally stated reason — no database access — was itself an untested negative claim and is withdrawn (`RE-13`).** The real position is narrower and is itself a finding: the deployed database examined has **zero** cost-of-sales lines, because split recognition is off there, **so it cannot exhibit duplicated ones**. Closing `C-04` needs either a deployment with split recognition on, or a live transaction. |
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

### C-12 — The Thai inbound-interim asymmetry does not exist

**Original:** the Thai chart supports the purchase-side interim mechanism and not the sales side.
**Contradicted by:** the account occurs once, in its own definition row, wired to nothing (`EV-P02-081`).
**Correct:** neither direction is chart-supported — a **uniform absence**, not an asymmetry.
**Materiality:** high — it was a headline in `01` and `07` and it routed a false question to P01.
**Disposition:** withdrawn and replaced by P02-F-38c. Raised by independent challenge **CH-01**, verified.

### C-13 — Owner-restricted stock does not produce a phantom cost line on an order-linked invoice

**Original:** two confirmed phantom-cost paths follow from the eligibility mismatch.
**Contradicted by:** the re-derivation subtracts owner-excluded quantity before the top-up, the result is
zero, and the generator's zero-skip fires (`EV-P02-020`, `EV-P02-016`).
**Correct:** **one** confirmed instance, the unpicked-completion case. The owner-restricted path survives
only where no order line is linked, which is already P02-F-21.
**Materiality:** moderate — it removes a claimed defect and reclassifies an edge case as sound.
**Disposition:** `03` §5a. Raised by **CH-02**, verified.

### C-14 — The reset-to-draft control exists and is wired on one side only

**Contradiction:** the package treated the destruction of cost lines as an absence of control.
**Actual:** a guard exists that would prevent it, and the link it tests is written in **one** non-test
place in the whole root — on the **purchase** side (`EV-P02-092`, `EV-P02-086`).
**Materiality:** high, and it makes the fix cheap: the control is already built.
**Disposition:** P02-F-24b; collapses with P02-F-15 into one root cause. Raised by **CH-03**, verified.

### C-15 — The obligation ledger does not resolve six findings

**Contradiction:** `10` §2 claimed six; three of the six are **one defect described three times** and
three are untouched by it (the service case, the producer defect, the chart gap).
**Materiality:** high — it was the package's principal handoff to Core Accounting Reconciliation.
**Disposition:** `10` §2a; `17` D-I corrected and D-VI split out; H-01 corrected. Raised by **CH-13**.

### C-16 — A summary count did not reproduce from its own table

**Contradiction:** `11` §9 stated totals that a mechanical recount of the table beneath them contradicts.
**Materiality:** high as a **method** matter — this is the enumeration failure the denominator rule exists
to prevent, and it was found by an outside reader.
**Disposition:** recounted and restated; recorded as `RE-07`. Raised by **CH-14**.

### C-17 — The package's statement of its own evidence base was false

| Field | Content |
|---|---|
| **Original** | "This session had no database or runtime evidence", repeated across six deliverables and used to explain two undischarged very-expert requirements and one open gating unknown. |
| **Contradicted by** | **Five deployed database archives on the execution host**, with restore tooling already installed. One was extracted offline and is reported in `21_P02_DEPLOYED_DATABASE_EVIDENCE.md`. |
| **How it was found** | A **peer session's memory file** recording the identical error on another process. **Not** by six self-corrections; **not** by the twenty-finding independent challenge. |
| **Why both reviews missed it** | Both were scoped at **the findings**. Neither was scoped at **the evidence base**. A negative claim about what evidence exists is still a negative claim and needs a declared search. |
| **Materiality** | **Maximum.** It bounded the exit assessment, and it moved `EC-06` from partially satisfied to **not satisfied** — because a negative-claim control that governs findings but not the evidence base is not a control. |
| **What the evidence then produced** | An **empirical confirmation** of the package's central mechanism claim (447,384 journal lines, **zero** cost-of-sales lines, exactly as predicted from the deployed configuration), a **correction** to the "Thai default" claim, and **one live exposure the package had not identified** (`21` §4.3). |

### C-18 — Cash-basis tax: the template says one thing, the deployments another

**Original:** `T3` §4 — "the delivered Thai tax data does NOT enable cash basis", from the tax template.
**Contradicted by:** `22` TC-05 — **every deployed company record that has a value carries the
company-level cash-basis switch ON** (93 company records, 6 archives).
**Correct:** both are true of different objects. The company **switch** is on estate-wide; the **per-tax
exigibility** is not set, so no tax is actually treated on a cash basis. The package stated only the
template half, which reads as though the capability were off.
**Materiality:** moderate for P02, high for P07 which owns tax treatment. **Routed to P07.**

### C-19 — `P02-F-43` was wrong, and a peer process caught it

**Original:** `09` §1 — *"The reference process **does** keep these separate, and does it well"*, tagged
`FACT VERIFIED`.
**Contradicted by:** peer process P06, **and by P02's own evidence two sections below the claim**: a
payment may post **no journal entry at all**; the outstanding account is force-assigned only when the
full-accounting module is absent; a payment booked straight to bank is declared matched at creation, so
the intermediate state does not exist.
**Correct:** the separation exists **only in the outstanding-account configuration**. In the alternative
configuration the three events collapse.
**How it was found:** **not** by self-review, **not** by the twenty-finding independent challenge, **not**
by the deployed-database pass — by a **peer process reading P02 for its own purposes**.
**Materiality:** high as a finding and higher as method evidence: **the refuting evidence was already
inside the same deliverable.** An internal inconsistency between a headline and its own supporting section
survived every control this package ran.
**Disposition:** `09` §1 corrected; agrees with P06's proposed reconciliation; routed to P11.

### C-20 — The package's cost analysis was written against the wrong generation

**Original:** the whole cost-recognition analysis (`01` S5, `02`, `03`, `06`, `07`, `11`) is built on the
v18 mechanism — an interim account, a valuation-layer model, and a company-level split-recognition gate.
**Contradicted by:** `22` §3 — **the deployed estate is 5 of 6 archives and 92 of 93 company records on
the v19 line**, where the valuation-layer model **does not exist**, the split-recognition gate **has been
removed**, the interim account **has been eliminated**, and the delivery posts **nothing** for an ordinary
customer sale.
**Correct:** the v18 analysis is sound **for v18** and is explicitly generation-scoped from now on. The
v19 mechanism is documented in `22` §3.2 and its truth table in `22` §4.2.
**Materiality:** **maximum.** It does not falsify the v18 findings; it bounds them to one generation and
to one of six archives.
**Disposition:** `22` carries the generation split. Every cost finding in `01`–`11` is to be read as
**v18-scoped** unless it says otherwise.

### C-21 … C-28 — Registered In `25_P02_CLOSURE_CHALLENGE_AND_CORRECTIONS.md`

The second independent challenge produced eight further contradictions. They are recorded in full in `25`
§2 rather than duplicated here, and they are numbered continuously with this register:

| # | Subject | File |
|---|---|---|
| C-21 | `iSMEs` is **Odoo 16.0**, not v18 — a third generation, carrying 99.9% of transactions, with no source on this host | `25` §2 |
| C-22 | The archive denominator: **8 files / 5 databases**, not 6; two archives never opened; the deduplication key was wrong | `25` §2 |
| C-23 | "93 company records" is a snapshot-sum over duplicate databases — **91** | `25` §2 |
| C-24 | TC-03 contradicted by TC-07 four lines below it — 91 false, **2 NULL** | `25` §2 |
| C-25 | TC-04's periodic count does not close — **89**, not 88 | `25` §2 |
| C-26 | TC-08 refuted — two of three real-time companies **do** carry a stock journal | `25` §2 |
| C-27 | **TC-15's direction reverses** on the accounting date | `25` §2 |
| C-28 | §12's cash-basis conclusion refuted by **7,738 posted entries** | `25` §2 |

### C-29 … C-31 — Registered In `26_P02_V18_DEPLOYMENT_EVIDENCE.md`

Raised after a peer process (P04) corrected P02's population.

| # | Subject | File |
|---|---|---|
| C-29 | **TC-35 refuted** — a v18 deployment **does** exist (`idemo18_uat`, 40,353 journal lines), and its source is readable here | `26` §3 |
| C-30 | **TC-03 refuted a second time** — one company carries `anglo_saxon_accounting = TRUE` | `26` §3 |
| C-31 | **Runtime evidence was declared absent without looking.** A complete, safe, resettable Odoo 18 lab exists on this host with the required test already scripted | `26` §10 |

**Register total: C-01 … C-31, contiguous, no overlap. 20 here, 8 in `25`, 3 in `26`.**

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
