# E00 — PRIMARY EVIDENCE BASE (LAYER 2 — AUDIT QUARANTINE)

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001
**Process:** P09 — Plan-to-Analyze (Management Accounting / Analytic / Budget)
**Classification:** LAYER 2 — AUDIT QUARANTINE. Boss / PMO / AI-Audit only.
**Prohibition:** No identifier, path, model name, method name or code fragment in this file may be transcribed into any Layer 1 deliverable. Layer 1 registers cite `EV-P09-xxx` identifiers only.

---

## 0. DENOMINATOR DECLARATION

Per the project denominator rule, a denominator is `POPULATION + PATTERN + PATH SET + UNIT`, and none of the four may be chosen by the author of the claim it bounds. All four are declared here before any finding is stated.

### 0.1 PATH SET (proved by enumeration, not by habit)

| Root | Path | Module count (`__manifest__.py`) | Analytic surface present |
|---|---|---|---|
| R1 | `<ref-erp>/odoo/addons/` | 790 | YES |
| R2 | `<ref-erp>/odoo/addons_archive/` | 959 (511 non-duplicate + 448 `__dup_` copies) | NOT FOUND IN SCOPE |
| R3 | project custom addon set, copy A | **65 modules** (68 directory entries; 3 are archive files, not modules) | partial (2 modules) |
| R4 | project custom addon set, copy B | **57 modules** (57 entries) | partial (2 modules) |
| R5 | project custom addon set, copy C | **47 modules** (50 directory entries; 3 are archive files, not modules) | partial (1 module) |
| R6 | nested vendored root inside a POS tooling directory of R1 | 1 | NOT FOUND IN SCOPE |

Total manifests across all roots enumerated: **1,753**.

**EV-P09-001 — The reference source tree carries a second, larger addons root.** `R2` holds 959 manifests against `R1`'s 790, of which 448 are timestamp-suffixed duplicate copies of modules also present under `R2`. Any enumeration that searched only `R1` has an undeclared 959-module blind spot. For this session the blind spot was tested rather than assumed: the analytic-surface pattern (§0.2 P1) returns **zero** hits in `R2`, so `R2` is excluded from the analytic population *by measurement*. Class **A (verified absence within stated scope: pattern P1 over R2)**.
Command: `grep -rln "analytic\.mixin" <R2> --include="*.py"` → 0 results.

**EV-P09-002 — Which custom copy is deployed is unknown.** Three custom addon roots exist with overlapping but non-identical module sets (65 / 57 / 47 modules). At least one analytic-relevant custom module is present in two of the three and absent from the third. No evidence in scope identifies which copy is the deployed one. Class **D (unknown)**. This is carried as a dependency, not a finding.

### 0.2 PATTERN (selecting expressions, with declared false-negative modes)

| ID | Pattern | Selects | Known false-negative mode |
|---|---|---|---|
| P1 | `analytic\.mixin` | models that carry an analytic distribution | misses models that carry analytic by a plain many2one instead of the mixin |
| P2 | `account\.analytic\.line` | modules that read or write analytic lines | misses writes performed through a variable-held model name |
| P3 | `analytic_distribution` | field-level carriers and readers | misses SQL-only access that spells the column directly |
| P4 | `analytic_account_id` \| `auto_account_id` \| `_column_name\(\)` | plan-column access | misses dynamic column names built at runtime |
| P5 | `*budget*` at module-name depth 1 | budget modules | misses budget behaviour implemented inside a non-budget module |

P1–P5 were each run over **R1 and R2**; P1 and the custom-module patterns were additionally run over R3–R5.

**Declared limitation:** P1 was the primary population selector. Its false-negative mode (a model carrying analytic by plain many2one) is **real and materialised** — see EV-P09-020, where a budget line carries analytic through the plan-column mixin and not through P1. The population in §0.3 is therefore stated as *the P1 population*, and the P4 population is stated separately. Neither is presented as "the complete set of analytic carriers in the system".

### 0.3 POPULATION

**P1 population — distribution carriers (R1, tests excluded): 10 concrete models + 1 abstract mixin.**

