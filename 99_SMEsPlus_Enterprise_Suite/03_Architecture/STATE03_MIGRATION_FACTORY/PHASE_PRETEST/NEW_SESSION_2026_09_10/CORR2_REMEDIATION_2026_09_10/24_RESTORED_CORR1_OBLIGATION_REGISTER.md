# 24 — RESTORED `CORR1` OBLIGATION REGISTER

# `3 RESTORED · 1 IDENTIFIER COLLISION RESOLVED · 0 CLOSED BY RESTORATION`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Authority: **`17_` §3** — *"`CORE-03`: RESTORE and preserve"* · *"the boundary obligation formerly
re-using `CORE-07` shall henceforth be `CORE-08`. **Do not overwrite the original `CORR1` `CORE-07`
identity**"* · Boss: **SOLE FINAL APPROVER**

> **Restoration is not closure.** All three obligations return **OPEN or BLOCKED**, in their original
> wording, with their original owners. **`0` are closed by being restored.**

---

## 1. HOW THEY DISAPPEARED — the measurement

```
POPULATION : obligation identifiers open or blocked at 35_ SS3 and 33_ (the CORR1 closing registers)
UNIT       : identifier
PATTERN    : grep -rl <id> RECOVERY_2026_09_10/   vs   CORRECTIVE_CLOSURE_2026_09_10/
PATH SET   : NEW_SESSION_2026_09_10/**  at c91d5840

id            CORRECTIVE_CLOSURE   RECOVERY    status at 35_ / 33_
CORR1-F-02          5 files          0 files    OPEN
CORR1-F-03          5 files          0 files    OPEN
CORE-03             3 files          0 files    CANNOT START
POSITIVE CONTROL
CORE-06             6 files          5 files    carried  -> the instrument fires
```

**Mechanism:** the recovery package rebuilt the obligation set from `22_`'s post-ruling state rather
than from `CORR1`'s closing state. **`CORR1`'s two new findings and one blocked obligation had no
predecessor in `22_`, so nothing carried them forward.** No act removed them; **an omission did.**

**Why no control caught it:** every integrity control in the package measures the package's **own**
membership. **None compares a successor's open list against its predecessor's.** That check is added at
`§5`.

---

## 2. THE RESTORATIONS

### `CORR1-F-02` — `FIFO` layer granularity

| Field | Entry |
|---|---|
| **Original requirement** | *"**`FIFO` layer gap** — `HX-24` supplies an **aggregate** where `FIFO` requires **ordered layers**"* (`33_` L44) · *"`HX-24` payload must carry `FIFO` layer granularity"* (`35_` L80) |
| **Latest controlling authority** | `29_PRETEST_MF01_VALUATION_AND_COUNTERPART_CORR1.md` §3: *"`FIFO` is **layer-ordered**: value is carried as an ordered set of `(quantity, unit cost, acquisition sequence)` layers … **`HX-24` carries `quantity` and `value` as an AGGREGATE.** An aggregate cannot reconstruct layers: **infinitely many layer sets share one total**"* |
| **Why it disappeared** | its routing identifier `CORE-07` was **re-used** by the recovery for a different obligation (§3); the finding identifier itself was never carried |
| **Current owner** | **SMEs Core → Functional Design** |
| **Current phase** | **`S` — semantic.** The payload definition is specifiable now |
| **Closure evidence required** | an `HX-24` payload carrying `(quantity, unit cost, acquisition sequence)` per layer, **or** a Boss/SMEs-Core determination that `FIFO`-costed categories are out of migration scope |
| **Downstream evidence contract** | Build/Test: migrate a `FIFO`-costed product and reconcile issue costs against the layer sequence |
| **Status** | **OPEN — RESTORED** · **FD blocker `8`** (`29_`) |
| **Identifier** | routed to **`CORE-07`**, which reverts to this obligation per `17_` §3 |

### `CORR1-F-03` — `MF-01` / `MF-02` idempotency exposure on re-run

