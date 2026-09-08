# SA11 — STANDARDS AND AUDIT CONTROL MAP

Status: **HOLD**
Governing law: master prompt §16 — the Audit and Standards function participates *during*
Phase SA, not after design.

**No certification or compliance is claimed anywhere in this map.** The objective is to
determine which standards apply, what SMEsPlus must support, what evidence is required, and
where the gaps are.

---

## 1. Status vocabulary (master prompt §16)

`SUPPORTED BY EVIDENCE` · `CONTROL GAP` · `STANDARD GAP` · `EVIDENCE GAP` ·
`NOT APPLICABLE` · `RESEARCH REQUIRED`

---

## 2. Accounting standards identified in the baseline

| Standard | Where it binds | Requirement established | SMEsPlus control | Status |
|---|---|---|---|---|
| **TAS 2 ¶12** (inventories — conversion cost) | Manufacturing → Inventory valuation | Fixed production overhead — **expressly including depreciation and maintenance of factory buildings, factory equipment and right-of-use assets used in production** — forms part of conversion cost. The asset lineage records the finding *"exceeds the question: absorption is required, not merely permitted"*, closed as `BLK-03 — CLOSED — EVIDENCE VERIFIED` | none yet | **`STANDARD GAP`** — see `SA11-F-01` |
| **TAS 2 ¶13** (normal capacity) | Overhead absorption denominator | Absorption requires a normal-capacity denominator | none | **`RESEARCH REQUIRED`** — open blocker `BLK-07`, `HOLD — DESIGN DECISION REQUIRED`, **Boss-owned**; the asset lineage records an explicit veto that no costing implementation may begin before it |
| **TAS 2** (net realisable value / write-down) | Inventory valuation | NRV write-down is an authoritative requirement with **no reference pattern to learn from** — recorded as *"original design work for SMEsPlus, not adaptation work"* | none | **`STANDARD GAP`** |
| **TAS 16** (property, plant and equipment) | Depreciation method and convention | Gazetted text **unretrieved** | — | **`EVIDENCE GAP`** — open blocker on the asset side |
| **Thai VAT / withholding statute** | SA-D07 | Statutory registers, form codes, filing | Company-scoped per `BD-ACC-02` | **`EVIDENCE GAP`** — `0 of 78` Thai validations; no authoritative government source consulted for form codes |

### SA11-F-01 — a requirement-versus-mechanism gap, corroborated three ways

TAS 2 ¶12 **requires** fixed production overhead to be absorbed into inventory value.

The measured position across four deployed databases is that **fixed production overhead has
no path into inventory value**: seven of eight overhead elements have no source path at all,
and the eighth — machine cost via a work-centre rate — has a path that is *not enabled*
(1 of 60 work centres rated).

The one structurally plausible route is closed by construction. The depreciation entry writes
its analytic distribution onto **both** legs; the legs are equal and opposite; therefore
**the analytic dimension nets to zero on a depreciation entry and can never accumulate a
depreciation cost pool.** This was reached independently by three separate packages —
manufacturing, asset and analytic — and is recorded as structural, configuration-independent
and version-independent.

**This is not a configuration gap and not a defect to fix in place. It is a requirement with no
mechanism.** For SMEsPlus it is original design work, and it is gated behind the normal-capacity
decision (`BLK-07`) that only Boss can take.

**Negative-claim discipline applied:** the permitted wording is *"no path verified in the
examined deployments"*, never *"no path exists"*. The source-side half of the claim is bounded
to the generations actually read; the measured half is version-independent and is the
load-bearing one.

---

## 3. Internal control and audit requirements

