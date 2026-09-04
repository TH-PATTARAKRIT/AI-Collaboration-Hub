# [SMEPLUS-26-09-05-INV-MTI-CONTROLLED-REMEDIATION-001]
# 11 — Open Items And Dependency Register

Control Level: `/L9999.9999`
Status: `19 NEW ITEMS RAISED — 0 PRIOR ITEMS CLOSED — 0 DEPENDENCIES DISCHARGED — ALL CARRIED IDENTIFIERS PRESERVED UNCHANGED`

---

## 1. Lane Vocabulary In Force

This register uses **the authorization's lane vocabulary**, which is the vocabulary the AAS+ / PMO review, the invariant-set package and the consolidation all used.

| Letter | Meaning here |
|---|---|
| **A** | Inventory-owned architecture / control / data identity |
| **B** | Accounting COGS / valuation / period-close dependency |
| **C** | Business SME / Thai user / statutory validation |
| **D** | Clean-room / governance / audit veto / Boss ruling |
| **E** | Cross-module joint decision |
| **F** | Duplicate / superseded / no-action |

`REV-F-03` — the lane-letter collision with R4's own registers, in which Lane C means *COGS-gated* — **remains open**. Until Boss ratifies one vocabulary programme-wide, every cross-document lane reference stays ambiguous. **This session adds a fourth document using the authorization's vocabulary; it does not resolve the collision.**

---

## 2. New Findings — `CF-F-01` .. `CF-F-06`

| ID | Finding | Lane | Severity | Owner | Next Action | Blocks v2.0 | Blocks DFG |
|---|---|---|---|---|---|---|---|
| `CF-F-01` | **The tenant-level shared surface is eliminated in full, not in part.** After conformance no Inventory object class in the 35-row context matrix remains anchored to `tenant` alone. `RC-F-02` records the elimination of one register entry and the voiding of `04` §4.1 *"for product and variant"*; the actual scope is the disappearance of the class | **A** | MATERIAL — **favourable** | Inventory | Correct the matrix and the register; **do not re-introduce a tenant-level definitional class under another name**. Boundary and enumeration at `06` §4 | No | No |
| `CF-F-02` | **`RC-V-01`'s discharge condition is under-inclusive.** It names `MTI-11`, `XCR-03`, `04` §4.1 and matrix rows 5-7. Rows **16** and **17** also require an anchor change, under `MTI-D-03` composed with `MTI-04` and `MTI-34`. Executing the condition exactly as written would leave two rows non-conforming | **D** then **A** | **MATERIAL, bearing on a veto** | **AAS+**, then Boss | **Widen or restate `RC-V-01`. This session does not amend it** — amending a veto is the issuing body's act. Evidence at `02` §2 | **Yes** — the veto's discharge test is the gate | **Yes** |
| `CF-F-03` | **`RC-P-16` becomes doubly conditional — a regression.** It carried one condition (Thai input for the compensating control). It now also carries `CF-D-02`, because a platform-level segregation rule cannot bind to a tenant-defined operation-type label | **A** design / **C** content / **D** ruling | MATERIAL | Inventory + Boss + Thai panel | Rule `CF-D-02`; the Thai half is unchanged and remains Lane C | No | Yes |
| `CF-F-04` | **The operation-type authorization axis ranges over a tenant-owned enumeration with no platform-owned class behind it.** `MTI-D-02` makes it an authorization axis; `MTI-D-03` makes it tenant-configurable; nothing maps a tenant type to a platform classification, so no platform-level control can bind to it | **D** then **A** | **MATERIAL, trending BLOCKING** | Boss + Inventory | `CF-I-05` specifies the shape on the `MTI-33` precedent. **`CF-D-02` closes the class enumeration and is a Boss decision.** `L13-CF-02` | **Yes** | **Yes** |
| `CF-F-05` | **Authorization has no conformance control.** Eight invariants carry the `CONTROL` layer; seven assert a property of `CTX` and the eighth asserts retention. `MTI-30` asserts a runtime precondition on one path, not a conformance property. **The authority half of element 10's widened obligation is carriage, not guarantee** | **A** | **MATERIAL, trending BLOCKING** | Inventory + SaaS Foundation | `CF-I-03` and `HF-CTX-11` specify the remedy. **Neither is built, and `HF-CTX-11` presently references a control that does not exist.** Boundary `B-02`; class `A` in scope, `B` wider. `L13-CF-01` | **Yes** | **Yes** |
| `CF-F-06` | **A control rule cites a ruling clause that does not contain what it cites.** The consolidation's `C-04` attributes an eight-module list including Payment to `MTI-D-01` rule 6; rule 6 names eight modules and **Payment is not among them**. The same package states the position correctly at `07` §9.1, so the `C-04` row compressed two sources under one citation | **D** | Observation | PMO | Quote rule 6 as ruled and cite the authorization's theme 13 separately. **Changes no conclusion** — Payment's obligation is required by theme 13 regardless | No | No |

