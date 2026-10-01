# U01 Base Platform — Neutral Knowledge (clean-room layer)

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
> Baseline: Odoo 19 Community (named once, here only)
> Scope: platform foundation (companies, access control, users, contacts, currencies, numbering, scheduler, automation, settings, attachments and data ownership)
> Each statement is tagged with an id that links to technical claims held in the restricted layer.
> Statements describe what the system must do and why; no implementation names appear here.

## CAP-U01-01 Multi-company data scope

### WHAT
- [N-U01-001] One database can serve several companies; each company has its own name, its own legal contact record, a default currency and an optional parent company.
- [N-U01-002] Companies form a tree: a company may have branches, a branch has exactly one parent, and the top of each tree is called the root company.
- [N-U01-003] Every user has a list of companies they may work in and one default company; during a session the user activates some of those companies, and the first activated company owns newly created data.
- [N-U01-004] A company is created together with its legal contact record when none is supplied, and may have its own anonymous public user account, created on demand.

### WHY
- [N-U01-005] Company scoping keeps one entity's data out of view of staff who work only for other entities, while still allowing shared reference data that every entity can use.

### BUSINESS RULE
- [N-U01-006] A record without a company is shared by all companies; a record with a company is visible when that company, or one of its branches, is among the activated companies.
- [N-U01-007] Records of a parent company are usable from its branches; records of a branch are not usable from the parent unless the branch is itself activated.
- [N-U01-008] Records that point to other records must stay inside one company: every linked record must be shared or belong to the same company (or an ancestor); a save that breaks this is refused with a message saying that no company crossover is allowed.
- [N-U01-009] A user's default company must be among the companies the user is allowed to use; an active user cannot be saved otherwise.
- [N-U01-010] The currency of a branch always equals the currency of its root company; it is copied when the branch is created and pushed to all branches when the root changes.
- [N-U01-011] The parent of a company cannot be changed after creation and a company cannot be duplicated; a new company must be created instead.
- [N-U01-012] Archiving a company archives its branches; a company cannot be archived while it is the default company of an active user.
- [N-U01-013] A newly created company is automatically added to the allowed companies of the person who created it and of the built-in system administrator account.
- [N-U01-014] A contact record linked to a person who owns user accounts keeps the company of those accounts; a contact's company is refused if it conflicts with the companies of its accounts, and a company change on a contact is pushed to its child contacts.

### STATE
- [N-U01-015] A company is either active or archived; the archive state cascades from a company to its branches.

### OPTIONALITY
- [N-U01-016] A one-company database needs no branch or switcher configuration; a display group for multi-company users is added to a user only when the user has more than one allowed company and removed again when the count falls to one, and it changes what is shown, not what is permitted.
- [N-U01-017] Company-specific values exist for selected fields (for example payment terms and accounts on a contact); each company keeps its own value with a database-wide fallback for companies that have none.

### DEPENDENCY
- [N-U01-018] The web client keeps the list of activated companies in the browser and sends it with every request; the server refuses a request that activates a company the user is not allowed to use.
- [N-U01-019] Accounting, stock, sales, purchasing and other applications add their own company scoping rules and company-specific settings; those belong to the units of those applications.

### CONSTRAINT
- [N-U01-020] Company names are unique across the database.
- [N-U01-021] Numbering sequences and default values may be company-specific; when both a company-specific and a shared entry exist, the company-specific one wins for the current company.
- [N-U01-022] Attachments store a company, but who may see them follows the record they are attached to.

### RISK
- [N-U01-023] Code that runs with elevated privileges (the built-in superuser mode) ignores company scoping, so integrations and automations in that mode can read or write across companies.
- [N-U01-024] Scheduled jobs run with the full list of allowed companies of the job owner rather than one active company; company-specific processing must select the company explicitly.
- [N-U01-025] When company scoping refuses a record the error text may suggest switching company; users without access to the target company only learn that they have no access.

### UNKNOWN
- [N-U01-026] Detailed browser behaviour of the company switcher (ordering, persistence, branch selection) was only partly read and needs runtime confirmation.
- [N-U01-027] The effect on existing data of removing a company from a user's allowed list, while that user created or owns records, is not determined.

## CAP-U01-02 Record rules engine

### WHAT
- [N-U01-028] A record rule is a filter attached to a type of record that limits which individual records a person may read, change, create or delete; each rule states which of the four operations it governs.
- [N-U01-029] A rule applies to everyone (global rule) or only to members of named permission groups (group rule).

