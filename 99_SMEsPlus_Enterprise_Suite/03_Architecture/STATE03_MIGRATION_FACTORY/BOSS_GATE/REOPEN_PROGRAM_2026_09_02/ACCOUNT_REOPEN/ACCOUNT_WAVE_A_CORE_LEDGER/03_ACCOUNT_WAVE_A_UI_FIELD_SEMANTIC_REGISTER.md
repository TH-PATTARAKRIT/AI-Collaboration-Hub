# 03 — LEVEL 2: UI / FIELD / CONFIGURATION FORENSIC — SEMANTIC REGISTER

Layer 1 clean-room · cites `EV-0NN` · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

This is **not** a field inventory. Each row states what the field *means*, what it *does to the
ledger*, and who *owns* it. Fields with no accounting consequence are excluded deliberately —
listing them would inflate the register without adding semantic coverage.

Column key — `Der.` derivation: `S` stored input · `D` derived/computed · `SD` stored-computed
(derived but persisted, therefore capable of drifting from its inputs) · `C` configuration.

## A — Account fields

| Field | Meaning | Accounting consequence | Req. | Der. | Editable | Depends on | Upstream owner | Downstream consumer | Hidden behaviour |
|---|---|---|---|---|---|---|---|---|---|
| Account identity | The account as a thing | none directly; anchors every posting | yes | S | never | — | ledger | every item, every report | The identity is the record, not the code (`EV-001`) |
| Code | Per-company label and sort key | none; orders reports | yes per company | SD | yes | acting company | company configuration | reports, mappings, imports | Resolves differently per company; two companies legitimately see different codes for one account (`EV-001`) |
| Name | Human label | none | yes | S | yes | — | configuration | reports | Translatable; not identity |
| Account type | Classification driving behaviour | selects balance-forward, forces reconcilability on receivable/payable, nominates the single current-year-earnings account | yes | SD | yes | usage | configuration | close, reports, subledger linkage | Cannot be changed to receivable/payable once used as a sale/purchase journal default, or as a journal bank account (`EV-019`) |
| Internal group | Coarse classification | reporting grouping | — | D | no | account type | derived | reports | Purely derived — not an independent fact (`EV-016`) |
| Bring balance forward | Whether the account carries across the year boundary | separates permanent from temporary accounts, and is the entire mechanism by which the year boundary exists | — | D | no | account type | derived | close, reports | This derived flag is what "year end" actually means in the reference model (`EV-016`) |
| Allow reconciliation | Whether items may be matched | enables open-item management and residual | — | SD | yes | account type | configuration | reconciliation, ageing | Forced true for receivable/payable; turning it off is refused while the account is a payment debit/credit account (`EV-019`) |
| Account currency | Forces every item to one currency | constrains posting | no | S | conditionally | existing items | configuration | posting, journal | Refused if items already exist in another currency; must match the journal currency (`EV-019`) |
| Companies | Which companies may use this account | governs sharing and consolidation | yes ≥1 | S | yes | posted items | configuration | posting, reports | Liquidity accounts cannot be shared; a company cannot be detached while its items reference the account (`EV-019`) |
| Deprecated | "No longer to be chosen" | **none** — does not stop posting through configuration paths | no | S | yes | tax use | configuration | pickers | Filters selection lists only. Whether it blocks programmatic posting is `UNKNOWN — EVIDENCE REQUIRED` (`EV-003`) |
| Tags | Free custom reporting dimension | none | no | SD | yes | — | configuration | custom reports | No control semantics found |
| Allowed journals | Restricts where the account may be used | admission control on posting | no | S | yes | — | configuration | posting | An account-side restriction; there is no symmetric journal-side account whitelist |
| Opening debit / credit / balance | The account's migrated starting position | writes into a single ordinary posted entry | no | D | yes | opening entry | migration | reports | Editing this field edits a posted journal entry indirectly (`EV-017`) |
| Non-trade | Splits trade from non-trade receivable/payable | reporting and filtering | no | S | yes | — | configuration | reports | |

## B — Journal fields

