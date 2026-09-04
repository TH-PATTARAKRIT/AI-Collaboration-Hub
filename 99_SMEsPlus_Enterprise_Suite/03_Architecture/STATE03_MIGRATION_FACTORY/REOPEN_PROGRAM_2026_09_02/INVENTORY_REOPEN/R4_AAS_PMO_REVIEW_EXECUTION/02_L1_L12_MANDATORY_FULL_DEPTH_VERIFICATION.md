# [SMEPLUS-26-09-04-INV-R4-AAS-PMO-REVIEW-001]
# 02 — L1-L12 Mandatory Full Depth Verification

Control Level: `/L9999.9999`
Standard Applied: `L1-L12 MANDATORY FULL DEPTH + L13+ NO CEILING`
Status: `VERIFIED WITH TWO NAMED SHORTFALLS — DEPTH SUBSTANTIALLY MET — ONE SHORTFALL IS MATERIAL UNDER THE CORRECTED STANDARD`

---

## 1. What Is Being Verified

Not "did R4 produce twelve files". The question is whether each level was worked to **full depth**, and where it was not, whether the shortfall is disclosed with a named cause and an owner.

The corrected standard forbids reading "L1-L12 minimum" as permission to stop early. This review applies the corrected reading, including where it is **less favourable to R4 than the standard R4 was executed under**.

---

## 2. Level-By-Level Verification

| Level | R4 File | Mandated Coverage | Achieved | Depth Verdict |
|---|---|---|---|---|
| `L1` Domain understanding | `02` | 29 menus | 29 | **FULL** — plus a menu identifier crosswalk preserving prior lineage |
| `L2` UI / field / configuration forensic | `03` | 29 menus | 23 COMPLETE, 6 PARTIAL | **FULL WITH NAMED PARTIALS** — see §3 |
| `L3` Function forensic | `04` | all controlled functions | 41 functions, 8 forensic dimensions each | **FULL** |
| `L4` Cross-module dependency | `05` | all handoffs | Handoff set mapped against the 16-element contract | **FULL** — and deepened beyond prior rounds by applying a contract that post-dates them |
| `L5` Whole-system semantics | `06` | 10 mandated | 10 of 10 | **FULL** |
| `L6` Contradiction / failure / edge case | `07` | 15 mandated | 15 of 15, plus 4 additional | **FULL, EXCEEDED** |
| `L7` Inventory / internal control | `08` | 10 mandated | 10 of 10 | **FULL** |
| `L8` Data identity / immutability | `09` | 15 mandated entities | 15 of 15 | **FULL** — assessed by R4's own overlay as its strongest area; this review concurs |
| `L9` SaaS / multi-tenant / multi-company | `10` | 8 proofs | 8 attempted, **0 achieved** | **FULL IN ATTEMPT, NIL IN RESULT** — see §4 |
| `L10` Migration / historical continuity | `11` | 10 areas | 10 of 10 | **FULL** |
| `L11` Reconciliation / end-to-end proof | `12` | 10 scenarios + Boss 22 | 10 of 10, and 22 of 22 covered on the Inventory side | **FULL IN COVERAGE, 0 PROVABLE** — see `04` |
| `L12` AAS+ adversarial challenge | `13` | 9 Council + 9 Special Team + 4 Overlay | All three layers, not collapsed | **FULL** — see §6 |

**Twelve of twelve levels have a dedicated register and none was skipped or deferred.**

---

## 3. The Six L2 Partials — Assessed

R4 records six menus as `L2 PARTIAL` with named causes. This review tested whether each cause is a genuine evidentiary barrier or a work choice.

| Menu | R4's Stated Cause | Review Assessment |
|---|---|---|
| `INV-M08` Product Variants | Attribute-set change semantics need a live instance test | **Genuine barrier.** Live-instance access is recorded unavailable (`R4-EG-04`) |
| `INV-M15` Warehouse Analysis | Measure set never evidenced in any round | **Genuine barrier**, and it is a *Thai validation* barrier, not a research barrier. Correctly owned "Boss to commission" |
| `INV-M22` Storage Categories | Thai regulated-storage mapping unevidenced | **Genuine barrier.** Correctly routed to Accounting-Tax, not answered |
| `INV-M23` Putaway Rules | Separation decision precondition-blocked on `JT-01` | **Genuine barrier.** Structure *was* established; only the decision is blocked. Arguably this is L2-complete with a downstream block rather than an L2 partial |
| `INV-M26` Product Packagings | Retrospective-change semantics unproven | **Genuine barrier** — live instance |
| `INV-M28` Barcode Nomenclatures | Real Thai supplier formats unevidenced | **Genuine barrier** — Thai field validation |

**Verdict: 6 of 6 partials have a real, named, non-discretionary cause.** Five are blocked on evidence the session could not obtain; one (`INV-M23`) is arguably mislabelled conservatively, which errs in the correct direction.

The counts reproduce independently: 23 `L2 COMPLETE` + 6 `L2 PARTIAL` = 29 rows.

---

## 4. L9 — Full Depth In Attempt, Nil In Result

This is the level most likely to be misread, so it is stated precisely.

