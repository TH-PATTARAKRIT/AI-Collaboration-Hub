# 64 — EQUIPMENT / ASSET BOUNDARY V2

**LAYER 2 — AUDIT QUARANTINE.** Scope-aware correction preserved; `36` stands.

---

## 1. Re-verified with the fourth database

`36` §1 established from source that Equipment and Asset are **unlinked objects**. Now
checked against a deployment that has both:

| Object | `iTEST02` | `iSMEs` | `BK12MAY26` |
|---|---|---|---|
| `account_asset` | 12 | 685 | 36 |
| `maintenance_equipment` | present, not enumerated | 0 | 0 |
| `mrp_maintenance` installed | **yes** | no | yes |
| Equipment → asset reference | **none in source** | — | — |
| Operation → equipment reference | **none in source** | — | — |

> The only link is equipment → **work centre**. Confirmed with the maintenance bridge
> **installed** (`iTEST02`), which removes the "maybe the module was missing" objection.
> `FACT VERIFIED`.

## 2. Scope determinations — unchanged, now with incidence

| Object | Ownership | Financial effect | Company context | Incidence measured |
|---|---|---|---|---|
| Equipment register | **`TENANT`** | none | not required | — |
| Asset | **`COMPANY`** | **yes** — depreciation | **mandatory** | 733 assets across 3 databases |
| Work centre — resource | **`TENANT`** | none | not required | 60 |
| **Work centre — rate** | **`COMPANY`** | **yes** — enters inventory value | **mandatory** | **1 of 60 rated; 0 of 60 company-less** |
| Routing operation | `TENANT` | none | not required | 154 |

## 3. `SCOPE-02` — mechanism stands, incidence now measured at zero

| | |
|---|---|
| **Mechanism** | The rate is a `COMPANY`-scoped financial parameter on a record whose company column is **nullable**. `CTR-P03-06`. **Unchanged — `FACT VERIFIED`** |
| **Incidence** | **0 of 60** work centres are company-less in the only deployment that has any |
| **Severity** | **High → Medium.** Reduced on measured incidence, not on the mechanism |
| **Status** | **OPEN**, preserved for P11 |

**Why it is not closed.** A nullable column that no one has yet left null is still a
nullable column, and `MISSING REQUIRED SCOPE = DENY` is a rule about what the system
*permits*, not about what a sample of 60 rows happens to contain. `P11-D-2` — what closes a
scope defect whose incidence is zero — is exactly this question and remains P11's.

## 4. Dissent preserved

P03's dissent from any reading that extends P04's tenant narrowing from Equipment to Asset
is **unchanged and reinforced**: §1 confirms with the bridge installed that the two objects
are not linked, so a scope conclusion about one carries no information about the other.

Recorded for P11 — `37` §3 `D-1`.
