# SC-11 — BOSS DECISION PROPAGATION REGISTER

Session `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · Branch `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Head at ruling `e113258f` · 2026-09-10 · **Boss is the SOLE FINAL APPROVER.**

**Every count below is recomputed from the decision records, not inherited from a headline.**

---

## 1. What Boss ruled

| Record | Subject | Ruling |
|---|---|---|
| `SC-BD-01` | **`FG-F-06`** scope clarification | **`READING B`** — `8C-001` does **not** bind the Phase SA exit to Pre-Test |
| `SC-BD-02` | `F4` | `XMC-D-02` = **EXTEND to all boundaries** · `C2-D-01` = **soft binding confirmed** |
| `SC-BD-03` | `F6` | `MTI-D-04` = **no cross-company grant in v1** · `TV6-BOSS-02` = **company-scoped** |
| `SC-BD-04` | `F7` | **Confirm the registers as they stand** · `location` is **not** an authorization axis |
| `SC-BD-05` | `F1` | `JT-04` = **physical movement** · `JT-05` = **original cost** |
| `SC-BD-06` | `F5` | `POH-D-06` = **RESTATE** · **normal capacity confirmed** as the absorption denominator |
| `SC-BD-07` | `F2` | **`block`**, on all three members, as one principle |
| `SC-BD-08` | `F3` | **Option (a)** — apply `BD-ACC-03A` as ruled, no route-specific exception |
| `SC-BD-09` | `F8` | **Option (b)** — design input, not gate-blocking |
| `SC-BD-10` | The five acts | **`B-7`, `C4-D-01`, `C4-D-02`, Thai panel APPROVED** · **`AAS-V-02` ratification NOT selected** |

## 2. Decision population, recomputed

| Family | In family | **Ruled** | **Still open** | Open IDs |
|---|---:|---:|---:|---|
| `F1` | 2 | **2** | 0 | — |
| `F2` | 3 | **3** | 0 | — |
| `F3` | 1 | **1** | 0 | — |
| `F4` | 2 | **2** | 0 | — |
| `F5` | 6 | **1** | **5** | `POH-D-01` `POH-D-02` `POH-D-03` `POH-D-04` `POH-D-05` |
| `F6` | 4 | **2** | **2** | `RC-D-03` `RC-D-04` |
| `F7` | 4 | **4** | 0 | — |
| `F8` | 1 | **1** | 0 | — |
| **Total** | **23** | **16** | **7** | |

**Validated three ways:** sum of family totals = **23**; ruled + open = 16 + 7 = **23**; length of the
enumerated open-ID list = **7**. All three agree.

> ### `16 of 23 RULED · 7 STILL OPEN · 0 ADDED · 0 REMOVED`

**No decision was dissolved by ruling it.** `F3` was resolved on the branch that requires nothing further
of Boss, so it leaves the *forward* list — but it is counted **ruled**, not removed, because Boss ruled it.

## 3. `SC-BD-F-01` — a defect in the controlling package, found at ruling time

`SC-06` §8 asserts: *"**23** Boss decisions in 8 questions … **each with a recommendation** and an SMT
disposition."*

**That claim is false for 2 of the 23.**

| Shape | Instrument | Result |
|---|---|---|
| **1** | every mention of `RC-D-03` / `RC-D-04` across the whole controlling package | 3 mentions — the `F6` membership list, the question sentence, and the `BD-ACC-02`-side table. **No recommendation** |
| **2** | either ID adjacent to a recommendation verb (`recommend`, `→`, `proposes`) | **0 hits** |
| **Control** | the same pattern on `MTI-D-04` / `TV6-BOSS-02` | **fires** — *"`MTI-D-04` → no cross-company grant in v1"*, *"`TV6-BOSS-02` → company-scoped"* |

**Consequence, and it was caught before it reached Boss:** the `F6` card put four members to Boss under one
recommendation that covered **two**. Presenting the family-level recommendation as covering all four would
have **put a SMEs Core position in Boss's mouth for `RC-D-03` and `RC-D-04`**, which gate prompt §4
expressly forbids. **`SC-BD-03` therefore records 2 of 4 ruled**, and the two remain open.

**Root cause:** the *"each with a recommendation"* claim was verified at **family** level (8 of 8 families
carry a recommendation) and asserted at **member** level (23 of 23). A count's unit again.
**Prevention control:** a family-level assurance may not be restated at member level without a member-level
sweep. This is the same unit-conflation class the programme has recorded repeatedly.

