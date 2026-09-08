# SA10 — TENANT AND COMPANY BOUNDARY MATRIX

Status: **HOLD** — the strongest specification in the SMEsPlus baseline, and none of it is proven.

---

## 1. The specification that exists

The Inventory multi-tenant invariant set is the most developed isolation specification in the
programme. Two live versions:

| Version | Branch @ SHA | Status line, verbatim |
|---|---|---|
| R1 | `design/inventory-multitenant-invariant-set-2026-09-04-001` @ `dcb92278` | `50 INVARIANTS SPECIFIED — 0 PROVEN — DESIGN / SPECIFICATION ONLY — NOT DEVELOPMENT FINAL GATE` |
| R2 conformed | `design/inventory-mti-ruling-conformance-2026-09-05-001` @ `bd096ffa` | `50 CARRIED + 8 ADDED = 58 INVARIANTS SPECIFIED — 0 PROVEN — 14 RE-SPECIFIED — DESIGN / SPECIFICATION ONLY — NOT DEVELOPMENT FINAL GATE` |

Context tuple: `CTX = (tenant, company, warehouse?, location?)`, with tenant and company the
**context spine** — never optional.

### 1.1 The nine invariant families

| Family | Subject | Count |
|---|---|---|
| A | Context spine — every record, value, event, job and emitted fact resolves to exactly one `CTX` | 6 |
| B | Object anchors — warehouse, location, operation type, route, product, lot/serial, package, reordering rule, movement, derived state | 10 |
| C | Enforcement — store-level, no unaudited privileged bypass, continuous conformance control, fail closed, deny by default on read, closed cross-context register | 6 |
| D | Visibility and derivation — no cross-boundary aggregation without a grant; **absence must not leak existence** | 6 |
| E | Execution boundary — single-context execution; deferred work carries `CTX` **and the authority it was scheduled under** | 5 |
| F | Configuration and template — platform template and tenant configuration are distinct classes; config copied at provisioning, versioned, never regenerated in place | 4 |
| G | Identity, event, audit, replay — immutable events, physical event date and entry date as two distinct values, replay never re-resolves `CTX` from current configuration | 5 |
| H | Handoff carriage — every emitted fact carries `CTX` **and an attestation** naming which invariants guaranteed it | 4 |
| I | Lifecycle — new tenant starts with zero inherited data; company deactivation **freezes, never deletes** | 4 |

R2 adds eight more, including that authorization is a **four-axis tuple** where no axis
substitutes for a wider one, and that every invariant states the isolation topology it is
scoped to.

---

## 2. Boss rulings binding this matrix

| Ruling | Decision, quoted | Effect |
|---|---|---|
| `MTI-D-01` Product master scope | `OPTION B — Company-owned Product Master / tenant-company scoped product identity`; *"Duplication across tenants/companies is acceptable and must not be treated as a defect"* | **Inverts the published `MTI-11`.** Two records in two companies sharing a code, name, barcode or unit are two different business objects; the similarity is never a defect or a cleanup candidate. The company-enablement clause of the published `MTI-11` is void |
| `MTI-D-02` Authorization granularity | `Company + Warehouse + Operation-Type` | A user authorised for one warehouse is not authorised for every warehouse in the company; the same for operation type. Background jobs must carry explicit context on all four axes |
| `MTI-D-03` Tenant-changeable boundary | `Platform-owned Core + Tenant Config Overlay` | No customer-specific change may fork core source, schema, posting behaviour, authorization behaviour, immutable event logic or isolation rules. A `Private Company` operating model exists for extreme cases and *"is not a bypass for evidence, authorization, audit, tenant isolation, or Boss approval"* |
| `BD-ACC-02` | Company-scoped statutory tax | No cross-company statutory posting, offsetting or filing |

Conformance to these three rulings required **32 deltas across 5 matrix rows, 14 invariants,
3 register entries, 2 handoff-field additions, 1 new enforcement-point class and 8 new
invariants** — larger than the veto that demanded it.

