# VDR_FRAMEWORK_PILOT_CORRECTION_REGISTER.md
# Framework Self-Correction Register (Preparation Framework §17)

Session `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]` · **LAYER 1 — CLEAN-ROOM**
Effective version: **Universal VDR Framework v1.0**, incorporating all corrections below.

---

## 1. Rule

> **Do not preserve a defective framework merely because it was previously approved.**

Every row records: the original rule, what the Pilot found, why the original was wrong, the
correction, the evidence, the impact, and the version from which the correction is effective.
Corrections are **already incorporated** in the frozen Preparation Control documents; this register is
the audit trail, not a to-do list.

Two classes are recorded and they are not the same thing:
- **FRAMEWORK corrections (F-01..F-06, F-14..F-20)** — the method was wrong.
- **INSTRUMENT corrections (F-07..F-13)** — the method was right and the tool could not execute it.

The second class is recorded because a framework that reports only its method and not its tooling
cannot be audited: **six of the seven instrument defects produced plausible, non-zero, internally
consistent numbers.**

---

## 2. Framework corrections

### CORR-F-01 — Execution order began too late
| | |
|---|---|
| **Original rule** | `LESA → Source Learning Population → Point-Focus VDR → …` |
| **Finding** | LESA cannot say what exists until the evidence base exists. This session's first two sweeps disagreed with each other (36 vs 40 roots, then 50), and the first chosen comparator was a localisation-stripped build. |
| **Why the original was wrong** | It permitted a domain to be researched before anyone had established *what evidence exists and of which generation*. |
| **Correction** | New **Step 0 — EVIDENCE BASE ESTABLISHMENT** precedes LESA: sweep the path set, fix each root's generation by a content discriminator, declare exclusions, census runtime evidence or prove its absence. |
| **Evidence** | `00A_EVIDENCE_BASE_AND_PATH_SET.md` §2–§5; source resolution `SR-05`, `SR-07` |
| **Impact** | Would have prevented a contaminated cross-generation delta and an incomplete path set |
| **Effective** | v1.0 |

### CORR-F-02 — Challenge could open on a moving package
| | |
|---|---|
| **Original rule** | `Registers → Coverage → SMEs Core Challenge` |
| **Finding** | Nothing in the sequence froze the package. A challenger cannot cite what may change under them. |
| **Correction** | New **Step 6 — PACKAGE FREEZE**: commit recorded, manifest hashed, challenge opens against that identifier only. |
| **Evidence** | `VDR_EXECUTION_ORDER.md` §1 |
| **Impact** | Makes every challenge finding attributable to an exact package state |
| **Effective** | v1.0 |

### CORR-F-03 — The Master List had no ownership concept
| | |
|---|---|
| **Original rule** | Schema fields 1–37 as prescribed; module scope derived from the object family |
| **Finding** | Treating universally-extended shared objects as owned expands the module set **100 → 445 in one step**; relational closure to fixpoint reaches **1,559 objects / 1,071 modules** — the whole system. |
| **Why the original was wrong** | Without an ownership distinction, any domain population is either arbitrarily truncated or degenerate. |
| **Correction** | Mandatory field **`Ownership Class`** (`OWNED` / `SHARED-CONSUMED` / `SHARED-EXTENDED` / `EXTERNAL`). **Only `OWNED` items expand the module set.** |
| **Evidence** | `00_SOURCE_LEARNING_MASTER_LIST.md` §7 (iteration table); `00B` §2 |
| **Impact** | Makes a domain population reproducible; makes the boundary auditable |
| **Effective** | v1.0 |

### CORR-F-04 — The Action field assumed one-hop resolution
| | |
|---|---|
| **Original rule** | Record the `Action` for each menu |
| **Finding** | 7 of 62 menus — including the three primary operational entry points — need **three hops** to reach their target, and the intermediate hop is executable code. |
| **Correction** | The `Action` field must record the **resolution hops**, and a menu whose target is only reachable through code is flagged as such. |
| **Evidence** | Register 01 `MM-F-01`; `hop2_resolution.json` |
| **Impact** | Prevents a menu→object map that is silently blind to its most important rows |
| **Effective** | v1.0 |

