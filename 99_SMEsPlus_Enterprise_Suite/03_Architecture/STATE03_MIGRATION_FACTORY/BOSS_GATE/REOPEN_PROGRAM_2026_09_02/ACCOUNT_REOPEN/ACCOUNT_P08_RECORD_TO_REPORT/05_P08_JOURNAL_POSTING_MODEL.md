# P08_JOURNAL_POSTING_MODEL — Posting engine semantics

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · Layer 1 · evidence in `LAYER2_EVIDENCE_QUARANTINE/E01_POSTING_KERNEL.md`

## 1. The entry lifecycle in the benchmark

| ID | Statement | Class |
|---|---|---|
| `JPM-01` | Three states only: unposted, posted, voided. Voiding is a label on the entry, not a reversing entry. There is no submitted-for-approval state. | FACT VERIFIED |
| `JPM-02` | **Posting has two doors and only one of them validates.** The documented posting action runs a twelve-check battery. A generic field update that merely sets the status attribute runs only the lock-date checks, the balance check and the seal. An entry with **no lines at all** can reach the posted state through the second door. | FACT VERIFIED for the code paths; SUPPORTED INTERPRETATION for reachability |
| `JPM-03` | Creating an entry already in the posted state is refused. | FACT VERIFIED — a positive control |
| `JPM-04` | Posting silently **relocates the accounting date** when the requested date falls in a locked period. The originally requested date is retained nowhere. | FACT VERIFIED |
| `JPM-05` | Returning a posted entry to unposted is an ordinary user action. It is refused only for system-generated difference entries, cash-basis tax entries, and sealed entries. | FACT VERIFIED |
| `JPM-06` | That return **silently destroys** the entry's cost-allocation lines and removes every settlement match it participated in, with no confirmation and no ledger record of what was removed. | FACT VERIFIED |

## 2. Balance — the defining invariant, and its actual standing

`JPM-07` — **Balance is enforced in application code only.** The assertion is a query executed around create, update and delete: it groups by entry and rejects a non-zero sum. `FACT VERIFIED`.

`JPM-08` — **It is asserted in the reporting currency only.** The transaction-currency legs of an entry are never summed. An entry balanced in the reporting currency and unbalanced in its transaction currency passes. `FACT VERIFIED`.

`JPM-09` — **It is suppressible by a request parameter.** The assertion reads a plain key from the calling context; supplying that key with the suppressing value returns from the check without validating. Product code itself uses this in the point-of-sale close path. `FACT VERIFIED`.

`JPM-10` — **The parameter is caller-supplied and unfiltered.** The framework's remote-call entry point pops the caller's context dictionary and applies it wholesale to the object being acted on; no allowlist, denylist, key validation or type check was found at the dispatch layer. `FACT VERIFIED` for the dispatch mechanism; the negative on filtering is `B NOT FOUND IN SEARCHED SCOPE` — scope: the framework's call entry point, its model-service layer, and its HTTP layer.

`JPM-11` — **No database constraint enforces per-entry balance.** `A VERIFIED ABSENCE`, scope = the declared constraints and table-initialisation routines of the entry and item models. Database-level constraints that *do* exist: a unique index on (entry number, book) restricted to posted, non-placeholder entries; a check that debit and credit are not both non-zero on one item; and a check that the reporting-currency and transaction-currency amounts agree in sign.

**Consequence.** The defining invariant of double-entry bookkeeping is the *weakest* control in the kernel, while four lesser per-item rules are genuine database constraints. This inversion was reported in prior Wave A work; P08 reproduces it independently and adds the dispatch-layer evidence that makes the suppression caller-reachable rather than merely internal.

## 3. Immutability after posting

`JPM-12` — Posting protects **nine** header attributes: the line collection, both dates, the counterparty, the payment terms, the currency, the tax-treatment profile and the rounding profile. `FACT VERIFIED`.

`JPM-13` — That protection is itself waived by a caller-supplied context key, used at seven places in product code. `FACT VERIFIED`.

`JPM-14` — Attributes **not** protected include the entry number, the external reference and the narrative. On the item side, only tax attributes are unconditionally frozen; account, amount, counterparty and label remain writable on a posted item whenever the period is open and the item is unmatched. `FACT VERIFIED`.

`JPM-15` — **Items can be added to a posted entry.** The deletion path checks the parent's posted state; the creation path does not. Adding balanced pairs to an already-posted entry is not refused, and the period check on that path fires only for items that would move a tax return. `FACT VERIFIED`.

`JPM-16` — **A journal item's parent entry is mutable.** A link command on the entry's item collection re-parents an existing item from one entry to another; both entries are added to the balance container, so the operation succeeds whenever both remain balanced. `FACT VERIFIED`.

## 4. The seal

`JPM-17` — Tamper-evident sealing is **opt-in per book** and is not a property of posting. Until a book is configured for it, nothing is sealed. `FACT VERIFIED`.

`JPM-18` — The sealed attribute set is narrow and explicitly declared: at entry level the number, date, book and company; at item level the label, debit, credit, account and counterparty. **Not sealed:** the transaction currency and its amount, tax codes, cost allocation, document type, external reference, maturity date, the settlement links, and the status attribute itself. `A VERIFIED ABSENCE` scoped to the two attribute-set definitions.

