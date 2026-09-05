# AI16 — P09_AAS_PLUS_ANALYTIC_INTEGRITY_CONSOLIDATION

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Role:** AAS+ — reconcile four AAS-03 challenges. **Dissent preserved. Consensus not forced.**
**Layer:** 1 — clean-room.

---

## 1. THE ONE-LINE POSITION

**The mechanism is real, it is firing in production at 98.57 % annihilation, and the author's characterisation of it was wrong in six separate ways — every one of them found by review, none by the author.**

## 2. DISPOSITION OF THE SIX REQUIRED ITEMS

| ID | Item | Disposition |
|---|---|---|
| **P09-AI-01** | record exists vs economic effect | **VERIFIED DEFECT.** Two well-formed records; net economic attribution zero. Measured, not inferred |
| **P09-AI-02** | symmetric balanced-pair allocation | **VERIFIED**, as a **conditional**: it holds where one allocation reaches every row of a balanced set. **Three mechanism families satisfy it, not five** |
| **P09-AI-03** | depreciation analytic attribution | **VERIFIED DEFECT, OBSERVED AT SCALE.** 670 of 685 assets allocated; 17,716 balance-sheet records annihilating 18,483 expense records; **98.57 % destroyed** |
| **P09-AI-04** | line eligibility | **VERIFIED.** By assignment alone — no account-type, row-type, context or company test on the creation path |
| **P09-AI-05** | scope ownership | **VERIFIED with one re-opened row.** Within-company for the intra-entry pair; a **cross-company** path was found and the closure withdrawn |
| **P09-AI-06** | cross-process cost duplication | **MECHANISM VERIFIED AT A CORRECTED LOCATION.** The author named the wrong pair; the genuine same-rate duplication is in a bridge module |

## 3. THE CENTRAL CLASSIFICATION

> ### **VERIFIED DEFECT — ANALYTIC RECORDS EXIST BUT ECONOMIC COST ZEROES OUT**
>
> Scope, stated exactly:
> - **exact zeroing** for asset depreciation, the cut-off/change-period accrual, and the two cash-basis pairs;
> - **residue rather than zero** for the change-account transfer, accrued orders, deferred recognition, and one tenant module — a different and arguably worse failure, since a residue looks like a real cost;
> - **observed in deployed data** at 98.57 % annihilation over a 685-asset population;
> - **not** confined to net-balance surfaces **in the target localization** — see §5.

## 4. WHERE THE FOUR EXPERTS AGREED

Convergence across disjoint assignments, none of them derived from another:

| Point | Reached by |
|---|---|
| the algebra is sound and the theorem holds as a conditional | all four |
| eligibility is by assignment alone; no account-type or row-type test on the creation path | three |
| the author's mechanism list over-applied the theorem | two, independently |
| the author's declared blind spot was **populated**, not theoretical | two, independently, by different measurements |

**The last row is the finding about the session itself.** Two reviewers, working on different assignments, each opened the residue the author had declared and left closed, and each found something material in it.

## 5. WHAT THE CHALLENGES OVERTURNED — SIX AUTHOR ERRORS

Ranked by consequence.

### 5.1 The evidence base was wrong, and the defect is not latent
The author concluded no deployment carried the precondition. **A 155 MB deployed dump was missed because the evidence strand's own listing command ended in a display limit over a 2,553-file directory.** The author re-ran the extraction directly and confirmed: **670 of 685 assets allocated, 98.57 % of depreciation attribution annihilated.**
**A negative result is only as good as the command that produced it — including its output limits.**

### 5.2 The target localization defeats the one surface called "correct"
The author stated budget consumption reports the full cost because its query admits only income and expense accounts. **In the Thai chart of accounts, both accumulated-depreciation accounts are typed as a depreciation-**expense** type on asset-range codes, and the filter splits that type on its first token — so it matches as an expense and the balance-sheet leg is admitted.** The chart contains no fixed-asset account at all, so these are the only candidates a Thai install offers.
**On a Thai-chart deployment, budget consumption nets to zero too.** The scope statement "confined to net-balance surfaces" **does not hold for the target market of this entire programme.** Verified directly by the author against the shipped chart.

### 5.3 The sweep's denominator did not contain its own subject
Declared pattern: 45 sites, 11 modules. Union with the two assignment forms: **82 sites, 23 modules (+82 %, +109 %)** — and **the headline both-legs write site is a subscript assignment, outside the declared pattern**. The author found it by reading the function, not by the sweep.

### 5.4 Two mechanisms were mis-classified as symmetric
The change-account transfer and accrued orders **re-derive** the counterpart's allocation rather than copying it. They fail by **residue**, not cancellation — and for two reasons the author had not identified: unallocated source rows dilute the counterpart's denominator, and percentage rounding shortens it further.