### CORR-F-05 — Evidence pointers carried no generation
| | |
|---|---|
| **Original rule** | `Source Location` + `Evidence Pointer` |
| **Finding** | A directory named for one series contains another series' code; every module manifest in every located root declares the same version string. **Neither path nor manifest is a discriminator.** |
| **Correction** | Mandatory field **`Generation Basis`**, established by a **content** discriminator and recorded beside every pointer. |
| **Evidence** | `00A` §3, finding `EB-01` |
| **Impact** | Makes source findings correctly bounded instead of silently mis-attributed |
| **Effective** | v1.0 |

### CORR-F-06 — Severity was assumed to be knowable from source
| | |
|---|---|
| **Original rule** | Criticality assigned per Learning Item |
| **Finding** | Whether a behaviour can fire on any real deployment is not knowable from source. This session established **no** runtime evidence, so nothing in it is ranked by reachability. |
| **Correction** | Mandatory field **`Reachability`** (`LATENT` / `LIVE` / `UNMEASURED`), and `CRITICAL` is redefined as *"governs a Critical Area"*, never *"observed to occur"*. |
| **Evidence** | Register 09 §5; `GAP-INV-09` |
| **Impact** | Stops structural severity being read as empirical severity |
| **Effective** | v1.0 |

### CORR-F-14 — The challenge checklist had no instrument, denominator, authority, boundary or generation classes
| | |
|---|---|
| **Finding** | All 25 original questions are about **content**. Six of the seven instrument defects in §3 below would have passed all 25. |
| **Correction** | Five mandatory classes added: **26 Instrument · 27 Denominator · 28 Decision-authority · 29 Boundary · 30 Generation.** |
| **Evidence** | `SMES_CORE_CHALLENGE_CHECKLIST.md` §3.G |
| **Effective** | v1.0 |

### CORR-F-15 — The register set had no place for a domain's menus outside its own application
| | |
|---|---|
| **Finding** | The Inventory module set contributes **134** menus to *other* applications against **62** in its own — 68.4% of the surface it owns. |
| **Correction** | New Learning Item class **`MENUX`**, mandatory in Register 01. |
| **Evidence** | Register 01 `MM-F-06` |
| **Effective** | v1.0 |

### CORR-F-16 — "Feature toggle" was modelled as one mechanism
| | |
|---|---|
| **Finding** | Five mechanisms exist, differing in where state lives, who may change it, what audit exists and what scope applies. The largest class (58.2%) stores state on a **different object** from the screen. |
| **Correction** | Register 03 must classify every toggle **A–E** and record where the state lives. |
| **Evidence** | Register 03 `FT-F-01`, `FT-F-03` |
| **Effective** | v1.0 |

### CORR-F-17 — Coverage could be published without instrument validation
| | |
|---|---|
| **Finding** | Seven instrument defects; six produced plausible numbers. |
| **Correction** | Controls **I1 second-shape · I2 positive control · I3 coverage assertion · I4 zero re-test** are mandatory for every extractor contributing to a published count. |
| **Evidence** | `VDR_COVERAGE_RULE.md` §3; `00B` §4–§5 |
| **Effective** | v1.0 |

### CORR-F-18 — A blind spot could be declared without being sized
| | |
|---|---|
| **Finding** | "There may be more" is not a declaration and cannot be audited. |
| **Correction** | Every declared blind spot must state its size **or explicitly state that its size is unknown**. Four are so recorded for the Pilot; two carry the word **unmeasured** deliberately. |
| **Evidence** | `00B` §6 |
| **Effective** | v1.0 |

### CORR-F-19 — A single sweep was treated as a complete sweep
| | |
|---|---|
| **Finding** | Two sweeps of the same host returned different root sets. **Their disagreement was the only signal that either was incomplete**; each alone reported success. |
| **Correction** | An evidence-base sweep must be run **twice with different reach** (different roots, different depth) and the difference reconciled before the path set is declared. |
| **Evidence** | `SR-07` |
| **Effective** | v1.0 |

