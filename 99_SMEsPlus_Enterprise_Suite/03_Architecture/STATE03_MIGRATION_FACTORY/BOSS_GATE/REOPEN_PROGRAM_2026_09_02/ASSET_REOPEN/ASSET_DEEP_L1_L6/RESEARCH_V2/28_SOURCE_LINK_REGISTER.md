# 28 — SOURCE LINK REGISTER
**LAYER 2 — AUDIT QUARANTINE**

Mandatory under §79. Every material source used in this session.

**Layer note:** file paths and line ranges below are Layer 2 audit evidence. They
must not be transcribed into any Team-B-facing package (`00`).

## A. Primary source code — reference ERP v18 Enterprise

| Source ID | Type | Locator | Build | Access date | Claims supported | Class |
|---|---|---|---|---|---|---|
| `SRC-01` | Primary source code | asset module — model file (≈1,230 lines) | v18 Enterprise, build 20250608 | 2026-09-04 | Field register (`04`); state machine (`23`); board engine (`16`); residual (`18`); disposal (`25`) | `FACT VERIFIED` |
| `SRC-02` | Primary source code | asset module — accounting-move extension (≈398 lines) | same | 2026-09-04 | Journal entry construction, move types, auto-creation from bills (`22`, `15`) | `FACT VERIFIED` |
| `SRC-03` | Primary source code | asset module — modify wizard (≈410 lines) | same | 2026-09-04 | The five modify actions (`24`) | `FACT VERIFIED` |
| `SRC-04` | Primary source code | asset module — account extension | same | 2026-09-04 | Account-driven asset creation flags; **off-balance exclusion** (`04` §2.5) | `FACT VERIFIED` |
| `SRC-05` | Primary source code | asset module — company extension | same | 2026-09-04 | Gain / loss accounts at company level (`25`) | `FACT VERIFIED` |
| `SRC-06` | Primary source code | asset module — asset group | same | 2026-09-04 | Grouping carries no behaviour (`02`) | `FACT VERIFIED` |
| `SRC-07` | Primary source code | asset module — views and menu data | same | 2026-09-04 | Field visibility; one menu item (`04` §1, §3) | `FACT VERIFIED` |
| `SRC-08` | Primary source code | asset module — access control file | same | 2026-09-04 | Three access grants (`02` §5) | `FACT VERIFIED` |
| `SRC-09` | Primary source code | asset module — depreciation schedule report | same | 2026-09-04 | Reporting capability (`22` §8) | `FACT VERIFIED` |
| `SRC-10` | Primary source code | maintenance module — models | same | 2026-09-04 | Equipment and request field sets; **no cost fields** (`20`, `08` §5) | `FACT VERIFIED` |
| `SRC-11` | Primary source code | manufacturing–maintenance bridge | same | 2026-09-04 | Equipment↔Work Center; maintenance blocks capacity only (`08` §5) | `FACT VERIFIED` |
| `SRC-12` | Primary source code | manufacturing — routing/operation model | same | 2026-09-04 | **Operation has no equipment field** (`08` §3) | `FACT VERIFIED` |
| `SRC-13` | Primary source code | manufacturing — work centre and work order models | same | 2026-09-04 | Hourly rate; rate snapshotting (`27` §1) | `FACT VERIFIED` |
| `SRC-14` | Primary source code | manufacturing-accounting — production, work order, work centre | same | 2026-09-04 | Cost chain links 3–6 (`27` §1) | `FACT VERIFIED` |
| `SRC-15` | Exhaustive search | the whole v18 Enterprise addons tree, 797 modules | same | 2026-09-04 | **Only three modules reference the asset model** (`08` §1) | `FACT VERIFIED` (negative) |

## B. Primary source code — project custom modules

| Source ID | Type | Locator | Version | Access date | Claims supported | Class |
|---|---|---|---|---|---|---|
| `SRC-20` | Custom source | equipment-sequence / asset-link module — asset model extension | 18.0.1.6 | 2026-09-04 | The Asset→Equipment field (`19` §2) | `FACT VERIFIED` |
| `SRC-21` | Custom source | same module — package initialiser | 18.0.1.6 | 2026-09-04 | **The wizard override is never imported** (`19` `EQ-DEF-01`) | `FACT VERIFIED` |
| `SRC-22` | Custom source | same module — wizard file (unimported) | 18.0.1.6 | 2026-09-04 | The intended disposal behaviour (`25` §5) | `CONTRADICTED` |
| `SRC-23` | Custom source | same module — equipment extension | 18.0.1.6 | 2026-09-04 | Status field, references, sequences (`20` §4) | `FACT VERIFIED` |
| `SRC-24` | Custom source | same module — inherited asset view | 18.0.1.6 | 2026-09-04 | The field targets the v18 asset model (`19` §2) | `FACT VERIFIED` |
| `SRC-25` | Custom source | same module — dead legacy file targeting a different asset model | 18.0.1.6 | 2026-09-04 | `CTR-03`; correction `REV-04` | `FACT VERIFIED` |
| `SRC-26` | Custom source | product/stock → equipment bridge module | v18 line | 2026-09-04 | The Product→Equipment route (`20` §4) | `FACT VERIFIED` |
| `SRC-27` | Custom source | **Thai straight-line depreciation module** | v14 line only | 2026-09-04 | The custom daily method (`17` §2.1) | `FACT VERIFIED` |
| `SRC-28` | Search | v18 and v19 trees, for any port of `SRC-27` | — | 2026-09-04 | **No copy found in any v18/v19-line tree in this workspace** (`H2`) | `FACT VERIFIED` (negative, workspace-bounded) |

