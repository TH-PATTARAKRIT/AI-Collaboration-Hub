# 12 — P04 CONTRADICTION REGISTER

Layer: **2 — audit quarantine**.
Disagreement is **preserved**, not resolved by preference.

---

## 1. Inherited — carried unchanged (16 open at P3)

*Identifier note (`01` §6A.18, `P04-F-117`): the rows below are **P3's** `CTR-nn`
and `CTR-C-nn`, carried unchanged for lineage. They are **not** this session's
`P04-CTR-nn`, which occupy the same numbers 01–06 with entirely different content.
Cited outside this register they are written **`P3 CTR-nn`**; the inherited
identifiers themselves are left untouched so the lineage to P3 survives.*

Six inherited by P3 from P2 and ten raised in P3. All are carried at their prior
severity and are **not re-derived**. Two are advanced by this session's evidence
and are annotated below; the rest stand as recorded.

| ID | Statement | Sev | P04 note |
|----|-----------|-----|----------|
| `CTR-01` | The configured depreciation method has no verified implementation on the target generation | High | unchanged |
| `CTR-02` | The custom link module's disposal behaviour does not execute | Med | **Re-verified this session.** The wizard package is still never imported, and **three** model files are unimported, not two (`P04-REV-04`) |
| `CTR-03` | On the legacy generation, daily depreciation and the machine link were attached to **two different asset records** | High | unchanged. Prior packages recorded that it has been stated twice and acted on zero times |
| `CTR-04` | Confirming an asset silently changes an operational record with no way back | Med | unchanged |
| `CTR-05` | Posted disposal gain and stored gain can differ | Low-Med | **Cause re-confirmed**: the stored figure uses a book value that **includes children**; the posted difference is per asset (`P04-F-27`) |
| `CTR-06` | The schedule-closes-to-zero invariant is application-enforced only, against bulk-loaded data | High | unchanged |
| `CTR-C-01` | `BD-01` says "must not silently alter"; the evidence permits a stronger rule | Low | unchanged |
| `CTR-C-02` | 100 % attribution and TAS 2 ¶13 conflict under the obvious reading | **High** | **Advanced** — see §2, `P04-CTR-03` |
| `CTR-C-03` | `BD-02` treats maintenance as one cause; TAS 2 ¶13 requires two | Med | unchanged |
| `CTR-C-04` | `BD-04` requires one driver; the standard requires two | Med | unchanged |
| `CTR-C-05` | Off-balance accounts are selectable and not postable on the costing path | Med | unchanged |
| `CTR-C-06` | The rate snapshot exists and is not used by the paths that matter | Med-High | unchanged |
| `CTR-C-07` | The labour ledger entry is dated at posting, not at production | High | **Compounded** by `P04-B-31` — see §2 |
| `CTR-C-08` | Cancellation deletes allocation records in a product that never edits a depreciation entry | Med | unchanged |
| `CTR-C-09` | Machine cost reaches inventory only under two of three costing methods | High if unnoticed | **Materially advanced** — see §2, `P04-CTR-04` |
| `CTR-C-10` | Company-optional master data contradicts the no-cross-tenant requirement | High for SaaS | **NARROWED under the scope-aware correction** — see `20` §4.1 and §2 below |

## 2. New — raised by this session (7)

