# [SMEPLUS-26-09-05-INV-MTI-CONTROLLED-REMEDIATION-001]
# 12 — AAS+ Adversarial Challenge And Verdict

Level: `L12 — adversarial audit challenge and veto`, with `L13+` escalation at §6
Reviewer: `AAS+ — AI Audit SMEsPlus`
Control Level: `/L9999.9999`
Status: `CHALLENGE COMPLETE — CONTROLLING VERDICT: HOLD / CONFORMANCE RE-SPECIFIED, NOT VERIFIED — 2 VETOES ISSUED, 4 INHERITED, 0 DISCHARGED — NO PASS DECLARED`

---

## 1. Standing Rules And Inherited Conditionality

AAS+ may not declare Gate `PASS`, Boss approval, Team B or Team C authorization, development readiness, merge, release or production. **Boss is the sole Final Approver.**

**Charter conditionality carried, not resolved.** `U-07` records two competing 9 Veto Council charters, both claiming Boss approval. R4 disclosed it; the AAS+ / PMO review inherited it; the invariant set inherited it; the consolidation inherited it; **this session inherits it a fifth time.** If Boss rules the other charter governs, this verdict's structure must be re-run.

**Reliance conditionality carried, not resolved.** The `C-05` containment ruling is outstanding and the R4 review confirmed the exposure live in a fresh clone. Downstream reliance on Inventory evidence — **including this package** — remains locked until Boss rules. A re-specification of locked evidence is itself locked.

This challenge is adversarial toward **this session's own work first**. Confirming one's own re-specification is worth nothing.

**Method note.** Every parent finding cited in this package was taken from its source's **adversarial or correction section**, never from its summary. `11` §2 and §5 of the consolidation, `12` §2 of the invariant set, and `10` §4 of the review were read **before** the headline tables of the packages that contain them.

---

## 2. Attacks Made On This Session's Own Work

