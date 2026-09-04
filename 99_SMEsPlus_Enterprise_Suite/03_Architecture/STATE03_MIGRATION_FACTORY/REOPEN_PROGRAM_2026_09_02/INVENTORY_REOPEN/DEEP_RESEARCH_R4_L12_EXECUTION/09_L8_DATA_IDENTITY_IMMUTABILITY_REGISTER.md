# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 09 — L8 Data / Identity / Immutability Register

Level: `L8 — Data / Identity / Immutability`
Scope: `15 mandated entities`
Control Level: `/L9999.9999`
Status: `L8 COMPLETE FOR 15/15 ENTITIES — 3 IDENTITIES DO NOT EXIST — DEEP RESEARCH ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. Governing Rule

The Boss standard states it directly and R4 applies it without exception:

**Account code, product code, names, and labels are not sufficient canonical identity by themselves.**

This matters in a Thai SME context specifically. Product codes are frequently re-used when an item is discontinued and a similar one introduced. Names exist in two languages and drift. Supplier batch codes repeat. An identity model resting on any of these will fail in ordinary operation, not only in edge cases.

Each entity below records: the canonical identity candidate, what is mutable, what is immutable, the lineage requirement, and R4's status. Concept identifiers `CN-*` and invariants `IV-*` are carried unchanged from the v1.0 concept model.

---

## 2. The Fifteen Mandated Entities

### `L8-01` Product (`CN-11`)

- **Canonical identity:** company or tenant scope plus a system-generated stable key. The human-readable code is an attribute, not the identity.
- **Mutable:** names in both languages, descriptions, category, supplier list, images, weight, volume.
- **Immutable once stock or history exists:** the identity key itself; the base unit of measure; effectively the stock-control classification, since changing it is destructive in one direction (`INV-F-17`).
- **Lineage:** must carry a provenance reference to its origin in the legacy system (`IV-09`).
- **R4 status:** `OPEN`. The two-axis stock-control classification persists in the target generation (`L2-OBS`) and the tie-break rule (`GAP-FS-04` / `GAP-MD-10`) is undefined. Real data from an earlier round showed the reference system's own theoretical invariant violated in practice, so the ambiguity is operational, not academic.

### `L8-02` Variant (`CN-12`)

- **Canonical identity:** parent product plus the ordered set of attribute-value codes.
- **Mutable:** variant code, barcode, images.
- **Immutable once stock exists:** the attribute-value combination itself.
- **Lineage:** provenance reference required; the attribute values it was built from must remain resolvable even if archived.
- **R4 status:** `OPEN`. `IV-14` — attribute value codes immutable once used by a variant — is the containing invariant and it is not yet a decided design position. `GAP-FS-03` (variant identity when the attribute set changes after variants hold stock) remains **unresolved**; R4 has first-hand field evidence of the structure now (`L2-OBS`) but the destructive-change semantics require a live instance test that was not available.

### `L8-03` Warehouse (`CN-02`)

- **Canonical identity:** company plus a stable key. The short code is an attribute.
- **Mutable:** name, address, step configuration.
- **Immutable:** the identity key; the company assignment, in practice, since moving a warehouse between companies re-interprets every movement it ever held.
- **Lineage:** provenance reference required.
- **R4 status:** `OPEN`. `L2-OBS` confirms that changing the step configuration causes derived structures to be re-created, which is the `SAAS-04` regeneration risk. `IV-15` — version configuration, never regenerate in place — is the required divergence. Separately, a warehouse must never be equated with a Thai tax branch (`TH-HOLD-06`, `GAP-MD-15`) — an identity distinction, not merely a naming one.

### `L8-04` Location (`CN-03`)

- **Canonical identity:** warehouse plus place path plus kind — not the name, which staff change freely.
- **Mutable:** name, barcode, storage category, counting frequency.
- **Immutable once movements exist:** the kind, because it determines the financial meaning of every movement that crossed it.
- **Lineage:** provenance reference required.
- **R4 status:** `OPEN` with a **material R4 finding**. `R4-F-09`: the company assignment is optional. An identity that may legitimately have no company cannot be relied on to carry company context, which breaks handoff element 10 (`05` §4). Carried to L9.

### `L8-05` Operation type (`CN-04`)

- **Canonical identity:** warehouse plus code.
- **Mutable:** name, print options, backorder policy.
- **Immutable:** the operation class; the numbering sequence, in the sense that changing it must preserve continuity and non-reuse of already-issued numbers.
- **Lineage:** provenance reference required.
- **R4 status:** `OPEN`. Prior evidence records classification coupled to string literals, which makes the class fragile as an identity component. `TH-HOLD-09` (delivery document to tax invoice linkage and numbering conventions) is **held**; R4 makes no Thai statutory claim.

### `L8-06` Route (`CN-05`)

- **Canonical identity:** company plus template identity plus **version**.
- **Mutable:** name, applicability scope.
- **Immutable:** a published version. A change creates a new version; it does not edit the old one.
- **Lineage:** every generated operation must resolve to the route version in force at generation time.
- **R4 status:** `OPEN`. Versioning is a design requirement (`IV-15`), not an observed reference behaviour. Without it, an operation generated last month cannot be explained against this month's configuration.

### `L8-07` Rule (`CN-05`)

- **Canonical identity:** route version plus sequence plus company.
- **Mutable:** delay, propagation options.
- **Immutable:** a published version.
- **Lineage:** every generated operation must name the rule instance that produced it (`P-06`).
- **R4 status:** `OPEN`. `L2-OBS` confirms company consistency between a route and its rules is genuinely enforced — a transferable strength. Versioning is not.

### `L8-08` Stock movement — the document (`CN-24`)

- **Canonical identity:** operation type plus document number, within company.
- **Mutable:** while in draft only.
- **Immutable:** once completed.
- **Lineage:** originating demand identity; the rule identity where generated automatically.
- **R4 status:** `OPEN`. The document number's continuity and non-reuse is a Thai audit expectation and is bound to `L8-05`.

### `L8-09` Movement line — the fact (`CN-25`)

- **Canonical identity:** document line plus **attempt identity**.
- **Mutable:** nothing once done. `P-02` / `IV-05`.
- **Immutable:** everything. Corrections are new reversing facts (`INV-F-40`).
- **Lineage:** original event linkage; reversal linkage; migration or replay batch identity.
- **R4 status:** **`IDENTITY DOES NOT EXIST`.** The attempt component of the identity is exactly `RISK-C02` / `IV-06` / `GAP-MD-21` — no stable identity making a retry safe exists in the reference pattern, and none has been designed. This is the **single most consequential entry in this register**: the movement fact is the atom of Stock Truth, and its identity is incomplete. Severity **BLOCKING**, owner **Boss**, **Lane A — not COGS-gated**. See `07` §5 for the new evidence R4 supplies toward the `C-02` decision.

### `L8-10` Lot (`CN-17`)

- **Canonical identity:** company plus product plus lot value.
- **Mutable:** expiry and alert dates, notes.
- **Immutable:** the identity triple; the batch's value after its first movement (`IV-13`).
- **Lineage:** origin document; supplier batch reference.
- **R4 status:** `OPEN` with a **material R4 finding**. `R4-F-06`: `L2-OBS` confirms the scope is (identifier, product, company) and that company-less identities are possible, requiring a reactive cross-company duplicate check rather than prevention. `IV-04` is confirmed as necessary.

### `L8-11` Serial (`CN-18`)

- **Canonical identity:** company plus product plus serial value, unique.
- **Mutable:** notes, warranty attributes.
- **Immutable:** the identity triple.
- **Lineage:** origin document; the single movement chain it participated in.
- **R4 status:** `OPEN`. Same scoping finding as `L8-10`. A serial is a stronger claim than a batch — it asserts a unique physical object — so a collision is correspondingly more damaging.

### `L8-12` Package / handling unit (`CN-19`)

- **Canonical identity:** handling-unit code, plus a history snapshot of its contents at each movement.
- **Mutable:** current contents.
- **Immutable:** the historical snapshots.
- **Lineage:** provenance reference; migration disposition.
- **R4 status:** `OPEN`. `GAP-FS-05` / `GAP-MD-26` — whether handling units migrate live, as history, or both — has been undecided since an early round and R4 does not decide it. The snapshot requirement is what makes "what was in that box when it shipped" answerable later, and R4 records it as a design requirement.

### `L8-13` Inventory adjustment (`CN-28`) and count session (`CN-27`)

- **Canonical identity:** adjustment number within company; count session identity separately.
- **Mutable:** while in draft only.
- **Immutable:** once applied — reason, approver, counted quantity, both dates.
- **Lineage:** the count session it arose from; the movement facts it produced.
- **R4 status:** `OPEN`. `R4-F-02`: the reference pattern gives the count no independent identity at all, holding it as an attribute of the balance. SMEsPlus separating `CN-27` from `CN-28` is therefore a required divergence and is confirmed correct by R4's forensic work.

### `L8-14` Scrap (`CN-29`)

- **Canonical identity:** scrap number within company.
- **Mutable:** while in draft only.
- **Immutable:** once done — reason, authoriser, quantity, batch, destination.
- **Lineage:** the movement facts produced; the destruction evidence where claimed.
- **R4 status:** `OPEN`. No approval identity exists to record because no approval state exists (`R4-F-04`). Salvage recovery has **no identity at all** because the concept does not exist (`R4-F-03`).

### `L8-15` Landed cost (`CN-30`) and valuation event (`CN-31`)

- **Canonical identity:** cost document plus target line for the allocation; movement plus policy version for the valuation event.
- **Mutable:** while in draft only.
- **Immutable:** once done.
- **Lineage:** the cost bill; the goods still on hand versus already gone at allocation time; the costing policy version in force.
- **R4 status:** `OPEN — DEPENDENCY LOCKED`. The **policy version** component of the valuation event's identity is unresolvable while `JT-01` (valuation policy owner) is NOT DECIDABLE — an identity cannot cite a policy version if the concept that owns policy is undecided. `L2-OBS` supplies the fact that costing method and valuation mode are company-scoped properties of the product category; the choice remains Joint.

---

## 3. Identities That Do Not Exist

Three required identities have no implementation and no design. All three are **Lane A — not COGS-gated** — which means they are actionable now and are blocked only by not having been commissioned.

| Identity | Entity | Register lineage | Consequence if absent |
|---|---|---|---|
| Attempt / idempotency identity | `L8-09` movement fact | `RISK-C02`, `IV-06`, `GAP-FS-06`, `GAP-MD-21` | A retry cannot be distinguished from a second genuine event. Handoff element 15 unsuppliable, so **no material handoff can be declared verified** under the Boss-approved contract. |
| Provenance reference | Every migrated entity (`CN-36`) | `GAP-FS-08`, `GAP-MD-27` | No migrated record can prove where it came from. Handoff element 14 unsuppliable. Cutover reconciliation unprovable. |
| Multi-tenant invariant set | All entities | `RISK-U03`, `GAP-FS-10`, `U-03` | Company and tenant context can be carried but not *guaranteed*. Handoff element 10 unsuppliable as a guarantee. |

R4 records these three together deliberately. Individually each has been carried for several rounds as one item among sixty. Together they are the reason the Boss-approved 16-element handoff contract cannot presently be satisfied by any Inventory handoff, which is finding `R4-F-16` and the lead item in the PMO recommendation.

---

## 4. Immutability Summary

| Immutability rule | Source | R4 status |
|---|---|---|
| Completed movement facts are immutable; corrections are reversing facts | `P-02`, `IV-05` | Confirmed as sound; append-only history is present in the reference pattern and is a genuine strength |
| On-hand is derived and never edited | `P-03` | Confirmed as required; `N-A13-01` remains an unread lead suggesting a write path may exist |
| A batch's value is immutable after first movement | `IV-13` | Carried; not yet a decided position |
| Unit conversion factor changes never alter historical quantity | `IV-11` | Confirmed necessary; `R4-F-13` (default upward rounding) makes the direction itself a versioned decision |
| Attribute value codes immutable once used by a variant | `IV-14` | Carried; `GAP-FS-03` unresolved |
| Configuration is versioned with effective dates, never regenerated in place | `IV-15` | Confirmed as a required divergence; `L2-OBS` shows the reference re-derives structures on warehouse reconfiguration |
| Packaging contained quantity change must not re-interpret history | R4, `INV-F-34` | New in R4; same principle as `IV-11` |
| A location's kind change must not re-interpret completed movements | R4, `INV-F-28` | New in R4; `L5-08` depends on it |

---

## 5. L8 Coverage Result

| Measure | Result |
|---|---:|
| Mandated entities | 15 |
| Given full L8 treatment | 15 |
| Entities whose canonical identity is defined and adequate | 12 |
| Entities whose identity is incomplete or does not exist | 3 — `L8-09`, plus the provenance and tenancy components affecting all |
| Immutability rules confirmed or newly raised | 8 |
| Entities closed by this session | **0** |

---

## 6. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
