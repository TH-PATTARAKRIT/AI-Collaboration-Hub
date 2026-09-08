# P08 RC-05 CONFIRMATION — RUN RESULTS, SCORED AGAINST THE PRE-RUN PREDICTION

**Prompt:** `[SMEPLUS-26-09-08-ACC-ONE-PROMPT-FINAL-CLOSURE-001]` §7
**Owner:** P08 Record-to-Report · **Baseline:** `e368d11da6f7e4973469ff5608d676ec2d13811c`
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. `P08-C3` — the control lineage, demonstrated rather than asserted

| | |
|---|---|
| **Prediction commit** | **`78f537876852ea6f20047524555fd89e90ee4c78`** · `2026-09-08T17:04:08+07:00` |
| **Prediction file digest** | `94b2117096360597ff2bba9141a5e4fd7711c22e2ccea752a4e90995208f967b` |
| **Its contents** | `00_PRE_RUN_PREDICTION.md` and `instrument/module_state.py`. **Nothing else. No run output of any kind.** |
| **This commit** | contains the results, and its **ancestry runs through the prediction commit** |

**Checkable by a third party without trusting a word of this file:**

```
git show --stat 78f5378          # prediction + instrument only, zero result files
git merge-base --is-ancestor 78f5378 <this commit>   # exit 0
git log --format='%H %cI' 78f5378..<this commit>     # result commit is strictly later
```

**Why this repairs `RC05-F3` and re-asserting the old timestamp would not.** The challenge was never that the prediction was wrong; it was that **Git did not record the ordering**, because the prediction, the instrument, the outputs and the asserted freeze-time all entered history in a single commit. **No wording could add an ordering that was never committed.** The ordering now exists as two commits, and it is read from the graph.

> **This is a repeat of the experiment, not a defence of the first one.** The 2026-09-07 freeze claim at `EXPECTED_CONTROL_BEHAVIOUR.md` is **not retroactively validated by this run** and remains as `RC05-F3` left it: **internally consistent, externally unprovable.**

## 2. Reproduction — every predicted cell, scored

**Instrument:** `rc05_balance.py`, SHA-256 `2151cd44…` — **unchanged**, matching the RC-05 manifest.
**Tool:** `pg_restore` 18.6 (Homebrew) · Python 3.14.0 · `decimal` precision 60, no float constructed at any step.
**Raw output:** `run/RUN_A_four_pg18.txt`.

| DB | posted moves w/ lines | posted lines | COMPUTED @ exact/1e-7/1e-4/0.005 | STORED @ same | PARENT_STATE_DISAGREE | sum \|debit\|+\|credit\| | Predicted? |
|---|---:|---:|---|---|---:|---:|---|
| `DB-SM` | **169,143** | **417,700** | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | **0** | 278,703,722,656.58 | **as predicted** |
| `DB-BK` | **16** | **563** | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | **0** | 29,420.00 | **as predicted** |
| `DB-EV` | **6** | **15** | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | **0** | 1,600.00 | **as predicted** |
| `DB-T2` | **5** | **14** | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | **0** | 1,832.08 | **as predicted** |

All four input SHA-256 digests equal those recorded in `RUN_4` at `e368d11`. **The frozen inputs are frozen.**

**The result stands: zero unbalanced posted entries at exact equality and at every tested tolerance, on both the computed and the stored column, in all four frozen RC-05 extracts.** The claim is **tolerance-independent**; stating a tolerance beside it was the original error and is not reintroduced.

## 3. Controls — scored, including the two that did not go as predicted

