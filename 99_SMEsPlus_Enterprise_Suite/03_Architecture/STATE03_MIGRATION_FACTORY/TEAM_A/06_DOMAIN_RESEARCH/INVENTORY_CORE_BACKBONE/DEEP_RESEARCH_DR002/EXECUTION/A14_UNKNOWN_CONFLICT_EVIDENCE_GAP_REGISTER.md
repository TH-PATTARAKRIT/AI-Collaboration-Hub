# A14 — Unknown / Conflict / Evidence Gap Exhaustion Register

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Maintain the one canonical register of every open Inventory unknown/conflict/gap, carrying forward GROUP A's register DELTA-FIRST and adding this pass's own findings | Claude (Team A, DR-002) | This artifact | 2026-08-31 | Independent Evidence Review (pending) | See per-item status | Directly gates A15 Material Unknown Exhaustion Report |

Mandatory fields per item, per DR-002 §7/A14: ID, topic, severity/materiality, exact evidence sought, evidence found, status, impact on Stock Truth, impact on Accounting interface, impact on dependent modules, SaaS/tenant impact, migration impact, Thailand reality impact, next action/stop condition.

## Part 1 — Carried forward from GROUP A frozen evidence (`8b0993d`), reconciled against this pass's own findings

### Critical — 0 open (all 3 resolved before this DR-002 pass began; listed for audit-trail completeness only)

