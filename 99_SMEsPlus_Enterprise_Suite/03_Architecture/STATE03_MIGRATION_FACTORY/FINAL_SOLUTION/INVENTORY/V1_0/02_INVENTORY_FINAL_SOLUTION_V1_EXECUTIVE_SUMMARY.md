# 02 — Inventory Final Solution v1.0 — Executive Summary

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V1-001` | Jira: `ERPPLUS-139`
Execution Branch: `design/inventory-final-solution-v1-2026-09-02-001`
Status: `DESIGN EVIDENCE PACKAGE — PREPARED FOR BOSS FINAL GATE REVIEW — NOT AN APPROVAL`

---

## 1. What This Package Is

This is the SMEsPlus-owned functional design for the Inventory module, version 1.0, expressed as business design: what a Thai SME needs to be able to do with its stock, what facts the system must hold, what controls must exist, and what the accounting consequence of each movement is.

It converts three rounds of prior clean-room study — a menu-by-menu process study, an independent clean-room re-audit, and a containment action on that re-audit's findings — into a single design record that stands on its own. From this point forward, an SMEsPlus reader should not need to consult any reference ERP to understand what the Inventory module is supposed to do.

**What it is not:** it is not an approval, not a `PASS`, not a schema, not an implementation plan, not a Team B / Team C / Development / Production / Release authorization, and not a merge into the canonical branch. It is prepared *for* the Boss Final Gate, and it stops there.

---

## 2. The Design in One Page

**Ownership.** Inventory owns **Stock Truth** — the single, immutable record of what physically moved, when, from where, to where, and in what quantity. Sales, Purchase and Manufacturing own commercial and production *intent* and receive movement facts. Accounting owns **Financial Truth** and receives valuation facts. Migration owns provenance and replay. Management reporting reads everything and owns nothing. No domain owns stock truth jointly with Inventory.

**The core fact.** Every quantity change in the system is one immutable movement fact: source location, destination location, product, quantity in the base unit, optional lot or serial, timestamp, actor, and source document. On-hand is derived from movement facts, never stored as an independently editable number. Corrections are made by new movements, never by editing history.

**The boundary that creates accounting.** A movement between two internal company locations changes *where* stock is and creates no accounting consequence. A movement crossing the boundary between an internal location and a non-internal counterpart — a supplier, a customer, a loss, an adjustment counterpart, production — changes *whether* the company owns the stock and therefore emits a valuation fact for Accounting to post. This single rule governs receipts, deliveries, returns, scrap, adjustments and manufacturing consumption alike.

**The Thai SME shape.** Most Thai SMEs run one warehouse, one-step receipt, one-step delivery, and count stock in pieces. Everything more advanced — multiple locations, lots and expiry, variants, packaging, landed cost, multi-step routes, barcode parsing, storage capacity — must exist as platform capability but stay switched off and invisible until the business needs it. Complexity is a setting, not a default.

**Language.** The user interface speaks the language of a Thai storekeeper and a Thai accountant, not the language of an ERP: รับเข้า, จ่ายออก, โอนย้าย, นับสต็อก, ตัดของเสีย, สต็อกการ์ด, มูลค่าสินค้าคงเหลือ. Every one of these candidate names is `UNVALIDATED - THAI USER REVIEW REQUIRED` — no Thai user has ever reviewed any Inventory label in this program.

---

## 3. Scope Covered

| Area | Files |
|---|---|
| Functional scope, boundaries, operating model, design principles | 03 |
| All 29 menus/functions, each under Purpose / Input / Process / Output / Accounting-Control Impact | 04 |
| End-to-end process flows and exception paths | 05 |
| Conceptual business-object model, identities, invariants (no schema) | 06 |
| Accounting-control impact of every stock event | 07 |
| Valuation, landed cost, and analytic/allocation cost for decision support | 08 |
| Reporting, stock card, dashboards, UAT-ready report requirements | 09 |
| Cross-module handoff with Sales, Purchase, Accounting, Manufacturing, POS/Barcode, Migration, Tax | 10 |
| Thai localization, UX naming, statutory routing | 11 |
| Every unresolved gap and decision | 12 |
| 9 Veto + 9 Special Team + 4 Expert Overlay challenge | 13 |
| Boss Final Gate package | 14 |
| Recommended next session | 15 |
| Manifest and closure | 16, 17 |

All 29 menus are covered. None is blank. Where the evidence chain is thin, this package writes an explicit SMEsPlus design hypothesis and labels it `UNVALIDATED - THAI USER REVIEW REQUIRED` rather than leaving a hole or inventing a fact.

---

## 4. The Five Things Boss Should Look At First

1. **Valuation policy ownership is still undecided.** Which object owns the costing method and valuation timing — product category, product, warehouse, or a standalone policy object — is a Joint Accounting ↔ Inventory decision that no Inventory session can make. Everything about the valuation report, the landed-cost posting and the period-close reconciliation waits behind it. (Files 07, 08; register items `GAP-FS-01`, `RISK-JOINT-01`.)

2. **Movement idempotency is a design invariant with no ruling.** Without a unique demand-identity key, a retried scheduler run or a retried integration call can create duplicate movement chains — duplicated stock, duplicated cost. This package treats it as mandatory; the carried finding `C-02` says its severity is Boss's call. (Files 06, 05; item `RISK-C02`.)

3. **`C-05` history containment is still open.** The current evidence surface is independently confirmed clean and this package reproduces none of the quarantined material, but the pre-remediation history remains reachable by any ordinary clone. That is a Boss-only repository-governance decision, and this package does not touch it. (Item `RISK-C05`.)

4. **No Thai user has validated anything.** Not one label, not one count practice, not one document split, not one reason code. This is the single precondition shared by every part of the design. (File 11; item `GAP-FS-11`.)

5. **Every Thai statutory claim is on hold.** Stock report format, scrap destruction evidence, import duty and VAT treatment, withholding-tax correlation by product kind, and the costing norm are all routed to the Accounting-Tax track marked `HOLD / EVIDENCE REQUIRED`. This session has no legal evidence source and asserts nothing. (File 11 §5.)

---

## 5. Clean-Room Position

Everything in this package is Layer 1. The reference ERP studied in earlier rounds is referred to only as "the reference ERP" or "the benchmark". No source code, model or field name, method name, database schema, markup structure, menu definition, or file-and-line citation appears anywhere in files 02–17. A mechanical vendor-token scan was run over this output directory before the final commit; its result is recorded in file 17 §4.

The two specific clean-room controls inherited from the containment branch are preserved:

- the `C-05` history-containment warning, restated and not weakened;
- the corrected warehouse/location wording, in which the five internal-location roles are described in prose and marked benchmark-derived and unvalidated rather than presented as a Thai business requirement.

---

## 6. Terminal Position of This Summary

This summary declares nothing. The package's single terminal status is stated in `14_BOSS_FINAL_GATE_PACKAGE.md` and `17_SESSION_CLOSURE_SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V1-001.md`.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
