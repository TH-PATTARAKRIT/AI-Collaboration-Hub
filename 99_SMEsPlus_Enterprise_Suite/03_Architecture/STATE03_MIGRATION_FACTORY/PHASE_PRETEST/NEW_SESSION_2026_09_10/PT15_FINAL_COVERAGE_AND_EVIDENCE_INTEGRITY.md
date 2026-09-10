# PT-15 — FINAL COVERAGE AND EVIDENCE INTEGRITY

## `CP-PT-15 — FINAL INTEGRITY CLEAN, WITH TWO OWN-PACKAGE DEFECTS FIXED AND A RE-FREEZE`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]`
Branch: `architecture/account-phase-pretest-new-session-2026-09-10-001` · head consumed `83c76531`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **Every sweep below was EXECUTED. The command and its result are published, not the pattern.**

---

## 1. Result

| Sweep | Result |
|---|---|
| `S1` clean-room vendor tokens | **`0`** — instrument proven able to fire by **synthetic injection (`0 → 2`)** |
| `S2` prohibited verdict semantics | **`0`** |
| `S3` veto self-discharge language | **`0`** |
| `S4` disallowed status on a scenario row | **`0`** |
| `S5` duplicate identifiers | **`0`** |
| `S6` denominator integrity | consistent across the package |
| `S7` unresolved items with a named owner | **`19 of 19` finding rows** (was `16` — **`3` fixed**) |
| **`S8` checkpoint-title fidelity** | **`7` DEFECTS FOUND IN THIS PACKAGE — ALL FIXED** |
| `S9` evidence-pointer resolution | **`32 of 32`** |
| **Baseline drift since the `PT-14` freeze** | **`10` files — RE-FROZEN, §5** |

---

## 2. `PT15-D-01` — this package reproduced the exact defect it found in `G02`

### The defect

**`PT-08` §7 recorded `SA10-F-04`'s finding about SaaS gate `G02`:**

> *"ten rows read **verified**, while its own closing block reads `HOLD / CORRECTION REQUIRED` … **recorded
> as a status-fidelity hazard for any consumer.**"*

**Sweep `S8` found the same shape in this session's own package.** `7` checkpoints carried the master
prompt's **nominal** title in the `##` header and the **honest, qualified** verdict only in the closing
block:

| Checkpoint | Header said | Closing block said |
|---|---|---|
| `CP-PT-02` | `INPUTS COMPLETE OR BOUNDED` | **`INPUTS BOUNDED`** |
| `CP-PT-04` | **`OUTPUT HANDOFF COMPLETE`** | **`INCOMPLETE, BOUNDED`** |
| `CP-PT-05` | `ROUTING PROOF COMPLETE` | `COMPLETE, WITH THREE MATERIAL FINDINGS` |
| `CP-PT-06` | `CONVERGENCE COMPLETE` | **`MAPPED, NOT PROVEN`** |
| `CP-PT-08` | `SAAS BOUNDARIES TESTABLE` | **`TESTABLE, NOT TESTED`** |
| `CP-PT-09` | `FAILURE MODES COVERED` | **`COVERED, NONE PROVEN`** |
| `CP-PT-12` | `PRE-TEST MATRIX COMPLETE` | `PRESENT AND POINTED, NOT PROVEN` |

> **A reader scanning headers would have seen `COMPLETE` on four checkpoints whose evidence says the
> opposite.** `PT-04` even stated the principle — *"the title is not allowed to grade the evidence"* — and
> then **left the title standing**. **Stating a rule is not applying it.**

### Fixed

**All `7` headers now carry the honest verdict, with the master-prompt checkpoint name preserved
underneath so the required checkpoint remains traceable.** Re-run of `S8` confirms: **`0` headers now
claim more than their evidence.**

## 3. `PT15-D-02` — three OPEN findings had a disposition but no named owner

`S7` measured `20` `OPEN` rows in the ledger; **`16`** named an owner or route. The gap was **`3` finding
rows** (`PT02-F-01`, `PT07-F-03`, `PT08-F-01`) — each had a *disposition* but no *owner*.

> **The master prompt's `PT-15` requires *"all unresolved items have authorized owners."* A disposition is
> not an owner.** Fixed: **`19 of 19`** finding rows now name one. *(The 20th `OPEN` match is the
> single-writer risk line, not a finding row.)*

---

## 4. The executed sweeps

### `S1` — clean-room, with a synthetic injection control

**PATTERN:** declared literal ∪ derived prefixes — `odoo`, `stock.*`, `product.*`, `ir.*`, `res.*`,
`account.move`, `mrp.*`, `purchase.order`, `sale.order`, `orderpoint`, `picking`, `_action_*`, `sudo`,
`.py`, `l10n_`, `scgl_`, `smesplus_`.

| Run | Result |
|---|---:|
| Over `PT-00`…`PT-14` | **`0`** |
| **Synthetic injection — negative file** | **`0`** |
| **Synthetic injection — positive file** (`stock.quant`, `l10n_th`) | **`2`** |

> **The instrument moves `0 → 2`. The zero over the package is a measurement, not a silence.**

### `S2`–`S5`

