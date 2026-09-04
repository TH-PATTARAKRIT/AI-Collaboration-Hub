> **CORR1 CORRECTION NOTICE.** Amended by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`.
> Corrections landing here: `VETO-01`. Governing text where they conflict with the body below: CORR1/C03 CC-02 — veto accepted, resolved by correction.
> Prior findings are retained unedited for lineage; see `CORR1/C02_..._ACCEPTED_CORRECTIONS_REGISTER.md`.

# 24 — LEVEL 12: ADVERSARIAL CHALLENGE & AUDIT VETO REGISTER

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

The independent challenge unit was instructed to **falsify** the evidence base, not to confirm it,
and did not author any part of it. Its full register is at
`CHALLENGE/C1_ADVERSARIAL_CHALLENGE_REGISTER.md`.

## 1. Veto issued

### `VETO-01` — against `EV-009` as originally written

**Raised by** the independent challenge unit.
**Target** the evidence base's account of how a locked period affects an entry's date.
**Ground** the cited location is inside the duplication path, not the creation or posting path. The
claim therefore described a real behaviour but attributed it to the wrong mechanism, and stated a
rule (`lock + 1 day`) that the actual posting path does not implement.

**Research team adjudication: `VETO ACCEPTED`.**

The research team re-verified against primary source and confirms the challenge unit is correct.
`EV-009` as written is superseded by `COR-02`.

**Effect of accepting the veto — the finding became more serious, not less.** The corrected mechanism
shows three independent re-dating paths, one of which operates **with no lock date configured at
all**, and the returned date is period-end rather than lock + 1. A vendor bill dated 15 January and
entered on 3 March books to 31 January in a completely unlocked system.

`VETO-01` is therefore **resolved by correction, not by dismissal**. The corrected finding
`CONTRA-12` is carried into the Final Gate package as a blocker.

## 2. Challenge results against the evidence base

| Claim challenged | Verdict | Outcome |
|---|---|---|
| `EV-002` no database constraint on account code | `CONFIRMED` | stands; extended by `COR-05` |
| `EV-003` no archive state on accounts | `CONFIRMED` | stands; posting-block unknown resolved by `COR-03` |
| `EV-009` silent re-dating | **`VETO`** | accepted; superseded by `COR-02`; **finding strengthened** |
| `EV-010` hash coverage is partial | `CONFIRMED WITH CAVEAT` | stands; split into `CONTRA-01a`/`01b` by `COR-06` |
| `EV-016` no fiscal-year model, no year-end closing entry | **`CONTRADICTED`** in its first half | a fiscal-year entity exists; **the load-bearing second half stands and is strengthened** (`COR-01`) |
| `EV-018` no rate-type dimension | **`CONTRADICTED`** | rate types are derived at query time (`COR-10`) |
| `EV-020` identifier-arithmetic ceiling | `CONFIRMED WITH CAVEAT` | trigger corrected — an identifier, not a count (`COR-18`) |
| `EV-021` permanent global exception possible; reason optional | `CONFIRMED WITH CAVEAT` | stands; "append-only" contradicted (`COR-04`) |

**Counts:** `CONFIRMED` 2 · `CONFIRMED WITH CAVEAT` 3 · `CONTRADICTED` 2 · `VETO` 1 · `UNKNOWN` 0.

## 3. Independent challenge findings

The challenge unit produced findings the research team had not reported. Those re-verified and
accepted are recorded as `COR-10` through `COR-13`. The most consequential:

| # | Challenge | Classification | Disposition |
|---|---|---|---|
| `CH-01` | The hash serialises company-currency amounts at the transaction currency's precision — a collision vector | `CONFIRMED BY EVIDENCE` | accepted as `COR-11` / `CONTRA-06` |
| `CH-02` | The hash chain is keyed on storage row identifiers and cannot survive migration | `CONFIRMED BY EVIDENCE` | accepted as `COR-12` / `CONTRA-07` |
| `CH-03` | The integrity verification stops at the first corrupted entry per prefix and has no gap check | `CONFIRMED BY EVIDENCE` | recorded; reinforces `ST-13` |
| `CH-04` | Thai localization source is present in the build and was not registered | `CONFIRMED BY EVIDENCE` | accepted as `COR-13` |
| `CH-05` | Six named context flags disable ledger controls across many production call sites | `CONFIRMED BY EVIDENCE` | recorded; reinforces `ST-28` / `CONTRA-13` |
| `CH-06` | Account code uniqueness is *unconstrainable*, not merely unconstrained | `CONFIRMED BY EVIDENCE` | accepted as `COR-05` |
| `CH-07` | Managers can delete mid-chain while an unreported gap detector exists | `HOLD` | recorded; not adjudicated this session |

## 4. Audit challenge categories — results

Against the mandatory challenge list:

| Category | Result |
|---|---|
| Unsupported assumption | **found** — three negatives asserted at a wider scope than searched |
| Missing evidence | **found** — Thai localization source unregistered |
| Semantic conflation | **found** — "posted", "locked", "closed" and "secured" were being used interchangeably; corrected in file 01 §7 |
| UI-driven design bias | **found and corrected** — the original account of re-dating was drawn from user-facing behaviour rather than from the posting path |
| Legacy architecture leakage | **not found** — no reference structure is carried into the SMEsPlus positions; ten behaviours are explicitly rejected |
| Wrong source-of-truth assumption | **found** — the accounting date was initially treated as a user input; it is system-derived |
| Wrong financial recognition point | not found |
| Broken audit trail | **found** — five of nine audit questions are unanswerable |
| SaaS boundary failure | **found** — four, in file 16 |
| Control weakness | **found** — fourteen, in file 14 |
| Reconciliation impossibility | **found** — three of seven proof equations do not hold as stated |

## 5. Challenge unit position, and the research team's response

The challenge unit's register stands as written; the research team does not edit it. Where the
research team reached a different conclusion — on the severity of the hash guard defect (`DIS-01`)
and on which field is most exposed (`DIS-03`) — both positions are preserved in file 23 rather than
reconciled.

**No finding in this package was dismissed by the team that produced it.** Every challenge was either
accepted and incorporated, or recorded as a preserved disagreement.