| # | Carrier | Kind |
|---|---|---|
| 1 | journal item | financial ledger row |
| 2 | bank-reconciliation widget line | transient UI row |
| 3 | reconciliation model | **rule / master data** |
| 4 | sales order line | commercial document |
| 5 | purchase order line | commercial document |
| 6 | purchase requisition line | commercial document |
| 7 | expense | commercial document |
| 8 | expense split wizard | transient wizard |
| 9 | fixed asset | asset master record |
| 10 | work centre | **manufacturing master data** |
| 11 | analytic distribution model | **rule / master data** (the rule carries a distribution as its payload) |

**P4 population — plan-column carriers:** the analytic line itself, and the budget line (§ EV-P09-020). These carry analytic as one many2one *per plan*, not as a distribution.

### 0.4 UNIT

One population member = **one persisted model that can hold an analytic assignment**. Not one field, not one call site, not one menu. Where a claim counts something else (call sites, SQL statements, record rules) the unit is restated at the claim.

---

## 1. THE ANALYTIC DIMENSION IS SCHEMA, NOT DATA

**EV-P09-010 — Creating an analytic plan performs DDL on a shared table.**
A root plan materialises as a **physical column** on every model that carries plan columns. The column name is derived from the plan's own database id; one privileged plan is mapped to a fixed column name and every other root plan to a generated one. Creating the plan creates a custom field record, the column, and a partial btree index on it.
Source: analytic plan model, column-name resolver and column-sync routine; index creation is explicit in the sync routine.
Consequence: the analytic dimension *set* is part of the database schema, not part of tenant data.

**EV-P09-011 — Deleting a plan drops the column, and with it every historical value in that dimension.**
The plan's `unlink` first unlinks the custom field record for its column, then deletes the plan. Dropping the field drops the column; all historical analytic-line values recorded in that dimension are removed with it. No archival, no export, no confirmation beyond ordinary delete rights.
Source: analytic plan model `unlink`, plus the column-sync routine that created the field.
Class **A** within scope (R1, plan model read in full).

**EV-P09-012 — Ordinary analytic rights include plan create and delete.**
The module ships **one** access-control group covering all five analytic models, each with read/write/create/unlink all set to 1, and that group is registered in a *hidden* category. There is no user/manager split on the analytic surface.
Source: analytic module access-rights CSV (5 rows) and the group record in the security XML.
Combined with EV-P09-010/011: **schema-altering DDL is reachable from a single, hidden, undifferentiated functional group.** Unit here = one ACL row (5 rows examined).

**EV-P09-013 — One plan is privileged by a database-global system parameter, and the source declares the setting unsafe to change.**
A system parameter names the id of the single "project" plan; the shipped data file sets it to a hard-coded id. The plan-column resolver branches on identity with that plan to decide whether a record uses the fixed column or a generated one. The shipped data file carries an explicit source comment stating that once set, the parameter cannot be changed safely without a manual database script, because the other plans generate dynamic columns whose names would also require renaming.
Source: analytic data file (parameter set + comment), plan model column resolvers.
The parameter is a **system-wide** parameter: it is not company-scoped and not tenant-scoped. The resolver reads it through elevated rights and caches it in a process-level cache.
Consequence: in a multi-tenant deployment, one tenant's analytic schema decision is a property of the whole database.

**EV-P09-014 — Re-parenting a plan or moving an analytic account between plans rewrites history by raw SQL.**
Writing a new plan on an analytic account, or writing a parent on a plan, triggers a routine that issues a **direct SQL `UPDATE` against the analytic line table**, moving values from the old plan column to the new one and nulling the old. It runs outside the ORM: no tracking, no message log, no audit record, no user confirmation.
The routine's only guard is a *collision* check — it raises a redirect warning if any target row already holds a different value in the destination column, with the message "Whoa there! Making this change would wipe out your current data." If there is no collision, the historical rewrite proceeds silently.
Source: analytic account model, history-move routine and `write` override; analytic plan model `write` override.
Class **A** within scope. Unit = one SQL statement, one call site in each of two models.

