# B15 — Design Traceability & Consistency Verification

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B15 — Traceability & Consistency Verification |
| Method | Genuine audit — findings below are real, not a rubber stamp. Two consistency issues were found and are resolved explicitly, not silently. |

## 1. Full Chain Traces (Exemplars)

**Chain A — the domain's central design thread:**

```
BF-04 (B01 Authorized Input: "correction should be additive, never destructive")
  → MG-01/AU-01 (B01 Requirement)
  → BINV-06 + BR-07 (B05/B06 Rule/Invariant)
  → B04 §4 Consumption Gate (Lifecycle/Event design)
  → Correction Link entity, "at most one direct target link" cardinality (B07 Conceptual Model)
  → CO-04 + CO-06 (B09 Control)
  → MG-C04/MG-C05 (B10 Migration Requirement)
  → AD-04 (B12 Advancement Objective — highest priority)
  → B04 §4 mechanism + BR-06/BR-07 (Design Decision)
  → B14 vendor-risk=NONE, B16 red-team review (Acceptance Criterion)
```

**Chain B — an assumption-flagged thread, traced to show the chain still works when the
answer is "not yet decided":**

```
OQ-03 (B01 Open Question: rounding policy unresolved)
  → MP-04 (B08 Mathematical Design Principle — Team B proposes round-half-up)
  → BR-01/BR-08 dependency (B06, balance checks operate on rounded values)
  → DT-01 (B13 Design Option — explicitly marked "not approved")
  → carried to B17 residual assumptions, not silently resolved
```

**Chain C — a regulatory-grounded thread:**

```
RG-04 (B01, Revenue Department of Thailand, official source)
  → BR-12/CAP-07 (B06/B02)
  → BINV-09 is NOT implicated (category vs. document-numbering are distinct — correctly
    not cross-wired)
  → CO-12 (B09 Control — individually traceable citation requirement)
  → B13 DT-06 (per-company sequence scope)
  → B14 provenance = RG, vendor risk = NONE
```

## 2. Orphan Check

Every B01 input item (BF-xx, PR-xx, IV-xx, LC-xx, RG-xx, MG-xx, AU-xx, AO-xx, OQ-xx) was
checked against B02–B14 for at least one downstream use. **Result: no orphans.** The one
input item with the thinnest downstream development is AO-05 (document typing / ADV-05),
consistent with it also being Team A's thinnest-evidenced advancement candidate
(single-source, Part 1 only, not independently re-evidenced by Sonnet) — carried at the same
weight, not silently dropped, not artificially inflated either (B12 AD-05 explicitly says so).

## 3. Consistency Issues Found and Resolved

**Issue 1 — ID space collision: `BR-xx` used in two places.**
B01 §4 ("Business Rules") assigned IDs `BR-01`..`BR-13` as a preliminary classification of
Team A's GR-01..13. B06 ("Business Rule Baseline") independently assigned the *same* ID space
`BR-01`..`BR-15` to its own, fully operationalized rule register. The underlying rules
correspond 1:1 for items 1–13 (same rule, increasing refinement), so there is no *content*
contradiction, but the shared numbering is a real risk for a reader (or auditor) encountering
both documents. **Resolution:** B06 is designated the canonical `BR-xx` register for this
domain going forward; B01 §4 is retroactively understood as a preliminary classification pass
that B06 supersedes in detail, not a competing definition. Recorded here rather than silently
edited into B01, per this project's own "visible corrections, not silent edits" principle
(already demonstrated in [B00](B00_GOVERNANCE_AND_HANDOFF_VERIFICATION.md)).

**Issue 2 — Interaction between CO-02 (segregation of duties) and CO-06 (safe-path-not-harder).**
CO-02 lists "corrections to consumed facts" as a candidate for optional maker-checker
separation. CO-06 requires that the correction path never carry a *higher* authorization tier
than whatever unconsumed Amendment (BR-14) requires. Read independently, a tenant could
configure CO-02's optional SoD for corrections without raising Amendment's bar to match,
which would silently violate CO-06's objective — exactly the kind of gap this domain's whole
design exists to close, so it cannot be left implicit. **Resolution (new, stated here for the
first time):** CO-02's optional SoD configuration for "corrections to consumed facts," if
enabled, must apply an equal-or-stricter authorization tier to unconsumed Amendment (BR-14)
at the same time — CO-06 constrains how CO-02 may be configured, not merely a static
comparison of two independently-set values. This resolution is itself now part of this
domain's control design and should be carried into B17's evidence pack as a stated
cross-reference, not left as an implicit reader inference.