| ID | Topic | Status |
|---|---|---|
| GRPA-Crit-1 | Orphaned two-level approval schema | `RESOLVED` (GROUP A CORR-003, DB-forensics corroborated by Independent Review) |
| GRPA-Crit-2 | Purchase post-confirmation cancellation cascade | `RESOLVED` (GROUP A CORR-003, independently re-verified) |
| GRPA-Crit-3 | `_run_buy()` exact implementation | `RESOLVED` (GROUP A CORR-003; **independently re-confirmed this pass** by this DR-002's own fresh reading of `purchase_stock/models/stock_rule.py — _run_buy()`, reaching the identical conclusion — see A6 §2) |

### High — 3 remain open, carried forward unchanged

| ID | Topic | Severity | Evidence Sought | Evidence Found | Status | Stock Truth Impact | Accounting Interface Impact | Dependent Module Impact | SaaS/Tenant Impact | Migration Impact | Thailand Impact | Next Action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GRPA-H4 | `account.fiscal.position` base model file never located | High | The model definition file | Not found in GROUP A's extraction; not independently re-searched this pass (out of this pass's assigned module scope) | `EVIDENCE_MISSING` | None (Accounting concept) | Indirect — fiscal position affects tax, not stock, but is cited in cross-module dependency evidence | Tax/Accounting | None identified | Low (not stock-record-bearing) | Possible (fiscal position often carries country logic) | Requires a session scoped to Accounting/Tax modules to locate |
| GRPA-H5 | Orphaned `res.partner` brand/HQ columns (`brand_id`, `parent_company_id`, `hq_brand_id`, `is_hq_brand`, `store_type_id`, `bh_parent_company_code`, 13 `x_studio_*`) | High | Owning module for each column | Not found; best candidate for future dump-forensics resolution per GROUP A's own note | `EVIDENCE_MISSING` | Indirect (party master data feeds ship-to/sold-to context) | None | Party/CRM | Medium — unexplained multi-brand/multi-HQ structure could represent an undocumented multi-entity pattern | Medium — orphan columns risk silent data loss if not mapped | Unknown | Requires the blocked DB forensics (A2) to resolve via column-usage statistics |
| GRPA-H8 (= this pass's SAAS-02/TH-INV-01) | Two uncoordinated Thai "branch" modules | High | Reconciliation of the two branch concepts | Confirmed structurally unconnected (GROUP A finding, reused; see A10, A11) | `CONFLICTING PRACTICE` (not merely EVIDENCE_MISSING — this pass upgrades the classification since the conflict itself is now confirmed, not just suspected) | Indirect (branch may scope warehouse/location in a target design) | Indirect (branch may scope journal/tax context) | Sales, Purchase, Accounting | High — directly relevant to SaaS multi-entity/branch design | High — a migration must choose one canonical branch representation | Direct — Thai statutory branch requirement is the reason this exists at all | `REQUIRES REAL USER VALIDATION` before either source pattern is adopted or replaced |

### Medium — 10 items reconciled; **1 resolved this pass**, 1 narrowed, 8 unchanged

| ID | Topic | Status (GROUP A) | Status (this pass) | Note |
|---|---|---|---|---|
| GRPA-M10 | `stock_move.is_in`/`is_out` column semantics | `EVIDENCE_MISSING` | **`RESOLVED`** | This pass's own fresh reading of `stock_account/models/stock_move.py` located and cited: `is_in`/`is_out`/`is_dropship`/`is_valued` — computed+stored booleans via `_is_in()`/`_is_out()` helper methods, `is_valued = is_in or is_out`. See A9 §2 |
| GRPA-M11 | `returned_move_ids` field definition never located | `EVIDENCE_MISSING` | `EVIDENCE_MISSING` (unchanged) | Not encountered by any of this pass's three source-research agents; still not located |
| GRPA-M12 | `produce_line_ids` (likely MRP) | `EVIDENCE_MISSING` | `EVIDENCE_MISSING` (unchanged, near-miss) | This pass's MRP research read `mrp.production`'s move fields in depth (`move_raw_ids`, `move_finished_ids`, `move_dest_ids`, `move_byproduct_ids`, `workorder_ids`) and did not encounter this exact field name — likely lives in a subcontracting/workorder extension module not read this pass |
| GRPA-M13 | Owning module for `sale_order_line.is_service` | `EVIDENCE_MISSING` | `EVIDENCE_MISSING` (unchanged) | Not encountered this pass |
| GRPA-M14 | `product.type` literal `'product'` alongside `'consu'` | `EVIDENCE_MISSING` | **`PARTIALLY VERIFIED`** — narrowed, not closed | This pass's direct reading of the *current* `product.template.type` Selection confirms exactly 3 values (`consu`/`service`/`combo`), no `'product'` literal in the field definition. Whether `'product'` exists as legacy **data** in the dump (not a field option) remains untested (DB restore blocked, A2). See A5 §4 |
| GRPA-M15 | Owning module for remaining `purchase_order_line` unexplained columns | `EVIDENCE_MISSING` | `EVIDENCE_MISSING` (unchanged) | Not in this pass's assigned scope |
| GRPA-M16 | Full contents of `stock_dropshipping/models/stock.py` | `EVIDENCE_MISSING` | `EVIDENCE_MISSING` (unchanged) | Registered in A1 as an explicitly out-of-scope module this pass, not read |
| GRPA-M17 | `stock.rule.Procurement`'s field typing | `RESOLVED` (pre-CORR-003) | **Independently re-confirmed this pass** | This pass's own MRP/routing research agent independently found and cited `Procurement` as a `NamedTuple`, assigned as `StockRule.Procurement` — corroborates the pre-existing resolution via a second, independent read |
| GRPA-M18 | WHT PND form-code correctness vs. current Thai RD rules | `REGULATORY VERIFICATION REQUIRED` | Unchanged | See A11 TH-INV-04 |
| GRPA-M19 | Thai district/sub-district address reaching delivery workflow | `UNKNOWN` | Unchanged | See A11 TH-INV-05; delivery/carrier modules registered out-of-scope in A1 |

### Low — 4 items, unchanged (not independently re-tested this pass, no contrary evidence)

| ID | Topic | Status |
|---|---|---|
| GRPA-L20 | MRP/Repair/Purchase-Requisition extension columns | `EVIDENCE_MISSING`, carried forward |
| GRPA-L21 | `stock_warehouse` MRP/repair/subcontracting extension columns | `EVIDENCE_MISSING`, carried forward |
| GRPA-L22 | `product_template` cold-chain/manufacturing columns | `EVIDENCE_MISSING`, carried forward |
| GRPA-L23 | `num2words` Thai-locale correctness | `EVIDENCE_MISSING`, carried forward |

### Independent Evidence Review's own findings (`626873c`), reused as Boss-classified

| ID | Topic | Boss-directed classification |
|---|---|---|
| IR-1 | PostgreSQL tooling-version documentation inaccuracy (PG16 vs PG18) | `CONTROLLED CARRY-FORWARD, NOT GATE BLOCKING` — this pass's own DB-restore attempt independently reproduces the same PG16→PG18 archive-incompatibility symptom (A2), further corroborating this is a real dump property, not session-specific noise |
| IR-2 | Fit-Gap candidate #15 unqualified generalization | `HYPOTHESIS / REQUIRES REAL USER VALIDATION` (Boss Evidence Gate §4 item 3) |
| IR-3 | Two secondary citations not independently re-opened | `CONTROLLED CARRY-FORWARD` |

## Part 2 — New items surfaced by this DR-002 pass's own deepening research

| ID | Topic | Severity | Evidence Sought | Evidence Found | Status | Stock Truth Impact | Accounting Interface Impact | Dependent Module Impact | SaaS/Tenant Impact | Migration Impact | Thailand Impact | Next Action / Stop Condition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-A9-01 | No `stock.valuation.layer` model exists; codebase version/provenance unconfirmed (no `release.py` found under the given source root) | Medium | Confirm whether this reflects a genuine current-Odoo architecture or a customer-specific/older fork | Structural absence confirmed by exhaustive grep (two independent research agents, A9 §1); version itself unconfirmed | `CONFLICTING EVIDENCE` (structure confirmed; provenance unresolved) | Directly changes what "valuation ledger" means for SMEsPlus to learn from | Direct — this is the core valuation-interface finding | None | None | Low | None | Locate an authoritative version marker for this specific checkout before treating its valuation architecture as representative of "Odoo 18" generally |
| N-A7-03 / N-A9-02 | No date/period-lock/cutoff field evidenced in `stock.quant`/`stock.move`/valuation flow this pass | **High** | Date/effective-date fields and any period-lock mechanism | Not located in the files read this pass | `EVIDENCE_MISSING` | Direct — cutoff timing is a Stock Truth concern | Direct — this is precisely Lane C Cross-Proof scenario 6's evidence requirement | Sales, Purchase, Accounting (all reference timing) | None identified | Medium — cutover timing depends on this | High materiality generally, no Thailand-specific angle found | Blocks full confidence in A16 Cross-Proof scenario 6 until a dedicated pass reads `stock.move`'s date fields and any lock mechanism in full |
| N-A13-02 | Record rules / ACLs governing `company_id` isolation not read this pass | **High** | `ir.rule` definitions scoping `stock.*` models by company | Not read (out of this pass's module scope — `stock/security/` was not opened) | `EVIDENCE_MISSING` | None directly | None | None | Direct — this is the actual enforcement mechanism (or absence of one) for SAAS-01's isolation concern | None | None | Read `stock/security/ir.model.access.csv` and any `ir.rule` XML data before treating company-scoping as either enforced or unenforced |
| N-DB-01 | This session's own DB re-verification of GROUP A's forensics was blocked (A2) | Medium | Independent SQL re-query of the restored dump for any Inventory-specific question beyond what GROUP A's combined Sales+Inventory+Purchase pass already asked | Not obtained — restore blocked by sandbox permission control, not by source access | `EVIDENCE_MISSING — ENVIRONMENTAL, NOT SOURCE, LIMITATION` | Possible (any query not yet asked) | Possible | Possible | None | Possible | None | A session with container/DB-provisioning permission should re-run targeted Inventory-only queries (e.g. `stock_quant` negative-quantity incidence, `stock_move` state distribution) |
| N-CONC-01 | No DB-level row-locking (`SELECT ... FOR UPDATE` or equivalent) evidence traced for quant reservation | Medium | Concurrency-control mechanism for simultaneous reservation attempts on the same bin | Not traced (time-boxed scope) | `EVIDENCE_MISSING` | Direct — race-condition behavior is a Stock Truth concern (Mandatory Question re: "concurrency or race-sensitive facts") | None | None | High — concurrent multi-tenant reservation is exactly this kind of race | Low | None | Read `stock/models/stock_quant.py`'s reservation methods specifically for locking hints (`FOR UPDATE`, `SKIP LOCKED`, `NO WAIT`) in a follow-up pass |
| N-A7-01 | Count-in-progress vs. settled on-hand freeze state unknown | Medium | A model/field/state representing "count in progress, do not allow normal moves" | Not found in `stock_quant.py` | `EVIDENCE_MISSING` | Direct | None | None | None | Medium (affects cutover-during-count safety) | None | Read `stock.inventory`-adjacent wizard/action code (not opened this pass) |
| N-A7-02 | Exact method converting `inventory_diff_quantity` into a posted `stock.move` not traced line-by-line | Low-Medium | The specific action/button method | Inferred from consistent `inventory`-usage-location convention, not directly read | `PARTIALLY VERIFIED` | Direct | Indirect | None | None | Low | None | Trace the exact "apply inventory count" method in a follow-up pass |
| N-A7-04 | Stock freeze/lock concept (beyond count-in-progress) unknown | Low-Medium | Any period-lock/location-lock field | Not found | `EVIDENCE_MISSING` | Direct | Indirect | None | None | Low | None | Same follow-up scope as N-A7-01 |
| N-A12-01 | Cross-year inventory continuity / fiscal-year-boundary handling unknown | Low-Medium | Year-end-closing-specific Inventory field/method | Not found in modules read | `EVIDENCE_MISSING` | Direct | Direct (ties to Accounting's own period-close) | None | None | Medium | None | Requires Accounting-side period/closing modules to be read jointly |
| N-A13-01 | `product.qty_available._inverse_qty_available()` not read in full — ambiguous which side is "source of truth" during a manual edit | Low | Full method body | Method's existence and general purpose confirmed; not read line-by-line | `PARTIALLY VERIFIED` | Direct | None | None | None | Low | None | Read the inverse method in full in a follow-up pass |
| N-A5-02 | Expiration date handling (`product_expiry` module) not researched | Low-Medium | Field/model evidence | Module confirmed present in source tree (A1); fields not read | `EVIDENCE_MISSING — NOT YET RESEARCHED` | Direct | None | None | None | Medium (perishable-goods migration) | Possibly high for food/pharma SMEs | Dedicated follow-up pass on `product_expiry` |
| N-A5-03 | Owner/consignment workflow not researched beyond `stock.quant.owner_id` existing as a bin key | Low-Medium | Dedicated consignment model/wizard evidence | Not found; not searched for specifically | `EVIDENCE_MISSING — NOT YET RESEARCHED` | Direct | None | None | None | Medium | Unknown | Dedicated follow-up pass |

## Part 3 — CORR-005 Reconciliation of the Five High Items (2026-09-01)

This section reconciles all five originally-open High items (Part 1's GRPA-H4/H5/H8, Part 2's N-A7-03/N-A9-02 and N-A13-02) against Independent Review IER-003 (`45c749eae826642872ccc2dc09f0f714932c5b8e`, branch `audit/inventory-core-dr002-independent-review-003`) and the Boss Inventory Scope Ruling (`BOSS_INVENTORY_SCOPE_RULING_BH_EXCLUSION_AND_BRANCH_BASELINE_2026_09_01.md`). Per DR-002/CORR-005 governance discipline, this is a documentation reconciliation, not new primary research — every citation below was already established by IER-003; this pass folds it into TEAM A's own register. The original rows in Part 1/Part 2 above are left intact for audit-trail continuity; this section is the authoritative current disposition.

| ID | Original DR-002 status | IER-003 independent verdict | Boss disposition | CORR-005 reconciled classification | Evidence |
|---|---|---|---|---|---|
| GRPA-H4 (fiscal position) | `EVIDENCE_MISSING` | `VERIFIED CLOSED` | N/A — no scope ruling needed | **`RESOLVED`** — not an open Inventory research blocker, not a carry-forward | `01 ACCOUNT/account/models/partner.py:27` (`_name = 'account.fiscal.position'`), read by IER-003 [04](../../../../../INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IER_003/EXECUTION/04_IER003_HIGH_H1_FISCAL_POSITION_BOUNDARY_REVIEW.md) |
| GRPA-H5 (partner brand/HQ, = H2) | `EVIDENCE_MISSING` | `PARTIALLY VERIFIED — TARGETED CORRECTION REQUIRED` (owning module identified: `bh_parent_company`, author BHPRO; source absent) | `CLOSED BY BOSS SCOPE EXCLUSION / LEGACY MIGRATION DATA CARRY-FORWARD ONLY` — `bh_*`/`bhpro_*` excluded from SMEsPlus source learning | **`CONTROLLED MIGRATION CARRY-FORWARD`** — removed from open Inventory research blockers; NOT proven as target logic (scope exclusion is not implementation proof) | `ir_model_data`/`ir_module_module` provenance query, IER-003 [05](../../../../../INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IER_003/EXECUTION/05_IER003_HIGH_H2_PARTNER_BRAND_HQ_FORENSIC_REVIEW.md); Boss Scope Ruling §1.1 |
| GRPA-H8 (Thai branch, = H3) | `CONFLICTING PRACTICE` | `CONFLICTING EVIDENCE` + `REQUIRES REAL USER VALIDATION` (structural conflict confirmed; "child `res.company`" characterization corrected — see A5 §3) | `CLOSED AS AN INVENTORY ARCHITECTURE QUESTION` — approved SaaS Tenant/Company/Branch baseline not reopened by Inventory | **`CONTROLLED MIGRATION / TBRAC CARRY-FORWARD`** (branch vs. `company_registry` mapping) + **`ACCOUNTING/TAX CARRY-FORWARD`** (tax-document branch semantics) — removed from open Inventory research blockers; Inventory does not own the Branch model | `l10n_th`/`l10n_th_partner` module read, `res_company` cardinality check, IER-003 [06](../../../../../INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IER_003/EXECUTION/06_IER003_HIGH_H3_THAI_BRANCH_TBRAC_REVIEW.md); Boss Scope Ruling §1.2 |
| N-A7-03 / N-A9-02 (cutoff, = H4) | `EVIDENCE_MISSING` | `VERIFIED CLOSED` | N/A — no scope ruling needed | **`RESOLVED`** — not an open Inventory research blocker, not a carry-forward | `stock/models/stock_move.py:28-193`, `stock_account/models/stock_picking.py` (full), IER-003 [07](../../../../../INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IER_003/EXECUTION/07_IER003_HIGH_H4_CUTOFF_TIMING_REVIEW.md) |
| N-A13-02 (company ACL, = H5) | `EVIDENCE_MISSING` | `VERIFIED WITH CONDITIONS` (ORM-layer enforcement confirmed; SAAS-03 DB-layer gap separately unchanged) | N/A — no scope ruling needed | **`RESOLVED (ORM-layer)`** — not an open Inventory research blocker, not a carry-forward. `FUTURE IMPLEMENTATION/TEST CARRY-FORWARD`: whether every code path (`stock_account`/`sale_stock`/`purchase_stock`/`mrp`) actually routes through the standard ORM (vs. `sudo()`) was not audited — a future implementation/test verification item, not a source-research blocker | `stock/security/ir.model.access.csv` (full), `stock/security/stock_security.xml` (full), IER-003 [08](../../../../../INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IER_003/EXECUTION/08_IER003_HIGH_H5_COMPANY_ACL_TENANT_REVIEW.md) |

**Net effect on the High-severity tier: 0 of 5 remain open Inventory research blockers.** 3 are fully `RESOLVED` (H1/GRPA-H4, H4/N-A7-03+N-A9-02, H5/N-A13-02's ORM-layer question); 2 are `CONTROLLED CARRY-FORWARDS` reclassified out of Inventory's research scope by binding Boss ruling (H2/GRPA-H5, H3/GRPA-H8) — neither is proven as target-architecture fact, and neither is silently dropped; both remain explicitly tracked (A12 §12, A10 CORR-005 note, A17 quarantine row). SAAS-03 (DB-layer constraint enforcement, A10) is a **distinct, separate** item, explicitly confirmed unchanged and still open by IER-003 — this reconciliation does not touch it. Medium item GRPA-M14 and all other Medium/Low items are out of this reconciliation's five-High scope and are unchanged.

No Unknown was converted to a Fact by this reconciliation: every `RESOLVED` disposition cites a primary-source read (file, line, or query) reproduced by IER-003; every `CONTROLLED CARRY-FORWARD` disposition is a scope/governance decision by Boss, explicitly not presented as technical proof.

## Mechanical count reconciliation

### As of original DR-002 session close (2026-08-31) — preserved for audit trail

- **Critical open: 0.**
- **High open: 5** (GRPA-H4, GRPA-H5, GRPA-H8, N-A7-03/N-A9-02, N-A13-02).
- **Medium open: 12** (9 unchanged GROUP A Medium items [GRPA-M11–M13, M15, M16, M18, M19 = 7, plus GRPA-M14 downgraded-but-still-open = 8, wait recount below] + this pass's N-DB-01, N-CONC-01, N-A7-01, N-A7-02, N-A7-04, N-A12-01).
- **Medium item recount for precision**: GROUP A Medium items still open after this pass = GRPA-M11, M12, M13, M15, M16, M18, M19 (7 unchanged) + GRPA-M14 (narrowed to PARTIALLY VERIFIED, still open) = **8** GROUP A Medium items open; plus this pass's own 6 new Medium items (N-DB-01, N-CONC-01, N-A7-01, N-A7-02, N-A7-04, N-A12-01) = **14 Medium open total**. (GRPA-M10 and GRPA-M17 move to Resolved this pass.)
- **Low open: 6** (GRPA-L20–L23 = 4 unchanged, + N-A13-01, N-A5-02, N-A5-03 = 3 new — **7 Low open total**, correcting the running count once more: 4 + 3 = 7).
- **Resolved this pass: 2** (GRPA-M10, GRPA-M17) **plus 3 pre-existing Critical resolutions independently re-confirmed** (not newly resolved, corroborated).
- **Total open (2026-08-31): 0 + 5 + 14 + 7 = 26.** Independently mechanically re-verified, exact match, by IER-003 [10](../../../../../INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IER_003/EXECUTION/10_IER003_UNKNOWN_REGISTER_COUNT_RECONCILIATION.md).

### CORR-005 reconciled counts (2026-09-01) — current authoritative view, per Part 3 above

This package distinguishes two views, per the CORR-005 governing prompt: items still actionable by further authorized Inventory source research (**Open Inventory Research Blockers**), and items no longer Inventory-blocking but tracked for another workstream (**Controlled Carry-Forwards**). A Boss scope exclusion is not counted as technical closure — Part 3's `RESOLVED` items (evidence-verified) and `CONTROLLED CARRY-FORWARD` items (scope/governance-reclassified) are kept in separate rows below for exactly that reason.

**View 1 — Open Inventory Research Blockers** (recomputed from the reconciled register; only severities/items actually changed by this reconciliation are recomputed, all others carried forward unchanged from the 2026-08-31 count above):

| Severity | Open (2026-08-31) | Change this reconciliation | Open (2026-09-01) |
|---|---:|---|---:|
| Critical | 0 | none | **0** |
| High | 5 | −5: GRPA-H4 and N-A7-03/N-A9-02 and N-A13-02 → `RESOLVED`; GRPA-H5 and GRPA-H8 → `CONTROLLED CARRY-FORWARD` (moved to View 2, not deleted) | **0** |
| Medium | 14 | none — no Medium item is among the five High items reconciled here; GRPA-M14 and all Part 2 Medium items are unchanged and out of this reconciliation's scope | **14** |
| Low | 7 | none | **7** |
| **Total open Inventory research blockers** | **26** | −5 | **21** |

**View 2 — Controlled Carry-Forwards** (new classification; these are not counted in View 1 and are not Inventory Gate blockers):

| ID | Carry-forward type | Owner / next action |
|---|---|---|
| GRPA-H5 (H2) | `CONTROLLED MIGRATION CARRY-FORWARD` | Migration — preserve legacy `bh_parent_company`-owned column data so it is not lost; external vendor/customer source acquisition (not a Team A task) if internal logic is ever needed |
| GRPA-H8 (H3) | `CONTROLLED MIGRATION / TBRAC CARRY-FORWARD` + `ACCOUNTING/TAX CARRY-FORWARD` | Migration/TBRAC — real Thai-business-user validation of which legacy branch field was operationally trusted; Accounting/Tax — tax-document branch semantics |
| N-A13-02 residual | `FUTURE IMPLEMENTATION/TEST CARRY-FORWARD` | Whether every `stock_account`/`sale_stock`/`purchase_stock`/`mrp` code path actually routes through the standard ORM (vs. `sudo()`) — a future implementation/test verification item |

**Total: 21 open Inventory research blockers (0 Critical / 0 High / 14 Medium / 7 Low) + 3 controlled carry-forwards (not Inventory-blocking, not silently dropped).** This is the recomputed figure per the reconciled package — it is not a mechanical copy of the original `0/5/14/7` count.

No Unknown was converted to a Fact anywhere in this register. No item is silently dropped.

No Evidence = No Progress. DELTA-FIRST. No Material Unknown Exhaustion = No Inventory Evidence Gate PASS.