| Field | Meaning | Accounting consequence | Req. | Der. | Editable | Depends on | Upstream owner | Downstream consumer | Hidden behaviour |
|---|---|---|---|---|---|---|---|---|---|
| Type | The journal's role | selects which lock date applies to its entries, which default account is auto-created, and sequence behaviour | yes | S | yes | — | configuration | posting, lock resolution | Sale and purchase types pull in their own lock dates on top of the global lock (`EV-008`) |
| Code | Short label, feeds the number prefix | shapes the number series | yes | S | yes | — | configuration | numbering | Because numbering is derived from existing data, changing the code mid-period does not re-base the series (`EV-005`) |
| Company | Sole owning company | scopes every entry, and transitively scopes number uniqueness | yes | S | no | — | configuration | everything | Exactly one — unlike accounts (`EV-006`) |
| Active | Archive flag | archived journals cannot receive new entries | — | S | yes | — | configuration | posting | The journal has this; the account does not (`EV-003`) |
| Default account | Counterpart account for this journal | determines the automatic side of generated entries | conditional | S | yes | type | configuration | posting | Auto-created at journal creation when absent (`EV-019`) |
| Suspense account | Interim holding for unidentified movement | parks value pending classification | conditional | D | yes | journal, then company | configuration | bank flow | Falls back to a company default; an ordinary account wearing a role (`EV-014`) |
| Secure posted entries with hash | Turns on chained integrity hashing for this journal | makes posted entries in this journal tamper-evident **for hashed fields only** | no | S | one-way | existing hashed entries | configuration | integrity | Default off. Once entries are hashed it cannot be switched off. Coverage is partial — see `CONTRA-01` (`EV-010`, `EV-011`) |
| Sequence override pattern | Overrides how the system parses the number | changes the numbering series interpretation | no | C | yes | — | configuration | numbering | A free-text pattern altering a core control — high blast radius (`EV-005`) |
| Currency | The journal's operating currency | must equal the default account's currency | no | S | yes | default account | configuration | posting | (`EV-019`) |

## C — Entry fields

| Field | Meaning | Accounting consequence | Req. | Der. | Editable | Depends on | Upstream owner | Downstream consumer | Hidden behaviour |
|---|---|---|---|---|---|---|---|---|---|
| State | Draft / posted / cancelled | posted asserts the accounting event | yes | S | via actions | guards | ledger | everything | Three states are not the real state space — see file 10 |
| Posted-before flag | Has this entry ever been posted | gates deletion protection and journal changes | — | S | no | history | ledger | audit trail | An entry reset to draft still carries this; it is the real carrier of "this once existed as fact" (`EV-011`) |
| Number / name | The entry's identifier in its series | uniqueness asserted only at posting | at post | SD | conditionally | journal, date | numbering | audit, reports | Duplicates are possible while draft (`EV-006`) |
| Accounting date | The period the entry belongs to | determines period, lock, reporting | yes | SD | while draft | lock dates | **the lock mechanism, not the user** | everything | **Silently rewritten to lock date + 1 when it falls in a locked period** (`EV-009`) — the single most consequential hidden behaviour in Wave A |
| Document date | The date on the source document | none directly | conditional | S | while draft | — | source document | reports, tax | Diverges from accounting date under lock, by design (`EV-009`) |
| Journal | The numbering and control domain | selects lock, sequence, defaults | yes | S | tightly guarded | number assigned | configuration | everything | Cannot be changed once a number is consumed unless the number is cleared (`EV-022`) |
| Integrity hash | Chained tamper-evidence marker | makes hashed fields unwritable | — | SD | never | journal setting | integrity | audit | Covers `[number, date, journal, company]` plus item `[label, debit, credit, account, partner]` **only** (`EV-010`) |
| Secured | Whether a hash exists | presentation of the above | — | D | no | hash | derived | audit | "Secured" overstates the coverage (`EV-010`) |
| Auto-post | Defer posting to a future date | delays the accounting event | no | S | yes | date | user | posting | Future-dated entries are held rather than posted under soft posting |
| Reference / narration | Descriptive metadata | none | no | S | **yes, even when posted** | — | user | reports | Not frozen by the posted guard and not hash-covered (`EV-022`) |
| Reversed-entry link | Points at the entry this reverses | establishes correction lineage | — | S | no | reversal | ledger | audit | Reversals of posted originals are auto-matched on posting (`EV-012`) |
| Payment state | Derived settlement summary | none | — | SD | no | reconciliation | derived | reports | A derived summary of item residuals, not an independent fact (`EV-014`) |

## D — Item fields

| Field | Meaning | Accounting consequence | Req. | Der. | Editable | Upstream owner | Hidden behaviour |
|---|---|---|---|---|---|---|---|
| Balance | Signed company-currency amount | **the primary posted amount** | yes | SD writable | while draft | ledger | Debit and credit are derived from this, not the reverse (`EV-013`) |
| Debit / Credit | Presentation split of balance | none independently | — | SD | via inverse | derived | Hash-covered; balance itself is not named in the hash, but is reconstructible from the pair |
| Currency | Transaction currency | qualifies the amount in currency | **yes, always** | SD | while draft | ledger | Always present even when equal to company currency (`EV-013`); **not hash-covered** (`EV-010`) |
| Amount in currency | The transaction-currency amount | the amount actually agreed | yes | SD | while draft | ledger | **Not hash-covered and not blocked by the posted-entry guard on a hashed entry** — `CONTRA-01` |
| Account | Classification of this amount | the posting target | yes | SD | while draft | ledger | Retargeted silently by an account merge (`EV-004`) |
| Partner | Counterparty | subledger attribution | no | SD | while draft | ledger | Hash-covered at item level |
| Due date | Maturity | drives ageing | no | S | while draft | payment terms | Not hash-covered (`EV-010`) |
| Analytic distribution | Management-accounting attribution | generates the analytic subledger | no | S | while draft | user/config | **The generated subledger is deleted on un-post and regenerated on repost** (`EV-012`) — it is derived, not a fact |
| Tax fields | Tax dimension | drives tax reporting | no | SD | while draft | tax engine | Not hash-covered (`EV-010`); semantics are Wave D |
| Residual (company) | Unsettled company-currency amount | drives payment state and ageing | — | SD | no | reconciliation | Stored-computed — capable of drifting from its inputs if recomputation is missed |
| Residual (currency) | Unsettled transaction-currency amount | as above, per currency | — | SD | no | reconciliation | |
| Reconciled | Fully settled marker | derived | — | SD | no | reconciliation | |
| Matching marker | `P` while partial, else the full-match name | operational reference | — | S | no | reconciliation | An indexed text marker, not a relation (`EV-014`) |
| Full-match link | Points at the full reconciliation | settlement lineage | — | S | no | reconciliation | |

