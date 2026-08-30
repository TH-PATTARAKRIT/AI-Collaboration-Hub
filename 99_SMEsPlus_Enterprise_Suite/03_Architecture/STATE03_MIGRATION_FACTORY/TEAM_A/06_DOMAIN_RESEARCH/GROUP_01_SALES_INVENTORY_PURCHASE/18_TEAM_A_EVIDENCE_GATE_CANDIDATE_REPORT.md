> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Team A Evidence Gate Candidate Report

# 18 — TEAM A EVIDENCE GATE CANDIDATE REPORT

## 01 — Terminal Status

```
TEAM A EVIDENCE GATE CANDIDATE — READY FOR INDEPENDENT REVIEW
```

This status is NOT a claim of Team B Design Approval, IBPV Formal PASS, Development Readiness, IDTM/IESA Formal
PASS, Release, Production, or Boss Approval. It means: the phases planned for this session are executed or
explicitly justified, findings are evidence-traceable, unknowns are preserved (not guessed), clean-room boundaries
were respected, and the required deliverable set is complete and internally consistent.

## 02 — Execution Summary

| Phase | Status | Deliverable(s) |
|---|---|---|
| 0 — Governance/Scope/Source/Legal/Evidence Baseline | Complete (delivered as the session's first-turn output, prior to this report) | — |
| 1 — Shared Master Dependency Learning | Complete | 01 |
| 2 — Inventory Core / Physical Reality Learning | Complete | 02 |
| 3 — Sales / Commercial Demand & Fulfillment Learning | Complete | 03 |
| 4 — Purchase / Supply & Receipt Learning | Complete | 04 |
| 5 — Cross-Module E2E Reconciliation | Complete | 05 |
| 6 — Exception/Partial/Return/Cancel/Correction Observation | Complete | 06, 07, 10 |
| 7 — Source↔Database↔Business Semantic Reconciliation | Complete | 08, 09 |
| 8 — Thailand Business Reality/Variation/User-Fitness Evidence | Complete | 11, 12 |
| 9 — Vendor-Neutral Capability/Lifecycle/Event/Dependency Consolidation | Complete (folded into Phases 5-7's deliverables per the evidence actually produced) | 05, 06, 07, 13 |
| 10 — Fit-Gap Candidate / Unknown / Conflict Handoff | Complete | 14, 15, 16 |

All 10 phases executed. No phase was skipped or deferred without the justification already recorded inline in
the relevant deliverable (e.g., Phase 9's content was produced across Phases 5-7's outputs rather than as a
separate late-stage pass, since the invariant/consolidation material was already fully evidenced by that point).

## 03 — Deliverables Complete / Total

**18 / 18** semantic deliverables required by governance §22 are present (see `17_GROUP_A_EVIDENCE_MANIFEST.md` for
the full file list and SHA-256 integrity values).

## 04 — Evidence Added (this session)

- Extracted a full schema-only DDL (~214,294 lines) from the `iTEST02` PostgreSQL dump via `pg_restore
  --schema-only` — no live database required — providing real, verifiable DB evidence for every phase, including
  table/column existence, FK targets, and CHECK constraints (or their absence).
- Read, in full or substantial part, the base `sale`, `purchase`, `stock`, `product`, `base`, `uom`, `account`
  (targeted), `analytic`, `purchase_requisition`, `purchase_requisition_stock` modules, the bridge modules
  `sale_stock`, `purchase_stock`, `sale_purchase`, `sale_purchase_stock`, the OCA `purchase_request` module, and a
  dozen+ SMEsPlus/Thai-localization `addons_extra` modules.
- Every material claim across all 16 content deliverables is cited to an exact file+line or exact DB
  table/column — no claim was escalated from UNKNOWN/EVIDENCE_MISSING to FACT anywhere in this evidence chain.

## 05 — Unknowns / Conflicts (see `14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md` for full detail)

**3 Critical, 6 High, 10 Medium, 4 Low** open items, plus **5 items resolved during this research effort** (audit
trail preserved). The single highest-priority Critical item — an orphaned two-level manager-approval DB schema
spanning `sale_order`, `purchase_order`, and `purchase_request` with zero corresponding source code anywhere —
was investigated across two full research phases (Sales, Purchase) and is genuinely unresolvable from source code
alone; it requires a row-level data pull (`ir_model_fields`/`ir_model_data`) that is out of this session's
read-only-source scope.

## 06 — Red Flags

1. **The orphaned approval schema** (§05 above) — the top item carried to Fit-Gap and to whoever gates Team B.
2. **Purchase's post-confirmation cancellation cascade into `stock.picking` was never verified** — Sale's
   equivalent is test-confirmed; Purchase's is not, creating an asymmetric confidence level between the two
   commercial modules on this one specific behavior.
3. **A recurring pattern of uncoordinated duplicate customizations** was found at least three times independently
   (two Thai "branch" modules, two `default_code` auto-generators, two byte-identical "amount to text" modules) —
   this is a build-hygiene/governance signal about how this codebase has evolved, worth surfacing to the Boss
   independent of any single finding's content.
4. **No DB CHECK constraints exist anywhere in the Inventory/Movement layer, and only a handful exist on
   Sale/Purchase headers** — every business rule in this domain is application-layer only; a migration approach
   that writes data via direct SQL bypasses all of it. This is a structural risk for the migration approach
   itself, not a defect in the source system.

## 07 — Next Action

Recommended, in priority order:
1. Boss/Team-B review of the orphaned two-level approval schema (§05/§06 item 1) — ideally with a row-level data
   pull from the live system, since this is genuinely outside what read-only source research can resolve.
2. A short, targeted follow-up pass (not a full new session) to open `purchase_stock`'s `button_cancel()`
   override and `stock.rule.py`'s `_run_buy()`/`make_to_order` re-trigger call site — both are narrow,
   well-scoped gaps, not broad unknowns.
3. Team B may begin independent design work using this evidence chain as input, subject to the Boss Gate this
   project already has in place for Domain 01 (Accounting Core) — this report does not itself authorize that
   transition.

## 08 — Gate Status

| Check | Status |
|---|---|
| Required research phases executed or explicitly justified | ✅ |
| Material findings traceable to evidence | ✅ |
| Source↔DB conflicts resolved or registered | ✅ (3 conflicts found, all resolved in favor of code+schema agreement over stale documentation; see `08_SOURCE_DATABASE_SEMANTIC_TRACEABILITY_MATRIX.md` §04) |
| Unknowns preserved (not guessed) | ✅ (23 open items across 4 severity tiers, none resolved by invention) |
| Clean-room boundaries respected | ✅ — no vendor source code, schema, or architecture was copied into a target design; this entire evidence chain is business-fact/semantic extraction only, per the governing directive |
| Thailand claims evidence-classified | ✅ — every Thailand-related finding uses the TBRAC vocabulary and is deliberately capped below "Verified Thai Business Reality" per governance §17's stricter rule |
| Required deliverables and evidence manifest present | ✅ (18/18, SHA-256 verified) |
| No hidden Scope expansion occurred | ✅ — all research stayed within Sales/Inventory/Purchase plus the minimum Shared-Master dependency depth required; Accounting Core, MRP, CRM, and e-commerce were only registered as external dependencies (§15), never researched in depth |
| Downstream work has NOT begun | ✅ — no target schema, target API, or target architecture was proposed anywhere in this evidence chain; the Fit-Gap pack (#16) explicitly defers all ADAPT/EXTEND/REJECT/UNKNOWN calls to Team B/Boss |
| Team A Evidence Gate Candidate Report produced | ✅ (this document) |

## 09 — Boss Exception / Override

NONE. This session operated under the standing autonomous-execution authorization the Boss gave mid-session
(after Phase 1 completed) to continue through Phase 10 without routine confirmation, including committing and
pushing evidence to a dedicated branch. No STOP/HOLD condition, scope-expansion request, frozen-baseline conflict,
clean-room boundary crossing, destructive action, or cross-team-authority requirement arose during execution.

## 10 — Closure Statement

Per governance §27, this report, together with the full evidence chain (files 01-17), is committed to the
controlled GitHub project path on branch `claude/group-a-sales-inventory-purchase-dr002` at repository
`TH-PATTARAKRIT/AI-Collaboration-Hub`. No merge into the `SMEsPlus` branch has been performed or requested — that
decision is reserved for the project's existing Boss Gate / PMO Verification process. This session is closed as
`TEAM A EVIDENCE GATE CANDIDATE — READY FOR INDEPENDENT REVIEW`, not as any downstream gate.
