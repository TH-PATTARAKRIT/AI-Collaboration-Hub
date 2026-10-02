# U71 Neutral Knowledge — Multi-Company Isolation
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U71-001 | In multi-company ERP deployments, every warehouse record is linked to exactly one owning company through a mandatory ownership field. |
| NR-U71-002 | The warehouse-to-company relationship is set as read-only after creation, preventing warehouse reassignment to a different company post-setup. |
| NR-U71-003 | Every transfer (physical movement of goods between locations) carries a mandatory reference to the company that owns that movement. |
| NR-U71-004 | The mandatory company reference on transfers means an uncompanied transfer record cannot be saved, enforcing hard data segregation at insert time. |
| NR-U71-005 | Each individual stock movement line carries its own company reference, independent of but consistent with the owning transfer header. |
| NR-U71-006 | Stock movement lines require a company value at creation, preventing orphan movement data that is not attributable to any legal entity. |
| NR-U71-007 | Quantity-on-hand records derive their company ownership from the storage location they are stored in, rather than carrying an independent company field. |
| NR-U71-008 | A database-level access rule filters all transfer records so a user can only read transfers belonging to one of their currently activated companies. |
| NR-U71-009 | The transfer access rule uses the full set of activated companies (the multi-company switch selection), not just the primary company, allowing users with multi-company access to work across their allowed set simultaneously. |
| NR-U71-010 | A database-level access rule filters all warehouse records to the set of currently activated companies. |
| NR-U71-011 | A database-level access rule filters all movement records to the set of currently activated companies. |
| NR-U71-012 | The access rule for quantity-on-hand records allows records with no company assignment alongside those matching the activated companies, accommodating shared or transit inventory. |
| NR-U71-013 | Transfer operation-type records trigger an automatic cross-record company consistency check on every save, verifying that all linked records belong to the same company. |
| NR-U71-014 | The Community edition of this ERP does not include any built-in intercompany automation module; automated intercompany purchase or sales order generation is an Enterprise-only feature. |
| NR-U71-015 | A database-level access rule restricts sales orders to the set of currently activated companies for the requesting user. |
| NR-U71-016 | A database-level access rule restricts sales order lines to the set of currently activated companies. |
| NR-U71-017 | A database-level access rule restricts purchase orders to the set of currently activated companies. |
| NR-U71-018 | A database-level access rule restricts purchase order lines to the set of currently activated companies. |
| NR-U71-019 | A user account holds a many-to-many relationship with companies, capturing every company the user is permitted to access, not just their primary company. |
| NR-U71-020 | Domain-rule caching at the ORM level keys on the active company selection, meaning the evaluated access domain is invalidated and recomputed whenever the user switches their active company set. |
| NR-U71-021 | During domain rule evaluation the platform injects the list of currently activated company identifiers as a named variable, making it available to all rule expressions without additional lookups. |
| NR-U71-022 | When any operation runs in elevated-privilege mode (the administrative bypass mode), all record-level access rules are entirely skipped; no company filter domain is applied in that mode. |
| NR-U71-023 | The access-rule model itself is configured to reject commands that attempt to modify it through elevated-privilege relational writes, adding a layer of protection against privilege-escalation attacks on the rule table. |
| NR-U71-024 | The base record type used by all data models sets the automatic company consistency check flag to disabled by default; each model that wants this protection must explicitly activate it. |
| NR-U71-025 | The automatic company consistency checker iterates every record being saved and verifies that each cross-reference field pointing to another record resolves to a record whose company matches the originating document's company. |
| NR-U71-026 | The default company domain builder for cross-reference validation returns a filter requiring the referenced record's company to be in the list of allowed companies, or to have no company set. |
| NR-U71-027 | The journal entry model explicitly enables the automatic company consistency check, so every write or create on a journal entry validates all its cross-referenced fields for company alignment. |
| NR-U71-028 | The sales order model explicitly enables the automatic company consistency check on every write or create. |
| NR-U71-029 | A database-level access rule restricts journal entries to the set of currently activated companies. |
| NR-U71-030 | The journal access rule uses a hierarchical parent-of operator rather than an exact match, allowing users of a child company to see journals that belong to the parent company in a branch hierarchy. |
| NR-U71-031 | The chart-of-accounts access rule uses a hierarchical parent-of operator against a multi-valued company membership field, so accounts shared across parent entities remain visible to child company users. |
| NR-U71-032 | Each company record may optionally declare a parent company, enabling a hierarchical branch or subsidiary structure within the platform. |
| NR-U71-033 | The company hierarchy stores a materialised ancestor path string that enables efficient hierarchical domain queries (such as parent-of lookups) without recursive SQL joins. |
| NR-U71-034 | A documented intentional elevated-privilege read is used during sequence-gap detection because the underlying query may return record identifiers from sibling or parent companies; the comment confirms this is a deliberate safe bypass for a housekeeping flag, not a data-mutation path. |
| NR-U71-035 | When validating that journal entry accounts are consistent with the posting company's hierarchy, the platform uses an elevated-privilege read to traverse the company ancestor chain; this is a read-only cross-boundary validation, not a data-modification bypass. |
| NR-U71-036 | The user model overrides the default company domain checker so that the domain tests the user's full allowed-company membership list rather than a single company field, reflecting that users can belong to multiple companies. |
