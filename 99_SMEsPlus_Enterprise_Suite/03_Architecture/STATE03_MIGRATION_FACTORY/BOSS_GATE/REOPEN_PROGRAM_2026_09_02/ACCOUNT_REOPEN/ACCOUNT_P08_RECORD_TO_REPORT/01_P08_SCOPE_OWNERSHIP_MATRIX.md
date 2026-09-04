# P08_SCOPE_OWNERSHIP_MATRIX — Record-to-Report

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · produced under correction `SMEPLUS-26-09-04-ACC-REV2-CORR1`
Layer 1 (clean-room). Benchmark observations are cited in `LAYER2_EVIDENCE_QUARANTINE/`.

Scopes: `PLATFORM` (no tenant, no company context) · `TENANT` (tenant mandatory) · `COMPANY` (tenant **and** company mandatory).
`MISSING REQUIRED SCOPE = DENY` · `REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY`.

Each row answers the eight mandated questions. `SMEsPlus scope` entries are `DESIGN CANDIDATE` unless marked otherwise — this session does not decide them, it evidences them.

## 1. Method note — why the object list is not author-chosen

POPULATION: every accounting model declared in the reference build.
PATTERN: anchored model-name census over the target root, filtered to the accounting namespace, deduplicated (`EV-P-04`)
PATH SET: `REF18` (790 modules).
UNIT: one model.
DENOMINATOR: **131**.

The matrix presents **42 rows**. The relationship between the 131 models, the rows, and the distinct benchmark objects is published below rather than asserted.

**Corrected after independent review.** An earlier draft claimed the 131 collapsed to "29 material objects" and said the collapse was reproducible from a prose exclusion list. **It was not reproducible, and the number was wrong.** A prose list of excluded domains is author-chosen, which the programme's own denominator rule forbids, and the stated count did not tie to the rows presented. The arithmetic is therefore shown in full:

| Step | Count |
|---|---|
| Rows in this matrix | **42** |
| less rows describing an object that **does not exist in the benchmark** — `SC-JE-03` accounting event, `SC-JE-07` provenance, `SC-CL-02` period-as-object, `SC-RP-06b` consolidated statements | −4 |
| rows describing a benchmark object | 38 |
| less **P08 splits** of one benchmark object across several rows — the account (`SC-CA-03`+`04`, −1), the rate table (`SC-FX-02`+`03`+`04`, −2), the statement definition (`SC-RP-01`+`02`+`03`, −2), the counterparty (`SC-SH-01`+`02`, −1) | −6 |
| **distinct benchmark objects covered** | **32** |

The four splits are the substantive output of the scope analysis: each is a place where the benchmark has one object and P08 finds two or three scopes fused inside it.

Excluded from the 32, and recorded as `PEER DEPENDENCY OPEN` rather than decided here: objects owned by another process — analytic, tax computation, asset, payment instrument, bank statement, electronic invoicing, loans, follow-up, banking synchronisation, spreadsheet, import, deferred reporting.

## 2. The matrix

Columns: **OWN** = scope that owns the object · **EXEC** = scope under which the operation executes · **ACC** = scope that may read · **MUT** = scope that may mutate · **REF** = scope that may reference it · **FIN** = creates a financial effect? · **FIN OWNER** = which company owns that effect · **CLASS** = platform reference / tenant-owned / company legal-accounting truth.

### 2.1 Chart and classification

| ID | Object | OWN | EXEC | ACC | MUT | REF | FIN | FIN OWNER | CLASS |
|---|---|---|---|---|---|---|---|---|---|
| `SC-CA-01` | Account classification vocabulary (the 18 classes) | `PLATFORM` | `PLATFORM` | any | `PLATFORM` | any | no | — | platform reference |
| `SC-CA-02` | Statutory chart template for a jurisdiction | `PLATFORM` | `PLATFORM` | any | `PLATFORM` | any | no | — | platform reference |
| `SC-CA-03` | Ledger account — **definition and identity** | `TENANT` | `TENANT` | `TENANT` | `TENANT` | `COMPANY` | no | — | tenant-owned |
| `SC-CA-04` | Ledger account — **number as presented in a set of books** | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | no | — | company legal/accounting |
| `SC-CA-05` | Account grouping / statement hierarchy | `TENANT` | `TENANT` | `TENANT` | `TENANT` | `COMPANY` | no | — | tenant-owned |
| `SC-CA-06` | Control-account designation on an account | `TENANT` | `TENANT` | `TENANT` | `TENANT` | `COMPANY` | no | — | tenant-owned |