### WHY
- [N-U01-030] Rules give row-level confidentiality and company isolation that model-level permissions cannot express.

### BUSINESS RULE
- [N-U01-031] All global rules that apply to a record type must be satisfied at the same time.
- [N-U01-032] Group rules are alternatives: a person must satisfy at least one rule among those of the groups they belong to, and that combined group result must hold together with all global rules.
- [N-U01-033] A group rule counts only for a person who belongs to one of its groups; otherwise it is ignored for that person.
- [N-U01-034] When no active rule governs a record type and operation, no record-level restriction exists; a rule with an empty filter allows everything.
- [N-U01-035] A rule filter may refer to the current user, the list of activated companies and the current company; it is evaluated per user and per company selection.
- [N-U01-036] A rule filter is validated when saved, a rule must grant at least one of the four operations, and no rule may target the record-rule type itself.
- [N-U01-037] Record types that reuse data of another record type also honour the rules of that parent type for the linked parent record.
- [N-U01-038] Elevated-privilege mode ignores all record rules; so does any code deliberately run in that mode.

### STATE
- [N-U01-039] A rule can be switched off without deleting it; if a seeded rule is deleted, a later update of the owning module may recreate it.

### OPTIONALITY
- [N-U01-040] Changing the activated companies changes what a user sees without any change to the rules.

### DEPENDENCY
- [N-U01-041] The website application adds the current website to the rule evaluation and to the caching of rule results; every other application contributes its own rules, which the base platform does not control.
- [N-U01-042] The base platform seeds rules only for its own record types: contacts, bank accounts, currency rates, users, companies, saved filters, personal defaults, API keys, devices, user settings, password wizards and embedded actions.

### CONSTRAINT
- [N-U01-043] The base platform seeds thirty-two rules: nine apply to everyone and twenty-three to specific groups, as confirmed in the reference database.
- [N-U01-044] Seven base rules scope by company: contacts, bank accounts, currency rates, users, and three company-record rules for employees, portal users and public users.
- [N-U01-045] Contacts of internal users are always visible whatever the company, so that those users stay selectable; other contacts follow the company rule.
- [N-U01-046] Portal and public users may only read the contact tree of their own commercial entity.
- [N-U01-047] Each user may see and delete only their own API keys; administrators may view all keys to revoke them; public users cannot touch keys.
- [N-U01-048] Personal items (saved filters, defaults, user settings, devices, device logs) are limited to their owner, with administrators seeing all.
- [N-U01-049] Company records: employees, portal and public users see only the activated companies; the access-rights manager group sees every company.

### RISK
- [N-U01-050] Because group rules are alternatives, a person who is both a standard user and an access-rights manager sees every company in the company record.
- [N-U01-051] Companyless records skip company scoping in every rule that includes the shared alternative, so a wrongly empty company on master data can expose it to other companies.
- [N-U01-052] Rule changes clear the caches of the whole registry, which can slow a busy system.
- [N-U01-053] Access errors list the failing rules and sample records only for technical users in debug mode; others see a generic message.

### UNKNOWN
- [N-U01-054] About five hundred further rules in the reference database belong to other applications and were not studied here; effective scoping of an application's records must be read from that application's own unit.

## CAP-U01-03 Access control (groups, model access, field and menu visibility)

### WHAT
- [N-U01-055] Permission groups collect users; a group can imply other groups so that members of the stronger group automatically belong to the implied ones.
- [N-U01-056] Model access entries state, per group, which of read, change, create and delete are allowed on a type of record.
- [N-U01-057] There are three mutually exclusive user types: internal (employees), portal (limited external users) and public (anonymous visitors).

### WHY
- [N-U01-058] Separating internal, portal and public users lets the same database serve staff and outsiders with different default rights.

### BUSINESS RULE
- [N-U01-059] A person may perform an operation on a record type when any group they belong to, directly or through implication, has an entry granting it; entries with no group apply to everybody, and the base platform seeds six such entries that all grant nothing.
- [N-U01-060] The check order is: elevated-privilege mode skips everything; otherwise model-level permission is checked first and only when granted are record rules applied to the individual records.
- [N-U01-061] A user cannot belong to two of the three user types at once, directly or through implied groups; this is checked when a user or a group is saved.
- [N-U01-062] Removing the last system administrator is refused (the check is skipped while the base module itself is being updated).
- [N-U01-063] The technical-features group takes effect only when debug mode is on.
- [N-U01-064] Menu entries are shown when they have no group or the user belongs to one of their groups, and only when the target of the menu is a record type the user may read.
- [N-U01-065] Contextual actions are listed only for users who belong to the action's groups and may read the target record type.
- [N-U01-066] A field can be restricted to groups; reading it without membership is refused or the field is omitted; some fields are marked as forbidden to everybody.
- [N-U01-067] A user may always read a short list of fields on their own record and write an even shorter list, regardless of model-level permissions.
- [N-U01-068] New internal users receive the internal-user group plus the groups implied by an editable template group named for default access of new users.
- [N-U01-069] A permission group that is tied to a settings switch cannot be deleted; group names are unique inside a privilege and cannot start with a minus sign.

