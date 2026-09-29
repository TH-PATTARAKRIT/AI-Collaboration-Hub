> Domain: SHARED_MASTER_DATA_PILOT | Neutral Function Knowledge Pack | Clean-Room boundary: eligible for STATE04 consideration only after STATE04's own separate authorization

# NEUTRAL FUNCTION KNOWLEDGE PACK

Per Master Prompt §10: sanitized companion to `06_BUSINESS_RULE_REGISTER.md`. Business purpose, rules, neutral state/event/data concepts, dependency, risk, and Unknowns only — no evidence URLs, no Odoo menu paths, no field/table-level identifiers, no source code, no schema/ORM structure. Not itself an authorization for STATE04, Functional Design, or any target-system decision.

**Scope note**: only `SMD-F04` is sanitized in full here. `SMD-F01`–`F03` are Carry-forward citations to a separate track's own evidence and are not this pilot's primary contribution — a sanitized pack for those three, if ever needed, belongs to that track's own governance chain, not duplicated here.

### SMD-F04 — Role-based access boundary

- **Business purpose**: Restrict which parts of a system a given user may act on, based on the job function(s) they are assigned.
- **Business rule**: Access is granted by membership in one or more named permission bundles; a user's effective access is the combination of everything every bundle they belong to grants — never reduced by any other bundle. If nothing grants an access, it is denied by default.
- **Neutral state**: A user is assigned one or more bundles → effective access recomputes as the union of all of them → re-evaluated whenever bundle membership changes, not retroactively against past actions.
- **Data concept**: A permission bundle is a standalone concept, independent of any one business object it happens to grant access to.
- **Control**: This is a coarse-grained, "can touch this kind of business object at all" control — a separate, finer-grained mechanism (which specific records, not just which kind) is a distinct concept not covered by this finding.
- **Dependency**: Interacts with, but is structurally independent from, a separate company/tenant-scoping boundary (already characterized elsewhere in this Deep Study) — the two can both apply to the same access decision at once.
- **Risk**: Because access is purely additive, granting a broad permission bundle to solve one narrow need creates a standing over-permission that cannot be narrowed by any other assignment — only removing the over-broad grant fixes it.
- **Unknown**: The precise interaction between this coarse-grained, kind-of-object access boundary and a separate, specific-records boundary when both apply to the same decision — not evidenced this pass.

## Clean-Room compliance statement

No source code, method name, table/field name, ORM relationship, physical schema, UI element, or menu path appears above. No SMEsPlus target design, schema, workflow, or architecture decision is implied or authorized by this pack. Odoo-reference learning input only, per the Master Prompt's Clean-Room boundary (§10), and not itself eligible for STATE04 use until STATE04 is separately authorized.
