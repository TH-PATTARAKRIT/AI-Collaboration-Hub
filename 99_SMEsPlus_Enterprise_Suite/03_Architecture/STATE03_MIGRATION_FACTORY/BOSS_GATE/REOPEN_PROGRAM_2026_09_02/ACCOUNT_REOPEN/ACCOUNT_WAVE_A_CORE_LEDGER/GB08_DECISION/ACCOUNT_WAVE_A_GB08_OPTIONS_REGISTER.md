# ACCOUNT WAVE A — `GB-08` OPTIONS REGISTER

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GB08-001` · Layer 1 clean-room
Date `2026-09-04`

> **This register does not select an option and does not rank them.** Boss is the sole Final Approver.
> Every evidence citation resolves to `ACCOUNT_WAVE_A_GB08_EVIDENCE_TRACE.md`, which is re-runnable.

---

## 0. The four options already in the package — located, cited, and reconciled

**Located.** Four formal options exist in the parent package:

> **File:** `…/ACCOUNT_WAVE_A_CORE_LEDGER/FINAL_CLOSURE/ACCOUNT_WAVE_A_GB08_BOSS_DECISION_PACKAGE.md`
> **Section:** `§10 — Options — evidence-supported, unranked, for Boss selection`
> **Lines:** `275–315` — Option `A` at `280`, `B` at `288`, `C` at `297`, `D` at `305`
> **Published at:** `origin/research/account-wave-a-mcc-2026-09-04-001`, commit `ba0b747`

**Reconciled — and they are not the same four options the round instruction describes.**

| | In-package `A`–`D` | Round-instruction `1`–`4` |
|---|---|---|
| **Question answered** | *What do we freeze, and when?* | *Who owns an FX rate, and in what precedence order is one selected?* |
| **Axis** | **Freeze scope / timing** | **Rate-ownership semantic** |
| **Decidable independently?** | Yes | Yes |

> **They are orthogonal, not alternatives.** A freeze decision without a semantic says *when* SMEsPlus
> stops moving but not *what* it stops on; a semantic without a freeze decision says *what* is true but
> not *when* it becomes binding. **This register therefore carries both axes and the matrix that crosses
> them (§7).** Neither set is discarded.

The semantic set is renumbered `S1`–`S4` (from the round instruction §5) and the freeze set keeps
`A`–`D` (from the package). Both have been **corrected against this session's evidence** where the
original wording is not supported.

---

## 1. What the evidence now says the decision actually is

Three results reshape the option space before any option is read:

| Result | Effect on the options |
|---|---|
| **`GB08-F1`** — `Δ1` does not change which rate row is selected; v18 and v19 `_get_conversion_rate` are otherwise byte-identical | **There is no v18-vs-v19 branch-rate semantic to choose between.** Option `A` loses most of its content: the two candidate "vendor positions" are one position |
| **`GB08-F4` / `GB08-F6`** — the three-tier silent fallback ending in par, and ownership-before-recency precedence, are **stable in all four variants** | The real defects are **not** version-dependent. No freeze choice removes them |
| **`GB08-F7`** — a branch-scoped rate row can be created and displayed and will never value anything | The concrete, present defect is a **dead-data** defect on the branch axis, not a version-divergence defect |

> **Restated decision, evidence-corrected:**
> `GB-08` asks **how SMEsPlus defines canonical FX-rate ownership and rate-selection precedence** —
> specifically **whether a branch may own an exchange rate at all**, and **what happens when no
> applicable rate exists**. The reference implementation answers the first *implicitly and negatively*
> (rates resolve at the root; branch rows are dead) and the second *silently* (fall forward, then to
> par). **Both answers are properties of the reference implementation, not requirements of accounting.**

---

# AXIS 1 — RATE-OWNERSHIP SEMANTIC (`S1`–`S4`)

---

## `S1` — Company-Specific Rate Authority

**Description.** FX-rate ownership is company-scoped. A rate row naming a company wins over a
company-less row. A global / null-company row may be used **only** as an explicitly allowed fallback and
may never override a company-specific rate.

| Field | Content |
|---|---|
| **Evidence supporting** | This is **already the reference implementation's precedence**, verified and stable: `order='company_id.id, name DESC'` (PostgreSQL `NULLS LAST`) puts owned rows before null rows in `_get_rates` in **all four variants**, and `Δ3`'s `ORDER BY currency_id, company_id, …` makes the same choice — `GB08-F6`. Adopting `S1` therefore requires the **least** divergence from every build in the estate |
| **Evidence against** | `S1` says nothing about **which** company owns the rate when the acting company is a branch. On the verified path the answer is always the **root** (`GB08-F1`, `_get_rates` domain `(False, company.root_id.id)`), so `S1` as worded is satisfied by root-only ownership **and** by branch ownership — it does not decide the question `GB-08` was raised for. It also leaves `GB08-F6`'s hazard in place: **a stale owned rate beats a current global rate** |
| **Business impact** | Lowest change cost. A group can maintain one rate table at the top company and let subsidiaries inherit; a subsidiary that needs its own rate sets one and it takes precedence |
| **Accounting impact** | Preserves ownership-first precedence, which is defensible. **Does not address** initial-recognition date semantics, and **does not remove** the par fallback. TAS 21 is the governing standard by name; **the specific paragraph obligations are not verified in this session and are held under the programme's statutory-claim rule** |
| **SaaS / tenant / company impact** | **Does not close `GB08-F8`.** A company-less row remains legal and globally readable, so in a shared database one tenant's global row is a candidate rate for every other tenant unless `S1`'s "explicitly allowed fallback" is defined to exclude cross-tenant rows |
| **Migration impact** | Smallest. No behavioural change to import: existing rate rows keep their meaning. But a pure-behaviour choice produces **no DDL and therefore no migration artefact** — the programme's DDL-shaped migration control cannot see it |
| **Reporting impact** | Unchanged from the reference on the ledger path. `Δ3`'s aggregate path still converts at **today**, so grouped multi-currency totals still disagree with the ledger |
| **Wave B impact** | Unblocks foreign-currency AR **only if** the branch question is answered separately. On its own it leaves `D2` partly open |
| **AAS+ view** | **Insufficient as a complete semantic.** It is a precedence rule, not an ownership rule, and it is silent on the two verified defects (`GB08-F5` par fallback, `GB08-F7` dead branch rows) |
| **PMO view** | Cheapest and most reversible. Traceable. But it will not close `D2` by itself, so it does not move Wave B |
| **Risk level** | **MEDIUM** — low delivery risk, high residual-defect risk |
| **What Boss is deciding** | That ownership precedence is *company-over-global*, and that a global rate is a permitted fallback |
| **What remains unknown** | Whether "company" means the root only or any company in the tree; whether cross-tenant global rows are permitted; what happens when no rate exists |

---

## `S2` — Branch / Operating-Unit Preference Within the Company Boundary

**Description.** Branch or operating-unit rate preference may exist, but **only inside an owning company
boundary**. It must never cross a tenant or company boundary. Branch hierarchy and inheritance rules
must be explicit.

| Field | Content |
|---|---|
| **Evidence supporting** | The **data model already permits it**: `res_currency_rate.company_id` is nullable, editable, defaults to the root but is **not constrained to it**, and the record rule `('company_id','parent_of',company_ids)` **shows a branch's own rows to that branch** — `GB08-F7`, `GB08-F8`. The `Δ1` hunk shows an author in the v18 line **intended** exactly this (`# Get rates through branch if selected company`) |
| **Evidence against** | **No reference build implements it.** `Δ1` was written to do this and **does not** — `_get_rates` collapses the branch back to `company.root_id` and the selected row is unchanged (`GB08-F1`). Consequently, adopting `S2` means building a resolver the estate does not contain, in **all 22 roots**, and it means **fixing** `GB08-F7` rather than inheriting anything |
| **Business impact** | This is the option that answers a real multi-branch Thai requirement — a branch that transacts in its own foreign-currency market and books at its own rate. It is also the largest build |
| **Accounting impact** | Requires an explicit answer to *"whose spot rate is the transaction's spot rate"* and to consolidation: branch-preferred resolution makes branch reporting coherent and makes **group** consolidation require an explicit re-translation step. Realised FX must reproduce the **original** resolution or reversals will not net to zero |
| **SaaS / tenant / company impact** | Strongest tenant story of the four **if and only if** the "never cross the boundary" clause is enforced by construction rather than by a record rule — `GB08-F8` shows the current rule deliberately punches a hole in the boundary for `company_id = False` |
| **Migration impact** | **Highest.** Any existing branch-scoped rate row in a live database is currently inert (`GB08-F7`); switching to `S2` makes it **live**. Figures that were being valued at the root rate would silently start being valued at the branch rate. **This is a data-dependent, retrospective revaluation with no DDL change and therefore no migration artefact to review** |
| **Reporting impact** | Branch P&L becomes internally coherent; group aggregates require an explicit translation policy. `Δ3` would have to be replaced, not merely avoided, because it is hardcoded to `root_id` |
| **Wave B impact** | Fully closes `D2` — and only after the resolver is specified, which is design work Wave A must not start |
| **AAS+ view** | **The only option that treats the branch as a first-class accounting entity.** Also the only one that requires SMEsPlus to own a resolver outright rather than inherit one. AAS+ regards the existing dead-data state (`GB08-F7`) as unacceptable in **any** option, so `S2` at least confronts it |
| **PMO view** | Largest scope, largest migration risk, and it depends on a business ruling PMO cannot supply. Not startable in Wave A |
| **Risk level** | **HIGH** |
| **What Boss is deciding** | That a branch is permitted to hold and be valued at its own exchange rate — a **business** ruling about how SMEsPlus's multi-branch customers actually operate |
| **What remains unknown** | Whether any live database already holds branch-scoped rate rows (not determinable from source); the inheritance direction when a branch has no rate of its own; the consolidation translation policy |

