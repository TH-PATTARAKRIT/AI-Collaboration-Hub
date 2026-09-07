# 07 — `RC` RESULT REGISTER

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-INDEPENDENT-RC-VERIFY-001]`
**Branch** `audit/account-phase-s-iv-rc-verify-2026-09-07-001` · base `origin/SMEsPlus` @ `b8666f1`
**Executing model:** Claude Opus 5 · **Appointed verifier under `Q-BOSS-03` §1:** ChatGPT GPT-5.6 Sol

## 1. Results — **0 `RC-PASS`, 0 `RC-FAIL`, 6 `RC-HOLD`**

| RC | Owner | Frozen SHA | Ref head verified | Inputs accessible | **Result** |
|---|---|---|---|---|---|
| `RC-01` | P09 | `2079a25` | **MATCH** | **YES** — root exists, 13,515 `.py` reproduced; `k1_population.json` hash-verified 4 of 4 | **`RC-HOLD` — STRUCTURAL INDEPENDENCE NOT PROVEN** |
| `RC-02` | P11 | `9d4ecdc` | **MATCH** | **YES** — repository-only | **`RC-HOLD` — STRUCTURAL INDEPENDENCE NOT PROVEN** |
| `RC-03` | P06 IEV | `692ea27` | **MATCH** | **YES** — repository-only | **`RC-HOLD` — STRUCTURAL INDEPENDENCE NOT PROVEN** |
| `RC-04` | P06 source | `b5f5a21` | **MATCH** | **YES** — repository-only | **`RC-HOLD` — STRUCTURAL INDEPENDENCE NOT PROVEN** |
| `RC-05` | P08 | `e368d11` | **MATCH** | **YES — 4 of 4 dumps, SHA-256 and byte-size verified; `pg_restore` 16.15 and 18.6 both present** | **`RC-HOLD` — STRUCTURAL INDEPENDENCE NOT PROVEN** |
| `RC-06` | P11 | `9d4ecdc` | **MATCH** | premise `c7cfd8a` present | **`RC-HOLD` — STRUCTURAL INDEPENDENCE NOT PROVEN** *and* dependency `RC-05` not certified |
| `RC-07` | P08 IEV | `d685176` | **MATCH** | — | **NOT REQUIRED** — pointer-only, per the handoff matrix |

**Cause, one for all six:** `Q-BOSS-02` §1 control 1 (Model / Agent Separation) and control 2
(Appointment Independence). Every repair under review carries `Co-Authored-By: Claude Opus 5`, which
is the model executing this session. Determination and evidence in `00_` §2.

> **`RC-HOLD` is not `RC-FAIL`.** Nothing here says any repair is defective. Nothing here says any
> repair is sound. **Six surfaces are untested**, and under §2.10 that may not be read as a discharge.

## 2. Not `HOLD — MISSING REPRODUCIBLE EVIDENCE`, and the distinction is load-bearing

`Q-BOSS-03` §2 directs `RC-05 = HOLD — MISSING REPRODUCIBLE EVIDENCE` if any required input is absent
or inaccessible. **Every input was found and hash-verified.** The two hold-states are different:

| | Missing evidence | Missing executor |
|---|---|---|
| `RC-05` state | **NOT this** | **This** |
| Cured by | owner republishing evidence | **Boss appointing / dispatching an eligible verifier** |
| Owner action required | **none** | **none** |

**`RC-05` is evidence-complete and executor-blocked.** Sending it back to P08 would be wasted work.

## 3. `IV-R-01` — declared surface vs changed surface, all five lanes

Instrument: `git show --name-only <sha>` against the surface as the handoff matrix describes it.

| Lane | Declared | Changed | Changed but undeclared | Declared but unchanged | Material? |
|---|---|---|---|---|---|
| `RC-04` | 2 (a directory) | 8 | **6 — 75%** | 0 | **YES** — the corrected counts, two blocker registers, the filtered-tree evidence boundary, **two outbound handoffs to P11** |
| `RC-02` | 4 named + *"re-stated registers"* | 10 | **6** — only 2 of them are registers | 0 | **YES** — includes `P11_EVIDENCE_MANIFEST.md` and `P11_RESEARCH_ERROR_AND_REVISION_LOG.md` |
| `RC-03` | 5 (by description) | 7 | **4** | **2** | **YES** — includes the terminal report and the AAS03 challenge |
| `RC-01` | 4 | 8 | **4** | 0 | **YES** — includes `PACKAGE_MANIFEST_SHA256.md` |
| `RC-05` | 7 (by role) | 8 | **1** | 0 | **NO** — a package record, no count, no disposition |

**The check fires in 5 of 5, so it has no passing control and is a weak discriminator.** Stated
plainly rather than presented as a clean sweep. The lanes are ranked **by magnitude**, and only the
top four are called material. `RC-06` shares `RC-02`'s SHA and inherits its row.

**Disposition: `NARROWED` — routed to the surface owners as a handoff-matrix defect, not an RC finding.**
No matrix row was edited; editing it is peer-owner mutation.

## 4. `IV-R-04` — manifest coverage assertions, **MATERIAL, and it recurs in the repair itself**

`P11-E-49` was registered by the remediation session as *"a manifest coverage assertion carried
forward and false … its shape is unswept across other packages and is flagged as a lead."*
**The lead was swept here. It was correct, and two of its three nearest instances are live.**

Every count below is taken **twice, in different command shapes** (`git ls-tree -r --name-only` and
`git archive` → extract → `find . -type f`), and both shapes agree in every row.

| Manifest | Declared population / pattern | Asserted | `find` actually returns | Listed | Verdict |
|---|---|---|---|---|---|
| `P11_EVIDENCE_MANIFEST.md` @ `9d4ecdc` | *every file in the P11 package directory* · `find . -type f` | *"`find` returned **91** and this manifest processed **91**"* (`NC-12`) | **92** | **91** | **FALSE AS STATED** |
| `RC05_REPRODUCIBILITY/MANIFEST.md` @ `e368d11` | *every file under `RC05_REPRODUCIBILITY/`* · `find . -type f` | *"`find` returned **7**, manifest processed **7**"* | **8** | **7** | **FALSE AS STATED** |
| `PACKAGE_MANIFEST_SHA256.md` @ `2079a25` (P09) | — | *"checksums every package document **except itself**"* | — | — | **CORRECT — the exclusion is declared. This is the passing control** |

**Member identity, not cardinality** (§4.F). Diffing the 92 actual against the 91 listed:

```
in package, not listed:  P11_EVIDENCE_MANIFEST.md
listed, not in package:  (none)
```

**One row, and it is the manifest itself.** Same for `RC-05`: 8 − 7 = `MANIFEST.md`.

**The defect is the assertion, not the omission.** A manifest cannot hash itself; excluding it is
right. Declaring the population as *every file*, with pattern `find . -type f`, and then asserting
that `find` returned the number the manifest processed, is wrong — `find` returns one more. P09 shows
the correct form in one clause: **state the exclusion.** A stated exclusion stops the audit; a silent
one nets the count.

**Why this is the sharpest finding in this package:** `P11-E-49` was raised, repaired at `9d4ecdc`,
and **the repair reproduces the defect in the same commit** — the number moved 86 → 91, the shape did
not. And the remediation session's own new package, published in the same commit that flagged the
lead, carries it too. **A number can be corrected while the claim about how it was obtained stays
false**, and only re-running the declared command catches it.

**Disposition: `CONTRADICTED`** — against the assertion text in both manifests.
**Materiality:** the *contents* of both manifests are correct and complete; no real file is missing
and none is listed spuriously. **No evidence is lost.** What is defective is a coverage assertion —
the exact control class this programme relies on to know a package is whole. **Routed to P11 and P08
owners. Neither manifest was edited here.**

**Not swept:** P06 (`13_P06_EVIDENCE_MANIFEST.md` is a per-file table without a coverage assertion in
this form) and every package outside the five correction SHAs. **Declared as unswept, not implied clean.**

## 5. Verifier instrument defects — all three, kept (§4.H)

| Id | Defect | Would have caused | Caught by |
|---|---|---|---|
| `IV-INSTR-01` | frozen-ref check compared an **empty** variable to the asserted SHA; `"" = ""` printed `MATCH` six times while measuring nothing | six false positives on the single fact the whole package rests on | re-run in a second command shape |
| `IV-INSTR-02` | input sweep globbed `*.backup`; zsh aborted the **whole** `ls` on the unmatched glob and printed no listing | **`RC-05 = HOLD — MISSING REPRODUCIBLE EVIDENCE`, wrongly** | re-run by exact filename with an explicit `ABSENT` branch |
| `IV-INSTR-03` | RC-05 package size read from **the package's own `MANIFEST.md` header** instead of measured | recorded `RC-05` as a clean `IV-R-01` negative control at `7 = 7`; the truth is `8` vs `7` — **and reading the manifest instead of the directory is precisely what hid `IV-R-04`** | measuring the directory |

**All three are the same species: a control that cannot detect its own failure.** Each was caught only
by re-running in a different shape, never by inspecting the first result. `IV-INSTR-03` is the one
worth carrying — it produced a *favourable* result about someone else's package, which is the kind
this session had no incentive to re-check.

## 6. Findings summary

| Id | Class | Disposition | Materiality | Routed to |
|---|---|---|---|---|
| `IV-R-01` | handoff surface declared as a description, not a set | `NARROWED` | material in 4 of 5 lanes | P06 ×2, P09, P11 (via the matrix owner) |
| `IV-R-04` | manifest coverage assertion false as stated | `CONTRADICTED` | material; no evidence lost | P11, P08 |
| `IV-R-03` | `q1.py` input provenance and byte-identity | **`SUPPORTED`** — matrix claim verified, 4 of 4 at `54edc214…bbbdc569` | none; two undeclared in-repo copies noted | P09 (informational) |
| — | `RC-05` evidence contract vs `Q-BOSS-03` §2 | **`SUPPORTED`** — 7 of 7 requirements met | — | — |

**0 findings against any repair's substance.** No repair was tested. See §1.

**Identifier-gap declaration:** the `IV-R-*` family runs `01`, `03`, `04`, `05` — **there is no
`IV-R-02`.** It was drafted as a separate finding for the `RC-04` lane, then merged into `IV-R-01` as
`IV-R-01/RC-04` when the check was extended to all five lanes. **The number was retired, not lost, and
nothing cites it.** Declared so the gap is not later read as a dropped finding.

**Verifier instrument family:** `IV-INSTR-01`, `-02`, `-03` — contiguous, all three defined in §5.
