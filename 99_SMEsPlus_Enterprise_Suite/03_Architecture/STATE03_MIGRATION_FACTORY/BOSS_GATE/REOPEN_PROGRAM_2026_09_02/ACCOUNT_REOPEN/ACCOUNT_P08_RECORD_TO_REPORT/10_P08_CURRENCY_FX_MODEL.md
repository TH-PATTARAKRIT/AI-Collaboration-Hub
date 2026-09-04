# P08_CURRENCY_FX_MODEL

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · Layer 1

GB-08 has frozen the SMEsPlus business semantics. This file does **not** re-decide them. It measures the gap, and it re-expresses the ruling under the corrected scope model.

## 1. Scope re-expression (per `SMEPLUS-26-09-04-ACC-REV2-CORR1`)

The benchmark holds three different objects in one table and applies four different scoping rules to it. Separating them is the substantive result of this file.

| Object | Scope | GB-08 invariants that apply |
|---|---|---|
| The currency unit | `PLATFORM` | none |
| A published market rate observation | `PLATFORM` | none — a platform reference rate is legitimately readable by every tenant |
| The tenant's approved rate policy — which source, which rate type, for which purpose | `TENANT` | cross-tenant isolation |
| **The rate applied to a posting**, with its date, source, type and provenance | `COMPANY` | **all five**, in full |
| Period-end revaluation adjustment | `COMPANY` | all five |

GB-08's `FX-INV-01` and `FX-INV-02` apply in full to the fourth row and **not at all** to the second. Enforcing them against an undifferentiated rate table would make published reference rates unusable. Recorded as `P08-RQ-FX-01`: the three must be separated before either invariant can be enforced coherently.

## 2. Verified reference behaviour

| ID | Statement | Class |
|---|---|---|
| `FX-01` | A ledger item carries two parallel amounts and **does not carry the factor relating them**. The factor is a derived presentation value recomputed from current master data on every read. | FACT VERIFIED |
| `FX-02` | On invoice-family documents a bare factor is frozen on the header — a number with no date, no source and no type. On a **manual journal entry no factor is stored at any level**. | FACT VERIFIED |
| `FX-03` | Rate resolution is a **three-step silent cascade**: the most recent rate on or before the date; failing that, **the earliest rate ever recorded regardless of date** — necessarily later than the posting; failing that, **parity**. The three outcomes are indistinguishable to any consumer. | FACT VERIFIED |
| `FX-04` | The parity fallback is present in the framework rate resolver of **21 of the declared 22 roots**; the one exception is a 28-module partial tree. It is not version-specific and is not avoidable by choosing a different root. | FACT VERIFIED across the declared 22-root set (`RS-P-01`) |
| `FX-05` | Rate records are owned by the **top of the company tree**, or by **no company at all**. Subordinate entities are forbidden their own rates and always resolve against their topmost ancestor. Resolution crosses company boundaries upward by design. | FACT VERIFIED |
| `FX-06` | Where both a company-owned and a company-less rate exist, the **company-owned rate wins unconditionally, irrespective of date**. A company rate from years earlier outranks a shared rate from yesterday. | FACT VERIFIED |
| `FX-07` | At least one production conversion path **omits the company argument** and resolves under the currently active company rather than the company owning the fact. A second path reads a company from the calling context and then **ignores it**, resolving under the active company instead. | FACT VERIFIED |
| `FX-08` | A rate-purpose dimension with four values exists, but **solely as a reporting construct** computed inside a temporary structure for the life of one query and assigned **by account classification rather than by transaction**. It never attaches to a posted fact. Two shortcut paths emit different value sets for the same mode. | FACT VERIFIED |
| `FX-09` | **Posting-side and reporting-side resolution disagree** on whether company-less rates are admissible: posting admits them, reporting excludes them by strict equality. The same fact can convert two ways depending on the consumer. | FACT VERIFIED |
| `FX-10` | Rate records may be created, amended or deleted at any time, for any period including closed ones, with **no change history, no author record and no check against facts already posted with them**. | A VERIFIED ABSENCE, scope = the rate model in full and every extension of it in the target root |
| `FX-11` | Amending or deleting a rate leaves posted amounts intact, but **silently changes the factor displayed against those postings and every consolidated figure for the affected closed periods**. No as-of pinning exists. | FACT VERIFIED (mechanism); SUPPORTED INTERPRETATION (magnitude) |
| `FX-12` | Period-end revaluation exists as a genuine posted provision with an automatically created and immediately posted reversal. It is not a report-only adjustment. | FACT VERIFIED |
| `FX-13` | **The rate driving that posted revaluation may be typed in by hand at the point of running the report, need not exist in the rate master, and is recorded on the resulting posting only inside a human-readable line description.** The only controls are a screen warning and a refusal of zero. | FACT VERIFIED |
| `FX-14` | There is **no rounding-difference account**. Residuals from rounding two currencies independently are absorbed into exchange gain or loss and are indistinguishable there from genuine rate movement. | FACT VERIFIED |
| `FX-15` | No tenant dimension exists on the currency, the rate, the item or the company. | A VERIFIED ABSENCE, scope = the four modules bearing on ledger currency in the target root |
| `FX-16` | **No custom module in the project addon set modifies currency or FX behaviour in the ledger.** Every custom currency touch is a consumer of the standard conversion interface. | A VERIFIED ABSENCE, scope = the 65-module project custom addon set under a 20-symbol sweep; one archive file within it was **not** content-searched (`C NOT YET SEARCHED`) |

