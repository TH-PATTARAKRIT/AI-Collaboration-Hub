# 03 — SC-02 DEFERRED REVENUE / EXPENSE EVIDENCE POINTER CHECK

| Field | Required Value |
|---|---|
| SC ID | `SC-02` |
| Decision ID | `ACC-DEC-005` |
| Topic | Deferred revenues, deferred expenses, recognition schedules |
| Source files checked | `05_ACCOUNT_SCOPE_RESEARCH_REGISTER_SC01_SC10.md` (Batch A); `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` (source pack); `12_ASSET_DEFERRED_RECOGNITION_MAP.md` (deep-study package, row `UK-04`, line 140) |
| Evidence pointer result | Verified |
| Owner status | Boss |
| Gate impact | No gate defined |
| GL impact known? | No |
| TB impact known? | No |
| BS / PL / Cash Flow / Tax Report impact known? | Unknown — deferral schedules conventionally affect BS (deferred asset/liability) and PL (recognition timing), but no source asserts a design for SMEsPlus |
| Subledger or interface impact | Deferred (per `12_ASSET_DEFERRED_RECOGNITION_MAP.md` file scope) |
| Thai menu/report communication issue | Unknown — not covered in `08_TBRAC_THAI_NAMING_VALIDATION_BRIEF.md` as read |
| AI Audit SMEsPlus objection | `10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md` §A explicitly instructs deferral-schedule research to wait for the `SC-02` scope ruling before starting — confirms this item is correctly sequenced, not stalled by omission |
| Readiness classification | `READY AFTER BOSS SCOPE DECISION` |
| Next action | Boss rules IN / OUT / DEFERRED in `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md`; if IN, feeds `10` §A (explicitly sequenced after `ACC-DEC-005`) |

## Detail

Both required registers cite "source `05` row `ACC-DEC-005`; source `12` UK-04." Source `05` resolves correctly within the required source pack. Source `12` UK-04 resolves (outside the required perimeter, as with `SC-01`) to `12_ASSET_DEFERRED_RECOGNITION_MAP.md` line 140:

> `UK-04` | Deferral design without benchmark "model" precedent (FT-07) | Original clean-room design required if in scope | Accounting Core (Team B DOMAIN_01) | UNVERIFIED (this session reading only) | No gate | `HOLD / EVIDENCE REQUIRED`

This is a direct, on-point match — it is the specific finding that no benchmark precedent exists for deferral models, so any SMEsPlus design here would need to be original clean-room work if Boss rules the item IN. The citation is real and topically correct.

`10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md` §A cross-references this item explicitly: "The deferral-schedule and fixed-asset sub-scopes should wait for `ACC-DEC-004`/`ACC-DEC-005` (SC-01/SC-02) scope rulings, since source `20` records those areas as **not yet scoped at all**." This is independent corroboration, inside a required-input file, that `SC-02`'s status and sequencing are correctly represented — no discrepancy found between the two required registers and this downstream routing file.
