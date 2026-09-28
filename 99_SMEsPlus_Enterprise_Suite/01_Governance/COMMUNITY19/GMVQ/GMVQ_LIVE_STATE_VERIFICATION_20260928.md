# GMVQ Live State Verification — 2026-09-28

## CANONICAL vs CANDIDATE

**Every count below is labeled CANONICAL or CANDIDATE.** CANONICAL means present on branch
`SMEsPlus` (or merged from it). CANDIDATE means present only in an unmerged pull request
(`#71` closed/not-merged, `#73` open/draft) — admissible as evidence-of-artifact-existence
only, never as roster admission, A1 admission, canonical G-group scope membership, or
progress toward completion. Per `MASTER_DECISION_LOG_G01_20260927.md` MD-20: "NOT FOUND ON
THIS BRANCH ≠ NOT FOUND IN THE PROJECT" — but the reverse discipline holds equally: found in
PR#71/#73 ≠ canonical, admitted, or counted.

This document supersedes no MASTER Decision Log entry; it adds a fresh, evidence-only
inventory pass. It is not Boss Final Approval and not a Formal Coverage statement.

---

## 1. CANONICAL GMVQ tree (`origin/SMEsPlus`)

Path: `99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/GMVQ/`

Total files under `GMVQ/`: **68**, of which **63** are under `GMVQ/G01_PLATFORM_BASE/`.

**Confirmed: `G01_PLATFORM_BASE/` is the only bank/module folder under `GMVQ/` on `SMEsPlus`.**
No `G02`–`G16` folder exists under canonical `GMVQ/`.

### GMVQ/ root-level files (non-G01), 5 files

- `GMVQ_BOSS_OVERNIGHT_G01_G16_AUTHORING_ORDER_20260924.md`
- `GMVQ_BOSS_STANDING_EXECUTION_AUTHORIZATION_20260922.md`
- `GROUP_STRUCTURE_V2_CORE_CANDIDATE_20260928.tsv`
- `GROUP_STRUCTURE_V2_CORE_CANDIDATE_20260928_README.md`
- `OVQDT_G02_G16_ROSTER_HOLD_20260925_1521.md`

### GMVQ/G01_PLATFORM_BASE/ contents, 63 files

Includes: 12 `FREEZE_W1-B01..B11.json` + `FREEZE_W1-STD.json` (+1 sha256 sidecar), 22
per-module `G01_*_GMVQ_MVQ_*_V1.00_DRAFT.md` module-specific question banks (auth_signup,
base_automation, base, base_setup, base_sparse_field, bus, digest, google_recaptcha,
html_builder, html_editor, http_routing, mail, onboarding, phone_validation, portal,
privacy_lookup, utm, web, web_tour), the standard question set
`QUESTION_BANK_STANDARD_55_V2.00.md`, `question_bank_lint.py`, `freeze_batch.py`, two SHA256
manifests, 6 `OVQDT_G01_STATUS_*.md` files, 7 `W1_B0*_OVQDT_REVIEW_*.md` / sha256 pairs,
`W1_FREEZE_VERIFICATION_20260922.md`, `W1_ROLLING_FREEZE_STATUS_20260922.md`, and
`QUESTION_GATE_G01_FREEZE_REPLAY_20260927.md`.

### Adjacent (sibling folder, not under `GMVQ/` itself), CANONICAL

`99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/LANE_A_CONTROL/`:
- `GMVQ_EVIDENCE_SOURCE_REGISTRY.tsv`
- `GMVQ_LANE_A_EVIDENCE_BRIDGE.md`

---

## 2. G01's actual canonical bank content

### `QUESTION_BANK_STANDARD_55_V2.00.md`

This file is **the common Standard question set ("ROOM A")**, not a per-module answer bank.
Counted directly from the file: it contains exactly **55** questions, `STD-Q01` through
`STD-Q55`, each appearing exactly once (verified: 55 `**STD-Q\d\d —` headers, 55 unique IDs).
No `V1.05` string appears anywhere in this file.

Header-declared facts (read verbatim, not estimated):
- Version: **V2.00** — supersedes `QUESTION_BANK_STANDARD_35_V1.00`
- Date: 2026-09-22
- Status: `PREPARED ONLY / READY FOR FREEZE`
- Combined floor per module: **≥95** (55 standard + ≥40 module-specific)
- Declared total module count in this document: **247**
- Declared workload at this floor: **247 × 95 = 23,465 answers per lane**
- Declared total questions to author (once, reused across all 247 modules): **9,880**
- Explicit statement: "Formal Coverage remains **NOT AUTHORIZED** until a Canonical
  Function-ID denominator is Boss-frozen." Also: "No Formal Coverage figure is claimed or
  authorized."

