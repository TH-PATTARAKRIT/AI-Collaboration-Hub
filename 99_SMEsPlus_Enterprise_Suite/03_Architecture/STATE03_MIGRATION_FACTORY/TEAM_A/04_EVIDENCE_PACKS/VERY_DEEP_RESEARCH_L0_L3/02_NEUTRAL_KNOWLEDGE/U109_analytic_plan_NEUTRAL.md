# U109 — Analytic Plan Multi-Plan Hierarchy: Neutral Knowledge Layer
**Status**: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

---

## N-U109-01: The Analytic Plan Model
Odoo 19 Community Edition contains a dedicated model for analytic plans. Each plan record represents a named dimension along which financial and operational costs can be tracked. The model supports recursive parent-child relationships, allowing organisations to model layered cost structures.

## N-U109-02: Parent-Store Hierarchy Indexing
The framework provides a built-in mechanism for efficiently querying hierarchical records by maintaining a materialised ancestor path for every record. When this mechanism is active, the system can retrieve entire subtrees without recursive queries at runtime.

## N-U109-03: Self-Referential Parent Relation
Every analytic plan may optionally point to another plan as its parent. The interface enforces a domain restriction to prevent circular references. Plans without a parent are root plans; those with a parent are sub-plans.

## N-U109-04: Stored Ancestor Path
A character field records the full chain of ancestors from the root plan down to each plan. The value is maintained automatically by the framework and is used for subtree search operations.

## N-U109-05: Root Plan Resolution
A computed relation field traverses the ancestor chain to identify the topmost plan in the hierarchy. This root reference is used throughout the system to determine which storage column to read or write when dealing with analytic data.

## N-U109-06: Path-Based Root Calculation
Root resolution works by splitting the stored ancestor path and reading its first element. The result is converted to an integer record reference and used to locate the root plan record.

## N-U109-07: Per-Company Applicability Default
The default applicability setting on a plan is company-dependent, meaning each company operating within the same installation can independently decide whether a given plan is optional, mandatory, or unavailable by default.

## N-U109-08: Installation-Time Default Setting
When the analytic module is first installed, a deferred initialisation step records the value optional as the system-wide default applicability for all plans. This ensures new plans require no action from administrators unless stricter rules are needed.

## N-U109-09: Cached Plan Registry
A cached method maintains the list of all root plans split into the designated project plan and all other plans. The cache is built once per database connection cycle and cleared when plans are created or modified.

## N-U109-10: System Parameter for Project Plan
A system parameter stores the identifier of the plan designated as the project plan. The project plan receives special treatment throughout the system, including a fixed and predictable storage column name. Absence or invalidity of this parameter causes a runtime error.

## N-U109-11: Fixed Column for Project Plan
The project plan always uses a predetermined column name for its association field on analytic line and distribution models. Every other root plan receives a dynamically constructed column name based on its record identifier. This asymmetry ensures the project plan remains compatible with fixed-field views and external integrations.

## N-U109-12: Dynamic Column for Root Plans
When a new root plan is created, the system creates a new stored relational field on every model that participates in analytic distribution. This field links rows on those models to analytic accounts belonging to the root plan.

## N-U109-13: Relational Grouping Field for Sub-Plans
Sub-plans do not receive their own stored column. Instead, the system creates a non-stored computed field that derives its value by walking up the plan tree from the root column. This allows grouping of analytic data by sub-plan depth without duplicating data.

## N-U109-14: Three-State Applicability
Each applicability setting uses one of three values. Optional means the plan field will appear in distribution interfaces but its sum is not validated. Mandatory means a full allocation of 100 is required. Unavailable means the plan field is hidden from the interface entirely.

## N-U109-15: Relevant Plans for Distribution Widgets
When building the list of plans to display in a distribution widget, the system considers only root plans that have at least one analytic account and are not marked as unavailable. Plans whose accounts already appear in an existing distribution are shown as optional regardless of their configured applicability, preventing loss of historical data.

## N-U109-16: Applicability Scoring
The system resolves which applicability rule to apply through a scoring mechanism. Company matching alone contributes a partial score. Business domain matching contributes a full point. The rule with the highest composite score wins; ties fall back to the plan default.

## N-U109-17: JSON Distribution Storage
Analytic distributions are stored as a single JSON object on each participating record. Keys are one or more analytic account identifiers joined by commas, and values are the corresponding allocation percentage expressed as a decimal number.

## N-U109-18: Indexed JSON for Efficient Account Lookup
A specialised index is created on the distribution column using array-extraction techniques to allow the database to efficiently answer queries asking which records reference a given analytic account.

## N-U109-19: Conditional Mandatory Validation
Percentage totals are only validated when a specific context flag is active. When triggered, the system retrieves the list of mandatory plans for the current context and raises an error if the sum of allocations for any mandatory plan does not equal 100.

## N-U109-20: Precision-Aware 100% Check
The validation compares the summed percentage to 100 using a configurable decimal precision named Percentage Analytic. This avoids rejecting distributions that sum to 100 within acceptable rounding tolerance.