R4 achieved **0 of 8** mandated isolation proofs. That is not a depth failure. The proofs are unachievable because `RISK-U03` — the Inventory-side multi-tenant invariant set — **does not exist**, and an isolation property cannot be proven against a specification that has never been written.

What R4 did at L9 instead is the correct response to that condition: it confirmed the gap is open, produced two new first-hand structural findings that make the gap concrete (`R4-F-06` company-less traceable identities, `R4-F-09` company-less locations), added a derived-surface requirement (`R4-F-22`), and stated per proof what would have to exist for it to become attemptable.

AAS+ Track 05 (IESA) challenged whether L9 should have been attempted at all rather than marked blocked. This review sides with R4 against that challenge: a blocked marker would have produced none of the three contributions above, and `R4-F-06` and `R4-F-09` are among the most load-bearing findings in the package.

**`0 of 8` must be carried into every downstream summary without softening.** This review restates it here for that purpose.

---

## 5. The Shortfall That Is Material Under The Corrected Standard

This is this review's principal L1-L12 finding, and it is one R4 could not have made about itself.

`R4-D-05` discloses that two specific, named, reachable leads were **not** followed despite primary-source access being available and used for thirteen other findings:

- `C-04` / `N-CONC-01` — reservation locking sufficiency.
- `N-A13-01` — the unread manual-override path onto the derived available quantity.

R4's stated reason is that it "prioritised breadth across 29 menus and 12 levels". AAS+ Track 07 raised this as a fair criticism and R4 accepted it without qualification.

**Under the standard R4 executed against** — `LEVEL 1 TO LEVEL 12 MINIMUM` — that trade is defensible. Breadth to the mandated floor across all 29 menus is precisely what a minimum standard asks for.

**Under the corrected standard** — `L1-L12 MANDATORY FULL DEPTH` — it reads differently. Full depth is not satisfied by declining a reachable line of inquiry in order to preserve breadth. Two integrity questions that were *within reach with the access this session actually held* were left open across a sixth round.

This is not a criticism of R4's judgement at the time. File `25`, which issued the corrected wording, was committed **after** files `00`-`24` were published (`fc0b168` follows `bdef581`). R4 could not have applied a standard that did not yet exist when it worked.

It is, however, a live consequence for what happens next:

| Consequence | Statement |
|---|---|
| Is R4's L1-L12 execution invalidated? | **No.** It met the standard in force when executed |
| Is R4's L1-L12 execution complete against the corrected standard? | **No.** Two named reachable leads remain unfollowed |
| What closes the gap? | One bounded verification pass on `C-04` and `N-A13-01`, using the same primary-source access R4 demonstrated |
| Is that pass a new Deep Research round? | **No.** It is a targeted continuation, and it is small |

Recorded as `REV-F-01`, severity `MATERIAL`, Lane A, owner Inventory / Track 07. It is carried into the PMO recommendation at `11` and the Boss decision package at `12`.

---

## 6. L12 Was Executed At Full Structure, Conditionally

The three challenge layers were kept distinct and not collapsed — 9 Council tracks, 9 Special Teams, 4 Overlay roles, each with separate content. Verdict distribution reproduces: **7 `HOLD`, 2 `CONTINUE_WITH_NOTES`, 0 `FAIL / FROZEN`**, reconciled to the conservative label `HOLD / EVIDENCE REQUIRED`.

The challenge is genuinely adversarial rather than self-congratulatory. Tracks 04 and 07 each extracted a correction R4 then accepted against its own interest — Track 04 forcing R4 to concede that `R4-F-16`'s components are not new, only their conjunction is; Track 07 forcing the `R4-D-05` disclosure. This review regards those two exchanges as the strongest internal evidence that L12 was performed rather than performed-at.

**The conditionality stands and is not resolved by this review.** `U-07` records two competing 9 Veto Council charters, both claiming Boss approval. R4 followed the canonical roster and disclosed the conditionality at `13` §1.1 rather than burying it. If Boss rules the other charter governs, the L12 challenge must be re-run. Carried to `08` and `12`.

---

## 7. Depth Verification Verdict

| Question | Answer |
|---|---|
| Were all twelve levels executed? | **Yes — 12 of 12, none skipped, none deferred** |
| Were all 29 menus traced through L1-L12? | **Yes — 29 of 29, 0 menu-level HOLDs** |
| Were level-specific partials disclosed with named causes and owners? | **Yes — 6 of 6 at L2, all with genuine barriers** |
| Was the zero result at L9 disclosed without softening? | **Yes** |
| Was L12 executed at full structure? | **Yes, conditional on `U-07`** |
| Does R4 satisfy `L1-L12 MANDATORY FULL DEPTH` in full? | **Substantially — with one material shortfall (`REV-F-01`), and one that arises from a standard published after execution** |

**Verdict: `L1-L12 MANDATORY FULL DEPTH — SUBSTANTIALLY MET, ONE MATERIAL SHORTFALL NAMED.`**

This review does not recommend re-running R4. It recommends closing `REV-F-01` by a bounded targeted pass, which is the same action AAS+ Track 07 and PMO Recommendation 7 already ask for, now additionally justified by the corrected depth standard.

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
