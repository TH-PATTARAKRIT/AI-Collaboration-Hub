# LESA_PREP004_RESOLUTION_REPORT.md
# Source Learning Navigator — every unresolved item answered, none referred upward

Session `[SMEPLUS-26-09-10-VDR-PREP-004]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 13.

---

## 1. Mandate under the Boss Decision Shield

§13 lists ten questions LESA must answer for every unresolved item. §2 forbids routing any of them
upward. This round, **eleven items that had been carried as open — five of them proposed as Boss
decisions — were resolved by going and measuring.** Not one required a decision.

## 2. Resolutions

### `LESA4-F-01` — WHERE the evidence is: the database population, answered by classification
Every discovered database identity was located and classified from **its own record of its platform
generation** — not from a filename, a directory name, or a manifest string, three of which have
produced wrong answers in this programme.

**Result: not one discovered identity is a current-generation deployment.** The lab that appeared able
to run the missing valuation counterfactual is the **prior generation and holds no movement data at
all**, so it fails the requirement twice. The target-generation evidence base stands at three
identities, and that is now measured rather than assumed.

### `LESA4-F-02` — WHAT RUNTIME PATH reaches it: the element registries
The table that records, per deployment, every element that deployment actually installed **had never
been extracted in three rounds.** It was extracted from all five deployments — ten tables each, no
server started.

**2,854 of 3,319 element-observable items are now observed as themselves.** The previous round's figure
was 77.

### `LESA4-F-03` — WHO OWNS the value: the valuation object, re-derived
Read from the deployment's own field registry: the per-movement value field is owned by the
**valuation-accounting module**, is **stored**, is **monetary**, and is **`readonly = false`**. The
discriminating control on the same object — three sibling fields that are `readonly = true` — proves the
flag distinguishes rather than defaulting.

Independently corroborated by the deactivation study: **the dedicated valuation-ledger model does not
exist in the current generation at all.** It is replaced by a differently-named object owned by the same
module. **Any analysis keyed on the old name returns a false zero in this generation** — which is
precisely the false zero the programme carried for two rounds.

### `LESA4-F-04` — WHAT CONFIGURATION changes it: the periodic premise, contradicted
Two rounds rested a conclusion on *"every located current-generation deployment runs periodic
valuation."* Read from the deployment's own category records: **real-time (perpetual) on 27 of 37
categories.** The premise was never tested against a configuration record, and it is false.

### `LESA4-F-05` — the boundary rule, measured instead of referred
`BOSS-DEC-10` had been carried for three rounds and proposed to the Boss. **It was answerable in one
query against the deployment's own field registry:**

| Boundary | Objects | Multiple |
|----------|--------:|---------:|
| owned (current population) | 96 | 1.0× |
| hop 1 | 83 related — **39 carried, 44 not** | — |
| **hop 2** | **+132 → 272** | **2.8×** |
| full closure | 369, depth 6 | 3.8× |

**And the unexpected half:** under a second, equally defensible edge definition the boundary is **not
complete even at hop 1**. 44 objects directly related to an owned object are **not carried** — including
a withholding-tax object, a fiscal-position object, a price-list object and a payment-method-line object,
all financially material. Conversely 51 carried boundary objects are not outbound-related to any owned
object. **The two definitions overlap on 39.**

> This is a defect in the *current* denominator, not only a cost estimate for a future one — and nobody
> had looked. It is the strongest evidence in this package that `BOSS-DEC-10` could not have been
> decided when it was proposed.

### `LESA4-F-06` — WHAT ACTIVATES it, and what happens when it stops
All 39 optional subjects now have **both halves** established. The structural result:
**module deactivation destroys schema and stored values; capability-switch deactivation does neither.**
40 tables and **278 columns on models the modules do not own** are destroyed across the 25 modules;
**not one of the 25 is safe.**

### `LESA4-F-07` — WHAT HIDDEN BEHAVIOUR exists: four cases where effects outlive the subject
FEFO silently degrading to FIFO with no error and no log · landed-cost value persisting while its
provenance is destroyed · a completion gate disappearing with its module · an uninstall path that
swallows its own failure in a bare catch-all.

### `LESA4-F-08` — WHAT MODULES it affects: 220 override sites
Every one of the 25 optional modules overrides at least one method on a model it does not own; **31 are
create/write/delete-level.** The concentration is on the transfer-completion path, where three subjects
override the pre-completion hook. **Whether a transfer can be completed depends on which optional
modules are installed.**

### `LESA4-F-09` — the unreconciled denominator, resolved
14,441 is every movement row; 3,680 is the completed subset. **Both prior figures were right; a column
heading was wrong.** The retraction that rested on 3,680 stands unchanged.

### `LESA4-F-10` — a false zero caused by the register's own vocabulary
**Five of the fourteen capability-group subjects were recorded in the register as settings-field names
rather than group identifiers.** Any search keyed on the register's own strings returns a **false zero**
for those five. The true identifiers were read from the security declaration. This is the vocabulary
defect that cost this programme a published finding two rounds ago, found again — this time in the
register rather than in a search term.

### `LESA4-F-11` — an internal contradiction in the register, reported rather than reconciled
**60 rows are classified optional yet record no activation condition.** No activation condition means no
deactivation condition, so these cannot meet the §8 standard. **Recorded as a defect and left visible**,
not quietly repaired — the repair would change a population, and populations change only through a new
version with a documented delta.

## 3. Items LESA could NOT resolve, with the exact limitation

| Item | Why not resolvable now | What would settle it |
|------|------------------------|----------------------|
| Whether any deactivation has fired on a real deployment | source semantics only; no module-state history was extracted | module state history + a column-existence check |
| 704 relational field sites (8.7%) whose target is supplied dynamically | statically unresolvable | a loaded-registry dump |
| Which cause produced the 1,249 zero-valued completed movements | needs per-product cost history | one extraction, next round |
| Where the current generation's inventory→accounting link runs, if it runs | three routes exhausted, all null | the accounting entry population itself |
| The 1,144 items with no possible element record | a method and a view sub-element are not database records | controlled execution or log evidence |

**Every one is a bounded measurement with a named instrument. None is a Boss question, and none is
recorded as one.**

## 4. LESA statement

Eleven open items resolved by measurement; five of them had been proposed as Boss decisions and are
**withdrawn**. Five remain genuinely open and each names its instrument.

**Not one unresolved technical fact is carried upward in this package.**
