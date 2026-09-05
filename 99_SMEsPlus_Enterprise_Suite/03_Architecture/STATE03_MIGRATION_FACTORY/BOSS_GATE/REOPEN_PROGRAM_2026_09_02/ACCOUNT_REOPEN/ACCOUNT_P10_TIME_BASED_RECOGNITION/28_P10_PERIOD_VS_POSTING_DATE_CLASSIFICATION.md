# P10 — RECOGNITION PERIOD vs POSTING DATE — OPTION CLASSIFICATION

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-CROSS-PROCESS-RECON-001` · Layer 1
**REVISION 2** — the first revision was materially wrong in three ways, all found by independent challenge and all verified by P10. See `34` §4 and §9.

**This document classifies options on evidence. It does not choose between them.** The decision is carried to `P11` / Boss Final Gate as `P10-D-02`.

---

## 0. What Revision 1 Got Wrong

| # | Revision 1 said | Corrected |
|---|-----------------|-----------|
| `R1-a` | The tolerance-zero boundary `T0-13` is "adopted programme-wide" by two peers, so its close condition excludes the status quo **as a consequence, not a preference** | **FALSE.** The peer's own register carries `T0-13` as an **open blocker, `BOSS DECISION REQUIRED`, `UNRESOLVED`, 0 of 13 resolved.** "Refuse or record a trace" is the **proposed close condition of an unresolved blocker**, not a ruling. P10's own `23` §4 already classed it as an *adopted position, not a fact* — so the package contradicted itself. **P10 covertly decided a prior question that was not its to decide: whether `T0-13` binds** |
| `R1-b` | Four options exist, and the trace-preserving option "is not implementable until `P08` provides a period field" | **FALSE.** At least **six** exist, and one of them — a shipped lock-exception mechanism — preserves the true date with **no period object and no ledger change at all** |
| `R1-c` | The behaviour is one specified convention: catch up in the first open period | **INCOMPLETE.** The landing period is selected by the journal's **sequence numbering format**: a month-reset sequence lands at that month's end, a year-reset sequence lands at **31 December**. Same lock, same charge, different period, decided by a non-accounting attribute |

## 1. The Two Concepts

| Concept | Definition | Owner |
|---------|-----------|-------|
| **Recognition period** | The accounting period an amount economically belongs to, determined by the schedule | `P10` |
| **Posting date** | The date the entry carries, against which locks, sequences and hashes are evaluated | `P08` |

## 2. Current State

| Fact | Evidence class |
|------|----------------|
| The two concepts are not distinguished; a recognition entry stores a date and no period | `VERIFIED FACT` |
| The ledger has no period object — a period is a date range and closing one is moving a date | Peer-supplied, class `B` |
| When a posting violates a lock, the date is **silently overwritten**; the amount is not re-spread | `VERIFIED FACT` |
| The re-dating is **specified, not incidental** — an executed test on the **asset** mechanism records a charge scheduled for the last day of 2020 posting as the last day of July 2021 | `VERIFIED FACT with an executed positive control` for the shared posting routine and the asset mechanism; `INFERENCE` for the transfer to the deferral mechanism, which has no test asserting its dates |
| **The test that records it is aimed elsewhere** — its stated subject is changing a computation method with draft moves before the lock | `VERIFIED FACT`. So the accurate claim is *the suite records the re-dating as expected output of a test aimed elsewhere*, **not** *the vendor asserts a misstatement as correct* |
| **The landing period depends on the journal's sequence numbering format** — month-reset lands at month end, year-reset lands at 31 December | `VERIFIED FACT` |
| No message, warning or flag records that the period changed — **while the sibling branch six lines above in the same routine does post a chatter message** about an accounting date | `VERIFIED FACT`. The silence is a **choice**, not a limitation |
| No mechanism re-derives the suppressed period when a period is reopened | `A — verified absence` within the searched module set |
| A test **does** exercise generation into a locked period on the validation path — it asserts the entry count and **says nothing about where the money lands** | `VERIFIED FACT`. This is stronger than P10's earlier "no test at all" |
| **Deployed exposure:** of four archives, three have **no lock date set on any company** (44 + 44 + 1). The fourth — the one P10 had wrongly declared unreadable — has fiscal-year, tax, sale and purchase locks all set | `VERIFIED FACT`, P10-executed, with a positive control |

**The deployment fact changes the decision's character.** In three of four deployed databases the defect **cannot fire, because there is nothing to violate**. In the fourth it can. So this is not remediation of a live estate-wide misstatement; it is a design choice being taken while exposure is still almost entirely ahead of the programme — which makes the disruptive options cheaper than revision 1 implied.

## 3. The Options

### Option A — permit the silent re-date (status quo)
Supportable. The product's specified behaviour; never blocks a close; no change. Against: the amount is misstated by period while every total stays correct, so no reconciliation detects it; and the landing period is selected by a sequence format. **Whether `T0-13` excludes this option depends on whether the Boss adopts `T0-13`, which is an open blocker.**

### Option B — refuse
Satisfies the proposed `T0-13` close condition. Not novel: the product already refuses on asset disposal and on grouped generation, both tested. Against: converts a silent misstatement into a visible failure at close. With three of four databases carrying no lock at all, the disruption argument is weaker than revision 1 stated.

### Option C — permit, and record an attributable trace
The other half of the proposed `T0-13` close condition. Preserves close integrity and period truth together. Revision 1 said this needs a ledger change; **Option E shows part of this family does not.** A queryable period field still would.

### Option D — separate the concepts entirely
Recognition event carries its period; posting act carries its date. Removes the defect class rather than the instance. Largest change; depends on the accounting-event object that does not yet exist, so it cannot be scoped before `D-5`.

### Option E — post at the true date under a recorded lock exception  *(new; revision 1 missed it)*
The product ships a first-class lock-exception object recording company, user, reason, validity window and the original lock date. An active exception suppresses the violation, so **the entry posts at its own date and is not re-dated at all**, and the exception itself is the attributable trace.

**Requires no period object and no ledger change.** Bounds: the irreversible hard lock is **not** exception-able; the exception table exists in the two newer deployed databases (with no rows) and **is absent from the older line**, so this option is unavailable on part of the estate.

### Option F — post the re-date as a chatter trace  *(new; revision 1 missed it)*
The routine already posts a chatter message in the adjacent branch. Recording the original period the same way costs nothing anyone else owns. Weaker than C — not queryable — but strictly stronger than A, and available immediately.

### Variants assessed and not counted as distinct
- **Generate into the open period from the start** — this is A with the damage done earlier, and it destroys even the schedule row that would evidence the true period.
- **Block generation when the schedule crosses a lock** — this is B relocated to source-document validation; it fails the invoice rather than the close. Precedent exists on the grouped path.
- **Suspense period** — needs an account, not a period object, so it escapes C's dependency; but it relocates the misstatement instead of recording it.
- **Lock aware of recognition journals** — half-built already: the violation check is journal-aware and exempts by journal type. A configuration-shaped variant of E.
- **Per-mechanism policy** — orthogonal to all of the above; its cost is that period truth then varies by mechanism, which is itself the problem `T0-13` names.

## 4. Relationship Between the Options

`D` ⊃ `C` ⊃ `F` in strength of trace. `E` sits outside that ordering: it prevents the divergence rather than recording it. `B` prevents it by refusing. `A` permits it unrecorded.

If the Boss adopts `T0-13`, `A` is excluded and `B`, `C`, `D`, `E`, `F` all remain admissible. **If the Boss does not adopt `T0-13`, `A` remains on the table.** Revision 1 asserted the first case as settled. It is not.

## 5. The Gap Revision 1 Did Not See

Every option above is framed around **the lock**. A peer process records a **second re-dating path that fires with no lock configured at all** — triggered by a document-date change. **A ruling scoped to the lock path would leave that path untouched.**

Recorded as `P10-U-23`, `PEER DEPENDENCY OPEN`, routed to `P08` and the peer that raised it. The Boss should be told that `P10-D-02` as currently framed does not dispose of it.

## 6. What Further Research Can and Cannot Resolve

**Can:** whether any entry in the one lock-carrying deployed database has actually been re-dated; whether the lock-exception route is viable on the older estate line; the population of the second, lock-free path.

**Cannot:** the choice. It is normative — reporting truth against operational disruption — and Stage J directs research to stop and produce a decision package.

## 7. Carried To

`P11` / Boss Final Gate as `P10-D-02`, and **jointly with the peer's `T0-13`**, because they are the same question in two vocabularies: *may a posting constraint alter a recognition period* and *may an accounting fact be mutated without refusal or trace* have the same answer set. **The Boss should be asked to decide them together, not in sequence.**
