# [SMEPLUS-26-09-04-INV-MT-INVARIANT-SET-001]
# 09 — Data Identity, Immutability And Replay Requirements

Levels: `L8 — data / identity / immutability` and `L10 — migration / historical continuity`
Control Level: `/L9999.9999`
Status: `CONTEXT COMPONENT OF IDENTITY SPECIFIED FOR 15 OF 15 ENTITIES — 2 OF 3 MISSING IDENTITIES REMAIN ABSENT — NOT DEVELOPMENT FINAL GATE`

---

## 1. The Governing Rule, Carried Unchanged

The Boss standard applies without exception, and it is the reason this file exists in the form it does:

> **Account code, product code, names and labels are not sufficient canonical identity by themselves.**

The L8 register explains why this matters in a Thai SME specifically: product codes are re-used when an item is discontinued, names exist in two languages and drift, and supplier batch codes repeat. This session adds the multi-tenant corollary, which no prior round states:

> **A context value that is carried but not guaranteed is not part of an identity either.** An identity whose company component may be absent, defaulted or re-derived is as unreliable as one resting on a re-used code.

---

## 2. The Context Component Of Identity — 15 Of 15 Entities

The 15 mandated entities are carried unchanged from `09_L8_DATA_IDENTITY_IMMUTABILITY_REGISTER.md`. This file adds only the context component and its immutability. Every other aspect of each identity is carried, not restated and not altered.

| Entity | Context component of canonical identity | Immutable from | Invariants |
|---|---|---|---|
| `L8-01` Product (`CN-11`) | `tenant` for the definitional identity; `company` on every attachment | Creation (tenant); first enablement (company) | `MTI-11`, `MTI-06` |
| `L8-02` Variant (`CN-12`) | Follows its parent product | As parent | `MTI-11` |
| `L8-03` Warehouse (`CN-02`) | `company`, mandatory | First completed movement in the warehouse | `MTI-07`, `MTI-06` |
| `L8-04` Location (`CN-03`) | `company`, **derived from the warehouse**, mandatory | Creation — the anchor is structural, not an attribute | `MTI-08`, `MTI-04` |
| `L8-05` Operation type (`CN-04`) | `warehouse`, therefore `company` | First issued document number | `MTI-09` |
| `L8-06` Route (`CN-05`) | `company` plus template identity plus **version** | Version publication | `MTI-10`, `MTI-36` |
| `L8-07` Rule (`CN-05`) | Route version plus sequence plus `company` — **and the rule's company must equal the route's** | Version publication | `MTI-10` |
| `L8-08` Movement document (`CN-24`) | `company` plus operation type plus number | Completion | `MTI-15`, `MTI-09` |
| `L8-09` Movement line / fact (`CN-25`) | `company` — **plus the attempt identity, which does not exist** | Completion | `MTI-15` — see §3 |
| `L8-10` Lot (`CN-17`) | `(tenant, company, product, value)` — company-less prohibited | Creation | `MTI-12` |
| `L8-11` Serial (`CN-18`) | Same tuple. A serial asserts a unique physical object, so a collision is correspondingly more damaging | Creation | `MTI-12` |
| `L8-12` Package / handling unit (`CN-19`) | `company`; content snapshots carry the `CTX` in force at snapshot time | Each snapshot, at the moment it is taken | `MTI-13` |
| `L8-13` Adjustment (`CN-28`) and count session (`CN-27`) | `company` plus number, separately for each | Application | `MTI-33`, `MTI-38` |
| `L8-14` Scrap (`CN-29`) | `company` plus number | Completion | `MTI-33`, `MTI-38` |
| `L8-15` Landed cost (`CN-30`) and valuation fact (`CN-31`) | `company` on both; the valuation fact additionally requires a **policy version**, which is unresolvable | Completion | `MTI-16` — see §3.3 |

---

## 3. The Three Identities That Do Not Exist — Position After This Session

R4 records three required identities with no implementation and no design. This session addresses **one of the three**, and only partly.