### CORR-F-20 — Menu coverage and function coverage shared a denominator
| | |
|---|---|
| **Finding** | The menu instrument identifies **13** contributing modules for this domain; the object instrument identifies **99** over the same root and generation — **7.6x**. |
| **Correction** | Menu, configuration, feature-toggle, function, object, cross-module, automation, security and edge coverage are **separate dimensions with separate denominators** and are never collapsed into one figure. |
| **Evidence** | `VDR_COVERAGE_RULE.md` §7.1; `INVENTORY_PILOT_COVERAGE_REPORT.md` §2.3 |
| **Effective** | v1.0 |

### CORR-F-21 — The register set had no effect surface other than the screen
| | |
|---|---|
| **Original rule** | Register 02 records configuration dependency; Register 03 records toggles. Both were populated from screen elements. |
| **Finding** | **7 of 21 group-toggles take effect nowhere on screen** — 4 in printed/report templates, 3 in runtime code branches (one of which also reaches a boundary object). A screen-element census cannot see any of them. |
| **Why the original was wrong** | It equated *configuration-dependent behaviour* with *configuration-dependent UI*. Printed documents are a user-visible, legally significant output surface, and code branches are behaviour with no declarative trace at all. |
| **Correction** | Registers 02 and 03 must enumerate **four** effect surfaces: screen element · **printed/report template** · **runtime code test** · **boundary-object surface**, and record which applies to each toggle. |
| **Evidence** | Register 02 `CD-F-03`; Register 03 `FT-F-07`; `SR-08` |
| **Impact** | Raises toggle→effect resolution for the Pilot from 66.7% to 100% and adds a permanently missing dimension |
| **Effective** | v1.0 |

---

## 3. Instrument corrections

| ID | Defect | Wrong result it produced | Corrected result | How it was caught |
|----|--------|--------------------------|------------------|-------------------|
| `CORR-F-07` | Visibility gating read on two element kinds only | **87** gated elements, 14 groups — plausible, non-zero, internally consistent | **633** gated elements, 43 groups, 12 element kinds | Asking whether the predicate could reach what it claimed to count (I3) |
| `CORR-F-08` | Constraint pattern matched a declaration form absent in the target generation | **0** constraints | **32** constraints | Mandatory zero re-test (I4) |
| `CORR-F-09` | Inbound cross-module edges searched only inside the domain's own modules | every inbound dependency invisible | 68 external objects referencing the domain | Asking who *declares* an inbound edge |
| `CORR-F-10` | Object-selection filter partly keyed on **module name** rather than on the declaration | 148 action rows, 29 of them included for a reason unrelated to the claim | **201** rows selected by declaration | Population instrument ≠ claim instrument (challenge class 27) |
| `CORR-F-11` | Identifier resolved by string transform instead of lookup against the declared-object census | **12** row-level rules | **28** row-level rules | Second-shape count (I1) disagreeing |
| `CORR-F-12` | Population file serialised a detail column by truncating serialised text | every long row unparseable downstream | 0 unparseable rows of 4,339 | Attempting to consume the package's own output |
| `CORR-F-13` | Lifecycle-state extraction read keyword-form declarations only | 13 of 14 state vocabularies empty | 14 of 14 extracted | Noticing a field that must have values reporting none |

**All seven were found and repaired before the package was frozen.**

---

## 4. What the Pilot could NOT correct

| Open framework weakness | Why it remains open |
|-------------------------|---------------------|
| The framework has been exercised on **one** domain of **one** shape | A master-data subject or a financial subject would exercise different failure modes. Not closable within this session. |
| The **Reachability** dimension (`CORR-F-06`) has never been executed | Requires a runtime evidence base; `GAP-INV-09`. The field exists in the schema and has never been populated with anything but `UNMEASURED`. |
| The **peer-exchange** control has not been applied | Self-challenge and independent adversarial challenge were both run. Peer exchange — a differently-biased party running the same method — is a third, non-substitutable control and is outside this session. |

These are stated as framework limitations, not as Pilot findings, and they are the substance of the
readiness shortfall in `VDR_PREPARATION_FINAL_READINESS_REPORT.md`.
