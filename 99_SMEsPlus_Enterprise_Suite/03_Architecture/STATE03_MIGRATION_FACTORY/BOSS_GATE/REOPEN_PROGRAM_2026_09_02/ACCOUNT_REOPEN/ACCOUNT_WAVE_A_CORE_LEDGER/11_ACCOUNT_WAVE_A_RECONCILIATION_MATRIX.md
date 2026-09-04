> **CORR1 CORRECTION NOTICE.** Amended by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`.
> Corrections landing here: `COR-09, COR-14, COR-17`. Governing text where they conflict with the body below: CORR1/C06; CORR1/C08.
> Prior findings are retained unedited for lineage; see `CORR1/C02_..._ACCEPTED_CORRECTIONS_REGISTER.md`.

# 11 — ACCOUNT_WAVE_A_RECONCILIATION_MATRIX

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

## 1. The Boss question, answered

> *Is reconciliation an accounting event, a matching state, a settlement semantic, a derived state,
> or a combination?*

**Answer — a combination of exactly three, and the three must be modelled separately.**

| Nature | What it is | Where it lives | Immutable? |
|---|---|---|---|
| **Matching record** | a stored pairwise fact: this debit item and this credit item are matched for this amount, in three currencies, as at this date | a first-class record | should be — **in the reference it is unconstrained** (`COR-09`) |
| **Derived settlement state** | residual, reconciled flag, matching marker, payment state, ageing placement | stored computed values on the item | no — derived, and must be reconstructible |
| **Emitted accounting event** | exchange difference; cash-basis tax | **new posted entries** | as any entry |

The reference model conflates the first two by storing the derived values, and hides the third
behind an operation users think of as clerical.

**Unreconciling is not an undo.** It removes matching records *and* posts reversals of the exchange
entries. A settlement and its withdrawal are both accounting events.

## 2. Reconciliation matrix

| Aspect | Reference behaviour | Evidence | SMEsPlus position |
|---|---|---|---|
| Granularity | pairwise, item to item — never entry to entry | `EV-014` | `ADAPT` |
| Amounts carried | three: company currency, and each side's transaction currency | `EV-014` | `ADAPT` — this is what makes difference computable |
| Bound against the item | **none — nothing prevents over-reconciliation, in any currency configuration** | `COR-09` | `EXTEND` — a hard bound is required |
| Residual | stored computed, both currencies | `EV-014` | `ADAPT` with a reconstruction guarantee |
| Partial match | marker `P`; residual reduced; no full-match record | `EV-014` | `ADAPT` |
| Full match | aggregation record created when residual reaches zero; owns the exchange entry | `EV-014` | `ADAPT` |
| Ageing placement | driven by the latest date among matched items | `EV-014` | `ADAPT` |
| Exchange difference | emitted automatically on a match where measurement differs | `EV-014` | `ADAPT` the emission; `EXTEND` the visibility |
| Missing rate | **converts at 1:1 with no error** | `COR-14` | **`REJECT`** |
| Cash-basis tax | emitted automatically; date ignores the tax lock in selection but the write is then refused, so the reconciliation **hard-fails** | `COR-17` | `EXTEND` — the failure must name the tax period as its cause |
| Write-off | mechanism exists; policy semantics not established | `GAP-E01` | `UNKNOWN` |
| Unreconcile | removes matches; **reverses the exchange entry by a new posted entry**; re-matches the reversal to the original so no residue shows | `EV-014` | `ADAPT` |
| Reconcile after reversal | a reversal posted against a posted original is auto-matched | `EV-012` | `ADAPT` |
| Destruction by un-posting | **matches are deleted silently when the entry is reset to draft** | `EV-012` | **`REJECT`** |
| Matching history | no dedicated history artefact identified | `GAP-E02` | `EXTEND` |
| Effect on period close | unreconciled bank statement lines **block** a fiscal-effective lock | `EV-019` | `ADAPT` — a good pattern |
| Payment state | derived from residuals; not an independent fact | `EV-014` | `ADAPT` |
| Account eligibility | an account property; receivable and payable types are forced reconcilable | `EV-019` | `ADAPT` |

## 3. What changes when reconciliation is partial

Answered explicitly, as required:

1. The item's **residual falls** in both currencies but the item **remains open**.
2. The matching marker becomes `P` — a marker, not a relation, so it carries no lineage.
3. **No full-match record exists**, therefore **no exchange difference is recognised yet** at
   full-match level; differences are recognised per partial where measurement differs.
4. Ageing placement moves to the **latest matched date**, so a partial settlement can move an old
   item into a younger ageing bucket.
5. Payment state becomes partially settled — derived, not stored intent.
6. The item stays available for further matching, and **nothing bounds the further matches against
   the remaining residual** (`COR-09`).

## 4. Reconciliation risks carried forward

| # | Risk | Class | Owner |
|---|---|---|---|
| `RC-01` | Over-reconciliation is structurally reachable — no bound between match and residual | `CONTRA-09` | Wave A |
| `RC-02` | Matching records are destroyed by an entry-level operation, silently | `CONTRA-10` | Wave A |
| `RC-03` | Missing rate converts at par, so an exchange difference is computed against a fabricated measurement | `CONTRA-08` | Wave A |
| `RC-04` | A settlement can hard-fail for a tax-period reason presented as a write error | `COR-17` | `WAVE-D TAX` |
| `RC-05` | Stored derived settlement values can drift with no identified reconstruction path | `GAP-E03` | Wave A |
| `RC-06` | No matching history — the question "was this ever matched, to what, and by whom" is unanswerable | `GAP-E02` | Wave A |