## N-U109-21: Percentage Rounding on Save
Each time a distribution is saved, all percentage values are rounded to the Percentage Analytic precision. This normalisation ensures that subsequent equality comparisons between distributions work reliably.

## N-U109-22: Selective Plan Merging
A dedicated method handles the case where a new distribution should update only certain plans while preserving others. It identifies which plans are changing based on an update marker in the data, then rescales both the preserved and the new portions so the overall total remains consistent.

## N-U109-23: Context-Sensitive Analytic Account Field
Analytic line models expose a unified account field whose resolved value depends on a context variable. When a specific plan identifier is provided through context, the field reads and writes the column belonging to that plan. This abstraction allows general-purpose views and code to work with a single field without knowing the active plan.

## N-U109-24: Minimum Account Constraint
Every analytic line record must have at least one plan column populated with a non-null account reference. The system enforces this through a declarative constraint that runs automatically on creation and modification.

## N-U109-25: Single-Account Distribution Helper
A helper method on analytic lines assembles a distribution dictionary from the accounts currently set on the line. The result places all active accounts in a single key and assigns 100 as the percentage, representing full allocation to that combination.

## N-U109-26: Distribution Model Prefill Logic
When a new document is created, the system consults stored distribution models to suggest an initial analytic distribution. Models are evaluated in sequence order and each is skipped if its root plans were already covered by an earlier model. Plans from accepted models are merged using the selective merge logic.

## N-U109-27: Sale Domain Applicability
When the sale module is active, applicability rules can be scoped specifically to sale order lines by selecting the sale order business domain. This allows plans to be mandatory on sales documents without affecting other document types.

## N-U109-28: Distribution Validation on Sale Lines
Sale order line validation passes the product identifier, the sale order business domain, and the company identifier to the generic distribution validator. The validator then evaluates applicability rules specific to that combination.

## N-U109-29: Validation Gate at Sale Confirmation
Analytic distribution validation is called unconditionally for all order lines as part of the sale order confirmation workflow, before the order state is changed to confirmed.

## N-U109-30: Purchase Domain Applicability
The purchase module adds a purchase order business domain to the applicability selection, enabling plan rules that apply specifically to purchase order lines.

## N-U109-31: Validation Gate at Purchase Confirmation
Purchase order confirmation calls the same analytic validation method on all order lines, passing the purchase order domain, before transitioning the order to the confirmed state.

## N-U109-32: Timesheet Domain Applicability
When the timesheet module is active, a timesheet business domain becomes available in applicability rules, allowing organisations to make certain plans mandatory for time tracking entries.

## N-U109-33: Rounding Correction for Stock Distributions
The stock-account module adds a rounding-correction method to the analytic plan. When distributing amounts across multiple analytic lines, the method tracks accumulated rounding errors per plan and corrects the final line to ensure the total distributed amount exactly matches the source amount.

## N-U109-34: Analytic Line Reconciliation for Stock
A method on the analytic account model reconciles the set of existing analytic lines against a target distribution. Matching lines are updated in place, lines no longer present in the distribution are deleted, and new lines are described by return values for the caller to create.

## N-U109-35: Stock Move Analytic Line Preparation
When a stock move is validated, it delegates analytic line creation to the reconciliation method. For movements that represent outgoing stock, the calculated amount is negated before distribution to reflect cost as a debit.

## N-U109-36: Work Centre Distribution Support
When the manufacturing accounting module is active, work centre records inherit the analytic mixin and therefore carry their own distribution field. This allows labour and machine costs generated by manufacturing orders to be distributed across analytic plans at the work centre level.

## N-U109-37: Plan-Level Applicability Rules
A plan may carry multiple applicability rules, each combining a business domain and optional company restriction with a specific applicability setting. The rule collection is filtered to the current company at the interface level.

## N-U109-38: Stored Breadcrumb Name
Each plan stores a concatenated label that combines its own name with the complete names of all its ancestors separated by slashes. The field is computed recursively and stored so it can be displayed in selection lists without joining the full ancestor chain at query time.

## N-U109-39: Root Plan Reference on Accounts
Analytic account records carry a stored computed reference to their root plan. This stored field enables efficient grouping and filtering of accounts by top-level plan without traversing the plan hierarchy at query time.

## N-U109-40: Single-Company Analytic Accounts
Each analytic account is assigned to a company. A constraint prevents reassigning an account to a different company once analytic lines referencing it have been created, avoiding inconsistencies in multi-company reporting.

## N-U109-41: Distribution Model Company Consistency
The system runs a database query to verify that distribution models do not reference company-specific analytic accounts while the model itself is shared across companies or assigned to a different company.

## N-U109-42: Project Plan Parameter Change Handling
Changing the system parameter that designates the project plan triggers automatic synchronisation of all dynamic plan columns across models. The column previously generated for the old project plan is removed as part of this transition.
