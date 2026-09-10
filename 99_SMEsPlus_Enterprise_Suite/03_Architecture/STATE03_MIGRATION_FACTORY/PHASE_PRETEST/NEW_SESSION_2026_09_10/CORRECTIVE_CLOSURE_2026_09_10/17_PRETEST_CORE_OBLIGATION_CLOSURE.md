# 17 — SMEs CORE OBLIGATION CLOSURE

## `CHECKPOINT B — 3 OBLIGATIONS PROCESSED · 0 REMAIN OPEN TO SMEs CORE`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-BOSS-RESOLUTION-001]`
Parent: `[SMEPLUS-26-09-10-PHASE-PRETEST-CORRECTIVE-CLOSURE-001]`
Branch head consumed: **`c9ed125a`** · Boss: **SOLE FINAL APPROVER**

> **`CORE-01` was ALREADY DISCHARGED before this round began — and this package said it was open.
> That correction is published first, because it changes the Boss decision set.**

---

## 1. `CORE-01` — **ALREADY DISCHARGED · AND THIS PACKAGE WAS WRONG ABOUT IT**

### 1.1 The correction

| | |
|---|---|
| What `PT-11` §2.1 claimed | `RC-D-03`/`RC-D-04` are **NOT presentable** — *"SMEs Core owes a recommendation first"* |
| What `13_` carried | the same |
| **What primary text says** | **`SC-14` (`RC-D-03`) and `SC-15` (`RC-D-04`) ARE those recommendations**, and `SC-16` is their specialist challenge |
| **Timing** | `SC-11` created the obligation at **`89ba9c7d`, 09-10 08:14**. `SC-14`/`-15`/`-16` were published at **`dfea73b7`, 09-10 08:37** — **23 minutes later** |
| **`SC-44` §2, verbatim** | **`SMEs Core-closable \| 0 \| "RC-D-03/RC-D-04 were closed at SC-14/SC-15; nothing else remains"`** |
| **`SC-44` §2, verbatim** | **`Genuine Boss election — open, ready \| 6 \| RC-D-03, RC-D-04, POH-D-01, POH-D-03, POH-D-04, POH-D-05`** |
| **`SC-59` §7** | **`6` ready and held** — including both |

### 1.2 How the error was made — and it is a regression, not an oversight

> **`PT-00` §4 read `SC-59` §7 CORRECTLY and recorded *"`7` open, of which `6` ready and held."***
> **`PT-11` then changed that to *"only `4` presentable"* on the strength of `SC-11` §6's obligation list —
> an artefact `23` minutes older than its own discharge.**

**This package therefore contradicted itself:** `PT-00` said `6` ready; `PT-11`, `13_` and `16_` said `4`.
**The later statement was the wrong one.** Defect class: **superseded-source citation — third instance**
(after `PT02-F-02` CORR4/CORR5 and `PT05-F-01`). The prior two were caught by following a pointer; this
one was caught only because §3 of this prompt ordered supersession resolved **first**.

### 1.3 The recommendations, as they stand

| Decision | Subject | SMEs Core recommendation |
|---|---|---|
| **`RC-D-03`** | **Private Company escalation criteria** — what objectively qualifies a tenant to leave the `SHARED SaaS POOL` | **MODEL (a) — OBJECTIVE-THRESHOLD**, with the §5 `NEVER` list binding, authored as a **pool-exit condition only**. Four trigger classes as the **closed** v1 set: regulatory mandate for physical isolation · data-residency obligation · unmeetable security/attestation obligation · unmeetable quantified performance/SLA class. **Each externally attributable — to a regulator, a contract or a measured pool limit — never to a preference** |
| **`RC-D-04`** | **Mapping-layer ownership** — the cross-company read mapping/provenance layer `XCR-02` would require (`CF-XCR-GAP-01`) | **MODEL (a) — SPLIT OWNERSHIP, PRE-ASSIGNED NOW, LAYER DORMANT IN v1.** Rule ownership now even though the grant is declined, so a future grant cannot create an unowned layer. **Explicitly NOT the 12-boundary handoff contract and NOT a migration mapping** — widening it would be scope creep into ruled decisions |

| | |
|---|---|
| **`CORE-01` status** | **DISCHARGED — before this round, at `SC-14`/`SC-15`, challenged at `SC-16`** |
| **Consequence** | **`B1` covers `6` decisions, not `4`** |
| **Work owed by SMEs Core** | **`0`** |

---

## 2. `CORE-02` — migration-class flow rows **PRODUCED** (proposed, not admitted)

**Authority basis:** `HX-23`/`-24`/`-25` (`10_INVENTORY_CROSS_MODULE_HANDOFF_V1`, blob `7bb74dd1`,
status *"SMEsPlus-OWNED HANDOFF DESIGN — BUSINESS FACTS ONLY — CLOSES NO JOINT OR ACCOUNTING DECISION"*),
element `14`, `RT-E15-05`, `X-20`, `X-21`, `XMC-C-A17` provenance-reference semantics, `MTI-42`.

