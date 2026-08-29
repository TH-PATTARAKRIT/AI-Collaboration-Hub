# B14 — Clean-Room Provenance Matrix

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B14 — Clean-Room Provenance Matrix |
| Acceptance requirement | Critical Vendor-Derived Design Risk = 0, or STOP |

## 1. Provenance Categories Used

`AS` = Accounting Standard · `RG` = Regulatory Requirement · `IP` = Industry Principle ·
`XP` = Cross-ERP Pattern · `TF` = Approved Team A Business Fact · `MR` = Approved Migration
Requirement · `IR` = Independent Team B Reasoning

## 2. Matrix

| Decision (source phase) | Statement | Provenance | Citation | Vendor-derived risk |
|---|---|---|---|---|
| Synchronous balance gate (B04 §7, MP-01) | Balance validation is structural to Posting, no suppression path | AS, IR | PR-01/AP-01 (Wikipedia — double-entry bookkeeping), CF-01 (as the weakness being deliberately not repeated) | **NONE** — design explicitly rejects the vendor's suppressible pattern rather than adopting it |
| Single-authority period model (CAP-04, BINV-02) | One authoritative open/closed answer per (date, company, class) | XP, AS, IR | NetSuite triangulation (`08_CROSS_SOURCE_TRIANGULATION.md`), AP-06 | **NONE** — explicitly rejects the vendor's six-field shape; modeled on a different vendor's (NetSuite) publicly documented pattern, itself only used as cross-ERP evidence of feasibility, not copied structurally |
| Consumption Gate (B04 §4) | Mutability gated on downstream consumption, not raw status | TF, IR | `06_STATE_EVENT_LOGIC_ANALYSIS.md` (Team A's neutral observation, explicitly stopping short of design), extended here into an actual mechanism | **NONE** — Team A's own artifact states it deliberately proposed no target mechanism; the mechanism is Team B's original contribution |
| Correction as bidirectional relationship (B04 §6, B07) | Correction is a permanent link, not a field/flag | XP, AS, IR | SAP Business One triangulation (CF-04 evidence), PR-06 | **NONE** — the *pattern* (reversal, not deletion) is cross-ERP validated; the *relationship modeling* (bidirectional, chainable, one-target-link cardinality) is independent Team B design not sourced from any vendor |
| Exact-decimal representation, correctly scoped (MP-03) | Computing-correctness norm, not cited as a formal accounting standard | IR (corrected from an earlier overclaim) | disagreement-02, CF-05 | **NONE** — the reference system's *storage type* was independently verifiable at the database level (Team A P2 direct evidence) and is a factual observation, not a copied design; the requirement itself is a general computing norm cited to no vendor |
| Rounding method default (MP-04) | Round-half-up proposed as default | IR only — **no AS/RG basis exists** | None — OQ-03 remains open | **NONE**, but flagged as a **TEAM B DESIGN ASSUMPTION — REQUIRES GATE** (B01 §7 disposition) precisely because it has no standard or regulatory anchor, only Team B's own judgment (B13 DT-01) |
| Currency remeasurement as designed capability (CAP-06, MP-06) | Non-optional, scheduled remeasurement | RG | AP-07/RG-05 (IFRS IAS 21, ifrs.org) | **NONE** — sourced directly from the international accounting standard, independent of whether the reference system implements it (Team A found this genuinely unknown, ADV-08) |
| Regulated-document integrity scope (CAP-07, BR-11/12) | Automatic coverage, narrowly scoped to evidenced classes | RG | RG-03 (ETDA, official source), RG-04 (Revenue Department of Thailand, official source, Revenue Code §86) | **NONE** — grounded in official government sources fetched directly this project (SONNET-CORR-001 round), not in the vendor's opt-in mechanism, which is referenced only as the weakness being corrected |
| Deprecated-account full guard (BR-13) | Guard applies to all posting paths, not one usage type | TF, IR | GR-13 (Team A: reference system guards only tax-repartition usage) | **NONE** — explicit, acknowledged strengthening beyond the vendor's partial implementation, cited as the gap being closed, not the design being copied |
| No source-system ID as identity (B07 §4, B10 MG-C01/C08) | Every entity gets a new, SMEsPlus-native identity | MR, IR | B01 §8 (candidate input MG-01..04); directive §10, "never use Odoo internal ID as SMEsPlus identity" | **NONE** — this decision exists specifically to prevent vendor-derived coupling, the opposite of the risk this matrix screens for |
| Multi-tenant-safe capability scoping (CO-10, AD-09) | No capability requires cross-tenant shared state | IR | Directive §1 (project identity: independent SaaS ERP) | **NONE** — no Team A source exists because the reference system was never evaluated as multi-tenant; this is original reasoning with no vendor artifact to have derived from |
| Document-numbering sequence scope, per-company (B13 DT-06) | Sequence scoped at least per-company, never platform-global | RG, IR | RG-04 (statutory numbering, entity-scoped by nature), CO-10 | **NONE** |
| Chart of accounts: template/instance option (B13 DT-03, Option B recommended) | Shared template with per-company override | XP (general SaaS multi-entity pattern), IR | GAP-D01-05 — Team A explicitly left the *vendor's own* template mechanics unread and unresolved | **NONE, verified explicitly** — because Team A never analyzed the vendor's chart-template mechanism in any detail (it remains an open gap, not a documented fact), there is nothing available to have copied; the recommended option is derived from general SaaS multi-tenant business patterns, not from this reference system |
| Migration consumption-on-import default (B10 MG-C04/C07) | Migrated historical entries import as already-consumed; historical periods import already-closed | IR, MR | B01 §8 migration requirements, extended by Team B reasoning (not separately evidenced by Team A at this level of detail) | **NONE** |
| Exception model resolutions for previously-unresearched scenarios (B11 #6, #9, #11, #15, #17, #18) | Wrong tenant, duplicate detection, future posting, missing reference, concurrency, partial failure | IR (all six) | Explicitly had no reference-system evidence to draw on — Team A declined to analyze these (out of scope) or found the reference's own answer unproven | **NONE** — by construction, these cannot be vendor-derived since no vendor behavior was ever read for them |
| Audit trail tamper-evidence, broad scope (CO-07, B13 DT-04 Option A) | Extended beyond evidenced legal requirement, as an independent control choice | IR, RG (partial) | AO-02, explicitly separated from OQ-01 (which stays open) | **NONE** — explicitly labeled in B09/B13 as this domain's own initiative, not a claim of vendor or regulatory origin |

## 3. Reviewed Vendor-Detail References (confirmed traceability-only, never adopted)

Per directive §5, a small number of vendor-specific terms appear in this domain's design
documents *only* as comparison points explaining what a decision deliberately does **not**
do — never as the source of the decision itself. Each is reviewed here explicitly:

| Term appearing in B02–B13 | Where | Role | Adopted into design? |
|---|---|---|---|
| "chatter / tracking" (optional event logging) | B02 CAP-08 | Named as the weakness CO-07/CAP-08 exists to not repeat (forced vs. optional logging) | **No** — design requires forced logging, the opposite of this mechanism |
| "reset-to-draft" | B04, B12 AD-07 | Neutral behavioral label (already used as neutral language in Team A's own `06_STATE_EVENT_LOGIC_ANALYSIS.md`) for the pattern BR-07 exists to forbid | **No** — this pattern is explicitly refused by BR-07 |
| "six lock-date fields" / "BYPASS_LOCK_CHECK" | B02 CAP-04, B05 BINV-02, B12 AD-03 | Cited as the fragmented shape CAP-04's single-authority design replaces | **No** — CAP-04 is one authoritative determination, structurally different |

No vendor object name, method name, table name, or class name appears anywhere in
B02–B13's actual design statements (as opposed to these three reviewed comparison
references, which describe behavior patterns already neutralized by Team A, not identifiers).

## 4. Acceptance Check

```
Every material decision maps to at least one provenance category : CONFIRMED (§2)
Vendor-detail-referencing sentences individually reviewed          : CONFIRMED (§3)
Critical Vendor-Derived Design Risk                                : 0
```

**Acceptance criterion met — B14 = COMPLETE. Not a STOP condition.**
