# P09_REVISION_LOG
## (also serves as the RESEARCH_ERROR_AND_REVISION_LOG required by SMEPLUS-26-09-04-ACC-REV2-CORR1)

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Layer:** 1 — clean-room.

Every revision, correction and superseded position, in the order it occurred. Superseded wording is retained rather than deleted, so that the error is legible.

---

## R1 — SCOPE REVALIDATION UNDER THE CONSTITUTION CORRECTION

**Trigger:** `SMEPLUS-26-09-04-ACC-REV2-CORR1` arrived mid-execution, superseding any wording implying that tenant context **and** company context are mandatory for every operation, and replacing it with the scope-aware model (PLATFORM / TENANT / COMPANY, context derived from the determined scope).

**Handling:** no reset, no restart, no evidence discarded, no completed work repeated. The four parallel evidence strands and the four expert challenges continued without interruption; **none of their output required re-running**, because scope-neutral facts — which objects carry a company field, what the record-rule domains are, which constraint fires on which field — are unaffected by how the constitution classifies them. Only the interpretation layer was affected.

**Affected finding — recorded in the required format:**

| Field | Content |
|---|---|
| **Original finding** | *(superseded wording, retained verbatim)* "**SMEsPlus position MA-08:** every analytic object shall carry a required tenant and a required company. An empty company shall not exist on any analytic object." |
| **Scope assumption used** | Blanket tenant-and-company enforcement on every object, irrespective of what the object is. |
| **Why it is over-constrained** | It treats an empty company as a defect *per se*. Under the corrected model, an analytic axis, an axis value, an assignment rule and an obligation rule may all be legitimately TENANT-scoped, for which company context is **not required**. The original position would have forced a company onto objects that carry no financial effect and are not legal artefacts. |
| **Correct scope analysis** | Determined object by object in `P09_SCOPE_OWNERSHIP_MATRIX` §3. Axis → TENANT. Axis value → TENANT by default, COMPANY where it denotes a legal-entity object. Management record → COMPANY. Allocation → COMPANY, following its carrier. Assignment and obligation rules → TENANT, with company as a *selector*, not as ownership. Budget → TENANT or COMPANY, declared per record. Reallocation mechanism → COMPANY, because it posts. |
| **Updated classification** | The finding is **not withdrawn but re-aimed.** The defect is **the absence of any scope declaration**, not the presence of a null company. The reference pattern uses one nullable field to express ownership, availability and selection simultaneously, so where it is empty the three meanings are indistinguishable. |
| **Architecture impact** | MA-08 rewritten (declared owning scope as first-class data; context derived from scope; deny on missing or unprovable scope; availability represented separately from ownership). MA-09 rewritten (uniform consistency enforcement, tenant-consistency where the object is tenant-scoped). **MA-10 added** (no implicit widening from COMPANY to a wider scope). **B-09 added** to the boundary document (aggregates computed within one declared scope; widening explicit and authorised). `P09_SCOPE_OWNERSHIP_MATRIX` created. |
| **Cross-process impact** | Six peer dependencies opened (PD-01…PD-06), plus PD-07 for findings landing inside P01/P02 territory. P09 does not stop for any of them and does not adjudicate against another process. |
| **Evidence required** | None additional for the re-aiming itself. Two scope determinations are held for evidence: the work centre as a cost object (`HOLD-SC-01`) and whether the deployed tenant custom set contains the department dimension at all (`HOLD-SC-02`, class D). |

**Findings explicitly re-read and confirmed *unaffected* by the correction:**
- the axis carries no company field and no tenant concept, and materialises as shared physical schema — this is not "missing company context", it is an object whose ownership is not representable at all;
- the scope check between a costed row and its axis values fires on one axis only — a COMPANY-scope finding about a COMPANY-scoped object, fully in force;
- every finding in the boundary, semantic, distribution, cost-object, budget, actual-versus-budget, event and edge-case documents that does not turn on company nullability.

## R2 — DENOMINATOR CORRECTION: TENANT CUSTOM ROOT COUNTS

**Raised by:** AAS-03 Expert 3, as `X3-COR-01`, against the research team.

