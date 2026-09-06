# P07 — CLOSURE QUESTION REGISTER

Round `SMEPLUS-26-09-06-…-002`. `LAYER 2 — AUDIT QUARANTINE`.
`COMMON_CLOSURE_EXECUTION_CONSTITUTION_V1 §11`: **no Closure Question may remain a vague
`OPEN`.** Each ends as exactly one of six terminal dispositions.

## 1. Dispositions

| CQ | Question | Terminal disposition | Basis |
|---|---|---|---|
| `CQ-P07-01` | Tax event identity without mutable labels | **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** | **There is no tax-event object.** Every tax fact is an attribute of a document; the tax invoice has no document identity P07 can supply (`DOC-01`); the certificate links to a payment; correction lineage is absent (`L-1`…`L-5`). The question is answered — the answer is that the identifier does not exist. Designing one is PHASE B. |
| `CQ-P07-02` | Tax timing / date semantics, five dates kept apart | **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** | `P07_TAX_EVENT_DATE_PERIOD_MATRIX.md §1`–`§3`. `D-1` has no carrier; `D-2` is display-only; `D-3` is the sole selector and has **no statutory relevance**; `D-4` is P06's and mutable; `D-5` is derived, never stored. The carriers that exist are measured (`P07-F-107`) and inert. **The dates were not collapsed.** |
| `CQ-P07-03` | VAT input/output boundary — prerequisites, base, state changes, corrections | **`UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`** | The **input** half cannot be closed: the deferred input-tax claim window has no primary statutory source held (`P07-U-03`, `CI-14`), and `AASR-P07-VETO-01` rests on it. **The exact missing dependency is named**, which is what makes this a valid terminal state rather than an `OPEN`. The output half is `FACT VERIFIED` within `02`, `04` and `CO-01`. |
| `CQ-P07-04` | WHT boundary — service / payment / recognition / certificate semantics and timing | **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** | The semantics are identified and the divergences measured: `P07-F-11` (reported against the invoice, not the payment), `W-C-01`, `W-C-02`, `P07-F-108`, `P07-F-109`, `P07-F-111`, `P07-F-112`. **Boss policy preserved: WHT is an Accounting function and not an Inventory stock-move function** — no inventory surface was entered. The *cause* of `P07-F-109` is separately carried as `P07-U-35`; the semantics do not depend on it. |
| `CQ-P07-05` | Tax document / certificate lifecycle; provenance that must survive | **`UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`** | The **states that exist** are fully enumerated (`CORRECTION_REVERSAL_LINEAGE_MATRIX.md §5`): create modelled, issue not distinguished from create, cancel a Boolean, reissue and replace not modelled. The **provenance that *must* survive** is statutory and unheld — `P07-U-26` (the prescribed contents of the s.87(3) report, which also gates P04's `P04-F-67`) and `P07-U-13`. Named dependency, not a vague open. |
| `CQ-P07-06` | Statutory period / cut-off across boundaries | **`BOSS DECISION REQUIRED — DECISION PACKAGE READY`** | `PX-01`…`PX-05` are traced and classed. `PX-06` — **may a filed period change at all?** — dominates and is not an evidence question: no tax-period state exists, the only control is P08's accounting lock, and un-reconciling is not lock-gated. P06, P07 and P05 hold the same question in the same state (`MD-06`). The decision package is `PX-06` plus `PS-10`. |
| `CQ-P07-07` | Correction / reversal continuity without silent divergence or double counting | **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** | **Answered: the chain does not exist end to end.** Three of five lineage links absent, two broken; `L-3` — no filed figure is stored — is the structural one. Silent divergence **measured** at 199 of 1,186 (`P07-F-109`), with the leading alternative explanation tested and excluded (`P07-C-29`). Double counting: `P07-F-111` and `P07-F-112`. |
| `CQ-P07-08` | Scope / legal entity classified before any scope rule is claimed | **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** | `DOMAIN_PURITY_AND_BOUNDARY_REGISTER.md §3`. Every material fact classified PLATFORM / TENANT / COMPANY on its own evidence; **none forced to TENANT + COMPANY**. Two are PLATFORM-only, and recognising that is what resolved `MD-02`. The tenant-containment ruling for the cross-company tax-unit grouping remains **P11's** (`H-07`, `P07-U-14`) and is not claimed here. |
| `CQ-P07-09` | Minimum semantic facts for tax registers to reconcile to source | **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** | The minimum set is stated (`CH-04`, `CRL-01`…`CRL-05`) and the blocking gap identified: **`L-3` — nothing records what was filed**, so no register can be reconciled to a filing. `P07-F-111` and `P07-F-112` establish that one statutory number is computed four ways over three bases and that **two of those bases cannot agree**, because one is empty on 96.5% of the population. `P07-U-36` was opened and closed inside this round rather than left deferred (`REV-M-99`). |
| `CQ-P07-10` | Evidence integrity and terminality | **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** | Every load-bearing negative carries a denominator, a path set, a version boundary, a firing positive control, a failure control where applicable and a declared residue (`…SUPPLEMENT.md §2`, `§9`). Six blind spots declared (`BS-01`…`BS-06`). **Background tasks: zero running, one dispositioned** (`22 §48.1`). Two instruments were used where one zero would have carried a claim. |

**Six `FACT VERIFIED`, two `UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE` with the exact
dependency named, one `BOSS DECISION REQUIRED`, one — none — left vague.**

**No question is disposed `EXTERNAL / CROSS-PROCESS OWNER` or `OUT OF SCOPE`**, because no
declared Closure Question turned out to belong to another process. Eight cross-domain *paths*
opened during execution and all eight were stopped at the boundary (`DOMAIN_PURITY…§2`); that is
a different thing from a question being someone else's.

## 2. Derived Subquestions, Also Terminally Disposed

The constitution requires every **material derived** subquestion to be disposed too.

| derived subquestion | arose under | disposition |
|---|---|---|
| Do installed Thai localisation modules alter recognition timing / accounts / presentation? | `MD-01` → `CQ-P07-02` | **`FACT VERIFIED`**, bounded and scope-noted after `CH-A`/`CH-C`; handoff published |
| How many Thai localisation modules are installed? | `MD-02` → `CQ-P07-08` | **`FACT VERIFIED`** — `10,10,10,10,9,9,1`; `P07-F-106` |
| Does an item-level tax-period carrier exist? | `MD-03` → `CQ-P07-02` | **`CONTRADICTED — CORRECTED AND CLOSED`** against P10's `FACT VERIFIED`; `P07-F-107` |
| Do the two candidate code bodies agree on `_compute_wht_amount`? | `CQ-P07-04` | **`FACT VERIFIED`** — they do not; `P07-F-108` |
| Does the stored `wht_amount` match its own transaction? | `CQ-P07-04`, `CQ-P07-07` | **`FACT VERIFIED`** at 199 of 1,186; `P07-F-109` |
| **Why** does it diverge? | above | **`UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`** — `P07-U-35`, `EVIDENCE NEVER RECORDED`; needs a controlled execution, not more reading |
| Is the divergence live? | above | **`FACT VERIFIED`** — latent; the only consumer is uninstalled in 6 of 7; `P07-F-110` |
| Can the two withholding bases disagree? | `CQ-P07-09` | **`FACT VERIFIED`** — one is empty on 96.5% of the population; `P07-F-112` |
| Does a rate edit explain the 199? | `CH-B` | **`FACT VERIFIED` — no.** 151 of 199 have no rate to have changed; the other 48 carry no rate-edit signature; `P07-C-29` |
| Where is `l10n_th_google_fonts`'s source? | `BS-01` | **`UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`** — `P07-U-34`, `NOT ON THIS HOST` |

## 3. Terminality Audit — `COMMON_CLOSURE_EXECUTION_CONSTITUTION_V1 §12`

| requirement | state |
|---|---|
| every Closure Question has one terminal disposition | **yes** — §1, ten of ten |
| all material derived subquestions terminally disposed | **yes** — §2, ten of ten |
| all material contradictions reconciled or named holds | **yes** — `P07-C-26` resolved, `P07-C-27` scoped, `P07-C-28` named hold, `P07-C-29` challenge failed on measurement |
| all handoffs published | **yes** — `P07_TO_P10_HANDOFF.md`; `CH-06` records that P06 is sent nothing it has not already committed |
| all background tasks finished or dispositioned | **yes — zero running.** Verified at round close; the one prior task is dispositioned at `22 §48.1` |
| checkpoint current | **yes** — `P07_CHECKPOINT_AND_AUTO_RESUME_STATE.md` |
| `AUTO_RESUME_STATE` records the exact next action | **yes** |
| commit pushed; remote HEAD equals the intended final commit | verified at round close and recorded in the terminal report |
| no silent mutation | **yes** — read-only throughout; no DB, runtime, source or configuration was modified |
| no receiving Pxx executed from P07 | **yes** — eight boundary stops recorded |
| no merge or Final Freeze inferred | **yes** |
