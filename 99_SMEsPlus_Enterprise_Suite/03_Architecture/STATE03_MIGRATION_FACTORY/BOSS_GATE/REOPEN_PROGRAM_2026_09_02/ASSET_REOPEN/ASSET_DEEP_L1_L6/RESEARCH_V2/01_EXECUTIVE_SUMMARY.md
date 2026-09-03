# 01 — EXECUTIVE SUMMARY
**LAYER 2 — AUDIT QUARANTINE**

Session `SMEPLUS-26-09-04-ASSET-DEEP-L1-L6-001` · 2026-09-04

## Terminal state

> **ASSET DEEP LEVEL 1–6 COMPLETE TO MAXIMUM AVAILABLE EVIDENCE —
> MATERIAL BLOCKERS REMAIN — READY FOR BOSS FINAL REVIEW GATE**
> (allowed terminal state **B**, §100)

Levels 1–6 were all executed. Nothing was skipped. Three items remain genuinely
undecidable on the evidence available in this session; they are listed in
`41_UNRESOLVED_EVIDENCE_REGISTER.md` and none of them blocks the *understanding*
of the Asset domain — they block specific **design** decisions.

No merge to `SMEsPlus`. No architecture-final, ready-for-development or
ready-for-production claim is made anywhere in this package.

## The single most important thing that changed this session

The previous Asset session (`SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001`, commit
`57cdb99`) recorded, as its governing constraint, that *"no code/DB access exists
for this session"*, and therefore worked from public documentation.

**That constraint was false.** This session located, in the workspace:

- the complete reference-ERP v18 Enterprise source tree (build `20250608`),
  including the entire asset module — 2,612 lines of primary Python across model
  and wizard files;
- the complete v14 legacy source tree including the project's own custom
  localisation modules;
- runtime ORM read-outs captured 2026-08-26 against the UAT database, and an
  Asset Model export captured 2026-08-27.

Every material conclusion of the prior session therefore had to be re-derived
against primary source rather than documentation. Five prior findings are
**CONFIRMED AGAIN**, four are **CORRECTED**, and two are **SUPERSEDED**. The full
trail is in `29_RESEARCH_ERROR_AND_REVISION_LOG.md`. The prior session's
conclusions are preserved verbatim there as audit lineage; nothing was rewritten
in place.

## Headline findings

### H1 — The depreciation engine has two mutually exclusive day conventions, and the Boss has been describing the wrong one for the target system. `FACT VERIFIED`

The reference ERP v18 offers three computation modes. Two of them matter:

- **Constant Periods** (the product default): a **30/360** convention. Every
  month is 30 days and every year is 360 days *regardless of the calendar*.
  February and January depreciate identically. Leap years are invisible.
- **Based on days per period**: a **true calendar-day** convention (365/366,
  real 28/29/30/31-day months), inclusive of both endpoints.

Both are implemented in the same helper, selected by one field, and they produce
materially different monthly amounts on the same asset. See
`16_DEPRECIATION_ENGINE_FORENSIC.md` §3 and `17_DAILY_DEPRECIATION_FORMULA_PROOF.md`.

An Asset Model export in the evidence set (`EV-XLS`) shows a **fourth** method
label that is not one of the three standard options (see H2). The provenance of
that export — legacy v14 or v18 UAT — could not be established from the file
itself, and this matters a great deal: see `UNR-B2`.

### H2 — "Thai daily depreciation" is a project-built custom module on the legacy system, and it has not been ported forward. `FACT VERIFIED`

The Asset Model export (`EV-XLS`) shows every listed model carrying a depreciation
method whose label is not one of the three standard options. Exhaustive search of
the workspace found exactly one definition of that label: a **custom localisation
module authored by the project's own vendor**, present only in the **v14** tree.
It computes:

> `amount_per_day = depreciable_base ÷ (actual calendar days in the whole life)`
> `period amount  = amount_per_day × actual calendar days in that period`

— which is the formula the Boss has consistently described.

There is **no v18 (or v19) copy of that module anywhere in the workspace**. Its
code calls a date field that was removed from the standard model after v14, and
it overrides a method whose signature was completely rewritten in v18. As written
it cannot run on v18.

**Consequence:** the depreciation behaviour the Boss has been describing as
"what the source system does" is, on the evidence available, a legacy-only,
project-authored behaviour. No v18 implementation of it was found in the
workspace. This is the most consequential correction in the package.

**Two things this session could NOT establish, and must not be read as settled:**

- whether the `EV-XLS` export was taken from the v14 legacy system or from the
  v18 UAT. The account codes on it match neither the target chart in `EV-HND` nor
  a chart this session could tie to a specific company, so provenance is open;
- whether a v18 port of the custom method exists **outside** this workspace (for
  example installed directly on the UAT server and never checked in). A workspace
  absence is not a server absence.

Both are recorded as `UNR-B2`. Until `UNR-B2` is answered on the running UAT, the
statement "the v18 target has no Thai day-count method" is a
**`SUPPORTED INTERPRETATION`**, not a FACT. See `26_THAI_ACCOUNTING_TAX_RESEARCH.md`
§5 and contradiction `CTR-01`.

### H3 — Thai statute does require pro-rating from acquisition, but does not itself specify *days*. `FACT VERIFIED` / `SUPPORTED INTERPRETATION`

Primary text obtained from the Revenue Department:

- Revenue Code s.65 bis (2): *"The depreciation and depletion of assets shall be
  deductible in proportion to the period from the acquisition of such assets."*
  → pro-rating from acquisition is **statutory**. `FACT VERIFIED`
