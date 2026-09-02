# 03 — Menu Package Mechanical Leakage Scan

Method: all 29 deliverables (`00`–`28`) of `audit/inventory-menu-deep-challenge-2026-09-02-001` were extracted directly with `git show <branch>:<path>` into an isolated scratch directory and scanned independently of the package's own self-reported scan (`20_CLEAN_ROOM_PROCESS_TRANSFORMATION_REGISTER.md`, `28` §5) — a fresh re-scan used to corroborate or contradict that prior result, not restate it.

Patterns scanned, per the governing prompt §4.1 and the clean-room rule's vendor-token list: fenced code blocks; vendor ORM/model tokens (`stock.`, `product.`, `ir.`, `res.[a-z_]+.[a-z_]+`, `quant`, `orderpoint`, `picking[-_]?type`, `_action_*`, `sudo(`, `.py`, `addons/`, `__manifest__`); source-code syntax (`def `, `class `, `import`, SQL verbs); the vendor name "Odoo" itself (checked for context, not banned outright).

## 1. Fenced code blocks

8 files contain 14 fenced blocks total (`04`, `08`, `10`, `11`, `12`, `13`, `14`, `26`), all tagged ` ```text `. Every block was read in full: plain-language ASCII process-flow diagrams, warehouse/location tree sketches, configuration build-order sequences, or (in `26`) a session-prompt template. None contains Odoo Python syntax, ORM class/method definitions, XML view markup, or a vendor-specific model/field identifier as such — content uses SMEsPlus's own generic menu-ID notation (`MENU-CF-02`, `HO-04`, etc.) and Thai/English business labels. **This is legitimate diagramming, not source-code leakage** — a mechanical "any fenced block = leak" rule would produce a false positive here; content was inspected, not counted.

**Risk class: none at the code-syntax level.** (One of these same blocks — file `10` — is separately flagged below at the structural/naming level; that is a different question from code-syntax leakage.)

## 2. Vendor ORM / model / path tokens

One match, in `20` — but this is the package's own description of the scan methodology it ran ("tokens matching vendor model naming patterns (`stock.`, `product.`, `ir.`, ...)"), i.e. documentation of a control, not leaked content. No other file matched.

## 3. Source-code syntax (`def`, `class`, `import`, SQL)

Zero matches across all 29 files.

## 4. Vendor name "Odoo"

Three mentions, all governance/methodology framing, not treatment of Odoo as SMEsPlus's target architecture: `20` (self-description of the scan), `05` ("consistent with a current-generation Odoo-style Inventory application. Exact version is `UNKNOWN / EVIDENCE REQUIRED`" — correctly hedged), `28` (the package's own prior self-check, independently confirmed correct here).

## 5. Finding beyond the mandated token list: location-path notation carried from the benchmark (file `10`)

Direct reading of `10_WAREHOUSE_LOCATION_ROUTE_RULE_MAP.md` §2 (this session's own primary-source read, not a restatement) shows a location tree using the notation:

```
WH/Stock, WH/Input, WH/Quality, WH/Output, WH/Packing
```

— a parent-code/child-name slash-path convention applied to exactly the five-location set a well-known reference ERP uses by default to model 1-/2-/3-step receipt and delivery. The Thai labels attached to each node are genuine translation work, but the **structural notation and the specific five-node set** are carried over rather than re-derived from Thai warehouse practice. This is not caught by the mandated §4.1 pattern list because it is not a dotted model identifier, a file path, or code syntax — it is a naming/structure convention, a category the seven mandated patterns do not test for. It also sits in tension with the same file's own header: "No vendor model, field, rule-engine architecture, or naming is proposed for reuse."

**Classification: `NEEDS_WORDING_REWRITE`** — replace the `WH/xxx` path notation with prose description of location roles, and re-derive the location set itself from Thai warehouse practice (pending TBRAC field validation) rather than carrying the benchmark's specific five-node structure forward as if it were a business requirement.

## 6. Result

| Verdict | File count |
|---|---|
| `SAFE_CLEAN_ROOM_LEARNING` | 28 |
| `NEEDS_WORDING_REWRITE` | 1 (`10_WAREHOUSE_LOCATION_ROUTE_RULE_MAP.md`) |
| `NEEDS_QUARANTINE` / `FAIL_LEAK` | 0 |

**Zero token-level mechanical leakage found across all 29 deliverables** — this independently corroborates the package's own self-reported scan. **One structural (not token-level) carry-over finding** is surfaced beyond the mandated checklist, narrow and correctable, not evidence of systemic leakage. Per the package's own files (`20`, `28` §5), a mechanical sweep is explicitly not a substitute for the full independent re-audit; semantic-level questions (whether benchmark *behavior*, not just vocabulary, has become design by default) are carried in `05_SEMANTIC_CONTAMINATION_CHALLENGE_REGISTER.md`.
