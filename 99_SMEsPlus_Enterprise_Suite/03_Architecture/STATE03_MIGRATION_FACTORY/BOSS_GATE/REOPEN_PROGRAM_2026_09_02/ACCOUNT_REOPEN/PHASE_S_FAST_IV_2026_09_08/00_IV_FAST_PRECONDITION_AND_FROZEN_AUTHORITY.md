# 00 — FAST IV: PRECONDITION, FROZEN AUTHORITY, AND EXECUTOR ELIGIBILITY

**Session** `[SMEPLUS-26-09-08-ACC-PHASE-S-FAST-FINAL-CLOSEOUT-001]`
**Branch** `audit/account-phase-s-fast-iv-2026-09-08-001` · base `origin/SMEsPlus` @ `b8666f1`
**Executing model/agent: Claude Opus 5.**
**Appointed verifier under `BOSS/Q-BOSS-03` §1: ChatGPT GPT-5.6 Sol.**

> **The governing prompt is addressed to ChatGPT GPT-5.6 Sol. It was executed by Claude Opus 5.**
> This session therefore issues **no `RC-PASS`, no `RC` disposition, no Veto discharge and no Phase S
> closure**. What it publishes is: the §2 precondition test, the §3 frozen-authority read-back, an
> **independently re-derived** eligibility determination, and **two material verifier findings that
> are true independently of who measured them** — both of which change what the appointed verifier
> must do next.

---

## 1. §2 Immutable handoff precondition — **SATISFIED, INDEPENDENTLY VERIFIED**

Re-derived in a fresh clone of `TH-PATTARAKRIT/AI-Collaboration-Hub` made 2026-09-08. Not inherited
from any prior session's assertion.

| Requirement | Declared in prompt §2 | Measured this session | Result |
|---|---|---|---|
| Remediation branch head | `0941161824f4d447d9e0816e492a90b99bcfaecc` | `git rev-parse origin/audit/account-phase-s-remediation-2026-09-07-001` → `0941161824f4d447d9e0816e492a90b99bcfaecc` | **MATCH, 40/40 chars** |
| Handoff artifact blob | `961b2ecfd11d29f34a7de5bbcdd1664547673453` | `git rev-parse 0941161:…/04_RC01_RC06_VERIFIER_HANDOFF_MATRIX.md` → `961b2ecfd11d29f34a7de5bbcdd1664547673453` | **MATCH, 40/40 chars** |
| Terminal state | `REMEDIATION-A — all six RC surfaces frozen and executable` | commit subject at `0941161` reads exactly that | **MATCH** |

**Per prompt §2, this is verified once and not repeated.** The historical Claude
`IV-PRECONDITION-HOLD` at `9d8ad70` is preserved as lineage and is **not** the current readiness
state. No material delta invalidates the handoff.

## 2. §3 Frozen RC authority — full 40-character read-back

Every declared short ref resolves to exactly one commit object in the fresh clone.

| Ref | Declared | Resolved (40) |
|---|---|---|
| `RC-01` P09 | `2079a25` | `2079a2594a6a76eb91bdb528f22eaf928d42c0d6` |
| `RC-02` P11 | `9d4ecdc` | `9d4ecdc744fbbb0e502a0b907f59c301bdf7812c` |
| `RC-03` P06 IEV | `692ea27` | `692ea27e11533bc72ef0123fa4d1e3524179bf6e` |
| `RC-04` P06 source | `b5f5a21` | `b5f5a211763568a4212d08954c835412f7728a0a` |
| `RC-05` P08 | `e368d11` | `e368d11da6f7e4973469ff5608d676ec2d13811c` |
| `RC-06` P11 | `9d4ecdc` | `9d4ecdc744fbbb0e502a0b907f59c301bdf7812c` |
| `RC-07` P08 IEV (NOT REQUIRED) | `d685176` | `d685176c2416210dfb67c01d862a911741530949` |
| Boss appointment | `6cb9946` | `6cb99464c4a3b9065c7cd9ae5014c13a7d6968b7` |
| Boss `Q-BOSS-02` | `2930723` | `2930723fbd45d8c4dada26197963ad6285d6c502` |

