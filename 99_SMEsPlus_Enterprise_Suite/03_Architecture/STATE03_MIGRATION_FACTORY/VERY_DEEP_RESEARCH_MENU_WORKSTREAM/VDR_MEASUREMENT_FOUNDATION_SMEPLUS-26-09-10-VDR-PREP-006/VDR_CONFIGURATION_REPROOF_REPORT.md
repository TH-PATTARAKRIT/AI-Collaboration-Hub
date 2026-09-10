# VDR_CONFIGURATION_REPROOF_REPORT.md
# Configuration — rebuilt from evidence, and still not measurable per function

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 13.

---

## 1. What was retracted and why

PREP-004 published `CONFIGURATION 17.31%` by crediting each gated element with a determination made
about its **gate**. The gates themselves were graded **not verified** — all 44 of them — while the 702
elements they govern were graded verified by inheriting a state the same document declared
*not determinable*. PREP-005 retracted it to **0.00%**.

**This round does not restore it. It states precisely what is proven and what is not.**

## 2. What IS proven, per gate

| | |
|---|---|
| Gates governing register elements | **42** — two independent shapes agree; the 48 published in PREP-003 does not reproduce |
| Gates including switch-only | **49**, all covered |
| Kind | **20 role · 29 capability** |
| Gates with a settings switch | **26 of 49** |
| Resolution | **49 of 49** to a declaration with file and line |

**The nine OFF-vs-ON axes are determined for all 49 gates.** Menu changes for 30; button 28; field 45;
action 9; workflow 30; **automation: no change for any of the 49**; **schema: no change for any of the
49**; records change for 7; stock or accounting 6; **security changes for 21 and widens in every case
measured**; cross-module 48.

## 3. What is NOT proven, and it is the whole dimension

§19 requires, **per material function**: configuration required · default · OFF · ON · **alternative
value** · dependencies · scope · runtime consequence — and *"no configuration result may rely solely on
UI setting labels; verify actual effect."*

| Requirement | State |
|-------------|-------|
| Per **gate** OFF-vs-ON consequence | **PROVEN** — nine axes, 49 gates |
| Per **function** consequence | **NOT PROVEN** for any function |
| **Alternative value** (a third state, not a second) | **NOT MEASURED.** Only OFF and ON were ever examined |
| Actual effect rather than label | proven for the gates; **not joined to any function** |

**Per-gate and per-function are different claims, and the previous round published the first wearing the
second's label.**

## 4. The runtime discrimination that does hold

Across five deployments: **is a gate necessary for its elements to be present, and is it sufficient?**

| Question | Result |
|----------|--------|
| Necessary? | **no counter-example** — 0 of 26 discriminable gates have elements present where the gate is absent |
| Sufficient? | **no — 4 gates are present where their gated elements are absent** |

**A gate installs nothing.** It ships with the module that declares it and governs visibility over what
is already installed. This is an observation from five real deployments, and it stands.

## 5. The finding that must not be lost in the retraction

**A capability switch turned OFF does not revoke it from anyone holding it directly.** Confirmed at
runtime this programme against three current-generation deployments: **8, 7 and 6 gates** are held by
direct membership that no holder group implies, and **the settings page reads those as OFF.**

Most are role groups where direct assignment is intended. **The sharp cases are capability gates** — on
the transacted deployment, multi-company and multi-warehouse.

> **A control had to be repaired before this could be believed.** The first runtime pass returned
> *"0 gates with direct members"* on all three deployments — a clean, plausible zero produced by a key
> extractor that never matched the real column names. A control on the relation sizes was added before
> any conclusion was drawn, and it failed the first instrument.

## 6. Coverage

| | |
|---|---:|
| Configuration Coverage, per function | **0.00%** |
| Floor | 96% |
| | **FAIL** |

**Zero is the honest figure.** The per-gate work is real, substantial and reusable; it is not a
per-function measurement, and this round declines to convert one into the other.

## 7. What would move it

The gate consequence joined to **each governed element's own process** — which is possible for the first
time, because the process dimension now has an instrument. That join is the next round's work, and it
requires a certified population to join against.
