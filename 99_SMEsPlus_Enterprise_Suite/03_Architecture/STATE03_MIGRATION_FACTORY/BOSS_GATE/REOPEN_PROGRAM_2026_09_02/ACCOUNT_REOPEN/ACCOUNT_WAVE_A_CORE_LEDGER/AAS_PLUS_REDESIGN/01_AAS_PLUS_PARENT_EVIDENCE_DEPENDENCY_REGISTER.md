# 01 — AAS+ PARENT EVIDENCE DEPENDENCY REGISTER

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-AASR-001` · Layer 1 clean-room
**`PROVISIONAL / NON-AUTHORITATIVE / EVIDENCE-CONSUMER MODE`** · AAS+ output is not canonical

> **This is the controlling register of the package.** No design file in `AAS_PLUS_REDESIGN/` is read
> without it. When the parent Very Deep / `L99999.99999` session terminates, **this register is the
> delta-revalidation worklist**: every row is re-tested against the final parent package before any
> design statement is carried forward.

---

## 0. The governing dependency

### `DEP-00` — every citation in this package points at uncommitted parent files

| Field | Content |
|---|---|
| **Design ID** | ALL — governs every row below |
| **Current evidence** | Parent `METHOD_CONVERGENCE_CLOSURE/` is untracked in git; no `mcc` remote branch exists; `MCC_J`, the MCC gate report and the MCC manifest do not exist (`AASR-F-01`) |
| **Parent finding dependency** | The entire parent package, at its final published state |
| **Assumption** | The parent files read on 2026-09-04 reflect findings the parent will retain |
| **Invalidation trigger** | **Any** difference between the copy preserved on this branch and the parent's final published package |
| **Current status** | `EVIDENCE-DEPENDENT` |
| **Required revalidation** | Byte-level diff of the preserved copy against the final parent package; every row below re-tested against the delta. **`MCC_J` has never been read by anyone — it does not yet exist — so no design here has been tested against the parent's own expert and audit challenge** |

> **`DEP-00` alone is sufficient to prevent this package from being canonical.** Everything below is
> conditional on it.

---

## 1. Register — design decisions against parent dependencies

Fields per the Boss containment directive: Design ID · Current Evidence · Parent Finding Dependency ·
Assumption · Invalidation Trigger · Current Status · Required Revalidation.

### 1.1 Event and fact model

| Design ID | Current evidence | Parent finding dependency | Assumption | Invalidation trigger | Status | Required revalidation |
|---|---|---|---|---|---|---|
| `D-01` **Accounting event separated from journal entry** | `L5 §2`; `GAP-B02`; `XM-01`; `MCU-02`/`MCU-03`; `07 AE-register` "events the reference does not have" | `MCU-02`, `MCU-03` remain `GATING — HOLD` | No event-identity carrier exists anywhere in the reference | A carrier **is** found — most plausibly in the **962 manifested modules never searched** (`GB-07`, `MCU-18`) | `PROVISIONAL` | Re-run the event-identity search over the corrected path set including the archive tree |
| `D-24` **Idempotency key on the accounting event** | `XM-01` duplicate posting undetectable; `MCU-34` reclassified **into** gating | `MCU-33`/`MCU-34`/`MCU-35` (concurrency · idempotency · completeness) | Duplicate suppression must be designed, not adapted | Parent finds an existing idempotency mechanism | `PROVISIONAL` | Re-read `MCU-34` disposition in the final package |
| `D-04` **Provenance travels with the fact (`F7`)** | `L5 §1` — `F7` not implemented at all; `EV-017`; `15 §4` five of seven lineages unrecorded | none open | Provenance absence is real, not a search artefact | A provenance carrier is found in the unsearched module tree | `PROVISIONAL` | Same path-set correction as `D-01` |
| `D-03` **Correction is additive, with an explicit correction link** | `ST-09`; `EV-012`; `15 §4` "corrected entry → entry it corrects: **no**" | `BW-35` (wrong reversal lineage — **closed as verified defect**) | The reversal pointer is the sole, unconstrained carrier | `BW-35`'s disposition changes in the final package | `PROVISIONAL` | Confirm `BW-35` survives as `CLOSED — VERIFIED DEFECT` |
| `D-02` **Immutability is unconditional** | `15 §2` — exactly **two** unconditionally immutable things exist | `MCU-01` (are suppression flags externally reachable?) `REMAINS GATING` | Configuration-conditional immutability is the defect | `MCU-01` resolves to "not externally reachable", weakening but not removing the case | `PROVISIONAL` | Re-read `MCU-01` and `MCU-56`-mechanism |
| `D-25` **Maker–checker before posting** | `07` — approval before posting absent; `MCU-08` approval-engine module **rescoped non-gating**, routed to module-baseline decision | `MCU-08` routing | Approval is a SMEsPlus design obligation | The approval engine is confirmed in the SMEsPlus baseline, making this `ADAPT` not `EXTEND` | `PROVISIONAL` | Await the module-baseline decision |

### 1.2 Date, period, close

| Design ID | Current evidence | Parent finding dependency | Assumption | Invalidation trigger | Status | Required revalidation |
|---|---|---|---|---|---|---|
| `D-05` **Seven date concepts separated; accounting date is user-owned** | `C07` — 3 of 7 concepts have **no carrier**; accounting date system-derived; consequence **B** (same-month bills take *today*) newly found | none open in Wave A | The derivation rule as stated in `C07` is complete | A further derivation branch is found | `PROVISIONAL` | Re-read `C07` §2 against the final package |
| `D-26` **Numbering must never influence period attribution** | `C07` consequence **C** — period attribution derived from a numbering format | `T0-08` (entry identity) **UNRESOLVED** | The dependency direction is genuinely inverted | `T0-08` resolution changes the numbering model materially | `PROVISIONAL` | Re-test after `T0-08` closes |
| `D-06` **Period is a first-class object with state** | `12 §2` — no period object; `COR-01` fiscal year fully mutable, no state, no link to any entry | none open | Absence confirmed by re-verification under `COR-01` | — | `PROVISIONAL` | Standard delta check |
| `D-07` **Close is a state the data earns (preconditions enforced)** | `ST-07`; `12 §4`; `EV-008`, `EV-019` | none open | Precondition pattern is transferable | — | `PROVISIONAL` | Standard delta check |
| `D-08` **Reopening is a governed event, never a free backward move** | `12 §2`/`§3` — soft locks move backward freely, no authority, no artefact | `T0-10` cross-company lock-exception creation/revocation **UNRESOLVED** | Reopen governance is separable from lock-exception governance | `T0-10` shows the two are one mechanism | `PROVISIONAL` | **Blocked pending `T0-10`** |
| `D-27` **Grant and revoke of a lock exception require different authority** | `EV-021`, `COR-04` — revocation by the **same role** that granted; `T0-10`: no record rule, caller-supplied company, revocation on group membership alone, then elevated write | `T0-10` **UNRESOLVED**, `MCU-10` `REMAINS GATING` | The exception object is the real lock control | `T0-10` resolves the object out of Wave A scope | `EVIDENCE-DEPENDENT` | **Blocked pending `T0-10` + `MCU-10`** |
| `D-22` **Year-end result transfer** | `12` — retained-earnings transfer never posted; no year-close event exists anywhere | none — this is a **decision**, not a gap | Boss baseline "month 12 is an ordinary month" holds | Boss decides otherwise | `UNKNOWN` — decider is **Boss** | Not a research item |

### 1.3 FX and measurement

| Design ID | Current evidence | Parent finding dependency | Assumption | Invalidation trigger | Status | Required revalidation |
|---|---|---|---|---|---|---|
| `D-09` **Missing rate halts the posting — no par fallback, no undated fallback** | `COR-14`; `CONTRA-08`; `BW-29` undated earliest-rate-ever fallback; `BW-30` opening valued at a 2010 rate | `T0-07` **UNRESOLVED — characterised worse than registered**: 8 raw-SQL reads, three modules, **four** distinct fallback semantics | Every fallback is a defect class, not a convenience | None credible — the evidence strengthened twice | `PROVISIONAL` | Confirm the fourth fallback semantic in the final `T0-07` text |
| `D-10` **Rate scope is tenant + company, never group-root** | `EV-018` rate per company **root**; `GB-03` **PARTIAL**; 20 files / 14 sites / 12 expressions bounded; 6 resolvers admit the company-less row, 6 refuse it | `GB-03` **null-company axis is an unclosed verified defect**, reduced into `GB-01`; `MCU-06`, `MCU-07`, `MCU-19` open | The company-less rate row is reachable and is the live defect | `GB-03`'s open half closes as unreachable | `EVIDENCE-DEPENDENT` | **Blocked pending `GB-03` null-company axis and `GB-01`** |
| `D-30` **Design must be stable across the v18→v19 span** | `GB-08` **NEW**; `MCU-20` — v19 ORM core adds an **eleventh** rate resolver, outside every record rule, converting at **today**, with a **fourth** fallback, reachable from any grouped monetary aggregation | `MCU-20` `GATING` | SMEsPlus targets the v19 line | The target line changes | `EVIDENCE-DEPENDENT` | **No FX conclusion carries into v19 until `MCU-20` closes** |
| ~~`D-23`~~ → **`D-23a`** Assess the **existing** revaluation mechanism before designing | `NC-19` **class `E — CONTRADICTED`**: a post-and-reverse unrealised-FX revaluation mechanism **exists** in the reporting module; `G-C2` adds that it is **user-overridable per currency with a warning** | `NC-19`, `G-C2` | The original `D-23` assumed absence and was wrong | already triggered | **`INVALIDATED` → successor `PROVISIONAL`** | Read the mechanism; re-decide `ADAPT`/`EXTEND`/`REJECT` |
| `D-11` **Realisation is caused by an event; revaluation by a date** | `13 §3` | none open | The distinction is sound and reference-corroborated | — | `PROVISIONAL` | Standard delta check |

### 1.4 Reconciliation

| Design ID | Current evidence | Parent finding dependency | Assumption | Invalidation trigger | Status | Required revalidation |
|---|---|---|---|---|---|---|
| `D-17` **Settlement is hard-bounded by the residual it discharges** | `COR-09`, `RC-01` — nothing prevents over-reconciliation in any currency configuration | none open | Over-reconciliation is structurally reachable | A bound is found elsewhere | `PROVISIONAL` | Standard delta check |
| `D-18` **Settlement facts are immutable and never destroyed by an entry-level operation** | `EV-012`, `RC-02` — matches deleted silently on un-post | `MCU-01` (suppression reachability) | Silent destruction is the defect | — | `PROVISIONAL` | Standard delta check |
| `D-19` **Derived values are never authoritative and must be reconstructible** | `11 §1`; `L5 §3` — residual, reconciled, marker, payment state, ageing all stored-derived; `GAP-E03` open | `GAP-E03` (does any mechanism reconstruct after drift?) — `UNCLASSIFIED` orphan id | Drift is possible because values are stored | `GAP-E03` finds a reconstruction mechanism | `PROVISIONAL` | Resolve `GAP-E03`'s classification — it is one of **5 orphan ids** |
| `D-31` **Cross-company settlement must be refused by default** | `BW-32` a receivable settled by cash that never entered its company; `MCU-22` cross-branch reconciliation + exchange posting + raw-SQL settlement write, guard tests the **root** | `GB-02` **WIDENED TWICE**; `MCU-22` `GATING` | The root-vs-company guard error is real | `GB-02` narrows | `EVIDENCE-DEPENDENT` | **Blocked pending `GB-02`** |

### 1.5 Classification (chart of accounts)

| Design ID | Current evidence | Parent finding dependency | Assumption | Invalidation trigger | Status | Required revalidation |
|---|---|---|---|---|---|---|
| `D-20` **Classification identity is permanent; replacement is succession, never rewrite** | `EV-004`, `COR-08`, `AE-20` — merge retargets posted items, deletes accounts past the ORM's guards, **writes no record of any kind** | none open | Merge destructiveness is as recorded | — | `PROVISIONAL` | Standard delta check |
| `D-21` **Classification carries temporal validity; labels are versioned** | `GAP-A03` — comparative reporting across a chart change unsupported; `L5 §4` no temporal validity anywhere | `GAP-A03` is an **orphan id** (one of 5 unclassified) | Retroactive meaning-change is a real reporting defect | — | `PROVISIONAL` | **Classify `GAP-A03`** before relying on it |
| `D-32` **Control-account status is a governed attribute, not an importable field** | `BW-33` a control-account attribute silently flipped by imported data; `T0-09` **16 company-consistency declarations on the company model do not execute at write** — they generate a client-side field domain, so the control is **present in the view layer and absent at write** (`G-C7`) | `T0-09` **UNRESOLVED** | Declared controls are inert as found | `T0-09` shows an executor exists | `EVIDENCE-DEPENDENT` | **Blocked pending `T0-09`** · apply "prove the executor of every declared control" |
| `D-16` **Template-derived and tenant-created configuration stay distinguishable for the tenant's life** | `16 §4` — **no distinction exists**; `TI-05`; Boss question 16 has **no reference answer** | none open | The distinction must be invented | — | `PROVISIONAL` | Standard delta check. Nothing to adapt — this is `DESIGN CHOICE` throughout |

### 1.6 Tenancy and SaaS boundary

| Design ID | Current evidence | Parent finding dependency | Assumption | Invalidation trigger | Status | Required revalidation |
|---|---|---|---|---|---|---|
| `D-12` **No control-affecting configuration without a tenant dimension** | `SB-01`/`COR-16` — the numbering/date-alignment control has **no company dimension at all**; one write affects every tenant in the database | none open | `SB-01` is as recorded | — | `PROVISIONAL` | Standard delta check |
| `D-13` **No identity encoded by arithmetic over other identities** | `SB-02`/`COR-18` — `account × 10000 + company`, silent aliasing past 10,000 | none open | — | — | `PROVISIONAL` | Standard delta check |
| `D-14` **Tamper-evidence keys on business identity, not storage identity** | `SB-03`/`COR-12`, `CONTRA-07` — hash chain keyed on storage row identifiers cannot survive split, merge, restore or migration | `T0-08` (entry identity) **UNRESOLVED** — empty constraint definition, index scoped by **journal not company**, a wizard that blanks the number to escape the index | The hash must survive the migration it is most needed for | `T0-08` resolution changes entry identity | `EVIDENCE-DEPENDENT` | **Blocked pending `T0-08`** |
| `D-15` **All control evidence, including evidence of destructive acts, is stored inside the tenant's own data** | `SB-04`/`EV-011` — deletion evidence goes to the application log, outside the tenant | none open | — | — | `PROVISIONAL` | Standard delta check |
| `D-33` **Tenant is a first-class identity above company** | `EV-020`, `16 §1` — **no tenant concept exists**; outermost reference boundary is the company group | `GB-01` cross-company / cross-tenant measurement crossing — **Boss decision**, `GB-03`'s open half now reduces into it | Tenant must be introduced above the group | Boss rules the company group *is* the tenant boundary | `EVIDENCE-DEPENDENT` — decider is **Boss** | **Blocked pending `GB-01`** |
| `D-34` **Cross-boundary exposure must be characterised before any isolation claim** | `GB-04`/`MCU-16` — **192 sites bounded, 9 assessed**; and the bound was computed over a path set now known to exclude 962 modules | `GB-04` `REMAINS GATING`; `MCU-18` archive-tree module path `GATING` | — | — | `EVIDENCE-DEPENDENT` | **No tenant-isolation claim may be made until 192/192 is traversed over the corrected path set** |

### 1.7 Migration and continuity

| Design ID | Current evidence | Parent finding dependency | Assumption | Invalidation trigger | Status | Required revalidation |
|---|---|---|---|---|---|---|
| `D-29` **Opening positions carry provenance to their origin** | `EV-017`, `AE-14`; `15 §4` migrated balance → origin: **no**; `BW-30` opening valued at a 2010 rate; `MCU-14` wrong-opening-provenance class | `MCU-14` (taxonomy class, searched — see `MCC_G`) | Opening provenance is absent | — | `PROVISIONAL` | Confirm `MCU-14`'s final disposition |
| `D-35` **A migrated rate row must be revalidated against its company at import** | `MCC-C-R1`; `MCU-19` — constraints are not re-run at upgrade; the feed maintains such a row's rate without re-checking its company | `MCU-19` **NEW GATING** — "one `SELECT` answers it" | The residual is real though `FX-08` itself is `NOT REPRODUCIBLE` | The `SELECT` returns empty across all target databases | `EVIDENCE-DEPENDENT` | **Blocked pending `MCU-19`** — cheapest open item in the set |

---

## 2. Designs already `INVALIDATED` by the parent, retained for lineage

| Design ID | What it was | Invalidating evidence | Note |
|---|---|---|---|
| `D-10a` | *"Branch-scoped rate rows are invisible to their resolver, so rate scope must be redesigned around that composite defect"* — the `FX-08` framing carried by **two prior gate reports** | `MCC_C` / `MCU-13`: writer half **`CONTRADICTED` at three independent layers**; composite defect **`NOT REPRODUCIBLE`** on this build; `BW-16` **withdrawn** | **`INVALIDATED`.** The correct successor is `D-10`, whose driver is the **company-less** row, not the branch row. Recorded because a design built on `FX-08` would have been built on a state that cannot be constructed |

> **`D-10a` is the register's most important row.** A blocker carried as a `VERIFIED DEFECT` through
> two gates was wrong. Any design synthesised before `MCU-13` would have inherited it. This is the
> concrete demonstration that **delta revalidation is mandatory, not ceremonial.**

---

## 3. Design-blocking summary

| Blocking parent item | Status | Designs blocked |
|---|---|---|
| `GB-01` cross-company/tenant crossing | Boss decision | `D-33`, `D-10` |
| `GB-02` cross-company rewrite of a posted fact | **widened twice** | `D-31` |
| `GB-03` null-company rate row | **PARTIAL — open half** | `D-10` |
| `GB-04` / `MCU-16` exposure 9 of 192 | gating | `D-34` |
| `GB-07` / `MCU-18` 962 unsearched modules | gating | `D-01`, `D-04`, `D-23` (all negative-claim exposed) |
| `GB-08` / `MCU-20` v19 instability | gating | `D-30`, and **every FX design** |
| `T0-07` rate fallbacks | unresolved | `D-09` (strengthens it) |
| `T0-08` entry identity | unresolved | `D-14`, `D-26` |
| `T0-09` declared-but-non-executing controls | unresolved | `D-32` |
| `T0-10` lock exception | unresolved | `D-08`, `D-27` |
| `MCU-19` migrated rate rows | new gating | `D-35` |

**11 of 35 designs are `EVIDENCE-DEPENDENT` and blocked. 1 is already `INVALIDATED`. 2 are `UNKNOWN`
pending Boss. 21 stand as `PROVISIONAL` or `PROVISIONAL` — none of them final.**

---

## 4. Delta revalidation procedure — to run when the parent terminates

1. **Stop synthesis.** No further design statement is written until step 5 completes.
2. **Ingest** the final parent package as published (branch + commit + manifest).
3. **Diff** it against the copy preserved on this branch under `DEP-00`. Enumerate every changed,
   added, withdrawn and renamed finding. **Read `MCC_J` first — it has never been read by anyone.**
4. **Re-test every row** in §1 against the delta. Move each design to `INVALIDATED`, revise it, or
   re-affirm it **with the new citation**, never the old one.
5. **Re-run the negative-claim scan** over this package's own text — `D-23`, `D-01` and `D-04` all
   rest on class `B` claims whose boundary is the path set the parent proved wrong.
6. **Only then** restart the AAS+ final redesign synthesis from the verified converged baseline.

> Until step 6 completes: **AAS+ OUTPUT IS NOT CANONICAL.**

---

## 5. REGISTER CLOSURE — parent ids the first draft omitted

> ### `AASR-VETO-01` was raised against this register and is **upheld**: it could not serve as the delta-revalidation worklist while it omitted twenty live parent ids.
>
> These are **backward** contradictions — parent text that already exists and was already in this
> session's evidence base. **Delta revalidation would never have surfaced them**, because it diffs
> against the consumed baseline, and the baseline omitted them. Closing them is the first item of any
> continuation, ahead of and independent of delta revalidation.

### 5.1 Tolerance-zero boundaries `T0-01`…`T0-06` — never enumerated anywhere in the first draft

| Boundary | Bears on | Status |
|---|---|---|
| `T0-01` | `D-02`, `D-18` — `MCU-01`: *"if externally reachable, `T0-01` moves from **defect** to **exploitable**"* | **UNRESOLVED** |
| `T0-02` | `D-09` / `FXD-02` — measurement | **UNRESOLVED** |
| `T0-03` | `D-02`, `D-18`, `D-20`, `DP-05`, `07 §5` — *"deletion or rewrite of a posted accounting fact; covers both the deletion bypass **and the merge**"*; `MCU-56` is *"a rewrite path on a posted fact — `T0-03`"* | **UNRESOLVED** |
| `T0-04` | `D-12`, `D-13`, `D-33`, `D-34`, `L-9`, `T-19` — tenant isolation. `MCU-04`: *"it is a **class**, not an instance, and the class now has two members"* | **UNRESOLVED** |
| `T0-05` | **`D-17`** — over-reconciliation: *"settlement exceeding the obligation"*. **`D-17` is `T0-05`** | **UNRESOLVED** |
| `T0-06` | inherited | **UNRESOLVED** |

**Consequence.** `D-02`, `D-12`, `D-13`, `D-17`, `D-18`, `D-20` were labelled as though nothing bore on
them. All are now `EVIDENCE-DEPENDENT` or `PROVISIONAL` per `AASR-C-01`.

### 5.2 Blockers `GB-05` and `GB-06` — counted, never assessed

| Blocker | Position | Bears on |
|---|---|---|
| `GB-05` | **UNCHANGED — 7 contradicted claims still live in the canonical registers** | **the whole of `02`.** This baseline was reconstructed by reading canonical registers in which seven contradicted affirmative claims still stand. Which `VF-*` rows are exposed is **not yet established** |
| `GB-06` | Channel exists and was demonstrated; **backlog uncleared** | the correction lineage this package relies on |

### 5.3 Gating unknowns `MCU-60` / `MCU-61` — the tenancy foundation

Reverted from `OUT OF SCOPE WITH EVIDENCE` to **`UNKNOWN`, class `B`**: *"neither carries a search
pattern or a path set in **any** file of the parent package. **A not-found presented as a positive
establishment.** `MCU-60` was additionally load-bearing for declaring one population 'unbounded by
construction, not by omission' — **which is circular**."* `MCU-61` is deployment- and hosting-layer
tenancy.

**`VF-15` (*"no tenant concept exists"*) is therefore class `B`, not a `VERIFIED FACT`.** `D-33`'s
foundation moves onto its **positive** evidence — root-keyed rates (`EV-018`), group-shared codes
(`EV-001`), root-only fiscal years (`COR-01`) — which is unaffected.

### 5.4 Boss decisions `CL-01`…`CL-04` — absent from the first draft

| id | Question the parent states **cannot be inferred** |
|---|---|
| `CL-01` | **Is a closed period a record with a closer, a timestamp and a basis — or a date?** Governs `D-06` |
| `CL-02` | close-model decision, carried |
| `CL-03` | close-model decision, carried |
| `CL-04` | **Does a late document post to its own period (requiring reopening) or to the current one (requiring restatement)?** The reference silently chooses the second. Governs `DP-07` |

### 5.5 `TI-07` and `TI-08` — the parent's highest-value structural requirement

| id | Requirement | Status |
|---|---|---|
| **`CR-09`** (= `TI-07`) | Every measurement, classification and control value carries exactly **one** owning boundary, **and every writer and every reader applies the same scoping rule** | the parent's *"single highest-value structural requirement"*; **`D-10` and `D-31` both turn on it** |
| **`CR-10`** (= `TI-08`) | No boundary may be enforced solely in the application layer where a database constraint can express it | corroborates `ADR-02` `B1` |

**`GB-01`'s Boss question is properly stated in `TI-07` terms** — *"a decision on the SMEsPlus boundary
model"* — not the narrower *"is the tenant above the company group?"* the first draft used.

### 5.6 `MCU-02` / `MCU-03` — mis-routed as research

Parent disposition: **`REMAINS GATING — HOLD`, and it is a BOSS DESIGN DECISION, not a research gap.
Cannot be closed by any amount of further research. It is `GB-01`-class.**

`D-01`'s revalidation instruction said *"re-run the event-identity search"*. **Moved to `15 §3`.** The
search remains worth running as supplementary evidence; it cannot settle the question.

### 5.7 `D-28` — a design with no row

| Design ID | Current evidence | Parent dependency | Assumption | Invalidation trigger | Status | Required revalidation |
|---|---|---|---|---|---|---|
| `D-28` **Per dimension: fact (immutable, part of the event) or attribution (restatable)?** | `P-L5 §5` — the reference never makes the distinction explicit, *"which is why analytic attribution can be silently destroyed while the account cannot"* | none — a **business** decision | Management reporting's restatement policy is a business choice | Boss rules | **`UNKNOWN` — decider Boss** | Not a research item. Determines membership of the immutable core at `04 §2` |

### 5.8 `MCD-02` — undeclared id collision

**`MCU-20`, `MCU-21`, `MCU-22` denote two different things in two parent rounds**: five *Boss decisions
on close, period and tenancy* in the convergence round (`NON-GATING`), and three *new gating findings*
in the closure round. The first draft cited all three closure-round meanings without noting the
collision — **losing five parent-registered Boss decisions**, in exactly the areas this package treats
as most blocked.

The package had flagged the strictly milder `BW-16`/`NBW-16` collision as `MCD-01` and missed its own.
**`MCD-02` is raised; renumbering is required before either id range is used as design input.**

---

## 6. Corrected register arithmetic

The first draft stated *"11 of 35 blocked · 1 `INVALIDATED` · 2 `UNKNOWN` · 21 stand"*. **It did not
reproduce.** Recounted mechanically after closure:

| Class | Count |
|---|---|
| `PROVISIONAL` | **19** |
| `EVIDENCE-DEPENDENT` | **11** |
| `UNKNOWN` — decider Boss | **6** (`D-22`, `D-28`, `D-33` in part, `CL-01`→`D-06`, `CL-04`→`DP-07`, `MCU-02`/`03`→`D-01` decision half) |
| `INVALIDATED` | **2** (`D-10a`, `D-23`) |
| **Total design rows** | **38** (`D-01`…`D-35` + `D-10a` + `D-23a` + `D-28`) |
| `STABLE-CANDIDATE` | **0** — the label is unused in this package (`AASR-C-01`) |

**Boss-decision count is stated once, here, and is `6`.** The first draft carried three different
figures in three files (`2`, *"at least 3"*, `6`).
