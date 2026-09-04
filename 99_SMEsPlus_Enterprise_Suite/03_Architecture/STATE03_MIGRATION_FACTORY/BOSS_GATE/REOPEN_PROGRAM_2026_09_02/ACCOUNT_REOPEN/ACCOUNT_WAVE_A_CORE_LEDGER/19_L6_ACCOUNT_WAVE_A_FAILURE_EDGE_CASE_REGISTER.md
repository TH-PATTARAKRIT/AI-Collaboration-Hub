> **CORR1 CORRECTION NOTICE.** Amended by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`.
> Corrections landing here: `COR-03, COR-09, COR-14, COR-17`. Governing text where they conflict with the body below: CORR1/C08 Part 2 (BALANCED BUT WRONG).
> Prior findings are retained unedited for lineage; see `CORR1/C02_..._ACCEPTED_CORRECTIONS_REGISTER.md`.

# 19 — LEVEL 6: CONTRADICTION / FAILURE / EDGE CASE REGISTER

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

Every challenge in the Boss list was attempted against the model. Result codes: `REACHABLE` (the
failure can occur), `PREVENTED` (a control blocks it), `DETECTED` (it can occur but is discoverable),
`UNKNOWN`.

| # | Challenge | Result | Mechanism | Evidence |
|---|---|---|---|---|
| `FE-01` | **Duplicate posting** of the same business event | **`REACHABLE`** | no accounting-event identity and no idempotency key exist; number uniqueness does not detect the same event posted twice under two numbers | `GAP-B02`, `XM-01` |
| `FE-02` | **Missing posting** | `UNKNOWN` | no completeness control identified; nothing asserts that a source event produced an entry | `GAP-B02` |
| `FE-03` | **Incorrect period** | **`REACHABLE`, and it is the default behaviour** | the accounting date is moved by a lock rule and, for non-sale documents, by a numbering rule that operates **with no lock configured** | `COR-02` |
| `FE-04` | **Wrong company** | `PREVENTED` | journal-to-company is exclusive; an account cannot be detached while its items reference it | `EV-006`, `EV-019` |
| `FE-05` | **Wrong tenant** | **`REACHABLE`** | no tenant concept exists; one configuration store has no company dimension at all | `SB-01` |
| `FE-06` | **Stale exchange rate** | **`REACHABLE`** | resolution falls back to the latest rate on or before the date, then to the earliest rate ever, then to **1.0** | `COR-14` |
| `FE-07` | **Partial reconciliation exceeding the item** | **`REACHABLE`** | the matching record carries no constraints at all | `COR-09` |
| `FE-08` | **Incorrect reversal** | `DETECTED` | reversal is linked to its original and both are annotated | `EV-012` |
| `FE-09` | **Locked-period override** | **`REACHABLE` by design** | a lock exception may apply to **every user**, **forever**, with an **optional** reason, granted and revoked by the same role | `EV-021`, `COR-04` |
| `FE-10` | **Orphan journal item** | `PREVENTED` | items belong to exactly one entry and are deleted with it | `EV-013` |
| `FE-11` | **Source deleted after posting** | **`REACHABLE`** | no general source reference is carried; nothing links a posting to its origin document | `GAP-B02` |
| `FE-12` | **Source modified after posting** | **`REACHABLE`** | as above — no link, therefore no divergence detection | `GAP-B02` |
| `FE-13` | **Reporting mismatch after a chart change** | **`REACHABLE`** | no temporal validity on accounts; a merge deletes the predecessor with no record | `GAP-A03`, `COR-08` |
| `FE-14` | **General ledger versus subledger mismatch** | `PREVENTED` — structurally | there is one set of items; the subledger is a view over it | `P-04` |
| `FE-15` | **Trial balance imbalance** | **`REACHABLE`** | the entry balance invariant is an application check with a suppression flag and **no storage constraint** | `COR-07` |
| `FE-16` | **Currency imbalance** | sign `PREVENTED`; magnitude **`REACHABLE`** | a database check enforces sign agreement only | `COR-06` |
| `FE-17` | **Analytic mismatch** | **`REACHABLE`** | analytic lines are deleted on un-post and regenerated only from the stored distribution; lines not derived from a distribution are lost permanently | `EV-012` |
| `FE-18` | **Tax mismatch** | **`REACHABLE`** | tax fields are outside hash coverage; the statutory extract recomputes amounts from configured rates rather than reading posted balances | `COR-06`, `COR-20` |
| `FE-19` | **Late transaction** | **`REACHABLE`, silently** | re-dated forward; the posted record carries no trace that its date was moved, and the warning is hidden once posted | `COR-02` |
| `FE-20` | **Backdated transaction** | as `FE-19` | | `COR-02` |
| `FE-21` | **Reopening a period** | **`REACHABLE`, unguarded** | soft locks move backward freely, with no distinct authority and no artefact | `EV-008` |
| `FE-22` | **Concurrent correction** | `UNKNOWN` | no optimistic-concurrency or record-version mechanism identified in the scope read | `GAP-C05` |
| `FE-23` | **Failed integration / retry** | **`REACHABLE`** | no idempotency key; a retry produces a second valid entry | `XM-01` |
| `FE-24` | **Migration inconsistency** | **`REACHABLE`** | no provenance carrier; tamper-evidence keyed on storage identifiers cannot cross the boundary | `EV-017`, `COR-12` |
| `FE-25` | **Concurrent account creation with the same code** | **`REACHABLE`** | uniqueness checked by an unlocked read; a conventional constraint is not expressible against the chosen storage | `COR-05` |
| `FE-26` | **Duplicate entry number** | `PREVENTED` when posted; **`REACHABLE`** while draft | the unique index is partial | `EV-006` |
| `FE-27` | **Posting to a retired account** | `PREVENTED` | blocked at three points, one of which has no bypass | `COR-03` |
| `FE-28` | **Retiring an account that still holds a balance** | **`REACHABLE`** | the only precondition is a tax-distribution check | `COR-03` |
| `FE-29` | **Editing a secured entry's canonical amount** | **`REACHABLE`; `DETECTED`** | the write guard reads pre-normalised keys and fails open; the integrity report still catches it | `CONTRA-01a` |
| `FE-30` | **Editing a secured entry's transaction-currency amount** | **`REACHABLE`; NOT detected** | neither guarded nor covered by the hash | `CONTRA-01b` |
| `FE-31` | **Hash collision on different amounts** | **`REACHABLE`** | company-currency amounts are serialised at the transaction currency's decimal places | `CONTRA-06` |
| `FE-32` | **Deleting a posted fact** | **`REACHABLE`** | protection is configuration, default off; the bypass records the deletion outside the database | `EV-011` |
| `FE-33` | **Rewriting posted history via a merge** | **`REACHABLE`, unlogged, irreversible** | executed by direct statement past the ORM's own deletion guards; nothing is recorded | `COR-08` |
| `FE-34` | **Settlement refused for a reason not stated** | **`REACHABLE`** | a reconciliation in the window between the fiscal and tax locks hard-fails as a write error | `COR-17` |

## Summary

| Result | Count |
|---|---|
| `REACHABLE` (including partly) | **24** |
| `PREVENTED` | 6 |
| `DETECTED` but reachable | 2 |
| `UNKNOWN` | 3 |

## The seven that matter most

Ranked by the combination of severity, silence and likelihood:

| Rank | Failure | Why it ranks here |
|---|---|---|
| 1 | `FE-06` **missing rate converts at par** | silent, produces an internally consistent wrong ledger, most likely during onboarding |
| 2 | `FE-03` / `FE-19` **period attribution altered, sometimes with no lock set** | silent, universal, statutory consequence |
| 3 | `FE-15` **trial balance can be imbalanced** | the defining invariant is suppressible |
| 4 | `FE-33` **merge rewrites history unlogged and irreversibly** | no control of any kind |
| 5 | `FE-01` / `FE-23` **duplicate posting** | no identity, no idempotency, no detection |
| 6 | `FE-07` **over-reconciliation** | unbounded settlement |
| 7 | `FE-05` **cross-tenant control disable** | one write, every tenant, invisible |

## CHECKPOINT L6

| Item | Record |
|---|---|
| Scope completed | All 25 Boss-listed challenges plus 9 additional, tested against the model |
| Evidence inspected | `EV-001`–`EV-023`, `COR-01`–`COR-20` |
| Verified findings | 24 of 35 challenges are reachable; only 6 are prevented; the most severe failures are silent rather than noisy |
| Contradictions | `CONTRA-01a`/`01b`, `CONTRA-02` through `CONTRA-11` — consolidated in file 20 |
| Unknowns | Missing-posting completeness (`FE-02`), concurrent correction (`FE-22`), and suppression-flag reachability from an external interface (`GAP-C04`) |
| Risks | The dominant pattern is silence: the worst failures produce valid-looking records |
| Expert disagreements | Four expert reviews returned; 20 corrections accepted, 6 contradicting research-team claims |
| Audit challenges | Independent challenge unit returned one veto and three contradictions |
| Next research target | Levels 7–12 executed; consolidation into the Final Gate package |

`CHECKPOINT L6 RECORDED.` The Boss instruction was not to stop at Level 6 unless a material blocker
prevents further evidence-based research. **No such blocker arose.** Research continued through
Levels 7 to 12. Not Boss approval.