| Field | Content |
|---|---|
| **Original wording** | The three tenant custom roots were recorded as "68 entries / 57 entries / 50 entries". |
| **The reviewer's measurement** | 65 / 57 / 47. |
| **Adjudication** | Re-measured by the research team. **Both are correct measurements of different units:** 68 / 57 / 50 directory entries, of which 65 / 57 / 47 are loadable modules; the difference is archive files that are not modules. |
| **Why it is nevertheless a defect** | The claim being bounded was a *module* population. Stating it in *entries* is precisely the project's own **UNIT** failure: "say what one member is." The label "entries" was accurate and the unit was wrong for the claim. |
| **Action** | The evidence base was corrected in place to state modules, with the entry count retained parenthetically. The correction is recorded here rather than only in the file, because the pattern — not the number — is the lesson. |

## R3 — RECONCILED NON-DISCREPANCY: REFERENCE ROOT COUNT

**Raised by:** AAS-03 Expert 1, which observed its own listing returned 797 entries against the evidence base's 790, and **declined to declare an error** without running the team's method.

**Adjudication:** both figures are correct. 790 module manifests; 797 directory entries including non-module files. **No correction required, and the reviewer's restraint is recorded as correct conduct** — a reviewer who reports a discrepancy without asserting a verdict is doing the job properly.

## R4 — CANDIDATE STATUS CHANGES FROM THE CHALLENGE PHASE

| Candidate | Entry status | Exit status | Changed by |
|---|---|---|---|
| CH-CAND-01 | PLAUSIBLE | **CONFIRMED** | X2 |
| CH-CAND-02 | PLAUSIBLE | **CONFIRMED**, reachability established without execution | X2 |
| CH-CAND-03 | PLAUSIBLE | **CONFIRMED** | X1 |
| CH-CAND-04 | PLAUSIBLE | **CONFIRMED and re-characterised** — misallocation, not duplication | X1 |
| CH-CAND-05 | PLAUSIBLE | **DISPROVED as an exposure claim**; mechanism confirmed and found stronger; retained as a latent hazard | X3 |
| CH-CAND-06 | class A on three lists | **CONFIRMED** by an independent guard-by-guard trace | X4 |

## R5 — WORDING SUPERSEDED BY REVIEWER CORRECTION

| ID | Superseded wording | Replacement | Raised by |
|---|---|---|---|
| COR-X2-02 | the privileged-axis lookup "caches it in a process-level cache" *(inviting a reading of indefinite staleness)* | the cache is invalidated on every write path that matters, bounded to one request; the separate scope claim stands | X2 |
| DIS-03 | "transferred as if it were total" | a **misallocation**: the whole balance moves, and the unallocated fraction is not picked up anywhere either | X1 |
| COR-REV-01 | the "no ledger link" finding, read as implying a homogeneous summable population | the record asserts at least five structurally different facts across producers | X1 |
| COR-X4-04 | the confirmed-budget lock is a view attribute *(implying raw programmatic access is needed to defeat it)* | it is reopenable through the normal interface via an unguarded state reset | X4 |
| R9 | `08` row E19 — depreciation produces management records from the asset own allocation | the records are produced **and net to zero**; the allocation is applied to both legs of a balanced pair | **P04**, post-publication |

## R6 — CONTROLS THAT FIRED DURING EXECUTION

| Control | Result |
|---|---|
| "if any path in this brief is wrong, report it as a finding" | **fired twice** — a doubled path segment in one brief; a missing root correctly declared class C rather than substituted |
| negative-claim standard (class A–E, declared boundaries) | applied to every negative; prevented at least four unbounded "does not exist" statements |
| denominator rule (population, pattern, path set, unit) | **caught two author defects** — an author-chosen 13-module producer list against a measured 9-module set with 5 absent from the list (COR-P09-01/02), and the unit failure in R2 |
| independent challenge inside the research phase | **13 corrections and 15 findings returned against the author; none of them originated with the author** |
| prohibited-verdict-vocabulary scan | run mechanically across every produced file before commit; result recorded in `P09_EVIDENCE_MANIFEST` |
| clean-room vendor-token scan | run mechanically across every Layer 1 file before commit; result recorded in `P09_EVIDENCE_MANIFEST` |

