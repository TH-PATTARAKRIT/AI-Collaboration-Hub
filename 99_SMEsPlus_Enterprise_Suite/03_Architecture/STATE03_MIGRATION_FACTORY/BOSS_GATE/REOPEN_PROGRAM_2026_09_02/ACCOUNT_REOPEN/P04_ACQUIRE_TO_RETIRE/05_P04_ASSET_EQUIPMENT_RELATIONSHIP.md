# 05 — P04 ASSET AND EQUIPMENT RELATIONSHIP

Layer: **2 — audit quarantine**.

Prior packages established the shape of this relationship. This file **imports**
that work, re-verifies the three claims that gate P04, and adds what is new.

---

## 1. Imported from prior evidence — not re-derived

| Imported finding | Source | Re-verified this session? |
|------------------|--------|---------------------------|
| No native equipment-to-asset link exists in the reference product | P2, upgraded there from SUPPORTED INTERPRETATION to FACT VERIFIED by exhaustive search | **Yes** — see §2 |
| The routing operation carries a work-centre reference and **no equipment field** | P2 / P3 | **Yes** — see §3 |
| Equipment references a work centre, many-to-one | P3 refinement of P2 | Yes |
| The project's custom asset-to-equipment link has three of four intended behaviours inert | P2, widened by P3 | **Yes, and corrected** — see §4 |
| Work-centre cost is logged duration × a single scalar rate; the model answers "how much machine cost" and cannot answer "which machine" | P3, `BD-03` structurally vindicated | Yes |
| A maintenance request carries **no monetary field of any kind** | P2 `REV-03` | Not re-tested this session |

## 2. Re-verification of the native-link negative

| Element | Declaration |
|---------|-------------|
| POPULATION | Every installable module in the reference build |
| PATTERN | `grep -rlE "['\"]account\.asset" --include='*.py'` and the manifest-dependency sweep |
| PATH SET | The reference addons root, full depth |
| UNIT | One module referencing the asset model |

**Result: three modules** — the asset module itself, the loans module, and the
project–asset bridge. None of them is an equipment or maintenance module.

> **P04-F-35.** The negative stands: **no equipment-to-asset link is found in
> the reference product** under the declared pattern and path set.
> Class: **FACT VERIFIED (scoped negative).**

### 2.1 A correction to the population figure this programme has been quoting

Prior packages state the reference population as **797 modules** — the phrase
appears in **22 files across the two source-based packages** — 10 and 12 —
once carrying the classification `FACT VERIFIED (negative)`. Two independent research streams in
this session repeated it. Executed directly this session:

| Measure | Count |
|---------|-------|
| Entries in the addons root (as a directory listing reports them) | **797** |
| Of which are **directories** | **791** |
| Of which carry a module manifest — the **installable-module population** | **790** |

> **P04-F-36.** The figure `797` is an **entry count**, not a module count. The
> installable-module population is **790**.
> The root holds **791 directories and 7 non-directory entries** — a licence, a
> readme, a contributing guide, a copyright notice, a package initialiser, a
> stray temporary write artefact, and a platform metadata dotfile. A listing that
> hides dotfiles reports 797 of those 798 entries, which is where `797` comes
> from.
> The one directory of 791 carrying **no manifest** is a web-integration module
> reduced to an empty translation folder. The 790 figure excludes it; the
> exclusion is stated rather than silent.
> Class: **FACT VERIFIED.**

The correction does not change any negative finding — the search covered the
whole tree either way. It is recorded because this programme's standing rule is
that a denominator may not be author-chosen, and `797` has been repeated as a
population across two packages and two research streams without being executed. The stray temporary write
artefact is separately noted as an **evidence-root integrity observation**:
something has written into the reference tree. Registered **P04-B-26**.

## 3. The operation-to-equipment gap, re-verified

| Element | Declaration |
|---------|-------------|
| PATTERN | Full field-set read of the routing-operation model, plus `grep -rn "equipment"` over the manufacturing and work-order model packages |
| PATH SET | The manufacturing modules of the reference build |

**Result, corrected after independent challenge.** The routing-operation model
declares **22** fields in its base definition, and **four** modules inherit it,
adding **4** more — a registration flag, two quality-point fields and an employee
ratio. The full field set is therefore **26**, and **none of the 26 is an
equipment reference**. All four inheritors were read.

The earlier statement that the model declares 20 fields was a **count of one
file that did not follow the inheritors** — under-scoped in exactly the way this
package's own rule targets.

