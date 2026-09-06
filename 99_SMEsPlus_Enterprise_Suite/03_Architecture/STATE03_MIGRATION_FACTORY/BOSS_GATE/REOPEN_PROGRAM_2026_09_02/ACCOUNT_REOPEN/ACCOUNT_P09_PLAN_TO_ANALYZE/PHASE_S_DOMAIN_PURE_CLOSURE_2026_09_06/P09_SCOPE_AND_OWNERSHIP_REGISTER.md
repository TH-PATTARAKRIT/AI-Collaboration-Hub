# P09_SCOPE_AND_OWNERSHIP_REGISTER

**Prompt:** `SMEPLUS-26-09-06-P09-P2A-DOMAIN-PURE-BOUNDED-CLOSURE-002` · **Phase S** · **AI EOS NOT ACTIVE**
**Layer:** 1 — clean-room. **Answers `CQ-P09-10`.** Carries forward the scope-aware constitution correction.

---

> ## ⚠ CORRECTED AFTER INDEPENDENT CHALLENGE
> Statements in this file were **contradicted by the AAS-03 challenges and re-verified against source by the author before adoption.** Corrections are marked inline; superseded wording is retained. The full list is in `P09_AAS03_INDEPENDENT_CHALLENGE_RECORD`.

---

## 1. THE GOVERNING DISTINCTION

`OWNERSHIP ≠ AVAILABILITY.` An object is *owned* by exactly one scope and may be *available* to many. The reference pattern has **no scope declaration at all**: it uses one nullable company field to mean both "this belongs to everyone" and "nobody set this".

**SO-01 — The defect is the absence of an explicit scope, not the presence of a null.** This survives from the corrected constitution unchanged, and this round found nothing against it.

---

## 2. SCOPE DETERMINATION FOR P09 OBJECTS

| Object | Reference-pattern scope carrier | P09 determination | Context required | Basis |
|---|---|---|---|---|
| **dimension type (axis)** | **none — no company field, no tenant concept**; materialises as shared physical schema | **TENANT** | tenant mandatory | a management-analysis policy carrying no financial effect |
| **dimension value** | optional company; empty = every company | **TENANT by default; COMPANY where the value denotes a legal-entity object** | tenant mandatory; company for the COMPANY subset | |
| **management record** | required, immutable, strictly scoped | **COMPANY** | tenant + company | it carries an amount attributable to a legal entity |
| **allocation instruction** | rides on the row | **TENANT as rule, COMPANY as application** | per use | |
| **assignment rule** | optional company, empty = wildcard on every selector | **TENANT**, with company as a *selector*, not ownership | tenant mandatory | |
| **obligation rule** | optional company | **TENANT**, company-qualified where the obligation is entity policy | tenant mandatory | |
| **plan (intended amount)** | ~~optional company; empty = every company~~ → **REQUIRED, defaulted, and stored down to the line** in the generation this round examined. **CONTRADICTED — CORRECTED** (EV-P09-208 §9.3): the nullable-company behaviour belongs to a **different generation** and was carried across without re-verification | **TENANT or COMPANY — declared per plan** — but note the carrier examined is unconditionally COMPANY | derived from the declaration | the determination stands as a *requirement*; it is **not** evidenced as present behaviour |
| **plan consumption figure** | derived | **the plan's scope** | derived | |
| **allocation-to-ledger postings** | company from destination journal | **COMPANY** | tenant + company | it produces financial truth |

---

## 3. THE THREE SCOPE FAILURES THAT SURVIVE

| # | Failure | Why it matters | Class |
|---|---|---|---|
| **SO-F1** | the axis is **physically global** — one tenant adding an axis changes the shared table for all | in a multi-tenant deployment, tenant isolation does not hold for the P09 primary structure | `FACT VERIFIED — P09` |
| **SO-F2** | the company-consistency check between a costed row and its dimension values is enforced on **exactly one axis** | every other axis is a runtime-created column carrying none of the platform's relational protections | `FACT VERIFIED — P09` |
| **SO-F3** | a management aggregate admits scope-empty records into **every** company's total, converted at today's rate into the reader's active company currency | an implicit, unmarked, unauthorised widening | `FACT VERIFIED — P09` |

**SO-02 — A TENANT-scoped plan consuming COMPANY-scoped actuals is legitimate and expected.** It is not a defect. What is a defect is that the widening happens **because a field is empty**, rather than because a scope was declared and an aggregation authorised.

---

## 4. THE SCOPE ROW THAT REMAINS OPEN

`S12` — a cross-company path was found that an earlier closure had not tested, and it was re-opened rather than smoothed.

**Status: `UNRESOLVED — SPECIFIC P09 EVIDENCE UNAVAILABLE`.** Closing it requires a deployment carrying all three preconditions simultaneously. Of the 19 enumerated database artefacts, **8 in-scope ones remain unread**, and any of them might carry that combination.

**Reading them is out of this prompt's bounded scope** — it is wider work, not deeper. Carried forward with its exact next action named, not silently left open.

---

## 5. PEER DEPENDENCY

The authoritative tenant/company semantics for the Account domain are being settled across P01–P11 and reconciled by P11.

- P09's determinations here are **P09's own scope analysis**.
- Marked `PEER DEPENDENCY OPEN — P11 SCOPE RECONCILIATION`.
- **P09 does not wait, does not adjudicate against another process, and has not consumed any peer's unpublished position.** P11 has published no branch.

---

## 6. DISPOSITIONS

| ID | Disposition |
|---|---|
| `SO-01`, `SO-02` | `FACT VERIFIED — CLOSED FOR CURRENT P09 EVIDENCE` |
| `SO-F1`, `SO-F2`, `SO-F3` | `FACT VERIFIED — CLOSED FOR CURRENT P09 EVIDENCE` |
| the scope table in §2 | `SUPPORTED INTERPRETATION — P09`, `PEER DEPENDENCY OPEN` |
| `S12` | `UNRESOLVED — SPECIFIC P09 EVIDENCE UNAVAILABLE` — exact action named |
