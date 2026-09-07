# 08 — POST-`RC` CROSS-PACKAGE VERIFICATION

> **§6 opens *"after all six RCs have terminal results."* They have terminal results — all six are
> `RC-HOLD`. But most §6 sweeps take an RC outcome as input, and there are none. Each sweep below is
> therefore marked EXECUTED, PARTIAL or NOT REACHABLE, with the reason. Nothing is scored on the
> absence of an input.**

## 1. Sweep register

| # | Sweep (§6) | State | Result |
|---|---|---|---|
| 1 | withdrawn/superseded claims still consumed as current | **PARTIAL** | §2 |
| 2 | stale SHA / currentness references | **PARTIAL** | §3 |
| 3 | handoff sent vs handoff received | **NOT REACHABLE** | the P06→P11 and P08→P11 receipt records are the substance of `RC-02`/`RC-04`/`RC-06`. Testing them here **is** those RCs, by another name |
| 4 | duplicate root defects vs manifestations | **NOT REACHABLE** | requires per-RC dispositions |
| 5 | contradiction propagation | **NOT REACHABLE** | the 6 live edges recorded at `XRD-011` resolve on RC outcomes |
| 6 | producer-qualified namespaces | **NOT REACHABLE** | `Q-P11-02`'s sweep is inside `RC-02` |
| 7 | P07 read-only closure impact | **EXECUTED** | §4 |
| 8 | Veto lifting dependencies | **EXECUTED** | `09_` |
| 9 | Boss-only decision dependencies | **EXECUTED** | `09_` §3 |
| — | *(added by this session)* manifest coverage-assertion shape across the correction SHAs | **EXECUTED** | `07_` §4 — **2 live instances found** |

**3 executed · 2 partial · 4 not reachable · 1 added.** The four not-reachable sweeps are blocked by
the same missing executor as the six RCs, **not by missing evidence.**

## 2. Sweep 1 — superseded claims consumed as current

| Claim | Where it stands | Current? | Action |
|---|---|---|---|
| `IV-PRECONDITION-HOLD — VERIFIER HANDOFF NOT COMPLETE`, `audit/account-phase-s-iv-rc-2026-09-07-001` @ `9d8ad70` | correct when written; `0941161` published afterwards | **NO — superseded** | **withdrawn as the current state by `00_` §1.** Lineage preserved; the commit is not rewritten |
| *"the `RC-04` surface does not exist"* (prior IV report) | contradicted at `b5f5a21` — the ref carries `G02_OWNER_CORRECTION_2026_09_07/` with 2 files, and the commit changes 8 | **NO — false at the frozen ref** | recorded in `06_` §3 |
| Live citations of `IV-PRECONDITION-HOLD` at `0941161` | **1** — `NEXT_PROMPT_CHATGPT_…_2026_09_07.md`, a **dispatch prompt** quoting it as the stop-condition to test, not asserting it | **N/A — not a carrier** | none |

**No live artefact was found asserting either superseded claim as current.** Population: files at
`0941161` matching `IV-PRECONDITION-HOLD`. **PATTERN and PATH SET are narrow and declared as such** —
this is not a claim that no such carrier exists anywhere in the repository.

## 3. Sweep 2 — stale SHA / currentness

| Reference | Asserted | Measured now | Verdict |
|---|---|---|---|
| 6 `corr/*` frozen heads | per handoff matrix | **6 of 6 MATCH**, full 40-char, from `git ls-remote` | **CURRENT** |
| `002748d`, `c7cfd8a` base refs | present, not rewritten | present | **CURRENT** |
| `REMEDIATION-A` @ `0941161` | remediation branch head | matches remote | **CURRENT** |
| Closeout SHA `09128a9` cited by the remediation dispatch | dispatch asserts it as head | remote head is `2e2b8de` | **STALE — already classified by the remediation session** as ancestor / fast-forward / 3 commits / additions only / governance only. **Independently re-checked here: `09128a9` is an ancestor of `2e2b8de`.** Non-material |

**Not swept:** the 3 peer SHAs pinned at CORR2 heads in P11's outbound registers (`XRD-005`). Those
sit inside `RC-02`'s surface. **Declared unswept.**

## 4. Sweep 7 — P07 read-only closure impact

| Check | Result |
|---|---|
| P07 branch head | `research/account-p07-th-tax-compliance-2026-09-04-001` = `ee2be30ebf155e241510b3c7133c69419eb060a0` |
| Moved since criterion 8 was assessed? | **NO** — `ee2be30`, the same SHA the closure register records |
| P07 artefact opened by this session | **none** |
| P07 mutation required for closure | **not at present** |

**Criterion 8's standing caveat is unchanged and still live:** if `Q-P11-02`'s producer-qualification
sweep or `B-39`'s generation question resolves such that a **P07 artefact itself** publishes the
defect, P07 mutation becomes mandatory and the recommendation becomes
`PHASE S HOLD — P07 OWNER ACTION REQUIRED`. **`Q-P11-02` sits inside `RC-02`, which is on HOLD.**
So criterion 8 passes **now** and is **re-evaluable, not settled** — and this session cannot settle it.

## 5. What a cross-package sweep cannot do here

Four of the nine sweeps exist to catch defects that only become visible **once RC dispositions exist**.
Running them against a package with zero dispositions returns clean, and **a clean result from a sweep
with no input is not evidence of anything**. They are marked NOT REACHABLE rather than run and reported
as clean, deliberately.
