# Correction requests (structured)

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Raised by controller spot-check/cross-unit audits in this session (not by the independent verifier). Classification vocabulary and procedure: `00_PROTOCOL.md`.

## CR-001 — CORRECTION_REQUIRED · Material
- **Boundary / scope / Function-ID:** U08 — stock transfers — return eligibility; SDV-F06, GRV-F07
- **Claim-ID(s):** VDR-U08-C235 (+ neutral N-U08-127)
- **Original commit and packet:** U08 c8173586 / HP_U08
- **Missing or conflicting evidence:** C235 states a transfer is returnable only when done; with sales delivery installed (it is) any sales-linked transfer passes the eligibility check (finding by C01 audit F01, reproduced by controller).
- **Source/dump research required:** Return wizard + sale_stock override (read).
- **Acceptance criteria:** Effective rule stated with both branches and pointers; unknown outcome for not-done sales-linked returns routed to AWT.
- **Resolution packet:** U08-R1 — PROCESSED (re-verification requested)

## CR-002 — CORRECTION_REQUIRED · Material
- **Boundary / scope / Function-ID:** U11 — account entry lifecycle — payment state 'in payment'; PCO-F01 context
- **Claim-ID(s):** VDR-U11-C003, C039, C040, C042 (+ N-U11-002, N-U11-016)
- **Original commit and packet:** U11 4202eba8 / HP_U11
- **Missing or conflicting evidence:** Statements imply 'in payment' is reachable; the hook returns paid and has a single definition in Community (U12 and C01 F02).
- **Source/dump research required:** Hook definition and call sites; grep of addons for overrides.
- **Acceptance criteria:** Conditional wording; reachable only via external override; AWT for runtime display.
- **Resolution packet:** U11-R1 — PROCESSED (re-verification requested)

## CR-005 — CORRECTION_REQUIRED · Material
- **Boundary / scope / Function-ID:** U11 — invoice cancel — effect on settling payments
- **Claim-ID(s):** VDR-U11-C031, C058 (+ N-U11-013, N-U11-024)
- **Original commit and packet:** U11 4202eba8 / HP_U11
- **Missing or conflicting evidence:** Cancel sets 'payment_ids' to canceled; that field holds payments whose own entry is the cancelled entry, not an invoice's settling payments (C01 F12).
- **Source/dump research required:** Field definitions payment_ids vs matched_payment_ids.
- **Acceptance criteria:** Distinction stated; invoice-cancel outcome marked RT.
- **Resolution packet:** U11-R1 — PROCESSED (re-verification requested)

## CR-003 — CORRECTION_REQUIRED · Normal
- **Boundary / scope / Function-ID:** U12 — payment framework — enabled providers in dump
- **Claim-ID(s):** U12 CAP-U12-08 DB-reconciliation prose ('custom (enabled)')
- **Original commit and packet:** U12 0b9dd753 / HP_U12
- **Missing or conflicting evidence:** Enabled provider with code custom is the cash-on-delivery row owned by delivery, not the wire-transfer provider (U20).
- **Source/dump research required:** Provider data files; dump provider rows (config only).
- **Acceptance criteria:** Provider ownership stated.
- **Resolution packet:** U12-R1 — PROCESSED (re-verification requested)

## CR-004 — CORRECTION_REQUIRED · C1
- **Boundary / scope / Function-ID:** U10 — valuation — COGS timing hook map; SDV-F05, GRV-F04
- **Claim-ID(s):** VDR-U10-C336, C338, C339 (+ N-U10-171, N-U10-172)
- **Original commit and packet:** U10 4a4f39cf / HP_U10
- **Missing or conflicting evidence:** Hook map credits two extension points with COGS delta booking/refund; no method in addons calls either (C01 audit F04).
- **Source/dump research required:** Full-tree search for the hook names.
- **Acceptance criteria:** Override facts kept; inert status stated; real trigger path flagged for confirmation.
- **Resolution packet:** U10-R1 — PROCESSED (re-verification requested)

## CR-006 — CORRECTION_REQUIRED · Normal
- **Boundary / scope / Function-ID:** U04 — order-line margin cost source (stock-margin bridge)
- **Claim-ID(s):** VDR-U04-C354 (+ N-U04-199)
- **Original commit and packet:** U04 2d9932ef / HP_U04; U22 37e4d26f
- **Missing or conflicting evidence:** C354 says all other lines go to the base computation; a standard-cost line with valued moves and ordered qty keeps its stored cost (U22).
- **Source/dump research required:** Bridge cost-computation branches.
- **Acceptance criteria:** Branch table with pointers.
- **Resolution packet:** U04-R1 — PROCESSED (re-verification requested)

## CR-007 — NEEDS_MORE_EVIDENCE · C1
- **Boundary / scope / Function-ID:** C01 — O2C chain — reservation timing at confirmation (SDV-F02)
- **Claim-ID(s):** gap: no unit states it (audit F06)
- **Original commit and packet:** C01 c9083627 / HP_C01
- **Missing or conflicting evidence:** Chain narrative lacks when goods are reserved at order confirmation.
- **Source/dump research required:** Move confirm/assign path; operation-type reservation method; dump values.
- **Acceptance criteria:** Source rule + dump configuration stated; insufficient-stock behaviour to AWT.
- **Resolution packet:** C01-R1 — PROCESSED (re-verification requested)

