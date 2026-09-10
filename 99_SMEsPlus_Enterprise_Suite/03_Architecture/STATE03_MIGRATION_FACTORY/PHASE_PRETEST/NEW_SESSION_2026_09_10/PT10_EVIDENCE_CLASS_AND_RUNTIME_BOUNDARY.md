# PT-10 — TEST EVIDENCE CLASSIFICATION AND RUNTIME BOUNDARY

## `CP-PT-10 — NO FAKE RUNTIME PROOF`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]`
Branch: `architecture/account-phase-pretest-new-session-2026-09-10-001` · head consumed `87d72f5e`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **`EC-04` enters at `0/3` and leaves at `0/3`. `0 of 22` verified in, `0 of 22` verified out.**
> **`0` runtime proof is claimed, simulated, inferred or implied anywhere in this package.**

---

## 1. Result

| | |
|---|---|
| **Material findings** | **`1`** — `PT10-F-01`, and it is the largest of the session |
| **`PT10-F-01` direction** | **IT MAKES THE PACKAGE LOOK BETTER, NOT WORSE** |
| Boss decisions ruled | **`16 of 23`** · still open **`7`** — validated three ways |
| `12 GATED` rows whose gating decision is **now RULED** | **at least `10 of 12`** |
| `13 B` cells whose gating decision is **now RULED** | **at least `9 of 13`** |
| Re-derivation performed by this session | **`0` — deliberately** |
| `EC-04` | **`0 of 3`** — unchanged |
| `EC-07` | **`0 of 2`** — unchanged; `B-7` appointment **does not itself create an independent pass** |
| `E2E-04` | **`NOT TRAVERSABLE`** — not re-graded |
| Rows mislabelled as passing | **`0`** |

---

## 2. `PT10-F-01` — MATERIAL: the readiness split is measured **before** the rulings that gate it

### The timeline, from commit metadata

| Artefact | Committed | Reports |
|---|---|---|
| `SA_CORR5_10` — the dimension register | **2026-09-09** | `10 WRITABLE` / `12 GATED` · `185 C` / `13 B` |
| **`SC-BD-05`** — `F1` ruled: **`JT-04` = physical movement · `JT-05` = original cost** | **2026-09-10 08:14** | `2 of 2` ruled |
| `SC-45` — routing/scenario re-run | **2026-09-10 11:03** | **still `10/12/0`** |
| `SC-59` — Pre-Test handoff | **2026-09-10 12:02** | **still `10/12/0`** |

**`SC-45` postdates the `F1` ruling by roughly three hours and carries the pre-ruling split unchanged.**

### What the rulings did to the gating decisions

**The `12 GATED` rows are gated on named decisions. Each was checked against `SC-11`'s recomputed
population (`16 of 23` ruled, validated three ways).**

| Rows | Gating decision | Status **now** | Ruled by |
|---|---|---|---|
| `1`–`6` | **`JT-04`** | **RULED** | `SC-BD-05` (`F1`, `2 of 2`) |
| `8`, `9` | **`JT-05`** | **RULED** | `SC-BD-05` |
| `10` | **`XD1-P1`** | **RULED** — `BLOCK`, all three members as one principle | `SC-BD-07` (`F2`, `3 of 3`) |
| `18` | **`XMC-D-02`** · **`XMC-D-01`** | **RULED** · **RULED** | `SC-BD-02` (`F4`) · `SC-BD-08` (`F3`) |
| **`16`, `17`** | **`B-6`** = restate `BLK-07`/`BLK-08` · **veto limb 2** · `POH-D-01`/`-02`/`-06` | **PARTLY RULED — STILL GATED.** `POH-D-06` ruled; **`POH-D-01` open · `POH-D-02` withheld · veto limb 2 outstanding** | `SC-BD-06` (`F5`, `1 of 6`) |

**`10 of the 12 GATED` rows now rest on decisions that are RULED. `2` (rows `16`, `17`) remain genuinely
gated.**

**On the `13 B` cells** — `AC` rows 1–6, 8, 9 (**8** cells, `JT-04`/`JT-05` → **ruled**) · `OUT` row 18
(**1** cell, `XMC-D-02` → **ruled**) · `AC` rows 16, 17 (**2** cells, **still gated**) · `AU` rows 5, 10
(**2** cells — row 10 is `XD1-P1`, **ruled**; **row 5's over-receipt tolerance default was NOT established
by this checkpoint** and is stated as unestablished rather than assumed).

> **At least `9 of 13` `B` cells and at least `10 of 12` `GATED` rows rest on decisions Boss has since made.**

