# 05 — ACCOUNT WAVE A — REVIEWER FINDING → ENUMERATION RULE MAP

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001` · Layer 1 clean-room
Executable command forms: `LAYER2_MC_EVIDENCE/MCE01_ENUMERATION_RULE_COMMANDS.md`

**Purpose.** For every material finding class a reviewer discovered, identify the deterministic rule
that should have surfaced it before review. After this file, the primary method must no longer depend
on reviewers to discover entire finding classes.

**Test each rule must pass:** it names a population, returns a count without judgement, and would
have surfaced the finding *as a matter of course*, not as a matter of insight.

---

## 1. The map

| Reviewer finding | Missed search dimension | New rule | Population | Evidence | Repeatable check |
|---|---|---|---|---|---|
| `AC-03` a parent's journal is usable by a descendant's entry; `16` L9 "tenant-safe: yes" contradicted | **Company-scoping override declarations** were never listed | **`ER-21a`** List every company-scoping domain override in the domain and record which variant each model uses (exact / parent-inclusive / collection-based). Any model whose variant admits a **parent or a null** owner is a boundary candidate | `P-21a` = **11** | `MCE-005` | One pass; returns 11 rows |
| `X-05` posted counterparty rewritten across all companies with an explicit lock bypass | **Named control-bypass tokens** were never listed | **`ER-21e`** List every named bypass/skip token in the domain and, for each, the call sites that pass it and the control it defeats | `P-21e` = **8** sites / 4 tokens | `MCE-005` | One pass; returns 8 rows |
| `X-04` numbering scan runs company-blind under elevated privilege; `B-05` approval skipped under elevation | **Privilege-elevation sites** were never listed | **`ER-21b`** List every privilege-elevation site. For each, record whether the query it guards carries a company clause. **Elevation without a company clause is a boundary defect until proven otherwise** | `P-21b` = **93** | `MCE-005` | One pass; returns 93 sites |
| `X-06` exigibility guard tests the root, not the company; `FX-08` writer/resolver disagree | **Root-vs-company divergence sites** were never listed | **`ER-21c`** List every site resolving an owner to a *root* rather than the acting owner, and pair each with the writer that populates the same field. **Any writer/reader pair using different rules is a defect** | `P-21c` = **37** | `MCE-005`, `MCE-007` | One pass; returns 37 sites |
| `X-06` the partial-reconciliation model has no record rule | **Record-scoping-rule coverage per model** was never tabulated | **`ER-16a`** For every model in the Wave scope, tabulate: record-scoping rules (count) × write rights granted (roles). **Any model with write rights and zero scoping rules is a boundary defect** | `P-16a` = **31** rules / **20** models | `MCE-004` | 12-row table; found 3 Wave A models with zero |
| `AC-02` raw SQL bypasses record scoping and defaults to par | **Raw-SQL sites** were never listed | **`ER-21d`** List every raw-SQL execution site. Each bypasses record scoping by construction; record what it selects and what it defaults to when empty | `P-21d` = **62** | `MCE-005`, `MCE-008` | One pass; returns 62 sites |
| `AC-01` a routine accounting role holds full rights on the rate table | **Access-control rows** were never tabulated against role seniority | **`ER-16`** Tabulate every access-control row for the Wave scope. Flag any row granting create/write/delete on a **measurement-defining** entity to a role below administrator | `P-16` = **132** (35 Wave A) | `MCE-002`, `MCE-008` | One pass; found the rate-table row |
| `AC-06` one config key is really a class; no company dimension | **Database-wide configuration keys** were never listed | **`ER-10a`** List every database-wide configuration key the domain reads or writes. Each is company-blind by construction; classify each material / non-material | `P-10a` = **5**, 2 material | `MCE-006` | One pass; **population closed** |
| `SB-05` a null-owner rate is matched for every company | **Ownership-field nullability** was never tabulated | **`ER-10b`** For every owning reference on a measurement-defining entity, record whether it is mandatory, its default, and whether the scoping rule admits null. **Nullable owner + null-admitting rule = cross-boundary by design** | subset of `P-10` = **397** | `MCE-007`, `MCE-009` | Per-entity table |
| `FX-07` the revaluation guard tests only for zero | **Failure and guard paths** were never enumerated | **`ER-23`** List every explicit failure path. For each guard on a **measured value**, record the exact predicate. **A guard testing one sentinel does not cover a second** | `P-23` = **153** | `MCE-002` | One pass; ~128 still unassessed |
| `EV-002`-class findings: uniqueness enforced only in the application | **Enforcement layer** was never recorded | **`ER-15`** For every integrity rule, record the layer that enforces it: storage constraint · record scoping · application check · configuration · none. This is `DR-AC-01` made mechanical | `P-15` = **11** storage vs `P-15a` = **32** application | `MCE-002` | Two passes; ratio is the finding |
| `G06`'s 17 unbounded negatives that six reviewers walked past | Negative claims were reviewed **incidentally**, not scanned | **`ER-24`** Scan **every file in the package manifest** for negative-strength tokens; triage each hit; declare the scope of every surviving claim | `P-24` = **577** hits / **64** files | `MCE-011` | One pass; **denominator is the manifest, never a list** |
| `MCE-010` register `02`'s rows and its own summary disagree | Internal arithmetic was never re-derived | **`ER-00`** Recompute every published ratio from the rows that produced it. **A headline figure that cannot be re-derived from its own register is void** | all registers | `MCE-010` | One pass; found a 4-row break |
| `MCE-012` a stale working copy made a present standard look absent | The **evidence surface itself** was never verified current | **`ER-01`** Before any negative claim, verify the working surface is current against its origin and record the commit. A negative result from a stale surface is not a finding | evidence base | `MCE-012` | Two commands |

## 2. Rules covering populations no finding has yet come from

Added because the population is bounded and unassessed, not because something went wrong. These are
the places the next finding is most likely to come from.

| Rule | Population | Denominator | Why it belongs |
|---|---|---|---|
| `ER-12` | State transitions | `UNBOUNDED` → derive by tracing writes to the 6 declared states across the 750 methods | The only population whose unboundedness is a **method** gap rather than a property of the system (file `02` §4) |
| `ER-11` | Actions and buttons | 59 actions / 55 buttons | Every user-reachable entry point to a ledger mutation; **zero** currently carry evidence |
| `ER-20` | Cross-module ledger producers | 38 modules | Producers write ledger facts under their own rules; only ~7 families examined |
| `ER-20a` | Scheduled jobs | 2 | Unattended ledger mutation, by definition without a user in scope |
| `ER-14a` | Method surface | 750 | The residual space; bounded, ~60 cited |

## 3. The rule that generalises all of them

Every rule above is one instance of a single test:

> **`ER-CORE`. For each population: name it, state the command that counts it, record the number,
> and traverse it. A population that cannot be counted is declared `UNBOUNDED`, and no percentage is
> stated over it.**

The parent method's defect was not insufficient rigour. It applied `ER-CORE` to exactly one
population — the one it had written itself — and to none of the nineteen the findings came from.

## 4. Adoption note for other SMEsPlus modules

`ER-16a`, `ER-21a`, `ER-21b`, `ER-21c`, `ER-21d`, `ER-21e` and `ER-10a` are **domain-independent**.
They ask about scoping, elevation, bypass and configuration, not about accounting. Any module with a
company or tenant boundary — Inventory, Purchase, Sale, Manufacturing, HR — can run all seven
unchanged, and each returns a bounded count on the first pass.

`ER-00`, `ER-01` and `ER-24` are **governance** rules and should apply to every research package
regardless of domain.

`ER-15` and `ER-23` are the mechanical form of the affirmative-claim standard `DR-AC-01` proposed by
`G09` §5: *cite the enforcement layer*. `ER-15` produces the layer; `ER-23` produces the predicate.
Recommended for Boss ratification together.