`SC-CA-03` vs `SC-CA-04` is the split the benchmark does not make. Benchmark evidence: the account is owned by a *set* of companies while its number is stored keyed by the **root of the company tree**, so every company under one root is forced to one number, and the interface nevertheless presents one number row per company. That is neither `TENANT` nor `COMPANY` — it is a fourth, undeclared "company-group" scope. `FACT VERIFIED`, `EV-COA-06/07`.

Consequence recorded, not decided: if SMEsPlus adopts `SC-CA-03`+`SC-CA-04`, a tenant holds one account definition and each of its companies may carry its own statutory number for that definition. If it adopts a single tenant-wide number, `SC-CA-04` collapses into `SC-CA-03` and per-company statutory numbering becomes impossible. This is a `BOSS CONTROLLED DECISION` — `P08-BD-01`.

### 2.2 Books and the entry

| ID | Object | OWN | EXEC | ACC | MUT | REF | FIN | FIN OWNER | CLASS |
|---|---|---|---|---|---|---|---|---|---|
| `SC-JE-01` | Journal / book of account | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | no | — | company legal/accounting |
| `SC-JE-02` | Journal group (presentation grouping of books) | `TENANT` | `TENANT` | `TENANT` | `TENANT` | `COMPANY` | no | — | tenant-owned |
| `SC-JE-03` | Accounting event *(does not exist in the benchmark)* | `COMPANY` | `COMPANY` | `COMPANY` | none after emission | `COMPANY` | **yes** | the company whose books the event affects | company legal/accounting |
| `SC-JE-04` | Journal entry | `COMPANY` | `COMPANY` | `COMPANY` | none once posted | `COMPANY` | **yes** | the entry's own company | company legal/accounting |
| `SC-JE-05` | Journal item | `COMPANY` | `COMPANY` | `COMPANY` | none once posted | `COMPANY` | **yes** | the parent entry's company | company legal/accounting |
| `SC-JE-06` | Entry numbering series | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | no | — | company legal/accounting |
| `SC-JE-07` | Provenance / lineage of a posted fact *(does not exist in the benchmark)* | `COMPANY` | `COMPANY` | `COMPANY` | none | `COMPANY` | no | — | company legal/accounting |
| `SC-JE-08` | Tamper-evident seal over posted entries | `COMPANY` | `COMPANY` | `COMPANY` | none | `COMPANY` | no | — | company legal/accounting |

`SC-JE-01` is `COMPANY` on business semantics: a book of account is an instrument of a legal entity's records. The benchmark scopes it to the company **tree** — a parent's book is selectable by every descendant company's entries — which is the same undeclared group scope as `SC-CA-04`. That is `CONTRADICTED` against `SC-JE-01` and is carried as `P08-CONTRA-07`.

`SC-JE-08`: a seal chain is `COMPANY` scope by construction, because it asserts a property of one company's records. A chain that spans two companies asserts nothing about either. The benchmark chains on a per-book series and a book is tree-scoped, so a chain can span companies. `P08-CONTRA-08`.

### 2.3 Measurement

| ID | Object | OWN | EXEC | ACC | MUT | REF | FIN | FIN OWNER | CLASS |
|---|---|---|---|---|---|---|---|---|---|
| `SC-FX-01` | Currency (the unit itself) | `PLATFORM` | `PLATFORM` | any | `PLATFORM` | any | no | — | platform reference |
| `SC-FX-02` | Published market rate observation | `PLATFORM` | `PLATFORM` | any | `PLATFORM` | `TENANT`, `COMPANY` | no | — | platform reference |
| `SC-FX-03` | Approved rate policy — which source, which rate type, for which purpose | `TENANT` | `TENANT` | `TENANT` | `TENANT` | `COMPANY` | no | — | tenant-owned |
| `SC-FX-04` | The rate **applied to a posting**, with its date, source, type and provenance | `COMPANY` | `COMPANY` | `COMPANY` | none once posted | `COMPANY` | **yes** | the posting's company | company legal/accounting |
| `SC-FX-05` | Rate purpose dimension (transaction / average / closing / historical) | `PLATFORM` | `PLATFORM` | any | `PLATFORM` | `COMPANY` | no | — | platform reference |
| `SC-FX-06` | Period-end revaluation adjustment | `COMPANY` | `COMPANY` | `COMPANY` | none once posted | `COMPANY` | **yes** | the revalued company | company legal/accounting |