**EV-P09-015 — The guard protects against overwrite, not against alteration.** The same routine that refuses to *overwrite* a populated destination column will *silently move* every value when the destination is empty. Prior-period management reporting therefore changes retrospectively on a master-data edit that the system treats as ordinary.

---

## 2. THE DISTRIBUTION CARRIER

**EV-P09-016 — Analytic distribution is a schemaless JSON column with no referential integrity.**
The distribution field is a JSON field whose keys are comma-joined analytic-account ids and whose values are percentages. It is indexed by a GIN index over a regex split of the JSON keys, created by direct DDL in the mixin's initialiser.
Because the ids live inside JSON, there is **no foreign key**, no `ondelete` behaviour, and no database-level guarantee that a referenced analytic account still exists. The mixin's own reader proves that dangling keys are an expected state: it browses the ids and filters them through an existence test before exposing them.
Source: analytic mixin field declaration, initialiser DDL, and the account-id computation.
Class **A** within scope.

**EV-P09-017 — Distribution percentages are not required to total 100 %.**
The routine that checks a 100 % total is **opt-in by execution context**: its first statement returns immediately unless a specific context flag is set by the caller. When the flag is set, it checks only those root plans whose applicability resolves to *mandatory*, and it checks each mandatory root plan independently. A plan that is optional may carry any total — 0 %, 37 %, 250 % — with no validation at any layer.
There is no model constraint and no database constraint on the total.
Source: analytic mixin validation routine (context guard, mandatory-plan filter, per-root-plan comparison).
Class **A** within scope (pattern: `constrains` and `Validation` over the analytic module and the mixin).

**EV-P09-018 — Percentages are rounded to a configurable precision, defaulted to 2 digits.**
Both `create` and `write` on the carrier round every percentage to the "percentage analytic" decimal precision before storage. The shipped default is 2 digits. Rounding is applied to the *percentage*, not to the resulting allocated amount, so the allocated amounts are a rounded percentage of a rounded base.
Source: analytic mixin `create` / `write` / sanitiser; shipped decimal-precision record.

**EV-P09-019 — Reporting over the distribution carrier is available to only 4 of the 11 carriers.**
Grouping a query by the distribution field requires a hard-coded table-to-identifier map. The map holds **four** table names. Any other carrier raises a value error on the grouping path.
Source: analytic mixin grouping helper (the map literal and the raise).
Unit = one map entry per supported table. Of the P1 population of 11, **7 cannot be grouped by distribution** through this path. Class **A** within scope; whether an alternative grouping path exists for those 7 was **not searched** — class **C** for that sub-question.

**EV-P09-020 — The budget line does not use the distribution carrier at all.**
The budget line carries analytic through the *plan-column* mixin (one many2one per plan) rather than through the JSON distribution. One commercial-document line in the same budget module carries a **second, derived JSON field** computed and stored from its own distribution, existing solely so that SQL can join it against budget lines.
Source: budget line model inheritance declaration; purchase-side derived JSON field in the same module.
Consequence: **two incompatible analytic shapes coexist**, and the bridge between them is a stored, derived copy — a second source of truth for the same allocation.

---

## 3. THE DISTRIBUTION RULE ENGINE

**EV-P09-021 — Distribution rules are selected by an `in [value, False]` domain, so a rule with no company matches every company.**
The rule search builds one domain clause per selector field, each of the form "field in [the requested value, False]". A rule with a null company therefore matches every company; a rule with a null partner matches every partner. The default search values are all null/empty.
Source: distribution model, domain builder and applicable-model search.

**EV-P09-022 — Rule precedence is order-dependent and last-write-wins within a root plan.**
Matching rules are iterated in the model's declared order (sequence ascending, then **id descending**). Each rule is skipped if any root plan it touches has already been contributed by an earlier rule; otherwise its distribution is merged into the result with a dictionary union, so a later rule's key overwrites an earlier rule's identical key.
Consequence: which rule wins depends on sequence, then on **creation order reversed**. Two rules created in a different order produce a different allocation from identical configuration.
Source: distribution model, distribution-combination routine.

**EV-P09-023 — A rule that touches two root plans blocks both.**
The skip test is "any root plan of this rule already applied". A rule spanning two root plans is therefore skipped in its entirety if either of its plans was already contributed, even when its other plan is still unallocated.
Source: same routine as EV-P09-022.