This is the one place in the canonical tree where a module-count figure (247) and a
question-count figure (9,880 to author / 23,465 answers per lane) are stated in writing —
but these are **declared workload targets under the Standard 55 floor definition, not a
count of modules that currently have banks, and not a count of questions currently answered**.
They must not be conflated with "≈170/247 modules with question banks" or "≈8,065 total
questions" — neither of those figures appears in this file or anywhere else located in this
pass.

### `question_bank_lint.py`

Read directly (100 lines). It:
- Parses `\`\`\`yaml` blocks for module-specific questions, requiring fields `QID, MODULE,
  TYPE, AUTHOR, RISK_TIER, OUTPUT_CLASS, HYPOTHESIS, WHY_IT_MATTERS,
  DISCONFIRMING_OBSERVATION, EXPECTED_SURFACE, PRECONDITIONS`; rejects `TYPE != MODULE` and
  empty `DISCONFIRMING_OBSERVATION`.
- Parses the Standard bank via `STD-Q\d\d —` headers, requires exactly 55 unique
  `STD-Q01`..`STD-Q55` and a `DISCONFIRM:` in every question block.
- Enforces a module-specific floor of **40** questions per module (`c < 40` fails), and
  flags duplicate QIDs and `MODULE` values not in the allow-list passed via `--modules`.
- On success prints `QUESTION BANK LINT: PASS` plus file/standard/module-specific/unique-QID
  counts.
- **No version number is printed or declared anywhere in this script.** There is no `V1.05`
  string in it. The `V1.05`/`question_bank_lint_v1_01.py` name found in this pass belongs to
  a **different, CANDIDATE-only** script referenced inside PR#71 documents (see §3) — not
  this canonical `question_bank_lint.py`.

---

## 3. PR#71 full candidate inventory — CANDIDATE ONLY, UNMERGED, NOT ADMITTED

Source: `pull_request_read(get_files)`, `TH-PATTARAKRIT/AI-Collaboration-Hub#71`, paginated
perPage=100 across page 1 (100 files) and page 2 (56 files). **Confirmed total: 156 files**
(matches the file count previously cited for this PR; verified directly, not assumed).

All 156 files live under one root:
`99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/GMVQ_CANDIDATE_ROSTER_NOT_VERIFIED/`
— a path that is **not** `GMVQ/` and carries its own `NOT_VERIFIED` label in the folder name.

Of the 156 files: **147** match the bank-file pattern `*_GMVQ_MVQ_*` (module question banks);
**9** are registers/README/audit files, not bank files.

### Candidate bank-file count per G-group folder (CANDIDATE, UNMERGED — none admitted)

| G-group folder | Candidate bank files (count) |
|---|---|
| G02_IDENTITY_ACCESS | 11 |
| G03_MASTER_DATA | 11 |
| G04_ACCOUNT_BASE | 9 |
| G05_INVENTORY | 14 |
| G06_MANUFACTURING | 12 |
| G07_PURCHASE | 9 |
| G08_SALES | 34 |
| G09_CRM | 8 |
| G11_EVENTS | 8 |
| G12_PROJECT | 20 |
| G15_PRODUCTIVITY | 11 |
| **Total (candidate bank files)** | **147** |

Non-bank files (9): `00_CANDIDATE_STATUS_README.md`, `00_INGEST_REGISTER.tsv`,
`00_REGISTERS_AND_AUDIT/31_ROSTER_RECONCILIATION_LANE_A_G02_G03_G04_G06_G07_G11_SMEPLUS-26-09-27.md`,
`00_REGISTERS_AND_AUDIT/G05_G06_INDEP_AUDIT_DEFECT_QUEUE.tsv`,
`00_REGISTERS_AND_AUDIT/G07_G08_INDEP_AUDIT_DEFECT_QUEUE.tsv`,
`00_REGISTERS_AND_AUDIT/G09_G11_INDEP_AUDIT_DEFECT_QUEUE.tsv`,
`00_REGISTERS_AND_AUDIT/G09_G11_INDEP_AUDIT_RECORD.md`,
`00_REGISTERS_AND_AUDIT/GROUP_BRIEF_G12_PROJECT.md`,
`00_REGISTERS_AND_AUDIT/GROUP_BRIEF_G15_PRODUCTIVITY.md`.

