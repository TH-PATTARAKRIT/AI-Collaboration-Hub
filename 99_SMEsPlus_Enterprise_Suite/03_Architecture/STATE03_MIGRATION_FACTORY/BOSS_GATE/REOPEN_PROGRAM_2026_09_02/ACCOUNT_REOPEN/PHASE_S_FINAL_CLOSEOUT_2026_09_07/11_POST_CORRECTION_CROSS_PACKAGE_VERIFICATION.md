# 11_POST_CORRECTION_CROSS_PACKAGE_VERIFICATION

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-FINAL-CLOSEOUT-001]`
**Classification** LAYER 2 — AUDIT QUARANTINE

## 0. Instrument, declared before results

| | |
|---|---|
| **POPULATION** | every `*.md` under each package's own root, at that package's frozen correction SHA |
| **PATTERN** | published per sweep below, as an ERE, with the command |
| **PATH SET** | the six roots in §1 — **each package's own root, not the branch** |
| **UNIT** | one matching line, reported as `total` and as `LIVE` (= not struck through with `~~`) |

**Two instrument defects were found and corrected before any result below was accepted:**

1. **The first positive control returned 0 on two populations.** `Phase S` is case-sensitive and P06
   writes `PHASE S`. The control, not the instrument, was broken. Re-run case-insensitively it returns
   `9 / 2 / 20 / 3 / 76 / 44` — non-zero on all six.
2. **The first sweep scoped by BRANCH, not by package root.** Every `corr/*` branch contains the entire
   repository (~1,050 `.md` files), so "hits on the P06 branch" included P11's files. **Every count in
   the first pass was wrong.** Rescoped to the six roots below.

Both are recorded because the results would have been published as clean had the controls not fired.

## 1. Path set and per-package denominators

| Package | Frozen SHA | Root | `.md` files |
|---|---|---|---|
| P06 source | `b5f5a21` | `…/PROCESS_DEEP_RESEARCH_2026_09_04/P06_BANK_TO_RECONCILE_EXECUTION` | **89** |
| P06 IEV | `692ea27` | `…/INDEPENDENT_REVIEW/P06_BANK_TO_RECONCILE/IEV_006` | **10** |
| P08 source | `c7cfd8a` | `…/ACCOUNT_REOPEN/ACCOUNT_P08_RECORD_TO_REPORT` | **73** |
| P08 IEV | `d685176` | `…/ACCOUNT_REOPEN/P08_INDEPENDENT_VERIFICATION_2026_09_06` | **8** |
| P09 | `2079a25` | `…/ACCOUNT_REOPEN/ACCOUNT_P09_PLAN_TO_ANALYZE` | **136** |
| P11 | `002748d` | `…/ACCOUNT_REOPEN/P11_CENTRAL_CORE_RECONCILIATION` | **81** |

Controls, all six populations: **positive fires everywhere; negative (`ZZQQ_IMPOSSIBLE_9931`) returns 0 everywhere.**

## 2. Sweep results

| # | Check | Result |
|---|---|---|
| **S1** | Stale / bookkeeping-vs-substantive SHA confusion | **3 found — all in the dispatching prompt, none in the packages.** See `16_` §3. P09's `2079a25`→`150a033` movement is confirmed bookkeeping-only (2 files: manifest + resume pointer) |
| **S2** | P06 `"65 blockers"` still asserted as current | **0 live claims.** 7 P06-source + 3 P06-IEV hits, **every one inside a correction record quoting the old figure beside the new**, or a notification to P11. Authoritative count **67**, re-verified here (§3) |
| **S3** | P06 IEV `"18 / 25 material defects"` current | **0 live claims.** 1 hit, in the `Q-P06-01` execution record's own before/after table |
| **S4** | P08's withdrawn no-referent `"3 at 1e-7"` figure consumed as current | **0 live claims.** 4 P08 + 5 P08-IEV + 4 P11 hits, **all quotations inside contradiction / correction / withdrawal records**. `58_` now states the tolerance-independent result |
| **S5** | Withdrawn P11 method rule consumed as current | **0 live claims.** 3 occurrences, 2 struck through, 1 narrative in the revision log |
| **S6** | Bare `HO-13` / `HO-14` (unqualified peer id) | **P11's claim of 0 bare in the live CORR3 surface HOLDS.** 4 hits: 3 are the correction record documenting the repair; 1 is `P11_UNIFIED_BUSINESS_EVENT_REGISTER.md`:46, **which P11 itself declared as `UNRESOLVED — NAMESPACE` residue.** A declared blind spot, correctly declared |
| **S7** | P06 `"three vetoes"` / `"four active vetoes"` | **0 live claims.** Authoritative: **seven** (`AASP-VETO-01…07`) |
| **S8** | P08 → P11 notification received and reflected | **FAILED — `CO-F-02`.** §4 |
| **S9** | P09 / P11 peer currentness | **FAILED — `CO-F-01`, `CO-F-02`.** §4 |
| **S10** | Duplicate defect ids / namespace collisions | **LATENT, one family tested clean.** §5 |
| **S11** | Unresolved contradictions | **1 found inside a single commit — `CO-F-01` §4.4.** §4 |
| **S12** | P07 read-only dependencies | **NO CLOSURE IMPACT.** §6 |
| **S13** | Open veto lifting dependencies | 17 standing, 0 discharged. `12_` |
| **S14** | Boss-only decisions still open | 51 domain + 0 unanswered control. `13_` |

## 3. P06 count propagation — re-verified independently, not adopted

```
POPULATION  every *.md under the P06 source root at b5f5a21  (89 files)
UNIT        one distinct P06-B-nn identifier
FORM 1  git grep -oh -E 'P06-B-[0-9]+' … | sort -u -V | wc -l      → 67
FORM 2  python re.findall(r'P06-B-\d+') over each file's bytes      → 67   SET IDENTITY: same
CONTIGUITY  min 1 · max 67 · distinct 67 · gaps NONE
POSITIVE CONTROL  P06-B-50 → 26 occurrences
NEGATIVE CONTROL  P06-B-68 → 0     ·  P06-B-99 → 0
```

**67 confirmed.** P06's `Q-P06-03` figure stands on independent re-execution.

**One row is deliberately NOT repaired:** `G02_RECOVERY_2026_09_06/P06_VERIFICATION_TOOL_DEFECT_REGISTER.md`:45
still reads `65 … max id = 65 and contiguous … YES`, self-contradicted by `:54`. **That row is the target
of the re-issued `Q-P06-02` (`09_` §3); repairing it here would execute an item this session re-issued.**

## 4. The two cross-package failures

### `CO-F-02` — P11 holds two stale inbound negatives *(S8, S9)*

| Inbound | Published at | P11's record at `002748d` |
|---|---|---|
| P08 `Q-P08-01` notification `64_P08_NOTIFICATION_TO_P11_Q_P08_01.md` | `c7cfd8a`, **09:05:24** | *"Not received"* (`P11_AUTO_RESUME_STATE.md`:101) and *"Not yet received"* (`P11_OWNER_BOUNDED_CORRECTION_2026_09_07.md`:112) |
| P06 `P06_TO_P11_COUNT_CORRECTION_NOTICE.md` | `b5f5a21`, **09:11:29** | not consumed — P11's last commit is 09:09:56 |

The P08 notification existed **2 minutes before P11's first correction commit** and 4½ before its last.
The P06 notice postdates P11 entirely, so P11's P06-derived figures (65 blockers, three/four vetoes) are
stale by construction.

**Both are receipt-side and correctable without re-opening research. Routed to P11. Not repaired here** —
editing P11 from this session is peer-owner mutation.

### `CO-F-01` — P11's denominator is non-deterministic *(S9, S11)*

Full reproduction in `09_` §4. Cross-package consequences:

- **P11's declared P08 pin `00ccd66` and its executed P08 membership disagree.** The published union
  contains `64_P08_NOTIFICATION…` (exists only at `c7cfd8a`) and drops `59_P08_METHOD_AND_REQUIREMENT_REGISTER`
  (exists at both). **A P08 correction commit silently changed P11's denominator.**
- **`S11`:** one commit publishes a fact and its negation — the revision log says *"union 212 unchanged"*,
  the correction record and the regenerated file say **214**.
- The denominator returns **216** today and moves whenever any of ten peer branches moves.

## 5. Namespace exposure — measured, and correctly classified as latent *(S10)*

Bare, producer-unqualified short identifier families, distinct ids per package:

| Family | P06src | P06iev | P08 | P08iev | P09 | P11 |
|---|---|---|---|---|---|---|
| `B-` | 76 | 14 | 9 | — | 13 | 40 |
| `F-` | 20 | 1 | 4 | — | — | 14 |
| `D-` | 23 | 1 | 3 | — | 5 | 24 |
| `M-` | — | — | 7 | — | 2 | 7 |
| `L-` | — | — | 1 | — | 8 | 6 |
| `HO-` | 6 | 2 | 6 | 14 | — | 12 |
| `CI-` | — | — | — | — | 6 | 15 |
| `T0-` | 1 | — | 7 | — | — | 16 |

**Family overlap is not collision.** A discriminating test was run on `M-`, the family most likely to
fire (P09's `M-1`/`M-2` are consumed by P11's `B-38`):

```
P08's family is ZERO-PADDED : M-01 M-02 M-03 M-04 M-05 M-06 M-07
P09's family is UNPADDED    : M-1  M-2
→ lexically disjoint; 'M-1' cannot match 'M-01'
P11's 4 citations of M-1/M-2 all attribute to P09 IN THE SAME SENTENCE
```

**Result: no live collision in `M-`.** The one family where a live collision *was* demonstrated (`HO-`)
was found and repaired by `Q-P08-02` / `Q-P11-02`.

> **Disposition: LATENT EXPOSURE, NOT A DEFECT.** One of eight families tested and clean; six untested.
> **Severity is not ranked, because reachability has not been measured for the untested six.** Routed to
> the independent verifier as a bounded check, not asserted as a defect.

## 6. P07 read-only dependencies — no closure impact *(S12)*

```
P07 branch head, read from remote: ee2be30ebf155e241510b3c7133c69419eb060a0
P11's instrument pins P07 at     : ee2be30
→ P07 HAS NOT MOVED. No freshness exposure from P07 in any package.
```

P07 is referenced by 32 / 1 / 18 / 1 / 16 / 47 files across the six packages, and stands at
`RECOMMEND HOLD, 0 of 8, no blocker closed`. **That HOLD is inherited standing context, not a Phase S
closure blocker**, and no Phase S conclusion is gated on a P07 result. **P07 was not opened, not edited
and not re-read beyond its head SHA and its standing terminal state.**
