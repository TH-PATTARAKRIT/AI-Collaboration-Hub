# P08_EVENT_TO_GL_MATRIX

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · Layer 1

## Evidence-discipline notice — read before the matrix

> **Debit and credit are marked `UNKNOWN — EVIDENCE REQUIRED` for every event whose posting pattern this session did not read from primary source.** They are not inferred from general accounting knowledge. Filling them from convention would convert inference into apparent fact, which this project's evidence standard forbids, and would pre-empt the owning process's gate.

This notice is inherited verbatim in substance from the prior Wave A matrix and is re-asserted here, because P08's scope is the ledger contract, not the producers' posting patterns.

## Part 1 — Ledger-emitted events, whose effect P08 did establish

| ID | Event | Journal | Accounts | Date rule | Dr/Cr | Company that owns the effect |
|---|---|---|---|---|---|---|
| `M-01` | Settlement difference | the company's dedicated difference journal | gain or loss account by sign; counter-leg returns to the original item's own account, carrying that item's counterparty and currency | later of the two matched dates, **moved forward** if that falls in a locked period | established: one leg to the difference account, one to the original account | **selected by recordset position when the match spans two companies — see `P08-T0-04`** |
| `M-02` | Cash-basis tax on settlement | configured tax journal | `UNKNOWN — EVIDENCE REQUIRED` → P07 | **the system clock's current date** when the matched documents predate the lock | `UNKNOWN` | the settling company |
| `M-03` | Entry reversed | the original's journal | mirrors the original | any date the operator supplies, **including one earlier than the original** | mirror of the original | the original's company |
| `M-04` | Period made final | — | — | — | **NOT APPLICABLE — it posts nothing**, and that is the finding | — |
| `M-05` | Year result appropriated | — | — | — | **NOT APPLICABLE — no entry is generated**; the figure is computed at read time | — |
| `M-06` | Period-end revaluation | configured revaluation journal | configured provision accounts | period end, with an immediately posted reversal at period end + 1 | pair per adjusted account, transaction-currency amount zero | the revalued company |
| `M-07` | Opening balance loaded | setup journal | balancing leg to the single undistributed-result account | operator-supplied | established | the loading company |

`M-04` and `M-05` are the two rows that matter most. Both are marked `NOT APPLICABLE` **with the reason stated**, rather than left blank, because a blank in this matrix would read as unsearched.

## Part 2 — Producer events, ledger interface established, posting pattern deliberately not stated

For each of the twenty producer events `BE-01`..`BE-18`, `BE-21`, `BE-22` in `12_P08_BUSINESS_EVENT_REGISTER.md`:

| Column | P08 states it? |
|---|---|
| Recognition trigger | **yes** — the ledger contract requires it (`BE-RQ-02`) |
| Journal selection rule | **yes** — the ledger constrains it |
| Currency handling | **yes** — `P08-RQ-FX-02`/`03` |
| Settlement participation | **yes** — whether the event creates or discharges an open item |
| Close impact | **yes** — whether the event may post into a closed period (it may not) |
| Correction route | **yes** — new fact only |
| **Debit** | **`UNKNOWN — EVIDENCE REQUIRED`** → owning process |
| **Credit** | **`UNKNOWN — EVIDENCE REQUIRED`** → owning process |

**The six columns P08 does complete are precisely the ledger contract each producing process must satisfy.** When P01–P07 and P09–P10 complete their posting patterns, **this matrix is the place they are recorded**, so that the ledger-side constraints established here travel with them. That routing is inherited from the prior Wave A matrix's own recommendation and is re-asserted.

## Part 3 — What the matrix establishes

1. **Three accounting events are emitted by the ledger itself** (`M-01`, `M-02`, and the reversal half of `M-03`), and **two of them can be attributed to a period other than the one the underlying event belongs to** — one by forward relocation, one by taking the system clock.
2. **The only events with no debit and credit at all are period close and year appropriation**, because they post nothing. Both are marked `NOT APPLICABLE` with the reason, not left blank.
3. **One event's owning company is selected by recordset position.** `M-01` under a cross-company match. That is not an accounting rule; it is an artefact of list order, and it is a tolerance-zero item.