| # | Control | Predicted | Observed | Verdict |
|---|---|---|---|---|
| C1 | injection `0.01`, `DB-T2` | +1 at all four tolerances | **1 / 1 / 1 / 1** on both columns | **as predicted** |
| C2 | injection `0.001`, `DB-T2` | +1 at exact/1e-7/1e-4, **0** at 0.005 | **1 / 1 / 1 / 0** on both columns | **as predicted — the tolerance boundary is visible, not asserted** |
| C3 | missing input | exit 2 | `FAIL-CLOSED: input not found` · **exit 2** | **as predicted** |
| C4 | real file, not an archive | exit 3, `no COPY block` | `FAIL-CLOSED: no COPY block for table account_move` · **exit 3** | **as predicted** |
| C5 | no `pg_restore` on `PATH` | exit 2 | **first attempt exit 127 — see §3.1** · redone: **exit 2** | **BROKEN THEN CONFIRMED** |
| C6 | two clean runs | byte-identical | `cmp` → **identical** | **as predicted** |
| C7 | `pg_restore` 16.15 vs 18.6, four inputs | identical figures | **FALSIFIED — see §3.2** | **PREDICTION WRONG** |
| C8 | positive control, every DB | `sum(\|d\|+\|c\|) > 0` | non-zero in all four | **as predicted** |
| C9 | discriminating set | printed for all four | printed; `DB-BK`/`DB-EV`/`DB-T2` draft populations 0, `DB-SM` non-zero | **as predicted** |

### 3.1 `C5` was not a control on its first run — it was a broken test that looked like a result

The first `C5` invocation was `env PATH=/nonexistent python3 …`. **It returned exit 127: the shell could not find `python3`.** The instrument never started, so the control proved nothing about the instrument's `pg_restore` check.

**127 and 2 are both non-zero.** A reader skimming for "did it fail closed" would have seen a failure and moved on. **The test could not see its own input, and a test that cannot see its input returns something indistinguishable from a result.**

Redone with `PATH` holding a `python3` symlink and no `pg_restore`:

```
$ command -v pg_restore  ->  not found
FAIL-CLOSED: pg_restore not on PATH — required to read the custom-format dumps
exit=2
```

**Both the broken run and the corrected run are published** (`run/C5_no_pg_restore.txt`, `run/C5_no_pg_restore_REDONE.txt`). The failed control is not deleted.

### 3.2 `C7` is FALSIFIED — and the falsification is a finding worth more than the confirmation

`RUN_C` under `pg_restore` **16.15** processed `DB-SM`, `DB-BK` and `DB-EV` with figures identical to the 18.6 run, then **stopped**:

```
FAIL-CLOSED: no COPY block for table account_move in …/iTEST02_2026-07-14_16-34-51.dump
exit=3
```

Direct probe (`run/C7_archive_version_boundary.txt`):

```
pg_restore 16.15 -l DB-T2  ->  pg_restore: error: unsupported version (1.16) in file header   exit 1
pg_restore 18.6  -l DB-T2  ->  exit 0

iSMEs_2026-07-11_05-03-27        pg16: READABLE     pg18: READABLE
BK12MAY26_2026-08-03_05-48-30    pg16: READABLE     pg18: READABLE
iEVING_2026-07-23_10-31-06       pg16: READABLE     pg18: READABLE
iTEST02_2026-07-14_16-34-51      pg16: UNREADABLE   pg18: READABLE
```

**`DB-T2` is written in archive format 1.16 and `pg_restore` 16 refuses it. The other three are readable by both.**

**Three consequences, and one correction to this file's own author.**

1. **`P08-C1a` — a tool-version precondition now travels with the four-input claim.** Reproducing the four-input result requires `pg_restore` **≥ 18**. This is recorded at `58_` beside the figure, not only here.
2. **The `C4` fail-closed guarantee is now demonstrated on real data, not only on a synthetic file.** An extract the tool cannot parse produced **exit 3**, never a fourth zero. **Had the instrument been written to treat an unreadable extract as an empty table, this run would have published `DB-T2 = 0 posted moves, 0 unbalanced` — a clean, plausible, wholly false fourth confirmation.**
3. **`RC-05` was right and this prediction was not.** RC-05 wrote *"**shared three-DB** outputs under pg_restore 16.15 vs 18.6 => normalized outputs identical"*. **The qualifier "shared three-DB" was load-bearing and this owner read past it**, generalising a carefully-bounded peer statement into a four-DB one and pre-registering the over-extension. **The peer's scope was correct; the owner widened it. A pre-registered prediction is the only reason that is visible now rather than propagating into `58_`.**

