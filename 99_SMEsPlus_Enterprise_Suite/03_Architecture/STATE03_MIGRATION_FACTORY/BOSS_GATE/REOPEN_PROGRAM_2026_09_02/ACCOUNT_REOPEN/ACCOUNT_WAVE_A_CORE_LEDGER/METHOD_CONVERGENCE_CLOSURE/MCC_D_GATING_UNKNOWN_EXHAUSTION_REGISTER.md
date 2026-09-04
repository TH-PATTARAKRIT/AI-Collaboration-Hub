# MCC_D — GATING UNKNOWN EXHAUSTION REGISTER

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Layer 1 clean-room
Governs `MC-06`. Layer 2 citations: `LAYER2_MCC_EVIDENCE/MCC_E00`, `MCC_E01`

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. The universe is re-enumerated first, and the parent's 59 does not survive as an enumeration

The round instruction says *"Do NOT assume the number is exactly 17. First re-enumerate."*

### 1.1 The parent's 59

| Class | Ids | Individually stated? |
|---|---|---|
| `GATING` | 17 | **17 — all** |
| `NON-GATING` | 16 | **0** — three grouped rows covering three id ranges |
| `ROUTED TO LATER WAVE` | 19 | **4** — the other 15 sit inside three ranges |
| `OUT OF SCOPE WITH EVIDENCE` | 2 | 2 |
| `UNCLASSIFIED` (orphan ids) | 5 | 5 |
| **Total** | **59** | **28 individually stated · 31 range-allocated** |

> ### `MCC-D-01` — the parent's 59 is a count of allocated id slots, not an enumeration. `VERIFIED FACT`.
>
> The arithmetic is exact. **The enumeration is not**: for 31 of the 59 ids no statement of the
> unknown exists — only a range and a shared one-line description. The parent round convicted its own
> parent of reporting `41` without enumerating it, and then reported `59` with 31 of it unenumerated.
> **The defect is one layer down, not gone.** `MC-06` cannot stand as `MET`.

### 1.2 The true id-level position, and why the two numbers were never going to reconcile

> ### `MCC-D-02` — `41` and `59` count two differently-keyed populations. `VERIFIED FACT`.
>
> Register `21` keys its unknowns `GAP-*` (14), `TX-*` (7), `CL-*` (5), `FE-02`, `TI-05`, `XM-01` —
> **28 rows, and its own count table totals 28. It reconciles exactly.**
> File `06` keys its unknowns `MCU-*` — a **new scheme, introduced at the convergence round, with no
> mapping to the old one in any file.**
> **No arithmetic can reconcile 41 to 59, because they are not two counts of one population.** That is
> the root cause of the non-reconciliation and neither round named it. Full treatment in `MCC_E`.

### 1.3 Re-enumerated universe used by this round

This round does **not** invent a third scheme. It works the `GATING` class, which is fully
id-enumerated in both directions and is the only class the Gate turns on.

| Class | Count | Basis |
|---|---|---|
| `GATING` | **17** — `MCU-01` … `MCU-17` | re-verified individually against their cited sources |
| `NON-GATING` | 16 | inherited; **`MCC-D-01` applies** — not re-enumerated by this round, class `C` |
| `ROUTED` | 19 | inherited; routing-abuse re-tested for the three items material to Wave A (§4) |
| `OUT OF SCOPE` | 2 | inherited; re-tested, both hold |
| `UNCLASSIFIED` | 5 | re-verified this session: register `21` holds 14 distinct `GAP-*` ids, files `01`–`26` cite 19; orphans are `GAP-A03`, `GAP-A04`, `GAP-C01`, `GAP-G01`, `GAP-H03` |
| **New this round** | **+3** — `MCU-18`, `MCU-19`, `MCU-19b` | §5 |

---

## 2. Closure records — the 17 `GATING` unknowns

Format per the round instruction. `Gate Impact` states what changes if the item stands.