---

## `S3` — Tenant-Standard Global Rate With Controlled Override

**Description.** A tenant-level standard FX rate is canonical by default. Company or branch override is
allowed only through explicit configuration, an audit trail, and deterministic precedence.

| Field | Content |
|---|---|
| **Evidence supporting** | Matches how a group in practice wants rates administered — one published table, exceptions by exception. The reference implementation's ordering already gives deterministic precedence (`GB08-F6`), so the "deterministic" half is achievable |
| **Evidence against** | **The reference implementation has no tenant concept on this table.** Its "global" row is `company_id IS NULL`, and the global record rule admits it to **every** user in the database (`GB08-F8`). A null-company row is therefore **not** tenant-standard — it is **database-wide**. `S3` cannot be built on the existing null semantics without either adding a tenant discriminator or forbidding `NULL` outright. It also inverts `GB08-F6`: today the *owned* row wins; `S3` makes the *standard* row win unless overridden |
| **Business impact** | Best administrative story: one rate table to maintain, exceptions visible. Requires an override workflow that does not exist |
| **Accounting impact** | An override with an audit trail is the strongest control of the four — it makes *why this rate* answerable at the row level. Nothing else here provides that |
| **SaaS / tenant / company impact** | **Directly collides with the verified cross-tenant path.** `S3` is only safe if `company_id = NULL` is redefined or removed. Choosing `S3` therefore forces a decision on `GB-03`'s null axis as a precondition |
| **Migration impact** | Every existing `company_id IS NULL` row must be assigned an owner or an explicit tenant scope. That **is** a data migration with an artefact — the only option here that produces one |
| **Reporting impact** | Cleanest: a group total has one defensible rate basis, and every deviation is a recorded override |
| **Wave B impact** | Closes `D2` for AR, but only after the override model exists |
| **AAS+ view** | Strongest **control** semantics; weakest fit to the reference data model. AAS+ notes that its audit-trail requirement is the only element in the whole option space that would make an FX rate's provenance reviewable |
| **PMO view** | Medium build, but it drags `GB-03` into scope as a hard precondition. That is a scope expansion Boss should see before choosing it |
| **Risk level** | **MEDIUM-HIGH** |
| **What Boss is deciding** | That the tenant, not the company, is the default owner of a rate — and that overrides are a controlled, audited exception |
| **What remains unknown** | What "tenant" means in the SMEsPlus deployment model (`T0-04` is open); how many `NULL`-company rows exist in any live database |

