# X4 — AAS-03 EXPERT 4 · CODE & UI ARCHITECT · ADVERSARIAL REVIEW
**LAYER 2 — AUDIT QUARANTINE.** Session SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001.
Independent reviewer, disjoint assignment, focused on the boundary between what a view enforces and what the server enforces.

## A. CORRECTIONS RETURNED AGAINST THE RESEARCH TEAM

**COR-X4-01 — the client-side allocation control is decorative, and the session's mandatory-ness narrative could be misread as implying otherwise.** The widget's completeness test (`analytic/static/src/components/analytic_distribution/analytic_distribution.js:184-186`) is consumed only to set a colour class on a header total (`:172-181`). The only save-adjacent gate (`:405-407`) checks merely that one row has an axis value and a non-zero share; it never reads completeness or obligation, **and it is not wired to the save path at all** — the editor's close handler calls save unconditionally on blur, escape, or an outside click (`:480-483`). **The widget performs colouring, not validation.**

**COR-X4-02 — strengthens EV-P09-029/114 with an admission in the source itself.** The axis-value picker's domain restricts by axis only (`analytic_distribution.js:285`), and the line immediately above it carries the developers' own comment that a company domain might be required here (`:284`). The client therefore never restricts axis-value choice by company, on any axis, **including the privileged one**. Combined with the server-side finding, there is no compensating control anywhere in the stack.

**COR-X4-03 — EV-P09-012 under-states its own severity by omitting how the group is granted.** The settings model declares the analytic group as an implied group with **no explicit granting group** (`analytic/models/res_config_settings.py:9`), and the platform's default for an unspecified granting group is the ordinary internal-user group (`base/models/res_config.py:240`, applied at `:350`). **Toggling one settings checkbox grants full create, write and delete on all five analytic objects to every internal user in the database**, with no intermediate approval. This is materially stronger than "hidden and undifferentiated": it is default-on-for-everyone by ordinary configuration semantics.

**COR-X4-04 — the budget-amount exploit path is narrower and worse than stated.** EV-P09-066 said the lock is a view attribute. The reviewer found the reachable path: the reset-to-draft action sets the state unconditionally from any state (`account_budget/models/budget_analytic.py:71-72`), and the amount's read-only attribute is keyed on that same state (`views/budget_line_view.xml:33`, `:52`; `views/account_analytic_account_views.xml:18`). **Resetting a closed budget to draft reopens the amount through the normal user interface** — no raw programmatic access needed, no elevated group beyond ordinary write.

**COR-X4-05 — reproduces E01 §B.1 independently and adds that the write path *actively executes* the destruction.** It is not merely that no guard fires; the only side effect the write produces is the inverse that destroys and rebuilds the management records.

## B. NEW FINDINGS

**X4-01 — schema-DDL rights are one settings checkbox away from every employee.** Citations as in COR-X4-03 plus the five all-permissions access rows. **The single "analytic accounting" toggle most implementers enable on day one converts "no user/manager split" into "every internal user can create and delete axes"** — that is, can perform live schema work that drops columns with cascade and destroys historical management data, with no confirmation beyond an ordinary delete click. Class A.

**X4-02 — the runtime view-patch's permission gate is evaluated inside a memoised routine whose cache key contains no user or group component.** The patch's gate is an access test on the axis object (`analytic/models/analytic_line.py:111-112`), evaluated during arch computation. The platform's view cache key is built from view id, view type, mobile flag, language and reference-context keys only (`base/models/ir_ui_view.py:2686-2702`), and the cache's **own docstring** (`:2711-2713`) states that the cached arch includes blocks for all groups and that group-restricted blocks must be removed *after* the cache, which the framework does through a separate post-cache step (`:2748`, `:2771-2777`). The patch does not use that documented mechanism; it bakes a permission decision in before the cache boundary. Whichever request populates the entry decides, for every later user on the same key, whether the axis columns appear at all — **over-exposing** (a user without rights inherits a primed entry, with fields present but labels and domains in their raw technical form, since the labelling routine is per-request and not cached the same way) or **under-exposing** (a user with rights inherits an entry primed without them). Mechanism class A — the contradiction is between two pieces of source, not an inference; the practical trigger order was not exercised, so the operational consequence is CONFIRMED WITH CAVEAT.

