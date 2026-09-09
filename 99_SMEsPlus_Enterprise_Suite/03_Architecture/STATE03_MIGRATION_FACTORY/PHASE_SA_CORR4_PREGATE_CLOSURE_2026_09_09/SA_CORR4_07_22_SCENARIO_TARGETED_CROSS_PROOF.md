# SA_CORR4_07 — TARGETED 22-SCENARIO CROSS-PROOF RE-RUN

## CP-SA-C4-70 — 22-SCENARIO PRE-TEST HANDOFF QUALIFIED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR4-PREGATE-CLOSURE-001]`
Branch: `architecture/phase-sa-corr4-pregate-closure-2026-09-09-001`
Boss: **SOLE FINAL APPROVER**

---

## 1. Scope, and the question this file answers

Master prompt §9: *"Do not repeat the entire CORR3 exercise mechanically. Re-run the 22 scenarios
specifically against the four newly closed conditions and affected element 10 / element 15
dependencies."*

**This is a different question from the joint cross-proof's.** The joint cross-proof asks *is this
scenario `VERIFIED`* — and `VERIFIED` requires an implementation and an executed test. This file asks
*is the **Phase SA contract** for this scenario complete enough to hand to the Pre-Test Matrix* — and
that is answerable now.

**The two answers must never be conflated, and CORR3 supplies the discipline for keeping them apart:**

> `JCP3-F-02`, verbatim: *"**discharging element 10 moves the joint cross-proof result from `0 of 22`
> to `0 of 22`.**"*

**That result stands unchanged after CORR4, and CORR4 does not weaken it.** The `0 of 22`
`HOLD — EXACT PROOF GAP` tally is reproduced, not revisited.

---

## 2. What the four closures did and did not do to this register

| Closure | Effect on the 22 |
|---|---|
| **`C4-01`** privileged-path enumeration | **The context dimension of every scenario becomes testable.** `MTI-18`'s enumeration dependency is discharged, so `MTI-02`, `MTI-17` and part of `MTI-38` are no longer unprovable *in principle*. **No scenario changes result** |
| **`C4-02`** `XMC-C-D1` | **The interface half of element 10 is stated as one contract.** Element 10's *status* does not move; `0 of 10` handoffs compliant is unchanged. **No scenario changes result** |
| **`C4-03`** `CF-I-03` | **`MTI-43`'s three negative forms become constructible.** They remain unexecutable. **No scenario changes result** |
| **`C4-04`** compliance propagation | **No effect on this register.** A governance act, not an interface one |

> **`C4-07-F-01`. Zero of the twenty-two scenarios changes result, and that is the predicted outcome,
> not a disappointment.** CORR3 ran the counterfactual explicitly and published its answer before CORR4
> existed: *"Elements 10 and 15 together → **0** scenarios moving to `VERIFIED`."* **CORR4 closed less
> than element 10 — it closed element 10's *interface* half — so any result other than zero would
> falsify CORR3's counterfactual, and a round reporting movement here should be disbelieved.**

**What did change is the Pre-Test obligation**, per scenario, per dimension — §4.

---

## 3. Element 15, and why every scenario stays at `SA MATERIAL GAP`

Element 15 blocks all 22 unconditionally. **Its ownership was read at primary text, because CORR3's own
register and the source registers appear to disagree, and they do not:**

| Object | Owner | Status |
|---|---|---|
| **Designing the deterministic idempotency identity** | **SMEs Core** — *"a design act"*; *"none has been designed"* | **Open. Not commissioned in CORR4 and not one of the four conditions** |
| **Ruling whether idempotency is gate-blocking** | **Boss** — *"severity is Boss's call"*; *"Rule on whether idempotency is gate-blocking"* | **Open** |

**Two different objects with two different owners, both open.** CORR3's *"a design act, owner SMEs
Core"* answers the first; the source registers' *"owner Boss"* answers the second. **Neither is wrong,
and a round that read only one of them would mis-route the remedy.**

**And `JCP3-F-05b` binds:** the only idempotency carrier in the estate is *"table-global rather than
tenant-scoped"* — **so the sole mechanism that could satisfy element 15 is incapable of satisfying
element 10.** They are one missing object with two contractual names.

