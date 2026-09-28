> Domain: INVENTORY_CORE_BACKBONE | Lineage Reconciliation (Boss Order, 2026-09-28, §3) | Provenance-by-reference — no branch merged | Boss sole Final Approver

# 03 — LINEAGE RECONCILIATION: DR-002 → CORR ROUNDS → REOPEN PROGRAM → PRESENT

Produced in response to Boss's direct order to reconcile the full Inventory Core Backbone evidence lineage before any of it is treated as usable Deep Study input (see `GOODS_RECEIPT_VALIDATION_PILOT/22_UNKNOWN_AND_GAPS.md` GAP-GRV-02). **No historical branch was merged.** This file was built by inspecting branch trees and reading two authoritative artifacts that already exist on the `audit/inventory-reopen-2026-09-02-inv-reopen-001` branch — its own prior-round reconciliation register (deliverable 15) and IDR-007's Boss recommendation (deliverable 10) — rather than re-deriving the reconciliation from zero (DELTA-FIRST).

## A. Branch / commit / artifact-set table

| Round | Branch | Commit SHA | Artifact set (count) | Evidence tier |
|---|---|---|---|---|
| R01 | — (prompt only) | — | Prompt only; no execution artifact ever existed | N/A |
| DR-002 | `claude/inventory-core-backbone-dr002` | `b31597fafa318c2edd9047ad89c128e4ace2e7cb` | 21 files, `DEEP_RESEARCH_DR002/EXECUTION/A0–A20` | Source-tier (Team A primary-source reading) |
| IER-003 (Independent Review) | referenced only; not independently walked this round | `45c749eae826642872ccc2dc09f0f714932c5b8e` | Not enumerated this round | Source-tier (independent) |
| CORR-004 | `claude/inventory-core-backbone-h2-h3-corr004` | `b31597fafa318c2edd9047ad89c128e4ace2e7cb` (identical to DR-002 tip) | Superseded before execution | N/A |
| CORR-005 | `claude/inventory-core-backbone-register-recon-corr005` | `d69da7900941bdae209eb33af20ac24e4893d536` | DR-002's 21 files + 7 new, `CORRECTIVE_CORR_005/EXECUTION/01–07` | Source-tier reconciliation |
| IDR-006 | — | — | Non-executed, superseded (per REOPEN's own Track 01 finding) | N/A |
| IDR-007 (Independent Delta Review of CORR-005) | not separately identified this round; content reachable via `audit/inventory-core-corr007b-3high-closure-010` tree | — | 12 files, `INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IDR_007/EXECUTION/01–12` | Independent-review tier |
| CORR-006 (Boss High Reproof) | `audit/inventory-core-corr006-boss-high-reproof-008` | `46a848375b4878f6d4b3e82cfeab4e2e6d6cb552` | 1 file (`01_CORR006_BOSS_HIGH_ESCALATION_REPROOF_REPORT.md`) at this domain path | Independent-review tier |
| CORR-007A (GRPA-M18 / WHT 50TWI) | `audit/inventory-core-corr007a-grpa-m18-wht-50twi-009` | `deceb7339b39eba309236782f159f8393224f5fd` | 7 files, `CORR_007A_GRPA_M18_WHT_50TWI/EXECUTION/01–07` | Independent-review tier, Thai-tax sub-scope |
| **CORR-007B** (3-High closure; controlling prior branch) | `audit/inventory-core-corr007b-3high-closure-010` | `9996072aa3a353dca99de4b22e8611171e24baf4` | 17 files, `CORR_007B_3HIGH_CLOSURE/EXECUTION/01–17`; also carries IDR-007's 12 files forward in its tree | Independent-review tier + Clean-Room remediation |
| **REOPEN** (Full Reopen — recommended canonical candidate) | `audit/inventory-reopen-2026-09-02-inv-reopen-001` | `170af9ea7a5afd127abcaae0ffb40aaa1fa25d4d` | 20 files, `REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/EXECUTION/01–20` | Full 9-Veto-Council independent revalidation, built by re-verifying (not assuming) all prior rounds |

## B. Supersedes / superseded-by

`R01` superseded-before-execution by `DR-002`. `CORR-004` superseded-before-execution, confirmed byte-identical to DR-002's tip. `IDR-006` non-executed, superseded, confirmed byte-identical to CORR-005's tip. Everything from `DR-002` through `CORR-007B` is **not superseded/discarded** — REOPEN explicitly frames itself as *"FULL-SCOPE REVALIDATION FROM ACCUMULATED LEARNING — NOT RESET-TO-ZERO RESEARCH"* and carries every prior round forward by reference, re-verifying rather than replacing it.

## C. Valid / stale / conflicting / unresolved classification (per REOPEN's own deliverable 15, reproduced/summarized here — not re-derived)

- **Six rounds carry forward with NO material delta**: CORR-005, IDR-007, CORR-006, CORR-007A, and the DR-002 High findings `GRPA-H4`, `N-A7-03`/`N-A9-02`.
- **Two rounds/findings carry forward WITH a precision note** (valid, but with a named caveat): DR-002 itself (its own named Gate criterion was never formally re-declared/retired by a later round), IER-003 (its document is physically unreachable from the CORR-007B branch tree — a chain-of-custody gap, independently confirmed twice), the Thai-branch dual-concept finding `GRPA-H8/H3` (approved baseline ≠ proven — the relevant COA gate is `NOT STARTED`), and the company-ACL finding `N-A13-02` (two named residuals remain open).
- **One round is PARTIALLY REVALIDATED, not fully valid as originally packaged**: **CORR-007B** — its overall disposition stands, but its own supporting evidence package for finding `N-A12-01` (files numbered 08/09 in its EXECUTION folder) contained **verbatim vendor source-code reproduction** — a Clean-Room boundary violation, tracked as item `C-05`. This was found and remediated (files rewritten as clean-room learning summaries; a remediation record was added) **on the same CORR-007B branch**, but an **independent Clean-Room re-audit of that remediation is still outstanding** per the branch's own Session Link Register.
- **No round is classified `REOPENED — CONTRADICTING EVIDENCE`** at the round level. The one individual item that was ambiguous (`N-A7-04`, a tracking-list omission) resolved favorably (mechanism located, not contradicted).
- **Two items are structurally uncloseable by further desk research**: `H2` (`bh_parent_company`, closed by Boss scope exclusion — requires external vendor/customer sourcing to go further, which is out of scope by that same exclusion) and `H3` (Thai-branch dual-concept — requires a real Thai-business-user interview, not more source reading).

## D. Carry-forward eligibility

**Eligible.** The entire `DR-002 → CORR-005 → IDR-007 → CORR-006 → CORR-007A → CORR-007B` chain is carry-forward-eligible as historical evidence lineage, and REOPEN is itself the artifact that performs and documents that carry-forward. Nothing in this chain should be re-executed from zero. The one open action is independent re-verification of the CORR-007B Clean-Room remediation (item C-05) — a re-audit of a fix already made, not a re-opening of the underlying research.

## E. Material Delta detected (this reconciliation round)

**MD-INV-LINEAGE-01**: The existence of a documented, already-remediated Clean-Room violation (`C-05`) inside the prior Inventory evidence chain is itself Material Delta relative to what this Deep Study workstream previously knew (GAP-GRV-02 originally only flagged the chain as "location unclear", not as "contains a known, remediated but not-yet-independently-re-audited Clean-Room finding"). This changes GAP-GRV-02's disposition from a simple location/merge question into one that also carries a pending independent Clean-Room re-audit requirement.

## F. Recommended canonical candidate

**`audit/inventory-reopen-2026-09-02-inv-reopen-001` @ `170af9ea7a5afd127abcaae0ffb40aaa1fa25d4d`** is the recommended canonical candidate: it is the most current, most complete synthesis, built by independently re-verifying (not assuming) everything before it, across all nine 9-Veto-Council mandates. Per its own Session Link Register:

- Terminal status: `INVENTORY FULL REOPEN DEEP REVALIDATION COMPLETE — READY FOR INDEPENDENT REOPEN AUDIT`.
- Gate PASS: **not declared**. Team B / Team C / Development: **not authorized**. Final Gate: **pending Boss.**
- Outstanding action named by the branch itself: an **independent Clean-Room Re-Audit** of the C-05 remediation, before any Team B/C reliance.

This recommendation is carried into `00_Architecture_Governance/STATE03_BOSS_GATE_QUEUE.md` as a queued Boss-only decision (merge/canonical-designation authorization) — it is not self-executed here, and no branch was merged to produce this file.

## G. Effect on `GOODS_RECEIPT_VALIDATION_PILOT/22_UNKNOWN_AND_GAPS.md` GAP-GRV-02

GAP-GRV-02 is updated (see that file) from "location confirmed, disposition pending" to "full lineage reconciled to a recommended canonical candidate (REOPEN), with one outstanding independent Clean-Room re-audit item and a Boss merge/canonical-designation decision now queued in `STATE03_BOSS_GATE_QUEUE.md`." This pilot's own findings still do not use any content from this chain — they remain documentation-tier only, sourced from Odoo 19 public documentation.
