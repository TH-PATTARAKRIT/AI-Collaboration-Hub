# SMEPLUS-L99 GitHub Update — Conflict & Folder Reuse Report

Document ID: SMEPLUS-AIOS-L99-CONFLICT-001
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Branch inspected: SMEsPlus (read-only clone, depth 1)
Target path requested: 99_SMEsPlus_Enterprise_Suite/
Prepared by: Claude Code AI (Engineering Execution AI role)
Status: HOLD — Boss decision required before any write action

---

## 1. Method
Repository was cloned read-only (`git clone --depth 1 --branch SMEsPlus`) to inspect
the real tree before proposing or creating any folder, per the AI Repository Contract
Mandatory Rule ("AI must not guess repository, folder, file name, reviewer, or
approval path"). No write credentials (PAT) are configured in this environment, so
no branch, commit, or Pull Request was created. This report is the required
Pre-Check output the L99 command calls for.

## 2. Key finding: an approved canonical registry already exists
`99_SMEsPlus_Enterprise_Suite/SMEPLUS_REGISTRY.yaml` (status: approved) already
defines the canonical folder registry for this exact path, using a numbered scheme
(00_Project_Governance, 01_AI_Handoff, 02_Functional_Design, 03_Architecture_Decisions,
04_Review_Gates, 05_Prompts, 06_Templates, 07_Output_From_AI, 08_Testing_Evidence,
09_Security_Clean_Room, 11_Diagrams, 12_Traceability, 12_State_AI_Execution_Control,
13_Jira_Control, 14_Claude_Execution, 15_ChatGPT_Review, 16_Learning_Analysis,
17_Functional_Specification_Factory). This registry is mirrored by `99_.../README.md`
and by a separate but similarly-named registry at repo root
(`repository-contract/FOLDER_REGISTRY.yaml`, for the root `docs/` tree — a different,
parallel scaffold).

The L99 command's proposed folder set (Functional_Specification/, Functional_Design/,
FDS_Factory/, AI_Governance/, Governance/, Traceability/, Evidence_Register/,
Review_Pack/, docs/, .claude/skills/) does **not** match this approved registry's
naming convention. Creating it as specified would add a second, differently-named
scaffold on top of the one already approved — the same class of problem already on
record for this repository (nine self-nested duplicate folders, a duplicate
functional-design folder tree, competing FDS Requirement Catalog files).

## 3. Folder Reuse Result

| Requested folder | Exists as-named? | Nearest existing canonical folder | Action recommended |
|---|---|---|---|
| Functional_Specification/ | No | `17_Functional_Specification_Factory/` | Reuse existing; do not create new name |
| Functional_Design/ | No | `02_Functional_Design/` (canonical per registry) | Reuse existing |
| FDS_Factory/ | No | `17_Functional_Specification_Factory/` (already serves this exact purpose, has README, standards, module content) | Reuse existing; do not create parallel "FDS_Factory" |
| AI_Governance/ | No | `00_Project_Governance/`, plus `00_Architecture_Office/Governance/` subfolder | Do not create third governance-named folder; place Claude Skills docs under `00_Project_Governance/` as a subfolder, pending Boss confirmation |
| Governance/ | No (as standalone) | same as above | Same as above |
| Traceability/ | No | `12_Traceability/` (canonical) | Reuse existing |
| Evidence_Register/ | No | `12_State_AI_Execution_Control/templates/STATE_XX_EVIDENCE_REGISTER.md` (template file, not a folder) | GAP — needs Boss/PMO decision on whether this becomes a subfolder under `12_State_AI_Execution_Control/` |
| Review_Pack/ | No | `04_Review_Gates/` (canonical) | Reuse existing as parent; add subfolder only with sign-off |
| docs/ | Exists, but at **repository root**, not inside `99_SMEsPlus_Enterprise_Suite/` | `docs/` root tree is a separate, parallel scaffold (own README, own folder registry, own document registry) | Flag: two parallel governance scaffolds already coexist (root `docs/` vs `99_SMEsPlus_Enterprise_Suite/00-17`). Do not add a third |
| .claude/skills/ | Not found anywhere in the repository (root or nested) | — | Genuine gap. Location (repo root vs nested inside `99_SMEsPlus_Enterprise_Suite/`) must be confirmed by Boss before creation, exactly as the L99 command itself requires |

## 4. Pre-existing structural issues re-confirmed during this check
These were already known and are unrelated to this task, but are re-surfaced because
adding new content on top of them would compound the problem:
- `02_Functional_Design/02_Functional_Design/` and `02_Functional_Design/02_Functional_Design_v2/` — self-nested duplicates
- `04_Review_Gates/04_Review_Gates/` — self-nested duplicate
- `05_Prompts/05_Prompts/` — self-nested duplicate
- `12_Traceability/Requirement_Matrix/12_Traceability/Requirement_Matrix/` — self-nested duplicate, three levels deep

## 5. Conflict Type Summary
- **Type:** Naming-scheme conflict (approved registry vs. ad-hoc L99 proposal) + risk of
  compounding existing duplicate-folder issues.
- **Severity:** Medium-High — not a data-loss risk (no overwrite proposed), but a
  governance/traceability risk: creating `FDS_Factory/`, `AI_Governance/`, `Governance/`,
  `Evidence_Register/`, `Review_Pack/` as new top-level folders would violate the
  "Folder Registry" approval requirement (`SMEPLUS_REGISTRY.yaml`, status: approved)
  and the Constitution's evidence/traceability rules, since these names are not
  registered.
- **Manual approval required:** Yes — per Repository Contract Mandatory Rule and
  Constitution Authority Rule, Boss approval is required before any new top-level
  folder is registered.

## 6. Recommended path forward (no action taken yet)
1. Boss confirms whether the FDS Factory pipeline content should live inside the
   existing `17_Functional_Specification_Factory/` folder (recommended — avoids a
   duplicate), or whether a genuinely new top-level folder is intended and should be
   added to `SMEPLUS_REGISTRY.yaml` first.
2. Boss confirms whether `.claude/skills/` should sit at repository root or nested
   under `99_SMEsPlus_Enterprise_Suite/`.
3. Once confirmed, content can be drafted directly into the correct, registered path.
4. Separately: this environment has no GitHub write credentials (PAT) configured, so
   branch creation / commit / Pull Request cannot be executed here. Output will need
   to be delivered as a file package for manual upload, or write access will need to
   be enabled, consistent with prior working pattern for this project.