> **Therefore: `22 of 22` scenarios carry an `SA MATERIAL GAP`, and on every one of the 22 the gap
> includes element 15.** No amount of context work closes it.

---

## 4. The register

**Columns.** `T`/`C` = tenant / company context required · `PB` = privileged-bypass relevance
(the `SA_CORR4_01` classes that can execute this scenario) · `CF3` = `CF-I-03` applicability ·
`Idem` = idempotency scope · `Iface` = interface completeness **after** `C4-02`.

**Conclusion class** is for the **scenario as a whole**. The **context dimension** is stated separately
in §4.1, because that is what CORR4 moved.

| # | Scenario | T · C | PB classes | CF3 | Idem | Iface | **(c) blocker independent of el.10/15** | **Class** |
|---:|---|:---:|---|:---:|:---:|:---:|---|---|
| 1 | Stockable purchase receipt → handoff | **M · M** | 4, 5, 6, 11 | ✔ | all | contract-stated | el.4/7 COGS; goods-received bridge is a **swept suspense account**, not item-matched | **`SA MATERIAL GAP`** |
| 2 | Vendor bill with receipt timing variation | **M · M** | 4, 5, 6, 11 | ✔ | all | contract-stated | el.4/7; **no prior-period attribution mechanism exists at all** | **`SA MATERIAL GAP`** |
| 3 | Stockable sales delivery → cost handoff | **M · M** | 4, 5, 11 | ✔ | all | contract-stated | el.4/7; `BP-02` (COGS at delivery) **not selectable** | **`SA MATERIAL GAP`** |
| 4 | Customer invoice, delivery timing variation | **M · M** | 4, 5, 11 | ✔ | all | contract-stated | el.4/7. `JT-04`'s `CONFLICTING` flag **discharged** by CORR2 — the only scenario whose named blocker was closed | **`SA MATERIAL GAP`** |
| 5 | Partial receipt | **M · M** | 4, 5, 6, 11 | ✔ | all | contract-stated | el.4/7; over-receipt tolerance **undefined** | **`SA MATERIAL GAP`** |
| 6 | Partial delivery | **M · M** | 4, 5, 11 | ✔ | all | contract-stated | el.4/7; **`H-05`** — a draft invoice consumes billable quantity while posting nothing and is **freely deletable** | **`SA MATERIAL GAP`** |
| 7 | Backorder | **M · M** | 4, 5 | ✔ | all | **`R-17` NO CONSUMER** | remainder-supply record **has no consumer at all**; never-mode cancellation leaves **no document trail** | **`SA MATERIAL GAP`** |
| 8 | Purchase return | **M · M** | 4, 5, 11 | ✔ | all | contract-stated | el.4/7; return basis conflict `PENDING`; **Boss decision class** | **`SA MATERIAL GAP`** |
| 9 | Sales return | **M · M** | 4, 5, 11 | ✔ | all | contract-stated | el.4/7; **`JT-05` NOT DECIDABLE** — original- vs current-cost reversal basis; **Boss** | **`SA MATERIAL GAP`** |
| 10 | Cancellation before physical execution | **M · M** | 4, 5, 11 | ✔ | all | contract-stated | `C-01` symmetry + `C2-F-01` durability — **both resolved at `SA_CORR3_01`**; residue is the `XD-01` **Boss decision** on which state blocks cancellation | **`SA MATERIAL GAP`** |
| 11 | Correction after physical execution | **M · M** | 4, 5, 7, 8 | ✔ | all | contract-stated | the **only** correction route after a completed movement is a return; **corrected-entry link does not exist** | **`SA MATERIAL GAP`** |
| 12 | Inventory count / adjustment | **M · M** | 4, 5, 7 | ✔ | all | contract-stated | **approval mechanism absent**; an adjustment can **silently reduce a reservation** | **`SA MATERIAL GAP`** |
| 13 | Scrap / damage / write-off | **M · M** | 4, 5 | ✔ | all | contract-stated | **salvage is undefined, not merely unproven**; scrap has **no cost causality**; `TH-HOLD-02` | **`SA MATERIAL GAP`** |
| 14 | Internal warehouse transfer — no financial effect | **M · M** | 4, 5, 9 | ✔ | all | contract-stated | **`R4-F-18` — no independent check exists**; neutrality is **configuration-protected only** | **`SA MATERIAL GAP`** |
| **15** | **Multi-company / tenant boundary** | **M · M** | **1, 2, 3, 6, 9, 10, 11, 12, 13** | **✔✔** | all | **contract-stated — this is `C4-02`'s subject** | **this scenario *is* element 10**; `0 of 8` isolation proofs; **`SA10-F-05` two lock-defeat paths, the second leaving no record**; **and `C4-01` `G1`/`G2` add four unscoped path classes and a baseline contradiction** | **`SA MATERIAL GAP`** |
| 16 | Manufacturing RM → WIP → FG | **M · M** | 4, 5 | ✔ | all | `R-22` `GAP` | el.4/7; **fixed-overhead elements have no injection path** | **`SA MATERIAL GAP`** |
| 17 | Manufacturing reversal / scrap / variance | **M · M** | 4, 5 | ✔ | all | `R-22` `GAP` | el.4/7; **no variance mechanism exists** — one of nine recognised | **`SA MATERIAL GAP`** |
| 18 | Stockable vs consumable vs service routing | **M · M** | 4, 5 | ✔ | all | contract-stated | **two-axis classification tie-break undefined**; **`BD-ACC-01` is silent for services** — `XMC-C-C1`…`C6` address it and are unreviewed; **Boss** | **`SA MATERIAL GAP`** |
| 19 | Period-end / cut-off | **M · M** | 4, 5, 7 | ✔ | all | contract-stated | el.4/7; **no accounting-period object exists**; reconciliation holds at the closing boundary, not continuously | **`SA MATERIAL GAP`** |
| 20 | Historical migration across fiscal years | **M · M** | **8** | ✔ | all | **el.14 attaches** | **the provenance reference does not exist and must be originated** — `GAP-FS-08` | **`SA MATERIAL GAP`** |
| 21 | AI migration mapping + deterministic reconciliation | **M · M** | **7, 8** | ✔ | all | **el.14 attaches** | element 14; **`MTI-42` prohibits inferring context at migration** and cannot evidence the compliant act | **`SA MATERIAL GAP`** |
| **22** | **Retry / idempotency / replay** | **M · M** | 4, 5, 11 | ✔ | **this scenario *is* element 15** | contract-stated | `RISK-C02` `CARRIED / BLOCKING`; **`UAE-29` `HOLD — BOSS DECISION REQUIRED — the root`** | **`SA MATERIAL GAP`** |