| Field | Entry |
|---|---|
| **Original requirement** | *"`MF-01`/`MF-02` admitted to `IR`/`AR` while the **idempotency of their execution is unbuilt**; **a re-run can duplicate an opening balance**"* (`35_` L81) — routed to `X-22` / element `15` |
| **Latest controlling authority** | `SA_CORR3_08` L177: element `15` `WHICH Idempotency Identity` — **`ABSENT`** · L230: *"`14` and `15` **`NOT SUPPLIABLE`**"* · `X-22`: *"this scenario **is** element `15`"* |
| **Why it disappeared** | `06_` re-grounded `MF-03` on element `14` and did not carry the element-`15` obligation forward |
| **Current owner** | **SMEs Core → Functional Design** |
| **Current phase** | **`S` for the identity semantic · `I` for the proof.** **The semantic is specifiable now; only the proof is downstream** |
| **Closure evidence required** | a specified **idempotency identity** — what makes two executions the same execution — then a Build/Test proof that a re-run adds `0` quantity and `0` value |
| **Downstream evidence contract** | Build/Test: run a migration batch twice; opening quantity and value must be identical after the second run, and the second run must be **recorded**, not silent |
| **Status** | **OPEN — RESTORED** |
| **Consequence of its absence** | **it is the exact semantic `MF-03`'s classification turns on** (`25_`). **The obligation that would have carried element `15` forward was dropped in the same package in which `06_` re-grounded `MF-03` on element `14`.** One omission, surfacing twice |

> **`CORR2-RST-01` — MATERIAL.** *"A re-run can duplicate an opening balance"* is an **accounting-integrity
> exposure**, not a technical nicety. **It was deleted from the register rather than deferred**, and
> `§14` of the ruling is explicit: *"`CORR1-F-03` idempotency must NOT disappear merely because runtime
> execution is downstream. **The obligation must survive phase transfer.**"*

### `CORE-03` — veto limb-`2` re-wording

| Field | Entry |
|---|---|
| **Original requirement** | limb-`2` re-wording of the veto — `35_` L76 |
| **Latest controlling authority** | `36_` external item **`X-02`** — AAS+ issuer authority |
| **Why it disappeared** | carried as `CANNOT START` in `CORR1`; the recovery's obligation set had no `CANNOT START` class |
| **Current owner** | **AAS+ issuer — EXTERNAL** |
| **Current phase** | **`G` — governance** |
| **Closure evidence required** | an **AAS+-authored** record. `0` exist: `3` instrument shapes + a firing synthetic injection return **`0` AAS+-authored records** across `779` files |
| **Downstream evidence contract** | none creatable below the issuer. **`AAS-V-02` remains NOT DISCHARGED; vetoes `7` · `0` discharged** |
| **Status** | **BLOCKED — RESTORED.** **`CANNOT START`** — this is an external blocker, not an SMEs Core gap |
| **Why it must be counted** | an obligation blocked on an external body **still occupies the denominator**. Dropping it made the external dependency invisible |

---

## 3. THE `CORE-07` IDENTIFIER COLLISION — RESOLVED AS RULED

| Round | `CORE-07` meant | Cited at |
|---|---|---|
| **`CORR1`** | *"`HX-24` payload must carry `FIFO` layer granularity (`CORR1-F-02`)"* | `35_` L80 · `33_` L44 · `32_` L178 · `29_` L80, L149 |
| **RECOVERY** | *"analyse `XMC-H-13`/`-14`/`-17`/`-18` **before any `B4′` amendment**"* | `14_` L117 · `15_` L60, L76 — and labelled ***"`-07` new"*** at `12_` L47 |

**Resolution, per `17_` §3:**

| Identifier | Now means | Status |
|---|---|---|
| **`CORE-07`** | **`CORR1`'s original** — `HX-24` `FIFO` layer granularity (`CORR1-F-02`) | **OPEN — RESTORED** |
| **`CORE-08`** | the boundary-analysis obligation formerly re-using `CORE-07` | **DISCHARGED as a mapping act** (`21_` §3) |

**Applied rule — *rename yours, attribute what you inherited*:** the **later** obligation is renamed,
because the earlier identifier has lineage in `5` files. **`0` prior artefacts are modified**; this
register governs the resolution forward.

