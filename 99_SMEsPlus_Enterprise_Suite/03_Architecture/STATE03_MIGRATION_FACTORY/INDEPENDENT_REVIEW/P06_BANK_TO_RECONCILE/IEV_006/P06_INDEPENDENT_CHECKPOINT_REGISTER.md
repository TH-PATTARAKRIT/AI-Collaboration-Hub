# P06_INDEPENDENT_CHECKPOINT_REGISTER.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-INDEPENDENT-EXTERNAL-CORRECTION-VERIFICATION-006]` · prompt commit `51763d8`
**Track:** INDEPENDENT EXTERNAL VERIFICATION · branch `audit/p06-independent-verifier-2026-09-06-001`
**Frozen audit surface:** `1b018c1` · **Terminal state:** `P06 INDEPENDENT VERIFICATION FOUND MATERIAL DEFECT — TARGETED REPAIR REQUIRED`

---

## 1. Checkpoints

| CP | Subject | Status |
|---|---|---|
| `CP-IEV-01` | **Independence precondition (§1)** | **NOT MET, and declared before any finding.** The executing context is the actor that authored the `REV-E-23` repairs. Recorded at the head of every artefact |
| `CP-IEV-02` | Fresh clone; write boundary (§7) | **COMPLETE.** Separate clone, audit branch, **0 files modified under the audited research package**, verified by `git status` on that path |
| `CP-IEV-03` | Stage A — freeze proved and inventoried | **COMPLETE.** `1b018c1`, tree `04f90a80…`, 87 files enumerated **from the tree**, extracted and verified **87 of 87 byte-identical**, digest `09c54632…` |
| `CP-IEV-04` | Stage A — repair population reproduced without the author's tally | **COMPLETE.** 26 occurrences / 19 files by three methods; 24 replaced statements by a fourth, marker-independent method; **21 + 3 = 24 reconciles** |
| `CP-IEV-05` | Stage C — instrument falsification | **COMPLETE, and this verifier's own instrument failed first.** `IEV-I-01`: a glob in a shell variable returned **0 occurrences of `P06` across 87 P06 files** and nine zero classes. Caught by the positive control |
| `CP-IEV-06` | Stage B — claim-class populations under widened patterns | **COMPLETE.** Nine classes; **7 carry survivors, 2 confirm complete** |
| `CP-IEV-07` | Stage E — four challengers in separate contexts | ~~**THREE OF FOUR RETURNED**~~ → **FOUR OF FOUR RETURNED and adjudicated** **[Q-P06-01 / XRD-001, 2026-09-07]**. Expert 2 returned after publication. **The prior disposition — *"its remit is materially covered by Experts 1 and 4"* — is FALSIFIED: it brought 7 material defects absent from the published 18.** `IEV-I-05` |
| `CP-IEV-08` | §5 — re-check every challenger claim before adoption | **COMPLETE. 2 refuted**: E1's `34_`:40/:99 delivery call (both qualified in-clause) and this verifier's own soft `VER-E-04` wording, **corrected against itself** |
| `CP-IEV-09` | §6 — protected items preserved | **COMPLETE.** `P06-B-08` `BOSS DECISION REQUIRED` · `P06-B-09` statutory · `P06-OQ-98` `HOLD` · `X-08` peer-owned · `AASP-VETO-07` nowhere discharged. Every apparent exception inspected individually |
| `CP-IEV-10` | §7 — route repairs to P06, do not self-repair | **COMPLETE. Zero source-package edits.** 18 defects routed as bounded correction items |
| `CP-IEV-11` | §9 — `AASP-VETO-07` decision | **PRESERVED.** Unavailable on the prompt's own terms *and* unsupported by the evidence |
| `CP-IEV-12` | Publication | **COMPLETE.** `dac6ac3` pushed to the audit branch; authoritative remote SHA verified via `git ls-remote origin refs/heads/…`, equal to local. **Research branch re-verified unchanged at `1b018c1` after the push** |
| `CP-IEV-13` | Post-publication record | **COMPLETE** |

## 2. Claims re-tested against the frozen tree

| Audited claim | Re-test | Verdict |
|---|---|---|
| *"21 repairs across 14 files"* | 4 methods | **TRUE as decomposed** — the propagation matrix's *"plus 3 supersession/snapshot markers"* reconciles to 24, and 24 is measured. **Five of the six statements of the figure omit the second component**, including the NEXT EXACT ACTION |
| *"65 blockers"* (4 repairs) | id count at 3 declared scopes | **FALSE. 67**, contiguous `B-01`…`B-67`, at every scope including both printed commands' own globs |
| *"three vetoes"* / *"four active vetoes"* | id count | **FALSE. Seven** |
| *"16 recorded author errors"* | id count | **FALSE. 23** |
| nine claim classes **COMPLETE** | widened patterns | **FALSE in 7 of 9** |
| `18_` and `70_` carry zero stale statements | measured | **FALSE. 5 and 1** |
| `HO-03`/`HO-04` *"are labelled"* WRITTEN, NOT DELIVERED | grep the artefact | **FALSE.** The pack's only delivery word is *"re-delivered"*; two statements certify the label *"verified by grep"* |
| `VER-E-01`, `02`, `03`, `05` | re-executed | **TRUE, all four** |
| `VER-E-04` | re-executed | **DOES NOT REPRODUCE** — exit 0, hits returned |
| the source-citation layer | re-executed against v18 and v19 | **TRUE.** Structure, line numbers, SQL quotation and eight version counts all exact |
| `P06-OQ-*` = 75 · `REV-E-*` = 23 · `34_`:51 tally | re-counted | **TRUE, all three** |

**`CPI-F-01` — Of twelve audited claims re-tested, five are true, six are false, and one is true only in its decomposed form. Every false one concerns the *state of the package*; every true one concerns the *ERP under study*.** The research is in better condition than the bookkeeping about the research.