| Control domain | Requirement | Evidence expected | Status |
|---|---|---|---|
| Segregation of duties | Identity-based self-approval exclusion; requester and approver distinguishable | approval record naming actor and time | **`CONTROL GAP`** — `XD-03`, the occurrence half populated on 0 of 27,874 rows |
| Approval authority | Amount threshold or configured N-level | approval record with mandatory rejection reason | `SUPPORTED BY EVIDENCE` on the buy side; **`CONTROL GAP`** on the sell side (`XD-02`) and on cross-module auto-created documents (`SA03-F-02`) |
| Audit trail immutability | Events immutable; a correction is a new linked event, never an edit or delete | event store | **`CONTROL GAP`** — specified (`MTI-38`/`MTI-39`), `0` proven |
| Event date vs entry date | Two distinct values | both recorded | `SUPPORTED BY EVIDENCE` as a specification (`MTI-38`) |
| Period lock integrity | A locked period cannot be written | control assertion | **`CONTROL GAP`** — locked-period entries recorded as silently re-dated; and a lock enforced by *refusing* one operation while *silently declining half* of another, telling the user nothing |
| Derecognition completeness | A disposal produces a posted, non-deletable entry | posted entry | **`CONTROL GAP`** — the derecognition entry is recorded as left in draft and silently deletable, and a blank account link drops the corresponding leg |
| Privileged bypass | No unaudited elevation; named grant with grantor, grantee, reason, scope, expiry | permanent record | **`EVIDENCE GAP`** — `MTI-18` specified; unverifiable until the bypass audit completes |
| Master-data control integrity | Values determining every future accounting entry are enforced below the interface | non-interface write path testing | **`CONTROL GAP`** — three of the four values determining every future depreciation entry are enforced **only at the user interface**, so every import, migration, integration and scripted correction bypasses all three |
| Evidence retention | The evidence that each invariant held is itself retained and inspectable | retained attestation | **`CONTROL GAP`** — `MTI-50` specified, `0` proven |

### SA11-F-02 — the recurring control shape is "enforced by the screen"

Three independent findings share one mechanism: values that determine accounting outcomes are
constrained only at the presentation layer — the asset master-data case above, the sell-side
credit and availability advisories (`XD-02`), and a display-only value that differs from the
value actually posted in the machine-cost case.

**SMEsPlus determination (Nature DNA, ND-06): a control that exists only in the user interface
is not a control.** Every constraint that determines an accounting outcome must hold on every
write path — import, migration, integration, scheduled job and API included. Independent
rationale: `MTI-30` already requires deferred executions to carry their authority; a
screen-only constraint is the exact complement of that rule and would defeat it.

---

## 4. SaaS and data-governance control domains

| Domain | Requirement | Status |
|---|---|---|
| Tenant isolation | No cross-tenant read, write, reference, aggregation or influence | **`CONTROL GAP`** — 58 invariants specified, `0` proven, `0 of 13` enforcement surfaces verified, `0 of 52` negative access tests executable |
| Company boundary | Closed; cross-company only through an enumerated register | **`CONTROL GAP`** — register empty, `0 of 3` entries proven |
| Existence non-disclosure | Absence must not leak existence through uniqueness or collision feedback | **`CONTROL GAP`** — `MTI-27` specified, unproven |
| Deny-by-default read scoping | Scoped before evaluation, not filtered after | **`CONTROL GAP`** — `MTI-21` specified, unproven |
| Offboarding / erasure | Bounded to exactly one tenant's data | **`RESEARCH REQUIRED`** — conditional |
| Change control | No customer fork of core, schema, posting, authorization, event logic or isolation rules | `SUPPORTED BY EVIDENCE` as a ruling (`MTI-D-03`) |

---

## 5. SA11-F-03 — the audit function has no consolidated standards map to inherit

Searched across the corpus for a consolidated mapping of SMEsPlus to control or accounting
standards. What exists is **standards cited inside individual findings** — TAS 2 in the asset
lineage, statutory tax in P07, control expectations distributed across the invariant sets.

**This map is the first consolidation.** It is therefore incomplete by construction: it can only
consolidate standards the baseline happened to name. Standards that no package has yet
encountered are absent from it, and this map must not be read as an applicability assessment.

Determining the applicable standard set — rather than collecting the ones already mentioned —
is a scoped piece of work that has not been done. Recorded as an open obligation for the
Audit/Standards function rather than silently presented as complete.

---

## 6. What this map does not claim

- No certification is claimed.
- No compliance conclusion is drawn for any standard.
- Thai statutory items remain `HOLD / EVIDENCE REQUIRED` and are routed to the tax track.
- TAS 2 ¶12's requirement is quoted from the package that established it; the gazetted primary
  text for TAS 16 remains unretrieved and is recorded as an evidence gap rather than assumed.

---

`CP-SA-70` (standards/audit half) — **HOLD**. Two standard gaps, one of them a requirement with
no mechanism corroborated three ways; nine control gaps; and no consolidated applicability
assessment exists.

Boss remains the sole Final Approver.
