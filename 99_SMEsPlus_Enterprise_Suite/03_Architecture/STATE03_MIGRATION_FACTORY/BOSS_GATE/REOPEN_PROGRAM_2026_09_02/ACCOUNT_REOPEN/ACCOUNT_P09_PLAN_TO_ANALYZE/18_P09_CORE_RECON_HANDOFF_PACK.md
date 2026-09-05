# P09_CORE_RECON_HANDOFF_PACK

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Terminal state declared by the directive:** READY FOR CORE ACCOUNTING RECONCILIATION
**Layer:** 1 — clean-room.

---

## 1. WHAT THIS PACK HANDS OVER

Core Accounting Reconciliation receives from P09 **five things**: a boundary, a set of requirements, a set of contradictions, a set of dependencies it must resolve or accept, and two vetoes it must honour or overturn.

It does **not** receive an approved model. P09's own gate recommendation is HOLD (`P09_PMO` §5).

## 2. THE ONE-PARAGRAPH HANDOVER

Management accounting in the reference pattern is expressed as **physical database schema plus a schemaless payload** rather than as scoped, relationally-integral data. Eleven independently-found defects follow from that single choice. Management records exist in three populations — derived from posted ledger truth, derived from unposted documents, and operational measurements with no financial event at all — and the system does not distinguish them. A financial report can present the second and third populations as posted ledger data. A management allocation on a posted, lock-dated, hash-chained entry can be changed by an ordinary billing role, with no audit trace, and every budget figure over that period changes silently as a result. A periodic reallocation rule converts management allocations into real journal entries, selects amounts by dimension, moves the whole balance when only a share was allocated, and writes no dimension onto what it posts. **Two of the eight constitutional trace steps — the financial-event identity and the cost object — have no carrier at all, so the trace cannot be inherited and must be authored.**

## 3. THE RECONCILIATION QUESTIONS P09 HANDS TO CORE ACCOUNTING

These are the questions P09 cannot answer alone and Core Accounting must.

| # | Question | Why it lands here | P09's position |
|---|---|---|---|
| **Q1** | What **is** an accounting event, as an identified object with provenance? | P09's entire traceability layer is expressed relative to it, and it does not exist | P09 requires: immutable identity, provenance carrier, and a link that a derived management record cannot discard |
| **Q2** | Does period close bind **management** truth as it binds financial truth? | P09 says it must (AB-07); Core Accounting owns the close | P09 requires closed-period allocations to be immutable, with correction by a dated reallocation event in an open period |
| **Q3** | Does the integrity envelope (hash chain, lock dates, tracked fields) extend to the management dimension? | today the allocation is in none of the three protection lists, none of the hash field lists, and not tracked | P09 requires it to be inside all three |
| **Q4** | Is a management allocation part of the **audit trail** of a posted entry? | today a change produces no chatter entry, no tracking value and no hash break | P09 requires every allocation change to be an append-only audited event |
| **Q5** | May a management rule create a financial posting, and under what authority? | the reference pattern's reallocation mechanism does exactly this on a schedule | P09 constrains the shape (B-05, EA-02) but does **not** authorise building one |
| **Q6** | What is the sign convention, declared once, at model level? | management data is signed inversely to the ledger, systematically | P09 requires one declaration and requires every published equation to state it |
| **Q7** | Is commitment ledger-visible? | it decides where budget control can be enforced (BC-02) | open — `DEC-P09-04`, `PD-03` |
| **Q8** | Which company owns the financial effect of a cross-company management aggregate? | the corrected constitution asks it directly | P09 requires explicit, authorised widening; never an empty field (B-09, MA-10) |

## 4. REQUIREMENTS HANDED OVER

Sixty-one numbered positions across the Layer 1 set. The ten that Core Accounting cannot proceed without:

| ID | Requirement |
|---|---|
| B-01 | one business fact, one financial effect; management representation is derived, never authored |
| B-02 | every management record declares an immutable provenance class |
| B-03 | where a financial event exists, the link is enforced by storage, not by the producing code |
| B-04 | management data never reaches a financial statement surface without a per-figure provenance marker |
| SM-03 | management records carry immutable identity; correction is a new signed record |
| SM-15 | no change class is implemented as a delete |
| DM-06/07/08 | allocation totals enforced at storage; relational integrity; uniform scope enforcement across all axes |
| AB-05 | actual-versus-budget is bidirectionally traversable |
| AB-07 | period close binds management truth |
| MA-08 | every analytic object declares an owning scope; context is derived from it, never applied uniformly |

## 5. THE THREE-TRUTH MODEL — THE CENTRAL HANDOVER

| Truth | Definition | May be summed into a financial statement? |
|---|---|---|
| **T1 Financial Ledger Truth** | posted accounting events and their double-entry effects | it *is* the statement |
| **T2 Management Dimension Truth** | the assignment of T1 to dimensions and cost objects | only with an explicit per-figure provenance marker |
| **T3 Operational Measurement Truth** | costed operational facts with no financial event — labour hours, machine hours, estimated valuations | **never**, without an explicit accounting event first |

