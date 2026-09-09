# SA_CORR4_04 — COMPLIANCE RETRACTION PROPAGATION

## CP-SA-C4-40 — COMPLIANCE RETRACTION PROPAGATED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR4-PREGATE-CLOSURE-001]`
Branch: `architecture/phase-sa-corr4-pregate-closure-2026-09-09-001`
Condition: **`C4-04`**
Boss: **SOLE FINAL APPROVER**

---

## 1. Re-measurement first — the denominator was not assumed

Master prompt §6.1: *"Do NOT assume the denominator is still `184` branches or that exactly `183`
remain."* It was not assumed. It was re-measured on two command shapes.

| Measure | CORR3 | **CORR4, re-measured** |
|---|---|---|
| Total relevant branches | 184 | **185** |
| Carrying the path at all | *"one blob, 184 branches"* | **185 — every branch. `0` absent** |
| Carrying the **corrected** blob `827b5906` | **1** | **2** — `…corr3-proof-verification…` and this branch, which inherits it |
| Carrying the **uncorrected** blob `111bfc41` | **183** | **183** |
| **`origin/SMEsPlus` (mainline)** | not stated | **carries the UNCORRECTED blob** |

**Both shapes** — `git rev-parse -q --verify '<branch>:<path>'` per branch, and `git ls-tree <branch> --
<path>` per branch — **agree exactly.**

> **`C4-04-F-01`. The remaining count is `183` in both rounds and the arithmetic behind it is different
> in each: CORR3's `183` is `184 − 1`; CORR4's is `185 − 2`.** A round that had carried the figure
> forward instead of re-measuring would have published a **wrong denominator and a wrong
> corrected-count** and would never have detected it, **because the only number it cared about was
> unchanged.** This is the exact failure §6.1 was written to prevent, and it would have occurred.

---

## 2. The claim class — scoped by class, not by the remembered file

The programme's own rule is that a correction is scoped by the **claim class**, never by a peer's file
name. CORR3 remediated one file. **`C4-04` tests whether one file was the population.**

**Four independently-shaped instruments** were run over the `CORR4-FRAME` — `U2` = 3,604 text paths
across 185 branch heads:

| Instrument | Shape | Distinct statements | Distinct paths |
|---|---|---:|---:|
| **A** broad seed sweep | `ISO 27001 / IEC · SOC 2 · GDPR · PDPA · HIPAA · PCI-DSS · certifi · compliance · compliant · attestation · accredit · conformance` | path-level | **1,061** |
| **B** assertion-verb | `compliant with · complies with · conforms to · conformant · adheres to · certified to/against/under · is certified · fully compliant` | **54** | **49** |
| **C** heading form | `standards? compliance` | **17** | **13** |
| **D** named-standard token | `ISO 27001 · ISO 9001 · SOC 2 · GDPR` | **40** | **16** |

**Instruments C and D were re-run independently by the orchestrator**, chunked, case-insensitive, and
**reproduce at 13 and 16 paths.** Instrument **A's population is `1,061`, not the `633` first
reported** — the two runs used different word-boundary anchoring, and the wider figure is the one
carried. **126 distinct files were read in full context** — every hit of B, C and D, and a stratified
sample of the broad population, which is **~12% of `1,061`, not ~20% of `633`.**

### 2.1 Classification

| Class | Result |
|---|---|
| **`PROHIBITED CLAIM`** — asserts SMEsPlus or a customer **is** compliant / certified / conformant | **1 file** |
| `QUOTATION / RETRACTION` | ~16 files — the Boss decisions, `KNOWLEDGE_CONSOLIDATION_REPORT`, `SA_CORR2_07`, `SA_CORR3_05`/`11`/`12`, `SA11`, `SA19`, the master prompts, **and the corrected blob itself**, whose retraction quotes the old heading |
| `DESIGN TARGET` | dozens — including the **two Boss prohibitions themselves**, `GAP-014`'s `PLANNED` control mappings, the TAS-2/TAS-16 open-research lines (all `HOLD`), and a scoped Thai Revenue Code functional requirement |
| `UNRELATED` | the large majority — governance boilerplate, the `MTI-*`/`CF-I-*` **internal** conformance vocabulary, instrument sign-off "certified", and **Thai withholding-tax "certificate" as a business document, not an assurance certificate** |

**Controls.** Instrument **B fires** (54 statements / 49 paths), so its `0 PROHIBITED CLAIM` is a **true
negative, not a broken pattern**. Instruments **C and D independently converge on the same single
file** — three differently-shaped instruments landing on one file is itself the control that the class
is not being missed by construction. Negative control `zqw94713_corr4_no_such_token` returns **0**.

