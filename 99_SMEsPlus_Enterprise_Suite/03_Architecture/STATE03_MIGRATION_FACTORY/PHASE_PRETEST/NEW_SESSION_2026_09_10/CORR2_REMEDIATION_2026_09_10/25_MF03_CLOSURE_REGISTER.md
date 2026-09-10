# 25 — `MF-03` CLOSURE REGISTER

# `STILL NOT DECIDABLE · THE MISSING SEMANTIC IS NAMED · OWNER: SMEs CORE`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Authority: `§15` of the ruling prompt — *"Do not force a classification"* · Boss: **SOLE FINAL APPROVER**

> **`§15` requires all `13` recorded properties compared, and — if still undecidable — the **EXACT**
> missing semantic and the owner required to close it. Both are delivered.**
> **`MF-03` cannot be treated Research-Complete while undecidable, and it is not.**

---

## 1. EVIDENCE BASE — re-established, with the path-set error corrected

| Question | Answer |
|---|---|
| Defining register on the frozen baseline? | **NO** — `10_INVENTORY_CROSS_MODULE_HANDOFF_V1.md` is not on the `c91d5840` tree |
| Where? | **`2` branches** — `origin/design/inventory-final-solution-v1-2026-09-02-001` and `-v2-…` |
| Do they differ? | **NO — byte-identical**, `sha256 233f5692…` |
| Does `V2_0` redefine `HX-24`/`HX-25`? | **NO** — `12` artefacts, **`0`** carrying `HX-25` |
| Is the payload nevertheless **on** the baseline? | **YES** — `05_` L49 and `17_` L70 transcribe it faithfully. **The falsification below needs no off-baseline evidence** |

**Path-set note carried from `26_` §2:** `07_` declared its path set as the frozen tree and was correct
here. **The narrower error affecting `IR`/`AR` (`08_` rows `9`–`12`) did not affect this analysis**, and
is corrected separately.

---

## 2. THE PRIMARY ROWS

```
| ID    | From -> To                       | Fact handed over                                | Trigger | Receiver's obligation                                              | Menus        | Class                        |
| HX-23 | Migration -> Inventory           | Master data with a provenance reference         | Cutover | Validate, load, reconcile counts                                   | PR-*, CF-*   | INV-OWNED (GAP-FS-08)        |
| HX-24 | Migration -> Inventory/Accounting| Certified opening balances, quantity and value  | Cutover | Human certification; cross-proof vs the opening trial balance      | OP-02, RP-05 | JOINT (JT-11, G-5)           |
| HX-25 | Migration -> Inventory           | Movement history, or opening plus history       | Cutover | Replay with a stable identity; reconcile                           | RP-03, RP-04 | INV-OWNED -- depends on C-02 |

ELEMENTS (SA_CORR3_08 L176-177)
| 14 | WHICH Migration / Replay Batch | ABSENT -- "the provenance reference does not exist yet" |
| 15 | WHICH Idempotency Identity     | ABSENT -- see XMC-F-11                                 |
```

---

## 3. ALL `13` PROPERTIES — `§15`'s full list

| # | Property | `MF-01` / `HX-24` | `MF-03` / `HX-25` | |
|---:|---|---|---|:-:|
| `1` | **Payload** | certified opening balances, **quantity and value** | **movement history**, or opening plus history from the cutover date | **DIFFER** |
| `2` | **Identity** | none stated by the row | **requires a stable identity — element `15`, `ABSENT`** | **DIFFER** |
| `3` | **Trigger** | Cutover | Cutover | **SAME** |
| `4` | **Guarantee** | human certification; cross-proof against the **opening trial balance** | **replay with a stable identity**; reconcile | **DIFFER** |
| `5` | **Owner** | **`JOINT` (`JT-11`, `G-5`)** | **`INV-OWNED`** — depends on `C-02` | **DIFFER** |
| `6` | **Control** | `OP-02`, `RP-05` | `RP-03`, `RP-04` | **DIFFER — disjoint** |
| `7` | **State transition** | creates an opening position where none existed | re-applies history from the cutover date | **DIFFER** |
| `8` | **Quantity** | quantity enters **without a movement** | **zero iff replay is idempotent** — element `15`, `ABSENT` | **UNDECIDABLE** |
| `9` | **Value** | value enters **without a purchase** | **zero iff replay is idempotent** — same dependency | **UNDECIDABLE** |
| `10` | **Accounting** | **dual-target** — Inventory **and** Accounting | **single-target** — Inventory | **DIFFER** |
| `11` | **Inventory** | establishes the opening position | applies subsequent history to it | **DIFFER** |
| `12` | **Replay behaviour** | none — a cutover load, not a replay | **the row's defining obligation** | **DIFFER** |
| `13` | **Failure behaviour** | certification fails → the load is rejected before it stands | **NOT SPECIFIED.** *"A re-run can **duplicate an opening balance**"* (`CORR1-F-03`) | **UNDECIDABLE** |