**Tally: `0 SA CONTRACT COMPLETE` · `0 SA EVIDENCE COMPLETE` · `22 SA MATERIAL GAP` · `0 NOT
APPLICABLE`.** 22 rows, each classified once. ✓

**`T · C` is `M · M` on all 22** and that is not a padded column — it is `R1` and `R2` of the
`XMC-C-D1` contract applied, and **all 22 are company-scoped business facts**, so no row takes the
`N/A with reason` branch. **`CF-I-03` applies to all 22** because every row records an act.

### 4.1 The dimension that did move

**Per scenario, the *context and authorization dimension* is now:**

> **`SA CONTRACT COMPLETE — RUNTIME TEST REQUIRED` on `22 of 22`.**

Because: `T`/`C` are contract-mandatory (`C4-02` `R1`/`R2`); the emitting fields are specified
(`HF-CTX-01`…`-11`); the execution paths that could bypass them are enumerated (`SA_CORR4_01`, 13
classes); the conformance control that attests them is specified to test-writable granularity
(`SA_CORR4_03`, 25 test classes); and `MTI-43`'s three negative forms are constructible.

> **`C4-07-F-02`. This is the whole of CORR4's movement in this register, stated exactly: one dimension
> of twenty-two scenarios goes from *not writable as a test* to *writable and not executable*.** It is
> a real change and it is **not** a change of scenario result. **A summary that reported `22 of 22`
> without naming the dimension would be false.**

---

