# [SMEPLUS-26-09-04-INV-MTI-RULING-CONSOLIDATION-001]
# 10 — Next Controlled Remediation Lane Split

Control Level: `/L9999.9999`
Status: `LANE SPLIT PUBLISHED — RECOMMENDATION ONLY — NO LANE AUTHORIZED BY THIS SESSION`

---

## 1. What This File Decides, And What It Does Not

It **separates** the remaining work into lanes that can proceed independently, states what each lane may and may not do, and identifies which lane should execute next.

It **authorizes nothing.** PMO recommends; Boss decides. No lane below begins without Boss commissioning it.

---

## 2. The Separation Rule Applied

The authorization at §9.6 requires identifying what can proceed **without** Accounting COGS evidence and what cannot. Two orthogonal separations are applied:

| Separation | Question |
|---|---|
| **COGS dependence** | Does the work require a valuation, COGS, landed-cost posting, period-close, return-cost-basis or cross-company valuation conclusion? |
| **Ruling dependence** | Does the work require a Boss decision that has not been taken? |

Work that is **neither COGS-dependent nor ruling-dependent** is available now. That is the definition of Lane R1, and it is the only lane that meets it.

---

## 3. The Seven Lanes

### Lane R1 — Ruling-Conformance Re-Specification · **Lane A** · **AVAILABLE NOW**

**Needs no Boss ruling. Needs no COGS evidence. Needs no Thai input. Needs no upstream package.**

| Aspect | Content |
|---|---|
| **Scope** | Bring the published multi-tenant design into conformance with `MTI-D-01`, `MTI-D-02` and `MTI-D-03`, and specify the two capabilities the rulings create |
| **Contents** | `RC-F-01` re-specify `MTI-11`, `XCR-03`, `04` §4.1 and matrix rows 5-7 to a company anchor · `RC-F-02` correct the `XCR` register to three entries · `RC-F-05` state the `CTX`-to-`AUTH` relationship and the operation-type axis on deferred execution · `RC-F-09` state Payment's context obligation or record why it has none · adopt the 48 proof requirements at `07` and `08` as the acceptance criteria of the invariant set |
| **May do** | Design and specification only. Revise documents. State propositions and acceptance criteria |
| **May not do** | Build. Implement. Declare any proof. Record element 10 as supplied (`AAS-V-01`). Re-litigate a ruling. Close a finding |
| **Unblocks** | Removes the independent bar on implementation start created by `RC-F-01`. Makes `L9-02` and `L9-03` proof definitions final rather than provisional. Makes the 48 requirements attachable to a conforming design |
| **If deferred** | **The canonical invariant set stays in contradiction with its governing ruling.** Anything built against it would violate `MTI-D-01`, and every downstream package inherits a document known to be non-conforming |

### Lane R2 — Privileged-Bypass Path Audit · **Lane A** · **AVAILABLE NOW**

Unchanged from rank 2 of the invariant-set PMO recommendation. **The rulings do not touch it.**

| Aspect | Content |
|---|---|
| **Scope** | Enumerate the complete set of privileged, system, background, administrative and migration code paths, and certify the enumeration complete |
| **May not do** | Substitute per-path results for a completeness result |
| **Unblocks** | `L9-01`'s completeness claim · `MTP-03` · the `EP-W` coverage assertion · **`RC-P-08`**, which is `NOT DEFINABLE` without it · the credibility of `MTI-17`, the invariant the whole set rests on |
| **If deferred** | `L9-01` can produce per-path results and never a completeness result, and the isolation claim stays permanently qualified — **including under the new rulings, which do not help it** |

### Lane R3 — Controlled Mapping / Provenance Layer Specification · **Lane A, gated on Lane R4** · **NOT AVAILABLE**

