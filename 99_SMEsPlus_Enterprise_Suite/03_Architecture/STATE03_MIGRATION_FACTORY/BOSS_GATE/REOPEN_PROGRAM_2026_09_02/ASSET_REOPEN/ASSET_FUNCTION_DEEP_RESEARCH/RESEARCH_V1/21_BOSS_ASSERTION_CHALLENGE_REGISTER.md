# 21 — Boss Assertion Challenge Register

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `EVERY BOSS ASSERTION TREATED AS A CLAIM REQUIRING EVIDENCE, PER GOVERNING RULE #2`

---

Columns: Boss Assertion | Evidence Supporting | Evidence Contradicting | Independent Accounting View | Independent System View | Classification | Decision Required.

## BA-01 — "Thai depreciation uses daily calculation, so monthly depreciation may differ by days in month"

- **Evidence Supporting**: A secondary practitioner (SAP implementation community) source explicitly states Thai tax depreciation is computed daily on actual days-in-year (365/366); a directly retrieved Thai tax-advisory source confirms a general "proportional to period from acquisition" principle consistent with, though not identical in wording to, a daily mechanic.
- **Evidence Contradicting**: No authoritative primary source (Revenue Department text, gazetted Royal Decree) independently retrieved and read confirms "daily" as the mandated convention as opposed to a monthly-proration convention; IAS 16 (accounting side) imposes no day-count mandate at all.
- **Independent Accounting View**: A daily convention is *plausible and common* in jurisdictions with strict proration-from-acquisition-date rules, and is mechanically supported by the reference ERP's own "Based on days per period" option (file `07`), but plausibility is not verification.
- **Independent System View**: The reference-ERP asset engine treats period-interval and prorata-computation-method as two separate configuration axes — daily-equivalent granularity is available as an *option*, not necessarily the *only or default* mode, so even if Thai law requires daily computation, SMEsPlus should not assume the reference-ERP default configuration achieves it without explicit selection.
- **Classification**: `SUPPORTED INTERPRETATION`
- **Decision Required**: Boss/Accounting-Tax track to obtain and read the primary Royal Decree/Revenue Department text before this converts to `FACT VERIFIED`; until then, SMEsPlus's tax-depreciation engine should be built with day-precision *capability* (not necessarily as the sole computation path) so the design is not blocked while evidence is completed.

## BA-02 — Hypothesis A: Active depreciation flows into production cost

