# 01 — Executor eligibility, re-derived with a control

## 1. Why this is re-derived and not inherited

`53fd951` reached the same conclusion. Under peer-intake discipline a prior
session's finding is verified before it is adopted — including a finding from
this session's own lineage. Every command below was run in this session against
a fresh clone of `origin/SMEsPlus`.

## 2. The governing clause

Two independent sources, neither of them the session prompt:

**Source A — the frozen handoff blob `961b2ec` itself**, first lines:

> **Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-REMEDIATION-002]` — **Claude Opus 5,
> disqualified from every lane below** under `XRECON/Q-BOSS-01` (`XRD-009`).
> **Verifier appointed by Boss:** ChatGPT GPT-5.6 Sol, eligibility conditional
> per repair/challenge pair.

The disqualification is written into the immutable artifact the Boss ruling
cites. It is not an inference drawn by any later session.

**Source B — today's Boss ruling, B-2 first condition:** "did not author or
execute the repair under review."

## 3. The test — did Claude Opus 5 author or execute the repairs under review?

Per-commit, because git author identity does not discriminate: four of the six
frozen SHAs are committed under the human account `TH.PATTARAKRIT SOLUTION
SERVICE CO., LTD. <scgl.thailand@gmail.com>`.

| Frozen SHA | Commit author | `Co-Authored-By` trailer |
|---|---|---|
| `2079a25` | human account | `Claude Opus 5 <noreply@anthropic.com>` |
| `9d4ecdc` | **Claude Opus 5** | `Claude Opus 5` |
| `692ea27` | human account | `Claude Opus 5` |
| `b5f5a21` | human account | `Claude Opus 5` |
| `e368d11` | **Claude Opus 5** | `Claude Opus 5` |
| `d685176` | human account | `Claude Opus 5` |

**6 of 6** carry the trailer. **2 of 6** are additionally authored directly by
Claude Opus 5. Reading the author field alone would have returned 2 of 6 and
produced the wrong eligibility answer for four lanes.

## 4. Control — the predicate can return empty

A trailer grep that matched everything would produce this same 6-of-6 result on
any input. The predicate was therefore run against a population where it must
return empty for most members:

- Population: the most recent 200 commits reachable from `origin/SMEsPlus`.
- Result: **193 of 200 carry no `Co-Authored-By` trailer at all.**
- Named negatives: `b8666f1`, `b2b5777`, `8f4921e`.

The predicate discriminates. The 6-of-6 positive is a real signal, not an
artefact of a filter that cannot fail.

## 5. Result

`EXECUTOR-INELIGIBLE — CLAUDE OPUS 5 AUTHORED OR EXECUTED ALL SIX REPAIRS UNDER REVIEW`

This holds for **every** lane, including the repo-only Lane A (`RC-02`, `RC-03`,
`RC-04`). Lane A is repo-only with respect to *evidence location*; it is not
exempt with respect to *verifier independence*. The two are different
constraints and B-1 relaxes only the first.

## 6. Why reproduction was withheld rather than run and labelled

An RC challenge executed by the author of the repair is inadmissible whichever
way it comes out: a confirming result is self-certification, a falsifying result
is still not independent evidence. Running the lanes would not have advanced
`CP-SC-14`.

There is a second and stronger reason. A published Claude-authored verdict on
`CO-F-01`, on the 26-vs-27 adjudication, or on the `:45`/`:54` contradiction
becomes something the appointed verifier has read before forming its own. That
would damage the independence B-1 exists to obtain. **Withholding is the
protective act here, not the passive one.**

Every material claim in §3 and §4 is model-independent: it is the content of git
objects, reproducible by any party from the frozen SHAs.
