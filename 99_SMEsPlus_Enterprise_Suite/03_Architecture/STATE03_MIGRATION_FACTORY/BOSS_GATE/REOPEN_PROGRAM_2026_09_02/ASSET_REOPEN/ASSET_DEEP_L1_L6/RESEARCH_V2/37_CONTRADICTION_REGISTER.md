# 37 — CONTRADICTION REGISTER
**LAYER 2 — AUDIT QUARANTINE**

Required under §74. Every contradiction carries the full mandated field set.

---

## `CTR-01` — The configured depreciation method has no implementation in the target version line

| Field | Content |
|---|---|
| **Claim A** | The controlled Asset Models use a Thai straight-line depreciation method |
| **Evidence A** | `EV-XLS-01` — an Asset Model export listing that method label on every model |
| **Claim B** | No such method exists in the v18 product, and no implementation of it exists in any v18- or v19-line tree in this workspace |
| **Evidence B** | `SRC-01` — the product's method field offers three values, none of them this one. `SRC-27` — the only implementation found is a **v14** custom module. `SRC-28` — no port found |
| **Severity** | **High** |
| **Business impact** | If the 217 running assets are not on an equivalent calendar-day basis, their monthly depreciation is wrong by up to 8% in February and 1.9% in 31-day months, every year |
| **Accounting impact** | Monthly interim accounts and any monthly product costing are misstated. **Annual totals differ by only 0.05%, so an annual review will not detect it** |
| **Architecture impact** | Determines whether SMEsPlus must build a Thai method or merely select a configuration |
| **Possible explanations** | (a) `EV-XLS-01` was exported from the v14 legacy system, not the UAT; (b) a v18 port exists on the server but not in this workspace; (c) the v18 assets use the standard calendar-day mode and the label in the export is historical |
| **Required evidence** | The computation mode of the 217 running assets, read from the UAT; and the provenance of `EV-XLS-01` |
| **Resolution** | **Materially de-escalated by `17`**: the custom method and the standard calendar-day mode are numerically equivalent within rounding. The capability is reproducible by one configuration field. The **exposure** is unchanged; the **remedy** is cheap |
| **Status** | **OPEN — `UNR-02`.** Highest-priority open item in this session |

---

## `CTR-02` — The custom Asset↔Equipment link's disposal behaviour is dead code

| Field | Content |
|---|---|
| **Claim A** | Selling an asset deactivates its linked equipment record |
| **Evidence A** | `SRC-22` — a wizard override implementing exactly that, present in the module |
| **Claim B** | The override never executes |
| **Evidence B** | `SRC-21` — the module's package initialiser imports only the models package. The wizard file is never imported, so the override is never registered |
| **Severity** | **Medium** technically, **High** as a class of defect |
| **Business impact** | Sold and disposed machines remain active in the equipment master, still flagged as taken-to-assets. The operational register drifts from reality with no mechanism to correct it |
| **Accounting impact** | None directly |
| **Architecture impact** | Two further constructs in the same module also do nothing (`19` `EQ-DEF-02`, `EQ-DEF-03`). **Three of the module's four intended behaviours are inert**, and none raises an error |
| **Possible explanation** | The module was migrated forward from an earlier version and the initialiser was not updated |
| **Required evidence** | Behavioural confirmation on the UAT: sell a linked asset and observe the equipment |
| **Resolution** | Not resolvable statically beyond the initialiser evidence, which is conclusive for the import |
| **Status** | **CONFIRMED from source; behavioural confirmation open — `UNR-13`** |

---

## `CTR-03` — Two different asset models existed in the legacy system, with the two capabilities the Boss relies on attached to different ones

| Field | Content |
|---|---|
| **Claim A** | The legacy system had an asset with a Thai daily depreciation method |
| **Evidence A** | `SRC-27` — the custom Thai module extends the **product's** asset model |
| **Claim B** | The legacy system had an asset with an equipment link |
| **Evidence B** | `SRC-25` — the legacy custom link file extends a **different, third-party** asset model |
| **Corroboration** | `SRC-31` — the v14 tree contains two third-party modules each defining that second asset model, alongside the product's own |
| **Severity** | **Medium** |
| **Business impact** | **A single legacy record cannot have carried both capabilities.** Any recollection of "the asset with the equipment link that depreciated daily" refers to two different objects, or to a later reconciliation |
| **Accounting impact** | None directly; it affects what "the legacy behaviour" means as a migration target |
| **Architecture impact** | High. The design has been treating a composite mental model as a single precedent |
| **Possible explanation** | Two vendors, two eras, two module families installed on one database |
| **Required evidence** | Which asset model held the live legacy data. Answerable from the legacy database |
| **Resolution** | Partially resolved: on **v18** the two capabilities are no longer split — the custom link (`SRC-20`) targets the product's asset model. The split is a **legacy** artefact |
| **Status** | **OPEN for the legacy question; resolved for v18** |