The equipment keyword does **not** return zero hits across the manufacturing and
work-order model packages: it returns **one**, in the help text of an
effectiveness metric on the work-centre model (*"Overall Equipment
Effectiveness"*). It is prose, not a field and not a reference. The corrected
negative is: **no equipment field or reference exists on the routing-operation
model or anywhere in the manufacturing and work-order model packages**; the sole
textual occurrence is a help string.

The only equipment link found anywhere in the manufacturing area is
**equipment → work centre**, declared by a maintenance-manufacturing bridge —
never equipment → operation, and never equipment → asset.

> **P04-F-37.** The relationship chain is
> `asset ✗ equipment → work centre ← operation`.
> The break is on the **asset side**, and a second break — operation to
> equipment — sits immediately after it. The Boss's "toll gate" concern remains
> structurally correct on re-verification.
> Class: **FACT VERIFIED.** Supports **BD-03**.

## 4. The custom link — corrected, and widened again

The project's custom equipment-sequence module adds an equipment reference to
the asset. Its import chain was read in full this session.

| Element | Status | Change from prior evidence |
|---------|--------|----------------------------|
| Package initialiser imports the model package **only** | live | unchanged |
| The **wizard package is never imported** | **DEAD** | unchanged — the override that would retire the equipment when its asset is sold does not execute |
| Model package imports **five of eight** model files | — | P3 corrected P2 from one unimported file to two; **this session counts three unimported** |
| Several view files and a sequence data file are **absent from the manifest data list** | **DEAD** | as P3 |
| The confirm override, which stamps a status onto the linked equipment | **LIVE**, no accounting effect | unchanged |
| A legacy-generation model file inheriting a model name that does not exist in this generation | **DEAD** | unchanged |

> **P04-F-38.** Re-confirmed and stated for P04: **retiring an asset does not
> retire its equipment.** The retire-end divergence between the accounting
> register and the operational register is the mirror image of the acquire-end
> divergence in `01` §4.4.
> Class: **FACT VERIFIED.**

## 5. What is new: a **second** custom module that creates equipment from stock

Prior packages identified one custom module creating equipment records on goods
receipt. A second exists.

| Module | Trigger | Creates | Accounting link |
|--------|---------|---------|-----------------|
| Equipment-sequence (already known) | Receipt validation, for serial-tracked products flagged as equipment | an equipment record | **none** |
| **Equipment-product-stock (new to this session)** | Inventory/stock validation, for serial-numbered products; carries an initialisation hook | an equipment record | **none — the module contains no accounting reference at all** |

The second module additionally forces any product flagged as equipment to a
**non-storable** type with serial tracking — **but only in the form**: the
forcing is an on-change handler, so an import, script or programmatic write sets
the equipment flag **without it firing**, leaving a product flagged as equipment
and still storable and untracked (`01` §6A.12, `P04-F-108`). This is the same
UI-enforced-only pattern as the three depreciation values at `01` §3, in a second
and unrelated module, and it holds in **both** distinct source trees of this
module that exist on this host. A non-storable product is excluded
from inventory valuation entirely and fails the cost-of-goods eligibility test,
so its vendor bill line keeps a **plain expense account**.

> **P04-F-39.** A product flagged as equipment is forced to a type that
> **cannot** land on a capitalizable account through the normal product →
> category → account chain. Combined with `01` §3 — where the capitalization
> designation lives only on the account — this means the estate's own equipment
> flag pushes an item **away from** capitalization rather than towards it.
> Class: **FACT VERIFIED.** Severity **High** for the acquire-end design.

> **P04-F-40.** There are now **two** custom paths creating equipment from stock
> operations and **zero** creating or linking an asset. Buying a machine creates
> two records by two paths that never meet — and the count of unmeeting paths is
> larger than previously recorded.
> Class: **FACT VERIFIED.**

## 6. A contradiction between parallel research streams, and its ruling

Three independent enumerations of the **same** custom-addon population were
performed this session. They disagreed.

| Stream | Reported population | Reported asset-touching custom modules |
|--------|--------------------|-----------------------------------------|
| Stream A | 60 | 2 (equipment-sequence; advance-expense, manifest only) |
| Stream B | 46 | **0 — "no custom module touches the asset domain"** |
| **Direct execution (this session, authoritative)** | **68 entries / 65 directories** | **2**, identical to stream A |

**Ruling.** Stream B's negative is **CONTRADICTED** by direct execution. The
asset-touching custom modules are the two named by stream A, confirmed by five
distinct file hits in the equipment-sequence module and one manifest dependency
in the advance-expense module. Three further hits are documentation files and
are false positives.

> **P04-F-41.** Three independent enumerations of one population produced three
> different denominators — 60, 46 and 65 — and one produced a **false
> negative on a load-bearing question**. The population that resolved the
> disagreement was obtained by executing the count, not by reading a report.
> Class: **FACT VERIFIED.**

This is the programme's own denominator-completeness rule reproducing itself
under controlled conditions. It is recorded here rather than quietly corrected,
because the governing constitution requires contradictions to be preserved, and
because it is direct evidence for the standing lesson that **independent
verification is the only control that catches this class of defect**. Carried to
`12_P04_CONTRADICTION_REGISTER.md` as `P04-CTR-01` and to `16_P04_AAS_PLUS.md`.