**7 of 7 RC refs and 2 of 2 Boss refs match. READY is not PASS and nothing below infers one.**

## 3. §2 of the appointment — executor eligibility, re-derived not inherited

`BOSS/Q-BOSS-02` §1 control 1 (**Model / Agent Separation**) and §2 state that **Claude Opus 5, where
it authored or executed the repair being reviewed, is NOT ELIGIBLE** for the corresponding `RC-*`
challenge, and that **eligibility is per repair/challenge pair**.

The per-pair test was executed here by reading each frozen commit's own trailers. **Git author
identity does not discriminate** — four of the six frozen SHAs are committed under the human account
— so the `Co-Authored-By` trailer was read on each commit individually.

| RC | Frozen SHA | `%an` author | `Co-Authored-By` trailer | Pair eligibility for **this** session |
|---|---|---|---|---|
| `RC-01` | `2079a25` | TH.PATTARAKRIT … | `Claude Opus 5 <noreply@anthropic.com>` | **NOT ELIGIBLE** |
| `RC-02` | `9d4ecdc` | **Claude Opus 5** | `Claude Opus 5` | **NOT ELIGIBLE** |
| `RC-03` | `692ea27` | TH.PATTARAKRIT … | `Claude Opus 5` | **NOT ELIGIBLE** |
| `RC-04` | `b5f5a21` | TH.PATTARAKRIT … | `Claude Opus 5` | **NOT ELIGIBLE** |
| `RC-05` | `e368d11` | **Claude Opus 5** | `Claude Opus 5` | **NOT ELIGIBLE** |
| `RC-06` | `9d4ecdc` | **Claude Opus 5** | `Claude Opus 5` | **NOT ELIGIBLE** |
| `RC-07` | `d685176` | TH.PATTARAKRIT … | `Claude Opus 5` | NOT REQUIRED |

**6 of 6 required RCs: Claude Opus 5 authored the repair under review.**

### `Q-BOSS-02` §1 control-by-control status of this session

| # | Control | Status |
|---|---|---|
| 1 | Model / Agent Separation | **FAILS — all six RCs**, §3 above |
| 2 | Appointment Independence | **FAILS** — `Q-BOSS-03` §1 appoints ChatGPT GPT-5.6 Sol. Substituting an unappointed executor is not a defect this session may cure for itself |
| 3 | Evidence Isolation | MET — fresh clone, separate session, frozen SHAs only |
| 4 | Read-Only Boundary | MET — owner evidence read only via `git show <sha>`; no owner artefact edited |
| 5 | Independent Reproduction | **NOT REACHED for any RC** — withheld deliberately, §4 |
| 6 | Independent Publication | MET — this branch |
| 7 | No Owner Mutation | MET — 0 peer refs written |
| 8 | No Self-Discharge | MET — 0 Vetoes discharged |
| 9 | No Self-Pass | MET — no `RC-PASS`, no closure |
| 10 | Boss Final Authority | MET |

## 4. Why reproduction was withheld rather than run and labelled

A same-model run **could not become `RC` evidence whichever way it came out**. Publishing it under
`RC-*` filenames would place a non-qualifying result in the tree inviting exactly the inference
`Q-BOSS-02` §5 prohibits (*"inference of PASS from silence or from prompt existence"*). The prompt's
§4 fast-track instruction to start Lane A immediately is **correct and is not refused** — it is
addressed to an eligible executor, and §5 below shows that executor exists and was wrongly blocked.

## 5. What this session publishes instead

Readiness and environment evidence that is **executor-neutral**: a SHA-256 is the same number
whoever computes it, and a file either exists on this host or does not. This is not `RC` evidence and
is not offered as any. See `07_RC_RESULT_REGISTER.md` for the two material findings.

`PHASE S = NOT CLOSED.`
No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
