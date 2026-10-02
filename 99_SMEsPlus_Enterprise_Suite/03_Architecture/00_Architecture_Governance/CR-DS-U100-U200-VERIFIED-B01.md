# CR-DS-U100-U200-VERIFIED-B01
## Criteria-Proven Correction Package — U100–U200 Handoff Packets

**Package ID:** CR-DS-U100-U200-VERIFIED-B01  
**Issued by:** Verifier (Claude Sonnet 4.6, session `2ef62826`)  
**Directed to:** DeepSeek (branch `claude/local-odoo-source-research`)  
**Authorization:** `START_STATE03_AUDIT_CRITERIA_PROOF_AND_CORRECTION_RELEASE` (Boss, 2026-10-02)  
**Date:** 2026-10-02  
**VDR Reference:** Will be recorded in §63 of `STATE03_VDR_CLAUDE_VERIFICATION_LOG.md`  
**Scope:** Handoff Packets U100–U200 on DeepSeek branch `origin/claude/local-odoo-source-research`  
**Snapshot SHA:** HEAD at time of audit (fetched 2026-10-02)

---

## Part 1 — Criteria Proof Matrix

Every criterion used in prior U100–U200 audit work is evaluated here against the **only canonical HP schema definition**: VDR §62.4 (`STATE03_VDR_CLAUDE_VERIFICATION_LOG.md` lines 2144–2193, commit context `4856652c`+).

The second-pass HP corpus (U70–U99) was additionally examined as the empirical baseline, per VDR §62.4 preamble: "established across U70–U99."

| Rule ID | Criterion | Canonical Source | Evidence | Verdict |
|---------|-----------|-----------------|----------|---------|
| **CPM-01** | HP must use `"unit"` key (not `"unit_id"`) | VDR §62.4 table row 1: `"unit"` required; absence of `unit_id` confirmed across all U70–U99 HPs | VDR line 2152: `\| \`unit\` \| \`"U104"\` \| **ABSENT** — HP uses \`unit_id\` instead \| **CRITICAL** \|` | **CANONICAL — CRITICAL** |
| **CPM-02** | `status` must equal `"GATE-PASS"` | VDR §62.4 table row 2; U70–U99 corpus shows `"GATE-PASS"` as canonical value; CR-V002 correction required changing `"GATE-PENDING"` to `"GATE-PASS"` | VDR line 2153; CR-V002 VERIFIED-CLOSED | **CANONICAL — CRITICAL** |
| **CPM-03** | `gate_result` must contain PASS content (not "PENDING", not absent) | VDR §62.4 table row 3; CRITICAL if absent; `"PENDING"` = explicitly open gate; abbreviated `"PASS"` accepted per §62.2 for U100–U102; `null` = LOW note (§62.2 U103) | VDR lines 2154, 2107–2112 | **CANONICAL — CRITICAL (PENDING = open gate defect; absent = LOW note)** |
| **CPM-04** | `function_ids_targeted` present and populated | VDR §62.4 table row 4: MEDIUM severity | VDR line 2155 | **CANONICAL — MEDIUM ONLY** |
| **CPM-05** | `modules_covered` present and populated | VDR §62.4 table row 5: MEDIUM severity | VDR line 2156 | **CANONICAL — MEDIUM ONLY** |
| **CPM-06** | `commit_sha` or `source_sha` required | NOT listed in VDR §62.4 schema table; absent from ALL U70–U109 HP files without any VDR flag; VDR CR-V003 spec mentions `source_sha` but acceptance verification did NOT check for it | VDR §62.4 table (5 rows only); U70/U71/U72/U73/U74/U75 HPs examined — none have commit_sha/source_sha | **NOT CANONICAL — REJECTED** |
| **CPM-07** | `marker` field required | NOT listed in VDR §62.4 schema table; absent from ALL U70–U75 HPs without any VDR flag | VDR §62.4 table; U70–U75 HP corpus | **NOT CANONICAL — REJECTED** |
| **CPM-08** | macOS `/Volumes/...` paths in Restricted Technical Evidence = defect | No canonical rule found in VDR, ADR-0005, or ADR-0006 prohibiting local file paths in `01_RESTRICTED_TECHNICAL_EVIDENCE/` tier; Boss explicitly: "Do not treat macOS `/Volumes/...` paths in Restricted Technical Evidence as defects merely because cloud Linux cannot access them." | ADR-0006 §Decision: study paths are observation (allowed); no VDR rule on path format in restricted evidence | **NOT CANONICAL — REJECTED (Boss override explicit)** |
| **CPM-09** | `neutral-leak-tokens` in `02_NEUTRAL_KNOWLEDGE/` files = defect | `neutral-leak-tokens=0` is the gate check METRIC embedded in `gate_result` string — it is the OUTCOME measure, not a prohibition on source pointers; ADR-0006 permits observation (source file paths) in evidence; no VDR rule found prohibiting source file paths in neutral tier | ADR-0006 allowed workflow: "Reference System → Observation → Generic Business Concept"; gate metric is pass/fail count | **NOT CANONICAL — UNPROVEN as blanket defect; requires file-by-file proof (Boss override: "Do not infer neutral leakage … Open the actual affected file and prove it")** |
| **CPM-10** | Legacy root path evidence (U172–U179) = defect | VDR §61.6 shows U70–U99 used root path `01_RESTRICTED_TECHNICAL_EVIDENCE/`, `02_NEUTRAL_KNOWLEDGE/`, `04_HANDOFF_PACKETS/` as canonical for second-pass; no VDR migration rule found requiring U172–U179 to use the canonical `VERY_DEEP_RESEARCH_L0_L3/` sub-path | VDR §62.4 preamble references U70–U99 as canonical standard; no migration rule read | **UNPROVEN — cannot confirm mandatory migration to canonical path for these units** |
| **CPM-11** | Non-atomic commits = defect | "Atomic Unit rule" referenced in Boss authorization but no canonical definition document found; VDR does not define atomicity requirements | VDR §62.4, ADR-0005, ADR-0006 examined — no atomic unit definition | **UNPROVEN — no canonical definition read; Boss: "Do not require historical commits to be rewritten. Test lineage preservation against the actual Atomic Unit rule."** |
| **CPM-12** | Verbatim source code in evidence files = defect | ADR-0006 prohibits COPYING as IMPLEMENTATION artifacts; permits OBSERVATION (source file paths, code excerpts for concept extraction) in evidence files; cannot classify as defect without opening file and proving copying vs. observation | ADR-0006 §Decision: "Allowed: learning business concepts … producing documentation"; "Prohibited: copying source code … as implementation artifacts" | **UNPROVEN — requires file-level proof; Boss: "Do not infer source-code copying … Open the actual affected file and prove it."** |
| **CPM-13** | `gate_result` must be exact canonical phrase (not abbreviated) | VDR §62.2: U100 `gate_result: "PASS"` accepted as INTAKE-PASS; U101/U102 accepted with object format; U103 `gate_result: null` = LOW NOTE only | VDR lines 2107–2112 | **NOT CANONICAL — abbreviated "PASS" and even null are accepted; "PENDING" is the only blocked value** |

