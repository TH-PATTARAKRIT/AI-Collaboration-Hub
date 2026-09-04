# 07 — ACCOUNT_WAVE_A_ACCOUNTING_EVENT_REGISTER

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

An **accounting event** is an occurrence after which the ledger asserts something it did not assert
before. This register enumerates every such event found in Wave A, including the ones the reference
model emits **without a user asking for them** — those are the dangerous ones.

Column `Visible?` records whether the event is apparent to the operator at the moment it occurs.

| # | Accounting event | Triggered by | Emits | Visible? | Reversible | Evidence |
|---|---|---|---|---|---|---|
| `AE-01` | **Entry posted** | user, schedule, or producer | the entry becomes fact; number assigned; permanent posted marker set | yes | by un-post (destructive) or reversal (additive) | `EV-006`, `EV-011` |
| `AE-02` | **Entry re-dated on posting** | lock violated at posting | the accounting date moves to the end of the first open period | **only while draft** — the warning is hidden once posted | no — the original intent is not retained | `COR-02` |
| `AE-03` | **Entry re-dated on document-date change** | any edit of the document date on a non-sale document | accounting date moves to the end of the document's month | **no** | no | `COR-02` — *fires with no lock configured* |
| `AE-04` | **Entry re-dated on duplication or reversal** | copy or reverse of an entry dated in a locked period | new entry dated lock + 1 day | partially | n/a | `EV-009` |
| `AE-05` | **Entry un-posted** | user | fact retracted; **analytic lines deleted; matches removed** | the state change is; the destruction is **not** | no — the destroyed records do not return | `EV-012` |
| `AE-06` | **Entry reversed** | user, or automatically on unreconciliation or cancellation | a new, opposite entry; optionally auto-matched to the original | yes | by reversing the reversal | `EV-012` |
| `AE-07` | **Entry cancelled** | user | routes through un-posting first, therefore carries `AE-05`'s destruction | the cancellation is; the destruction is not | no | `EV-012` |
| `AE-08` | **Entry deleted** | user, where the audit-trail flag is off or bypassed | the fact ceases to exist | yes to the actor; **invisible afterwards** | no | `EV-011` |
| `AE-09` | **Entry hashed** | posting into a secure journal, or the on-demand secure action | the entry and its unhashed predecessors become tamper-evident for hashed fields only | yes — logged to the entry's thread | no — hashing cannot be undone | `EV-010`, `EV-011` |
| `AE-10` | **Items matched** | user, rule, payment registration, or posting of a reversal | settlement facts; residuals and payment state change | yes | by unmatching, which itself emits `AE-12` | `EV-014` |
| `AE-11` | **Exchange difference recognised** | a match where the two sides' measurement differs | **a new posted entry** | partially — it appears as a separate entry | by unmatching | `EV-014` |
| `AE-12` | **Match removed** | user | residuals restored; **the exchange entry is reversed by a new posted entry** | partially | by re-matching | `EV-014` |
| `AE-13` | **Cash-basis tax recognised** | a match on a document carrying cash-basis tax | **new posted entries**, dated **today** if their natural period is locked | **no** | the entries can be reversed | `EV-015` |
| `AE-14` | **Opening position established** | migration or company setup | an ordinary posted entry balanced to current-year earnings | yes | as any entry | `EV-017` |
| `AE-15` | **Period made final** | lock date moved forward | subsequent postings for that range are re-dated | yes | soft: freely reversed. hard: **never** | `EV-008` |
| `AE-16` | **Period reopened** | soft lock moved backward | that range accepts postings again | yes | yes | `EV-008` — no distinct authority required |
| `AE-17` | **Finality overridden for a user** | lock exception granted | the effective lock is lowered for the named scope | to the granter, and on the company thread | by revocation — **by the same role that granted it** | `EV-021`, `COR-04` |
| `AE-18` | **Tax period made final** | posting of a tax return | the tax lock date is set automatically | yes | as a soft lock | `EV-008` |
| `AE-19` | **Classification retired** | deprecation flag set | the account is refused for new postings | yes | by unsetting | `COR-03` |
| `AE-20` | **Classifications merged** | user | posted items retargeted; accounts **deleted by direct statement past the ORM's own guards**; no tracking written | **no — no record of any kind is created** | **no** | `EV-004`, `COR-08` |
| `AE-21` | **Measurement recorded or corrected** | rate entry or feed | one rate per currency per day per company group | yes | by replacement | `EV-018` |

## Events that occur without an operator asking

This is the register's most important cut. Seven events are emitted by the system on its own
initiative, and four of them are not visible at the moment they happen:

| Event | Invisible? | Why it matters |
|---|---|---|
| `AE-03` re-dating on document-date change | **yes** | changes period attribution with **no lock configured** and no accounting justification |
| `AE-02` re-dating on posting | after posting, yes | the posted record carries no trace that its date was moved |
| `AE-13` cash-basis tax dated today | **yes** | can cross a year boundary |
| `AE-20` merge | **yes** | rewrites posted history with no record |
| `AE-11` exchange difference | no | a visible separate entry |
| `AE-12` exchange reversal on unmatch | partly | |
| `AE-18` tax lock set by return posting | no | |

`RECOMMENDATION:` for SMEsPlus, every accounting event must be **explicit, recorded and attributable**.
An event the ledger emits on its own is still an event: it needs an actor (the system), a reason, and
a record. The four invisible events above are the concrete list of what a naive adoption of the
reference behaviour would import.

## Events the reference model does NOT have

| Absent event | Consequence | Evidence |
|---|---|---|
| **Period close** | there is no closer, no close date, no basis, no artefact — only a moved date | `EV-016`, `COR-01` |
| **Year-end result transfer** | current-year earnings is computed at report time and never posted | `EV-016` |
| **Revaluation / unrealised FX** | no carrier found in the scope read | `GAP-H01` |
| **Accounting event recognition, distinct from entry creation** | no event identity; duplicates undetectable | `GAP-B02`, `XM-01` |
| **Approval before posting** | posting authority is a single permission; there is no maker-checker step | `EV-011` |

These five absences are the Wave A design agenda. Each is recorded as a decision in file 22.
