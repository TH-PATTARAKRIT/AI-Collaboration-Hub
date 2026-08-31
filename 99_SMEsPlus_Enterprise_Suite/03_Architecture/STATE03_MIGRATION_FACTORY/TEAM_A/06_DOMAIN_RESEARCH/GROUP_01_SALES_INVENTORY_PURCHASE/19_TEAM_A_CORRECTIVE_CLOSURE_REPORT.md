> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-31-MIG-A-GRPA-SIP-CORR-003 | Targeted Evidence-Gap Corrective Closure
> Supersedes nothing in the original 18-deliverable evidence chain — this report documents what this corrective
> session added/closed/narrowed on top of it. All original deliverables (01-18) remain in place with their
> original content intact; affected sections carry inline "CORRECTIVE UPDATE (Session CORR-003)" additions.

# 19 — TEAM A CORRECTIVE CLOSURE REPORT

## 01 — Terminal Recommendation

```
TEAM A CORRECTIVE CLOSURE COMPLETE — READY FOR INDEPENDENT EVIDENCE REVIEW
```

Not a Formal Evidence Gate PASS, Team B authorization, IBPV/IDTM/IESA Formal PASS, Development Ready, or Boss
Approved — same restriction that applied to the original session's terminal status.

## 02 — Scope Executed

All four correction clusters from the governing prompt were executed to completion:

