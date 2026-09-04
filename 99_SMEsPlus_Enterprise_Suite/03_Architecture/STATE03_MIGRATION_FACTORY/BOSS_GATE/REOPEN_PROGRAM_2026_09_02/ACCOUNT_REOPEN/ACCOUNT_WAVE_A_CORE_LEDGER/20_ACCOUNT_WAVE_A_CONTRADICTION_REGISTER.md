> **CORR1 CORRECTION NOTICE.** Amended by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`.
> Corrections landing here: `all`. Governing text where they conflict with the body below: CORR1/C03; CORR1/C04.
> Prior findings are retained unedited for lineage; see `CORR1/C02_..._ACCEPTED_CORRECTIONS_REGISTER.md`.

# 20 — ACCOUNT_WAVE_A_CONTRADICTION_REGISTER

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

A **contradiction** here means a place where the system's stated purpose and its actual behaviour
disagree — not merely a limitation. Each is stated, evidenced, and classified.

Classification: `CONFIRMED BY EVIDENCE` · `CONTRADICTED` · `UNKNOWN` · `HOLD` · `VETO`.

---

| # | Contradiction | Classification | Evidence |
|---|---|---|---|
| `CONTRA-01a` | An entry marked **"Secured"** by an inalterability hash permits its **canonical amount field** to be written. The guard evaluates the caller's raw keys before they are normalised, so the same economic change is refused when expressed one way and accepted when expressed another. The integrity report still detects it. | `CONFIRMED BY EVIDENCE` | `COR-06` |
| `CONTRA-01b` | The same "Secured" entry permits its **transaction-currency amount, currency, tax fields, analytic distribution and due date** to be changed — **neither blocked nor detected**. The label asserts an integrity guarantee the mechanism does not provide in a multi-currency ledger. | `CONFIRMED BY EVIDENCE` | `EV-010`, `COR-06` |
| `CONTRA-02` | The per-company code interface encodes identity as **arithmetic over two identifiers**, with a ceiling of 10,000. Above it the encoding aliases and the interface reads or writes another company's code — **silently, without raising**. | `CONFIRMED BY EVIDENCE` | `EV-020`, `COR-18` |
| `CONTRA-03` | The system deliberately separates account **identity** from account **code** so identity survives relabelling — and then provides a merge that **deletes the account record and retargets posted history to another account**. The architecture asserts durable identity; one operation destroys it. | `CONFIRMED BY EVIDENCE` | `EV-001`, `EV-004`, `COR-08` |
| `CONTRA-04` | A lock exists to protect a closed period. Machine-generated consequences of events in that period are **relocated into the current period** — potentially a different fiscal year — so the lock preserves the period's *arithmetic* while corrupting its *attribution*. | `CONFIRMED BY EVIDENCE` | `EV-015`, `COR-17` |
| `CONTRA-05` | **The defining invariant of double-entry accounting — debits equal credits — has no storage-level enforcement and is suppressible by a named flag**, while four lesser per-item rules *are* genuine database constraints. The control tiering is inverted relative to accounting significance. | `CONFIRMED BY EVIDENCE` | `COR-07` |
| `CONTRA-06` | The integrity hash serialises **company-currency** amounts at the **transaction currency's** decimal precision. Two materially different amounts can hash identically. The mechanism intended to make amounts tamper-evident is precision-blind in exactly the multi-currency case where `CONTRA-01b` already applies. | `CONFIRMED BY EVIDENCE` | `COR-11` |
| `CONTRA-07` | The tamper-evidence chain is keyed on **database row identifiers**, so it cannot survive a migration, a restore, or a tenant split or merge — the moments at which independent assurance is most needed. | `CONFIRMED BY EVIDENCE` | `COR-12` |
| `CONTRA-08` | **A posting in a currency with no configured rate is converted at 1:1, silently.** The resulting entry balances, satisfies the sign constraint, and passes every other control — while asserting an exchange rate the business never agreed to. A fabricated measurement is indistinguishable from a real one. | `CONFIRMED BY EVIDENCE` | `COR-14` |
| `CONTRA-09` | Reconciliation records carry **no constraints at all**. Nothing prevents settlement exceeding the obligation it settles, in **any** currency configuration. | `CONFIRMED BY EVIDENCE` | `COR-09` |
| `CONTRA-10` | Matching records — settlement facts — are **deleted silently** by an operation performed on the entry, with no reconciliation-level action, no authority check, and no record that a match ever existed. | `CONFIRMED BY EVIDENCE` | `EV-012` |
| `CONTRA-11` | The **grant** and the **revocation** of a lock-date override are held by the **same single role**, and the revocation path deliberately escalates past the read-only access rule that appears to prevent it. An override control with no segregation of duties is not a control. | `CONFIRMED BY EVIDENCE` | `COR-04` |
| `CONTRA-12` | **The accounting date is not a user input.** It is moved by a lock rule and, for non-sale documents, by a **numbering-convenience rule that operates with no lock configured at all**. Period attribution — an accounting fact — is subordinated to sequence monotonicity, a presentation concern. The user-visible warning is hidden once the entry is posted, so the record carries no trace that its date was moved. | `CONFIRMED BY EVIDENCE` | `COR-02`, `COR-20` |
| `CONTRA-13` | The posted-entry field freeze is presented as an invariant of the ledger but is **owned by the calling module**: one core module suppresses it on **every** write it performs. | `CONFIRMED BY EVIDENCE` | `COR-15` |
| `CONTRA-14` | Deletion of a posted fact — where permitted — is recorded to the **application log, outside the tenant database**. The evidence of the most destructive act available leaves the records it concerns. | `CONFIRMED BY EVIDENCE` | `EV-011` |
| `CONTRA-15` | A configuration value governing a core numbering control has **no company dimension whatsoever**. In a shared database, one write disables that control for **every tenant**, invisibly. | `CONFIRMED BY EVIDENCE` | `COR-16` |

---

## Contradictions raised against this session's own evidence base

Recorded for completeness, because the challenge unit and experts contradicted the research team as
well as the reference system. Full detail in `E01`.

| # | Research-team claim | Outcome |
|---|---|---|
| `SELF-01` | "No fiscal-year model exists in the tree" | **`CONTRADICTED`** — one exists; the *conclusion* survives and is strengthened (`COR-01`) |
| `SELF-02` | "The lock re-dates to lock + 1 day on create" | **`CONTRADICTED` in mechanism** — three mechanisms exist; the conclusion is understated, not overstated (`COR-02`) |
| `SELF-03` | "Lock exceptions are append-only" | **`CONTRADICTED`** (`COR-04`) |
| `SELF-04` | "No rate-type dimension exists" | **`CONTRADICTED`** — types are derived at query time (`COR-10`) |
| `SELF-05` | "The numbering control parameter is tenant-writable and tenant-wide" | **`CONTRADICTED` in both directions** (`COR-16`) |
| `SELF-06` | "Thai localization source was not available" | **corrected** — two modules are present in the verified build (`COR-13`) |

## Counts

| Classification | Reference-system contradictions | Self-contradictions |
|---|---|---|
| `CONFIRMED BY EVIDENCE` | 15 | — |
| `CONTRADICTED` | — | 6 |
| `UNKNOWN` | 0 | 0 |
| `HOLD` | 0 | 0 |
| `VETO` | 0 (see file 24) | 0 |

## Resolution status

**None of the fifteen contradictions is resolved by this session, and none can be.** Each describes
the reference system's behaviour, which Wave A may only *learn from*. Each is carried into file 22 as
a semantic-transfer decision — `ADAPT`, `EXTEND`, `REJECT` or `UNKNOWN` — and the four most severe are
carried into file 26 as blockers to a research gate.
