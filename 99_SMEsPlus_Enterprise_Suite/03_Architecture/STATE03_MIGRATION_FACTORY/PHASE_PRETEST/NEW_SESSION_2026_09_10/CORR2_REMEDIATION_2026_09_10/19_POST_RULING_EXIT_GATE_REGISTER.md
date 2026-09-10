# 19 — POST-RULING EXIT GATE REGISTER

# `DENOMINATOR 14 · EVERY DOWNSTREAM OBLIGATION CARRIES ITS 6 CONTRACT ELEMENTS`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Authority: **`BOSS-CORR2-RD01`, option (b)** via `17_` §1.2 · Boss: **SOLE FINAL APPROVER**

> **This file constitutes the gates.** `31_` records the per-condition **status**. The separation exists
> because `14_` of the recovery package merged them, and the merge is where condition `11`'s `G` limb
> was lost from the counting instrument (`R2-F-06`).

---

## 1. THE GATE CONSTITUTION AS RULED

| Condition | Obligation | Limb | **Gate** | Governing instrument | Ruled by |
|---|---|:-:|---|---|---|
| `9` | `EC-04` complete | `I` | **STATE 8-Criteria Exit Gate** | **`SC-54` cl. 3** — *"closed by EXECUTED RUNTIME PROOF plus INDEPENDENT REPRODUCTION, evidenced no later than the STATE 8-Criteria Exit Gate"* | `BOSS-CORR2-RD01` (b) |
| `10` | `EC-07` complete | `G` | **MODULE + STATE 8-Criteria Exit Gates** | **`SC-54` cl. 2** — *"An internal `PHASE` transition inside a State is NOT an eight-criteria gate"*; cl. 4 | `BOSS-CORR2-RD01` (b) |
| `12` | `48`-item verification | `I` | **BUILD / TEST** | **`SA17` §2b** — *"nothing may be read as testing tenant isolation until an implementation exists"* | `BOSS-CORR2-RD01` (b) |
| **`11`** | **`E2E-04` traversable** | **split — §2** | **PRE-TEST (`G`) + FD Exit (`D`) + Build/Test (`I`)** | Boss's `E2E-04` clause; `B8′`; `09_` §2.4 | `BOSS-CORR2-RD01` (b) |

**All other `13` conditions remain at Pre-Test.**

```
17 master-prompt conditions
 - 3 re-placed wholesale        {9, 10, 12}
 = 14 PRE-TEST EXIT DENOMINATOR       <- condition 11 RETAINED, as ruled
```

> **The `G` limb MUST remain counted** — `17_` §1.2, verbatim. **It is counted.**

---

## 2. CONDITION `11` — THE LIMB REGISTRY

**The instrument that `14_` lacked.** Each limb is a row, so removing a condition cannot silently remove
an obligation.

| Limb | Obligation | Class | **Gate** | State | Owner |
|---|---|:-:|---|---|---|
| **`S`** | the supply-raised exit **specified** | `S` | **Pre-Test** | **CLOSED** — `SC-01` §6.2 | SMEs Core |
| **`G`** | **the re-grade act** | `G` | **PRE-TEST** | **OUTSTANDING — NOT PERFORMED** | **SMT, per `B8′`** |
| `D` | the target state machine **carrying** the exit | `D` | **Functional Design Exit** | OPEN | Functional Design |
| `I` | the traversal **executed** | `I` | **Build / Test** | OPEN | Build / Test |

**Condition `11`'s Pre-Test status = the `G` limb's status = `FAIL`.**

### 2.1 The `G` limb's unresolved routing — carried, not closed

`B7-F-11`, confirmed at primary text and **not disturbed by any ruling**:

> `SC-03` L21: *"**And this is not independent assurance.** It is **internal first-line challenge by
> specialist role**"* · `SC-04` L94: *"`SC-03` is internal first-line challenge by specialist role.
> It is not independent assurance"*

**The re-grade act is routed to SMT, which primary text says is not independent of SMEs Core.**
`BOSS-CORR2-RD01` places the act at Pre-Test and **does not address who may perform it**.

> **`CORR2-EGR-01` — MODERATE.** The `G` limb is now correctly **counted** and still **unperformable
> by an independent party**, because the party it is assigned to is declared non-independent by the two
> registers that define it. **Counted ≠ closable.** Carried to `32_` as an eligibility observation and
> **not escalated** — `B8′` already assigned it, and re-asking without material delta is prohibited.

---

## 3. `SC-54` CLAUSE `5` — APPLIED, WITH THE EXEMPTION IN ITS EXACT SCOPE

**Clause `5` (`NO DUMPING`), verbatim:** *"Only obligations that **REQUIRE EXECUTION** to discharge may
be met in Pre-Test. Any item moved forward must be recorded **with the evidence proving it is
execution-dependent**."*

| Moved | Execution-dependency evidence | Clause `5` |
|---|---|---|
| `9` `EC-04` | *"specified, not executed"*; `0 / 3` | **SATISFIED** — evidence present in substance |
| `12` `48` items | *"enumerated, not executed"*; `0 of 48` | **SATISFIED** |
| `11` `I` limb | traversal cannot occur pre-build | **SATISFIED** |
| **`11` `D` limb** | **NONE — it is a design artefact, not an execution artefact** | **EXPRESSLY EXEMPTED by Boss** — `17_` §1.3 |
| `10` `EC-07` | — | **not a cl. `5` case**: cl. `2` says Pre-Test was never its gate, so nothing is *moved forward* |

