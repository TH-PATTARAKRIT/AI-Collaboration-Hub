# 10 — PRE-TEST FUNCTIONAL-DESIGN BLOCKER REGISTER · `CORR2`

# `11 BLOCKERS · FUNCTIONAL DESIGN CANNOT BEGIN`

## `CHECKPOINT L`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Baseline: `c91d5840` · Boss: **SOLE FINAL APPROVER**

> **`§22` forbids inheriting `5`. It was not inherited, and neither was `3`.** The register is rebuilt by
> enumerating every **missing business semantic** a Functional Designer would have to invent.

---

## 1. THE PUBLISHED FIGURES, AND WHY BOTH ARE WRONG

| Source | States | Measured |
|---|---:|---|
| `10_` §1 table | **`3`** | its **own §2** lists `3` **"plus `2` new material items this recovery surfaced"** = **`5`** |
| resume state L73 | **`3 → 5`** | the recovery's own result |
| resume state L89 | **`3` (was `5`)** | a **stale post-`CORR1` line**, never marked superseded |
| `14_`, `15_`, `17_` | `5` | consistent with `10_` §2 |
| **this register** | — | **`11`** |

**`10_` §1 and `10_` §2 contradict each other inside one file** (`R2-F-14`). **`5` was the recovery's
honest figure; `3` is a transcription of a superseded line.**

---

## 2. `CORR2-FD-01` — MATERIAL · THREE OPEN OBLIGATIONS DROPPED AND ONE IDENTIFIER RE-USED

**Found in this session. Neither B-7 round detected it.**

`35_` §3 is `CORR1`'s closing SMEs Core obligation register. Measured against the recovery package:

```
POPULATION : the obligation identifiers open or blocked at 35_ §3 / 33_ §
UNIT       : identifier
PATTERN    : grep -rl <id> RECOVERY_2026_09_10/   vs   grep -rl <id> CORRECTIVE_CLOSURE_2026_09_10/
PATH SET   : NEW_SESSION_2026_09_10/**  at c91d5840

id            CORRECTIVE_CLOSURE   RECOVERY     status at 35_/33_
CORR1-F-02          5 files          0 files     OPEN   "FIFO layer gap"
CORR1-F-03          5 files          0 files     OPEN   "MF-01/MF-02 idempotency exposure on re-run"
CORE-03             3 files          0 files     CANNOT START — blocked on AAS+ issuer authority
POSITIVE CONTROL — CORE-06           6 files      5 files     (carried; the instrument fires)
```

| Dropped | What it was | Where it went |
|---|---|---|
| **`CORR1-F-02`** | *"`HX-24` supplies an **aggregate** where `FIFO` requires **ordered layers**"* — routed to `CORE-07` | **`0` occurrences in the recovery.** The substance survives only as a valuation-method remark in `06_` §1 (*"FIFO requires layers with costs … must be supplied"*), **with no obligation, no owner and no status** |
| **`CORR1-F-03`** | *"`MF-01`/`MF-02` admitted to `IR`/`AR` while the **idempotency of their execution is unbuilt**; **a re-run can duplicate an opening balance**"* — routed to `X-22` / element `15` | **`0` occurrences in the recovery** |
| **`CORE-03`** | limb-`2` re-wording — **`CANNOT START`**, blocked on AAS+ issuer authority (`X-02`) | **`0` occurrences in the recovery** |

**And the identifier collision:**

| Round | `CORE-07` means | Cited at |
|---|---|---|
| **`CORR1`** | *"**`HX-24` payload must carry `FIFO` layer granularity** (`CORR1-F-02`)"* | `35_` L80 · `33_` L44 · `32_` L178 · `29_` L80, L149 |
| **RECOVERY** | *"analyse `XMC-H-13`/`-14`/`-17`/`-18` **before any `B4′` amendment**"* | `14_` L117 · `15_` L60, L76 |
| RECOVERY's own label for it | ***"`-07` new"*** (`12_` L47) | — |

> **One identifier, two unrelated obligations, one commit apart — and the second is announced as *new*
> while the first is still open.**

