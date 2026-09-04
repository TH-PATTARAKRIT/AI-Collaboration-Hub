# X2 — AAS-03 EXPERT 2 · DATABASE DESIGN · ADVERSARIAL REVIEW
**LAYER 2 — AUDIT QUARANTINE.** Session SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001.
Independent reviewer, disjoint assignment, instructed to settle claims by reading the platform's own implementation rather than by intuition.

## A. CORRECTIONS RETURNED AGAINST THE RESEARCH TEAM

**COR-X2-01 — strengthens EV-P09-011 and raises its severity.** Deleting an axis does not merely drop a column. `ir.model.fields` deletion routes to a routine issuing `ALTER TABLE … DROP COLUMN … CASCADE` (`odoo/addons/base/models/ir_model.py:874-876`). `CASCADE` drops **every database object depending on that column** — views, indexes, constraints — without enumerating or reporting them. The blast radius is unbounded by construction, not merely unconfirmed. Class A.

**COR-X2-02 — narrows EV-P09-013. A correction against the research team.** E00 stated the privileged-axis lookup "caches it in a process-level cache", which invites a reading of indefinite staleness. That reading is wrong: the cache **is** invalidated on every write path that matters — system-parameter writes clear the registry cache explicitly (`ir_config_parameter.py:106-119` → `registry.py:761-769`, `827-851`), and any axis create or delete forces a model re-setup (`ir_model.py:1047-1050`, `1005-1013` → `registry.py:324`). Cross-worker propagation is bounded to one request, not unbounded. **E00's separate scope claim — that the parameter is database-global — is unaffected and stands.** Class A.

**COR-X2-03 — adds missing prior-shape evidence bearing on EV-P09-029/030.** Before the current module version, non-privileged axis columns on the management-record table carried an **on-delete set-null** rule, not restrict (`analytic/migrations/1.2/pre-migrate.py:17-27`). Deleting an axis value silently nulled every management record's pointer in that dimension. The protected-versus-unprotected story therefore has a **third, historical state**.

## B. NEW FINDINGS

**X2-04 — a runtime-created relational field structurally cannot carry a company check; this is a closed door, not an omission.** The attribute list used to build a field object from a manual field row (`ir_model.py:1299-1305`) sets, for a many2one, exactly the comodel, the delete rule, the domain and a group-expand hook. The company-check attribute appears **nowhere** in that routine (full-file pattern sweep, zero hits) and the field class defaults it to false (`fields.py:3054`). There is no column on the field-definition model to hold it and no code path that assigns it. **Every runtime-created axis column, for every non-privileged axis, on every model, is structurally exempt.** Class A.

**X2-05 — a second, independent gate: the company check is not even *invoked* for such a write.** The platform's write path sets its company-check flag only when a written field name is the company field itself or is a relational field whose company-check attribute is true (`odoo/models.py:4751-4752`), and the call is gated on that flag (`:4838-4839`). A write of only a non-privileged axis column never sets it, so the check is **never invoked**, not merely ineffective. Class A. Either mechanism alone would defeat the control.

**X2-06 — no database-level check constraint exists anywhere on the analytic or budget surface.** Pattern sweep for both the legacy and current constraint declarations over the analytic models and the budget models: zero hits. Every integrity control on this surface is either an application constraint — which fires only in-transaction, only on its declared trigger fields, and is bypassed entirely by any direct-statement path such as EV-P09-014's rewrite — or a foreign key on axis columns only. Nothing at the storage layer prevents a negative budget amount, a negative precision, or a non-100 % allocation total. Class A within the two surfaces; class C for the rest of the tree.

**X2-07 — the two index families are not comparable.** The privileged axis column receives a plain btree via the ordinary field attribute (`analytic/models/analytic_line.py:16-22`); every runtime-created axis column receives an explicitly **partial** btree (`analytic/models/analytic_plan.py:288-291`). Reasonable as an optimisation, but the two families have different selectivity and maintenance characteristics; a planner comparing them is not comparing like with like. Not a defect; recorded because no prior evidence carried it.

**X2-08 — the allocation index supports exactly one expression shape.** One functional index over a regex split of the JSON keys (`analytic/models/analytic_mixin.py:33-37`), usable only by the overlap expression the model itself builds (`:60-99`). **There is no index of any kind over the percentages.** A query such as "find every row allocating more than half to this axis value" is a full scan by construction. Class A — no second index statement exists in the file.