**EV-P09-024 — The company-consistency constraint on distribution rules is triggered by the company field only.**
The constraint that forbids a company-shared rule from containing company-specific analytic accounts is declared as triggering on the **company field alone**. It executes a raw SQL check joining the rule's JSON keys to the analytic accounts.
Because the trigger list names only the company field, the constraint fires on create and on any write that includes the company field — but a later write that changes **only the distribution payload** does not re-trigger it.
Source: distribution model constraint declaration and its SQL body.
**Status: PLAUSIBLE, not confirmed.** This is a code-path inference from the constraint's trigger declaration; it was not executed against a running database. Routed to adversarial verification as CH-CAND-01.

---

## 4. THE ANALYTIC LINE

**EV-P09-025 — At its own module level the analytic line has no link to the ledger.**
The analytic line model as declared in the analytic module carries: description, date, amount, quantity, unit of measure, partner, user, company, currency, category, and one many2one per plan. It carries **no** reference to a journal item, a journal entry, or a general account. Those links are added by the accounting layer above it.
Source: analytic line model field block (read in full, 211 lines).
Consequence: the analytic line is structurally an independent record. Its existence does not imply, and is not implied by, a ledger posting.

**EV-P09-026 — The analytic line has no transaction currency.**
Its currency field is *related to the company's currency*, stored, and read-only. There is no second amount in a document currency and no rate field. A management figure originating in a foreign-currency document is stored only after conversion, with no record of what it was converted from or at what rate.
Source: analytic line currency and amount field declarations.

**EV-P09-027 — Company on the analytic line is required and immutable; company on the analytic account is optional.**
The line's company field is `required=True, readonly=True`, defaulted from the active company at creation. The analytic account's company field is **not required** and defaults to the active company.
Source: analytic line and analytic account company field declarations.

**EV-P09-028 — The record rules are asymmetric: accounts leak across companies by design, lines do not.**
Four global record rules ship with the analytic module:

| Model | Rule domain (paraphrased) |
|---|---|
| analytic account | company is null **OR** company is a parent of the user's companies |
| analytic line | company is in the user's companies |
| plan applicability | company is null **OR** company is a parent of the user's companies |
| distribution rule | company is null **OR** company is a parent of the user's companies |

Three of the four admit a null company as universally visible. The analytic **line** rule does not. The analytic **plan** model has **no** record rule at all.
Source: analytic module security XML (4 rule records; the plan model is absent from the file).
Class **A** within scope (whole file read; unit = one rule record).

**EV-P09-029 — Only the privileged plan's column is company-checked; every other plan's column is not.**
The fixed column belonging to the privileged plan is declared in the mixin with an explicit company check. The columns for all other root plans are created at runtime by the column-sync routine, which sets the relation, the delete behaviour and the copy flag — but **does not set a company check**.
Source: mixin field declaration (company check present) vs column-sync creation dictionary (company check absent).
Consequence: a journal item of one company can be allocated to an analytic account of another company through any non-privileged plan. The control exists on exactly one dimension of N.
Class **A** within scope. **Status: mechanism confirmed from source; the resulting cross-company allocation was not executed against a running system.** Routed to adversarial verification as CH-CAND-02.

**EV-P09-030 — The analytic account's company-consistency constraint is one-directional.**
The analytic account carries a constraint, triggered on its company field, that refuses to change the account's company while analytic lines of a different company reference it. There is no matching constraint on the *line* side preventing the creation of such a line in the first place.
Source: analytic account constraint declaration and body.

**EV-P09-031 — Analytic balances are converted at today's rate, in the reader's active company currency.**
The debit/credit/balance computation converts each currency group to `env.company.currency_id` at `Date.today()`. It is not converted at the line's own date, and not at a reporting date.
Its domain includes analytic lines whose company is **null** in addition to the user's companies.
Its debit/credit split is derived purely from the sign of the amount: negative amounts are reported as debit (negated), positive as credit, and balance is credit minus debit.
Source: analytic account balance computation (domain, conversion helper, sign split).
Three consequences, each independently material:
1. The same analytic account shows a **different balance on a different day** with no underlying change.
2. The same analytic account shows a **different balance to a different user** whose active company has another currency.
3. The analytic sign convention is the **inverse** of the ledger's: cost is negative in analytic and debit-positive in the ledger.

