# 02 — SC-01 FIXED ASSET EVIDENCE POINTER CHECK

| Field | Required Value |
|---|---|
| SC ID | `SC-01` |
| Decision ID | `ACC-DEC-004` |
| Topic | Fixed assets, depreciation, disposal |
| Source files checked | `05_ACCOUNT_SCOPE_RESEARCH_REGISTER_SC01_SC10.md` (Batch A, commit `2b54417c`); `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` (source pack, commit `1fbc64c2`); `12_ASSET_DEFERRED_RECOGNITION_MAP.md` (deep-study package, branch `audit/account-menu-process-deep-study-2026-09-02-001`, commit `5183e9f6`, row `UK-02`, line 138) |
| Evidence pointer result | Verified |
| Owner status | Boss |
| Gate impact | No gate defined |
| GL impact known? | No — no design exists; `12` UK-02 explicitly frames this as "Boss decision" pending, status `HOLD / EVIDENCE REQUIRED` |
| TB impact known? | No |
| BS / PL / Cash Flow / Tax Report impact known? | Unknown — fixed assets conventionally touch BS (asset) and PL (depreciation), but no source document asserts this for SMEsPlus; asserting it here would be this session inventing evidence |
| Subledger or interface impact | Asset (per `12_ASSET_DEFERRED_RECOGNITION_MAP.md` file scope; roll-forward research listed but not started, per `10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md` §A) |
| Thai menu/report communication issue | Unknown — no Thai naming work for this area appears in `08_TBRAC_THAI_NAMING_VALIDATION_BRIEF.md`'s scope as read |
| AI Audit SMEsPlus objection | The item is currently scope-only; no research has begun, so calling this "READY FOR RESEARCH" without a Boss IN/OUT/DEFERRED ruling risks a research team investigating an area Boss ultimately rules OUT — a resourcing objection, not a content one |
| Readiness classification | `READY AFTER BOSS SCOPE DECISION` |
| Next action | Boss rules IN / OUT / DEFERRED in `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` (source pack); if IN, feeds `10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md` §A (Fixed Asset research pass, currently `UNASSIGNED`) |

## Detail

Both required registers agree word-for-word in substance: Batch A's `05` row for `ACC-DEC-004`/`SC-01` cites "source `05` row `ACC-DEC-004`; source `12` UK-02" as its evidence location. "Source `05`" resolves correctly to the source pack's own `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` (required input, confirmed present, row matches). "Source `12` UK-02" does **not** resolve inside either required package — there is no file `12` inside the Batch A or source-routing packages that carries a row `UK-02`. Tracing it, `12` refers to `12_ASSET_DEFERRED_RECOGNITION_MAP.md` in the (non-required) deep-study package. That file's row `UK-02` (line 138) reads:

> `UK-02` | Whether Boss Section 6.7 intends fixed assets as v1 Mandatory scope for Thai SMEs | Determines whether AS-01..AS-08 need a design pass before COA-G05 taxonomy | Boss | Boss decision | No gate defined — BOSS SCOPE DECISION | `HOLD / EVIDENCE REQUIRED`

This is a topical, on-point match: it is the specific unresolved question "is fixed-asset scope IN for v1" that `SC-01` routes to Boss. The citation is real and supports the row, but it sits one layer outside this session's required source perimeter (see `01_SOURCE_PACKAGE_VERIFICATION_REGISTER.md` §B), so it is marked **Verified** with that caveat rather than treated as if it were inside the required package boundary.

No GL, TB, BS, PL, Cash Flow, or Tax Report impact statement exists anywhere in the evidence chain for this item — because no design work has started. This is consistent with, not contradictory to, "Verified": the pointer correctly verifies that the item is genuinely unresearched, not that research findings exist.