This four-way split is the substantive result of applying the correction to the FX question. The benchmark holds `SC-FX-02`, `SC-FX-03` and `SC-FX-04` in **one table** and applies **four different scoping rules** to it depending on the caller — a writer scoped to the acting company, a resolver scoped to the ancestor company, a report builder that matches the ancestor by strict equality and therefore excludes shared rows, and a caller path that omits the company argument altogether and resolves under whichever company is active. `FACT VERIFIED`, `EV-FX-09/11/15/22`.

Read scope-aware, those are not four bugs. They are **one object being asked to be three scopes at once**. GB-08's `FX-INV-01` (cross-tenant access prohibited) and `FX-INV-02` (cross-company substitution prohibited) apply in full to `SC-FX-04`, and apply **not at all** to `SC-FX-02`, which is platform reference data that every tenant may legitimately read. Recorded as `P08-RQ-FX-01`: the three must be separate objects before either invariant can be enforced without also making published reference rates unusable.

### 2.4 Settlement

| ID | Object | OWN | EXEC | ACC | MUT | REF | FIN | FIN OWNER | CLASS |
|---|---|---|---|---|---|---|---|---|---|
| `SC-RC-01` | Matching record between open items | `COMPANY` | `COMPANY` | `COMPANY` | none once made; undone only by a new fact | `COMPANY` | **yes** (it emits difference entries) | the company of the matched items — which must be one company | company legal/accounting |
| `SC-RC-02` | Derived settlement state (residual, ageing, payment state) | `COMPANY` | `COMPANY` | `COMPANY` | derived only | `COMPANY` | no | — | company legal/accounting |
| `SC-RC-03` | Automatic matching rule | `TENANT` | `TENANT` | `TENANT` | `TENANT` | `COMPANY` | no | — | tenant-owned |
| `SC-RC-04` | Difference entry emitted by settlement | `COMPANY` | `COMPANY` | `COMPANY` | none once posted | `COMPANY` | **yes** | the settling company | company legal/accounting |

`SC-RC-01`'s `FIN OWNER` cell states the invariant: a matching record has exactly one owning company, because it emits a posting and a posting is owned by one company. Prior evidence records that the benchmark's matching record carries **no isolation rule at all** and performs no company check on creation. Under the corrected model that is a `REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY` case. `P08-T0-04`.

### 2.5 Calendar and finality

| ID | Object | OWN | EXEC | ACC | MUT | REF | FIN | FIN OWNER | CLASS |
|---|---|---|---|---|---|---|---|---|---|
| `SC-CL-01` | Fiscal calendar definition | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | no | — | company legal/accounting |
| `SC-CL-02` | Accounting period as an object *(does not exist in the benchmark)* | `COMPANY` | `COMPANY` | `COMPANY` | state transitions only | `COMPANY` | no | — | company legal/accounting |
| `SC-CL-03` | Finality declaration (the close itself) | `COMPANY` | `COMPANY` | `COMPANY` | forward only | `COMPANY` | no | — | company legal/accounting |
| `SC-CL-04` | Relaxation of a finality declaration (derogation) | **`TENANT` or above grants**; `COMPANY` may request, never self-grant | `COMPANY` | `TENANT` | **not `COMPANY`** | `COMPANY` | no | — | tenant control over a company act |
| `SC-CL-05` | Retention / audit-trail policy | `PLATFORM` **floor**, immutable downward; `COMPANY` may **extend only** | `PLATFORM`/`TENANT` | `TENANT` | `PLATFORM`/`TENANT` sets the floor; `COMPANY` may lengthen | `COMPANY` | no | — | platform floor over a company obligation |