### Specific-token search across all 156 PR#71 files (filenames + full patch text) — exact findings, not inferred

- **`certificate`** — FOUND, but only as an ordinary English word inside the
  `G02_AUTH_LDAP_GMVQ_MVQ_48_V1.00_DRAFT.md` candidate question content ("a trust or
  certificate validation failure between the system and the external directory service...").
  **No file, module, or bank named `certificate` exists anywhere in PR#71.** There is no
  "`certificate` module GMVQ bank" in this candidate set.
- **`W2`** — FOUND, but as a **wave label** (`Wave: W2`), used as the authoring-batch tag on
  roughly 20+ G08/G09 candidate bank files (parallel to `Wave: W1` used elsewhere in the same
  PR), and once as a citation ("W2/G09/G11 audit record") inside the Lane A roster
  reconciliation doc. **No "audit backlog" concept, and no count of 4,000 or any other
  number attached to `W2`, appears anywhere.** "4,000+ W2 audit backlog" is NOT FOUND.
- **`100CELL`** — NOT FOUND. No filename or text match anywhere in PR#71 or PR#73.
- **`WAVE_G12_G15_PRODUCTION_AND_AUDIT`** — NOT FOUND as a filename or text string. (Plain
  "Wave" appears only as the W1/W2 authoring-batch label described above; two `GROUP_BRIEF_*`
  files reference "Wave 3, 20 modules" for G12 and "Wave 4, 11 modules" for G15 in prose, but
  no file named `GMVQ_WAVE_G12_G15_PRODUCTION_AND_AUDIT` exists.)
- **`V1.05`** — FOUND, twice, but attached to a **different, candidate-only tool**:
  "`03_TOOLS/question_bank_lint_v1_01.py` V1.05 per-group" and "Validator V1.05 re-run: 0
  field/format/vocabulary errors..." inside PR#71's own audit-record prose (G07 purchase
  register). This is **not** the canonical `question_bank_lint.py` on `SMEsPlus` (§2), which
  has no version string at all. `V1.05` as applied to *the canonical* lint tool is NOT FOUND.
- **`QSHA`** — NOT FOUND. No match anywhere in PR#71 or PR#73 (filenames or patch text).
- **`project_hr_skills`** — FOUND as one filename:
  `G12_PROJECT/G12_PROJECT_HR_SKILLS_GMVQ_MVQ_50_V1.00_DRAFT.md` (candidate question bank,
  module metadata `project_hr_skills`). This is a candidate bank file name only; it says
  nothing about the real Odoo module's license (see §5).

---

## 4. PR#73 content — verified directly

Source: `pull_request_read(get_files)`, `#73`, page 1, perPage=100. **Confirmed: exactly 2
files**, both added, both under
`99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/GMVQ/RECONCILIATION/`:

1. `GMVQ_ROSTER_RECONCILIATION_PASS1_20260928.md` (42 lines)
2. `GMVQ_ROSTER_RECONCILIATION_PASS1_20260928.tsv` (18 lines, 17 data rows)

