# 26 — Next Prompt Recommendation

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `RECOMMENDATION ONLY — BOSS DECIDES`

---

## 1. Recommended Next Controlled Actions (ordered)

| # | Action | Type | Why first | Proposed session ID |
|---|---|---|---|---|
| 1 | **Boss written Gate decision** on the Inventory Reopen package (`170af9ea`) and acknowledgement of this reference package | Boss decision | Two rounds now end in "READY FOR BOSS" with no ruling (reopen Tier 0 item 0.5) | — |
| 2 | **Independent Clean-Room Re-Audit** of CORR-007B `08`/`09` and of this 29-file package (mechanical + citation-level sweep by a session that did not author either) | Audit | `C-05` gate; precondition for any Team B reading | `SMEPLUS-26-09-0X-INV-CLEANROOM-REAUDIT-001` |
| 3 | **TBRAC real-user validation session** (named panel: 2+ Thai SME warehouses, 1 accountant, 1 auditor) walking through 17 (names), 14/13 (documents, count, scrap), 11 §4 (roles) with per-item acceptance records | Research / validation | Every Thai-fitness claim is unvalidated; single common precondition of all overlay roles | `SMEPLUS-26-09-0X-INV-TBRAC-USER-VALIDATION-001` |
| 4 | **Boss decision pack**: `C-02` idempotency severity; `U-03` Inventory SaaS invariants; `U-07` Council definition; authorization scope (`U-01`); freeze/tolerance policy decision path | Boss decision | Unblocks Team B preconditions | — |
| 5 | **Account × Inventory Joint Session (ERPPLUS-140)** using 15 §5, 04 §2, reopen `20` as Inventory-side input | Joint | Blocks Joint Backbone publication | as already planned |
| 6 | **Targeted research passes** (each one bounded session): expiry/consignment; variants/packaging/barcode; landed-cost mechanism; cross-company transfer; Thai statutory reporting formats via Accounting-Tax | Research | `HOLD / EVIDENCE REQUIRED` rows | `SMEPLUS-26-09-0X-INV-RESEARCH-<topic>-001` |
| 7 | Governance hygiene: archive screenshots; populate ledger `INV-FP` rows; correct canonical evidence index | PMO | Traceability | — |

Team B, Team C, Development: **not recommended and not authorized** by anything above.

---

## 2. Draft Skeleton for Action 3 (TBRAC validation) — for Boss/PMO to challenge before issuance

```text
[SMEPLUS-26-09-0X-INV-TBRAC-USER-VALIDATION-001]
Mode: FIELD VALIDATION / EVIDENCE CAPTURE / NO DESIGN / CLEAN-ROOM
Inputs: 17 (labels), 06 (menu flows), 11 §4 (roles), 13 (count/scrap), 14 (documents)
Panel: named per TBRAC control document §10 (Boss assigns membership)
Method: structured walk-through per menu; per label: accept / rename / reject + reason; per flow: "we do it this way / we do not do this / missing step"
Outputs: acceptance register per label and flow; Thai reason-code taxonomy for adjustments and scrap; observed count practice; observed document names/numbering; industry conditionality confirmation
Terminal: VALIDATION EVIDENCE PUBLISHED — NOT DESIGN APPROVAL
Prohibited: designing screens; choosing freeze policy; asserting statutory rules
```

---

## 3. What Must Not Happen Next

- No Team B kickoff reading this package before actions 2 and 3.
- No migration tooling before `C-02`, `U-03`, provenance layer design and `G-5` certification design.
- No statutory claim in any Inventory document without Accounting-Tax authoritative evidence.
- No merge of this branch to `SMEsPlus` without Boss decision (consistent with the reopen chain's non-merge pattern).

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