## 5. The exact Pre-Test obligation, per gap class

| Class | Scenarios | n | Pre-Test obligation |
|---|---|---:|---|
| **Element 15** | all | **22** | **May NOT be tested.** The object does not exist. Any Pre-Test case asserting retry-safety, replay-safety or duplicate detection **would pass vacuously** and must not be written |
| **COGS gap, el. 4/7** | 1–6, 8, 9, 13, 16, 17, 19 | **12** | May not be tested. Joint decision |
| **A design mechanism that does not exist** | 2, 7, 12, 13, 14, 16, 17, 19 | **8** | May not be tested. Origination act |
| **A Boss decision** | 8, 9, 10, 18, 22 | **5** | May not be tested. Normative |
| **Element 14** | 20, 21 | **2** | May not be tested. Origination act |
| **Context + authorization dimension** | all | **22** | **MAY be prepared in full and executed the moment an implementation exists.** The 25 `CF-I-03` test classes, `MTI-43`'s three negative forms, and the four-axis negative set `S-01`…`S-08` are all writable now |

**A scenario appears in more than one row above; the rows are gap classes, not a partition of the 22.**
Stated because CORR3 recorded a programme defect of exactly this shape — a count whose unit was
conflated with its population.

### 5.1 The three prohibitions the Pre-Test Matrix must carry verbatim

1. **Nothing may be read as testing tenant isolation until an implementation exists.** `0 of 8`
   isolation proofs, `0 of 52` negative access tests, `0 of 13` enforcement surfaces — *"because no
   implementation exists."*
2. **Nothing may be read as testing idempotency.** The carrier is *"table-global rather than
   tenant-scoped"*, and `0 of 13,814` rows in the production-scale database carry a deduplication key.
   **A test over that population returns clean and means nothing** — the programme's recorded
   *control-that-cannot-detect-its-own-failure* class.
3. **Nothing may be read as testing a cross-module join.** Element 15 is the join key and it does not
   exist.

### 5.1a `C4-07-F-03` — the Pre-Test handoff baseline over-grades the one dimension that cannot be tested

**Found while establishing §5.2's ordering against the existing Pre-Test baseline, and it is the most
consequential finding in this file for the decision Boss is being asked to take.**

`SA17_PRE_TEST_MATRIX_HANDOFF_BASELINE.md` — **the artefact that hands work to the phase under
consideration** — grades scenario `E2E-15` *Correction / reversal / retry / duplicate*:

> `TRAVERSABLE` · expected evidence *"idempotent retry; ordering-independent reconciliation"* ·
> bounded risk carried: ***"Strongest established area"***

`SA15_END_TO_END_SCENARIO_REGISTER.md` agrees and names its source:

> `E2E-15` … `TRAVERSABLE` — *"strongest area: **idempotency and ordering-independence established
> (`SA09`)**"*, and *"`E2E-02` … `E2E-11` … `E2E-12` and `E2E-15` … are the **only** end-to-end flows
> that traverse without a named break."*

**`SA09` has since been corrected to say the opposite, in its own text:**

> `SA09_EXCEPTION_REVERSAL_MATRIX.md`, inline: *"**SUPERSEDED BY CORR2 — `SA_CORR2_09` §3** … and
> **idempotency moves the other way** — graded `ESTABLISHED` here, **recorded absent in four Accounting
> packages.**"*

And the joint cross-proof's scenario 22 — **the same subject** — is `HOLD`, with `RISK-C02`
`CARRIED / BLOCKING`, `UAE-29` `HOLD — BOSS DECISION REQUIRED — the root`, the only carrier in the
estate *"table-global rather than tenant-scoped"*, and **`0 of 13,814` rows carrying a deduplication
key**.

**Measured, with a positive control:**

| Document | `SUPERSEDED` blocks | cites `SA_CORR2_09` | cites `RISK-C02` | cites *"element 15"* |
|---|---:|---:|---:|---:|
| `SA09` *(positive control — carries the correction)* | **1** | — | — | — |
| `SA15` | **2** — and **neither touches `E2E-15`**; both correct the *other* scenarios' distribution | **0** | **0** | **0** |
| **`SA17`** | **0** | **0** | **0** | **0** |