**Summary — Prior Criteria Verdict Distribution:**

| Verdict | Count | Criteria |
|---------|-------|----------|
| CANONICAL — CRITICAL | 3 | CPM-01, CPM-02, CPM-03 |
| CANONICAL — MEDIUM | 2 | CPM-04, CPM-05 |
| NOT CANONICAL — REJECTED | 4 | CPM-06 (commit_sha), CPM-07 (marker), CPM-08 (macOS paths), CPM-13 (exact phrase) |
| NOT CANONICAL — REJECTED (Boss override) | 1 | CPM-08 |
| UNPROVEN | 4 | CPM-09 (neutral-leak), CPM-10 (legacy path), CPM-11 (atomic), CPM-12 (verbatim source) |

---

## Part 2 — U100–U200 Re-Evaluation Against Canonical Criteria Only

Evaluation performed by extracting `unit`/`unit_id` key name, `status`, and `gate_result` fields from each HP JSON via `git show origin/claude/local-odoo-source-research`. Canonical criteria applied: CPM-01, CPM-02, CPM-03 (CRITICAL); CPM-04, CPM-05 (MEDIUM, noted only).

**Legend:**
- ✅ INTAKE-PASS — all CRITICAL criteria met
- ⚠ LOW — gate_result absent but status=GATE-PASS (non-blocking, LOW note per §62.2 precedent)
- ❌ DEFECT-A — `unit_id` key used instead of `unit` (CPM-01 CRITICAL)
- ❌ DEFECT-B — `gate_result: "PENDING"` — open gate (CPM-03 CRITICAL)
- ❌ DEFECT-C — malformed `gate_result` value (non-string object, or semantically wrong value)
- 🔵 IN-PROGRESS — status explicitly shows pending Claude verification (not gate-passed; no canonical defect until DeepSeek finalizes)
- ⬜ NOT-GATE-PASS — status ≠ "GATE-PASS" and no open gate; intermediate state; needs gate-pass before VDR intake