`SC-CL-01` is `COMPANY` because a fiscal year is a legal attribute of a legal entity. The benchmark delegates it to the root of the company tree, so a subsidiary cannot hold its own year-end. For a platform whose tenants include groups with differing statutory year-ends per entity, that is an over-constraint in the benchmark, not in SMEsPlus. `P08-CONTRA-09`.

`SC-CL-04` was re-assigned after independent review. The draft made the derogation `COMPANY`-owned and `COMPANY`-mutable, with the tenant allowed only to audit. The reviewer applied this package's **own** argument for retention to it, and it holds: granting and revoking a derogation are the same authority; the widest grant available produces **no record at all**; and the derogation's own audit trail depends on a company-level switch with no default. A company administrator can therefore grant themselves an unbounded, unrecorded reopen and switch off the log that would show it. Under the corrected model that is a scope *decision*, not a defect — so the decision is corrected: **the grant sits above the company.**

`SC-CL-05` is the one row where the correction **loosens** nothing and **tightens** something.

**The draft's stated attack path is withdrawn — it is contradicted.** The draft argued that "an administrator who can switch retention off can erase the evidence of their own erasure". Independent review found, and P08 verified, that the option **cannot be disabled once any entry exists for the company** — a constraint refuses it. That path does not exist.

**The requirement survives on the stronger and different ground the draft also recorded:** the option is **off by default**, so an installation that never enabled it never needs to disable it, and on that installation a forced deletion of a posted entry leaves no record of any kind. Reasoning from the default, not from a disable path, is the correct basis, and the row's assignment is unchanged. Placing it at `PLATFORM` (or at `TENANT` with no path to disable once any entry exists) is `P08-RQ-CL-01`, and it is a tolerance-zero candidate, `P08-T0-05`.

**Refined after independent review:** the direction of the tightening is right, but excluding `COMPANY` outright was wrong. A retention period is an obligation of a legal entity, and entities inside one tenant may face different ones. The rule is therefore a **platform floor that a company may extend and may never shorten**.

### 2.6 Reporting

| ID | Object | OWN | EXEC | ACC | MUT | REF | FIN | FIN OWNER | CLASS |
|---|---|---|---|---|---|---|---|---|---|
| `SC-RP-01` | Statutory statement layout for a jurisdiction | `PLATFORM` | `PLATFORM` | any | `PLATFORM` | `TENANT`, `COMPANY` | no | — | platform reference |
| `SC-RP-02` | Tenant's own management statement layout | `TENANT` | `TENANT` | `TENANT` | `TENANT` | `COMPANY` | no | — | tenant-owned |
| `SC-RP-03` | A produced statement (a run, for a company, for a period) | `COMPANY` | `COMPANY` | `COMPANY` | none once issued | `COMPANY` | no | — | company legal/accounting |
| `SC-RP-04` | Externally supplied / manually entered statement value | `COMPANY` | `COMPANY` | `COMPANY` | authorised restatement only | `COMPANY` | **yes in effect** — it changes a reported figure without a posting | the reported company | company legal/accounting |
| `SC-RP-05` | Carried-forward value materialised at close | `COMPANY` | `COMPANY` | `COMPANY` | none | `COMPANY` | **yes in effect** | the reported company | company legal/accounting |
| `SC-RP-06a` | **Management** multi-company aggregation | `TENANT` | `TENANT` | `TENANT` | derived only | `TENANT` | no | — | tenant-owned derivation |
| `SC-RP-06b` | **Consolidated financial statements** | `COMPANY` (the consolidating parent) | `COMPANY` | `COMPANY` | eliminations and translation adjustments as company-scope posted facts | `COMPANY` | **yes** | the consolidating parent | company legal/accounting |
| `SC-RP-07` | **Statutory jurisdiction filing output** (a return or extract bearing a legal identity) | `COMPANY` | `COMPANY` | `COMPANY` | none once filed; layout is `PLATFORM` | `COMPANY` | **yes in effect** | the filing company | company legal/accounting |