### STATE
- [N-U01-070] A user's effective groups are the explicit memberships plus everything they imply; membership is recomputed and caches are cleared whenever groups change.

### OPTIONALITY
- [N-U01-071] The user form offers a simple choice between ordinary user and administrator in addition to detailed group selection.

### DEPENDENCY
- [N-U01-072] Every application adds its own groups and model access entries under named privileges; the reference database holds one hundred nineteen groups and twenty-seven privileges, of which twelve groups and two privileges come from the base platform.
- [N-U01-073] The base platform seeds one hundred forty-six model access entries (confirmed); the reference database holds two thousand ten in total.

### CONSTRAINT
- [N-U01-074] Seeded base groups: ordinary user, access-rights manager, system administrator, multi-company display, multi-currency display, technical features, export permission, contact creation permission, bypass of rich-text sanitising, portal, public and the template group for new users.
- [N-U01-075] The system administrator group implies the access-rights manager group, which implies ordinary user.

### RISK
- [N-U01-076] Access-rights managers can edit groups, model access entries and record rules and create or change users, so they can grant themselves almost any right; they are effectively privileged.
- [N-U01-077] Because membership is transitive, removing a group from a user who still obtains it by implication is refused.
- [N-U01-078] Seeded public and portal template accounts must never be given employee groups; the disjoint-type check is the only guard.

### UNKNOWN
- [N-U01-079] How the browser decides to hide form fields and buttons from group information was not read and needs runtime confirmation.

## CAP-U01-04 Users and authentication-related lifecycle

### WHAT
- [N-U01-080] A user account is a login plus technical settings and is always attached to exactly one contact record that carries the person's name, email and language.
- [N-U01-081] Users are internal, portal or public; the flag marking an external user is derived automatically from group membership.

### WHY
- [N-U01-082] Separating account data from contact data lets the same person be customer, vendor and user without duplicating the contact.

### BUSINESS RULE
- [N-U01-083] Logins are unique and matched exactly.
- [N-U01-084] Passwords are stored only as slow salted hashes with a minimum work factor; weaker stored forms are upgraded transparently at the next successful login; empty new passwords are refused, and the field documentation states that leaving the password blank is meant to prevent the account from signing in.
- [N-U01-085] Users cannot change their own password through the ordinary form; they must use a dedicated step that asks for the old password, and sensitive actions (own password change, API key creation or removal, device revocation) require a fresh password confirmation younger than ten minutes.
- [N-U01-086] Access-rights managers set other users' passwords through a separate wizard; the temporary value is cleared afterwards.
- [N-U01-087] Creating an internal user creates a settings record and a generated initials avatar when no image is given; a global contact stays global and any other contact takes the company of the user.
- [N-U01-088] Nobody can deactivate the account they are logged in with or reactivate the built-in superuser; reactivating a user reactivates its contact first.
- [N-U01-089] The built-in superuser, the default administrator, the signup template user and the public user cannot be deleted; accounts are normally archived instead.
- [N-U01-090] A contact tied to an active user cannot be archived or deleted until the user is archived.
- [N-U01-091] A portal user may request deletion of their own account: the login is replaced, the password cleared, API keys removed, user and contact archived and the user queued for a daily deletion job that works in batches and keeps the contact if documents still reference it.
- [N-U01-092] Repeated failed sign-ins from one network address put that address on a cooldown during which attempts are ignored; the thresholds come from two database parameters and the counters live in each server process, not in shared storage.
- [N-U01-093] A session stays valid only while the account's id, login, stored password hash and active flag are unchanged, so a password or login change or an archive signs the user out.
- [N-U01-094] The latest sign-in time of each user is recorded, and a daily cleanup keeps only the most recent entry per user.
- [N-U01-095] API keys can be created only by internal users; non-administrators must give an expiry date capped by the longest key lifetime of their groups (ninety days for the internal-user group); administrators may create keys without expiry; keys are random, shown once, stored hashed and purged by cleanup after expiry.
- [N-U01-096] Creating or revoking API keys by program rather than by screen is disabled unless a database parameter enables it (administrators exempt) and is limited to ten keys per user by default.
- [N-U01-097] A user changes default company only among companies they are allowed to use; a change of default company to a disallowed one, made by the user on their own account, is silently ignored.
- [N-U01-098] When a system administrator signs in through a browser, the stored base web address is refreshed to the address used unless it has been frozen.

