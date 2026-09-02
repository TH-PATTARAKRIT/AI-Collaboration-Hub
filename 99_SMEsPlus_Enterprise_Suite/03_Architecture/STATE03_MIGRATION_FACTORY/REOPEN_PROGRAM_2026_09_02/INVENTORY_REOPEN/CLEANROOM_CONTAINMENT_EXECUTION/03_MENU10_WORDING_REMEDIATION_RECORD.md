# 03 — Menu-10 Wording Remediation Record

## 1. What This Action Is

Remediation Action Register item 2 and Menu Package Mechanical Leakage Scan §5 both name a single, narrow, non-blocking defect in one file: `10_WAREHOUSE_LOCATION_ROUTE_RULE_MAP.md` §2 carries forward a reference ERP's benchmark-style parent-code/child-name path notation (`WH/Stock`, `WH/Input`, `WH/Quality`, `WH/Output`, `WH/Packing`) and its specific five-node location set, without re-deriving either from Thai warehouse practice. Classification: `NEEDS_WORDING_REWRITE`. Required action per the register: "replace the `WH/xxx` path notation with prose description of location roles, and re-derive the location set itself from Thai warehouse practice (pending TBRAC field validation) rather than carrying the benchmark's specific five-node structure forward as if it were a business requirement."

## 2. Where the Rewrite Was Made

File: `10_WAREHOUSE_LOCATION_ROUTE_RULE_MAP.md`, §2 only
Original location: `audit/inventory-menu-deep-challenge-2026-09-02-001` at commit `885f3cd5e920adae4c9746d13349c2bc50005aee` (unchanged — this session did not push to that branch)
This session's copy: same repository path, on `audit/inventory-cleanroom-containment-2026-09-02-001`

## 3. What Changed

- The fenced `text` block using `WH/Stock`, `WH/Input`, `WH/Quality`, `WH/Output`, `WH/Packing` slash-path notation was removed and replaced with a prose description plus a table of location roles (name, Thai label, business meaning, when used) — no vendor-style path notation remains in §2.
- A new caveat paragraph was added at the top of §2 explicitly marking the five-role set as **benchmark-derived and unvalidated**, stating that which roles Thai SME warehouses actually use — and under what names — is `UNKNOWN / EVIDENCE REQUIRED` pending TBRAC field input, and is not a business requirement established by the document.
- The virtual-location list (vendor, customer, loss, adjustment, production, transit) was kept but rewritten as prose rather than tree notation, for consistency with the rest of the rewritten section.
- The Thai labels themselves (translation work, e.g. "คลังสินค้า", "ตรวจคุณภาพ") were preserved unchanged — only the structural notation and the validation status changed.
- §1 and §3–§7 were **not** touched. This includes the `WH-A Stock` / `WH-B Stock` labels in the `RT-RESUPPLY` row of §3's route-template table: those are generic example warehouse labels (A/B), not the specific benchmark slash-path construct the Leakage Scan flagged in §2, and rewriting them is outside the "narrow" scope this session was given.

## 4. What Was Not Done

- The five-node location set itself was not re-derived from actual Thai warehouse practice — that requires TBRAC field input this session does not have, and the caveat says so explicitly rather than fabricating a substitute set.
- No other menu-package deliverable (of the 29 covered by the Leakage Scan) was touched; the Scan found the other 28 `SAFE_CLEAN_ROOM_LEARNING` and this session did not re-open them.
- No Boss Gate status was changed for the menu package as a whole.

## 5. Verification

A grep for `WH/` across the full edited file after the change found one remaining match: the caveat paragraph's own reference to `WH/Stock`-style notation, used to describe what was removed, not to reuse it. No fenced-code path notation of the original construct remains in §2.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