`SC-RP-01`/`SC-RP-02` versus `SC-RP-03` is the second split the benchmark does not make. The benchmark's statement definitions carry **no company dimension and no isolation rule**, and one ordinary accounting role holds full create/update/delete on them with no change history. In a single-tenant deployment that is a configuration surface. In a shared multi-tenant deployment it is a cross-tenant surface, because the object that decides what every tenant's balance sheet says is owned by nobody. `FACT VERIFIED`, `EV-RPT-17`. Under the corrected model the resolution is not "add a company id" — it is that a **statutory layout is platform reference data that tenants must not be able to edit at all**, while a **management layout is tenant-owned**. `P08-RQ-RP-01`.

`SC-RP-04` carries `FIN = yes in effect` deliberately. It is not a posting, and no ledger control reaches it, yet it changes the number a statement reports. Any control model that protects the ledger and ignores this object protects the wrong thing. `P08-T0-06`.

`SC-RP-06a` is `TENANT` scope and is a **derivation**, never a store. A consolidated figure is not owned by any company, so it cannot be a company-scope fact; and it must never be writable, because a writable consolidated figure would be a financial assertion with no owning company — a `REQUIRED OWNERSHIP CANNOT BE PROVEN` case.

### 2.7 Shared reference data that the ledger depends on

| ID | Object | OWN | EXEC | ACC | MUT | REF | FIN | FIN OWNER | CLASS |
|---|---|---|---|---|---|---|---|---|---|
| `SC-SH-01` | Counterparty (customer/supplier identity) | `TENANT` | `TENANT` | `TENANT` | `TENANT` | `COMPANY` | no directly | — | tenant-owned |
| `SC-SH-02` | Counterparty **as recorded on a posted fact** | `COMPANY` | `COMPANY` | `COMPANY` | none once posted | `COMPANY` | **yes** — it is part of the fact | the posting's company | company legal/accounting |
| `SC-SH-03` | Payment terms | `TENANT` | `TENANT` | `TENANT` | `TENANT` | `COMPANY` | no | — | tenant-owned |
| `SC-SH-04` | Rounding profile | `TENANT` | `TENANT` | `TENANT` | `TENANT` | `COMPANY` | no | — | tenant-owned |
| `SC-SH-05` | System configuration parameter store | `PLATFORM` | `PLATFORM` | `PLATFORM` | `PLATFORM` | — | no | — | platform reference |

`SC-SH-01` versus `SC-SH-02` is the third and most consequential split, and it is the one that explains a defect prior rounds recorded but could not classify.

The benchmark treats the counterparty as one object. Consolidating two counterparty records — an ordinary customer-data operation, available to a contacts role, not an accounting role — rewrites the counterparty **on posted journal items**, across every company, with the period-lock check explicitly suppressed. `FACT VERIFIED`, `EV-KRN-09`, independently reproduced by this session.

Scope-aware, the diagnosis is exact: `OWNERSHIP ≠ AVAILABILITY`. The counterparty *master record* is legitimately `TENANT` scope and legitimately mutable by a tenant role. The counterparty *as a component of a posted financial fact* is `COMPANY` scope and immutable. The benchmark lets a mutation at `TENANT` scope reach through and rewrite objects at `COMPANY` scope. Every such reach-through is a scope violation regardless of whether the underlying edit was reasonable. `P08-T0-07`, and the general form is `P08-RQ-SH-01`: **a tenant-scope mutation may never rewrite a company-scope posted fact; it may only add a new company-scope fact.**

`SC-SH-05`: the benchmark's parameter store has no tenant or company dimension for any key it holds, and at least one accounting control is read from it. One write disables that control for every tenant in a shared database. Under the corrected model the store is correctly `PLATFORM`; the error is that **tenant and company policy is being kept in it**. `P08-RQ-SH-02`.

## 3. Scope-violation classes found

Applying the model to the benchmark yields five recurring violation shapes. They are stated as classes, because prior rounds' experience in this programme is that enumerating instances understates the population.