> **`C4-04-F-02`. CORR3's remediation population was complete at the file level.
> `16_Learning_Analysis/01_SYSTEM_OVERVIEW.md` is the only file in the repository, on any of the 185
> branches, carrying a claim in the prohibited class.** Recorded because the programme's default
> expectation — and mine on opening this condition — was that a one-file remediation would prove
> under-scoped. **It did not, and a negative result verified on four instruments is worth as much as a
> finding.**

### 2.2 The folder census

`16_Learning_Analysis/` holds **6 files**. The other five — `00_LEARNING_INDEX`,
`02_MODULE_ARCHITECTURE`, `03_DATA_MODEL_OVERVIEW`, `COMPLETION_SUMMARY`, `README` — each resolve on
**185 of 185 branches with exactly 1 distinct blob** (byte-identical everywhere) and each return **0**
hits on the full keyword pattern. **Positive control: the uncorrected `01_SYSTEM_OVERVIEW` returns 10
on the identical pattern.** The instrument fires; the five zeros are real.

### 2.3 `GAP-KC-01` — the repudiation, quoted

`07_Output_From_AI/Phase_2.5_Knowledge_Consolidation/KNOWLEDGE_CONSOLIDATION_REPORT.md` §4:

> *"**Conclusion:** `16_Learning_Analysis/` should be treated as **low-confidence / not evidence-grade**
> for Phase 3 purposes. It reads as a generic architecture-education template rather than a factual
> account of the actual repository … this consolidation report does **not** use `16_Learning_Analysis/`
> as a source for any specific business rule, module, or data model claim … recorded as **`GAP-KC-01`**
> … raised to Boss/PMO for a decision on whether to archive, correct, or explicitly relabel."*

**Not re-escalated.** `GAP-KC-01` is open, PMO-owned, and correcting the prohibited claim does not
require answering it. **Recorded so that no reader treats §3 below as having disposed of the folder.**

### 2.4 `C4-I-06` — a reported instrument defect, tested and **not reproduced**

The first executor of this sweep reported that **`git grep` silently truncates when given ~185
revisions at once**, citing `96` paths single-command against `633` chunked, with a spot check showing
`74` matches on one branch of which only `10` were captured. **That claim was material enough to
invalidate every branch-wide count in this package, so it was tested before being adopted.**

**It does not reproduce.** Single-command and 19-way-chunked runs were compared with **identical
flags**:

| Pattern shape | Single-command | Chunked | |
|---|---:|---:|---|
| 15 fixed strings — `BD-ACC-01` · `MTI-18` · `privileged` · `break-glass` · `superuser` · four `FDS_*` · `HX-` · `CF-I-` · `MODULE_SPEC_AUTHORIZATION` · `ACCOUNTING_INVENTORY_INTERFACE_CONTRACT` · `compliance` (**557**) · `ISO 27001` | — | — | **agree, all 15** |
| Simple `-E` alternation | **29** | **29** | agree |
| **Broad `-E` alternation — the shape the defect was reported on** | **1,061** | **1,061** | **agree** |

> **`C4-I-06`. The reported truncation is not a property of the revision count.** A first comparison
> appeared to show a discrepancy and was itself an artefact — the two runs differed in the `-i` flag,
> not in chunking. **The real difference between `96` and `633` was the pattern, not the method.**
>
> **Recorded, and the peer's record corrected, because the claim as stated would have caused a later
> reader to distrust every branch-wide count in this package and in CORR3's.** The programme's rule is
> to verify a peer's instrument claim before adopting it; **this is the first time in the chain that
> the verification returned *not reproduced*, and the finding is worth as much as a confirmation.**

---

## 3. Verification of the correction itself

Audited against `git cat-file -p 827b59068d8fdafa4d72acbcb42913b3bbdb3b97`, read directly.

| Test | Result |
|---|---|
| **(a)** Any unqualified claim remaining? | **No.** 10 lines match `complian\|certif\|attest\|conform\|accredit`; every one is the relabelled heading, the retraction quoting the old heading and both Boss decisions verbatim, or the explicit disclaimer |
| **(b)** Any evidence-backed claim accidentally removed? | **No.** All five items retained; nothing deleted, two columns added |
| **(c)** Any new contradictory variant introduced? | **No.** No claim-shaped statement appears elsewhere in the 315-line file |
| **(d)** The fifth line, `Local regulations (Thailand)` | **Correct.** Verbatim: `| Local regulations (Thailand) — statutory, **candidate / UNVALIDATED** | HOLD / EVIDENCE REQUIRED | None |` — **both** required qualifiers present |

