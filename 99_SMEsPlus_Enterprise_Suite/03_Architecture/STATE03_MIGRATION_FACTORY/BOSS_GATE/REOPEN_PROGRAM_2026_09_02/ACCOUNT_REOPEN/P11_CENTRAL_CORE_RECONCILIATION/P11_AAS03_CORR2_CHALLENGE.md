# P11 — AAS-03 CORR2 FRESH BOUNDED CHALLENGE

`[SMEPLUS-26-09-06-…-CORR2-PHASES-001]` · `CP-P11C2-11` · **PHASE S**

> **Package frozen at `14de462` before commissioning. No edit was made to the reviewed surface
> until all four experts returned** — the control CORR1 broke (`P11-E-30`), honoured here (`P11-M-06`).
> Four experts, bounded to P11 + the frozen peer artefacts, read-only, unable to see each other.

---

## 1. Verdict

> ## `CONTRADICTED — EVIDENCE-SELECTION FAILURE`
>
> **Not a finding about one claim. A finding about the instrument that chose the evidence.**
> Four independent experts, four attack surfaces, **converged on the same defect class**: the
> population feeding CORR2 was selected by a filename-matching instrument, and the round's own
> supersession rule says filenames do not determine currency. **The rule and the instrument
> disagreed, and the instrument won.**

**Findings raised: 47. Accepted: 44. Disputed in part: 3.**

## 2. The independent convergence — the strongest signal in the round

Five defects were found by **more than one expert who could not see the others**:

| Defect | Found by |
|---|---|
| `P08 AAS+-VETO-01` over P11's largest evidence source is **absent from the package** | E1 · E3 · E4 |
| P06's *"not confirmed to be the SMEsPlus target"* qualifier **dropped** | E1 · E3 · E4 |
| `P11-C-09` independence **never tested**; P07 never read | E1 · E3 |
| Addressed-artefact count wrong | E1 · E2 · E3 |
| `B-26`'s universal quantifier **over-extended** | E1 · E2 · E4 |

## 3. `CRITICAL` findings — all verified by P11 at source before acceptance

| # | Finding | Verified |
|---|---|---|
| `X2-C1` | **`47` candidates is `53`.** Re-executing P11's own declared pattern returns 53 paths. And §3's table enumerates **18** addressed artefacts, not 12. `53 − 18 = 35`, exactly the *"remaining 35"* P11 published — **the arithmetic in the paragraph contradicts the headline in the same paragraph** | ✔ re-executed: 53 |
| `X4-C1` | **The `P09` chain is SIX deep, not four.** `D24`, `D26`, `D27` exist at P09's frozen head; `D26` (10:42) and `D27` (14:18) post-date `D25` (09:01). P11 took generation 4 **in the document stating "a claim is current only at its last statement"** | ✔ all three exist, dates confirmed |
| `X4-C1b` | **`B-23` rests on a withdrawn position.** `D26`: *"`B7` is **PARTIALLY WITHDRAWN** … **Every mechanism claim in this programme is version-matched to at least two real deployments**"* | ✔ verbatim |
| `X4-C2` | **The declared blind spot is the wrong shape.** The pattern is `peer-id AND token`; its blind spot is `¬A ∨ ¬B`, not the `¬A ∧ ¬B` P11 declared. **804 files carry a peer id and no token.** The 5-item positive control could only test the half that works | ✔ |
| `X2-C4` | **P02 is recorded *"none addressed to P11"* and this is false in both halves** — the pattern returns two P02 hits, and `43_G02_P02_FINAL_CLEANROOM_HANDOFF.md` carries a section headed **"What P11 Receives"** | ✔ |
| `X1-C5` | **P11 wrote *"no evidence says the module fired"* while P06 states it *"has already been run and produced user-visible breakage"*** — a sentence **P11 itself carried at CORR1** | ✔ P06 `70_:13`; 4 CORR1 occurrences |
| `X1-C1` | **`P11-C-12` equivocates on "reconciliation"** — the "exists" half is open-item matching (P01), the "vacuous" half is control-account tie-out (P08). Two mechanisms, one sentence | ✔ |
| `X3-X1` | **`P11-C-09` is one responder satisfying two requesters.** P06's own basis column: `P07-R-01` closes *"`X-07`, and P08's `XP-05`"*; **`PBD-F-04`: "`P07-R-01` and `P07-R-03` are the same two requirements P08 asked for."** And **no cited id asserts *identity*** | ✔ verbatim |
| `X2-C11` | **`B-26`'s mechanism is incoherent for 3 of 6 named zeros.** `ON DELETE SET NULL` NULLs foreign keys; a seal flag, a company lock date and a marker-absence in a fully-populated table are not FKs to deleted parents. **An *unfiltered* table delete leaves 0 lines, not 447,384 lines with zero COGS** | ✔ |
| `X2-C12` | **The 30 withheld cells' warrant cites a section P11 marked `SUPERSEDED`**, and its factual premise (*"P01–P10 have published nothing"*) is dead at this SHA | ✔ |
| `X4-C7` | **`OC-06` was adjudicable inside P11's own frozen population.** P02 `45_` `C-86`: *"**MAJOR REVERSAL** … THE REFERENCE DISTRIBUTIONS EXIST"*, a **950-module 16.0 Enterprise** distribution | ✔ verbatim |
| `X1-N1` | **`฿29,029,467.66` received-not-invoiced — headed by P01 *"THE NUMBER P11 AND P08 BOTH NEED"* — appears `0` times in P11's package.** *"Recognised nowhere in the ledger — no receipt entry, no clearing balance, no accrual"* | ✔ 0 occurrences |