| Identity | Before | After This Session | Remaining |
|---|---|---|---|
| **Multi-tenant context guarantee** (`RISK-U03`, all entities) | Carried but not guaranteed | **Specified as a guarantee**, with anchors, layers, controls, acceptance criteria and an attestation field (`HF-CTX-06`) | Implementation and independent verification. **`RISK-U03` remains open** |
| **Attempt / idempotency identity** (`RISK-C02`, `L8-09`) | Does not exist | **Unchanged — does not exist.** `MTI-31` supplies run scoping and mutual exclusion within a context; it supplies no identity | Rank 2 of `04` §4. Severity ruling `C-02` outstanding. **Not in this authorization** |
| **Provenance reference** (`GAP-FS-08`, `CN-36`, every migrated entity) | Does not exist | **Unchanged — does not exist.** `MTI-42` prohibits inferring context at migration; it cannot evidence what was assigned | Rank 3 of `04` §4. **Not in this authorization** |

### 3.1 `L8-09` remains the most consequential entry, and this session does not change that

The L8 register names the movement fact the atom of Stock Truth and records its identity as incomplete. That assessment is carried unchanged. Adding a guaranteed company component to an identity that still cannot distinguish a retry from a second genuine event **improves the identity without completing it**.

Stated as a rule for downstream readers: **a guaranteed context makes a duplicate attributable; it does not make it detectable.** Two identical movement facts in the same company, both correctly contextualised, remain indistinguishable.

### 3.2 The interaction that must not be assumed away

`MTI-41` requires a replay to reproduce the identical `CTX` on every resulting record, and never to re-resolve context from current configuration. That is specifiable and is specified. But a replay in a system without an attempt identity produces duplicate records whose context is individually correct and collectively wrong — and `MTI-19`'s conformance control would report **no breach**, because every row conforms.

**Context conformance and duplicate freedom are independent properties.** Neither implies the other, and this package supplies only the first.

### 3.3 The valuation fact's identity is doubly blocked

`L8-15` requires a policy version as part of the valuation event's identity. The L8 register records that this is unresolvable while `JT-01` — which concept owns valuation policy — is **NOT DECIDABLE**. The context component is specified here; the policy-version component is not, and carries:

`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`

---

## 4. Immutability Requirements

| Rule | Source | Position |
|---|---|---|
| Completed movement facts are immutable; corrections are reversing facts | `P-02`, `IV-05`, `INV-F-40` | Carried unchanged. Extended: **a correction may not change `CTX`** (`MTI-39`, `MTI-40`). A context change is a migration act, never a correction |
| On-hand is derived and never edited | `P-03` | Carried. Extended: a derived value carries the `CTX` of its inputs (`MTI-23`). `N-A13-01` remains an **unread lead** and this session did not read it |
| Configuration is versioned with effective dates, never regenerated in place | `IV-15` | Carried into `MTI-36`. Extended: regeneration is also the bulk mechanism by which company-less derived records appear (`MTA-01`) |
| One company per record, guaranteed below the application layer | `IV-08` | This package **is** the expansion of `IV-08` — `MTI-04`, `MTI-05`, `MTI-17` |
| Traceable identity unique per product per company, enforced below the application layer | `IV-04` | Carried into `MTI-12`, with the non-confusability rule added (`MTI-F-01`) |
| A location's kind change must not re-interpret completed movements | R4, `INV-F-28` | Carried. `MTI-08` adds that the kind is versioned and the change is an approved, evented act |
| **A record's tenant and company are immutable once it has participated in any completed act** | **`ORIGINATED`** | `MTI-06`. This is the immutability rule this session adds, and it is what makes `HF-CTX-05` meaningful — an anchor path that could be rewritten afterwards would evidence nothing |

---

## 5. Event And Audit Requirements

| Requirement | Content | Invariant |
|---|---|---|
| Event completeness | Every context-bearing act emits an immutable event carrying full `CTX`, actor, authority relied on, **physical event date and entry date as two distinct values**, and an evidence reference | `MTI-38` |
| Event context immutability | An event's `CTX` is immutable; an event is never edited and never deleted; a correction is a new linked event | `MTI-39` |
| Anchor change auditability | Any change to a context anchor is itself an evented, approved act with before and after values | `MTI-40` |
| Authority auditability | The authority relied on, including any `MTI-18` elevation grant, is recorded on the event and is reachable afterwards | `MTI-18`, `MTI-38` |
| Control evidence retention | The conformance control's runs — scope, timestamp, result — are retained, context-scoped and inspectable, and constitute the element 16 evidence for the context portion of a handoff | `MTI-19`, `MTI-50` |
| Audit visibility scoping | The audit trail is itself context-scoped. An auditor working in one company does not see another's trail except under an `XCR-02` grant | `MTI-21`, `MTI-25` |