| # | Attack | Outcome |
|---:|---|---|
| 1 | **"This is a diff of the invariant set dressed as a design."** | **Failed.** Thirty-two deltas, fourteen re-specified invariants, eight added, twelve proof requirements, two handoff fields, one enforcement-point class and a sixty-cell negative specification appear in no prior document. Two structural gaps — `CF-F-04`, `CF-F-05` — are found by composing two rulings that no prior package composed |
| 2 | **"`CF-F-02` widens `RC-V-01`, and widening a veto is not your act."** | **Failed — and the package pre-empts it.** `02` §2 states explicitly *"this session does not amend `RC-V-01`"*, supplies the evidence, and routes the widening to AAS+ and Boss. The finding is that the **condition** is under-inclusive, which is an observation about a test, not a change to a veto |
| 3 | **"`CD-12` .. `CD-14` move three object classes Boss never mentioned. That is your design position, not a ruling consequence."** | **Partially succeeded, and the split is disclosed.** For rows 7 and 16 the attack fails: `MTI-D-03` §3 names *Product Category* and *Barcode Nomenclature* explicitly, `MTI-34` requires tenant configuration to carry a `CTX`, `MTI-04` forbids a null company, and `RC-P-36` already states the resulting acceptance criterion. For row 17 the attack **succeeds in part**: whether `MTI-D-03`'s *"Unit of Measure Category"* is the matrix's *"Unit group and unit (`CN-14`)"* is a naming question, and **it is registered as `CF-D-01` with all three readings and their consequences, and not chosen.** Recorded as `CF-CH-01` |
| 4 | **"`CF-I-05` invents a platform operation class Boss did not ask for."** | **Partially succeeded.** The **gap** is real and composed from two rulings. The **remedy shape** is a design choice, and an alternative exists — that platform-level controls over operation types simply do not exist, which is option (c) of `CF-D-02` and is stated. `CF-I-05` is `SPECIFIED — CONDITIONAL` on that decision precisely so the option stays open. Recorded as `CF-CH-02` |
| 5 | **"`CF-F-05` is a negative claim over a set you chose."** | **Failed as stated, upheld in method.** The population is not author-chosen: it is the complete published invariant set, 50 of 50 rows, and the enumeration was mechanical. **Boundary `B-02` is declared at `01` §8**, the result is classed **`A` within that boundary and `B` for the wider system**, and the wider claim is never made. That is the standard the programme's negative-claim rule requires, and it is met — but the attack correctly notes that a boundary declared by the author is still a boundary declared by the author, and **only independent review can test it** |
| 6 | **"You added eight invariants and twelve proof requirements to a set already criticised as un-minimised."** | **Upheld, and disclosed.** `MTI-CH-02` records that the published 50 were made complete rather than minimal. **The set is now 58 and the criticism is worse, not better.** `03` §15 states it directly. The defence — that each addition traces to a ruling clause or a composed gap — is a reason each addition is warranted, not a reason the set is minimal |
| 7 | **"`CF-P-10` is count-padding. You made theme 6 look better without touching the mapping layer."** | **Partially succeeded, and the package pre-empts it.** `08` §5.1 states: *"That is a change in definability of one requirement. It is not progress toward the mapping layer, and it does not reduce `RC-F-03`."* `10` §3 says the same. **The attack is correct that the theme's count improves and the theme's blocker does not, and the package says so in two places rather than one** |
| 8 | **"You say `RC-F-05` is specified and also that it is not closed. Which is it?"** | **Failed.** Both. `RC-F-05`'s own wording is *"the gap is in the specification"*; the specification now exists at `04` and `CF-I-02`. **A finding closes when the thing it describes is built and independently verified, not when it is described.** `04` §10 and `11` §5 both state the position |
| 9 | **"The Payment answer is a non-answer dressed as a discharge."** | **Partially succeeded.** The authorization asked for an obligation **or** a reason, and both are supplied: five obligations at `PAY-01` .. `PAY-05`, and a declared search boundary returning **zero** published Inventory-to-Payment handoffs. **But the underlying scope question is routed, not answered** — `CF-D-04` — and `RC-F-09` is therefore *discharged as a coverage item* rather than closed. **A reader could reasonably call that a gap identified and deferred. That is exactly what it is, and `07` §4.4 says so** |
| 10 | **"You executed an authorization whose own header says it is not authorized."** | **Upheld, and disclosed.** The header reads *"It is not authorized until Boss commissions it. Do not execute on the strength of this file alone."* This session executed on Boss's instruction to execute it. **The commissioning act is Boss's; this session records the basis it ran on and does not assert its own authorization.** `CF-EN-03` |
| 11 | **"Element 10's status is unchanged, so nothing was achieved."** | **Failed as stated, upheld in substance.** Element 10 is `specified, not built, not verified` before and after, stated in that wording and no other in five places. **What changed is that its obligation is now larger** — two attestations rather than one, one of which references a control that does not exist. **That moves the target further away.** The package presents it as such and not as progress |
| 12 | **"No Thai validation, so the whole conformed set is unfounded."** | **Upheld, and disclosed.** Nothing here is Thai-validated. `0 of 78`, unremedied since 2026-08-30. **The rulings and now this package make the checklist larger**: every configurable record class, every operation type, and every platform operation-class name `CF-I-05` would introduce is a further unvalidated label. `03` §14, `04` §10 and `11` §5 all carry it |

**Five attacks failed outright. Four partially succeeded. Three were upheld and disclosed.**

The three that landed hardest — `CF-CH-01`, `CF-CH-02`, and attack 6 — are all cases where a re-specification session reached the edge of its authority or made its parent's known weakness worse. **That is the correct place for a re-specification session to be stopped.**

### 2.1 Challenge items raised against this session

| ID | Item | Disposition |
|---|---|---|
| `CF-CH-01` | The row-17 anchor change rests on a naming equivalence this session cannot establish | Registered as `CF-D-01` with three readings. `CD-14` and `CF-F-01` both carry the qualifier **everywhere they are stated** |
| `CF-CH-02` | `CF-I-05` supplies a remedy shape for a gap Boss has not been asked about | `SPECIFIED — CONDITIONAL (CF-D-02)`, with a withdrawal option stated as `CF-D-02` option (c) |
| `CF-CH-03` | The set grew from 50 to 58 while `MTI-CH-02` records it as already un-minimised | Disclosed at `03` §15 and here. **Not remedied.** Minimisation is a later pass and is not in this authorization |