### STATE
- [N-U01-099] A user is active or archived; the contact's active state follows when the user is archived through the user screen and is reactivated before the user.

### OPTIONALITY
- [N-U01-100] Additional sign-in methods, second factors, passkeys, external identity providers and signup are supplied by other modules and change the credential check; they are outside this unit.

### DEPENDENCY
- [N-U01-101] Inviting users by email address needs the discussion application, because it relies on a normalised email field.
- [N-U01-102] Several applications widen the lists of fields a user may read or write on their own record.

### CONSTRAINT
- [N-U01-103] At least one administrator must exist; a home action that needs a selected record or reloads the page is refused.

### RISK
- [N-U01-104] The seed data creates a default administrator with a trivially guessable initial password; it must be changed before any real use.
- [N-U01-105] The cooldown counters are not shared between server processes, so brute-force protection is approximate on multi-process deployments.
- [N-U01-106] A signed-in administrator can silently change the base web address, which feeds links in outgoing documents.

### UNKNOWN
- [N-U01-107] Whether the default administrator password in the reference database has been changed was not examined, because credential values are out of scope for research queries.
- [N-U01-108] Second-factor, passkey, external-provider and signup behaviour were deliberately not read.

## CAP-U01-05 Partner master data

### WHAT
- [N-U01-109] A contact is a person or a company; contacts form a tree in which people belong to a company, and each has an address type (contact, invoice, delivery or other).
- [N-U01-110] A contact carries tags, industry, tax identifier, company registration number, language, time zone, salesperson, website, notes, bank accounts and optional company-specific commercial settings.

### WHY
- [N-U01-111] A single contact tree lets sales, purchasing, accounting and user management share one identity per party and keeps commercial data consistent between a company and its people.

### BUSINESS RULE
- [N-U01-112] Contacts of address type contact must have a name; other address types may be nameless and are displayed by their type.
- [N-U01-113] The contact hierarchy cannot be cyclic.
- [N-U01-114] The commercial entity of a contact is the nearest company above it, or the contact itself if it is a company or has no parent.
- [N-U01-115] A tax identifier, company registration number and industry belong to the commercial entity; people below a company inherit them, and applications extend this list with payment terms, accounts, price list and credit limit.
- [N-U01-116] Synchronisation runs both ways: a tax identifier edited on a person goes up to the company and from there to all people; the address of a contact-type child equals the address of its parent, edits on either side propagate, and the first contact added to a company without address gives that company its address.
- [N-U01-117] A child contact starts with the company, language and, for people, the salesperson of its parent.
- [N-U01-118] The tax identifier is not unique: the system only warns about another contact with the same value, including archived contacts and common prefix variants, and a slash means no tax identifier; the same soft warning exists for the registration number; no uniqueness is enforced on reference, name or email.
- [N-U01-119] A contact barcode must be unique.
- [N-U01-120] Bank account numbers are normalised, unique per account holder, and the choice of account holder is limited to companies and top-level contacts; deleting an account archives it; the send-money flag is off by default; when a contact is renamed, account holder names that equalled the old name follow.
- [N-U01-121] Automatic creation of a bank account refuses to create accounts for the database's own companies unless explicitly allowed, and prefers an existing account of the commercial entity.
- [N-U01-122] Contacts linked to an active user cannot be archived or deleted.
- [N-U01-123] Merging contacts handles at most three at once, refuses a parent with its own child and contacts tied to more than one user, requires identical email unless an administrator runs it, and keeps by default the oldest active contact as destination.
- [N-U01-124] A merge repoints every reference to the destination (database links, attachments, followers, activities, messages, external identifiers, reference fields and company-specific values), merges bank accounts, fills empty destination fields from sources, adds up summable counters supplied by applications, then deletes the sources; conflicting dependants that would break uniqueness are deleted; the base platform only logs the merge on the server, while a note listing the merged contacts is posted on the destination contact when the discussion application is installed.
- [N-U01-125] The merge assistant can find candidate groups by email, name, tax identifier, company flag or parent, and an automatic mode merges every group, committing after each group.
- [N-U01-126] Only people with contact-creation permission may run the merge assistant.

