# PT-09 — EXCEPTION / REVERSAL / RECOVERY / IDEMPOTENCY MATRIX

## `CP-PT-09 — FAILURE MODES COVERED`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]`
Branch: `architecture/account-phase-pretest-new-session-2026-09-10-001` · head consumed `bcea9952`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **Element 15 is the join key. It is specified and NOT BUILT.**
> **Nothing in this file may be read as testing idempotency or any cross-module join.**

---

## 1. Result

| | |
|---|---|
| **Boss obligation discharged by this checkpoint** | **`1`** — `SC-BD-09` §8.1, §4 |
| **Pre-Test exit criteria constituted** | **`11`** — `PTX-01`…`PTX-11`, §4 |
| **Material findings** | **`3`** — `PT09-F-01`, `-F-02`, `-F-03` |
| Idempotency severity | **Boss-ruled `SC-BD-09` = `DESIGN INPUT, NOT GATE-BLOCKING`** |
| Whether idempotency is *required* | **NOT RE-OPENABLE** — `BD-ACC-01` rules it; `UAE-29` thereby ruled |
| Deduplication carrier in the reference estate | **`0 of 13,814` rows** |
| Reversal semantics | **ESTABLISHED** — a new event referencing the original |
| Reversal **value basis** | **Boss election `JT-05`** — original vs current cost |
| Correction after a completed movement | **the corrected-entry link DOES NOT EXIST** |
| Runtime obligations written into exit criteria | **`RT-E15-01`…`-09`**, verbatim |

---

## 2. `PT09-F-01` — MATERIAL: a Boss instruction with no receiving artefact — **and this checkpoint discharges it**

### The instruction

`SC-BD-09` (`F8`, idempotency severity), ruled `OPTION (b) — DESIGN INPUT, NOT GATE-BLOCKING`:

> **§7:** *"Not entry-gating. **It sets Pre-Test *exit* criteria** — which is why it was ruled **before**
> those criteria are agreed."*
> **§8.1:** *"Element 15 is specified and not built. The deterministic-identity proof and
> `RT-E15-01`…`RT-E15-09` become **Pre-Test exit criteria**, and **must be written into them**."*

### The measurement

**PATH SET:** the Pre-Test prompt set. **Positive control:** `checkpoint` → **`23`** in the master prompt.

| Token | `00_…CONTEXT_AND_LINEAGE.md` | `01_…MASTER_PROMPT.md` |
|---|---:|---:|
| `exit criteri` | **`0`** | **`0`** |
| `RT-E15` | **`0`** | **`0`** |
| `checkpoint` *(control)* | `0` | **`23`** |

**The Pre-Test prompt structure defines `23` checkpoints and `0` exit criteria.** Boss's instruction to
write `RT-E15-01`…`-09` into the Pre-Test exit criteria therefore arrived at a phase that **has no such
set to write them into**.

> **This is an unconsumed instruction, not a disagreement.** The programme's recorded failure mode is that
> a prior round's directive *"sat unconsumed for a whole round"*. **`SC-BD-09` §8.1 is a Boss direction
> addressed to this phase, and it had not been actioned.**

### Discharge

**This checkpoint constitutes the Pre-Test exit-criteria set at §4 and writes the nine obligations into it
verbatim.** This is **within authority**: Boss expressly directed it; constituting exit criteria is not
Functional Design, not implementation, not a veto discharge, and not a re-scoping of any ruled denominator.

| | |
|---|---|
| Status | **DISCHARGED BY THIS CHECKPOINT** |
| Confirmation required | **`PT-16` presents `PTX-01`…`PTX-11` to Boss for adoption** — SMEs Core may constitute and propose; **Boss adopts** |

---

## 3. The idempotency position, as ruled

| Question | Answer | Authority |
|---|---|---|
| Is idempotency **required**? | **YES, always, for accounting events** — `BD-ACC-01`'s sentence is **unqualified** | **NOT RE-OPENABLE** (`SC-BD-09` §8.2) |
| Is its absence **gate-blocking**? | **NO — design input** | `SC-BD-09` `OPTION (b)` |
| Who owns the canonical event identity? | **Accounting Core** | `SC-BD-09` §8.3 |
| Who determines *when* idempotency is required? | resolved: the contract §4 condition is **always met**, so the protection is **not vacuous** | `SC-SMT-03` |

### 3.1 The history Boss was shown — and why it belongs in this file

`SC-BD-09` §4, verbatim:

> *"**History Boss was shown, and it cut against the recommendation:** CORR5's first freeze declared this
> *'dissolved by standing rulings'* and **two challengers independently reversed it**. It was presented as
> open **precisely because the executing party twice tried to close it.**"*