---

## 3. Verdict By Challenge Track

| Track | Question | Verdict |
|---|---|---|
| **T1 — Evidence integrity** | Were all mandatory sources fetched, resolved and verified? | **CONTINUE_WITH_NOTES.** 6 of 6 stated tips match; **70 of 70 digests** recomputed and matched across four upstream manifests; 42 of 42 mandatory files read; both governing Boss controls read at source; **0 sources missing**. Four evidence notes raised, one of which is a **correction to the authorization's own ancestry statement** |
| **T2 — Ruling fidelity** | Are the three rulings carried exactly, without softening or extension? | **CONTINUE_WITH_NOTES.** The §5 carry-forward block is carried verbatim. **One fidelity observation raised against the parent, not this session** — `CF-F-06`, where a control rule attributes to `MTI-D-01` rule 6 a module list that rule 6 does not contain. Where the published design contradicts a ruling, **the design changes and the ruling stands**, at every one of the 32 deltas |
| **T3 — Authority boundary** | Did the session decide anything belonging to Boss? | **HOLD.** **No decision taken.** Four decision items raised and **routed with options, never chosen**. `SME-Q-02`, `SME-Q-03`, `MTI-D-06` untouched. `C-02` severity not classified. `MTI-D-04`, `MTI-D-05`, `RC-D-01` .. `RC-D-04` not answered. **No Thai statutory claim of any kind.** The closest approaches are `CF-CH-01` and `CF-CH-02`, both disclosed |
| **T4 — Closure honesty** | Is any item recorded as closed because a specification exists? | **CONTINUE_WITH_NOTES.** **0 findings, 0 proofs, 0 gaps, 0 capabilities, 0 dependencies, 0 vetoes closed or discharged.** `RC-F-09` is explicitly *discharged as a coverage item*, which is stated not to be a closure. `RC-F-05`'s specification half is supplied and the finding is stated as open in three places |
| **T5 — Specification versus proof** | Is the distinction maintained? | **CONTINUE_WITH_NOTES.** `08` §1 states it as the file's organising principle; **`0 of 60` executable** is stated four times; `0 of 60` negative cases executed; the word *proven* is applied to nothing. **Definability movement is reported in both directions**, including one regression — `RC-P-16` |
| **T6 — Accounting COGS boundary** | Was any valuation conclusion trespassed? | **HOLD / EVIDENCE REQUIRED.** **No trespass found.** `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` is carried on `CD-11`, `CD-12`'s costing facet, `CD-32` elements 4 and 7, `RC-P-22`, `RC-P-34` value half, `RC-P-39` costing facet, `XCR-01`, `XCR-02`, surfaces 10 and 13 of the rejection matrix, `MTI-16`, `MTI-23`, `MTI-33`, `MTI-46` and `PAY-05`. **`AAS-V-03` carried in force. 10 of 10 dependency areas remain locked and none is upgraded** |
| **T7 — Thai and business reality** | Is any Thai or statutory claim made? | **HOLD.** **None.** `TH-HOLD-06` respected — `CD-30` records that `MTI-07`'s prohibition on equating a warehouse with a Thai tax branch survives `MTI-D-02` intact, because an authorization axis is operational and a tax branch is statutory. The withholding example at `06` §2 is recorded as **Boss's stated business reason**, explicitly not as a statement of Thai tax law. `0 of 78`, and the surface is **widened again** |
| **T8 — Clean-room** | Is the Layer 1 boundary held? | **HOLD.** Self-scan at §4. **No first-hand reference-system inspection performed; no quarantine accessed.** `C-05` reliance lock inherited and **not** discharged. `RISK-CR-02` **not** further discharged |
| **T9 — Conformance completeness** | Does the re-specification cover every item the rulings touch? | **HOLD.** All 50 invariants, all 35 matrix rows, all 41 functions, all 4 register entries, all 16 contract elements, all 8 consuming modules, all 13 themes and all 48 carried proof requirements are individually assessed. **But completeness cannot be self-certified**: `CF-F-02` shows the parent's own discharge condition was under-inclusive, which is direct evidence that a conformance set is exactly the kind of enumeration an author gets wrong. **`RC-V-01` is discharged by an independent check, not by this document** |

