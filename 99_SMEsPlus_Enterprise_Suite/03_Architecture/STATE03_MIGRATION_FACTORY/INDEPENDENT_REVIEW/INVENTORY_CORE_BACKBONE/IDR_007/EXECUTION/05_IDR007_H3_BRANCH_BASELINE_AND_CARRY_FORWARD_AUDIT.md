# 05 — H3 (GRPA-H8) Branch Baseline and Carry-Forward Audit

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Verify H3's closure does not claim the customer's legacy branch usage is fully understood, and does not reopen the approved platform baseline | Claude (IDR-007) | This artifact | 2026-09-01 | Self | Semantics correctly used; baseline not reopened; a residual scope-precision gap noted (not blocking) | Confirms this closure is a controlled non-claim, not a hidden architecture decision |

## Required semantics (governing prompt §5.4)

> `CLOSED AS AN INVENTORY ARCHITECTURE QUESTION — CONTROLLED MIGRATION/TBRAC + ACCOUNTING-TAX CARRY-FORWARD` if and only if no unresolved branch fact changes Inventory Stock Truth or the approved platform hierarchy.

## Check 1 — label correctness

`02_CORR005_FIVE_HIGH_RECONCILIATION_MATRIX.md` L15, CORR-005 reconciled column for GRPA-H8, quoted: **`CLOSED AS AN INVENTORY ARCHITECTURE QUESTION`** — `CONTROLLED MIGRATION / TBRAC CARRY-FORWARD` + `ACCOUNTING/TAX CARRY-FORWARD`. This matches the required phrase. **PASS.**

## Check 2 — does the closure claim the legacy branch usage is understood?

Explicitly checked for overclaiming language ("confirmed," "the customer uses X pattern," "verified as correct") anywhere the H3/GRPA-H8 disposition is stated:

- `06_IER003_HIGH_H3_THAI_BRANCH_TBRAC_REVIEW.md` L24 (quoted in the raw-evidence extraction): *"There is no second, child company record to examine — meaning the specific claim 'branch is implemented as a child `res.company` record' cannot be verified as this customer's *actual practice* from this dataset..."* — this is IER-003 **correcting** TEAM A's original DR-002 characterization down to a weaker, honest claim, not strengthening it.
- `A14` Part 3 L84 (CORR-005 reconciled row), quoted: *"structural conflict confirmed; TEAM A's 'branch = child `res.company`' characterization corrected to 'structurally available, not confirmed as this customer's practice' (single-company dataset)."*
- `06_IER003_...md` L35 (verbatim, from the earlier extraction): *"What remains unknown: (1) whether the customer's real business operations use either field meaningfully or if both are vestigial/unused... (2) the underlying Thai statutory requirement itself."*

**PASS** — at every layer of the chain (DR-002 → IER-003 → CORR-005), the closure explicitly states what is *not* known (which of the two legacy branch fields, if either, reflects real operational practice), rather than asserting an answer. This is the correct shape for a "requires real user validation" carry-forward, not a disguised technical conclusion.

## Check 3 — is the approved SaaS Multi-Tenant/Multi-Company/Multi-Branch platform baseline reopened?

- Boss Inventory Scope Ruling (`origin/SMEsPlus`) §1.2, L31, quoted: *"SMEsPlus already operates under an approved SaaS architecture baseline with Tenant, Company and Branch context... must not re-research or redefine the Tenant/Company/Branch architecture unless new material evidence demonstrates a direct contradiction, compliance defect, or unresolvable business-reality conflict."*
- The H3 finding concerns **legacy source data field mapping** (`l10n_th_partner`'s `branch` field vs. `l10n_th`'s `company_registry` field — which one the customer's *legacy* system actually populated/relied on), not the SMEsPlus platform's own Branch model design. No file in the reconciled package proposes an alternative Branch architecture or claims the platform baseline is wrong.
- This review independently re-read the required constraint (governing prompt §4.2: "Do not research Branch architecture again... Only verify that Inventory evidence correctly carries Tenant/Company/Branch context") and found no violation — H3's closure is scoped to a legacy-mapping question, explicitly deferred to Migration/TBRAC and Accounting/Tax, and does not touch the platform's own Tenant/Company/Branch design.

**PASS** — baseline not reopened.

## Check 4 — carry-forward completeness (does anything disappear?)

`03_CORR005_RESIDUAL_BLOCKER_AND_CARRY_FORWARD_REGISTER.md` View 2 correctly splits H3 into **two** carry-forward rows (not one, and not zero): `CONTROLLED MIGRATION / TBRAC CARRY-FORWARD` (which legacy field reflects actual practice) and `ACCOUNTING/TAX CARRY-FORWARD` (Thai tax-document branch semantics). Both rows have explicit owners and explicit "must not be inferred" guardrails. Nothing about H3 is silently dropped.

## One scope-precision observation (not a defect, noted for completeness)

IER-003's own gate-impact register (`16_IER003_BOSS_GATE_RECOMMENDATION.md` L33, from the raw extraction) also names a **third**, narrower dependency implicit in H3 — Thai statutory/regulatory confirmation of which branch representation is legally correct — which CORR-005's two-row carry-forward folds into the Accounting/Tax row rather than breaking out as its own row. This is a reasonable consolidation (statutory confirmation and tax-document semantics are closely related and share the same Accounting/Tax owner) and does not lose the dependency — it remains discoverable by following the citation chain into IER-003 `06`. Not severity-elevating; noted only so a future reader tracing H3 end-to-end has this pointer.

## Verdict

**PASS.** H3's closure correctly avoids claiming the customer's actual legacy branch practice is known, does not reopen the approved platform Tenant/Company/Branch baseline, and its two carry-forward rows are complete and explicitly owned. No correction required.