**The corrected heading and disclaimer, verbatim:**

> `### **Standards Alignment — design targets, not compliance or certification claims**`
> *"The following are standards SMEsPlus **aims to design controls in alignment with**. SMEsPlus makes
> **no claim of compliance, conformance or certification** against any of them, **for itself or for any
> customer**, and **holds no attestation** for any of them."*

Every conformance status `NOT ASSESSED`; every attestation cell `None`.

**`C2-F-20` is closed and the reason is method, not vocabulary.** The Thailand line matches none of
`ISO|SOC 2|GDPR|CERTIFIED`; it is corrected because CORR3 remediated **the claim block as a block**.
**Reproduced and confirmed:** a token-driven remediation would have corrected four rows and left the
statutory one asserting compliance.

---

## 4. Propagation — what is technically possible, and what is authorized

**These are two different questions and this file answers both separately, because conflating them is
how a governance blocker gets reported as a technical one.**

| Question | Answer | Evidence |
|---|---|---|
| Is `origin/SMEsPlus` protected? | **No** — `{"name":"SMEsPlus","protected":false}`; the protection endpoint returns `404 Branch not protected` | GitHub API, read-only |
| Does the operating account have write access? | **Yes** — `{"admin":true,"maintain":true,"push":true}` | GitHub API, read-only |
| Is propagation therefore **technically possible**? | **Yes, on all 183** | — |
| Is it **authorized for this session**? | **No** | §4.1 |

### 4.1 The exact authority blocker

Three independent instruments forbid it, and **any one of them is sufficient**:

1. **The containment rule.** Publishing to another party's branch is prohibited. `SA_CORR3_05` §3.6
   records it as the reason CORR3 did not propagate: *"Method available to this session: **none**.
   Publishing to another party's branch is prohibited by the containment rule; merging is prohibited by
   master prompt §21."*
2. **Master prompt §0**, this round: `DO NOT … merge/release/deploy`.
3. **Master prompt §12** authority boundary: this session writes to its own branch and no other.

**The blocker is authority, not capability.** Stated in exactly those terms because a reader told only
that propagation "could not be done" would reasonably infer a technical obstacle, and there is none.

### 4.2 `C4-04-F-03` — the exposure is external, and no round has recorded that

CORR3 classified this as *"a mainline act. **Not a Boss decision**"* — correct as to owner, and
**silent as to reach**. Measured:

| Measure | Result |
|---|---|
| Repository visibility | **`public`** — `{"private":false,"visibility":"public"}` |
| Unauthenticated fetch of the uncorrected claim on mainline | **`HTTP 200`** |

> **The unsupported ISO 27001 / ISO 9001 / SOC 2 / GDPR compliance assertion is, at the time of
> writing, publicly readable without authentication from the default branch of a public repository.**
>
> **This changes no ownership and it changes the character of the item.** Boss decision `03` prohibits
> self-declaring compliance *"solely because the software contains supporting functions"*; decision
> `05` §10 separates Standard Alignment from Certification. **A prohibited claim that is externally
> readable is the case those decisions exist to prevent, not an internal tidiness item** — and it has
> been externally readable since before `GAP-KC-01` first flagged the folder as not evidence-grade
> on 2026-07-05.

### 4.3 The propagation is one act, not 183

The 183 uncorrected branches, classified by namespace:

| Namespace | n | Forward value of correcting |
|---|---:|---|
| **`SMEsPlus` (mainline, default branch)** | **1** | **The whole of it.** Every future branch is cut from it; the public URL resolves to it |
| `claude/*` | 56 | historical execution branches |
| `audit/*` · `research/*` · `corr/*` · `prompt/*` | 86 | historical, unmerged by design |
| `control/*` · `design/*` · `ruling/*` · `governance/*` · `architecture/*` · `review/*` · `boss/*` | 22 | historical |
| `ibpv/*` · `chatgpt/*` · `agent/*` · `state0*` · `feature/*` | 9 | historical |
| `ignore`, `ignore2`…`ignore7`, `noop`, `state03-governance-v2` | 9 | **disposable by their own names** |
| **Total** | **183** | |