**Distribution: 5 `HOLD`, 4 `CONTINUE_WITH_NOTES`, 0 `FAIL / FROZEN`.** Reconciled to the conservative label.

---

## 4. Clean-Room Position

| Control | Result |
|---|---|
| Vendor product or model identifiers | **0** — this package names no system |
| Vendor technical tokens, field names, method names, file paths, line references | **0** |
| Code fragments or fenced code blocks | **0.** The two fenced blocks are the carry-forward ruling text at `00` §1 and the two-tuple notation at `04` §2, both governance and design wording |
| Schema, DDL, ORM structure or migration script | **0** |
| Reference-system language used | `reference ERP`, `reference pattern`, `reference behaviour` only, and only where carried from a cited upstream statement |
| Reference behaviour adopted by this session | **0.** `MTI-10`'s route-to-rule consistency is carried as an existing invariant, not newly adopted |
| Thai candidate strings introduced | **0** |
| First-hand reference-system inspection performed | **None** |
| Quarantine accessed | **None** |
| Files created, modified or deleted outside the output folder | **0** |

**`RISK-CR-02` is not further discharged by this session.** The residual scope the R4 review defined — Layer 2 findings, quarantine citations, Thai content — is unchanged.

---

## 5. Veto Status — The Section That Matters Most

### 5.1 The four inherited vetoes

| ID | Veto | Status After This Session |
|---|---|---|
| **`AAS-V-01`** | Veto on recording handoff element 10 as supplied, satisfied or suppliable. Its status is `specified, not built, not verified` and **no other wording may be substituted** | **IN FORCE, UNCHANGED.** The wording is used and no other in `02`, `03`, `07`, `08` and `14`. **The obligation is widened, which moves element 10 further from supply, not closer** |
| **`AAS-V-02`** | Veto on implementation start before `MTI-D-01`, `MTI-D-02` and `MTI-D-03` are ruled | **CONDITION SATISFIED — NOT DISCHARGED.** Carried exactly as the consolidation recorded it. **Never reported as lifted.** Discharge is the issuing body's act ratified by Boss |
| **`AAS-V-03`** | Veto on any Cross-Context Report Grant carrying valuation content while the Accounting COGS Gap stands | **IN FORCE, UNCHANGED.** `JT-01` still **NOT DECIDABLE**; `GAP-FS-07` still records the cross-company path as never traced end to end |
| **`RC-V-01`** | Veto on implementation start against `03_INVENTORY_MULTI_TENANT_INVARIANT_SET.md` as published, until `MTI-11`, `XCR-03`, `04` §4.1 and matrix rows 5-7 are re-specified to a company anchor | **IN FORCE — NOT DISCHARGED BY THIS SESSION.** See §5.2 |

### 5.2 `RC-V-01` — the remedy is produced; the veto is not discharged

**What is true:** `RC-V-01`'s stated remedy is *"a bounded re-specification pass (Lane R1), which needs no ruling and no upstream input"*, and its stated discharge is *"executing Lane R1 and having the result independently checked."* **Lane R1 is executed. The result is this package.**

**What does not follow:**

| # | Reason the veto is not discharged |
|---:|---|
| 1 | **The discharge condition has two halves and this session supplies one.** `RC-V-01`'s own wording requires the re-specification **and** an independent check. An author's check of an author's re-specification is not an independent check, and `MCC`-line reasoning applies without exception here: **a control designed by the author is not independent of the author** |
| 2 | **The stated condition is under-inclusive — `CF-F-02`.** It names matrix rows 5-7; rows 16 and 17 also require an anchor change. **Discharging the veto against its literal condition would leave two rows non-conforming**, which is worse than not discharging it. Whether to widen the condition is AAS+'s and Boss's act, not this session's |
| 3 | **One delta in the conformance set is itself conditional.** `CD-14` depends on `CF-D-01`, unruled. A conformance claim resting on an unruled naming question is not a conformance claim |
| 4 | No Boss authorization for development exists in any package in this chain, so nothing turns on the veto's status today in practical terms |

**AAS+ therefore records `RC-V-01` as: `REMEDY PRODUCED — VETO NOT DISCHARGED — DISCHARGE CONDITION UNDER-INCLUSIVE, SEE `CF-F-02``.**