## CR-010 — NEEDS_MORE_EVIDENCE · C1
- **Boundary / scope / Function-ID:** C01/U08/U11 — transfer date-done lock-period constraint (PCO-F04)
- **Claim-ID(s):** gap: only U10 C185/C186 (audit F14)
- **Original commit and packet:** C01 c9083627; U10 4a4f39cf
- **Missing or conflicting evidence:** Cut-off constraint on transfers not in order-to-cash/procure-to-pay narratives.
- **Source/dump research required:** stock_account picking lock-period check.
- **Acceptance criteria:** Cross-referenced chain statement with pointer.
- **Resolution packet:** C01-R1 — PROCESSED (re-verification requested)

## CR-008 — CORRECTION_REQUIRED · C1
- **Boundary / scope / Function-ID:** U10 — lock dates — posting inside a locked period; PCO-F01
- **Claim-ID(s):** VDR-U10-C150, C164, C194 (+ N-U10-074, N-U10-093, N-U10-096)
- **Original commit and packet:** U10 4a4f39cf / HP_U10
- **Missing or conflicting evidence:** U10 says post is refused inside a lock; posting shifts the date to the first open date (U11 CAP-04, C02 audit F01).
- **Source/dump research required:** Posting lock check, shift code, closing-entry post.
- **Acceptance criteria:** Shift rule + refusal-on-edit rule; per-lock date outcome to AWT.
- **Resolution packet:** U10-R2 — PROCESSED (re-verification requested)

## CR-009 — CORRECTION_REQUIRED · Material
- **Boundary / scope / Function-ID:** U07 — receipts/returns — inert extension methods; bill reset valuation
- **Claim-ID(s):** VDR-U07-C145, C097, C158; VDR-U10-C144, C145 (+ neutral refs)
- **Original commit and packet:** U07 03a764e2 / HP_U07; U10 4a4f39cf
- **Missing or conflicting evidence:** Return-wizard override never runs (signature/model mismatch), extra-move override orphaned, return classifier has no caller, bill reset does not re-value receipts (C02 audit F02, F19–F21).
- **Source/dump research required:** Base/override signatures and callers (full-tree search).
- **Acceptance criteria:** Inert status with pointers; link source for return moves flagged for AWT.
- **Resolution packet:** U07-R1 — PROCESSED (re-verification requested)

## CR-011 — CORRECTION_REQUIRED · Material
- **Boundary / scope / Function-ID:** B01 — control document — valuation flag wording, chart count
- **Claim-ID(s):** B01 §2.1, §3, B01-U05
- **Original commit and packet:** B01 1c7a8e8e
- **Missing or conflicting evidence:** Self-identified: equated anglo-saxon flag with perpetual switch; chart count 181 vs 179.
- **Source/dump research required:** Source field + dump rows.
- **Acceptance criteria:** Lineage packet with original wording preserved.
- **Resolution packet:** B01-R1 — PROCESSED (re-verification requested)

## CR-012 — CORRECTION_REQUIRED · Normal
- **Boundary / scope / Function-ID:** B02 — control document — theme row wording
- **Claim-ID(s):** B02 §1 theme row
- **Original commit and packet:** B02 d8760861
- **Missing or conflicting evidence:** Garbled wording.
- **Source/dump research required:** Dump counts by owner module.
- **Acceptance criteria:** Clear statement.
- **Resolution packet:** B02-R1 — PROCESSED (re-verification requested)

## CR-013 — NEEDS_MORE_EVIDENCE · Normal
- **Boundary / scope / Function-ID:** U06 — purchase order — bill creation entry points, receipt-validation acknowledgement, posting role, bill-side vendor price lookup ownership
- **Claim-ID(s):** gaps from C02 audit F04, F05, F16, F17
- **Original commit and packet:** U06 e0a987bc / HP_U06; C02 72cf594a
- **Missing or conflicting evidence:** U06 omits: no form-level create-bill button (bills from list header/upload/auto-complete/matching), receipt validation acknowledges the order, posting needs the invoicing role, vendor-price lookup on bills sits in U02.
- **Source/dump research required:** Bill creation paths, acknowledgement hook, security groups for posting.
- **Acceptance criteria:** Pointer-backed claims or explicit UNKNOWN.
- **Resolution packet:** U06-R1 — IN PROGRESS (worker)

## CR-014 — NEEDS_MORE_EVIDENCE · Normal
- **Boundary / scope / Function-ID:** U07 — receipts — double-negative condition; lot-to-PO link
- **Claim-ID(s):** gaps from C02 audit F06, F07
- **Original commit and packet:** U07 03a764e2 / HP_U07
- **Missing or conflicting evidence:** stock_move.py:196 double negative and purchase_stock/stock.py lot-to-PO link are covered by neither U07 nor U09.
- **Source/dump research required:** Read both sites; effect on received quantity and lot traceability.
- **Acceptance criteria:** Pointer-backed claims.
- **Resolution packet:** U07-R2 — IN PROGRESS (worker)

