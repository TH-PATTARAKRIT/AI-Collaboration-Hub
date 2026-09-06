# P10 — CLOSURE QUESTION REGISTER

Prompt: `[SMEPLUS-26-09-06-G02-P10-TBR-BOUNDED-DEEP-CLOSURE-DESIGN-INPUT-001]`
Group: **G02 — Sales / Revenue / Cash.** Closure sequence `P02 → P10 → P06`.
Execution: continuation of the existing P10 session. **Not a reset, not a new research round.**

---

## 1. Baseline Verification — `CP-01`

| Declared in prompt | Verified | Result |
|---|---|---|
| P10 evidence baseline `284ea054…` | `git cat-file -e` | **DOES NOT EXIST in this repository** |
| Actual P10 head at prompt receipt | `git rev-parse HEAD` | **`284ea6651b7ba2ac712072d2654fc54f83d2deb3`** — *"decision-integrity and evidence-base repair"*, 2026-09-05 |
| P02 authoritative closure `7cb1c27…` | verified | **EXISTS** — *"P02: CP-06..CP-10 — challenge record, AAS+, PMO, final reconciliation"*, 2026-09-06 |
| Closure Constitution `48ee264…` | verified | **EXISTS** — *"establish bounded-deep Closure Execution Constitution v1"*, 2026-09-06 |

> **`G02-P10-E-01` — the declared baseline SHA does not resolve.** The two strings share their first five characters (`284ea`), so this reads as a transcription slip rather than a different commit. **P10 proceeds on the verified head**, which is the actual state of the declared working branch, and records the discrepancy rather than silently substituting. `FACT VERIFIED`. Routed to whoever issues prompts; **P10 does not correct another party's record**.

## 2. Declared Closure Scope — monotonic, per Constitution §4

| # | Declaration |
|---|---|
| **Closure Question IDs** | `CQ-P10-01` … `CQ-P10-13` as issued. **No question added by P10.** |
| **Domain boundary** | Time-based recognition only: deferred revenue, deferred expense, accrual, and the depreciation/loan mechanisms **solely as comparators** |
| **Source boundary** | The reference root already declared in this session's lineage, both of its module trees. **No new root admitted.** |
| **Evidence population** | The four deployed databases already examined in this session. **No new sweep.** P02's measurements on its own population are consumed as **controlled input**, not re-derived |
| **Cross-process interfaces** | `P02` inbound (consume only) · `P06`, `P08`, `P11` outbound (publish only) · `P07` outbound for statutory questions only |
| **Explicit exclusions** | No execution or reopening of `P02`, `P06`, `P07`, `P08`, `P11`. No whole-estate, whole-volume, whole-backup or whole-repository search. No mutation. No new deployed-database enumeration |

**Standing constraint applied throughout:** *closure may become deeper; it may never become wider.*

## 3. Prior-Baseline Preservation — per prompt §6

Preserved without re-derivation, revalidated only where a Material Delta arises:

| Preserved item | Where it lives |
|---|---|
| Separation of recognition semantics from posting mechanics | prior session `01`, `28` |
| Shared semantic-kernel candidate (six elements, later three) | `30`, `56` |
| Separate domain-engine concept | `57` |
| `AASP-VETO-01` revision 3 and its HOLD lineage | `51`, `32` |
| Contradictions on lock behaviour, recognition period, allocation-policy ownership, currency, reporting/company ownership, screen-versus-post | `11`, `67` |
| The **60 cumulative corrections** across four prior rounds | `14`, `70` |

## 4. P02 Controlled Input — consumed, not researched

P02 terminal state **preserved as issued**: `MAXIMUM AVAILABLE EVIDENCE REACHED — HOLD FOR NAMED DEPENDENCY`. **Not reinterpreted as PASS or CLOSED.**