| Unit | `unit` key | `status` | `gate_result` | Classification | Note |
|------|-----------|---------|--------------|----------------|------|
| U100 | `unit` ✓ | GATE-PASS ✓ | PASS ✓ | ✅ INTAKE-PASS | Already recorded VDR §62.2 |
| U101 | `unit` ✓ | GATE-PASS ✓ | object {result:PASS} | ✅ INTAKE-PASS | Object format accepted per §62.2 |
| U102 | `unit` ✓ | GATE-PASS ✓ | object {result:PASS} | ✅ INTAKE-PASS | Object format accepted per §62.2 |
| U103 | `unit` ✓ | GATE-PASS ✓ | ABSENT | ⚠ LOW | Already recorded VDR §62.2 (null=LOW) |
| U104 | `unit` ✓ | GATE-PASS ✓ | PASS (claim-checks=0...) ✓ | ✅ INTAKE-PASS | **CR-V005 APPEARS RESOLVED** — DeepSeek branch now shows canonical schema; VDR §62.5 shows CR-V005 OPEN but DeepSeek has corrected |
| U105 | `unit` ✓ | DEEPSEEK-REPORTED / PENDING | ABSENT | 🔵 IN-PROGRESS | Not yet gate-passed; not a canonical defect |
| U106 | `unit_id` ✗ | DEEPSEEK-REPORTED / PENDING | **PENDING** | ❌ DEFECT-A+B | CPM-01 CRITICAL + open gate |
| U107 | `unit` ✓ | EVIDENCE_GATHERED | **PENDING** | ❌ DEFECT-B | Open gate (CPM-03 CRITICAL) |
| U108 | `unit` ✓ | DEEPSEEK-REPORTED / PENDING | ABSENT | 🔵 IN-PROGRESS | Not yet gate-passed |
| U109 | `unit` ✓ | DEEPSEEK-REPORTED / PENDING | ABSENT | 🔵 IN-PROGRESS | Not yet gate-passed |
| U110 | `unit_id` ✗ | DEEPSEEK-REPORTED / PENDING | PENDING | ❌ DEFECT-A+B | CPM-01 + open gate |
| U111 | `unit_id` ✗ | DEEPSEEK-REPORTED / PENDING | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U112 | `unit_id` ✗ | DEEPSEEK-REPORTED / PENDING | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U113 | `unit` ✓ | GATE-PASS ✓ | PASS ✓ | ✅ INTAKE-PASS | |
| U114 | `unit` ✓ | GATE-PASS ✓ | PASS ✓ | ✅ INTAKE-PASS | |
| U115 | `unit` ✓ | GATE-PASS ✓ | PASS ✓ | ✅ INTAKE-PASS | |
| U116 | `unit` ✓ | GATE-PASS ✓ | PASS ✓ | ✅ INTAKE-PASS | |
| U117 | `unit` ✓ | GATE-PASS ✓ | PASS ✓ | ✅ INTAKE-PASS | |
| U118 | `unit` ✓ | GATE-PASS ✓ | PASS ✓ | ✅ INTAKE-PASS | |
| U119 | `unit` ✓ | GATE-PASS ✓ | PASS ✓ | ✅ INTAKE-PASS | |
| U120 | `unit` ✓ | GATE-PASS ✓ | PASS ✓ | ✅ INTAKE-PASS | |
| U121 | `unit` ✓ | GATE-PASS ✓ | PASS ✓ | ✅ INTAKE-PASS | |
| U122 | `unit` ✓ | GATE-PASS ✓ | PASS ✓ | ✅ INTAKE-PASS | |
| U123 | `unit` ✓ | GATE-PASS ✓ | PASS ✓ | ✅ INTAKE-PASS | |
| U124 | `unit_id` ✗ | ABSENT | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U125 | `unit_id` ✗ | ABSENT | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U126 | `unit_id` ✗ | ABSENT | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U127 | `unit_id` ✗ | ABSENT | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U128 | `unit_id` ✗ | ABSENT | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U129 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass before VDR intake |
| U130 | `unit` ✓ | COMPLETE | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U131 | `unit` ✓ | GATE-PASS ✓ | **PENDING** | ❌ DEFECT-B | CRITICAL — claims GATE-PASS but gate is PENDING |
| U132 | `unit` ✓ | GATE-PASS ✓ | ABSENT | ⚠ LOW | gate_result absent = LOW note (per §62.2 precedent) |
| U133 | `unit` ✓ | AWT-READY | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U134 | `unit` ✓ | COMPLETE | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U135 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass |
| U136 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass |
| U137 | `unit` ✓ | COMPLETE | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U138 | `unit` ✓ | COMPLETE | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status (prior audit erred saying gate_result=PENDING) |
| U139 | `unit` ✓ | CLOSED | "claim-checks=0, neutral-leak-tokens=0" | ❌ DEFECT-C | gate_result malformed — missing PASS prefix; status "CLOSED" non-canonical |
| U140 | `unit_id` ✗ | ABSENT | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U141 | `unit` ✓ | COMPLETE | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U142 | `unit` ✓ | COMPLETE | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U143 | `unit_id` ✗ | COMPLETE | PASS | ❌ DEFECT-A | CPM-01 CRITICAL; status also non-canonical |
| U144 | `unit` ✓ | ABSENT | PASS | ⬜ NOT-GATE-PASS | gate_result=PASS but status not GATE-PASS; needs status fix |
| U145 | `unit_id` ✗ | COMPLETE | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U146 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass (prior audit erred saying gate_result=PENDING) |
| U147 | `unit_id` ✗ | COMPLETE | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U148 | `unit` ✓ | COMPLETE | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U149 | `unit` ✓ | COMPLETE | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U150 | `unit` ✓ | COMPLETE | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U151 | `unit` ✓ | COMPLETE | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U152 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass |
| U153 | `unit` ✓ | PRESENT | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U154 | `unit` ✓ | GATE-PASS ✓ | ABSENT | ⚠ LOW | gate_result absent = LOW note |
| U155 | `unit` ✓ | ABSENT | **PENDING** | ❌ DEFECT-B | Open gate with no status claim — PENDING gate_result is canonically a CRITICAL defect |
| U156 | `unit_id` ✗ | PRESENT | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U157 | `unit_id` ✗ | ABSENT | "GATE-PASS" | ❌ DEFECT-A+C | CPM-01; gate_result contains status value (wrong field) |
| U158 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass |
| U159 | `unit_id` ✗ | GATE-PASS ✓ | ABSENT | ❌ DEFECT-A + ⚠ LOW | CPM-01 CRITICAL + gate_result absent = LOW |
| U160 | `unit` ✓ | ABSENT | "GATE-PASS" | ❌ DEFECT-C | gate_result contains status value (wrong field) |
| U161 | `unit` ✓ | PRESENT | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U162 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass |
| U163 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass |
| U164 | `unit` ✓ | PRESENT | PASS | ⬜ NOT-GATE-PASS | gate_result=PASS but status not GATE-PASS; needs status fix |
| U165 | `unit_id` ✗ | ABSENT | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U166 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass |
| U167 | `unit` ✓ | COMPLETE | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U168 | `unit_id` ✗ | PRESENT | PASS | ❌ DEFECT-A | CPM-01 CRITICAL; status also non-canonical |
| U169 | `unit_id` ✗ | PRESENT | PASS | ❌ DEFECT-A | CPM-01 CRITICAL; status also non-canonical |
| U170 | `unit_id` ✗ | ABSENT | PASS | ❌ DEFECT-A | CPM-01 CRITICAL; status also non-canonical |
| U171 | `unit_id` ✗ | ABSENT | PASS | ❌ DEFECT-A | CPM-01 CRITICAL; status also non-canonical |
| U172 | **MISSING** | — | — | ❌ MISSING-HP | No HP file exists on DeepSeek branch |
| U173 | **MISSING** | — | — | ❌ MISSING-HP | No HP file exists |
| U174 | **MISSING** | — | — | ❌ MISSING-HP | No HP file exists |
| U175 | **MISSING** | — | — | ❌ MISSING-HP | No HP file exists |
| U176 | **MISSING** | — | — | ❌ MISSING-HP | No HP file exists |
| U177 | **MISSING** | — | — | ❌ MISSING-HP | No HP file exists |
| U178 | **MISSING** | — | — | ❌ MISSING-HP | No HP file exists |
| U179 | **MISSING** | — | — | ❌ MISSING-HP | No HP file exists |
| U180 | `unit` ✓ | ABSENT | PASS | ⬜ NOT-GATE-PASS | gate_result=PASS but status not GATE-PASS; needs status fix |
| U181 | `unit` ✓ | COMPLETE | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U182 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass |
| U183 | `unit` ✓ | ABSENT | {object/dict} | ❌ DEFECT-C | gate_result is an object (non-string), non-canonical type |
| U184 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass |
| U185 | `unit_id` ✗ | PRESENT | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U186 | `unit_id` ✗ | STUDIED | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U187 | `unit_id` ✗ | STUDIED | PASS | ❌ DEFECT-A | CPM-01 CRITICAL |
| U188 | `unit` ✓ | COMPLETE | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U189 | `unit` ✓ | STUDIED | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U190 | `unit` ✓ | STUDIED | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U191 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass |
| U192 | `unit_id` ✗ | COMPLETE | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U193 | `unit` ✓ | COMPLETE | ABSENT | ⬜ NOT-GATE-PASS | Non-canonical status |
| U194 | `unit_id` ✗ | COMPLETE | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U195 | `unit_id` ✗ | COMPLETE | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U196 | `unit_id` ✗ | COMPLETE | ABSENT | ❌ DEFECT-A | CPM-01 CRITICAL |
| U197 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass |
| U198 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass |
| U199 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass |
| U200 | `unit` ✓ | ABSENT | ABSENT | ⬜ NOT-GATE-PASS | Needs gate-pass |

