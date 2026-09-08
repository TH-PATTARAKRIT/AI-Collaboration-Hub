# P06_ONE_PROMPT_OWNER_CLOSURE_RECORD.md

**Prompt:** `[SMEPLUS-26-09-08-ACC-ONE-PROMPT-FINAL-CLOSURE-001]` — Part A
**Control branch:** `control/account-one-prompt-final-closure-2026-09-08-001` · prompt commit `a06f5d9c69e020bf8e7749108b892b73c6b31e62`
**Owner:** P06 Bank-to-Reconcile
**Baseline:** `b5f5a211763568a4212d08954c835412f7728a0a`
**Parent verifier result:** `RC-04 = FAIL` (`04_RC04_P06_SOURCE_CHALLENGE.md`)
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. Authorised surface, and what was actually touched

RC-04 authorises exactly one carrier. Three files changed:

| File | Change | Authority |
|---|---|---|
| `G02_RECOVERY_2026_09_06/P06_VERIFICATION_TOOL_DEFECT_REGISTER.md` | §3 row superseded; §3.1–§3.6 added | RC-04, the named carrier |
| `13_P06_EVIDENCE_MANIFEST.md`:94–95 | path set declared on both count rows | `VER-E-06`, same claim class — prompt §5 *"fix it immediately in P06 in this same loop"* |
| `18_P06_CORE_RECON_HANDOFF_PACK.md`:214 | path set declared on the 75 figure | `VER-E-06` |

**No `Q-P06-03` / `Q-P06-04` research was reopened.** No blocker was raised, closed, re-severitied or renumbered. No peer package was touched. No veto was discharged.

## 2. The eight required executions

| # | Required by prompt §5 | Where | Result |
|---|---|---|---|
| 1 | preserve the 65 row as visibly superseded lineage | register §3, first row | struck through, marked **SUPERSEDED / WITHDRAWN 2026-09-08**, text preserved |
| 2 | publish the current 67 row | register §3, second row | published with both instrument shapes named |
| 3 | state unit, population, scope, exact identifier rule | register §3.1, four-clause table | POPULATION / PATTERN / PATH SET / UNIT all declared |
| 4 | re-run two independent count/contiguity shapes | register §3.1 | SHAPE A (shell, string set) **67**; SHAPE B (Python, integer set vs constructed range) **67**, contiguous `True` |
| 5 | publish the full 67-ID enumeration | register §3.3 | `P06-B-01`…`P06-B-67` printed in full |
| 6 | failure/positive control able to expose a missing/new id | register §3.2 | injection **67→68**; deletion **67→66, missing `[33]`, contiguity False**; negative **0**; family-boundary **54 excluded** |
| 7 | re-check `Q-P06-03`/`Q-P06-04` still reconcile | register §3.4 | vetoes **7**, author errors **21**, host archive present; **open items did not reconcile → `VER-E-06`** |
| 8 | do not reopen their research | — | not reopened |

## 3. Two defects the self-test found that RC-04 did not

Prompt §5: *"If self-test finds another defect in the same changed claim class, fix it immediately in P06 in this same loop."* Both were fixed in this loop.

**`VER-E-06` — two live totals for one concept.** `13_`:95 publishes the open-item population as **68**; `18_`:214 publishes it as **75**. Both current-tense, same commit, same named concept. Neither is a miscount: 68 is the package root alone (70 files), 75 is the three frozen roots (84 files). **Neither carrier stated its path set.** RC-04 reproduced 68 and never saw 75, because it inherited the narrower published command. Repaired by declaring the scope at both carriers; **the values are unchanged because both were right.**

**`VER-E-07` — this register inflated the population it was correcting.** The control table in §3.2 was first written with the synthetic identifiers spelled out. The immediate re-run of SHAPE A returned **69**, max **9999** — the two highest members of the P06 blocker population were tokens this correction had just written. That is `VER-E-03` recurring **inside the round that documents `VER-E-03`**, nine lines from the standing rule forbidding it. Repaired by writing synthetic identifiers with bracketed digits; recount returns **67**, contiguous, on both shapes.

## 4. Path-set sensitivity — the reason both defects exist

| Family | root only (70 files) | three frozen roots (84) | recursive (89) | Sensitive? |
|---|---:|---:|---:|---|
| `P06-B-*` | 67 | 67 | 67 | **no** |
| `P06-OQ-*` | **68** | **75** | **75** | **yes** |

**A stable count and an unstable count look identical in a published total.** The blocker figure survived three years of path-set ambiguity because it happens not to depend on it. The open-item figure did not, and nobody had run the table.

## 5. Self-test exit

```
P06 OWNER CLOSURE COMPLETE — RC04 DELTA SELF-TEST PASS
```

Executed at this commit, over the declared path set, with both instrument shapes and all four controls:
`67 distinct P06-B-* · P06-B-01…P06-B-67 · contiguous · no gaps`.

**This is an owner self-test. It is not independent certification.** RC-04's fresh delta challenge remains the external control, and is reserved for the single final independent gate.

## 6. What is NOT claimed

- Not a PASS, not a freeze, not a merge, not an implementation authorisation.
- `AASP-VETO-01`…`07` — **seven, none discharged.**
- `P06-B-34` / `P06-B-35` remain **flagged, not disposed**.
- **67 is a floor, not a ceiling** (`P06-B-67`): the population is what the package raised, not what the system contains.
