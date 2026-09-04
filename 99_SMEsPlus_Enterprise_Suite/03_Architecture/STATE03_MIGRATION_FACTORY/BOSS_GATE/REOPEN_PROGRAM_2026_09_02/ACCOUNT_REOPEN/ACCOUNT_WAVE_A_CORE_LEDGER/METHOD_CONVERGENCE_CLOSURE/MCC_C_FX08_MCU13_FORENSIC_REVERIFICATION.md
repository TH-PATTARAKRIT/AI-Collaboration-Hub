# MCC_C — `FX-08` / `MCU-13` FORENSIC RE-VERIFICATION

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Layer 1 clean-room
Tolerance = 0 · Depth `VERY DEEP / L99999.99999`
Layer 2 citations: `LAYER2_MCC_EVIDENCE/MCC_E00`

> **Recommendation only. Boss is the sole Final Approver. No `PASS` is declared here.**
> **`G03` is not edited.** Per `DR-NC-06` this file governs where it conflicts with `G03`, for the
> claims addressed here and for no others.

---

## 1. What was re-verified, and how

`FX-08` was re-verified **from first principles** — not by re-reading `G03`, but by re-deriving the
mechanism from primary source and only then comparing. Every source root named in `MCE-000` was
re-tested for reachability this session, and one root was added that no prior round had searched.

The re-verification was executed against **eight** evidence layers, because a conclusion supported by
one layer is not deep enough when another can contradict it:

`UI / configuration` · `model / business logic` · `access / security` · `database constraint / raw
SQL` · `framework ORM core` · `shipped data` · `cross-version` · `company-boundary structure`.

---

## 2. `FX-08` as recorded, restated exactly

`G03` §3, verbatim in substance:

> *"When the acting company is not its own root, the writer stores `company_id = <branch>` and the
> resolver looks for `company_id ∈ (NULL, <root>)`. The two do not intersect. A rate maintained at
> branch level is invisible to the conversion that consumes it."*

Disposition `VERIFIED DEFECT`. Registered as balanced-but-wrong case `BW-16`, distinguished from
`BW-01` on the ground that *"the tenant has evidence that rates are loaded"*.

The claim has **two halves**. They are re-verified separately, because they do not fail together.

---

## 3. Resolver half — `RE-CONFIRMED, and extended`

**`VERIFIED FACT`.** The posting-time resolver filters on the **root** company or the company-less
row. Read directly at source this session; unchanged from `G03`.

**Extension `G03` did not record.** The resolver has **three** outcomes, not two:

1. the latest rate at or before the date, in `(NULL, root)` scope;
2. failing that, **the earliest rate ever recorded** for that currency in the same scope — a
   *second* query, ordered ascending, with **no date bound at all**;
3. failing that, **par**.

> Outcome 2 is the more dangerous of the two silent fallbacks and it is **not** the one the programme
> has been tracking. A posting dated today, in a database whose only rate for that currency is from
> years ago, is valued at **that historical rate**, silently, and looks entirely normal. Par at least
> announces itself to an attentive reader; a real-but-wrong historical rate does not.

Recorded as a new balanced-but-wrong case in `MCC_G`. It is a resolver property, independent of the
branch question, and it applies to **every** company including single-company installations.

---

## 4. Writer half — `CONTRADICTED`

This is the substance of `MCU-13`.

### 4.1 The constraint exists, and it is exactly on point

**`VERIFIED FACT`.** The rate model carries a Python constraint on the company field which raises
whenever the named company has a parent, with the message *"Currency rates should only be created for
main companies"*. It fires on **create** always, and on **write** whenever the company field is in the
written values.

**A rate row cannot be created against a branch company through the ORM.**

### 4.2 The parent round's stated reason for not acting on it does not survive

`MCD-02` declined to invalidate `FX-08` because *"a constraint can be bypassed by paths that do not go
through it (raw SQL: 62 sites)."* Tested:

> **`VERIFIED ABSENCE` — there is no raw-SQL write to the rate table anywhere in the source root.**
> Across **1,752** module directories plus the framework core, every raw-SQL site touching the rate
> table is a read. The 62 accounting raw-SQL sites do not touch it. Scope declared in `MCC_E00`
> §`MCC-E-001`/`MCC-E-010`.

**The constraint has no raw-SQL bypass. The reason for the hold was correct to state and is now
answered.**

### 4.3 Every other route to a branch-scoped row, tested

| Route | Result |
|---|---|
| ORM create / write | constraint fires |
| Elevated privilege | constraints are user-independent |
| A context flag disabling constraints | **none exists in the ORM core**; the validation routine has no skip parameter and no caller passes one |
| Data / XML / CSV loading, module install | loads through the ORM; constraint fires |
| Migration scripts | 5 exist; **none touches the rate table** |
| A localisation or custom module overriding the constraint | **none** in either module tree; the one localisation extending the rate model adds a UI warning only |
| Project custom modules (all three v18-line copies) | **none touches the rate table at all** |
| **Create as a root, write rates, then demote to a branch** | **BLOCKED.** The company model refuses *any* write containing the parent field, unconditionally: *"The company hierarchy cannot be changed."* |
| Raw-SQL rewrite of the company hierarchy | no non-test site writes the company table's hierarchy columns |
| **Module upgrade over rows that already exist** | **OPEN — see §7** |

### 4.4 The writer `G03` actually cited writes a root company, and fails loudly if it cannot

- The **scheduled** rate feed searches companies with **no parent** — root companies only.
- The **manual** settings button passes the **acting** company. If that company is a branch, the
  create raises the constraint, and the surrounding handler re-raises user-facing errors rather than
  swallowing them. **The branch user gets an explicit refusal, not a silent wrong write.**
- The **model default** for the company field is the acting company's **root**.

> **`MCE-007`'s central narrative — "the automated feed writes a branch, and this is the production
> path" — is CONTRADICTED, and `MCX-02` was right to withdraw it.** This round adds the reason it
> could never have been true: the write would have raised.

### 4.5 The economic premise does not hold either — and this is the deeper answer

**`VERIFIED FACT`, four enforcement layers.** The company currency is a **root-delegated field**. A
branch company is forced to carry its root's currency: copied down at creation, propagated on every
change to the root, enforced by a model constraint, and shown read-only in the form for any company
that has a parent. The accounting addon extends the same delegation to the **fiscal year definition**.

> **A branch cannot have its own company currency.** Therefore resolving a branch's foreign-currency
> postings against the **root's** rate table is not a scope mismatch — it is the **semantically
> correct** source, because the measurement target is the root's currency by construction.
>
> `G03` reasoned about a branch maintaining its own rates for its own currency. **That configuration
> is not constructible on this build.** The defect it describes has no state in which it can occur.

---

## 5. `MCU-13` protocol record

| Stage | Content |
|---|---|
| **Claim** | `FX-08`: writer stores a branch company; resolver reads root-or-null; the two do not intersect; silent mis-valuation follows |
| **Original evidence** | Resolver filter; the manual-settings writer passing the acting company; two framework helpers disagreeing on scope. All real, all re-read, none disputed as *facts* |
| **Reopened evidence** | A model constraint forbidding a branch-scoped row, present in the source and in **0 of the 64** baseline files — independently re-verified by this session, including against semantic variants, not only the identifier |
| **Search boundary** | Declared pattern over 1,752 module directories + framework core, `.py`/`.xml`/`.csv`; three false-negative modes tested; false positives recorded |
| **Re-test** | 10 bypass routes closed with declared scope; 1 open; the economic premise independently foreclosed by root-delegation of the company currency |
| **Contradiction** | The writer half is contradicted at the model layer, at the hierarchy layer, and at the currency-structure layer — three independent contradictions, any one of which is sufficient |
| **Final disposition** | §6 |

---

## 6. `FX-08` disposition

> ## `PARTIALLY VERIFIED` — the resolver half stands, the writer half is `CONTRADICTED`, and the composite defect as recorded is `NOT REPRODUCIBLE` on this build