### STATE
- [N-U01-127] A contact is active or archived; archived contacts still count in duplicate warnings so that they can be reactivated instead of recreated.

### OPTIONALITY
- [N-U01-128] Format validation of tax identifiers by country is not part of the base platform; it comes from a separate module that is not installed in the reference database.
- [N-U01-129] Copying a contact appends a copy marker to its name.

### DEPENDENCY
- [N-U01-130] Accounting, sales, purchasing, stock, website and loyalty applications extend commercial fields, merge behaviour and company-specific settings of contacts.

### CONSTRAINT
- [N-U01-131] A contact that represents a company record must keep that company assigned as its own company.

### RISK
- [N-U01-132] A merge cannot be undone and the automatic mode commits group by group, so an interruption leaves a partially merged set.
- [N-U01-133] Absence of uniqueness on tax identifier, reference and email means duplicates are possible and must be controlled by process.

### UNKNOWN
- [N-U01-134] Contributions of the installed address-extension, auto-complete and country-specific modules to contact validation were not studied.

## CAP-U01-06 Currency and exchange rates

### WHAT
- [N-U01-135] A currency has an international three-letter code, symbol and symbol position, a rounding factor and a derived number of decimals; exchange rates are dated entries per currency and per root company.
- [N-U01-136] The reference database lists one hundred seventy currencies of which two are active, and holds no rate entries.

### WHY
- [N-U01-137] Rounding and dated rates make amounts in different currencies comparable and reproducible at a given date.

### BUSINESS RULE
- [N-U01-138] A currency code is unique and its rounding factor must be positive; decimals are derived from the rounding factor.
- [N-U01-139] Amounts are rounded to multiples of the rounding factor, and equality tests compare rounded amounts rather than raw differences.
- [N-U01-140] There is at most one rate per currency, company and day, and every rate must be strictly positive.
- [N-U01-141] Rates are stored against a reference currency and displayed relative to the company currency; entering a rate that differs by more than twenty percent from the previous one raises a warning.
- [N-U01-142] Rates may be held only by root companies, so branches use the rate of their root; a rate without company is shared by all companies.
- [N-U01-143] A conversion uses the latest rate dated on or before the conversion date; if none exists before that date it uses the earliest rate; if the currency has no rate at all it converts one to one.
- [N-U01-144] Converted amounts are rounded to the target currency's rounding unless rounding is switched off for the call.
- [N-U01-145] A currency that is the currency of a company cannot be deactivated, and choosing a currency for a company activates it.

### STATE
- [N-U01-146] A currency is active or archived; the number of active currencies drives whether the multi-currency display group is on for internal users.

### OPTIONALITY
- [N-U01-147] When more than one currency is active, every internal user gets the multi-currency display group; when one remains it is removed; the pricing application additionally enables price lists, and archiving a currency archives its price lists.
- [N-U01-148] No automatic exchange-rate download was found in the base platform or other community modules examined; rates are entered or imported manually.

### DEPENDENCY
- [N-U01-149] The accounting application forbids reducing the decimals of a currency once accounting entries use it and builds multi-currency reporting tables on the same rates.

### CONSTRAINT
- [N-U01-150] Everyone including portal and public users may read currencies and rates; only system administrators may change them.

### RISK
- [N-U01-151] A currency without any rate converts at one to one without warning, so missing rates silently misstate foreign amounts.
- [N-U01-152] The reference database company currency differs from the base platform seed value, so any assumption about the seed currency would be wrong.

### UNKNOWN
- [N-U01-153] Accounting-side revaluation and rate usage on documents is studied by the accounting unit and is not covered here.

## CAP-U01-07 Numbering sequences

### WHAT
- [N-U01-154] A numbering sequence generates the next reference text from a prefix, a padded counter, a suffix and a step, optionally per company and optionally split into date ranges.

### WHY
- [N-U01-155] Controlled numbering gives documents unique, readable and, where required, gap-free identifiers.