---

## `CTR-04` — A financial action mutates an operational record, with no inverse

| Field | Content |
|---|---|
| **Claim A** | Confirming an asset is a financial action |
| **Evidence A** | `SRC-01` — the confirm routine posts entries |
| **Claim B** | Confirming an asset writes to the equipment master |
| **Evidence B** | `SRC-20` — the custom confirm override flips the equipment's status |
| **Severity** | **Medium** |
| **Business impact** | Cancel an asset after confirming it and the equipment stays flipped. `CTR-02` means selling it does not reset it either. **The status is one-way** |
| **Accounting impact** | None |
| **Architecture impact** | An unowned cross-domain write with no transaction boundary stated and no reverse path. Raised by Expert 3 (`07`) and Expert 2 (`09`) independently |
| **Required evidence** | Whether the write participates in the confirm transaction |
| **Resolution** | Not resolvable statically |
| **Status** | **OPEN — `UNR-13`** |

---

## `CTR-05` — The posted gain on disposal and the stored gain on disposal can differ

| Field | Content |
|---|---|
| **Claim A** | Gain on sale = proceeds − book value |
| **Evidence A** | `SRC-01` — the stored field is computed exactly that way |
| **Claim B** | The posted gain/loss is the balance of gross cost, accumulated depreciation and proceeds — which **includes** the not-depreciable amount |
| **Evidence B** | `SRC-01` — the disposal entry writes out the **full original value** |
| **Compounding factor** | Book value is computed **after** the state is set to `close`, and the closure clause **subtracts** the not-depreciable amount |
| **Severity** | **Low** in the ledger, **Medium** for any consumer of the stored field |
| **Business impact** | Two different gain figures for the same disposal, differing by exactly the not-depreciable value |
| **Accounting impact** | **The posted figure is correct.** The stored field is the inconsistent one — and it is **not visible in the standard form**, so the discrepancy is invisible to users and available to integrations |
| **Architecture impact** | SMEsPlus must not read the stored field |
| **Resolution** | Characterised at Level 6 (Expert 3, `D6-03`) as a presentation inconsistency inside a correct accounting treatment |
| **Status** | **RESOLVED — characterised. Carried into `39` as a design rule** |

---

## `CTR-06` — The board invariant is ORM-enforced, and the population was loaded by migration

| Field | Content |
|---|---|
| **Claim A** | Every running asset's last depreciation line leaves exactly zero remaining |
| **Evidence A** | `SRC-01` — a model constraint enforcing precisely that |
| **Claim B** | The constraint is evaluated on ORM write. A direct data load does not evaluate it |
| **Evidence B** | The constraint's declaration; `EV-HND-01` describes a bulk migration of 280 assets |
| **Severity** | **Medium**, pending measurement |
| **Business impact** | Assets may exist whose schedule does not close to zero, with nothing reporting it |
| **Accounting impact** | Sub-ledger internally inconsistent; not necessarily divergent from the GL |
| **Architecture impact** | SMEsPlus should enforce this at the data layer, not only in the application |
| **Required evidence** | Whether the migration used the ORM; and a count of assets violating the invariant |
| **Status** | **OPEN — `UNR-25`** |

---

## Summary

| ID | Severity | Status |
|---|---|---|
| `CTR-01` | High | Open, de-escalated by `17` |
| `CTR-02` | Medium / High as a class | Confirmed from source |
| `CTR-03` | Medium | Open for legacy, resolved for v18 |
| `CTR-04` | Medium | Open |
| `CTR-05` | Low / Medium | Resolved — characterised |
| `CTR-06` | Medium | Open |

The prior session recorded **no contradictions**. That was a consequence of
documentation-only evidence, not of their absence — `29` `REV-09`.