| Aspect | Content |
|---|---|
| **Scope** | Specify the object `D-01` rules 5 and 8 require. Ten required properties enumerated at `06` §5.3 |
| **Gating** | **`MTI-D-04` must be ruled first.** `RC-F-04` — properties M-04, M-08 and M-09 are the properties of `XCR-02`, whose existence is `MTI-D-04`'s subject. Specifying a mapping layer before knowing whether a sanctioned cross-company read exists would design the mechanism before the authorization |
| **Unblocks** | `RC-P-20`, `RC-P-21` — currently the only two requirements in the package that cannot be stated as propositions at all |
| **If deferred** | The group-view need is met by export. `MTA-09` names that the worst available outcome, and **Option B makes the need larger**, because a Thai SME group now maintains several catalogues instead of one |

### Lane R4 — Boss Rulings And Governance · **Lane D** · **BOSS ONLY**

The cheapest high-value actions on the list, because they are decisions rather than investigations.

| # | Ruling | Unblocks |
|---:|---|---|
| 1 | **`MTI-D-04`** — whether a sanctioned cross-company read exists | Lane R3 · `XCR-02` · `RC-P-28` export · `RC-F-03` and `RC-F-04`. **Ruling "no" is a perfectly good ruling; leaving it unruled is not** |
| 2 | **`RC-D-03`** — Private Company escalation criteria, and the disposition of pool prohibitions 4 and 5 | `RC-F-07` · `RC-P-45`, `-46`, `-48` · **4 of 7 live requirement classes currently unclassifiable** |
| 3 | **`C-02` severity**, then commission the movement attempt identity | Handoff element 15 · **scenario 22, a Boss-approved mandatory scenario** · `RC-P-25`, `RC-P-31` · six enforcement points |
| 4 | **`C-05` containment** — options (a), (b), (c) | **Downstream reliance on all Inventory evidence, this package included.** Exposure confirmed live in a fresh clone |
| 5 | **`U-07`** — which Council charter governs | R4's L12 challenge, the review's verdict, and **this session's `11` verdict**, all currently conditional |
| 6 | **`RC-D-02`** — closure of the configurable-record enumeration | `RC-F-06` · `L9-04` boundary half · `RC-P-35`, `-36`, `-37` |
| 7 | **`RC-D-01`** — location axis disposition | Five matrix rows. **Lowest urgency of the seven**: design proceeds correctly on the three axes ruled |
| 8 | **`MTI-D-05`** and route PDPA scope to Legal | `GAP-MD-29`, **zero coverage anywhere** · `MTI-49` · `MTA-24` |
| 9 | **`GAP-FS-19`** Manufacturing scope | `JT-09` · one whole proof scenario |
| 10 | **`RC-D-04`** — mapping-layer ownership and commissioning | Follows ruling 1 |
| 11 | **Register hygiene** — ratify one lane vocabulary (`REV-F-03`); publish the open-item crosswalk (`REV-F-04`) | Every cross-document lane and count reference. **Three documents now use the authorization's vocabulary and R4's registers use another** |

### Lane R5 — Business SME / Thai Validation · **Lane C** · **AVAILABLE NOW, AS AN APPOINTMENT**

**Filling the panel membership remains the precondition and has never been done.** Routing is not answering, and **no AI may answer any item in this lane.**

| Aspect | Content |
|---|---|
| **Scope** | Fill the panel; route `SME-Q-02`, `SME-Q-03`, `MTI-D-06` and the `MTI-F-05` compensating control; execute the 78-item checklist |
| **Widened by the rulings** | Every one of the eleven record-class names in `D-03` §3 and every operation type in `D-02` §5 is a **further unvalidated label**. The checklist is larger than 78 now, not smaller |
| **Unblocks** | `L9-07`, `L9-08` · `RC-P-16` segregation degradation · `R4-F-19` · every user-facing conclusion across five rounds |
| **If deferred** | **Plausible reasoning continues hardening into accepted fact by citation.** Unremedied since 2026-08-30 |

### Lane R6 — Accounting COGS · **Lane B** · **HOLD, NOTHING PROCEEDS**

| Aspect | Content |
|---|---|
| **Status** | `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`. **10 of 10 dependency areas locked**, independently confirmed by the R4 review |
| **What the rulings changed** | **Nothing.** No ruling touches valuation, and none was expected to |
| **What must not be done** | Re-commissioning the COGS Deep Research. It has been executed — **verified, 37 deliverables at `a959327`** — and its own named missing inputs are business-SME input, Thai statutory confirmation and live reference-instance access. **No further research pass supplies any of them** |
| **What is available** | The **seven Inventory-owned obligations** need no Joint decision and no COGS evidence. See Lane R7 |