**EV-P09-032 — A search filter's meaning depends on the reader's active company.**
The analytic line overrides SQL generation for one special date value, resolving it through the **active company's** fiscal-year computation and then subtracting a further year. Two users in different companies running the same saved filter select different periods.
Source: analytic line SQL condition override.

---

## 5. APPLICABILITY — WHETHER ANALYTIC IS MANDATORY

**EV-P09-033 — Mandatory-ness is decided by a floating-point score, not by a rule.**
Each root plan resolves to optional / mandatory / unavailable by scoring its applicability rules. The score is: **0.5** if both the rule and the request name a company; **+1** if the business domain matches; **−1** if it does not. The highest strictly-greater score wins; ties keep the incumbent, and the incumbent starts as the plan's default applicability.
Source: plan applicability resolver and the rule scoring routine (the literals 0.5, +1, −1 are in source, with an inline comment explaining the 0.5 as "company is less important than other fields").

**EV-P09-034 — A rule with no company applies to every company.**
The resolver's filter accepts a rule when the rule has no company, **or** when the request has no company, **or** when they are equal.
Source: applicability resolver filter.

**EV-P09-035 — Default applicability is stored per company outside the plan record.**
The plan's default applicability is a company-dependent field, i.e. it is persisted as a per-company default record rather than on the plan row, and it is seeded to "optional" for the model at table-initialisation time.
Source: plan default-applicability field declaration and the plan model's initialiser.

**EV-P09-036 — The applicability model ships exactly one business domain value.**
The applicability record's business-domain selection is declared in the analytic module with a single value ("miscellaneous"), extended by higher modules. The scoring in EV-P09-033 is therefore, at base level, a two-valued decision dressed as a score.
Source: applicability model selection declaration.

---

## 6. AUTOMATIC TRANSFER — WHERE MANAGEMENT ALLOCATION BECOMES LEDGER TRUTH

The reference pattern ships a distinct mechanism, in its own module, whose purpose is periodic reallocation between general accounts, optionally filtered by analytic account or partner.

**EV-P09-040 — Automatic transfer creates real journal entries.** It creates entries in a nominated destination journal, links them back to the transfer definition by a dedicated field on the entry, and populates ordinary debit/credit lines against real general accounts. This is not an annotation: it is financial posting produced by a management-allocation rule.
Source: transfer model creation routine; the entry-level back-reference field.

**EV-P09-041 — Generated entries are recreated from scratch on every run until posted.**
The generation routine locates an existing **draft** entry for the period, **unlinks all its lines**, and rewrites them. The module's own source comment states that entries "will be recomputed everyday until posted".
Consequence: an unposted allocation is not a document; it is a view that silently changes as new source postings land in the period.
Source: transfer model period routine (line unlink then rewrite) and the scheduling comment.

**EV-P09-042 — Once posted, a period is never revisited.**
The start date for a run is derived from the most recent **posted** generated entry, plus one day. Source postings that arrive in an already-posted period are therefore never allocated, and no exception, warning or reconciliation surfaces the omission.
Source: transfer model start-date routine (domain restricted to posted state, order by date descending, limit 1).
Class **A** within scope for the code path. **Status: PLAUSIBLE for the operational consequence** — not executed. Routed as CH-CAND-03.

**EV-P09-043 — The analytic filter matches on presence and transfers the whole balance.**
A transfer line filtered by analytic account builds its domain with a containment test on the distribution field. That test is satisfied by **any** non-zero presence of the account in the JSON — including a 1 % allocation. The routine then sums the **full balance** of every matching journal item and transfers that full amount.
The complementary "unfiltered" bucket excludes the same lines using the negated containment test, so the partially-allocated amount is not left behind either.
Source: transfer model line domain construction (containment operator), the balance aggregation, and the negated-containment exclusion in the unfiltered routine; the containment operator's SQL is defined in the analytic mixin as an array-overlap test.
Consequence: **a partial analytic allocation is transferred as if it were total.** A cost line allocated 10 % to a cost centre moves 100 % of its balance to that cost centre's destination account.
**Status: PLAUSIBLE, not confirmed** — inferred from three source locations, not executed. Routed as CH-CAND-04. This is the highest-severity candidate produced by this session.