### The propagation was never commissioned

`SC-11` §6 enumerates **`9` new obligations created by the rulings** — AAS+ concurrence on `POH-D-06`;
a SMEs Core recommendation on `RC-D-03`/`RC-D-04`; the `Average`-costing reversal residual;
re-wording veto limb 2; the per-boundary applicability declaration; per-company export; `M-1`…`M-6`;
**element 15 into Pre-Test exit criteria**; executing the four approved acts.

> **None of the nine is *"re-derive the 22-scenario dimension register against the rulings."***
> **The rulings were recorded, their downstream obligations were enumerated, and the register they
> unblock was not among them.** The split therefore travelled into the Pre-Test handoff **pre-ruling**.

### Why this session does NOT re-derive it

| Reason | |
|---|---|
| **1** | The carry-forward is explicit: ***"None of these values may be silently upgraded by entering Pre-Test."*** A `10/12 → 20/2` move made by the consuming session **is exactly that upgrade** |
| **2** | The `22`-scenario dimension register is a **Phase SA artefact**. This session may not rewrite Phase SA |
| **3** | A ruling being made is **not the same** as its consequence being specified. `SC-BD-05` fixes *which event recognises cost*; whether elements `4`/`7` are thereby **supplied** at the contract's three-conjunct standard (*known, traceable **and** evidence-backed*) is a separate question this checkpoint has **not** measured |
| **4** | **The direction of the error is the reason to be more careful, not less.** This is the one finding of the session that improves the picture, and it is the one most likely to be adopted without scrutiny |

### Disposition

| | |
|---|---|
| Status | **OPEN — MATERIAL** |
| Carried figures | **`10 WRITABLE` / `12 GATED` and `185 C` / `13 B` are carried UNCHANGED**, as reported |
| Recorded beside them | **the split is pre-ruling and at least `10 of 12` gates have since been ruled** |
| Owner of the re-derivation | **Phase SA / PMO**, on Boss authority |
| Routed to | **`PT-11`**, `PT-13`, **`PT-14` B-7 — flagged as the finding most likely to be accepted uncritically**, and `PT-16` as a **Boss decision input** |

---

## 3. Evidence classification — `PTE-1`…`PTE-5`

**Rule: exactly one primary class per row; secondary tags allowed; the primary must be unambiguous.**

| Class | What it covers here | Count |
|---|---|---:|
| **`PTE-1` STATIC / SEMANTIC** | claims provable from approved evidence **today**: that the 16-element contract is `BOSS APPROVED / EFFECTIVE`; that `16 of 23` decisions are ruled; that `BN` status is `1/17/0`; that `HX-01`…`HX-31` exists | **the register facts only — `0` scenario rows** |
| **`PTE-2` REFERENCE / EXPERIMENT** | bounded, non-authoritative measurements of the reference estate: direct-shipment installed **`0 of 3`** deployments · dedup carrier populated on **`0 of 13,814`** rows · inter-company path traced at data level (`1,201` out-legs / `1,201` in-legs) · the two lock-defeat paths as **source capability** | **`4` measurements** |
| **`PTE-3` EXECUTION-DESIGN READY** | every scenario row; all `11` `SA17` controls; `PTX-01`…`PTX-11`; the `8` runtime-obligation families; `0 of 58` invariants; `0 of 18` contracts | **the bulk** |
| **`PTE-4` EXTERNAL AUTHORITY** | **AAS+**: `POH-D-06` concurrence, **limb-2 re-wording**, `AAS-V-02` discharge act · **Thai statutory `4`**: `TH-NEW-01`, `TH-NEW-02`, `POH-D-02` tax consequences, over-absorption cap strength · **Business SME `2`**: `SME-Q-02`, `SME-Q-03` · **PMO**: `GAP-KC-01` | **`10`** |
| **`PTE-5` BOSS AUTHORITY** | the **`7`** open decisions — `RC-D-03`, `RC-D-04`, `POH-D-01`, `POH-D-03`, `POH-D-04`, `POH-D-05` **ready and held**; **`POH-D-02` withheld** | **`7`** |

### 3.1 Two classification rulings this checkpoint had to make

**`POH-D-02` is `PTE-4`, not `PTE-5`.** It is nominally a Boss election, but it is **withheld pending Thai
statutory evidence** — Boss **cannot** be asked until the external input exists. **The primary class is the
one that blocks first.** Classifying it `PTE-5` would put it on the Boss list when no Boss act can move it.