---

## `S4` — No Implicit Preference / Explicit Rate Resolution Required

**Description.** The system must not infer an ambiguous rate precedence. Any posting or revaluation that
needs an FX rate **blocks** until the applicable rate context is explicit. A missing rate is an error,
never a substituted value.

| Field | Content |
|---|---|
| **Evidence supporting** | It is the only option that addresses the **verified** defects rather than choosing around them. All three are properties of the reference implementation, not of accounting: the **three-tier silent fallback** ending in par (`GB08-F5`, stable in all four variants), the **future-dated tier 2** (`GB08-F5`), and **ownership-over-recency** letting a stale owned rate beat a current one (`GB08-F6`). A number produced by `COALESCE(…, 1.0)` is not an exchange rate; it is the absence of one, rendered as `1` |
| **Evidence against** | It is the **largest divergence** from every build in the estate and forfeits reference compatibility on a hot path. It converts a class of silent wrong answers into a class of **blocked postings** — an operational cost that falls on users, not on the ledger. It also does not, by itself, say **who owns** a rate; it must be combined with one of `S1`–`S3` to be a complete semantic |
| **Business impact** | Postings stop when rate data is missing. For a business that books foreign-currency invoices daily, the rate table becomes an operational prerequisite, not a convenience |
| **Accounting impact** | **Highest correctness.** Removes the possibility of a foreign-currency amount silently recognised at par or at a future rate. Makes the FX-rate table an explicit input to recognition rather than a best-effort lookup |
| **SaaS / tenant / company impact** | Neutral on ownership; strongly positive on isolation, because "explicit" necessarily excludes an unowned, database-wide row as an implicit source |
| **Migration impact** | Historical rows valued under the reference's fallbacks **cannot be reproduced** by an `S4` resolver — by construction, since `S4` refuses to produce what they contain. Comparatives require a stated policy: re-derive and restate, or freeze historical values as-is |
| **Reporting impact** | A report either has a rate basis for every line or refuses to render the total. No more "a number that looks like a ledger total and is not one" |
| **Wave B impact** | Closes `D2`'s **failure** semantics fully; leaves `D2`'s **ownership** semantics open unless paired |
| **AAS+ view** | **The par fallback is not a design choice, it is a defect, and AAS+ does not treat its removal as optional under any option.** `S4` is the only option that states it as a rule rather than an aspiration |
| **PMO view** | Deliverable, and mostly a *refusal* rather than a build — cheaper than `S2` or `S3`. The cost lands in change management and support, which is a real cost Boss should price |
| **Risk level** | **MEDIUM** — low technical risk, high operational-acceptance risk |
| **What Boss is deciding** | That SMEsPlus will refuse to post rather than substitute a rate — accepting the operational consequence |
| **What remains unknown** | The volume of postings that would block in practice (not determinable from source); the restatement policy for historical fallback-valued rows |