## C. Legacy v14 source code

| Source ID | Type | Locator | Claims supported | Class |
|---|---|---|---|---|
| `SRC-30` | Primary source code | v14 standard asset module | The board loop that wraps `SRC-27`, incl. the first-period prorata factor (`17` §2.1) | `FACT VERIFIED` |
| `SRC-31` | Primary source code | v14 third-party accounting kit and community asset module, both defining a **second** asset model | `CTR-03` | `FACT VERIFIED` |

## D. Runtime and project evidence

| Source ID | Type | Locator | Date | Claims supported | Class |
|---|---|---|---|---|---|
| `EV-RT-01` | Runtime ORM read-out | UAT database `idemo18_uat`, `search_count` by company and state | 2026-08-26 | Population: 280 real assets; 16 templates; 35/217/1/27/0 by state; companies 2–4 empty (`04` §7) | `FACT VERIFIED` |
| `EV-RT-02` | Runtime ORM read-out | same, `search_read` of assets | 2026-08-26 | **All 280 have no model linked**; six distinct account triples; 35 with no accounts (`14` §5) | `FACT VERIFIED` |
| `EV-RT-03` | Runtime ORM read-out | same, external-identifier lookups | 2026-08-26 | Migration provenance of the sampled assets | `FACT VERIFIED` |
| `EV-XLS-01` | Runtime export | Asset Model export | 2026-08-27 | 16 models with method, duration and account triple; **method label is not a standard option** | `FACT VERIFIED` (content) / **provenance `UNRESOLVED`** — `UNR-02` |
| `EV-HND-01` | Project record | Asset Actual Mapping execution handoff | 2026-08-26 | Target platform and database; 16 controlled models; population counts; *"assets have no model set"*; target chart of accounts | `FACT VERIFIED` (as a project record) |

## E. Thai statutory and standards sources

| Source ID | Type | Publisher | URL | Access date | Claims supported | Class |
|---|---|---|---|---|---|---|
| `LAW-01` | Primary statute | Thai Revenue Department | https://www.rd.go.th/english/37764.html | 2026-09-04 | Revenue Code s.65 bis (2): deduction **in proportion to the period from acquisition** | `FACT VERIFIED` |
| `LAW-02` | Primary statute | Thai Revenue Department | https://www.rd.go.th/2369.html | 2026-09-04 | Royal Decree 145 s.4: computation by period held, apportioned for part periods; **maximum rates by class**; s.5 vehicle cap | `FACT VERIFIED` |
| `LAW-03` | Professional secondary | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/thailand/corporate/deductions | 2026-09-04 | Rates are **ceilings**; straight line most common; other bases permitted. **Silent on day-vs-month proration** | Secondary corroboration |
| `LAW-04` | Practice secondary | Thai ERP vendor guidance | https://www.businessplus.co.th/ (depreciation article) | 2026-09-04 | Thai practice formula: per-day = (cost − accumulated − salvage) ÷ remaining days; × days in month | Secondary; supports `SUPPORTED INTERPRETATION` only |
| `LAW-05` | Not obtained | TFAC | — | — | TAS on property, plant and equipment, Thai primary text | **`HOLD / EVIDENCE REQUIRED`** — `UNR-20` |

## F. Derived evidence

| Source ID | Type | Locator | Claims supported | Class |
|---|---|---|---|---|
| `EV-SIM-01` | Analytic reproduction | Python transcription of the v18 board algorithm from `SRC-01` | All numeric scenarios in `16`, `17`, `40` | **`SUPPORTED INTERPRETATION`** — not a runtime execution |
| `EV-SIM-02` | Analytic reproduction | Python transcription of `SRC-27` + `SRC-30` | The equivalence proof in `17` §3 | **`SUPPORTED INTERPRETATION`** |

## G. Prior session evidence, carried as lineage

| Source ID | Type | Locator | Use |
|---|---|---|---|
| `PRI-01` | Prior AI research | Session `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001`, branch `audit/asset-function-deep-research-2026-09-03-001`, commit `57cdb99`, 28 files | Re-tested in `29`. Preserved, not overwritten |

## H. Evidence NOT available this session

| Missing | Consequence |
|---|---|
| Live UAT session | 14 of the unresolved items in `41` |
| UAT installed-module list | Caps every negative finding — `UNR-04` |
| UAT build identity | `UNR-05` |
| Product documentation | **Deliberately not used.** This session worked from source only |
| TFAC primary texts | `UNR-20` |
| ~~Jira connector~~ | **Withdrawn — it was authorised.** Assumed unavailable without testing; corrected as `REV-11`. Jira record at `43` §10 |
