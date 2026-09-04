# P09_AAS_PLUS

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Role:** AAS+ — synthesis across the four AAS-03 expert challenges, **preserving disagreement**.
**Layer:** 1 — clean-room.

---

## 1. WHAT AAS+ DOES AND DOES NOT DO HERE

AAS+ does **not** reconcile the experts into one voice. Where they disagree, the disagreement is the finding. Where they agree, agreement is stated as convergence and not as proof.

This synthesis reads the four reviews and the research evidence together and asks one question the individual reviews could not: **do the findings compose into a single structural account, or into several unrelated ones?**

They compose into one. That is the AAS+ headline.

## 2. THE SINGLE STRUCTURAL ACCOUNT

Every confirmed finding in this session is a consequence of **one architectural choice**: the management dimension is expressed as *physical schema plus a schemaless payload*, rather than as *scoped data with referential integrity*.

| Consequence | Follows because… |
|---|---|
| axes cannot be tenant-scoped | a column has no owner |
| axis lifecycle is destructive | dropping a column drops its data |
| axis history is silently rewritable | moving a value between axes is a column-to-column update, done by direct statement |
| the scope check applies to one axis only | it is a relational-field mechanism, and only one axis is a conventional relational field |
| the scope check can never apply to the payload | it is a relational-field mechanism, and the payload is a JSON value |
| the allocation has no referential integrity | keys inside JSON have no foreign key |
| the allocation total is unenforceable at the storage layer | there is no constraint surface on a JSON payload |
| the allocation is invisible to the lock date, the hash and the tracking | those are field-name lists, and the field is one opaque value that no list names |
| reporting must shadow the ledger table | there is no relational path from a dimension to a figure, so a view is synthesised |
| the shadow view must expand per axis | the axes are columns, so they must be unpivoted |
| the reallocation filter cannot see percentages | the query can only test the JSON's keys |

**Eleven independently-found defects, one root cause.** This matters for SMEsPlus more than any individual finding: **fixing them individually would be eleven patches on a representation that will regenerate them.** The representation is the decision.

**AAS+-01.** The single highest-value determination available to SMEsPlus from P09 is: **express the management dimension as scoped, relationally-integral data.** Every requirement in the Layer 1 documents (MA-*, SM-*, DM-*, CO-*, BC-*, AB-*, EA-*, CP-*, B-*) is downstream of it.

## 3. WHERE THE EXPERTS CONVERGED

Convergence across disjoint assignments is the strongest signal this session produced, because no expert saw another's brief.

