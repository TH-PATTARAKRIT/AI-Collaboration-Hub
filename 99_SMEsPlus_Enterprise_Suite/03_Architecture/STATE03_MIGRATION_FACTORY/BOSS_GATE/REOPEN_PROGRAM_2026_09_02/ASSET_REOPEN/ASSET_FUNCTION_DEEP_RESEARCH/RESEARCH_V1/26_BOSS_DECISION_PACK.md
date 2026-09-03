# 26 — Boss Decision Pack

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `FOR BOSS REVIEW — BOSS IS SOLE FINAL APPROVER OF EVERY ITEM BELOW`

---

## 1. FACT VERIFIED Items (highest confidence, safe to build on)

- Reference-ERP depreciation-method mechanics (straight-line, declining, declining-then-straight-line) — file `03`, `07`.
- Prorata computation options exist, including a days-based option — file `07`.
- Residual/Not-Depreciable Value structurally excluded from the depreciable base, both in the reference ERP and under IAS 16 — file `09`.
- Work Center cost-per-hour mechanism (per-workcenter/per-employee rates, precedence) — file `12`.
- No native Equipment↔Asset link exists in reference-ERP documentation (a verified *absence*, materially useful for planning) — file `04`, `11`.
- No documented maintenance-cost-to-production-cost integration exists (a verified *absence*) — file `06`, `12`.
- IAS 16 depreciation-stops-at-full-depreciation-or-derecognition rule — file `10`, `15`.

## 2. Boss Hypotheses — Supported vs. Contradicted

| Hypothesis | Status |
|---|---|
| A (active depreciation → production cost) | `CONTRADICTED` as an assumption of existing precedent; `DESIGN CANDIDATE` as original construction, subject to an unaddressed IAS 2 normal-capacity constraint (file `21` BA-02, file `25` P06) |
| B (single allocation driver) | `DESIGN CANDIDATE`, only partially analogous to reference-ERP evidence (file `21` BA-03) |
| C (fully depreciated asset may carry non-zero internal usage cost) | `DESIGN CANDIDATE`, sound as management accounting, correctly excluded from statutory accounting (file `21` BA-04) |
| Post-depreciation formula | `DESIGN CANDIDATE`, base-value choice unresolved among 5 options (file `13`, `21` BA-05) |
| Continuous residual usage | `DESIGN CANDIDATE`, termination condition (UE-29) and usage-vs-time-basis (file `21` BA-06) both undecided |
| Off-balance accounting model | `DESIGN CANDIDATE`, reference-ERP precedent search incomplete (UE-26) |
| Asset-Model target control point | `DESIGN CANDIDATE`, inheritance mechanics unconfirmed (UE-19) |
| "Thai depreciation uses daily calculation" (factual claim) | `SUPPORTED INTERPRETATION`, not `FACT VERIFIED` — primary source not read (file `08`, `21` BA-01) |

## 3. Unresolved Items (see file `24` for full register — 29 items, 4 `BLOCKING`)

The four `BLOCKING` items: native Equipment↔Asset link existence (UE-01); any maintenance-cost-to-production-cost linkage in unsearched editions/modules (UE-07); Asset Model→Asset inheritance/effective-dating mechanics (UE-19); the Royal Decree number for Thai depreciation caps (UE-20).

## 4. Accounting Risks

- Absorbing depreciation into product cost without an idle/normal-capacity carve-out (Hypothesis A as currently stated) risks overstating product cost during low-utilization periods, contrary to IAS 2's normal-capacity principle (file `15`, `25` P06).
- Off-balance internal usage costing, if implemented loosely, risks accidental statutory contamination (file `14`, `25` P08).

## 5. Thai Tax Risks

- Citing an unconfirmed Royal Decree number in any compliance-facing SMEsPlus documentation is a credibility/compliance-review risk until UE-20 is resolved (file `16`, `20` CR-03).
- Building a day-precision-only tax depreciation engine before confirming the exact day-count convention and confirming daily calculation actually applies to the accounting books (not just tax) risks over- or under-engineering (file `08`, `16`).
- Disposal-related deductibility documentation requirements and gain-on-disposal tax treatment are both `HOLD` — SMEsPlus should not assume a specific treatment without Revenue Department confirmation (file `16`).