---

## 3. SA10-F-01 — the strongest specification in the programme, with zero proofs

Every counted proof obligation in the isolation lineage stands at zero, and has stayed at zero
across every round including the most recent:

> `0 of 8` L9 proofs · `0 of 22` cross-proof scenarios · `0 of 10` material handoffs
> contract-compliant · `0 of 12` Joint decisions ready · `0 of 78` Thai validations ·
> `0 of 13` enforcement surfaces verified · `0 of 41` functions verified against any axis ·
> `0 of 60` proof requirements executable · **`0` findings closed, `0` capabilities built,
> `0` vetoes discharged.**

Also recorded: `0 of 52` negative access tests executable *"because no implementation exists"*,
and `0 of 3` cross-context register entries proven — the register being, in its own words,
*"the only door, and it is currently empty"*.

**Phase SA position.** This is not a criticism of the specification, which is unusually good.
It is a statement about what Phase SA may rely on: **a specification is not a control.** The
isolation guarantees may be cited as *design intent* and may not be cited as *assurance*.

## 4. SA10-F-02 — one context guarantee moved from unsuppliable to specified, and that is all that moved

Of the three cross-module handoff elements that Inventory cannot supply, element 10 —
*which company / tenant*, **as a guarantee** — moved to `Specified, not built, not verified`.
Elements 14 (migration/replay batch identity) and 15 (deterministic idempotency identity) did
not move.

The controlling standard, quoted from the isolation proof matrix:

> an element must be **known, traceable and evidence-backed**; a specification satisfies none
> of the three on its own.

**All three are recorded as not caused by the accounting dependency.** They would remain open
even if every accounting question were answered tomorrow. For Phase SA this matters because it
means the isolation gap is **not downstream of the accounting gap** and cannot be closed by
resolving it.

## 5. SA10-F-03 — a tenant-isolation defect exists in the estate but cannot currently fire

The manufacturing lineage records that company-dependent accounts are resolved in the **user's**
company rather than the transaction's — classified Critical, tenant isolation. Its measured
reachability is nil: both manufacturing databases are single-company, so the defect cannot
currently express itself.

Phase SA records both halves together. A defect that cannot fire today is not thereby safe: it
is a defect whose trigger is *becoming multi-company*, which is precisely what SMEsPlus is.
Severity ranking must use the target architecture, not the reference deployment's accident.

## 6. Cross-company relationship register

`MTI-22` establishes a closed, enumerated register as the **only** permitted cross-company path,
and `MTI-44` requires that no handoff fact spans contexts — an inter-company movement emits two
single-context facts linked by a register identity.

**Phase SA adopts both as SMEsPlus determinations**, with independent rationale: under
`BD-ACC-02` statutory tax is company-scoped, so a fact that spans companies has no single
statutory owner and cannot be filed. The register is what makes cross-company legitimate
without making it implicit.

Status: `SPECIFIED — CONDITIONAL`, register currently empty, `0 of 3` entries proven.

---

## 7. Boundary status summary

| Boundary | Specified | Ruled | Proven |
|---|---|---|---|
| Tenant isolation | Yes — 58 invariants | Yes | **No — 0 proofs** |
| Company boundary | Yes | Yes — `MTI-D-01`, `BD-ACC-02` | **No** |
| Warehouse / operation-type authorization | Yes — `MTI-D-02`, `CF-I-01` | Yes | **No — 0 of 13 enforcement surfaces** |
| Platform vs tenant configuration | Yes — Family F, `MTI-D-03` | Yes | **No** |
| Cross-company relationship register | Yes — `MTI-22`, `MTI-44` | — | **No — register empty** |
| Context carriage on handoffs | Yes — `MTI-43`, `MTI-45` | — | **No — 0 of 10 handoffs compliant** |

---

`CP-SA-70` (tenant/company half) — **HOLD**. The boundary is the best-specified area in the
baseline and the least proven. Phase SA cites it as design intent only.

Boss remains the sole Final Approver.
