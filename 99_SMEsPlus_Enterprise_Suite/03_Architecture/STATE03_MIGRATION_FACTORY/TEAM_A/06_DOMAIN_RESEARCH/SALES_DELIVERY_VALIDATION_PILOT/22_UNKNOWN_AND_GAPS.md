> Domain: SALES_DELIVERY_VALIDATION_PILOT (Gx2) | Evidence Gap Register | Gaps recorded as Evidence Gap / Evidence Conflict, not Fail

# 22 — UNKNOWN AND GAPS (Gx2)

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-SDV-01 | **RESOLVED 2026-09-28 (Gx6), documentation-tier.** Was: Evidence Conflict between "posts at movement" (Gx1) and "posts at invoice" (this Gx). Gx6 found the full architecture: no entry at movement, entry at invoice time, month-end Stock Closing/accrual sweeps up anything uninvoiced by period end — see `../PERIOD_CUTOFF_VALIDATION_PILOT/06_BUSINESS_RULE_REGISTER.md` PCO-F03. This Gx's original finding (posts at invoice) was the accurate half of the picture; Gx1's original finding was the incomplete/generic half — reconciled, not contradictory. **STATUS DOWNGRADE (2026-09-29, Boss ruling): this resolution is `Material Finding — Independently Unverified`, not Canonical Architecture Truth — it was reconciled by the same session that raised the original conflict, not an independent reviewer. Routed to `CHATGPT_AUDIT`; see `00_Architecture_Governance/STATE03_VALUATION_TIMING_CROSS_GX_CONTRADICTION_MATRIX.md`.** | No longer blocks downstream design discussion at documentation-tier confidence, though AWT still recommended for formal runtime confirmation. | **Material Finding — Independently Unverified** (was: Resolved, documentation-tier, high confidence) | AWT (shared capstone session, queued in Gx6's `AWT_BACKLOG.md`) for final runtime confirmation; independent audit via `CHATGPT_AUDIT` |
| GAP-SDV-02 | Delivery-side backorder documentation reads as more automatic than Gx1's purchase-side, action-gated backorder description; not confirmed whether this is a real mechanical difference or documentation-emphasis difference | Cannot yet state with confidence that GRV-F03 and SDV-F03 are mechanically identical | **Targeted Validation Needed** | Direct page comparison once network access allows, or runtime confirmation |
| GAP-SDV-03 | No documentation evidence gathered on multi-company/tenant scoping for delivery, invoicing-policy enforcement, or credit notes | Control Applicability Matrix records Company/Data Scope as `Unknown` | **Non-blocking** | Targeted documentation pass, or runtime observation |
| GAP-SDV-04 | No documentation evidence on audit trail/event emission for delivery validation, return, or credit-note issuance | Control Applicability Matrix records Audit/Event as `Unknown` | **Non-blocking** | Documentation or runtime pass |
| GAP-SDV-05 | Credit Note amount derivation (automatic vs. manual) not evidenced | SDV-F07 UNKNOWN field | **`CONDITIONALLY VERIFIED CANDIDATE` (2026-10-01/02) — see below** | Documentation or runtime pass (still recommended for final confirmation) |
| GAP-SDV-06 | Same network/egress constraint as Gx1 (`GAP-GRV-08`) — all citations are search-synthesis, not verbatim reads | Slightly lower confidence tier on every claim | **Non-blocking** (disclosed in `19_PROVENANCE_REGISTER.md`) | Same as Gx1 |

## GAP-SDV-05 update (2026-10-01/02) — DeepSeek Atomic Boundary `U05`, `STATE03 BUSINESS PROCESS VERIFICATION AND INTEGRATION CONTROLLER` reconciliation

DeepSeek (Primary Source/Dump Research Worker, separate `STATE03_Odoo19 Deep Research` session) delivered Atomic Boundary `U05` (sales invoicing/delivery) via PR #74, and this session verified it for mechanical integrity (file-hash match, Clean-Room compliance of the neutral-knowledge layer) and internal consistency. A static code-trace finding, bound to this Function-ID (`SDV-F07`): a credit note's effect on billed quantity is **not** restricted to credit notes generated from the sales order itself, contrary to an in-code comment claiming otherwise — a credit note created directly from an invoice still reduces the order line's billed quantity (and can make the order propose re-billing already-credited goods), because the reversal keeps the order-line link regardless of how the credit note was created. DeepSeek itself flagged this as a code-vs-comment contradiction (`VDR-U05-C146`), not an settled fact.

**Status assigned**: `CONDITIONALLY VERIFIED CANDIDATE`, not `CLAUDE-VERIFIED CANDIDATE` — this session confirmed the finding is internally consistent (restricted-evidence claim ↔ neutral-knowledge statement ↔ packet-level counts all agree) and Clean-Room compliant, but has no access to the actual Odoo 19 source tree or restored database itself (that access is DeepSeek's local environment only) and so cannot independently re-derive the cited source pointer. Full detail: `00_Architecture_Governance/STATE03_VDR_CLAUDE_VERIFICATION_LOG.md` §5. **Not a closure** — AWT/runtime confirmation or independent (`CHATGPT_AUDIT`) re-derivation from source is still the route to final confirmation.

## Cross-Gx action taken

`GAP-SDV-01` was pushed back into Gx1: `../GOODS_RECEIPT_VALIDATION_PILOT/AWT_BACKLOG.md` GRV-F04 entry was updated with a cross-reference (not a rewrite of GRV-F04's original documentation-tier finding, which stands as recorded — only the AWT plan was extended to also test this contradiction). This is the Material Delta mechanism working as intended: a later Gx's research improved an earlier Gx's open question without discarding it.

## Status summary

```
GAPS OPEN                 : 6
RESOLVED (2026-09-28, Gx6) : 1 (GAP-SDV-01, was Evidence Conflict)
TARGETED VALIDATION       : 1 (GAP-SDV-02)
CONDITIONALLY VERIFIED CANDIDATE (2026-10-01/02, DeepSeek U05 + Claude verification) : 1 (GAP-SDV-05)
NON-BLOCKING              : 3 (GAP-SDV-03, 04, 06)
```