> **The executing party twice tried to close this item and was twice reversed by challengers.** This
> session is the same execution body. **That is the strongest available reason for it not to treat any
> element-15 question as settled by its own reasoning** — and it is why `PT-02`'s withdrawn `PT02-F-02`
> was resolved by following a pointer to primary text rather than by argument.

---

## 4. `PTX-01`…`PTX-11` — PRE-TEST EXIT CRITERIA, CONSTITUTED

> **Proposed by SMEs Core under `SC-BD-09` §8.1. `PT-16` presents these for Boss adoption.**
> **None is satisfied. All are `PTE-3` or higher.**

| ID | Exit criterion | Class | Source |
|---|---|---|---|
| **`PTX-01`** | `RT-E15-01` — present one basis twice → **exactly one** Accounting Event; the second presentation returns the first identity | `PTE-3` | `SC-BD-09` §8.1 |
| **`PTX-02`** | `RT-E15-02` — same occurrence, two recognition roles → **two** events, each joinable to the occurrence | `PTE-3` | " |
| **`PTX-03`** | `RT-E15-03` — reversal discoverable from its original **and vice versa**; the original unchanged **byte-for-byte** | `PTE-3` | " |
| **`PTX-04`** | `RT-E15-04` — two tenants, byte-identical occurrence identities → **two distinct** events; **a never-transacted tenant returns a structurally DIFFERENT result from a clean one, not the same zero** | `PTE-3` **negative + discriminating population** | " |
| **`PTX-05`** | `RT-E15-05` — replay of a batch reproduces identical identities and adds **zero** events; batch identity present beside each, **absent from the basis** | `PTE-3` + element 14 | " |
| **`PTX-06`** | `RT-E15-06` — `A14`: same attempt identity written twice → **one** fact; a write with **no** attempt identity → **refused and recorded** | `PTE-3` positive + negative | " |
| **`PTX-07`** | `RT-E15-07` — an identity computed on day 1 and recomputed on day 90 **from the stored basis** is byte-identical | `PTE-3` | " |
| **`PTX-08`** | `RT-E15-08` — **synthetic injection**: inject one fact whose basis differs by one part; confirm the event count moves **`1 → 2`**. *Proves the predicate can fire* | **`PTE-3` INSTRUMENT** | " |
| **`PTX-09`** | `RT-E15-09` — **coverage assertion**: presentations **requested vs recognised vs refused**, published beside every run | **`PTE-3` INSTRUMENT** | " |
| **`PTX-10`** | The **deterministic-identity proof** itself — the six-part basis (`XMC-C-A2`) demonstrated deterministic and duplicate-preventing | `PTE-3` | `SC-BD-09` §8.1 |
| **`PTX-11`** | **Ordering constraint, binding on all of the above:** `MTI-50` built → `CF3-C-01`…`C-04` instrument controls → **only then** any positive test; and `RT-E15-08`/`-06` **before any scenario's retry dimension is scheduled** | **ORDER GATE** | `SA17` §2a |

### 4.1 Why `PTX-08`, `PTX-09` and `PTX-11` are the load-bearing three

**`PTX-01`…`PTX-07` and `PTX-10` are the tests. `PTX-08`, `PTX-09` and `PTX-11` are what make their
results mean anything.**

- **`PTX-08` synthetic injection** proves the predicate **can fire**. Without it, a duplicate-prevention
  test that finds no duplicates is indistinguishable from a test that cannot detect them.
- **`PTX-09` coverage assertion** publishes **requested vs recognised vs refused**, so a run that silently
  processed a subset is visible.
- **`PTX-11`** prevents a positive test being scheduled before its instrument controls exist.

> **`SA17` §2b prohibition 2 states the hazard exactly: the carrier is table-global, `0 of 13,814` rows
> carry a deduplication key, and *"a test over that population returns clean and means nothing."***
> **A clean result from an instrument that cannot fail is the specific outcome these three criteria exist
> to prevent** — and it is the failure mode this programme has recorded most often.

---

## 5. Exception, reversal, correction, cancellation — the matrix