## 4. `P08-C4` — install state over the four frozen inputs

**Instrument:** `module_state.py`, frozen in the prediction commit, first executed after it. Raw output: `run/M1_module_state_pg18.txt`.

| DB | `ir_module_module` rows | `state='installed'` | `om_data_remove` | `account` | `smesplus_nonexistent_control_module` |
|---|---:|---:|---|---|---|
| `DB-SM` | 1,009 | 190 | **installed** | installed | **NOT PRESENT** |
| `DB-BK` | 1,508 | 251 | **installed** | installed | **NOT PRESENT** |
| `DB-EV` | 1,504 | 232 | **installed** | installed | **NOT PRESENT** |
| `DB-T2` | 1,559 | 453 | **installed** | installed | **NOT PRESENT** |

**The open prediction of §3.3 is confirmed: `om_data_remove` is `state='installed'` in all four frozen extracts.**

**Both controls fired.** `account` installed everywhere — the ledger tables the balance instrument reads therefore exist, which is a coherence check across the two instruments. The impossible module returned **NOT PRESENT** in all four, proving the reader distinguishes *"a row in another state"* from *"no row at all"* and is not echoing its argument. Fail-closed confirmed on an unreadable extract at **exit 3** (`run/M2_module_failclosed.txt`).

### What this does and does not license

| Wording | Verdict |
|---|---|
| *"installed in all four frozen RC-05 extracts"* | **SUPPORTED — this is now the wording at `58_`** |
| *"installed in all three deployed databases"* | **SUPERSEDED** — incomplete against the frozen population |
| *"installed across the deployed estate"* | **NOT SUPPORTED.** The estate's size is unproven; **four extracts are four extracts** |
| *"has been executed"* | **NOT SUPPORTED and not claimed.** Install state is **capability**. `P08-HO-13` stays *capability confirmed, execution NOT evidenced* |

## 5. `P08-C2` self-test — the `HO` namespace

| Check | Result |
|---|---|
| live P08 family | **`P08-HO-01`…`P08-HO-14`** — 14 distinct, contiguous, no gaps |
| defining rows per identifier in `54_` | **exactly one each** |
| apparent duplicate `P08-HO-01` | **false positive of the check, disclosed.** The second match is the namespace-inventory row *"`P08-HO-01` … `P08-HO-14`"*, a range statement, not a definition. **A row-shaped regex cannot tell a definition from an inventory; the classification was made by reading both, not by trusting the count.** |
| bare `HO-nn` occurrences remaining | **6 in `25_` §4 — now all struck and marked RETIRED** · 2 lines in `17_` and 3 in `54_` that *describe* the retirement |
| P06's `HO-01`…`HO-06` | **untouched, not renumbered** — a different package's family |

## 6. Manifest — `P08-C5`

`RC05_REPRODUCIBILITY/` holds **8 files on disk**; the substantive population is **7**. **`MANIFEST.md` is excluded by definition** — a manifest cannot carry its own digest, because writing it changes the bytes that produced it. The exclusion is now stated in the manifest rather than left to be inferred. **No missing substantive hash was found and none is invented.**

## 7. Self-test exit

```
P08 OWNER CLOSURE COMPLETE — RC05 DELTA SELF-TEST PASS
```

**Scored honestly: 7 of 9 controls as predicted, 1 broken-then-repaired, 1 falsified.** The falsified one changed a published claim and added a precondition. **An owner self-test that scores 9 of 9 has usually not been given the chance to fail.**

**Owner self-test only. Not independent certification.** RC-05's fresh delta challenge on the changed surfaces is reserved for the single final independent gate.

## 8. What is NOT claimed

- **Four frozen extracts are not an established deployment census.** Every corrected carrier says *four frozen RC-05 database extracts*.
- The 2026-09-07 freeze assertion is **not** retroactively proven.
- No Veto discharged. No P11 mutation. Not a PASS, not a freeze, not a merge, not an implementation authorisation.
