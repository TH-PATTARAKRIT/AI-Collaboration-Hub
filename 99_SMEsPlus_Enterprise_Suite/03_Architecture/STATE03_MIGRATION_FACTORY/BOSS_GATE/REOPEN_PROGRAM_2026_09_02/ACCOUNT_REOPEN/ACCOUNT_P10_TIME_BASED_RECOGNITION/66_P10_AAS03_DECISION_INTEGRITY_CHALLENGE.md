# P10 — AAS-03 DECISION-INTEGRITY CHALLENGE

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D20`.

**The four challenges were split by class**, as the directive requires: **A** evidence base and denominator · **B** method, tooling and extraction · **C** findings and semantics · **D** decision authority and cross-process.

---

## 1. Status

| Class | Assignment | Status |
|-------|-----------|--------|
| **D** | Decision authority / cross-process | **COMPLETE** — §2 |
| **C** | Findings / semantics | **COMPLETE** — §3 |
| **A** | Evidence base / denominator | **COMPLETE** — §6 |
| **B** | Method / tooling / extraction | **COMPLETE** — §6 |

**All four returned. `CP-P10D20` is COMPLETE.** `EC-07` cannot count this round regardless — see §7.

## 2. Challenge D — Decision Authority. **The most damaging.**

The class added this round found five live defects, **one of them caused by the control added this round**.

| # | Finding | P10 verification | Repair |
|---|---------|------------------|--------|
| `W-33` | **The withdrawn claim was still live in two documents.** `38` asserted *"every assertion that the boundary is adopted is withdrawn"*. It was false of P10's own package: the dependency register still read *"adopted programme-wide"* **and** carried the superseded unrefined close condition **and** graded a Boss-reserved item *"partially resolved"* | Verified | Struck; `19` corrected |
| `W-34` | **The breach had propagated into a peer-facing obligation.** An obligation placed on the ledger owner read *"the close condition, which P10 adopts unchanged"* — unrefined, and never revisited | Verified | `25` `OB-03` corrected and restated with the refined condition |
| `W-35` | The intake register still classed the boundary **ADOPTED** with an *applicability* argument recorded in its verification column | Verified | `23` `IN-03` corrected |
| **`W-36`** | **The same defect inverted, inside the new control's first application.** P10 **downgraded** a peer's class `A` claim to `C`. The peer's register records it as **`A VERIFIED ABSENCE over the declared 22-root set`** and as **one of the three claims legitimately promoted** after re-running all 22 roots, two independently reproduced. **P10 applied its own intake rule and got the membership wrong** | **Verified from the peer's register** | `27` corrected; the peer's class `A` restored |
| **`W-37`** | **A peer *design* veto naming P10's own mechanism had never been read.** It prohibits any *"asset, accrual, deferred-recognition or cash-basis design"* from allocating a balance-sheet row into the management ledger — **design adoption only**, and its subject is precisely P10's own attribution finding. P10 had asserted in three documents that its own veto was *"the only veto binding P10"*, over a population it had enumerated at two | **Verified from the peer's register** | `32` corrected; the claim withdrawn |
| `W-38` | The veto's lift condition named the **superseded** option document, which states that refusal alone satisfies the boundary | Verified | `51` re-pointed at `39` and `40` |
| `W-39` | **`D-5` is coupled, by P10's own criterion.** One outcome of it removes an option from the admissible set — which is the definition P10 wrote. **The Boss faces three coupled decisions, not two** | Verified | `40` corrected |
| `W-40` | A fourth decision, on the tenant-hierarchy question, appears nowhere in the new documents though the peer's register names it beside the boundary | Verified | `40` records it as adjacent |
| `W-41` | Presenting a **programme-wide** tolerance-zero boundary as *"the second half of a P10 decision"* understates whom the ruling binds — it governs at least three domain instances, one of which is P10's | Verified | `40` §7 corrected |
| `W-42` | P10 quoted the boundary's status correctly and **never carried the raiser's own recorded defect in its derivation** — that it was scoped from the occasion that prompted it and *"the owed enumeration was never performed"* | Verified | `40` §7 records it |
| `W-43` | **Authority creep.** Four programme-level rules stated in the imperative by one process | Accepted | Re-framed as P10-internal controls **proposed** for adoption |
| `W-44` | Two options were described as *"found during the repair"*; they were found in the **prior** round | Accepted | `41` corrected |

**Challenge D also credited P10 with catching its own `TZ-1` over-closure**, and noted it was the third round in which the deciding correction came from a peer's artefact rather than from a challenge.

## 3. Challenge C — Findings and Semantics. **The most substantive.**

| # | Finding | Effect |
|---|---------|--------|
| `W-45` | **The collapse claim holds for two of four mechanisms, not product-wide.** The asset entry carries **two independent date fields** | `01` scoped |
| `W-46` | **Three of the four consequences claimed to follow from the collapse do not.** Catch-up exists on a path with no event object; the silent shift is caused by the posting layer and is only made *undetectable* by the collapse; currency is orthogonal — the loan has the strongest identity and still cannot express one | `01` corrected |
| `W-47` | **Carrying a period is necessary and not sufficient.** The asset carries its period and is **still** silently re-dated. A design can hold the field and never read it | Requirement `R-02` must be paired with a reportable-divergence obligation |
| `W-48` | **The six-primitive model is defective in four ways** — one primitive is derived, one is three policies, two are missing, and the accrual instantiates two of six, contradicting the universal quantifier | `01` corrected with the four repairs stated |
| **`W-49`** | **`P10-F-38`'s accounting significance settled against the counter-reading.** Correcting the emission does **not** double-count, so the both-legs shape buys nothing — and the netting **survives period bounding**, so a period-scoped analytic report shows **zero movement** from the whole deferral machinery. Cumulatively correct; **by period exactly as wrong as no deferral at all** — which is the level P10 owns | `24` §9 |
| `W-50` | **New:** the analytic balance splits debit and credit by sign before netting, so each pair inflates gross analytic turnover by roughly twice the base plus the periods. **Turnover reconciliations break; balance reconciliations pass** | `24` §9 |
| **`W-51`** | **There are THREE day-count engines, not two** — and the third, in the loan module, is a complete standards-named library of **eight** conventions. The deferral's convention is a named standard **with its February exception deleted**, in a codebase that implements the same standard correctly elsewhere. A 14–28 February window differs **5.5%** between two engines | `06` §8 |
| `W-52` | **Kernel element `K-1` changes from *build* to *adopt-and-extend*** — a complete convention library already exists in the reference root | `56` |
| `W-53` | **The loan allocation row is contradicted, class `E`** — it said amounts are supplied externally; the module ships its own engine | `06` corrected |
| `W-54` | **Four verified non-equivalences between the two journal shapes**, including that the grouped path always applies the revenue method, and that **intra-month divergence is total** | `02` §12 |
| `W-55` | **The switch is asymmetric and one direction is destructive** — grouped to validation **silently abandons** the deferral | `02` §12 |
| `W-56` | **`P10-F-18` was mis-titled** — the reversing convention is ordinary practice; the defect is the absent settlement link | `04` re-titled |
| `W-57` | **A THIRD instance of the attribution defect** — the accrual counterpart, failing **differently**: a denominator including lines with nothing to accrue, summing to **less than 100%** | `04`, `24` |
| `W-58` | One Layer 2 evidence item stated two mutually exclusive outcomes as one | Corrected |
| `W-59` | Three items carried as reviewer- or peer-supplied class `B` were **re-derived from source by a second party** and re-classed | Layer 2 §6 |

## 4. What the Two Challenges Confirmed

- The authority forensic **stands at the peer's current head**, verified four ways including a per-file search of 43 peer files.
- No later peer delta changes the boundary's close condition — the raiser states it in terms.
- **No unauthorised elimination beyond the one already restored** was found.
- The coupling of the two decisions is **sound and could not be broken**.
- The lock-exception option **survives** — it rests on P10's own extraction, not a peer claim.
- `P10-F-38`'s code shape **verified independently**, and the netting is arithmetic rather than inference.
- The monthly-only grid, the residue behaviour and the dead accrual back-link all **verified independently**, the last at class `A` over both module trees with a positive control.

## 5. Effect on `EC-07`

Two of four classes returned; both found material defects; one found a defect **caused by this round's own new control**. **This round is not a clean pass and cannot be counted. Consecutive clean passes: ZERO.**


## 6. Challenges A and B — the evidence base and the method

**These two classes had never been run before this round. They found 13 of the round's 22 corrections.** Full record at `67`; the load-bearing items:

| # | Finding | Class |
|---|---------|-------|
| `W-60` | **The denominator double-counts.** Two databases hold **identical company sets**; they are two restores of one tenant lineage. **46 distinct companies, not 90** | `E` |
| `W-61` | **The population is a floor, not a total.** The declaration was host-wide; the sweep covered three directories. **At least 9 further deployed databases exist inside the declared population.** Declared-pattern-not-run, fourth occurrence, in the document that says it corrects it | `E` |
| `W-62` | **Two files under `raw/` are authored prose, not transcripts** — re-running the shipped probe gives different hit counts | `E` |
| `W-63` | **The positive control was asserted and never executed.** Both challenges supplied it independently; **the zeros are read zeros** — but on someone else's control | `E` |
| `W-64` | **The byte-size control cannot detect the failure it was adopted for.** Extracting an absent table exits successfully and writes 722 bytes; empty-table artefacts are 913–915. The conclusion was right by a 191-byte margin never examined. **The probe printed a byte size for an absent table on one archive** | `E` |
| `W-65` | **The stated reason the defect cannot fire on one database is false** — three lock columns exist there, including a differently-named one found on no other archive | `E` |
| `W-66` | **Column counts wrong** — trailing constraints counted as columns. True 194/187/141/259 | `E` |
| `W-67` | **"Not a production database" is unsupported** — the discriminator was never computed for the comparison group. One database has **6 journal entries against 44 companies**, fewer than the one so classified | `E` |
| `W-68` | **The manifest listed 49 of 79 artefacts** and its scan record was stale | `E` |
| `W-69` | **Scripts are not executable, tool versions are pinned nowhere.** Following the manifest's reproduction instructions **with the default tool re-derives the corrected-away conclusion** | `E` |
| `W-70` | **The installed-module manifests were obtainable from containers in P10's own path set** — deployed estate is **19.0+e on PostgreSQL 15**, 251/216/179 modules, **nine Thai localisation modules**. The version is stated nowhere in the package | Class `C` → **`A`** |
| `W-71` | **A snapshot newer than anything P10 read exists**, dated 2026-08-26. Reading it was **refused by permission controls** and not worked around. *"No lock exists in the estate"* does not reach it | `C`, reason stated |
| `W-72` | Four further method defects: hard-coded path arrays under an "enumerated" declaration; a unit that counts translation and chart files as code paths; an undeclared filter; case-sensitivity suppressing 75 modules | mixed |

### 6.1 What Both Challenges Confirmed

The headline **survives, independently re-derived twice** across four archives plus three additional snapshots: **exactly one company row carries a period lock.** So do the database-D figures, the absence of the deferral mechanism from the older line, and the fact that **no deferral entry exists anywhere**.

## 7. Effect on `EC-07`

Four classes, all complete, **22 corrections**, nine of them against this round's own repair documents, one caused by the control this round introduced.

**This round is not a clean pass. Consecutive clean passes: ZERO of the two required.**

## 8. The Result That Should Govern the Next Round

**The two challenge classes that had never been run found 13 of 22 corrections — more than the two that had.** That is the strongest argument for the split protocol, and equally the strongest argument for distrusting any earlier round in which those classes were absent. Rounds 1 and 2 had neither.