---

## 3. New Decision Items — `CF-D-01` .. `CF-D-04`

Each requires a decision this session is **not empowered to take. Options are stated. None is chosen.** None is an investigation.

| ID | Decision required | Lane | Owner | Options | Consequence if deferred |
|---|---|---|---|---|---|
| `CF-D-01` | **Is `MTI-D-03`'s *"Unit of Measure Category"* the same object as the context matrix's *"Unit group and unit (`CN-14`)"*?** | **D** | **Boss** | **(a)** Same object — row 17 moves to a company anchor under `CD-14`, and `CF-F-01`'s elimination holds in full. **(b)** Different objects — row 17 stays tenant-anchored, one shared surface survives, `04` §4.1 remains live for it, and it needs its own isolation proof. **(c)** Neither, and the matrix row is out of scope for `MTI-D-03` | `CD-14` stays conditional. **`CF-F-01` cannot be stated without the qualifier**, and one row of the matrix has two possible anchors. `R4-F-13`'s rounding surface is either per-company or tenant-wide, and the two need different proofs |
| `CF-D-02` | **What closes the platform-owned operation-class enumeration, and who approves an addition?** | **D** then **A** | **Boss / product scope** | **(a)** Close it at the eight classes `MTI-D-02` §5 illustrates, plus a named process for adding one. **(b)** Derive it from the `INV-F-*` function set rather than from the ruling's examples. **(c)** Rule that no platform class exists and platform-level controls over operation types are out of scope, in which case `CF-I-05` is withdrawn and `L7-09` segregation stays per-tenant only | `CF-F-04`. `CF-I-05` stays `SPECIFIED — CONDITIONAL`; `CF-P-03` stays conditional; **`RC-P-16` stays doubly conditional**; the whole operation-type column of the rejection matrix at `09` §3 stays inconclusive |
| `CF-D-03` | **What control replaces deduplication as a defence against identity failure, given that deduplication is now prohibited as a default?** | **D** then **A** | **Boss** | **(a)** The controlled mapping / provenance layer — **gated on `MTI-D-04`**, so this option is not available today. **(b)** Per-company catalogue governance as an operational control, with no system object. **(c)** A group-level correspondence **report** with no identity effect — which `M-10` warns becomes the shared master it replaced. **(d)** Accept the exposure in writing | **The exposure is uncontrolled and is stated as uncontrolled** at `06` §6.3. The L8 evidence names duplicate masters over one catalogue a live source of identity failure, and Boss ruled with that cost visible — but no replacement control follows automatically from the ruling |
| `CF-D-04` | **Is Payment a direct consumer of Inventory facts?** | **D** | **Boss / product scope** | **(a)** No — Payment inherits context through Accounting and Purchase; `PAY-01`..`-05` stand as inherited constraints; **cheapest, and consistent with the search result**. **(b)** Yes for at least one flow — a handoff must be mapped, and `0 of 10` becomes `0 of 11`, starting non-compliant on the same three elements. **(c)** Payment is outside Inventory's scope and theme 13's naming is a drafting artefact | `RC-F-09` stays discharged-as-coverage and unclosed. `CF-P-09` stays `DEFINABLE — CONDITIONAL`. `MTI-45` R2's eighth module has an obligation and no handoff |

---

## 4. Evidence Notes — `CF-EN-01` .. `CF-EN-04`