`0` bare pass-verdicts · `0` veto-discharge assertions · `0` disallowed scenario statuses ·
`0` duplicate identifiers across `X-01`…`X-22`, `E2E-01`…`E2E-18`, `PT-S-01`…`-07`, `PTX-01`…`-11`.

### `S6` — denominator integrity

`0 of 22` (9 files) · `0/3` (7) · `0 of 2` (11) · `16 of 23` (2) · `9 of 16` (1) · `10 WRITABLE` (4) ·
`12 GATED` (4) · `58` (6). **No file states a different value for the same measure.**

### `S9` — evidence pointers

**`32` distinct git objects cited · `32` resolve · `0` unresolved** — including the two blob-pinned Boss
approvals (`a1fc7cd6`, `b4c39831`), the handoff-register blob (`7bb74dd1`), and the two Module-gate
remediation commits (`ea78e160`, `1d54c7e4`).

---

## 5. Re-freeze — the `PT-14` baseline moved and is restated

**`PT-14` froze the B-7 baseline at `37f7d006`. `PT-15`'s own fixes then modified `10` files in the frozen
path.**

| | |
|---|---|
| Files changed since the freeze | **`10`** — `PT-02`, `-04`, `-05`, `-06`, `-08`, `-09`, `-12`, `PT-14`, the resume state, the manifest |
| Nature of the changes | **`7` checkpoint-header corrections · `3` owner attributions · the manifest regeneration.** **`0` findings added, removed or re-graded; `0` counts changed** |
| Action | **RE-FROZEN.** `PRETEST_PACKAGE_MANIFEST_SHA256.txt` regenerated; the new baseline is **this commit** |

> **`PT-14`'s own rule is `… → CORRECT → RE-RUN → RE-FREEZE → RE-CHALLENGE`. It applies to corrections
> this session makes to itself, not only to B-7's.** A baseline that silently drifts after being declared
> frozen is not frozen — and B-7 would have been routed at a manifest that no longer matched the files.

---

## 6. Coverage — the master prompt's `PT-15` checklist, item by item

| Required check | Result |
|---|---|
| unique IDs | **`0` duplicates** |
| denominator integrity | consistent; **`3` inherited denominator defects recorded** (`PT00-F-01`, `PT04-F-01`, `PT07-F-01`) and **`1` own denominator move published** (`47 → 48`) |
| no orphan rows | **`1` found and fixed** (`PT13-D-01`) |
| all evidence pointers resolve | **`32 of 32`** |
| no hidden source-copying | **`0`**, injection-controlled |
| **no missing consumers** | **`4` missing consumers EXIST and are RECORDED** (`PT04-F-03`). The check is that they are named, not that they are absent |
| unresolved items have authorized owners | **`19 of 19`** after `PT15-D-02` |
| allowed status semantics | **`0`** violations; **`7` header violations fixed** (`PT15-D-01`) |
| no veto self-discharged | **`0`** — `6` in force, and the **`7th`'s membership routed as a question** |
| no `PTE-3`/`-4`/`-5` mislabelled | **`0`** |

---

## 7. What remains open at the close of `PT-15`

| Category | Count | Detail |
|---|---:|---|
| **Material findings open** | **`16`** | `PT00-F-01`/`-F-03`, `PT02-F-01`, `PT03-F-01`, `PT04-F-01`/`-02`/`-03`, `PT05-F-01`/`-02`/`-03`, `PT06-F-01`/`-02`, `PT07-F-01`/`-02`/`-03`, `PT08-F-01`/`-02`, `PT09-F-02`/`-03`, `PT10-F-01` |
| Findings withdrawn by their own author | **`1`** | `PT02-F-02` |
| Own-package defects found and fixed | **`3`** | `PT13-D-01`, `PT15-D-01`, `PT15-D-02` |
| Tolerance-zero | **`EC-04` `0/3`** | unchanged |
| Independence | **`EC-07` `0/2`** | B-7 not executed |
| Vetoes | **`6` in force, `0` discharged** | plus the `6`-or-`7` membership question |
| Boss decisions open | **`7`**, of which **`4` presentable** | |
| Scenarios runtime-verified | **`0 of 48`** | |

---

## 8. Checkpoint

> ## `CP-PT-15 — FINAL INTEGRITY CLEAN`
>
> **`9` sweeps executed with their commands and results published · clean-room `0` with a **synthetic
> injection control proving the predicate fires (`0 → 2`)** · `32 of 32` evidence pointers resolve ·
> `0` duplicate identifiers · `0` veto self-discharge · `0` mislabelled evidence classes ·
> **`2` further defects found in this session's OWN package and fixed: `PT15-D-01` — `7` checkpoint headers
> claimed `COMPLETE` where the evidence said otherwise, the exact status-fidelity hazard this package had
> already flagged in `G02`; and `PT15-D-02` — `3` OPEN findings carried a disposition but no owner** ·
> **the B-7 baseline drifted `10` files after being declared frozen and has been RE-FROZEN**, with the
> changes characterised as `0` findings added, removed or re-graded.
>
> **`16` material findings open · `EC-04` `0/3` · `EC-07` `0/2` · `6` vetoes · `0 of 48` verified.**

Next checkpoint: `PT-16 — Boss Functional-Design Entry Gate Pack`.

No Evidence = No Progress. Never Skip Gate. Stating a rule is not applying it.
Boss remains the sole Final Approver.
