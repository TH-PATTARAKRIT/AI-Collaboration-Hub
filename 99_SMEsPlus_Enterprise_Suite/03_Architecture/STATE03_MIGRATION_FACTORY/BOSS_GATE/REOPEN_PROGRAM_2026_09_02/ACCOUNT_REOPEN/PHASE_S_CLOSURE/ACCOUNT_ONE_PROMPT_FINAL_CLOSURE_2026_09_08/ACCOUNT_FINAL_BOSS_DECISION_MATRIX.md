# ACCOUNT_FINAL_BOSS_DECISION_MATRIX.md

**Prompt:** `[SMEPLUS-26-09-08-ACC-ONE-PROMPT-FINAL-CLOSURE-001]` · deliverable **10 of 12**
**Boss:** sole Final Approver · **Boss waits at the FINAL GATE**
**Surfaces:** P06 `a533fe9` · P08 `ca577be` · P09 `ab8c013` · P11 `79e1369` · P07 `ee2be30` READ-ONLY
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 0. What is asked of Boss, and what is not

**Four decisions and one gate instruction.** Nothing else in this package needs Boss.

> **Every question the Account team could answer from evidence has been answered.** The four below are **non-reversible decisions that materially change statutory compliance, accounting architecture, tenancy isolation, or approved business policy** — the only class the prompt permits to reach here. **No operational detail is asked. No "should we continue" is asked.**

---

## 1. The four decisions

### `BD-ACC-01` — Is accounting-event identity a platform property?

| | |
|---|---|
| **Class** | accounting architecture · **non-reversible** |
| **Why Boss** | it determines whether **eight** processes are given an identity or must each invent one. Evidence establishes the *absence*; it cannot establish the *choice* |
| **Evidence** | event identity is **absent as a platform property**; on the one channel that carries a candidate it is nullable and **unpopulated on 13,814 of 13,814**. The estate reliably carries the **posting act** and not the accounting event |
| **What it unblocks** | `G-01`, `G-04`, `G-11` — **one root under three Phase SA deltas** |
| **If deferred** | Phase SA proceeds by treating event identity, recognition trigger and period membership as **required inputs it must be given**. **Not a blocker. A carried constraint** |
| **Options** | **(a)** platform-owned identity, every process consumes it · **(b)** Account-owned, sources supply a correlation key · **(c)** defer, and carry the constraint into Phase SA explicitly |

### `BD-ACC-02` — May a tax-reporting grouping span companies, and under what security boundary?

| | |
|---|---|
| **Class** | **statutory compliance + tenancy isolation** · **non-reversible** |
| **Why Boss** | it is a **legal and security** determination. P07 routed it to reconciliation; **P11 registered it verbatim and refused to answer it** |
| **Evidence** | P07 `19_` §6 at `ee2be30`, content SHA-256 `482fc987…`, consumed read-only. **The evidence does not determine the answer** |
| **What it unblocks** | interface 8 (Thailand Tax), gap `G-12` |
| **If deferred** | **every non-statutory interface proceeds.** Only the statutory grouping attribute waits |
| **Options** | **(a)** grouping is company-scoped, no cross-company reporting entity · **(b)** cross-company grouping permitted under a named security boundary · **(c)** route to external legal/tax counsel before Phase SA |

### `BD-ACC-03` — The valuation-method policy decision

| | |
|---|---|
| **Class** | **approved business policy** · **non-reversible** |
| **Why Boss** | it is **one configuration decision with five downstream consequences**, and it is a **policy**, not a finding. **No further research changes it** |
| **Evidence** | one setting reaching **126 of 126** categories; conversion cost arriving at zero; the costing dependency HELD across prior rounds |
| **What it unblocks** | interfaces 3 and 4, gap `G-06` |
| **If deferred** | **costing-dependent outputs wait. The other nine interfaces do not** |
| **Options** | **(a)** decide the method now · **(b)** decide it at Phase SA entry with the two interfaces explicitly gated · **(c)** route to the finance-policy owner |

### `BD-ACC-04` — The `AAS+-VETO-01` identifier collision

