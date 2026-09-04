# [SMEPLUS-26-09-04-INV-MT-INVARIANT-SET-001]
# 04 — Context Ownership And Visibility Matrix

Control Level: `/L9999.9999`
Status: `MATRIX COMPLETE FOR ALL 17 MANDATED CONTEXT SUBJECTS — DESIGN / SPECIFICATION ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. What This Matrix Answers

For every subject named in the authorization: **which axis of `CTX` owns it, where its context comes from, who may see it, and what may cross.**

Column meanings:

- **Anchor** — the single authoritative ancestor from which `company` derives (`MTI-05`). `—` means the subject *is* an axis rather than being anchored to one.
- **T / C / W / L** — whether `tenant`, `company`, `warehouse`, `location` are present on the subject. `Y` mandatory · `S` situational (present by the object's nature) · `N` not applicable.
- **May cross company?** — whether any legitimate cross-company path exists, and under what.
- **Status** — carried from `03`.

Reading rule: `S` never means optional. It means the axis applies to some instances of the object and not others, determined by the object's nature and not by configuration. Where the axis applies, it is mandatory.

---

## 2. The Context Axes Themselves

| # | Subject | Anchor | T | C | W | L | Visibility Rule | Invariants | Status |
|---:|---|---|:-:|:-:|:-:|:-:|---|---|---|
| 1 | **Tenant** | — | Y | N | N | N | The outermost boundary. Nothing crosses it — no record, computation, event, job, report, export, grant or handoff | `MTI-01`, `MTI-02`, `MTI-25`, `MTI-47`, `MTI-49` | `SPECIFIED` |
| 2 | **Company** | tenant | Y | Y | N | N | Closed within a tenant. Crossing occurs only through the `MTI-22` register | `MTI-01`, `MTI-03`, `MTI-22`, `MTI-48` | `SPECIFIED` |
| 3 | **Warehouse** (`CN-02`) | company | Y | Y | Y | N | Visible within its company. Company immutable after first completed movement. **Never equated with a Thai tax branch** | `MTI-07`, `MTI-06`, `MTI-40` | `SPECIFIED` — `TH-HOLD-06` held |
| 4 | **Location / storage place** (`CN-03`) | **warehouse** | Y | Y | Y | Y | Visible within its company. Parent must resolve to the same company. Kind is versioned and financially load-bearing | `MTI-08`, `MTI-04`, `MTI-36`, `MTI-40` | `SPECIFIED` — shape of `R4-F-09`, finding not closed |

### 2.1 The location anchor is the finding, restated as a rule

The whole of `R4-F-09` reduces to one sentence: a location's company was an attribute that could be blank. Under `MTI-08` it is not an attribute at all — it is derived from the warehouse the location belongs to, stored, and continuously asserted. A location cannot exist without a warehouse, and a warehouse cannot exist without a company. The blank case ceases to be expressible.

**This is a design position. `R4-F-09` remains open** and requires implementation and independent verification to close.

---

## 3. Master Data And Traceable Identity

| # | Subject | Anchor | T | C | W | L | Visibility Rule | Invariants | Status |
|---:|---|---|:-:|:-:|:-:|:-:|---|---|---|
| 5 | **Product** (`CN-11`) | tenant (definition) / company (attachment) | Y | Y | N | N | Definitional identity readable tenant-wide; **transactable only in a company that has an explicit enablement**. Costing and valuation attachment is company-scoped | `MTI-11`, `MTI-21` | `SPECIFIED — CONDITIONAL (`MTI-D-01`)` |
| 6 | **Product variant** (`CN-12`) | its parent product | Y | Y | N | N | Follows the product. The attribute-value combination is part of the definitional identity and is therefore tenant-level; stock and value are company-level | `MTI-11` | `SPECIFIED — CONDITIONAL (`MTI-D-01`, `GAP-FS-03`)` |
| 7 | **Product category** (`CN-08`) | tenant (structure) / company (costing facet) | Y | S | N | N | Structure may be tenant-level; **the costing and valuation facet is company-scoped**, which the reference evidence confirms is the correct shape | `MTI-11` | `SPECIFIED — VALUE HELD` — the facet split is `GAP-FS-02`, precondition-blocked on `JT-01` (**NOT DECIDABLE**) |
| 8 | **Lot** (`CN-17`) and **Serial** (`CN-18`) | company + product | Y | Y | N | N | Identity is `(tenant, company, product, value)`. Company-less identity prohibited. Uniqueness per company. **The bare value is never the identity** in any display, export, scan result or handoff | `MTI-12`, `MTI-26`, `MTI-27` | `SPECIFIED` — shape of `R4-F-06`, finding not closed |
| 9 | **Package / handling unit** (`CN-19`) | company | Y | Y | S | S | Visible within its company. **May never contain goods resolving to more than one company.** Content snapshots carry the `CTX` in force at snapshot time | `MTI-13` | `SPECIFIED` — migration disposition `GAP-FS-05` open |

### 3.1 Legitimate cross-company value collision, illegitimate cross-company disclosure

Two companies in one tenant buying from the same supplier will receive the same batch code. That is normal trade, and prohibiting it would be a design error. The matrix therefore permits the **value** to repeat across companies and prohibits two things instead:

- the identity ever being the bare value (`MTI-12`);
- any surface disclosing, by uniqueness feedback or otherwise, that the value is in use elsewhere (`MTI-27`).

This replaces the reactive cross-company duplicate check that `R4-F-06` describes. A reactive check treats the collision as an error to be found afterwards; the matrix treats it as a legitimate state that must simply never be confusable.

---

## 4. Operational Structure

| # | Subject | Anchor | T | C | W | L | Visibility Rule | Invariants | Status |
|---:|---|---|:-:|:-:|:-:|:-:|---|---|---|
| 10 | **Operation type** (`CN-04`) | warehouse | Y | Y | Y | N | Visible within its company. Numbering per `(company, operation type)`, continuous, never reused across contexts. Default source and destination locations must resolve to the same company | `MTI-09`, `MTI-08` | `SPECIFIED` — numbering convention `TH-HOLD-09` held |
| 11 | **Route** (`CN-05`) | company | Y | Y | S | N | Visible within its company. Versioned; a generated operation resolves to the version in force at generation | `MTI-10`, `MTI-36` | `SPECIFIED` |
| 12 | **Rule** (`CN-05`) | its route | Y | Y | S | S | **A rule may not belong to a company other than its route's** — adopted from the reference behaviour as a positive transfer. Source and destination locations must resolve to the route's company | `MTI-10` | `SPECIFIED` |
| 13 | **Reordering rule** (`CN-20`) | company + location | Y | Y | S | Y | May propose supply only within its own `CTX`. Cross-company proposal is prohibited outright | `MTI-14`, `MTI-32` | `SPECIFIED` — **does not resolve** the within-company nested overlap at `R4-F-11` |
| 14 | **Put-away rule** (`CN-*` via `INV-F-32`) | company + location | Y | Y | Y | Y | Suggested and overridden destinations must resolve to the same company as the source. An override is an evented act | `MTI-08`, `MTI-33`, `MTI-38` | `SPECIFIED` |
| 15 | **Storage category** (`INV-F-31`) | company | Y | Y | S | S | Constrains what may be stored where, within one company | `MTI-04` | `SPECIFIED` — Thai regulated-storage mapping unevidenced, routed |
| 16 | **Barcode nomenclature** (`CN-16`) | tenant | Y | S | N | N | A nomenclature may be tenant-level; **resolution of a scanned value is always performed within the caller's `CTX`** and never resolves an identity outside it | `MTI-26`, `MTI-27` | `SPECIFIED` — real Thai formats unevidenced, `R4-Q-03` |
| 17 | **Unit group and unit** (`CN-14`) | tenant | Y | N | N | N | Tenant-level definitional data. Conversion factors are versioned; a factor change never alters historical quantity in any company | `MTI-36`, `IV-11` | `SPECIFIED` — rounding direction is an Inventory decision, `R4-F-13` |

### 4.1 Tenant-level definitional data is a shared surface, and shared surfaces must be proven too

Entries 5, 7, 16 and 17 place definitional data at tenant level. That is a deliberate position, and it creates a shared surface within a tenant that `MTI-02` protects across tenants but that nothing protects *within* a tenant — because within a tenant, sharing is the point.

The safeguard is the split itself: **definitional data carries no quantity, no value, no policy attachment and no transactional history.** The moment any of those attach, the anchor moves to `company` (entries 5, 7, 8). A change to tenant-level definitional data is still an evented, approved act under `MTI-40`, and is still non-retroactive under `MTI-36`.

This split is the substance of `MTI-D-01`. If Boss rules for a company-owned master instead, entries 5, 6 and 7 move wholly to `company` and this section is superseded.

---

## 5. Movement, Transfer And The Acts That Change Stock

| # | Subject | Anchor | T | C | W | L | Visibility Rule | Invariants | Status |
|---:|---|---|:-:|:-:|:-:|:-:|---|---|---|
| 18 | **Movement document** (`CN-24`) | operation type | Y | Y | Y | S | One company. Numbering per `(company, operation type)` | `MTI-15`, `MTI-09` | `SPECIFIED` |
| 19 | **Movement fact** (`CN-25`) | its document | Y | Y | Y | Y | **Exactly one company. Source and destination locations must resolve to the same company.** A movement between companies is not one fact | `MTI-15`, `MTI-44` | `SPECIFIED — RANK 2 DEPENDENT` — attempt identity is `RISK-C02` |
| 20 | **Internal transfer** (`HO-21`) | its document | Y | Y | Y | Y | Both endpoints internal and in the same company. Financial neutrality is asserted by an independent zero-value check, not assumed from configuration | `MTI-15`, `MTI-46`, `R4-F-18` | `SPECIFIED — VALUE HELD` |
| 21 | **Inter-company transfer** (`HO-22`) | — | Y | Y | Y | Y | **Two single-context facts** linked by a Cross-Context Relationship identity. Never one fact spanning two companies | `MTI-44`, `MTI-22` | `SPECIFIED — CONDITIONAL (`JT-10`)` — path **never traced end to end** (`GAP-FS-07`) |
| 22 | **Inventory adjustment** (`CN-28`) and **count session** (`CN-27`) | company + location | Y | Y | Y | Y | One company. Reason classification defined tenant-wide so it means the same in every company; the act is single-context | `MTI-33`, `MTI-38` | `SPECIFIED — VALUE HELD` — taxonomy `R4-Q-01` |
| 23 | **Scrap** (`CN-29`) | company + location | Y | Y | Y | Y | One company. Same reason-classification rule. Salvage has no object and must be originated | `MTI-33`, `MTI-38` | `SPECIFIED — VALUE HELD` — `R4-F-03` carried |
| 24 | **Return** (`INV-F-11`) | its original movement | Y | Y | Y | Y | Resolves to the **same company as the original movement** it reverses or relates to; a return may not change context | `MTI-39`, `MTI-15` | `SPECIFIED — VALUE HELD` — cost basis `JT-05` **NOT DECIDABLE** |
| 25 | **Landed cost allocation** (`CN-30`) | company | Y | Y | S | N | Allocates only across target lines resolving to the same company. Cross-company allocation is prohibited | `MTI-33`, `MTI-03` | `SPECIFIED — VALUE HELD` — `JT-08`, Audit VETO retained |

### 5.1 Entry 21 is the one door this matrix cannot finish

Inter-company transfer is the principal legitimate cross-company path and therefore the principal entry in the `MTI-22` register. Its **structure** is specifiable and is specified: two facts, one per company, correlated. Its **treatment** — what each side recognises, and at what basis — is `JT-10`, open, and its path is recorded as **never traced end to end** (`GAP-FS-07`).

This session specifies the structure and stops. It does not trace the path, and tracing it is not in this authorization.

---

## 6. Execution, Derivation And Reporting

| # | Subject | Anchor | T | C | W | L | Visibility Rule | Invariants | Status |
|---:|---|---|:-:|:-:|:-:|:-:|---|---|---|
| 26 | **Replenishment run** (`CN-35`, `INV-F-01`, `INV-F-15`) | company | Y | Y | S | S | **One `CTX` per run.** Reads only within it; the proposal carries the `CTX` and the input snapshot | `MTI-29`, `MTI-32` | `SPECIFIED` |
| 27 | **Scheduler / background execution** | company | Y | Y | S | S | One `CTX`. Carries the scheduling authority; a lapsed or revoked authority prevents execution and the non-execution is recorded | `MTI-29`, `MTI-30`, `MTI-31` | `SPECIFIED — RANK 2 DEPENDENT` |
| 28 | **Place balance** (`CN-26`) | its location | Y | Y | Y | Y | Derived from single-context facts. **The owner dimension is orthogonal to company and must never be conflated with it** | `MTI-16`, `MTI-23` | `SPECIFIED` — consignment policy `GAP-MD-09` open |
| 29 | **Reservation** (`CN-23`) | its balance | Y | Y | Y | Y | Follows the balance. Concurrency sufficiency is `C-04`, an unarbitrated conflict, not touched here | `MTI-16` | `SPECIFIED` — `C-04` carried |
| 30 | **Valuation fact** (`CN-31`) | its movement fact | Y | Y | S | S | Follows the movement. Cost layers and the retroactive compensation pass must respect the company boundary in every path | `MTI-16`, `MTI-23` | `SPECIFIED — VALUE HELD` — `L9-06`, `JT-01` **NOT DECIDABLE** |
| 31 | **Stock and location reporting** (`INV-M10`, `INV-M11`) | the query | Y | Y | S | S | Scoped before evaluation, not filtered after. No aggregation across companies except under a Cross-Context Report Grant | `MTI-21`, `MTI-24`, `MTI-28` | `SPECIFIED` |
| 32 | **Valuation reporting** (`INV-M14`) | the query | Y | Y | S | S | Same scoping. **A Cross-Context Report Grant may not carry valuation content while the COGS Gap stands** | `MTI-24`, `MTI-25` | `SPECIFIED — VALUE HELD` — see `12` `AAS-V-03` |
| 33 | **Movement history and stock card** (`INV-M12`, `INV-M13`) | the query | Y | Y | S | S | Same scoping. The report states its ordering rule and its `CTX` scope, both being part of its identity | `MTI-28` | `SPECIFIED` — ordering rule `R4-F-08` |
| 34 | **Warehouse analytics** (`INV-M15`) | the query | Y | Y | Y | S | Same scoping. Derived measures carry the `CTX` of their inputs | `MTI-23`, `MTI-24` | `SPECIFIED` — measure set evidence-thin, `GAP-FS-13` |
| 35 | **Event and audit trail** | the act | Y | Y | S | S | Every event carries the full `CTX`, actor, authority, both dates and evidence reference. Audit visibility is itself context-scoped | `MTI-38`, `MTI-39`, `MTI-50` | `SPECIFIED` |

### 6.1 The derived-surface rule is the part with no prior statement

Entries 28 and 30 through 34 exist because of `R4-F-22`. The point is easy to lose: **every stored record can carry a correct company and the module can still leak**, because design principle `P-03` makes the most-used numbers in the module derived. A sum, a forecast, a ranking or an alert is computed at query time, and the computation is where the boundary must also hold.

`MTI-24` therefore forbids cross-context aggregation as an invariant in its own right, rather than treating it as a consequence of record scoping. `MTI-23` requires the derived value to carry the context of its inputs so that the assertion is checkable rather than assumed.

---

## 7. Authorization Scope — Specified In Both Shapes, Because The Ruling Is Outstanding

`L9-03` cannot be proven because `RISK-U01` / `U-01` — whether user rights can be scoped to a warehouse or a storage place — is recorded in prior evidence as *"not merely undesigned — unevidenced either way"*. That is a Boss scope ruling and is not taken here.

The matrix therefore specifies the authorization context in a way that expresses **either** ruling without pre-empting it:

`AUTH = (tenant, company[, warehouse][, location][, operation class])`

| Ruling | Consequence For This Matrix |
|---|---|
| **Company-level only** | `AUTH = (tenant, company)`. Every row's visibility rule stands unchanged. `L9-03` becomes vacuous rather than unproven |
| **Warehouse-level** | `AUTH` gains `warehouse`. Rows 3, 4, 10, 18, 19, 20, 22, 23, 26, 34 acquire a second filter beneath company. No invariant changes; the scope set narrows |
| **Location- or operation-class-level** | `AUTH` gains further axes. Rows 4, 14, 19, 22, 23 acquire the finest filter. Segregation of duties (`L7-09`) becomes designable, which prior evidence records it currently is not |

**Two rules hold under every ruling**, and are stated as invariant consequences rather than as options:

1. `AUTH` is always a **subset** of a single `CTX`, never a superset and never a union across companies. Multi-company access is several `AUTH` entries, never one broadened entry.
2. A Thai tax branch is **not** a warehouse (`TH-HOLD-06`). If a branch dimension is introduced it is a separate dimension, and operational warehouse scoping must not be reused to carry it. Conflating them would make a statutory concept depend on an operational configuration.

Recorded as decision blocker `MTI-D-02`, carried from `U-01`. This session does not rule.

---

## 8. Coverage Result

| Measure | Result |
|---|---:|
| Context subjects mandated by the authorization | 17 |
| Subjects given a full ownership and visibility position | **35 rows covering all 17** |
| Subjects with a mandatory `company` axis | 31 of 35 — `Y`. Two are situational (`S`) and two are tenant-level by nature (`tenant` itself and unit groups) |
| Subjects `SPECIFIED` unconditionally | 22 |
| Subjects `SPECIFIED — VALUE HELD` | 8 |
| Subjects `SPECIFIED — CONDITIONAL` | 3 |
| Subjects `SPECIFIED — RANK 2 DEPENDENT` | 2 |
| Prior items closed by this matrix | **0** |

---

## 9. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
