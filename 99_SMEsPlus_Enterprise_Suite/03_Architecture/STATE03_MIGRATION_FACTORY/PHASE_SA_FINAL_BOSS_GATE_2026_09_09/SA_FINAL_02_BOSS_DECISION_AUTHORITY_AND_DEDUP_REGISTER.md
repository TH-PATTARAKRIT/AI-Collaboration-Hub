# SA_FINAL_02 — BOSS-DECISION AUTHORITY AND DE-DUPLICATION REGISTER

## CP-SA-FG-20 — BOSS DECISION LIST AUTHORITY-CLEAN

Session: `[SMEPLUS-26-09-09-PHASE-SA-FINAL-BOSS-GATE-001]`
Branch: `architecture/phase-sa-final-boss-gate-readiness-2026-09-09-001`
Boss: **SOLE FINAL APPROVER**

---

## 1. The rule this register applies

Master prompt §0:

> **NO ITEM MAY REACH BOSS AS A DECISION IF EXISTING BOSS RULINGS, SMEs CORE AUTHORITY, PMO AUTHORITY,
> DOCUMENT-OWNER AUTHORITY OR EXISTING EVIDENCE CAN RESOLVE IT.**

Six tests, applied in order, to **every atomic candidate** — not to CORR5's fifteen presentation rows.
A row that bundles six decisions is six candidates.

---

## 2. The population, declared

CORR5 `SA_CORR5_14` §2.3 presents **15 rows**. Decomposed to atomic decisions:

| CORR5 row | Atomic candidates |
|---|---:|
| B1 `JT-04` · B2 `JT-05` · B3 `XD1-P1` · B4 tolerance default · B7 `XMC-D-02` · B8 `C-02` · B9 `MTI-D-04` · B12 `C2-D-01` · B15 wallet character | 1 each = **9** |
| B5 `B-6` | `BLK-07` restatement · `BLK-08` restatement · veto limb 2 restatement · `POH-D-01` · `POH-D-02` · `POH-D-06` = **6** |
| B6 | `XMC-D-01` · `C2-D-02` = **2** |
| B10 | `RC-D-01` · `RC-D-02` · `RC-D-03` · `RC-D-04` · `CF-D-01` · `CF-D-02` = **6** |
| B11 | `TV6-BOSS-01` · `TV6-BOSS-02` = **2** |
| B13 | `POH-D-03` · `POH-D-04` · `POH-D-05` = **3** |
| B14 | `B-7` appointment · `C4-D-01` · `C4-D-02` · `AAS-V-02` discharge · Thai panel commissioning = **5** |
| **Total candidates** | **33** |

**Instrument for Test A.** Every candidate identifier was searched across all **188** branch heads, and
every hit falling in a file whose name or status marks it a Boss act (`*BOSS_RULING*`, `*BOSS_DECISION*`
where the status line reads `BOSS RULED` / `BOSS APPROVED`, `*BOSS_APPROVAL*`, `*BOSS_DIRECTION*`, the
`ruling/*` branches, `01_BOSS_APPROVED_ARCHITECTURE_RULINGS.md`, `04_PHASE_S_CONDITIONAL_CLOSURE…`)
was read. **Controls:** the ruling branches are exactly three — `inventory-mti-d01…`,
`-d02…`, `-d03…` — and `MTI-D-02`'s ruling text is read verbatim, so the instrument reaches Boss rulings.

> **`FG-F-02` — the instrument's first result was a false positive class, and it is worth recording.**
> Seven candidates return hits in files named `14_BOSS_DECISION_PACKAGE.md` and `P11_BOSS_DECISION_
> MATRIX_CORR1.md`. **Those are escalation packages — documents that *ask* Boss — not Boss acts.** A
> name-based instrument cannot tell "decision package" from "decision". **Every hit was resolved by
> reading the file's own status field**, which is the programme's *peer status-field rule* applied to
> its own file-naming convention. **Test A's true result is: 0 of 33 candidates has been ruled.**

---

## 3. Test results, candidate by candidate

`A` already ruled · `B` SMEs Core authority · `C` PMO/governance authority · `D` evidence acquisition
only · `E` runtime/Pre-Test proof only · `F` genuine Boss authority.