Confirmed content (read in full, not summarized from title): it reconciles the merged
`GROUP_STRUCTURE_V2_CORE_CANDIDATE_20260928.tsv` roster against **existing GMVQ question-bank
artifacts** (i.e., PR#71's candidate banks). Stated result: 17 named non-G01 roster rows;
question banks found for all 17; 9 rows `MATCH_CONFIRMED` (G03 product/uom/analytic, G05
stock, G06 mrp, G07 purchase, G08 sale, G09 crm, G12 project); 8 rows `MATCH_DERIVED` (G11
event family). The document itself states explicitly: "This pass removes 'question bank
absent' as a blocker for the 17 named rows. It does not remove the roster-governance blocker
for unresolved GAP rows, and it does not self-authorize Freeze, Formal Coverage, or Final
Approval." **This confirms the "roster reconciliation pass 1, 2 files" description as
accurate** — it was verified directly, not taken on faith.

---

## 5. `certificate` and `project_hr_skills` — license/edition findings from primary Odoo source

Fetched directly at the pinned anchor (`odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`),
per MD-07's evidence-admissibility rule:

- `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/certificate/__manifest__.py`
  → **HTTP 200.** Manifest found at `addons/certificate/` (the Community addons tree, not an
  `enterprise/` path). Declared `'license': 'LGPL-3'`. Name: "Certificate", category
  "Hidden/Tools", depends on `base_setup`.
- `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/project_hr_skills/__manifest__.py`
  → **HTTP 200.** Manifest found at `addons/project_hr_skills/` (Community addons tree).
  Declared `'license': 'LGPL-3'`. Name: "Project - Skills", depends on `['project',
  'hr_skills']`, `auto_install: True`.

**Both modules exist in the Community (`addons/`) tree at the pinned anchor and both declare
`LGPL-3`, not an OEEL-1/Enterprise license.** Neither manifest's `license` field says OEEL-1,
and neither module required a lookup under an `enterprise/` path — they were found on the
first attempt at `addons/`. This directly contradicts any prior claim that either module is
Enterprise-only; that claim is unverified and appears incorrect on this evidence.

**Governance note, stated explicitly per the task's requirement:** the existence of a
candidate GMVQ bank filename such as `G12_PROJECT_HR_SKILLS_GMVQ_MVQ_50_V1.00_DRAFT.md` in
unmerged PR#71 is evidence that a candidate document was authored under that name — it is
**not** evidence of canonical G-group scope membership, canonical roster admission, or
license status. License status can only be established from the primary Odoo source, as
done above.

---

## 6. Cross-module identity / frozen-state check

`GMVQ/G01_PLATFORM_BASE/QUESTION_BANK_STANDARD_55_V2.00.md`'s own header states:

- `Status: PREPARED ONLY / READY FOR FREEZE` — **not yet frozen** as of the document's own
  declaration (dated 2026-09-22).
- No hash/checksum of the bank itself is declared in the header (separate SHA256 manifest
  files exist alongside it in the same folder — `GMVQ_W1_SHA256_MANIFEST_20260922.txt` and
  `..._R2.txt` — but these are freeze/lineage artifacts for the Wave-1 batch files, not a
  hash embedded in this document's own header).
- The one genuinely declared, written figure that functions as a frozen input (not a
  completion count) is: **247** total modules in scope, **≥95** combined-floor questions per
  module (55 standard + ≥40 module-specific), **9,880** total questions to author once across
  all 247 modules, **23,465** total answers at full floor across all lanes. This is a
  **target/floor definition Boss decided on 2026-09-22 ("Option B")**, not a count of modules
  currently banked or questions currently answered.

---

## 7. UNVERIFIED / SOURCE NOT LOCATED

The following claims from the original directive were searched for directly in `SMEsPlus`,
PR#71, and PR#73 in this pass. None was found as stated:

| Claim | Finding |
|---|---|
| `≈170/247 modules with question banks` | Not found in `SMEsPlus`, PR#71, or PR#73. The only "247" found is the Standard-55 document's declared total scope/floor target (§2, §6), not a count of modules currently holding banks. |
| `≈8,065 total questions` | Not found in `SMEsPlus`, PR#71, or PR#73. The only question-count figures found are: G01 Standard bank = 55 questions (counted directly, §2); the Standard-55 document's own declared target of 9,880 questions to author across all 247 modules (a target, not a current total, §2/§6). |
| `4,000+ W2 audit backlog` | Not found. `W2` exists only as a wave/authoring-batch label in PR#71 candidate files (§3); no backlog count of any size is attached to it anywhere. |
| `V1.05 lint` (as the canonical tool) | Not found on the canonical `question_bank_lint.py` (§2), which carries no version string. A `V1.05` reference does exist, but only inside PR#71 candidate prose, attached to a different, candidate-only script `question_bank_lint_v1_01.py` (§3). |
| `QSHA governance state` | Not found. No match for `QSHA` anywhere in `SMEsPlus` GMVQ tree, PR#71, or PR#73. |
| `GMVQ_100CELL_UTILIZATION_MASTER` | Not found. No such filename, and no `100CELL` text match, anywhere in `SMEsPlus`, PR#71, or PR#73. |
| `GMVQ_WAVE_G12_G15_PRODUCTION_AND_AUDIT` | Not found. No such filename exists; only unrelated "Wave 3"/"Wave 4" prose labels inside two PR#71 `GROUP_BRIEF_*` files (§3). |
| A `certificate` module GMVQ bank | Not found. No bank file named for a `certificate` module exists in `SMEsPlus` or PR#71; the word appears only inside unrelated question text (§3). |

---

## Formal Coverage = NOT AUTHORIZED

Nothing in this inventory changes that status. No Canonical Function-ID denominator has been
Boss-frozen; no percentage-complete figure is claimed or implied anywhere in this document.
This is a raw, verified, evidence-only inventory — canonical counts and candidate counts kept
strictly separate throughout, per governance discipline MD-07/08/17/20.