**Citations inherited by others:** `R2-F-11` (`d878a603`) refers to *"`CORE-07` — which Boss made a
precondition to any `B4′` amendment"*. **That is `CORE-08`.** The challenger inherited the re-used
identifier without detecting the collision. **The observation stands; its identifier is corrected here**
rather than in the challenger's file, which remains audit lineage.

---

## 4. THE FULL SMEs CORE OBLIGATION SET, RECONCILED

**`10_`'s count of `4` had three different memberships across the package (`08_` row `21`). Settled:**

| ID | Obligation | Status | Owner |
|---|---|---|---|
| `CORE-01` | `RC-D-03`/`-04` recommendations | **DISCHARGED** before `CORR1` | SMEs Core |
| `CORE-02` | migration-class flow rows | **DISCHARGED** — admitted by `B9′` | SMEs Core |
| **`CORE-03`** | veto limb-`2` re-wording | **BLOCKED — RESTORED** | **AAS+ issuer, EXTERNAL** |
| `CORE-04` | map `12 ↔ 18 ↔ 10` | **DISCHARGED as a mapping**; superseded by `CORE-08` on the `17` | SMEs Core |
| `CORE-05` | deterministic refusal rule | **SPECIFIED** (`32A_`); build obligation passes to FD | SMEs Core |
| `CORE-06` | `MF-01` counterpart account | **DISCHARGED at architecture level** (`29_` §6); `2` residuals routed to configuration and statutory | SMEs Core |
| **`CORE-07`** | **`HX-24` `FIFO` layer granularity** | **OPEN — RESTORED** | SMEs Core → FD |
| **`CORE-08`** | `17 ↔ 18 ↔ 10` mapping | **DISCHARGED as a mapping act** (`21_` §3) | SMEs Core |
| **`CORR1-F-03`** | `MF-01`/`MF-02` idempotency on re-run | **OPEN — RESTORED** | SMEs Core → FD |

```
TOTAL OBLIGATIONS          9
DISCHARGED                 5    CORE-01, -02, -04, -06, -08
SPECIFIED                  1    CORE-05
OPEN                       2    CORE-07, CORR1-F-03
BLOCKED (external)         1    CORE-03
CHECK  5 + 1 + 2 + 1       9    OK
```

**Membership named once, in one place. The `3` competing memberships of `10_` row `21` are superseded.**

---

## 5. REQUIRED CONTROL — added because none existed

**Pre-commit sweep unit `1c` — predecessor reconciliation.**

> **Every identifier `OPEN`, `BLOCKED` or `CANNOT START` in the predecessor package must appear in the
> successor with an explicit disposition.**

```
Run at c91d5840 (recovery vs CORR1)  : FAILS on 3 identifiers
Run on THIS package (CORR2+ vs CORR1): CORR1-F-02 -> CORE-07 OPEN
                                       CORR1-F-03 -> OPEN
                                       CORE-03    -> BLOCKED
                                       0 unreconciled
```

**Pre-commit sweep unit `1d` — identifier redefinition.**

> **No identifier may be defined twice with different content.**

```
Run at c91d5840 : FAILS on CORE-07
Run on THIS package : CORE-07 = FIFO layer granularity (one definition, SS2)
                      CORE-08 = boundary mapping (one definition, SS3)
                      0 redefinitions
```

---

## 6. CHECKPOINT

> **`3` obligations **RESTORED** — `CORE-07` (was `CORR1-F-02`) **OPEN** · `CORR1-F-03` **OPEN** ·
> `CORE-03` **BLOCKED, external** · **`0` closed by restoration** ·
> `CORE-07` / `CORE-08` collision **resolved as ruled**, later obligation renamed, `0` prior files
> modified · full SMEs Core set reconciled to **`9`, one membership, `5` discharged · `1` specified ·
> `2` open · `1` blocked** ✔ · **`2` new pre-commit sweep units added**, both failing at `c91d5840` and
> clean here · **`CORR2-RST-01`: an accounting-integrity exposure was deleted rather than deferred.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the SOLE FINAL APPROVER.**