### 5.3 The two vetoes issued by this session

| ID | Veto | Basis |
|---|---|---|
| **`CF-V-01`** | **VETO on recording `HF-CTX-11`, the authorization attestation, or the authority half of handoff element 10, as supplied, available, satisfied or suppliable. Their status is `specified, not built, not verified`, and no other wording may be substituted** | `HF-CTX-11` references the control `CF-I-03` requires, **and that control does not exist** — `CF-F-05`. The field is specified in this package and a downstream reader seeing *"eleven context fields"* would reasonably infer eleven are available. **This is the exact failure `AAS-V-01` exists to prevent, reproduced one axis along**, and it deserves its own veto rather than an assumption that `AAS-V-01` covers it |
| **`CF-V-02`** | **VETO on citing `CF-I-06` as reducing `RC-F-03`, or `CF-I-08` as reducing `RC-F-07`.** `CF-I-06` is a prohibition that holds in the mapping layer's absence and states nothing about the object. `CF-I-08` is a labelling control that states nothing about the Private Company topology | Both are the kind of construct most likely to be read as progress by a later summary. **`10` §3 and §4 already state that neither reduces its root cause**; the veto makes the statement binding rather than advisory. `RC-P-20`, `RC-P-21`, `RC-P-45`, `RC-P-46` and `RC-P-48` remain `NOT DEFINABLE` |

**Both vetoes are on wording and reliance. Neither is a veto on design content, and neither prevents Boss from commissioning any lane.**

**Vetoes in force after this session: 6** — `AAS-V-01`, `AAS-V-02` (condition satisfied, not discharged), `AAS-V-03`, `RC-V-01` (remedy produced, not discharged), `CF-V-01`, `CF-V-02`.
**Vetoes discharged by this session: 0.**

---

## 6. `L13+` Escalation — Two Levels Opened

Opened where the evidence shows complexity that `L1-L12` does not reach. Each carries all six required fields.

### `L13-CF-01` — Authorization conformance as a continuously asserted property

| Field | Content |
|---|---|
| **Trigger** | `CF-F-05`. `MTI-D-02` makes authorization a four-axis property that must be evidenced separately from context (`04` §2.1 rule 4 of the consolidation), while every control in the published set asserts a property of `CTX` |
| **Evidence** | Boundary `B-02`: 8 of 50 invariants carry the `CONTROL` layer; 7 assert context, 1 asserts retention; `MTI-30` asserts a runtime precondition on one path. `HF-CTX-08` carries an authority **value** with no attestation, while `HF-CTX-06` carries a context attestation — the asymmetry `06` §3.1 of the invariant set identifies as the difference between carriage and guarantee |
| **Why `L1-L12` is insufficient** | `L7` treats internal control as a property of a **design** — who may do what. `L8` treats identity and immutability as properties of a **record**. Neither addresses a property of the **relationship between an act and a grant over time**, which is what an authorization conformance control asserts: not that a rule exists, and not that a record is right, but that every act that happened was permitted **when it happened**. `L11`'s reconciliation vocabulary is the nearest and it reconciles populations, not permissions |
| **Objective** | Define what an authorization conformance control asserts, over what population, at what cadence, what a breach is, what it may never silently repair, how its runs are retained and referenced, and how `HF-CTX-11` cites one |
| **Checkpoint** | Complete when `CF-P-06` can be executed against an implementation and `HF-CTX-11` references a control that exists |
| **Impact on Boss decision** | **Small in scope and it lands inside the same implementation as the invariant set.** It should be commissioned **with** that build, not after it: retrofitting a conformance control over acts already recorded without a resolved `AUTH` tuple is materially harder than building it in. `AAS-V-02` and `RC-V-01` both stand in front of any such build |

### `L13-CF-02` — Platform-owned classification over a tenant-owned enumeration