| Component | Disposition |
|---|---|
| Resolver filters root-or-null | **`VERIFIED FACT`** — re-confirmed, and **extended**: three outcomes, not two |
| Two framework helpers disagree on company scope | **`VERIFIED FACT`** — re-confirmed; and the disagreement is wider than `G03` knew (§ `MCC_B` §5) |
| A rate can be stored against a branch | **`CONTRADICTED`** — forbidden at the model layer, unreachable by every enumerated route but one |
| The stored branch rate is then invisible to the resolver | **`NOT REPRODUCIBLE`** — the antecedent cannot be established |
| A branch maintains rates for its own currency | **`CONTRADICTED`** — a branch cannot have its own currency |
| **`BW-16` as registered** | **WITHDRAWN as a distinct case.** Its residual content is absorbed by `BW-01` (no rate) and by the new historical-fallback case in `MCC_G` |

### What this does and does not mean

**It does not exonerate the rate table.** The other half of `GB-03` — the **company-less** rate row —
is untouched by everything above, and it is worse than `FX-08` ever was: admitted by an explicit
disjunct in the record rule, creatable by a routine accounting role, resolved by six paths and
refused by six others, and — in a demo-seeded database — **already present 162 times**.

**It does mean one of the four blockers reported "closed with evidence" was closed on a mechanism
that does not exist**, and that this was found only because a fresh reviewer read a constraint layer
nobody had enumerated. `FX-08` was not *wrong to raise*; it was **right about the resolver and wrong
about the writer**, and no round could see that until the surface was bounded.

---

## 7. The one open residual — and it is real

> ### `MCC-C-R1` — rows that predate the constraint are never revalidated. `D — UNKNOWN`.

Python constraints run on write. They are **not** re-run over existing rows at module upgrade. If a
database ever held a branch-scoped rate row — because it was created on a version without this
constraint, or imported from one, or restored from a backup taken then — that row survives the
upgrade **silently**, and `FX-08`'s mechanism becomes live exactly as `G03` describes it.

**Two facts make this more than theoretical:**

1. **The maintenance path would keep such a row alive without ever revalidating it.** When the rate
   feed finds an existing row for the currency and date, it writes only the rate value — the company
   field is not in the written values, so the constraint does not fire. A pre-existing branch row is
   therefore **silently maintained forever**.
2. **The pre-v18 baseline cannot be established from the sources available here.** No v16 or v14
   framework core exists in the searched roots — only project custom addons. Whether the constraint
   is new in v18 is **`C — NOT YET SEARCHED`**, and must not be reported as "the constraint has always
   existed".

**Cheap, decisive test, and it is not research:** on any migrated or restored SMEsPlus database, count
rate rows whose company has a parent. A non-zero count converts `MCC-C-R1` from `UNKNOWN` to a live
data defect; zero closes it for that database. **This is a migration acceptance check, and it belongs
in the migration factory's checklist regardless of the outcome here.**

---

## 8. Tolerance-zero position after this round

| id | Boundary | Position |
|---|---|---|
| `T0-07` | Cross-company rate resolution in raw SQL, outside every record rule, with an undeclared par fallback | **CHARACTERISED — and it is worse than registered.** The raw-SQL rate reads are **8**, spread over three addons; the record-rule bypass is total on all of them; the fallbacks are **par in four places and a historical rate in one**; and the two halves of the system disagree about the company-less row. **UNRESOLVED** |
| `FX-08`'s contribution to `T0-04` (tenant isolation) | — | **REDUCED on the branch axis, UNCHANGED on the null axis** |

**Tolerance remains 0 and is not met.** The re-verification narrowed the defect; it did not close the
boundary.

---

## 9. Accounting consequence, per verified path