| Cluster | Target | Result |
|---|---|---|
| A | Purchase post-confirmation cancellation cascade (Critical #2, High #9) | **CLOSED** |
| B | Procurement → Purchase handoff: `_run_buy()`, `'buy'` registration, MTO re-trigger site (Critical #3, High #6, High #7) | **CLOSED** (all 3 sub-gaps) |
| C | Orphaned two-level approval schema (Critical #1) | **CLOSED** via full data+schema dump restore and row-level forensics — the corrective prompt's own mandated "existing dump first" step, performed before any consideration of live-system access |
| D | Evidence manifest / report integrity wording | **CLOSED** — wording corrected, this report and the final hash manifest created |

## 03 — Method Summary

- **Clusters A and B**: two parallel, independent, read-only source-code research passes (subagents), each
  reading the specific files/methods left unopened by the original session, with explicit instructions not to
  assume symmetry with already-documented behavior. Both closed all assigned gaps with exact file+line citations.
- **Cluster C**: PostgreSQL 16 was installed locally (Homebrew) specifically for this investigation. The full
  `iTEST02` dump (not just its schema, which was all the original session had extracted) was restored into a
  scratch database (`pg_restore -j4`; 18 restore errors, all isolated to an unrelated `pgvector`-dependent
  AI-embedding table and one harmless unrecognized GUC — neither touches any table relevant to this
  investigation). Direct SQL queries against `ir_model_fields`, `ir_model_data`, `ir_module_module`, and the
  actual data rows of `sale_order`/`purchase_order`/`purchase_request` resolved the mystery definitively. The
  scratch database was stopped and is not persisted anywhere; no live/production system was touched.
- **Cluster D**: a wording audit found one place (`18_TEAM_A_EVIDENCE_GATE_CANDIDATE_REPORT.md`'s Gate Status
  table) that overstated SHA-256 coverage ("18/18" when only 16 content files were hashed); corrected in place,
  plus a note added to `17_GROUP_A_EVIDENCE_MANIFEST.md` explaining why files hashing themselves is not possible.

## 04 — Items Closed (full detail in the cited files)

1. **Purchase's `button_cancel()` cascade into `stock.picking`/`stock.move`** — traced to
   `purchase_stock/models/purchase_order.py` L186-233. State-partitioned: not-yet-received orders get a full
   cancel+unreserve; partially-received orders are never ambiguous because Odoo's own backorder mechanics
   guarantee the completed portion is always already split onto its own (spared) picking before cancellation
   logic runs; fully-received orders are untouched beyond a chatter note. `stock.picking.action_cancel()` itself
   confirmed to be generic/shared code, not Purchase- or Sale-specific.
2. **`_run_buy()`'s exact implementation** — traced to `purchase_stock/models/stock_rule.py` L58-165. Resolves a
   vendor via `product.supplierinfo`, searches for and reuses an existing draft PO on a vendor/company/
   picking-type/currency/(optional RFQ-window) domain before creating a new one, batches new/updated PO lines,
   and the created line carries `move_dest_ids` linking back to the originating chained stock move via the
   `stock_move_created_purchase_line_rel` junction table.
3. **`'buy'` action registration** — confirmed verbatim: `purchase_stock/models/stock_rule.py` L18-20,
   `selection_add=[('buy','Buy')]`.
4. **MTO re-trigger call site** — confirmed at `stock/models/stock_move.py` L1580, inside `_action_confirm()`;
   `_action_assign()` independently confirmed to NOT re-trigger.
5. **The orphaned two-level approval schema** — resolved to three real, actively-installed Odoo modules via
   row-level dump forensics: `sale_order_level_approve` (first-party, author "SMEsPlus"),
   `purchase_request_level_approve_po` and `purchase_request_level_approve` (third-party, author "BH Pro
   International"). All three show `state='installed'` in `ir_module_module` with real version numbers; their
   fields show `state='base'` in `ir_model_fields` (Python-declared, not Studio); the modules' source code is
   simply absent from the `SOURCE CODE` extraction Team A was given. Live data confirms genuine historical usage
   (heaviest on Purchase Request: 1,945 `approved`, 96 `rejected` of 2,199 records).
6. **A secondary, distinct finding**: `x_review_result`/`x_has_request_approval`/`x_need_approval` are confirmed
   genuine Odoo-Studio/dynamic fields (`state='manual'`), present only on Purchase Order/Request (never Sale
   Order), with a compute snippet referencing the `multi_level_approval` engine's `multi.approval.type` model —
   real but non-functional in this database snapshot (that engine's own tables were confirmed to not exist here),
   and touching only 10 Purchase Order rows and 4 Purchase Request rows in a narrow 2-day window.
7. **A bonus discovery, not originally sought**: live `purchase_order.state` includes `to_check_level` (131 of
   27,874 rows) — a value not present in the base `purchase` module's Selection documented in the original
   session's Phase 4 research. Direct evidence that `purchase_request_level_approve_po` extends the state machine
   itself.
8. **Evidence manifest integrity wording** — corrected.

## 05 — Items Narrowed But Still Open

| Item | What's now known | What's still unknown |
|---|---|---|
| The three approval modules' internal workflow logic | WHO owns them, THAT they're real/installed/used, WHAT the DB-level field shape is, and (for Purchase Order) that `level1_approved_by`/`reject_reason` are populated on 0 of 27,874 rows despite `level1_user_id` being populated on 98.5% | The exact button/method-level logic (what triggers `to_check_level`, what the approval buttons actually do) — requires the modules' source code, not obtainable from this dump |
| The `multi_level_approval` Studio pilot's fate | It exists, is real, references a genuinely-uninstalled engine, and touched a tiny fraction of records in a narrow window | Whether it was deliberately abandoned, superseded by the two BH Pro modules, or something else — inference only |
| `res.partner` multi-brand/HQ orphaned columns (High #5) | Unchanged — not in scope for this corrective session's four clusters | Same dump-forensics technique that resolved Critical #1 could plausibly resolve this in a future session |
| `account.fiscal.position`'s base model (High #4) | Unchanged | Not addressed this session |
| Two uncoordinated Thai "branch" modules (High #8) | Unchanged | Not addressed this session |

## 06 — Files Changed / Created

**Modified (inline "CORRECTIVE UPDATE (Session CORR-003)" additions, original content preserved)**:
`02_INVENTORY_CAPABILITY_MODEL.md`, `04_PURCHASE_CAPABILITY_MODEL.md`, `05_INTEGRATED_E2E_LIFECYCLE_MAP.md`,
`06_CROSS_MODULE_EVENT_AND_DEPENDENCY_MAP.md`, `07_BUSINESS_FACT_OWNERSHIP_AND_HANDOFF_MATRIX.md`,
`08_SOURCE_DATABASE_SEMANTIC_TRACEABILITY_MATRIX.md`, `13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md`,
`14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md`, `16_FIT_GAP_CANDIDATE_PACK.md`, `17_GROUP_A_EVIDENCE_MANIFEST.md`,
`18_TEAM_A_EVIDENCE_GATE_CANDIDATE_REPORT.md`.

**Not modified** (no material change identified for this corrective session's scope):
`01_SHARED_MASTER_DEPENDENCY_MAP.md`, `03_SALES_CAPABILITY_MODEL.md`, `09_QUANTITY_SEMANTICS_REGISTER.md`,
`10_EXCEPTION_PARTIAL_RETURN_CANCELLATION_MATRIX.md`, `11_THAILAND_BUSINESS_REALITY_AND_VARIATION_REGISTER.md`,
`12_PERSONA_USER_FITNESS_OBSERVATION_MATRIX.md`, `15_EXTERNAL_DEPENDENCY_AND_SYSTEM_RISK_OBSERVATION_REGISTER.md`.

**Created**: `19_TEAM_A_CORRECTIVE_CLOSURE_REPORT.md` (this file), `20_GROUP_A_FINAL_SHA256_MANIFEST.txt`.

## 07 — Updated Gap Counts

| Tier | Before CORR-003 | After CORR-003 |
|---|---|---|
| Critical | 3 | **0** |
| High | 6 | 3 (items 4, 5, 8 — unchanged, out of this session's scope) |
| Medium | 10 | 10 (one item, `stock.rule.Procurement`'s field typing, was already closed before this session and remains closed) |
| Low | 4 | 4 |
| Resolved (audit trail) | 5 | **9** (R1-R5 from the original session, R6-R8 from this one, plus the Cluster D wording fix) |

## 08 — Non-Generalization / Governance Compliance Statement

Per TBRAC guidance (extended to this corrective session's approval findings): the specific usage patterns
discovered (e.g., 96.9% of `purchase_order.level1_user_id` values being a single default-looking user ID; the
near-total absence of `level1_approved_by` population on Purchase Order) describe **this customer's specific
historical operational practice in this specific dump snapshot**. They are not evidence of Thai-wide, industry-
wide, or even universally-current practice for this customer. No finding in this corrective session was promoted
beyond what the data directly shows.

## 09 — Branch / Commit Lineage

- Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
- Working branch (unchanged from the original session): `claude/group-a-sales-inventory-purchase-dr002`
- Prior terminal commit (verified against GitHub before this session began): `cfd1e2adb8ddeb34ea1d59eb33f6ab35a94c21df`
- Canonical governance baseline verified at session start: `f3e365e7cfe64d28769d1479a448f1fd7a216446`
  ("governance: supersede historical ChatGPT venue for GROUP A execution")
- This corrective session's commit(s): recorded in the final closure message and in
  `20_GROUP_A_FINAL_SHA256_MANIFEST.txt`'s generation timestamp context.
- No merge into `SMEsPlus` was performed or requested. No live/production system was written to at any point —
  the only database written to was a local, scratch, non-persisted PostgreSQL instance created and destroyed
  within this session for read-only forensic querying.

## 10 — Boss Exception / Override

NONE. This corrective session operated entirely under the standing autonomous end-to-end authorization in its own
governing prompt. No STOP/HOLD condition, scope-expansion request, frozen-baseline conflict, clean-room boundary
crossing, destructive/irreversible action, or cross-team-authority requirement arose during execution.
