# Inventory Full Reopen — Full Coverage Status Register (40 Mandatory Items)

Session: `SMEPLUS-26-09-02-INV-REOPEN-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-06 OUTPUT — COVERAGE REGISTER COMPLETE — NOT A GATE DECISION`

Compiled from deliverables `03`–`12` (9 Veto Council/Special Team convergence documents + the Stockable/Consumable/Service deep proof) and `01` (prior-evidence fingerprint index). Per item: **Prior Status / Prior Evidence / Delta / Current Evidence / Unknown / Special Team / Accounting Dependency / Gate Impact**. "Accounting Dependency" uses the CP-07 taxonomy: `INVENTORY_OWNED_STOCK_FACT` / `ACCOUNTING_INTERFACE_REQUIREMENT` / `PENDING_ACCOUNT_SESSION` / `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` / `OUT_OF_INVENTORY_SCOPE`.

---

### 1. Product/inventory-management classification
**Prior:** DR-002 documented source `type`/`is_storable` gate as fact only. **Delta:** dedicated deep-proof commissioned (`INV-FP-13`). **Current:** Two-axis model confirmed (`type`×`is_storable`), not a flat 3-way field; 989/83,753 real rows violate the theoretical invariant; matches Thai วัสดุสิ้นเปลือง accounting concept for the partial-rigor tier (deliverable `12`). **Unknown:** type/is_storable tie-break rule when they disagree; Consumable sub-bucketing. **Special Team:** ROUTING research pass. **Accounting Dependency:** `ACCOUNTING_INTERFACE_REQUIREMENT` (WHT correlation). **Gate Impact:** `CARRY_FORWARD` — informs Team B, not implementation-ready.

### 2. Product variants
**Prior:** Not separately researched in DR-002. **Delta:** none surfaced this round. **Current:** No track produced dedicated variant evidence. **Unknown:** whole item. **Special Team:** none assigned. **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `UNKNOWN — STILL MATERIAL`, not yet a named blocker.

### 3. UOM and conversion
**Prior:** DR-002 A3/A5: no `uom.category` model, tree-based conversion, global rounding precision — `CLOSED_WITH_EVIDENCE`. **Delta:** Track 04 Special Team fresh read. **Current:** `_compute_quantity()` default rounding is `'UP'`, not neutral; `relative_factor` edits are non-retroactive (`uom_uom.py:79-93`) — a historical-continuity risk additive to `N-A12-01`. **Unknown:** whether SMEsPlus needs per-UOM rounding. **Special Team:** IDTM. **Accounting Dependency:** `ACCOUNTING_INTERFACE_REQUIREMENT` (conversion affects valuation). **Gate Impact:** `CARRY_FORWARD`.

### 4. Warehouse
**Prior:** DR-002 A5: config record, not a quantity ledger. **Delta:** IESA Special Team. **Current:** `reception_steps`/`delivery_steps` regenerate the `stock.rule`/`stock.route` graph on write (not static data) — a SaaS-provisioning-template risk (`SAAS-04`) for tenant cloning. **Unknown:** target provisioning-template design. **Special Team:** IESA. **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CARRY_FORWARD`.

### 5. Location
**Prior:** DR-002 A5: 7-value `location.usage` enum. **Delta:** none. **Current:** confirmed clean, exhaustive enumeration — `CLOSED_WITH_EVIDENCE`. **Unknown:** none material. **Special Team:** IESA (confirmatory). **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CLOSED_WITH_EVIDENCE`.

