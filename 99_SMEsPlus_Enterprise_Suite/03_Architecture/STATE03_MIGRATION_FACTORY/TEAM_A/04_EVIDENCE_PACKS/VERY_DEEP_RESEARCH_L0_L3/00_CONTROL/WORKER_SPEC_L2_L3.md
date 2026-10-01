# VDR Worker Specification — L2/L3 capability study (Odoo 19 Community)

> Applies to every research worker. Output status label on every file: `DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION`. Read-only on source. Community only.

## 0. Hard rules
1. **Source is read-only.** Never write under the Odoo source tree. Never start Odoo. No L5/AWT claims; anything that needs execution to confirm is flagged `RT` (RUNTIME/AWT REQUIRED).
2. **Scope = Odoo 19 Community only** (`odoo-19.0.post20260921/odoo/addons`, revision string `19.0.post20260921`). Do NOT open or attribute behavior from `Extra_Thailand`, `Extra_Module_scgl`, or any OEEL-1/OPL-1/proprietary/Enterprise code. If a Community module reaches another Community module outside your assignment, read it only as far as needed and record it as `DISCOVERED SUPPORTING MODULE` in your report.
3. **Do not assign** V-levels, "Complete", coverage %, denominator, Gate PASS or Clean-Room approval. Do not edit any existing file outside your two output files. Do not run git commands that change state (no add/commit/push).
4. **No fabrication.** Write a claim only for lines you actually read. Every pointer must be a real `path:line` that you viewed. When you could not determine something, say `UNKNOWN — EVIDENCE INSUFFICIENT` and what would resolve it.
5. **No business data.** The database may only be queried for configuration/structure (counts, flags, names of seeded configuration, ACL/rule/cron/automation rows). Never print or record partner, user, company-identifying or credential values.

## 1. Inputs
- Source root: `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/<module>`
- Prior structural extract (reuse, DELTA-FIRST; verified current): `~/STATE03_RESTRICTED_LOCAL/sourcemap/<module>.json`; prior candidate source-map record: `…/04_EVIDENCE_PACKS/SOURCE_MAP_CANDIDATE/MODULE_<module>.md` (may contain errors; re-verify before relying).
- Existing Function-ID index: `…/VERY_DEEP_RESEARCH_L0_L3/00_CONTROL/EXISTING_FUNCTION_ID_INDEX_53.json`. Use an existing ID only when the capability genuinely matches; otherwise `FUNCTION MAPPING REQUIRED` (never invent an ID).
- B01 reconciliation baseline: `…/03_DB_RECONCILIATION/B01_*.md`.
- Restored database (read-only configuration queries only):
  `PATH=/opt/homebrew/opt/postgresql@18/bin:$PATH psql -h /private/tmp/s03pg -p 54329 -U research -d itest19c_research -At -c "<SQL>"`
  Facts: 1 company, chart `th`, perpetual-valuation flag OFF, no transactions, demo not loaded, no valuation-layer table.

## 2. What to study
For each assigned capability (a business function such as "confirm a sales order", not a file), trace: entry points (UI/buttons/actions/crons/hooks) → methods → state transitions → data written → side effects on other modules → exceptions. Read inheritance: base definition AND every override in the assigned modules and in installed Community modules that extend it (find with grep for the method/model across `odoo/addons/*`). State the effective behavior as "base + overrides when module X is installed".

For **every critical capability** cover all ten dimensions (write `NOT APPLICABLE — <reason>` or `UNKNOWN` instead of skipping):
1 Happy path · 2 Reversal/cancel/negative path · 3 Multi-company / data-scope behavior · 4 Side effects & cross-module triggers · 5 Configuration & optionality · 6 Validation & constraints · 7 Roles & permissions (groups, ACL, record rules actually declared; confirm against the DB tables) · 8 Scheduled/automated behavior · 9 Exception & failure behavior · 10 Accounting, stock, audit, security & compliance implications.

L3 = three dimensions per capability: **(D1) business purpose & process semantics**, **(D2) architecture/data/object relationships**, **(D3) source/technical/workflow logic** (control/data flow, state machine, inheritance/override chain).

## 3. Output — two files, two layers (separate!)
### 3.1 Restricted Technical Evidence (may contain paths, models, fields, methods)
`…/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/<UNIT>_<short_name>.md`

Header: unit, modules, source revision, date, banner `RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION`, status label.
Per capability a section `## CAP-<UNIT>-<nn> <neutral capability name>` with: Function-ID(s) or `FUNCTION MAPPING REQUIRED`; D1; D2; D3 (include state diagram as a list `A -> B [trigger]`); the ten-dimension table; DB reconciliation (what the restored DB shows for this capability, config only); Unknown/Runtime list.
**Claims table** (one per file, at the end), exactly this pipe format, one claim per row, one line per row:

`| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |`

- Claim-ID `VDR-<UNIT>-C001…`; Pointer `<module>/<relative path>:<line>` (module-relative, e.g. `sale/models/sale_order.py:812`); **Anchor** = a short verbatim token (≤6 words, no pipes) that appears on that line or within 3 lines of it — a script will check this; Class ∈ `FACT` (stated directly by the code), `OBSERVATION` (restored DB/config), `INFERENCE` (derived from several lines — cite the lines in the statement), `UNKNOWN`; Condition = the configuration/installed-module condition (e.g. `valuation flag ON`, `module X installed`, `always`); Flags ∈ `RT` (runtime/AWT required), `CONTRA` (contradiction with prior evidence — name it), `—`; Neutral-ref = id of the neutral statement `N-<UNIT>-###` that abstracts it.
Aim for depth: a capability usually needs 15–40 claims. Prefer many precise claims over prose.

### 3.2 Neutral Knowledge (clean-room layer)
`…/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/<UNIT>_<short_name>_NEUTRAL.md`

For each capability, sections **WHAT · WHY · BUSINESS RULE · STATE · OPTIONALITY · DEPENDENCY · CONSTRAINT · RISK · UNKNOWN**, each statement tagged `[N-<UNIT>-###]` and linked to its claims by the same id used as Neutral-ref. Write in plain business/process language about *what the system must do and why*, e.g. "A confirmed order may not be changed once locked; unlocking requires the order-management role".
**Forbidden in the neutral file:** file paths, module/technical names with underscores or dots (`sale_order`, `account.move`), class/method/field/table/column names, XML ids, code, SQL, line numbers, vendor class structure. Use generic nouns (order, delivery, vendor bill, journal entry, lock date, valuation). Product names "Odoo 19 Community" is allowed once in the header only. A script scans for these.

## 4. Quality gates (run before you finish)
1. `python3 ~/STATE03_RESTRICTED_LOCAL/tools/vdr_check.py <restricted_file> <neutral_file>` — verifies every claim pointer exists, the anchor appears within ±3 lines, every Neutral-ref exists in the neutral file, and the neutral file has no forbidden vendor tokens. **Fix every failure** (re-read the source and correct the claim; delete claims you cannot support). Report the final script output.
2. Re-read 5 randomly chosen claims against source one last time for semantic support.
3. Report: capabilities covered, claim count, any capability you could not finish (say so — an honest partial is fine), DISCOVERED SUPPORTING MODULES, contradictions with prior evidence, RT list. Do not claim completeness.