**Why this is material and not clerical:** `CORR1-F-03` is **exactly** the element-`15` idempotency
dependency that `07_` re-derives. **The obligation that would have carried that dependency forward was
dropped in the same package in which `06_` re-grounded `MF-03` on element `14`.** The drop and the
mis-grounding are the same failure seen twice.

**Consequence for the Round-2 finding set:** `R2-F-11` reports *"`CORE-07` — which Boss made a
precondition to any `B4′` amendment — is scoped to `4`"*. **That is the recovery's `CORE-07`.** The
challenger inherited the re-used identifier without noticing the collision. **The observation stands; its
identifier does not.**

---

## 3. THE ELEVEN BLOCKERS

| # | Blocker | Missing business semantic | Affected function | Dimension | Cov. | Floor | Crit. | Evidence | Downstream consequence | SMEs Core | Arch. | External | **Boss** | Status |
|---:|---|---|---|---|---:|---:|:--:|---|---|:--:|:--:|:--:|:--:|---|
| **`1`** | `2` outputs + `1` orphan input `D ORPHAN` | who consumes the remaining-supply record; the `XMC-H-09` **Asset → Equipment** route; the customer-invoice lifecycle state | output contracts | Source | `—` | `96 %` | **Y** | `10_` §2 #1; `B10′` `3 → 2` | a designer must invent a consumer | **Y** | Y | — | — | **OPEN** |
| **`2`** | **`O-1`** corrected-entry link does not exist | how a correction references what it corrects | correction / reversal | Source | `—` | `96 %` | **Y** | `10_` §2 #2 | correction semantics invented per screen | **Y** | — | — | — | **OPEN** |
| **`3`** | **`O-3`** reversal after downstream consumption unrepresented | what happens when a consumed fact is reversed | reversal | Source | `—` | `96 %` | **Y** | `10_` §2 #3 | undefined behaviour at the most audit-sensitive point | **Y** | — | — | — | **OPEN** |
| **`4`** | Gap-carrying flows outside the declared boundary set | whether `XMC-H-13`/`-14`/`-17`/`-18` **+ `Purchase → Inventory`** are in scope | boundary contracts | Source | **`91.7 %`** | `96 %` | **Y** | `06_`; `B7-F-07` | **floor `5`, up to `7`** (`§4` of `06_`) — designers cannot know their own scope | **Y** | Y | — | **Y** | **OPEN — widened** |
| **`5`** | **`B4′` × `B9′`** tension | `B9′` admits `MF-01`/`MF-02` onto `XMC-H-18`, which `B4′` **excludes** | migration flows | Source | `—` | `96 %` | **Y** | `B7-F-08`; `31_` row `16` | flows admitted to a boundary outside the contract denominator | — | Y | — | **Y** | **OPEN** |
| **`6`** | **NEW** — declared class `12` covered by no contract row | how period close reaches the subledgers; **there is no accounting-period object**, and the accounting date is *"silently movable past a lock"* | period close | Source | **`0 %`** | `96 %` | **Y** | `06_` §6; `SA_CORR3_08` `XMC-H-12` | **close cannot be designed** — no object to close | **Y** | Y | — | **Y** | **OPEN** |
| **`7`** | **NEW** — flow population not established | `MF-03` **`NOT DECIDABLE`**; `IR 20` / `AR 30` memberships **unsupported** (max `6` / `10` enumerated) | material-flow register | Source | **`30 %` / `33 %`** | `96 %` | **Y** | `07_` §5, §6; `08_` rows `9`–`12` | designers cannot enumerate the flows they must design | **Y** | Y | — | — | **OPEN** |
| **`8`** | **RESTORED** — **`CORR1-F-02`** `FIFO` layer granularity | `HX-24` carries *"quantity and value"* as an **aggregate**; `FIFO` needs **ordered layers**, and an aggregate is not reducible to layers | migration valuation | Source | `—` | `96 %` | **Y** | `29_` §3; `33_` L44 | a `FIFO`-costed category **cannot be migrated correctly** | **Y** | — | — | — | **OPEN — was dropped** |
| **`9`** | **RESTORED** — **`CORR1-F-03`** idempotency exposure | *"a **re-run can duplicate an opening balance**"*; element `15` unbuilt | migration replay | Source + **Runtime** | **`0 %`** | `96 %` | **Y** | `35_` L81; `07_` §3 | **duplicate opening balances** — an accounting-integrity exposure | **Y** | — | — | — | **OPEN — was dropped** |
| **`10`** | **RESTORED** — **`CORE-03`** limb-`2` re-wording | the veto's second limb wording | veto / `AAS-V-02` | Governance | `—` | `100 %` | **Y** | `35_` L76; `36_` `X-02` | **`CANNOT START`** — needs the AAS+ issuer, who has produced `0` records | — | — | **Y** | — | **BLOCKED — was dropped** |
| **`11`** | **`SC-SMT-01`** return-reversal residual | the reconciliation control for the `Average`-costing original-cost reversal residual | sales / purchase return | Source | `—` | `96 %` | **Y** | `SC-BD-05` §8.1; `27_` `C-08-AC` | *"a return-reversal case for an `Average`-costed category **cannot state its expected accounting result**"* — **gates `X-08` and `X-09`** | — | — | — | **Y** | **OPEN — Boss** |