**X4-03 — the view patch silently no-ops when a customer's own inheritance has moved or wrapped the anchor node.** The patch locates a single named node and gates all injection on finding it (`analytic/models/analytic_line.py:116-117`, `:124-137`). No error, no log. **This is reachable by the single most common customisation operation on that view.** Class A for the code path; whether any deployed tenant view actually triggers it is class **C**.

**X4-04 — the allocation field carries no group restriction at the model level, so the view-level restriction gates nothing.** Neither of the field's two declarations carries a group parameter. The lowest write-capable role on the ledger row is the billing role, whose access row grants full permissions on that model, and it does **not** require the analytic group at all. **Any user who can write a ledger row can set its allocation, regardless of the analytic group.** The analytic group's access rows gate the five *analytic* objects; they do nothing to gate the *carrier* field on the eleven host objects, each of which has its own, weaker, access rules. Class A — a second, independent access gap beneath the one already found.

**X4-05 — the report shadow view is a connection-scoped database object that this code never drops.** The existence check is an unqualified catalogue lookup that returns early if the object is present (`account_reports/models/account_analytic_report.py:114-116`); the creation is reached only otherwise (`:147-157`). The table substitution itself (`:248-258`) is per-query and context-scoped, which is correct. What is not request-scoped is the database object: **once any report run creates it on a pooled connection, that connection carries it for the rest of its life in the pool — across arbitrarily many later, unrelated requests, users and companies.** It is a live view, not a snapshot, so this is not a stale-data fault; it is (a) an uncleaned per-connection catalogue object and (b) a namespace claim — any other code needing that name on the same connection is silently shadowed. Mechanism class A; pooled blast radius and read-only-pool interaction **NOT DECIDABLE FROM SOURCE**, class C.

**X4-06 — a create call reaches a privileged state that the write access rules appear to reserve.** The transfer object's state field carries no read-only and no group restriction, and its activate action is a plain write. The access rows give the billing role create-yes / write-no, and the manager role everything. There is **no create override forcing a new record to start disabled**. A billing user can therefore create a transfer definition already in the running state. **The true least-privileged role able to reach a running automatic transfer is billing, not accounting manager as the access table implies at a glance.** Class A.

## C. VIEW-LOCK VERSUS SERVER-LOCK

