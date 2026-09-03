# 04 — Equipment Function Forensic

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `EVIDENCE COLLECTION`

---

## 1. Scope

Forensic review of the reference ERP's Equipment concept (maintenance-module domain object), per governing brief research object 02. Cardinalities are determined where possible and explicitly marked `UNRESOLVED` where public documentation does not reach implementation-level detail.

---

## 2. Field-by-Field Forensic

| Field | Reference-ERP evidence | Classification |
|---|---|---|
| Equipment Name | Documented as a required identity field on the equipment-creation form. | `FACT VERIFIED` |
| Equipment Category | Documented as a configurable classification field. | `FACT VERIFIED` |
| Company | Documented as a field on the equipment form. | `FACT VERIFIED` (existence) / `UNRESOLVED / EVIDENCE REQUIRED` (multi-company isolation enforcement mechanics) |
| Used By (employee/department/other) | Documented as a field (owner/user of the equipment). | `FACT VERIFIED` (existence) / `UNRESOLVED / EVIDENCE REQUIRED` (exact cardinality — one user at a time vs. a department-level pool) |
| Work Center | Documented as a field linking Equipment to a Work Center. | `FACT VERIFIED` (existence) / `UNRESOLVED / EVIDENCE REQUIRED` (cardinality — whether one Equipment can link to multiple Work Centers, or vice versa; documentation examples show single-link usage but do not state an enforced constraint) |
| Product link | Not confirmed as a native field in the official documentation retrieved this session. A third-party module was located that auto-generates and links a Product record when an Equipment record is created, which implies this link does **not** exist natively — otherwise such a module would be redundant. Treated as negative evidence, not proof of absence. | `UNRESOLVED / EVIDENCE REQUIRED`, leaning toward `NOT PRESENT NATIVELY` — see file `05` |
| Serial Number | Documented as a field where relevant (e.g., for serialized equipment). | `SUPPORTED INTERPRETATION` |
| Asset (fixed-asset) link | **No official documentation page located that describes a native field connecting Equipment to a fixed-asset Asset record.** Multiple independent sources (a forum thread explicitly titled around "integration between Equipment (Maintenance) and Assets Management," another titled "Fixed Assets integration with Maintenance/Equipment") describe this as something a business must build via customization (e.g., adding a Many2one-style link field), not something delivered out of the box. This is treated as reasonably strong negative evidence given multiple independent community sources converge on the same "no native link, build it yourself" conclusion. | `CONTRADICTED (of the assumption that a native link exists)` — see file `20` item on this |
| Maintenance Team / Maintenance Requests | Documented: Equipment is the subject of Maintenance Requests, grouped by Maintenance Team, with request history visible against the equipment record. | `FACT VERIFIED` |
| Usage / runtime / meter / machine-hours | Not independently confirmed in this session's retrieval as a native Equipment field. Preventive-maintenance scheduling is documented as time-based (frequency/interval), not meter/usage-based, in the pages retrieved. A usage/meter-based trigger was not ruled out but also not confirmed. | `UNRESOLVED / EVIDENCE REQUIRED` |
| Status/state (in service / idle / standby / maintenance / breakdown / out of service / disposed) | Not independently confirmed as a single enumerated state field. The documented mechanism instead appears to be: Equipment exists as a record; Maintenance Requests against it have their own stage (new/in progress/repaired/scrap); there is no confirmed single "Equipment.status" field synthesizing these into one of the seven states listed in the governing brief. | `UNRESOLVED / EVIDENCE REQUIRED` — do not assume a native seven-state enum exists |

## 3. Cardinality Findings (do not assume 1:1)

| Relationship | Evidence-based cardinality | Classification |
|---|---|---|
| Equipment : Work Center | Documentation examples consistently show a single Work Center per Equipment record in worked examples, but no explicit statement of an enforced 1:1 (vs. advisory) constraint was located. Plausible that one Work Center hosts multiple Equipment (many Equipment : one Work Center), which is the more common real-world pattern (a work center = a station with several machines). | `SUPPORTED INTERPRETATION`: many Equipment : one Work Center is the more plausible reading, but `UNRESOLVED / EVIDENCE REQUIRED` for a confirmed statement either way |
| Equipment : Maintenance Request | One-to-many (an Equipment record accumulates a history of many Maintenance Requests over time) — directly evidenced by the documented request-history view against an equipment record. | `FACT VERIFIED` |
| Equipment : Asset | No native link located at all (§2) — cardinality question is moot until/unless a link is confirmed to exist. | `UNRESOLVED / EVIDENCE REQUIRED` |
| Equipment : Product | No native link confirmed (§2); third-party modules suggest a 1:1 auto-generated pairing is a common *desired* pattern, not a native default. | `UNRESOLVED / EVIDENCE REQUIRED` |

## 4. SMEsPlus Candidate Semantics (Layer C)

`DESIGN CANDIDATE`, not adopted from any confirmed reference-ERP mechanism (because none was confirmed): SMEsPlus needs an explicit, first-class Equipment↔Asset link if Hypothesis A (depreciation flowing into production cost) and the post-depreciation internal usage formula (file `13`) are to be operationally meaningful — because without that link, there is no way to know which fixed asset's depreciation should be attributed to which Work Center's operating cost. This is flagged as a **build-from-scratch requirement**, not an adaptation of reference-ERP behavior, since no reference-ERP precedent for this link was found.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