**`RC-D-03` / `RC-D-04` are `PTE-5` but NOT YET PRESENTABLE.** `SC-BD-F-01` found that the `F6` card put
four members to Boss under a recommendation covering **two** — *"presenting the family-level recommendation
as covering all four would have put a SMEs Core position in Boss's mouth."* **`SC-11` §6 obligation 2
requires a SMEs Core recommendation on both before either is re-put.** **They are Boss's to decide and not
yet Boss's to be asked.**

---

## 4. Runtime boundary — reconciled explicitly, as `PT-10` requires

| Carry-forward obligation | State on entry | **State on exit** | Moved? |
|---|---|---|:--:|
| **`EC-04`** tolerance-zero | **`0 of 3`** | **`0 of 3`** | **NO** |
| **`EC-07`** independent passes | **`0 of 2`** | **`0 of 2`** | **NO** |
| `22` scenarios runtime-verified | **`0 of 22`** | **`0 of 22`** | **NO** |
| `58` invariants proven | `0 of 58` | `0 of 58` | **NO** |
| `18` contracts proven | `0 of 18` | `0 of 18` | **NO** |
| `8` isolation proofs | `0 of 8` | `0 of 8` | **NO** |
| `60` negative cases | `0 of 60` | `0 of 60` | **NO** |
| **`E2E-04`** | **`NOT TRAVERSABLE`** | **`NOT TRAVERSABLE`** | **NO** |
| `6` vetoes | `6` in force · `0` discharged | `6` in force · `0` discharged | **NO** |

**`EC-04`'s closure standard, restated unweakened:** **executed runtime proof + independent reproduction,
no later than the State 8-Criteria Exit Gate.** **Specification evidence NEVER satisfies `EC-04`**
(`8C-CLARIFICATION-01` clause 3). **`CONDITIONAL PASS` may never bypass a tolerance-zero residual.**

**`EC-07`, stated precisely:** `B-7` is **approved as an act** (`SC-BD-10`) — and *"`B-7`'s appointment
does not itself create an independent pass; structurally independent passes remain **`0`**."*

---

## 5. The anti-fabrication sweep over this session's own package

| Test | Result |
|---|---:|
| Rows claiming executed runtime proof | **`0`** |
| `PTE-3`/`-4`/`-5` rows labelled as passing | **`0`** |
| Reference-system behaviour used as SMEsPlus design authority | **`0`** — the `0 of 3` dropship and `0 of 13,814` dedup measurements are published as `PTE-2` **and neither was used to decide anything** |
| Tolerance-zero boundaries reclassified | **`0`** |
| Vetoes discharged or narrowed | **`0`** |
| Scenario grades changed | **`0`** |
| Ruled denominators re-scoped | **`0`** |
| **Values silently upgraded** | **`0`** — including the one upgrade the evidence would have supported (§2) |

---

## 6. Checkpoint

> ## `CP-PT-10 — NO FAKE RUNTIME PROOF`
>
> **`PT10-F-01` MATERIAL — the `10 WRITABLE / 12 GATED` split and the `13 B` cells were measured on
> 2026-09-09 and the decisions that gate them were ruled on 2026-09-10. **At least `10 of 12` gated rows
> and at least `9 of 13` `B` cells now rest on RULED decisions.** `SC-45` carries the pre-ruling split
> three hours after the ruling; `SC-11` enumerates `9` downstream obligations and **re-deriving the
> register is not one of them.** **This session carries the reported figures UNCHANGED and does not
> re-derive** — because the carry-forward forbids silent upgrades, because the register is Phase SA's,
> because a ruling is not the same as its consequence being specified, and **because this is the one
> finding that improves the picture and is therefore the one most likely to be accepted without
> scrutiny.** Routed to Boss as a decision input, and flagged to B-7 for exactly that reason** ·
> `PTE-1`…`PTE-5` assigned with one primary class each; **`POH-D-02` classified `PTE-4` not `PTE-5`
> because no Boss act can move it**; `RC-D-03`/`RC-D-04` are Boss's to decide and **not yet Boss's to be
> asked** ·
> **`EC-04` `0/3` in, `0/3` out · `EC-07` `0/2` in, `0/2` out · `0 of 22` in, `0 of 22` out ·
> `E2E-04 NOT TRAVERSABLE` · `6` vetoes · `0` values upgraded, including the one the evidence supported.**

Next checkpoint: `PT-11 — Boss / External / Veto Dependency Reconciliation`.

No Evidence = No Progress. Never Skip Gate. Truth over Pass. Specification evidence NEVER satisfies EC-04.
Boss remains the sole Final Approver.