| Convergence | Reached independently by | Assessment |
|---|---|---|
| the scope check covers one axis and cannot cover the rest | X2 (platform mechanism) and X4 (client-side absence, with the source's own admission) | **Strong.** Two different layers, same conclusion, neither derived from the other. |
| management records with no ledger counterpart are a first-class, reported-on population — not an edge case | X1 (three producers plus a profitability domain built for them) and X3 (the budget's own achieved filter engineered to catch them) | **Strong.** |
| the controls that exist are display-level, and the server-level counterparts are missing or elective | X4 (systematically, in a table) and X2 (no storage-level constraint anywhere on the surface) | **Strong.** |
| silence at a boundary is the recurring failure mode — not incorrect values, but correct values disappearing without a record | X3 (inter-company drop, bill-line overwrite) and X4 (untracked allocation change) | **Strong, and the most transferable lesson.** |

## 4. WHERE THEY DID NOT CONVERGE — PRESERVED

| ID | The disagreement | AAS+ position |
|---|---|---|
| **DIS-01** | X3 disproved the exposure the research team asserted (row multiplication). | **AAS+ upholds the disproof and refuses the closure.** The mechanism is confirmed and is *worse* than the team stated; only the exposure fails, and it fails because one call site happens always to attach one filter. AAS+ records this as a **latent hazard**, not a resolved item, and rejects any downstream restatement of "disproved" as "safe". |
| **DIS-02** | X2 narrowed the team's cache claim. | **AAS+ accepts the narrowing without qualification** and notes that the team's *scope* claim was untouched. This is the correct shape for a correction: narrow the wrong part, leave the right part standing. |
| **DIS-03** | X1 re-characterised the highest-severity finding from duplication to misallocation. | **AAS+ adopts X1's characterisation as authoritative** and treats the team's imprecision as a defect in its own right, because at this severity an imprecise characterisation would have produced the wrong remedy. |
| **DIS-04 / DIS-05** | Coverage and unit disagreements between X1 and the team. | **AAS+ retains both records verbatim and forbids retro-fitting.** A class-C declaration that later turns out to have been resolvable elsewhere is evidence that a brief was incomplete; erasing it destroys the only trace of that. |
| **DIS-06** | X4 could not locate the budget access rows and routed it as a dependency; nobody else looked. | **AAS+ leaves it open as `DEP-P09-04`.** No participant may close another's class-B by not having searched. |
| **DIS-07** | The scope-aware constitution correction superseded the team's original position. | **AAS+ upholds the correction** and requires the superseded wording to remain visible in the revision log. An over-constraint that is silently deleted teaches nothing. |

## 5. AAS+ FINDINGS THAT NO SINGLE REVIEW COULD PRODUCE

**AAS+-F1 — Three independent double-count mechanisms were found by two experts who were not looking for double-counting.**
X1 found two (one work-order event producing two records at two rates into one aggregate; one management record matching several budget lines in full). X3 established a third is *not* reachable (the report view). None of the four briefs mentioned double-counting. **A defect class that surfaces three times from unrelated assignments is a property of the design, not a set of bugs.** The common cause is §2: without relational integrity there is no place to state that two records are two views of one fact.

**AAS+-F2 — The severity ranking changes once the findings are composed.**
Individually, the highest-severity finding is the misallocating reallocation (CH-CAND-04) because it moves real money to the wrong account. Composed, the highest-severity finding is **X4-01**: schema-altering rights over the dimension structure are one settings toggle away from every internal user, and that toggle is the one an implementer enables on day one. Every other finding in this package is a bounded error; that one is an unbounded, irreversible capability held by the wrong population.
**AAS+ ranks X4-01 first.** No individual reviewer could rank it first, because none of them held the destructive-lifecycle findings and the access findings at the same time.

**AAS+-F3 — The reference pattern's controls are consistently one representation-layer too high.**
The completeness rule lives in application code, opt-in by context. The scope rule lives on a field attribute that one of N dimensions happens to have. The budget lock lives in a view. The activation restriction lives on a write permission that a create call bypasses. **In every case a control was placed at the layer where the *feature* was implemented rather than at the layer where the *invariant* holds.**
**AAS+-02:** in SMEsPlus, every invariant shall be enforced at the lowest layer that can express it, and each control shall carry a declaration of the layer it is enforced at, so that a later reviewer can test the claim rather than infer it.

**AAS+-F4 — The negative-claim standard and the brief-error clause both paid for themselves in this session.**
The brief-error clause fired twice (a wrong path, and a missing root correctly declared class C rather than substituted). The negative-claim standard prevented at least four "does not exist" statements that would have been wrong: the maintenance surface, the budgetary position, the budget control, and the export surface are all class-B or scoped class-A statements with declared boundaries, and at least one of them (budget control) is explicitly still open system-wide.
**AAS+ records that neither control was applied by the author to itself** — both were applied to reviewers by instruction and then returned against the author. That is the intended direction.

**AAS+-F5 — What P09 cannot deliver, and why that is a finding rather than a failure.**
Two of the eight constitutional trace steps have **no carrier at all** in the reference pattern: the financial-event identity and the cost object. P09 cannot design either alone — the first belongs to Core Ledger, the second is contested across P03 and P04. **P09's terminal state therefore cannot be "model complete", and any claim that it is should be treated as an error.** The correct output is a specified gap with named owners, which is what `P09_CORE_RECON_HANDOFF_PACK` carries.

## 6. AAS+ VETO

**AAS+-VETO-01 — No implementation of the P09 management-accounting model may begin while the financial-event identity is undefined.**

Grounds: every P09 requirement that makes management truth traceable (SM-03 identity, SM-14/15 change classes, B-02 provenance class, B-03 enforced link, AB-05 bidirectional traversability, AB-07 period binding) is expressed *relative to an accounting event that does not yet exist as an object*. Building the management layer first would force it to invent a provisional identity, and every record written against that provisional identity would require migration when the real one arrives.

Scope of the veto: **implementation only.** It does not block design, does not block Boss decisions, and does not block the other P0x processes. It is lifted when the accounting-event identity is defined and ratified.

**AAS+-VETO-02 — No SMEsPlus design may adopt the reference pattern's report-shadowing mechanism, in any form, for any statement presented as accounting information.**

Grounds: it asserts a posting state the data does not have (CN-07), and its safety depends on a filter that one call site happens always to attach (DIS-01). Both grounds are independently sufficient. This veto is **not** lifted by the disproof of CH-CAND-05; the disproof addressed reachability, not the assertion of a false state.

## 7. WHAT AAS+ DOES NOT CLAIM

- AAS+ does not certify the evidence base. It reviewed four reviews and the two evidence files; it did not re-run the source reads.
- AAS+ does not close any class-B, class-C or class-D item, and does not convert any of them.
- AAS+ makes no statutory claim of any kind, Thai or otherwise.
- AAS+ issues no approval and moves no gate.

## 8. TERMINAL STATE

**SYNTHESIS ISSUED. ONE ROOT CAUSE IDENTIFIED. SEVEN DISAGREEMENTS PRESERVED UNRESOLVED. FIVE AAS+ FINDINGS. TWO VETOES RAISED, BOTH LIMITED TO IMPLEMENTATION AND DESIGN ADOPTION RESPECTIVELY. NO GATE MOVED. BOSS IS SOLE FINAL APPROVER.**
