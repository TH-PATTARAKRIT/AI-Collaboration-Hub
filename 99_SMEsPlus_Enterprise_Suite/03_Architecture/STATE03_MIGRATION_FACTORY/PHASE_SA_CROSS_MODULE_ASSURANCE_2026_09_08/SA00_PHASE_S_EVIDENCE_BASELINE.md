# SA00 — PHASE S EVIDENCE BASELINE
## CP-SA-00 — EVIDENCE BASELINE LOCKED

Session: `[SMEPLUS-26-09-08-ACC-PHASE-SA-SA-MASTER-001]`
Branch: `architecture/account-phase-sa-new-session-2026-09-08-001`
Baseline commit read: `b1d24eea`
Status: **CP-SA-00 CLOSED (execution status)** — see §9 for what that does and does not mean.

---

## 1. Why this register measures instead of asserts

Phase SA must know what Phase S actually established before it can assure anything across
modules. A statement such as "Phase S covered the Account domain deeply" is a claim about an
evidence base, and a claim about an evidence base is itself a claim that must be measured.

This register therefore declares its **population, pattern, path set and unit** before
reporting any number, and publishes the commands' results rather than the intent.

---

## 2. Declared measurement frame

| Clause | Declaration |
|---|---|
| **POPULATION** | Every branch on remote `origin` of `TH-PATTARAKRIT/AI-Collaboration-Hub` at fetch time 2026-09-08, excluding `origin/HEAD` (a symbolic alias for `origin/SMEsPlus`). **n = 182.** Not author-chosen: enumerated by `git for-each-ref refs/remotes/origin`. |
| **PATH SET** | For each branch *b*, every path differing between `merge-base(origin/SMEsPlus, b)` and *b*. Whole-repo; no directory pre-filter. |
| **UNIT** | Two units are used and never conflated: **(U1) unique blob** = distinct content object; **(U2) unique path** = distinct repository path. Counts state which unit they use. |
| **PATTERN** | Declared per measurement in the tables below, and executed. Patterns are published with their results, not described. |
| **ELIGIBILITY** | All 183 branches are eligible. One declared exclusion is applied and named in §4. |

### 2.1 Corpus construction and its coverage assertion

| Quantity | Value |
|---|---|
| Branches measured | 182 / 182 (183 refs enumerated, 1 symbolic alias excluded) |
| Branch-path pairs | 6,609 |
| Unique paths (U2) | 2,580 |
| Unique (blob, path) pairs | 2,803 |
| Unique **text** blobs extracted (U1, `.md`/`.txt`/`.csv`) | **2,722** |
| Extraction requested / written / missing / extra | 2,722 / 2,722 / 0 / 0 |
| Zero-byte files after extraction | 0 |
| Corpus bytes | 28,455,846 |
| Content positive control `BD-ACC-01` | 17 blobs — fires |
| Content positive control `clean.room` | 921 blobs — fires |

**Note on units.** 2,803 unique (blob, path) against 2,580 unique paths means **223 paths
carry more than one distinct content version across branches.** A path-only count understates
the corpus. Both figures are published; neither is used as the other.

---

## 3. Instrument defects found and corrected during this measurement

Four defects were found in this session's *own* instruments before any result was relied on.
They are published because a corrected instrument is only trustworthy if its failures are visible.

| # | Defect | How it presented | How found | Correction |
|---|---|---|---|---|
| SA00-I-01 | **False positive.** Token `PROJECT` counted 161 paths as Project-module evidence. | Looked like solid Project coverage. | Printing what the pattern actually matched: 159 of 161 were `00_Project_Governance` scaffolding. | Governance scaffolding declared an exclusion (§4); Project-module evidence re-measured. |
| SA00-I-02 | **False negative.** Pattern `/P05_` returned 1 for the Expense-to-Pay package. | Looked like P05 was near-absent. | A second command of different shape (`EXPENSE` token) returned 91. The real filenames are `01_P05_...`, so the segment-anchored pattern could not fire. | Patterns re-cut as word-bounded tokens, not path-segment anchors. |
| SA00-I-03 | **Control that could not detect its own failure.** The content corpus extracted as 2,722 files, the file-count coverage assertion reported "complete", and every file was **zero bytes**. | A complete-looking corpus containing nothing. | A *content* positive control (`BD-ACC-01` must be findable) returned 0. The file-count assertion could never have detected this. | Extraction rebuilt through a single batch process; corpus re-verified by byte count **and** content control. |
| SA00-I-04 | **Delimiter collision.** The domain table used `\|` as both field separator and regex alternation, so each domain silently searched only its **first** term. | Plausible per-domain numbers, understated by up to 5x (D01 Sales read 54, actually 297). | Cross-checking a domain whose package size was independently known. | Separator changed; every domain re-measured. |