| Control | View gate | Server counterpart | Verdict |
|---|---|---|---|
| allocation totals 100 % on a mandatory axis | colour class only, no save block | a real check exists but is **opt-in by execution context** and is invoked only at four named confirm/post call sites | CONFIRMED WITH CAVEAT — a raw write, an import, an automation or an API client never triggers it |
| allocation's axis value matches the company | **none** — and a source comment admits the gap | exists only on the privileged axis column; structurally cannot attach to the payload | CONFIRMED — no client gate, and the one server gate cannot reach the path the interface actually uses |
| allocation editable on a posted, hashed, lock-dated row | read-only on **one** view (the invoice line's secondary tab, unconditional). The journal-items list views carry **none** | **none** — see §D | CONFIRMED |
| budget amount after confirmation | read-only keyed on budget state, three views | none — no write override, no field read-only, no group | CONFIRMED, and reopenable through the normal interface via the unguarded state reset |
| budget state transitions | button visibility only | none — reset and cancel set state unconditionally from any state | CONFIRMED |
| transfer activation | button level | write access rules genuinely restrict the *write* path; the *create* path is unguarded | CONFIRMED WITH CAVEAT |
| runtime-injected axis columns | presence decided pre-cache by an access test, then memoised without a user-scoped key | the real per-user filter runs on group attributes only; injected nodes inherit whatever the anchor node had — often nothing | CONFIRMED WITH CAVEAT |

## D. ACCESS CONTROL — LEAST PRIVILEGE

Access rows read directly. All five analytic objects: **one group, all four permissions, undifferentiated.** Transfer object: readonly role read-only; manager role everything; **billing role read and create but not write**. Budget objects: **no access rows found in the budget module's own security directory** — `NOT FOUND IN SCOPE: that module's security directory, filename and content patterns; class B` — the rows must be granted by another module not located this session; routed as a dependency, **not** asserted as absent.

| Question | Least-privileged answer |
|---|---|
| (a) create an axis | **any internal user**, once the analytic setting is enabled (X4-01); otherwise whatever role was granted the group by data — class D for a live deployment |
| (b) delete an axis | **identical to (a)** — the access row is undifferentiated; there is no create-but-not-delete tier anywhere |
| (c) change an allocation on a posted entry | **the billing role** — the lowest write-capable role on the ledger row; the analytic group is **not** required (X4-04) |
| (d) change a confirmed budget amount | ordinary write access on the budget objects, combined with the unguarded state reset that reopens the view attribute; no group distinction found |
| (e) activate an automatic transfer | **the billing role**, via create with the running state in the initial values (X4-06) — not the manager role the access table implies |

## E. ADVERSARIAL VERDICT — CH-CAND-06: **CONFIRMED**

Full guard-by-guard trace of the ledger row's write path for an allocation-only write:
1. **hash / inalterability** — the violated-field set is the intersection of the written values with the integrity-hash field list; that list, at **every** supported hash version, is drawn only from description, debit, credit, account and partner. The intersection is empty, so the branch never raises **even on an entry carrying a hash**. Does not fire.
2. **tax-on-posted** — checks two tax fields. Does not fire.
3. **fiscal lock date** — fires only if a field in the fiscal protection list changes; the allocation is absent from it. **The lock-date check is never called.**
4. **tax lock date** — fires only on the tax list. Does not fire.
5. **reconciliation** — fires only on the reconciliation list. Does not fire.
6. **value sanitisation** — touches only debit, credit, balance and the matching number. No-op.
7. **balance check** — debit and credit are unaffected; exits cleanly.
8. **tracking / chatter** — the tracked-field set is built from the written keys whose field carries a truthy tracking attribute. The allocation carries none in either of its two declarations, confirmed by enumerating every tracking declaration on the model (six: account, description, balance, tax ids, tax tags, maturity date). **No tracking values, no message log, no chatter entry.**
9. **record rules** — every rule on the model is a company scope or an unconditional group grant. **None references state, posting state, or the allocation.** No rule blocks this write for any user with base write access.
10. **what does happen** — the write executes and invokes the field's inverse, which selects the rows whose parent entry is posted and **destroys and rebuilds their management records**, with no confirmation and no record of either the field change or the rebuild.

**Which guard fires: none.** Every protective check is keyed off explicit field-name lists that omit the allocation in every version and every branch read. The only code that reacts is the inverse, whose effect is the vulnerability, not a control.

**Least-privileged role able to execute it: the billing role** (§D(c)).

**Boundary declared:** this is a code-path read, not an executed reproduction. Three context managers entered by the write path were located but not read to completion; their relevance to an allocation-only write was assessed by field-membership inspection rather than full-body reading. **CONFIRMED for the specific guards named; CONFIRMED WITH CAVEAT for the residual "leaves no trace anywhere in the system"** — a company-level audit-trail mechanism exists but was traced and found to depend on the same field-level tracking declarations and to govern *deletion* of posted entries rather than field writes, so it is structurally inapplicable here, not merely silent. `NOT FOUND IN SCOPE: the reference addons root, an audit-trail-named module at depth 1; class B`.

## F. SEARCH BOUNDARY
40+ enumerated command groups: full reads of the allocation widget (690 lines) and its template, the analytic mixin, the analytic line mixin and its view patch, the analytic report layer, the platform's view-cache implementation and its access post-processing, the platform's settings-model group resolution, both budget models and their views, the transfer module's models and access rows; targeted reads of the ledger row's field block, write path, protection lists and hash field lists. Four explicit residual gaps declared with classes. **No prohibited verdict vocabulary used.**
