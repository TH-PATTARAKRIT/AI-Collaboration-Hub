# CORR-007A — Team 5: Final Disposition & Boss Recommendation

Session: `SMEPLUS-26-09-01-CORR007A-GRPA-M18-WHT-50TWI-001`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `audit/inventory-core-corr007a-grpa-m18-wht-50twi-009`
Base commit: `46a848375b4878f6d4b3e82cfeab4e2e6d6cb552` (CORR-006, `audit/inventory-core-corr006-boss-high-reproof-008`)
Timestamp: 2026-09-01
Mode: Evidence-first / clean-room / no development authorization

## 1. Independent Challenge Pass (Team 5 vs. Teams 1–4)

- **Unsupported-closure check**: Teams 1-3's FOUND claims were re-verified by this team by re-opening `reports/layout.xml` and `models/withholding_tax_cert.py` independently and re-confirming field/CSS-class correspondence; no unsupported claim was found. The three gaps Team 2 raised (branch number, 3/7 tax-form checkboxes, 2/4 WHT-condition checkboxes) are real and independently reproducible from the same source lines cited.
- **SHA manifest check**: see `06_CORR007A_SHA256_MANIFEST.txt` — every source file cited in Teams 1-4 has a computed SHA-256; spot-recomputation matches.
- **Boss-only decision boundary check**: no document in this package declares Gate PASS, Team B authorization, or Team C authorization. All three are explicitly marked NO below.
- **Render-proof honesty check**: Team 3 does not claim a PDF was actually generated. It says the chain is proven statically and names the exact reason live execution did not happen (scope-prohibited Odoo install/production connection). This team concurs that is an accurate, non-inflated characterization.
- **Boundary-integrity check**: Team 4 does not close PND3/PND53 using certificate evidence. Confirmed no cross-contamination of disposition.

## 2. GRPA-M18 Disposition Table

| Sub-item | Description | Disposition | Basis |
|---|---|---|---|
| `GRPA-M18-A` | 50-twi source form existence | **RESOLVED** | Module `l10n_th_withholding_tax_cert_form` fully located, SHA-256-hashed, 78/78 zip entries accounted for. Team 1. |
| `GRPA-M18-B` | 50-twi field mapping vs. Boss image | **PARTIAL — HIGH-CONFIDENCE, THREE NAMED GAPS** | 9 of 14 required fields FOUND with full source citation; 1 NOT FOUND (branch number — low materiality, no branch box on this specific form image); 4 rows PARTIAL, collapsing to two functional gaps: tax-form-code checkboxes (4/7 supported) and WHT-condition checkboxes (2/4 supported). Team 2. Per task Case B: because field mapping is incomplete, `GRPA-M18-B` cannot be marked fully `RESOLVED` — it is `PARTIAL`, with materiality assessed as low-to-medium (form-code and WHT-condition completeness are Accounting/Tax scoping items, not Inventory blockers). |
| `GRPA-M18-C` | Render/print path proof | **RESOLVED AS STATIC CHAIN PROOF (COMPLETE) — LIVE RENDER NOT EXECUTED** | Full action→template→image chain traced and cited; background image is byte-identical evidence-file reuse; source-level automated test (`test_01_print_wt_cert_form`) exercises the same call path. Live execution intentionally not performed — out of authorized session scope (no install, no production connection), not a missing-evidence gap. Team 3. |
| `GRPA-M18-D` | PND3/PND53 monthly filing/export correctness | **CONTROLLED CARRY-FORWARD TO ACCOUNTING/TAX** (unchanged from CORR-006) | Certificate module is code-level separate from `l10n_th_reports/models/tax_report_pnd.py`. This session supplies no new evidence for or against PND3/PND53 statutory completeness and does not attempt to close it. Team 4. |
| `GRPA-M18-E` | Legal/tax statutory sign-off boundary | **LEGAL_TAX_REVIEW_REQUIRED** | No official Thai Revenue Department verification was performed or is claimed anywhere in this package. The three named field-mapping gaps (`GRPA-M18-B`) specifically require Accounting/Tax judgment on materiality before any statutory-compliance representation can be made. |

## 3. Remaining blocker count after CORR-007A

- **1 remaining High-severity blocker outside this session's scope**: `GRPA-M18-D` (PND3/PND53 filing/export), unchanged carry-forward from CORR-006 — not newly created or newly resolved here.
- **0 new High blockers created by CORR-007A.**
- `GRPA-M18-B`'s three named gaps are downgraded from "unknown/unproven" (CORR-006's original position, which did not examine the certificate module at all) to "known, named, and evidence-cited, pending Accounting/Tax materiality judgment" — a strict evidentiary improvement, not a closure.

## 4. Does GRPA-M18 still block the Inventory Evidence Gate?

**No, not as a High Inventory blocker.** The original CORR-006 concern (`GRPA-M18` re-escalated to High as "source implementation located but statutory correctness not fully proven") is now split:
- The certificate existence/mapping/render sub-items (A/B/C) are proven to the degree source evidence can prove them, with named residual gaps that are Accounting/Tax-domain, not Inventory-domain.
- The filing sub-item (D) was never an Inventory Core Backbone concern in the first place — it is an Accounting/Tax statutory-filing concern that happened to be bundled under the same `GRPA-M18` label. Team 4 formally separates it.
- The legal sign-off sub-item (E) requires human statutory review that no source-code audit can substitute for, by definition.

Recommendation: `GRPA-M18` should be **removed from the Inventory Evidence Gate's High blocker list** and tracked going forward as an Accounting/Tax-domain item (`GRPA-M18-D`) plus a legal-review item (`GRPA-M18-E`), neither of which is an Inventory Core Backbone blocker.

## 5. Team B / Team C authorization

- Team B (Inventory Design) authorized from this task: **NO**
- Team C (Development) authorized from this task: **NO**

## 6. Boss Decision Options

1. **ACCEPT CLOSURE OF GRPA-M18-A/B/C** — with `GRPA-M18-B` explicitly accepted as PARTIAL (branch number not rendered; 3/7 tax-form checkboxes and 2/4 WHT-condition checkboxes unsupported) and `GRPA-M18-C` explicitly accepted as static-chain-proof-only (no live render executed this session).
2. **ACCEPT PND3/PND53 AS ACCOUNTING/TAX CARRY-FORWARD** — `GRPA-M18-D` remains High under Accounting/Tax ownership, unaffected by this session.
3. **KEEP GRPA-M18 HIGH** — if Boss judges the three named field-mapping gaps or the absence of a live render to be materially disqualifying, GRPA-M18 (or its B/C sub-items specifically) can remain High pending either a live-render session (would require explicit authorization to install/run the module) or a scoped fix.
4. **REQUEST ADDITIONAL TAX REVIEW** — for `GRPA-M18-E` and/or the materiality of the `GRPA-M18-B` gaps (form-code/WHT-condition checkbox coverage), route to Accounting/Tax for statutory sign-off.

## 7. Final Status

**CORR-007A COMPLETE — READY FOR BOSS GRPA-M18 DECISION**

This is not a Gate PASS. This is not Team B or Team C authorization. This is not a statutory legal sign-off. Boss remains the sole Final Approver.
