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

### 1.2 What R2 did and did not change

`CD-04` (Product, row 5) and `CD-12` (Product category, row 7) re-anchored both `X / Y` rows to
**`company`** — the R2 register's own note: *"Row 5 was the only row in the matrix declaring two anchors
for one object, which sat awkwardly against `MTI-05`."* **The two slash rows are gone. The five
`company + X` rows are untouched by R2, and they are the whole of the residual:**

| Row | Object | R1 anchor cell | Where its company actually comes from (primary text) |
|---:|---|---|---|
| 8 | Lot / Serial (`CN-17`/`-18`) | `company + product` | **Identity** is `(tenant, company, product, value)` (`MTI-12`; `09` §2 `L8-10`/`-11` *"company … Creation"*). Under `MTI-D-01` Option B the product is **company-anchored** (`CD-04`), so a lot's company is its product's company. **One ancestor: the product** |
| 13 | Reordering rule (`CN-20`) | `company + location` | a rule is defined at a location; **location → warehouse → company** (`MTI-08`: location company *derived from the warehouse*, structural) |
| 14 | Put-away rule | `company + location` | same chain |
| 22 | Adjustment / count session (`CN-28`/`-27`) | `company + location` | `09` §2 `L8-13`: *"company plus number"*; the act executes at a location — **location → warehouse → company** |
| 23 | Scrap (`CN-29`) | `company + location` | `L8-14` *"company plus number"*; same chain |

And the matrix's own legend, §1: *"**Anchor** — the single authoritative ancestor from which `company`
derives (`MTI-05`)."* Row 4 (Location) reads anchor **`warehouse`** — single — and row 10 (Operation
type) reads **`warehouse`**. **The convention of the matrix is a single ancestor; the `company + X` form
appears on exactly the rows whose canonical *identity tuple* carries `company` explicitly** (lot,
adjustment number, scrap number). The notation records **identity composition**, not dual derivation.

> ### Adjudication `M05-A1`
> **Reading (i) governs.** `company + X` in the R1 matrix means *"company, stored on the record and
> derived via the single ancestor X"* — which is exactly what `MTI-05` requires: **one declared
> ancestor, the derived value stored, a control asserting stored = derived.** The five rows honour the
> invariant. **`MTI-05` is not contradicted; the matrix's notation was ambiguous in the one column where
> it could least afford to be, and this file is the declared reading.**

### 1.3 The declared anchor table — the Phase SA controlled reading for the nine affected rows

| Row | Object | **Declared single anchor** | Company stored on record | Note |
|---:|---|---|:---:|---|
| 5 | Product | **company** (`CD-04`) | ✔ | R2 |
| 7 | Product category | **company** (`CD-12`) | ✔ | R2; costing facet `HOLD — see §3 of `SA_CORR5_10`` |
| 8 | Lot / Serial | **product** | ✔ | identity tuple carries company |
| 13 | Reordering rule | **location** | ✔ | |
| 14 | Put-away rule | **location** | ✔ | |
| 22 | Adjustment / count session | **location** (the counted/adjusted location) | ✔ | a count spanning several locations of one warehouse anchors to the warehouse; **never two companies** (`MTI-33`) |
| 23 | Scrap | **source location** | ✔ | |
| 1 | Tenant | **root — legitimately anchorless** | n/a | `INV-PR-07` agrees |
| 26 | Inter-company transfer | **not an object — an `MTI-22` relationship** between two single-context facts, each anchored to its own movement document (`XCR-01`) | n/a each | `INV-PR-07` listed it as *no anchor*; it has none because it is not a record |

The other 26 rows are single-anchored and unchanged. **35 of 35 rows now carry exactly one declared
anchor or a stated reason for none.**

### 1.4 Status, downstream impact, and the document-owner correction

| Item | Before | After |
|---|---|---|
| `MTI-05` | `CONTRADICTED` (CORR4) | **`SA-SPEC-COMPLETE / RUNTIME PROOF REQUIRED`** — the declaration half is closed by §1.3; the store-and-control half was always runtime (`CORR3` `M-2`) |
| `CF-I-07` (inherits `MTI-05`) | inherited the contradiction | inherits the closure; stays `SPECIFIED — CONDITIONAL (RC-D-02)` on its own ground |
| `HF-CTX-05` anchor path | — | for the five rows the anchor path is *record → X → … → company*, one chain each |
| R1 matrix `04_CONTEXT_OWNERSHIP_AND_VISIBILITY_MATRIX.md` | notation ambiguous | **document-owner correction (Inventory), stated as a patch:** replace `company + product` / `company + location` in the `Anchor` column of rows 8, 13, 14, 22, 23 with `product` / `location` and add a legend line *"company is stored on every record; the Anchor column names the ancestor it derives from."* **Non-material once this file is the controlled reading** (`SA_CORR5_14` §3) |

**Evidence basis:** R1 matrix §1 legend and rows 4, 8, 10, 13, 14, 22, 23; `MTI-08`, `MTI-12`;
`09` §2 rows `L8-10`…`L8-14`; R2 `CD-04`, `CD-12`; `SA_CORR3_07` §6.1 (both readings, unresolved).
**Runtime proof:** `RT-M05-01` stored ≠ derived on any of the five object types → `MTI-19` breach fires
(synthetic injection `0 → 1`).

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
export; SIGNATURE `PGDMP` header or `PostgreSQL database dump` preamble; TOOL
`/opt/homebrew/opt/postgresql@18/bin/pg_restore 18.6 --data-only --table=<t>` (the host's default
`pg_restore 16.15` refuses archive format 1.16 — `C5-I-02`); IDENTITY keyed on `dbname` from the archive
TOC, **not** on file name (the archive-denominator rule): **five distinct databases, six artefacts**
(`iTEST02` appears twice, a month apart). UNIT = one row of the scrap-reason configuration table, one
scrap record, one adjustment movement.