| # | Candidate | A | B | C | D | E | **Verdict** | Ground (primary text) |
|---:|---|:-:|:-:|:-:|:-:|:-:|---|---|
| 1 | **`JT-04`** COGS recognition timing | ✗ | ✗ | ✗ | **partial** | ✗ | **`F` KEEP** | `08_JT04` §5: *"Final event selection → **Boss**, informed by the above but not derivable from them alone."* §3 classes it a `DESIGN DECISION` with a `BUSINESS POLICY` input. `11_COGS_RECOGNITION_OPTIONS_ANALYSIS` summary table: **all five models "Requires Business/Boss decision: Yes"**. Test B fails because the governing input `SME-Q-03` — *SMEsPlus's own invoice/delivery sequencing pattern* — is a **business** fact no architecture act can supply; §8 records that the session rejected `DECIDABLE WITH CONTROL` precisely because adopting one "would be designing blind". Test D is *partial*: two inputs (`SME-Q-03`, `TH-NEW-01`) are acquisitions, but the election survives them |
| 2 | **`JT-05`** return cost basis | ✗ | ✗ | ✗ | partial | ✗ | **`F` KEEP** | `09_JT05` §5: *"Final return-cost-basis rule (and the reconciliation-control design for the AVCO admitted gap) → **Boss**"* |
| 3 | **`XD1-P1`** cancellation-gate severity default | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` KEEP** | `SA_CORR3_01` §14.3: trigger, data contract, durability, failure behaviour, audit and scoping **all determined**; *"exactly two [alternatives], both architecturally sound"*. `SA_CORR3_12` `B-1`: **Group A's owning session reserved this election to Boss in writing and the reservation is undischarged** — a reservation SMEs Core does not hold and may not discharge |
| 4 | **Over-receipt tolerance default** | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` KEEP** | Same shape as #3, established by CORR5's own challenge (`CHC-13`): *"what does a commercial control default to when the business has not said?"* — a risk-appetite election. **Originated by CORR5 and routed, never decided** |
| 5 | **`TV6-BOSS-01`** confirmation-gate policy default | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` KEEP** | `SA_CORR3_13`: *"`APR-003`'s explicitly deferred item and Fit-Gap candidate #14. It is not new. It has been open since the Group A design round and has been re-reported as 'undefined' three times since"* |
| 6 | **`TV6-BOSS-02`** base sell-price scope | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` KEEP** | `SA_CORR3_12` `B-3`: the one commercial quantity in its set that is not company-scoped, while its cost, revenue account, credit limit, tax convention and rounding all are |
| 7 | **`XMC-D-01`** dropship: two valuation facts or none | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` KEEP, with a standing dissent** | `SA_CORR3_12` `B-4`: *"Both readings are consistent with every fact in the corpus"*; carried **with a dissent — "a second executor's buy-side evidence suggests the answer may be available without a decision"**. **The dissent is not resolved by this session and is presented to Boss as CORR3 required** |
| 8 | **`C2-D-02`** where dropship cost lands, and the identity binding it to the sale | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` KEEP** | `SA_CORR2_02` §6: *"SMEs Core → Boss. Both reference generations are `FACT VERIFIED` and they disagree. Choosing between them is a determination"* |
| 9 | **`XMC-D-02`** does the 16-element contract extend beyond Inventory → Accounting | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` KEEP** | `SA_CORR3_12` `B-5`: scope *"unambiguous at primary text — one boundary, one direction"*; **11 of 12 mandated handoffs have no element contract**. *"Nothing to research; something to decide"* |
| 10 | **`C2-D-01`** shortage: does it raise supply, and is the fulfiller hard- or soft-bound | ✗ | **partial** | ✗ | ✗ | ✗ | **`F` KEEP — NARROWED** | `SA_CORR2_02` §6: *"SMEs Core design position → **Boss confirm**"*. **The design position exists** — `SA_CORR2_03` §3.1: the target fact-ownership matrix binds the fulfiller **softly** (*"Hard trigger, soft binding — Inventory does not know who will respond"*), `BN-04` re-graded **`PARTIAL`**, ownership `FACT VERIFIED`. **So Boss is confirming a stated position, not choosing in a vacuum** — the question is narrowed accordingly at `SA_FINAL_03` |
| 11 | **`C-02`** is idempotency gate-blocking | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` KEEP** | Owner *"Boss directly"* (R4 `07_L6` line 210; line 222 *"R4 does not decide it"*); R1 `03` §7.2; R2 `04` §7.2 (*"consistent with R4, the review, the invariant set and the consolidation all declining"*); `GAP-FS-06`; **and the SMEsPlus-owned functional design itself** — `03_INVENTORY_FUNCTIONAL_DESIGN_V1` line 132: *"Carried finding `C-02`: whether this is gate-blocking is Boss's decision."* **Five independent instruments.** CORR5's first freeze declared it dissolved and its own challenge reversed that |
| 12 | **`MTI-D-04`** cross-company visibility policy | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` KEEP** | R1 `11`: *"A real Thai SME group need, and a deliberate hole in an isolation boundary. **Only Boss may authorise a door**"* |
| 13–16 | **`RC-D-01`** location as an authorization axis · **`RC-D-02`** configurable-record enumeration closure · **`CF-D-01`** UoM-category scope · **`CF-D-02`** operation-class enumeration | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` KEEP** | R1/R2 open-items registers. `CF-D-01`'s ground is decisive and general: ***"only Boss may state what a Boss ruling covers"*** — a scope clarification of `MTI-D-03` |
| 17–18 | **`RC-D-03`** Private Company escalation criteria · **`RC-D-04`** mapping-layer ownership | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` KEEP** | R2 `11`; `RC-D-04` is gated on `MTI-D-04` and is a commissioning-plus-policy act |
| 19–21 | **`BLK-07` restatement** · **`BLK-08` restatement** · **veto limb 2 restatement** | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` KEEP** | `SA_CORR3_03` `POH-D-06`: *"**Governance act.** A Boss-owned blocker can only be retired, restated or confirmed by Boss… This document requests a restatement; it does not perform one."* And `POH-F-12`: as currently worded Boss is being asked to choose between an option and **an option his own register already rejected by name** |
| 22 | **`POH-D-01`** confirm the declared departure from `BD-04` | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` KEEP** | *"It **modifies a standing Boss decision.** Only Boss may amend one, however statutory the reason"* |
| 23 | **`POH-D-02`** depreciation-method election | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` KEEP** | *"changes the charge itself, is an accounting-policy election, has **unresearched tax consequences**, and requires a per-asset expected-output estimate the business does not maintain"* |
| 24–26 | **`POH-D-03`** is SETUP time productive · **`POH-D-04`** are IDLE and NO_DEMAND one cause or two · **`POH-D-05`** who owns the normal-capacity figure and its review cadence | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` KEEP (minor)** | `SA_CORR3_03` §9 — business-meaning policy, management-reporting policy, control-ownership policy |
| 27 | **`B-7`** appoint a `Q-BOSS-02`-eligible challenger for Phase SA | ✗ | ✗ | ✗ | ✗ | ✗ | **`F` — but an ACT, not a decision** | `Q-BOSS-02` control 2 **forbids a session selecting its own challenger**. It has no alternatives, no dissent and no scenario effect: it fails the §4 decision-card form. **Moved to the Acts list** |
| 28 | **`C4-D-01`** commission the joint interface artefact; dispose of the 20 stranded deliverables | ✗ | ✗ | **partial** | ✗ | ✗ | **ACT** | An appointment plus a merge-or-archive act. The *disposition* is PMO's; only the **commissioning** is Boss's. **Moved to the Acts list** |
| 29 | **`C4-D-02`** the platform-actor review (`G2`: R1 separate identity domain vs R2 scoped role) | ✗ | ✗ | ✗ | ✗ | ✗ | **ACT** | CORR4 re-scoped it *"from a design act to a governance act plus an independent review"*; CORR5 left both models standing with a recommendation. Boss appoints the review; the review decides. **Moved to the Acts list** |
| 30 | **`AAS-V-02`** discharge | ✗ | ✗ | ✗ | ✗ | ✗ | **ACT** | Its stated condition (three rulings) **is satisfied**; R2 records *"CONDITION SATISFIED — NOT DISCHARGED … never reported as lifted"*. Discharge is the **issuer's** act ratified by Boss — a ratification, not an election. **Moved to the Acts list** |
| 31 | **Thai user panel commissioning** | ✗ | ✗ | ✗ | ✗ | ✗ | **ACT** | `18_THAI_USER_VALIDATION_CHECKLIST` line 11: **"Boss to commission"**. No alternatives; it is a resourcing act |
| 32 | **`POH-D-06`** *(counted at 21 as the veto-limb-2/blocker restatement)* | — | — | — | — | — | **merged into 19–21** | `POH-D-06` *is* the restatement request; listing it twice would duplicate |
| 33 | **Prepaid-wallet balance-sheet character and tax treatment** | ✗ | ✗ | **YES** | ✗ | ✗ | **REMOVE — `C`** | §5 |

---

## 4. Removals

### 4.1 `REMOVE — PMO/GOVERNANCE OWNED · another Boss-authorized session now owns it`

**Prepaid-wallet balance-sheet character and tax treatment.** CORR5 carried this as `B15` because
`SAAS_CELL/27` lists it as an open item requiring *"accounting/tax review, and Boss Final Approval"*.

**Delta this session (`SA_FINAL_01` §4.1):** `ERPPLUS-152` — *SMEsPlus Core Resource Governance &
Package Capacity Architecture* — landed on mainline at `784f60a2` as a **Boss-authorized architecture
session** whose scope contains **`WS-09` Prepaid Wallet & Capacity Authorization**, gate **`G6` Metering
/ Wallet Gate**, deliverable **`10_USAGE_LEDGER_METERING_AND_PREPAID_AUTHORIZATION_MODEL.md`**, and its
own **`G11` Boss Final Decision Gate** whose instruction is *"Stop and present Boss with only decisions
that genuinely require Boss judgment."*

> **The question has an owner, a workstream, a deliverable and a Boss gate — all outside Phase SA.
> Presenting it again in the Phase SA pack would be exactly the duplication this register exists to
> remove.** It changes no Phase SA dimension cell (CORR5 marked it `HOLD` and the `G5` handoff shape is
> specified without it), so Phase SA carries it as a **cross-session dependency**, not a decision.
>
> **Stated for the receiving session, not applied here:** `SA_CORR5_04` BP-1's handoff row and
> `SA_CORR5_02` class 13 record the platform-side handoff shape under `BD-ACC-01` and leave the
> character `HOLD`. `ERPPLUS-152`'s stop condition *"any proposal that changes previously approved
> business/accounting semantics"* should be read against them.

### 4.2 `REMOVE FROM THE DECISION LIST — these are ACTS, not decisions`

`B-7` · `C4-D-01` · `C4-D-02` · `AAS-V-02` discharge · Thai panel commissioning. **Five.**

None has alternatives, a dissent, an SMEs Core recommendation between options, or a scenario-level
effect that changes with the answer — the six form-elements master prompt §4 requires of a genuine Boss
item. Each is a **single authorised act with one correct form**. They are presented at `SA_FINAL_03` §4
as an **Acts list**, so that Boss is not asked to *decide* what he is being asked to *do*.

### 4.3 Nothing was removed under Tests A, B, D or E — and that is a result

| Test | Candidates removed | Why none |
|---|---:|---|
| **A** already ruled | **0** | Three ruling branches exist and none touches a candidate; every apparent hit was a *decision package*, not a decision (`FG-F-02`) |
| **B** SMEs Core authority | **0** | Two candidates were *narrowed* by existing SMEs Core positions (`C2-D-01`'s soft binding; `JT-04`'s `ND-10`) but neither is thereby resolved: one is an explicit "Boss confirm", the other an explicit "not derivable" |
| **D** evidence acquisition only | **0** | `JT-04` and `JT-05` each have named evidence inputs, and both source files state the election survives them |
| **E** runtime / Pre-Test proof only | **0** | Every candidate's semantic is unsettled *by election*, not by absence of a build |

> **`FG-F-03`. The CORR5 Boss list was already authority-clean on its merits; what it was not was
> *structurally* clean.** Of 33 candidates, **0 were wrongly escalated on authority** and **6 were
> wrongly *shaped*** — one owned by a newer session, five that are acts rather than decisions. **The
> de-duplication this round achieves is structural and by consolidation (`SA_FINAL_03`), not by
> discovering that SMEs Core should have decided something.** Recorded because the opposite result —
> "we removed twelve items Boss never needed to see" — would have been the more flattering one, and it
> is not what the evidence supports.

---

## 5. Result

| | Count |
|---|---:|
| Atomic candidates tested | **33** |
| Removed — owned by another Boss-authorized session | **1** |
| Removed from the decision list — acts, not decisions | **5** |
| **Surviving genuine Boss decisions** | **27** |
| Consolidated into families (`SA_FINAL_03`) | **8** |
| New Boss decisions originated by this session | **0** |
| Boss decisions **removed** because SMEs Core / PMO / evidence can resolve them | **0** — and §4.3 says why |

## 6. Checkpoint

> ## `CP-SA-FG-20 — BOSS DECISION LIST AUTHORITY-CLEAN`
> **33 candidates · 6 tests each · 27 survive · 1 removed to `ERPPLUS-152` · 5 re-shaped as acts ·
> 0 already ruled · 0 new · 2 findings (`FG-F-02`, `FG-F-03`).**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
