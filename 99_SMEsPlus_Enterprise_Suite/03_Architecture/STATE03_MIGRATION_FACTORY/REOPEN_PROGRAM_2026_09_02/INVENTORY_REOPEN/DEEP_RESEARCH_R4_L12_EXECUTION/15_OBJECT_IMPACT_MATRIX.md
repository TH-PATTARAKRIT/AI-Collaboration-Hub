# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 15 — Object Impact Matrix

Scope: `36 business objects, carried unchanged from the v1.0 concept model and the Menu Deep Challenge object register`
Control Level: `/L9999.9999`
Status: `MATRIX UPDATED WITH R4 FINDINGS — NOT A DATA MODEL — NOT APPROVED DESIGN — DEEP RESEARCH ONLY`

---

## 1. Basis And Lineage

This matrix does **not** create a new object set. The concept register `CN-01` .. `CN-36` and the object register `OBJ-01` .. `OBJ-36` are the same 36 business objects under two identifier schemes from two prior rounds. R4 carries both unchanged and adds only what its own forensic work established.

**This is a conceptual business model. It is not a database schema and it is not approved design.**

R4's contribution to this matrix is threefold: it confirms or corrects the identity and immutability position of specific objects from first-hand inspection; it attaches the new `R4-F-*` findings to the objects they affect; and it records which objects are affected by the three identities that do not exist.

---

## 2. Objects Materially Affected By R4 Findings

Only objects where R4 changes or strengthens the prior position are listed. Every other object carries forward unchanged.

| Object | Concept | R4 finding | Effect on the prior position |
|---|---|---|---|
| `CN-03` / `OBJ-03` | Storage place | `R4-F-09` | **Strengthened to a structural exposure.** Company assignment on a location is optional in the reference pattern. Prior rounds recorded company scoping as an application-layer concern generally; R4 identifies a specific record type where the scope may legitimately be absent. Feeds `L9-02`, `L9-05`. |
| `CN-05` / `OBJ-05` | Flow template and rule | New positive finding | Route-to-rule company consistency **is** genuinely enforced in the reference pattern — a transferable strength. Versioning (`IV-15`) is not, and remains a required divergence. |
| `CN-08` / `OBJ-08` | Product category | `R4-F-10` | **Root cause identified.** The category simultaneously owns a reporting concern, an operational put-away concern and a financial costing concern. This triple ownership is the structural root of `GAP-FS-02`, `JT-01` and `GAP-MD-13` alike. Costing method and valuation mode are **company-scoped properties** of the category. |
| `CN-09` / `OBJ-09` | Valuation policy | — | Owner remains **Joint**. `JT-01` NOT DECIDABLE. The policy-version component of the valuation fact's identity (`CN-31`) is unresolvable until `JT-01` is decided. |
| `CN-14` / `OBJ-14` | Unit group and unit | `R4-F-13` | **Confirmed and sharpened.** Cross-category conversion is refused outright — correct and transferable. Default rounding direction is **upward**, so repeated conversion inflates quantity monotonically and silently. `IV-11` confirmed necessary; rounding direction must itself be a versioned decision. |
| `CN-15` / `OBJ-15` | Packaging | `R4-D-02` | **Prior finding corrected.** An earlier round found no packaging model in the source it examined; a packaging structure with a contained base quantity **does exist** in the target generation. Non-retroactivity of contained-quantity change is a new R4 requirement. |
| `CN-16` / `OBJ-16` | Barcode format | `R4-F-12` | **Upgraded from no evidence to first-hand structure.** Plain and structured-standard nomenclatures both exist; structured patterns can encode quantity, weight, batch and expiry. A misparse yields a plausible wrong quantity **silently**. |
| `CN-17` / `OBJ-17`, `CN-18` / `OBJ-18` | Lot, Serial | `R4-F-06` | **Strengthened to a structural exposure.** Uniqueness is scoped to (identifier, product, company) with company-less identities possible, handled by a reactive cross-company duplicate check rather than prevention. `IV-04` confirmed necessary rather than merely desirable. |
| `CN-20` / `OBJ-20` | Reorder rule | `R4-F-01`, `R4-F-11` | **Two new material findings.** Uniqueness is enforced only on (product, location, company), so overlapping rules on nested locations are both permitted and both active. The shortfall computation uses the greater of minimum and maximum, so an inverted entry is silently accepted. |
| `CN-23` / `OBJ-23` | Reservation | — | **Confirmed as not a first-class fact** in the reference pattern; held as a quantity on the balance record. An adjustment can therefore silently reduce a reservation. `C-04` concurrency conflict remains unarbitrated. |
| `CN-25` / `OBJ-25` | Movement fact | `R4-F-16` component | **Identity confirmed incomplete.** The attempt component does not exist. This is the atom of Stock Truth and its identity is incomplete — the most consequential entry in `09_L8...`. |
| `CN-26` / `OBJ-26` | Place balance | `R4-F-07` | Available quantity is display-clamped at zero while true on-hand can be negative. No uniqueness constraint exists on the balance identity in the reference pattern, so duplicates are structurally possible and reconciled after the fact. `IV-02` and `IV-03` both confirmed as required divergences. |
| `CN-27` / `OBJ-27`, `CN-28` / `OBJ-28` | Count session, Adjustment | `R4-F-02` | **Separation confirmed correct.** The reference pattern gives the count no independent identity, holding it as an attribute of the balance, with no approval state. SMEsPlus separating `CN-27` from `CN-28` is a required divergence, and R4's forensic work confirms it. |
| `CN-29` / `OBJ-29` | Scrap | `R4-F-03`, `R4-F-04` | **Two absences established.** No salvage-value concept of any kind exists. The lifecycle has two states with no approval or rejection path. Salvage recovery has **no object at all** and must be originated. |
| `CN-30` / `OBJ-30` | Landed cost allocation | `R4-F-05` | Five allocation bases exist; weight- and volume-based bases silently distort when those product attributes are unmaintained. Residual-on-sold-goods behaviour is `JT-08`, Audit VETO retained. |
| `CN-31` / `OBJ-31` | Valuation fact | — | Carries a remaining quantity and remaining value consumed over time; a **negative remaining quantity** marks value released against stock not yet received. This is the mechanism behind `L13-01` retroactive cost correction. |
| `CN-34` / `OBJ-34` | Feature switch set | — | Reconfiguring a warehouse causes derived structures to be **re-created**, which is the `SAAS-04` regeneration risk. `IV-15` confirmed as the required divergence. |
| `CN-36` / `OBJ-36` | Provenance reference | `R4-F-16` component | **Confirmed still non-existent.** Must be originated. Blocks handoff element 14 and all ten L10 continuity areas. |

