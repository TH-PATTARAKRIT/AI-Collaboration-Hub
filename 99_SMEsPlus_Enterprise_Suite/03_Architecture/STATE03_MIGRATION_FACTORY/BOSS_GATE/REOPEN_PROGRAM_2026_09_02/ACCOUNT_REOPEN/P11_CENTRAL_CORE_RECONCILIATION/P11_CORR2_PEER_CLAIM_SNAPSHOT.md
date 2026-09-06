# P11 — CORR2 FROZEN PEER CLAIM SNAPSHOT

`[SMEPLUS-26-09-06-ACC-P11-CORE-RECON-CORR2-PHASES-001]` · `CP-P11C2-01` · **PHASE S** · Layer 1 clean-room

> **FROZEN `2026-09-06`.** Peer heads resolved **once**, at CORR2 bootstrap. **P11 does not chase moving
> peer heads after this point.** Anything published by a peer after these SHAs is recorded as
> `POST-SNAPSHOT MATERIAL DELTA CANDIDATE` and does **not** widen this run.

---

## 1. Frozen peer heads — every one of the ten moved since CORR1

| Peer | Branch | CORR1 SHA | **CORR2 FROZEN SHA** | Moved |
|---|---|---|---|---|
| `P01` Procure-to-Pay | `research/account-p01-procure-to-pay-2026-09-04-001` | `49d0fe3` | **`b820b29`** | ✔ |
| `P02` Order-to-Cash | `research/account-p02-order-to-cash-2026-09-04-001` | `06c5ed8` | **`7cb1c27`** | ✔ |
| `P03` Manufacture-to-Cost | `research/account-p03-manufacture-to-cost-2026-09-04-001` | `7fca09a` | **`bc767a8`** | ✔ |
| `P04` Acquire-to-Retire | `research/account-p04-acquire-to-retire-2026-09-04-001` | `c57d846` | **`65b8841`** | ✔ |
| `P05` Expense-to-Pay | `research/account-p05-expense-to-pay-2026-09-04-001` | `808b30e` | **`205e0ac`** | ✔ |
| `P06` Bank-to-Reconcile | `research/account-p06-bank-to-reconcile-2026-09-04-001` | `9e5d729` | **`249b7c2`** | ✔ |
| `P07` Tax-to-Compliance | `research/account-p07-th-tax-compliance-2026-09-04-001` | `547b774` | **`ee2be30`** | ✔ |
| `P08` Record-to-Report | `research/account-p08-record-to-report-2026-09-04-001` | `838134f` | **`194efcb`** | ✔ |
| `P09` Plan-to-Analyze | `research/account-p09-plan-to-analyze-2026-09-04-001` | `c029df3` | **`5441f8d`** | ✔ |
| `P10` Time-Based Recognition | `research/account-p10-time-based-recognition-2026-09-04-001` | `284ea66` | **`1fea562`** | ✔ |

**`10 of 10` moved.** CORR1's peer table was stale in every row within 24 hours. This is the structural
argument for a **frozen snapshot** rather than a rolling read: a rolling read is never current and
cannot be audited, because the thing it was current against no longer exists.

## 2. Declared denominator for the artefact enumeration

| Element | Declaration |
|---|---|
| **POPULATION** | Every `*.md` in each peer's tree at its frozen SHA |
| **PATH SET** | **The whole tree.** Not the peer's package directory — that assumption produced three consecutive false empties (§2.1) |
| **PATTERN** | basename contains the peer id **AND** one of `CORE_RECON` · `P11` · `POST_PUBLICATION` · `CORRECTION` · `SUPERSED` · `WITHDRAW` |
| **UNIT** | **one path = one artefact** |
| **POSITIVE CONTROL** | five artefacts known to exist must all return: `52_P08…_V2`, `71_P10…`, `70_P06_P11…`, `37_P03_SCOPE02_P11…`, `S23_P09_POST_PUBLICATION_CORRECTION`. **Result: 5 of 5.** |
| **NEGATIVE CONTROL** | P11's own directory must not appear. **Result: 0.** |
| **DECLARED BLIND SPOT** | a peer correction whose basename carries **neither** the peer id nor any of the six tokens is **not** in this population. No such artefact is known; none is excluded by claim |

