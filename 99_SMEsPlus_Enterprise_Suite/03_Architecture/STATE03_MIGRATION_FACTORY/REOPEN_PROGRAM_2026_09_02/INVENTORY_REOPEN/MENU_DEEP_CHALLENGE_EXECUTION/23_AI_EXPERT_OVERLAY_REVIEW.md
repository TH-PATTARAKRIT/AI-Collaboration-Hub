# 23 — 4 AI Expert Roles Overlay Review

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-09 OUTPUT — OVERLAY CHALLENGE ONLY — NOT APPROVAL, NOT A SUBSTITUTE FOR 9+9`
Independence disclosure: four lenses applied in sequence by one session after 21 and 22 were drafted; not four independent parties (CORR-007B file 14 precedent). These roles may challenge, expose unknowns and recommend evidence; they may not approve.

---

## E1 Leader Functional Design
**Focus:** Replenishment, Inventory Adjustments, Transfers, Scrap, Lots/Serial Numbers, Operation Types.
**Required challenge:** Are user flows, UAT scenarios, exception paths and Thai UX names sufficient for later Team B design?

| Challenge | Assessment | Unknown exposed |
|---|---|---|
| User flows | Present for all six focus menus as step sequences with roles (12, 13, 14, 11, 09). Sufficient as *input*; not as design. | Which of the four count-freeze options; over-receipt tolerance; partial representation. |
| UAT scenarios | Not written. Exception grammar (14 §6) and "what goes wrong" rows (06 Q9) are scenario seeds, not test cases. | A UAT scenario catalogue is a Team B deliverable, not authorized. |
| Exception paths | Partial, backorder, cancel, return, over-fulfilment, backdate, damaged hold, conflict-during-count all named. | Damaged-goods state (`U-02`); Thai return practice. |
| Thai UX names | Proposed with principles; unvalidated. | Panel validation (`GAP-MD-30`). |
| Figma/UX readiness | Not reached; no screens exist and none should before Gate. | — |

**Recommendation:** treat 06/11–14/17 as the Team B kickoff reading pack *after* (a) real-user validation and (b) Boss decisions on freeze policy, tolerance policy, `C-02`. Evidence requirement: per-label and per-flow acceptance records from Thai users.

## E2 Leadership Database Design
**Focus:** Products, Product Variants, Lots/Serial Numbers, Locations, Stock Moves, UoM Categories, Product Packagings.
**Required challenge:** Are identities, relationships, constraints, migration keys and reconciliation facts clearly understood?

| Challenge | Assessment | Unknown exposed |
|---|---|---|
| Identities | 36 business objects with candidate identity (03 §1); movement fact attributes (11 §3). | Product kind tie-break; variant identity when attributes change; package identity (live vs history). |
| Relationships | Expressed as menu create/read ownership, not as a model — correct for this stage. | Category ↔ valuation policy relationship is Joint. |
| Constraints | 12 candidate invariants (03 §3) contrasting benchmark app-layer-only enforcement with DB-enforced candidates. | Whether Boss treats idempotency (INV-06) as Gate-blocking (`C-02`). |
| Migration keys | Provenance map required (OBJ-36) — does not exist. | Everything about the mapping layer. |
| Reconciliation facts | REC-01..10 (18 §2). | `G-5` opening value cross-proof; cardinality transform table. |

**Recommendation:** no schema work until Boss rules on `C-02`/`U-03` and the provenance layer is designed as a first-class Migration Factory component. Evidence requirement: Team A data profiling results against DQ-01..10.

## E3 Lead Integration & Localization
**Focus:** Valuation, Landed Costs, Product Categories, Accounting handoff, Thai reporting/control.
**Required challenge:** Are Thai accounting/tax/localization impacts separated from Inventory ownership and properly routed?

| Challenge | Assessment | Unknown exposed |
|---|---|---|
| Separation | Every accounting decision is classified Joint/Account/Interface (15 §5, 04 §4); Inventory closes none. | Posting-architecture fork; COGS timing; return cost basis. |
| Thai tax | WHT goods-vs-service, scrap destruction evidence, import duty/VAT, stock report format, costing norm — all routed to Accounting-Tax with `HOLD`. | Authoritative sources; `GRPA-M18-D` receiving owner still unconfirmed. |
| Localization of labels | Thai candidates exist; accounting labels (มูลค่าสินค้าคงเหลือ, สต็อกการ์ด) align with accountant vocabulary but unvalidated. | Auditor acceptance. |
| Routing | `PENDING_ACCOUNT_SESSION` items → ERPPLUS-138 track; `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` → ERPPLUS-140. | Whether the Account track has acknowledged receipt. |

**Recommendation:** hand 15 §5 and 04 §2 to the Joint Session as Inventory-side input only after `C-05` re-audit; confirm receiving owners in the Account track. Evidence requirement: Account track acknowledgement record.

## E4 Lead Code & UI Architect
**Focus:** Settings, Warehouses, Routes, Rules, Putaway Rules, Scheduler, Reporting.
**Required challenge:** Are future UI/process architecture risks visible without copying source code or vendor architecture?

| Challenge | Assessment | Unknown exposed |
|---|---|---|
| Vendor architecture leakage | Routes/rules reduced to Thai templates; scheduler to deterministic background function; settings to business questions; no code/model/path in package (mechanical scan, 28 §5). | Independent clean-room re-audit not performed. |
| UI risks | Hidden complexity behind templates must still be explainable (explanation records); SME tiering (T0/T1/T2) needs enforcement of switch-off guards; report exports must be acceptance-tested (benchmark defect lesson). | Tenant provisioning versus regeneration (`SAAS-04`) design. |
| Node.js SaaS implications | Not addressed by design (correct); requirements stated: DB-enforced isolation, idempotent jobs, versioned configuration. | Inventory SaaS invariant set (`U-03`). |
| Process architecture | Deterministic route resolution, immutable facts, native period guard independent of Accounting bridge. | Whether Inventory owns the period guard (reopen `05` §10 item 7). |

**Recommendation:** carry the reopen do-not-inherit list plus this package's "what was not carried" column (20 §1) as a mandatory clean-room checklist for any future Team B kickoff. Evidence requirement: independent Clean-Room Re-Audit (`C-05`) and mechanical scan repeated on Team B outputs.

---

## Overlay Contradictions and Cross-Notes

| # | Note |
|---|---|
| O-1 | E1 wants richer flows; E4 warns that richer flows drift toward design. Resolution: flows stay at "what happens and who", never "how the screen works". |
| O-2 | E2's DB-enforced invariants are candidate requirements that could be read as schema decisions; E3 notes valuation-related invariants (INV-10) are Joint. Resolution: 03 §3 labelled requirements, ownership per invariant. |
| O-3 | E3 and E1 both depend on Thai user validation that does not exist; this is the single precondition common to all four roles. |
| O-4 | None of the four roles can verify the package independently (single-session disclosure). |

**Overlay conclusion:** the package is sufficient as reference input and insufficient as design basis; the four roles recommend `HOLD / EVIDENCE REQUIRED` be carried and do not approve anything.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