A fifth defect (join key mismatch: corpus keyed by 40-character blob SHA, path map by
abbreviated SHA) produced an empty attribution table; it was caught by its own positive
control returning zero and was corrected before any attribution result was used.

**Lesson carried into this package:** every count below was produced by an instrument that
has a positive control, and no count is reported without one.

---

## 4. Declared exclusion

| Excluded | Paths | Authority for the exclusion |
|---|---|---|
| `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/**` and `00_PROJECT_STANDARD/**` | 161 | Programme governance scaffolding (state/step/gate administration). It is not module business evidence and its presence inflates any module token count that shares a word with it. |

The exclusion is applied to path-token measurements only. **The content corpus is not
pruned** — all 2,722 text blobs remain searchable, so nothing is hidden from content search.

---

## 5. Accounting process coverage (Phase S P-series)

UNIT = unique path (U2), after the §4 exclusion. PATTERN = word-bounded token, executed.
Every pattern below fired; the example is the positive control.

| Process | Paths | Positive-control example |
|---|---|---|
| P01 Procure-to-Pay | 122 | `00_README_P01_PACKAGE_INDEX.md` |
| P02 Order-to-Cash | 61 | `00_README_PACKAGE_INDEX.md` |
| P03 Manufacture-to-Cost | 102 | `P01_P03_CORRECTION_HANDOFF.md` |
| P04 Acquire-to-Retire | 56 | `P01_P04_CENSUS_RESPONSE.md` |
| P05 Expense-to-Pay | 90 | `P01_P05_VENDOR_ADVANCE_RECONCILIATION.md` |
| P06 Bank-to-Reconcile | 117 | `P01_P06_SUPERSESSION_RECONCILIATION.md` |
| P07 Tax (Thailand) | 41 | `51_P05_P07_TX01_STATUTORY_HANDOFF.md` |
| P08 Record-to-Report | 131 | `P01_TO_P08_HANDOFF.md` |
| P09 Plan-to-Analyze | 165 | `00_README_PACKAGE_INDEX.md` |
| P10 Time-Based Recognition | 114 | `P09_P10_HANDOFF_REFRESH.md` |
| P11 Core Reconciliation | 134 | `P01_P11_EVIDENCE_VERSION_DEPLOYMENT_SUPPLEMENT.md` |

All eleven accounting processes carry substantial, locatable evidence. **No P-series process
is unevidenced.**

---

## 6. Domain coverage against the SA-D00…SA-D16 split

UNIT = unique text blob (U1), n = 2,722. MENTION = blob contains any declared term.
MENTION is a **floor**, not a coverage measure: a package may address a domain in vocabulary
the pattern does not carry (D10 shows this — 55 mentions against 91 subject-named files).

| Domain | MENTION | % corpus | SUBJECT (filename-scoped) |
|---|---|---|---|
| SA-D00 Master Data / Tenant / Company | 856 | 31.4% | 37 |
| SA-D01 Sales + AR | 297 | 10.9% | 147 |
| SA-D02 Purchase + AP | 448 | 16.5% | 265 |
| SA-D03 Inventory / Warehouse / Delivery | 1,367 | 50.2% | 560 |
| SA-D04 Manufacturing / BOM / WIP | 512 | 18.8% | 105 |
| SA-D05 Supply Routing (MTO / Dropship / Kit) | **81** | **3.0%** | 35 |
| SA-D06 Accounting Event / GL / Posting | 612 | 22.5% | 199 |
| SA-D07 Tax / VAT / WHT | 1,217 | 44.7% | 97 |
| SA-D08 Payment / Bank / Cash | 1,493 | 54.8% | 353 |
| SA-D09 Asset / Depreciation / Disposal | 416 | 15.3% | 127 |
| SA-D10 Expense / Employee Expense | 55 | 2.0% | 91 |
| SA-D11 Analytic / Dimension / Cost | 790 | 29.0% | 177 |
| SA-D12 Period Close / Year Close | 248 | 9.1% | 461 |
| SA-D13 Approval / Workflow / SoD | 1,048 | 38.5% | 20 |
| SA-D14 Cross-Company / Multi-Company | 507 | 18.6% | 37 |
| SA-D15 Audit / Traceability / Evidence | 2,559 | 94.0% | 471 |
| SA-D16 Cross-Domain Reconciliation | 338 | 12.4% | 431 |

