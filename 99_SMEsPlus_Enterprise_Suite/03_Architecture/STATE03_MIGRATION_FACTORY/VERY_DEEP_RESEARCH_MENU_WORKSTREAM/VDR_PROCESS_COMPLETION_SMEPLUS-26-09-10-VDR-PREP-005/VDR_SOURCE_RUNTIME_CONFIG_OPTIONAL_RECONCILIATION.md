# VDR_SOURCE_RUNTIME_CONFIG_OPTIONAL_RECONCILIATION.md
# Four axes, four instruments — and a test that none was inferred from another

Session `[SMEPLUS-26-09-10-VDR-PREP-005]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 06.

---

## 1. The rule this table enforces

§2: *source present ≠ runtime reachable ≠ configuration reachable ≠ optional function active.*
**No dimension may be inferred from another.**

That is easy to state and easy to violate silently, so it is **tested** here rather than asserted.

| Axis | Its own instrument |
|------|--------------------|
| **Source presence** | the evidence pointer resolved against the declared tree, to file **and** line |
| **Runtime reachability** | the deployment's own element registry, joined on the item's identity |
| **Configuration reachability** | the gate census over twelve declarative element kinds |
| **Optional-function reachability** | the module dependency graph and the capability-switch bindings |

## 2. The independence test

If one axis were being inferred from another, they would agree everywhere. Measured pairwise over all
5,074 items:

| Pair | Agreement |
|------|----------:|
| source vs runtime | 84.8% |
| source vs configuration | 22.3% |
| source vs optional | 22.3% |
| runtime vs configuration | 26.8% |
| runtime vs optional | 30.3% |
| configuration vs optional | 79.8% |

**No pair reaches 100%, and four of the six sit below a third.** The two highest are explicable and were
checked: source-vs-runtime is high because most declared elements are installed somewhere, and
configuration-vs-optional is high because a capability switch is frequently *both* a gate and an
optional activation route — which is a property of the domain, not of the instrument.

**The axes are measured independently. That is now evidenced, not claimed.**

## 3. The reconciliation

| Classification | n | % |
|----------------|--:|--:|
| SOURCE PRESENT + RUNTIME REACHABLE | 1,983 | 39.1% |
| SOURCE PRESENT + RUNTIME REACHABLE *(inferred from module installation, not observed)* | 966 | 19.0% |
| **SOURCE PRESENT + RUNTIME UNREACHABLE** | **600** | **11.8%** |
| SOURCE PRESENT + RUNTIME REACHABLE + OPTIONAL DEPENDENT | 424 | 8.4% |
| SOURCE PRESENT + CONFIG DEPENDENT + OPTIONAL DEPENDENT *(inferred runtime)* | 326 | 6.4% |
| SOURCE PRESENT + CONFIG DEPENDENT *(inferred runtime)* | 205 | 4.0% |
| **SOURCE ABSENT — the pointer is prose, not a path** | **186** | **3.7%** |
| SOURCE PRESENT + CONFIG DEPENDENT | 155 | 3.1% |
| SOURCE PRESENT + CONFIG DEPENDENT + OPTIONAL DEPENDENT | 109 | 2.1% |
| SOURCE PRESENT + OPTIONAL DEPENDENT *(inferred runtime)* | 70 | 1.4% |
| SOURCE PRESENT + CONFIG DEPENDENT + **SECURITY RESTRICTED** | 47 | 0.9% |
| SOURCE PRESENT + CONFIG + OPTIONAL + SECURITY RESTRICTED | 3 | 0.1% |
| **TOTAL** | **5,074** | |

## 4. What the table says

### `FW5-F-01` — only 39.1% of the domain is plainly present and observed
Everything else carries at least one qualification: the element was inferred rather than seen, or it
depends on a configuration, or on an optional module, or it is restricted to a technical role, or its
own source pointer does not resolve to a path.

**A design derived from "the source contains it" would over-scope this domain by nearly two to one.**

### `FW5-F-02` — 600 items are source-present and reachable on no deployment
11.8% of the domain exists in the reference tree and on none of five real deployments across three
generations. They are **not excluded** — §6 forbids excluding an item for being inactive — but no
runtime claim is made about them in either direction.

### `FW5-F-03` — 966 items are counted reachable on an inference, and they are labelled as such
Their **module** is installed; the **element** was not observed, because for their class no element
record can exist. This is the honest boundary of the runtime instrument and it is carried in the
classification rather than hidden inside a percentage.

### `FW5-F-04` — 186 items have no source path at all
Their pointer is a sentence — *"derived from the model-declaration census"* — not a location. PREP-004
graded all 5,074 items as source-**determined**; that was a grade no row could fail. **These 186 are now
`NOT DETERMINED` on source**, which is what they are.

### `FW5-F-05` — 50 items are source-present, runtime-reachable, and restricted to a technical role
They exist, they are installed, and no ordinary business role can reach them. **That is a fourth state,
distinct from absent and from available**, and it is the state in which the object at the centre of
`CRITICAL-GAP-06` sits.

## 5. The rule that follows for SMEsPlus

**No source-only conclusion counts as function-complete.** Of the four axes, source is the cheapest to
establish and the least informative on its own: it agrees with runtime only 84.8% of the time, and with
configuration and optional reachability barely a fifth of the time.
