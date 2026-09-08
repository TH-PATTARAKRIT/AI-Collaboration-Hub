# P06_FINAL_DELTA_EVIDENCE.md

**Prompt:** `[SMEPLUS-26-09-08-ACC-ONE-PROMPT-FINAL-CLOSURE-001]` Part A · deliverable **3 of 12**
**Owner SHA:** **`a533fe92d6f6855e0b362179403476520cc9aafa`** · baseline `b5f5a211763568a4212d08954c835412f7728a0a`
**Parent verifier result:** `RC-04 = FAIL`
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. The delta, in one line

**A live validation row certified 65 distinct `P06-B-*` identifiers with `contiguous = YES`, in a file that raises `P06-B-66` and `P06-B-67` nine lines below it.** The row is superseded, the current figure is **67**, and it is published as an enumeration with two instrument shapes and four controls.

## 2. Files changed — three, not one

| File | Change | Authority |
|---|---|---|
| `G02_RECOVERY_2026_09_06/P06_VERIFICATION_TOOL_DEFECT_REGISTER.md` | §3 row superseded; §3.1–§3.6 added | `RC-04`, the named carrier |
| `13_P06_EVIDENCE_MANIFEST.md`:94–95 | path set declared on both count rows | `VER-E-06` — same claim class |
| `18_P06_CORE_RECON_HANDOFF_PACK.md`:214 | path set declared on the 75 figure | `VER-E-06` |
| **new** `G03_ONE_PROMPT_FINAL_2026_09_08/P06_ONE_PROMPT_OWNER_CLOSURE_RECORD.md` | the owner record | — |

## 3. The four denominator clauses, declared

| Clause | Declaration |
|---|---|
| **POPULATION** | every distinct `P06-B-*` blocker identifier raised anywhere in the package, **closed or open** |
| **PATTERN** | ERE `P06-B-[0-9]+` / Python `\bP06-B-(\d+)\b` — requires the hyphen and a digit, **excluding the adjacent `P06-B2R` family (54 occurrences)** |
| **PATH SET** | recursive `*.md` under the package root — **89 files**: root 70 · `G02_CLOSURE` 12 · `G02_VERIFICATION` 2 · `G02_RECOVERY` 3 · `G02_OWNER_CORRECTION` 2 |
| **UNIT** | **distinct identifier token** — not occurrence, not file, not open blocker |

**Path-set sensitivity, measured rather than assumed:**

| Path set | Files | `P06-B-*` |
|---|---:|---:|
| root only | 70 | **67** |
| the three frozen roots | 84 | **67** |
| recursive | 89 | **67** |

## 4. Two instrument shapes, agreeing

```
SHAPE A  shell, string set        find … | xargs grep -ohE 'P06-B-[0-9]+' | sort -u | wc -l   → 67
SHAPE B  Python, integer set      len(ids)=67 · min 1 · max 67 · set(range(1,68))-ids = []  → contiguous True
```
**They share no code path.** A compares strings from a stream filter; B compares integers from a parser against a constructed range.

## 5. Four controls, each able to fail

| Control | Mutation | Observed |
|---|---|---|
| negative | impossible id | **0** |
| **injection** | append a synthetic id | **67 → 68, max 68** — a NEW identifier is detected |
| **deletion** | strip every `P06-B-33` | **67 → 66, missing `[33]`, contiguous False** — a MISSING identifier is detected |
| family boundary | `P06-B[^-]` | **54 `P06-B2R` occurrences visible and excluded** |

> **The deletion control is the one the superseded row never had.** Its cross-check was *"max id = 65 and contiguous"* — **both computed from the set the total came from. A check derived from the measurement cannot contradict it.**

## 6. The enumeration — the population, not its cardinality

`P06-B-01` … `P06-B-67`, contiguous, no gaps, carried in **73 of the 89** files. Printed in full at the register §3.3.

## 7. Two defects the self-test found that `RC-04` did not

### `VER-E-06` — two live totals for one concept, separated only by an undeclared path set
`13_`:95 publishes open items as **68**; `18_`:214 as **75**. Both current-tense, same commit, same concept. **Neither is a miscount** — 68 is the 70-file root, 75 is the 84-file three-root scope — **and neither stated its path set.**

**`RC-04` reproduced 68 and never reached 75, because it inherited the narrower published command.** An undeclared path set propagates to the verifier as silently as to the reader. Repaired by declaring the scope at both carriers; **values unchanged, because both were right.**

### `VER-E-07` — the register inflated the population it was correcting
The control table was first written with the synthetic identifiers spelled in full. The immediate re-run returned **69**, max **9999**: **the two highest members of the P06 blocker population were tokens this correction had just written.** That is `VER-E-03` recurring **inside the round that documents `VER-E-03`**, nine lines from the standing rule forbidding it. Synthetic ids are now written with bracketed digits; recount **67**, contiguous, both shapes.

## 8. `Q-P06-03` / `Q-P06-04` reconciliation — re-checked, not re-researched

| Figure | Now | Prior | Reconciles? |
|---|---|---|---|
| blockers | **67** | 67 | yes |
| vetoes | `AASP-VETO-01…07` = **7** | 7 | yes |
| author errors | **21** (23 ids, 21 defined; unit = author error) | 21 | yes |
| host archive | **present and readable** at this run | 961 dirs | yes — the evidence base is still at rest |
| open items | **68 / 75** | both published, neither scoped | **no → `VER-E-06`** |

## 9. Self-test exit and standing limits

```
P06 OWNER CLOSURE COMPLETE — RC04 DELTA SELF-TEST PASS
```

**Owner self-test. Not independent certification.**

- `AASP-VETO-01`…`07` — **seven, none discharged.**
- `P06-B-34` / `P06-B-35` — **flagged, not disposed.**
- **67 is a floor, not a ceiling** (`P06-B-67`): the population is what the package raised, not what the system contains.
- No `Q-P06-03`/`Q-P06-04` research reopened. No blocker raised, closed or renumbered. No peer package touched.