**SA-D15 at 94% is a saturated, non-discriminating term** — this is an audit programme, so
almost every file mentions evidence. It is reported for completeness and carries no coverage
signal. It must not be read as "audit is 94% assured".

---

## 7. The discriminating test — operational semantics vs accounting lens

Domain totals cannot distinguish *"Phase S understands how this module operates"* from
*"Phase S understands the accounting consequence of this module"*. The following pairs a set
of purely operational terms against a set of purely accounting terms over the same corpus.
UNIT = unique text blob (U1).

| Operational semantic | Blobs | | Accounting lens | Blobs |
|---|---|---|---|---|
| Stock reservation / allocation | 631 | | COGS recognition | 386 |
| Scrap / by-product / production variance | 265 | | Inventory valuation | 268 |
| Work order execution / WIP | 257 | | AR / AP ageing | 116 |
| Pick / pack / ship | 188 | | Depreciation schedule | 60 |
| Storage location / bin assignment | 74 | | Revenue recognition | 28 |
| **Quotation / sales quote lifecycle** | **80** | | | |
| **BOM / routing step / work center** | **48** | | | |
| **Price list / pricing rule** | **18** | | | |
| **Credit limit / customer hold** | **16** | | | |
| **RFQ / vendor selection** | **12** | | | |
| *negative control (unmatchable token)* | *0* | | | |

The negative control returned 0, so the instrument is not matching indiscriminately.

### 7.1 Finding SA00-F-01 — the evidence base is asymmetric, and the asymmetry is not where it was assumed

Phase S is **deep** on: inventory movement and reservation semantics, manufacturing execution
and variance, and the accounting consequence of every material flow.

Phase S is **thin** on the *demand-and-supply front end*:

- **the commercial entry of a sale** (quotation lifecycle 80, pricing 18, credit control 16);
- **the commercial entry of a purchase** (RFQ / vendor selection 12);
- **the product structure that drives manufacturing** (BOM / routing / work center 48);
- **the supply-routing decision itself** (SA-D05, 81 blobs — the lowest of all seventeen domains).

This matters because **SA-D05 supply routing is the subject of the Business-Nature Routing Law
(master prompt §6)** — the rule that a sale of a stocked item, a manufactured item, a dropship
item, a make-to-order item, a kit and a service must each take a different downstream route.
The one domain Phase SA is constitutionally required to determine is the domain Phase S
evidenced least.

---

## 8. Finding SA00-F-02 — a cross-module programme exists that the Phase SA entry baseline does not reference

The Phase S → Phase SA handoff register (`5b7a7ea1`) and the New Session context record
(`a2ce06f9`) name their authoritative inputs. Neither names the **Group A
Sales + Inventory + Purchase integrated backbone programme**, which is present on this remote
and is cross-module by construction.

| Branch | Short SHA | Files | Date | Role |
|---|---|---|---|---|
| `claude/group-a-sales-inventory-purchase-dr002` | `8b0993d8` | 20 | 2026-08-31 | Capability models, E2E lifecycle map, cross-module event/dependency map, business-fact ownership + handoff matrix, exception/partial/return/cancellation matrix, cross-module invariant register, unknown/conflict/gap register |
| `audit/group-a-sip-evidence-review-004` | `626873c3` | 10 | 2026-08-31 | Independent evidence review |
| `claude/team-b-group-a-sip-design-005` | `b98a3b9f` | 21 | 2026-08-31 | Design |
| `claude/team-b-group-a-sip-corr-007` | `b98a3b9f` | 21 | 2026-08-31 | Correction |
| `claude/team-b-group-a-sip-corr-008` | `359f96c0` | 28 | 2026-08-31 | Correction |
| `claude/team-b-group-a-sip-nonacct-corr-010` | `e4418644` | 55 | 2026-08-31 | Non-accounting correction |
| `ibpv/group-a-sip-formal-verification-006` | `535724c0` | 16 | 2026-08-31 | Independent formal verification |
| `ibpv/group-a-sip-formal-reverification-009` | `b2f7cbd3` | 45 | 2026-08-31 | Independent re-verification |
| `ibpv/group-a-sip-nonacct-reverification-011` | `77e93d44` | 72 | 2026-08-31 | **TERMINAL independent re-verification** |

