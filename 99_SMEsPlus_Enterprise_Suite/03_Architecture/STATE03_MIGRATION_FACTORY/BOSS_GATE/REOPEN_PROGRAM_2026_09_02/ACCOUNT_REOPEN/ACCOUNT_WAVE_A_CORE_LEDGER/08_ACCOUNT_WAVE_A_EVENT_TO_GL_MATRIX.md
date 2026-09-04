> **CORR1 CORRECTION NOTICE.** Amended by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`.
> Corrections landing here: `COR-14`. Governing text where they conflict with the body below: CORR1/C06.
> Prior findings are retained unedited for lineage; see `CORR1/C02_..._ACCEPTED_CORRECTIONS_REGISTER.md`.

# 08 — ACCOUNT_WAVE_A_EVENT_TO_GL_MATRIX

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

> **Evidence discipline notice — read before using this matrix.**
> Wave A researched the **core ledger mechanism**: how an entry comes into existence, how it is
> numbered, dated, locked, secured, matched and reported. It did **not** research the posting
> patterns of the producing modules — Sales, Purchase, Inventory, Assets, Payroll and Tax each own
> their own recognition rules and their own Wave.
>
> Accordingly, **debit and credit are marked `UNKNOWN — EVIDENCE REQUIRED` for every event whose
> posting pattern was not read from primary source this session.** They are not inferred from
> general ERP knowledge. Filling them from convention would convert inference into apparent fact,
> which this project's evidence standard forbids, and would pre-empt the owning Wave's gate.
>
> The columns that *are* populated everywhere — recognition trigger, journal, currency, reconciliation,
> close impact, reversal, correction — are the columns Wave A actually owns.

Legend: `UNK` = `UNKNOWN — EVIDENCE REQUIRED`, with the owning Wave named.

---

## Part 1 — Events whose ledger effect Wave A verified

### `M-01` Opening position established

| Column | Value |
|---|---|
| Source | migration or company setup |
| Business event | the business begins keeping books in this system at a stated position |
| Recognition trigger | the opening entry is created and posted |
| Accounting event | `AE-14` |
| Journal | a nominated opening journal |
| **Debit** | per-account opening debit, written through computed fields on the account |
| **Credit** | per-account opening credit, **balanced to the current-year-earnings account** |
| Currency | company currency; per-item transaction currency where applicable |
| Partner | `UNK` — whether open items carry counterparties at migration is a Level 10 requirement, not an observed behaviour |
| Analytic | `UNK` |
| Tax | not applicable — an opening position carries no tax event |
| Reconciliation | migrated open items must be individually reconcilable, or subsequent settlement cannot match them |
| Reporting | establishes every account's starting balance |
| Close impact | subject to lock like any entry |
| Reversal | ordinary reversal |
| Correction | ordinary — including deletion where the audit-trail flag is off |
| Evidence | `EV-017`, `EV-011` |

### `M-02` Exchange difference on settlement

| Column | Value |
|---|---|
| Source | the reconciliation itself |
| Business event | an obligation is settled at a measurement different from the one it was recorded at |
| Recognition trigger | a partial or full match where the two sides' measurement differs |
| Accounting event | `AE-11` — **emitted by the ledger, not requested by a user** |
| Journal | the company's nominated exchange journal |
| **Debit / Credit** | the difference between the matched amounts, computed from the three amounts the matching record carries (company currency, and each side's transaction currency). The **account** used is configuration, and the specific gain/loss account selection was `UNK` at the scope read |
| Currency | company currency; the difference exists only there |
| Partner | inherited from the matched items |
| Analytic | `UNK` |
| Tax | none |
| Reconciliation | the exchange entry is itself matched so the counterparty account shows no residue |
| Reporting | FX gain or loss |
| Close impact | **if its natural date is locked, the entry is re-dated** |
| Reversal | **automatic** — removing the match reverses it, emitting `AE-12` |
| Correction | by unmatching and rematching |
| Evidence | `EV-014`, `EV-015` |

### `M-03` Cash-basis tax recognised on settlement

| Column | Value |
|---|---|
| Source | the reconciliation |
| Business event | tax on a document becomes reportable because the document was settled |
| Recognition trigger | a match against a document carrying cash-basis tax |
| Accounting event | `AE-13` — emitted by the ledger |
| Journal | the company's nominated cash-basis journal |
| **Debit / Credit** | a proportional mirror of the original document's tax lines, scaled by the matched percentage. Exact account pairs are `UNK` — `WAVE-D TAX` |
| Currency | the original document's currency, scaled by the matched proportion |
| Partner | inherited |
| Analytic | `UNK` |
| Tax | **this event exists solely to move tax between reportable states** |
| Reconciliation | not itself reconciled |
| Reporting | tax return |
| Close impact | **dated today when its natural period is locked — it can cross a fiscal year boundary** |
| Reversal | the generated entries can be reversed but **cannot be reset to draft** |
| Correction | by reversal only |
| Evidence | `EV-015`, `EV-012` |

### `M-04` Entry reversed

| Column | Value |
|---|---|
| Source | user, or an automatic consequence |
| Business event | a recorded fact is withdrawn |
| Recognition trigger | the reversal action |
| Accounting event | `AE-06` |
| Journal | the original's journal by default |
| **Debit / Credit** | an exact mirror of the original — this is the one posting pattern Wave A can state without qualification, because it is defined by the original, not by a rule |
| Currency | mirrors the original |
| Partner | mirrors |
| Analytic | mirrors the original's distribution |
| Tax | mirrors |
| Reconciliation | where the reversal cancels the original, the two are **auto-matched on posting** |
| Reporting | net effect zero across the two entries |
| Close impact | **the reversal is re-dated into the first open period if the original's period is locked** — so the reversal and the original can sit in different periods, and different years |
| Reversal | reversible |
| Correction | this *is* the non-destructive correction path |
| Evidence | `EV-012`, `EV-009`, `COR-02` |

### `M-05` Period made final

| Column | Value |
|---|---|
| Source | governance |
| Business event | a period is declared no longer open |
| Recognition trigger | a lock date moved forward |
| Accounting event | `AE-15` |
| Journal / Debit / Credit / Currency / Partner / Analytic / Tax | **NOT APPLICABLE** — closing posts nothing. This is the finding, not a gap: the reference model has no closing entry (`EV-016`) |
| Reconciliation | bank reconciliation completeness is a **precondition**, and draft entries block a hard lock |
| Reporting | the year's result is computed at report time against the current-year-earnings account |
| Close impact | subsequent postings for the range are re-dated |
| Reversal | soft locks move back freely; the hard lock never does |
| Correction | not applicable |
| Evidence | `EV-008`, `EV-016`, `EV-019`, `COR-01` |

---

## Part 2 — Producer events: ledger interface verified, posting pattern not researched

For every row below the ledger-side columns are Wave A findings; the debit/credit columns are
explicitly withheld.

| Event | Recognition trigger | Journal | Debit | Credit | Currency | Reconciliation | Close impact | Reversal / correction | Owning Wave |
|---|---|---|---|---|---|---|---|---|---|
| Customer invoice | document validation | sale | `UNK` | `UNK` | transaction currency required on every item | receivable item is an open item | **sale lock applies**; re-dating capped at today | reverse; credit note | `WAVE-B AR` |
| Customer credit note | document validation | sale | `UNK` | `UNK` | as above | auto-matched where it cancels | sale lock | reverse | `WAVE-B AR` |
| Vendor bill | document validation | purchase | `UNK` | `UNK` | as above | payable item is an open item | **purchase lock applies; and the accounting date is moved to the end of the document's month even with no lock configured** | reverse; debit note | `WAVE-C AP` |
| Vendor credit note | document validation | purchase | `UNK` | `UNK` | as above | auto-matched where it cancels | as above | reverse | `WAVE-C AP` |
| Customer payment received | payment registration | bank or cash | `UNK` | `UNK` | as above | **matched against the open receivable — emits `M-02` where measurement moved** | ordinary | reverse; unmatch | `WAVE-H BANKING` |
| Vendor payment made | payment registration | bank or cash | `UNK` | `UNK` | as above | matched against the open payable | ordinary | reverse; unmatch | `WAVE-H BANKING` |
| Bank statement line matched | matching | bank | `UNK` | `UNK` | as above | may clear through a suspense account | **unreconciled lines block period locking** | unmatch | `WAVE-H BANKING` |
| Tax return posted | return closing | a tax journal | `UNK` | `UNK` | company currency | not reconciled | **sets the tax lock date automatically**; reset-to-draft is restricted where carryover exists | restricted | `WAVE-D TAX` |
| Inventory receipt / issue / valuation | receipt, issue or valuation run | inventory | `UNK` | `UNK` | as above | not open items | ordinary | reverse | Inventory — `PRIOR`: v2.0 `HELD` |
| Cost of sales recognised | delivery or period cost run | inventory or general | `UNK` | `UNK` | as above | not open items | ordinary | reverse | Inventory — `PRIOR`: `PARTIAL RESOLUTION`, three questions `NOT DECIDABLE` |
| Depreciation charge | period run | general or a nominated asset journal | `UNK` | `UNK` | company currency | not open items | ordinary | reverse | Asset — `PRIOR`: terminal state B |
| Asset disposal | disposal event | general | `UNK` | `UNK` | as above | not open items | ordinary | reverse | Asset — `PRIOR` |
| Production order completion | completion | inventory | `UNK` | `UNK` | as above | not open items | ordinary | reverse | Manufacturing — `PRIOR`: links 2–6 exist; rate derivation and the equipment dimension missing |
| Employee expense approved | approval | purchase | `UNK` | `UNK` | as above | payable item | purchase lock | reverse | `WAVE-C AP` |
| Deferred revenue / cost release | period run | general | `UNK` | `UNK` | as above | not open items | ordinary | reverse | `WAVE-F` |

---

## What this matrix establishes

1. **Three accounting events are emitted by the ledger itself** (`M-02`, `M-03`, and the reversal
   half of `M-04`). Two of the three can be **attributed to a period other than the one the
   underlying event belongs to** when that period is locked. This is a Wave A finding with
   consequences in Waves D, G and H.
2. **The only event with no debit and credit at all is period close** — because it posts nothing.
   Marked `NOT APPLICABLE` with reason, as required, rather than left blank.
3. **Fourteen producer events have a verified ledger interface and an unresearched posting pattern.**
   That is the correct state at the end of Wave A. Populating those cells is each owning Wave's work,
   and Wave A must not pre-empt it.
4. The columns Wave A *can* complete for every row — recognition trigger, journal selection, currency
   handling, reconciliation participation, close impact, correction route — are precisely the ledger
   contract each producing Wave will have to satisfy.

`RECOMMENDATION:` when each later Wave completes its own posting patterns, this matrix should be the
place they are recorded, so that the ledger-side constraints established here travel with them.