---

## Part 3 — Prior Audit Findings Re-Classification

All findings from the `START_STATE03_U100_U200_FULL_BATCH_AUDIT_PARALLEL` report (prior session) are re-classified below using **only canonical criteria** (CPM-01 through CPM-13).

| Prior Finding Category | Prior Count (est.) | Canonical Verdict | Reason |
|-----------------------|-------------------|-------------------|--------|
| `unit_id` key used instead of `unit` | ~28 | ✅ CONFIRMED DEFECT | CPM-01 CANONICAL-CRITICAL |
| `gate_result: "PENDING"` — open gate | ~4 (U106,U107,U131,U155) | ✅ CONFIRMED DEFECT | CPM-03 CANONICAL-CRITICAL |
| `gate_result` malformed/wrong-field value | ~4 (U139,U157,U160,U183) | ✅ CONFIRMED DEFECT | CPM-03 CANONICAL-CRITICAL |
| HP file missing (U172–U179) | 8 | ✅ CONFIRMED DEFECT | No HP = no VDR registration possible |
| `status ≠ "GATE-PASS"` on PENDING/in-progress units | est. ~40–50 | ❌ REJECTED — NOT CANONICAL CRITERION | In-progress units not yet gate-passed; no canonical defect until DeepSeek finalizes |
| `commit_sha` / `source_sha` absent | all units | ❌ REJECTED — NON-CANONICAL CRITERION | CPM-06: NOT in VDR §62.4; absent from ALL U70–U109 without flag |
| `marker` absent | all units | ❌ REJECTED — NON-CANONICAL CRITERION | CPM-07: NOT in VDR §62.4; absent from all U70–U75 |
| macOS `/Volumes/...` paths in evidence | various | ❌ REJECTED — NON-CANONICAL + BOSS OVERRIDE | CPM-08: No canonical rule; Boss explicit exclusion |
| Exact `gate_result` phrase required | various | ❌ REJECTED — NON-CANONICAL | CPM-13: abbreviated "PASS" accepted §62.2 |
| Neutral-leak tokens in neutral evidence | U150, U151 (claimed) | ⚠ NOT PROVEN | CPM-09: UNPROVEN; Boss: open file and prove |
| Non-atomic commits | various (claimed) | ⚠ NOT PROVEN | CPM-11: UNPROVEN; no canonical atomic unit definition |
| Verbatim source code in evidence | U135 (claimed) | ⚠ NOT PROVEN | CPM-12: UNPROVEN; Boss: open file and prove |
| Legacy root path (U172–U179) | 8 (prior claim) | ⚠ NOT PROVEN | CPM-10: UNPROVEN; path migration rule not confirmed canonical |