**EV-P09-044 — Only one destination account per transfer definition.**
A database unique constraint enforces one row per (definition, destination account). A definition therefore cannot split the same destination account across two analytic filters.
Source: transfer model line SQL constraint.

**EV-P09-045 — The percentage remainder rule is an exact-equality test.**
The final line absorbs the rounding remainder only when the definition's total percentage is **exactly** 100.0. The total is itself computed with a float comparison that snaps a near-100 total to 100.0 at 6 digits, but the remainder rule then tests plain equality against 100.0. Rounding of each line uses the journal currency, falling back to the company currency.
Source: transfer model total-percentage computation and the remainder branch.

**EV-P09-046 — Percentage lines and filtered lines are scored differently, and the total-percentage computation ignores filtered lines entirely.**
If a definition contains *only* filtered lines, the total percentage is forced to 100.0 with an inline comment that "percentage does not matter". Mixed definitions sum only the unfiltered lines.
Source: transfer model total-percentage computation.

**EV-P09-047 — The generated entries carry no analytic distribution.**
Both the origin-side and the destination-side line value dictionaries contain description, account, maturity date, and one of debit/credit. **No analytic field is written.** The analytic account that *selected* the amount is recorded only inside the human-readable description string.
Source: origin-side and destination-side line value builders (full dictionaries read).
Consequence: the allocation destroys its own audit trail. The link from the transferred amount back to the analytic dimension that caused the transfer exists only as free text.
Class **A** within scope (both builders read in full).

**EV-P09-048 — Tax is forbidden on transfer entries by constraint.** A constraint on the journal item raises if any line of a transfer-generated entry carries a tax.
Source: the module's journal-item constraint.

**EV-P09-049 — The transfer definition is company-scoped only through its journal.** Its company field is read-only and related to the destination journal's company; its record rule restricts on that company.
Source: transfer model company field; module security XML (one rule record).

---

## 7. MANAGEMENT REPORTING — THE LEDGER TABLE IS SHADOWED BY ANALYTIC DATA

This is the most consequential mechanism found in the session.

**EV-P09-050 — When a financial report is given an analytic column, the ledger table is replaced by a temporary view built from analytic lines.**
The reporting layer overrides the query-construction entry point on the journal-item model. When a report-level context flag is present, it builds a temporary view and then **substitutes that view's name for the journal-item table in the query's table map**. Every subsequent expression in that report column is evaluated against analytic data while still being written, read and audited as though it were the ledger.
Source: report layer's journal-item query override (the table substitution is a single assignment into the query's table map), and the view-preparation routine.

**EV-P09-051 — The shadow view stamps every analytic row as posted.**
The view is built by mapping analytic-line columns onto the journal-item schema. Among the mapped values are **literals**: the entry-state column is set to the constant `'posted'`, and the display-type column to a constant. Fields absent from the analytic line are filled from a **left join** to the journal item — so rows with no journal item survive with nulls.
The only filter on the view body is that the analytic line's general-account column is not null.
Source: view-preparation routine (equivalence map literals, left join, single where clause).
Consequence: **an analytic line that was never posted to the ledger is presented to a financial report as a posted journal item.** Class **A** within scope for the mechanism.

**EV-P09-052 — The behaviour has a user-facing switch, and the product names it "Including Analytic Simulations".**
An option key toggles inclusion of analytic rows that have no journal item. When it is on, the report's journal domain is widened by a disjunction admitting a null journal, and the audit drill-down is widened by a disjunction admitting a null journal item.
Source: report option label list (the visible caption is in source), the journal-domain widener, and the audit-cell drill-down builder.