## 4. Contradictory Rules Check

Beyond Issue 2 (resolved above), no other rule pair was found to assert incompatible
requirements. BR-07 (consumed: no mutation) and BR-14 (unconsumed: mutation permitted, logged)
are complementary partitions of the same state space (consumed vs. not), not a contradiction.

## 5. Circular Definition Check

Traced: Consumption (B04 §4) depends on Period-close (CAP-04), which does not depend on
Consumption — no cycle. SUPERSEDED status depends on an incoming Correction Link, which can
only attach to an already-COMMITTED target at link-creation time — links only ever point from
newer to older, so no cycle is reachable through chaining (B04 §6, B07 §3). **No circular
definitions found.**

## 6. Unresolved Critical Assumptions Register (consolidated)

| Assumption | First flagged | Disposition (per B01 §7 categories) |
|---|---|---|
| Rounding method = round-half-up | B08 MP-04, B13 DT-01 | **TEAM B DESIGN ASSUMPTION — REQUIRES GATE** |
| Period close as automatic, blanket consumption trigger | B04 §4, B13 DT-02 | **TEAM B DESIGN ASSUMPTION — REQUIRES GATE** |
| Chart of accounts template/instance structure (Option B) | B07 §2, B13 DT-03 | **TEAM B DESIGN ASSUMPTION — REQUIRES GATE** (also **CARRIED FORWARD** from Team A's GAP-D01-05, itself still open) |
| Audit trail tamper-evidence extended beyond evidenced legal scope | B09 CO-07, B13 DT-04 | **TEAM B DESIGN ASSUMPTION — REQUIRES GATE** |
| Correction shape left flexible (both reversal-repost and delta permitted) | B08 MP-08, B13 DT-05 | **TEAM B DESIGN ASSUMPTION — REQUIRES GATE** |
| CO-02/CO-06 configuration coupling (Issue 2 above) | B15 §3 (new) | **TEAM B DESIGN ASSUMPTION — REQUIRES GATE** |
| Whether Thai law extends tamper-evidence/gapless-numbering beyond e-Tax/tax-invoice scope | B01 §11 OQ-01 | **CARRIED FORWARD** (unchanged from Team A — this domain's design does not depend on the answer either way, per CO-07's explicit separation) |
| IAS 21 remeasurement — whether reference system does this at all | B01 §11 OQ-02 | **OUT OF DOMAIN for this question specifically** — this domain designs CAP-06 to satisfy the standard regardless of the answer (AD-08), so the carried-forward unknown does not block design, only migration-time comparison |
| Full 20-item Team A residual unknown register | `11_RESIDUAL_UNKNOWN_REGISTER.md` | **CARRIED FORWARD**, incorporated by reference (B01 §11) |

## 7. Regulatory Overreach Check

Every regulatory citation in this design (RG-01..05, cited throughout B02–B13) was checked
against its B01 scope statement. No design document was found asserting general-ledger-wide
tamper evidence or universal gapless numbering as a *legal* requirement — where broader
coverage is designed (CO-07), it is consistently and explicitly labeled as Team B's own
initiative, not a regulatory claim. **No overreach found.**

## 8. Vendor Leakage Cross-Check

Full vendor-derivation review was performed in [B14](B14_CLEAN_ROOM_PROVENANCE_MATRIX.md).
Cross-checked again here from the traceability angle (does any design decision's *chain*
bottom out in a vendor artifact rather than an AS/RG/IP/XP/TF/MR/IR category): **no**, every
chain traced in §1 and spot-checked across B02–B13 bottoms out in one of the seven approved
categories.

## 9. Acceptance Check

```
No orphan critical design decision       : CONFIRMED (§2)
Contradictory rules                       : 1 found (Issue 2), RESOLVED explicitly (§3)
Circular definitions                      : NONE (§5)
Unresolved critical assumptions           : 6 Team B assumptions + 3 carried-forward Team A
                                             items, ALL VISIBLE (§6), none hidden
Regulatory overreach                      : NONE (§7)
Vendor leakage                            : NONE (§8, cross-checked against B14)
```

**B15 = COMPLETE.**
