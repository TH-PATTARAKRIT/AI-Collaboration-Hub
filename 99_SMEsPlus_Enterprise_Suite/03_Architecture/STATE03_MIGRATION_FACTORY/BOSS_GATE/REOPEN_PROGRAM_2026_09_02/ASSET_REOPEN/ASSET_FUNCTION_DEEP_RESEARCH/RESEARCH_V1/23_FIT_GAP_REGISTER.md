# 23 — Fit/Gap Register

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `CLASSIFICATION REGISTER — NEVER "CLONE"`

---

Every reference-ERP capability examined is classified `ADOPT SEMANTICS` / `ADAPT` / `EXTEND` / `REJECT` / `UNKNOWN`. "Clone" is never used, per governing rule.

| Reference-ERP Capability | Classification | Reasoning |
|---|---|---|
| Straight-line / declining / declining-then-straight-line depreciation methods | `ADOPT SEMANTICS` | Well-evidenced, standards-consistent (IAS 16 systematic allocation), no reason to diverge from the general shape |
| Prorata computation options (no-prorata / constant-periods / days-per-period) | `ADOPT SEMANTICS`, with `EXTEND` for exact Thai day-count convention once file `08`/`16` HOLDs resolve | The general three-option shape is sound; the specific day-count math needs Thai-specific research this session did not complete |
| Not-Depreciable Value / residual exclusion from depreciable base | `ADOPT SEMANTICS` | Double-sourced (reference-ERP mechanism + IAS 16 principle), the strongest-evidenced item in the package |
| Modify Depreciation (mid-life adjustment) action | `ADAPT` | Mechanism confirmed to exist; exact GL account pairing unconfirmed, so SMEsPlus must adapt the shape while independently deciding the accounts |
| Equipment identity/category/company/used-by/work-center fields | `ADOPT SEMANTICS` | Well-evidenced, uncontroversial data-modeling pattern |
| Equipment status/state as a single enum | `UNKNOWN` | Not confirmed to exist in the reference ERP at all; SMEsPlus may need to design its own state model regardless (file `04`) |
| Equipment usage/meter/runtime tracking | `UNKNOWN` | Not confirmed present or absent; needed for Hypothesis C's "continuous usage" variant (file `21` BA-06) but no reference-ERP pattern to draw on |
| Equipment↔Asset native link | `REJECT the assumption of precedent` / `EXTEND` in practice | No native mechanism exists to adapt; SMEsPlus must build this link from scratch if it wants the lineage the governing brief envisions |
| Equipment↔Product native link | `UNKNOWN`, leaning `REJECT the assumption of precedent` | Same reasoning as above, weaker evidence base |
| Maintenance Request lifecycle/team/stage | `ADOPT SEMANTICS` | Well-evidenced, no reason to diverge |
| Maintenance Request cost field | `EXTEND` | Not confirmed native; if SMEsPlus wants cost visibility on maintenance, it must add this field, which the reference ERP does not appear to have |
| Maintenance cost → production cost integration | `REJECT the assumption of precedent` | No mechanism found; if desired, build new (file `06`) |
| Work Center cost-per-hour (per-workcenter / per-employee / override precedence) | `ADOPT SEMANTICS` | Well-evidenced, clean mechanism, directly reusable in concept for a depreciation-rate input extension |
| Depreciation → Work Center cost integration (Hypothesis A mechanism) | `REJECT the assumption of precedent` / `EXTEND` the Work Center rate concept | No existing mechanism; SMEsPlus would extend the existing rate-input pattern with a new depreciation-derived input, but this is new construction |
| Product/Bill → Asset capitalization path | `ADOPT SEMANTICS` | Reasonably evidenced, standards-consistent general pattern |
| Automatic Product→Equipment→Asset pipeline | `REJECT the assumption of precedent` | Does not exist as a single pipeline in the reference ERP (file `05`) |
| Off-Balance / statistical account mechanism | `UNKNOWN` | Search this session was narrower/time-boxed (file `14` §2); needs a dedicated follow-up before a fit/gap call can be made with confidence |
| Post-depreciation internal usage formula | `UNKNOWN` — n/a, not a reference-ERP capability at all | Purely original SMEsPlus design work; this register entry exists only to note there is nothing to adopt/adapt/extend/reject because no reference-ERP analogue exists |

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
