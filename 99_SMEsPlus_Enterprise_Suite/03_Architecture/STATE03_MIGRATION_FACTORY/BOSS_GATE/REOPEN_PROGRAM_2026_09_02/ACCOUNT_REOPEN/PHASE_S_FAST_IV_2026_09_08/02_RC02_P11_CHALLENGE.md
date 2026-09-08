# 02 — `RC-02` P11 CHALLENGE

**Frozen surface** `corr/p11-phase-s-remediation-2026-09-07-001` @ `9d4ecdc744fbbb0e502a0b907f59c301bdf7812c`
**Lane** A — repository-only, prompt §4 says start immediately
**Result** `RC-HOLD — REQUIRED EVIDENCE OR INDEPENDENCE UNAVAILABLE`
**Cause** independence only. **The evidence is complete and the lane is executable today.**

## 1. Exact scope restated before testing (prompt §6)

Test `CO-F-01`, `CO-F-02`, `Q-P11-01`, `Q-P11-02`, `Q-P11-03` against the **repaired instrument**:
test the repair itself and not only the original defect; change pin/control input and prove the
instrument reacts or fails closed; prove the immutable pins are actually consumed; compare **member
identity**, not count; independently reproduce the **214-vs-214 one-out/one-in** set difference;
verify no moving `origin/<branch>` head silently substitutes for a declared pin; preserve `P11-E-49`
as a registered lead unless closure criteria require a bounded cross-package sweep.

## 2. Not run

`RC-02` was **NOT RUN**. `intake_derivations_pinned.py` was not executed, no pin sensitivity was
exercised, and the 214-vs-214 set difference was **not** reproduced. `CO-F-01` remains an untested
lead exactly as the handoff §3 offers it: *"Reproduce the one-out/one-in independently before
believing it."*

## 3. Input-locality determination — this lane needs no host (executor-neutral)

Read from the frozen ref, this is a **feasibility** fact about the lane, not a verdict on the repair.

| Probe | Command | Result |
|---|---|---|
| Absolute host paths in the instrument | grep `/Users/` `/Volumes/` in `9d4ecdc:…/corr3_instrument/intake_derivations_pinned.py` | **none** |
| Network access | grep `http`, `requests` | **none** |
| External processes | `subprocess.run` call sites, lines 59, 65, 67, 74, 80, 91 | **`git` only** — `rev-parse`, `merge-base --is-ancestor`, `log`, `ls-tree`, `grep`, `rev-parse --show-toplevel` |
| Writes | line 108–109, `open(os.environ.get("P11_UNION_OUT","union_pinned.txt"),"w")` | one output file in cwd; **no owner artefact written** |

**`RC-02` requires a clone of this repository and nothing else.** No database, no source tree, no
host-local file. It is executable by any eligible verifier with git and Python, immediately.

## 4. Consequence

This is the evidentiary basis for **`IV2-F-01`** (`07_`): `RC-02` was placed on an
execution-environment hold at `9a5699e` that **cannot apply to it**.
