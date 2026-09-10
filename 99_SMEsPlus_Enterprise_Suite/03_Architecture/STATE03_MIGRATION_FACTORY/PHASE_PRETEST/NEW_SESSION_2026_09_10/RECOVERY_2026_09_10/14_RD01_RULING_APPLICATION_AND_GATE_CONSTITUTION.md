# 14 — `R-D-01` RULING APPLICATION · GATE CONSTITUTION CORRECTION

## `CHECKPOINT H — APPLIED · 7 of 13 · 0 EVIDENCE WAIVED`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-RECOVERY-NEWSESSION-001]`
Ruling: `[SMEPLUS-26-09-10-PHASE-PRETEST-RECOVERY-BOSS-RULING-001]` · Recovery baseline **`94f23976`**
Boss: **SOLE FINAL APPROVER**

> **Boss's own words, carried as the governing constraint on this application:**
> *"It does NOT waive evidence. It does NOT satisfy any criterion. It does NOT create runtime proof.
> It does NOT authorize Functional Design. It does NOT declare Pre-Test PASS."*

---

## 1. The four re-placements

| # | Criterion | Was | **Ruled placement** | Status **after** |
|---:|---|---|---|---|
| **9** | **`EC-04`** | Pre-Test exit | **STATE GATE** | **`0 / 3` — deferred to its correct gate, NOT discharged** |
| **10** | **`EC-07`** | Pre-Test exit | **MODULE GATE + STATE GATE** | **`0 / 2` — B-7 Round 1 does NOT automatically count as a clean pass** |
| **12** | **`48`-item verification** | Pre-Test exit | **BUILD / TEST GATE** | **`0 PASS · 0 FAIL · 48 HOLD` — `0` items upgraded** |
| **11** | **`E2E-04`** | Pre-Test exit, whole | **`D`-limb → FUNCTIONAL DESIGN EXIT · `I`-limb → BUILD / TEST** | **`NOT TRAVERSABLE` — no re-grade performed or certified** |

---

## 2. Arithmetic verification — Boss required it, so it is executed and shown

```
before          : 7 satisfied / 17 total          (7 + 10 = 17 ✔)
removed         : {9, 10, 11, 12}   — all four were FAIL
removed & SATISFIED : {}            — the satisfied count CANNOT move
after           : 7 satisfied / 13 applicable     (7 + 6 = 13 ✔)
surviving FAIL  : {3, 4, 13, 15, 16, 17}
Boss expected 7/13 → CONFIRMED
```

**`0` satisfied conditions were among the removed four, so the numerator is arithmetically incapable of
rising from this ruling.** That is the structural guarantee that this is an instrument correction and not
a waiver.

---

## 3. `R-F-02` — the ratio improves and the position does not

| | Before | After |
|---|---|---|
| Fraction | `7 / 17` | **`7 / 13`** |
| **Percentage** | **`41.2 %`** | **`53.8 %`** |
| Conditions satisfied | **`7`** | **`7`** |
| Conditions failing | **`10`** | **`6`** |
| **Obligations owed** | **`10`** | **`10`** |

> **The percentage rises `12.6` points while `0` obligations close.** Boss stated it directly —
> *"This denominator change is NOT a readiness improvement by waiver"* — and it is repeated here because
> **`53.8 %` is the number a later reader will quote, and it is the most misreadable figure this recovery
> produces.**
>
> **Every downstream citation of `7 / 13` by this session carries the words *"instrument correction, not
> improvement"*.**

---

## 4. Preservation — nothing deleted, everything re-registered

**Boss: *"PRESERVED IN THEIR CORRECT DOWNSTREAM GATE REGISTERS. No evidence may be deleted. No historical
FAIL/HOLD may be rewritten."***

| Obligation | Now registered at | Status carried forward **verbatim** |
|---|---|---|
| `EC-04` boundary 1 — `CF-I-03` `D3` cross-tenant | **State Gate** | `SPECIFIED, not executed` |
| `EC-04` boundary 2 — privileged-bypass path enumeration | **State Gate** | `enumerated, not executed` |
| `EC-04` boundary 3 — `SA10` tenant/company matrix | **State Gate** | **`TOLERANCE-ZERO — HOLD`** |
| `EC-07` pass 1 · pass 2 | **Module + State Gates** | `0 / 2` |
| `48` verification items | **Build / Test Gate** | `0 PASS · 0 FAIL · 48 HOLD` |
| `E2E-04` `D`-limb — the target state machine carrying the supply-raised exit | **Functional Design Exit** | **OPEN** |
| `E2E-04` `I`-limb — executed traversal | **Build / Test Gate** | **OPEN** |