**Not an `SMT Escape`** — it did not reach Boss. It is a package defect detected by the execution owner at
the point of use.

## 4. Vetoes — recomputed

> ### `6 IN FORCE · 0 DISCHARGED · 0 SELF-DISCHARGED`

| Veto | Effect of this round's rulings | Who releases it |
|---|---|---|
| `AAS-V-01` | unchanged — awaits runtime proof | AAS+, Boss ratifies · **implementation start** |
| `AAS-V-02` | **condition satisfied; ratification WITHHELD at `SC-BD-10`** — in force | AAS+ discharge, Boss ratifies |
| `AAS-V-03` | COGS limb **vacuous** on `SC-BD-03`'s branch. **Vacuous is not discharged** | AAS+ |
| `RC-V-01` | unchanged — **bars implementation start**; needs the independent check over the wider five-row set. **This requirement issues from AAS+ / RC, not `8C-001`**, so `SC-BD-01` does not touch it | AAS+ after the check, Boss ratifies |
| `CF-V-01` | unchanged — awaits runtime proof | AAS+, Boss ratifies · **implementation start** |
| `CF-V-02` | **first limb closed** by `SC-BD-03`. The veto is **not** lifted | AAS+ |

## 5. Acts — recomputed

**5 in the population · 4 approved · 1 held.** `B-7`, `C4-D-01`, `C4-D-02` and the Thai panel are
**approved**; **`AAS-V-02` ratification was not selected** and stays outstanding.

**No approved act is Pre-Test-entry blocking** under `SC-BD-01`. **`B-7`'s appointment does not itself
create an independent pass** — structurally independent passes remain **0**.

## 6. New obligations created by this round

| # | Obligation | Owner | Created by |
|---:|---|---|---|
| 1 | **AAS+ concurrence on `POH-D-06`'s restatement.** Boss's ruling alone does not complete it — *"restating a veto limb is reserved to the veto's **issuer and Boss**"* | **AAS+**, Boss ratifies | `SC-BD-06` / `SC-ADD-01` |
| 2 | **A SMEs Core recommendation on `RC-D-03` and `RC-D-04`** before either is re-put to Boss | **SMEs Core** | `SC-BD-F-01` |
| 3 | **Reconciliation-control design for the `Average`-costing original-cost reversal residual.** `09_JT05` §5 assigns it to **Boss** at primary text | **Boss**, on SMEs Core input | `SC-BD-05` / `SC-SMT-01` |
| 4 | **Re-word veto limb 2** so it no longer *"tests for uniqueness where the answer is zero"*, before any discharge attempt | SMEs Core + AAS+ | `SC-BD-06` |
| 5 | Per-boundary **applicability declaration** carried in the contract amendment with contract-level authority; attestation `HF-CTX-06`/`-11` extended to 12 boundaries | SMEs Core | `SC-BD-02` |
| 6 | **Per-company export becomes a designed deliverable** | SMEs Core | `SC-BD-03` |
| 7 | `M-1`…`M-6` carried into Functional Design and Pre-Test as assertions | SMEs Core | `SC-BD-07` |
| 8 | Element 15 proof + `RT-E15-01`…`-09` written into **Pre-Test exit criteria** | Pre-Test | `SC-BD-09` |
| 9 | Execute the four approved acts; `AAS-V-02` ratification remains open to Boss | Boss / appointees | `SC-BD-10` |

## 7. Not re-openable

`FG-F-06` (`SC-BD-01`) · `BOSS-ROUTE-01` · `BD-ACC-01` · `BD-ACC-02` · `BD-ACC-03A` · `BD-ACC-03B` ·
`MTI-D-01`/`-02`/`-03` · `Q-BOSS-02` · `BD-02` · `BD-04` · `C2-D-02` · `UAE-29` (ruled via `BD-ACC-01`) ·
the `F3` standing dissent · whether idempotency is required (only severity was open, now ruled) ·
the `26` and `25` decision headlines (superseded — **23**).

## 8. Authority

> Boss is the **SOLE FINAL APPROVER**. **Phase SA is NOT closed. No veto is discharged. No structural
> independence is claimed. No `PASS` is declared.** No SMEs Core recommendation was converted into a
> ruling except where Boss explicitly selected it.