**The two-date requirement is not new** — `INV-F-07` and handoff element 3 already require it. It is restated because backdating is routine in a Thai SME, and `R4-F-08` records that ordering movement history by entry sequence and by effective date give different running balances. Any context-conformance evidence that does not state which date it was evaluated against is not reproducible.

---

## 6. Replay And Migration Requirements — L10

The ten mandated continuity areas are carried unchanged. This file states only the **context** requirement in each and does not touch the others.

| Area | Context requirement | Status |
|---|---|---|
| `L10-01` Opening stock | Every opening balance row carries an explicitly assigned, evidenced `CTX`; never inferred | `SPECIFIED — RANK 3 DEPENDENT`; value half held (`JT-11` / `G-5`) |
| `L10-02` Historical movement | Migrated movements carry the `CTX` in force **at the time of the original event**, not the current configuration | `SPECIFIED — RANK 2 DEPENDENT` — replay without an attempt identity is unsafe |
| `L10-03` Lot and serial history | Legacy batch identities are resolved to a company **before** import, never after | `SPECIFIED` — directly serves `R4-F-23` |
| `L10-04` Product identity continuity | A legacy product resolves to exactly one product, and its company enablements are assigned explicitly | `SPECIFIED — CONDITIONAL (`MTI-D-01`)` |
| `L10-05` Warehouse and location continuity | Company derived from the warehouse structure as built, never from a name match. **Location kind assigned deliberately** | Context half `SPECIFIED`; the **kind** half is `R4-F-24`, a financial-meaning attribute, **not addressed here** |
| `L10-06` Valuation continuity | Cost layers carry `CTX`; matching never crosses a company | `SPECIFIED — VALUE HELD` — `JT-01`, `JT-02` |
| `L10-07` Cutover reconciliation | Reconciliation is performed and certified **per company**, and a group total is a sum of certified per-company results, never a substitute for them | Quantity half `SPECIFIED` — serves `R4-F-25`; value half held |
| `L10-08` Migration exception treatment | A quarantined record retains its assigned `CTX` and is **counted** in its company's reconciliation as an explicit exception, never omitted | `SPECIFIED` |
| `L10-09` Legacy reference quarantine | Legacy identifiers are readable and never authoritative, and are themselves context-scoped. **A provenance mapping is data, never design inheritance** — a clean-room obligation as well as a migration one | `SPECIFIED — RANK 3 DEPENDENT` |
| `L10-10` Evidence lineage | Every migration decision, transform and exception carries `CTX` and is reachable after go-live | `SPECIFIED — RANK 3 DEPENDENT` — element 14 unsuppliable |

### 6.1 `L10-07` carries the one available opportunity, and it is a real one

`R4-F-25` records that quantity-side cutover reconciliation is achievable independently of the value side and should not be deferred behind it. The context requirement makes that sharper: **per-company certification is what makes the quantity certificate meaningful.** A group-level quantity reconciliation that balances overall while two companies are individually wrong in opposite directions is not a reconciliation — it is the arithmetic that hides one.

This is Inventory-owned, not COGS-gated, and specifiable now. It is carried to `13` as a recommended action.

---

## 7. Coverage Result

| Measure | Result |
|---|---:|
| L8 entities given a context identity component | **15 of 15** |
| L10 continuity areas given a context requirement | **10 of 10** |
| Missing identities addressed by this session | **1 of 3** — and that one is specified, not built |
| Missing identities unchanged | **2 of 3** — ranks 2 and 3, outside this authorization |
| Immutability rules carried unchanged | 6 |
| Immutability rules originated here | 1 — `MTI-06` |
| L10 areas whose context half is unblocked | 4 — `L10-03`, `L10-05` (context only), `L10-07` (quantity), `L10-08` |
| Items closed | **0** |

---

## 8. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