### 5.5 The intent question was declared unanswerable, and is answered
The author wrote that the source carries no statement of intent. **It does:** the analytic account's only statistic button is labelled **"Gross Margin"** over the net balance, the drill-down action carries the same name, and its help text names costs and revenues only. **The declared design is a margin ledger.** This *strengthens* P09 — allocating a balance-sheet leg into a margin ledger departs from the product's own stated purpose.

### 5.6 The most quotable paragraph rested on an uncited premise
The "masking interaction" assumed machine-hour rates recover depreciation. **The source shows the rate is a bare scalar with no components, no asset link, and three incompatible names across three modules.** Re-based to what the source supports: **the rate has no declared composition and no provenance, so anything folded into it is untraceable.** Stronger, and no longer imported from outside the evidence base.

## 6. DISSENT PRESERVED — NOT RECONCILED

| ID | The disagreement | AAS+ position |
|---|---|---|
| **D-01** | The disprover calls the hypothesis `CONTRADICTED as stated`; the other three treat the mechanism as confirmed. | **Both stand.** The theorem is confirmed; the author's *application* of it was contradicted. Recording only "confirmed" would erase the correction; recording only "contradicted" would misstate the mechanism. |
| **D-02** | One reviewer ranks the cash-basis pair as requiring cancellation (it would otherwise double-count); the author had ranked it the programme's most severe finding. | **The reviewer prevails on the economics.** The author's ranking is **withdrawn** — it carried the highest reversal risk in the package. What survives is a data-hygiene defect: 16,332 guaranteed-noise records measured in deployment. |
| **D-03** | Whether the cut-off wizard is a defect at all, given it carries no new economic effect. | **UNRESOLVED, and the sharper framing is adopted:** the analytic cut-off **does not happen** — the cost stays attributed to the period the wizard was invoked to move it out of. That is a **period-misattribution** defect, not a net-zero one. The reviewer's proposed discriminator — *does the entry change a dimension the record carries?* — is adopted in place of *does it carry a new economic effect*, and it **weakens the author's own concession** on the change-account transfer, which changes the general account, a dimension the record does carry. |
| **D-04** | Whether the residue mechanisms are worse or milder than the zeroing ones. | **UNRESOLVED.** A clean zero is recognisable; a residue looks real. AAS+ declines to rank them and records both. |
| **D-05** | One reviewer holds SW-U-04 (tenant custom modules) **CLOSED**; another did not search it. | **CLOSED on the searcher's evidence**, with its declared class-C residue for archive files that grep cannot read. |

## 7. AAS+ FINDINGS NO SINGLE REVIEW PRODUCED

**AAS+-AI-1 — The session's own controls failed in the same shape as the defect it studied.** The defect is: *a mechanism that faithfully does what it was told, over a population nobody checked was the right one.* The session's evidence strand did exactly that — ran a correct command over a truncated listing. **The lesson is not "search harder"; it is that a bounding claim must be produced by a command that could have returned the counter-example.**

**AAS+-AI-2 — Every author error was found by review; none by the author.** Six errors, four reviewers, zero self-caught. This is now the invariant result of this programme, and it should be treated as a design parameter of the process rather than a recurring surprise.

**AAS+-AI-3 — The Thai finding is the most actionable item in the package and is not an analytic finding at all.** It is a chart-of-accounts typing question, discoverable in a 28-line file, and it changes the blast radius of every other finding here for the target market. **It was found only because one reviewer was told to enumerate the localization.** No amount of deeper analytic analysis would have surfaced it.

**AAS+-AI-4 — The strongest verified statement in the package is now empirical, not theoretical.** 98.57 % annihilation over a real population outranks any theorem for a Boss decision, and it was obtained by re-running an extraction the session had already declared complete.

## 8. AAS+ VETO STATUS

| ID | Veto | Status |
|---|---|---|
| `AAS+-VETO-01` | no implementation while the accounting-event identity is undefined | **UPHELD and strengthened.** The event-level completeness check is the one control that would have caught every mechanism here, and it needs the event object |
| `AAS+-VETO-02` | no adoption of the report-shadowing mechanism | **UPHELD, unchanged** |
| **`AAS+-VETO-03`** *(new)* | **no SMEsPlus asset, accrual, deferred-recognition or cash-basis design may allocate a balance-sheet row into the management ledger** | **RAISED.** Grounds: verified in source, verified in deployed data at 98.57 %, and contrary to the reference product's own declared margin-ledger intent. Scope: design adoption only |

## 9. WHAT AAS+ DOES NOT CLAIM

No statutory claim, Thai or otherwise — the Thai finding is an **internal** contradiction between a chart's code block and its account typing, and every statutory reading of it is `HOLD — STATUTORY EVIDENCE REQUIRED`. No settlement of `HOLD-AS-01` or `DIS-09`. No class upgraded. No gate moved.

## CHECKPOINT

**CP-AI13(a) — AAS+ CONSOLIDATION COMPLETE.** Six disposition items settled, six author errors recorded, five dissents preserved, one new veto raised. Auto-continue.