| Database (`dbname`) | Generation (installed `base`) | Companies | **Configured scrap reasons** | Scrap records | Adjustment movements (`is_inventory`) | All movements |
|---|---|---:|---:|---:|---:|---:|
| `BK12MAY26` (2026-08-03) | 19.0 | 44 | **0** | 0 | 1,262 | 14,443 |
| `iEVING` (2026-07-23) | 19.0 | 44 | **0** | 0 | 6 | 15 |
| `iEVING` (2026-03-31, plain SQL) | 19.0 | 2 | **0** | 0 | — | — |
| **`iSMEs`** (2026-07-11) | **16.0** | 1 | **0** | **2,286** (2,277 done) | **3,010** | **103,949** |
| `iTEST02` (2026-06-14 and 2026-07-14) | 19.0 | 1 | **0** | 0 | 0 | 57 |

Positive control: the scrap-reason configuration table **exists and is empty** in all five (an absent
table would fail `--table`; an empty one returns zero data rows after the archive's own preamble lines —
**the two were distinguished by reading the extracted files, not by byte size**, the programme's
*control-that-cannot-detect-its-failure* rule). Coverage: 5 requested / 5 opened / 0 unreadable.

> **`C5-07-F-01` — the existing Thailand evidence answers `R4-Q-01` in the negative, and that is an
> answer.** In the one deployed Thai database that scraps at production scale — **2,286 scrap records
> over 103,949 movements, 3,010 adjustments** — **zero reasons are configured and therefore zero are
> used**; the scrap `origin` field, the only free-text carrier, is populated on 2,075 rows with **892
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
| **The classes — candidate, derived from the distinctions the corpus requires** | `COUNT_VARIANCE_UNEXPLAINED` (count/adjustment; `L7-08`) · `COUNT_VARIANCE_EXPLAINED` (with sub-reason label) · `DAMAGE` · `EXPIRY` · `THEFT_OR_LOSS` · `QUALITY_REJECT` (link to the quality hold route, `SA_CORR2_03` §3.3) · `PRODUCTION_SCRAP_NORMAL` · `PRODUCTION_SCRAP_ABNORMAL` (scenario 17; the normal/abnormal split is what determines whether the loss stays in inventory cost or is expensed) · `SAMPLE_OR_INTERNAL_CONSUMPTION` · `DESTRUCTION_FOR_TAX` (requires `TH-HOLD-02` destruction evidence — the class exists; the statutory rule attached to it is `HOLD / EVIDENCE REQUIRED`) · `RETURN_TO_VENDOR` (distinguishes a return from a loss; scenario 8) · `TRANSFER_INTERNAL` (no reduction — carried so transfers are never mislabelled as losses; scenario 14) · `OTHER_STATED` (free text mandatory, **reported as an exception class** so it cannot become the default) |
| **Accounting consequence binding** | Each class declares its **cost-consequence class** (stays in inventory cost · expensed as loss · reversed to supplier · no consequence) — the binding Accounting needs for periodic cost-of-sales to exclude non-sale reductions (`05_L4` identity 4). **Which account, and at what value, is `BD-ACC-03A/B` policy plus the COGS residual of `SA_CORR5_10` §3 — not decided here** |
| **Handoff** | The class travels on the emitted fact (element 1 *what happened* qualified; element 16 evidence pack for scrap) |
| **Thai labels** | **All candidate / UNVALIDATED.** The R4 candidates are carried as labels of `DAMAGE`/`DESTRUCTION_FOR_TAX`, unvalidated |
| **Audit** | reason class and label on the `MTI-38` event; a class change on a used label is refused (immutability) |

### 3.4 Q-B — bounded exactly, and it is not a Phase SA gap

| Item | Class | Owner |
|---|---|---|
| Thai label set and completeness of the class set against Thai SME practice | **external user validation** — `GAP-FS-11`, `18_THAI_USER_VALIDATION_CHECKLIST` §6 row `R4-Q-01` | Thai user panel (PMO convenes); **not** Boss, **not** SMEs Core, **not** research |
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
| `MTI-05` | `CONTRADICTED` | **`SA-SPEC-COMPLETE / RUNTIME PROOF REQUIRED`** | runtime (store + control) |
| `MTI-22` | `SA-SPEC-GAP` (SMEs Core) | **`SA-SPEC-COMPLETE AT REGISTER LEVEL`** — content conditional on `MTI-D-04`, `RC-D-02` (Boss), `JT-10` (joint) | **Boss** (carried, not new) |
| `MTI-33` | `SA-SPEC-GAP` (SMEs Core) | **`SA-SPEC-COMPLETE / VALUE HELD / THAI LABEL VALIDATION PENDING`** | Thai user panel (external validation); COGS residual for value |
| `MTI-44` | `SA-SPEC-GAP` | follows `MTI-22` | Boss |

**Targeted Very Deep Research opened: 0.** One bounded evidence-at-rest pass was executed inside
Workstream G for `MTI-33` only, and it closed the question by showing the answer is not in Thai practice.

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
> **`MTI-05` adjudicated not contradicted (9-row anchor declaration) · `MTI-22` closed at register level,
> content bounded to 2 carried Boss rulings + 1 joint decision · `MTI-33` structure specified (13 classes),
> labels bounded to Thai user validation, evidence-at-rest pass over 5 databases (`C5-07-F-01`) ·
> 0 TVDR opened · 2 document-owner patches stated · 1 SMEs Core recommendation to Boss on `MTI-D-04`.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
