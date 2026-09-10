# VDR_OPTIONAL_FUNCTION_DEEPENING_REPORT.md
# Optional function — classified in full, deepened almost nowhere

Session `[SMEPLUS-26-09-10-VDR-PREP-003]` · Layer: **LAYER 1 — CLEAN-ROOM.**
> ### R2 correction notice
>
> **A published zero in this report was false, and the classifier that produced it had no branch capable
> of returning the class.** See §2. Two enumeration figures are also corrected. The population census
> itself — 4,097 items, four populated classes, all activation routes — reproduced exactly under
> independent challenge.
>
> Commissioning instruction §8: *"Optional Function must NOT be excluded merely because disabled in the
current default configuration."*

---

## 1. Denominator and instrument

| Clause | Value |
|--------|-------|
| **POPULATION** | frozen `POPULATION_V3`, 5,074 items |
| **ELIGIBILITY** | classes for which `OPTIONAL_FUNCTION` is applicable → **4,097** (R1: 4,100) |
| **UNIT** | one element and its activation route |
| **PATTERN** | join of the element's declaring module against the parsed dependency graph of **1,433** manifests, plus the gate census |
| **COVERAGE ASSERTION** | 4,097 of 4,097 carry a recorded class and activation route — **100%** |
| **EXCLUSION RULE APPLIED** | **none.** No element was dropped for being disabled in the default configuration — this is the §8 instruction, executed |

## 2. The six-class taxonomy, and its measured population

| Class | n | % | Population present? |
|-------|--:|--:|---------------------|
| **CORE ALWAYS-AVAILABLE** — present once the domain module is installed | 2,630 | 64.1% | yes |
| **OPTIONAL MODULE FEATURE** — requires installing a further module | 707 | 17.2% | yes |
| **CORE CONFIG-DEPENDENT** — present, but governed by a setting | 500 | 12.2% | yes |
| **OPTIONAL CORE FEATURE** — shipped in core, off until a capability is switched on | 263 | 6.4% | yes |
| **DEPRECATED / SUCCEEDED** — retained for compatibility only | **0** | 0% | **unfalsifiable — see below** |
| **VENDOR / EDITION-RESTRICTED** — present only in a restricted edition | ~~0~~ **1,411** | **34.4%** | **the R1 zero is RETRACTED** |

### `O3-F-05` — the edition-restricted zero was false, and there was no instrument behind it

**RETRACTED (`CH-05`).** R1 published *"none found in the declared path set"* as a determined absence.
Two things were wrong:

1. **The classifier had no branch that could emit the class.** The register holds exactly four
   `OPTIONAL_CLASS` values; the strings `VENDOR`, `EDITION`, `RESTRICTED` and `DEPRECATED` occur **zero
   times** in it. There was no census, because there was no instrument — the silence of a test that
   cannot run is not evidence.
2. **The zero is wrong on the merits.** Parsing the licence declaration of every resolvable domain module:

```
domain modules resolvable in the declared root : 126
licence distribution : enterprise 70 · open 55 · proprietary 1
edition-restricted   : 71 modules
population items declared inside one : 1,411  (34.4% of the applicable population)
```

**More than a third of the applicable surface sits in edition-restricted modules — inside the very tree
the zero was declared against.** The independent challenger reports 70 modules and 1,375 items, counting
the enterprise licence only; both derivations are published, and the difference is the single
proprietary-licensed module.

*(The `DEPRECATED / SUCCEEDED` zero could not be falsified — a sweep of all 126 manifests returns one
deprecation marker, outside the domain element set. But it came from the same branchless classifier, so
it is recorded as **unfalsifiable, not verified**. The distinction is the whole point of this finding.)*

**Consequence for `O3-F-01`:** the optional surface is not 23.6%. Adding the edition axis, **the share
of this domain that is unavailable in some configuration or edition is materially larger**, and the two
axes overlap in ways this session did not decompose.

## 3. Activation routes — enumerated

**25 distinct optional modules** supply 606 of the 707 optional-module elements. *R1 published 33, which
is the count of distinct activation **strings**: 8 of the 33 are not modules at all, and 101 elements
carry no module-install route (`CH-19`).* The ten largest modules:

| Activation | Elements |
|-----------|---------:|
| quality control | 101 |
| batch transfers | 99 |
| barcode | 93 |
| master production schedule | 76 |
| subcontracting | 44 |
| landed costs | 42 |
| product expiry | 38 |
| product lifecycle management | 37 |
| fleet integration | 27 |
| SMS notification | 7 |

**14 distinct capability switches** supply 243 of the 263 optional-core elements — 16 distinct activation
values, 15 of them group routes, 14 atomic groups; the remaining 20 elements are unconditional within
their module. *R1 published 12, which reproduces under no reading (`CH-19`).* Led by multi-location (75),
production lot (50), lot/serial tracking (41) and routing (25).

Optional-module elements by class: fields 275 · views 109 · gate-bearing elements 89 · buttons 84 ·
settings 57 · extension menus 39 · actions 25 · objects 13 · menus 6 · groups 5 · automations 3 ·
system parameters 2.

## 4. Findings

### `O3-F-01` — 23.6% of the applicable surface (970 of 4,100) is optional in some form.
Nearly a
quarter of what looks like "the inventory domain" is not present in a default install. Any SMEsPlus
scope derived from a default-configuration walkthrough would miss roughly one element in four. **This
is precisely the exclusion §8 forbids, and it was not applied here.**

### `O3-F-02` — landed costs (42 elements) is an optional module, and it is a valuation input.
An
element set that changes inventory value is not in the core. This matters for `CRITICAL-GAP-01` and for
Inventory Valuation: a valuation design derived only from core elements is incomplete by construction,
and the missing part is the part that adjusts cost after the fact.

### `O3-F-03` — the four largest optional modules (quality, batch, barcode, MPS: 369 elements) are operational, not financial.
The optional surface is weighted toward warehouse execution. SMEsPlus can
therefore treat a large share of this domain as genuinely deferrable — with landed costs and
subcontracting (86 elements between them) as the two that cannot be, because both touch value.

### `O3-F-04` — 40 elements classified OPTIONAL MODULE FEATURE carry the activation route "always available once the module is installed".
These are elements *inside* an optional module that are
unconditional *within* it. The distinction matters: their availability is binary at module level and
carries no further switch, so their OFF state is "module absent" — a coarser, and more disruptive,
off-state than a capability switch.

## 5. Why OPTIONAL_FUNCTION is 0.17% RESEARCH-VERIFIED (7 of 4,100)

`DETERMINED` is 100%: every element's class and activation route is established.

`RESEARCH-VERIFIED` requires the **thirteen §8 attributes**, and the one that fails almost everywhere is
**deactivation behaviour**: what happens to records already created when the capability is switched off
or the module uninstalled. Answering it needs a controlled install-then-deactivate cycle on a populated
database. **This session did not perform one, and does not claim one.** Seven settings met the bar
because their full activation and deactivation path was traced end to end.

**Classification is complete for the four classes the instrument could emit — and one of the two classes
it could not emit was not empty.** Depth is 0.17%, and this is one of only three dimensions whose
verified grade is a genuine per-item decision rather than a class label (`CH-03`).
