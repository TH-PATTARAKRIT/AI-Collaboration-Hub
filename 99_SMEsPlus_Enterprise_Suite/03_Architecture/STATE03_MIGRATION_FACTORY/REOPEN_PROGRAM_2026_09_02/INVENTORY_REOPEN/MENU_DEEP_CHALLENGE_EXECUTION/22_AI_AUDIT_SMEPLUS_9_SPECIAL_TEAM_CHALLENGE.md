# 22 — AI Audit SMEsPlus: 9 Special Team Challenge

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-09 OUTPUT — 9 SPECIAL TEAM DEEP-DIVE CHALLENGE — NOT A GATE DECISION`
Independence disclosure: same as 21 — nine mandates applied in sequence by one session; not nine independent parties. Special Teams investigate and return findings; they do not decide.

Each team answers its required question, then lists objections, evidence, gaps, and recommended next action.

---

## S1 Warehouse Operations — Transfers, adjustments, scrap, physical flow
**Question:** Can a Thai warehouse user execute the process without hidden accounting or IT knowledge?
**Finding:** The candidate flows (11, 13, 14) are expressed in Thai document terms and hide valuation, routes and rules. Points where accounting knowledge still leaks to the warehouse user: choosing a reason code that determines tax deductibility (scrap), and period-guard errors when validating late. Points where IT knowledge leaks: multi-step route behaviour ("why did a second document appear?") — mitigated by explanation records.
**Objections:** no Thai warehouse staff has seen any flow; SoD matrix is an executor proposal.
**Evidence:** reopen `04`, `05`, `09`; maps 11, 13, 14.
**Gaps:** `GAP-MD-02`, `GAP-MD-06`, `GAP-MD-07`, `GAP-MD-22`, `U-02`.
**Next action:** structured walk-through of the three documents + count + scrap with at least two Thai SME warehouses (TBRAC panel) before Team B.

## S2 Product Master / UoM — Products, variants, attributes, UoM, packaging
**Question:** Is product identity stable enough for stock truth and migration?
**Finding:** Identity requirements are now explicit (09 §6, 03 §3): immutable code after first movement, attribute-value codes, versioned UoM factors, packaging over base unit. The benchmark data shows identity is *not* stable by default (989 kind-invariant violations; app-layer-only constraints). Variants, packagings and barcodes have no evidence.
**Objections:** three Thai kind labels sit over a two-axis fact with an undecided tie-break; kit/combo unresolved.
**Evidence:** reopen `12`, `06`; map 09.
**Gaps:** `GAP-MD-08`, `GAP-MD-10`, `GAP-MD-18`, `GAP-MD-19`.
**Next action:** decide tie-break rule and kit scope as recorded Team B/Migration decisions; profile variant/packaging data in Team A.

## S3 Stock Movement / Reservation — stock moves, history, availability
**Question:** Are movement facts, reservations and availability clearly separated?
**Finding:** Yes at reference and candidate level: three quantities (on hand / reserved / available) plus planned; done facts immutable; reports separate fact ledger (RP-04) from stock card (RP-03) from availability (RP-01). Negative-clamping in the benchmark is explicitly rejected as a candidate.
**Objections:** idempotency of movement facts remains unresolved (`C-02`); reservation locking (`C-04`) unverified.
**Evidence:** reopen `05`, `06`, `09`; maps 11, 16.
**Gaps:** `C-02`, `C-04`, INV-06.
**Next action:** Boss ruling on `C-02`; bounded verification of `C-04` (already in reopen Tier 1).

## S4 Traceability — lot, serial, package, storage category, putaway
**Question:** Can the system trace recall, warranty, expiry and location history?
**Finding:** Recall query, expiry watch list and warranty lookup are defined as first-class outputs (09 §3, 17 §3); lot history = movement history filtered by lot. Package history and storage/putaway are conditional and unevidenced. Serial uniqueness must be DB-enforced (benchmark is reactive).
**Objections:** expiry workflow depth unread since 2026-08-31; consignment stock never researched; package migration disposition undecided.
**Evidence:** reopen `02` items 20–23, `04`, `06`; map 09.
**Gaps:** `GAP-MD-09`, `GAP-MD-11`, `GAP-MD-16`, `GAP-MD-17`, `GAP-MD-26`.
**Next action:** dedicated expiry/consignment research for food/pharma/FMCG tenants (reopen `04` §10 item 2), not a re-read.

## S5 Replenishment / Route / Scheduler — replenishment, reordering rules, routes, rules, scheduler
**Question:** Can replenishment be explained as business logic without copying vendor architecture?
**Finding:** Yes: forecast → rule → proposal → confirm → owning-domain document (12); routes as eleven Thai templates (10 §3); scheduler as deterministic, logged background function. No rule engine or job architecture is described.
**Objections:** template list is an executor synthesis; Thai purchasing lead-time practice unknown; duplicate-proposal safety unproven.
**Evidence:** reopen `02` item 24, `07`, `11`; maps 10, 12.
**Gaps:** `GAP-MD-01`, `GAP-MD-14`, `GAP-MD-21`, `GAP-MD-23`.
**Next action:** validate template set with Thai SMEs; state idempotency requirement in Team B design-freeze checklist.

## S6 Valuation / Landed Cost / Accounting Handoff — landed costs, valuation, product categories
**Question:** Does Inventory emit enough facts for Accounting without owning Accounting truth?
**Finding:** Fact list (15 §2.1) and handoff matrix (15 §5, 04) are complete at business level and every accounting decision is routed Joint/Account. Landed cost mechanism and Thai import treatment held. `C-05` handled by Layer 1 only.
**Objections:** the package cannot prove the fact list is *sufficient* until Accounting's posting design exists (posting-architecture fork open); return cost basis conflicting.
**Evidence:** CORR-007B `09`, `17`; reopen `08`, `14`, `20`; map 15.
**Gaps:** `GAP-MD-05`, `GAP-MD-13`, `GAP-MD-24`, `C-03`, `C-05`.
**Next action:** Joint Session (ERPPLUS-140) using 15 §5 as Inventory-side input; independent `C-05` re-audit first.

## S7 Reporting / Analytics — stock, locations, valuation, warehouse analysis
**Question:** Do reports answer operational, management and audit questions separately?
**Finding:** Four report classes with audience matrix (16); integrity rules (as-of reproducibility, policy printed, exports tested, negatives shown). Warehouse analysis KPI set is a candidate only.
**Objections:** no report was ever studied at source; Thai statutory stock report format unknown; auditor expectations unvalidated.
**Evidence:** reopen `06`/`07` (`G-7`), `09`; map 16.
**Gaps:** `GAP-MD-12`, `GAP-MD-25`.
**Next action:** obtain authoritative Thai stock-report requirement via Accounting-Tax track; validate stock card layout with a Thai auditor.

## S8 Thai UX / Localization — all labels and workflow language
**Question:** Are Thai candidate names understandable to Thai SMEs and auditors?
**Finding:** 29 menu names + 14 report names proposed with seven naming principles (17). Five conflicts recorded (17 §4). All `UNVALIDATED`.
**Objections:** executor-authored Thai; no accountant/auditor/storekeeper review; risk of choosing accounting-register vocabulary where colloquial warehouse vocabulary is expected, and vice versa.
**Evidence:** reopen `04`, `12` (วัสดุสิ้นเปลือง alignment); 17.
**Gaps:** `GAP-MD-15` (branch labelling), `GAP-MD-30` (label validation panel).
**Next action:** two-panel review (storekeepers; accountants/auditors) with per-label acceptance record.

## S9 Migration / Data Quality — master data, balances, history, traceability
**Question:** Can legacy stock be migrated, reconciled and replayed without losing truth?
**Finding:** Not yet provable: no provenance layer, no idempotency key, no cutover opening-balance mechanism (`G-5`), cardinality transform undocumented, empirical incidence blocked (`N-DB-01`). Package supplies the requirement set (18: REC-01..10, DQ-01..10) but nothing is designed or tested.
**Objections:** requirement lists could be mistaken for a plan; they are not.
**Evidence:** reopen `06`, `11`, `12`; map 18.
**Gaps:** `GAP-MD-26`, `GAP-MD-27`, `GAP-MD-28`, `C-02`, `G-5`, `N-DB-01`.
**Next action:** Boss decisions on `C-02`, `U-03`; Team A profiling (once authorized); Joint `G-5` cross-proof design.

---

## Special Team Roll-Up

| Team | Material objection | Blocking? |
|---|---|---|
| S1 | No Thai warehouse walk-through | For Thai-fitness, yes |
| S2 | Kind tie-break, variants unevidenced | Team B precondition |
| S3 | Idempotency / locking | Boss decision |
| S4 | Expiry / consignment unresearched | For tracked industries, yes |
| S5 | Templates unvalidated; duplicate safety | Team B precondition |
| S6 | Posting design absent; `C-05` re-audit | Joint / Boss |
| S7 | Statutory report format | Accounting-Tax |
| S8 | Labels unvalidated | Team B precondition |
| S9 | No provenance / opening-balance mechanism | Migration authorization |

All nine return findings only; none authorizes progression.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
