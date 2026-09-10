# 08 — `RT-E15` / `PTX` RECONCILIATION

## `CANONICAL RELATIONSHIP ESTABLISHED · 0 DISCHARGED · NO BULK`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-CORRECTIVE-CLOSURE-001]` · Boss: **SOLE FINAL APPROVER**

> **§11: establish the relationship · prevent duplicate counting · define each criterion · evidence
> requirement · `PASS`/`FAIL`/`HOLD`/`N/A` · **individual** discharge. No bulk. No inferred pass.**

---

## 1. The canonical relationship — `PTX` ⊇ `RT-E15`, and the difference is `2`

| | |
|---|---|
| `RT-E15-01`…`-09` | **`9`** runtime obligations, authored at `SA_CORR5_01` §9 |
| `PTX-01`…`PTX-11` | **`11`** Pre-Test exit criteria, constituted at `PT-09` §4 under `SC-BD-09` §8.1 |
| **Relationship** | **`PTX-01`…`PTX-09` ARE `RT-E15-01`…`-09`, one-to-one, verbatim.** `PTX-10` and `PTX-11` are **additions** |

### 1.1 Duplicate-counting control

> **The exit-criteria denominator is `11`, NOT `20`.**
> **`9 RT-E15 + 11 PTX = 20` is a double count** — `PTX-01`…`-09` are the same `9` obligations carrying a
> Pre-Test identifier. **Anyone reporting `20` has counted the `RT-E15` family twice.**

**Stated because this programme has recorded unit-conflation as its most frequent defect class, and this
is the exact shape: one population, two identifier families.**

---

## 2. The register — `11` criteria, each with its own status

| `PTX` | = `RT-E15` | Criterion | Evidence requirement | Status |
|---|---|---|---|---|
| `PTX-01` | `-01` | present one basis twice → **exactly one** Accounting Event; the second returns the first identity | executed run, both presentations logged | **`HOLD`** |
| `PTX-02` | `-02` | same occurrence, two recognition roles → **two** events, each joinable to the occurrence | executed run | **`HOLD`** |
| `PTX-03` | `-03` | reversal discoverable from its original **and vice versa**; original unchanged **byte-for-byte** | executed run + byte comparison | **`HOLD`** — **and `04_` §3 records `H-07` as a direct conflict with this criterion** |
| `PTX-04` | `-04` | two tenants, byte-identical occurrence identities → **two distinct** events; **a never-transacted tenant returns a structurally DIFFERENT result from a clean one** | executed run + **discriminating population** | **`HOLD`** |
| `PTX-05` | `-05` | batch replay reproduces identical identities, **adds zero events**; batch identity beside each, **absent from the basis** | executed replay + element 14 | **`HOLD`** |
| `PTX-06` | `-06` | `A14`: same attempt identity twice → **one** fact; a write with **no** attempt identity → **refused and recorded** | executed positive + negative | **`HOLD`** |
| `PTX-07` | `-07` | identity computed day 1 and recomputed day 90 **from the stored basis** is byte-identical | two executions ≥ 90 days apart, or a proven deterministic function | **`HOLD`** |
| `PTX-08` | `-08` | **synthetic injection** — inject one fact differing by one basis part; event count moves **`1 → 2`** | the injection itself | **`HOLD` — INSTRUMENT** |
| `PTX-09` | `-09` | **coverage assertion** — presentations **requested vs recognised vs refused**, published beside every run | the run's own output | **`HOLD` — INSTRUMENT** |
| **`PTX-10`** | **—** | the **deterministic-identity proof**: the six-part basis (`XMC-C-A2`) shown deterministic **and** duplicate-preventing | executed proof | **`HOLD`** |
| **`PTX-11`** | **—** | **order gate**: `MTI-50` built → `CF3-C-01`…`C-04` fire → **only then** any positive test; `RT-E15-08`/`-06` **before** any scenario's retry dimension | build + instrument-control evidence | **`HOLD` — ORDER GATE** |

**`11` criteria · `0 PASS` · `0 FAIL` · **`11 HOLD`** · `0 N/A`.**

---

## 3. Why every status is `HOLD` and none is `FAIL`

| | |
|---|---|
| **Not `FAIL`** | a `FAIL` asserts the system was tested and did not satisfy the criterion. **Element 15 is not built; nothing was tested.** Recording `FAIL` would be a fabricated runtime result |
| **Not `N/A`** | **`SC-BD-09` §8.2: whether idempotency is required is NOT re-openable** — `BD-ACC-01`'s sentence is unqualified. **No criterion may be excused as inapplicable** |
| **`HOLD`** | correct: the obligation stands, is defined, and cannot yet be executed |

**§11's *"no bulk discharge"* is satisfied: `11` rows, `11` individual statuses, `0` inferred.**

---

## 4. Discharge status of the Boss instruction itself

| Obligation | State |
|---|---|
| **`SC-BD-09` §8.1** — write `RT-E15-01`…`-09` + the deterministic-identity proof **into Pre-Test exit criteria** | **DISCHARGED** — `PT-09` §4; owner recorded as *"Pre-Test"* at `SC-11` §6 #8 |
| **Boss ADOPTION of `PTX-01`…`-11`** | **OUTSTANDING — Boss item `B6`** |
| **Satisfaction of the criteria** | **`0 of 11`** — requires element 15 built |

> **Three distinct states that must not be collapsed: the instruction is discharged; the criteria are not
> adopted; and none is satisfied.** Reporting only the first would read as completion.

---

## 5. Checkpoint

> **`PTX-01`…`-09` = `RT-E15-01`…`-09` one-to-one; `PTX-10`/`-11` are the `2` additions ·
> **exit-criteria denominator is `11`, not `20` — `9 + 11` double-counts the family** ·
> `11` individual statuses, **`11 HOLD`, `0 PASS`, `0 FAIL`, `0 N/A`, `0` bulk, `0` inferred** ·
> the Boss instruction is **discharged**, the criteria are **not adopted** (`B6`), and **`0 of 11` are
> satisfied** — three states, kept apart.**

