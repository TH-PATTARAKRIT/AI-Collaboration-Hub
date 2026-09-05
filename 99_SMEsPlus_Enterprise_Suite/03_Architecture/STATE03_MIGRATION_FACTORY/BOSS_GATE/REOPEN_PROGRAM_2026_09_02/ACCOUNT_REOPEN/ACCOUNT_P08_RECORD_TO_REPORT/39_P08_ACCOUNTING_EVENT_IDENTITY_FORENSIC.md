# P08_ACCOUNTING_EVENT_IDENTITY_FORENSIC

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · `CP-T05`

## 1. Retraction of a class-A claim published by this session

> **`RS-A-01` — "No accounting-event model exists", published at class `A VERIFIED ABSENCE` across 22 reference roots — is `CONTRADICTED` and is WITHDRAWN.**

An independent forensic pass, commissioned specifically to disprove it, produced counterexamples. The session author verified each against primary source before accepting the retraction.

| Counterexample | Verified |
|---|---|
| A bank statement line is a **persistent model** carrying a database `UNIQUE` constraint on an external import identifier — *"a bank account transaction can be imported only once"* | **yes, read directly** |
| That same model stands in an **ORM-enforced 1:1 delegation** with the journal entry: one statement line owns exactly one entry, created with it and cascade-deleted with it | **yes, read directly** |
| A payment transaction carries a database `UNIQUE` constraint on the provider's reference | **yes, read directly** |
| An electronic-invoicing document carries a database `UNIQUE` constraint on (format, entry) | reported, not independently re-read |

Two of these are exactly the function the withdrawn claim denied: **a durable, database-enforced identity for an accounting event, bound one-to-one to the resulting journal entry.**

## 2. Why the claim failed, and the method lesson that is larger than the claim

The supporting instrument was a **model-name census filtered on the token "event"**. None of the counterexamples is named "event". **The pattern could not match the thing it was asked to deny.**

This session had already added positive controls to every re-run pattern precisely to prevent this class of error — and `RS-A-01` **passed** its control. The control demonstrated that the pattern could find *models whose name contains "event"*. It did not demonstrate that the pattern could find *event identity*.

> **`P08-M-07` — A positive control must demonstrate that the pattern can match the thing being denied, not merely that the pattern produces output.** A control that tests the mechanism rather than the claim gives false assurance, and it gave it here.

This is the third distinct instance in this session of a negative failing because its instrument could not fire on its target — after the balance-constraint pattern that could not aggregate across rows, and the three shell-level false zeros the reviewing agent reported against its own work. The defect is systemic to pattern-based negatives, not incidental.

## 3. The corrected finding

**`P08-AEI-01` — Durable accounting-event identity exists where the event originates OUTSIDE the system, and is absent where it originates INSIDE it.** `FACT VERIFIED`.

| Origin class | Identity | Enforcement |
|---|---|---|
| Bank transaction imported from a file (two of the shipped formats) | external transaction identifier, composed with the bank account and the book | **database `UNIQUE`** |
| Payment-provider transaction | provider reference, feeding an idempotent state machine and a link guard | **database `UNIQUE`**, retry-idempotent |
| Electronic-invoicing dispatch | (format, entry) | **database `UNIQUE`** |
| Inventory valuation movement | a valuation record links to its entry | link only, **not enforced** |
| **Sales, purchase, expense, payroll, asset, point-of-sale, manual payment, reversal, manual journal** | **none** | **a state field on the source document, sometimes with an emptiness test on a link** |

**`P08-AEI-02` — For every internally-originated posting path, the only barrier to double posting is a state field, and it fails three ways.** `FACT VERIFIED`.

1. **Cancellation resets the balance.** The invoiced-quantity computation excludes cancelled entries, so cancel → re-invoice → return the cancelled one to draft → post yields two posted invoices for one delivery. The posting method performs no source-side check.
2. **Nothing is enforced at the database.** The single unique index on the entry table constrains the **sequence number** — and the numbering design *guarantees* two concurrent postings receive different numbers, so that index is structurally incapable of colliding on a duplicate. Of the 24 source-reference carriers on the entry, **not one is unique**.
3. **Nothing is locked.** No lock spans the create-and-post transition on any producing path. Two concurrent callers both read the pre-write state, both pass, and both post.

**`P08-AEI-03` — The tamper seal does not close this.** It covers the entry's number, date, book and company plus line content. **No provenance field is sealed.** A duplicate entry hashes exactly as validly as the original.

**`P08-AEI-04` — Duplicate detection on documents is detective and advisory.** It matches on a reference string, declines only to *auto*-post, and does not stop a user pressing Post.

## 4. The deployment finding that governs all of the above

The identity that does exist was tested against the deployed databases.

| Measurement, `DB-SM` | Value |
|---|---|
| Bank statement lines | **13,814** |
| Carrying an external import identifier | **0** |
| Carrying an online-feed transaction identifier | **0** |

`FACT VERIFIED`. **Every one of the 13,814 bank transactions in the production-scale database was created by a path that sets no deduplication key at all.** Because a database `UNIQUE` constraint permits unlimited empty values, the constraint admits all 13,814 rows without objection.

So the corrected position has two halves, and both matter:

- **In source:** durable, database-enforced event identity **exists** — my published claim was wrong.
- **In deployment:** it is populated on **zero** rows, so the protection it provides is **inoperative in this database**.

This is the fourth control in this session found to be present in source and unengaged in deployment, after the tamper seal (0 of 64 journals), the period lock (0 of 89 companies) and the retention feature (column absent). The pattern is now the dominant finding of the whole package:

> **The reference system's accounting controls are, in the deployed estate examined, overwhelmingly present and switched off.**

## 5. Final classification, per the directive's required vocabulary

> **ACCOUNTING EVENT IDENTITY: `CONFIGURATION OR MODULE DEPENDENT`.**

Not "no independent event identity verified" — that was the withdrawn claim. Identity exists, is database-enforced, and is bound 1:1 to the entry — **for externally-originated events, in some modules and some file formats only**, and it is **unpopulated in the deployed data examined**. For internally-originated events no identity exists at any layer.

## 6. Consequences for the rest of the package

| Artefact | Change |
|---|---|
| `01A` `RS-A-01` | **withdrawn**; the root-set class-A count falls from 17 to 16 |
| `03` kernel `K2` | **strengthened, not weakened.** The kernel still needs an accounting-event object — but it is no longer proposed into a vacuum. Two working patterns exist to adapt: a database-unique external key, and a unique key plus state machine plus link guard |
| `13`, `16`, `25`, `29` | the accounting-event absence is re-scoped to internally-originated events wherever it appears |
| `P08-BD-04` | sharpened: the question is no longer *whether* to have event identity but whether to extend the existing external-origin pattern to internal origins |
