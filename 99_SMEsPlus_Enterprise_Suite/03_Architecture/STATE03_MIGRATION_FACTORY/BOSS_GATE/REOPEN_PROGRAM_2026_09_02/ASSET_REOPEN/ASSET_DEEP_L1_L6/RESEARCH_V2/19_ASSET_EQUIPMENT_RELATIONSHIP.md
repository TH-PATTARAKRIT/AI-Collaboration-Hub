# 19 — ASSET ↔ EQUIPMENT RELATIONSHIP
**LAYER 2 — AUDIT QUARANTINE**

Answers §34 and §35 in full. This is the deliverable the prompt asked for most
specifically, and the answer is more complicated — and more defective — than
"a custom field exists".

## 1. The native position

**There is no native relationship.** Established by exhaustive search of the
reference v18 Enterprise addons tree (797 modules): the asset model is referenced
in Python by exactly three modules, none of them operational (`08` §1).

Confirmed in both directions:
- No equipment field on the asset.
- No asset field on the equipment.
- No module inherits both.
- The only two modules that extend the equipment model are an HR bridge and the
  manufacturing bridge; neither mentions assets.
- The equipment model has **no product field** either.

`FACT VERIFIED` — a verified absence, established by exhausting the search space.

Note for completeness: a **fleet** integration for assets exists in the *next*
version line, but not in v18 and not for equipment.

## 2. The custom link — what it is

Added by a project custom module (v18 line, versioned 18.0.1.6, authored by the
project's own vendor), which depends on the asset module, the maintenance module
and the project's equipment/stock bridge.

| Property | Value |
|---|---|
| Direction | **Asset → Equipment** |
| Type | `Many2one` |
| Label | *Equipment* |
| Domain | Only equipment whose custom status is *Equipment* (i.e. not yet taken as an asset) |
| **Inverse** | **None** |
| **Uniqueness constraint** | **None** |
| Required | No |
| Companion field | A related group-reference string, read-only, reaching through to the equipment's own reference code |
| View | Added to the asset form by an inherited view, in an "Other" group, hidden on templates |

Behaviour attached:

1. **On asset confirm**, the linked equipment's custom status is written from
   *Equipment* to *To Assets*.
2. **On asset sale**, the linked equipment is intended to be deactivated.

`FACT VERIFIED`

## 3. Three defects in the custom link

All three were found by reading the module's package initialiser and view files as
well as its model file. All three are silent — none raises an error.

### `EQ-DEF-01` — the disposal behaviour never runs `CONTRADICTED`

The "deactivate the equipment on sale" behaviour lives in a wizard override file.
The module's package initialiser imports **only the models package**. The wizard
file is therefore **never imported and the override never registered**.

**Consequence: selling or disposing of an asset leaves its linked equipment active
and still flagged *To Assets*.** The intended lifecycle closure does not happen.

`FACT VERIFIED` — module initialiser versus file inventory.

### `EQ-DEF-02` — the display-name override never fires

The module overrides a display-name hook that was **removed from the framework
after v16**. On v18 nothing calls it. The intended behaviour — appending the
equipment's group reference to the asset's displayed name — does not occur.

`FACT VERIFIED` — the hook is absent from the v18 framework.

### `EQ-DEF-03` — the field's read-only rule is inert

The equipment field is declared with a **state-conditional read-only attribute**
whose framework support was **removed after v16**. The attribute is accepted and
ignored. The intended control — editable only while the asset is draft — is not
enforced, so the equipment link can be changed on a **running or closed** asset.

`SUPPORTED INTERPRETATION` — the attribute is obsolete and the framework tolerates
unknown field attributes without raising. Whether it is silently ignored or
partially honoured on this exact build should be confirmed on the UAT (`UNR-13`).

### Dead legacy file

The module also carries an unreferenced file targeting a **different asset model**
(the third-party one described in `CTR-03`). It is not imported and does nothing.
Its presence is why an earlier reading in this session initially concluded the
module could not load at all — corrected in `29` `REV-04`.

## 4. Cardinality — the exposure

```
Asset  ──── N:1 ────►  Equipment
```

with **no inverse and no unique constraint**. Therefore:

- **N assets may point at one machine.** Nothing prevents it, warns about it, or
  reports it.
- **One machine cannot be traced to its assets** without scanning all assets.
- After one upward re-evaluation the parent and child are two asset records; the
  child does **not** inherit the equipment link (it is not in the copied field
  set), so the machine's total capitalised value is not reachable from the link.

For a costing design that keys a machine's cost pool on this association, **the
duplicate case double-counts and the child case under-counts**. Both are
correctness failures, not hygiene issues.

`FACT VERIFIED` (structure) · **uncounted on the UAT** — `UNR-08`

## 5. Classification demanded by §35

| Question | Answer |
|---|---|
| Does the asset model contain a relation to the equipment model? | **Yes — on this project only** |
| Field name | A custom field on the asset, labelled *Equipment* |
| Field owner | Project custom module |
| Module | Project custom equipment-sequence module, v18 line |
| Code | Model inherit + one confirm override; plus a non-executing wizard override |
| View | Inherited view on the asset form |
| Database representation | A nullable integer column on the asset table with a foreign key to the equipment table |
| Business behaviour | A **label**. One status side-effect. Nothing financial consumes it |
| Classification | **`CUSTOM EXTENSION` — SOURCE LEARNING LOCAL FEATURE** |

## 6. The honest summary

> The Asset↔Equipment relationship that this project relies on is a **manually
> chosen dropdown**, added by a custom module, with **no inverse, no uniqueness
> constraint, no financial consumer**, whose intended read-only rule does not
> apply, whose intended display behaviour does not fire, and whose intended
> disposal behaviour **does not execute at all**.
>
> It is the only bridge between the financial and operational halves of the same
> physical machine, and three of its four behaviours are inert.

This must be repaired before any per-machine costing design can rest on it. It is
the **first** item in the sequencing recommended at `10` §3.1 — not because it is
the most interesting, but because everything else depends on it.

## 7. Cross-references

- The equipment side of the story, including how equipment records come into
  existence: `20`.
- Why the Boss's memory of "an asset with an equipment link that depreciates
  daily" cannot be a single legacy record: `CTR-03` in `37`.
- The cross-domain write with no inverse: `CTR-04`.