## R9 — INCOMING CORRECTION FROM P04, AFTER PUBLICATION

**Received:** from the P04 (Acquire-to-Retire) process after the P09 package was published at `16f884f`.
**Handling:** every claim was **re-verified by P09 against primary source before acceptance.** A peer report is not evidence; the source is.

| Field | Content |
|---|---|
| **Original finding** | *(superseded wording, retained)* `08` row E19 recorded that a posted asset depreciation produces management records from the asset own allocation, linked through the ordinary posting path. |
| **What was wrong** | The row was **true of the records and false of the effect.** The allocation is written onto **both** rows of the depreciation entry; analytic-line creation runs over all rows with no account-type filter; and the analytic amount is the **negated signed balance** times the share. The two rows of a balanced pair therefore produce mirror-image analytic amounts that **cancel**. |
| **Verification performed by P09** | three locations read directly: the asset-side value builder that sets the key on both rows under an explicit guard; the creation routine iterating the entire row set; the amount builder negated-balance formula. All three confirmed. Class **A**. |
| **Updated classification** | Row E19 corrected; row **E20** added for the complementary no-allocation case (each row computes its own allocation from its own account, so a balanced pair can be attributed to two different cost objects, giving a non-zero residue — mechanism class A, outcome class D per deployment); row **E21** added for programmatic posts. |
| **Architecture impact** | **EA-06** added (allocate only the rows carrying the effect; symmetric allocation of a balanced pair attributes nothing, by arithmetic). **EA-07** added (allocate an event rows as one event and verify the result against the intended attribution). Contradictions **CN-20** and **CN-21** added. Edge cases **EC-56 … EC-59** added. |
| **Cross-process impact** | P04 reports the finding contradicts a premise underpinning a standing costing veto held by a prior Asset package. **P09 records this as a pointer and does not adjudicate** — reconciling parallel evidence tracks is a Boss-level decision. Registered as `HOLD-AS-01` and `DIS-09`. |
| **Evidence required** | whether any **other** event type allocates both legs of a balanced pair symmetrically — class **C, not searched**; P09 did not sweep for the pattern. |

**Second correction in the same message — extends EV-P09-017.** P09 had recorded that the 100 % obligation check is opt-in by execution context. P04 supplied a **second, independent gate**: the validation routine filters to product display type, so entries with no product-type rows are skipped even when the flag is set. **P09 verified the row-type gate directly.** P04 accompanying enumeration of the posting call sites was **not** re-run by P09 and is carried at class **B from P09 position**, not restated as P09 class A.

**Third item — scope, accepted as convergence.** P04 scopes the analytic **plan** as a TENANT candidate and the **distributed amount** as a COMPANY financial fact. This **independently reproduces** P09 own determination in `19` §3, reached from a different domain without sight of it. P04 sharper corollary is adopted as **MA-11** (`20` §B, `P04-PD-04`).

**Assessment recorded, not softened:** this is the **second** time in this session that a published P09 claim was corrected by someone other than its author, and the first time by another process rather than a commissioned reviewer. The count of author-originated material corrections in this session remains **zero**.

## R7 — WHAT WAS NOT REVISED, AND WHY

No finding was withdrawn on the basis of inconvenience, and no class-B, class-C or class-D item was converted to class A at any point in this session. The unsearched list in `P09_CONTRADICTION_REGISTER` §D is the same length at the end of the session as when each item was raised, with the single exception of one class-C residue closed by transcription (COR-REV-02).

## R8 — TERMINAL STATE

**REVISION LOG: ONE CONSTITUTION CORRECTION ABSORBED WITHOUT RESET · TWO AUTHOR DENOMINATOR DEFECTS · FIVE WORDINGS SUPERSEDED · ONE CANDIDATE DISPROVED · ONE POST-PUBLICATION CORRECTION FROM A PEER PROCESS, VERIFIED BEFORE ACCEPTANCE. NO GATE MOVED.**
