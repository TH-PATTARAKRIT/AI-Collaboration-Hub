# SA_CORR5_07 — `MTI-05` / `MTI-22` / `MTI-33` CLOSURE

## CP-SA-C5-70 — MTI RESIDUAL SPEC GAPS CLOSED OR EXACTLY BOUNDED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR5-ZERO-SME-CARRYFORWARD-001]`
Branch: `architecture/phase-sa-corr5-zero-sme-carryforward-closure-2026-09-09-001`
Workstream: **G**
Boss: **SOLE FINAL APPROVER**

---

## 1. `MTI-05` — the contradiction, adjudicated

### 1.1 The invariant and the ground

`MTI-05` (R1 §3, R2 `R2-CARRIED · SPECIFIED`): *"Each object type declares exactly one **context
anchor** — the single authoritative ancestor from which its company is derived. The derived value is
stored on the record, and a `CONTROL` continuously asserts stored equals derived."*

The `CONTRADICTED` grade (`SA_CORR4_06` row 4) rests on `SA_CORR3_07` §6.1 `INV-PR-07`, which measured
the R1 context matrix's `Anchor` column (35 rows): **26 single · 2 `X / Y` · 5 `X + Y` · 2 anchorless**,
stated **two readings** of `company + X` — (i) *company, derived via X* (honours the invariant),
(ii) *two anchors declared* (contradicts it) — and closed *"Not resolved here. Re-scoring another body's
matrix is that body's act."* **CORR4 then recorded the unresolved reading as a contradiction.**

### 1.2 What R2 did and did not change — and the lean of the record, stated rather than passed over

`CD-04` (Product, row 5) and `CD-12` (Product category, row 7) re-anchored both `X / Y` rows to
**`company`**. `CD-13` (row 16, Barcode nomenclature) and **`CD-14` (row 17, Unit group and unit,
*conditional on `CF-D-01`* — a Boss scope clarification, unruled)** moved two `tenant` anchors to
`company`. **The five `company + X` rows (8, 13, 14, 22, 23) are untouched by R2, and they are the whole
of the residual.**

`SA_CORR3_07` §6.1 does not only state two readings: it **leans to reading (ii)** — *"`MTI-05` requires
a *declared* anchor, so the notation is the declaration, which favours reading (ii)"* — and then declines
to resolve. The adjudication below argues **against** that lean, on the matrix's own text (`CHB-08`):

| Evidence | What it shows |
|---|---|
| Matrix §1 legend: *"**Anchor** — the single authoritative ancestor from which `company` derives (`MTI-05`)"* | the column's own definition is a **single ancestor** |
| Matrix §4.1 (R1): *"The moment any of those attach, the anchor moves to **`company`** (entries 5, 7, 8)"* — **a section R2 `CD-15` voids in full**, so it is cited only as evidence of the *author's own reading* of the notation, never as authority (`CHD-06`) | the R1 author read row 8's `company + product` as *company-anchored* — the notation was never intended as two ancestors; the **authority** for row 8 is `CD-04` (product → company) and `L8-10` (company at creation) |
| Rows 4 (Location → `warehouse`), 10 (Operation type → `warehouse`), 18 (Movement document → `operation type`) | the convention elsewhere is one ancestor, and the `company + X` form appears only on rows whose canonical **identity tuple** carries `company` explicitly (`L8-10` lot `(tenant, company, product, value)`; `L8-13`/`-14` *"company plus number"*) |
| `09` §2 rows `L8-10`, `-11`, `-13`, `-14`: company *"Creation"* / *"Application"* / *"Completion"* | company is **assigned directly** on these records; the `+ X` names the scoping ancestor of the identity, not a second derivation |

> ### Adjudication `M05-A1` (restated after `CHC-03`)
> **Reading (i) governs, on the matrix's own legend and its own §4.1.** `company + X` records identity
> composition; the derivation ancestor is single. **`MTI-05` is not contradicted.** The notation is
> ambiguous in the one column where it could least afford to be, and the controlled patch below is
> the declared reading, offered to the Inventory owner as the mechanical correction.

### 1.3 The declared anchor column — published as a controlled patch, closing the document-owner item