## E — Reconciliation record fields

| Field | Meaning | Accounting consequence |
|---|---|---|
| Debit item / credit item | The exactly-two items matched | defines the match; matching is pairwise, always |
| Amount (company currency) | Value matched, always positive | reduces both residuals |
| Amount (debit-side currency) / (credit-side currency) | Value matched in each side's own transaction currency | the pair of these is what makes exchange difference computable (`EV-014`) |
| Maximum match date | Latest date among matched items | **places the match on ageing reports**, and is the date a cash-basis tax entry inherits (`EV-015`) |
| Exchange entry link | The entry created to book the FX difference | reversed when the match is undone (`EV-014`) |
| Full-match link | Aggregation once residual reaches zero | owns the exchange entry at full-match level |

## F / G — Company-level close configuration

| Field | Meaning | Accounting consequence | Reversible | Hidden behaviour |
|---|---|---|---|---|
| Global lock date | The general accounting lock | entries on or before it are re-dated forward | yes, freely | Re-dates rather than rejects (`EV-009`) |
| Tax return lock date | Locks tax-affecting entries | as above, for entries carrying tax | yes | Set automatically when a tax return is posted |
| Sales lock date | Locks sale-journal entries | as above, for sale journals | yes | Applies only via journal type (`EV-008`) |
| Purchase lock date | Locks purchase-journal entries | as above | yes | |
| **Hard lock date** | Irreversible lock | as above, with no exception possible | **no — may only move forward** | Cascades: a company's effective hard lock is the maximum across its parent chain (`EV-008`). Refused while draft entries remain in the period |
| Fiscal year last day / month | Two integers defining the year end | derives period boundaries on demand | yes | **This is the entire fiscal-year model — there is no year entity** (`EV-016`) |
| Audit trail flag | Blocks deletion of once-posted entries | makes deletion an error rather than an operation | yes | Bypassable by context; the bypass records the deletion **outside the database** (`EV-011`) |
| Opening entry link | Points at the migrated starting position | defines "accounting is initialised" | — | An ordinary posted entry (`EV-017`) |
| Current-year-earnings account | Where the year's result is presented | **presentation only — nothing is posted to it by a close** (`EV-016`) | — | Exactly one per company is enforced; created on demand |

## Configuration parameters with ledger consequence

| Parameter | What it does | Risk |
|---|---|---|
| Number/date alignment start date | Skips the control that a number's encoded period must match the entry's date, for all entries dated on or before it | Setting it forward disables a core numbering control tenant-wide, silently (`EV-007`) |
| Per-journal sequence override pattern | Redefines how numbers are parsed | Alters the series interpretation for a whole journal (`EV-005`) |
| Per-journal hashing flag | Turns integrity hashing on | Default **off**; partial coverage when on (`EV-010`, `EV-011`) |
| Per-company audit-trail flag | Turns deletion protection on | Default state must be established for SMEsPlus; bypass logs outside the database (`EV-011`) |

## CHECKPOINT L2

| Item | Record |
|---|---|
| Scope completed | Every field in scopes A–H carrying an accounting consequence, with meaning, ownership, derivation and hidden behaviour |
| Evidence inspected | `EV-001` through `EV-023` |
| Verified findings | Four fields carry behaviour a user cannot see at the moment it matters: accounting date (silent re-dating), analytic distribution (subledger destroyed on un-post), amount in currency (unprotected on a secured entry), deprecated flag (does not stop posting) |
| Contradictions | `CONTRA-01` raised here — the "Secured" label overstates hash coverage |
| Unknowns | Whether the deprecated flag blocks programmatic posting (`GAP-A04`) |
| Risks | Stored-computed fields (residual, reconciled, code) can drift from their inputs; SMEsPlus needs a reconstruction guarantee for each |
| Expert disagreements | Deferred to Level 12 |
| Audit challenges | Challenge unit tasked to falsify `CONTRA-01` specifically |
| Next research target | Level 3 — function forensic |

`CHECKPOINT L2 RECORDED — CONTINUING AUTOMATICALLY.` Not Boss approval.
