# 49 — P02 AAS-03 ROUND-3 CHALLENGE RECORD

`LAYER 2 — AUDIT QUARANTINE.` **CP-07.** Prompt §12. Baseline `aca211e`.

Four fresh experts, run **against this round's new material only** (`44`–`47`), each with a mandatory
falsification assignment. **No expert issued PASS/FAIL for the process.**

---

## 1. Assignment Coverage — All Four §12 Mandates Discharged

| §12 mandate | Expert | Discharged how |
|---|---|---|
| ≥1 must actively attempt to **disprove the Evidence Identity Model** | **2** | Attacked the composite key from both directions; **disproved it** (`C-63`/`C-64`) |
| ≥1 must attack the **population denominator method**, not its findings | **2** | Attacked coverage, units, formats; **broke the coverage assertion** (`C-67`) |
| ≥1 must attack **C-04 closure logic and the mutation boundary** | **4** | **Found the safety defect** (`C-74`) and the conditional split (`C-80`) |
| ≥1 must compare **source/deployed-code identity against custom-module reality** | **4** | `C-83`–`C-85`; and Expert 1 added the 90.7% concentration |

## 2. Outcome

| Expert | Scope | Confirmed contradictions |
|---|---|---|
| **1 — Leader Functional Design** | business consequences of the identity/population corrections | `C-54` … `C-62` |
| **2 — Leadership Database Design** | the identity model and the discovery method | `C-63` … `C-70` |
| **3 — Lead Integration & Localization** | scope-awareness, localisation, intercompany, routing | `C-71`, `C-72` |
| **4 — Lead Code & UI Architect** | `C-04` logic, mutation boundary, code identity | `C-74` … `C-85` |

**24 confirmed contradictions. Every one re-derived by P02 against primary source before adoption.**
**Two expert claims were refuted** and are recorded as refuted (§4).

## 3. The Two Findings That Dominate

**`C-74` — a safety defect, not an accuracy defect.** The `C-04` authorisation pack forbade companies
2–5 and named a script whose line 4 is `COMPANY_ID = 2`, which commits. **Approving it would have
authorised a committed write to a real-entity company record.** No other finding in this programme has
had that character. The pack is withdrawn.

**`C-86` — a reversal, and a positive one.** Found by P02 while verifying Expert 4's `CH-4`: full
reference distributions for six generations sit under `~/Library/CloudStorage` (**v14 796**, **v16 950**
module directories). `C-55` — "90.7% of the evidence rests on a generation whose standard source cannot
be read" — is **withdrawn**. Non-standard modules fall **620 → 540**; **`iSMEs` 13 → 1**.

## 4. Expert Claims P02 Did Not Adopt

| Claim | Why not |
|---|---|
| **Expert 3, `C-4`** — `46` §2's *"14.0 does not carry `cogs` in the selection"* is an **unsourced cross-generation transfer** | **Refuted.** It is sourced — to the **deployment's own** `ir_model_fields ⋈ ir_model_fields_selection`, re-verified this round with a `move_type` positive control returning 7 values. **A deployment's own schema is stronger evidence than a source root.** The separate observation that no 14.0 *code* root was then known stands, and is itself now withdrawn by `C-86`. |
| **Expert 4, `CH-4`** — *"no 16.0 or 14.0 core distribution anywhere on this host"*, ten module names return 0 | **Refuted by `C-86`.** Its sweep pruned `Library`, the same blind spot as P02's own three sweeps. |

**Both refusals were tested, not asserted** — the first by re-running the extraction, the second by
locating the distributions.

## 5. What The Challenges Could Not Break

- The **path-split arithmetic**: 24,500 + 109,673 + 1,000 + 6,062 = 141,235; 193,222 total — reproduced.
- The **`<1 MB` floor's minimum**: exactly 3,374,773 bytes.
- The **substantive valuation finding** on `551ab874`: independently re-derived from the artefact —
  **47,801 layers, `account_move_id` NULL on all 47,801**.
- The **zero-`cogs` measurement** on `45a8e08e`: reproduced on a materially independent instrument —
  447,384 rows, five marker values as the positive control, `cogs` = 0.
- **Raw PostgreSQL data directories**: searched for by an expert; **none exist**.
- **16.0 marker-capability**: Expert 4 supplied the package's **first primary-evidence proof**
  (8 selection members including `cogs`), where `C-43` had proved only the 14.0 negative and inferred
  the rest.

## 6. Method Observation

**Two experts reached the `pfp` single-lineage conclusion by entirely different instruments** — content
ancestry versus uuid version and provenance — without contact. **And both inherited P02's `~/Library`
prune.** Independent challenge caught what self-review could not; a **shared method assumption** was
caught by neither, and only by following an expert's wrong claim to its source.
