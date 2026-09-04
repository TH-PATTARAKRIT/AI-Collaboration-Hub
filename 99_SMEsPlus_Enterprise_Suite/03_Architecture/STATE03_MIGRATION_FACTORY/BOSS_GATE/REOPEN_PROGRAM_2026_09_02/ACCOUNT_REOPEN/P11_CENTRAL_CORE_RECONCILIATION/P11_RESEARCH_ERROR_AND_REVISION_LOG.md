# P11 — RESEARCH ERROR AND REVISION LOG

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**
> This log records **this session's own errors**, not other packages'. Errors found in other packages
> are contradictions and live in `P11_CONTRADICTION_REGISTER.md`.

---

## `P11-E-01` — a headline figure contradicted its own table

| | |
|---|---|
| **Where** | `P11_UNIFIED_EVENT_OWNERSHIP_REGISTER.md` §2 |
| **Error** | The headline was drafted as *"`C2` fails for **8** of 44"*. Re-deriving the count from the §3 table returns **9** business facts |
| **Cause** | The draft figure was written before the table was finished and was not re-derived afterwards |
| **Detection** | Self-caught, by re-deriving the count from the table rather than restating the headline |
| **Correction** | Stated **inside the affected file**, adjacent to both figures, with the corrected value: **`C2` fails for 9 of 44** |
| **Why it is logged at all** | This is **`GB-06`'s exact shape** — a published count contradicting the dispositions beneath it — and it is the defect that produced `FC-F1` in the parent programme. It occurred here, in the first session to write about it. **A log that only recorded other people's instances of `GB-06` would be evidence that the control does not work** |

## `P11-E-02` — the superseded scope assumption

| | |
|---|---|
| **Where** | Every scope statement written before constitution correction `SMEPLUS-26-09-04-ACC-REV2-CORR1` was received |
| **Original assumption** | Tenant context + company context mandatory for every operation, inherited from `BC-02` element 10 and Wave A `TI-01` |
| **Why over-constrained** | `PLATFORM`-scoped reference data legitimately requires neither; a blanket rule would forbid the platform layer from existing |
| **Correction applied** | `P11_SCOPE_OWNERSHIP_MATRIX.md` created; five revalidations `RV-01`…`RV-05` recorded in full, each with original finding → assumption used → why over-constrained → correct analysis → updated classification → architecture impact → cross-process impact → evidence required |
| **Scope of rework** | **Delta only.** No evidence discarded, no checkpoint re-run, no completed enumeration repeated. Findings **not** touching the assumption are preserved byte-for-byte |
| **Net effect on severity** | **`RV-05` did not relax.** The 10-of-10 element-10 failure stands, because all ten material handoffs create a financial effect and are `COMPANY`-scoped. `RV-02` and `RV-03` **sharpened** their findings without changing either disposition. `RV-04` **narrowed** one blast radius. `RV-01` corrected a rule's reach while preserving its intent |

> A correction that relaxes a rule invites the reading that failing counts relax with it. **They did
> not, in four of five cases.** Recording the direction of each revalidation — rather than assuming
> it — is the whole point of running them.

## `P11-E-03` — a peer clone was mis-enumerated on the first pass

| | |
|---|---|
| **Where** | The first peer-intake sweep |
| **Error** | The glob `ACCOUNT_P0*_2026_09_04_EXECUTION` **silently excluded `P10`**, whose directory is `ACCOUNT_P10_TBR_...`. The first reading was "nine clones exist, `P10` has none" |
| **Cause** | An author-chosen pattern that did not cover its own declared population — **the exact defect the denominator rule exists to prevent**, committed while writing the file that states the rule |
| **Detection** | Caught when the enumeration script was written with the population declared **first**, which forced the pattern to cover `P10` |
| **Correction** | `p11_scripts/peer_intake.sh` and `peer_wip_snapshot.sh` both enumerate `P0[1-9]` **and** `P10` explicitly. All counts in this package are from the scripts, not from the first sweep |
| **Consequence if undetected** | The register would have reported a **9**-process peer dependency instead of **10** |

## `P11-E-04` — a peer working tree changed between two observations

| | |
|---|---|
| **Where** | `P01`'s working tree, between the intake script and the WIP snapshot, minutes apart |
| **Not an error — a property of the observation** | The peer sessions are **live**. `P01` showed `worktree_changes=0` on the first run and one untracked file on the second |
| **Correction to method** | Every peer-state count in this package is stamped `SNAPSHOT_UTC=2026-09-04T22:41:38+0700` and is described as a reading at an instant, not a stable population |
| **Why it is logged** | Because the alternative — reporting a count of peer work-in-progress as a finding — would have been a measurement presented as a fact about the programme |

---

## Summary

| Measure | Count |
|---|---|
| Errors made by this session | **3** (`P11-E-01`, `P11-E-02`, `P11-E-03`) |
| Self-caught before publication | **3 of 3** |
| Caught by an external reviewer | **0** — and this is **not** evidence of quality. `EC-07` requires two consecutive clean independent passes; this session has had **none** |
| Method observations logged | **1** (`P11-E-04`) |