This programme already contains the artefact types the master prompt §11 requires per domain:
input/output registers, downstream consumer register, routing, exception matrix, ownership,
tenant boundary, idempotency, SoD and cross-domain invariants — for exactly the three modules
where §7 above shows the Phase S accounting programme is thinnest.

**Disposition: this programme is admitted to the Phase SA evidence baseline.** It is not new
research; it is existing verified evidence that the entry baseline omitted.

### 8.1 Terminal state of Group A, quoted from its own register

From `ibpv/group-a-sip-nonacct-reverification-011` `77e93d44`,
`.../EXPERT_IBPV/GROUP_A_SALES_INVENTORY_PURCHASE/FORMAL_REVERIFICATION_RV_011/11_RV011_RESIDUAL_OPEN_ITEM_AND_BLOCKING_RULE_REGISTER.md`:

> **Pre-Development Gate remains `HOLD`** — items A1 and A2 are Boss/Accounting-dependent and are unaffected by
> this session's non-Accounting closure verification.

Open items carried at that terminal state:

| Item | Status (verbatim) | Owner |
|---|---|---|
| A1 — Sales-side cancellation-gate symmetry / Accounting-AR-AP dependency | `HOLD — WAITING FOR ACCOUNTING/AR-AP AUTHORITY` | Boss, with Accounting Core / AR-AP domain input |
| A2 — Legacy approval internal workflow/permission evidence | `EVIDENCE MISSING / BOSS DECISION REQUIRED` | Boss / PMO |
| A3 — Three deferred policy defaults | `SAFE TO DEFER` | Boss / business |
| C4 — Team A evidence branch-lineage gap | `EVIDENCE MISSING (in-lineage)` | PMO |
| C5 — Governance-evidence cross-branch lineage gap | `GOVERNANCE EVIDENCE EXISTS — CROSS-BRANCH TRACEABILITY / LINEAGE VISIBILITY ISSUE` | PMO |
| N12 — Reservation-claim tie-break policy | `CONTROLLED CARRY-FORWARD` | design |
| N13 — Dead-event-catalog inclusion rule | `CONTROLLED CARRY-FORWARD` | design |

---

## 9. Finding SA00-F-03 — a cross-programme handoff failure, measured

Item **A1** is explicitly addressed to *"Accounting Core/AR-AP domain input"* and has stood at
`HOLD — WAITING FOR ACCOUNTING/AR-AP AUTHORITY` since 2026-08-31.

Between 2026-09-04 and 2026-09-08 the Account programme executed eleven process packages
(P01–P11) and reached `CP-SC-15 — PHASE S CONDITIONALLY CLOSED`.

**Question tested:** did the Account programme answer A1?

**Instrument.** UNIT = unique text blob (U1) over the full 2,722-blob corpus; blobs matching a
subject pattern are joined to their repository paths and the path's owning programme is
counted. The join is validated by a positive control before any result is read.

| Pattern | Hit blobs | Programme attribution of the hit paths |
|---|---|---|
| `BD-ACC-01` *(positive control — an Account-owned ruling)* | 17 | `ACCOUNT_REOPEN` **17** |
| `cancellation.gate` *(subject of A1)* | 28 | `GROUP_A_SALES_INVENTORY_PURCHASE` 24, `EXPERT_IBPV` 16, `TEAM_B_DESIGN` 7, `INVENTORY_REOPEN` 1, `CHATGPT_AUDIT` 1, **`ACCOUNT_REOPEN` 0** |

(Programme tokens are counted as occurrences across distinct paths; one path may carry two
tokens, so the columns are not disjoint. The `ACCOUNT_REOPEN` figure is unaffected by this.)

The positive control fires at 17/17 on the same instrument, so a zero for `ACCOUNT_REOPEN` on
the A1 subject is a measured absence and not an instrument failure.

**SA00-F-03 — RESTATED BY CORR1. The original wording was falsified; see `SA20` §2.1.**

> ~~The Account Phase S programme contains **no** treatment of the Sales-side cancellation gate.~~

**What was wrong.** The pattern `cancellation.gate` is *Group A's own coinage*. The Account
programme was never going to write another programme's phrase, so the pattern could not fire on
it — the exact `SA00-I-02` defect this register documents, committed in its own headline. The
denominator *1,273 files* also carried **no unit** and is not reproducible: the same declared
method yields 1,368 unique paths, 1,304 text paths, or 1,449 (blob, path) pairs.