| ID | Note | Lane | Severity | Owner | Action |
|---|---|---|---|---|---|
| `CF-EN-01` | **The authorization's §4.3 ancestry statement is false as written.** `6897cc9` is not a descendant of every evidence commit the prompt names — it is an **ancestor** of `a57bd555`, the consolidation package named at §4.1 as the immediate predecessor. The commit that is a descendant of all six others is `a57bd555`. Inherited from the parent's drafting: file `13` could not cite its own publication commit | **D** | WATCH | PMO | State the base as `a57bd555` in any successor prompt. **No evidence was unavailable and no conclusion depends on the correction.** This session based its branch on `a57bd555` |
| `CF-EN-02` | **`EVIDENCE-NOTE-02` reproduces for a fifth time, in a sharper form.** The folder `…/ACCOUNT_INVENTORY_JOINT/` **is** present in this branch's working tree and contains exactly two files — `00` and `01`. The two governing Boss controls are the files numbered `02` and `03`, and they are **not** there. A working-tree reader now finds a folder that looks complete and is missing exactly the two documents that matter | **D** | WATCH | PMO / Boss | Carry the two controls onto prompt branches, as `EVIDENCE-NOTE-02` recommended in the first instance. **Both were read at source at `d9e845e` and `296b495`** |
| `CF-EN-03` | **The commissioning condition.** The authorization's own header states it *"is not authorized until Boss commissions it"*. This session executed on Boss's instruction, which is decision 1 of the consolidation's Boss Decision List and rank 1 of its PMO recommendation. **The commissioning act is Boss's and is recorded, not asserted** | **D** | Disclosure | PMO | None |
| `CF-EN-04` | **Date-stamp disclosure.** The session identifier and the mandated branch carry `2026-09-05`; the **actual execution date is `2026-09-04`**. The identifier and branch are used exactly as mandated; the execution date is stated wherever a date is recorded | **D** | Disclosure | PMO | None. No conclusion depends on the difference |

---

## 4A. Challenge Items And Vetoes Raised By This Session

Raised by this session's own adversarial challenge at `12` §2 and §5.3. Listed here so the register is the single place an item can be found.

| ID | Item | Lane | Severity | Owner | Disposition |
|---|---|---|---|---|---|
| `CF-CH-01` | The row-17 anchor change rests on a naming equivalence this session cannot establish — is `MTI-D-03`'s *"Unit of Measure Category"* the matrix's *"Unit group and unit (`CN-14`)"*? | **D** | MATERIAL | Boss | Registered as `CF-D-01` with three readings. **`CD-14` and `CF-F-01` carry the qualifier everywhere they are stated** |
| `CF-CH-02` | `CF-I-05` supplies a remedy shape for a gap Boss has not been asked about | **D** then **A** | MATERIAL | Boss | `SPECIFIED — CONDITIONAL (CF-D-02)`, with withdrawal available as `CF-D-02` option (c) |
| `CF-CH-03` | The invariant set grew from 50 to 58 while `MTI-CH-02` already records it as un-minimised | **A** | WATCH | Inventory | **Disclosed, not remedied.** Minimisation is a later pass and is not in this authorization |
| `CF-V-01` | **VETO** on recording `HF-CTX-11`, the authorization attestation, or the authority half of element 10, as supplied, available, satisfied or suppliable | **D** | **IN FORCE** | AAS+ | The field references `CF-I-03`, **which does not exist**. Status is `specified, not built, not verified` and **no other wording may be substituted** |
| `CF-V-02` | **VETO** on citing `CF-I-06` as reducing `RC-F-03`, or `CF-I-08` as reducing `RC-F-07` | **D** | **IN FORCE** | AAS+ | One is a prohibition in an object's absence; the other is a labelling control. **`RC-P-20`, `-21`, `-45`, `-46`, `-48` remain `NOT DEFINABLE`** |

---

## 5. Dependencies This Session Inherits And Does Not Discharge

Nothing in this table is affected by the work in this package. Each is listed because the conformed set cannot be implemented or verified while it stands.

