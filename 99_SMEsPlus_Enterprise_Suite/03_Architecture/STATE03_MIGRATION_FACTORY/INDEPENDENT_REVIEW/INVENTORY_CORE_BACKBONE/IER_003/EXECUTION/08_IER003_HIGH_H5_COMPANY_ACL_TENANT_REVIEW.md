# 08 — High H5 (N-A13-02): Company Isolation / ACL / Record Rules — Independent Verdict

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Independently inspect `stock/security/` and determine whether company-scoped Stock Truth access is enforced | Independent Evidence Reviewer | `stock/security/ir.model.access.csv`, `stock/security/stock_security.xml` (both read in full) | 2026-09-01 | Boss | **VERIFIED WITH CONDITIONS — MAJOR CORRECTION** | Enforcement mechanism found; DB-layer gap (SAAS-03) stands unchanged as a separate, correctly-registered concern |

## TEAM A's claim (A14 Part 2, N-A13-02; A13 §5)

> "Record rules / ACLs governing `company_id` isolation not read this pass — out of this pass's module scope (`stock/security/` was not opened). Status: `EVIDENCE_MISSING`... Next Action: Read `stock/security/ir.model.access.csv` and any `ir.rule` XML data before treating company-scoping as either enforced or unenforced."

## What this review found

This review did exactly what TEAM A's own next-action instructed: opened `stock/security/ir.model.access.csv` (78 lines, standard group-based CRUD permissions) and `stock/security/stock_security.xml` (full file, 108 lines). The latter contains a `<data noupdate="1">` block of `ir.rule` records — Odoo's row-level record-rule mechanism — with an explicit `<!-- multi -->` comment marking the company-scoping section:

| Model | `domain_force` |
|---|---|
| `stock.picking` | `[('company_id', 'in', company_ids)]` |
| `stock.picking.type` | `[('company_id','in', company_ids)]` |
| `stock.putaway.rule` | `[('company_id','in', company_ids)]` |
| `stock.lot` | `[('company_id', 'in', company_ids + [False])]` |
| `stock.warehouse` | `[('company_id', 'in', company_ids)]` |
| `stock.location` | `[('company_id', 'in', company_ids + [False])]` |
| `stock.move` | `[('company_id', 'in', company_ids)]` |
| `stock.move.line` | `[('company_id', 'in', company_ids + [False])]` |
| `stock.quant` | `[('company_id', 'in', company_ids + [False])]` |
| `stock.warehouse.orderpoint` | `[('company_id', 'in', company_ids)]` |
| `stock.rule` (pull/push flow) | `[('company_id', 'in', company_ids + [False])]` |
| `stock.route` | `[('company_id', 'in', company_ids + [False])]` |
| `stock.package` | `[('company_id', 'in', company_ids + [False])]` |
| `stock.scrap` | `[('company_id', 'in', company_ids)]` |
| `report.stock.quantity` | `[('company_id', 'in', company_ids)]` |
| `stock.storage.category` | `[('company_id', 'in', company_ids + [False])]` |

This is **comprehensive, company-scoped row-level enforcement across essentially every core Inventory model** — not a partial or token set. Every model A3–A9 identify as a Stock Truth-bearing model (`stock.quant`, `stock.move`, `stock.move.line`, `stock.picking`, `stock.warehouse`, `stock.location`) is covered.

## What this does and does not prove

- **Confirms**: the reference source's Odoo ORM layer restricts read/write access to these models by `company_id` for any query executed through the standard ORM (not raw SQL, not `sudo()`-elevated code paths, both of which bypass `ir.rule` by design in Odoo).
- **Does not contradict** A2/A10 SAAS-03's finding that no **DB-level** CHECK constraint or row-security policy enforces this — `ir.rule` is an application/ORM-layer mechanism, evaluated in Python at query-build time, not a Postgres `ROW LEVEL SECURITY` policy. A direct-SQL client, or any code path using `sudo()`, is unaffected by these rules. SAAS-03 remains correctly registered as a **separate, still-open** concern about DB-layer guarantees — this finding narrows N-A13-02 specifically (the ORM-layer question), it does not close SAAS-03 (the DB-layer question).
- **Does not prove** SMEsPlus's own future multi-tenant isolation is safe — per A10's own governing rule, restated here: "Source behavior never proves SMEsPlus SaaS isolation." This finding establishes what the *reference source* does; SMEsPlus's own tenant model remains a distinct, later design decision.

## Independent verdict

**`VERIFIED WITH CONDITIONS`**

- Evidence read: `stock/security/ir.model.access.csv` (full), `stock/security/stock_security.xml` (full).
- What remains unknown: (1) whether every code path in `stock_account`/`sale_stock`/`purchase_stock`/`mrp` that touches these models does so through the standard ORM (and thus respects these rules) versus using `sudo()` internally — not audited this pass; (2) DB-level enforcement remains genuinely absent (SAAS-03, unchanged).
- **Inventory Gate blocking: NO** — was previously the literal enforcement-mechanism gap TEAM A flagged as unread; now read and found to be a real, comprehensive, evidenced mechanism.
- Stock Truth impact: None directly (this is an access-control fact, not a quantity/valuation fact).
- Accounting interface impact: None found in this specific file (Accounting's own `ir.rule` set was not read this pass — out of scope, Accounting-owned).
- Dependent-module impact: None additional.
- **SaaS/tenant impact: Direct — this is precisely the enforcement-mechanism evidence Cross-Proof scenario 9 needed.** Upgrades scenario 9 from "NOT READY — enforcement mechanism unverified on both sides" to "Inventory side ready" (Accounting's own side remains separately unverified — see [11](11_IER003_ACCOUNTING_X_INVENTORY_CROSS_PROOF_READINESS.md)).
- Migration impact: None additional.
- **Next owner / next action**: None required to close the narrow N-A13-02 question. SAAS-03 (DB-layer enforcement) remains open and correctly registered — no action changes there. Recommended: fold this citation into A10/A13/A14/A16 in TEAM A's next pass.

No Unknown was converted to a Fact beyond what the evidence supports — this finding is scoped precisely to what `ir.rule`/`ir.model.access.csv` prove (ORM-layer enforcement), and explicitly does not extend that to a DB-layer or SMEsPlus-target claim.