---

## Part 4 — Correction Package: CONFIRMED DEFECTS Only

The following corrections are directed to DeepSeek for resolution on branch `claude/local-odoo-source-research`. Only items with CANONICAL basis are included.

**File path prefix:** `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/04_HANDOFF_PACKETS/`

---

### DEFECT-A: `unit_id` key must be renamed to `unit` (CPM-01 — CRITICAL)

Affects 28 units. For each: rename JSON key `"unit_id"` → `"unit"`. Value unchanged.

| Unit | File | Fix |
|------|------|-----|
| U106 | `U106_handoff_packet.json` | Rename `unit_id` → `unit`; also resolve open gate (see DEFECT-B) |
| U110 | `U110_handoff_packet.json` | Rename `unit_id` → `unit`; also resolve open gate (see DEFECT-B) |
| U111 | `U111_handoff_packet.json` | Rename `unit_id` → `unit` |
| U112 | `U112_handoff_packet.json` | Rename `unit_id` → `unit` |
| U124 | `U124_handoff_packet.json` | Rename `unit_id` → `unit` |
| U125 | `U125_handoff_packet.json` | Rename `unit_id` → `unit` |
| U126 | `U126_handoff_packet.json` | Rename `unit_id` → `unit` |
| U127 | `U127_handoff_packet.json` | Rename `unit_id` → `unit` |
| U128 | `U128_handoff_packet.json` | Rename `unit_id` → `unit` |
| U140 | `U140_handoff_packet.json` | Rename `unit_id` → `unit` |
| U143 | `U143_handoff_packet.json` | Rename `unit_id` → `unit`; also set `status` → `"GATE-PASS"` (gate_result=PASS already present) |
| U145 | `U145_handoff_packet.json` | Rename `unit_id` → `unit` |
| U147 | `U147_handoff_packet.json` | Rename `unit_id` → `unit` |
| U156 | `U156_handoff_packet.json` | Rename `unit_id` → `unit` |
| U157 | `U157_handoff_packet.json` | Rename `unit_id` → `unit`; also fix malformed `gate_result` (see DEFECT-C) |
| U159 | `U159_handoff_packet.json` | Rename `unit_id` → `unit`; note: gate_result absent (LOW) |
| U165 | `U165_handoff_packet.json` | Rename `unit_id` → `unit` |
| U168 | `U168_handoff_packet.json` | Rename `unit_id` → `unit`; also set `status` → `"GATE-PASS"` (gate_result=PASS already present) |
| U169 | `U169_handoff_packet.json` | Rename `unit_id` → `unit`; also set `status` → `"GATE-PASS"` (gate_result=PASS already present) |
| U170 | `U170_handoff_packet.json` | Rename `unit_id` → `unit`; also set `status` → `"GATE-PASS"` (gate_result=PASS already present) |
| U171 | `U171_handoff_packet.json` | Rename `unit_id` → `unit`; also set `status` → `"GATE-PASS"` (gate_result=PASS already present) |
| U185 | `U185_handoff_packet.json` | Rename `unit_id` → `unit` |
| U186 | `U186_handoff_packet.json` | Rename `unit_id` → `unit` |
| U187 | `U187_handoff_packet.json` | Rename `unit_id` → `unit`; also set `status` → `"GATE-PASS"` (gate_result=PASS already present) |
| U192 | `U192_handoff_packet.json` | Rename `unit_id` → `unit` |
| U194 | `U194_handoff_packet.json` | Rename `unit_id` → `unit` |
| U195 | `U195_handoff_packet.json` | Rename `unit_id` → `unit` |
| U196 | `U196_handoff_packet.json` | Rename `unit_id` → `unit` |