The full patch is `04_CONTEXT_MATRIX_ANCHOR_COLUMN_CORR5_CONTROLLED.md` in this package (the programme's
parallel-copy form for another party's artefact; the Inventory file is not modified). Summary:

| Row | Object | R1 cell | **Declared single anchor** |
|---:|---|---|---|
| 1 | Tenant | — | root — legitimately anchorless |
| 5 | Product | `tenant / company` | `company` (`CD-04`) |
| 7 | Product category | `tenant / company` | `company` (`CD-12`); costing facet value `HOLD` |
| 8 | Lot / Serial | `company + product` | **`company`** — assigned at creation (`L8-10`; `CD-04`) (*first draft of this file declared `product` and is corrected*) |
| 13 | Reordering rule | `company + location` | `location` |
| 14 | Put-away rule | `company + location` | `location` |
| 16 | Barcode nomenclature | `tenant` | `company` (`CD-13`) |
| 17 | Unit group and unit | `tenant` | `company` — **CONDITIONAL on Boss `CF-D-01`** |
| **21** | Inter-company transfer *(first draft wrote row 26, which is Replenishment run — corrected)* | — | not an object — an `MTI-22` relationship (`XCR-01`) |
| 22 | Count session (`CN-27`) · Adjustment (`CN-28`) | `company + location` | **two objects, one ancestor each**: session → `warehouse` `✎`; adjustment → `location` (*first draft named two ancestor types for one object — corrected; the session's ancestor is originated here, `CHD-05`*) |
| 23 | Scrap | `company + location` | `source location` `✎` (originated; `L8-14` supplies only *company plus number*) |

**35 rows: 34 carry exactly one declared anchor or a stated reason for none; row 17 is conditional on
Boss ruling `CF-D-01`.** *(First draft claimed 35 of 35 and "26 rows unchanged"; rows 16 and 17 had
moved under `CD-13`/`-14` and `CF-D-01` was not consulted — `CHC-03`.)*

### 1.4 Status, downstream impact

| Item | Before | After |
|---|---|---|
| `MTI-05` | `CONTRADICTED` (CORR4) | **`SA-SPEC-COMPLETE / RUNTIME PROOF REQUIRED — CONDITIONAL (`CF-D-01`, row 17 only)`** — declaration closed by the controlled patch; store-and-control half runtime (`CORR3` `M-2`) |
| `CF-I-07` | inherited the contradiction | inherits the closure; stays `SPECIFIED — CONDITIONAL (RC-D-02)` on its own ground |
| `HF-CTX-05` anchor path | — | one chain per row |
| Document-owner item on the Inventory matrix | open | **closed at Phase SA level by the controlled patch**; the Inventory owner's adoption is a conformance edit, non-material |
| `CF-D-01` | not consulted | **genuine Boss scope clarification, carried (pre-existing, 2026-09-05)** |

**Evidence basis:** matrix §1 legend, §4.1, rows 4, 8, 10, 13, 14, 16, 17, 18, 21, 22, 23; `MTI-08`,
`MTI-12`; `09` §2 `L8-10`…`-14`; R2 `CD-04`, `-12`, `-13`, `-14`; `SA_CORR3_07` §6.1 (both readings and
its lean). **Runtime proof:** `RT-M05-01` stored ≠ derived on any of the five object types → `MTI-19`
breach fires (synthetic injection `0 → 1`).

---

## 2. `MTI-22` — the register, closed at register level and bounded exactly

### 2.1 The stale count (`C5-B-01`)

CORR4 carried *"4 entries — 1 incomplete, 3 conditional"* (R1). The **R2** register
(`05_CROSS_CONTEXT_REGISTER_R2.md`, 2026-09-05) is the current one:

| Entry | Relationship | Direction | `AUTH` stated | Status (R2) | What keeps it open |
|---|---|---|:---:|---|---|
| `XCR-01` | Inter-company transfer | A → B, **paired** two single-context facts | ✔ | **`INCOMPLETE`** | `JT-10` (treatment) open; `GAP-FS-07` path never traced end to end; valuation `HOLD — COGS GAP` |
| `XCR-02` | Cross-Context Report Grant | read-only, one tenant | ✔ | **`SPECIFIED — CONDITIONAL (MTI-D-04)`** | **Boss ruling `MTI-D-04` unruled**; `AAS-V-03` |
| `XCR-04` | Platform template instantiation | platform → tenant, at provisioning | ✔ | **`SPECIFIED`**, bounded by `RC-F-06` | class list open-ended → **Boss `RC-D-02`** |
| `XCR-03` | *(struck)* tenant-level definitional master | — | — | **ELIMINATED** (`CD-06`) | — |
| `CF-XCR-GAP-01` | controlled product mapping / provenance correspondence | — | — | **required, unspecified, deliberately un-numbered** | gated on **Boss `MTI-D-04`**; ownership **Boss `RC-D-04`** |

### 2.2 What "register-level incompleteness" means, tested

Master prompt §10: *"Close the register-level incompleteness if all semantics already exist. If a real
semantic gap remains, route only that gap through Targeted Very Deep Research."*

| Semantic the register must carry (`MTI-22` text) | `XCR-01` | `XCR-02` | `XCR-04` |
|---|:---:|:---:|:---:|
| the two contexts | ✔ | ✔ | ✔ |
| correlation identity | ✔ (`HF-CTX-07`) | ✔ (grant identity) | ✔ (template version) |
| direction | ✔ | ✔ | ✔ |
| permitted effect | ✔ | ✔ | ✔ |
| evidence obligation | ✔ | ✔ | ✔ |
| `AUTH` to traverse (R2 addition) | ✔ | ✔ | ✔ |

**Every semantic `MTI-22` requires exists on every surviving entry. The register is complete as a list of
relationships that exist** (its own §5). What remains open is **not a semantic gap and not a research
gap**:

| Open item | Class | Owner |
|---|---|---|
| `MTI-D-04` — does a sanctioned cross-company read exist at all? (*"'No such grant exists' is a perfectly good ruling"*) | **genuine Boss policy** — registered 2026-09-04, options stated, never chosen | Boss |
| `RC-D-02` — closure of the configurable-record enumeration | genuine Boss | Boss |
| `RC-D-04` — mapping-layer ownership/commissioning (only if `MTI-D-04` = yes) | genuine Boss, dependent | Boss |
| `JT-10` inter-company transfer treatment; `GAP-FS-07` path tracing | joint Accounting × Inventory + an Inventory evidence act | joint / Inventory |

> ### Adjudication `M22-A1`
> **`MTI-22` moves from `SA-SPEC-GAP` (SMEs Core) to `SA-SPEC-COMPLETE AT REGISTER LEVEL — CONTENT
> CONDITIONAL ON BOSS RULINGS (`MTI-D-04`, `RC-D-02`) AND ONE JOINT DECISION (`JT-10`)`.** No Targeted
> Very Deep Research is opened: no unknown exists that research could close — the door's existence is a
> policy election Boss has held since 2026-09-04. **SMEs Core recommendation, offered and not decided:**
> rule `MTI-D-04` **"no cross-company grant in v1; the group-view need is met by per-company export"** —
> which settles `XCR-02`, `CF-XCR-GAP-01`, `AAS-V-03`'s subject and `CF-I-03`'s exception-path test
> data in one ruling, and can be widened later by a new ruling without unbuilding anything.

### 2.3 `GAP-FS-07` — the inter-company path, traced at data level (bounded evidence-at-rest pass)

`XCR-01` is `INCOMPLETE` partly because *"the path is never traced end to end"*. Instrument as §3.2 (same
tool, same identity key). Over the two 44-company databases, with the single-company production-scale database as the discriminating negative (`CHD-03`; the 2-company plain-SQL export was not opened for movements):

| Database | Companies | Transit-type locations (company-less) | Completed legs **into** the company-less transit location | Companies sending | Completed legs **out of** it | Companies receiving | Sending company also receives | Inter-company configuration present |
|---|---:|---:|---:|---:|---:|---:|:---:|---|
| `BK12MAY26` (gen 19) | 44 | 1 of 45 | **1,201** | **1** | **1,201** | **7** | yes (1) | 4 of 44 companies configured |
| `iEVING` 2026-07-23 (gen 19) | 44 | 1 of 45 | 0 (2 not completed) | 1 | 0 (2 not completed) | 1 | no | 4 of 44 |
| `iSMEs` (gen 16) | 1 | 0 | 0 | — | 0 | — | — | none (0 columns) |

Movements whose source and destination locations belong to **two different companies directly**:
**0** in all three (positive control: the join reaches 4,846 transit-involved movements in
`BK12MAY26`).

> **`C5-07-F-02`. In the one multi-company deployment that transfers between companies, the path is
> realised as two single-company movements — 1,201 completed legs from one company into a company-less
> transit place, paired with 1,201 completed legs from that place into seven companies — and never as
> one movement spanning two companies.** That is precisely the `XCR-01` shape (`MTI-44`: two
> single-context facts; `MTI-15`: never one fact spanning two companies), now **evidenced at data level**
> rather than asserted. **What remains untraced is the value leg** — what each company records as the
> cost of the goods it sends and receives — which is `JT-10`, a COGS/joint decision inside the COGS
> unknown population (`SA_CORR5_10` §3.1). `GAP-FS-07` moves from *never traced* to *structure traced,
> value untraced*; `XCR-01` stays `INCOMPLETE` on `JT-10` alone.

**Downstream:** `MTI-44` (paired facts, depends on `MTI-22`) reclassifies identically; `CF-I-03` `P5`
(*register content closed*) is a Boss-gated precondition, not a Phase SA gap; `CF3-P-04`'s test data
exists for `XCR-01`/`XCR-04` and is Boss-gated for `XCR-02`.

---

## 3. `MTI-33` — the Thai reason taxonomy

### 3.1 The invariant and the exact unanswered question

`MTI-33` R2: *"Adjustment, count, scrap, return, transfer and landed-cost allocation each execute within
exactly one `CTX`, and each carries a reason classification that is **defined independently of
context**, so that the same reason means the same thing in every company."* Status `SPECIFIED — VALUE
HELD`, *"reason taxonomy `R4-Q-01`, Thai panel, unanswered."*

`R4-Q-01` at primary text (R4 `20_RISK_GAP_DECISION_REGISTER` §6; `18_THAI_USER_VALIDATION_CHECKLIST`
§6): *"What reason taxonomy should adjustments and scrap use — this is what keeps non-sale reductions
distinguishable from sales, so it is not cosmetic"* — routed **Thai business validation**. The
requirement it serves (`L7-08`; `05_L4` §5 identity 4): *"every non-sale stock reduction must carry a
classification that distinguishes it from a sale, or the periodic cost-of-sales computation silently
mislabels it"* — **Inventory-owned, not COGS-gated, actionable now.**

**Two questions are folded into one identifier, and only one is Thai:**

| Question | Nature | Who can close it |
|---|---|---|
| **Q-A** What must the taxonomy *do* — which distinctions must it make so Accounting, control and Thai statutory evidence are each served? | a **specification** question, answerable from the corpus | SMEs Core |
| **Q-B** Which Thai labels, and is the candidate set complete for how Thai SMEs actually classify losses? | a **user-validation** question (`GAP-FS-11`: no Thai user has validated any label in any round) | a Thai user panel — **not Boss, not SMEs Core, not research** |

### 3.2 Existing Thailand evidence, consulted first (master prompt §10) — including evidence at rest

**Corpus (Layer 1):** R4 `03_L2` rows for adjustment and scrap — reference *"reason: optional"* on
adjustment; scrap carries a configurable *"reason tag list"*, *"the reason is not mandatory anywhere and
no approval gate exists"*; Thai candidate labels for scrap `ตัดสินค้าชำรุด/สูญเสีย` (alternates
`ตัดสินค้าเสีย`, `ทำลาย…`) — **candidate / UNVALIDATED**; `TH-HOLD-02` *destruction evidence where
destruction is claimed for Thai tax purposes* — `HOLD / EVIDENCE REQUIRED`; `TH-R07` adjustment
register; `L7-08` mechanism *"mandatory reason taxonomy; approver distinct from counter"*; scenario 17
*"normal vs abnormal scrap"* (`SA17` row 14 *"normal vs abnormal scrap; cost causality"*);
`SA_CORR3_08` §2.3 element 16 *"an evidence pack exists for scrap only"*.

**Evidence at rest (Layer 2, audit quarantine — neutral aggregates only, no customer data transcribed).**
Instrument declared: PATH SET `~/Downloads/*.dump` + `/Volumes/iMacSys/**/*.dump` + one plain-SQL
export — **declared exclusion:** the rest of `$HOME` (incl. `~/Library`) and the mirror volume were not swept in this pass; the five databases are the ones the programme's own census names (`C5-I-02`); SIGNATURE `PGDMP` header or `PostgreSQL database dump` preamble; TOOL
`/opt/homebrew/opt/postgresql@18/bin/pg_restore 18.6 --data-only --table=<t>` (the host's default
`pg_restore 16.15` refuses archive format 1.16 — `C5-I-02`); IDENTITY keyed on `dbname` from the archive
TOC, **not** on file name (the archive-denominator rule): **four distinct databases, six artefacts**
(`iTEST02` and `iEVING` each appear twice; `CHD-03` — a first draft counted five). UNIT = one row of the scrap-reason configuration table, one
scrap record, one adjustment movement.

| Database (`dbname`) | Generation (installed platform core module version) | Companies | **Configured scrap reasons** | Scrap records | Adjustment movements (the movement record's adjustment marker) | All movements |
|---|---|---:|---:|---:|---:|---:|
| `BK12MAY26` (2026-08-03) | 19.0 | 44 | **0** | 0 | 1,262 | 14,443 |
| `iEVING` (2026-07-23) | 19.0 | 44 | **0** | 0 | 6 | 15 |
| `iEVING` (2026-03-31, plain SQL) | 19.0 | 2 | **0** | 0 | — | — |
| **`iSMEs`** (2026-07-11) | **16.0** | 1 | **0** | **2,286** (2,277 done) | **3,010** | **103,949** |
| `iTEST02` (2026-06-14 and 2026-07-14) | 19.0 | 1 | **0** | 0 | 0 | 57 |

Positive control: the scrap-reason configuration table **exists and is empty** in all six artefacts (an absent
table would fail `--table`; an empty one returns zero data rows after the archive's own preamble lines —
**the two were distinguished by reading the extracted files, not by byte size**, the programme's
*control-that-cannot-detect-its-failure* rule). Coverage **by artefact**: 6 requested / 6 opened / 0 unreadable; by database (identity key `dbname`): 4 of 4. The second `iTEST02` artefact (2026-06-14) returned the same zeros as the first. **The executed commands and their raw outputs are published in Appendix A** with the vendor table names replaced by neutral descriptors (the literal names are Layer 2 and are held in the session scratch evidence only).

> **`C5-07-F-01` — the existing Thailand evidence answers `R4-Q-01` in the negative, and that is an
> answer.** In the one deployed Thai database that scraps at production scale — **2,286 scrap records
> over 103,949 movements, 3,010 adjustments** — **zero reasons are configured and therefore zero are
> used**; the scrap record's free-text source field, the only free-text carrier, is populated on 2,075 rows with **892
> distinct values** — a free-text field, not a classification, and no vocabulary analysis of it was
> performed here. The adjustment-movement record of that generation carries **no reason column at all**
> (0 of its column names contain *reason*). **Thai SMEs on the reference estate do not classify non-sale reductions, because
> the reference never asked them to.** The taxonomy therefore cannot be *discovered* from Thai practice;
> it must be **specified by SMEsPlus (Q-A) and validated by Thai users (Q-B)**. No further research —
> targeted or broad — can change that finding, and none is opened.

### 3.3 Q-A — the taxonomy contract, specified (`M33-A1`)

The pattern is the one the corpus already mandates twice (`MTI-33`'s own context-independence rule;
`CF-I-05`'s platform-owned class + tenant-owned label):

| Clause | Specification |
|---|---|
| **Structure** | A **platform-owned reason *class*** enumeration (context-independent, immutable once used — `CF-I-05` pattern) **plus tenant-configurable reason *labels*** each declaring exactly one class. Controls, accounting consequence and statutory evidence bind to the **class**, never to the label |
| **Mandatory** | A reason (label → class) is **mandatory on every non-sale stock reduction and every count variance application**; absent → the act is refused (`L7-08`; `MTI-20`). *Reference behaviour — reason optional — is expressly not inherited* (`SA12-F-01` clause) |
| **The classes — candidate, derived from the distinctions the corpus requires** | `COUNT_VARIANCE_UNEXPLAINED` (count/adjustment; `L7-08`) · `COUNT_VARIANCE_EXPLAINED` (with sub-reason label) · `DAMAGE` · `EXPIRY` · `THEFT_OR_LOSS` · `QUALITY_REJECT` (link to the quality hold route, `SA_CORR2_03` §3.3) · `PRODUCTION_SCRAP_NORMAL` · `PRODUCTION_SCRAP_ABNORMAL` (scenario 17; the normal/abnormal split is what determines whether the loss stays in inventory cost or is expensed) · `SAMPLE_OR_INTERNAL_CONSUMPTION` · `DESTRUCTION_FOR_TAX` (requires `TH-HOLD-02` destruction evidence — the class exists; the statutory rule attached to it is `HOLD / EVIDENCE REQUIRED`) · `RETURN_TO_VENDOR` (scenario 8) · **`RETURN_FROM_CUSTOMER`** (with sub-labels *restock at value* / *write-off*; scenario 9 — the reason decides re-entry vs loss; `CHC-10`) · `TRANSFER_INTERNAL` (no reduction — carried so transfers are never mislabelled as losses; scenario 14) · **`LANDED_COST_ALLOCATION`** (the allocation basis class on a landed-cost act — row 25 of the matrix, `JT-08`; the sixth of `MTI-33`'s six acts; `CHC-10`) · `OTHER_STATED` (free text mandatory, **reported as an exception class** so it cannot become the default) |
| **Accounting consequence binding** | Each class declares its **cost-consequence class** (stays in inventory cost · expensed as loss · reversed to supplier · no consequence) — the binding Accounting needs for periodic cost-of-sales to exclude non-sale reductions (`05_L4` identity 4). **Which account, and at what value, is `BD-ACC-03A/B` policy plus the COGS residual of `SA_CORR5_10` §3 — not decided here** |
| **Handoff** | The class travels on the emitted fact (element 1 *what happened* qualified; element 16 evidence pack for scrap) |
| **Thai labels** | **All candidate / UNVALIDATED.** The R4 candidates are carried as labels of `DAMAGE`/`DESTRUCTION_FOR_TAX`, unvalidated |
| **Audit** | reason class and label on the `MTI-38` event; a class change on a used label is refused (immutability) |

### 3.4 Q-B — bounded exactly, and it is not a Phase SA gap

| Item | Class | Owner |
|---|---|---|
| Thai label set and completeness of the class set against Thai SME practice | **external user validation** — `GAP-FS-11`, `18_THAI_USER_VALIDATION_CHECKLIST` §6 row `R4-Q-01` | **the panel is Boss's to commission** (`18_THAI_USER_VALIDATION_CHECKLIST` line 11: *"Boss to commission"*) — a Boss act, carried and pre-existing; the validation itself is external, **not** SMEs Core, **not** research (`CHC-04`) |
| `DESTRUCTION_FOR_TAX` statutory evidence rule | `HOLD / EVIDENCE REQUIRED` | Thai Accounting-Tax track |
| Value of a loss (which account, which cost) | COGS residual | `SA_CORR5_10` §3 |

**Status:** `MTI-33` moves from `SA-SPEC-GAP` to **`SA-SPEC-COMPLETE / VALUE HELD / THAI LABEL VALIDATION
PENDING`** — the *structure* is specified, the *labels* await the panel the corpus already routed them
to, and the *value* half was always the COGS residual. **Runtime proof:** `RT-M33-01` a scrap with no
reason class → refused; `RT-M33-02` the same label in two companies resolves to one class;
`RT-M33-03` periodic cost-of-sales excludes every reduction whose class is not a sale.

---

## 4. Tally, and what moved

| Invariant | CORR4 | **CORR5** | Owner of what remains |
|---|---|---|---|
| `MTI-05` | `CONTRADICTED` | **`SA-SPEC-COMPLETE / RUNTIME PROOF REQUIRED — CONDITIONAL (`CF-D-01`, row 17)`** | runtime (store + control); Boss `CF-D-01` for one row |
| `MTI-22` | `SA-SPEC-GAP` (SMEs Core) | **`SA-SPEC-COMPLETE AT REGISTER LEVEL`** — content conditional on `MTI-D-04`, `RC-D-02` (Boss), `JT-10` (joint) | **Boss** (carried, not new) |
| `MTI-33` | `SA-SPEC-GAP` (SMEs Core) | **`SA-SPEC-COMPLETE / VALUE HELD / THAI LABEL VALIDATION PENDING`** | Boss commissions the Thai panel (`GAP-FS-11`); external validation; COGS residual for value |
| `MTI-44` | `SA-SPEC-GAP` | follows `MTI-22` | Boss |

**Targeted Very Deep Research opened: 0.** Two bounded evidence-at-rest passes were executed inside
Workstream G — for `MTI-33` (§3.2) and for `GAP-FS-07` (§2.3) — each declared with instrument, identity
key, coverage by artefact and neutral outputs (Appendix A).

## 5. Residual

1. **The reason-class set (§3.3) is originated here.** Its distinctions are each traceable to a corpus
   requirement; its *completeness* is exactly the Thai-panel question and is not claimed.
2. **`M05-A1` is an adjudication of another body's notation.** The Inventory owner may re-score the
   matrix differently; if it declares a genuinely dual anchor for any of the five rows, `MTI-05` returns
   to `CONTRADICTED` for that row. The patch in §1.4 is stated so that cannot happen silently.
3. **The evidence-at-rest pass is generation-qualified**: four databases are generation 19, one is 16;
   the *absence* of a reason mechanism on adjustments was measured on the generation-16 database's
   movement table and on generation 19's configuration tables. Both agree; neither is the SMEsPlus target.

## 6. Checkpoint

> ## `CP-SA-C5-70 — MTI RESIDUAL SPEC GAPS CLOSED OR EXACTLY BOUNDED`
> **`MTI-05` adjudicated not contradicted (11-row anchor declaration) · `MTI-22` closed at register level,
> content bounded to 2 carried Boss rulings + 1 joint decision · `MTI-33` structure specified (15 classes, covering all six `MTI-33` acts),
> labels bounded to Thai user validation (a Boss commissioning act per `GAP-FS-11`), evidence-at-rest pass over 4 databases / 6 artefacts (`C5-07-F-01`) and the inter-company path traced at data level (`C5-07-F-02`) ·
> 0 TVDR opened · 2 document-owner patches stated · 1 SMEs Core recommendation to Boss on `MTI-D-04`.**

## Appendix A — executed commands and outputs (evidence-at-rest pass), neutral vocabulary

```
# tool
/opt/homebrew/opt/postgresql@18/bin/pg_restore --version      -> pg_restore (PostgreSQL) 18.6 (Homebrew)
pg_restore (16.15) -l <iTEST02 archive>                        -> error: unsupported version (1.16) in file header
# identity (per artefact)
pg_restore -l <archive> | grep 'dbname:'                       -> BK12MAY26 ; iEVING ; iSMEs ; iTEST02 ; iTEST02
# extraction (per artefact, per table)
pg_restore --data-only --table=<scrap-reason-configuration-table>          -f out.sql <archive>
pg_restore --data-only --table=<scrap-record-to-reason link table>         -f out.sql <archive>
pg_restore --data-only --table=<scrap-record table>                        -f out.sql <archive>
pg_restore --data-only --table=<company table>                             -f out.sql <archive>
pg_restore --data-only --table=<movement table>                            -f out.sql <archive>
pg_restore --data-only --table=<location table>                            -f out.sql <archive>
# row count rule (excludes the pg18 \restrict/\unrestrict preamble and COPY framing)
grep -v -E '^(--|SET|SELECT|COPY|\\)' out.sql | grep -v '^$' | wc -l
# adjustment marker: the movement table's boolean adjustment column, counted where = 't'
# cross-company legs: join each movement's two location ids to the location table's company and usage
```

| Artefact | reason rows | link rows | scrap rows | company rows | movement rows | adjustment-marked | transit legs in / out (completed) |
|---|---:|---:|---:|---:|---:|---:|---|
| `BK12MAY26_2026-08-03` | 0 | 0 | 0 | 44 | 14,443 | 1,262 | 2,008 / 2,838 (1,201 / 1,201) |
| `iEVING_2026-07-23` | 0 | 0 | 0 | 44 | 15 | 6 | 2 / 2 (0 / 0) |
| `iEVING_2026-03-31` (plain SQL) | 0 | 0 | 0 | 2 | — | — | — |
| `iSMEs_2026-07-11` | 0 | 0 | 2,286 (2,277 completed) | 1 | 103,949 | 3,010 | 0 / 0 |
| `iTEST02_2026-07-14` | 0 | 0 | 0 | 1 | 57 | 0 | — |
| `iTEST02_2026-06-14` | 0 | 0 | 0 | 1 | — | — | — |

Positive controls: every named table opened in every artefact (an absent table fails `--table`);
`iSMEs` scrap rows fire; the location join reaches 4,846 transit-involved movements in `BK12MAY26`.
Discriminating negative: `iTEST02` (1 company, 57 movements) returns structurally different results
(no transit locations at all) from `BK12MAY26`'s zero cross-company movements.

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