### 4.1 `R-F-03` — the limb that would have been lost

**Condition `11` leaves the Pre-Test exit denominator as a whole. Its `S` and `G` limbs do not leave the
programme.**

| Limb | Class | Where it now sits | Status |
|---|---|---|---|
| supply-raised exit **specified** | `S` | **CLOSED** at `SC-01` §6.2 | closed |
| target state machine carrying it | `D` | Functional Design Exit | OPEN |
| executed traversal | `I` | Build / Test | OPEN |
| **the re-grade ACT** | **`G`** | **Boss's `E2E-04` clause: *"remain applicable at the appropriate architecture / Pre-Test control point"*** | **OUTSTANDING — SMT's, per `B8′`, NOT PERFORMED** |

> **Removing condition `11` from the exit set would silently drop an outstanding `G`-limb obligation if
> the limbs were not re-registered individually.** The re-grade act is **not** an `I`-class item and does
> **not** travel to Build/Test with the rest of the condition. **It stays live, unowned by any gate the
> ruling moved, and is carried here explicitly.**

---

## 5. Controls re-run — materially affected only

| Control | Re-run? | Result |
|---|:--:|---|
| Exit-condition count | **YES** | **`7 of 13`**, arithmetic shown |
| Exit-condition membership | **YES** | surviving set `{1,2,3,4,5,6,7,8,13,14,15,16,17}` |
| `EC-04` · `EC-07` · verification · `E2E-04` | **YES** | **`0/3` · `0/2` · `0 of 48` · `NOT TRAVERSABLE` — all UNCHANGED** |
| Readiness split `18 / 4 / 0` | **NO** | not affected by phase placement; still **PROVISIONAL** |
| Boundary set · `12↔18` · `MF-01`/`MF-03` · `AAS-V-02` · vetoes | **NO** | untouched by this ruling |
| FD blockers | **NO** | **`5`** — none was among the re-placed conditions |
| Circular gate defects | **YES** | **`3` → `0` at the Pre-Test gate.** `CGD-01`/`-02`/`-03` are **resolved by re-placement, not by satisfaction** |

---

## 6. Non-Boss items — carried exactly as ruled

| Item | Ruling | Applied |
|---|---|---|
| **`POH-D-02`** | remain with Thai statutory authority; **Boss authority shall NOT substitute** | **`PTE-4`, unchanged.** `0` Boss substitution |
| **`SC-SMT-01`** | existing open Boss-owned obligation; **do NOT re-ask** | **carried, NOT re-asked.** It gates `X-08`/`X-09` — recorded, not escalated |
| **`CORE-07`** | SMEs Core / Architecture; complete the `XMC-H-13`/`-14`/`-17`/`-18` analysis **before** asking Boss to amend the boundary set | **OPEN — and the precondition on any future `B4′` amendment is recorded** |
| **`AAS-V-02`** | **NOT DISCHARGED** until AAS+ issuer evidence proves the act occurred | **NOT DISCHARGED.** Vetoes **`7` · `0` discharged** |

---

## 7. Post-ruling state

| Control | Value |
|---|---|
| Pre-Test verdict | **`HOLD PRE-TEST EXIT`** |
| Exit conditions | **`7` satisfied / `13` applicable** — *instrument correction, not improvement* |
| Surviving FAIL | **`6`** — conditions `3`, `4`, `13`, `15`, `16`, `17` |
| FD blockers | **`5`** |
| `EC-04` · `EC-07` | **`0/3` · `0/2`** — deferred, not discharged |
| Verification | **`0 PASS · 0 FAIL · 48 HOLD`** |
| `E2E-04` | **`NOT TRAVERSABLE`**; re-grade act **OUTSTANDING** |
| Vetoes | **`7` · `0` discharged** |
| Open Boss decisions | **`1`** — `POH-D-02`, not askable |
| Functional Design | **NOT AUTHORIZED** |

---

## 8. Checkpoint

> ## `CHECKPOINT H — R-D-01 APPLIED`
>
> **`4` criteria re-placed · **`7 / 13`, arithmetic executed and shown; `0` of the removed four were
> satisfied, so the numerator was structurally incapable of rising** · `R-F-02`: the percentage rises
> `41.2 % → 53.8 %` while **`0` obligations close**, and every downstream citation carries that caveat ·
> `R-F-03`: **`E2E-04`'s `G`-limb re-grade act would have been silently dropped** by removing the
> condition wholesale — re-registered explicitly · `3` circular gate defects **resolved by re-placement,
> not by satisfaction** · **`0` evidence deleted · `0` historical `FAIL`/`HOLD` rewritten · `0` criteria
> satisfied · `0` runtime proof created.**

