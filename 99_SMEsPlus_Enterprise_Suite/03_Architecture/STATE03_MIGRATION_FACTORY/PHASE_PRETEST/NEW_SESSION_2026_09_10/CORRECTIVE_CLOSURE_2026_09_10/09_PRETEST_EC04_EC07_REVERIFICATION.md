# 09 — `EC-04` / `EC-07` RE-VERIFICATION

## `EC-04 = 0/3 CONFIRMED · EC-07 = 0/2 CONFIRMED`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-CORRECTIVE-CLOSURE-001]` · Boss: **SOLE FINAL APPROVER**

> **§12: *"Do not upgrade status without fresh proof."* — Re-tested per sub-item, not inherited.**

---

## 1. `EC-04` — the three tolerance-zero boundaries

| # | Exact requirement | Inherited finding | Current evidence | Material delta? | Verification | Disposition |
|---:|---|---|---|:--:|---|---|
| **1** | `CF-I-03` `D3` **cross-tenant** behaviour under breach | **SPECIFIED, not executed** | `CF-I-03` specified to test-writable granularity; **`CF-I-03R` added at CORR5**; **`MTI-50` must be built first — *"not partially: at all"*** | **NO** | is there an executed run? **NO** — no implementation | **`0` — OPEN** |
| **2** | **Privileged-bypass path enumeration** | **enumerated, not executed** | **`C4-01` `ENUMERATION COMPLETE — EXACT BOUNDED GAPS LISTED`**: 13 path classes over 185 branches / 3,604 paths, coverage 21/21 tokens, **2 false zeros found and corrected**, 5 named gaps `G1`–`G5` | **NO — and see §1.1** | is there an executed **test**? **NO** | **`0` — OPEN** |
| **3** | **`SA10` tenant/company boundary matrix** | **`TOLERANCE-ZERO — HOLD`** | `0 of 58` invariants · `0 of 8` isolation proofs · `0 of 13` enforcement surfaces · `0 of 3` register entries · **register empty** | **NO** | executed proof? **NO** | **`0` — OPEN** |

### 1.1 `CC-F-07` — boundary 2's enumeration is complete and its execution is not, and the two look alike

**`C4-01` is genuinely closed as an enumeration** — and the closure sentence is *"it makes downstream
security testing **writable**, which is the criterion."*

> **Writable is the criterion for the ENUMERATION. It is not the criterion for `EC-04`.**
> **`8C-CLARIFICATION-01` clause 3: specification evidence NEVER satisfies `EC-04`; closure is executed
> runtime proof + independent reproduction.** A reader meeting *"`ENUMERATION COMPLETE`"* beside a
> tolerance-zero boundary could reasonably take the boundary as closed. **It is not.**

**`EC-04` = `0 of 3`. `0` boundaries moved. `0` reclassified.**

---

## 2. `EC-07` — two consecutive clean structurally independent passes

| Requirement | Inherited | Current evidence | Material delta? | Disposition |
|---|---|---|:--:|---|
| Pass 1 | `0` | **`B-7` approved as an ACT** at `SC-BD-10` | **NO** | **`0`** |
| Pass 2 | `0` | — | **NO** | **`0`** |

**`SC-11` §5, verbatim:** ***"`B-7`'s appointment does not itself create an independent pass; structurally
independent passes remain `0`."***

| | |
|---|---|
| Candidates named by SMEs Core | **`0`** |
| Executions | **`0`** |
| **`EC-07`** | **`0 of 2` — CONFIRMED** |
| Bundled obligation | **`SC-55` §4.4** — independent delta re-check of `P08 ea78e160` and `P09 1d54c7e4`; both commits verified to resolve |

> **Approving the act and performing the pass are different events.** This is the same three-state
> distinction as `08_` §4, and collapsing it would be the single easiest false upgrade in the package.

---

## 3. What would close each — stated so the path is not mistaken for progress

| Item | Closure condition |
|---|---|
| `EC-04` `1` | `MTI-50` built → `CF3-C-01`…`C-04` fire → `CF-I-03` `D3` **executed** → **independently reproduced** |
| `EC-04` `2` | the enumerated bypass paths **executed as tests**, not enumerated |
| `EC-04` `3` | element 10 built → `0 of 8` isolation proofs **executed** → independently reproduced |
| `EC-07` | **two consecutive clean passes** by an eligible structurally independent verifier |

**Latest lawful closure point for `EC-04`: no later than the State 8-Criteria Exit Gate.**

---

## 4. Checkpoint

> **`EC-04` re-tested per boundary: **`0 of 3`**, `0` moved · **`CC-F-07`: boundary 2's enumeration is
> complete and reads like closure — *writable* is the enumeration's criterion, not `EC-04`'s** ·
> `EC-07` **`0 of 2`**, `0` candidates, **appointment ≠ pass** · `0` upgrades without fresh proof.**