---

## 3. Objects Affected By The Three Non-Existent Identities

| Missing identity | Objects affected | Consequence |
|---|---|---|
| Attempt / idempotency identity (`RISK-C02`, `IV-06`) | `CN-21` proposal, `CN-22` demand, `CN-25` movement fact, `CN-31` valuation fact, `CN-35` planning run | A retry cannot be distinguished from a second genuine event on any of them. Handoff element 15 unsuppliable. |
| Provenance reference (`GAP-FS-08`, `CN-36`) | **Every migrated object** | No migrated record can prove its origin. Handoff element 14 unsuppliable. |
| Multi-tenant invariant set (`RISK-U03`) | **All 36 objects** | Company and tenant context can be carried but not guaranteed. Handoff element 10 unsuppliable as a guarantee. |

All three are **Lane A — not COGS-gated.**

---

## 4. Candidate Invariant Status After R4

The v1.0 candidate invariants `IV-01` .. `IV-15` are carried unchanged. R4 records which are now supported by first-hand evidence rather than by inference.

| Invariant | Subject | R4 evidence movement |
|---|---|---|
| `IV-01` | On hand equals total in minus total out | Unchanged |
| `IV-02` | Negative on hand only where allowed, **displayed and flagged** | **Strengthened** — `R4-F-07` confirms the reference pattern hides it |
| `IV-03` | Exactly one balance per product, place, batch, handling unit, owner | **Strengthened** — no uniqueness constraint exists in the reference pattern |
| `IV-04` | Serial unique per product per company, enforced below the application layer | **Strengthened** — `R4-F-06` confirms reactive detection rather than prevention |
| `IV-05` | Done movement fact immutable; corrections by reversing facts | Confirmed — append-only history present in the reference pattern is a genuine strength |
| `IV-06` | Stable identity making retries safe | **Confirmed absent**; now contract-blocking (`R4-F-16`) |
| `IV-07` | Movement date in an open period unless a recorded exception with grantor, reason, expiry | Unchanged; global unaudited bypass remains rejected |
| `IV-08` | One company per record, guaranteed below the application layer | **Strengthened** — `R4-F-09` identifies a record type where the scope may be absent |
| `IV-09` | Provenance reference on every migrated record | Confirmed absent |
| `IV-10` | Valuation as of a date reproducible and agreeing with the ledger after close | **Qualified** — holds at the closing boundary, not continuously |
| `IV-11` | Unit factor change never alters historical quantity | **Strengthened** — `R4-F-13` adds that rounding direction must itself be versioned |
| `IV-12` | Product-kind change while stock exists is an approved action | Unchanged; reference behaviour confirmed asymmetric |
| `IV-13` | Lot value immutable after first movement | Unchanged |
| `IV-14` | Attribute value codes immutable once used by a variant | Unchanged; `GAP-FS-03` unresolved |
| `IV-15` | Configuration versioned with effective dates, never regenerated in place | **Strengthened** — reference re-derivation behaviour confirmed |

Nine of fifteen candidate invariants now rest on first-hand evidence rather than inference. **None is closed or approved by this session.**

---

## 5. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