## 3. Gap against GB-08, re-scored under the corrected scope model

| GB-08 facet | Verdict | Change from the pre-correction reading |
|---|---|---|
| Resolve under current **tenant** | `SILENT` for platform reference rates; **`VIOLATES`** for the rate applied to a posting | previously scored a single blanket `SILENT` |
| Resolve under current **company** | **VIOLATES** — three independent mechanisms resolve under a company other than the fact's own (`FX-05`, `FX-07`) | unchanged |
| No valid rate = no posting | **VIOLATES** — no such gate exists; the cascade always returns a number (`FX-03`) | unchanged |
| Silent parity prohibited | **VIOLATES**, and **more broadly than the rule names**: the earliest-rate-ever substitution of `FX-03` is a second silent substitution the rule does not yet cover | unchanged, and widened |
| Posted fact retains rate | **VIOLATES** for entries and settlements; partially satisfied for invoice headers | unchanged |
| … rate date | **VIOLATES** | unchanged |
| … rate source | **VIOLATES** | unchanged |
| … tenant | **VIOLATES** for the posted fact | previously `SILENT` |
| … company | **SATISFIES** | unchanged |
| … currency pair | **SATISFIES** | unchanged |
| … rate type | **VIOLATES** — the dimension exists but attaches to no posted fact | unchanged |
| … provenance | **VIOLATES** | unchanged |
| Master change must not silently rewrite posted history | **VIOLATES** — posted amounts survive; the **reported view of closed history does not**, and the change is silent both in the making and in the effect | unchanged |

**Two gaps are wider than GB-08 currently articulates**, and are put to the ruling owner rather than resolved here:
- `P08-BD-07` — the **earliest-rate-ever** substitution is distinct from the parity substitution the ruling names. A remediation that eliminates only parity leaves it in place.
- `P08-BD-08` — the ruling speaks to resolution **at posting**. It is silent on whether **reporting** must resolve identically. `FX-09` shows the two currently disagree.

## 4. Requirements

| ID | Candidate requirement |
|---|---|
| `P08-RQ-FX-01` | Separate the platform observation, the tenant policy and the company-applied measurement into three objects with three scopes. |
| `P08-RQ-FX-02` | A measurement is pinned to the fact at posting: rate, rate date, rate source, rate type, currency pair, tenant, company, provenance. Nothing about a posted fact's measurement is recomputed later. |
| `P08-RQ-FX-03` | No implicit rate. No parity, no nearest, no earliest, no latest-ever. A missing required measurement is a **refusal with a named cause**, at posting and at settlement. |
| `P08-RQ-FX-04` | Reporting resolves identically to posting, or states explicitly and on the face of the statement that it is applying a reporting basis. |
| `P08-RQ-FX-05` | A measurement correction is itself dated and never silently retroactive; historical statements are pinned as of issuance. |
| `P08-RQ-FX-06` | A hand-entered rate that produces a posted fact is itself a governed, auditable fact — not a line of free text. |