## 4. `HIGH` findings accepted

| # | Finding | Verified |
|---|---|---|
| `X2-C10` | *"The CRITICAL count went up"* is **false**. CORR1 had **3** CRITICAL open (`B-17`, `B-21`, `B-23`), not 2. It is **3 → 3, unchanged** | ✔ executed: 3 |
| `X2-C8` | Decision population is **19**, not 18 — `D-3b` is a full row by P11's own ruling | ✔ |
| `X2-C9` | **`D-10` re-declared "discharged"** after CORR1 struck exactly that word: *"~~DISCHARGED~~ corrected per `D-05`: an authorisation cannot be discharged by the party performing the act"* | ✔ verbatim |
| `X2-C3` | *"13 new from 7 peers"* is **9 new files from 6 peers** (11 from 7 if modifications count) | accepted |
| `X2-C6` / `X1-4` | P06's qualifiers **elided in the artefact whose whole purpose is scope repair** — CORR1 had written *"not elided"* | ✔ |
| `X1-3` | The matrix says *"0 of 7 subledgers of record"*, dropping **"unqualified"**; the re-run records Inventory **and** Asset as `OF RECORD` | ✔ |
| `X1-4b` / `X2-C7` | B-17 §4 states Inventory's CORR1 verdict was *"derived view"*. It was **`OF RECORD — with a disclosed agreement rule`**. And the population was silently redrawn **10 → 7**, dropping the `UNKNOWN` row | ✔ verbatim |
| `X4-C4b` | `47,801` is **96.2 % migrated series-14**; the defensible series-18 runtime set is **558** (`ERR-P01-27`) — absent package-wide | ✔ verbatim |
| `X4-C4c` | P01 headed a section *"THE ITEM MOST LIKELY TO BE MIS-CARRIED"* warning that the series-18 and series-19 zeros are **same shape, different cause**, and that merging them makes **both available errors**. `B-26` merges them | ✔ |
| `X2-C13` | The **Boss-facing gate pack** carries **six stale counts** and no supersession banner | ✔ |
| `X4-C6` / `X2-R3` | `B-25`/`B-26` declare blanket downgrades **executed on no row**, while the same run dispositions the downgraded claims `FACT VERIFIED — CLOSED` | ✔ |
| `X1-6` | **P11 decides `D-18` twice, in opposite directions**, while attesting *"0 of 18 decided"* — permitted-but-unfired **fails** `S3-DEP` and **downgrades** `B-26` | accepted |
| `X4-C7b` | Domain-purity register attests *"No file content read outside the 12"* — **false**; P11 read `P09 D23`/`D25` and `P08 52_V2` | ✔ |

## 5. Disputed — in part, and stated with the reason

| # | Expert claim | P11's position |
|---|---|---|
| `X1-1` | `P11-C-12`'s party-dimension claim is *falsified* by 10 of 1,904 mis-typed payables | **Partly accepted.** The counterexample is real and is accepted as bounding the claim — the identity holds only if the filter predicate is right, and it is measurably not. **But P08's structural point survives within its own scope**: where the subledger *is* the ledger filtered by account, agreement is not evidence. The claim is **re-scoped, not withdrawn** |
| `X1-9` | `OC-01`/`OC-02` are one peer finding split in two | **Disputed.** P08 states one kernel requirement over **two distinct stores**; the asset register and the inventory valuation record have different owners, different tie-out counterparties and different remedies. **One requirement, two items.** The *count* is corrected to 10 and the register says so |
| `X2-R4` | The FK strengthens `S4`, not `S3` | **Accepted as a criterion correction, disputed as a defect of the conclusion.** The item is re-filed under `S4`. `S3-DEP`'s status is re-derived in §6 without it |

## 6. What survives, and it is less than the round claimed

| Survives | Basis |
|---|---|
| **10 of 10 peer heads moved** | fully re-derived by E2, commit distances 2–45 |
| **Error population 37 / method 6** | re-derived by executing P11's declared rule; ids contiguous |
| **Tolerance-zero 15**, blocker arithmetic **26 / 22** | re-derived |
| **`P11-E-36`, `P11-E-37`** — P11's self-caught errors | verified by E2 and E4 as genuine and correctly reasoned |
| **`OC-08` / `P11-F-15`** gross-not-net, 43× | *"the strongest genuinely P11-authored accounting statements in the package"* (E3) |
| **The `S3-SRC`/`S3-DEP` method** | *"the strongest single piece of reasoning in the package"* (E1) — **and P11 did not apply it uniformly** |
| **Quotation fidelity to P09, P03, P05, P04** | verified exact by E1 and E2 |
| **6 contamination stops** | verified genuine by E1 |

> **The method is stronger than any peer artefact reviewed. The counts published under it are not.**
> That is E2's summary and P11 adopts it.

**`CP-P11C2-11` — COMPLETE — `CONTRADICTED`.**
