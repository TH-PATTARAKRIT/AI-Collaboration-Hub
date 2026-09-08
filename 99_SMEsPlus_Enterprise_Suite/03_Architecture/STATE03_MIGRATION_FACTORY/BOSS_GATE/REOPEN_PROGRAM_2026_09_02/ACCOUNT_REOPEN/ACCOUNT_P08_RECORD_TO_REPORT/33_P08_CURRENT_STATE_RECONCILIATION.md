# P08_CURRENT_STATE_RECONCILIATION

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001`
Targeted continuation of `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`. **No reset. No restart. No prior evidence discarded.**

## 1. Baseline as found

| Field | Value |
|---|---|
| Branch | `research/account-p08-record-to-report-2026-09-04-001` |
| Head at continuation start | `4bdf8a2` |
| Layer 1 deliverables | 36 |
| Layer 2 quarantine files | 3 |
| Prior terminal position | `RECOMMEND HOLD`, EC 0 of 8, MC 1 met / 4 partial / 5 not met |

## 2. Counts in the continuation prompt, reconciled against the artefacts

The prompt instructed that its own figures must not be forced, and that the current authoritative artefacts govern. Result of that reconciliation:

| Prompt figure | Artefact figure | Delta |
|---|---|---|
| ~22 declared roots | **22**, listed in `01A` §2.1 | none |
| ~23 attacks documented | **23** in `16` §E | none |
| ~22 not prevented | **22 not stopped, 1 stopped on one path only** | none |
| ~28 controls | **28** in `30_P08_CONTROL_MATRIX.md` | none |
| ~6 at database level | **6** | none |
| ~1 protecting an accounting relationship | **1** | none |
| 26 defects found by review, 3 self-caught | **26 / 3** in `22` §8 | none |
| ~3 of ~23 class-A closed, ~19 not re-run | **3 closed, 19 listed** in `20` §5 | none |
| ~21 custom modules touching the ledger, ~1 examined | **21** in `E00` §2; more than one had in fact been examined — see Phase B | **delta recorded** |
| ~6 Supported Interpretations resolvable | **the true population is larger** — see Phase C | **delta recorded** |

Two deltas are recorded rather than absorbed. Everything else reconciles exactly.

## 3. What this continuation adds

| Phase | Checkpoint | Result |
|---|---|---|
| A | `CP-T02` | every eligible class-A pattern re-run across all 22 roots, each with a positive control |
| B | `CP-T03` | custom ledger module population re-derived and swept |
| C | `CP-T04` | **database evidence acquired** — three deployed database dumps, read-only, no server started |
| D–M | `CP-T05`..`CP-T13` | event identity, double-entry stack, context attack, truth roles, traces, close, scope, peers, attacks |

## 4. The material change of posture in this continuation

The prior session had **no runtime or database evidence of any kind** and said so. This continuation located and read **three deployed database dumps** on the evidence host, one of them production-scale (447,384 journal items, 169,143 posted entries).

That changes the evidential character of the package: findings that were `SUPPORTED INTERPRETATION` on source reading alone can now be **confirmed, quantified, or retracted** against real deployed data. Both outcomes occurred. See `35_P08_SUPPORTED_INTERPRETATION_CLOSURE.md`.

**Nothing was executed against a live system.** The dumps were read with an offline archive reader; no database server was started, no write was performed, no module installed.


---

## `P08-C4e` — THE THREE-EXTRACT BOUNDARY, DECLARED RATHER THAN CARRIED SILENTLY

**2026-09-08, one-prompt final closure, cross-package reconciliation.**

`RC-05` added a **fourth** frozen extract, `DB-T2`. Four P08 claims were **re-measured** across all four and are now stated over the four-extract population:

| Claim | Where | Re-measured on four? |
|---|---|---|
| ledger balance, both columns, four tolerances | `58_` §1 item 1, §8.2 | **yes** — `P08-C1` |
| the deletion module's install state | `58_` §5, `54_`, `56_` | **yes** — `P08-C4`, `C4b`, `C4d` |
| the external balance-check control's install state | `43_` §3 | **yes** — `P08-C4c` |
| six custom modules' install state | `LAYER2…/E00` | **yes** — `P08-C4c` |

**Every other P08 row whose population reads *"all three databases"* was measured on THREE extracts and has NOT been re-measured on `DB-T2`.**

**Named, not summarised** — these are the current `FACT VERIFIED` rows carrying that population:

| Row | File |
|---|---|
| *"States are draft, posted, cancelled"* | `53_P08_PHASE_S_CLOSURE_QUESTION_REGISTER.md`:61 |
| *"Moves the state to posted"* | `56_P08_POSTING_FINALITY_AND_CORRECTION_REGISTER.md`:14 |

> **THE POPULATION OF THESE ROWS IS THE THREE EXTRACTS EXAMINED AT THAT ROUND.** They are **not** claims about four extracts and **not** claims about the deployed estate.
>
> **They are not re-measured here, and the reason is scope, not convenience:** the one-prompt closure authorises the bounded four-input propagation that `RC05-F4` names, which is the population premise where the truth *could change*. **A state enumeration is not made false by a fourth extract; it is only made narrower than it looks.** Re-measuring it would be new research on an unchanged claim.
>
> **The blind spot is therefore the complement, and it is stated as a set rather than described:** `DB-T2` × {the two rows above}. **An undeclared boundary and a false claim are indistinguishable to a reader**, which is why this section exists instead of a silent carry-forward.

**Statements about how many dumps a prior round *located and read* — `28_`, `33_` §C, `35_` — are historical records of that round and are correct as written.** They are not current population claims and are not restated.