> **`C4-04-F-04`. Correcting `origin/SMEsPlus` alone carries the entire forward exposure and the whole
> of the public exposure.** The other 182 are **historical execution branches that are unmerged by
> design** — the programme's own model is that they are never merged and Boss decides. **Correcting
> them would rewrite the evidence record of rounds that have already been published**, which the
> supersession rule forbids: prior evidence must remain readable as it was.
>
> **The propagation therefore has two parts with opposite dispositions:** one mainline act that closes
> the exposure, and 182 branches on which the uncorrected text is **audit lineage that should be
> preserved, not corrected.** No prior round has drawn that distinction, and CORR3's *"183 of 184
> branches still carry the retracted claim"* reads as 183 outstanding acts when the operative number
> is **one**.

### 4.4 What this session produced instead of a prohibited write

The correction is made **mechanically applicable** so the PMO act is an application, not a
re-derivation:

| Artefact | Where |
|---|---|
| The corrected blob, byte-exact | `827b59068d8fdafa4d72acbcb42913b3bbdb3b97`, reachable from this branch and from `…corr3-proof-verification…` |
| The single act that closes the exposure | apply that blob at `99_SMEsPlus_Enterprise_Suite/16_Learning_Analysis/01_SYSTEM_OVERVIEW.md` on `origin/SMEsPlus` |
| Verification, per branch, reproducible | `git rev-parse -q --verify '<branch>:99_SMEsPlus_Enterprise_Suite/16_Learning_Analysis/01_SYSTEM_OVERVIEW.md'` → expect `827b5906…`; and `git ls-tree <branch> -- <path>` as the second shape |
| Completion test | the count of branches on `111bfc41…` falls from **183** to **182**, and the 182 are the historical set of §4.3 |
| The claim-class population, so the act is not re-scoped later | **1 file**, established on four instruments — §2 |

---

## 5. Disposition

> # `PROPAGATION HOLD — THIS SESSION MAY NOT WRITE TO ANY BRANCH BUT ITS OWN`

**The exact blocker, stated once:** propagation is **technically possible on all 183** — mainline is
unprotected and the operating account has push and admin — and is **prohibited to this session** by the
containment rule, master prompt §0 and master prompt §12, **any one of which is sufficient**. The act
is a **PMO / repository-owner mainline act**, and it is **not a Boss decision**: Boss decisions `03` and
`05` already prohibit the claim class, and applying a prohibition Boss has already issued is execution,
not decision.

**It is not `PROPAGATION COMPLETE`**, and it is not `COMPLETE WITH NON-MATERIAL EXCEPTIONS` — **the one
branch that matters is uncorrected, and its exposure is public.** Recording anything else would be a
false assurance of exactly the kind this condition exists to remove.

**What CORR4 did close:** the denominator is re-measured and wrong in the record it inherited; the claim
class is established as one file on four instruments; the correction is audited on all four required
tests and passes; the exposure is measured and is external; the act is reduced from 183 to **one**; and
the remaining 182 are reclassified from *outstanding* to **audit lineage to be preserved**.

---

## 6. Residual

1. **§2's `1,061`-path broad population was sampled, not exhaustively read** — **126 of 1,061, ~12%**,
   stratified. **The `1 file` result rests on instruments B, C and D being exhaustively read and
   converging — two of which the orchestrator re-ran independently — not on the broad sweep being
   fully classified.** A challenger should read the unread **935** rather than re-run the same three
   instruments.
2. **I did not verify that a fourth claim shape does not exist.** Instruments B, C and D are
   assertion-verb, heading and named-token. **A claim made in a table cell, an image caption, a Thai
   sentence, or a filename would escape all three.** Thai in particular: every instrument here is
   English-token based, and the corpus is bilingual.
3. **`GAP-KC-01` is open and this file does not close it.** The folder-level disposition — archive,
   correct or relabel — remains PMO's and is not re-escalated.
4. **§4.3's recommendation that 182 branches be left uncorrected is mine.** Its ground is the
   supersession rule and the programme's own never-merge model. **A reader who holds that a prohibited
   claim should not survive anywhere would reach the opposite conclusion**, and that reading is
   coherent. **It is a PMO judgement and I have stated my reasoning rather than assumed it.**

## 7. Checkpoint

> ## `CP-SA-C4-40 — COMPLIANCE RETRACTION PROPAGATED`
> **Disposition: `PROPAGATION HOLD` — exact blocker: this session's authority.**
> **Denominator re-measured `185 / 2 / 183 / 0`. Claim class established as `1 file` on four
> instruments. Correction audited on 4 of 4 tests and passes. Exposure measured and is `public,
> HTTP 200`. The act reduced from 183 to 1. 4 findings — `C4-04-F-01` … `C4-04-F-04`.**

**Next autonomous action:** `CP-SA-C4-50`, the four-condition closure matrix.

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