## CR-015 — NEEDS_MORE_EVIDENCE · C1
- **Boundary / scope / Function-ID:** U10 — period cut-off — accrued-orders wizard (goods received/delivered not invoiced); PCO-F03 accrual half
- **Claim-ID(s):** gap from C02 audit F15 (nobody owns the accrual wizard)
- **Original commit and packet:** U10 4a4f39cf; C02 72cf594a
- **Missing or conflicting evidence:** Accrual path is outside every unit; U10 found the closing report accrual getter empty.
- **Source/dump research required:** Accrued-orders wizard in account/sale_stock/purchase_stock: inputs, entries, reversal, lock interplay.
- **Acceptance criteria:** Full L2/L3 claims for the accrual path with 10-dimension coverage.
- **Resolution packet:** U10-R3 — IN PROGRESS (worker)

## CR-016 — RUNTIME/AWT_REQUIRED · Material
- **Boundary / scope / Function-ID:** multi — AWT backlog items from audits
- **Claim-ID(s):** C02 F03 (receipt recreation after reset), F12 (stock-side cancel rollback), F18 (reminder service-only filter), C01 F07 (confirmation override order), U08-R1 (return quantity for not-done sales-linked transfer), U10-R2 (date outcome per lock type)
- **Original commit and packet:** various
- **Missing or conflicting evidence:** Cannot be settled from source or dump; must not be inferred.
- **Source/dump research required:** None (runtime).
- **Acceptance criteria:** Entered in 06_AWT_BACKLOG.
- **Resolution packet:** — — RECORDED IN AWT BACKLOG


---
## Status log (append-only)
- 2026-10-02 — Verifier (independent, PR #74 comment 5937448609): `U08-R1`, `U10-R1`, `U10-R2`, `U11-R1` read in full → **ACCEPTED** at static-evidence tier; `U04-R1`, `U07-R1`, `U12-R1`, `B01-R1`, `B02-R1`, `C01-R1` reviewed at metadata level (full read queued); nothing sent back. CR-016 routed to AWT.
- 2026-10-02 — CR-013 → `U06-R1` (68 claims), CR-014 → `U07-R2` (38 claims), CR-015 → `U10-R3` (108 claims, C1): packets produced by correction worker, gate pass (pointer/anchor/neutral-leak), controller spot-check of two claims (stock_move double-negative line; accrual helper files without callers) reproduced. Status: **PROCESSED (re-verification requested)**; all three are supplements (no superseded originals).
- 2026-10-02 — **CR-018** (CORRECTION_REQUIRED · Normal): controller's mechanical country-pack profile corrected after U27 recount → packet `SCOPE-R1` (PROCESSED, re-verification requested). Self-identified through cross-unit comparison; originals preserved.
- 2026-10-02 — **CR-019** (CORRECTION_REQUIRED · Material): U11-C191 / U11 dim-5 corrected after TXA2 cross-check (invoice delivery date filled by the sales-delivery module; abnormal-document wizard active from posting buttons) → packet `U11-R2` (PROCESSED, re-verification requested).
- 2026-10-02 — **CR-017** (NEEDS_MORE_EVIDENCE · C1/Material, statutory lane): raw re-read of TXS conflicts and summarised high-risk statements → supplement `07_THAI_TAX_CORE/TXS-R1_statutory_conflict_resolution.md` + `TXS-R1_statutory_neutral.md` (59 rows; final base status 50 VERIFIED-OFFICIAL · 4 OFFICIAL-SUMMARY-ONLY · 4 UNVERIFIED · 1 CONFLICT). Controller independent corroboration: WHT minimum (Order Tor.Por. 4/2528) via an official RD search result. PROCESSED (re-verification requested).
- 2026-10-02 — **CR-020** (verifier request, numbered CR-017 by the verifier — ID collides with controller CR-017 = TXS-R1; this register uses CR-020 for it): CORRECTION_REQUIRED · Normal · relabel U24 CAP-U24-08 gap register `NOT PRESENT IN COMMUNITY SOURCE` → `NATIVE GAP / EXTENSION REQUIRED` → packet `U24-R1` (PROCESSED: label changed per item with statutory links to TXS where verified; items without a verified statutory need are labelled as such; amount-in-words kept out of the gap list). Re-verification requested.
- 2026-10-02 — **CR-021** (CORRECTION_REQUIRED · Normal): U17-C399 corrected after U39 cross-check (employee-departure wizard of the fleet bridge sets the assignment end date) → packet `U17-R1` (PROCESSED, re-verification requested).
- 2026-10-02 — **CR-022** (CORRECTION_REQUIRED · Normal): U13-C441 corrected and U13-C430 qualified after U34 cross-check (import tax tolerance 0.03 staged / no threshold legacy / 0.05 only in a comment; export-method shadowing RT) → packet `U13-R1` (PROCESSED, re-verification requested).