The reference pattern merges T2 and T3 into one record type with one amount and no discriminator, then permits the merged result to be presented as T1. **Separating T3 is the single largest architectural requirement P09 produces.**

## 6. VETOES CORE ACCOUNTING MUST HONOUR OR OVERTURN

| ID | Veto | Scope | Lifted when |
|---|---|---|---|
| **AAS+-VETO-01** | no implementation of the P09 management-accounting model may begin while the financial-event identity is undefined | **implementation only** — design, Boss decisions and other processes are unaffected | the accounting-event identity is defined and ratified |
| **AAS+-VETO-02** | no SMEsPlus design may adopt the report-shadowing mechanism for any statement presented as accounting information | design adoption | not lifted by the disproof of the row-multiplication exposure; that disproof addressed reachability, not the assertion of a false posting state |

## 7. WHAT CORE ACCOUNTING MUST NOT INFER FROM THIS PACK

- **No class B, C or D finding may be restated as class A.** The eleven unsearched items in `P09_CONTRADICTION_REGISTER` §D are unsearched, not absent. This includes "no budget control" (class A within two modules, **class C system-wide**) and "no equipment link" (class B with a declared four-module boundary).
- **No statutory claim, Thai or otherwise, is made anywhere in this package.** Three Thai items are held and routed to the Accounting-Tax track.
- **The disproved candidate is not a safe mechanism.** It is a latent hazard whose correctness depends on one filter that one call site happens always to attach.
- **Nothing here is executed.** Every operational consequence is a code-path conclusion. Four dependencies can only be closed by execution.
- **P09 does not adjudicate between parallel evidence tracks.** Where another branch's evidence overlaps, it is a pointer only.

## 8. OPEN ITEMS TRANSFERRED

| Class | Count | Where |
|---|---|---|
| blocking dependencies | 2 | `20` §A |
| peer dependencies open | 7 | `20` §B |
| evidence dependencies | 8 (+1 Jira) | `20` §C, `12` §5 |
| Boss determinations | 5 | `20` §D |
| held for evidence | 7 | `20` §E |
| preserved disagreements | 7 | `11` §B |
| declared unsearched | 11 | `11` §D |

## 8A. ANALYTIC ECONOMIC INTEGRITY — CONTINUATION ADDENDUM

Full package under `AI_ANALYTIC_ECONOMIC_INTEGRITY/`. The four items Core Accounting must carry forward:

**1. The measurement, which outranks every argument in this package.**
> In a deployed database, **670 of 685 assets carry a management allocation**, and **17,716 balance-sheet-leg records annihilate 18,483 expense-leg records — 98.57 % of the depreciation attribution destroyed** (gross 206,518,404.07; net −2,961,221.81). Verified by the research team's own re-extraction, not accepted on report.

**2. The rule that produces it.** An allocation is carried **per row**, while the attribution's subject is the **event**. Where one allocation reaches every row of a balanced set, the records mirror and the net is zero — a theorem, not an observation. Where a counterpart's allocation is instead **re-derived**, it fails differently, leaving a residue that looks like a real cost. Both come from the same root cause.

**3. The one control that would have caught all of it.** An **event-level completeness check**: the accounting event declares its intended attribution, and the system verifies that the records it produced sum to it. Cheap, checkable at creation, and impossible without the accounting-event identity — which is why `AAS+-VETO-01` stands.

**4. The localization finding, which is actionable now.** The Thai chart types both accumulated-depreciation accounts as an **expense** type on asset-range codes and ships **no fixed-asset account**. The budget query splits the type on its first token, so the balance-sheet leg is admitted and **budget consumption nets to zero on a Thai-chart install** — defeating the one surface this package had called correct. **If an asset's depreciation account points at either Thai accumulated-depreciation account, that asset's depreciation consumes no budget.** Statutory readings are held; the internal contradiction is verified.

**What Core Accounting must NOT infer:** the sweep's counts are a **lower bound** (45/11 declared, 82/23 measured); `AI-E-02` is derived from a misread witness and must be re-derived or dropped; the cash-basis pair's cancellation is arguably **required**, not defective; and no class B, C or D anywhere in this package may be restated as A.

**New veto:** `AAS+-VETO-03` — no SMEsPlus asset, accrual, deferred-recognition or cash-basis design may allocate a balance-sheet row into the management ledger. Design adoption only.

## 9. TERMINAL STATE

**READY FOR CORE ACCOUNTING RECONCILIATION.**

Qualified as follows, and the qualification travels with the declaration:
- P09's own gate recommendation is **HOLD** on **six** named blockers — the original four, plus the sweep-denominator re-derivation and the Thai chart-typing decision;
- **three** vetoes stand, all limited in scope;
- no approval is issued, nothing is merged, no implementation is authorised, and no gate has moved;
- **Boss is sole Final Approver.**