### 2.1 The instrument failed three times and each failure was caught by a control

| # | Assumption | Failure | Caught by |
|---|---|---|---|
| 1 | pattern `HANDOFF\|CORE_RECON\|…` over the whole tree | returned adjacent-package artefacts the prompt forbids rediscovering — **too wide** | inspection of output |
| 2 | PATH SET = `ACCOUNT_REOPEN/*<PEER>*/` | **P01, P02, P03, P06 returned empty** — their package directories are not under `ACCOUNT_REOPEN` and are not named for the peer | prior knowledge that ≥4 of those empties were false |
| 3 | directory bound `/<DIR>` | **P09 `S23` not returned** — its directory is `ACCOUNT_P09_…`, so the leading `/` never matched | the 5-item positive control |

> **Three false results, all zero-shaped, all in the direction of "less work to do".** Not one was
> caught by reading the output; each was caught by a control that named a specific artefact in advance.
> **`P11-E-35`.**

## 3. Frozen artefact population — `47` candidates, `12` addressed to P11

**Only the P11-addressed set is consumed in CORR2.** The remaining 35 are the peers' internal
correction records; reading them would be `adjacent Pxx full-package rediscovery`, which §14 of the
controlling prompt forbids by default.

| Peer | P11-addressed artefacts at the frozen SHA | New since CORR1 |
|---|---|---|
| `P01` | `P01_TO_P11_HANDOFF.md` · `P01_P11_EVIDENCE_VERSION_DEPLOYMENT_SUPPLEMENT.md` · `P01_P11_S18_DIRECT_VERIFICATION_SUPPLEMENT.md` · `P01_S16_P11_HANDOFF.md` | **4 of 4** |
| `P02` | *(none addressed to P11; `19_` core-recon pack only)* | — |
| `P03` | `P03_TO_P11_HANDOFF.md` · `73_P03_P11_RUNTIME_INVERSION_SUPPLEMENT.md` · `37_P03_SCOPE02_P11_HANDOFF.md` | **2 of 3** |
| `P04` | `P04_TO_P11_HANDOFF.md` | **1 of 1** |
| `P05` | `65_P05_P11_EVIDENCE_BASE_AND_LIVE_RISK_SUPPLEMENT.md` | **1 of 1** |
| `P06` | `70_P06_P11_SUPPLEMENTAL_CRITICAL_RISK_HANDOFF.md` | consumed CORR1 |
| `P07` | *(none addressed to P11)* | — |
| `P08` | `58_P08_P11_RECONCILIATION_BOUNDARY_HANDOFF.md` | **1 of 1** |
| `P09` | `D23_P09_P11_DENOMINATOR_SIGN_PLATFORM_SUPPLEMENT.md` · `S18_…` · `S23_…` · `D25_P09_CHALLENGE_CORRECTION.md` | **2 of 4** |
| `P10` | `P10_TO_P11_HANDOFF.md` · `41_P10_P11_DECISION_INTEGRITY_CORRECTION.md` · `71_…` | **2 of 3** |

> **13 P11-addressed artefacts new since CORR1, from 7 peers.** CORR1 closed 20 hours before this
> snapshot was taken. **The peer surface P11 reconciles is not stable at the timescale P11 works at**,
> which is the whole justification for `POST-SNAPSHOT MATERIAL DELTA CANDIDATE` as a disposition.

## 4. Post-snapshot handling

Nothing was published by any peer between snapshot resolution and this file. **`POST-SNAPSHOT MATERIAL
DELTA CANDIDATES: NONE at freeze time.`** Any later peer commit is out of scope for CORR2 and reopens
only the affected `CQ` in a future targeted delta.

**`CP-P11C2-01` — COMPLETE — EVIDENCE VERIFIED.**
