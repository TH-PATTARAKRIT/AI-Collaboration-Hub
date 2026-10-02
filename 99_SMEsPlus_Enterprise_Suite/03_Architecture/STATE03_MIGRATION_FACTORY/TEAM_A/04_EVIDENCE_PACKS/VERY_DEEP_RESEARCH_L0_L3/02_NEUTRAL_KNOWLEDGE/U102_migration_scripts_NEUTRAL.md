# U102 Neutral Knowledge — Migration Scripts
## DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U102-001 | The framework uses a dedicated manager component to orchestrate migration of modules; each migration file must expose a single callable accepting a database cursor and a version string |
| NR-U102-002 | Three execution stages exist for migration scripts: a pre-stage that runs before module data loads, a post-stage that runs after module initialisation, and an end-stage that runs after all modules in the upgrade batch have been processed |
| NR-U102-003 | A specially named zero-version folder causes its scripts to execute on every version upgrade; in the pre-stage these run first; in post and end stages they run last |
| NR-U102-004 | Script discovery scans two alternative subdirectory names per module; an additional external namespace allows third-party upgrade script packages to contribute scripts under their own file system path |
| NR-U102-005 | The migration executor loads each qualifying script file, verifies the required callable exists, inspects its parameter signature for compliance, and then invokes it passing the cursor and the previously installed version string |
| NR-U102-006 | Absence of the required callable causes an attribute error at runtime; a non-conforming parameter signature causes a type error — both are enforced before the callable is invoked |
| NR-U102-007 | Version directory names are validated against a regular expression that accepts both server-prefixed versions and module-only version strings; a directory named after the test suite is explicitly excluded |
| NR-U102-008 | Scripts for a given version directory are only executed when the currently installed version is strictly less than that directory's version and the directory's version does not exceed the module's declared current version |
| NR-U102-009 | A pre-stage migration in the purchasing module converts two relational column values into property records in the generic properties table, then removes the source columns with a cascading drop |
| NR-U102-010 | The column-conversion helper checks whether the source column exists in the schema before proceeding, providing an idempotency guard against re-running the migration on a database where the column was already removed |
| NR-U102-011 | A post-stage migration in the project module constructs an ORM environment under the superuser identity and uses the external identifier resolution mechanism to activate a mail template record |
| NR-U102-012 | A pre-stage migration in the analytic module queries system parameters and the analytic plan table to determine dynamic column names, then uses the SQL utility layer to drop and recreate foreign key constraints with a stricter deletion policy |
| NR-U102-013 | A pre-stage migration in the expense module combines ORM environment creation with direct parameterised SQL to locate mail notification subtype records by external identifier and set their default flag to false |
| NR-U102-014 | A pre-stage migration in the website recruitment module runs a regular expression replacement directly against a stored view definition column in the database to remove a CSRF token element from customised view records |
| NR-U102-015 | A pre-stage migration in a localisation module deletes records from the model data registry to prevent the ORM from removing records that are in use, then renames a series of data records by updating their external identifier names |
| NR-U102-016 | A post-stage migration in a localisation module resolves tax tags through an ORM model method and then remaps foreign key values in a many-to-many relation table via direct parameterised SQL |
| NR-U102-017 | A pre-stage migration in a localisation module resolves references using the safe raise-if-not-found flag, then deletes report column and line records and clears code fields via direct SQL |
| NR-U102-018 | A post-stage migration in a localisation module uses the domain composition utility to build complex search domains, then updates account type fields through the ORM with per-company context |
| NR-U102-019 | An end-stage migration in a localisation module reloads the chart of accounts template for each matching company using the try-loading mechanism with force-create disabled |
| NR-U102-020 | An end-stage migration in a France localisation module follows the same chart-template reload pattern, confirming this as the standard approach for chart of accounts re-synchronisation after all modules have settled |
| NR-U102-021 | A module may place migration scripts under an alternative subdirectory name; this alternative path is treated equivalently to the primary migrations path during script discovery |
| NR-U102-022 | A leave management module demonstrates the alternative subdirectory pattern for correcting access rule domain expressions via a SQL join with the model data registry |
| NR-U102-023 | The stock module declares a pre-install hook in its manifest that deletes stale model data entries for stock models before module data loads |
| NR-U102-024 | The stock module post-install hook assigns a default delivery confirmation mail template to every company that does not yet have one, using external identifier lookup |
| NR-U102-025 | The stock module uninstall hook deletes the number sequences associated with all picking type records when the module is removed |
| NR-U102-026 | The accounting module post-install hook computes the fiscal country field on all existing companies and creates batch payment number sequences for companies that lack them |
| NR-U102-027 | The manufacturing module pre-install hook adds two columns directly to the stock moves table via raw cursor DDL statements before the ORM processes the module, preventing out-of-memory failures on large databases during computed stored field population |
| NR-U102-028 | The manufacturing module post-install hook backfills warehouse manufacturing data for warehouses that existed before the module was installed, by searching for warehouses lacking a manufacturing pull route and enabling resupply |
| NR-U102-029 | The sales module post-install hook synchronises cron job active states from system parameters and sets up downpayment accounts based on chart template data for each company |
| NR-U102-030 | A column existence utility queries the database catalogue to determine whether a column is present in a table, enabling migration scripts to guard against re-execution on already-migrated databases |
| NR-U102-031 | A column rename utility wraps the rename column DDL statement using identifier-safe quoting, providing a canonical way to rename columns in migration scripts |
| NR-U102-032 | Constraint management utilities wrap drop-constraint and add-foreign-key DDL statements with identifier-safe quoting and logging, used by migration scripts to modify referential integrity rules |