### 6. Company/tenant ownership
**Prior:** `N-A13-02` VERIFIED WITH CONDITIONS. **Delta:** conditions re-extracted for the first time this reopen (Track 07 primary task). **Current:** comprehensive 16-model company-scoped `ir.rule` table (ORM layer) confirmed by four independent reads; `SAAS-03` (no DB-layer backstop) and the `sudo()`-bypass audit (never performed) remain open, named residuals; `company_id` is the *only* organizational scope on `stock.move` (`SAAS-01`). **Unknown:** warehouse-level (intra-company) authorization — no evidence either way. **Special Team:** Security (07), corroborated by IESA (05) and AI Control (09). **Accounting Dependency:** `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` (shared `ir.rule` pattern with Accounting's own side per A16 scenario 9, itself unverified). **Gate Impact:** `CARRY_FORWARD`.

### 7. Demand/planned quantity
**Prior:** `CLOSED_WITH_EVIDENCE`, `stock.move.product_uom_qty`. **Delta:** none. **Current:** reconfirmed by both IBPV Council and Special Team, no contradiction. **Unknown:** none. **Special Team:** IBPV (confirmatory). **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CLOSED_WITH_EVIDENCE`.

### 8. Reservation/allocation
**Prior:** `CLOSED_WITH_EVIDENCE`, `_action_assign`/`_update_reserved_quantity`. **Delta:** row-locking re-verified (see item 37). **Current:** reconfirmed; `is_storable=False` bypass noted as additive detail. **Unknown:** none on the mechanism itself. **Special Team:** IBPV/IDTM. **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CLOSED_WITH_EVIDENCE`.

### 9. On-hand
**Prior:** `CLOSED_WITH_EVIDENCE`, `stock.quant.quantity`. **Delta:** none on the fact; schema-integrity caveat carried under item 37. **Current:** reconfirmed by 3 independent reading passes (DR-002, IDR-007, this reopen's IDTM Special Team). **Unknown:** empirical incidence of negative on-hand in real data (`N-DB-01`, blocked). **Special Team:** IDTM. **Accounting Dependency:** `ACCOUNTING_INTERFACE_REQUIREMENT`. **Gate Impact:** `CLOSED_WITH_EVIDENCE` (fact) / `CARRY_FORWARD` (empirical incidence).

### 10. Available/free
**Prior:** `CLOSED_WITH_EVIDENCE`. **Delta:** clamp mechanism detail added. **Current:** `_get_available_quantity()` clamps to zero by default (`allow_negative=False`); a true negative can persist silently underneath. **Unknown:** none on the mechanism. **Special Team:** IDTM. **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CLOSED_WITH_EVIDENCE`.

### 11. Executed movement
**Prior:** `CLOSED_WITH_EVIDENCE`, `stock.move`/`stock.move.line`. **Delta:** record-state idempotency framing disagreement (see item 37). **Current:** `_action_done()` state-filter guard confirmed real by Special Team; Council's inherited framing rates the broader guard bucket more skeptically — `CONFLICTING` in weight, not in fact. **Unknown:** none on existence of the guard. **Special Team:** IDTM. **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CARRY_FORWARD`.

### 12. Receipt
**Prior:** `CLOSED_WITH_EVIDENCE`, direct/synchronous Purchase→Inventory. **Delta:** none. **Current:** reconfirmed by both IBPV bodies. **Unknown:** none. **Special Team:** IBPV. **Accounting Dependency:** `ACCOUNTING_INTERFACE_REQUIREMENT` (valuation handoff). **Gate Impact:** `CLOSED_WITH_EVIDENCE`.

### 13. Delivery
**Prior:** `CLOSED_WITH_EVIDENCE`, indirect via `stock.rule.run()`. **Delta:** Sale-vs-Purchase structural asymmetry named as an open design question (4 independent citations across Tracks 03/04/05). **Current:** mechanism confirmed; whether to preserve or unify the asymmetry is undecided. **Unknown:** target decision. **Special Team:** IBPV/IESA. **Accounting Dependency:** `ACCOUNTING_INTERFACE_REQUIREMENT` (COGS handoff). **Gate Impact:** `CARRY_FORWARD`.

### 14. Internal transfer
**Prior:** `CLOSED_WITH_EVIDENCE`. **Delta:** none. **Current:** reconfirmed; Special Team notes `picking_type.code=='internal'` is a string literal (registered migration-coupling risk, not new). **Unknown:** none material. **Special Team:** IBPV. **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CLOSED_WITH_EVIDENCE`.

### 15. Partial/backorder
**Prior:** DR-002 documented three domain idioms. **Delta:** elevated this round from "fact" to a named open design question by both IBPV and IESA. **Current:** no single cross-domain representation (header enum / uncapped running total / explicit MO-split) on one shared `stock.move`/backorder primitive; no Team B design-freeze item exists yet. **Unknown:** unify vs. preserve. **Special Team:** IBPV, IESA. **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CARRY_FORWARD`.

### 16. Return/reversal
**Prior:** `CLOSED_WITH_EVIDENCE`, single generic wizard. **Delta:** cost-basis-of-returned-stock question (`FIN-DELTA-05`). **Current:** Financial Council found this untraced in CORR-007B and flagged it open; Financial Special Team independently traced `_get_value_from_returns()` at primary source and reports it closed. **`CONFLICTING`**, not resolved in this document — routed to Boss/Track 01. **Special Team:** IBPV (mechanism), Financial (valuation). **Accounting Dependency:** `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION`. **Gate Impact:** `CONFLICTING`.

### 17. Cancellation
**Prior:** GROUP_A-imported symmetry claim, never independently re-traced within Inventory Core Backbone. **Delta:** the one genuine IBPV item-level disagreement this round (`MOV-31`). **Current:** Council reads the same shared fact as `PARTIALLY VERIFIED` (recommends native re-trace, citing GROUP_A's organizational split and known staleness); Special Team reads it as `CLOSED_WITH_EVIDENCE, reconfirmed, no delta`. **Unknown:** which reading governs. **Special Team:** IBPV. **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CONFLICTING`.

### 18. Scrap/damage
**Prior:** `CLOSED_WITH_EVIDENCE` for scrap; "damaged goods" as a distinct category never evidenced. **Delta:** both TBRAC and IBPV independently ran the identical zero-hit search this round. **Current:** only scrap (dedicated `stock.scrap` model) and a generic return wizard exist; no distinct damaged-goods workflow anywhere in the chain. **Unknown:** whether SMEsPlus needs one. **Special Team:** TBRAC, IBPV. **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `UNKNOWN — STILL MATERIAL`.

### 19. Physical count/adjustment
**Prior:** `N-A7-01` RESOLVED AS SOURCE BEHAVIOR; DESIGN POLICY REQUIRED (CORR-007B). **Delta:** re-verified a fourth independent time this round (IBPV Special Team's additional `stock_move.py` grep closes the last residual gap); two-axis structuring of the 4 design options offered. **Current:** soft conflict-detection only, no hard freeze anywhere; freeze-policy choice remains a Team B decision this session may not make. **Unknown:** which of the 4 (composable) options. **Special Team:** IBPV (primary owner). **Accounting Dependency:** `ACCOUNTING_INTERFACE_REQUIREMENT` (ties to G-2/G-3 lock-date). **Gate Impact:** `CARRY_FORWARD`.

### 20. Lot
**Prior:** `CLOSED_WITH_EVIDENCE`, tracking gate confirmed. **Delta:** identity-constraint coverage detail. **Current:** `stock.lot` uniqueness enforced only by `@api.constrains`, not a DB-level constraint. **Unknown:** none on the fact. **Special Team:** IDTM. **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CLOSED_WITH_EVIDENCE`.

### 21. Serial
**Prior:** `CLOSED_WITH_EVIDENCE`. **Delta:** `stock.quant.sn_duplicated` is a reactive detector, not a preventive gate. **Current:** confirmed, no DB uniqueness. **Unknown:** none on the fact. **Special Team:** IDTM. **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CLOSED_WITH_EVIDENCE`.

### 22. Package/handling unit
**Prior:** `CLOSED_WITH_EVIDENCE`, live vs. immutable-history distinction documented. **Delta:** none this round (migration disposition question flagged since DR-002, not revisited). **Current:** `stock.package.name` carries only a trigram index, no uniqueness. **Unknown:** carry live state, history snapshot, or both at migration. **Special Team:** IDTM (not re-taken up). **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CARRY_FORWARD`.

### 23. Expiry
**Prior:** `EVIDENCE_MISSING — NOT YET RESEARCHED` since 2026-08-31 (`N-A5-02`). **Delta:** narrowed by the ROUTING deep-proof this round. **Current:** `product_expiry` schema confirmed present; expiration is nested under the Stockable leg (requires `is_storable=True`), not a fourth bucket. Full expiry-workflow logic (removal/alert automation) still unread. **Unknown:** full workflow depth. **Special Team:** TBRAC, IBPV (both independently flag as open), ROUTING. **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CARRY_FORWARD`.

### 24. Routes/replenishment
**Prior:** `CLOSED_WITH_EVIDENCE`, `stock.rule.run()` single dispatch point. **Delta:** idempotency caveat added. **Current:** dispatch mechanism well-mapped; duplicate/retry safeguards are quantity-remaining merges only — `PARTIALLY SUPPORTED, not proven` (IESA Special Team's more cautious framing adopted as operative). **Unknown:** concurrent-retry interleaving safety. **Special Team:** IESA, AI Control. **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CARRY_FORWARD`.

### 25. MTO/MTS
**Prior:** referenced within route dispatch (`_run_buy`/`_run_manufacture`). **Delta:** none dedicated this round. **Current:** covered as part of item 24's dispatch mechanism; not separately deep-dived. **Unknown:** whether separate MTO/MTS evidence is still required. **Special Team:** IESA (incidental). **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CARRY_FORWARD`.

### 26. Procurement handoff
**Prior:** no `procurement.group` model; `stock.reference` substitute (DR-002, reconfirmed independently this round by IESA). **Delta:** tenant-isolation implication drawn: grouping is scoped only by whatever `company_id` the linking document already carries — inherited, not independently enforced (`SAAS-08`). **Unknown:** none on the fact. **Special Team:** IESA. **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CLOSED_WITH_EVIDENCE` (fact) / `CARRY_FORWARD` (tenant implication).

### 27. Sales handoff
**Prior:** `CLOSED_WITH_EVIDENCE`, no duplicate ownership. **Delta:** empirically re-tested this round (zero-write-hit grep of `sale_stock/models/`). **Current:** confirmed for the reference pattern; explicitly not yet testable against an actual SMEsPlus schema (Team B unauthorized). **Unknown:** target-schema equivalent. **Special Team:** IBPV (empirical re-test). **Accounting Dependency:** `ACCOUNTING_INTERFACE_REQUIREMENT`. **Gate Impact:** `CLOSED_WITH_EVIDENCE` (reference pattern only).

### 28. Purchase handoff
**Prior:** `CLOSED_WITH_EVIDENCE`, direct/synchronous. **Delta:** over-receipt guard gap elevated as an under-triaged item (no `N-A7-01`-parity design brief exists despite comparable severity). **Current:** no ceiling anywhere in the reference system, confirmed via two independent evidence paths. **Unknown:** design-policy brief. **Special Team:** IBPV, TBRAC. **Accounting Dependency:** `ACCOUNTING_INTERFACE_REQUIREMENT`. **Gate Impact:** `CARRY_FORWARD` (with a governance-triage flag).

### 29. Manufacturing handoff
**Prior:** `CLOSED_WITH_EVIDENCE`, ordinary `stock.move` rows tagged to MO. **Delta:** Financial track's new blind spot — manufacturing WIP valuation has no automated equivalent to the periodic stock-closing cron proven for ordinary Inventory. **Current:** consumption/WIP/FG mechanism confirmed; valuation-close automation for WIP specifically is untested. **Unknown:** whether SMEsPlus needs one and how it sequences against the existing periodic-closing mechanism. **Special Team:** IBPV (mechanism), Financial (valuation gap — new this round). **Accounting Dependency:** `ACCOUNTING_INTERFACE_REQUIREMENT`. **Gate Impact:** `CARRY_FORWARD`.

### 30. Accounting valuation interface
**Prior:** `N-A12-01` = HIGH FUNCTIONAL DESIGN GAP — REOPENED (CORR-007B, the single live pure-Inventory High item entering this reopen). **Delta:** deeply re-confirmed by Financial Council + Special Team this round; both independently reconfirm the Periodic/Perpetual posting gate, Product Category's true ownership of valuation policy, and the absent year-end retained-earnings entry; new blind spots (manufacturing valuation, landed cost, AP-bridge/late-bill mechanism) surfaced; one `CONFLICTING` item (return-valuation cost basis, item 16). **Current:** standing disposition unchanged: `HIGH FUNCTIONAL DESIGN GAP — REOPENED`, `Account + Inventory Backbone Reference Baseline = HOLD`. Also: the Inventory→Accounting posting-architecture fork (direct `account.move` write vs. neutral event emission) remains unresolved since DR-002 (IESA). **Unknown:** G-1 (lock-date sequencing), G-2 (asymmetric correction governance), G-5 (migration cutover opening-balance cross-proof, needs Accounting), G-6 (retained-earnings design). **Special Team:** Financial (primary), IESA (architecture fork), IBPV/IDTM (mechanism edges). **Accounting Dependency:** `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION`. **Gate Impact:** `CARRY_FORWARD` (standing HOLD, independently reconfirmed, not newly closed or newly worsened).

### 31. Period/cut-off
**Prior:** G-3 (backdate at picking- not move-level). **Delta:** mechanism fully traced this round (`N-A7-04` resolved — found in the Accounting lock-date bridge, not the stock module). **Current:** `_check_backdate_allowed()`/`_is_date_in_lock_period()` gate picking-level dates only; Inventory Adjustments post directly as `stock.move` and may not inherit the same protection. G-2's global, unaudited `skip_lock_date_check` kill-switch (no user/reason/expiry tracking) contrasts with Accounting's governed `account.lock_exception`. **Unknown:** whether Inventory should own a native temporal-integrity guard independent of the Accounting bridge. **Special Team:** IBPV (mechanism resolution), Security (G-2 audit-trail gap), TBRAC (Thai statutory-audit fit). **Accounting Dependency:** `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION`. **Gate Impact:** `CARRY_FORWARD`.

### 32. Multi-warehouse
**Prior:** referenced in warehouse/location structure. **Delta:** none dedicated. **Current:** covered structurally under items 4–5; no multi-warehouse-specific stress case tested. **Unknown:** cross-warehouse concurrency at scale. **Special Team:** IESA (incidental). **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CARRY_FORWARD`.

### 33. Multi-company
**Prior:** `GRPA-H8` — two uncoordinated Thai branch concepts, closed as an Inventory architecture scope question. **Delta:** re-verified at primary source this round (IESA, TBRAC) — no delta found on the underlying dual-mechanism fact; wording-precision risk flagged (Council: "approved baseline" should not be read as "proven," given canonical `COA-G07 = NOT STARTED`). **Current:** cross-company transfer flow never traced end-to-end anywhere in the chain — only a `transit` location-usage value is named. **Unknown:** whether SMEsPlus needs true inter-company transfer, and its workflow. **Special Team:** IESA, TBRAC. **Accounting Dependency:** `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION`. **Gate Impact:** `CARRY_FORWARD`.

### 34. SaaS/tenant isolation
**Prior:** treated only implicitly. **Delta:** the single most consequential IESA finding — a Boss-approved Cross-Gate SaaS Invariants framework (`SI-01`..`SI-10`, commit `e16b29f3`) exists and is rigorous for Accounting, unexecuted even there (`COA-G04S`=AUTHORIZED/NOT EXECUTED, `COA-G07`=NOT STARTED), and has **no Inventory-side equivalent at all**. **Current:** zero Team B design-execution artifacts exist for Inventory; no SMEsPlus target-side tenancy architecture exists anywhere to evaluate. **Unknown:** whether `SI-01..10` extends to Inventory or Inventory needs its own Boss-approved invariant set — no document answers this. **Special Team:** IESA (primary), Security, AI Control. **Accounting Dependency:** `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION`. **Gate Impact:** `UNKNOWN — STILL MATERIAL` (structural planning gap, not merely an unexecuted step).

### 35. Migration/provenance
**Prior:** DR-002 A12: no external-ID/provenance field exists on any source Inventory record. **Delta:** AI Control track's full-repository verification: **zero migration/ETL code exists anywhere**; `MIGRATION_PLAN_v0.1.md` is an unauthored placeholder. **Current:** foundational absence confirmed and now dated to "not yet begun," not merely "not designed." **Unknown:** what dedup/external-ID key SMEsPlus's own tooling will use. **Special Team:** IDTM, AI Control (primary). **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT` (design), `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` (opening-balance cross-proof, item 36). **Gate Impact:** `CARRY_FORWARD`.

### 36. Historical stock continuity
**Prior:** `N-A12-01` sub-item F (opening-balance carry-forward), NOT PROVEN. **Delta:** AI Control's new finding — `G-5` (migration-cutover first opening balance) has **no reference mechanism in source at all**, named "the single highest AI-fabrication-risk point in the whole Inventory scope." **Current:** standing REOPENED disposition reconfirmed; no design exists to close it. **Unknown:** everything about how the first opening balance will be established and human-certified. **Special Team:** Financial, IDTM, AI Control. **Accounting Dependency:** `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION`. **Gate Impact:** `CARRY_FORWARD`.

### 37. Idempotency/retry/concurrency
**Prior:** DR-002: "no single unified idempotency-key mechanism exists," PARTIALLY SUPPORTED not VERIFIED. **Delta:** the most-examined single item in this reopen — a genuine row-lock (`try_lock_for_update()`, UPDATE path only) and a genuine record-state guard (`_action_done()`) both re-confirmed, but framed with **two distinct `CONFLICTING` severity judgments**: (a) IDTM — Council treats the overall gap as this mandate's weakest point, un-advanced across 5 rounds, deserving first-class Team B status; Special Team credits the fresh guards and routes replay-safety to Team A/Migration, not a Gate blocker; (b) Security — `N-CONC-01` itself: Council rates it an unfollowed lead requiring one bounded verification pass; Special Team rates it already better-supported than the register states. **Current:** zero hits for "idempotency"/"replay" anywhere in CORR-006/007A/007B's own text (AI Control's literal search) despite being this reopen's own named delta trigger (`INV-DELTA-07`). **Unknown:** severity/ownership, resolved by Boss, not this reopen. **Special Team:** IDTM (primary), Security, AI Control. **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT`. **Gate Impact:** `CONFLICTING`.

### 38. Security/SoD/audit trail
**Prior:** `N-A13-02` conditions unextracted. **Delta:** extracted this round (item 6); operation-level role/CRUD segregation (receive vs. adjust vs. scrap) found genuinely unitemized by any deliverable — new finding, both bodies. **Current:** append-only done-move history confirmed as a real positive control (no un-confirm path exists); PDPA research totally absent (zero hits, both bodies independently confirmed); G-2's audit-trail gap (no record of who/why/how-long) named. **Track verdict itself conflicted** (Security: HOLD vs. CONTINUE_WITH_NOTES). **Unknown:** warehouse-level authorization, operation-level CRUD breakdown, PDPA scope. **Special Team:** Security (primary). **Accounting Dependency:** `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` (A16 scenario 9, Accounting's own side unverified). **Gate Impact:** `CARRY_FORWARD`, with the track-level verdict conflict itself carried to Boss.

### 39. Thailand user/business reality
**Prior:** structural real-user-validation gap, unremedied since the 2026-08-30 founding TBRAC control document. **Delta:** independently reconfirmed as total and structural this round; new Thai regulatory/accounting-standard evidence gathered for the ROUTING deep-proof only (WHT law, TAS 2 consumables guidance, FlowAccount comparator) — genuinely new ground, but explicitly not a substitute for real-user validation. **Current:** every operational-mechanics claim in the chain still traces to one reference vendor's source plus one 48-row customer dataset; TBRAC's own named-membership assignment remains unfilled. **Unknown:** essentially the entire operational-fitness question for count-freeze, backdate governance, receiving controls, and routing, absent real Thai user input. **Special Team:** TBRAC (primary), ROUTING (regulatory evidence only). **Accounting Dependency:** `PENDING_ACCOUNT_SESSION` (TH-INV-03 → COA-G06 dependency). **Gate Impact:** `CARRY_FORWARD` — the single broadest standing gap in the whole reopen.

### 40. AI control boundary
**Prior:** genuinely new mandate — no AI-authority domain exists anywhere in DR-002's original 22-domain checklist. **Delta:** full new track executed this round (Track 09) against a system with zero migration code and an unbuilt migration plan; 17 paired AI-use/deterministic-control items evaluated, only a handful closed. **Current:** idempotency and the `sudo()`-bypass residual are the two most strongly corroborated preconditions; Product Category AI-assignment risk and the `G-5` opening-balance fabrication risk are the two highest-stakes newly-drawn findings. A self-referential concern was independently raised by both bodies: neither can verify whether this reopen's own 9-Council/9-Special-Team structure is genuinely parallel or another instance of the single-session-sequential pattern CORR-007B's file 14 disclosed at smaller scale. **Track verdict itself conflicted** (AI Control: HOLD vs. CONTINUE_WITH_NOTES). **Unknown:** essentially all target-side AI-governance design, since no target system yet exists. **Special Team:** AI Control (primary). **Accounting Dependency:** `INVENTORY_OWNED_STOCK_FACT` (design) / `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` (reconciliation-explanation surface). **Gate Impact:** `CARRY_FORWARD`, with the track-level verdict conflict and the self-referential parallelism question both carried to Boss.

---

## Summary Roll-Up

| Gate Impact | Count | Items |
|---|---:|---|
| `CLOSED_WITH_EVIDENCE` | 10 | 5, 7, 8, 10, 12, 14, 20, 21, 26 (fact only), 27 (reference pattern only) |
| `CARRY_FORWARD` | 24 | 1, 2, 3, 4, 6, 9, 11, 13, 15, 19, 22, 23, 24, 25, 28, 29, 30, 31, 32, 33, 35, 36, 38, 39 |
| `UNKNOWN — STILL MATERIAL` | 2 | 18, 34 |
| `CONFLICTING` | 4 | 16, 17, 37, and the two track-verdict-level conflicts folded into 38 and 40 |

No item is classified `SUPERSEDED` or `FAIL/FROZEN` at the coverage-register level. No item required fabrication to complete this register — every row above cites a specific deliverable, file, or commit. Full detail, citations, and the two challenge bodies' original language for every item are preserved in deliverables `03`–`12`; this register is a navigation index into them, not a replacement for them.