| | |
|---|---|
| **Class** | **governance / veto integrity** · reversible, but **must not be left implicit** |
| **Why Boss** | **`AAS+-VETO-01` carries two different meanings** — P08's method veto and P09's scope veto — **in an unprefixed namespace. A discharge recorded against the bare identifier would not say which veto was discharged**, which is the exact failure the non-degradation ruling forbids. **Renaming another package's veto is a governance act, not a reconciliation act** |
| **Interim control already applied** | every Account citation is **producer-qualified**: `P08/AAS+-VETO-01`, `P09/AAS+-VETO-01` |
| **Options** | **(a)** ratify producer-qualified citation as the standing rule · **(b)** instruct the owning registers to renumber, preserving lineage · **(c)** rule that the collision is immaterial and record why |

---

## 2. The gate instruction

### `BD-ACC-GATE` — one final independent gate, and what it must cover

**Every remaining Account item requires structural independence, which no actor inside this execution possesses.** The gate must cover **exactly** this, and nothing more:

| # | What the gate must test | Why an owner cannot |
|---|---|---|
| 1 | fresh `RC-04` delta on P06's changed validation surface | the owner made the change |
| 2 | fresh `RC-01` delta on P09's four corrected surfaces | as above |
| 3 | fresh `RC-05` delta on P08's changed population/namespace/provenance surfaces **and the newly published run** | a newly published run must be independently re-executed |
| 4 | fresh `RC-06` delta on P11's propagation | as above |
| 5 | **`B-35` certification against the full twelve-control set including `S06`** | **the certifier must not be the author** — this is the single largest item |
| 6 | whether `B-37`'s repair closes it | closing one's own registered blocker is the practice this programme ruled against |
| 7 | whether `AASP-VETO-06`'s delivery limb is satisfied now that P11 has recorded receipt | delivery is a two-party fact |

**`RC-02` and `RC-03` are not reopened** — no Account correction in this prompt changed their validated surfaces.

---

## 3. Conformance against the Boss non-degradation acceptance test

| # | Acceptance test | Evidence |
|---|---|---|
| 1 | every authorised item completed, superseded with evidence, or carried as an exact external dependency | all five embedded correction prompts executed; every carry is named with an owner and a smallest next action |
| 2 | **no prior accepted finding disappeared** | zero findings withdrawn without evidence. **Six new findings were added** — `VER-E-06`, `VER-E-07`, `P08-F-NEW-01`, `XR-03`, `XR-05`, the cwd-dependence defect |
| 3 | **no evidence requirement replaced by narrative** | every count re-executed; commands and outputs published; a **falsified** prediction published as falsified |
| 4 | no Gate skipped | **zero vetoes discharged**; the independent gate is reserved, not absorbed |
| 5 | **no Veto silently discharged** | 0 discharged. **`XR-05` raised precisely because an identifier collision could make a discharge silent** |
| 6 | no cross-package dependency lost | one reconciliation executed over all four final SHAs; **P07 consumed read-only and unmutated** |
| 7 | **all changed material surfaces tested** | P06 two shapes + four controls · P08 nine controls scored, 1 falsified, 1 broken-then-repaired · P09 `q1` re-executed byte-identical + sweep controls · P11 four controls + a run-location control |
| 8 | Phase SA I/O clarity **equal or stronger** | eleven interfaces classified individually; **21 semantic elements** with direction and owner; **twelve gaps each with an owner and a smallest next action**; **the prior global HOLD posture is replaced by nine usable interfaces** |
| 9 | historical evidence traceable | every supersession is **struck in place with the original preserved**; nothing deleted |
| 10 | Boss can reconstruct every disposition | each carries its finding id, its executed evidence and its owner |

**Item 8 is the one that changed most. The prior posture blocked the programme on Account as a whole; this package blocks it on two named attributes.**

---

## 4. What Boss is NOT asked to approve

- **No merge, release, production, or implementation authorisation.**
- **No Phase A / B / C, no Functional Design, no Phase SA design.**
- **No veto discharge** — zero are recommended for discharge.
- **No adjudication between two parallel evidence tracks.**
- **No approval of the Account package as complete.** It is not complete; **it is ready for one independent gate.**

---

## 5. Recommendation to Boss

> **Send the package to the one final independent gate defined in `BD-ACC-GATE`.**
> **Decide `BD-ACC-01`…`BD-ACC-04` on the gate's report, or earlier if `BD-ACC-03` is wanted sooner — it is a policy decision and needs no further evidence.**
> **Do not hold the rest of the programme.** Nine of eleven Account interfaces are usable now; the two that are not are waiting on **`BD-ACC-02`** and **`BD-ACC-03`**, which are decisions, not research.