| ID | Contradiction | Sev | Disposition |
|----|--------------|-----|-------------|
| **P04-CTR-01** | **Three independent enumerations of one population disagreed** — 60, 46 and 65 — and one produced a **false negative on a load-bearing question** ("no custom module touches the asset domain"). Settled by direct execution: **65 directories, 2 asset-touching modules** | **High for method** | **RESOLVED by execution.** Preserved because it is direct evidence for the standing lesson that independent verification is the only control that catches this class. `05` §6 |
| **P04-CTR-02** | Prior evidence states that *"depreciation already reaches production cost centres through the analytic distribution"* — one of the two mechanisms the AAS+ veto names as live. **It nets to zero.** Both entry lines carry the distribution and the analytic amounts cancel | **High** | **The prior statement is CONTRADICTED.** The veto is not lifted; its shape changes and its second limb widens. `06` §4 |
| **P04-CTR-03** | `CTR-C-02` framed `BLK-07` as a binary between two readings, one of which breaches TAS 2 ¶13. **TAS 16 governs the size of the charge; TAS 2 governs its absorption.** Once separated, a **third compliant option** exists | Med | **OPEN — Boss decision.** `P04-BD-05`. Does not displace the standing recommendation |
| **P04-CTR-04** | Under **standard costing** the finished move credits the production account with **standard** overhead on **planned** duration, while the relief entry — which has **no cost-method guard** — debits **actual** overhead. The difference is stranded with **no variance account and no report line** | **High** | **OPEN.** This is a genuine general-ledger mismatch, independent of the depreciation question, that **no prior package recorded**. It also bears directly on the prior open item asking how a standard-costed product complies with TAS 2. `06` §3 |
| **P04-CTR-05** | The estate **hard-blocks** a disposal at the fiscal lock date and **silently re-dates** a depreciation entry past it. Two asset operations, one lock date, two opposite outcomes. **Corrected after independent challenge:** this is **not** an inconsistency inside one module. The hard refusal is asset-module code; the silent re-dating is the **accounting core's generic posting routine** and applies to every programmatically posted entry in the product. The contradiction is real and its **owner is the core, not the asset domain** — which makes it larger, not smaller | **High** | **OPEN.** `P04-B-31`, `11` §3. Owner **P08** |
| **P04-CTR-06** | The prompt requires *"always trace financial fact to initiating business event"*. For assets that is **not satisfiable from stored data** — the purchase-order reference lives on the journal item and the two-hop join is nowhere materialised | Med | **OPEN.** `P04-B-01` |
| **P04-CTR-07** | The estate's own equipment flag forces a product to a **non-storable** type, which **cannot** reach a capitalizable account through the product → category → account chain. The flag intended to mark equipment pushes it **away from** capitalization | **High** | **OPEN.** `05` §5, `P04-F-39` |

### 2.1 `CTR-C-10` — narrowed, not withdrawn

Recorded here because narrowing a High-severity finding must be visible.

**Before:** company-optional master data across four object classes is a
multi-tenant-safety failure.
**After the scope-aware correction:** company-optional is a defect **only** where
the object creates a financial effect and therefore cannot answer *which company
owns that effect*. That is **one** of the four classes — the work centre. The
machine register is legitimately tenant-scoped and company-less.

The finding is **weaker in breadth and stronger in force**: for the work centre
it is now a scope violation on the corrected constitution's own terms
(question 7 unanswerable ⇒ DENY). Full analysis in `20` §4.1.

## 3. Re-opened — the handover residue (7 disagreements)

Seven expert disagreements preserved by P2 were **never closed and never
carried**. They are re-registered here so they survive this boundary.

| # | Disagreement | Status |
|---|--------------|--------|
| 1 | Capitalization: **absent** or **partial**? | **Advanced by this session.** `01` establishes exactly one automatic path, three manual, one system-generated, one import. The correct answer is **partial**, and the dispute was about whether that count deserved the word. **Recommend closing as PARTIAL** |
| 2 | Revaluation: a boundary statement, or **partial**? | **Advanced by this session.** `07` §4.1: of seven TAS 16 derecognition requirements, one is met, two partly, **four have no host**. Revaluation specifically has no surplus and no equity component. **Recommend closing as PARTIAL, with the four gaps named** |
| 3 | Retire a piece of terminology? | Open, unadvanced |
| 4 | Severity of the unguarded confirm path — High versus unrateable-because-untested | Open. This session **re-confirms the mechanism** (`P04-B-32`) without resolving the severity dispute. **Both positions preserved** |
| 5 | Is maintenance costing a genuine differentiator? | Open, unadvanced |
| 6 | Where should machine identity live? | Open. `05` §3 and §5 strengthen the factual base — the break is on the asset side and there are now **two** custom equipment-creating paths — without deciding it |
| 7 | Report an internal scoreboard? | Open, unadvanced |

## 4. Contradictions this session **closed**

| ID | Closed how |
|----|-----------|
| `P04-CTR-01` | By direct execution of the disputed count |
| The prior **destruction-evidence** question (dropped, not closed, in P1) | By primary statutory evidence: the goods-and-scrap instruction does **not** cover fixed assets; a separate ruling governs them, requiring proof of destruction and auditor certification. `07` §5. **One residual question remains and is registered** (`P04-B-24`) rather than being presented as closed |

## 5. Standing qualifier

Every statement of the form *"not found"* in this package is bounded by the
source trees available in this workspace and by the declared pattern and path
set. That qualifier **cannot be dropped** until the installed-module list of the
running system is known — which remains a priority-1 runtime query, carried
unchanged from the prior package.
