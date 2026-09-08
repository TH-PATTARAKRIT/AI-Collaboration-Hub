# P08_FINAL_DELTA_EVIDENCE.md

**Prompt:** `[SMEPLUS-26-09-08-ACC-ONE-PROMPT-FINAL-CLOSURE-001]` Part C · deliverable **5 of 12**
**Owner SHA:** **`ca577be42e6ba9535e1911dc0bad1dfab74a8aa8`** · baseline `e368d11da6f7e4973469ff5608d676ec2d13811c`
**Parent verifier result:** `RC-05 = FAIL` — *"the arithmetic result passes independent reproduction"*
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. `P08-C3` — the control lineage, demonstrated instead of asserted

`RC05-F3` did not challenge the balance result. It challenged the **provenance of the control**: the prediction, the instrument, the outputs, the manifest and the asserted freeze-time all entered history **in a single commit**, so Git recorded no ordering.

**No wording can add an ordering that was never committed.** The only repair is to do it again, visibly:

| # | SHA | Time | Contents |
|---|---|---|---|
| 1 | `78f537876852ea6f20047524555fd89e90ee4c78` | `17:04:08+07:00` | **prediction + two instruments. No run output of any kind.** |
| 2 | `f0cf287ac9f4ad37b0c19145df4a0e396af84c13` | `17:16:03+07:00` | results, scored |

```
git show --stat 78f5378                        # prediction only
git merge-base --is-ancestor 78f5378 ca577be   # exit 0
```

> **The 2026-09-07 freeze claim is NOT retroactively validated by this run.** It remains where `RC05-F3` left it: internally consistent, externally unprovable. **This is a repeat of the experiment, not a defence of the first one.**

## 2. Reproduction — unchanged instrument, unchanged inputs, different tool version

Instrument `rc05_balance.py` SHA-256 `2151cd44…` — **unchanged**, matching the RC-05 manifest.

| DB | posted moves w/ lines | posted lines | COMPUTED @ exact/1e-7/1e-4/0.005 | STORED | `PARENT_STATE_DISAGREE` |
|---|---:|---:|---|---|---:|
| `DB-SM` | 169,143 | 417,700 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 0 |
| `DB-BK` | 16 | 563 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 0 |
| `DB-EV` | 6 | 15 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 0 |
| `DB-T2` | 5 | 14 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 0 |

All four input digests equal those recorded at `e368d11`. **The frozen inputs are frozen.**

**Zero unbalanced posted entries at exact equality and at every tested tolerance, on both columns, in all four frozen RC-05 extracts.** The claim is **tolerance-independent**.

## 3. Controls — scored honestly: **7 as predicted, 1 broken then repaired, 1 falsified**

| # | Control | Predicted | Observed | Verdict |
|---|---|---|---|---|
| C1 | injection `0.01` | +1 at all four | 1 / 1 / 1 / 1 | as predicted |
| C2 | injection `0.001` | +1 at three, **0 at 0.005** | 1 / 1 / 1 / **0** | as predicted — the boundary is **visible**, not asserted |
| C3 | missing input | exit 2 | exit 2 | as predicted |
| C4 | non-archive file | exit 3 | exit 3 | as predicted |
| **C5** | no restore client on `PATH` | exit 2 | **exit 127**, then **exit 2** | **BROKEN, THEN CONFIRMED** |
| C6 | two clean runs | byte-identical | `cmp` identical | as predicted |
| **C7** | 16.x vs 18.x client, four inputs | identical | **FALSIFIED** | **PREDICTION WRONG** |
| C8 | positive control | non-zero money | non-zero in all four | as predicted |
| C9 | discriminating set | printed always | printed | as predicted |

### `C5` — a broken test that looked like a result
The first invocation stripped `PATH` so completely that **`python3` itself was not found: exit 127.** The instrument never started. **127 and 2 are both non-zero**, and a reader skimming for *"did it fail closed"* would have seen a failure and moved on. Redone with the interpreter reachable and the restore client absent: **exit 2**, correct message. **Both runs are published; the broken one is not deleted.**

### `C7` — falsified, and worth more than the seven confirmations
```
16.x client, DB-T2  →  unsupported version (1.16) in file header   exit 1
18.x client, DB-T2  →  exit 0
the other three extracts  →  readable by BOTH
```
**`DB-T2` is written in a newer dump-archive format that the 16.x client refuses.** The instrument **failed closed at exit 3** rather than reporting a fourth zero.