**The exemption's scope, restated because it is narrow:** it changes **phase placement only**. It does
**not** satisfy the `D` limb, waive downstream evidence, waive `E2E` proof, close the `G` limb, or
create runtime proof. **`R2-F-07` is closed as a governance defect — answered by exemption, not silence.**

---

## 4. DOWNSTREAM OBLIGATION CONTRACTS — `§8`'s six elements, per obligation

**`§8`: *"A downstream proof obligation MUST still have: named population, exact future gate, evidence
contract, owner, trigger, success criterion."* A deferral without all six is not a deferral.**

| Obligation | Named population | Future gate | Evidence contract | Owner | Trigger | Success criterion |
|---|---|---|---|---|---|---|
| **`EC-04`** | `3` boundaries | **State 8-Criteria Exit Gate** | executed runtime proof **plus independent reproduction** for each boundary | Architecture | first runtime capable of the boundary | `3 / 3` closed, each with an independent reproduction |
| **`EC-07`** | `2` consecutive clean structurally independent passes | **Module + State Gates** | two passes, each by a party whose **reasoning-executor identity** is recorded before evidence review | Independent party | Module gate entry | `2 / 2` clean, consecutive, structurally independent |
| **`48`-item verification** | `X-01`…`X-22` (`22`) + `E2E-01`…`E2E-18` (`18`) + `PT-S-01`…`-07` (`7`) + `PT-C-01` (`1`) | **Build / Test** | each item exercised against a built system | Build/Test | first build | `48 / 48` `PASS`, **and every `FAIL` recorded, not re-run away** |
| **`E2E-04` `D` limb** | the target state machine carrying the supply-raised exit | **Functional Design Exit** | a state machine in which the supply-raised exit is a modelled transition | Functional Design | FD commencement | the exit is representable and its guard is stated |
| **`E2E-04` `I` limb** | the traversal | **Build / Test** | the traversal executed end to end | Build/Test | first build | traversed, with the re-grade consumed |
| **`CORR1-F-03` idempotency** | `MF-01`, `MF-02` re-run | **Build / Test** (semantic first — `28_` `BS-05`) | run a batch twice | SMEs Core → Build/Test | element `15` specified | opening quantity and value **identical** after the second run, **and the second run recorded, not silent** |
| **`ZT-06` isolation proof** | `48` items; `X-15` | **Build / Test** (semantic first — `28_` `BS-14`) | two companies configured | Architecture | first multi-company build | **`8 / 8`** isolation proofs; both lock-defeat paths closed **and leaving a record** |
| **Configuration reachability** | `CFG-01`…`CFG-12` | Build/Test; FD Exit first for `7` | found, reached, selected, activated, persisted, applied | per `22_` §3 | owning scenario exercised | expected behaviour observed **and the negative case observed** |
| **Optional function reachability** | `OPT-01`…`OPT-08` | Build/Test; FD Exit first for `4` | enabled and disabled | per `23_` §3 | owning scenario exercised | **both directions** — enabled produces the effect, **disabled produces nothing** |

**`9` downstream obligations · `9` carrying all `6` elements · `0` bare deferrals.**

---

## 5. THE FIVE-STATUS CLASSIFICATION — `§8`

| Status | Applied to |
|---|---|
| **`PASS AT CURRENT PHASE`** | the `7` critical controls at `100 %` (`27_`); `12` source-presence rows (`26_`) |
| **`HOLD AT CURRENT PHASE`** | `7` failing exit conditions; `6` source rows; Configuration `41.7 %`; Optional `12.5 %`; `ZT-05`, `ZT-06` |
| **`DEFERRED WITH VALID DOWNSTREAM CONTRACT`** | the `9` obligations at §4 |
| **`UNMEASURABLE — INVALID POPULATION`** | **`0`** — both former instances closed by `22_` and `23_` |
| **`N/A — AUTHORITY SUPPORTED ONLY`** | **`0`** — `XMC-H-15`/`-16` re-classified `CONDITIONAL` by `BOSS-CORR1-01` §2.3 |

> **`0` items in the two statuses that hide a gap.** That is the governance result of this round.

---

## 6. WHAT THE GATE CONSTITUTION DOES NOT DO

| |
|---|
| It does **not** satisfy `EC-04`, `EC-07` or any of the `48` — all remain `0` |
| It does **not** discharge the `G` limb — **OUTSTANDING** |
| It does **not** make Pre-Test exitable — `31_` reports `7 of 14` |
| It does **not** authorize Functional Design |
| **`96 %` coverage is not permission to pass a gate** (`§9`) — both tests are separate and both must hold |

---

## 7. CHECKPOINT

> **Gate constitution recorded as ruled · **denominator `14`, condition `11` retained, `G` limb
> counted** · limb registry created so an obligation cannot be dropped by removing a row ·
> `SC-54` cl. `5` applied to all `4` moves, **`1` expressly exempted in its exact scope** ·
> `9` downstream obligations, **each carrying all `6` contract elements** · five-status classification
> applied with **`0` items in `UNMEASURABLE` and `0` in `N/A`** ·
> **`CORR2-EGR-01`: the `G` limb is counted and remains routed to a party primary text calls
> non-independent.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the SOLE FINAL APPROVER.**