> **`C4-07-F-03`. The one scenario the Pre-Test handoff baseline grades as its strongest established
> area is the one the joint cross-proof grades `HOLD` with its enabling object absent — and the
> correction that reconciles them exists on the upstream document and propagated to neither
> consumer.** `SA17` carries **no supersession block at all**.
>
> **This is the programme's recorded *a revision log is not a correction* defect, and `SA15`'s own
> header documents that exact defect class three lines above the uncorrected row** — *"CORR1's `CH-05`
> corrected the §4 table and not the header that summarises it — the same revision-log defect the
> package documents elsewhere."*
>
> **Consequence, and it is a safety consequence, not a tidiness one.** A Pre-Test Matrix built from
> `SA17` would schedule `E2E-15` as low-risk and expect *"idempotent retry"* as its evidence.
> **That evidence cannot be produced, and the test would return clean** — the estate's only carrier
> admits unlimited empty values, so a uniqueness check over it passes on every row. **A clean result
> from a control that cannot fail is the programme's recorded
> *control-that-cannot-detect-its-own-failure* class, and this is where it would land.**

**Correction owner: the `SA15`/`SA17` owner, as a Phase SA act.** Not corrected here — **this session
does not overwrite another artefact's disposition**, and `SA15`/`SA17` are Phase SA baseline documents
whose amendment is their owner's act. **Carried to the Boss Final Gate as the first item the Pre-Test
Matrix must not inherit uncorrected.**

### 5.2 What must be tested **first**, and why that order

**In dependency order, not effort order:**

1. **`MTI-50` retention** — `CF-I-03` is unbuildable without a historised grant store. **Not partially:
   at all.**
2. **`CF-I-03` `CF3-C-01`…`C-04`, the instrument controls** — synthetic injection, discriminating
   population, coverage assertion, negative control. **Before any positive test**, because this
   control's characteristic failure is a **false clean result** and no positive test detects it.
3. **`CF3-B-02`** — a grant issued *after* the act must be `D1`. **The one boundary case an
   implementation reading current grants passes wrongly**, and it passes wrongly *silently*.
4. **`CF3-B-07`** — an actor holding grants in two tenants. **The membership-vs-execution boundary,
   tested directly**, against the `C4-01` `G2` contradiction.
5. **The four unscoped path classes** — `C4-01` `G1`: platform operator, service account, internal
   service-to-service, wallet/prepaid. **A test suite that omits them tests the paths that were
   specified and none of the paths that were not**, which is how the enumeration's residual becomes a
   silent pass.

---

## 6. Residual

1. **`C4-01`'s enumeration widened this register's attack surface and closed none of it.** Scenario 15
   now carries **nine** privileged path classes rather than an unenumerated set. **More classes is a
   better description and a worse position**, and this file reports both.
2. **The `PB` column is a mapping I made.** No prior artefact maps path classes to scenarios. Where I
   assign classes 4/5 to a scenario I am asserting that scenario can be executed by a background or
   scheduled run; that is a design inference from the scenario's trigger, and a challenger should test
   the assignments individually rather than the column as a whole.
3. **`22 of 22 SA MATERIAL GAP` is a result about Phase SA's remaining work, and 6 of the gap classes
   are not Phase SA's to close** — the COGS gap, five Boss decisions, and element 15's severity ruling.
   **A reader taking `22 of 22` as a measure of Phase SA's incompleteness would over-attribute.**

## 7. Checkpoint

> ## `CP-SA-C4-70 — 22-SCENARIO PRE-TEST HANDOFF QUALIFIED`
> **22 re-run · `0 SA CONTRACT COMPLETE` · `0 SA EVIDENCE COMPLETE` · `22 SA MATERIAL GAP` ·
> `0 NOT APPLICABLE`.**
> **The context and authorization dimension is `SA CONTRACT COMPLETE — RUNTIME TEST REQUIRED` on
> `22 of 22`.** **Joint cross-proof result unchanged at `0 of 22`, exactly as CORR3's counterfactual
> predicted.** **2 findings — `C4-07-F-01`, `C4-07-F-02`.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