| Class | Shape | Instances found in P08 |
|---|---|---|
| `SV-1` | An object is given an **undeclared group scope** between tenant and company | `SC-CA-04`, `SC-JE-01`, `SC-JE-06` (the numbering series, which the seal chain orders on), `SC-CL-01`, and the **rate master** behind `SC-FX-02`/`SC-FX-03` |
| `SV-2` | **One object serves several scopes**, with different callers applying different rules | `SC-FX-02/03/04` (four rules, one table) |
| `SV-3` | A **tenant-scope mutation reaches through and rewrites a company-scope posted fact, or silently changes a company-scope issued statement** | `SC-SH-02`; `SC-CA-03`→`SC-CA-04` re-coding; account consolidation; **statement-layout and grouping edits restating an issued statement**; **an account flag change rewriting stored open amounts by direct database statement** |
| `SV-4` | An object with a **financial effect has no owning company** | `SC-RC-01` (matching record with no isolation rule), `SC-RP-04` (manual statement value) |
| `SV-5a` | **Tenant or company policy stored at platform scope** — remediation: move the policy down to its owning scope | `SC-SH-05` |
| `SV-5b` | **Platform or tenant policy left to company discretion** — remediation: move the policy up | `SC-CL-05` (retention), `SC-CL-04` (derogation grant) |
| `SV-6` | **Ownership taken from the ambient session context** rather than from the object whose ownership is at stake | `FX-07` (conversion resolves under the active company, not the fact's company); the statutory extract's filer identity and its very availability; a statutory filing's rounding precision; two custom withholding objects capturing ownership from the ambient company |

`SV-4` is the class that maps directly onto the correction's `REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY`. Every `SV-4` instance is a tolerance-zero candidate by construction.

`SV-6` was **added after independent review** and is the class that maps onto the correction's second denial rule most directly: ambient-context ownership is ownership *assumed* rather than *proven*. It is distinct from `SV-2` — in `SV-2` one object serves several scopes; in `SV-6` the object has exactly one correct scope and the code selects the wrong **instance** of it. `FX-07` was previously filed under `SV-2`, which lost the diagnosis, and is re-filed here.

## 4. Findings materially affected by the withdrawn "tenant+company everywhere" reading

Recorded in full, with the six mandated columns, in `21_P08_REVISION_LOG.md` §2. Summary of the affected set:

| Finding | Was classified | Now classified |
|---|---|---|
| "No tenant dimension exists on the currency or rate model" | gap against a mandatory tenant context | **not a gap for `SC-FX-01/02/05`** (platform reference, correctly tenant-free); a gap only for `SC-FX-03/04` |
| "No tenant dimension on the report definition models" | gap | **not a gap for `SC-RP-01`** (platform reference); a gap for `SC-RP-02`, and a tolerance-zero issue for `SC-RP-03/04` |
| "Shared master data is not company-isolated" (counterparty, terms, rounding, currency) | leak surface | **correct at `TENANT` scope**; the defect is the reach-through of `SV-3`, not the sharing itself |
| "The parameter store has no company dimension" | leak | **correct at `PLATFORM` scope**; the defect is `SV-5` — accounting policy kept there |
| GB-08 facets `1a` and `4d`, previously scored `SILENT` because no tenant concept exists | silent | re-scored: `SILENT` stands for `SC-FX-02` and `SC-FX-05`; becomes **`VIOLATES`** for `SC-FX-04`, where a posted financial fact must carry its owning tenant and company and does not |

Nothing in the posting-engine, entry-identity, close-mechanism or report-derivability finding sets was materially affected. Those were **not** re-run. Their evidence, citations and lineage are preserved unchanged.

## 5. Unresolved scope questions

| ID | Question | State |
|---|---|---|
| `P08-SC-U-01` | Whether a single tenant may contain companies with different statutory fiscal year-ends | `HOLD — SCOPE EVIDENCE REQUIRED`; determines whether `SC-CL-01` may be delegated upward |
| `P08-SC-U-02` | Whether `SC-CA-04` (per-company account number) is required by Thai statutory reporting | `HOLD / EVIDENCE REQUIRED` — statutory, routed to the Accounting-Tax track, not decidable here |
| `P08-SC-U-03` | Whether a tenant may author a statutory statement layout, or only a management one | `BOSS CONTROLLED DECISION` `P08-BD-02` |
| `P08-SC-U-04` | Whether intercompany settlement within one tenant is in scope at all, and if so which company owns the matching record | `PEER DEPENDENCY OPEN` — P01/P02 boundary |
| `P08-SC-U-05` | Whether the platform itself may hold a rate source, or whether every tenant must supply its own | `BOSS CONTROLLED DECISION` `P08-BD-03`; GB-08 froze resolution, not sourcing |
