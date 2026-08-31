> GROUP A — Sales + Inventory + Purchase | Independent Evidence Reviewer | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-31-GRPA-SIP-IER-004 | Cluster D — Fit-Gap Neutrality / TBRAC Review

# 04 — FIT-GAP NEUTRALITY / TBRAC REVIEW

## 00 — Method

`16_FIT_GAP_CANDIDATE_PACK.md` was reviewed as a Team A proposal, not approved target design. Every material
`ADAPT`/`EXTEND`/`REJECT`/`UNKNOWN` candidate was checked for: (1) evidence support for the underlying observed
semantic, (2) whether the recommendation label's strength is proportionate to the evidence, (3) neutrality for
Team B's independent design. `11_THAILAND_BUSINESS_REALITY_AND_VARIATION_REGISTER.md` and
`12_PERSONA_USER_FITNESS_OBSERVATION_MATRIX.md` were checked against the TBRAC vocabulary defined in
`THAILAND_BUSINESS_REALITY_USER_FITNESS_CONTROL_V1.md`.

## 01 — TBRAC discipline in files 11/12: overall assessment

**`NEUTRAL / SAFE AS CANDIDATE INPUT`.** This is the strongest-disciplined part of the entire evidence chain.
Every one of the 10 rows in file 11's register is explicitly capped at `Company Variation`, `Observed Customer
Practice`, or `Unknown / Requires Real-User Validation` — the file's own governing statement ("No entry in this
register is classified `Verified Thai Business Reality`") is independently confirmed true by inspection: no row
anywhere claims a general Thai-wide or industry-wide requirement. File 12 goes further, marking every single
persona row `Unknown / Requires Real-User Validation` without exception, including two rows explicitly flagged as
"highest-value gap for a real-user interview" rather than resolved by inference. No instance of
customer-specific practice being generalized to "Thailand requires X" was found in either file.

## 02 — Fit-Gap candidate-by-candidate classification

| # | Team A candidate | This review's classification | Rationale |
|---|---|---|---|
| 1 | ADAPT — quotation/order as one lifecycle | `NEUTRAL / SAFE AS CANDIDATE INPUT` | Directly evidenced (Sales SO-01), no generalization |
| 2 | ADAPT — amount-threshold approval gate | `NEUTRAL / SAFE AS CANDIDATE INPUT` | Test-confirmed mechanism (PO-08), independently spot-checked in Cluster A/B re-performance |
| 3 | ADAPT — quantity quadruple + policy-driven billing fork | `NEUTRAL / SAFE AS CANDIDATE INPUT` | Well-evidenced on both sides |
| 4 | ADAPT — backorder as self-referential link | `NEUTRAL / SAFE AS CANDIDATE INPUT` | Directly evidenced |
| 5 | ADAPT — unified Return mechanism | `NEUTRAL / SAFE AS CANDIDATE INPUT` | The most fully-closed finding in the whole chain (exhaustive negative greps for both Sale and Purchase) |
| 6 | ADAPT (as a pattern) — reflective `_run_<action>` dispatch | `NEUTRAL / SAFE AS CANDIDATE INPUT` | Explicitly scoped as "the shape of the decoupling," not the literal mechanism — correctly hedged for a non-Odoo target |
| 7 | UNKNOWN — fused count/ledger row | `NEUTRAL / SAFE AS CANDIDATE INPUT` | Correctly left as a design question, not a recommendation |
| 8 | REJECT (duplication) / UNKNOWN (underlying requirement) — two Thai branch modules | `NEUTRAL / SAFE AS CANDIDATE INPUT` | Correctly separates the defect (uncoordinated duplication) from the underlying requirement (left UNKNOWN) |
| 9 | REJECT (dual-writer) / ADAPT-worthy (underlying need) — SKU auto-numbering | `NEUTRAL / SAFE AS CANDIDATE INPUT` | Same clean separation pattern as #8 |
| 10 | UNKNOWN — unguarded over-receipt/delivery | `NEUTRAL / SAFE AS CANDIDATE INPUT` | Correctly framed as a decision SMEsPlus must make, not inherited |
| 11 | REJECT — inconsistent sentinel (`"New"` vs `"/"`) | `NEUTRAL / SAFE AS CANDIDATE INPUT` | Genuine inconsistency, correctly labeled a defect not a rule |
| 12 | UNKNOWN — asymmetric cancellation gate | `NEUTRAL / SAFE AS CANDIDATE INPUT` | Independently re-verified in Cluster A (Purchase's dual gate vs. Sale's single gate) — correctly left as a design question rather than assumed intentional |
| **13** | EXTEND (Purchase Request) / UNKNOWN (Purchase Order, Sale Order) — two-level approval schema | `NEUTRAL / SAFE AS CANDIDATE INPUT` | Independently re-verified in full in Cluster C — every statistic cited here (1,945/96/2,199; 98.5%; 0 rows) reproduces exactly. The UNKNOWN qualifiers (Purchase Order's assign-but-never-approve pattern; Sale Order's small sample) are appropriately conservative given the same data this review independently pulled |
| 14 | UNKNOWN — Sale confirmation not gated by availability | `NEUTRAL / SAFE AS CANDIDATE INPUT` | Correctly framed as a deliberate-decision item |
| **15** | EXTEND — Sales-initiated RMA/return UX | `SAFE ONLY WITH QUALIFIER` — see §03 | The underlying observation (no dedicated Return object/button on either Sale or Purchase) is fully evidenced; the rationale text is not |
| 16 | UNKNOWN — approval traceability, depends on #13 | `NEUTRAL / SAFE AS CANDIDATE INPUT` | Correctly deferred to #13's resolution |
| 17 | REJECT (naming trap) — `purchase.requisition` ≠ tendering | `NEUTRAL / SAFE AS CANDIDATE INPUT` | Confirmed manifest-vs-code mismatch, correctly framed as a naming-clarity issue for target design, not a business-rule claim |

## 03 — Finding: Fit-Gap item #15's rationale contains an unqualified generalization

Item 15's Rationale column states: *"...many SME businesses expect a salesperson-initiated RMA flow — this is a
plausible extension point, explicitly flagged as a candidate rather than a finding of a defect."*

The Reference Observation itself (no dedicated Return object/button on either commercial side) is fully evidenced
and independently consistent with Scenarios 5/6 of `05_INTEGRATED_E2E_LIFECYCLE_MAP.md`. But the phrase **"many
SME businesses expect..."** is a general business-practice claim — broader even than a Thailand-specific claim —
asserted with no TBRAC classification, no evidence citation, and no "Unknown/Requires Real-User Validation"
qualifier, unlike every comparable statement in files 11/12. This is the one place in the entire Fit-Gap pack
where the evidence-discipline visible everywhere else (§01 above) lapses: a plausible personal inference from the
author is stated in the same voice as an evidenced finding.

This does not invalidate the EXTEND candidate itself — the underlying observation is real and the candidate label
is reasonable — but the rationale text should not be read by Team B as evidence-backed. **Recommended correction
(not performed by this review, per the read-only boundary on Team A's files)**: qualify the sentence as Team A's
own inference (e.g., "plausibly, though not confirmed by any evidence gathered in this research — a real-user
validation item"), consistent with how items 8/9/10/12/14 handle similar judgment calls elsewhere in the same
document. **Classification: `SAFE ONLY WITH QUALIFIER`. Not Gate-blocking** — a wording-precision item, not a
design-contamination risk (no target code/schema is proposed either way).

## 04 — Clean-room / design-contamination check

No candidate in the pack proposes Node.js code, a target database schema, a target API contract, or a target UI
structure. Every candidate stays at the "generic business semantic" level required by the governing prompt's §5
clean-room boundary (independently re-read and confirmed to prohibit copying source code, ORM architecture, DB
schema, vendor workflow implementation, or UI structure as target requirements). **No design-contamination risk
found anywhere in the pack.**

## 05 — Overall Cluster D verdict

**`NEUTRAL / SAFE AS CANDIDATE INPUT`** for 16 of 17 candidates, **`SAFE ONLY WITH QUALIFIER`** for candidate #15
(rationale wording only, not the candidate itself). No `DOWNGRADE TO UNKNOWN/HYPOTHESIS` or
`DESIGN-CONTAMINATION RISK` classification was warranted for any candidate.
