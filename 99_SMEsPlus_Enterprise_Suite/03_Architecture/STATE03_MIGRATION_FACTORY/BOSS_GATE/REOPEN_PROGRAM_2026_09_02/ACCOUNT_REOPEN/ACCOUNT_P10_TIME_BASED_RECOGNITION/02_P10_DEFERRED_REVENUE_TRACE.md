# P10 — DEFERRED REVENUE TRACE

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1 · Evidence IDs resolve in `12_P10_SOURCE_LINK_REGISTER.md`

Scope of this trace: **reference-ERP observed behaviour**, obtained by reading primary source in reference root `RR-1`. It is `REFERENCE BEHAVIOR`, not SMEsPlus design authority. Where the reference behaviour is judged unacceptable that judgement is stated separately and marked.

---

## 1. Stage 1 — Source Document

A customer invoice line carrying an income-type account, with a start date and an end date written on the **journal item** (not on the invoice, not on a schedule). Eligibility is decided by document direction and account type, and is enforced only as a form-level reaction, not as a stored constraint (`E-P10-017`).

Producers observed:
- manual entry by a user on the invoice line (`E-P10-042`);
- subscription billing, which writes the window from the billing plan (`E-P10-041`);
- inbound electronic invoicing, which writes the window from the statutory invoice period of the received document (`E-P10-040`).

**`P10-F-11` originates here**: the third producer means an inbound legal declaration silently becomes a revenue recognition instruction.

## 2. Stage 2 — Recognition Base

The base is the journal item's company-currency balance (`E-P10-011`). Neither the foreign-currency amount nor the rate is carried into the recognition machinery.

Consequence (`P10-F-04`): for a foreign-currency contract, the entire service period is recognised at the rate in force on the invoice date. No subsequent period can carry a different rate, because the recognition lines have no currency dimension to revalue. The reference behaviour is therefore *internally consistent* — it is a deliberate freeze — but it removes the ability to express the alternative treatment at all.

## 3. Stage 3 — Schedule

Derivation, in order:
1. The window is `[start, end]`, both **inclusive** (`E-P10-015` documents the inclusive assumption explicitly).
2. The window is cut at **calendar month ends** (`E-P10-007`). This is unconditional.
3. Each segment's amount is computed by one of three allocation rules (`E-P10-006`):
   - `day` — true calendar days;
   - `month` — a 30-day synthetic month in which the last calendar day of any month is normalised to day 30 (`E-P10-005`);
   - `full_months` — both window and period are snapped to the first of the month before measuring.
4. Rounding residue is forced into the **final** segment (`E-P10-009`).

Three consequences:
- **`P10-F-12`** — the schedule grid is monthly under every setting. The `day` rule changes the *weights*, never the *dates*. A contract requiring daily revenue recognition cannot be expressed.
- The `month` rule makes February, March and April produce identical monthly amounts. That is the stated intent, and for a 12-month contract it is defensible; for a 6-week contract it materially distorts.
- A window of exactly one year expressed as 1 Jan → 1 Jan (rather than 1 Jan → 31 Dec) is 12 + 1/30 months and produces uneven amounts. The product warns but does not prevent (`E-P10-015`).

## 4. Stage 4 — Period Event

**There is no period event object.** The segment set is computed, consumed, and discarded inside one generation call (`E-P10-008`). Nothing persists that says "period 3 of 12 has been recognised".

`P10-F-07`. Every downstream control in this trace is therefore a proxy control.

## 5. Stage 5 — Accounting Event and Stage 6 — Journal

Two mutually exclusive paths, selected by one company setting (`E-P10-018`).

### 5.1 Path A — on source-document validation

At posting time, in one transaction (`E-P10-008`):
- one **full deferral** entry dated at the source document's accounting date, moving the whole amount from the income account to the deferred revenue account;
- one **recognition** entry per month-end segment, moving that segment's share back from deferred revenue to income;
- every entry is stamped for automatic posting at its own date; entries dated in the future stay in draft until the cron reaches them (`E-P10-035`, `E-P10-038`);
- entries that would net to zero within the same month as the full deferral are deleted before posting (`E-P10-010`).

### 5.2 Path B — manual and grouped

From the deferred-revenue report, for a chosen period end (`E-P10-019`):
- one **grouped** entry dated at period end, aggregating every eligible item across the whole population;
- one **reversal** dated the next day (`E-P10-021`);
- a lock-date check that refuses if the period is locked (`E-P10-020`);
- a duplicate guard keyed on the existence of a related entry at that exact date in an acceptable state (`E-P10-022`).

### 5.3 The path divergence — `P10-F-06`

The two paths do not produce the same books. Path A produces a deferred-revenue balance that unwinds monthly. Path B produces a period-end reclassification that is undone the following day and re-derived from scratch each month. The **balance sheet is the same at each month end; the general ledger is not, the audit trail is not, and the sub-ledger reasoning is not.**

Switching the setting mid-life migrates nothing. Items deferred under Path A keep unwinding; items posted after the switch are handled by Path B; the report's duplicate guard was not designed to arbitrate between the two.

This is the direct violation of `ONE ECONOMIC FACT -> ONE RECOGNITION EVENT PATH` that the process directive requires be attacked. It is not a defect of implementation; it is a defect of semantics, because both shapes are individually defensible and the product provides no rule for which is correct.