| Field | Content |
|---|---|
| **Trigger** | `CF-F-04`. `MTI-D-02` makes operation type an authorization axis over an enumeration explicitly *"not limited to"* its examples; `MTI-D-03` makes Operation Type tenant-configurable; nothing maps a tenant type to a platform class |
| **Evidence** | `MTI-D-02` §5's eight illustrative types; `MTI-D-03` §3's configurable list; `RC-P-14`'s published note that the test set *"must be derived from the implemented set, not from the ruling's examples"*; `L7-09` and `R4-F-21` on segregation of duties; `MTI-33`, which solves exactly this problem for **reason** classification and is the only precedent in the set |
| **Why `L1-L12` is insufficient** | `L2` treats configuration as a **surface**; `L9` treats the tenant boundary as a **prohibition**. Neither addresses the case where a **control's own vocabulary** is tenant-owned — where the platform is not trying to reach into a tenant's data but to **name** something inside it in order to constrain it. It is a modelling problem about the boundary itself, not about crossing it |
| **Objective** | Define the platform-owned operation-class model: what a class is, what declaring one obliges, why the declaration is immutable after a completed movement, how platform controls bind to a class, and what happens to a tenant type whose class is withdrawn |
| **Checkpoint** | Complete when `CF-P-03` is `DEFINABLE` unconditionally and `RC-P-16` returns to a single condition |
| **Impact on Boss decision** | **Gated on `CF-D-02`, which is a Boss decision including the option to rule the whole construct out.** Ruling it out is a perfectly good ruling and would withdraw `CF-I-05`; leaving it unruled leaves segregation of duties expressible per tenant and unstatable per platform |

---

## 7. Controlling AAS+ Verdict

**`HOLD` — CONFORMANCE RE-SPECIFIED, NOT VERIFIED.**

Five of nine challenge tracks return `HOLD`. None reached `FAIL / FROZEN`. Reconciled to the conservative label.

| Dimension | Assessment |
|---|---|
| **The three rulings** | Carried exactly. Where the published design contradicted one, **the design changed at every point and the ruling stood at every point** |
| **The conformance set** | **Larger than the veto that demands it.** 32 deltas against a discharge condition naming four artifacts. Two structural gaps found by composing rulings that no prior package composed |
| **The re-specification itself** | Assessed as internally consistent (`03` §14), attached to every function and surface it must govern (`04` §6), and **not verified, not validated, not minimised** |
| **`RC-V-01`** | **Remedy produced. Veto not discharged**, and its stated condition is under-inclusive — `CF-F-02` |
| **`RISK-U03` / `GAP-FS-10`** | **REMAINS OPEN.** The item is the capability; this session produced a conformed specification of it |
| **The 8 L9 proofs** | **`0 of 8` unchanged.** One requirement gained definability, one lost it |
| **The 22 cross-proof scenarios** | **`0 of 22` unchanged.** No scenario's position moves |
| **The 10 material handoffs** | **`0 of 10` unchanged.** Four contract elements had their obligations **widened** |
| **Accounting COGS dependency** | **`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`** — 10 of 10 areas locked, not lifted, no trespass found |
| **Thai validation** | **`HOLD`** — `0 of 78`, over a **larger** surface than before |
| **`C-05` / `U-07`** | **Both remain governance blockers.** This package inherits both locks |
| **Clean-room, Layer 1** | Held on this session's own scan. `RISK-CR-02` residual unchanged |
| **Inventory Final Solution v2.0** | **NOT READY.** `0 of 12` Joint decisions ready, 3 **NOT DECIDABLE**, `0 of 22` provable |
| **Development Final Gate** | **NOT IN SCOPE AND NOT APPROACHED.** No AAS+ member is empowered to approach it |

**This package is suitable to proceed as a controlled input to an independent conformance check, subject to `RC-V-01`, `CF-V-01`, `CF-V-02` and every hold carried at `11`.** That is a recommendation to Boss. It is not an approval, and AAS+ cannot make it one.

---

## 8. Not Declared

This verdict does not declare, and no member of AAS+ is empowered to declare: `PASS`, `APPROVED`, `CLOSED`, `FINAL SOLUTION ACCEPTED`, `READY FOR DEVELOPMENT`, `READY FOR PRODUCTION`, `TEAM B AUTHORIZED`, `TEAM C AUTHORIZED`, merge approval, or release authorization.

**Items closed by this session: 0. Prior evidence preserved. All carried identifiers unchanged.**

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
