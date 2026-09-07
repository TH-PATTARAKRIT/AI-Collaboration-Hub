# 05 — `RC-03` (P06 IEV) — INDEPENDENT CHALLENGE

**Verifier session** `[SMEPLUS-26-09-07-ACC-PHASE-S-INDEPENDENT-RC-VERIFY-001]` · branch `audit/account-phase-s-iv-rc-verify-2026-09-07-001`
**Executing model:** Claude Opus 5 · **Appointed verifier:** ChatGPT GPT-5.6 Sol

## 1. Exact scope restated before testing (§4.A)

Bounded to `corr/p06-iev-phase-s-final-2026-09-07-001` @ `692ea27`:
`IEV_006/P06_Q_P06_01_02_EXECUTION_RECORD.md` plus 4 registers. Inputs: **repository only.**
Surface: the revised population/denominator and enumeration, including the **26-vs-25** adjudication
and the revised totals.

## 2. Result

```
RC-03 = RC-HOLD — STRUCTURAL INDEPENDENCE NOT PROVEN
```

**Reason:** `Q-BOSS-02` §1 controls 1 and 2 fail for this executor. The repair at `692ea27` carries
`Co-Authored-By: Claude Opus 5`. Per `Q-BOSS-01` §2, a challenge run by the model that authored the
repair does not satisfy `RC-*`. **No falsification attempted; see `00_` §3.**

## 3. Readiness verified (does NOT certify this RC)

| Check | Result |
|---|---|
| Frozen ref head == asserted SHA | `corr/p06-iev-phase-s-final-2026-09-07-001` = `692ea27e11533bc72ef0123fa4d1e3524179bf6e` — **MATCH** |
| External inputs required | **none** — repository-only surface |
| Known trap declared by the owner | **YES** — the naive count returns **27**; the extra member is the documented negative-control token **matching its own documentation**. The adjudicated figure is **26** |

### 3.1 Declared surface ≠ changed surface — `IV-R-01/RC-03`, **MATERIAL**

The matrix declares the `RC-03` surface as *"`IEV_006/P06_Q_P06_01_02_EXECUTION_RECORD.md` + 4
registers"* — **5 files by description.** `git show --name-only 692ea27` changes **7 files**.

| Set | Members |
|---|---|
| Declared (execution record + the 4 `IEV_006` files named `*REGISTER*`) | `P06_Q_P06_01_02_EXECUTION_RECORD.md` · `P06_CLAIM_CLASS_POPULATION_REGISTER.md` · `P06_INDEPENDENT_CHECKPOINT_REGISTER.md` · `P06_INDEPENDENT_CORRECTION_VERIFICATION_REGISTER.md` · `P06_VERIFICATION_INSTRUMENT_CONTROL_REGISTER.md` |
| Actually changed at `692ea27` | `P06_Q_P06_01_02_EXECUTION_RECORD.md` (+106) · `P06_INDEPENDENT_AAS03_CHALLENGE.md` · `P06_INDEPENDENT_AUTO_RESUME_STATE.md` · `P06_INDEPENDENT_CHECKPOINT_REGISTER.md` · `P06_INDEPENDENT_CORRECTION_VERIFICATION_REGISTER.md` · `P06_INDEPENDENT_VERIFICATION_ADDENDUM_E2.md` · `P06_INDEPENDENT_VERIFICATION_TERMINAL_REPORT.md` |

**declared ∩ changed = 3 · changed \ declared = 4 · declared \ changed = 2.**

**Why it is material:** a challenger bounded to the declared description leaves **4 modified files
untested**, including the **terminal report** and the **AAS03 challenge** — the two artefacts most
likely to carry a disposition. Equal-sounding scope is not equal membership.

**Routed to the owner:** declare the `RC-03` surface as the enumerated changed set. **Not edited here
— that would be peer-owner mutation.**

**One instance of `IV-R-01`, measured in all five lanes in `07_` §3.** The check **fires in all five**,
including `RC-05`, so it has **no passing control** and is weak as a discriminator; `07_` §3 therefore
ranks the lanes **by magnitude** rather than treating them alike. This session does not call
`RC-05`'s single-file miss material.

## 4. Findings

**None issued.** Absence of findings is absence of testing. Under §2.10 it may not be read as a
discharge of anything.

## 5. What the appointed verifier must still do

Test the **26** with a **second command shape** — the owner's own note records that this programme lost
a whole search to a `git grep` `\b` that silently matched nothing, and that a grep for a literal token
matches its own documentation. **Compare member identity, not cardinality** (§4.F): 26 and 26 can be
different sets. Every zero or negative in this surface needs a **positive control inside the same
population**.