- Royal Decree No. 145 (B.E. 2527) s.4 fixes **maximum** rates per asset class
  (5% durable buildings, 20% general assets, 100% temporary structures, …) and
  requires computation *"according to the period the asset was held in each
  accounting period"*, pro-rated where the period is under twelve months.
  Rates are **ceilings, not schedules**. `FACT VERIFIED`
- That the pro-ration **unit is the day** (365/366) is standard Thai practice and
  is exactly what the custom module implements — but the statutory text retrieved
  says *period* (`ระยะเวลา`), not *days* (`จำนวนวัน`). Classified
  **`SUPPORTED INTERPRETATION`**, not FACT VERIFIED. See `38` assertion `BA-02`.

This upgrades — but does not fully close — the prior session's classification of
the same Boss assertion.

### H4 — There is no native Asset↔Equipment relationship; the one in use is a custom field, and half of it is dead code. `FACT VERIFIED`

Across the entire v18 Enterprise addons tree (797 modules), the asset model is
referenced by exactly **three** modules — the asset module itself and two
unrelated finance modules. **Zero** references from maintenance, equipment,
manufacturing, stock or product. The native absence is confirmed by exhaustive
search, not inferred.

The link that *does* exist is a custom `Many2one` from Asset → Equipment added by
a project custom module. Forensics on it found three defects:

1. **No inverse and no uniqueness constraint** — N assets may point at the same
   equipment record with no error. A real data-integrity exposure.
2. The custom "on sale, deactivate the linked equipment" behaviour lives in a
   wizard file that **the module's `__init__` never imports**. It is dead code on
   v18: disposing or selling an asset leaves its equipment record active.
3. The custom display-name override uses a hook **removed after v16**; it never
   fires on v18.

See `19_ASSET_EQUIPMENT_RELATIONSHIP.md` and contradiction `CTR-02`.

### H5 — The cost lineage is not missing. Only its *first link* is missing. This reframes the SMEsPlus opportunity. `FACT VERIFIED`

The prior session reported, correctly, that no mechanism connects depreciation to
production cost. Primary-source tracing shows something more precise and much
more useful:

```
Work Center hourly rate  →  Work Order cost  →  finished move price_unit
                         →  stock valuation layer  →  FG cost  →  COGS
                         (+ a real GL entry, and analytic lines)
```

**Every link in that chain exists and is implemented.** What does not exist is the
link *into* the front of it: the hourly rate is a **static number a human types
in**, with no derivation from depreciation, and no equipment dimension at all.

So this is not "the reference ERP cannot cost production equipment". It is:
*the reference ERP costs production equipment from a hand-maintained rate, and
SMEsPlus's differentiator is to derive that rate from the asset sub-ledger.*
The absorption machinery downstream can be adopted rather than invented.

See `27_MRP_ASSET_COSTING_EXTENSION_RESEARCH.md` and `36_COST_LINEAGE_MATRIX.md`.

### H6 — The Boss's "toll gate" concern is correct, and the gap is structural. `FACT VERIFIED`

An Operation carries a Work Center and **no equipment field**. Equipment carries a
Work Center. So the model is `Operation → Work Center ← many Equipment`, and there
is no path from a job to *the specific machine it ran on*. Any allocation built on
the reference model necessarily averages across every machine in the work centre —
precisely the outcome the Boss ruled out.

`Operation → Equipment` is a **VERIFIED SOURCE GAP** and a genuine SMEsPlus
extension candidate, not an oversight in prior research.

### H7 — Maintenance cost is not merely disconnected from production. It is not recorded at all. `FACT VERIFIED`

Equipment carries a single plain `Cost` float — no currency, no account, no
analytic distribution, no link to any journal. A Maintenance Request carries a
duration in hours and **no monetary field whatsoever**. Maintenance's only effect
on production is on **capacity** (it books unavailability on the work centre
calendar), never on cost.

This is stronger than the prior session's "no mechanism flows maintenance cost to
production": there is no maintenance cost figure in the system to flow.

### H8 — Financial residual protection, which the Boss's design depends on, is confirmed by source. `FACT VERIFIED`

The not-depreciable (salvage) amount is excluded from the depreciable base at the
top of the engine, is never touched by any depreciation line, and remains in Book
Value for the whole life of a running asset. Reproduced numerically in
`40_TEST_MATRIX.md` T08/T09.

One boundary condition the Boss's design must handle explicitly: on closure the
system **removes** salvage from Book Value, and the disposal entry writes the
**full original cost** out against accumulated depreciation, so the residual is
absorbed into gain/loss rather than surviving as a separate figure. See
`18_RESIDUAL_VALUE_FORENSIC.md` §6 and `25_ASSET_SALE_DISPOSAL_RESEARCH.md`.

## What still blocks design (not understanding)

| # | Blocker | Why it blocks | Owner |
|---|---------|---------------|-------|
| `UNR-B1` | Which day convention SMEsPlus adopts as its **financial** default | Changes every schedule, every GL amount, and the migration of 280 live assets | Boss policy + Accounting-Tax track |
| `UNR-B2` | Whether the v18 UAT actually has a working Thai day-count method, and where `EV-XLS` came from | Determines whether the 280 migrated assets are being depreciated on the intended basis right now, and whether H2 is a FACT or an interpretation | Runtime verification on UAT |
| `UNR-B3` | Whether Off-Balance internal usage cost may exceed residual indefinitely | No accounting-standard precedent found; original SMEsPlus construction | Boss policy + Accounting-Tax track |

`UNR-B2` is the operationally urgent one: 217 assets are in Running state on the
UAT (`EV-RT`), and static evidence alone cannot determine which method they are
actually computing with. It is answerable in minutes on the running UAT — the
exact check is written out in `41_UNRESOLVED_EVIDENCE_REGISTER.md`.

## Coverage

See `46_CHECKPOINT_REGISTER.md` for per-level coverage and evidence counts.
