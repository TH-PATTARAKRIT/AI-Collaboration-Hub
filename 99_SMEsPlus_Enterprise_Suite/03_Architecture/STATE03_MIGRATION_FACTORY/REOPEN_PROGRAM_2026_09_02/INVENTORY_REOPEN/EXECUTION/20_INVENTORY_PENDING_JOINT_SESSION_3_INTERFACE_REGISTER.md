# Inventory Full Reopen — Pending Joint Session 3 (Account × Inventory) Interface Register

Session: `SMEPLUS-26-09-02-INV-REOPEN-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-07 OUTPUT — SESSION 3 HANDOFF REGISTER — NOT A GATE DECISION, NOT A JOINT SESSION AUTHORIZATION`

Per execution prompt §11.6. This register hands evidence to the separately-authorized Accounting × Inventory Joint Reopen (Jira `ERPPLUS-140`); it does not authorize that session to begin or to reach any particular conclusion.

---

## 1. Inventory-Owned Conclusions Ready for Joint Use

- Complete physical-stock lifecycle semantics (demand → reservation → receipt/delivery → transfer → backorder → return → scrap → count/adjustment), evidenced to method-body depth (deliverables `05`, `06`).
- The Inventory-side valuation-emission facts: what Inventory knows and when (receipt cost, delivery quantity/cost, adjustment deltas, manufacturing consumption) — deliverable `08` §3–§6.
- Product Category confirmed as the reference system's true valuation-policy owner (not product, not company) — deliverable `08`, `11`.
- Stockable/Consumable/Service routing mechanism and its accounting-relevant edges (WHT independence from routing, valuation-eligibility gate) — deliverable `12` §8.
- `N-A13-02` company/tenant ORM-layer isolation, fully re-extracted and independently reconfirmed — deliverable `09`.

## 2. Accounting-Dependent Open Questions (Inventory cannot answer these)

- `TH-INV-03` — Thai costing-method/valuation-norm requirement for Inventory, explicitly deferred to `COA-G06` by DR-002 on 2026-08-31; `COA-G06` remains not closed.
- `GRPA-M18-D` — Thai WHT/PND3/PND53 monthly filing; hand-off made by CORR-007A, receipt not yet confirmed by the Account Reopen track.
- WHT-applicability-vs-product-routing linkage (should WHT eligibility be derived from Stockable/Consumable/Service classification, or remain an independent attribute as the reference system keeps it) — deliverable `12` §8, §10.4.

## 3. Joint Account × Inventory Questions (neither domain can close alone)

| Question | Inventory-side evidence | Accounting-side evidence needed |
|---|---|---|
| `N-A12-01` full closure (monthly/year-end close, cut-off, GL reconciliation, retained earnings) | Periodic/Perpetual posting gate located; closing-cron mechanism located; Product Category confirmed as policy owner; no year-end retained-earnings entry found in reference system (`G-6`) | Accounting's own close-sequencing design; `COA-G04`–`COA-G08` closure |
| `G-1` — lock-date/closing sequencing | Inventory's own picking-level backdate gate documented | Accounting's own period-close sequencing design |
| `G-2` — post-close correction governance asymmetry | Inventory's global, unaudited `skip_lock_date_check` toggle fully documented | Accounting's governed `account.lock_exception` model as the possible template |
| `G-5` — migration-cutover opening-balance cross-proof | Confirmed **no reference mechanism exists in source at all** — highest AI-fabrication-risk item in the whole Inventory scope (Track 09) | Accounting's own opening-balance/carry-forward policy design |
| Inventory→Accounting posting-architecture fork | Direct `account.move` construction vs. neutral valuation-event emission, both traced to source (`_create_account_move()`) | Accounting-owned posting-service design decision |
| Return-valuation cost basis | `CONFLICTING` between Inventory's own Council and Special Team passes (item `C-03`, deliverable `13`) — needs resolution before joint reliance | N/A until Inventory-side conflict resolved |
| Company/tenant cross-domain enforcement consistency | Inventory's `ir.rule` side evidenced-ready | Accounting's own side of the same shared-model enforcement, explicitly flagged "still pending" in its own source (A16 scenario 9) |
| Product Category dual ownership (valuation policy + routing/putaway policy) | Both roles traced to the same source record | Whether Category redesign should be one joint design pass to avoid `GRPA-H8`'s history of uncoordinated parallel ownership |
| Multi-company / cross-company transfer | `transit` location-usage value named; no workflow ever traced end-to-end | Whether SMEsPlus's Accounting model requires true inter-company transfer at all |

