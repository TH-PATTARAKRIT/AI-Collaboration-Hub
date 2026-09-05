# P01 — SOURCE LINK REGISTER

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1.** Deliberately holds no reference-system paths — those are Layer 2.

## 1. EVIDENCE CLASSES USED, RANKED

| Rank | Class | Where it lives | Used for |
|---|---|---|---|
| 1 | **Deployed database schema** | `P01_DEPLOYED_SCHEMA_EVIDENCE.md` | The clearing-account and valuation-layer absence in the v19 line; referential integrity of the chain |
| 2 | **Reference source code** | `LAYER2_EVIDENCE_QUARANTINE/E00_…` (`EV-P01-01`..`EV-P01-53`) | Everything else |
| 3 | **Independent expert reading** | `_expert_out/` (four reports) | Admitted only after re-derivation by this session; otherwise carried as SUPPORTED INTERPRETATION |
| — | *Runtime behaviour* | **not obtained** | — |
| — | *Statutory sources* | **not obtained** | — |

## 2. PROJECT EVIDENCE INHERITED, NOT RE-DERIVED

| Source | What P01 takes from it |
|---|---|
| Very Deep Research 8-Criteria Universal Exit Constitution | The exit test applied in `P01_PMO_REVIEW.md` |
| Canonical Evidence Acquisition Flow Standard | The Discover → Bound → Enumerate → Collect → Correlate → Challenge → Reproduce → Classify → Preserve sequence |
| Deep Research Negative Claim Standard | Classes A–E, used on every negative in this package |
| Scope-aware constitution correction | `P01_SCOPE_OWNERSHIP_MATRIX.md`, and the re-framing in `REV-P01-01` |
| Account Wave A track | FX rate ownership and missing-rate policy — **inherited, not decided** |
| COGS track (standing HOLD) | The prohibition on assuming a cost method survives |
| Inventory multi-tenant invariant set | The invariants against which the cross-company trigger must be tested |

## 3. WHAT A REVIEWER NEEDS IN ORDER TO REPRODUCE THIS PACKAGE

1. The five source roots, as tabulated in the Layer 2 evidence base §1.
2. The three restorable database dumps and PostgreSQL restore tooling.
3. The enumeration scripts, preserved verbatim in the Layer 2 evidence base §6 and §10.
4. The four expert reports in `_expert_out/`.

Every population in this package states its **population, unit, pattern, path set and declared
false-negative modes**. Any of them can be re-run and disagreed with. Where a count changed
during the session it is recorded in `P01_RESEARCH_ERROR_AND_REVISION_LOG.md` rather than
silently replaced.

---

# ADDENDUM — EVIDENCE BASE CORRECTED (2026-09-05)

## A.1 The evidence base was wrong about itself, and is corrected here

| Prior record | Corrected |
|---|---|
| Three readable databases, one unreadable | **Four readable.** The fourth needs a newer restore binary that was already installed on the machine (`ERR-P01-15`) |
| Two v19 deployments and one **v18** | Two v19, one **v16**, and the fourth is **v19**. **No deployed v18 exists in this estate** (`ERR-P01-09`) |
| Deployed evidence ranked above source | Unchanged — and this round shows why: every one of the eight external corrections came from the deployed layer or from reading the vendor's own design intent |

## A.2 The four databases

| Tag | Version | Installed modules | Character |
|---|---|---|---|
| `D1` | 19.0 | 251 | 44 companies; 31 orders; 14,441 movements; **16 journal entries** |
| `D2` | 19.0 | 232 | near-empty |
| `D3` | **16.0** | 190 | 5,881 orders; 103,949 movements; 183,590 journal entries |
| `D4` | 19.0 | **453** | the fullest module set; **the only one with a period lock set**; transactions **unread** |

## A.3 Reproduction — corrected

1. The five source roots as declared in the Layer 2 evidence base.
2. **All four** dumps. The fourth requires the newer restore binary; both are present at sibling
   paths under the local package manager.
3. Extraction method that works: restore a single table **to a file** — piping the restore
   output yields zero bytes — then parse the copy block.
4. **Read the version from the module registry. Never infer it from feature presence.**
5. The enumeration scripts in the Layer 2 evidence base §6 and §10.
6. The eight expert reports in `_expert_out/` and `_expert_out2/`.

## A.4 A standing instruction this round earned

> **Before recording any evidence source as unavailable, enumerate the instruments actually
> present — not the one that failed.**

`D4` was excluded for a full round on a single failed invocation, and it is the most relevant
database in the estate.

---

# ADDENDUM 2 — EVIDENCE BASE AFTER THE INTEGRITY REPAIR (2026-09-05)

## A.1 The estate, corrected

| Tag | Archives | App series | Companies | Orders | Movements | Journal entries | Modules |
|---|---|---|---|---|---|---|---|
| `E-1` | two, one estate | 19.0 | 44 | 31 | 14,441 | 16 | 251 |
| `E-2` | one | **16.0** | 1 | 5,881 | 103,949 | **183,590** | 190 |
| `E-3` | one | 19.0 | 1 | **27,879** | 55 | 10 | **453** |

**Only `E-2` exercises the full procure-to-pay chain.**

## A.2 Source roots — corrected

| Root | Series | In the original path set? | Status |
|---|---|---|---|
| v18 enterprise + archive | 18 | yes | **no deployment exists for this series** |
| v19 enterprise | 19 | yes | matches `E-1` and `E-3` |
| custom, v18 line | — | yes | |
| custom, v19 line | — | yes | |
| **custom, series-16 line** | 16 | **NO — added this round** | **is the source of `E-2`'s custom layer** — six of six versions match |
| **core, series 16** | 16 | — | **`VERIFIED ABSENCE`** — 13 core trees on the volume, 0 at series 14–17 |

## A.3 Tooling — required, and previously wrong

| Archive | Restore binary |
|---|---|
| `E-1`, `E-2` | either installed binary |
| **`E-3`** | **requires the newer binary** — it carries an archive format the older one predates |

**Method:** restore one table **to a file** and parse the copy block. Piping yields zero bytes.
**Read the version from the module registry — never infer it from feature presence.**
**Company-dependent values resolve from two places** — the per-record value **and** a
company-level defaults table. A per-record probe alone produces false zeros; that defect
falsified this package's headline cause (`ERR-P01-19`).

## A.4 Instruments that are NOT available on this platform

`timeout` is **not installed**. Any negative claim produced through a command wrapped in it is
**void**. Reported by an independent expert; recorded here so no future round repeats it.

## A.5 Standing instruction earned this round

> **Before recording an evidence source as unavailable, enumerate the instruments actually
> present. Before recording a configuration value as unset, enumerate the places that value can
> be stored in that version. Before publishing an absence, run the enumeration twice with
> patterns of different width and reconcile.**

Each clause corresponds to a specific defect this package published and then had to correct.
