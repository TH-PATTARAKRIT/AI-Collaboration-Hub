# 00 — APPOINTMENT, PRECONDITION AND EXECUTOR ELIGIBILITY

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-INDEPENDENT-RC-VERIFY-001]`
**Branch** `audit/account-phase-s-iv-rc-verify-2026-09-07-001` · base `origin/SMEsPlus` @ `b8666f1`
**Executing model/agent: Claude Opus 5.**
**Appointed verifier under `BOSS/Q-BOSS-03` §1: ChatGPT GPT-5.6 Sol.**

> **This session is not the appointed verifier and is not an eligible `RC-*` executor.**
> It therefore issues **no `RC-PASS`, no veto discharge and no Phase S closure**. What it does
> publish is the §1 precondition test, the §2 independence determination, and the read-only
> readiness evidence a future eligible verifier can build on without re-deriving it.

---

## 1. §1 Hard precondition — **SATISFIED**

| Requirement | Evidence | Result |
|---|---|---|
| `REMEDIATION-A` published | `audit/account-phase-s-remediation-2026-09-07-001` @ **`0941161`**, subject *"PHASE S REMEDIATION: REMEDIATION-A — all six RC surfaces frozen and executable"* | **MET** |
| Present on remote, not inferred from a moving head | `git ls-remote origin refs/heads/audit/account-phase-s-remediation-2026-09-07-001` → `0941161824f4d447d9e0816e492a90b99bcfaecc` | **MET** |
| `04_RC01_RC06_VERIFIER_HANDOFF_MATRIX.md` exists | `0941161:…/PHASE_S_REMEDIATION_2026_09_07/04_RC01_RC06_VERIFIER_HANDOFF_MATRIX.md`, 56 lines | **MET** |
| Every RC row carries owner · SHA · surface · inputs · controls · expected challenge · dependency · evidence path | all 6 rows + `RC-07` pointer row; columns read individually, not from the header | **MET** |

**This corrects the prior IV session.** `audit/account-phase-s-iv-rc-2026-09-07-001` @ **`9d8ad70`**
published `IV-PRECONDITION-HOLD — VERIFIER HANDOFF NOT COMPLETE`. That was **correct when written**
(`9d8ad70` is dated before `0941161`) and is **superseded, not contradicted**. Lineage preserved.

`IV-PRECONDITION-HOLD` is **withdrawn as the current state**. The precondition is met.

---

## 2. §2 Structural independence — **FAILS FOR THIS EXECUTOR ON ALL SIX RCs**

Determination made from the **primary Boss text**, not from the handoff matrix's summary line
(the matrix asserts *"Claude Opus 5, disqualified from every lane below"*; that is a secondary
statement and is **not** what this determination rests on).

**Governing text — `BOSS_DECISION_PHASE_S_Q_BOSS_02_2026_09_07.md` @ `0941161` §1 control 1:**
> *"Model / Agent Separation — the verifier must not be the same model/agent that authored or
> executed the repair under review."*

**§2 of the same ruling:**
> *"Claude Opus 5, where it authored or executed the repair being reviewed, is **NOT ELIGIBLE** to
> perform the corresponding `RC-*` independent challenge for that repair."*

**`Q-BOSS-01` §2 forward-binding clause:**
> *"A challenge run by the same model that authored the repair it challenges does not satisfy `RC-*`."*

### 2.1 Authorship of each repair under review — measured, not assumed

`git` author identity is **not** the discriminating instrument here: six of the eight `corr/*` heads
are committed under the human account `TH.PATTARAKRIT SOLUTION SERVICE CO., LTD.`, which says nothing
about the executing model. The discriminating instrument is the **`Co-Authored-By` trailer**, checked
on every SHA individually.

| RC | Repair SHA | Commit author identity | `Co-Authored-By` trailer | Executing model |
|---|---|---|---|---|
| `RC-01` | `2079a25` | TH.PATTARAKRIT | `Claude Opus 5` | **Claude Opus 5** |
| `RC-02` | `9d4ecdc` | Claude Opus 5 | `Claude Opus 5` | **Claude Opus 5** |
| `RC-03` | `692ea27` | TH.PATTARAKRIT | `Claude Opus 5` | **Claude Opus 5** |
| `RC-04` | `b5f5a21` | TH.PATTARAKRIT | `Claude Opus 5` | **Claude Opus 5** |
| `RC-05` | `e368d11` | Claude Opus 5 | `Claude Opus 5` | **Claude Opus 5** |
| `RC-06` | `9d4ecdc` (+ premise `c7cfd8a`) | Claude Opus 5 / TH.PATTARAKRIT | `Claude Opus 5` on both | **Claude Opus 5** |

Corroborated independently by `Q-BOSS-01` §3: *"Every session in this programme to date has been
executed by the same model."*

**6 of 6.** There is no RC in this programme whose repair was authored by a model other than the one
executing this session.

### 2.2 Per-control determination for this session

| # | Control (`Q-BOSS-02` §1) | Status |
|---|---|---|
| 1 | Model / Agent Separation | **FAILS — all six RCs.** §2.1 |
| 2 | Appointment Independence | **FAILS.** `Q-BOSS-03` §1 appoints ChatGPT GPT-5.6 Sol. This session is a different party than the one appointed; substituting an unappointed executor is not a defect this session may cure for itself |
| 3 | Evidence Isolation | MET — separate clone, separate session, frozen SHAs only |
| 4 | Read-Only Boundary | MET — no owner artefact read outside `git show <sha>`; no peer branch written |
| 5 | Independent Reproduction | **NOT REACHED** — withheld, see §3 |
| 6 | Independent Publication | MET — this branch |
| 7 | No Owner Mutation | MET — 0 peer refs written |
| 8 | No Self-Discharge | MET — 0 vetoes discharged |
| 9 | No Self-Pass | MET — no `RC-PASS`, no closure |
| 10 | Boss Final Authority | MET |

**Controls 1 and 2 fail. Under §2 of the governing prompt, every RC is classified
`RC-HOLD — STRUCTURAL INDEPENDENCE NOT PROVEN`.**

---

## 3. Why reproduction was withheld rather than run and labelled

Controls 1–2 fail **before** any test is run, so a reproduction executed here could not become
`RC` evidence no matter what it returned. Running the six challenges and publishing the outputs
would create an artefact that **reads exactly like RC evidence** and is one careless citation away
from being consumed as one — the precise failure this programme has recorded repeatedly
(a summary adopted as a result; an unresolved item promoted to a rule).

`Q-BOSS-02` §5 prohibits *"inference of PASS from silence or from prompt existence"*. A same-model
run of all six RCs, sitting in the tree under RC filenames, is a standing invitation to exactly that
inference. **It is withheld deliberately, and that is a decision, not an omission.**

**What is NOT withheld:** readiness facts that are true independently of who measured them and that
carry no disposition — frozen-ref integrity, input existence, input hashes, tool availability. Those
are published in `07_` and `08_` so the appointed verifier starts from a checked surface. **None of
them certifies any RC.**

---

## 4. Verifier instrument defects — recorded, not erased (§4.H)

| Id | Defect | Effect | Action |
|---|---|---|---|
| **`IV-INSTR-01`** | Frozen-ref check compared `${H:0:7}` against the asserted SHA where `H` was **empty** for all six rows. `"" = ""` is true, so the instrument printed **`MATCH` six times while measuring nothing.** A control that cannot detect its own failure | Six false positives | **Re-run with a different command shape** (`git ls-remote origin 'refs/heads/corr/*'`, full 40-char SHAs, no truncation). All six genuinely match — see `07_` |
| **`IV-INSTR-02`** | Input sweep used `ls …*.dump …*.sql …*.backup`; zsh aborted the **whole command** on the unmatched `*.backup` glob, printing `no matches found` and **no file listing at all**. Read naively this is *"no dumps on the host"* — a false negative about the evidence base | Would have produced `RC-05 = HOLD — MISSING REPRODUCIBLE EVIDENCE` **wrongly** | Re-run by **exact filename**, per file, with an explicit `ABSENT` branch. All four present — see `07_` |

Both defects are of the shape this programme has already paid for. Both were caught by re-running
in a second command shape, which is the only control that caught either.
