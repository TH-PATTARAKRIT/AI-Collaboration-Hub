# [SMEPLUS-26-09-05-INV-MTI-CONTROLLED-REMEDIATION-001]
# 07 — Consuming Module Obligation Matrix R2

Control Level: `/L9999.9999`
Topology Scope: `SHARED SaaS POOL`
Status: `8 OF 8 MODULES GIVEN AN OBLIGATION — 11 CONTEXT FIELDS — PAYMENT DISCHARGED AS A COVERAGE ITEM, NOT AS A HANDOFF — 0 HANDOFFS CONTRACT-COMPLIANT`

---

## 1. What Changed, And Why

`MTI-45` published seven consuming modules. `MTI-D-02` widens what each must carry, and the authorization's theme 13 names **eight**, adding Payment — which is `RC-F-09`.

Three changes run through every row:

1. **`AUTH` joins `CTX` as a mandatory, non-inferable input.** A consumer receiving a fact must be able to state not only where the fact belongs but under what authority it was produced. `MTI-45` R2.
2. **Two new fields.** `HF-CTX-10` operation-type identity; `HF-CTX-11` authorization attestation. `CD-25`.
3. **Rejection is the required behaviour on absence.** A consumer that supplies a missing context, or accepts a fact whose attestation is absent or failing, has defeated the control. This is not new — `MTI-45` already required it — but under `MTI-D-02` there is more that can be absent.

---

## 2. The Context Field Group R2 — Eleven Fields

`HF-CTX-01` .. `HF-CTX-09` are carried unchanged from `06_CROSS_MODULE_HANDOFF_CONTRACT_FIELDS.md` at `dcb9227` and are **not restated**, per the transcription rule at `03` §1.1. The two additions are stated in full.

| Field | Content | Mandatory | Owner | Governing |
|---|---|---|---|---|
| `HF-CTX-01` .. `HF-CTX-09` | Carried unchanged — tenant, company, warehouse, location, anchor path, conformance attestation, cross-context relationship identity, authority reference, owner dimension | as published | as published | as published |
| **`HF-CTX-10`** | **Operation-type identity of the act, as the resolved tenant-configured operation type together with its platform-owned operation class (`CF-I-05`)** | **Always, where the fact arose from an act performed through an operation type; `N/A` with reason otherwise** | Inventory | `MTI-D-02` §4; `MTI-09` R2, `MTI-38` R2 |
| **`HF-CTX-11`** | **Authorization attestation — the identifier of the control run that last asserted the authorization conformance property (`CF-I-03`) over this act's class, with its timestamp and result** | **Always** | Inventory + SaaS Foundation | `CF-F-05`; `CF-I-03`, `MTI-43` R2, `MTI-50` |

### 2.1 Why both fields, and why the second is presently a reference to nothing

`HF-CTX-10` closes the **carriage** half. Without it, `MTI-D-02` §4's requirement — that the audit trail answer *who performed what action under which tenant, company, warehouse and operation type* — has no carrier on a handoff payload.

`HF-CTX-11` closes the **guarantee** half, and it is the direct consequence of `CF-F-05`. The invariant set's own reasoning at `06` §3.1 is the governing statement:

> *"`HF-CTX-06` is deliberately a reference to a control run rather than a boolean. A boolean is an assertion by the emitter about itself; a control-run reference is inspectable by the consumer and by an auditor."*

The published fields give the context half both a value and an attestation, and give the authority half a **value only** (`HF-CTX-08`). Under `MTI-D-02` the authority half is now a four-axis grant and is exactly as much in need of a guarantee as the context half was.

**`HF-CTX-11` presently references a control that does not exist.** `CF-I-03` specifies it; nothing builds it. **This is stated rather than smoothed over**, and it is why element 10's status does not move and why `AAS-V-01` remains in force with the wording `specified, not built, not verified` used and no other.

---

## 3. The Eight Consuming Modules

`CTX` and `AUTH` are mandatory and non-inferable for all eight. **A consumer may not derive, default or reconstruct either** (`MTI-45` R2).