| Field | **`MF-01`** | **`MF-02`** | **`MF-03`** |
|---|---|---|---|
| **Flow** | **Certified opening balance** | **Historical movement history** | **Migration replay / re-run** |
| Business purpose | establish stock and value at cutover | establish auditable history before cutover | recover or re-run a migration batch |
| Source state | legacy system, certified extract | legacy movement history | a prior migration batch |
| Destination state | on-hand + valuation at cutover date | historical movement records | identical to the original outcome |
| **Quantity behaviour** | quantity **created without a movement** | quantities **already historical**; must not re-affect on-hand | **adds ZERO quantity** (`RT-E15-05`) |
| **Valuation behaviour** | **value created without a purchase** — `HX-24` *"quantity and value"* | historical cost basis, not re-valued | **adds ZERO value** |
| **Accounting behaviour** | opening equity/suspense counterpart — **counterpart account UNDETERMINED** | **none** — history, not posting | **none** |
| **Historical date semantics** | the **cutover date**, not the system date | **original historical dates** | original identities preserved |
| Opening-balance semantics | **this flow IS the opening balance** | `HX-25`: *"opening plus history from the cutover date"* | n/a |
| Ownership | Migration → Inventory **and** Accounting (`HX-24` is the only **dual-target** handoff) | Migration → Inventory | Migration |
| Reversal / correction | **UNDETERMINED** — element `13`'s corrected-entry link does not exist | **UNDETERMINED** | replay is not a reversal |
| Consumer | Inventory + Accounting | Inventory | both |
| Reconciliation | certified extract ↔ opening position | history ↔ movement ledger | **batch identity present beside each, absent from the basis** |
| **Evidence authority** | `HX-24` · `X-20` · element `14` | `HX-25` · `X-20` | element `14` · `RT-E15-05` · `X-21` |
| **Proposed membership** | **`IR` and `AR`** — it moves quantity **and** value | **`IR` only** — quantity/history, no financial effect | **NEITHER — it is a DIMENSION of `MF-01`/`MF-02`, not a flow** |

### 2.1 What the rows expose

| Finding | |
|---|---|
| **`CC-F-11`** | **`MF-01` creates value with no purchase and no movement.** Every valuation rule in the corpus binds value to a **movement** (`JT-04` = recognition at the physical movement). **Opening balance has no movement, so no existing rule reaches it, and its counterpart account is undetermined.** This is why its absence from `AR` matters: the one flow that creates value without a movement was never asked to converge |
| **`CC-F-12`** | **`MF-03` is a dimension, not a flow** — including it would inflate the denominator. **`3` candidates resolve to `2` flow rows + `1` dimension**, which is why `05_` refused to assert `n` |

| | |
|---|---|
| **Proposed** | **`IR` `18 → 19`** (`MF-02`) · **`AR` `29 → 30`** (`MF-01`) · `MF-01` also joins `IR` → **`IR 18 → 20`** |
| **`CORE-02` status** | **COMPLETE — PROPOSED, NOT ADMITTED.** Admission is **`B9′`**, Boss authority |

---

## 3. `CORE-03` — limb-2 re-wording: **EXTERNAL AUTHORITY REQUIRED**

### 3.1 Tests SMEs Core CAN perform, performed

| Test | Result |
|---|---|
| **Preserve original control intent** | Intent: **ensure exactly one mechanism carries machine cost into product cost** — i.e. prevent double-counting of machine cost. **Intent is coherent and must survive any re-wording** |
| **Where the ambiguity is** | *"prove exactly **one** mechanism"* is a **uniqueness** assertion. Its own reviewer records it *"tests for uniqueness where the answer is **zero**"* — **`R-22`: fixed-overhead elements have NO INJECTION PATH.** A uniqueness test over an empty set **cannot be satisfied or falsified** |
| **Does it weaken tolerance-zero protection?** | Re-wording must **not**. The protection is against **double-counting**; a re-worded limb must still bar two mechanisms if two ever exist |
| **Relationship to `AAS-V-03`** | **DISTINCT — not duplicate.** `AAS-V-03`'s limbs are **`F6` (`MTI-D-04`)** and **`F1`'s COGS gap**; the manufacturing veto's are **`BLK-07`** and **machine cost**. **Four limbs, four subjects, `0` overlap** — the `07_` `CLASS C` finding, re-tested here and unchanged |
| **Duplicate or distinct?** | **DISTINCT** |

### 3.2 What SMEs Core may NOT do

**`SC-42` §2, verbatim:** *"**AAS+ re-wording of limb 2** — it 'tests for uniqueness where the answer is
zero', so it 'cannot be discharged in either direction as written'. **AAS+ — issuer authority. SMEs Core
does not draft it.**"* · **SMEs Core proof obligation: *"CANNOT START"*.**

**`SC-42` §1: AAS+ input arrived since `093585d0`? — *"NO — `0`."***

> **§4 `CORE-03` asks for *"proposed canonical wording."* Primary text says SMEs Core does not draft it,
> and §25 forbids inventing authority. The diagnosis and the required properties are supplied above;
> the wording itself is not, and fabricating issuer text would be the prohibited act.**

**Required properties any AAS+ re-wording must satisfy** *(supplied as input to the issuer, not as
issuer text)*: satisfiable when the mechanism count is `0` · falsifiable when it is `≥ 2` ·
preserves the double-counting bar · does not presume `R-22`'s injection path exists.

| | |
|---|---|
| **`CORE-03` status** | **`EXTERNAL AUTHORITY REQUIRED` — AAS+ (issuer)** |
| SMEs Core work owed | **`0`** — the proof obligation **cannot start** until the re-worded limb exists |

---

## 4. Checkpoint

> ## `CHECKPOINT B — 3 OBLIGATIONS PROCESSED`
>
> **`CORE-01` **ALREADY DISCHARGED** at `SC-14`/`SC-15`/`SC-16`, `23` minutes after the obligation was
> created — and **this package wrongly carried it open at `PT-11`, `13_` and `16_`, contradicting its own
> `PT-00`**. Corrected: **`B1` covers `6` decisions, not `4`** ·
> `CORE-02` **COMPLETE** — `3` candidates resolve to **`2` flow rows + `1` dimension**; `CC-F-11`:
> **opening balance creates value with no movement and no rule reaches it** ·
> `CORE-03` **`EXTERNAL AUTHORITY REQUIRED`** — tests performed, `AAS-V-03` confirmed **distinct**,
> **wording not fabricated** ·
> **SMEs Core obligations still open: `0`.**

