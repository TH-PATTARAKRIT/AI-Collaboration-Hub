# 03 — Menu Package Mechanical Leakage Scan

Session: `SMEPLUS-26-09-02-INV-CLEANROOM-REAUDIT-001` | Control Level: `/L999.999`

Method: all 29 numbered deliverables under `MENU_DEEP_CHALLENGE_EXECUTION/` plus the separately-filed issuing prompt `04_NEW_SESSION_PROMPT_SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001.md` (30 files total) were extracted from `origin/audit/inventory-menu-deep-challenge-2026-09-02-001` via `git show` (no checkout, no merge) into a local scratch directory and scanned pattern-by-pattern. Every raw regex hit was individually re-classified as a true or false positive by reading the matched line in context. One finding below (§4) was located by direct reading rather than by a pre-specified pattern, then independently re-confirmed by this session against the live branch content.

---

## 1. Pattern Results (30 files)

| # | Pattern class | Raw hits | True positives | Notes |
|---|---|---|---|---|
| 1 | Fenced code blocks (` ``` `) | 32 lines (16 fence pairs), 9 files | **0** | Every fence is opened as ` ```text ` and contains ASCII process-flow arrows / location-tree diagrams in Thai/English business prose, not programming syntax |
| 2 | ORM/Python syntax (`def `, `self.`, `class `, `@api.`, `.sudo(`, `.create(`, `.write(`, `.search(`, `_compute_`, `_action_`) | 6 lines | **0** | `class` hits are all the English words "impact class", "storage classes", "first-class"; the single `_action_` hit is inside file `20`'s own sentence describing what its internal scan searches for |
| 3 | Vendor dotted identifiers (`stock.`, `product.`, `ir.`, `quant`, `orderpoint`, `picking`) | `quant` ≈ 45 lines, `picking` ≈ 6 lines, `orderpoint` = 1, rest 0 | **0** | `quant` hits are all "quantity/quantities"; `picking` hits are ordinary English ("picking strategy", "batch picking") plus file `20`'s and `28`'s self-referential meta-text |
| 4 | File-path leakage (`.py`, `/addons/`, `/models/`) | 1 | **0** | Inside file `20`'s meta-sentence naming the tokens its own prior scan searched for, not a leaked path |
| 5 | SQL/schema (`CREATE TABLE`, `ALTER TABLE`, `FOREIGN KEY`, column-def) | 0 | **0** | — |
| 6 | Source comments in prose (`#`, `//`) | ~103 (`#`) + 14 (`//`) | **0** | `#` hits are Markdown headings; `//` hits are `https://github.com/...` URLs in file `28`'s publication table |
| 7 | Named open-source ERP vendor (Odoo / ERPNext / Dolibarr / Tryton) | 6 (all "Odoo") | 0 policy-violating | See §2 |

**Zero true-positive mechanical leakage across categories 1–6.** Every one of the ~185 raw pattern hits traces to ordinary English business vocabulary or to the package's own self-referential audit-trail text, not to reproduced vendor syntax, model identifiers, file paths, or SQL.

## 2. Named-Vendor Mentions (Category 7 — Contextual Review)

| File | Line context | Judgment |
|---|---|---|
| `04_NEW_SESSION_PROMPT_...` (issuing prompt, ×4) | "Study Open ERP / Odoo-style Inventory menus as a process benchmark only"; "Do not claim SMEsPlus must follow Open ERP / Odoo behavior"; "Open ERP / Odoo = Process Benchmark Only" | Legitimate — this is the charter document defining the clean-room boundary; naming the benchmark in order to instruct against copying it is the correct and necessary use |
| `05_INVENTORY_SCREENSHOT_MENU_EVIDENCE_REGISTER.md` (×1) | "screenshot menu tree is consistent with a current-generation Odoo-style Inventory application" | Legitimate — an explicitly-labeled provenance/evidence register, not a design deliverable; states plainly "No label below is an approved SMEsPlus name" |
| `20_CLEAN_ROOM_PROCESS_TRANSFORMATION_REGISTER.md` (×1) | quoting its own banned-phrase example, "as Odoo does" | Legitimate — self-referential, naming the exact phrase the package prohibits itself from using |
| `28_SESSION_CLOSURE_...md` (×1) | self-report: "the word 'Odoo' appears only in governance context... Acceptable per prompt §2" | Legitimate — self-audit meta-text |

**None of the 25 Layer-2-facing process/design deliverable files (`06`–`19`, `21`–`26`) name the vendor anywhere.** That is the correct pattern for output that is supposed to be pure business-learning content; the vendor name is confined to governance/provenance/self-audit text, which is exactly where the package's own Layer 1/2 model says it belongs.

## 3. Extraction Integrity

All 30 `git show` extractions succeeded with no errors; the file set matches the 29-file inventory independently confirmed in `01_MANDATORY_EVIDENCE_INTAKE_REGISTER.md` §3.

## 4. Finding Outside the Seven Mandated Patterns — File `10`, Location-Path Notation

Direct read of `10_WAREHOUSE_LOCATION_ROUTE_RULE_MAP.md` §2 (independently re-fetched and confirmed by this session, not taken solely on the evidence-gathering pass's word) shows a location tree using the notation:

```text
[internal] WH/Stock  "คลังสินค้า"
[internal] WH/Input   "รับเข้า (รอตรวจ/รอเก็บ)"
[internal] WH/Quality "ตรวจคุณภาพ"
[internal] WH/Output  "รอจัดส่ง"
[internal] WH/Packing "แพ็กสินค้า"
```

This is a near-verbatim rendering of a specific reference-ERP default location scaffold: the parent-code/child-name slash path convention, applied to exactly the five-location set (Stock / Input / Quality / Output / Packing) that the benchmark uses to model 1-/2-/3-step receipt and delivery. The Thai labels attached to each node are genuine business-language translation, but the **structural notation and the specific location set** are carried over rather than re-derived from first principles.

This is not caught by the pattern list in §1 because it is not a dotted model identifier (`stock.location`), a file path, or code syntax — it is a naming/structure convention, a leak category the mandated seven patterns do not test for. It also sits in direct tension with the same file's own header: *"No vendor model, field, rule-engine architecture, or naming is proposed for reuse."* File `20`'s own internal scan (§4 of that file) confirms its token list only covers dotted model identifiers and prescriptive phrases — not path/notation leakage — so this gap was structurally unreachable by the package's self-scan, not merely missed by inattention.

Classification: **`NEEDS_WORDING_REWRITE`** — replace the `WH/xxx` path notation with a prose description of location roles (e.g., "an internal receiving-hold area used only when a multi-step receipt template is active"), and re-derive the location *set itself* from Thai warehouse practice rather than carrying the benchmark's specific five-node structure, pending TBRAC validation of what Thai SME warehouses actually use.

## 5. Per-File Classification Summary

| Verdict | File count |
|---|---|
| `SAFE_CLEAN_ROOM_LEARNING` | 29 |
| `NEEDS_WORDING_REWRITE` | 1 (`10_WAREHOUSE_LOCATION_ROUTE_RULE_MAP.md`) |
| `NEEDS_QUARANTINE` | 0 |
| `FAIL_LEAK` | 0 |

## 6. Overall Judgment

The package is **mechanically clean** against the seven specified leak categories — this independent re-scan corroborates the authoring session's own self-reported remediation (file `28` §5: "3 hit classes found on first pass... replaced with neutral business wording before publication"). The one substantive gap this re-audit surfaces, beyond the mandated checklist, is the location-path notation in file `10` — a real but narrow and correctable finding, not evidence of systemic leakage. Per the package's own files `20` §4 and `28` §5, a mechanical sweep (whether the authoring session's or this one) is explicitly **not** a substitute for the full independent Clean-Room Re-Audit; it establishes lexical/syntactic cleanliness only. Semantic-level questions (whether benchmark *behavior*, as opposed to benchmark *vocabulary*, has become design by default) are addressed separately in `05_SEMANTIC_CONTAMINATION_CHALLENGE_REGISTER.md`.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