| # | Module | Fields Required | Obligation On The Consumer | Lineage | Change From Published |
|---:|---|---|---|---|---|
| 1 | **Accounting** | `HF-CTX-01`, `-02`, `-05`, `-06`, `-07`, `-08`, `-09`, **`-10`**, **`-11`** | Post within the company the fact resolves to and no other. May not infer, default or reconstruct company. **Must reject a fact whose context attestation *or* authorization attestation is absent or failing** | `HO-07`, `-09`, `-10`, `-11`, `-12`, `-14`, `-17`, `-20`, `-22`, `-24` | Two fields added; rejection condition widened to two attestations |
| 2 | **Purchase** | `HF-CTX-01` .. `-04`, `-08`, **`-10`**, **`-11`** | A proposal or expected receipt is actioned only in its own company. Over-receipt tolerance and approver are per company. **The receiving operation type is carried, not re-derived from the document type** | `HO-04`, `-05`, `-06` | `HF-CTX-10` added — a receipt is an operation type and Purchase acts on its outcome |
| 3 | **Sale** | `HF-CTX-01` .. `-04`, `-08`, `-09`, **`-10`**, **`-11`** | Availability promised is availability in the customer's company. **The owner dimension must not be read as availability.** The despatching operation type is carried | `HO-01`, `-02` | `HF-CTX-10` added |
| 4 | **Manufacturing** | `HF-CTX-01` .. `-04`, `-08`, **`-10`**, **`-11`** | Component demand and output resolve to one company; batch genealogy links identities within one company or via `XCR-01`. **Under `MTI-D-01` a component and its output are company-scoped products and genealogy may never be reconstructed from product attributes** | `HO-18`, `-19`, `-20` — conditional on `GAP-FS-19` scope ruling | `HF-CTX-10` added; `MTI-D-01` consequence stated |
| 5 | **Approval** | `HF-CTX-01`, `-02`, `-08`, **`-10`**, **`-11`** | **An approver must hold `AUTH` in the record's own company, warehouse and operation type.** Approval routing may not cross a company boundary. Segregation of duties composes with, and never overrides, the context boundary | `L7-03`, `L7-04`, `L7-09` | **Materially widened.** The published obligation was company-level; under `MTI-D-02` an approver holding company authority but not the warehouse or operation type is **not** a qualifying approver |
| 6 | **Document** | `HF-CTX-01`, `-02`, `-08`, `-11`, **`-10`** | An attached document inherits the `CTX` of the fact it evidences and is visible only within the `AUTH` set that may see that fact. **PDPA scope is `GAP-MD-29`, zero coverage anywhere — `MTI-D-05`, unruled** | `INV-F-04`, `-07`, `-12`, `-14`, `-19`, `-41` | Visibility bound to `AUTH` rather than to `CTX` alone |
| 7 | **Reporting** | `HF-CTX-01` .. `-04`, **`-10`**, plus the report's own scope statement | Scope **before** evaluation, never filter after. State the `CTX` scope **and the `AUTH` set** as part of the report identity. No cross-company aggregation except under `XCR-02` | `HO-26`, `-27`; `INV-M10` .. `INV-M15` | Report identity gains the `AUTH` set — two reports produced under different `AUTH` sets are different reports |
| 8 | **Payment** | **See §4** | **See §4** | **No published Inventory handoff** | **New coverage item — `RC-F-09`** |

### 3.1 The Approval obligation is the one most likely to be got wrong, and it is now harder

The published package already recorded this at `06` §6.1: segregation of duties requires a *different person*; the context boundary requires the approver be *inside the same company*; in a Thai SME with two office staff those can conflict directly, and **the context boundary wins**.

`MTI-D-02` makes the conflict sharper, not softer. The qualifying approver must now match on **three** axes, not one. In a two-person company where one person runs the warehouse and the other does the books, there may be **no second actor holding the operation type at all** — and segregation must then degrade to a compensating control rather than be satisfied by relaxing an axis.

**The compensating control's content requires Thai user input.** `MTI-F-05`, `R4-F-21`, Lane C, `0 of 78`. **No AI may supply it and none is supplied here.**

---

## 4. Payment — `RC-F-09` Discharged As A Coverage Item

The authorization requires this session to *"either state Payment's obligation or record why it has none."* Both halves are answered, in that order, and the search boundary is declared first.

### 4.1 The search, with its boundary

**Boundary `B-01`**, declared at `01` §8.

| Element | Value |
|---|---|
| **Population** | The 74 published `.md` files of the four evidence packages, widened to the **86** files under `…/REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/` and the **29** under `…/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/`, plus both governing Boss controls read at their approval commits |
| **Pattern** | case-insensitive `payment\|payable\|receivable\|remittance\|settlement` |
| **Path set** | The two tree roots above on this branch, which is a descendant of all four cited tips and whose upstream folders are digest-identical to their published manifests — 70 of 70 |
| **Unit** | One matching line |