**The corrected finding.** Widening the pattern by one token (`cancel`) returns **24 files** in
the Order-to-Cash package alone. Its edge-case matrix carries a `CANCEL` row across order,
delivery, invoice, payment and matching, and a section on cancellation and reversal; its business
event register enumerates invoice draft / posted / reset-to-draft / cancelled / return / credit
note, each `FACT VERIFIED`. **The Account programme did establish the semantics Group A asked
for.**

**What survives, and it is still material.** Nobody answered Group A **in Group A's register**.
The item has stood at `HOLD — WAITING FOR ACCOUNTING/AR-AP AUTHORITY` since 2026-08-31 while the
answer existed in a sibling programme. **This is a routing and notification failure between two
programmes, not an absence of the input** — and the remedy differs: the input does not need
researching, it needs delivering, and the residual question (which state carries blocking weight)
needs a decision.

This correction *strengthens* `SA13-F-02`: the cross-programme reconciliation was constituted and
never convened, and this is precisely the cost of not convening it.

**Class.** This is a cross-programme handoff failure, not an error inside either programme.
Each programme is internally coherent; neither owned the boundary between them. It is exactly
the defect class Phase SA exists to detect, and it was invisible to every control that scoped
itself to one programme.

**SMEs Core first-detector status: SATISFIED.** Detected by SMEs Core cross-module review at
CP-SA-00, before Boss review. Boss is not the first detector.

**Routing:** carried to `SA14_CROSS_DOMAIN_CONTRADICTION_REGISTER.md` as the first entry, and
to `SA19_BOSS_FINAL_GATE_PACK.md` — A1 requires an authority decision that only Boss can make.

---

## 10. Baseline lock

| Component | Locked at |
|---|---|
| Account Phase S P01–P11 | terminal branches per process, enumerated in `SA01_DOMAIN_COVERAGE_REGISTER.md` |
| Inventory programme (R4 L1–L12, multi-tenant invariant set, MTI rulings D-01/D-02/D-03, conformance) | `dcb92278`, `bd096ffa`, `a57bd555` |
| Asset programme (Deep L1–L6, DR continuation, P04/G01 closure) | asset branches per `SA01` |
| COGS lineage | `audit/cogs-deep-research-2026-09-02-001`, `research/cogs-targeted-resolution-2026-09-03-001` |
| **Group A Sales+Inventory+Purchase backbone** | **`77e93d44` terminal (RV-011)** — admitted by SA00-F-02 |
| Boss architecture rulings (SaaS Cell) | `origin/SMEsPlus` `fa57d10f`, files 00–18 |
| Boss accounting rulings BD-ACC-01/02/03A/03B + product-account override boundary | `79d70278` |
| **GB-08 — FX rate ownership and missing-rate policy**, `BOSS APPROVED — CANONICAL BUSINESS SEMANTIC` (admitted by CORR1; it was on this branch and unconsumed) | `.../ACCOUNT_FULL_DEEP_RESEARCH/GB08_BOSS_RULING_FX_RATE_OWNERSHIP_AND_MISSING_RATE_POLICY_2026_09_04.md` |
| Clean-room Nature DNA constitution | `c0880b10` |
| Very Deep Research re-entry protocol | `54dd32f2` |
| SMT/SMEs Core first-line detection rule | `5ce7747b`, `79d70278` |

### 9.1 Seven Boss decisions on `origin/SMEsPlus` not present in the Phase SA entry lineage

`origin/SMEsPlus` (`fa57d10f`) carries seven commits that are **not** ancestors of this branch.
They are cross-module boundary decisions and are material to Phase SA routing:

| Commit | Decision |
|---|---|
| `fa57d10f` | Project and Analytic Accounting boundary |
| `e47f0f2f` | Service menu structure |
| `a11c9e7b` | Manufacturing Work Orders vs Maintenance Orders naming |
| `36c62ab3` | Equipment vs Fixed Asset boundary |
| `4c469f8e` | Quality menu naming |
| `e6504225` | Accounting workspace — Invoicing / General Ledger / Finance + cross-report traceability |
| `f926ee0d` | Canonical English default and Purchase menu |

They are **cited, not merged** — this branch performs no merge. They are admitted to the
baseline as authority.

---

## 11. What CP-SA-00 closure means

`CP-SA-00 — CLOSED (execution status)`.

This means: the evidence baseline has been enumerated by a declared and executed method, its
instrument defects have been found and corrected, its omissions have been identified and
repaired, and the lineage is locked and citable.

It does **not** mean the evidence is sufficient, that the domains are assured, or that any
subject matter is correct. Three findings (SA00-F-01, SA00-F-02, SA00-F-03) are open and carry
forward.

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