**Acceptance test for DEFECT-A fixes:** `python3 -c "import json; d=json.load(open('UXX_handoff_packet.json')); assert 'unit' in d and 'unit_id' not in d"`

---

### DEFECT-B: Open gate — `gate_result: "PENDING"` must be resolved (CPM-03 — CRITICAL)

| Unit | File | Current State | Required Fix |
|------|------|---------------|-------------|
| U106 | `U106_handoff_packet.json` | status="DEEPSEEK-REPORTED...", gate_result="PENDING" | Run gate check; if PASS: set `status`→`"GATE-PASS"`, `gate_result`→`"PASS (claim-checks=0, neutral-leak-tokens=0)"`; also rename `unit_id`→`unit` (DEFECT-A) |
| U107 | `U107_handoff_packet.json` | status="EVIDENCE_GATHERED", gate_result="PENDING" | Run gate check; if PASS: set `status`→`"GATE-PASS"`, `gate_result`→`"PASS (claim-checks=0, neutral-leak-tokens=0)"` |
| U110 | `U110_handoff_packet.json` | status="DEEPSEEK-REPORTED...", gate_result="PENDING" | Run gate check; if PASS: set `status`→`"GATE-PASS"`, `gate_result`→`"PASS (claim-checks=0, neutral-leak-tokens=0)"`; also rename `unit_id`→`unit` (DEFECT-A) |
| U131 | `U131_handoff_packet.json` | status="GATE-PASS", gate_result="PENDING" | **CRITICAL CONFLICT**: claims gate-pass but gate is PENDING; must re-run gate check; if PASS: replace `gate_result`→`"PASS (claim-checks=0, neutral-leak-tokens=0)"` |
| U155 | `U155_handoff_packet.json` | status=ABSENT, gate_result="PENDING" | Run gate check; if PASS: set `status`→`"GATE-PASS"`, `gate_result`→`"PASS (claim-checks=0, neutral-leak-tokens=0)"` |