### BUSINESS RULE
- [N-U01-156] Two implementations exist: the standard one is fast but numbers consumed by an aborted transaction are lost, so gaps can appear; the gap-free one locks the sequence row, never skips a number on rollback and is slower.
- [N-U01-157] Prefix and suffix may contain date placeholders for year, month, day, week and similar parts, in current, document-date and range-date variants; an invalid placeholder is refused when the number is drawn.
- [N-U01-158] With date ranges, a range is created automatically for the date being numbered when none exists, covering the calendar year and trimmed so ranges do not overlap, and each range counts separately.
- [N-U01-159] Looking up a sequence by code uses the sequence of the current company if there is one, otherwise a shared sequence; if none exists the lookup returns nothing without raising an error.
- [N-U01-160] A step of zero is refused; changing the implementation recreates the underlying counters; administrators may reset the next number.
- [N-U01-161] Internal users may read sequences; only system administrators may create or change them; drawing a number requires read access.

### STATE
- [N-U01-162] A sequence is active or inactive and its counter only moves forward by the step.

### OPTIONALITY
- [N-U01-163] Date ranges and company are optional per sequence.

### DEPENDENCY
- [N-U01-164] The base platform seeds no sequences of its own; the thirty-four sequences of the reference database come from other applications, two of them gap-free and one using date ranges, with thirteen having no company.

### CONSTRAINT
- [N-U01-165] There is no company isolation rule on sequences in the base platform; company separation relies on the company lookup only.

### RISK
- [N-U01-166] The gap-free implementation fails at once rather than waiting if another transaction holds the same sequence, which can surface as concurrency errors under load.
- [N-U01-167] A sequence of one company can be drawn by identity from another company by anyone who can read it, because no company rule hides it.

### UNKNOWN
- [N-U01-168] Which applications rely on gap-free numbering for legal reasons is for the applications' units to determine.

## CAP-U01-08 Scheduler framework

### WHAT
- [N-U01-169] A scheduled job couples a server action with a repeat interval in minutes, hours, days, weeks or months, a next and last execution time, a priority, an owner user and an active flag.

### WHY
- [N-U01-170] Background jobs perform recurring maintenance and business processing without user interaction.

### BUSINESS RULE
- [N-U01-171] A job is ready when it is active and its next time has passed or a one-off trigger is pending; ready jobs run ordered by recent failure count, then priority, then age.
- [N-U01-172] Each job is locked while it runs and processed in its own transaction, so two workers never run the same job and a worker skips a job already taken.
- [N-U01-173] A job runs as its owner, with no selected company, which means all allowed companies of the owner; the context carries the last successful run time and the job identity.
- [N-U01-174] A job may report progress in batches; it is run repeatedly until at least ten runs and ten seconds have elapsed, and when work remains it is rescheduled immediately by a trigger.
- [N-U01-175] A failure without committed progress counts as a failed run; three consecutive timeouts without progress also count as failed; a failed job is rescheduled normally.
- [N-U01-176] A job is deactivated only after at least five consecutive failures and a first failure older than seven days; the administrator is notified, through the discussion channel when that application is installed.
- [N-U01-177] A successful or partial run resets the failure count; the next time is advanced by the interval in the owner's time zone so the hour of day is kept across daylight saving changes.
- [N-U01-178] Jobs are skipped when the code version differs from the database version or modules are being installed or updated; if that state lasts over five hours the module states are reset.
- [N-U01-179] A job can be run manually: it executes in the current web request but in its own transaction, is refused if already running, and requires change permission on jobs.
- [N-U01-180] A running job cannot be edited or deleted.
- [N-U01-181] Other code can request a one-off run at a given time; such triggers are removed when the job starts and stale ones of inactive jobs are purged after a week.

### STATE
- [N-U01-182] A job is idle, ready, running, partially done (re-queued) or failed; fully done and partial runs reset the failure counter and failure advances it.

### OPTIONALITY
- [N-U01-183] Jobs can be switched on and off by their owners or by code; on a neutralised database code cannot switch them back on.

### DEPENDENCY
- [N-U01-184] The base platform seeds two daily jobs: a cleanup that runs every registered cleanup routine in random order, and a deletion of portal users who asked to leave, in batches of fifty; the reference database holds fifty-four jobs, forty-seven active, all owned by the superuser.
- [N-U01-185] The cleanup job refuses to run unless started by the scheduler under an administrator, and a failure in one routine rolls back that routine only.

### CONSTRAINT
- [N-U01-186] The interval must be a positive number; only system administrators can manage jobs.

### RISK
- [N-U01-187] Jobs owned by the superuser bypass access rules and company scoping.
- [N-U01-188] A persistently failing job is silently deactivated after a week of failures unless the administrator notice is read.
- [N-U01-189] Actual execution cadence depends on running background workers and was not tested.

### UNKNOWN
- [N-U01-190] How jobs behave under multiple concurrent workers and during module updates in the target deployment needs runtime confirmation.

