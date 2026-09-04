> **CORR1 CORRECTION NOTICE.** Amended by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`.
> Corrections landing here: `COR-03, COR-10, COR-13`. Governing text where they conflict with the body below: CORR1/C04 — GAP-H01 rescoped; Thai items unchanged (HOLD).
> Prior findings are retained unedited for lineage; see `CORR1/C02_..._ACCEPTED_CORRECTIONS_REGISTER.md`.

# 21 — ACCOUNT_WAVE_A_UNKNOWN / EVIDENCE GAP REGISTER

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

Every unknown states **exactly what evidence is missing** and **what would close it**. Nothing here
is guessed, and nothing here is filled from general ERP knowledge.

## A — Closable by further primary-source reading

| # | Unknown | What would close it | Priority |
|---|---|---|---|
| `GAP-A01` | Whether an explicit control-account concept exists, distinct from account type | targeted read of the reporting layer's subledger handling | medium |
| `GAP-A02` | Whether any equity-movement restrictions exist | targeted read of equity handling | low |
| `GAP-E01` | Write-off policy semantics — authority, limits, account selection | read of the write-off path in the reconciliation interface | medium |
| `GAP-E02` | Whether any matching history artefact exists | targeted search for match audit records | **high** — five of nine audit questions depend on it |
| `GAP-E03` | Whether any mechanism reconstructs stored derived settlement values after drift | search for recompute or repair routines | **high** |
| `GAP-H02` | Effect of correcting a past rate on already-posted entries | trace rate-change propagation | medium |
| `GAP-S01` | Whether chart-template rollback exists | read of the template reload path | medium |
| `GAP-C02` | Whether account merge is reversible or audited by any means | already largely answered — nothing is logged (`COR-08`); confirm no external audit hook | low |

## B — Requires an executed test, not source reading

| # | Unknown | Why reading cannot close it |
|---|---|---|
| `GAP-C04` | Whether the control-suppression flags are reachable from an external interface | reachability depends on runtime request handling, not on the definitions; **this is the single most important open question in the control model** — if reachable externally, `IC-01`, `IC-07`, `IC-08` and `CONTRA-05` become remotely exploitable rather than internally risky |
| `GAP-C05` | Whether concurrent correction is protected by any versioning | requires a concurrency test |
| `GAP-C03` | Whether any posting path is idempotent in practice | requires a retry test |
| `FE-02` | Whether any completeness control detects a missing posting | requires an end-to-end test |

`RECOMMENDATION:` `GAP-C04` should be closed before any SMEsPlus control design is finalised. It
determines whether the reference model's suppression-flag pattern is an internal engineering
convenience or an externally reachable control bypass — a difference that changes the severity of
four separate findings.

## C — Requires Boss or governance decision, not evidence

| # | Unknown | Owner |
|---|---|---|
| `CL-01` | Is a closed period a record or a date? | Boss |
| `CL-02` | Is retained earnings posted or computed at year end? | Boss |
| `CL-03` | Who may reopen, and does reopening leave an artefact? | Boss |
| `CL-04` | Does a late document post to its own period or the current one? | Boss |
| `CL-05` | Is the parent-to-subsidiary hard-lock cascade correct for SMEsPlus tenancy? | Boss |
| `TI-05` | How are template-derived and tenant-created configuration kept distinguishable? | Boss — **no reference answer exists** |
| `XM-01` | What is the accounting-event identity and idempotency model? | Boss |

## D — Routed to the Accounting-Tax track — `HOLD / EVIDENCE REQUIRED`

This session makes **no** Thai statutory determination. Each item below states what was observed in
an implementation, never what the law requires.

| # | Item | Status |
|---|---|---|
| `TX-01` | Whether re-dating a late document to a later accounting period is acceptable for Thai VAT period attribution | `HOLD / EVIDENCE REQUIRED` |
| `TX-02` | Whether the same is acceptable for withholding-tax period attribution and certificate dating | `HOLD / EVIDENCE REQUIRED` |
| `TX-03` | Whether a statutory extract may recompute a tax amount from a configured rate rather than reading the posted balance | `HOLD / EVIDENCE REQUIRED` |
| `TX-04` | Whether a cash-basis tax entry relocated into a later year is acceptable | `HOLD / EVIDENCE REQUIRED` |
| `TX-05` | What Thai year-end statutory close and audit require that a lock date cannot evidence | `HOLD / EVIDENCE REQUIRED` |
| `TX-06` | Retention and filing-history requirements bearing on migration | `HOLD / EVIDENCE REQUIRED` |
| `TX-07` | Whether withholding tax suffered requires a certificate-matching carrier | `HOLD / EVIDENCE REQUIRED` |

All Thai account, tax and report names encountered are **candidate / UNVALIDATED**.

## E — Deliberately out of Wave A scope

Recorded so that later Waves do not treat Wave A's silence as a finding.

| Area | Owning Wave |
|---|---|
| Producer posting patterns — debit and credit per event | each producing Wave; see file 08 |
| Tax computation and reporting semantics | `WAVE-D TAX` |
| Analytic accounting semantics | `WAVE-E ANALYTIC` |
| Deferred and time-based recognition | `WAVE-F` |
| Financial statement structure and presentation | `WAVE-G REPORTING` |
| Bank statement flow and payment mechanics | `WAVE-H BANKING` |
| Receivable and payable process | `WAVE-B AR`, `WAVE-C AP` |

## F — Bootstrap layer

| # | Item | Status |
|---|---|---|
| `GAP-B01` | Three of five named bootstrap documents are absent under those exact filenames; equivalent content exists under domain-specific names | non-blocking — the constitution itself was read and applied (`EV-023`) |
| `GAP-B02` | **No accounting-event identity and no provenance carrier exist anywhere in the domain** | **the root cause of `FE-01`, `FE-11`, `FE-12`, `FE-23`, `FE-24` and the collapse of correction semantics** — this is the most consequential single gap in Wave A |

## Counts

| Category | Count |
|---|---|
| Closable by further reading | 8 |
| Requires an executed test | 4 |
| Requires Boss decision | 7 |
| Routed to Accounting-Tax (`HOLD`) | 7 |
| Out of scope by design | 7 areas |
| Bootstrap | 2 |
| **Total open unknowns** | **28** |