---

### `MCU-01` — Are the control-suppression flags externally reachable?

| Field | Content |
|---|---|
| **Why gating** | Governs the severity of the entry-balance tolerance-zero boundary |
| **Search universe** | Named bypass tokens across the accounting addon; the calling surface of each |
| **Positive evidence** | The tokens exist and are read under elevated privilege at their consumption sites |
| **Negative evidence** | No web-controller or RPC-reachable entry point sets them **within the accounting addon** |
| **Remaining gap** | Reachability from a **client-supplied context** over RPC is not determinable from source alone; it needs an executed test |
| **Final disposition** | **`REMAINS GATING — HOLD`** |
| **Gate impact** | If externally reachable, `T0-01` moves from *defect* to *exploitable* |

---

### `MCU-02` · `MCU-03` — No accounting-event identity / no idempotency model

| Field | Content |
|---|---|
| **Why gating** | Ledger identity. Everything downstream — correction semantics, provenance, de-duplication — rests on it |
| **Search universe** | Whole accounting domain, all prior rounds, re-confirmed here |
| **Evidence** | Positively established: **no accounting-event object distinct from the journal entry exists** in the reference system |
| **Final disposition** | **`REMAINS GATING — HOLD`, and it is a BOSS DESIGN DECISION, not a research gap** |
| **Gate impact** | Cannot be closed by any amount of further research. It is `GB-01`-class |

---

### `MCU-04` — Report definitions carry no company dimension

| Field | Content |
|---|---|
| **Why gating** | Verified **adversely** by a final reviewer as a cross-tenant defect editable by any tenant's accounting manager, yet carried as a *medium open unknown* |
| **This round** | The **class is confirmed and widened**: `MCC-D-03` finds a second, independent instance of caller-supplied company scope with no defence in depth — a client-callable currency-conversion endpoint that takes a company id from the caller, browses it without an access check, and returns **par** rather than an error when the record rule denies the rows |
| **Final disposition** | **`REMAINS GATING — HOLD`** |
| **Gate impact** | `T0-04` tenant isolation. It is a **class**, not an instance, and the class now has two members |

---

### `MCU-05` — The lost tolerance-zero candidate (= `T0-07`)

| Field | Content |
|---|---|
| **This round** | **CHARACTERISED.** `MCC_C` §8: the raw-SQL rate reads number **8** across three addons; record-rule bypass is total on all of them; the fallbacks are **par in four places and an undated historical rate in one**; and the two halves of the system disagree about the company-less row |
| **Final disposition** | **`CLOSED — VERIFIED` as an unknown. The underlying boundary `T0-07` REMAINS UNRESOLVED** |
| **Gate impact** | The unknown is answered; the tolerance-zero boundary it names is not |

---

### `MCU-06` — Rate precedence: null vs own-company rows, never executed