## CAP-U01-09 Server actions and automation rules

### WHAT
- [N-U01-191] A server action is a stored operation on a record type: update a record, create a record, duplicate a record, run code, send a notification to an outside address, or run several actions; other applications add email, follower, activity and message actions.
- [N-U01-192] An automation rule attaches actions to an event on a record type: creation, update, deletion, archive, field-specific changes, a date reached, an incoming or outgoing message, a live form change, or an external call.

### WHY
- [N-U01-193] Automation lets administrators react to business events without writing a module.

### BUSINESS RULE
- [N-U01-194] A rule may have a condition before the change and a condition after the change; actions run only on records that satisfy them and only when a watched field changed, or on any change when none are listed.
- [N-U01-195] A rule runs at most once per record within one chain of events, which stops recursion; messages produced by an automation do not retrigger message rules.
- [N-U01-196] Actions of a rule must target the same record type as the rule; live-change rules accept only code actions; deletion rules cannot use email, follower or activity actions; message rules need a record type with discussion support.
- [N-U01-197] Time-based rules compare a date field with a delay before or after, in minutes, hours, days or months, optionally counting working days of a calendar; they run from a scheduled job that is active only when at least one such rule exists and that adapts its interval to the shortest delay between one minute and four hours.
- [N-U01-198] A failure in an action of a create, update or delete rule stops the user's operation and rolls it back; in time-based processing a failing rule is rolled back, the others continue and the last error makes the job fail.
- [N-U01-199] An external-call rule exposes a public address with a random secret identifier; calling it needs no sign-in, finds the record through a stored expression and runs the rule; the identifier can be rotated and calls can be logged.
- [N-U01-200] A server action may be limited to groups; without groups the caller needs change permission on the record type and the records; code is editable only by system administrators, checked for syntax, run in a restricted interpreter and its previous versions are kept.
- [N-U01-201] Rules and their actions are found and evaluated with elevated privileges, and the actions themselves run after the permission check in elevated mode.
- [N-U01-202] Notification actions to an outside address send the selected fields after the transaction commits, do not wait more than a second and are cancelled on rollback.

### STATE
- [N-U01-203] A rule is active or archived; saving a rule that affects event handling re-installs the interception of the affected record types and tells other workers to reload.

### OPTIONALITY
- [N-U01-204] The reference database has no automation rules; the scheduled job for time-based rules exists but is switched off; one hundred sixty-eight server actions exist, all of the run-code kind, none belonging to automation.

### DEPENDENCY
- [N-U01-205] Automation rules depend on the discussion, SMS, digest and resource-calendar applications; message and calendar features come from them.

### CONSTRAINT
- [N-U01-206] Only system administrators can manage automation rules; rules have no company field and no company rule, so they apply across all companies.

### RISK
- [N-U01-207] Because actions and the external-call address run in elevated mode, whoever can create a rule or knows an address can cause changes beyond their own permissions.
- [N-U01-208] Every create, update or delete of a watched record type passes through the rule engine, so heavy rules affect performance, and a rule change needs workers to reload.

### UNKNOWN
- [N-U01-209] Rule behaviour with real data, on live change in forms and under heavy write load needs runtime confirmation.

## CAP-U01-10 Configuration parameters and settings flow

### WHAT
- [N-U01-210] The settings screen is a transient form whose fields, by naming convention, switch applications on or off, switch permission groups on or off, store default values, store database-wide parameters or edit fields of the current company.
- [N-U01-211] The base settings add toggles for data import, calendar synchronisation, mail plugins, external login providers, inter-company rules, telephony, image library, SMS, partner auto-complete, geolocation, captcha, address auto-complete, multi-currency, and the display effect, plus company report footer and layout and a profiling time window.

### WHY
- [N-U01-212] One screen lets an administrator tailor the installation without technical file edits.

### BUSINESS RULE
- [N-U01-213] Saving settings requires the access-rights manager capability; the screen itself is limited to system administrators, and a settings record cannot be duplicated.
- [N-U01-214] Group switches add or remove an implied group on the internal-user group, so they affect all internal users globally.
- [N-U01-215] Application switches install the chosen applications immediately at the end of the save; unchecking one opens an uninstall confirmation step instead of acting at once.
- [N-U01-216] Default-value fields store a database-wide default for all users and companies; parameter fields store a database-wide key and value; related company fields edit the company chosen on the screen, which is the current company by default.
- [N-U01-217] The settings screen shows counts of companies, active internal users and languages and whether the chosen company is a root.
- [N-U01-218] The default group for new users can be edited from the settings screen and is created on demand if missing.

