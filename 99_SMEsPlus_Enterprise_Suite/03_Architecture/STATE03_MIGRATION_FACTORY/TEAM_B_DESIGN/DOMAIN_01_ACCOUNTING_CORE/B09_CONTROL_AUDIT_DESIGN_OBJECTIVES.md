# B09 — Control & Audit Design Objectives

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B9 — Control & Audit Design Objectives |
| Scope | Design objectives only. No access-control code, permission schema, or role table below. |
| **Corrected (Round 2)** | **CORR-B2-01/02 (2026-08-29)** — CO-14/CO-15 added, required by B08/B04's temporal-model and Restatement corrections. See [CORR_B2_CORRECTIVE_ROUND.md](CORR_B2_CORRECTIVE_ROUND.md). |
| **Corrected (Round 3)** | **CORR-B3-04 (2026-08-29)** — CO-16 added (materiality is a policy input, never computed or invented by this domain's design), required by B04 §3b/§3c's new IAS 8 classification, which references CO-16 by name. See [CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md](CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md). |
| **Corrected (Round 4)** | **CORR-B4-04 (2026-08-30)** — CO-14's mode-labeling scope extended to explicitly cover Reported Retained Earnings / Reported Equity (B07 §1g), required by ChatGPT's Round 4 finding `M-AUD-10`. See [CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md](CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md). |
| **Corrected (Round 5)** | **CORR-B5-02/05 (2026-08-30)** — CO-14's scope extended again to cover B08 MP-12's three Trial Balance outputs (`M-AUD-11`); CO-15's authorization tier extended (reused, not reinvented) to cover post-reliance Fiscal Year boundary changes (`M-AUD-12`), B07 §1h. See [CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md](CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md). |

## CO-01 — Authorization

**Objective:** every state-changing action against the Ledger (B04 §3's event list) must be
attributable to a specific, authorized actor, and "authorized" is a decision independently
checkable from "technically able to." Having system access is not the same as being
authorized for a specific action class — this domain's design must leave room for that
distinction to be enforced by whatever platform-level permission system exists, by never
assuming an action is legitimate solely because it reached CAP-02/03/04.
**Basis:** AU-01/AU-03; GAP-D01-22 (Team A left "is reopen role-gated" genuinely unresolved
— this objective is this domain's design answer: it must be, even though the mechanism
itself is a platform concern outside this domain's boundary, B03 §4).

## CO-02 — Segregation of Duties

**Objective:** the design must **support** maker-checker separation for higher-risk actions
(manual Entries above a threshold, corrections to consumed facts, period reopens) without
**mandating** it universally — an SME with two accounting staff cannot always achieve the
segregation a larger enterprise can. The capability model (B02) achieves this by keeping
proposal (originating domains, or manual capture) and commitment (CAP-02) as logically
distinct steps even when the same person performs both — the separation is available to be
enforced by policy/role configuration outside this domain, not foreclosed by this domain's
design.
**Basis:** general internal-control principle; not evidenced as a specific Thai statutory
requirement in this domain's input — stated as a design objective, not a regulatory claim.

## CO-03 — Commitment Integrity

**Objective:** Posting (CAP-02) is atomic — an Entry is either fully committed, satisfying
every check in [B06](B06_BUSINESS_RULE_BASELINE.md) BR-01 through BR-05 simultaneously, or
not committed at all. Both outcomes (success and refusal) are evidenced (BR-01's Audit
Consequence column).
**Basis:** B04 §7, BINV-01.

## CO-04 — Immutability of Consumed Fact

**Objective:** immutability after consumption (BINV-06) is a control the design enforces
structurally (B04 §4 gate), not a policy that depends on user discipline or training. This is
restated here specifically as a *control* objective — distinct from BINV-06's statement as an
*invariant* — because a control objective additionally requires that any attempt to violate
it produces evidence of the attempt, not just a silent refusal (BR-07's Audit Consequence).
**Basis:** BINV-06, ADV-04 — the domain's central control objective.

## CO-05 — Correction Must Be Self-Evident

**Objective:** a correction Entry must be identifiable as a correction by any reviewer without
requiring them to already know the Correction Link exists — i.e., the linkage (B07) is not
merely queryable, it is a defining, visible property of the Entry, not an optional annotation.
A ledger reader must never mistake a correction for an unrelated, ordinary Entry.
**Basis:** BINV-05, PR-07.

## CO-06 — The Safe Correction Path Must Not Be the Harder One

**Objective:** reversal/correction (BR-06) must not require a higher authorization tier than
whatever unconsumed in-place Amendment (BR-14) is permitted at. If the safe, additive path is
bureaucratically harder to use than a risky shortcut, users will rationally gravitate to the
shortcut — the reference system's own failure mode (CF-06: a sound pattern and an unsound one
coexist, and nothing favors the sound one) is a control-design lesson as much as a technical
one. This objective makes that lesson structural: **at minimum equal, and where staffing
allows, lower** authorization friction for reversal/correction than for any other path to the
same outcome.
**Basis:** ADV-04, disagreement-03 (priority elevation of this exact tension).

## CO-07 — Audit Trail Independence and Tamper-Evidence

**Objective:** the Audit Evidence stream (CAP-08) must be independently reconstructable
(BINV-08) and, as an independent Team B design choice, **tamper-evident by default across
the whole trail** — not merely for the narrow, statutorily-confirmed document classes
(RG-03/RG-04). This is stated explicitly as a **design objective this domain adopts on its
own initiative (an advancement, per AO-02), not as a claim that Thai law requires it for the
general ledger** — OQ-01 remains open and this objective does not silently resolve it. The
distinction matters: CO-07 is defensible internal-control practice regardless of how OQ-01 is
eventually answered.
**Basis:** AO-02, BINV-08; explicitly NOT based on an extended reading of RG-03/RG-04 beyond
their evidenced scope.

## CO-08 — Period Control Authorization Tier

**Objective:** closing or reopening a Period (CAP-04) requires a distinct, higher
authorization tier than ordinary posting within an open one — the two are different classes
of action with different blast radii (one entry vs. every entry in a period) and must not
share an authorization tier by default.
**Basis:** BINV-02, CO-08 extends BR-05's override requirement with an explicit tiering
objective not separately stated in B06.

## CO-09 — Multi-Company Access Scoping

**Objective:** a user's ability to view or post within one Company (CAP-05) must be
independently grantable from their access to any other Company in the same deployment — no
implicit "if you can see one, you can see all" default.
**Basis:** BINV-03.

## CO-10 — Multi-Tenant Isolation *(new — not covered by any prior phase)*

**Objective:** this domain is designed to operate entirely within one tenant's context.
Multi-company (CO-09) separates legal entities *within* one customer's deployment;
multi-tenant isolation separates *different customers* of the SaaS platform from each other
entirely, including from each other's aggregate or statistical data, not just line-level
detail. This domain's design must not introduce anything that would make tenant isolation
harder to enforce at the platform layer beneath it — concretely: no capability in
[B02](B02_ACCOUNTING_CORE_CAPABILITY_MODEL.md) requires shared mutable state across tenants
(e.g., a single global sequence for CAP-07's numbering must be scoped at least per-company,
never shared platform-wide, since a cross-tenant-visible sequence would itself leak
information — how many documents another tenant has issued).
**Basis:** Project identity (SaaS ERP, directive §1) — this objective exists because the
target is explicitly multi-tenant SaaS, a dimension the reference system (typically
single-tenant, on-premise-style deployment per seat) was never evidenced against by Team A
and required independent reasoning here.

## CO-11 — Evidence Retention Floor

**Objective:** committed Entries and their Audit Evidence must be retained for at least the
longest statutory minimum applicable to the tenant's jurisdiction(s) — evidenced today as
5–7 years for Thailand (RG-02) — and retention configuration must enforce this as a **floor**
that cannot be configured below the legal minimum, not a default that happens to meet it.
Because this is a SaaS product not limited to one jurisdiction by the project's own identity
(directive §1), the design objective is stated generally (retention floor derived from
applicable jurisdiction) with Thailand's specific figure as the only currently evidenced
instance — extending to other jurisdictions' figures without evidence would be exactly the
overclaim this project's provenance rules forbid.
**Basis:** RG-02.

## CO-12 — Regulated-Document Integrity Coverage Is Automatic and Individually Traceable

**Objective:** restates BR-11/CAP-07 as a control objective: integrity/numbering coverage for
a regulated document class is automatic once tagged (never an administrator-remembered
setting), and — the control addition this phase makes — **every covered class must trace to
a specific, named regulatory citation** (currently: RG-03 for e-Tax invoices/receipts, RG-04
for tax invoices). A class must not receive integrity treatment merely by resemblance to one
that does — scope discipline is itself a control, preventing the domain's regulated-document
surface from silently growing beyond what evidence supports.
**Basis:** BR-11, RG-03, RG-04, OQ-01 (explicit boundary against overclaiming).

## CO-13 — Stale Draft Surfacing *(added at B16 §11, Persona 6 fix)*

**Objective:** an Entry remaining in DRAFT beyond a policy-defined age threshold must be
surfaced for review — never auto-posted (that would bypass the deliberate human judgment
DRAFT exists to allow), never auto-deleted (that could destroy legitimate in-progress work),
but no longer silently invisible either. DRAFT's correct design property — invisible to the
Ledger until committed (B03 §2) — has a failure mode the earlier control objectives did not
name: it is also an available way to indefinitely defer or effectively conceal a transaction
that should have been posted, simply by never posting it. This objective closes that gap
without weakening DRAFT's legitimate purpose.
**Basis:** B16 §11 (Security/Control Reviewer red-team finding) — no direct Team A source ID;
identified independently during this domain's own review, not carried from any input.

## Residual Scope Boundary *(added at B16 §11, Persona 2 fix)*

Every control objective above (CO-01 through CO-13) governs behavior at the application/
business-logic layer this domain designs — CAP-02/03/04/08 and whatever platform-level
permission system CO-01/CO-09 assume exists. **None of them can prevent a sufficiently
privileged infrastructure-level actor (e.g., direct data-store access bypassing the
application entirely) from altering committed data or Audit Evidence outside this domain's
reach.** This is stated explicitly, not left for an auditor to discover by asking: this
domain's control design assumes the application layer is the only path to the data, and
infrastructure-level tamper-resistance (encryption at rest, storage-level access controls,
infrastructure audit logging) is a platform/infrastructure concern outside DOMAIN_01's
boundary (B03 §4), not a gap in this domain's own design.

## CO-14 — Temporal Mode Labeling *(added at CORR-B2-01/02; scope extended at CORR-B4-04, CORR-B5-02)*

**Objective:** every report or query result derived from MP-09 (B08, corrected) must be
explicitly labeled with which temporal mode produced it — "as originally known as of
[recording-time T]" (Mode 1) or "current / restated as of [business date D]" (Mode 2) — never
presented as an unlabeled single number. This is the control-layer enforcement of
ChatGPT's Round 2 acceptance requirement (`M-AUD-04`): "do not let one silently masquerade as
the other."
**Extended at CORR-B4-04 (`M-AUD-10`):** this labeling requirement explicitly covers Reported
Retained Earnings and Reported Equity ([B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1g's
`_Known(C,D,T)` / `_Current(C,D)` functions), not only raw MP-09 balance queries. ChatGPT's
Round 4 audit found these derived figures were left out of CO-14's original scope even though
B20 Test 8 already relied on a Mode-1 reading of them — this extension closes that scope gap
without inventing a new control, since the underlying requirement ("do not let one silently
masquerade as the other") already applied in substance; only the enumeration of which outputs
it covers was incomplete.
**Extended again at CORR-B5-02 (`M-AUD-11`):** this labeling requirement additionally covers
which of B08 MP-12's three outputs a presentation is showing — the Raw Cumulative Trial
Balance (Proof G1), the Current-Fiscal-Year Reporting Balance (Proof G2, never itself labeled
"balanced" or "a Trial Balance"), or the Balanced Presentation Trial Balance (Proof G3). Any
presentation carrying G3's derived bridge line must carry the exact label "DERIVED PRESENTATION
COMPONENT — NOT A POSTED FINANCIAL FACT" (or an equivalent, equally explicit annotation)
alongside it — the same "do not let one silently masquerade as the other" principle CO-14 has
enforced since Round 2, now extended to a case ChatGPT's Round 5 audit found this domain's own
Round-4 design had itself violated (MP-12 Proof G calling G2 "the Raw Trial Balance").
**Basis:** B08 MP-09 (corrected), BINV-11 (corrected), B07 §1g (new), B08 MP-12 (corrected) —
no direct Team A source ID, since this distinction did not exist before this domain's own
Round 2 correction.

## CO-15 — Restatement Authorization Tier *(added at CORR-B2-01/02; scope extended at CORR-B5-05)*

**Objective:** a Restatement (B04 §3a — a Correction/Void whose target has independent
Consumption and whose Effective Date falls within the period that Consumption covers)
requires an authorization tier at least as strict as Fiscal Year Close (CO-08 tiering
extended) — stricter than an ordinary Correction (CO-06). This is deliberately asymmetric
with CO-06's "safe path not harder" principle: CO-06 governs the choice between Amendment and
ordinary Correction for the *same* underlying risk level; Restatement is a *different*, higher
risk level (rewriting the "current" view of an already-relied-upon period), and earns its own,
higher bar rather than inheriting Correction's low-friction tier by default.
**Extended at CORR-B5-05 (`M-AUD-12`):** this same authorization tier is reused, not
reinvented, for a post-reliance Fiscal Year boundary change (B07 §1h, new
`FiscalYearBoundaryChanged` event, B04) — re-partitioning which Fiscal Year a transaction
belongs to carries a comparable blast radius to restating a period's "current" view, so it
earns the same bar. **The exact tier is flagged as a new, seventh Team B assumption** ([B15](B15_DESIGN_TRACEABILITY_MATRIX.md)
§6) — reusing CO-15's tier is this domain's working default, not a fact this domain's evidence
independently settles the way, for example, CO-16's materiality-policy-input decision is.
**Basis:** `M-AUD-04`'s acceptance requirement that formal restatement be "explicit,
auditable, and separately reconstructable" — no direct Team A source ID. `M-AUD-12`'s
requirement that a Fiscal Year boundary change be gated, audited, and never silent — also no
direct Team A source ID.

## CO-16 — Materiality Is a Policy Input, Never a Computed or Invented Threshold *(added at CORR-B3-04)*

**Objective:** whether a Prior-Period Error is **Material** or **Immaterial** (B04 §3b's
classification decision tree) is never computed, defaulted, or invented by this domain's
design — no numeric threshold (percentage of Revenue, absolute currency amount, or any other
formula) is proposed anywhere in this design pack. Materiality is supplied, per correction, as
an explicit judgment input from an authorized role (a Controller, CFO, or equivalent
policy-setting authority — the specific role is a Boss-level/organizational decision, not a
Team B design decision), and that judgment — who made it, when, and what it was — is itself an
auditable fact (CO-07) attached to the classification.
**Why this control exists, not just the classification concept in B04:** without a named
control objective, a future implementation could "helpfully" fill the gap with an invented
default threshold, which would silently convert a required professional judgment (IAS 8 itself
defines materiality only qualitatively — see IAS 8 para 5's cross-reference to the
Framework/IAS 1, and states no numeric bright line) into a false sense of automation. This
control exists specifically to block that failure mode at the design level, the same way CO-06
blocks "the safe path becomes the harder one" as a design-level failure mode rather than
trusting implementation discipline alone.
**Basis:** `M-AUD-06`'s underlying finding and IAS 8 (verified from primary-source PDF text)
paras 5, 41 — materiality is defined by reference to whether omission/misstatement could
influence users' economic decisions, a qualitative judgment test, never a formula. No direct
Team A source ID, since this control did not exist before this domain's own Round 3
correction.

## Acceptance Check

```
All 12 mandated areas covered : CONFIRMED (Authorization=CO-01, Segregation of duties=CO-02,
  Commitment=CO-03, Immutability=CO-04, Correction=CO-05, Reversal=CO-06, Audit trail=CO-07,
  Period control=CO-08, Multi-company=CO-09, Multi-tenant isolation=CO-10, Evidence
  retention=CO-11, Regulated-document integrity=CO-12)
No access-control code/schema proposed : CONFIRMED
No objective overclaims regulatory scope beyond B01 §7/§11 : CONFIRMED (CO-07, CO-11 both
  explicitly separate "this domain's own design choice" from "confirmed legal requirement")
CO-13 added post-hoc via B16 red-team review (13th item, beyond the 12 mandated) : CONFIRMED
CO-14/CO-15 added at CORR-B2-01/02 (14th/15th items, temporal model + Restatement) : CONFIRMED
CO-16 added at CORR-B3-04 (16th item, materiality as policy input, never computed) : CONFIRMED
  — directly closes the risk that a future implementation invents a numeric materiality
  threshold this design never authorized
```

**B9 = COMPLETE.** *(Corrected at CORR-B2-01/02/CORR-B3-04/CORR-B4-04/CORR-B5-02/05 — CO-14/
CO-15 added Round 2, CO-16 added Round 3, CO-14 scope extended Round 4 and again Round 5,
CO-15 scope extended Round 5 (no new CO either round — still 16 total). CO-01..13 unchanged
since their respective original passes.)*