---

# AXIS 2 — FREEZE SCOPE AND TIMING (`A`–`D`, from the package)

Reproduced from `FINAL_CLOSURE/ACCOUNT_WAVE_A_GB08_BOSS_DECISION_PACKAGE.md:275–315` and corrected
against this session's evidence.

## `A` — Freeze the current verified semantic (to one named tree's behaviour)

| Field | Content |
|---|---|
| **Evidence supporting** | The semantics are pinned to a seven-line diff and a named SQL block; there is no ambiguity about what would be frozen |
| **Evidence against — CORRECTED** | The package argued this "selects between two vendor positions". **`GB08-F1` removes that premise: on the verified path there is only one position.** What is left to freeze is the *stable* semantic — root-scoped resolution, ownership-before-recency, three-tier silent fallback — i.e. **freezing the defects in place**. `GB08-F10` also shows a named tree cannot be identified from its directory path |
| **Risk level** | **HIGH** — it now means adopting `GB08-F5`, `GB08-F6` and `GB08-F7` as SMEsPlus design |
| **Status** | **Materially weakened by this session's evidence** |

## `B` — Freeze the interface only, defer the implementation detail

| Field | Content |
|---|---|
| **Evidence supporting** | The **schema is stable across all four variants** (`unique (name, currency_id, company_id)`, nullable `company_id`, `_get_rates` domain and order), so an interface freeze rests on the part of the evidence that does not vary. Unblocks Wave B's data contracts without deciding the semantic |
| **Evidence against** | It does not answer the AR foreign-currency questions in the dependency map, which need the resolution rule, not only its signature. **And `GB08-F5` means the interface itself is contested**: does the contract return *"a rate or an explicit failure"* (`S4`) or *"always a number"* (every reference build)? That is a semantic decision hiding inside an interface freeze |
| **Risk level** | **MEDIUM** |
| **Status** | Viable, but it contains a concealed `S4`-vs-not decision that must be surfaced |