| Consequence | Reachable? | Path |
|---|---|---|
| Balanced but economically wrong posting | **YES** | company-less row resolved at posting time; or the undated earliest-rate fallback; or par |
| Wrong company-currency valuation | **YES** | same |
| Wrong realised FX | **YES** | same resolver serves settlement |
| Wrong unrealised FX | **YES** | revaluation uses the posting-time resolver, so it inherits every fallback |
| Wrong opening / migration valuation | **YES, and it is the highest-exposure case** | a demo-seeded or template-cloned database carries 162 company-less rows before any user acts |
| Wrong tax / reporting amount | **YES** | the reporting currency table **excludes** the company-less row that the posting **included**, then substitutes par |
| Cross-company contamination | **YES, by construction** | the company-less row is resolved by every company; the raw-SQL consolidation helper additionally **attributes** each such row to every company |
| Cross-tenant contamination | **UNDETERMINED — by design choice, not by missing evidence** | depends entirely on the SMEsPlus tenant-to-company mapping. `GB-01` |
| **Branch-scoped rate invisible to its own resolver** | **NO on this build** | forbidden at the model layer — §4 |

---

## 10. Statement of limitation

No live database was used. The uniqueness rule's behaviour over company-less rows remains
`INFERENCE`. The pre-v18 baseline is `NOT SEARCHED`. Client-side code was searched for the table name
and not read. These limitations are restated in `MCC_E00` §`MCC-E-012` and are **not** dissolved by
anything in this file.

---

## 11. CORRECTION NOTICE — applied to this file by the fixed-point passes, before the round closed

> **This is `GB-06`'s remedy being exercised. The correction lands in the file it contradicts, by id,
> and the original text above is left standing so the lineage is visible.**

| # | Claim in this file | Correction | Governing record |
|---|---|---|---|
| `C-1` | §9 "a demo-seeded or template-cloned database carries **162 company-less rows** … the highest-exposure case" | **WITHDRAWN AS TO "company-less".** The loader applies the model's default, so the 162 demo rows load as **root-company** rows. **The silent-2010-rate exposure STANDS on a corrected mechanism** — 157 rows dated `2010-01-01` owned by the installing root; any company inside that root's tree with no newer rate resolves at the 2010 rate, while a **second root company** in the same database resolves at **par**. Two wrong answers, neither announced | `MCC_E01` `MCCX-01` |
| `C-2` | §9 "Wrong opening / migration valuation — a demo-seeded database carries 162 company-less rows **before any user acts**" | **CORRECTED** as above. The row that matters is not the null company; it is the **date** | `MCC_E01` `MCCX-01` |
| `C-3` | §4.3 "no raw-SQL write to the rate table anywhere in the source root" | **STANDS, and is STRENGTHENED.** Independently reproduced by a fresh reviewer across **four** version trees with a second, line-wrap-tolerant method that re-tested every file containing the table name. Three candidates resolved as false positives | `MCC_E01` §3 |
| `C-4` | §6 "the composite defect as recorded is `NOT REPRODUCIBLE` on this build" | **STANDS**, and a fresh reviewer independently reached the same disposition by an independent route, adding that the site `FX-08` names carries a **different, verified defect**: the manual rate-update button is not gated by the root-company test that the framework already provides, so a branch user receives an untranslated hard failure. `FX-08`'s severity moves from *silent data defect* to *reachable hard failure with no UI gate* | `MCC_E01` §3 |
| `C-5` | §7 residual `MCC-C-R1` | **STANDS and is SHARPENED.** There is **no database-level constraint** behind the model constraint, and the constraint is create-time only. A fresh reviewer states it as: boundedness rests on one Python constraint with no stored invariant behind it | `MCC_E01` §3 |
| `C-6` | §10 limitation statement | **EXTENDED.** Test fixtures were excluded from every search in this round by instruction — and test fixtures are frequently the only place a branch-company or company-less rate row is constructed. The **reachability** evidence was therefore excluded by the search design itself | `MCC_E01` §3 |

### One consequence for the disposition, and it does not move

`FX-08` remains **`PARTIALLY VERIFIED`**: resolver half re-confirmed and extended, writer half
`CONTRADICTED`, composite `NOT REPRODUCIBLE`. **Two independent reviewers reached that disposition on
disjoint routes, and one of them issued a veto against any convergence claim resting on the
branch-rate constraint alone. This session accepts that veto and makes no such claim.**