**Result:**

| Source | Hits |
|---|---:|
| Inventory R4 Deep Research — 26 files at `fc0b168` | **0** |
| Inventory R4 AAS+ / PMO Review — 15 files at `e218e5b` | **0** |
| Inventory Multi-Tenant Invariant Set — 17 files at `dcb9227` | **0** |
| MTI Ruling Consolidation — 17 files at `a57bd55` | 7 files, **every hit tracing to `RC-F-09` itself or to the authorization at file `13`** |
| Minimum Handoff Data Contract at `d9e845e` | **0** |
| 22-Scenario Cross-Proof Baseline at `296b495` | **0** |
| Account Reopen prompt — outside Inventory scope | 4 lines, all Accounting-side (bank/cash/payment reconciliation, withholding tax) |

**No published Inventory-to-Payment handoff exists within boundary `B-01`.** `HO-01` .. `HO-28` and `HX-01` .. `HX-31` contain none; the sixteen contract elements name none; the twenty-two scenarios name none.

Class **`A` within boundary `B-01`.** Class **`B`** for the wider system: Payment is an Accounting-side concern with its own reopen track, and this session searched the Inventory chain, not that track. **`NO EVIDENCE FOUND` is not `DOES NOT EXIST`.**

### 4.2 A fidelity observation on the citation — `CF-F-06`

The consolidation's control rule `C-04` at `04` §4 reads:

> *"Every consuming module — Sale, Purchase, Manufacturing, Accounting, Reporting, Approval, Document, Payment — consumes product identity **through** tenant/company context, never by inference"* — Source: `D-01` rule 6.

`MTI-D-01` rule 6 as ruled reads:

> *"Inventory, Sale, Purchase, Manufacturing, Accounting, Reporting, Approval, and Document modules must consume product identity through tenant/company context."*

**Rule 6 does not name Payment.** The consolidation merged the ruling's eight-module list with the authorization's theme-13 list under a single citation to the ruling. The same package states the position correctly elsewhere — `07` §9.1: *"Payment is named in this authorization's theme 13 and does not appear in the invariant set's seven-module obligation table"* — so the package knew the distinction and the `C-04` row compressed it.

**Severity: observation. It changes no conclusion**, because Payment's obligation is required by the authorization's theme 13 whether or not the ruling names it. It is recorded because a control rule that cites a ruling clause should be readable against that clause. Owner PMO. Recorded as `CF-F-06`.

### 4.3 Payment's obligation, stated

Payment is a consuming module under `MTI-45` R2 whether or not a direct Inventory handoff is ever mapped. **The generic obligation applies and is stated; a handoff-specific obligation cannot be stated because no handoff is published.**

| # | Payment's obligation | Basis |
|---:|---|---|
| `PAY-01` | Payment receives `CTX` and `AUTH` as **mandatory, non-inferable** inputs on any fact that originates in Inventory, however it arrives | `MTI-45` R2 |
| `PAY-02` | **Payment may not infer, default or reconstruct company from a payment instrument, bank account, vendor, customer, currency or settlement route.** Where a group shares banking, the instrument is not evidence of the company a fact belongs to | `MTI-D-01` rule 6; `R-03` at `04` §3; `MTI-42` |
| `PAY-03` | Payment resolves product identity **through** company context and never by code, name, barcode, UoM or description similarity — the same prohibition every other consumer carries | `P-02`, `P-05`, `CF-I-06` |
| `PAY-04` | A settlement, allocation or matching act that spans companies is a **cross-context act** and requires an `MTI-22` register entry. **No such entry exists**, so under `MTI-03` it is prohibited outright rather than merely unauthorized | `MTI-03`, `MTI-22` R2, `05` §5 |
| `PAY-05` | **Every valuation, cost, recognition-timing and posting consequence of any Payment-side treatment is out of Inventory's ownership and is held** | `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |

**`PAY-01` .. `PAY-05` are obligations, not a handoff contract.** They constrain what Payment may do with an Inventory-originated fact. They do not assert that such a fact reaches Payment, and they do not map any handoff.

### 4.4 The decision this leaves open — `CF-D-04`

Whether Payment is a **direct** consumer of Inventory facts is a scope question this session may not answer. Three readings are consistent with the evidence and are stated with their consequences. **None is chosen.**