## 4. Required Evidence for Session 3

- Boss Gate decision (or explicit deferral) on `N-A12-01`'s Inventory-owned facets, since Session 3 will need a stable Inventory-side starting position, not an open `HOLD`.
- Remediated CORR-007B files 08/09 (item `C-05`, deliverable `13`) — Session 3 should not inherit the code-reproduction-affected version.
- Accounting Reopen's own closure status on `COA-G04`–`COA-G08`, `TH-INV-03`, and `GRPA-M18-D` receipt.
- Resolution or explicit non-resolution of the return-valuation `CONFLICTING` item.

## 5. Blocked Baseline Assumptions

- **`Account + Inventory Backbone Reference Baseline = HOLD`** remains the controlling status; Session 3 does not start from a "backbone confirmed" assumption.
- No assumption should be made that Inventory's `N-A12-01` disposition is final — it is `REOPENED`, independently reconfirmed by this pass, not closed.
- No assumption should be made that either domain's tenant-isolation enforcement has a database-layer backstop — both sides currently rely on ORM-layer trust only.

## 6. Owner and Target Gate Per Pending Interface

| Interface | Owner | Target Gate |
|---|---|---|
| `N-A12-01` full closure | Joint (Team B, both domains, once authorized) | Account × Inventory Cross-Proof |
| `TH-INV-03` | Accounting Reopen | `COA-G06` |
| `GRPA-M18-D` | Accounting/Tax | Account Reopen receipt confirmation |
| `G-5` opening balance | Joint | Account × Inventory Cross-Proof, pre-migration |
| Posting-architecture fork | Accounting-owned design, Inventory-informed | Team B Accounting-posting-service design |
| Company/tenant cross-domain consistency | Joint | Account × Inventory Cross-Proof |
| Product Category redesign | Joint (explicitly recommended as one pass) | Team B Category design |

## 7. Gate-Impact Classification Per Item

Using: `BLOCKS_INVENTORY_ONLY_UNDERSTANDING` / `BLOCKS_ACCOUNT_ONLY_UNDERSTANDING` / `BLOCKS_JOINT_BACKBONE_PUBLICATION`.

- `N-A12-01` full closure, `G-1`, `G-2`, `G-5`, `G-6`, posting-architecture fork, company/tenant cross-domain consistency, Product Category redesign → **all `BLOCKS_JOINT_BACKBONE_PUBLICATION`**. None of these blocks Inventory's own standalone understanding (Inventory's side is evidenced) or Account's own standalone understanding (Account's own gates proceed on their own timeline) — they specifically block the point where the two backbones would be published as a reconciled whole.
- `TH-INV-03`, `GRPA-M18-D` → **`BLOCKS_ACCOUNT_ONLY_UNDERSTANDING`** — these are Accounting's own open items; Inventory has supplied what evidence it can and is not blocked by them.
- Return-valuation cost basis (`C-03`) → **`BLOCKS_INVENTORY_ONLY_UNDERSTANDING`** until Inventory's own internal conflict resolves — not yet ready to hand to Session 3 as settled.

No item in this register is authorized for Session 3 action by virtue of appearing here. This is an evidence handoff, prepared under Inventory's own authority, for Session 3's separately-governed use.