| ID | Dependency | Lane | Severity | Owner | What It Blocks Here |
|---|---|---|---|---|---|
| `RC-V-01` | Veto on implementation against the invariant set as published | D | **BLOCKING** | AAS+ / Boss | **Not discharged.** This package is the remedy's first half; an **independent check** is the second. `CF-F-02` additionally shows the condition is under-inclusive |
| `AAS-V-01` | Veto on recording element 10 as supplied | D | **IN FORCE** | AAS+ | Element 10 is `specified, not built, not verified` throughout this package and **no other wording is used** |
| `AAS-V-02` | Veto on implementation start before the three shape decisions are ruled — **CONDITION SATISFIED, NOT DISCHARGED** | D | **IN FORCE** | AAS+ / Boss | **Never reported as lifted.** Discharge is the issuing body's act |
| `AAS-V-03` | Veto on cross-company valuation content while the COGS Gap stands | D | **IN FORCE** | AAS+ | Binds themes 5, 6 and 13; `RC-P-22`, `XCR-02`, surface 10 of the rejection matrix |
| `RC-F-01` | `MTI-11` contradicts `MTI-D-01` | A | **BLOCKING for reliance** | Inventory | **Not closed.** The re-specification exists; the finding closes on implementation and independent verification |
| `RC-F-03` | The controlled mapping / provenance layer does not exist | A / D | **BLOCKING** for group reporting | Inventory + Boss | `RC-P-20`, `RC-P-21` `NOT DEFINABLE`; `CF-XCR-GAP-01`; `CF-D-03` option (a) unavailable |
| `RC-F-04` | `MTI-D-01` is not fully operable until `MTI-D-04` is ruled | D | MATERIAL | **Boss** | Gates Lane R3 |
| `RC-F-05` | The execution family carries no operation-type axis | A | MATERIAL | Inventory + SaaS Foundation | **Specification half supplied at `04`; the finding is not closed** |
| `RC-F-06` | The tenant-configurable enumeration is open-ended | D then A | MATERIAL | Boss / product scope | `RC-P-35`, `-36`, `-37` conditional; `CF-I-07` conditional; `L9-04` boundary half |
| `RC-F-07` | Private Company is a second topology with no invariants | D then A | MATERIAL, trending BLOCKING | Boss + Inventory | `RC-P-45`, `-46`, `-48`; **`CF-I-08` labels, it does not supply** |
| `RC-F-08` | Product Category is tenant-configurable and COGS-blocked at once | A / B | MATERIAL | Inventory + Joint | `CD-12`'s costing facet; `RC-P-39` `HELD` |
| `RC-F-09` | Payment has no published context obligation | A | WATCH | Inventory | **Discharged as a coverage item at `07` §4. Not closed** — `CF-D-04` |
| `RC-D-01` | Location axis disposition | D | Open | **Boss** | Five matrix rows unsettled. Design proceeds on the three ruled dimensions |
| `RC-D-02` | Closure of the configurable-record enumeration | D then A | Open | **Boss** | `CF-I-07` conditional |
| `RC-D-03` | Private Company escalation criteria; prohibitions 4 and 5 | D | Open | **Boss** | Root cause 3 at `10` §4 — **four requirements** |
| `RC-D-04` | Mapping-layer ownership and commissioning | D then A | Open | **Boss** | Root cause 2 at `10` §3 |
| `MTI-D-04` | Cross-company visibility policy | D | **BLOCKING for `RC-F-03`** | **Boss** | `XCR-02`, `RC-P-28`, Lane R3. **"No such grant exists" is a perfectly good ruling** |
| `MTI-D-05` | PDPA and tenant erasure scope | D then Legal | MATERIAL | Boss + Legal | `MTI-49` shape-only; `MTA-24` `BLOCKING`; `GAP-MD-29` **zero coverage anywhere** |
| `MTI-D-06` | Physical consolidation across companies | C then A | MATERIAL | **Thai panel** then Inventory | `MTI-13`, `MTA-20`. **No AI may answer it** |
| `RISK-U03` / `GAP-FS-10` | The multi-tenant invariant **capability** | A | **BLOCKING** | Inventory + SaaS Foundation | **Open. The item is the capability; this session produced a conformed specification** |
| `RISK-C02` / `IV-06` | Deterministic movement attempt identity — severity ruling `C-02` outstanding | A build / D severity | **BLOCKING** | **Boss** | `RC-P-25` partial, `RC-P-31` not exercisable; handoff element 15; `MTA-12`. **Severity not classified here** |
| `GAP-FS-08` / `CN-36` | Migration and replay provenance reference — **scope widened by `CD-09`** | A | **BLOCKING** | Migration + Inventory | Handoff element 14; `L10-04` R2's evidence obligation; `RC-P-48`; `CF-P-12`'s migration path |
| Privileged-bypass path audit | Started once, never completed | A | **BLOCKING for `L9-01`** | Inventory + SaaS Foundation | `RC-P-08` `NOT DEFINABLE`; `N-07` at `09`; the credibility of `MTI-17` |
| `GAP-MD-14` / `SAAS-04` | Regeneration, switch-off guards, versioning | A | MATERIAL | Boss / product | `MTI-37` conditional; `RC-P-42`, the highest-value configuration proof |
| `GAP-FS-02` | Product category costing facet split — precondition-blocked on `JT-01` | B | **BLOCKING** | Joint | `CD-12` costing facet **`HOLD`** |
| `GAP-FS-03` | Variant attribute change after stock exists | A | Open | Inventory | `CD-05`'s residual conditionality |
| `JT-01`, `JT-04`, `JT-05` | Valuation policy owner; COGS at delivery; return cost basis — **all three NOT DECIDABLE** | E | **BLOCKING** | Joint | Every valuation consequence in this package. **`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`** |
| `JT-02`, `JT-03`, `JT-06` .. `JT-12` | The remaining Joint decisions | E | **BLOCKING** | Joint | `0 of 12` ready. `JT-08` **Audit VETO retained**; `JT-10` complicated by `CD-11` |
| `GAP-FS-07` | Cross-company transfer path **never traced end to end** | B | **BLOCKING** | Joint / Inventory | `XCR-01` `INCOMPLETE` |
| `GAP-MD-09` | Consignment and ownership policy | B | MATERIAL | Joint | `MTI-16`, `HF-CTX-09`, `MTI-F-02` |
| `GAP-MD-29` | PDPA scope — **zero coverage anywhere** | D | MATERIAL, trending BLOCKING | Boss + Legal | `MTI-49`, `MTI-D-05` |
| `GAP-FS-11` / `GAP-MD-30` | Thai user validation — **`0 of 78`**, unremedied since 2026-08-30 | C | **BLOCKING for user-facing design** | **Boss to commission** | **Every label in this package is unvalidated**, including the platform operation-class names `CF-I-05` would introduce |
| `TH-HOLD-01` .. `TH-HOLD-09` | Thai statutory holds, including `TH-HOLD-06` branch-versus-warehouse | C statutory | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track | `MTI-07`; `CD-30`. **No statutory claim is made by this session** |
| `C-05` / `RISK-C05` | Clean-room containment — exposure confirmed live in a fresh clone | D | **BLOCKING for downstream reliance** | **Boss only** | **This package inherits the lock** |
| `RISK-CR-02` | Residual independent clean-room re-audit | D | Open | Boss | **Not further discharged.** No first-hand reference inspection; no quarantine access |
| `U-07` / `RISK-U07` | Two competing 9 Veto Council charters | D | **BLOCKING for challenge finality** | **Boss only** | **This session's `12` verdict inherits the conditionality for the fifth time** |
| `R4-F-01` .. `R4-F-25` | The 25 R4 findings — **0 closed** | A / B / C | Various | Inventory | `R4-F-12` and `R4-F-13` surfaces **grow** under `CD-13`, `CD-14`; `R4-F-11` untouched; `R4-F-16` stands in full |
| `MTI-F-01` .. `MTI-F-06` | The six invariant-set findings — **0 closed** | A | MATERIAL | Inventory | `MTI-F-03` widened again; `MTI-F-04` widened; `MTI-F-06`'s conserved quantity is four-part |
| `MTI-CH-01`, `-02`, `-03` | `STORE` satisfiability; set not minimised; three unrunnable scenarios | A | Open | Inventory / Team B | **`MTI-CH-02` is worse, not better** — the set grew from 50 to 58 |
| `REV-F-01` .. `REV-F-04` | Depth shortfall; element 14 conditionality; lane collision; roll-up not reconstructable | A / D | MATERIAL | Team A / PMO / Boss | All open. `REV-F-02` governs element 14 throughout this package |
| `C-01`, `C-02`, `C-04` / `N-CONC-01`, `N-A13-01` | Cancellation symmetry; idempotency severity; reservation locking; unread override path | A / D | CONFLICTING | Team A / Boss | **The two reachable leads were not read by this session either.** Out of a re-specification's scope, and that is a boundary, not an achievement |
| `SME-Q-02`, `SME-Q-03` | Routed business-SME questions | C | Open | Business SME | **No AI may answer either. Untouched** |
| `GAP-FS-19` | Manufacturing scope ruling | D | Open | Boss | `JT-09`; the Manufacturing obligation at `07` stays conditional |
| `EVIDENCE-NOTE-01`, `-02` | Invariant-set evidence notes | D | WATCH | PMO | `-02` reproduced as `CF-EN-02` |
| `RC-EVIDENCE-NOTE-01`, `-02` | Consolidation evidence notes | D | WATCH | PMO | `-01` was adopted by this authorization; the three AAS+ advice records were treated as mandatory |
| `L13-MT-01` .. `-03`, `L13-RC-01`, `-02` | Five inherited `L13+` levels | A / D | Open | Inventory + Boss | `L13-MT-01` is directly addressed in specification by `04` §7 and `CF-I-02`; **it is not closed** |