## 6. Stage 7 — Modification

Available:
- change the window **before** any deferral entry exists — unconstrained;
- change the account **after** deferral entries exist — blocked (`E-P10-012`);
- reset the source document to draft, which reverses or unlinks the deferral entries and permits re-derivation (`E-P10-013`), unless the deferral groups more than one source document, in which case reset is refused outright.

Not available: any change to an in-flight schedule that keeps the already-posted periods and re-derives only the remainder. See `P10_NEGATIVE_CLAIM_REGISTER` `NC-04` for the exact class and search boundary of this negative.

## 7. Stage 8 — Reversal and Cancellation

Reversal is decided per generated entry, not per schedule (`E-P10-045`): unlink where permitted, cancel where the audit trail protects the entry, reverse otherwise. Because the schedule has no identity, the three outcomes can be mixed across the periods of one contract, and nothing records that they were.

A credit note against the source document does **not** propagate to the deferral schedule; it is an ordinary reversal of the source entry. The deferred balance continues to unwind unless the source document is reset to draft.

## 8. Stage 9 — Reporting

Two report surfaces (`E-P10-043`), read-only, showing the *computed* spread of the eligible population — recomputed from the two date fields on every render, not read from posted history. The report is therefore a **model of what should have been recognised**, not a record of what was. Where posting was re-dated by a lock (`P10-F-05`) the report and the ledger disagree, and the report is the one that is right about the economics.

## 9. Stage 10 — Close

- Path B refuses to generate into a locked period (`E-P10-020`).
- Path A does not check. The entry reaches the shared posting layer, which **silently overwrites its date** with the next permissible accounting date (`E-P10-036`, `E-P10-037`).

`P10-F-05`. The amount is unchanged; the period it lands in is not. No exception, no message, no flag records that the recognition period was moved. Because there is no period event object, nothing afterwards can detect it.

## 10. Scope Determination (`REV2-CORR1`)

| Question | Answer for deferred revenue | Basis |
|----------|------------------------------|-------|
| What scope OWNS the schedule? | COMPANY — it is inseparable from the journal items | `E-P10-001` |
| What scope OWNS the service window semantically? | TENANT — it is a contract fact | Business semantics; see `10b` |
| What scope EXECUTES generation? | The **active** company, or the cron user's company | `E-P10-004`, `E-P10-038` |
| What scope may MUTATE it? | Any user who can edit the source journal item | `E-P10-012` is the only guard |
| Which company owns the financial effect? | The document's company | `E-P10-003` |
| Executing scope == owning scope? | **No** — `P10-F-02` | |

## 11. Classification of this trace

| Section | Classification |
|---------|----------------|
| §1–§9 factual descriptions | `REFERENCE BEHAVIOR`, verified against primary source |
| `P10-F-04`, `P10-F-05`, `P10-F-06`, `P10-F-07`, `P10-F-11`, `P10-F-12` | `VERIFIED FACT` within reference root `RR-1` |
| §5.3 judgement that both shapes are individually defensible | `INFERENCE` |
| §7 statement about credit notes | `INFERENCE` — derived from the absence of any propagation path in the searched scope; see `NC-06` |


---

## 12. The Two Journal Shapes — corrected and sharpened

`66` Challenge C §6.

**Non-migration is now VERIFIED, not asserted.** An executed search over both module trees finds **five non-view read sites** for the generation-method setting and **no hook, constraint or migration script on either field**. Class `A` bounded to the reference root, with a positive control.

**The equivalence claim was both understated and overstated.**

*Understated:* the income statement is also equal for any interval bounded by month ends, not only the balance sheet — because the grouped path's cumulative reclassification differences out to the amount earned in the month.

*Overstated — four verified non-equivalences:*

1. **Different allocation rule.** The grouped generation passes a boolean where a direction name is expected, so **the revenue computation method is always applied, on both reports**. Where the two direction settings differ, the two shapes produce **different monthly amounts for the same fact**.
2. **Different residue destination** — the profit-and-loss account on one path, the control account on the other. A second, independent instance of the one-fact-two-shapes violation, not previously cited in support of it.
3. **Different analytic effect.** One path nets to zero; the other writes two non-cancelling weighted distributions. **The same economic fact produces zero analytic movement under one company setting and non-zero under the other.**
4. **Intra-month divergence is total.** The grouped path's deferred balance exists on the period-end date only and is reversed the next day. A balance sheet drawn on **any** date other than a month end shows the full unearned amount as earned under one path and correctly deferred under the other. The package stated the month-end equality and never its converse, which is the larger fact.

**The switch is asymmetric, and one direction is destructive.** Switching from grouped to validation: the validation path fires only inside the posting of a document being posted, so pre-switch invoices are never revisited, their last grouped entry has already been reversed, and from the switch onward **there is no deferred balance at all** for them. The deferral is not stranded — it is **silently abandoned**. The other direction is largely safe because the grouped guard excludes the validation path's entries.

**And the earlier phrasing was too strong:** the guard *does* arbitrate in the normal case. It arbitrates by a **date-and-state proxy** that fails in two named conditions, and one switch direction bypasses arbitration entirely because no code path revisits already-posted documents.