```
TOTAL BLOCKERS                            11
  carried from the recovery's own list      5   (1, 2, 3, 4, 5)
  new in this session                       2   (6, 7)
  restored after being dropped              3   (8, 9, 10)
  open Boss-owned, blocking FD              1   (11)
  CHECK  5 + 2 + 3 + 1                     11   OK
OWNERSHIP  SMEs Core 7 · Architecture 5 · External 1 · Boss 4   (a blocker may have more than one owner)
```

---

## 4. THE CONTROLLING QUESTION

> ## **CAN FUNCTIONAL DESIGN BEGIN WITHOUT INVENTING MISSING BUSINESS SEMANTICS?**
>
> # `NO`

**A designer starting today would have to invent, at minimum:**

1. a **consumer** for `2` orphan outputs and an **origin** for `1` orphan input;
2. how a **correction references what it corrects**;
3. what happens when a **consumed fact is reversed**;
4. **which boundaries are in scope** — `12`, `16`, or `17`;
5. how **period close** reaches the subledgers **when no period object exists**;
6. **which material flows exist** — `IR` and `AR` memberships are unpublished;
7. how a **`FIFO` opening balance carries layers** when the payload is an aggregate;
8. what happens when a **migration is re-run** and no idempotency identity exists;
9. the **expected accounting result of a return reversal** under `Average` costing.

**Nine inventions. Each is a business semantic, not a design choice.** `§10` item `8` forbids handoff
while any remains.

---

## 5. REQUIRED CORRECTION

1. **Restore `CORR1-F-02`, `CORR1-F-03` and `CORE-03`** to the obligation register with their original wording and `OPEN` status.
2. **Resolve the `CORE-07` collision.** The recovery's boundary-analysis obligation is renamed **`CORE-08`**; `CORE-07` reverts to the `FIFO` layer gap. **Rename yours; attribute what you inherited.**
3. **A successor package must reconcile its predecessor's open obligation list, identifier by identifier.**
4. **Pre-commit sweep unit (a):** every identifier open in the predecessor appears in the successor with an explicit disposition. **Run at `c91d5840`, it fails on `3` identifiers.**
5. **Pre-commit sweep unit (b):** no identifier is defined twice with different content. **Run at `c91d5840`, it fails on `CORE-07`.**

---

## 6. CHECKPOINT

> ## `CHECKPOINT L — FD BLOCKERS RECOMPUTED`
>
> **`11` blockers** — `5` carried · `2` new · **`3` restored after being silently dropped** · `1` Boss-owned ·
> **`CORR2-FD-01`: `3` open obligations dropped and the identifier `CORE-07` re-used for a different
> obligation between `CORR1` and the recovery — undetected by both B-7 rounds** ·
> the dropped `CORR1-F-03` is the same element-`15` dependency `06_` mis-grounded ·
> **`9` business semantics a designer would have to invent** ·
> **FUNCTIONAL DESIGN NOT AUTHORIZED.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the sole Final Approver.**