`JPM-19` — **The sealed attribute set is selected by a caller-supplied version key.** Both the entry-level and item-level definitions read a version value from the calling context and return a smaller set for the older version — a set from which the entry number is absent. `FACT VERIFIED` for the mechanism; the exploitability statement is `SUPPORTED INTERPRETATION`, as no runtime reproduction was performed.

`JPM-20` — **The chain is ordered by an editable, gap-prone key.** The design once carried an independent gapless counter for this purpose; the attribute still exists in the schema and **nothing writes to it** (`A VERIFIED ABSENCE`, scope = both the primary and the archived module trees, that exact symbol). Chain ordering therefore falls back on the user-visible, administratively re-assignable entry number.

`JPM-21` — **The integrity report verifies content, not completeness.** It walks only records that already carry a seal. An entry never sealed, or a sealed entry removed from the tail of a chain, leaves the remainder internally consistent and is reported as verified. `FACT VERIFIED`.

## 5. Numbering

`JPM-22` — Numbers are allocated at posting, not at creation, from a per-book, per-period series. `FACT VERIFIED`.
`JPM-23` — Uniqueness is a **partial** database index covering only posted, numbered entries; duplicates among unposted or voided entries are permitted, and the concurrency lock that guarantees cross-session uniqueness is documented as ineffective for rows not yet posted. `FACT VERIFIED`.
`JPM-24` — Gaps arise from unposted entries that consumed a number, from voided entries, and from deletions. They are detected and warned about; **no operation is ever refused because of one**, and gap detection is truncated at the period-lock date, so gaps in closed periods are invisible. `FACT VERIFIED`.
`JPM-25` — **Numbers can be re-assigned after posting** by an administrative tool that renumbers a selection in one book. Its only seal-related safeguard blocks date-based reordering on sealed books; sequence-preserving renumbering is permitted, and during the operation the affected rows leave the uniqueness index entirely. `FACT VERIFIED`.

## 6. Deletion

`JPM-26` — Three independent guards exist and each has a defeat: the chain guard is waived for any administrator, for any company in simplified-entry mode, and by a caller-supplied key; the retention guard depends on a company setting that is **off by default** and is waived by the same key; the seal guard applies only where sealing was enabled. `FACT VERIFIED`.
`JPM-27` — On a default configuration a posted entry that happens to be last in its number chain is deletable by an ordinary billing user. `SUPPORTED INTERPRETATION`, built on `JPM-26` and the permission finding below.
`JPM-28` — The evidence of a forced deletion is a **server log line**, not a database record. `FACT VERIFIED`.
`JPM-29` — The item-to-entry and item-to-account references both carry database-level cascade deletion; the application guard protecting an account with postings is declared not to apply during module removal. `FACT VERIFIED`; the cascade consequence is `SUPPORTED INTERPRETATION`.

## 7. Authorisation

`JPM-30` — The permission table grants full create, update and delete on both the entry and the item to the **billing** role, and read-only rows to the **administrator** role; the administrator obtains write only by inheriting billing. Visibility rules for both are unrestricted. `FACT VERIFIED`.
`JPM-31` — **Superuser authorship of ledger entries is routine.** Thirteen subsystem integrations create entries or items with the permission layer switched off, and two post them with the posting-rights assertion switched off. `FACT VERIFIED`.
`JPM-32` — **The review flag is self-certifying.** The attribute marking an entry as reviewed is set by the posting operation itself from a per-book default that is enabled out of the box. No second identity is involved or recorded, and no maker-checker construct exists in the entry lifecycle. `A VERIFIED ABSENCE` for maker-checker, scope = the entry's state vocabulary and its declared constraint set.
`JPM-33` — Two unattended posting channels exist: a scheduled job that posts flagged unposted entries under an install-time superuser identity, and a supplier-invoice path that creates *and posts* from an inbound attachment or e-mail when a company setting (on by default) and a per-counterparty setting agree. `FACT VERIFIED`.

## 8. Requirements raised

| ID | Candidate requirement |
|---|---|
| `P08-RQ-JPM-01` | Balance is a persistence-layer invariant. No request parameter may switch off an accounting invariant. |
| `P08-RQ-JPM-02` | Balance is asserted in every currency frame the entry uses, not only the reporting currency. |
| `P08-RQ-JPM-03` | Posting has exactly one door. No generic attribute write may move an entry into the posted state. |
| `P08-RQ-JPM-04` | A posted entry is immutable in all attributes, with no context-supplied waiver. Correction is by new fact only. |
| `P08-RQ-JPM-05` | An item's parent entry is fixed at creation and can never be re-pointed. |
| `P08-RQ-JPM-06` | Sealing is not opt-in, its attribute set is not caller-selectable, and its chain is ordered by an internal gapless counter that no user can see or change. |
| `P08-RQ-JPM-07` | A posted entry is never deleted. Retention is a platform or tenant policy, not a company setting, and not defeasible by a request parameter. |
| `P08-RQ-JPM-08` | The date the ledger records is the date the user intended, or the posting is refused. Silent relocation is prohibited. |
| `P08-RQ-JPM-09` | Authoring and posting are distinct authorisations held by distinct identities, and the reviewed marker is set by the reviewer, never by the poster's own action. |
| `P08-RQ-JPM-10` | Every unattended posting channel names the authority under which it posts, and that authority is a real, revocable identity — not an install-time superuser. |
