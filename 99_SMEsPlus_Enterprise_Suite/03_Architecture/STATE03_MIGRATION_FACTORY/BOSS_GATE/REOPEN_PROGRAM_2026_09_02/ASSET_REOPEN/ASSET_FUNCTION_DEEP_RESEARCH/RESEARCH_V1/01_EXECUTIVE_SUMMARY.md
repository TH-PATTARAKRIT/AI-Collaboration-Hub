# 01 — Executive Summary

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Jira: `ERPPLUS` (update not performed — see §6) | Control scope: Asset / Asset Model / Equipment / Maintenance function-level forensic deep research

**Terminal state: `BLOCKED — MATERIAL EVIDENCE REQUIRED`**

---

## 1. What This Package Is

A function-level forensic deep research package into the Asset / Asset Model / Equipment / Maintenance domain, conducted before any SMEsPlus architecture in this domain is frozen. It is not production code, not a design freeze, and not an approval of any hypothesis it evaluates. It extracts business semantics only — never verbatim code, schema, or field names — from a publicly documented reference ERP (referred to throughout as "the reference ERP"; its public documentation covers the asset/fixed-asset, equipment/maintenance, and manufacturing-order-costing areas relevant here) and from authoritative accounting/Thai-tax sources reachable via public web research. No source code or database access existed for this session (confirmed by search — see file `00` §2), so this package leans heavily, and openly, on public documentation and secondary sourcing rather than direct system observation.

## 2. Headline Findings

1. **The reference ERP's asset engine is well-documented and internally coherent** on depreciation *method* mechanics (straight-line, declining, declining-then-straight-line; prorata via no-prorata / constant-periods / based-on-days-per-period) — see file `07`. This is the strongest evidence base in the whole package.
2. **The reference ERP does not appear to have a native, first-class Equipment↔Asset (fixed-asset) field link.** Every source located that connects the two is a community/third-party module or a forum thread proposing a customization — never an official documentation page describing a built-in field. This is a material negative finding, not a gap in this session's search effort — see file `04`, file `11`.
3. **Maintenance cost integration into Equipment/Work-Center/MO/Product cost is not evidenced as automatic** in the reference ERP's documented mechanism. Work Center hourly cost is evidenced (per-workcenter and per-employee rates feeding operation cost); no documented pathway was found by which a maintenance request's cost automatically flows into that rate or into product cost. Challenged directly, not assumed — see file `06`, file `12`.
4. **The Boss's factual claim that Thai depreciation uses daily calculation is `SUPPORTED INTERPRETATION`, not `FACT VERIFIED`.** Secondary sourcing (a SAP-implementation community discussion citing Thai business practice) asserts day-count-based (365/366) tax depreciation; a directly retrieved Thai tax-rates summary (Sherrings) confirms Royal-Decree-based maximum rates by asset category but does not itself state the daily-computation mechanic; the primary Royal Decree 145 text was not independently retrieved and read in this session. See file `08`, file `21`.
5. **The Boss-approved post-depreciation internal usage costing formula (Residual Book Value × Original Depreciation Cost Rate ÷ Original Cost Base) is correctly treated in this package as a `DESIGN CANDIDATE`, not an accounting fact** — it has no located precedent in the reference ERP's documented feature set and is not a requirement of IAS/TAS 16. It is original SMEsPlus design work. See file `13`, file `14`.
6. **A large share of the Function Matrix, Event-to-GL Matrix, and Cost Lineage Matrix cells are `UNRESOLVED / EVIDENCE REQUIRED`** because no code/DB access exists and public documentation does not reach implementation-level mechanism detail (e.g., exact journal-posting triggers, exact cardinality enforcement). This is expected and disclosed, not concealed — see file `24`.

## 3. Terminal State Reasoning

`BLOCKED — MATERIAL EVIDENCE REQUIRED` is selected over `READY FOR AAS+ INDEPENDENT CHALLENGE` because:

- The Equipment↔Asset↔Work Center cardinality question (file `11`) — foundational to the Cost Lineage Matrix (file `19`) and to Hypothesis A/B/C evaluation (files `13`–`14`) — has no confirmed reference-ERP mechanism.
- The Thai daily-depreciation assertion (file `08`) is not verified against a primary statutory source.
- Maintenance cost integration into production cost (file `06`, file `12`) is challenged and not confirmed either way with authority.
- The Unresolved Evidence Register (file `24`) is, by design and by honest count, substantial.

None of these block an AAS+ challenge session from *starting* — the package is complete and internally consistent enough to be read and contested — but they are material enough that this file does not claim readiness without flagging them as the reason a Boss-facing reader should expect follow-up evidence work, not a green light.

## 4. What Was Independently Verified vs. Not

| Classification | Approximate share of material findings |
|---|---|
| `FACT VERIFIED` (reference-ERP documented mechanism, directly cited) | Asset Model depreciation-method mechanics; Work Center hourly-cost mechanism; residual/"Not Depreciable Value" concept |
| `SUPPORTED INTERPRETATION` | Thai daily depreciation claim (secondary-sourced); several Equipment status/state field patterns |
| `DESIGN CANDIDATE` | Post-depreciation internal usage formula; Off-Balance costing control design; most SMEsPlus-target proposals throughout |
| `CONTRADICTED` | None found at the "two authoritative sources disagree" level in this pass — see file `20` for the near-misses that were considered and not classified as contradictions |
| `UNRESOLVED / EVIDENCE REQUIRED` | Equipment↔Asset native link; Asset→Work Center depreciation flow; maintenance-cost-to-product-cost mechanism; primary Thai Revenue Code text; primary TFAC TAS 16 Thai-language text |

## 5. Scope Boundary

This package does not decide SMEsPlus architecture, does not authorize any downstream team's work, and does not represent Boss approval of any hypothesis, formula, or design candidate it discusses. Every verdict label used throughout this package follows the mandated enum (`FACT VERIFIED` / `SUPPORTED INTERPRETATION` / `DESIGN CANDIDATE` / `CONTRADICTED` / `UNRESOLVED / EVIDENCE REQUIRED`), and no file in this package uses the forbidden pass/fail-style verdict wording, per governing rule #5 (grep-verified — see file `00` §6).

## 6. Jira Note

This session's Jira key (`ERPPLUS`) was not updated. The Atlassian/Jira MCP connector is not authorized in this session. This is stated here and in file `26` rather than silently omitted.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