| # | P02 → P10 item | P02's evidence | Exact question put to P10 |
|---|---|---|---|
| `IN-P02-1` | ~~Billing ahead of performance dominates~~ — **WITHDRAWN by P02, `G02-R-01`** | Draft-basis: 789 vs 47; 2,564 vs 253. **Posted basis (Archive C): 1,145 delivered-not-invoiced vs 792 billed-ahead — 1.4:1 toward DELIVERY.** Other rows are **floors**, quoted **by unit**, never summed | Does revenue recognise on billing or on performance? The cut-off population exists **on both sides**; segmentation by product invoicing policy is owed by P02 before either figure is acted on |
| `IN-P02-2` | **Bill-and-hold has no representation** | Representable only as invoice-on-order | Is bill-and-hold in scope, and if so what is the recognition trigger? |
| `IN-P02-3` | **A deployment delivering and never invoicing** | 1,201 delivered-not-invoiced, **0 matched, ever** | Is this a configuration state P10's model must tolerate? |
| `IN-P02-4` | **An un-invoiced balance exists in sales and not in the ledger** | — | Should the obligation position be P10-owned or P02-owned? |

**Also consumed as controlled input, and load-bearing:**

- **Boss Decision 3 — *revenue on billing versus performance* is `OPEN — Boss reserved`.** P02 supplies measurement only. P10 **may not settle it**.
- P02 unresolved dependency 5: **revenue timing — owner `Boss / P10`**.
- P02 design candidates include **event identity** and a **two-date model** — reached independently of P10 and converging with P10's own.
- P02's invariant finding: *one business fact → one canonical event owner → one accounting effect path* is **not satisfied by the reference at the correction/reversal stage**.
- P02 names a database (`iErpOCC`) **outside P10's examined four**. Under the monotonic scope rule P10 **does not go and read it**; it bounds P10's population claims instead — see `P10_EVIDENCE_POPULATION_BOUNDARY.md`.

## 5. The Register

| CQ | Subject | Terminal disposition | Deliverable |
|---|---|---|---|
| `CQ-P10-01` | Recognition event identity | see `P10_RECOGNITION_EVENT_IDENTITY_TRACE.md` | ✔ |
| `CQ-P10-02` | Recognition period versus posting date | see `P10_RECOGNITION_PERIOD_VS_POSTING_DATE.md` | ✔ |
| `CQ-P10-03` | Schedule / period grid / convention | see `P10_PERIOD_GRID_CONVENTION_TRACE.md` | ✔ |
| `CQ-P10-04` | Revenue versus expense recognition | see `P10_REVENUE_EXPENSE_SEMANTIC_BOUNDARY.md` | ✔ |
| `CQ-P10-05` | Allocation policy ownership and scope | see `P10_ALLOCATION_POLICY_SCOPE_MATRIX.md` | ✔ |
| `CQ-P10-06` | Currency / amount semantics | see `P10_CURRENCY_AMOUNT_TRACE.md` | ✔ |
| `CQ-P10-07` | Correction / reversal / cancellation algebra | see `P10_CORRECTION_REVERSAL_ALGEBRA.md` | ✔ |
| `CQ-P10-08` | Period close / lock interaction | see `P10_PERIOD_CLOSE_LOCK_MATRIX.md` | ✔ |
| `CQ-P10-09` | Shared semantic kernel boundary | see `P10_SHARED_SEMANTIC_KERNEL_ASSESSMENT.md` | ✔ |
| `CQ-P10-10` | Reporting / audit / source-to-recognition lineage | see `P10_AUDIT_LINEAGE_TRACE.md` | ✔ |
| `CQ-P10-11` | Scope / multi-company / access | see `P10_SCOPE_OWNERSHIP_MATRIX.md` | ✔ |
| `CQ-P10-12` | Evidence identity / population boundary | see `P10_EVIDENCE_POPULATION_BOUNDARY.md` | ✔ |
| `CQ-P10-13` | Evidence integrity / terminality | `P10_G02_TERMINALITY_RECORD.md` | ✔ **— and this tick was FALSE when first made.** The file did not exist; three of four challengers found it independently (`G02-R-08`). It is now written. Recorded rather than quietly satisfied |

Dispositions are recorded in each deliverable and consolidated at `P10_G02_TERMINALITY_RECORD.md`. **Every disposition is exactly one of the five permitted values; no `OPEN` and no `TBD`.**

## 6. Material Delta Log — this round

Every challenge-driven additional pass is recorded here before it is executed, per prompt §8.

| MD ID | CQ affected | Bounded evidence surface | Why current evidence is insufficient | Stop condition | Outcome |
|---|---|---|---|---|---|
| *(entries appended as raised — see §6a in the terminality record)* | | | | | |
