# VDR_HOP0_RECONCILIATION_MATRIX.md
# Every prior identity classified against the reconstructed Hop-0

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 03 groundwork.

---

## 1. Prior population against the new Hop-0

| Classification | Count | Meaning |
|----------------|------:|---------|
| **PREVIOUSLY KNOWN** | **4,148** | found by the reconstruction, in the same identity |
| **KIND NOT ENUMERATED BY THE NEW METHODS** | **700** | a real prior item of a kind the two new methods do not emit — settings fields, gated view sub-elements, buttons, handoff objects, system parameters |
| **OUT OF SCOPE UNDER THE NARROWER ANCHOR RULE** | **215** | its module declares and extends no anchor model |
| **UNRESOLVED — in scope, not found** | **11** | in a domain module, of an enumerated kind, and the reconstruction did not find it |

**4,148 of 5,074 prior rows survive under the match predicate used here — and that predicate was never declared.** An independent challenger reproduced **2,942** on exact identity and **4,349** on a deliberately over-counting bound; 4,148 lies between them, so it is reachable only under an undeclared rule. **The figure is withdrawn pending a declared predicate; 2,942 is the reproducible floor.** The two registers also mix units — 926 *rows* against 1,802 *identities* — presented as one reconciliation. The other 926 are classified, not
dropped, and each class carries a different consequence.

## 2. The 700 — a real limitation of the new methods, not a shrunken domain

These are **not false prior entries.** They are kinds the two new discovery methods do not emit:

| Kind | Why neither method emits it |
|------|-----------------------------|
| **Settings field** | a field on the settings object; the source method emits it as a field of that model, under a different identity, so the join misses it |
| **Gated view sub-element** | a `<field>` or `<button>` *inside* a view's definition. The source method emits the **view**, not its elements. The runtime method emits the view record, not its contents |
| **Button** | a control inside a view definition, same reason |
| **Handoff object** | a cross-boundary relation, which is a derived fact rather than a declared entity |
| **System parameter** | emitted as a data record, under a different identity |

> **This is the reconstruction's own blind spot, and it is larger than the prior population's blind spot
> in the opposite direction.** The prior population carried 525 gated view elements and 431 buttons that
> this reconstruction does not see; the reconstruction carries 17,429 entities the prior population did
> not. **Neither is a superset of the other**, which is precisely why neither can be certified alone.

## 3. The 215 — the cost of the narrower anchor rule

The new rule requires a module to **declare or extend an anchor model**. A module that touches the
domain only through a menu, a report, a dashboard or a security rule is invisible to it. Examples from
the 215: a dashboard module, several localisation point-of-sale reporting extensions.

**Whether that is correct scoping or a defect is exactly what the independent population challenge was
asked to decide**, and its answer is in `VDR_HOP0_INDEPENDENT_CHALLENGE_REPORT.md`.

## 4. The 11 — the only entries that are unexplained

In-scope modules, enumerated kinds, and not found. All are groups declared by the framework's base
module, which the anchor rule excludes but which the prior population carried because domain elements
reference them. **Recorded as UNRESOLVED rather than reclassified into a comfortable bucket.**

## 5. Newly discovered — 17,429

| Kind | Count |
|------|------:|
| Field on a domain model, owned by any module | 9,619 |
| Behaviour | 4,096 |
| Field declared by a domain module | 3,382 |
| Data record | 1,490 |
| View | 627 |
| Access line | 406 |
| Model | 126 |
| Window action | 114 |
| Constraint | 58 |
| Model extension | 32 |
| Record rule | 29 |
| Server action | 19 |
| Group · Client action · Report action · Menu · Sequence | 59 |

**The four largest classes were all predicted by an independent challenger in the previous round**, from
a much smaller sample: it reported 652 uncarried field records, 138 action records, 251 models and 76
record rules. **The reconstruction finds the same classes at full scale**, which is the strongest
available evidence that the reconstruction is measuring something real.

## 6. Field schema, per §7

Each row of `HOP0_POPULATION.csv` carries: `kind` · `identity` · `module` · `discovery` (BOTH /
SOURCE ONLY / RUNTIME ONLY) · `source_pointer` · `observed_on` · `n_deployments`.
The prior-population classification above is derivable from it by the published join.

## 7. Status

**NOT CERTIFIED.** Two independent methods corroborate 49.5% of what they jointly find, and this
reconciliation adds a second reason: **the reconstruction has a blind spot of 700 prior items that the
prior population could see.** A population that is neither a superset nor a subset of its predecessor,
built by methods that agree on half, is not a denominator.