**EV-P09-053 — The shadow view inverts the sign of the ledger.**
The balance column is mapped to the **negated** analytic amount; debit is the analytic amount when negative, credit when positive. This is consistent with EV-P09-031 and confirms the inversion is systematic rather than incidental.
Source: view-preparation equivalence map.

**EV-P09-054 — The shadow view expands one analytic line into one row per plan.**
The distribution column of the view is built by wrapping an array of **all** plan columns in a set-returning unnest. A set-returning function in the select list multiplies the row: an analytic line with two plan columns populated yields two rows, each repeating the full balance, debit and credit.
The report's own query then adds a filter restricting the distribution column to the accounts of the single plan or single account being reported, which suppresses the duplicate rows **on the intended path**.
Source: view-preparation routine (unnest over the plan-column array) and the report query's added where clauses (two branches, one per option shape).
**Status: PLAUSIBLE, not confirmed.** The multiplication is a property of the view; whether any caller reaches the view without the restricting filter was not exhaustively enumerated. Routed as CH-CAND-05.

**EV-P09-055 — Read-only query optimisation is disabled whenever an analytic column is present.** The reporting layer explicitly clears its read-only-query flag when the analytic grouping option is active, because the mechanism must create a temporary view. Source: read-only option initialiser override.

**EV-P09-056 — The analytic report column is gated by the same single hidden group as plan DDL.** Both the analytic filter and the analytic group-by initialisers return early unless the user holds the analytic group — the same group that EV-P09-012 shows carries create and unlink on plans. Source: two option initialisers in the report layer.

---

## 8. BUDGET AND BUDGETARY CONTROL

Evidence in this section was collected by a separately-tasked researcher against R1 and R2 and is reproduced with its citations intact in `E01`.

**EV-P09-060 — There is no budgetary-position object.** The budget surface consists of a budget header, a budget line, and a non-stored SQL view used for reporting. A named budgetary-position model was searched for by three spellings across both budget modules and returned no code hits (translation catalogues only). Class **B** (not found in searched scope: two modules, three patterns).

**EV-P09-061 — Budget is matched to actuals by plan column + date window + company, not by account.** A budget line is joined to actual analytic lines on the plan-column equality, the analytic line's date falling inside the line's date window, and a company test that treats a null budget company as matching everything.
Source: budget reporting view join conditions.

**EV-P09-062 — "Achieved" is computed from analytic lines, not from the ledger.** The achieved figure aggregates the analytic line amount, sign-flipped for expense budgets, filtered by the *general account's* account type. It is not stored: it is recomputed by a non-materialised view on every read.
Source: budget reporting view achieved branch; budget line computed-field declaration without storage.

**EV-P09-063 — "Committed" is computed from open purchase order lines.** The committed figure aggregates the not-yet-invoiced quantity of purchase order lines whose order is in a confirmed or done state, dated by the order date, and is excluded for revenue budgets.
Source: budget reporting view committed branch.
Consequence: budget consumption mixes **three different time bases** — the analytic line date for achieved, the purchase order date for committed, and a straight-line elapsed-days proration for theoretical.

**EV-P09-064 — "Theoretical" is a straight-line proration of elapsed days.** Computed in application code, not stored, not derived from any transaction.
Source: budget line theoretical computation; the formula appears in the field's own help text.

**EV-P09-065 — No hard budget control exists in the budget modules.** Every raise in the two budget modules was enumerated: a date-order check on the line, a recursive-revision guard on the header, and a delete guard limiting deletion to draft/cancelled. None references an amount, a consumption figure, or an excess. Budget excess surfaces only as a **computed boolean displayed** on the budget line, the purchase order and the purchase order line; it gates no write, no state transition and no confirmation.
Source: exhaustive read of both modules' model files plus a raise/constrains pattern sweep.
Class **A within the stated scope of the two budget modules.** Whether another module imposes budget control was searched only by module-name pattern P5 — class **C** for the rest of the system.

**EV-P09-066 — Budget amounts are locked only by a view attribute.** After confirmation the amount field is made read-only by an XML attribute on the list and form views. No server-side write override, field-level readonly, or record rule was found in the two modules.
Source: view XML read-only attribute; absence confirmed by full read of both model files.
Consequence: the lock holds through the user interface and **not** through the programmable interface. Class **B** for the absence.