- **Evidence Supporting**: None from reference-ERP observation; the hypothesis is stated as approved business intent, and is directionally consistent with general cost-accounting theory (depreciation as a component of manufacturing overhead is a widely accepted practice generally, independent of any specific system).
- **Evidence Contradicting**: Files `04`, `06`, `11`, `12`, `19` converge on no documented reference-ERP mechanism connecting Asset depreciation to Work Center, Operation, or MO cost.
- **Independent Accounting View**: Depreciation-as-overhead is a legitimate and common costing treatment (consistent with the general spirit of IAS 2's production-overhead concept, file `15`), but IAS 2's normal-capacity rule constrains it — it should not be absorbed at 100% into product cost during idle/low-utilization periods without adjustment.
- **Independent System View**: No adaptable precedent exists; this is original SMEsPlus construction, not reference-ERP adaptation.
- **Classification**: `DESIGN CANDIDATE` (as business intent) / `CONTRADICTED` (as an assumption of reference-ERP precedent)
- **Decision Required**: Boss to confirm whether Hypothesis A should proceed as original design work (with the IAS 2 normal-capacity constraint incorporated) given the absence of any adaptable pattern.

## BA-03 — Hypothesis B: Single allocation driver for equipment/work-center cost absorption

- **Evidence Supporting**: The reference ERP's Work Center cost-per-hour mechanism does use a single driver concept (hours × rate) for labor/machine-time absorption, which is a structurally similar (though not identical-subject) precedent.
- **Evidence Contradicting**: No evidence the reference ERP uses, or requires, a *single* driver across multiple cost types (labor rate and machine rate are two separate configurable inputs feeding one calculation, not literally one driver) — so the precedent is partial, not a clean match for "single allocation driver" read strictly.
- **Independent Accounting View**: A single allocation driver (e.g., machine-hours) is a common, defensible simplification in cost accounting, but multiple-driver approaches (machine-hours plus a separate depreciation rate, for instance) are equally legitimate and often more accurate — no standards-level requirement favors one over the other.
- **Independent System View**: Partial structural analogy only (§ above); not a confirmed precedent for a strictly single-driver model.
- **Classification**: `DESIGN CANDIDATE`
- **Decision Required**: Boss to confirm whether "single driver" is a hard design constraint or a simplification preference; this register does not find evidence compelling either choice.

## BA-04 — Hypothesis C: Fully depreciated asset may carry non-zero internal economic usage cost

- **Evidence Supporting**: Directionally consistent with general managerial-accounting theory (opportunity cost / economic vs. accounting depreciation distinction); coherent with the Boss's own paired Off-Balance model proposal.
- **Evidence Contradicting**: IAS 16 is explicit that depreciation stops at full depreciation — no standards-level statutory mechanism supports recognizing a new expense for continued use of a fully depreciated asset.
- **Independent Accounting View**: Sound as a management-accounting concept; unsound, and correctly not attempted, as a statutory-accounting concept. See file `15` §4 boundary statement.
- **Independent System View**: No reference-ERP precedent (expected — this is not a feature category the reference ERP's documented fixed-asset module addresses).
- **Classification**: `DESIGN CANDIDATE`
- **Decision Required**: None blocking — this hypothesis is coherent as stated, provided it stays strictly off-balance (file `14`). Boss should confirm intent to proceed as management-only tooling.

## BA-05 — Post-Depreciation Internal Usage Formula (Residual Book Value × Original Depreciation Cost Rate ÷ Original Cost Base)

- **Evidence Supporting**: None — stated as Boss-approved business intent, not as an observed pattern.
- **Evidence Contradicting**: No accounting-standard or reference-ERP precedent located for this specific formula.
- **Independent Accounting View**: Internally plausible but the base-choice question (file `13` §3) is genuinely open across five candidate interpretations; no single answer is accounting-mandated.
- **Independent System View**: No system precedent; the reference ERP's own day-based prorata option (file `07`) is a useful mechanical analogy for the daily variant only, not for the base-value question.
- **Classification**: `DESIGN CANDIDATE`
- **Decision Required**: Boss decision needed among the base-value options in file `13` §3 before this formula can move to implementation.

## BA-06 — Continuous Residual Usage Hypothesis (usage cost continues indefinitely post-full-depreciation until disposal/removal)

- **Evidence Supporting**: Logically follows from Hypothesis C if accepted; no independent evidence beyond that dependency.
- **Evidence Contradicting**: None specifically found, but also not independently tested beyond the Hypothesis C analysis it depends on (file `10`).
- **Independent Accounting View**: Consistent with treating the charge as tied to continued physical use rather than to remaining book value (which, once fully depreciated, is constant) — this is itself informative for the file `13` base-choice decision, since a *constant* residual book value multiplied by a *constant* rate produces a *constant* periodic charge, which may or may not match the Boss's intent of a usage-sensitive (not time-sensitive) charge.
- **Independent System View**: No precedent.
- **Classification**: `DESIGN CANDIDATE`
- **Decision Required**: Boss to clarify whether the "continuous" charge should vary with actual usage/hours (requiring a usage/meter data source not currently confirmed to exist on Equipment, file `04`) or accrue uniformly per period regardless of usage — these are materially different designs.

## BA-07 — Off-Balance Accounting Model (Dr Internal Equipment Usage Cost / Cr Internal Equipment Usage Offset, both Off-Balance type)

- **Evidence Supporting**: Consistent in spirit with general double-entry-system "statistical"/off-balance account patterns known from general professional knowledge; not independently confirmed as a reference-ERP feature.
- **Evidence Contradicting**: This session's search for a reference-ERP analogue was narrower/time-boxed and is itself flagged as incomplete (file `14` §2) — not a strong contradiction, more an incomplete-evidence caveat.
- **Independent Accounting View**: Sound in principle provided the structural controls in file `14` §4 are implemented; unsound if implemented loosely (risk of accidental statutory contamination).
- **Independent System View**: `UNRESOLVED / EVIDENCE REQUIRED` on reference-ERP precedent.
- **Classification**: `DESIGN CANDIDATE`
- **Decision Required**: Boss to confirm the control requirements in file `14` §4 as mandatory acceptance criteria before this proceeds to design.

## BA-08 — Asset-Model Target Control Point (should Asset Model be the primary policy control point)

- **Evidence Supporting**: The reference ERP's general template/instance pattern (Asset Model → Asset) is well-established structurally elsewhere in the system (by analogy, file `03` §3), suggesting a template-level control point is a coherent design.
- **Evidence Contradicting**: The specific inheritance/override and effective-dating mechanics for the asset module were not independently re-confirmed this session (file `03` §3–§4) — the analogy is not the same as direct evidence for this module.
- **Independent Accounting View**: A template-level control point supports consistency (e.g., enforcing a Thai-compliant depreciation method/rate by asset category) but must not retroactively alter in-flight Asset schedules (file `03` §5 candidate).
- **Independent System View**: `UNRESOLVED / EVIDENCE REQUIRED` for this specific module's inheritance mechanics.
- **Classification**: `DESIGN CANDIDATE`
- **Decision Required**: Boss to confirm the copy-not-live-reference design candidate in file `03` §5 as the intended behavior.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