```
DIFFER 9   SAME 1   UNDECIDABLE 3
06_ tested 1 -- property 3, the only one that returns "same"
```

---

## 4. THE CITED GROUND — falsified, and the falsification re-verified

`06_` §2.2: *"`MF-03` = `EXECUTION MODE` … established on **`HX-25`** and **element `14`**, **not** on
`RT-E15-05`. … **the ground is now evidence rather than an unbuilt control**."*

| # | Falsification | Verified at |
|---:|---|---|
| `1` | **`HX-25` does not describe replay as re-running a migration package.** Its payload is *"movement history, or opening plus history from the cutover date"* — **a payload, not a manner of performing another flow**, and a **different** payload from `HX-24`'s | primary register; **and `05_` L49 on the baseline** |
| `2` | **Element `14` is `ABSENT`** (*"WHICH Migration / Replay Batch"* — *"does not exist yet"*) **and belongs to `HX-23`**, whose payload is *"master data with **a provenance reference**"* | `SA_CORR3_08` L176; primary rows |
| `3` | **`HX-25`'s own guarantee is *"Replay with a stable identity"* = element `15`, also `ABSENT`** — the unbuilt control the re-grounding claimed to leave | primary register; `SA_CORR3_08` L177 |

> **The exclusion moved from one absent element to another absent element, and to the row whose own
> guarantee is the first absent element. `06_`'s closing claim is false, and re-verified as false.**

---

## 5. CLASSIFICATION ATTEMPT — all five candidate classes

| Class | Test | Result |
|---|---|---|
| **`FLOW`** | own trigger, source state, destination state distinct from `MF-01`/`MF-02`? | **NOT ESTABLISHED — but the evidence leans here.** `9 of 13` properties distinct. **Blocked by properties `8`, `9`, `13`**: the flow-population test is quantity/value effect, and that is undecidable |
| **`EXECUTION MODE`** | a **manner of performing** another flow? | **FALSIFIED ON ITS CITED GROUND** (§4). The primary register treats `HX-25` as a **row**, not as a mode of `HX-24` |
| **`DIMENSION`** | an attribute of a row? | **NO** — it carries an act, a receiver obligation and its own control references |
| **`CONTROL`** | a test or verification mechanism? | **NO** — `RT-E15-05` is the test **of** replay; **replay is the subject**, not the test |
| **`HYBRID`** | a combination? | **NOT REACHABLE** — every hybrid still requires the quantity/value determination that is absent |

> # `MF-03 CLASSIFICATION = NOT DECIDABLE`
>
> **Forcing it is prohibited by `§15` and would repeat `B7-F-10`'s defect: asserting a property of a
> flow on the strength of an unbuilt control.**

---

## 6. THE EXACT MISSING SEMANTIC — `§15`'s required output

> ## **MISSING SEMANTIC `MF03-MS-01`**
>
> ### **What makes two executions of a migration batch *the same execution*.**
>
> Formally: **element `15`, the Idempotency Identity** — the identity under which a replayed batch is
> recognised as already applied, and therefore contributes **`0` quantity and `0` value** rather than a
> second opening position.

**Why this and only this decides the classification:**

| If element `15` is specified such that… | Then `MF-03` is… |
|---|---|
| a replayed batch is recognised and contributes **`0` quantity, `0` value** | **`EXECUTION MODE`** — a manner of re-performing `MF-01`/`MF-02`, adding no flow |
| a replayed batch **can** contribute quantity or value | **`FLOW`** — it has its own quantity and value effect and must enter `IR`/`AR` as a member |

**Both branches are decidable the moment the semantic exists. Neither is decidable now.**

### 6.1 Owner and phase — and the distinction that matters