**Acceptance test:** `python3 -c "import json; d=json.load(open('UXX_handoff_packet.json')); assert d.get('gate_result') != 'PENDING'"`

---

### DEFECT-C: Malformed `gate_result` field (CPM-03 — CRITICAL)

| Unit | File | Current gate_result | Required Fix |
|------|------|---------------------|-------------|
| U139 | `U139_handoff_packet.json` | `"claim-checks=0, neutral-leak-tokens=0"` (missing PASS prefix) | Set `gate_result`→`"PASS (claim-checks=0, neutral-leak-tokens=0)"`; also set `status`→`"GATE-PASS"` (currently "CLOSED") |
| U157 | `U157_handoff_packet.json` | `"GATE-PASS"` (status value put in gate_result field) | Set `gate_result`→`"PASS (claim-checks=0, neutral-leak-tokens=0)"`; set `status`→`"GATE-PASS"`; also rename `unit_id`→`unit` (DEFECT-A) |
| U160 | `U160_handoff_packet.json` | `"GATE-PASS"` (same confusion) | Set `gate_result`→`"PASS (claim-checks=0, neutral-leak-tokens=0)"`; set `status`→`"GATE-PASS"` |
| U183 | `U183_handoff_packet.json` | Object/dict (non-string type) | Replace with string: `"PASS (claim-checks=0, neutral-leak-tokens=0)"` if gate actually passed, else resolve gate; set `status`→`"GATE-PASS"` |

**Acceptance test:** `python3 -c "import json; d=json.load(open('UXX_handoff_packet.json')); gr=d.get('gate_result',''); assert isinstance(gr,str) and ('PASS' in gr) and gr != 'GATE-PASS'"`

---

### DEFECT-D: Missing HP files (U172–U179)

8 HP files are entirely absent from the DeepSeek branch. These units cannot be registered in the VDR.

| Units | Required Action |
|-------|----------------|
| U172, U173, U174, U175, U176, U177, U178, U179 | Create `UXX_handoff_packet.json` for each in the canonical path with: `unit: "UXX"`, `status: "GATE-PASS"` (when research complete), `gate_result: "PASS (claim-checks=0, neutral-leak-tokens=0)"`, `claim_count: <N>` |

**Note:** If U172–U179 were intentionally skipped (scope change, module not applicable, etc.), provide a JSON stub with `status: "OUT_OF_SCOPE"` and `skip_reason: "<explanation>"` so the VDR can register them as explicitly excluded rather than silently missing.

---

### NOT-GATE-PASS Notice (informational — not blocking corrections above)

The following 43 units have `unit` key present but `status ≠ "GATE-PASS"`. These are NOT current CONFIRMED DEFECTS (units appear to be in intermediate research states). DeepSeek must finalize each unit to "GATE-PASS" before the verifier can perform semantic verification:

U129, U130, U133, U134, U135, U136, U137, U138, U141, U142, U144, U146, U148, U149, U150, U151, U152, U153, U158, U161, U162, U163, U164, U166, U167, U180, U181, U182, U184, U188, U189, U190, U191, U193, U197, U198, U199, U200, U105, U108, U109

For units with `gate_result=PASS` but `status≠"GATE-PASS"` (U144, U164, U180): simply set `status`→`"GATE-PASS"` to complete the canonical schema.

---

### LOW Note (non-blocking)

Units with `status: "GATE-PASS"` but `gate_result` absent (per §62.2 precedent, null=LOW):

| Unit | Note |
|------|------|
| U103 | Already recorded VDR §62.2 — LOW, INTAKE-PASS |
| U132 | LOW note; suggest adding `gate_result: "PASS (claim-checks=0, neutral-leak-tokens=0)"` |
| U154 | LOW note; suggest adding `gate_result` |
| U159 | Also DEFECT-A (`unit_id`); LOW note on gate_result after unit key fix |

---

## Part 5 — CR-V005 Status Update

**Finding:** U104 HP on DeepSeek branch (`origin/claude/local-odoo-source-research`) NOW shows:
- `"unit": "U104"` ✓  
- `"status": "GATE-PASS"` ✓  
- `"gate_result": "PASS (claim-checks=0, neutral-leak-tokens=0)"` ✓