| Failure mode | Specified? | State |
|---|---|---|
| **Reversal** | **YES — ESTABLISHED** | a new event referencing the original (`BD-ACC-01`, `XMC-C-A8`) |
| **Reversal value basis** | **NO** | **Boss election `JT-05`** — original vs current cost. SMEs Core recommendation: **original cost** (a current-cost reversal *"manufactures a margin no sale earned"*); `TH-NEW-02` statutory `HOLD` |
| **Correction** | **PARTIAL** | `XMC-C-A9`. **After a completed movement the ONLY route is a return, and the corrected-entry link DOES NOT EXIST** (`X-11`) |
| **Cancellation before physical execution** | **PARTIAL** | design resolved (`SA_CORR3_01`); `C-01` symmetry; `C2-F-01` durability; **Boss election `XD1-P1`** |
| **Never-mode remainder cancellation** | **DEFECT** | *"leaves **no document trail**"* → `XMC-C-D5` (`X-07`) |
| **Retry (same event)** | **specified, NOT TESTABLE** | element 15 not built |
| **Duplicate submission** | **specified, NOT TESTABLE** | ditto |
| **Replay / migration batch** | **NO CARRIER** | element 14 — *"the provenance reference does not exist and must be originated"* |
| **Out-of-order / stale events** | **NOT REPRESENTED** | `0` corpus representation → `PT-S-07` |
| **Partial mid-chain failure** | **NOT REPRESENTED** | `0` corpus representation → `PT-S-07` |
| **Reversal after downstream consumption** | **NOT REPRESENTED** | → `PT-S-06` |
| **Payment/settlement durability** | **DEFECT** | `H-07` **`NOT DURABLE`** — matching is *"not an entry"*, matching rows are **freely destructible across a closed period**, and **cash-basis tax keys off it** |

### 5.1 `PT09-F-02` — MATERIAL: the correction path and the reversal path are the same path, and one end is missing

**Three records converge:**

1. **`X-11`:** *"the **only** correction route after a completed movement is a return; corrected-entry link **does not exist**."*
2. **`X-09`/`JT-05`:** the return's **value basis** is an unruled Boss election.
3. **`PT-S-06`** (this session's addition): **reversal after a downstream module has consumed the output** has no representation at all.

> **Composed: after a completed movement, a correction must become a return; the return's value is
> undecided; and if a downstream module already consumed the original output, there is no specified
> behaviour at all.** Each of the three is separately recorded as open. **Their composition is not
> recorded anywhere** — and it is the ordinary business case of *"we shipped it, billed it, the customer
> returned it, and month-end already closed."*

| | |
|---|---|
| Status | **OPEN — MATERIAL, composition not previously recorded** |
| Routed to | `PT-12` (as one composed row), `PT-13`, **B-7** |

### 5.2 `PT09-F-03` — the durability defect undermines the reversal guarantee it sits beneath

**`XMC-C-A8` guarantees a reversal references its original.** `H-07` records that **payment matching is
*"not an entry"* and matching rows are *"freely destructible across a closed period"***.

> **A reversal that references an original whose settlement linkage can be destroyed after period close
> preserves the reference and loses the fact it refers to.** `RT-E15-03`/`PTX-03` requires the original be
> *"unchanged byte-for-byte"* — **`H-07` describes a path on which it is not.** Carried as a **direct
> conflict between an established semantic and a measured estate behaviour**, unresolved here.

---

## 6. What may NOT be claimed

**Carried verbatim and unweakened (`SA17` §2b):**

1. **Nothing may be read as testing tenant isolation until an implementation exists.**
2. **Nothing may be read as testing idempotency.** `0 of 13,814` rows carry a deduplication key.
3. **Nothing may be read as testing a cross-module join.** Element 15 is the join key; specified, not built.

**And `SA17`'s reading of the historical prohibition, carried:** the element-15 case **may be written**,
and **may not be executed or read as passing** until built. **This checkpoint writes; it does not execute.**

---

## 7. Checkpoint

> ## `CP-PT-09 — FAILURE MODES COVERED, NONE PROVEN`
>
> **`PT09-F-01` MATERIAL, AND DISCHARGED — Boss's `SC-BD-09` §8.1 directed that `RT-E15-01`…`-09` and the
> deterministic-identity proof *"must be written into"* Pre-Test **exit criteria**; the Pre-Test prompt set
> contains **`0`** references to exit criteria and **`0`** to `RT-E15` (positive control `23`). **The
> instruction had no receiving artefact. This checkpoint constitutes `PTX-01`…`PTX-11` and writes the nine
> in verbatim**, for Boss adoption at `PT-16`** ·
> **`PT09-F-02` MATERIAL — correction-after-movement must become a return, the return's value is an unruled
> Boss election, and reversal after downstream consumption has no representation. Three open items whose
> **composition** — the ordinary ship/bill/return-after-close case — is recorded nowhere** ·
> **`PT09-F-03` — `H-07`'s freely-destructible matching rows conflict directly with `XMC-C-A8`/`PTX-03`'s
> *unchanged byte-for-byte* original** ·
> Idempotency: **required (not re-openable), severity ruled non-gate-blocking**; the executing party
> **twice tried to close this item and was twice reversed** — recorded as a standing caution against this
> session's own reasoning.
>
> **`0` idempotency tests executed · `0` cross-module joins tested · `0 of 13,814` dedup keys ·
> `0` vetoes discharged.**

Next checkpoint: `PT-10 — Test Evidence Classification + Runtime Boundary`.

No Evidence = No Progress. Never Skip Gate. A test over that population returns clean and means nothing.
Boss remains the sole Final Approver.