| | |
|---|---|
| **Owner** | **SMEs Core → Functional Design** |
| **Phase of the SEMANTIC** | **`S` — specifiable NOW.** Defining what makes two executions the same is a **design determination**, not a runtime measurement |
| **Phase of the PROOF** | **`I` — Build / Test.** Proving a re-run adds `0` requires a build |
| **Not Boss** | no election is required. **`§28`: do not escalate what SMEs Core can resolve** |
| **Not external** | no statutory or AAS+ input is involved |

> **`CORR2-MF3-01` — MATERIAL. The blocker is a specification, not a measurement.**
> `MF-03` has been carried as *"awaiting element `15`"* as though it were waiting on a build.
> **It is waiting on a definition.** The definition is within SMEs Core authority and has never been
> written — and the obligation that carried it (`CORR1-F-03`) **was dropped from the register** (`24_`).

**This session does not write it.** Specifying idempotency identity is a Functional Design act, and
inventing it here is exactly what `§18`/`§31` prohibit. **It is registered as `MF03-MS-01`, carried at
`28_` as a business-semantic gap and at `29_` as an FD blocker.**

---

## 7. CONSEQUENCE FOR THE FLOW POPULATIONS

`§24`: an unsupported **exclusion** counts as `UNRESOLVED` and is **not** removed from the denominator.

| Register | Published | Membership | Disposition |
|---|---:|---|---|
| `IR` flows | **`20`** | `IR-01`…`IR-18` **enumerated at `SA_CORR2_05` (`18` distinct, `18` rows, two shapes)** + `MF-01`, `MF-02` per `B9′` | **MEMBERSHIP SOUND** (`26_` §2 corrects `08_`) · **COMPLETENESS UNRESOLVED** — `MF-03` is a candidate `21`st member |
| `AR` flows | **`30`** | `AR-01`…`AR-29` **enumerated at `SA_CORR2_06` (`29` distinct)** + `MF-01` per `B9′` | **MEMBERSHIP SOUND** · **COMPLETENESS UNRESOLVED** |
| `IR` reconciled | `14` | `14 / 3 / 3` = `20` ✔ | decomposition published |
| `AR` reconciled | `15` | `15 / 14 / 1` = `30` ✔ | decomposition published |

**Positive control:** `PTX-01`…`-11` → `11` distinct ids in `2` files against a declared `11`; and
`IR-99` → `0`. **The enumeration instrument both fires and discriminates.**

> **The denominators are valid; their **completeness** is not.** `MF-03` sits outside them on a ground
> that is falsified, so it is carried as **`UNRESOLVED`** rather than as excluded — a state that resolves
> the moment `MF03-MS-01` is written.

---

## 8. `MF-01` — unchanged, with its precondition still unmeasured

`B7-F-09`'s narrowing of `CC-F-11` **stands**: under `Standard`, value is a policy attribute of the
product, corroborated at `SA_CORR3_03` L178. **`CORE-06` is the correct residue and is discharged at
architecture level.** `CORE-07`'s `FIFO` layer gap is the genuine sharpening (`24_`).

**`CORR2-MF-02` remains open and unmeasured:** the `Standard` asymmetry holds **only if the product
standard cost is itself established independently of the migration**, and **in a cutover the standard
cost is itself migrated data**. `06_` §1 neither states nor tests it. **Carried at `28_`.**

---

## 9. RESEARCH-COMPLETE DETERMINATION

**`§8` of the CORR2 governance:** a function may not be declared Research-Complete while a required
semantic is missing.

| | |
|---|---|
| `MF-03` **RESEARCH-COMPLETE** | **NO** |
| Reason | classification undecidable; `MF03-MS-01` absent; flow-population completeness unresolved |
| Handoff | **HOLD** |

---

## 10. CHECKPOINT

> **All `13` properties compared — **`9` DIFFER · `1` SAME · `3` UNDECIDABLE**; `06_` tested the one
> that returns *same*** · cited ground **falsified on `3` counts and re-verified** ·
> all `5` candidate classes tested · **`MF-03` = `NOT DECIDABLE`**, and **not forced** ·
> **`MF03-MS-01` named exactly: the Idempotency Identity — what makes two executions the same** ·
> **owner SMEs Core; the blocker is a SPECIFICATION, not a measurement** (`CORR2-MF3-01`) ·
> `IR`/`AR` memberships **corrected to SOUND**, completeness **UNRESOLVED** ·
> **`MF-03` NOT Research-Complete · `0` classification asserted without its measurement.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the SOLE FINAL APPROVER.**