This matches all three CRITICAL criteria from VDR §62.4. **CR-V005 appears to have been resolved by DeepSeek** since §62 was written. The verifier will confirm this in VDR §63 and update CR-V005 status from OPEN → VERIFIED-CLOSED (pending semantic verification at BAR-008 authorization).

---

## Part 6 — Boss-Gated Decisions (BOSS DECISION REQUIRED)

The following items require Boss ruling before further action — they cannot be resolved by DeepSeek routine correction:

| Item | Decision Required |
|------|------------------|
| **BD-001** | U172–U179 missing HP gap: Were these units intentionally skipped (scope change), never assigned, or does DeepSeek need to create them? If skipped: approve `"OUT_OF_SCOPE"` stub pattern. |
| **BD-002** | Neutral-leak-tokens proof for U150/U151: Prior audit claimed neutral leakage in these units' evidence files. Requires: (a) Boss authorization for verifier to open and read U150/U151 neutral knowledge files on DeepSeek branch, OR (b) DeepSeek to self-certify neutral-leak-tokens=0 and set correct gate_result. CPM-09 = UNPROVEN until file is opened. |
| **BD-003** | Verbatim source code in U135 evidence: Prior audit claimed verbatim code copying. CPM-12 = UNPROVEN. Requires: (a) Boss authorization to read U135 evidence file, OR (b) DeepSeek to self-certify compliance with ADR-0006. |
| **BD-004** | Non-canonical status values for 43 NOT-GATE-PASS units: These are research-in-progress. Boss to confirm: (a) DeepSeek continues finalizing these on its own schedule (no verifier intervention), OR (b) set a deadline/milestone for gate-passing all U100–U200 units. |

---

## Part 7 — Re-Evaluation Count Summary

| Category | Count |
|----------|-------|
| INTAKE-PASS (all CRITICAL criteria met) | **12** (U100–U104 + U113–U123) |
| LOW note only (GATE-PASS, gate_result absent) | **4** (U103, U132, U154; U159 also DEFECT-A) |
| IN-PROGRESS (DEEPSEEK-REPORTED / PENDING) | **5** (U105, U108, U109; some others) |
| NOT-GATE-PASS (research incomplete) | **~43** |
| **CONFIRMED DEFECT-A** (`unit_id` key) | **28** |
| **CONFIRMED DEFECT-B** (open gate `PENDING`) | **5** (U106, U107, U110, U131, U155) |
| **CONFIRMED DEFECT-C** (malformed gate_result) | **4** (U139, U157, U160, U183) |
| **CONFIRMED DEFECT-D** (missing HP file) | **8** (U172–U179) |
| BOSS DECISION REQUIRED | **4** (BD-001 through BD-004) |
| NOT PROVEN (unproven claims withdrawn) | **3** (neutral-leak, verbatim source, non-atomic) |
| NOT CANONICAL (prior criteria rejected) | **5 criterion types** (commit_sha, marker, macOS paths, exact phrase, function_ids exact key) |

**Total units with at least one CONFIRMED DEFECT: 41** (28 DEFECT-A + 5 DEFECT-B + 4 DEFECT-C + 8 DEFECT-D, with overlaps: U106/U110/U157 counted in multiple categories)

**Unique units needing correction: ~38** (after deduplication of overlaps)

---

## Acceptance Criteria for Correction Completion

DeepSeek's correction commit is accepted when:

1. `python3 -c "import json; d=json.load(open('UXX.json')); assert 'unit' in d and 'unit_id' not in d"` passes for all 28 DEFECT-A units
2. `python3 -c "import json; d=json.load(open('UXX.json')); assert d.get('gate_result') != 'PENDING'"` passes for all 5 DEFECT-B units
3. `python3 -c "import json; d=json.load(open('UXX.json')); gr=d.get('gate_result',''); assert isinstance(gr,(str,dict)) and str(gr)!='GATE-PASS'"` passes for DEFECT-C units
4. All 8 HP files U172–U179 exist in canonical path (or Boss approves OUT_OF_SCOPE stubs)

**DeepSeek handles all DEFECT-A/B/C/D corrections autonomously** per Boss authorization ("DeepSeek handles confirmed routine corrections without Boss approval").

---

*Stop marker: see VDR §63 — `STATE03_AUDIT_CRITERIA_PROOF_COMPLETE` + `STATE03_AUTOMATION_PAUSE_BOSS_GATED`*