| Field | Content |
|---|---|
| **Why gating** | Load-bearing for the severity of the null-company crossing; labelled `INFERENCE` on both sides by every prior round |
| **Search universe** | The resolver's order specification, and the ORM core routine that renders an order specification into SQL |
| **Positive evidence** | The resolver orders by the company column **first**, then by date descending, limit 1. The ORM's order-rendering routine emits the **raw column** for an `<m2o>.id` order term with **no direction and no null-ordering clause**, so the database's defaults apply: ascending, nulls last |
| **Conclusion** | **A company-scoped row sorts BEFORE a company-less row. The company-less row is reached only when the resolving company's root has NO row at or before the date.** |
| **Final disposition** | **`CLOSED — VERIFIED`** · `VERIFIED FACT` (source) + `INFERENCE` (the database's null-ordering default, not executed) |
| **Gate impact** | **REDUCES the severity of `SB-05`.** Own-company precedence is a real mitigation and no round had established it. It does **not** close `SB-05`: the crossing is unmitigated for exactly the case that matters most — a company with no rates of its own |

---

### `MCU-07` — Does shipped or localization data contain null-company rate rows?

| Field | Content |
|---|---|
| **Why gating** | Decides whether the crossing is reachable **out of the box** |
| **Search universe** | Every rate record in `.xml`/`.csv` across **both** module trees (1,752 directories), with each file's manifest placement resolved to `data` (always loaded) or `demo` |
| **Evidence** | **`data`: ZERO rate rows anywhere in either tree.** **`demo`: 162 rows in the framework's demo file, every one of them company-less**, plus 3 rows in two localisation demo files, all three company-scoped. **157 of the 162 are dated `2010-01-01`** |
| **Final disposition** | **`CLOSED — VERIFIED`** · class `A — verified absence of `data` rows within the declared pattern and path set` |
| **Gate impact** | **MATERIAL, and it cuts both ways.** A production database seeded **without** demo data ships **no** company-less rate rows — the crossing is **not** reachable out of the box. A database seeded **with** demo data ships **162** of them, before any user acts |

> ### `MCC-D-04` — the composition of `MCU-06` and `MCU-07` is a verified defect that no round has named.
>
> `MCU-06` establishes that a company-less row is used only when the company's root has no rate of its
> own. `MCU-07` establishes that a demo-seeded database contains one company-less row per currency,
> dated 2010. **A newly-onboarded company that has not yet loaded its own rates therefore values every
> foreign-currency posting at a 2010 rate — silently, with no warning, and the entry balances.**
> This is **not** the par fallback the programme has been tracking. Par is at least visible to an
> attentive reader. A real-looking sixteen-year-old rate is not.
>
> **It is squarely a Wave A opening-balance and onboarding defect**, and it closes `MCU-14` — a
> balanced-but-wrong taxonomy class that had **zero instances and had never been searched**.

---

### `MCU-08` — Is the approval-engine module in the SMEsPlus reference baseline?

| Field | Content |
|---|---|
| **Search universe** | Module presence in the primary tree; **and, new this round, the archive tree** |
| **Remaining gap** | Which modules SMEsPlus will actually install is a **Boss/architecture decision not yet made**; it is not discoverable from a source tree |
| **Final disposition** | **`CLOSED — RESCOPED NON-GATING`**, routed to the SMEsPlus module-baseline decision |
| **Gate impact** | None on Wave A research. The approval-bypass finding's **scope** depends on it; its **existence** does not |

---

### `MCU-09` — Is a null-company tax-repartition row reachable?

| Field | Content |
|---|---|
| **Why gating** | Would carry a tax split **and an account** across companies |
| **Search universe** | The repartition model's company field, the tax model's company field, and the record rule over the repartition model |
| **Positive evidence** | The repartition model's record rule **does** carry an explicit `company_id = False` disjunct — identical in shape to the rate table's |
| **Negative evidence, and it is decisive** | The repartition line's company field is **not independently settable**: it is a stored mirror of the owning tax's company. **The tax model's company field is `required`**, which is enforced by the ORM *and* by a database not-null column |
| **Conclusion** | **A null-company tax cannot exist; therefore a null-company repartition line cannot exist.** The record rule's null disjunct is **unreachable code** for this model |
| **Final disposition** | **`CLOSED — VERIFIED SAFE`** · class `A` within the declared scope. **Residual:** a stored mirror can only diverge from its source by a raw-SQL write, and no such write exists in either tree |
| **Gate impact** | **Removes a suspected second instance of the null-company class.** The class has one member — the rate table — not two |

---

### `MCU-10` — Lock-exception creation path: a lock-control object with no record rule

| Field | Content |
|---|---|
| **Why gating** | Control over the control. It is the object that relaxes the period lock |
| **Search universe** | The lock-exception model in full; its access rows; every `ir.rule` in the accounting addon and in the framework; its create, revoke and re-create paths; and its consumption path on the company model |
| **Positive evidence** | Its company field is declared `required` **and** `readonly` with a default of the acting company — which reads as a control |
| **Negative evidence** | **There is no `ir.rule` on the model at any layer.** The access rows give an ordinary accounting-manager role **read and create, with no write and no unlink** |
| **Contradiction — and this is the finding** | Three facts compose into a defect none of them shows alone: (1) `readonly` is a **client-side** attribute; the model's own create routine **explicitly honours a caller-supplied company** in the creation values, falling back to the acting company only when none is supplied; (2) the revoke action authorises on **group membership alone — it never checks the company** — and then performs its write under **elevated privilege**, precisely to work around the missing write right; (3) the consumption path filters exceptions by company and admits an exception with **no user** as applying to **everyone** |
| **Runtime consequence** | An accounting manager in **any** company can create a lock exception naming **any other** company, for **every** user, with **no expiry** — and can revoke **any** company's exceptions. The period control of a company the actor cannot otherwise see is reachable both ways |
| **Final disposition** | **`CLOSED — VERIFIED DEFECT`. The unknown is answered; a new verified defect replaces it** |
| **Gate impact** | **TOLERANCE-ZERO.** It attaches to `T0-03` (rewrite of a posted fact — the lock is what prevents it) and `T0-04` (tenant isolation). Registered as **`T0-08`** — see `MCC_G` |

---

### `MCU-11` — Report company scope is a caller-supplied parameter with no defence in depth

| Field | Content |
|---|---|
| **This round** | **CONFIRMED and widened.** A second instance found: a client-callable conversion endpoint takes a company id from the caller, browses it **without an access check**, and — when the record rule denies the underlying rows — returns **par** instead of an error. A wrong number, not a refusal |
| **Final disposition** | **`REMAINS GATING — HOLD`**, merged with `MCU-04` as one class with two verified members |
| **Gate impact** | `T0-04`. The package's own readiness criterion 3 (defence in depth) is not met on either instance |

---

### `MCU-12` — 58.1% of the package has never had the negative-claim control applied

| Field | Content |
|---|---|
| **This round** | Addressed in `MCC_F`, over the **corrected** file manifest rather than a hand-written list |
| **Final disposition** | See `MCC_F` §6 |
| **Gate impact** | `MC-05` |

---

### `MCU-13` — `FX-08` requires targeted re-verification

| Field | Content |
|---|---|
| **This round** | **EXECUTED IN FULL.** `MCC_C` |
| **Final disposition** | **`CLOSED — VERIFIED`.** `FX-08` → **`PARTIALLY VERIFIED`**: resolver half re-confirmed **and extended**; writer half **`CONTRADICTED`** at three independent layers; the composite defect as recorded is **`NOT REPRODUCIBLE`** on this build. One residual, `MCC-C-R1`, class `D` |
| **Gate impact** | **One of the four blockers reported "closed with evidence" was closed on a mechanism that does not exist.** `GB-03`'s branch axis closes; its null axis does not |

---

### `MCU-14` — Wrong opening provenance: taxonomy class with zero instances, never searched

| Field | Content |
|---|---|
| **This round** | **SEARCHED, and it is no longer empty.** `MCC-D-04`: a demo-seeded or template-cloned database carries 162 company-less rate rows dated 2010, which value every foreign-currency opening entry of any company that has not loaded its own rates |
| **Final disposition** | **`CLOSED — VERIFIED DEFECT`.** Registered as balanced-but-wrong case `BW-30` |
| **Gate impact** | Removes an empty taxonomy class — one of the two the parent round flagged as suspicious *because* they were empty |

---

### `MCU-15` — Wrong reversal lineage: taxonomy class with zero instances, never searched

| Field | Content |
|---|---|
| **Search universe** | The reversal wizard and the reversal linkage fields on the entry model |
| **Status** | **NOT SEARCHED to a conclusion by this round.** The round instruction confines scope to the `GB-03`/`FX-08`/`MCU-13` chain and to gating unknowns reachable from it; this one is reachable only by opening the reversal surface, which would broaden the round |
| **Final disposition** | **`REMAINS GATING — HOLD`** · class `C — NOT YET SEARCHED`, boundary declared |
| **Gate impact** | An empty taxonomy class that has never been searched cannot be reported as an absence. **`MCU-14`'s outcome is the reason this matters**: the other empty class turned out to contain a verified defect on first search |

---

### `MCU-16` — The exposure surface is 192 sites, of which 9 are assessed (= `GB-04`)

| Field | Content |
|---|---|
| **This round** | The **denominator itself is now known to be understated.** `MCC-B-01`: every population count in the programme was bounded to the primary module tree and excluded a **second module tree of 961 directories** in the same source root. Bounded counts do not become wrong, but their **scope statements were** |
| **Final disposition** | **`REMAINS GATING — HOLD`.** Exposure is bounded but not traversed; and the bound must be restated over the corrected path set |
| **Gate impact** | `GB-04` exposure. Mechanical, schedulable, not research |

---

### `MCU-17` — No correction-propagation channel exists

| Field | Content |
|---|---|
| **This round** | **The channel is defined and exercised for the first time.** `MCC_K` §3 specifies the rule; this round applies it to itself — every correction it makes to a parent claim is recorded **against the claim's id**, in this package, with the governing order stated once in `MCC_A` §4. Eleven corrections are so recorded |
| **What is NOT done** | The **standing backlog** is not cleared: 7 contradicted affirmative claims still stand live in the canonical registers in their original wording, 5 orphan unknown ids still have no row, and 2 balanced-but-wrong cases are still unregistered. This round does not edit parent artefacts (`DR-NC-06`) |
| **Final disposition** | **`REMAINS GATING — HOLD`** — the channel now exists in specification and in demonstration; the backlog it must carry is uncleared |
| **Gate impact** | `GB-06`. Cost to clear: editorial, low, no new research |

---

## 3. Result

| Disposition | Count | Ids |
|---|---|---|
| **`CLOSED — VERIFIED`** | **5** | `MCU-05`, `MCU-06`, `MCU-07`, `MCU-13`, `MCU-14` |
| **`CLOSED — VERIFIED SAFE`** | **1** | `MCU-09` |
| **`CLOSED — VERIFIED DEFECT`** (unknown answered, defect opened) | **1** | `MCU-10` |
| **`CLOSED — RESCOPED NON-GATING`** | **1** | `MCU-08` |
| **`REMAINS GATING — HOLD`** | **9** | `MCU-01`, `MCU-02`, `MCU-03`, `MCU-04`+`MCU-11`, `MCU-12`, `MCU-15`, `MCU-16`, `MCU-17` |
| **`ROUTED — LATER WAVE`** | **0** | **No Wave A blocker was routed to clear the Gate** |

> **8 of 17 gating unknowns closed — the first non-zero closure count in the programme.
> 9 remain. The Gate stays on `HOLD` by the standard's own rule, without qualification.**

Of the 9 remaining: **3 are Boss design decisions** (`MCU-02`, `MCU-03`, and the tenant half of
`MCU-04`/`MCU-11`) which no research closes; **3 are mechanical and cheap** (`MCU-12`, `MCU-16`,
`MCU-17`); **2 need an executed test against a running system** (`MCU-01`, and the runtime half of
`MCU-06`); **1 needs a bounded further search** (`MCU-15`).

---

## 4. Routing-abuse re-test

Required, because routing a blocker to a later Wave to clear a Gate is forbidden.

| Item | Routed to | Re-test | Result |
|---|---|---|---|
| `MCU-04` | was Wave G | Does it determine ledger identity, measurement, period control or integrity? | **YES — integrity.** Correctly recovered to `GATING` by the parent round; **stays** |
| `MCU-08` | rescoped by this round | Same test | **NO.** It determines the *scope* of a finding, not a ledger property. Rescoping is legitimate and is recorded with its reason |
| `MCU-40`…`MCU-58` | Waves B–H | Same test, applied to the three that touch measurement | **NO** for all three. Routing stands |
| **`MCU-15`** | **not routed** | Same test | **YES — integrity.** It is **retained in Wave A** despite being unsearched. Routing it would be exactly the abuse the rule forbids |

**No Wave A blocker is routed to a later Wave by this round.**

---

## 5. New unknowns opened by this round

Opening unknowns during an exhaustion round is expected; concealing them is the failure.

| id | Unknown | Class | Why |
|---|---|---|---|
| **`MCU-18`** | Whether the **archive module tree** in the source root is on the deployment's module path | **`GATING`** | It is referenced by no code or config; the module path is a runtime configuration value. If it is on the path, **961** further module directories — **450 of them duplicate copies of primary-tree modules** — become installable, and duplicate module names on one path is a known failure mode. **Every whole-tree negative claim in the programme is scoped to the primary tree only** |
| **`MCU-19`** | Whether any migrated or restored SMEsPlus database contains a rate row whose company has a parent | **`GATING`** | `MCC-C-R1`. Python constraints are not re-run at upgrade, and the maintenance path writes such a row's rate **without** re-validating its company. One `SELECT` answers it |
| **`MCU-19b`** | Whether the pre-v18 reference baseline carried the branch-rate constraint | **`NON-GATING`** | No v16 or v14 framework core exists in the searched roots — **only project custom addons**. Class `C — NOT SEARCHED`, and it must never be reported as "the constraint has always existed" |

**Re-enumerated gating total: 9 carried + 2 new gating = `11 GATING` unknowns stand.**

---

## 6. Has the gating set reached a fixed point?

**No, and it is reported as no.** The set moved 17 → 11 by closing 8 and opening 2. The two new ones
were found by extending a **path set**, not by looking harder — which is the same discovery mechanism
that produced `GB-07`, one round earlier, in the same shape.

> **The honest statement is that the gating set converges only when the path set stops moving, and
> this round moved it. `MCC_H` tests whether it has now stopped.**

---

## 7. CORRECTION NOTICE — applied before the round closed

> **`GB-06`'s remedy, exercised.** Governing record: `LAYER2_MCC_EVIDENCE/MCC_E01`.

### 7.1 Closures corrected

| id | This file's disposition | Correction |
|---|---|---|
| `MCU-07` | `CLOSED — VERIFIED`, with "162 **null-company** rows shipped in demo" | **The CLOSURE STANDS; its content is CORRECTED.** No rate row is shipped in `data` in **any** of four version trees — independently reproduced. The demo rows are **root-company**, not company-less: the loader applies the model default. **Null-company rows are not SHIPPED; they are USER-CREATABLE** — the field is not required, the constraint passes an empty company, the record rule admits it by explicit disjunct, and it is editable in the shipped views. Disposition unchanged: **`CLOSED — VERIFIED`** |
| `MCU-14` | `CLOSED — VERIFIED DEFECT`, `BW-30` | **STANDS ON A CORRECTED MECHANISM.** The defect is the **date**, not the company: 157 demo rows dated `2010-01-01` owned by the installing root. A company inside that root's tree with no newer rate values every foreign-currency opening at the 2010 rate; a **second root company** in the same database gets **par**. The class is no longer empty either way |
| `MCU-06` | `CLOSED — VERIFIED` | **INDEPENDENTLY CONFIRMED** by a fresh reviewer on the same reasoning chain and the same ORM-core citation, reached without sight of this file |
| `MCU-13` | `CLOSED — VERIFIED` | **INDEPENDENTLY CONFIRMED** by two fresh reviewers on disjoint routes, with an accepted **partial veto**: no convergence claim may rest on the branch-rate constraint alone. This session makes none |
| `MCU-09` | `CLOSED — VERIFIED SAFE` | **UNCHALLENGED.** One reviewer explicitly records it as not searched by them, so it rests on this round's evidence alone — stated so the confidence is visible |
| `MCU-10` | `CLOSED — VERIFIED DEFECT` (`T0-08` proposed) | **CONFIRMED as a defect; the `T0-08` LABEL IS REASSIGNED.** A fresh reviewer independently proposed `T0-08` for a different and stronger boundary — **entry identity** (§7.3). The lock-exception defect is re-registered as **`T0-10`** |

### 7.2 Reclassifications accepted from the adversarial pass

Each was re-verified at source by this session before acceptance.

| id | Was | Now | Evidence |
|---|---|---|---|
| `MCU-33` … `MCU-35` (concurrency / idempotency / completeness) | `NON-GATING` — *"require executed tests, outside a research round"* | **`GATING`** | The ground is false: the source **states** the behaviour statically. The sequence mixin's own documentation records that when the governing uniqueness condition is not met *"the lock won't be taken, and sequence numbers may not be unique when returned"*, and a missing uniqueness index degrades to a **logged warning**, not a refusal. Entry-number uniqueness determines **ledger identity**, and the evidence is a source read |
| `MCU-56` (bank-flow semantics) | `ROUTED — Wave H` | **SPLIT: mechanism `GATING` in Wave A; semantics routed** | The bank-statement path holds the **only production consumers** of the posted-move immutability suppression flag, writing to **posted** moves. That is a rewrite path on a posted fact — `T0-03` — and it is exactly `MCU-01`'s subject. The file is in **neither** the 18-file nor the corrected 26-file surface |
| `MCU-60`, `MCU-61` | `OUT OF SCOPE WITH EVIDENCE` | **`UNKNOWN`, class `B`** | Neither carries a search pattern or a path set in **any** file of the parent package. A not-found presented as a positive establishment. `MCU-60` was additionally load-bearing for declaring one population "unbounded by construction, not by omission" — which is circular |
| `MCU-16` | `GATING` unknown | **DOUBLE-COUNTED** — the identical fact is also blocker `GB-04`. The parent's total of 59 inherits the double count. Classification unchanged; the arithmetic is flagged |

### 7.3 New tolerance-zero boundaries, verified and accepted

| id | Boundary | Basis |
|---|---|---|
| **`T0-08`** | **Entry identity — one posted entry, one unambiguous immutable number, unique within the company and the period** | Six independent source mechanisms weaken it: the **declared** uniqueness constraint on the entry model has an **empty definition** and is a no-op; the real control is a raw-DDL partial index scoped by **journal, not company**, while journals are parent-inclusive; the lock protecting it is documented as conditional; a missing index degrades to a log line; the resequencing wizard **deliberately blanks the number to fall out of the partial index**, then rewrites; and the number/date alignment is disabled by a database-wide key with no company dimension. **Every one of these is balanced.** No existing boundary `T0-01`…`T0-07` can hold any of them |
| **`T0-09`** | **Declared-but-inert control — a control present to a reader and absent to the machine** | Two bounded instances: the **16** company-consistency guards declared on the company model, on the destination accounts of automatically generated ledger facts, where **automatic checking is never enabled and the check is never invoked**; and the empty uniqueness-constraint definition above |
| **`T0-10`** | Cross-company creation and revocation of the control that relaxes the period lock | `MCU-10`, this file §2 |

### 7.4 New gating unknowns from the fixed-point passes

| id | Unknown | Why gating |
|---|---|---|
| **`MCU-20`** | The v19 ORM **core** adds an eleventh read-side rate resolver in raw SQL, outside every record rule, converting at **today** rather than at the record's date, with a **fourth** fallback semantic (earliest *future* rate), reachable from **any grouped monetary aggregation in any list or pivot view**. Zero occurrences in either v18 core | **SMEsPlus targets the v19 line.** A v18 → v19 migration **widens** the rate-scoping universe. No Wave A conclusion about FX can carry into v19 without it |
| **`MCU-21`** | The company-consistency **enforcement** surface — **9 of 22** Wave A models enable automatic checking; **36 of 139** relational fields opt in; **16** declared guards on the company model are **inert** | It is the mechanism layer beneath `GB-01` and `GB-02`, and it is enumerated by no round |
| **`MCU-22`** | Cross-branch reconciliation, exchange-difference posting and the raw-SQL settlement write, admitted because the sole guard tests the **root** rather than the company | Tolerance-zero-severity, reachable by an ordinary accounting role in the normal branch configuration |

### 7.5 Restated result

| Disposition | Count |
|---|---|
| `CLOSED` this round (verified · safe · defect · rescoped) | **8** |
| `REMAINS GATING` from the inherited set | **9** |
| **Reclassified INTO gating** by the adversarial pass | **+4** (`MCU-33`, `MCU-34`, `MCU-35`, `MCU-56`-mechanism) |
| **Reverted to `UNKNOWN`** from out-of-scope | **+2** (`MCU-60`, `MCU-61`) |
| **New gating** from the fixed-point passes | **+3** (`MCU-20`, `MCU-21`, `MCU-22`) |
| **Standing gating total** | **18** |

> **The gating set did not converge. It went 17 → 11 by this round's own work, then 11 → 18 under two
> fresh passes. Eight real closures were more than offset by nine items that were always gating and
> were classified otherwise, or that nobody had looked at.**
>
> **This is reported as the round's result, not buried in it.** A closure count is meaningless while
> the classification of the remainder is still moving.

---

## 8. ADDENDUM — `MCU-15` closed after §7 was written

`MCU-15` (wrong reversal lineage — a taxonomy class with zero instances, never searched) was reported
in §2 as **`REMAINS GATING — HOLD`, class `C — NOT YET SEARCHED`**, on the ground that searching it
would broaden the round.

**`ER-CORE-4` — an empty cell means UNSEARCHED, never ABSENT — obliged the search, and the search was
one file and one wizard.** It was done.

| Field | Content |
|---|---|
| **Search universe** | All 11 occurrences of the reversal-lineage field and its inverse across the accounting addon, `.py` + `.xml`, tests and translations excluded; plus the reversal wizard and the entry model's reversal region, read in full |
| **Positive evidence** | The lineage field exists, carries the company-consistency flag, and the entry model **does** enable automatic checking — so the *company* dimension of the link is guarded |
| **Negative evidence** | **No constraint of any kind on the link.** Not unique, so one entry may carry N reversals. `readonly` is client-side and the addon writes the field server-side. No delete behaviour declared, so the lineage is severable. Auto-reconciliation with the original happens **only** in the cancel case; otherwise the pointer is the sole carrier of the correction relationship |
| **Contradiction** | None. No prior round made any claim about this class |
| **Final disposition** | **`CLOSED — VERIFIED DEFECT`.** Registered as `BW-35` |
| **Gate impact** | The **last** empty taxonomy class is no longer empty. **Both** classes that stood at zero produced a verified defect on first search — `ER-CORE-4` now has a 2-of-2 record |

### Restated result

| Disposition | Count |
|---|---|
| `CLOSED` this round | **9** (was 8; `MCU-15` added) |
| `REMAINS GATING` from the inherited set | **8** (was 9) |
| Reclassified into gating by the adversarial pass | +4 |
| Reverted to `UNKNOWN` from out-of-scope | +2 |
| New gating from the fixed-point passes | +3 |
| **Standing gating total** | **17** |

> **The gating set went 17 → 11 → 18 → 17. It is oscillating, not converging.** Nine real closures
> against nine items that were always gating and were classified otherwise, or that nobody had looked
> at. **The number returning to its starting value is a coincidence and is reported as one** — the
> membership is almost entirely different.