| Option | Reading | Consequence if taken |
|---|---|---|
| **(i)** | Payment has **no direct** Inventory obligation and inherits context through Accounting and Purchase | `PAY-01` .. `PAY-05` remain as inherited constraints; no handoff is mapped; `RC-F-09` closes as *coverage stated, no handoff exists*. **Cheapest, and consistent with boundary `B-01`'s result** |
| **(ii)** | Payment is a **direct** consumer for at least one flow — for example a settlement that must reference a receipt or a return | A handoff must be identified, mapped into the `HO-*` register, and subjected to the sixteen contract elements. **`0 of 10` material handoffs becomes `0 of 11`, and the new one starts non-compliant on the same three elements** |
| **(iii)** | Payment is **outside Inventory's scope entirely**, and theme 13's naming of it is an authorization-drafting artefact | `RC-F-09` closes as *out of scope*. `MTI-45` R2 reverts to seven modules. **Requires a Boss statement, because the authorization named it** |

**`RC-F-09` is discharged as a coverage item and is not closed.** The authorization asked for an obligation or a reason; both are supplied. Closure requires `CF-D-04`.

---

## 5. Element-By-Element Position — R2

For the ten material Inventory-to-Accounting handoffs at `16` §3 of R4. **The published positions are carried; only the changed rows are stated.**

| # | Element | Position After This Session | Suppliable? |
|---:|---|---|---|
| 8 | `WHICH Product / Lot / Serial` | **Simplified.** The product half of the resolved tuple is company-resolved by construction under `MTI-D-01`. The lot and serial halves are unchanged — the identity is the tuple, never the bare value | Yes, subject to implementation |
| 9 | `WHICH Warehouse / Location` | Unchanged in content. **Warehouse is now also an authorization axis**, so `HF-CTX-03` is read by two controls rather than one | Yes, subject to implementation |
| **10** | **`WHICH Company / Tenant`** | **`specified, not built, not verified`.** The obligation is **widened**: the value plus the anchor path plus **two** attestations, one of which (`HF-CTX-11`) references a control that does not exist | **`specified, not built, not verified`** — `AAS-V-01` in force, **no other wording is used** |
| 2 | `WHO owns the fact` | **Widened.** `HF-CTX-08` must now be readable together with the four-axis `AUTH` in `HF-CTX-10` and the attestation in `HF-CTX-11` | Yes, obligation widened |
| 14 | `WHICH Migration / Replay Batch` | **Not suppliable, scope grown.** `CD-09` makes deliberate duplication something the provenance reference must evidence. **`REV-F-02` still governs its conditionality** — contractually required on migration, replay and recovery handoffs, not on all ten | No — `GAP-FS-08` |
| 16 | `WHAT Evidence proves it` | **Widened.** The evidence must now cover the authorization half as well as the context half | Partial |
| 1, 3, 5, 6, 11 | | Unchanged | Yes |
| 4, 7 | `WHEN financial recognition` / `WHAT valuation` | **Unchanged** | No — **`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`** |
| 12, 13 | | Unchanged — rank 2 dependent | Partial |
| 15 | `WHICH Idempotency Identity` | **Unchanged** | No — `RISK-C02` |

**Zero of the ten material Inventory-to-Accounting handoffs is contract-compliant. Unchanged.** Four elements had their obligations widened by conformance, which moves the target further away, not closer.

---

## 6. Coverage Result

| Measure | Result |
|---|---:|
| Consuming modules given a field obligation | **8 of 8** |
| Context field group | **11 fields** — `HF-CTX-01` .. `HF-CTX-11` |
| Fields added by this session | **2** — `HF-CTX-10`, `HF-CTX-11` |
| Modules whose obligation is materially widened | **1** — Approval |
| Modules gaining `HF-CTX-10` | **7** — all but Payment, whose handoff is unmapped |
| Modules with a **published** Inventory handoff | **7 of 8.** Payment: **0**, within boundary `B-01` |
| Payment obligations stated | **5** — `PAY-01` .. `PAY-05` |
| Fields referencing a control that does not exist | **1** — `HF-CTX-11` → `CF-I-03` |
| Contract elements whose obligation is widened | **4** — 2, 10, 14, 16 |
| Contract elements whose position improves | **1** — element 8, simplified |
| **Material handoffs contract-compliant** | **0 of 10 — unchanged** |
| **Handoffs verified against any obligation** | **0.** No implementation exists |
| Findings closed | **0.** `RC-F-09` is **discharged as a coverage item**, which is not a closure |

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