**X2-09 — the upgrade script crashes on a state the runtime declares possible.** The migration unpacks a query result with no existence guard (`pre-migrate.py:13`); if the privileged-axis parameter is unset the unpack raises and the migration aborts. The module's own runtime code treats that exact state as expected and handles it with a user-facing error (`analytic/models/analytic_plan.py:101-103`). The asymmetry is a defect, not a design choice. Class A.

## C. CONSTRAINT TRIGGER INVENTORY

Every row tested against the platform's actual trigger-resolution code, not inferred from the decorator.

| Object | Constraint | Declared trigger | What actually re-fires it |
|---|---|---|---|
| axis value | company consistency | company field | only a write whose values contain the company field; a write of name, axis or partner alone does not re-run it |
| allocation rule | company/account consistency | **company field only** | a write of only the allocation payload **never** triggers it — **CH-CAND-01 CONFIRMED** |
| axis-column mixin (management record, budget line, every carrier) | at least one axis set | **dynamic** — re-evaluated per call from the current axis set | any write touching any axis column; correctly tracks new axes, contingent on the axis cache being fresh (COR-X2-02) |
| all five analytic objects | automatic company check | company field, or a field carrying the company-check attribute | privileged axis column checked; **every runtime-created axis column never checked, by construction** — **CH-CAND-02 CONFIRMED** |
| budget header | recursion guard | parent field | only a write touching the parent; state, dates and amounts do not |
| budget header | delete guard | fires on every deletion, blocks unless draft or cancelled | delete-time only; **no write-time guard on state transitions exists anywhere in the file** |
| budget line | date-order check | the two related, stored date fields | fires when those recompute from the header; **not** when the amount or any axis column changes |
| budget line | — | — | **no constraint anywhere references the amount, the consumption figure, or an excess condition** — independently reproduces EV-P09-065 |

## D. ADVERSARIAL VERDICTS

### CH-CAND-01 — **CONFIRMED**
The constraint declares the company field as its only trigger. The platform's validation entry point invokes a constraint only when the field-name set intersects the constraint's declared trigger set (`odoo/models.py:1622-1631`), and on write that set is populated **directly from the written values' keys** (`:4813`) — not from all fields, not from pending recomputes. A write of only the allocation payload produces a disjoint set; the constraint is not called. **On create the behaviour differs**: validation is invoked with every stored field (`:5275`), so the constraint does fire at creation. **The gap is write-only, and specifically a write that omits the company field.**

### CH-CAND-02 — **CONFIRMED**
Two independent structural facts, either sufficient: (1) a runtime-created relational field can never be instantiated with a company check through that mechanism (X2-04); (2) the platform never invokes the company check at all for such a write (X2-05). No user-interface domain compensates — the axis-value domain restricts by axis only, never by company (`analytic/models/analytic_line.py:82-83`). The mechanism is reachable both through direct writes and through the ordinary form view. **Stronger than the research team's "operational consequence unexecuted" framing: the *reachability* claim needs no execution, because both gates that would have to fire are shown by their own source to be structurally incapable of firing for this field class.** Observing the resulting reporting distortion in practice would still require execution.

## E. MIGRATION AND UPGRADE RISK
The migration is the **current** one — the module version matches the migration directory name, so it runs for any database being brought forward. Its scope is the literal management-record table only. The column-sync routine is generic over **any** carrier of axis columns, which in the base module already includes the budget line. **A pre-upgrade database whose budget lines already carried axis columns under the old set-null rule is not touched**, producing an inconsistent delete-rule surface: restrict on one table, set-null still in force on others referencing the same axis values. `NOT FOUND IN SCOPE: the module's migrations directory, all files, pattern = a migration for non-management-record axis-column carriers — 0 of 1 files` — class **B**; other modules' migration directories were not searched.

## F. SEARCH BOUNDARY
17 enumerated command groups: full reads of all five analytic model files, the migration script, both budget model files, the analytic security files; targeted reads of the platform's field-definition model, its validation entry point, its company-check implementation and call gate, its cache implementation, its registry signalling, and its system-parameter model. **Path finding returned against the brief:** the brief's stated platform-source path carried a doubled directory segment and does not exist; the correct path was located and every citation uses it. **No prohibited verdict vocabulary used.**
