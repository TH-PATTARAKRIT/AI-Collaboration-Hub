> **CORR1 CORRECTION NOTICE.** Amended by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`.
> Corrections landing here: `COR-02`. Governing text where they conflict with the body below: CORR1/C07 — accounting date is system-owned.
> Prior findings are retained unedited for lineage; see `CORR1/C02_..._ACCEPTED_CORRECTIONS_REGISTER.md`.

# 09 — ACCOUNT_WAVE_A_SOURCE_OF_TRUTH_REGISTER

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

Classification: `SOURCE FACT` (owned outside accounting) · `ACCOUNTING FACT` (owned by the ledger,
immutable once asserted) · `DERIVED FACT` (computed, must be reconstructible) · `REPORTING FACT`
(exists only in presentation) · `CONTROL FACT` (governance state).

A field appearing on several screens does **not** imply several owners. Each row names exactly one.

| Fact | Class | Authoritative owner | Reference position | Evidence |
|---|---|---|---|---|
| Document date | `SOURCE FACT` | the source document | the only date the user genuinely owns | `COR-02` |
| **Accounting date** | `ACCOUNTING FACT` | **the ledger, not the user** | system-derived; moved by a lock rule *and* by a numbering-convenience rule | `COR-02` |
| Recognition date | `SOURCE FACT` | the producing module | no distinct carrier exists — collapsed into the accounting date | `GAP-B02` |
| Due date | `SOURCE FACT` | payment terms on the document | stored on the item; outside hash coverage | `COR-06` |
| Transaction currency | `SOURCE FACT` | the agreement | required on every item, always | `EV-013` |
| Exchange rate | `ACCOUNTING FACT` | the rate table, by date | one per currency per day per company group | `EV-018` |
| **Balance (company currency)** | `ACCOUNTING FACT` | the item | **the canonical amount**; debit and credit derive from it | `EV-013` |
| Debit / credit | `DERIVED FACT` | derived from balance | stored, and hash-covered — the hash is keyed on the derivation, not the source | `COR-06` |
| Transaction-currency amount | `ACCOUNTING FACT` | the item | sign DB-constrained against balance; **magnitude unprotected** | `COR-06` |
| Account | `ACCOUNTING FACT` | the item | **retargeted silently by a merge** | `COR-08` |
| Counterparty | `ACCOUNTING FACT` | the item | hash-covered at item level | `EV-010` |
| Analytic attribution | `ACCOUNTING FACT` (intent) | the item's distribution | the expanded subledger is `DERIVED` and destructible | `EV-012` |
| Analytic lines | `DERIVED FACT` | regenerated from the distribution | deleted on un-post | `EV-012` |
| Tax base / tax amount | `ACCOUNTING FACT` | the tax engine at posting | outside hash coverage; semantics are Wave D | `COR-06` |
| Entry number | `ACCOUNTING FACT` | the numbering mechanism | derived from existing data, not from a counter | `EV-005` |
| Posting status | `CONTROL FACT` | the ledger | three states plus a permanent "has been posted" marker | `EV-011` |
| **Entry is balanced** | `CONTROL FACT` | **application code, switchable off** | no database constraint; four lesser item rules *are* DB constraints | `COR-07` |
| Residual (both currencies) | `DERIVED FACT` | recomputed from matching records | **stored**, therefore capable of drift | `EV-014` |
| Reconciliation state | `DERIVED FACT` | matching records | stored | `EV-014` |
| Matching record | `ACCOUNTING FACT` | the settlement | **unconstrained against the item it matches** | `COR-09` |
| Settlement / payment state | `DERIVED FACT` | residuals | a presentation summary | `EV-014` |
| Ageing placement | `DERIVED FACT` | the maximum matched date | | `EV-014` |
| Journal | `CONTROL FACT` | configuration | selects lock, numbering, defaults | `EV-008` |
| Account classification identity | `CONTROL FACT` | configuration | the record, never the code | `EV-001` |
| Account code | `REPORTING FACT` | configuration, **per company** | a label resolved in context | `EV-001` |
| Account type | `CONTROL FACT` | configuration | changes reporting behaviour **retroactively** | `EV-016` |
| Closing period | `CONTROL FACT` | governance | a bare date; **no period object** | `EV-016`, `COR-01` |
| Fiscal year definition | `CONTROL FACT` | configuration | an optional, fully mutable calendar override | `COR-01` |
| Current-year earnings | `REPORTING FACT` | **computed at report time** | never posted, never stored | `EV-016` |
| Opening balance | `ACCOUNTING FACT` | an ordinary posted entry | with **no provenance carrier** | `EV-017` |
| Source document reference | `SOURCE FACT` | the producer | no general carrier; mutable metadata where present | `GAP-B02` |
| Accounting event identity | — | **no owner — does not exist** | the root cause of `XM-01` duplicate exposure | `GAP-B02` |
| Provenance / lineage | — | **no owner — does not exist** | | `EV-017`, `GAP-B02` |

## Contested ownership — resolved

Three facts appear to have two owners. Each resolves to one:

| Apparent conflict | Resolution | Basis |
|---|---|---|
| Accounting date — user or system? | **System.** The user owns only the document date. | `COR-02`: three independent mechanisms move it, one of which needs no lock |
| Amount — balance or debit/credit? | **Balance.** Debit and credit are a presentation split. | `EV-013`; the write path collapses debit/credit into balance |
| Reconciliation — state or event? | **Both, and the distinction is real.** The matching *record* is the fact; residual and payment state are derived from it; and it *emits* further events. | `EV-014` |

## The two facts with no owner

`GAP-B02` — **accounting event identity** and **provenance** have no carrier anywhere in the
evidence. They are not weakly implemented; they are absent. Together they account for:
duplicate-posting exposure (`XM-01`), the collapse of "correct the event" into "edit the entry"
(`EV-012`), the loss of migration lineage (`EV-017`), and the impossibility of asking what a posting
originally referred to after a merge (`COR-08`).

`RECOMMENDATION:` supplying these two owners is the highest-leverage single change SMEsPlus can make
relative to the reference model. Boss decision required.
