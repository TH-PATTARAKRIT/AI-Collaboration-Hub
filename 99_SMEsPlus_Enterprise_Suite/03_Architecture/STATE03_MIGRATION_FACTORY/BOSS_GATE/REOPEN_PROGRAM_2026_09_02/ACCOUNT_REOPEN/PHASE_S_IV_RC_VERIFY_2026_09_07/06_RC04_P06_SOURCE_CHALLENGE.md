# 06 — `RC-04` (P06 source) — INDEPENDENT CHALLENGE

**Verifier session** `[SMEPLUS-26-09-07-ACC-PHASE-S-INDEPENDENT-RC-VERIFY-001]` · branch `audit/account-phase-s-iv-rc-verify-2026-09-07-001`
**Executing model:** Claude Opus 5 · **Appointed verifier:** ChatGPT GPT-5.6 Sol

## 1. Exact scope restated before testing (§4.A)

Bounded to `corr/p06-source-phase-s-final-2026-09-07-001` @ `b5f5a21`:
`G02_OWNER_CORRECTION_2026_09_07/` including `P06_TO_P11_COUNT_CORRECTION_NOTICE.md`.
Scope: `Q-P06-03`, `Q-P06-04`, the re-issued `Q-P06-02`, the corrected count families,
`P06-B-58` scaling, and the archive-negative instrument.
**Not in scope:** unrelated P06 findings — they may not be reopened here.

## 2. Result

```
RC-04 = RC-HOLD — STRUCTURAL INDEPENDENCE NOT PROVEN
```

**Reason:** `Q-BOSS-02` §1 controls 1 and 2 fail for this executor. The repair at `b5f5a21` carries
`Co-Authored-By: Claude Opus 5`. Per `Q-BOSS-01` §2, a challenge run by the model that authored the
repair does not satisfy `RC-*`. **No falsification attempted; see `00_` §3.**

## 3. Readiness verified (does NOT certify this RC)

| Check | Result |
|---|---|
| Frozen ref head == asserted SHA | `corr/p06-source-phase-s-final-2026-09-07-001` = `b5f5a211763568a4212d08954c835412f7728a0a` — **MATCH** |
| External inputs required | **none** — repository-only surface |
| Surface exists | **YES.** A prior IV report stated the `RC-04` surface did not exist; the frozen ref is present and carries the correction directory. **That prior negative is superseded** |
| Declared unrepaired row | the `:45` row is **unrepaired at this SHA by design** and **contradicts `:54`**. Declared by the owner, not concealed — the challenger must test it, not discover it |

### 3.1 Declared surface ≠ changed surface — `IV-R-01/RC-04`, **MATERIAL — the widest of the five**

The matrix declares the `RC-04` surface as *"`G02_OWNER_CORRECTION_2026_09_07/`, incl.
`P06_TO_P11_COUNT_CORRECTION_NOTICE.md`"*. That directory holds **2 files** at `b5f5a21`.
`git show --name-only b5f5a21` changes **8**.

| Inside the declared directory (2) | Outside it, and changed anyway (6) |
|---|---|
| `G02_OWNER_CORRECTION_2026_09_07/P06_Q_P06_03_04_EXECUTION_RECORD.md` (+106) | `13_P06_EVIDENCE_MANIFEST.md` |
| `G02_OWNER_CORRECTION_2026_09_07/P06_TO_P11_COUNT_CORRECTION_NOTICE.md` (+55) | `18_P06_CORE_RECON_HANDOFF_PACK.md` |
| | `40_P06_TARGETED_BLOCKER_REGISTER.md` |
| | `46_P06_55_BLOCKER_SEVERITY_REGISTER.md` |
| | `56_P06_FILTERED_TREE_EVIDENCE_BOUNDARY.md` (**largest edit, 22 lines**) |
| | `70_P06_P11_SUPPLEMENTAL_CRITICAL_RISK_HANDOFF.md` |

All six sit directly under
`…/PROCESS_DEEP_RESEARCH_2026_09_04/P06_BANK_TO_RECONCILE_EXECUTION/`.
**6 of 8 changed files fall outside the declared surface — 75%.**

**Why it is material:** the excluded set is exactly where the corrected *counts* landed — the evidence
manifest, two blocker registers, the filtered-tree evidence boundary — **and two outbound handoff
artefacts to P11** (`18_`, `70_`). `RC-04`'s own mandate is corrected count families and `P06-B-58`
scaling; a challenger bounded to `G02_/` would test the correction **notice** and never the registers
the correction was applied to, and would miss two changed outbound artefacts — the precise class §6
cross-package verification exists to catch.

**Routed to the owner:** declare the `RC-04` surface as the enumerated changed set. Not edited here.

**One instance of `IV-R-01`, measured in all five lanes in `07_` §3.** The check **fires in all five**,
including `RC-05`, so it has **no passing control** and is weak as a discriminator; `07_` §3 therefore
ranks the lanes **by magnitude** rather than treating them alike. This session does not call
`RC-05`'s single-file miss material.

## 4. Findings

**None issued.** Absence of findings is absence of testing. Under §2.10 it may not be read as a
discharge of anything.

## 5. What the appointed verifier must still do

Verify the corrected count families and `P06-B-58` scaling with **two independently shaped counts**.
For the **archive-negative instrument**, the decisive control is a **pattern proven to fire**: run a
positive control inside the same population and, where feasible, a **synthetic injection** taking the
count from 0 to 1 — a negative from a predicate that cannot fire is indistinguishable from absence.
Then adjudicate the declared `:45`/`:54` contradiction on the evidence, without widening into
unrelated P06 findings.