**Three consequences.**
1. **`P08-C1a` — a tool-version precondition now travels with the four-input figure**, recorded at `58_` beside it: reproducing it requires the **18.x restore client or newer**.
2. **The `C4` guarantee is now demonstrated on real data.** Had the instrument treated an unreadable extract as an empty table, this run would have published *"`DB-T2` = 0 posted moves, 0 unbalanced"* — **a clean, plausible, wholly false fourth confirmation.**
3. **`RC-05` was right and the prediction was not.** RC-05 wrote *"**shared three-DB** outputs … identical". **The qualifier was load-bearing and this owner read past it**, pre-registering the over-extension. A pre-registered prediction is the only reason that is visible now rather than propagating into `58_`.

## 4. Population and namespace repairs

| Item | Was | Now |
|---|---|---|
| `P08-C1` `58_` §1/§8 | *"all three deployed databases"* | **four frozen RC-05 database extracts**, `DB-T2` row added |
| `P08-C2` `25_` | bare `HO-01…HO-06` live; `54_` pointed at a *"`25_` §0"* **that did not exist** | **§0 retirement banner**; six rows struck **RETIRED**; P06's own `HO` family untouched |
| `P08-C4` `58_` §5 | *"installed in all three"* | **all four frozen extracts** |
| `P08-C4b` `54_` | third-party carrier of the same claim, uncorrected | corrected |
| `P08-C4d` `56_` ×2 | **third** carrier of the same claim | corrected |
| `P08-C5` manifest | population undeclared | **8 files on disk, 7 substantive; the manifest excluded by definition** |

**Live P08 handoff family: `P08-HO-01`…`P08-HO-14` — 14 distinct, contiguous, one defining row each.** The apparent duplicate at `P08-HO-01` is a **false positive of the check** — the second match is a range statement, not a definition — and is disclosed rather than silently discounted.

## 5. `P08-C4c` — the four-input install-state refresh, and one new finding

| Module (Layer 2 identifiers) | `DB-SM` | `DB-BK` | `DB-EV` | `DB-T2` |
|---|---|---|---|---|
| deletion module | installed | installed | installed | **installed** |
| external balance-check control | uninstalled | uninstalled | uninstalled | **uninstalled** |
| **custom access-rights module** | **NOT PRESENT** | uninstalled | uninstalled | ***installed*** |
| custom tax-period module | installed | installed | uninstalled | installed |
| negative control (impossible name) | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |

Positive control — modules at `installed` per extract: **190 · 251 · 232 · 453**.

> ### `P08-F-NEW-01` — the fourth extract carries a custom access-rights module the other three do not
>
> **Three different answers across four extracts: installed in one, present-but-uninstalled in two, no row at all in a third.** The earlier three-column table recorded two of them, and its `—` cells meant **unmeasured**, not absent.
>
> **P08 has not read this module's source and claims nothing about its behaviour.** What is established is an **install state in one frozen extract**, and that **the estate is not homogeneous in its custom access-rights layer** — adjacent to the isolation controls the Boss non-degradation ruling protects.
>
> **Whether `DB-T2` is a deployment, a test restore or a clone is not determined by this evidence and is not asserted.** Routed open, not closed.

## 6. `P08-C4e` — the three-extract boundary, declared as a set

Four claims were **re-measured** on all four extracts. **Every other row reading *"all three databases"* was measured on three and has NOT been re-measured on `DB-T2`.** The two current `FACT VERIFIED` rows in that position are **named individually**, and the blind spot is stated as a set — `DB-T2` × {those two rows} — **not described**.

**They are not re-measured, and the reason is scope:** a state enumeration is not made *false* by a fourth extract, only **narrower than it looks**. Re-measuring it would be new research on an unchanged claim.

## 7. Clean-room — a leak made and caught inside this round

**The first draft of the `P08-C1` / `P08-C4` corrections wrote a module technical name, a registry table name and a restore-tool name into `58_`, which carried ZERO such tokens at its baseline.**

Found by a **mechanical token-count delta against `e368d11`**, not by reading. **Five tokens, one file, one commit — and `58_` is the file that goes to P11.** Scrubbed to zero; the same facts are stated in business terms and the identifiers live in the Layer 2 quarantine, which is now marked as such.

> **The scrub is not a formatting rule. `58_` is a handoff. Whatever it says travels.**

## 8. Self-test exit and standing limits

```
P08 OWNER CLOSURE COMPLETE — RC05 DELTA SELF-TEST PASS
```

**Owner self-test. Not independent certification.**

- **Four frozen extracts are NOT an established deployment census.** No corrected carrier says otherwise.
- **`P08-HO-13` stays *capability confirmed, execution NOT evidenced*.** Install state is capability, not act.
- The 2026-09-07 freeze assertion is **not** retroactively proven.
- No Veto discharged. No P11 mutation.
