# SA_CORR5_03 — `G3` AUDIT-SHAPE COMPLETENESS

## CP-SA-C5-30 — G3 AUDIT SHAPE SA-SPEC COMPLETE

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR5-ZERO-SME-CARRYFORWARD-001]`
Branch: `architecture/phase-sa-corr5-zero-sme-carryforward-closure-2026-09-09-001`
Workstream: **C** · Closes: **`G3`** — *"the corpus's audit shape carries 1 of `MTI-D-02`'s 4 axes, in
two independently authored schemas"* (`SA_CORR4_01` §4.1 class 10, `C4-01-F-09`).
Boss: **SOLE FINAL APPROVER**

---

## 1. The four-axis requirement, reconstructed from primary evidence

The requirement is **not** stated in the `MTI-D-02` ruling as an audit-trail sentence; CORR4 cited it
as *"`MTI-D-02` §4"*. Reconstructed exactly:

| Source | Verbatim | What it supplies |
|---|---|---|
| **Boss ruling `MTI-D-02`** (`BOSS_GATE/REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/26_BOSS_RULING_SMEPLUS-26-09-04-INV-MTI-D02-AUTHORIZATION-GRANULARITY-001.md`, branch `ruling/inventory-mti-d02-authorization-granularity-2026-09-04-001` @ `13b3e63f`, 2026-09-04) §2–§3 | *"Company + Warehouse + Operation-Type … Inventory permission and execution context must be controlled by all applicable dimensions: 1. Tenant / Company context 2. Warehouse context 3. Operation-Type context"* | the **axes**: tenant, company, warehouse, operation type |
| same, §4 rule 7 | *"…adjustments, transfers, scrap, landed cost flows, scheduler actions, and **stock movement history** must preserve the same authorization context"* | history must carry the axes |
| same, §4 rule 8 | *"Background jobs and system automation must carry explicit tenant/company/warehouse/operation-type context when executing inventory actions"* | non-interactive acts included |
| **`CD-26`** (R2 delta register) | *"`MTI-D-02` §4 and advice `27` §5 both require the audit trail to answer **who performed what action under which tenant, company, warehouse and operation type**. An authority reference identifies the grant; it does not by itself state the four axes the act was performed under"* | the **audit-trail** form of the requirement — a resolved tuple, not a reference |
| **`MTI-38` R2** (§12.11) | *"Every context-bearing act emits an immutable event carrying the full `CTX`, the full four-axis `AUTH` relied on as a resolved tuple, the actor, the authority relied on including any `MTI-18` grant, the physical event date and the entry date as two distinct values, and the evidence reference. **The audit trail must answer: who performed what action, in which tenant, in which company, in which warehouse, and under which operation type.**"* | the invariant text |
| `MTI-39`, `MTI-40`, `MTI-50` | event immutability; anchor-change auditability with before/after; control-run retention | lineage and retention |
| `09_DATA_IDENTITY…` §5 | *"The audit trail is itself context-scoped. An auditor working in one company does not see another's trail except under an `XCR-02` grant"*; two-date requirement restated | visibility scope; time semantics |

> **The requirement, in one line:** *every audit record answers who · what · on which object · in which
> tenant · in which company · in which warehouse · under which operation type · when (two dates) ·
> under which authority · with what before/after where the act changed a value · with an inspectable
> evidence reference — and is immutable, context-scoped and retained.*

### 1.1 The gap, re-measured (escape-tolerant pattern, `C4-I-05`)

| Schema | Fields | tenant | company | warehouse | operation type | actor | before/after | two dates | authority |
|---|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `FDS_AUDIT` §12 | 12 | ✔ | **✗** | **✗** | **✗** | `user_id` | ✔ | **one** (`created_at`) | **✗** |
| `FDS_SUBSCRIPTION_MODULE` §12 | 10 | ✔ | **✗** | **✗** | **✗** | `actor_id` | ✔ | one | **✗** |
| `FDS_TENANT` §10 event | 4 | (object) | ✗ | ✗ | ✗ | ✔ | old/new status | — | ✗ |

**1 of 4 axes** in both schemas reproduces. **Two further absences the CORR4 finding did not name:** no
**authority** field (the grant relied on — `MTI-38`'s *"authority relied on including any `MTI-18`
grant"*) and **one timestamp** where two are required (`MTI-38`, `INV-F-07`, handoff element 3).
`G3` is therefore **three** gaps in one shape: axes, authority, time.

---

## 2. Why the answer is a conceptual contract and not a field list

`FDS_AUDIT` §12 is a vendor-style column list; copying its shape into Phase SA would violate the
clean-room rule and would still be wrong. The SMEsPlus audit contract is stated below as **semantic
axes with producers and obligations**; representation (columns, types, partitioning, log technology) is
Functional Design and beyond. Each axis carries the ten attributes the master prompt names.

**Scope rule that governs the whole contract:** `SCOPE-AWARE EVERYWHERE`. A **`PLATFORM`**-scoped act
(class 1, 13 of `SA_CORR5_02`) has **no tenant of its own** — `BR-AUD-003` *"Audit belongs to Tenant"*
is true of tenant-context acts and **false as a universal**; the platform's audit stream is a
**platform-context stream with the target tenant as object**. This is the correction the two schemas
need most and CORR4 did not name: **they have no place for an act that is *about* a tenant but not
*in* one.**

---

## 3. The audit contract — `AUD-C`

### 3.1 The context axes (`AUD-C-A1`…`A5`)

**`AUD-C-A5` — Location (situational).** `CTX` is `(tenant, company, warehouse?, location?)` (R1 `03`
§2.1; R2 `04` §2), so *"the full `CTX`"* (`MTI-38`) includes the location where the object is
location-anchored (rows 4, 13, 14, 22, 23 of the context matrix). `A5` carries the location identity
or `N/A + reason`; producer `EP-R`; scope as company; immutable at the act. **Whether location is also
an *authorization* axis is `RC-D-01`, unruled (Boss)** — `A5` is a context axis only (`CHA-08`). The
first freeze omitted it.

| Attribute | **Tenant** `A1` | **Company** `A2` | **Warehouse** `A3` | **Operation type** `A4` |
|---|---|---|---|---|
| Semantic purpose | the security boundary the act was inside; for platform acts, the tenant **acted on** | the legal/accounting boundary; **required for every company-scoped object** | the physical scope the `AUTH` was evaluated at | the platform **operation class** (`CF-I-05`) and the tenant's operation-type identity the act ran under |
| Authoritative producer | `EP-R` resolution of the act's `CTX` (`MTI-19` attested) | same | same, where the object is warehouse-anchored | `EP-P` evaluation of the four-axis `AUTH` (`CF-I-03` attested) |
| Required identifiers | tenant identity; **scope class** (`PLATFORM`/`TENANT`/`COMPANY`) of the act | company identity or **`N/A` + reason** (never blank) | warehouse identity or `N/A` + reason | operation-type identity **and** its platform class (`HF-CTX-10`) or `N/A` + reason |
| Tenant/Company scope | the record lives in the tenant's audit stream **or**, for platform acts, in the platform stream with tenant as object | company-scoped records visible only inside the company (`MTI-21`) | as company | as company |
| Time semantics | resolved at the act; **immutable thereafter** (`MTI-39`) | same | same | same |
| Actor semantics | n/a (axis of the *act*, not the actor) — the actor's membership is **not** the source of this value | same | same | same |
| Before/after · lineage | where the act **changes an anchor**, before and after values (`MTI-40`) | same | same | class change is immutable after first use (`CF-I-05`) — an attempted change is itself an audited refusal |
| Retention | `MTI-50`; never edited, never deleted (`BR-AUD-001/002`) | same | same | same |
| Evidence use | `HF-CTX-01`, `-05`, `-06` | `HF-CTX-02` | `HF-CTX-03`/`-04` | `HF-CTX-10` |
| Runtime proof | `RT-AUD-01`: an act in a company-scoped object with any axis absent is **refused and the refusal audited** — never recorded with a blank | | | |

### 3.2 The act axes (`AUD-C-B1`…`B4`)

| Attribute | **Actor** `B1` | **Authority** `B2` | **Act and object** `B3` | **Time** `B4` |
|---|---|---|---|---|
| Semantic purpose | who performed it: human, service principal (**with version**), platform principal; *"the system" is not an asserter* | the grant relied on — **as a resolved four-axis tuple plus the grant identity**, including any `MTI-18` elevation | what was done, to which object (type + identity), and the **occurrence identity** where the act is a business fact (`E15-A1`) | when — **physical event date and entry date as two distinct values** |
| Producer | `EP-P` (the evaluated principal) | `EP-P` / `CF-I-03` run | the emitting module | the emitting module (physical) · the store (entry) |
| Identifiers | principal identity; principal class; version for non-human | grant identity; four axes; `CF-I-03` run reference (`HF-CTX-11`) | act class (the platform operation class where applicable); object type; object identity; attempt identity (`XMC-C-A14`) | two timestamps; the time basis (which date a control evaluated — `09` §5) |
| Scope | as the act | as the act | as the act | as the act |
| Time semantics | at the act | **the grant in force at the act's timestamp** (`CF-I-03` §3.4) — later revocation adds a `SUSPECT` layer, never edits | at the act | entry date is the store's clock; physical date is asserted by the actor and **never later than entry** except for evidenced backdating, which is itself audited |
| Actor semantics | never inferred from session where the act carries its own | n/a | — | — |
| Before/after · lineage | — | grant supersession chain (`CF-I-03R` §3.2) | before/after values where a value changed; reversal ↔ original linkage (`XMC-C-A8`); anchor-path (`HF-CTX-05`) | — |
| Retention | `MTI-50` | `MTI-50` + the historised grant store (`I2`) | `MTI-50` | `MTI-50` |
| Evidence use | `HF-CTX-08` | `HF-CTX-08`, `-11` | `HF-CTX-05`, element 12/13, element 16 | element 3, `MTI-38` |
| Runtime proof | `RT-AUD-02`: a non-human actor without version → refused | `RT-AUD-03`: an event whose authority is a bare reference with no resolved tuple → fails the `CF-I-03` `D5` sweep | `RT-AUD-04`: an event with no object identity → refused | `RT-AUD-05`: an event with one date → refused |

### 3.3 The record axes (`AUD-C-C1`…`C3`)

| Attribute | **Evidence reference** `C1` | **Immutability** `C2` | **Visibility** `C3` |
|---|---|---|---|
| Semantic purpose | the inspectable thing that proves the act — the control run, the document, the count sheet; **never a boolean** | the record is append-only; correction is a new linked record | who may read the record |
| Producer | the emitting module; the control (`MTI-19`, `CF-I-03`) | the store | `EP-Q` (reads scoped by `AUTH`, `MTI-21`) |
| Identifiers | evidence identity + type | record identity; predecessor link where a correction | the reader's `AUTH` |
| Scope | as the act | — | **context-scoped**: a company auditor sees that company; a tenant owner sees the tenant; **cross-company read only under `XCR-02`** (`MTI-D-04` unruled → conditional); **platform-stream records are readable by platform principals only, and by the target tenant for the acts on it** (`✎`). **A control that must assess acts in several tenants (a `CF-I-03R` sweep of a platform grant) runs as N tenant-context runs, each inside its tenant, whose *results* are lifted to platform context — never as one platform-context read of N tenant streams** (`CHA-09`; the `G5` `T(i)`/`P` rule) |
| Time semantics | — | forever from creation | — |
| Before/after · lineage | — | edit attempts are audited refusals | — |
| Retention | `MTI-50` | `BR-AUD-001/002` | — |
| Evidence use | element 16 | — | `FR-AUD-002`/`-003` |
| Runtime proof | `RT-AUD-06`: element 16 of an emitted handoff resolves to a retained record | `RT-AUD-07`: an update or delete against the audit store is refused and audited | `RT-AUD-08`: a company-A auditor querying company B receives a **structurally different** result from an empty company, not the same zero (`CF3-C-02`'s rule) |

---

## 4. Reconciliation with the two existing schemas — what each must gain, stated as a patch

| Schema | Keep | Add (conceptual) | Correct |
|---|---|---|---|
| `FDS_AUDIT` §12 | `audit_id`, `tenant_id` (as `A1`), `user_id` (as `B1` with class + version), `action`, `resource`, `resource_id` (as `B3`), `before_value`/`after_value`, `request_id` (as attempt identity carrier), `created_at` (as **entry** date) | **scope class · company · warehouse · operation type + platform class · authority (grant identity + resolved tuple + `CF-I-03` run) · physical event date · evidence reference · predecessor link** | `BR-AUD-003` *"Audit belongs to Tenant"* → *"Audit belongs to the act's context; platform-scoped acts belong to the platform stream with the target tenant as object"*; §14 risks gain mitigations (`RT-AUD-07`, `C3`); `BR-REP-002`'s pointer *"section 8"* → §11 |
| `FDS_SUBSCRIPTION_MODULE` §12 | its ten | the same additions; **scope class = `PLATFORM`** for `FR-SM-005` and plan/module acts, with the target tenant as object; **`reason` mandatory** (`SA_CORR5_02` class 1) | — |
| `FDS_TENANT` §10 | `tenant.status_changed (actor, old_status, new_status, reason)` — the one event already carrying reason | authority; scope class `PLATFORM`; two dates | — |

**Copying vendor structure — tested:** no field, table or column name from the reference estate is
carried; the axes are the ruled `MTI-D-02` dimensions and the `MTI-38` invariant text.

---

## 5. Consumers of the contract, and the runtime obligations gathered

| Consumer | Uses |
|---|---|
| `CF-I-03` / `CF-I-03R` | `B2` as the act's recorded `AUTH`; `B4` as the act's timestamp; `C2` for the sweep population |
| `MTI-19` | `A1`–`A3` as stored context vs derived |
| Handoff contract | `A1`–`A4`, `B1`–`B4`, `C1` map to `HF-CTX-01`…`-11` and elements 3, 12, 13, 16 |
| Reporting (`FDS_REPORTING` `REP-001`, `REP-003`) | `C3` scoping |
| Pre-Test Matrix | `RT-AUD-01`…`-08`; plus **`RT-AUD-09` synthetic injection** — inject one event with a deliberately absent axis and confirm the sweep moves `0 → 1` |

## 6. What this file does not do

Choose a log technology, table, column or partition · rule `MTI-D-04` (visibility across companies stays
conditional) · decide retention periods · set a platform-stream reader role beyond *platform principal*
(`G4`'s role question) · build anything.

## 7. Residual

1. **The platform-stream visibility rule (`C3`, `✎`) is originated here.** The alternative — platform acts
   mirrored into the target tenant's own stream — is coherent; it was rejected because a tenant-stream
   record whose actor is outside the tenant breaks `A1`'s meaning. Challenge target.
2. **`operation type` on non-Inventory acts.** The ruling is Inventory-scoped; the contract applies `A4`
   as *platform operation class* to every module and `N/A + reason` where a module has no operation
   classes yet. Whether Accounting/Sales/Purchase adopt operation classes is their design, not settled
   here.
3. **Two schemas were re-measured; a third may exist.** The escape-tolerant sweep covered the 17 `FDS`
   files and `ARC-WP-*`; a module-level audit list elsewhere in `U2` would be outside this file's
   population. Declared, not closed.

## 8. Checkpoint

> ## `CP-SA-C5-30 — G3 AUDIT SHAPE SA-SPEC COMPLETE`
> **Four-axis requirement reconstructed from 6 primary sources · 12 contract axes (incl. situational
> location, `CHA-08`) × 10 attributes · 3 gaps named (axes, authority, time) where CORR4 named 1 ·
> 3 schemas reconciled with stated patches · 9 runtime obligations · 0 vendor structure copied ·
> corrected by `CHA-08`, `-09`, `-11`.**

**Next autonomous action:** `CP-SA-C5-40` (`SA_CORR5_04`).

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
