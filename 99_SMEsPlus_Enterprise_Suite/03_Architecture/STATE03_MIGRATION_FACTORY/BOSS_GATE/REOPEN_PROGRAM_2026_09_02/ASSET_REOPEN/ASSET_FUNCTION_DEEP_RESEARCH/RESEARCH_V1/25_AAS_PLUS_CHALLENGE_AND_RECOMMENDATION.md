# 25 — AAS+ Challenge and Recommendation

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `EVERY PRINCIPLE CHALLENGED — NONE RUBBER-STAMPED — BOSS IS SOLE FINAL APPROVER`

---

## 1. Purpose

This file individually challenges the 10 design principles (P01–P10) referenced by the governing brief's design-hypothesis framing. Each is stress-tested against this package's evidence, not accepted by default.

## 2. Principle-by-Principle Challenge

**P01 — Asset Model is the primary policy control point for depreciation method/rate/accounts.**
Challenge: this session could not confirm the reference-ERP inheritance/effective-dating mechanics for this module (file `03` §3–§4, UE-19). Recommending Asset-Model-as-control-point without confirming whether edits retroactively affect in-flight Assets is premature. **Recommendation**: adopt the copy-not-live-reference candidate (file `03` §5) explicitly as a design decision, not as an assumed inherited behavior.

**P02 — Depreciation prorata should use days-per-period by default for Thai compliance.**
Challenge: the Thai daily-calculation claim is only `SUPPORTED INTERPRETATION` (file `08`), and forcing days-per-period as the *default* for all companies (not just Thai-regulated ones, if SMEsPlus ever serves other jurisdictions) may be premature. **Recommendation**: make it configurable per company/jurisdiction, defaulting for Thai entities only once UE-20/UE-21 are resolved, not globally.

**P03 — Equipment and Asset should be tightly, automatically linked.**
Challenge: no reference-ERP precedent exists (file `04`, `11`); this is desirable but entirely new construction, with real design cost (cardinality decisions, migration of any pre-existing Equipment/Asset records that lack the link). **Recommendation**: proceed, but budget it as a from-scratch build, not an integration task, and decide the cardinality (file `04` §3) explicitly rather than defaulting to 1:1 by assumption.

**P04 — A fully depreciated but still-productive asset may carry non-zero internal economic usage cost (Hypothesis C).**
Challenge: sound as management accounting, unsupported and correctly not attempted as statutory accounting (file `10`, `15`). The real risk is scope creep — if implementation drifts toward touching real GL accounts even partially, it violates IAS 16 outright. **Recommendation**: proceed only with the off-balance control list in file `14` §4 treated as hard, non-negotiable acceptance criteria, not aspirational guidance.

**P05 — Single allocation driver for equipment/work-center cost absorption (Hypothesis B).**
Challenge: the reference-ERP precedent is partial at best (file `21` BA-03) — it uses two configurable rate inputs (per-workcenter, per-employee) feeding one calculation, which is not quite "a single driver" in the strict sense the hypothesis implies. **Recommendation**: do not treat "single driver" as settled; explicitly decide whether SMEsPlus wants strict single-driver simplicity or a multi-input model closer to the actual reference-ERP pattern.

**P06 — Depreciation should flow into production cost as overhead (Hypothesis A).**
Challenge: this is the most evidence-thin hypothesis in the package relative to its architectural weight — zero reference-ERP precedent (file `11`, `19`), and a real accounting constraint (IAS 2 normal-capacity rule, file `15`) that the hypothesis as stated does not yet address (idle/breakdown periods, T10–T12). **Recommendation**: do not approve as stated; require the normal-capacity/idle-capacity carve-out to be designed concurrently, not bolted on later, or the resulting product costs will overstate cost during low-utilization periods.

**P07 — The post-depreciation internal usage formula's base should be the Depreciable Base (most internally consistent option per file `13`).**
Challenge: "most internally consistent" was this file's own weakest possible endorsement (file `13` §3) — it explicitly is not asserted as correct, only as one candidate with a specific, named trade-off (it reduces the formula to reproducing the historical average rate, which may not be the economic signal intended). **Recommendation**: Boss must pick from the five options in file `13` §3 with the stated trade-offs in view; this challenge file declines to pre-select one.

**P08 — Off-balance internal costing must never touch statutory accounts.**
Challenge: agreed in principle, but this session's reference-ERP precedent search for an off-balance mechanism was itself incomplete (file `14` §2, UE-26) — the control design in file `14` §4 is this file's own construction, informed by general professional double-entry-system knowledge, not verified against the reference ERP's actual (if any) implementation of the same idea. **Recommendation**: treat file `14` §4 as a starting control checklist requiring independent accounting-control review before build, not as a finished specification.

**P09 — Maintenance cost should be visible in Equipment/Work Center costing.**
Challenge: reasonable operational goal, but zero reference-ERP precedent (file `06`), and the governing brief itself frames this as something to challenge directly rather than assume — this file's evidence supports the challenge's premise (no integration exists to adopt). **Recommendation**: treat as a genuinely separate, lower-priority feature from the depreciation/off-balance work, since it has an even thinner evidence base and was investigated less deeply than the depreciation-centric objects in this package.

**P10 — Thai statutory depreciation and SMEsPlus accounting-book depreciation can share one engine with jurisdiction-specific configuration.**
Challenge: plausible given the reference ERP's own configurable prorata-method design (file `07`), but the accounting-vs-tax-depreciation divergence noted in file `16` (accounting rate must be used for tax if lower than the statutory cap) means a single-engine design must support **two independently-tracked schedules** (book and tax) reconciled at filing time, not one schedule serving both purposes interchangeably. **Recommendation**: confirm this dual-schedule requirement explicitly before committing to a single-engine architecture; a naive single-schedule design would not satisfy the Thai reconciliation requirement evidenced in file `16`.

## 3. Overall AAS+ Recommendation

None of P01–P10 is rejected outright, and none is approved as stated without qualification. Every principle carries at least one specific, evidence-grounded caveat above. The package's overall posture is: **proceed to Boss review and, where the Boss elects to continue, to a Joint design session that treats the `BLOCKING`-severity unresolved items (file `24` §3) as prerequisites for the specific principles they gate** — P01/P03 need UE-01/UE-19; P02/P10 need UE-20/UE-21; P06 needs UE-07.

**The Boss remains the sole final approver of every principle above.** This file's role is to ensure no principle reaches Boss review unchallenged, not to substitute its own judgment for the Boss's decision.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