### Lane R7 — Inventory-Owned Non-Blocked Work · **Lane A** · **AVAILABLE NOW**

Unchanged, and still the work that is available today. Items 1 and 2 remain the highest-leverage.

| # | Obligation | Note |
|---:|---|---|
| 1 | Classification on every non-sale stock reduction | **Highest-value item in the programme.** Stops a periodic cost-of-sales computation from silently mislabelling scrap, shrinkage, write-down and adjustment as cost of sales. **Inventory is the only domain that can supply it** |
| 2 | Reversal-to-original linkage on every correction | |
| 3 | Physical event date and entry date carried as two distinct values | |
| 4 | Landed cost allocation statement inspectable **before** validation | |
| 5 | Quantity-side cutover reconciliation, certifiable independently of value — **now naturally per company under `D-01`** | `R4-F-25`, the one finding that creates work rather than blocking it |
| 6 | Independent check that internal-to-internal movements net to zero value effect | `R4-F-18` |
| 7 | Movement history with an explicitly stated ordering rule | `R4-F-08` |
| — | Plus the disclosure obligation: any reconciliation output must **state which posture it measures against** | An unqualified claim that the two balances always match is unsupported by any evidence in this programme |

---

## 4. Lane Availability Summary

| Lane | Needs A Ruling? | Needs COGS? | Needs Thai Input? | Available Now |
|---|:---:|:---:|:---:|:---:|
| **R1** Ruling-conformance re-specification | **No** | **No** | **No** | **YES** |
| **R2** Privileged-bypass path audit | **No** | **No** | **No** | **YES** |
| **R3** Mapping / provenance layer | **Yes** — `MTI-D-04` | No | No | No |
| **R4** Boss rulings and governance | Is the ruling | No | No | **Boss only** |
| **R5** Thai validation | No — an appointment | No | Is the input | **YES, as an appointment** |
| **R6** Accounting COGS | — | Is the gap | Partly | **No** |
| **R7** Inventory-owned non-blocked | **No** | **No** | **No** | **YES** |

**Four lanes are available today. Only one of them — R1 — is created by the rulings, and it is the one that should execute next.**

---

## 5. Why R1 Executes Next

| Criterion | R1 | R2 | R5 | R7 |
|---|---|---|---|---|
| Needs nothing from Boss | Yes | Yes | Yes | Yes |
| Removes a **live contradiction** between a governing ruling and a canonical document | **Yes** | No | No | No |
| Blocks every other Inventory design act until done | **Yes** — anything built on file `03` would violate `MTI-D-01` | No | No | No |
| Consumes the rulings Boss has just taken | **Yes** | No | No | No |
| Can be executed as a bounded, single-session pass | **Yes** | Requires access | Requires appointments | Yes |

**R1 is the only lane whose deferral leaves a known non-conformance standing in the canonical evidence chain.** R2, R5 and R7 should be commissioned in parallel — they have different owners, different gating and different reach, and PMO recommends against bundling them, which was the error the R4 review corrected at `04` §4.

---

## 6. What No Lane May Do

| Prohibited | Applies To |
|---|---|
| Start development, write application code, or freeze a schema | Every lane |
| Merge to the canonical branch | Every lane |
| Declare `PASS`, `APPROVED`, `CLOSED`, or Final Solution accepted | Every lane |
| Record element 10 as supplied | Every lane — `AAS-V-01` |
| Record a specification as a proof | Every lane |
| Close a COGS-dependent item without Accounting COGS evidence | Every lane |
| Carry valuation content across a company boundary | Every lane — `AAS-V-03` |
| Re-litigate `MTI-D-01`, `-D-02` or `-D-03` | Every lane |
| Treat product duplication across companies as a defect | Every lane |
| Treat Private Company as approved | Every lane |
| Rely on `C-05`-affected material | **Every lane, until Boss rules** |

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