**EV-P09-067 — The budget state machine has no server-side transition guards.** Reset-to-draft sets the state unconditionally from any state; cancel has no server-side state precondition; the draft-only restriction on the cancel button is a view-level visibility rule.
Source: budget header action methods.

**EV-P09-068 — A budget created from the project side is auto-confirmed.** When the header is created with a project-update context key present, confirmation is invoked immediately after creation, bypassing the manual open step.
Source: project-side budget header create override.

**EV-P09-069 — The budget surface has no fiscal-period object.** Budget windows are free-form dates. No fiscal-year or date-range model participates. Searched by three patterns over both budget modules and by module-name pattern over both roots. Class **B**.

**EV-P09-070 — Budget record rules admit a null company as globally visible;** both budget models carry a global rule of the form "company in the user's companies OR company is null". Neither budget model uses a company check on any relational field.
Source: budget module security XML (two rule records) and a company-check pattern sweep over the module.

---

## 9. NEGATIVE-CLAIM LEDGER FOR THIS FILE

Every negative statement made above, with its class and its boundary. Per `DR-NC-01..06`, no class B/C/D claim in this file may be restated as class A anywhere downstream.

| Ref | Negative claim | Class | Declared boundary |
|---|---|---|---|
| EV-P09-001 | analytic surface not present in the archive root | **A** | pattern P1 over R2, 959 manifests |
| EV-P09-011 | no archival/export on plan deletion | **A** | analytic module, plan model read in full |
| EV-P09-012 | no user/manager split on the analytic surface | **A** | analytic module ACL CSV, 5 rows |
| EV-P09-016 | no foreign key on the distribution carrier | **A** | mixin field declaration + initialiser DDL |
| EV-P09-017 | no model or database constraint on distribution total | **A** | analytic module, constrains pattern |
| EV-P09-019 | 7 of 11 carriers cannot be grouped by distribution *by this path* | **A** for the path; **C** for alternative paths | mixin grouping helper only |
| EV-P09-025 | analytic line has no ledger link at its own module level | **A** | analytic module analytic-line model, read in full |
| EV-P09-026 | no transaction currency on the analytic line | **A** | same |
| EV-P09-028 | no record rule on the analytic plan model | **A** | analytic module security XML, read in full |
| EV-P09-029 | no company check on non-privileged plan columns | **A** | mixin declaration vs column-sync creation dictionary |
| EV-P09-030 | no line-side company constraint | **B** | analytic module only; higher layers not swept for this |
| EV-P09-047 | no analytic field on generated transfer lines | **A** | both value builders read in full |
| EV-P09-060 | no budgetary-position object | **B** | two budget modules, three patterns |
| EV-P09-065 | no hard budget control in the budget modules | **A** within the two modules; **C** system-wide | exhaustive read of two modules |
| EV-P09-066 | no server-side lock on budget amounts | **B** | two budget modules, full model read |
| EV-P09-069 | no fiscal-period object on the budget surface | **B** | two budget modules + module-name pattern over R1/R2 |
| EV-P09-002 | which custom copy is deployed | **D** | no evidence in any searched root |

---

## 10. CLAIMS ROUTED TO ADVERSARIAL VERIFICATION

| ID | Claim | Status on entry |
|---|---|---|
| CH-CAND-01 | distribution-rule company constraint does not re-fire on a payload-only write (EV-P09-024) | PLAUSIBLE |
| CH-CAND-02 | cross-company allocation is reachable through a non-privileged plan column (EV-P09-029) | PLAUSIBLE |
| CH-CAND-03 | postings arriving in an already-posted transfer period are never allocated (EV-P09-042) | PLAUSIBLE |
| CH-CAND-04 | a partial analytic allocation is transferred at 100 % (EV-P09-043) | PLAUSIBLE |
| CH-CAND-05 | the shadow view multiplies rows per plan (EV-P09-054) | PLAUSIBLE on entry — **DISPROVED as an exposure claim by independent challenge**; see `P09_AAS03_CHALLENGE` |

**END OF E00.**
