# A17 — Clean-Room Classification and Quarantine Register

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Confirm clean-room provenance discipline was followed throughout this DR-002 pass and register any quarantine items | Claude (Team A, DR-002) | This artifact | 2026-08-31 | Independent Evidence Review (pending) | VERIFIED | Blocks claiming clean-room PASS if violated; no violation found |

## 1. Discipline followed this pass

- All source reading was performed by three dispatched read-only research agents, each explicitly instructed: read-only, no writes to the source tree, cite exact field/method names rather than paraphrase, and separate observed vendor field names from any target-design proposal. Confirmed: zero write operations were issued against `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/` at any point this session (only `Read`/`Grep`/`Bash` read-only commands, `find`/`ls`/`grep`/`wc`).
- Every deliverable (A3–A13) cites vendor field/method names **only as evidence of business semantics** (e.g., "the field is named `is_storable`, gates X") — none proposes adopting those literal technical names as SMEsPlus's own schema. This mirrors the discipline GROUP A's own frozen evidence used (their C-06-equivalent clean-room boundary, reused DELTA-FIRST as a working pattern, not re-litigated here since it is an Account-domain-specific finding, not Inventory's).
- No vendor source code body, ORM class definition, or schema DDL was copied verbatim into any A0–A20 deliverable — every citation is `file path — Class.field_or_method_name`, not a code block reproduction.

## 2. Vendor terminology adopted into design — none

No SMEsPlus target design was produced in this pass (explicitly prohibited by DR-002 §13). Consequently, the "was vendor terminology adopted into target design" check that a design-time clean-room review would perform does not yet apply — there is no design artifact yet to check. This register instead confirms the **research artifacts themselves** stay within the evidence/business-semantics boundary, which they do (§1).

## 3. Database dump handling

- The dump (`iTEST02_2026-06-14_14-41-19.dump`) was never restored successfully this session (A2) — no row-level customer data was read, viewed, or reasoned over directly by this pass. Every DB-forensics finding reused in A2/A14 comes from GROUP A's own frozen, independently-corroborated prior work, not from this session's own inspection of customer data.
- Temporary local copies of the dump file made during the (unsuccessful) restore troubleshooting were deleted immediately (A2 §1) — no residual copy exists outside the original authorized source path.
- No dump content, raw or derived, was committed to this branch or referenced by literal customer data value anywhere in A0–A20.

## 4. Source-specific technical behaviors flagged for quarantine from Team B

Per DR-002 Mandatory Question #16 ("which source-specific technical behaviors must be quarantined from Team B"):

| Behavior | Why it must not leak into Team B design as-is |
|---|---|
| `product.type` 3-value Selection (`consu`/`service`/`combo`) and the `is_storable` boolean gating chain | This is this specific vendor's own historical naming/split; SMEsPlus's own product-classification model is a Team B design decision, informed by but not bound to this shape |
| `stock.move.value` living directly on the move (no `stock.valuation.layer`) | A vendor-specific (and possibly fork-specific, per N-A9-01) architectural choice — not evidence that SMEsPlus should or shouldn't use a similar pattern |
| The `stock.reference` grouping model replacing `procurement.group` | Same caution — a vendor implementation detail, not a design recommendation |
| `uom.uom.relative_uom_id` self-referential tree replacing `uom.category` | Same caution |
| String-literal branching on `type`/`picking_type.code` throughout the integration modules | A vendor technical-debt pattern (also flagged in GROUP A's External Dependency register §10) — explicitly **not** a pattern to replicate |
| The three unresolved third-party approval modules' existence and observed usage statistics | Business-fact evidence (a customer uses layered approval) is fair to carry forward; their internal Python logic is quarantined by construction — it is not even available to read (source absent from the machine) |
| `bh_parent_company` module (CORR-005, 2026-09-01): field *names/existence* (`brand_id`, `parent_company_id`, `hq_brand_id`, `is_hq_brand`, `store_type_id`, `bh_parent_company_code`) confirmed via `ir_model_data` by IER-003 | Per the Boss Inventory Scope Ruling, `bh_*`/`bhpro_*` modules are excluded from SMEsPlus source learning entirely — this is a hard quarantine, stronger than the other rows above: no further source acquisition, reading, or business-logic inference from this module is authorized, at all, for any team. Legacy-data provenance (column existence, for migration data-loss avoidance) is the only permitted carry-forward — see A12 §12 |

## 5. Statement

No vendor source code, schema, ORM structure, or workflow was copied into SMEsPlus target design in this pass, because no target design was produced. Every business fact recorded describes observed vendor behavior as **evidence**, consistent with the clean-room boundary restated in every A3–A13 deliverable. Critical Vendor-Derived Design Risk for this pass: **0** (no design exists yet to carry risk) — this is not asserted as a permanent clean-room PASS for whatever Team B eventually produces; that remains a future, Team-B-scoped clean-room review's responsibility.

No Evidence = No Progress.