---

## 6. Roll-Up

| Measure | Result |
|---|---:|
| New findings raised | **6** — `CF-F-01` .. `CF-F-06` |
| New decision items raised | **4** — `CF-D-01` .. `CF-D-04` |
| New evidence notes raised | **4** — `CF-EN-01` .. `CF-EN-04` |
| New challenge items raised against this session's own work | **3** — `CF-CH-01` .. `CF-CH-03` |
| New vetoes issued | **2** — `CF-V-01`, `CF-V-02` |
| **Total new register items** | **19** |
| New items by lane | A 3 · A/D 1 · D 10 · D-then-A 4 · A-C-D 1 |
| New invariants specified | **8** — `CF-I-01` .. `CF-I-08` |
| New proof requirements specified | **12** — `CF-P-01` .. `CF-P-12` |
| New handoff context fields specified | **2** — `HF-CTX-10`, `HF-CTX-11` |
| New enforcement-point class specified | **1** — `EP-P` |
| New negative-test structural rules | **3** — `N-04`, `N-05`, `N-06`, `N-07` — **4** |
| Conformance deltas registered | **32** — `CD-01` .. `CD-32` |
| `L13+` levels opened | **2** — `L13-CF-01`, `L13-CF-02` |
| Prior items closed | **0** |
| Inherited dependencies discharged | **0** |
| Vetoes issued | **2** |
| Vetoes discharged | **0** |
| Vetoes in force after this session | **6** — `AAS-V-01`, `AAS-V-02`, `AAS-V-03`, `RC-V-01`, `CF-V-01`, `CF-V-02` |
| Carried identifiers renumbered, retired or merged | **0** |
| Proofs achieved | **0 of 8** |
| Cross-proof scenarios verified | **0 of 22** |
| Handoffs contract-compliant | **0 of 10** |
| Joint decisions ready | **0 of 12** |
| Thai validations | **0 of 78** |
| Proof requirements executable | **0 of 60** |
| Enforcement surfaces verified | **0 of 13** |
| Negative cases executed | **0 of 60** |

The `N-04` .. `N-07` row is stated as **4** because four rules were added; the enumeration in the same cell lists them.

**No open-item roll-up total is asserted by this session.** `REV-F-04` records that the 92 figure is not independently reconstructable and that no open-item crosswalk exists. The invariant-set session and the consolidation both declined to assert a total on those grounds; this session declines on the same grounds. **Adding fourteen items to a total that cannot be reconstructed would produce a number that looks precise and is not.** The fourteen new items are enumerated exactly above; the roll-up awaits the crosswalk PMO has been asked to publish.

---

## 7. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
