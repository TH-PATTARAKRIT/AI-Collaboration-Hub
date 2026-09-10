# VDR_PREP004_FINDING_RESOLUTION_REGISTER.md
# The five PREP-004 findings, resolved individually — not merely recorded

Session `[SMEPLUS-26-09-10-VDR-PREP-005]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 05.

§11 requires ten steps for each: population · source evidence · runtime evidence · configuration
dependency · optional-function dependency · security impact · accounting/inventory impact · challenge ·
SMEsPlus control implication · close or HOLD with an explicit evidence gap.

---

## `RF-A` — a capability switch turned OFF does not necessarily revoke the capability

| Step | Result |
|------|--------|
| **Population** | **48 of 49 gates.** The exception is one gate whose settings path clears user membership explicitly |
| **Source evidence** | the switch machinery adds and removes an *implication* on the holder group; it never touches a user's own group list. A corpus-wide sweep for group→user revocation, with its predicate validated against the corresponding grant form, found **exactly one** such site |
| **Runtime evidence** | **ESTABLISHED THIS ROUND.** The group-implication and user-membership tables were extracted from all three current-generation deployments and the mechanism is confirmed: gates are held by **direct membership that no holder group implies** — 8 such gates on the transacted deployment, 7 and 6 on the other two. The settings page, which reads only the holder group, would display those as OFF |
| **Configuration dependency** | the settings page reads the switch from the **holder group only**, so it displays OFF while the capability is live for directly-assigned users |
| **Optional-function dependency** | none — this is a capability-switch mechanism, not a module one |
| **Security impact** | **direct and severe.** A capability believed withdrawn is still exercisable by anyone who holds it directly |
| **Accounting / inventory impact** | depends on the gate; the multi-location and lot-tracking gates both govern stock behaviour |
| **Challenge** | independently derived by the source navigator; not yet challenged against runtime |
| **SMEsPlus control implication** | **every SMEsPlus capability switch must revoke what it grants, and its displayed state must be computed from actual holders — not from an implication.** A switch that cannot revoke is a one-way door |
| **Precision, because the population matters** | Most of the affected gates are **role groups** — manager roles — where direct assignment is intended and the "switch" framing does not apply. **The sharp cases are the capability gates**: on the transacted deployment, **multi-company (8 direct members) and multi-warehouse (1)** are held directly with no implication. For those two the displayed state is misleading, and multi-company is additionally machine-managed from a user's company list |
| **Status** | **CLOSED.** The mechanism is established from source and **confirmed at runtime on three deployments**, with the affected population separated into the role gates where it is expected and the capability gates where it is not |

> **A control had to be repaired before this could be believed.** The first runtime pass returned
> *"0 gates with direct members"* on all three deployments — a clean, plausible zero produced by a key
> extractor that never matched the real column names. **A positive control on the relation sizes was
> added before any conclusion was drawn**, and it failed the first instrument. The corrected pass reads
> 165, 144 and 718 membership rows respectively.

## `RF-B` — module deactivation destroys structures the module does not own

| Step | Result |
|------|--------|
| **Population** | **25 optional modules**, governing 606 population elements |
| **Source evidence** | the framework's uninstall path drops owned tables with cascade, drops module-added columns from **foreign** models with cascade, unlinks fields on surviving models whose target is removed, and **skips deletion guards** declared not to run at uninstall. Measured: **40 tables and 278 columns on models the modules do not own** |
| **Runtime evidence** | **NOT ESTABLISHED.** Whether any of this has fired on a real deployment needs module-state history plus a column-existence check |
| **Configuration dependency** | none — uninstall is not gated |
| **Optional-function dependency** | this *is* the optional-function mechanism |
| **Security impact** | one module's removal deletes a completion gate; three deletion guards are skipped |
| **Accounting / inventory impact** | **landed costs: the posted entries and the value rows survive; the documents, their lines and the adjustment lines are destroyed.** The books keep the adjustment and lose the reason |
| **Challenge** | independently derived; the framework mechanism was read at eleven separate call sites |
| **SMEsPlus control implication** | **a SMEsPlus capability must be a switch, not a module, unless its removal is genuinely meant to destroy data.** Not one of the 25 is safe to remove |
| **Status** | **HOLD — source-established, runtime-unverified** |

## `RF-C` — an interface gate may not be a security control

| Step | Result |
|------|--------|
| **Population** | **56 register elements**, and by extension the object at the centre of `CRITICAL-GAP-06` |
| **Source evidence** | every internal user is already a member by declaration; the framework discards the gate from the user's group set unless a debug flag is set, and rewrites it in views into a private display attribute. **The source's own comment says it should not be treated as a security group** |
| **Runtime evidence** | the gate is present on **all five deployments**, as are the elements it governs — consistent with a display flag rather than an access control |
| **Configuration dependency** | its ON state is a **per-session debug flag, not stored configuration** |
| **Optional-function dependency** | none |
| **Security impact** | **anything whose only protection is this gate is protected by nothing.** 56 elements |
| **Accounting / inventory impact** | includes maintenance routines that write outside the object layer |
| **Challenge** | the mechanism was read at four framework sites; the population count is reproduced from the register |
| **SMEsPlus control implication** | **SMEsPlus must not use a display gate as an access control, and must not carry a group that every user holds.** Any element needing protection needs a record rule or a field-level access control |
| **Status** | **CLOSED.** The mechanism is fully established from source and corroborated at runtime; nothing further is measurable, and the response is a design act |

## `RF-D` — the inventory value field is writable

| Step | Result |
|------|--------|
| **Population** | the per-movement value field on the movement object, and the **3,680 completed movements** carrying one on the transacted deployment |
| **Source evidence** | the field is declared by the valuation-accounting module |
| **Runtime evidence** | **read from the deployment's own field registry: stored, monetary, `readonly = false`.** The discriminating control: three sibling fields on the same object are `readonly = true`, so the flag distinguishes rather than defaulting |
| **Configuration dependency** | **CORRECTED.** The transacted deployment is **periodic on 44 of 44 companies** (`inventory_period = manual`). PREP-004 read a **company-dependent** category property that was set for company 1 only, on a 44-company deployment, and reported it as the deployment's configuration. The one genuinely perpetual current-generation deployment is a different one |
| **Optional-function dependency** | landed costs, an optional module, also writes value; removing it destroys the provenance and keeps the value |
| **Security impact** | writable by anything that can write the record; the on-hand valuation field is access-controlled to a manager role, but **the movement value field is not** |
| **Accounting impact** | **CORRECTED.** The per-movement link mechanism **is** located in source and is gated on a valuation account being set on the source or destination location — **0 of 525 locations carry one**, so the link is null *by construction of the configuration*. A **fourth route exists and was not examined**: a daily superuser job posting a valuation closing **at company level with no movement reference** |
| **Challenge** | the field attributes were read from the deployment's registry, not from source, and the control fired |
| **SMEsPlus control implication** | **inventory value must be immutable once written, and produced by a posting act rather than a field write.** If a value can be written directly, no downstream control can be trusted |
| **Status** | **CLOSED as a finding — the fact is established at runtime with a discriminating control.** The exposure it names is a design constraint, not an open research question |

## `RF-E` — FEFO silently degrades to FIFO after optional-module removal

| Step | Result |
|------|--------|
| **Population** | every location and product category configured for expiry-based removal |
| **Source evidence** | the expiry module contributes a single removal-strategy record. On uninstall the record is deleted; the strategy fields declare no delete behaviour, so the framework **sets them to null**, and the resolver falls through to first-in-first-out. **No error, no log** |
| **Runtime evidence** | **NOT ESTABLISHED** — needs a deployment that had the module and lost it |
| **Configuration dependency** | affects only locations and categories that were configured for expiry-based removal |
| **Optional-function dependency** | this *is* an optional-module removal effect |
| **Security impact** | none directly |
| **Inventory impact** | **the removal order changes permanently and the configuration cannot be recovered.** 15 columns of expiry history are destroyed, and expired stock **returns to available quantity** |
| **Challenge** | the researcher's own prediction was a hard error; **the tested result was a silent fallthrough, and the tested result was published** |
| **SMEsPlus control implication** | **a removal strategy must be a first-class value, not a record contributed by an optional module** — and any strategy that cannot be resolved must refuse, not fall back silently |
| **Status** | **HOLD — source-established, runtime-unverified.** The gap is named and bounded |

---

## Roll-up

| | |
|---|---|
| Findings resolved to CLOSED | **2** — `RF-C`, `RF-D` |
| Findings on HOLD with a named, bounded evidence gap | **3** — `RF-A`, `RF-B`, `RF-E` |
| Findings referred to the Boss as an open technical question | **0** |

**Every one of the three HOLDs has the same gap in the same shape: source semantics are established and
the runtime confirmation needs one further extraction.** For `RF-A` it is two tables; for `RF-B` a
module-state history; for `RF-E` a deployment that lost the module. **None is a question about what
should be done — each is a question about what to read next**, and all three are named precisely enough
to be executed without further analysis.