### STATE
- [N-U01-219] Parameters are plain key and value pairs; setting a value to nothing deletes the key; unchanged values are not rewritten.

### OPTIONALITY
- [N-U01-220] Most toggles are optional; module and group toggles take effect for the whole database, not for one company.

### DEPENDENCY
- [N-U01-221] The setup module is installed automatically with the base and supplies the settings screen, a data endpoint restricted to access-rights managers for user counts and pending invitations, and the display-effect parameter.

### CONSTRAINT
- [N-U01-222] A set of parameters is created at database creation (a secret, an identifier, the creation date, the web address and the two sign-in cooldown values); these cannot be deleted or renamed.
- [N-U01-223] Parameter values are cached and read access to the parameter table is limited to system administrators, while code reads them in elevated mode.
- [N-U01-224] The reference database holds forty-five parameters.

### RISK
- [N-U01-225] Some parameters hold secrets or drive security behaviour (the secret used in session tokens, the web address, cooldown values, programmatic key enabling), so write access to the parameter table is highly privileged.
- [N-U01-226] Changing a group or application switch is global and, for removal, can be hard to reverse.

### UNKNOWN
- [N-U01-227] The data endpoint code for key indicators in the setup module was not read.

## CAP-U01-11 Attachments, external identifiers and language activation

### WHAT
- [N-U01-228] An attachment is a file or web link attached to a record by record type, record identity and optionally a field; files are stored on disk keyed by content hash and the company is stamped on creation.
- [N-U01-229] Every record created from module data files has an external identifier made of the owning module and a name, unique across the database.
- [N-U01-230] Languages are catalogue entries that can be activated; the reference database lists ninety-three of which only the base language is active.

### WHY
- [N-U01-231] Attachment rules prevent leaking documents of records the user cannot see; external identifiers let updates, imports and integrations find the same record reliably; language activation controls which translations are loaded and offered.

### BUSINESS RULE
- [N-U01-232] Attachments follow the access of the record they belong to: reading needs read access on the record, creating, changing and deleting need change access; attachments marked public are readable by anybody; attachments without a record are reachable only by their creator and administrators; attachments tied to a field also need field access unless the user is a system administrator.
- [N-U01-233] Searches for attachments return only those the user may read; model-level entries give internal users full rights and portal and public users none, so outsiders depend on access tokens or on public attachments served through web routes.
- [N-U01-234] Link attachments that could be served as web pages can be changed only by members of the serving groups unless the user is an administrator; an attachment cannot be attached to itself.
- [N-U01-235] Records loaded from module data files remain owned by their module: on module update they are rewritten unless their identifier is flagged as non-updatable, in which case user edits survive; records no longer present in a module's data are deleted on update only when not flagged non-updatable.
- [N-U01-236] Identifiers cannot contain spaces; the non-updatable flag can be toggled by anyone allowed to change the record; uninstalling a module deletes records only that module owns and requires system administrator rights.
- [N-U01-237] At least one language must remain active, the base language cannot be deleted, and a language that is active or is the user's own language cannot be deleted; language codes and names are unique.
- [N-U01-238] Installing a language activates it and loads its translations for all installed applications, with an option to overwrite customised translations; only system administrators can do this.
- [N-U01-239] The user context language falls back from the user's language to the request language, the company contact language, the default language, then any installed language.

### STATE
- [N-U01-240] An external identifier is updatable or non-updatable; a language is active or inactive.

### OPTIONALITY
- [N-U01-241] Storage backend for attachment content (disk or database) is selectable; external storage can be added by overriding.

### DEPENDENCY
- [N-U01-242] The reference database holds about fifty-four thousand external identifiers and about three and a half thousand attachments, mostly link-type attachments; base-seeded rules and company data are flagged non-updatable while its model access entries and groups are mostly updatable.

### CONSTRAINT
- [N-U01-243] Seed counts confirmed in the reference database: six thousand six hundred eighty external identifiers belong to the base module, of which one thousand two hundred ninety-four are non-updatable.

### RISK
- [N-U01-244] Non-updatable seeded records no longer follow module corrections, so an upgrade can leave stale rules or settings.
- [N-U01-245] Attachment company stamping does not restrict access; relying on it for company separation would be wrong.

### UNKNOWN
- [N-U01-246] Public sharing by access token and cleanup of unreferenced files were only skimmed and need runtime confirmation.
