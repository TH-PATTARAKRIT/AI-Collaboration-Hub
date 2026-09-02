# 24 — Unknown / Conflict / Gap / Owner / Gate Impact Register

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-09 OUTPUT — CONSOLIDATED REGISTER — NOT A GATE DECISION`
Rule: no item here is closed by this session. Owners are challenge tracks / special teams / Boss / Joint Session; naming an owner is not an authorization. Gate impact vocabulary: `BLOCKS_JOINT_BACKBONE_PUBLICATION` / `BOSS_DECISION` / `STATUTORY_HOLD` / `TEAM_B_PRECONDITION` / `MIGRATION_PRECONDITION` / `BOUNDED_VERIFICATION` / `NON_BLOCKING`.

---

## 1. New Gaps Raised by This Session (`GAP-MD-*`)

| Gap ID | Menu / area | Gap | Owner | Verifier | Gate impact | Status |
|---|---|---|---|---|---|---|
| GAP-MD-01 | OP-01 | Replenishment user process never studied at source; Thai purchasing practice absent | Track 02, 05 / S5 | UNVERIFIED | TEAM_B_PRECONDITION | OPEN |
| GAP-MD-02 | OP-02 | Count freeze/conflict policy unselected; Thai count approval, reason taxonomy, year-end witness flow unvalidated | Track 03, 02 / S1; Team B | UNVERIFIED | TEAM_B_PRECONDITION | OPEN |
| GAP-MD-03 | OP-02/03/04 | Native period guard and audited exception model (`G-2`/`G-3`) | Track 06, 07 / S6; Joint | UNVERIFIED | BLOCKS_JOINT_BACKBONE_PUBLICATION | OPEN |
| GAP-MD-04 | OP-04 | Thai statutory destruction evidence rule for scrap deductibility | Accounting-Tax track (ERPPLUS-138) | UNVERIFIED | STATUTORY_HOLD | HOLD / EVIDENCE REQUIRED |
| GAP-MD-05 | OP-05 | Landed-cost allocation mechanism completeness (periodic/standard path never read) | Track 06 / S6 | UNVERIFIED | TEAM_B_PRECONDITION (conditional) | HOLD / EVIDENCE REQUIRED |
| GAP-MD-06 | OP-03 | Over-receipt / over-delivery tolerance policy brief | Track 03 / S1 | UNVERIFIED | TEAM_B_PRECONDITION | OPEN |
| GAP-MD-07 | OP-03 | Unified partial/backorder/return Thai user flow; damaged-goods hold | Track 03, 02 / S1 | UNVERIFIED | TEAM_B_PRECONDITION | OPEN |
| GAP-MD-08 | PR-02, CF-10 | Variants/attributes: no evidence in any round | Track 04 / S2 | UNVERIFIED | TEAM_B_PRECONDITION (conditional) | HOLD / EVIDENCE REQUIRED |
| GAP-MD-09 | PR-03 | Expiry/removal workflow depth; consignment stock (`N-A5-02/03`) | Track 02, 04 / S4 | UNVERIFIED | TEAM_B_PRECONDITION (tracked industries) | HOLD / EVIDENCE REQUIRED |
| GAP-MD-10 | PR-01 | Product kind two-axis tie-break rule; kit/combo scope | Track 03 / S2; Team B, Migration | UNVERIFIED | TEAM_B_PRECONDITION | OPEN |
| GAP-MD-11 | PR-03 | Serial/lot uniqueness must be DB-enforced in target | Track 04 / S4 | UNVERIFIED | NON_BLOCKING (requirement) | OPEN |
| GAP-MD-12 | RP-03 | Thai statutory stock report format (รายงานสินค้าและวัตถุดิบ) | Accounting-Tax track | UNVERIFIED | STATUTORY_HOLD | HOLD / EVIDENCE REQUIRED |
| GAP-MD-13 | RP-05, CF-09 | Valuation policy owner; Category redesign; `N-A12-01` closure; reconciliation export | Joint Session (ERPPLUS-140); Boss | UNVERIFIED | BLOCKS_JOINT_BACKBONE_PUBLICATION | OPEN |
| GAP-MD-14 | CF-01, CF-02 | Feature-switch inventory, switch-off guards, versioning vs regeneration (`SAAS-04`) | Track 05 / S5 | UNVERIFIED | TEAM_B_PRECONDITION | OPEN |
| GAP-MD-15 | CF-02 | Warehouse vs Thai tax branch labelling rule | Track 02 / S8 | UNVERIFIED | TEAM_B_PRECONDITION | OPEN |
| GAP-MD-16 | CF-07 | Storage categories: no evidence | Track 05 / S4 | UNVERIFIED | NON_BLOCKING | HOLD / EVIDENCE REQUIRED |
| GAP-MD-17 | CF-08 | Putaway rules: no evidence; category dual ownership | Track 05 / S4; Joint | UNVERIFIED | TEAM_B_PRECONDITION | HOLD / EVIDENCE REQUIRED |
| GAP-MD-18 | CF-11 | Packaging behaviour: no menu-level evidence | Track 04 / S2 | UNVERIFIED | NON_BLOCKING | HOLD / EVIDENCE REQUIRED |
| GAP-MD-19 | CF-13 | Barcode nomenclature: no evidence | Track 04 / S2 | UNVERIFIED | NON_BLOCKING | HOLD / EVIDENCE REQUIRED |
| GAP-MD-20 | OP-03, CF-02 | Cross-warehouse/cross-company transfer via transit never traced | Track 05 / S5; Joint | UNVERIFIED | BLOCKS multi-company design | OPEN |
| GAP-MD-21 | OP-06, CF-04 | Route resolution / scheduler idempotency under concurrent retry | Track 04, 09 / S3, S5 | UNVERIFIED | BOSS_DECISION (`C-02`) | OPEN |
| GAP-MD-22 | CF-06 | Operation-type SoD matrix; Thai document numbering standards | Track 07, 02 / S1, S8 | UNVERIFIED | TEAM_B_PRECONDITION | OPEN |
| GAP-MD-23 | CF-12 | Forecast definition and Thai lead-time practice | Track 02 / S5 | UNVERIFIED | TEAM_B_PRECONDITION | OPEN |
| GAP-MD-24 | OP-05 | Import duty / VAT cost treatment for Thai importers | Accounting-Tax track | UNVERIFIED | STATUTORY_HOLD | HOLD / EVIDENCE REQUIRED |
| GAP-MD-25 | RP-06 | Warehouse analysis KPI set and benchmark content | Track 03 / S7 | UNVERIFIED | NON_BLOCKING | HOLD / EVIDENCE REQUIRED |
| GAP-MD-26 | OBJ-19 | Package migration disposition (live / history / both) | Track 04 / S9 | UNVERIFIED | TEAM_B_PRECONDITION (conditional) | OPEN |
| GAP-MD-27 | OBJ-36 | Provenance / external-ID map must be originated | Track 04, 09 / S9 | UNVERIFIED | MIGRATION_PRECONDITION | OPEN |
| GAP-MD-28 | Migration | Cardinality transform table and orphan quarantine rules | Track 04, 09 / S9 | UNVERIFIED | MIGRATION_PRECONDITION | OPEN |
| GAP-MD-29 | All documents | PDPA scope for Inventory documents | Track 07; Account/Legal | UNVERIFIED | Pre-production | HOLD / EVIDENCE REQUIRED |
| GAP-MD-30 | 17 | Thai label validation panel (storekeepers; accountants/auditors) | Track 02 / S8; Boss (TBRAC membership) | UNVERIFIED | TEAM_B_PRECONDITION | OPEN |
| GAP-MD-31 | 05 | Boss screenshot image files not archived in repository | PMO | UNVERIFIED | NON_BLOCKING (evidence hygiene) | HOLD / EVIDENCE REQUIRED |

## 2. Carried Unknowns (from reopen `13`, unchanged)

| ID | Item | Owner | Gate impact | Status |
|---|---|---|---|---|
| U-01 | Warehouse-level authorization | Track 07; Boss scope ruling | TEAM_B_PRECONDITION | UNKNOWN |
| U-02 | Damaged-goods exception category | Track 02, 03 / S1 | TEAM_B_PRECONDITION | UNKNOWN |
| U-03 | Inventory-side SaaS invariant set (`SI-01..10` extension) | Track 05; Boss | BOSS_DECISION | UNKNOWN |
| U-04 / G-5 | Migration-cutover first opening balance (no reference mechanism) | Joint; Track 09 | BLOCKS_JOINT_BACKBONE_PUBLICATION; MIGRATION_PRECONDITION | UNKNOWN |
| U-05 | Genuine parallelism of 9+9 dispatch (this session: sequential, disclosed) | Track 01 / PMO | NON_BLOCKING (governance) | UNKNOWN |
| U-06 | Material Unknown Exhaustion formally superseded or re-run? | Track 01; Boss | NON_BLOCKING (governance) | UNKNOWN |
| U-07 | Which 9 Veto Council definition governs (this session follows ratified Charter) | Track 01; Boss | BOSS_DECISION | UNKNOWN |

## 3. Carried Conflicts (preserved, not arbitrated)

| ID | Conflict | Owner | Gate impact | Status |
|---|---|---|---|---|
| C-01 | Purchase-side cancellation cascade | Track 01 / Team A | BOUNDED_VERIFICATION | CONFLICTING |
| C-02 | Idempotency/replay: Gate-blocking vs design input | Boss | BOSS_DECISION | CONFLICTING |
| C-03 | Return cost basis | Track 01 / Boss | BOUNDED_VERIFICATION | CONFLICTING |
| C-04 | Reservation locking verification | Track 07 / Team A | BOUNDED_VERIFICATION | CONFLICTING |
| C-05 | CORR-007B 08/09 clean-room exposure — surface remediated; independent re-audit pending | Boss; Track 08 | Precondition for any Team B reliance | **BOSS-VISIBLE, OPEN** |
| Track 07/08/09 verdict splits | Threshold judgement | Boss | BOSS_DECISION | CONFLICTING (reconciled HOLD) |

## 4. Required Evidence Before Any Gate Movement (consolidated)

1. Real Thai user validation (storekeepers, accountants, auditors) of menu names, Transfers split, count/scrap flows, SoD roles — with named TBRAC membership.
2. Boss decisions: `C-02`, `U-03`, `U-07`, warehouse/operation-level authorization scope, count-freeze and over-fulfilment policy selection path.
3. Independent Clean-Room Re-Audit of CORR-007B `08`/`09` (`C-05`) and of this package.
4. Accounting-Tax authoritative evidence: scrap destruction, stock report format, import duty/VAT, costing norm (`TH-INV-03`), WHT correlation; confirmed receiving owner for `GRPA-M18-D`.
5. Joint Session outputs: valuation policy owner, posting architecture, COGS timing, return cost basis, period guard/exception model, `G-5` cross-proof design, `G-6` retained-earnings decision.
6. Dedicated research (not re-read): expiry/consignment; variants/packaging/barcode; landed-cost mechanism; cross-company transfer; reporting formats.
7. Bounded verifications: `C-01`, `C-03`, `C-04`, `N-A13-01`, `N-DB-01`.
8. Governance hygiene: screenshot archive; Global Challenge Ledger `INV-FP` rows; canonical evidence index correction; Boss written Gate decision on the reopen package.

## 5. Counts

| Class | Count |
|---|---:|
| New gaps (GAP-MD) | 31 |
| Carried unknowns | 7 |
| Carried conflicts | 6 (5 item-level + track-level splits) |
| BLOCKS_JOINT_BACKBONE_PUBLICATION | 3 (GAP-MD-03, 13; U-04/G-5) |
| STATUTORY_HOLD | 3 (GAP-MD-04, 12, 24) |
| BOSS_DECISION | 5 (GAP-MD-21/C-02, U-03, U-07, track splits, authorization scope) |
| HOLD / EVIDENCE REQUIRED rows | 13 |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