## 6. Architecture Risks

- The single most consequential architecture risk in this package: **the Asset↔Equipment↔Work Center chain does not exist today in any reference-ERP precedent** (file `11`, `19`). Every downstream hypothesis (A, B, C, the post-depreciation formula) depends on this chain existing. Building it is necessary regardless of which hypotheses the Boss ultimately approves.
- Single-engine vs. dual-schedule (book vs. tax depreciation) architecture decision is open (file `25` P10) and has significant downstream implications if decided late.

## 7. Costing Risks

- No confirmed distinct per-Equipment cost field separate from Work Center rate (file `12`) — if SMEsPlus needs per-machine depreciation attribution (which Hypothesis A implies), this is a gap requiring new design, not configuration of an existing field.
- The post-depreciation formula's base-value choice (5 candidates, file `13` §3) materially changes the resulting cost figure — this is not a rounding-level decision, it changes the answer by potentially large margins depending on how much of original cost was residual.

## 8. Audit Risks

- No confirmed audit-trail mechanism for the reference ERP's "Product Revaluation"-style manual corrections generalizes to this domain — any SMEsPlus Modify-Depreciation-equivalent action needs its own purpose-built audit trail (who, when, why, old value, new value), which this package did not confirm the reference ERP provides beyond the bare fact that an entry posts (file `07` UE-13).
- Off-balance entries, being outside statutory audit scope by design, need their own internal audit discipline (file `14` §4) so they are not later mistaken for, or omitted from, an internal controls review.

## 9. SaaS Risks

- Multi-company/multi-tenant scoping of the asset-model-equivalent record is unconfirmed (UE-18) — material for a multi-tenant SaaS product where cross-tenant data leakage via a shared template record would be a serious defect.
- Effective-dating/versioning of Asset Model policy changes (UE-19) is more consequential in a SaaS context where many tenants might share upgrade timing — a retroactive-change bug would affect many customers simultaneously if not isolated per-tenant correctly.

## 10. Options Where Material Choices Remain Open

**OPTION A — Minimal, statutory-only scope for this reopen cycle.** Build Asset Model/Asset/depreciation-engine mechanics only (the best-evidenced area, file `03`/`07`/`09`), defer Equipment↔Asset linkage, Hypotheses A/B/C, and the off-balance mechanism to a later cycle once the `BLOCKING` unresolved items are closed. Lowest risk, slowest to deliver the Boss's full stated intent.

**OPTION B — Full scope, but with all `DESIGN CANDIDATE` items explicitly flagged as such in the shipped architecture (not silently treated as decided), and the four `BLOCKING` unresolved items assigned as directed follow-up research before implementation of the specific principles they gate (P01/P03, P02/P10, P06 per file `25` §3).** Matches the Boss's stated ambition, carries the risk profile in §4–§9 above, mitigated by explicit tracking.

**OPTION C — Full scope, live-instance verification pass first.** Before any SMEsPlus implementation, obtain access to a live reference-ERP instance (even a free/community trial) to directly test the `UNRESOLVED` items in file `24`, converting as many as possible to `FACT VERIFIED` or `CONTRADICTED` before design proceeds. Highest evidence quality, adds a research cycle before implementation begins.

## 11. AAS+ Recommendation

Per file `25`, AAS+ does not rubber-stamp any principle and recommends **Option C**, or at minimum **Option B with the four `BLOCKING` items in file `24` §3 treated as hard prerequisites**, given how much of this package's downstream analysis (Hypotheses A/B/C, both Cost Lineage matrices) depends on the single unconfirmed Asset↔Equipment link. **This is a recommendation only. The Boss remains the sole final approver of scope, sequencing, and every design candidate in this package. No Team B/C/D work is authorized by this file or by any part of this package.**

## 12. Jira Note

This session's Jira key was not updated. The Atlassian/Jira MCP connector is not authorized in this session — this package's findings should be manually transcribed to Jira by whoever has connector access, if the Boss wants them tracked there.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
