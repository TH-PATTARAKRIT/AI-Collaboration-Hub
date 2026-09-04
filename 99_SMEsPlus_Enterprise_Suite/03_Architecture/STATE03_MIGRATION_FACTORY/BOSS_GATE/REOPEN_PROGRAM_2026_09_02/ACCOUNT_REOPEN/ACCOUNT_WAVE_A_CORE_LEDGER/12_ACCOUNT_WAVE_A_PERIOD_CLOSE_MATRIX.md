> **CORR1 CORRECTION NOTICE.** Amended by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`.
> Corrections landing here: `COR-01, COR-02`. Governing text where they conflict with the body below: CORR1/C04 NC-01; CORR1/C07.
> Prior findings are retained unedited for lineage; see `CORR1/C02_..._ACCEPTED_CORRECTIONS_REGISTER.md`.

# 12 — ACCOUNT_WAVE_A_PERIOD_CLOSE_MATRIX

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

## 1. The Boss question, answered

> *What exactly becomes locked: source document, accounting event, journal entry, reporting period,
> tax period, or combinations?*

**Answer — none of those. What is locked is a range of accounting dates, per company, per lock kind.**

There is no period object to lock (`EV-016`, `COR-01`), no document-level lock, and no entry-level
lock. There are five dates, and an entry falls inside or outside each of them by comparison. The
effective lock for a posting is composed at the moment of posting from the greater of the global and
hard locks, raised further by the sale or purchase lock when the journal is of that type.

And critically, being "locked" does **not** mean refused. It means **re-dated** (`COR-02`).

## 2. Period close matrix

| Dimension | Reference behaviour | Evidence | SMEsPlus position |
|---|---|---|---|
| **Is there a period object?** | **No.** Two integers on the company derive boundaries; an optional, fully mutable fiscal-year record may override them | `EV-016`, `COR-01` | `EXTEND` — a closed period must be a record |
| What close *is* | moving a date forward | `EV-008` | `EXTEND` |
| Monthly close | move the lock to month end | `EV-008` | `ADAPT` — matches the Boss baseline |
| Month 12 | **procedurally identical to any other month** | `EV-016` | `ADAPT` — **independently corroborates the Boss baseline** |
| Year-end closing entry | **does not exist anywhere in the tree** | `EV-016`, re-verified under `COR-01` | design decision — no reference to adapt |
| Retained earnings transfer | **never posted**; the year's result is computed at report time against a current-year-earnings account | `EV-016` | **`UNKNOWN` — Boss decision required** |
| Carry forward | an account-**type** property, evaluated at report time — not an event | `EV-016` | `ADAPT` the concept; `EXTEND` the auditability |
| Temporary vs permanent accounts | derived from account type | `EV-016` | `ADAPT` |
| Opening balance | an ordinary posted entry balanced to current-year earnings | `EV-017` | `ADAPT` with provenance added |
| Post-close adjustment | permitted — it is re-dated forward, or a lock exception is granted | `EV-009`, `EV-021` | `EXTEND` — must be a named, authorised event |
| Prior-period correction | same as above; the correction lands in an open period, not the original one | `COR-02` | `EXTEND` |
| **Reopening** | soft locks move backward **freely, with no distinct authority and no artefact** | `EV-008` | **`REJECT`** — reopening must be a governed event |
| Hard close | monotonic, no exception, **cascades from parent companies**, refuses while drafts remain in the period | `EV-008` | `ADAPT` — the strongest control in Wave A |
| Preconditions to close | drafts must be cleared (hard lock only); **unreconciled bank lines block any fiscal-effective lock** | `EV-008`, `EV-019` | `ADAPT` and `EXTEND` — a good pattern to generalise |
| Who closed, when, on what basis | **no artefact** — only a tracked field change on the company record | `GAP-G01` | `EXTEND` |
| Tax period close | a posted tax return sets the tax lock automatically; reset-to-draft restricted where carryover exists | `EV-008` | `WAVE-D TAX` |
| Tax lock interaction | **excluded from the composed fiscal lock**; applies only to entries carrying tax; **shifts on creation but refuses on modification** | `COR-17` | `WAVE-D TAX` |
| Comparative reporting across a chart change | unsupported — there is no temporal validity on accounts | `GAP-A03` | `EXTEND` |

## 3. Hard versus soft — the real difference

| Property | Soft locks (four) | Hard lock (one) |
|---|---|---|
| Can move backward | **yes, freely** | **never** |
| Can be removed | yes | **never** |
| Exceptions possible | yes — per user, or for everyone, optionally forever | **none** |
| Cascades from parent | no | **yes** |
| Preconditions | unreconciled bank lines block it | that, plus no drafts in the period |
| Effect | re-dates | re-dates |

`INFERENCE:` the reference model gives one genuinely irreversible control and four advisory ones,
and the four advisory ones are what most users will operate. A soft lock is best understood as a
**default date policy**, not as a close.

## 4. The three preconditions worth adopting

The one part of the close design Wave A recommends adopting largely unchanged is the **precondition
pattern**: a close is refused, with a direct route to the offending records, when

1. draft entries remain in the period being closed;
2. unreconciled bank statement lines remain in the period;
3. (by extension, recommended) unhashed entries remain where securing is expected.

`RECOMMENDATION:` generalise this into a system-enforced close checklist. It is the only place in
Wave A where the reference model treats closing as a *state the data must earn* rather than a date
someone types.

## 5. Close-model decisions requiring Boss direction

| # | Decision | Why it cannot be inferred |
|---|---|---|
| `CL-01` | Is a closed period a **record** with a closer, a timestamp and a basis, or a date? | The reference has no artefact; the Boss baseline implies a monthly close discipline that a bare date cannot evidence |
| `CL-02` | Is retained earnings **posted** at year end, or **computed**? | No reference implementation exists either way; both are defensible; the choice determines whether a year can be reopened at all |
| `CL-03` | Who may **reopen**, and does reopening create an artefact? | The reference requires no authority and leaves no trace |
| `CL-04` | Does a late document post to its **own** period (requiring reopening) or to the **current** one (requiring restatement)? | `COR-02` shows the reference silently chooses the second, including with no lock configured |
| `CL-05` | Is the hard-lock cascade from parent to subsidiary correct for SMEsPlus tenancy? | It couples companies that a tenant may consider independent |