## `C` — Hold the build freeze pending additional evidence

| Field | Content |
|---|---|
| **Evidence supporting** | Two gaps remain open and cheap: **(i)** no executed test exists (`MCU-01`) — and `GB08-F1` is now a *derivation* that an executed test would confirm or overturn in hours; **(ii)** the target build is undeclared, and `GB08-F10` shows path names cannot substitute for the declaration |
| **Evidence against** | It leaves Wave B's foreign-currency AR scope open, which is most of foreign-currency AR. **And this session materially reduces what more research can buy**: the reference behaviour has now converged to **one** semantic across 4 distinct variants. The remaining questions are a **business ruling** and a **programme declaration**, neither of which is research |
| **Risk level** | **MEDIUM** |
| **Status** | Still viable; its yield is now smaller and more precisely known |

## `D` — Reject reference-specific behaviour, define the SMEsPlus clean-room semantic

| Field | Content |
|---|---|
| **Evidence supporting** | **Strengthened by this session.** All four verified pathologies — the database-wide company-less row (`GB08-F8`), the par fallback (`GB08-F4`/`F5`), `today`-dated aggregate conversion (`Δ3`), and dead branch-scoped rows (`GB08-F7`) — are **properties of the reference implementation, not requirements of accounting**, and **none of them is removed by any version choice**. Consistent with the clean-room rule that reference behaviour is evidence, not authority |
| **Evidence against** | Largest work; forfeits reference compatibility on a core path; must still answer `GB-03`'s null axis before it can be specified |
| **Risk level** | **MEDIUM-HIGH** |
| **Status** | **Strengthened.** `D` is the container in which `S1`–`S4` are actually chosen |

---

## 7. The matrix — how the two axes cross

`S` = semantic (what the rule is) · `A`–`D` = freeze (what is fixed, and when)

| | `A` freeze a build | `B` freeze the interface | `C` hold | `D` clean-room |
|---|---|---|---|---|
| **`S1`** company-owned wins | Coherent — it *is* the current behaviour, defects included | Coherent | Coherent | Coherent, minimal divergence |
| **`S2`** branch preference | **Incoherent** — no build implements it (`GB08-F1`) | Coherent, defers the hard part | Coherent | **The only home for `S2`** |
| **`S3`** tenant standard + override | **Incoherent** — no build has a tenant concept here | Coherent | Coherent | **The only home for `S3`** |
| **`S4`** explicit or block | **Incoherent** — every build falls back silently | Contradicts `B`'s "always a number" reading | Coherent | **The only home for `S4`** |

> **Reading:** Option `A` is coherent with exactly one semantic — `S1` — and only by adopting the
> reference's defects with it. **`S2`, `S3` and `S4` all require `D`.** That is not a recommendation;
> it is what the matrix shows.

---

## 8. What is *not* a `GB-08` Boss decision

Carried forward from the package §11 and re-verified. These must not be routed into `GB-08` to make it
look decidable:

| Item | Owner | This session's status |
|---|---|---|
| Which build SMEsPlus actually ships | **Programme declaration** — a fact to be stated | Still undeclared; `GB08-F10` shows path names cannot supply it |
| An executed test on a running root + branch instance | **Research** — `MCU-01` | Open. Its value rose: it now tests `GB08-F1` |
| `Δ3`'s `today`-dated conversion, par fallback and rule bypass | **Verified defects** (`MCU-20` / `BW-31`) | Re-verified; widened by `GB08-F9`, `GB08-F11` |
| `GB-03`'s null axis | **Open verified defect** | Re-verified at rule and ACL level (`GB08-F8`). It is a **precondition** of `S3` and `D` |
| The dead branch-scoped rate row | **Verified defect** — `GB08-F7`, **new** | Not an option; it is broken under every option and must be fixed or forbidden |
